# -*- coding: utf-8 -*-
"""
figures.py — Schémas pédagogiques de l'application BTS CPI.

Chaque figure est un dessin vectoriel (SVG) généré par le code : aucune image
n'est téléchargée, rien n'est copié sur internet, tout est libre de droits et
reste net quel que soit le zoom.

Utilisation dans une fiche de cours : écrire le marqueur [[FIG:cle]] dans le
texte, à l'endroit exact où le schéma doit apparaître. Par exemple :

    ### 2. Les trois natures d'ajustement
    [[FIG:trois_ajustements]]

Ajouter une figure = écrire une fonction qui renvoie du SVG, puis l'inscrire
dans le dictionnaire FIGURES en bas du fichier.
"""

import base64

# --- palette commune (fond clair) ------------------------------------------
TRAIT = "#1f2937"      # trait fort : contours vus
FIN = "#6b7280"        # trait fin : cotes, attaches
AXE = "#0891b2"        # axes et repères
ALESAGE = "#2563eb"    # tout ce qui concerne la pièce creuse
ARBRE = "#ea580c"      # tout ce qui concerne la pièce pleine
OK = "#16a34a"
ALERTE = "#dc2626"
FOND = "#f8fafc"

_POLICE = "font-family='system-ui, sans-serif'"


def _svg(contenu, largeur=760, hauteur=380):
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {largeur} {hauteur}' "
            f"width='100%' style='max-width:{largeur}px;height:auto'>"
            f"<rect width='{largeur}' height='{hauteur}' fill='{FOND}' rx='8'/>"
            f"{contenu}</svg>")


def _txt(x, y, texte, taille=13, couleur=TRAIT, ancre="start", gras=False):
    poids = "600" if gras else "400"
    return (f"<text x='{x}' y='{y}' {_POLICE} font-size='{taille}' fill='{couleur}' "
            f"text-anchor='{ancre}' font-weight='{poids}'>{texte}</text>")


# ===========================================================================
# 1. PROJECTION EUROPÉENNE — où se placent les vues
# ===========================================================================

