# -*- coding: utf-8 -*-
"""
BTS CPI — Cours complémentaires (Blocs 9 et 10)
Statismes des mécanismes, assemblages mécano-soudés et Cotation GPS
"""

BLOC_9 = {
    "titre": "Bloc 9 : Statisme des Mécanismes & Assemblages Soudés",
    "chapitres": {
        "1. Isostatisme et Hyperstatisme": """
### Analyse structurelle des mécanismes

* **Degré d'hyperstatisme ($h$) :**
  $$h = m + E_s - 6(N - 1)$$
  *(avec $m$ = mobilité du mécanisme, $E_s$ = nombre d'inconnues statiques des liaisons, $N$ = nombre de pièces du mécanisme)*
* **Mécanisme Isostatique ($h = 0$) :** Le système de forces admet une solution unique. Facile à assembler, peu sensible aux dilations thermiques et aux tolérances géométriques.
* **Mécanisme Hyperstatique ($h > 0$) :** Nécessite une grande précision de fabrication (tolérances serrées) sous peine de coincement ou de contraintes parasites.
""",
        "2. Assemblages Mécano-soudés": """
### Calcul des cordons de soudure d'angle

* **Épaisseur de gorge ($a$) :** Hauteur du triangle isocèle inscrit dans la section du cordon.
  $$a \\approx 0{,}7 \\cdot e_{mini}$$
* **Critère de résistance (Formule simplifiée) :**
  $$\\tau_{moyen} = \\frac{F}{a \\cdot L_{totale}} \\le \\frac{R_e}{\\gamma_m}$$
  *(avec $L_{totale}$ = longueur utile cumulée des cordons, $R_e$ = limite élastique, $\\gamma_m$ = coefficient de sécurité)*
"""
    }
}

BLOC_10 = {
    "titre": "Bloc 10 : Spécification Géométrique des Produits (GPS)",
    "chapitres": {
        "1. Tolérances de Forme et d'Orientation": """
### Tolérancement géométrique ISO 1101

* **Tolérances de forme :** Rectitude, Planéité, Circularité, Cylindricité. *(Pas besoin de référence de datation)*.
* **Tolérances d'orientation :** Perpendicularité, Parallélisme, Inclinaison. *(Nécessitent une ou plusieurs références de spécification)*.
* **Symbole de Perpendicularité (⟂) :** La zone de tolérance est comprise entre deux plans parallèles distants de $t$ et perpendiculaires à la référence $A$.
""",
        "2. Exigence du Maximum de Matière (MMR)": """
### Modificateur Ⓜ (Maximum Material Condition)

* **Objectif :** Autoriser un jeu de fabrication supplémentaire lorsque l'élément tolérancé s'éloigne de son état au maximum de matière.
* **Application :** Essentiellement utilisé pour garantir le montage de pièces d'assemblage (axes, taraudages, passage de vis) à moindre coût d'usinage.
"""
    }
}
