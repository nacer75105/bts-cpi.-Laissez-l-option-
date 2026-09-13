"""Pages Streamlit de la section Part-66 (EASA B1.1).

Section indépendante des pages BTS : sa propre persistance
(progression_part66.json, via part66.logic), son propre suivi Leitner,
sa propre navigation interne (onglets), branchée sur un seul point
d'entrée dans app.py (page_part66).
"""
import random
from datetime import datetime, timedelta

import streamlit as st

from . import logic


def _options_melangees(q, seed):
    """Ordre d'affichage des options, mélangé de façon déterministe pour
    une (session ou examen, question) donnée — stable sur les reruns
    Streamlit, mais différent d'une session à l'autre, pour ne pas biaiser
    la position de la bonne réponse (cf. relecture M10)."""
    rng = random.Random(f"{seed}:{q['uid']}")
    ordre = list(range(len(q["options"])))
    rng.shuffle(ordre)
    options = [q["options"][i] for i in ordre]
    bonne_affichee = ordre.index(q["bonne"])
    return options, ordre, bonne_affichee


def _progression():
    if "p66_progression" not in st.session_state:
        st.session_state.p66_progression = logic.charger_progression()
    return st.session_state.p66_progression


def _module_courant():
    """Sélecteur de module, affiché seulement s'il y a un vrai choix à
    faire : masqué tant qu'un seul module est disponible (l'accueil reste
    alors réduit au bouton Session du jour, conformément au principe 1 de
    METHODOLOGIE.md), affiché dès qu'un second module (comme M5) est
    disponible, pour permettre de choisir lequel réviser."""
    dispo = [m for m, info in logic.MODULES.items() if info["disponible"]]
    if not dispo:
        return None
    cle = "p66_module"
    if st.session_state.get(cle) not in dispo:
        st.session_state[cle] = dispo[0]
    if len(dispo) > 1:
        st.selectbox(
            "Module",
            dispo,
            format_func=lambda m: f"{m} — {logic.MODULES[m]['titre']}",
            key=cle,
        )
    return st.session_state[cle]


def page_part66():
    st.title("Espace Part-66 — licence B1.1")
    P = _progression()
    module = _module_courant()

    if module is None:
        st.info("Aucun module n'est disponible pour l'instant.")
        return

    onglet_accueil, onglet_cours, onglet_redaction, onglet_progression, onglet_examen = st.tabs(
        ["🏠 Accueil", "📖 Cours", "✍️ Rédaction", "📊 Progression", "⏱️ Examen blanc"])
    with onglet_accueil:
        _page_accueil(P, module)
    with onglet_cours:
        _page_cours(P, module)
    with onglet_redaction:
        _page_redaction(module)
    with onglet_progression:
        _page_progression(P, module)
    with onglet_examen:
        _page_examen_blanc(P, module)


# ---------------------------------------------------------------------------
# Accueil — un seul bouton, "Session du jour" (principe 1)
# ---------------------------------------------------------------------------

def _demarrer_session(module):
    questions = logic.construire_session_du_jour(_progression(), module, taille_cible=25)
    st.session_state.p66_sess = {
        "module": module,
        "file": questions,
        "index": 0,
        "bonnes": 0,
        "total_note": len(questions),
        "on_rejeu": False,
        "ratees": [],
        "phase": "en_cours",
        "reponse_choisie": None,
        "valide": False,
        "seed": random.randint(0, 10**9),
    }


def _page_accueil(P, module):
    sess = st.session_state.get("p66_sess")
    if sess:
        _rendu_session(P, sess)
        return

    serie = logic.serie_jours_consecutifs(P)
    if serie:
        st.caption(f"🔥 {serie} jour(s) de suite")

    st.write("")
    _, col, _ = st.columns([1, 2, 1])
    with col:
        if st.button("▶️ Session du jour", type="primary", use_container_width=True):
            _demarrer_session(module)
            st.rerun()
    st.write("")
    st.caption(f"Module en cours : {module} — {logic.MODULES[module]['titre']}")


