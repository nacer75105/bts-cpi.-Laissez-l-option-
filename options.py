# -*- coding: utf-8 -*-
"""
options.py — les fonctions ajoutées à l'application BTS CPI.

Tout ce qui est ici reprend ce qui existe déjà dans les cahiers de maths et de
physique-chimie, adapté à Streamlit et au contenu du BTS :

    1. les vidéos de fiche, avec la recherche YouTube déjà remplie
    2. le corrigé dévoilé étape par étape
    3. la révision espacée : une question ratée revient, de plus en plus tard
    4. le mode contrôle : chronométré, noté sur 20, corrigé à la fin
    5. l'aide-mémoire : toutes les formules et toutes les méthodes réunies
    6. l'entraînement illimité : des exercices tirés au hasard, corrigés en
       six étapes, avec un diagnostic pour chaque erreur classique

Le module ne connaît pas l'application : il reçoit le dictionnaire de
progression et la fonction qui l'enregistre. Il peut donc être testé seul.
"""

import math
import random
import re
from datetime import datetime, timedelta

import streamlit as st


# ===========================================================================
# OUTILS COMMUNS
# ===========================================================================

def fr(x, d=2):
    """Un nombre à la française : virgule décimale, espace des milliers."""
    if x is None:
        return "—"
    if isinstance(x, int) or (isinstance(x, float) and abs(x - round(x)) < 1e-9 and abs(x) < 1e6):
        t = f"{int(round(x)):,}".replace(",", " ")
    else:
        t = f"{x:,.{d}f}".replace(",", " ").replace(".", ",")
    return t


def lire_nombre(txt):
    """Accepte 3,5 · 3.5 · 7/2 · 2,5e-3 · 6,02x10^23 — comme au clavier."""
    if txt is None:
        return None
    s = str(txt).strip().replace(" ", "").replace(" ", "").replace(",", ".")
    s = s.replace("−", "-").lstrip("+")
    if not s:
        return None
    m = re.match(r"^(-?\d+(?:\.\d+)?)[×x*·]?10\^?\(?(-?\d+)\)?$", s, re.I)
    if m:
        return float(m.group(1)) * 10 ** int(m.group(2))
    m = re.match(r"^(-?\d+(?:\.\d+)?)/(-?\d+(?:\.\d+)?)$", s)
    if m:
        return float(m.group(1)) / float(m.group(2))
    try:
        return float(s)
    except ValueError:
        return None


# ===========================================================================
# 1. LES VIDÉOS DE FICHE
# ---------------------------------------------------------------------------
# Aucune adresse n'est fournie d'avance : un lien inventé mène à une page
# morte, ce qui est pire que pas de vidéo du tout. L'application amène devant
# les résultats de recherche, l'étudiant juge, et rapporte l'adresse.
# ===========================================================================

def analyser_video(url):
    """Renvoie (mode, adresse, hébergeur) ou None si la source n'est pas acceptée."""
    u = (url or "").strip()
    if not re.match(r"^https?://", u, re.I):
        return None

    debut = 0
    m = re.search(r"[?&#]t=(\d+)m(\d+)s", u)
    if m:
        debut = int(m.group(1)) * 60 + int(m.group(2))
    else:
        m = re.search(r"[?&#](?:t|start)=(\d+)", u)
        if m:
            debut = int(m.group(1))

    m = re.search(r"(?:youtube\.com/(?:watch\?(?:.*&)?v=|embed/|shorts/|live/)"
                  r"|youtu\.be/)([A-Za-z0-9_-]{11})", u, re.I)
    if m:
        src = "https://www.youtube-nocookie.com/embed/" + m.group(1) + "?rel=0"
        if debut:
            src += "&start=%d" % debut
        return ("cadre", src, "YouTube")

    m = re.search(r"vimeo\.com/(?:video/)?(\d+)", u, re.I)
    if m:
        return ("cadre", "https://player.vimeo.com/video/" + m.group(1), "Vimeo")

    m = re.search(r"dailymotion\.com/(?:video/|embed/video/)([A-Za-z0-9]+)", u, re.I)
    if m:
        return ("cadre", "https://www.dailymotion.com/embed/video/" + m.group(1), "Dailymotion")

    if re.search(r"\.(mp4|webm|ogv|ogg)(\?.*)?$", u, re.I):
        return ("fichier", u, "fichier vidéo")

    return None


def afficher_video(v):
    """Un lecteur, avec son titre. Les sources non reconnues sont signalées."""
    info = analyser_video(v.get("url", ""))
    st.markdown(f"**{v.get('titre') or 'Vidéo'}**")
    if not info:
        st.warning("Adresse non reconnue. L'application accepte les liens YouTube, "
                   "Vimeo, Dailymotion, et les fichiers .mp4 ou .webm.")
        st.write(v.get("url", ""))
        return
    mode, src, hote = info
    if mode == "fichier":
        st.video(src)
    else:
        st.components.v1.iframe(src, height=340, scrolling=False)
    st.caption(hote)


