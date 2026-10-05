# -*- coding: utf-8 -*-
# Corrections du brouillon 6.22 après relecture (relecteur-bts-meca B1-B6 + améliorations ;
# prof-pedagogue B1-B4 + améliorations). Huile alignée sur la fiche 8.9 : 850 kg/m³ (donnée d'énoncé).
import os
ICI = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(ICI, 'brouillon_6_22.py')
c = open(F, encoding='utf-8').read()


def R(a, b, n=1):
    global c
    assert c.count(a) == n, (a[:80], c.count(a))
    c = c.replace(a, b)


def remplacer_fonction(nom, nouveau):
    global c
    i = c.index(f"def {nom}(")
    j = c.index("\ndef ", i + 5)
    c = c[:i] + nouveau.strip("\n") + "\n\n" + c[j:]


# ---------------------------------------------------------------- figures
# hydrostatique : flèches vers le point, flèches verticales, vase évasé
R('''        p.append(_k_fl(x0 + 70 + lg, y, x0 + 70, y, ALERTE, "kr", 2))
        p.append(_k_fl(x0 + 190 - lg, y, x0 + 190, y, ALERTE, "kr", 2))''',
  '''        p.append(_k_fl(x0 + 126 - lg, y, x0 + 124, y, ALERTE, "kr", 2))
        p.append(_k_fl(x0 + 134 + lg, y, x0 + 136, y, ALERTE, "kr", 2))
        if i == 1:
            p.append(_k_fl(x0 + 130, y - 8 - lg * 0.8, x0 + 130, y - 6, ALERTE, "kr", 2))
            p.append(_k_fl(x0 + 130, y + 8 + lg * 0.8, x0 + 130, y + 6, ALERTE, "kr", 2))
            p.append(_txt(x0 + 190, y + 4, "même pression dans", 9, ALERTE, "start"))
            p.append(_txt(x0 + 190, y + 15, "toutes les directions", 9, ALERTE, "start"))''')
R('''    p.append(_txt(x0 + 130, y0 + H + 18, "flèches rouges : la pression grandit avec la profondeur", 10, ALERTE, "middle"))''',
  '''    p.append(_txt(x0 + 130, y0 + H + 18, "flèches rouges : la pression sur le point grandit avec la profondeur", 10, ALERTE, "middle"))''')
R('''    formes = ((x1 + 20, 50), (x1 + 120, 20), (x1 + 210, 90))
    p.append(f"<rect x='{x1 + 10}' y='{yb}' width='330' height='26' fill='#dbeafe' stroke='{TRAIT}' stroke-width='2'/>")
    for xv, w in formes:
        p.append(f"<rect x='{xv}' y='{ys}' width='{w}' height='{yb - ys}' fill='#dbeafe' stroke='{TRAIT}' stroke-width='2'/>")''',
  '''    p.append(f"<rect x='{x1 + 10}' y='{yb}' width='330' height='26' fill='#dbeafe' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<rect x='{x1 + 30}' y='{ys}' width='30' height='{yb - ys}' fill='#dbeafe' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<polygon points='{x1 + 120},{yb} {x1 + 150},{yb} {x1 + 200},{ys} {x1 + 70},{ys}' fill='#dbeafe' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<polygon points='{x1 + 240},{yb} {x1 + 330},{yb} {x1 + 300},{ys} {x1 + 270},{ys}' fill='#dbeafe' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(_txt(x1 + 45, ys + 60, "étroit", 9, FIN, "middle"))
    p.append(_txt(x1 + 135, ys + 60, "évasé", 9, FIN, "middle"))
    p.append(_txt(x1 + 285, ys + 60, "rétréci", 9, FIN, "middle"))''')
# presse : animation à l'échelle, charge, c1/c2, surfaces
R('''    p.append(f"<g><animateTransform attributeName='transform' type='translate' values='0,0; 0,-6; 0,0' dur='3s' repeatCount='indefinite'/>"''',
  '''    p.append(f"<g><animateTransform attributeName='transform' type='translate' values='0,0; 0,-2; 0,0' dur='3s' repeatCount='indefinite'/>"''')
R('''    p.append(_txt(400, 44, "F2 (grande)", 11, OK, "middle", True))''',
  '''    p.append(_txt(400, 44, "F2 (grande)", 11, OK, "middle", True))
    p.append(_txt(64, ya + 30, "c1", 11, ALERTE, "end", True))
    p.append(_txt(290, ya + 6, "c2 (petite)", 10, OK, "end", True))''')
