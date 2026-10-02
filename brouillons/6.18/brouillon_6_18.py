# -*- coding: utf-8 -*-
# BROUILLON — fiche 6.18 « Mécanismes de transmission : accoupler, débrayer, limiter, freiner,
# transformer le mouvement » (référentiel S5.2). Rien de ceci n'est encore dans app.py.
# _k_defs, _k_fl (6.15) et _k_apparait (6.16) existent déjà dans app.py.
import math

# ===========================================================================
# 1. FIGURES
# ===========================================================================

def chaine_transmission():
    """La chaîne de transmission d'un axe : chaque composant a une FONCTION (un verbe)."""
    p = [_k_defs(), _txt(30, 24, "Une chaîne de transmission : chaque composant remplit une fonction", 13, TRAIT, "start", True)]
    blocs = (("moteur", "CONVERTIR", FIN), ("accouplement", "ACCOUPLER", ALESAGE), ("limiteur", "PROTÉGER", ALERTE),
             ("courroie", "ADAPTER la vitesse", ARBRE), ("frein", "IMMOBILISER", ALERTE), ("vis-écrou", "TRANSFORMER", OK))
    x = 30
    for i, (nom, verbe, c) in enumerate(blocs):
        p.append(f"<rect x='{x}' y='70' width='100' height='56' rx='8' fill='#ffffff' stroke='{c}' stroke-width='2'/>")
        p.append(_txt(x + 50, 94, nom, 12, TRAIT, "middle", True))
        p.append(_txt(x + 50, 114, verbe, 10, c, "middle", True))
        if i < len(blocs) - 1:
            p.append(f"<line x1='{x + 100}' y1='98' x2='{x + 122}' y2='98' stroke='{FIN}' stroke-width='3' stroke-dasharray='6 4'>"
                     "<animate attributeName='stroke-dashoffset' values='20;0' dur='0.8s' repeatCount='indefinite'/></line>")
        x += 122
    p.append(f"<rect x='{x - 10}' y='78' width='40' height='40' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.6'>"
             "<animateTransform attributeName='transform' type='translate' values='0,0; 6,0; 0,0' dur='2s' repeatCount='indefinite'/></rect>")
    p.append(_txt(x + 10, 140, "chariot", 10, TRAIT, "middle"))
    p.append(_txt(80, 158, "rotation", 10, FIN, "middle"))
    p.append(_txt(400, 158, "rotation, vitesse et couple adaptés", 10, FIN, "middle"))
    p.append(_txt(700, 158, "translation", 10, FIN, "middle"))
    p.append(f"<rect x='30' y='176' width='745' height='118' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    for i, t in enumerate((
            "Sans changer la vitesse : accoupler (relier deux arbres), embrayer (relier ou séparer en marche),",
            "limiter (glisser ou déclencher au-delà d'un couple), freiner (ralentir, arrêter, maintenir).",
            "En changeant la vitesse : courroie, chaîne, engrenages (fiches 6.11, 6.13, 12.5).",
            "En transformant le mouvement : vis-écrou, came, systèmes articulés (rotation ↔ translation).",
            "À chaque étage, une part de la puissance se perd : P sortie = η × P entrée (fiche 8.5).")):
        p.append(_txt(46, 198 + 22 * i, t, 12, TRAIT, "start", i == 4))
    return _svg("".join(p), 805, 308)


