# -*- coding: utf-8 -*-
"""Base matériaux + moteur de calcul RDM pour l'application BTS CPI."""

import math

# ---------------------------------------------------------------------------
# BASE MATÉRIAUX
# Re, Rm en MPa | E en GPa | rho en kg/m3 | A en %
# ---------------------------------------------------------------------------

MATERIAUX = [
    # --- Aciers d'usage général ---
    {"nom": "S235", "famille": "Acier non allié", "Re": 235, "Rm": 400, "E": 210, "rho": 7850,
     "A": 26, "designation": "Acier de construction, Re = 235 MPa",
     "emploi": "Charpente, mécano-soudure, châssis. Soudable sans précaution.", "prix": 1.0},
    {"nom": "S275", "famille": "Acier non allié", "Re": 275, "Rm": 430, "E": 210, "rho": 7850,
     "A": 23, "designation": "Acier de construction, Re = 275 MPa",
     "emploi": "Poutrelles, structures soudées de moyenne sollicitation.", "prix": 1.05},
    {"nom": "S355", "famille": "Acier non allié", "Re": 355, "Rm": 510, "E": 210, "rho": 7850,
     "A": 22, "designation": "Acier de construction, Re = 355 MPa",
     "emploi": "Structures fortement sollicitées, levage, ponts.", "prix": 1.2},
    {"nom": "E335", "famille": "Acier non allié", "Re": 335, "Rm": 590, "E": 210, "rho": 7850,
     "A": 16, "designation": "Acier de construction mécanique",
     "emploi": "Bielles, tirants, pièces mécaniques peu traitées.", "prix": 1.2},

    # --- Aciers non alliés spéciaux ---
    {"nom": "C22", "famille": "Acier non allié spécial", "Re": 240, "Rm": 500, "E": 210,
     "rho": 7850, "A": 22, "designation": "0,22 % de carbone",
     "emploi": "Cémentation, pièces peu sollicitées, soudable.", "prix": 1.3},
    {"nom": "C35", "famille": "Acier non allié spécial", "Re": 300, "Rm": 620, "E": 210,
     "rho": 7850, "A": 18, "designation": "0,35 % de carbone",
     "emploi": "Axes, leviers, compromis résistance/usinabilité.", "prix": 1.35},
    {"nom": "C45", "famille": "Acier non allié spécial", "Re": 340, "Rm": 680, "E": 210,
     "rho": 7850, "A": 16, "designation": "0,45 % de carbone",
     "emploi": "Arbres, axes, engrenages. Le plus utilisé en mécanique générale.", "prix": 1.4},
    {"nom": "C45 trempé revenu", "famille": "Acier traité", "Re": 660, "Rm": 850, "E": 210,
     "rho": 7850, "A": 12, "designation": "C45 après trempe + revenu",
     "emploi": "Arbres sollicités, tiges. Même acier que C45, propriétés doublées.", "prix": 1.8},
    {"nom": "C60", "famille": "Acier non allié spécial", "Re": 380, "Rm": 820, "E": 210,
     "rho": 7850, "A": 11, "designation": "0,60 % de carbone",
     "emploi": "Ressorts, outillage, pièces à forte dureté.", "prix": 1.5},

    # --- Aciers faiblement alliés ---
    {"nom": "16MnCr5", "famille": "Acier allié", "Re": 590, "Rm": 900, "E": 210, "rho": 7850,
     "A": 10, "designation": "0,16 % C - 1,25 % Mn - Cr",
     "emploi": "Acier de CÉMENTATION : pignons, arbres cannelés (peau dure, cœur tenace).",
     "prix": 2.2},
    {"nom": "34CrMo4", "famille": "Acier allié", "Re": 650, "Rm": 1000, "E": 210, "rho": 7850,
     "A": 12, "designation": "0,34 % C - 1 % Cr - Mo",
     "emploi": "Arbres de transmission, pièces de sécurité traitées.", "prix": 2.5},
    {"nom": "42CrMo4 trempé revenu", "famille": "Acier allié", "Re": 750, "Rm": 1100, "E": 210,
     "rho": 7850, "A": 11, "designation": "0,42 % C - 1 % Cr - Mo",
     "emploi": "Arbres, vilebrequins, tiges de vérin. Nitrurable. Référence en fatigue.",
     "prix": 2.8},
    {"nom": "51CrV4", "famille": "Acier allié", "Re": 900, "Rm": 1200, "E": 210, "rho": 7850,
     "A": 9, "designation": "0,51 % C - 1 % Cr - V",
     "emploi": "Acier à ressorts : lames, ressorts de soupape, outillage à main.", "prix": 2.9},
    {"nom": "100Cr6", "famille": "Acier allié", "Re": 1600, "Rm": 2000, "E": 210, "rho": 7850,
     "A": 2, "designation": "1 % C - 1,5 % Cr",
     "emploi": "Bagues de roulement (62 HRC). Résiste à la pression hertzienne.", "prix": 3.2},

    # --- Inox ---
    {"nom": "X5CrNi18-10 (304)", "famille": "Acier inoxydable", "Re": 210, "Rm": 600, "E": 200,
     "rho": 7900, "A": 45, "designation": "0,05 % C - 18 % Cr - 10 % Ni",
     "emploi": "Inox austénitique courant. Agroalimentaire, décoration. Amagnétique, très ductile.",
     "prix": 4.5},
    {"nom": "X2CrNiMo17-12-2 (316L)", "famille": "Acier inoxydable", "Re": 200, "Rm": 580,
     "E": 200, "rho": 8000, "A": 45, "designation": "0,02 % C - 17 % Cr - 12 % Ni - 2 % Mo",
     "emploi": "Résiste aux chlorures : marine, médical, chimie. Soudable sans corrosion.",
     "prix": 6.5},
    {"nom": "X12Cr13", "famille": "Acier inoxydable", "Re": 450, "Rm": 700, "E": 215, "rho": 7700,
     "A": 15, "designation": "0,12 % C - 13 % Cr",
     "emploi": "Inox martensitique TREMPABLE. Coutellerie, axes inox durs.", "prix": 4.0},

    # --- Fontes ---
    {"nom": "EN-GJL-250", "famille": "Fonte", "Re": 165, "Rm": 250, "E": 110, "rho": 7200,
     "A": 0.5, "designation": "Fonte à graphite lamellaire, Rm = 250 MPa",
     "emploi": "Bâtis de machines-outils, carters. AMORTIT LES VIBRATIONS. Fragile.", "prix": 0.9},
    {"nom": "EN-GJS-500-7", "famille": "Fonte", "Re": 320, "Rm": 500, "E": 169, "rho": 7100,
     "A": 7, "designation": "Fonte à graphite sphéroïdal, Rm = 500, A = 7 %",
     "emploi": "Fonte DUCTILE : vilebrequins, moyeux, corps de vanne.", "prix": 1.3},
    {"nom": "EN-GJS-400-15", "famille": "Fonte", "Re": 250, "Rm": 400, "E": 169, "rho": 7100,
     "A": 15, "designation": "Fonte GS ferritique, A = 15 %",
     "emploi": "Pièces moulées tenaces : bras de suspension, raccords.", "prix": 1.3},

    # --- Aluminium ---
    {"nom": "EN AW-6060 T6", "famille": "Aluminium", "Re": 150, "Rm": 190, "E": 69, "rho": 2700,
     "A": 8, "designation": "Al-Mg-Si, trempé revenu",
     "emploi": "PROFILÉS EXTRUDÉS rainurés (40x40). Bonne anodisation.", "prix": 3.5},
    {"nom": "EN AW-6082 T6", "famille": "Aluminium", "Re": 260, "Rm": 310, "E": 70, "rho": 2700,
     "A": 9, "designation": "Al-Si-Mg-Mn, trempé revenu",
     "emploi": "Alu de structure : bras, platines usinées. Bon compromis.", "prix": 3.8},
    {"nom": "EN AW-2017A T4 (AU4G)", "famille": "Aluminium", "Re": 280, "Rm": 430, "E": 72,
     "rho": 2790, "A": 15, "designation": "Al-Cu, trempé mûri",
     "emploi": "Décolletage, aéronautique. NON SOUDABLE, corrosion médiocre.", "prix": 4.5},
    {"nom": "EN AW-7075 T6", "famille": "Aluminium", "Re": 470, "Rm": 540, "E": 71, "rho": 2810,
     "A": 7, "designation": "Al-Zn-Mg-Cu, trempé revenu",
     "emploi": "Alu le plus résistant. Aéronautique, sport. Cher, non soudable.", "prix": 8.0},

    # --- Cuivreux ---
    {"nom": "CuZn39Pb3 (laiton)", "famille": "Cuivreux", "Re": 250, "Rm": 430, "E": 100,
     "rho": 8470, "A": 20, "designation": "Laiton de décolletage",
     "emploi": "Robinetterie, raccords, pièces décolletées. Usinabilité exceptionnelle.",
     "prix": 8.5},
    {"nom": "CuSn8 (bronze)", "famille": "Cuivreux", "Re": 250, "Rm": 400, "E": 110, "rho": 8800,
     "A": 35, "designation": "Bronze à 8 % d'étain",
     "emploi": "COUSSINETS, bagues de guidage. Faible frottement contre l'acier.", "prix": 11.0},

    # --- Titane ---
    {"nom": "TA6V (Ti-6Al-4V)", "famille": "Titane", "Re": 830, "Rm": 900, "E": 114, "rho": 4430,
     "A": 10, "designation": "Titane 6 % Al - 4 % V",
     "emploi": "Aéronautique, implants médicaux. Excellent Re/rho, biocompatible. Très cher.",
     "prix": 45.0},

    # --- Polymères ---
    {"nom": "PA6-6 (Nylon)", "famille": "Polymère", "Re": 55, "Rm": 80, "E": 3.0, "rho": 1140,
     "A": 50, "designation": "Polyamide 6-6",
     "emploi": "Engrenages silencieux, galets, guides. Autolubrifiant. Reprend l'humidité.",
     "prix": 6.0},
    {"nom": "POM-C (Delrin)", "famille": "Polymère", "Re": 48, "Rm": 68, "E": 2.8, "rho": 1410,
     "A": 35, "designation": "Polyoxyméthylène copolymère",
     "emploi": "Pièces usinées de précision, galets, glissières. Stable dimensionnellement.",
     "prix": 7.0},
    {"nom": "PEHD", "famille": "Polymère", "Re": 22, "Rm": 25, "E": 1.0, "rho": 950, "A": 600,
     "designation": "Polyéthylène haute densité",
     "emploi": "Guides de convoyeur, réservoirs. Très faible frottement, chimiquement inerte.",
     "prix": 2.5},
    {"nom": "ABS", "famille": "Polymère", "Re": 40, "Rm": 45, "E": 2.3, "rho": 1050, "A": 25,
     "designation": "Acrylonitrile butadiène styrène",
     "emploi": "Carters injectés, boîtiers. Bon compromis choc/rigidité/prix.", "prix": 2.8},
    {"nom": "PLA (impression 3D)", "famille": "Polymère", "Re": 45, "Rm": 50, "E": 3.5,
     "rho": 1240, "A": 6, "designation": "Acide polylactique",
     "emploi": "Prototypage FDM. Facile à imprimer mais CASSANT et anisotrope.", "prix": 20.0},
    {"nom": "PETG (impression 3D)", "famille": "Polymère", "Re": 45, "Rm": 50, "E": 2.1,
     "rho": 1270, "A": 100, "designation": "Polyéthylène téréphtalate glycolisé",
     "emploi": "Prototypage FDM fonctionnel. Plus tenace que le PLA.", "prix": 24.0},
]

