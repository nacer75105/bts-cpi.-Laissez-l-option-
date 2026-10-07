# -*- coding: utf-8 -*-
# BROUILLON — fiche 3.5 « Essais mécaniques et compléments : fatigue, résilience, flexion, céramiques,
# traitements mécaniques de surface, coûts » (référentiel S4.1 et S4.2). Rien de ceci n'est encore dans app.py.
#
# Sources des valeurs utilisées :
# - Re, Rm, ρ : table MATERIAUX de l'application (S235, S355, EN AW-6082 T6, 42CrMo4 trempé revenu) ;
# - essai Charpy : ISO 148-1 (vérifiée : iso.org, BSI) ; qualités JR, J0, J2 d'EN 10025-2 (extrait officiel :
#   les qualités « diffèrent par leur énergie de rupture », exemple J0 = 27 J à 0 °C ; JR à +20 °C et J2 à −20 °C,
#   déjà en fiche 3.2) ;
# - g = 9,81 m/s² ;
# - limites d'endurance, coefficients Kt, prix au kilo, dimensions, efforts : DONNÉES D'ÉNONCÉ ;
# - aucun gain chiffré de traitement (grenaillage, galetage) : le gain se mesure par essai sur la pièce.
import math

# ===========================================================================
# 1. FIGURES
# ===========================================================================