def projection_europeenne():
    p = []
    # vue de face
    p.append(f"<rect x='90' y='60' width='170' height='110' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2.5'/>")
    p.append(_txt(175, 120, "VUE DE FACE", 14, TRAIT, "middle", True))
    p.append(_txt(175, 140, "on la choisit en premier", 11, FIN, "middle"))
    # vue de gauche, placée À DROITE
    p.append(f"<rect x='320' y='60' width='120' height='110' fill='#eef2f7' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(_txt(380, 115, "VUE DE GAUCHE", 12, TRAIT, "middle", True))
    p.append(_txt(380, 133, "dessinée à droite", 10, ALERTE, "middle"))
    # vue de dessus, placée EN DESSOUS
    p.append(f"<rect x='90' y='215' width='170' height='95' fill='#eef2f7' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(_txt(175, 258, "VUE DE DESSUS", 12, TRAIT, "middle", True))
    p.append(_txt(175, 276, "dessinée en dessous", 10, ALERTE, "middle"))
    # lignes d'alignement
    p.append(f"<line x1='60' y1='190' x2='470' y2='190' stroke='{AXE}' stroke-width='1' stroke-dasharray='6 4'/>")
    p.append(f"<line x1='290' y1='40' x2='290' y2='330' stroke='{AXE}' stroke-width='1' stroke-dasharray='6 4'/>")
    p.append(_txt(60, 45, "Les vues restent alignées : jamais de décalage", 11, AXE))
    # observateur
    p.append(f"<circle cx='545' cy='115' r='16' fill='none' stroke={chr(39)}{ARBRE}{chr(39)} stroke-width='2'/>")
    p.append(_txt(545, 120, "œil", 10, ARBRE, "middle"))
    p.append(f"<line x1='529' y1='115' x2='450' y2='115' stroke='{ARBRE}' stroke-width='2' marker-end='url(#fl)'/>")
    p.append("<defs><marker id='fl' markerWidth='9' markerHeight='9' refX='8' refY='4.5' orient='auto'>"
             f"<path d='M0,0 L9,4.5 L0,9 z' fill='{ARBRE}'/></marker></defs>")
    p.append(_txt(575, 150, "L'observateur regarde", 11, FIN))
    p.append(_txt(575, 166, "la pièce depuis la gauche,", 11, FIN))
    p.append(_txt(575, 182, "et la vue se dessine", 11, FIN))
    p.append(_txt(575, 198, "de l'autre côté.", 11, FIN, "start", True))
    p.append(_txt(575, 230, "C'est ça, la méthode", 11, FIN))
    p.append(_txt(575, 246, "européenne.", 11, TRAIT, "start", True))
    return _svg("".join(p), 760, 340)


# ===========================================================================
# 2. LES TYPES DE TRAITS
# ===========================================================================

def types_de_traits():
    lignes = [
        ("Continu fort", "ce que l'œil voit : les contours et les arêtes", TRAIT, 3, "none"),
        ("Interrompu fin", "ce qui est caché derrière la matière", TRAIT, 1.4, "9 5"),
        ("Mixte fin", "les axes : tout trou rond, tout arbre en a un", AXE, 1.4, "16 4 3 4"),
        ("Continu fin", "les cotes, les attaches, les hachures", FIN, 1, "none"),
    ]
    p = [_txt(40, 34, "Quatre traits, quatre significations. Il n'y en a pas d'autres à connaître pour démarrer.",
              13, FIN)]
    y = 78
    for nom, role, couleur, ep, tirets in lignes:
        dash = "" if tirets == "none" else f" stroke-dasharray='{tirets}'"
        p.append(f"<line x1='45' y1='{y}' x2='250' y2='{y}' stroke='{couleur}' stroke-width='{ep}'{dash}/>")
        p.append(_txt(270, y - 4, nom, 13, TRAIT, "start", True))
        p.append(_txt(270, y + 14, role, 12, FIN))
        y += 62
    p.append(f"<rect x='40' y='300' width='670' height='40' fill='#fff7ed' stroke='{ARBRE}' rx='6'/>")
    p.append(_txt(56, 325, "Règle simple : si deux traits tombent au même endroit, on garde le plus fort.",
                  12, TRAIT))
    return _svg("".join(p), 760, 360)


# ===========================================================================
# 3. POURQUOI ON COUPE UNE PIÈCE
# ===========================================================================

def pourquoi_couper():
    p = []
    # avant : plein de tirets
    p.append(_txt(40, 34, "AVANT — la pièce vue de l'extérieur", 13, TRAIT, "start", True))
    p.append(f"<rect x='55' y='55' width='230' height='150' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2.5'/>")
    for x in (110, 150, 190, 230):
        p.append(f"<line x1='{x}' y1='55' x2='{x}' y2='205' stroke='{TRAIT}' stroke-width='1.3' stroke-dasharray='8 5'/>")
    p.append(_txt(170, 235, "illisible : que des traits cachés", 12, ALERTE, "middle"))

    # flèche
    p.append(f"<line x1='310' y1='130' x2='390' y2='130' stroke='{FIN}' stroke-width='2' marker-end='url(#f2)'/>")
    p.append("<defs><marker id='f2' markerWidth='10' markerHeight='10' refX='9' refY='5' orient='auto'>"
             f"<path d='M0,0 L10,5 L0,10 z' fill='{FIN}'/></marker></defs>")
    p.append(_txt(350, 118, "on scie", 11, FIN, "middle"))

    # après : coupe hachurée
    p.append(_txt(420, 34, "APRÈS — la pièce coupée (COUPE A-A)", 13, TRAIT, "start", True))
    p.append(f"<rect x='435' y='55' width='230' height='150' fill='none' stroke='{TRAIT}' stroke-width='2.5'/>")
    # matière hachurée à gauche et à droite du trou central
    for x0 in range(440, 660, 12):
        p.append(f"<line x1='{x0}' y1='200' x2='{x0 + 45}' y2='55' stroke='{FIN}' stroke-width='0.9'/>")
    p.append(f"<rect x='510' y='55' width='80' height='150' fill='{FOND}' stroke='{TRAIT}' stroke-width='2.5'/>")
    p.append(_txt(550, 135, "le trou", 12, TRAIT, "middle"))
    p.append(_txt(550, 235, "clair : la matière est hachurée,", 12, OK, "middle"))
    p.append(_txt(550, 252, "le vide reste blanc", 12, OK, "middle"))

    p.append(f"<rect x='40' y='285' width='680' height='42' fill='#f0fdf4' stroke='{OK}' rx='6'/>")
    p.append(_txt(56, 305, "Couper sert à SUPPRIMER des traits cachés, jamais à en ajouter.", 12, TRAIT, "start", True))
    p.append(_txt(56, 321, "On hachure uniquement là où la scie a traversé de la matière.", 12, FIN))
    return _svg("".join(p), 760, 345)


# ===========================================================================
# 4. LA TOLÉRANCE : POURQUOI UNE COTE N'EST JAMAIS EXACTE
# ===========================================================================

def pourquoi_tolerance():
    p = [_txt(40, 32, "On demande 20 mm. Voilà ce qui sort vraiment de la machine :", 13, TRAIT, "start", True)]
    valeurs = [("19,98", 120), ("20,01", 210), ("19,99", 300), ("20,03", 390), ("20,00", 480)]
    for v, x in valeurs:
        p.append(f"<circle cx='{x}' cy='95' r='26' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
        p.append(_txt(x, 100, v, 12, TRAIT, "middle"))
    p.append(_txt(600, 100, "aucune n'est", 12, FIN))
    p.append(_txt(600, 116, "exactement 20", 12, ALERTE, "start", True))

    # zone acceptée
    p.append(f"<rect x='120' y='175' width='380' height='70' fill='#f0fdf4' stroke='{OK}' stroke-width='2' rx='6'/>")
    p.append(_txt(310, 200, "ZONE ACCEPTÉE : de 19,98 à 20,02", 14, OK, "middle", True))
    p.append(_txt(310, 226, "toute pièce qui tombe ici est bonne", 12, FIN, "middle"))
    p.append(f"<line x1='390' y1='95' x2='390' y2='170' stroke='{ALERTE}' stroke-width='1.5' stroke-dasharray='5 4'/>")
    p.append(_txt(560, 205, "20,03 est refusée", 12, ALERTE, "start", True))
    p.append(_txt(560, 222, "(hors de la zone)", 11, FIN))

    p.append(f"<rect x='40' y='280' width='680' height='60' fill='#fff7ed' stroke='{ARBRE}' rx='6'/>")
    p.append(_txt(56, 302, "La largeur de cette zone s'appelle l'INTERVALLE DE TOLÉRANCE (IT).", 12, TRAIT, "start", True))
    p.append(_txt(56, 324, "Ici IT = 20,02 − 19,98 = 0,04 mm. Plus la zone est étroite, plus la pièce coûte cher.", 12, FIN))
    return _svg("".join(p), 760, 355)


# ===========================================================================
# 5. JEU / INCERTAIN / SERRAGE — les trois natures d'ajustement
# ===========================================================================

def _cas_ajustement(x0, titre, y_arbre, couleur_cadre, legende, sous_legende):
    """Un des trois cas, dessine dans une colonne de 220 px."""
    p = []
    zero = 130                      # ligne zero (cote nominale)
    p.append(f"<rect x='{x0}' y='30' width='215' height='250' fill='#ffffff' stroke='{couleur_cadre}' "
             f"stroke-width='2' rx='8'/>")
    p.append(_txt(x0 + 107, 55, titre, 14, couleur_cadre, "middle", True))
    # ligne zero
    p.append(f"<line x1='{x0 + 15}' y1='{zero}' x2='{x0 + 200}' y2='{zero}' stroke='{FIN}' "
             f"stroke-width='1' stroke-dasharray='5 4'/>")
    p.append(_txt(x0 + 15, zero + 14, "cote nominale", 9, FIN))
    # zone alesage (lettre H : toujours au-dessus de la ligne zero)
    p.append(f"<rect x='{x0 + 35}' y='{zero - 42}' width='68' height='42' fill='{ALESAGE}' opacity='0.28' "
             f"stroke='{ALESAGE}' stroke-width='1.5'/>")
    p.append(_txt(x0 + 69, zero - 17, "trou", 11, ALESAGE, "middle", True))
    # zone arbre
    p.append(f"<rect x='{x0 + 118}' y='{y_arbre}' width='68' height='34' fill='{ARBRE}' opacity='0.32' "
             f"stroke='{ARBRE}' stroke-width='1.5'/>")
    p.append(_txt(x0 + 152, y_arbre + 22, "arbre", 11, ARBRE, "middle", True))
    p.append(_txt(x0 + 107, 236, legende, 11, TRAIT, "middle", True))
    p.append(_txt(x0 + 107, 256, sous_legende, 10, FIN, "middle"))
    return "".join(p)


def trois_ajustements():
    p = [_txt(40, 22, "Chaque rectangle est la fourchette dans laquelle la pièce peut sortir de la machine.",
              12, FIN)]
    p.append(_cas_ajustement(20, "JEU", 140, OK,
                             "L'arbre est toujours plus petit",
                             "ça tourne, ça coulisse (H7/g6)"))
    p.append(_cas_ajustement(268, "INCERTAIN", 112, ARBRE,
                             "Les deux zones se chevauchent",
                             "jeu ou serrage selon les pièces (H7/k6)"))
    p.append(_cas_ajustement(516, "SERRAGE", 84, ALERTE,
                             "L'arbre est toujours plus gros",
                             "il faut une presse (H7/p6)"))
    p.append(_txt(380, 305, "Zone bleue au-dessus de l'orange = du jeu.  Zone orange au-dessus de la bleue = du serrage.",
                  12, TRAIT, "middle", True))
    return _svg("".join(p), 760, 320)


# ===========================================================================
# 6. LIRE UNE ÉCRITURE H7/g6
# ===========================================================================

def lire_h7g6():
    """L'ecriture normalisee expliquee morceau par morceau, sans lignes qui se croisent."""
    p = []
    p.append(_txt(380, 62, "Ø30 H7 / g6", 40, TRAIT, "middle", True))
    reperes = [(250, "1", FIN), (360, "2", ALESAGE), (405, "3", ALESAGE),
               (492, "4", ARBRE), (535, "5", ARBRE)]
    for x, num, couleur in reperes:
        p.append(f"<line x1='{x}' y1='75' x2='{x}' y2='96' stroke='{couleur}' stroke-width='1.5'/>")
        p.append(f"<circle cx='{x}' cy='108' r='11' fill='{couleur}'/>")
        p.append(_txt(x, 112, num, 11, "#ffffff", "middle", True))

    lignes = [
        ("1", "30", "le diamètre voulu — c'est la cote commune aux deux pièces", FIN),
        ("2", "H", "la position du trou — H veut dire : le trou part exactement de 30", ALESAGE),
        ("3", "7", "la précision du trou — plus le chiffre est petit, plus c'est précis", ALESAGE),
        ("4", "g", "la position de l'arbre — g veut dire : un peu plus petit que 30", ARBRE),
        ("5", "6", "la précision de l'arbre — 6 est plus serré que 7", ARBRE),
    ]
    y = 165
    for num, morceau, texte, couleur in lignes:
        p.append(f"<circle cx='62' cy='{y - 4}' r='11' fill='{couleur}'/>")
        p.append(_txt(62, y, num, 11, "#ffffff", "middle", True))
        p.append(_txt(88, y, morceau, 15, couleur, "start", True))
        p.append(_txt(115, y, texte, 12, TRAIT))
        y += 38

    p.append(f"<rect x='40' y='348' width='680' height='46' fill='#eff6ff' stroke='{ALESAGE}' rx='6'/>")
    p.append(_txt(56, 368, "Majuscule = le trou (l'alésage).  Minuscule = l'arbre.", 12, TRAIT, "start", True))
    p.append(_txt(56, 386, "C'est la seule chose à ne jamais confondre.", 12, FIN))
    return _svg("".join(p), 760, 410)


# ===========================================================================
# 7. FLEXION : LA HAUTEUR COMPTE AU CUBE
# ===========================================================================

def flexion_hauteur():
    p = []
    p.append(_txt(40, 30, "Même quantité de matière, même matériau — seule l'orientation change :", 13, TRAIT, "start", True))
    # poutre à plat
    p.append(f"<rect x='70' y='105' width='230' height='26' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(_txt(185, 55, "posée à plat (h = 26)", 12, FIN, "middle"))
    p.append(f"<path d='M70,131 Q185,175 300,131' fill='none' stroke='{ALERTE}' stroke-width='2' stroke-dasharray='5 4'/>")
    p.append(_txt(185, 200, "elle plie beaucoup", 12, ALERTE, "middle", True))
    # poutre sur chant
    p.append(f"<rect x='470' y='60' width='26' height='115' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(_txt(575, 120, "posée sur chant", 12, FIN, "middle"))
    p.append(_txt(575, 138, "(h = 115)", 12, FIN, "middle"))
    p.append(f"<path d='M400,175 L470,175 M496,175 L620,175' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(_txt(510, 200, "elle plie 90 fois moins", 12, OK, "middle", True))
    # charges
    for x, base in ((185, 105), (483, 60)):
        p.append(f"<line x1='{x}' y1='{base - 40}' x2='{x}' y2='{base - 8}' stroke='{ARBRE}' stroke-width='2.5' marker-end='url(#f3)'/>")
    p.append("<defs><marker id='f3' markerWidth='9' markerHeight='9' refX='8' refY='4.5' orient='auto'>"
             f"<path d='M0,0 L9,4.5 L0,9 z' fill='{ARBRE}'/></marker></defs>")
    p.append(_txt(40, 250, "Pourquoi ? Parce que la résistance dépend de la hauteur AU CUBE.", 13, TRAIT, "start", True))
    p.append(_txt(40, 272, "Doubler la hauteur, c'est multiplier la résistance par 8 (2 × 2 × 2), sans ajouter de matière.", 12, FIN))
    p.append(_txt(40, 294, "C'est pour ça que les poutres de charpente sont hautes et fines, jamais larges et plates.", 12, FIN))
    return _svg("".join(p), 760, 315)


# ===========================================================================
# 8. RUGOSITÉ Ra : CE QU'ON TOUCHE AVEC L'ONGLE
# ===========================================================================

def rugosite_ra():
    p = [_txt(40, 30, "Une surface usinée n'est jamais lisse : vue de très près, c'est une montagne.", 13, TRAIT, "start", True)]
    import math as _m
    # profil rugueux
    pts = []
    for i in range(0, 481, 8):
        h = 12 * _m.sin(i / 14.0) + 5 * _m.sin(i / 5.0)
        pts.append(f"{60 + i},{130 - h:.1f}")
    p.append(f"<polyline points='{' '.join(pts)}' fill='none' stroke='{TRAIT}' stroke-width='1.8'/>")
    p.append(f"<line x1='60' y1='130' x2='540' y2='130' stroke='{ALESAGE}' stroke-width='1.5' stroke-dasharray='6 4'/>")
    p.append(_txt(548, 134, "ligne moyenne", 11, ALESAGE))
    p.append(f"<line x1='300' y1='112' x2='300' y2='130' stroke='{ARBRE}' stroke-width='2'/>")
    p.append(_txt(60, 70, "Ra = hauteur moyenne des bosses au-dessus de la ligne moyenne", 11, ARBRE, "start", True))

    niveaux = [("brut de fonderie", "Ra 12,5", "on sent nettement les aspérités", ALERTE),
               ("usinage courant", "Ra 3,2", "lisse au toucher, suffit pour un appui", TRAIT),
               ("finition", "Ra 1,6", "brillant, pour les pièces qui frottent", FIN),
               ("rectifié", "Ra 0,8", "obligatoire sous un roulement ou un joint", OK)]
    y = 190
    for nom, ra, usage, couleur in niveaux:
        p.append(f"<rect x='60' y='{y - 14}' width='84' height='22' fill='{couleur}' opacity='0.15' stroke='{couleur}' rx='4'/>")
        p.append(_txt(102, y + 2, ra, 12, couleur, "middle", True))
        p.append(_txt(158, y + 2, nom, 12, TRAIT, "start", True))
        p.append(_txt(300, y + 2, usage, 12, FIN))
        y += 34
    p.append(_txt(40, 330, "Demander Ra 0,8 partout, c'est tripler le prix de la pièce pour rien.", 12, ALERTE, "start", True))
    return _svg("".join(p), 760, 345)


# ===========================================================================
# 9. LES LIAISONS : CE QUI PEUT ENCORE BOUGER
# ===========================================================================

def liaisons_de_base():
    cas = [
        ("ENCASTREMENT", "0 mouvement", "les deux pièces sont soudées, vissées : plus rien ne bouge", 0),
        ("PIVOT", "1 rotation", "la porte sur ses gonds, l'arbre dans ses roulements", 1),
        ("GLISSIÈRE", "1 translation", "le tiroir, la table de fraiseuse", 2),
        ("PIVOT GLISSANT", "1 rotation + 1 translation", "la tige de vérin dans son guide", 3),
    ]
    p = [_txt(40, 30, "Nommer une liaison, c'est simplement compter ce qui peut encore bouger.", 13, TRAIT, "start", True)]
    y = 75
    for nom, ddl, exemple, i in cas:
        p.append(f"<rect x='45' y='{y}' width='95' height='46' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2' rx='4'/>")
        p.append(f"<rect x='140' y='{y + 8}' width='75' height='30' fill='#cbd5e1' stroke='{TRAIT}' stroke-width='2' rx='4'/>")
        if i == 1:
            p.append(f"<path d='M232,{y + 30} a 14,14 0 1,1 12,-8' fill='none' stroke='{ARBRE}' stroke-width='2.2' marker-end='url(#f4)'/>")
        if i in (2, 3):
            p.append(f"<line x1='228' y1='{y + 23}' x2='276' y2='{y + 23}' stroke='{ARBRE}' stroke-width='2.2' marker-end='url(#f4)'/>")
        if i == 3:
            p.append(f"<path d='M232,{y + 46} a 12,12 0 1,1 10,-7' fill='none' stroke='{ARBRE}' stroke-width='2' marker-end='url(#f4)'/>")
        if i == 0:
            p.append(f"<line x1='232' y1='{y + 14}' x2='262' y2='{y + 34}' stroke='{ALERTE}' stroke-width='2.2'/>")
            p.append(f"<line x1='262' y1='{y + 14}' x2='232' y2='{y + 34}' stroke='{ALERTE}' stroke-width='2.2'/>")
        p.append(_txt(310, y + 20, nom, 13, TRAIT, "start", True))
        p.append(_txt(310, y + 38, f"{ddl} — {exemple}", 11, FIN))
        y += 66
    p.append("<defs><marker id='f4' markerWidth='8' markerHeight='8' refX='7' refY='4' orient='auto'>"
             f"<path d='M0,0 L8,4 L0,8 z' fill='{ARBRE}'/></marker></defs>")
    return _svg("".join(p), 760, 350)


# ===========================================================================
# 10. ENGRENAGE : LE MODULE
# ===========================================================================

def engrenage_module():
    p = [_txt(40, 30, "Deux roues ne peuvent tourner ensemble que si leurs dents ont la même taille.", 13, TRAIT, "start", True)]
    p.append(f"<circle cx='230' cy='185' r='95' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<circle cx='230' cy='185' r='80' fill='none' stroke='{AXE}' stroke-width='1.4' stroke-dasharray='8 4'/>")
    p.append(f"<circle cx='450' cy='185' r='60' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<circle cx='450' cy='185' r='45' fill='none' stroke='{AXE}' stroke-width='1.4' stroke-dasharray='8 4'/>")
    p.append(_txt(230, 155, "Z1 = 32 dents", 12, TRAIT, "middle", True))
    p.append(_txt(450, 155, "Z2 = 18", 12, TRAIT, "middle", True))
    p.append(_txt(230, 300, "d1 = m × Z1", 12, AXE, "middle"))
    p.append(_txt(450, 265, "d2 = m × Z2", 12, AXE, "middle"))
    p.append(f"<line x1='230' y1='185' x2='450' y2='185' stroke='{ARBRE}' stroke-width='1.6'/>")
    p.append(_txt(340, 205, "entraxe a", 11, ARBRE, "middle", True))
    p.append(f"<rect x='560' y='95' width='170' height='120' fill='#eff6ff' stroke='{ALESAGE}' rx='6'/>")
    p.append(_txt(575, 120, "Le module m,", 12, TRAIT, "start", True))
    p.append(_txt(575, 138, "c'est la taille d'une", 11, FIN))
    p.append(_txt(575, 154, "dent. Il est normalisé :", 11, FIN))
    p.append(_txt(575, 174, "1 — 1,5 — 2 — 2,5 — 3…", 11, ALESAGE, "start", True))
    p.append(_txt(575, 198, "Même m obligatoire !", 11, ALERTE, "start", True))
    p.append(_txt(40, 335, "La petite roue tourne plus vite que la grande : c'est le rapport de transmission.", 12, FIN))
    return _svg("".join(p), 760, 350)


# ===========================================================================
# REGISTRE DES FIGURES
# ===========================================================================

FIGURES = {
    "projection_europeenne": ("Où se placent les vues", projection_europeenne),
    "types_de_traits": ("Les quatre traits du dessin technique", types_de_traits),
    "pourquoi_couper": ("Pourquoi on coupe une pièce", pourquoi_couper),
    "pourquoi_tolerance": ("Pourquoi une cote n'est jamais exacte", pourquoi_tolerance),
    "trois_ajustements": ("Jeu, incertain, serrage", trois_ajustements),
    "lire_h7g6": ("Décoder l'écriture Ø30 H7/g6", lire_h7g6),
    "flexion_hauteur": ("En flexion, la hauteur compte au cube", flexion_hauteur),
    "rugosite_ra": ("La rugosité Ra en images", rugosite_ra),
    "liaisons_de_base": ("Les liaisons : compter ce qui bouge", liaisons_de_base),
    "engrenage_module": ("Le module d'un engrenage", engrenage_module),
}


def html(cle):
    """Renvoie la figure prête à être insérée dans st.markdown(..., unsafe_allow_html=True).

    Le SVG est encodé en image pour être affiché de façon fiable par Streamlit.
    """
    if cle not in FIGURES:
        return f"<i>Figure inconnue : {cle}</i>"
    titre, fonction = FIGURES[cle]
    svg = fonction()
    b64 = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    return (f"<figure style='margin:18px 0'>"
            f"<img src='data:image/svg+xml;base64,{b64}' style='width:100%;max-width:760px;'/>"
            f"<figcaption style='font-size:0.85em;color:#64748b;margin-top:6px'>{titre}</figcaption>"
            f"</figure>")
