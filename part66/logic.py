"""Logique métier de la section Part-66 : chargement du contenu, boîtes de
Leitner (5 boîtes, intervalles 1/2/4/8/16 jours), session du jour, examen
blanc et calcul de progression par sous-chapitre.

Indépendant du système de révision espacée du BTS (app.py) : ici, toute
question obtient une carte dès son import, pas seulement les questions
ratées, et une carte n'est jamais retirée du suivi.
"""
import json
import os
import random
from datetime import datetime, timedelta
from pathlib import Path

_ICI = os.path.dirname(__file__)
_RACINE = os.path.dirname(_ICI)
FICHIER_PROGRESSION = os.path.join(_RACINE, "progression_part66.json")

# Intervalles de réapparition en jours, indexés par boîte (boîte 1 -> index 0).
INTERVALLES_JOURS = [1, 2, 4, 8, 16]
NB_BOITES = len(INTERVALLES_JOURS)

SEUIL_REUSSITE_EXAMEN_PCT = 75
SEUIL_RESERVATION_EXAMEN_REEL_PCT = 85
NB_BLANCS_CONSECUTIFS_REQUIS = 3

# Modules du programme B1.1. M10 et M5 sont construits ; les titres des
# autres modules sont des libellés d'affichage à confirmer avant de les
# construire (voir part66/A_VERIFIER.md).
MODULES = {
    "M10": {"titre": "Législation aéronautique", "disponible": True,
             "nb_questions_examen": 32, "duree_examen_min": 40},
    "M5": {"titre": "Techniques numériques / systèmes d'instruments électroniques",
           "disponible": True,
           "nb_questions_examen": 20, "duree_examen_min": 25},
    "M7A": {"titre": "Pratiques de maintenance", "disponible": True,
             "nb_questions_examen": 25, "duree_examen_min": 30},
    "M11A": {"titre": "Aérodynamique, structures et systèmes — avion à turbine",
              "disponible": False,  # lots 1-3/5 (M11A.1-M11A.15) relus et corrigés ; reste lots 4-5 puis test local avant activation
              "nb_questions_examen": 140, "duree_examen_min": 175},  # TODO : 175 min = 75 s/question x 140, à confirmer sur l'Appendix VIII officiel
    "M15": {"titre": "Turbomachines à gaz", "disponible": True,  # module complet (14 fiches), relu et validé par l'utilisateur (lots 1-3, tests locaux inclus) le 2026-09-11
             "nb_questions_examen": 25, "duree_examen_min": 30},  # TODO : valeurs provisoires non vérifiées (alignées sur M17A), à confirmer avec l'utilisateur une fois le module M15 complet (14 fiches)
    "M17A": {"titre": "Hélices", "disponible": True,  # module complet (14 fiches), relu et validé par l'utilisateur (lots 1-3, tests locaux inclus) le 2026-09-11
             "nb_questions_examen": 25, "duree_examen_min": 30},
}


def _fichier_module(module, nom):
    return os.path.join(_ICI, "data", module, nom)


def charger_fiches(module):
    chemin = _fichier_module(module, "fiches.json")
    if not os.path.exists(chemin):
        return []
    with open(chemin, "r", encoding="utf-8") as f:
        return json.load(f)["fiches"]


def charger_schemas(module, fiche_id):
    """Liste des chemins (pathlib.Path) vers les schémas HTML interactifs
    d'une fiche, dans l'ordre d'affichage : <fiche_id>.html (principe) puis
    <fiche_id>-2.html (application/panne) s'il existe. Liste vide si aucun
    schéma — l'illustration interactive reste optionnelle."""
    chemins = []
    for suffixe in ("", "-2"):
        chemin = Path(_fichier_module(module, os.path.join("schemas", f"{fiche_id}{suffixe}.html")))
        if chemin.exists():
            chemins.append(chemin)
    return chemins


def charger_questions(module):
    chemin = _fichier_module(module, "questions.json")
    if not os.path.exists(chemin):
        return []
    with open(chemin, "r", encoding="utf-8") as f:
        return json.load(f)["questions"]


# ---------------------------------------------------------------------------
# Persistance (fichier séparé de progression.json, propre au BTS)
# ---------------------------------------------------------------------------

