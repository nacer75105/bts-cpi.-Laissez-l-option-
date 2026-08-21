# -*- coding: utf-8 -*-
"""Blocs 5 et 6 du référentiel BTS CPI."""

BLOC_5 = {
    "id": "bloc5",
    "titre": "Bloc 5 — CAO et modélisation 3D",
    "resume": "Construire un modèle 3D robuste, l'assembler, le mettre en plan et l'exporter.",
    "fiches": [
        {
            "id": "5.1",
            "titre": "Esquisse, contraintes et degrés de liberté",
            "duree": "12 h",
            "cours": """
### 1. L'esquisse : la fondation de tout le modèle

En CAO paramétrique (SolidWorks, CATIA, Inventor, Fusion), **tout part d'une esquisse 2D**
que l'on transforme ensuite en volume. Une esquisse mal construite produit un modèle qui
**casse à la première modification**. C'est le point qui distingue un débutant d'un modeleur
professionnel.

**Règle absolue :** une esquisse doit être **entièrement contrainte** avant de quitter le mode
esquisse. SolidWorks l'indique par la mention *« Entièrement contraint »* et par des entités
qui passent du **bleu** (sous-contraint) au **noir** (contraint).

### 2. Degrés de liberté d'une entité 2D

| Entité | Degrés de liberté |
|---|---|
| Point | 2 (x, y) |
| Ligne | 4 (2 extrémités × 2) |
| Cercle | 3 (centre x, y + rayon) |
| Arc | 5 (centre x, y + rayon + 2 angles) |

**Contraindre = supprimer tous les degrés de liberté.** Chaque contrainte géométrique ou
dimensionnelle en supprime un ou plusieurs.

### 3. Les deux types de contraintes

**a) Contraintes GÉOMÉTRIQUES** (relations, sans valeur numérique)

| Contrainte | Effet | Degrés supprimés |
|---|---|---|
| Coïncidence | Deux points confondus | 2 |
| Horizontale / Verticale | Fixe la direction | 1 |
| Parallèle / Perpendiculaire | Lie deux directions | 1 |
| Tangence | Raccordement continu | 1 |
| Concentrique | Mêmes centres | 2 |
| Égalité | Mêmes longueurs / rayons | 1 |
| Symétrie | Par rapport à un axe | 2 |
| Fixe | Bloque totalement | tous |

**b) Contraintes DIMENSIONNELLES** (les cotes : longueur, rayon, angle)

**Principe de conception à appliquer systématiquement :** *privilégier les contraintes
géométriques aux cotes.* Une symétrie vaut mieux que deux cotes égales — elle **reste vraie**
quand on modifie la pièce, alors que deux cotes doivent être modifiées à la main.

### 4. Les erreurs à éviter absolument

| Erreur | Conséquence |
|---|---|
| Esquisse sous-contrainte | La géométrie « glisse » à la première modification |
| Esquisse **surcontrainte** | Message d'erreur, contraintes en conflit — il faut en supprimer une |
| Utiliser « Fixe » pour forcer | Masque le problème, l'esquisse devient non paramétrable |
| Esquisse trop complexe (50 entités) | Impossible à déboguer. **Préférer plusieurs esquisses simples.** |
| Ne pas partir de l'origine | La pièce flotte dans l'espace, les assemblages deviennent pénibles |

**Règle d'or : ancrer la première entité sur l'ORIGINE du repère.** C'est le seul point
absolument fixe du modèle.

### 5. Arbre de création et intention de conception

L'**arbre de création** (*feature tree*) enregistre l'ordre des opérations. Chaque fonction
dépend des précédentes. C'est ce qu'on appelle l'**intention de conception**
(*design intent*) : le modèle doit se modifier **de la façon dont le produit évoluerait réellement**.

> *Exemple :* si un trou doit **toujours** rester centré sur une face, on le contraint par
> symétrie sur les bords de la face — pas par une cote « 25 mm depuis le bord gauche ».
> Quand la face passera de 50 à 80 mm de large, le trou restera centré tout seul.

### 6. Le paramétrage par équations

Les logiciels permettent d'écrire des **relations entre cotes** :

```
"Épaisseur" = "Diamètre" / 8
"Entraxe"   = "Longueur" * 0.75
"NbTrous"   = int("Longueur" / 100) + 1
```

C'est ce qui permet de créer une **famille de pièces** (table de configurations) : une seule
maquette pilote 20 références du catalogue.
""",
            "formules": """
**Calcul du degré de liberté résiduel d'une esquisse**

$$ DDL_{résiduel} = \\sum DDL_{entités} - \\sum DDL_{supprimés\\ par\\ contraintes} $$

L'esquisse est entièrement contrainte quand $DDL_{résiduel} = 0$.

**Nombre minimal de cotes pour un contour polygonal fermé de $n$ côtés**

Un polygone fermé de $n$ segments possède $n$ sommets, soit $2n$ degrés de liberté.
Les $n$ coïncidences des extrémités en suppriment $2n - 2n = 0$… en pratique, on retient :

$$ \\text{cotes nécessaires} \\approx 2n - (\\text{contraintes géométriques appliquées}) $$

**Cas courant — rectangle :**
- 4 lignes = 16 DDL
- 4 coïncidences aux coins = −8 → reste 8
- 2 horizontales + 2 verticales = −4 → reste 4
- coïncidence d'un coin sur l'origine = −2 → reste 2
- **2 cotes (longueur + largeur) → 0** ✔️

**Volume d'une extrusion**

$$ V = A_{esquisse} \\times L_{extrusion} $$

**Volume d'une révolution (théorème de Guldin)**

$$ V = 2\\pi \\, d_G \\, A $$

où $A$ est l'aire de l'esquisse et $d_G$ la distance de son centre de gravité à l'axe.

**Surface engendrée par révolution (Guldin)**

$$ S = 2\\pi \\, d_G \\, L $$

où $L$ est la longueur du profil générateur.

**Masse d'une pièce depuis la CAO**

$$ m = \\rho \\times V $$

⚠️ Toujours vérifier que le **matériau est bien affecté** dans le modèle : par défaut le
logiciel applique souvent une masse volumique de 1 000 kg/m³ (eau), ce qui fausse tout.
""",
            "exemple": """
**Cas industriel — Modéliser une équerre paramétrique réutilisable**

Un bureau d'études conçoit une équerre de fixation qui existera en **6 tailles**.
Deux approches sont possibles :

**❌ Approche naïve : 6 fichiers indépendants**
Chaque modification (ajout d'un chanfrein, changement de perçage) doit être répétée 6 fois.
Risque d'oubli, incohérences dans la famille, temps perdu.

**✅ Approche professionnelle : 1 modèle paramétrique + table de configurations**

| Paramètre piloté | Valeur | Relation |
|---|---|---|
| `L` (longueur aile) | 40 / 60 / 80 / 100 / 120 / 150 | *variable maîtresse* |
| `H` (hauteur aile) | — | `= L` (équerre carrée) |
| `E` (épaisseur) | — | `= L / 10` arrondi |
| `D` (Ø perçage) | — | `= E * 1.2` |
| `Entraxe` | — | `= L - 2 * (D + 4)` |
| `R` (congé) | — | `= E` |

**Construction de l'esquisse principale :**
1. Ancrer le coin intérieur sur **l'origine**.
2. Tracer le L avec contraintes **horizontale/verticale** (pas de cotes d'angle).
3. Coter uniquement `L` et `E` — le reste découle des équations.
4. Vérifier la mention *« Entièrement contraint »*.

**Placement des perçages — le point clé :**
Les trous sont contraints par **symétrie** par rapport au plan médian de l'aile, et cotés
depuis l'extrémité par `D + 4`. Résultat : en passant de L=40 à L=150, **les trous se
repositionnent correctement tout seuls** et restent à distance constante du bord.

**Gain mesuré en bureau d'études :** création initiale 45 min (contre 20 min pour un modèle
figé), mais les 6 déclinaisons sont générées en **3 minutes** au lieu de 2 heures, et toute
évolution ultérieure est propagée automatiquement à la famille entière.

**Le piège que cette méthode évite :** dans l'approche naïve, si un client demande un
chanfrein de dégagement, il faut rouvrir 6 fichiers. Sur un catalogue de 200 références,
c'est ce qui fait la différence entre un BE qui tient ses délais et un qui ne les tient pas.
""",
            "exercice": """
**Exercice type examen — Contrainte d'esquisse et paramétrage**

**Partie A.** On esquisse le profil suivant : un rectangle de base surmonté d'un demi-cercle
(forme dite « en oblong vertical »), soit **3 segments de droite + 1 arc de demi-cercle**.

1. Calculer le nombre total de degrés de liberté avant contrainte.
2. Lister les contraintes géométriques à appliquer pour rendre le profil cohérent
   (coïncidences, tangences, horizontales/verticales, symétrie).
3. En déduire le nombre de **cotes** strictement nécessaires. Lesquelles choisir ?
4. Le profil doit rester symétrique par rapport à l'axe vertical quelle que soit la largeur.
   Quelle contrainte garantit cela, et pourquoi est-elle préférable à deux cotes ?

**Partie B.** On extrude ce profil sur 15 mm. Dimensions : largeur 40 mm, hauteur totale
70 mm (dont le demi-cercle en partie haute).

5. Calculer l'aire de l'esquisse puis le volume de la pièce.
6. La pièce est en **EN AW-6060 T6** ($\\rho = 2\\,700$ kg/m³). Calculer sa masse.
7. On perce un trou Ø18 concentrique au demi-cercle, débouchant. Recalculer la masse.
8. Écrire les **équations de paramétrage** permettant que le trou reste toujours concentrique
   au demi-cercle et que son diamètre vaille 45 % de la largeur du profil.
""",
            "corrige": """
**PARTIE A**

**1. Degrés de liberté avant contrainte**

| Entité | Nombre | DDL unitaire | Total |
|---|---|---|---|
| Segments de droite | 3 | 4 | 12 |
| Arc (demi-cercle) | 1 | 5 | 5 |
| | | **TOTAL** | **17 DDL** |

**2. Contraintes géométriques à appliquer**

| Contrainte | Nombre | DDL supprimés |
|---|---|---|
| **Coïncidences** aux 4 jonctions du contour fermé | 4 | 4 × 2 = **8** |
| **Horizontale** sur le segment de base | 1 | **1** |
| **Verticales** sur les deux montants | 2 | **2** |
| **Tangences** arc / montants (aux 2 raccords) | 2 | **2** |
| **Coïncidence** du milieu de la base sur l'origine | 1 | **2** |
| | | **Total : 15** |

$$ DDL_{résiduel} = 17 - 15 = \\mathbf{2} $$

**3. Nombre de cotes nécessaires : 2**

Choix retenu :
- **Largeur = 40 mm** (cote sur le segment de base)
- **Hauteur totale = 70 mm** (de la base au sommet de l'arc)

*Le rayon de l'arc n'a pas à être coté :* les tangences aux deux montants verticaux, combinées
à la largeur, **imposent** $R = 40/2 = 20$ mm. Le coter créerait une **surcontrainte**.

*C'est exactement le type de piège testé en examen : un demi-cercle tangent à deux verticales
parallèles a son rayon entièrement déterminé par leur écartement.*

**4. Contrainte garantissant la symétrie**

$$ \\boxed{\\textbf{La contrainte de SYMÉTRIE des deux montants verticaux par rapport à l'axe Y}} $$

**Pourquoi elle est préférable à deux cotes de 20 mm :**

| | Symétrie | Deux cotes de 20 mm |
|---|---|---|
| Modification de la largeur | ✅ Automatique, la symétrie est **conservée par construction** | ❌ Il faut modifier **les deux cotes** manuellement |
| Risque d'erreur | Nul | Élevé (oubli d'une des deux → profil dissymétrique) |
| Nombre de cotes | 1 (largeur totale) | 2 |
| Lisibilité de l'intention | La symétrie est **explicite** dans le modèle | L'intention est implicite, invisible |

**Principe général à retenir :** *une contrainte géométrique exprime une **intention** qui reste
vraie après modification ; une cote n'exprime qu'un **état** à un instant donné.* En CAO
paramétrique, on privilégie toujours l'intention.

---

**PARTIE B**

**5. Aire de l'esquisse et volume**

L'oblong se décompose en un rectangle surmonté d'un demi-disque de rayon $R = 20$ mm.

*Hauteur de la partie rectangulaire :*
$$ h_{rect} = H_{totale} - R = 70 - 20 = 50\\ \\mathrm{mm} $$

*Aire du rectangle :*
$$ A_1 = 40 \\times 50 = 2\\,000\\ \\mathrm{mm^2} $$

*Aire du demi-disque :*
$$ A_2 = \\frac{\\pi R^2}{2} = \\frac{\\pi \\times 20^2}{2} = \\frac{\\pi \\times 400}{2} = 628,3\\ \\mathrm{mm^2} $$

*Aire totale :*
$$ A = A_1 + A_2 = 2\\,000 + 628,3 = \\mathbf{2\\,628,3\\ \\mathrm{mm^2}} $$

*Volume extrudé :*
$$ V = A \\times L_{extrusion} = 2\\,628,3 \\times 15 = \\mathbf{39\\,425\\ \\mathrm{mm^3}} $$

---

**6. Masse de la pièce pleine**

Conversion : $39\\,425\\ \\mathrm{mm^3} = 39\\,425 \\times 10^{-9}\\ \\mathrm{m^3} = 3,9425\\times10^{-5}\\ \\mathrm{m^3}$

$$ m = \\rho \\times V = 2\\,700 \\times 3,9425\\times10^{-5} = \\mathbf{0,1064\\ kg} = \\mathbf{106,4\\ g} $$

---

**7. Masse après perçage Ø18**

*Volume du trou (cylindre débouchant sur toute l'épaisseur) :*
$$ V_{trou} = \\frac{\\pi d^2}{4} \\times e = \\frac{\\pi \\times 18^2}{4} \\times 15 = 254,47 \\times 15 = 3\\,817\\ \\mathrm{mm^3} $$

*Volume restant :*
$$ V' = 39\\,425 - 3\\,817 = \\mathbf{35\\,608\\ \\mathrm{mm^3}} $$

*Masse :*
$$ m' = 2\\,700 \\times 35\\,608\\times10^{-9} = \\mathbf{0,0961\\ kg} = \\mathbf{96,1\\ g} $$

**Allègement obtenu :**
$$ \\frac{106,4 - 96,1}{106,4} \\times 100 = \\mathbf{9,7\\ \\%} $$

---

**8. Équations de paramétrage**

On définit une **variable maîtresse** unique, la largeur, et on en déduit tout le reste.

```
' --- Variable maîtresse ---
"Largeur" = 40

' --- Géométrie du profil ---
"Rayon_arc"     = "Largeur" / 2
"Hauteur_totale" = 70
"Epaisseur"      = 15

' --- Perçage ---
"Diametre_trou" = "Largeur" * 0.45
```

**Contraintes d'esquisse à poser pour la concentricité (et NON une cote) :**

| Contrainte | Rôle |
|---|---|
| **Concentricité** entre le cercle du trou et l'arc du demi-cercle | Garantit que le trou suit l'arc quelle que soit la largeur ET la hauteur |
| **Symétrie** des montants par rapport à l'axe Y | Maintient le profil symétrique |
| **Tangences** arc / montants | Impose automatiquement `Rayon_arc = Largeur / 2` |

**Vérification du paramétrage avec la valeur de l'énoncé :**
$$ \\text{Diametre\\_trou} = 40 \\times 0,45 = \\mathbf{18\\ mm} \\quad ✔️ $$

**Test de robustesse — ce qu'un correcteur attend :**

Si l'on passe `Largeur` de 40 à **60 mm**, le modèle doit se régénérer ainsi, **sans aucune
intervention manuelle** :

| Paramètre | Avant (L=40) | Après (L=60) |
|---|---|---|
| Rayon de l'arc | 20 mm | **30 mm** (par tangence) |
| Ø du trou | 18 mm | **27 mm** (par équation) |
| Position du trou | Centre de l'arc | **Centre de l'arc** (par concentricité) |
| Symétrie du profil | ✔️ | ✔️ (par contrainte de symétrie) |

⚠️ **Point de vigilance à mentionner :** `Rayon_arc` ne doit **pas** être écrit comme une
équation *et* imposé par tangence — ce serait une **surcontrainte**. On choisit l'un ou
l'autre. La bonne pratique est de laisser la **tangence géométrique** faire le travail et de
supprimer l'équation `"Rayon_arc" = "Largeur" / 2`, qui n'est qu'une commodité de lecture.

De même, il faut vérifier que `Diametre_trou < 2 × Rayon_arc` sous peine de percer hors matière.
Une **règle de contrôle** peut être ajoutée : `"Diametre_trou" <= "Largeur" * 0.8`.
""",
        },
        {
            "id": "5.2",
            "titre": "Fonctions volumiques et surfaciques",
            "duree": "14 h",
            "cours": """
### 1. Les quatre fonctions volumiques fondamentales

Toute pièce mécanique, aussi complexe soit-elle, se construit avec quatre opérations de base,
en **ajout de matière** (bossage) ou en **retrait** (enlèvement) :

| Fonction | Principe | Exemple typique |
|---|---|---|
| **Extrusion** | Translation d'un profil selon une direction | Plaque, nervure, semelle |
| **Révolution** | Rotation d'un profil autour d'un axe | Arbre, poulie, bride, vase |
| **Balayage** (*sweep*) | Profil suivi le long d'une trajectoire | Tube cintré, joint torique, poignée |
| **Lissage** (*loft*) | Transition entre plusieurs profils différents | Carter de transition, pale, coque |

**Options d'extrusion à maîtriser :**
- *Borgne* (profondeur donnée), *Jusqu'au suivant*, *Jusqu'à la surface*, *À travers tout*
- **Symétrique par rapport au plan** — indispensable pour les pièces symétriques
- **Dépouille** (angle) — obligatoire pour les pièces moulées ou injectées

### 2. Les fonctions d'habillage

Elles s'appliquent **après** la construction du volume brut :

| Fonction | Emploi | Point de vigilance |
|---|---|---|
| **Congé** (rayon) | Supprimer les angles vifs, répartir les contraintes | Ordre d'application crucial : un congé placé trop tôt casse les fonctions suivantes |
| **Chanfrein** | Faciliter le montage, ébavurer | Normaliser : 1×45°, 2×45° |
| **Coque** (*shell*) | Évider une pièce en conservant une épaisseur constante | Pièces plastiques injectées |
| **Nervure** | Rigidifier sans ajouter de masse | Épaisseur ≈ 60 % de la paroi principale |
| **Perçage assisté** | Trous normalisés (taraudés, lamés, fraisés) | Utilise les normes ISO intégrées |
| **Dépouille** | Angle de démoulage | 0,5° à 3° selon le procédé |

### 3. Les fonctions de duplication

**Répétition linéaire**, **circulaire**, **par symétrie**, **pilotée par esquisse** ou
**par table**. Elles évitent de recréer 12 fois le même trou — et surtout, elles permettent de
modifier le nombre d'occurrences d'un seul paramètre.

**Règle :** dupliquer la **fonction**, pas la géométrie. Une répétition de fonction reste
paramétrable ; un copier-coller de faces ne l'est pas.

### 4. Modélisation surfacique

Quand utiliser le surfacique plutôt que le volumique ?

| Situation | Approche |
|---|---|
| Pièce mécanique prismatique | **Volumique** |
| Carrosserie, coque, forme galbée (style) | **Surfacique** |
| Tôlerie complexe dépliable | **Tôlerie** (module dédié) |
| Réparation d'un import STEP défectueux | **Surfacique** (bouchage de trous) |

**Fonctions surfaciques clés :** surface extrudée / révolutionnée / balayée / lissée,
**surface limite** (*boundary*), **surface remplie**, **couture**, **découpe avec surface**,
**épaississement**, **décalage de surface**.

**Continuité des raccords** — vocabulaire de style à connaître :
- **G0** : les surfaces se touchent (arête visible)
- **G1** : tangence (pas de cassure, mais reflet discontinu)
- **G2** : continuité de courbure (**reflet parfaitement fluide** — exigé en carrosserie)

### 5. La stratégie de modélisation — l'ordre compte

**Séquence recommandée, à respecter :**

```
1. Volume brut principal (la forme englobante)
2. Formes secondaires (bossages, nervures)
3. Enlèvements (poches, perçages)
4. Répétitions
5. Habillage : congés, chanfreins, dépouilles   ← TOUJOURS EN DERNIER
6. Coque (si pièce plastique)
```

**Pourquoi les congés en dernier ?** Un congé crée des faces courbes. Si une fonction ultérieure
s'y appuie, la moindre modification de rayon **casse tout l'arbre de création** (erreurs de
régénération en cascade). En les plaçant à la fin, on isole le risque.

### 6. Robustesse d'un modèle

Un modèle robuste est un modèle qui **se régénère sans erreur après modification**.

**Bonnes pratiques :**
- Esquisser sur les **plans de référence** (Face, Dessus, Droite) plutôt que sur des faces du modèle
- Éviter les références à des **arêtes créées par des congés**
- Nommer les fonctions de façon explicite (`Percage_fixation_M8` au lieu de `Enlèvement-extrusion7`)
- Limiter la profondeur de l'arbre : **une pièce de plus de 60 fonctions doit être repensée**
- Utiliser des **plans de construction** pour les géométries complexes
""",
            "formules": """
**VOLUMES DES FORMES DE BASE**

| Forme | Volume |
|---|---|
| Prisme / extrusion | $V = A \\times L$ |
| Cylindre | $V = \\dfrac{\\pi d^2}{4} \\times h$ |
| Cône | $V = \\dfrac{\\pi d^2 h}{12}$ |
| Sphère | $V = \\dfrac{\\pi d^3}{6}$ |
| Tore (Ø méridien $d$, Ø moyen $D$) | $V = \\dfrac{\\pi^2 d^2 D}{4}$ |
| Tronc de cône | $V = \\dfrac{\\pi h}{12}(D^2 + Dd + d^2)$ |

**THÉORÈMES DE GULDIN (révolution)**

Volume engendré par la rotation d'une surface $A$ autour d'un axe :
$$ \\boxed{V = 2\\pi \\, d_G \\, A} $$

Aire engendrée par la rotation d'une ligne de longueur $L$ :
$$ \\boxed{S = 2\\pi \\, d_G \\, L} $$

$d_G$ = distance du centre de gravité du générateur à l'axe de révolution.

**VOLUME D'UNE COQUE (pièce évidée d'épaisseur $e$)**

$$ V_{coque} \\approx S_{intérieure} \\times e $$

Approximation valable si $e \\ll$ dimensions ; sinon soustraire les volumes exacts.

**MASSE ET CENTRE DE GRAVITÉ D'UNE PIÈCE COMPOSÉE**

$$ m = \\sum m_i = \\rho \\sum V_i $$

$$ x_G = \\frac{\\sum m_i x_i}{\\sum m_i} \\qquad y_G = \\frac{\\sum m_i y_i}{\\sum m_i} \\qquad z_G = \\frac{\\sum m_i z_i}{\\sum m_i} $$

⚠️ Pour un **enlèvement de matière**, compter le volume en **négatif** dans les sommes.

**DÉPOUILLE DE DÉMOULAGE**

Surépaisseur induite par un angle de dépouille $\\alpha$ sur une hauteur $h$ :
$$ \\Delta e = h \\times \\tan\\alpha $$

| Procédé | Dépouille usuelle |
|---|---|
| Injection plastique (surface lisse) | 0,5° à 1° |
| Injection plastique (surface grainée) | 1,5° à 3° |
| Moulage sable (fonderie) | 1° à 3° |
| Moulage coquille | 0,5° à 2° |

**RETRAIT AU MOULAGE** (à intégrer dans les cotes de l'empreinte)

$$ L_{empreinte} = L_{pièce} \\times (1 + r) $$

| Matière | Retrait $r$ |
|---|---|
| Fonte | 1,0 % |
| Acier moulé | 2,0 % |
| Aluminium | 1,2 % |
| ABS | 0,5 % |
| PA6-6 | 1,5 % |
| POM | 2,0 % |
""",
            "exemple": """
**Cas industriel — Modélisation d'un carter de pompe en aluminium moulé**

Le carter comporte : un corps cylindrique Ø120, une bride de fixation carrée 160×160,
une volute (canal courbe), 4 pattes de fixation, des nervures de rigidité, et un
alésage Ø52 H7 pour le roulement.

**Arbre de création réel construit par le BE, dans l'ordre :**

| N° | Fonction | Type | Justification de la position dans l'arbre |
|---|---|---|---|
| 1 | Corps cylindrique | Révolution | Volume principal, ancré sur l'origine |
| 2 | Bride carrée | Extrusion symétrique | Deuxième volume, s'appuie sur le plan de référence |
| 3 | Volute | **Balayage** le long d'une spirale | Impossible en extrusion : la section suit une trajectoire courbe |
| 4 | 1 patte de fixation | Extrusion + dépouille 2° | On n'en modélise **qu'une seule** |
| 5 | Répétition circulaire ×4 | Duplication | Le nombre de pattes devient un paramètre modifiable |
| 6 | Nervures | Fonction Nervure, ép. 5 mm | Paroi principale 8 mm → nervure ≈ 60 % = 5 mm |
| 7 | Alésage Ø52 | Enlèvement de révolution | **Après** les volumes, jamais avant |
| 8 | Perçages de bride | Perçage assisté M10 | Utilise la norme intégrée |
| 9 | Répétition linéaire ×4 | Duplication | |
| 10 | **Dépouilles 2°** sur faces verticales | Habillage | Obligatoire pour le démoulage |
| 11 | **Congés R3 et R5** | Habillage | **EN DERNIER** — 47 arêtes traitées en 3 opérations |

**Ce que cet ordre évite concrètement :**

Un stagiaire avait initialement placé les congés en position 4. Résultat : lorsqu'il a voulu
faire passer la bride de 160 à 180 mm, **11 fonctions se sont mises en erreur** car les
perçages étaient référencés sur des arêtes créées par les congés (arêtes qui avaient disparu
ou changé d'identifiant). Il a fallu 2 h de reprise. Avec l'ordre correct, la modification
prend **8 secondes**.

**Vérification de masse par le calcul (contrôle du modèle CAO) :**

Le logiciel annonce $V = 1\\,247\\,000\\ \\mathrm{mm^3}$ pour un alliage **EN AC-46000**
($\\rho = 2\\,700$ kg/m³) :

$$ m = 2\\,700 \\times 1\\,247\\,000 \\times 10^{-9} = \\mathbf{3,37\\ kg} $$

**Contrôle de cohérence par estimation manuelle :** le carter tient approximativement dans un
parallélépipède de 160×160×140 mm, soit $3,58\\times10^6\\ \\mathrm{mm^3}$. Le rapport
$1{,}247/3{,}58 = 35\\ \\%$ de remplissage est **plausible** pour une pièce creuse nervurée
(fourchette habituelle : 25 à 45 %).

> **Réflexe professionnel à acquérir : toujours vérifier l'ordre de grandeur de la masse
> annoncée par le logiciel.** Une masse aberrante trahit soit un matériau mal affecté, soit
> un volume non fermé (fuite dans le modèle surfacique), soit une unité erronée.
""",
            "exercice": """
**Exercice type examen — Poulie moulée et stratégie de modélisation**

Une poulie de renvoi doit être modélisée puis moulée en **EN-GJS-500-7**
($\\rho = 7\\,100$ kg/m³, retrait 1,0 %).

**Géométrie :**
- Jante extérieure : Ø200, largeur 40, épaisseur 12 mm
- Moyeu central : Ø70 extérieur, alésage Ø35 H7, largeur 40 mm
- Liaison jante/moyeu : **voile plein** d'épaisseur 10 mm
- 6 trous d'allègement Ø30, répartis sur un cercle de Ø135
- Congés R4 à tous les raccords
- Dépouille 2° sur les faces du voile

**Questions :**

1. Proposer l'arbre de création complet (ordre des fonctions), en justifiant la position
   des congés et de la dépouille.
2. Calculer le volume de la jante (couronne creuse).
3. Calculer le volume du moyeu (couronne creuse).
4. Calculer le volume du voile plein, puis déduire le volume des 6 trous d'allègement.
5. En déduire le volume total et la masse de la poulie (négliger congés et dépouille).
6. Calculer les dimensions de l'empreinte du moule pour le Ø200 et le Ø35, compte tenu du
   retrait de 1,0 %.
7. L'alésage Ø35 doit être en H7. Peut-on l'obtenir directement de fonderie ?
   Que doit prévoir le concepteur ?
8. Quelle serait la masse si les 6 trous d'allègement étaient supprimés ?
   Le gain justifie-t-il leur usinage ? Discuter.
""",
            "corrige": """
**1. Arbre de création proposé**

| N° | Fonction | Type | Justification |
|---|---|---|---|
| 1 | Profil complet de la poulie (demi-section) | **Révolution** | Une seule révolution génère jante + voile + moyeu d'un coup. C'est la fonction reine des pièces axisymétriques. |
| 2 | Alésage Ø35 | Enlèvement de révolution (ou inclus dans le profil n°1) | Peut être intégré directement au profil esquissé |
| 3 | 1 trou d'allègement Ø30 | Enlèvement-extrusion | On n'en modélise **qu'un seul** |
| 4 | **Répétition circulaire ×6** | Duplication | Le nombre de trous devient un paramètre |
| 5 | **Dépouille 2°** sur les faces du voile | Habillage | Appliquée **avant** les congés : elle modifie l'orientation des faces, donc la géométrie sur laquelle les congés s'appuieront |
| 6 | **Congés R4** | Habillage | **EN DERNIER**, systématiquement |
| 7 | Rainure de clavette (si requise) | Enlèvement-extrusion | Après les congés, car localisée dans l'alésage |

**Justification de l'ordre dépouille → congés :**
La dépouille **incline les faces** ; si les congés étaient posés avant, ils seraient recalculés
sur des faces réorientées et pourraient générer des erreurs de régénération ou des rayons
variables non voulus. La règle est constante : **géométrie fonctionnelle d'abord, habillage
ensuite, congés en tout dernier.**

---

**2. Volume de la jante**

La jante est une **couronne creuse** de Ø extérieur 200, d'épaisseur radiale 12 mm, sur une
largeur de 40 mm.

Diamètre intérieur de la jante :
$$ D_{int} = 200 - 2 \\times 12 = 176\\ \\mathrm{mm} $$

$$ V_{jante} = \\frac{\\pi(D_{ext}^2 - D_{int}^2)}{4} \\times \\ell = \\frac{\\pi(200^2 - 176^2)}{4} \\times 40 $$

$$ V_{jante} = \\frac{\\pi(40\\,000 - 30\\,976)}{4} \\times 40 = \\frac{\\pi \\times 9\\,024}{4} \\times 40 = 7\\,088,2 \\times 40 $$

$$ \\boxed{V_{jante} = 283\\,529\\ \\mathrm{mm^3}} $$

---

**3. Volume du moyeu**

Couronne creuse : Ø extérieur 70, alésage Ø35, largeur 40 mm.

$$ V_{moyeu} = \\frac{\\pi(70^2 - 35^2)}{4} \\times 40 = \\frac{\\pi(4\\,900 - 1\\,225)}{4} \\times 40 $$

$$ V_{moyeu} = \\frac{\\pi \\times 3\\,675}{4} \\times 40 = 2\\,886,0 \\times 40 $$

$$ \\boxed{V_{moyeu} = 115\\,440\\ \\mathrm{mm^3}} $$

---

**4. Volume du voile et des trous d'allègement**

**Voile plein** : couronne de Ø extérieur 176 (intérieur de la jante) à Ø intérieur 70
(extérieur du moyeu), d'épaisseur 10 mm.

$$ V_{voile} = \\frac{\\pi(176^2 - 70^2)}{4} \\times 10 = \\frac{\\pi(30\\,976 - 4\\,900)}{4} \\times 10 $$

$$ V_{voile} = \\frac{\\pi \\times 26\\,076}{4} \\times 10 = 20\\,481,6 \\times 10 = \\mathbf{204\\,816\\ \\mathrm{mm^3}} $$

**Trous d'allègement** : 6 cylindres Ø30, traversant le voile d'épaisseur 10 mm.

$$ V_{1\\ trou} = \\frac{\\pi \\times 30^2}{4} \\times 10 = 706,86 \\times 10 = 7\\,068,6\\ \\mathrm{mm^3} $$

$$ V_{6\\ trous} = 6 \\times 7\\,068,6 = \\mathbf{42\\,412\\ \\mathrm{mm^3}} $$

*Vérification de faisabilité géométrique :* les trous sont sur un cercle de Ø135, soit à un
rayon de 67,5 mm. Le voile s'étend du rayon 35 (moyeu) au rayon 88 (jante). Un trou Ø30
occupe de $67,5 - 15 = 52,5$ à $67,5 + 15 = 82,5$ mm. Ces valeurs sont bien comprises entre
35 et 88 → **les trous sont entièrement dans le voile** ✔️

*Entraxe angulaire :* $360°/6 = 60°$. Distance entre deux centres :
$2 \\times 67,5 \\times \\sin(30°) = 67,5$ mm $> 30$ mm → **pas de recouvrement** ✔️

---

**5. Volume total et masse**

$$ V_{total} = V_{jante} + V_{moyeu} + V_{voile} - V_{6\\ trous} $$

$$ V_{total} = 283\\,529 + 115\\,440 + 204\\,816 - 42\\,412 $$

$$ \\boxed{V_{total} = 561\\,373\\ \\mathrm{mm^3}} $$

**Masse :**
$$ m = \\rho \\times V = 7\\,100 \\times 561\\,373 \\times 10^{-9} $$

$$ \\boxed{m = 3,986\\ \\mathrm{kg} \\approx \\mathbf{3,99\\ kg}} $$

---

**6. Dimensions de l'empreinte du moule (retrait 1,0 %)**

La pièce **se contracte** en refroidissant : l'empreinte doit donc être **plus grande** que
la pièce finie.

$$ L_{empreinte} = L_{pièce} \\times (1 + r) = L_{pièce} \\times 1,01 $$

| Cote pièce | Calcul | Cote empreinte |
|---|---|---|
| Ø200 (jante) | $200 \\times 1,01$ | **Ø202,0 mm** |
| Ø35 (alésage) | $35 \\times 1,01$ | **Ø35,35 mm** |
| Largeur 40 | $40 \\times 1,01$ | **40,4 mm** |
| Ø135 (cercle des trous) | $135 \\times 1,01$ | **Ø136,35 mm** |

⚠️ **Point souvent mal compris :** le retrait s'applique **aussi aux alésages**, dans le même
sens. Le noyau qui forme l'alésage Ø35 doit mesurer Ø35,35 — car en se contractant, la fonte
**se resserre sur le noyau**. (C'est d'ailleurs pourquoi les noyaux de fonderie doivent être
destructibles ou en sable : sinon la pièce les emprisonne.)

---

**7. Obtention de l'alésage Ø35 H7**

**Non, c'est impossible directement de fonderie.**

*Précision de la fonderie :* le moulage sable donne au mieux une tolérance **IT13 à IT15**,
soit pour Ø35 (tranche 30-50) : IT13 = 390 µm, IT15 = 1 000 µm.
*Précision requise :* Ø35 **H7** → IT7 = **25 µm**.

$$ \\frac{390}{25} = 15,6 \\quad \\Rightarrow \\quad \\textbf{la fonderie est 16 fois trop imprécise} $$

Sans compter l'état de surface : Ra 12,5 à 25 en brut de fonderie, contre Ra 1,6 exigé pour
une portée H7.

**Ce que le concepteur doit prévoir :**

1. **Une surépaisseur d'usinage** sur l'alésage : couler un trou brut de **Ø32** (soit 1,5 mm
   de surépaisseur au rayon), puis **aléser à Ø35 H7**.
2. **Des surfaces de mise en position** (appuis usinés ou zones brutes de référence) pour
   reprendre la pièce en machine.
3. **Une surépaisseur sur les faces latérales du moyeu** (0,5 à 1 mm) si elles servent d'appui.
4. Une **gamme d'usinage** : tournage de reprise en 2 phases avec référence sur la jante.
5. Indiquer sur le plan les **surfaces brutes de fonderie** (symbole d'état de surface avec
   cercle = enlèvement de matière interdit) et les **surfaces usinées**.

> **Règle générale à retenir : la fonderie donne la FORME, l'usinage donne la PRÉCISION.**
> Toute surface fonctionnelle (portée, appui, alésage ajusté) doit être reprise en usinage,
> et donc recevoir une surépaisseur au stade de la conception du modèle.

---

**8. Masse sans les trous d'allègement — analyse coût/bénéfice**

$$ V_{sans\\ trous} = 283\\,529 + 115\\,440 + 204\\,816 = 603\\,785\\ \\mathrm{mm^3} $$

$$ m_{sans\\ trous} = 7\\,100 \\times 603\\,785 \\times 10^{-9} = \\mathbf{4,287\\ kg} $$

**Gain de masse apporté par les trous :**
$$ \\Delta m = 4,287 - 3,986 = \\mathbf{0,301\\ kg} \\qquad \\text{soit } \\frac{0,301}{4,287} \\times 100 = \\mathbf{7,0\\ \\%} $$

**Discussion — les arguments à peser :**

| ✅ En faveur des trous | ❌ Contre les trous |
|---|---|
| **Réduction de l'inertie** : les trous sont à R = 67,5 mm, donc leur suppression de matière réduit $J$ de façon significative → **accélération/décélération plus rapides** | **Coût d'usinage** : 6 perçages Ø30 = 6 opérations, soit ~4 à 6 min machine + outillage |
| Économie de matière : 0,3 kg de fonte par pièce | Sur une **pièce moulée**, les trous peuvent être **venus de fonderie** (noyaux) → coût quasi nul, mais moule plus complexe |
| Meilleur refroidissement de la fonte (épaisseurs plus homogènes → moins de retassures) | Concentration de contrainte autour des trous ($K_t \\approx 2,2$) |
| Facilite la manutention (prises de main) | Si la poulie tourne vite, les trous génèrent du **bruit aérodynamique** |

**Calcul complémentaire décisif — le moment d'inertie :**

Le vrai bénéfice n'est pas la masse mais l'**inertie de rotation** $J = \\sum m_i r_i^2$.
Les trous retirent 0,301 kg à un rayon moyen de 67,5 mm :

$$ \\Delta J \\approx 0,301 \\times 0,0675^2 = 1,37\\times10^{-3}\\ \\mathrm{kg\\cdot m^2} $$

Inertie totale approximative de la poulie : $J \\approx 0,020\\ \\mathrm{kg\\cdot m^2}$
→ **réduction d'environ 7 %** de l'inertie également.

**Conclusion argumentée :**

- **Si la poulie est en rotation permanente à vitesse constante** (renvoi de courroie
  classique) : les trous sont **peu justifiés**. 7 % de masse pour 6 opérations d'usinage,
  le retour sur investissement est faible. **On les supprime**, sauf s'ils sont venus de fonderie.

- **Si la poulie subit des démarrages/arrêts fréquents** (axe asservi, machine à cycles
  rapides) : les trous sont **pleinement justifiés**. L'inertie pénalise directement les temps
  de cycle et la consommation du moteur.

- **Si la pièce est produite en grande série moulée** : les trous **venus de fonderie**
  (par noyaux) ne coûtent presque rien et apportent en prime une meilleure santé métallurgique
  (épaisseurs plus régulières → moins de retassures). **On les garde.**

> **La leçon de conception :** un allègement ne se juge jamais en pourcentage de masse seul.
> Il se juge sur **ce que la masse coûte réellement dans l'usage** — inertie, énergie,
> manutention — mis en regard du **surcoût de fabrication**.
""",
        },
        {
            "id": "5.3",
            "titre": "Assemblages, mise en plan et formats d'échange",
            "duree": "14 h",
            "cours": """
### 1. Assemblage : la logique des contraintes

Un assemblage positionne des pièces les unes par rapport aux autres. Chaque pièce libre dans
l'espace possède **6 degrés de liberté** (3 translations + 3 rotations). Les contraintes
d'assemblage les suppriment progressivement.

| Contrainte | DDL supprimés | Usage |
|---|---|---|
| **Coïncidence** (face/face) | 3 (1 T + 2 R) | Mise à plat |
| **Coaxialité** (cylindre/cylindre) | 4 (2 T + 2 R) | Axe dans alésage |
| **Distance** | 1 | Réglage d'un jeu |
| **Angle** | 1 | Orientation |
| **Parallélisme / Perpendicularité** | 2 | Orientation de faces |
| **Tangence** | 1 | Came, galet |

**La première pièce insérée est FIXE par défaut** (ancrée sur l'origine de l'assemblage) :
c'est le bâti. Toutes les autres se positionnent par rapport à elle.

**Erreur classique :** sur-contraindre l'assemblage. Un axe dans un alésage a besoin d'une
**coaxialité** (4 DDL) + une **coïncidence de butée** (1 DDL) = 5 DDL supprimés. Il reste
**1 DDL : la rotation** — c'est exactement ce qu'on veut pour une liaison pivot. Ajouter une
contrainte de plus figerait la simulation de mouvement.

### 2. Assemblage descendant / ascendant

| Méthode | Principe | Quand l'utiliser |
|---|---|---|
| **Ascendant** (*bottom-up*) | On modélise les pièces séparément puis on les assemble | Composants standards, pièces indépendantes |
| **Descendant** (*top-down*) | On esquisse l'assemblage, puis on crée les pièces dedans | Pièces dont les formes dépendent les unes des autres (capot épousant un châssis) |

Le **squelette** (esquisse d'assemblage pilote) est l'outil du descendant : une esquisse
maîtresse définit les entraxes et les encombrements, et toutes les pièces s'y réfèrent.

### 3. Simulation de mouvement et détection d'interférences

Trois vérifications obligatoires avant validation d'un assemblage :

1. **Détection d'interférences** : deux volumes qui se pénètrent → erreur de conception.
   ⚠️ Attention : un ajustement serré (H7/p6) apparaît comme une interférence — c'est normal.
2. **Analyse des jeux** (*clearance*) : distance minimale entre pièces mobiles.
3. **Étude de mouvement** : parcours complet de la course, recherche de collision en position
   intermédiaire (souvent le point critique n'est ni au début ni à la fin).

### 4. Mise en plan à partir du modèle 3D

La mise en plan est **associative** : toute modification du 3D se répercute automatiquement.

**Éléments obligatoires d'un plan de définition :**
- **Cartouche** : titre, indice, échelle, format, auteur, date, projection, matériau, masse
- **Vues** nécessaires et suffisantes (voir fiche 1.2)
- **Cotation complète et fonctionnelle** (fiches 1.3 et 2.1)
- **Tolérances géométriques** (fiche 2.3)
- **États de surface**
- **Tolérances générales** : mention `ISO 2768-mK` (m = moyen, K = classe géométrique)
- **Traitement** et **matériau**

Pour un **plan d'ensemble** s'ajoutent : les **repères** (bulles), la **nomenclature**
(repère / nombre / désignation / matière / observations), et les **cotes d'encombrement**.

### 5. Formats d'échange — le point critique de l'interopérabilité

| Format | Type | Ce qu'il conserve | Usage |
|---|---|---|---|
| **.SLDPRT / .CATPart** | Natif | **Tout** : arbre, paramètres, historique | Travail interne |
| **STEP** (.stp, AP214/AP242) | Neutre **volumique** | Géométrie exacte (BREP), topologie, parfois couleurs. **Perd l'historique** | ✅ **Le standard des échanges industriels** |
| **IGES** (.igs) | Neutre **surfacique** | Surfaces, souvent non cousues | Ancien, à éviter sauf nécessité |
| **Parasolid** (.x_t) | Noyau géométrique | Géométrie exacte | Échange entre logiciels partageant le noyau |
| **STL** | Maillage **triangulaire** | **Approximation** par facettes. Pas de courbes exactes | ✅ **Impression 3D** |
| **3MF** | Maillage enrichi | Maillage + couleurs + matériaux + unités | Impression 3D moderne |
| **PDF 3D / eDrawings** | Visualisation | Vue seule, pas de géométrie exploitable | Revue de projet, client |

**Règle professionnelle :**
> **STEP AP214 pour envoyer une pièce à un usineur. STL (ou 3MF) pour l'impression 3D.
> Jamais l'inverse.**

Envoyer un STL à un usineur est une faute : il ne peut pas en extraire un Ø20 H7, seulement
un polyèdre approché à 0,05 mm près.

### 6. Préparation à l'impression 3D

Paramètres à maîtriser lors de l'export STL :
- **Tolérance de corde** (écart max entre facette et surface réelle) : 0,01 à 0,05 mm
- **Écart angulaire** : 5 à 15°
- Plus le maillage est fin, plus le fichier est lourd (un STL de 200 Mo est ingérable)

Contraintes de conception spécifiques à l'impression FDM :
- **Anisotropie** : la pièce est **30 à 50 % moins résistante** dans l'axe Z (entre couches)
  → orienter la pièce pour que les efforts soient **dans le plan des couches**
- **Porte-à-faux** : au-delà de **45°**, des supports sont nécessaires
- **Trous** : imprimés systématiquement **sous-dimensionnés** (retrait + effet d'escalier)
  → prévoir 0,2 à 0,4 mm de jeu, ou percer après impression
- **Première couche** : prévoir un chanfrein ou un congé de pied pour l'adhérence
""",
            "formules": """
**DEGRÉS DE LIBERTÉ D'UN ASSEMBLAGE**

Un solide libre dans l'espace : **6 DDL** (3 translations + 3 rotations)

$$ DDL_{restants} = 6 - \\sum DDL_{supprimés\\ par\\ contraintes} $$

| Liaison à obtenir | DDL restants | Contraintes CAO typiques |
|---|---|---|
| Encastrement | 0 | Coïncidence + coaxialité + coïncidence plane |
| **Pivot** | 1 (rotation) | Coaxialité + coïncidence de butée |
| **Glissière** | 1 (translation) | 2 coïncidences planes |
| **Pivot glissant** | 2 | Coaxialité seule |
| Rotule | 3 | Coïncidence de points |

**Mobilité d'un mécanisme (formule de Grübler-Kutzbach, plan)**

$$ m = 3(n - 1) - 2 j_1 - j_2 $$

où $n$ = nombre de pièces (bâti compris), $j_1$ = liaisons à 1 DDL (pivot, glissière),
$j_2$ = liaisons à 2 DDL.

*Exemple — mécanisme bielle-manivelle :* $n = 4$, $j_1 = 4$ (3 pivots + 1 glissière), $j_2 = 0$
$$ m = 3(4-1) - 2\\times4 = 9 - 8 = \\mathbf{1} \\quad \\text{✔️ un seul moteur suffit} $$

**TOLÉRANCES GÉNÉRALES ISO 2768-m** (à connaître, elles s'appliquent à toute cote non tolérancée)

| Domaine (mm) | Écart admissible |
|---|---|
| 0,5 à 3 | ± 0,1 |
| 3 à 6 | ± 0,1 |
| 6 à 30 | ± 0,2 |
| 30 à 120 | ± 0,3 |
| 120 à 400 | ± 0,5 |
| 400 à 1000 | ± 0,8 |

**QUALITÉ D'UN MAILLAGE STL**

Erreur de corde maximale pour un cylindre de rayon $R$ maillé avec un angle $\\theta$ par facette :

$$ e = R\\left(1 - \\cos\\frac{\\theta}{2}\\right) $$

*Exemple : $R = 25$ mm, $\\theta = 10°$ → $e = 25(1 - \\cos 5°) = 25 \\times 0,0038 = 0,095$ mm.*
Pour descendre sous 0,01 mm, il faut $\\theta \\approx 3°$, ce qui multiplie le nombre de
facettes par 11.

**ANISOTROPIE EN IMPRESSION FDM**

$$ R_{m,Z} \\approx k \\times R_{m,XY} \\qquad \\text{avec } k = 0,5 \\text{ à } 0,7 $$

**TEMPS D'IMPRESSION (estimation)**

$$ t \\approx \\frac{V_{pièce} \\times (\\text{taux de remplissage}) + V_{supports}}{\\text{débit d'extrusion}} $$

**RETRAIT ET JEU D'ASSEMBLAGE EN FDM**

| Type d'ajustement | Jeu à prévoir au modèle |
|---|---|
| Glissant (pièces mobiles) | 0,3 à 0,5 mm au diamètre |
| Ajusté (montage à la main) | 0,15 à 0,25 mm |
| Serré (montage forcé) | 0 à 0,1 mm |
""",
            "exemple": """
**Cas industriel — Chaîne complète : de la CAO à la pièce imprimée puis usinée**

Un BE conçoit un **support de capteur** pour une ligne de production. Le projet suit deux
chemins parallèles : un prototype imprimé pour valider l'implantation, une série usinée.

**PHASE 1 — Modélisation et assemblage numérique**

| Étape | Action | Contrôle effectué |
|---|---|---|
| 1 | Import du **profilé 40×40 STEP** fourni par le fournisseur | Vérification des unités (mm) et de l'orientation |
| 2 | Modélisation du support en **descendant**, esquissé sur la face du profilé | Le support épouse la rainure automatiquement |
| 3 | Insertion du **capteur STEP** (fichier constructeur) | |
| 4 | Contraintes : coaxialité vis/trou + coïncidence face/face | DDL restants vérifiés = 0 (encastrement) |
| 5 | **Détection d'interférences** | 1 interférence détectée : la tête de vis touche le capteur → décalage de 3 mm |
| 6 | **Analyse de jeu** avec les bouteilles en mouvement | Jeu minimal 12 mm ✔️ (mini requis 8 mm) |

**PHASE 2 — Prototype imprimé (validation d'implantation)**

Export **STL**, tolérance de corde 0,02 mm, écart angulaire 8° → fichier de 4,2 Mo.

Décisions d'impression :

| Paramètre | Choix | Justification |
|---|---|---|
| **Orientation** | Face d'appui à plat sur le plateau | Les efforts de serrage sont **dans le plan des couches** → on évite l'axe Z faible |
| Remplissage | 40 % gyroïde | Compromis rigidité/temps |
| Matière | PETG | Meilleure tenue thermique que le PLA (atelier à 35 °C l'été) |
| Trous Ø8,5 | Modélisés à **Ø8,9** | Compensation du retrait FDM (+0,4 mm) |
| Supports | Aucun | La pièce a été orientée pour que tous les porte-à-faux soient < 45° |

Résultat : prototype en 2 h 40, monté sur ligne le lendemain. **Deux défauts détectés que la
CAO n'avait pas révélés** : le câble du capteur frottait sur une arête (ajout d'un congé R5),
et le support gênait l'accès à la vis de réglage voisine (échancrure ajoutée).

**PHASE 3 — Série usinée**

Export **STEP AP214** vers l'usineur, accompagné du **plan de définition 2D** portant :
- Ø8,5 **H9** sur les trous de fixation
- ⊥ 0,1 A sur la face d'appui du capteur
- Ra 3,2 sur les faces usinées, Ra 6,3 ailleurs
- `ISO 2768-mK` pour les cotes générales
- Matière : **EN AW-6082 T6**, anodisation naturelle 15 µm

**Ce que l'usineur n'aurait PAS pu faire avec le STL :** lire le H9, lire la perpendicularité,
lire le Ra. Le STL ne contient que des triangles — aucune sémantique.

> **La leçon centrale : STL = forme approchée pour prototypage. STEP + plan 2D = définition
> contractuelle de la pièce.** Les deux ne sont pas interchangeables.
""",
            "exercice": """
**Exercice type examen — Assemblage, mobilité et préparation de fabrication**

Un mécanisme de serrage rapide comporte : un **bâti** (1), un **levier** (2) articulé sur le
bâti, une **biellette** (3), et un **poussoir** (4) coulissant dans le bâti.
Liaisons : pivot 1-2, pivot 2-3, pivot 3-4, glissière 4-1.

**PARTIE A — Assemblage numérique**

1. Calculer la mobilité du mécanisme par la formule de Grübler. Combien d'actionneurs faut-il ?
2. Dans le logiciel de CAO, quelles contraintes poser pour réaliser le **pivot 1-2** ?
   Combien de DDL restent supprimés, combien restent libres ?
3. Un stagiaire ajoute une contrainte de parallélisme entre le levier et le bâti.
   Que se passe-t-il ? Expliquer.
4. Citer les **trois vérifications** à effectuer avant de valider un assemblage, et indiquer
   pour chacune une erreur typique qu'elle permet de détecter.

**PARTIE B — Formats d'échange**

Le poussoir (4) est un cylindre Ø20 h7, longueur 90, avec une gorge de circlips et un
chanfrein 1,5×45°.

5. On veut le faire fabriquer par un sous-traitant. Quel(s) fichier(s) lui envoyer ? Justifier.
6. On veut en imprimer un prototype. Quel format ? Quels paramètres d'export ?
7. Le poussoir est maillé en STL avec un écart angulaire de 12°. Calculer l'erreur de corde
   sur le Ø20. Est-ce acceptable pour un prototype d'implantation ? Pour un contrôle
   dimensionnel ?
8. Le prototype imprimé doit coulisser dans un alésage Ø20 également imprimé.
   Quelle cote modéliser pour le poussoir ? Justifier.
9. Le sous-traitant renvoie un STEP dont l'alésage mesure Ø19,987. Est-ce conforme au h7 ?
   *(Donnée : tranche 18-30, IT7 = 21 µm.)* Attention au piège de l'énoncé.
""",
            "corrige": """
**PARTIE A — ASSEMBLAGE NUMÉRIQUE**

**1. Mobilité du mécanisme**

Inventaire :
- **Pièces** : bâti (1), levier (2), biellette (3), poussoir (4) → $n = 4$
- **Liaisons à 1 DDL** : pivot 1-2, pivot 2-3, pivot 3-4, glissière 4-1 → $j_1 = 4$
- **Liaisons à 2 DDL** : aucune → $j_2 = 0$

$$ m = 3(n-1) - 2j_1 - j_2 = 3(4-1) - 2\\times4 - 0 = 9 - 8 = \\mathbf{1} $$

$$ \\boxed{\\textbf{Mobilité } m = 1 \\;\\Rightarrow\\; \\textbf{UN SEUL actionneur suffit}} $$

**Interprétation physique :** en imposant une seule grandeur d'entrée — ici l'**angle du levier**,
actionné à la main — toutes les autres positions sont **entièrement déterminées**. C'est
précisément ce qu'on attend d'un mécanisme de serrage : un geste, une position de sortie.

*C'est le mécanisme bielle-manivelle classique, celui du moteur à explosion et de la presse
à genouillère.*

---

**2. Contraintes CAO pour le pivot 1-2**

| Contrainte | DDL supprimés |
|---|---|
| **Coaxialité** entre l'axe du levier et l'alésage du bâti | **4** (2 translations + 2 rotations) |
| **Coïncidence** de la face d'appui du levier sur le bâti (butée axiale) | **1** (la translation restante le long de l'axe) |
| | **Total : 5** |

$$ DDL_{restants} = 6 - 5 = \\mathbf{1} \\;\\Rightarrow\\; \\textbf{la ROTATION autour de l'axe} $$

C'est bien la définition d'une **liaison pivot** : 1 degré de liberté en rotation. ✔️

*Remarque : la coïncidence de face supprime en théorie 3 DDL (1 T + 2 R), mais 2 des rotations
sont déjà supprimées par la coaxialité. Le logiciel ne compte que le DDL **effectivement**
nouvellement supprimé, soit 1. C'est pourquoi il faut raisonner en DDL restants, pas en
addition brute.*

---

**3. Conséquence de la contrainte de parallélisme ajoutée**

$$ \\boxed{\\textbf{L'assemblage devient SURCONTRAINT}} $$

**Ce qui se passe concrètement :**

Le pivot 1-2 ne laissait qu'**un seul DDL** : la rotation du levier. Ajouter un parallélisme
entre le levier et le bâti **fige cette rotation** — le seul degré de liberté restant.

Deux cas selon le logiciel :

| Cas | Réaction du logiciel |
|---|---|
| La position actuelle **satisfait** le parallélisme | La contrainte est acceptée, mais **le levier ne peut plus tourner**. L'étude de mouvement devient impossible, la mobilité tombe à $m = 0$ : le mécanisme est **bloqué**. |
| La position actuelle **ne satisfait pas** le parallélisme | **Message d'erreur** : « Contraintes en conflit » ou « Impossible de résoudre ». La contrainte apparaît en rouge dans l'arbre. |

**Diagnostic à formuler :** le stagiaire a confondu **positionner** et **contraindre**. S'il
voulait simplement placer le levier dans une position particulière pour une capture d'écran,
il fallait utiliser une contrainte **d'angle avec option « supprimer »**, ou déplacer
librement la pièce — pas ajouter une contrainte permanente.

**Règle générale :** *dans un assemblage destiné à la simulation, on ne contraint jamais les
DDL qui correspondent aux mouvements réels du mécanisme.*

---

**4. Les trois vérifications avant validation**

| Vérification | Ce qu'elle détecte | Erreur typique révélée |
|---|---|---|
| **1. Détection d'interférences** (*interference detection*) | Deux volumes qui s'interpénètrent | Une vis trop longue qui traverse et ressort ; une nervure qui percute un capot. ⚠️ **Un ajustement serré H7/p6 apparaît comme interférence — c'est normal, il faut savoir l'écarter du diagnostic.** |
| **2. Analyse des jeux** (*clearance verification*) | Distance minimale entre pièces mobiles | Un câble ou un flexible qui frotte ; un jeu de 0,2 mm là où il en faut 5 pour la dilatation thermique |
| **3. Étude de mouvement** (*motion study*) sur la course complète | Collision en **position intermédiaire** | **Le cas le plus vicieux** : les positions extrêmes sont libres, mais le mécanisme percute à mi-course. Une vérification statique en position initiale ne le voit pas. |

*Une quatrième vérification, souvent oubliée mais attendue en examen :* le contrôle de la
**masse et du centre de gravité** de l'assemblage, qui révèle immédiatement un matériau mal
affecté ou un volume non fermé.

---

**PARTIE B — FORMATS D'ÉCHANGE**

**5. Fichiers à envoyer au sous-traitant**

$$ \\boxed{\\textbf{STEP AP214 (.stp) + PLAN DE DÉFINITION 2D (PDF)}} $$

**Justification détaillée :**

| Fichier | Rôle | Pourquoi indispensable |
|---|---|---|
| **STEP AP214** | Géométrie **exacte** (BREP) | Permet la programmation FAO directement sur le modèle. Format neutre lisible par tous les logiciels (contrairement au natif .SLDPRT). Conserve les courbes analytiques exactes — un cylindre reste un cylindre. |
| **Plan 2D (PDF)** | **Définition contractuelle** | Porte le **Ø20 h7**, la géométrie de la gorge, les **états de surface**, les tolérances générales `ISO 2768-mK`, la **matière** et le **traitement**. Ces informations n'existent **nulle part** dans le STEP. |

**Pourquoi PAS de STL :** un STL ne contient que des triangles. Il est impossible d'en extraire
un h7 (21 µm de tolérance) puisque le maillage lui-même introduit une erreur bien supérieure.
L'usineur ne saurait même pas quelle surface est fonctionnelle.

**Pourquoi PAS le format natif seul :** le sous-traitant peut travailler sous CATIA, Mastercam
ou TopSolid. Le natif SolidWorks serait illisible chez lui.

*Bon usage complémentaire :* joindre aussi un **PDF 3D ou eDrawings** pour que l'atelier puisse
visualiser la pièce sans licence CAO.

---

**6. Format et paramètres pour l'impression 3D**

$$ \\boxed{\\textbf{STL binaire (ou 3MF)}} $$

**Paramètres d'export recommandés :**

| Paramètre | Valeur | Justification |
|---|---|---|
| **Tolérance de corde** | 0,02 mm | Bien inférieure à la précision de l'imprimante FDM (~0,1 mm) : le maillage n'est pas le facteur limitant |
| **Écart angulaire** | 5 à 8° | Compromis qualité/poids de fichier sur les surfaces cylindriques |
| **Format** | **Binaire** | 5 à 6 fois plus léger que l'ASCII, pour une information identique |
| **Unités** | **millimètres** | Erreur classique : un export en pouces donne une pièce 25,4 fois trop petite |

**Le 3MF est préférable quand c'est possible** : il embarque les unités, les couleurs, le
matériau et les métadonnées, ce qui supprime toute ambiguïté d'échelle.

---

**7. Erreur de corde pour un écart angulaire de 12°**

$$ e = R\\left(1 - \\cos\\frac{\\theta}{2}\\right) $$

Avec $R = 10$ mm (rayon du Ø20) et $\\theta = 12°$ :

$$ \\frac{\\theta}{2} = 6° \\qquad \\cos 6° = 0,99452 $$

$$ e = 10 \\times (1 - 0,99452) = 10 \\times 0,005478 $$

$$ \\boxed{e = 0,0548\\ \\mathrm{mm} \\approx 55\\ \\mu m} $$

**Interprétation selon l'usage :**

| Usage | Verdict | Analyse |
|---|---|---|
| **Prototype d'implantation** | ✅ **ACCEPTABLE** | 55 µm est très inférieur à la précision réelle d'une imprimante FDM (100 à 200 µm). L'erreur de maillage est **noyée dans l'erreur du procédé** : elle ne se verra pas. |
| **Contrôle dimensionnel** | ❌ **INACCEPTABLE** | Le Ø20 **h7** a un IT de **21 µm**. L'erreur de maillage seule (55 µm) est **2,6 fois plus grande que la tolérance totale**. Le STL est structurellement incapable de porter cette information. |

$$ \\frac{55}{21} = 2,6 \\quad \\Rightarrow \\quad \\textbf{le maillage à lui seul consomme 260 \\% de l'IT} $$

**Conclusion à formuler :** *un fichier STL n'est jamais un document de contrôle dimensionnel,
quelle que soit la finesse du maillage.* Même à 3° d'écart angulaire ($e = 3,4$ µm), le format
resterait inadapté car il ne porte **aucune tolérance, aucune référence, aucun état de surface**.
Le contrôle se fait sur le **plan 2D** et le modèle **STEP**.

---

**8. Cote à modéliser pour le poussoir imprimé**

Les **deux pièces** (poussoir et alésage) sont imprimées en FDM, où les trous sortent
systématiquement **sous-dimensionnés** et les cylindres extérieurs **sur-dimensionnés**
(sur-extrusion, effet de coin, dilatation du fil).

**Jeu à prévoir pour un ajustement glissant en FDM : 0,3 à 0,5 mm au diamètre** (voir formulaire).

$$ \\boxed{\\text{Modéliser le poussoir à } \\mathbf{Ø19,6\\ mm} \\text{ pour un alésage modélisé à Ø20}} $$

soit un jeu nominal de **0,4 mm au diamètre** (0,2 mm au rayon).

**Justification détaillée :**

| Effet | Conséquence | Compensation |
|---|---|---|
| Sur-extrusion sur le contour extérieur | Le poussoir sort **plus gros** de +0,1 à 0,2 mm | Réduire la cote modélisée |
| Effet de « coin arrondi » sur les trous | L'alésage sort **plus petit** de −0,1 à 0,3 mm | Idem |
| Retrait thermique différentiel | Variable selon la matière (PLA ≈ 0,3 %, ABS ≈ 0,7 %) | Marge de sécurité |
| Rugosité des couches (strates) | Frottement accru | Jeu supplémentaire |

⚠️ **Ne PAS modéliser Ø20 h7 comme sur le plan de la pièce usinée.** C'est l'erreur la plus
fréquente : on exporte le modèle « propre » et les deux pièces sont **impossibles à assembler**
(ou au contraire flottantes). La compensation est **spécifique au procédé** et doit être
appliquée sur une **copie** du modèle destinée à l'impression, jamais sur le modèle maître.

*Bonne pratique en BE :* créer une **configuration « prototype FDM »** dans le fichier pièce,
avec les cotes compensées, distincte de la configuration « série usinée ».

---

**9. Contrôle du Ø19,987 — le piège de l'énoncé**

**Décodage du Ø20 h7 :**
- Tranche de dimension : $18 < 20 \\le 30$ → **tranche 18 à 30 mm**
- IT7 = **21 µm = 0,021 mm**
- Lettre **h** (arbre) → par définition $es = 0$
$$ ei = es - IT = 0 - 21 = -21\\ \\mu m $$

$$ \\boxed{Ø20\\ h7 \\;\\Rightarrow\\; 19,979 \\le d \\le 20,000\\ \\mathrm{mm}} $$

**Vérification de la mesure :**
$$ 19,979 \\;\\le\\; 19,987 \\;\\le\\; 20,000 \\quad ✔️ $$

$$ \\boxed{\\textbf{La cote 19,987 est CONFORME au Ø20 h7}} $$

**⚠️ LE PIÈGE DE L'ÉNONCÉ — c'est le point noté :**

L'énoncé dit *« le sous-traitant renvoie un STEP dont **l'alésage** mesure Ø19,987 »*.

Or **le poussoir est un ARBRE, pas un alésage.** La désignation **h7** est en **minuscule**,
donc elle s'applique **obligatoirement à un arbre** (convention absolue vue en fiche 2.1 :
majuscules = alésages, minuscules = arbres).

**Il y a donc une incohérence dans l'énoncé, qu'il faut relever :**

- Si l'on contrôle bien **le poussoir Ø20 h7** (arbre), la valeur 19,987 est **conforme** ✔️
- Si l'on contrôle réellement **un alésage**, la désignation h7 est **impossible** : il faudrait
  écrire **H7** (Ø20 +0,021/0 → 20,000 à 20,021), et 19,987 serait alors **REBUTÉE**
  (trop petit de 13 µm).

**Réponse attendue en copie :**

> *« La cote 19,987 est conforme au Ø20 h7 **si elle concerne le poussoir (arbre)**, ce qui est
> le cas d'après la Partie B. L'énoncé emploie improprement le terme « alésage » : le h7 étant
> en minuscule, il s'applique nécessairement à un arbre. Si la mesure portait effectivement sur
> un alésage, la spécification devrait être H7 et la pièce serait non conforme. »*

**Second point de vigilance à mentionner :** une cote **mesurée sur un fichier STEP** n'est pas
une **cote de contrôle**. Le STEP reproduit le modèle nominal du sous-traitant, **pas la pièce
réellement usinée**. Le contrôle de conformité se fait sur la **pièce physique**, avec un
micromètre ou une MMT, jamais sur un fichier. Un sous-traitant qui envoie un STEP « conforme »
n'a rien prouvé sur sa production.
""",
        },
    ],
}


