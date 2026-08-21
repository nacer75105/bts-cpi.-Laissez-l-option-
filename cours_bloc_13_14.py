# -*- coding: utf-8 -*-
"""
BTS CPI — Cours complémentaires (Blocs 13 et 14)
RDM Avancée, Injection Plastique et Matériaux Composites
"""

BLOC_13 = {
    "titre": "Bloc 13 : RDM Avancée (Flambement & Torsion)",
    "fiches": {
        "1. Flambement des Poutres Comprimées (Formule d'Euler)": """
### Résistance à l'instabilité élastique

* **Charge critique d'Euler ($F_c$) :**
  $$F_c = \\frac{\\pi^2 \\cdot E \\cdot I_min}{L_k^2}$$
  *(avec $E$ = module de Young, $I_min$ = moment d'inertie minimal, $L_k$ = longueur de flambement)*
* **Longueur de flambement ($L_k$) selon les liaisons :**
  * Articulée-Articulée : $L_k = L$
  * Encastrée-Libre : $L_k = 2L$
  * Encastrée-Encastrée : $L_k = 0{,}5L$
  * Encastrée-Articulée : $L_k \\approx 0{,}7L$
""",
        "2. Torsion Simple des Arbres Circulaires": """
### Contraintes de cisaillement en torsion

* **Contrainte de cisaillement maximale ($\\tau_{max}$) :**
  $$\\tau_{max} = \\frac{M_t}{\\frac{I_0}{v}} = \\frac{16 \\cdot M_t}{\\pi \\cdot d^3} \\le R_{pg}$$
  *(avec $M_t$ = moment de torsion, $I_0/v$ = module de flexion polaire, $d$ = diamètre de l'arbre)*
* **Angle de vrillage ($\\alpha$) :**
  $$\\alpha = \\frac{M_t \\cdot L}{G \\cdot I_0} \\quad \\text{(en radians)}$$
"""
    }
}

BLOC_14 = {
    "titre": "Bloc 14 : Mise en Œuvre des Plastiques & Composites",
    "fiches": {
        "1. Conception de Pièces Injectées en Thermoplastique": """
### Règles de tracé des pièces plastique

* **Dépouille :** Prévoir un angle de dépouille (minimum $1^\\circ$ à $2^\\circ$) pour faciliter l'éjection.
* **Épaisseur de paroi :** Maintenir une constante d'épaisseur pour éviter les retassures et les tensions internes.
* **Rayons de raccordement :** Éviter les angles vifs ($R \\ge 0{,}5 \\cdot e$) pour réduire la concentration de contraintes.
""",
        "2. Matériaux Composites": """
### Fibres et Matrices

* **Renforts (Fibres) :** Fibre de verre (économique), fibre de carbone (haute rigidité/légèreté), fibre d'aramide/Kevlar (résistance aux chocs).
* **Matrices :** Thermodurcissables (résine époxy, polyester) ou Thermoplastiques (PA, PEEK).
* **Procédés d'élaboration :** Infusion sous vide, RTM (*Resin Transfer Molding*), drapage autoclavé.
"""
    }
}