def zone_videos(P, sauver, cle, titre_fiche):
    """L'onglet « Vidéos » d'une fiche."""
    P.setdefault("videos", {})
    liste = P["videos"].get(cle, [])

    if liste:
        st.caption("Les vidéos que tu as ajoutées pour cette fiche. "
                   "Elles sont enregistrées avec ta progression.")
        for i, v in enumerate(liste):
            afficher_video(v)
            if st.button("Retirer cette vidéo", key=f"delvid_{cle}_{i}"):
                P["videos"][cle].pop(i)
                if not P["videos"][cle]:
                    del P["videos"][cle]
                sauver(P)
                st.rerun()
            st.divider()
    else:
        st.caption("Aucune vidéo pour l'instant. Ajoute le lien d'une vidéo qui "
                   "explique bien cette fiche — un tuto SolidWorks, une capsule "
                   "de cours — et elle restera rangée ici.")

    st.markdown("##### Ajouter une vidéo")
    st.markdown(
        "1. Clique sur le bouton ci-dessous : la recherche YouTube s'ouvre dans un "
        "autre onglet, **déjà remplie**.\n"
        "2. Choisis une vidéo, ouvre-la, et vérifie qu'elle te convient.\n"
        "3. Copie l'adresse dans la barre du navigateur — elle commence par "
        "`youtube.com/watch` — puis reviens ici et colle-la.")

    requete = f"{titre_fiche} BTS CPI conception produits industriels"
    st.link_button("Chercher sur YouTube ↗",
                   "https://www.youtube.com/results?search_query=" +
                   requete.replace(" ", "+"))

    url = st.text_input("Adresse de la vidéo", key=f"vidurl_{cle}",
                        placeholder="https://www.youtube.com/watch?v=...")
    nom = st.text_input("Titre, pour t'y retrouver (facultatif)", key=f"vidnom_{cle}")

    if url:
        info = analyser_video(url)
        if info:
            st.success(f"Lien reconnu ({info[2]}).")
            afficher_video({"titre": nom or "Aperçu", "url": url})
        else:
            st.error("Adresse non reconnue — YouTube, Vimeo, Dailymotion "
                     "ou un fichier .mp4.")

    if st.button("Ajouter à la fiche", key=f"vidadd_{cle}", type="primary"):
        if not url:
            st.warning("Colle d'abord une adresse.")
        elif not analyser_video(url):
            st.error("Cette adresse n'est pas reconnue.")
        else:
            P["videos"].setdefault(cle, []).append(
                {"titre": nom.strip() or f"Vidéo — {titre_fiche}", "url": url.strip()})
            sauver(P)
            st.success("Vidéo ajoutée.")
            st.rerun()


# ===========================================================================
# 2. LE CORRIGÉ DÉVOILÉ ÉTAPE PAR ÉTAPE
# ---------------------------------------------------------------------------
# Un corrigé lu d'un bloc donne l'illusion de comprendre. On le découpe sur
# ses titres de niveau 3, ou à défaut sur ses paragraphes, et on l'ouvre une
# étape à la fois.
# ===========================================================================

def decouper_corrige(texte):
    if not texte:
        return []
    morceaux = re.split(r"\n(?=###\s)", texte.strip())
    if len(morceaux) > 1:
        return [m.strip() for m in morceaux if m.strip()]
    morceaux = [m.strip() for m in re.split(r"\n\s*\n", texte.strip()) if m.strip()]
    if len(morceaux) <= 1:
        return morceaux
    # on regroupe par deux pour éviter les étapes d'une seule ligne
    groupes, tampon = [], []
    for m in morceaux:
        tampon.append(m)
        if len("\n\n".join(tampon)) > 220:
            groupes.append("\n\n".join(tampon))
            tampon = []
    if tampon:
        groupes.append("\n\n".join(tampon))
    return groupes


def corrige_progressif(texte, cle, afficher):
    """Affiche le corrigé une étape à la fois. `afficher` rend le markdown."""
    etapes = decouper_corrige(texte)
    if not etapes:
        st.info("Pas de corrigé pour cette fiche.")
        return

    k = f"corr_{cle}"
    st.session_state.setdefault(k, 0)
    vues = st.session_state[k]

    if vues == 0:
        st.markdown('<div class="warn-box">Le corrigé se dévoile étape par étape. '
                    "Arrête-toi dès que tu as compris : c'est le moment où tu "
                    "apprends le plus.</div>", unsafe_allow_html=True)

    for i in range(vues):
        st.markdown(f"**Étape {i + 1} sur {len(etapes)}**")
        afficher(etapes[i])
        st.divider()

    c1, c2, c3 = st.columns([1, 1, 2])
    if vues < len(etapes):
        with c1:
            if st.button("Étape suivante" if vues else "Première étape", key=f"btn_{k}",
                         type="primary"):
                st.session_state[k] = vues + 1
                st.rerun()
        with c2:
            if st.button("Tout afficher", key=f"all_{k}"):
                st.session_state[k] = len(etapes)
                st.rerun()
        with c3:
            st.caption(f"{vues} / {len(etapes)} étapes")
    else:
        with c1:
            if st.button("Replier", key=f"reset_{k}"):
                st.session_state[k] = 0
                st.rerun()


# ===========================================================================
# 3. LA RÉVISION ESPACÉE
# ---------------------------------------------------------------------------
# Chaque question ratée devient une carte. À chaque réussite elle monte d'un
# cran et revient plus tard ; à chaque échec elle retombe au premier cran.
# ===========================================================================

PALIERS = [0, 1, 3, 7, 16, 35, 70]          # en jours


def srs_maj(P, sauver, uid, reussi, libelle=""):
    P.setdefault("srs", {})
    carte = P["srs"].get(uid)
    aujourd = datetime.now()
    if not reussi:
        P["srs"][uid] = {
            "palier": 0,
            "du": aujourd.isoformat(),
            "ratages": (carte or {}).get("ratages", 0) + 1,
            "libelle": libelle or (carte or {}).get("libelle", ""),
        }
    elif carte:
        p = min(carte.get("palier", 0) + 1, len(PALIERS) - 1)
        if p >= len(PALIERS) - 1:
            del P["srs"][uid]                # acquise : on retire la carte
        else:
            carte["palier"] = p
            carte["du"] = (aujourd + timedelta(days=PALIERS[p])).isoformat()
    sauver(P)


def srs_dues(P):
    maintenant = datetime.now()
    out = []
    for uid, c in (P.get("srs") or {}).items():
        try:
            if datetime.fromisoformat(c["du"]) <= maintenant:
                out.append((uid, c))
        except (ValueError, KeyError):
            out.append((uid, c))
    return sorted(out, key=lambda x: x[1].get("du", ""))


