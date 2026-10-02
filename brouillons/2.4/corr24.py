# -*- coding: utf-8 -*-
# Corrections du brouillon 2.4 après relecture (relecteur-bts-meca B1-B4 + améliorations ;
# prof-pedagogue B1-B7 + améliorations).
import os, re
ICI = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(ICI, 'brouillon_2_4.py')
c = open(F, encoding='utf-8').read()


def R(a, b, n=1):
    global c
    assert c.count(a) == n, (a[:70], c.count(a))
    c = c.replace(a, b)


def remplacer_fonction(nom, nouveau):
    global c
    i = c.index(f"def {nom}(")
    j = c.index("\ndef ", i + 5)
    c = c[:i] + nouveau.strip("\n") + "\n\n" + c[j:]


# ---------------------------------------------------------------- figures
remplacer_fonction("mmr_bonus", '''
def mmr_bonus():
    """Trou de passage plus grand → la vis passe même si le trou est plus décalé : le bonus de Ⓜ.
    Vis, trou et décalage dessinés à la MÊME échelle (le jeu est exagéré pour être visible)."""
    p = [_k_defs(), _txt(30, 24, "Maximum de matière Ⓜ : plus le trou est grand, plus il peut être décalé", 13, TRAIT, "start", True)]
    cadres = ((30, "TROU AU PLUS PETIT : Ø11,00", 0.0, "décalage permis : 0,2 mm (zone Ø0,4)"),
              (275, "TROU MOYEN : Ø11,12", 0.12, "décalage permis : 0,26 mm (zone Ø0,52)"),
              (520, "TROU AU PLUS GRAND : Ø11,27", 0.27, "décalage permis : 0,335 mm (zone Ø0,67)"))
    rv, kj = 34, 60  # rayon dessiné de la vis Ø10 ; px par mm de jeu
    for x0, titre, bonus, legende in cadres:
        cx, cy = x0 + 95, 150
        p.append(f"<rect x='{x0}' y='40' width='225' height='230' rx='8' fill='#ffffff' stroke='{ALESAGE}' stroke-width='2'/>")
        p.append(_txt(x0 + 112, 62, titre, 11, ALESAGE, "middle", True))
        rt = rv + (1.0 + bonus) / 2 * kj           # rayon du trou : vis + jeu radial
        dec = (0.4 + bonus) / 2 * kj                # décalage permis (rayon de la zone)
        # vis à la position exacte
        p.append(f"<circle cx='{cx}' cy='{cy}' r='{rv}' fill='#fde68a' stroke='{ARBRE}' stroke-width='1.6'/>")
        p.append(_txt(cx, cy + 4, "vis", 10, ARBRE, "middle", True))
        # trou réel décalé au maximum permis, avec son centre
        p.append(f"<g><circle cx='{cx + dec:.1f}' cy='{cy}' r='{rt:.1f}' fill='none' stroke='{TRAIT}' stroke-width='2.4'/>"
                 f"<line x1='{cx + dec - 5:.1f}' y1='{cy}' x2='{cx + dec + 5:.1f}' y2='{cy}' stroke='{TRAIT}' stroke-width='1.6'/>"
                 f"<line x1='{cx + dec:.1f}' y1='{cy - 5}' x2='{cx + dec:.1f}' y2='{cy + 5}' stroke='{TRAIT}' stroke-width='1.6'/>"
                 f"<animateTransform attributeName='transform' type='translate' values='0,0; {-dec:.1f},0; 0,0' dur='3s' repeatCount='indefinite'/></g>")
        # jeu restant côté gauche (constant : 0,3 mm)
        p.append(f"<line x1='{cx - rv - 0.3 * kj:.1f}' y1='{cy - 52}' x2='{cx - rv:.1f}' y2='{cy - 52}' stroke='{OK}' stroke-width='2'/>")
        p.append(_txt(cx - rv - 9, cy - 58, "jeu restant", 9, OK, "middle", True))
        # loupe : la zone où le centre a le droit d'être
        lx, ly, kz = x0 + 190, 100, 50
        p.append(f"<circle cx='{lx}' cy='{ly}' r='{(0.4 + bonus) / 2 * kz:.1f}' fill='#dcfce7' stroke='{OK}' stroke-width='1.4'/>")
        p.append(f"<circle cx='{lx + (0.4 + bonus) / 2 * kz:.1f}' cy='{ly}' r='2.5' fill='{TRAIT}'/>")
        p.append(_txt(lx, ly + 28, "zone du centre", 9, OK, "middle"))
        p.append(_txt(x0 + 112, 246, legende, 10, OK, "middle", True))
    p.append(_txt(30, 288, "Jaune : la vis M10, à sa place. Noir : le trou réel, décalé au maximum permis (croix = son centre). Vert : zone où ce centre a le droit d'être.", 10, FIN))
    p.append(f"<rect x='30' y='298' width='715' height='52' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 320, "Le jeu restant est le même dans les trois cas : le trou plus grand « paie » lui-même son décalage supplémentaire.", 12, TRAIT, "start", True))
    p.append(_txt(46, 340, "Le jeu est exagéré sur le dessin ; le jeu restant (0,3 mm) est la part réservée aux défauts de l'autre pièce.", 11, FIN))
    return _svg("".join(p), 775, 364)
''')