R('''                                   ("→ F2 = F1 × S2 / S1", OK, True), ("", TRAIT, False),''',
  '''                                   ("→ F2 = F1 × S2 / S1", OK, True),
                                   ("S = π D²/4 : D × 10 → S × 100", FIN, False),''')
# paroi : diagramme côté eau, flèches vers la paroi, résultante fléchée
R('''    # triangle de pression côté extérieur de la paroi (dessiné à gauche)
    p.append(f"<polygon points='{x0},{y0} {x0},{y0 + H} {x0 - 110},{y0 + H}' fill='#fecaca' stroke='{ALERTE}' stroke-width='1.4'/>")
    for k in range(1, 6):
        y = y0 + H * k / 5
        lg = 110 * k / 5
        p.append(_k_fl(x0 - lg, y, x0 - 2, y, ALERTE, "kr", 1.4))
    p.append(_txt(20, y0 + H + 22, "p = ρ g h : nulle en surface, maximale au fond", 10, ALERTE, "start"))
    # résultante
    yr = y0 + H * 2 / 3
    p.append(f"<line x1='{x0 + 2}' y1='{yr}' x2='{x0 + 70}' y2='{yr}' stroke='{OK}' stroke-width='4'>"
             "<animate attributeName='stroke-width' values='3;6;3' dur='1.6s' repeatCount='indefinite'/></line>")
    p.append(_txt(x0 + 76, yr + 4, "F résultante", 11, OK, "start", True))''',
  '''    # diagramme de pression côté eau : l'eau pousse la paroi vers l'extérieur (vers la gauche)
    p.append(f"<polygon points='{x0},{y0} {x0},{y0 + H} {x0 + 110},{y0 + H}' fill='#fecaca' stroke='{ALERTE}' stroke-width='1.4' opacity='0.8'/>")
    for k in range(1, 6):
        y = y0 + H * k / 5
        lg = 110 * k / 5
        p.append(_k_fl(x0 + lg, y, x0 + 3, y, ALERTE, "kr", 1.4))
    p.append(_txt(x0 + 60, y0 + 40, "pression de l'eau", 10, ALERTE, "start", True))
    p.append(_txt(x0 + 60, y0 + 52, "sur la paroi", 10, ALERTE, "start", True))
    p.append(_txt(20, y0 + H + 22, "p = ρ g h : nulle en surface, maximale au fond", 10, ALERTE, "start"))
    # résultante : vers l'extérieur de la cuve
    yr = y0 + H * 2 / 3
    p.append(_k_fl(x0, yr, x0 - 80, yr, OK, "kg", 4))
    p.append(_txt(x0 - 84, yr - 8, "F résultante", 11, OK, "end", True))''')
R('''                                   ("F = ρ g h × S = poids de l'eau au-dessus", OK, True), ("", TRAIT, False),''',
  '''                                   ("F = ρ g h × S (= poids de l'eau si", OK, True),
                                   ("parois verticales)", OK, True),''')
# archimède : une seule échelle, flotteur immergé à 20 %, blocs au fond
R('''    blocs = ((x0 + 50, "ACIER 1 L", "#94a3b8", 77, 9.81, False), (x0 + 200, "ALUMINIUM 1 L", "#cbd5e1", 26.5, 9.81, False),
             (x0 + 350, "FLOTTEUR 10 L, 2 kg", "#fde68a", 19.6, 19.6, True))
    for xb, nom, col, poids, pa, flotte in blocs:
        yb = y0 + 25 if flotte else y0 + 110
        hb = 70 if flotte else 50''',
  '''    blocs = ((x0 + 50, "ACIER 1 L (au fond)", "#94a3b8", 77, 9.81, False), (x0 + 200, "ALUMINIUM 1 L (au fond)", "#cbd5e1", 26.5, 9.81, False),
             (x0 + 350, "FLOTTEUR 10 L, 2 kg", "#fde68a", 19.6, 19.6, True))
    for xb, nom, col, poids, pa, flotte in blocs:
        yb = y0 - 16 if flotte else y0 + 150
        hb = 70 if flotte else 50''')
R('''        p.append(_k_fl(xb + 18, yb + hb / 2, xb + 18, yb + hb / 2 + min(70, poids * 0.9), ALERTE, "kr", 2.2))
        p.append(_k_fl(xb + 42, yb + hb / 2, xb + 42, yb + hb / 2 - min(70, pa * 2.5), OK, "kg", 2.2))''',
  '''        p.append(_k_fl(xb + 18, yb + hb / 2, xb + 18, yb + hb / 2 + min(48, poids * 1.6), ALERTE, "kr", 2.2))
        p.append(_k_fl(xb + 42, yb + hb / 2, xb + 42, yb + hb / 2 - min(48, pa * 1.6), OK, "kg", 2.2))
        if poids * 1.6 > 48:
            p.append(_txt(xb + 4, yb + hb / 2 + 40, "77 N (flèche coupée)", 8, ALERTE, "end"))''')
