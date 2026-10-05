# Insère le brouillon 6.22 dans app.py (ancres textuelles uniques). Aucune retouche du contenu existant.
import json, os, re, textwrap

ICI = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(ICI, '..', '..', 'app.py')
app = open(APP, encoding='utf-8').read()
br = open(os.path.join(ICI, 'brouillon_6_22.py'), encoding='utf-8').read()


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
      "# 72j. STATIQUE DES FLUIDES — hydrostatique, Pascal, Archimède, paroi (fiche 6.22)\n"
      "#      Eau 1 000 kg/m³ (valeur arrondie d'usage) ; acier, aluminium : table MATERIAUX ;\n"
      "#      huile (850 kg/m³, comme en 8.9) et toutes les autres valeurs : données d'énoncé.\n"
      "# ===========================================================================\n\n"
      + seg("def hydrostatique_profondeur():", "def dyn_presse(").rstrip() + "\n\n\n")

# 2. registre FIGURES
entrees = re.findall(r'^    "(\w+)": \("([^"]+)", (\w+)\),$', seg("FIGURES_NOUVELLES = {", "}\nDYN_NOUVELLE"), re.M)
assert len(entrees) == 5, entrees
apres('    "equilibrage": ("Équilibrage statique et dynamique d\'un rotor", equilibrage),\n',
      "".join(f'    "{k}": ("{t}", {f}),\n' for k, t, f in entrees))

# 3. figure à curseurs + registre DYNAMIQUES
avant("# Figures à curseurs, insérées dans un texte de fiche par le repère [[DYN:cle]].",
      seg("def dyn_presse(", "FIGURES_NOUVELLES = {").rstrip() + "\n\n\n")
fin_dyn = ('         {"nom": "mb", "label": "Masse de chaque balourd (g)", "min": 2.0, "max": 20.0, "defaut": 10.0, '
           '"pas": 2.0}]),\n}')
remplacer(fin_dyn, fin_dyn[:-1] + seg('    "presse_curseurs": (', "}\n\n# ====").rstrip() + "\n}")

# 4. la fiche, en fin de bloc 6 (après la 6.21)
lignes, dans = [], False
for ligne in seg("FICHE_6_22 = {", "\n# ====").rstrip().split("\n"):
    lignes.append(("        " + ligne if ligne.strip() else ligne) if not dans else ligne)
    if ligne.count('"""') % 2 == 1:
        dans = not dans
assert not dans
lignes[0] = "        {"
i6 = app.index('            "id": "6.21",')
fin6 = app.index('        },\n    ],\n}\n', i6)
app = app[:fin6 + len('        },\n')] + "\n".join(lignes) + ",\n" + app[fin6 + len('        },\n'):]

# 5. méthode
mth = seg("MTH_6_22 = (", "\n# ====").rstrip()
avant('_mth("6.21", "Écrire le PFD d\'un système qui accélère", [', "_mth(" + mth[len("MTH_6_22 = ("):] + "\n\n")

# 6. ateliers : at172 et at173 après at171 (dernier élément)
i171 = app.index('        "id": "at171",')
fin_at = app.index("\n    },\n]\n", i171)
at = seg("ATELIERS_NOUVEAUX = [\n", "\n]\n")[len("ATELIERS_NOUVEAUX = [\n"):].rstrip().rstrip(",")
app = app[:fin_at] + "\n    },\n" + at + "," + app[fin_at + len("\n    },"):]


# 7. quiz
def chaine(txt, retrait, largeur=96):
    morceaux = textwrap.wrap(txt, largeur - retrait, break_long_words=False, drop_whitespace=False)
    return ("\n" + " " * retrait).join(json.dumps(m, ensure_ascii=False) for m in morceaux)


g = {}
exec(seg("QUIZ_FLUIDES = [", "\n]\n") + "\n]\n", g)
qs = []
for question, options, bonne, expl, niveau in g["QUIZ_FLUIDES"]:
    ops = ",\n       ".join(chaine(o, 7) for o in options)
    qs.append(f"    q({chaine(question, 6)},\n      [{ops}], {bonne},\n      {chaine(expl, 6)},\n"
              f"      {json.dumps(niveau, ensure_ascii=False)}),\n")
avant('QUIZ["Roulements et visserie : dimensionner"] = [',
      'QUIZ["Statique des fluides"] = [\n' + "\n".join(qs) + "]\n\n")

# 8. générateurs, nouvelle famille « Statique des fluides » : catalogue ET menu « Thème »
gen = br.split("GENERATEUR = '''")[1].split("'''")[0].strip("\n")
avant("def gen_masse_piece():", gen + "\n\n\n")
apres('        "Dynamique": [gen_force_balourd, gen_cdg_arbre],\n',
      '        "Statique des fluides": [gen_presse_hydraulique, gen_poussee_archimede],\n')
remplacer('"Roulements", "Motorisation", "Dynamique",\n',
          '"Roulements", "Motorisation", "Dynamique",\n                          "Statique des fluides",\n')

# 9. carte du programme : ligne « Mécanique des fluides »
remplacer('''         "Pertes de charge, nombre de Reynolds, continuité et théorème de Bernoulli (effet Venturi).",
         [(8, ["8.2", "8.9"])]),''',
          '''         "Statique (hydrostatique, théorème de Pascal, presse et vérin, poussée d'Archimède, effort sur une "
         "paroi), pertes de charge, nombre de Reynolds, continuité et théorème de Bernoulli (effet Venturi).",
         [(8, ["8.2", "8.9"]), ("bloc6", ["6.22"])]),''')

compile(app, APP, "exec")
open(APP, 'w', encoding='utf-8', newline='\n').write(app)
print("inséré")
