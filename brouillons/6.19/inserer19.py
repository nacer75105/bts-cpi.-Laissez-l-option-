# Insère le brouillon 6.19 dans app.py, par ancres textuelles uniques, et fait les quatre retouches
# validées par l'auteur (6.5, 11.1, 14.2 → renvoi vers la 6.19 ; 10.1 → C et C0 SKF du 6205).
import json, os, re, textwrap

ICI = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(ICI, '..', '..', 'app.py')
app = open(APP, encoding='utf-8').read()
br = open(os.path.join(ICI, 'brouillon_6_19.py'), encoding='utf-8').read()


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


def remplacer(ancien, nouveau):
    global app
    assert app.count(ancien) == 1, ancien[:60]
    app = app.replace(ancien, nouveau)


# 1. figures statiques, après celles de la 6.18
avant("# ===========================================================================\n# 73. CARACTÉRISER UNE FONCTION",
      "# ===========================================================================\n"
      "# 72f. ROULEMENTS ET VISSERIE — durée de vie L10, solutions constructives, précharge (fiche 6.19)\n"
      "#      Valeurs de catalogue : SKF 6205 (C = 14,8 kN) et NU 205 ECP (C = 32,5 kN), fiches skf.com ;\n"
      "#      sections résistantes ISO 898-1.\n"
      "# ===========================================================================\n\n"
      + seg("def duree_vie_dispersion():", "# --- figure à curseurs").rstrip() + "\n\n\n")

# 2. registre FIGURES
entrees = re.findall(r'^    "(\w+)": \("([^"]+)", (\w+)\),$', seg("FIGURES_NOUVELLES = {", "}\nDYN_NOUVELLE"), re.M)
assert len(entrees) == 4, entrees
apres('    "courroies_chaines": ("Courroies et chaînes : adhérence ou obstacle", courroies_chaines),\n',
      "".join(f'    "{k}": ("{t}", {f}),\n' for k, t, f in entrees))

# 3. figure à curseurs (table des roulements, fonction, choix) + registre DYNAMIQUES
avant("# Figures à curseurs, insérées dans un texte de fiche par le repère [[DYN:cle]].",
      seg("_ROULEMENTS = {", "FIGURES_NOUVELLES = {").rstrip() + "\n\n\n")
fin_dyn = ('         {"nom": "f", "label": "Frottement f (donné)", "min": 0.05, "max": 0.30, "defaut": 0.15, '
           '"pas": 0.05}]),\n}')
remplacer(fin_dyn, fin_dyn[:-1] + seg('    "duree_roulement_curseurs": (', "}\n\n# ====").rstrip() + "\n}")

# 4. la fiche, en fin de bloc 6 (après la 6.18)
lignes, dans = [], False
for ligne in seg("FICHE_6_19 = {", "\n# ====").rstrip().split("\n"):
    lignes.append(("        " + ligne if ligne.strip() else ligne) if not dans else ligne)
    if ligne.count('"""') % 2 == 1:
        dans = not dans
assert not dans
lignes[0] = "        {"
i6 = app.index("            \"id\": '6.18',")
fin6 = app.index('        },\n    ],\n}\n', i6)
app = app[:fin6 + len('        },\n')] + "\n".join(lignes) + ",\n" + app[fin6 + len('        },\n'):]

# 5. méthode
mth = seg("MTH_6_19 = (", "\n# ====").rstrip()
avant('_mth("6.9", "Vérifier la tenue d\'un assemblage vissé", [', "_mth(" + mth[len("MTH_6_19 = ("):] + "\n\n")

# 6. ateliers : at163 est le dernier élément de ATELIERS
i163 = app.index('        "id": "at163",')
fin_at = app.index("\n    },\n]\n", i163)
at = seg("ATELIERS_NOUVEAUX = [\n", "\n]\n")[len("ATELIERS_NOUVEAUX = [\n"):].rstrip().rstrip(",")
app = app[:fin_at] + "\n    },\n" + at + "," + app[fin_at + len("\n    },"):]


# 7. quiz
def chaine(txt, retrait, largeur=96):
    morceaux = textwrap.wrap(txt, largeur - retrait, break_long_words=False, drop_whitespace=False)
    return ("\n" + " " * retrait).join(json.dumps(m, ensure_ascii=False) for m in morceaux)


g = {}
exec(seg("QUIZ_ROULEMENTS = [", "\n]\n") + "\n]\n", g)
qs = []
for question, options, bonne, expl, niveau in g["QUIZ_ROULEMENTS"]:
    ops = ",\n       ".join(chaine(o, 7) for o in options)
    qs.append(f"    q({chaine(question, 6)},\n      [{ops}], {bonne},\n      {chaine(expl, 6)},\n"
              f"      {json.dumps(niveau, ensure_ascii=False)}),\n")
avant('QUIZ["Statique et frottement"] = [', 'QUIZ["Roulements et visserie : dimensionner"] = [\n' + "\n".join(qs) + "]\n\n")

# 8. générateur, nouvelle famille « Roulements » : catalogue ET menu « Thème »
gen = br.split("GENERATEUR = '''")[1].split("'''")[0].strip("\n")
avant("def gen_masse_piece():", gen + "\n\n\n")
apres('        "Liaisons": [gen_hyperstatisme_paliers],\n', '        "Roulements": [gen_duree_roulement],\n')
remplacer('                          "Transmission de puissance", "Cinématique", "Statique", "Liaisons",\n',
          '                          "Transmission de puissance", "Cinématique", "Statique", "Liaisons", "Roulements",\n')

# 9. carte du programme : ligne « RDM & Dimensionnement »
remplacer('''         [("bloc4", ["4.1", "4.2", "4.3"]), (12, ["12.2", "12.5"]), (15, ["15.1"])]),''',
          '''         [("bloc4", ["4.1", "4.2", "4.3"]), (12, ["12.2", "12.5"]), (15, ["15.1"]), ("bloc6", ["6.19"])]),''')

# 10. les quatre retouches
remplacer('''catalogue — ce qui est au programme de deuxième année.''',
          '''catalogue — c'est le calcul de durée de vie L10 de la fiche 6.19.''')
remplacer('''**Un avant-goût de ce calcul, pour que ce ne soit pas qu'un mot.** La durée de vie d'un''',
          '''**Un avant-goût de ce calcul (traité en entier en fiche 6.19).** La durée de vie d'un''')
remplacer('''  c'est le calcul qui manque à ce sujet, et il relève de la deuxième année ;''',
          '''  c'est le calcul qui manque à ce sujet (méthode complète : fiche 6.19) ;''')
remplacer('''Extrait typique d'un catalogue anglophone :

> **Deep groove ball bearing 6205-2RS**
> Bore: 25 mm · Outside diameter: 52 mm · Width: 15 mm
> Dynamic load rating C: 14.0 kN · Static load rating C₀: 7.80 kN''',
          '''Extrait d'une fiche technique en anglais. C et C₀ sont les valeurs du catalogue SKF pour le 6205 (les
mêmes qu'en fiche 6.19 : une donnée de catalogue est la même partout) ; la vitesse limite est une valeur
d'exemple pour l'exercice de lecture — comme C, elle se lit au catalogue du fabricant, pour la référence
exacte.

> **Deep groove ball bearing 6205-2RS**
> Bore: 25 mm · Outside diameter: 52 mm · Width: 15 mm
> Dynamic load rating C: 14.8 kN · Static load rating C₀: 7.8 kN''')

compile(app, APP, "exec")
open(APP, 'w', encoding='utf-8', newline='\n').write(app)
print("inséré")
