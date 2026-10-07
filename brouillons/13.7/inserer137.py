# Insère le brouillon 13.7 dans app.py (ancres textuelles uniques). Aucune retouche du contenu existant.
import json, os, re, textwrap

ICI = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(ICI, '..', '..', 'app.py')
app = open(APP, encoding='utf-8').read()
br = open(os.path.join(ICI, 'brouillon_13_7.py'), encoding='utf-8').read()


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
      "# 72l. PROCÉDÉS, COMPLÉMENTS — plasturgie, poudres et MIM, assemblages, STL, seuil de rentabilité (fiche 13.7)\n"
      "#      Aucune valeur de procédé (température, pression, tolérance) ; coûts : données d'énoncé.\n"
      "# ===========================================================================\n\n"
      + seg("def plasturgie_procedes():", "# --- figure à curseurs").rstrip() + "\n\n\n")

# 2. registre FIGURES
entrees = re.findall(r'^    "(\w+)": \("([^"]+)", (\w+)\),$', seg("FIGURES_NOUVELLES = {", "}\nDYN_NOUVELLE"), re.M)
assert len(entrees) == 6, entrees
apres('    "grenaillage": ("Grenaillage : contraintes résiduelles de compression", grenaillage),\n',
      "".join(f'    "{k}": ("{t}", {f}),\n' for k, t, f in entrees))

# 3. figure à curseurs + registre DYNAMIQUES
avant("# Figures à curseurs, insérées dans un texte de fiche par le repère [[DYN:cle]].",
      seg("def dyn_facettes(", "FIGURES_NOUVELLES = {").rstrip() + "\n\n\n")
fin_dyn = ('         {"nom": "Kt", "label": "Coefficient de concentration Kt", "min": 1.0, "max": 3.0, "defaut": 2.5, '
           '"pas": 0.1}]),\n}')
remplacer(fin_dyn, fin_dyn[:-1] + seg('    "facettes_curseurs": (', "}\n\n# ====").rstrip() + "\n}")

# 4. la fiche, en fin de bloc 13 (après la 13.6)
lignes, dans = [], False
for ligne in seg("FICHE_13_7 = {", "\n# ====").rstrip().split("\n"):
    lignes.append(("        " + ligne if ligne.strip() else ligne) if not dans else ligne)
    if ligne.count('"""') % 2 == 1:
        dans = not dans
assert not dans
lignes[0] = "        {"
i13 = app.index("            \"id\": '13.6',")
fin13 = app.index('        },\n    ],\n}\n', i13)
assert fin13 < app.index('    "id": 14,', i13)
app = app[:fin13 + len('        },\n')] + "\n".join(lignes) + ",\n" + app[fin13 + len('        },\n'):]

# 5. méthode
mth = seg("MTH_13_7 = (", "\n# ====").rstrip()
avant('_mth("3.5", "Vérifier une pièce en fatigue", [', "_mth(" + mth[len("MTH_13_7 = ("):] + "\n\n")

# 6. ateliers : at176 et at177 après at175 (dernier élément)
i175 = app.index('        "id": "at175",')
fin_at = app.index("\n    },\n]\n", i175)
at = seg("ATELIERS_NOUVEAUX = [\n", "\n]\n")[len("ATELIERS_NOUVEAUX = [\n"):].rstrip().rstrip(",")
app = app[:fin_at] + "\n    },\n" + at + "," + app[fin_at + len("\n    },"):]


# 7. quiz
def chaine(txt, retrait, largeur=96):
    morceaux = textwrap.wrap(txt, largeur - retrait, break_long_words=False, drop_whitespace=False)
    return ("\n" + " " * retrait).join(json.dumps(m, ensure_ascii=False) for m in morceaux)


g = {}
exec(seg("QUIZ_PROCEDES = [", "\n]\n") + "\n]\n", g)
qs = []
for question, options, bonne, expl, niveau in g["QUIZ_PROCEDES"]:
    ops = ",\n       ".join(chaine(o, 7) for o in options)
    qs.append(f"    q({chaine(question, 6)},\n      [{ops}], {bonne},\n      {chaine(expl, 6)},\n"
              f"      {json.dumps(niveau, ensure_ascii=False)}),\n")
avant('QUIZ["Roulements et visserie : dimensionner"] = [',
      'QUIZ["Procédés : compléments et choix"] = [\n' + "\n".join(qs) + "]\n\n")

# 8. générateurs, nouvelle famille « Procédés » : catalogue ET menu « Thème »
gen = br.split("GENERATEUR = '''")[1].split("'''")[0].strip("\n")
avant("def gen_masse_piece():", gen + "\n\n\n")
apres('        "Statique des fluides": [gen_presse_hydraulique, gen_poussee_archimede],\n',
      '        "Procédés": [gen_seuil_rentabilite, gen_facettes_stl],\n')
remplacer('                          "Statique des fluides",\n',
          '                          "Statique des fluides", "Procédés",\n')

# 9. carte du programme : ligne « Procédés de fabrication et contraintes »
remplacer('''         "Obtention des bruts, usinage, plasturgie, chaudronnerie/soudage, fabrication "
         "additive métallique.",
         [(12, ["12.3", "12.4"]), (13, ["13.1", "13.2", "13.6"]), ("bloc0i", ["0.12.1", "0.12.2"])]),''',
          '''         "Obtention des bruts, usinage, plasturgie (injection, extrusion, soufflage, thermoformage, "
         "compression), poudres et MIM, chaudronnerie/soudage, brasage, friction, ultrasons, fabrication "
         "additive métallique, fichier STL et numérisation 3D, choix du procédé (seuil de rentabilité).",
         [(12, ["12.3", "12.4"]), (13, ["13.1", "13.2", "13.6", "13.7"]), ("bloc0i", ["0.12.1", "0.12.2"])]),''')

compile(app, APP, "exec")
open(APP, 'w', encoding='utf-8', newline='\n').write(app)
print("inséré")
