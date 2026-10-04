# -*- coding: utf-8 -*-
# BROUILLON — fiche 6.20 « Chaîne d'énergie et motorisation : effort × flux, point de fonctionnement,
# rendement » (référentiel S3.1 et S5.3). Rien de ceci n'est encore dans app.py.
#
# Sources des valeurs utilisées :
# - classes de rendement : IEC 60034-30-1:2014, tableau des rendements minimaux à 50 Hz (note technique ABB
#   9AKK107319 EN 05-2018) — 4 pôles : 4 kW IE1 83,1 / IE2 86,6 / IE3 88,6 / IE4 91,1 % ;
#   11 kW IE1 87,6 / IE2 89,8 / IE3 91,4 / IE4 93,3 % ;
# - obligations européennes : règlement (UE) 2019/1781 modifié par 2021/341 (synthèse ABB « MEPS UE ») —
#   depuis le 1er juillet 2021, IE3 minimum pour les moteurs triphasés de 0,75 à 1 000 kW, 2 à 8 pôles
#   (IE2 de 0,12 à 0,75 kW) ; depuis le 1er juillet 2023, IE4 pour les 2, 4 et 6 pôles de 75 à 200 kW ;
# - « 75 % de l'énergie consommée dans l'industrie », « 30 % économisables » : texte du référentiel BTS CPI
#   (S3.1), cité comme tel ;
# - vitesse de synchronisme ns = 60 f / p (p = nombre de paires de pôles) : relation physique ;
# - toutes les autres valeurs (plaques moteur, charges, cylindrées, pressions, rendements volumétriques et
#   mécaniques) sont des DONNÉES D'ÉNONCÉ, annoncées comme telles.
import math

# ===========================================================================
# 1. FIGURES
# ===========================================================================