def charger_progression():
    if os.path.exists(FICHIER_PROGRESSION):
        try:
            with open(FICHIER_PROGRESSION, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return {"boites": {}, "sessions": [], "examens_blancs": []}


def sauver_progression(p):
    try:
        with open(FICHIER_PROGRESSION, "w", encoding="utf-8") as f:
            json.dump(p, f, ensure_ascii=False, indent=2)
    except OSError:
        pass


# ---------------------------------------------------------------------------
# Boîtes de Leitner
# ---------------------------------------------------------------------------

def _assurer_cartes(p, questions):
    """Chaque question obtient une carte en boîte 1, due immédiatement,
    dès son import — pas seulement les questions ratées."""
    boites = p.setdefault("boites", {})
    maintenant = datetime.now().isoformat()
    for q in questions:
        if q["uid"] not in boites:
            boites[q["uid"]] = {"boite": 1, "echeance": maintenant}


def repondre(p, uid, reussi):
    """Met à jour la boîte de Leitner d'une question après une réponse.
    Bonne réponse -> boîte suivante (max 5). Mauvaise réponse -> boîte 1,
    quel que soit le palier atteint."""
    boites = p.setdefault("boites", {})
    carte = boites.setdefault(uid, {"boite": 1, "echeance": datetime.now().isoformat()})
    if reussi:
        boite = min(carte.get("boite", 1) + 1, NB_BOITES)
    else:
        boite = 1
    carte["boite"] = boite
    carte["echeance"] = (datetime.now() + timedelta(days=INTERVALLES_JOURS[boite - 1])).isoformat()
    sauver_progression(p)


def _echeance(boites, uid, maintenant):
    try:
        return datetime.fromisoformat(boites[uid]["echeance"])
    except (KeyError, ValueError):
        return maintenant


def construire_session_du_jour(p, module, taille_cible=25):
    """Priorité aux cartes échues, complète avec des questions neuves si
    besoin, puis entrelace (mélange l'ordre plutôt que de grouper par
    sous-chapitre)."""
    questions = charger_questions(module)
    if not questions:
        return []
    _assurer_cartes(p, questions)
    sauver_progression(p)

    par_uid = {q["uid"]: q for q in questions}
    boites = p.get("boites", {})
    maintenant = datetime.now()

    dues = sorted(
        (uid for uid in par_uid if _echeance(boites, uid, maintenant) <= maintenant),
        key=lambda uid: _echeance(boites, uid, maintenant),
    )
    selection = dues[:taille_cible]
    if len(selection) < taille_cible:
        restantes = [uid for uid in par_uid if uid not in selection]
        random.shuffle(restantes)
        selection += restantes[: taille_cible - len(selection)]

    random.shuffle(selection)
    return [par_uid[uid] for uid in selection]


def construire_examen_blanc(module):
    """Tire le nombre officiel de questions dans tout le module, sans
    tenir compte du suivi Leitner (l'examen blanc simule l'épreuve réelle,
    pas une révision ciblée)."""
    infos = MODULES[module]
    questions = list(charger_questions(module))
    random.shuffle(questions)
    nb = min(infos.get("nb_questions_examen", 32), len(questions))
    return questions[:nb], infos.get("duree_examen_min", 40)


# ---------------------------------------------------------------------------
# Historique et progression
# ---------------------------------------------------------------------------

def enregistrer_session(p, module, nb_questions, bonnes, type_session="session_du_jour"):
    p.setdefault("sessions", []).insert(0, {
        "date": datetime.now().isoformat(timespec="minutes"),
        "module": module, "nb_questions": nb_questions, "bonnes": bonnes,
        "type": type_session,
    })
    sauver_progression(p)


def enregistrer_examen_blanc(p, module, nb_questions, bonnes, duree_min):
    note_pct = round(100 * bonnes / nb_questions, 1) if nb_questions else 0
    p.setdefault("examens_blancs", []).insert(0, {
        "date": datetime.now().isoformat(timespec="minutes"),
        "module": module, "nb_questions": nb_questions, "bonnes": bonnes,
        "note_pct": note_pct, "reussi": note_pct >= SEUIL_REUSSITE_EXAMEN_PCT,
        "duree_min": duree_min,
    })
    sauver_progression(p)
    return note_pct


def serie_jours_consecutifs(p):
    """Nombre de jours consécutifs, jusqu'à aujourd'hui inclus, avec au
    moins une session du jour effectuée."""
    jours = {s["date"][:10] for s in p.get("sessions", [])}
    serie = 0
    jour = datetime.now().date()
    while jour.isoformat() in jours:
        serie += 1
        jour -= timedelta(days=1)
    return serie


def progression_par_sous_chapitre(p, module):
    """Taux de maîtrise (0-100 %) par sous-chapitre, déduit de la boîte
    moyenne des questions de ce sous-chapitre."""
    questions = {q["uid"]: q for q in charger_questions(module)}
    boites = p.get("boites", {})
    stats = {}
    for uid, q in questions.items():
        sc = q["sous_chapitre"]
        s = stats.setdefault(sc, {"total": 0, "somme_boite": 0})
        s["total"] += 1
        s["somme_boite"] += boites.get(uid, {"boite": 1}).get("boite", 1)
    out = {}
    for sc, s in stats.items():
        moyenne_boite = s["somme_boite"] / s["total"] if s["total"] else 1
        out[sc] = round(100 * (moyenne_boite - 1) / (NB_BOITES - 1), 1)
    return out


def peut_reserver_examen_reel(p, module):
    """Règle d'affichage : n'encourager la réservation de l'examen réel
    qu'après 3 examens blancs consécutifs >= 85 %."""
    blancs = [e for e in p.get("examens_blancs", []) if e["module"] == module]
    trois_derniers = blancs[:NB_BLANCS_CONSECUTIFS_REQUIS]
    return (len(trois_derniers) == NB_BLANCS_CONSECUTIFS_REQUIS
            and all(e["note_pct"] >= SEUIL_RESERVATION_EXAMEN_REEL_PCT for e in trois_derniers))
