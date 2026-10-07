# -*- coding: utf-8 -*-
# BROUILLON — fiche 13.7 « Procédés, compléments : plasturgie (extrusion, soufflage, thermoformage,
# compression), poudres et MIM, assemblages sans fusion, numérisation 3D et STL » (référentiel S7.1.1 et
# S7.2.3). Rien de ceci n'est encore dans app.py.
#
# Sources des valeurs utilisées :
# - AUCUNE température, pression, tolérance ou cadence de procédé : la fiche reste qualitative, comme le demande
#   le référentiel (« approche qualitative, identifiant des ordres de grandeur… pour des analyses multicritères ») ;
# - flèche d'une corde : f = R (1 − cos(π / n)), relation géométrique ;
# - coûts d'outillage et coûts unitaires des exemples de rentabilité : DONNÉES D'ÉNONCÉ.
import math

# ===========================================================================
# 1. FIGURES
# ===========================================================================

def plasturgie_procedes():
    p = [_k_defs(), _txt(30, 24, "Quatre procédés de plasturgie, quatre familles de formes", 13, TRAIT, "start", True)]
    cadres = ((30, "EXTRUSION", "profilé continu, section constante"), (215, "SOUFFLAGE", "corps creux fermé"),
              (400, "THERMOFORMAGE", "coque mince à partir d'une plaque"), (585, "COMPRESSION", "pièce épaisse, thermodurcissable"))
    for x0, nom, leg in cadres:
        p.append(f"<rect x='{x0}' y='40' width='175' height='250' rx='8' fill='#ffffff' stroke='{ALESAGE}' stroke-width='1.8'/>")
        p.append(_txt(x0 + 87, 60, nom, 11, ALESAGE, "middle", True))
        p.append(_txt(x0 + 87, 276, leg, 9, FIN, "middle"))
    # extrusion : vis dans un fourreau, filière, profilé qui sort
    x = 30
    p.append(f"<rect x='{x + 10}' y='110' width='100' height='34' fill='#e2e8f0' stroke='{TRAIT}'/>")
    for k in range(5):
        p.append(f"<line x1='{x + 18 + k * 18}' y1='112' x2='{x + 28 + k * 18}' y2='142' stroke='{FIN}' stroke-width='2'/>")
    p.append(_txt(x + 60, 104, "vis (fourreau chauffé)", 9, FIN, "middle"))
    p.append(f"<rect x='{x + 110}' y='104' width='14' height='46' fill='{FIN}'/>")
    p.append(_txt(x + 117, 164, "filière", 9, FIN, "middle"))
    p.append(f"<rect x='{x + 124}' y='118' width='44' height='18' fill='{ARBRE}'><animate attributeName='width' values='0;44;44' dur='3s' repeatCount='indefinite'/></rect>")
    p.append(_txt(x + 150, 176, "profilé qui sort", 9, ARBRE, "middle", True))
    p.append(_txt(x + 87, 200, "tubes, joints, profilés,", 9, TRAIT, "middle"))
    p.append(_txt(x + 87, 213, "gaines, film", 9, TRAIT, "middle"))
    # soufflage : paraison gonflée dans un moule
    x = 215
    p.append(f"<rect x='{x + 40}' y='90' width='26' height='110' fill='none' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<rect x='{x + 109}' y='90' width='26' height='110' fill='none' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(_txt(x + 87, 84, "moule en deux coquilles", 9, FIN, "middle"))
    p.append(f"<ellipse cx='{x + 87}' cy='145' rx='12' ry='45' fill='#fde68a' stroke='{ARBRE}' stroke-width='2'>"
             "<animate attributeName='rx' values='12;40;40;12' dur='3s' repeatCount='indefinite'/></ellipse>")
    p.append(_txt(x + 87, 150, "paraison", 9, ARBRE, "middle", True))
    p.append(_k_fl(x + 87, 214, x + 87, 196, ALERTE, "kr", 2))
    p.append(_txt(x + 87, 228, "air soufflé dans la paraison", 9, ALERTE, "middle"))
    p.append(_txt(x + 87, 244, "flacons, réservoirs, bidons", 9, TRAIT, "middle"))
    # thermoformage : plaque chauffée aspirée sur un moule
    x = 400
    p.append(f"<rect x='{x + 30}' y='180' width='115' height='40' fill='#cbd5e1' stroke='{TRAIT}'/>")
    p.append(_txt(x + 87, 236, "moule (une seule face)", 9, FIN, "middle"))
    p.append(f"<path d='M {x + 20} 120 Q {x + 87} 120 {x + 155} 120' fill='none' stroke='{ARBRE}' stroke-width='3'>"
             f"<animate attributeName='d' values='M {x + 20} 120 Q {x + 87} 120 {x + 155} 120; M {x + 20} 178 Q {x + 87} 240 {x + 155} 178; M {x + 20} 120 Q {x + 87} 120 {x + 155} 120' dur='3s' repeatCount='indefinite'/></path>")
    p.append(_txt(x + 87, 108, "plaque chauffée, ramollie", 9, ARBRE, "middle"))
    p.append(_txt(x + 87, 252, "aspiration (vide) sous la plaque", 9, ALERTE, "middle"))
    # compression : moule chauffé, presse
    x = 585
    p.append(f"<rect x='{x + 40}' y='160' width='95' height='50' fill='#cbd5e1' stroke='{TRAIT}'/>")
    p.append(f"<rect x='{x + 60}' y='170' width='55' height='30' fill='#fde68a' stroke='{ARBRE}'/>")
    p.append(f"<g><animateTransform attributeName='transform' type='translate' values='0,0; 0,26; 0,0' dur='3s' repeatCount='indefinite'/>"
             f"<rect x='{x + 58}' y='110' width='59' height='34' fill='{FIN}'/></g>")
    p.append(_txt(x + 87, 104, "poinçon (presse)", 9, FIN, "middle"))
    p.append(_txt(x + 87, 226, "matière dosée dans le moule chauffé", 9, TRAIT, "middle"))
    p.append(_txt(x + 87, 244, "pièces électriques, composites SMC", 9, TRAIT, "middle"))
    p.append(f"<rect x='30' y='302' width='730' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 324, "La FORME de la pièce désigne presque le procédé : profil constant, creux fermé, coque mince, pièce épaisse.", 12, TRAIT, "start", True))
    return _svg("".join(p), 790, 348)


def poudres_mim():
    p = [_k_defs(), _txt(30, 24, "Métallurgie des poudres et MIM : façonner de la poudre, puis la souder par frittage", 13, TRAIT, "start", True)]
    lignes = ((70, "COMPRESSION + FRITTAGE", ALESAGE, ("poudre", "compression", "frittage", "pièce (poreuse)"),
               "pièces de série, formes « démoulables » d'un seul axe"),
              (200, "MIM (injection de métal)", ARBRE, ("poudre + liant", "injection", "déliantage", "frittage = pièce"),
               "petites pièces complexes, retrait important"))
    for y, nom, c, etapes, leg in lignes:
        p.append(_txt(40, y - 18, nom, 12, c, "start", True))
        for k, e in enumerate(etapes):
            x = 40 + k * 185
            p.append(f"<rect x='{x}' y='{y}' width='150' height='44' rx='8' fill='#ffffff' stroke='{c}' stroke-width='1.8'/>")
            p.append(_txt(x + 75, y + 27, e, 11, TRAIT, "middle", True))
            if k < 3:
                p.append(_k_fl(x + 152, y + 22, x + 183, y + 22, c, "kk", 1.8))
        p.append(_txt(40, y + 64, leg, 10, FIN, "start"))
    p.append(f"<rect x='{40 + 3 * 185 + 20}' y='{200 + 6}' width='{110}' height='32' rx='4' fill='#fde68a' opacity='0.6'>"
             "<animate attributeName='width' values='110;90;90' dur='3s' repeatCount='indefinite'/></rect>")
    p.append(_txt(40 + 3 * 185 + 75, 196, "la pièce rétrécit", 9, ARBRE, "middle", True))
    p.append(f"<rect x='30' y='296' width='730' height='52' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 318, "Frittage : la poudre est chauffée sous son point de fusion ; les grains se soudent entre eux.", 12, TRAIT, "start", True))
    p.append(_txt(46, 338, "Le moule est fait plus grand que la pièce, pour compenser le retrait (valeur donnée par le fournisseur).", 11, FIN))
    return _svg("".join(p), 790, 362)


def assemblages_sans_fusion():
    p = [_k_defs(), _txt(30, 24, "Assembler sans arc ni métal fondu en masse : brasage, friction, ultrasons", 13, TRAIT, "start", True)]
    cadres = ((30, "BRASAGE", ALESAGE), (275, "SOUDAGE PAR FRICTION", ARBRE), (520, "SOUDAGE PAR ULTRASONS", OK))
    for x0, nom, c in cadres:
        p.append(f"<rect x='{x0}' y='40' width='235' height='250' rx='8' fill='#ffffff' stroke='{c}' stroke-width='1.8'/>")
        p.append(_txt(x0 + 117, 60, nom, 11, c, "middle", True))
    # brasage : deux tubes emboîtés, métal d'apport qui monte par capillarité
    p.append(f"<rect x='70' y='110' width='150' height='22' fill='#e2e8f0' stroke='{TRAIT}'/>")
    p.append(f"<rect x='110' y='104' width='110' height='34' fill='none' stroke='{TRAIT}' stroke-width='1.6'/>")
    p.append(f"<rect x='110' y='104' width='0' height='5' fill='{ARBRE}'><animate attributeName='width' values='0;110;110' dur='3s' repeatCount='indefinite'/></rect>")
    p.append(_txt(147, 96, "manchon", 9, FIN, "middle"))
    p.append(_txt(85, 146, "tube", 9, FIN, "middle"))
    p.append(_txt(232, 112, "jeu fin", 9, FIN, "start"))
    p.append(_txt(145, 160, "le métal d'apport fondu", 10, ARBRE, "middle", True))
    p.append(_txt(145, 174, "s'infiltre dans le jeu", 10, ARBRE, "middle", True))
    p.append(_txt(145, 188, "(capillarité)", 10, ARBRE, "middle"))
    p.append(_txt(147, 220, "les pièces ne fondent pas", 10, TRAIT, "middle"))
    p.append(_txt(147, 236, "cuivre, laiton, acier, carbure", 9, FIN, "middle"))
    # friction rotative
    p.append(f"<g><animateTransform attributeName='transform' type='translate' values='0,0; 8,0; 0,0' dur='1s' repeatCount='indefinite'/>"
             f"<rect x='300' y='110' width='80' height='40' fill='#e2e8f0' stroke='{TRAIT}'/></g>")
    p.append(f"<rect x='388' y='110' width='80' height='40' fill='#e2e8f0' stroke='{TRAIT}'/>")
    p.append(_txt(340, 134, "tourne", 9, FIN, "middle"))
    p.append(_txt(428, 134, "fixe", 9, FIN, "middle"))
    p.append(f"<path d='M 330 100 A 14 14 0 1 1 350 100' fill='none' stroke='{ARBRE}' stroke-width='2' marker-end='url(#ko)'/>")
    p.append(_txt(364, 84, "tourne", 9, ARBRE, "start", True))
    p.append(_k_fl(296, 165, 330, 165, ALERTE, "kr", 2))
    p.append(_txt(340, 182, "poussée", 9, ALERTE, "middle"))
    p.append(_txt(392, 200, "le frottement chauffe, la matière", 10, TRAIT, "middle"))
    p.append(_txt(392, 214, "se malaxe sans fondre, puis on écrase", 10, TRAIT, "middle"))
    p.append(_txt(392, 236, "arbres, axes (pièces de révolution) ;", 9, FIN, "middle"))
    p.append(_txt(392, 250, "variante FSW : tôles d'aluminium", 9, FIN, "middle"))
    # ultrasons
    p.append(f"<g><animateTransform attributeName='transform' type='translate' values='0,0; 0,3; 0,0' dur='0.2s' repeatCount='indefinite'/>"
             f"<rect x='610' y='86' width='54' height='40' fill='{FIN}'/></g>")
    p.append(_txt(637, 80, "sonotrode (vibre)", 9, FIN, "middle"))
    p.append(f"<rect x='575' y='130' width='125' height='14' fill='#fde68a' stroke='{TRAIT}'/>")
    p.append(f"<rect x='575' y='144' width='125' height='14' fill='#fde68a' stroke='{TRAIT}'/>")
    p.append(_txt(637, 176, "deux pièces thermoplastiques", 10, TRAIT, "middle"))
    p.append(_txt(637, 196, "la vibration fond l'interface seule,", 10, OK, "middle", True))
    p.append(_txt(637, 210, "cycle très court, sans apport", 10, OK, "middle", True))
    p.append(_txt(637, 236, "boîtiers, filtres, connectique", 9, FIN, "middle"))
    p.append(f"<rect x='30' y='302' width='730' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 324, "Point commun : peu ou pas de chaleur dans la masse des pièces — moins de déformation, matériaux différents assemblables.", 11, TRAIT))
    return _svg("".join(p), 790, 348)


def stl_facettes():
    p = [_k_defs(), _txt(30, 24, "Le fichier STL : la surface remplacée par des triangles", 13, TRAIT, "start", True)]
    cx, cy, R = 170, 170, 110
    p.append(f"<circle cx='{cx}' cy='{cy}' r='{R}' fill='none' stroke='{ALESAGE}' stroke-width='2' stroke-dasharray='5 4'/>")
    n = 8
    pts = [(cx + R * math.cos(2 * math.pi * k / n), cy + R * math.sin(2 * math.pi * k / n)) for k in range(n)]
    p.append("<polygon points='" + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f"' fill='#fde68a' fill-opacity='0.5' stroke='{ARBRE}' stroke-width='2.4'/>")
    # flèche f sur une facette
    a0, a1 = 0, 2 * math.pi / n
    xm, ym = cx + R * math.cos((a0 + a1) / 2), cy + R * math.sin((a0 + a1) / 2)
    xc, yc = cx + R * math.cos(a0 / 2 + a1 / 2) * math.cos(math.pi / n), cy + R * math.sin((a0 + a1) / 2) * math.cos(math.pi / n)
    p.append(f"<line x1='{xc:.1f}' y1='{yc:.1f}' x2='{xm:.1f}' y2='{ym:.1f}' stroke='{ALERTE}' stroke-width='2.4'/>")
    x1_, y1_ = pts[0]
    x2_, y2_ = pts[1]
    p.append(f"<line x1='{cx}' y1='{cy}' x2='{x1_:.1f}' y2='{y1_:.1f}' stroke='{TRAIT}' stroke-width='1.2'/>")
    p.append(f"<line x1='{cx}' y1='{cy}' x2='{x2_:.1f}' y2='{y2_:.1f}' stroke='{TRAIT}' stroke-width='1.2'/>")
    p.append(f"<line x1='{cx}' y1='{cy}' x2='{xc:.1f}' y2='{yc:.1f}' stroke='{OK}' stroke-width='1.6' stroke-dasharray='4 3'/>")
    p.append(_txt(cx + 60, cy - 6, "R", 11, TRAIT, "middle", True))
    p.append(_txt(cx + 30, cy + 20, "π/n", 10, TRAIT, "middle", True))
    p.append(_txt(cx + 40, cy + 54, "R cos(π/n)", 10, OK, "middle", True))
    p.append(_txt(xm + 8, ym + 4, "flèche f", 11, ALERTE, "start", True))
    p.append(_txt(cx, cy + R + 22, "cercle exact (CAO) en pointillé ; 8 cordes (STL) en orange", 10, FIN, "middle"))
    # un triangle et sa normale
    x0 = 360
    p.append(f"<polygon points='{x0 + 20},180 {x0 + 120},200 {x0 + 70},110' fill='#fde68a' stroke='{ARBRE}' stroke-width='2'/>")
    p.append(_k_fl(x0 + 70, 165, x0 + 50, 90, OK, "kg", 2.2))
    p.append(_txt(x0 + 46, 84, "normale (vers l'extérieur)", 10, OK, "end", True))
    for (x, y, lab) in ((x0 + 20, 180, "S1"), (x0 + 120, 200, "S2"), (x0 + 70, 110, "S3")):
        p.append(f"<circle cx='{x}' cy='{y}' r='3.5' fill='{TRAIT}'/>")
        p.append(_txt(x + 6, y + 14, lab, 10, TRAIT, "start", True))
    p.append(_txt(x0 + 70, 228, "une facette = 3 sommets + 1 normale", 10, TRAIT, "middle", True))
    x1 = 540
    p.append(f"<rect x='{x1}' y='44' width='230' height='250' rx='6' fill='#ffffff' stroke='{FIN}'/>")
    for i, (t, c, g) in enumerate((("Ce que le STL contient :", TRAIT, True), ("des triangles, rien d'autre.", TRAIT, False),
                                   ("", TRAIT, False), ("Ce qu'il ne contient pas :", ALERTE, True),
                                   ("ni unité, ni cote, ni tolérance,", ALERTE, False), ("ni matière, ni arbre CAO.", ALERTE, False),
                                   ("", TRAIT, False), ("Ce qu'il exige :", OK, True),
                                   ("un volume fermé (« étanche »),", OK, False), ("des normales cohérentes.", OK, False),
                                   ("", TRAIT, False), ("Plus de facettes = plus fidèle,", FIN, False),
                                   ("mais fichier plus lourd.", FIN, False))):
        if t:
            p.append(_txt(x1 + 12, 66 + 17 * i, t, 11, c, "start", g))
    p.append(f"<rect x='30' y='306' width='740' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 328, "f = R (1 − cos(π / n)) : la flèche entre le cercle et la corde diminue quand le nombre n de facettes augmente.", 12, TRAIT, "start", True))
    return _svg("".join(p), 800, 352)


def numerisation_3d():
    p = [_k_defs(), _txt(30, 24, "Numérisation 3D : de la pièce réelle au modèle CAO (rétroconception)", 13, TRAIT, "start", True)]
    etapes = (("PIÈCE RÉELLE", "à copier, réparer,", "ou contrôler"), ("NUAGE DE POINTS", "scanner (lumière ou", "laser) ou palpeur"),
              ("MAILLAGE (STL)", "triangles reliant", "les points"), ("MODÈLE CAO", "surfaces et volumes", "reconstruits, cotés"))
    for k, (nom, l1, l2) in enumerate(etapes):
        x = 30 + k * 190
        p.append(f"<rect x='{x}' y='60' width='160' height='140' rx='8' fill='#ffffff' stroke='{ALESAGE}' stroke-width='1.8'/>")
        p.append(_txt(x + 80, 82, nom, 11, ALESAGE, "middle", True))
        p.append(_txt(x + 80, 180, l1, 9, FIN, "middle"))
        p.append(_txt(x + 80, 192, l2, 9, FIN, "middle"))
        if k < 3:
            p.append(_k_fl(x + 162, 130, x + 188, 130, TRAIT, "kk", 2))
    # pictos
    p.append(f"<rect x='75' y='105' width='70' height='50' rx='10' fill='#cbd5e1' stroke='{TRAIT}'/>")
    for i in range(40):
        a = i * 0.7
        x, y = 290 + 30 * math.cos(a) * (1 - 0.3 * math.sin(3 * a)), 130 + 22 * math.sin(a)
        p.append(f"<circle cx='{x:.1f}' cy='{y:.1f}' r='2' fill='{ARBRE}'/>")
    for k in range(5):
        p.append(f"<polygon points='{430 + k * 18},150 {448 + k * 18},150 {439 + k * 18},{112 + (k % 2) * 10}' fill='#fde68a' stroke='{ARBRE}'/>")
    p.append(f"<rect x='635' y='105' width='70' height='50' rx='10' fill='#dbeafe' stroke='{ALESAGE}' stroke-width='2'/>")
    p.append(_txt(670, 134, "Ø, plans", 9, ALESAGE, "middle", True))
    p.append(f"<rect x='30' y='220' width='740' height='70' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 242, "Deux usages : rétroconception (copier une pièce sans plan) et contrôle (comparer le scan au modèle CAO :", 12, TRAIT))
    p.append(_txt(46, 262, "une carte d'écarts colorée montre où la pièce s'éloigne de la forme voulue).", 12, TRAIT))
    p.append(_txt(46, 282, "Le maillage seul ne suffit pas pour usiner : on reconstruit des surfaces et on recote les fonctions.", 11, FIN))
    return _svg("".join(p), 800, 304)


def seuil_rentabilite():
    p = [_k_defs(), _txt(30, 24, "Choisir selon la série : le coût total de deux procédés se croise au seuil de rentabilité", 13, TRAIT, "start", True)]
    ox, oy, L, H = 80, 270, 440, 210
    p.append(_k_fl(ox, oy, ox + L + 10, oy, TRAIT, "kk", 1.4))
    p.append(_k_fl(ox, oy, ox, oy - H - 10, TRAIT, "kk", 1.4))
    p.append(_txt(ox + L, oy + 18, "nombre de pièces N", 10, TRAIT, "end"))
    p.append(_txt(ox + 4, oy - H - 14, "coût total (€)", 10, TRAIT, "start"))
    X = lambda N: ox + N / 5000 * L  # noqa: E731
    Y = lambda c: oy - c / 65000 * H  # noqa: E731
    p.append(f"<line x1='{X(0):.1f}' y1='{Y(0):.1f}' x2='{X(5000):.1f}' y2='{Y(60000):.1f}' stroke='{ALESAGE}' stroke-width='3'/>")
    p.append(_txt(X(4300), Y(52000) - 8, "usinage : 12 € par pièce", 10, ALESAGE, "end", True))
    p.append(f"<line x1='{X(0):.1f}' y1='{Y(25000):.1f}' x2='{X(5000):.1f}' y2='{Y(35000):.1f}' stroke='{ARBRE}' stroke-width='3'/>")
    p.append(_txt(X(5000), Y(35000) + 18, "MIM : moule 25 000 € + 2 € par pièce", 10, ARBRE, "end", True))
    p.append(f"<circle cx='{X(2500):.1f}' cy='{Y(30000):.1f}' r='7' fill='{ALERTE}'><animate attributeName='r' values='6;9;6' dur='1.6s' repeatCount='indefinite'/></circle>")
    p.append(f"<line x1='{X(2500):.1f}' y1='{Y(30000):.1f}' x2='{X(2500):.1f}' y2='{oy}' stroke='{ALERTE}' stroke-dasharray='4 4'/>")
    p.append(_txt(X(2500), oy + 16, "2 500", 10, ALERTE, "middle", True))
    p.append(_txt(X(2500) + 10, Y(30000) - 10, "seuil", 10, ALERTE, "start", True))
    p.append(_txt(X(900), oy - 16, "petite série : usinage", 9, ALESAGE, "middle"))
    p.append(_txt(X(4100), oy - 16, "grande série : MIM", 9, ARBRE, "middle"))
    x0 = 550
    p.append(f"<rect x='{x0}' y='44' width='220' height='230' rx='6' fill='#ffffff' stroke='{FIN}'/>")
    for i, (t, c, g) in enumerate((("Coût total = outillage", TRAIT, True), ("+ N × coût par pièce", TRAIT, True), ("", TRAIT, False),
                                   ("Seuil : les deux coûts", ALERTE, True), ("totaux sont égaux", ALERTE, True),
                                   ("N* = Δoutillage / Δcoût unitaire", ALERTE, False), ("= 25 000 / (12 − 2) = 2 500", ALERTE, False),
                                   ("", TRAIT, False), ("Valeurs : données d'énoncé.", FIN, False))):
        if t:
            p.append(_txt(x0 + 12, 68 + 20 * i, t, 11, c, "start", g))
    p.append(f"<rect x='30' y='292' width='740' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 314, "Un procédé à outillage cher (moule) ne devient rentable qu'au-delà d'un certain nombre de pièces.", 12, TRAIT))
    return _svg("".join(p), 800, 338)


# --- figure à curseurs : tolérance de corde d'un STL
def dyn_facettes(R=20.0, n=36.0):
    """Cercle de rayon R (mm) approché par n cordes : flèche f = R (1 − cos(π/n)) ; tolérance visée 0,01 mm (énoncé)."""
    n = int(round(n))
    f = R * (1 - math.cos(math.pi / n))
    tol = 0.01
    n_min = math.ceil(math.pi / math.acos(1 - tol / R))
    ok = f <= tol
    p = [_k_defs(), _txt(30, 24, f"Cercle R = {_fr_court(R, 0)} mm, approché par n = {n} facettes", 13, TRAIT, "start", True)]
    cx, cy, Rd = 170, 210, 85
    p.append(f"<circle cx='{cx}' cy='{cy}' r='{Rd}' fill='none' stroke='{ALESAGE}' stroke-width='2' stroke-dasharray='5 4'/>")
    pts = [(cx + Rd * math.cos(2 * math.pi * k / n), cy + Rd * math.sin(2 * math.pi * k / n)) for k in range(n)]
    p.append("<polygon points='" + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f"' fill='#fde68a' fill-opacity='0.4' stroke='{ARBRE}' stroke-width='1.6'/>")
    p.append(_txt(cx, cy + Rd + 16, "cercle exact (pointillé) et polygone du STL (orange)", 9, FIN, "middle"))
    # loupe : une facette, écart agrandi 400 fois
    hf = min(40.0, f * 400)
    p.append(f"<rect x='40' y='44' width='260' height='68' rx='6' fill='#ffffff' stroke='{FIN}'/>")
    p.append(f"<path d='M 60 98 Q 170 {98 - 2 * hf:.1f} 280 98' fill='none' stroke='{ALESAGE}' stroke-width='2' stroke-dasharray='5 4'/>")
    p.append(f"<line x1='60' y1='98' x2='280' y2='98' stroke='{ARBRE}' stroke-width='2.4'/>")
    p.append(f"<line x1='170' y1='98' x2='170' y2='{98 - hf:.1f}' stroke='{ALERTE}' stroke-width='2'/>")
    p.append(_txt(176, 92, "f", 11, ALERTE, "start", True))
    p.append(_txt(170, 58, "une facette, écart agrandi 400 fois" + (" (coupé)" if f * 400 > 40 else ""), 9, FIN, "middle"))
    x0 = 340
    col = OK if ok else ALERTE
    p.append(f"<rect x='{x0}' y='44' width='430' height='230' rx='6' fill='#ffffff' stroke='{col}' stroke-width='1.8'/>")
    lignes = ((f"f = R (1 − cos(π / n)) = {_fr_court(R, 0)} × (1 − cos(π / {n}))", TRAIT, False),
              (f"f ≈ {_fr_court(f, 4)} mm", col, True), ("", TRAIT, False),
              ("tolérance visée f_max (énoncé) : 0,01 mm", TRAIT, False),
              (("respectée" if ok else "non respectée : il faut plus de facettes"), col, True),
              (f"nombre minimal : n ≥ π / arccos(1 − f_max / R) = {n_min}", ALESAGE, True), ("", TRAIT, False),
              ("Doubler n double le fichier et divise la flèche par 4.", FIN, False),
              ("Au-delà de la finesse de la machine, plus rien n'est gagné.", FIN, False))
    for i, (t, c, g) in enumerate(lignes):
        if t:
            p.append(_txt(x0 + 12, 68 + 22 * i, t, 12, c, "start", g))
    p.append(_txt(30, 330, "Réglage d'export STL : le logiciel de CAO demande cette tolérance (écart de corde) et un écart angulaire.", 10, FIN))
    return _svg("".join(p), 790, 344)


FIGURES_NOUVELLES = {
    "plasturgie_procedes": ("Extrusion, soufflage, thermoformage, compression", plasturgie_procedes),
    "poudres_mim": ("Métallurgie des poudres et MIM", poudres_mim),
    "assemblages_sans_fusion": ("Brasage, soudage par friction, soudage par ultrasons", assemblages_sans_fusion),
    "stl_facettes": ("Le fichier STL : facettes, normales, flèche", stl_facettes),
    "numerisation_3d": ("Numérisation 3D et rétroconception", numerisation_3d),
    "seuil_rentabilite": ("Seuil de rentabilité entre deux procédés", seuil_rentabilite),
}
DYN_NOUVELLE = {
    "facettes_curseurs": (
        "Change le rayon et le nombre de facettes : la flèche entre le cercle et le STL se recalcule",
        dyn_facettes,
        [{"nom": "R", "label": "Rayon du cercle R (mm)", "min": 5.0, "max": 50.0, "defaut": 20.0, "pas": 5.0},
         {"nom": "n", "label": "Nombre de facettes n", "min": 8.0, "max": 200.0, "defaut": 36.0, "pas": 4.0}]),
}

# ===========================================================================
# 2. FICHE 13.7 — en FIN de bloc 13 (après la 13.6)
# ===========================================================================

FICHE_13_7 = {
    "id": "13.7",
    "titre": "Procédés, compléments : extrusion, soufflage, thermoformage, poudres et MIM, assemblages sans fusion, STL",
    "duree": "5 h",
    "cours": """### 1. Pourquoi cette fiche

Les fiches 12.3 (bruts : fonderie, forgeage, tôlerie, soudage), 12.4 (usinage), 13.1 (injection plastique et
composites), 9.7 (prototypage rapide) et 13.6 (fabrication additive métallique) ont posé les grands
procédés. Il en manque plusieurs, très présents dans les produits du quotidien : les autres procédés de la
plasturgie, la métallurgie des poudres, les assemblages qui ne fondent pas les pièces, et la chaîne
numérique de la numérisation 3D et du fichier STL.

Pour un concepteur, connaître un procédé, c'est savoir répondre à trois questions : **à quoi il sert** (quelles
formes), **quand le choisir** (quelle série, quel matériau) et **quelles limites** il impose au dessin. C'est le
fil de toute la fiche. Les valeurs de température, de pression ou de tolérance propres à chaque procédé
dépendent de la machine et de la matière : elles viennent du spécialiste ou du fournisseur, pas d'un cours.
« Petite » ou « grande » série n'est pas un nombre fixe : c'est le seuil de rentabilité (§6) qui dit, pour une
pièce donnée, à partir de combien d'exemplaires un moule devient rentable.

### 2. Plasturgie : la forme désigne le procédé

[[FIG:plasturgie_procedes]]

**Extrusion.** Une vis tourne dans un fourreau chauffé, fait fondre les granulés et pousse la matière à
travers une **filière** qui lui donne sa section. *C'est le tube de dentifrice, ou la machine à pâtes fraîches :
ce qui sort a toujours la forme du trou ; changer de profil, c'est changer de filière, pas de machine.*
- **À quoi** : tout ce qui a une **section constante** et une grande longueur : tubes, joints, gaines,
  profilés de fenêtre, film, fil.
- **Quand** : très grandes séries (production continue) ; thermoplastiques (le même principe file aussi les
  profilés d'aluminium et les joints en caoutchouc).
- **Limites** : la section ne varie pas le long de la pièce ; les détails (perçages, encoches) demandent une
  opération supplémentaire après.

**Soufflage.** Un tube de matière chaude (la **paraison**) ou une préforme injectée est enfermé dans un moule
en deux coquilles, puis gonflé à l'air comprimé contre ses parois. *Comme un ballon qu'on gonfle à l'intérieur
d'une boîte : il en prend la forme. La préforme, c'est la petite « éprouvette » à goulot déjà fileté qu'on voit
avant qu'elle devienne bouteille d'eau : le goulot est injecté (précis), le corps est soufflé.*
- **À quoi** : les **corps creux fermés** : flacons, bouteilles, bidons, réservoirs.
- **Quand** : grandes séries ; thermoplastiques.
- **Limites** : on maîtrise la forme extérieure, pas l'intérieur ; l'épaisseur varie — comme un ballon, la
  paroi est plus fine là où elle a dû aller le plus loin, dans les coins.

**Thermoformage** (complément au programme). Une plaque thermoplastique est chauffée jusqu'à se ramollir, puis
plaquée sur un moule par aspiration (vide) ou par pression. *C'est le blister des piles, ou le pot de yaourt.*
- **À quoi** : les **coques minces** : bacs, capots, habillages, emballages.
- **Quand** : petites et moyennes séries pour les grandes pièces techniques (l'outillage, à une seule face, est
  simple et peu coûteux) ; très grandes séries pour les emballages minces, sur des machines alimentées en
  bobine.
- **Limites** : une seule face est précise (seule la face plaquée contre le moule en recopie la forme) ;
  l'épaisseur diminue dans les angles, parce que la plaque s'étire comme un chewing-gum ; il faut détourer la
  pièce après formage (découper le bord de plaque en trop).

**Compression.** La matière est déposée dans un moule chauffé, puis pressée par un poinçon jusqu'au
durcissement. *Comme un gaufrier : on dépose la pâte dosée, on ferme, on chauffe ; un thermodurcissable « cuit »
et ne refondra plus jamais, comme la gaufre.*
- **À quoi** : pièces **épaisses** en **thermodurcissables** (pièces électriques isolantes) et composites en
  **SMC** (*Sheet Moulding Compound* : feuille de résine chargée de fibres de verre coupées, prête à mouler :
  capots, boîtiers électriques).
- **Quand** : moyennes à grandes séries.
- **Limites** : formes plus simples qu'en injection ; une bavure à reprendre au plan de joint.

*Retenir la logique : profil constant → extrusion ; creux fermé → soufflage ; coque mince → thermoformage ;
pièce complexe de grande série → injection (fiche 13.1) ; thermodurcissable épais → compression.*

### 3. Métallurgie des poudres et MIM

[[FIG:poudres_mim]]

**Le principe commun : le frittage.** Une poudre métallique, mise en forme, est chauffée **sous son point de
fusion** : les grains se soudent entre eux à leurs points de contact. *Pensez à la neige d'une piste : tassée,
puis laissée au froid, elle devient une plaque dure sans jamais avoir fondu.* Pourquoi ne pas fondre
complètement ? Un métal liquide coulerait et perdrait la forme donnée par la matrice : en restant sous la
fusion, la pièce garde sa forme. (Les céramiques techniques de la fiche 3.5 sont aussi frittées.)

**Compression et frittage (métallurgie des poudres « classique »).** La poudre est comprimée dans une matrice
par des poinçons, puis frittée.
- **À quoi** : engrenages, cames, pièces de serrures, **coussinets autolubrifiants** (la porosité retient
  l'huile, comme une éponge imbibée qui la rend quand l'arbre tourne).
- **Quand** : grandes séries ; très peu de matière perdue, peu ou pas d'usinage.
- **Limites** : on tasse la poudre comme le café dans le porte-filtre d'un expresso — on ne peut presser que de
  haut en bas, et la pastille ressort par le haut : pas de contre-dépouille (gorge ou trou sur le côté, qui
  accrocherait la pièce dans la matrice) ; la pièce reste un peu **poreuse**, donc moins résistante qu'une
  pièce forgée.

**MIM (moulage par injection de métal).** Une poudre très fine est mélangée à un **liant** plastique ; le
mélange est **injecté** comme un plastique (fiche 13.1), puis on retire le liant (**déliantage**) et on fritte.
- **À quoi** : **petites pièces métalliques complexes** : pièces d'horlogerie, d'armes, de serrures,
  d'instruments chirurgicaux, d'électronique.
- **Quand** : grandes séries de petites pièces que l'usinage rendrait chères (formes 3D, détails fins).
- **Limites** : le **retrait** au frittage est important. Pourquoi : après déliantage, il reste un
  « squelette » de grains avec des vides là où était le plastique ; au frittage, les grains se rapprochent pour
  les combler, et toute la pièce rétrécit. Le moule est donc fait plus grand, d'une valeur donnée par le
  fournisseur. Pièces de petite taille ; moule coûteux, donc rentable seulement en série (§6).

### 4. Assembler sans arc ni métal fondu en masse

[[FIG:assemblages_sans_fusion]]

Le soudage à l'arc (fiches 12.3 et 13.2) fond les bords des pièces. Trois familles évitent de fondre la masse
des pièces : le brasage (seul l'apport fond), la friction (soudage à l'état solide, sans fusion), les ultrasons
(fusion très localisée de l'interface des plastiques, sans apport ni chauffage extérieur).

**Brasage.** Un **métal d'apport**, qui fond à une température plus basse que celle des pièces, est fondu et
s'infiltre par **capillarité** dans le jeu entre les pièces ; les pièces, elles, ne fondent pas. *Comme le sucre
trempé dans le café, qui « boit » le liquide par le bas : un liquide monte tout seul dans un passage très fin.
D'où un jeu faible et régulier : trop large, le métal fondu n'est plus aspiré et le joint reste creux. Le fer à
souder de l'électronicien fait d'ailleurs du brasage tendre : la « soudure à l'étain » ne fond jamais les pattes
du composant.* On distingue
le brasage **tendre** (alliages à l'étain : électronique, plomberie) et le brasage **fort** (alliages au
cuivre ou à l'argent : joints plus résistants, températures plus élevées).
- **À quoi** : tuyauteries de climatisation, plaquettes de carbure sur un corps d'outil, électronique.
- **Quand** : assembler des **matériaux différents** (cuivre sur acier, carbure sur acier), des pièces minces,
  des tubes.
- **Limites** : le métal d'apport est moins résistant que les pièces — on compense par un recouvrement
  (emboîtement) suffisant ; il faut un jeu faible et régulier et des surfaces propres.

**Soudage par friction.** Une pièce tourne contre l'autre sous poussée ; le frottement chauffe l'interface (comme
des mains frottées très vite), la matière se ramollit et se malaxe **sans fondre** ; puis on arrête la rotation et
on pousse fort une dernière fois : les deux matières s'écrasent l'une dans l'autre et se soudent.
- **À quoi** : arbres, axes, soupapes bimétal.
- **Quand** : pièces de **révolution**, y compris de matériaux différents ; la variante **FSW**
  (friction-malaxage), avec un outil tournant qui avance le long du joint comme une cuillère qui touille une
  pâte épaisse, assemble des tôles d'aluminium sans les fondre : moins de déformation, et possibilité de souder
  certains alliages réputés difficiles à souder à l'arc.
- **Limites** : machine spécifique et coûteuse ; géométries imposées (révolution, ou joint accessible).

**Soudage par ultrasons.** Une **sonotrode** fait vibrer une pièce contre l'autre à haute fréquence : c'est comme
frotter les deux pièces des milliers de fois par seconde ; seule l'interface de deux **thermoplastiques** chauffe
jusqu'à fondre, en un cycle très court, sans apport, le reste de la pièce restant froid.
- **À quoi** : boîtiers plastiques, filtres, emballages ; sur des fils et feuilles métalliques minces
  (connectique), la liaison se fait sans fusion.
- **Limites** : pièces de petite taille, matières compatibles ; le joint se prépare au dessin (une nervure en
  pointe, le « directeur d'énergie », concentre la vibration sur une ligne, comme la pointe d'une punaise
  concentre l'effort).

**Quel assemblage ?** Deux métaux identiques et épais, qu'on peut fondre : soudage à l'arc. Deux matériaux
différents, des pièces minces ou des tubes : brasage. Deux pièces de révolution, ou des tôles d'aluminium :
friction, FSW. Deux petites pièces thermoplastiques : ultrasons.

### 5. Numérisation 3D et fichier STL

[[FIG:stl_facettes]]

*Un ballon de football est fait de pièces plates cousues : de loin il paraît rond, de près on voit des
facettes. Le STL, c'est pareil, avec des triangles.*

**Le STL, format pivot de la fabrication additive.** Le logiciel de préparation de l'imprimante (le
**trancheur**) ne lit pas un modèle CAO : le modèle CAO décrit des formes exactes par leurs paramètres (un
cylindre = un axe et un rayon), dans un format propre à chaque logiciel. Le trancheur a besoin d'une
description simple et universelle qu'il peut couper en tranches : une surface découpée en **facettes
triangulaires** (fiche 9.7). Chaque facette est décrite par ses **trois sommets** et sa **normale** (une petite
flèche qui pointe vers l'extérieur de la matière). Le trancheur coupe ce maillage en couches et produit le
programme de la machine.

**Ce que le STL ne contient pas** : ni unité, ni cote, ni tolérance, ni matière, ni historique de construction.
*Le STL est à la CAO ce qu'une photo pixelisée est à un dessin coté : on voit la forme, mais on ne peut pas y
lire « Ø20 H7 ». L'alésage y est devenu un polygone : l'usineur ne retrouve ni son vrai diamètre ni son axe, et
ne sait même pas si « 20 » veut dire 20 mm ou 20 pouces.* C'est pour cela qu'on n'envoie jamais un STL pour
usiner une pièce cotée (fiche 12.4) : on envoie un **STEP** (format d'échange qui garde les vraies surfaces,
lisible par tous les logiciels de CAO et de FAO) et un plan.

**Ce qu'il exige** : un volume **fermé** (« étanche » : aucun trou entre facettes — comme un ballon, un seul trou
et on ne sait plus ce qui est dedans ou dehors) et des normales cohérentes ; sinon le trancheur ne sait plus où
est la matière. Les logiciels de préparation détectent et réparent ces
défauts.

**La finesse du maillage.** Une surface courbe est remplacée par des cordes : l'écart maximal entre le cercle et
une corde s'appelle la **flèche** (ou écart de corde). *Pensez à un arc de tir : la flèche est posée au milieu
de la corde et pointe vers le bois de l'arc. Ici, c'est la distance entre le milieu de la corde (la facette) et
l'arc de cercle.*

**D'où vient la formule**, en trois étapes : (1) n facettes se partagent le tour : chacune occupe un angle 2π/n
vu depuis le centre ; (2) le rayon qui coupe la facette en son milieu forme, avec la demi-corde, un triangle
rectangle dont l'angle au centre vaut π/n : le centre est à R × cos(π/n) du milieu de la corde ; (3) le cercle,
lui, est à R du centre ; l'écart entre les deux est la flèche :

> **f = R − R cos(π / n) = R × (1 − cos(π / n))** · nombre minimal de facettes pour une flèche maximale admise
> f_max : **n ≥ π / arccos(1 − f_max / R)** (calculatrice en radians), arrondi à l'entier supérieur

*Exemple : un cercle de rayon 20 mm, avec une flèche maximale admise f_max = 0,01 mm (donnée d'énoncé) : il faut
n ≥ π / arccos(1 − 0,01 / 20) ≈ 99,3, soit **100 facettes** sur le tour. Avec 36 facettes (π/36 rad, soit 5°), la
flèche vaut 20 × (1 − cos 5°) ≈ 0,076 mm : un cylindre visiblement facetté.* À l'export, le logiciel de CAO
demande cette tolérance de corde et un **écart angulaire** (le « pli » maximal autorisé entre deux facettes
voisines, qui évite que les petits rayons soient trop facettés). Doubler n double le fichier et divise la flèche
par 4 : c'est payant au début ; mais une fois la flèche plus fine que ce que l'imprimante sait reproduire
(épaisseur de couche, diamètre de buse), ajouter des facettes n'apporte plus rien.

[[DYN:facettes_curseurs]]

**Encadré : le chemin inverse, la numérisation 3D.** On part d'une pièce réelle.

[[FIG:numerisation_3d]]

Un **scanner** (lumière structurée ou laser) ou un palpeur relève des milliers de points de la surface : un
**nuage de points**. Le logiciel les relie en **maillage** (un STL), puis le concepteur **reconstruit** des
surfaces et des volumes CAO, et recote les surfaces fonctionnelles.
- **Rétroconception** : refaire une pièce dont on n'a pas le plan (pièce ancienne, pièce concurrente,
  forme sculptée à la main).
- **Contrôle** : comparer le scan d'une pièce fabriquée à son modèle CAO ; une **carte d'écarts** colorée
  montre où elle s'éloigne de la forme voulue.
- **Limites** : surfaces brillantes ou transparentes difficiles à scanner ; trous profonds et zones cachées
  non relevés ; un maillage n'est pas un modèle CAO utilisable pour usiner une pièce cotée et tolérancée.

### 6. Choisir selon la série : le seuil de rentabilité

[[FIG:seuil_rentabilite]]

Beaucoup de procédés de série (injection, soufflage, MIM, poudres) demandent un **outillage** coûteux (un
moule, une matrice) mais un coût par pièce faible ; l'usinage ou l'impression 3D, presque pas d'outillage mais
un coût par pièce élevé. Le coût total vaut :

> **Coût total = coût d'outillage + N × coût par pièce**

Appelons A le procédé sans (ou presque sans) outillage, par exemple l'usinage, et B le procédé à moule, par
exemple le MIM. Au **seuil de rentabilité** N*, les deux factures sont égales :

> outillage A + N × coût unitaire A = outillage B + N × coût unitaire B, d'où
> **N* = (outillage B − outillage A) / (coût unitaire A − coût unitaire B)** = surcoût du moule / économie par pièce

*Exemple (données d'énoncé) : une petite pièce en acier, usinée pour 12 € pièce sans outillage, ou en MIM avec un
moule de 25 000 € et 2 € par pièce. Chaque pièce faite en MIM fait économiser 12 − 2 = 10 € ; il en faut 25 000 /
10 = **2 500** pour que ces économies « remboursent » le moule — le calcul d'un abonnement de salle de sport
comparé aux entrées à l'unité. Pour 1 000 pièces : usinage
12 000 €, MIM 27 000 € → usiner. Pour 5 000 pièces : usinage 60 000 €, MIM 35 000 € → MIM.*

**La grille de choix d'un concepteur** — ordre conseillé, avec retours en arrière quand une exigence (contact
alimentaire, température) impose le matériau :
1. **La forme** : profil constant, creux fermé, coque mince, pièce de révolution, petite pièce complexe… La
   forme élimine déjà la plupart des procédés.
2. **Le matériau** : thermoplastique, thermodurcissable, métal ; un procédé ne travaille qu'une famille.
3. **La série** : outillage cher amorti seulement au-delà du seuil de rentabilité.
4. **Les exigences** : précision, état de surface, résistance (une pièce frittée est poreuse, une pièce
   thermoformée a une seule face précise).

| Ma pièce est… | Matériau | Procédé à envisager | La limite à vérifier sur le dessin |
|---|---|---|---|
| un profil de section constante, long (tube, joint) | thermoplastique | extrusion | section identique partout ; perçages après |
| un corps creux fermé (flacon, réservoir) | thermoplastique | soufflage | seul l'extérieur est précis ; épaisseur variable |
| une coque mince (bac, capot, emballage) | thermoplastique en plaque | thermoformage | une seule face précise ; amincissement dans les angles |
| une pièce plastique complexe, grande série | thermoplastique | injection (13.1) | dépouilles, épaisseur régulière |
| une pièce épaisse qui ne doit pas refondre | thermodurcissable, SMC | compression | formes simples ; bavure au plan de joint |
| une pièce métallique qui sort de la matrice dans un seul sens (pignon, came) | poudre métallique | compression + frittage | pas de contre-dépouille ; pièce poreuse |
| une petite pièce métallique de forme 3D complexe, grande série | poudre métallique | MIM | retrait au frittage ; petite taille |
| une pièce unitaire ou en très petite série, cotes serrées | métal, plastique | usinage (12.4) | coût par pièce élevé |
| un prototype, une forme impossible à mouler | plastique, métal | fabrication additive (9.7, 13.6), fichier STL | facettage, état de surface |

### 7. Les erreurs classiques

1. **Choisir un procédé à moule pour quelques pièces** : l'outillage ne s'amortit pas.
2. **Dessiner une contre-dépouille transversale sur une pièce frittée** : elle ne sortira pas de la matrice.
3. **Oublier le retrait du MIM** : le moule est plus grand que la pièce.
4. **Attendre deux faces précises d'un thermoformage** : seule la face contre le moule l'est.
5. **Envoyer un STL pour usiner une pièce cotée** : pas de cote, pas de tolérance, pas d'unité.
6. **Exporter un STL trop grossier** : cylindres facettés ; ou trop fin : fichier énorme, plus fin que ce que la
   machine sait faire.
7. **Croire que le brasage fond les pièces** : seul le métal d'apport fond.

### 8. À retenir

- **Extrusion** : section constante, en continu. **Soufflage** : corps creux. **Thermoformage** : coque mince,
  petite série, une face précise. **Compression** : thermodurcissables, pièces épaisses.
- **Frittage** : souder une poudre sous son point de fusion. Poudres comprimées : grande série, démoulage d'un
  seul axe, pièce poreuse. **MIM** : petites pièces métalliques complexes, retrait important.
- **Brasage** (apport seul fondu, capillarité), **friction** (malaxage sans fusion, révolution ; FSW pour
  l'aluminium), **ultrasons** (fusion locale de l'interface des thermoplastiques, cycle court).
- **STL** : facettes triangulaires (3 sommets + normale), sans unité ni tolérance ; volume étanche ; flèche
  **f = R (1 − cos(π/n))**, et **n ≥ π / arccos(1 − f_max / R)**.
- **Numérisation** : nuage de points → maillage → CAO reconstruite (rétroconception, contrôle).
- **Choix** : forme → matériau → série (**N* = Δoutillage / Δcoût unitaire**) → exigences.
""",
    "formules": """
**Seuil de rentabilité** — coût total = outillage + N × coût unitaire · A sans outillage, B à moule :
N* = (outillage B − outillage A) / (coût unitaire A − coût unitaire B) = surcoût du moule / économie par pièce

**Flèche d'un maillage** — f = R × (1 − cos(π / n)) · nombre minimal de facettes pour une flèche maximale admise
f_max : n ≥ π / arccos(1 − f_max / R), en radians, arrondi à l'entier supérieur

**Grille de choix** — forme → matériau → série → exigences (précision, surface, résistance)
""",
    "exemple": """
### Cas industriel — Le réservoir qui fuyait : deux coques injectées remplacées par une pièce soufflée

**Le point de départ.** Un fabricant de petits équipements de jardin produit un réservoir de carburant en
deux coques **injectées** puis assemblées par vis, avec un joint. Les fuites au joint sont fréquentes et le
montage est long.

**L'analyse, avec la grille de choix.**
- **Forme** : le réservoir est un **corps creux fermé** — exactement ce que fait le **soufflage**.
- **Matériau** : un thermoplastique, compatible avec le soufflage.
- **Série** : plusieurs milliers par an ; le moule de soufflage remplace deux moules d'injection et supprime le
  montage.
- **Exigences** : l'étanchéité au liquide est assurée par construction (une seule pièce, plus de joint) ;
  l'intérieur n'a pas besoin d'être précis. (Un réservoir de carburant demande en plus une couche barrière
  contre la perméation des vapeurs : c'est l'affaire du spécialiste du soufflage.)

**Le bouchon, lui, reste injecté** : ce n'est pas un corps creux fermé, et son filetage intérieur et ses clips sont
des formes intérieures que le soufflage ne maîtrise pas (seule la forme extérieure l'est). Le goulot fileté du
réservoir, lui, sort du moule de soufflage. Pour le petit levier de verrouillage métallique (forme 3D complexe :
crochet, ergot, perçage oblique), l'usinage revenait cher : avec les devis (données d'énoncé : usinage 7 € la
pièce ; MIM : moule 20 000 € + 1 € la pièce), le seuil vaut 20 000 / 6 ≈ 3 300 pièces ; à 5 000 leviers par an,
il passe en **MIM**.

**Ce que le cas apprend.** On ne choisit pas un procédé pour toute la machine, mais **pièce par pièce**, avec la
grille forme → matériau → série → exigences. Le meilleur choix supprime parfois des pièces et des opérations
(le joint, le montage) : c'est là que se fait la plus grosse économie.
""",
    "exercice": """
### Exercice — Choisir les procédés d'un petit appareil

Pour chacune des pièces suivantes, proposer un procédé et justifier par la grille **forme → matériau → série →
exigences**.

**1.** Un joint de porte en élastomère thermoplastique, de section constante, vendu au mètre.

**2.** Un bac de rangement de 600 × 400 mm, fabriqué à 300 exemplaires.

**3.** Une petite gâchette métallique de 20 mm, de forme complexe, fabriquée à 50 000 exemplaires par an.

**4.** Le prototype unique d'un boîtier, à imprimer en 3D à partir du modèle CAO : quel fichier envoyer, et
quel réglage surveiller à l'export ?

**5.** Pour la gâchette (question 3), deux devis : usinage à 6 € pièce sans outillage, ou MIM avec un moule de
40 000 € et 1,50 € par pièce (données d'énoncé). Calculer le seuil de rentabilité. Le MIM est-il justifié pour
50 000 pièces par an ?

**6.** Il faut fixer une plaquette de carbure sur un corps d'outil en acier : quel assemblage, et pourquoi pas le
soudage à l'arc ?
""",
    "corrige": """
### Corrigé, en six temps

#### 1. Ce que dit l'énoncé

Cinq pièces de formes, de matériaux et de séries différents ; deux devis pour la dernière.

#### 2. Quelle règle, et pourquoi

> **Grille de choix : forme → matériau → série → exigences.** **N* = Δoutillage / Δcoût unitaire.** Le STL
> est le format de la fabrication additive (triangles, sans cote), réglé par la tolérance de corde.

#### 3. Les conversions

Coûts en euros, séries en nombre de pièces.

#### 4. Le remplacement

N* = (40 000 − 0) / (6 − 1,50).

#### 5. Le calcul

**1.** **Extrusion** : section constante, grande longueur, thermoplastique, production continue.

**2.** **Thermoformage** : coque mince de grande surface, thermoplastique, petite série (300 pièces : un moule
d'injection de cette taille ne s'amortirait pas) ; une seule face précise suffit pour un bac.

**3.** **MIM** : petite pièce métallique complexe, grande série. (La métallurgie des poudres classique
conviendrait si la forme se démoulait d'un seul axe.)

**4.** Un fichier **STL** (maillage de triangles) ; surveiller la **tolérance de corde** et l'écart angulaire à
l'export, et vérifier que le maillage est fermé.

**5.** N* = 40 000 / 4,50 ≈ **8 889 pièces**. À 50 000 pièces par an, on est très au-delà du seuil : le MIM est
justifié (coût total : usinage 300 000 €, MIM 40 000 + 75 000 = 115 000 € la première année).

**6.** **Brasage fort** : deux matériaux différents, et le carbure ne doit pas fondre ; seul le métal d'apport
fond et s'infiltre par capillarité. Prévoir un jeu fin et régulier et des surfaces propres.

#### 6. La vérification

**Bon sens** : chaque procédé proposé correspond à la forme de la pièce. **Ordre de grandeur** : un moule de
40 000 € s'amortit avec quelques milliers de pièces quand on économise plusieurs euros par pièce.
""",
}

# ===========================================================================
# 3. MÉTHODE
# ===========================================================================
MTH_13_7 = ("13.7", "Choisir un procédé pour une pièce", [
    "**La forme** : section constante (extrusion), creux fermé (soufflage), coque mince (thermoformage), pièce de "
    "révolution, petite pièce complexe (injection, MIM)… La forme élimine déjà la plupart des procédés.",
    "**Le matériau** : thermoplastique, thermodurcissable ou métal — chaque procédé ne travaille qu'une famille.",
    "**La série** : comparer les coûts totaux ; calculer le seuil N* = Δoutillage / Δcoût unitaire.",
    "**Les exigences** : précision, état de surface, résistance — et les règles de dessin du procédé retenu "
    "(démoulage, retrait, épaisseur, jeu de brasage).",
], "Gâchette métallique complexe de 20 mm, 50 000 pièces/an : forme et série → MIM. Devis : usinage 6 €, MIM moule "
   "40 000 € + 1,50 € → N* ≈ 8 889 pièces : MIM justifié.")

# ===========================================================================
# 4. ATELIERS (fin de liste ATELIERS, après at175)
# ===========================================================================
ATELIERS_NOUVEAUX = [
    {
        "id": "at176",
        "chapitre": "Bloc 13",
        "titre": "Usiner ou passer en MIM ? Le seuil de rentabilité",
        "theme": "Procédés",
        "fiche": "13.7",
        "figure": "seuil_rentabilite",
        "vocabulaire": [
            ("Outillage",
             "le moule ou la matrice propre à une pièce : coût fixe, payé une fois."),
            ("Coût unitaire",
             "ce que coûte chaque pièce en plus (matière, machine, main-d'œuvre)."),
            ("Seuil de rentabilité",
             "le nombre de pièces à partir duquel le procédé à outillage devient le moins cher."),
        ],
        "enonce": "Une pièce métallique de petite taille et de forme complexe peut être usinée pour 9 € pièce sans "
                  "outillage, ou fabriquée en MIM avec un moule de 30 000 € et 1,50 € par pièce (données d'énoncé).",
        "etapes": [
            {"type": "numerique", "label": "Seuil de rentabilité",
             "unite": "pièces", "attendu": 4000, "tol": 1,
             "consigne": "Calcule N* = Δoutillage / Δcoût unitaire.",
             "indice": "30 000 / (9 − 1,50).",
             "pieges": [(3333.3, "3 333 : tu as divisé par 9 au lieu de 9 − 1,50. Ce qui compte, c'est l'économie "
                                 "par pièce."),
                        (20000, "20 000 : tu as divisé par 1,50. L'outillage s'amortit grâce à la DIFFÉRENCE de coût "
                                "par pièce."),
                        (2857.1, "2 857 : tu as additionné 9 + 1,50 ; c'est l'économie par pièce, 9 − 1,50, qui amortit "
                                 "le moule.")],
             "aide": "30 000 / 7,50 = 4 000 pièces."},
            {"type": "numerique", "label": "Coût total en MIM pour 2 000 pièces",
             "unite": "€", "attendu": 33000, "tol": 1,
             "consigne": "Calcule le coût total en MIM pour une série de 2 000 pièces.",
             "indice": "Outillage + N × coût unitaire.",
             "pieges": [(3000, "3 000 € : tu as oublié le moule (30 000 €)."),
                        (18000, "18 000 €, c'est le coût de l'usinage (2 000 × 9). La question porte sur le MIM.")],
             "aide": "30 000 + 2 000 × 1,50 = 33 000 €."},
            {"type": "qcm", "label": "Décision pour 2 000 pièces",
             "question": "Pour 2 000 pièces, l'usinage coûte 18 000 € et le MIM 33 000 €. Que choisir ?",
             "options": ["Le MIM : il coûte moins cher par pièce", "L'usinage : on est sous le seuil de 4 000 pièces",
                         "Indifférent"], "bonne": 1,
             "indice": "Comparer la série au seuil de rentabilité.",
             "diagnostics": {0: "Le coût unitaire est plus faible, mais le moule n'est pas amorti à 2 000 pièces : le coût "
                                 "TOTAL est plus élevé.",
                             2: "18 000 € contre 33 000 € : l'écart est net. Ce n'est indifférent qu'au seuil (4 000)."}},
            {"type": "qcm", "label": "Contrainte de dessin",
             "question": "Le MIM est retenu pour une série plus grande. Quelle contrainte le concepteur doit-il intégrer ?",
             "options": ["Le retrait important au frittage : le moule est fait plus grand que la pièce",
                         "Aucune : le MIM reproduit exactement le moule",
                         "La pièce doit être de révolution"], "bonne": 0,
             "indice": "Que se passe-t-il quand on retire le liant et qu'on fritte ?",
             "diagnostics": {1: "Le liant retiré laisse des vides que le frittage referme : la pièce rétrécit nettement.",
                             2: "C'est le cas du soudage par friction, pas du MIM, qui fait justement des formes complexes."}},
        ],
        "corrige": {
            "enonce": "Usinage 9 € sans outillage ; MIM : moule 30 000 € + 1,50 € par pièce.",
            "regle": "**Coût total = outillage + N × coût unitaire** ; **N* = Δoutillage / Δcoût unitaire**.",
            "conversions": "Coûts en €.",
            "remplacement": "N* = 30 000 / (9 − 1,50) ; coût MIM 2 000 pièces = 30 000 + 2 000 × 1,50.",
            "calcul": "**N* = 4 000 pièces** ; pour 2 000 pièces : usinage **18 000 €**, MIM **33 000 €** → usiner.",
            "verification": "Au seuil (4 000 pièces) : usinage 36 000 €, MIM 30 000 + 6 000 = 36 000 € : les deux "
                            "coûts sont bien égaux.",
        },
        "a_retenir": "À retenir : un procédé à outillage ne se choisit qu'au-delà du seuil de rentabilité "
                     "N* = Δoutillage / Δcoût unitaire.",
    },
    {
        "id": "at177",
        "chapitre": "Bloc 13",
        "titre": "Exporter un STL : combien de facettes ?",
        "theme": "Procédés",
        "fiche": "13.7",
        "figure": "stl_facettes",
        "vocabulaire": [
            ("STL",
             "format de fichier qui décrit une surface par des facettes triangulaires (3 sommets + 1 normale)."),
            ("Flèche (écart de corde)",
             "l'écart maximal entre la surface exacte et la facette qui la remplace."),
            ("Maillage étanche",
             "un volume fermé, sans trou entre facettes, que l'imprimante sait remplir."),
        ],
        "enonce": "Un alésage de rayon 40 mm doit être imprimé en 3D. On veut une flèche (écart de corde) d'au plus "
                  "0,05 mm (donnée d'énoncé).",
        "etapes": [
            {"type": "numerique", "label": "Flèche avec 24 facettes",
             "unite": "mm", "attendu": 0.3422, "tol": 0.002,
             "consigne": "Calcule f = R (1 − cos(π / n)) pour n = 24 facettes.",
             "indice": "π / 24 = 7,5° ; cos(7,5°) ≈ 0,99144.",
             "pieges": [(1.363, "1,36 : tu as pris cos(2π / n) au lieu de cos(π / n) : la flèche se mesure au milieu "
                                 "de la corde, soit un demi-angle."),
                        (0.0001044, "0,0001 : calculatrice en degrés alors que π / 24 est en radians (ou calcule "
                                    "cos 7,5° en degrés).")],
             "aide": "40 × (1 − cos 7,5°) ≈ 0,342 mm : trop grossier."},
            {"type": "numerique", "label": "Nombre minimal de facettes",
             "unite": "facettes", "attendu": 63, "tol": 0.1,
             "consigne": "Calcule le nombre minimal de facettes : n ≥ π / arccos(1 − f_max / R), arrondi à l'entier "
                         "supérieur.",
             "indice": "1 − 0,05 / 40 = 0,99875 ; arccos en radians.",
             "pieges": [(62, "62 : on arrondit à l'entier SUPÉRIEUR, sinon la flèche dépasse la tolérance."),
                        (126, "126 : tu as pris 2π au lieu de π : la flèche se mesure au milieu de la corde.")],
             "aide": "arccos(0,99875) ≈ 0,05001 rad ; π / 0,05001 ≈ 62,8 → 63 facettes."},
            {"type": "qcm", "label": "Ce que le fichier transmet",
             "question": "Le STL est envoyé. Que transmet-il à l'imprimante ?",
             "options": ["La géométrie, la tolérance de l'alésage et la matière",
                         "Seulement des triangles : ni cote, ni tolérance, ni unité, ni matière",
                         "L'arbre de construction CAO"], "bonne": 1,
             "indice": "Que contient une facette ?",
             "diagnostics": {0: "Le STL ne porte ni tolérance ni matière : on les règle dans le logiciel de l'imprimante "
                                 "ou on les précise à part.",
                             2: "L'arbre CAO reste dans le fichier natif ; le STL n'est qu'un maillage."}},
        ],
        "corrige": {
            "enonce": "Alésage R = 40 mm ; flèche admise 0,05 mm.",
            "regle": "**f = R (1 − cos(π / n))** ; **n ≥ π / arccos(1 − f_max / R)**, arrondi à l'entier supérieur.",
            "conversions": "Angles en radians pour arccos.",
            "remplacement": "f(24) = 40 × (1 − cos(π / 24)) ; n ≥ π / arccos(1 − 0,05 / 40) (radians).",
            "calcul": "**f ≈ 0,342 mm** avec 24 facettes ; **63 facettes** minimum.",
            "verification": "Avec 63 facettes : f = 40 × (1 − cos(π / 63)) ≈ 0,0497 mm ≤ 0,05 mm.",
        },
        "a_retenir": "À retenir : le STL remplace les courbes par des triangles ; la tolérance de corde fixe le nombre "
                     "de facettes, et le fichier ne porte ni cote ni tolérance.",
    },
]

# ===========================================================================
# 5. GÉNÉRATEURS (nouvelle famille « Procédés »)
# ===========================================================================
GENERATEUR = '''
def gen_seuil_rentabilite():
    """Seuil de rentabilité entre un procédé sans outillage et un procédé à outillage."""
    out = random.choice([10000, 15000, 20000, 25000, 30000, 40000, 50000])
    ca = random.choice([6, 8, 9, 10, 12, 15])
    cb = random.choice([c for c in (0.5, 1, 1.5, 2, 3) if c < ca - 2])
    N = out / (ca - cb)
    diag = []
    for val, msg in (
            (out / ca, "Tu as divisé par le coût unitaire du procédé sans outillage : il faut la DIFFÉRENCE des coûts "
                       "unitaires."),
            (out / cb, "Tu as divisé par le coût unitaire du procédé à outillage : il faut la DIFFÉRENCE des coûts "
                       "unitaires."),
            (out / (ca + cb), "Tu as additionné les coûts unitaires : c'est l'économie par pièce (A − B) qui amortit "
                              "l'outillage."),
    ):
        if abs(val - N) > 1.5 and all(abs(val - d["v"]) > 1 for d in diag):
            diag.append(_diag(round(val, 1), msg))
    return {
        "titre": "Procédés — seuil de rentabilité",
        "enonce": (f"Une pièce peut être usinée pour **{fr(ca, 2)} € pièce** sans outillage, ou moulée avec un outillage "
                   f"de **{fr(out, 0)} €** et **{fr(cb, 2)} € par pièce**. Calcule le seuil de rentabilité N* (nombre "
                   "de pièces pour lequel les deux coûts totaux sont égaux)."),
        "rep": round(N, 1), "tol": 1.0, "unite": "pièces", "decimales": 1,
        "diag": diag,
        "corr": [
            f"**Ce que dit l'énoncé.** Usinage {fr(ca, 2)} €/pièce ; moulage : outillage {fr(out, 0)} € + {fr(cb, 2)} €/pièce.",
            "**La règle.** Au seuil, les coûts totaux sont égaux : ca × N = outillage + cb × N.",
            f"**Le calcul.** N* = {fr(out, 0)} / ({fr(ca, 2)} − {fr(cb, 2)}) = {fr(N, 1)} pièces.",
            "**Ce que cela apprend.** En dessous du seuil, on usine ; au-dessus, l'outillage est amorti.",
        ],
        "indice": "N* = outillage / (coût unitaire sans outillage − coût unitaire avec outillage).",
    }


def gen_facettes_stl():
    """Nombre minimal de facettes pour respecter une flèche donnée sur un cercle."""
    R = random.choice([10, 15, 20, 25, 30, 40, 50])
    f = random.choice([0.01, 0.02, 0.05, 0.1])
    x = math.pi / math.acos(1 - f / R)
    n = math.ceil(x)
    diag = []
    for val, msg in (
            (math.floor(x), "On arrondit à l'entier SUPÉRIEUR : avec moins de facettes, la flèche dépasse la tolérance."),
            (math.ceil(2 * math.pi / math.acos(1 - f / R)), "Tu as pris 2π au lieu de π : la flèche se mesure au milieu "
                                                            "de la corde, soit un demi-angle π / n."),
    ):
        if val != n and all(val != d["v"] for d in diag):
            diag.append(_diag(val, msg))
    return {
        "titre": "Procédés — facettes d'un fichier STL",
        "enonce": (f"Un cercle de rayon **{R} mm** doit être exporté en STL avec une flèche (écart de corde) d'au plus "
                   f"**{fr(f, 2)} mm**. Combien de facettes faut-il au minimum sur le tour ?"),
        "rep": n, "tol": 0.5, "unite": "facettes",
        "diag": diag,
        "corr": [
            f"**Ce que dit l'énoncé.** R = {R} mm, flèche admise {fr(f, 2)} mm.",
            "**La règle.** f = R (1 − cos(π / n)), donc n ≥ π / arccos(1 − f_max / R) (radians).",
            f"**Le calcul.** π / arccos(1 − {fr(f, 2)} / {R}) = {fr(x, 2)} → arrondi supérieur : {n} facettes.",
            "**Je vérifie.** Avec n facettes, la flèche est juste sous la tolérance ; avec n − 1, elle la dépasse.",
        ],
        "indice": "n ≥ π / arccos(1 − f_max / R), arccos en radians, arrondi à l'entier supérieur.",
    }
'''

# ===========================================================================
# 6. QUIZ — nouvelle catégorie « Procédés : compléments et choix »
#    positions de la bonne réponse : 2, 0, 3, 1, 1, 3, 0, 2
# ===========================================================================
QUIZ_PROCEDES = [
    ("Quel procédé choisir pour fabriquer un tube plastique en grande longueur ?",
     ["Le thermoformage", "Le soufflage", "L'extrusion", "La compression"], 2,
     "Section constante, grande longueur, production continue : c'est l'extrusion (une vis pousse la matière à travers "
     "une filière).", "Base"),
    ("Quel procédé est fait pour les corps creux fermés (flacons, bidons, réservoirs) ?",
     ["Le soufflage", "L'extrusion", "Le thermoformage", "Le frittage"], 0,
     "Une paraison ou une préforme est gonflée dans un moule en deux coquilles : seule la forme extérieure est maîtrisée.",
     "Base"),
    ("Pourquoi le thermoformage convient-il aux petites séries de grandes coques ?",
     ["Parce qu'il donne deux faces précises sans aucune reprise après formage", "Parce qu'il travaille les thermodurcissables",
      "Parce qu'il ne demande aucune matière", "Parce que son outillage, à une seule face, est simple et peu coûteux"], 3,
     "Un seul moule, à une face, chauffe une plaque et l'aspire : outillage économique. En contrepartie, une seule face "
     "est précise et l'épaisseur diminue dans les angles.", "Intermédiaire"),
    ("Qu'est-ce que le frittage ?",
     ["Fondre une poudre puis la couler", "Chauffer une poudre mise en forme sous son point de fusion pour souder ses grains",
      "Comprimer une poudre à froid sans chauffer", "Un traitement de surface"], 1,
     "Les grains se soudent à leurs points de contact sans que le métal fonde. C'est l'étape commune à la métallurgie "
     "des poudres et au MIM.", "Base"),
    ("Quelle contrainte de dessin le MIM impose-t-il ?",
     ["Aucune, il reproduit exactement le moule", "Un retrait important au frittage, compensé par un moule plus grand",
      "Une pièce obligatoirement de révolution", "Une épaisseur d'au moins plusieurs centimètres"], 1,
     "Le liant retiré laisse des vides que le frittage referme : la pièce rétrécit nettement ; la valeur est donnée par "
     "le fournisseur.", "Intermédiaire"),
    ("Il faut fixer une plaquette de carbure sur un corps d'outil en acier. Quel assemblage choisir ?",
     ["Le soudage à l'arc", "Le soudage par ultrasons", "Le soudage par friction", "Le brasage fort"], 3,
     "Deux matériaux différents, et le carbure ne doit pas fondre : seul le métal d'apport fond et s'infiltre par "
     "capillarité. Les ultrasons visent les thermoplastiques ; la friction, des pièces de révolution.", "Piège"),
    ("Que contient un fichier STL ?",
     ["Des facettes triangulaires (3 sommets et une normale chacune)", "Les cotes et les tolérances de la pièce",
      "L'arbre de construction CAO", "La matière et la couleur de la pièce"], 0,
     "Le STL n'est qu'un maillage de triangles, sans unité ni tolérance : c'est le format de la fabrication additive, "
     "pas celui de l'usinage.", "Base"),
    ("Usinage : 10 € pièce sans outillage. Moulage : outillage de 20 000 € et 2 € pièce. Quel est le seuil de "
     "rentabilité (nombre de pièces pour lequel les deux coûts totaux sont égaux) ?",
     ["2 000", "10 000", "2 500", "1 667"], 2,
     "N* = 20 000 / (10 − 2) = 2 500 pièces. 2 000 serait 20 000 / 10 (sans la différence des coûts).", "Calcul"),
]