R('''    p.append(_txt(x0 + 414, y0 + 62, "immergé", 9, FIN, "start"))
    p.append(_txt(x0 + 414, y0 + 74, "à 20 %", 9, FIN, "start"))''',
  '''    p.append(_txt(x0 + 414, y0 + 38, "immergé", 9, FIN, "start"))
    p.append(_txt(x0 + 414, y0 + 50, "à 20 %", 9, FIN, "start"))''')
R('''    p.append(f"<rect x='{x0}' y='{y0 + 40}' width='{W}' height='{H - 40}' fill='#dbeafe'/>")''',
  '''    p.append(f"<rect x='{x0}' y='{y0 + 40}' width='{W}' height='{H - 40}' fill='#dbeafe'/>")
    p.append(f"<line x1='{x0}' y1='{y0 + H}' x2='{x0 + W}' y2='{y0 + H}' stroke='{TRAIT}' stroke-width='2'/>")''')
R('''                                   ("au centre du volume immergé", TRAIT, False), ("", TRAIT, False),''',
  '''                                   ("au centre de carène (centre du", TRAIT, False),
                                   ("volume immergé)", TRAIT, False),''')
R('''                                   ("même poussée (9,81 N), poids", TRAIT, False),
                                   ("différents : les deux coulent.", TRAIT, False), ("", TRAIT, False),''',
  '''                                   ("même poussée (9,81 N), poids", TRAIT, False),
                                   ("différents : les deux coulent.", TRAIT, False),''')
# stabilité : métacentre dessiné, écart G-C plus visible, libellés
remplacer_fonction("stabilite_flottant", '''
def stabilite_flottant():
    p = [_k_defs(), _txt(30, 24, "Stabilité d'un flotteur : G sous le métacentre M, le couple redresse", 13, TRAIT, "start", True)]
    for x0, titre, ok in ((30, "STABLE : G sous M", True), (410, "INSTABLE : G au-dessus de M", False)):
        p.append(f"<rect x='{x0}' y='40' width='360' height='250' rx='8' fill='#ffffff' stroke='{OK if ok else ALERTE}' stroke-width='2'/>")
        p.append(_txt(x0 + 180, 62, titre, 11, OK if ok else ALERTE, "middle", True))
        cx, cy = x0 + 180, 170
        p.append(f"<rect x='{x0 + 10}' y='{cy}' width='340' height='96' fill='#dbeafe'/>")
        p.append(_txt(x0 + 18, cy + 88, "eau", 10, ALESAGE, "start", True))
        p.append(f"<g transform='rotate(-20 {cx} {cy})'><rect x='{cx - 70}' y='{cy - 40}' width='140' height='80' fill='#fde68a' stroke='{TRAIT}' stroke-width='2'/>"
                 f"<line x1='{cx}' y1='{cy - 120}' x2='{cx}' y2='{cy + 40}' stroke='{FIN}' stroke-dasharray='4 3'/>"
                 + (f"<rect x='{cx - 60}' y='{cy + 18}' width='120' height='18' fill='{FIN}'/>" if ok else
                    f"<rect x='{cx - 30}' y='{cy - 92}' width='60' height='52' fill='{FIN}'/>")
                 + "</g>")
        p.append(_txt(cx + 70, cy - 52, "flotteur", 10, TRAIT, "start", True))
        p.append(_txt(cx + 38, cy + 30 if ok else cy - 76, "lest" if ok else "charge haute", 10, "#ffffff" if ok else TRAIT, "start", True))
        # métacentre : sur l'axe de symétrie incliné, au-dessus de C
        a = math.radians(-20)
        yb_ = 14 if ok else -46
        gx, gy = cx - yb_ * math.sin(a), cy + yb_ * math.cos(a)
        ym = -22
        mx, my = cx - ym * math.sin(a), cy + ym * math.cos(a)
        xc = mx   # la poussée, verticale, passe par M
        p.append(f"<line x1='{xc:.1f}' y1='{cy + 22}' x2='{xc:.1f}' y2='{my:.1f}' stroke='{OK}' stroke-dasharray='3 3'/>")
        p.append(f"<circle cx='{xc:.1f}' cy='{cy + 22}' r='5' fill='{OK}'/>")
        p.append(_txt(xc - 8, cy + 38, "C", 11, OK, "end", True))
        p.append(_k_fl(xc, cy + 22, xc, cy - 10, OK, "kg", 2.2))
        p.append(f"<circle cx='{mx:.1f}' cy='{my:.1f}' r='4' fill='{ALESAGE}'/>")
        p.append(_txt(mx - 8, my - 4, "M", 11, ALESAGE, "end", True))
        p.append(f"<circle cx='{gx:.1f}' cy='{gy:.1f}' r='5' fill='{ALERTE}'/>")
        p.append(_txt(gx + 8, gy - 6, "G", 11, ALERTE, "start", True))
        p.append(_k_fl(gx, gy, gx, gy + 44, ALERTE, "kr", 2.2))
        p.append(_txt(x0 + 180, 282, ("poids et poussée forment un couple qui redresse" if ok else "poids et poussée forment un couple qui fait chavirer"), 10, TRAIT, "middle", True))
    p.append(f"<rect x='30' y='300' width='740' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 322, "C : centre de carène (volume immergé), décalé vers le côté qui s'enfonce. M : où la poussée coupe l'axe du flotteur.", 11, TRAIT))
    return _svg("".join(p), 800, 346)
''')

