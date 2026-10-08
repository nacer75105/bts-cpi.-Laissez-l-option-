# -*- coding: utf-8 -*-
# BROUILLON — fiche 12.9 « Simulation numérique et chaîne numérique » (référentiel S2.1, S2.2, S3.2.6 « notions
# d'élasticité »). Rien de ceci n'est encore dans app.py.
#
# Niveau (référentiel 2016) :
# - S3.2 : « En autonomie, le titulaire du BTS CPI interprète les résultats des simulations » ; pour les cas
#   complexes, « il est capable de dialoguer avec un spécialiste à qui il confie les modélisations ».
# - S3.2.6, notions d'élasticité : maillage (forme et taille), conditions aux limites, critère de Von Mises,
#   déplacements et déformations ; « La discrétisation en termes de taille et de type de maillage du problème est
#   donnée » ; « Les simulations de modèles surfaciques ne sont pas exigées » (S2.2).
# - S2.2 : processus « modélisation, traitement, interprétation et comparaison au réel » ; résultats : textes,
#   courbes, cartographies.
# - S2.1 : maillons de la chaîne numérique ; PDM : livrables, révisions, historique, processus de validation,
#   import/export (formats, précision), droits des intervenants.
#
# Sources des faits :
# - σ éq ≤ Rpe = Re / s et Von Mises : fiche 12.2 de l'appli ; Kt : fiche 4.1 ; fatigue : fiche 3.5 ;
#   I/v = b h²/6 : fiche 4.3 ; E = 210 000 MPa (acier) : table MATERIAUX ; STEP/STL : fiches 12.4 et 13.7.
# - Appuis trop étendus : la flèche est sous-estimée ; les contraintes sont faussées dans les deux sens
#   (vérifié par le relecteur sur un petit modèle éléments finis : pic artificiel au bord de la zone bloquée).
# - Singularité : en élasticité linéaire, la contrainte au sommet d'un angle rentrant vif est non bornée
#   (M. L. Williams, « Stress singularities resulting from various boundary conditions in angular corners of
#   plates in extension », J. Appl. Mech. 19, 1952, p. 526-528). Conséquence : la valeur affichée par le calcul
#   à cet endroit augmente à chaque raffinement du maillage, au lieu de se stabiliser.
# - STEP = ISO 10303 (vérifié : NIST, « Introduction to ISO 10303 - the STEP Standard for Product Data Exchange »).
# - Re de S235 / S355 : la désignation (fiche 3.2) ; 235 et 355 MPa.
# - Les résultats de simulation (380, 520, 170, 174, 175 MPa…), la pièce et le coefficient de sécurité exigé
#   sont des DONNÉES D'ÉNONCÉ (résultats fictifs fournis à l'élève), pas des valeurs de référence.
import math
import random

# ===========================================================================
# 1. FIGURES
# ===========================================================================

_FE_COUL = ("#1d4ed8", "#0891b2", "#16a34a", "#84cc16", "#eab308", "#f97316", "#dc2626")