def _rendu_session(P, sess):
    if sess["phase"] == "bilan":
        _rendu_bilan(P, sess)
        return

    file = sess["file"]
    i = sess["index"]
    if i >= len(file):
        if not sess["on_rejeu"] and sess["ratees"]:
            sess["file"] = sess["ratees"]
            sess["ratees"] = []
            sess["on_rejeu"] = True
            sess["index"] = 0
            sess["reponse_choisie"] = None
            sess["valide"] = False
            st.rerun()
            return
        sess["phase"] = "bilan"
        st.rerun()
        return

    q = file[i]
    st.caption(f"Question {i + 1} / {len(file)}"
               + ("  ·  rejeu des questions ratées" if sess["on_rejeu"] else ""))
    st.subheader(q["question"])

    options, ordre, _ = _options_melangees(q, sess["seed"])
    cle_radio = f"p66_radio_{sess['module']}_{sess['on_rejeu']}_{i}"
    choix = st.radio("Ta réponse", options, index=None, key=cle_radio,
                      disabled=sess["valide"])

    if not sess["valide"]:
        if st.button("Valider", type="primary", disabled=choix is None):
            idx_choix = ordre[options.index(choix)]
            reussi = idx_choix == q["bonne"]
            sess["valide"] = True
            sess["reponse_choisie"] = idx_choix
            if not sess["on_rejeu"]:
                if reussi:
                    sess["bonnes"] += 1
                else:
                    sess["ratees"].append(q)
            logic.repondre(P, q["uid"], reussi)
            st.rerun()
        return

    idx_choix = sess["reponse_choisie"]
    if idx_choix == q["bonne"]:
        st.success("✅ Bonne réponse.")
    else:
        st.error(f"❌ Pas la bonne réponse. La bonne réponse était : {q['options'][q['bonne']]}")
    st.info(q["explication"])
    if st.button("Suivante →"):
        sess["index"] += 1
        sess["reponse_choisie"] = None
        sess["valide"] = False
        st.rerun()


def _rendu_bilan(P, sess):
    st.subheader("Session terminée")
    total = sess["total_note"]
    bonnes = sess["bonnes"]
    pct = round(100 * bonnes / total, 1) if total else 0
    st.metric("Score", f"{bonnes} / {total} ({pct} %)")

    if not sess.get("enregistre"):
        logic.enregistrer_session(P, sess["module"], total, bonnes)
        sess["enregistre"] = True

    if st.button("Retour à l'accueil"):
        del st.session_state["p66_sess"]
        st.rerun()


# ---------------------------------------------------------------------------
# Cours
# ---------------------------------------------------------------------------

_NIVEAU_LEGENDE = """\
**Niveau 1 — notions générales** : tu dois reconnaître et décrire
simplement le sujet, avec des mots courants et des exemples — pas
besoin de savoir l'appliquer en détail.

**Niveau 2 — connaissance générale** : tu dois comprendre la théorie du
sujet, en donner une description avec des exemples typiques, lire des
schémas qui le concernent, et l'appliquer en suivant une procédure
détaillée.

**Niveau 3 — connaissance détaillée** : le niveau le plus exigeant. Tu
dois maîtriser la théorie en profondeur, savoir comment ce sujet
s'articule avec d'autres, et être capable d'interpréter un résultat
concret (une mesure, un symptôme) pour décider de la bonne action.

Plus le niveau est élevé, plus la fiche mérite de temps de révision et
d'entraînement — c'est indicatif, mais ça aide à doser ton effort.
(Source : Part-66 Appendix I, EASA *Easy Access Rules for Continuing
Airworthiness*.)
"""


