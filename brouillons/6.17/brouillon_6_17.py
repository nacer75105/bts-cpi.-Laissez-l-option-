# -*- coding: utf-8 -*-
# BROUILLON — fiche 6.17 « Modéliser les liaisons : torseurs transmissibles, liaisons équivalentes,
# mobilité et hyperstatisme » (référentiel S3.2.1). Rien de ceci n'est encore dans app.py.
# _k_defs, _k_fl (6.15) et _k_apparait (6.16) existent déjà dans app.py.
import math

# ===========================================================================
# 1. FIGURES
# ===========================================================================

def contacts_nature():
    p = [_k_defs(), _txt(40, 24, "La forme du contact décide de la liaison", 13, TRAIT, "start", True)]
    cadres = ((30, "PONCTUEL", "sphère sur plan", "ponctuelle : 5 ddl, 1 inconnue", ALESAGE),
              (275, "LINÉIQUE", "cylindre sur plan", "linéaire rectiligne : 4 ddl, 2 inconnues", ARBRE),
              (520, "SURFACIQUE", "plan sur plan", "appui plan : 3 ddl, 3 inconnues", OK))
    for x0, titre, forme, liaison, c in cadres:
        p.append(f"<rect x='{x0}' y='40' width='225' height='225' rx='8' fill='#ffffff' stroke='{c}' stroke-width='2'/>")
        p.append(_txt(x0 + 112, 62, titre, 12, c, "middle", True))
        p.append(f"<rect x='{x0 + 25}' y='175' width='175' height='16' fill='#cbd5e1' stroke='{TRAIT}' stroke-width='1'/>")
        p.append(_txt(x0 + 112, 212, forme, 11, TRAIT, "middle"))
        p.append(_txt(x0 + 112, 246, liaison, 11, c, "middle", True))
    # sphère : contact en un point, elle peut rouler et pivoter
    p.append(f"<g><circle cx='142' cy='140' r='35' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>"
             f"<line x1='142' y1='140' x2='142' y2='108' stroke='{FIN}' stroke-width='2'>"
             "<animateTransform attributeName='transform' type='rotate' values='0 142 140; 360 142 140' dur='4s' repeatCount='indefinite'/></line></g>")
    p.append(f"<circle cx='142' cy='175' r='5' fill='{ALERTE}'/>")
    # cylindre vu en perspective : contact le long d'une ligne
    p.append(f"<rect x='315' y='130' width='145' height='45' rx='22' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<line x1='325' y1='175' x2='450' y2='175' stroke='{ALERTE}' stroke-width='5'>"
             "<animate attributeName='opacity' values='1;0.3;1' dur='1.6s' repeatCount='indefinite'/></line>")
    # bloc plan sur plan : contact sur toute une face
    p.append(f"<rect x='570' y='125' width='125' height='50' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'>"
             "<animateTransform attributeName='transform' type='translate' values='0,0; 14,0; 0,0' dur='2.4s' repeatCount='indefinite'/></rect>")
    p.append(f"<rect x='570' y='171' width='125' height='6' fill='{ALERTE}' opacity='0.8'/>")
    p.append(f"<rect x='30' y='278' width='715' height='52' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 300, "En rouge, la zone de contact. En général, plus elle est étendue, plus elle bloque de mouvements — et plus elle", 12, TRAIT, "start", True))
    p.append(_txt(46, 320, "transmet d'efforts : ddl + inconnues d'effort = 6, toujours.", 12, FIN))
    return _svg("".join(p), 775, 344)


def torseur_complementaire():
    """Pivot d'axe x : ce qui bouge (une rotation) et ce qui est transmis (tout le reste)."""
    p = [_k_defs(), _txt(40, 24, "Un pivot d'axe x : ce qui est libre n'est pas transmis, ce qui est bloqué l'est", 13, TRAIT, "start", True)]
    ox, oy = 200, 185
    # axes du repère local
    for (dx, dy, n) in ((150, 0, "x"), (0, -120, "z"), (-80, 60, "y")):
        p.append(f"<line x1='{ox}' y1='{oy}' x2='{ox + dx}' y2='{oy + dy}' stroke='{AXE}' stroke-width='1.4' stroke-dasharray='5 4'/>")
        p.append(_txt(ox + dx * 1.08, oy + dy * 1.08 + 4, n, 13, AXE, "middle", True))
    # arbre et alésage stylisés
    p.append(f"<rect x='{ox - 60}' y='{oy - 14}' width='200' height='28' rx='4' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.6'/>")
    p.append(f"<rect x='{ox - 30}' y='{oy - 26}' width='60' height='52' fill='none' stroke='{ALESAGE}' stroke-width='3'/>")
    p.append(_txt(ox, oy + 44, "pivot d'axe x", 11, ALESAGE, "middle", True))
    # rotation libre autour de x (animée)
    p.append(f"<path d='M {ox + 105} {oy - 30} A 22 30 0 1 1 {ox + 105} {oy + 30}' fill='none' stroke='{OK}' stroke-width='2.6' marker-end='url(#kg)'>"
             "<animate attributeName='opacity' values='1;0.3;1' dur='1.6s' repeatCount='indefinite'/></path>")
    p.append(_txt(ox + 132, oy - 34, "Rx libre", 12, OK, "start", True))
    # efforts transmis
    p.append(_k_fl(ox, oy, ox + 60, oy, ARBRE, "ko", 2.6))
    p.append(_txt(ox + 52, oy - 6, "X", 12, ARBRE, "end", True))
    p.append(_k_fl(ox, oy, ox, oy - 70, ARBRE, "ko", 2.6))
    p.append(_txt(ox - 6, oy - 60, "Z", 12, ARBRE, "end", True))
    p.append(_k_fl(ox, oy, ox - 46, oy + 34, ARBRE, "ko", 2.6))
    p.append(_txt(ox - 50, oy + 30, "Y", 12, ARBRE, "end", True))
    # tableau des 6 composantes
    x0 = 420
    p.append(f"<rect x='{x0}' y='44' width='325' height='230' rx='6' fill='#ffffff' stroke='{FIN}'/>")
    p.append(_txt(x0 + 14, 66, "Les 6 mouvements, les 6 actions :", 12, TRAIT, "start", True))
    lignes = (("Tx bloquée", "→ X transmise", ARBRE), ("Ty bloquée", "→ Y transmise", ARBRE), ("Tz bloquée", "→ Z transmise", ARBRE),
              ("Rx LIBRE", "→ L = 0 (aucun moment autour de x)", OK), ("Ry bloquée", "→ M transmis", ARBRE), ("Rz bloquée", "→ N transmis", ARBRE))
    for i, (a, b, c) in enumerate(lignes):
        p.append(_txt(x0 + 20, 92 + 22 * i, a, 12, c, "start", c == OK))
        p.append(_txt(x0 + 130, 92 + 22 * i, b, 12, c, "start", c == OK))
    p.append(_txt(x0 + 14, 236, "Torseur transmissible au centre :", 12, TRAIT, "start", True))
    p.append(_txt(x0 + 14, 258, "résultante (X, Y, Z) ; moment (0, M, N)", 12, ARBRE, "start", True))
    p.append(f"<rect x='40' y='288' width='705' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(56, 310, "Règle (sans frottement) : un mouvement libre ↔ la composante d'action correspondante est nulle.", 12, TRAIT))
    return _svg("".join(p), 775, 336)


def liaisons_serie_parallele():
    p = [_k_defs(), _txt(40, 24, "Liaisons équivalentes : en parallèle les blocages se cumulent, en série on réunit les libertés", 13, TRAIT, "start", True)]
    for x0, titre, c in ((30, "EN PARALLÈLE : un arbre, deux paliers", ALESAGE), (395, "EN SÉRIE : un patin à rotule", ARBRE)):
        p.append(f"<rect x='{x0}' y='40' width='350' height='250' rx='8' fill='#ffffff' stroke='{c}' stroke-width='2'/>")
        p.append(_txt(x0 + 175, 62, titre, 12, c, "middle", True))
    # parallèle : arbre + rotule en A + linéaire annulaire en B
    p.append(f"<rect x='60' y='132' width='290' height='16' rx='3' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.6'>"
             "<animate attributeName='fill' values='#e2e8f0;#dbeafe;#e2e8f0' dur='2s' repeatCount='indefinite'/></rect>")
    for x, nom, sous in ((110, "A : rotule", "roulement arrêté"), (290, "B : linéaire annulaire", "roulement libre")):
        p.append(f"<circle cx='{x}' cy='140' r='20' fill='none' stroke='{ALESAGE}' stroke-width='3'/>")
        p.append(_txt(x, 186, nom, 11, ALESAGE, "middle", True))
        p.append(_txt(x, 202, sous, 10, FIN, "middle"))
    p.append(f"<line x1='86' y1='112' x2='86' y2='168' stroke='{TRAIT}' stroke-width='3'/>")
    p.append(f"<line x1='134' y1='112' x2='134' y2='168' stroke='{TRAIT}' stroke-width='3'/>")
    p.append(_k_fl(300, 104, 330, 104, OK, "kg", 2))
    p.append(_k_fl(280, 104, 250, 104, OK, "kg", 2))
    p.append(_txt(290, 96, "glisse", 10, OK, "middle"))
    p.append(_txt(205, 236, "3 + 2 = 5 inconnues, mobilité 1 (rotation)", 11, TRAIT, "middle"))
    p.append(_txt(205, 256, "→ PIVOT équivalent, sans blocage en double", 12, ALESAGE, "middle", True))
    p.append(_txt(205, 276, "les blocages s'ajoutent, les libertés communes restent", 10, FIN, "middle"))
    # série : vérin → rotule → patin → appui plan → pièce
    p.append(f"<rect x='530' y='70' width='80' height='60' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.6'/>")
    p.append(_txt(570, 104, "vérin", 11, TRAIT, "middle"))
    p.append(f"<line x1='570' y1='130' x2='570' y2='150' stroke='{TRAIT}' stroke-width='5'/>")
    p.append(f"<circle cx='570' cy='160' r='11' fill='#ffffff' stroke='{ARBRE}' stroke-width='3'/>")
    p.append(f"<g><path d='M 540 186 L 600 186 L 590 172 L 550 172 Z' fill='#ffffff' stroke='{ARBRE}' stroke-width='2.4'/>"
             "<animateTransform attributeName='transform' type='rotate' values='0 570 180; -6 570 180; 6 570 180; 0 570 180' dur='3s' repeatCount='indefinite'/></g>")
    p.append(f"<rect x='470' y='186' width='200' height='22' fill='#cbd5e1' stroke='{TRAIT}' transform='rotate(-4 570 197)'/>")
    p.append(_txt(620, 146, "rotule : 3 ddl", 11, ARBRE, "start", True))
    p.append(_txt(620, 164, "appui plan : 3 ddl", 11, ARBRE, "start", True))
    p.append(_txt(570, 228, "pièce brute, surface inclinée", 10, FIN, "middle"))
    p.append(_txt(570, 252, "libertés réunies : 3 rotations + 2 translations", 11, TRAIT, "middle"))
    p.append(_txt(570, 272, "→ PONCTUELLE équivalente (5 ddl)", 12, ARBRE, "middle", True))
    p.append(f"<rect x='30' y='300' width='715' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 322, "Piège : en série, on RÉUNIT les libertés, on ne les additionne pas (3 + 3 = 6 ddl serait « rien de bloqué »).", 12, TRAIT))
    return _svg("".join(p), 775, 348)


def glissiere_deux_colonnes():
    p = [_k_defs(), _txt(40, 24, "Guider une table en translation : deux colonnes ou une colonne et un appui", 13, TRAIT, "start", True)]
    for x0, titre, verdict, c in ((30, "DEUX COLONNES", "h = 8 − 6 + 1 = 3", ALERTE), (395, "UNE COLONNE + UN APPUI", "h = 5 − 6 + 1 = 0", OK)):
        p.append(f"<rect x='{x0}' y='40' width='350' height='262' rx='8' fill='#ffffff' stroke='{c}' stroke-width='2'/>")
        p.append(_txt(x0 + 175, 62, titre, 12, c, "middle", True))
        p.append(_txt(x0 + 175, 284, verdict, 13, c, "middle", True))
    # gauche : deux colonnes verticales, une table qui monte et descend
    for x in (110, 300):
        p.append(f"<rect x='{x - 6}' y='80' width='12' height='122' fill='#cbd5e1' stroke='{TRAIT}'/>")
    p.append(f"<g><rect x='80' y='150' width='250' height='26' rx='3' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.6'/>"
             f"<rect x='96' y='144' width='28' height='38' fill='none' stroke='{ALESAGE}' stroke-width='3'/>"
             f"<rect x='286' y='144' width='28' height='38' fill='none' stroke='{ALESAGE}' stroke-width='3'/>"
             "<animateTransform attributeName='transform' type='translate' values='0,0; 0,-40; 0,0' dur='3s' repeatCount='indefinite'/></g>")
    p.append(_txt(205, 102, "2 pivots glissants (douilles longues)", 10, ALESAGE, "middle", True))
    for i, t in enumerate(("3 conditions à tenir par l'usinage :", "• colonnes parallèles (2 directions)", "• même entraxe sur table et bâti")):
        p.append(_txt(48, 216 + 18 * i + 10, t, 11, ALERTE if i == 0 else TRAIT, "start", i == 0))
    # droite : une colonne + un galet bombé roulant sur une règle placée DEVANT la table (vue de dessus)
    p.append(f"<rect x='449' y='80' width='12' height='122' fill='#cbd5e1' stroke='{TRAIT}'/>")
    p.append(f"<g><rect x='425' y='150' width='160' height='26' rx='3' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.6'/>"
             f"<rect x='441' y='144' width='28' height='38' fill='none' stroke='{ALESAGE}' stroke-width='3'/>"
             f"<circle cx='570' cy='163' r='8' fill='#ffffff' stroke='{OK}' stroke-width='3'/>"
             "<animateTransform attributeName='transform' type='translate' values='0,0; 0,-40; 0,0' dur='3s' repeatCount='indefinite'/></g>")
    p.append(_txt(470, 102, "1 pivot glissant", 10, ALESAGE, "start", True))
    p.append(_txt(505, 196, "vue de face", 10, FIN, "middle"))
    # vue de dessus
    p.append(f"<rect x='608' y='76' width='130' height='126' rx='4' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(673, 92, "vue de dessus", 10, FIN, "middle"))
    p.append(f"<rect x='620' y='112' width='100' height='30' fill='#e2e8f0' stroke='{TRAIT}'/>")
    p.append(f"<circle cx='636' cy='127' r='9' fill='#cbd5e1' stroke='{ALESAGE}' stroke-width='2.4'/>")
    p.append(f"<line x1='614' y1='158' x2='734' y2='158' stroke='{TRAIT}' stroke-width='4'/>")
    p.append(f"<circle cx='706' cy='150' r='7' fill='#ffffff' stroke='{OK}' stroke-width='2.6'/>")
    p.append(_k_fl(706, 172, 706, 160, OK, "kg", 2))
    p.append(_txt(673, 184, "règle devant la table ;", 9, TRAIT, "middle"))
    p.append(_txt(673, 196, "normale ⊥ à colonne–galet", 9, OK, "middle", True))
    for i, t in enumerate(("Aucune condition : la table se monte sans", "contrainte ; le galet bombé (ponctuelle) arrête",
                           "seulement la rotation autour de la colonne.")):
        p.append(_txt(413, 216 + 18 * i + 10, t, 11, TRAIT))
    p.append(f"<rect x='30' y='312' width='715' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 334, "h compte les conditions géométriques à respecter : chacune se paie en usinage précis, ou en pièces qui forcent.", 12, TRAIT))
    return _svg("".join(p), 775, 360)


def broche_paliers():
    """Exercice : arbre de broche dans deux paliers lisses longs, butée axiale (sans la solution)."""
    p = [_k_defs(), _txt(40, 24, "Arbre de broche guidé par deux bagues longues en bronze", 13, TRAIT, "start", True)]
    p.append(f"<rect x='60' y='70' width='560' height='18' fill='#cbd5e1'/>")
    p.append(f"<rect x='60' y='196' width='560' height='18' fill='#cbd5e1'/>")
    p.append(_txt(64, 64, "carter (0), deux alésages usinés séparément", 10, FIN))
    p.append(f"<rect x='40' y='122' width='640' height='40' rx='4' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.6'>"
             "<animate attributeName='fill' values='#e2e8f0;#dbeafe;#e2e8f0' dur='1.5s' repeatCount='indefinite'/></rect>")
    p.append(_txt(360, 147, "arbre (1)", 11, TRAIT, "middle", True))
    for x, n in ((150, "bague 1 : L = 80 mm"), (480, "bague 2 : L = 80 mm")):
        p.append(f"<rect x='{x - 40}' y='88' width='80' height='34' fill='#fde68a' stroke='{ARBRE}' stroke-width='2'/>")
        p.append(f"<rect x='{x - 40}' y='162' width='80' height='34' fill='#fde68a' stroke='{ARBRE}' stroke-width='2'/>")
        p.append(_txt(x, 236, n, 11, ARBRE, "middle", True))
    p.append(f"<rect x='522' y='114' width='10' height='56' fill='{TRAIT}'/>")
    p.append(_txt(540, 98, "épaulement en appui", 10, TRAIT, "start"))
    p.append(_txt(540, 110, "sur la bague 2 (butée)", 10, TRAIT, "start"))
    p.append(_txt(150, 254, "Ø 40 mm", 10, FIN, "middle"))
    p.append(f"<line x1='150' y1='270' x2='480' y2='270' stroke='{FIN}'/>")
    p.append(_txt(315, 286, "entraxe des bagues : 330 mm", 10, FIN, "middle"))
    p.append(f"<rect x='40' y='298' width='700' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(56, 320, "Bagues de longueur 80 mm pour un diamètre de 40 mm (L = 2 × Ø). Cotes en mm.", 12, TRAIT))
    return _svg("".join(p), 760, 346)


# --- figure à curseurs (deux listes de choix)
_PALIERS = {
    "rot": ("rotule", "roulement arrêté axialement", 3, True, False),
    "la": ("linéaire annulaire", "roulement libre axialement", 2, False, False),
    "pg": ("pivot glissant", "bague longue libre", 4, False, True),
    "piv": ("pivot", "bague longue arrêtée", 5, True, True),
}


def dyn_arbre_deux_paliers(a="rot", b="la"):
    """Arbre sur deux paliers A et B (même axe) : inconnues, mobilité, hyperstatisme et conditions."""
    na, sa, ia, axa, la_ = _PALIERS[a]
    nb, sb, ib, axb, lb = _PALIERS[b]
    ns = ia + ib
    m = 1 if (axa or axb) else 2
    h = ns - 6 + m
    p = [_k_defs(), _txt(30, 24, f"Palier A : {na} · palier B : {nb}", 13, TRAIT, "start", True)]
    # arbre
    p.append(f"<rect x='40' y='112' width='380' height='18' rx='3' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.6'/>")
    for x, nom, sous, ax, long_ in ((120, na, sa, axa, la_), (340, nb, sb, axb, lb)):
        w = 70 if long_ else 30
        p.append(f"<rect x='{x - w / 2}' y='94' width='{w}' height='18' fill='#fde68a' stroke='{ARBRE}' stroke-width='2'/>")
        p.append(f"<rect x='{x - w / 2}' y='130' width='{w}' height='18' fill='#fde68a' stroke='{ARBRE}' stroke-width='2'/>")
        if ax:
            for dx in (-w / 2 - 6, w / 2 + 2):
                p.append(f"<rect x='{x + dx}' y='104' width='4' height='34' fill='{TRAIT}'/>")
            p.append(_txt(x, 172, "arrêté axialement", 10, TRAIT, "middle"))
        else:
            p.append(_k_fl(x + w / 2 + 6, 84, x + w / 2 + 30, 84, OK, "kg", 2))
            p.append(_txt(x, 172, "libre axialement", 10, OK, "middle"))
        p.append(_txt(x, 190, nom, 11, ARBRE, "middle", True))
        p.append(_txt(x, 206, sous, 10, FIN, "middle"))
    # calcul
    x0 = 450
    c = OK if h == 0 else ALERTE
    p.append(f"<rect x='{x0}' y='40' width='290' height='176' rx='6' fill='#ffffff' stroke='{c}' stroke-width='1.8'/>")
    lignes = [(f"Inconnues : Ns = {ia} + {ib} = {ns}", TRAIT, False),
              ("Équations : 6 × (2 − 1) = 6", TRAIT, False),
              (f"Mobilité : m = {m} " + ("(rotation)" if m == 1 else "(rotation + glissement)"), TRAIT, False),
              (f"h = {ns} − 6 + {m} = {h}", c, True),
              ("Liaison équivalente : " + ("pivot" if m == 1 else "pivot glissant"), TRAIT, False)]
    for i, (t, col, g) in enumerate(lignes):
        p.append(_txt(x0 + 14, 66 + 24 * i, t, 12, col, "start", g))
    # conditions géométriques
    cond = []
    n_ax = int(axa) + int(axb)
    if n_ax == 2:
        cond.append("• 1 : distance entre les deux arrêts axiaux (dilatation !)")
    n_long = int(la_) + int(lb)
    if n_long:
        cond.append("• 2 : l'axe de la bague longue doit passer par le centre de l'autre palier (2 décalages)" if n_long == 1
                    else "• 4 : les deux axes confondus : 2 décalages + 2 inclinaisons")
    if m == 2:
        cond.append("• aucune condition, mais l'arbre peut glisser : il manque un arrêt axial" if h == 0
                    else "• et l'arbre peut glisser : il manque un arrêt axial")
    if h == 0 and m == 1:
        cond.append("• aucune : montage sans contrainte, tolérances larges")
    p.append(f"<rect x='30' y='230' width='710' height='{34 + 20 * len(cond)}' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 250, "Conditions géométriques imposées (le compte redonne h) :", 12, TRAIT, "start", True))
    for i, t in enumerate(cond):
        p.append(_txt(56, 272 + 20 * i, t, 12, TRAIT))
    return _svg("".join(p), 760, 280 + 20 * len(cond) + 10)


_CHOIX_PALIERS = [("rotule (roulement arrêté)", "rot"), ("linéaire annulaire (roulement libre)", "la"),
                  ("pivot glissant (bague longue libre)", "pg"), ("pivot (bague longue arrêtée)", "piv")]

FIGURES_NOUVELLES = {
    "contacts_nature": ("Ponctuel, linéique, surfacique : la nature du contact", contacts_nature),
    "torseur_complementaire": ("Torseur transmissible d'un pivot : libre ↔ non transmis", torseur_complementaire),
    "liaisons_serie_parallele": ("Liaisons équivalentes en parallèle et en série", liaisons_serie_parallele),
    "glissiere_deux_colonnes": ("Glissière équivalente : deux colonnes ou une colonne et un appui", glissiere_deux_colonnes),
    "broche_paliers": ("Arbre de broche sur deux bagues longues", broche_paliers),
}
DYN_NOUVELLE = {
    "arbre_deux_paliers_choix": (
        "Choisis les deux paliers : inconnues, mobilité, hyperstatisme et conditions se recalculent",
        dyn_arbre_deux_paliers,
        [{"nom": "a", "label": "Palier A", "choix": _CHOIX_PALIERS, "defaut": "rotule (roulement arrêté)"},
         {"nom": "b", "label": "Palier B", "choix": _CHOIX_PALIERS, "defaut": "linéaire annulaire (roulement libre)"}]),
}

# ===========================================================================
# 2. FICHE 6.17 — en FIN de bloc 6 (après la 6.16)
# ===========================================================================

FICHE_6_17 = {
    "id": '6.17',
    "titre": 'Modéliser les liaisons : torseur transmissible, liaisons équivalentes, hyperstatisme',
    "duree": '6 h',
    "cours": """### 1. Pourquoi cette fiche

La fiche 6.1 nomme les liaisons, la fiche 6.3 explique pourquoi un montage hyperstatique coûte cher. Il
manque deux outils pour décider en bureau d'études :

- savoir **quels efforts** une liaison peut transmettre (pour dimensionner, et pour la statique de la
  fiche 6.16) ;
- **compter** l'hyperstatisme d'un montage, et savoir **quelles cotes** il impose.

Le référentiel (S3.2.1) demande explicitement ce calcul, pour les liaisons pivot, glissière et ponctuelle
équivalentes. Et c'est un vrai choix de conception : un
montage hyperstatique est rigide mais exige des pièces précises ; un montage isostatique se monte sans
contrainte avec des tolérances larges.

### 2. La nature du contact décide de la liaison

[[FIG:contacts_nature]]

Deux pièces se touchent selon un **point**, une **ligne** ou une **surface**. En général, plus la zone de
contact est étendue, plus elle bloque de mouvements :

| Contact | Liaison (nom normalisé) | ddl | Exemple |
|---|---|---|---|
| point | **ponctuelle** (sphère-plan) | 5 | bille, galet bombé, pointe de vis sur une face |
| ligne droite | **linéaire rectiligne** (cylindre-plan) | 4 | rouleau sur un plan |
| cercle | **linéaire annulaire** (sphère-cylindre) | 4 | bille dans un alésage, roulement libre axialement |
| sphère | **rotule** (sphérique) | 3 | rotule de direction, roulement arrêté axialement |
| plan | **appui plan** | 3 | pièce posée sur un marbre |
| cylindre | **pivot glissant** | 2 | tige dans un alésage long |

Pivot, glissière, hélicoïdale et encastrement ne viennent pas d'un seul contact élémentaire : on les obtient
en associant plusieurs contacts, par exemple un cylindre et un épaulement pour un pivot (§4).

**Les liaisons réelles ne sont jamais parfaites.** Il y a du jeu, des pièces qui fléchissent, du
frottement. Modéliser, c'est décider ce qui compte : un roulement à billes seul accepte que l'arbre
s'incline de quelques dixièmes de degré dans sa bague (le « rotulage ») ; on le modélise en **rotule**
(s'il est arrêté axialement) ou en **linéaire annulaire** (s'il peut coulisser). Un alésage **long** devant son diamètre empêche l'arbre de basculer : **pivot glissant**.
Un alésage **court** le laisse basculer un peu : **linéaire annulaire**.

### 3. Le torseur transmissible : ce qui est libre n'est pas transmis

[[FIG:torseur_complementaire]]

On attache à la liaison un **repère local** : trois axes posés sur la liaison elle-même, x le long de son
axe (ou z perpendiculaire à la surface de contact) — comme on cote une pièce depuis sa propre référence.
Dans ce repère, ce qu'une pièce exerce sur l'autre se décompose en six effets :

- trois **forces X, Y, Z**, qui poussent selon x, y, z ;
- trois **moments L, M, N**, qui font tourner autour de x, y, z (l'effet d'une clé sur un écrou : force ×
  bras de levier).

Ces six valeurs rangées ensemble forment le **torseur** de la fiche 6.16, écrit composante par composante.

> **Règle de complémentarité (liaison sans frottement)** : si un mouvement est **libre**, la composante
> d'action correspondante est **nulle**. Si un mouvement est **bloqué**, la liaison transmet l'action
> correspondante.

*Image : une porte sur ses gonds tourne librement ; on ne peut donc lui transmettre aucun moment autour
de l'axe des gonds (elle tournerait). Dans l'autre sens : soulevez la porte, les gonds résistent — ils
transmettent une force verticale, parce que ce mouvement est bloqué.*

**Pourquoi c'est forcément ainsi** : pour qu'une liaison exerce un effort dans une direction, il faut
qu'une surface s'y oppose. Si le mouvement est libre dans cette direction, aucune surface ne s'y oppose :
sans frottement, rien ne peut pousser dans ce sens.

D'où le tableau, au centre de chaque liaison :

| Liaison (repère local) | Mouvements libres | Forces transmises | Moments transmis | Inconnues |
|---|---|---|---|---|
| encastrement | aucun | X, Y, Z | L, M, N | 6 |
| pivot d'axe x | Rx | X, Y, Z | M, N | 5 |
| glissière d'axe x | Tx | Y, Z | L, M, N | 5 |
| hélicoïdale d'axe x | Rx et Tx liées | X, Y, Z | L (lié à X par le pas), M, N | 5 |
| pivot glissant d'axe x | Rx, Tx | Y, Z | M, N | 4 |
| rotule de centre O | Rx, Ry, Rz | X, Y, Z | aucun | 3 |
| appui plan de normale z | Tx, Ty, Rz | Z | L, M | 3 |
| linéaire annulaire d'axe x | Rx, Ry, Rz, Tx | Y, Z | aucun | 2 |
| linéaire rectiligne (normale z, ligne x) | Tx, Ty, Rx, Rz | Z | M | 2 |
| ponctuelle de normale z | tout sauf Tz | Z | aucun | 1 |

*Hélicoïdale = vis-écrou : tourner la vis la fait avancer, rotation et translation comptent pour **un seul**
ddl ; de même, le couple de serrage (L) et l'effort d'avance (X) sont liés par le pas.*

**À chaque fois : ddl + inconnues = 6.** Pourquoi 6 ? Il y a 6 mouvements dans l'espace ; chacun est soit
**libre** (1 ddl, pas d'effort), soit **bloqué** (1 inconnue d'effort). Chacun compte une fois, d'un côté
ou de l'autre. C'est le meilleur contrôle.

**Le lien avec la statique graphique (6.16).** La 6.16 demande, pour chaque force, soit sa direction,
soit un point de sa droite d'action. Le tableau dit ce qu'on sait, dans un problème plan :

- **rotule, ou pivot vu dans le plan perpendiculaire à son axe** : une force qui **passe par le centre**.
  On connaît son point, pas sa direction ;
- **ponctuelle** : une force **perpendiculaire au contact**. On connaît sa direction ;
- **glissière** : une force perpendiculaire au glissement (direction connue) **et** un moment — dans le
  plan, cela revient à une force dont on ne connaît **pas la position** ; **encastrement** : ni direction
  ni position. Pas de point connu : la méthode graphique ne s'applique pas, on calcule (12.1).

### 4. Liaisons équivalentes : en parallèle et en série

[[FIG:liaisons_serie_parallele]]

**En parallèle** (plusieurs liaisons entre les **deux mêmes** pièces) : chaque liaison bloque des
mouvements ; **les blocages se cumulent**. Les mouvements qui restent sont ceux que **toutes** laissent
libres. Les efforts, eux, se partagent : chaque palier porte une part de la charge.

- Arbre sur une **rotule** en A et une **linéaire annulaire** en B : seule la rotation autour de AB reste
  possible. **Pivot équivalent.**
- Deux **pivots glissants** d'axes parallèles (deux colonnes) : chaque colonne, seule, laisserait la table
  tourner autour d'elle ; mais si la table tournait autour de la colonne 1, la douille 2 devrait sortir de
  la colonne 2. Seule la translation commune reste. **Glissière équivalente.**

**En série** (pièce 1 → pièce intermédiaire → pièce 2) : chaque liaison ajoute ses libertés ; on **réunit**
les mouvements possibles.

- Patin de vérin : **rotule** (vérin–patin) puis **appui plan** (patin–pièce). Les libertés réunies :
  trois rotations et deux translations, soit **5 ddl : ponctuelle équivalente**. Le patin s'adapte à une
  surface brute inclinée, et ne pousse que selon la normale.
- **Piège** : 3 + 3 = 6 ddl donnerait « rien de bloqué ». Faux : la rotation autour de la normale est
  offerte **deux fois** (par la rotule et par l'appui plan). Elle ne compte qu'une fois dans la liaison
  équivalente, et laisse au patin une **mobilité interne** (un mouvement d'une pièce intermédiaire qui ne
  change rien pour les autres, comme une rondelle qui tourne sous un écrou).

**La symétrie à retenir** : en parallèle, un **blocage** présent deux fois donne de l'**hyperstatisme** ;
en série, une **liberté** présente deux fois donne une **mobilité interne**.

### 5. Mobilité et hyperstatisme : le calcul

**L'image avant le calcul : le tabouret et la table.** Un tabouret à **trois pieds** ne boite jamais :
quel que soit le sol, les trois pieds touchent, et la statique donne l'effort dans chacun : il est
**isostatique**. Une table à **quatre pieds** boite, sauf si le quatrième pied est exactement dans le plan
des trois autres : **une condition géométrique** à tenir. Et si on la force à poser sur ses quatre pieds,
l'effort dans chaque pied dépend de « qui est le plus long » : la statique ne peut pas le dire. C'est ce
que mesure h : les appuis en trop, qui obligent les pièces à être parfaites ou à forcer.

Pour un mécanisme de **p pièces** (bâti compris) :

- chaque pièce isolée donne **6 équations** : 3 sommes de forces (selon x, y, z) et 3 sommes de moments
  (autour de x, y, z) — le principe fondamental de la 12.1, passé de 3 équations dans le plan à 6 dans
  l'espace. On n'isole pas le **bâti** : il est fixé au sol, qui exerce sur lui des actions inconnues ;
  l'isoler ajouterait autant d'inconnues que d'équations. D'où **Es = 6 (p − 1)** ;
- chaque liaison apporte ses inconnues (tableau du §3) : **Ns = somme des inconnues** ;
- **m** est la **mobilité** : le nombre de mouvements indépendants encore possibles.

**Compter m, concrètement** : tenez le bâti dans un étau. Avec les mains, sans rien démonter, quels
mouvements pouvez-vous donner aux pièces ? Chaque mouvement indépendant compte 1. Arbre sur rotule +
linéaire annulaire : il tourne, c'est tout, m = 1. Arbre sur deux roulements **libres** axialement : il
tourne **et** coulisse, m = 2 — en général un défaut de conception (il manque un arrêt axial). S'y
ajoutent les mobilités internes, comme le patin qui tourne sur lui-même.

> **h = Ns − Es + m**

**Pourquoi « + m » ?** L'équation qui correspond à un mouvement possible ne contient aucune inconnue de
liaison : elle ne donne qu'une condition sur les efforts extérieurs (couple moteur = couple résistant), ou
0 = 0. Il reste donc **Es − m équations utiles**, et **h = inconnues − équations utiles**.

*Sur l'arbre (rotule en A + linéaire annulaire en B), l'équation des moments autour de l'axe x de l'arbre :
la rotule ne transmet aucun moment (L_A = 0), la linéaire annulaire non plus (L_B = 0). Elle s'écrit
L_A + L_B = 0, soit 0 = 0 : elle n'apprend rien, parce que l'arbre tourne librement autour de x. Il reste
5 équations utiles pour 5 inconnues : tout se calcule, h = 0.*

- **h = 0** : **isostatique**. Toutes les actions dans les liaisons se calculent par la statique ; le
  montage s'assemble sans contrainte.
- **h > 0** : **hyperstatique d'ordre h**. Il reste h inconnues que la statique ne peut pas trouver :
  elles dépendent des défauts de fabrication et des déformations.

**La même formule en plan** (fiche 12.1) : 3 équations par pièce, et les inconnues planes (appui simple 1,
articulation 2, encastrement 3). La poutre de la 12.1 sur **deux articulations** : Ns = 2 + 2 = 4, Es = 3, m = 0, **h = 1** — c'est exactement le
« 4 inconnues pour 3 équations » de la 12.1.

**Exemple pas à pas — l'arbre sur deux roulements.**

| Montage | Ns | Es | m | h |
|---|---|---|---|---|
| rotule en A + linéaire annulaire en B | 3 + 2 = 5 | 6 | 1 | **0** |
| rotule en A + rotule en B (deux roulements arrêtés) | 3 + 3 = 6 | 6 | 1 | **1** |

1. **Pièces** : le bâti et l'arbre, p = 2, donc Es = 6.
2. **Inconnues** : rotule 3, linéaire annulaire 2 (tableau du §3).
3. **Mobilité** : l'arbre tourne, rien d'autre : m = 1.
4. **h = 5 − 6 + 1 = 0** : isostatique. Avec deux rotules : h = 6 − 6 + 1 = **1**.

### 6. Le sens physique de h : des conditions à payer

**D'où vient le lien entre inconnues en trop et conditions géométriques ?** Prenons l'arbre sur **deux
roulements arrêtés** (h = 1). Les deux roulements empêchent tous les deux l'arbre de glisser selon son
axe : ce blocage est fait **deux fois**. Si la distance entre les deux arrêts vaut 300,00 mm sur l'arbre
et 300,05 mm dans le carter, il faut forcer pour monter l'arbre, et il reste tendu par un effort axial
qui dépend de ces 0,05 mm — que la statique ne peut pas calculer. **Un blocage fait deux fois = une
inconnue en trop = une cote qui doit être parfaite pour que les pièces ne forcent pas.** Le compte de h et
celui des conditions sont le même compte.

[[DYN:arbre_deux_paliers_choix]]

**h compte les conditions géométriques** que les pièces doivent respecter pour s'assembler sans forcer.
Chaque condition se paie d'une des trois façons :

- par la **précision** : une tolérance serrée (distances : fiche 2.1 ; coaxialité, parallélisme : fiche
  2.3), ou les deux alésages usinés **en une seule passe** (même outil, même réglage) ;
- par la **déformation** : les pièces forcent, s'usent, chauffent ;
- par un **réglage** au montage : cales pelables sous un palier, bague excentrée qu'on tourne pour décaler
  un axe de quelques centièmes.

| Montage | h | Conditions (le compte redonne h) |
|---|---|---|
| arbre sur deux rotules | 1 | distance entre les deux arrêts axiaux — et la dilatation la fait varier |
| arbre sur deux bagues longues | 4 | les deux axes confondus : 2 décalages (selon y et z) + 2 inclinaisons (autour de y et z) |
| table sur deux colonnes | 3 | parallélisme des colonnes (2 directions) + même entraxe sur table et bâti |
| colonne + appui ponctuel | 0 | aucune |

[[FIG:glissiere_deux_colonnes]]

**Isostatique ou hyperstatique, que choisir ?** Ce n'est pas une règle morale :

| Choix | Pour | Contre |
|---|---|---|
| **isostatique** | tolérances larges, montage sans réglage, dilatation libre | moins rigide (moins d'appuis, chacun porte plus), parfois plus de pièces (butées, galets) |
| **hyperstatique** | rigidité, efforts répartis sur plus d'appuis | conditions géométriques à usiner ou à régler, risque de contraintes au montage |

Le réflexe de concepteur : **calculer h, lister les conditions, puis décider** si on les usine (précision
payée une fois), si on les règle, ou si on les supprime en changeant une liaison (rotule, linéaire
annulaire, appui ponctuel).

### 7. Les erreurs classiques

1. **Oublier le bâti** dans p, ou le compter deux fois : Es = 6 (p − 1), le bâti est l'une des p pièces.
2. **Oublier la mobilité** : écrire h = Ns − Es. Pour un arbre qui tourne, il manque + 1.
3. **Confondre ddl et inconnues** : une rotule a 3 ddl **et** 3 inconnues ; un pivot a 1 ddl mais **5**
   inconnues. Contrôle : ddl + inconnues = 6.
4. **Additionner les libertés en série** sans repérer celles qui se répètent : le patin à rotule n'a pas 6
   ddl, il en a 5, plus une mobilité interne.
5. **Croire qu'un hyperstatisme est une faute** : c'est un choix, à condition d'en connaître le prix.
6. **Écrire une composante transmise pour un mouvement libre** : un pivot d'axe x ne transmet aucun moment
   autour de x (sans frottement).

### 8. À retenir

- La **nature du contact** (point, ligne, surface) donne la liaison ; un alésage long devant son diamètre =
  pivot glissant, court = linéaire annulaire.
- **Torseur transmissible** : mouvement libre ↔ composante nulle. **ddl + inconnues = 6.**
- **Parallèle** : les blocages se cumulent (un blocage en double = hyperstatisme). **Série** : on réunit
  les libertés (une liberté en double = mobilité interne).
- **h = Ns − Es + m**, avec Es = 6 (p − 1), bâti compris dans p.
- **h = nombre de conditions géométriques** à payer : précision, déformation ou réglage.
- Pivot isostatique : **rotule + linéaire annulaire**. Glissière isostatique : **pivot glissant +
  ponctuelle**. Ponctuelle « adaptative » : **rotule + appui plan** en série.
""",
    "formules": """
**Contact** — point : ponctuelle (5 ddl) · ligne : linéaire rectiligne ou annulaire (4) · surface : appui
plan, rotule (3), pivot glissant (2)

**Torseur transmissible** — mouvement libre ↔ composante d'action nulle (sans frottement) ·
ddl + inconnues = 6

**Inconnues par liaison** — encastrement 6 · pivot, glissière, hélicoïdale 5 · pivot glissant 4 ·
rotule, appui plan 3 · linéaire annulaire, linéaire rectiligne 2 · ponctuelle 1

**Liaisons équivalentes** — en parallèle : les blocages s'ajoutent · en série : on réunit les libertés

**Hyperstatisme** — h = Ns − Es + m · Es = 6 (p − 1), p pièces bâti compris · en plan : Es = 3 (p − 1)

**Montages isostatiques types** — pivot : rotule + linéaire annulaire · glissière : pivot glissant +
ponctuelle · ponctuelle adaptative : rotule + appui plan en série
""",
    "exemple": """
### Cas industriel — Le convoyeur qui force à chaque montage

**Le symptôme.** L'arbre d'entraînement d'un convoyeur (Ø 40, entraxe des paliers 900 mm) tourne dans
deux **paliers à bague bronze longue**, boulonnés sur deux supports soudés au châssis. À chaque
remplacement de bague, l'arbre devient dur à tourner, les bagues chauffent, et l'une d'elles est usée
d'un seul côté au bout de quelques semaines.

**L'analyse.** Deux bagues longues = deux **pivots glissants** ; un épaulement arrête l'arbre axialement
(une inconnue de plus). Ns = 4 + 4 + 1 = 9, Es = 6, m = 1 : **h = 4**. Les quatre conditions sont la
**coaxialité** des deux alésages : les deux axes doivent être confondus (2 décalages + 2 inclinaisons). Sur
un châssis soudé, avec deux
supports usinés séparément, personne ne garantit cela à quelques centièmes sur 900 mm : l'arbre est
**forcé** dans des bagues désalignées.

**Les corrections possibles :**

| Action | h | Effet |
|---|---|---|
| **paliers à semelle à roulement auto-aligneur** (palier en fonte boulonné, contenant un roulement à rotule) : un arrêté (rotule), un libre (linéaire annulaire) | 5 − 6 + 1 = 0 | aucune coaxialité à tenir ; la dilatation de l'arbre est libre |
| bagues **courtes** (linéaires annulaires) + une seule butée | 2 + 2 + 1 − 6 + 1 = 0 | plus de coaxialité à tenir ; mais une bague courte en bronze s'use plus vite (pression de contact plus forte) |
| reprendre les deux alésages **en une seule passe**, supports montés | 4 | les conditions restent, mais on les obtient par l'usinage |

**Ce que le cas apprend.** Le problème n'était pas la qualité des bagues : c'était le **modèle** du
montage. Le calcul de h, fait avant de dessiner les supports, désigne les cotes impossibles à tenir sur
un châssis soudé.
""",
    "exercice": """
### Exercice — L'arbre de broche

[[FIG:broche_paliers]]

Un arbre de broche (1) tourne dans un carter (0), guidé par **deux bagues en bronze longues** (longueur
80 mm pour un diamètre de 40 mm), distantes de 330 mm. Un épaulement de l'arbre appuie sur la bague 2 :
c'est la butée axiale, une couronne d'appui étroite. Les deux alésages du carter sont usinés
**séparément**.

**1.** Modélisez chaque bague, puis la butée. Justifiez par la nature du contact.

**2.** Écrivez le torseur transmissible d'une bague, dans son repère local (x : axe de l'arbre).

**3.** Calculez Ns, Es, m, puis h.

**4.** Quelles conditions géométriques ce montage impose-t-il ? Combien sont-elles ?

**5.** Proposez un montage isostatique qui garde la fonction (arbre qui tourne, arrêté axialement).
Calculez son h.

**6.** Si l'on garde les bagues longues, quelle solution d'usinage permet de tenir les conditions ?
""",
    "corrige": """
### Corrigé, en six temps

#### 1. Ce que dit l'énoncé

Deux pièces (carter, arbre), trois liaisons en parallèle : deux bagues longues et une butée. L'arbre doit
tourner et être arrêté axialement. On cherche h et ce qu'il impose.

#### 2. Quelle règle, et pourquoi

> Alésage **long** → pivot glissant. **Torseur** : mouvement libre ↔ composante nulle.
> **h = Ns − Es + m**, Es = 6 (p − 1). **h = nombre de conditions géométriques.**

#### 3. Les conversions

Aucune : on compte des inconnues et des équations. Le rapport L/Ø = 80 / 40 = 2 sert seulement à choisir le
modèle (bague longue).

#### 4. Le remplacement

p = 2, donc Es = 6. Bague longue : pivot glissant, 4 inconnues. Butée : ponctuelle, 1 inconnue.
Mouvement possible : la rotation de l'arbre, m = 1.

#### 5. Le calcul

**1.** Chaque bague est longue (L = 2 × Ø) : elle empêche l'arbre de basculer et laisse tourner et
coulisser → **pivot glissant** d'axe x. La butée : une couronne étroite. Pourquoi pas un appui plan ? Face
aux deux bagues longues, son bras de levier est trop petit pour empêcher l'arbre de basculer : les bagues
s'en chargent. On ne garde que ce qu'elle fait vraiment, empêcher l'avance → **ponctuelle** de normale x.

**2.** Bague, au centre, axe x : forces **(0, Y, Z)**, moments **(0, M, N)** — Tx et Rx libres, donc X = 0
et L = 0. Quatre inconnues.

**3.** Ns = 4 + 4 + 1 = **9** ; Es = 6 × (2 − 1) = **6** ; m = **1** ; **h = 9 − 6 + 1 = 4**.

**4.** Quatre conditions : les deux axes doivent être **confondus** — l'axe de la bague 2 ni décalé (selon y,
selon z), ni incliné (autour de y, autour de z) par rapport à celui de la bague 1. Image : une longue tige
dans deux douilles longues ; si l'une est décalée **ou** penchée, la tige coince. Avec deux alésages usinés
séparément, ces conditions ne sont pas tenues : l'arbre force.

**5.** Rotule (roulement arrêté axialement) en A + linéaire annulaire (roulement libre) en B :
Ns = 3 + 2 = 5, **h = 5 − 6 + 1 = 0**. La butée devient inutile : la rotule arrête l'arbre axialement.

**6.** **Aléser les deux paliers en une seule passe** (même outil, même réglage, carter monté) : la
coaxialité est obtenue par l'usinage. Le montage reste hyperstatique (h = 4), mais ses conditions sont
tenues.

#### 6. La vérification

**Contrôle ddl + inconnues = 6** : pivot glissant 2 + 4, ponctuelle 5 + 1. **Contrôle par les
conditions** : quatre conditions listées pour h = 4, aucune pour h = 0 — le compte concorde. **Le choix du
modèle compte** : si l'on modélisait l'épaulement en appui plan (3 inconnues), on trouverait h = 6, deux
conditions de plus — la perpendicularité de la face d'appui à l'axe, qu'on tolérance d'ailleurs sur les
plans de broche. **Bon sens** : une broche de machine-outil est souvent volontairement hyperstatique, pour
la rigidité ; ses alésages sont alors usinés en ligne (d'un même passage d'outil, carter monté), jamais
séparément.
""",
}

# ===========================================================================
# 3. MÉTHODE
# ===========================================================================
MTH_6_17 = ("6.17", "Calculer le degré d'hyperstatisme d'un montage", [
    "**Compter les pièces p, bâti compris**, et en déduire les équations : Es = 6 (p − 1) "
    "(3 (p − 1) pour un problème plan).",
    "**Modéliser chaque liaison** par la nature du contact (alésage long : pivot glissant ; court : "
    "linéaire annulaire ; roulement arrêté : rotule…).",
    "**Additionner les inconnues** de toutes les liaisons (tableau du torseur transmissible) : Ns. "
    "Contrôle pour chaque liaison : ddl + inconnues = 6.",
    "**Compter la mobilité m** : le mouvement utile, plus les mobilités internes (pièce qui peut "
    "tourner sur elle-même sans effet).",
    "**Calculer h = Ns − Es + m**, puis **lister les conditions géométriques** : il doit y en avoir h. "
    "Décider : les usiner, les régler, ou changer une liaison.",
], "Arbre sur deux roulements arrêtés (deux rotules) : p = 2, Es = 6 ; Ns = 3 + 3 = 6 ; m = 1 ; "
   "h = 6 − 6 + 1 = 1. Condition : la distance entre les deux arrêts axiaux. Remède : libérer un "
   "roulement (linéaire annulaire), h = 0.")

# ===========================================================================
# 4. ATELIERS (fin de liste ATELIERS, après at159)
# ===========================================================================
ATELIERS_NOUVEAUX = [
    {
        "id": "at160",
        "chapitre": "Bloc 6",
        "titre": "Presse à deux colonnes : une glissière qui coûte trois conditions",
        "theme": "Liaisons et guidages",
        "fiche": "6.17",
        "figure": "glissiere_deux_colonnes",
        "vocabulaire": [
            ("Pivot glissant",
             "liaison d'une tige dans un alésage long : elle peut tourner et coulisser, rien d'autre. "
             "4 inconnues d'effort."),
            ("Degré d'hyperstatisme h",
             "le nombre d'inconnues que la statique ne peut pas trouver : h = Ns − Es + m. C'est aussi "
             "le nombre de conditions géométriques à respecter."),
            ("Mobilité m",
             "le nombre de mouvements indépendants encore possibles dans le montage."),
        ],
        "enonce": "Le coulisseau d'une petite presse est guidé par deux colonnes verticales parallèles, "
                  "chacune dans une douille longue. On étudie le guidage seul : bâti (0) et coulisseau "
                  "(1).",
        "etapes": [
            {"type": "numerique", "label": "Inconnues des deux douilles",
             "unite": "sans unité", "attendu": 8, "tol": 0.1,
             "consigne": "Chaque douille longue est un pivot glissant. Combien d'inconnues d'effort Ns "
                         "les deux douilles apportent-elles ensemble ?",
             "indice": "Pivot glissant : 2 ddl, donc 6 − 2 = 4 inconnues, par douille.",
             "pieges": [(4, "4, c'est une seule douille. Il y en a deux, en parallèle : leurs inconnues "
                            "s'ajoutent."),
                        (2, "2, ce sont les ddl d'un pivot glissant (tourner, coulisser). Les inconnues "
                            "d'effort sont le complément à 6 : 4 par douille.")],
             "aide": "4 + 4 = 8 inconnues."},
            {"type": "numerique", "label": "Équations",
             "unite": "sans unité", "attendu": 6, "tol": 0.1,
             "consigne": "Le montage compte deux pièces, bâti compris. Combien d'équations Es la statique "
                         "fournit-elle ?",
             "indice": "Es = 6 × (p − 1).",
             "pieges": [(12, "12 = 6 × 2 : le bâti ne donne pas d'équations (on ne l'isole pas). "
                             "Es = 6 × (2 − 1).")],
             "aide": "Es = 6 × (2 − 1) = 6."},
            {"type": "numerique", "label": "Degré d'hyperstatisme",
             "unite": "sans unité", "attendu": 3, "tol": 0.1,
             "consigne": "Le coulisseau ne peut que monter et descendre : m = 1. Calcule h.",
             "indice": "h = Ns − Es + m.",
             "pieges": [(2, "2 = 8 − 6 : il manque la mobilité. Le mouvement de translation rend une "
                            "équation inutile : + 1."),
                        (1, "1 : tu as soustrait la mobilité. h = Ns − Es + m, avec un signe plus.")],
             "aide": "h = 8 − 6 + 1 = 3."},
            {"type": "qcm", "label": "Les conditions",
             "question": "Quelles sont les trois conditions géométriques à tenir ?",
             "options": ["La longueur des deux colonnes, et leur diamètre",
                         "Le parallélisme des deux colonnes (dans deux directions), et le même entraxe "
                         "sur le bâti et sur le coulisseau",
                         "La rugosité des colonnes, la dureté des douilles, le graissage"], "bonne": 1,
             "indice": "Ce qui empêche de monter le coulisseau sans forcer : l'orientation relative des "
                       "colonnes et leur écartement.",
             "diagnostics": {0: "La longueur et le diamètre n'empêchent pas le montage. Ce sont "
                                 "l'orientation (parallélisme) et l'écartement (entraxe) qui forcent.",
                             2: "Ce sont des conditions de bon fonctionnement. h ne compte que les "
                                "conditions d'assemblage : ce qui empêche de monter sans forcer."}},
            {"type": "numerique", "label": "Montage isostatique",
             "unite": "sans unité", "attendu": 0, "tol": 0.1,
             "consigne": "On garde une seule colonne (pivot glissant) et on remplace la seconde par un "
                         "galet BOMBÉ roulant sur une règle placée devant la table : il touche la règle en "
                         "un point (ponctuelle), et appuie de face, perpendiculairement au plan qui contient "
                         "la colonne et le galet. Calcule le nouveau h.",
             "indice": "Ns = 4 + 1 ; Es et m ne changent pas.",
             "pieges": [(1, "1 : tu as compté 2 inconnues pour le galet (linéaire rectiligne ou "
                            "annulaire). Un galet BOMBÉ touche la règle en un point : ponctuelle, 1 inconnue."),
                        (-1, "−1 : il manque la mobilité (+ 1).")],
             "aide": "h = 5 − 6 + 1 = 0."},
        ],
        "corrige": {
            "enonce": "Coulisseau de presse guidé par deux colonnes dans des douilles longues.",
            "regle": "**h = Ns − Es + m**, Es = 6 (p − 1). Pivot glissant : **4** inconnues ; "
                    "ponctuelle : **1**. h = nombre de conditions géométriques.",
            "conversions": "Sans objet : on compte des inconnues et des équations.",
            "remplacement": "Ns = 4 + 4 ; Es = 6 × 1 ; m = 1. Variante : Ns = 4 + 1.",
            "calcul": "Deux colonnes : **h = 8 − 6 + 1 = 3**. Colonne + galet : **h = 5 − 6 + 1 = 0**.",
            "verification": "Trois conditions listées (parallélisme dans deux directions, entraxe) pour "
                            "h = 3. Avec le galet, plus de condition d'assemblage. Trois précisions : le "
                            "galet doit appuyer perpendiculairement au plan colonne–galet (s'il appuyait "
                            "vers la colonne, il n'arrêterait pas la rotation : m = 2) ; il doit être "
                            "maintenu en appui (ressort, poids) ; la rectitude de la règle reste une "
                            "condition de précision du guidage, pas d'assemblage. Un galet cylindrique "
                            "(contact linéique) donnerait h = 1.",
        },
        "a_retenir": "À retenir : deux colonnes, c'est h = 3 — parallélisme et entraxe à usiner. Une "
                     "colonne et un appui ponctuel suffisent pour guider en translation sans contrainte.",
    },
    {
        "id": "at161",
        "chapitre": "Bloc 6",
        "titre": "Patin à rotule : deux liaisons en série, une ponctuelle équivalente",
        "theme": "Liaisons et guidages",
        "fiche": "6.17",
        "figure": "liaisons_serie_parallele",
        "vocabulaire": [
            ("En série",
             "deux liaisons enchaînées par une pièce intermédiaire (vérin → patin → pièce). Les libertés "
             "se réunissent."),
            ("Mobilité interne",
             "un mouvement possible d'une pièce qui n'a aucun effet sur le reste du mécanisme : le patin "
             "qui tourne sur lui-même."),
            ("Torseur transmissible",
             "les forces et moments qu'une liaison peut transmettre : tout sauf ce qui correspond à un "
             "mouvement libre."),
        ],
        "enonce": "Un vérin de bridage appuie sur une pièce brute par un patin : le patin est relié à la "
                  "tige par une rotule, et repose à plat sur la pièce (appui plan). On cherche la "
                  "liaison équivalente entre la tige et la pièce.",
        "etapes": [
            {"type": "numerique", "label": "ddl de la rotule",
             "unite": "sans unité", "attendu": 3, "tol": 0.1,
             "consigne": "Combien de degrés de liberté une rotule laisse-t-elle ?",
             "indice": "Les trois rotations autour du centre.",
             "pieges": [(5, "5, c'est une ponctuelle. La rotule bloque les trois translations : il "
                            "reste les trois rotations.")],
             "aide": "3 : Rx, Ry, Rz."},
            {"type": "numerique", "label": "ddl de la liaison équivalente",
             "unite": "sans unité", "attendu": 5, "tol": 0.1,
             "consigne": "L'appui plan (normale z) laisse Tx, Ty et Rz. En série, on réunit les libertés "
                         "des deux liaisons. Combien de ddl différents au total ?",
             "indice": "Rotule : Rx, Ry, Rz. Appui plan : Tx, Ty, Rz. Rz apparaît deux fois.",
             "pieges": [(6, "6 = 3 + 3 : Rz est compté deux fois. On réunit les libertés, on ne les "
                            "additionne pas : 5 ddl différents.")],
             "aide": "Rx, Ry, Rz, Tx, Ty : 5 ddl."},
            {"type": "qcm", "label": "Nom de la liaison équivalente",
             "question": "Quelle liaison laisse 5 ddl et ne bloque que la translation selon la normale ?",
             "options": ["Une linéaire annulaire", "Une ponctuelle (sphère-plan)", "Un appui plan"],
             "bonne": 1,
             "indice": "1 seul mouvement bloqué : un contact en un point.",
             "diagnostics": {0: "La linéaire annulaire laisse 4 ddl (elle bloque deux translations).",
                             2: "L'appui plan laisse 3 ddl (il bloque une translation et deux rotations)."}},
            {"type": "numerique", "label": "Inconnues transmises",
             "unite": "sans unité", "attendu": 1, "tol": 0.1,
             "consigne": "Combien de composantes d'action la liaison équivalente transmet-elle ?",
             "indice": "ddl + inconnues = 6.",
             "pieges": [(5, "5, ce sont ses ddl. Les inconnues sont le complément : 6 − 5.")],
             "aide": "6 − 5 = 1 : la seule force normale Z."},
            {"type": "qcm", "label": "Pourquoi ce montage",
             "question": "Pourquoi monter un patin à rotule plutôt qu'une tige à bout plat ?",
             "options": ["Pour que l'effort de bridage soit plus grand",
                         "Pour économiser une pièce",
                         "Pour que le patin s'oriente sur une surface brute inclinée et ne pousse que "
                         "selon la normale, sans moment parasite"], "bonne": 2,
             "indice": "Une tige à bout plat sur une surface inclinée ne touche que par un bord.",
             "diagnostics": {0: "L'effort vient du vérin (pression × section) : le patin ne le "
                                 "change pas. Il change où et comment il s'applique.",
                             1: "On ajoute une pièce (le patin) : ce n'est pas une économie, c'est un "
                                "choix de conception."}},
        ],
        "corrige": {
            "enonce": "Patin de bridage : rotule (tige–patin) puis appui plan (patin–pièce), en série.",
            "regle": "**En série, on réunit les libertés**, sans compter deux fois celles qui se "
                    "répètent. **ddl + inconnues = 6.**",
            "conversions": "Sans objet.",
            "remplacement": "Rotule {Rx, Ry, Rz} ∪ appui plan {Tx, Ty, Rz} = {Rx, Ry, Rz, Tx, Ty}.",
            "calcul": "**5 ddl** : **ponctuelle** équivalente ; **1 inconnue** (la force normale).",
            "verification": "3 + 3 = 6 mouvements offerts pour 5 différents : il reste une mobilité "
                            "interne, le patin qui tourne sur lui-même autour de la normale, sans effet "
                            "sur la pièce. Le patin peut s'orienter sur une surface brute : c'est "
                            "pourquoi on le choisit pour brider des bruts de fonderie.",
        },
        "a_retenir": "À retenir : en série, on réunit les libertés ; une liberté offerte deux fois ne "
                     "compte qu'une fois, et laisse une mobilité interne.",
    },
]

# ===========================================================================
# 5. GÉNÉRATEUR (famille « Liaisons » de l'Entraînement)
# ===========================================================================
GENERATEUR = '''
def gen_hyperstatisme_paliers():
    """Degré d'hyperstatisme d'un arbre sur deux paliers coaxiaux, modèles tirés au hasard."""
    paliers = [("une rotule (roulement arrêté axialement)", 3, True),
               ("une linéaire annulaire (roulement libre axialement)", 2, False),
               ("un pivot glissant (bague longue, libre axialement)", 4, False),
               ("un pivot (bague longue arrêtée axialement)", 5, True)]
    (na, ia, axa), (nb, ib, axb) = random.choice(paliers), random.choice(paliers)
    ns = ia + ib
    m = 1 if (axa or axb) else 2
    h = ns - 6 + m
    cond = []
    if axa and axb:
        cond.append("1 pour la distance entre les deux arrêts axiaux")
    n_long = (ia in (4, 5)) + (ib in (4, 5))
    if n_long == 1:
        cond.append("2 pour que l'axe de la bague longue passe par le centre de l'autre palier")
    elif n_long == 2:
        cond.append("4 pour que les deux axes soient confondus (2 décalages, 2 inclinaisons)")
    diag = []
    for v, msg in (
            (ns - 6, "Tu as oublié la mobilité : h = Ns − Es + m. Chaque mouvement possible rend une "
                     "équation inutile."),
            (ns - 6 - m, "Tu as soustrait la mobilité. La formule est h = Ns − Es + m, avec un signe plus."),
            (ns - 12 + m, "Tu as compté 12 équations (6 par pièce, bâti compris). Le bâti ne donne pas "
                          "d'équations : Es = 6 × (2 − 1) = 6."),
            ((6 - ia) + (6 - ib) - 6 + m, "Tu as additionné les ddl des paliers au lieu de leurs "
                                          "inconnues d'effort (6 − ddl)."),
    ):
        if abs(v - h) > 0.5 and all(abs(v - d["v"]) > 0.5 for d in diag):
            diag.append(_diag(float(v), msg))
    return {
        "titre": "Liaisons — degré d'hyperstatisme d'un arbre sur deux paliers",
        "enonce": (f"Un arbre tourne dans un bâti, guidé par deux paliers coaxiaux : en A, {na} ; en B, "
                   f"{nb}. Quel est le degré d'hyperstatisme h du montage ?"),
        "rep": float(h), "tol": 0.1, "unite": "",
        "diag": diag,
        "corr": [
            "**Ce que dit l'énoncé.** Deux pièces (bâti, arbre) et deux liaisons en parallèle. On cherche h.",
            f"**Les inconnues.** Palier A : {ia} inconnues ; palier B : {ib}. Ns = {ia} + {ib} = {ns}.",
            "**Les équations.** Deux pièces, bâti compris : Es = 6 × (2 − 1) = 6.",
            f"**La mobilité.** L'arbre tourne" + (" ; aucun palier ne l'arrête axialement, il peut aussi "
                                                  "glisser" if m == 2 else "") + f" : m = {m}.",
            f"**Le calcul.** h = Ns − Es + m = {ns} − 6 + {m} = {h}.",
            "**Je vérifie.** " + ("Montage isostatique : aucune condition géométrique." if h == 0 else
                                  f"{h} condition(s) géométrique(s) à tenir : " + " ; ".join(cond) + ".")
            + (" Attention : l'arbre peut glisser, il manque un arrêt axial." if m == 2 else ""),
        ],
        "indice": "h = Ns − Es + m ; rotule 3, linéaire annulaire 2, pivot glissant 4, pivot 5 inconnues.",
    }
'''

# ===========================================================================
# 6. QUIZ — nouvelle catégorie « Modélisation des liaisons »
#    positions de la bonne réponse : 2, 0, 3, 1, 1, 3, 0, 2
# ===========================================================================
QUIZ_LIAISONS = [
    ("Un pivot d'axe x, sans frottement : quelle composante d'action ne peut-il PAS transmettre ?",
     ["La force selon x", "Le moment autour de y", "Le moment autour de x", "La force selon z"], 2,
     "Le pivot laisse libre la rotation autour de x : il ne peut donc transmettre aucun moment autour "
     "de x (L = 0). Il transmet tout le reste : X, Y, Z, M, N, soit 5 inconnues.", "Base"),
    ("Combien d'inconnues d'effort une liaison rotule transmet-elle ?",
     ["3", "1", "5", "6"], 0,
     "Une rotule laisse 3 rotations libres : elle transmet les 3 forces, aucun moment. ddl + inconnues "
     "= 6 : 3 + 3.", "Base"),
    ("Un arbre est guidé par une rotule en A et une linéaire annulaire en B, sur le même axe. Quel est "
     "son degré d'hyperstatisme ?",
     ["1", "2", "5", "0"], 3,
     "Ns = 3 + 2 = 5, Es = 6, m = 1 (rotation) : h = 5 − 6 + 1 = 0. C'est le montage isostatique "
     "classique d'un arbre sur deux roulements, un arrêté et un libre.", "Calcul"),
    ("Dans la formule h = Ns − Es + m, pourquoi ajoute-t-on la mobilité m ?",
     ["Parce que chaque mouvement ajoute une inconnue d'effort",
      "Parce que chaque mouvement possible rend une équation de la statique inutile (0 = 0)",
      "Parce que le bâti compte pour une pièce", "Par convention, sans raison physique"], 1,
     "Une équation qui correspond à un mouvement libre ne contient aucune inconnue d'effort : elle "
     "s'écrit 0 = 0 et n'aide à rien. Il reste Es − m équations utiles, d'où h = Ns − (Es − m).",
     "Intermédiaire"),
    ("Une rotule (3 ddl) et un appui plan (3 ddl) sont montés en série, comme un patin de vérin. Combien "
     "de ddl a la liaison équivalente ?",
     ["6", "5", "3", "0"], 1,
     "On réunit les libertés : {Rx, Ry, Rz} et {Tx, Ty, Rz}. Rz apparaît deux fois : 5 ddl différents, "
     "une ponctuelle. Le doublon laisse une mobilité interne (le patin tourne sur lui-même).", "Piège"),
    ("Un coulisseau est guidé par deux colonnes parallèles dans des douilles longues. Quel est le degré "
     "d'hyperstatisme du guidage ?",
     ["0", "1", "8", "3"], 3,
     "Ns = 4 + 4 = 8, Es = 6, m = 1 : h = 3. Trois conditions : parallélisme des colonnes dans deux "
     "directions, et même entraxe sur le bâti et sur le coulisseau.", "Calcul"),
    ("Que représente concrètement un degré d'hyperstatisme h = 2 ?",
     ["Deux conditions géométriques à respecter, par la précision, la déformation ou un réglage",
      "Deux pièces de trop dans le mécanisme",
      "Deux mouvements parasites possibles (deux mobilités en trop)",
      "Un mécanisme qui ne peut pas fonctionner"], 0,
     "h compte les conditions géométriques (coaxialité, parallélisme, distance) que les pièces doivent "
     "respecter pour s'assembler sans forcer. Un montage hyperstatique fonctionne : il coûte plus cher "
     "en usinage ou en réglage.", "Intermédiaire"),
    ("Un arbre tourne dans un alésage dont la longueur vaut deux fois le diamètre. Quel modèle choisir ?",
     ["Une linéaire annulaire", "Une rotule", "Un pivot glissant", "Une ponctuelle"], 2,
     "Un alésage long empêche l'arbre de basculer : il bloque deux translations et deux rotations, "
     "et laisse la rotation et le glissement. C'est un pivot glissant. Un alésage court le laisserait "
     "basculer : linéaire annulaire.", "Base"),
]
