# -*- coding: utf-8 -*-
# BROUILLON — fiche 1.9 « Lire un diagramme SysML » (référentiel S1.1, en lecture). Rien de ceci n'est encore dans
# app.py.
#
# Sources de la notation (vérifiées) :
# - spécification OMG SysML 1.6 (formal/19-11-01, novembre 2019, omg.org/spec/SysML/1.6) :
#   * en-tête de cadre : « diagramKind [modelElementType] modelElementName [diagramName] », diagramKind en gras ;
#   * abréviations : req, uc, bdd, ibd, sd, stm (et act, par, pkg : neuf types en tout) ;
#   * dépendances (satisfy, include…) : trait pointillé à pointe OUVERTE (règle UML reprise par SysML, non relue
#     dans le texte extrait, cohérente avec « allocate … dashed line with an open arrow head ») ; la pointe noire
#     pleine est réservée au flux d'éléments ;
#   * exigence «requirement» avec id et texte ; relations containment, deriveReqt, satisfy, verify, refine, copy,
#     trace ; «satisfy» va de l'élément de conception vers l'exigence, «verify» du cas de test vers l'exigence,
#     «deriveReqt» de l'exigence dérivée vers l'exigence source ;
#   * bdd : une partie (part property) se note par un losange noir sur l'association ;
#   * ibd : partie = boîte en trait plein, propriété de référence = trait pointillé, flux d'éléments (item flow) =
#     pointe de flèche noire sur le connecteur, dirigée vers la cible ;
# - les diagrammes de cas d'utilisation, de séquence et d'états réutilisent la notation UML (SysML 1.6, §4 :
#   sous-ensemble « UML4SysML ») : acteur, ellipse, «include» / «extend» ; ligne de vie, message ; état arrondi,
#   état initial (disque noir), état final, transition « événement [garde] / effet ».
# - Le portail coulissant et ses exigences sont un EXEMPLE PÉDAGOGIQUE (données d'énoncé), pas un produit réel.
import math

# ===========================================================================
# 1. FIGURES
# ===========================================================================

def _sy_cadre(p, x, y, w, h, entete):
    """Cadre SysML : rectangle et étiquette à coin coupé en haut à gauche (en-tête du diagramme)."""
    p.append(f"<rect x='{x}' y='{y}' width='{w}' height='{h}' fill='#ffffff' stroke='{TRAIT}' stroke-width='1.4'/>")
    lg = 9 + 6.3 * len(entete)
    p.append(f"<path d='M {x} {y} L {x + lg} {y} L {x + lg} {y + 14} L {x + lg - 10} {y + 24} L {x} {y + 24} Z' "
             f"fill='#f1f5f9' stroke='{TRAIT}' stroke-width='1.2'/>")
    ab, _, reste = entete.partition(" ")
    p.append(_txt(x + 6, y + 16, f"<tspan font-weight='700'>{ab}</tspan> {reste}", 11, TRAIT, "start"))


def _sy_bloc(p, x, y, w, h, nom, mot="«block»", couleur=ALESAGE, lignes=()):
    p.append(f"<rect x='{x}' y='{y}' width='{w}' height='{h}' fill='#ffffff' stroke='{couleur}' stroke-width='1.6'/>")
    p.append(_txt(x + w / 2, y + 14, mot, 9, FIN, "middle"))
    p.append(_txt(x + w / 2, y + 28, nom, 11, couleur, "middle", True))
    for i, t in enumerate(lignes):
        if i == 0:
            p.append(f"<line x1='{x}' y1='{y + 36}' x2='{x + w}' y2='{y + 36}' stroke='{couleur}' stroke-width='0.8'/>")
        p.append(_txt(x + 6, y + 50 + 13 * i, t, 9, TRAIT, "start"))