remplacer_fonction("mmr_calibre", '''
def mmr_calibre():
    """Le calibre fonctionnel : une broche au diamètre virtuel, à la position exacte."""
    p = [_k_defs(), _txt(30, 24, "Le sens physique de Ⓜ : un calibre fixe dit si la pièce s'assemble", 13, TRAIT, "start", True)]
    p.append(f"<rect x='60' y='60' width='280' height='200' rx='6' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.6'/>")
    p.append(_txt(200, 76, "plaque posée sur A, poussée contre B et C", 10, FIN, "middle"))
    pos = ((110, 120), (290, 120), (110, 210), (290, 210))
    dec = ((4, -2), (-3, 3), (2, 4), (-4, -2))
    for (x, y), (dx, dy) in zip(pos, dec):
        p.append(f"<circle cx='{x + dx}' cy='{y + dy}' r='22' fill='#ffffff' stroke='{TRAIT}' stroke-width='2'/>")
        p.append(f"<circle cx='{x}' cy='{y}' r='16' fill='{OK}' opacity='0.75'>"
                 "<animate attributeName='opacity' values='0.75;0.35;0.75' dur='2s' repeatCount='indefinite'/></circle>")
    p.append(f"<line x1='132' y1='120' x2='175' y2='150' stroke='{FIN}' stroke-width='1'/>")
    p.append(_txt(178, 156, "trou réel (décalé)", 10, TRAIT))
    p.append(f"<line x1='110' y1='194' x2='150' y2='176' stroke='{FIN}' stroke-width='1'/>")
    p.append(_txt(153, 178, "broche Ø10,6", 10, OK, "start", True))
    p.append(_txt(200, 284, "les 4 broches entrent en même temps → pièce bonne", 11, OK, "middle", True))
    x0 = 380
    p.append(f"<rect x='{x0}' y='44' width='390' height='236' rx='6' fill='#ffffff' stroke='{OK}' stroke-width='1.6'/>")
    for i, (t, g, c) in enumerate((("Le calibre : 4 broches parfaites, aux positions exactes,", True, TRAIT),
                                   ("de diamètre = taille virtuelle :", False, TRAIT),
                                   ("Ø11,00 (trou au plus petit) − 0,4 (zone) = Ø10,6", True, OK),
                                   ("", False, TRAIT),
                                   ("Trou de diamètre D décalé de e : son bord le plus", False, TRAIT),
                                   ("proche est à D/2 − e de la position exacte. La plus", False, TRAIT),
                                   ("grosse broche qui entre a pour diamètre D − 2e.", False, TRAIT),
                                   ("Pièce bonne si D − 2e ≥ 10,6,", False, TRAIT),
                                   ("soit 2e ≤ 0,4 + (D − 11,00) : la règle du bonus.", True, TRAIT),
                                   ("La taille du trou (11,00 à 11,27) se contrôle à part.", False, FIN))):
        if t:
            p.append(_txt(x0 + 14, 66 + 21 * i, t, 12, c, "start", g))
    p.append(f"<rect x='30' y='296' width='740' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 318, "Ⓜ ne relâche pas la fonction : il accepte tout ce qui passe le calibre, et seulement cela.", 12, TRAIT))
    return _svg("".join(p), 800, 344)
''')

R('''    p.append(_txt(212, 140, "trou de passage", 9, FIN))''',
  '''    p.append(_txt(212, 140, "trou de passage", 9, FIN))
    p.append(_txt(70, 300, "zone projetée sur 40 mm (= épaisseur de la pièce assemblée)", 10, ALERTE))''')
R('''                                   ("La réponse : Ⓟ suivi d'une longueur encadrée", True, ALERTE),
                                   ("(l'épaisseur de la pièce assemblée) : la tolérance", False, TRAIT),
                                   ("s'applique au-dessus de la surface, sur cette longueur.", False, TRAIT))):''',
  '''                                   ("La réponse : Ⓟ suivi de la longueur de projection", True, ALERTE),
                                   ("(l'épaisseur de la pièce assemblée), ex. ⊥ Ø0,1 Ⓟ 40 A :", False, TRAIT),
                                   ("la zone s'applique au-dessus de la surface, sur 40 mm.", False, TRAIT))):''')
R('''"Ⓟ sert pour les goujons, vis et pions ajustés : là où l'élément fileté sort de la pièce cotée."''',
  '''"Ⓟ sert là où un élément inséré (goujon, vis, pion) sort de la pièce cotée et traverse la suivante."''')
R('''    p.append(f"<rect x='30' y='286' width='730' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 308,''', '''    p.append(f"<rect x='30' y='310' width='730' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 332,''')
R('''    return _svg("".join(p), 790, 334)''', '''    return _svg("".join(p), 790, 358)''')
# Ⓛ / Ⓕ
R('''Ⓛ : GARANTIR UNE ÉPAISSEUR MINIMALE''', '''Ⓛ : GARANTIR UNE PAROI MINIMALE''')
R('''    p.append(_txt(680, 222, "maintenue (montée)", 10, TRAIT, "middle", True))''',
  '''    p.append(_txt(680, 222, "maintenue (montée)", 10, TRAIT, "middle", True))
    p.append(_txt(680, 86, "appuis du montage de contrôle", 9, FIN, "middle"))''')
R('''    p.append(_txt(46, 304, "Ⓛ : comme Ⓜ, mais le pire cas est l'autre extrême (trou au plus grand, arbre au plus petit).", 12, TRAIT))
    p.append(_txt(46, 324, "Ⓕ : la tolérance s'applique à la pièce libre ; sinon, à la pièce maintenue dans les conditions notées sur le plan.", 12, FIN))''',
  '''    p.append(_txt(46, 304, "Ⓛ : paroi garantie au pire cas (trou au plus grand) ; un trou plus petit reçoit un bonus de position.", 12, TRAIT))
    p.append(_txt(46, 324, "Ⓕ : sur un plan marqué ISO 10579-NR (pièce contrôlée maintenue), Ⓕ signale ce qui se vérifie à l'état libre.", 12, FIN))''')
