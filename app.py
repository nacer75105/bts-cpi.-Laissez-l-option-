# -*- coding: utf-8 -*-
"""
BTS CPI — Application de révision et de calcul
Conception de Produits Industriels — 1re année

Lancement :  streamlit run app.py
"""

import json
import math
import os
import random
from datetime import datetime

import pandas as pd
import streamlit as st

try:
    from donnees import iso286, materiaux as mat, quiz as qz
    from donnees.cours_bloc_1_2 import BLOC_1, BLOC_2
    from donnees.cours_bloc_3_4 import BLOC_3, BLOC_4
    from donnees.cours_bloc_5_6 import BLOC_5, BLOC_6
    from cours_bloc_7_8 import BLOC_7, BLOC_8
    from cours_bloc_9_10 import BLOC_9, BLOC_10
    from cours_bloc_11_12 import BLOC_11, BLOC_12
    from cours_bloc_13_14 import BLOC_13, BLOC_14
except ModuleNotFoundError:
    # Fichiers de donnees places a la racine (a plat)
    import iso286
    import materiaux as mat
    import quiz as qz
    from cours_bloc_1_2 import BLOC_1, BLOC_2
    from cours_bloc_3_4 import BLOC_3, BLOC_4
    from cours_bloc_5_6 import BLOC_5, BLOC_6
    from cours_bloc_7_8 import BLOC_7, BLOC_8
    from cours_bloc_9_10 import BLOC_9, BLOC_10
    from cours_bloc_11_12 import BLOC_11, BLOC_12
    from cours_bloc_13_14 import BLOC_13, BLOC_14
BLOCS = [BLOC_1, BLOC_2, BLOC_3, BLOC_4, BLOC_5, BLOC_6, BLOC_7, BLOC_8, BLOC_9, BLOC_10, BLOC_11, BLOC_12, BLOC_13, BLOC_14]
FICHIER_PROGRESSION = os.path.join(os.path.dirname(__file__), "progression.json")

st.set_page_config(page_title="BTS CPI — Révisions", page_icon="⚙️", layout="wide")


# ===========================================================================
# PROGRESSION (persistance locale)
# ===========================================================================

