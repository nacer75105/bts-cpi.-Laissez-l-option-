# -*- coding: utf-8 -*-
"""
BTS CPI — Cours complémentaires (Blocs 15 et 16)
Métrologie, Contrôle Qualité et Analyse Fonctionnelle APTE
"""

BLOC_15 = {
    "titre": "Bloc 15 : Métrologie & Contrôle Qualité",
    "fiches": {
        "1. Mesure et Instruments de Contrôle": """
### Instruments de métrologie dimensionnelle

* **Pied à coulisse au 1/50e :** Précision de $0{,}02 \\text{ mm}$.
* **Micromètre (Palmer) :** Précision de $0{,}01 \\text{ mm}$ à $0{,}001 \\text{ mm}$ (système vis-écrou au pas de $0{,}5 \\text{ mm}$).
* **Machines à Mesurer Tridimensionnelles (MMT) :** Palpage mécanique ou optique pour le contrôle des tolérances géométriques complexes (GPS).
* **Calibres à limites (Tampons et Entre-N'entre pas) :** Contrôle rapide en série (validation conforme / non-conforme).
""",
        "2. Capabilité des Procédés de Fabrication": """
### Indicateurs de qualité ($Cp$ et $Cpk$)

* **Capabilité machine ($Cp$) :**
  $$Cp = \\frac{IT}{6 \\cdot \\sigma}$$
  *(avec $IT$ = Intervalle de Tolérance, $\\sigma$ = écart-type du procédé)*
* **Indicateur de centrage ($Cpk$) :**
  $$Cpk = \\min\\left(\\frac{Ts - \\bar{X}}{3\\sigma}, \\frac{\\bar{X} - Ti}{3\\sigma}\\right)$$
* **Critère d'acceptabilité :** Un procédé est considéré comme capable si $Cpk \\ge 1{,}33$.
"""
    }
}

BLOC_16 = {
    "titre": "Bloc 16 : Analyse Fonctionnelle & Cahier des Charges (APTE)",
    "fiches": {
        "1. Analyse Fonctionnelle Externe": """
### Méthode APTE & Diagramme Pieuvre

* **Soustraction d'analyse (Bête à cornes) :** 
  * À qui le produit rend-il service ?
  * Sur quoi agit-il ?
  * Dans quel but existe-t-il ?
* **Diagramme d'interacteurs (Pieuvre) :**
  * **Fonction Principale (FP) :** Lie deux éléments du milieu extérieur via le produit.
  * **Fonction de Contrainte (FC) :** Adapte le produit à un élément du milieu extérieur.
""",
        "2. Cahier des Charges Fonctionnel (CdCF)": """
### Caractérisation des fonctions

* **Critère d'appréciation :** Grandeur mesurable permettant d'évaluer le service rendu (ex: masse, vitesse, coût).
* **Niveau :** Valeur cible chiffrée assortie d'une tolérance (ex: $15 \\text{ kg} \\pm 0{,}5 \\text{ kg}$).
* **Flexibilité :** Indication sur le degré de négociation de la valeur (F0 : impératif, F1 : peu négociable, F2 : négociable).
"""
    }
}