def srs_quand(carte):
    try:
        d = (datetime.fromisoformat(carte["du"]) - datetime.now()).days
    except (ValueError, KeyError):
        return "à réviser maintenant"
    if d <= 0:
        return "à réviser maintenant"
    if d == 1:
        return "demain"
    if d < 14:
        return f"dans {d} jours"
    return f"dans {max(1, round(d / 7))} semaine(s)"


def page_revoir(P, sauver, qz):
    st.title("À revoir")
    st.caption("Chaque question ratée revient ici, de plus en plus espacée dans le "
               "temps. C'est la façon la plus économique de retenir durablement.")

    toutes = {q["uid"]: q for q in qz.toutes_les_questions()}
    dues = [(uid, c) for uid, c in srs_dues(P) if uid in toutes]
    total = len([u for u in (P.get("srs") or {}) if u in toutes])

    c1, c2 = st.columns(2)
    c1.metric("Cartes à réviser aujourd'hui", len(dues))
    c2.metric("Cartes en cours", total)

    if not total:
        st.success("Aucune carte pour l'instant. Les questions ratées au quiz ou "
                   "en contrôle viendront se ranger ici automatiquement.")
        return
    if not dues:
        st.info("Rien à réviser aujourd'hui — tout est à jour. Les prochaines cartes "
                "reviendront d'elles-mêmes.")
        with st.expander("Voir les cartes programmées"):
            for uid, c in sorted((P.get("srs") or {}).items(),
                                 key=lambda x: x[1].get("du", "")):
                if uid in toutes:
                    st.write(f"• {toutes[uid]['question'][:80]}… — {srs_quand(c)}")
        return

    uid, carte = dues[0]
    q = toutes[uid]
    st.divider()
    st.caption(f"{q['categorie']} · ratée {carte.get('ratages', 1)} fois")
    st.subheader(q["question"])

    k = f"rev_{uid}"
    choix = st.radio("Ta réponse", q["options"], index=None, key=k)
    if st.button("Vérifier", key=f"btnrev_{uid}", type="primary"):
        if choix is None:
            st.warning("Choisis une réponse.")
        else:
            juste = q["options"].index(choix) == q["correct"]
            if juste:
                st.success("Bonne réponse. La carte revient plus tard.")
            else:
                st.error(f"Non. La bonne réponse était : **{q['options'][q['correct']]}**")
            st.info(q["explication"])
            srs_maj(P, sauver, uid, juste, q["question"][:80])
            if st.button("Carte suivante", key=f"next_{uid}"):
                st.rerun()


# ===========================================================================
# 4. LE MODE CONTRÔLE
# ---------------------------------------------------------------------------
# Chronométré, sans correction en direct, noté sur 20. Les questions ratées
# alimentent la révision espacée.
# ===========================================================================

def page_controle(P, sauver, qz):
    st.title("Mode contrôle")
    E = st.session_state.setdefault("ctl", {"phase": "reglage"})

    # ------------------------------------------------------------- réglages
    if E["phase"] == "reglage":
        st.caption("Un devoir chronométré, sans correction en direct. La correction "
                   "complète arrive à la fin, question par question, et les erreurs "
                   "sont envoyées en révision espacée.")
        cats = st.multiselect("Thèmes", qz.CATEGORIES, default=qz.CATEGORIES)
        c1, c2 = st.columns(2)
        nb = c1.slider("Nombre de questions", 5, 30, 12)
        minutes = c2.slider("Durée (minutes)", 5, 60, 20)

        pool = [q for q in qz.toutes_les_questions() if q["categorie"] in cats]
        st.caption(f"{len(pool)} questions disponibles sur les thèmes choisis.")

        if st.button("Commencer le contrôle", type="primary", disabled=not pool):
            random.shuffle(pool)
            E.update({"phase": "epreuve", "questions": pool[:nb],
                      "reponses": [None] * min(nb, len(pool)),
                      "debut": datetime.now().isoformat(), "minutes": minutes,
                      "index": 0})
            st.rerun()
        return

    # ------------------------------------------------------------- épreuve
    if E["phase"] == "epreuve":
        qs = E["questions"]
        reste = (timedelta(minutes=E["minutes"]) -
                 (datetime.now() - datetime.fromisoformat(E["debut"])))
        secondes = int(reste.total_seconds())

        c1, c2, c3 = st.columns([1, 1, 1])
        c1.metric("Question", f"{E['index'] + 1} / {len(qs)}")
        c2.metric("Répondues", sum(1 for r in E["reponses"] if r is not None))
        c3.metric("Temps restant", f"{max(0, secondes) // 60:02d}:{max(0, secondes) % 60:02d}")
        if secondes <= 0:
            st.error("Le temps est écoulé. La copie est ramassée.")
            E["phase"] = "bilan"
            st.rerun()
        st.caption("Le temps affiché se met à jour à chaque action. "
                   "Tu peux revenir en arrière tant qu'il reste du temps.")
        st.divider()

        q = qs[E["index"]]
        st.caption(q["categorie"] + " · " + q.get("niveau", ""))
        st.subheader(q["question"])
        actuelle = E["reponses"][E["index"]]
        choix = st.radio("Ta réponse", q["options"],
                         index=actuelle if actuelle is not None else None,
                         key=f"ctl_q{E['index']}")
        if choix is not None:
            E["reponses"][E["index"]] = q["options"].index(choix)

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

    # ------------------------------------------------------------- bilan
    qs, reps = E["questions"], E["reponses"]
    bons = sum(1 for q, r in zip(qs, reps) if r == q["correct"])
    note = round(20 * bons / len(qs), 1) if qs else 0

    st.subheader(f"Note : {note} / 20")
    c1, c2, c3 = st.columns(3)
    c1.metric("Bonnes réponses", f"{bons} / {len(qs)}")
    c2.metric("Sans réponse", sum(1 for r in reps if r is None))
    duree = datetime.now() - datetime.fromisoformat(E["debut"])
    c3.metric("Temps passé", f"{int(duree.total_seconds()) // 60} min")

    if not E.get("enregistre"):
        P.setdefault("controles", []).insert(0, {
            "date": datetime.now().isoformat(timespec="minutes"),
            "note": note, "questions": len(qs), "bonnes": bons})
        for q, r in zip(qs, reps):
            srs_maj(P, sauver, q["uid"], r == q["correct"], q["question"][:80])
        sauver(P)
        E["enregistre"] = True

    st.divider()
    st.markdown("### La correction, question par question")
    for i, (q, r) in enumerate(zip(qs, reps), 1):
        juste = r == q["correct"]
        with st.expander(f"{'✅' if juste else '❌'} Question {i} — {q['question'][:70]}…",
                         expanded=not juste):
            st.write(q["question"])
            for j, opt in enumerate(q["options"]):
                marque = "✅" if j == q["correct"] else ("❌" if j == r else "　")
                st.write(f"{marque} {opt}")
            if r is None:
                st.caption("Tu n'as pas répondu à cette question.")
            st.info(q["explication"])

    if st.button("Nouveau contrôle"):
        st.session_state["ctl"] = {"phase": "reglage"}
        st.rerun()