# références : points 3-2-1 et côté matière
R('''    p.append(f"<rect x='560' y='100' width='140' height='90' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.6'/>")''',
  '''    p.append(f"<rect x='560' y='100' width='140' height='90' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.6'/>")
    for x_, y_ in ((580, 194), (630, 194), (680, 194)):
        p.append(f"<circle cx='{x_}' cy='{y_}' r='4' fill='{OK}'/>")
    for x_, y_ in ((556, 120), (556, 170)):
        p.append(f"<circle cx='{x_}' cy='{y_}' r='4' fill='{ALESAGE}'/>")
    p.append(f"<circle cx='630' cy='96' r='4' fill='{ARBRE}'/>")
    p.append(_txt(712, 198, "A", 11, OK, "start", True))
    p.append(_txt(546, 148, "B", 11, ALESAGE, "end", True))
    p.append(_txt(642, 94, "C", 11, ARBRE, "start", True))''')
R('''    p.append(_txt(142, 120, "surface réelle (imparfaite)", 10, TRAIT, "middle"))''',
  '''    p.append(f"<rect x='50' y='130' width='180' height='34' fill='#e2e8f0' opacity='0.7'/>")
    p.append(_txt(142, 150, "matière", 9, FIN, "middle"))
    p.append(_txt(142, 120, "surface réelle (imparfaite)", 10, TRAIT, "middle"))''')
# figure à curseurs
R('''    p.append(_txt(cx, 56, "centre du trou (point) et position exacte (centre)", 10, FIN, "middle"))''',
  '''    p.append(_txt(cx, 56, "gros point = centre réel du trou ; petit point = position exacte ; trait = décalage e", 10, FIN, "middle"))''')
R('''(f"zone occupée : 2 × e = Ø{_fr_court(occ, 3)}", TRAIT, False),''',
  '''(f"plus petite zone contenant le centre : Ø2e = Ø{_fr_court(occ, 3)}", TRAIT, False),''')

# ---------------------------------------------------------------- cours
R('''Les **modificateurs** (une lettre entourée dans le cadre) règlent ces cas : **Ⓜ** (maximum de matière),
**Ⓛ** (minimum de matière), **Ⓟ** (zone projetée), **Ⓕ** (état libre). Comme l'exigence de l'enveloppe
**Ⓔ** vue en 2.3, ce sont des **exceptions déclarées** au principe d'indépendance : sans symbole, la règle
reste l'indépendance.''',
  '''Les **modificateurs** (une lettre entourée dans le cadre) règlent ces cas. Ils sont de deux natures :

- **Ⓜ** (maximum de matière) et **Ⓛ** (minimum de matière), comme l'exigence de l'enveloppe **Ⓔ** vue en
  2.3, sont des **exceptions déclarées** au principe d'indépendance : ils **lient la taille et la
  géométrie**. Sans symbole, l'indépendance reste la règle.
- **Ⓟ** (zone projetée) et **Ⓕ** (état libre) sont d'une autre nature : Ⓟ **déplace** la zone de
  tolérance, Ⓕ précise **dans quel état** (libre ou maintenu) on contrôle la pièce.

En 2.3, tu as vu Ⓜ comme une formule de bonus. Ici, on comprend **pourquoi** cette formule est juste.''')

R('''- un **arbre** est au maximum de matière quand il est **au plus gros** (d max).

C'est le **pire cas pour l'assemblage** : le trou le plus petit et l'arbre le plus gros laissent le
moins de jeu.''',
  '''- un **arbre** est au maximum de matière quand il est **au plus gros** (d max).

*Le test de la balance : pèse la plaque. Un trou, c'est du vide ; le métal est **autour**. Plus le trou est
petit, plus il reste de métal, plus la plaque est lourde. « Maximum de matière » = **la pièce la plus
lourde** : plaque aux trous les plus petits, arbre le plus gros.* ⚠️ « Maximum » ne veut pas dire « plus
grand trou » : pour un trou, maximum de matière = **plus petit** diamètre.

C'est le **pire cas pour l'assemblage** : le trou le plus petit et l'arbre le plus gros laissent le
moins de jeu. Imagine le pire montage possible : le trou le plus petit permis, décalé du maximum permis,
face à la vis. Si **celui-là** s'assemble encore, tous les autres s'assembleront.

*Notations : D (majuscule) pour un trou, d (minuscule) pour un arbre ; t = la tolérance écrite dans le
cadre.*''')

R('''position des trous est tolérancée **⌖ Ø0,4 Ⓜ A B**.''',
  '''position des trous est tolérancée **⌖ Ø0,4 Ⓜ A B C** (A : face d'appui ; B et C : deux chants usinés,
qui fixent les directions x et y).''')

R('''- Au plus grand (Ø11,27) : **Ø0,4 + 0,27 = Ø0,67**.
''', '''- Au plus grand (Ø11,27) : **Ø0,4 + 0,27 = Ø0,67**.

*Pourquoi ajouter 0,12 tel quel ? Le trou passe de Ø11,00 à Ø11,12 : il s'élargit de 0,06 mm **de chaque
côté**. Son centre peut donc aller 0,06 mm plus loin **dans n'importe quelle direction** sans que le bord
touche la vis. Le cercle où le centre a le droit d'être grossit de 0,06 en rayon, donc de **0,12 en
diamètre**. Gain de diamètre du trou = gain de diamètre de la zone.*
''')

R('''Ce supplément s'appelle le **bonus**. Il n'est pas un cadeau : c'est exactement le jeu supplémentaire
que la pièce apporte elle-même.''',
  '''Ce supplément s'appelle le **bonus**. Il n'est pas un cadeau : c'est exactement le jeu supplémentaire
que la pièce apporte elle-même.

*D réel : pour un trou imparfait (ovale, tordu), c'est le diamètre du plus grand cylindre parfait qui y
entre — le calibre, lui, en tient compte tout seul.*''')

