# -*- coding: utf-8 -*-
# BROUILLON — fiche 6.21 « Masse, centre de gravité, inertie, PFD et équilibrage » (référentiel S3.2.5).
# Rien de ceci n'est encore dans app.py.
#
# Sources des valeurs utilisées :
# - masse volumique de l'acier : 7 850 kg/m³, table MATERIAUX de l'application (S235, C45…) ;
# - moments d'inertie : formules classiques des solides homogènes (cylindre plein ½ m R², tube
#   ½ m (R² + r²), anneau mince m R², barre mince m L²/12, masse ponctuelle m d²) et théorème de Huygens ;
# - g = 9,81 m/s² ;
# - toutes les autres valeurs (dimensions, masses de balourd, vitesses, charges) sont des DONNÉES D'ÉNONCÉ.
# - Aucune classe de qualité d'équilibrage chiffrée (norme ISO 21940-11 citée sans valeur).
import math

# ===========================================================================
# 1. FIGURES
# ===========================================================================

def cdg_barycentre():
    p = [_k_defs(), _txt(30, 24, "Centre de gravité d'un arbre étagé : le barycentre des deux tronçons", 13, TRAIT, "start", True)]
    k = 3.2  # px par mm
    ox, oy = 90, 150
    p.append(f"<line x1='{ox - 20}' y1='{oy}' x2='{ox + 170 * k}' y2='{oy}' stroke='{AXE}' stroke-width='1' stroke-dasharray='10 3 2 3'/>")
    p.append(f"<rect x='{ox}' y='{oy - 20 * k}' width='{100 * k}' height='{40 * k}' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.8'/>")
    p.append(f"<rect x='{ox + 100 * k}' y='{oy - 10 * k}' width='{60 * k}' height='{20 * k}' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.8'/>")
    p.append(_txt(ox + 50 * k, oy - 20 * k - 8, "tronçon 1 : Ø40 × 100", 11, TRAIT, "middle", True))
    p.append(_txt(ox + 130 * k, oy - 10 * k - 8, "tronçon 2 : Ø20 × 60", 11, TRAIT, "middle", True))
    for x, nom, c in ((50, "G1", ALESAGE), (130, "G2", ALESAGE)):
        p.append(f"<circle cx='{ox + x * k}' cy='{oy}' r='5' fill='{c}'/>")
        p.append(_txt(ox + x * k, oy + 22, f"{nom} (x = {x})", 11, c, "middle", True))
    xg = 60.43
    p.append(f"<circle cx='{ox + xg * k:.1f}' cy='{oy}' r='7' fill='{ALERTE}'>"
             "<animate attributeName='r' values='6;9;6' dur='1.6s' repeatCount='indefinite'/></circle>")
    p.append(_txt(ox + xg * k, oy - 20 * k - 26, "G (x ≈ 60,4)", 12, ALERTE, "middle", True))
    p.append(f"<line x1='{ox + xg * k:.1f}' y1='{oy - 20 * k - 22}' x2='{ox + xg * k:.1f}' y2='{oy - 8}' stroke='{ALERTE}' stroke-dasharray='3 3'/>")
    p.append(_txt(ox, oy + 20 * k + 22, "x en mm, depuis la face gauche ; même matériau : les masses sont proportionnelles aux volumes.", 10, FIN))
    p.append(f"<rect x='30' y='{oy + 20 * k + 34}' width='730' height='52' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, oy + 20 * k + 56, "xG = (m1 x1 + m2 x2) / (m1 + m2) = (40² × 100 × 50 + 20² × 60 × 130) / (40² × 100 + 20² × 60) ≈ 60,4 mm", 12, TRAIT, "start", True))
    p.append(_txt(46, oy + 20 * k + 76, "G est attiré vers le tronçon le plus lourd : il est bien plus près de G1 que de G2.", 11, FIN))
    return _svg("".join(p), 790, 314)


def inertie_repartition():
    p = [_k_defs(), _txt(30, 24, "Même masse, même rayon extérieur : l'inertie dépend de l'endroit où est la matière", 13, TRAIT, "start", True)]
    cas = ((30, "DISQUE PLEIN", "J = ½ m R²", 0.5, False), (275, "ANNEAU MINCE", "J ≈ m R²", 1.0, True),
           (520, "MASSE PRÈS DE L'AXE", "J petit : matière près de l'axe", 0.117, None))
    for x0, nom, form, f, typ in cas:
        cx, cy = x0 + 112, 150
        p.append(f"<rect x='{x0}' y='40' width='225' height='236' rx='8' fill='#ffffff' stroke='{ALESAGE}' stroke-width='1.8'/>")
        p.append(_txt(cx, 62, nom, 11, ALESAGE, "middle", True))
        g = f"<g><animateTransform attributeName='transform' type='rotate' values='0 {cx} {cy}; 360 {cx} {cy}' dur='4s' repeatCount='indefinite'/>"
        if typ is False:
            g += f"<circle cx='{cx}' cy='{cy}' r='62' fill='#cbd5e1' stroke='{TRAIT}' stroke-width='2'/>"
        elif typ is True:
            g += f"<circle cx='{cx}' cy='{cy}' r='62' fill='none' stroke='#94a3b8' stroke-width='14'/>"
            g += f"<circle cx='{cx}' cy='{cy}' r='62' fill='none' stroke='{TRAIT}' stroke-width='1'/>"
        else:
            g += f"<circle cx='{cx}' cy='{cy}' r='62' fill='none' stroke='{TRAIT}' stroke-width='1' stroke-dasharray='4 4'/>"
            g += f"<circle cx='{cx}' cy='{cy}' r='30' fill='#94a3b8' stroke='{TRAIT}' stroke-width='2'/>"
        g += f"<line x1='{cx}' y1='{cy}' x2='{cx + 62}' y2='{cy}' stroke='{ALERTE}' stroke-width='2'/></g>"
        p.append(g)
        p.append(f"<circle cx='{cx}' cy='{cy}' r='4' fill='{TRAIT}'/>")
        p.append(_txt(cx, cy + 76, "axe au centre ; rayon extérieur R", 9, FIN, "middle"))
        if typ is None:
            p.append(_txt(cx, cy - 68, "même rayon R (vide)", 9, FIN, "middle"))
        p.append(_txt(cx, 244, form, 12, ARBRE, "middle", True))
        p.append(f"<rect x='{x0 + 20}' y='252' width='{185 * f:.0f}' height='8' rx='3' fill='{ARBRE}' opacity='0.7'/>")
        p.append(_txt(x0 + 20, 272, "inertie (barre proportionnelle)", 9, FIN))
    p.append(f"<rect x='30' y='288' width='730' height='52' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 310, "J = Σ m × r² : une masse compte avec le CARRÉ de sa distance à l'axe.", 12, TRAIT, "start", True))
    p.append(_txt(46, 330, "Un volant met sa matière en jante ; un rotor qui doit accélérer vite la garde près de l'axe.", 11, FIN))
    return _svg("".join(p), 790, 354)


def huygens_axes():
    p = [_k_defs(), _txt(30, 24, "Théorème de Huygens : changer d'axe, c'est ajouter m × d²", 13, TRAIT, "start", True)]
    cx, cy = 150, 172
    p.append(f"<circle cx='{cx}' cy='{cy}' r='50' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<circle cx='{cx}' cy='{cy}' r='5' fill='{ALESAGE}'/>")
    p.append(_txt(cx, cy + 22, "G : axe (G)", 11, ALESAGE, "middle", True))
    p.append(_txt(cx + 55, cy + 70, "axes perpendiculaires à l'écran", 9, FIN, "middle"))
    ax = cx + 110
    p.append(f"<circle cx='{ax}' cy='{cy}' r='6' fill='{ALERTE}'/>")
    p.append(_txt(ax, cy + 22, "axe Δ", 11, ALERTE, "middle", True))
    p.append(_k_fl(cx + 6, cy - 40, ax - 4, cy - 40, TRAIT, "kk", 1.6))
    p.append(_k_fl(ax - 6, cy - 40, cx + 4, cy - 40, TRAIT, "kk", 1.6))
    p.append(_txt((cx + ax) / 2, cy - 48, "d", 13, TRAIT, "middle", True))
    p.append(f"<g><animateTransform attributeName='transform' type='rotate' values='0 {ax} {cy}; 360 {ax} {cy}' dur='6s' repeatCount='indefinite'/>"
             f"<circle cx='{cx}' cy='{cy}' r='50' fill='none' stroke='{ALERTE}' stroke-width='1.4' stroke-dasharray='6 4'/></g>")
    x0 = 470
    p.append(f"<rect x='{x0}' y='44' width='305' height='236' rx='6' fill='#ffffff' stroke='{FIN}'/>")
    for i, (t, c, g) in enumerate((("J_Δ = J_G + m × d²", ALERTE, True), ("", TRAIT, False),
                                   ("J_G : inertie autour de l'axe parallèle", TRAIT, False),
                                   ("passant par le centre de gravité G ;", TRAIT, False),
                                   ("d : distance entre les deux axes.", TRAIT, False), ("", TRAIT, False),
                                   ("J_G est le plus petit des J autour d'axes", TRAIT, False),
                                   ("parallèles : décentrer coûte toujours.", TRAIT, False), ("", TRAIT, False),
                                   ("Sert à : trou décentré, bossage, pièce", ARBRE, True),
                                   ("composée, axe de rotation décalé.", ARBRE, True))):
        if t:
            p.append(_txt(x0 + 14, 70 + 19 * i, t, 13 if i == 0 else 12, c, "start", g))
    p.append(_txt(30, 334, "Disque gris : la pièce ; cercle rouge pointillé : la même pièce qui tourne autour de l'axe Δ décalé.", 10, FIN))
    return _svg("".join(p), 790, 346)


def pfd_treuil():
    p = [_k_defs(), _txt(30, 24, "PFD sur un treuil : la charge en translation, le tambour en rotation", 13, TRAIT, "start", True)]
    cx, cy, r = 170, 100, 40
    p.append(f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<circle cx='{cx}' cy='{cy}' r='4' fill='{TRAIT}'/>")
    p.append(_txt(cx, cy - r - 8, "tambour (J, rayon r)", 11, TRAIT, "middle", True))
    p.append(f"<path d='M {cx + 24} {cy + 18} A 30 30 0 0 0 {cx + 18} {cy - 24}' fill='none' stroke='{ALESAGE}' stroke-width='2.4' marker-end='url(#kb)'/>")
    p.append(_txt(cx + 2, cy - 14, "Cm", 12, ALESAGE, "middle", True))
    p.append(f"<line x1='{cx}' y1='{cy + 8}' x2='{cx + r}' y2='{cy + 8}' stroke='{TRAIT}' stroke-width='1'/>")
    p.append(_txt(cx + r / 2, cy + 22, "r", 11, TRAIT, "middle", True))
    p.append(_k_fl(cx + r + 4, cy + 6, cx + r + 4, cy + 44, OK, "kg", 2))
    p.append(_txt(cx - 2, cy + 62, "T tire le tambour vers le bas", 9, OK, "end", True))
    p.append(f"<line x1='{cx + r}' y1='{cy}' x2='{cx + r}' y2='230' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<g><animateTransform attributeName='transform' type='translate' values='0,0; 0,-14' dur='2s' repeatCount='indefinite'/>"
             f"<rect x='{cx + r - 30}' y='230' width='60' height='50' fill='#cbd5e1' stroke='{TRAIT}' stroke-width='2'/>"
             f"<text x='{cx + r}' y='260' text-anchor='middle' font-size='12' font-weight='600' fill='{TRAIT}'>m</text></g>")
    p.append(_k_fl(cx + r + 50, 250, cx + r + 50, 212, OK, "kg", 2.4))
    p.append(_txt(cx + r + 58, 230, "T (câble)", 11, OK, "start", True))
    p.append(_k_fl(cx + r + 50, 268, cx + r + 50, 306, ALERTE, "kr", 2.4))
    p.append(_txt(cx + r + 58, 296, "m × g (poids)", 11, ALERTE, "start", True))
    p.append(_k_fl(cx + r - 50, 280, cx + r - 50, 240, ARBRE, "ko", 2))
    p.append(_txt(cx + r - 56, 262, "a", 12, ARBRE, "end", True))
    x0 = 400
    p.append(f"<rect x='{x0}' y='44' width='370' height='262' rx='6' fill='#ffffff' stroke='{FIN}'/>")
    for i, (t, c, g) in enumerate((("1. J'isole la charge (+ vers le haut) :", TRAIT, True),
                                   ("T − m g = m a  →  T = m (g + a)", OK, True), ("", TRAIT, False),
                                   ("2. J'isole le tambour (rotation) :", TRAIT, True),
                                   ("Cm − r × T = J × α, avec α = a / r", ALESAGE, True),
                                   ("→ Cm = J α + r m (g + a)", ALESAGE, True), ("", TRAIT, False),
                                   ("Le câble transmet T dans les deux sens :", TRAIT, False),
                                   ("il tire la charge vers le haut et freine", TRAIT, False),
                                   ("le tambour (bras de levier r).", TRAIT, False), ("", TRAIT, False),
                                   ("Une seule accélération (a = r α) relie", FIN, False),
                                   ("les deux isolements.", FIN, False))):
        if t:
            p.append(_txt(x0 + 14, 68 + 18 * i, t, 12, c, "start", g))
    return _svg("".join(p), 790, 320)


def equilibrage():
    p = [_k_defs(), _txt(30, 24, "Équilibrage d'un rotor : statique (G sur l'axe) et dynamique (les masses se compensent plan par plan)", 13, TRAIT, "start", True)]
    cas = ((30, "ÉQUILIBRÉ", OK, ((0, 0, 0),), "ni force ni couple tournants"),
           (275, "BALOURD STATIQUE", ALERTE, ((1, 0, 0),), "une force tournante : G hors de l'axe"),
           (520, "BALOURD DYNAMIQUE", ARBRE, ((1, -1, 0), (-1, 1, 0)), "G sur l'axe, mais un couple tournant"))
    for x0, nom, c, masses, leg in cas:
        p.append(f"<rect x='{x0}' y='40' width='235' height='250' rx='8' fill='#ffffff' stroke='{c}' stroke-width='2'/>")
        p.append(_txt(x0 + 117, 62, nom, 11, c, "middle", True))
        ox, oy = x0 + 30, 160
        # arbre et paliers
        p.append(f"<line x1='{ox}' y1='{oy}' x2='{ox + 175}' y2='{oy}' stroke='{TRAIT}' stroke-width='3'/>")
        for xp in (ox + 8, ox + 167):
            p.append(f"<rect x='{xp - 8}' y='{oy + 4}' width='16' height='14' fill='{FIN}'/>")
        p.append(_txt(ox + 8, oy + 34, "palier A", 9, FIN, "middle"))
        p.append(_txt(ox + 87, 278, "rotor vu de côté (2 disques)", 9, FIN, "middle"))
        p.append(_txt(ox + 167, oy + 34, "palier B", 9, FIN, "middle"))
        # rotor (vu de côté) : deux disques
        for xd in (ox + 60, ox + 115):
            p.append(f"<rect x='{xd - 7}' y='{oy - 50}' width='14' height='100' rx='3' fill='#e2e8f0' stroke='{TRAIT}'/>")
        for (signe, cote, _z) in masses:
            if signe == 0:
                continue
            xd = ox + 60 if cote <= 0 else ox + 115
            if len(masses) == 1:
                xd = ox + 87
            y = oy - 42 * signe
            p.append(f"<circle cx='{xd}' cy='{y}' r='7' fill='{c}'>"
                     f"<animate attributeName='cy' values='{y};{2 * oy - y};{y}' dur='1.2s' repeatCount='indefinite'/></circle>")
        if len(masses) == 1 and masses[0][0] != 0:
            p.append(_txt(ox + 87, oy + 66, "masse en trop (plan milieu)", 9, c, "middle", True))
            p.append(_k_fl(ox + 87, oy - 52, ox + 87, oy - 80, c, "kr", 2))
            p.append(_txt(ox + 96, oy - 70, "F = mb r ω²", 10, c, "start", True))
        if len(masses) == 2:
            p.append(_txt(ox + 87, 80, "deux masses opposées, décalées", 9, c, "middle", True))
            p.append(_k_fl(ox + 60, oy - 52, ox + 60, oy - 72, c, "ko", 2))
            p.append(_k_fl(ox + 115, oy + 52, ox + 115, oy + 74, c, "ko", 2))
            p.append(_txt(ox + 64, oy - 62, "F", 10, c, "start", True))
            p.append(_txt(ox + 119, oy + 70, "F", 10, c, "start", True))
            p.append(_txt(ox + 87, oy - 6, "z", 10, c, "middle", True))
            p.append(_txt(ox + 8, oy - 8, "↑", 12, c, "middle", True))
            p.append(_txt(ox + 182, oy + 14, "↓", 12, c, "middle", True))
        p.append(_txt(x0 + 117, 240, leg, 10, c, "middle", True))
        p.append(_txt(x0 + 117, 258, ("sur couteaux : ne roule pas ; en rotation : ne vibre pas" if nom == "ÉQUILIBRÉ" else ("test des couteaux : il roule" if "STATIQUE" in nom else "immobile sur couteaux, vibre en rotation")), 9, FIN, "middle"))
    p.append(f"<rect x='30' y='300' width='730' height='52' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 322, "Statique : on ramène G sur l'axe (une masse corrigée dans un plan).", 12, TRAIT, "start", True))
    p.append(_txt(46, 342, "Dynamique : on annule aussi le couple (G sur l'axe ET masses compensées plan par plan) — DEUX plans.", 12, TRAIT, "start", True))
    return _svg("".join(p), 790, 366)


# --- figure à curseurs : balourd d'un rotor (rotor d'énoncé : disque acier Ø300 × 40, paliers à 200 mm)
_CONFIGS = [("Une masse (balourd statique)", "statique"),
            ("Deux masses opposées, même plan (équilibré)", "equilibre"),
            ("Deux masses opposées, plans décalés de 40 mm (balourd dynamique)", "dynamique")]


def dyn_balourd(config="statique", N=3000.0, mb=10.0):
    """Masse de balourd mb (g) à r = 150 mm ; paliers A et B distants de 200 mm, rotor au milieu."""
    w = 2 * math.pi * N / 60
    F1 = mb / 1000 * 0.150 * w ** 2
    L, dz = 0.200, 0.040
    if config == "statique":
        R_, Cb = F1, 0.0
        RA = RB = F1 / 2
    elif config == "equilibre":
        R_, Cb, RA, RB = 0.0, 0.0, 0.0, 0.0
    else:
        R_, Cb = 0.0, F1 * dz
        RA = RB = Cb / L
    m_rotor = 7850 * math.pi * 0.15 ** 2 * 0.04
    poids = m_rotor * 9.81
    noms = {v: k for k, v in _CONFIGS}
    p = [_k_defs(), _txt(30, 24, noms.get(config, config).split(" (")[0] + f" : {_fr_court(mb, 0)} g à 150 mm, {_fr_court(N, 0)} tr/min", 13, TRAIT, "start", True)]
    ox, oy = 60, 170
    p.append(f"<line x1='{ox}' y1='{oy}' x2='{ox + 320}' y2='{oy}' stroke='{TRAIT}' stroke-width='3'/>")
    p.append(_txt(ox + 250, oy - 6, "arbre", 9, FIN, "middle"))
    for xp, nom, Rv in ((ox + 20, "A", RA), (ox + 300, "B", RB)):
        p.append(f"<rect x='{xp - 10}' y='{oy + 4}' width='20' height='16' fill='{FIN}'/>")
        p.append(_txt(xp, oy + 38, f"palier {nom}", 10, FIN, "middle"))
        if Rv > 0.5:
            hl = min(80, 12 + Rv / 2)
            vers_haut = nom == "A" or config == "statique"
            y1 = oy - 8 if vers_haut else oy + 24
            y2 = y1 - hl if vers_haut else y1 + hl
            p.append(_k_fl(xp, y1, xp, y2, ALERTE, "kr", 2.6))
            p.append(_txt(xp + 8 if nom == "A" else xp - 8, (y1 + y2) / 2, f"{_fr_court(Rv, 0)} N tournant", 10, ALERTE,
                          "start" if nom == "A" else "end", True))
    for xd in (ox + 140, ox + 180):
        p.append(f"<rect x='{xd - 8}' y='{oy - 70}' width='16' height='140' rx='3' fill='#e2e8f0' stroke='{TRAIT}'/>")
    p.append(_txt(ox + 160, oy + 92, "rotor Ø300 × 40 (deux faces)", 10, TRAIT, "middle"))
    if config == "statique":
        p.append(f"<circle cx='{ox + 160}' cy='{oy - 60}' r='7' fill='{ALERTE}'/>")
    elif config == "equilibre":
        p.append(f"<circle cx='{ox + 160}' cy='{oy - 60}' r='7' fill='{OK}'/>")
        p.append(f"<circle cx='{ox + 160}' cy='{oy + 60}' r='7' fill='{OK}'/>")
    else:
        p.append(f"<circle cx='{ox + 140}' cy='{oy - 60}' r='7' fill='{ARBRE}'/>")
        p.append(f"<circle cx='{ox + 180}' cy='{oy + 60}' r='7' fill='{ARBRE}'/>")
    p.append(_txt(ox + 160, oy - 82, "masse(s) de balourd", 10, FIN, "middle"))
    x0 = 430
    col = OK if config == "equilibre" else (ALERTE if config == "statique" else ARBRE)
    p.append(f"<rect x='{x0}' y='44' width='340' height='250' rx='6' fill='#ffffff' stroke='{col}' stroke-width='1.8'/>")
    lignes = ((f"ω = 2π × {_fr_court(N, 0)} / 60 ≈ {_fr_court(w, 1)} rad/s", TRAIT, False),
              (f"force d'une masse : mb × r × ω² ≈ {_fr_court(F1, 0)} N", TRAIT, False), ("", TRAIT, False),
              (f"force tournante résultante : {_fr_court(R_, 0)} N", col, True),
              (f"couple tournant : {_fr_court(Cb, 2)} N·m", col, True),
              (f"effort tournant sur chaque palier : {_fr_court(RA, 0)} N", col, True),
              (("sur couteaux : il roule" if config == "statique" else "sur couteaux : il ne roule pas"), FIN, False),
              (f"pour comparer, poids du rotor ≈ {_fr_court(poids, 0)} N", FIN, False),
              (("Rien ne tourne : rotor équilibré." if config == "equilibre" else
                ("G hors de l'axe : force tournante." if config == "statique" else
                 "G sur l'axe, mais un couple tournant :")), col, True),
              (("" if config != "dynamique" else "les paliers sont secoués en opposition."), col, True))
    for i, (t, c, g) in enumerate(lignes):
        if t:
            p.append(_txt(x0 + 12, 68 + 22 * i, t, 12, c, "start", g))
    p.append(_txt(30, 316, "Rotor (énoncé) : disque acier Ø300 × 40 (7 850 kg/m³, table des matériaux), paliers à 200 mm, rotor au milieu.", 10, FIN))
    return _svg("".join(p), 790, 330)


FIGURES_NOUVELLES = {
    "cdg_barycentre": ("Centre de gravité d'un arbre étagé par le barycentre", cdg_barycentre),
    "inertie_repartition": ("Inertie : même masse, matière répartie différemment", inertie_repartition),
    "huygens_axes": ("Théorème de Huygens", huygens_axes),
    "pfd_treuil": ("PFD sur un treuil : translation et rotation", pfd_treuil),
    "equilibrage": ("Équilibrage statique et dynamique d'un rotor", equilibrage),
}
DYN_NOUVELLE = {
    "balourd_curseurs": (
        "Choisis la répartition des balourds, la vitesse et la masse : forces et couple aux paliers",
        dyn_balourd,
        [{"nom": "config", "label": "Répartition", "choix": _CONFIGS, "defaut": _CONFIGS[0][0]},
         {"nom": "N", "label": "Vitesse N (tr/min)", "min": 500.0, "max": 3000.0, "defaut": 3000.0, "pas": 250.0},
         {"nom": "mb", "label": "Masse de chaque balourd (g)", "min": 2.0, "max": 20.0, "defaut": 10.0, "pas": 2.0}]),
}

# ===========================================================================
# 2. FICHE 6.21 — en FIN de bloc 6 (après la 6.20)
# ===========================================================================

FICHE_6_21 = {
    "id": "6.21",
    "titre": "Masse, centre de gravité, inertie, PFD et équilibrage d'une pièce tournante",
    "duree": "6 h",
    "cours": """### 1. Pourquoi cette fiche

La fiche 8.1 a posé F = m × a et son équivalent en rotation, Mt = I × α, avec le moment d'inertie d'un
disque plein. La fiche 6.20 a donné le théorème de l'énergie cinétique (TEC). Cette fiche va plus loin
sur trois questions de bureau d'études :

- **où est le centre de gravité** d'une pièce composée, et **quelle est son inertie** autour de l'axe où
  elle tourne vraiment ;
- comment écrire le **principe fondamental de la dynamique (PFD)** quand plusieurs efforts agissent, et
  comment il se relie au TEC ;
- pourquoi une pièce tournante **vibre** si elle est mal **équilibrée**, et comment on la corrige.

### 2. Masse et centre de gravité

**Masse** : m = ρ × V (ρ : masse volumique ; acier : 7 850 kg/m³, table des matériaux de l'appli).

**Centre de gravité G** : le point où l'on peut considérer que tout le poids s'applique — le point où il
faut accrocher l'élingue pour que la pièce levée reste horizontale. Pour une pièce composée de volumes
simples, G est le **barycentre** des centres de gravité des morceaux, pondérés par leurs masses (la notion
de barycentre est celle de la fiche 7.5) :

> **xG = Σ (mi × xi) / Σ mi** (de même pour yG et zG)

[[FIG:cdg_barycentre]]

*Exemple (données d'énoncé) : arbre étagé en acier, tronçon 1 Ø40 × 100 mm (G1 à x = 50 mm), tronçon 2
Ø20 × 60 mm (G2 à x = 130 mm). Le volume d'un cylindre vaut π/4 × d² × L et ρ est le même partout : π/4
et ρ apparaissent en haut et en bas de la fraction et se simplifient, il reste d² × L. xG = (40² × 100 × 50 + 20² × 60 × 130) / (40² × 100 + 20² × 60)
≈ **60,4 mm**. Masses : m1 = 7 850 × π × 0,02² × 0,1 ≈ 0,986 kg, m2 ≈ 0,148 kg.*

**Une pièce percée** = la pièce pleine **moins** le cylindre de matière enlevé (le « bouchon ») : dans la
somme, la masse du bouchon entre avec un signe moins, à la position de son centre.

*Exemple (données d'énoncé) : le tronçon Ø40 × 100 seul, percé depuis la face gauche d'un trou borgne
Ø20 × 50 (centre du bouchon à x = 25 mm). xG = (40² × 100 × 50 − 20² × 50 × 25) / (40² × 100 − 20² × 50) ≈
**53,6 mm** : G s'éloigne du côté percé.*

*Pourquoi G compte : le poids s'applique en G (statique, fiches 12.1 et 6.16) ; une pièce tournante dont G n'est pas
sur l'axe tourne « en fronde » (§6) ; et le PFD en translation s'écrit pour le mouvement de G.*

### 3. Le moment d'inertie : la « masse » de la rotation

En translation, la masse mesure la résistance à l'accélération. En rotation, c'est le **moment
d'inertie J** autour de l'axe (noté I en fiche 8.1). Il dépend de la masse **et de sa répartition** :
chaque petite masse compte avec le **carré** de sa distance à l'axe.

> **J = Σ mi × ri²** (kg·m²)

*Pourquoi le carré ? Une masse à la distance r de l'axe se déplace à la vitesse v = r × ω : deux fois plus
loin, elle va deux fois plus vite. Son énergie cinétique vaut ½ m v² = ½ m (r ω)² = ½ (m r²) ω² : une
rotation se paie en m r², et J est simplement ce qui remplace m dans ½ m v² (fiche 6.20). C'est pour la même
raison qu'on ferme une porte sans effort en poussant près de la poignée, difficilement près des gonds.*

[[FIG:inertie_repartition]]

**Formules classiques des solides homogènes** (autour de l'axe indiqué) :

| Solide | Moment d'inertie |
|---|---|
| cylindre plein, disque (rayon R), autour de son axe de révolution | J = ½ m R² |
| tube, couronne (rayons R et r), autour de son axe de révolution | J = ½ m (R² + r²) |
| anneau mince (rayon R), autour de son axe | J ≈ m R² |
| barre mince de longueur L, autour d'un axe perpendiculaire passant par son milieu | J = m L² / 12 |
| petite masse à la distance d de l'axe | J = m d² |

**Ordre de grandeur** (données d'énoncé) : un disque acier Ø300 × 40 mm pèse m = 7 850 × π × 0,15² × 0,04 ≈
**22,2 kg** ; J = ½ × 22,2 × 0,15² ≈ **0,25 kg·m²**. La même masse placée en jante (anneau de rayon
150 mm) donnerait environ deux fois plus : 22,2 × 0,15² ≈ 0,50 kg·m². *Ce que veut dire 0,25 kg·m² : avec
un couple de 10 N·m, ce disque prend α = 10 / 0,25 = 40 rad/s², soit environ 8 s pour atteindre 3 000 tr/min
(314 rad/s) ; matière en jante, il lui en faudrait environ 16.*

**Le théorème de Huygens.** Quand une pièce tourne autour d'un axe Δ qui ne passe pas par G, elle fait deux
choses à la fois : son centre G décrit un cercle de rayon d autour de Δ, comme si toute la masse était en G
(cela coûte m d²), et la pièce pivote sur elle-même d'un tour à chaque tour (cela coûte J_G). C'est le cas
d'une pièce bridée de façon décentrée sur le plateau d'un tour. Les deux coûts s'ajoutent : pour un axe Δ
parallèle à l'axe passant par G, à la distance d,

> **J_Δ = J_G + m × d²**

[[FIG:huygens_axes]]

*Exemple (données d'énoncé) : on allège le disque précédent par 4 trous Ø60 traversants, dont les axes sont
à d = 100 mm de l'axe. Chaque trou retire m_t = 7 850 × π × 0,03² × 0,04 ≈ 0,888 kg. Inertie d'un trou
autour de l'axe du disque : ½ × 0,888 × 0,03² + 0,888 × 0,1² ≈ 0,0093 kg·m². Comme pour G, un trou se compte
en négatif : J(disque percé) = J(disque plein) − 4 × J(un bouchon) ≈ 0,2497 − 4 × 0,0093 ≈ **0,213 kg·m²**
(−15 %), pour une masse de 22,2 − 4 × 0,888 ≈ 18,6 kg (−16 %). L'inertie baisse à peu près autant que la
masse parce que les trous sont à mi-rayon ; percés plus près de la jante, ils feraient gagner nettement plus
d'inertie pour la même masse retirée.*

**La matrice d'inertie.** Une pièce n'a pas une seule inertie : elle en a une par axe — une bielle tourne
facilement autour de sa longueur, beaucoup moins « en hélice ». Le logiciel de CAO range ces valeurs dans un
tableau 3 × 3 (menu « propriétés de masse ») :

- **sur la diagonale**, Jx, Jy, Jz : les moments d'inertie autour des trois axes — les J de cette section ;
- **hors diagonale**, les **produits d'inertie** (Jxy, Jyz, Jxz) : ils mesurent si la matière est « penchée »
  par rapport aux axes (plus de matière en haut à droite et en bas à gauche que l'inverse, par exemple).

**Le rôle des symétries.** Si la pièce a un plan de symétrie, chaque morceau de matière d'un côté a son
jumeau de l'autre : un plan de symétrie annule les deux produits d'inertie qui font intervenir l'axe
perpendiculaire à ce plan. Avec deux plans de symétrie perpendiculaires, la matrice calculée en G est
**diagonale** dans les axes formés par leur droite commune et leurs deux normales : ce sont les **axes
principaux d'inertie** (une pièce de révolution en a une infinité autour de son axe).

**Ce que vous en ferez.** Lire dans la CAO si les produits d'inertie sont nuls (ou négligeables) dans le
repère de l'axe de rotation, calculé en G. S'ils ne le sont pas, la pièce aura un balourd dynamique en
tournant (§6). On ne calcule jamais cette matrice à la main.

### 4. Le principe fondamental de la dynamique (PFD)

Pour un solide isolé, le PFD généralise l'équilibre de la statique (fiches 12.1 et 6.16) : la somme des
efforts extérieurs n'est plus nulle, elle produit l'accélération.

> **Translation rectiligne : Σ F ext = m × aG** (en projection sur la direction du mouvement), et
> Σ M_G(F ext) = 0, puisque le solide ne tourne pas. aG : accélération du centre de gravité (en
> translation, tous les points ont la même).

> **Rotation autour d'un axe fixe Δ : Σ M_Δ(F ext) = J_Δ × α**, avec α en rad/s² (on trouve aussi la
> notation θ̈ = d²θ/dt²).

**La méthode est celle de la statique** : isoler, faire le bilan de **tous** les efforts extérieurs (poids,
contacts, câbles, couple moteur, frottements), projeter. Seule la conclusion change : au lieu de « = 0 »,
on écrit « = m a » ou « = J α ».

[[FIG:pfd_treuil]]

*Exemple (données d'énoncé) : un treuil soulève une charge de m = 200 kg avec une accélération a = 0,5 m/s².
Le tambour a un rayon r = 0,1 m et une inertie J = 0,25 kg·m².*

- *Charge isolée (on compte positif vers le haut, dans le sens de a) : T − m g = m a → T = 200 × (9,81 +
  0,5) = **2 062 N**.*
- *Tambour isolé : T tire le bord du tambour vers le bas, à la distance r de l'axe ; son moment r × T
  s'oppose à Cm, d'où le signe moins : Cm − r × T = J × α, avec α = a / r = 5 rad/s² → Cm = 0,25 × 5 + 0,1 ×
  2 062 ≈ **207,5 N·m**.*

*Le terme d'accélération du tambour (1,25 N·m) est ici petit devant celui de la charge : c'est la charge
qui dimensionne. Ce n'est pas toujours vrai — pour un rotor lourd et rapide, c'est l'inverse (fiche 13.3).*

### 5. PFD et théorème de l'énergie cinétique : deux portes pour le même problème

Le TEC de la fiche 6.20 et le PFD décrivent le même mouvement :

- le **PFD** parle d'**efforts** et d'**accélération** : il donne les forces intérieures (la tension du
  câble T, l'effort dans un palier) et l'accélération à un instant ;
- le **TEC** parle d'**énergie** et de **puissance** : il donne directement une vitesse atteinte ou une
  puissance, sans passer par les efforts intérieurs, dont la puissance totale est nulle tant que les
  liaisons sont sans frottement.

*Le PFD, c'est le détail des virements (qui pousse, avec quelle force) ; le TEC, c'est le relevé de compte
(combien d'énergie entre, où elle va). Au bureau d'études, le PFD donne le **couple** et la **tension**, qui
servent à choisir le réducteur et à dimensionner le câble et l'arbre ; le TEC donne la **puissance**, qui
sert à choisir le moteur sur sa plaque.*

**Le lien.** Une puissance est une force × une vitesse (fiche 6.20). Multiplions le PFD de la charge par sa
vitesse v : (T − m g) × v = m a × v. Le membre de droite, m a v, est l'énergie cinétique gagnée par seconde :
pendant un petit instant Δt, la vitesse passe de v à v + a Δt, et ½ m v² augmente d'environ m v a Δt. Donc
T v = m v a + m g v : la puissance fournie par le câble remplit l'énergie cinétique (m v a) **et** l'énergie
de position (la charge monte de v mètres par seconde et gagne m g v joules chaque seconde). Même chose en
rotation : C × ω = J α ω, l'énergie cinétique du tambour gagnée par seconde.

*Vérification sur le treuil, à l'instant où la charge monte à v = 0,8 m/s (ω = v / r = 8 rad/s) : le moteur
fournit Cm × ω = 207,45 × 8 ≈ 1 660 W. Où va cette puissance ? J ω α = 0,25 × 8 × 5 = 10 W pour faire tourner
le tambour plus vite ; m v a = 200 × 0,8 × 0,5 = 80 W pour faire aller la charge plus vite ; m g v = 200 × 9,81
× 0,8 ≈ 1 570 W pour la monter. Total ≈ **1 660 W** : les deux portes mènent au même endroit.*

*Pourquoi le TEC « saute » la tension du câble : si l'on regarde tout le treuil d'un coup (tambour + câble +
charge), T devient un effort intérieur. Il donne T × v à la charge et en reprend exactement autant au tambour
(r × T × ω = T × v) : dans le bilan global, il s'annule. Le PFD oblige à couper le système en morceaux, et
c'est pour ça qu'il donne T.*

**Quand choisir laquelle ?** PFD quand on cherche un effort ou une accélération ; TEC quand on cherche une
vitesse finale ou une puissance, surtout s'il y a plusieurs solides liés.

### 6. Équilibrage d'une pièce tournante

Une pièce qui tourne n'est jamais parfaitement répartie autour de son axe. Le défaut se modélise par une
petite masse en trop mb à la distance r de l'axe : c'est le **balourd**, chiffré par U = mb × r (en g·mm), qui
ne dépend pas de la vitesse. *Faites tourner un seau d'eau à bout de bras : votre main doit tirer en
permanence vers le centre, de plus en plus fort quand vous accélérez.* En rotation, la masse en trop décrit
un cercle : elle a une accélération centripète r × ω², donc l'arbre doit la retenir par une force

> **F = mb × r × ω²** — la **force de balourd** : elle **tourne avec la pièce** (en haut, sur le côté, en
> bas, à chaque tour) et croît comme le carré de la vitesse.

*Exemple (données d'énoncé) : le rotor acier Ø300 × 40 (≈ 22,2 kg) porte un balourd de 10 g à 150 mm. À
3 000 tr/min (ω ≈ 314 rad/s) : F = 0,010 × 0,15 × 314² ≈ **148 N**, qui tourne 50 fois par seconde — à
comparer au poids du rotor, ≈ 218 N. Dix grammes suffisent à secouer les paliers d'une force comparable au
poids de la pièce.*

[[FIG:equilibrage]]

**Équilibrage statique : ramener G sur l'axe.** Si G n'est pas sur l'axe, la pièce posée sur deux
**couteaux** (deux règles d'acier horizontales à arête fine, sur lesquelles on pose les tourillons de
l'arbre : il y roule presque sans frottement) roule jusqu'à ce que son point lourd soit en bas : c'est le test du balourd
statique. On le corrige par une seule masse (ou un perçage) dans un plan, du côté opposé. Suffisant pour une
pièce mince (disque, meule, poulie étroite).

**Équilibrage dynamique : l'axe de rotation confondu avec un axe principal central d'inertie** (un axe
principal qui passe par G). Deux balourds égaux, opposés, mais situés dans des plans différents : G reste sur
l'axe, mais en rotation les deux forces forment un **couple qui tourne** et secoue les deux paliers en
opposition.

**Pourquoi les couteaux ne voient rien.** Sur couteaux, la pièce est presque immobile : la seule force qui
agit est son poids, et le poids ne « voit » que la position de G. Or deux masses égales et opposées laissent G
sur l'axe : rien ne fait rouler la pièce. Les forces mb r ω², elles, n'existent qu'en rotation. Une fois la
pièce lancée, chaque masse tire vers l'extérieur dans son propre plan ; comme les deux plans sont décalés le
long de l'axe, les deux tractions ne s'annulent pas : elles forment un couple qui cherche à faire **basculer**
l'arbre. *Prenez un manche à balai par les deux bouts, poussez un bout vers le haut et l'autre vers le bas :
le balai ne monte pas, il pivote.* Les paliers doivent empêcher ce basculement, et comme le couple tourne avec
la pièce, ils sont secoués à chaque tour.

**Ce que veut dire « axe principal central ».** L'axe est principal et passe par G quand la matière est
« rangée en paires » autour de lui : à chaque petite masse correspond une masse jumelle diamétralement
opposée, **dans le même plan**. En rotation, les tractions des jumelles s'annulent plan par plan : ni force ni
couple. Le balourd statique, c'est une masse sans jumelle (une force) ; le balourd dynamique, ce sont des
jumelles **décalées de plan** (un couple). Le produit d'inertie mesure ce décalage : pour les deux balourds de
l'exemple ci-dessous, à y = +150 mm, z = +20 mm et y = −150 mm, z = −20 mm, Σ m y z = 2 × 0,010 × 0,15 × 0,02 ≠
0 ; ramenés dans le même plan (z = 0), ce produit est nul et le couple disparaît.

*L'image du garagiste : pour équilibrer une roue de voiture, on pose des masses de plomb sur le bord
intérieur et sur le bord extérieur de la jante : ce sont les deux plans de correction.*

**Pourquoi deux plans.** Une seule masse corrective peut annuler la force ou le couple, pas les deux. On
corrige donc dans **deux plans** : c'est le travail d'une **équilibreuse**, qui mesure les efforts aux paliers
en rotation. Obligatoire pour une pièce longue (rotor de moteur, arbre de transmission, cylindre) : le couple
vaut F × z, et plus la pièce est longue, plus deux défauts peuvent être éloignés. Sur un disque mince, z ≈ 0 :
le couple reste négligeable et un équilibrage statique suffit.

*Exemple (données d'énoncé ; calcul d'ordre de grandeur pour comprendre — en BTS, l'équilibrage se traite à
l'équilibreuse ou au logiciel) : deux balourds de 10 g à 150 mm, opposés, sur les deux faces du rotor (40 mm
d'écart). Résultante nulle ; couple tournant 148 × 0,04 ≈ **5,9 N·m**. Les paliers doivent opposer un couple
égal et contraire : deux forces R opposées, distantes de L = 0,2 m, donnent R × L = C, donc R = C / L ≈ 5,9 /
0,2 ≈ **30 N** par palier, en sens opposés, qui tournent.*

[[DYN:balourd_curseurs]]

**La tolérance d'équilibrage** se choisit avec la norme ISO 21940-11 (rotors à comportement rigide) : le
balourd résiduel admissible, en g·mm, dépend du type de machine (classe de qualité G), de sa vitesse maximale
de service et de la masse du rotor. On ne vise jamais un balourd nul : il est inaccessible et coûterait de
plus en plus cher à approcher ; on vise ce que la machine supporte à sa vitesse.

**Le lien avec les vibrations.** Le balourd est une excitation périodique à la fréquence de rotation. Si
cette fréquence approche une fréquence propre de la machine, l'amplitude s'emballe : c'est la résonance
(fiche 13.5).

### 7. Les erreurs classiques

1. **Pondérer par les volumes quand les matériaux sont différents** : il faut les masses (ρ × V).
2. **Oublier le carré** dans J = m r² ou dans F = mb r ω² : doubler la vitesse multiplie la force de balourd
   par 4.
3. **Appliquer Huygens entre deux axes dont aucun ne passe par G** : la formule part toujours de J_G. Pour
   aller d'un axe A à un axe B, passer par G : on retire m d_A², puis on ajoute m d_B².
4. **Oublier un effort dans le bilan du PFD** (le poids, un frottement) : la méthode est celle de la
   statique, bilan complet d'abord.
5. **Croire qu'une pièce équilibrée statiquement est équilibrée** : le balourd dynamique ne se voit qu'en
   rotation.
6. **Utiliser N en tr/min dans r ω²** : ω en rad/s.

### 8. À retenir

- m = ρ V ; **xG = Σ mi xi / Σ mi** (trou : masse négative).
- **J = Σ m r²** ; disque ½ m R², tube ½ m (R² + r²), anneau m R², barre m L²/12 ; **Huygens : J_Δ = J_G +
  m d²**.
- Matrice d'inertie : symétries → produits d'inertie nuls → axes principaux ; la CAO la fournit.
- **PFD** : Σ F = m aG (translation), Σ M_Δ = J α (rotation) ; méthode de la statique, « = m a » au lieu de
  « = 0 ».
- **PFD × vitesse = TEC** : efforts et accélération d'un côté, énergie et puissance de l'autre.
- **Balourd U = mb r** ; **force de balourd F = mb r ω²**, tournante. Statique : G sur l'axe (un plan) ;
  dynamique : G sur l'axe **et** produits d'inertie nuls — l'axe de rotation est un axe principal central
  (deux plans).
""",
    "formules": """
**Masse** — m = ρ V (acier : 7 850 kg/m³)

**Centre de gravité** — xG = Σ mi xi / Σ mi (idem y, z) ; un trou compte en masse négative

**Moment d'inertie** — J = Σ mi ri² · disque ½ m R² · tube ½ m (R² + r²) · anneau m R² · barre m L²/12 ·
petite masse m d²

**Huygens** — J_Δ = J_G + m d²

**PFD** — translation : Σ F ext = m aG (et Σ M_G = 0) · rotation autour d'un axe fixe : Σ M_Δ = J_Δ α (rad/s²)

**Lien avec le TEC** — F v = d(½ m v²)/dt · C ω = d(½ J ω²)/dt

**Balourd** — U = mb r (g·mm) · force F = mb r ω² (ω = 2πN/60) · deux balourds opposés distants de z :
couple C = F z, repris par deux paliers distants de L : R = C / L
""",
    "exemple": """
### Cas industriel — Le ventilateur qui faisait vibrer tout l'atelier

**Le symptôme.** Après le remplacement de sa roue, un ventilateur d'extraction fait vibrer son support et
ses roulements chauffent. La roue neuve a pourtant été « équilibrée » chez le fournisseur : posée sur des
couteaux, elle ne roule pas.

**L'analyse.** Ne pas rouler sur couteaux prouve seulement l'**équilibrage statique** : G est sur l'axe.
Mais la roue est large (deux flasques — les deux disques latéraux entre lesquels sont fixées les aubes —
espacées) ; un balourd sur une flasque compensé par un balourd
opposé sur l'autre laisse G sur l'axe et crée un **couple tournant**. C'est un balourd **dynamique** : il ne
se voit qu'en rotation, et il secoue les deux paliers en opposition.

**L'ordre de grandeur** (données d'énoncé) : deux balourds de 15 g à 200 mm, sur deux flasques espacées de
120 mm, à 1 500 tr/min (ω ≈ 157 rad/s) : chaque force vaut 0,015 × 0,2 × 157² ≈ 74 N ; le couple tournant,
74 × 0,12 ≈ 8,9 N·m ; avec des paliers à 300 mm, chacun encaisse ≈ 30 N tournant, 25 fois par seconde.

**La correction.** Équilibrage dynamique sur équilibreuse, avec correction dans **deux plans** (les deux
flasques), jusqu'au balourd résiduel fixé selon ISO 21940-11. Et vérifier que la vitesse de rotation reste
loin des fréquences propres du support (fiche 13.5).

**Ce que le cas apprend.** « Équilibré » ne veut rien dire tant qu'on ne précise pas **statique ou
dynamique**. Pour une pièce large ou longue, seul l'équilibrage dynamique garantit l'absence de vibration.
""",
    "exercice": """
### Exercice — Le rotor d'un banc d'essai

Un rotor de banc d'essai est un disque en acier (7 850 kg/m³) de **Ø300 mm** et **40 mm** d'épaisseur,
monté au milieu d'un arbre porté par deux paliers distants de **200 mm** (données d'énoncé).

**1.** Calculer sa masse et son moment d'inertie autour de son axe.

**2.** Le moteur doit l'amener de 0 à 3 000 tr/min en **2 s**, à accélération constante. Calculer
l'accélération angulaire et le couple nécessaire (frottements négligés). Vérifier avec le TEC : énergie
cinétique finale et puissance moyenne.

**3.** Un défaut de fabrication équivaut à un balourd de **10 g à 150 mm** de l'axe. Calculer la force
tournante à 3 000 tr/min et la comparer au poids du rotor.

**4.** Le défaut est en réalité deux balourds de 10 g, opposés, sur les deux faces du disque. Le rotor
roule-t-il sur couteaux ? Que reçoivent les paliers en rotation ?

**5.** Pour l'alléger, on perce le disque de 4 trous Ø60 traversants, dont les axes sont à 100 mm de son axe.
Calculer sa nouvelle masse et son nouveau moment d'inertie (théorème de Huygens).
""",
    "corrige": """
### Corrigé, en six temps

#### 1. Ce que dit l'énoncé

Un disque homogène connu par ses dimensions, une montée en vitesse imposée, puis deux défauts de répartition
de masse.

#### 2. Quelle règle, et pourquoi

> m = ρ V ; **J = ½ m R²** ; **PFD en rotation : C = J α** ; **TEC : Ec = ½ J ω²** ; **force de balourd :
> F = mb r ω²** ; deux balourds opposés décalés de z : **couple F × z**, repris par les paliers : **R = F z / L** ;
> **Huygens : J_Δ = J_G + m d²** (un trou se compte en négatif).

#### 3. Les conversions

R = 0,15 m, épaisseur 0,04 m ; ω = 2π × 3 000 / 60 ≈ 314,2 rad/s ; mb = 0,010 kg ; r = 0,15 m.

#### 4. Le remplacement

m = 7 850 × π × 0,15² × 0,04 ; J = ½ m × 0,15² ; α = 314,2 / 2 ; C = J α ; F = 0,010 × 0,15 × 314,2².

#### 5. Le calcul

**1.** m ≈ **22,2 kg** ; J ≈ ½ × 22,2 × 0,0225 ≈ **0,2497 kg·m²** (≈ 0,25).

**2.** α = 314,2 / 2 ≈ **157,1 rad/s²** ; C = 0,2497 × 157,1 ≈ **39,2 N·m**. TEC : Ec = ½ × 0,2497 × 314,2² ≈
12 330 J ; puissance moyenne ≈ 12 330 / 2 ≈ **6 160 W**. Par le PFD : l'accélération étant constante, ω croît
régulièrement de 0 à 314,2 rad/s, sa valeur moyenne est la moitié, 157,1 rad/s ; C × ω moyen = 39,2 × 157,1 ≈
6 160 W : même résultat.

**3.** F = 0,010 × 0,15 × 314,2² ≈ **148 N**, tournant ; poids ≈ 22,2 × 9,81 ≈ 218 N. La force de balourd
vaut les deux tiers du poids.

**4.** Résultante nulle : G reste sur l'axe, le rotor **ne roule pas** sur couteaux (équilibré
statiquement). En rotation : couple 148 × 0,04 ≈ **5,9 N·m** ; chaque palier reçoit ≈ 5,9 / 0,2 ≈ **30 N**,
en sens opposés, tournant à 50 Hz : balourd **dynamique**, à corriger dans deux plans.

**5.** Un bouchon : m_t = 7 850 × π × 0,03² × 0,04 ≈ 0,888 kg ; J d'un bouchon autour de l'axe du disque :
½ × 0,888 × 0,03² + 0,888 × 0,1² ≈ 0,0093 kg·m². Disque allégé : m ≈ 22,2 − 4 × 0,888 ≈ **18,6 kg** ;
J ≈ 0,2497 − 4 × 0,0093 ≈ **0,213 kg·m²**.

#### 6. La vérification

**Deux portes, un résultat** : PFD (C × ω moyen) et TEC (Ec / t) donnent la même puissance moyenne.
**Unités** : kg × m × (rad/s)² = N. **Bon sens** : la force de balourd croît comme ω² — à 1 500 tr/min, elle
serait quatre fois plus faible (≈ 37 N).
""",
}

# ===========================================================================
# 3. MÉTHODE
# ===========================================================================
MTH_6_21 = ("6.21", "Écrire le PFD d'un système qui accélère", [
    "**Isoler chaque solide** (comme en statique) et faire le bilan complet des efforts extérieurs : poids, "
    "contacts, câbles, couple moteur, frottements.",
    "**Choisir l'équation** : translation → Σ F = m a (projetée sur le mouvement) ; rotation autour d'un axe "
    "fixe → Σ M = J α.",
    "**Relier les solides** par la cinématique (a = r α pour un câble enroulé sans glisser) et par les "
    "efforts qu'ils échangent (le câble tire la charge et freine le tambour).",
    "**Résoudre**, puis **vérifier par le TEC** : la puissance motrice doit égaler la variation d'énergie "
    "par seconde (cinétique + potentielle) plus les pertes.",
], "Treuil : charge 200 kg, a = 0,5 m/s², tambour r = 0,1 m, J = 0,25 kg·m². Charge : T = 200 × (9,81 + 0,5) "
   "= 2 062 N. Tambour : Cm = J a / r + r T ≈ 1,25 + 206,2 ≈ 207,5 N·m. À v = 0,8 m/s : ≈ 1 660 W des deux côtés.")

# ===========================================================================
# 4. ATELIERS (fin de liste ATELIERS, après at169)
# ===========================================================================
ATELIERS_NOUVEAUX = [
    {
        "id": "at170",
        "chapitre": "Bloc 6",
        "titre": "Treuil de levage : le couple pour accélérer la charge",
        "theme": "Dynamique",
        "fiche": "6.21",
        "figure": "pfd_treuil",
        "vocabulaire": [
            ("PFD (translation)",
             "Σ F ext = m a : la somme des efforts extérieurs produit l'accélération du centre de gravité."),
            ("PFD (rotation)",
             "Σ M = J α : la somme des moments autour de l'axe produit l'accélération angulaire."),
            ("Moment d'inertie J",
             "la « masse » de la rotation : J = Σ m r², en kg·m²."),
        ],
        "enonce": "Un treuil soulève une charge de 200 kg avec une accélération de 0,5 m/s². Le tambour a un rayon "
                  "de 0,1 m et un moment d'inertie de 0,25 kg·m² (données d'énoncé ; g = 9,81 m/s² ; "
                  "frottements négligés).",
        "etapes": [
            {"type": "numerique", "label": "Tension du câble",
             "unite": "N", "attendu": 2062, "tol": 3,
             "consigne": "Isole la charge et écris le PFD : T − m g = m a. Calcule T.",
             "indice": "T = m (g + a).",
             "pieges": [(1962, "1 962 N, c'est le poids seul : la charge à l'équilibre. Pour l'accélérer vers le "
                               "haut, le câble doit tirer plus fort : T = m (g + a)."),
                        (100, "100 N, c'est seulement m a. Le câble doit aussi porter le poids.")],
             "aide": "T = 200 × (9,81 + 0,5) = 2 062 N."},
            {"type": "numerique", "label": "Accélération angulaire du tambour",
             "unite": "rad/s²", "attendu": 5, "tol": 0.05,
             "consigne": "Le câble s'enroule sans glisser : α = a / r.",
             "indice": "a = 0,5 m/s², r = 0,1 m.",
             "pieges": [(0.05, "0,05 : tu as multiplié a par r. Pour un câble enroulé, a = r α, donc α = a / r.")],
             "aide": "α = 0,5 / 0,1 = 5 rad/s²."},
            {"type": "numerique", "label": "Couple moteur sur le tambour",
             "unite": "N·m", "attendu": 207.45, "tol": 0.5,
             "consigne": "Isole le tambour : Cm − r × T = J × α. Calcule Cm.",
             "indice": "Cm = J α + r T.",
             "pieges": [(206.2, "206,2 N·m, c'est r × T seul : tu as oublié le couple qui accélère le tambour lui-même "
                                "(J α)."),
                        (1.25, "1,25 N·m, c'est J α seul : le tambour doit aussi tirer le câble (r × T).")],
             "aide": "Cm = 0,25 × 5 + 0,1 × 2 062 ≈ 207,5 N·m."},
            {"type": "numerique", "label": "Puissance motrice à v = 0,8 m/s",
             "unite": "W", "attendu": 1659.6, "tol": 5,
             "consigne": "À l'instant où la charge monte à 0,8 m/s, calcule la puissance du moteur Cm × ω.",
             "indice": "ω = v / r.",
             "pieges": [(165.96, "166 : tu as gardé ω = 0,8. ω = v / r = 0,8 / 0,1 = 8 rad/s.")],
             "aide": "ω = 8 rad/s ; P = 207,45 × 8 ≈ 1 660 W."},
            {"type": "qcm", "label": "Le lien avec le TEC",
             "question": "Cette puissance vaut 10 + 80 + 1 570 W. Que représentent ces trois termes ?",
             "options": ["Les pertes du moteur, du réducteur et du câble",
                         "Les puissances de trois moteurs différents",
                         "Variation par seconde de l'Ec du tambour (J ω α), de l'Ec de la charge (m v a), et "
                         "énergie potentielle gagnée par seconde (m g v)"],
             "bonne": 2,
             "indice": "TEC en puissance : la puissance motrice remplit l'énergie cinétique et potentielle.",
             "diagnostics": {0: "Les frottements sont négligés ici : aucune perte. Toute la puissance va dans "
                                 "l'énergie du système.",
                             1: "Un seul moteur : ce sont trois destinations de la même puissance (J ω α, m v a, "
                                "m g v)."}},
        ],
        "corrige": {
            "enonce": "Charge 200 kg, a = 0,5 m/s² ; tambour r = 0,1 m, J = 0,25 kg·m² ; g = 9,81 m/s².",
            "regle": "**PFD charge : T − m g = m a** ; **cinématique : α = a / r** ; **PFD tambour : Cm − r T = J α** ; "
                    "vérification **TEC : Cm ω = J ω α + m v a + m g v**.",
            "conversions": "Unités SI ; ω = v / r.",
            "remplacement": "T = 200 × 10,31 ; α = 0,5 / 0,1 ; Cm = 0,25 × 5 + 0,1 × 2 062 ; P = Cm × 8.",
            "calcul": "**T = 2 062 N** ; **α = 5 rad/s²** ; **Cm ≈ 207,5 N·m** ; **P ≈ 1 660 W**.",
            "verification": "TEC : 0,25 × 8 × 5 + 200 × 0,8 × 0,5 + 200 × 9,81 × 0,8 = 10 + 80 + 1 569,6 ≈ 1 660 W : "
                            "les deux portes donnent la même puissance.",
        },
        "a_retenir": "À retenir : on isole chaque solide, on écrit « = m a » ou « = J α » au lieu de « = 0 », et "
                     "on relie les isolements par la cinématique ; le TEC vérifie le résultat.",
    },
    {
        "id": "at171",
        "chapitre": "Bloc 6",
        "titre": "Rotor de banc d'essai : balourd statique ou dynamique ?",
        "theme": "Dynamique",
        "fiche": "6.21",
        "figure": "equilibrage",
        "vocabulaire": [
            ("Balourd",
             "une masse en trop mb à la distance r de l'axe : en rotation, elle exige une force tournante mb r ω²."),
            ("Équilibrage statique",
             "ramener le centre de gravité sur l'axe : une correction dans un plan suffit."),
            ("Équilibrage dynamique",
             "faire en sorte que les masses se compensent plan par plan (axe de rotation = axe principal d'inertie "
             "passant par G) : ni force ni couple tournants ; correction dans deux plans."),
        ],
        "enonce": "Rotor : disque en acier (7 850 kg/m³) de Ø300 mm et 40 mm d'épaisseur, au milieu de deux paliers "
                  "distants de 200 mm. Il tourne à 3 000 tr/min. Balourd : 10 g à 150 mm de l'axe (données d'énoncé).",
        "etapes": [
            {"type": "numerique", "label": "Masse du rotor",
             "unite": "kg", "attendu": 22.195, "tol": 0.05,
             "consigne": "Calcule m = ρ × π × R² × e.",
             "indice": "R = 0,15 m, e = 0,04 m.",
             "pieges": [(88.78, "88,8 kg : tu as pris le diamètre (0,3 m) au lieu du rayon.")],
             "aide": "7 850 × π × 0,15² × 0,04 ≈ 22,2 kg."},
            {"type": "numerique", "label": "Vitesse angulaire",
             "unite": "rad/s", "attendu": 314.16, "tol": 0.3,
             "consigne": "Calcule ω = 2πN/60.",
             "indice": "N = 3 000 tr/min.",
             "pieges": [(3000, "3 000, c'est N en tr/min : il faut ω en rad/s.")],
             "aide": "ω = 2π × 3 000 / 60 ≈ 314,2 rad/s."},
            {"type": "numerique", "label": "Force de balourd",
             "unite": "N", "attendu": 148.04, "tol": 0.5,
             "consigne": "Calcule F = mb × r × ω².",
             "indice": "mb = 0,010 kg, r = 0,15 m.",
             "pieges": [(0.471, "0,47 : tu as oublié le carré de ω. F = mb r ω²."),
                        (148044, "148 044 : tu as gardé mb en grammes. 10 g = 0,010 kg.")],
             "aide": "0,010 × 0,15 × 314,2² ≈ 148 N."},
            {"type": "numerique", "label": "Réaction tournante par palier (balourd dynamique)",
             "unite": "N", "attendu": 29.61, "tol": 0.3,
             "consigne": "Le défaut est en fait deux balourds de 10 g, opposés, sur les deux faces du disque (40 mm "
                         "d'écart). Calcule le couple tournant F × 0,04, puis la réaction de chaque palier (couple / 0,2).",
             "indice": "Les deux forces forment un couple ; les paliers le reprennent avec un bras de levier de 0,2 m.",
             "pieges": [(74.02, "74 N, c'est la moitié de F : ce serait le cas d'un balourd STATIQUE (une seule masse, "
                                "partagée entre les deux paliers). Ici, les deux forces forment un couple."),
                        (5.92, "5,92, c'est le couple tournant, en N·m. Chaque palier le reprend avec un bras de levier "
                               "de 0,2 m : R = C / 0,2."),
                        (14.8, "14,8 N : tu as encore partagé en deux. Le couple est repris en entier par le couple des "
                               "deux réactions, R × 0,2 = C.")],
             "aide": "C = 148 × 0,04 ≈ 5,92 N·m ; R = 5,92 / 0,2 ≈ 29,6 N."},
            {"type": "qcm", "label": "Le test des couteaux",
             "question": "Avec les deux balourds opposés, que montre le rotor posé sur deux couteaux horizontaux ?",
             "options": ["Il ne roule pas : il est équilibré statiquement, le défaut ne se voit qu'en rotation",
                         "Il roule jusqu'à ce que le point lourd soit en bas",
                         "Il roule dans les deux sens alternativement"], "bonne": 0,
             "indice": "Où est le centre de gravité quand les deux masses sont opposées ?",
             "diagnostics": {1: "Ce serait vrai pour un balourd statique (une seule masse). Deux masses opposées "
                                 "laissent G sur l'axe : rien ne fait rouler la pièce.",
                             2: "Sur couteaux, seul le poids agit : avec G sur l'axe, la pièce reste où on la pose."}},
        ],
        "corrige": {
            "enonce": "Disque acier Ø300 × 40, paliers à 200 mm, 3 000 tr/min ; balourd 10 g à 150 mm, puis deux "
                      "balourds opposés sur les deux faces.",
            "regle": "**m = ρ V** ; **ω = 2πN/60** ; **F = mb r ω²** ; deux balourds opposés décalés de z : "
                    "**couple F z**, repris par les paliers : **R = F z / L**.",
            "conversions": "mm → m ; g → kg ; tr/min → rad/s.",
            "remplacement": "m = 7 850 × π × 0,15² × 0,04 ; ω = 2π × 3 000 / 60 ; F = 0,010 × 0,15 × ω² ; "
                            "R = F × 0,04 / 0,2.",
            "calcul": "**m ≈ 22,2 kg** ; **ω ≈ 314,2 rad/s** ; **F ≈ 148 N** ; **R ≈ 29,6 N** par palier, en "
                     "opposition.",
            "verification": "F ≈ 148 N pour un poids de 218 N : dix grammes secouent la machine presque autant que "
                            "son propre poids, et ce défaut-là ne se voit pas sur couteaux.",
        },
        "a_retenir": "À retenir : un balourd crée une force tournante mb r ω² ; deux balourds opposés dans des plans "
                     "différents laissent G sur l'axe mais créent un couple : seul l'équilibrage dynamique (deux "
                     "plans) le corrige.",
    },
]

# ===========================================================================
# 5. GÉNÉRATEURS (nouvelle famille « Dynamique »)
# ===========================================================================
GENERATEUR = '''
def gen_force_balourd():
    """Force tournante d'un balourd : F = mb × r × ω²."""
    mb = random.choice([2, 5, 8, 10, 12, 15, 20])
    r = random.choice([50, 80, 100, 120, 150, 200])
    N = random.choice([750, 1000, 1500, 2000, 3000])
    w = 2 * math.pi * N / 60
    F = mb / 1000 * r / 1000 * w ** 2
    diag = []
    for val, msg in (
            (mb / 1000 * r / 1000 * w, "Il manque le carré de ω : la force de balourd croît comme ω²."),
            (mb / 1000 * r / 1000 * N ** 2, "Tu as utilisé N en tr/min au lieu de ω en rad/s (ω = 2πN/60)."),
            (mb * r / 1000 * w ** 2, "Tu as gardé la masse en grammes : 1 g = 0,001 kg."),
    ):
        if abs(val - F) > max(0.05, F * 0.02) * 2 and all(abs(val - d["v"]) > 0.05 for d in diag):
            diag.append(_diag(round(val, 2), msg))
    return {
        "titre": "Dynamique — force de balourd",
        "enonce": (f"Un rotor tourne à **{N} tr/min**. Son défaut d'équilibrage équivaut à une masse de **{mb} g** "
                   f"placée à **{r} mm** de l'axe. Quelle force tournante (en N) les paliers doivent-ils reprendre ?"),
        "rep": round(F, 2), "tol": max(0.05, F * 0.02), "unite": "N",
        "diag": diag,
        "corr": [
            f"**Ce que dit l'énoncé.** Balourd {mb} g à {r} mm, vitesse {N} tr/min.",
            f"**Les unités SI.** mb = {fr(mb / 1000, 3)} kg ; r = {fr(r / 1000, 3)} m ; ω = 2π × {N} / 60 = "
            f"{fr(w, 2)} rad/s.",
            f"**La force.** F = mb × r × ω² = {fr(mb / 1000, 3)} × {fr(r / 1000, 3)} × {fr(w, 2)}² = {fr(F, 1)} N.",
            "**Ce que cela apprend.** Le balourd (mb × r) ne change pas, mais sa force croît comme le carré de la "
            "vitesse : doubler N multiplie la force de balourd par 4. C'est pourquoi une machine rapide exige un "
            "équilibrage plus soigné.",
        ],
        "indice": "F = mb × r × ω², tout en unités SI (kg, m, rad/s).",
    }


def gen_cdg_arbre():
    """Centre de gravité d'un arbre étagé à deux tronçons cylindriques du même matériau."""
    d1 = random.choice([30, 40, 50, 60])
    L1 = random.choice([60, 80, 100, 120])
    d2 = random.choice([d for d in (16, 20, 25, 30) if d < d1])
    L2 = random.choice([40, 50, 60, 80])
    x1, x2 = L1 / 2, L1 + L2 / 2
    v1, v2 = d1 ** 2 * L1, d2 ** 2 * L2
    xg = (v1 * x1 + v2 * x2) / (v1 + v2)
    diag = []
    for val, msg in (
            ((x1 + x2) / 2, "Tu as fait la moyenne simple des positions : il faut pondérer par les masses."),
            ((L1 * x1 + L2 * x2) / (L1 + L2), "Tu as pondéré par les longueurs : la masse dépend aussi du diamètre "
                                              "(volume ∝ d² × L)."),
            ((d1 * L1 * x1 + d2 * L2 * x2) / (d1 * L1 + d2 * L2), "Tu as pondéré par d × L : le volume d'un cylindre "
                                                                  "est proportionnel à d², pas à d."),
    ):
        if abs(val - xg) > 0.6 and all(abs(val - d["v"]) > 0.5 for d in diag):
            diag.append(_diag(round(val, 2), msg))
    return {
        "titre": "Géométrie des masses — centre de gravité d'un arbre étagé",
        "enonce": (f"Un arbre en acier comporte deux tronçons : **Ø{d1} × {L1} mm**, puis **Ø{d2} × {L2} mm**. À quelle "
                   "distance de la face gauche (côté gros tronçon) se trouve son centre de gravité, en mm ?"),
        "rep": round(xg, 2), "tol": 0.3, "unite": "mm",
        "diag": diag,
        "corr": [
            f"**Ce que dit l'énoncé.** Deux cylindres du même matériau : les masses sont proportionnelles aux "
            f"volumes, donc à d² × L.",
            f"**Les centres de gravité.** x1 = {fr(x1, 1)} mm ; x2 = {L1} + {fr(L2 / 2, 1)} = {fr(x2, 1)} mm.",
            f"**Les parts de masse (∝ d² × L).** d1² × L1 = {v1} ; d2² × L2 = {v2}.",
            f"**Le barycentre.** xG = ({v1} × {fr(x1, 1)} + {v2} × {fr(x2, 1)}) / ({v1} + {v2}) = {fr(xg, 2)} mm.",
            "**Je vérifie.** G est entre G1 et G2, plus près du tronçon le plus lourd.",
        ],
        "indice": "xG = Σ mi xi / Σ mi ; même matériau : m ∝ d² × L.",
    }
'''

# ===========================================================================
# 6. QUIZ — nouvelle catégorie « Masse, inertie, PFD et équilibrage »
#    positions de la bonne réponse : 1, 3, 0, 2, 3, 1, 2, 0
# ===========================================================================
QUIZ_DYNAMIQUE = [
    ("Deux cylindres de même masse et même rayon extérieur : l'un plein, l'autre creux (tube mince). Lequel est le "
     "plus difficile à mettre en rotation ?",
     ["Le cylindre plein", "Le tube mince", "Ils sont identiques : même masse", "Cela dépend de la vitesse"], 1,
     "J = Σ m r² : dans le tube, toute la matière est loin de l'axe (J ≈ m R²) ; dans le cylindre plein, une partie "
     "est près de l'axe (J = ½ m R²). Le tube a environ deux fois plus d'inertie.", "Base"),
    ("Un disque a un moment d'inertie J_G autour de son axe. Autour d'un axe parallèle situé à la distance d, son "
     "moment d'inertie vaut :",
     ["J_G − m d²", "J_G", "J_G × d²", "J_G + m d²"], 3,
     "Théorème de Huygens : J_Δ = J_G + m d². L'axe passant par G donne toujours le plus petit moment d'inertie "
     "parmi les axes parallèles.", "Base"),
    ("Un balourd de 5 g à 100 mm tourne à 3 000 tr/min. Quelle force tournante crée-t-il ?",
     ["Environ 49 N", "Environ 0,16 N", "Environ 4 500 N", "Environ 1,6 N"], 0,
     "ω = 2π × 3 000 / 60 ≈ 314,2 rad/s ; F = 0,005 × 0,1 × 314,2² ≈ 49 N. Sans le carré de ω : 0,16 N ; avec N en "
     "tr/min : 4 500 N.", "Calcul"),
    ("Un rotor posé sur deux couteaux horizontaux ne roule pas. Que peut-on en conclure ?",
     ["Il est parfaitement équilibré", "Il a un balourd dynamique", "Il est équilibré statiquement, pas forcément dynamiquement",
      "Ses paliers sont trop serrés"], 2,
     "Sur couteaux, seul le poids agit : la pièce ne roule pas si G est sur l'axe (équilibrage statique). Deux "
     "balourds opposés dans des plans différents restent invisibles : ils ne se révèlent qu'en rotation.", "Piège"),
    ("Pour corriger un balourd dynamique, il faut agir sur :",
     ["Un seul plan, du côté opposé au point lourd", "La vitesse de rotation", "Le jeu des paliers",
      "Deux plans de correction"], 3,
     "Un balourd dynamique est un couple tournant : une seule masse corrective ne peut pas l'annuler sans créer une "
     "force. L'équilibreuse corrige dans deux plans.", "Intermédiaire"),
    ("Un treuil soulève une charge de 100 kg avec une accélération de 1 m/s² (g = 9,81 m/s²). Quelle est la tension "
     "du câble ?",
     ["981 N", "1 081 N", "881 N", "100 N"], 1,
     "PFD sur la charge : T − m g = m a → T = m (g + a) = 100 × 10,81 = 1 081 N. 881 N correspondrait à une charge "
     "qui accélère vers le bas.", "Calcul"),
    ("Quel est le lien entre le PFD et le théorème de l'énergie cinétique ?",
     ["Ils sont indépendants", "Le TEC ne vaut qu'en rotation",
      "Multiplier le PFD par la vitesse donne le TEC en puissance", "Le PFD ne vaut qu'à vitesse constante"], 2,
     "F × v = m a v = d(½ m v²)/dt, et C × ω = J α ω = d(½ J ω²)/dt. Le PFD parle d'efforts, le TEC d'énergie : "
     "deux portes pour le même mouvement.", "Intermédiaire"),
    ("Que garantit un équilibrage dynamique d'un rotor ?",
     ["Que l'axe de rotation est un axe principal d'inertie passant par G : ni force ni couple tournants",
      "Que le rotor ne roule pas sur couteaux, et rien de plus", "Que le rotor n'a plus aucune fréquence propre",
      "Que le moment d'inertie est minimal"], 0,
     "Dynamique = statique (G sur l'axe) + produits d'inertie nuls par rapport à l'axe : l'axe de rotation devient "
     "axe principal. Les fréquences propres, elles, existent toujours (fiche 13.5).", "Base"),
]