# ===========================================================================
# 5. L'AIDE-MÉMOIRE
# ---------------------------------------------------------------------------
# Rien n'est écrit deux fois : les formules et les méthodes sont ramassées
# dans les fiches elles-mêmes.
# ===========================================================================

def page_memo(BLOCS, afficher):
    st.title("Aide-mémoire")
    st.caption("Rassemblé automatiquement depuis les fiches. Les formules pour "
               "réviser, les méthodes pour savoir par où commencer devant un exercice.")

    onglet = st.radio("Quoi réviser ?", ["Les formules", "Les méthodes"],
                      horizontal=True, label_visibility="collapsed")
    champ = "formules" if onglet == "Les formules" else "methode"

    total = 0
    for bloc in BLOCS:
        fiches = bloc.get("fiches", [])
        if isinstance(fiches, dict):
            fiches = list(fiches.values())
        morceaux = [(f.get("id", ""), f.get("titre", ""), f.get(champ, ""))
                    for f in fiches if f.get(champ)]
        if not morceaux:
            continue
        st.markdown(f"### {bloc['titre']}")
        for fid, titre, contenu in morceaux:
            total += 1
            with st.expander(f"{fid} — {titre}", expanded=False):
                afficher(contenu)
    if total == 0:
        st.info("Aucun contenu pour cette rubrique.")
    else:
        st.caption(f"{total} fiches contiennent une rubrique « {onglet.lower()} ».")


# ===========================================================================
# 6. L'ENTRAÎNEMENT ILLIMITÉ
# ---------------------------------------------------------------------------
# Les nombres changent à chaque tirage, mais les diagnostics d'erreur sont
# recalculés avec eux : le message reste juste, quels que soient les nombres.
# ===========================================================================

def _diag(valeur, message):
    return {"v": valeur, "m": message}


def gen_iso_jeu(iso286):
    """Jeu maximal d'un ajustement ISO, à partir des tables officielles."""
    dim = random.choice([12, 16, 20, 25, 30, 40, 50, 63, 80, 100])
    ajust = random.choice(["H7/g6", "H7/h6", "H7/f7", "H8/e8", "H9/d9"])
    al, ar = ajust.split("/")
    r = iso286.calcul_ajustement(dim, al[0], al[1:], ar[0], ar[1:])
    jmax, jmin = r["jeu_maxi"], r["jeu_mini"]
    return {
        "titre": "Ajustement ISO — jeu maximal",
        "enonce": (f"Un ajustement **⌀{dim} {ajust}** est monté sur un mécanisme. "
                   f"Quel est le **jeu maximal**, en micromètres ?"),
        "rep": jmax, "tol": 0.6, "unite": "µm",
        "diag": [
            _diag(jmin, "C'est le jeu **minimal**. Le jeu maximal se produit dans le cas "
                        "le plus défavorable : alésage au maximum, arbre au minimum."),
            _diag(r["IT_alesage"], "C'est l'intervalle de tolérance de l'alésage seul. "
                                   "Le jeu combine les deux pièces."),
            _diag(r["IT_arbre"], "C'est l'intervalle de tolérance de l'arbre seul. "
                                 "Le jeu se calcule à partir des deux."),
        ],
        "corr": [
            f"**Ce que dit l'énoncé.** Un ajustement ⌀{dim} {ajust}. On cherche le jeu "
            "maximal, c'est-à-dire l'espace le plus grand possible entre l'arbre et l'alésage.",
            "**Quand le jeu est-il maximal ?** Quand l'alésage est au plus grand et l'arbre "
            "au plus petit — les deux écarts jouent dans le même sens.",
            f"**Les cotes de l'alésage.** {al} donne un alésage entre "
            f"{fr(r['alesage_mini'], 3)} et {fr(r['alesage_maxi'], 3)} mm.",
            f"**Les cotes de l'arbre.** {ar} donne un arbre entre "
            f"{fr(r['arbre_mini'], 3)} et {fr(r['arbre_maxi'], 3)} mm.",
            f"**Je soustrais.** Jeu maxi = alésage maxi − arbre mini = "
            f"{fr(r['alesage_maxi'], 3)} − {fr(r['arbre_mini'], 3)} = {fr(jmax, 0)} µm.",
            f"**Je vérifie.** Le jeu minimal vaut {fr(jmin, 0)} µm : il est bien plus petit, "
            "et tous deux sont positifs, ce qui confirme un ajustement avec jeu.",
        ],
        "indice": "Alésage au maximum, arbre au minimum : c'est le cas le plus défavorable.",
    }