R('''Imaginez le contrôle le plus direct : un **calibre** avec quatre broches parfaites, placées aux positions
exactes, de diamètre **Ø11,00 − 0,4 = Ø10,6**. C'est la **taille virtuelle** au maximum de matière : le
« trou parfait » le plus contraignant qu'on accepte.

Un trou de diamètre D, décalé de e de sa position exacte, laisse passer une broche à la position exacte
de diamètre **D − 2e**. La pièce passe le calibre si D − 2e ≥ 10,6, c'est-à-dire si **2e ≤ 0,4 +
(D − 11,00)** — c'est la règle du bonus, retrouvée par la géométrie. Et si le calibre entre, les vis
entreront : la fonction est garantie au pire cas.

*Exemple : trou mesuré Ø11,12, centre décalé de Δx = 0,20 mm et Δy = 0,12 mm. e = √(0,20² + 0,12²) ≈ 0,233
mm, zone occupée 2e ≈ Ø0,466.*''',
  '''**D'où vient le Ø0,4 ?** Entre une vis Ø10 et un trou Ø11,00, il y a 1 mm de jeu sur le diamètre. Le
bureau d'études n'en donne qu'une partie, 0,4, à la position de ce trou : le reste est réservé aux
défauts de l'autre pièce (le taraudage du bâti est lui aussi un peu mal placé) et à une marge.

Imagine le contrôle le plus direct : un **calibre**, une plaque d'acier avec quatre « doigts » ronds,
placés aux positions exactes, de diamètre **Ø11,00 − 0,4 = Ø10,6**. On présente la pièce contre ses
références A, B, C : si les quatre doigts s'enfilent en même temps, la pièce est bonne. Ce diamètre est
la **taille virtuelle** : la plus grosse « vis parfaite, parfaitement placée » que tous les trous
acceptables doivent laisser passer. Elle combine les deux pires cas : le plus petit trou (11,00), moins
toute la place que le défaut de position peut lui faire perdre (0,4).

**Pourquoi c'est la même règle.** Prenons un trou de diamètre D dont le centre est décalé de e. Son bord le
plus proche de la position exacte n'est plus à D/2 de celle-ci, mais à **D/2 − e** : le trou « mange » e
d'un côté. La plus grosse broche qui entre, plantée à la position exacte, a donc un rayon D/2 − e, soit un
**diamètre D − 2e**. Elle doit valoir au moins 10,6 :

> D − 2e ≥ 11,00 − 0,4  ⇔  **2e ≤ 0,4 + (D − 11,00)**

On retrouve mot pour mot la règle du bonus. Et si le calibre entre, les vis entreront : la fonction est
garantie au pire cas — à condition que la pièce en face respecte, elle aussi, sa tolérance.

**Attention : rayon ou diamètre.** La tolérance Ø0,4 est un **diamètre** de zone. Le décalage e se mesure
depuis le centre : c'est un **rayon**. Pense à une cible de fléchettes de 0,4 de diamètre : son rayon n'est
que de 0,2 ; une fléchette à 0,23 du centre est **hors** de la cible, même si 0,23 < 0,4. Le centre est
dans la zone si e ≤ t/2, soit **2e ≤ t**.

*Exemple : trou mesuré Ø11,12, centre décalé de Δx = 0,20 mm et Δy = 0,12 mm. e = √(0,20² + 0,12²) ≈ 0,233
mm (Pythagore : le décalage réel, en diagonale) ; plus petite zone contenant le centre : 2e ≈ Ø0,466.*''')

R('''**Le gain pour l'atelier.** Le bonus élargit la tolérance de position dès que les trous ne sont pas au
plus petit : l'atelier peut accepter plus de pièces, ou percer avec des moyens moins précis, **sans aucun
risque pour l'assemblage**. C'est un gain de coût obtenu par la seule cotation.

**Quand ne pas mettre Ⓜ.** Quand la fonction n'est **pas** un assemblage avec jeu : un alésage de
centrage, un ajustement serré, une position qui règle un mécanisme (un engrenage, un capteur). Là, un
trou plus grand ne compense rien : la position doit être tenue telle quelle.''',
  '''**Le gain pour l'atelier.** Le bonus élargit la tolérance de position dès que les trous ne sont pas au
plus petit : l'atelier peut accepter plus de pièces, ou percer avec des moyens moins précis, **sans risque
pour l'assemblage**. C'est un gain de coût obtenu par la seule cotation.

**Ce que Ⓜ ne change pas.** La taille reste contrôlée : le diamètre doit rester entre 11,00 et 11,27. Le
calibre vérifie la position ; un tampon ou un alésomètre vérifie la taille. C'est le **tolérancement par
gabarits** du référentiel.

**Quand ne pas mettre Ⓜ.** Quand la fonction n'est **pas** un assemblage avec jeu : un alésage de
centrage, un ajustement serré, une position qui règle un mécanisme (un engrenage, un capteur). *Un
roulement monté dans un alésage de centrage : si l'alésage est plus grand, le roulement flotte. Le jeu en
plus n'aide pas, il aggrave.* Ⓜ n'a de sens que si un trou plus grand **rend service** à l'assemblage.''')

