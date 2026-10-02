# Aperçu du brouillon de la fiche 6.19, rendu avec Streamlit comme dans l'appli (sans toucher à app.py).
import base64, math, os, re
import streamlit as st

ICI = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'app.py'), encoding='utf-8').read()
g = {'math': math}
head = src[:src.index('def projection_europeenne')]
exec(head[head.index('TRAIT = '):], g)
for nom in ('def fr(', 'def _fr_court', 'def _k_defs', 'def _k_fl', 'def _k_apparait', 'def _diag('):
    i = src.index(nom); j = src.index('\ndef ', i + 10); exec(src[i:j], g)
exec(open(os.path.join(ICI, 'brouillon_6_19.py'), encoding='utf-8').read(), g)

st.set_page_config(page_title="Brouillon 6.15", layout="wide")
F = g['FICHE_6_19']


def img(svg, titre=""):
    b64 = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    return (f"<figure style='margin:18px 0'><img src='data:image/svg+xml;base64,{b64}' "
            f"style='width:100%;max-width:760px;'/><figcaption style='font-size:0.85em;color:#64748b'>"
            f"{titre}</figcaption></figure>")


def contenu(texte):
    morceaux = re.split(r"\[\[(FIG|DYN):([a-z0-9_]+)\]\]", texte)
    for i in range(0, len(morceaux), 3):
        if morceaux[i].strip():
            st.markdown(morceaux[i])
        if i + 2 < len(morceaux):
            cle = morceaux[i + 2]
            if morceaux[i + 1] == "FIG":
                t, f = g['FIGURES_NOUVELLES'][cle]
                st.markdown(img(f(), t), unsafe_allow_html=True)
            else:
                t, f, params = g['DYN_NOUVELLE'][cle]
                vals = {}
                for col, p in zip(st.columns(len(params)), params):
                    with col:
                        if "choix" in p:
                            lab = st.select_slider(p["label"], options=[e for e, _ in p["choix"]], value=p["defaut"], key="k" + p["nom"])
                            vals[p["nom"]] = dict(p["choix"])[lab]
                        else:
                            vals[p["nom"]] = st.slider(p["label"], p["min"], p["max"], p["defaut"], step=p["pas"], key="k" + p["nom"])
                st.markdown(img(f(**vals), t), unsafe_allow_html=True)


st.title(f"BROUILLON — Fiche {F['id']} · {F['titre']}")
st.caption(f"Durée : {F['duree']} · Bloc 6, insérée en fin de bloc (après la 6.18)")
ong = st.tabs(["Cours", "Formules", "Exemple", "Exercice", "Corrigé", "Méthode", "Ateliers", "Quiz", "Générateur"])
with ong[0]:
    contenu(F["cours"])
with ong[1]:
    contenu(F["formules"])
with ong[2]:
    contenu(F["exemple"])
with ong[3]:
    contenu(F["exercice"])
with ong[4]:
    contenu(F["corrige"])
with ong[5]:
    fid, titre, etapes, ex = g['MTH_6_19']
    st.markdown(f"### {titre}\n\n" + "\n".join(f"{i}. {e}" for i, e in enumerate(etapes, 1))
                + f"\n\n> **Sur un exemple.** {ex}")
with ong[6]:
    for a in g['ATELIERS_NOUVEAUX']:
        st.subheader(f"{a['id']} — {a['titre']}")
        st.markdown(img(g['FIGURES_NOUVELLES'][a['figure']][1](), ""), unsafe_allow_html=True)
        for mot, d in a["vocabulaire"]:
            st.markdown(f"- **{mot}** : {d}")
        st.info(a["enonce"])
        for k, e in enumerate(a["etapes"], 1):
            if e["type"] == "numerique":
                pi = " · ".join(f"{v:g} → {m}" for v, m in e.get("pieges", []))
                st.markdown(f"**Étape {k} — {e['label']}** ({e['unite']}) : {e['consigne']}  \n"
                            f"attendu **{e['attendu']:g}** ± {e['tol']:g} · indice : {e['indice']}  \n"
                            f"pièges : {pi}")
            else:
                ops = " / ".join(("✅ " if j == e['bonne'] else "") + o for j, o in enumerate(e["options"]))
                st.markdown(f"**Étape {k} — {e['label']}** : {e['question']}  \n{ops}")
        c = a["corrige"]
        st.markdown("**Corrigé** — " + " · ".join(f"*{k}* : {c[k]}" for k in
                    ("regle", "conversions", "remplacement", "calcul", "verification")))
        st.success(a["a_retenir"])
with ong[7]:
    for n, (qq, ops, bonne, expl, niv) in enumerate(g['QUIZ_ROULEMENTS'], 1):
        st.markdown(f"**{n}. [{niv}] {qq}**  \n" + "  \n".join(("✅ " if j == bonne else "▫️ ") + o
                                                              for j, o in enumerate(ops)))
        st.caption(expl)
with ong[8]:
    import random
    g["random"] = random
    exec(g["GENERATEUR"], g)
    SAUT = chr(10)
    for _ in range(3):
        e = g["gen_duree_roulement"]()
        st.markdown(f"**{e['titre']}**" + "  " + SAUT + e["enonce"] + "  " + SAUT
                    + f"Réponse : **{e['rep']:g} {e['unite']}** (± {e['tol']:.1f})")
        st.markdown(SAUT.join("- " + c for c in e["corr"]))
        st.caption(" · ".join(f"{d['v']:g} → {d['m']}" for d in e["diag"]))
        st.divider()