def gen_iso_it(iso286):
    """Valeur d'un intervalle de tolérance."""
    dim = random.choice([10, 18, 25, 35, 45, 60, 75, 90, 120])
    grade = random.choice(["6", "7", "8", "9"])
    it = iso286.valeur_it(dim, grade)
    return {
        "titre": "Intervalle de tolérance IT",
        "enonce": (f"Quelle est la valeur de l'intervalle de tolérance **IT{grade}** "
                   f"pour une cote nominale de **{dim} mm** ? Réponds en micromètres."),
        "rep": it, "tol": 0.6, "unite": "µm",
        "diag": [
            _diag(iso286.valeur_it(dim, str(int(grade) + 1)),
                  f"C'est la valeur de l'IT{int(grade) + 1}. Un grade plus grand signifie "
                  "une tolérance plus large, donc une pièce moins précise."),
            _diag(iso286.valeur_it(dim, str(max(1, int(grade) - 1))),
                  f"C'est la valeur de l'IT{max(1, int(grade) - 1)}. Attention au grade demandé."),
            _diag(it / 1000.0, "Ton résultat est en millimètres. La question demande des "
                               "micromètres : il y a un facteur 1000."),
        ],
        "corr": [
            f"**Ce que demande la question.** La largeur de la zone de tolérance pour un "
            f"grade IT{grade} et une cote de {dim} mm.",
            "**Où se lit cette valeur.** Dans la table ISO 286-1, qui croise deux entrées : "
            "la tranche de dimension et le grade.",
            f"**Je repère la tranche.** {dim} mm tombe dans la tranche qui contient cette cote.",
            f"**Je lis la colonne IT{grade}.**",
            f"**Je lis la valeur.** IT{grade} = {fr(it, 0)} µm.",
            "**Ce qu'il faut retenir.** Plus le grade est petit, plus la pièce est précise — "
            "et plus elle coûte cher à fabriquer.",
        ],
        "indice": "Table ISO 286-1 : une ligne par tranche de dimension, une colonne par grade.",
    }


def gen_traction_sigma():
    """Contrainte normale dans une pièce tendue."""
    F = random.choice([2000, 3500, 5000, 8000, 12000, 20000])
    d = random.choice([8, 10, 12, 16, 20, 25])
    S = math.pi * d * d / 4
    sigma = F / S
    return {
        "titre": "Traction — contrainte normale",
        "enonce": (f"Une barre cylindrique de **diamètre {d} mm** est tendue par un effort "
                   f"de **{fr(F, 0)} N**. Quelle est la contrainte normale, en MPa ?"),
        "rep": round(sigma, 2), "tol": max(0.5, sigma * 0.02), "unite": "MPa",
        "diag": [
            _diag(round(F / (math.pi * d * d), 2),
                  "Tu as oublié le facteur 4 : l'aire d'un disque est πd²/4, pas πd²."),
            _diag(round(F / d, 2),
                  "Tu as divisé par le diamètre au lieu de l'aire. Une contrainte est une "
                  "force par unité de **surface**."),
            _diag(round(F / (math.pi * d), 2),
                  "Tu as divisé par le périmètre. C'est l'aire de la section qui compte."),
        ],
        "corr": [
            f"**Ce que dit l'énoncé.** Un effort de traction de {fr(F, 0)} N sur une barre "
            f"de diamètre {d} mm. On cherche la contrainte.",
            "**La formule.** σ = N / S : l'effort divisé par l'aire de la section droite.",
            f"**L'aire d'un disque.** S = πd²/4 = π × {d}² / 4 = {fr(S, 1)} mm². "
            "Le facteur 4 est l'oubli le plus fréquent.",
            f"**Je remplace.** σ = {fr(F, 0)} / {fr(S, 1)}.",
            f"**Je calcule.** σ = {fr(sigma, 2)} MPa.",
            "**Je vérifie l'unité.** Des newtons divisés par des mm² donnent des N/mm², "
            "c'est-à-dire des MPa. C'est tout l'intérêt de travailler en N et en mm.",
        ],
        "indice": "σ = N/S, avec S = πd²/4. Le facteur 4 est indispensable.",
    }


def gen_traction_diametre():
    """Diamètre minimal d'une pièce tendue, avec coefficient de sécurité."""
    F = random.choice([5000, 10000, 15000, 25000, 40000])
    Re = random.choice([235, 275, 355, 500, 700])
    s = random.choice([2, 2.5, 3, 4])
    Rpe = Re / s
    S = F / Rpe
    d = math.sqrt(4 * S / math.pi)
    return {
        "titre": "Traction — diamètre minimal",
        "enonce": (f"Une tige doit supporter **{fr(F, 0)} N** en traction. Le matériau a "
                   f"**Re = {Re} MPa** et l'on prend un coefficient de sécurité **s = {fr(s, 1)}**. "
                   "Quel est le diamètre minimal, en mm ?"),
        "rep": round(d, 2), "tol": max(0.05, d * 0.02), "unite": "mm",
        "diag": [
            _diag(round(math.sqrt(4 * (F / Re) / math.pi), 2),
                  "Tu as dimensionné sur Re, sans appliquer le coefficient de sécurité. "
                  "La contrainte admissible vaut Rpe = Re / s."),
            _diag(round(S, 2),
                  "C'est l'aire de la section, en mm², pas le diamètre. Il reste à remonter "
                  "au diamètre par d = √(4S/π)."),
            _diag(round(Rpe, 2),
                  "C'est la contrainte admissible, en MPa. La question porte sur un diamètre."),
        ],
        "corr": [
            f"**Ce que dit l'énoncé.** Un effort de {fr(F, 0)} N, une limite élastique de "
            f"{Re} MPa, un coefficient de sécurité de {fr(s, 1)}.",
            f"**Étape 1 — la contrainte admissible.** Rpe = Re / s = {Re} / {fr(s, 1)} = "
            f"{fr(Rpe, 1)} MPa. C'est la contrainte qu'on s'autorise, jamais Re.",
            "**Étape 2 — la condition de résistance.** σ ≤ Rpe, c'est-à-dire N/S ≤ Rpe.",
            f"**Étape 3 — l'aire minimale.** S ≥ N / Rpe = {fr(F, 0)} / {fr(Rpe, 1)} = "
            f"{fr(S, 1)} mm².",
            f"**Étape 4 — le diamètre.** S = πd²/4 donne d = √(4S/π) = {fr(d, 2)} mm.",
            "**Étape 5 — ce que ce résultat n'est pas.** C'est un **minimum théorique**, "
            "jamais une cote de plan : il faut encore tenir compte des concentrations de "
            "contrainte, de la fatigue, et prendre le diamètre normalisé au-dessus.",
        ],
        "indice": "Trois temps : Rpe = Re/s, puis S = N/Rpe, puis d = √(4S/π).",
    }