FAMILLES = sorted({m["famille"] for m in MATERIAUX})


def get_materiau(nom):
    for m in MATERIAUX:
        if m["nom"] == nom:
            return m
    return None


# ---------------------------------------------------------------------------
# SECTIONS
# ---------------------------------------------------------------------------

def section_aire(forme, **kw):
    """Aire en mm2."""
    if forme == "Cercle plein":
        return math.pi * kw["d"] ** 2 / 4
    if forme == "Tube":
        return math.pi * (kw["D"] ** 2 - kw["d"] ** 2) / 4
    if forme == "Rectangle":
        return kw["b"] * kw["h"]
    if forme == "Rectangle creux":
        return kw["b"] * kw["h"] - kw["bi"] * kw["hi"]
    raise ValueError(forme)


def section_igz(forme, **kw):
    """Moment quadratique de flexion IGz en mm4, et v en mm."""
    if forme == "Cercle plein":
        d = kw["d"]
        return math.pi * d ** 4 / 64, d / 2
    if forme == "Tube":
        D, d = kw["D"], kw["d"]
        return math.pi * (D ** 4 - d ** 4) / 64, D / 2
    if forme == "Rectangle":
        b, h = kw["b"], kw["h"]
        return b * h ** 3 / 12, h / 2
    if forme == "Rectangle creux":
        b, h, bi, hi = kw["b"], kw["h"], kw["bi"], kw["hi"]
        return (b * h ** 3 - bi * hi ** 3) / 12, h / 2
    raise ValueError(forme)


