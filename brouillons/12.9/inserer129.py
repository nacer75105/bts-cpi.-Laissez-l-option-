# Insère le brouillon 12.9 dans app.py (ancres textuelles uniques). Aucune retouche du contenu existant.
import json, os, re, textwrap

ICI = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(ICI, '..', '..', 'app.py')
app = open(APP, encoding='utf-8').read()
br = open(os.path.join(ICI, 'brouillon_12_9.py'), encoding='utf-8').read()


def seg(debut, fin):
    i = br.index(debut); j = br.index(fin, i)
    return br[i:j]


def avant(ancre, texte):
    global app
    assert app.count(ancre) == 1, ancre[:60]
    app = app.replace(ancre, texte + ancre)


def apres(ancre, texte):
    global app
    assert app.count(ancre) == 1, ancre[:60]
    app = app.replace(ancre, ancre + texte)


def remplacer(ancien, nouveau, n=1):
    global app
    assert app.count(ancien) == n, (ancien[:70], app.count(ancien))
    app = app.replace(ancien, nouveau)


# 1. figures statiques
avant("# ===========================================================================\n# 73. CARACTÉRISER UNE FONCTION",
      "# ===========================================================================\n"
      "# 72n. SIMULATION NUMÉRIQUE ET CHAÎNE NUMÉRIQUE — maillage, conditions aux limites, Von Mises, singularité,\n"
      "#      PDM (fiche 12.9). Résultats de simulation : données d'énoncé ; singularité : Williams (1952).\n"
      "# ===========================================================================\n\n"
      + seg("_FE_COUL = (", "FIGURES_NOUVELLES = {").rstrip() + "\n\n\n")

# 2. registre FIGURES
entrees = re.findall(r'^    "(\w+)": \("([^"]+)", (\w+)\),$', seg("FIGURES_NOUVELLES = {", "}\n"), re.M)
assert len(entrees) == 5, entrees
apres('    "sysml_comportement": ("Cas d\'utilisation, séquence et états (uc, sd, stm)", sysml_comportement),\n',
      "".join(f'    "{k}": ("{t}", {f}),\n' for k, t, f in entrees))

# 3. la fiche, en fin de bloc 12 (après la 12.8)
lignes, dans = [], False
for ligne in seg("FICHE_12_9 = {", "\n# ====").rstrip().split("\n"):
    lignes.append(("        " + ligne if ligne.strip() else ligne) if not dans else ligne)
    if ligne.count('"""') % 2 == 1:
        dans = not dans
assert not dans
lignes[0] = "        {"
i12 = app.index('    "id": "12.8",')
fin12 = app.index('        },\n    ],\n}\n', i12)
assert fin12 < app.index('BLOC_13 = {', i12)
app = app[:fin12 + len('        },\n')] + "\n".join(lignes) + ",\n" + app[fin12 + len('        },\n'):]

# 4. méthode
mth = seg("MTH_12_9 = (", "\n# ====").rstrip()
avant('_mth("3.5", "Vérifier une pièce en fatigue", [', "_mth(" + mth[len("MTH_12_9 = ("):] + "\n\n")

# 5. ateliers : at180 et at181 après at179 (dernier élément)
i179 = app.index('        "id": "at179",')
fin_at = app.index("\n    },\n]\n", i179)
at = seg("ATELIERS_NOUVEAUX = [\n", "\n]\n")[len("ATELIERS_NOUVEAUX = [\n"):].rstrip().rstrip(",")
app = app[:fin_at] + "\n    },\n" + at + "," + app[fin_at + len("\n    },"):]


# 6. quiz
def chaine(txt, retrait, largeur=96):
    morceaux = textwrap.wrap(txt, largeur - retrait, break_long_words=False, drop_whitespace=False)
    return ("\n" + " " * retrait).join(json.dumps(m, ensure_ascii=False) for m in morceaux)


g = {}
exec(seg("QUIZ_SIMULATION = [", "\n]\n") + "\n]\n", g)
qs = []
for question, options, bonne, expl, niveau in g["QUIZ_SIMULATION"]:
    ops = ",\n       ".join(chaine(o, 7) for o in options)
    qs.append(f"    q({chaine(question, 6)},\n      [{ops}], {bonne},\n      {chaine(expl, 6)},\n"
              f"      {json.dumps(niveau, ensure_ascii=False)}),\n")
avant('QUIZ["Roulements et visserie : dimensionner"] = [',
      'QUIZ["Simulation et chaîne numérique"] = [\n' + "\n".join(qs) + "]\n\n")

# 7. générateurs, famille existante « Résistance des matériaux » (catalogue ; le menu Thème l'a déjà)
gen = br.split("GENERATEUR = '''")[1].split("'''")[0].strip("\n")
avant("def gen_masse_piece():", gen + "\n\n\n")
remplacer('        "Résistance des matériaux": [gen_traction_sigma, gen_traction_diametre, gen_flexion_mf],\n',
          '        "Résistance des matériaux": [gen_traction_sigma, gen_traction_diametre, gen_flexion_mf,\n'
          '                                     gen_securite_simulation, gen_ordre_grandeur_simulation],\n')

# 8. carte du programme : ligne « RDM & Dimensionnement »
remplacer('''         "chiffrées (page Exercices guidés).",
         [("bloc4", ["4.1", "4.2", "4.3"]), (12, ["12.2", "12.5"]), (15, ["15.1"]), ("bloc6", ["6.19"])]),''',
          '''         "chiffrées (page Exercices guidés) ; lecture critique d'une simulation par éléments finis "
         "(maillage, conditions aux limites, Von Mises, singularités) et chaîne numérique / PDM.",
         [("bloc4", ["4.1", "4.2", "4.3"]), (12, ["12.2", "12.5", "12.9"]), (15, ["15.1"]), ("bloc6", ["6.19"])]),''')

compile(app, APP, "exec")
open(APP, 'w', encoding='utf-8', newline='\n').write(app)
print("inséré")