def sysml_panorama():
    p = [_txt(30, 24, "Les six diagrammes SysML à savoir lire, et la question à laquelle chacun répond", 13, TRAIT, "start", True)]
    cases = (("req", "EXIGENCES", "Que doit faire le système,", "et avec quelles performances ?", ARBRE),
             ("uc", "CAS D'UTILISATION", "Qui s'en sert,", "et pour faire quoi ?", ARBRE),
             ("bdd", "DÉFINITION DE BLOCS", "De quoi est-il composé ?", "(nomenclature)", ALESAGE),
             ("ibd", "BLOCS INTERNES", "Comment les blocs sont-ils reliés,", "qu'est-ce qui circule ?", ALESAGE),
             ("sd", "SÉQUENCE", "Dans quel ordre les éléments", "échangent-ils des messages ?", OK),
             ("stm", "ÉTATS-TRANSITIONS", "Dans quels états peut-il être,", "qu'est-ce qui le fait changer ?", OK))
    for k, (ab, nom, q1, q2, c) in enumerate(cases):
        x = 30 + (k % 3) * 245
        y = 44 + (k // 3) * 120
        p.append(f"<rect x='{x}' y='{y}' width='230' height='104' rx='8' fill='#ffffff' stroke='{c}' stroke-width='1.8'/>")
        p.append(f"<path d='M {x} {y} L {x + 44} {y} L {x + 44} {y + 12} L {x + 36} {y + 20} L {x} {y + 20} Z' fill='#f1f5f9' stroke='{c}'/>")
        p.append(_txt(x + 6, y + 15, ab, 11, c, "start", True))
        p.append(_txt(x + 115, y + 42, nom, 11, c, "middle", True))
        p.append(_txt(x + 115, y + 66, q1, 10, TRAIT, "middle"))
        p.append(_txt(x + 115, y + 80, q2, 10, TRAIT, "middle"))
    p.append(_txt(30, 304, "Orange : le besoin (exigences, usages) · Bleu : la structure (composition, liaisons) · Vert : le comportement (déroulement, états).", 10, FIN))
    p.append(f"<rect x='30' y='314' width='720' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 336, "Au BTS CPI, ces diagrammes sont FOURNIS : on les lit, on les exploite, on peut avoir à les compléter.", 12, TRAIT, "start", True))
    return _svg("".join(p), 780, 360)


def _sy_fleche(p, x1, y1, x2, y2, couleur, pointilles=False, larg=1.3):
    """Flèche à pointe OUVERTE (deux traits), comme en UML/SysML pour les dépendances, messages et transitions."""
    tir = " stroke-dasharray='5 3'" if pointilles else ""
    p.append(f"<line x1='{x1:.1f}' y1='{y1:.1f}' x2='{x2:.1f}' y2='{y2:.1f}' stroke='{couleur}' stroke-width='{larg}'{tir}/>")
    a = math.atan2(y2 - y1, x2 - x1)
    for s in (1, -1):
        xa = x2 - 9 * math.cos(a + s * 0.45)
        ya = y2 - 9 * math.sin(a + s * 0.45)
        p.append(f"<line x1='{x2:.1f}' y1='{y2:.1f}' x2='{xa:.1f}' y2='{ya:.1f}' stroke='{couleur}' stroke-width='{larg}'/>")


def _sy_flux(p, x1, y1, x2, y2):
    """Connecteur d'ibd portant un flux d'éléments : pointe noire pleine au milieu, vers la cible."""
    p.append(f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{TRAIT}' stroke-width='1.4'/>")
    xm, ym = (x1 + x2) / 2, (y1 + y2) / 2
    a = math.atan2(y2 - y1, x2 - x1)
    pts = [(xm + 6 * math.cos(a), ym + 6 * math.sin(a)),
           (xm - 5 * math.cos(a) - 6 * math.sin(a), ym - 5 * math.sin(a) + 6 * math.cos(a)),
           (xm - 5 * math.cos(a) + 6 * math.sin(a), ym - 5 * math.sin(a) - 6 * math.cos(a))]
    p.append("<polygon points='" + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f"' fill='{TRAIT}'/>")


def _sy_port(p, x, y):
    p.append(f"<rect x='{x - 4}' y='{y - 4}' width='8' height='8' fill='#ffffff' stroke='{TRAIT}' stroke-width='1.2'/>")


def sysml_exigences():
    p = [_txt(30, 24, "Diagramme d'exigences : ce que le système DOIT faire, avec des valeurs à respecter", 13, TRAIT, "start", True)]
    _sy_cadre(p, 20, 40, 750, 300, "req [package] Exigences du portail")

    def exi(x, y, ident, nom, texte, w):
        p.append(f"<rect x='{x}' y='{y}' width='{w}' height='74' fill='#fff7ed' stroke='{ARBRE}' stroke-width='1.6'/>")
        p.append(_txt(x + w / 2, y + 14, "«requirement»", 9, FIN, "middle"))
        p.append(_txt(x + w / 2, y + 28, nom, 11, ARBRE, "middle", True))
        p.append(f"<line x1='{x}' y1='{y + 34}' x2='{x + w}' y2='{y + 34}' stroke='{ARBRE}' stroke-width='0.8'/>")
        p.append(_txt(x + 6, y + 48, f'id = "{ident}"', 9, TRAIT, "start"))
        p.append(_txt(x + 6, y + 62, f'text = "{texte}"', 9, TRAIT, "start"))
    exi(280, 76, "1", "Ouvrir le portail", "Le portail s'ouvre sur commande", 210)
    exi(34, 210, "1.1", "Durée d'ouverture", "Ouverture complète en 20 s au plus", 236)
    exi(280, 210, "1.2", "Sécurité", "Arrêt si un obstacle est détecté", 236)
    exi(526, 210, "1.3", "Commande à distance", "Commande depuis 30 m au moins", 236)
    # contenance : traits reliés à un cercle marqué d'une croix, côté exigence mère
    for xe in (152, 398, 644):
        p.append(f"<line x1='{xe}' y1='210' x2='385' y2='162' stroke='{TRAIT}' stroke-width='1.2'/>")
    p.append(f"<circle cx='385' cy='156' r='6' fill='#ffffff' stroke='{TRAIT}' stroke-width='1.2'/>")
    p.append(f"<line x1='379' y1='156' x2='391' y2='156' stroke='{TRAIT}'/><line x1='385' y1='150' x2='385' y2='162' stroke='{TRAIT}'/>")
    p.append(_txt(500, 150, "contenance (cercle à croix, côté mère) :", 9, FIN, "start"))
    p.append(_txt(500, 162, "l'exigence 1 contient 1.1, 1.2 et 1.3", 9, FIN, "start"))
    # «satisfy» : du bloc vers l'exigence 1.1
    p.append(f"<rect x='50' y='80' width='160' height='44' fill='#ffffff' stroke='{ALESAGE}' stroke-width='1.6'/>")
    p.append(_txt(130, 96, "«block»", 9, FIN, "middle"))
    p.append(_txt(130, 112, "Motoréducteur", 11, ALESAGE, "middle", True))
    p.append(_txt(124, 150, "élément de", 9, FIN, "end"))
    p.append(_txt(124, 162, "conception", 9, FIN, "end"))
    _sy_fleche(p, 130, 124, 130, 208, ALESAGE, True, 1.4)
    p.append(_txt(138, 160, "«satisfy»", 9, ALESAGE, "start", True))
    p.append(_txt(138, 174, "le bloc satisfait 1.1", 9, ALESAGE, "start"))
    p.append(_txt(40, 316, "Exemple pédagogique (valeurs d'énoncé). Une exigence = un identifiant + un texte vérifiable.", 10, FIN))
    p.append(f"<rect x='30' y='350' width='720' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 372, "Flèche pointillée «satisfy» : du bloc VERS l'exigence qu'il satisfait (il la « montre du doigt »).", 12, TRAIT, "start", True))
    return _svg("".join(p), 790, 396)


def sysml_bdd():
    p = [_txt(30, 24, "Diagramme de définition de blocs (bdd) : de quoi le système est composé", 13, TRAIT, "start", True)]
    _sy_cadre(p, 20, 40, 750, 300, "bdd [block] Portail motorisé")
    _sy_bloc(p, 300, 70, 180, 50, "Portail motorisé")
    p.append(_txt(490, 92, "le tout", 9, FIN, "start"))
    enfants = ((34, 85, "Vantail", "1"), (127, 115, "Motoréducteur", "1"), (250, 125, "Carte de commande", "1"),
               (383, 105, "Galet de guidage", "4"), (496, 120, "Capteur d'obstacle", "1"),
               (624, 140, "Capteur fin de course", "2"))
    for x, w, nom, mult in enfants:
        _sy_bloc(p, x, 220, w, 50, nom)
        xm = x + w / 2
        p.append(f"<line x1='{xm}' y1='220' x2='390' y2='136' stroke='{TRAIT}' stroke-width='1.2'/>")
        p.append(_txt(xm + 6, 212, mult, 11, ALERTE, "start", True))
    p.append(_txt(36, 200, "les morceaux", 9, FIN, "start"))
    # losange noir côté bloc composé (le tout)
    p.append(f"<polygon points='390,120 384,128 390,136 396,128' fill='{TRAIT}'/>")
    p.append(_txt(404, 132, "losange noir, collé au tout = « est composé de »", 9, FIN, "start"))
    _sy_bloc(p, 124, 296, 120, 40, "Moteur")
    p.append(f"<line x1='184' y1='286' x2='184' y2='296' stroke='{TRAIT}' stroke-width='1.2'/>")
    p.append(f"<polygon points='184,270 178,278 184,286 190,278' fill='{TRAIT}'/>")
    p.append(_txt(190, 294, "1", 11, ALERTE, "start", True))
    p.append(_txt(270, 300, "Les nombres en rouge (multiplicités) : combien d'exemplaires de chaque bloc.", 9, ALERTE, "start", True))
    p.append(f"<rect x='30' y='350' width='720' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 372, "Lecture : un portail = 1 vantail, 1 motoréducteur (qui contient 1 moteur), 1 carte, 4 galets, 1 + 2 capteurs.", 11, TRAIT, "start", True))
    return _svg("".join(p), 790, 396)


def sysml_ibd():
    p = [_txt(30, 24, "Diagramme de blocs internes (ibd) : comment les blocs sont reliés, et ce qui circule", 13, TRAIT, "start", True)]
    _sy_cadre(p, 20, 40, 750, 290, "ibd [block] Portail motorisé")
    parts = ((120, 150, 60, "carte : Carte de commande"), (350, 150, 60, "motoréducteur : Motoréducteur"),
             (585, 150, 60, "vantail : Vantail"), (120, 250, 46, "capteur : Capteur d'obstacle"))
    for x, y, h, nom in parts:
        p.append(f"<rect x='{x}' y='{y}' width='165' height='{h}' fill='#ffffff' stroke='{ALESAGE}' stroke-width='1.6'/>")
        p.append(_txt(x + 82.5, y + h / 2 + 4, nom, 9, ALESAGE, "middle", True))
    # ports sur les bords des parties et du cadre
    for x, y in ((285, 180), (350, 180), (515, 180), (585, 180), (120, 166), (120, 194), (202, 210), (202, 250),
                 (20, 166), (20, 194)):
        _sy_port(p, x, y)
    # flux d'éléments
    _sy_flux(p, 289, 180, 346, 180)
    p.append(_txt(317, 144, "énergie électrique", 9, ARBRE, "middle", True))
    _sy_flux(p, 519, 180, 581, 180)
    p.append(_txt(550, 144, "mouvement (couple)", 9, ARBRE, "middle", True))
    _sy_flux(p, 24, 166, 116, 166)
    p.append(_txt(70, 158, "ordre radio", 9, ARBRE, "middle", True))
    _sy_flux(p, 24, 194, 116, 194)
    p.append(_txt(70, 210, "énergie électrique", 9, ARBRE, "middle", True))
    p.append(_txt(70, 222, "(réseau)", 9, ARBRE, "middle"))
    _sy_flux(p, 202, 246, 202, 214)
    p.append(_txt(210, 234, "présence d'obstacle", 9, ARBRE, "start", True))
    # libellés de rôle
    p.append(_txt(66, 244, "venus de l'extérieur", 8, FIN, "middle"))
    p.append(_txt(66, 254, "(télécommande,", 8, FIN, "middle"))
    p.append(_txt(66, 264, "réseau)", 8, FIN, "middle"))
    p.append(_txt(667, 226, "partie « nom : Bloc »", 9, FIN, "middle"))
    p.append(_txt(285, 224, "port", 9, FIN, "middle"))
    p.append(_txt(318, 198, "connecteur", 8, FIN, "middle"))
    p.append(_txt(310, 300, "Pointe noire sur un connecteur = ce qui circule, vers le bloc qui reçoit.", 10, FIN))
    p.append(f"<rect x='30' y='340' width='720' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 362, "Le bdd dit « de quoi c'est fait » ; l'ibd dit « comment c'est branché » : énergie, matière, information.", 12, TRAIT, "start", True))
    return _svg("".join(p), 790, 386)


def sysml_comportement():
    p = [_txt(30, 24, "Cas d'utilisation, séquence, états : qui s'en sert, dans quel ordre, dans quel état", 13, TRAIT, "start", True)]
    # ---- uc
    _sy_cadre(p, 20, 40, 240, 290, "uc [package] Usages")
    p.append(f"<rect x='90' y='80' width='160' height='220' fill='none' stroke='{FIN}' stroke-width='1.2'/>")
    p.append(_txt(170, 96, "frontière : Portail motorisé", 8, FIN, "middle", True))
    cx, cy = 50, 170
    p.append(f"<circle cx='{cx}' cy='{cy - 22}' r='8' fill='none' stroke='{TRAIT}' stroke-width='1.4'/>")
    p.append(f"<line x1='{cx}' y1='{cy - 14}' x2='{cx}' y2='{cy + 8}' stroke='{TRAIT}' stroke-width='1.4'/>")
    p.append(f"<line x1='{cx - 10}' y1='{cy - 6}' x2='{cx + 10}' y2='{cy - 6}' stroke='{TRAIT}' stroke-width='1.4'/>")
    p.append(f"<line x1='{cx}' y1='{cy + 8}' x2='{cx - 8}' y2='{cy + 22}' stroke='{TRAIT}' stroke-width='1.4'/>")
    p.append(f"<line x1='{cx}' y1='{cy + 8}' x2='{cx + 8}' y2='{cy + 22}' stroke='{TRAIT}' stroke-width='1.4'/>")
    p.append(_txt(cx, cy + 36, "Utilisateur", 9, TRAIT, "middle", True))
    p.append(_txt(cx, cy + 48, "(acteur)", 8, FIN, "middle"))
    for y, t in ((130, "Ouvrir"), (190, "Fermer")):
        p.append(f"<ellipse cx='175' cy='{y}' rx='55' ry='18' fill='#fff7ed' stroke='{ARBRE}' stroke-width='1.4'/>")
        p.append(_txt(175, y + 4, t, 10, ARBRE, "middle", True))
        p.append(f"<line x1='{cx + 10}' y1='{cy - 6}' x2='120' y2='{y}' stroke='{TRAIT}'/>")
    p.append(_txt(175, 164, "(cas d'utilisation)", 8, FIN, "middle"))
    p.append(f"<ellipse cx='175' cy='262' rx='62' ry='18' fill='#fff7ed' stroke='{ARBRE}' stroke-width='1.4'/>")
    p.append(_txt(175, 266, "Détecter obstacle", 9, ARBRE, "middle", True))
    _sy_fleche(p, 175, 208, 175, 243, TRAIT, True, 1.2)
    p.append(_txt(181, 224, "«include»", 8, FIN, "start", True))
    p.append(_txt(181, 236, "Fermer inclut", 8, FIN, "start"))
    p.append(_txt(170, 294, "toujours Détecter obstacle", 8, FIN, "middle"))
    # ---- sd
    _sy_cadre(p, 270, 40, 250, 290, "sd [interaction] Ouvrir")
    for x, n in ((304, "utilisateur"), (364, "carte"), (424, "motoréd."), (486, "capteur FdC")):
        p.append(f"<rect x='{x - 29}' y='74' width='58' height='22' fill='#ffffff' stroke='{OK}'/>")
        p.append(_txt(x, 89, n, 8, OK, "middle", True))
        p.append(f"<line x1='{x}' y1='96' x2='{x}' y2='304' stroke='{FIN}' stroke-dasharray='4 3'/>")
    p.append(_txt(334, 110, "message", 8, FIN, "middle"))
    for x1, x2, y, t in ((304, 364, 134, "appuyer()"), (364, 424, 174, "démarrer(sens)"),
                         (486, 364, 220, "finDeCourse()"), (364, 424, 260, "arrêter()")):
        _sy_fleche(p, x1, y, x2, y, TRAIT, False, 1.3)
        p.append(_txt((x1 + x2) / 2, y - 6, t, 8, TRAIT, "middle"))
    p.append(_txt(308, 296, "ligne de vie", 8, FIN, "start"))
    p.append(_txt(395, 320, "le temps descend ↓", 8, FIN, "middle"))
    # ---- stm
    _sy_cadre(p, 530, 40, 240, 290, "stm [state machine] Portail")
    p.append(f"<circle cx='548' cy='90' r='6' fill='{TRAIT}'/>")
    p.append(_txt(558, 84, "état initial", 8, FIN, "start"))
    _sy_fleche(p, 552, 95, 566, 102, TRAIT, False, 1.2)
    for x, y, n in ((556, 102, "Fermé"), (650, 172, "En ouverture"), (556, 236, "Ouvert")):
        p.append(f"<rect x='{x}' y='{y}' width='86' height='30' rx='12' fill='#f0fdf4' stroke='{OK}' stroke-width='1.4'/>")
        p.append(_txt(x + 43, y + 19, n, 9, OK, "middle", True))
    p.append(_txt(599, 146, "(état)", 8, FIN, "middle"))
    _sy_fleche(p, 642, 124, 680, 170, TRAIT, False, 1.2)
    p.append(_txt(662, 118, "appui [aucun obstacle]", 8, TRAIT, "start", True))
    p.append(_txt(662, 130, "/ démarrer moteur", 8, TRAIT, "start"))
    p.append(_txt(668, 148, "(transition)", 8, FIN, "start"))
    _sy_fleche(p, 680, 202, 630, 236, TRAIT, False, 1.2)
    p.append(_txt(676, 224, "fin de course", 8, TRAIT, "start", True))
    p.append(_txt(676, 236, "/ arrêter moteur", 8, TRAIT, "start"))
    p.append(_txt(540, 284, "Simplifié : la fermeture n'est pas représentée.", 8, FIN, "start"))
    p.append(_txt(540, 300, "transition :", 8, FIN, "start"))
    p.append(_txt(540, 312, "événement [garde] / effet", 8, FIN, "start", True))
    p.append(f"<rect x='30' y='340' width='740' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 362, "uc : qui fait quoi · sd : l'ordre des messages (de haut en bas) · stm : les états et ce qui fait passer de l'un à l'autre.", 11, TRAIT))
    return _svg("".join(p), 790, 386)


FIGURES_NOUVELLES = {
    "sysml_panorama": ("Les six diagrammes SysML et leur question", sysml_panorama),
    "sysml_exigences": ("Diagramme d'exigences (req)", sysml_exigences),
    "sysml_bdd": ("Diagramme de définition de blocs (bdd)", sysml_bdd),
    "sysml_ibd": ("Diagramme de blocs internes (ibd)", sysml_ibd),
    "sysml_comportement": ("Cas d'utilisation, séquence et états (uc, sd, stm)", sysml_comportement),
}

# ===========================================================================
# 2. FICHE 1.9 — en FIN de bloc 1 (après la 1.8)
# ===========================================================================

FICHE_1_9 = {
    "id": "1.9",
    "titre": "Lire un diagramme SysML : exigences, blocs, cas d'utilisation, séquence, états",
    "duree": "4 h",
    "cours": """### 1. Pourquoi cette fiche

Dans un sujet de BTS CPI, le système étudié est souvent décrit par des **diagrammes SysML** (*Systems Modeling
Language*). Le référentiel le dit clairement (S1.1) : ces diagrammes sont une **donnée d'entrée** de l'étude, et
« on se limitera à la lecture et la compréhension des diagrammes SysML ». Cette fiche apprend donc à **lire**
et à **exploiter** un diagramme fourni. Le référentiel n'exige pas d'en créer un de toutes pièces, mais un sujet
peut demander de le compléter ou de le modifier (S1.1.3 : « décoder ou modifier ces différents diagrammes
SysML »).

SysML est un langage normalisé par l'**OMG** (*Object Management Group*, un organisme international qui publie
la norme) ; la notation de cette fiche suit sa spécification officielle.

*Image à garder : un dessin technique montre la même pièce en vue de face, de dessus et en coupe ; aucune vue ne
suffit seule, c'est leur ensemble qui décrit la pièce. SysML fait pareil pour un système : plusieurs diagrammes
du même système, chacun répondant à une question.*

**Les mots à connaître, en français courant :**

| Mot | En français courant |
|---|---|
| **bloc** | un constituant (pièce, sous-ensemble, carte électronique, logiciel) : une **référence** |
| **partie** | un **exemplaire** d'un bloc, monté à une place précise du système |
| **multiplicité** | combien d'exemplaires (la colonne « Nb » d'une nomenclature) |
| **port** | un point de branchement : prise, bornier, arbre de sortie |
| **connecteur** | le trait qui relie deux ports : un câble, un arbre, une liaison radio |
| **flux d'éléments** | ce qui circule sur un connecteur : énergie, matière, information |
| **ligne de vie** | la « colonne » d'un élément dans un scénario ; elle descend avec le temps |
| **garde** | une condition qui doit être vraie pour qu'un changement d'état ait lieu |

**Pour se repérer avec ce que vous connaissez déjà** (correspondances approximatives, pas des équivalences) :
bête à cornes et pieuvre → **uc** (qui utilise le système, pour quoi) ; critère et niveau du cahier des charges →
**req** (une exigence chiffrée) ; nomenclature → **bdd** ; chaîne d'énergie et d'information → **ibd**.

*Pour un concepteur, l'enjeu est simple : comprendre le système avant de dessiner ses pièces — savoir ce qu'il
doit faire (les exigences), de quoi il est fait (les blocs) et comment il fonctionne (le comportement).*

### 2. Les six diagrammes, et la question de chacun

[[FIG:sysml_panorama]]

| Diagramme | Abréviation | La question à laquelle il répond |
|---|---|---|
| exigences | **req** | Que doit faire le système, avec quelles performances ? |
| cas d'utilisation | **uc** | Qui s'en sert, et pour faire quoi ? |
| définition de blocs | **bdd** | De quoi est-il composé ? |
| blocs internes | **ibd** | Comment ses blocs sont-ils reliés, et qu'est-ce qui circule entre eux ? |
| séquence | **sd** | Dans quel ordre les éléments échangent-ils des messages ? |
| états-transitions | **stm** | Dans quels états peut-il être, et qu'est-ce qui le fait changer d'état ? |

*SysML compte neuf types de diagrammes ; trois ne sont pas au programme du BTS CPI : activité (act),
paramétrique (par) et paquetage (pkg).*

**Premier réflexe : lire l'en-tête.** Chaque diagramme est dans un **cadre** ; dans l'étiquette à coin coupé en
haut à gauche, on lit d'abord **l'abréviation** (en gras : req, bdd…), puis, entre crochets et parfois omis, le
type d'élément décrit, puis son nom. Exemple : « **bdd** [block] Portail motorisé » = diagramme de définition de blocs du bloc « Portail
motorisé ». En trois mots, on sait de quoi parle le diagramme. Entre crochets, le type de ce qui est décrit :
[block] = un constituant, [package] = un « classeur » qui regroupe des éléments, [interaction] = un scénario
d'échanges, [state machine] = une machine à états. Ce mot entre crochets est secondaire et peut être omis :
l'abréviation et le nom suffisent pour s'orienter.

*Tous les exemples de cette fiche décrivent le même système fictif, un portail coulissant motorisé (valeurs
d'énoncé).*

### 3. Le diagramme d'exigences (req) : ce que le système DOIT faire

[[FIG:sysml_exigences]]

**Comment le lire.**
- Chaque **exigence** est un rectangle marqué «requirement», avec un **identifiant** (id) et un **texte**. Le
  texte dit ce qui doit être obtenu, souvent avec une valeur : « Ouverture complète en 20 s au plus ».
- **Contenance** : un trait terminé par un petit cercle marqué d'une croix, côté exigence « mère », signifie
  qu'elle **contient** les exigences plus détaillées (1 contient 1.1, 1.2, 1.3). On lit de haut en bas, du
  général au détail.
- Les **relations** sont des flèches en pointillé, avec un mot-clé. **Règle unique : la flèche pointe vers
  l'exigence de référence** — l'élément qui la satisfait, le test qui la vérifie, l'exigence qui en est déduite,
  tous la « montrent du doigt » :
  - «**satisfy**» : un **élément de conception** (une solution retenue, ici un bloc) **satisfait** l'exigence —
    la flèche va du bloc vers l'exigence (« le motoréducteur satisfait la durée d'ouverture ») ;
  - «**verify**» : un cas de test **vérifie** l'exigence — la flèche va du test vers l'exigence (un essai
    chronométré d'ouverture vérifierait l'exigence 1.1) ;
  - «**deriveReqt**» : une exigence est **déduite** d'une autre — la flèche va de l'exigence dérivée vers
    l'exigence source (pour un vantail de 4 m, « vitesse du vantail au moins 0,2 m/s » se déduit de
    « ouverture en 20 s au plus » : 4 m ÷ 20 s = 0,2 m/s) ;
  - d'autres mots-clés existent («refine», «trace», «copy») : si vous en croisez un, lisez-le comme un lien
    entre deux éléments dont le mot-clé dit la nature ; inutile de les apprendre.

**Pourquoi c'est le diagramme le plus utile au concepteur** : c'est le **cahier des charges** sous forme de
schéma. Chaque exigence chiffrée devient un critère de conception et de validation (« 20 s au plus » : le moteur
et le réducteur doivent le permettre ; un essai le vérifiera). C'est la même idée que la caractérisation des
fonctions et le cahier des charges fonctionnel (fiches 1.3 et 1.6) : dans « Ouverture complète en 20 s au plus », le **critère** est la durée d'ouverture et
le **niveau** est 20 s au maximum.

### 4. Le diagramme de définition de blocs (bdd) : de quoi le système est composé

[[FIG:sysml_bdd]]

**Comment le lire.**
- Un **bloc** («block») est un constituant du système : une pièce, un sous-ensemble, une carte, un logiciel.
- Le **losange noir** est collé au **tout** ; les traits partent vers les **morceaux**. On lit en partant du
  losange : « le portail **est composé de** » un vantail, un motoréducteur, une carte de commande…
- Les **nombres** près des blocs (les **multiplicités**) disent **combien** d'exemplaires : « 4 » près du galet =
  4 galets de guidage.
- Un bloc peut lui-même être décomposé : le motoréducteur contient un moteur.

*C'est une **nomenclature** dessinée. Le bdd du portail, transposé :*

| Nb | Désignation |
|---|---|
| 1 | Vantail |
| 1 | Motoréducteur (dont 1 moteur) |
| 1 | Carte de commande |
| 4 | Galet de guidage |
| 1 | Capteur d'obstacle |
| 2 | Capteur de fin de course |

### 5. Le diagramme de blocs internes (ibd) : comment les blocs sont reliés

[[FIG:sysml_ibd]]

**Comment le lire.**
- Le cadre est le système (ici le portail) ; à l'intérieur, chaque **partie** est un rectangle « nom : Bloc »
  (« motoréducteur : Motoréducteur » se lit « l'exemplaire appelé motoréducteur, qui est un Motoréducteur »).
- **Bloc ou partie ?** Un **bloc**, c'est une **référence de catalogue** (« Motoréducteur », comme « Vis CHc
  M8×20 ») ; une **partie**, c'est **un exemplaire monté à une place précise** de ce système (la vis repère 12
  qui tient le carter). Le bdd parle de références, l'ibd parle d'exemplaires montés et branchés.
- Les **ports** sont les petits carrés sur le bord des parties ou du cadre : les points de branchement (une
  prise, un bornier, un arbre de sortie).
- Les **connecteurs** sont les traits qui relient les ports (ou directement les parties) : un câble, un arbre, un engrènement, ou une liaison
  sans contact comme la radio.
- Une **pointe de flèche noire posée sur un connecteur** est un **flux d'éléments** : comme la flèche sur une
  canalisation, elle dit **ce qui circule** et dans quel sens — énergie électrique du réseau vers la carte, puis
  de la carte vers le motoréducteur ; mouvement du motoréducteur vers le vantail ; présence d'obstacle du capteur
  vers la carte ; ordre radio de la télécommande vers la carte. Le réseau et la télécommande sont **hors du
  système étudié** : leurs flux arrivent par des ports posés sur le bord du cadre.

*On y lit la **chaîne d'énergie** (fiche 6.20) : le réseau **alimente**, la carte **distribue**, le
motoréducteur **convertit** (moteur) et **transmet** (réducteur), le vantail est mis en mouvement. Et la
**chaîne d'information** (le trajet des ordres et des mesures) : l'ordre radio et la présence d'obstacle arrivent
à la carte, qui commande le moteur.*

**Au premier coup d'œil :** le **bdd** est un **arbre** — un bloc en haut, ses constituants en dessous, des
losanges noirs, des nombres ; l'**ibd** est un **plan de branchement** — des boîtes rangées DANS le cadre du
système, des petits carrés sur leurs bords, des traits entre eux, des pointes noires, et des noms de la forme
« nom : Bloc ». *Le bdd est la liste des pièces d'un kit ; l'ibd est le schéma de câblage du même kit.*

### 6. Le comportement : cas d'utilisation, séquence, états

[[FIG:sysml_comportement]]

**Diagramme de cas d'utilisation (uc) — qui s'en sert, pour quoi faire.** Un **acteur** (bonhomme) est à
l'extérieur du système ; le rectangle est la **frontière** du système ; chaque **ellipse** est un service rendu
(« Ouvrir », « Fermer »). Un trait relie l'acteur aux services qu'il utilise. Une flèche pointillée «include»
dit qu'un cas en inclut un autre à chaque fois : ici, **fermer** le portail inclut toujours **détecter un
obstacle** — on ne referme jamais sans surveiller le passage. La flèche part du cas qui inclut et pointe vers le
cas inclus. *C'est l'équivalent SysML de la frontière de l'étude et des fonctions de service (bête à cornes,
pieuvre).*

**Diagramme de séquence (sd) — dans quel ordre.** Chaque élément a une **ligne de vie** verticale en
pointillé : elle représente l'élément pendant toute la durée du scénario (d'où « de vie »). Les **messages** sont
des flèches horizontales de l'émetteur vers le récepteur ; **le temps s'écoule de haut en bas**, comme dans un fil
de messages de groupe où chaque colonne est un interlocuteur et le plus ancien message est en haut. Entre
les parenthèses d'un message, ce qui le précise (« démarrer(sens) » = démarrer, dans le sens ouverture ou
fermeture). On lit l'histoire d'un scénario : l'utilisateur appuie, la carte démarre le motoréducteur, le
capteur de fin de course signale la fin de course à la carte, la carte arrête le motoréducteur.

**Diagramme d'états-transitions (stm) — dans quel état.** Les **états** sont des rectangles aux coins arrondis
(« Fermé », « En ouverture », « Ouvert ») ; le **disque noir** est le **pseudo-état initial** : il désigne l'état par lequel le système démarre ; les **flèches** sont les
**transitions**, étiquetées « **événement [garde] / effet** » : l'événement qui déclenche le passage, une
condition entre crochets (facultative), l'**effet** — ce que le système fait au moment où il change d'état
(facultatif). *Exemple : « appui [aucun obstacle] / démarrer moteur ».* On lit : « depuis Fermé, un appui fait
passer En ouverture, **à condition** qu'aucun obstacle ne soit détecté ; au moment du passage, la carte démarre le
moteur ». La garde, c'est comme un gardien à l'entrée : l'événement frappe à la porte, et la transition n'a lieu
que si le gardien dit oui. Si un obstacle est là, l'appui ne fait rien : le portail reste Fermé. *Le diagramme
de la figure est simplifié : la fermeture n'y est pas représentée.*

### 7. SysML et SADT

La fiche 1.5 présente le **SADT** (actigramme). Le référentiel 2016 du BTS CPI ne cite pas le SADT : pour
décrire un système, il demande de lire des diagrammes **SysML** (S1.1). La fiche 1.5 est gardée comme
complément, pas à réviser pour l'examen.

Les deux ne se superposent pas exactement. Sur le portail, un actigramme « Ouvrir le portail » mettrait tout sur
**une seule boîte** : entrée « portail fermé », sortie « portail ouvert » ; en haut, W (énergie électrique) et E
(ordre de l'utilisateur) ; en bas, le mécanisme (motoréducteur, carte). SysML **répartit** ces informations sur
plusieurs diagrammes : les états Fermé → Ouvert sur le **stm**, l'énergie et l'ordre radio comme flux sur l'**ibd**,
le motoréducteur et la carte comme blocs du **bdd**. *Attention : en SADT, l'énergie va en haut, jamais en
entrée ; sur un ibd, elle circule sur un connecteur comme n'importe quel flux. Ce n'est pas une contradiction :
ce sont deux conventions différentes.*

### 8. Les erreurs classiques

1. **Lire le diagramme sans lire l'en-tête** : l'abréviation (req, bdd, ibd…) dit tout de suite de quoi il parle.
2. **Confondre bdd et ibd** : le bdd (un arbre, des losanges, des nombres) dit de quoi le système est
   composé ; l'ibd (des boîtes « nom : Bloc » dans le cadre, des ports, des connecteurs) dit comment ses parties
   sont reliées.
3. **Inverser le sens de «satisfy»** : la flèche part du bloc qui satisfait et pointe vers l'exigence.
4. **Oublier les multiplicités** : « 4 » près d'un bloc, ce sont 4 exemplaires.
5. **Lire un diagramme de séquence de gauche à droite** : le temps descend, on le lit de haut en bas.
6. **Prendre une flèche de transition pour un flux** : dans un stm, la flèche est un changement d'état, pas
   quelque chose qui circule.
7. **Vouloir tout redessiner** : on lit, on exploite, et l'on ne modifie que ce que l'énoncé demande.

### 9. À retenir

- SysML (norme OMG) : diagrammes **fournis** dans le sujet, à **lire** et exploiter (parfois à compléter).
- **req** : exigences (id + texte), contenance (cercle à croix), «satisfy», «verify», «deriveReqt».
- **bdd** : de quoi c'est fait — losange noir « est composé de », multiplicités.
- **ibd** : comment c'est branché — parties, ports, connecteurs, flux (pointe noire sur le connecteur).
- **uc** : acteurs et services ; **sd** : messages, le temps descend ; **stm** : états, transitions
  « événement [garde] / effet ».
- Premier réflexe : **lire l'en-tête du cadre**.
""",
    "formules": """
**En-tête d'un cadre** — abréviation [type d'élément] nom · req · uc · bdd · ibd · sd · stm

**Exigences (req)** — «requirement» : id + texte · contenance : cercle à croix côté exigence mère ·
«satisfy» : bloc → exigence · «verify» : test → exigence · «deriveReqt» : dérivée → source

**Blocs (bdd)** — losange noir = « est composé de » · multiplicité = nombre d'exemplaires

**Blocs internes (ibd)** — partie « nom : Bloc » · port = petit carré sur le bord · connecteur = trait · flux
d'éléments = pointe noire sur le connecteur, vers le bloc qui reçoit

**Comportement** — uc : acteur, ellipse, «include» · sd : lignes de vie, messages, le temps descend · stm : état
arrondi, disque noir initial, transition « événement [garde] / effet »
""",
    "exemple": """
### Cas industriel — Comprendre un système avant d'en dessiner une pièce

**La situation.** Un bureau d'études doit reconcevoir le **support du motoréducteur** d'un portail coulissant
(le système fictif de la fiche). Le dossier fourni par le client contient un diagramme d'exigences, un bdd et un
ibd — pas de plan d'ensemble détaillé.

**Ce que la lecture apprend, diagramme par diagramme.**
- **req** : l'exigence 1.1 (« ouverture complète en 20 s au plus ») est satisfaite par le motoréducteur ;
  l'exigence 1.2 (« arrêt si un obstacle est détecté ») impose que le capteur d'obstacle et la carte agissent sur
  le moteur.
  Le support ne doit gêner ni l'un ni l'autre.
- **bdd** : le motoréducteur est un sous-ensemble qui contient le moteur ; le support n'existe pas encore comme
  bloc : c'est la pièce à créer, rattachée au portail.
- **ibd** : le motoréducteur reçoit l'énergie électrique de la carte et transmet le mouvement au vantail. Le
  support doit donc laisser passer le câble d'alimentation et garder l'alignement entre la sortie du réducteur et
  la crémaillère du vantail (une crémaillère n'est pas dessinée sur l'ibd simplifié de la fiche : c'est le
  dossier complet qui la précise).

**Ce que le cas apprend.** Avant de dessiner la moindre pièce, la lecture des diagrammes SysML donne les
**exigences à respecter** (req), la **place de la pièce dans la nomenclature** (bdd) et les **liaisons et flux à
ne pas couper** (ibd). Ce sont les données d'entrée du cahier des charges de la pièce.
""",
    "exercice": """
### Exercice — Lire le dossier SysML du portail

À partir des figures de la fiche (portail coulissant motorisé, exemple pédagogique) :

**1.** Que signifie l'en-tête « ibd [block] Portail motorisé » ?

**2.** Dans le diagramme d'exigences, quelle est la valeur à respecter pour la durée d'ouverture ? Quel bloc
satisfait cette exigence, et dans quel sens va la flèche «satisfy» ?

**3.** D'après le bdd, combien de galets de guidage le portail comporte-t-il ? Quel symbole indique que le
portail est composé de ces blocs ?

**4.** D'après l'ibd, qu'est-ce qui circule de la carte de commande vers le motoréducteur ? Et du motoréducteur
vers le vantail ?

**5.** Dans le diagramme d'états, depuis l'état « Fermé », quel événement fait passer à « En ouverture » ?

**6.** Dans le diagramme de séquence, quel message la carte envoie-t-elle en premier au motoréducteur ? Comment
sait-on qu'il précède « arrêter() » ?
""",
    "corrige": """
### Corrigé, en six temps

#### 1. Ce que dit l'énoncé

Cinq diagrammes du même système, à lire ; aucune construction demandée.

#### 2. Quelle règle, et pourquoi

> **En-tête** : abréviation [type] nom. **req** : id + texte, «satisfy» du bloc vers l'exigence. **bdd** : losange
> noir = composé de, multiplicité = nombre. **ibd** : pointe noire sur un connecteur = ce qui circule. **stm** :
> transition « événement [garde] / effet ». **sd** : le temps descend.

#### 3. Les conversions

Aucune : c'est une lecture.

#### 4. Le remplacement

On lit chaque diagramme à l'endroit demandé.

#### 5. Le calcul (ici : la lecture)

**1.** Diagramme de **blocs internes** du bloc « Portail motorisé » : il montre comment ses parties sont reliées.

**2.** **20 s au plus** (exigence 1.1). Elle est satisfaite par le **Motoréducteur** ; la flèche «satisfy» va **du
bloc vers l'exigence**.

**3.** **4 galets** (multiplicité 4). Le **losange noir**, côté portail, se lit « est composé de ».

**4.** De la carte vers le motoréducteur : l'**énergie électrique** ; du motoréducteur vers le vantail : le
**mouvement** (couple). Les pointes noires sur les connecteurs indiquent le sens.

**5.** L'événement « **appui** » (sur la télécommande), à condition qu'aucun obstacle ne soit détecté (la garde
[aucun obstacle]) ; l'effet est « démarrer moteur ».

**6.** « **démarrer(sens)** » : il est placé plus haut que « arrêter() » ; dans un diagramme de séquence, le temps
s'écoule de haut en bas.

#### 6. La vérification

**Cohérence entre diagrammes** : le motoréducteur qui satisfait la durée d'ouverture (req) est bien un constituant
du portail (bdd) et reçoit l'énergie de la carte (ibd) : les diagrammes décrivent le même système sous des angles
différents.
""",
}

# ===========================================================================
# 3. MÉTHODE
# ===========================================================================
MTH_1_9 = ("1.9", "Lire un diagramme SysML fourni", [
    "**Lire l'en-tête du cadre** : l'abréviation (req, uc, bdd, ibd, sd, stm) dit quelle question le diagramme traite.",
    "**Identifier les éléments** : exigences (id + texte), blocs, parties et ports, acteurs, lignes de vie, états.",
    "**Lire les liens avec leur sens** : «satisfy» bloc → exigence ; losange noir = composé de ; pointe noire sur un "
    "connecteur = ce qui circule ; messages de haut en bas ; transitions « événement [garde] / effet ».",
    "**Croiser les diagrammes** : le même bloc apparaît dans le req (ce qu'il satisfait), le bdd (où il est) et "
    "l'ibd (ce qu'il reçoit et transmet).",
    "**En tirer les données de conception** : exigences chiffrées, nomenclature, liaisons et flux à respecter.",
], "Portail : l'exigence 1.1 (20 s au plus) est satisfaite par le Motoréducteur (req) ; il fait partie du portail "
   "(bdd) ; il reçoit l'énergie électrique de la carte et transmet le mouvement au vantail (ibd).")

# ===========================================================================
# 4. ATELIERS (fin de liste ATELIERS, après at177)
# ===========================================================================
ATELIERS_NOUVEAUX = [
    {
        "id": "at178",
        "chapitre": "Bloc 1",
        "titre": "Lire les exigences et la composition d'un système (req, bdd)",
        "theme": "Analyse fonctionnelle",
        "fiche": "1.9",
        "figure": "sysml_bdd",
        "vocabulaire": [
            ("Exigence",
             "ce que le système doit faire ou respecter, avec un identifiant et un texte (souvent une valeur)."),
            ("Bloc",
             "un constituant du système (pièce, sous-ensemble, logiciel)."),
            ("Multiplicité",
             "le nombre d'exemplaires d'un bloc, écrit près de lui sur le bdd."),
        ],
        "enonce": "On étudie le dossier SysML du portail coulissant motorisé de la fiche (exemple pédagogique) : un "
                  "diagramme d'exigences (req) et un diagramme de définition de blocs (bdd).",
        "etapes": [
            {"type": "qcm", "label": "L'en-tête",
             "question": "Le cadre porte l'en-tête « bdd [block] Portail motorisé ». Que décrit ce diagramme ?",
             "options": ["De quoi le portail motorisé est composé", "L'ordre des messages échangés",
                         "Les exigences du portail"], "bonne": 0,
             "indice": "bdd = diagramme de définition de blocs : la liste des constituants.",
             "diagnostics": {1: "L'ordre des messages, c'est le diagramme de séquence (sd).",
                             2: "Les exigences sont dans le diagramme d'exigences (req)."}},
            {"type": "numerique", "label": "Nombre de galets",
             "unite": "galets", "attendu": 4, "tol": 0.1,
             "consigne": "Sur le bdd, combien de galets de guidage le portail comporte-t-il ?",
             "indice": "Lis le nombre écrit près du bloc « Galet de guidage ».",
             "pieges": [(1, "1 : c'est la multiplicité du vantail, du motoréducteur ou de la carte. Près du galet, "
                            "on lit 4.")],
             "aide": "Multiplicité 4 : 4 galets."},
            {"type": "numerique", "label": "Nombre total de galets et de capteurs",
             "unite": "pièces", "attendu": 5, "tol": 0.1,
             "consigne": "Combien faut-il commander de galets de guidage et de capteurs d'obstacle au total pour un "
                         "portail ?",
             "indice": "Additionne les deux multiplicités.",
             "pieges": [(4, "4 : ce sont les galets seuls. Ajoute le capteur d'obstacle (multiplicité 1).")],
             "aide": "4 galets + 1 capteur = 5."},
            {"type": "qcm", "label": "Le sens de «satisfy»",
             "question": "Sur le diagramme d'exigences (figure du § 3 de la fiche), une flèche pointillée «satisfy» "
                         "va du Motoréducteur vers l'exigence « Durée d'ouverture ». Comment la lire ?",
             "options": ["L'exigence satisfait le motoréducteur",
                         "Le motoréducteur est vérifié par un essai",
                         "Le motoréducteur satisfait l'exigence de durée d'ouverture"], "bonne": 2,
             "indice": "La flèche «satisfy» part de l'élément de conception.",
             "diagnostics": {0: "Sens inverse : c'est l'élément de conception (le bloc) qui satisfait l'exigence.",
                             1: "Un essai qui vérifie une exigence se lit avec «verify», pas «satisfy»."}},
        ],
        "corrige": {
            "enonce": "Dossier SysML du portail : req et bdd.",
            "regle": "**En-tête** : abréviation [type] nom. **bdd** : losange noir = composé de ; multiplicité = nombre "
                    "d'exemplaires. **req** : «satisfy» va du bloc vers l'exigence.",
            "conversions": "Aucune : lecture.",
            "remplacement": "On lit l'en-tête, les multiplicités et le sens de la flèche.",
            "calcul": "**bdd** = composition du portail ; **4 galets** ; **5 pièces** (4 galets + 1 capteur) ; "
                     "le **motoréducteur satisfait** l'exigence.",
            "verification": "Le motoréducteur qui satisfait l'exigence (req) figure bien dans la composition du "
                            "portail (bdd) : les deux diagrammes sont cohérents.",
        },
        "a_retenir": "À retenir : l'en-tête dit de quoi parle le diagramme ; le bdd donne la composition et les "
                     "quantités ; «satisfy» relie un bloc à l'exigence qu'il satisfait.",
    },
    {
        "id": "at179",
        "chapitre": "Bloc 1",
        "titre": "Lire le fonctionnement d'un système (ibd, séquence, états)",
        "theme": "Analyse fonctionnelle",
        "fiche": "1.9",
        "figure": "sysml_comportement",
        "vocabulaire": [
            ("Flux d'éléments",
             "ce qui circule sur un connecteur d'ibd (énergie, matière, information) : pointe noire vers le bloc qui "
             "reçoit."),
            ("Ligne de vie",
             "la ligne verticale pointillée d'un élément dans un diagramme de séquence ; le temps descend."),
            ("Transition",
             "le passage d'un état à un autre : « événement [garde] / effet »."),
        ],
        "enonce": "On étudie le fonctionnement du portail coulissant motorisé de la fiche (exemple pédagogique) à partir "
                  "de son ibd, de son diagramme de séquence et de son diagramme d'états.",
        "etapes": [
            {"type": "qcm", "label": "Ce qui circule",
             "question": "Sur l'ibd (figure du § 5 de la fiche), une pointe noire est posée sur le connecteur entre la carte et le motoréducteur, "
                         "dirigée vers le motoréducteur, avec l'étiquette « énergie électrique ». Que signifie-t-elle ?",
             "options": ["L'énergie électrique circule de la carte vers le motoréducteur",
                         "Le motoréducteur commande la carte",
                         "La carte est composée du motoréducteur"], "bonne": 0,
             "indice": "Pointe noire sur un connecteur = flux d'éléments, vers le bloc qui reçoit.",
             "diagnostics": {1: "La pointe est dirigée vers le motoréducteur : c'est lui qui reçoit.",
                             2: "La composition se lit sur le bdd (losange noir), pas sur un connecteur d'ibd."}},
            {"type": "numerique", "label": "Messages reçus par le motoréducteur",
             "unite": "messages", "attendu": 2, "tol": 0.1,
             "consigne": "Sur le diagramme de séquence « Ouvrir » (figure affichée), combien de messages la carte "
                         "envoie-t-elle au motoréducteur ?",
             "indice": "Ne compte que les flèches qui partent de la ligne de vie « carte » et arrivent sur celle du "
                       "motoréducteur.",
             "pieges": [(4, "4 : c'est le nombre total de messages du scénario. Ne garde que ceux de la carte vers le "
                            "motoréducteur : démarrer(sens) et arrêter()."),
                        (3, "3 : finDeCourse() va du capteur vers la carte, pas de la carte vers le motoréducteur.")],
             "aide": "démarrer(sens) et arrêter() : 2 messages."},
            {"type": "qcm", "label": "L'ordre",
             "question": "Dans ce diagramme de séquence, comment sait-on que « démarrer(sens) » a lieu avant "
                         "« arrêter() » ?",
             "options": ["Il est écrit plus à gauche", "Il est placé plus haut : le temps s'écoule de haut en bas",
                         "Il est plus court"], "bonne": 1,
             "indice": "Dans quel sens le temps s'écoule-t-il dans un diagramme de séquence ?",
             "diagnostics": {0: "La position horizontale distingue les éléments (lignes de vie), pas le temps.",
                             2: "La longueur d'une flèche dépend de l'écart entre les lignes de vie, pas de l'ordre."}},
            {"type": "qcm", "label": "Une transition",
             "question": "Dans le diagramme d'états, la transition de « Fermé » vers « En ouverture » porte "
                         "l'étiquette « appui [aucun obstacle] / démarrer moteur ». Que représente « [aucun obstacle] » ?",
             "options": ["L'événement déclencheur", "L'action réalisée",
                         "Une condition (garde) qui doit être vraie pour que la transition ait lieu"], "bonne": 2,
             "indice": "Syntaxe : événement [garde] / effet.",
             "diagnostics": {0: "L'événement est « appui », écrit avant les crochets.",
                             1: "L'action réalisée est « démarrer moteur », écrite après la barre oblique."}},
        ],
        "corrige": {
            "enonce": "ibd, diagramme de séquence et diagramme d'états du portail.",
            "regle": "**ibd** : pointe noire sur un connecteur = ce qui circule, vers le bloc qui reçoit. **sd** : le "
                    "temps descend. **stm** : « événement [garde] / effet ».",
            "conversions": "Aucune : lecture.",
            "remplacement": "On lit le sens de la pointe, l'ordre vertical des messages, la syntaxe de la transition.",
            "calcul": "**énergie électrique de la carte vers le motoréducteur** ; **2 messages** de la carte vers le "
                     "motoréducteur ; ordre lu **de haut en "
                     "bas** ; **[aucun obstacle] = garde** : sans elle vraie, l'appui ne fait rien.",
            "verification": "Le scénario de séquence (démarrer puis arrêter le moteur) est cohérent avec les états "
                            "« Fermé → En ouverture → Ouvert » : deux vues du même fonctionnement.",
        },
        "a_retenir": "À retenir : l'ibd montre ce qui circule, la séquence l'ordre des échanges (de haut en bas), le "
                     "diagramme d'états les états et ce qui fait passer de l'un à l'autre.",
    },
]

# ===========================================================================
# 5. GÉNÉRATEURS : aucun (fiche de lecture, sans calcul).
# ===========================================================================

# ===========================================================================
# 6. QUIZ — nouvelle catégorie « SysML en lecture »
#    positions de la bonne réponse : 2, 0, 3, 1, 1, 3, 0, 2
# ===========================================================================
QUIZ_SYSML = [
    ("Dans un sujet de BTS CPI, que fait-on des diagrammes SysML fournis ?",
     ["On les redessine au propre", "On les complète par un diagramme d'activités",
      "On les lit pour comprendre le système et en tirer les données de l'étude", "On les traduit en SADT"], 2,
     "Le référentiel (S1.1) limite SysML à la lecture et à la compréhension : les diagrammes sont une donnée "
     "d'entrée de l'étude.", "Base"),
    ("Quel diagramme répond à la question « que doit faire le système, avec quelles performances ? »",
     ["Le diagramme d'exigences (req)", "Le diagramme de définition de blocs (bdd)",
      "Le diagramme de séquence (sd)", "Le diagramme d'états (stm)"], 0,
     "Chaque exigence porte un identifiant et un texte, souvent chiffré : c'est le cahier des charges sous forme de "
     "diagramme.", "Base"),
    ("Sur un bdd, un losange noir relie le bloc « Portail » à plusieurs autres blocs. Comment le lire ?",
     ["Le portail hérite de ces blocs", "Les blocs échangent de l'énergie", "Le portail vérifie ces blocs",
      "Le portail est composé de ces blocs"], 3,
     "Le losange noir, côté bloc composé, se lit « est composé de » ; les multiplicités disent combien "
     "d'exemplaires.", "Base"),
    ("Une flèche pointillée «satisfy» va du bloc « Motoréducteur » à l'exigence « Durée d'ouverture ». Que "
     "signifie-t-elle ?",
     ["L'exigence est déduite du motoréducteur", "Le motoréducteur satisfait l'exigence",
      "Un essai vérifie le motoréducteur", "L'exigence contient le motoréducteur"], 1,
     "«satisfy» part de l'élément de conception et pointe vers l'exigence qu'il satisfait. Un essai, c'est «verify» ; "
     "une exigence déduite, «deriveReqt».", "Piège"),
    ("Quel diagramme montre comment les parties d'un système sont reliées et ce qui circule entre elles ?",
     ["Le diagramme de définition de blocs (bdd)", "Le diagramme de blocs internes (ibd)",
      "Le diagramme de cas d'utilisation (uc)", "Le diagramme d'exigences (req)"], 1,
     "L'ibd montre les parties, leurs ports, les connecteurs et les flux d'éléments (énergie, matière, information) ; "
     "le bdd dit seulement de quoi le système est composé.", "Intermédiaire"),
    ("Dans un diagramme de séquence, dans quel sens s'écoule le temps ?",
     ["De gauche à droite", "De droite à gauche", "De bas en haut", "De haut en bas"], 3,
     "Les lignes de vie sont verticales ; les messages sont lus de haut en bas, dans l'ordre où ils sont émis.",
     "Base"),
    ("Dans un diagramme d'états, une transition porte « appui [aucun obstacle] / démarrer moteur ». Quel est "
     "l'événement déclencheur ?",
     ["appui", "aucun obstacle", "démarrer moteur", "Il n'y en a pas"], 0,
     "Syntaxe : événement [garde] / effet. « aucun obstacle » est la condition (garde), « démarrer moteur » l'effet.",
     "Intermédiaire"),
    ("L'en-tête d'un cadre indique « ibd [block] Portail motorisé ». Quelle information donne-t-il en premier ?",
     ["La date du diagramme", "L'auteur du diagramme", "Le type de diagramme (ici blocs internes)",
      "La matière du portail"], 2,
     "L'en-tête suit la forme « abréviation [type d'élément] nom » : on lit d'abord quel diagramme on a sous les yeux.",
     "Base"),
]
