# -*- coding: utf-8 -*-
"""
BTS CPI — Cours complémentaires (Blocs 7 et 8)
Conception détaillée, transmission de puissance et choix des matériaux
"""

BLOC_7 = {
    "titre": "Bloc 7 : Transmission de Puissance & Engrenages",
    "chapitres": {
        "1. Roulements & Guidages": """
### Guidage en rotation par roulements

Le choix des roulements dépend des efforts appliqués (radiaux, axiaux) et des conditions de fonctionnement (vitesse, durée de vie $L_{10}$).

* **Roulements à billes à contact radial (ISO 6000) :** Supportent des charges radiales prépondérantes et de faibles charges axiales.
* **Roulements à rouleaux coniques :** Adaptés aux charges combinées très élevées (axiales + radiales). Nécessitent un montage par paires (en X ou en O).
* **Règle d'arrêt axial :** 
  * Arbre tournant / charge tournante par rapport à la bague : Bague intérieure montée **serrée**.
  * Bague extérieure montée **glissante** dans le logement.
""",
        "2. Transmission par Engrenages": """
### Engrenages cylindriques à denture droite

* **Rapport de transmission ($m$) :**
  $$i = \\frac{N_{sortie}}{N_{entrée}} = \\frac{Z_{menante}}{Z_{menée}}$$
* **Entraxe ($a$) :**
  $$a = \\frac{m \\cdot (Z_1 + Z_2)}{2}$$
  *(avec $m$ = module normalisé et $Z$ = nombre de dents)*
* **Conditions de non-interférence :** $Z_{min} \\ge 17$ pour un angle d'pression $\\alpha = 20^\\circ$.
"""
    }
}

BLOC_8 = {
    "titre": "Bloc 8 : Choix des Matériaux & Traitements Surfaciques",
    "chapitres": {
        "1. Désignation des Aciers & Alliages": """
### Normalisation des matériaux (ISO)

* **Aciers non alliés d'usage général :** `S235`, `E335` ($S$ = acier de construction, $235$ = limite élastique $Re$ en MPa).
* **Aciers fortement alliés :** `X5CrNi18-10` ($X$ = fortement allié, $0.05\\%$ de carbone, $18\\%$ de Chrome, $10\\%$ de Nickel -> Acier Inoxydable 304).
* **Alliages d'aluminium :** `EN AW-6060` (Série 6000 : Aluminium + Magnésium + Silicium, très bonne aptitudes à l'extrudage et au traitement anodique).
""",
        "2. Traitements Thermiques & Surfaciques": """
### Amélioration des propriétés mécaniques

* **Trempe + Revenu :** Augmente la dureté et la résistance à la rupture, suivi d'un revenu pour réduire la fragilité.
* **Cémentation :** Enrichissement en carbone de la surface pour obtenir un cœur tenace et une surface très dure (ex: engrenages, arbres).
* **Anodisation (Oxydaion Anodique) :** Traitement de surface spécifique aux alliages d'aluminium pour améliorer la résistance à la corrosion et à l'usure.
"""
    }
}
