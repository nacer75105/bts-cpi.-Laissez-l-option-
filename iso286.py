"""
Tables ISO 286 : degrés de tolérance normalisés (IT) et écarts fondamentaux.
Toutes les valeurs sont en micromètres (µm).
Source : ISO 286-1 / ISO 286-2 (domaine 0 à 500 mm).
"""

# --- Tranches de dimensions nominales pour les valeurs IT (mm) ---
TRANCHES_IT = [
    (0, 3), (3, 6), (6, 10), (10, 18), (18, 30), (30, 50), (50, 80),
    (80, 120), (120, 180), (180, 250), (250, 315), (315, 400), (400, 500),
]

GRADES_IT = ["IT1", "IT2", "IT3", "IT4", "IT5", "IT6", "IT7", "IT8",
             "IT9", "IT10", "IT11", "IT12", "IT13", "IT14", "IT15", "IT16"]

# Valeurs IT en µm, une ligne par tranche de TRANCHES_IT
TABLE_IT = {
    (0, 3):     [0.8, 1.2, 2, 3, 4, 6, 10, 14, 25, 40, 60, 100, 140, 250, 400, 600],
    (3, 6):     [1, 1.5, 2.5, 4, 5, 8, 12, 18, 30, 48, 75, 120, 180, 300, 480, 750],
    (6, 10):    [1, 1.5, 2.5, 4, 6, 9, 15, 22, 36, 58, 90, 150, 220, 360, 580, 900],
    (10, 18):   [1.2, 2, 3, 5, 8, 11, 18, 27, 43, 70, 110, 180, 270, 430, 700, 1100],
    (18, 30):   [1.5, 2.5, 4, 6, 9, 13, 21, 33, 52, 84, 130, 210, 330, 520, 840, 1300],
    (30, 50):   [1.5, 2.5, 4, 7, 11, 16, 25, 39, 62, 100, 160, 250, 390, 620, 1000, 1600],
    (50, 80):   [2, 3, 5, 8, 13, 19, 30, 46, 74, 120, 190, 300, 460, 740, 1200, 1900],
    (80, 120):  [2.5, 4, 6, 10, 15, 22, 35, 54, 87, 140, 220, 350, 540, 870, 1400, 2200],
    (120, 180): [3.5, 5, 8, 12, 18, 25, 40, 63, 100, 160, 250, 400, 630, 1000, 1600, 2500],
    (180, 250): [4.5, 7, 10, 14, 20, 29, 46, 72, 115, 185, 290, 460, 720, 1150, 1850, 2900],
    (250, 315): [6, 8, 12, 16, 23, 32, 52, 81, 130, 210, 320, 520, 810, 1300, 2100, 3200],
    (315, 400): [7, 9, 13, 18, 25, 36, 57, 89, 140, 230, 360, 570, 890, 1400, 2300, 3600],
    (400, 500): [8, 10, 15, 20, 27, 40, 63, 97, 155, 250, 400, 630, 970, 1550, 2500, 4000],
}

# --- Tranches fines utilisées pour les écarts fondamentaux (mm) ---
TRANCHES_EF = [
    (0, 3), (3, 6), (6, 10), (10, 14), (14, 18), (18, 24), (24, 30),
    (30, 40), (40, 50), (50, 65), (65, 80), (80, 100), (100, 120),
    (120, 140), (140, 160), (160, 180), (180, 200), (200, 225), (225, 250),
    (250, 280), (280, 315), (315, 355), (355, 400), (400, 450), (450, 500),
]