R('''Ⓛ suit la même logique que Ⓜ, mais pour l'autre extrême : le **minimum de matière** (trou au plus
**grand**, arbre au plus **petit**). On l'utilise quand le risque n'est pas « ça ne passe pas » mais
« **il ne reste pas assez de matière** » : un trou près d'un bord (épaisseur de paroi minimale), un
tube dont la paroi doit résister, une surépaisseur d'usinage à garantir.

> trou : **t disponible = t + (D max − D réel)** · arbre : **t disponible = t + (d réel − d min)**

*Un trou plus petit que son maximum laisse plus de métal autour de lui : il peut être un peu plus décalé
vers le bord sans que la paroi descende sous son minimum.*''',
  '''Ⓛ suit la même logique que Ⓜ, mais pour l'autre extrême : le **minimum de matière** (trou au plus
**grand**, arbre au plus **petit** — la plaque la plus **légère**). On l'utilise quand le risque n'est pas
« ça ne passe pas » mais « **il ne reste pas assez de matière** » : un trou près d'un bord (épaisseur de
paroi minimale), un tube dont la paroi doit résister, une surépaisseur d'usinage (la couche de métal à
enlever en finition) à garantir.

Pour la paroi, le pire cas est le trou **au plus grand** et décalé vers le bord : c'est à ce pire cas que
la tolérance t est donnée. Un trou plus petit laisse plus de métal autour de lui : il peut être un peu
plus décalé sans que la paroi descende sous son minimum. Ⓛ lui accorde ce bonus :

> trou : **t disponible = t + (D max − D réel)** · arbre : **t disponible = t + (d réel − d min)**

*Exemple : trou Ø11 H13 (11,00 à 11,27) près d'un bord, ⌖ Ø0,4 Ⓛ. Mesuré Ø11,15, il est plus petit que son
maximum de 0,12 : zone Ø0,4 + 0,12 = Ø0,52.*

**Ce que Ⓛ apporte vraiment.** Sans modificateur, la zone Ø0,4 vaut pour tous les diamètres : la paroi
minimale est déjà garantie. Mais on rebute alors des trous plus petits qui pourraient être plus décalés
sans danger. Ⓛ garantit **la même paroi** et accepte ces trous — exactement comme Ⓜ pour un assemblage.''')

R('''Le symbole **Ⓟ**, suivi d'une longueur **encadrée** (en général l'épaisseur de la pièce assemblée),
reporte la zone de tolérance **au-dessus de la surface**, sur cette longueur (ISO 1101). On tolérance
l'axe là où il travaille vraiment.

*Exemple (données d'énoncé) : l'axe d'un taraudage de 12 mm de profondeur s'écarte de 0,04 mm pour 10 mm
de hauteur. Sur la profondeur du trou, son écart est de 0,04 × 12 / 10 = 0,048 mm : il tient dans une
perpendicularité Ø0,1. Mais sur les 40 mm de la pièce assemblée, l'écart atteint 0,04 × 40 / 10 =
0,16 mm : hors de Ø0,1. Sans Ⓟ, la pièce serait acceptée et l'assemblage coincerait.*''',
  '''*Un goujon, c'est une tige filetée aux deux bouts, vissée dans le bâti. Pense à un piquet planté un peu de
travers : au ras du sol, l'écart est minuscule ; en haut du piquet, il saute aux yeux.*

Le symbole **Ⓟ**, suivi de la **longueur de projection** (en général l'épaisseur de la pièce assemblée),
reporte la zone de tolérance **au-dessus de la surface**, sur cette longueur (ISO 1101). Exemple de cadre :
**⊥ | Ø0,1 Ⓟ 40 | A** — perpendicularité à la face d'appui A, zone projetée sur 40 mm. On tolérance l'axe
là où il travaille vraiment.

*Exemple (données d'énoncé) : l'axe d'un taraudage de 12 mm de profondeur s'écarte de 0,04 mm pour 10 mm
de hauteur. Sur la profondeur du trou, son écart est de 0,04 × 12 / 10 = 0,048 mm : il tient dans une
perpendicularité Ø0,1. Mais sur les 40 mm de la pièce assemblée, l'écart atteint 0,04 × 40 / 10 =
0,16 mm : hors de Ø0,1. Sans Ⓟ, la pièce serait acceptée alors que, dans la pièce assemblée, l'axe sort de
la tolérance que le concepteur a jugée nécessaire au montage.*

*Ici, pas de 2e : pour une perpendicularité, le cylindre n'est pas planté à une position exacte ; on peut le
décaler pour qu'il enveloppe au mieux l'axe. Seule compte la dérive totale de l'axe sur la longueur,
comparée directement au diamètre de la zone. Le 2e ne sert que pour une **localisation** ⌖, dont la zone est
centrée sur la position exacte.*''')

R('''Une pièce **non rigide** (joint, pièce mince en tôle ou en plastique, grande couronne) n'a pas la même
forme posée sur une table et montée dans son logement : elle se déforme sous son poids ou sous l'effort de
maintien. La norme ISO 10579 prévoit que, pour ces pièces, les tolérances s'appliquent **à la pièce
maintenue** dans les conditions notées sur le plan (efforts, position, appuis). Le symbole **Ⓕ** indique
qu'une tolérance particulière s'applique au contraire **à l'état libre**.

*Exemple : une bague d'étanchéité mince peut être tolérancée en circularité une fois montée (son
logement la remet ronde), et seulement limitée en ovalisation à l'état libre (Ⓕ), pour qu'elle reste
montable.*''',
  '''*Pense à un joint torique : posé sur la table, il s'avachit en ovale ; enfilé dans sa gorge, il redevient
rond. Mesurer sa circularité sur la table n'a pas de sens : on mesurerait son avachissement, pas sa
fabrication.*

**La règle par défaut.** Toute spécification s'applique à la pièce **libre**, comme si elle était
indéformable (ISO 8015, principe de la pièce rigide). C'est juste pour un carter en fonte, pas pour une
pièce **non rigide** (joint, pièce mince en tôle ou en plastique, grande couronne), qui se déforme sous son
poids ou sous l'effort de maintien.

**Pour une pièce non rigide.** Le concepteur écrit **ISO 10579-NR** près du cartouche et indique les
conditions de maintien (appuis, efforts, position) : les tolérances s'appliquent alors à la pièce
**maintenue** dans ces conditions. Le symbole **Ⓕ** signale celles qui restent à vérifier **à l'état
libre**.

*Exemple : une bague d'étanchéité mince sur un plan marqué ISO 10579-NR : une circularité serrée, vérifiée
dans un montage qui l'imite montée, et une circularité Ⓕ plus large à l'état libre, pour qu'elle reste
montable par l'opérateur.*''')