# ---------------------------------------------------------------- cours
R('''> **p = p0 + ρ × g × h**
> p0 : pression à la surface libre (Pa) ; ρ : masse volumique du fluide (kg/m³) ; h : profondeur (m)''',
  '''> **p = p0 + ρ × g × h**
> p0 : pression à la surface libre (Pa) ; ρ : masse volumique du fluide (kg/m³) ; g : accélération de la
> pesanteur, 9,81 m/s² ; h : profondeur sous la surface libre, comptée vers le bas (m) ; p en Pa.
> En pression relative (comptée à partir de la pression atmosphérique), p0 = 0 et il reste p = ρ g h.''')
R('''- elle **pousse perpendiculairement** à toute surface en contact (paroi, piston, fond) ;
- en un point donné, elle a **la même valeur dans toutes les directions**.''',
  '''- elle **pousse perpendiculairement** à toute surface en contact (paroi, piston, fond) ;
- en un point donné, elle a **la même valeur dans toutes les directions**.

*Percez une bouteille d'eau de trois trous l'un au-dessus de l'autre : l'eau jaillit perpendiculairement à
la paroi, et le jet du bas va plus loin que celui du haut. En plongée, la pression pince les oreilles de la
même façon, tête droite ou penchée.*''')
R('''- **Même profondeur, même pression**, quelle que soit la forme du récipient : c'est le principe des **vases
  communicants** (le niveau s'égalise) et du **niveau à eau** des maçons.''',
  '''- **Même profondeur, même pression**, quelle que soit la forme du récipient : c'est le principe des **vases
  communicants** (le niveau s'égalise) et du **niveau à eau** des maçons (un tuyau transparent rempli d'eau
  dont les deux bouts affichent le même niveau). *Pourquoi la forme ne compte pas : dans la démonstration,
  la colonne ne porte que l'eau située juste au-dessus d'elle ; dans un vase évasé, l'eau « en trop » sur
  les côtés est portée par les parois inclinées, pas par le fond.*''')
R('''- **Dans un circuit hydraulique, on néglige ρ g h.** *Exemple (huile de masse volumique 870 kg/m³, donnée
  d'énoncé) : 1 m de dénivelé donne 870 × 9,81 × 1 ≈ 8 500 Pa ≈ 0,085 bar, à comparer aux 100 bar d'un
  circuit (donnée d'énoncé) : moins de 0,1 %.*''',
  '''- **Dans un circuit hydraulique, on néglige ρ g h.** *Exemple (huile de masse volumique 850 kg/m³, donnée
  d'énoncé, la même qu'en fiche 8.9) : 1 m de dénivelé donne 850 × 9,81 × 1 ≈ 8 340 Pa ≈ 0,083 bar, à comparer
  aux 100 bar d'un circuit (donnée d'énoncé) : moins de 0,1 %.*''')
