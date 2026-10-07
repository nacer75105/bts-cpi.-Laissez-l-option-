# Insère le brouillon 3.5 dans app.py (ancres textuelles uniques) et fait les deux retouches validées par
# l'auteur : 1. fiche 3.1 : résilience en J (énergie KV, essai Charpy), et non en J/cm² (ancienne KCV) ;
# 2. renvois fatigue de la 3.1 et de la 4.1 : ajout de la fiche 3.5, fiche de référence sur la fatigue.
import json, os, re, textwrap

ICI = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(ICI, '..', '..', 'app.py')
app = open(APP, encoding='utf-8').read()
br = open(os.path.join(ICI, 'brouillon_3_5.py'), encoding='utf-8').read()


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
      "# 72k. ESSAIS ET COMPLÉMENTS MATÉRIAUX — fatigue, Charpy, flexion, grenaillage (fiche 3.5)\n"
      "#      Re, Rm, ρ : table MATERIAUX ; ISO 148-1 vérifiée ; σD, Kt, prix : données d'énoncé.\n"
      "# ===========================================================================\n\n"
      + seg("def wohler():", "# --- figure à curseurs").rstrip() + "\n\n\n")

# 2. registre FIGURES
entrees = re.findall(r'^    "(\w+)": \("([^"]+)", (\w+)\),$', seg("FIGURES_NOUVELLES = {", "}\nDYN_NOUVELLE"), re.M)
assert len(entrees) == 5, entrees
apres('    "stabilite_flottant": ("Stabilité d\'un flotteur : poids et poussée", stabilite_flottant),\n',
      "".join(f'    "{k}": ("{t}", {f}),\n' for k, t, f in entrees))

# 3. figure à curseurs + registre DYNAMIQUES
avant("# Figures à curseurs, insérées dans un texte de fiche par le repère [[DYN:cle]].",
      seg("def dyn_fatigue(", "FIGURES_NOUVELLES = {").rstrip() + "\n\n\n")
fin_dyn = ('         {"nom": "F1", "label": "Effort sur le petit piston F1 (N)", "min": 50.0, "max": 500.0, "defaut": 200.0, '
           '"pas": 50.0}]),\n}')
remplacer(fin_dyn, fin_dyn[:-1] + seg('    "fatigue_curseurs": (', "}\n\n# ====").rstrip() + "\n}")

# 4. la fiche, en fin de bloc 3 (après la 3.4)
lignes, dans = [], False
for ligne in seg("FICHE_3_5 = {", "\n# ====").rstrip().split("\n"):
    lignes.append(("        " + ligne if ligne.strip() else ligne) if not dans else ligne)
    if ligne.count('"""') % 2 == 1:
        dans = not dans
assert not dans
lignes[0] = "        {"
i3 = app.index("            \"id\": '3.4',")
fin3 = app.index('        },\n    ],\n}\n', i3)
assert fin3 < app.index('    "id": "bloc4",')
app = app[:fin3 + len('        },\n')] + "\n".join(lignes) + ",\n" + app[fin3 + len('        },\n'):]

# 5. méthode
mth = seg("MTH_3_5 = (", "\n# ====").rstrip()
avant('_mth("6.22", "Calculer un effort hydraulique (presse, vérin, paroi)", [', "_mth(" + mth[len("MTH_3_5 = ("):] + "\n\n")

# 6. ateliers : at174 et at175 après at173 (dernier élément)
i173 = app.index('        "id": "at173",')
fin_at = app.index("\n    },\n]\n", i173)
at = seg("ATELIERS_NOUVEAUX = [\n", "\n]\n")[len("ATELIERS_NOUVEAUX = [\n"):].rstrip().rstrip(",")
app = app[:fin_at] + "\n    },\n" + at + "," + app[fin_at + len("\n    },"):]


# 7. quiz
def chaine(txt, retrait, largeur=96):
    morceaux = textwrap.wrap(txt, largeur - retrait, break_long_words=False, drop_whitespace=False)
    return ("\n" + " " * retrait).join(json.dumps(m, ensure_ascii=False) for m in morceaux)


g = {}
exec(seg("QUIZ_ESSAIS = [", "\n]\n") + "\n]\n", g)
qs = []
for question, options, bonne, expl, niveau in g["QUIZ_ESSAIS"]:
    ops = ",\n       ".join(chaine(o, 7) for o in options)
    qs.append(f"    q({chaine(question, 6)},\n      [{ops}], {bonne},\n      {chaine(expl, 6)},\n"
              f"      {json.dumps(niveau, ensure_ascii=False)}),\n")
avant('QUIZ["Roulements et visserie : dimensionner"] = [',
      'QUIZ["Essais mécaniques, fatigue et traitements"] = [\n' + "\n".join(qs) + "]\n\n")

# 8. générateurs, famille existante « Matériaux et masses »
gen = br.split("GENERATEUR = '''")[1].split("'''")[0].strip("\n")
avant("def gen_masse_piece():", gen + "\n\n\n")
remplacer('        "Matériaux et masses": [gen_masse_piece],',
          '        "Matériaux et masses": [gen_masse_piece, gen_charpy_energie, gen_flexion_3points],')

# 9. carte du programme : ligne « Choix des matériaux »
remplacer('''         "Familles, désignation normalisée, critères de choix comparés sur exemple chiffré.",
         [("bloc3", ["3.1", "3.2"]), ("bloc0h", ["0.11.1", "0.11.2"])]),''',
          '''         "Familles, désignation normalisée, critères de choix comparés sur exemple chiffré ; essais (fatigue et "
         "courbe de Wöhler, résilience Charpy, flexion, dureté), céramiques, traitements mécaniques, coûts.",
         [("bloc3", ["3.1", "3.2", "3.5"]), ("bloc0h", ["0.11.1", "0.11.2"])]),''')

# ---------------------------------------------------------------- retouches du contenu existant
# retouche 1 : résilience en J (KV), et non en J/cm² (ancienne KCV) — fiche 3.1 (cours affiché, formules, et
# version d'origine non affichée, alignée par cohérence)
remplacer('''| **résilience** | sa résistance aux **chocs** | J/cm² | pièces qui prennent des coups, froid |''',
          '''| **résilience** | sa résistance aux **chocs** | J (énergie KV, essai Charpy) | pièces qui prennent des coups, froid |''')
remplacer('''| **résilience** | la résistance aux **chocs** | J/cm² | pièces qui prennent des coups, froid |''',
          '''| **résilience** | la résistance aux **chocs** | J (énergie KV, essai Charpy) | pièces qui prennent des coups, froid |''')
remplacer('''· A % (allongement) · résilience (J/cm²)''',
          '''· A % (allongement) · résilience (J : énergie KV, essai Charpy, fiche 3.5)''')
assert "J/cm²" not in app.replace("c'était la KCV, en J/cm²", "")

# retouche 2 : renvois fatigue vers la 3.5
remplacer('''en fatigue** — la capacité à supporter des millions de cycles, à un niveau bien inférieur à Re
(fiches 12.5 et 13.5).''',
          '''en fatigue** — la capacité à supporter des millions de cycles, à un niveau bien inférieur à Re
(fiche 3.5, et les cas des fiches 12.5 et 13.5).''')
remplacer('''l'endroit où Kt est maximal. C'est ce que montrent les cas des fiches 12.5 et 13.5.*''',
          '''l'endroit où Kt est maximal. La méthode est en fiche 3.5 ; les cas des fiches 12.5 et 13.5 le montrent.*''')

compile(app, APP, "exec")
open(APP, 'w', encoding='utf-8', newline='\n').write(app)
print("inséré")