R('''- **On ne mesure jamais « par rapport à une surface »** : la surface réelle est imparfaite. On lui
  **associe un élément idéal** (un plan, un axe) — c'est cet élément idéal qui est la **référence**. En
  contrôle, c'est par exemple le marbre sur lequel la pièce repose.
- **Une référence peut être commune** : deux portées d'arbre A et B qui travaillent ensemble définissent un
  **seul axe** commun, noté **A-B** dans le cadre. On tolérance alors un battement par rapport à l'axe
  réel de rotation de l'arbre, et non par rapport à une seule portée.
- **Un système de références A | B | C** suit l'ordre de mise en position (fiche 6.3 : 3 + 2 + 1 points) :
  l'ordre change ce qu'on mesure.
- **Sur une surface brute** (pièce moulée, forgée), on ne prend pas toute la surface : on désigne quelques
  zones de contact, les **cibles de référence**, pour que la mise en position soit répétable.''',
  '''- **On ne mesure jamais « par rapport à une surface »** : pose la pièce sur le marbre ; sa face bosselée
  ne le touche que par ses bosses les plus hautes. Le plan parfait du marbre — qui **matérialise** la
  référence — c'est la référence A, pas la surface bosselée elle-même. On **associe** à la surface réelle un
  **élément idéal** (un plan, un axe) : c'est lui, la **référence**.
- **Une référence peut être commune** : un arbre tourne sur deux roulements, posés sur les portées A et B ;
  son axe de rotation passe par les deux centres à la fois. On le note **A-B** dans le cadre : un **seul
  axe** commun, qui représente l'axe de rotation de l'arbre dans ses paliers. En contrôle, on pose l'arbre
  sur deux vés, un sous chaque portée.
- **Un système de références A | B | C** suit l'ordre de mise en position (fiche 2.3 : 3 + 2 + 1 points) :
  plaque posée d'abord à plat sur A (3 points), puis poussée contre B (2 points) et C (1 point), elle est
  bien assise. Dans l'autre ordre, elle peut rester légèrement basculée : les cotes mesurées changent.
- **Sur une surface brute** (pièce moulée, forgée), on ne prend pas toute la surface : on désigne quelques
  zones de contact, les **cibles de référence** — comme un tabouret à 3 pieds, qui ne boite jamais sur un
  sol inégal —, pour que la mise en position soit répétable.''')

R('''1. **Croire que Ⓜ relâche la fonction** : il ne tolère que ce qui s'assemble encore. Le calibre le
   prouve.''', '''1. **Croire que Ⓜ relâche la fonction** : il n'accepte que ce qui passe le calibre. Et la taille du
   trou reste contrôlée à part.''')
R('''6. **Oublier Ⓟ pour un goujon** : le trou taraudé est conforme, l'assemblage coince plus haut.''',
  '''6. **Oublier Ⓟ pour un goujon** : le trou taraudé est conforme, mais l'axe sort de sa tolérance plus
   haut, dans la pièce assemblée.''')
R('''7. **Contrôler une pièce mince posée sur la table** quand le plan prévoit l'état maintenu : on mesure sa
   déformation, pas sa géométrie.''', '''7. **Contrôler une pièce mince posée sur la table** quand le plan porte ISO 10579-NR : on mesure sa
   déformation, pas sa géométrie.''')

R('''- Par défaut : **indépendance** (ISO 8015). Ⓔ, Ⓜ, Ⓛ sont des **exceptions déclarées**.''',
  '''- Par défaut : **indépendance** (ISO 8015). Ⓔ, Ⓜ, Ⓛ sont des **exceptions déclarées** (ils lient
  taille et géométrie) ; Ⓟ déplace la zone, Ⓕ fixe l'état de contrôle.''')
R('''- **Ⓜ** : t disponible = t + écart au maximum de matière (trou : D réel − D min). Le **calibre** (broches
  à la taille virtuelle D min − t, aux positions exactes) en donne le sens physique.''',
  '''- **Ⓜ** : t disponible = t + écart au maximum de matière (trou : D réel − D min). **Le bonus n'est pas un
  cadeau : c'est le jeu que la pièce apporte elle-même.** Le **calibre** (broches à la taille virtuelle
  D min − t, aux positions exactes) en donne le sens physique. Pour un arbre, le calibre est une **bague**
  de diamètre d max + t.''')
R('''- **Ⓛ** : même logique pour garantir une **matière minimale** (paroi, surépaisseur).
- **Ⓟ** + longueur encadrée : la zone est **projetée** là où passe la pièce suivante (goujons, vis).
- **Ⓕ** : tolérance à l'**état libre** ; sinon, pièce non rigide contrôlée **maintenue** (ISO 10579).''',
  '''- **Ⓛ** : même paroi garantie au pire cas, avec un bonus pour les trous plus petits.
- **Ⓟ** + longueur de projection : la zone est **projetée** là où passe la pièce suivante (goujons, vis).
- Par défaut, contrôle à l'**état libre** (pièce rigide). Plan marqué **ISO 10579-NR** : pièce non rigide
  contrôlée **maintenue** ; **Ⓕ** marque ce qui reste à l'état libre.''')

# formules
R('''**Taille virtuelle (calibre)** — trou : D min − t · arbre : d max + t''',
  '''**Taille virtuelle (calibre)** — trou : broche D min − t · arbre : bague d max + t''')