R('''Appuyez sur un piston qui ferme un circuit plein d'huile : la pression monte de la même quantité partout,
jusqu'au piston le plus lointain. C'est ce qui permet de commander un effort à distance par un simple
tuyau.''',
  '''**D'où il vient.** De la loi précédente : p = p0 + ρ g h. Si l'on appuie sur le piston, p0 augmente, par
exemple de 10 bar. Le fluide, **incompressible** (on ne peut pas réduire son volume en appuyant, contrairement
à l'air d'une pompe à vélo dont on bouche la sortie), ne bouge pratiquement pas : ρ g h ne change pas, et p
augmente de 10 bar en chaque point. *Image : une seringue pleine ou un tube de dentifrice — on appuie à un
bout, ça pousse à l'autre.* C'est ce qui permet de commander un effort à distance par un simple tuyau.''')
R('''> p = F1 / S1 = F2 / S2  →  **F2 = F1 × S2 / S1**

*Exemple (données d'énoncé) :''',
  '''> p = F1 / S1 = F2 / S2  →  **F2 = F1 × S2 / S1**

**Pourquoi la grande surface donne la grande force.** La pression, c'est la force portée par chaque mm². La
pression étant la même partout, chaque mm² du grand piston est poussé exactement comme chaque mm² du petit :
un piston qui a 100 fois plus de mm² reçoit 100 fois plus de force — comme 100 petits pistons côte à côte.

**Pourquoi le carré des diamètres.** S = π D² / 4 : dans le rapport S2 / S1, le π / 4 se simplifie, et
S2 / S1 = (D2 / D1)². *Une plaque carrée de 10 mm de côté, puis une de 20 mm : le côté double, mais il faut 4
petites plaques pour couvrir la grande.* Un piston 10 fois plus large a 10 × 10 = 100 fois plus de surface.
La figure à curseurs ci-dessous le montre : le rapport des surfaces suit le carré du rapport des diamètres.

*Exemple (données d'énoncé) :''')
R('''**Rien n'est gratuit : la course.** L'huile est incompressible : le volume qui quitte le petit cylindre
entre dans le grand, **S1 × c1 = S2 × c2**. Si le petit piston descend de 100 mm, le grand monte de 100 /
100 = **1 mm**. Le travail est le même des deux côtés : F1 × c1 = 200 × 0,1 = 20 J = F2 × c2 = 20 000 ×
0,001 J. C'est le **effort × flux** de la fiche 6.20 : la presse échange de la force contre de la course,
comme un réducteur échange du couple contre de la vitesse.''',
  '''**Rien n'est gratuit : la course.** Le petit piston descend de sa course c1 : il chasse un cylindre d'huile
de section S1 et de hauteur c1, soit un volume S1 × c1. L'huile étant incompressible, ce volume s'étale sous
le grand piston, 100 fois plus large : il ne le soulève que d'une couche 100 fois plus mince,
**S1 × c1 = S2 × c2**. Si le petit piston descend de 100 mm, le grand monte de 100 / 100 = **1 mm**. *C'est
pour ça qu'on pompe une vingtaine de fois le levier d'un cric pour monter la voiture de quelques
centimètres.* Le travail est le même des deux côtés : F1 × c1 = 200 × 0,1 = 20 J, et F2 × c2 = 20 000 × 0,001
= 20 J.

C'est la logique **effort × flux** de la fiche 6.20 : côté petit piston, F1 × v1 ; côté grand piston, F2 ×
v2 ; côté huile, p × Qv, le même des deux côtés. Le grand piston va 100 fois moins vite : F2 peut être 100
fois plus grande pour la même puissance. La presse échange de la force contre de la course, comme un réducteur
échange du couple contre de la vitesse.''')
R('''**Le vérin.** Un vérin est la moitié d'une presse : la pompe (fiche 6.20) impose la pression, le piston la
transforme en force.

> **Sortie : F = p × S** (toute la surface du piston) · **Rentrée : F = p × (S − s)** (surface annulaire,
> la tige occupe s)''',
  '''**Le vérin.** Un vérin est la moitié d'une presse. La centrale envoie l'huile : la pompe fournit le
**débit** (fiche 6.20), la pression monte jusqu'à ce qu'il faut pour vaincre la charge (au plus le réglage
du limiteur de pression), et le piston la transforme en force.

> **Sortie : F = p × S** (toute la surface du piston) · **Rentrée : F = p × (S − s)** (surface annulaire :
> le disque du piston moins le disque de la tige, là où l'huile ne peut pas appuyer)
> L'autre chambre est reliée au réservoir (0 bar relatif) ; frottements des joints négligés.''')
R('''*Vis ou vérin (fiche 6.18) ? La vis-écrou donne une position précise et peut être irréversible ; le vérin''',
  '''*Vis ou vérin (fiche 6.18) ? Les deux obéissent à la même règle que la presse : la vis transforme beaucoup de
tours de manivelle en un petit avancement avec un gros effort ; le vérin, beaucoup d'huile pompée en une
petite course avec un gros effort. La vis-écrou donne une position précise et peut être irréversible ; le vérin''')
R('''> **F = ρ g h × S** — c'est exactement le poids du fluide au-dessus du fond.''',
  '''> **F = ρ g h × S** — le poids d'une colonne de fluide de base S et de hauteur h. Pour une cuve à parois
> verticales, c'est exactement le poids du fluide qu'elle contient ; pour un récipient évasé ou rétréci, non :
> l'effort sur le fond ne dépend que de h et de S, pas de la quantité de liquide.''')
R('''**Sur une paroi verticale** de hauteur h et de largeur L, la pression relative croît de 0 (surface) à ρ g h
(fond) : la répartition est **triangulaire**. La force totale vaut la pression moyenne × la surface :''',
  '''**Sur une paroi verticale** de hauteur h et de largeur L, la pression relative croît de 0 (surface) à ρ g h
(fond) : la répartition est **triangulaire**. *Découpez une paroi de 2 m en 4 bandes de 0,5 m : la pression au
milieu de chaque bande correspond aux profondeurs 0,25 ; 0,75 ; 1,25 ; 1,75 m, dont la moyenne est 1 m, soit
h / 2.* Comme la pression grandit régulièrement avec la profondeur, la force totale vaut la pression de
mi-hauteur × la surface :''')
R('''> **Tout corps immergé dans un fluide subit une poussée verticale, vers le haut, égale au poids du volume de
> fluide déplacé : Pa = ρ fluide × V immergé × g**, appliquée au centre du volume immergé (centre de poussée).

**D'où elle vient.** Les pressions sur le dessous d'un objet immergé sont plus fortes que sur le dessus (le
dessous est plus profond) : la différence pousse vers le haut. Elle vaut exactement le poids du fluide qui
occuperait la place de l'objet.''',
  '''> **Tout corps immergé dans un fluide subit une poussée verticale, vers le haut, égale au poids du volume de
> fluide déplacé : Pa = ρ fluide × V immergé × g**, appliquée au centre du volume immergé, appelé **centre de
> carène** C.

**D'où elle vient.** Les pressions sur le dessous d'un objet immergé sont plus fortes que sur le dessus (le
dessous est plus profond) : la différence pousse vers le haut. *Pourquoi elle vaut le poids du fluide
déplacé : imaginez à la place de l'objet un « bloc d'eau » de même forme. Il ne monte pas et ne descend pas :
l'eau autour le porte exactement, donc les pressions sur sa surface valent tout juste son poids. Remplacez ce
bloc d'eau par de l'acier ou de l'aluminium de même forme : l'eau autour ne « sait » pas ce qu'il y a dedans,
elle pousse exactement pareil. La poussée dépend de la place occupée, pas de ce qui l'occupe ; seul le poids
change, et c'est lui qui décide si l'objet coule.*''')
R('''2,7 × 9,81 ≈ 26,5 N pour l'aluminium (table des matériaux). Les deux coulent, mais le bloc d'aluminium
« pèse » dans l'eau 26,5 − 9,8 ≈ 16,7 N au lieu de 26,5 N.*''',
  '''2,7 × 9,81 ≈ 26,5 N pour l'aluminium (table des matériaux). Les deux coulent, mais le bloc d'aluminium
« pèse » dans l'eau 26,5 − 9,8 ≈ 16,7 N au lieu de 26,5 N : c'est son **poids apparent**, ce qu'indiquerait un
peson qui le tient sous l'eau.*''')
R('''**Stabilité d'un flotteur** (notion). Le poids s'applique en G, la poussée au centre de poussée C. Si le
flotteur s'incline, C se déplace (la forme immergée change). Si le couple formé par le poids et la poussée le
ramène, il est **stable** ; s'il l'incline davantage, il **chavire**. La limite se trouve avec le
**métacentre** : le point autour duquel la poussée semble pivoter pour de petites inclinaisons ; le flotteur
est stable si G est sous le métacentre. En pratique : abaisser G (lest en bas), élargir la flottaison.''',
  '''**Stabilité d'un flotteur.** *Pensez au canoë : assis, il est stable ; debout, vous chavirez. Ce qui compte,
c'est la hauteur de G.* Le poids s'applique en G, la poussée au centre de carène C. Inclinez un peu le
flotteur : la poussée reste verticale, mais elle se décale vers le côté qui s'enfonce, parce que c'est là
qu'il y a maintenant plus de volume immergé. Prolongez sa ligne d'action : elle coupe l'axe de symétrie du
flotteur en un point M, le **métacentre**. Si G est **sous** M, le poids tombe du côté relevé et le couple
redresse : le flotteur est **stable**. Si G est **au-dessus** de M, le couple aggrave l'inclinaison : il
**chavire**.

**Trouver le métacentre** (petites inclinaisons) : M est au-dessus de C, à la distance **CM = I / V**, avec V
le volume immergé (m³) et I le moment quadratique de la surface de flottaison autour de l'axe d'inclinaison
(m⁴). *Exemple (données d'énoncé) : ponton de 2 m × 1 m, de 400 kg, dans l'eau. V = 0,4 m³, donc enfoncement
0,4 / 2 = 0,2 m, et C à 0,1 m du fond. Pour une inclinaison autour du grand côté : I = 2 × 1³ / 12 ≈ 0,167 m⁴,
CM = 0,167 / 0,4 ≈ 0,42 m : M est à environ 0,52 m du fond. La charge doit garder G sous 0,52 m.* En pratique :
mettre le lourd en bas (lest, cales sous une charge), élargir la coque au niveau de l'eau (I augmente) —
un ponton large ou un catamaran chavirent difficilement.''')
R('''- Fond : **F = ρ g h S** (poids du fluide). Paroi verticale : **F = ρ g L h² / 2**, à **h/3** du fond.
- **Archimède : Pa = ρ fluide V immergé g** — le volume, pas la masse. Flottaison : poussée = poids.
  Stabilité : G sous le métacentre.''',
  '''- Fond : **F = ρ g h S** (poids du fluide si parois verticales). Paroi verticale : **F = ρ g L h² / 2**, à
  **h/3** du fond.
- **Archimède : Pa = ρ fluide V immergé g** — le volume, pas la masse. Flottaison : poussée = poids.
  Stabilité : G sous le métacentre M, avec **CM = I / V**.''')
