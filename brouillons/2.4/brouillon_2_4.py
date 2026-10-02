# -*- coding: utf-8 -*-
# BROUILLON — fiche 2.4 « GPS, compléments : maximum et minimum de matière, zone projetée, état libre,
# références spécifiées » (référentiel S6.1.2). Rien de ceci n'est encore dans app.py.
#
# Sources des valeurs utilisées :
# - trous de passage pour vis (ISO 273, série moyenne) : M6 → 6,6 ; M8 → 9 ; M10 → 11 ; M12 → 13,5 mm ;
# - tolérances H13 : table ISO 286 de l'application (TABLE_IT) — IT13 = 220 µm (6-10 mm), 270 µm (10-18 mm) ;
# - normes citées : ISO 8015 (principe d'indépendance), ISO 2692 (exigences du maximum et du minimum de
#   matière), ISO 1101 (tolérancement géométrique, zone projetée), ISO 10579 (pièces non rigides, état libre),
#   ISO 5459 (références et systèmes de références), ISO 14405-1 (exigence de l'enveloppe).
# - Toutes les autres valeurs (tolérances de position, écarts mesurés, longueurs) sont des données d'énoncé.
import math

# ===========================================================================
# 1. FIGURES
# ===========================================================================

def mmr_bonus():
    """Trou de passage plus grand → la vis passe même si le trou est plus décalé : le bonus de Ⓜ.
    Vis, trou et décalage dessinés à la MÊME échelle (le jeu est exagéré pour être visible)."""
    p = [_k_defs(), _txt(30, 24, "Maximum de matière Ⓜ : plus le trou est grand, plus il peut être décalé", 13, TRAIT, "start", True)]
    cadres = ((30, "TROU AU PLUS PETIT : Ø11,00", 0.0, "décalage permis : 0,2 mm (zone Ø0,4)"),
              (275, "TROU MOYEN : Ø11,12", 0.12, "décalage permis : 0,26 mm (zone Ø0,52)"),
              (520, "TROU AU PLUS GRAND : Ø11,27", 0.27, "décalage permis : 0,335 mm (zone Ø0,67)"))
    rv, kj = 26, 50  # rayon dessiné de la vis Ø10 ; px par mm de jeu
    for x0, titre, bonus, legende in cadres:
        cx, cy = x0 + 82, 150
        p.append(f"<rect x='{x0}' y='40' width='225' height='230' rx='8' fill='#ffffff' stroke='{ALESAGE}' stroke-width='2'/>")
        p.append(_txt(x0 + 112, 62, titre, 11, ALESAGE, "middle", True))
        rt = rv + (1.0 + bonus) / 2 * kj           # rayon du trou : vis + jeu radial
        dec = (0.4 + bonus) / 2 * kj                # décalage permis (rayon de la zone)
        # vis à la position exacte
        p.append(f"<circle cx='{cx}' cy='{cy}' r='{rv}' fill='#fde68a' stroke='{ARBRE}' stroke-width='1.6'/>")
        p.append(_txt(cx, cy + 18, "vis", 10, ARBRE, "middle", True))
        # trou réel décalé au maximum permis, avec son centre
        p.append(f"<g><circle cx='{cx + dec:.1f}' cy='{cy}' r='{rt:.1f}' fill='none' stroke='{TRAIT}' stroke-width='2.4'/>"
                 f"<line x1='{cx + dec - 5:.1f}' y1='{cy}' x2='{cx + dec + 5:.1f}' y2='{cy}' stroke='{TRAIT}' stroke-width='1.6'/>"
                 f"<line x1='{cx + dec:.1f}' y1='{cy - 5}' x2='{cx + dec:.1f}' y2='{cy + 5}' stroke='{TRAIT}' stroke-width='1.6'/>"
                 f"<animateTransform attributeName='transform' type='translate' values='0,0; {-dec:.1f},0; 0,0' dur='3s' repeatCount='indefinite'/></g>")
        # jeu restant côté gauche (constant : 0,3 mm)
        p.append(f"<line x1='{cx - rv - 0.3 * kj:.1f}' y1='{cy}' x2='{cx - rv:.1f}' y2='{cy}' stroke='{OK}' stroke-width='3'/>")
        p.append(f"<line x1='{cx - rv - 8:.1f}' y1='{cy - 4}' x2='{x0 + 30}' y2='{cy - 72}' stroke='{OK}' stroke-width='1'/>")
        p.append(_txt(x0 + 30, cy - 76, "jeu restant", 9, OK, "middle", True))
        # loupe : la zone où le centre a le droit d'être
        lx, ly, kz = x0 + 184, 110, 50
        p.append(f"<circle cx='{lx}' cy='{ly}' r='{(0.4 + bonus) / 2 * kz:.1f}' fill='#dcfce7' stroke='{OK}' stroke-width='1.4'/>")
        p.append(f"<circle cx='{lx + (0.4 + bonus) / 2 * kz:.1f}' cy='{ly}' r='2.5' fill='{TRAIT}'/>")
        p.append(_txt(lx, ly + 26, "zone où le", 9, OK, "middle"))
        p.append(_txt(lx, ly + 37, "centre peut être", 9, OK, "middle"))
        p.append(_txt(x0 + 112, 246, legende, 10, OK, "middle", True))
    p.append(_txt(30, 288, "Jaune : la vis M10, à sa place. Noir : le trou réel, décalé au maximum permis (croix = son centre). Vert : zone où ce centre a le droit d'être.", 10, FIN))
    p.append(f"<rect x='30' y='298' width='715' height='52' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 320, "Le jeu restant est le même dans les trois cas : le trou plus grand « paie » lui-même son décalage supplémentaire.", 12, TRAIT, "start", True))
    p.append(_txt(46, 340, "Le jeu est exagéré sur le dessin ; le jeu restant (0,3 mm) est la part réservée aux défauts de l'autre pièce.", 11, FIN))
    return _svg("".join(p), 775, 364)


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


def zone_projetee():
    p = [_k_defs(), _txt(30, 24, "Zone projetée Ⓟ : l'axe compte là où passe la pièce suivante", 13, TRAIT, "start", True)]
    # carter avec trou taraudé incliné, goujon qui dépasse, pièce assemblée au-dessus
    p.append(f"<rect x='60' y='190' width='260' height='70' fill='#cbd5e1' stroke='{TRAIT}' stroke-width='1.6'/>")
    p.append(_txt(70, 278, "carter (pièce cotée)", 10, FIN))
    p.append(f"<rect x='60' y='110' width='260' height='60' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.6' opacity='0.9'/>")
    p.append(_txt(70, 104, "pièce assemblée", 10, FIN))
    p.append(f"<rect x='176' y='110' width='28' height='60' fill='#ffffff' stroke='{TRAIT}' stroke-width='1.2'/>")
    p.append(_txt(212, 140, "trou de passage", 9, FIN))
    p.append(_txt(70, 300, "zone projetée sur 40 mm (= épaisseur de la pièce assemblée)", 10, ALERTE))
    # goujon incliné
    p.append(f"<g><line x1='190' y1='252' x2='206' y2='92' stroke='{ARBRE}' stroke-width='12' stroke-linecap='round'/>"
             "<animateTransform attributeName='transform' type='rotate' values='0 190 252; 1.5 190 252; 0 190 252' dur='3s' repeatCount='indefinite'/></g>")
    p.append(_txt(214, 88, "goujon", 10, ARBRE, "start", True))
    # zones : dans le trou (petite), projetée (au-dessus, en pointillé)
    p.append(f"<rect x='181' y='190' width='18' height='70' fill='none' stroke='{OK}' stroke-width='2' stroke-dasharray='4 3'/>")
    p.append(f"<rect x='181' y='110' width='18' height='60' fill='none' stroke='{ALERTE}' stroke-width='2.4' stroke-dasharray='4 3'>"
             "<animate attributeName='opacity' values='1;0.4;1' dur='1.6s' repeatCount='indefinite'/></rect>")
    p.append(_txt(160, 230, "zone dans le trou", 9, OK, "end", True))
    p.append(_txt(160, 150, "zone projetée Ⓟ", 9, ALERTE, "end", True))
    x0 = 380
    p.append(f"<rect x='{x0}' y='44' width='380' height='216' rx='6' fill='#ffffff' stroke='{FIN}'/>")
    for i, (t, g, c) in enumerate((("Le problème :", True, TRAIT),
                                   ("un trou taraudé un peu penché se tient dans sa", False, TRAIT),
                                   ("tolérance sur sa propre profondeur. Mais le goujon", False, TRAIT),
                                   ("prolonge cette inclinaison, et c'est plus haut, dans", False, TRAIT),
                                   ("le trou de la pièce suivante, que l'écart grandit.", False, TRAIT),
                                   ("", False, TRAIT),
                                   ("La réponse : Ⓟ suivi de la longueur de projection", True, ALERTE),
                                   ("(l'épaisseur de la pièce assemblée), ex. ⊥ Ø0,1 Ⓟ 40 A :", False, TRAIT),
                                   ("la zone s'applique au-dessus de la surface, sur 40 mm.", False, TRAIT))):
        if t:
            p.append(_txt(x0 + 14, 66 + 21 * i, t, 12, c, "start", g))
    p.append(f"<rect x='30' y='310' width='730' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 332, "Ⓟ sert là où un élément inséré (goujon, vis, pion) sort de la pièce cotée et traverse la suivante.", 12, TRAIT))
    return _svg("".join(p), 790, 358)


def lmr_etat_libre():
    p = [_k_defs(), _txt(30, 24, "Minimum de matière Ⓛ et état libre Ⓕ : deux autres situations", 13, TRAIT, "start", True)]
    for x0, titre, c in ((30, "Ⓛ : GARANTIR UNE PAROI MINIMALE", ALESAGE), (410, "Ⓕ : PIÈCE QUI SE DÉFORME SOUS SON POIDS", OK)):
        p.append(f"<rect x='{x0}' y='40' width='360' height='230' rx='8' fill='#ffffff' stroke='{c}' stroke-width='2'/>")
        p.append(_txt(x0 + 180, 62, titre, 11, c, "middle", True))
    # Ⓛ : trou près d'un bord, paroi minimale
    p.append(f"<rect x='60' y='90' width='300' height='120' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.6'/>")
    p.append(f"<g><circle cx='300' cy='150' r='34' fill='#ffffff' stroke='{TRAIT}' stroke-width='2'/>"
             "<animateTransform attributeName='transform' type='translate' values='0,0; 10,0; 0,0' dur='3s' repeatCount='indefinite'/></g>")
    p.append(f"<line x1='334' y1='150' x2='360' y2='150' stroke='{ALERTE}' stroke-width='3'/>")
    p.append(_txt(347, 136, "paroi", 9, ALERTE, "middle", True))
    p.append(_txt(210, 232, "le pire cas pour la paroi : le trou le plus GRAND", 10, TRAIT, "middle"))
    p.append(_txt(210, 250, "(minimum de matière) et le plus décalé vers le bord", 10, TRAIT, "middle"))
    # Ⓕ : bague mince, libre (ovale) et maintenue (ronde)
    p.append(f"<ellipse cx='520' cy='150' rx='62' ry='46' fill='none' stroke='{OK}' stroke-width='3'>"
             "<animate attributeName='ry' values='46;54;46' dur='3s' repeatCount='indefinite'/></ellipse>")
    p.append(_txt(520, 222, "à l'état libre", 10, OK, "middle", True))
    p.append(f"<circle cx='680' cy='150' r='52' fill='none' stroke='{TRAIT}' stroke-width='3'/>")
    for a in range(0, 360, 90):
        r_ = math.radians(a)
        p.append(f"<rect x='{680 + 58 * math.cos(r_) - 4:.0f}' y='{150 + 58 * math.sin(r_) - 4:.0f}' width='8' height='8' fill='{FIN}'/>")
    p.append(_txt(680, 222, "maintenue (montée)", 10, TRAIT, "middle", True))
    p.append(_txt(680, 86, "appuis du montage de contrôle", 9, FIN, "middle"))
    p.append(_txt(600, 250, "joints, pièces minces, plastiques", 10, FIN, "middle"))
    p.append(f"<rect x='30' y='282' width='740' height='52' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 304, "Ⓛ : paroi garantie au pire cas (trou au plus grand) ; un trou plus petit reçoit un bonus de position.", 12, TRAIT))
    p.append(_txt(46, 324, "Ⓕ : sur un plan marqué ISO 10579-NR (pièce contrôlée maintenue), Ⓕ signale ce qui se vérifie à l'état libre.", 12, FIN))
    return _svg("".join(p), 800, 348)


def references_specifiees():
    p = [_k_defs(), _txt(30, 24, "Références spécifiées : de la surface réelle à l'élément de référence idéal", 13, TRAIT, "start", True)]
    cadres = ((30, "RÉFÉRENCE SIMPLE", ALESAGE), (275, "RÉFÉRENCE COMMUNE A-B", ARBRE), (520, "SYSTÈME A | B | C", OK))
    for x0, titre, c in cadres:
        p.append(f"<rect x='{x0}' y='40' width='225' height='220' rx='8' fill='#ffffff' stroke='{c}' stroke-width='2'/>")
        p.append(_txt(x0 + 112, 62, titre, 11, c, "middle", True))
    # simple : surface réelle ondulée + plan tangent
    pts = " ".join(f"{50 + i * 9},{170 + 6 * math.sin(i * 0.9)}" for i in range(21))
    p.append(f"<polyline points='{pts}' fill='none' stroke='{TRAIT}' stroke-width='2.4'/>")
    p.append(f"<line x1='45' y1='{170 + 6:.0f}' x2='240' y2='{170 + 6:.0f}' stroke='{ALESAGE}' stroke-width='2' stroke-dasharray='6 4'>"
             "<animate attributeName='opacity' values='1;0.3;1' dur='2s' repeatCount='indefinite'/></line>")
    p.append(f"<rect x='50' y='130' width='180' height='34' fill='#e2e8f0' opacity='0.7'/>")
    p.append(_txt(142, 150, "matière", 9, FIN, "middle"))
    p.append(_txt(142, 120, "surface réelle (imparfaite)", 10, TRAIT, "middle"))
    p.append(_txt(142, 206, "plan idéal associé =", 10, ALESAGE, "middle", True))
    p.append(_txt(142, 220, "la référence A", 10, ALESAGE, "middle", True))
    # commune : deux portées d'un arbre → un seul axe
    for x in (300, 430):
        p.append(f"<rect x='{x}' y='130' width='50' height='40' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.6'/>")
    p.append(f"<rect x='350' y='140' width='80' height='20' fill='#e2e8f0' stroke='{TRAIT}'/>")
    p.append(f"<line x1='285' y1='150' x2='495' y2='150' stroke='{ARBRE}' stroke-width='2' stroke-dasharray='8 4'/>")
    p.append(_txt(325, 120, "A", 12, TRAIT, "middle", True))
    p.append(_txt(455, 120, "B", 12, TRAIT, "middle", True))
    p.append(_txt(387, 206, "un seul axe commun aux deux", 10, ARBRE, "middle", True))
    p.append(_txt(387, 220, "portées : la référence A-B", 10, ARBRE, "middle", True))
    # système : trois plans orthogonaux, ordre
    p.append(f"<rect x='560' y='100' width='140' height='90' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.6'/>")
    for x_, y_ in ((580, 194), (630, 194), (680, 194)):
        p.append(f"<circle cx='{x_}' cy='{y_}' r='4' fill='{OK}'/>")
    for x_, y_ in ((556, 120), (556, 170)):
        p.append(f"<circle cx='{x_}' cy='{y_}' r='4' fill='{ALESAGE}'/>")
    p.append(f"<circle cx='630' cy='96' r='4' fill='{ARBRE}'/>")
    p.append(_txt(712, 198, "A", 11, OK, "start", True))
    p.append(_txt(546, 148, "B", 11, ALESAGE, "end", True))
    p.append(_txt(642, 94, "C", 11, ARBRE, "start", True))
    p.append(_txt(630, 210, "A : 3 points d'appui (primaire)", 10, OK, "middle", True))
    p.append(_txt(630, 224, "B : 2 points, C : 1 point", 10, OK, "middle", True))
    p.append(_txt(630, 240, "l'ordre = l'ordre de mise en position", 10, FIN, "middle"))
    p.append(f"<rect x='30' y='272' width='715' height='52' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 294, "On ne mesure jamais « par rapport à la surface » : on lui associe un élément idéal (plan, axe), selon ISO 5459.", 12, TRAIT))
    p.append(_txt(46, 314, "Pour une surface brute, on ne prend que quelques zones de contact : les cibles de référence.", 12, FIN))
    return _svg("".join(p), 775, 338)


# --- figure à curseurs : le bonus de Ⓜ sur un trou Ø11 H13, ⌖ Ø0,4 Ⓜ
def dyn_bonus_mm(D=11.12, e=0.23):
    """Trou de passage Ø11 H13 (11,00 à 11,27), localisation ⌖ Ø0,4 Ⓜ : conformité avec et sans Ⓜ."""
    Dmin, t = 11.00, 0.4
    bonus = D - Dmin
    zone = t + bonus
    occ = 2 * e
    ok_m = occ <= zone + 1e-9
    ok_sans = occ <= t + 1e-9
    broche = D - 2 * e
    p = [_k_defs(), _txt(30, 24, f"Trou mesuré Ø{D:.2f}".replace(".", ",") + f", décalé de {_fr_court(e, 2)} mm de sa position exacte", 13, TRAIT, "start", True)]
    cx, cy, k = 200, 170, 90  # k : px par mm pour le dessin des zones (agrandi)
    p.append(f"<circle cx='{cx}' cy='{cy}' r='{zone / 2 * k * 2:.1f}' fill='#dcfce7' stroke='{OK}' stroke-width='1.6' stroke-dasharray='4 3'/>")
    p.append(f"<circle cx='{cx}' cy='{cy}' r='{t / 2 * k * 2:.1f}' fill='none' stroke='{ALESAGE}' stroke-width='1.6'/>")
    p.append(f"<circle cx='{cx + e * k * 2:.1f}' cy='{cy}' r='5' fill='{ALERTE if not ok_m else TRAIT}'/>")
    p.append(f"<line x1='{cx}' y1='{cy}' x2='{cx + e * k * 2:.1f}' y2='{cy}' stroke='{TRAIT}' stroke-width='1.4'/>")
    p.append(f"<circle cx='{cx}' cy='{cy}' r='3' fill='{TRAIT}'/>")
    p.append(_txt(cx, cy + zone * k + 22, f"vert : zone avec Ⓜ, Ø{_fr_court(zone, 2)}", 11, OK, "middle", True))
    p.append(_txt(cx, cy + zone * k + 38, "bleu : zone sans Ⓜ, Ø0,4", 11, ALESAGE, "middle", True))
    p.append(_txt(cx, 56, "gros point = centre réel du trou ; petit point = position exacte ; trait = décalage e", 10, FIN, "middle"))
    x0 = 420
    col = OK if ok_m else ALERTE
    p.append(f"<rect x='{x0}' y='44' width='350' height='230' rx='6' fill='#ffffff' stroke='{col}' stroke-width='1.8'/>")
    lignes = [(f"bonus = D − D min = {D:.2f}".replace(".", ",") + f" − 11,00 = {_fr_court(bonus, 2)} mm", TRAIT, False),
              (f"zone avec Ⓜ : Ø0,4 + {_fr_court(bonus, 2)} = Ø{_fr_court(zone, 2)}", OK, True),
              (f"plus petite zone contenant le centre : Ø2e = Ø{_fr_court(occ, 3)}", TRAIT, False),
              ("sans Ⓜ : " + ("conforme" if ok_sans else "REBUTÉE"), ALESAGE if ok_sans else ALERTE, True),
              ("avec Ⓜ : " + ("CONFORME" if ok_m else "REBUTÉE"), col, True),
              ("", TRAIT, False),
              (f"calibre : broche Ø10,6 à la position exacte ;", TRAIT, False),
              (f"le trou laisse passer Ø{_fr_court(broche, 3)}" + (" ≥ 10,6 : la broche entre" if broche >= 10.6 - 1e-9 else " : moins de 10,6, la broche n'entre pas"),
               col, True)]
    for i, (t_, c, g) in enumerate(lignes):
        if t_:
            p.append(_txt(x0 + 12, 70 + 25 * i, t_, 12, c, "start", g))
    p.append(_txt(30, 300, "Ø11 H13 (11,00 à 11,27, ISO 286) ; ⌖ Ø0,4 Ⓜ. Les deux tests — zone avec bonus et calibre — donnent toujours le même verdict.", 10, FIN))
    return _svg("".join(p), 790, 314)


FIGURES_NOUVELLES = {
    "mmr_bonus": ("Maximum de matière Ⓜ : le bonus de position d'un trou de passage", mmr_bonus),
    "mmr_calibre": ("Le calibre fonctionnel : la taille virtuelle au maximum de matière", mmr_calibre),
    "zone_projetee": ("Zone de tolérance projetée Ⓟ", zone_projetee),
    "lmr_etat_libre": ("Minimum de matière Ⓛ et état libre Ⓕ", lmr_etat_libre),
    "references_specifiees": ("Références spécifiées : simple, commune, système", references_specifiees),
}
DYN_NOUVELLE = {
    "bonus_mm_curseurs": (
        "Change le diamètre réel du trou et son décalage : avec ou sans Ⓜ, le verdict change",
        dyn_bonus_mm,
        [{"nom": "D", "label": "Diamètre réel du trou D (mm)", "min": 11.0, "max": 11.27, "defaut": 11.12, "pas": 0.03},
         {"nom": "e", "label": "Décalage e du centre (mm)", "min": 0.0, "max": 0.35, "defaut": 0.23, "pas": 0.01}]),
}

# ===========================================================================
# 2. FICHE 2.4 — en FIN de bloc 2 (après la 2.3)
# ===========================================================================

FICHE_2_4 = {
    "id": "2.4",
    "titre": "GPS, compléments : maximum de matière, zone projetée, état libre, références",
    "duree": "5 h",
    "cours": """### 1. Pourquoi cette fiche

La fiche 2.3 a posé les bases : le cadre de tolérance, les quatre familles, les références, et le
**principe d'indépendance** (ISO 8015) — par défaut, une cote et une tolérance géométrique se vérifient
**séparément**. Ce principe est sain, mais il est parfois trop sévère, et parfois insuffisant :

- **trop sévère** pour un trou de passage de vis : il rebute des pièces qui s'assembleraient très bien ;
- **insuffisant** pour un goujon, une pièce mince, ou une surface de référence brute.

Les **modificateurs** (une lettre entourée dans le cadre) règlent ces cas. Ils sont de deux natures :

- **Ⓜ** (maximum de matière) et **Ⓛ** (minimum de matière), comme l'exigence de l'enveloppe **Ⓔ** vue en
  2.3, sont des **exceptions déclarées** au principe d'indépendance : ils **lient la taille et la
  géométrie**. Sans symbole, l'indépendance reste la règle.
- **Ⓟ** (zone projetée) et **Ⓕ** (état libre) sont d'une autre nature : Ⓟ **déplace** la zone de
  tolérance, Ⓕ précise **dans quel état** (libre ou maintenu) on contrôle la pièce.

En 2.3, tu as vu Ⓜ comme une formule de bonus. Ici, on comprend **pourquoi** cette formule est juste.

### 2. Le maximum de matière Ⓜ : garantir l'assemblage au pire cas

[[FIG:mmr_bonus]]

**Le vocabulaire.** Une pièce est **au maximum de matière** quand elle contient le plus de métal permis :

- un **trou** est au maximum de matière quand il est **au plus petit** (D min) ;
- un **arbre** est au maximum de matière quand il est **au plus gros** (d max).

*Le test de la balance : pèse la plaque. Un trou, c'est du vide ; le métal est **autour**. Plus le trou est
petit, plus il reste de métal, plus la plaque est lourde. « Maximum de matière » = **la pièce la plus
lourde** : plaque aux trous les plus petits, arbre le plus gros.* ⚠️ « Maximum » ne veut pas dire « plus
grand trou » : pour un trou, maximum de matière = **plus petit** diamètre.

C'est le **pire cas pour l'assemblage** : le trou le plus petit et l'arbre le plus gros laissent le
moins de jeu. Imagine le pire montage possible : le trou le plus petit permis, décalé du maximum permis,
face à la vis. Si **celui-là** s'assemble encore, tous les autres s'assembleront.

*Notations : D (majuscule) pour un trou, d (minuscule) pour un arbre ; t = la tolérance écrite dans le
cadre.*

**Le sens physique, sur un exemple.** Une plaque est fixée par 4 vis M10 dans des trous de passage
**Ø11 H13** (Ø11 : trou de passage de la série moyenne, ISO 273 ; H13 : 11,00 à 11,27 mm, ISO 286). La
position des trous est tolérancée **⌖ Ø0,4 Ⓜ A B C** (A : face d'appui ; B et C : deux chants usinés,
qui fixent les directions x et y).

- Un trou **au plus petit** (Ø11,00) laisse peu de place autour de la vis : sa position doit être tenue
  dans **Ø0,4**.
- Un trou **plus grand** (Ø11,12) laisse **0,12 mm de jeu en plus** autour de la vis : il peut être
  **décalé davantage** sans que la vis cesse de passer. Sa zone de position devient **Ø0,4 + 0,12 =
  Ø0,52**.
- Au plus grand (Ø11,27) : **Ø0,4 + 0,27 = Ø0,67**.

*Pourquoi ajouter 0,12 tel quel ? Le trou passe de Ø11,00 à Ø11,12 : il s'élargit de 0,06 mm **de chaque
côté**. Son centre peut donc aller 0,06 mm plus loin **dans n'importe quelle direction** sans que le bord
touche la vis. Le cercle où le centre a le droit d'être grossit de 0,06 en rayon, donc de **0,12 en
diamètre**. Gain de diamètre du trou = gain de diamètre de la zone.*

> **Avec Ⓜ, la tolérance de position grandit quand la pièce s'écarte du maximum de matière :**
> trou : **t disponible = t + (D réel − D min)** · arbre : **t disponible = t + (d max − d réel)**

Ce supplément s'appelle le **bonus**. Il n'est pas un cadeau : c'est exactement le jeu supplémentaire
que la pièce apporte elle-même.

*D réel : pour un trou imparfait (ovale, tordu), c'est le diamètre du plus grand cylindre parfait qui y
entre — le calibre, lui, en tient compte tout seul.*

### 3. Pourquoi c'est juste : le calibre

[[FIG:mmr_calibre]]

**D'où vient le Ø0,4 ?** Entre une vis Ø10 et un trou Ø11,00, il y a 1 mm de jeu sur le diamètre. Le
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
mm (Pythagore : le décalage réel, en diagonale) ; plus petite zone contenant le centre : 2e ≈ Ø0,466.*

- *Sans Ⓜ : 0,466 > 0,4 → la pièce est **rebutée**.*
- *Avec Ⓜ : 0,466 ≤ 0,4 + 0,12 = 0,52 → **conforme**. Le calibre confirme : 11,12 − 0,466 ≈ 10,65 ≥ 10,6.*

Cette pièce s'assemble parfaitement : sans Ⓜ, on l'aurait jetée pour rien.

[[DYN:bonus_mm_curseurs]]

**Le gain pour l'atelier.** Le bonus élargit la tolérance de position dès que les trous ne sont pas au
plus petit : l'atelier peut accepter plus de pièces, ou percer avec des moyens moins précis, **sans risque
pour l'assemblage**. C'est un gain de coût obtenu par la seule cotation.

**Ce que Ⓜ ne change pas.** La taille reste contrôlée : le diamètre doit rester entre 11,00 et 11,27. Le
calibre vérifie la position ; un tampon ou un alésomètre vérifie la taille. C'est le **tolérancement par
gabarits** du référentiel.

**Quand ne pas mettre Ⓜ.** Quand la fonction n'est **pas** un assemblage avec jeu : un alésage de
centrage, un ajustement serré, une position qui règle un mécanisme (un engrenage, un capteur). *Un
roulement monté dans un alésage de centrage : si l'alésage est plus grand, le roulement flotte. Le jeu en
plus n'aide pas, il aggrave.* Ⓜ n'a de sens que si un trou plus grand **rend service** à l'assemblage.

### 4. Le minimum de matière Ⓛ : garantir une matière minimale

[[FIG:lmr_etat_libre]]

Ⓛ suit la même logique que Ⓜ, mais pour l'autre extrême : le **minimum de matière** (trou au plus
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
sans danger. Ⓛ garantit **la même paroi** et accepte ces trous — exactement comme Ⓜ pour un assemblage.

### 5. La zone projetée Ⓟ : l'axe là où passe la pièce suivante

[[FIG:zone_projetee]]

Un trou taraudé reçoit un goujon qui traverse une autre pièce. Si le trou est **un peu penché**, il peut
rester dans sa tolérance sur sa propre profondeur, mais le goujon prolonge cette inclinaison : c'est
**plus haut, dans le trou de la pièce suivante**, que l'écart grandit et que l'assemblage coince.

*Un goujon, c'est une tige filetée aux deux bouts, vissée dans le bâti. Pense à un piquet planté un peu de
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
centrée sur la position exacte.*

### 6. L'état libre Ⓕ : les pièces qui se déforment

*Pense à un joint torique : posé sur la table, il s'avachit en ovale ; enfilé dans sa gorge, il redevient
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
montable par l'opérateur.*

### 7. Les références spécifiées

[[FIG:references_specifiees]]

La fiche 2.3 a introduit les références A, B, C. Deux précisions (ISO 5459) :

- **On ne mesure jamais « par rapport à une surface »** : pose la pièce sur le marbre ; sa face bosselée
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
  sol inégal —, pour que la mise en position soit répétable.

### 8. Les erreurs classiques

1. **Croire que Ⓜ relâche la fonction** : il n'accepte que ce qui passe le calibre. Et la taille du
   trou reste contrôlée à part.
2. **Se tromper de maximum de matière** : pour un **trou**, c'est le **plus petit** diamètre ; pour un
   **arbre**, le **plus gros**.
3. **Calculer le bonus à partir du nominal ou du maximum** : bonus = écart **par rapport au maximum de
   matière** (D réel − D min pour un trou).
4. **Mettre Ⓜ sur un centrage ou un ajustement** : un trou plus grand ne compense rien quand la fonction
   n'est pas un jeu d'assemblage.
5. **Comparer e (et non 2e) au diamètre de la zone** : la zone est un cylindre de diamètre t ; le centre
   y est si **2e ≤ t**.
6. **Oublier Ⓟ pour un goujon** : le trou taraudé est conforme, mais l'axe sort de sa tolérance plus
   haut, dans la pièce assemblée.
7. **Contrôler une pièce mince posée sur la table** quand le plan porte ISO 10579-NR : on mesure sa
   déformation, pas sa géométrie.

### 9. À retenir

- Par défaut : **indépendance** (ISO 8015). Ⓔ, Ⓜ, Ⓛ sont des **exceptions déclarées** (ils lient
  taille et géométrie) ; Ⓟ déplace la zone, Ⓕ fixe l'état de contrôle.
- **Maximum de matière** : trou au plus petit, arbre au plus gros = **pire cas pour l'assemblage**.
- **Ⓜ** : t disponible = t + écart au maximum de matière (trou : D réel − D min). **Le bonus n'est pas un
  cadeau : c'est le jeu que la pièce apporte elle-même.** Le **calibre** (broches à la taille virtuelle
  D min − t, aux positions exactes) en donne le sens physique. Pour un arbre, le calibre est une **bague**
  de diamètre d max + t.
- **Ⓛ** : même paroi garantie au pire cas, avec un bonus pour les trous plus petits.
- **Ⓟ** + longueur de projection : la zone est **projetée** là où passe la pièce suivante (goujons, vis).
- Par défaut, contrôle à l'**état libre** (pièce rigide). Plan marqué **ISO 10579-NR** : pièce non rigide
  contrôlée **maintenue** ; **Ⓕ** marque ce qui reste à l'état libre.
- **Référence** = élément **idéal associé** à la surface réelle ; référence commune **A-B** ; système
  **A | B | C** dans l'ordre de mise en position ; **cibles** sur les surfaces brutes.
""",
    "formules": """
**Maximum de matière** — trou : D min · arbre : d max (pire cas pour l'assemblage)

**Bonus Ⓜ** — trou : t disponible = t + (D réel − D min) · arbre : t disponible = t + (d max − d réel)

**Taille virtuelle (calibre)** — trou : broche D min − t · arbre : bague d max + t

**Conformité d'une position** — centre décalé de (Δx, Δy) : e = √(Δx² + Δy²) ; conforme si 2e ≤ t disponible

**Bonus Ⓛ** — trou : t disponible = t + (D max − D réel) · arbre : t disponible = t + (d réel − d min)

**Zone projetée Ⓟ** — la zone s'applique au-dessus de la surface, sur la longueur de projection qui suit Ⓟ
(ex. ⊥ Ø0,1 Ⓟ 40 A)

**Normes** — ISO 8015 (indépendance, pièce rigide) · ISO 2692 (Ⓜ, Ⓛ) · ISO 1101 (Ⓟ) · ISO 10579 (pièces non
rigides, Ⓕ) · ISO 5459 (références)
""",
    "exemple": """
### Cas industriel — Les capots rebutés qui s'assemblaient très bien

**Le symptôme.** Un fournisseur livre des capots de machine percés de 6 trous Ø9 H13 (trous de passage
pour vis M8, ISO 273 ; 9,00 à 9,22 mm, ISO 286), localisés **⌖ Ø0,3 A B C**, **sans Ⓜ**. Au contrôle
d'entrée, une partie des capots est rebutée pour position hors tolérance. Pourtant, au montage d'essai,
tous les capots rebutés s'assemblent sans difficulté.

**L'analyse.** Les trous rebutés sont presque tous percés **au-dessus de leur minimum** (vers 9,10 à 9,20
mm). Sans Ⓜ, leur tolérance de position reste Ø0,3, même si leur diamètre laisse beaucoup plus de jeu
autour de la vis. Le plan rebutait donc des pièces **fonctionnellement bonnes**.

**La correction.** La fonction est un assemblage avec jeu : on cote **⌖ Ø0,3 Ⓜ A B C**. Un trou à 9,15 mm
dispose alors de Ø0,3 + 0,15 = **Ø0,45**. Le contrôle se fait au **calibre** (broches Ø9,00 − 0,3 = Ø8,7
aux positions exactes) : rapide, sans calcul, et il garantit que les vis passeront, si la pièce en face
respecte sa propre tolérance. La taille des trous reste contrôlée à part (9,00 à 9,22).

**Ce que le cas apprend.** La cotation par défaut (indépendance) n'est pas toujours la plus juste. Quand
la fonction est un **assemblage avec jeu**, Ⓜ traduit exactement cette fonction : il accepte tout ce
qui s'assemble, et rien d'autre. Le gain de coût vient de la cotation, pas de la machine.
""",
    "exercice": """
### Exercice — Platine de fixation d'un moteur

Une platine est fixée par 4 vis M10 dans des trous **Ø11 H13** (11,00 à 11,27 mm). Leur position est
cotée **⌖ Ø0,4 Ⓜ A B C** (A : face d'appui ; B, C : deux chants, qui fixent x et y).

**1.** Quel est le diamètre au maximum de matière de ces trous ? Pourquoi est-ce le pire cas pour
l'assemblage ?

**2.** Un trou mesure Ø11,20. Quelle tolérance de position dispose-t-il ?

**3.** Son centre est décalé de Δx = 0,25 mm et Δy = 0,15 mm. Le trou est-il conforme ? Le serait-il sans
Ⓜ ?

**4.** Quel diamètre faut-il donner aux broches du calibre de contrôle ? Vérifiez la question 3 avec le
calibre.

**5.** Sous la platine, un trou taraudé du bâti reçoit un goujon qui traverse la platine (épaisseur
20 mm). Quel modificateur faut-il sur la perpendicularité de ce taraudage (référence A : face d'appui du
bâti), et pourquoi ?

**6.** On veut aussi garantir une paroi minimale entre un des trous et le bord de la platine, en
acceptant les trous plus petits un peu plus décalés. Quel modificateur traduit ce besoin ?
""",
    "corrige": """
### Corrigé, en six temps

#### 1. Ce que dit l'énoncé

Des trous de passage (assemblage avec jeu), une localisation au maximum de matière, une mesure réelle à
juger. Puis deux besoins voisins : un goujon qui traverse une pièce, une paroi à garantir.

#### 2. Quelle règle, et pourquoi

> Trou au maximum de matière = **D min**. Avec Ⓜ : **t disponible = t + (D réel − D min)**. Conforme si
> **2e ≤ t disponible**. Calibre : broches à la **taille virtuelle D min − t**.

#### 3. Les conversions

Toutes les longueurs en mm. Le décalage e se calcule à partir de Δx et Δy, puis on compare 2e au
diamètre de la zone.

#### 4. Le remplacement

t disponible = 0,4 + (11,20 − 11,00). e = √(0,25² + 0,15²). Calibre : 11,00 − 0,4. Broche qui passe : 11,20 − 2e.

#### 5. Le calcul

**1.** **D min = 11,00 mm**. Le trou le plus petit laisse le moins de jeu autour de la vis : c'est le cas
le plus défavorable pour l'assemblage.

**2.** Bonus = 11,20 − 11,00 = 0,20 mm ; **t disponible = Ø0,60**.

**3.** e = √(0,0625 + 0,0225) = √0,085 ≈ 0,292 mm ; plus petite zone contenant le centre : 2e ≈ **Ø0,583**. Avec Ⓜ : 0,583 ≤ 0,60 →
**conforme**. Sans Ⓜ : 0,583 > 0,4 → il serait **rebuté**.

**4.** Broches à **Ø11,00 − 0,4 = Ø10,6**, aux positions exactes. Le trou laisse passer une broche de
11,20 − 0,583 ≈ **Ø10,62** ≥ 10,6 : le calibre entre, même verdict.

**5.** **Ⓟ**, suivi de la longueur de projection **20** (épaisseur de la platine) : **⊥ Ø… Ⓟ 20 A**. Le
goujon prolonge l'inclinaison du taraudage ; c'est dans le trou de la platine que l'écart compte.

**6.** **Ⓛ** (minimum de matière) : le risque n'est pas que ça ne passe pas, mais qu'il ne reste pas
assez de matière. La paroi est garantie au pire cas (trou au plus grand, décalé vers le bord) ; Ⓛ accorde
un bonus de position aux trous plus petits, qui laissent plus de métal.

#### 6. La vérification

**Deux méthodes, un verdict** : zone avec bonus (0,583 ≤ 0,60) et calibre (10,62 ≥ 10,6) concordent, et
c'est toujours le cas — le calibre n'est que la traduction physique du bonus. **Bon sens** : la marge est
faible (0,017 mm) ; un trou au plus petit avec le même décalage serait rebuté, ce qui est normal : il
laisserait moins de jeu à la vis.
""",
}

# ===========================================================================
# 3. MÉTHODE
# ===========================================================================
MTH_2_4 = ("2.4", "Juger une localisation avec le maximum de matière Ⓜ", [
    "**Vérifier que la fonction est un assemblage avec jeu** (trou de passage, vis, pion libre) : "
    "sinon, Ⓜ n'a pas de sens.",
    "**Repérer le maximum de matière** : D min pour un trou, d max pour un arbre.",
    "**Calculer le bonus** (trou : D réel − D min) et la tolérance disponible t + bonus.",
    "**Calculer le décalage** e = √(Δx² + Δy²) et comparer **2e** à la tolérance disponible.",
    "**Contrôler par le calibre** : broche à la taille virtuelle D min − t, à la position exacte ; la "
    "pièce est bonne si D réel − 2e ≥ D min − t. Les deux méthodes donnent le même verdict.",
], "Trou Ø11 H13 (11,00 à 11,27), ⌖ Ø0,4 Ⓜ A B C. Mesuré Ø11,12, décalé de 0,233 mm : 2e = 0,466 ; "
   "t disponible = 0,4 + 0,12 = 0,52 → conforme (rebuté sans Ⓜ). Calibre Ø10,6 : 11,12 − 0,466 = 10,65 ≥ 10,6.")

# ===========================================================================
# 4. ATELIERS (fin de liste ATELIERS, après at165)
# ===========================================================================
ATELIERS_NOUVEAUX = [
    {
        "id": "at166",
        "chapitre": "Bloc 2",
        "titre": "Capot à trous de passage : le bonus du maximum de matière",
        "theme": "Tolérancement géométrique",
        "fiche": "2.4",
        "figure": "mmr_calibre",
        "vocabulaire": [
            ("Maximum de matière",
             "l'état où la pièce contient le plus de métal permis : trou au plus petit, arbre au plus "
             "gros. C'est le pire cas pour l'assemblage."),
            ("Bonus",
             "le supplément de tolérance de position accordé par Ⓜ quand la pièce s'écarte du maximum de "
             "matière : pour un trou, D réel − D min."),
            ("Taille virtuelle",
             "le diamètre des broches du calibre fonctionnel : D min − t pour un trou."),
        ],
        "enonce": "Un capot est fixé par des vis M8 dans des trous Ø9 H13 (trous de passage ISO 273 ; 9,00 à "
                  "9,22 mm, ISO 286). Leur position est cotée ⌖ Ø0,3 Ⓜ A B C (A : face d'appui ; B, C : deux chants). Un trou est mesuré à Ø9,15 ; "
                  "son centre est décalé de Δx = 0,18 mm et Δy = 0,12 mm de la position exacte.",
        "etapes": [
            {"type": "numerique", "label": "Diamètre au maximum de matière",
             "unite": "mm", "attendu": 9.0, "tol": 0.005,
             "consigne": "Quel est le diamètre de ces trous au maximum de matière ?",
             "indice": "Pour un trou, le maximum de matière, c'est le plus petit diamètre permis.",
             "pieges": [(9.22, "9,22 mm, c'est le trou au plus GRAND : la plaque a alors le MOINS de métal "
                               "autour. Le maximum de matière d'un trou, c'est son plus petit diamètre.")],
             "aide": "D min = 9,00 mm."},
            {"type": "numerique", "label": "Tolérance de position disponible",
             "unite": "mm", "attendu": 0.45, "tol": 0.005,
             "consigne": "Avec Ⓜ, quelle tolérance de position (diamètre de zone) dispose ce trou mesuré à "
                         "Ø9,15 ?",
             "indice": "t disponible = t + (D réel − D min).",
             "pieges": [(0.3, "0,3, c'est la tolérance au maximum de matière. Ce trou est plus grand : "
                              "il reçoit un bonus de 9,15 − 9,00."),
                        (0.37, "0,37 : tu as calculé le bonus depuis le maximum (9,22 − 9,15). Le bonus se "
                               "mesure depuis le maximum de matière : 9,15 − 9,00.")],
             "aide": "0,3 + 0,15 = Ø0,45."},
            {"type": "numerique", "label": "Plus petite zone contenant le centre",
             "unite": "mm", "attendu": 0.4327, "tol": 0.008,
             "consigne": "Calcule le diamètre de la plus petite zone, centrée sur la position exacte, qui "
                         "contient le centre du trou : 2 × √(Δx² + Δy²).",
             "indice": "√(0,18² + 0,12²), puis × 2.",
             "pieges": [(0.2163, "0,216, c'est e, le décalage. La zone est un cylindre de DIAMÈTRE t : on "
                                 "compare 2e à t.")],
             "aide": "e = √(0,0324 + 0,0144) = 0,2163 ; 2e ≈ 0,433 mm."},
            {"type": "qcm", "label": "Verdict",
             "question": "2e ≈ 0,433 mm. Le trou est-il conforme ?",
             "options": ["Rebuté : 0,433 > 0,3",
                         "Conforme avec Ⓜ (0,433 ≤ 0,45) ; il serait rebuté sans Ⓜ",
                         "Conforme dans tous les cas"], "bonne": 1,
             "indice": "Comparer 2e à la tolérance disponible avec Ⓜ, puis à 0,3.",
             "diagnostics": {0: "0,3 est la tolérance au maximum de matière. Ce trou est à 9,15 : il dispose "
                                 "de 0,45.",
                             2: "Sans Ⓜ, la zone resterait Ø0,3 et 0,433 la dépasse : c'est le bonus qui "
                                "le rend conforme."}},
            {"type": "numerique", "label": "Diamètre des broches du calibre",
             "unite": "mm", "attendu": 8.7, "tol": 0.005,
             "consigne": "Quel diamètre donner aux broches du calibre fonctionnel (taille virtuelle) ?",
             "indice": "Taille virtuelle d'un trou : D min − t.",
             "pieges": [(9.3, "9,3 = 9,00 + 0,3 : pour un trou, on retire la tolérance (D min − t). Une "
                              "broche plus grosse que le trou ne rentrerait jamais."),
                        (8.85, "8,85 : tu es parti du diamètre mesuré. Le calibre est le même pour toutes "
                               "les pièces : il part de D min.")],
             "aide": "9,00 − 0,3 = Ø8,7."},
        ],
        "corrige": {
            "enonce": "Trous Ø9 H13 (9,00 à 9,22), ⌖ Ø0,3 Ⓜ A B ; trou mesuré Ø9,15, décalé de (0,18 ; 0,12).",
            "regle": "**Trou au maximum de matière = D min.** **t disponible = t + (D réel − D min)**. "
                    "Conforme si **2e ≤ t disponible**. Calibre : **D min − t**.",
            "conversions": "Toutes les longueurs en mm.",
            "remplacement": "t = 0,3 + (9,15 − 9,00) ; e = √(0,18² + 0,12²) ; calibre 9,00 − 0,3.",
            "calcul": "**D min = 9,00** ; **t disponible = Ø0,45** ; **2e ≈ 0,433** → conforme (rebuté sans "
                     "Ⓜ) ; calibre **Ø8,7**.",
            "verification": "Par le calibre : le trou laisse passer une broche de 9,15 − 0,433 ≈ 8,717 mm ≥ "
                            "8,7 : il entre. Même verdict que par la zone.",
        },
        "a_retenir": "À retenir : avec Ⓜ, un trou plus grand que son minimum dispose d'un bonus égal à "
                     "son écart au maximum de matière ; le calibre à la taille virtuelle donne le même "
                     "verdict.",
    },
    {
        "id": "at167",
        "chapitre": "Bloc 2",
        "titre": "Goujon et pièce mince : zone projetée, état libre, minimum de matière",
        "theme": "Tolérancement géométrique",
        "fiche": "2.4",
        "figure": "zone_projetee",
        "vocabulaire": [
            ("Zone projetée Ⓟ",
             "une zone de tolérance reportée au-dessus de la surface, sur la longueur de projection : là où "
             "l'élément fileté traverse la pièce suivante."),
            ("État libre Ⓕ",
             "sur un plan marqué ISO 10579-NR (pièce non rigide contrôlée maintenue), Ⓕ signale une "
             "tolérance à vérifier sur la pièce libre."),
            ("Minimum de matière Ⓛ",
             "trou au plus grand, arbre au plus petit : le pire cas pour une épaisseur de paroi."),
        ],
        "enonce": "Un taraudage de 12 mm de profondeur reçoit un goujon qui traverse une bride de 40 mm "
                  "d'épaisseur. Sa perpendicularité est cotée Ø0,1 par rapport à A (face d'appui du carter). Mesure : l'axe du taraudage s'écarte de "
                  "0,04 mm pour 10 mm de hauteur (données d'énoncé).",
        "etapes": [
            {"type": "numerique", "label": "Écart sur la profondeur du taraudage",
             "unite": "mm", "attendu": 0.048, "tol": 0.002,
             "consigne": "De combien l'axe s'écarte-t-il sur les 12 mm du taraudage ?",
             "indice": "0,04 × 12 / 10.",
             "pieges": [(0.04, "0,04, c'est l'écart pour 10 mm. Sur 12 mm, il est proportionnellement plus "
                               "grand.")],
             "aide": "0,04 × 12 / 10 = 0,048 mm."},
            {"type": "numerique", "label": "Écart sur l'épaisseur de la bride",
             "unite": "mm", "attendu": 0.16, "tol": 0.003,
             "consigne": "De combien l'axe prolongé (le goujon) s'écarte-t-il sur les 40 mm de la bride ?",
             "indice": "0,04 × 40 / 10.",
             "pieges": [(0.048, "0,048, c'est dans le taraudage. Le goujon prolonge l'inclinaison sur toute "
                                "l'épaisseur de la bride.")],
             "aide": "0,04 × 40 / 10 = 0,16 mm."},
            {"type": "qcm", "label": "Que coter ?",
             "question": "Le taraudage tient dans Ø0,1 sur sa profondeur (0,048), mais pas sur l'épaisseur de "
                         "la bride (0,16). Comment le plan doit-il l'exprimer ?",
             "options": ["⊥ Ø0,1 Ⓟ 40 A : zone projetée sur 40 mm",
                         "⊥ Ø0,1 Ⓜ A", "⊥ Ø0,1 Ⓕ A"], "bonne": 0,
             "indice": "La zone doit être reportée là où passe la pièce suivante.",
             "diagnostics": {1: "Ⓜ donne un bonus selon le diamètre : il ne déplace pas la zone. Le "
                                 "problème ici est l'endroit où l'axe compte.",
                             2: "Ⓕ concerne les pièces qui se déforment : un taraudage dans un bâti rigide "
                                "n'en fait pas partie."}},
            {"type": "qcm", "label": "Une bague mince",
             "question": "Une bague d'étanchéité mince, sur un plan marqué ISO 10579-NR, se déforme posée sur la "
                         "table et redevient ronde montée. Quel symbole permet de limiter sa circularité telle "
                         "qu'elle est livrée, avant montage ?",
             "options": ["Ⓟ", "Ⓜ", "Ⓕ (état libre)"], "bonne": 2,
             "indice": "On veut une tolérance qui s'applique à la pièce NON maintenue.",
             "diagnostics": {0: "Ⓟ reporte une zone au-dessus d'une surface : rien à voir avec une pièce "
                                 "qui se déforme.",
                             1: "Ⓜ lie la tolérance au diamètre réel : il ne dit rien de l'état, libre ou "
                                "maintenu."}},
            {"type": "qcm", "label": "Une paroi à garantir",
             "question": "Un trou est percé près d'un bord ; il doit rester au moins une épaisseur de paroi. Quel "
                         "modificateur traduit exactement ce besoin, en acceptant les trous plus petits plus "
                         "décalés ?",
             "options": ["Ⓜ, car c'est un trou", "Ⓛ (minimum de matière)", "Aucun : l'indépendance suffit"],
             "bonne": 1,
             "indice": "Quel est le pire cas pour la paroi : trou petit ou trou grand ?",
             "diagnostics": {0: "Ⓜ protège l'assemblage (trou au plus petit). Ici, le pire cas est le trou "
                                 "au plus grand, qui mange la paroi : c'est Ⓛ.",
                             2: "L'indépendance garantit aussi la paroi (la zone vaut pour tous les "
                                "diamètres), mais elle rebute des trous plus petits qui pourraient être plus "
                                "décalés sans danger. Ⓛ leur accorde ce bonus, comme Ⓜ pour un assemblage."}},
        ],
        "corrige": {
            "enonce": "Taraudage de 12 mm, goujon traversant une bride de 40 mm, perpendicularité Ø0,1 ; axe "
                      "incliné de 0,04 mm pour 10 mm.",
            "regle": "**Ⓟ + longueur de projection** : la zone s'applique au-dessus de la surface. **Ⓕ** : "
                    "tolérance à l'état libre (plan ISO 10579-NR). **Ⓛ** : garantir une matière minimale.",
            "conversions": "Sans objet : écarts en mm, proportionnels à la hauteur.",
            "remplacement": "0,04 × 12 / 10 ; 0,04 × 40 / 10.",
            "calcul": "**0,048 mm** dans le taraudage (conforme sans Ⓟ) ; **0,16 mm** sur la bride (hors "
                     "Ø0,1) → **⊥ Ø0,1 Ⓟ 40 A**.",
            "verification": "Plus la pièce assemblée est épaisse, plus l'écart projeté grandit pour la même "
                            "inclinaison : c'est pourquoi la longueur de projection après Ⓟ est l'épaisseur "
                            "de la pièce traversée.",
        },
        "a_retenir": "À retenir : Ⓟ reporte la zone là où passe la pièce suivante ; Ⓕ s'applique à la "
                     "pièce libre ; Ⓛ protège une épaisseur de paroi.",
    },
]

# ===========================================================================
# 5. GÉNÉRATEUR (famille existante « Ajustements ISO »)
# ===========================================================================
GENERATEUR = '''
def gen_bonus_mmr():
    """Tolérance de position disponible avec Ⓜ pour un trou de passage (ISO 273, série moyenne ; H13, ISO 286)."""
    # (vis, trou de passage série moyenne ISO 273, IT13 de la tranche en mm, d'après TABLE_IT)
    vis, d, it13 = random.choice([("M6", 6.6, 0.22), ("M8", 9.0, 0.22), ("M10", 11.0, 0.27), ("M12", 13.5, 0.27)])
    t = random.choice([0.2, 0.3, 0.4, 0.5])
    bonus = round(random.choice([0.03, 0.05, 0.08, 0.1, 0.12, 0.15, 0.18, 0.2]), 2)
    D = round(d + bonus, 2)
    rep = round(t + bonus, 2)
    diag = []
    for val, msg in (
            (t, "C'est la tolérance au maximum de matière. Ce trou est plus grand que son minimum : il "
                "reçoit un bonus D réel − D min."),
            (round(t + (d + it13 - D), 2), "Tu as compté le bonus depuis le diamètre maximum. Le bonus se "
                                           "mesure depuis le maximum de matière, le plus petit trou : "
                                           "D réel − D min."),
            (round(bonus, 2), "C'est le bonus seul. La tolérance disponible, c'est t + bonus."),
    ):
        if abs(val - rep) > 0.005 and all(abs(val - x["v"]) > 0.005 for x in diag):
            diag.append(_diag(val, msg))
    return {
        "titre": "Tolérancement — bonus du maximum de matière Ⓜ",
        "enonce": (f"Des trous de passage pour vis {vis} sont percés **Ø{fr(d, 1)} H13** ({fr(d, 2)} à "
                   f"{fr(d + it13, 2)} mm). Leur position est cotée **⌖ Ø{fr(t, 1)} Ⓜ A B C**. Un trou mesure "
                   f"**Ø{fr(D, 2)}**. Quelle tolérance de position (diamètre de zone, en mm) dispose-t-il ?"),
        "rep": rep, "tol": 0.005, "unite": "mm",
        "diag": diag,
        "corr": [
            f"**Ce que dit l'énoncé.** Un trou de passage Ø{fr(d, 1)} H13, ⌖ Ø{fr(t, 1)} Ⓜ, mesuré à Ø{fr(D, 2)}.",
            f"**Le maximum de matière.** Pour un trou, c'est le plus petit diamètre : D min = {fr(d, 2)} mm.",
            f"**Le bonus.** D réel − D min = {fr(D, 2)} − {fr(d, 2)} = {fr(bonus, 2)} mm.",
            f"**La tolérance disponible.** t + bonus = {fr(t, 1)} + {fr(bonus, 2)} = Ø{fr(rep, 2)} mm.",
            f"**Je vérifie par le calibre.** Broches à la taille virtuelle {fr(d, 2)} − {fr(t, 1)} = "
            f"Ø{fr(d - t, 2)} : un trou de Ø{fr(D, 2)} décalé de e les laisse passer tant que 2e ≤ "
            f"{fr(rep, 2)} — la même condition.",
        ],
        "indice": "Trou : maximum de matière = D min ; t disponible = t + (D réel − D min).",
    }
'''

# ===========================================================================
# 6. QUIZ — nouvelle catégorie « GPS : modificateurs »
#    positions de la bonne réponse : 3, 1, 0, 2, 1, 3, 2, 0
# ===========================================================================
QUIZ_GPS = [
    ("Quand un trou est-il au maximum de matière ?",
     ["Quand il est au plus grand", "Quand il est à sa cote nominale", "Quand il est le plus profond",
      "Quand il est au plus petit diamètre permis"], 3,
     "Au maximum de matière, la pièce contient le plus de métal : pour un trou, c'est le plus petit "
     "diamètre ; pour un arbre, le plus gros. C'est le pire cas pour l'assemblage.", "Base"),
    ("Un trou Ø11 H13 (11,00 à 11,27) est localisé ⌖ Ø0,4 Ⓜ. Mesuré à Ø11,15, de quelle tolérance de "
     "position dispose-t-il ?",
     ["Ø0,4", "Ø0,55", "Ø0,52", "Ø0,67"], 1,
     "Bonus = D réel − D min = 11,15 − 11,00 = 0,15 ; tolérance disponible = 0,4 + 0,15 = Ø0,55. Ø0,67 "
     "serait le cas du trou au plus grand (11,27).", "Calcul"),
    ("Pourquoi le maximum de matière Ⓜ ne met-il pas l'assemblage en danger ?",
     ["Parce qu'il n'accorde de tolérance supplémentaire que si la pièce apporte elle-même ce jeu "
      "supplémentaire", "Parce que les vis se déforment", "Parce qu'il ne s'applique qu'aux pièces "
      "plastiques", "Parce qu'il réduit la tolérance"], 0,
     "Un trou plus grand laisse plus de jeu autour de la vis : le bonus est exactement ce jeu. Un calibre "
     "à broches de taille virtuelle (D min − t) aux positions exactes le prouve : s'il entre, les vis "
     "entrent.", "Intermédiaire"),
    ("Sur quel élément le maximum de matière Ⓜ n'a-t-il PAS de sens ?",
     ["Un trou de passage de vis", "Un trou de passage de goujon", "Un alésage de centrage d'un roulement",
      "Un trou de fixation d'un capot"], 2,
     "Ⓜ traduit un assemblage avec jeu. Un centrage ou un ajustement doit tenir sa position telle quelle : "
     "un alésage plus grand ne compense rien.", "Piège"),
    ("Un trou taraudé reçoit un goujon qui traverse une bride. Quel modificateur reporte la tolérance de "
     "perpendicularité là où passe la bride ?",
     ["Ⓜ", "Ⓟ suivi de la longueur de projection", "Ⓔ", "Ⓕ"], 1,
     "La zone projetée Ⓟ, suivie de la longueur de projection (l'épaisseur de la bride), s'applique au-dessus "
     "de la surface : le goujon prolonge l'inclinaison du taraudage, c'est dans la bride que l'écart "
     "compte.", "Base"),
    ("Pour garantir une paroi minimale entre un trou et le bord d'une pièce tout en acceptant les trous "
     "plus petits plus décalés, on utilise :",
     ["l'enveloppe Ⓔ", "le maximum de matière Ⓜ", "l'état libre Ⓕ", "le minimum de matière Ⓛ"], 3,
     "Le pire cas pour la paroi est le trou au plus grand (minimum de matière) et décalé vers le bord : "
     "Ⓛ garantit la paroi à ce pire cas et accorde un bonus aux trous plus petits.", "Intermédiaire"),
    ("Le centre d'un trou est décalé de Δx = 0,3 mm et Δy = 0,4 mm. Quelle tolérance de position (diamètre "
     "de zone) faut-il au minimum ?",
     ["Ø0,5", "Ø0,7", "Ø1,0", "Ø0,35"], 2,
     "e = √(0,3² + 0,4²) = 0,5 mm. La zone est un cylindre de diamètre t, centré sur la position exacte : "
     "il faut t ≥ 2e = Ø1,0. Ø0,5 compare e, et non 2e, au diamètre.", "Calcul"),
    ("Qu'est-ce qu'une référence spécifiée, au sens GPS (ISO 5459) ?",
     ["Un élément idéal (plan, axe) associé à la surface réelle", "La surface réelle elle-même, telle "
      "qu'usinée", "La cote nominale de la pièce", "Le premier trou percé"], 0,
     "La surface réelle est imparfaite : on lui associe un élément idéal (plan tangent, axe du plus grand "
     "cylindre inscrit…). C'est lui, la référence ; en contrôle, c'est par exemple le marbre.", "Base"),
]