R('''**Zone projetée Ⓟ** — la zone s'applique au-dessus de la surface, sur la longueur encadrée qui suit Ⓟ''',
  '''**Zone projetée Ⓟ** — la zone s'applique au-dessus de la surface, sur la longueur de projection qui suit Ⓟ
(ex. ⊥ Ø0,1 Ⓟ 40 A)''')
R('''**Normes** — ISO 8015 (indépendance) · ISO 2692 (Ⓜ, Ⓛ) · ISO 1101 (Ⓟ) · ISO 10579 (Ⓕ) · ISO 5459 (références)''',
  '''**Normes** — ISO 8015 (indépendance, pièce rigide) · ISO 2692 (Ⓜ, Ⓛ) · ISO 1101 (Ⓟ) · ISO 10579 (pièces non
rigides, Ⓕ) · ISO 5459 (références)''')

# exemple / exercice / corrigé : A B → A B C
R('''localisés **⌖ Ø0,3 A B**, **sans Ⓜ**''', '''localisés **⌖ Ø0,3 A B C**, **sans Ⓜ**''')
R('''on cote **⌖ Ø0,3 Ⓜ A B**.''', '''on cote **⌖ Ø0,3 Ⓜ A B C**.''')
R('''aux positions exactes) : rapide, sans calcul, et il garantit que les vis passeront.''',
  '''aux positions exactes) : rapide, sans calcul, et il garantit que les vis passeront, si la pièce en face
respecte sa propre tolérance. La taille des trous reste contrôlée à part (9,00 à 9,22).''')
R('''cotée **⌖ Ø0,4 Ⓜ A B**.

**1.**''', '''cotée **⌖ Ø0,4 Ⓜ A B C** (A : face d'appui ; B, C : deux chants, qui fixent x et y).

**1.**''')
R('''20 mm). Quel modificateur faut-il sur la perpendicularité de ce taraudage, et pourquoi ?''',
  '''20 mm). Quel modificateur faut-il sur la perpendicularité de ce taraudage (référence A : face d'appui du
bâti), et pourquoi ?''')
R('''**6.** On veut aussi garantir une paroi minimale entre un des trous et le bord de la platine. Quel
modificateur exprime ce besoin ?''',
  '''**6.** On veut aussi garantir une paroi minimale entre un des trous et le bord de la platine, en
acceptant les trous plus petits un peu plus décalés. Quel modificateur traduit ce besoin ?''')
R('''**3.** e = √(0,0625 + 0,0225) = √0,085 ≈ 0,292 mm ; zone occupée 2e ≈ **Ø0,583**.''',
  '''**3.** e = √(0,0625 + 0,0225) = √0,085 ≈ 0,292 mm ; plus petite zone contenant le centre : 2e ≈ **Ø0,583**.''')
R('''**5.** **Ⓟ**, suivi de la longueur encadrée **20** (épaisseur de la platine) : le goujon prolonge
l'inclinaison du taraudage ; c'est dans le trou de la platine que l'écart compte.''',
  '''**5.** **Ⓟ**, suivi de la longueur de projection **20** (épaisseur de la platine) : **⊥ Ø… Ⓟ 20 A**. Le
goujon prolonge l'inclinaison du taraudage ; c'est dans le trou de la platine que l'écart compte.''')
R('''**6.** **Ⓛ** (minimum de matière) : le risque n'est pas que ça ne passe pas, mais qu'il ne reste pas
assez de matière. Le pire cas est le trou au plus grand et décalé vers le bord.''',
  '''**6.** **Ⓛ** (minimum de matière) : le risque n'est pas que ça ne passe pas, mais qu'il ne reste pas
assez de matière. La paroi est garantie au pire cas (trou au plus grand, décalé vers le bord) ; Ⓛ accorde
un bonus de position aux trous plus petits, qui laissent plus de métal.''')
R('''"Trou Ø11 H13 (11,00 à 11,27), ⌖ Ø0,4 Ⓜ. Mesuré Ø11,12''', '''"Trou Ø11 H13 (11,00 à 11,27), ⌖ Ø0,4 Ⓜ A B C. Mesuré Ø11,12''')

# ateliers
R('''9,22 mm, ISO 286). Leur position est cotée ⌖ Ø0,3 Ⓜ A B. Un trou''',
  '''9,22 mm, ISO 286). Leur position est cotée ⌖ Ø0,3 Ⓜ A B C (A : face d'appui ; B, C : deux chants). Un trou''')
R('''"pieges": [(9.22, "9,22 mm, c'est le trou au plus GRAND : le minimum de matière. Un trou "
                               "contient le plus de métal autour de lui quand il est au plus petit.")],''',
  '''"pieges": [(9.22, "9,22 mm, c'est le trou au plus GRAND : la plaque a alors le MOINS de métal "
                               "autour. Le maximum de matière d'un trou, c'est son plus petit diamètre.")],''')
R('''{"type": "numerique", "label": "Zone occupée par le centre",
             "unite": "mm", "attendu": 0.4327, "tol": 0.003,
             "consigne": "Calcule la zone occupée : 2 × √(Δx² + Δy²).",''',
  '''{"type": "numerique", "label": "Plus petite zone contenant le centre",
             "unite": "mm", "attendu": 0.4327, "tol": 0.008,
             "consigne": "Calcule le diamètre de la plus petite zone, centrée sur la position exacte, qui "
                         "contient le centre du trou : 2 × √(Δx² + Δy²).",''')
R('''"enonce": "Un taraudage de 12 mm de profondeur reçoit un goujon qui traverse une bride de 40 mm "
                  "d'épaisseur. Sa perpendicularité est cotée Ø0,1. Mesure''',
  '''"enonce": "Un taraudage de 12 mm de profondeur reçoit un goujon qui traverse une bride de 40 mm "
                  "d'épaisseur. Sa perpendicularité est cotée Ø0,1 par rapport à A (face d'appui du carter). Mesure''')
R('''"options": ["Perpendicularité Ø0,1 Ⓟ suivie de la longueur encadrée 40",
                         "Perpendicularité Ø0,1 Ⓜ", "Perpendicularité Ø0,1 Ⓕ"], "bonne": 0,''',
  '''"options": ["⊥ Ø0,1 Ⓟ 40 A : zone projetée sur 40 mm",
                         "⊥ Ø0,1 Ⓜ A", "⊥ Ø0,1 Ⓕ A"], "bonne": 0,''')