def _page_cours(P, module):
    fiches = logic.charger_fiches(module)
    if not fiches:
        st.info("Pas encore de fiches pour ce module.")
        return
    if any("niveau" in fiche for fiche in fiches):
        with st.expander("ℹ️ Niveaux de connaissance (1/2/3) — ce que ça change pour réviser"):
            st.markdown(_NIVEAU_LEGENDE)
    for fiche in fiches:
        with st.expander(f"{fiche['id']} — {fiche['titre']}", key=f"p66_expander_{module}_{fiche['id']}"):
            legende = f"{fiche['sous_chapitre']} · ⏱ {fiche.get('duree_min', '?')} min"
            if fiche.get("item_syllabus"):
                legende += f" · Item officiel {fiche['item_syllabus']}"
            if "niveau" in fiche and not fiche.get("niveau_note"):
                legende += f" · Niveau {fiche['niveau']}"
            st.caption(legende)
            if fiche.get("niveau_note"):
                st.caption(f"⚠️ {fiche['niveau_note']}")
            st.markdown(fiche["contenu_md"])
            for schema in logic.charger_schemas(module, fiche["id"]):
                st.html(schema, unsafe_allow_javascript=True)


# ---------------------------------------------------------------------------
# Rédaction — sujets type examen (essays), pas de notation automatique
# ---------------------------------------------------------------------------

def _page_redaction(module):
    essais = logic.charger_essais(module)
    if not essais:
        st.info(
            "Ce module n'a pas d'épreuve rédactionnelle à l'examen "
            "(seul le Module 7 — M7A — en comporte une pour l'instant).")
        return
    st.caption(
        "Rédige ta réponse sur papier, chronomètre en main — c'est ce que tu "
        "feras à l'examen. Le temps indiqué sous chaque sujet est celui du "
        "format réel de l'épreuve. Ne déroule le corrigé qu'une fois ta copie "
        "terminée : il n'y a pas de notation automatique ici, c'est à toi de "
        "comparer ton travail au corrigé.")
    for essai in essais:
        with st.expander(f"{essai['uid']} — {essai['titre']}", key=f"p66_essai_{module}_{essai['uid']}"):
            st.caption(f"{essai['sous_chapitre']} · ⏱ {essai.get('temps_indicatif_min', '?')} min")
            st.markdown(f"**Sujet :** {essai['enonce']}")
            with st.expander("Voir le corrigé"):
                st.markdown(essai["corrige_md"])
                if essai.get("erreurs_frequentes"):
                    st.warning("**Erreurs fréquentes à éviter sur ce sujet :**\n\n"
                               + "\n".join(f"- {e}" for e in essai["erreurs_frequentes"]))


# ---------------------------------------------------------------------------
# Progression — par sous-chapitre (principe 6), pas de score global
# ---------------------------------------------------------------------------

def _page_progression(P, module):
    st.markdown("### Taux de maîtrise par sous-chapitre")
    taux = logic.progression_par_sous_chapitre(P, module)
    if not taux:
        st.info("Pas encore de questions suivies pour ce module.")
    else:
        for sc, pct in sorted(taux.items()):
            st.caption(f"{sc} — {pct} %")
            st.progress(min(100, max(0, int(pct))) / 100)

    st.divider()
    st.markdown("### Examens blancs")
    blancs = [e for e in P.get("examens_blancs", []) if e["module"] == module]
    if not blancs:
        st.caption("Aucun examen blanc passé pour ce module.")
    else:
        for e in blancs[:10]:
            statut = "✅ Réussi" if e["reussi"] else "❌ Échoué"
            st.write(f"{e['date']} — {e['note_pct']} % ({e['bonnes']}/{e['nb_questions']}) — {statut}")

    if logic.peut_reserver_examen_reel(P, module):
        st.success(
            f"Tu as réussi {logic.NB_BLANCS_CONSECUTIFS_REQUIS} examens blancs consécutifs à "
            f"{logic.SEUIL_RESERVATION_EXAMEN_REEL_PCT} % ou plus : c'est le moment de "
            "réserver l'examen réel.")
    else:
        st.caption(
            f"Ne réserve l'examen réel qu'après {logic.NB_BLANCS_CONSECUTIFS_REQUIS} examens "
            f"blancs consécutifs à {logic.SEUIL_RESERVATION_EXAMEN_REEL_PCT} % ou plus.")


# ---------------------------------------------------------------------------
# Examen blanc — séparé du mode révision (principe 7)
# ---------------------------------------------------------------------------