R('''**Archimède** — Pa = ρ fluide × V immergé × g · flottaison : Pa = poids''',
  '''**Archimède** — Pa = ρ fluide × V immergé × g · flottaison : Pa = poids · métacentre : CM = I / V ; stable si
G sous M''')

# ---------------------------------------------------------------- cas industriel
R('''constructeur annonce 50 kN. À l'essai, avec la même pompe à main, l'opérateur n'obtient qu'environ 32 kN, et
le grand piston « remonte » lentement quand on relâche.''',
  '''constructeur annonce 50 kN. À l'essai, avec la même pompe à main, l'opérateur n'obtient qu'environ 32 kN, et
le grand piston recule lentement sous la charge quand on relâche.''')
R('''- de l'**air** dans le circuit : l'air est compressible, il « absorbe » une partie de la course du petit
  piston sans transmettre la pression (Pascal suppose un fluide incompressible) ;
- une **fuite** au joint du grand piston ou au clapet : la pression retombe, d'où le piston qui remonte.''',
  '''- de l'**air** dans le circuit : l'air est compressible, il se comprime comme un ressort ; à chaque coup de
  pompe, la course du petit piston sert à écraser la bulle au lieu de chasser de l'huile vers le grand piston,
  et la pompe n'arrive plus à faire monter la pression (le volume ne se conserve plus : S1 c1 = S2 c2 suppose
  un fluide incompressible). La presse devient « spongieuse » ;
- une **fuite** au joint du grand piston ou au clapet : la pression retombe, d'où le piston qui recule.''')
R('''**La correction.** Purge de l'air (actionner la pompe tête en bas, vis de purge ouverte), remplacement du
joint du grand piston''',
  '''**La correction.** Purge de l'air selon la notice du constructeur, remplacement du joint du grand piston''')