def section_i0(forme, **kw):
    """Moment quadratique polaire I0 en mm4 (sections circulaires uniquement), et v."""
    if forme == "Cercle plein":
        d = kw["d"]
        return math.pi * d ** 4 / 32, d / 2
    if forme == "Tube":
        D, d = kw["D"], kw["d"]
        return math.pi * (D ** 4 - d ** 4) / 32, D / 2
    raise ValueError("La torsion n'est valable que pour les sections circulaires.")


# ---------------------------------------------------------------------------
# CALCULS RDM
# ---------------------------------------------------------------------------

def traction(N, S, Re, s, L=None, E=None):
    """N en newtons, S en mm2, Re en MPa, L en mm, E en MPa."""
    sigma = N / S
    rpe = Re / s
    res = {
        "sigma": sigma, "Rpe": rpe, "ok": sigma <= rpe,
        "s_reel": Re / sigma if sigma else float("inf"),
    }
    if L and E:
        res["allongement"] = N * L / (E * S)
        res["epsilon"] = res["allongement"] / L * 100
    return res


def cisaillement(T, S, Re, s, double=False, coef_Reg=0.5):
    S_eff = 2 * S if double else S
    tau = T / S_eff
    Reg = coef_Reg * Re
    rpg = Reg / s
    return {
        "tau": tau, "Reg": Reg, "Rpg": rpg, "ok": tau <= rpg,
        "S_effective": S_eff, "s_reel": Reg / tau if tau else float("inf"),
    }


