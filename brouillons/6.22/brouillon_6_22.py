# -*- coding: utf-8 -*-
# BROUILLON — fiche 6.22 « Statique des fluides : hydrostatique, Pascal, Archimède, poussée sur une paroi »
# (référentiel S3.2.7). Rien de ceci n'est encore dans app.py.
#
# Sources des valeurs utilisées :
# - eau : 1 000 kg/m³, valeur arrondie d'usage (validée par l'auteur) ;
# - acier 7 850 kg/m³, aluminium EN AW-6082 2 700 kg/m³ : table MATERIAUX de l'application ;
# - g = 9,81 m/s² ; 1 bar = 10⁵ Pa (définition de l'unité) ;
# - masse volumique de l'huile hydraulique, pression atmosphérique et toutes les autres valeurs
#   (dimensions, efforts, pressions) : DONNÉES D'ÉNONCÉ, annoncées comme telles.
import math

# ===========================================================================
# 1. FIGURES
# ===========================================================================

def hydrostatique_profondeur():
    p = [_k_defs(), _txt(30, 24, "Loi de l'hydrostatique : la pression ne dépend que de la profondeur", 13, TRAIT, "start", True)]
    # cuve
    x0, y0, L, H = 40, 60, 260, 220
    p.append(f"<rect x='{x0}' y='{y0 + 20}' width='{L}' height='{H - 20}' fill='#dbeafe' stroke='none'/>")
    p.append(f"<path d='M {x0} {y0} L {x0} {y0 + H} L {x0 + L} {y0 + H} L {x0 + L} {y0}' fill='none' stroke='{TRAIT}' stroke-width='3'/>")
    p.append(f"<line x1='{x0}' y1='{y0 + 20}' x2='{x0 + L}' y2='{y0 + 20}' stroke='{ALESAGE}' stroke-width='1.6'/>")
    p.append(_txt(x0 + L - 4, y0 + 14, "surface libre : p = p0", 10, ALESAGE, "end", True))
    for i, prof in enumerate((50, 110, 170)):
        y = y0 + 20 + prof
        lg = 10 + prof * 0.18
        p.append(_k_fl(x0 + 126 - lg, y, x0 + 124, y, ALERTE, "kr", 2))
        p.append(_k_fl(x0 + 134 + lg, y, x0 + 136, y, ALERTE, "kr", 2))
        if i == 1:
            p.append(_k_fl(x0 + 130, y - 8 - lg * 0.8, x0 + 130, y - 6, ALERTE, "kr", 2))
            p.append(_k_fl(x0 + 130, y + 8 + lg * 0.8, x0 + 130, y + 6, ALERTE, "kr", 2))
            p.append(_txt(x0 + 190, y + 4, "même pression dans", 9, ALERTE, "start"))
            p.append(_txt(x0 + 190, y + 15, "toutes les directions", 9, ALERTE, "start"))
        p.append(f"<circle cx='{x0 + 130}' cy='{y}' r='4' fill='{TRAIT}'/>")
        p.append(_txt(x0 + 130, y - 8, f"h{i + 1}", 10, TRAIT, "middle", True))
    p.append(_k_fl(x0 - 18, y0 + 22, x0 - 18, y0 + H - 2, FIN, "kk", 1.4))
    p.append(_txt(x0 - 22, y0 + 120, "h", 12, FIN, "end", True))
    p.append(_txt(x0 + 130, y0 + H + 18, "flèches rouges : la pression sur le point grandit avec la profondeur", 10, ALERTE, "middle"))
    # vases communicants
    x1 = 360
    p.append(_txt(x1 + 170, 62, "Vases de formes différentes, même niveau", 11, TRAIT, "middle", True))
    yb, ys = 250, 130
    p.append(f"<rect x='{x1 + 10}' y='{yb}' width='330' height='26' fill='#dbeafe' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<rect x='{x1 + 30}' y='{ys}' width='30' height='{yb - ys}' fill='#dbeafe' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<polygon points='{x1 + 120},{yb} {x1 + 150},{yb} {x1 + 200},{ys} {x1 + 70},{ys}' fill='#dbeafe' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<polygon points='{x1 + 240},{yb} {x1 + 330},{yb} {x1 + 300},{ys} {x1 + 270},{ys}' fill='#dbeafe' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(_txt(x1 + 45, ys + 60, "étroit", 9, FIN, "middle"))
    p.append(_txt(x1 + 135, ys + 60, "évasé", 9, FIN, "middle"))
    p.append(_txt(x1 + 285, ys + 60, "rétréci", 9, FIN, "middle"))
    p.append(f"<line x1='{x1}' y1='{ys}' x2='{x1 + 350}' y2='{ys}' stroke='{ALESAGE}' stroke-dasharray='6 4'/>")
    p.append(_txt(x1 + 350, ys - 6, "même hauteur partout", 10, ALESAGE, "end", True))
    p.append(_txt(x1 + 175, yb + 46, "au fond : même pression p0 + ρ g h, quelle que soit la forme", 10, TRAIT, "middle"))
    p.append(f"<rect x='30' y='316' width='730' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 338, "p = p0 + ρ g h : à la même profondeur, la même pression, dans toutes les directions.", 12, TRAIT, "start", True))
    return _svg("".join(p), 790, 362)


def presse_pascal():
    p = [_k_defs(), _txt(30, 24, "Théorème de Pascal : la presse hydraulique multiplie la force par le rapport des surfaces", 13, TRAIT, "start", True)]
    # deux cylindres reliés
    ya = 120
    p.append(f"<rect x='80' y='{ya}' width='40' height='150' fill='#fde68a' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<rect x='300' y='{ya}' width='200' height='150' fill='#fde68a' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<rect x='80' y='250' width='420' height='40' fill='#fde68a' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<rect x='82' y='252' width='416' height='36' fill='#fde68a'/>")
    p.append(_txt(290, 276, "huile : même pression p partout", 11, ARBRE, "middle", True))
    # piston 1 qui descend, piston 2 qui monte peu
    p.append(f"<g><animateTransform attributeName='transform' type='translate' values='0,0; 0,40; 0,0' dur='3s' repeatCount='indefinite'/>"
             f"<rect x='78' y='{ya - 10}' width='44' height='14' fill='{FIN}'/>"
             + _k_fl(100, ya - 52, 100, ya - 14, ALERTE, "kr", 3) + "</g>")
    p.append(_txt(100, 56, "F1 (petite)", 11, ALERTE, "middle", True))
    p.append(_txt(100, 72, "piston S1", 10, FIN, "middle"))
    p.append(f"<g><animateTransform attributeName='transform' type='translate' values='0,0; 0,-2; 0,0' dur='3s' repeatCount='indefinite'/>"
             f"<rect x='298' y='{ya - 10}' width='204' height='14' fill='{FIN}'/>"
             f"<line x1='400' y1='{ya - 10}' x2='400' y2='{ya - 62}' stroke='{OK}' stroke-width='5' marker-end='url(#kg)'/></g>")
    p.append(_txt(400, 44, "F2 (grande)", 11, OK, "middle", True))
    p.append(_txt(64, ya + 30, "c1", 11, ALERTE, "end", True))
    p.append(_txt(290, ya + 6, "c2 (petite)", 10, OK, "end", True))
    p.append(_txt(400, 60, "piston S2", 10, FIN, "middle"))
    x0 = 530
    p.append(f"<rect x='{x0}' y='60' width='240' height='230' rx='6' fill='#ffffff' stroke='{FIN}'/>")
    for i, (t, c, g) in enumerate((("Même pression des deux côtés :", TRAIT, True),
                                   ("p = F1 / S1 = F2 / S2", ARBRE, True),
                                   ("→ F2 = F1 × S2 / S1", OK, True),
                                   ("S = π D²/4 : D × 10 → S × 100", FIN, False),
                                   ("Même volume d'huile déplacé :", TRAIT, True),
                                   ("S1 × c1 = S2 × c2", ARBRE, True),
                                   ("→ le gros piston bouge peu", TRAIT, False), ("", TRAIT, False),
                                   ("Travail : F1 × c1 = F2 × c2", ALESAGE, True),
                                   ("on gagne en force, on perd", TRAIT, False),
                                   ("en course : rien n'est gratuit.", TRAIT, False))):
        if t:
            p.append(_txt(x0 + 12, 84 + 19 * i, t, 12, c, "start", g))
    p.append(f"<rect x='30' y='304' width='740' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 326, "Le même principe fait le vérin (F = p × S), le cric hydraulique, la presse d'atelier et le frein de voiture.", 12, TRAIT))
    return _svg("".join(p), 800, 350)


def poussee_paroi():
    p = [_k_defs(), _txt(30, 24, "Force de pression sur une paroi verticale : répartition triangulaire, résultante au tiers", 13, TRAIT, "start", True)]
    x0, y0, H = 150, 60, 220
    p.append(f"<rect x='{x0}' y='{y0}' width='160' height='{H}' fill='#dbeafe'/>")
    p.append(f"<line x1='{x0}' y1='{y0 - 10}' x2='{x0}' y2='{y0 + H + 6}' stroke='{TRAIT}' stroke-width='4'/>")
    p.append(f"<line x1='{x0}' y1='{y0 + H}' x2='{x0 + 170}' y2='{y0 + H}' stroke='{TRAIT}' stroke-width='3'/>")
    p.append(_txt(x0 + 80, y0 - 6, "eau (pression relative)", 10, ALESAGE, "middle", True))
    p.append(_txt(x0 + 6, y0 + H + 38, "paroi de la cuve", 10, TRAIT, "start", True))
    # diagramme de pression côté eau : l'eau pousse la paroi vers l'extérieur (vers la gauche)
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
    p.append(_txt(x0 - 84, yr - 8, "F résultante", 11, OK, "end", True))
    p.append(_k_fl(x0 + 190, y0 + H, x0 + 190, yr + 2, FIN, "kk", 1.2))
    p.append(_txt(x0 + 196, (y0 + H + yr) / 2 + 4, "h / 3", 11, FIN, "start", True))
    p.append(_k_fl(x0 + 230, y0 + 2, x0 + 230, y0 + H - 2, FIN, "kk", 1.2))
    p.append(_txt(x0 + 236, y0 + H / 2, "h", 11, FIN, "start", True))
    x1 = 470
    p.append(f"<rect x='{x1}' y='50' width='300' height='240' rx='6' fill='#ffffff' stroke='{FIN}'/>")
    for i, (t, c, g) in enumerate((("Paroi verticale, hauteur h, largeur L :", TRAIT, True),
                                   ("pression moyenne = ρ g h / 2", ARBRE, True),
                                   ("F = ρ g h / 2 × (h × L) = ρ g L h² / 2", OK, True),
                                   ("appliquée à h / 3 au-dessus du fond", OK, True), ("", TRAIT, False),
                                   ("Fond horizontal (profondeur h) :", TRAIT, True),
                                   ("pression uniforme ρ g h", ARBRE, True),
                                   ("F = ρ g h × S (= poids de l'eau si", OK, True),
                                   ("parois verticales)", OK, True),
                                   ("La pression atmosphérique agit des deux", FIN, False),
                                   ("côtés : on calcule en pression relative.", FIN, False))):
        if t:
            p.append(_txt(x1 + 12, 74 + 20 * i, t, 12, c, "start", g))
    p.append(f"<rect x='30' y='310' width='740' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 332, "La force sur une paroi croît comme h² : doubler la hauteur d'eau multiplie l'effort par 4.", 12, TRAIT, "start", True))
    return _svg("".join(p), 800, 356)


def archimede():
    p = [_k_defs(), _txt(30, 24, "Poussée d'Archimède : elle dépend du volume immergé, pas de la masse de l'objet", 13, TRAIT, "start", True)]
    x0, y0, W, H = 30, 70, 470, 200
    p.append(f"<rect x='{x0}' y='{y0 + 40}' width='{W}' height='{H - 40}' fill='#dbeafe'/>")
    p.append(f"<line x1='{x0}' y1='{y0 + H}' x2='{x0 + W}' y2='{y0 + H}' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<line x1='{x0}' y1='{y0 + 40}' x2='{x0 + W}' y2='{y0 + 40}' stroke='{ALESAGE}' stroke-width='1.6'/>")
    p.append(_txt(x0 + 4, y0 + 34, "surface de l'eau", 10, ALESAGE, "start"))
    blocs = ((x0 + 50, "ACIER 1 L (coule)", "#94a3b8", 77, 9.81, False), (x0 + 200, "ALUMINIUM 1 L (coule)", "#cbd5e1", 26.5, 9.81, False),
             (x0 + 350, "FLOTTEUR 10 L, 2 kg", "#fde68a", 19.6, 19.6, True))
    for xb, nom, col, poids, pa, flotte in blocs:
        yb = y0 - 16 if flotte else y0 + 90
        hb = 70 if flotte else 50
        p.append(f"<rect x='{xb}' y='{yb}' width='60' height='{hb}' fill='{col}' stroke='{TRAIT}' stroke-width='1.6'/>")
        p.append(_txt(xb + 30, y0 + H + 20, nom, 10, TRAIT, "middle", True))
        p.append(_k_fl(xb + 18, yb + hb / 2, xb + 18, yb + hb / 2 + min(48, poids * 1.6), ALERTE, "kr", 2.2))
        p.append(_k_fl(xb + 42, yb + hb / 2, xb + 42, yb + hb / 2 - min(48, pa * 1.6), OK, "kg", 2.2))
        if poids * 1.6 > 48:
            p.append(_txt(xb + 64, yb + hb / 2 + 44, "77 N (coupée)", 9, ALERTE, "start"))
        p.append(_txt(xb + 30, y0 + H + 36, f"poids {_fr_court(poids, 1)} N", 10, ALERTE, "middle"))
        p.append(_txt(xb + 30, y0 + H + 50, f"poussée {_fr_court(pa, 1)} N", 10, OK, "middle", True))
    p.append(_txt(x0 + 414, y0 + 38, "immergé", 9, FIN, "start"))
    p.append(_txt(x0 + 414, y0 + 50, "à 20 %", 9, FIN, "start"))
    x1 = 520
    p.append(f"<rect x='{x1}' y='50' width='250' height='240' rx='6' fill='#ffffff' stroke='{FIN}'/>")
    for i, (t, c, g) in enumerate((("Poussée d'Archimède :", TRAIT, True),
                                   ("Pa = ρ fluide × V immergé × g", OK, True),
                                   ("verticale, vers le haut,", TRAIT, False),
                                   ("au centre de carène (centre du", TRAIT, False),
                                   ("volume immergé)", TRAIT, False),
                                   ("Acier et aluminium, même volume :", TRAIT, True),
                                   ("même poussée (9,81 N), poids", TRAIT, False),
                                   ("différents : les deux coulent.", TRAIT, False),
                                   ("Flotteur : il s'enfonce jusqu'à", TRAIT, True),
                                   ("poussée = poids (2 L immergés).", TRAIT, False))):
        if t:
            p.append(_txt(x1 + 12, 74 + 20 * i, t, 12, c, "start", g))
    p.append(_txt(30, 344, "Eau 1 000 kg/m³ ; acier 7 850 et aluminium 2 700 kg/m³ (table des matériaux) ; g = 9,81 m/s². Flèches rouges : poids ; vertes : poussée.", 10, FIN))
    return _svg("".join(p), 800, 356)


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


def dyn_presse(D1=20.0, D2=200.0, F1=200.0):
    """Presse hydraulique : petit piston D1, grand piston D2 (mm), effort F1 (N), course du petit piston 100 mm."""
    S1, S2 = math.pi * D1 ** 2 / 4, math.pi * D2 ** 2 / 4
    pr = F1 / S1               # N/mm² = MPa
    F2 = pr * S2
    c2 = 100 * S1 / S2
    p = [_k_defs(), _txt(30, 24, f"Presse : petit piston Ø{_fr_court(D1, 0)}, grand piston Ø{_fr_court(D2, 0)}, F1 = {_fr_court(F1, 0)} N", 13, TRAIT, "start", True)]
    k = 1.0
    w1, w2 = max(10, D1 * k), max(30, D2 * k)
    x1, x2, yb = 80, 230, 270
    p.append(f"<rect x='{x1}' y='110' width='{w1:.0f}' height='{yb - 110}' fill='#fde68a' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<rect x='{x2}' y='110' width='{w2:.0f}' height='{yb - 110}' fill='#fde68a' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<rect x='{x1}' y='{yb}' width='{x2 + w2 - x1:.0f}' height='22' fill='#fde68a' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(_k_fl(x1 + w1 / 2, 60, x1 + w1 / 2, 104, ALERTE, "kr", 2.4))
    p.append(_txt(x1 + w1 / 2, 54, f"F1 = {_fr_court(F1, 0)} N", 11, ALERTE, "middle", True))
    lg = min(70, 20 + F2 / 1500)
    p.append(_k_fl(x2 + w2 / 2, 106, x2 + w2 / 2, 106 - lg, OK, "kg", 3))
    p.append(_txt(x2 + w2 / 2 + 8, 106 - lg / 2, f"F2 = {_fr_court(F2, 0)} N", 11, OK, "start", True))
    p.append(_txt((x1 + x2 + w2) / 2, yb + 40, f"huile à p = {_fr_court(pr, 2)} N/mm² = {_fr_court(pr * 10, 1)} bar", 11, ARBRE, "middle", True))
    x0 = 470
    p.append(f"<rect x='{x0}' y='44' width='300' height='250' rx='6' fill='#ffffff' stroke='{OK}' stroke-width='1.6'/>")
    lignes = ((f"S1 = π × {_fr_court(D1, 0)}² / 4 ≈ {_fr_court(S1, 0)} mm²", TRAIT, False),
              (f"S2 = π × {_fr_court(D2, 0)}² / 4 ≈ {_fr_court(S2, 0)} mm²", TRAIT, False),
              (f"rapport S2 / S1 = {_fr_court(S2 / S1, 1)}", ARBRE, True), ("", TRAIT, False),
              (f"F2 = F1 × S2 / S1 ≈ {_fr_court(F2, 0)} N", OK, True),
              (f"course : 100 mm en bas → {_fr_court(c2, 2)} mm en haut", ALESAGE, True),
              (f"travail : {_fr_court(F1 * 0.1, 1)} J des deux côtés", ALESAGE, False), ("", TRAIT, False),
              ("La force est multipliée, la course divisée,", FIN, False),
              ("dans le même rapport (pertes négligées).", FIN, False))
    for i, (t, c, g) in enumerate(lignes):
        if t:
            p.append(_txt(x0 + 12, 68 + 22 * i, t, 12, c, "start", g))
    p.append(_txt(30, 330, "Dessin à l'échelle des diamètres. Effort de l'opérateur, diamètres : données d'énoncé ; poids de l'huile négligé.", 10, FIN))
    return _svg("".join(p), 790, 344)


FIGURES_NOUVELLES = {
    "hydrostatique_profondeur": ("Loi de l'hydrostatique et vases communicants", hydrostatique_profondeur),
    "presse_pascal": ("Théorème de Pascal : la presse hydraulique", presse_pascal),
    "poussee_paroi": ("Force de pression sur une paroi verticale et sur un fond", poussee_paroi),
    "archimede": ("Poussée d'Archimède : volume immergé, pas masse", archimede),
    "stabilite_flottant": ("Stabilité d'un flotteur : poids et poussée", stabilite_flottant),
}
DYN_NOUVELLE = {
    "presse_curseurs": (
        "Change les diamètres des pistons et l'effort : la force et la course se recalculent",
        dyn_presse,
        [{"nom": "D1", "label": "Diamètre du petit piston D1 (mm)", "min": 10.0, "max": 40.0, "defaut": 20.0, "pas": 5.0},
         {"nom": "D2", "label": "Diamètre du grand piston D2 (mm)", "min": 50.0, "max": 200.0, "defaut": 200.0, "pas": 10.0},
         {"nom": "F1", "label": "Effort sur le petit piston F1 (N)", "min": 50.0, "max": 500.0, "defaut": 200.0, "pas": 50.0}]),
}

# ===========================================================================
# 2. FICHE 6.22 — en FIN de bloc 6 (après la 6.21)
# ===========================================================================

FICHE_6_22 = {
    "id": "6.22",
    "titre": "Statique des fluides : hydrostatique, théorème de Pascal, poussée d'Archimède, effort sur une paroi",
    "duree": "5 h",
    "cours": """### 1. Pourquoi cette fiche

Un vérin hydraulique soulève plusieurs tonnes avec une pompe de quelques kilowatts ; une cuve de quelques
mètres de haut doit résister à des dizaines de kilonewtons sur chaque paroi ; un flotteur de niveau monte
avec le liquide. Tout cela relève de la **statique des fluides** : un fluide **au repos**, et les efforts
qu'il exerce. La fiche 8.9 traite les fluides en mouvement (débit, Bernoulli, pertes de charge) ; la fiche
8.2 a posé p = F / S et l'effort d'un vérin. Celle-ci explique **d'où vient** la pression dans un fluide
et comment elle se transmet.

### 2. La pression, en un point d'un fluide

La pression est une force répartie sur une surface : **p = F / S** (fiche 8.2). Dans un fluide au repos,
elle a deux propriétés qui changent tout :

- elle **pousse perpendiculairement** à toute surface en contact (paroi, piston, fond) ;
- en un point donné, elle a **la même valeur dans toutes les directions**.

*Percez une bouteille d'eau de trois trous l'un au-dessus de l'autre : l'eau jaillit perpendiculairement à
la paroi, et le jet du bas va plus loin que celui du haut. En plongée, la pression pince les oreilles de la
même façon, tête droite ou penchée.*

**Unités** : 1 Pa = 1 N/m² ; 1 bar = 10⁵ Pa ; 1 N/mm² = 1 MPa = 10 bar.

**Pression absolue ou relative.** Le manomètre d'un circuit indique en général la pression **relative** :
l'écart avec la pression atmosphérique. Pour un effort sur une paroi qui a l'air des deux côtés, c'est la
pression relative qui compte : la pression atmosphérique pousse autant d'un côté que de l'autre.

### 3. La loi de l'hydrostatique

[[FIG:hydrostatique_profondeur]]

> **p = p0 + ρ × g × h**
> p0 : pression à la surface libre (Pa) ; ρ : masse volumique du fluide (kg/m³) ; g : accélération de la
> pesanteur, 9,81 m/s² ; h : profondeur sous la surface libre, comptée vers le bas (m) ; p en Pa.
> En pression relative (comptée à partir de la pression atmosphérique), p0 = 0 et il reste p = ρ g h.

**D'où elle vient : une statique.** Isolons une colonne verticale de fluide, de section S et de hauteur h,
qui part de la surface. Trois efforts verticaux : en haut, la pression p0 pousse vers le bas (p0 × S) ; en
bas, la pression p pousse vers le haut (p × S) ; et le poids de la colonne, ρ × (S × h) × g. Le fluide est
au repos, donc la somme est nulle (fiche 12.1) : p × S = p0 × S + ρ S h g, d'où p = p0 + ρ g h. La pression
au fond, c'est ce qu'il faut pour porter le fluide au-dessus.

*Ordre de grandeur (eau : 1 000 kg/m³, valeur arrondie d'usage) : à 10 m de profondeur, ρ g h = 1 000 × 9,81
× 10 = 98 100 Pa ≈ **1 bar** de plus qu'en surface.*

**Conséquences directes.**

- **Même profondeur, même pression**, quelle que soit la forme du récipient : c'est le principe des **vases
  communicants** (le niveau s'égalise) et du **niveau à eau** des maçons (un tuyau transparent rempli d'eau
  dont les deux bouts affichent le même niveau). *Pourquoi la forme ne compte pas : dans la démonstration,
  la colonne ne porte que l'eau située juste au-dessus d'elle ; dans un vase évasé, l'eau « en trop » sur
  les côtés est portée par les parois inclinées, pas par le fond.*
- **Dans un circuit hydraulique, on néglige ρ g h.** *Exemple (huile de masse volumique 850 kg/m³, donnée
  d'énoncé, la même qu'en fiche 8.9) : 1 m de dénivelé donne 850 × 9,81 × 1 ≈ 8 340 Pa ≈ 0,083 bar, à comparer
  aux 100 bar d'un circuit (donnée d'énoncé) : moins de 0,1 %.* C'est pourquoi on considère la pression **uniforme** dans
  tout le circuit.

### 4. Le théorème de Pascal : la pression se transmet

> **Une variation de pression en un point d'un fluide incompressible au repos se transmet intégralement en
> tous ses points.**

**D'où il vient.** De la loi précédente : p = p0 + ρ g h. Si l'on appuie sur le piston, p0 augmente, par
exemple de 10 bar. Le fluide, **incompressible** (on ne peut pas réduire son volume en appuyant, contrairement
à l'air d'une pompe à vélo dont on bouche la sortie), ne bouge pratiquement pas : ρ g h ne change pas, et p
augmente de 10 bar en chaque point. *Image : une seringue pleine ou un tube de dentifrice — on appuie à un
bout, ça pousse à l'autre.* C'est ce qui permet de commander un effort à distance par un simple tuyau.

[[FIG:presse_pascal]]

**La presse hydraulique.** Deux pistons de surfaces S1 (petit) et S2 (grand), reliés par l'huile :

> p = F1 / S1 = F2 / S2  →  **F2 = F1 × S2 / S1**

**Pourquoi la grande surface donne la grande force.** La pression, c'est la force portée par chaque mm². La
pression étant la même partout, chaque mm² du grand piston est poussé exactement comme chaque mm² du petit :
un piston qui a 100 fois plus de mm² reçoit 100 fois plus de force — comme 100 petits pistons côte à côte.

**Pourquoi le carré des diamètres.** S = π D² / 4 : dans le rapport S2 / S1, le π / 4 se simplifie, et
S2 / S1 = (D2 / D1)². *Une plaque carrée de 10 mm de côté, puis une de 20 mm : le côté double, mais il faut 4
petites plaques pour couvrir la grande.* Un piston 10 fois plus large a 10 × 10 = 100 fois plus de surface.
La figure à curseurs ci-dessous le montre : le rapport des surfaces suit le carré du rapport des diamètres.

*Exemple (données d'énoncé) : petit piston Ø20, grand piston Ø200, effort de l'opérateur F1 = 200 N.
S2 / S1 = (200 / 20)² = 100 → **F2 = 20 000 N** (le poids d'environ 2 tonnes). Pression : p = 200 / (π × 10²)
≈ 0,64 N/mm² ≈ 6,4 bar.*

**Rien n'est gratuit : la course.** Le petit piston descend de sa course c1 : il chasse un cylindre d'huile
de section S1 et de hauteur c1, soit un volume S1 × c1. L'huile étant incompressible, ce volume s'étale sous
le grand piston, 100 fois plus large : il ne le soulève que d'une couche 100 fois plus mince,
**S1 × c1 = S2 × c2**. Si le petit piston descend de 100 mm, le grand monte de 100 / 100 = **1 mm**. *C'est
pour ça qu'on pompe une vingtaine de fois le levier d'un cric pour monter la voiture de quelques
centimètres.* Le travail est le même des deux côtés : F1 × c1 = 200 × 0,1 = 20 J, et F2 × c2 = 20 000 × 0,001
= 20 J.

C'est la logique **effort × flux** de la fiche 6.20 : côté petit piston, F1 × v1 ; côté grand piston, F2 ×
v2 ; côté huile, p × Qv, le même des deux côtés. Le grand piston va 100 fois moins vite : F2 peut être 100
fois plus grande pour la même puissance. La presse échange de la force contre de la course, comme un réducteur
échange du couple contre de la vitesse.

[[DYN:presse_curseurs]]

**Le vérin.** Un vérin est la moitié d'une presse. La centrale envoie l'huile : la pompe fournit le
**débit** (fiche 6.20), la pression monte jusqu'à ce qu'il faut pour vaincre la charge (au plus le réglage
du limiteur de pression), et le piston la transforme en force.

> **Sortie : F = p × S** (toute la surface du piston) · **Rentrée : F = p × (S − s)** (surface annulaire :
> le disque du piston moins le disque de la tige, là où l'huile ne peut pas appuyer)
> L'autre chambre est reliée au réservoir (0 bar relatif) ; frottements des joints négligés.

*Exemple (données d'énoncé) : vérin d'alésage Ø63, tige Ø36, sous 100 bar = 10 N/mm². Sortie : S = π × 63² /
4 ≈ 3 117 mm², F ≈ **31 200 N**. Rentrée : S − s = 3 117 − π × 36² / 4 ≈ 2 100 mm², F ≈ **21 000 N**.*

*Vis ou vérin (fiche 6.18) ? Les deux obéissent à la même règle que la presse : la vis transforme beaucoup de
tours de manivelle en un petit avancement avec un gros effort ; le vérin, beaucoup d'huile pompée en une
petite course avec un gros effort. La vis-écrou donne une position précise et peut être irréversible ; le vérin
hydraulique donne de très grands efforts sous un faible encombrement, avec une centrale à distance — mais
il faut une pompe, des tuyaux, et il peut fuir.*

### 5. Force de pression sur une surface

**Sur un fond horizontal**, à la profondeur h, la pression relative ρ g h est la même partout :

> **F = ρ g h × S** — le poids d'une colonne de fluide de base S et de hauteur h. Pour une cuve à parois
> verticales, c'est exactement le poids du fluide qu'elle contient ; pour un récipient évasé ou rétréci, non :
> l'effort sur le fond ne dépend que de h et de S, pas de la quantité de liquide.

**Sur une paroi verticale** de hauteur h et de largeur L, la pression relative croît de 0 (surface) à ρ g h
(fond) : la répartition est **triangulaire**. *Découpez une paroi de 2 m en 4 bandes de 0,5 m : la pression au
milieu de chaque bande correspond aux profondeurs 0,25 ; 0,75 ; 1,25 ; 1,75 m, dont la moyenne est 1 m, soit
h / 2.* Comme la pression grandit régulièrement avec la profondeur, la force totale vaut la pression de
mi-hauteur × la surface :

> **F = (ρ g h / 2) × (h × L) = ρ g L h² / 2**, appliquée à **h / 3 au-dessus du fond** (centre de poussée)

[[FIG:poussee_paroi]]

*Pourquoi h / 3 : la répartition est un triangle, et la résultante d'une charge triangulaire passe par le
centre de gravité du triangle, au tiers de sa hauteur, côté du grand bord — ici, le fond.*

*Exemple (données d'énoncé) : cuve d'eau rectangulaire, fond 3 m × 1,5 m, hauteur d'eau 2 m.
Pression au fond : ρ g h = 1 000 × 9,81 × 2 = **19 620 Pa**. Fond : F = 19 620 × 4,5 = **88 290 N** — le
poids des 9 m³ d'eau, 9 000 × 9,81 ✔. Grande paroi (L = 3 m) : F = 1 000 × 9,81 × 3 × 2² / 2 = **58 860 N**,
appliquée à 2 / 3 ≈ 0,67 m au-dessus du fond.*

**Ce que ça change en conception.** L'effort sur la paroi croît comme **h²** : doubler la hauteur d'eau
multiplie l'effort par 4, et son point d'application est en bas. C'est pour cela que les raidisseurs d'une
cuve sont plus serrés près du fond, et qu'un barrage est plus épais à sa base.

### 6. La poussée d'Archimède

> **Tout corps immergé dans un fluide subit une poussée verticale, vers le haut, égale au poids du volume de
> fluide déplacé : Pa = ρ fluide × V immergé × g**, appliquée au centre du volume immergé, appelé **centre de
> carène** C.

**D'où elle vient.** Les pressions sur le dessous d'un objet immergé sont plus fortes que sur le dessus (le
dessous est plus profond) : la différence pousse vers le haut. *Pourquoi elle vaut le poids du fluide
déplacé : imaginez à la place de l'objet un « bloc d'eau » de même forme. Il ne monte pas et ne descend pas :
l'eau autour le porte exactement, donc les pressions sur sa surface valent tout juste son poids. Remplacez ce
bloc d'eau par de l'acier ou de l'aluminium de même forme : l'eau autour ne « sait » pas ce qu'il y a dedans,
elle pousse exactement pareil. La poussée dépend de la place occupée, pas de ce qui l'occupe ; seul le poids
change, et c'est lui qui décide si l'objet coule.*

[[FIG:archimede]]

**Le piège classique : la poussée ne dépend pas de la masse de l'objet, mais de son volume immergé.** *Un
bloc d'acier et un bloc d'aluminium de 1 L chacun, entièrement immergés dans l'eau, reçoivent la même
poussée : 1 000 × 0,001 × 9,81 = **9,81 N**. Leurs poids sont différents : 7,85 × 9,81 ≈ 77 N pour l'acier,
2,7 × 9,81 ≈ 26,5 N pour l'aluminium (table des matériaux). Les deux coulent, mais le bloc d'aluminium
« pèse » dans l'eau 26,5 − 9,8 ≈ 16,7 N au lieu de 26,5 N : c'est son **poids apparent**, ce qu'indiquerait un
peson qui le tient sous l'eau.*

**Flottaison.** Un objet flotte quand il peut déplacer un volume de fluide qui pèse autant que lui : il
s'enfonce jusqu'à ce que **poussée = poids**. *Exemple (données d'énoncé) : flotteur creux de 10 L et de 2 kg.
Il s'enfonce jusqu'à déplacer 2 kg d'eau, soit 2 L : il flotte immergé à 20 %.* C'est le principe du
flotteur de niveau et du robinet flotteur.

**Stabilité d'un flotteur.** *Pensez au canoë : assis, il est stable ; debout, vous chavirez. Ce qui compte,
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
un ponton large ou un catamaran chavirent difficilement.

[[FIG:stabilite_flottant]]

### 7. Les erreurs classiques

1. **Mélanger les unités** : 1 bar = 10⁵ Pa ; 1 N/mm² = 10 bar. Un effort en N avec une surface en mm²
   donne des N/mm².
2. **Prendre le rapport des diamètres au lieu du rapport des surfaces** : F2 / F1 = (D2 / D1)², pas D2 / D1.
3. **Oublier la tige** pour la rentrée d'un vérin : surface annulaire S − s.
4. **Calculer la force sur une paroi avec la pression du fond** : la pression moyenne est la moitié.
5. **Croire que la poussée d'Archimède dépend de la masse** : elle dépend du volume immergé et du fluide.
6. **Compter la pression atmosphérique** sur une paroi qui a l'air des deux côtés : elle s'annule.
7. **Croire qu'une presse « crée » de l'énergie** : la force est multipliée, la course divisée.

### 8. À retenir

- **p = p0 + ρ g h** : la pression ne dépend que de la profondeur (vases communicants). Dans un circuit
  hydraulique, ρ g h est négligeable : pression uniforme.
- **Pascal** : la pression se transmet intégralement. Presse : **F2 = F1 × S2 / S1** et **S1 c1 = S2 c2** ;
  le travail se conserve. Vérin : **F = p S** (sortie), **p (S − s)** (rentrée).
- Fond : **F = ρ g h S** (poids du fluide si parois verticales). Paroi verticale : **F = ρ g L h² / 2**, à
  **h/3** du fond.
- **Archimède : Pa = ρ fluide V immergé g** — le volume, pas la masse. Flottaison : poussée = poids.
  Stabilité : G sous le métacentre M, avec **CM = I / V**.
""",
    "formules": """
**Pression** — p = F / S · 1 bar = 10⁵ Pa · 1 N/mm² = 1 MPa = 10 bar

**Loi de l'hydrostatique** — p = p0 + ρ g h (pression relative : ρ g h)

**Pascal, presse** — F2 = F1 × S2 / S1 = F1 × (D2 / D1)² · S1 c1 = S2 c2 · F1 c1 = F2 c2

**Vérin** — sortie F = p S · rentrée F = p (S − s) · S = π D² / 4

**Fond horizontal** — F = ρ g h S · **Paroi verticale** — F = ρ g L h² / 2, à h / 3 au-dessus du fond

**Archimède** — Pa = ρ fluide × V immergé × g · flottaison : Pa = poids · métacentre : CM = I / V ; stable si
G sous M

**Données** — eau 1 000 kg/m³ (valeur arrondie d'usage) · g = 9,81 m/s² · autres fluides : données d'énoncé
""",
    "exemple": """
### Cas industriel — La presse qui ne donnait pas son effort

**Le symptôme.** Un atelier installe une presse hydraulique manuelle pour emmancher des bagues. Le
constructeur annonce 50 kN. À l'essai, avec la même pompe à main, l'opérateur n'obtient qu'environ 32 kN, et
le grand piston recule lentement sous la charge quand on relâche.

**L'analyse, avec Pascal.** L'effort obtenu vaut p × S2. Le rapport des surfaces est fixé par les diamètres :
il n'a pas changé. C'est donc **la pression** qui n'atteint pas sa valeur. Deux causes possibles :

- de l'**air** dans le circuit : l'air est compressible, il se comprime comme un ressort ; à chaque coup de
  pompe, la course du petit piston sert à écraser la bulle au lieu de chasser de l'huile vers le grand piston,
  et la pompe n'arrive plus à faire monter la pression (le volume ne se conserve plus : S1 c1 = S2 c2 suppose
  un fluide incompressible). La presse devient « spongieuse » ;
- une **fuite** au joint du grand piston ou au clapet : la pression retombe, d'où le piston qui recule.

**Le diagnostic chiffré** (données d'énoncé) : grand piston Ø80, S2 = π × 80² / 4 ≈ 5 027 mm². Pour 50 kN, il
faut p = 50 000 / 5 027 ≈ 9,95 N/mm² ≈ 99,5 bar. Les 32 kN mesurés correspondent à ≈ 64 bar : il manque
plus d'un tiers de la pression.

**La correction.** Purge de l'air selon la notice du constructeur, remplacement du joint du grand piston, contrôle au manomètre : la pression monte à 100 bar et reste stable, l'effort atteint
les 50 kN.

**Ce que le cas apprend.** Le théorème de Pascal suppose un fluide **incompressible** et un circuit
**étanche**. Quand l'effort manque sur un système hydraulique, on contrôle d'abord la pression (manomètre),
puis l'air et les fuites — le rapport des surfaces, lui, ne ment pas.
""",
    "exercice": """
### Exercice — Le vérin de levage et sa cuve d'huile

Un vérin hydraulique d'alésage **Ø80 mm** et de tige **Ø45 mm** soulève une charge. La centrale délivre
**120 bar** (données d'énoncé).

**1.** Calculer l'effort du vérin en sortie et en rentrée.

**2.** La charge à soulever pèse 5 000 kg (g = 9,81 m/s²). Le vérin, monté verticalement, la soulève en
sortie. Quelle pression minimale faut-il (frottements, poids du piston et de la tige négligés ; chambre côté
tige reliée au réservoir) ?

**3.** Le réservoir de la centrale est une cuve parallélépipédique remplie d'huile sur **0,6 m** de hauteur,
de masse volumique **850 kg/m³** (donnée d'énoncé). Sa grande paroi mesure **0,8 m** de large. Calculer la
pression relative au fond et la force sur la grande paroi. Où s'applique-t-elle ?

**4.** Un flotteur de niveau, en plastique, a un volume de 0,5 L et une masse de 0,2 kg. Quelle fraction de
son volume est immergée dans l'huile ?
""",
    "corrige": """
### Corrigé, en six temps

#### 1. Ce que dit l'énoncé

Un vérin et sa pression d'alimentation, une charge à soulever, un réservoir d'huile et son flotteur.

#### 2. Quelle règle, et pourquoi

> **Vérin : F = p S (sortie), p (S − s) (rentrée)** ; **hydrostatique : p = ρ g h** ; **paroi : F = ρ g L h² / 2
> à h/3 du fond** ; **Archimède : flottaison quand ρ fluide V immergé g = m g**.

#### 3. Les conversions

120 bar = 12 N/mm² ; surfaces en mm² ; hauteurs en m ; 0,5 L = 0,0005 m³.

#### 4. Le remplacement

S = π × 80² / 4 ; s = π × 45² / 4 ; F = 12 × S ; p min = m g / S ; p fond = 850 × 9,81 × 0,6 ;
F paroi = 850 × 9,81 × 0,8 × 0,6² / 2 ; V immergé = m / ρ huile.

#### 5. Le calcul

**1.** S = π × 80² / 4 ≈ 5 027 mm² → sortie F = 12 × 5 027 ≈ **60 300 N**. s = π × 45² / 4 ≈ 1 590 mm² →
rentrée F = 12 × (5 027 − 1 590) ≈ **41 200 N**.

**2.** Poids : 5 000 × 9,81 = 49 050 N. p min = 49 050 / 5 027 ≈ 9,76 N/mm² ≈ **97,6 bar** : les 120 bar
suffisent, avec une marge.

**3.** p fond = 850 × 9,81 × 0,6 ≈ **5 003 Pa** (≈ 0,05 bar). F paroi = 850 × 9,81 × 0,8 × 0,36 / 2 ≈
**1 201 N**, appliquée à 0,6 / 3 = **0,2 m** au-dessus du fond.

**4.** Volume d'huile à déplacer : m / ρ = 0,2 / 850 ≈ 0,000235 m³ = 0,235 L ; fraction immergée 0,235 / 0,5 ≈
**47 %**.

#### 6. La vérification

**Unités** : N/mm² × mm² = N ; Pa × m² = N. **Bon sens** : la rentrée donne moins d'effort que la sortie (la
tige mange de la surface) ; l'effort sur la paroi du réservoir reste modeste (faible hauteur : il croît comme
h²) ; le flotteur s'enfonce davantage dans l'huile que dans l'eau, l'huile étant moins dense.
""",
}

# ===========================================================================
# 3. MÉTHODE
# ===========================================================================
MTH_6_22 = ("6.22", "Calculer un effort hydraulique (presse, vérin, paroi)", [
    "**Mettre les unités d'accord** : bar → N/mm² (÷ 10) pour un effort en N sur une surface en mm² ; ou Pa et m².",
    "**Presse ou vérin (Pascal)** : pression uniforme dans le circuit ; F = p × S, avec S = π D² / 4 (surface "
    "annulaire S − s en rentrée). Presse : F2 = F1 × (D2 / D1)², courses dans le rapport inverse.",
    "**Paroi ou fond (hydrostatique)** : pression relative ρ g h ; fond : F = ρ g h S ; paroi verticale : "
    "F = ρ g L h² / 2, à h / 3 au-dessus du fond.",
    "**Vérifier** : pour un fond de cuve à parois verticales, F doit valoir le poids du fluide ; pour une "
    "presse, F1 c1 = F2 c2.",
], "Presse Ø20 / Ø200, F1 = 200 N : rapport (200 / 20)² = 100 → F2 = 20 000 N ; 100 mm de course en bas → 1 mm "
   "en haut ; 20 J des deux côtés.")

# ===========================================================================
# 4. ATELIERS (fin de liste ATELIERS, après at171)
# ===========================================================================
ATELIERS_NOUVEAUX = [
    {
        "id": "at172",
        "chapitre": "Bloc 6",
        "titre": "Presse hydraulique d'atelier : effort, pression et course",
        "theme": "Statique des fluides",
        "fiche": "6.22",
        "figure": "presse_pascal",
        "vocabulaire": [
            ("Théorème de Pascal",
             "une variation de pression dans un fluide incompressible au repos se transmet intégralement en tous ses "
             "points."),
            ("Rapport des surfaces",
             "S2 / S1 = (D2 / D1)² : c'est lui qui multiplie la force."),
            ("Course",
             "le déplacement d'un piston ; le volume d'huile se conserve : S1 c1 = S2 c2."),
        ],
        "enonce": "Une presse hydraulique a un petit piston de Ø20 mm et un grand piston de Ø200 mm. L'opérateur "
                  "exerce 200 N sur le petit piston (données d'énoncé ; poids de l'huile et frottements négligés).",
        "etapes": [
            {"type": "numerique", "label": "Pression dans l'huile",
             "unite": "N/mm²", "attendu": 0.6366, "tol": 0.005,
             "consigne": "Calcule p = F1 / S1, avec S1 = π × D1² / 4.",
             "indice": "S1 = π × 20² / 4 ≈ 314,2 mm².",
             "pieges": [(0.1592, "0,159 : tu as pris S1 = π × D², en oubliant le « / 4 ». S1 = π × 20² / 4 = π × 10² "
                                 "≈ 314 mm².")],
             "aide": "p = 200 / 314,2 ≈ 0,637 N/mm² ≈ 6,4 bar."},
            {"type": "numerique", "label": "Effort du grand piston",
             "unite": "N", "attendu": 20000, "tol": 20,
             "consigne": "Calcule F2 = F1 × S2 / S1 (garde p non arrondi, ou passe par le rapport des surfaces).",
             "indice": "S2 / S1 = (D2 / D1)².",
             "pieges": [(2000, "2 000 N : tu as pris le rapport des diamètres (10) au lieu du rapport des surfaces "
                               "(10² = 100).")],
             "aide": "(200 / 20)² = 100 ; F2 = 200 × 100 = 20 000 N."},
            {"type": "numerique", "label": "Course du grand piston",
             "unite": "mm", "attendu": 1, "tol": 0.02,
             "consigne": "Le petit piston descend de 100 mm. De combien monte le grand piston ?",
             "indice": "Le volume d'huile se conserve : S1 × c1 = S2 × c2.",
             "pieges": [(10, "10 mm : tu as divisé par le rapport des diamètres. Ce sont les surfaces (rapport 100) "
                             "qui comptent.")],
             "aide": "c2 = 100 / 100 = 1 mm."},
            {"type": "qcm", "label": "Énergie",
             "question": "La presse multiplie la force par 100. Multiplie-t-elle aussi l'énergie ?",
             "options": ["Oui : 100 fois plus de force, donc 100 fois plus d'énergie",
                         "Non : la course est divisée par 100, le travail F × c est le même (20 J) des deux côtés",
                         "Non : elle en perd la moitié par principe"], "bonne": 1,
             "indice": "Comparer F1 × c1 et F2 × c2.",
             "diagnostics": {0: "Le travail, c'est F × c : la force est multipliée par 100 mais la course divisée par "
                                 "100. 200 × 0,1 = 20 000 × 0,001 = 20 J.",
                             2: "Aucune perte « par principe » : sans frottement ni fuite, le travail se conserve "
                                "exactement. Les pertes réelles viennent des frottements et des fuites."}},
        ],
        "corrige": {
            "enonce": "Presse Ø20 / Ø200, F1 = 200 N ; course du petit piston 100 mm.",
            "regle": "**Pascal : p = F1 / S1 = F2 / S2** ; **F2 = F1 × (D2 / D1)²** ; **S1 c1 = S2 c2**.",
            "conversions": "Surfaces en mm², efforts en N, pression en N/mm² (1 N/mm² = 10 bar).",
            "remplacement": "S1 = π × 20² / 4 ; p = 200 / S1 ; F2 = 200 × 100 ; c2 = 100 / 100.",
            "calcul": "**p ≈ 0,637 N/mm²** (≈ 6,4 bar) ; **F2 = 20 000 N** ; **c2 = 1 mm**.",
            "verification": "F1 c1 = 200 × 0,1 = 20 J ; F2 c2 = 20 000 × 0,001 = 20 J : on gagne en force ce qu'on "
                            "perd en course.",
        },
        "a_retenir": "À retenir : la presse multiplie la force par le rapport des SURFACES, (D2 / D1)², et divise la "
                     "course dans le même rapport : le travail se conserve.",
    },
    {
        "id": "at173",
        "chapitre": "Bloc 6",
        "titre": "Cuve d'eau et flotteur : poussée sur la paroi, poussée d'Archimède",
        "theme": "Statique des fluides",
        "fiche": "6.22",
        "figure": "poussee_paroi",
        "vocabulaire": [
            ("Pression relative",
             "l'écart avec la pression atmosphérique : ρ g h sous la surface libre."),
            ("Centre de poussée (paroi)",
             "le point d'application de la résultante des pressions sur une paroi ; paroi verticale : à h/3 du fond."),
            ("Poussée d'Archimède",
             "poids du fluide déplacé : ρ fluide × V immergé × g, vers le haut."),
        ],
        "enonce": "Une cuve d'eau (1 000 kg/m³) a un fond de 3 m × 1,5 m et contient 2 m d'eau. Un flotteur creux de 10 L "
                  "et de 2 kg y flotte (données d'énoncé ; g = 9,81 m/s²).",
        "etapes": [
            {"type": "numerique", "label": "Pression relative au fond",
             "unite": "Pa", "attendu": 19620, "tol": 20,
             "consigne": "Calcule p = ρ g h.",
             "indice": "ρ = 1 000 kg/m³, h = 2 m.",
             "pieges": [(2000, "2 000 : tu as oublié g. p = ρ × g × h.")],
             "aide": "1 000 × 9,81 × 2 = 19 620 Pa."},
            {"type": "numerique", "label": "Force sur la grande paroi (L = 3 m)",
             "unite": "N", "attendu": 58860, "tol": 60,
             "consigne": "Calcule F = ρ g L h² / 2.",
             "indice": "Pression moyenne ρ g h / 2, sur une surface h × L.",
             "pieges": [(117720, "117 720 N : tu as pris la pression du fond sur toute la paroi. Elle croît de 0 en "
                                 "surface à ρ g h au fond : la moyenne est la moitié.")],
             "aide": "1 000 × 9,81 × 3 × 2² / 2 = 58 860 N."},
            {"type": "numerique", "label": "Hauteur du point d'application",
             "unite": "m", "attendu": 0.667, "tol": 0.01,
             "consigne": "À quelle hauteur au-dessus du fond s'applique cette force ?",
             "indice": "Répartition triangulaire : résultante au tiers de la hauteur, côté du fond.",
             "pieges": [(1.0, "1 m, c'est mi-hauteur : vrai pour une pression uniforme. Ici elle est plus forte en "
                              "bas : la résultante descend à h/3."),
                        (1.333, "1,33 m : c'est 2h/3 mesuré depuis le fond. La résultante est à h/3 au-dessus du fond "
                                "(2h/3 sous la surface).")],
             "aide": "2 / 3 ≈ 0,667 m au-dessus du fond."},
            {"type": "numerique", "label": "Volume immergé du flotteur",
             "unite": "L", "attendu": 2, "tol": 0.02,
             "consigne": "À l'équilibre, poussée = poids. Quel volume d'eau le flotteur déplace-t-il ?",
             "indice": "ρ eau × V × g = m × g → V = m / ρ.",
             "pieges": [(10, "10 L, c'est le volume total du flotteur : il ne coulerait que s'il pesait 10 kg."),
                        (0.002, "0,002 : c'est en m³ ; la réponse est demandée en litres (× 1 000).")],
             "aide": "V = 2 / 1 000 = 0,002 m³ = 2 L (20 % du flotteur)."},
            {"type": "qcm", "label": "Le piège d'Archimède",
             "question": "On remplace le flotteur par un bloc d'acier de 1 L, puis par un bloc d'aluminium de 1 L, "
                         "entièrement immergés. Lequel reçoit la plus grande poussée ?",
             "options": ["L'acier, parce qu'il est plus lourd", "L'aluminium, parce qu'il est plus léger",
                         "Les deux reçoivent la même poussée : même volume immergé (9,81 N)"], "bonne": 2,
             "indice": "De quoi dépend la poussée : de la masse de l'objet ou du volume de fluide déplacé ?",
             "diagnostics": {0: "La poussée ne dépend pas de la masse de l'objet : c'est le poids du fluide déplacé, "
                                 "1 L d'eau pour les deux.",
                             1: "Plus léger ne veut pas dire plus poussé : même volume immergé, même poussée. "
                                "L'aluminium coule moins « lourdement », c'est tout."}},
        ],
        "corrige": {
            "enonce": "Cuve d'eau, fond 3 m × 1,5 m, 2 m d'eau ; flotteur 10 L, 2 kg.",
            "regle": "**p = ρ g h** ; **paroi : F = ρ g L h² / 2, à h/3 du fond** ; **Archimède : ρ V immergé g = m g**.",
            "conversions": "Unités SI ; 1 L = 0,001 m³.",
            "remplacement": "p = 1 000 × 9,81 × 2 ; F = 1 000 × 9,81 × 3 × 4 / 2 ; h/3 = 2/3 ; V = 2 / 1 000.",
            "calcul": "**p = 19 620 Pa** ; **F = 58 860 N** à **0,667 m** du fond ; **V immergé = 2 L**.",
            "verification": "Le fond reçoit 19 620 × 4,5 = 88 290 N = poids des 9 m³ d'eau (9 000 × 9,81), comme il "
                            "se doit pour une cuve à parois verticales.",
        },
        "a_retenir": "À retenir : sur une paroi verticale, pression moyenne ρ g h / 2 et résultante à h/3 du fond ; "
                     "la poussée d'Archimède dépend du volume immergé, pas de la masse de l'objet.",
    },
]

# ===========================================================================
# 5. GÉNÉRATEURS (nouvelle famille « Statique des fluides »)
# ===========================================================================
GENERATEUR = '''
def gen_presse_hydraulique():
    """Effort du grand piston d'une presse hydraulique : F2 = F1 × (D2 / D1)²."""
    D1 = random.choice([10, 12, 16, 20, 25, 30])
    D2 = random.choice([d for d in (50, 63, 80, 100, 125, 160, 200) if d > 2 * D1])
    F1 = random.choice([50, 100, 150, 200, 250, 300])
    F2 = F1 * (D2 / D1) ** 2
    diag = []
    for val, msg in (
            (F1 * D2 / D1, "Tu as multiplié par le rapport des diamètres. Ce sont les SURFACES qui comptent : "
                           "(D2 / D1)²."),
            (F1 * D1 / D2, "Tu as inversé le rapport : le grand piston donne la plus grande force."),
            (F1 * (D1 / D2) ** 2, "Rapport inversé : F2 = F1 × S2 / S1, avec S2 la grande surface."),
    ):
        if abs(val - F2) > F2 * 0.02 and all(abs(val - d["v"]) > 1 for d in diag):
            diag.append(_diag(round(val, 1), msg))
    return {
        "titre": "Statique des fluides — presse hydraulique",
        "enonce": (f"Une presse hydraulique a un petit piston de **Ø{D1} mm** et un grand piston de **Ø{D2} mm**. On "
                   f"exerce **{F1} N** sur le petit piston. Quel effort (en N) le grand piston fournit-il (pertes "
                   "négligées) ?"),
        "rep": round(F2, 1), "tol": max(1.0, F2 * 0.005), "unite": "N",
        "diag": diag,
        "corr": [
            f"**Ce que dit l'énoncé.** Petit piston Ø{D1}, grand piston Ø{D2}, effort {F1} N.",
            "**Le théorème de Pascal.** La pression est la même sous les deux pistons : F1 / S1 = F2 / S2.",
            f"**Le rapport des surfaces.** S2 / S1 = (D2 / D1)² = ({D2} / {D1})² = {fr((D2 / D1) ** 2, 2)}.",
            f"**L'effort.** F2 = {F1} × {fr((D2 / D1) ** 2, 2)} = {fr(F2, 0)} N.",
            "**Je vérifie.** La course du grand piston est divisée dans le même rapport : le travail se conserve.",
        ],
        "indice": "F2 = F1 × S2 / S1 = F1 × (D2 / D1)².",
    }


def gen_poussee_archimede():
    """Poussée d'Archimède sur un objet entièrement immergé dans l'eau (1 000 kg/m³)."""
    a = random.choice([50, 80, 100, 120, 150, 200])
    b = random.choice([40, 50, 60, 80, 100])
    c = random.choice([20, 25, 30, 40, 50])
    mat = random.choice([("acier", 7850), ("aluminium", 2700)])
    V = a * b * c / 1e9
    Pa = 1000 * V * 9.81
    diag = []
    for val, msg in (
            (mat[1] * V * 9.81, "Tu as utilisé la masse volumique de l'objet : la poussée, c'est le poids du FLUIDE "
                                "déplacé (eau, 1 000 kg/m³)."),
            (1000 * V, "Il manque g : la poussée est une force, ρ × V × g."),
            ((mat[1] - 1000) * V * 9.81, "C'est le poids apparent dans l'eau (poids − poussée), pas la poussée."),
    ):
        if abs(val - Pa) > max(0.01, Pa * 0.02) * 2 and all(abs(val - d["v"]) > 0.01 for d in diag):
            diag.append(_diag(round(val, 3), msg))
    return {
        "titre": "Statique des fluides — poussée d'Archimède",
        "enonce": (f"Un bloc d'{mat[0]} de **{a} × {b} × {c} mm** est entièrement immergé dans l'eau "
                   "(1 000 kg/m³ ; g = 9,81 m/s²). Quelle poussée d'Archimède (en N) reçoit-il ?"),
        "rep": round(Pa, 3), "tol": max(0.005, Pa * 0.01), "unite": "N",
        "diag": diag,
        "corr": [
            f"**Ce que dit l'énoncé.** Un bloc de {a} × {b} × {c} mm, entièrement immergé dans l'eau.",
            f"**Le volume immergé.** V = {a} × {b} × {c} = {a * b * c} mm³ = {fr(V, 6)} m³.",
            f"**La poussée.** Pa = ρ eau × V × g = 1 000 × {fr(V, 6)} × 9,81 = {fr(Pa, 2)} N.",
            f"**Ce que cela apprend.** Le matériau ({mat[0]}) n'intervient pas : seule compte la place occupée dans "
            "l'eau. Il servirait pour savoir si le bloc coule (poids comparé à la poussée).",
        ],
        "indice": "Pa = ρ FLUIDE × V immergé × g, en unités SI (m³).",
    }
'''

# ===========================================================================
# 6. QUIZ — nouvelle catégorie « Statique des fluides »
#    positions de la bonne réponse : 2, 0, 3, 1, 2, 3, 0, 1
# ===========================================================================
QUIZ_FLUIDES = [
    ("À quelle profondeur d'eau (1 000 kg/m³, g = 9,81 m/s²) la pression relative atteint-elle environ 1 bar ?",
     ["1 m", "100 m", "Environ 10 m", "0,1 m"], 2,
     "ρ g h = 10⁵ Pa → h = 10⁵ / (1 000 × 9,81) ≈ 10,2 m. Environ 1 bar tous les 10 m d'eau.", "Calcul"),
    ("Trois récipients de formes différentes sont remplis d'eau jusqu'à la même hauteur. Où la pression au fond "
     "est-elle la plus grande ?",
     ["Elle est la même dans les trois", "Dans le plus large", "Dans le plus étroit", "Dans celui qui contient le plus "
      "d'eau"], 0,
     "p = p0 + ρ g h ne dépend que de la profondeur, pas de la forme ni de la quantité de liquide.", "Piège"),
    ("Une presse a un petit piston Ø10 mm et un grand piston Ø100 mm. Pour 100 N sur le petit piston, le grand "
     "fournit :",
     ["1 000 N", "100 N", "100 000 N", "10 000 N"], 3,
     "Rapport des surfaces (100 / 10)² = 100 → 100 × 100 = 10 000 N. 1 000 N serait le rapport des diamètres.",
     "Calcul"),
    ("Un vérin rentre (la tige rentre dans le corps). Sous la même pression, son effort est :",
     ["Le même qu'en sortie", "Plus faible qu'en sortie : la tige réduit la surface utile", "Plus fort qu'en sortie",
      "Nul"], 1,
     "En rentrée, la pression agit sur la surface annulaire S − s : la tige en occupe une partie.", "Base"),
    ("Pourquoi néglige-t-on ρ g h dans un circuit hydraulique industriel ?",
     ["Parce que l'huile n'a pas de masse", "Parce que la pression atmosphérique l'annule",
      "Parce qu'il est très petit devant la pression du circuit (moins d'un millième)", "Parce que l'huile est compressible"], 2,
     "Exemple : 1 m d'huile à 850 kg/m³ donne ≈ 0,083 bar, contre 100 bar dans le circuit : moins de 0,1 %.",
     "Intermédiaire"),
    ("Une paroi verticale retient une hauteur d'eau h. Où s'applique la résultante des forces de pression ?",
     ["À mi-hauteur", "À la surface", "Au fond", "À h/3 au-dessus du fond"], 3,
     "La pression croît linéairement de 0 à ρ g h : répartition triangulaire, résultante au tiers de la hauteur, "
     "côté du fond.", "Intermédiaire"),
    ("Un bloc d'acier et un bloc de bois de même volume sont maintenus entièrement immergés dans l'eau. Lequel "
     "reçoit la plus grande poussée d'Archimède ?",
     ["Ils reçoivent la même poussée", "Le bloc d'acier", "Le bloc de bois", "Cela dépend de la profondeur"], 0,
     "La poussée vaut le poids du volume d'eau déplacé : même volume, même poussée, quels que soient la masse et "
     "le matériau.", "Piège"),
    ("Si l'on double la hauteur d'eau dans une cuve, l'effort sur une paroi verticale est :",
     ["Doublé", "Multiplié par 4", "Inchangé", "Multiplié par 8"], 1,
     "F = ρ g L h² / 2 : l'effort croît comme h². Doubler h multiplie l'effort par 4.", "Calcul"),
]