def gen_flexion_mf():
    """Moment fléchissant maximal, poutre sur deux appuis, charge centrée."""
    F = random.choice([500, 800, 1200, 2000, 3000])
    L = random.choice([200, 300, 400, 500, 600, 800])
    Mf = F * L / 4
    return {
        "titre": "Flexion — moment fléchissant maximal",
        "enonce": (f"Une poutre sur **deux appuis** de portée **{L} mm** reçoit une charge "
                   f"**concentrée en son milieu** de **{fr(F, 0)} N**. Quel est le moment "
                   "fléchissant maximal, en N·mm ?"),
        "rep": Mf, "tol": max(1.0, Mf * 0.01), "unite": "N·mm",
        "diag": [
            _diag(F * L, "Tu as calculé F × L. C'est le cas d'une poutre encastrée avec une "
                         "charge à son extrémité, pas d'une poutre sur deux appuis."),
            _diag(F * L / 8, "F·L/8 correspond à une charge **répartie** sur toute la portée. "
                             "Ici la charge est concentrée au milieu."),
            _diag(F * L / 2, "F·L/2 ne correspond à aucun des cas usuels. Pour deux appuis et "
                             "une charge centrée, le moment maximal vaut F·L/4."),
        ],
        "corr": [
            f"**Ce que dit l'énoncé.** Deux appuis, portée {L} mm, charge de {fr(F, 0)} N "
            "concentrée au milieu. Il faut d'abord **identifier le cas de charge** : c'est "
            "lui qui choisit la formule.",
            "**Les réactions aux appuis.** Par symétrie, chaque appui reprend la moitié de "
            f"la charge : {fr(F / 2, 0)} N.",
            "**Où le moment est-il maximal ?** Au milieu, sous la charge — c'est le point le "
            "plus éloigné des deux appuis.",
            f"**La formule du cas.** Mf max = F·L/4 = {fr(F, 0)} × {L} / 4.",
            f"**Je calcule.** Mf max = {fr(Mf, 0)} N·mm.",
            "**Attention à l'unité.** En travaillant en N et en mm, le moment sort en N·mm. "
            f"Cela fait {fr(Mf / 1000, 2)} N·m — un facteur 1000 à ne pas confondre.",
        ],
        "indice": "Deux appuis et charge centrée : Mf max = F·L/4.",
    }


def gen_couple_puissance():
    """Couple transmis par un arbre à partir de la puissance et de la fréquence."""
    P_kw = random.choice([1.5, 2.2, 3, 4, 5.5, 7.5, 11])
    N = random.choice([750, 900, 1000, 1450, 1500, 2800, 3000])
    C = P_kw * 1000 * 60 / (2 * math.pi * N)
    return {
        "titre": "Transmission — couple sur un arbre",
        "enonce": (f"Un moteur de **{fr(P_kw, 1)} kW** tourne à **{N} tr/min**. Quel couple "
                   "transmet-il, en N·m ?"),
        "rep": round(C, 2), "tol": max(0.05, C * 0.02), "unite": "N·m",
        "diag": [
            _diag(round(P_kw * 1000 / N, 3),
                  "Tu as divisé la puissance par la fréquence de rotation en tr/min, sans la "
                  "convertir en rad/s. Il manque le facteur 2π/60."),
            _diag(round(P_kw * 60 / (2 * math.pi * N), 4),
                  "Tu as gardé la puissance en kilowatts. La formule demande des watts : "
                  "1 kW = 1000 W."),
            _diag(round(C * 1000, 1),
                  "Ton résultat est en N·mm. La question demande des N·m."),
        ],
        "corr": [
            f"**Ce que dit l'énoncé.** Une puissance de {fr(P_kw, 1)} kW et une fréquence de "
            f"rotation de {N} tr/min. On cherche le couple.",
            "**La relation.** P = C × ω, où ω est la vitesse angulaire **en rad/s**. "
            "Tout le calcul tient dans cette conversion.",
            f"**Étape 1 — la puissance en watts.** P = {fr(P_kw, 1)} × 1000 = {fr(P_kw * 1000, 0)} W.",
            f"**Étape 2 — la vitesse angulaire.** ω = 2πN/60 = 2π × {N} / 60 = "
            f"{fr(2 * math.pi * N / 60, 2)} rad/s.",
            f"**Étape 3 — le couple.** C = P/ω = {fr(P_kw * 1000, 0)} / "
            f"{fr(2 * math.pi * N / 60, 2)} = {fr(C, 2)} N·m.",
            "**Ce que cela apprend.** À puissance égale, un arbre lent transmet un couple "
            "**plus grand** : c'est pourquoi un réducteur impose des arbres plus gros en sortie.",
        ],
        "indice": "P = C·ω, avec ω = 2πN/60. Attention aux kilowatts et aux tr/min.",
    }