# ---------------------------------------------------------------- exercice / corrigé (huile 850)
R('''**2.** La charge à soulever pèse 5 000 kg (g = 9,81 m/s²). Le vérin, monté verticalement, la soulève en
sortie. Quelle pression minimale faut-il (frottements négligés) ?''',
  '''**2.** La charge à soulever pèse 5 000 kg (g = 9,81 m/s²). Le vérin, monté verticalement, la soulève en
sortie. Quelle pression minimale faut-il (frottements, poids du piston et de la tige négligés ; chambre côté
tige reliée au réservoir) ?''')
R('''de masse volumique **870 kg/m³** (donnée d'énoncé).''', '''de masse volumique **850 kg/m³** (donnée d'énoncé).''')
R('''S = π × 80² / 4 ; s = π × 45² / 4 ; F = 12 × S ; p min = m g / S ; p fond = 870 × 9,81 × 0,6 ;
F paroi = 870 × 9,81 × 0,8 × 0,6² / 2 ; V immergé = m / ρ huile.''',
  '''S = π × 80² / 4 ; s = π × 45² / 4 ; F = 12 × S ; p min = m g / S ; p fond = 850 × 9,81 × 0,6 ;
F paroi = 850 × 9,81 × 0,8 × 0,6² / 2 ; V immergé = m / ρ huile.''')
R('''**3.** p fond = 870 × 9,81 × 0,6 ≈ **5 121 Pa** (≈ 0,05 bar). F paroi = 870 × 9,81 × 0,8 × 0,36 / 2 ≈
**1 229 N**, appliquée à 0,6 / 3 = **0,2 m** au-dessus du fond.

**4.** Volume d'huile à déplacer : m / ρ = 0,2 / 870 ≈ 0,000230 m³ = 0,230 L ; fraction immergée 0,230 / 0,5 ≈
**46 %**.''',
  '''**3.** p fond = 850 × 9,81 × 0,6 ≈ **5 003 Pa** (≈ 0,05 bar). F paroi = 850 × 9,81 × 0,8 × 0,36 / 2 ≈
**1 201 N**, appliquée à 0,6 / 3 = **0,2 m** au-dessus du fond.

**4.** Volume d'huile à déplacer : m / ρ = 0,2 / 850 ≈ 0,000235 m³ = 0,235 L ; fraction immergée 0,235 / 0,5 ≈
**47 %**.''')