def accouplement_defauts():
    p = [_k_defs(), _txt(40, 24, "Deux arbres ne sont jamais parfaitement alignés : trois défauts", 13, TRAIT, "start", True)]
    cadres = ((30, "DÉCALAGE RADIAL", "axes parallèles, décalés"), (275, "DÉFAUT ANGULAIRE", "axes qui se croisent"),
              (520, "ÉCART AXIAL", "arbres qui s'éloignent (dilatation)"))
    for x0, titre, sous in cadres:
        p.append(f"<rect x='{x0}' y='40' width='225' height='170' rx='8' fill='#ffffff' stroke='{ALESAGE}' stroke-width='2'/>")
        p.append(_txt(x0 + 112, 62, titre, 12, ALESAGE, "middle", True))
        p.append(_txt(x0 + 112, 196, sous, 10, FIN, "middle"))
    # radial
    p.append(f"<rect x='45' y='112' width='85' height='14' fill='#e2e8f0' stroke='{TRAIT}'/>")
    p.append(f"<rect x='140' y='122' width='95' height='14' fill='#e2e8f0' stroke='{TRAIT}'>"
             "<animateTransform attributeName='transform' type='translate' values='0,0; 0,-8; 0,0' dur='2s' repeatCount='indefinite'/></rect>")
    p.append(f"<line x1='40' y1='119' x2='240' y2='119' stroke='{AXE}' stroke-dasharray='5 4'/>")
    # angulaire
    p.append(f"<rect x='290' y='112' width='90' height='14' fill='#e2e8f0' stroke='{TRAIT}'/>")
    p.append(f"<rect x='388' y='112' width='90' height='14' fill='#e2e8f0' stroke='{TRAIT}'>"
             "<animateTransform attributeName='transform' type='rotate' values='0 388 119; -7 388 119; 0 388 119' dur='2s' repeatCount='indefinite'/></rect>")
    # axial
    p.append(f"<rect x='535' y='112' width='90' height='14' fill='#e2e8f0' stroke='{TRAIT}'/>")
    p.append(f"<rect x='640' y='112' width='90' height='14' fill='#e2e8f0' stroke='{TRAIT}'>"
             "<animateTransform attributeName='transform' type='translate' values='0,0; 8,0; 0,0' dur='2s' repeatCount='indefinite'/></rect>")
    for x in (130, 380, 625):
        p.append(f"<rect x='{x + 2}' y='98' width='12' height='42' rx='3' fill='#fde68a' stroke='{ARBRE}' stroke-width='1.6'/>")
    p.append(_txt(135, 92, "accouplement élastique", 10, ARBRE, "middle", True))
    p.append(f"<rect x='30' y='222' width='715' height='76' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 244, "Accouplement RIGIDE : il exige un alignement parfait. Moteur et réducteur, chacun sur ses paliers,", 12, TRAIT, "start", True))
    p.append(_txt(46, 264, "forment alors un montage hyperstatique (fiche 6.17) : les défauts deviennent des efforts sur les roulements.", 12, TRAIT))
    p.append(_txt(46, 284, "Accouplement ÉLASTIQUE ou à soufflet : il tolère ces défauts (dans les limites du catalogue) et amortit les à-coups.", 12, FIN))
    return _svg("".join(p), 775, 312)


def embrayage_limiteur_frein():
    p = [_k_defs(), _txt(40, 24, "Embrayage, limiteur, frein : le même frottement, trois fonctions", 13, TRAIT, "start", True)]
    cadres = ((30, "EMBRAYAGE", "relier ou séparer en marche", ALESAGE),
              (275, "LIMITEUR DE COUPLE", "en cas de blocage, il glisse", ALERTE),
              (520, "FREIN À MANQUE DE COURANT", "serré sans énergie, desserré alimenté", OK))
    for x0, titre, sous, c in cadres:
        p.append(f"<rect x='{x0}' y='40' width='225' height='215' rx='8' fill='#ffffff' stroke='{c}' stroke-width='2'/>")
        p.append(_txt(x0 + 112, 62, titre, 12, c, "middle", True))
        p.append(_txt(x0 + 112, 240, sous, 10, FIN, "middle"))
    # embrayage : deux disques, un ressort, une commande qui écarte
    p.append(f"<rect x='45' y='132' width='60' height='12' fill='#e2e8f0' stroke='{TRAIT}'/>")
    p.append(f"<rect x='165' y='132' width='60' height='12' fill='#e2e8f0' stroke='{TRAIT}'/>")
    p.append(f"<rect x='105' y='96' width='10' height='84' fill='{ALESAGE}'/>")
    p.append(f"<rect x='117' y='96' width='10' height='84' fill='#fde68a' stroke='{ARBRE}'>"
             "<animateTransform attributeName='transform' type='translate' values='0,0; 0,0; 14,0; 14,0; 0,0' dur='4s' repeatCount='indefinite'/></rect>")
    p.append(f"<path d='M 130 138 l 6 -8 l 6 16 l 6 -16 l 6 16 l 6 -8' fill='none' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(_txt(142, 120, "ressort", 9, FIN, "middle"))
    p.append(_k_fl(122, 88, 150, 88, ALESAGE, "kb", 2))
    p.append(_txt(45, 80, "commande : écarte = débrayé", 9, ALESAGE, "start"))
    p.append(_txt(142, 206, "C = n f F rmoy", 13, ALESAGE, "middle", True))
    # limiteur : moyeu, garnitures, écrou de réglage
    p.append(f"<circle cx='387' cy='138' r='44' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<g><line x1='387' y1='138' x2='387' y2='98' stroke='{ALERTE}' stroke-width='3'/>"
             "<animateTransform attributeName='transform' type='rotate' values='0 387 138; 360 387 138' dur='3s' repeatCount='indefinite'/></g>")
    p.append(f"<circle cx='387' cy='138' r='14' fill='#ffffff' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<circle cx='387' cy='138' r='30' fill='none' stroke='{ARBRE}' stroke-width='5' opacity='0.7'/>")
    p.append(_txt(340, 96, "garnitures", 9, ARBRE, "end"))
    p.append(_txt(387, 84, "ressort + écrou de réglage", 9, TRAIT, "middle"))
    p.append(_txt(387, 206, "couple de réglage", 11, ALERTE, "middle", True))
    p.append(_txt(387, 222, "> couple utile maxi", 10, TRAIT, "middle"))
    # frein à manque de courant
    p.append(f"<rect x='575' y='100' width='30' height='76' fill='#e2e8f0' stroke='{TRAIT}'/>")
    p.append(_txt(590, 92, "disque", 9, FIN, "middle"))
    p.append(f"<rect x='612' y='106' width='12' height='64' fill='#fde68a' stroke='{ARBRE}'>"
             "<animateTransform attributeName='transform' type='translate' values='0,0; 0,0; 10,0; 10,0; 0,0' dur='4s' repeatCount='indefinite'/></rect>")
    p.append(f"<path d='M 626 138 l 4 -8 l 4 16 l 4 -16 l 4 16 l 4 -8' fill='none' stroke='{TRAIT}' stroke-width='1.6'/>")
    p.append(_txt(634, 186, "ressort", 9, FIN, "middle"))
    p.append(f"<rect x='648' y='104' width='60' height='68' fill='#ffffff' stroke='{OK}' stroke-width='2'/>")
    p.append(_txt(678, 134, "électro-", 10, OK, "middle"))
    p.append(_txt(678, 148, "aimant", 10, OK, "middle"))
    p.append(_txt(632, 206, "coupure = ressort serre", 11, OK, "middle", True))
    p.append(_txt(632, 222, "(sécurité positive)", 10, TRAIT, "middle"))
    p.append(f"<rect x='30' y='266' width='715' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 288, "Même physique (des surfaces pressées qui frottent), trois intentions : transmettre, protéger, arrêter.", 12, TRAIT))
    return _svg("".join(p), 775, 314)


def vis_un_deux_filets():
    p = [_k_defs(), _txt(40, 24, "Vis à un ou deux filets : un tour fait avancer l'écrou du pas de l'hélice", 13, TRAIT, "start", True)]
    for x0, titre, nf in ((30, "1 FILET : ph = P", 1), (395, "2 FILETS : ph = 2 × P", 2)):
        p.append(f"<rect x='{x0}' y='40' width='350' height='230' rx='8' fill='#ffffff' stroke='{ALESAGE}' stroke-width='2'/>")
        p.append(_txt(x0 + 175, 62, titre, 12, ALESAGE, "middle", True))
        # vis vue de côté : filets en traits obliques, P = 24 px
        xv = x0 + 30
        p.append(f"<rect x='{xv}' y='120' width='290' height='34' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.4'/>")
        for k in range(12):
            xx = xv + 6 + 24 * k
            c = ARBRE if (nf == 2 and k % 2) else TRAIT
            p.append(f"<line x1='{xx}' y1='154' x2='{xx + 12 * nf}' y2='120' stroke='{c}' stroke-width='2'/>")
        # écrou qui avance d'un pas d'hélice par tour
        d = 24 * nf
        p.append(f"<rect x='{xv + 70}' y='110' width='56' height='54' rx='4' fill='none' stroke='{OK}' stroke-width='3'>"
                 f"<animateTransform attributeName='transform' type='translate' values='0,0; {d},0; {d},0; 0,0' "
                 "keyTimes='0;0.45;0.8;1' dur='3s' repeatCount='indefinite'/></rect>")
        p.append(f"<line x1='{xv + 70}' y1='186' x2='{xv + 70 + d}' y2='186' stroke='{OK}' stroke-width='2'/>")
        p.append(_txt(xv + 70 + d / 2, 204, "1 tour = " + ("P" if nf == 1 else "2 P"), 12, OK, "middle", True))
        p.append(f"<line x1='{xv + 6}' y1='98' x2='{xv + 30}' y2='98' stroke='{FIN}'/>")
        p.append(_txt(xv + 18, 92, "P", 11, FIN, "middle", True))
        p.append(_txt(x0 + 175, 244, "pas apparent P : distance entre deux filets voisins" if nf == 1
                      else "les deux filets (noir, orange) s'intercalent", 10, FIN, "middle"))
    p.append(f"<rect x='30' y='282' width='715' height='54' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 304, "v = ph × N, avec ph = P × nombre de filets. Exemple : Tr 20 × 8 (P4) = pas de 4 mm, 2 filets, ph = 8 mm.", 12, TRAIT, "start", True))
    p.append(_txt(46, 324, "Plus l'hélice s'incline (ph grand), plus la vis est rapide… et plus elle risque d'être réversible.", 12, FIN))
    return _svg("".join(p), 775, 350)


def came_excentrique():
    p = [_k_defs(), _txt(40, 24, "Came disque et poussoir à galet : la forme de la came impose le mouvement", 13, TRAIT, "start", True)]
    cx, cy, e, r0 = 190, 200, 22, 70
    # came excentrique : disque de rayon r0, centre décalé de e par rapport à l'axe de rotation
    p.append(f"<g><circle cx='{cx + e}' cy='{cy}' r='{r0}' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>"
             f"<circle cx='{cx + e}' cy='{cy}' r='3' fill='{FIN}'/>"
             f"<animateTransform attributeName='transform' type='rotate' values='0 {cx} {cy}; 360 {cx} {cy}' dur='4s' repeatCount='indefinite'/></g>")
    p.append(f"<circle cx='{cx}' cy='{cy}' r='6' fill='#ffffff' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(_txt(cx - 10, cy + 22, "O (axe)", 10, TRAIT, "end"))
    # poussoir : se déplace verticalement de 2e (approximation sinusoïdale)
    # galet posé sur le contour : à l'instant 0 (excentration horizontale), le haut de la came au-dessus
    # de l'axe est à √(r0² − e²) ; la rotation (sens horaire à l'écran) fait descendre puis monter le galet
    ymoy = cy - math.sqrt(r0 * r0 - e * e) - 10
    p.append(f"<g><circle cx='{cx}' cy='{ymoy:.1f}' r='10' fill='#ffffff' stroke='{OK}' stroke-width='3'/>"
             f"<rect x='{cx - 5}' y='{ymoy - 62:.1f}' width='10' height='52' fill='{OK}'/>"
             f"<animateTransform attributeName='transform' type='translate' values='0,0; 0,{e}; 0,0; 0,{-e}; 0,0' "
             "dur='4s' repeatCount='indefinite'/></g>")
    p.append(f"<rect x='{cx - 14}' y='{ymoy - 70:.1f}' width='4' height='44' fill='#cbd5e1'/>")
    p.append(f"<rect x='{cx + 10}' y='{ymoy - 70:.1f}' width='4' height='44' fill='#cbd5e1'/>")
    ybas = ymoy
    p.append(_txt(cx + 22, ybas - 40, "poussoir guidé", 10, OK, "start", True))
    p.append(_txt(cx + 22, ybas - 6, "galet", 10, OK, "start"))
    p.append(_txt(cx + e + r0 + 8, cy + 40, "came (excentrée de e)", 10, TRAIT, "start"))
    # loi de levée
    gx, gy, gw, gh = 430, 200, 300, 90
    p.append(f"<rect x='410' y='60' width='340' height='200' rx='6' fill='#ffffff' stroke='{FIN}'/>")
    p.append(_txt(422, 80, "Loi de levée : position du poussoir selon l'angle", 11, TRAIT, "start", True))
    p.append(f"<line x1='{gx}' y1='{gy}' x2='{gx + gw}' y2='{gy}' stroke='{FIN}'/>")
    pts = " ".join(f"{gx + gw * i / 120:.1f},{gy - 45 + 40 * math.sin(2 * math.pi * i / 120):.1f}" for i in range(121))
    p.append(f"<polyline points='{pts}' fill='none' stroke='{OK}' stroke-width='2.4'/>")
    p.append(f"<line x1='{gx + gw + 6}' y1='{gy - 85}' x2='{gx + gw + 6}' y2='{gy - 5}' stroke='{ARBRE}' stroke-width='1.6'/>")
    p.append(_txt(gx + gw + 10, gy - 42, "course", 9, ARBRE, "start", True))
    p.append(_txt(gx + gw + 10, gy - 30, "= 2 e", 9, ARBRE, "start", True))
    for deg, lab in ((0, "0°"), (180, "180°"), (360, "360°")):
        p.append(_txt(gx + gw * deg / 360, gy + 16, lab, 9, FIN, "middle"))
    p.append(_txt(422, 240, "Came excentrique : le poussoir monte et descend sans à-coup. Une came de", 10, FIN))
    p.append(_txt(422, 253, "forme quelconque impose montées, arrêts et descentes à volonté.", 10, FIN))
    p.append(f"<rect x='30' y='290' width='715' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 312, "Le contact doit être maintenu : ressort de rappel, poids, ou came à rainure (le galet roule dans une gorge).", 12, TRAIT))
    return _svg("".join(p), 775, 338)


def courroies_chaines():
    p = [_k_defs(), _txt(40, 24, "Courroies et chaînes : ce qui glisse, ce qui ne glisse pas", 13, TRAIT, "start", True)]
    cadres = ((30, "COURROIE TRAPÉZOÏDALE", "adhérence : glisse un peu", ARBRE),
              (275, "COURROIE CRANTÉE", "obstacle : rapport exact", ALESAGE),
              (520, "CHAÎNE À ROULEAUX", "obstacle : rapport exact", OK))
    for x0, titre, sous, c in cadres:
        p.append(f"<rect x='{x0}' y='40' width='225' height='200' rx='8' fill='#ffffff' stroke='{c}' stroke-width='2'/>")
        p.append(_txt(x0 + 112, 62, titre, 12, c, "middle", True))
        p.append(_txt(x0 + 112, 226, sous, 10, FIN, "middle"))
    # trapézoïdale : section dans la gorge
    p.append(f"<path d='M 95 90 L 175 90 L 160 150 L 110 150 Z' fill='none' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<path d='M 112 100 L 158 100 L 148 140 L 122 140 Z' fill='{ARBRE}' opacity='0.8'/>")
    p.append(_txt(142, 172, "les flancs coincent dans la gorge", 10, TRAIT, "middle"))
    p.append(_txt(142, 190, "r ≈ d1 / d2", 12, ARBRE, "middle", True))
    # crantée : dents
    for k in range(7):
        p.append(f"<rect x='{300 + 26 * k}' y='112' width='14' height='14' fill='{ALESAGE}'/>")
    p.append(f"<rect x='295' y='100' width='190' height='12' fill='{ALESAGE}'>"
             "<animateTransform attributeName='transform' type='translate' values='0,0; 26,0' dur='1.5s' repeatCount='indefinite'/></rect>")
    p.append(_txt(387, 172, "les dents engrènent sur la poulie", 10, TRAIT, "middle"))
    p.append(_txt(387, 190, "r = Z1 / Z2", 12, ALESAGE, "middle", True))
    # chaîne : maillons
    for k in range(6):
        x = 548 + 30 * k
        p.append(f"<rect x='{x}' y='104' width='34' height='18' rx='9' fill='none' stroke='{TRAIT}' stroke-width='2'/>")
        p.append(f"<circle cx='{x + 9}' cy='113' r='5' fill='{OK}'/>")
    p.append(_txt(632, 172, "les rouleaux engrènent sur le pignon", 10, TRAIT, "middle"))
    p.append(_txt(632, 190, "r = Z1 / Z2", 12, OK, "middle", True))
    p.append(f"<rect x='30' y='252' width='715' height='54' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 274, "r = N2 / N1 (rapport de transmission). Courroie lisse : silencieuse, amortit, peut patiner (protection non réglée).", 12, TRAIT))
    p.append(_txt(46, 294, "Crantée ou chaîne : synchronisme exact, mais un blocage casse quelque chose — d'où le limiteur de couple.", 12, TRAIT, "start", True))
    return _svg("".join(p), 775, 320)


# --- figure à curseurs : vis-écrou
def dyn_vis_ecrou(P=4.0, nf=1.0, N=300.0, f=0.15):
    """Vis trapézoïdale Ø 20 : vitesse, pas de l'hélice, angle d'hélice et réversibilité."""
    nf = int(round(nf))
    ph = P * nf
    d2 = 20 - 0.5 * P
    alpha = math.degrees(math.atan(ph / (math.pi * d2)))
    phi = math.degrees(math.atan(f))
    v = ph * N / 60
    irrev = alpha <= phi
    c = OK if irrev else ALERTE
    p = [_k_defs(), _txt(30, 24, f"Exemple de calcul : vis de Ø 20, pas {_fr_court(P, 1)} mm, {nf} filet{'s' if nf > 1 else ''}, {int(N)} tr/min", 13, TRAIT, "start", True)]
    # triangle de l'hélice déroulée : base π d2, hauteur ph
    bx, by, bw = 60, 250, 300
    hp = bw * ph / (math.pi * d2)
    p.append(f"<line x1='{bx}' y1='{by}' x2='{bx + bw}' y2='{by}' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<line x1='{bx + bw}' y1='{by}' x2='{bx + bw}' y2='{by - hp:.1f}' stroke='{ALESAGE}' stroke-width='2.4'/>")
    p.append(f"<line x1='{bx}' y1='{by}' x2='{bx + bw}' y2='{by - hp:.1f}' stroke='{c}' stroke-width='3'/>")
    p.append(_txt(bx + bw / 2, by + 18, "un tour déroulé : π × d2", 11, TRAIT, "middle"))
    p.append(_txt(bx + bw + 8, by - hp / 2, f"ph = {_fr_court(ph, 1)} mm", 11, ALESAGE, "start", True))
    p.append(_txt(bx + bw + 8, by - hp / 2 + 20, f"α = {_fr_court(alpha, 1)}° (hélice)", 11, c, "start", True))
    # angle de frottement en pointillé
    hf = bw * math.tan(math.radians(phi))
    p.append(f"<line x1='{bx}' y1='{by}' x2='{bx + bw}' y2='{by - hf:.1f}' stroke='{FIN}' stroke-width='1.4' stroke-dasharray='5 4'/>")
    p.append(_txt(bx + bw + 8, by - hp / 2 + 38, f"φ = {_fr_court(phi, 1)}° (frottement, pointillé)", 10, FIN))
    x0 = 470
    p.append(f"<rect x='{x0}' y='44' width='290' height='196' rx='6' fill='#ffffff' stroke='{c}' stroke-width='1.8'/>")
    lignes = [(f"Pas de l'hélice : ph = {_fr_court(P, 1)} × {nf} = {_fr_court(ph, 1)} mm", TRAIT, False),
              (f"Vitesse : v = ph × N = {_fr_court(ph * N, 0)} mm/min", TRAIT, False),
              (f"            soit {_fr_court(v, 1)} mm/s", TRAIT, True),
              (f"Angle d'hélice : tan α = ph / (π d2) → {_fr_court(alpha, 1)}°", TRAIT, False),
              (f"Angle de frottement : tan φ = f → {_fr_court(phi, 1)}°", TRAIT, False),
              ("α ≤ φ : IRRÉVERSIBLE" if irrev else "α > φ : RÉVERSIBLE", c, True),
              ("la charge ne fait pas tourner la vis" if irrev else "la charge peut faire tourner la vis :", c, False),
              ("" if irrev else "il faut un frein pour la tenir", c, False)]
    for i, (t, col, g) in enumerate(lignes):
        if t:
            p.append(_txt(x0 + 12, 68 + 22 * i, t, 12, col, "start", g))
    p.append(_txt(30, 292, "Ajouter des filets accélère la vis, mais incline davantage l'hélice : au-delà de φ, elle devient réversible.", 11, FIN))
    return _svg("".join(p), 775, 306)


FIGURES_NOUVELLES = {
    "chaine_transmission": ("Une chaîne de transmission, composant par composant", chaine_transmission),
    "accouplement_defauts": ("Les trois défauts d'alignement et l'accouplement élastique", accouplement_defauts),
    "embrayage_limiteur_frein": ("Embrayage, limiteur de couple, frein à manque de courant", embrayage_limiteur_frein),
    "vis_un_deux_filets": ("Vis à un ou deux filets : pas apparent et pas de l'hélice", vis_un_deux_filets),
    "came_excentrique": ("Came excentrique et poussoir à galet : la loi de levée", came_excentrique),
    "courroies_chaines": ("Courroies et chaînes : adhérence ou obstacle", courroies_chaines),
}
DYN_NOUVELLE = {
    "vis_ecrou_curseurs": (
        "Change le pas, le nombre de filets, la vitesse et le frottement : vitesse et réversibilité suivent",
        dyn_vis_ecrou,
        [{"nom": "P", "label": "Pas apparent P (mm)", "min": 2.0, "max": 5.0, "defaut": 4.0, "pas": 1.0},
         {"nom": "nf", "label": "Nombre de filets", "min": 1.0, "max": 4.0, "defaut": 1.0, "pas": 1.0},
         {"nom": "N", "label": "Vitesse N (tr/min)", "min": 100.0, "max": 1500.0, "defaut": 300.0, "pas": 100.0},
         {"nom": "f", "label": "Frottement f (donné)", "min": 0.05, "max": 0.30, "defaut": 0.15, "pas": 0.05}]),
}

# ===========================================================================
# 2. FICHE 6.18 — en FIN de bloc 6 (après la 6.17)
# ===========================================================================

FICHE_6_18 = {
    "id": '6.18',
    "titre": 'Mécanismes de transmission : accoupler, débrayer, limiter, freiner, transformer',
    "duree": '6 h',
    "cours": """### 1. Pourquoi cette fiche

Entre un moteur qui tourne et un chariot qui doit avancer, il y a toujours une **chaîne de transmission**.
Chaque composant y est pour une raison précise, qui se dit avec un verbe : **accoupler** deux arbres,
**débrayer** une machine sans arrêter le moteur, **protéger** la mécanique d'un blocage, **immobiliser**
une charge, **adapter** la vitesse, **transformer** une rotation en translation.

[[FIG:chaine_transmission]]

Le bon réflexe de concepteur : partir de la **fonction** (le verbe), puis choisir le composant. Pas
l'inverse. Cette fiche range les solutions comme le référentiel :

| Famille | Fonction | Composants |
|---|---|---|
| sans transformation, **même vitesse** | relier, séparer, protéger, arrêter | accouplement, embrayage, limiteur de couple, frein |
| sans transformation, **vitesse modifiée** | adapter vitesse et couple | courroie, chaîne, engrenages (fiches 6.11, 6.13, 12.5) |
| **avec transformation** du mouvement | rotation ↔ translation, ou mouvement imposé | vis-écrou, came, systèmes articulés |

Deux grandeurs suivent toute la chaîne : la **puissance**, qui se perd un peu à chaque étage
(P sortie = η × P entrée, fiche 8.5), et la **réversibilité** : la sortie peut-elle entraîner l'entrée ?

*Exemple que tout le monde a manipulé : le **cric à vis** d'une voiture. Vous tournez la manivelle, la
voiture monte ; vous lâchez la manivelle, la voiture **reste en l'air** : son poids ne fait pas tourner la
vis. Ce cric est **irréversible**. À l'inverse, sur une vis à billes, lâchez le moteur et la charge
redescend en faisant tourner la vis toute seule : elle est **réversible**. Pour un axe vertical, c'est la
différence entre « la charge tient » et « la charge tombe » (voir le cas industriel).*

### 2. Accoupler : relier deux arbres

[[FIG:accouplement_defauts]]

Un **accouplement** relie en permanence deux arbres alignés (moteur et réducteur, réducteur et vis). Il
transmet le couple, à la même vitesse. Mais deux arbres montés chacun sur leurs paliers ne sont **jamais
parfaitement alignés** : décalage radial, défaut angulaire, écart axial (dilatation).

| Type | Ce qu'il accepte | Quand le choisir |
|---|---|---|
| **rigide** (manchon, plateaux) | aucun défaut | arbres sur un même bâti usiné, alignement garanti |
| **élastique** (élément en élastomère) | petits défauts, amortit les à-coups | cas général : moteur + réducteur |
| **à soufflet, à lamelles** | petits défauts, **aucun jeu en rotation** : le moteur tourne de 1°, la vis tourne de 1° | positionnement précis, quand un capteur compte les tours pour connaître la position |
| **cardan** (joint de transmission) | grands angles, comme la rallonge à rotule d'une clé à cliquet | arbres volontairement non alignés (seul, il ne transmet pas une vitesse parfaitement constante : on les monte par paires) |

**Le lien avec la fiche 6.17.** Image : une porte montée sur quatre gonds pas parfaitement alignés ; elle
force, grince et use ses gonds. Deux arbres reliés rigidement, chacun tenu par deux roulements, c'est
pareil : les deux axes doivent être exactement dans le prolongement l'un de l'autre (la **coaxialité**),
sinon ce sont les roulements qui encaissent l'écart — le montage est **hyperstatique**. L'accouplement
élastique est une articulation souple entre les deux : chaque arbre garde son alignement, l'élastomère
absorbe la différence. On ne demande plus au monteur un alignement parfait.

### 3. Débrayer, limiter, freiner : trois fonctions, un même frottement

[[FIG:embrayage_limiteur_frein]]

**L'embrayage : relier ou séparer en marche** (embrayer = relier ; débrayer = séparer). Pourquoi ne pas
simplement arrêter le moteur ? Parce que certains moteurs ne peuvent pas démarrer en charge, ou mettent du
temps à se lancer. L'exemple connu est la **voiture** : le moteur tourne au ralenti au feu rouge, la pédale
sépare moteur et roues ; au démarrage, on relâche doucement, les disques glissent puis « collent ». En
atelier, sur une **presse à volant**, le volant reste lancé en permanence et l'embrayage ne le relie au
coulisseau que le temps d'un coup de presse.

- **embrayage à friction** : des disques pressés les uns contre les autres ; il démarre en douceur en
  glissant au début ;
- **embrayage à crabots** : deux couronnes à dents frontales qui s'emboîtent, comme les doigts de deux mains
  croisées ; il ne glisse jamais, mais s'enclenche à l'arrêt ou à vitesses égales, sinon les dents se
  cognent ;
- **coupleur hydraulique** : deux roues à aubes face à face dans un carter plein d'huile ; la première
  brasse l'huile, qui entraîne la seconde. Démarrage très progressif des machines lourdes à lancer
  (convoyeur chargé, broyeur).

Le couple qu'un embrayage à friction peut transmettre avant de glisser :

> **C = n × f × F × rmoy**

- **n** : le nombre de surfaces frottantes (un disque pris entre deux plateaux : n = 2) ;
- **f** : le coefficient de frottement des **garnitures** — les couronnes de matériau de friction fixées
  sur le disque, l'équivalent des plaquettes de frein — donné par le fabricant ou l'énoncé ;
- **F** : l'effort presseur (le ressort) ;
- **rmoy** : le rayon moyen des garnitures, **(R + r) / 2**, où l'on considère que tout le frottement
  s'applique (hypothèse retenue pour une garniture rodée).

*D'où vient la formule ? Chaque surface frotte avec une force tangentielle f × F (loi de Coulomb, fiche
12.1), appliquée en moyenne à la distance rmoy de l'axe : f × F × rmoy. Avec n surfaces, on multiplie par n.*

*Exemple : n = 2, f = 0,3, F = 1 500 N, garnitures de R = 60 mm et r = 40 mm. rmoy = 50 mm = 0,05 m.
C = 2 × 0,3 × 1 500 × 0,05 = **45 N·m**.*

**Le limiteur de couple : protéger.** Une chaîne de transmission a toujours un maillon faible (une
clavette, une dent, une chaîne). En cas de blocage — une pièce coincée dans un convoyeur —, le couple
monte jusqu'à casser ce maillon. Le limiteur **glisse** (à friction) ou **se déclenche** au-delà d'un
couple réglé. Le limiteur à billes fonctionne comme une clé dynamométrique à déclenchement : des billes
poussées par des ressorts sont logées dans des creux ; au-delà du couple réglé, elles sortent des creux
(« clac ») et la transmission est coupée net ; on le réarme ensuite. Sa règle de réglage :

> **couple utile maximal < couple de réglage < couple qui casse le maillon faible**

Trop bas, il glisse en service normal ; trop haut, il ne protège rien. La goupille de cisaillement est
un limiteur « fusible » : elle casse à la place de la mécanique, et on la remplace.

**Le frein : ralentir, arrêter, maintenir.** Il transforme l'énergie cinétique (½ m v², ½ I ω², fiche
8.1 ; I : moment d'inertie, la « masse » d'un objet qui tourne) en chaleur, ou il **maintient** une charge immobile. Le **frein à manque de courant** (frein à
ressort, desserré par un électroaimant) **serre quand l'alimentation est coupée** : coupure, arrêt
d'urgence, panne, la charge est tenue. C'est la **sécurité positive** : l'état sans énergie est l'état
sûr. C'est le frein des axes verticaux et des levages.

*Même physique, trois intentions : l'embrayage veut transmettre (et glisser seulement au démarrage),
le limiteur veut glisser au bon moment, le frein veut dissiper ou tenir.*

### 4. Adapter la vitesse : courroies et chaînes

[[FIG:courroies_chaines]]

Le **rapport de transmission** r = N2 / N1 (sortie sur entrée), comme en fiche 6.11. Un maillon de la
chaîne passe à la même vitesse sur les deux pignons, sinon la chaîne casserait ou ferait du mou : π d1 N1
= π d2 N2, d'où **r = N2 / N1 = d1 / d2 = Z1 / Z2**. Les indices s'inversent : le petit tourne vite, le
grand lentement (la poulie de 24 dents fait 2 tours pendant que celle de 48 en fait 1).

**Le couple, par la puissance** : P = C × ω passe d'un bout à l'autre, moins les pertes : C2 × ω2 = η × C1 ×
ω1, d'où **C2 = C1 × η / r**. Image : le vélo — sur le grand pignon arrière, on monte la côte lentement
mais facilement. Ce qu'on perd en vitesse, on le gagne en couple.

| Lien | Principe | Rapport | Ce que ça change pour la conception |
|---|---|---|---|
| **courroie plate, trapézoïdale, poly-V** (plate à petites nervures en V, celle de l'alternateur d'une voiture) | **adhérence** (flancs coincés dans la gorge) | approché (léger glissement) | **patine si blocage** : protection non réglée, qui use et échauffe la courroie |
| **courroie crantée** | **obstacle** (dents) | **exact** | synchronisme ; tension de pose plus faible qu'une trapézoïdale ; un blocage la fait sauter ou casser |
| **chaîne à rouleaux** | **obstacle** (rouleaux sur pignon) | **exact** en moyenne | gros couples ; sur un petit pignon, la chaîne s'enroule « par facettes » et la vitesse de sortie fluctue un peu à chaque dent |

Rendements, encombrement, tension sur les paliers : **fiche 6.11**.

*Exemple : moteur à 960 tr/min, pignon de 17 dents, couronne de 34 dents : N2 = 960 × 17 / 34 =
**480 tr/min**.*

**Le choix, par la fonction** : faut-il un **synchronisme** exact (axe de positionnement) → crantée ou
chaîne. Faut-il **amortir** et accepter de patiner en cas de blocage → trapézoïdale. Les engrenages, eux,
sont traités en fiches 6.11, 6.13 et 12.5.

### 5. Transformer le mouvement : vis-écrou, cames, systèmes articulés

**La vis-écrou : rotation → translation.** Un tour de vis fait avancer l'écrou du **pas de l'hélice** :

> **v = ph × N**, avec **ph = P × n** (pas apparent P × nombre de filets n)

[[FIG:vis_un_deux_filets]]

- **P, le pas apparent** : la distance entre deux filets voisins, celle qu'on mesure au réglet ;
- **n, le nombre de filets** : une vis peut avoir plusieurs hélices intercalées. Regardez le goulot d'un pot
  de confiture : plusieurs débuts de filet tout autour, et un quart de tour suffit pour fermer. Plusieurs
  filets, c'est beaucoup d'avance par tour sans filet grossier ;
- **ph = P × n** : l'avance réelle pour un tour. C'est lui qui compte dans v = ph × N.

**Lire une désignation : Tr 20 × 8 (P4)** — **Tr** : filet trapézoïdal (flancs en trapèze, pour transmettre
des efforts) ; **20** : diamètre nominal, en mm ; **8** : pas de l'hélice ph ; **(P4)** : pas apparent,
4 mm. Donc **2 filets**. Sans parenthèse (« Tr 20 × 4 »), la vis n'a qu'un filet et les deux pas sont égaux.

*Exemple : Tr 20 × 8 (P4) à N = 300 tr/min. v = 8 × 300 = 2 400 mm/min = **40 mm/s**. Avec P à la place
de ph, on trouverait 20 mm/s : moitié trop lent.*

**La réversibilité : la charge peut-elle faire tourner la vis ?** Deux étapes.

*L'angle de frottement, par l'expérience.* Posez une caisse sur une planche et soulevez lentement un bout.
Tant que la pente est faible, la caisse reste en place ; à un angle précis, elle se met à glisser. Cet angle
limite est **l'angle de frottement φ** ; il ne dépend que des deux matériaux, et **tan φ = f** (fiche
12.1). Pour f = 0,15, φ = arctan 0,15 ≈ 8,5°.

*Le filet est une rampe.* Enroulez un triangle de papier autour d'un crayon : son grand côté dessine une
hélice. Une vis, c'est cela à l'envers : « déroulé » à plat, un tour de filet devient une **rampe** de
longueur **π × d2** (d2 : diamètre moyen du filet, **d2 = d − 0,5 P** pour un filet trapézoïdal ; Tr 20 au
pas de 4 : d2 = 18 mm) et de hauteur **ph**. Sa pente : **tan α = ph / (π d2)**. L'écrou chargé est posé sur
cette rampe comme la caisse sur la planche : si la rampe est plus raide que l'angle de frottement, la
charge « glisse » le long du filet, et pour glisser elle doit faire tourner la vis.

> **irréversible si α ≤ φ**, avec tan φ = f

*(Modèle simplifié, comme si le filet était carré. Sur un filet trapézoïdal, l'inclinaison des flancs
augmente un peu le frottement apparent : la conclusion est la même, avec une marge légèrement plus grande.)*

[[DYN:vis_ecrou_curseurs]]

| Vis | Rendement | Réversibilité | Conséquence |
|---|---|---|---|
| **trapézoïdale à 1 filet** (à glissement) | faible | en général **irréversible** | tient la charge seule ; chauffe ; usure |
| **trapézoïdale à plusieurs filets** | plus élevé | **réversible dès que α > φ** | à vérifier au cas par cas |
| **à billes** (à roulement) | élevé (de l'ordre de 0,9, valeur de catalogue constructeur) | **réversible** | rapide, précise ; **un axe vertical exige un frein** |

*Avec f = 0,15, une Tr 20 au pas de 4 est irréversible à un filet (α = 4,0°, φ = 8,5°) et encore à deux
filets (α = 8,05°), mais de justesse ; à trois filets (α = 12°), elle devient réversible. Le frottement
réel varie (graissage, usure) : on ne compte pas sur une irréversibilité « de justesse » pour tenir une
charge.*

**Irréversible, donc peu efficace.** C'est le même frottement qui tient la charge et qui consomme
l'énergie : avec f = 0,15, cette Tr 20 a un rendement d'environ 0,32 à un filet et 0,47 à deux filets. Une
vis irréversible a toujours un rendement inférieur à 50 % (approfondissement : η = tan α / tan(α + φ)).

**La came : un mouvement imposé.** Une came est un disque profilé qui tourne ; un **poussoir** (souvent à
galet) suit son contour. La forme de la came impose, angle par angle, la position du poussoir : montées,
arrêts, descentes — la **loi de levée**. Le cas le plus simple est la **came excentrique** : un disque
circulaire monté décalé de **e** sur son axe ; le poussoir fait une **course de 2e** et monte et descend
sans à-coup, comme un piston. Pourquoi 2e ? Quand le décalage pointe vers le poussoir, le bord du disque est
à r0 + e de l'axe (poussoir au plus haut) ; un demi-tour plus tard, à r0 − e (au plus bas). La différence
vaut 2e : le rayon r0 du disque s'élimine.

[[FIG:came_excentrique]]

- le contact doit être **maintenu** : ressort de rappel, poids, ou came à rainure ;
- le **galet** roule au lieu de frotter : moins d'usure ;
- usage : machines à cadence fixe (emballage, assemblage), où une seule rotation commande plusieurs
  mouvements synchronisés, sans électronique.

**Les systèmes articulés : bielle-manivelle, quadrilatère, genouillère.**

- **Bielle-manivelle** : rotation de la manivelle ↔ translation alternative du piston, **course = 2r**.
  Deux points morts par tour, où bielle et manivelle sont alignées : pousser sur le piston ne fait plus
  tourner la manivelle (d'où le volant d'inertie des moteurs, qui passe les points morts sur son élan).
  Sa cinématique (vitesses, CIR, loi entrée-sortie non linéaire) est traitée en fiche **6.15** : on ne la
  refait pas ici. Un **excentrique à collier** (différent de la came excentrique : ici une bielle entoure
  le disque, au lieu d'un poussoir qui le touche) remplace la manivelle par un disque décalé de e
  (course 2e) : plus compact, plus robuste, pour les petites courses (pompes, presses).
- **Quadrilatère articulé** : quatre barres reliées par quatre articulations, dont une fixe. Le moteur
  d'essuie-glace tourne toujours dans le même sens ; une petite manivelle fait le tour complet et pousse
  une biellette qui fait aller et venir le bras du balai : une rotation continue devient une
  **oscillation**, sans inverser le moteur.
- **Genouillère** : vous l'avez en main avec la **pince-étau** — en fin de fermeture, les biellettes
  s'alignent presque, et la main suffit à serrer un écrou grippé. Pourquoi ? Près de l'alignement, un
  grand mouvement de la poignée ne fait plus avancer les mors que de quelques centièmes ; or le travail se
  conserve (aux pertes près) : effort × déplacement en entrée = effort × déplacement en sortie. Si la
  sortie bouge 50 fois moins, elle pousse environ 50 fois plus fort. Usages : bridage rapide, presse,
  sertisseuse.

### 6. Choisir par la fonction

| Fonction demandée | Composant |
|---|---|
| relier deux arbres, avec de petits défauts d'alignement | accouplement élastique |
| relier ou séparer la machine sans arrêter le moteur | embrayage |
| protéger la transmission en cas de blocage | limiteur de couple (une courroie lisse qui patine protège aussi, sans réglage) |
| tenir une charge à l'arrêt, même en cas de coupure | frein à manque de courant |
| ralentir une grosse inertie | frein (vérifier l'énergie à dissiper, fiche 8.1) |
| réduire la vitesse avec un rapport exact | courroie crantée, chaîne, engrenages |
| transformer rotation en translation précise | vis à billes (+ frein si vertical) |
| transformer et tenir seule la charge | vis trapézoïdale irréversible |
| répéter un mouvement imposé, synchronisé | came |
| très grand effort sur une petite course | genouillère |

### 7. Les erreurs classiques

1. **Oublier le nombre de filets** : v = ph × N, avec ph = P × n. Une Tr 20 × 8 (P4) avance de 8 mm par
   tour, pas de 4.
2. **Croire qu'une vis à billes tient la charge** : elle est réversible ; un axe vertical sans frein
   descend dès la coupure du moteur.
3. **Confondre embrayage et limiteur** : l'embrayage est commandé (on choisit quand il relie) ; le
   limiteur est automatique (il glisse au-delà d'un couple réglé).
4. **Régler un limiteur au hasard** : il doit être au-dessus du couple utile maximal **et** en dessous
   du couple qui casse le maillon faible.
5. **Accoupler rigidement deux arbres montés séparément** : montage hyperstatique, roulements chargés
   par les défauts d'alignement.
6. **Choisir une courroie lisse pour un axe de positionnement** : elle glisse, le rapport n'est
   qu'approché.
7. **Refaire la cinématique de la bielle-manivelle** : elle est en fiche 6.15 ; ici, on choisit le
   mécanisme pour sa fonction.

### 8. À retenir

- Partir de la **fonction** : accoupler, débrayer, protéger, immobiliser, adapter, transformer.
- **Accouplement élastique** : tolère les défauts d'alignement, évite l'hyperstatisme (6.17).
- **Embrayage à friction** : C = n f F rmoy, rmoy = (R + r) / 2. **Limiteur** : couple utile maxi < réglage <
  couple de rupture. **Frein à manque de courant** : serré sans énergie (sécurité positive).
- **Courroie, chaîne** : r = N2 / N1 = d1 / d2 = Z1 / Z2 ; trapézoïdale = adhérence (glisse), crantée et
  chaîne = obstacle (rapport exact).
- **Vis-écrou** : v = ph × N, **ph = P × nombre de filets** ; irréversible si α ≤ φ (tan α = ph / π d2,
  d2 = d − 0,5 P) ;
  vis à billes réversible → **frein** sur un axe vertical.
- **Came excentrique** : course 2e. **Bielle-manivelle** : course 2r, cinématique en 6.15.
  **Genouillère** : grand effort près du point mort.
""",
    "formules": """
**Puissance** — P sortie = η × P entrée · rendement global = produit des rendements (fiche 8.5)

**Embrayage, limiteur à friction** — C = n × f × F × rmoy · rmoy = (R + r) / 2 · n : nombre de surfaces
frottantes

**Réglage d'un limiteur** — couple utile maxi < couple de réglage < couple de rupture du maillon faible

**Courroie, chaîne** — r = N2 / N1 = d1 / d2 = Z1 / Z2 · C2 = C1 × η / r

**Vis-écrou** — v = ph × N · ph = P × n (pas apparent × nombre de filets) · tan α = ph / (π d2),
d2 = d − 0,5 P · irréversible si α ≤ φ, tan φ = f

**Came excentrique, bielle-manivelle** — course = 2e · course = 2r (cinématique : fiche 6.15)
""",
    "exemple": """
### Cas industriel — L'axe qui descendait tout seul

**Le symptôme.** Un poste de dépose a un axe vertical : un chariot de 40 kg monté sur une **vis
trapézoïdale** à un filet. Pour gagner en vitesse et en précision, on la remplace par une **vis à billes**
de même pas. Les cadences doublent. Mais au premier arrêt d'urgence, l'axe **descend** et vient taper la
butée basse ; à la coupure du soir, on le retrouve en bas.

**L'analyse.** La vis trapézoïdale était **irréversible** : son angle d'hélice était sous l'angle de
frottement, la charge ne pouvait pas la faire tourner. La vis à billes **roule** au lieu de frotter : son
rendement est élevé, et elle est **réversible**. Le poids du chariot (40 × 9,81 ≈ 392 N) fait tourner la
vis dès que le moteur ne la retient plus. Personne n'avait perdu de pièce : on avait perdu une
**fonction**, « tenir la charge sans énergie », que l'ancienne vis remplissait sans qu'on le sache.

**Les corrections :**

| Action | Effet |
|---|---|
| **frein à manque de courant** sur le moteur (ou intégré au moteur) | serre à la coupure, à l'arrêt d'urgence et en panne : la charge est tenue |
| contrepoids ou vérin d'équilibrage | réduit l'effort à tenir, mais ne remplace pas le frein |
| revenir à la vis trapézoïdale | on retrouve l'irréversibilité, mais on perd vitesse et précision |

**Ce que le cas apprend.** Changer un composant, c'est vérifier **toutes** ses fonctions, y compris
celles qu'il remplissait sans qu'on les ait écrites. La réversibilité fait partie du cahier des charges
d'un axe vertical.
""",
    "exercice": """
### Exercice — L'axe vertical d'un poste de dépose

Un moteur tourne à **1 500 tr/min**. Il entraîne, par une **courroie crantée** (poulie moteur 24 dents,
poulie de vis 48 dents), une **vis à billes** de pas 5 mm à un filet. L'écrou porte un chariot vertical ;
l'effort à vaincre en montée est de **400 N**. Rendements : courroie 0,95 ; vis 0,9.

**1.** Décrivez la chaîne de transmission composant par composant, avec la fonction de chacun.

**2.** Calculez la vitesse de rotation de la vis.

**3.** Calculez la vitesse de montée du chariot, en mm/s. Combien de temps pour une course de 250 mm ?

**4.** Pourquoi une courroie **crantée** plutôt qu'une courroie trapézoïdale ?

**5.** La vis à billes est-elle réversible ? Quel composant faut-il ajouter, et pourquoi ce type-là ?

**6.** Quelle puissance le moteur doit-il fournir en montée ?
""",
    "corrige": """
### Corrigé, en six temps

#### 1. Ce que dit l'énoncé

Une chaîne moteur → courroie crantée → vis à billes → chariot vertical. On cherche les vitesses, la
puissance, et ce qui manque pour la sécurité.

#### 2. Quelle règle, et pourquoi

> **r = Z1 / Z2** (courroie crantée). **v = ph × N**, ph = P × n. **P sortie = η × P entrée**,
> η global = produit des rendements. Vis à billes : **réversible**.

#### 3. Les conversions

v en mm/min → mm/s : diviser par 60. Puissance : P = F × v avec F en N et v en m/s, pour des watts.

#### 4. Le remplacement

N vis = 1 500 × 24 / 48. v = 5 × 1 × N vis. P utile = 400 × v. η global = 0,95 × 0,9.

#### 5. Le calcul

**1.** Moteur (**convertir** l'énergie électrique en rotation) → courroie crantée (**adapter** la vitesse,
rapport exact) → vis à billes (**transformer** la rotation en translation) → chariot. Il manque un
composant pour **immobiliser** la charge (question 5).

**2.** N vis = 1 500 × 24 / 48 = **750 tr/min**.

**3.** v = 5 × 750 = 3 750 mm/min = **62,5 mm/s**. Course de 250 mm : 250 / 62,5 = **4 s**.

**4.** Un axe de positionnement demande un **rapport exact** : la position du chariot se déduit des tours
du moteur. Une courroie trapézoïdale glisse légèrement : la position dériverait.

**5.** Oui : une vis à billes **roule**, son rendement est élevé, elle est **réversible**. Le chariot
descendrait seul dès que le moteur ne le retient plus. Il faut un **frein à manque de courant** : il
serre quand l'alimentation est coupée (arrêt d'urgence, panne, coupure du soir) — c'est la sécurité
positive. On le place souvent sur le moteur : avant la courroie 24/48, le couple à tenir est deux fois
plus faible que sur la vis, et un frein plus petit coûte moins cher (d'où les moteurs à frein intégré).
Mais la courroie devient alors un maillon dont dépend la sécurité : si elle casse, la charge tombe. Sur un
axe vertical, on préfère un frein côté vis, ou bien une surveillance de rupture de courroie.

**6.** P utile = 400 × 0,0625 = **25 W**. η global = 0,95 × 0,9 = **0,855**. P moteur = 25 / 0,855 ≈
**29 W**.

#### 6. La vérification

**Ordres de grandeur** : 62,5 mm/s, une course en 4 s, cohérent pour un axe de dépose. **Puissance** :
29 W pour lever 400 N (environ 40 kg) à 6 cm/s, c'est peu — les axes réels sont dimensionnés surtout pour
**l'accélération** (fiche 13.3), pas pour la vitesse constante. **Sécurité** : sans le frein, la question
5 serait le défaut grave de cette conception, quel que soit le calcul de puissance.
""",
}

# ===========================================================================
# 3. MÉTHODE
# ===========================================================================
MTH_6_18 = ("6.18", "Choisir un composant de transmission par sa fonction", [
    "**Écrire la fonction avec un verbe** : accoupler, débrayer, protéger, immobiliser, adapter la "
    "vitesse, transformer le mouvement.",
    "**Tracer la chaîne de transmission** du moteur à l'effecteur, et placer chaque composant avec sa "
    "fonction ; repérer ce qui manque.",
    "**Calculer les vitesses étage par étage** : r = Z1 / Z2 (courroie, chaîne), v = ph × N avec "
    "ph = P × nombre de filets (vis).",
    "**Vérifier la réversibilité** de chaque étage (tan α = ph / π d2 comparé à tan φ = f) : un axe "
    "vertical réversible exige un frein à manque de courant.",
    "**Vérifier puissance et couples** : P sortie = η × P entrée ; régler un limiteur entre le couple "
    "utile maximal et le couple de rupture du maillon faible.",
], "Axe vertical : moteur 1 500 tr/min, courroie crantée 24/48 → vis à 750 tr/min ; vis à billes de "
   "pas 5 → 62,5 mm/s. Vis à billes réversible → frein à manque de courant. P = 25 W utiles, "
   "29 W au moteur (η = 0,855).")

# ===========================================================================
# 4. ATELIERS (fin de liste ATELIERS, après at161)
# ===========================================================================
ATELIERS_NOUVEAUX = [
    {
        "id": "at162",
        "chapitre": "Bloc 6",
        "titre": "Table de machine sur vis Tr 20 × 8 (P4) : vitesse et réversibilité",
        "theme": "Transmission",
        "fiche": "6.18",
        "figure": "vis_un_deux_filets",
        "vocabulaire": [
            ("Pas apparent P",
             "la distance entre deux filets voisins, celle qu'on mesure sur la vis."),
            ("Pas de l'hélice ph",
             "l'avance de l'écrou pour un tour de vis : ph = P × nombre de filets."),
            ("Réversible",
             "se dit d'une transmission où la sortie peut entraîner l'entrée : ici, la charge qui fait "
             "tourner la vis."),
        ],
        "enonce": "Le chariot d'un axe vertical est déplacé par une vis trapézoïdale Tr 20 × 8 (P4) qui "
                  "tourne à N = 300 tr/min. Le diamètre moyen du filet vaut d2 = 18 mm ; le coefficient "
                  "de frottement vis-écrou est donné : f = 0,15.",
        "etapes": [
            {"type": "numerique", "label": "Nombre de filets",
             "unite": "sans unité", "attendu": 2, "tol": 0.1,
             "consigne": "Dans la désignation Tr 20 × 8 (P4), 8 est le pas de l'hélice et 4 le pas "
                         "apparent. Combien la vis a-t-elle de filets ?",
             "indice": "ph = P × n.",
             "pieges": [(4, "4, c'est le pas apparent en mm, pas le nombre de filets. n = ph / P = 8 / 4.")],
             "aide": "n = 8 / 4 = 2 filets."},
            {"type": "numerique", "label": "Vitesse du chariot",
             "unite": "mm/s", "attendu": 40, "tol": 0.5,
             "consigne": "Calcule la vitesse du chariot, en mm/s.",
             "indice": "v = ph × N, puis diviser par 60 pour passer de mm/min à mm/s.",
             "pieges": [(20, "20 mm/s : tu as pris le pas apparent (4 mm). Avec 2 filets, l'écrou avance "
                             "de 8 mm par tour."),
                        (2400, "2 400, c'est en mm/min. Divise par 60 pour des mm/s.")],
             "aide": "v = 8 × 300 = 2 400 mm/min = 40 mm/s."},
            {"type": "numerique", "label": "Angle d'hélice",
             "unite": "°", "attendu": 8.05, "tol": 0.1,
             "consigne": "Calcule l'angle d'hélice α : tan α = ph / (π × d2).",
             "indice": "tan α = 8 / (π × 18) = 0,1415.",
             "pieges": [(4.05, "4,05° : tu as pris le pas apparent (4 mm) au lieu du pas de l'hélice "
                               "(8 mm)."),
                        (7.26, "7,26° : tu as pris le diamètre nominal (20 mm). L'hélice se déroule sur le "
                               "diamètre moyen d2 = 18 mm."),
                        (0.1405, "0,1405 : ta calculatrice est en radians. Passe-la en degrés.")],
             "aide": "α = arctan 0,1415 = 8,05°."},
            {"type": "numerique", "label": "Angle de frottement",
             "unite": "°", "attendu": 8.53, "tol": 0.1,
             "consigne": "Calcule l'angle de frottement φ : tan φ = f.",
             "indice": "φ = arctan 0,15.",
             "pieges": [(0.15, "0,15, c'est f lui-même. L'angle de frottement est arctan f, en degrés."),
                        (0.1489, "0,1489 : ta calculatrice est en radians. Passe-la en degrés.")],
             "aide": "φ = arctan 0,15 = 8,53°."},
            {"type": "qcm", "label": "Réversibilité",
             "question": "α = 8,05° et φ = 8,53°. Que conclure pour ce chariot vertical ?",
             "options": ["La vis est réversible : la table descend seule",
                         "La vis est irréversible, mais de justesse : avec un frottement plus faible "
                         "(graissage), elle pourrait devenir réversible — on prévoit un frein",
                         "La vis est irréversible avec une large marge : aucun frein n'est utile"],
             "bonne": 1,
             "indice": "Irréversible si α ≤ φ. Regarder aussi l'écart entre les deux.",
             "diagnostics": {0: "α (8,05°) est sous φ (8,53°) : la vis est irréversible. Mais l'écart "
                                 "est faible.",
                             2: "L'écart n'est que de 0,5° : le frottement réel varie (graissage, "
                                "usure). On ne compte pas sur une irréversibilité de justesse pour "
                                "tenir une charge."}},
        ],
        "corrige": {
            "enonce": "Vis Tr 20 × 8 (P4), N = 300 tr/min, d2 = 18 mm, f = 0,15.",
            "regle": "**v = ph × N**, **ph = P × n**. **Irréversible si α ≤ φ**, tan α = ph / (π d2), "
                    "tan φ = f.",
            "conversions": "v en mm/min → mm/s : ÷ 60. Angles en degrés.",
            "remplacement": "n = 8 / 4. v = 8 × 300 / 60. tan α = 8 / (π × 18). tan φ = 0,15.",
            "calcul": "**n = 2** ; **v = 40 mm/s** ; **α = 8,05°** ; **φ = 8,53°** : irréversible, de "
                     "justesse.",
            "verification": "Avec un seul filet (Tr 20 × 4), on aurait α = 4,05° : irréversible avec une "
                            "vraie marge, mais deux fois plus lent (20 mm/s). Ajouter un filet double la "
                            "vitesse et redresse l'hélice : c'est le prix de la vitesse.",
        },
        "a_retenir": "À retenir : v = ph × N, avec ph = P × nombre de filets ; plus de filets = plus "
                     "rapide, mais plus près de la réversibilité.",
    },
    {
        "id": "at163",
        "chapitre": "Bloc 6",
        "titre": "Convoyeur : régler un limiteur de couple à friction",
        "theme": "Transmission",
        "fiche": "6.18",
        "figure": "embrayage_limiteur_frein",
        "vocabulaire": [
            ("Limiteur de couple",
             "un composant qui glisse ou se déclenche au-delà d'un couple réglé, pour protéger la "
             "transmission d'un blocage."),
            ("Rayon moyen rmoy",
             "la distance moyenne des garnitures à l'axe : (R + r) / 2."),
            ("Maillon faible",
             "la pièce de la transmission qui casserait la première en cas de surcharge (clavette, "
             "dent, chaîne)."),
        ],
        "enonce": "Sur l'arbre d'un convoyeur, un limiteur de couple à friction a un disque pris entre "
                  "deux plateaux (2 surfaces frottantes). Garnitures : rayon extérieur R = 60 mm, "
                  "intérieur r = 40 mm, f = 0,3 (donné par le fabricant). En service, le couple maximal "
                  "est de 30 N·m ; la clavette de l'arbre cède à 70 N·m.",
        "etapes": [
            {"type": "numerique", "label": "Rayon moyen",
             "unite": "mm", "attendu": 50, "tol": 0.5,
             "consigne": "Calcule le rayon moyen des garnitures rmoy.",
             "indice": "rmoy = (R + r) / 2.",
             "pieges": [(100, "100 mm, c'est R + r. Le rayon moyen est leur moyenne : (R + r) / 2.")],
             "aide": "rmoy = (60 + 40) / 2 = 50 mm."},
            {"type": "numerique", "label": "Couple pour F = 1 500 N",
             "unite": "N·m", "attendu": 45, "tol": 0.5,
             "consigne": "Le ressort presse avec F = 1 500 N. Quel couple le limiteur transmet-il avant "
                         "de glisser ?",
             "indice": "C = n × f × F × rmoy, avec rmoy en mètres.",
             "pieges": [(22.5, "22,5 N·m : tu as compté une seule surface frottante. Le disque frotte "
                               "sur ses deux faces : n = 2."),
                        (45000, "45 000, c'est en N·mm : rmoy doit être en mètres (0,05 m).")],
             "aide": "C = 2 × 0,3 × 1 500 × 0,05 = 45 N·m."},
            {"type": "qcm", "label": "Le réglage est-il bon ?",
             "question": "Couple de service maxi 30 N·m, clavette à 70 N·m, limiteur à 45 N·m. Ce "
                         "réglage convient-il ?",
             "options": ["Non : il faut le régler à 30 N·m pile, le couple de service",
                         "Oui : 30 < 45 < 70, il ne glisse pas en service et protège la clavette",
                         "Non : il faut le régler au-dessus de 70 N·m pour ne jamais glisser"], "bonne": 1,
             "indice": "couple utile maxi < réglage < couple de rupture du maillon faible.",
             "diagnostics": {0: "Réglé pile au couple de service, il glisserait au moindre pic "
                                 "normal (démarrage, à-coup) : il faut une marge au-dessus.",
                             2: "Au-dessus de 70 N·m, la clavette casse avant que le limiteur glisse : "
                                "il ne protège plus rien."}},
            {"type": "numerique", "label": "Effort presseur pour 55 N·m",
             "unite": "N", "attendu": 1833, "tol": 10,
             "consigne": "On veut régler le limiteur à 55 N·m. Quel effort presseur F faut-il ?",
             "indice": "F = C / (n × f × rmoy).",
             "pieges": [(3667, "3 667 N : tu as compté une seule surface frottante (n = 1)."),
                        (1.833, "1,833 : rmoy est en mm dans ton calcul ; il doit être en mètres.")],
             "aide": "F = 55 / (2 × 0,3 × 0,05) = 1 833 N."},
            {"type": "qcm", "label": "Après un blocage",
             "question": "Une pièce se coince dans le convoyeur. Le limiteur glisse. Que doit faire "
                         "l'opérateur ?",
             "options": ["Arrêter le convoyeur, dégager la pièce : le limiteur à friction se remet à "
                         "transmettre de lui-même", "Remplacer le limiteur, qui est détruit",
                         "Augmenter l'effort presseur pour que le convoyeur force le passage"], "bonne": 0,
             "indice": "Un limiteur à friction glisse sans casser ; c'est la goupille de cisaillement "
                       "qui se remplace.",
             "diagnostics": {1: "C'est la goupille de cisaillement (limiteur « fusible ») qui se remplace. "
                                 "Le limiteur à friction glisse, chauffe un peu, et retransmet une fois le "
                                 "blocage dégagé.",
                             2: "Serrer davantage, c'est remonter le couple de réglage vers celui qui casse "
                                "la clavette : on supprime la protection au lieu de traiter la cause."}},
        ],
        "corrige": {
            "enonce": "Limiteur à friction, n = 2, R = 60 mm, r = 40 mm, f = 0,3 ; service 30 N·m, "
                      "clavette 70 N·m.",
            "regle": "**C = n × f × F × rmoy**, rmoy = (R + r) / 2. Réglage : **couple utile maxi < "
                    "réglage < couple de rupture du maillon faible**.",
            "conversions": "rmoy = 50 mm = 0,05 m.",
            "remplacement": "C = 2 × 0,3 × 1 500 × 0,05. F = 55 / (2 × 0,3 × 0,05).",
            "calcul": "**rmoy = 50 mm** ; **C = 45 N·m** ; réglage correct (30 < 45 < 70) ; pour 55 N·m, "
                     "**F = 1 833 N**.",
            "verification": "Doubler l'effort presseur double le couple : la relation est linéaire, d'où "
                            "un réglage simple par écrou et ressort. f dépend des garnitures et de leur "
                            "état : on vérifie le couple de glissement réel au banc après réglage.",
        },
        "a_retenir": "À retenir : un limiteur se règle entre le couple de service et le couple qui "
                     "casse le maillon faible ; à friction, il glisse sans casser et retransmet une fois "
                     "le blocage dégagé.",
    },
]

# ===========================================================================
# 5. GÉNÉRATEUR (famille « Transmission de puissance », déjà au menu)
# ===========================================================================
GENERATEUR = '''
def gen_vis_ecrou():
    """Vitesse d'avance d'un écrou : v = ph × N, ph = pas apparent × nombre de filets."""
    P = random.choice([2, 3, 4, 4, 5, 6])
    nf = random.choice([1, 2, 2, 3])
    N = random.choice([150, 200, 300, 400, 600, 750, 900, 1200])
    ph = P * nf
    v = ph * N / 60
    diag = []
    for val, msg in (
            (P * N / 60, "Tu as pris le pas apparent P. Avec plusieurs filets, l'écrou avance du pas de "
                         "l'hélice : ph = P × nombre de filets."),
            (ph * N, "Ton résultat est en mm/min. La question demande des mm/s : divise par 60."),
            (ph * N / 60 / (2 * math.pi), "Tu as divisé par 2π : ce n'est pas utile ici. N est déjà en "
                                          "tours par minute, et un tour fait avancer de ph."),
            (P * N, "Tu as pris le pas apparent et gardé des mm/min."),
    ):
        if abs(val - v) > max(0.05, v * 0.01) and all(abs(val - d["v"]) > 0.05 for d in diag):
            diag.append(_diag(round(val, 2), msg))
    # la désignation n'est écrite que pour la vis du cours (Tr 20 au pas de 4) ; sinon, pas de diamètre
    if P == 4:
        desig = f"**Tr 20 × {ph} (P4)**" if nf > 1 else "**Tr 20 × 4**"
    else:
        desig = (f"trapézoïdale à **{nf} filets**, de pas apparent **{P} mm**," if nf > 1
                 else f"trapézoïdale à **un filet**, de pas **{P} mm**,")
    return {
        "titre": "Transmission — vitesse d'avance d'une vis-écrou",
        "enonce": (f"Une vis {desig} tourne à **{N} tr/min**. À quelle vitesse l'écrou avance-t-il, "
                   "en mm/s ?"),
        "rep": round(v, 2), "tol": max(0.05, v * 0.01), "unite": "mm/s",
        "diag": diag,
        "corr": [
            f"**Ce que dit l'énoncé.** Une vis à {nf} filet{'s' if nf > 1 else ''}, de pas apparent {P} mm, "
            f"à {N} tr/min. On cherche la vitesse de l'écrou.",
            "**Le pas de l'hélice.** " + (f"Avec {nf} filets, l'écrou avance de {nf} pas apparents par tour."
                                          + (f" (Tr 20 × {ph} (P4) : {ph} = pas de l'hélice, P4 = pas apparent.)"
                                             if P == 4 else "") if nf > 1 else
                                          "Un seul filet : le pas de l'hélice égale le pas apparent."),
            f"**La règle.** v = ph × N, avec ph = P × nombre de filets = {P} × {nf} = {ph} mm.",
            f"**Le calcul.** v = {ph} × {N} = {fr(ph * N, 0)} mm/min, soit {fr(v, 2)} mm/s.",
            "**Je vérifie.** " + (f"Avec le pas apparent seul, on trouverait {fr(P * N / 60, 2)} mm/s : "
                                  f"{nf} fois trop lent." if nf > 1 else
                                  "Un seul filet : pas apparent et pas de l'hélice se confondent."),
        ],
        "indice": "v = ph × N, avec ph = P × nombre de filets ; diviser par 60 pour des mm/s.",
    }
'''

# ===========================================================================
# 6. QUIZ — nouvelle catégorie « Mécanismes de transmission »
#    positions de la bonne réponse : 1, 3, 0, 2, 0, 2, 3, 1
# ===========================================================================
QUIZ_TRANSMISSION = [
    ("Une vis Tr 20 × 8 (P4) tourne à 300 tr/min. À quelle vitesse avance l'écrou ?",
     ["20 mm/s", "40 mm/s", "2 400 mm/s", "160 mm/s"], 1,
     "Tr 20 × 8 (P4) : pas apparent 4 mm, pas de l'hélice 8 mm, donc 2 filets. v = ph × N = 8 × 300 = "
     "2 400 mm/min = 40 mm/s. Avec le pas apparent, on trouverait 20 mm/s.", "Calcul"),
    ("Un axe vertical est entraîné par une vis à billes. Que faut-il prévoir ?",
     ["Rien : la vis à billes tient la charge", "Une courroie lisse qui patine",
      "Un limiteur de couple", "Un frein à manque de courant"], 3,
     "La vis à billes roule, son rendement est élevé : elle est réversible. Sans frein, la charge "
     "descend dès que le moteur ne la retient plus. Le frein à manque de courant serre quand "
     "l'alimentation est coupée : sécurité positive.", "Intermédiaire"),
    ("Quelle est la différence entre un embrayage et un limiteur de couple ?",
     ["L'embrayage est commandé (on choisit quand il relie) ; le limiteur glisse seul au-delà d'un "
      "couple réglé", "Aucune, ce sont deux noms du même composant",
      "L'embrayage protège d'un blocage, le limiteur relie deux arbres",
      "Le limiteur fonctionne seulement à l'arrêt"], 0,
     "Même physique (des surfaces qui frottent), deux fonctions : l'embrayage relie ou sépare à la "
     "demande ; le limiteur protège automatiquement la transmission d'une surcharge.", "Base"),
    ("Un limiteur de couple protège une transmission dont la clavette cède à 80 N·m ; le couple de "
     "service maximal est de 40 N·m. Où le régler ?",
     ["À 40 N·m pile", "À 100 N·m", "Entre 40 et 80 N·m, par exemple 55 N·m", "À 0 N·m"], 2,
     "Le réglage doit être au-dessus du couple de service (sinon il glisse en marche normale) et en "
     "dessous du couple qui casse le maillon faible (sinon il ne protège rien).", "Intermédiaire"),
    ("Pourquoi place-t-on souvent un accouplement élastique entre un moteur et un réducteur ?",
     ["Pour tolérer les petits défauts d'alignement et amortir les à-coups",
      "Pour réduire la vitesse", "Pour augmenter le rendement", "Pour rendre la transmission irréversible"], 0,
     "Moteur et réducteur, chacun sur ses paliers, ne sont jamais parfaitement alignés. Un accouplement "
     "rigide transformerait ces défauts en efforts sur les roulements (montage hyperstatique, fiche "
     "6.17).", "Base"),
    ("Pour un axe de positionnement qui doit garder un rapport exact entre moteur et vis, quel lien "
     "choisir ?",
     ["Une courroie trapézoïdale", "Une courroie plate", "Une courroie crantée",
      "Un coupleur hydraulique"], 2,
     "La courroie crantée transmet par obstacle (dents) : le rapport est exact. Une courroie trapézoïdale "
     "ou plate transmet par adhérence et glisse légèrement : la position dériverait.", "Base"),
    ("Une came excentrique est un disque de rayon 40 mm dont l'axe de rotation est décalé de 12 mm "
     "par rapport à son centre. Quelle est la course du poussoir ?",
     ["12 mm", "40 mm", "80 mm", "24 mm"], 3,
     "La course d'une came excentrique vaut 2e : 2 × 12 = 24 mm. Le rayon du disque fixe la position "
     "moyenne du poussoir, pas sa course.", "Calcul"),
    ("Pourquoi une transmission par chaîne a-t-elle souvent besoin d'un limiteur de couple, alors qu'une "
     "courroie trapézoïdale peut s'en passer ?",
     ["Parce que la chaîne est plus lente",
      "Parce que la chaîne transmet par obstacle et ne patine pas : en cas de blocage, une pièce casse",
      "Parce que la chaîne a un rendement plus faible", "Parce que la chaîne est réversible"], 1,
     "Une courroie trapézoïdale patine quand la machine se bloque : c'est une protection naturelle. Une "
     "chaîne ou une courroie crantée ne glisse pas : sans limiteur, le couple monte jusqu'à casser le "
     "maillon faible.", "Intermédiaire"),
]
