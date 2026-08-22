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
# 11. LA BÊTE À CORNES — cadrer le besoin
# ===========================================================================

def bete_a_cornes():
    p = [_txt(380, 28, "Trois questions, posées AVANT de dessiner quoi que ce soit", 13, FIN, "middle")]
    # les deux cornes
    p.append(f"<rect x='90' y='60' width='220' height='58' rx='8' fill='#dbeafe' stroke='{ALESAGE}' stroke-width='2'/>")
    p.append(_txt(200, 84, "À QUI rend-il service ?", 12, ALESAGE, "middle", True))
    p.append(_txt(200, 104, "l'opérateur de la machine", 11, TRAIT, "middle"))
    p.append(f"<rect x='450' y='60' width='220' height='58' rx='8' fill='#ffedd5' stroke='{ARBRE}' stroke-width='2'/>")
    p.append(_txt(560, 84, "SUR QUOI agit-il ?", 12, ARBRE, "middle", True))
    p.append(_txt(560, 104, "la pièce à usiner", 11, TRAIT, "middle"))
    # le produit
    p.append(f"<rect x='280' y='170' width='200' height='62' rx='8' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2.5'/>")
    p.append(_txt(380, 197, "LE PRODUIT", 13, TRAIT, "middle", True))
    p.append(_txt(380, 217, "l'étau de bridage", 11, FIN, "middle"))
    p.append(f"<line x1='200' y1='118' x2='330' y2='170' stroke='{ALESAGE}' stroke-width='2'/>")
    p.append(f"<line x1='560' y1='118' x2='430' y2='170' stroke='{ARBRE}' stroke-width='2'/>")
    # le but
    p.append(f"<rect x='230' y='275' width='300' height='58' rx='8' fill='#dcfce7' stroke='{OK}' stroke-width='2'/>")
    p.append(_txt(380, 299, "DANS QUEL BUT ?", 12, OK, "middle", True))
    p.append(_txt(380, 319, "immobiliser la pièce pendant l'usinage", 11, TRAIT, "middle"))
    p.append(f"<line x1='380' y1='232' x2='380' y2='275' stroke='{OK}' stroke-width='2'/>")
    p.append(_txt(380, 362, "Cette dernière phrase est la fonction globale : c'est elle qu'on écrira en tête du cahier des charges.",
                  12, TRAIT, "middle", True))
    return _svg("".join(p), 760, 380)


# ===========================================================================
# 12. LE DIAGRAMME PIEUVRE — FP et FC
# ===========================================================================