# ---------------------------------------------------------------- méthode
R('''    "**Vérifier** : pour un fond, F doit valoir le poids du fluide au-dessus ; pour une presse, F1 c1 = F2 c2.",''',
  '''    "**Vérifier** : pour un fond de cuve à parois verticales, F doit valoir le poids du fluide ; pour une "
    "presse, F1 c1 = F2 c2.",''')

# ---------------------------------------------------------------- ateliers
R('''             "consigne": "Calcule F2 = F1 × S2 / S1.",''', '''             "consigne": "Calcule F2 = F1 × S2 / S1 (garde p non arrondi, ou passe par le rapport des surfaces).",''')
R('''             "pieges": [(10, "10 L, c'est le volume total du flotteur : il ne coulerait que s'il pesait 10 kg.")],''',
  '''             "pieges": [(10, "10 L, c'est le volume total du flotteur : il ne coulerait que s'il pesait 10 kg."),
                        (0.002, "0,002 : c'est en m³ ; la réponse est demandée en litres (× 1 000).")],''')
R('''            ("Centre de poussée",
             "le point d'application de la résultante des pressions ; sur une paroi verticale, à h/3 du fond."),''',
  '''            ("Centre de poussée (paroi)",
             "le point d'application de la résultante des pressions sur une paroi ; paroi verticale : à h/3 du fond."),''')
R('''            "verification": "Le fond reçoit 19 620 × 4,5 = 88 290 N = poids des 9 m³ d'eau (9 000 × 9,81) : la loi "
                            "de l'hydrostatique est cohérente avec le poids.",''',
  '''            "verification": "Le fond reçoit 19 620 × 4,5 = 88 290 N = poids des 9 m³ d'eau (9 000 × 9,81), comme il "
                            "se doit pour une cuve à parois verticales.",''')

# ---------------------------------------------------------------- générateur et quiz
R('''        "rep": round(Pa, 3), "tol": max(0.05, Pa * 0.01), "unite": "N",''', '''        "rep": round(Pa, 3), "tol": max(0.005, Pa * 0.01), "unite": "N",''')
R('''        if abs(val - Pa) > max(0.05, Pa * 0.02) * 2 and all(abs(val - d["v"]) > 0.05 for d in diag):''',
  '''        if abs(val - Pa) > max(0.01, Pa * 0.02) * 2 and all(abs(val - d["v"]) > 0.01 for d in diag):''')
R('''      "Parce qu'il est très petit devant la pression de la pompe (quelques millièmes)", "Parce que l'huile est compressible"], 2,
     "Exemple : 1 m d'huile à 870 kg/m³ donne ≈ 0,085 bar, contre 100 bar dans le circuit : moins de 0,1 %.",''',
  '''      "Parce qu'il est très petit devant la pression du circuit (moins d'un millième)", "Parce que l'huile est compressible"], 2,
     "Exemple : 1 m d'huile à 850 kg/m³ donne ≈ 0,083 bar, contre 100 bar dans le circuit : moins de 0,1 %.",''')

open(F, 'w', encoding='utf-8').write(c)
print("corrigé")