R('''("État libre Ⓕ",
             "la pièce non rigide contrôlée sans être maintenue (ISO 10579)."),''',
  '''("État libre Ⓕ",
             "sur un plan marqué ISO 10579-NR (pièce non rigide contrôlée maintenue), Ⓕ signale une "
             "tolérance à vérifier sur la pièce libre."),''')
R('''"question": "Une bague d'étanchéité mince s'ovalise posée sur la table et redevient ronde montée. "
                         "Quel symbole permet de limiter son ovalisation telle qu'elle est livrée, avant montage ?",''',
  '''"question": "Une bague d'étanchéité mince, sur un plan marqué ISO 10579-NR, se déforme posée sur la "
                         "table et redevient ronde montée. Quel symbole permet de limiter sa circularité telle "
                         "qu'elle est livrée, avant montage ?",''')
R('''"question": "Un trou est percé près d'un bord ; il doit rester au moins une épaisseur de paroi. "
                         "Quel modificateur sur sa localisation ?",''',
  '''"question": "Un trou est percé près d'un bord ; il doit rester au moins une épaisseur de paroi. Quel "
                         "modificateur traduit exactement ce besoin, en acceptant les trous plus petits plus "
                         "décalés ?",''')
R('''2: "L'indépendance ne lie pas le diamètre et la position : un trou au plus "
                                "grand ET décalé vers le bord pourrait percer la paroi."}},''',
  '''2: "L'indépendance garantit aussi la paroi (la zone vaut pour tous les "
                                "diamètres), mais elle rebute des trous plus petits qui pourraient être plus "
                                "décalés sans danger. Ⓛ leur accorde ce bonus, comme Ⓜ pour un assemblage."}},''')
R('''"calcul": "**0,048 mm** dans le taraudage (conforme sans Ⓟ) ; **0,16 mm** sur la bride (hors "
                     "Ø0,1) → **⊥ Ø0,1 Ⓟ 40**.",''',
  '''"calcul": "**0,048 mm** dans le taraudage (conforme sans Ⓟ) ; **0,16 mm** sur la bride (hors "
                     "Ø0,1) → **⊥ Ø0,1 Ⓟ 40 A**.",''')
R('''"regle": "**Ⓟ + longueur encadrée** : la zone s'applique au-dessus de la surface. **Ⓕ** : "
                    "tolérance à l'état libre. **Ⓛ** : garantir une matière minimale.",''',
  '''"regle": "**Ⓟ + longueur de projection** : la zone s'applique au-dessus de la surface. **Ⓕ** : "
                    "tolérance à l'état libre (plan ISO 10579-NR). **Ⓛ** : garantir une matière minimale.",''')
R('''"verification": "Plus la pièce assemblée est épaisse, plus l'écart projeté grandit pour la même "
                            "inclinaison : c'est pourquoi la longueur encadrée après Ⓟ est l'épaisseur de "
                            "la pièce traversée.",''',
  '''"verification": "Plus la pièce assemblée est épaisse, plus l'écart projeté grandit pour la même "
                            "inclinaison : c'est pourquoi la longueur de projection après Ⓟ est l'épaisseur "
                            "de la pièce traversée.",''')
R('''"calcul": "**D min = 9,00** ; **t disponible = Ø0,45** ; **2e ≈ 0,433** → conforme''',
  '''"calcul": "**D min = 9,00** ; **t disponible = Ø0,45** ; **2e ≈ 0,433** → conforme''')

# générateur et quiz
R('''f"{fr(d + it13, 2)} mm). Leur position est cotée **⌖ Ø{fr(t, 1)} Ⓜ A B**.''',
  '''f"{fr(d + it13, 2)} mm). Leur position est cotée **⌖ Ø{fr(t, 1)} Ⓜ A B C**.''')
R('''    bonus = min(bonus, it13)\n''', '')
R('''["Un trou de passage de vis", "Un trou de pion libre", "Un alésage de centrage d'un roulement",''',
  '''["Un trou de passage de vis", "Un trou de passage de goujon", "Un alésage de centrage d'un roulement",''')
R('''["Ⓜ", "Ⓟ suivi de la longueur encadrée", "Ⓔ", "Ⓕ"], 1,
     "La zone projetée Ⓟ, suivie d'une longueur encadrée (l'épaisseur de la bride)''',
  '''["Ⓜ", "Ⓟ suivi de la longueur de projection", "Ⓔ", "Ⓕ"], 1,
     "La zone projetée Ⓟ, suivie de la longueur de projection (l'épaisseur de la bride)''')
R('''     "Le pire cas pour la paroi est le trou au plus grand (minimum de matière) et décalé vers le bord. Ⓛ "
     "lie la tolérance de position à cet état.", "Intermédiaire"),''',
  '''     "Le pire cas pour la paroi est le trou au plus grand (minimum de matière) et décalé vers le bord : "
     "Ⓛ garantit la paroi à ce pire cas et accorde un bonus aux trous plus petits.", "Intermédiaire"),''')
R('''("Pour garantir une épaisseur de paroi minimale entre un trou et le bord d'une pièce, on utilise :",''',
  '''("Pour garantir une paroi minimale entre un trou et le bord d'une pièce tout en acceptant les trous "
     "plus petits plus décalés, on utilise :",''')

assert "zone occupée" not in c.replace("Zone occupée", ""), [m.start() for m in re.finditer("zone occupée", c)]
import sys; [print("ENCADREE:", l) for l in c.split("FICHE_2_4")[1].splitlines() if "encadrée" in l]
open(F, 'w', encoding='utf-8').write(c)
print("corrigé")