def wohler():
    p = [_k_defs(), _txt(30, 24, "Courbe de Wöhler : plus l'amplitude est faible, plus la pièce tient de cycles", 13, TRAIT, "start", True)]
    ox, oy, L, H = 80, 270, 440, 210
    p.append(_k_fl(ox, oy, ox + L + 10, oy, TRAIT, "kk", 1.4))
    p.append(_k_fl(ox, oy, ox, oy - H - 10, TRAIT, "kk", 1.4))
    p.append(_txt(ox + L, oy + 30, "nombre de cycles à rupture N (échelle logarithmique)", 10, TRAIT, "end"))
    p.append(_txt(ox - 6, oy - H - 14, "amplitude de contrainte σa", 10, TRAIT, "start"))
    for k, lab in enumerate(("10³", "10⁴", "10⁵", "10⁶", "10⁷", "10⁸")):
        x = ox + 30 + k * 80
        p.append(f"<line x1='{x}' y1='{oy}' x2='{x}' y2='{oy + 4}' stroke='{TRAIT}'/>")
        p.append(_txt(x, oy + 16, lab, 9, FIN, "middle"))
    # acier : décroissance puis palier
    pts_a = [(ox + 30, oy - 190), (ox + 110, oy - 160), (ox + 190, oy - 125), (ox + 270, oy - 95), (ox + 320, oy - 82)]
    pts_a += [(ox + 350, oy - 80), (ox + 470, oy - 80)]
    p.append("<polyline points='" + " ".join(f"{x},{y}" for x, y in pts_a) + f"' fill='none' stroke='{ALESAGE}' stroke-width='3'/>")
    p.append(_txt(ox + 470, oy - 88, "acier : palier", 10, ALESAGE, "end", True))
    p.append(f"<line x1='{ox}' y1='{oy - 80}' x2='{ox + 350}' y2='{oy - 80}' stroke='{ALESAGE}' stroke-dasharray='4 4'/>")
    p.append(_txt(ox - 6, oy - 76, "σD", 12, ALESAGE, "end", True))
    # aluminium : pas de palier
    pts_b = [(ox + 30, oy - 150), (ox + 110, oy - 120), (ox + 190, oy - 92), (ox + 270, oy - 68), (ox + 350, oy - 50), (ox + 470, oy - 30)]
    p.append("<polyline points='" + " ".join(f"{x},{y}" for x, y in pts_b) + f"' fill='none' stroke='{ARBRE}' stroke-width='3' stroke-dasharray='8 4'/>")
    p.append(_txt(ox + 470, oy - 16, "alliage d'aluminium : pas de palier", 10, ARBRE, "end", True))
    # zones
    p.append(f"<line x1='{ox}' y1='{oy - 200}' x2='{ox + 470}' y2='{oy - 200}' stroke='{ALERTE}' stroke-dasharray='6 4'/>")
    p.append(_txt(ox + 470, oy - 204, "Re (traction) : toute la courbe reste en dessous", 9, ALERTE, "end", True))
    p.append(_txt(ox + 70, oy - H + 22, "peu de cycles", 9, FIN, "middle"))
    p.append(_txt(ox + 230, oy - H + 22, "endurance limitée", 9, FIN, "middle"))
    p.append(_txt(ox + 410, oy - H + 22, "endurance illimitée (acier)", 9, FIN, "middle"))
    p.append(f"<circle cx='{ox + 190}' cy='{oy - 125}' r='6' fill='{ALERTE}'><animate attributeName='r' values='5;8;5' dur='1.6s' repeatCount='indefinite'/></circle>")
    p.append(_txt(ox + 200, oy - 132, "une éprouvette rompue", 9, ALERTE, "start"))
    x0 = 560
    p.append(f"<rect x='{x0}' y='44' width='210' height='240' rx='6' fill='#ffffff' stroke='{FIN}'/>")
    for i, (t, c, g) in enumerate((("Chaque point : une éprouvette", TRAIT, True), ("sollicitée à σa jusqu'à rupture.", TRAIT, False),
                                   ("", TRAIT, False), ("Sous σD (acier) : la pièce", ALESAGE, True), ("tient indéfiniment.", ALESAGE, True),
                                   ("", TRAIT, False), ("Aluminium : pas de palier,", ARBRE, True), ("on choisit une durée de", ARBRE, False),
                                   ("vie visée et on lit σa.", ARBRE, False), ("", TRAIT, False),
                                   ("Courbes schématiques :", FIN, False), ("les valeurs viennent des essais.", FIN, False))):
        if t:
            p.append(_txt(x0 + 10, 66 + 18 * i, t, 11, c, "start", g))
    p.append(f"<rect x='30' y='310' width='740' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 332, "La fatigue casse des pièces sous des contraintes bien inférieures à Re, après un grand nombre de cycles.", 12, TRAIT, "start", True))
    return _svg("".join(p), 800, 356)


def fatigue_entaille():
    p = [_k_defs(), _txt(30, 24, "Une rupture de fatigue : amorçage à une entaille, propagation lente, rupture finale brutale", 13, TRAIT, "start", True)]
    # arbre avec gorge et pic de contrainte
    p.append(f"<rect x='40' y='90' width='170' height='80' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<rect x='210' y='100' width='14' height='60' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<rect x='224' y='90' width='160' height='80' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(_txt(217, 86, "gorge (petit rayon)", 10, ALERTE, "middle", True))
    p.append(_txt(120, 190, "arbre en flexion rotative (il tourne, chargé : chaque fibre passe", 9, TRAIT, "start"))
    p.append(_txt(120, 202, "de la traction à la compression à chaque tour)", 9, TRAIT, "start"))
    # répartition de contrainte au fond de gorge
    pts = [(40, 72), (150, 72), (195, 68), (210, 52), (217, 42), (224, 52), (240, 68), (290, 72), (384, 72)]
    p.append("<polyline points='" + " ".join(f"{x},{y}" for x, y in pts) + f"' fill='none' stroke='{ALERTE}' stroke-width='2.4'/>")
    p.append(_txt(390, 74, "σ nominale", 10, ALERTE, "start"))
    p.append(_txt(40, 64, "contrainte en surface, le long de l'arbre", 9, ALERTE, "start"))
    p.append(_txt(230, 46, "σmax = Kt × σnom", 10, ALERTE, "start", True))
    # faciès de rupture
    cx, cy, r = 600, 135, 75
    p.append(f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='#cbd5e1' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<path d='M {cx - r} {cy} A {r} {r} 0 0 1 {cx + r * 0.2:.0f} {cy - r * 0.98:.0f} L {cx + 10} {cy + 20} Z' fill='#e2e8f0' stroke='none'/>")
    for k in range(1, 5):
        rr = 14 * k
        p.append(f"<path d='M {cx - r + 2} {cy - rr} A {rr * 1.6} {rr * 1.6} 0 0 1 {cx - r + rr * 1.3:.0f} {cy + rr * 0.6:.0f}' fill='none' stroke='{FIN}' stroke-width='1.2'/>")
    p.append(f"<circle cx='{cx - r + 3}' cy='{cy - 4}' r='5' fill='{ALERTE}'><animate attributeName='r' values='4;7;4' dur='1.6s' repeatCount='indefinite'/></circle>")
    p.append(_txt(cx - r - 8, cy - 8, "amorçage", 10, ALERTE, "end", True))
    p.append(_txt(cx - 40, cy + 92, "zone lisse : propagation", 10, FIN, "middle"))
    p.append(_txt(cx - 40, cy + 104, "(lignes d'arrêt)", 10, FIN, "middle"))
    p.append(_txt(cx + 40, cy - 86, "zone rugueuse : rupture finale", 10, TRAIT, "middle", True))
    p.append(_txt(cx + 40, cy - 100, "cassure vue de face (coupe au fond de la gorge)", 9, FIN, "middle"))
    p.append(f"<rect x='30' y='250' width='740' height='52' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 272, "La fissure naît presque toujours en surface, là où la contrainte est la plus forte : entaille, gorge, rayure.", 12, TRAIT, "start", True))
    p.append(_txt(46, 292, "Faciès vu de face (à droite) : la zone lisse grandit cycle après cycle, puis ce qui reste casse d'un coup.", 11, FIN))
    return _svg("".join(p), 800, 316)


def essai_charpy():
    p = [_k_defs(), _txt(30, 24, "Essai Charpy : l'énergie absorbée par la rupture d'une éprouvette entaillée", 13, TRAIT, "start", True)]
    # pendule
    ax, ay, Lp = 160, 60, 150
    p.append(f"<circle cx='{ax}' cy='{ay}' r='5' fill='{TRAIT}'/>")
    p.append(f"<g><animateTransform attributeName='transform' type='rotate' values='70 {ax} {ay}; 0 {ax} {ay}; -45 {ax} {ay}; 70 {ax} {ay}' dur='4s' repeatCount='indefinite'/>"
             f"<line x1='{ax}' y1='{ay}' x2='{ax}' y2='{ay + Lp}' stroke='{TRAIT}' stroke-width='3'/>"
             f"<rect x='{ax - 22}' y='{ay + Lp - 8}' width='44' height='26' rx='4' fill='{ALESAGE}'/></g>")
    p.append(f"<rect x='{ax - 30}' y='{ay + Lp + 22}' width='60' height='10' fill='#cbd5e1' stroke='{TRAIT}'/>")
    p.append(_txt(ax, ay + Lp + 48, "éprouvette entaillée (V)", 10, TRAIT, "middle", True))
    p.append(f"<line x1='{ax - 150}' y1='{ay + Lp + 5}' x2='{ax + 140}' y2='{ay + Lp + 5}' stroke='{FIN}' stroke-dasharray='3 3'/>")
    p.append(_txt(ax - 150, ay + Lp - 1, "point le plus bas", 8, FIN, "start"))
    p.append(f"<line x1='{ax - 150}' y1='{ay + 55}' x2='{ax - 80}' y2='{ay + 55}' stroke='{ALESAGE}' stroke-dasharray='3 3'/>")
    p.append(_k_fl(ax - 140, ay + Lp + 3, ax - 140, ay + 58, ALESAGE, "kb", 1.4))
    p.append(_txt(ax - 136, ay + 100, "h0 (départ)", 10, ALESAGE, "start", True))
    p.append(f"<line x1='{ax + 70}' y1='{ay + 95}' x2='{ax + 140}' y2='{ay + 95}' stroke='{ALESAGE}' stroke-dasharray='3 3'/>")
    p.append(_k_fl(ax + 130, ay + Lp + 3, ax + 130, ay + 98, ALESAGE, "kb", 1.4))
    p.append(_txt(ax + 126, ay + 125, "h1", 10, ALESAGE, "end", True))
    p.append(_txt(ax + 126, ay + 137, "(remontée)", 9, ALESAGE, "end"))
    p.append(_txt(ax, ay + Lp + 66, "KV = m g (h0 − h1)", 12, OK, "middle", True))
    # courbe de transition
    ox, oy, L, H = 380, 250, 360, 180
    p.append(_k_fl(ox, oy, ox + L + 10, oy, TRAIT, "kk", 1.4))
    p.append(_k_fl(ox, oy, ox, oy - H - 10, TRAIT, "kk", 1.4))
    p.append(_txt(ox + L, oy + 18, "température d'essai :  ← plus froid · plus chaud →", 10, TRAIT, "end"))
    p.append(_txt(ox + 4, oy - H - 14, "énergie absorbée KV (J)", 10, TRAIT, "start"))
    pts = []
    for k in range(0, 61):
        u = k / 60
        y = 20 + 140 / (1 + math.exp(-(u - 0.5) * 12))
        pts.append(f"{ox + u * L:.1f},{oy - y:.1f}")
    p.append(f"<polyline points='{' '.join(pts)}' fill='none' stroke='{ARBRE}' stroke-width='3'/>")
    p.append(_txt(ox + 30, oy - 30, "fragile", 10, ALERTE, "start", True))
    p.append(_txt(ox + L - 10, oy - 170, "ductile", 10, OK, "end", True))
    p.append(_txt(ox + L / 2 + 8, oy - 92, "transition", 10, ARBRE, "start", True))
    p.append(f"<line x1='{ox}' y1='{oy - 40}' x2='{ox + L}' y2='{oy - 40}' stroke='{FIN}' stroke-dasharray='4 4'/>")
    p.append(_txt(ox + L, oy - 44, "27 J (niveau garanti par JR, J0, J2)", 9, FIN, "end"))
    p.append(f"<rect x='30' y='300' width='740' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 322, "Un acier de construction ductile à 20 °C peut devenir fragile au froid : on choisit sa qualité selon la température de service.", 11, TRAIT, "start", True))
    return _svg("".join(p), 800, 346)


def essai_flexion():
    p = [_k_defs(), _txt(30, 24, "Essai de flexion trois points : l'essai de référence des céramiques", 13, TRAIT, "start", True)]
    p.append(f"<rect x='90' y='120' width='340' height='30' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='2'/>")
    for x in (110, 410):
        p.append(f"<polygon points='{x},152 {x - 12},176 {x + 12},176' fill='{FIN}'/>")
    p.append(_k_fl(260, 60, 260, 116, ALERTE, "kr", 3))
    p.append(_txt(268, 76, "F", 13, ALERTE, "start", True))
    p.append(_k_fl(110, 196, 410, 196, FIN, "kk", 1.2))
    p.append(_txt(260, 212, "L (entre appuis)", 10, FIN, "middle"))
    p.append(_txt(440, 140, "b × h", 11, TRAIT, "start", True))
    p.append(_txt(260, 240, "face du dessous tendue : c'est là que l'éprouvette casse", 10, ALERTE, "middle", True))
    x0 = 470
    p.append(f"<rect x='{x0}' y='50' width='300' height='200' rx='6' fill='#ffffff' stroke='{FIN}'/>")
    for i, (t, c, g) in enumerate((("Section rectangulaire b × h :", TRAIT, True),
                                   ("σmax = 3 F L / (2 b h²)", OK, True), ("", TRAIT, False),
                                   ("Pour les céramiques : une", TRAIT, False),
                                   ("éprouvette de traction se", TRAIT, False),
                                   ("briserait dans les mors.", TRAIT, False), ("", TRAIT, False),
                                   ("La flèche mesurée donne aussi E.", FIN, False))):
        if t:
            p.append(_txt(x0 + 12, 74 + 22 * i, t, 12, c, "start", g))
    p.append(f"<rect x='30' y='262' width='740' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 284, "RDM de la flexion (fiche 4.3) : σ = Mf / (I/v), avec Mf = F L / 4 au milieu et I/v = b h² / 6.", 12, TRAIT))
    return _svg("".join(p), 800, 308)


def grenaillage():
    p = [_k_defs(), _txt(30, 24, "Grenaillage : des billes martèlent la surface et y laissent de la compression", 13, TRAIT, "start", True)]
    p.append(f"<rect x='40' y='170' width='420' height='110' fill='#cbd5e1' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<rect x='40' y='170' width='420' height='22' fill='#93c5fd' opacity='0.8'/>")
    p.append(_txt(250, 186, "couche comprimée", 10, ALESAGE, "middle", True))
    p.append(_txt(250, 236, "pièce (cœur)", 10, TRAIT, "middle"))
    for k in range(6):
        x = 70 + k * 70
        p.append(f"<circle cx='{x}' cy='60' r='9' fill='{FIN}'><animate attributeName='cy' values='60;160;60' dur='1.2s' begin='{k * 0.2:.1f}s' repeatCount='indefinite'/></circle>")
    p.append(_txt(250, 44, "billes projetées à grande vitesse", 10, FIN, "middle", True))
    # fissure qui doit s'ouvrir contre la compression
    p.append(f"<line x1='330' y1='170' x2='336' y2='200' stroke='{ALERTE}' stroke-width='2.4'/>")
    p.append(_k_fl(300, 182, 322, 182, ALESAGE, "kb", 2))
    p.append(_k_fl(370, 182, 348, 182, ALESAGE, "kb", 2))
    p.append(_txt(336, 162, "fissure refermée", 9, ALERTE, "middle", True))
    x0 = 490
    p.append(f"<rect x='{x0}' y='50' width='280' height='230' rx='6' fill='#ffffff' stroke='{FIN}'/>")
    for i, (t, c, g) in enumerate((("Ce qui se passe :", TRAIT, True),
                                   ("la surface, martelée, voudrait", TRAIT, False),
                                   ("s'étendre ; le cœur l'en empêche :", TRAIT, False),
                                   ("elle reste comprimée.", TRAIT, False), ("", TRAIT, False),
                                   ("Pourquoi ça aide en fatigue :", OK, True),
                                   ("une fissure doit s'ouvrir pour", OK, False),
                                   ("avancer ; la compression la", OK, False),
                                   ("tient fermée.", OK, False), ("", TRAIT, False),
                                   ("Ressorts, engrenages, bielles.", FIN, False))):
        if t:
            p.append(_txt(x0 + 12, 74 + 19 * i, t, 12, c, "start", g))
    p.append(f"<rect x='30' y='292' width='740' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 314, "Le gain dépend de la pièce et se mesure par essai. Un usinage APRÈS grenaillage enlève la couche utile.", 12, TRAIT))
    return _svg("".join(p), 800, 338)


# --- figure à curseurs : vérification en fatigue d'une gorge
def dyn_fatigue(sig=140.0, Kt=2.5):
    """Contrainte alternée nominale sig (MPa), coefficient Kt ; limite d'endurance de la pièce : 270 MPa (énoncé)."""
    sD = 270.0
    smax = Kt * sig
    ok = smax <= sD
    p = [_k_defs(), _txt(30, 24, f"σnom = {_fr_court(sig, 0)} MPa, Kt = {_fr_court(Kt, 1)} : σmax = {_fr_court(smax, 0)} MPa", 13, TRAIT, "start", True)]
    ox, oy, L, H = 80, 270, 400, 210
    p.append(_k_fl(ox, oy, ox + L + 10, oy, TRAIT, "kk", 1.4))
    p.append(_k_fl(ox, oy, ox, oy - H - 10, TRAIT, "kk", 1.4))
    p.append(_txt(ox + L, oy + 18, "nombre de cycles N (log)", 10, TRAIT, "end"))
    p.append(_txt(ox + 4, oy - H - 14, "σa (MPa)", 10, TRAIT, "start"))
    Y = lambda s: oy - min(s, 800) / 800 * H  # noqa: E731
    for s in (0, 200, 400, 600, 800):
        p.append(_txt(ox - 6, Y(s) + 3, str(s), 9, FIN, "end"))
    pts = [(ox + 20, Y(520)), (ox + 120, Y(430)), (ox + 220, Y(340)), (ox + 280, Y(sD)), (ox + L, Y(sD))]
    p.append("<polyline points='" + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f"' fill='none' stroke='{ALESAGE}' stroke-width='3'/>")
    p.append(_txt(ox + L - 4, Y(sD) - 6, "σD pièce = 270 MPa (énoncé)", 10, ALESAGE, "end", True))
    col = OK if ok else ALERTE
    p.append(f"<line x1='{ox}' y1='{Y(smax):.1f}' x2='{ox + L}' y2='{Y(smax):.1f}' stroke='{col}' stroke-width='2' stroke-dasharray='6 4'/>")
    p.append(_txt(ox + 8, Y(smax) - 6, f"σmax = {_fr_court(smax, 0)} MPa", 10, col, "start", True))
    x0 = 510
    p.append(f"<rect x='{x0}' y='44' width='260' height='240' rx='6' fill='#ffffff' stroke='{col}' stroke-width='1.8'/>")
    lignes = ((f"σmax = Kt × σnom = {_fr_court(Kt, 1)} × {_fr_court(sig, 0)}", TRAIT, False),
              (f"= {_fr_court(smax, 0)} MPa", col, True), ("", TRAIT, False),
              (("Sous σD : endurance illimitée." if ok else "Au-dessus de σD : durée limitée,"), col, True),
              (("" if ok else "la pièce cassera à terme."), col, True), ("", TRAIT, False),
              ("Leviers : agrandir le congé (Kt ↓),", FIN, False), ("réduire σnom (section ↑), soigner", FIN, False),
              ("la surface, grenailler.", FIN, False))
    for i, (t, c, g) in enumerate(lignes):
        if t:
            p.append(_txt(x0 + 12, 68 + 22 * i, t, 12, c, "start", g))
    p.append(_txt(30, 316, "Courbe schématique ; σD de la pièce (état de surface et taille compris) : donnée d'énoncé. On applique Kt tel quel : choix prudent.", 10, FIN))
    return _svg("".join(p), 790, 330)


FIGURES_NOUVELLES = {
    "wohler": ("Courbe de Wöhler et limite d'endurance", wohler),
    "fatigue_entaille": ("Rupture de fatigue : amorçage, propagation, rupture finale", fatigue_entaille),
    "essai_charpy": ("Essai Charpy et transition ductile-fragile", essai_charpy),
    "essai_flexion": ("Essai de flexion trois points", essai_flexion),
    "grenaillage": ("Grenaillage : contraintes résiduelles de compression", grenaillage),
}
DYN_NOUVELLE = {
    "fatigue_curseurs": (
        "Change la contrainte nominale et le coefficient de concentration : la pièce tient-elle en fatigue ?",
        dyn_fatigue,
        [{"nom": "sig", "label": "Contrainte alternée nominale σnom (MPa)", "min": 60.0, "max": 260.0, "defaut": 140.0, "pas": 10.0},
         {"nom": "Kt", "label": "Coefficient de concentration Kt", "min": 1.0, "max": 3.0, "defaut": 2.5, "pas": 0.1}]),
}

# ===========================================================================
# 2. FICHE 3.5 — en FIN de bloc 3 (après la 3.4)
# ===========================================================================

FICHE_3_5 = {
    "id": "3.5",
    "titre": "Essais et compléments : fatigue, résilience, flexion, céramiques, grenaillage, coûts",
    "duree": "5 h",
    "cours": """### 1. Pourquoi cette fiche

La fiche 3.1 a donné l'essai de traction, d'où viennent Re, Rm, E et A % ; la 3.2 la désignation (avec les
qualités de résilience JR, J0, J2) ; la 3.3 les traitements thermiques et de surface. Il manque ce qui fait
casser les pièces **en service** : la **fatigue** et la **rupture fragile**, et les essais qui les mesurent.
Une pièce correctement dimensionnée en statique (σ ≤ Re / s) peut casser après quelques mois de
fonctionnement, sous une charge **répétée** bien inférieure à Re : c'est la fatigue, l'une des toutes
premières causes de rupture des pièces mécaniques en service. Arbres de transmission, ressorts, bielles,
boulons de roue, cordons de soudure de châssis : quand une pièce mécanique casse en service, on pense d'abord
à la fatigue.

### 2. La fatigue : casser sous une charge trop faible pour casser

[[FIG:fatigue_entaille]]

Un arbre qui tourne en flexion voit chaque fibre passer de la traction à la compression **à chaque tour**.
Un ressort, une bielle, une dent d'engrenage subissent des millions de cycles.

**Pourquoi une charge trop faible pour casser finit par casser.** *Pliez un trombone dans un sens puis dans
l'autre : au bout de quelques allers-retours il casse, alors qu'un seul pliage ne l'aurait jamais cassé.* La
fatigue, c'est le même phénomène, en invisible. Re est une valeur moyenne sur toute la section ; au fond d'une
rayure ou d'une gorge, à l'échelle de quelques grains de métal, la contrainte locale est plus forte. Quelques
grains glissent d'un micron dans un sens, puis dans l'autre, à chaque cycle : un trombone miniature. Après des
milliers de cycles, ce va-et-vient ouvre une microfissure ; et une fissure est elle-même une entaille
extrêmement aiguë, au bout de laquelle la contrainte se concentre encore plus : elle avance un peu à chaque
cycle. La pièce ne s'use pas dans la masse : elle se fissure **à partir de sa surface**, pour trois raisons :
en flexion et en torsion, la contrainte est maximale en surface (RDM) ; c'est en surface que se trouvent les
rayures, les marques d'outil et les gorges ; un grain de surface n'est soutenu que d'un côté.

La pièce s'endommage donc progressivement, en trois temps :

1. **Amorçage** : une microfissure naît en surface, là où la contrainte est la plus forte (entaille, gorge,
   trou, rayure, défaut de soudure) ;
2. **Propagation** : à chaque cycle, la fissure avance un peu — la cassure garde une zone **lisse** avec des
   lignes d'arrêt, comme les cernes d'un arbre ;
3. **Rupture finale** : la section restante ne suffit plus, elle casse d'un coup (zone **rugueuse**).

*C'est pour cela qu'une rupture de fatigue est traîtresse : pas de déformation visible avant, la pièce casse
« sans prévenir », souvent bien après sa mise en service.*

### 3. La courbe de Wöhler et la limite d'endurance

[[FIG:wohler]]

**Amplitude, alternée.** Une fibre d'un arbre qui tourne en flexion passe de +120 MPa (traction) à −120 MPa
(compression), puis revient à +120 MPa, à chaque tour : c'est une contrainte **alternée**, et 120 MPa est son
**amplitude σa** (l'écart entre le milieu du cycle, ici 0, et le sommet).

**Pourquoi une échelle logarithmique.** Les durées de vie vont de mille à cent millions de cycles : sur une
règle normale, tout se tasserait à gauche. L'axe avance donc d'une graduation à chaque **× 10** (10³, 10⁴,
10⁵…). *Pour fixer les idées : un arbre à 3 000 tr/min fait 180 000 cycles par heure ; il atteint 10⁷ cycles
en environ 55 heures de marche. C'est pour cela qu'en mécanique on vise une durée « illimitée ».*

**L'essai de fatigue.** On sollicite des éprouvettes identiques avec une contrainte alternée d'amplitude σa,
et on compte le nombre de cycles N jusqu'à la rupture. Chaque éprouvette donne un point ; l'ensemble trace la
**courbe de Wöhler** (σa en fonction de N, N en échelle logarithmique).

- **Pour les aciers**, la courbe présente un **palier** : sous une amplitude σD, la **limite d'endurance**,
  l'éprouvette ne casse plus. En pratique, σD est définie pour un très grand nombre de cycles fixé par
  l'essai : en dessous, on considère la durée de vie comme **illimitée**. C'est l'objectif de
  dimensionnement.
- **Pour les alliages d'aluminium**, il n'y a pas de palier (fiche 3.1) : la courbe continue de descendre.
  C'est un constat d'essai : en aluminium, toute pièce cyclée a une durée de vie finie, et c'est le
  concepteur qui la choisit. On fixe une **durée de vie visée** (un nombre de cycles) et on lit la contrainte
  admissible correspondante sur la courbe du fournisseur.

**De l'éprouvette à la pièce.** σD est mesurée sur une petite éprouvette polie. Une vraie pièce tient moins :
son **état de surface** est moins bon (une rayure d'usinage est une minuscule gorge, un point de départ
possible pour la fissure ; une surface polie en a beaucoup moins), sa **taille** est plus grande (plus de
chances d'y trouver un défaut), et
ses **changements de forme** concentrent la contrainte. Les valeurs de σD et de ses corrections viennent des
essais ou des données du fournisseur : ici, elles seront toujours données dans l'énoncé.

### 4. Concentration de contrainte : le lien avec la forme

Au fond d'une gorge, d'un épaulement ou d'un trou, la contrainte locale dépasse la contrainte nominale
calculée en RDM. *Les « lignes d'effort » traversent la pièce comme l'eau d'une rivière : devant une pile de
pont, l'eau se resserre et accélère sur les bords. Au fond d'une gorge, les lignes d'effort se resserrent de la
même façon : plus l'angle est vif, plus le resserrement est brutal ; plus le congé est grand, plus le passage
est doux.*

> **σmax = Kt × σnom** — c'est le coefficient Kt de la fiche 4.1 (σ réelle = Kt × σ calculée), lu sur abaque
> selon la forme et le type de sollicitation. σnom se calcule comme en RDM : pour un arbre en flexion rotative,
> σnom = Mf / (I/v) (fiche 4.3). Attention : σmax désigne ici le **pic au fond de la gorge** ; c'est toujours
> une amplitude de cycle, qu'on peut placer sur la courbe de Wöhler.

**Pourquoi le pic compte en fatigue et pas en statique.** En statique, chargé une seule fois, le petit volume
au fond de la gorge dépasse Re, se déforme un peu, « cède » et reporte l'effort sur le métal voisin : la pièce
s'en accommode. En fatigue, ce même petit volume est sollicité dans un sens puis dans l'autre des millions de
fois : c'est lui qui joue le trombone. D'où la règle de vérification :

> **Kt × σnom ≤ σD de la pièce** (et σD / s si l'énoncé impose un coefficient de sécurité s)

*En fatigue, l'effet réel d'une entaille, mesuré par essai et noté Kf, est inférieur ou égal à Kt : appliquer
Kt tel quel va dans le sens de la sécurité.*

**Domaine de validité.** Cette règle vaut pour une contrainte **purement alternée**, de moyenne nulle : c'est le
cas de l'arbre en flexion rotative. Si la contrainte oscille autour d'une valeur non nulle (ressort préchargé,
vis serrée, bielle), l'amplitude admissible est plus faible ; la valeur à utiliser est alors donnée par
l'énoncé ou par le fournisseur.

*Exemple (données d'énoncé ; aucun coefficient de sécurité imposé, s = 1) : un arbre subit une contrainte
alternée nominale de 140 MPa au droit d'une gorge à petit rayon de fond (Kt = 2,5). La limite d'endurance de la
pièce, corrections comprises, vaut 270 MPa. σmax = 2,5 × 140 = **350 MPa** > 270 : **la pièce cassera en
fatigue**. Avec un congé plus grand (Kt = 1,8), σmax = **252 MPa** < 270 : elle tient — de justesse ; en bureau
d'études, une marge aussi faible serait le plus souvent refusée.*

[[DYN:fatigue_curseurs]]

**Les leviers du concepteur** : arrondir les angles (grand rayon de congé : Kt baisse), éloigner les
changements de section des zones très chargées, soigner l'état de surface, augmenter la section (σnom baisse),
et mettre la surface en **compression** (grenaillage, galetage, §8).

### 5. La résilience : l'essai Charpy

[[FIG:essai_charpy]]

La **résilience**, c'est l'aptitude d'un matériau à encaisser un choc sans se fendre ; on la mesure par
l'énergie qu'il « boit » en cassant.

**L'essai** (ISO 148-1) : un mouton-pendule lâché d'une hauteur h0 frappe une éprouvette entaillée en V et la
casse ; il remonte moins haut, à h1 (h0 et h1 : hauteurs du centre de gravité du mouton au départ et à la
remontée). L'énergie qu'il a perdue a été absorbée par la rupture. L'entaille et le choc placent l'éprouvette
dans le pire cas (un défaut et un chargement brutal) : si le métal encaisse ça, il encaissera une rayure et
un coup en service.

> **KV = m × g × (h0 − h1)** (en joules ; la norme corrige en plus les frottements)

*Autrefois, on divisait cette énergie par la section sous l'entaille (0,8 cm² pour l'éprouvette normale) :
c'était la KCV, en J/cm², qu'on trouve encore dans de vieux documents. La norme actuelle donne KV en joules ;
c'est aussi en joules que la désignation garantit ses 27 J.*

Une rupture **ductile** absorbe beaucoup d'énergie (le métal se déforme avant de céder) ; une rupture
**fragile** en absorbe très peu (elle casse net, comme du verre).

*Exemple (données d'énoncé) : mouton de 20 kg lâché de 1,5 m, qui remonte à 1,2 m. KV = 20 × 9,81 × 0,3 ≈
**58,9 J**.*

**La transition ductile-fragile.** Pour les aciers de construction, l'énergie absorbée chute quand la
température baisse : au-dessus de la **zone de transition**, rupture ductile ; en dessous, rupture fragile.
*Une barre de chocolat sortie du congélateur casse net avec un « clac », alors qu'à température ambiante elle
se tord avant de céder : certains aciers font pareil.* En simplifiant : pour se déformer, les plans d'atomes du
métal doivent glisser les uns sur les autres ; au froid, ce glissement devient plus difficile pour les aciers
de construction, et quand glisser « coûte » plus que se fendre, le métal se fend. Un acier parfaitement
correct en été peut casser net en hiver, au moindre choc — c'est ce qui est arrivé à des navires soudés
(fiche 3.1). Les aciers inoxydables austénitiques (304) et les alliages d'aluminium ne présentent pas de
transition marquée.

**Ce que garantit la désignation** (EN 10025-2, fiche 3.2) : les qualités JR, J0, J2 garantissent une énergie
minimale de **27 J** à une température d'essai donnée — **+20 °C** (JR), **0 °C** (J0), **−20 °C** (J2) ; la
norme prévoit aussi une qualité K2 pour certaines nuances. *Un garde-corps extérieur, une structure de levage
utilisée l'hiver : règle simple et prudente, on choisit la qualité dont la température d'essai couvre la
température de service la plus basse. Pour −10 °C, la désignation J0 ne garantit plus rien ; il faut J2.* (En
charpente, le choix réglementaire dépend aussi de l'épaisseur et du niveau de contrainte.)

**Et la dureté ?** C'est l'autre essai du programme, déjà cité en fiche 3.1 : on enfonce un pénétrateur très
dur (bille pour Brinell, HB ; pyramide de diamant pour Vickers, HV ; cône de diamant pour Rockwell C, HRC) et
on mesure l'empreinte (taille ou profondeur). Plus elle est petite, plus le matériau est dur. Essai rapide,
presque non destructif, il sert à contrôler un traitement thermique (« 58 HRC » sur un plan, fiche 3.3) ;
l'échelle se choisit selon la dureté et l'épaisseur de la pièce.

### 6. L'essai de flexion

[[FIG:essai_flexion]]

Pour les matériaux **très fragiles** comme les céramiques, l'essai de traction est délicat : pour tirer une
éprouvette, il faut la serrer dans des mors, et ce serrage crée des points d'appui très durs ; le moindre défaut
d'alignement ajoute une petite flexion parasite ; elle casse là, et on ne mesure rien d'utile. On la pose donc
simplement sur deux appuis et on charge au milieu (**flexion trois points**). L'essai de flexion sert aussi,
pour les plastiques et les composites, à caractériser un matériau qui travaillera en flexion.

La contrainte maximale, sur la face tendue, vaut (section rectangulaire b × h, portée L) :

> **σmax = 3 F L / (2 b h²)**

C'est la RDM de la flexion (fiche 4.3) : σ = Mf / (I/v), avec Mf = F L / 4 au milieu et I/v = b h² / 6 pour un
rectangle ; donc σmax = (F L / 4) × 6 / (b h²) = 3 F L / (2 b h²). La formule suppose le matériau élastique
jusqu'à la rupture, ce qui est le cas des céramiques ; cette « résistance à la flexion » n'est pas Rm : seule une
petite zone est très sollicitée, ce qui la rend en général plus élevée.

*Exemple (données d'énoncé) : éprouvette céramique de 4 × 3 mm (b × h), portée 30 mm, rompue sous 150 N :
σmax = 3 × 150 × 30 / (2 × 4 × 3²) = **187,5 MPa** : c'est sa résistance à la flexion.*

### 7. Les céramiques

*Vous connaissez déjà une céramique : le carrelage, ou une tasse. C'est dur (un couteau ne la raye pas), ça ne
rouille pas, ça va au four… mais ça se brise si ça tombe.* Les céramiques techniques — alumine, carbure de
silicium, nitrure de silicium, zircone — ont les mêmes qualités et le même défaut, en beaucoup plus
performant : **très dures**, **très rigides**, **réfractaires** (elles tiennent à haute température), souvent
**isolantes** et **chimiquement inertes** (pas de corrosion). Mais **fragiles** : aucune déformation plastique
avant rupture, une rupture brutale à partir du moindre défaut. Leur résistance est **dispersée** d'une pièce à
l'autre (elle dépend du plus gros défaut caché).

**Compression oui, traction non.** Une fissure doit s'ouvrir pour avancer : la traction l'ouvre, la compression
la referme. Un matériau sans plasticité, qui ne peut pas « émousser » ses fissures, doit donc travailler en
compression.

**Emplois** : plaquettes d'outils de coupe, billes de roulements hybrides (bagues en acier, billes en
céramique), garnitures d'étanchéité, isolateurs, revêtements anti-usure. **Règles de conception** : éviter la
traction, les chocs et les **chocs thermiques** (chauffage ou refroidissement brutal), éviter les angles vifs,
préférer des formes simples (le matériau s'obtient par frittage : on presse de la poudre dans un moule puis on
la cuit, comme une brique ; il est difficile à usiner ensuite).

### 8. Les traitements mécaniques de surface

[[FIG:grenaillage]]

- **Grenaillage** : projection de billes (acier, verre, céramique) à grande vitesse. Chaque bille agit comme un
  petit coup de marteau : elle écrase et étire le métal juste sous la surface, comme un chaudronnier qui martèle
  une tôle. Cette fine peau voudrait s'agrandir, mais elle est collée au cœur, qui n'a pas bougé : elle reste en
  **compression**, comme un tapis trop grand coincé entre quatre murs. Le cycle de contrainte en surface est
  décalé vers la compression : la partie « traction » du cycle, celle qui ouvre la fissure, diminue. **Usage** :
  ressorts, engrenages, bielles, arbres, cordons de soudure. **Défauts induits** : il augmente la rugosité et
  peut déformer une pièce mince (c'est même un procédé de mise en forme) : on masque les portées
  fonctionnelles.
- **Galetage** : un galet roule sous forte pression sur la surface (souvent un rayon de congé d'arbre) ; il
  écrase les aspérités et met la surface en compression. Il améliore à la fois l'état de surface et la tenue
  en fatigue.
- **Brunissage** : écrasement des crêtes de rugosité par un outil lisse : surtout une **finition** (état de
  surface, tenue à l'usure).
- **Sablage** : projection d'abrasif pour **nettoyer, décaper ou rendre rugueux** avant peinture ou collage :
  ce n'est **pas** un traitement anti-fatigue.

**Ce qu'il faut savoir pour concevoir** : le gain en fatigue dépend de la pièce et du réglage, et se
**mesure par essai** ; il ne se décrète pas. Les contraintes de compression sont **en surface** : un usinage
réalisé **après** les enlève ; un traitement thermique ou un soudage ultérieur peut les relâcher. Le
traitement se place donc **après les opérations d'usinage et de traitement thermique**, et s'écrit sur le
plan.

### 9. Comparer les coûts matière

Le prix d'un matériau se donne **au kilo** : comparer deux matériaux au kilo ne dit rien. Il faut comparer
le coût de **la pièce qui remplit la fonction**.

*Exemple (prix au kilo : données d'énoncé ; Re et ρ : table des matériaux) : un tirant de 1 m doit porter
50 kN en traction, avec un coefficient de sécurité de 2. Section : S = F × s / Re ; masse : ρ × S × L. Ligne
S235 détaillée : S = 50 000 × 2 / 235 ≈ 426 mm² = 426 × 10⁻⁶ m² ; masse = 7 850 × 426 × 10⁻⁶ × 1 ≈ 3,34 kg ;
coût = 3,34 × 1,2 ≈ 4,0 €.*

| Matériau | Re (MPa) | Section (mm²) | Masse (kg) | Prix (€/kg, énoncé) | Coût (€) |
|---|---|---|---|---|---|
| S235 | 235 | 426 | 3,34 | 1,2 | 4,0 |
| S355 | 355 | 282 | 2,21 | 1,4 | 3,1 |
| EN AW-6082 T6 | 260 | 385 | 1,04 | 4,5 | 4,7 |
| 42CrMo4 trempé revenu | 750 | 133 | 1,05 | 3,2 | 3,3 |

*Le S355, un peu plus cher au kilo que le S235, est le moins cher par pièce : il faut moins de matière. L'aluminium
est le plus léger mais le plus cher ; le 42CrMo4 est presque aussi léger que l'aluminium, pour un coût proche
du S355 — sans compter son traitement thermique. Ce tirant est chargé en statique : s'il était cyclé, il
faudrait refaire la comparaison avec σD, pas avec Re.* Le coût complet ajoute la mise en forme, les traitements et
l'assemblage (fiche 3.3 : un traitement thermique a un coût et peut déformer la pièce).

### 10. Les erreurs classiques

1. **Dimensionner une pièce cyclée avec Re seul** : c'est σD (de la pièce, pas de l'éprouvette) qui compte.
2. **Oublier Kt en fatigue** : le pic de contrainte au fond d'une gorge amorce la fissure.
3. **Croire qu'un alliage d'aluminium a une limite d'endurance** comme l'acier : sa courbe ne fait pas de palier.
4. **Choisir un acier JR pour une structure exposée au gel** : 27 J ne sont garantis qu'à +20 °C.
5. **Confondre sablage et grenaillage** : le sablage nettoie, il ne renforce pas.
6. **Usiner après grenaillage** : on enlève la couche comprimée.
7. **Comparer des prix au kilo** au lieu du coût de la pièce qui remplit la fonction.

### 11. À retenir

- **Fatigue** : rupture sous charge répétée, bien sous Re ; amorçage en surface, propagation, rupture finale.
- **Wöhler** : σa en fonction de N ; acier : palier **σD** (endurance illimitée) ; aluminium : pas de palier.
- **σmax = Kt × σnom ≤ σD de la pièce** (contrainte alternée) : la forme compte autant que le matériau.
- **Charpy** (ISO 148-1) : **KV = m g (h0 − h1)**, en joules ; transition ductile-fragile au froid ; JR, J0,
  J2 = 27 J à +20, 0, −20 °C. **Dureté** : empreinte d'un pénétrateur (HB, HV, HRC).
- **Flexion trois points** : **σmax = 3 F L / (2 b h²)**, pour les matériaux fragiles.
- **Céramiques** : dures, rigides, réfractaires, mais fragiles : compression oui, traction et chocs non.
- **Grenaillage, galetage** : compression en surface → meilleure tenue en fatigue ; en fin de gamme.
- **Coût** : comparer le coût de la pièce qui remplit la fonction, pas le prix au kilo.
""",
    "formules": """
**Concentration de contrainte** — σmax = Kt × σnom · fatigue (contrainte alternée) : Kt × σnom ≤ σD (pièce) / s

**Wöhler** — acier : palier σD (endurance illimitée) · aluminium : contrainte lue pour une durée de vie visée

**Charpy** — KV = m g (h0 − h1) (J) · JR / J0 / J2 : 27 J à +20 / 0 / −20 °C (EN 10025-2)

**Flexion trois points** — σmax = 3 F L / (2 b h²) (section b × h, portée L)

**Coût d'une pièce en traction** — S = F s / Re · m = ρ S L · coût = m × prix au kilo
""",
    "exemple": """
### Cas industriel — Le ressort de clapet qui cassait au bout de six mois

**Le symptôme.** Sur un compresseur, des ressorts de clapet cassent après plusieurs mois de service. Le
calcul statique du ressort était juste : la contrainte maximale restait bien sous la limite élastique du fil.

**L'analyse.** Le ressort travaille à chaque cycle du compresseur. À 1 500 cycles par minute en service
continu (donnée d'énoncé), cela fait plus de 2 millions de cycles par jour, et environ 3,9 × 10⁸ en six mois. La cassure montre une zone **lisse** partant d'un point de la surface du fil, puis une petite
zone rugueuse : une **rupture de fatigue** typique. Le point de départ est une petite marque laissée par
l'enroulement.

**Les causes.** Le dimensionnement avait été fait sur la limite élastique (statique), pas sur la limite
d'endurance du fil ; et la surface du fil n'avait reçu aucun traitement.

**La correction.**
- vérification en fatigue sur les données du fournisseur du fil, qui tiennent compte de la précharge (la
  contrainte du ressort ne revient pas à zéro : la règle « Kt × σnom ≤ σD » ne s'applique pas telle quelle) ;
- **grenaillage** du ressort après enroulement et traitement thermique, écrit sur le plan ;
- contrôle de l'état de surface du fil à réception.

Les ressorts suivants ont dépassé la durée de vie visée lors des essais d'endurance du constructeur.

**Ce que le cas apprend.** Une pièce cyclée se dimensionne en **fatigue**. Et pour une pièce qui casse en
fatigue, l'état de **surface** compte autant que le matériau : c'est là que tout commence.
""",
    "exercice": """
### Exercice — L'arbre de convoyeur et la structure extérieure

**Partie A — Fatigue.** Un arbre de convoyeur tourne en flexion rotative. Au droit d'un épaulement, la
contrainte alternée nominale vaut **120 MPa** (donnée d'énoncé). La limite d'endurance de la pièce,
corrections d'état de surface et de taille comprises, vaut **250 MPa** (donnée d'énoncé).

**1.** Avec un épaulement à petit congé (Kt = 2,4), calculer σmax. L'arbre tient-il en fatigue (aucun coefficient
de sécurité imposé) ?

**2.** Le bureau d'études propose un congé de rayon plus grand (Kt = 1,6). Même question.

**3.** Citer deux autres moyens d'améliorer la tenue en fatigue sans changer de matériau.

**Partie B — Résilience.** Une passerelle extérieure doit rester sûre jusqu'à **−15 °C**.

**4.** Parmi S355JR, S355J0 et S355J2, laquelle choisir ? Justifier.

**5.** Lors d'un essai Charpy réalisé à −20 °C sur une éprouvette de la tôle livrée, un mouton de 20 kg lâché de
1,5 m remonte à 1,3 m. Calculer l'énergie absorbée. La tôle respecte-t-elle la garantie de la qualité choisie en 4 ?
""",
    "corrige": """
### Corrigé, en six temps

#### 1. Ce que dit l'énoncé

Un arbre cyclé avec une concentration de contrainte, une limite d'endurance de pièce donnée ; une structure
exposée au froid ; un essai Charpy.

#### 2. Quelle règle, et pourquoi

> **σmax = Kt × σnom ≤ σD de la pièce** (fatigue : la fissure s'amorce au pic) ; **KV = m g (h0 − h1)** ;
> qualités JR / J0 / J2 : 27 J garantis à +20 / 0 / −20 °C.

#### 3. Les conversions

Contraintes en MPa ; énergie en J (kg × m/s² × m).

#### 4. Le remplacement

σmax = 2,4 × 120 ; σmax = 1,6 × 120 ; KV = 20 × 9,81 × (1,5 − 1,3).

#### 5. Le calcul

**1.** σmax = 2,4 × 120 = **288 MPa** > 250 : l'arbre **ne tient pas** en fatigue, il cassera à terme.

**2.** σmax = 1,6 × 120 = **192 MPa** < 250 : il **tient** (marge 250 / 192 ≈ 1,3).

**3.** Soigner l'état de surface (rectification, polissage) ; **grenailler** ou **galeter** le congé (compression
en surface) ; éloigner l'épaulement de la zone la plus chargée ; augmenter le diamètre (σnom baisse).

**4.** **S355J2** : c'est la seule dont la température d'essai (−20 °C) couvre −15 °C. J0 (0 °C) et JR (+20 °C)
ne garantissent rien à −15 °C.

**5.** KV = 20 × 9,81 × 0,2 ≈ **39,2 J** ≥ 27 J à −20 °C : la tôle respecte bien la garantie J2 choisie en 4.

#### 6. La vérification

**Bon sens** : le congé ne change ni le matériau ni la charge, mais divise le pic de contrainte : la forme
compte autant que le matériau. **Unités** : J = N × m. **Prudence** : un Charpy ne renseigne pas sur les
températures plus basses que celle de l'essai.
""",
}

# ===========================================================================
# 3. MÉTHODE
# ===========================================================================
MTH_3_5 = ("3.5", "Vérifier une pièce en fatigue", [
    "**Repérer si la pièce est cyclée** (rotation en flexion, vibration autour de zéro : contrainte alternée) : "
    "si oui, le critère n'est pas Re mais la limite d'endurance. Contrainte qui ne revient pas à zéro (ressort "
    "préchargé, vis serrée) : utiliser les données de l'énoncé ou du fournisseur.",
    "**Calculer la contrainte alternée nominale** σnom par la RDM, à l'endroit le plus défavorable (gorge, "
    "épaulement, trou).",
    "**Appliquer la concentration de contrainte** : σmax = Kt × σnom (Kt lu sur abaque, donné dans l'énoncé).",
    "**Comparer à la limite d'endurance de la pièce** (éprouvette corrigée de l'état de surface et de la "
    "taille) : σmax ≤ σD / s.",
    "**Si ça ne passe pas** : agrandir le congé, éloigner l'accident de forme, améliorer la surface, "
    "grenailler ou galeter, augmenter la section — avant de changer de matériau.",
], "Arbre : σnom = 120 MPa, épaulement à petit congé Kt = 2,4 → σmax = 288 MPa > σD = 250 MPa (s = 1, énoncé) : "
   "refusé. Congé plus grand, Kt = 1,6 → 192 MPa : accepté.")

# ===========================================================================
# 4. ATELIERS (fin de liste ATELIERS, après at173)
# ===========================================================================
ATELIERS_NOUVEAUX = [
    {
        "id": "at174",
        "chapitre": "Bloc 3",
        "titre": "Arbre à gorge : tiendra-t-il en fatigue ?",
        "theme": "Matériaux",
        "fiche": "3.5",
        "figure": "fatigue_entaille",
        "vocabulaire": [
            ("Limite d'endurance σD",
             "l'amplitude de contrainte sous laquelle un acier tient un nombre illimité de cycles (palier de la "
             "courbe de Wöhler)."),
            ("Coefficient Kt",
             "le facteur de concentration de contrainte d'un accident de forme : σmax = Kt × σnom."),
            ("Fatigue",
             "rupture progressive sous charge répétée, bien en dessous de Re."),
        ],
        "enonce": "Un arbre tourne en flexion rotative. Au droit d'une gorge, la contrainte alternée nominale vaut "
                  "130 MPa. La limite d'endurance de la pièce, corrections comprises, vaut 270 MPa ; la limite "
                  "élastique du matériau vaut 600 MPa (données d'énoncé ; aucun coefficient de sécurité imposé).",
        "etapes": [
            {"type": "numerique", "label": "Contrainte maximale, gorge à petit rayon",
             "unite": "MPa", "attendu": 325, "tol": 1,
             "consigne": "La gorge a un petit rayon de fond (Kt = 2,5). Calcule σmax = Kt × σnom.",
             "indice": "σmax = 2,5 × 130.",
             "pieges": [(130, "130 MPa, c'est la contrainte nominale : au fond de la gorge, elle est multipliée par Kt.")],
             "aide": "2,5 × 130 = 325 MPa."},
            {"type": "qcm", "label": "Verdict",
             "question": "σmax = 325 MPa pour σD = 270 MPa (et Re = 600 MPa). Que se passe-t-il ?",
             "options": ["Rien : 325 MPa reste sous Re, la pièce est sûre",
                         "La pièce cassera en fatigue, à terme : σmax dépasse σD",
                         "La pièce casse au premier tour"], "bonne": 1,
             "indice": "En fatigue, le critère n'est pas Re mais σD.",
             "diagnostics": {0: "Sous Re, la pièce ne se déforme pas au premier chargement ; mais répété des millions "
                                 "de fois, σmax > σD amorce une fissure de fatigue.",
                             2: "Non : 325 MPa ne casse pas la pièce d'un coup. La fatigue est progressive : la "
                                "fissure avance cycle après cycle."}},
            {"type": "numerique", "label": "Contrainte maximale avec un congé",
             "unite": "MPa", "attendu": 234, "tol": 1,
             "consigne": "On remplace la gorge par un congé de grand rayon (Kt = 1,8). Calcule σmax.",
             "indice": "σmax = 1,8 × 130.",
             "pieges": [(325, "325, c'est l'ancien Kt (2,5). Le congé fait baisser Kt à 1,8.")],
             "aide": "1,8 × 130 = 234 MPa < 270 MPa : la pièce tient."},
            {"type": "numerique", "label": "Marge par rapport à σD",
             "unite": "", "attendu": 1.154, "tol": 0.005,
             "consigne": "Calcule le rapport σD / σmax avec le congé.",
             "indice": "270 / 234.",
             "pieges": [(0.867, "0,867 : rapport inversé. La marge, c'est σD / σmax.")],
             "aide": "270 / 234 ≈ 1,15 : la pièce tient, avec une marge encore faible."},
            {"type": "qcm", "label": "Gagner de la marge",
             "question": "Pour augmenter encore la marge sans changer de matériau ni de diamètre, que faire ?",
             "options": ["Grenailler ou galeter le congé, et soigner son état de surface",
                         "Sabler la pièce", "Augmenter Re en choisissant un acier plus dur"], "bonne": 0,
             "indice": "Une fissure de fatigue naît en surface et doit s'ouvrir pour avancer.",
             "diagnostics": {1: "Le sablage nettoie ou rend rugueux : il n'apporte pas de compression utile, et une "
                                 "surface rugueuse tient plutôt moins bien en fatigue.",
                             2: "Changer d'acier, c'est changer de matériau ; et c'est σD, pas Re, qui compte en fatigue."}},
        ],
        "corrige": {
            "enonce": "σnom = 130 MPa alternée, σD de la pièce = 270 MPa ; gorge à petit rayon Kt = 2,5, puis congé Kt = 1,8.",
            "regle": "**σmax = Kt × σnom ≤ σD** : la fissure de fatigue s'amorce au pic de contrainte.",
            "conversions": "Contraintes en MPa.",
            "remplacement": "2,5 × 130 ; 1,8 × 130 ; 270 / 234.",
            "calcul": "**325 MPa** (refusé) → **234 MPa** (accepté) ; marge **1,15**.",
            "verification": "Le matériau et la charge n'ont pas changé : seule la forme a fait passer la pièce. En "
                            "fatigue, un rayon de congé vaut souvent mieux qu'un acier plus cher.",
        },
        "a_retenir": "À retenir : en fatigue, on compare Kt × σnom à la limite d'endurance de la pièce ; agrandir un "
                     "congé ou grenailler fait souvent gagner plus que changer d'acier.",
    },
    {
        "id": "at175",
        "chapitre": "Bloc 3",
        "titre": "Passerelle extérieure : essai Charpy et choix de la qualité d'acier",
        "theme": "Matériaux",
        "fiche": "3.5",
        "figure": "essai_charpy",
        "vocabulaire": [
            ("Résilience (KV)",
             "l'aptitude à encaisser un choc : l'énergie absorbée par la rupture d'une éprouvette entaillée en V, "
             "mesurée en joules à l'essai Charpy (ISO 148-1)."),
            ("Transition ductile-fragile",
             "la chute d'énergie absorbée d'un acier de construction quand la température baisse."),
            ("Qualité JR, J0, J2",
             "27 J garantis à +20 °C, 0 °C ou −20 °C (EN 10025-2)."),
        ],
        "enonce": "Essai Charpy : le mouton, de masse 25 kg, est lâché d'une hauteur de 1,5 m et remonte à 1,32 m après "
                  "rupture (données d'énoncé ; g = 9,81 m/s² ; frottements négligés). La passerelle doit rester sûre "
                  "jusqu'à −15 °C.",
        "etapes": [
            {"type": "numerique", "label": "Énergie absorbée",
             "unite": "J", "attendu": 44.145, "tol": 0.1,
             "consigne": "Calcule KV = m × g × (h0 − h1).",
             "indice": "h0 − h1 = 0,18 m.",
             "pieges": [(367.88, "367,9 J : c'est m g h0, l'énergie de départ. Ce qui compte, c'est ce que le mouton a "
                                 "perdu : h0 − h1."),
                        (323.73, "323,7 J, c'est l'énergie restante à la remontée (m g h1) ; l'énergie absorbée est la "
                                 "différence."),
                        (4.5, "4,5 : tu as oublié g. KV = m × g × Δh.")],
             "aide": "25 × 9,81 × 0,18 ≈ 44,1 J."},
            {"type": "qcm", "label": "Niveau atteint",
             "question": "KV ≈ 44 J à la température d'essai. Que peut-on conclure ?",
             "options": ["L'acier est sûr à toutes les températures",
                         "Il dépasse 27 J à la température d'essai ; on ne peut rien en conclure pour une température plus basse",
                         "Il est fragile"], "bonne": 1,
             "indice": "Que se passe-t-il pour un acier de construction quand la température baisse ?",
             "diagnostics": {0: "Non : sous la zone de transition, l'énergie absorbée chute. Un Charpy ne renseigne pas "
                                 "sur les températures plus basses que celle de l'essai.",
                             2: "44 J dépassent le niveau de 27 J : à cette température, la rupture absorbe assez "
                                "d'énergie."}},
            {"type": "qcm", "label": "Choix de la qualité",
             "question": "Pour une passerelle sûre jusqu'à −15 °C, quelle qualité de S355 choisir ?",
             "options": ["S355JR", "S355J0", "S355J2"], "bonne": 2,
             "indice": "Il faut une température d'essai au moins aussi basse que la température de service la plus froide.",
             "diagnostics": {0: "JR : 27 J garantis à +20 °C seulement. À −15 °C, rien n'est garanti.",
                             1: "J0 : 27 J garantis à 0 °C. −15 °C est plus froid : il faut J2 (−20 °C)."}},
        ],
        "corrige": {
            "enonce": "Mouton 25 kg, h0 = 1,5 m, h1 = 1,32 m ; service jusqu'à −15 °C.",
            "regle": "**KV = m g (h0 − h1)** ; qualités **JR / J0 / J2 : 27 J à +20 / 0 / −20 °C** (EN 10025-2).",
            "conversions": "Unités SI : J = kg × m/s² × m.",
            "remplacement": "KV = 25 × 9,81 × 0,18.",
            "calcul": "**KV ≈ 44,1 J** ; qualité **S355J2**.",
            "verification": "La température d'essai (−20 °C) couvre la température de service (−15 °C) : la garantie "
                            "de 27 J s'applique.",
        },
        "a_retenir": "À retenir : KV = m g (h0 − h1) ; un acier de construction devient fragile au froid ; on choisit la "
                     "qualité (JR, J0, J2) dont la température d'essai couvre la température de service.",
    },
]

# ===========================================================================
# 5. GÉNÉRATEURS (famille existante « Matériaux et masses »)
# ===========================================================================
GENERATEUR = '''
def gen_charpy_energie():
    """Énergie absorbée à l'essai Charpy : KV = m g (h0 − h1)."""
    m = random.choice([10, 15, 20, 25, 30])
    h0 = random.choice([1.2, 1.4, 1.5, 1.6])
    dh = random.choice([0.1, 0.15, 0.2, 0.25, 0.3, 0.4])
    h1 = round(h0 - dh, 2)
    KV = m * 9.81 * (h0 - h1)
    diag = []
    for val, msg in (
            (m * 9.81 * h0, "C'est l'énergie de départ (m g h0). L'énergie absorbée, c'est ce que le mouton a perdu : "
                            "m g (h0 − h1)."),
            (m * 9.81 * h1, "C'est l'énergie restante à la remontée. L'énergie absorbée est la différence."),
            (m * (h0 - h1), "Il manque g : KV = m × g × (h0 − h1)."),
    ):
        if abs(val - KV) > 1 and all(abs(val - d["v"]) > 0.5 for d in diag):
            diag.append(_diag(round(val, 2), msg))
    return {
        "titre": "Matériaux — énergie absorbée à l'essai Charpy",
        "enonce": (f"Lors d'un essai Charpy, un mouton de **{m} kg** est lâché d'une hauteur de **{fr(h0, 2)} m** et remonte "
                   f"à **{fr(h1, 2)} m** après la rupture de l'éprouvette (g = 9,81 m/s² ; frottements négligés). "
                   "Quelle énergie (en J) la rupture a-t-elle absorbée ?"),
        "rep": round(KV, 2), "tol": 0.2, "unite": "J",
        "diag": diag,
        "corr": [
            f"**Ce que dit l'énoncé.** Mouton {m} kg, de {fr(h0, 2)} m à {fr(h1, 2)} m.",
            "**La règle.** L'énergie absorbée est l'énergie potentielle perdue : KV = m g (h0 − h1).",
            f"**Le calcul.** KV = {m} × 9,81 × ({fr(h0, 2)} − {fr(h1, 2)}) = {fr(KV, 1)} J.",
            "**Ce que cela apprend.** Ce résultat ne vaut qu'à la température de l'essai : un acier de construction "
            "absorbe beaucoup moins d'énergie au froid.",
        ],
        "indice": "KV = m × g × (h0 − h1).",
    }


def gen_flexion_3points():
    """Contrainte maximale à l'essai de flexion trois points (section rectangulaire)."""
    b = random.choice([6, 8, 10])
    h = random.choice([4, 5, 6])
    L = random.choice([30, 40, 50, 60])
    F = random.choice([100, 150, 200, 250, 300, 400])
    s = 3 * F * L / (2 * b * h ** 2)
    diag = []
    for val, msg in (
            (3 * F * L / (2 * h * b ** 2), "Tu as inversé b et h : c'est la hauteur h (dans le sens de la charge) qui "
                                           "est au carré."),
            (F * L / (4 * b * h ** 2), "Tu as divisé M par b h² : le module de flexion vaut b h² / 6, donc σ = (F L / 4) "
                                      "× 6 / (b h²)."),
            (3 * F * L / (b * h ** 2), "Il manque le facteur 2 au dénominateur : σ = 3 F L / (2 b h²)."),
    ):
        if abs(val - s) > max(0.5, s * 0.02) and all(abs(val - d["v"]) > 0.5 for d in diag):
            diag.append(_diag(round(val, 2), msg))
    return {
        "titre": "Matériaux — essai de flexion trois points",
        "enonce": (f"Une éprouvette de section **{b} × {h} mm** (largeur × hauteur) repose sur deux appuis distants de "
                   f"**{L} mm**. Elle rompt sous un effort central de **{F} N**. Quelle est sa résistance à la flexion "
                   "(contrainte maximale, en MPa) ?"),
        "rep": round(s, 2), "tol": max(0.5, s * 0.01), "unite": "MPa",
        "diag": diag,
        "corr": [
            f"**Ce que dit l'énoncé.** b = {b} mm, h = {h} mm, L = {L} mm, F = {F} N.",
            "**La règle.** σmax = 3 F L / (2 b h²) — moment F L / 4 au milieu, module de flexion b h² / 6.",
            f"**Le calcul.** σmax = 3 × {F} × {L} / (2 × {b} × {h}²) = {fr(s, 1)} MPa.",
            "**Je vérifie.** N et mm donnent des N/mm², c'est-à-dire des MPa.",
        ],
        "indice": "σmax = 3 F L / (2 b h²), en N et mm.",
    }
'''

# ===========================================================================
# 6. QUIZ — nouvelle catégorie « Essais mécaniques, fatigue et traitements »
#    positions de la bonne réponse : 1, 3, 0, 2, 3, 0, 2, 1
# ===========================================================================
QUIZ_ESSAIS = [
    ("Un arbre dimensionné avec σ ≤ Re / 2 casse après quelques mois de rotation, sans s'être déformé. Quelle est la "
     "cause la plus probable ?",
     ["Une surcharge statique ponctuelle", "La fatigue : charge répétée sur des millions de cycles",
      "Un défaut de dureté", "Une corrosion généralisée"], 1,
     "Rupture différée, sans déformation, sous charge répétée inférieure à Re : signature de la fatigue. La cassure "
     "montre une zone lisse (propagation) et une zone rugueuse (rupture finale).", "Base"),
    ("Sur la courbe de Wöhler d'un acier, que représente le palier horizontal ?",
     ["La limite élastique Re", "La résistance à la rupture Rm", "L'énergie Charpy",
      "La limite d'endurance : sous cette amplitude, la durée de vie est illimitée"], 3,
     "Le palier est la limite d'endurance σD. Les alliages d'aluminium n'ont pas ce palier : on raisonne sur une "
     "durée de vie visée.", "Base"),
    ("Au fond d'une gorge, Kt = 2. La contrainte nominale alternée vaut 100 MPa. Quelle contrainte faut-il comparer "
     "à la limite d'endurance ?",
     ["200 MPa", "100 MPa", "50 MPa", "102 MPa"], 0,
     "σmax = Kt × σnom = 2 × 100 = 200 MPa. En fatigue, la fissure s'amorce au pic de contrainte.", "Calcul"),
    ("Pourquoi le grenaillage améliore-t-il la tenue en fatigue ?",
     ["Il durcit tout le cœur de la pièce", "Il augmente la limite élastique de toute la pièce",
      "Il crée des contraintes de compression en surface, qui empêchent les fissures de s'ouvrir",
      "Il dépose un revêtement protecteur"], 2,
     "Une fissure de fatigue doit s'ouvrir pour avancer ; la compression de surface la tient fermée. L'effet est en "
     "surface : un usinage après grenaillage l'enlève.", "Intermédiaire"),
    ("Une structure en acier doit rester sûre jusqu'à −5 °C. Quelle qualité choisir parmi JR, J0, J2 ?",
     ["JR", "J0", "N'importe laquelle : 27 J dans tous les cas", "J2"], 3,
     "27 J sont garantis à +20 °C (JR), 0 °C (J0), −20 °C (J2). −5 °C est plus froid que 0 °C : seule J2 couvre "
     "−5 °C.", "Piège"),
    ("À l'essai Charpy, un mouton de 10 kg lâché de 1,5 m remonte à 1,2 m. Quelle énergie la rupture a-t-elle "
     "absorbée (g = 9,81 m/s²) ?",
     ["Environ 29,4 J", "Environ 147 J", "3 J", "Environ 118 J"], 0,
     "KV = m g (h0 − h1) = 10 × 9,81 × 0,3 ≈ 29,4 J. 147 J est l'énergie de départ, 118 J l'énergie restante.",
     "Calcul"),
    ("Pourquoi mesure-t-on la résistance d'une céramique par un essai de flexion plutôt que de traction ?",
     ["Parce qu'elle est trop molle pour être tirée", "Parce que la flexion est plus rapide",
      "Parce qu'elle est fragile : une éprouvette de traction se briserait dans les mors",
      "Parce qu'une céramique n'a pas de module d'Young"], 2,
     "Les matériaux fragiles se prêtent mal à la traction (serrage, alignement). La flexion trois points donne "
     "σmax = 3 F L / (2 b h²) sur la face tendue.", "Intermédiaire"),
    ("Le sablage d'une pièce sert à :",
     ["Augmenter sa tenue en fatigue", "Nettoyer, décaper ou rendre la surface rugueuse avant peinture ou collage",
      "Durcir son cœur", "Supprimer les contraintes résiduelles"], 1,
     "Le sablage est une préparation de surface. Pour la fatigue, on grenaille ou on galète : ce n'est pas le "
     "même but.", "Piège"),
]