def gen_masse_piece(mat):
    """Masse d'une pièce simple, à partir de la masse volumique du matériau."""
    m = random.choice([x for x in mat.MATERIAUX if x.get("rho")])
    a = random.choice([20, 30, 40, 50, 60])
    b = random.choice([20, 30, 40, 50])
    e = random.choice([5, 8, 10, 12, 15, 20])
    V_cm3 = a * b * e / 1000.0
    masse = V_cm3 * m["rho"] / 1000.0 * 1000.0    # rho en kg/dm3 -> g/cm3
    return {
        "titre": "Masse d'une pièce",
        "enonce": (f"Une plaque de **{m['nom']}** mesure {a} × {b} × {e} mm. Sa masse "
                   f"volumique vaut **{fr(m['rho'], 2)} kg/dm³**. Quelle est sa masse, en grammes ?"),
        "rep": round(masse, 1), "tol": max(0.5, masse * 0.02), "unite": "g",
        "diag": [
            _diag(round(a * b * e * m["rho"], 0),
                  "Tu as multiplié le volume en **mm³** par une masse volumique en kg/dm³. "
                  "Les unités ne se correspondent pas : convertis d'abord le volume en cm³."),
            _diag(round(masse / 1000.0, 4),
                  "Ton résultat est en kilogrammes. La question demande des grammes."),
            _diag(round(V_cm3, 2),
                  "C'est le volume en cm³, pas la masse. Il reste à multiplier par la masse "
                  "volumique."),
        ],
        "corr": [
            f"**Ce que dit l'énoncé.** Une plaque de {a} × {b} × {e} mm en {m['nom']}, de "
            f"masse volumique {fr(m['rho'], 2)} kg/dm³.",
            "**La relation.** masse = masse volumique × volume. Tout le travail est dans "
            "l'accord des unités.",
            f"**Étape 1 — le volume en mm³.** V = {a} × {b} × {e} = {fr(a * b * e, 0)} mm³.",
            f"**Étape 2 — la conversion.** 1 cm³ = 1000 mm³, donc V = {fr(V_cm3, 2)} cm³. "
            "Et 1 kg/dm³ vaut exactement 1 g/cm³ : la masse volumique se lit directement en g/cm³.",
            f"**Étape 3 — la masse.** m = {fr(V_cm3, 2)} × {fr(m['rho'], 2)} = {fr(masse, 1)} g.",
            "**Je vérifie l'ordre de grandeur.** Une plaque de cette taille pèse quelques "
            "dizaines à quelques centaines de grammes : c'est cohérent.",
        ],
        "indice": "Volume en cm³, masse volumique en g/cm³ (même nombre qu'en kg/dm³), puis multiplication.",
    }


def gen_unites():
    """Les conversions qui font perdre le plus de points."""
    cas = random.choice([
        ("Combien vaut **1 MPa** en N/mm² ?", 1, "N/mm²",
         [(1e6, "1 MPa = 10⁶ Pa = 10⁶ N/m². Mais en N/mm², cela fait exactement 1."),
          (0.001, "Tu as divisé par 1000. Le mégapascal et le N/mm² sont la même chose.")],
         "**1 MPa = 1 N/mm².** C'est LA conversion du BTS : en travaillant en newtons et "
         "en millimètres, toute contrainte sort directement en MPa."),
        ("Un couple vaut **35 N·m**. Combien fait-il en N·mm ?", 35000, "N·mm",
         [(35, "Tu as recopié la valeur. Un mètre vaut 1000 mm, donc le nombre est multiplié "
               "par 1000."),
          (0.035, "Tu as divisé par 1000 au lieu de multiplier. En passant à une unité plus "
                  "petite, le nombre devient plus grand.")],
         "1 m = 1000 mm, donc 35 N·m = 35 × 1000 = 35 000 N·mm."),
        ("Une force vaut **250 daN**. Combien fait-elle en newtons ?", 2500, "N",
         [(25, "Tu as divisé par 10. Le déca- multiplie par 10 : 1 daN = 10 N."),
          (250000, "Tu as multiplié par 1000. Le préfixe déca- vaut 10, pas 1000.")],
         "Le préfixe déca- vaut 10 : 250 daN = 250 × 10 = 2500 N. C'est l'unité affichée "
         "sur beaucoup de vérins et de dynamomètres."),
        ("Une cote est tolérancée à **0,02 mm**. Combien cela fait-il en micromètres ?", 20, "µm",
         [(0.02, "Tu as recopié la valeur en millimètres."),
          (2, "Tu as multiplié par 100. Un millimètre vaut 1000 µm.")],
         "1 mm = 1000 µm, donc 0,02 mm = 0,02 × 1000 = 20 µm. Les tolérances ISO se lisent "
         "toujours en micromètres."),
    ])
    enonce, rep, unite, diags, expl = cas
    return {
        "titre": "Unités et conversions",
        "enonce": enonce,
        "rep": rep, "tol": max(1e-6, abs(rep) * 0.001), "unite": unite,
        "diag": [_diag(v, m) for v, m in diags],
        "corr": [
            "**Ce que demande la question.** Une conversion d'unité, rien de plus — mais "
            "c'est là que se perdent le plus de points en devoir.",
            "**Le réflexe.** Écrire d'abord l'équivalence entre les deux unités, avant tout "
            "calcul.",
            expl,
            "**Le contrôle de sens.** En passant à une unité **plus petite**, le nombre "
            "devient plus **grand**, et inversement.",
            f"**La réponse.** {fr(rep, 3)} {unite}.",
            "**Ce qu'il faut retenir.** En bureau d'études, on travaille en N et en mm : "
            "les contraintes sortent alors en MPa sans aucune conversion.",
        ],
        "indice": "Écris l'équivalence entre les deux unités avant de calculer.",
    }


