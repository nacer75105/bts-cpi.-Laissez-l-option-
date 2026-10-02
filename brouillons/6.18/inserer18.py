# Insère le brouillon 6.18 dans app.py, par ancres textuelles uniques (une seule compilation de
# contrôle à la fin : ast.parse sur app.py prend plus d'une minute).
import json, os, re, textwrap

ICI = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(ICI, '..', '..', 'app.py')
app = open(APP, encoding='utf-8').read()
br = open(os.path.join(ICI, 'brouillon_6_18.py'), encoding='utf-8').read()


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


# 1. figures statiques, après celles de la 6.17
avant("# ===========================================================================\n# 73. CARACTÉRISER UNE FONCTION",
      "# ===========================================================================\n"
      "# 72e. MÉCANISMES DE TRANSMISSION — accoupler, débrayer, limiter, freiner, transformer\n"
      "#      (fiche 6.18)\n"
      "# ===========================================================================\n\n"
      + seg("def chaine_transmission():", "# --- figure à curseurs").rstrip() + "\n\n\n")

# 2. registre FIGURES
entrees = re.findall(r'^    "(\w+)": \("([^"]+)", (\w+)\),$', seg("FIGURES_NOUVELLES = {", "}\nDYN_NOUVELLE"), re.M)
assert len(entrees) == 6, entrees
apres('    "broche_paliers": ("Arbre de broche sur deux bagues longues", broche_paliers),\n',
      "".join(f'    "{k}": ("{t}", {f}),\n' for k, t, f in entrees))

# 3. figure à curseurs + registre DYNAMIQUES
avant("# Figures à curseurs, insérées dans un texte de fiche par le repère [[DYN:cle]].",
      seg("def dyn_vis_ecrou(", "FIGURES_NOUVELLES = {").rstrip() + "\n\n\n")
fin_dyn = ('         {"nom": "b", "label": "Palier B", "choix": _CHOIX_PALIERS, "defaut": "linéaire annulaire '
           '(roulement libre)"}]),\n}')
remplacer(fin_dyn, fin_dyn[:-1] + seg('    "vis_ecrou_curseurs": (', "}\n\n# ====").rstrip() + "\n}")

# 4. la fiche, en fin de bloc 6 (après la 6.17)
lignes, dans = [], False
for ligne in seg("FICHE_6_18 = {", "\n# ====").rstrip().split("\n"):
    lignes.append(("        " + ligne if ligne.strip() else ligne) if not dans else ligne)
    if ligne.count('"""') % 2 == 1:
        dans = not dans
assert not dans
lignes[0] = "        {"
i6 = app.index("            \"id\": '6.17',")
fin6 = app.index('        },\n    ],\n}\n', i6)
app = app[:fin6 + len('        },\n')] + "\n".join(lignes) + ",\n" + app[fin6 + len('        },\n'):]

# 5. méthode
mth = seg("MTH_6_18 = (", "\n# ====").rstrip()
avant('_mth("6.9", "Vérifier la tenue d\'un assemblage vissé", [', "_mth(" + mth[len("MTH_6_18 = ("):] + "\n\n")

# 6. ateliers : at161 est le dernier élément de ATELIERS
i161 = app.index('        "id": "at161",')
fin_at = app.index("\n    },\n]\n", i161)
at = seg("ATELIERS_NOUVEAUX = [\n", "\n]\n")[len("ATELIERS_NOUVEAUX = [\n"):].rstrip().rstrip(",")
app = app[:fin_at] + "\n    },\n" + at + "," + app[fin_at + len("\n    },"):]


# 7. quiz
def chaine(txt, retrait, largeur=96):
    morceaux = textwrap.wrap(txt, largeur - retrait, break_long_words=False, drop_whitespace=False)
    return ("\n" + " " * retrait).join(json.dumps(m, ensure_ascii=False) for m in morceaux)


g = {}
exec(seg("QUIZ_TRANSMISSION = [", "\n]\n") + "\n]\n", g)
qs = []
for question, options, bonne, expl, niveau in g["QUIZ_TRANSMISSION"]:
    ops = ",\n       ".join(chaine(o, 7) for o in options)
    qs.append(f"    q({chaine(question, 6)},\n      [{ops}], {bonne},\n      {chaine(expl, 6)},\n"
              f"      {json.dumps(niveau, ensure_ascii=False)}),\n")
avant('QUIZ["Statique et frottement"] = [', 'QUIZ["Mécanismes de transmission"] = [\n' + "\n".join(qs) + "]\n\n")

# 8. générateur, dans la famille « Transmission de puissance » (déjà au catalogue et au menu Thème)
gen = br.split("GENERATEUR = '''")[1].split("'''")[0].strip("\n")
avant("def gen_masse_piece():", gen + "\n\n\n")
remplacer('        "Transmission de puissance": [gen_couple_puissance],\n',
          '        "Transmission de puissance": [gen_couple_puissance, gen_vis_ecrou],\n')

# 9. carte du programme : ligne « Dynamique et Énergétique »
remplacer('''         "F=ma, énergie cinétique, moment d'inertie — et depuis cette session, le PFD projeté "
         "sur un plan incliné (a = g·sin α).",
         [(8, ["8.1", "8.5"]), (13, ["13.3", "13.5"])]),''',
          '''         "F=ma, énergie cinétique, moment d'inertie, PFD projeté sur un plan incliné (a = g·sin α), "
         "et mécanismes de transmission (accouplements, embrayages, limiteurs, freins, vis-écrou, "
         "cames, systèmes articulés).",
         [(8, ["8.1", "8.5"]), (13, ["13.3", "13.5"]), ("bloc6", ["6.18"])]),''')

compile(app, APP, "exec")
open(APP, 'w', encoding='utf-8', newline='\n').write(app)
print("inséré")