def chaine_energie():
    p = [_k_defs(), _txt(30, 24, "La chaîne d'énergie : la puissance traverse, et change de forme à chaque bloc", 13, TRAIT, "start", True)]
    blocs = (("ALIMENTER", "réseau, centrale hydr.", ALESAGE), ("STOCKER", "batterie, accumulateur", FIN),
             ("DISTRIBUER", "contacteur, variateur,", ALESAGE), ("CONVERTIR", "moteur, vérin", ARBRE),
             ("TRANSMETTRE", "réducteur, vis, courroie", OK))
    sous2 = ("", "(si besoin)", "distributeur", "", "")
    x0, w, g = 22, 120, 22
    for i, ((nom, ex, c), s2) in enumerate(zip(blocs, sous2)):
        x = x0 + i * (w + g)
        tir = " stroke-dasharray='5 3'" if nom == "STOCKER" else ""
        p.append(f"<rect x='{x}' y='60' width='{w}' height='70' rx='8' fill='#ffffff' stroke='{c}' stroke-width='2'{tir}/>")
        p.append(_txt(x + w / 2, 84, nom, 12, c, "middle", True))
        p.append(_txt(x + w / 2, 104, ex, 10, FIN, "middle"))
        if s2:
            p.append(_txt(x + w / 2, 118, s2, 10, FIN, "middle"))
        if i < 4:
            p.append(_k_fl(x + w + 2, 95, x + w + g - 2, 95, TRAIT, "kk", 2))
    xe = x0 + 5 * (w + g) - g + 4
    p.append(_k_fl(xe - 2, 95, xe + 18, 95, TRAIT, "kk", 2))
    p.append(_txt(xe + 22, 90, "effec-", 10, TRAIT, "start", True))
    p.append(_txt(xe + 22, 103, "teur", 10, TRAIT, "start", True))
    # couples effort × flux sous chaque liaison
    paires = ((x0 + w + g / 2, "U × I"), (x0 + 2 * (w + g) - g / 2, "U × I"), (x0 + 3 * (w + g) - g / 2, "U × I"),
              (x0 + 4 * (w + g) - g / 2, "C × ω"))
    for xm, t in paires:
        p.append(_txt(xm, 50, t, 11, ARBRE, "middle", True))
    p.append(_txt(xe + 26, 50, "C × ω ou F × v", 11, ARBRE, "end", True))
    # points de puissance qui défilent
    for k in range(4):
        p.append(f"<circle cy='140' r='4' fill='{ALERTE}'><animate attributeName='cx' values='{x0};{xe}' dur='4s' "
                 f"begin='{k}s' repeatCount='indefinite'/></circle>")
    p.append(_txt(x0, 156, "puissance qui circule", 10, ALERTE, "start", True))
    # pertes
    for i in (2, 3, 4):
        x = x0 + i * (w + g) + w / 2
        p.append(_k_fl(x, 132, x, 176, ALERTE, "kr", 2))
        p.append(_txt(x, 190, "pertes (chaleur)", 10, ALERTE, "middle", True))
    p.append(_txt(30, 214, "Au-dessus de chaque flèche : le couple « effort × flux » qui porte la puissance à cet endroit.", 11, FIN))
    p.append(_txt(30, 228, "Chaîne hydraulique : U × I → (moteur) → C × ω → (pompe) → p × Qv → (vérin) → F × v.", 11, OK, "start", True))
    p.append(f"<rect x='30' y='238' width='730' height='52' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 260, "Chaque bloc reçoit une puissance et en rend un peu moins : P sortie = η × P entrée.", 12, TRAIT, "start", True))
    p.append(_txt(46, 280, "Le rendement global est le produit des rendements partiels (fiche 8.2).", 12, FIN))
    return _svg("".join(p), 790, 304)


def analogie_effort_flux():
    p = [_k_defs(), _txt(30, 24, "Une seule idée dans trois domaines : puissance = effort × flux", 13, TRAIT, "start", True)]
    cols = (("MÉCANIQUE", ARBRE, ("translation : P = F × v", "N × m/s = W", "rotation : P = C × ω", "N·m × rad/s = W"),
             "effort : force F, couple C", "flux : vitesse v, ω"),
            ("ÉLECTRIQUE", ALESAGE, ("continu : P = U × I", "V × A = W", "triphasé (actif) :", "P = √3 U I cos φ"),
             "effort : tension U", "flux : courant I"),
            ("HYDRAULIQUE", OK, ("P = p × Qv", "Pa × m³/s = W", "", "1 bar = 10⁵ Pa"),
             "effort : pression p", "flux : débit Qv"))
    for i, (nom, c, lignes, eff, flux) in enumerate(cols):
        x = 30 + i * 248
        p.append(f"<rect x='{x}' y='42' width='232' height='196' rx='8' fill='#ffffff' stroke='{c}' stroke-width='2'/>")
        p.append(_txt(x + 116, 64, nom, 12, c, "middle", True))
        p.append(_txt(x + 116, 86, eff, 11, TRAIT, "middle"))
        p.append(_txt(x + 116, 102, flux, 11, TRAIT, "middle"))
        for j, t in enumerate(lignes):
            if t:
                p.append(_txt(x + 116, 132 + 22 * j, t, 12 if j % 2 == 0 else 11, c if j % 2 == 0 else FIN, "middle", j % 2 == 0))
        p.append(f"<rect x='{x + 20}' y='206' width='192' height='22' rx='4' fill='{c}' opacity='0.18'>"
                 f"<animate attributeName='opacity' values='0.18;0.45;0.18' dur='2.4s' begin='{0.8 * i}s' repeatCount='indefinite'/></rect>")
        p.append(_txt(x + 116, 221, "P = effort × flux, en W", 11, c, "middle", True))
    p.append(f"<rect x='30' y='252' width='728' height='54' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 274, "Un vérin Ø50 sous 100 bar, alimenté à 6 L/min (données d'énoncé) : F = p × S ≈ 19 635 N, v = Qv / S ≈ 0,051 m/s.", 12, TRAIT))
    p.append(_txt(46, 294, "p × Qv = 10⁷ × 10⁻⁴ = 1 000 W, et F × v ≈ 19 635 × 0,0509 ≈ 1 000 W : la même puissance, vue des deux côtés.", 12, OK, "start", True))
    return _svg("".join(p), 790, 320)


def couples_resistants():
    p = [_k_defs(), _txt(30, 24, "Quatre familles de couples résistants : comment la charge réagit à la vitesse", 13, TRAIT, "start", True)]
    types = (("CONSTANT", "C = constante", "levage, convoyeur, compresseur à piston", lambda u: 0.6, "P ∝ n"),
             ("LINÉAIRE", "C proportionnel à n", "frottement visqueux, calandre", lambda u: 0.75 * u, "P ∝ n²"),
             ("QUADRATIQUE", "C proportionnel à n²", "ventilateur, pompe centrifuge", lambda u: 0.8 * u * u, "P ∝ n³"),
             ("HYPERBOLIQUE", "C × n = constante", "enrouleuse, broche à puissance constante", lambda u: min(0.9, 0.18 / max(u, 0.05)), "P = constante"))
    for i, (nom, loi, ex, f, pl) in enumerate(types):
        x0 = 30 + i * 186
        p.append(f"<rect x='{x0}' y='40' width='174' height='236' rx='8' fill='#ffffff' stroke='{ALESAGE}' stroke-width='1.6'/>")
        p.append(_txt(x0 + 87, 60, nom, 11, ALESAGE, "middle", True))
        ox, oy, L, H = x0 + 26, 200, 130, 110
        p.append(_k_fl(ox, oy, ox + L + 6, oy, TRAIT, "kk", 1.4))
        p.append(_k_fl(ox, oy, ox, oy - H - 6, TRAIT, "kk", 1.4))
        p.append(_txt(ox + L + 4, oy + 14, "n", 10, TRAIT, "end"))
        p.append(_txt(ox - 4, oy - H, "C", 10, TRAIT, "end"))
        pts = " ".join(f"{ox + L * u:.1f},{oy - H * f(u):.1f}" for u in [k / 40 for k in range(2, 41)])
        p.append(f"<polyline points='{pts}' fill='none' stroke='{ARBRE}' stroke-width='2.6' stroke-dasharray='400' stroke-dashoffset='400'>"
                 f"<animate attributeName='stroke-dashoffset' values='400;0;0' dur='3s' begin='{0.5 * i}s' repeatCount='indefinite'/></polyline>")
        p.append(_txt(x0 + 87, 224, loi, 11, ARBRE, "middle", True))
        p.append(_txt(x0 + 87, 76, pl, 11, OK, "middle", True))
        mots = ex.split(", ")
        for j, m in enumerate(mots):
            p.append(_txt(x0 + 87, 244 + 14 * j, m + ("," if j < len(mots) - 1 else ""), 10, FIN, "middle"))
    p.append(f"<rect x='30' y='288' width='730' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 310, "La forme de la courbe de charge décide du point de fonctionnement et du moteur à choisir.", 12, TRAIT))
    return _svg("".join(p), 790, 336)


def _axes_fonctionnement(p, ox, oy, L, H, nmin, nmax, cmax):
    X = lambda n: ox + (n - nmin) / (nmax - nmin) * L  # noqa: E731
    Y = lambda c: oy - min(c, cmax) / cmax * H  # noqa: E731
    p.append(_k_fl(ox, oy, ox + L + 10, oy, TRAIT, "kk", 1.4))
    p.append(_k_fl(ox, oy, ox, oy - H - 10, TRAIT, "kk", 1.4))
    for n in range(int(nmin), int(nmax) + 1, 50):
        p.append(f"<line x1='{X(n):.1f}' y1='{oy}' x2='{X(n):.1f}' y2='{oy + 4}' stroke='{TRAIT}'/>")
        p.append(_txt(X(n), oy + 16, str(n), 9, FIN, "middle"))
    for c in range(0, int(cmax) + 1, 10):
        p.append(f"<line x1='{ox - 4}' y1='{Y(c):.1f}' x2='{ox}' y2='{Y(c):.1f}' stroke='{TRAIT}'/>")
        p.append(_txt(ox - 7, Y(c) + 3, str(c), 9, FIN, "end"))
    p.append(_txt(ox + L, oy - 8, "vitesse n (tr/min)", 10, TRAIT, "end"))
    p.append(_txt(ox + 4, oy + 30, f"zoom : l'axe commence à {int(nmin)} tr/min", 9, FIN, "start"))
    p.append(_txt(ox - 4, oy - H - 14, "couple C (N·m)", 10, TRAIT, "start"))
    return X, Y


_PLAQUE = {"ns": 1500.0, "nn": 1440.0, "Pn": 4000.0}   # moteur asynchrone 4 pôles, 50 Hz — données d'énoncé


def _cn():
    return _PLAQUE["Pn"] / (2 * math.pi * _PLAQUE["nn"] / 60)


def _c_moteur(n):
    """Modèle linéaire de la partie utile de la caractéristique (entre ns et un peu au-delà du nominal)."""
    return _cn() * (_PLAQUE["ns"] - n) / (_PLAQUE["ns"] - _PLAQUE["nn"])


def _intersection(c_charge):
    a, b = 1300.0, _PLAQUE["ns"]
    for _ in range(60):
        m = (a + b) / 2
        if _c_moteur(m) - c_charge(m) > 0:
            a = m
        else:
            b = m
    return (a + b) / 2


def point_fonctionnement():
    p = [_k_defs(), _txt(30, 24, "Le point de fonctionnement : là où le couple du moteur égale le couple de la charge", 13, TRAIT, "start", True)]
    ox, oy, L, H = 70, 280, 420, 220
    X, Y = _axes_fonctionnement(p, ox, oy, L, H, 1350, 1500, 50)
    pts = " ".join(f"{X(n):.1f},{Y(_c_moteur(n)):.1f}" for n in range(1350, 1501, 5) if _c_moteur(n) <= 50)
    p.append(f"<polyline points='{pts}' fill='none' stroke='{ALESAGE}' stroke-width='2.8'/>")
    p.append(_txt(X(1415), Y(46), "moteur", 11, ALESAGE, "start", True))
    k = 18 / 1450 ** 2
    pts = " ".join(f"{X(n):.1f},{Y(k * n * n):.1f}" for n in range(1350, 1501, 5))
    p.append(f"<polyline points='{pts}' fill='none' stroke='{ARBRE}' stroke-width='2.4'/>")
    p.append(_txt(X(1352), Y(k * 1352 ** 2) + 14, "ventilateur (quadratique)", 10, ARBRE, "start", True))
    p.append(f"<line x1='{X(1350):.1f}' y1='{Y(20):.1f}' x2='{X(1500):.1f}' y2='{Y(20):.1f}' stroke='{OK}' stroke-width='2.4' stroke-dasharray='7 4'/>")
    p.append(_txt(X(1352), Y(20) - 6, "convoyeur (constant, 20 N·m)", 10, OK, "start", True))
    # nominal
    cn = _cn()
    p.append(f"<circle cx='{X(1440):.1f}' cy='{Y(cn):.1f}' r='5' fill='none' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(_txt(X(1440) - 8, Y(cn) - 8, "nominal : 1 440 tr/min, 26,5 N·m", 10, TRAIT, "end"))
    for c_ch, col, dy, dx, anc in ((lambda n: k * n * n, ARBRE, 20, -10, "end"), (lambda n: 20.0, OK, -14, 10, "start")):
        n0 = _intersection(c_ch)
        p.append(f"<circle cx='{X(n0):.1f}' cy='{Y(c_ch(n0)):.1f}' r='6' fill='{col}'>"
                 "<animate attributeName='r' values='5;8;5' dur='1.6s' repeatCount='indefinite'/></circle>")
        p.append(_txt(X(n0) + dx, Y(c_ch(n0)) + dy, "point de fonctionnement", 9, col, anc, True))
    p.append(_txt(X(1395), Y(8), "moteur > charge : accélère →", 9, TRAIT, "middle"))
    p.append(_txt(X(1478), Y(31), "← charge > moteur", 9, TRAIT, "middle"))
    p.append(_txt(X(1478), Y(28), "ralentit", 9, TRAIT, "middle"))
    x0 = 520
    p.append(f"<rect x='{x0}' y='44' width='250' height='236' rx='6' fill='#ffffff' stroke='{FIN}'/>")
    nv, nc = _intersection(lambda n: k * n * n), _intersection(lambda n: 20.0)
    lignes = (("Plaque (énoncé) : 4 kW, 1 440 tr/min,", TRAIT, False), ("4 pôles, 50 Hz → ns = 1 500 tr/min", TRAIT, False),
              ("Cn = P / ω = 26,5 N·m", TRAIT, True), ("", TRAIT, False),
              ("Ventilateur : point à", ARBRE, False), (f"{_fr_court(nv, 0)} tr/min, {_fr_court(k * nv * nv, 1)} N·m", ARBRE, True),
              ("Convoyeur : point à", OK, False), (f"{_fr_court(nc, 0)} tr/min, 20 N·m", OK, True), ("", TRAIT, False),
              ("Les deux sont sous le nominal :", TRAIT, False), ("le moteur ne chauffe pas plus", TRAIT, False),
              ("que prévu.", TRAIT, False))
    for i, (t, c, g) in enumerate(lignes):
        if t:
            p.append(_txt(x0 + 12, 66 + 18 * i, t, 11, c, "start", g))
    p.append(_txt(30, 330, "Partie utile de la courbe du moteur, modélisée par une droite entre ns et le nominal ; le démarrage est traité en fiche 13.3.", 10, FIN))
    return _svg("".join(p), 790, 344)


def classes_ie():
    p = [_k_defs(), _txt(30, 24, "Classes de rendement IE : un moteur de 11 kW, 4 pôles, 50 Hz (IEC 60034-30-1)", 13, TRAIT, "start", True)]
    classes = (("IE1", 87.6), ("IE2", 89.8), ("IE3", 91.4), ("IE4", 93.3))
    ox, oy = 150, 70
    for i, (nom, eta) in enumerate(classes):
        y = oy + i * 50
        pab = 11000 / (eta / 100)
        pertes = pab - 11000
        p.append(_txt(ox - 12, y + 18, f"{nom} : η ≥ {_fr_court(eta, 1)} %", 12, TRAIT, "end", True))
        lw = pertes / 1600 * 380
        col = ALERTE if i == 0 else (ARBRE if i == 1 else OK)
        p.append(f"<rect x='{ox}' y='{y}' width='{lw:.1f}' height='28' rx='4' fill='{col}' opacity='0.8'>"
                 f"<animate attributeName='width' values='0;{lw:.1f};{lw:.1f}' dur='3s' repeatCount='indefinite'/></rect>")
        p.append(_txt(ox + lw + 8, y + 18, f"pertes ≈ {_fr_court(round(pertes), 0)} W", 12, col, "start", True))
    p.append(_txt(ox, oy + 210, "Longueur des barres : pertes à pleine charge, P absorbée − 11 000 W (échelle linéaire).", 10, FIN))
    p.append(f"<rect x='30' y='300' width='730' height='70' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 322, "De IE1 à IE3, les pertes baissent d'un tiers environ ; elles finissent en chaleur dans le moteur.", 12, TRAIT, "start", True))
    p.append(_txt(46, 342, "UE (règlement 2019/1781) : IE3 minimum depuis le 1er juillet 2021 de 0,75 à 1 000 kW ;", 11, FIN))
    p.append(_txt(46, 360, "IE4 depuis le 1er juillet 2023 pour les 2, 4 et 6 pôles de 75 à 200 kW (sauf exceptions du règlement).", 11, FIN))
    return _svg("".join(p), 790, 384)


def pompe_moteur_hydraulique():
    p = [_k_defs(), _txt(30, 24, "Pompe et moteur hydrauliques : la cylindrée relie le débit à la vitesse", 13, TRAIT, "start", True)]
    items = ((30, "MOTEUR ÉLECTRIQUE", "U × I", ALESAGE), (205, "POMPE", "C × ω → p × Qv", ARBRE),
             (440, "MOTEUR HYDRAULIQUE", "p × Qv → C × ω", OK), (640, "CHARGE", "C × ω", TRAIT))
    for x, nom, t, c in items:
        w = 150 if nom != "CHARGE" else 120
        p.append(f"<rect x='{x}' y='60' width='{w}' height='70' rx='8' fill='#ffffff' stroke='{c}' stroke-width='2'/>")
        p.append(_txt(x + w / 2, 88, nom, 11, c, "middle", True))
        p.append(_txt(x + w / 2, 110, t, 11, FIN, "middle"))
    p.append(_k_fl(182, 95, 203, 95, TRAIT, "kk", 2))
    p.append(_k_fl(592, 95, 638, 95, TRAIT, "kk", 2))
    # conduites aller/retour
    p.append(f"<line x1='357' y1='80' x2='438' y2='80' stroke='{ALERTE}' stroke-width='5'/>")
    p.append(f"<line x1='357' y1='112' x2='438' y2='112' stroke='{ALESAGE}' stroke-width='5'/>")
    for k in range(3):
        p.append(f"<circle cy='80' r='3' fill='#ffffff'><animate attributeName='cx' values='357;438' dur='1.5s' begin='{0.5 * k}s' repeatCount='indefinite'/></circle>")
        p.append(f"<circle cy='112' r='3' fill='#ffffff'><animate attributeName='cx' values='438;357' dur='1.5s' begin='{0.5 * k}s' repeatCount='indefinite'/></circle>")
    p.append(_txt(397, 72, "haute pression", 9, ALERTE, "middle", True))
    p.append(_txt(397, 128, "retour", 9, ALESAGE, "middle", True))
    p.append(_txt(397, 100, "huile", 9, FIN, "middle"))
    for xm in (280, 515):
        p.append(_k_fl(xm, 132, xm, 150, ALERTE, "kr", 1.6))
        p.append(_txt(xm, 160, "fuites (ηv), frottements (ηm) → chaleur", 9, ALERTE, "middle", True))
    x0 = 30
    for i, (t, c, g) in enumerate((("Cylindrée Cyl : volume d'huile chassé par tour (cm³/tr).", TRAIT, True),
                                   ("Sans pertes : C × ω = p × Qv, d'où Qv = Cyl × N et C = p × Cyl / (2π).", TRAIT, False),
                                   ("Les pertes jouent toujours contre toi : ce que la machine DONNE baisse (× η),", ALERTE, True),
                                   ("ce qu'elle DEMANDE augmente (÷ η). Rendement d'une machine : η = ηv × ηm.", ALERTE, True))):
        p.append(_txt(x0 + 16, 188 + 22 * i, t, 12, c, "start", g))
    p.append(f"<rect x='30' y='290' width='730' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 312, "Même principe (la cylindrée), en sens inverse : la pompe crée le débit, le moteur hydraulique le reçoit.", 12, TRAIT))
    return _svg("".join(p), 790, 338)


# --- figure à curseurs : point de fonctionnement d'un moteur asynchrone (plaque d'énoncé)
_CHARGES = {
    "Constant (convoyeur, levage)": lambda C0, n: C0,
    "Linéaire (frottement visqueux)": lambda C0, n: C0 * n / 1450,
    "Quadratique (ventilateur, pompe centrifuge)": lambda C0, n: C0 * (n / 1450) ** 2,
    "Hyperbolique (enrouleuse)": lambda C0, n: C0 * 1450 / n,
}
_CHOIX_CHARGES = [(k, k) for k in _CHARGES]   # (étiquette, valeur), format des curseurs « choix »


def dyn_point_fonctionnement(charge="Quadratique (ventilateur, pompe centrifuge)", C0=18.0):
    """Moteur asynchrone 4 pôles 50 Hz, 4 kW, 1 440 tr/min (énoncé) ; charge définie par son couple à 1 450 tr/min."""
    f = _CHARGES.get(charge, _CHARGES[_CHOIX_CHARGES[2][0]])
    cc = lambda n: f(C0, n)  # noqa: E731
    n0 = _intersection(cc)
    c0 = cc(n0)
    P0 = c0 * 2 * math.pi * n0 / 60
    cn = _cn()
    sur = c0 > cn + 1e-9
    p = [_k_defs(), _txt(30, 24, "Charge : " + charge.split(" (")[0].lower() + f", {_fr_court(C0, 0)} N·m à 1 450 tr/min", 13, TRAIT, "start", True)]
    ox, oy, L, H = 70, 280, 400, 220
    X, Y = _axes_fonctionnement(p, ox, oy, L, H, 1300, 1500, 60)
    pts = " ".join(f"{X(n):.1f},{Y(_c_moteur(n)):.1f}" for n in range(1300, 1501, 5) if _c_moteur(n) <= 60)
    p.append(f"<polyline points='{pts}' fill='none' stroke='{ALESAGE}' stroke-width='2.8'/>")
    p.append(_txt(X(1490), Y(_c_moteur(1490)) - 10, "moteur", 11, ALESAGE, "end", True))
    pts = " ".join(f"{X(n):.1f},{Y(cc(n)):.1f}" for n in range(1300, 1501, 5))
    p.append(f"<polyline points='{pts}' fill='none' stroke='{ARBRE}' stroke-width='2.4'/>")
    p.append(_txt(X(1302), Y(cc(1302)) - 8, "charge", 11, ARBRE, "start", True))
    p.append(f"<line x1='{X(1300):.1f}' y1='{Y(cn):.1f}' x2='{X(1500):.1f}' y2='{Y(cn):.1f}' stroke='{FIN}' stroke-dasharray='3 3'/>")
    p.append(_txt(X(1500), Y(cn) - 5, "Cn = 26,5 N·m", 9, FIN, "end"))
    col = ALERTE if sur else OK
    p.append(f"<circle cx='{X(n0):.1f}' cy='{Y(c0):.1f}' r='7' fill='{col}'/>")
    x0 = 500
    p.append(f"<rect x='{x0}' y='44' width='270' height='236' rx='6' fill='#ffffff' stroke='{col}' stroke-width='1.8'/>")
    lignes = (("Point de fonctionnement :", TRAIT, True),
              (f"n = {_fr_court(n0, 0)} tr/min", col, True),
              (f"C = {_fr_court(c0, 1)} N·m", col, True),
              (f"P utile = C × ω = {_fr_court(P0, 0)} W", col, True),
              ("", TRAIT, False),
              (("SURCHARGE : C dépasse Cn." if sur else "C ne dépasse pas Cn :"), col, True),
              (("Le moteur chauffe au-delà de" if sur else "régime admissible en continu."), TRAIT, False),
              (("sa classe : moteur plus gros." if sur else ""), TRAIT, False))
    for i, (t, c, g) in enumerate(lignes):
        if t:
            p.append(_txt(x0 + 12, 70 + 24 * i, t, 12, c, "start", g))
    p.append(_txt(30, 330, "Moteur (énoncé) : 4 kW, 1 440 tr/min, 4 pôles, 50 Hz. Droite valable de la marche à vide à un peu au-delà du nominal.", 10, FIN))
    return _svg("".join(p), 790, 344)


FIGURES_NOUVELLES = {
    "chaine_energie": ("La chaîne d'énergie : alimenter, distribuer, convertir, transmettre", chaine_energie),
    "analogie_effort_flux": ("Puissance = effort × flux, dans les trois domaines", analogie_effort_flux),
    "couples_resistants": ("Les quatre familles de couples résistants", couples_resistants),
    "point_fonctionnement": ("Le point de fonctionnement moteur / charge", point_fonctionnement),
    "classes_ie": ("Classes de rendement IE1 à IE4 d'un moteur de 11 kW", classes_ie),
    "pompe_moteur_hydraulique": ("Pompe et moteur hydrauliques : la cylindrée", pompe_moteur_hydraulique),
}
DYN_NOUVELLE = {
    "point_fonctionnement_curseurs": (
        "Choisis le type de charge et son couple : le point de fonctionnement se déplace",
        dyn_point_fonctionnement,
        [{"nom": "charge", "label": "Type de charge", "choix": _CHOIX_CHARGES, "defaut": _CHOIX_CHARGES[2][0]},
         {"nom": "C0", "label": "Couple de la charge à 1 450 tr/min (N·m)", "min": 5.0, "max": 40.0, "defaut": 18.0, "pas": 1.0}]),
}

# ===========================================================================
# 2. FICHE 6.20 — en FIN de bloc 6 (après la 6.19)
# ===========================================================================

FICHE_6_20 = {
    "id": "6.20",
    "titre": "Chaîne d'énergie et motorisation : effort × flux, point de fonctionnement, rendement",
    "duree": "6 h",
    "cours": """### 1. Pourquoi cette fiche

Le référentiel du BTS CPI le dit en ouverture du chapitre S3.1, à propos de la motorisation électrique :
« Cette consommation électrique représente 75% de l'énergie consommée dans l'industrie. Sachant qu'il est
possible d'économiser 30% de cette énergie par l'amélioration du rendement, un dimensionnement correct
associé à des dispositifs de régulation optimisés, […] ». Le concepteur qui
choisit un moteur décide donc d'une part de la facture et de l'empreinte du produit pendant toute sa vie.

Les fiches 8.2 et 8.5 ont posé P = C × ω et la multiplication des rendements ; la fiche 13.3 a donné les
familles de moteurs, le calcul du démarrage (inertie ramenée), le profil de commande et le choix du
rapport de réduction. Cette fiche relie le tout : **d'où vient
la puissance, sous quelle forme elle circule, où elle se perd, et à quelle vitesse le moteur va vraiment
tourner une fois attelé à sa charge.**

### 2. La chaîne d'énergie

[[FIG:chaine_energie]]

Toute machine motorisée suit le même trajet :

- **Alimenter** : prendre l'énergie quelque part (réseau électrique, batterie, centrale hydraulique).
- **Stocker** (si besoin) : garder l'énergie pour plus tard (batterie, accumulateur hydropneumatique).
- **Distribuer** : laisser passer l'énergie quand la commande le demande (contacteur, variateur de
  vitesse, distributeur hydraulique).
- **Convertir** : changer de forme d'énergie (un moteur électrique transforme U × I en C × ω ; un vérin
  transforme p × Qv en F × v).
- **Transmettre** : adapter le mouvement à l'effecteur (réducteur, poulies, vis-écrou — fiche 6.18).

**Réversibilité.** Un actionneur est réversible s'il peut aussi recevoir la puissance de la charge : un
moteur électrique qui retient une charge en descente devient générateur (l'énergie est renvoyée au réseau
ou dissipée dans une résistance de freinage). Pour une transmission (vis irréversible, vis à billes), voir
la fiche 6.18.

À chaque bloc, une partie de la puissance part en chaleur : **P sortie = η × P entrée**, et le rendement
global est le **produit** des rendements partiels.

### 3. Le fil conducteur : puissance = effort × flux

[[FIG:analogie_effort_flux]]

Dans les trois domaines que traverse une chaîne d'énergie, la puissance s'écrit de la même façon : le
produit d'une grandeur d'**effort** (ce qui pousse) par une grandeur de **flux** (ce qui circule).

| Domaine | Effort | Flux | Puissance |
|---|---|---|---|
| Mécanique, translation | force F (N) | vitesse v (m/s) | **P = F × v** |
| Mécanique, rotation | couple C (N·m) | vitesse angulaire ω (rad/s) | **P = C × ω** |
| Électrique (continu) | tension U (V) | courant I (A) | **P = U × I** |
| Hydraulique | pression p (Pa) | débit Qv (m³/s) | **P = p × Qv** |

*En hydraulique, p est la **différence** de pression entre l'entrée et la sortie (le retour au réservoir
est pris à 0 bar relatif). Le débit est noté Qv ici, Q en fiche 8.2 : c'est la même grandeur.*

*En alternatif triphasé, la puissance électrique absorbée s'écrit P = √3 × U × I × cos φ (fiches 8.2 et
8.11 ; U : tension entre phases) : c'est toujours un effort (U) par un flux (I) ; cos φ tient compte du
fait que tension et courant n'atteignent pas leur maximum au même instant. La fiche 8.2 écrit
P = √3 U I cos φ × η pour la puissance mécanique utile : le η fait le passage.*

**Les unités le confirment** (vérification des unités) : N × m/s = J/s = W ; V × A = W ;
Pa × m³/s = (N/m²) × (m³/s) = N·m/s = W. Trois domaines, **une seule unité de puissance**.

**Pourquoi c'est utile.** Un convertisseur ne crée pas de puissance : il échange un couple effort-flux contre
un autre. Un vérin transforme une pression en force (F = p × S) et un débit en vitesse (v = Qv / S) : à
puissance égale, si l'on veut plus de force, on obtient moins de vitesse. Un réducteur fait la même chose
avec le couple et la vitesse angulaire.

*Exemple (données d'énoncé) : un vérin Ø50 (S ≈ 1 963 mm²) alimenté sous 100 bar (10⁷ Pa) avec un débit de
6 L/min (10⁻⁴ m³/s). Côté hydraulique : P = p × Qv = 10⁷ × 10⁻⁴ = **1 000 W**. Côté mécanique : F = p × S =
10 N/mm² × 1 963 mm² ≈ 19 635 N, v = Qv / S = 10⁻⁴ / 1,963 × 10⁻³ ≈ 0,051 m/s, et F × v ≈ **1 000 W**.
La même puissance, vue des deux côtés du vérin (pertes négligées).*

### 4. Énergie, travail et théorème de l'énergie cinétique

*Pourquoi un moteur qui entraîne très bien sa charge une fois lancé peut-il peiner au démarrage ? Parce
qu'au démarrage, il doit en plus « remplir un réservoir » : l'énergie de mouvement des pièces. Une fois le
réservoir plein (vitesse atteinte), il ne paie plus que la charge.*

L'**énergie cinétique** est l'énergie que possède un solide parce qu'il bouge :

- en translation : **Ec = ½ × m × v²** ;
- en rotation autour d'un axe fixe : **Ec = ½ × J × ω²** (J : moment d'inertie, kg·m², noté I en fiche
  8.1).

Le **théorème de l'énergie cinétique** dit que la variation d'énergie cinétique d'un solide, entre deux
instants, est égale à la somme des travaux des efforts qui s'exercent sur lui :

> **ΔEc = Σ (travaux des efforts)**, en joules — ou, en puissance : **dEc/dt = Σ P** (la variation d'énergie
> cinétique par seconde = puissance motrice − puissances résistantes)

Chaque puissance du bilan est encore un effort × un flux : côté moteur C_m × ω, côté charge C_r × ω. Pour
un arbre entraîné, le théorème en puissance s'écrit donc **dEc/dt = (C_m − C_r) × ω**. Pour plusieurs
solides liés (moteur, réducteur, charge), on ajoute les puissances perdues dans les liaisons
(frottements) : c'est là qu'interviennent les rendements.

**Ce que ça dit concrètement.** Pendant un démarrage, le moteur fournit à la fois la puissance de la charge
**et** l'énergie cinétique qu'il faut donner aux pièces en mouvement. Une fois la vitesse atteinte, Ec ne
varie plus : le moteur ne fournit plus que la puissance de la charge et des frottements.

*Exemple (données d'énoncé) : un volant de J = 0,5 kg·m² amené de 0 à 1 500 tr/min (ω ≈ 157,1 rad/s).
Ec = ½ × 0,5 × 157,1² ≈ **6 170 J**. Si le démarrage dure 2 s, il faut en moyenne 6 170 / 2 ≈ **3 080 W**
en plus de la charge : c'est pourquoi le démarrage décide souvent de la taille du moteur (fiche 13.3).*

### 5. Les couples résistants : comment la charge réagit à la vitesse

[[FIG:couples_resistants]]

Une charge ne demande pas le même couple à toutes les vitesses. On distingue quatre familles :

- **couple constant** — levage, convoyeur, compresseur à piston : le couple ne dépend pas de la vitesse
  (soulever une masse demande le même couple, qu'on monte vite ou lentement). P = C × ω est un effort fixe
  multiplié par un flux qui augmente : la puissance croît comme n ;
- **couple linéaire** — C proportionnel à n. *Une cuillère dans du miel : deux fois plus vite, deux fois
  plus dur.* C'est le frottement visqueux, celui d'un fluide épais ; on le rencontre aussi sur une calandre
  (machine à rouleaux qui lamine du papier, du plastique ou du textile). P varie comme n² ;
- **couple quadratique** — ventilateur, pompe centrifuge : C proportionnel à n² (l'air ou l'eau brassés
  résistent d'autant plus qu'on les brasse vite). P = C × ω, avec C en n² et ω en n : **P varie comme n³** ;
- **couple hyperbolique** — C × n = constante. *Une enrouleuse de film plastique : le film doit défiler à
  vitesse constante et rester tendu pareil. Plus la bobine grossit, plus elle doit tourner lentement (son
  tour est plus long) et plus il faut de couple (le rayon, donc le bras de levier, augmente).* C × ω reste
  constant : la puissance ne bouge pas.

*Conséquence importante pour un ventilateur ou une pompe centrifuge : comme la puissance varie comme n³,
réduire un peu la vitesse réduit beaucoup la puissance (à 80 % de la vitesse : 0,8³ ≈ 0,51). C'est pour ces charges qu'un variateur de vitesse
est le plus rentable.*

### 6. Le point de fonctionnement : où le moteur va vraiment tourner

[[FIG:point_fonctionnement]]

Un moteur asynchrone ne tourne pas à une vitesse fixe : sa vitesse dépend du couple qu'on lui demande.
Sa **vitesse de synchronisme** — celle du champ tournant — vaut **ns = 60 × f / p** (f : fréquence du
réseau, p : nombre de **paires** de pôles ; fiche 8.11). À vide, il tourne presque à ns ; plus on le
charge, plus il ralentit : pour produire un couple, le rotor doit tourner un peu moins vite que le champ,
parce que c'est ce retard qui crée les courants dans le rotor. Ce retard relatif est le **glissement**
g = (ns − n) / ns (fiche 13.3).

Dans sa partie utile, de la marche à vide jusqu'un peu au-delà du nominal, sa courbe couple-vitesse est
presque une **droite** qui passe par (ns ; 0) et par le point nominal (nn ; Cn). Cette droite ne vaut
plus près du couple maximal du moteur (couple de décrochage) : en dessous de la vitesse de ce maximum, la
courbe s'effondre et le modèle est faux.

> Le **point de fonctionnement** est l'intersection de la courbe du moteur et de la courbe de la charge :
> **C moteur(n) = C charge(n)**. C'est là, et seulement là, que la vitesse se stabilise.

Le moteur et la charge sont sur le même arbre : ils partagent forcément le même flux, la vitesse. Le point
de fonctionnement, c'est le flux auquel l'effort que le moteur peut donner égale l'effort que la charge
réclame.

**Pourquoi là ?** Reprenons le théorème de l'énergie cinétique : dEc/dt = (C_m − C_r) × ω.

- C_m > C_r : la différence de couple sert à accélérer, la vitesse monte.
- C_m < C_r : le moteur puise dans l'énergie cinétique, la vitesse baisse.
- C_m = C_r : Ec ne change plus, la vitesse est stable.

*Image : une voiture en côte, accélérateur bloqué. Elle accélère tant que la poussée du moteur dépasse la
résistance, ralentit si la pente durcit, et se stabilise à la vitesse où les deux se valent. Personne ne
« règle » cette vitesse : c'est l'équilibre qui la fixe.* Ce raisonnement vaut parce que, dans la partie
utile, le couple du moteur baisse plus vite avec n que le couple de la charge : le point est stable.

*Exemple (plaque d'énoncé) : moteur 4 kW, 1 440 tr/min, 4 pôles (p = 2), 50 Hz → ns = 60 × 50 / 2 =
1 500 tr/min ; glissement nominal g = (1 500 − 1 440) / 1 500 = 4 % ; Cn = 4 000 / (2π × 1 440 / 60) ≈
**26,5 N·m**. La droite du moteur :*

> *C moteur(n) = 26,5 × (1 500 − n) / (1 500 − 1 440), où le dénominateur 1 500 − 1 440 = 60 tr/min est
> l'écart ns − nn — pas une conversion de tr/min en rad/s. Vérification : n = 1 500 donne C = 0 (à vide) ;
> n = 1 440 donne C = 26,5 (nominal).*

- *Convoyeur, couple constant de 20 N·m (ramené à l'arbre moteur) : 26,5 × (1 500 − n) / (1 500 − 1 440) =
  20 → n ≈ **1 455 tr/min** ; ω = 2π × 1 455 / 60 ≈ 152,3 rad/s ; P ≈ 20 × 152,3 ≈ **3 050 W**.*
- *Ventilateur, couple quadratique valant 18 N·m à 1 450 tr/min : 26,5 × (1 500 − n) / (1 500 − 1 440) =
  18 × (n / 1 450)². C'est une équation du second degré, qu'on résout à la calculatrice — ou qu'on lit sur la
  figure à curseurs ci-dessous : n ≈ **1 459 tr/min**, C ≈ 18,2 N·m, P ≈ **2 780 W**.*

[[DYN:point_fonctionnement_curseurs]]

**Le point de conception.** En régime permanent, le couple au point de fonctionnement doit être **plus
faible que Cn** — donc la vitesse un peu plus élevée que nn : à droite du point nominal sur le graphe.
Au-delà, le moteur fournit plus que ce pour quoi il est construit et chauffe au-delà de sa classe
d'isolation (la classe thermique des isolants du bobinage, qui fixe l'échauffement admissible).

**Choisir le moteur, en quatre questions.**

1. **Quel couple la charge demande-t-elle, ramené à l'arbre, vers la vitesse prévue ?** Lire sa famille
   (§5) et sa valeur.
2. **Je prends dans le catalogue le premier moteur dont Cn dépasse ce couple**, puis je calcule (ou je
   trace) le point de fonctionnement.
3. **Couple au point plus grand que Cn ?** Le moteur chaufferait en continu : je passe à la taille
   au-dessus et je recommence.
4. **Le démarrage passe-t-il ?** Énergie cinétique à fournir (§4), méthode complète en fiche 13.3.

*Pourquoi pas « beaucoup plus gros, pour être tranquille » ? Un moteur a des pertes presque fixes : il faut
aimanter le fer et faire tourner son ventilateur, quelle que soit la charge. Peu chargé, il paie ces pertes
pour peu de puissance utile, et son rendement baisse — comme un bus qui roule avec deux passagers consomme
presque autant que plein.*

### 7. Rendement des moteurs : les classes IE1 à IE4

[[FIG:classes_ie]]

La norme **IEC 60034-30-1** classe les moteurs à courant alternatif alimentés directement par le réseau
(des asynchrones pour l'essentiel) selon leur rendement minimal à pleine charge :
IE1 (standard), IE2 (haut rendement), IE3 (premium), IE4 (super premium). Les seuils dépendent de la
puissance et du nombre de pôles. Pour un moteur de **11 kW, 4 pôles, 50 Hz** : IE1 ≥ 87,6 %, IE2 ≥ 89,8 %,
IE3 ≥ 91,4 %, IE4 ≥ 93,3 %.

Le rendement d'un moteur compare encore deux produits effort × flux : η = (C × ω) / (√3 × U × I × cos φ).
Le moteur reçoit de la tension et du courant, et rend du couple et de la vitesse ; ce qui manque est devenu
chaleur.

*Ce que ça représente : à pleine charge, un IE1 de 11 kW absorbe **au plus** 11 000 / 0,876 ≈ 12 557 W, un
IE3 **au plus** 11 000 / 0,914 ≈ 12 035 W. En comparant ces deux seuils sur 4 000 h de fonctionnement par
an (donnée d'énoncé) : (12,557 − 12,035) kW × 4 000 h ≈ **2 090 kWh par an** d'écart estimé, pour un seul
moteur.*

**Ce qu'impose la réglementation européenne** (règlement (UE) 2019/1781) : depuis le 1er juillet 2021, les
moteurs triphasés de 0,75 à 1 000 kW (2 à 8 pôles) mis sur le marché doivent être au moins **IE3** ; depuis
le 1er juillet 2023, les moteurs 2, 4 et 6 pôles de 75 à 200 kW doivent être **IE4** (sauf exceptions
prévues par le règlement). Un concepteur ne « choisit » donc plus un IE1 : il choisit entre IE3 et mieux,
et il dimensionne juste, parce qu'un moteur très peu chargé travaille loin de son rendement de plaque
(l'image du bus, §6).

### 8. Pompes et moteurs hydrauliques

[[FIG:pompe_moteur_hydraulique]]

Une **pompe hydraulique volumétrique** convertit la puissance mécanique du moteur qui l'entraîne (C × ω) en
puissance hydraulique (p × Qv). Un **moteur hydraulique** fait l'inverse : même principe, en sens inverse
(certaines machines sont réversibles, mais une pompe ne s'utilise pas forcément en moteur).

**D'abord la machine idéale, sans pertes.** *Une pompe volumétrique, c'est une pompe à vélo qu'on
actionnerait en tournant : à chaque tour, elle chasse toujours le même volume d'huile, la **cylindrée**
Cyl (par exemple 16 cm³/tr).* À N tours par minute, elle débite donc **Qv = Cyl × N**. Et puisque, sans
pertes, effort × flux se conserve : C × ω = p × Qv, avec ω = 2π × N (N en tr/s) et Qv = Cyl × N, d'où
C × 2π × N = p × Cyl × N : le N se simplifie, **C = p × Cyl / (2π)** (p en Pa, Cyl en m³/tr).

**Ensuite les pertes. Une seule règle : elles jouent toujours contre toi.**

- **ηv, rendement volumétrique** : les fuites internes — la pompe à vélo dont le joint fuit.
- **ηm, rendement hydromécanique** : les frottements et pertes internes — une partie du couple sert à les
  vaincre.

| | Pompe (reçoit C × ω, donne p × Qv) | Moteur hydraulique (reçoit p × Qv, donne C × ω) |
|---|---|---|
| ηv | elle **donne** moins de débit : Qv = Cyl × N **× ηv** | une partie du débit fuit sans le faire tourner : N = Qv **× ηv** / Cyl |
| ηm | elle **demande** plus de couple : C = p × Cyl / (2π) **÷ ηm** | il **donne** moins de couple : C = p × Cyl / (2π) **× ηm** |

*Pour vérifier : ce que la machine donne baisse (× η) ; ce qu'elle demande augmente (÷ η). Rendement d'une
machine : η = ηv × ηm.*

*Exemple (données d'énoncé) : pompe de 16 cm³/tr entraînée à 1 450 tr/min, ηv = 0,95, ηm = 0,90, sous
150 bar. Qv = 16 × 1 450 × 0,95 = 22 040 cm³/min ≈ **22,0 L/min**. P hydraulique = p × Qv = 150 × 10⁵ ×
22,04 × 10⁻³ / 60 ≈ **5 510 W**. Couple absorbé : 150 × 10⁵ × 16 × 10⁻⁶ / (2π × 0,90) ≈ 42,4 N·m ; avec
ω = 2π × 1 450 / 60 ≈ 151,8 rad/s, la puissance mécanique vaut C × ω ≈ 42,4 × 151,8 ≈ **6 440 W**.
Rendement : 5 510 / 6 440 ≈ 0,855 = 0,95 × 0,90 ✔ — effort × flux d'un côté, effort × flux de l'autre.*

**Transmission hydrostatique** : une pompe et un moteur hydraulique reliés par des conduites. Elle permet
de transmettre une grande puissance loin et dans des endroits encombrés (engins de chantier, machines
agricoles), avec une vitesse réglable — au prix d'un rendement global plus faible qu'une transmission
mécanique, puisque deux conversions se suivent.

### 9. Les erreurs classiques

1. **Mélanger les unités dans effort × flux** : bar et L/min dans P = p × Qv donnent un nombre faux.
   Toujours Pa et m³/s (ou : P (W) = p (bar) × Qv (L/min) × 10⁵ × 10⁻³ / 60).
2. **Oublier 2π/60** : P = C × ω avec ω en rad/s, pas N en tr/min.
3. **Prendre ns pour la vitesse du moteur** : un asynchrone tourne sous ns, d'autant plus bas qu'il est
   chargé.
4. **Lire le 60 de la droite du moteur comme une conversion** : dans C = Cn × (ns − n) / (ns − nn), il vaut
   ns − nn.
5. **Confondre p (paires de pôles) et le nombre de pôles** : un moteur 4 pôles a p = 2, donc ns = 1 500
   tr/min à 50 Hz.
6. **Choisir le moteur sur la seule puissance de la charge en régime établi** : le démarrage (énergie
   cinétique) et le point de fonctionnement décident aussi.
7. **Croire que le rendement de plaque vaut à toutes les charges** : la classe IE est définie à pleine
   charge.
8. **Additionner les rendements** de la pompe et du moteur hydraulique : ils se multiplient.

### 10. À retenir

- Chaîne d'énergie : **alimenter → (stocker) → distribuer → convertir → transmettre**. À chaque bloc,
  P sortie = η × P entrée ; η global = produit des η.
- **Puissance = effort × flux** : F × v, C × ω, U × I, p × Qv — toujours des watts.
- **TEC** : ΔEc = Σ travaux ; en puissance, dEc/dt = (C_m − C_r) × ω ; Ec = ½ m v², ½ J ω². Le démarrage
  coûte de l'énergie.
- Couples résistants : **constant, linéaire, quadratique, hyperbolique**.
- **Point de fonctionnement** = intersection moteur / charge ; couple au point plus faible que Cn, sinon
  moteur plus gros. ns = 60 f / p ; le moteur tourne sous ns (glissement).
- **IE1 à IE4** (IEC 60034-30-1) ; IE3 minimum en UE depuis 2021 (0,75 à 1 000 kW).
- Pompe : **Qv = Cyl × N × ηv**, η = ηv × ηm ; le moteur hydraulique fait l'inverse. Les pertes : ce que
  la machine donne × η, ce qu'elle demande ÷ η.
""",
    "formules": """
**Puissance = effort × flux** — P = F × v · P = C × ω (ω = 2πN/60) · P = U × I · P = p × Qv (Pa, m³/s)

**Triphasé (puissance active)** — P = √3 × U × I × cos φ

**Rendement** — η = P sortie / P entrée · chaîne : η = η1 × η2 × …

**Énergie cinétique** — translation : Ec = ½ m v² · rotation : Ec = ½ J ω² · **TEC : ΔEc = Σ travaux** ·
en puissance : dEc/dt = (C_m − C_r) × ω

**Vitesse de synchronisme** — ns = 60 f / p (p : paires de pôles) · glissement g = (ns − n) / ns

**Moteur asynchrone, partie utile** — C(n) ≈ Cn × (ns − n) / (ns − nn)

**Point de fonctionnement** — C moteur(n) = C charge(n)

**Pompe** — Qv = Cyl × N × ηv · C = p × Cyl / (2π ηm) · **Moteur hydraulique** — N = Qv ηv / Cyl · C = p Cyl ηm / (2π)

**Classes IE** — IEC 60034-30-1 ; ex. 11 kW, 4 pôles, 50 Hz : IE1 87,6 · IE2 89,8 · IE3 91,4 · IE4 93,3 %
""",
    "exemple": """
### Cas industriel — La centrale de ventilation qui consommait trop

**Le symptôme.** Une centrale de ventilation d'atelier est entraînée par un moteur asynchrone ancien, de
classe IE1 (données d'énoncé : 11 kW, 4 pôles, 50 Hz), qui tourne en permanence. Le débit d'air est réglé
en fermant partiellement un volet : le moteur tourne donc toujours à pleine vitesse.

**L'analyse, bloc par bloc de la chaîne d'énergie.**

- **Convertir** : à pleine charge (on suppose ici le moteur à pleine charge, donnée d'énoncé), un IE1 de
  11 kW 4 pôles a un rendement d'au moins 87,6 % ; un IE3, d'au moins 91,4 % (IEC 60034-30-1). Remplacer le
  moteur fait passer la puissance absorbée **maximale** de 12 557 W à 12 035 W : environ 520 W d'économie
  estimée, à vitesse égale.
- **Distribuer et réguler** : aujourd'hui, on règle le débit par un volet, une perte volontaire dans le
  circuit d'air ; le ventilateur tourne toujours à la même vitesse. Côté air, la puissance est encore un
  effort × un flux : P = Δp × Qv. Le volet crée une chute de pression, et la puissance correspondante est
  brûlée dans le volet, pour rien — comme rouler pied au plancher en tenant sa vitesse avec le frein. Un
  variateur, placé dans le bloc Distribuer, règle plutôt la vitesse.

**Le calcul qui convainc.** Chaque tour de roue du ventilateur pousse à peu près le même volume d'air : sur
un réseau d'air inchangé (volet ouvert en grand, pas de pression statique à vaincre), les **lois de
similitude** des ventilateurs donnent débit ∝ n, pression ∝ n², puissance ∝ n³. Un débit de 80 % s'obtient
donc à 80 % de la vitesse, et la puissance tombe à 0,8³ ≈ **0,51** fois celle à pleine vitesse. Avec le
volet, la puissance baisse aussi un peu, mais beaucoup moins : l'écart entre les deux réglages est le gain
du variateur.

**Ce que le cas apprend.** Le rendement du moteur compte, mais la plus grosse économie vient souvent du
**bon réglage de la chaîne** : supprimer la perte volontaire (le volet) plutôt que gagner quelques points
de rendement. C'est exactement l'esprit du référentiel : rendement **et** dimensionnement **et** régulation.
""",
    "exercice": """
### Exercice — Motoriser un convoyeur

Un convoyeur est entraîné par un moteur asynchrone dont la plaque (données d'énoncé) indique : **4 kW,
1 440 tr/min, 4 pôles, 50 Hz**. Ramené à l'arbre du moteur, le convoyeur demande un **couple constant de
22 N·m**.

**1.** Calculer la vitesse de synchronisme ns et le couple nominal Cn du moteur.

**2.** En modélisant la partie utile de la courbe du moteur par une droite passant par (ns ; 0) et
(1 440 ; Cn), calculer la vitesse au point de fonctionnement.

**3.** Calculer la puissance utile au point de fonctionnement. Le moteur est-il en surcharge ?

**4.** Le moteur est de classe IE3. Un moteur IE3 de 4 kW, 4 pôles, a un rendement d'au moins 88,6 % à
pleine charge (IEC 60034-30-1). Quelle puissance absorbe-t-il au plus à sa charge nominale ?

**5.** Au démarrage, la bande et ses rouleaux représentent, ramenés à l'arbre moteur, une inertie de
0,2 kg·m² (donnée d'énoncé ; inertie du rotor du moteur négligée). Quelle énergie cinétique faut-il leur
donner pour atteindre la vitesse de fonctionnement ?
""",
    "corrige": """
### Corrigé, en six temps

#### 1. Ce que dit l'énoncé

Un moteur asynchrone connu par sa plaque, une charge à couple constant, un rendement de classe IE3, une
inertie à mettre en mouvement.

#### 2. Quelle règle, et pourquoi

> ns = 60 f / p ; Cn = Pn / ωn ; point de fonctionnement : **C moteur(n) = C charge(n)** ; P = C × ω ;
> P absorbée = P utile / η ; **Ec = ½ J ω²**.

#### 3. Les conversions

4 pôles → p = 2 paires. ω = 2πN/60 en rad/s. Puissances en W.

#### 4. Le remplacement

ns = 60 × 50 / 2. Cn = 4 000 / (2π × 1 440 / 60). Cn × (1 500 − n) / (1 500 − 1 440) = 22.

#### 5. Le calcul

**1.** ns = **1 500 tr/min**. ωn = 150,8 rad/s ; Cn = 4 000 / 150,8 ≈ **26,5 N·m**.

**2.** 26,53 × (1 500 − n) / (1 500 − 1 440) = 22 → 1 500 − n = 22 × 60 / 26,53 ≈ 49,8 (le 60 est
ns − nn) → n ≈ **1 450 tr/min**.

**3.** ω = 2π × 1 450,2 / 60 ≈ 151,9 rad/s ; P = 22 × 151,9 ≈ **3 340 W**. 22 N·m est sous Cn = 26,5 N·m :
**pas de surcharge**, le moteur travaille à environ 83 % de son couple nominal.

**4.** P absorbée ≤ 4 000 / 0,886 ≈ **4 515 W** à la charge nominale. La classe IE ne garantit le
rendement qu'à pleine charge : au point de fonctionnement (3 340 W), on ne pourrait que l'estimer — c'est
pour cela que la question porte sur le point nominal.

**5.** Ec = ½ × 0,2 × 151,9² ≈ **2 300 J**.

#### 6. La vérification

**Ordre de grandeur** : un asynchrone 4 pôles chargé tourne un peu sous 1 500 tr/min — 1 450 est
plausible, et plus proche de ns que le nominal (1 440), puisque la charge est plus faible que Cn.
**Cohérence** : P (3 340 W) est sous Pn (4 000 W), comme C sous Cn. **Unités** : J = kg·m² × (rad/s)².
""",
}

# ===========================================================================
# 3. MÉTHODE
# ===========================================================================
MTH_6_20 = ("6.20", "Trouver le point de fonctionnement d'un moteur asynchrone", [
    "**Lire la plaque** : Pn, nn, nombre de pôles, fréquence. Nombre de pôles ÷ 2 = p (paires).",
    "**Calculer ns = 60 f / p et Cn = Pn / ωn**, avec ωn = 2π nn / 60 en rad/s.",
    "**Écrire la droite du moteur** dans sa partie utile : C(n) = Cn × (ns − n) / (ns − nn) (le dénominateur "
    "est l'écart ns − nn, pas une conversion).",
    "**Écrire la courbe de la charge** ramenée à l'arbre moteur (constante, linéaire, quadratique ou "
    "hyperbolique) et résoudre C moteur(n) = C charge(n).",
    "**Conclure** : vitesse, couple, puissance au point. Si le couple dépasse Cn : moteur de taille "
    "supérieure, puis recalculer ; vérifier ensuite le démarrage (fiche 13.3).",
], "Moteur 4 kW, 1 440 tr/min, 4 pôles, 50 Hz : ns = 1 500 tr/min, Cn ≈ 26,5 N·m. Charge constante "
   "22 N·m : 26,5 × (1 500 − n) / (1 500 − 1 440) = 22 → n ≈ 1 450 tr/min, P ≈ 3 340 W, sous le nominal.")

# ===========================================================================
# 4. ATELIERS (fin de liste ATELIERS, après at167)
# ===========================================================================
ATELIERS_NOUVEAUX = [
    {
        "id": "at168",
        "chapitre": "Bloc 6",
        "titre": "Convoyeur : le point de fonctionnement d'un moteur asynchrone",
        "theme": "Motorisation",
        "fiche": "6.20",
        "figure": "point_fonctionnement",
        "vocabulaire": [
            ("Vitesse de synchronisme ns",
             "la vitesse du champ tournant, ns = 60 f / p : le moteur asynchrone tourne toujours un peu "
             "en dessous."),
            ("Point de fonctionnement",
             "l'intersection de la courbe du moteur et de celle de la charge : la vitesse où les deux couples "
             "s'égalent."),
            ("Couple nominal Cn",
             "le couple que le moteur peut fournir en permanence sans chauffer au-delà de sa classe."),
        ],
        "enonce": "Plaque du moteur (données d'énoncé) : 4 kW, 1 440 tr/min, 4 pôles, 50 Hz. Le convoyeur demande, "
                  "ramené à l'arbre moteur, un couple constant de 22 N·m. Partie utile de la courbe du moteur : "
                  "droite passant par (ns ; 0) et (1 440 ; Cn), soit C(n) = Cn × (ns − n) / (ns − 1 440).",
        "etapes": [
            {"type": "numerique", "label": "Vitesse de synchronisme",
             "unite": "tr/min", "attendu": 1500, "tol": 0.5,
             "consigne": "Calcule ns = 60 f / p.",
             "indice": "4 pôles, c'est 2 paires de pôles.",
             "pieges": [(750, "750 tr/min : tu as pris p = 4. Un moteur 4 pôles a 2 PAIRES de pôles : p = 2."),
                        (3000, "3 000 tr/min, c'est un moteur 2 pôles (p = 1). Ici, p = 2.")],
             "aide": "ns = 60 × 50 / 2 = 1 500 tr/min."},
            {"type": "numerique", "label": "Couple nominal",
             "unite": "N·m", "attendu": 26.53, "tol": 0.1,
             "consigne": "Calcule Cn = Pn / ωn.",
             "indice": "ωn = 2π × 1 440 / 60, en rad/s.",
             "pieges": [(2.78, "2,78 : tu as divisé 4 000 par 1 440 sans convertir en rad/s. Il manque 2π/60.")],
             "aide": "ωn = 150,8 rad/s ; Cn = 4 000 / 150,8 ≈ 26,5 N·m."},
            {"type": "numerique", "label": "Vitesse au point de fonctionnement",
             "unite": "tr/min", "attendu": 1450.24, "tol": 1.0,
             "consigne": "Résous Cn × (1 500 − n) / (1 500 − 1 440) = 22.",
             "indice": "1 500 − n = 22 × 60 / Cn.",
             "pieges": [(1440, "1 440 tr/min, c'est la vitesse nominale, pour un couple de 26,5 N·m. Ici la "
                               "charge demande moins (22 N·m) : le moteur tourne un peu plus vite.")],
             "aide": "1 500 − n = 22 × 60 / 26,53 ≈ 49,8 → n ≈ 1 450 tr/min."},
            {"type": "numerique", "label": "Puissance utile au point",
             "unite": "W", "attendu": 3341.1, "tol": 8,
             "consigne": "Calcule P = C × ω au point de fonctionnement.",
             "indice": "ω = 2π × 1 450,2 / 60.",
             "pieges": [(4000, "4 000 W, c'est la puissance nominale. Au point de fonctionnement, le couple vaut 22 N·m, "
                               "pas Cn : la puissance est plus faible.")],
             "aide": "ω ≈ 151,9 rad/s ; P ≈ 22 × 151,9 ≈ 3 341 W."},
            {"type": "qcm", "label": "Surcharge ?",
             "question": "Le moteur est-il bien dimensionné pour ce convoyeur, en régime établi ?",
             "options": ["Non : il tourne moins vite que ns, il est donc surchargé",
                         "Non : sa puissance utile n'atteint pas 4 kW, il est trop petit",
                         "Oui : 22 N·m est sous Cn = 26,5 N·m ; il reste à vérifier le démarrage"], "bonne": 2,
             "indice": "Comparer le couple au point de fonctionnement au couple nominal.",
             "diagnostics": {0: "Un asynchrone tourne TOUJOURS sous ns, même bien chargé : c'est son principe. "
                                 "La surcharge se juge sur le couple, comparé à Cn.",
                             1: "Un moteur ne doit pas forcément fournir sa puissance nominale : il fournit ce que "
                                "la charge demande. Être un peu sous le nominal est sain."}},
        ],
        "corrige": {
            "enonce": "Moteur 4 kW, 1 440 tr/min, 4 pôles, 50 Hz ; charge constante de 22 N·m ramenée à l'arbre.",
            "regle": "**ns = 60 f / p** ; **Cn = Pn / ωn** ; point : **Cn × (ns − n) / (ns − nn) = C charge** ; "
                    "**P = C × ω**.",
            "conversions": "4 pôles → p = 2 ; ω = 2πN/60.",
            "remplacement": "ns = 60 × 50 / 2 ; Cn = 4 000 / (2π × 1 440 / 60) ; 26,53 × (1 500 − n) / (1 500 − 1 440) = 22.",
            "calcul": "**ns = 1 500 tr/min** ; **Cn ≈ 26,5 N·m** ; **n ≈ 1 450 tr/min** ; **P ≈ 3 341 W** ; sous "
                     "le nominal.",
            "verification": "Le point est entre ns (1 500) et nn (1 440), plus près de ns puisque 22 N·m est "
                            "sous Cn : cohérent avec un moteur moins chargé que nominal.",
        },
        "a_retenir": "À retenir : la vitesse d'un asynchrone se lit à l'intersection de sa courbe et de "
                     "celle de la charge ; le couple au point doit rester sous Cn.",
    },
    {
        "id": "at169",
        "chapitre": "Bloc 6",
        "titre": "Transmission hydrostatique : où part la puissance ?",
        "theme": "Motorisation",
        "fiche": "6.20",
        "figure": "pompe_moteur_hydraulique",
        "vocabulaire": [
            ("Cylindrée",
             "le volume d'huile déplacé par tour, en cm³/tr : elle relie le débit à la vitesse."),
            ("Rendement volumétrique ηv",
             "la part du débit théorique qui sort vraiment : le reste fuit à l'intérieur de la machine."),
            ("Rendement hydromécanique ηm",
             "la part du couple qui n'est pas perdue en frottements et pertes internes. Règle : ce que la "
             "machine donne × η, ce qu'elle demande ÷ η."),
        ],
        "enonce": "Données d'énoncé : une pompe de 16 cm³/tr est entraînée à 1 450 tr/min (ηv = 0,95 ; ηm = 0,90). "
                  "Elle alimente sous 150 bar un moteur hydraulique de 50 cm³/tr (ηv = 0,95 ; ηm = 0,90). Pertes "
                  "dans les conduites négligées.",
        "etapes": [
            {"type": "numerique", "label": "Débit de la pompe",
             "unite": "L/min", "attendu": 22.04, "tol": 0.1,
             "consigne": "Calcule Qv = Cyl × N × ηv, en L/min.",
             "indice": "16 × 1 450 × 0,95 en cm³/min, puis ÷ 1 000.",
             "pieges": [(23.2, "23,2 L/min, c'est le débit théorique : tu as oublié les fuites internes (× ηv)."),
                        (24.42, "24,4 : tu as divisé par ηv au lieu de multiplier. Les fuites RÉDUISENT le débit.")],
             "aide": "16 × 1 450 × 0,95 = 22 040 cm³/min ≈ 22,0 L/min."},
            {"type": "numerique", "label": "Puissance hydraulique",
             "unite": "W", "attendu": 5510, "tol": 15,
             "consigne": "Calcule P = p × Qv, en watts (p en Pa, Qv en m³/s).",
             "indice": "150 bar = 150 × 10⁵ Pa ; 22,04 L/min = 22,04 × 10⁻³ / 60 m³/s.",
             "pieges": [(3306, "3 306 : tu as multiplié 150 par 22,04 sans convertir. Il faut des Pa et des m³/s.")],
             "aide": "15 × 10⁶ × 3,673 × 10⁻⁴ ≈ 5 510 W."},
            {"type": "numerique", "label": "Couple absorbé par la pompe",
             "unite": "N·m", "attendu": 42.44, "tol": 0.2,
             "consigne": "Calcule le couple que le moteur électrique doit fournir à la pompe : C = p × Cyl / (2π × ηm).",
             "indice": "La pompe DEMANDE du couple : les frottements l'augmentent, on divise par ηm.",
             "pieges": [(34.38, "34,4 : tu as multiplié par ηm. La pompe REÇOIT le couple : les frottements en "
                                "demandent plus, on divise."),
                        (38.2, "38,2, c'est le couple de la pompe idéale, sans frottements.")],
             "aide": "15 × 10⁶ × 16 × 10⁻⁶ / (2π × 0,90) ≈ 42,4 N·m ; × 151,8 rad/s ≈ 6 440 W absorbés."},
            {"type": "numerique", "label": "Vitesse du moteur hydraulique",
             "unite": "tr/min", "attendu": 418.76, "tol": 1.5,
             "consigne": "Calcule N = Qv × ηv / Cyl pour le moteur hydraulique.",
             "indice": "Qv en cm³/min (22 040), Cyl = 50 cm³/tr.",
             "pieges": [(440.8, "440,8 : tu as oublié un des deux rendements volumétriques (celui de la pompe ou "
                                "celui du moteur) : il faut 16 × 1 450 × 0,95 × 0,95 / 50.")],
             "aide": "22 040 × 0,95 / 50 ≈ 418,8 tr/min."},
            {"type": "numerique", "label": "Couple du moteur hydraulique",
             "unite": "N·m", "attendu": 107.43, "tol": 0.5,
             "consigne": "Calcule C = p × Cyl × ηm / (2π).",
             "indice": "p = 15 × 10⁶ Pa ; Cyl = 50 × 10⁻⁶ m³/tr.",
             "pieges": [(132.63, "132,6 : tu as divisé par ηm. Pour un MOTEUR, les frottements réduisent le couple "
                                 "de sortie : on multiplie.")],
             "aide": "15 × 10⁶ × 50 × 10⁻⁶ × 0,90 / (2π) ≈ 107,4 N·m."},
            {"type": "qcm", "label": "Où part la puissance ?",
             "question": "La puissance de sortie vaut environ 4 710 W (107,4 N·m × 43,85 rad/s), pour 6 440 W "
                         "absorbés par la pompe (42,4 N·m × 151,8 rad/s). Que devient la différence ?",
             "options": ["Elle est stockée dans l'huile sous pression",
                         "Elle se transforme en chaleur : fuites et frottements dans la pompe et le moteur",
                         "Elle est rendue au réseau électrique"], "bonne": 1,
             "indice": "η global = 0,95 × 0,90 × 0,95 × 0,90.",
             "diagnostics": {0: "En régime établi, la pression ne stocke rien : elle porte la puissance d'un bout à "
                                 "l'autre. Ce qui manque est perdu.",
                             2: "Rien ne revient au réseau : les pertes (fuites, frottements) chauffent l'huile — "
                                "c'est pour cela qu'une centrale hydraulique a souvent un refroidisseur."}},
        ],
        "corrige": {
            "enonce": "Pompe 16 cm³/tr à 1 450 tr/min, moteur hydraulique 50 cm³/tr, 150 bar, ηv = 0,95 et ηm = 0,90 "
                      "pour chacun.",
            "regle": "**Pompe : Qv = Cyl × N × ηv**, **C = p Cyl / (2π ηm)** ; **P = p × Qv** ; **moteur : N = Qv ηv / "
                    "Cyl**, **C = p Cyl ηm / (2π)** — ce que la machine donne × η, ce qu'elle demande ÷ η.",
            "conversions": "1 bar = 10⁵ Pa ; 1 L/min = 10⁻³ / 60 m³/s ; 1 cm³ = 10⁻⁶ m³.",
            "remplacement": "Qv = 16 × 1 450 × 0,95 ; P = 15 × 10⁶ × 22,04 × 10⁻³ / 60 ; N = 22 040 × 0,95 / 50 ; "
                            "C = 15 × 10⁶ × 50 × 10⁻⁶ × 0,90 / (2π).",
            "calcul": "**Qv ≈ 22,0 L/min** ; **P hydraulique ≈ 5 510 W** ; **C pompe ≈ 42,4 N·m** (6 440 W absorbés) ; "
                     "**N ≈ 419 tr/min** ; **C ≈ 107,4 N·m** ; P sortie ≈ 107,4 × 43,85 ≈ 4 710 W.",
            "verification": "η global = 4 710 / 6 440 ≈ 0,73 = 0,95 × 0,90 × 0,95 × 0,90 : les rendements se "
                            "multiplient, deux conversions coûtent deux fois.",
        },
        "a_retenir": "À retenir : la cylindrée relie débit et vitesse ; dans une transmission hydrostatique, "
                     "les rendements des deux machines se multiplient, et les pertes chauffent l'huile.",
    },
]

# ===========================================================================
# 5. GÉNÉRATEURS (nouvelle famille « Motorisation »)
# ===========================================================================
GENERATEUR = '''
def gen_point_fonctionnement():
    """Vitesse au point de fonctionnement d'un asynchrone (droite utile) avec une charge à couple constant."""
    # (pôles, ns à 50 Hz, vitesses nominales d'énoncé)
    poles, ns, nns = random.choice([(2, 3000, (2850, 2880, 2900)), (4, 1500, (1420, 1440, 1460)),
                                    (6, 1000, (940, 950, 960))])
    nn = random.choice(nns)
    Pn = random.choice([1500, 2200, 3000, 4000, 5500, 7500])
    Cn = Pn / (2 * math.pi * nn / 60)
    Cr = round(Cn * random.choice([0.5, 0.6, 0.7, 0.8, 0.9]), 1)
    n = ns - (ns - nn) * Cr / Cn
    diag = []
    for val, msg in (
            (nn, "C'est la vitesse nominale, pour le couple nominal. La charge demande ici un autre couple : "
                 "le moteur tourne à une autre vitesse."),
            (ns, "C'est la vitesse de synchronisme : le moteur ne l'atteint jamais en charge."),
            (ns - (ns - nn) * Cn / Cr, "Tu as inversé le rapport : c'est (ns − nn) × C charge / Cn qu'on retire à ns."),
    ):
        if abs(val - n) > 1.0 and all(abs(val - d["v"]) > 1.0 for d in diag):
            diag.append(_diag(round(val, 1), msg))
    return {
        "titre": "Motorisation — point de fonctionnement",
        "enonce": (f"Un moteur asynchrone porte sur sa plaque : **{fr(Pn / 1000, 1)} kW, {nn} tr/min, {poles} pôles, "
                   f"50 Hz**. Il entraîne une charge à **couple constant de {fr(Cr, 1)} N·m** (ramené à son arbre). "
                   "En modélisant sa partie utile par une droite passant par (ns ; 0) et (nn ; Cn), à quelle vitesse "
                   "tourne-t-il, en tr/min ?"),
        "rep": round(n, 1), "tol": 1.0, "unite": "tr/min",
        "diag": diag,
        "corr": [
            f"**Ce que dit l'énoncé.** Moteur {poles} pôles (p = {poles // 2}), {fr(Pn / 1000, 1)} kW à {nn} tr/min ; "
            f"charge constante de {fr(Cr, 1)} N·m.",
            f"**Vitesse de synchronisme.** ns = 60 × 50 / {poles // 2} = {ns} tr/min.",
            f"**Couple nominal.** Cn = {Pn} / (2π × {nn} / 60) = {fr(Cn, 2)} N·m.",
            f"**Point de fonctionnement.** {fr(Cn, 2)} × ({ns} − n) / {ns - nn} = {fr(Cr, 1)} → "
            f"n = {ns} − {ns - nn} × {fr(Cr, 1)} / {fr(Cn, 2)} = {fr(n, 1)} tr/min.",
            f"**Je vérifie.** n est entre nn ({nn}) et ns ({ns}), puisque la charge ({fr(Cr, 1)} N·m) est sous Cn.",
        ],
        "indice": "ns = 60 f / p ; Cn = Pn / ωn ; puis Cn × (ns − n) / (ns − nn) = C charge.",
    }


def gen_pompe_hydraulique():
    """Débit d'une pompe hydraulique volumétrique."""
    cyl = random.choice([4, 6.3, 8, 10, 12.5, 16, 20, 25, 32])
    N = random.choice([960, 1450, 1500, 2900])
    ev = random.choice([0.90, 0.92, 0.94, 0.95, 0.96])
    Q = cyl * N * ev / 1000
    diag = []
    for val, msg in (
            (cyl * N / 1000, "C'est le débit théorique : il manque le rendement volumétrique (les fuites internes "
                             "réduisent le débit)."),
            (cyl * N / ev / 1000, "Tu as divisé par ηv : les fuites RÉDUISENT le débit, on multiplie."),
            (cyl * N * ev, "Ton résultat est en cm³/min : divise par 1 000 pour des litres."),
    ):
        if abs(val - Q) > 0.12 and all(abs(val - d["v"]) > 0.05 for d in diag):
            diag.append(_diag(round(val, 3), msg))
    return {
        "titre": "Motorisation — débit d'une pompe hydraulique",
        "enonce": (f"Une pompe hydraulique de cylindrée **{fr(cyl, 1)} cm³/tr** est entraînée à **{N} tr/min**. Son "
                   f"rendement volumétrique vaut **{fr(ev, 2)}** (donnée d'énoncé). Quel débit fournit-elle, en L/min ?"),
        "rep": round(Q, 3), "tol": 0.1, "unite": "L/min",
        "diag": diag,
        "corr": [
            f"**Ce que dit l'énoncé.** Cylindrée {fr(cyl, 1)} cm³/tr, vitesse {N} tr/min, ηv = {fr(ev, 2)}.",
            f"**Débit théorique.** Cyl × N = {fr(cyl, 1)} × {N} = {fr(cyl * N, 0)} cm³/min.",
            f"**Les fuites.** × ηv : {fr(cyl * N, 0)} × {fr(ev, 2)} = {fr(cyl * N * ev, 0)} cm³/min.",
            f"**En litres.** ÷ 1 000 : Qv = {fr(Q, 2)} L/min.",
            "**Je vérifie.** Le débit réel est un peu plus faible que le débit théorique : c'est le sens des fuites.",
        ],
        "indice": "Qv = Cyl × N × ηv ; 1 L = 1 000 cm³.",
    }
'''

# ===========================================================================
# 6. QUIZ — nouvelle catégorie « Chaîne d'énergie et motorisation »
#    positions de la bonne réponse : 0, 2, 1, 3, 2, 0, 3, 1
# ===========================================================================
QUIZ_ENERGIE = [
    ("Dans P = p × Qv, quelles unités faut-il utiliser pour obtenir des watts ?",
     ["p en pascals et Qv en m³/s", "p en bars et Qv en L/min", "p en MPa et Qv en L/s", "p en bars et Qv en m³/h"], 0,
     "Pa × m³/s = (N/m²) × (m³/s) = N·m/s = W. Avec des bars et des L/min, il faut convertir : 1 bar = 10⁵ Pa, "
     "1 L/min = 10⁻³ / 60 m³/s.", "Base"),
    ("Quelle grandeur joue, en hydraulique, le rôle que joue le courant I en électricité ?",
     ["La pression p", "La cylindrée", "Le débit Qv", "La viscosité de l'huile"], 2,
     "Effort × flux : la pression est l'effort (comme la tension U), le débit est le flux (comme le courant I). "
     "P = p × Qv comme P = U × I.", "Base"),
    ("Un moteur asynchrone 6 pôles est alimenté en 50 Hz. Quelle est sa vitesse de synchronisme ?",
     ["3 000 tr/min", "1 000 tr/min", "1 500 tr/min", "500 tr/min"], 1,
     "6 pôles = 3 paires : ns = 60 × 50 / 3 = 1 000 tr/min. 500 tr/min reviendrait à prendre p = 6 pôles au lieu "
     "de 3 paires.", "Calcul"),
    ("Pour quel type de charge un variateur de vitesse fait-il gagner le plus d'énergie ?",
     ["Un levage (couple constant)", "Une enrouleuse (puissance constante)", "Un convoyeur chargé (couple constant)",
      "Un ventilateur (couple quadratique)"], 3,
     "Couple en n² donc puissance en n³ : à 80 % de la vitesse, un ventilateur ne demande qu'environ la moitié de "
     "sa puissance (0,8³ ≈ 0,51).", "Intermédiaire"),
    ("Qu'est-ce que le point de fonctionnement d'un moteur entraînant une charge ?",
     ["Le point indiqué sur la plaque du moteur", "La vitesse de synchronisme",
      "L'intersection de la courbe couple-vitesse du moteur et de celle de la charge", "Le couple de démarrage"], 2,
     "La vitesse se stabilise là où le couple moteur égale le couple résistant : au-dessus, le moteur ralentit ; "
     "en dessous, il accélère. La plaque donne le point nominal, pas le point réel.", "Base"),
    ("Un volant de 0,5 kg·m² passe de 0 à 1 500 tr/min. Quelle énergie cinétique a-t-il reçue ?",
     ["Environ 6 170 J", "Environ 375 J", "Environ 563 000 J", "Environ 39 J"], 0,
     "ω = 2π × 1 500 / 60 ≈ 157,1 rad/s ; Ec = ½ × 0,5 × 157,1² ≈ 6 170 J. 563 000 J vient de N en tr/min au lieu "
     "de ω en rad/s.", "Calcul"),
    ("Que garantit la classe IE3 d'un moteur asynchrone (IEC 60034-30-1) ?",
     ["Un rendement constant quelle que soit la charge", "Une puissance minimale garantie",
      "Une vitesse de rotation fixe", "Un rendement minimal à pleine charge, fonction de la puissance et du nombre de pôles"], 3,
     "Les classes IE fixent un rendement minimal à pleine charge. À faible charge, le rendement réel baisse : "
     "d'où l'intérêt de dimensionner juste.", "Intermédiaire"),
    ("Une pompe et un moteur hydrauliques ont chacun un rendement de 0,85. Quel est le rendement de la "
     "transmission hydrostatique (conduites négligées) ?",
     ["0,85", "Environ 0,72", "0,70", "1,70"], 1,
     "Les rendements se multiplient : 0,85 × 0,85 ≈ 0,72. Additionner (1,70) n'a pas de sens ; 0,70 viendrait "
     "de 1 − 0,15 − 0,15.", "Piège"),
]
