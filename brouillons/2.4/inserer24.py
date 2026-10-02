# Insère le brouillon 2.4 dans app.py (ancres textuelles uniques) et fait les six retouches validées
# par l'auteur : 1. bride 2.3 (IT13 de Ø11 = 0,27 ; « 82 → 99 % » retiré) ; 2. suppression d'at122
# (doublon d'at166, même erreur d'IT) ; 3. exercice 2.3 : trous de passage Ø12 H12 pour M10, système
# A B C ; 4. bride : ⊥ Ø0,03 A partout ; 5. surface brute : « sauf premières opérations, par cibles de
# référence » en 2.3 et en 5.5 ; 6. renvoi « Ⓜ développé en fiche 2.4 » dans la 2.3.
import json, os, re, textwrap

ICI = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(ICI, '..', '..', 'app.py')
app = open(APP, encoding='utf-8').read()
br = open(os.path.join(ICI, 'brouillon_2_4.py'), encoding='utf-8').read()


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
      "# 72g. GPS, COMPLÉMENTS — maximum et minimum de matière, zone projetée, état libre, références (fiche 2.4)\n"
      "#      Trous de passage : ISO 273, série moyenne (H13) ; IT : table ISO 286 de l'application.\n"
      "# ===========================================================================\n\n"
      + seg("def mmr_bonus():", "# --- figure à curseurs").rstrip() + "\n\n\n")

# 2. registre FIGURES
entrees = re.findall(r'^    "(\w+)": \("([^"]+)", (\w+)\),$', seg("FIGURES_NOUVELLES = {", "}\nDYN_NOUVELLE"), re.M)
assert len(entrees) == 5, entrees
apres('    "precharge_vis": ("Couple de serrage et précharge d\'une vis", precharge_vis),\n',
      "".join(f'    "{k}": ("{t}", {f}),\n' for k, t, f in entrees))

# 3. figure à curseurs + registre DYNAMIQUES
avant("# Figures à curseurs, insérées dans un texte de fiche par le repère [[DYN:cle]].",
      seg("def dyn_bonus_mm(", "FIGURES_NOUVELLES = {").rstrip() + "\n\n\n")
fin_dyn = ('         {"nom": "N", "label": "Vitesse N (tr/min)", "min": 300.0, "max": 3000.0, "defaut": 1500.0, '
           '"pas": 100.0}]),\n}')
remplacer(fin_dyn, fin_dyn[:-1] + seg('    "bonus_mm_curseurs": (', "}\n\n# ====").rstrip() + "\n}")

# 4. la fiche, en fin de bloc 2 (après la 2.3)
lignes, dans = [], False
for ligne in seg("FICHE_2_4 = {", "\n# ====").rstrip().split("\n"):
    lignes.append(("        " + ligne if ligne.strip() else ligne) if not dans else ligne)
    if ligne.count('"""') % 2 == 1:
        dans = not dans
assert not dans
lignes[0] = "        {"
i2 = app.index('            "id": "2.3",')
fin2 = app.index('        },\n    ],\n}\n', i2)
assert fin2 < app.index("VERSION DÉBUTANT DE LA FICHE 2.2")
app = app[:fin2 + len('        },\n')] + "\n".join(lignes) + ",\n" + app[fin2 + len('        },\n'):]

# 5. méthode
mth = seg("MTH_2_4 = (", "\n# ====").rstrip()
avant('_mth("6.19", "Vérifier un roulement pour une durée de vie visée", [', "_mth(" + mth[len("MTH_2_4 = ("):] + "\n\n")

# 6. ateliers : at166 et at167 après at165 (dernier élément) ; thème aligné sur les ateliers GPS existants
i165 = app.index('        "id": "at165",')
fin_at = app.index("\n    },\n]\n", i165)
at = seg("ATELIERS_NOUVEAUX = [\n", "\n]\n")[len("ATELIERS_NOUVEAUX = [\n"):].rstrip().rstrip(",")
at = at.replace('"theme": "Tolérancement géométrique",', '"theme": "Tolérancement géométrique (GPS)",')
app = app[:fin_at] + "\n    },\n" + at + "," + app[fin_at + len("\n    },"):]

# retouche 2 : suppression d'at122 (doublon d'at166, IT13 faux)
d122 = app.index('    {\n        "id": "at122",')
f122 = app.index("\n    },\n", d122) + len("\n    },\n")
assert app[d122:f122].count('"id": "at') == 1
app = app[:d122] + app[f122:]