def _fe_hachures(p, x, y, w, h, pas=8):
    """Bâti hachuré (encastrement) : rectangle gris avec hachures obliques."""
    p.append(f"<rect x='{x}' y='{y}' width='{w}' height='{h}' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.2'/>")
    k = 0
    while k < w + h:
        x1, y1 = x + min(k, w), y + max(0, k - w)
        x2, y2 = x + max(0, k - h), y + min(k, h)
        p.append(f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{FIN}' stroke-width='0.8'/>")
        k += pas


def _fe_maillage_L(p, x0, y0, ech, pas, noeuds):
    """Équerre en L (jambe verticale 40 × 160, aile 200 × 40) maillée en triangles de côté « pas »."""
    def dedans(u, v):
        return (0 <= u <= 40 and 0 <= v <= 160) or (0 <= u <= 200 and 120 <= v <= 160)
    pts = set()
    u = 0
    while u < 200:
        v = 0
        while v < 160:
            if dedans(u + pas / 2, v + pas / 2):
                X, Y, S = x0 + u * ech, y0 + v * ech, pas * ech
                p.append(f"<rect x='{X:.1f}' y='{Y:.1f}' width='{S:.1f}' height='{S:.1f}' fill='#eff6ff' "
                         f"stroke='{ALESAGE}' stroke-width='0.7'/>")
                p.append(f"<line x1='{X:.1f}' y1='{Y + S:.1f}' x2='{X + S:.1f}' y2='{Y:.1f}' stroke='{ALESAGE}' "
                         f"stroke-width='0.7'/>")
                pts.update({(u, v), (u + pas, v), (u, v + pas), (u + pas, v + pas)})
            v += pas
        u += pas
    contour = [(0, 0), (40, 0), (40, 120), (200, 120), (200, 160), (0, 160)]
    p.append("<polygon points='" + " ".join(f"{x0 + a * ech:.1f},{y0 + b * ech:.1f}" for a, b in contour)
             + f"' fill='none' stroke='{TRAIT}' stroke-width='1.8'/>")
    if noeuds:
        for a, b in pts:
            p.append(f"<circle cx='{x0 + a * ech:.1f}' cy='{y0 + b * ech:.1f}' r='2.4' fill='{TRAIT}'/>")


def fem_maillage():
    p = [_k_defs(), _txt(30, 24, "Le maillage : découper la pièce en petits éléments que le logiciel sait calculer", 13, TRAIT, "start", True)]
    _fe_maillage_L(p, 50, 60, 1.5, 40, True)
    _fe_maillage_L(p, 430, 60, 1.5, 10, False)
    p.append(_txt(200, 320, "MAILLAGE GROSSIER", 11, ALESAGE, "middle", True))
    p.append(_txt(200, 336, "peu d'éléments : calcul rapide, résultat approximatif", 10, TRAIT, "middle"))
    p.append(_txt(580, 320, "MAILLAGE FIN", 11, ALESAGE, "middle", True))
    p.append(_txt(580, 336, "beaucoup d'éléments : calcul plus long, plus précis", 10, TRAIT, "middle"))
    # repères : un élément, un nœud
    p.append(f"<polygon points='50,120 50,180 110,120' fill='#fde68a' stroke='{ARBRE}' stroke-width='1.4'/>")
    p.append(_k_fl(200, 150, 76, 146, ARBRE, "ko", 1.4))
    p.append(_txt(204, 146, "un élément (triangle)", 10, ARBRE, "start", True))
    p.append(_k_fl(200, 104, 114, 118, TRAIT, "kk", 1.4))
    p.append(_txt(204, 100, "un nœud (sommet)", 10, TRAIT, "start", True))
    p.append(_txt(204, 172, "le calcul donne les déplacements", 9, FIN, "start"))
    p.append(_txt(204, 184, "aux nœuds, puis les contraintes", 9, FIN, "start"))
    p.append(f"<rect x='30' y='350' width='740' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 372, "Au BTS, la taille et le type de maillage sont DONNÉS dans le sujet : on lit et on critique le résultat.", 12, TRAIT, "start", True))
    return _svg("".join(p), 800, 396)


def _fe_plaque(p, x, y, deforme=True):
    """Plat en porte-à-faux de 220 × 16 dont l'extrémité droite reçoit une force F vers le bas."""
    p.append(f"<rect x='{x}' y='{y}' width='220' height='16' fill='#dbeafe' stroke='{ALESAGE}' stroke-width='1.6'/>")
    p.append(_k_fl(x + 214, y - 44, x + 214, y - 4, ALERTE, "kr", 2.2))
    p.append(_txt(x + 206, y - 30, "F", 12, ALERTE, "end", True))
    if deforme:
        p.append(f"<path d='M {x} {y + 8} Q {x + 140} {y + 10} {x + 220} {y + 34}' fill='none' stroke='{ALERTE}' "
                 f"stroke-width='1.2' stroke-dasharray='5 3'/>")


def fem_conditions_limites():
    p = [_k_defs(), _txt(30, 24, "Conditions aux limites : dire au logiciel comment la pièce est tenue et chargée", 13, TRAIT, "start", True),
         _txt(30, 38, "Même pièce réelle (tenue par 2 vis sur un bâti), trois façons de la déclarer au logiciel :", 10, FIN, "start", True)]
    cadres = ((20, "JUSTE", OK), (280, "TROP RIGIDE", ARBRE), (540, "PAS TENUE", ALERTE))
    for x, titre, c in cadres:
        p.append(f"<rect x='{x}' y='46' width='250' height='244' rx='8' fill='#ffffff' stroke='{c}' stroke-width='1.8'/>")
        p.append(_txt(x + 125, 62, titre, 12, c, "middle", True))
    # JUSTE : le plat est vissé au bâti par deux vis à gauche ; fixation modélisée sur les trous de vis
    _fe_hachures(p, 30, 150, 60, 30)
    _fe_plaque(p, 30, 134)
    for xv in (44, 74):
        p.append(f"<line x1='{xv}' y1='126' x2='{xv}' y2='176' stroke='{TRAIT}' stroke-width='3'/>")
    p.append(_txt(145, 206, "déclarée fixée sur les trous de vis,", 10, TRAIT, "middle"))
    p.append(_txt(145, 220, "en appui sur le bâti ; force sur", 10, TRAIT, "middle"))
    p.append(_txt(145, 234, "la vraie surface d'appui", 10, TRAIT, "middle"))
    p.append(_txt(145, 262, "déformée calculée réaliste", 10, OK, "middle", True))
    # TROP RIGIDE : même bâti, mêmes vis ; mais la moitié gauche est DÉCLARÉE bloquée
    _fe_hachures(p, 290, 150, 60, 30)
    _fe_plaque(p, 290, 134, False)
    for xv in (304, 334):
        p.append(f"<line x1='{xv}' y1='126' x2='{xv}' y2='176' stroke='{TRAIT}' stroke-width='3'/>")
    p.append(f"<rect x='290' y='130' width='120' height='24' fill='{ARBRE}' fill-opacity='0.35' stroke='{ARBRE}' stroke-dasharray='4 2'/>")
    p.append(_txt(350, 124, "zone déclarée bloquée", 9, ARBRE, "middle", True))
    p.append(f"<path d='M 410 142 Q 470 143 510 154' fill='none' stroke='{ALERTE}' stroke-width='1.2' stroke-dasharray='5 3'/>")
    p.append(_txt(470, 168, "déformée calculée", 9, ALERTE, "middle"))
    p.append(_txt(320, 196, "bâti + vis", 9, FIN, "middle"))
    p.append(_txt(405, 214, "toute une zone bloquée alors", 10, TRAIT, "middle"))
    p.append(_txt(405, 228, "que la pièce ne tient que par", 10, TRAIT, "middle"))
    p.append(_txt(405, 242, "deux vis : modèle trop raide", 10, TRAIT, "middle"))
    p.append(_txt(405, 260, "flèche sous-estimée,", 10, ARBRE, "middle", True))
    p.append(_txt(405, 274, "contraintes faussées", 10, ARBRE, "middle", True))
    # PAS TENUE : même pièce, aucune fixation déclarée (bâti dessiné en pointillé : ignoré par le logiciel)
    p.append(f"<rect x='570' y='150' width='60' height='30' fill='none' stroke='{FIN}' stroke-dasharray='4 3'/>")
    p.append(_txt(600, 196, "bâti non déclaré", 9, FIN, "middle"))
    _fe_plaque(p, 560, 134, False)
    p.append(_txt(665, 214, "aucune fixation déclarée :", 10, TRAIT, "middle"))
    p.append(_txt(665, 228, "la pièce peut glisser en bloc", 10, TRAIT, "middle"))
    p.append(_txt(665, 242, "sous la force", 10, TRAIT, "middle"))
    p.append(_txt(665, 256, "le calcul ne peut pas aboutir", 10, ALERTE, "middle", True))
    p.append(_txt(665, 270, "(message d'erreur ou résultat absurde)", 10, ALERTE, "middle"))
    p.append(_txt(60, 196, "bâti + vis", 9, FIN, "middle"))
    p.append(f"<rect x='20' y='304' width='770' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(36, 326, "Le logiciel calcule exactement ce qu'on lui décrit : un appui faux donne un résultat faux, même joli.", 12, TRAIT, "start", True))
    return _svg("".join(p), 810, 350)


def fem_von_mises():
    p = [_k_defs(), _txt(30, 24, "Lire une carte de contraintes de Von Mises : couleurs, échelle, zone critique", 13, TRAIT, "start", True)]
    _fe_hachures(p, 40, 70, 50, 150)
    # plat en porte-à-faux, vu de côté, bandes de couleur : σ maxi à l'encastrement, nulle sous la force
    x0, L, y, h = 90, 440, 120, 48
    n, nr = 11, 6
    for k in range(n):
        for j in range(nr):
            yrel = max(abs(j / nr - 0.5), abs((j + 1) / nr - 0.5)) * 2
            sig = 156 * (1 - k / n) * yrel      # σ = M y / I : maxi sur les faces, nulle sur la fibre neutre
            idx = min(6, int(sig / (240 / 7)))
            p.append(f"<rect x='{x0 + k * L / n:.1f}' y='{y + j * h / nr:.1f}' width='{L / n + 0.5:.1f}' "
                     f"height='{h / nr + 0.5:.1f}' fill='{_FE_COUL[idx]}'/>")
    p.append(f"<rect x='{x0}' y='{y}' width='{L}' height='{h}' fill='none' stroke='{TRAIT}' stroke-width='1.4'/>")
    p.append(_k_fl(x0 + L - 6, y - 46, x0 + L - 6, y - 4, ALERTE, "kr", 2.2))
    p.append(_txt(x0 + L - 14, y - 30, "F = 500 N", 11, ALERTE, "end", True))
    # pic à l'angle vif (jonction plat / bâti)
    p.append(f"<circle cx='{x0 + 2}' cy='{y + 1}' r='6' fill='{_FE_COUL[6]}' stroke='{TRAIT}'/>")
    p.append(_k_fl(150, 88, 96, 114, TRAIT, "kk", 1.3))
    p.append(_txt(154, 84, "pic rouge au coin plat / bâti (angle vif) : 380 MPa affichés", 10, ALERTE, "start", True))
    p.append(_txt(154, 98, "→ singularité ? (§ 5) : à vérifier avant de conclure", 10, ALERTE, "start"))
    p.append(_txt(x0 + 115, y + h + 22, "zone la plus sollicitée : faces haute et", 10, TRAIT, "middle", True))
    p.append(_txt(x0 + 115, y + h + 36, "basse près de l'encastrement ≈ 150 MPa (jaune)", 10, TRAIT, "middle"))
    p.append(_txt(x0 + 115, y + h + 50, "fibre neutre (milieu) : presque 0", 10, TRAIT, "middle"))
    p.append(_txt(x0 + L - 50, y + h + 22, "bout libre : presque 0", 10, TRAIT, "middle", True))
    p.append(_txt(x0 + L - 50, y + h + 36, "(bleu)", 10, TRAIT, "middle"))
    p.append(_txt(65, 238, "bâti", 9, FIN, "middle"))
    p.append(_txt(x0 + L / 2, y - 8, "plat en S235 (Re = 235 MPa), vu de côté", 10, TRAIT, "middle", True))
    # échelle de couleurs 0 – 240 MPa, repère Re
    xe, ye, he = 640, 56, 210
    for k in range(7):
        p.append(f"<rect x='{xe}' y='{ye + he - (k + 1) * he / 7:.1f}' width='22' height='{he / 7 + 0.5:.1f}' fill='{_FE_COUL[k]}'/>")
    p.append(f"<rect x='{xe}' y='{ye}' width='22' height='{he}' fill='none' stroke='{TRAIT}'/>")
    for v in (0, 60, 120, 180, 240):
        yy = ye + he - v / 240 * he
        p.append(f"<line x1='{xe + 22}' y1='{yy:.1f}' x2='{xe + 28}' y2='{yy:.1f}' stroke='{TRAIT}'/>")
        p.append(_txt(xe + 32, yy + 4, f"{v}", 10, TRAIT, "start"))
    yre = ye + he - 235 / 240 * he
    p.append(f"<line x1='{xe - 8}' y1='{yre:.1f}' x2='{xe + 30}' y2='{yre:.1f}' stroke='{ALERTE}' stroke-width='2'/>")
    p.append(_txt(xe - 12, yre + 4, "Re", 11, ALERTE, "end", True))
    p.append(_txt(xe + 11, ye - 8, "σ Von Mises (MPa)", 10, TRAIT, "middle", True))
    p.append(_txt(xe + 11, ye + he + 18, "échelle", 9, FIN, "middle"))
    p.append(f"<rect x='30' y='290' width='740' height='48' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 310, "Réflexe : lire l'échelle, repérer le maximum, le comparer à Re / s (σ éq ≤ Rpe, fiche 12.2).", 12, TRAIT, "start", True))
    p.append(_txt(46, 328, "Exemple pédagogique (données d'énoncé). Échelle arrêtée à 240 MPa pour lire la pièce : le pic de 380 la dépasse.", 10, FIN, "start"))
    return _svg("".join(p), 800, 350)


def fem_singularite():
    p = [_k_defs(), _txt(30, 24, "Raffiner le maillage : une vraie contrainte se stabilise, une singularité grimpe sans fin", 13, TRAIT, "start", True)]
    # axes
    x0, y0, w, h = 90, 300, 420, 240
    p.append(_k_fl(x0, y0, x0 + w + 20, y0, TRAIT, "kk", 1.4))
    p.append(_k_fl(x0, y0, x0, y0 - h - 20, TRAIT, "kk", 1.4))
    p.append(_txt(x0 + w / 2, y0 + 36, "maillage de plus en plus fin (taille d'élément divisée par 2 à chaque fois) →", 10, TRAIT, "middle"))
    p.append(_txt(x0 + 10, y0 - h - 6, "contrainte maxi affichée (MPa)", 10, TRAIT, "start", True))
    vif = (250, 300, 380, 520, 700)
    conge = (160, 170, 174, 175, 175)
    ymax = 750

    def pt(i, v):
        return x0 + 40 + i * 90, y0 - v / ymax * h
    for i in range(5):
        X, _ = pt(i, 0)
        p.append(f"<line x1='{X}' y1='{y0}' x2='{X}' y2='{y0 + 5}' stroke='{TRAIT}'/>")
        p.append(_txt(X, y0 + 18, f"n° {i + 1}", 9, TRAIT, "middle"))
    for serie, c, dec in ((vif, ALERTE, -10), (conge, OK, 18)):
        p.append("<polyline points='" + " ".join(f"{pt(i, v)[0]:.1f},{pt(i, v)[1]:.1f}" for i, v in enumerate(serie))
                 + f"' fill='none' stroke='{c}' stroke-width='2.2'/>")
        for i, v in enumerate(serie):
            X, Y = pt(i, v)
            p.append(f"<circle cx='{X:.1f}' cy='{Y:.1f}' r='3.5' fill='{c}'/>")
            p.append(_txt(X, Y + dec, f"{v}", 9, c, "middle", True))
    p.append(_txt(430, 70, "angle vif : ne se stabilise jamais — pic qui grimpe, pic qui trompe", 10, ALERTE, "end", True))
    p.append(_txt(430, 84, "→ SINGULARITÉ du modèle, pas physique", 10, ALERTE, "end"))
    p.append(_txt(500, 222, "congé : se stabilise (≈ 175) — pic qui se pose, pic qui compte", 10, OK, "end", True))
    p.append(_txt(500, 236, "→ contrainte réelle, à exploiter", 10, OK, "end"))
    # croquis : angle vif et congé
    p.append(f"<rect x='560' y='50' width='220' height='250' rx='8' fill='#ffffff' stroke='{FIN}'/>")
    p.append(f"<path d='M 590 70 L 590 150 L 680 150' fill='none' stroke='{ALERTE}' stroke-width='3'/>")
    p.append(f"<circle cx='590' cy='150' r='6' fill='none' stroke='{ALERTE}' stroke-width='1.6'/>")
    p.append(_txt(700, 120, "angle vif", 11, ALERTE, "middle", True))
    p.append(_txt(700, 134, "(rayon nul)", 10, ALERTE, "middle"))
    p.append(f"<path d='M 590 190 L 590 245 Q 590 270 615 270 L 680 270' fill='none' stroke='{OK}' stroke-width='3'/>")
    p.append(_txt(700, 240, "congé", 11, OK, "middle", True))
    p.append(_txt(700, 254, "(rayon réel)", 10, OK, "middle"))
    p.append(f"<rect x='30' y='344' width='750' height='48' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 364, "Un angle vif parfait n'existe pas sur une vraie pièce : le modèle y affiche une valeur sans limite.", 12, TRAIT, "start", True))
    p.append(_txt(46, 382, "Valeurs d'illustration (résultats fournis, données d'énoncé) — c'est l'allure qui compte.", 10, FIN, "start"))
    return _svg("".join(p), 800, 404)


def pdm_versions():
    p = [_k_defs(), _txt(30, 24, "La chaîne numérique et le PDM : un seul dossier de données, des versions, des droits", 13, TRAIT, "start", True)]
    maillons = ("Maquette 3D", "Simulation", "Prototype", "Outillage", "Production", "Qualification")
    for k, m in enumerate(maillons):
        x = 30 + k * 125
        p.append(f"<rect x='{x}' y='44' width='110' height='34' rx='6' fill='#eff6ff' stroke='{ALESAGE}' stroke-width='1.4'/>")
        p.append(_txt(x + 55, 65, m, 10, ALESAGE, "middle", True))
        if k < 5:
            p.append(_k_fl(x + 110, 61, x + 123, 61, ALESAGE, "kb", 1.4))
    p.append(f"<path d='M 720 78 Q 720 100 400 100 Q 85 100 85 82' fill='none' stroke='{ARBRE}' stroke-width='1.4' "
             f"stroke-dasharray='5 3' marker-end='url(#ko)'/>")
    p.append(_txt(400, 96, "boucle d'optimisation : ce qu'on apprend en aval revient corriger la maquette", 9, ARBRE, "middle", True))
    # PDM au centre
    p.append(f"<rect x='250' y='120' width='300' height='60' rx='10' fill='#fff7ed' stroke='{ARBRE}' stroke-width='2'/>")
    p.append(_txt(400, 144, "PDM (Product Data Management)", 12, ARBRE, "middle", True))
    p.append(_txt(400, 162, "chaque maillon y dépose et y lit ses fichiers", 10, TRAIT, "middle"))
    for xm in (85, 335, 465, 715):
        p.append(f"<line x1='{xm}' y1='104' x2='{250 if xm < 400 else 550}' y2='150' stroke='{ARBRE}' stroke-width='0.8'/>")
    # révisions
    p.append(_txt(40, 212, "RÉVISIONS d'un plan", 11, TRAIT, "start", True))
    revs = (("A", "validée", "archivée", FIN), ("B", "validée", "en vigueur", OK), ("C", "en cours", "réservée par le dessinateur", ARBRE))
    for k, (r, st, note, c) in enumerate(revs):
        x = 40 + k * 130
        p.append(f"<rect x='{x}' y='222' width='110' height='56' rx='6' fill='#ffffff' stroke='{c}' stroke-width='1.6'/>")
        p.append(_txt(x + 55, 242, f"indice {r}", 11, c, "middle", True))
        p.append(_txt(x + 55, 258, st, 10, TRAIT, "middle"))
        p.append(_txt(x + 55, 272, note if len(note) < 18 else "réservée", 9, FIN, "middle"))
        if k < 2:
            p.append(_k_fl(x + 110, 250, x + 128, 250, TRAIT, "kk", 1.3))
    p.append(_txt(300, 292, "réservée par le dessinateur : personne d'autre ne peut la modifier en même temps", 9, FIN, "start"))
    p.append(_txt(40, 292, "on ne modifie jamais B :", 9, FIN, "start"))
    p.append(_txt(40, 304, "on crée C, B reste lisible", 9, FIN, "start"))
    # workflow et droits
    p.append(_txt(460, 212, "VALIDATION", 11, TRAIT, "start", True))
    etapes = ("en cours", "en validation", "validé")
    for k, e in enumerate(etapes):
        x = 460 + k * 105
        p.append(f"<rect x='{x}' y='222' width='92' height='26' rx='13' fill='#f0fdf4' stroke='{OK}'/>")
        p.append(_txt(x + 46, 239, e, 10, OK, "middle", True))
        if k < 2:
            p.append(_k_fl(x + 92, 235, x + 103, 235, OK, "kg", 1.3))
    p.append(_txt(460, 266, "droits : le calculateur LIT, le dessinateur", 9, TRAIT, "start"))
    p.append(_txt(460, 278, "MODIFIE, le responsable VALIDE", 9, TRAIT, "start"))
    p.append(f"<rect x='30' y='316' width='740' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 338, "Échange : format neutre STEP (ISO 10303) pour la 3D, STL pour l'impression (fiches 12.4, 13.7). PLM : tout le cycle de vie.", 11, TRAIT, "start", True))
    return _svg("".join(p), 800, 362)


FIGURES_NOUVELLES = {
    "fem_maillage": ("Le maillage d'une pièce", fem_maillage),
    "fem_conditions_limites": ("Conditions aux limites : juste, trop rigide, pas tenue", fem_conditions_limites),
    "fem_von_mises": ("Lire une carte de contraintes de Von Mises", fem_von_mises),
    "fem_singularite": ("Singularité à un angle vif et convergence au congé", fem_singularite),
    "pdm_versions": ("Chaîne numérique, PDM, révisions et validation", pdm_versions),
}

# ===========================================================================
# 2. FICHE 12.9 — en FIN de bloc 12 (après la 12.8)
# ===========================================================================

FICHE_12_9 = {
    "id": "12.9",
    "titre": "Simulation numérique et chaîne numérique : lire et critiquer un calcul, gérer les données",
    "duree": "6 h",
    "cours": """### 1. Pourquoi cette fiche

Avant de fabriquer une pièce, le bureau d'études la **valide** : va-t-elle tenir ? Pour une pièce simple, le
calcul de RDM à la main suffit (blocs 4 et 12). Pour une forme compliquée — un carter, une équerre, une pièce
moulée — on passe par une **simulation par éléments finis**.

Le programme du BTS fixe le niveau : pour des **cas simples**, le technicien propose la modélisation et conduit
lui-même la simulation ; pour les **cas complexes**, il **dialogue avec un spécialiste** (le calculateur) à qui il
la confie ; dans tous les cas, il **interprète les résultats en autonomie**. La taille et le type de maillage sont
**donnés** dans le sujet. Cette fiche se concentre sur la **lecture critique** d'un résultat fourni ; la mise en
œuvre du logiciel se pratique en TP.

*Le piège classique, que toute la fiche combat : croire le calcul parce que l'image est belle. Un logiciel
calcule exactement ce qu'on lui a décrit — si la description est fausse, le résultat est faux, avec de jolies
couleurs.*

**Les mots à connaître, en français courant :**

| Mot | En français courant |
|---|---|
| **maillage** | le découpage de la pièce en petits morceaux simples (les éléments) |
| **élément** | un petit morceau du maillage : triangle en 2D, tétraèdre (petite pyramide à 4 faces) en 3D |
| **nœud** | un sommet d'élément : c'est là que le logiciel calcule les déplacements |
| **conditions aux limites** | comment la pièce est tenue (fixations, appuis) et chargée (forces, pressions) |
| **contrainte de Von Mises** | la contrainte équivalente (fiche 12.2), affichée en couleurs sur toute la pièce |
| **singularité** | un point où le modèle affiche une contrainte sans limite, qui n'existe pas en réalité |
| **convergence** | la valeur ne change presque plus quand on affine le maillage : on peut lui faire confiance |
| **calculateur** | la **personne** (ingénieur ou technicien) spécialiste de la simulation — pas la machine |
| **PDM** | le logiciel qui range, suit et protège toutes les données d'un projet |

### 2. Le principe : découper pour calculer

[[FIG:fem_maillage]]

Le logiciel ne sait pas calculer directement une forme compliquée. Il la **découpe** en milliers de petits
**éléments** simples, accrochés les uns aux autres par leurs sommets, les **nœuds**. *Image : chaque élément se
comporte comme un petit ressort ; la pièce maillée devient un grand réseau de ressorts accrochés par leurs nœuds,
comme un sommier.* Le logiciel cherche de combien chaque nœud **se déplace** sous la charge ; il en déduit les
**déformations** (comme ε = ΔL / L en traction), puis les **contraintes** (σ = E ε, loi de Hooke).

- **Maillage grossier** : peu d'éléments, calcul rapide, résultat approximatif — il peut « rater » un pic de
  contrainte dans un petit congé.
- **Maillage fin** : plus précis, mais calcul plus long (sauf sur une singularité, § 5, où la valeur grimpe sans
  fin). Sur une note de calcul, **vérifie** que le maillage est plus fin aux congés, trous et changements de
  section : sinon, un pic a pu passer inaperçu.

*Image : c'est comme dessiner un cercle avec des segments. Avec 6 segments, on a un hexagone ; avec 100, on ne
voit plus la différence. Le maillage approche la pièce de la même façon.*

**Ce qu'on peut simuler** (le programme cite plusieurs types de logiciels) : le comportement **mécanique**
(statique, cinématique, dynamique), le **calcul de structures** — modèle **poutre** ou modèle **volumique** (les
modèles surfaciques ne sont pas exigés) —, la **simulation de procédés** (par exemple le remplissage d'un moule,
bloc 13) et l'**ergonomie** (réalité virtuelle). Cette fiche traite du calcul de structure volumique, le plus
courant en bureau d'études mécanique. Dans tous les cas, le résultat dépend des **données d'entrée** :
géométrie, matériau (E, Re), conditions aux limites, maillage.

### 3. Les conditions aux limites : là où tout se joue

[[FIG:fem_conditions_limites]]

Il faut dire au logiciel **comment la pièce est tenue** (fixations, appuis) et **comment elle est chargée**
(forces, pressions, couples). C'est la traduction des **liaisons** et des **actions mécaniques** de la statique
(blocs 6 et 12). La figure montre **la même pièce réelle**, tenue par deux vis, déclarée de trois façons :

- **Juste** : fixée sur les trous de vis, en appui sur la face du bâti ; la force sur la surface où elle
  s'applique vraiment.
- **Trop rigide** : bloquer toute une face alors que la pièce ne tient que par deux vis rend le modèle plus raide
  que la réalité. La **flèche est sous-estimée**, et les **contraintes sont faussées** : celles qui comptent,
  autour des vis, ne sont pas calculées, et un pic artificiel apparaît souvent au bord de la zone bloquée.
  *Image : un plongeoir boulonné au bord de la piscine par deux boulons. Si on déclare au logiciel qu'il est
  collé sur la moitié de sa longueur, sa partie libre est raccourcie : il plie beaucoup moins qu'en vrai. La pièce
  calculée n'est plus celle qu'on fabriquera.*
- **Pas tenue** : le logiciel cherche de combien la pièce se déforme. Une pièce qu'aucune fixation ne retient
  glisse en bloc sous la force, comme un carton poussé sur de la glace : le calcul ne peut pas aboutir (message
  d'erreur ou résultat absurde).
- **Force en un point** : σ = F / S ; si la force est appliquée sur un seul nœud, la surface S est presque nulle,
  donc σ devient énorme sous ce point — l'effet d'une pointe de punaise. Une vraie force s'applique toujours sur
  une surface.

*C'est pourquoi un mauvais appui fausse tout : le logiciel n'invente rien, il calcule la pièce qu'on lui a
décrite — pas celle qu'on fabriquera.*

### 4. Lire une carte de Von Mises

[[FIG:fem_von_mises]]

Le résultat le plus courant est une **cartographie** (le programme cite les textes, courbes et cartographies) :
la pièce colorée selon la **contrainte équivalente de Von Mises**, la même que celle de la fiche 12.2, calculée
en chaque point. Ce critère convient aux matériaux **ductiles** (aciers, alliages d'aluminium) ; une pièce en
matériau fragile, comme une fonte, se juge autrement.

**Comment la lire, dans l'ordre :**
1. **Lire l'échelle** : quelles valeurs, en quelle unité (MPa), du bleu (faible) au rouge (fort) ? Les couleurs
   seules ne disent rien : un rouge vaut peut-être 20 MPa sur une pièce, 400 MPa sur une autre. Si l'échelle va
   jusqu'au maximum affiché, un pic de singularité « écrase » toutes les autres couleurs, et la pièce paraît
   bleue.
2. **Repérer le maximum** et **où** il se trouve : c'est la **zone critique**.
3. **Se demander si ce maximum est crédible** (§ 5 : singularité ou vraie concentration ?).
4. **Conclure avec la condition de résistance** (fiche 12.2) : σ éq ≤ Rpe = Re / s, où **Rpe** est la
   résistance pratique, la contrainte qu'on s'autorise. Autrement dit : **s obtenu = Re / σ éq** doit être au
   moins égal au **s exigé** par le cahier des charges.

**Pourquoi Re, et pas Rm ?** Au-delà de Re, la pièce reste tordue une fois la charge retirée, comme un trombone
trop plié : on veut qu'elle revienne à sa forme. Et le calcul lui-même suppose ce comportement de ressort.

**Toujours vérifier par un ordre de grandeur à la main.** Exemple : un **plat** (barre méplate) en S235
(Re = 235 MPa), de section 30 × 8 mm (largeur 30 mm, épaisseur 8 mm dans le sens de la force), encastré, reçoit
F = 500 N à 100 mm de l'encastrement. À la main (fiche 4.3) : M = F × L = 500 × 100 = 50 000 N·mm ;
I/v = b h²/6 = 30 × 8² / 6 = 320 mm³ (I/v : module de flexion) ; σ = M / (I/v) = 50 000 / 320 ≈ **156 MPa**, sur
les faces haute et basse de la section d'encastrement. La carte affiche environ 150 MPa à cet endroit : le calcul
et la simulation se confirment. s obtenu = 235 / 156,25 ≈ **1,50**.

**Les déplacements aussi se lisent.** Le logiciel affiche une carte de **déplacements** (en mm). Sur ce même plat,
la flèche au bout se calcule à la main : f = F L³ / (3 E I), avec I = b h³/12 = 30 × 8³ / 12 = 1 280 mm⁴ et
E = 210 000 MPa (acier) : f = 500 × 100³ / (3 × 210 000 × 1 280) ≈ **0,62 mm**. La carte de déplacements doit
afficher environ 0,6 mm au bout libre.

> **La main et la simulation se contrôlent l'une l'autre.**
> - Le calcul à la main donne la contrainte **nominale**, celle de la poutre « idéale », sans trou ni congé.
> - La simulation voit en plus les détails de forme : près d'un congé ou d'un trou, elle doit trouver **un peu
>   plus** que la main — c'est le Kt des fiches 4.1 et 3.5. C'est normal, et c'est même ce qu'on attend d'elle.
> - Si elle trouve **nettement moins** que la main dans la section la plus chargée, quelque chose l'a « aidée » à
>   tort : un appui trop étendu, une force mal saisie, une erreur d'unité. Un petit écart est normal (les deux
>   méthodes ne font pas les mêmes approximations) ; un écart important doit être **expliqué** avant de conclure ;
>   un facteur 2 ou 10 trahit presque toujours une erreur grossière.
> - Tant que l'écart n'est pas expliqué, on retient la valeur **la plus défavorable** : c'est elle qui donne le
>   plus petit s. Ce n'est jamais « la simulation qui a raison parce qu'elle est plus précise ».

### 5. Les limites du modèle : un résultat de calcul n'est pas la réalité

[[FIG:fem_singularite]]

**La singularité à l'angle vif.** Un **angle rentrant**, c'est un coin creux vu depuis la matière, comme le coin
intérieur d'une équerre en L. Dans le modèle du calcul (l'**élasticité linéaire** : contrainte proportionnelle à
la déformation, loi de Hooke), la contrainte au sommet d'un angle rentrant **parfaitement vif** est
théoriquement **infinie** (résultat établi par M. L. Williams en 1952). Le logiciel ne peut pas afficher l'infini :
il affiche une grande valeur, **qui augmente à chaque fois qu'on affine le maillage** (380, puis 520, puis
700 MPa…).

*Image : la loupe sans fin. Zoomer sur un congé, c'est finir par voir un arrondi d'une certaine taille : la valeur
se fixe. Zoomer sur un angle parfaitement vif, c'est retrouver toujours le même coin pointu, quel que soit le
grossissement. Chaque raffinement du maillage est un zoom de plus : le pic monte encore.*

> **Pic qui grimpe, pic qui trompe ; pic qui se pose, pic qui compte.**

**Comment reconnaître une singularité :**
- le pic est **ponctuel**, exactement sur un angle vif, sous une force appliquée en un point, sur une fixation
  ponctuelle, ou au bord d'une zone déclarée bloquée (là où le bord bloqué rejoint le bord libre) ;
- il **grimpe sans se stabiliser** quand on raffine le maillage.

**Attention : c'est le chiffre qui est faux, pas le danger.** Un vrai coin n'est jamais parfaitement vif : il a
toujours un petit rayon (d'usinage, de moulage) — c'est pourquoi la fiche 4.1 donne à une arête vive réelle un
Kt **fini**. Seul le modèle, parfaitement vif, donne l'infini. Ce coin concentre bien les contraintes, et c'est là
que démarre une fissure de fatigue. On n'écrit donc pas « 700 MPa » dans la note, mais on demande un congé.

**La vraie concentration de contrainte.** Avec un **congé** de rayon réel, le pic devient fini : sur les derniers
maillages, la valeur se **stabilise** (170, 174, 175 MPa) — on dit que le calcul **converge**. Celle-là est
**réelle** : c'est la concentration de contrainte des fiches 4.1 et 3.5 (σ maxi = Kt × σ nominale). Elle compte
**double** : elle réduit le coefficient de sécurité, et elle marque l'endroit où une fissure de **fatigue**
démarrerait. Une contrainte sous Re ne casse pas la pièce du premier coup ; répétée des milliers de fois
(vibrations, charges qui vont et viennent), elle peut faire naître une fissure (fiche 3.5).

**Ce qu'on fait d'une singularité :** on ne la prend pas pour la contrainte de la pièce ; on **demande au
calculateur** de modéliser le vrai congé et de montrer que la valeur se stabilise. Ici, le maillage est donné :
il ne s'agit pas de mener une étude de convergence, mais de **lire** celle qu'on vous fournit.

**Les autres limites à garder en tête :**
- **maillage trop grossier** : un pic réel dans un petit congé peut être « lissé » et passer inaperçu ;
- **hypothèses du modèle** : comportement élastique, matériau homogène, géométrie idéale — sans défauts de
  fabrication, sans contraintes résiduelles de soudage ;
- **données d'entrée** : un mauvais matériau (Re, module d'Young) ou une force fausse donnent un résultat faux ;
- d'où la **comparaison au réel** demandée par le programme : un essai sur prototype confirme ou non.

> **Les cinq questions à poser au calculateur avant de signer :**
> 1. Où as-tu mis les fixations, et est-ce là que la pièce est vraiment tenue ?
> 2. Sur quelle surface est appliquée la force, et avec quelle valeur ?
> 3. Quel matériau, et quel Re, as-tu saisis ?
> 4. Le maximum se stabilise-t-il quand on affine le maillage ?
> 5. Sur quelle révision de la maquette as-tu fait le calcul ?

### 6. La chaîne numérique et le PDM

[[FIG:pdm_versions]]

La **chaîne numérique**, c'est l'enchaînement des étapes qui partent toutes du **même modèle 3D** : maquette
numérique → simulation → prototype → outillage → production → qualification (contrôle), avec une **boucle
d'optimisation** (ce qu'on apprend en simulation ou à l'essai revient modifier la maquette). Voir aussi la figure
de la fiche 12.4 :

[[FIG:chaine_numerique]]

Pour que tout le monde travaille sur la bonne version, les données sont gérées dans un **PDM** (*Product Data
Management*). Un **PLM** (*Product Lifecycle Management*) étend cette gestion à tout le cycle de vie du produit,
jusqu'à la maintenance et la fin de vie. Le PDM assure, selon le programme :
- les **livrables** : les fichiers exigés par le cahier des charges (modèles, plans, notes de calcul) ;
- les **plannings** (diagramme de **Gantt**) : les tâches du projet et leurs échéances, reliées aux livrables ;
- le **suivi et l'archivage** : chaque document a des **révisions** et un **historique**. L'**indice de
  révision**, c'est la lettre (A, B, C…) que tu vois dans le cartouche de tes plans ;
- le **processus de validation** : un document passe par « en cours → en validation → validé » ; un document
  validé n'est plus modifié — on crée une **nouvelle révision**, et l'ancienne reste lisible ;
- les **droits des intervenants** : qui peut lire, modifier, valider. Un document « réservé » par une personne ne
  peut pas être modifié en même temps par une autre — comme un livre emprunté à la bibliothèque ;
- les **liens entre données** : dans SolidWorks, l'assemblage du support appelle les fichiers de ses pièces
  (équerre, plat, vis). Si quelqu'un remplace le fichier de l'équerre sans le dire, l'assemblage change sans que
  personne ne le voie. Dans le PDM, la nomenclature du support indique « équerre, révision C » : si l'équerre passe
  en D, le PDM signale qu'il faut mettre l'assemblage à jour ;
- l'**import/export** : passer d'un logiciel à un autre par un format neutre — **STEP** (norme ISO 10303) pour
  la 3D, STL pour l'impression (fiches 12.4 et 13.7) — en surveillant la **précision** : un STL, c'est le cercle
  dessiné avec des segments du § 2, une surface approchée par de petits triangles plats.

**Une semaine dans le PDM.**
- Lundi, le dessinateur **réserve** le plan de l'équerre et crée la **révision C** (« en cours ») pour ajouter un
  congé. Personne d'autre ne peut la modifier.
- Mardi, le calculateur ouvre la C **en lecture** et relance le calcul.
- Mercredi, le responsable **valide** la C. La B passe en « archivée », toujours lisible.
- Jeudi, l'atelier, qui ne voit que les versions validées, reçoit la C.

*Pourquoi c'est vital : une simulation faite sur la révision B d'une pièce ne vaut rien si l'atelier fabrique la
révision C. Le PDM dit qui a modifié quoi, quand, et quelle version est en vigueur.*

### 7. Les erreurs classiques

1. **Faire une confiance aveugle au calcul** : une belle image n'est pas une preuve ; on vérifie par un ordre de
   grandeur à la main.
2. **Prendre une singularité pour la contrainte de la pièce** : un pic ponctuel sur un angle vif, qui grimpe
   quand on affine le maillage, n'est pas physique.
3. **Négliger une vraie concentration** au prétexte que « c'est peut-être une singularité » : si la valeur se
   stabilise au congé, elle est réelle (fiches 4.1 et 3.5).
4. **Lire les couleurs sans lire l'échelle** : le rouge n'a pas de valeur fixe.
5. **Bloquer trop de choses** dans les conditions aux limites : modèle trop raide, flèche sous-estimée,
   contraintes mal placées.
6. **Comparer Von Mises à Rm** au lieu de Re (ou de Re / s) : on vérifie que la pièce reste élastique.
7. **Garder la valeur la plus flatteuse** quand la main et la simulation divergent : on retient la plus
   défavorable tant que l'écart n'est pas expliqué.
8. **Modifier un plan validé** au lieu de créer une nouvelle révision dans le PDM.

### 8. À retenir

- Simulation par éléments finis : **maillage** (donné au BTS), **conditions aux limites**, résultats en
  **cartographies** (Von Mises, déplacements).
- Lecture : échelle → maximum → crédible ? → **s obtenu = Re / σ éq ≥ s exigé**.
- **Toujours** recouper par un calcul à la main ; si la simulation trouve nettement moins, chercher l'erreur.
- **Pic qui grimpe, pic qui trompe ; pic qui se pose, pic qui compte** : singularité à un angle vif → pas
  physique (mais le coin reste à risque) ; congé qui converge → réel (Kt, fatigue).
- **PDM** : livrables, Gantt, révisions, historique, validation, droits ; format neutre **STEP** (ISO 10303).
""",
    "formules": """
**Condition de résistance** (fiche 12.2) — σ éq (Von Mises) ≤ Rpe = Re / s · s obtenu = Re / σ éq ≥ s exigé

**Ordre de grandeur à la main** (fiche 4.3) — plat encastré, section b × h (h dans le sens de la force) :
M = F × L · I/v = b h² / 6 · σ = M / (I/v) · flèche au bout f = F L³ / (3 E I), I = b h³ / 12

**Concentration réelle** (fiches 4.1 et 3.5) — σ maxi = Kt × σ nominale

**Lire une carte** — échelle → maximum et zone critique → singularité ou vraie concentration ? → s obtenu

**Singularité** — pic ponctuel (angle vif, force ou fixation ponctuelle, bord de zone bloquée) qui augmente à
chaque raffinement · **Convergence** — la valeur se stabilise quand on raffine

**Main contre simulation** — la simulation trouve un peu plus près d'un congé (Kt) : normal ; nettement moins :
erreur à chercher ; tant que ce n'est pas expliqué, valeur la plus défavorable

**PDM** — livrables · Gantt · révision (A, B, C…) · historique · en cours → en validation → validé · droits
(lire / modifier / valider) · format neutre STEP (ISO 10303)
""",
    "exemple": """
### Cas industriel — Valider une équerre avant de la fabriquer

**La situation.** Une équerre de fixation en S235 (Re = 235 MPa) est modélisée et calculée par le calculateur
de l'entreprise. Son aile, de section 30 × 8 mm, se comporte comme un plat encastré dans la jambe et reçoit
F = 500 N à 100 mm de l'angle (les mêmes valeurs qu'au § 4). Le cahier des charges impose **s ≥ 1,5** (donnée
d'énoncé). Le technicien reçoit la note de calcul et doit dire si la pièce peut partir en fabrication.

**Ce que montre la note (résultats fournis).**
- Carte de Von Mises : environ **150 MPa** dans la section de l'angle, sur les faces haute et basse de l'aile ; un
  **pic rouge de 380 MPa** exactement dans l'angle intérieur, dessiné **vif** sur la maquette.
- Calcul relancé avec un maillage deux fois plus fin : le pic passe à **520 MPa**.

**La lecture critique.**
1. **Ordre de grandeur** : à la main, σ ≈ 156 MPa dans la section de l'angle — cohérent avec les 150 MPa de la
   carte. Le modèle est crédible.
2. **Le pic de 380 MPa** est ponctuel, sur un angle vif, et grimpe à 520 MPa quand on affine : c'est une
   **singularité**, pas la contrainte réelle. On ne conclut pas « la pièce casse », mais on ne l'ignore pas non
   plus : la vraie pièce aura un rayon, qu'il faut **dessiner** et calculer.
3. **Le congé est ajouté** sur la maquette (nouvelle **révision** dans le PDM) et le calcul relancé : sur les
   derniers maillages, **170, 174, 175 MPa** — la valeur **converge**. C'est une vraie concentration de
   contrainte, un peu au-dessus des 156 MPa nominaux, comme attendu (Kt).
4. **Conclusion** : s obtenu = 235 / 175 ≈ **1,34**, inférieur au s exigé de 1,5. **Refusé en l'état** : le
   technicien demande d'augmenter l'épaisseur ou le rayon du congé, puis un nouveau calcul. Ce pic au congé est
   aussi l'endroit où démarrerait une fissure de fatigue si la charge est répétée (fiche 3.5).

**Ce que le cas apprend.** La simulation n'a pas « donné la réponse » : c'est la **lecture critique** — ordre de
grandeur, singularité, convergence, coefficient de sécurité — qui a permis de décider. Et c'est le PDM qui
garantit que l'atelier fabriquera bien la révision avec le congé.
""",
    "exercice": """
### Exercice — Lire et critiquer une note de calcul

Un plat en **S355** (Re = 355 MPa), de section **40 × 10 mm** (épaisseur 10 mm dans le sens de la force), est
encastré et reçoit une force **F = 1 200 N** à **150 mm** de l'encastrement. Le s exigé est **s ≥ 2** (données
d'énoncé). La simulation fournie affiche environ **165 MPa** sur la face supérieure, **dans la section
d'encastrement**, à quelques millimètres de l'angle vif ; et un pic de **610 MPa** dans l'angle vif lui-même, qui
passe à **830 MPa** avec un maillage plus fin.

**1.** Calcule à la main la contrainte de flexion dans la section d'encastrement.

**2.** La simulation est-elle cohérente avec ce calcul ? Que faut-il faire de l'écart ?

**3.** Que penser du pic de 610 MPa ? Justifie avec deux indices.

**4.** Entre la valeur de la simulation (165 MPa) et ton calcul à la main, laquelle retiens-tu pour conclure, et
pourquoi ? Calcule le coefficient de sécurité correspondant et dis si la pièce peut partir en fabrication.

**5.** Le dessinateur modifie la pièce et crée la révision C du plan. Pourquoi ne modifie-t-il pas directement la
révision B, déjà validée ?
""",
    "corrige": """
### Corrigé, en six temps

#### 1. Ce que dit l'énoncé

Plat S355 (Re = 355 MPa), section 40 × 10 mm, F = 1 200 N à L = 150 mm, s exigé ≥ 2. Simulation : ≈ 165 MPa dans
la section d'encastrement ; pic de 610 puis 830 MPa à l'angle vif.

#### 2. Quelle règle, et pourquoi

> σ = M / (I/v), avec M = F × L et I/v = b h² / 6 ; s obtenu = Re / σ éq ≥ s exigé ;
> une singularité est un pic ponctuel, sur un angle vif, qui grimpe quand on affine le maillage ;
> si la simulation trouve nettement moins que la main dans la section la plus chargée, on cherche l'erreur et,
> tant qu'elle n'est pas expliquée, on retient la valeur la plus défavorable.

#### 3. Les conversions

Tout en N et mm : les contraintes sortent en N/mm² = MPa.

#### 4. Le remplacement

M = 1 200 × 150 = 180 000 N·mm ; I/v = 40 × 10² / 6 = 4 000 / 6 ≈ 666,7 mm³.

#### 5. Le calcul (et la lecture)

**1.** σ = 180 000 / 666,7 ≈ **270 MPa**.

**2.** **Non.** Dans la section d'encastrement, la simulation devrait trouver au moins la valeur nominale (un peu
plus près de l'angle) ; elle trouve 165 MPa, près de 40 % de moins. C'est un écart important : il faut
l'**expliquer** avant de conclure. Pistes à vérifier avec le calculateur : une zone bloquée qui déborde au-delà
du vrai encastrement (elle raccourcit le bras de levier, donc le moment), une force mal placée ou mal saisie, une
erreur d'unité.

**3.** C'est une **singularité** : le pic est **ponctuel, sur un angle vif**, et il **grimpe** (610 → 830 MPa)
quand on affine le maillage au lieu de se stabiliser. Ce n'est pas une contrainte physique — mais le coin devra
recevoir un congé sur la vraie pièce, car c'est une zone à risque en fatigue.

**4.** On retient **270 MPa**, la valeur la plus défavorable, tant que l'écart n'est pas expliqué : le calcul à la
main repose sur trois données que l'on peut vérifier ligne par ligne, alors que le modèle contient des dizaines de
réglages qu'on ne voit pas sur l'image. s obtenu = 355 / 270 ≈ **1,31** < 2 : **refusé en l'état**. Le technicien
renvoie la note au calculateur avec deux demandes : vérifier les conditions aux limites, puis proposer une
modification (épaisseur, congé) avec un nouveau calcul. *Avec les 165 MPa de la simulation, on aurait trouvé
s ≈ 2,15 et accepté la pièce à tort : c'est exactement le piège de la confiance aveugle.*

**5.** Parce qu'un document **validé** ne se modifie plus : on crée une **nouvelle révision** (C) qui suit à son
tour le circuit de validation, et la révision B reste **lisible et archivée** — on sait ce qui a été fabriqué ou
calculé avec B, et qui a changé quoi.

#### 6. La vérification

**Unités** : N·mm / mm³ = N/mm² = MPa. **Ordre de grandeur** : 270 MPa reste sous Re = 355 MPa, la pièce ne
plastifie pas, mais la marge exigée (s ≥ 2) n'est pas atteinte.
""",
}

# ===========================================================================
# 3. MÉTHODE
# ===========================================================================
MTH_12_9 = ("12.9", "Lire et critiquer un résultat de simulation", [
    "**Vérifier le modèle** : matériau (Re), conditions aux limites (fixations là où la pièce est vraiment tenue, "
    "forces sur de vraies surfaces), maillage donné.",
    "**Lire la carte** : l'échelle d'abord (unité, valeurs), puis le maximum et sa position (zone critique).",
    "**Recouper à la main** : un ordre de grandeur de RDM (σ = M / (I/v)…) doit retrouver la simulation loin des "
    "singularités ; si la simulation trouve nettement moins, chercher l'erreur et garder la valeur la plus défavorable.",
    "**Trier les pics** : ponctuel sur un angle vif et qui grimpe au raffinement → singularité ; stable au congé "
    "→ vraie concentration (fiches 4.1 et 3.5, fatigue).",
    "**Conclure** : s obtenu = Re / σ éq comparé au s exigé ; si refusé, proposer une modification (épaisseur, "
    "congé) et une nouvelle révision dans le PDM.",
], "Équerre S235 : carte ≈ 150 MPa, cohérente avec 156 MPa à la main ; pic de 380 → 520 MPa à l'angle vif = "
   "singularité ; congé ajouté : 170, 174, 175 MPa (converge) ; s obtenu = 235/175 ≈ 1,34 < 1,5 exigé → refusé.")

# ===========================================================================
# 4. ATELIERS (fin de liste ATELIERS, après at179)
# ===========================================================================
ATELIERS_NOUVEAUX = [
    {
        "id": "at180",
        "chapitre": "Bloc 12",
        "titre": "Lire une carte de Von Mises et la recouper à la main",
        "theme": "Résistance des matériaux",
        "fiche": "12.9",
        "figure": "fem_von_mises",
        "vocabulaire": [
            ("Carte de Von Mises",
             "la pièce colorée selon la contrainte équivalente de Von Mises, avec une échelle en MPa."),
            ("Ordre de grandeur",
             "un calcul simple à la main qui dit si le résultat du logiciel est crédible."),
            ("Singularité",
             "un pic ponctuel, à un angle vif, qui grimpe quand on affine le maillage : pas physique."),
        ],
        "enonce": "Un plat en S235 (Re = 235 MPa), de section b × h = 30 × 8 mm (h dans le sens de la force), est "
                  "encastré et reçoit une force F = 500 N à L = 100 mm de l'encastrement. La simulation fournie "
                  "(figure) affiche environ 150 MPa sur les faces haute et basse de la section d'encastrement et un "
                  "pic de 380 MPa à l'angle vif de la fixation (données d'énoncé).",
        "etapes": [
            {"type": "qcm", "label": "Que montre la carte ?",
             "question": "Que représentent les couleurs de la carte ?",
             "options": ["La température de la pièce",
                         "Les déplacements de la pièce, en mm",
                         "La contrainte équivalente de Von Mises, lue sur l'échelle en MPa"], "bonne": 2,
             "indice": "Regarde le titre de l'échelle de couleurs.",
             "diagnostics": {0: "Ce serait une simulation thermique ; ici l'échelle est en MPa.",
                             1: "Une carte de déplacements existe aussi, mais elle serait en mm ; l'échelle est "
                                "en MPa."}},
            {"type": "numerique", "label": "Contrainte à la main",
             "unite": "MPa", "attendu": 156.25, "tol": 1.5,
             "consigne": "Calcule à la main la contrainte de flexion dans la section d'encastrement : "
                         "σ = M / (I/v), avec M = F × L et I/v = b h² / 6.",
             "indice": "M = 500 × 100 N·mm ; I/v = 30 × 8² / 6 mm³.",
             "pieges": [(26.04, "26 MPa : tu as oublié le 6 de I/v = b h²/6."),
                        (41.67, "42 MPa : tu as inversé b et h (I/v = b² h / 6 = 30² × 8 / 6). C'est l'épaisseur "
                                "fléchie h = 8 mm qui est au carré.")],
             "aide": "M = 50 000 N·mm ; I/v = 320 mm³ ; σ = 50 000 / 320 ≈ 156 MPa."},
            {"type": "numerique", "label": "Coefficient de sécurité",
             "unite": "", "attendu": 1.504, "tol": 0.02,
             "consigne": "Avec la contrainte crédible (≈ 156 MPa), calcule le coefficient de sécurité s = Re / σ.",
             "indice": "s = 235 / 156.",
             "pieges": [(0.664, "0,66 : tu as calculé σ / Re. Le coefficient de sécurité est Re / σ."),
                        (0.618, "0,62 : tu as pris le pic de 380 MPa (235/380). Ce pic est une singularité.")],
             "aide": "s = 235 / 156,25 ≈ 1,50.",
             "depend_de": {"etape": 2, "formule": lambda v: 235 / v}},
            {"type": "qcm", "label": "Le pic de 380 MPa",
             "question": "Relancé avec un maillage plus fin, le pic de l'angle vif passe de 380 à 520 MPa. Qu'en "
                         "conclure ?",
             "options": ["C'est une singularité du modèle : ce n'est pas la contrainte réelle",
                         "La pièce va casser : 520 MPa dépasse Re",
                         "Le maillage fin est faux, il faut garder le maillage grossier"], "bonne": 0,
             "indice": "Une vraie contrainte se stabilise quand on raffine.",
             "diagnostics": {1: "Un pic ponctuel à un angle vif qui grimpe à chaque raffinement n'est pas physique ; "
                                "on ne conclut pas sur cette valeur.",
                             2: "Le maillage fin n'est pas faux : il révèle que la valeur ne se stabilise pas, signe "
                                "d'une singularité."}},
        ],
        "corrige": {
            "enonce": "Plat S235, 30 × 8 mm, F = 500 N à 100 mm ; carte ≈ 150 MPa, pic 380 → 520 MPa à l'angle vif.",
            "regle": "**Lire l'échelle** ; **recouper à la main** σ = M/(I/v), I/v = b h²/6 ; **s = Re / σ** ; un pic "
                    "ponctuel à un angle vif qui grimpe au raffinement est une **singularité**.",
            "conversions": "N et mm : les contraintes sortent en MPa.",
            "remplacement": "M = 500 × 100 = 50 000 N·mm ; I/v = 30 × 64 / 6 = 320 mm³.",
            "calcul": "σ = 50 000 / 320 ≈ **156 MPa** ; s = 235 / 156,25 ≈ **1,50** ; le pic est une **singularité**.",
            "verification": "Le calcul à la main (156 MPa) retrouve les ≈ 150 MPa de la carte : le modèle est crédible "
                            "loin de l'angle vif.",
        },
        "a_retenir": "À retenir : échelle → maximum → crédible ? → s = Re / σ. Une simulation se recoupe toujours par "
                     "un ordre de grandeur à la main, et un pic qui grimpe au raffinement n'est pas physique.",
    },
    {
        "id": "at181",
        "chapitre": "Bloc 12",
        "titre": "Critiquer une simulation et gérer ses révisions",
        "theme": "Résistance des matériaux",
        "fiche": "12.9",
        "figure": "fem_singularite",
        "vocabulaire": [
            ("Conditions aux limites",
             "les fixations et les chargements déclarés au logiciel."),
            ("Convergence",
             "la valeur ne bouge presque plus quand on affine le maillage : on peut l'exploiter."),
            ("Révision",
             "une nouvelle version d'un document validé (indice A, B, C…), suivie dans le PDM."),
        ],
        "enonce": "L'équerre en S235 (Re = 235 MPa) de la fiche est recalculée avec un congé à la place de l'angle vif. "
                  "Le modèle retenu fixe l'équerre sur ses deux trous de vis, en appui sur le bâti. Le cahier des "
                  "charges exige s ≥ 1,5 (données d'énoncé).",
        "etapes": [
            {"type": "qcm", "label": "Les appuis",
             "question": "Un collègue propose de bloquer toute la face arrière de l'équerre, alors que la vraie pièce "
                         "ne tient que par deux vis. Quel serait l'effet sur le résultat ?",
             "options": ["Aucun : le logiciel corrige de lui-même",
                         "Le modèle serait trop raide : la flèche serait sous-estimée et les contraintes autour des "
                         "vis ne seraient pas représentées",
                         "Le modèle serait trop souple : la flèche serait surestimée"], "bonne": 1,
             "indice": "Bloquer plus que la réalité, c'est rendre la pièce plus rigide.",
             "diagnostics": {0: "Le logiciel calcule exactement ce qu'on lui décrit ; il ne devine pas les vraies "
                                "fixations.",
                             2: "C'est l'inverse : bloquer davantage rigidifie le modèle ; la pièce plie moins qu'en "
                                "réalité."}},
            {"type": "qcm", "label": "Convergence au congé",
             "question": "Au congé, trois maillages de plus en plus fins donnent 170, 174 puis 175 MPa. Que vaut ce "
                         "résultat ?",
             "options": ["C'est une singularité, on l'ignore",
                         "C'est faux, car les trois valeurs sont différentes",
                         "La valeur converge : c'est une vraie concentration de contrainte, à exploiter"],
             "bonne": 2,
             "indice": "Une singularité grimpe sans fin ; ici, la valeur se stabilise.",
             "diagnostics": {0: "Une singularité grimpe à chaque raffinement ; ici, la valeur se stabilise vers 175 MPa.",
                             1: "De petites différences qui diminuent sont normales : c'est la convergence."}},
            {"type": "numerique", "label": "Coefficient de sécurité au congé",
             "unite": "", "attendu": 1.343, "tol": 0.02,
             "consigne": "Calcule le coefficient de sécurité s = Re / σ avec la valeur convergée au congé (175 MPa).",
             "indice": "s = 235 / 175.",
             "pieges": [(1.504, "1,50 : c'est le coefficient avec la contrainte nominale (156 MPa). Au congé, la "
                                "contrainte réelle est plus forte : 175 MPa."),
                        (0.745, "0,74 : tu as calculé σ / Re. Le coefficient de sécurité est Re / σ.")],
             "aide": "s = 235 / 175 ≈ 1,34 : inférieur à 1,5, la pièce est refusée en l'état."},
            {"type": "qcm", "label": "La révision",
             "question": "Pour épaissir l'équerre, le dessinateur doit modifier le plan, validé en révision B. Que "
                         "fait-il dans le PDM ?",
             "options": ["Il crée une révision C, qui suivra le circuit de validation ; la B reste archivée",
                         "Il modifie directement la révision B, puisqu'elle est fausse",
                         "Il enregistre une copie du fichier sur son poste"], "bonne": 0,
             "indice": "Un document validé ne se modifie plus.",
             "diagnostics": {1: "On ne modifie jamais un document validé : on perdrait la trace de ce qui a été "
                                "calculé ou fabriqué avec B.",
                             2: "Une copie hors du PDM échappe aux révisions et aux droits : personne ne saurait "
                                "quelle version est la bonne."}},
        ],
        "corrige": {
            "enonce": "Équerre S235 recalculée avec un congé ; s ≥ 1,5 exigé.",
            "regle": "**Appuis trop étendus** → modèle trop raide, flèche sous-estimée, contraintes faussées ; **valeur qui converge** → vraie "
                    "concentration ; **s = Re / σ** ; **document validé** → nouvelle révision.",
            "conversions": "Aucune : contraintes en MPa.",
            "remplacement": "s = 235 / 175.",
            "calcul": "Modèle **trop raide** (à refuser) ; **175 MPa** exploitable ; s ≈ **1,34** < 1,5 → refusé ; **révision C**.",
            "verification": "175 MPa est un peu au-dessus des 156 MPa nominaux : c'est l'effet attendu d'un congé "
                            "(σ maxi = Kt × σ nominale, fiches 4.1 et 3.5, avec Kt un peu supérieur à 1).",
        },
        "a_retenir": "À retenir : un appui mal déclaré fausse tout ; une valeur qui converge se prend en compte ; un "
                     "document validé ne se modifie pas, on crée une révision.",
    },
]

# ===========================================================================
# 5. GÉNÉRATEURS (famille existante « Résistance des matériaux »)
# ===========================================================================
GENERATEUR = '''
def gen_securite_simulation():
    """Coefficient de sécurité à partir d'une carte de Von Mises, en écartant la singularité."""
    nom, Re = random.choice([("S235", 235), ("S355", 355)])
    sig = random.choice([v for v in range(90, 260, 5) if Re / v >= 1.05])
    pic = random.choice([v for v in range(int(Re * 1.4), int(Re * 2.6), 10) if abs(Re / v - sig / Re) > 0.02])
    s = Re / sig
    return {
        "titre": "Simulation — coefficient de sécurité lu sur une carte de Von Mises",
        "enonce": (f"Une pièce en **{nom}** (Re = {Re} MPa) est calculée par éléments finis. La carte de Von Mises "
                   f"affiche environ **{sig} MPa** dans la zone la plus sollicitée, valeur qui se stabilise quand on "
                   f"affine le maillage, et un pic de **{pic} MPa** exactement sur un angle vif, qui augmente à chaque "
                   "raffinement. Quel est le coefficient de sécurité de la pièce (arrondi au centième) ?"),
        "rep": s, "tol": 0.01, "unite": "", "decimales": 2,
        "diag": [
            _diag(sig / Re, "Tu as calculé σ / Re. Le coefficient de sécurité est Re / σ : il doit être supérieur "
                            "à 1 si la pièce tient."),
            _diag(Re / pic, f"Tu as pris le pic de {pic} MPa. Il est ponctuel, sur un angle vif, et grimpe quand on "
                            "affine le maillage : c'est une singularité, pas la contrainte réelle."),
            _diag(Re - sig, "Tu as fait une différence Re − σ : c'est une marge en MPa, pas un coefficient de "
                            "sécurité, qui est un rapport."),
        ],
        "corr": [
            f"**Ce que dit l'énoncé.** {nom}, Re = {Re} MPa ; zone critique ≈ {sig} MPa (stable au raffinement) ; "
            f"pic de {pic} MPa sur un angle vif (grimpe au raffinement).",
            "**Trier les valeurs.** Le pic est ponctuel, sur un angle vif, et ne se stabilise pas : c'est une "
            f"**singularité**. La valeur crédible est {sig} MPa.",
            "**La règle.** Condition de résistance (fiche 12.2) : σ éq ≤ Re / s, donc s = Re / σ éq.",
            f"**Je calcule.** s = {Re} / {sig} = {fr(s, 2)}.",
            "**Je vérifie.** s est un rapport sans unité, supérieur à 1 puisque la contrainte reste sous Re. On le "
            "compare ensuite au coefficient exigé par le cahier des charges.",
        ],
        "indice": "Écarte d'abord la singularité (pic qui grimpe au raffinement), puis s = Re / σ.",
    }


def gen_ordre_grandeur_simulation():
    """Recouper une simulation par un calcul de flexion à la main (plat encastré, section rectangulaire)."""
    while True:   # pièce réaliste : poutre élancée (L/h ≥ 8) et contrainte comprise entre 30 et 250 MPa
        b = random.choice([20, 25, 30, 40, 50])
        h = random.choice([6, 8, 10])
        F = random.choice([200, 300, 500, 800, 1000, 1200])
        L = random.choice([60, 80, 100, 120, 150])
        M = F * L
        w = b * h * h / 6
        sig = M / w
        if L / h >= 8 and 30 <= sig <= 250:
            break
    return {
        "titre": "Simulation — ordre de grandeur à la main",
        "enonce": (f"Avant d'accepter une simulation, on la recoupe à la main. Un plat de section **{b} × {h} mm** "
                   f"(largeur × épaisseur h dans le sens de la force) est encastré et reçoit **{fr(F, 0)} N** à **{L} mm** de "
                   "l'encastrement. Quelle contrainte de flexion attend-on dans la section d'encastrement, en MPa ?"),
        "rep": sig, "tol": max(0.5, sig * 0.01), "unite": "MPa", "decimales": 1,
        "diag": [
            _diag(M / (b * h * h), "Tu as oublié le 6 : pour une section rectangulaire, I/v = b h² / 6."),
            _diag(M / (b * b * h / 6), "Tu as inversé b et h : c'est l'épaisseur h, dans le sens de la force, "
                                       "qui est au carré : I/v = b h² / 6."),
            _diag(M / (b * h ** 3 / 12), "Tu as divisé par I = b h³/12 au lieu de I/v = b h²/6 : σ = M / (I/v)."),
        ],
        "corr": [
            f"**Ce que dit l'énoncé.** Section {b} × {h} mm, F = {fr(F, 0)} N à L = {L} mm de l'encastrement.",
            f"**Le moment à l'encastrement.** M = F × L = {fr(F, 0)} × {L} = {fr(M, 0)} N·mm.",
            f"**Le module de flexion** (I/v, fiche 4.3). I/v = b h² / 6 = {b} × {h}² / 6 = {fr(w, 1)} mm³.",
            f"**Je calcule.** σ = M / (I/v) = {fr(M, 0)} / {fr(w, 1)} = {fr(sig, 1)} MPa.",
            "**À quoi ça sert.** Loin des angles vifs, la carte de Von Mises doit afficher une valeur proche (un peu "
            "plus près d'un congé : Kt). Si elle affiche nettement moins, l'écart doit être expliqué (appuis, force, "
            "unités) ; en attendant, on garde la valeur la plus défavorable.",
        ],
        "indice": "σ = M / (I/v), avec M = F × L et I/v = b h² / 6.",
    }
'''

# ===========================================================================
# 6. QUIZ — nouvelle catégorie « Simulation et chaîne numérique »
#    positions de la bonne réponse : 1, 3, 0, 2, 2, 0, 3, 1
# ===========================================================================
QUIZ_SIMULATION = [
    ("Au BTS CPI, qu'attend le référentiel face à une simulation par éléments finis fournie ?",
     ["Savoir programmer le solveur", "Savoir interpréter et critiquer le résultat, et dialoguer avec un spécialiste",
      "Savoir choisir seul la taille de maillage de tout problème", "Recopier les valeurs maximales sans les discuter"], 1,
     "Le programme demande d'interpréter les résultats en autonomie ; la taille et le type de maillage sont donnés ; "
     "pour les cas simples on conduit la simulation, pour les cas complexes on dialogue avec un spécialiste.", "Base"),
    ("Toute la face arrière d'une pièce est bloquée dans le modèle, alors qu'elle ne tient que par deux vis. "
     "Conséquence ?",
     ["Le modèle est trop souple : la flèche est surestimée", "Le calcul ne peut pas aboutir",
      "Aucune, le logiciel corrige",
      "Le modèle est trop raide : la flèche est sous-estimée et les contraintes sont faussées"], 3,
     "Bloquer plus que la réalité rigidifie le modèle : la pièce plie moins qu'en vrai, les contraintes autour des "
     "vis ne sont pas calculées et un pic artificiel apparaît souvent au bord de la zone bloquée.", "Piège"),
    ("Sur une carte de Von Mises, que faut-il lire en premier ?",
     ["L'échelle : unité et valeurs associées aux couleurs", "La couleur rouge, qui signale la rupture",
      "Le nombre de nœuds du maillage", "La couleur bleue, qui signale la zone critique"], 0,
     "Les couleurs n'ont pas de valeur fixe : un rouge peut valoir 20 MPa sur une pièce et 400 MPa sur une autre.",
     "Base"),
    ("Un pic de contrainte ponctuel, exactement sur un angle vif, augmente à chaque raffinement du maillage. "
     "C'est :",
     ["La contrainte réelle maximale de la pièce", "Une erreur de saisie du matériau",
      "Une singularité du modèle, pas une contrainte physique", "Une preuve que le maillage fin est faux"], 2,
     "En élasticité, la contrainte au sommet d'un angle rentrant parfaitement vif n'est pas bornée : le calcul "
     "affiche une valeur qui grimpe sans se stabiliser.", "Intermédiaire"),
    ("Au congé d'une pièce, trois maillages de plus en plus fins donnent 170, 174 puis 175 MPa. Que faire de "
     "cette valeur ?",
     ["L'ignorer, c'est une singularité", "La diviser par Kt", "La prendre en compte : elle converge, c'est une "
      "vraie concentration de contrainte", "Garder la première valeur, 170 MPa"], 2,
     "Une valeur qui se stabilise est exploitable ; c'est la concentration de contrainte de la fiche 3.5, "
     "importante en fatigue (fiches 4.1 et 3.5).", "Intermédiaire"),
    ("Pour conclure sur une pièce en acier à partir d'une carte de Von Mises, on calcule :",
     ["s = Re / σ éq, comparé au coefficient de sécurité exigé", "s = σ éq / Re", "s = Rm − σ éq",
      "s = σ éq / Rm"], 0,
     "Condition de résistance de la fiche 12.2 : σ éq ≤ Rpe = Re / s.", "Base"),
    ("La simulation affiche 60 MPa là où le calcul de flexion à la main donne 270 MPa. Que conclure ?",
     ["La simulation a raison, elle est plus précise", "La pièce est quatre fois plus solide que prévu",
      "On fait la moyenne des deux", "Il y a une erreur de modèle à chercher (appuis, force, unités)"], 3,
     "Loin des singularités, simulation et calcul à la main doivent se recouper ; un écart de ce niveau signale "
     "une erreur.", "Piège"),
    ("Dans un PDM, que fait-on pour modifier un plan déjà validé en révision B ?",
     ["On écrase la révision B", "On crée une révision C qui suit le circuit de validation ; B reste archivée",
      "On envoie le fichier modifié par courriel à l'atelier", "On supprime l'historique pour repartir propre"], 1,
     "Un document validé ne se modifie plus : la nouvelle révision garde la trace de qui a changé quoi, et "
     "l'ancienne reste lisible.", "Base"),
]