# Écarts fondamentaux des ARBRES (lettres minuscules), en µm.
# Pour a..h  -> il s'agit de l'écart SUPÉRIEUR es (négatif ou nul)
# Pour k..zc -> il s'agit de l'écart INFÉRIEUR ei (positif ou nul)
ECARTS_ARBRE = {
    "c": [-60, -70, -80, -95, -95, -110, -110, -120, -130, -140, -150, -170, -180,
          -200, -210, -230, -240, -260, -280, -300, -330, -360, -400, -440, -480],
    "d": [-20, -30, -40, -50, -50, -65, -65, -80, -80, -100, -100, -120, -120,
          -145, -145, -145, -170, -170, -170, -190, -190, -210, -210, -230, -230],
    "e": [-14, -20, -25, -32, -32, -40, -40, -50, -50, -60, -60, -72, -72,
          -85, -85, -85, -100, -100, -100, -110, -110, -125, -125, -135, -135],
    "f": [-6, -10, -13, -16, -16, -20, -20, -25, -25, -30, -30, -36, -36,
          -43, -43, -43, -50, -50, -50, -56, -56, -62, -62, -68, -68],
    "g": [-2, -4, -5, -6, -6, -7, -7, -9, -9, -10, -10, -12, -12,
          -14, -14, -14, -15, -15, -15, -17, -17, -18, -18, -20, -20],
    "h": [0] * 25,
    "js": [0] * 25,   # cas particulier : tolérance symétrique ± IT/2
    "k": [0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3,
          3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5],   # valable pour IT4 à IT7
    "m": [2, 4, 6, 7, 7, 8, 8, 9, 9, 11, 11, 13, 13,
          15, 15, 15, 17, 17, 17, 20, 20, 21, 21, 23, 23],
    "n": [4, 8, 10, 12, 12, 15, 15, 17, 17, 20, 20, 23, 23,
          27, 27, 27, 31, 31, 31, 34, 34, 37, 37, 40, 40],
    "p": [6, 12, 15, 18, 18, 22, 22, 26, 26, 32, 32, 37, 37,
          43, 43, 43, 50, 50, 50, 56, 56, 62, 62, 68, 68],
    "r": [10, 15, 19, 23, 23, 28, 28, 34, 34, 41, 43, 51, 54,
          63, 65, 68, 77, 80, 84, 94, 98, 108, 114, 126, 132],
    "s": [14, 19, 23, 28, 28, 35, 35, 43, 43, 53, 59, 71, 79,
          92, 100, 108, 122, 130, 140, 158, 170, 190, 208, 232, 252],
    "u": [18, 23, 28, 33, 33, 41, 48, 60, 70, 87, 102, 124, 144,
          170, 190, 210, 236, 258, 284, 315, 350, 390, 435, 490, 540],
}

LETTRES_ARBRE = ["c", "d", "e", "f", "g", "h", "js", "k", "m", "n", "p", "r", "s", "u"]
LETTRES_ALESAGE = [l.upper() for l in LETTRES_ARBRE]

# Ajustements recommandés courants (ISO 286 - système de l'alésage normal H)
AJUSTEMENTS_COURANTS = {
    "H7/g6": ("Jeu", "Glissement juste, pièce démontable à la main. Pige de centrage, coulisseau précis."),
    "H7/h6": ("Jeu quasi nul", "Glissement gras. Assemblage se faisant à la main, sans jeu perceptible."),
    "H7/f7": ("Jeu", "Rotation lente ou alternative bien lubrifiée. Paliers lisses, axes de bielle."),
    "H8/e8": ("Jeu", "Rotation rapide avec bonne lubrification. Paliers de moteurs."),
    "H9/d9": ("Jeu large", "Rotation rapide, échauffement, mauvais alignement toléré."),
    "H11/c11": ("Jeu très large", "Assemblage grossier, chape mécano-soudée, pièces peintes."),
    "H7/k6": ("Incertain", "Mise en place au maillet. Poulies, engrenages démontables, bagues de roulement."),
    "H7/m6": ("Incertain / léger serrage", "Montage à la presse, démontage possible. Moyeux d'engrenage."),
    "H7/n6": ("Serrage léger", "Montage à la presse. Bagues, canons de perçage."),
    "H7/p6": ("Serrage", "Montage à la presse ou par dilatation. Goupilles, bagues de guidage."),
    "H7/s6": ("Serrage fort", "Montage à chaud obligatoire. Couronne dentée frettée sur moyeu."),
    "H7/u6": ("Serrage très fort", "Frettage. Transmission de couple par adhérence seule."),
}


def _tranche(dim, tranches):
    """Retourne la tranche de dimension contenant `dim` (borne inf exclue, sup incluse)."""
    for t in tranches:
        if t[0] < dim <= t[1]:
            return t
    return None


def valeur_it(dim, grade):
    """Valeur de l'intervalle de tolérance IT en µm pour une dimension et un grade.
    grade : entier (ex. 7) ou chaîne ('IT7')."""
    if isinstance(grade, str):
        grade = int(grade.upper().replace("IT", ""))
    t = _tranche(dim, TRANCHES_IT)
    if t is None:
        raise ValueError("Dimension hors du domaine 0 < d <= 500 mm")
    if not 1 <= grade <= 16:
        raise ValueError("Grade IT hors du domaine IT1..IT16")
    return TABLE_IT[t][grade - 1]