def fabriquer(iso286, mat, famille=None):
    """Tire un exercice au hasard, éventuellement dans une famille donnée."""
    catalogue = {
        "Ajustements ISO": [lambda: gen_iso_jeu(iso286), lambda: gen_iso_it(iso286)],
        "Résistance des matériaux": [gen_traction_sigma, gen_traction_diametre, gen_flexion_mf],
        "Transmission de puissance": [gen_couple_puissance],
        "Matériaux et masses": [lambda: gen_masse_piece(mat)],
        "Unités et conversions": [gen_unites],
    }
    if famille and famille in catalogue:
        pool = catalogue[famille]
    else:
        pool = [g for gens in catalogue.values() for g in gens]
    ex = random.choice(pool)()

    # Selon les nombres tirés, un distracteur peut tomber sur la bonne réponse :
    # on l'écarte, pour ne jamais déclarer fausse une réponse juste.
    tol = ex.get("tol", 0.001)
    vus = []
    propres = []
    for d in ex.get("diag", []):
        v = d["v"]
        if v is None or abs(v - ex["rep"]) <= tol:
            continue
        if any(abs(v - u) <= tol for u in vus):
            continue
        vus.append(v)
        propres.append(d)
    ex["diag"] = propres
    return ex


FAMILLES = ["Mélange", "Ajustements ISO", "Résistance des matériaux",
            "Transmission de puissance", "Matériaux et masses", "Unités et conversions"]


def page_entrainement(P, sauver, iso286, mat):
    st.title("Entraînement illimité")
    st.caption("Les nombres changent à chaque tirage, mais les explications d'erreur "
               "sont recalculées avec eux : tu auras toujours un diagnostic juste, "
               "jamais un message passe-partout.")

    E = st.session_state.setdefault("ent", {"exo": None, "famille": "Mélange",
                                            "serie": 0, "faits": 0, "reussis": 0,
                                            "essais": 0, "fini": False})

    famille = st.selectbox("Thème", FAMILLES, index=FAMILLES.index(E["famille"]))
    if famille != E["famille"]:
        E.update({"famille": famille, "exo": None, "essais": 0, "fini": False})

    if E["exo"] is None:
        E["exo"] = fabriquer(iso286, mat, None if famille == "Mélange" else famille)
        E["essais"] = 0
        E["fini"] = False

    ex = E["exo"]
    c1, c2, c3 = st.columns(3)
    c1.metric("Série en cours", E["serie"])
    c2.metric("Exercices faits", E["faits"])
    c3.metric("Réussite", f"{round(100 * E['reussis'] / E['faits']) if E['faits'] else 0} %")

    st.divider()
    st.caption(ex["titre"])
    st.markdown(f"#### {ex['enonce']}")

    col_r, col_u = st.columns([3, 1])
    saisie = col_r.text_input("Ta réponse", key=f"rep_{id(ex)}",
                              placeholder="En chiffres…", label_visibility="collapsed")
    col_u.markdown(f"**{ex.get('unite', '')}**")

    b1, b2, b3 = st.columns([1, 1, 2])
    verifier = b1.button("Vérifier", type="primary", disabled=E["fini"])
    indice = b2.button("Un indice")
    if b3.button("Passer à un autre"):
        E.update({"exo": None, "serie": 0, "essais": 0, "fini": False})
        st.rerun()

    if indice:
        st.info("**Indice.** " + ex["indice"])

    if verifier:
        v = lire_nombre(saisie)
        if v is None:
            st.warning("Je n'ai pas réussi à lire ce nombre. Écris-le en chiffres, "
                       "par exemple 3,5.")
        else:
            E["essais"] += 1
            if abs(v - ex["rep"]) <= ex.get("tol", 0.001):
                st.success("Bonne réponse." if E["essais"] > 1
                           else "Exact, du premier coup.")
                E["faits"] += 1
                E["reussis"] += 1
                E["serie"] += 1
                E["fini"] = True
            else:
                message = None
                for d in ex.get("diag", []):
                    if abs(v - d["v"]) <= max(ex.get("tol", 0.001), abs(d["v"]) * 0.005):
                        message = d["m"]
                        break
                if message is None:
                    r = ex["rep"]
                    if r and abs(v + r) < ex.get("tol", 0.001):
                        message = ("Le bon nombre, mais le mauvais signe. Reprends en "
                                   "surveillant chaque « moins ».")
                    elif r and abs(v - 2 * r) < ex.get("tol", 0.001) * 2:
                        message = ("Ton résultat est le double de la bonne réponse : il "
                                   "manque probablement une division par 2.")
                    elif r and abs(v - r) < abs(r) * 0.05:
                        message = ("Tu es tout près : l'écart vient d'un arrondi. Refais "
                                   "la dernière étape sans arrondir en cours de route.")
                    else:
                        message = ("Ce n'est pas la bonne valeur. Ouvre la correction "
                                   "ci-dessous et compare ligne à ligne avec ton calcul.")
                st.error(message)
                if E["essais"] >= 2:
                    E["faits"] += 1
                    E["serie"] = 0
                    E["fini"] = True

    if E["fini"]:
        st.markdown(f"**Réponse : {fr(ex['rep'], 2)} {ex.get('unite', '')}**")
        with st.expander("La méthode, étape par étape", expanded=True):
            for i, etape in enumerate(ex["corr"], 1):
                st.markdown(f"**{i}.** {etape}")
        if st.button("Exercice suivant →", type="primary"):
            E.update({"exo": None, "essais": 0, "fini": False})
            st.rerun()
