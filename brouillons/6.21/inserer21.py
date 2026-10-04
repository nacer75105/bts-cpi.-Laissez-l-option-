# Insère le brouillon 6.21 dans app.py (ancres textuelles uniques). Aucune retouche du contenu existant.
import json, os, re, textwrap

ICI = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(ICI, '..', '..', 'app.py')
app = open(APP, encoding='utf-8').read()
br = open(os.path.join(ICI, 'brouillon_6_21.py'), encoding='utf-8').read()


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
      "# 72i. MASSE, CENTRE DE GRAVITÉ, INERTIE, PFD ET ÉQUILIBRAGE (fiche 6.21)\n"
      "#      ρ acier : table MATERIAUX ; inerties : formules classiques des solides homogènes + Huygens ;\n"
      "#      dimensions, balourds, vitesses, charges : données d'énoncé. ISO 21940-11 vérifiée (extrait ISO).\n"
      "# ===========================================================================\n\n"
      + seg("def cdg_barycentre():", "# --- figure à curseurs").rstrip() + "\n\n\n")

# 2. registre FIGURES
entrees = re.findall(r'^    "(\w+)": \("([^"]+)", (\w+)\),$', seg("FIGURES_NOUVELLES = {", "}\nDYN_NOUVELLE"), re.M)
assert len(entrees) == 5, entrees
apres('    "pompe_moteur_hydraulique": ("Pompe et moteur hydrauliques : la cylindrée", pompe_moteur_hydraulique),\n',
      "".join(f'    "{k}": ("{t}", {f}),\n' for k, t, f in entrees))

# 3. figure à curseurs + registre DYNAMIQUES
avant("# Figures à curseurs, insérées dans un texte de fiche par le repère [[DYN:cle]].",
      seg("_CONFIGS = [", "FIGURES_NOUVELLES = {").rstrip() + "\n\n\n")
fin_dyn = ('         {"nom": "C0", "label": "Couple de la charge à 1 450 tr/min (N·m)", "min": 5.0, "max": 40.0, '
           '"defaut": 18.0, "pas": 1.0}]),\n}')
remplacer(fin_dyn, fin_dyn[:-1] + seg('    "balourd_curseurs": (', "}\n\n# ====").rstrip() + "\n}")

# 4. la fiche, en fin de bloc 6 (après la 6.20)
lignes, dans = [], False
for ligne in seg("FICHE_6_21 = {", "\n# ====").rstrip().split("\n"):
    lignes.append(("        " + ligne if ligne.strip() else ligne) if not dans else ligne)
    if ligne.count('"""') % 2 == 1:
        dans = not dans
assert not dans
lignes[0] = "        {"
i6 = app.index('            "id": "6.20",')
fin6 = app.index('        },\n    ],\n}\n', i6)
app = app[:fin6 + len('        },\n')] + "\n".join(lignes) + ",\n" + app[fin6 + len('        },\n'):]

# 5. méthode
mth = seg("MTH_6_21 = (", "\n# ====").rstrip()
avant('_mth("6.20", "Trouver le point de fonctionnement d\'un moteur asynchrone", [', "_mth(" + mth[len("MTH_6_21 = ("):] + "\n\n")

# 6. ateliers : at170 et at171 après at169 (dernier élément)
i169 = app.index('        "id": "at169",')
fin_at = app.index("\n    },\n]\n", i169)
at = seg("ATELIERS_NOUVEAUX = [\n", "\n]\n")[len("ATELIERS_NOUVEAUX = [\n"):].rstrip().rstrip(",")
app = app[:fin_at] + "\n    },\n" + at + "," + app[fin_at + len("\n    },"):]


# 7. quiz
def chaine(txt, retrait, largeur=96):
    morceaux = textwrap.wrap(txt, largeur - retrait, break_long_words=False, drop_whitespace=False)
    return ("\n" + " " * retrait).join(json.dumps(m, ensure_ascii=False) for m in morceaux)


g = {}
exec(seg("QUIZ_DYNAMIQUE = [", "\n]\n") + "\n]\n", g)
qs = []
for question, options, bonne, expl, niveau in g["QUIZ_DYNAMIQUE"]:
    ops = ",\n       ".join(chaine(o, 7) for o in options)
    qs.append(f"    q({chaine(question, 6)},\n      [{ops}], {bonne},\n      {chaine(expl, 6)},\n"
              f"      {json.dumps(niveau, ensure_ascii=False)}),\n")
avant('QUIZ["Roulements et visserie : dimensionner"] = [',
      'QUIZ["Masse, inertie, PFD et équilibrage"] = [\n' + "\n".join(qs) + "]\n\n")

# 8. générateurs, nouvelle famille « Dynamique » : catalogue ET menu « Thème »
gen = br.split("GENERATEUR = '''")[1].split("'''")[0].strip("\n")
avant("def gen_masse_piece():", gen + "\n\n\n")
apres('        "Motorisation": [gen_point_fonctionnement, gen_pompe_hydraulique],\n',
      '        "Dynamique": [gen_force_balourd, gen_cdg_arbre],\n')
remplacer('"Roulements", "Motorisation",\n', '"Roulements", "Motorisation", "Dynamique",\n')

# 9. carte du programme : ligne « Dynamique et Énergétique »
remplacer('''         "IE, pompes et moteurs hydrauliques).",
         [(8, ["8.1", "8.5"]), (13, ["13.3", "13.5"]), ("bloc6", ["6.18", "6.20"])]),''',
          '''         "IE, pompes et moteurs hydrauliques), masse, centre de gravité, inertie (Huygens), PFD et "
         "équilibrage statique et dynamique.",
         [(8, ["8.1", "8.5"]), (13, ["13.3", "13.5"]), ("bloc6", ["6.18", "6.20", "6.21"])]),''')

compile(app, APP, "exec")
open(APP, 'w', encoding='utf-8', newline='\n').write(app)
print("inséré")