# 7. quiz
def chaine(txt, retrait, largeur=96):
    morceaux = textwrap.wrap(txt, largeur - retrait, break_long_words=False, drop_whitespace=False)
    return ("\n" + " " * retrait).join(json.dumps(m, ensure_ascii=False) for m in morceaux)


g = {}
exec(seg("QUIZ_GPS = [", "\n]\n") + "\n]\n", g)
qs = []
for question, options, bonne, expl, niveau in g["QUIZ_GPS"]:
    ops = ",\n       ".join(chaine(o, 7) for o in options)
    qs.append(f"    q({chaine(question, 6)},\n      [{ops}], {bonne},\n      {chaine(expl, 6)},\n"
              f"      {json.dumps(niveau, ensure_ascii=False)}),\n")
avant('QUIZ["Roulements et visserie : dimensionner"] = [',
      'QUIZ["GPS : maximum de matière et modificateurs"] = [\n' + "\n".join(qs) + "]\n\n")

# 8. générateur, famille existante « Ajustements ISO »
gen = br.split("GENERATEUR = '''")[1].split("'''")[0].strip("\n")
avant("def gen_masse_piece():", gen + "\n\n\n")
remplacer('        "Ajustements ISO": [gen_iso_jeu, gen_iso_it],',
          '        "Ajustements ISO": [gen_iso_jeu, gen_iso_it, gen_bonus_mmr],')

# ---------------------------------------------------------------- retouches du contenu existant
# retouche 1 : bride de la 2.3 (IT13 de Ø11 = 0,27 mm, table ISO 286 ; 0,43 était l'IT14)
remplacer('''**Le gain apporté par Ⓜ, chiffré :**
- Trous à leur **minimum** (Ø11,0) → tolérance de position = **Ø0,4 mm**
- Trous à leur **maximum** (Ø11,43, IT13) → bonus = 11,43 − 11,00 = 0,43 mm
  → tolérance disponible = 0,4 + 0,43 = **Ø0,83 mm**, soit **plus du double**.

L'atelier peut percer avec un simple gabarit au lieu d'un centre d'usinage indexé. Le rendement
passe de 82 % à 99 %, **sans le moindre risque de non-assemblage** — car la condition Ⓜ garantit
mathématiquement que les vis passeront toujours.''',
          '''**Le gain apporté par Ⓜ, chiffré** (trous Ø11 H13 : 11,00 à 11,27 mm, ISO 286) :
- Trous à leur **minimum** (Ø11,00) → tolérance de position = **Ø0,4 mm**
- Trous à leur **maximum** (Ø11,27) → bonus = 11,27 − 11,00 = 0,27 mm
  → tolérance disponible = 0,4 + 0,27 = **Ø0,67 mm**, soit près de 70 % de plus.

L'atelier peut percer avec des moyens moins précis : toute pièce qui passe le calibre s'assemblera,
si la pièce en face respecte sa propre tolérance. Le maximum de matière Ⓜ est développé en fiche 2.4.''')

# retouche 4 : bride, ⊥ Ø0,03 A partout (tableau du cas : Ø0,03)
remplacer('''| **perpendicularité Ø0,05 A** | l'axe du trou doit rester dans un cylindre de 0,05 mm, droit par rapport à A |''',
          '''| **perpendicularité Ø0,03 A** | l'axe du trou doit rester dans un cylindre de 0,03 mm, droit par rapport à A |''')

# retouche 3 : exercice de la 2.3 — trous de passage Ø12 H12 (IT12 de 10-18 mm = 0,18 mm) pour vis M10,
# système de références A B C
i_ex = app.index("**Exercice type examen — Lecture et exploitation d'un tolérancement géométrique**")
j_ex = app.index("*Recommandation au BE : conserver ⌖ Ø0,05 Ⓜ A B.*", i_ex) + len("*Recommandation au BE : conserver ⌖ Ø0,05 Ⓜ A B.*")
ex = app[i_ex:j_ex]


def rex(a, b, n=1):
    global ex
    assert ex.count(a) == n, (a[:70], ex.count(a))
    ex = ex.replace(a, b)