def _index_ef(dim):
    t = _tranche(dim, TRANCHES_EF)
    if t is None:
        raise ValueError("Dimension hors du domaine 0 < d <= 500 mm")
    return TRANCHES_EF.index(t)


def ecarts_arbre(dim, lettre, grade):
    """Retourne (ei, es) en µm pour un arbre, ex. ecarts_arbre(20, 'g', 6)."""
    lettre = lettre.lower()
    it = valeur_it(dim, grade)
    if lettre == "js":
        return (-it / 2, it / 2)
    if lettre not in ECARTS_ARBRE:
        raise ValueError(f"Lettre '{lettre}' non prise en charge")
    ef = ECARTS_ARBRE[lettre][_index_ef(dim)]
    if lettre in ("c", "d", "e", "f", "g", "h"):
        es = ef            # écart fondamental = écart supérieur
        ei = es - it
    else:
        ei = ef            # écart fondamental = écart inférieur
        es = ei + it
    return (ei, es)


def _delta(dim, grade):
    """Terme correctif Delta = IT(n) - IT(n-1), utilisé pour les alésages K, M, N, P..ZC."""
    if grade <= 1:
        return 0
    return valeur_it(dim, grade) - valeur_it(dim, grade - 1)


def ecarts_alesage(dim, lettre, grade):
    """Retourne (EI, ES) en µm pour un alésage, ex. ecarts_alesage(20, 'H', 7).
    Règle générale ISO : l'écart de l'alésage se déduit de l'arbre homologue
    par symétrie, avec un terme correctif Delta pour K, M, N (<= IT8)
    et P..ZC (<= IT7)."""
    L = lettre.upper()
    it = valeur_it(dim, grade)
    if L == "JS":
        return (-it / 2, it / 2)
    if L == "H":
        return (0.0, float(it))
    l_min = L.lower()
    if l_min not in ECARTS_ARBRE:
        raise ValueError(f"Lettre '{L}' non prise en charge")
    ef = ECARTS_ARBRE[l_min][_index_ef(dim)]
    if L in ("C", "D", "E", "F", "G"):
        # règle générale : EI = -es(arbre)
        EI = -ef
        ES = EI + it
    else:
        # K, M, N, P, R, S, U : ES = -ei(arbre) + Delta
        applique_delta = (L in ("K", "M", "N") and grade <= 8) or \
                         (L in ("P", "R", "S", "U") and grade <= 7)
        d = _delta(dim, grade) if applique_delta else 0
        ES = -ef + d
        EI = ES - it
    return (float(EI), float(ES))


def calcul_ajustement(dim, lettre_alesage, grade_alesage, lettre_arbre, grade_arbre):
    """Analyse complète d'un ajustement. Dimensions en mm, écarts renvoyés en mm."""
    EI, ES = ecarts_alesage(dim, lettre_alesage, grade_alesage)
    ei, es = ecarts_arbre(dim, lettre_arbre, grade_arbre)

    it_al = valeur_it(dim, grade_alesage)
    it_ar = valeur_it(dim, grade_arbre)

    al_min, al_max = dim + EI / 1000, dim + ES / 1000
    ar_min, ar_max = dim + ei / 1000, dim + es / 1000

    jeu_maxi = ES - ei          # µm
    jeu_mini = EI - es          # µm

    if jeu_mini >= 0:
        nature = "Ajustement AVEC JEU"
        detail = "L'arbre est toujours plus petit que l'alésage : la pièce est libre de tourner ou coulisser."
    elif jeu_maxi <= 0:
        nature = "Ajustement AVEC SERRAGE"
        detail = "L'arbre est toujours plus gros que l'alésage : montage à la presse ou par dilatation."
    else:
        nature = "Ajustement INCERTAIN"
        detail = "Selon les pièces réellement usinées, on peut obtenir du jeu ou du serrage."

    return {
        "designation": f"Ø{dim} {lettre_alesage.upper()}{grade_alesage}/{lettre_arbre.lower()}{grade_arbre}",
        "EI": EI, "ES": ES, "ei": ei, "es": es,
        "IT_alesage": it_al, "IT_arbre": it_ar,
        "alesage_mini": al_min, "alesage_maxi": al_max,
        "arbre_mini": ar_min, "arbre_maxi": ar_max,
        "jeu_maxi": jeu_maxi, "jeu_mini": jeu_mini,
        "serrage_maxi": -jeu_mini, "serrage_mini": -jeu_maxi,
        "nature": nature, "detail": detail,
        "tolerance_ajustement": jeu_maxi - jeu_mini,
    }