def charger_progression():
    if os.path.exists(FICHIER_PROGRESSION):
        try:
            with open(FICHIER_PROGRESSION, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return {"fiches_lues": [], "resultats_quiz": [], "notes": {}}


def sauver_progression(p):
    try:
        with open(FICHIER_PROGRESSION, "w", encoding="utf-8") as f:
            json.dump(p, f, ensure_ascii=False, indent=2)
    except OSError:
        st.warning("Impossible d'enregistrer la progression (droits d'écriture).")


if "progression" not in st.session_state:
    st.session_state.progression = charger_progression()

P = st.session_state.progression


# ===========================================================================
# STYLE
# ===========================================================================

st.markdown("""
<style>
  .bloc-titre {
      background: linear-gradient(90deg, #1f4e79 0%, #2e75b6 100%);
      color: white; padding: 14px 18px; border-radius: 8px; margin-bottom: 6px;
  }
  .fiche-meta { color:#555; font-size:0.88em; margin-bottom:14px; }
  .ok-box  { background:#e7f5e9; border-left:5px solid #2e7d32; padding:12px; border-radius:4px; }
  .ko-box  { background:#fdecea; border-left:5px solid #c62828; padding:12px; border-radius:4px; }
  .info-box{ background:#e8f1fa; border-left:5px solid #1f4e79; padding:12px; border-radius:4px; }
  .warn-box{ background:#fff6e5; border-left:5px solid #ef6c00; padding:12px; border-radius:4px; }
  div[data-testid="stMetricValue"] { font-size: 1.5rem; }
</style>
""", unsafe_allow_html=True)


# ===========================================================================
# NAVIGATION
# ===========================================================================

st.sidebar.title("⚙️ BTS CPI")
st.sidebar.caption("Conception de Produits Industriels — 1re année")

PAGE = st.sidebar.radio(
    "Navigation",
    ["🏠 Tableau de bord",
     "📚 Cours (18 fiches)",
     "🎯 Quiz interactif",
     "📐 Calculateur d'ajustements ISO",
     "🔧 Calculateurs RDM",
     "🧱 Base matériaux",
     "📊 Ma progression"],
    label_visibility="collapsed",
)

st.sidebar.divider()
nb_fiches = sum(len(b["fiches"]) for b in BLOCS)
lues = len(set(P["fiches_lues"]))
st.sidebar.progress(lues / nb_fiches if nb_fiches else 0)
st.sidebar.caption(f"Fiches lues : {lues}/{nb_fiches}")


# ===========================================================================
# PAGE : TABLEAU DE BORD
# ===========================================================================

if PAGE == "🏠 Tableau de bord":
    st.title("Tableau de bord")
    st.markdown("Programme de 1re année de BTS CPI : cours, exercices corrigés et outils de calcul.")

    s = qz.stats()
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Blocs de cours", len(BLOCS))
    c2.metric("Fiches détaillées", nb_fiches)
    c3.metric("Questions de quiz", s["total"])
    c4.metric("Matériaux référencés", len(mat.MATERIAUX))

    st.divider()
    st.subheader("Les six blocs du programme")

    for bloc in BLOCS:
        fiches_bloc = [f"{bloc['id']}#{f['id']}" for f in bloc["fiches"]]
        lues_bloc = sum(1 for f in fiches_bloc if f in P["fiches_lues"])
        with st.container(border=True):
            col_a, col_b = st.columns([5, 1])
            with col_a:
                st.markdown(f"**{bloc['titre']}**")
                st.caption(bloc["resume"])
                st.caption(" · ".join(f"{f['id']} {f['titre']}" for f in bloc["fiches"]))
            with col_b:
                st.metric("Lues", f"{lues_bloc}/{len(bloc['fiches'])}")

    st.divider()
    st.subheader("Par où commencer ?")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="info-box">
        <b>1. Lire les fiches dans l'ordre</b><br>
        Chaque fiche contient le cours, les formules, un cas industriel réel et un exercice
        de type examen entièrement corrigé.
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="info-box">
        <b>2. Se tester au quiz</b><br>
        Les questions marquées « Piège » correspondent aux erreurs les plus fréquentes
        en devoir surveillé. Chaque réponse est expliquée.
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="info-box">
        <b>3. Vérifier ses calculs</b><br>
        Les calculateurs servent à contrôler un résultat obtenu à la main —
        pas à le remplacer. Toujours poser le calcul avant.
        </div>""", unsafe_allow_html=True)

    st.divider()
    st.subheader("Les cinq réflexes à acquérir cette année")
    st.markdown("""
| # | Réflexe | Pourquoi |
|---|---|---|
| 1 | **Toujours vérifier résistance ET rigidité** | Tantôt l'une, tantôt l'autre dimensionne. Sur les pièces longues, c'est presque toujours la rigidité. |
| 2 | **E ≠ Re** | Tous les aciers ont E ≈ 210 GPa. Changer de nuance ne réduit jamais une flèche. |
| 3 | **Lettre = position, chiffre = largeur** | En ISO 286, l'écart fondamental dépend de la lettre seule, jamais du grade. |
| 4 | **Ne jamais resserrer une tolérance « par sécurité »** | Passer de IT11 à IT7 multiplie le coût par 3 à 5. On resserre parce que la fonction l'exige. |
| 5 | **Modéliser pour la modification à venir** | Une esquisse bleue est une bombe à retardement. Contraindre à 100 %, ancrer sur les plans de référence. |
""")


# ===========================================================================
# PAGE : COURS
# ===========================================================================

elif PAGE == "📚 Cours (18 fiches)":
    st.title("Cours")

    noms_blocs = [b["titre"] for b in BLOCS]
    choix_bloc = st.selectbox("Bloc", noms_blocs)
    bloc = BLOCS[noms_blocs.index(choix_bloc)]

    st.markdown(f'<div class="bloc-titre"><b>{bloc["titre"]}</b><br>'
                f'<span style="font-size:0.9em">{bloc["resume"]}</span></div>',
                unsafe_allow_html=True)

    noms_fiches = [f"Fiche {f['id']} — {f['titre']}" for f in bloc["fiches"]]
    choix_fiche = st.selectbox("Fiche", noms_fiches)
    fiche = bloc["fiches"][noms_fiches.index(choix_fiche)]

    cle = f"{bloc['id']}#{fiche['id']}"
    col_t, col_c = st.columns([4, 1])
    with col_t:
        st.header(f"{fiche['id']} — {fiche['titre']}")
        st.markdown(f'<div class="fiche-meta">Volume horaire indicatif : {fiche["duree"]}</div>',
                    unsafe_allow_html=True)
    with col_c:
        deja = cle in P["fiches_lues"]
        if st.checkbox("Fiche lue", value=deja, key=f"lu_{cle}") != deja:
            if deja:
                P["fiches_lues"].remove(cle)
            else:
                P["fiches_lues"].append(cle)
            sauver_progression(P)
            st.rerun()

    t1, t2, t3, t4, t5 = st.tabs(
        ["📖 Cours", "📐 Formules", "🏭 Cas industriel", "✍️ Exercice", "✅ Corrigé"])

    with t1:
        st.markdown(fiche["cours"])
    with t2:
        st.markdown(fiche["formules"])
    with t3:
        st.markdown(fiche["exemple"])
    with t4:
        st.markdown(fiche["exercice"])
        st.markdown('<div class="warn-box">Cherchez l\'exercice complètement avant '
                    'd\'ouvrir le corrigé. Un corrigé lu trop tôt donne l\'illusion de '
                    'comprendre.</div>', unsafe_allow_html=True)
    with t5:
        st.markdown(fiche["corrige"])

    st.divider()
    note = st.text_area("Mes notes personnelles sur cette fiche",
                        value=P["notes"].get(cle, ""), height=120, key=f"note_{cle}")
    if st.button("Enregistrer la note", key=f"btn_note_{cle}"):
        P["notes"][cle] = note
        sauver_progression(P)
        st.success("Note enregistrée.")


# ===========================================================================
# PAGE : QUIZ
# ===========================================================================

elif PAGE == "🎯 Quiz interactif":
    st.title("Quiz interactif")

    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        cats = st.multiselect("Thèmes", qz.CATEGORIES, default=qz.CATEGORIES[:1])
    with col2:
        nb = st.number_input("Nombre de questions", 3, 30, 8)
    with col3:
        niveaux = st.multiselect("Niveaux", qz.NIVEAUX, default=qz.NIVEAUX)

    if st.button("🚀 Démarrer le quiz", type="primary"):
        pool = [q for q in qz.toutes_les_questions()
                if q["categorie"] in cats and q["niveau"] in niveaux]
        if not pool:
            st.error("Aucune question ne correspond à ces filtres.")
        else:
            random.shuffle(pool)
            st.session_state.quiz_questions = pool[:int(nb)]
            st.session_state.quiz_index = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_reponses = []
            st.session_state.quiz_valide = False
            st.rerun()

    if "quiz_questions" in st.session_state and st.session_state.quiz_questions:
        questions = st.session_state.quiz_questions
        i = st.session_state.quiz_index

        if i < len(questions):
            q = questions[i]
            st.progress((i) / len(questions))
            st.caption(f"Question {i+1}/{len(questions)} — {q['categorie']} · "
                       f"niveau {q['niveau']}")

            with st.container(border=True):
                st.subheader(q["question"])
                choix = st.radio("Votre réponse", q["options"],
                                 key=f"q_{i}", index=None,
                                 disabled=st.session_state.quiz_valide)

            if not st.session_state.quiz_valide:
                if st.button("Valider", type="primary", disabled=choix is None):
                    idx = q["options"].index(choix)
                    juste = idx == q["correct"]
                    if juste:
                        st.session_state.quiz_score += 1
                    st.session_state.quiz_reponses.append({
                        "question": q["question"], "categorie": q["categorie"],
                        "juste": juste, "donnee": choix,
                        "attendue": q["options"][q["correct"]],
                    })
                    st.session_state.quiz_valide = True
                    st.rerun()
            else:
                derniere = st.session_state.quiz_reponses[-1]
                if derniere["juste"]:
                    st.markdown(f'<div class="ok-box"><b>✅ Correct</b></div>',
                                unsafe_allow_html=True)
                else:
                    st.markdown(
                        f'<div class="ko-box"><b>❌ Incorrect</b><br>'
                        f'Réponse attendue : <b>{derniere["attendue"]}</b></div>',
                        unsafe_allow_html=True)
                st.info(f"**Explication —** {q['explication']}")

                if st.button("Question suivante ▶", type="primary"):
                    st.session_state.quiz_index += 1
                    st.session_state.quiz_valide = False
                    st.rerun()
        else:
            score = st.session_state.quiz_score
            total = len(questions)
            pct = score / total * 100
            st.header("Résultat")
            c1, c2, c3 = st.columns(3)
            c1.metric("Score", f"{score}/{total}")
            c2.metric("Pourcentage", f"{pct:.0f} %")
            c3.metric("Note /20", f"{score/total*20:.1f}")

            if pct >= 80:
                st.success("Très bon niveau. Les notions sont acquises.")
            elif pct >= 60:
                st.warning("Niveau correct. Revoyez les questions manquées ci-dessous.")
            else:
                st.error("Il faut reprendre les fiches de cours correspondantes.")

            erreurs = [r for r in st.session_state.quiz_reponses if not r["juste"]]
            if erreurs:
                st.subheader("Questions à revoir")
                for e in erreurs:
                    with st.expander(f"❌ {e['question'][:80]}…"):
                        st.write(f"**Votre réponse :** {e['donnee']}")
                        st.write(f"**Réponse attendue :** {e['attendue']}")
                        st.caption(f"Thème : {e['categorie']}")

            if st.button("Enregistrer ce résultat"):
                P["resultats_quiz"].append({
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "score": score, "total": total,
                    "themes": ", ".join(sorted({r["categorie"]
                                                for r in st.session_state.quiz_reponses})),
                })
                sauver_progression(P)
                st.success("Résultat enregistré dans la progression.")

            if st.button("Nouveau quiz"):
                del st.session_state.quiz_questions
                st.rerun()


# ===========================================================================
# PAGE : AJUSTEMENTS ISO
# ===========================================================================

elif PAGE == "📐 Calculateur d'ajustements ISO":
    st.title("Calculateur d'ajustements ISO 286")
    st.caption("Domaine couvert : 0 < d ≤ 500 mm, grades IT1 à IT16.")

    onglet1, onglet2, onglet3 = st.tabs(
        ["🔩 Ajustement complet", "📏 Cote isolée", "📋 Ajustements recommandés"])

    # ---------------- Ajustement complet ----------------
    with onglet1:
        c1, c2, c3, c4, c5 = st.columns([2, 1.2, 1, 1.2, 1])
        with c1:
            dim = st.number_input("Cote nominale (mm)", 0.5, 500.0, 20.0, step=0.5)
        with c2:
            lettre_al = st.selectbox("Alésage", iso286.LETTRES_ALESAGE,
                                     index=iso286.LETTRES_ALESAGE.index("H"))
        with c3:
            grade_al = st.selectbox("Grade", list(range(1, 17)), index=6, key="gal")
        with c4:
            lettre_ar = st.selectbox("Arbre", iso286.LETTRES_ARBRE,
                                     index=iso286.LETTRES_ARBRE.index("g"))
        with c5:
            grade_ar = st.selectbox("Grade", list(range(1, 17)), index=5, key="gar")

        try:
            r = iso286.calcul_ajustement(dim, lettre_al, grade_al, lettre_ar, grade_ar)

            st.markdown(f"### {r['designation']}")

            couleur = {"Ajustement AVEC JEU": "ok-box",
                       "Ajustement AVEC SERRAGE": "warn-box",
                       "Ajustement INCERTAIN": "info-box"}[r["nature"]]
            st.markdown(f'<div class="{couleur}"><b>{r["nature"]}</b><br>{r["detail"]}</div>',
                        unsafe_allow_html=True)

            st.write("")
            ca, cb = st.columns(2)
            with ca:
                st.markdown(f"#### Alésage Ø{dim} {lettre_al}{grade_al}")
                st.dataframe(pd.DataFrame({
                    "Grandeur": ["IT", "Écart supérieur ES", "Écart inférieur EI",
                                 "Cote maxi", "Cote mini"],
                    "Valeur": [f"{r['IT_alesage']:.0f} µm",
                               f"{r['ES']:+.1f} µm  ({r['ES']/1000:+.4f} mm)",
                               f"{r['EI']:+.1f} µm  ({r['EI']/1000:+.4f} mm)",
                               f"{r['alesage_maxi']:.4f} mm",
                               f"{r['alesage_mini']:.4f} mm"],
                }), hide_index=True, width="stretch")
            with cb:
                st.markdown(f"#### Arbre Ø{dim} {lettre_ar}{grade_ar}")
                st.dataframe(pd.DataFrame({
                    "Grandeur": ["IT", "Écart supérieur es", "Écart inférieur ei",
                                 "Cote maxi", "Cote mini"],
                    "Valeur": [f"{r['IT_arbre']:.0f} µm",
                               f"{r['es']:+.1f} µm  ({r['es']/1000:+.4f} mm)",
                               f"{r['ei']:+.1f} µm  ({r['ei']/1000:+.4f} mm)",
                               f"{r['arbre_maxi']:.4f} mm",
                               f"{r['arbre_mini']:.4f} mm"],
                }), hide_index=True, width="stretch")

            st.write("")
            m1, m2, m3 = st.columns(3)
            if r["jeu_mini"] >= 0:
                m1.metric("Jeu maximal", f"{r['jeu_maxi']:.0f} µm")
                m2.metric("Jeu minimal", f"{r['jeu_mini']:.0f} µm")
            elif r["jeu_maxi"] <= 0:
                m1.metric("Serrage maximal", f"{r['serrage_maxi']:.0f} µm")
                m2.metric("Serrage minimal", f"{r['serrage_mini']:.0f} µm")
            else:
                m1.metric("Jeu maximal", f"{r['jeu_maxi']:.0f} µm")
                m2.metric("Serrage maximal", f"{r['serrage_maxi']:.0f} µm")
            m3.metric("Tolérance de l'ajustement", f"{r['tolerance_ajustement']:.0f} µm")

            with st.expander("📝 Détail du calcul, pas à pas"):
                st.markdown(f"""
**Étape 1 — Lecture des IT dans la table**
- Cote {dim} mm → tranche correspondante
- IT{grade_al} = **{r['IT_alesage']:.0f} µm** (alésage)
- IT{grade_ar} = **{r['IT_arbre']:.0f} µm** (arbre)

**Étape 2 — Placement de l'alésage {lettre_al}{grade_al}**
- EI = {r['EI']:+.1f} µm
- ES = EI + IT = {r['EI']:+.1f} + {r['IT_alesage']:.0f} = **{r['ES']:+.1f} µm**

**Étape 3 — Placement de l'arbre {lettre_ar}{grade_ar}**
- ei = {r['ei']:+.1f} µm
- es = ei + IT = {r['ei']:+.1f} + {r['IT_arbre']:.0f} = **{r['es']:+.1f} µm**

**Étape 4 — Calcul des jeux**

$$ J_{{max}} = ES - ei = {r['ES']:.1f} - ({r['ei']:.1f}) = \\mathbf{{{r['jeu_maxi']:.1f}\\ \\mu m}} $$

$$ J_{{min}} = EI - es = {r['EI']:.1f} - ({r['es']:.1f}) = \\mathbf{{{r['jeu_mini']:.1f}\\ \\mu m}} $$

**Étape 5 — Conclusion**

{r['nature']} — {r['detail']}

**Vérification :** IT_ajustement = IT_alésage + IT_arbre =
{r['IT_alesage']:.0f} + {r['IT_arbre']:.0f} = **{r['tolerance_ajustement']:.0f} µm** ✔️
                """)

            cle_aj = f"{lettre_al.upper()}{grade_al}/{lettre_ar.lower()}{grade_ar}"
            if cle_aj in iso286.AJUSTEMENTS_COURANTS:
                nature, emploi = iso286.AJUSTEMENTS_COURANTS[cle_aj]
                st.success(f"**{cle_aj} — ajustement normalisé courant** ({nature}) : {emploi}")

        except ValueError as e:
            st.error(str(e))

    # ---------------- Cote isolée ----------------
    with onglet2:
        c1, c2, c3 = st.columns(3)
        with c1:
            dim2 = st.number_input("Cote nominale (mm)", 0.5, 500.0, 25.0, step=0.5, key="d2")
        with c2:
            typ = st.radio("Type", ["Alésage (majuscule)", "Arbre (minuscule)"])
        with c3:
            grade2 = st.selectbox("Grade IT", list(range(1, 17)), index=6, key="g2")

        lettres = iso286.LETTRES_ALESAGE if typ.startswith("Alésage") else iso286.LETTRES_ARBRE
        lettre2 = st.select_slider("Lettre de position", lettres,
                                   value="H" if typ.startswith("Alésage") else "h")

        try:
            if typ.startswith("Alésage"):
                inf, sup = iso286.ecarts_alesage(dim2, lettre2, grade2)
                label_inf, label_sup = "EI", "ES"
            else:
                inf, sup = iso286.ecarts_arbre(dim2, lettre2, grade2)
                label_inf, label_sup = "ei", "es"
            it = iso286.valeur_it(dim2, grade2)

            st.markdown(f"### Ø{dim2} {lettre2}{grade2}")
            k1, k2, k3, k4 = st.columns(4)
            k1.metric("IT", f"{it:.0f} µm")
            k2.metric(f"Écart sup. {label_sup}", f"{sup:+.1f} µm")
            k3.metric(f"Écart inf. {label_inf}", f"{inf:+.1f} µm")
            k4.metric("Cote maxi", f"{dim2 + sup/1000:.4f} mm")

            st.latex(rf"\varnothing {dim2}\ {lettre2}{grade2} = "
                     rf"\varnothing {dim2}^{{{sup/1000:+.4f}}}_{{{inf/1000:+.4f}}}"
                     rf"\quad\Rightarrow\quad {dim2 + inf/1000:.4f} \le d \le {dim2 + sup/1000:.4f}\ mm")

            st.divider()
            st.subheader("Contrôle de conformité")
            mesure = st.number_input("Cote mesurée (mm)", value=float(dim2), step=0.001,
                                     format="%.4f")
            mini, maxi = dim2 + inf / 1000, dim2 + sup / 1000
            if mini <= mesure <= maxi:
                st.markdown(f'<div class="ok-box"><b>✅ CONFORME</b> — '
                            f'{mini:.4f} ≤ {mesure:.4f} ≤ {maxi:.4f} mm</div>',
                            unsafe_allow_html=True)
            else:
                ecart = (mesure - maxi if mesure > maxi else mesure - mini) * 1000
                sens = "trop grande" if mesure > maxi else "trop petite"
                st.markdown(f'<div class="ko-box"><b>❌ REBUT</b> — pièce {sens} '
                            f'de {abs(ecart):.1f} µm</div>', unsafe_allow_html=True)
        except ValueError as e:
            st.error(str(e))

    # ---------------- Recommandés ----------------
    with onglet3:
        st.subheader("Ajustements normalisés courants (système de l'alésage normal H)")
        lignes = [{"Ajustement": k, "Nature": v[0], "Application typique": v[1]}
                  for k, v in iso286.AJUSTEMENTS_COURANTS.items()]
        st.dataframe(pd.DataFrame(lignes), hide_index=True, width="stretch")
        st.info("**Règle de choix :** la pièce qui doit tourner ou coulisser reçoit le jeu ; "
                "la pièce qui doit être immobilisée reçoit le serrage. Pour un roulement, "
                "la bague soumise à charge tournante est toujours serrée.")


# ===========================================================================
# PAGE : CALCULATEURS RDM
# ===========================================================================

elif PAGE == "🔧 Calculateurs RDM":
    st.title("Calculateurs RDM")
    st.markdown('<div class="warn-box">Ces outils servent à <b>vérifier</b> un calcul posé à '
                'la main, pas à le remplacer. En examen, seule la démarche écrite est notée.</div>',
                unsafe_allow_html=True)
    st.write("")

    onglets = st.tabs(["Traction / Compression", "Cisaillement + matage",
                       "Torsion", "Flexion", "Flambage", "Flexion + torsion"])

    def choisir_materiau(cle):
        noms = [m["nom"] for m in mat.MATERIAUX]
        nom = st.selectbox("Matériau", noms, index=noms.index("S355"), key=cle)
        return mat.get_materiau(nom)

    def choisir_section(cle, avec_rect=True):
        formes = ["Cercle plein", "Tube"] + (["Rectangle", "Rectangle creux"] if avec_rect else [])
        forme = st.selectbox("Section", formes, key=f"f_{cle}")
        kw = {}
        c = st.columns(4)
        if forme == "Cercle plein":
            kw["d"] = c[0].number_input("Ø (mm)", 1.0, 1000.0, 25.0, key=f"d_{cle}")
        elif forme == "Tube":
            kw["D"] = c[0].number_input("Ø ext (mm)", 1.0, 1000.0, 30.0, key=f"De_{cle}")
            kw["d"] = c[1].number_input("Ø int (mm)", 0.0, 999.0, 22.0, key=f"Di_{cle}")
        elif forme == "Rectangle":
            kw["b"] = c[0].number_input("Largeur b (mm)", 1.0, 1000.0, 40.0, key=f"b_{cle}")
            kw["h"] = c[1].number_input("Hauteur h (mm)", 1.0, 1000.0, 80.0, key=f"h_{cle}")
        else:
            kw["b"] = c[0].number_input("b ext (mm)", 1.0, 1000.0, 60.0, key=f"b_{cle}")
            kw["h"] = c[1].number_input("h ext (mm)", 1.0, 1000.0, 60.0, key=f"h_{cle}")
            kw["bi"] = c[2].number_input("b int (mm)", 0.0, 999.0, 50.0, key=f"bi_{cle}")
            kw["hi"] = c[3].number_input("h int (mm)", 0.0, 999.0, 50.0, key=f"hi_{cle}")
        return forme, kw

    def verdict(ok, texte_ok, texte_ko):
        cls = "ok-box" if ok else "ko-box"
        txt = texte_ok if ok else texte_ko
        st.markdown(f'<div class="{cls}">{txt}</div>', unsafe_allow_html=True)

    # ------------- Traction -------------
    with onglets[0]:
        c1, c2 = st.columns([1, 1])
        with c1:
            m = choisir_materiau("mat_tr")
            N = st.number_input("Effort normal N (N)", 1.0, 1e7, 45000.0, step=100.0)
            s = st.number_input("Coefficient de sécurité s", 1.0, 15.0, 3.0, step=0.5)
            L = st.number_input("Longueur L (mm)", 0.0, 100000.0, 2500.0, step=10.0)
        with c2:
            forme, kw = choisir_section("tr")
        S = mat.section_aire(forme, **kw)
        r = mat.traction(N, S, m["Re"], s, L=L or None, E=m["E"] * 1000)

        st.divider()
        k = st.columns(4)
        k[0].metric("Section S", f"{S:.1f} mm²")
        k[1].metric("Contrainte σ", f"{r['sigma']:.1f} MPa")
        k[2].metric("Rpe admissible", f"{r['Rpe']:.1f} MPa")
        k[3].metric("Sécurité réelle", f"{r['s_reel']:.2f}")
        verdict(r["ok"],
                f"<b>✅ RÉSISTANCE VÉRIFIÉE</b> — σ = {r['sigma']:.1f} ≤ Rpe = {r['Rpe']:.1f} MPa",
                f"<b>❌ RÉSISTANCE INSUFFISANTE</b> — σ = {r['sigma']:.1f} > Rpe = {r['Rpe']:.1f} MPa")
        if "allongement" in r:
            st.metric("Allongement ΔL", f"{r['allongement']:.3f} mm",
                      f"ε = {r['epsilon']:.4f} %")
        st.latex(rf"\sigma = \frac{{N}}{{S}} = \frac{{{N:.0f}}}{{{S:.1f}}} = {r['sigma']:.2f}"
                 rf"\ \mathrm{{MPa}} \qquad R_{{pe}} = \frac{{{m['Re']}}}{{{s}}} = {r['Rpe']:.1f}"
                 rf"\ \mathrm{{MPa}}")

    # ------------- Cisaillement -------------
    with onglets[1]:
        c1, c2 = st.columns(2)
        with c1:
            m = choisir_materiau("mat_ci")
            T = st.number_input("Effort tranchant T (N)", 1.0, 1e7, 48000.0, step=100.0)
            s = st.number_input("Coefficient de sécurité", 1.0, 15.0, 3.0, step=0.5, key="sci")
            double = st.checkbox("Cisaillement double (chape)", value=True)
            coef = st.slider("Reg / Re", 0.4, 0.8, 0.5, 0.05)
        with c2:
            forme, kw = choisir_section("ci", avec_rect=False)
            st.markdown("**Vérification du matage**")
            e_mat = st.number_input("Épaisseur de la pièce matée (mm)", 1.0, 500.0, 20.0)
            f_mat = st.number_input("Effort sur cette pièce (N)", 1.0, 1e7, 48000.0, step=100.0)

        S = mat.section_aire(forme, **kw)
        r = mat.cisaillement(T, S, m["Re"], s, double=double, coef_Reg=coef)
        d_axe = kw.get("d") if forme == "Cercle plein" else kw.get("D")
        rm = mat.matage(f_mat, d_axe, e_mat, m["Re"])

        st.divider()
        k = st.columns(4)
        k[0].metric("Section résistante", f"{r['S_effective']:.1f} mm²")
        k[1].metric("Contrainte τ", f"{r['tau']:.1f} MPa")
        k[2].metric("Rpg admissible", f"{r['Rpg']:.1f} MPa")
        k[3].metric("Sécurité réelle", f"{r['s_reel']:.2f}")
        verdict(r["ok"], "<b>✅ CISAILLEMENT VÉRIFIÉ</b>", "<b>❌ CISAILLEMENT INSUFFISANT</b>")
        st.latex(rf"\tau = \frac{{T}}{{{'2S' if double else 'S'}}} = "
                 rf"\frac{{{T:.0f}}}{{{r['S_effective']:.1f}}} = {r['tau']:.2f}\ \mathrm{{MPa}}")

        st.write("")
        k2 = st.columns(3)
        k2[0].metric("Pression de matage p", f"{rm['p']:.1f} MPa")
        k2[1].metric("p admissible", f"{rm['p_adm']:.1f} MPa")
        k2[2].metric("Marge", f"{rm['p_adm'] - rm['p']:+.1f} MPa")
        verdict(rm["ok"], "<b>✅ MATAGE VÉRIFIÉ</b>", "<b>❌ MATAGE EXCESSIF</b>")

    # ------------- Torsion -------------
    with onglets[2]:
        c1, c2 = st.columns(2)
        with c1:
            m = choisir_materiau("mat_to")
            mode = st.radio("Donnée d'entrée", ["Couple direct", "Puissance + vitesse"])
            if mode == "Couple direct":
                Mt_nm = st.number_input("Couple Mt (N·m)", 0.1, 1e6, 280.0, step=1.0)
            else:
                Pw = st.number_input("Puissance (kW)", 0.01, 1000.0, 22.0, step=0.5)
                Ntr = st.number_input("Vitesse (tr/min)", 1.0, 30000.0, 750.0, step=10.0)
                _, Mt_nm, _ = mat.couple_depuis_puissance(Pw * 1000, Ntr)
                st.info(f"Couple calculé : **{Mt_nm:.1f} N·m**")
            s = st.number_input("Coefficient de sécurité", 1.0, 15.0, 5.0, step=0.5, key="sto")
            Ltor = st.number_input("Longueur de l'arbre (mm)", 0.0, 20000.0, 1200.0, step=10.0)
        with c2:
            forme, kw = choisir_section("to", avec_rect=False)
            st.caption("La théorie de la torsion n'est valable que pour les sections circulaires.")
            lim_ang = st.number_input("Angle unitaire admissible (°/m)", 0.05, 5.0, 0.5, step=0.05)

        I0, v = mat.section_i0(forme, **kw)
        r = mat.torsion(Mt_nm * 1000, I0, v, m["Re"], s, L=Ltor or None)

        st.divider()
        k = st.columns(4)
        k[0].metric("I₀ polaire", f"{I0:,.0f} mm⁴".replace(",", " "))
        k[1].metric("Contrainte τmax", f"{r['tau']:.1f} MPa")
        k[2].metric("Rpg admissible", f"{r['Rpg']:.1f} MPa")
        k[3].metric("Sécurité réelle", f"{r['s_reel']:.2f}")
        verdict(r["ok"], "<b>✅ RÉSISTANCE VÉRIFIÉE</b>", "<b>❌ RÉSISTANCE INSUFFISANTE</b>")

        if "theta_deg" in r:
            st.write("")
            k2 = st.columns(3)
            k2[0].metric("Angle total θ", f"{r['theta_deg']:.3f} °")
            k2[1].metric("Angle unitaire", f"{r['theta_deg_par_m']:.3f} °/m")
            k2[2].metric("Limite fixée", f"{lim_ang:.2f} °/m")
            verdict(r["theta_deg_par_m"] <= lim_ang,
                    "<b>✅ RIGIDITÉ VÉRIFIÉE</b>",
                    "<b>❌ RIGIDITÉ INSUFFISANTE</b> — sur un arbre long, c'est souvent "
                    "ce critère qui dimensionne, pas la résistance. Augmentez le diamètre "
                    "ou fractionnez l'arbre avec un palier intermédiaire.")

    # ------------- Flexion -------------
    with onglets[3]:
        c1, c2 = st.columns(2)
        with c1:
            m = choisir_materiau("mat_fl")
            cas = st.selectbox("Cas de charge", list(mat.CAS_FLEXION.keys()))
            est_repartie = mat.CAS_FLEXION[cas]["type"] == "repartie"
            if est_repartie:
                charge = st.number_input("Charge répartie q (N/mm)", 0.001, 1000.0, 0.155,
                                         step=0.01, format="%.3f")
            else:
                charge = st.number_input("Charge F (N)", 1.0, 1e7, 11772.0, step=100.0)
            Lf = st.number_input("Portée L (mm)", 1.0, 50000.0, 4000.0, step=10.0)
            s = st.number_input("Coefficient de sécurité", 1.0, 15.0, 5.0, step=0.5, key="sfl")
        with c2:
            forme, kw = choisir_section("fl")
            div = st.number_input("Flèche admissible = L / …", 50, 5000, 500, step=50)

        I, v = mat.section_igz(forme, **kw)
        r = mat.flexion(cas, charge, Lf, I, v, m["E"] * 1000, m["Re"], s,
                        fleche_adm=Lf / div)

        st.caption(r["description"])
        st.divider()
        k = st.columns(4)
        k[0].metric("IGz", f"{I:,.0f} mm⁴".replace(",", " "))
        k[1].metric("Moment Mf max", f"{r['Mf']/1000:.1f} N·m")
        k[2].metric("Contrainte σ", f"{r['sigma']:.1f} MPa")
        k[3].metric("Sécurité réelle", f"{r['s_reel']:.2f}")
        verdict(r["ok_resistance"],
                f"<b>✅ RÉSISTANCE VÉRIFIÉE</b> — σ = {r['sigma']:.1f} ≤ {r['Rpe']:.1f} MPa",
                f"<b>❌ RÉSISTANCE INSUFFISANTE</b> — σ = {r['sigma']:.1f} > {r['Rpe']:.1f} MPa")

        st.write("")
        k2 = st.columns(3)
        k2[0].metric("Flèche f", f"{r['fleche']:.3f} mm")
        k2[1].metric("Flèche admissible", f"{r['fleche_adm']:.3f} mm")
        k2[2].metric("Ratio", f"{r['fleche']/r['fleche_adm']*100:.0f} %")
        verdict(r["ok_rigidite"], "<b>✅ RIGIDITÉ VÉRIFIÉE</b>",
                "<b>❌ FLÈCHE EXCESSIVE</b> — rappel : changer de nuance d'acier ne sert à rien "
                "(E identique). Agir sur la hauteur de section (en h³) ou sur la portée (en L³).")

    # ------------- Flambage -------------
    with onglets[4]:
        c1, c2 = st.columns(2)
        with c1:
            m = choisir_materiau("mat_fb")
            F = st.number_input("Effort de compression F (N)", 1.0, 1e7, 32000.0, step=100.0)
            Lfb = st.number_input("Longueur L (mm)", 1.0, 50000.0, 600.0, step=10.0)
            liaison = st.selectbox("Liaisons aux extrémités",
                                   ["Rotule - rotule", "Encastrement - libre",
                                    "Encastrement - rotule", "Encastrement - encastrement"])
        with c2:
            forme, kw = choisir_section("fb")

        I, v = mat.section_igz(forme, **kw)
        S = mat.section_aire(forme, **kw)
        r = mat.flambage(m["E"] * 1000, I, Lfb, liaison, F=F)
        rho = math.sqrt(I / S)
        lam = r["Lf"] / rho

        st.divider()
        k = st.columns(4)
        k[0].metric("Longueur libre Lf", f"{r['Lf']:.0f} mm")
        k[1].metric("Rayon de giration ρ", f"{rho:.2f} mm")
        k[2].metric("Élancement λ", f"{lam:.1f}")
        k[3].metric("Charge critique Fc", f"{r['Fc']/1000:.1f} kN")
        st.metric("Coefficient de sécurité au flambage", f"{r['s_flambage']:.2f}")
        verdict(r["ok"], "<b>✅ FLAMBAGE VÉRIFIÉ</b> (s ≥ 3)",
                "<b>❌ RISQUE DE FLAMBAGE</b> — augmentez le moment quadratique (tube plutôt "
                "que barre pleine) ou réduisez la longueur libre.")
        if lam < 100:
            st.markdown('<div class="warn-box"><b>λ &lt; 100 :</b> on est dans le domaine du '
                        'flambage plastique. La formule d\'Euler <b>surestime</b> la charge '
                        'critique réelle. Une vérification par les courbes de l\'Eurocode 3 '
                        'donnerait une valeur inférieure. Le mentionner en copie.</div>',
                        unsafe_allow_html=True)

    # ------------- Flexion + torsion -------------
    with onglets[5]:
        st.markdown("Dimensionnement d'un **arbre** soumis simultanément à flexion et torsion.")
        c1, c2 = st.columns(2)
        with c1:
            m = choisir_materiau("mat_ft")
            Mf = st.number_input("Moment de flexion Mf (N·m)", 0.0, 1e6, 360.0, step=1.0)
            Mt = st.number_input("Moment de torsion Mt (N·m)", 0.0, 1e6, 159.2, step=1.0)
            s = st.number_input("Coefficient de sécurité", 1.0, 15.0, 4.0, step=0.5, key="sft")
        with c2:
            critere = st.radio("Critère", ["Tresca", "Von Mises"])
            Kt = st.number_input("Coefficient de concentration Kt", 1.0, 4.0, 2.0, step=0.1,
                                 help="Rainure de clavette fond arrondi ≈ 1,6-2,0 ; "
                                      "fond vif ≈ 2,5-3,5 ; épaulement r/d=0,05 ≈ 1,8")
            d_ex = st.number_input("Diamètre à vérifier (mm)", 1.0, 1000.0, 40.0, step=1.0)

        Mi = mat.flexion_torsion(Mf * 1000, Mt * 1000, critere)
        Rpe = m["Re"] / s
        d_min = (32 * Mi / (math.pi * Rpe)) ** (1 / 3)
        d_min_kt = d_min * Kt ** (1 / 3)
        module = math.pi * d_ex ** 3 / 32
        sigma_nom = Mi / module
        sigma_max = sigma_nom * Kt

        st.divider()
        k = st.columns(4)
        k[0].metric("Moment idéal", f"{Mi/1000:.1f} N·m")
        k[1].metric("Ø mini (sans Kt)", f"{d_min:.1f} mm")
        k[2].metric("Ø mini (avec Kt)", f"{d_min_kt:.1f} mm")
        k[3].metric("Rpe", f"{Rpe:.1f} MPa")

        st.write("")
        k2 = st.columns(3)
        k2[0].metric(f"σ nominale (Ø{d_ex:.0f})", f"{sigma_nom:.1f} MPa")
        k2[1].metric("σ max avec Kt", f"{sigma_max:.1f} MPa")
        k2[2].metric("Sécurité réelle", f"{m['Re']/sigma_max:.2f}")
        verdict(sigma_max <= Rpe,
                f"<b>✅ Ø{d_ex:.0f} CONVIENT</b> — σmax = {sigma_max:.1f} ≤ {Rpe:.1f} MPa",
                f"<b>❌ Ø{d_ex:.0f} INSUFFISANT</b> — σmax = {sigma_max:.1f} > {Rpe:.1f} MPa. "
                f"Diamètre minimal nécessaire : <b>{d_min_kt:.1f} mm</b>")

        st.latex(rf"M_{{idéal}} = \sqrt{{M_f^2 + M_t^2}} = "
                 rf"\sqrt{{{Mf:.0f}^2 + {Mt:.1f}^2}} = {Mi/1000:.1f}\ \mathrm{{N \cdot m}}")
        st.info("Le diamètre calculé est un **minimum**. Le diamètre final est généralement "
                "imposé par les composants standards (roulements, accouplements) et par la "
                "tenue en fatigue.")


# ===========================================================================
# PAGE : MATÉRIAUX
# ===========================================================================

elif PAGE == "🧱 Base matériaux":
    st.title("Base matériaux")

    t1, t2, t3 = st.tabs(["📋 Tableau", "⚖️ Comparateur", "🎯 Indices de performance"])

    with t1:
        familles = st.multiselect("Familles", mat.FAMILLES, default=mat.FAMILLES)
        data = [m for m in mat.MATERIAUX if m["famille"] in familles]
        df = pd.DataFrame([{
            "Désignation": m["nom"], "Famille": m["famille"],
            "Re (MPa)": m["Re"], "Rm (MPa)": m["Rm"], "E (GPa)": m["E"],
            "ρ (kg/m³)": m["rho"], "A (%)": m["A"], "Prix rel.": m["prix"],
        } for m in data])
        st.dataframe(df, hide_index=True, width="stretch", height=520)

        st.divider()
        noms = [m["nom"] for m in data]
        if noms:
            sel = st.selectbox("Fiche détaillée", noms)
            m = mat.get_materiau(sel)
            with st.container(border=True):
                st.subheader(m["nom"])
                st.caption(f"{m['famille']} — {m['designation']}")
                k = st.columns(5)
                k[0].metric("Re", f"{m['Re']} MPa")
                k[1].metric("Rm", f"{m['Rm']} MPa")
                k[2].metric("E", f"{m['E']} GPa")
                k[3].metric("ρ", f"{m['rho']} kg/m³")
                k[4].metric("A", f"{m['A']} %")
                st.markdown(f"**Emploi :** {m['emploi']}")

    with t2:
        noms = [m["nom"] for m in mat.MATERIAUX]
        choix = st.multiselect("Matériaux à comparer (2 à 4)", noms,
                               default=["S355", "EN AW-6082 T6", "EN-GJS-500-7"],
                               max_selections=4)
        if len(choix) >= 2:
            sel = [mat.get_materiau(n) for n in choix]
            df = pd.DataFrame({
                "Critère": ["Limite élastique Re (MPa)", "Résistance Rm (MPa)",
                            "Module de Young E (GPa)", "Masse volumique ρ (kg/m³)",
                            "Allongement A (%)", "Prix relatif",
                            "Re/ρ (résistance spécifique)", "E/ρ (rigidité spécifique)",
                            "√E/ρ (flexion)"],
                **{m["nom"]: [
                    f"{m['Re']}", f"{m['Rm']}", f"{m['E']}", f"{m['rho']}", f"{m['A']}",
                    f"×{m['prix']:.1f}",
                    f"{m['Re']/m['rho']*1000:.1f}",
                    f"{m['E']*1000/m['rho']*1000:.1f}",
                    f"{math.sqrt(m['E']*1000)/m['rho']*1000:.2f}",
                ] for m in sel}
            })
            st.dataframe(df, hide_index=True, width="stretch")

            st.divider()
            st.subheader("Masse d'une même pièce selon le matériau")
            vol = st.number_input("Volume de la pièce (cm³)", 1.0, 100000.0, 500.0, step=10.0)
            masses = pd.DataFrame({
                "Matériau": [m["nom"] for m in sel],
                "Masse (kg)": [m["rho"] * vol * 1e-6 for m in sel],
                "Coût matière relatif": [m["rho"] * vol * 1e-6 * m["prix"] for m in sel],
            })
            st.bar_chart(masses.set_index("Matériau")["Masse (kg)"])
            st.dataframe(masses, hide_index=True, width="stretch")
        else:
            st.info("Sélectionnez au moins deux matériaux.")

    with t3:
        st.markdown("""
Un bon choix de matériau ne consiste jamais à prendre « le plus résistant », mais celui qui
offre le meilleur **rapport performance / masse** pour la sollicitation dominante.
        """)
        objectif = st.selectbox("Objectif de conception", [
            "Pièce légère et résistante (traction) — maximiser Re/ρ",
            "Pièce légère et rigide (traction) — maximiser E/ρ",
            "Poutre légère et rigide (flexion) — maximiser √E/ρ",
            "Ressort (énergie élastique) — maximiser Re²/E",
        ])
        def indice(m):
            if objectif.startswith("Pièce légère et résistante"):
                return m["Re"] / m["rho"] * 1000
            if objectif.startswith("Pièce légère et rigide"):
                return m["E"] * 1e6 / m["rho"]
            if objectif.startswith("Poutre"):
                return math.sqrt(m["E"] * 1000) / m["rho"] * 1000
            return m["Re"] ** 2 / (m["E"] * 1000)

        classement = sorted(mat.MATERIAUX, key=indice, reverse=True)[:12]
        df = pd.DataFrame({
            "Rang": range(1, len(classement) + 1),
            "Matériau": [m["nom"] for m in classement],
            "Famille": [m["famille"] for m in classement],
            "Indice": [round(indice(m), 2) for m in classement],
            "Prix rel.": [m["prix"] for m in classement],
        })
        st.dataframe(df, hide_index=True, width="stretch")
        st.info("L'indice ne tient compte ni du coût, ni de la mise en œuvre, ni de la "
                "corrosion. Le titane sort souvent premier — et reste souvent injustifiable.")


# ===========================================================================
# PAGE : PROGRESSION
# ===========================================================================

elif PAGE == "📊 Ma progression":
    st.title("Ma progression")

    c1, c2, c3 = st.columns(3)
    c1.metric("Fiches lues", f"{lues}/{nb_fiches}")
    res = P["resultats_quiz"]
    c2.metric("Quiz réalisés", len(res))
    if res:
        moy = sum(r["score"] / r["total"] for r in res) / len(res) * 20
        c3.metric("Moyenne /20", f"{moy:.1f}")
    else:
        c3.metric("Moyenne /20", "—")

    st.divider()
    st.subheader("Avancement par bloc")
    for bloc in BLOCS:
        fiches_bloc = [f"{bloc['id']}#{f['id']}" for f in bloc["fiches"]]
        n = sum(1 for f in fiches_bloc if f in P["fiches_lues"])
        st.write(f"**{bloc['titre']}** — {n}/{len(bloc['fiches'])}")
        st.progress(n / len(bloc["fiches"]))

    if res:
        st.divider()
        st.subheader("Historique des quiz")
        df = pd.DataFrame([{
            "Date": r["date"], "Thèmes": r["themes"],
            "Score": f"{r['score']}/{r['total']}",
            "Note /20": round(r["score"] / r["total"] * 20, 1),
        } for r in reversed(res)])
        st.dataframe(df, hide_index=True, width="stretch")
        st.line_chart(pd.DataFrame({
            "Note /20": [r["score"] / r["total"] * 20 for r in res]
        }))

    notes = {k: v for k, v in P["notes"].items() if v.strip()}
    if notes:
        st.divider()
        st.subheader("Mes notes personnelles")
        for cle, txt in notes.items():
            with st.expander(cle):
                st.write(txt)

    st.divider()
    with st.expander("⚠️ Réinitialiser la progression"):
        st.warning("Cette action efface les fiches lues, les résultats de quiz et les notes.")
        if st.button("Tout effacer", type="secondary"):
            st.session_state.progression = {"fiches_lues": [], "resultats_quiz": [], "notes": {}}
            sauver_progression(st.session_state.progression)
            st.success("Progression réinitialisée.")
            st.rerun()


st.sidebar.divider()
st.sidebar.caption("Les calculateurs vérifient un résultat, ils ne remplacent pas "
                   "la démarche écrite attendue en examen.")