rex('''Une plaque de guidage porte deux alésages **Ø12 H7** destinés à recevoir deux colonnes de guidage
d'un outillage de presse. Le dessin porte les spécifications suivantes :

- La face inférieure est **référence A**, avec ⏥ **0,02**
- Alésage n°1 : ⊥ **Ø0,02 A**
- Alésage n°2 : ⌖ **Ø0,05 Ⓜ A B**, où **B** est l'axe de l'alésage n°1
- Entraxe théorique encadré : ⟦150⟧''',
    '''Une plaque d'outillage de presse est fixée sur son bâti par deux vis M10, qui passent dans deux
**trous de passage Ø12 H12** (12,000 à 12,180 mm, ISO 286). Le dessin porte les spécifications
suivantes :

- La face inférieure est **référence A**, avec ⏥ **0,02**
- Trou n°1 : ⊥ **Ø0,02 A** ; son axe est la **référence B**
- Un chant usiné de la plaque, parallèle à l'entraxe, est la **référence C**
- Trou n°2 : ⌖ **Ø0,05 Ⓜ A B C**
- Position théorique du trou n°2, en cotes encadrées : ⟦150⟧ de B parallèlement à C, et sur la même
  parallèle à C que le trou n°1''')
rex('''3. Expliquer le choix de A comme référence primaire et de B comme référence secondaire.
4. L'alésage n°2 est mesuré à **Ø12,015 mm**.''',
    '''3. Expliquer le choix de A comme référence primaire, de B comme secondaire et de C comme tertiaire.
4. Le trou n°2 est mesuré à **Ø12,015 mm**.''')
rex('''5. Le centre mesuré de l'alésage n°2 se trouve à''', '''5. Le centre mesuré du trou n°2 se trouve à''')
rex('''   de sa position théorique. La pièce est-elle conforme ? Justifier par le calcul.
6. Le BE envisage de remplacer ⌖ Ø0,05 Ⓜ par une cotation **150 ± 0,025**.''',
    '''   de sa position théorique (Δx parallèle à C, Δy perpendiculaire). La pièce est-elle conforme ?
   Justifier par le calcul.
6. Le BE envisage de remplacer ⌖ Ø0,05 Ⓜ par deux cotes tolérancées : **150 ± 0,025** (selon x) et
   **0 ± 0,025** (selon y).''')
rex('''**b) ⊥ Ø0,02 A (alésage n°1)** — *« L'axe de l'alésage n°1 doit''', '''**b) ⊥ Ø0,02 A (trou n°1)** — *« L'axe du trou n°1 doit''')
rex('''**c) ⌖ Ø0,05 Ⓜ A B (alésage n°2)** — *« L'axe de l'alésage n°2 doit être contenu dans un cylindre
de Ø0,05 mm, dont l'axe est à la position théorique exacte (150 mm de B, perpendiculaire à A),
cette tolérance pouvant être augmentée du bonus de matière lorsque l'alésage s'écarte de son
maximum de matière. »*''',
    '''**c) ⌖ Ø0,05 Ⓜ A B C (trou n°2)** — *« L'axe du trou n°2 doit être contenu dans un cylindre
de Ø0,05 mm, perpendiculaire à A, dont l'axe est à la position théorique exacte (150 mm de B,
parallèlement à C), cette tolérance pouvant être augmentée du bonus de matière lorsque le trou
s'écarte de son maximum de matière. »*''')
rex('''**d) ⟦150⟧** — cote **théorique exacte**''', '''**d) ⟦150⟧** — cote **théorique exacte**''')
rex('''- **B = axe de l'alésage n°1 (référence secondaire)** : une fois la plaque posée à plat, il reste
  3 degrés (2 translations + 1 rotation dans le plan). La première colonne, engagée dans
  l'alésage n°1, **supprime les 2 translations**. Il ne reste que la rotation autour de cet axe.

- Le second alésage, localisé par rapport à A **et** B, supprime le dernier degré.

**L'ordre A puis B n'est pas interchangeable** : il reproduit la **chronologie réelle du montage**
(on pose à plat, *puis* on engage la première colonne, *puis* la seconde). Inverser l'ordre
donnerait un contrôle qui ne correspond plus à la mise en position réelle.''',
    '''- **B = axe du trou n°1 (référence secondaire)** : une fois la plaque posée à plat, il reste
  3 degrés (2 translations + 1 rotation dans le plan). Un pion de contrôle engagé dans le trou n°1
  **supprime les 2 translations**. Il ne reste que la rotation autour de cet axe.

- **C = chant usiné (référence tertiaire)** : la plaque, tournée jusqu'à appuyer sur C, perd le
  dernier degré. Sans C, la direction de Δy ne serait pas définie : la plaque pourrait tourner
  autour de B.

**L'ordre A, B, C n'est pas interchangeable** : il reproduit la **mise en position** (on pose à
plat, *puis* on centre sur le trou n°1, *puis* on oriente sur C). Inverser l'ordre donnerait un
contrôle qui ne correspond plus à la mise en position réelle.''')
rex('''L'alésage n°2 est un **Ø12 H7** → tranche 10-18 → IT7 = 18 µm → **12,000 à 12,018 mm**.

Pour un **alésage**, le maximum de matière correspond au **plus petit diamètre** :''',
    '''Le trou n°2 est un **Ø12 H12** → tranche 10-18 → IT12 = 180 µm → **12,000 à 12,180 mm**.

Pour un **trou**, le maximum de matière correspond au **plus petit diamètre** :''')
rex('''*Soit 30 % de tolérance en plus, gratuitement.*''', '''*Soit 30 % de tolérance en plus, sans risque pour l'assemblage.*''')
rex('''**Approche par cotation ± :** la zone de tolérance est un **carré** de côté $2 \\\\times 0,025 = 0,05$ mm.''',
    '''**Approche par cotation ± :** les deux cotes 150 ± 0,025 et 0 ± 0,025 définissent un **carré** de côté
$2 \\\\times 0,025 = 0,05$ mm.''')
rex('''La colonne de guidage, elle, ne sait pas si elle est décalée « en diagonale ».''',
    '''La vis, elle, ne sait pas si le trou est décalé « en diagonale ».''')
