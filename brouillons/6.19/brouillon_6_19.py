# -*- coding: utf-8 -*-
# BROUILLON — fiche 6.19 « Dimensionner un roulement et serrer une vis » (référentiel S5.1).
# Rien de ceci n'est encore dans app.py. _k_defs, _k_fl (6.15) existent déjà dans app.py.
#
# Sources des valeurs de catalogue utilisées :
# - SKF 6205 (roulement rigide à billes, 25 × 52 × 15 mm) : C = 14,8 kN, C0 = 7,8 kN
#   (fiche produit skf.com, reprise par les distributeurs).
# - SKF NU 205 ECP (roulement à rouleaux cylindriques, 25 × 52 × 15 mm) : C = 32,5 kN, C0 = 27 kN
#   (fiche produit « Generated from www.skf.com on 2022-12-05 »).
# - Sections résistantes des vis (ISO 898-1) : M8 36,6 mm² ; M10 58,0 mm² ; M12 84,3 mm².
import math

# ===========================================================================
# 1. FIGURES
# ===========================================================================

def duree_vie_dispersion():
    """Durée de vie d'un lot de roulements identiques : une dispersion, et la définition de L10."""
    p = [_k_defs(), _txt(30, 24, "Cent roulements identiques, même charge : ils ne lâchent pas tous en même temps", 13, TRAIT, "start", True)]
    x0, y0, w, h = 70, 250, 420, 170
    p.append(f"<line x1='{x0}' y1='{y0}' x2='{x0 + w + 10}' y2='{y0}' stroke='{FIN}' stroke-width='1.4'/>")
    p.append(f"<line x1='{x0}' y1='{y0}' x2='{x0}' y2='{y0 - h - 10}' stroke='{FIN}' stroke-width='1.4'/>")
    p.append(_txt(x0 + w + 12, y0 + 4, "durée", 11, FIN))
    p.append(_txt(x0 - 6, y0 - h - 14, "nombre de défaillances", 10, FIN, "start"))
    # histogramme qualitatif (loi dissymétrique : beaucoup de roulements dépassent largement L10)
    barres = (2, 8, 14, 18, 17, 14, 10, 7, 5, 3, 2)
    bw = w / len(barres)
    for i, b in enumerate(barres):
        c = ALERTE if i < 2 else ALESAGE
        p.append(f"<rect x='{x0 + i * bw + 2:.1f}' y='{y0 - b * 8}' width='{bw - 4:.1f}' height='{b * 8}' fill='{c}' opacity='0.75'/>")
    xl = x0 + 2 * bw
    p.append(f"<line x1='{xl:.1f}' y1='{y0 + 6}' x2='{xl:.1f}' y2='{y0 - h}' stroke='{ALERTE}' stroke-width='2.4' stroke-dasharray='6 4'>"
             "<animate attributeName='opacity' values='1;0.3;1' dur='1.8s' repeatCount='indefinite'/></line>")
    p.append(_txt(xl, y0 + 22, "L10", 13, ALERTE, "middle", True))
    p.append(_txt(xl - 6, y0 - h + 12, "10 % ont lâché", 10, ALERTE, "end", True))
    p.append(_txt(xl + 6, y0 - h + 12, "90 % tournent encore", 10, ALESAGE, "start", True))
    x1 = 520
    p.append(f"<rect x='{x1}' y='44' width='240' height='206' rx='6' fill='#ffffff' stroke='{FIN}'/>")
    for i, (t, g, c) in enumerate((("L10 :", True, TRAIT), ("la durée atteinte ou dépassée", False, TRAIT),
                                   ("par 90 % des roulements", False, TRAIT), ("d'un lot (fiabilité 90 %).", False, TRAIT),
                                   ("", False, TRAIT), ("C, charge dynamique de base :", True, TRAIT),
                                   ("la charge pour laquelle", False, TRAIT), ("L10 = 1 million de tours.", False, TRAIT),
                                   ("Elle se lit au catalogue.", False, OK))):
        if t:
            p.append(_txt(x1 + 14, 68 + 20 * i, t, 12, c, "start", g))
    p.append(f"<rect x='30' y='278' width='730' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 300, "Un roulement bien monté et lubrifié finit par la fatigue : la piste s'écaille. C'est un phénomène statistique.", 12, TRAIT))
    return _svg("".join(p), 790, 326)


def charge_vie_catalogue():
    """6205 (billes) et NU 205 ECP (rouleaux), même encombrement, même charge : la durée de vie."""
    p = [_k_defs(), _txt(30, 24, "Même encombrement (25 × 52 × 15 mm), même charge 2 kN à 1 500 tr/min", 13, TRAIT, "start", True)]
    lignes = (("SKF 6205", "billes, C = 14,8 kN", 4502, ALESAGE), ("SKF NU 205 ECP", "rouleaux, C = 32,5 kN", 120763, OK))
    x0, y0, wmax = 230, 80, 380
    vmax = 120763
    for i, (nom, sous, v, c) in enumerate(lignes):
        y = y0 + 80 * i
        w = max(8, wmax * v / vmax)
        p.append(_txt(x0 - 12, y + 18, nom, 13, TRAIT, "end", True))
        p.append(_txt(x0 - 12, y + 36, sous, 11, FIN, "end"))
        p.append(f"<rect x='{x0}' y='{y}' width='{w:.0f}' height='40' rx='4' fill='{c}' opacity='0.85'>"
                 "<animate attributeName='opacity' values='0.85;0.45;0.85' dur='2.4s' repeatCount='indefinite'/></rect>")
        p.append(_txt(x0 + w + 8, y + 26, f"L10h ≈ {v:,} h".replace(",", " "), 13, c, "start", True))
    p.append(_txt(x0, y0 + 168, "(échelle linéaire : un facteur 27 entre les deux)", 10, FIN))
    p.append(f"<rect x='30' y='270' width='730' height='54' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 292, "Contact sur une ligne (rouleaux) au lieu d'un point (billes) : C plus de deux fois plus grand, exposant 10/3.", 12, TRAIT, "start", True))
    p.append(_txt(46, 312, "Mais un NU ne tient pas d'effort axial (bague intérieure sans épaulement) : le choix dépend aussi des charges.", 12, FIN))
    return _svg("".join(p), 790, 338)


def rotule_helicoidale_solutions():
    p = [_k_defs(), _txt(30, 24, "Solutions constructives : la rotule et l'hélicoïdale", 13, TRAIT, "start", True)]
    for x0, titre, c in ((30, "ROTULE : accepter un désalignement", ALESAGE), (410, "HÉLICOÏDALE : vis et écrou", ARBRE)):
        p.append(f"<rect x='{x0}' y='40' width='360' height='240' rx='8' fill='#ffffff' stroke='{c}' stroke-width='2'/>")
        p.append(_txt(x0 + 180, 62, titre, 12, c, "middle", True))
    # roulement à rotule, vu en coupe : la piste extérieure est un arc de sphère, l'arbre et la bague
    # intérieure s'inclinent dedans (rotulage)
    cx, cy = 120, 150
    p.append(f"<path d='M {cx - 30} {cy - 50} A 58 58 0 0 1 {cx + 30} {cy - 50}' fill='none' stroke='{TRAIT}' stroke-width='7'/>")
    p.append(f"<path d='M {cx - 30} {cy + 50} A 58 58 0 0 0 {cx + 30} {cy + 50}' fill='none' stroke='{TRAIT}' stroke-width='7'/>")
    p.append(f"<g><rect x='{cx - 80}' y='{cy - 8}' width='160' height='16' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.6'/>"
             f"<rect x='{cx - 24}' y='{cy - 30}' width='48' height='22' fill='#cbd5e1' stroke='{TRAIT}'/>"
             f"<rect x='{cx - 24}' y='{cy + 8}' width='48' height='22' fill='#cbd5e1' stroke='{TRAIT}'/>"
             + "".join(f"<circle cx='{cx + dx}' cy='{cy + dy}' r='7' fill='#ffffff' stroke='{ALESAGE}' stroke-width='2'/>"
                       for dx in (-11, 11) for dy in (-39, 39))
             + f"<animateTransform attributeName='transform' type='rotate' values='0 {cx} {cy}; -6 {cx} {cy}; 6 {cx} {cy}; 0 {cx} {cy}' dur='3s' repeatCount='indefinite'/></g>")
    p.append(_txt(cx, 230, "roulement à rotule (coupe)", 11, ALESAGE, "middle", True))
    p.append(_txt(cx, 245, "piste extérieure sphérique", 9, FIN, "middle"))
    # embout à rotule : la sphère reste dans son logement, la tige pivote autour
    ex, ey = 290, 150
    p.append(f"<g><rect x='{ex - 6}' y='{ey + 26}' width='12' height='70' fill='#cbd5e1' stroke='{TRAIT}'/>"
             f"<circle cx='{ex}' cy='{ey}' r='30' fill='none' stroke='{TRAIT}' stroke-width='5'/>"
             f"<animateTransform attributeName='transform' type='rotate' values='0 {ex} {ey}; 12 {ex} {ey}; -12 {ex} {ey}; 0 {ex} {ey}' dur='3s' repeatCount='indefinite'/></g>")
    p.append(f"<circle cx='{ex}' cy='{ey}' r='20' fill='#fde68a' stroke='{ARBRE}' stroke-width='2'/>")
    p.append(_txt(ex, 92, "embout à rotule", 11, ALESAGE, "middle", True))
    p.append(_txt(ex, 106, "(bout de tige de vérin)", 10, FIN, "middle"))
    p.append(_txt(205, 268, "Usage : arbres longs, bâtis soudés, vérins articulés.", 10, TRAIT, "middle"))
    # hélicoïdale : vis trapézoïdale + écrou bronze ; vis à billes
    for y, nom, sous, billes in ((100, "vis trapézoïdale + écrou bronze", "glissement : simple, souvent irréversible", False),
                                 (190, "vis à billes", "roulement : rendement élevé, réversible", True)):
        p.append(f"<rect x='440' y='{y}' width='300' height='20' fill='#e2e8f0' stroke='{TRAIT}'/>")
        for k in range(14):
            p.append(f"<line x1='{446 + 21 * k}' y1='{y + 20}' x2='{456 + 21 * k}' y2='{y}' stroke='{TRAIT}' stroke-width='1.6'/>")
        p.append(f"<g><rect x='520' y='{y - 10}' width='70' height='40' rx='4' fill='none' stroke='{ARBRE}' stroke-width='3'/>"
                 + ("".join(f"<circle cx='{530 + 12 * k}' cy='{y - 3}' r='4' fill='{ARBRE}'/>" for k in range(5)) if billes else "")
                 + "<animateTransform attributeName='transform' type='translate' values='0,0; 90,0; 0,0' dur='5s' repeatCount='indefinite'/></g>")
        p.append(_txt(590, y + 46, nom, 11, ARBRE, "middle", True))
        p.append(_txt(590, y + 62, sous, 10, FIN, "middle"))
    p.append(f"<rect x='30' y='292' width='740' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 314, "Loi v = ph × N et réversibilité : fiche 6.18. Ici : quelle solution technologique réalise la liaison.", 12, TRAIT))
    return _svg("".join(p), 800, 340)


def precharge_vis():
    p = [_k_defs(), _txt(30, 24, "Serrer une vis : le couple de serrage crée la précharge F0", 13, TRAIT, "start", True)]
    # assemblage : deux plaques, une vis, un écrou
    p.append(f"<rect x='90' y='110' width='200' height='34' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.6'/>")
    p.append(f"<rect x='90' y='144' width='200' height='34' fill='#cbd5e1' stroke='{TRAIT}' stroke-width='1.6'/>")
    p.append(f"<rect x='176' y='84' width='28' height='120' fill='#ffffff' stroke='{TRAIT}' stroke-width='2'/>")
    p.append(f"<rect x='160' y='72' width='60' height='14' fill='{TRAIT}'/>")
    p.append(f"<rect x='164' y='204' width='52' height='14' fill='{TRAIT}'/>")
    p.append(_k_fl(190, 62, 190, 40, ARBRE, "ko", 3))
    p.append(_k_fl(190, 230, 190, 252, ARBRE, "ko", 3))
    p.append(_txt(250, 54, "F0 : la vis est tendue", 11, ARBRE, "start", True))
    p.append(_k_fl(300, 100, 300, 126, ALESAGE, "kb", 2.4))
    p.append(_k_fl(300, 188, 300, 162, ALESAGE, "kb", 2.4))
    p.append(_txt(306, 148, "les plaques sont serrées", 11, ALESAGE, "start", True))
    p.append(f"<path d='M 150 66 A 46 14 0 1 1 232 66' fill='none' stroke='{OK}' stroke-width='2.6' marker-end='url(#kg)'>"
             "<animate attributeName='opacity' values='1;0.3;1' dur='1.6s' repeatCount='indefinite'/></path>")
    p.append(_txt(120, 62, "couple Cs", 11, OK, "end", True))
    x0 = 470
    p.append(f"<rect x='{x0}' y='44' width='300' height='220' rx='6' fill='#ffffff' stroke='{FIN}'/>")
    for i, (t, g, c) in enumerate((("Où part le couple de serrage ?", True, TRAIT),
                                   ("une grande partie dans le frottement", False, TRAIT),
                                   ("sous la tête (ou l'écrou) et dans les filets ;", False, TRAIT),
                                   ("le reste tend la vis.", False, TRAIT), ("", False, TRAIT),
                                   ("Ordre de grandeur : Cs ≈ 0,2 × d × F0", True, OK),
                                   ("le 0,2 dépend du frottement : graissé,", False, TRAIT),
                                   ("il baisse — le même couple tend alors", False, TRAIT),
                                   ("davantage la vis.", False, TRAIT))):
        if t:
            p.append(_txt(x0 + 14, 68 + 21 * i, t, 12, c, "start", g))
    p.append(f"<rect x='30' y='276' width='740' height='34' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 298, "Contrôle : σ = F0 / As sous Re, avec une marge (la torsion de serrage s'ajoute) ; As : ISO 898-1.", 12, TRAIT))
    return _svg("".join(p), 800, 324)


# --- figure à curseurs : durée de vie
_ROULEMENTS = {"6205": ("SKF 6205 (billes)", 14.8, 3.0), "NU205": ("SKF NU 205 ECP (rouleaux)", 32.5, 10 / 3)}


def dyn_duree_roulement(r="6205", P=2.0, N=1500.0):
    """Durée de vie L10 et L10h d'un roulement de catalogue, selon la charge et la vitesse."""
    nom, C, n = _ROULEMENTS[r]
    L10 = (C / P) ** n
    L10h = L10 * 1e6 / (60 * N)
    vise = 20000
    ok = L10h >= vise
    col = OK if ok else ALERTE
    p = [_k_defs(), _txt(30, 24, f"{nom} : C = {_fr_court(C, 1)} kN, P = {_fr_court(P, 2)} kN, N = {int(N)} tr/min", 13, TRAIT, "start", True)]
    x0, y0, wmax = 60, 140, 420
    lmax = math.log10(1e6)
    w = max(4, wmax * min(1, math.log10(max(L10h, 1)) / lmax))
    wv = wmax * math.log10(vise) / lmax
    p.append(f"<rect x='{x0}' y='{y0}' width='{wmax}' height='34' rx='4' fill='#f1f5f9' stroke='{FIN}'/>")
    p.append(f"<rect x='{x0}' y='{y0}' width='{w:.0f}' height='34' rx='4' fill='{col}' opacity='0.85'/>")
    p.append(f"<line x1='{x0 + wv:.0f}' y1='{y0 - 14}' x2='{x0 + wv:.0f}' y2='{y0 + 48}' stroke='{TRAIT}' stroke-width='2' stroke-dasharray='5 4'/>")
    p.append(_txt(x0 + wv, y0 - 18, "20 000 h (exemple de durée visée)", 10, TRAIT, "middle"))
    for v, lab in ((100, "100 h"), (1000, "1 000"), (10000, "10 000"), (100000, "100 000"), (1000000, "10⁶ h")):
        xx = x0 + wmax * math.log10(v) / lmax
        p.append(_txt(xx, y0 + 52, lab, 9, FIN, "middle"))
    p.append(_txt(x0, y0 + 72, "(échelle logarithmique : chaque graduation vaut 10 fois la précédente)", 9, FIN))
    x1 = 510
    p.append(f"<rect x='{x1}' y='44' width='260' height='190' rx='6' fill='#ffffff' stroke='{col}' stroke-width='1.8'/>")
    lignes = [(f"exposant n = {'3 (billes)' if n == 3 else '10/3 (rouleaux)'}", TRAIT, False),
              (f"L10 = (C/P)^n = {_fr_court(L10, 1)} millions de tours", TRAIT, False),
              (f"L10h = L10 × 10⁶ / (60 N)", TRAIT, False),
              (f"       ≈ {_fr_court(L10h, 0)} h", col, True),
              ("au moins 20 000 h : convient" if ok else "moins de 20 000 h : trop juste", col, True),
              (f"C requis pour 20 000 h : {_fr_court(P * (vise * 60 * N / 1e6) ** (1 / n), 1)} kN", TRAIT, False)]
    for i, (t, c, g) in enumerate(lignes):
        p.append(_txt(x1 + 12, 68 + 26 * i, t, 12, c, "start", g))
    p.append(_txt(30, 262, "Doubler la charge divise la durée de vie par 8 (billes) ou par environ 10 (rouleaux).", 11, FIN))
    return _svg("".join(p), 790, 276)


_CHOIX_ROULEMENTS = [("SKF 6205 (billes, C = 14,8 kN)", "6205"), ("SKF NU 205 ECP (rouleaux, C = 32,5 kN)", "NU205")]

FIGURES_NOUVELLES = {
    "duree_vie_dispersion": ("La durée de vie d'un roulement : dispersion et définition de L10", duree_vie_dispersion),
    "charge_vie_catalogue": ("Billes ou rouleaux, même encombrement : la durée de vie", charge_vie_catalogue),
    "rotule_helicoidale_solutions": ("Solutions constructives de la rotule et de l'hélicoïdale", rotule_helicoidale_solutions),
    "precharge_vis": ("Couple de serrage et précharge d'une vis", precharge_vis),
}
DYN_NOUVELLE = {
    "duree_roulement_curseurs": (
        "Choisis le roulement, la charge et la vitesse : L10 et L10h se recalculent",
        dyn_duree_roulement,
        [{"nom": "r", "label": "Roulement", "choix": _CHOIX_ROULEMENTS, "defaut": "SKF 6205 (billes, C = 14,8 kN)"},
         {"nom": "P", "label": "Charge équivalente P (kN)", "min": 0.5, "max": 6.0, "defaut": 2.0, "pas": 0.5},
         {"nom": "N", "label": "Vitesse N (tr/min)", "min": 300.0, "max": 3000.0, "defaut": 1500.0, "pas": 100.0}]),
}

# ===========================================================================
# 2. FICHE 6.19 — en FIN de bloc 6 (après la 6.18)
# ===========================================================================

FICHE_6_19 = {
    "id": '6.19',
    "titre": 'Dimensionner un roulement (L10) et serrer une vis à la bonne précharge',
    "duree": '6 h',
    "cours": """### 1. Pourquoi cette fiche

Les fiches 6.4 à 6.6 apprennent à **choisir le type** de roulement et à le monter. Il reste la question
du bureau d'études : **ce roulement-là tiendra-t-il la durée demandée** ? Et pour la visserie (fiche 6.9) :
**à quel couple serrer** pour obtenir la précharge voulue ? Ce sont les deux calculs de **pré-dimensionnement**
de cette fiche (un premier calcul rapide, pour choisir une taille avant les vérifications détaillées),
avec des valeurs lues dans des **catalogues de fabricants**.

Le calcul de durée de vie avait été annoncé en avant-goût (fiche 11.1) : le voici en entier.

### 2. La durée de vie d'un roulement : une affaire de statistique

[[FIG:duree_vie_dispersion]]

Un roulement bien choisi, bien monté et bien lubrifié ne meurt pas d'usure : il finit par la **fatigue**.
Comme un fil de fer qu'on plie et déplie jusqu'à ce qu'il casse : à chaque passage d'une bille, le métal
de la piste est écrasé puis relâché. Après des centaines de millions de passages, une petite fissure
apparaît, puis un éclat de métal se détache — l'**écaillage** : le roulement devient bruyant et vibre.
Mais cent roulements identiques, sous la même charge, ne lâchent pas tous au même moment. On définit donc :

- **L10** : la durée (en **millions de tours**) atteinte ou dépassée par **90 %** des roulements d'un lot.
  C'est une fiabilité de 90 %, pas une durée « garantie ». Pourquoi pas la moyenne ? Planifier la
  maintenance à la durée moyenne, ce serait accepter qu'environ la moitié des machines tombent en panne
  avant ; à L10, seulement 1 roulement sur 10 a lâché ;
- **C, la charge dynamique de base** : la charge radiale constante, de direction fixe, pour laquelle L10
  vaut exactement **1 million de tours** (norme ISO 281). C'est une caractéristique du roulement, **donnée
  par le catalogue du fabricant**. Attention, ce n'est **pas** une charge de service : 1 million de tours, à
  1 500 tr/min, c'est 1 000 000 / 1 500 ≈ 667 minutes, à peine 11 heures. C est une **charge de
  référence**, qui sert à comparer les roulements ; en service, P est bien plus petite que C ;
- **P, la charge dynamique équivalente** : la charge que le roulement subit réellement, ramenée à une
  charge radiale unique.

**La charge équivalente P.** *Radial* : perpendiculaire à l'arbre, comme la tension d'une courroie qui tire
sur la poulie. *Axial* : le long de l'arbre, comme la poussée d'un pignon à denture hélicoïdale. Si le
roulement ne porte qu'un effort radial Fr, **P = Fr**. S'il porte aussi un effort axial Fa, on le remplace,
pour le calcul, par une seule charge radiale fictive qui le fatiguerait autant : **P = X × Fr + Y × Fa**.
Les coefficients X et Y dépendent du type de roulement et du rapport des charges ; ils sont **donnés par le
catalogue** (ou par l'énoncé), on ne les invente pas.

### 3. La formule de durée de vie

> **L10 = (C / P)ⁿ**, en millions de tours, avec **n = 3** pour les roulements à **billes** et
> **n = 10/3** pour les roulements à **rouleaux**.
>
> En heures : **L10h = L10 × 10⁶ / (60 × N)**, avec N en tr/min.

**D'où vient cette formule ? Vérifions-la sur la définition de C.** Si P = C, alors C/P = 1 et L10 = 1ⁿ =
1 million de tours : c'est la définition de C. Si on charge deux fois moins (P = C/2), C/P = 2 et, pour des
billes, L10 = 2³ = 8 millions de tours. Diviser la charge par 2 ne double pas la vie : cela la multiplie
par 8. L'effet est **beaucoup plus que proportionnel**, à cause de l'exposant.

**Pourquoi deux exposants ?** Une bille appuie sur sa piste comme un pointeau sur une tôle : toute la charge
passe par **un point**. Un rouleau appuie comme un rouleau de laminoir : la charge est **étalée sur une
ligne**. Les deux contacts ne réagissent pas de la même façon quand on charge plus ; les fabricants l'ont
mesuré par des essais d'endurance, et la norme ISO 281 résume ces essais par l'exposant. On ne le démontre
pas en BTS. On retient : **bille = point = 3 ; rouleau = ligne = 10/3**.

**La conversion en heures, pas à pas** : L10 est en millions de tours, donc L10 × 10⁶ tours. Combien de
tours le roulement fait-il en une heure ? N tours par minute × 60 minutes = **60 N tours par heure** (à
1 500 tr/min : 90 000). Le nombre d'heures, c'est le total de tours divisé par les tours faits en une heure :
**L10h = L10 × 10⁶ / (60 N)**. Si l'on oublie le 60, on obtient des **minutes** : un résultat 60 fois trop
grand.

**Exemple chiffré, valeurs de catalogue.** Deux roulements de même encombrement (25 × 52 × 15 mm), sous
une charge radiale de **2 kN** à **1 500 tr/min** :

- **SKF 6205**, à billes, **C = 14,8 kN** (catalogue SKF) : L10 = (14,8 / 2)³ = 7,4³ = **405 millions de
  tours** ; L10h = 405 × 10⁶ / (60 × 1 500) ≈ **4 500 h** ;
- **SKF NU 205 ECP**, à rouleaux cylindriques, **C = 32,5 kN** (catalogue SKF) : L10 = (32,5 / 2)^(10/3)
  ≈ 10 900 millions de tours ; L10h ≈ **120 800 h**.

*Valeurs lues sur les fiches produit SKF (skf.com) : elles peuvent changer d'une édition du catalogue à
l'autre, et d'un fabricant à l'autre. **À la calculatrice**, tapez 16,25 ^ ( 10 ÷ 3 ) : les **parenthèses
autour de 10 ÷ 3 sont obligatoires** — sans elles, la calculatrice élève à la puissance 10 puis divise par 3.*

[[FIG:charge_vie_catalogue]]

**La charge compte énormément.** Doubler P divise L10 par 2³ = **8** (billes), par 2^(10/3) ≈ **10**
(rouleaux). Inversement, alléger un peu un roulement allonge beaucoup sa vie.

### 4. Choisir un roulement pour une durée visée

On part de la **durée visée** (donnée par le cahier des charges, ou par les tableaux des catalogues selon
le type de machine) et on retourne la formule, en trois étapes : (C/P)ⁿ = L10 ; on « défait » la
puissance n en prenant la puissance 1/n des deux côtés, C/P = L10^(1/n) (pour n = 3, c'est la **racine
cubique**) ; on multiplie par P.

> **C requis = P × L10^(1/n)**, avec L10 = L10h × 60 × N / 10⁶

*Exemple : 20 000 h à 1 500 tr/min sous 2 kN. L10 = 20 000 × 60 × 1 500 / 10⁶ = **1 800 millions de
tours**. À billes : C requis = 2 × 1 800^(1/3) = 2 × 12,2 ≈ **24,3 kN** — le 6205 (14,8 kN) ne suffit pas,
il faut un roulement à billes plus chargeable dans le catalogue (de C ≥ 24,3 kN). À rouleaux (1/n =
3/10 = 0,3) : C requis = 2 × 1 800^(0,3) ≈ **19,0 kN** — le NU 205 ECP (32,5 kN) suffit… **si la charge est
purement radiale** : un roulement NU n'a pas d'épaulement sur sa bague intérieure, il ne tient pas d'effort
axial. C'est d'ailleurs ce qui en fait un excellent **palier libre** : la dilatation de l'arbre se fait dans
le roulement (fiche 6.6). Les variantes NJ et NUP, avec épaulements, tiennent un effort axial modéré.*

[[DYN:duree_roulement_curseurs]]

**Ce que le calcul ne dit pas.** L10 suppose une lubrification correcte et un roulement propre. Les
catalogues proposent une durée **corrigée**, qui tient compte de la propreté du lubrifiant et de la
fiabilité voulue : on la calcule avec les logiciels du fabricant, pas à la main. Pour un roulement qui
tourne très lentement ou qui reste chargé à l'arrêt (pivot de grue, palier d'une porte lourde), on vérifie
aussi la **charge statique de base C0** : la charge supportée sans tourner sans que les billes s'impriment
dans les pistes (catalogue).

### 5. Solutions constructives : la rotule et l'hélicoïdale

Une fois le roulement dimensionné, il reste à savoir **avec quel composant** réaliser les autres liaisons.
Deux cas reviennent souvent en bureau d'études : un arbre qui n'est pas parfaitement aligné (rotule), et
une translation commandée par une rotation (hélicoïdale).

[[FIG:rotule_helicoidale_solutions]]

| Liaison | Solution | À quoi elle sert |
|---|---|---|
| **rotule** | **roulement à rotule** (sur billes ou sur rouleaux) : piste extérieure sphérique | supporter un arbre qui fléchit ou des paliers mal alignés (arbres longs, bâtis soudés) |
| **rotule** | **embout à rotule, rotule lisse** | articuler un vérin ou une biellette qui travaille dans plusieurs plans |
| **hélicoïdale** | **vis trapézoïdale + écrou** (souvent en bronze) | simple, économique, souvent **irréversible** (pousser sur l'écrou ne fait pas tourner la vis, comme un cric à vis) ; jeu à rattraper, usure |
| **hélicoïdale** | **vis à billes** | rendement élevé, précise ; **réversible** (une charge sur l'écrou fait tourner la vis : frein sur un axe vertical, fiche 6.18) ; jeu supprimé par un écrou préchargé |

La loi v = ph × N (ph : pas de l'hélice, l'avance de l'écrou pour un tour) et la réversibilité sont en
fiche **6.18** ; le modèle de ces liaisons (rotule = 3 mouvements possibles, hélicoïdale = 1) en fiches
**6.1 et 6.17**. Ici, on choisit la **réalisation**.

### 6. Serrer une vis à la bonne précharge

[[FIG:precharge_vis]]

*Attention, ne pas confondre : dans cette fiche, **C** est la charge dynamique de base d'un roulement (en
kN) ; le couple de serrage d'une vis se note **Cs** (en N·m).*

La fiche 6.9 l'a montré : une vis serrée est une vis **tendue**. C'est sa tension, la **précharge F0**, qui
plaque les pièces et les empêche de bouger. Deux questions :

**1. La vis tient-elle cette précharge ?** On compare la contrainte dans sa section résistante à la limite
élastique de sa classe :

> **σ = F0 / As < Re**

- **As** : la **section résistante** du filetage (plus petite que π d² / 4, à cause des filets), donnée par
  la norme ISO 898-1 : M8 → **36,6 mm²** ; M10 → **58,0 mm²** ; M12 → **84,3 mm²** ;
- **Re** : la limite élastique de la classe (fiche 6.9) : classe 8.8 → 8 × 8 × 10 = **640 MPa** (la norme
  l'appelle Rp0,2).

**Avec une marge.** σ = F0 / As ne compte que la **traction**. Pendant le serrage, le couple tord aussi la
vis : la contrainte réelle est nettement plus haute que F0 / As. C'est pourquoi on ne vise jamais F0 / As
proche de Re.

**2. À quel couple serrer pour obtenir F0 ?** Un couple, c'est une force × un bras de levier. Pour tendre
la vis à F0, il faut vaincre des frottements qui augmentent avec F0, et qui agissent à une distance de
l'axe de l'ordre du diamètre. Le couple est donc proportionnel à F0 × d :

> **Cs ≈ 0,2 × d × F0** (d : diamètre nominal ; avec d en mm et F0 en N, Cs sort en N·mm : ÷ 1 000 pour des N·m)

**Le 0,2 n'est qu'un ordre de grandeur** (il correspond à des surfaces sèches ou peu huilées). Une grande
partie du couple de serrage part en **frottement** : sous la tête (ou l'écrou) et dans les filets ; le reste
seulement tend la vis. **Vis graissée : le coefficient baisse** — le même couple tend alors davantage la
vis, jusqu'à dépasser Re : elle s'allonge **définitivement**, comme un ressort trop tiré, perd sa précharge
ou casse au resserrage. **Surfaces sèches ou rugueuses : il monte** — la vis est moins serrée qu'on ne croit.
Pour un serrage précis, on utilise les **tables de couples du fabricant de visserie** pour la lubrification
réelle, et on serre à la **clé dynamométrique**.

*Exemple : vis M10 classe 8.8, précharge visée F0 = 25 kN (donnée du bureau d'études). σ = 25 000 / 58 ≈
**431 MPa** < 640 MPa : en **traction seule**, la vis est à 67 % de Re — la torsion de serrage s'y ajoute.
Couple : Cs ≈ 0,2 × 10 × 25 000 = 50 000 N·mm = **50 N·m** — ordre de grandeur. Sur une vis huilée, ce même
couple tendrait davantage la vis et pourrait l'amener près de sa limite : le couple réel se prend dans la
table du fabricant, pour la lubrification réelle.*

### 7. Les erreurs classiques

1. **Se tromper d'exposant** : 3 pour les billes, **10/3** pour les rouleaux.
2. **Oublier que L10 est en millions de tours** : la conversion en heures est L10 × 10⁶ / (60 N).
3. **Prendre P = Fr quand il y a un effort axial** : P = X Fr + Y Fa, avec X et Y du catalogue.
4. **Inventer C** : la charge dynamique de base se lit au catalogue, pour **la marque et la référence
   exactes** — elle change d'un fabricant à l'autre et d'une génération à l'autre (les valeurs de la fiche
   10.1 ne sont qu'un exemple de lecture).
5. **Choisir un NU pour un effort axial** : un roulement à rouleaux cylindriques NU ne tient pas d'axial.
6. **Prendre la section nominale π d² / 4** au lieu de la section résistante As.
7. **Prendre Cs ≈ 0,2 × d × F0 pour une valeur exacte** : c'est un ordre de grandeur, qui dépend du
   frottement. Et oublier que la torsion de serrage s'ajoute à F0 / As.

### 8. À retenir

- **L10 = (C/P)ⁿ** en millions de tours, **n = 3 (billes), 10/3 (rouleaux)** ; **L10h = L10 × 10⁶ / (60 N)**.
- L10 : durée atteinte par **90 %** des roulements. **C** : charge pour L10 = 1 million de tours, lue au
  **catalogue**. **P = Fr**, ou X Fr + Y Fa avec X, Y du catalogue.
- Doubler la charge divise la vie par **8** (billes). **C requis = P × L10^(1/n)**.
- Rotule : roulement à rotule, embout à rotule. Hélicoïdale : vis trapézoïdale ou à billes (fiche 6.18).
- Vis : **σ = F0 / As < Re**, avec une marge (la torsion de serrage s'ajoute) ; couple **Cs ≈ 0,2 × d × F0**,
  **ordre de grandeur** qui dépend du frottement.
""",
    "formules": """
**Durée de vie (ISO 281)** — L10 = (C / P)ⁿ (millions de tours) · n = 3 (billes), 10/3 (rouleaux) ·
L10h = L10 × 10⁶ / (60 × N)

**Charge équivalente** — P = Fr (radiale pure) · P = X × Fr + Y × Fa (X, Y : catalogue ou énoncé)

**Choix pour une durée visée** — L10 = L10h × 60 × N / 10⁶ · C requis = P × L10^(1/n)

**Vis : précharge** — σ = F0 / As < Re, avec une marge (torsion de serrage) · As (ISO 898-1) : M8 36,6 mm²,
M10 58,0 mm², M12 84,3 mm² · classe 8.8 : Re = 640 MPa

**Couple de serrage** — Cs ≈ 0,2 × d × F0 : **ordre de grandeur**, le coefficient dépend du frottement
""",
    "exemple": """
### Cas industriel — Le roulement qui tenait 9 mois au lieu de 3 ans

**Le symptôme.** Un ventilateur de séchage tourne à 1 500 tr/min, 16 h par jour. Le roulement côté turbine,
un SKF 6205 (C = 14,8 kN), devait durer plus de trois ans ; il lâche au bout de neuf mois. Le lot suivant
fait pareil : ce n'est pas un défaut de fabrication.

**Ce qu'annonçait le calcul de conception.** L'effort sur le roulement avait été estimé à **1,2 kN** :
L10 = (14,8 / 1,2)³ ≈ 1 880 millions de tours, soit L10h = 1 880 × 10⁶ / (60 × 1 500) ≈ **20 800 h**. À 16 h
par jour, cela fait environ 1 300 jours : **3,6 ans**. D'où l'attente de la maintenance.

**Ce qui se passe vraiment.** La turbine s'encrasse : la poussière collée d'un seul côté des pales décentre
la masse — un **balourd**. À chaque tour, la turbine « tire » sur l'arbre comme une machine à laver qui
essore avec le linge en boule, et cet effort s'ajoute. Mesuré sur site, l'effort atteint **2 kN** :
L10 = (14,8 / 2)³ ≈ 405 millions de tours, soit **4 500 h** — environ 280 jours à 16 h par jour : **neuf
mois**. Exactement la durée observée.

**Ce que le calcul montre.** L'effort n'a augmenté que de 67 %, mais la durée de vie a été divisée par
(2 / 1,2)³ ≈ **4,6**. C'est l'exposant 3 qui rend le roulement si sensible à la charge.

**Les corrections**, par ordre d'efficacité :

| Action | Effet |
|---|---|
| **nettoyer et équilibrer la turbine**, puis contrôler la vibration | supprime la surcharge à la source |
| choisir un roulement de C plus grand au catalogue, pour la charge réelle | marge sur la charge |
| estimer la durée attendue par la durée **corrigée** (logiciel du fabricant), avec la vraie lubrification | une attente réaliste pour la maintenance |

**Ce que le cas apprend.** Une durée de vie se calcule avec la **charge réelle**, pas avec la charge
nominale du cahier des charges. Et une petite surcharge coûte cher : l'exposant amplifie tout.
""",
    "exercice": """
### Exercice — Le palier d'un tambour de convoyeur

Un tambour de convoyeur tourne à **960 tr/min**. Chaque palier reçoit un effort **radial** de **1,6 kN**
(pas d'effort axial sur ce palier). Le bureau d'études propose un roulement **SKF 6205** (catalogue SKF :
C = 14,8 kN). Le cahier des charges demande **20 000 h** de durée de vie L10.

**1.** Quelle est la charge équivalente P ? Pourquoi ?

**2.** Calculez L10, en millions de tours.

**3.** Calculez L10h. Le 6205 convient-il ?

**4.** Quelle charge dynamique de base C faudrait-il au minimum pour atteindre 20 000 h avec un roulement à
billes ?

**5.** Le SKF NU 205 ECP (rouleaux cylindriques, même encombrement, C = 32,5 kN) conviendrait-il ici ?
Calculez sa durée de vie et dites à quelle condition on peut le monter.

**6.** Le palier est fixé au bâti par deux vis M10 classe 8.8, serrées à une précharge F0 = 20 kN.
Vérifiez la contrainte dans les vis et donnez l'ordre de grandeur du couple de serrage.
""",
    "corrige": """
### Corrigé, en six temps

#### 1. Ce que dit l'énoncé

Un roulement à billes de catalogue (C = 14,8 kN), une charge radiale pure de 1,6 kN, 960 tr/min, une
durée visée de 20 000 h. Puis une alternative à rouleaux, et le serrage du palier.

#### 2. Quelle règle, et pourquoi

> **L10 = (C/P)ⁿ**, n = 3 (billes), 10/3 (rouleaux) ; **L10h = L10 × 10⁶ / (60 N)** ; **C requis =
> P × L10^(1/n)**. Vis : **σ = F0 / As < Re** (avec une marge) ; couple **Cs ≈ 0,2 × d × F0** (ordre de grandeur).

#### 3. Les conversions

P en kN comme C (seul le rapport compte). L10 en millions de tours. As = 58,0 mm² (M10, ISO 898-1) ;
couple en N·mm puis N·m.

#### 4. Le remplacement

L10 = (14,8 / 1,6)³. L10h = L10 × 10⁶ / (60 × 960). L10 visé = 20 000 × 60 × 960 / 10⁶ = 1 152.
C requis = 1,6 × 1 152^(1/3). Rouleaux : L10 = (32,5 / 1,6)^(10/3). Vis : σ = 20 000 / 58 ; Cs ≈ 0,2 × 10 ×
20 000.

#### 5. Le calcul

**1.** Effort radial seul : **P = Fr = 1,6 kN**.

**2.** L10 = (14,8 / 1,6)³ = 9,25³ ≈ **791 millions de tours**.

**3.** L10h = 791 × 10⁶ / (60 × 960) ≈ **13 700 h** < 20 000 h : **le 6205 ne convient pas**.

**4.** L10 visé = 1 152 millions de tours ; C requis = 1,6 × 1 152^(1/3) = 1,6 × 10,5 ≈ **16,8 kN** : il
faut un roulement à billes de C ≥ 16,8 kN, à choisir au catalogue.

**5.** L10 = (32,5 / 1,6)^(10/3) = 20,31^(10/3) ≈ 22 900 millions de tours ; L10h ≈ **397 000 h** : très
large. **Condition** : la charge doit rester purement radiale, car un NU ne tient pas d'effort axial. Sur ce
palier (aucun effort axial), c'est possible ; l'autre palier, lui, devra arrêter l'arbre axialement
(règle des montages, fiche 6.6).

**6.** σ = 20 000 / 58 ≈ **345 MPa** < 640 MPa : en traction seule, les vis sont à 54 % de Re, ce qui
laisse la marge nécessaire pour la torsion de serrage. Couple Cs ≈ 0,2 × 10 × 20 000 = 40 000 N·mm ≈
**40 N·m**, **ordre de grandeur** à confirmer dans la table du fabricant de visserie.

#### 6. La vérification

**Sensibilité** : il manque 20 000 / 13 700 ≈ 1,46 fois la durée. Comme la durée varie comme C³, il faut
multiplier C par la racine cubique de 1,46, soit environ 1,13 : 14,8 × 1,13 ≈ 16,8 kN. On retrouve la
question 4. **Bon sens** : un
roulement à rouleaux de même taille porte beaucoup plus, mais seulement en radial — c'est pourquoi on ne
le choisit pas par réflexe.
""",
}

# ===========================================================================
# 3. MÉTHODE
# ===========================================================================
MTH_6_19 = ("6.19", "Vérifier un roulement pour une durée de vie visée", [
    "**Calculer la charge équivalente P** : P = Fr si l'effort est radial ; sinon P = X Fr + Y Fa, "
    "avec X et Y lus au catalogue (ou donnés).",
    "**Lire C au catalogue**, pour la référence exacte du roulement (C change d'une génération à "
    "l'autre).",
    "**Calculer L10 = (C/P)ⁿ** en millions de tours, avec **n = 3 (billes)** ou **10/3 (rouleaux)**.",
    "**Convertir en heures** : L10h = L10 × 10⁶ / (60 N), et comparer à la durée visée.",
    "**Si c'est trop court**, calculer C requis = P × L10^(1/n) et choisir au catalogue ; vérifier "
    "que le type choisi accepte les efforts (un NU ne tient pas d'axial).",
], "Palier à 960 tr/min, P = 1,6 kN, SKF 6205 (C = 14,8 kN, catalogue SKF) : L10 = 9,25³ ≈ 791 "
   "millions de tours, L10h ≈ 13 700 h < 20 000 h. C requis = 1,6 × 1 152^(1/3) ≈ 16,8 kN.")

# ===========================================================================
# 4. ATELIERS (fin de liste ATELIERS, après at163)
# ===========================================================================
ATELIERS_NOUVEAUX = [
    {
        "id": "at164",
        "chapitre": "Bloc 6",
        "titre": "Moteur de pompe : le SKF 6205 tiendra-t-il 20 000 heures ?",
        "theme": "Roulements",
        "fiche": "6.19",
        "figure": "duree_vie_dispersion",
        "vocabulaire": [
            ("L10",
             "la durée de vie, en millions de tours, atteinte ou dépassée par 90 % des roulements d'un lot."),
            ("Charge dynamique de base C",
             "la charge pour laquelle L10 vaut 1 million de tours ; elle se lit au catalogue du fabricant."),
            ("Charge équivalente P",
             "la charge réellement subie par le roulement, ramenée à un effort radial unique."),
        ],
        "enonce": "Le roulement côté accouplement d'un moteur de pompe est un SKF 6205, à billes (catalogue "
                  "SKF : C = 14,8 kN). Il porte un effort radial pur de 2,5 kN, à 720 tr/min. On vise "
                  "une durée de vie L10 de 20 000 heures.",
        "etapes": [
            {"type": "numerique", "label": "L10 en millions de tours",
             "unite": "millions de tours", "attendu": 207.47, "tol": 1,
             "consigne": "Calcule L10 = (C / P)ⁿ, avec l'exposant qui convient à un roulement à billes.",
             "indice": "Billes : n = 3. C / P = 14,8 / 2,5 = 5,92.",
             "pieges": [(375.32, "375 : tu as pris l'exposant 10/3, celui des rouleaux. Pour des billes, "
                                 "n = 3."),
                        (5.92, "5,92, c'est C / P. Il faut l'élever à la puissance 3.")],
             "aide": "L10 = 5,92³ ≈ 207,5 millions de tours."},
            {"type": "numerique", "label": "L10 en heures",
             "unite": "h", "attendu": 4802.7, "tol": 30,
             "consigne": "Convertis en heures : L10h = L10 × 10⁶ / (60 × N).",
             "indice": "207,5 × 10⁶ / (60 × 720).",
             "depend_de": {"etape": 1, "formule": lambda v: v * 1e6 / (60 * 720)},
             "pieges": [(288159, "288 000 : tu n'as pas divisé par 60. N est en tours par MINUTE, et on "
                                 "veut des heures."),
                        (207.47, "207, c'est encore L10 en millions de tours : il faut le convertir.")],
             "aide": "L10h = 207,5 × 10⁶ / 43 200 ≈ 4 803 h."},
            {"type": "qcm", "label": "Verdict",
             "question": "4 800 h pour 20 000 h visées. Que conclure ?",
             "options": ["Le roulement convient : 4 800 h, c'est déjà beaucoup",
                         "Il ne convient pas : sa durée L10 est environ quatre fois trop courte",
                         "Il convient, car 90 % des roulements dépassent L10"], "bonne": 1,
             "indice": "Comparer L10h à la durée visée.",
             "diagnostics": {0: "La référence, c'est la durée visée (20 000 h), pas une impression.",
                             2: "Justement : L10 est la durée que 90 % atteignent. À 4 800 h, déjà 10 % "
                                "des roulements ont lâché ; à 20 000 h, bien davantage."}},
            {"type": "numerique", "label": "C requis",
             "unite": "kN", "attendu": 23.81, "tol": 0.3,
             "consigne": "Quelle charge dynamique de base faudrait-il, à billes, pour atteindre 20 000 h ? "
                         "(L10 visé = 20 000 × 60 × 720 / 10⁶ = 864 millions de tours.)",
             "indice": "C requis = P × L10^(1/3) = 2,5 × 864^(1/3).",
             "pieges": [(2160, "2 160 : tu as multiplié P par L10. Il faut la racine cubique de L10 : "
                               "C = P × L10^(1/3)."),
                        (19.01, "19,0 : tu as pris 1/n = 0,3, celui des rouleaux. Billes : racine cubique, "
                                "L10^(1/3).")],
             "aide": "864^(1/3) ≈ 9,52 ; C ≈ 2,5 × 9,52 ≈ 23,8 kN."},
            {"type": "qcm", "label": "Que choisir ?",
             "question": "Le SKF NU 205 ECP (rouleaux, même encombrement, C = 32,5 kN) aurait la capacité. "
                         "Peut-on le monter côté accouplement d'un moteur ?",
             "options": ["Oui, sans condition : C est plus grand",
                         "Oui, seulement si ce palier ne reçoit aucun effort axial : un NU n'en tient pas",
                         "Non, un roulement à rouleaux ne peut jamais remplacer un roulement à billes"],
             "bonne": 1,
             "indice": "Que tient, et que ne tient pas, un roulement à rouleaux cylindriques NU ?",
             "diagnostics": {0: "C ne dit pas tout : un NU n'a pas d'épaulement sur sa bague intérieure, il "
                                 "ne tient aucun effort axial.",
                             2: "Il le peut, pour un effort purement radial — l'autre palier arrêtant "
                                "l'arbre axialement."}},
        ],
        "corrige": {
            "enonce": "SKF 6205 (C = 14,8 kN), P = 2,5 kN radial, 720 tr/min, durée visée 20 000 h.",
            "regle": "**L10 = (C/P)³** (billes), **L10h = L10 × 10⁶ / (60 N)**, **C requis = P × "
                    "L10^(1/3)**.",
            "conversions": "L10 visé = 20 000 × 60 × 720 / 10⁶ = 864 millions de tours.",
            "remplacement": "L10 = (14,8 / 2,5)³ ; L10h = L10 × 10⁶ / 43 200 ; C = 2,5 × 864^(1/3).",
            "calcul": "**L10 ≈ 207,5 millions de tours** ; **L10h ≈ 4 803 h** : insuffisant ; **C requis ≈ 23,8 kN**.",
            "verification": "Rapport des durées : 20 000 / 4 803 ≈ 4,16 ; racine cubique ≈ 1,61 ; "
                            "14,8 × 1,61 ≈ 23,8 kN : même résultat par la sensibilité.",
        },
        "a_retenir": "À retenir : L10 = (C/P)³ pour des billes, en millions de tours ; on convertit en "
                     "heures avant de comparer à la durée visée.",
    },
    {
        "id": "at165",
        "chapitre": "Bloc 6",
        "titre": "Fixation d'un palier : précharge et couple de serrage d'une vis M10",
        "theme": "Visserie",
        "fiche": "6.19",
        "figure": "precharge_vis",
        "vocabulaire": [
            ("Précharge F0",
             "la tension de la vis serrée : c'est elle qui plaque les pièces (fiche 6.9)."),
            ("Section résistante As",
             "la section qui travaille dans un filetage, plus petite que π d² / 4 ; donnée par la norme "
             "ISO 898-1."),
            ("Classe 8.8",
             "Rm (résistance à la rupture) = 8 × 100 = 800 MPa ; Re (limite élastique : au-delà, la vis "
             "reste allongée) = 8 × 8 × 10 = 640 MPa."),
        ],
        "enonce": "Un palier est fixé par des vis M10 de classe 8.8 (section résistante As = 58,0 mm², ISO "
                  "898-1). Le bureau d'études vise une précharge F0 = 25 kN par vis.",
        "etapes": [
            {"type": "numerique", "label": "Limite élastique",
             "unite": "MPa", "attendu": 640, "tol": 1,
             "consigne": "Quelle est la limite élastique Re d'une vis de classe 8.8 ?",
             "indice": "Re = premier chiffre × second chiffre × 10.",
             "pieges": [(800, "800 MPa, c'est Rm (8 × 100). La limite élastique vaut 8 × 8 × 10.")],
             "aide": "Re = 8 × 8 × 10 = 640 MPa."},
            {"type": "numerique", "label": "Contrainte dans la vis",
             "unite": "MPa", "attendu": 431.03, "tol": 2,
             "consigne": "Calcule σ = F0 / As.",
             "indice": "25 000 / 58,0.",
             "pieges": [(318.31, "318 MPa : tu as pris la section nominale π × 10² / 4 = 78,5 mm². Le "
                                 "filetage travaille sur sa section résistante As = 58,0 mm².")],
             "aide": "σ = 25 000 / 58 ≈ 431 MPa."},
            {"type": "qcm", "label": "La vis tient-elle ?",
             "question": "σ ≈ 431 MPa pour Re = 640 MPa. Que conclure ?",
             "options": ["La vis casse",
                         "La vis tient en traction (environ 67 % de Re) ; la torsion de serrage s'y ajoute, "
                         "d'où la marge",
                         "On ne peut pas conclure sans le couple de serrage"], "bonne": 1,
             "indice": "Comparer σ à Re.",
             "diagnostics": {0: "431 < 640 : la vis reste dans son domaine élastique.",
                             2: "La tenue se juge sur la précharge (σ = F0 / As) ; le couple sert ensuite "
                                "à obtenir cette précharge."}},
            {"type": "numerique", "label": "Couple de serrage (ordre de grandeur)",
             "unite": "N·m", "attendu": 50, "tol": 1,
             "consigne": "Donne l'ordre de grandeur du couple de serrage : Cs ≈ 0,2 × d × F0, en N·m.",
             "indice": "0,2 × 10 mm × 25 000 N, en N·mm, puis divise par 1 000.",
             "pieges": [(50000, "50 000, c'est en N·mm : divise par 1 000 pour des N·m."),
                        (0.05, "0,05 : tu as mis d en mètres ET divisé par 1 000. Garde d = 10 mm, "
                               "puis convertis les N·mm en N·m.")],
             "aide": "Cs ≈ 0,2 × 10 × 25 000 = 50 000 N·mm = 50 N·m."},
            {"type": "qcm", "label": "Vis graissée",
             "question": "Le monteur graisse les vis et serre quand même à 50 N·m. Que se passe-t-il ?",
             "options": ["Rien : le couple est le même, donc la précharge aussi",
                         "La précharge est plus faible : le graissage fait glisser",
                         "La précharge est plus forte : le frottement baisse, le même couple tend "
                         "davantage la vis"], "bonne": 2,
             "indice": "Une grande partie du couple part en frottement. Que devient-elle si on graisse ?",
             "diagnostics": {0: "Le couple n'est qu'un moyen : la part qui tend la vis dépend du "
                                 "frottement.",
                             1: "C'est l'inverse : moins de frottement, donc plus de couple disponible "
                                "pour tendre la vis. Elle peut alors dépasser sa limite."}},
        ],
        "corrige": {
            "enonce": "Vis M10 classe 8.8, As = 58,0 mm², F0 visée = 25 kN.",
            "regle": "**σ = F0 / As < Re**, avec une marge ; **Cs ≈ 0,2 × d × F0** (ordre de grandeur, "
                    "dépend du frottement).",
            "conversions": "Cs en N·mm → N·m : ÷ 1 000.",
            "remplacement": "Re = 8 × 8 × 10 ; σ = 25 000 / 58 ; Cs = 0,2 × 10 × 25 000.",
            "calcul": "**Re = 640 MPa** ; **σ ≈ 431 MPa** (67 % de Re, en traction seule) ; **Cs ≈ 50 N·m**.",
            "verification": "Le 0,2 n'est qu'un ordre de grandeur : la table du fabricant de visserie, "
                            "pour la lubrification réelle, donne le couple à appliquer. Pendant le serrage, "
                            "la torsion s'ajoute à la traction : 67 % de Re en traction seule ne laisse pas "
                            "une si grande marge. Un graissage non prévu augmente la précharge pour le même "
                            "couple.",
        },
        "a_retenir": "À retenir : on vérifie la vis sur sa précharge (σ = F0 / As < Re, avec une marge), "
                     "puis on cherche le couple qui donne cette précharge — Cs ≈ 0,2 × d × F0 n'est qu'un "
                     "ordre de grandeur.",
    },
]

# ===========================================================================
# 5. GÉNÉRATEUR (nouvelle famille « Roulements »)
# ===========================================================================
GENERATEUR = '''
def gen_duree_roulement():
    """Durée de vie L10h d'un roulement de catalogue SKF (6205 billes, NU 205 ECP rouleaux)."""
    nom, C, n, type_ = random.choice([("SKF 6205", 14.8, 3, "à billes"),
                                      ("SKF NU 205 ECP", 32.5, 10 / 3, "à rouleaux cylindriques")])
    # charges réalistes pour chaque roulement (des durées de plusieurs siècles n'apprennent rien)
    P = random.choice([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0] if n == 3 else [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
    N = random.choice([500, 720, 960, 1000, 1450, 1500, 2900])
    L10 = (C / P) ** n
    L10h = L10 * 1e6 / (60 * N)
    autre_n = 10 / 3 if n == 3 else 3
    tol = max(1.0, L10h * 0.01)
    diag = []
    for val, msg in (
            ((C / P) ** autre_n * 1e6 / (60 * N),
             "Tu as pris le mauvais exposant : 3 pour les billes, 10/3 pour les rouleaux."),
            (L10, "C'est L10 en millions de tours. Convertis : L10h = L10 × 10⁶ / (60 × N)."),
            (L10 * 1e6 / N, "Tu n'as pas divisé par 60 : N est en tours par minute, on veut des heures."),
            ((C / P) * 1e6 / (60 * N), "Tu as oublié l'exposant : L10 = (C / P)ⁿ."),
    ):
        if abs(val - L10h) > tol and all(abs(val - d["v"]) > tol for d in diag):
            diag.append(_diag(round(val, 1), msg))
    return {
        "titre": "Roulements — durée de vie L10h",
        "enonce": (f"Un roulement **{nom}**, {type_} (catalogue SKF : C = {fr(C, 1)} kN), porte une charge "
                   f"équivalente **P = {fr(P, 1)} kN** à **{N} tr/min**. Quelle est sa durée de vie L10h, "
                   "en heures ?"),
        "rep": round(L10h, 1), "tol": tol, "unite": "h",
        "diag": diag,
        "corr": [
            f"**Ce que dit l'énoncé.** Un roulement {type_} de C = {fr(C, 1)} kN, sous P = {fr(P, 1)} kN, "
            f"à {N} tr/min. On cherche L10h.",
            f"**L'exposant.** Roulement {type_} : n = {'3' if n == 3 else '10/3'}.",
            f"**L10 en millions de tours.** L10 = (C / P)ⁿ = ({fr(C, 1)} / {fr(P, 1)})^"
            f"{'3' if n == 3 else '(10/3)'} = {fr(L10, 1)} millions de tours.",
            f"**En heures.** L10h = L10 × 10⁶ / (60 × N) = {fr(L10, 1)} × 10⁶ / (60 × {N}) = "
            f"{fr(L10h, 0)} h.",
            "**Je vérifie.** Doubler la charge diviserait cette durée par "
            + ("8 (2³)." if n == 3 else "environ 10 (2^(10/3))."),
        ],
        "indice": "L10 = (C / P)ⁿ, n = 3 (billes) ou 10/3 (rouleaux), puis L10h = L10 × 10⁶ / (60 × N).",
    }
'''

# ===========================================================================
# 6. QUIZ — nouvelle catégorie « Roulements et visserie : dimensionner »
#    positions de la bonne réponse : 0, 2, 1, 3, 2, 0, 3, 1
# ===========================================================================
QUIZ_ROULEMENTS = [
    ("Que représente la durée de vie L10 d'un roulement ?",
     ["La durée atteinte ou dépassée par 90 % des roulements d'un lot",
      "La durée garantie de chaque roulement", "La durée moyenne d'un lot",
      "Dix fois la durée d'un roulement neuf"], 0,
     "L10 est une notion statistique : 90 % des roulements d'un lot l'atteignent ou la dépassent, 10 % "
     "lâchent avant. Ce n'est ni une garantie, ni une moyenne.", "Base"),
    ("Quel exposant utiliser dans L10 = (C/P)ⁿ pour un roulement à rouleaux ?",
     ["2", "3", "10/3", "1"], 2,
     "n = 3 pour les roulements à billes (contact ponctuel), n = 10/3 pour les roulements à rouleaux "
     "(contact linéique).", "Base"),
    ("On double la charge P d'un roulement à billes. Sa durée de vie L10 :",
     ["est divisée par 2", "est divisée par 8", "ne change pas", "est divisée par 3"], 1,
     "L10 = (C/P)³ : doubler P divise L10 par 2³ = 8. C'est pourquoi une petite surcharge (un balourd, "
     "un désalignement) raccourcit tant la vie d'un roulement.", "Intermédiaire"),
    ("Où trouve-t-on la charge dynamique de base C d'un roulement ?",
     ["On la calcule à partir de la charge appliquée", "Elle vaut toujours 10 kN",
      "C'est la masse du roulement multipliée par g", "Dans le catalogue du fabricant, pour la référence exacte"], 3,
     "C est une caractéristique du roulement, établie par le fabricant et lue dans son catalogue. Elle "
     "peut changer d'une génération de roulement à l'autre : on la lit pour la référence exacte.", "Base"),
    ("Un SKF 6205 (C = 14,8 kN) porte 2 kN à 1 500 tr/min. Sa durée L10h vaut environ :",
     ["405 h", "120 000 h", "4 500 h", "270 000 h"], 2,
     "L10 = (14,8/2)³ = 405 millions de tours ; L10h = 405 × 10⁶ / (60 × 1 500) ≈ 4 500 h. 405 est L10 "
     "en millions de tours, pas en heures.", "Calcul"),
    ("Peut-on monter un roulement à rouleaux cylindriques NU sur un palier qui reçoit un effort axial ?",
     ["Non : sa bague intérieure n'a pas d'épaulement, il ne tient pas d'effort axial",
      "Oui, il est plus chargeable qu'un roulement à billes", "Oui, si on le graisse",
      "Oui, à condition de serrer davantage l'écrou"], 0,
     "Un NU porte de fortes charges radiales mais laisse la bague intérieure coulisser : aucun effort axial. "
     "Un C élevé ne suffit pas : le type doit accepter les efforts.", "Intermédiaire"),
    ("Pourquoi vérifie-t-on une vis sur sa section résistante As plutôt que sur π d² / 4 ?",
     ["Parce que As est plus grande", "Par convention, sans raison",
      "Parce que π d² / 4 ne s'applique qu'aux vis en inox",
      "Parce que le filetage réduit la section qui travaille réellement"], 3,
     "Les filets enlèvent de la matière : la section qui travaille est plus petite que la section nominale. "
     "La norme ISO 898-1 donne As (M10 : 58,0 mm², contre 78,5 mm² en nominal).", "Base"),
    ("La formule Cs ≈ 0,2 × d × F0 donne le couple de serrage :",
     ["exactement, pour toutes les vis",
      "en ordre de grandeur seulement : le coefficient dépend du frottement (lubrification, état des surfaces)",
      "seulement pour les vis graissées", "seulement pour les vis de classe 12.9"], 1,
     "Une grande partie du couple part en frottement sous la tête et dans les filets. Le coefficient varie "
     "donc avec la lubrification : pour un serrage précis, on utilise les tables du fabricant et une clé "
     "dynamométrique.", "Intermédiaire"),
]
