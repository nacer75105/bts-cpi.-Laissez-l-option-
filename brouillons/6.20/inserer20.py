# Insère le brouillon 6.20 dans app.py (ancres textuelles uniques) et fait les trois retouches validées
# par l'auteur : 1. fiche 8.11 : 60 f / p est la vitesse de SYNCHRONISME ns, le moteur tourne en dessous
# (glissement) ; 2. « cos φ souvent 0,8 à 0,9 » (non sourcé) retiré de la 8.11 — et, par cohérence, la même
# affirmation retirée de la 8.3 et du commentaire de la figure plaque_moteur ; 3. figure plaque_moteur et
# exercice de la 8.3 : 7,9 A au lieu de 8,3 A, pour un rendement conforme à IE3 (≥ 88,6 % pour 4 kW, 4 pôles).
import json, os, re, textwrap

ICI = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(ICI, '..', '..', 'app.py')
app = open(APP, encoding='utf-8').read()
br = open(os.path.join(ICI, 'brouillon_6_20.py'), encoding='utf-8').read()


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


# 1. figures statiques (et fonctions du modèle moteur)
avant("# ===========================================================================\n# 73. CARACTÉRISER UNE FONCTION",
      "# ===========================================================================\n"
      "# 72h. CHAÎNE D'ÉNERGIE ET MOTORISATION — effort × flux, point de fonctionnement, IE (fiche 6.20)\n"
      "#      Classes IE : IEC 60034-30-1:2014 (tableau 50 Hz) ; obligations : règlement (UE) 2019/1781.\n"
      "#      Plaques moteur, charges, cylindrées, pressions, rendements ηv / ηm : données d'énoncé.\n"
      "# ===========================================================================\n\n"
      + seg("def chaine_energie():", "# --- figure à curseurs").rstrip() + "\n\n\n")

# 2. registre FIGURES
entrees = re.findall(r'^    "(\w+)": \("([^"]+)", (\w+)\),$', seg("FIGURES_NOUVELLES = {", "}\nDYN_NOUVELLE"), re.M)
assert len(entrees) == 6, entrees
apres('    "references_specifiees": ("Références spécifiées : simple, commune, système", references_specifiees),\n',
      "".join(f'    "{k}": ("{t}", {f}),\n' for k, t, f in entrees))

# 3. figure à curseurs + registre DYNAMIQUES
avant("# Figures à curseurs, insérées dans un texte de fiche par le repère [[DYN:cle]].",
      seg("_CHARGES = {", "FIGURES_NOUVELLES = {").rstrip() + "\n\n\n")
fin_dyn = ('         {"nom": "e", "label": "Décalage e du centre (mm)", "min": 0.0, "max": 0.35, "defaut": 0.23, '
           '"pas": 0.01}]),\n}')
remplacer(fin_dyn, fin_dyn[:-1] + seg('    "point_fonctionnement_curseurs": (', "}\n\n# ====").rstrip() + "\n}")

# 4. la fiche, en fin de bloc 6 (après la 6.19)
lignes, dans = [], False
for ligne in seg("FICHE_6_20 = {", "\n# ====").rstrip().split("\n"):
    lignes.append(("        " + ligne if ligne.strip() else ligne) if not dans else ligne)
    if ligne.count('"""') % 2 == 1:
        dans = not dans
assert not dans
lignes[0] = "        {"
i6 = app.index("            \"id\": '6.19',")
fin6 = app.index('        },\n    ],\n}\n', i6)
app = app[:fin6 + len('        },\n')] + "\n".join(lignes) + ",\n" + app[fin6 + len('        },\n'):]

# 5. méthode
mth = seg("MTH_6_20 = (", "\n# ====").rstrip()
avant('_mth("6.19", "Vérifier un roulement pour une durée de vie visée", [', "_mth(" + mth[len("MTH_6_20 = ("):] + "\n\n")

# 6. ateliers : at168 et at169 après at167 (dernier élément)
i167 = app.index('        "id": "at167",')
fin_at = app.index("\n    },\n]\n", i167)
at = seg("ATELIERS_NOUVEAUX = [\n", "\n]\n")[len("ATELIERS_NOUVEAUX = [\n"):].rstrip().rstrip(",")
app = app[:fin_at] + "\n    },\n" + at + "," + app[fin_at + len("\n    },"):]


# 7. quiz
def chaine(txt, retrait, largeur=96):
    morceaux = textwrap.wrap(txt, largeur - retrait, break_long_words=False, drop_whitespace=False)
    return ("\n" + " " * retrait).join(json.dumps(m, ensure_ascii=False) for m in morceaux)