def _page_examen_blanc(P, module):
    E = st.session_state.get("p66_exam")
    if not E or E.get("module") != module:
        E = {"phase": "reglage", "module": module}
        st.session_state.p66_exam = E

    infos = logic.MODULES[module]

    if E["phase"] == "reglage":
        st.caption(
            f"Épreuve dans les conditions réelles : {infos['nb_questions_examen']} questions, "
            f"{infos['duree_examen_min']} minutes, aucune correction avant la fin, seuil de "
            f"réussite {logic.SEUIL_REUSSITE_EXAMEN_PCT} %.")
        if st.button("Commencer l'examen blanc", type="primary"):
            questions, duree = logic.construire_examen_blanc(module)
            E.update({"phase": "epreuve", "questions": questions,
                      "reponses": [None] * len(questions),
                      "debut": datetime.now().isoformat(), "duree_min": duree, "index": 0,
                      "seed": random.randint(0, 10**9)})
            st.rerun()
        return

    if E["phase"] == "epreuve":
        qs = E["questions"]
        reste = (timedelta(minutes=E["duree_min"])
                 - (datetime.now() - datetime.fromisoformat(E["debut"])))
        secondes = int(reste.total_seconds())

        c1, c2, c3 = st.columns(3)
        c1.metric("Question", f"{E['index'] + 1} / {len(qs)}")
        c2.metric("Répondues", sum(1 for r in E["reponses"] if r is not None))
        c3.metric("Temps restant", f"{max(0, secondes) // 60:02d}:{max(0, secondes) % 60:02d}")
        if secondes <= 0:
            st.error("Le temps est écoulé. La copie est ramassée.")
            E["phase"] = "bilan"
            st.rerun()
            return

        st.divider()
        q = qs[E["index"]]
        st.caption(q["sous_chapitre"])
        st.subheader(q["question"])
        options, ordre, _ = _options_melangees(q, E["seed"])
        actuelle = E["reponses"][E["index"]]
        index_affiche = ordre.index(actuelle) if actuelle is not None else None
        choix = st.radio("Ta réponse", options,
                          index=index_affiche,
                          key=f"p66_exam_q{E['index']}")
        if choix is not None:
            E["reponses"][E["index"]] = ordre[options.index(choix)]

        b1, b2, b3 = st.columns([1, 1, 2])
        if b1.button("← Précédente", disabled=E["index"] == 0):
            E["index"] -= 1
            st.rerun()
        if b2.button("Suivante →", disabled=E["index"] >= len(qs) - 1):
            E["index"] += 1
            st.rerun()
        if b3.button("Terminer et corriger", type="primary"):
            E["phase"] = "bilan"
            st.rerun()
        return

    qs, reps = E["questions"], E["reponses"]
    bonnes = sum(1 for q, r in zip(qs, reps) if r == q["bonne"])
    if not E.get("enregistre"):
        note_pct = logic.enregistrer_examen_blanc(P, module, len(qs), bonnes, E["duree_min"])
        E["enregistre"] = True
        E["note_pct"] = note_pct
    note_pct = E.get("note_pct", round(100 * bonnes / len(qs), 1) if qs else 0)

    statut = "Réussi ✅" if note_pct >= logic.SEUIL_REUSSITE_EXAMEN_PCT else "Échoué ❌"
    st.subheader(f"{statut} — {note_pct} % ({bonnes}/{len(qs)})")

    st.divider()
    st.markdown("### Correction, question par question")
    for i, (q, r) in enumerate(zip(qs, reps), 1):
        juste = r == q["bonne"]
        with st.expander(f"{'✅' if juste else '❌'} Question {i} — {q['question'][:70]}…"):
            st.write(f"Ta réponse : {q['options'][r] if r is not None else 'aucune réponse'}")
            st.write(f"Bonne réponse : {q['options'][q['bonne']]}")
            st.info(q["explication"])

    if st.button("Retour au réglage"):
        st.session_state.p66_exam = {"phase": "reglage", "module": module}
        st.rerun()