BLOC_6 = {
    "id": "bloc6",
    "titre": "Bloc 6 — Liaisons mécaniques et conception d'ensembles",
    "resume": "Assembler, guider, transmettre : les solutions constructives du mécanicien.",
    "fiches": [
        {
            "id": "6.1",
            "titre": "Liaisons mécaniques et schéma cinématique",
            "duree": "10 h",
            "cours": """
### 1. Le concept de liaison

Une **liaison** est le résultat du contact entre deux solides. Elle **supprime** certains
degrés de liberté et en **autorise** d'autres. Un solide libre dans l'espace possède
**6 degrés de liberté** : 3 translations (Tx, Ty, Tz) et 3 rotations (Rx, Ry, Rz).

$$ \\text{Nombre de DDL de la liaison} + \\text{Degré d'hyperstatisme local} = 6 $$

### 2. Les 11 liaisons normalisées (NF EN ISO 3952)

| Liaison | DDL | Mouvements autorisés | Réalisation typique |
|---|---|---|---|
| **Encastrement** | **0** | aucun | Vissage, soudure, frettage, clavetage + épaulement |
| **Pivot** | **1** | 1 rotation | Roulements, palier lisse + butée |
| **Glissière** | **1** | 1 translation | Queue d'aronde, rail à billes |
| **Hélicoïdale** | **1** | rotation **liée** à translation | Vis-écrou |
| **Pivot glissant** | **2** | 1 rotation + 1 translation (même axe) | Arbre lisse dans bague |
| **Rotule (sphérique)** | **3** | 3 rotations | Rotule de direction, articulation à bille |
| **Appui plan** | **3** | 2 translations + 1 rotation | Deux surfaces planes en contact |
| **Linéaire annulaire** | **4** | 3 rotations + 1 translation | Sphère dans cylindre |
| **Linéaire rectiligne** | **4** | 2 T + 2 R | Cylindre sur plan |
| **Sphère-plan (ponctuelle)** | **5** | 3 R + 2 T | Bille sur plan |
| **Sphérique à doigt** | **2** | 2 rotations | Rotule + ergot |

**Les 4 à connaître par cœur pour le BTS : encastrement, pivot, glissière, pivot glissant.**
Ce sont 90 % des cas réels.

### 3. Le schéma cinématique

C'est une **représentation symbolique minimale** d'un mécanisme : on ne dessine ni les formes,
ni les dimensions, seulement les **liaisons** et les **classes d'équivalence**.

**Méthode en 4 étapes :**

1. **Identifier les classes d'équivalence** : regrouper toutes les pièces qui n'ont **aucun
   mouvement relatif** entre elles (elles forment un même « bloc »). Les vis, clavettes,
   goupilles, roulements font partie du bloc qu'ils solidarisent.
2. **Colorier** chaque classe sur le dessin d'ensemble (méthode de travail éprouvée).
3. **Identifier les liaisons** entre classes (une liaison par couple de classes en contact).
4. **Tracer** le schéma avec les symboles normalisés, en respectant les positions relatives
   et les axes.

**Graphe de liaisons** : outil intermédiaire très utile. Un cercle par classe, un trait par
liaison, avec le nom de la liaison et son axe.

### 4. Isostatisme et hyperstatisme

**Isostatique** : chaque degré de liberté est supprimé **exactement une fois**. Le montage est
possible sans déformer les pièces, les efforts sont bien définis.

**Hyperstatique** : un même degré est supprimé **plusieurs fois**. Conséquences :
- ✅ Meilleure **rigidité** et répartition des charges
- ❌ **Montage impossible** sans jeu ou sans déformation
- ❌ Exigences de **précision géométrique** très sévères (coaxialité, parallélisme)
- ❌ Efforts **indéterminés** par la statique seule

**Degré d'hyperstatisme :**
$$ h = 6(n-1) - \\sum(\\text{DDL supprimés}) + m $$

**Exemple canonique — arbre sur deux paliers :**

| Solution | Liaisons | Nature |
|---|---|---|
| 2 roulements à billes (2 pivots) | pivot + pivot | **Hyperstatique de degré 4** — exige une coaxialité parfaite des logements |
| 1 pivot + 1 pivot glissant | pivot + pivot glissant | **Isostatique** ✅ — c'est le **montage à palier libre**, standard en réducteur |

> **Le montage « un palier fixe + un palier libre » est LA solution industrielle de référence.**
> Il rend le système isostatique et permet à l'arbre de **dilater** librement.

### 5. La mise en position isostatique (MiP)

Pour poser une pièce sur un montage d'usinage, on applique la règle **3-2-1** :

| Appui | Nombre de points | DDL supprimés |
|---|---|---|
| **Appui plan** (primaire) | 3 points | 3 (1 T + 2 R) |
| **Appui linéaire** (secondaire) | 2 points | 2 (1 T + 1 R) |
| **Appui ponctuel** (tertiaire) | 1 point | 1 (1 T) |
| | **6 points** | **6 DDL → pièce isostatiquement posée** |

C'est exactement la logique des **références A, B, C** du tolérancement géométrique
(fiche 2.3). **MiP et tolérancement géométrique sont les deux faces d'une même pièce.**
""",
            "formules": """
**DEGRÉS DE LIBERTÉ**

$$ \\text{DDL d'un solide libre dans l'espace} = 6 $$
$$ \\text{DDL d'un solide libre dans le plan} = 3 $$

**MOBILITÉ D'UN MÉCANISME — formule générale (espace)**

$$ m = 6(n-1) - \\sum_{i} (6 - DDL_i) $$

où $n$ = nombre de solides (bâti compris), $DDL_i$ = degrés de liberté de la liaison $i$.

**Formule dans le plan (Grübler) :**
$$ m = 3(n-1) - 2j_1 - j_2 $$

**DEGRÉ D'HYPERSTATISME**

$$ \\boxed{h = m_c - m_u} $$

où $m_c$ = mobilité calculée, $m_u$ = mobilité utile (réellement souhaitée).

Formule équivalente :
$$ h = 6(n-1) - \\sum(6 - DDL_i) - m_u \\quad \\text{... exprimée en inconnues statiques} $$

**En pratique en BTS, on retient :**
$$ h = I_s - E_s $$
$I_s$ = nombre d'inconnues statiques, $E_s$ = nombre d'équations d'équilibre indépendantes
(6 par solide isolé, 3 dans le plan).

| Valeur de $h$ | Interprétation |
|---|---|
| $h = 0$ | **Isostatique** — montage facile, efforts calculables |
| $h > 0$ | **Hyperstatique** — rigide mais exigeant en précision |

**INTERPRÉTATION DES RÉSULTATS DE MOBILITÉ**

| $m$ | Signification |
|---|---|
| $m = 0$ | Structure **fixe** (treillis, bâti) |
| $m = 1$ | Mécanisme à **1 entrée** (le cas le plus courant) |
| $m \\ge 2$ | Plusieurs actionneurs nécessaires (robot, machine multi-axes) |
| $m < 0$ | Système **hyperstatique** — vérifier le calcul |

**LOI ENTRÉE-SORTIE — mécanisme bielle-manivelle**

Position du piston en fonction de l'angle de manivelle $\\theta$ :

$$ x = R\\cos\\theta + \\sqrt{L^2 - R^2\\sin^2\\theta} $$

avec $R$ le rayon de manivelle et $L$ la longueur de bielle.

Course du piston : $C = 2R$
""",
            "exemple": """
**Cas industriel — Analyse d'un vérin pneumatique et de son mécanisme de bridage**

Un dispositif de bridage sur une machine d'assemblage comporte : le **bâti** (1), le **corps
du vérin** (2) fixé au bâti, la **tige + piston** (3), la **biellette** (4), et le
**levier de bridage** (5) articulé sur le bâti.

**Étape 1 — Classes d'équivalence**

| Classe | Pièces regroupées | Justification |
|---|---|---|
| **A** (bâti) | Bâti, corps du vérin, vis de fixation, axes fixes | Le corps du vérin est **vissé** au bâti : aucun mouvement relatif → même classe |
| **B** | Tige, piston, écrou de tige, joint | Solidaires entre eux |
| **C** | Biellette + ses bagues | |
| **D** | Levier de bridage + patin de serrage | |

**Étape 2 — Graphe de liaisons**

```
        pivot glissant (axe x)
   A ─────────────────────────── B
   │                             │
   │ pivot (axe z)               │ pivot (axe z)
   │                             │
   D ─────────────────────────── C
              pivot (axe z)
```

**Étape 3 — Calcul de mobilité (dans le plan)**

$n = 4$ classes ; liaisons : 3 pivots + 1 pivot glissant.
En schéma plan, le pivot glissant se comporte comme une **glissière** (1 DDL) car la rotation
est bloquée par le guidage de la tige :

$$ m = 3(4-1) - 2 \\times 4 = 9 - 8 = \\mathbf{1} $$

✔️ **Un seul actionneur (le vérin) suffit.** Le mécanisme est cinématiquement correct.

**Étape 4 — Analyse de l'hyperstatisme réel du guidage de tige**

Dans le vérin réel, la tige est guidée par **deux bagues** (une à l'avant du corps, une sur le
piston). Deux pivots glissants coaxiaux sur le même axe = **hyperstatisme de degré 4**.

**Pourquoi c'est acceptable ici :** les deux bagues sont **usinées dans le même corps, en une
seule prise**, ce qui garantit une coaxialité de quelques centièmes. Le constructeur du vérin
maîtrise cette contrainte. C'est un hyperstatisme **assumé et rentable** : il apporte la
rigidité nécessaire pour reprendre les efforts radiaux parasites.

**Le contre-exemple qui illustre le danger :** si le concepteur du bridage avait ajouté un
**troisième guidage** de la tige sur le bâti (par exemple une bague de guidage extérieure),
l'hyperstatisme serait devenu **incontrôlable** : la moindre imprécision de position entre le
bâti et le vérin créerait un effort de flexion sur la tige, un grippage, et une usure
prématurée du joint. **On ne guide jamais une tige de vérin une seconde fois.**

> **Règle de conception :** l'articulation d'un vérin sur son bâti se fait toujours par une
> liaison **laissant au moins un DDL** (chape à axe, tourillon, rotule) — jamais par un
> encastrement rigide aux deux extrémités.
""",
            "exercice": """
**Exercice type examen — Étude cinématique d'un système de levage à ciseaux**

Une table élévatrice à ciseaux comporte : le **châssis fixe** (1), deux **bras croisés**
(2) et (3) articulés entre eux en leur milieu, le **plateau** (4), et un **vérin** dont on
notera le corps (5) et la tige (6).

Liaisons identifiées :
- Bras (2) / châssis (1) : **pivot** en A
- Bras (3) / châssis (1) : **pivot glissant** (galet dans rail) en B
- Bras (2) / bras (3) : **pivot** central en C
- Bras (2) / plateau (4) : **pivot glissant** en D
- Bras (3) / plateau (4) : **pivot** en E
- Corps du vérin (5) / châssis (1) : **pivot** en F
- Tige (6) / corps (5) : **pivot glissant** en G
- Tige (6) / bras (2) : **pivot** en H

**Questions :**

1. Établir le **graphe de liaisons** du mécanisme (description textuelle acceptée).
2. Calculer la **mobilité** dans le plan. Combien d'actionneurs sont nécessaires ?
3. Expliquer pourquoi les liaisons en B et D sont des **pivots glissants** et non des pivots
   simples. Que se passerait-il si on les remplaçait par des pivots ?
4. Le plateau doit rester **horizontal** à toute hauteur. Quelle propriété géométrique du
   mécanisme le garantit ? Justifier.
5. Déterminer les **classes d'équivalence** et proposer un schéma cinématique (description
   des symboles et de leur disposition).
6. Le bureau d'études envisage d'ajouter un **second vérin symétrique** pour doubler la
   capacité. Analyser les conséquences sur l'hyperstatisme et formuler une recommandation.
""",
            "corrige": """
**1. Graphe de liaisons**

```
                        (1) CHÂSSIS
                    ╱      │        ╲
        pivot A    ╱  pivot glissant B  ╲  pivot F
                  ╱        │              ╲
              (2) BRAS ─── (3) BRAS      (5) CORPS VÉRIN
                  │  pivot C   │              │
   pivot glissant D│           │pivot E       │ pivot glissant G
                  │           │              │
                  └──── (4) PLATEAU          (6) TIGE
                                              │
              (2) BRAS ──────────────────────┘
                        pivot H
```

**Inventaire des liaisons :**

| Repère | Liaison | Solides | DDL (plan) |
|---|---|---|---|
| A | Pivot | 1-2 | 1 |
| B | Pivot glissant | 1-3 | 2 |
| C | Pivot | 2-3 | 1 |
| D | Pivot glissant | 2-4 | 2 |
| E | Pivot | 3-4 | 1 |
| F | Pivot | 1-5 | 1 |
| G | Pivot glissant | 5-6 | 2 |
| H | Pivot | 2-6 | 1 |

---

**2. Calcul de la mobilité (dans le plan)**

Nombre de solides : $n = 6$ (châssis 1, bras 2, bras 3, plateau 4, corps 5, tige 6)

Dans le plan, un pivot glissant se réduit à une **glissière** (1 DDL) ou reste à 2 DDL selon
la modélisation. **Ici, les liaisons B, D et G autorisent chacune 1 translation ET la rotation
est bloquée par la géométrie** (galet dans rail, tige guidée) → on les modélise en
**glissières à 1 DDL** dans le plan.

$$ j_1 = 8 \\text{ liaisons à 1 DDL} \\qquad j_2 = 0 $$

$$ m = 3(n-1) - 2j_1 - j_2 = 3(6-1) - 2\\times8 - 0 = 15 - 16 = \\mathbf{-1} $$

**Résultat négatif → le mécanisme est HYPERSTATIQUE de degré 1 dans cette modélisation.**

**Analyse à mener (c'est ce qui est attendu) :**

Le résultat $m = -1$ signifie que la formule de Grübler, appliquée brutalement, révèle une
contrainte surabondante. En réalité, **le mécanisme fonctionne** avec **une mobilité utile
$m_u = 1$** (la montée du plateau, pilotée par le vérin).

$$ h = m_c - m_u = -1 - 1 = -2 \\quad \\Rightarrow \\quad \\textbf{hyperstatisme de degré 2} $$

**Origine physique de cet hyperstatisme :** la boucle fermée
`châssis → bras 2 → plateau → bras 3 → châssis` impose une contrainte géométrique
supplémentaire. En pratique, cet hyperstatisme est **résolu par les jeux de fonctionnement**
des galets dans leurs rails.

$$ \\boxed{\\textbf{UN SEUL actionneur (le vérin) est nécessaire}} $$

---

**3. Pourquoi des pivots glissants en B et D**

**Raisonnement géométrique — c'est le cœur de la question :**

Quand la table monte, les deux bras croisés **se redressent** : l'angle qu'ils forment avec
l'horizontale augmente. Or **la longueur des bras est constante**.

$$ \\text{Si } L \\text{ est constante et l'angle } \\alpha \\text{ augmente} \\;\\Rightarrow\\; \\text{la projection horizontale } L\\cos\\alpha \\text{ DIMINUE} $$

Concrètement : la distance horizontale entre les extrémités des bras **se réduit** au fur et
à mesure de la montée. Il faut donc que **les extrémités puissent se rapprocher**.

- En **A** (pivot fixe) et **E** (pivot) : les points sont fixes sur leur solide.
- En **B** et **D** : les extrémités **doivent coulisser** pour absorber la variation
  $\\Delta x = L(\\cos\\alpha_1 - \\cos\\alpha_2)$.

**Que se passerait-il avec des pivots simples en B et D ?**

$$ m = 3(6-1) - 2 \\times 10 = 15 - 20 = -5 $$

Le mécanisme deviendrait **totalement bloqué** (hyperstatisme de degré 6). Physiquement :

| Conséquence | Explication |
|---|---|
| **Blocage complet** | Le quadrilatère châssis-bras-plateau-bras devient un système **triangulé indéformable** |
| Si on force malgré tout | Les bras travaillent en **flexion pure** au lieu de la compression prévue |
| Rupture | L'effort du vérin (plusieurs tonnes) se transforme intégralement en effort de déformation → **rupture des articulations ou flambage des bras** |

*C'est une erreur de conception classique et fatale : oublier une liaison glissante dans une
boucle fermée transforme un mécanisme en structure.*

---

**4. Horizontalité du plateau**

$$ \\boxed{\\textbf{La SYMÉTRIE du mécanisme par rapport au pivot central C}} $$

**Démonstration géométrique :**

Les deux bras (2) et (3) sont de **même longueur** $L$ et articulés **exactement en leur
milieu** en C. Ils forment donc deux triangles isocèles symétriques.

Soit $\\alpha$ l'angle des bras avec l'horizontale :
- Extrémités basses (A et B) : à la hauteur $y = 0$
- Point central C : à la hauteur $y_C = \\dfrac{L}{2}\\sin\\alpha$
- Extrémités hautes (D et E) : à la hauteur $y = L\\sin\\alpha$

**Les deux points d'attache du plateau (D et E) sont à la MÊME hauteur** $L\\sin\\alpha$,
quel que soit $\\alpha$.

$$ y_D = y_E = L\\sin\\alpha \\quad \\forall \\alpha \\;\\Longrightarrow\\; \\textbf{plateau horizontal} $$

**Les trois conditions à respecter impérativement à la fabrication :**

1. **Bras strictement de même longueur** (tolérance serrée sur l'entraxe)
2. **Articulation centrale exactement à mi-longueur** des deux bras
3. **Rails B et D parfaitement horizontaux** et à la même cote

⚠️ Si l'une de ces conditions n'est pas respectée — par exemple un bras 2 mm plus long — le
plateau **s'inclinera progressivement** avec la montée, et l'erreur sera **maximale en position
haute**. C'est le défaut de fabrication le plus courant sur ce type de table.

**Hauteur de levage :**
$$ H = L\\sin\\alpha \\qquad \\text{course maximale pour } \\alpha \\text{ de } \\alpha_{min} \\text{ à } \\alpha_{max} $$

---

**5. Classes d'équivalence et schéma cinématique**

**Classes d'équivalence** (aucun mouvement relatif interne) :

| Classe | Composition |
|---|---|
| **S1** | Châssis + rails + axes fixes en A et F + patins de sol |
| **S2** | Bras (2) + ses bagues et axes solidaires |
| **S3** | Bras (3) + galets d'extrémité |
| **S4** | Plateau + platine de roulement en D + axe en E |
| **S5** | Corps du vérin + fixation en F |
| **S6** | Tige + piston + chape en H |

*Note : les galets, bagues, roulements ne constituent PAS des classes séparées — ils font
partie de la classe qu'ils guident, sauf si l'on étudie finement le contact.*

**Description du schéma cinématique à tracer :**

```
                  ┌─────────── PLATEAU (S4) ───────────┐
                  │                                     │
             [D] ═╪═ glissière                     [E] ─○─ pivot
                  │                                     │
                   ╲                                   ╱
                    ╲          BRAS S2  /  BRAS S3    ╱
                     ╲                ╳              ╱
                      ╲          [C] ─○─ pivot      ╱
                       ╲            ╱   ╲          ╱
                        ╲          ╱     ╲        ╱
              [H] ─○─────╲────────╱       ╲──────╱
                    ╲     ╲      ╱         ╲    ╱
              TIGE S6╲     ╲    ╱           ╲  ╱
                      ╲     ╲  ╱             ╲╱
              [G] ═╪═  ╲     ╲╱              ╱╲
              CORPS S5  ╲    ╱              ╱  ╲
                    ╲    ╲  ╱              ╱    ╲
        ▓▓▓▓▓▓▓▓[F]─○─▓▓▓[A]─○─▓▓▓▓▓▓▓[B]═╪═▓▓▓▓▓▓▓
                       CHÂSSIS S1 (hachuré = bâti)
```

**Symboles à employer :**
- **○** avec trait perpendiculaire : **pivot** (A, C, E, F, H)
- **╪** dans une glissière : **pivot glissant / glissière** (B, D, G)
- **▓▓▓** hachures : le **bâti** (S1)
- Traits pleins reliant les liaisons : les **barres rigides** (bras, plateau)

---

**6. Ajout d'un second vérin symétrique — analyse**

**a) Nouveau calcul de mobilité**

L'ajout du second vérin apporte : 2 solides ($n$ passe de 6 à 8) et 3 liaisons
(pivot F', pivot glissant G', pivot H').

$$ m = 3(8-1) - 2 \\times 11 = 21 - 22 = \\mathbf{-1} $$

Avec $m_u = 1$ (les deux vérins sont pilotés **ensemble**, ils ne constituent qu'une seule
commande) :

$$ h = -1 - 1 = -2 \\;\\rightarrow\\; \\textbf{l'hyperstatisme AUGMENTE de 3 degrés} $$

**b) Conséquences concrètes**

| ✅ Avantages | ❌ Inconvénients |
|---|---|
| **Capacité doublée** (2 × l'effort) | **Synchronisation obligatoire** : si un vérin sort plus vite que l'autre, le plateau se **vrille** |
| Meilleure **répartition des efforts** sur les bras | Les vérins **luttent l'un contre l'autre** en cas de désynchronisation → efforts internes énormes |
| **Redondance** de sécurité en cas de défaillance d'un vérin | Exigences de **précision géométrique** accrues (positions de F' et H' à quelques dixièmes) |
| Réduction de la flexion des bras | Risque de **grippage** des articulations sous les efforts parasites |

**c) Recommandation argumentée**

**⚠️ NE PAS installer deux vérins en parallèle sans dispositif de synchronisation.**

Le problème physique : deux vérins hydrauliques alimentés par la même ligne ne sortent
**jamais** exactement à la même vitesse (différences de frottement, de fuites internes, de
charge). L'écart, même de 1 mm, crée une **torsion du plateau** que les articulations doivent
encaisser — et elles ne sont pas dimensionnées pour cela.

**Trois solutions par ordre de préférence :**

| Solution | Principe | Avis |
|---|---|---|
| **1. Un seul vérin plus gros** ⭐ | Augmenter le Ø du vérin unique et/ou la pression | **Recommandée.** Supprime le problème à la racine. Un vérin Ø100 au lieu de Ø70 double la capacité sans aucun hyperstatisme ajouté. |
| **2. Deux vérins + diviseur de débit** | Un bloc hydraulique répartit le débit à 1-2 % près | Acceptable. Coût du diviseur + réglage. |
| **3. Deux vérins + barre de synchronisation mécanique** | Un arbre de torsion relie les deux côtés | Robuste mais lourd et encombrant. Utilisé sur les grandes tables. |

**Conclusion à formuler en copie :**

> *« Doubler le vérin double la capacité mais augmente l'hyperstatisme de 3 degrés, ce qui rend
> le mécanisme sensible au moindre défaut de synchronisation. La solution la plus simple et la
> plus fiable est d'augmenter le diamètre du vérin unique existant. Si l'encombrement l'interdit,
> deux vérins sont envisageables **à condition impérative** d'installer un diviseur de débit ou
> une synchronisation mécanique. »*

> **Principe général à retenir : on n'ajoute jamais un actionneur en parallèle sans se demander
> qui garantit leur synchronisme. Deux moteurs sur un même arbre, deux vérins sur un même
> plateau, deux ressorts sur une même course — c'est toujours le même problème.**
""",
        },
        {
            "id": "6.2",
            "titre": "Guidage en rotation : paliers et roulements",
            "duree": "12 h",
            "cours": """
### 1. Les trois familles de solutions

| Solution | Principe | Charge | Vitesse | Frottement | Coût |
|---|---|---|---|---|---|
| **Contact direct** (arbre dans alésage) | Glissement métal/métal | Faible | Très faible | Élevé (µ ≈ 0,15) | Très bas |
| **Palier lisse** (coussinet, bague) | Glissement sur matériau antifriction | Moyenne à forte | Faible à moyenne | Moyen (µ ≈ 0,05-0,1) | Bas |
| **Roulement** | Roulement de billes/rouleaux | Forte | Élevée | **Très faible (µ ≈ 0,0015)** | Moyen |

### 2. Paliers lisses

Le **coussinet** est une bague en matériau antifriction (bronze CuSn8, bronze fritté imprégné
d'huile, PTFE, polyamide) **emmanchée serrée** dans le logement, l'arbre tournant **avec jeu**
à l'intérieur.

**Montage type :** logement **H7**, coussinet monté en **p6/r6** (serré), alésage du coussinet
après montage en **H8** avec un arbre en **f7** (jeu).

⚠️ **Point crucial : le coussinet se déforme au montage.** Un coussinet de Ø20 alésé à H8 avant
montage se retrouvera à Ø19,95 après emmanchement serré. D'où deux stratégies :
- **coussinet auto-lubrifiant calibré** : la déformation est prévue par le fabricant
- **alésage après montage** : on rectifie le coussinet une fois en place (solution précise)

**Critère de dimensionnement : la pression × vitesse (facteur PV)**

$$ p = \\frac{F}{d \\cdot L} \\qquad v = \\frac{\\pi d N}{60\\,000} \\qquad PV = p \\times v $$

Chaque matériau a un $PV_{adm}$ à ne pas dépasser (échauffement, fusion du polymère).

### 3. Roulements : les types et leur choix

| Type | Charge radiale | Charge axiale | Vitesse | Rotulage | Emploi |
|---|---|---|---|---|---|
| **Rigide à billes** (6xxx) | ++ | + | +++ | ~0,15° | **Le plus courant, 80 % des cas** |
| Contact oblique (7xxx) | ++ | ++ (1 sens) | ++ | non | Broches, montage par paire |
| **Rouleaux cylindriques** (NUxxx) | +++ | 0 | ++ | non | Fortes charges radiales |
| **Rouleaux coniques** (3xxxx) | +++ | +++ | + | non | Roues de véhicule, montage en O ou X |
| Butée à billes (5xxxx) | 0 | +++ | + | non | Charge axiale pure |
| Rotule sur billes/rouleaux | ++ | + | + | **2-3°** | Défauts d'alignement importants |
| Aiguilles | +++ | 0 | ++ | non | Encombrement radial minimal |

**Désignation d'un roulement rigide à billes 6205 :**
- **6** : série (rigide à billes)
- **2** : série de largeur/diamètre (série légère)
- **05** : $05 \\times 5 = \\mathbf{25\\ mm}$ d'alésage

**Règle de l'alésage :** pour les 2 derniers chiffres ≥ 04, multiplier par 5.
(00 = 10 mm, 01 = 12 mm, 02 = 15 mm, 03 = 17 mm, 04 = 20 mm, 05 = 25 mm…)

### 4. La règle des charges — ce qui détermine les ajustements

C'est **la** notion à maîtriser (déjà rencontrée en fiche 2.2) :

| Situation | Bague concernée | Type de charge | Ajustement |
|---|---|---|---|
| Arbre tournant, charge fixe en direction | Bague **intérieure** | **Tournante** | **Serrée** (k6, m6) |
| Arbre tournant, charge fixe en direction | Bague **extérieure** | **Fixe** | **Glissante** (H7) |
| Alésage tournant (poulie folle), charge fixe | Bague **extérieure** | **Tournante** | **Serrée** (N7, P7) |
| Alésage tournant, charge fixe | Bague **intérieure** | **Fixe** | **Glissante** (g6, h6) |

**Mnémotechnique : la bague qui subit une charge TOURNANTE doit être SERRÉE.**
Sinon elle « rampe » dans son logement et l'use.

### 5. Montage à palier fixe / palier libre

**Principe :** un seul palier assure le **positionnement axial** (palier fixe) ; l'autre laisse
l'arbre **libre de dilater** (palier libre).

| Palier | Rôle | Réalisation |
|---|---|---|
| **Fixe** | Bloque l'arbre axialement dans les deux sens | Bague intérieure ET extérieure épaulées + circlips |
| **Libre** | Reprend la charge radiale seulement | Bague extérieure **libre de coulisser** dans son logement (ou roulement à rouleaux cylindriques) |

**Pourquoi c'est indispensable :** un arbre en acier de 500 mm chauffé de 40 °C s'allonge de
$$ \\Delta L = 11\\times10^{-6} \\times 500 \\times 40 = 0,22\\ \\mathrm{mm} $$
Si les deux paliers étaient fixes, cette dilatation créerait un **effort axial de plusieurs
tonnes** sur les roulements → destruction en quelques heures.

**Deux dispositions classiques pour les roulements à contact oblique :**
- **Montage en X** (directions de charge convergentes vers l'extérieur) : bon pour les arbres
  courts, tolère la dilatation du carter
- **Montage en O** (directions divergentes) : plus grand écartement des points d'application,
  meilleure reprise des moments de basculement (roues de véhicule)

### 6. Lubrification et étanchéité

| Mode | Domaine | Remarque |
|---|---|---|
| **Graisse** | $n \\cdot d_m < 500\\,000$ | 90 % des cas. Remplir à **30-50 %** du volume libre (pas plus : échauffement) |
| **Bain d'huile** | Vitesses élevées, forte charge | Niveau au centre de la bille la plus basse |
| Brouillard d'huile | Très hautes vitesses | Broches de machine-outil |

**Étanchéité :** joints à lèvres (type A ou AS), déflecteurs, chicanes, roulements étanches
(2RS = 2 joints caoutchouc, ZZ = 2 flasques métalliques).
""",
            "formules": """
**DIMENSIONNEMENT D'UN ROULEMENT — durée de vie**

Durée de vie nominale $L_{10}$ (en **millions de tours**) :

$$ \\boxed{L_{10} = \\left(\\frac{C}{P}\\right)^n} $$

- $C$ : **charge dynamique de base** (donnée catalogue, en N)
- $P$ : **charge dynamique équivalente** appliquée (N)
- $n = 3$ pour les roulements à **billes**, $n = 10/3$ pour les roulements à **rouleaux**

Durée de vie en **heures** :

$$ \\boxed{L_{10h} = \\frac{10^6}{60 \\, N} \\left(\\frac{C}{P}\\right)^n} \\qquad N \\text{ en tr/min} $$

**Charge dynamique équivalente** (roulement rigide à billes) :

$$ P = X F_r + Y F_a $$

Avec la règle simplifiée usuelle :
- Si $\\dfrac{F_a}{F_r} \\le e$ : $X = 1$, $Y = 0$ → $P = F_r$
- Si $\\dfrac{F_a}{F_r} > e$ : $X = 0,56$, $Y$ selon catalogue (1,2 à 2,3)

$e \\approx 0,22$ à $0,44$ selon $F_a/C_0$.

**Charge à appliquer pour un dimensionnement — durées usuelles**

| Application | $L_{10h}$ visée |
|---|---|
| Électroménager | 1 000 à 2 000 h |
| Machine-outil | 20 000 à 30 000 h |
| Réducteur industriel (service continu) | 20 000 à 40 000 h |
| Moteur électrique | 20 000 à 30 000 h |
| Roue de véhicule | 5 000 à 10 000 h |

---

**PALIERS LISSES — critère PV**

$$ p = \\frac{F}{d \\times L} \\quad \\mathrm{[MPa]} \\qquad v = \\frac{\\pi \\, d \\, N}{60\\,000} \\quad \\mathrm{[m/s]} $$

$$ \\boxed{PV = p \\times v \\le PV_{adm}} $$

| Matériau du coussinet | $p_{max}$ (MPa) | $v_{max}$ (m/s) | $PV_{adm}$ (MPa·m/s) |
|---|---|---|---|
| Bronze CuSn8 | 25 | 8 | 1,8 |
| Bronze fritté imprégné | 14 | 6 | 1,6 |
| PTFE + bronze (bague composite) | 80 | 2 | 1,8 |
| Polyamide PA6-6 | 10 | 3 | 0,10 |
| POM | 14 | 3 | 0,14 |

**Rapport L/d recommandé pour un palier lisse : 0,5 à 1,5** (au-delà, risque d'arc-boutement).

---

**PUISSANCE PERDUE PAR FROTTEMENT**

$$ P_{perdue} = \\mu \\cdot F \\cdot v \\qquad \\mathrm{[W]} $$

Couple de frottement d'un roulement :
$$ M_f = \\frac{\\mu \\cdot F \\cdot d}{2} \\qquad \\mathrm{[N \\cdot mm]} $$

| Type de guidage | $\\mu$ |
|---|---|
| Roulement à billes | 0,0015 |
| Roulement à rouleaux | 0,0018 |
| Coussinet bronze lubrifié | 0,05 à 0,10 |
| Acier sur acier sec | 0,15 à 0,20 |

---

**DILATATION AXIALE À COMPENSER**

$$ \\Delta L = \\alpha \\cdot L \\cdot \\Delta T $$

**VITESSE LIMITE**

$$ n \\cdot d_m \\le \\text{valeur limite} \\qquad d_m = \\frac{d + D}{2} $$

| Lubrification | Limite $n \\cdot d_m$ (mm·tr/min) |
|---|---|
| Graisse | 500 000 |
| Bain d'huile | 700 000 |
| Brouillard d'huile | 1 500 000 |
""",
            "exemple": """
**Cas industriel — Montage complet de l'arbre intermédiaire d'un réducteur**

Un arbre intermédiaire porte deux pignons et tourne à **480 tr/min**. Les efforts d'engrènement
donnent une charge radiale de **3 200 N** sur le palier gauche et **2 400 N** sur le palier
droit, plus une charge axiale de **850 N** (denture hélicoïdale). Entraxe entre paliers :
**280 mm**. Durée de vie visée : **25 000 h** (service continu 3×8).

**ÉTAPE 1 — Choix de l'architecture**

| Palier | Rôle | Choix |
|---|---|---|
| **Gauche** | **FIXE** — reprend la charge radiale de 3 200 N **et** toute la charge axiale de 850 N | Roulement **rigide à billes 6208**, épaulé des deux côtés (arbre + carter) |
| **Droit** | **LIBRE** — charge radiale seule, laisse dilater | Roulement **rigide à billes 6207**, bague extérieure **libre de coulisser** dans son logement |

*Pourquoi le palier fixe est celui le plus chargé radialement ?* Ce n'est pas obligatoire, mais
c'est cohérent : on place le palier fixe **côté entraînement**, là où les efforts sont maîtrisés
et où l'accès au montage est le plus facile.

**ÉTAPE 2 — Charge équivalente sur le palier fixe (6208)**

Données catalogue du 6208 : $C = 30\\,700$ N, $C_0 = 19\\,000$ N.

$$ \\frac{F_a}{C_0} = \\frac{850}{19\\,000} = 0,045 \\;\\Rightarrow\\; e \\approx 0,26 $$

$$ \\frac{F_a}{F_r} = \\frac{850}{3\\,200} = 0,266 \\;>\\; e = 0,26 $$

Donc $X = 0,56$ et $Y \\approx 1,71$ :

$$ P = 0,56 \\times 3\\,200 + 1,71 \\times 850 = 1\\,792 + 1\\,454 = \\mathbf{3\\,246\\ N} $$

**ÉTAPE 3 — Durée de vie**

$$ L_{10h} = \\frac{10^6}{60 \\times 480}\\left(\\frac{30\\,700}{3\\,246}\\right)^3 = 34,72 \\times (9,458)^3 $$

$$ L_{10h} = 34,72 \\times 846,1 = \\mathbf{29\\,378\\ heures} \\quad ✔️ \\; (>25\\,000\\ h) $$

**ÉTAPE 4 — Ajustements (application de la règle des charges)**

L'arbre tourne, la charge (efforts d'engrènement) est **fixe en direction** :

| Bague | Charge | Ajustement | Cotes (Ø40, tranche 30-50) |
|---|---|---|---|
| Intérieure | **tournante** | **k6** serré | IT6 = 16 µm, ei = +2 → **40,002 / 40,018** |
| Extérieure | **fixe** | **H7** glissant | IT7 = 25 µm → **80,000 / 80,025** (Ø80) |

**ÉTAPE 5 — Vérification de la dilatation**

Arbre en acier, longueur entre paliers 280 mm, échauffement estimé 35 °C :

$$ \\Delta L = 11\\times10^{-6} \\times 280 \\times 35 = \\mathbf{0,108\\ mm} $$

Le palier libre doit permettre **au moins 0,11 mm** de coulissement. Avec le jeu H7/h6 du
logement (0 à 44 µm) plus une longueur de portée suffisante, c'est assuré. ✔️

**ÉTAPE 6 — Montage et lubrification**

- **Ordre de montage :** chauffer les bagues intérieures à 80 °C (jamais plus de 120 °C : le
  revenu du 100Cr6 est à 150 °C), les emmancher, laisser refroidir, puis engager l'arbre dans
  le carter.
- ⚠️ **Ne jamais frapper sur la bague extérieure pour monter la bague intérieure** — l'effort
  transiterait par les billes et **matèrait les pistes** (marques de brinelling). Le roulement
  serait détruit avant sa première rotation.
- **Lubrification :** graisse, vérification $n \\cdot d_m = 480 \\times \\dfrac{40+80}{2} = 28\\,800 \\ll 500\\,000$ ✔️
- **Remplissage :** 30 à 50 % du volume libre du logement.
""",
            "exercice": """
**Exercice type examen — Choix et vérification d'un guidage en rotation**

**PARTIE A — Roulement d'un tambour de convoyeur**

Un tambour d'entraînement de convoyeur à bande tourne à **N = 65 tr/min**. Il est supporté par
**deux roulements identiques**. La charge totale (poids du tambour + tension de la bande) vaut
**F = 14 000 N**, répartie **également** sur les deux paliers. Aucune charge axiale.
L'arbre du tambour a un diamètre de **50 mm** aux portées.

*Données catalogue :*
| Roulement | $d$ | $D$ | $C$ (N) | $C_0$ (N) |
|---|---|---|---|---|
| 6210 | 50 | 90 | 35 100 | 23 200 |
| 6310 | 50 | 110 | 65 000 | 38 000 |
| NU210 (rouleaux) | 50 | 90 | 64 400 | 54 000 |

Durée de vie exigée : **50 000 heures** (installation industrielle, service continu).

1. Calculer la charge radiale sur chaque palier et la charge équivalente $P$.
2. Calculer la durée de vie $L_{10h}$ du **6210**. Conclure.
3. Faire de même pour le **6310** et le **NU210**. Établir un tableau comparatif.
4. Recommander une solution en tenant compte de l'encombrement, du coût et de la fonction.
5. Le tambour tourne dans un carter fixe, la charge est fixe en direction et l'arbre tourne.
   Préciser les ajustements des deux bagues et justifier par la règle des charges.
6. Vérifier la vitesse limite du roulement retenu (lubrification à la graisse).

**PARTIE B — Palier lisse d'un galet de guidage**

Un galet de Ø80 tourne sur un axe fixe Ø25 via un **coussinet en bronze fritté imprégné**
($p_{max} = 14$ MPa, $v_{max} = 6$ m/s, $PV_{adm} = 1,6$ MPa·m/s). Le galet subit une charge
radiale de **1 800 N** et roule à **7 m/min** sur un rail.

7. Calculer la vitesse de rotation du galet, puis la vitesse de glissement dans le coussinet.
8. Déterminer la longueur minimale du coussinet pour respecter $p_{max}$, puis $PV_{adm}$.
   Quelle condition est dimensionnante ?
9. Vérifier le rapport $L/d$ et conclure sur la validité du choix.
""",
            "corrige": """
**PARTIE A — ROULEMENT DE TAMBOUR**

**1. Charge par palier et charge équivalente**

$$ F_r = \\frac{F}{2} = \\frac{14\\,000}{2} = \\mathbf{7\\,000\\ N\\ \\text{par palier}} $$

Aucune charge axiale ($F_a = 0$), donc $X = 1$ et $Y = 0$ :

$$ P = X F_r + Y F_a = 1 \\times 7\\,000 + 0 = \\mathbf{7\\,000\\ N} $$

---

**2. Durée de vie du 6210**

Roulement à **billes** → exposant $n = 3$.

$$ L_{10h} = \\frac{10^6}{60 N}\\left(\\frac{C}{P}\\right)^3 = \\frac{10^6}{60 \\times 65}\\left(\\frac{35\\,100}{7\\,000}\\right)^3 $$

$$ \\frac{10^6}{3\\,900} = 256,4 \\qquad \\frac{35\\,100}{7\\,000} = 5,014 \\qquad 5,014^3 = 126,1 $$

$$ L_{10h} = 256,4 \\times 126,1 = \\mathbf{32\\,332\\ heures} $$

$$ 32\\,332\\ \\mathrm{h} \\;<\\; 50\\,000\\ \\mathrm{h} \\quad ❌ \\;\\; \\textbf{INSUFFISANT} $$

*Le 6210 tiendrait environ 3,7 ans en service continu, contre les 5,7 ans exigés.*

---

**3. Comparaison des trois solutions**

**6310** (billes, $n = 3$) :
$$ \\frac{65\\,000}{7\\,000} = 9,286 \\qquad 9,286^3 = 800,7 $$
$$ L_{10h} = 256,4 \\times 800,7 = \\mathbf{205\\,300\\ heures} \\quad ✔️ $$

**NU210** (rouleaux, $n = 10/3$) :
$$ \\frac{64\\,400}{7\\,000} = 9,200 \\qquad 9,200^{10/3} = e^{(10/3) \\times \\ln 9,2} = e^{3,333 \\times 2,219} = e^{7,397} = 1\\,631 $$
$$ L_{10h} = 256,4 \\times 1\\,631 = \\mathbf{418\\,200\\ heures} \\quad ✔️ $$

**Tableau comparatif :**

| | **6210** | **6310** | **NU210** |
|---|---|---|---|
| Type | Billes | Billes | Rouleaux cylindriques |
| $D$ extérieur | 90 mm | **110 mm** | 90 mm |
| $C$ | 35 100 N | 65 000 N | 64 400 N |
| $L_{10h}$ | **32 332 h** ❌ | **205 300 h** ✔️ | **418 200 h** ✔️ |
| Marge / 50 000 h | −35 % | ×4,1 | ×8,4 |
| Charge axiale supportée | Oui (modérée) | Oui (modérée) | **NON** |
| Encombrement radial | Compact | **+22 %** | Compact |
| Coût relatif | 1 | 1,8 | 2,4 |

---

**4. Recommandation**

$$ \\boxed{\\textbf{Solution retenue : 6310}} $$

**Justification :**

| Critère | Analyse |
|---|---|
| **Durée de vie** | 205 300 h = **4,1 fois** l'exigence. Marge confortable pour absorber les surcharges de démarrage et les variations de tension de bande. |
| **Charge axiale** | Le **NU210 n'en supporte AUCUNE**. Or un convoyeur subit inévitablement des efforts axiaux parasites : bande légèrement désalignée, tambour non parfaitement perpendiculaire, dilatation. **C'est rédhibitoire** — le NU210 est écarté malgré ses performances. |
| **Encombrement** | Le Ø110 au lieu de Ø90 impose un palier plus gros, mais sur un convoyeur industriel l'espace n'est pas critique. |
| **Coût** | +80 % sur le roulement, mais le roulement représente une part faible du coût du tambour. À comparer au coût d'un **arrêt de production** pour changement prématuré. |
| **Standardisation** | Le 6310 est un roulement très courant, disponible partout. |

**Analyse économique décisive :** un remplacement de roulement sur convoyeur immobilise la ligne
4 à 8 heures. Sur 15 ans, le 6210 imposerait **1 à 2 remplacements** supplémentaires. Le
surcoût initial de quelques dizaines d'euros est sans commune mesure.

*Si l'encombrement radial était vraiment critique, la solution serait le **NU210 associé à un
roulement rigide** sur l'autre palier pour reprendre l'axial (montage fixe/libre classique).*

---

**5. Ajustements des bagues**

Configuration : **arbre tournant**, **charge fixe en direction** (le poids et la tension de bande
ne tournent pas).

| Bague | Type de charge subie | Raisonnement | Ajustement |
|---|---|---|---|
| **Intérieure** (sur l'arbre Ø50) | **TOURNANTE** — chaque point de la bague passe successivement sous la zone chargée | Sans serrage, elle « ramperait » sur l'arbre et l'userait | **Ø50 k6** → serré |
| **Extérieure** (dans le carter Ø110) | **FIXE** — la zone chargée reste toujours la même | Pas de tendance au rampement ; on veut pouvoir démonter et laisser dilater | **Ø110 H7** → glissant |

**Cotes calculées :**

*Arbre Ø50 k6* — tranche 30-50 : IT6 = 16 µm ; $ei = +2$ µm → $es = +18$ µm
$$ \\boxed{50,002 \\;\\text{à}\\; 50,018\\ \\mathrm{mm}} $$

*Alésage Ø110 H7* — tranche 80-120 : IT7 = 35 µm ; $EI = 0$ → $ES = +35$ µm
$$ \\boxed{110,000 \\;\\text{à}\\; 110,035\\ \\mathrm{mm}} $$

**Énoncé de la règle :** *« La bague soumise à une charge tournante doit être montée serrée ;
la bague soumise à une charge fixe peut être montée glissante. »*

---

**6. Vérification de la vitesse limite (graisse)**

Diamètre moyen du 6310 :
$$ d_m = \\frac{d + D}{2} = \\frac{50 + 110}{2} = 80\\ \\mathrm{mm} $$

$$ n \\cdot d_m = 65 \\times 80 = \\mathbf{5\\,200\\ mm \\cdot tr/min} $$

$$ 5\\,200 \\;\\ll\\; 500\\,000 \\quad ✔️ \\;\\; \\textbf{TRÈS LARGEMENT VÉRIFIÉ} $$

Le rapport est de **96 fois inférieur** à la limite. La lubrification à la graisse est
parfaitement adaptée — c'est d'ailleurs le cas de toutes les applications lentes.

*Conséquence pratique :* on peut utiliser des **roulements étanches 6310-2RS** (graissés à vie),
ce qui supprime le graisseur et la maintenance périodique. Recommandation à formuler au BE.

---

**PARTIE B — PALIER LISSE DE GALET**

**7. Vitesses**

**a) Vitesse de rotation du galet**

Le galet Ø80 roule sans glisser à 7 m/min sur le rail :

$$ v_{lineaire} = 7\\ \\mathrm{m/min} = \\frac{7}{60} = 0,1167\\ \\mathrm{m/s} $$

$$ N = \\frac{v \\times 1\\,000 \\times 60}{\\pi \\times D_{galet}} = \\frac{7 \\times 1\\,000}{\\pi \\times 80} = \\frac{7\\,000}{251,3} = \\mathbf{27,9\\ tr/min} $$

**b) Vitesse de glissement DANS le coussinet**

⚠️ **Le point clé : la vitesse dans le coussinet se calcule sur le Ø25 de l'axe, PAS sur le Ø80
du galet.** C'est l'erreur classique.

$$ v = \\frac{\\pi \\, d \\, N}{60\\,000} = \\frac{\\pi \\times 25 \\times 27,9}{60\\,000} = \\frac{2\\,191}{60\\,000} $$

$$ \\boxed{v = 0,0365\\ \\mathrm{m/s}} $$

*La vitesse de glissement est 3,2 fois plus faible que la vitesse de roulement, dans le rapport
des diamètres $25/80$. C'est tout l'intérêt d'un galet de grand diamètre sur petit axe.*

---

**8. Longueur minimale du coussinet**

**a) Condition de PRESSION** ($p \\le p_{max} = 14$ MPa)

$$ p = \\frac{F}{d \\times L} \\le 14 \\;\\Longrightarrow\\; L \\ge \\frac{F}{d \\times p_{max}} = \\frac{1\\,800}{25 \\times 14} $$

$$ L \\ge \\frac{1\\,800}{350} = \\mathbf{5,14\\ mm} $$

**b) Condition de PV** ($PV \\le PV_{adm} = 1,6$ MPa·m/s)

$$ PV = p \\times v = \\frac{F}{d \\times L} \\times v \\le 1,6 $$

$$ L \\ge \\frac{F \\times v}{d \\times PV_{adm}} = \\frac{1\\,800 \\times 0,0365}{25 \\times 1,6} = \\frac{65,7}{40} $$

$$ L \\ge \\mathbf{1,64\\ mm} $$

**c) Condition dimensionnante**

| Critère | $L_{min}$ |
|---|---|
| **Pression** $p_{max}$ | **5,14 mm** ⬅️ **DIMENSIONNANTE** |
| Facteur $PV$ | 1,64 mm |

$$ \\boxed{\\textbf{C'est la PRESSION qui dimensionne le coussinet}} $$

**Explication physique :** la vitesse de glissement est **très faible** (0,0365 m/s, soit
2,2 m/min). Le facteur $PV$ traduit l'**échauffement** par frottement ; à cette vitesse, la
chaleur dégagée est négligeable. En revanche, la charge de 1 800 N sur une petite surface
génère une pression importante → risque d'**écrasement (matage)** du bronze.

*Règle générale : à basse vitesse, c'est la pression qui commande ; à haute vitesse, c'est le PV.*

---

**9. Vérification du rapport L/d et conclusion**

Le calcul donne $L_{min} = 5,14$ mm, mais il faut vérifier la **règle de proportion** :

$$ \\frac{L}{d} = 0,5 \\;\\text{à}\\; 1,5 \\quad \\Longrightarrow \\quad L = 12,5 \\;\\text{à}\\; 37,5\\ \\mathrm{mm} $$

$$ \\text{Avec } L = 5,14 : \\quad \\frac{L}{d} = \\frac{5,14}{25} = \\mathbf{0,21} \\;<\\; 0,5 \\quad ❌ $$

**Le coussinet calculé est TROP COURT au regard du rapport L/d.**

**Pourquoi c'est un problème :**

| Risque | Explication |
|---|---|
| **Arc-boutement / basculement** | Un coussinet trop court ne guide pas : le galet peut basculer sur l'axe (« coincement en biais »), comme un tiroir mal guidé |
| **Pression de bord** | Le moindre défaut de perpendicularité concentre la charge sur les arêtes du coussinet → matage local très supérieur au calcul moyen |
| **Fragilité au montage** | Une bague de 5 mm sur Ø25 est difficile à emmancher droite |

**Longueur retenue :**

$$ \\boxed{L = 20\\ \\mathrm{mm} \\;\\Rightarrow\\; \\frac{L}{d} = \\frac{20}{25} = 0,8 \\quad ✔️} $$

**Vérifications finales avec L = 20 mm :**

$$ p = \\frac{1\\,800}{25 \\times 20} = \\mathbf{3,6\\ MPa} \\;\\le\\; 14\\ \\mathrm{MPa} \\quad ✔️ \\;(\\text{coefficient } 3,9) $$

$$ v = 0,0365\\ \\mathrm{m/s} \\;\\le\\; 6\\ \\mathrm{m/s} \\quad ✔️ \\;(\\text{coefficient } 164) $$

$$ PV = 3,6 \\times 0,0365 = \\mathbf{0,131\\ MPa\\cdot m/s} \\;\\le\\; 1,6 \\quad ✔️ \\;(\\text{coefficient } 12) $$

**CONCLUSION :**

Le choix d'un **coussinet en bronze fritté imprégné Ø25 × Ø31 × 20** (dimensions normalisées
courantes) est **parfaitement validé**, avec des marges très confortables sur les trois critères.

**Ce que l'exercice enseigne — la leçon centrale :**

> **Un calcul de RDM ou de tribologie donne un MINIMUM, jamais une dimension de plan.**
> Ici, le calcul de pression autorise 5,14 mm, mais les règles de proportion imposent 20 mm.
> Les règles empiriques (L/d, épaisseur minimale, diamètres normalisés) **encadrent** toujours
> le résultat du calcul. Un technicien qui ne retiendrait que le calcul concevrait une pièce
> qui ne fonctionne pas.

*Recommandation complémentaire :* prévoir un **jeu de fonctionnement** entre axe et coussinet
de l'ordre de **H8/f7** (soit 20 à 74 µm sur Ø25), et un **épaulement ou circlips** pour
l'immobilisation axiale du galet.
""",
        },
        {
            "id": "6.3",
            "titre": "Guidage en translation, assemblages et transmission de puissance",
            "duree": "12 h",
            "cours": """
### 1. Guidage en translation

**Principe :** ne laisser qu'**un seul degré de liberté**, la translation selon un axe.

| Solution | Précision | Charge | Frottement | Coût |
|---|---|---|---|---|
| Glissière prismatique (queue d'aronde) | ++ | +++ | Élevé | Moyen |
| Arbres cylindriques + douilles à billes | ++ | + | Très faible | Moyen |
| **Rail à billes / patins (guidage linéaire)** | +++ | ++ | Très faible | Élevé |
| Glissière à galets | + | ++ | Faible | Bas |
| Cylindre + clavette (anti-rotation) | + | + | Moyen | Bas |

**Le problème de l'arc-boutement** — phénomène à comprendre absolument :

Quand l'effort moteur est appliqué **loin** de la glissière (grand porte-à-faux), le coulisseau
tend à se coincer. La condition de non-arc-boutement s'écrit :

$$ \\frac{L_{guidage}}{d_{porte-à-faux}} > 2\\mu $$

**Règle pratique : $L_{guidage} \\ge 1,5 \\times$ le porte-à-faux.** Un coulisseau court avec un
grand bras de levier se bloquera systématiquement, quelle que soit la force appliquée.
C'est le principe du **serre-joint** — qu'on utilise volontairement dans ce cas.

### 2. Assemblages démontables : la visserie

**Classes de qualité (ISO 898-1)** — désignation à deux nombres, ex. **8.8** :
- Premier nombre × 100 = $R_m$ en MPa → **800 MPa**
- Produit des deux × 10 = $R_e$ en MPa → $8 \\times 8 \\times 10 = \\mathbf{640}$ MPa

| Classe | $R_m$ | $R_e$ | Emploi |
|---|---|---|---|
| 4.6 | 400 | 240 | Charpente légère |
| **8.8** | 800 | 640 | **Mécanique générale — le standard** |
| **10.9** | 1000 | 900 | **Assemblages fortement sollicités** |
| 12.9 | 1200 | 1080 | Haute performance, moteur |

**Le principe fondamental de l'assemblage vissé :**

> **Une vis ne doit JAMAIS travailler en cisaillement.**
> Elle sert à créer une **précontrainte axiale** qui plaque les pièces l'une contre l'autre.
> C'est l'**adhérence** entre les pièces qui transmet l'effort tangentiel.

Si l'effort tangentiel dépasse l'adhérence, on ajoute des **pions de centrage** ou des
**goupilles** — jamais on ne compte sur les vis en cisaillement.

**Précontrainte et couple de serrage :**

$$ C = K \\cdot F_0 \\cdot d $$

avec $K \\approx 0,20$ (acier non lubrifié), $F_0$ la précontrainte visée
(typiquement $0,7 \\times R_e \\times A_s$), $d$ le diamètre nominal.

**Freinage :** rondelle élastique (Grower — peu efficace), rondelle éventail, écrou Nylstop,
frein filet chimique (Loctite), goupille, écrou à créneaux, contre-écrou.

### 3. Assemblages arbre-moyeu

| Solution | Couple transmis | Démontable | Centrage | Remarque |
|---|---|---|---|---|
| **Clavette parallèle** | ++ | ✅ | Non (jeu latéral) | Le plus courant. Affaiblit l'arbre ($K_t \\approx 2$) |
| Cannelures | +++ | ✅ | ✅ | Fort couple, coûteux |
| **Frettage** (H7/s6, u6) | +++ | ❌ | ✅ | Pas d'entaille → **meilleure tenue en fatigue** |
| Moyeu conique / anneaux de serrage | +++ | ✅ | ✅ | Solution moderne, sans entaille |
| Goupille | + | ✅ | ✅ | Faible couple, positionnement |
| Vis de pression | + | ✅ | Non | Marque l'arbre |

**Dimensionnement d'une clavette parallèle** — deux vérifications :
- **Matage** sur les flancs : $p = \\dfrac{2 M_t}{d \\cdot L \\cdot (h/2)} \\le p_{adm}$
- **Cisaillement** : $\\tau = \\dfrac{2 M_t}{d \\cdot L \\cdot b} \\le R_{pg}$

Le **matage est presque toujours dimensionnant**.

### 4. Transmission de puissance

| Solution | Rapport | Rendement | Distance | Remarque |
|---|---|---|---|---|
| **Engrenage droit** | jusqu'à 1:8 | 0,96-0,98 | Courte | Bruyant à haute vitesse |
| **Engrenage hélicoïdal** | jusqu'à 1:8 | 0,96-0,98 | Courte | Silencieux, mais **effort axial** |
| Roue et vis sans fin | jusqu'à 1:100 | **0,5-0,8** | Courte | Compact, souvent **irréversible** |
| **Courroie crantée** | jusqu'à 1:8 | 0,95-0,98 | Moyenne | Pas de glissement, silencieux |
| Courroie trapézoïdale | jusqu'à 1:8 | 0,92-0,96 | Moyenne | Glissement possible = sécurité |
| **Chaîne** | jusqu'à 1:7 | 0,95-0,98 | Moyenne | Fort couple, bruyante, lubrification |

**Relations d'engrenage — à connaître par cœur :**

$$ m = \\frac{d}{Z} \\qquad d = m Z \\qquad \\text{entraxe } a = \\frac{d_1 + d_2}{2} = \\frac{m(Z_1 + Z_2)}{2} $$

**Rapport de transmission :**
$$ i = \\frac{N_{sortie}}{N_{entrée}} = \\frac{Z_{menante}}{Z_{menée}} = \\frac{d_{menante}}{d_{menée}} $$

Pour un train à plusieurs étages, les rapports se **multiplient**.

### 5. Étanchéité

| Type | Solution | Domaine |
|---|---|---|
| **Statique** | Joint plat, joint torique, silicone | Plans de joint, brides |
| **Dynamique en rotation** | Joint à lèvre (type A/AS), garniture mécanique | Sortie d'arbre |
| **Dynamique en translation** | Joint torique, joint à lèvre, racleur | Tige de vérin |
| Sans contact | Chicane, déflecteur, labyrinthe | Vitesses élevées |

**Le joint à lèvre :** lèvre orientée **vers le fluide à retenir**, ressort côté huile.
Exige un état de surface **Ra 0,2 à 0,8**, sans stries hélicoïdales, dureté ≥ 45 HRC si
service continu.
""",
            "formules": """
**VISSERIE**

Section résistante d'une vis :
$$ A_s = \\frac{\\pi}{4}\\left(\\frac{d_2 + d_3}{2}\\right)^2 $$

| Vis | $d$ (mm) | Pas | $A_s$ (mm²) |
|---|---|---|---|
| M5 | 5 | 0,8 | 14,2 |
| M6 | 6 | 1,0 | 20,1 |
| M8 | 8 | 1,25 | 36,6 |
| M10 | 10 | 1,5 | 58,0 |
| M12 | 12 | 1,75 | 84,3 |
| M16 | 16 | 2,0 | 157 |
| M20 | 20 | 2,5 | 245 |

Précontrainte recommandée :
$$ F_0 = 0,7 \\times R_e \\times A_s $$

Couple de serrage :
$$ \\boxed{C = K \\cdot F_0 \\cdot d} \\qquad K \\approx 0,20 \\text{ (sec)}, \\; 0,15 \\text{ (lubrifié)} $$

Effort transmissible par adhérence ($n$ vis, $f$ = coefficient d'adhérence, $j$ = plans de joint) :
$$ \\boxed{F_T = n \\cdot j \\cdot f \\cdot F_0} $$

$f \\approx 0,15$ (acier/acier usiné), $0,10$ (peint), $0,20$ (grenaillé).

---

**CLAVETTE PARALLÈLE**

Dimensions normalisées (NF E 22-177) :

| Ø arbre (mm) | $b \\times h$ |
|---|---|
| 10 à 12 | 4 × 4 |
| 12 à 17 | 5 × 5 |
| 17 à 22 | 6 × 6 |
| 22 à 30 | 8 × 7 |
| 30 à 38 | 10 × 8 |
| 38 à 44 | 12 × 8 |
| 44 à 50 | 14 × 9 |
| 50 à 58 | 16 × 10 |

**Vérification au matage** (dimensionnante dans 90 % des cas) :
$$ \\boxed{p = \\frac{4 M_t}{d \\cdot L \\cdot h} \\le p_{adm}} $$
$p_{adm} \\approx 100$ MPa (acier courant), 150 MPa (acier traité).

**Vérification au cisaillement :**
$$ \\tau = \\frac{2 M_t}{d \\cdot L \\cdot b} \\le R_{pg} $$

---

**ENGRENAGES**

$$ m = \\frac{d}{Z} \\qquad d = mZ \\qquad d_a = m(Z+2) \\qquad d_f = m(Z - 2,5) $$
$$ p = \\pi m \\qquad a = \\frac{m(Z_1+Z_2)}{2} $$

**Rapport de transmission :**
$$ i = \\frac{N_2}{N_1} = \\frac{Z_1}{Z_2} \\qquad \\text{(train simple)} $$

$$ i_{global} = i_1 \\times i_2 \\times \\dots \\times i_n \\qquad \\text{(train à n étages)} $$

**Efforts sur une denture droite :**
$$ F_t = \\frac{2 M_t}{d} \\qquad F_r = F_t \\tan\\alpha \\qquad (\\alpha = 20°) $$

**Denture hélicoïdale** (angle d'hélice $\\beta$) :
$$ F_t = \\frac{2M_t}{d} \\qquad F_a = F_t \\tan\\beta \\qquad F_r = \\frac{F_t \\tan\\alpha}{\\cos\\beta} $$

---

**COURROIES ET CHAÎNES**

$$ i = \\frac{d_1}{d_2} = \\frac{Z_1}{Z_2} \\qquad v = \\frac{\\pi d_1 N_1}{60\\,000} \\;\\mathrm{[m/s]} $$

Longueur approchée d'une courroie (entraxe $a$) :
$$ L \\approx 2a + \\frac{\\pi(d_1+d_2)}{2} + \\frac{(d_2-d_1)^2}{4a} $$

---

**PUISSANCE ET RENDEMENT**

$$ P = M_t \\, \\omega \\qquad P_{sortie} = \\eta \\, P_{entrée} \\qquad \\eta_{global} = \\eta_1 \\times \\eta_2 \\times \\dots $$

**NON-ARC-BOUTEMENT D'UNE GLISSIÈRE**
$$ \\frac{L_{guidage}}{d_{porte-à-faux}} > 2\\mu $$
""",
            "exemple": """
**Cas industriel — Conception complète d'un étage de réduction**

Un motoréducteur doit entraîner un tapis. Cahier des charges : moteur **4 kW à 1 450 tr/min**,
vitesse de sortie souhaitée **≈ 290 tr/min**, arbre de sortie Ø40.

**ÉTAPE 1 — Rapport de réduction**

$$ i = \\frac{N_{sortie}}{N_{entrée}} = \\frac{290}{1\\,450} = \\frac{1}{5} $$

Choix des dentures : $Z_1 = 19$ dents (pignon), $Z_2 = 95$ dents (roue)
$$ i = \\frac{19}{95} = \\frac{1}{5} \\quad ✔️ \\qquad N_2 = 1\\,450 \\times \\frac{19}{95} = \\mathbf{290\\ tr/min} $$

*Pourquoi 19 et non 20 ? Un nombre de dents **premier** avec l'autre roue répartit l'usure :
chaque dent du pignon rencontre toutes les dents de la roue avant de retomber sur la même. Avec
20/100, une dent du pignon ne verrait que 5 dents de la roue — usure localisée.*

**ÉTAPE 2 — Module et géométrie**

Module normalisé retenu : **m = 3 mm**

$$ d_1 = mZ_1 = 3 \\times 19 = 57\\ \\mathrm{mm} \\qquad d_2 = mZ_2 = 3 \\times 95 = 285\\ \\mathrm{mm} $$

$$ a = \\frac{d_1 + d_2}{2} = \\frac{57 + 285}{2} = \\mathbf{171\\ mm} $$

**ÉTAPE 3 — Couples et efforts**

$$ M_{t1} = \\frac{30 P}{\\pi N_1} = \\frac{30 \\times 4\\,000}{\\pi \\times 1\\,450} = 26,3\\ \\mathrm{N\\cdot m} $$

$$ M_{t2} = \\frac{M_{t1}}{i} \\times \\eta = \\frac{26,3}{0,2} \\times 0,97 = \\mathbf{127,6\\ N\\cdot m} $$

Effort tangentiel sur la denture :
$$ F_t = \\frac{2 M_{t1}}{d_1} = \\frac{2 \\times 26\\,300}{57} = \\mathbf{923\\ N} $$

Effort radial : $F_r = F_t \\tan 20° = 923 \\times 0,364 = \\mathbf{336\\ N}$

**ÉTAPE 4 — Liaison roue/arbre de sortie (Ø40) : clavette**

Clavette normalisée pour Ø40 : **12 × 8**. Longueur à déterminer.

$$ p = \\frac{4 M_t}{d \\cdot L \\cdot h} \\le 100\\ \\mathrm{MPa} $$

$$ L \\ge \\frac{4 \\times 127\\,600}{40 \\times 8 \\times 100} = \\frac{510\\,400}{32\\,000} = \\mathbf{15,95\\ mm} $$

**Clavette retenue : 12 × 8 × 40** (longueur normalisée supérieure, alignée sur la largeur du moyeu).

Vérification au cisaillement :
$$ \\tau = \\frac{2 \\times 127\\,600}{40 \\times 40 \\times 12} = \\frac{255\\,200}{19\\,200} = 13,3\\ \\mathrm{MPa} \\;\\ll\\; R_{pg} \\quad ✔️ $$

**Le matage est bien dimensionnant** (facteur 8 d'écart entre les deux critères) — c'est le cas
général.

**ÉTAPE 5 — Fixation du carter : assemblage vissé**

Le carter est fixé au bâti par **4 vis M10 classe 8.8**. Le couple de réaction vaut 127,6 N·m
sur un rayon de fixation de 90 mm.

$$ F_{tangentiel} = \\frac{M_t}{r} = \\frac{127\\,600}{90} = 1\\,418\\ \\mathrm{N} $$

Précontrainte par vis :
$$ F_0 = 0,7 \\times 640 \\times 58,0 = \\mathbf{25\\,984\\ N} $$

Effort transmissible par adhérence (4 vis, 1 plan de joint, $f = 0,15$) :
$$ F_T = n \\cdot j \\cdot f \\cdot F_0 = 4 \\times 1 \\times 0,15 \\times 25\\,984 = \\mathbf{15\\,590\\ N} $$

$$ \\frac{15\\,590}{1\\,418} = \\mathbf{11} \\quad ✔️ \\;\\text{coefficient de sécurité très confortable} $$

**Couple de serrage à prescrire :**
$$ C = K F_0 d = 0,20 \\times 25\\,984 \\times 10 = 51\\,968\\ \\mathrm{N\\cdot mm} = \\mathbf{52\\ N\\cdot m} $$

> **Ce couple doit figurer sur le plan d'ensemble.** Un assemblage vissé non prescrit en couple
> est un assemblage non maîtrisé : trop serré, la vis casse ; trop peu, l'adhérence disparaît et
> les vis se retrouvent en cisaillement — exactement ce qu'on voulait éviter.
""",
            "exercice": """
**Exercice type examen — Conception d'un poste de perçage automatisé**

Un poste de perçage comporte une **broche** montée sur un **coulisseau** guidé en translation
verticale, entraîné par un système **vis-écrou** motorisé.

**Données :**
- Effort de poussée maximal en perçage : **F = 2 400 N**
- Masse du coulisseau + broche : **35 kg**
- Course : **250 mm**, vitesse d'avance : **0,05 m/s**
- Vis à billes Ø25, pas **p = 5 mm**, rendement $\\eta = 0,90$
- Le moteur tourne à **1 500 tr/min** max
- Coefficient de frottement dans les guidages : $\\mu = 0,01$ (rail à billes)

**PARTIE A — Guidage en translation**

1. Le porte-à-faux entre l'axe de la broche et le plan des rails est de **180 mm**.
   Déterminer la longueur minimale de guidage pour éviter l'arc-boutement, puis proposer
   une valeur conforme aux bonnes pratiques.
2. Le concepteur hésite entre des **rails à billes** et une **glissière queue d'aronde**.
   Comparer les deux solutions sur 4 critères et recommander.

**PARTIE B — Entraînement vis-écrou**

3. Calculer l'effort axial total sur la vis (perçage + poids + frottements).
4. Calculer la vitesse de rotation de la vis pour l'avance demandée. Faut-il un réducteur ?
5. Calculer le couple moteur nécessaire.
6. Calculer la puissance du moteur, puis choisir dans la série normalisée
   (0,25 / 0,37 / 0,55 / 0,75 / 1,1 / 1,5 kW).

**PARTIE C — Assemblage de la broche**

7. La broche est fixée au coulisseau par **4 vis M8 classe 8.8** ($A_s = 36,6$ mm²).
   Calculer la précontrainte par vis et le couple de serrage ($K = 0,20$).
8. Vérifier que l'assemblage résiste par adhérence à l'effort de perçage
   ($f = 0,15$, 1 plan de joint).
9. Un technicien propose de remplacer les 4 vis M8 par **2 vis M12 classe 8.8**
   ($A_s = 84,3$ mm²) « puisque la section totale est équivalente ». Analyser cette
   proposition par le calcul et conclure.
""",
            "corrige": """
**PARTIE A — GUIDAGE EN TRANSLATION**

**1. Longueur minimale de guidage (non-arc-boutement)**

Condition théorique :
$$ \\frac{L_{guidage}}{d_{porte-à-faux}} > 2\\mu $$

$$ L > 2 \\times 0,01 \\times 180 = \\mathbf{3,6\\ mm} $$

**Ce résultat est théoriquement correct mais pratiquement inutilisable.**

*Analyse :* avec un rail à billes ($\\mu = 0,01$), la condition d'arc-boutement est satisfaite
avec une longueur dérisoire — c'est justement l'intérêt du roulement. **Mais l'arc-boutement
n'est pas le seul critère.**

**Critère réellement dimensionnant : la RIGIDITÉ et la reprise du moment de basculement.**

L'effort de perçage de 2 400 N appliqué à 180 mm crée un moment :
$$ M = F \\times d = 2\\,400 \\times 180 = 432\\,000\\ \\mathrm{N\\cdot mm} = 432\\ \\mathrm{N\\cdot m} $$

Ce moment est repris par un **couple de forces** sur les patins, distants de $L$ :
$$ F_{patin} = \\frac{M}{L} = \\frac{432\\,000}{L} $$

| $L$ | Effort par patin | Commentaire |
|---|---|---|
| 100 mm | 4 320 N | Élevé, déformation du guidage |
| **200 mm** | **2 160 N** | Raisonnable |
| 300 mm | 1 440 N | Confortable, mais encombrant |

**Règle de bonne pratique à appliquer :**
$$ \\boxed{L_{guidage} \\ge 1,5 \\times d_{porte-à-faux} = 1,5 \\times 180 = \\mathbf{270\\ mm}} $$

**Valeur retenue : L = 280 mm** (entraxe des patins), soit $L/d = 1,56$.

**Justification complémentaire :** la course étant de 250 mm, un entraxe de 280 mm impose des
rails d'environ 530 mm — dimension parfaitement standard. Le surcoût est marginal au regard
du gain en précision de perçage (un basculement de 0,05 mm en bout de broche décale le trou
d'autant).

---

**2. Comparaison rails à billes / queue d'aronde**

| Critère | **Rails à billes** | **Queue d'aronde** |
|---|---|---|
| **Frottement** | $\\mu \\approx 0,005$ à $0,01$ → moteur plus petit, pas d'échauffement | $\\mu \\approx 0,10$ à $0,20$ → il faut vaincre ~700 N de frottement en plus |
| **Précision / rigidité** | Précision de positionnement élevée, **précontrainte réglable**, faible jeu | Excellente rigidité en compression, mais **jeu à rattraper par lardon** (réglage manuel, dérive dans le temps) |
| **Amortissement des vibrations** | ❌ **Faible** — le contact ponctuel bille/piste transmet les vibrations | ✅ **Excellent** — grande surface de contact, film d'huile amortissant |
| **Vitesse** | ✅ Jusqu'à plusieurs m/s | ❌ Limitée (échauffement, usure) |
| **Résistance aux copeaux** | ❌ Sensible : un copeau qui entre détruit les pistes → **soufflets obligatoires** | ✅ Robuste, tolère un environnement sale |
| **Coût** | Élevé (rails rectifiés + patins) | Modéré (usinage + grattage) |
| **Maintenance** | Graissage périodique, patins remplaçables | Réglage du lardon, rodage |

**RECOMMANDATION : rails à billes avec soufflets de protection.**

**Justification pour ce cas précis :**

1. **L'avance est motorisée et asservie** (vis à billes + moteur). Un frottement de 700 N dans
   une queue d'aronde exigerait un moteur **3 fois plus puissant** et rendrait l'asservissement
   imprécis (phénomène de *stick-slip* : le coulisseau avance par à-coups).
2. La **précision de position** est critique en perçage automatisé.
3. **Le point faible (copeaux) est maîtrisable** : un soufflet ou un capot de protection résout
   le problème, alors que le frottement d'une queue d'aronde est irréductible.

*Si le poste était une machine d'usinage lourde avec fortes vibrations (fraisage, rabotage), la
queue d'aronde reprendrait l'avantage grâce à son amortissement. Le perçage génère peu de
vibrations : ce critère ne tranche pas ici.*

---

**PARTIE B — ENTRAÎNEMENT VIS-ÉCROU**

**3. Effort axial total sur la vis**

| Contribution | Calcul | Valeur |
|---|---|---|
| Effort de perçage | donné | 2 400 N |
| Poids du coulisseau (descente : aide / montée : résiste) | $35 \\times 9,81$ | 343 N |
| Frottement dans les guidages | $\\mu \\times F_{normal}$ — la charge normale sur les patins provient du moment de basculement, majorée : $0,01 \\times (343 + 2\\,160 \\times 2)$ | ≈ 47 N |

**Cas le plus défavorable — la remontée en charge n'existe pas (perçage à la descente), mais
le cas dimensionnant est la DESCENTE en perçage où l'effort résiste :**

$$ F_{axial} = F_{perçage} - P_{poids} + F_{frottement} = 2\\,400 - 343 + 47 = \\mathbf{2\\,104\\ N} $$

**Par prudence, on retient le cas où le poids ne peut pas être compté comme aidant** (position
horizontale possible, ou remontée sous charge résiduelle) :

$$ \\boxed{F_{axial} = 2\\,400 + 343 + 47 \\approx \\mathbf{2\\,790\\ N}} $$

*Justification du choix : dimensionner sur le cas favorable serait une faute. On retient
l'hypothèse enveloppe.*

---

**4. Vitesse de rotation de la vis**

La vis à billes avance de **1 pas (5 mm) par tour** :

$$ N_{vis} = \\frac{v_{avance}}{p} = \\frac{0,05\\ \\mathrm{m/s} \\times 1\\,000 \\times 60}{5} = \\frac{3\\,000}{5} $$

$$ \\boxed{N_{vis} = 600\\ \\mathrm{tr/min}} $$

**Faut-il un réducteur ?**

Le moteur tourne à **1 500 tr/min** max, la vis doit tourner à **600 tr/min**.

$$ i = \\frac{600}{1\\,500} = \\frac{2}{5} = 0,4 $$

$$ \\boxed{\\textbf{OUI, un réducteur de rapport 1:2,5 est nécessaire}} $$

**Solutions possibles :**
- **Courroie crantée** poulies 20/50 dents ($i = 0,4$) — solution la plus simple et la plus
  économique, absorbe les vibrations, permet le déport du moteur
- Réducteur planétaire i = 1:3 avec vitesse moteur ajustée à 1 800 tr/min (variateur)
- **Entraînement direct** avec un servomoteur piloté à 600 tr/min (le plus élégant si le budget
  le permet — supprime tout jeu de transmission)

*Recommandation : courroie crantée, car elle isole aussi le moteur des efforts axiaux parasites.*

---

**5. Couple moteur nécessaire**

Couple sur la vis :
$$ M_{t,vis} = \\frac{F_{axial} \\times p}{2\\pi \\times \\eta} = \\frac{2\\,790 \\times 5}{2\\pi \\times 0,90} $$

$$ M_{t,vis} = \\frac{13\\,950}{5,655} = \\mathbf{2\\,467\\ N\\cdot mm} = 2,47\\ \\mathrm{N\\cdot m} $$

*C'est là toute la magie de la vis à billes : un effort de 2 790 N est vaincu par un couple de
2,5 N·m seulement, grâce au faible pas (5 mm) qui agit comme une démultiplication.*

Couple moteur (en tenant compte du réducteur $i = 0,4$ et de son rendement $\\eta_r = 0,95$) :

$$ M_{moteur} = \\frac{M_{t,vis} \\times i}{\\eta_r} = \\frac{2,47 \\times 0,4}{0,95} = \\mathbf{1,04\\ N\\cdot m} $$

---

**6. Puissance du moteur**

$$ \\omega_{moteur} = \\frac{2\\pi \\times 1\\,500}{60} = 157,1\\ \\mathrm{rad/s} $$

$$ P = M_{moteur} \\times \\omega = 1,04 \\times 157,1 = \\mathbf{163\\ W} $$

**Vérification par le chemin direct (contrôle de cohérence) :**
$$ P_{utile} = F \\times v = 2\\,790 \\times 0,05 = 139,5\\ \\mathrm{W} $$
$$ P_{absorbée} = \\frac{139,5}{0,90 \\times 0,95} = 163\\ \\mathrm{W} \\quad ✔️ \\text{ cohérent} $$

**Choix dans la série normalisée :**

| Puissance | Marge | Verdict |
|---|---|---|
| 0,25 kW | 250/163 = **1,53** | Un peu juste |
| **0,37 kW** | 370/163 = **2,27** | ✅ **RETENU** |
| 0,55 kW | ×3,4 | Surdimensionné |

$$ \\boxed{\\textbf{Moteur 0,37 kW}} $$

**Justification de la marge de 2,3 :** il faut couvrir les **pointes au démarrage**
(accélération de la masse de 35 kg), les **surcharges de perçage** (perçage d'un matériau plus
dur, foret émoussé), et le **vieillissement** des composants (rendement qui se dégrade). Un
moteur à 1,5 de marge décrocherait à la première contrainte.

---

**PARTIE C — ASSEMBLAGE DE LA BROCHE**

**7. Précontrainte et couple de serrage (M8 classe 8.8)**

Classe **8.8** → $R_m = 800$ MPa, $R_e = 8 \\times 8 \\times 10 = 640$ MPa

$$ F_0 = 0,7 \\times R_e \\times A_s = 0,7 \\times 640 \\times 36,6 $$

$$ \\boxed{F_0 = 16\\,397\\ \\mathrm{N} \\approx 16,4\\ \\mathrm{kN\\ par\\ vis}} $$

Couple de serrage :
$$ C = K \\cdot F_0 \\cdot d = 0,20 \\times 16\\,397 \\times 8 = 26\\,235\\ \\mathrm{N\\cdot mm} $$

$$ \\boxed{C \\approx 26\\ \\mathrm{N\\cdot m}} $$

*Cette valeur doit figurer sur le plan d'ensemble et dans la notice de montage.*

---

**8. Vérification de la tenue par adhérence**

Effort transmissible par adhérence :
$$ F_T = n \\cdot j \\cdot f \\cdot F_0 = 4 \\times 1 \\times 0,15 \\times 16\\,397 $$

$$ \\boxed{F_T = 9\\,838\\ \\mathrm{N}} $$

Comparaison à l'effort de perçage (qui sollicite l'assemblage en cisaillement) :

$$ s = \\frac{F_T}{F} = \\frac{9\\,838}{2\\,400} = \\mathbf{4,1} \\quad ✔️ $$

**L'assemblage résiste par adhérence avec un coefficient de 4,1.** Les vis ne travaillent
**jamais en cisaillement** — c'est exactement le principe recherché.

⚠️ **Remarque essentielle à formuler :** il faut aussi vérifier le **moment de basculement**.
L'effort de 2 400 N appliqué à 180 mm crée $M = 432$ N·m que l'assemblage doit reprendre par
**décollement**. Avec 4 vis M8 sur un carré de 100 mm de côté, l'effort d'arrachement par vis
vaut environ $432\\,000 / (2 \\times 100) = 2\\,160$ N, très inférieur à la précontrainte de
16 400 N → **pas de décollement** ✔️

---

**9. Analyse de la proposition « 2 vis M12 au lieu de 4 vis M8 »**

**a) Vérification de l'affirmation sur les sections**

$$ 4 \\times A_{s,M8} = 4 \\times 36,6 = \\mathbf{146,4\\ mm^2} $$
$$ 2 \\times A_{s,M12} = 2 \\times 84,3 = \\mathbf{168,6\\ mm^2} $$

L'affirmation est **approximativement vraie** (168,6 > 146,4, soit +15 %).

**b) Calcul de l'effort transmissible par adhérence**

Précontrainte par vis M12 :
$$ F_{0,M12} = 0,7 \\times 640 \\times 84,3 = 37\\,766\\ \\mathrm{N} $$

$$ F_T = n \\cdot j \\cdot f \\cdot F_0 = 2 \\times 1 \\times 0,15 \\times 37\\,766 = \\mathbf{11\\,330\\ N} $$

$$ s = \\frac{11\\,330}{2\\,400} = \\mathbf{4,7} $$

**En adhérence pure, la proposition est même LÉGÈREMENT MEILLEURE** (4,7 contre 4,1).

**c) MAIS — l'analyse du moment de basculement change tout**

C'est ici que la proposition s'effondre.

| | **4 vis M8** | **2 vis M12** |
|---|---|---|
| Disposition | Carré 100 × 100 mm | Ligne, entraxe 100 mm |
| Reprise du moment dans l'axe X | ✅ 2 vis de chaque côté | ✅ 1 vis de chaque côté |
| **Reprise du moment dans l'axe Y** | ✅ 2 vis de chaque côté | ❌ **AUCUNE** — les deux vis sont alignées |
| Effort d'arrachement (axe défavorable) | 2 160 N/vis | **basculement libre autour de l'axe des 2 vis** |

**Le problème fondamental :** deux vis alignées définissent un **axe de rotation**. L'assemblage
peut **pivoter autour de cette ligne** — seule l'adhérence des surfaces s'y oppose, et cette
adhérence n'est pas fiable sous vibrations.

Or le porte-à-faux de la broche est de **180 mm** : le moment de basculement de 432 N·m
s'applique dans **toutes les directions** selon l'orientation du perçage et les efforts
latéraux de coupe.

**d) Autres inconvénients**

| Inconvénient | Explication |
|---|---|
| **Perte de redondance** | Si une vis M8 sur 4 se desserre, il reste 75 % de la capacité. Si une vis M12 sur 2 se desserre, il ne reste que **50 %** — et l'assemblage devient un pivot |
| **Concentration de contrainte** | Deux M12 concentrent 37,8 kN chacune sur une petite zone → risque de **matage** du coulisseau si celui-ci est en aluminium |
| **Répartition de la pression de contact** | 4 points répartissent mieux la pression sur le plan de joint → contact plus uniforme, meilleure rigidité |
| **Couple de serrage** | $C = 0,20 \\times 37\\,766 \\times 12 = 91$ N·m — nécessite une clé dynamométrique plus grosse, moins d'accessibilité |

**e) CONCLUSION**

$$ \\boxed{\\textbf{PROPOSITION À REJETER}} $$

**Argumentaire à formuler en copie :**

> *« La proposition est valide sur le seul critère de la section résistante et de l'adhérence
> (coefficient 4,7 contre 4,1). Elle est cependant **à rejeter** car deux vis alignées ne
> reprennent le moment de basculement que dans **une seule direction**. Or la broche présente un
> porte-à-faux de 180 mm générant un moment de 432 N·m dont l'orientation varie avec les efforts
> de coupe. Un assemblage à 2 points constitue un axe de pivotement potentiel. S'y ajoutent la
> perte de redondance et le risque de matage du support. **On conserve les 4 vis M8**, disposées
> en carré pour reprendre le basculement dans toutes les directions. »*

> **PRINCIPE GÉNÉRAL À RETENIR — c'est le message de l'exercice :**
> **Le nombre et la DISPOSITION des vis comptent autant que leur section.**
> Un assemblage se dimensionne sur trois critères, jamais un seul :
> 1. la **résistance** (section, précontrainte)
> 2. la **transmission d'effort** (adhérence)
> 3. la **reprise des moments** (répartition géométrique)
>
> La règle d'atelier : **jamais moins de 3 points de fixation** pour une pièce soumise à un
> moment, et de préférence **4 en carré**.
""",
        },
    ],
}