g = {}
exec(seg("QUIZ_ENERGIE = [", "\n]\n") + "\n]\n", g)
qs = []
for question, options, bonne, expl, niveau in g["QUIZ_ENERGIE"]:
    ops = ",\n       ".join(chaine(o, 7) for o in options)
    qs.append(f"    q({chaine(question, 6)},\n      [{ops}], {bonne},\n      {chaine(expl, 6)},\n"
              f"      {json.dumps(niveau, ensure_ascii=False)}),\n")
avant('QUIZ["Roulements et visserie : dimensionner"] = [',
      'QUIZ["Chaîne d\'énergie et motorisation"] = [\n' + "\n".join(qs) + "]\n\n")

# 8. générateurs, nouvelle famille « Motorisation » : catalogue ET menu « Thème »
gen = br.split("GENERATEUR = '''")[1].split("'''")[0].strip("\n")
avant("def gen_masse_piece():", gen + "\n\n\n")
apres('        "Roulements": [gen_duree_roulement],\n',
      '        "Motorisation": [gen_point_fonctionnement, gen_pompe_hydraulique],\n')
remplacer('"Liaisons", "Roulements",\n', '"Liaisons", "Roulements", "Motorisation",\n')

# 9. carte du programme : ligne « Dynamique et Énergétique »
remplacer('''         "cames, systèmes articulés).",
         [(8, ["8.1", "8.5"]), (13, ["13.3", "13.5"]), ("bloc6", ["6.18"])]),''',
          '''         "cames, systèmes articulés), chaîne d'énergie (effort × flux, point de fonctionnement, classes "
         "IE, pompes et moteurs hydrauliques).",
         [(8, ["8.1", "8.5"]), (13, ["13.3", "13.5"]), ("bloc6", ["6.18", "6.20"])]),''')

# ---------------------------------------------------------------- retouches du contenu existant
# retouche 1 et 2 : fiche 8.11
i811 = app.index("            \"id\": '8.11',")
j811 = app.index('"id": ', i811 + 30)
f = app[i811:j811]


def rf(a, b, n=1):
    global f
    assert f.count(a) == n, (a[:70], f.count(a))
    f = f.replace(a, b)


rf('''$U$ est la tension entre deux phases (souvent $400$ V en triphasé industriel), $I$ le courant de
ligne, $cos(φ)$ le facteur de puissance de la charge (souvent $0{,}8$ à $0{,}9$ pour un moteur).''',
   '''$U$ est la tension entre deux phases (souvent $400$ V en triphasé industriel), $I$ le courant de
ligne, $cos(φ)$ le facteur de puissance de la charge (il se lit sur la plaque du moteur).''')
rf('''> $N (tr/min) = \\\\dfrac{60 × f}{p}$

$f$ est la fréquence du réseau ($50$ Hz en France), $p$ le nombre de **paires** de pôles du
moteur — pas le nombre de pôles. Un **variateur de fréquence** fait varier $f$ électroniquement,
donc fait varier la vitesse **sans changer ni le moteur ni la mécanique**''',
   '''> $n_s (tr/min) = \\\\dfrac{60 × f}{p}$

C'est la vitesse de **synchronisme** $n_s$ : celle du champ tournant, pas celle du moteur. Le moteur
asynchrone tourne **un peu en dessous** de $n_s$, d'autant plus qu'il est chargé : c'est le
**glissement** $g = (n_s − n)/n_s$ (fiches 6.20 et 13.3). Exemple : un moteur 4 pôles à $50$ Hz a
$n_s = 1500$ tr/min, et sa plaque indique par exemple $1445$ tr/min en charge nominale.

$f$ est la fréquence du réseau ($50$ Hz en France), $p$ le nombre de **paires** de pôles du
moteur — pas le nombre de pôles. Un **variateur de fréquence** fait varier $f$ électroniquement,
donc fait varier $n_s$ — et la vitesse du moteur, qui la suit à un glissement près — **sans changer
ni le moteur ni la mécanique**''')
rf('''**b)** Ce moteur a $2$ paires de pôles (donc $4$ pôles). À $50$ Hz : $N = 60 × 50/2 = 1500$
tr/min. Un variateur réduit la fréquence à $25$ Hz : $N = 60 × 25/2 = 750$ tr/min — la vitesse a
été divisée par deux, exactement comme la fréquence.''',
   '''**b)** Ce moteur a $2$ paires de pôles (donc $4$ pôles). À $50$ Hz : $n_s = 60 × 50/2 = 1500$
tr/min (vitesse de synchronisme ; le moteur tourne un peu en dessous). Un variateur réduit la
fréquence à $25$ Hz : $n_s = 60 × 25/2 = 750$ tr/min — la vitesse de synchronisme a été divisée par
deux, exactement comme la fréquence, et la vitesse du moteur suit, à son glissement près.''')
rf('''- $N = 60f/p$ ($p$ = paires de pôles) — un variateur fait varier $f$, donc directement $N$, sans
  toucher au moteur.''',
   '''- $n_s = 60f/p$ ($p$ = paires de pôles) est la vitesse de **synchronisme** ; le moteur tourne un peu
  en dessous (glissement). Un variateur fait varier $f$, donc $n_s$ et la vitesse du moteur, sans
  toucher au moteur.''')