def diagramme_pieuvre():
    import math as _m
    p = [_txt(380, 26, "Le produit au centre, tout ce qui l'entoure autour", 13, FIN, "middle")]
    cx, cy, r = 380, 225, 62
    elements = [("Opérateur", 180), ("Pièce", 0), ("Table machine", 62),
                ("Copeaux, huile", 118), ("Budget", 242), ("Norme sécurité", 298)]
    pos = {}
    for nom, angle in elements:
        a = _m.radians(angle)
        x, y = cx + 255 * _m.cos(a), cy + 155 * _m.sin(a)
        pos[nom] = (x, y)
        p.append(f"<rect x='{x - 62}' y='{y - 17}' width='124' height='34' rx='17' fill='#f1f5f9' "
                 f"stroke='{FIN}' stroke-width='1.5'/>")
        p.append(_txt(x, y + 5, nom, 11, TRAIT, "middle"))
    # FP : traverse le produit et relie deux elements
    x1, y1 = pos["Opérateur"]; x2, y2 = pos["Pièce"]
    p.append(f"<line x1='{x1 + 62}' y1='{y1}' x2='{x2 - 62}' y2='{y2}' stroke='{OK}' stroke-width='2.5'/>")
    p.append(_txt(cx, cy - 80, "FP — serrer la pièce", 12, OK, "middle", True))
    # FC : relie le produit a un seul element
    for nom, couleur in (("Table machine", ARBRE), ("Copeaux, huile", ARBRE), ("Budget", ARBRE)):
        x, y = pos[nom]
        p.append(f"<line x1='{cx}' y1='{cy}' x2='{x}' y2='{y}' stroke='{couleur}' stroke-width='1.6' stroke-dasharray='6 4'/>")
    p.append(f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2.5'/>")
    p.append(_txt(cx, cy + 5, "L'ÉTAU", 13, TRAIT, "middle", True))
    p.append(f"<rect x='40' y='400' width='680' height='46' fill='#f8fafc' stroke='{FIN}' rx='6'/>")
    p.append(_txt(56, 420, "Trait plein qui TRAVERSE le produit = fonction principale (FP) : la raison d'être.", 12, OK, "start", True))
    p.append(_txt(56, 438, "Trait pointillé qui s'arrête au produit = fonction contrainte (FC) : une obligation subie.", 12, ARBRE, "start", True))
    return _svg("".join(p), 760, 460)


# ===========================================================================
# 13. LE DIAGRAMME FAST — de la fonction au composant
# ===========================================================================

def diagramme_fast():
    p = [_txt(40, 26, "On lit de gauche à droite : à chaque colonne, on répond à « comment ? »", 13, FIN)]
    colonnes = [
        (55, "Fonction de service", ["Serrer la pièce", "sur la table"], ALESAGE),
        (255, "Fonctions techniques", ["Créer un effort", "Guider le mors", "Bloquer en position"], TRAIT),
        (490, "Solutions techniques", ["Vis + écrou", "Glissière queue d'aronde", "Écrou de blocage"], ARBRE),
    ]
    for x, titre, items, couleur in colonnes:
        p.append(_txt(x + 100, 60, titre, 12, couleur, "middle", True))
        y = 90
        for it in items:
            p.append(f"<rect x='{x}' y='{y}' width='200' height='46' rx='6' fill='#f8fafc' stroke='{couleur}' stroke-width='1.8'/>")
            p.append(_txt(x + 100, y + 28, it, 11, TRAIT, "middle"))
            y += 66
    for y in (113, 179, 245):
        p.append(f"<line x1='455' y1='{y}' x2='490' y2='{y}' stroke='{FIN}' stroke-width='1.2'/>")
        p.append(f"<line x1='220' y1='{y}' x2='255' y2='{y}' stroke='{FIN}' stroke-width='1.2'/>")
    p.append(f"<line x1='220' y1='113' x2='220' y2='245' stroke='{FIN}' stroke-width='1.2'/>")
    p.append(f"<line x1='255' y1='113' x2='255' y2='113' stroke='{FIN}' stroke-width='1.2'/>")
    p.append(f"<line x1='255' y1='113' x2='255' y2='245' stroke='{FIN}' stroke-width='1.2'/>")
    p.append(f"<line x1='255' y1='113' x2='255' y2='245' stroke='{FIN}' stroke-width='1.2'/>")
    p.append(f"<path d='M40,300 L720,300' stroke='{FIN}' stroke-width='1' stroke-dasharray='5 4'/>")
    p.append(f"<line x1='120' y1='320' x2='40' y2='320' stroke='{ALESAGE}' stroke-width='2' marker-end='url(#f5)'/>")
    p.append("<defs><marker id='f5' markerWidth='9' markerHeight='9' refX='8' refY='4.5' orient='auto'>"
             f"<path d='M0,0 L9,4.5 L0,9 z' fill='{ALESAGE}'/></marker></defs>")
    p.append(_txt(130, 324, "vers la gauche : POURQUOI ?", 11, ALESAGE, "start", True))
    p.append(f"<line x1='600' y1='320' x2='690' y2='320' stroke='{ARBRE}' stroke-width='2' marker-end='url(#f6)'/>")
    p.append("<defs><marker id='f6' markerWidth='9' markerHeight='9' refX='8' refY='4.5' orient='auto'>"
             f"<path d='M0,0 L9,4.5 L0,9 z' fill='{ARBRE}'/></marker></defs>")
    p.append(_txt(590, 324, "vers la droite : COMMENT ?", 11, ARBRE, "end", True))
    p.append(_txt(40, 358, "Le nom d'un vrai composant n'apparaît QU'À LA DERNIÈRE COLONNE. Jamais avant.", 12, TRAIT, "start", True))
    return _svg("".join(p), 760, 375)


# ===========================================================================
# 14. LES ÉLÉMENTS D'UNE COTE
# ===========================================================================

def elements_cotation():
    p = [_txt(40, 28, "Une cote, ce sont quatre éléments — toujours les mêmes :", 13, TRAIT, "start", True)]
    p.append(f"<rect x='150' y='95' width='330' height='120' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2.5'/>")
    # lignes d'attache
    p.append(f"<line x1='150' y1='90' x2='150' y2='55' stroke='{FIN}' stroke-width='1'/>")
    p.append(f"<line x1='480' y1='90' x2='480' y2='55' stroke='{FIN}' stroke-width='1'/>")
    # ligne de cote avec fleches
    p.append(f"<line x1='150' y1='68' x2='480' y2='68' stroke='{FIN}' stroke-width='1.2' "
             f"marker-start='url(#g1)' marker-end='url(#g2)'/>")
    p.append("<defs>"
             f"<marker id='g1' markerWidth='10' markerHeight='8' refX='1' refY='4' orient='auto'><path d='M10,0 L0,4 L10,8 z' fill='{FIN}'/></marker>"
             f"<marker id='g2' markerWidth='10' markerHeight='8' refX='9' refY='4' orient='auto'><path d='M0,0 L10,4 L0,8 z' fill='{FIN}'/></marker>"
             "</defs>")
    p.append(f"<rect x='288' y='52' width='56' height='22' fill='{FOND}'/>")
    p.append(_txt(316, 68, "120", 15, TRAIT, "middle", True))
    # reperes
    reperes = [
        (150, 78, "1", "ligne d'attache", 545, 70),
        (400, 68, "2", "ligne de cote", 545, 108),
        (316, 62, "3", "la valeur réelle (jamais mesurée à la règle)", 545, 146),
        (480, 68, "4", "flèches d'extrémité", 545, 184),
    ]
    y_leg = 70
    for i, (x, y, num, texte, lx, ly) in enumerate(reperes):
        p.append(f"<circle cx='{lx - 18}' cy='{ly - 4}' r='10' fill='{AXE}'/>")
        p.append(_txt(lx - 18, ly, num, 10, "#ffffff", "middle", True))
        p.append(_txt(lx, ly, texte, 11, TRAIT))
    p.append(f"<rect x='40' y='250' width='680' height='88' fill='#f0fdf4' stroke='{OK}' rx='6'/>")
    p.append(_txt(56, 272, "Trois règles qui suffisent en première année :", 12, TRAIT, "start", True))
    p.append(_txt(56, 294, "• une dimension n'est cotée QU'UNE FOIS sur tout le plan ;", 11, FIN))
    p.append(_txt(56, 312, "• on ne cote jamais une dimension qui se déduit des autres ;", 11, FIN))
    p.append(_txt(56, 330, "• les cotes se lisent du bas ou de la droite de la feuille, jamais à l'envers.", 11, FIN))
    return _svg("".join(p), 760, 350)


# ===========================================================================
# 15. LETTRE ET CHIFFRE : POSITION ET LARGEUR DE LA ZONE
# ===========================================================================

def lettres_et_grades():
    p = [_txt(40, 26, "La lettre dit OÙ se place la zone. Le chiffre dit sa LARGEUR.", 13, TRAIT, "start", True)]
    zero = 150
    p.append(f"<line x1='60' y1='{zero}' x2='700' y2='{zero}' stroke='{FIN}' stroke-width='1.2' stroke-dasharray='6 4'/>")
    p.append(_txt(62, zero + 34, "ligne zéro = cote nominale (par ex. Ø30)", 10, FIN))
    # arbres : positions relatives
    arbres = [("d", 95, -62, "grand jeu"), ("f", 185, -38, "jeu franc"),
              ("g", 275, -22, "petit jeu"), ("h", 365, -4, "jeu nul"),
              ("k", 455, 8, "léger serrage"), ("p", 545, 30, "serrage")]
    for lettre, x, dec, role in arbres:
        y = zero + dec
        p.append(f"<rect x='{x - 26}' y='{y}' width='52' height='22' fill='{ARBRE}' opacity='0.35' "
                 f"stroke='{ARBRE}' stroke-width='1.4'/>")
        p.append(_txt(x, y + 16, lettre, 12, ARBRE, "middle", True))
        p.append(_txt(x, 258, role, 9, FIN, "middle"))
    p.append(_txt(640, zero - 30, "l'arbre grossit", 11, ARBRE, "middle", True))
    p.append(f"<line x1='95' y1='240' x2='585' y2='240' stroke='{ARBRE}' stroke-width='1.6' marker-end='url(#h1)'/>")
    p.append("<defs><marker id='h1' markerWidth='9' markerHeight='9' refX='8' refY='4.5' orient='auto'>"
             f"<path d='M0,0 L9,4.5 L0,9 z' fill='{ARBRE}'/></marker></defs>")
    # alesage H, toujours au-dessus
    p.append(f"<rect x='{365 - 26}' y='{zero - 52}' width='52' height='30' fill='{ALESAGE}' opacity='0.30' "
             f"stroke='{ALESAGE}' stroke-width='1.4'/>")
    p.append(_txt(365, zero - 32, "H", 12, ALESAGE, "middle", True))
    p.append(_txt(365, zero - 62, "l'alésage H part toujours de la ligne zéro", 10, ALESAGE, "middle"))
    # grades
    p.append(f"<rect x='40' y='285' width='680' height='72' fill='#eff6ff' stroke='{ALESAGE}' rx='6'/>")
    p.append(_txt(56, 307, "Et le chiffre ? Il fixe la largeur de la zone, pour un Ø30 :", 12, TRAIT, "start", True))
    p.append(_txt(56, 329, "IT6 = 13 µm (rectifié, cher)   ·   IT7 = 21 µm (usinage soigné)   ·   IT8 = 33 µm", 11, FIN))
    p.append(_txt(56, 347, "IT11 = 130 µm (usinage courant)   ·   IT13 = 330 µm (pièce brute)", 11, FIN))
    return _svg("".join(p), 760, 370)


# ===========================================================================
# 16. UNE PIÈCE AUX BONNES COTES QUI NE MARCHE PAS
# ===========================================================================

def defaut_geometrique():
    p = [_txt(40, 28, "Les deux arbres mesurent 30 mm partout au pied à coulisse :", 13, TRAIT, "start", True)]
    # arbre droit
    p.append(f"<rect x='70' y='90' width='250' height='44' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(_txt(195, 75, "arbre droit", 12, OK, "middle", True))
    p.append(_txt(195, 160, "il entre dans son alésage", 11, OK, "middle"))
    # arbre banane
    p.append(f"<path d='M440,105 Q565,55 690,105 L690,140 Q565,90 440,140 Z' fill='#e2e8f0' "
             f"stroke='{TRAIT}' stroke-width='2'/>")
    p.append(_txt(565, 75, "arbre cintré (banane)", 12, ALERTE, "middle", True))
    p.append(_txt(565, 175, "il n'entre pas", 11, ALERTE, "middle", True))
    # mesures
    for x in (110, 195, 280):
        p.append(f"<line x1='{x}' y1='90' x2='{x}' y2='134' stroke='{AXE}' stroke-width='1.2'/>")
        p.append(_txt(x, 148, "30", 9, AXE, "middle"))
    for x, y1, y2 in ((480, 96, 131), (565, 72, 107), (650, 96, 131)):
        p.append(f"<line x1='{x}' y1='{y1}' x2='{x}' y2='{y2}' stroke='{AXE}' stroke-width='1.2'/>")
        p.append(_txt(x, y2 + 14, "30", 9, AXE, "middle"))
    p.append(f"<rect x='40' y='205' width='680' height='86' fill='#fff7ed' stroke='{ARBRE}' rx='6'/>")
    p.append(_txt(56, 228, "La cote dimensionnelle ne dit rien sur la FORME ni sur la POSITION.", 12, TRAIT, "start", True))
    p.append(_txt(56, 250, "Il faut donc un second langage : les tolérances géométriques.", 12, FIN))
    p.append(_txt(56, 274, "Ici, on ajouterait une exigence de rectitude ou de cylindricité sur l'arbre.", 11, ARBRE))
    return _svg("".join(p), 760, 305)


# ===========================================================================
# 17. LIRE UN CADRE DE TOLÉRANCE GÉOMÉTRIQUE
# ===========================================================================

def cadre_tolerance():
    p = [_txt(40, 28, "Un cadre se lit toujours dans le même ordre, de gauche à droite :", 13, TRAIT, "start", True)]
    x0, y0 = 210, 70
    largeurs = [58, 92, 52]
    etiquettes = ["⊥", "Ø0,03", "A"]
    x = x0
    for i, (w, e) in enumerate(zip(largeurs, etiquettes)):
        p.append(f"<rect x='{x}' y='{y0}' width='{w}' height='46' fill='#ffffff' stroke='{TRAIT}' stroke-width='2'/>")
        p.append(_txt(x + w / 2, y0 + 31, e, 17, TRAIT, "middle", True))
        x += w
    legendes = [
        (x0 + 29, "1", "le défaut visé : ici la perpendicularité", ALESAGE),
        (x0 + 104, "2", "la taille de la zone : 0,03 mm, et Ø = zone cylindrique", ARBRE),
        (x0 + 176, "3", "par rapport à quoi : la surface de référence A", OK),
    ]
    y = 165
    for x, num, texte, couleur in legendes:
        p.append(f"<line x1='{x}' y1='{y0 + 46}' x2='{x}' y2='{y - 15}' stroke='{couleur}' stroke-width='1.4' opacity='0.55'/>")
        p.append(f"<circle cx='{x}' cy='{y - 4}' r='11' fill='{couleur}'/>")
        p.append(_txt(x, y, num, 11, "#ffffff", "middle", True))
        p.append(_txt(x + 20, y, texte, 12, TRAIT))
        y += 42
    p.append(f"<rect x='40' y='295' width='680' height='72' fill='#f0fdf4' stroke='{OK}' rx='6'/>")
    p.append(_txt(56, 318, "Traduction en français : « l'axe de ce perçage doit rester dans un cylindre de", 12, TRAIT, "start", True))
    p.append(_txt(56, 338, "0,03 mm de diamètre, perpendiculaire à la face A. »", 12, TRAIT, "start", True))
    p.append(_txt(56, 358, "Les défauts de FORME (planéité, rectitude, cylindricité) n'ont pas de référence.", 11, FIN))
    return _svg("".join(p), 760, 380)


# ===========================================================================
# 18. LA CHAÎNE DE COTES
# ===========================================================================

def chaine_de_cotes():
    p = [_txt(40, 26, "Le jeu Ja n'appartient à aucune pièce : il dépend des trois à la fois.", 13, TRAIT, "start", True)]
    # carter
    p.append(f"<rect x='90' y='70' width='30' height='150' fill='#cbd5e1' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<rect x='560' y='70' width='30' height='150' fill='#cbd5e1' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<rect x='90' y='190' width='500' height='30' fill='#cbd5e1' stroke='{TRAIT}' stroke-width='2'/>")
    # roue
    p.append(f"<rect x='210' y='95' width='230' height='95' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(_txt(325, 148, "la roue (B)", 12, TRAIT, "middle", True))
    # couvercle
    p.append(f"<rect x='470' y='95' width='90' height='95' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(_txt(515, 148, "couvercle", 11, TRAIT, "middle", True))
    p.append(_txt(515, 165, "(C)", 11, TRAIT, "middle"))
    # jeu
    p.append(f"<rect x='440' y='95' width='30' height='95' fill='{ALERTE}' opacity='0.25' stroke='{ALERTE}' stroke-width='1.5'/>")
    p.append(_txt(455, 80, "Ja", 13, ALERTE, "middle", True))
    # cotes
    p.append(f"<line x1='120' y1='250' x2='560' y2='250' stroke='{ALESAGE}' stroke-width='1.5'/>")
    p.append(_txt(340, 268, "A = 60 (le carter)", 12, ALESAGE, "middle", True))
    p.append(f"<line x1='210' y1='290' x2='440' y2='290' stroke='{ARBRE}' stroke-width='1.5'/>")
    p.append(_txt(325, 308, "B = 40 (la roue)", 12, ARBRE, "middle", True))
    p.append(f"<line x1='470' y1='290' x2='560' y2='290' stroke='{ARBRE}' stroke-width='1.5'/>")
    p.append(_txt(515, 308, "C = 19,7", 11, ARBRE, "middle", True))
    p.append(f"<rect x='40' y='330' width='680' height='66' fill='#eff6ff' stroke='{ALESAGE}' rx='6'/>")
    p.append(_txt(56, 353, "Ja = A − B − C = 60 − 40 − 19,7 = 0,3 mm", 13, TRAIT, "start", True))
    p.append(_txt(56, 377, "ITja = ITa + ITb + ITc — les tolérances s'ADDITIONNENT toujours, jamais ne se compensent.",
                  12, ALERTE, "start", True))
    return _svg("".join(p), 760, 410)


# ===========================================================================
# 19. L'ESSAI DE TRACTION : D'OÙ VIENNENT Re ET Rm
# ===========================================================================

def courbe_traction():
    p = [_txt(40, 26, "On tire sur une éprouvette jusqu'à la rupture, et on enregistre :", 13, TRAIT, "start", True)]
    ox, oy = 90, 300
    p.append(f"<line x1='{ox}' y1='{oy}' x2='620' y2='{oy}' stroke='{TRAIT}' stroke-width='1.6'/>")
    p.append(f"<line x1='{ox}' y1='{oy}' x2='{ox}' y2='60' stroke='{TRAIT}' stroke-width='1.6'/>")
    p.append(_txt(360, 335, "allongement de l'éprouvette", 11, FIN, "middle"))
    p.append(f"<text x='30' y='180' {_POLICE} font-size='11' fill='{FIN}' transform='rotate(-90 30,180)'>contrainte (MPa)</text>")
    # partie elastique puis plastique
    p.append(f"<path d='M{ox},{oy} L250,150' fill='none' stroke='{ALESAGE}' stroke-width='2.6'/>")
    p.append(f"<path d='M250,150 Q330,95 430,90 Q510,88 560,130' fill='none' stroke='{ARBRE}' stroke-width='2.6'/>")
    p.append(f"<circle cx='560' cy='130' r='5' fill='{ALERTE}'/>")
    # reperes Re et Rm
    p.append(f"<line x1='{ox}' y1='150' x2='250' y2='150' stroke='{ALESAGE}' stroke-width='1' stroke-dasharray='5 4'/>")
    p.append(_txt(ox - 8, 154, "Re", 13, ALESAGE, "end", True))
    p.append(f"<line x1='{ox}' y1='90' x2='430' y2='90' stroke='{ARBRE}' stroke-width='1' stroke-dasharray='5 4'/>")
    p.append(_txt(ox - 8, 94, "Rm", 13, ARBRE, "end", True))
    p.append(_txt(575, 128, "rupture", 11, ALERTE, "start", True))
    # zones
    p.append(_txt(165, 235, "ZONE ÉLASTIQUE", 11, ALESAGE, "middle", True))
    p.append(_txt(165, 252, "la pièce revient", 10, FIN, "middle"))
    p.append(_txt(165, 267, "à sa forme initiale", 10, FIN, "middle"))
    p.append(_txt(400, 235, "ZONE PLASTIQUE", 11, ARBRE, "middle", True))
    p.append(_txt(400, 252, "la pièce reste déformée :", 10, FIN, "middle"))
    p.append(_txt(400, 267, "elle est bonne à jeter", 10, FIN, "middle"))
    p.append(f"<rect x='640' y='90' width='100' height='120' fill='#eff6ff' stroke='{ALESAGE}' rx='6'/>")
    p.append(_txt(690, 115, "La pente", 11, TRAIT, "middle", True))
    p.append(_txt(690, 133, "de la droite,", 10, FIN, "middle"))
    p.append(_txt(690, 151, "c'est E :", 10, FIN, "middle"))
    p.append(_txt(690, 172, "la RIGIDITÉ", 11, ALESAGE, "middle", True))
    p.append(_txt(690, 194, "du matériau", 10, FIN, "middle"))
    p.append(_txt(40, 362, "On dimensionne TOUJOURS dans la zone élastique : Re est la limite à ne pas franchir.",
                  12, TRAIT, "start", True))
    return _svg("".join(p), 760, 380)


# ===========================================================================
# 20. RÉSISTANCE ET RIGIDITÉ SONT DEUX CHOSES DIFFÉRENTES
# ===========================================================================

def resistance_vs_rigidite():
    p = [_txt(40, 28, "Deux propriétés que tout le monde confond :", 13, TRAIT, "start", True)]
    donnees = [("Acier S235", 235, 210), ("Acier 42CrMo4 traité", 750, 210),
               ("Aluminium 6060", 160, 70), ("Polymère POM", 65, 3)]
    y = 70
    for nom, re_, e in donnees:
        p.append(_txt(48, y + 16, nom, 12, TRAIT, "start", True))
        p.append(f"<rect x='250' y='{y}' width='{re_ * 0.22:.0f}' height='22' fill='{ARBRE}' opacity='0.75' rx='3'/>")
        p.append(_txt(250 + re_ * 0.22 + 8, y + 17, f"Re = {re_} MPa", 11, ARBRE))
        p.append(f"<rect x='250' y='{y + 26}' width='{e * 0.78:.0f}' height='22' fill='{ALESAGE}' opacity='0.75' rx='3'/>")
        p.append(_txt(250 + e * 0.78 + 8, y + 43, f"E = {e} GPa", 11, ALESAGE))
        y += 72
    p.append(f"<rect x='40' y='360' width='680' height='86' fill='#fff7ed' stroke='{ARBRE}' rx='6'/>")
    p.append(_txt(56, 383, "Re (orange) = à partir de quand la pièce se déforme DÉFINITIVEMENT. Le traitement", 12, TRAIT, "start", True))
    p.append(_txt(56, 401, "thermique le multiplie par trois.", 12, TRAIT))
    p.append(_txt(56, 425, "E (bleu) = à quel point elle plie sous charge. Il ne change PAS avec la nuance :", 12, TRAIT, "start", True))
    p.append(_txt(56, 441, "tous les aciers ont E = 210 GPa. Pour raidir, il faut changer la forme, pas l'acier.", 11, FIN))
    return _svg("".join(p), 760, 460)


# ===========================================================================
# 21. DÉCODER UNE DÉSIGNATION
# ===========================================================================

def decoder_designation():
    p = []
    exemples = [
        ("S235", [("S", "acier de structure", ALESAGE), ("235", "limite élastique Re = 235 MPa", ARBRE)],
         "soudable, bon marché : charpente, tôlerie"),
        ("C45", [("C", "acier non allié", ALESAGE), ("45", "0,45 % de carbone", ARBRE)],
         "trempable : arbres, axes, pignons"),
        ("42CrMo4", [("42", "0,42 % de carbone", ARBRE), ("CrMo", "chrome + molybdène", ALESAGE),
                     ("4", "÷ 4 → ≈ 1 % de chrome", OK)],
         "haute résistance : arbres très chargés"),
        ("X5CrNi18-10", [("X", "fortement allié (≥ 5 %)", ALESAGE), ("5", "0,05 % de carbone", ARBRE),
                         ("18-10", "18 % Cr, 10 % Ni", OK)],
         "inox : agroalimentaire, milieu humide"),
    ]
    y = 46
    for nom, morceaux, usage in exemples:
        p.append(f"<rect x='40' y='{y - 24}' width='680' height='84' fill='#ffffff' stroke='{FIN}' rx='6'/>")
        p.append(_txt(58, y + 4, nom, 20, TRAIT, "start", True))
        x = 195
        for texte, sens, couleur in morceaux:
            p.append(f"<rect x='{x}' y='{y - 16}' width='{max(58, len(texte) * 11)}' height='26' fill='{couleur}' "
                     f"opacity='0.18' stroke='{couleur}' stroke-width='1.2' rx='4'/>")
            p.append(_txt(x + max(58, len(texte) * 11) / 2, y + 3, texte, 12, couleur, "middle", True))
            p.append(_txt(x, y + 30, sens, 10, FIN))
            x += max(58, len(texte) * 11) + 130
        p.append(_txt(58, y + 46, usage, 11, FIN))
        y += 104
    return _svg("".join(p), 760, y - 40)


# ===========================================================================
# 22. CÉMENTATION : PEAU DURE, CŒUR TENACE
# ===========================================================================

def peau_dure_coeur_tenace():
    p = [_txt(40, 28, "Une dent de pignon doit être dure en surface (usure) et tenace à cœur (chocs).",
              13, TRAIT, "start", True)]
    # dent trempee a coeur
    p.append(_txt(190, 70, "Trempée dans la masse", 12, ALERTE, "middle", True))
    p.append(f"<path d='M120,190 L150,110 L230,110 L260,190 Z' fill='#fecaca' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(_txt(190, 160, "dure partout", 11, TRAIT, "middle"))
    p.append(f"<path d='M150,110 L165,132' stroke='{ALERTE}' stroke-width='2.5'/>")
    p.append(_txt(190, 215, "dure = fragile :", 11, ALERTE, "middle", True))
    p.append(_txt(190, 232, "la dent casse net au premier choc", 10, FIN, "middle"))
    # dent cementee
    p.append(_txt(540, 70, "Cémentée puis trempée", 12, OK, "middle", True))
    p.append(f"<path d='M470,190 L500,110 L580,110 L610,190 Z' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<path d='M470,190 L500,110 L580,110 L610,190' fill='none' stroke='{OK}' stroke-width='7' opacity='0.55'/>")
    p.append(_txt(540, 155, "cœur tenace", 11, TRAIT, "middle"))
    p.append(_txt(645, 120, "peau dure", 11, OK, "start", True))
    p.append(_txt(645, 137, "0,5 à 1,5 mm", 10, FIN, "start"))
    p.append(_txt(540, 215, "elle résiste à l'usure ET aux chocs", 11, OK, "middle", True))
    p.append(f"<rect x='40' y='255' width='680' height='72' fill='#f0fdf4' stroke='{OK}' rx='6'/>")
    p.append(_txt(56, 278, "Principe : on enrichit seulement la peau en carbone (cémentation), puis on trempe.", 12, TRAIT, "start", True))
    p.append(_txt(56, 298, "Le cœur, resté pauvre en carbone, ne durcit pas : il garde sa ténacité.", 12, FIN))
    p.append(_txt(56, 318, "Aciers concernés : 16MnCr5, 18CrMo4 — reconnaissables à leur faible teneur en carbone.", 11, FIN))
    return _svg("".join(p), 760, 340)


# ===========================================================================
# 23. ISOLER UNE PIÈCE ET COUPER : LE TORSEUR DE COHÉSION
# ===========================================================================

def isoler_et_couper():
    p = [_txt(40, 26, "Pour savoir ce qui se passe DANS la pièce, on la coupe par la pensée :", 13, TRAIT, "start", True)]
    # barre complete
    p.append(f"<rect x='90' y='70' width='300' height='40' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<line x1='60' y1='90' x2='88' y2='90' stroke='{ARBRE}' stroke-width='2.5' marker-start='url(#k1)'/>")
    p.append(f"<line x1='392' y1='90' x2='420' y2='90' stroke='{ARBRE}' stroke-width='2.5' marker-end='url(#k2)'/>")
    p.append("<defs>"
             f"<marker id='k1' markerWidth='10' markerHeight='8' refX='1' refY='4' orient='auto'><path d='M10,0 L0,4 L10,8 z' fill='{ARBRE}'/></marker>"
             f"<marker id='k2' markerWidth='10' markerHeight='8' refX='9' refY='4' orient='auto'><path d='M0,0 L10,4 L0,8 z' fill='{ARBRE}'/></marker>"
             "</defs>")
    p.append(_txt(45, 62, "F", 13, ARBRE, "middle", True))
    p.append(_txt(432, 62, "F", 13, ARBRE, "middle", True))
    p.append(_txt(240, 138, "la barre tendue, vue de l'extérieur", 11, FIN, "middle"))
    p.append(f"<line x1='240' y1='60' x2='240' y2='120' stroke='{ALERTE}' stroke-width='1.6' stroke-dasharray='6 4'/>")
    p.append(_txt(240, 52, "on coupe ici", 10, ALERTE, "middle", True))
    # les deux troncons
    p.append(f"<rect x='90' y='215' width='150' height='40' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<rect x='300' y='215' width='150' height='40' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<line x1='60' y1='235' x2='88' y2='235' stroke='{ARBRE}' stroke-width='2.5' marker-start='url(#k1)'/>")
    p.append(f"<line x1='452' y1='235' x2='480' y2='235' stroke='{ARBRE}' stroke-width='2.5' marker-end='url(#k2)'/>")
    p.append(f"<line x1='240' y1='235' x2='262' y2='235' stroke='{ALESAGE}' stroke-width='3' marker-end='url(#k3)'/>")
    p.append(f"<line x1='300' y1='235' x2='278' y2='235' stroke='{ALESAGE}' stroke-width='3' marker-end='url(#k4)'/>")
    p.append("<defs>"
             f"<marker id='k3' markerWidth='10' markerHeight='8' refX='9' refY='4' orient='auto'><path d='M0,0 L10,4 L0,8 z' fill='{ALESAGE}'/></marker>"
             f"<marker id='k4' markerWidth='10' markerHeight='8' refX='1' refY='4' orient='auto'><path d='M10,0 L0,4 L10,8 z' fill='{ALESAGE}'/></marker>"
             "</defs>")
    p.append(_txt(270, 200, "N", 13, ALESAGE, "middle", True))
    p.append(_txt(270, 285, "l'effort intérieur : c'est LUI qu'on cherche", 11, ALESAGE, "middle", True))
    p.append(f"<rect x='510' y='190' width='210' height='100' fill='#eff6ff' stroke='{ALESAGE}' rx='6'/>")
    p.append(_txt(525, 214, "Méthode, toujours :", 12, TRAIT, "start", True))
    p.append(_txt(525, 234, "1. j'isole un tronçon", 11, FIN))
    p.append(_txt(525, 252, "2. je liste les forces extérieures", 11, FIN))
    p.append(_txt(525, 270, "3. j'écris l'équilibre", 11, FIN))
    p.append(f"<rect x='40' y='310' width='680' height='46' fill='#f0fdf4' stroke='{OK}' rx='6'/>")
    p.append(_txt(56, 331, "L'effort intérieur N vaut ici F. La contrainte vaut ensuite σ = N / S : c'est ce que", 12, TRAIT, "start", True))
    p.append(_txt(56, 349, "ressent vraiment la matière, et c'est ça qu'on compare à la limite du matériau.", 12, FIN))
    return _svg("".join(p), 760, 370)


# ===========================================================================
# 24. LES QUATRE SOLLICITATIONS SIMPLES
# ===========================================================================

def quatre_sollicitations():
    p = [_txt(40, 26, "Toute pièce subit une combinaison de ces quatre cas :", 13, TRAIT, "start", True)]
    cases = [
        (40, "TRACTION", "σ = N / S", "on tire : la barre s'allonge", "tirant, tige de vérin", ALESAGE),
        (225, "CISAILLEMENT", "τ = T / S", "on tranche : les sections glissent", "axe, goupille, rivet", ARBRE),
        (410, "TORSION", "τ = Mt / (I₀/v)", "on tord : les sections tournent", "arbre de transmission", OK),
        (595, "FLEXION", "σ = Mf / (I/v)", "on plie : une face tendue, l'autre comprimée", "poutre, potence", ALERTE),
    ]
    for x, nom, formule, desc, ex, couleur in cases:
        p.append(f"<rect x='{x}' y='55' width='165' height='265' rx='8' fill='#ffffff' stroke='{couleur}' stroke-width='2'/>")
        p.append(_txt(x + 82, 80, nom, 12, couleur, "middle", True))
        cy = 135
        if nom == "TRACTION":
            p.append(f"<rect x='{x + 52}' y='{cy - 30}' width='60' height='60' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
            p.append(f"<line x1='{x + 82}' y1='{cy - 55}' x2='{x + 82}' y2='{cy - 33}' stroke='{couleur}' stroke-width='2.5'/>")
            p.append(f"<line x1='{x + 82}' y1='{cy + 33}' x2='{x + 82}' y2='{cy + 55}' stroke='{couleur}' stroke-width='2.5'/>")
        elif nom == "CISAILLEMENT":
            p.append(f"<rect x='{x + 42}' y='{cy - 28}' width='80' height='26' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
            p.append(f"<rect x='{x + 42}' y='{cy + 2}' width='80' height='26' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
            p.append(f"<line x1='{x + 30}' y1='{cy - 15}' x2='{x + 130}' y2='{cy - 15}' stroke='{couleur}' stroke-width='2'/>")
            p.append(f"<line x1='{x + 130}' y1='{cy + 15}' x2='{x + 30}' y2='{cy + 15}' stroke='{couleur}' stroke-width='2'/>")
        elif nom == "TORSION":
            p.append(f"<rect x='{x + 32}' y='{cy - 18}' width='100' height='36' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
            p.append(f"<path d='M{x + 40},{cy - 30} a 18,18 0 1,1 -6,14' fill='none' stroke='{couleur}' stroke-width='2.2'/>")
            p.append(f"<path d='M{x + 124},{cy + 30} a 18,18 0 1,1 6,-14' fill='none' stroke='{couleur}' stroke-width='2.2'/>")
        else:
            p.append(f"<path d='M{x + 25},{cy - 12} Q{x + 82},{cy + 32} {x + 139},{cy - 12} L{x + 139},{cy + 6} "
                     f"Q{x + 82},{cy + 50} {x + 25},{cy + 6} Z' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
            p.append(f"<line x1='{x + 82}' y1='{cy - 45}' x2='{x + 82}' y2='{cy - 18}' stroke='{couleur}' stroke-width='2.5'/>")
        p.append(_txt(x + 82, 205, formule, 12, TRAIT, "middle", True))
        # description sur deux lignes
        mots = desc.split()
        moitie = len(mots) // 2
        p.append(_txt(x + 82, 235, " ".join(mots[:moitie]), 10, FIN, "middle"))
        p.append(_txt(x + 82, 250, " ".join(mots[moitie:]), 10, FIN, "middle"))
        p.append(_txt(x + 82, 290, ex, 10, couleur, "middle", True))
    return _svg("".join(p), 760, 340)


# ===========================================================================
# 25. FLEXION : FIBRE TENDUE, FIBRE COMPRIMÉE
# ===========================================================================

def fibres_flexion():
    p = [_txt(40, 26, "Quand une poutre plie, le haut et le bas ne subissent pas la même chose :", 13, TRAIT, "start", True)]
    # poutre flechie
    p.append(f"<path d='M80,110 Q330,175 580,110 L580,160 Q330,225 80,160 Z' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<path d='M80,135 Q330,200 580,135' fill='none' stroke='{AXE}' stroke-width='1.6' stroke-dasharray='7 4'/>")
    p.append(_txt(628, 132, "axe neutre", 11, AXE, "end", True))
    p.append(_txt(628, 148, "(ni tendu ni comprimé)", 9, FIN, "end"))
    p.append(f"<line x1='330' y1='60' x2='330' y2='88' stroke='{ALERTE}' stroke-width='2.5' marker-end='url(#m1)'/>")
    p.append("<defs><marker id='m1' markerWidth='9' markerHeight='9' refX='8' refY='4.5' orient='auto'>"
             f"<path d='M0,0 L9,4.5 L0,9 z' fill='{ALERTE}'/></marker></defs>")
    p.append(_txt(330, 52, "F", 13, ALERTE, "middle", True))
    p.append(_txt(330, 120, "fibres COMPRIMÉES", 11, ALESAGE, "middle", True))
    p.append(_txt(330, 212, "fibres TENDUES", 11, ARBRE, "middle", True))
    # repartition triangulaire
    p.append(_txt(690, 90, "contrainte", 11, TRAIT, "middle", True))
    p.append(f"<line x1='690' y1='105' x2='690' y2='215' stroke='{TRAIT}' stroke-width='1.4'/>")
    p.append(f"<path d='M690,105 L740,105 L690,160 Z' fill='{ALESAGE}' opacity='0.4'/>")
    p.append(f"<path d='M690,160 L640,215 L690,215 Z' fill='{ARBRE}' opacity='0.4'/>")
    p.append(_txt(690, 232, "maxi aux extrémités", 9, FIN, "middle"))
    p.append(f"<rect x='40' y='255' width='680' height='96' fill='#f0fdf4' stroke='{OK}' rx='6'/>")
    p.append(_txt(56, 278, "Deux conséquences majeures pour le concepteur :", 12, TRAIT, "start", True))
    p.append(_txt(56, 300, "• la matière proche de l'axe neutre ne sert presque à rien → d'où les profils I, U, tubes ;", 11, FIN))
    p.append(_txt(56, 320, "• la contrainte est maximale sur les faces extérieures → une rayure ou une arête vive", 11, FIN))
    p.append(_txt(56, 338, "   à cet endroit amorce la rupture. C'est là qu'il faut des congés généreux.", 11, FIN))
    return _svg("".join(p), 760, 365)


# ===========================================================================
# 26. CONCENTRATION DE CONTRAINTE
# ===========================================================================

def concentration_contrainte():
    p = [_txt(40, 26, "Deux barres tirées avec la même force. Laquelle casse en premier ?", 13, TRAIT, "start", True)]
    # barre saine
    p.append(f"<rect x='70' y='90' width='260' height='60' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    for i in range(8):
        x = 82 + i * 33
        p.append(f"<line x1='{x}' y1='95' x2='{x}' y2='145' stroke='{OK}' stroke-width='1.6'/>")
    p.append(_txt(200, 175, "lignes de force régulières : σ = N/S partout", 11, OK, "middle"))
    # barre avec entaille
    p.append(f"<path d='M430,90 L690,90 L690,150 L430,150 Z' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<path d='M545,90 a 18,18 0 0,1 36,0' fill='{FOND}' stroke='{TRAIT}' stroke-width='2'/>")
    for i in range(8):
        x = 442 + i * 33
        if 520 < x < 610:
            p.append(f"<path d='M{x},95 Q{x + (10 if x > 563 else -10)},120 {x},145' fill='none' stroke='{ALERTE}' stroke-width='2'/>")
        else:
            p.append(f"<line x1='{x}' y1='95' x2='{x}' y2='145' stroke='{OK}' stroke-width='1.6'/>")
    p.append(_txt(563, 78, "entaille", 10, ALERTE, "middle", True))
    p.append(_txt(560, 175, "les lignes se resserrent : la contrainte locale explose", 11, ALERTE, "middle"))
    p.append(f"<rect x='40' y='200' width='680' height='118' fill='#fff7ed' stroke='{ARBRE}' rx='6'/>")
    p.append(_txt(56, 224, "σ réelle = Kt × σ calculée. Le coefficient Kt vaut couramment 2 à 3, et jusqu'à 5", 12, TRAIT, "start", True))
    p.append(_txt(56, 242, "sur une arête vive.", 12, TRAIT))
    p.append(_txt(56, 268, "Concrètement : une pièce calculée « largement suffisante » casse quand même,", 11, FIN))
    p.append(_txt(56, 286, "toujours au même endroit — gorge, épaulement, angle rentrant, trou, filetage.", 11, FIN))
    p.append(_txt(56, 310, "La parade est gratuite : un congé de raccordement au lieu d'un angle vif.", 12, OK, "start", True))
    return _svg("".join(p), 760, 335)


# ===========================================================================
# 27. ESQUISSE SOUS-CONTRAINTE OU TOTALEMENT CONTRAINTE
# ===========================================================================

def esquisse_contraintes():
    p = [_txt(40, 26, "La même esquisse, dans les deux états possibles :", 13, TRAIT, "start", True)]
    # sous-contrainte
    p.append(_txt(190, 58, "SOUS-CONTRAINTE (bleue)", 12, ALERTE, "middle", True))
    p.append(f"<rect x='95' y='80' width='190' height='110' fill='none' stroke='#3b82f6' stroke-width='2.2'/>")
    p.append(f"<rect x='118' y='96' width='190' height='110' fill='none' stroke='#93c5fd' stroke-width='1.6' stroke-dasharray='6 4'/>")
    p.append(f"<circle cx='190' cy='135' r='22' fill='none' stroke='#3b82f6' stroke-width='2'/>")
    p.append(_txt(190, 232, "elle peut encore bouger toute seule", 11, ALERTE, "middle", True))
    p.append(_txt(190, 250, "à la prochaine modification", 10, FIN, "middle"))
    # totalement contrainte
    p.append(_txt(560, 58, "TOTALEMENT CONTRAINTE (noire)", 12, OK, "middle", True))
    p.append(f"<rect x='465' y='80' width='190' height='110' fill='none' stroke='{TRAIT}' stroke-width='2.2'/>")
    p.append(f"<circle cx='560' cy='135' r='22' fill='none' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<line x1='465' y1='205' x2='655' y2='205' stroke='{FIN}' stroke-width='1'/>")
    p.append(_txt(560, 200, "190", 11, FIN, "middle"))
    p.append(f"<line x1='690' y1='80' x2='690' y2='190' stroke='{FIN}' stroke-width='1'/>")
    p.append(_txt(700, 138, "110", 11, FIN))
    p.append(f"<line x1='560' y1='135' x2='560' y2='80' stroke='{AXE}' stroke-width='1' stroke-dasharray='4 3'/>")
    p.append(_txt(560, 232, "sa forme ne peut plus dériver :", 11, OK, "middle", True))
    p.append(_txt(560, 250, "elle ne change que par ses cotes", 10, FIN, "middle"))
    p.append(f"<rect x='40' y='275' width='680' height='68' fill='#f0fdf4' stroke='{OK}' rx='6'/>")
    p.append(_txt(56, 298, "Une esquisse bleue est une bombe à retardement : elle passera l'examen d'aujourd'hui,", 12, TRAIT, "start", True))
    p.append(_txt(56, 316, "et cassera la pièce dans six mois, quand quelqu'un modifiera une cote en amont.", 12, FIN))
    p.append(_txt(56, 336, "Réflexe : contraindre à 100 % — géométrie d'abord (symétrie, tangence), cotes ensuite.", 11, ALESAGE))
    return _svg("".join(p), 760, 360)


# ===========================================================================
# 28. L'ARBRE DE CRÉATION : L'ORDRE COMPTE
# ===========================================================================

def arbre_de_creation():
    p = [_txt(40, 26, "Deux façons de construire la MÊME pièce :", 13, TRAIT, "start", True)]
    mauvais = ["Extrusion du corps", "Congés R3", "Perçage Ø10", "Congés R2", "Perçage Ø6", "Congé R5"]
    bon = ["Extrusion du corps", "Perçage Ø10", "Perçage Ø6", "Répétition des perçages", "TOUS les congés", "Dépouille"]
    for x, titre, liste, couleur, verdict in ((55, "Désordonné", mauvais, ALERTE, "modifier le corps casse tout"),
                                              (415, "Ordonné", bon, OK, "on modifie sans rien casser")):
        p.append(f"<rect x='{x}' y='55' width='290' height='278' rx='8' fill='#ffffff' stroke='{couleur}' stroke-width='2'/>")
        p.append(_txt(x + 145, 80, titre, 13, couleur, "middle", True))
        y = 105
        for item in liste:
            marque = ALERTE if ("Congé" in item and liste is mauvais and item != liste[-1]) else FIN
            p.append(f"<rect x='{x + 20}' y='{y}' width='250' height='26' rx='4' fill='#f8fafc' stroke='{FIN}' stroke-width='1'/>")
            p.append(_txt(x + 32, y + 18, item, 11, TRAIT))
            if "Congé" in item and liste is mauvais:
                p.append(_txt(x + 258, y + 18, "!", 13, ALERTE, "end", True))
            y += 33
        p.append(_txt(x + 145, 320, verdict, 11, couleur, "middle", True))
    p.append(f"<rect x='40' y='350' width='680' height='68' fill='#fff7ed' stroke='{ARBRE}' rx='6'/>")
    p.append(_txt(56, 373, "Règle : congés, chanfreins et dépouilles TOUJOURS en fin d'arbre.", 12, TRAIT, "start", True))
    p.append(_txt(56, 393, "Placés trop tôt, ils font disparaître les arêtes sur lesquelles s'appuient les fonctions", 11, FIN))
    p.append(_txt(56, 411, "suivantes — et le modèle tombe en erreur à la première modification.", 11, FIN))
    return _svg("".join(p), 760, 435)


# ===========================================================================
# 29. LES FORMATS D'ÉCHANGE
# ===========================================================================

def formats_echange():
    p = [_txt(40, 26, "Chaque format garde une partie de l'information — et perd le reste :", 13, TRAIT, "start", True)]
    lignes = [
        (".sldprt / .catpart", "format natif", "TOUT : l'historique, les fonctions, les paramètres",
         "seulement entre utilisateurs du même logiciel", OK),
        (".step", "échange 3D exact", "la géométrie exacte (surfaces, volumes), mais plus l'historique",
         "LE format d'échange entre bureaux d'études", ALESAGE),
        (".stl", "maillage", "une peau faite de triangles : forme approchée",
         "impression 3D uniquement — on ne remodélise jamais dessus", ARBRE),
        (".dxf", "2D", "des contours à plat",
         "découpe laser, jet d'eau, poinçonnage de tôle", ARBRE),
        (".pdf", "image du plan", "le dessin coté, non modifiable",
         "diffusion, archivage, envoi à l'atelier", FIN),
    ]
    y = 62
    for ext, nature, contenu, usage, couleur in lignes:
        p.append(f"<rect x='45' y='{y}' width='670' height='58' rx='6' fill='#ffffff' stroke='{couleur}' stroke-width='1.6'/>")
        p.append(_txt(62, y + 24, ext, 14, couleur, "start", True))
        p.append(_txt(62, y + 44, nature, 10, FIN))
        p.append(_txt(215, y + 24, contenu, 11, TRAIT))
        p.append(_txt(215, y + 44, usage, 10, FIN))
        y += 66
    return _svg("".join(p), 760, y + 10)


# ===========================================================================
# 30. ISOSTATIQUE OU HYPERSTATIQUE
# ===========================================================================

def isostatique_hyperstatique():
    p = [_txt(40, 26, "Le même arbre, monté de deux façons :", 13, TRAIT, "start", True)]
    for x0, titre, couleur, verdict, detail in (
            (45, "MONTAGE HYPERSTATIQUE", ALERTE, "les deux paliers bloquent l'axial",
             "l'arbre chauffe, s'allonge, ne peut pas → il précontraint les roulements → grippage"),
            (400, "MONTAGE ISOSTATIQUE", OK, "un palier fixe, un palier libre",
             "l'arbre s'allonge librement : la dilatation est absorbée")):
        p.append(f"<rect x='{x0}' y='50' width='315' height='190' rx='8' fill='#ffffff' stroke='{couleur}' stroke-width='2'/>")
        p.append(_txt(x0 + 157, 75, titre, 12, couleur, "middle", True))
        # arbre
        p.append(f"<rect x='{x0 + 40}' y='140' width='235' height='22' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
        # paliers
        for xp in (x0 + 60, x0 + 235):
            p.append(f"<rect x='{xp - 16}' y='120' width='32' height='62' fill='#cbd5e1' stroke='{TRAIT}' stroke-width='1.8'/>")
        # butees
        p.append(f"<line x1='{x0 + 44}' y1='118' x2='{x0 + 44}' y2='184' stroke='{ALERTE}' stroke-width='3'/>")
        p.append(f"<line x1='{x0 + 76}' y1='118' x2='{x0 + 76}' y2='184' stroke='{ALERTE}' stroke-width='3'/>")
        if titre.endswith("HYPERSTATIQUE"):
            p.append(f"<line x1='{x0 + 219}' y1='118' x2='{x0 + 219}' y2='184' stroke='{ALERTE}' stroke-width='3'/>")
            p.append(f"<line x1='{x0 + 251}' y1='118' x2='{x0 + 251}' y2='184' stroke='{ALERTE}' stroke-width='3'/>")
            p.append(_txt(x0 + 235, 205, "bloqué aussi", 10, ALERTE, "middle", True))
        else:
            p.append(f"<line x1='{x0 + 219}' y1='151' x2='{x0 + 265}' y2='151' stroke='{OK}' stroke-width='2'/>")
            p.append(_txt(x0 + 240, 205, "libre de coulisser", 10, OK, "middle", True))
        p.append(_txt(x0 + 60, 205, "bloqué", 10, TRAIT, "middle"))
        p.append(_txt(x0 + 157, 228, verdict, 11, couleur, "middle", True))
        p.append(_txt(x0 + 157, 262, "", 10, FIN, "middle"))
    p.append(f"<rect x='45' y='252' width='315' height='58' rx='6' fill='#fef2f2' stroke='{ALERTE}'/>")
    p.append(_txt(60, 273, "L'arbre chauffe et s'allonge, mais ne", 11, TRAIT))
    p.append(_txt(60, 290, "peut pas : il précontraint les roulements,", 11, TRAIT))
    p.append(_txt(60, 305, "qui chauffent encore plus → grippage.", 11, ALERTE))
    p.append(f"<rect x='400' y='252' width='315' height='58' rx='6' fill='#f0fdf4' stroke='{OK}'/>")
    p.append(_txt(415, 273, "La dilatation est absorbée par le palier", 11, TRAIT))
    p.append(_txt(415, 290, "libre. Règle absolue : UN SEUL palier", 11, TRAIT))
    p.append(_txt(415, 305, "fixe par arbre.", 11, OK, "start", True))
    return _svg("".join(p), 760, 330)


# ===========================================================================
# 31. LA RÈGLE DES CHARGES : QUELLE BAGUE SERRER ?
# ===========================================================================

def regle_des_charges():
    p = [_txt(40, 26, "Quelle bague monte-t-on serrée ? Une seule question à se poser :", 13, TRAIT, "start", True)]
    p.append(f"<rect x='60' y='55' width='640' height='42' rx='8' fill='#eff6ff' stroke='{ALESAGE}' stroke-width='2'/>")
    p.append(_txt(380, 82, "« Cette bague tourne-t-elle par rapport à la direction de la charge ? »", 13, ALESAGE, "middle", True))
    cas = [
        (60, "Arbre tournant, charge fixe", "le cas le plus courant : réducteur, pompe",
         "bague INTÉRIEURE serrée → arbre en k6", "bague extérieure glissante → alésage H7"),
        (400, "Moyeu tournant, charge fixe", "tambour de convoyeur, roue folle",
         "bague EXTÉRIEURE serrée → alésage M7", "bague intérieure glissante → arbre h6"),
    ]
    for x0, titre, exemple, serre, glisse in cas:
        p.append(f"<rect x='{x0}' y='120' width='300' height='170' rx='8' fill='#ffffff' stroke='{FIN}' stroke-width='1.6'/>")
        p.append(_txt(x0 + 150, 145, titre, 12, TRAIT, "middle", True))
        p.append(_txt(x0 + 150, 163, exemple, 10, FIN, "middle"))
        p.append(f"<rect x='{x0 + 30}' y='185' width='240' height='34' rx='5' fill='{ARBRE}' opacity='0.16' stroke='{ARBRE}'/>")
        p.append(_txt(x0 + 150, 207, serre, 11, ARBRE, "middle", True))
        p.append(f"<rect x='{x0 + 30}' y='230' width='240' height='34' rx='5' fill='{ALESAGE}' opacity='0.14' stroke='{ALESAGE}'/>")
        p.append(_txt(x0 + 150, 252, glisse, 11, ALESAGE, "middle", True))
    p.append(f"<rect x='40' y='305' width='680' height='66' fill='#fff7ed' stroke='{ARBRE}' rx='6'/>")
    p.append(_txt(56, 328, "Si la bague qui devrait être serrée est montée avec du jeu, elle « flue » lentement", 12, TRAIT, "start", True))
    p.append(_txt(56, 346, "sur sa portée : la surface est matée en quelques dizaines d'heures, et le montage", 12, FIN))
    p.append(_txt(56, 364, "est bon à jeter. C'est l'erreur de montage la plus fréquente en maintenance.", 12, FIN))
    return _svg("".join(p), 760, 390)


# ===========================================================================
# 32. ARBRE-MOYEU : COMMENT TRANSMETTRE LE COUPLE
# ===========================================================================

def liaison_arbre_moyeu():
    p = [_txt(40, 26, "Faire tourner un moyeu avec son arbre : quatre solutions courantes",
              13, TRAIT, "start", True)]
    solutions = [
        (50, "Clavette", "une barrette dans deux rainures", "démontable, économique",
         "il faut usiner deux rainures", ALESAGE),
        (232, "Cannelures", "des dents sur tout le tour", "couple élevé, coulissement possible",
         "cher : brochage ou taillage", OK),
        (414, "Serrage H7/p6", "l'arbre est plus gros que le trou", "aucun usinage de rainure",
         "montage à la presse, démontage difficile", ARBRE),
        (596, "Goupille", "une tige traversante", "très simple, sert de fusible",
         "couple faible, affaiblit l'arbre", ALERTE),
    ]
    for x, nom, principe, avantage, limite, couleur in solutions:
        p.append(f"<rect x='{x}' y='55' width='164' height='250' rx='8' fill='#ffffff' stroke='{couleur}' stroke-width='2'/>")
        p.append(_txt(x + 82, 80, nom, 12, couleur, "middle", True))
        cy = 130
        p.append(f"<circle cx='{x + 82}' cy='{cy}' r='38' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
        p.append(f"<circle cx='{x + 82}' cy='{cy}' r='22' fill='{FOND}' stroke='{TRAIT}' stroke-width='2'/>")
        if nom == "Clavette":
            p.append(f"<rect x='{x + 74}' y='{cy - 30}' width='16' height='16' fill='{couleur}' stroke='{TRAIT}' stroke-width='1.4'/>")
        elif nom == "Cannelures":
            import math as _m
            for k in range(10):
                a = _m.radians(k * 36)
                x1, y1 = x + 82 + 22 * _m.cos(a), cy + 22 * _m.sin(a)
                x2, y2 = x + 82 + 30 * _m.cos(a), cy + 30 * _m.sin(a)
                p.append(f"<line x1='{x1:.1f}' y1='{y1:.1f}' x2='{x2:.1f}' y2='{y2:.1f}' stroke='{couleur}' stroke-width='2.4'/>")
        elif nom.startswith("Serrage"):
            p.append(f"<circle cx='{x + 82}' cy='{cy}' r='26' fill='none' stroke='{couleur}' stroke-width='3' stroke-dasharray='4 3'/>")
        else:
            p.append(f"<line x1='{x + 44}' y1='{cy}' x2='{x + 120}' y2='{cy}' stroke='{couleur}' stroke-width='3.5'/>")
        p.append(_txt(x + 82, 190, principe.split(" ")[0], 10, FIN, "middle"))
        p.append(_txt(x + 82, 204, " ".join(principe.split(" ")[1:]), 10, FIN, "middle"))
        p.append(_txt(x + 82, 234, "+ " + avantage.split(",")[0], 10, OK, "middle", True))
        p.append(_txt(x + 82, 262, "− " + limite.split(",")[0], 10, ALERTE, "middle"))
        p.append(_txt(x + 82, 276, ",".join(limite.split(",")[1:]).strip(), 10, ALERTE, "middle"))
    p.append(f"<rect x='40' y='320' width='680' height='48' fill='#eff6ff' stroke='{ALESAGE}' rx='6'/>")
    p.append(_txt(56, 342, "La clavette transmet le COUPLE. Elle ne maintient jamais le moyeu axialement :", 12, TRAIT, "start", True))
    p.append(_txt(56, 360, "l'arrêt axial se fait par un épaulement, un anneau élastique ou une vis de bout d'arbre.", 11, FIN))
    return _svg("".join(p), 760, 385)


# ===========================================================================
# 33. CALCULER UN AJUSTEMENT EN QUATRE ÉTAPES
# ===========================================================================

def calcul_ajustement_etapes():
    p = [_txt(40, 26, "Ø30 H7/g6 — la marche à suivre, toujours la même :", 13, TRAIT, "start", True)]
    etapes = [
        ("1", "Lire les IT dans la table", "Ø30 → IT7 = 21 µm  ·  IT6 = 13 µm", ALESAGE),
        ("2", "Placer l'alésage (lettre H)", "EI = 0  →  30,000  à  30,021", ALESAGE),
        ("3", "Placer l'arbre (lettre g)", "es = −7 µm  →  29,980  à  29,993", ARBRE),
        ("4", "Soustraire", "Jmax = 30,021 − 29,980 = 0,041   ·   Jmin = 30,000 − 29,993 = 0,007", OK),
    ]
    y = 62
    for num, titre, detail, couleur in etapes:
        p.append(f"<rect x='45' y='{y}' width='670' height='62' rx='6' fill='#ffffff' stroke='{couleur}' stroke-width='1.6'/>")
        p.append(f"<circle cx='78' cy='{y + 31}' r='16' fill='{couleur}'/>")
        p.append(_txt(78, y + 36, num, 14, "#ffffff", "middle", True))
        p.append(_txt(110, y + 26, titre, 12, TRAIT, "start", True))
        p.append(_txt(110, y + 47, detail, 12, couleur))
        y += 72
    p.append(f"<rect x='45' y='{y + 6}' width='670' height='44' fill='#f0fdf4' stroke='{OK}' rx='6'/>")
    p.append(_txt(62, y + 33, "Les deux valeurs sont positives : il y a TOUJOURS du jeu. C'est un ajustement glissant.",
                  12, TRAIT, "start", True))
    return _svg("".join(p), 760, y + 66)


# ===========================================================================
# 34. CHOISIR UN MATÉRIAU : L'ARBRE DE DÉCISION
# ===========================================================================

def choisir_materiau():
    p = [_txt(40, 26, "Les questions à se poser, dans cet ordre :", 13, TRAIT, "start", True)]
    questions = [
        ("La pièce doit-elle surtout RÉSISTER ou surtout ne pas PLIER ?",
         "résister → jouer sur la nuance (Re) · ne pas plier → jouer sur la FORME (I), pas sur la nuance", ALESAGE),
        ("Sera-t-elle soudée ?",
         "oui → S235, S355, C22 · non → tout est ouvert, y compris C45 et 42CrMo4", ARBRE),
        ("Faudra-t-il la tremper ?",
         "il faut au moins 0,3 % de carbone : C45 oui, S235 non", OK),
        ("Le milieu est-il humide, chloré, alimentaire ?",
         "oui → inox (X5CrNi18-10) ou protection : galvanisation, époxy, anodisation", ALESAGE),
        ("La masse est-elle critique ?",
         "oui → aluminium ou polymère, mais prévoir des sections plus épaisses (E plus faible)", ARBRE),
        ("Quelle série, quel budget, quelle disponibilité locale ?",
         "une nuance introuvable ou à 4 mois de délai est un mauvais choix, même si elle est idéale", FIN),
    ]
    y = 58
    for question, reponse, couleur in questions:
        p.append(f"<rect x='45' y='{y}' width='670' height='52' rx='6' fill='#ffffff' stroke='{couleur}' stroke-width='1.5'/>")
        p.append(_txt(62, y + 22, question, 12, TRAIT, "start", True))
        p.append(_txt(62, y + 41, reponse, 11, couleur))
        y += 60
    p.append(_txt(40, y + 24, "On retient toujours la solution LA MOINS CHÈRE qui satisfait toutes les exigences —",
                  12, TRAIT, "start", True))
    p.append(_txt(40, y + 42, "jamais la plus performante.", 12, TRAIT, "start", True))
    return _svg("".join(p), 760, y + 60)


# ===========================================================================
# 35. DÉCOMPOSER UNE FORCE
# ===========================================================================

def decomposer_force():
    p = [_txt(40, 26, "Une force qui tire de biais se remplace par deux forces perpendiculaires :",
              13, TRAIT, "start", True)]
    ox, oy = 140, 250
    p.append(f"<line x1='{ox}' y1='{oy}' x2='420' y2='{oy}' stroke='{FIN}' stroke-width='1.4'/>")
    p.append(f"<line x1='{ox}' y1='{oy}' x2='{ox}' y2='80' stroke='{FIN}' stroke-width='1.4'/>")
    # force oblique
    p.append(f"<line x1='{ox}' y1='{oy}' x2='380' y2='110' stroke='{ALERTE}' stroke-width='3' marker-end='url(#p1)'/>")
    p.append("<defs><marker id='p1' markerWidth='10' markerHeight='10' refX='9' refY='5' orient='auto'>"
             f"<path d='M0,0 L10,5 L0,10 z' fill='{ALERTE}'/></marker></defs>")
    p.append(_txt(395, 105, "F = 800 N", 13, ALERTE, "start", True))
    # composantes
    p.append(f"<line x1='{ox}' y1='{oy}' x2='380' y2='{oy}' stroke='{ALESAGE}' stroke-width='2.5' marker-end='url(#p2)'/>")
    p.append("<defs><marker id='p2' markerWidth='9' markerHeight='9' refX='8' refY='4.5' orient='auto'>"
             f"<path d='M0,0 L9,4.5 L0,9 z' fill='{ALESAGE}'/></marker></defs>")
    p.append(_txt(260, oy + 22, "Fx = F cos α = 693 N", 12, ALESAGE, "middle", True))
    p.append(f"<line x1='380' y1='{oy}' x2='380' y2='110' stroke='{ARBRE}' stroke-width='2.5' stroke-dasharray='6 4' marker-end='url(#p3)'/>")
    p.append("<defs><marker id='p3' markerWidth='9' markerHeight='9' refX='8' refY='4.5' orient='auto'>"
             f"<path d='M0,0 L9,4.5 L0,9 z' fill='{ARBRE}'/></marker></defs>")
    p.append(_txt(370, 190, "Fy = F sin α", 12, ARBRE, "end", True))
    p.append(_txt(370, 208, "= 400 N", 12, ARBRE, "end", True))
    # angle
    p.append(f"<path d='M{ox + 55},{oy} a 55,55 0 0,0 51,-20' fill='none' stroke='{TRAIT}' stroke-width='1.3'/>")
    p.append(_txt(ox + 62, oy - 14, "α = 30°", 12, TRAIT, "start", True))
    p.append(f"<rect x='470' y='120' width='250' height='120' fill='#eff6ff' stroke='{ALESAGE}' rx='6'/>")
    p.append(_txt(486, 146, "SOH — sin = opp / hyp", 12, TRAIT, "start", True))
    p.append(_txt(486, 170, "CAH — cos = adj / hyp", 12, TRAIT, "start", True))
    p.append(_txt(486, 194, "TOA — tan = opp / adj", 12, TRAIT, "start", True))
    p.append(_txt(486, 222, "Calculatrice en mode DEG !", 11, ALERTE, "start", True))
    p.append(_txt(40, 300, "En RDM, c'est la composante PERPENDICULAIRE à la pièce qui la fait fléchir — pas la force totale.",
                  12, TRAIT, "start", True))
    return _svg("".join(p), 760, 320)


# ===========================================================================
# 36. LE PROFIL DE VITESSE TRAPÉZOÏDAL
# ===========================================================================

def profil_trapezoidal():
    p = [_txt(40, 26, "Un axe motorisé ne démarre jamais brutalement :", 13, TRAIT, "start", True)]
    ox, oy = 90, 230
    p.append(f"<line x1='{ox}' y1='{oy}' x2='640' y2='{oy}' stroke='{TRAIT}' stroke-width='1.5'/>")
    p.append(f"<line x1='{ox}' y1='{oy}' x2='{ox}' y2='70' stroke='{TRAIT}' stroke-width='1.5'/>")
    p.append(_txt(365, 262, "temps (s)", 11, FIN, "middle"))
    p.append(f"<text x='38' y='150' {_POLICE} font-size='11' fill='{FIN}' transform='rotate(-90 38,150)'>vitesse (m/s)</text>")
    # trapeze
    p.append(f"<path d='M{ox},{oy} L230,110 L470,110 L610,{oy} Z' fill='{ALESAGE}' opacity='0.18' stroke='{ALESAGE}' stroke-width='2.5'/>")
    p.append(f"<line x1='{ox}' y1='110' x2='230' y2='110' stroke='{FIN}' stroke-width='1' stroke-dasharray='4 3'/>")
    p.append(_txt(ox - 8, 114, "v", 13, ALESAGE, "end", True))
    # zones
    p.append(_txt(160, 175, "accélération", 11, ARBRE, "middle", True))
    p.append(_txt(160, 192, "a = v / t", 10, FIN, "middle"))
    p.append(_txt(350, 175, "vitesse constante", 11, TRAIT, "middle", True))
    p.append(_txt(350, 192, "le moteur ne fait", 10, FIN, "middle"))
    p.append(_txt(350, 206, "que vaincre les frottements", 10, FIN, "middle"))
    p.append(_txt(540, 175, "décélération", 11, ARBRE, "middle", True))
    p.append(f"<rect x='660' y='90' width='90' height='90' fill='#fff7ed' stroke='{ARBRE}' rx='6'/>")
    p.append(_txt(705, 114, "L'AIRE", 11, ARBRE, "middle", True))
    p.append(_txt(705, 134, "du trapèze", 10, FIN, "middle"))
    p.append(_txt(705, 152, "= la distance", 10, FIN, "middle"))
    p.append(_txt(705, 170, "parcourue", 10, FIN, "middle"))
    p.append(f"<rect x='40' y='285' width='680' height='66' fill='#f0fdf4' stroke='{OK}' rx='6'/>")
    p.append(_txt(56, 308, "La PENTE des rampes donne l'accélération, donc l'effort : F = m × a.", 12, TRAIT, "start", True))
    p.append(_txt(56, 328, "Raccourcir la rampe de moitié double l'effort demandé au moteur — et son prix.", 12, FIN))
    p.append(_txt(56, 346, "C'est pourquoi on allonge toujours les rampes autant que le temps de cycle le permet.", 11, OK))
    return _svg("".join(p), 760, 365)


# ===========================================================================
# 37. LA COURBE EN CLOCHE, Cp ET Cpk
# ===========================================================================

def courbe_capabilite():
    import math as _m
    p = [_txt(40, 26, "La production d'une machine se répartit en cloche autour d'une moyenne :",
              13, TRAIT, "start", True)]
    base = 250

    def cloche(centre, largeur, couleur, opac):
        pts = []
        for i in range(0, 101):
            x = centre - 3 * largeur + i * 6 * largeur / 100
            y = base - 120 * _m.exp(-((x - centre) ** 2) / (2 * largeur ** 2))
            pts.append(f"{x:.1f},{y:.1f}")
        return (f"<polyline points='{' '.join(pts)}' fill='none' stroke='{couleur}' stroke-width='2.4' opacity='{opac}'/>")

    # limites de tolerance
    p.append(f"<rect x='180' y='95' width='330' height='155' fill='{OK}' opacity='0.07'/>")
    for x, lbl in ((180, "cote mini"), (510, "cote maxi")):
        p.append(f"<line x1='{x}' y1='90' x2='{x}' y2='{base}' stroke='{OK}' stroke-width='2'/>")
        p.append(_txt(x, 82, lbl, 10, OK, "middle", True))
    p.append(f"<line x1='180' y1='105' x2='510' y2='105' stroke='{OK}' stroke-width='1.2'/>")
    p.append(_txt(345, 100, "IT (la tolérance)", 11, OK, "middle", True))
    # production capable et centree
    p.append(cloche(345, 40, ALESAGE, 1))
    p.append(_txt(345, 272, "Cp = 1,4 · Cpk = 1,4", 12, ALESAGE, "middle", True))
    p.append(_txt(345, 290, "capable et centrée", 10, FIN, "middle"))
    # production decalee
    p.append(cloche(470, 40, ARBRE, 1))
    p.append(_txt(600, 200, "même dispersion,", 11, ARBRE, "start", True))
    p.append(_txt(600, 218, "mais décalée :", 11, ARBRE, "start", True))
    p.append(_txt(600, 240, "Cp = 1,4 inchangé", 11, TRAIT, "start", True))
    p.append(_txt(600, 258, "Cpk chute à 0,3", 11, ALERTE, "start", True))
    p.append(f"<line x1='40' y1='{base}' x2='720' y2='{base}' stroke='{TRAIT}' stroke-width='1.4'/>")
    p.append(f"<rect x='40' y='310' width='680' height='68' fill='#eff6ff' stroke='{ALESAGE}' rx='6'/>")
    p.append(_txt(56, 333, "Cp = IT / 6σ — la machine est-elle assez précise ?", 12, TRAIT, "start", True))
    p.append(_txt(56, 353, "Cpk — est-elle en plus bien centrée ? Cp bon et Cpk mauvais = simple déréglage.", 12, TRAIT, "start", True))
    p.append(_txt(56, 371, "Exigence industrielle courante : Cp et Cpk supérieurs à 1,33.", 11, ALESAGE))
    return _svg("".join(p), 760, 395)


# ===========================================================================
# 38. L'EFFORT D'UN VÉRIN
# ===========================================================================

def effort_verin():
    p = [_txt(40, 26, "Un vérin ne pousse pas aussi fort qu'il ne tire :", 13, TRAIT, "start", True)]
    for y0, titre, couleur, formule, valeur in (
            (70, "EN SORTIE (poussée)", OK, "F = p × S piston", "6 bars × 19,6 cm² = 1 178 N"),
            (215, "EN RENTRÉE (traction)", ARBRE, "F = p × (S piston − S tige)", "6 bars × 16,5 cm² = 989 N")):
        p.append(_txt(56, y0 + 16, titre, 12, couleur, "start", True))
        # corps du verin
        p.append(f"<rect x='60' y='{y0 + 34}' width='230' height='58' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
        # piston
        px = 130 if y0 == 70 else 215
        p.append(f"<rect x='{px}' y='{y0 + 36}' width='16' height='54' fill='{couleur}' opacity='0.6' stroke='{TRAIT}' stroke-width='1.5'/>")
        # tige
        p.append(f"<rect x='{px + 16}' y='{y0 + 56}' width='{300 - px}' height='14' fill='#cbd5e1' stroke='{TRAIT}' stroke-width='1.5'/>")
        # pression
        for k in range(3):
            xa = 70 + k * 18 if y0 == 70 else 300 + k * 14
            p.append(_txt(xa, y0 + 68, "»" if y0 == 70 else "«", 15, ALESAGE, "middle", True))
        p.append(_txt(330, y0 + 52, formule, 12, TRAIT, "start", True))
        p.append(_txt(330, y0 + 76, valeur, 12, couleur, "start", True))
    p.append(f"<rect x='40' y='330' width='680' height='66' fill='#fff7ed' stroke='{ARBRE}' rx='6'/>")
    p.append(_txt(56, 353, "En rentrée, la tige occupe une partie de la surface : il reste moins de section utile.", 12, TRAIT, "start", True))
    p.append(_txt(56, 373, "Réflexe de conception : on oriente toujours un vérin de bridage pour que le serrage", 12, FIN))
    p.append(_txt(56, 391, "se fasse EN POUSSANT.", 12, ARBRE, "start", True))
    return _svg("".join(p), 760, 410)


# ===========================================================================
# 39. LIRE UNE PLAQUE SIGNALÉTIQUE DE MOTEUR
# ===========================================================================

def plaque_moteur():
    p = [_txt(40, 26, "Tout ce qu'il faut savoir tient sur cette plaque :", 13, TRAIT, "start", True)]
    p.append(f"<rect x='60' y='55' width='300' height='210' rx='8' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2.5'/>")
    lignes = [("3 ~ MOT", ""), ("4 kW", "puissance mécanique"), ("400 V", "tension"),
              ("8,3 A", "intensité"), ("1445 min⁻¹", "vitesse réelle"),
              ("cos φ 0,82", "facteur de puissance"), ("IP 55", "indice de protection")]
    y = 85
    for gauche, droite in lignes:
        p.append(_txt(80, y, gauche, 13, TRAIT, "start", True))
        y += 26
    reperes = [(111, "la puissance sur l'arbre, pas celle absorbée", ALESAGE),
               (137, "couplage étoile ou triangle selon le réseau", FIN),
               (163, "sert à choisir le câble et la protection", FIN),
               (189, "1445 et non 1500 : c'est le glissement", ARBRE),
               (215, "0,8 environ pour un moteur asynchrone", FIN),
               (241, "5 = protégé poussière · 5 = jets d'eau", OK)]
    for ly, texte, couleur in reperes:
        p.append(f"<line x1='362' y1='{ly - 4}' x2='395' y2='{ly - 4}' stroke='{couleur}' stroke-width='1.2'/>")
        p.append(_txt(402, ly, texte, 11, couleur))
    p.append(f"<rect x='40' y='285' width='680' height='86' fill='#eff6ff' stroke='{ALESAGE}' rx='6'/>")
    p.append(_txt(56, 308, "Le couple se déduit : C = P / ω, avec ω = 2π × 1445 / 60 = 151 rad/s", 12, TRAIT, "start", True))
    p.append(_txt(56, 330, "→ C = 4000 / 151 = 26,4 N·m", 12, ALESAGE, "start", True))
    p.append(_txt(56, 356, "Et 1445 tr/min ≈ 1500 → moteur 4 pôles. Glissement = 55/1500 = 3,7 %, normal en charge.",
                  11, FIN))
    return _svg("".join(p), 760, 390)


# ===========================================================================
# 40. LE PLANNING DE PROJET ET LE CHEMIN CRITIQUE
# ===========================================================================

def planning_projet():
    p = [_txt(40, 26, "Un projet de 16 semaines, phase par phase :", 13, TRAIT, "start", True)]
    ox = 190
    largeur = 500
    # echelle
    for k in range(0, 17, 4):
        x = ox + k * largeur / 16
        p.append(f"<line x1='{x}' y1='52' x2='{x}' y2='300' stroke='{FIN}' stroke-width='0.8' stroke-dasharray='3 4'/>")
        p.append(_txt(x, 46, f"S{k}", 10, FIN, "middle"))
    taches = [("Analyse du besoin", 0, 3, ALESAGE, True),
              ("Recherche de solutions", 3, 6, ALESAGE, True),
              ("Conception détaillée", 6, 10, ALESAGE, True),
              ("Commande matière", 6, 10, ARBRE, True),
              ("Industrialisation", 10, 13, ALESAGE, True),
              ("Montage et essais", 13, 15, ALESAGE, True),
              ("Dossier et soutenance", 12, 16, OK, False)]
    y = 68
    for nom, deb, fin, couleur, critique in taches:
        x1 = ox + deb * largeur / 16
        x2 = ox + fin * largeur / 16
        p.append(_txt(180, y + 15, nom, 11, TRAIT, "end"))
        p.append(f"<rect x='{x1}' y='{y}' width='{x2 - x1}' height='22' rx='4' fill='{couleur}' "
                 f"opacity='{0.75 if critique else 0.4}' stroke='{couleur}' stroke-width='1.4'/>")
        y += 33
    p.append(f"<line x1='{ox + 16 * largeur / 16}' y1='52' x2='{ox + largeur}' y2='300' stroke='{ALERTE}' stroke-width='2'/>")
    p.append(_txt(ox + largeur - 6, 180, "soutenance", 11, ALERTE, "end", True))
    p.append(f"<rect x='40' y='312' width='680' height='84' fill='#fff7ed' stroke='{ARBRE}' rx='6'/>")
    p.append(_txt(56, 335, "La commande de matière (en orange) est sur le CHEMIN CRITIQUE : tout retard sur", 12, TRAIT, "start", True))
    p.append(_txt(56, 355, "elle décale le montage, donc les essais, donc le dossier.", 12, FIN))
    p.append(_txt(56, 381, "Règle : on planifie à rebours depuis la soutenance, et on garde 15 % de marge.", 12, ARBRE, "start", True))
    return _svg("".join(p), 760, 410)


# ===========================================================================
# 41. LE SEUIL DE RENTABILITÉ ENTRE DEUX PROCÉDÉS
# ===========================================================================

def seuil_rentabilite():
    p = [_txt(40, 26, "Usiner ou mouler ? Tout dépend du nombre de pièces :", 13, TRAIT, "start", True)]
    ox, oy = 100, 300
    p.append(f"<line x1='{ox}' y1='{oy}' x2='680' y2='{oy}' stroke='{TRAIT}' stroke-width='1.5'/>")
    p.append(f"<line x1='{ox}' y1='{oy}' x2='{ox}' y2='70' stroke='{TRAIT}' stroke-width='1.5'/>")
    p.append(_txt(390, 332, "nombre de pièces produites", 11, FIN, "middle"))
    p.append(f"<text x='48' y='190' {_POLICE} font-size='11' fill='{FIN}' transform='rotate(-90 48,190)'>coût total (€)</text>")
    # usinage : droite depuis 0
    p.append(f"<line x1='{ox}' y1='{oy}' x2='640' y2='90' stroke='{ALESAGE}' stroke-width='2.6'/>")
    p.append(_txt(650, 92, "usinage", 12, ALESAGE, "start", True))
    p.append(_txt(650, 110, "46 €/pièce", 10, FIN, "start"))
    # fonderie : depuis outillage
    p.append(f"<line x1='{ox}' y1='215' x2='640' y2='150' stroke='{ARBRE}' stroke-width='2.6'/>")
    p.append(_txt(650, 152, "fonderie", 12, ARBRE, "start", True))
    p.append(_txt(650, 170, "8 500 € + 7 €/pièce", 10, FIN, "start"))
    p.append(f"<line x1='{ox}' y1='215' x2='{ox}' y2='{oy}' stroke='{ARBRE}' stroke-width='1.4' stroke-dasharray='4 3'/>")
    p.append(_txt(ox - 8, 212, "outillage", 10, ARBRE, "end"))
    # croisement
    p.append(f"<circle cx='265' cy='222' r='7' fill='{ALERTE}'/>")
    p.append(f"<line x1='265' y1='222' x2='265' y2='{oy}' stroke='{ALERTE}' stroke-width='1.4' stroke-dasharray='4 3'/>")
    p.append(_txt(265, 318, "≈ 218 pièces", 11, ALERTE, "middle", True))
    p.append(_txt(175, 150, "on usine", 11, ALESAGE, "middle", True))
    p.append(_txt(450, 250, "on moule", 11, ARBRE, "middle", True))
    p.append(f"<rect x='40' y='345' width='680' height='48' fill='#f0fdf4' stroke='{OK}' rx='6'/>")
    p.append(_txt(56, 367, "Le seuil se calcule : 46 N = 8 500 + 7 N → N = 218. En dessous on usine, au-dessus on moule.",
                  12, TRAIT, "start", True))
    p.append(_txt(56, 386, "C'est le premier calcul à faire avant de choisir un procédé.", 11, FIN))
    return _svg("".join(p), 760, 405)


# ===========================================================================
# 42. LA STRUCTURE D'UN DOSSIER ET D'UNE SOUTENANCE
# ===========================================================================

def structure_soutenance():
    p = [_txt(40, 26, "20 minutes de soutenance, 15 diapositives maximum :", 13, TRAIT, "start", True)]
    parties = [("Le besoin en une phrase", 1, ALESAGE),
               ("Cahier des charges : 4 exigences chiffrées", 2, ALESAGE),
               ("Solutions comparées + tableau de choix", 3, ARBRE),
               ("La solution retenue, en image", 3, ARBRE),
               ("Deux ou trois points techniques approfondis", 6, OK),
               ("Réalisation et essais MESURÉS", 4, OK),
               ("Bilan honnête et perspectives", 2, FIN)]
    total = sum(d for _, d, _ in parties)
    ox, largeur = 60, 640
    x = ox
    p.append(_txt(40, 60, "Répartition du temps :", 12, FIN, "start", True))
    for nom, duree, couleur in parties:
        w = duree * largeur / total
        p.append(f"<rect x='{x}' y='70' width='{w - 3}' height='30' rx='4' fill='{couleur}' opacity='0.55'/>")
        p.append(_txt(x + w / 2, 90, f"{duree}′", 11, TRAIT, "middle", True))
        x += w
    y = 130
    for nom, duree, couleur in parties:
        p.append(f"<circle cx='72' cy='{y - 4}' r='6' fill='{couleur}'/>")
        p.append(_txt(90, y, nom, 12, TRAIT))
        y += 26
    p.append(f"<rect x='40' y='305' width='680' height='90' fill='#eff6ff' stroke='{ALESAGE}' rx='6'/>")
    p.append(_txt(56, 328, "Les trois questions qui tombent toujours :", 12, TRAIT, "start", True))
    p.append(_txt(56, 350, "• pourquoi ce choix plutôt qu'un autre ?", 11, FIN))
    p.append(_txt(56, 368, "• comment avez-vous vérifié que ça fonctionne ?", 11, FIN))
    p.append(_txt(56, 386, "• que feriez-vous différemment si c'était à refaire ?", 11, FIN))
    return _svg("".join(p), 760, 410)


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
    "bete_a_cornes": ("La bête à cornes : cadrer le besoin", bete_a_cornes),
    "diagramme_pieuvre": ("Le diagramme pieuvre : FP et FC", diagramme_pieuvre),
    "diagramme_fast": ("Le FAST : de la fonction au composant", diagramme_fast),
    "elements_cotation": ("Les éléments d'une cote", elements_cotation),
    "lettres_et_grades": ("Lettre = position, chiffre = largeur", lettres_et_grades),
    "defaut_geometrique": ("Bonnes cotes, pièce inutilisable", defaut_geometrique),
    "cadre_tolerance": ("Lire un cadre de tolérance géométrique", cadre_tolerance),
    "chaine_de_cotes": ("La chaîne de cotes", chaine_de_cotes),
    "courbe_traction": ("L'essai de traction : Re, Rm et E", courbe_traction),
    "resistance_vs_rigidite": ("Résistance et rigidité : deux choses différentes", resistance_vs_rigidite),
    "decoder_designation": ("Décoder une désignation normalisée", decoder_designation),
    "peau_dure_coeur_tenace": ("Cémentation : peau dure, cœur tenace", peau_dure_coeur_tenace),
    "isoler_et_couper": ("Isoler et couper : l'effort intérieur", isoler_et_couper),
    "quatre_sollicitations": ("Les quatre sollicitations simples", quatre_sollicitations),
    "fibres_flexion": ("Flexion : fibre tendue, fibre comprimée", fibres_flexion),
    "concentration_contrainte": ("Pourquoi les pièces cassent aux angles vifs", concentration_contrainte),
    "esquisse_contraintes": ("Esquisse sous-contrainte ou totalement contrainte", esquisse_contraintes),
    "arbre_de_creation": ("L'arbre de création : l'ordre compte", arbre_de_creation),
    "formats_echange": ("Les formats d'échange CAO", formats_echange),
    "isostatique_hyperstatique": ("Palier fixe et palier libre", isostatique_hyperstatique),
    "regle_des_charges": ("Quelle bague monter serrée ?", regle_des_charges),
    "liaison_arbre_moyeu": ("Transmettre le couple : quatre solutions", liaison_arbre_moyeu),
    "calcul_ajustement_etapes": ("Calculer un ajustement en quatre étapes", calcul_ajustement_etapes),
    "choisir_materiau": ("Choisir un matériau : l'ordre des questions", choisir_materiau),
    "decomposer_force": ("Décomposer une force en deux composantes", decomposer_force),
    "profil_trapezoidal": ("Le profil de vitesse trapézoïdal", profil_trapezoidal),
    "courbe_capabilite": ("Courbe en cloche, Cp et Cpk", courbe_capabilite),
    "effort_verin": ("L'effort d'un vérin en poussée et en traction", effort_verin),
    "plaque_moteur": ("Lire une plaque signalétique de moteur", plaque_moteur),
    "planning_projet": ("Planning de projet et chemin critique", planning_projet),
    "seuil_rentabilite": ("Le seuil de rentabilité entre deux procédés", seuil_rentabilite),
    "structure_soutenance": ("Structure d'une soutenance de 20 minutes", structure_soutenance),
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
