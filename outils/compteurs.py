# -*- coding: utf-8 -*-
"""
Compteurs du README et de l'en-tête d'app.py : calculés, jamais écrits à la main.

Le README annonçait « 143 schémas, tous animés » quand app.py en contenait 187 (dont une partie
seulement animée), et « 150 fiches · 363 questions » bien après que le contenu eut grandi. Un
nombre recopié à la main finit toujours par se décaler. Ce module recalcule chaque compteur à
partir des données d'app.py, exactement comme l'application le fait (NB_FICHES, stats()) :

    python outils/compteurs.py            contrôle : code 1 si un compteur est périmé
    python outils/compteurs.py --ecrire   réécrit les compteurs périmés

L'audit (verifier_tolerances_ateliers.py, contrôle COMPTEUR) appelle verifier_compteurs() : un
compteur périmé y compte comme un défaut, donc bloque le commit comme les autres.

Pour compter, on exécute la partie « données » d'app.py (tout ce qui précède la section
NAVIGATION), sans la page Streamlit : environ une minute, le temps de compiler le fichier.
"""
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.join(RACINE, "app.py")
README = os.path.join(RACINE, "README.md")
FIN_DONNEES = "\n# NAVIGATION\n"


def calculer():
    """Les compteurs réels, calculés comme dans l'application."""
    src = open(APP, encoding="utf-8").read()
    g = {"__name__": "compteurs", "__file__": APP}
    if RACINE not in sys.path:
        sys.path.insert(0, RACINE)  # app.py importe le paquet part66, à côté de lui
    import logging
    logging.getLogger("streamlit").setLevel(logging.ERROR)
    exec(compile(src[:src.index(FIN_DONNEES)], APP, "exec"), g)
    figures = g["FIGURES"]
    return {
        "fiches": sum(len(b.get("fiches", [])) for b in g["BLOCS"]),
        "blocs": len(g["BLOCS"]),
        "questions": g["stats"]()["total"],
        "categories": len(g["QUIZ"]),
        "schemas": len(figures),
        "animes": sum(1 for _, f in figures.values() if "<animate" in f()),
        "materiaux": len(g["MATERIAUX"]),
    }


def _schemas(c, avec_smil=False):
    if c["animes"] == c["schemas"]:
        return "tous animés en SMIL" if avec_smil else "tous animés"
    return f"dont {c['animes']} animés en SMIL" if avec_smil else f"dont {c['animes']} animés"


# (fichier, motif, gabarit) : chaque motif doit apparaître exactement une fois.
def remplacements(c):
    return [
        (README, r"\*\*\d+ fiches de cours\*\* réparties en \d+ blocs",
         f"**{c['fiches']} fiches de cours** réparties en {c['blocs']} blocs"),
        (README, r"\*\*\d+ questions de quiz\*\*", f"**{c['questions']} questions de quiz**"),
        (README, r"\*\*\d+ schémas dessinés par le code, (?:tous animés|dont \d+ animés)\*\*",
         f"**{c['schemas']} schémas dessinés par le code, {_schemas(c)}**"),
        (README, r"\*\*\d+ nuances de(\s+)matériaux\*\*", rf"**{c['materiaux']} nuances de\g<1>matériaux**"),
        (README, r"les \d+ fiches, par matière", f"les {c['fiches']} fiches, par matière"),
        (README, r"\| \d+ questions, correction immédiate", f"| {c['questions']} questions, correction immédiate"),
        (APP, r"l'application, les \d+ fiches de cours, les(\s+)\d+ schémas \((?:tous animés en SMIL|dont \d+ animés en SMIL)\), "
              r"les \d+ questions de quiz",
         rf"l'application, les {c['fiches']} fiches de cours, les\g<1>{c['schemas']} schémas ({_schemas(c, True)}), "
         rf"les {c['questions']} questions de quiz"),
        (APP, r"FIGURES       — les \d+ schémas (?:animés )?dessinés par le code(?: \(dont \d+ animés\))?",
         f"FIGURES       — les {c['schemas']} schémas dessinés par le code"
         + ("" if c["animes"] == c["schemas"] else f" (dont {c['animes']} animés)")),
        (APP, r"QUIZ           — les \d+ questions, réparties en \d+ catégories",
         f"QUIZ           — les {c['questions']} questions, réparties en {c['categories']} catégories"),
    ]


def verifier_compteurs(ecrire=False):
    """Compare chaque compteur écrit à sa valeur calculée. Renvoie le nombre de défauts."""
    c = calculer()
    textes = {f: open(f, encoding="utf-8").read() for f in (README, APP)}
    defauts = []
    for fichier, motif, gabarit in remplacements(c):
        trouves = list(re.finditer(motif, textes[fichier]))
        nom = os.path.basename(fichier)
        if len(trouves) != 1:
            defauts.append(f"COMPTEUR    {nom} : la phrase « {motif[:50]}… » apparaît {len(trouves)} fois "
                           "(attendu : 1). Si elle a été reformulée, mettre à jour outils/compteurs.py.")
            continue
        voulu = trouves[0].expand(gabarit)
        if trouves[0].group(0) != voulu:
            if ecrire:
                textes[fichier] = textes[fichier].replace(trouves[0].group(0), voulu)
            else:
                defauts.append(f"COMPTEUR    {nom} : « {trouves[0].group(0)} » ; calculé : « {voulu} »")
    if ecrire:
        for f, t in textes.items():
            open(f, "w", encoding="utf-8", newline="\n").write(t)
    print(f"COMPTEURS : {c['fiches']} fiches, {c['blocs']} blocs, {c['questions']} questions en "
          f"{c['categories']} catégories, {c['schemas']} schémas dont {c['animes']} animés, "
          f"{c['materiaux']} matériaux.")
    print(f"{len(defauts)} compteur(s) périmé(s)"
          + (" — corriger avec : python outils/compteurs.py --ecrire" if defauts else "") + ".")
    for d in defauts:
        print("  " + d)
    return len(defauts)


if __name__ == "__main__":
    sys.exit(1 if verifier_compteurs(ecrire="--ecrire" in sys.argv) else 0)
