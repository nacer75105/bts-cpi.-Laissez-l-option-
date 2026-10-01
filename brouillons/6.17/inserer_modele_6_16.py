# Insère le brouillon 6.16 dans app.py, par ancres textuelles uniques (sans ast, trop lent : une
# seule compilation de contrôle à la fin).
import json, os, re, textwrap

ICI = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'app.py')
app = open(APP, encoding='utf-8').read()
br = open(os.path.join(ICI, 'brouillon_6_16.py'), encoding='utf-8').read()


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


# 1. figures statiques, après celles de la 6.15
figs = seg("def _k_apparait(", "# --- figure à curseur")
avant("# ===========================================================================\n# 73. CARACTÉRISER UNE FONCTION",
      "# ===========================================================================\n"
      "# 72c. STATIQUE GRAPHIQUE — torseur, isolement, graphe des actions, 2 et 3 forces\n"
      "#      (fiche 6.16)\n"
      "# ===========================================================================\n\n" + figs.rstrip() + "\n\n\n")

# 2. registre FIGURES
entrees = re.findall(r'^    "(\w+)": \("([^"]+)", (\w+)\),$', seg("FIGURES_NOUVELLES = {", "}\nDYN_NOUVELLE"), re.M)
assert len(entrees) == 7, entrees
apres('    "composition_vitesses_pont": ("Composition des vitesses sur un pont roulant", composition_vitesses_pont),\n',
      "".join(f'    "{k}": ("{t}", {f}),\n' for k, t, f in entrees))

# 3. figure à curseur + registre DYNAMIQUES
avant("# Figures à curseurs, insérées dans un texte de fiche par le repère [[DYN:cle]].",
      seg("def dyn_potence_hauban(", "FIGURES_NOUVELLES = {").rstrip() + "\n\n\n")
fin_dyn = ('        [{"nom": "theta", "label": "Angle de manivelle θ (°)", "min": 0.0, "max": 360.0, '
           '"defaut": 60.0, "pas": 15.0}]),\n}')
assert app.count(fin_dyn) == 1
app = app.replace(fin_dyn, fin_dyn[:-1] + seg('    "potence_hauban_curseur": (', "}\n\n# ====").rstrip() + "\n}")

# 4. la fiche, en fin de bloc 6 (après la 6.15)
fiche = seg("FICHE_6_16 = {", "\n# ====")
lignes, dans = [], False
for ligne in fiche.rstrip().split("\n"):
    lignes.append(("        " + ligne if ligne.strip() else ligne) if not dans else ligne)
    if ligne.count('"""') % 2 == 1:
        dans = not dans
assert not dans
lignes[0] = "        {"
i6 = app.index("            \"id\": '6.15',")
fin6 = app.index('        },\n    ],\n}\n', i6)
app = app[:fin6 + len('        },\n')] + "\n".join(lignes) + ",\n" + app[fin6 + len('        },\n'):]

# 5. méthode
mth = seg("MTH_6_16 = (", "\n# ====").rstrip()
avant('_mth("6.9", "Vérifier la tenue d\'un assemblage vissé", [', "_mth(" + mth[len("MTH_6_16 = ("):] + "\n\n")

# 6. ateliers : at157 est le dernier élément de ATELIERS
i157 = app.index('        "id": "at157",')
fin_at = app.index("\n    },\n]\n", i157)
at = seg("ATELIERS_NOUVEAUX = [\n", "\n]\n")[len("ATELIERS_NOUVEAUX = [\n"):].rstrip().rstrip(",")
app = app[:fin_at] + "\n    },\n" + at + "," + app[fin_at + len("\n    },"):]


# 7. quiz
def chaine(txt, retrait, largeur=96):
    morceaux = textwrap.wrap(txt, largeur - retrait, break_long_words=False, drop_whitespace=False)
    return ("\n" + " " * retrait).join(json.dumps(m, ensure_ascii=False) for m in morceaux)


g = {}
exec(seg("QUIZ_STATIQUE = [", "\n]\n") + "\n]\n", g)
qs = []
for question, options, bonne, expl, niveau in g["QUIZ_STATIQUE"]:
    ops = ",\n       ".join(chaine(o, 7) for o in options)
    qs.append(f"    q({chaine(question, 6)},\n      [{ops}], {bonne},\n      {chaine(expl, 6)},\n"
              f"      {json.dumps(niveau, ensure_ascii=False)}),\n")
avant('QUIZ["Statique et frottement"] = [', 'QUIZ["Statique graphique"] = [\n' + "\n".join(qs) + "]\n\n")

# 8. générateur, catalogue et menu de l'Entraînement (les DEUX listes)
gen = br.split("GENERATEUR = '''")[1].split("'''")[0].strip("\n")
avant("def gen_masse_piece():", gen + "\n\n\n")
apres('        "Cinématique": [gen_bielle_manivelle],\n', '        "Statique": [gen_potence_hauban],\n')
a = '                          "Transmission de puissance", "Cinématique", "Matériaux et masses",'
assert app.count(a) == 1
app = app.replace(a, '                          "Transmission de puissance", "Cinématique", "Statique",\n'
                     '                          "Matériaux et masses",')

# 9. carte du programme
a = '''         "Degrés de liberté, schéma cinématique, isostatisme, cinématique du solide (vitesses, "
         "équiprojectivité, CIR, roulement sans glissement, loi entrée-sortie), "
         "équilibre/appuis/frottement — répartie sur six fiches distinctes plutôt qu'une seule.",
         [("bloc6", ["6.1", "6.2", "6.3", "6.15"]), (8, ["8.1"]), (12, ["12.1"]), (15, ["15.3"])]),'''
b = '''         "Degrés de liberté, schéma cinématique, isostatisme, cinématique du solide (vitesses, "
         "équiprojectivité, CIR, roulement sans glissement, loi entrée-sortie), "
         "équilibre/appuis/frottement, statique graphique (isolement, graphe des actions, 2 et 3 "
         "forces) — répartie sur sept fiches distinctes plutôt qu'une seule.",
         [("bloc6", ["6.1", "6.2", "6.3", "6.15", "6.16"]), (8, ["8.1"]), (12, ["12.1"]), (15, ["15.3"])]),'''
assert app.count(a) == 1
app = app.replace(a, b)

compile(app, APP, "exec")
open(APP, 'w', encoding='utf-8', newline='\n').write(app)
print("inséré")