rex('''   (un simple gabarit à deux pions) qui reproduit exactement la condition d'assemblage''',
    '''   (un simple gabarit à pions, à la taille virtuelle) qui reproduit exactement la condition d'assemblage''')
rex('''*Recommandation au BE : conserver ⌖ Ø0,05 Ⓜ A B.*''',
    '''*Recommandation au BE : conserver ⌖ Ø0,05 Ⓜ A B C. (Ⓜ convient ici parce que ce sont des trous de
passage : sur un alésage de centrage, il n'aurait pas de sens — voir fiche 2.4.)*''')
assert "alésage n°" not in ex and "colonne" not in ex, [m.start() for m in re.finditer("alésage n°|colonne", ex)]
app = app[:i_ex] + ex + app[j_ex:]

# retouche 5 : surface brute en référence (2.3 affichée et 5.5)
remplacer('''dans le mécanisme** — presque toujours la face d'appui principale, jamais une surface brute de
fonderie.''',
          '''dans le mécanisme** — presque toujours la face d'appui principale usinée. Une surface brute de
fonderie ne sert de référence que pour les premières opérations, et alors par des **cibles de
référence** (fiche 2.4).''')
remplacer('''mécanisme** — presque toujours la face d'appui principale, **jamais une surface brute de
fonderie**.''',
          '''mécanisme** — presque toujours la face d'appui principale usinée. Une surface brute de fonderie
ne sert de référence que pour les premières opérations, et alors par des **cibles de référence**
(fiche 2.4).''')
remplacer('''3. **Choisir une surface brute comme référence.**''',
          '''3. **Choisir une surface brute comme référence d'une surface fonctionnelle usinée.**''', n=2)
remplacer('''**Choix de la référence** — la surface qui positionne la pièce dans le mécanisme,
jamais une surface brute de fonderie''',
          '''**Choix de la référence** — la surface qui positionne la pièce dans le mécanisme, usinée ;
une surface brute seulement pour les premières opérations, par des cibles de référence''')

# retouche 6 : renvoi dans le « À retenir » de la 2.3 affichée
remplacer('''- Chaîne courte, ou cale de réglage : c'est ce qui rend une conception économique.
"""''',
          '''- Chaîne courte, ou cale de réglage : c'est ce qui rend une conception économique.
- Les modificateurs (maximum de matière Ⓜ, minimum de matière Ⓛ, zone projetée Ⓟ, état libre Ⓕ)
  et les références spécifiées sont développés en **fiche 2.4**.
"""''')

compile(app, APP, "exec")
open(APP, 'w', encoding='utf-8', newline='\n').write(app)
print("inséré")