rf('''**Vitesse de synchronisme** — $N$ (tr/min) $= 60 × f / p$, avec $p$ le nombre de PAIRES de pôles''',
   '''**Vitesse de synchronisme** — $n_s$ (tr/min) $= 60 × f / p$, avec $p$ le nombre de PAIRES de pôles ; le
moteur tourne un peu en dessous : glissement $g = (n_s − n)/n_s$''')
rf('''**Le réflexe variateur** — changer $f$ change directement $N$, dans les mêmes proportions''',
   '''**Le réflexe variateur** — changer $f$ change $n_s$ dans les mêmes proportions, et la vitesse du moteur
suit, à son glissement près''')
rf('''**2.** $N = 60 × 50 / 3$.

**3.** $N = 60 × 40 / 3$.''', '''**2.** $n_s = 60 × 50 / 3$.

**3.** $n_s = 60 × 40 / 3$.''')
rf('''**2.** $N = 1000$ tr/min.

**3.** $N = 800$ tr/min — cohérent : la fréquence a baissé de $20$ %, la vitesse aussi, exactement
dans la même proportion.''', '''**2.** $n_s = 1000$ tr/min (le moteur, lui, tournera un peu en dessous : glissement).

**3.** $n_s = 800$ tr/min — cohérent : la fréquence a baissé de $20$ %, la vitesse de synchronisme
aussi, exactement dans la même proportion.''')
rf('''la formule $N = 60f/p$ reste valable''', '''la formule $n_s = 60f/p$ reste valable''')
assert "$N = 60" not in f and "$N$ (tr/min)" not in f and "directement $N$" not in f
app = app[:i811] + f + app[j811:]

# retouche 2 (cohérence) : même affirmation non sourcée dans la 8.3
remplacer('''- **cos φ** (cosinus phi) : le **facteur de puissance**, qui traduit un déphasage entre tension
  et courant propre aux moteurs — typiquement entre 0,8 et 0,9''',
          '''- **cos φ** (cosinus phi) : le **facteur de puissance**, qui traduit un déphasage entre tension
  et courant propre aux moteurs — il se lit sur la plaque du moteur''')

# retouche 3 : plaque_moteur et exercice de la 8.3 — 7,9 A (η ≈ 0,89, conforme IE3 : ≥ 88,6 % pour 4 kW,
# 4 pôles, IEC 60034-30-1)
remplacer('''              ("8,3 A", "intensité"), ("1445 min⁻¹", "vitesse réelle"),''',
          '''              ("7,9 A", "intensité"), ("1445 min⁻¹", "vitesse réelle"),''')
remplacer('''               (215, "0,8 environ pour un moteur asynchrone", FIN),''',
          '''               (215, "déphasage courant / tension, lu sur la plaque", FIN),''')
remplacer('''**1.** Un moteur porte sur sa plaque : 4 kW, 400 V, 8,3 A, 1 445 tr/min, cos φ 0,82.''',
          '''**1.** Un moteur porte sur sa plaque : 4 kW, 400 V, 7,9 A, 1 445 tr/min, cos φ 0,82.''')
remplacer('''**1.** Puissance absorbée = √3 × U × I × cos φ = 1,732 × 400 × 8,3 × 0,82 = **4 716 W**
Puissance mécanique = 4 000 W → rendement = 4 000 / 4 716 = **0,85**

*C'est cohérent : un moteur de cette taille a un rendement de 0,85 à 0,90. Les 716 W de''',
          '''**1.** Puissance absorbée = √3 × U × I × cos φ = 1,732 × 400 × 7,9 × 0,82 = **4 488 W**
Puissance mécanique = 4 000 W → rendement = 4 000 / 4 488 = **0,89**

*C'est cohérent avec la classe IE3, qui impose au moins 88,6 % à un moteur de 4 kW, 4 pôles
(IEC 60034-30-1, fiche 6.20). Les 488 W de''')

compile(app, APP, "exec")
open(APP, 'w', encoding='utf-8', newline='\n').write(app)
print("inséré")