def matage(F, d, e, Re, coef=0.8):
    p = F / (d * e)
    p_adm = coef * Re
    return {"p": p, "p_adm": p_adm, "ok": p <= p_adm}


def torsion(Mt, I0, v, Re, s, L=None, G=80000, coef_Reg=0.6):
    """Mt en N.mm, I0 en mm4, L en mm, G en MPa."""
    tau = Mt * v / I0
    Reg = coef_Reg * Re
    rpg = Reg / s
    res = {"tau": tau, "Reg": Reg, "Rpg": rpg, "ok": tau <= rpg,
           "module_torsion": I0 / v,
           "s_reel": Reg / tau if tau else float("inf")}
    if L:
        theta_rad = Mt * L / (G * I0)
        res["theta_rad"] = theta_rad
        res["theta_deg"] = math.degrees(theta_rad)
        res["theta_deg_par_m"] = math.degrees(theta_rad) / (L / 1000)
    return res


CAS_FLEXION = {
    "2 appuis - charge F au milieu": {
        "type": "ponctuelle",
        "Mf": lambda F, L: F * L / 4,
        "f": lambda F, L, E, I: F * L ** 3 / (48 * E * I),
        "desc": "Poutre sur deux appuis simples, charge concentrée à mi-portée.",
    },
    "2 appuis - charge répartie q": {
        "type": "repartie",
        "Mf": lambda q, L: q * L ** 2 / 8,
        "f": lambda q, L, E, I: 5 * q * L ** 4 / (384 * E * I),
        "desc": "Poutre sur deux appuis simples, charge uniformément répartie.",
    },
    "Console - charge F en bout": {
        "type": "ponctuelle",
        "Mf": lambda F, L: F * L,
        "f": lambda F, L, E, I: F * L ** 3 / (3 * E * I),
        "desc": "Poutre encastrée-libre, charge concentrée à l'extrémité libre.",
    },
    "Console - charge répartie q": {
        "type": "repartie",
        "Mf": lambda q, L: q * L ** 2 / 2,
        "f": lambda q, L, E, I: q * L ** 4 / (8 * E * I),
        "desc": "Poutre encastrée-libre, charge uniformément répartie.",
    },
    "2 encastrements - charge F au milieu": {
        "type": "ponctuelle",
        "Mf": lambda F, L: F * L / 8,
        "f": lambda F, L, E, I: F * L ** 3 / (192 * E * I),
        "desc": "Poutre bi-encastrée, charge concentrée à mi-portée.",
    },
}


