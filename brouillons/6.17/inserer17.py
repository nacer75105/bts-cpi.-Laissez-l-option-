# Insère le brouillon 6.17 dans app.py, par ancres textuelles uniques (une seule compilation de
# contrôle à la fin : ast.parse sur app.py prend plus d'une minute).
import json, os, re, textwrap

ICI = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(ICI, '..', '..', 'app.py')
app = open(APP, encoding='utf-8').read()
br = open(os.path.join(ICI, 'brouillon_6_17.py'), encoding='utf-8').read()


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


# 1. figures statiques, après celles de la 6.16
avant("# ===========================================================================\n# 73. CARACTÉRISER UNE FONCTION",
      "# ===========================================================================\n"
      "# 72d. MODÉLISATION DES LIAISONS — nature du contact, torseur transmissible, liaisons\n"
      "#      équivalentes, hyperstatisme (fiche 6.17)\n"
      "# ===========================================================================\n\n"
      + seg("def contacts_nature():", "# --- figure à curseurs").rstrip() + "\n\n\n")

# 2. registre FIGURES
entrees = re.findall(r'^    "(\w+)": \("([^"]+)", (\w+)\),$', seg("FIGURES_NOUVELLES = {", "}\nDYN_NOUVELLE"), re.M)
assert len(entrees) == 5, entrees
apres('    "echelle_mur": ("Échelle appuyée contre une paroi lisse", echelle_mur),\n',
      "".join(f'    "{k}": ("{t}", {f}),\n' for k, t, f in entrees))

# 3. figure à curseurs (table des paliers, fonction, choix) + registre DYNAMIQUES
avant("# Figures à curseurs, insérées dans un texte de fiche par le repère [[DYN:cle]].",
      seg("_PALIERS = {", "FIGURES_NOUVELLES = {").rstrip() + "\n\n\n")
fin_dyn = ('        [{"nom": "h", "label": "Hauteur d\'attache du hauban h (m)", "min": 0.3, "max": 1.2, '
           '"defaut": 0.6, "pas": 0.15}]),\n}')
remplacer(fin_dyn, fin_dyn[:-1] + seg('    "arbre_deux_paliers_choix": (', "}\n\n# ====").rstrip() + "\n}")

# 4. la fiche, en fin de bloc 6 (après la 6.16)
lignes, dans = [], False
for ligne in seg("FICHE_6_17 = {", "\n# ====").rstrip().split("\n"):
    lignes.append(("        " + ligne if ligne.strip() else ligne) if not dans else ligne)
    if ligne.count('"""') % 2 == 1:
        dans = not dans
assert not dans
lignes[0] = "        {"
i6 = app.index("            \"id\": '6.16',")
fin6 = app.index('        },\n    ],\n}\n', i6)
app = app[:fin6 + len('        },\n')] + "\n".join(lignes) + ",\n" + app[fin6 + len('        },\n'):]

# 5. méthode
mth = seg("MTH_6_17 = (", "\n# ====").rstrip()
avant('_mth("6.9", "Vérifier la tenue d\'un assemblage vissé", [', "_mth(" + mth[len("MTH_6_17 = ("):] + "\n\n")

# 6. ateliers : at159 est le dernier élément de ATELIERS
i159 = app.index('        "id": "at159",')
fin_at = app.index("\n    },\n]\n", i159)
at = seg("ATELIERS_NOUVEAUX = [\n", "\n]\n")[len("ATELIERS_NOUVEAUX = [\n"):].rstrip().rstrip(",")
app = app[:fin_at] + "\n    },\n" + at + "," + app[fin_at + len("\n    },"):]


# 7. quiz
def chaine(txt, retrait, largeur=96):
    morceaux = textwrap.wrap(txt, largeur - retrait, break_long_words=False, drop_whitespace=False)
    return ("\n" + " " * retrait).join(json.dumps(m, ensure_ascii=False) for m in morceaux)


g = {}
exec(seg("QUIZ_LIAISONS = [", "\n]\n") + "\n]\n", g)
qs = []
for question, options, bonne, expl, niveau in g["QUIZ_LIAISONS"]:
    ops = ",\n       ".join(chaine(o, 7) for o in options)
    qs.append(f"    q({chaine(question, 6)},\n      [{ops}], {bonne},\n      {chaine(expl, 6)},\n"
              f"      {json.dumps(niveau, ensure_ascii=False)}),\n")
avant('QUIZ["Statique et frottement"] = [', 'QUIZ["Modélisation des liaisons"] = [\n' + "\n".join(qs) + "]\n\n")

# 8. générateur, catalogue ET menu « Thème » de l'Entraînement
gen = br.split("GENERATEUR = '''")[1].split("'''")[0].strip("\n")
avant("def gen_masse_piece():", gen + "\n\n\n")
apres('        "Statique": [gen_potence_hauban],\n', '        "Liaisons": [gen_hyperstatisme_paliers],\n')
remplacer('                          "Transmission de puissance", "Cinématique", "Statique",\n',
          '                          "Transmission de puissance", "Cinématique", "Statique", "Liaisons",\n')

# 9. carte du programme
remplacer('''         "équilibre/appuis/frottement, statique graphique (isolement, graphe des actions, 2 et 3 "
         "forces) — répartie sur sept fiches distinctes plutôt qu'une seule.",
         [("bloc6", ["6.1", "6.2", "6.3", "6.15", "6.16"]), (8, ["8.1"]), (12, ["12.1"]), (15, ["15.3"])]),''',
          '''         "équilibre/appuis/frottement, statique graphique (isolement, graphe des actions, 2 et 3 "
         "forces), modélisation des liaisons (torseur transmissible, liaisons équivalentes, "
         "hyperstatisme) — répartie sur huit fiches distinctes plutôt qu'une seule.",
         [("bloc6", ["6.1", "6.2", "6.3", "6.15", "6.16", "6.17"]), (8, ["8.1"]), (12, ["12.1"]), (15, ["15.3"])]),''')

compile(app, APP, "exec")
open(APP, 'w', encoding='utf-8', newline='\n').write(app)
print("inséré")