def flexion(cas, charge, L, I, v, E, Re, s, fleche_adm=None):
    """charge = F en N (ponctuelle) ou q en N/mm (répartie). L en mm."""
    c = CAS_FLEXION[cas]
    Mf = c["Mf"](charge, L)
    f = c["f"](charge, L, E, I)
    sigma = Mf * v / I
    rpe = Re / s
    res = {
        "Mf": Mf, "sigma": sigma, "Rpe": rpe, "fleche": f,
        "ok_resistance": sigma <= rpe,
        "module_flexion": I / v,
        "s_reel": Re / sigma if sigma else float("inf"),
        "description": c["desc"],
    }
    if fleche_adm:
        res["fleche_adm"] = fleche_adm
        res["ok_rigidite"] = f <= fleche_adm
    return res


def flexion_torsion(Mf, Mt, critere="Tresca"):
    """Moment idéal pour sollicitation combinée. Mf, Mt en N.mm."""
    if critere == "Tresca":
        return math.sqrt(Mf ** 2 + Mt ** 2)
    return math.sqrt(Mf ** 2 + 0.75 * Mt ** 2)


def flambage(E, I, L, liaison="Rotule - rotule", F=None):
    coefs = {
        "Rotule - rotule": 1.0,
        "Encastrement - libre": 2.0,
        "Encastrement - rotule": 0.7,
        "Encastrement - encastrement": 0.5,
    }
    Lf = coefs[liaison] * L
    Fc = math.pi ** 2 * E * I / Lf ** 2
    res = {"Lf": Lf, "Fc": Fc, "coef_liaison": coefs[liaison]}
    if F:
        res["s_flambage"] = Fc / F
        res["ok"] = Fc / F >= 3
    return res


def couple_depuis_puissance(P_watt, N_tr_min):
    """Retourne (omega en rad/s, Mt en N.m, Mt en N.mm)."""
    omega = 2 * math.pi * N_tr_min / 60
    Mt_nm = P_watt / omega
    return omega, Mt_nm, Mt_nm * 1000
