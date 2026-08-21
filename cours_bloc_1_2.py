# -*- coding: utf-8 -*-
"""Blocs 1 et 2 du référentiel BTS CPI."""

BLOC_1 = {
    "id": "bloc1",
    "titre": "Bloc 1 — Analyse fonctionnelle et lecture de plan",
    "resume": "Comprendre pourquoi un produit existe, puis savoir lire le langage normalisé qui le décrit.",
    "fiches": [
        {
            "id": "1.1",
            "titre": "Analyse du besoin et cahier des charges fonctionnel",
            "duree": "6 h",
            "cours": """
### 1. De quoi part un concepteur ?

Un produit industriel n'existe jamais « parce qu'on avait envie de le dessiner ». Il existe parce
qu'un **utilisateur a un besoin** et qu'un **client est prêt à payer** pour qu'on le satisfasse.
Toute la démarche du BTS CPI part de là : on ne commence pas par SolidWorks, on commence par
**écrire ce que le produit doit faire**, sans dire comment il le fera.

C'est la distinction la plus importante de l'année :

| On exprime… | Exemple | Nom |
|---|---|---|
| **Ce que le produit doit faire** | « Maintenir la pièce pendant l'usinage » | Fonction (le *quoi*) |
| **Comment il le fait** | « Avec un vérin pneumatique Ø32 » | Solution technique (le *comment*) |

Si vous écrivez la solution dans le cahier des charges, vous vous interdisez d'en trouver une
meilleure. Un cahier des charges bien écrit est **neutre technologiquement**.

### 2. La bête à cornes (outil de cadrage du besoin)

Trois questions, et une seule fonction en sortie :

- **À qui le produit rend-il service ?** → l'utilisateur
- **Sur quoi agit-il ?** → la matière d'œuvre
- **Dans quel but ?** → la fonction globale

> *Exemple — étau de bridage d'établi* : rend service à **l'opérateur**, agit sur **la pièce à usiner**,
> dans le but de **l'immobiliser pendant l'opération**.

Test de validation en trois questions (à savoir par cœur pour l'examen) :
1. Pourquoi ce besoin existe-t-il ? (sa cause)
2. Qu'est-ce qui pourrait le faire disparaître ? (sa fin de vie)
3. Ce risque est-il probable ? (sa robustesse)

### 3. Le diagramme pieuvre et les fonctions

On place le produit au centre, les **éléments du milieu extérieur** (EME) autour, puis on relie :

- **Fonction principale (FP)** : relie **deux** EME *à travers* le produit. C'est la raison d'être.
- **Fonction contrainte (FC)** : relie le produit à **un seul** EME. C'est une adaptation imposée.

> Étau : **FP1** = « permettre à l'opérateur de serrer la pièce ». **FC1** = « résister aux copeaux et
> au liquide de coupe », **FC2** = « se fixer sur la table de la machine », **FC3** = « respecter un
> budget de 80 € ».

### 4. Caractériser une fonction : critère, niveau, flexibilité

Une fonction non chiffrée est inutilisable. Chaque fonction reçoit :

- un **critère d'appréciation** (la grandeur observée : effort, masse, durée…)
- un **niveau** (la valeur à atteindre : 5 000 N, 2,5 kg, 10 s…)
- une **flexibilité** (la tolérance admise : ± 5 %, mini, maxi)
- une **classe de flexibilité** F0 (impératif) → F3 (souhait)

C'est ce tableau qui deviendra plus tard votre **critère de validation** : à la fin du projet, on
reprend le cahier des charges ligne par ligne et on coche.

### 5. Le FAST : passer de la fonction à la solution

Le diagramme FAST se lit de gauche à droite avec trois questions :
**Pourquoi ?** (on remonte vers le besoin) — **Comment ?** (on descend vers la solution) —
**Quand ?** (fonctions simultanées, branches verticales).

Fonction de service → fonctions techniques → **solutions constructives**. C'est seulement à
l'extrémité droite du FAST que le nom d'un composant réel apparaît.
""",
            "formules": """
**Il n'y a pas de formule physique ici, mais une syntaxe à respecter scrupuleusement.**

Rédaction normalisée d'une fonction : **verbe à l'infinitif + complément**, sans nom de composant.

- ✅ « Transmettre un couple de 12 N·m entre l'arbre moteur et le réducteur »
- ❌ « Utiliser une clavette parallèle 8×7 » *(c'est une solution, pas une fonction)*

**Taux de satisfaction d'une fonction** (utilisé en revue de projet) :

$$ T = \\frac{\\text{niveau atteint}}{\\text{niveau demandé}} \\times 100 \\;(\\%) $$

**Coût de l'estimation fonctionnelle** — analyse de la valeur :

$$ \\text{Valeur} = \\frac{\\text{Satisfaction des fonctions}}{\\text{Coût}} $$

On améliore la valeur en augmentant le service rendu **ou** en baissant le coût. Une fonction qui
coûte 30 % du prix de revient pour 5 % de la satisfaction est le premier candidat à la refonte.
""",
            "exemple": """
**Cas industriel — Support de capteur pour ligne d'embouteillage (client : agro-alimentaire)**

Le client demande d'abord : « Je veux une équerre en inox avec deux trous taraudés M6. »
Le concepteur reformule en fonctions :

| Fonction | Critère | Niveau | Flexibilité |
|---|---|---|---|
| FP1 — Positionner le capteur face aux bouteilles | Distance capteur/bouteille | 45 mm | ± 2 mm |
| FP1 — (suite) | Répétabilité après démontage | ≤ 0,2 mm | F0 |
| FC1 — Résister au lavage haute pression | Indice de protection | IP69K | F0 |
| FC2 — Résister aux produits chlorés | Matériau | Inox X2CrNiMo17-12-2 | F1 |
| FC3 — Se monter sur profilé existant | Profilé alu 40×40, rainure 8 | — | F0 |
| FC4 — Être réglable en hauteur | Course | 0 à 120 mm | ± 10 mm |
| FC5 — Coût unitaire | Prix pour 50 pièces | ≤ 35 € | F2 |

**Ce que la reformulation a changé :** en ne figeant pas « équerre à deux trous », le concepteur a
pu proposer un **collier de serrage sur tige lisse Ø12**, qui satisfait FC4 (réglage continu) que
l'équerre percée ne satisfaisait pas. Le client n'avait pas vu que son besoin réel incluait le réglage.

**Leçon :** le client exprime souvent une solution. Le travail du technicien CPI est de remonter au besoin.
""",
            "exercice": """
**Exercice type examen — Distributeur automatique de croquettes pour animal domestique**

Un particulier souhaite nourrir son chat pendant une absence de 3 jours. Le produit doit délivrer
une ration à heures fixes, être posé au sol dans une cuisine, et fonctionner sans être branché sur
le secteur (risque que l'animal débranche le câble).

**Questions :**
1. Tracer la bête à cornes et énoncer la fonction globale.
2. Identifier au minimum 5 éléments du milieu extérieur et tracer le diagramme pieuvre.
3. Énoncer FP1 et quatre fonctions contraintes en respectant la syntaxe normalisée.
4. Caractériser FP1 et deux FC avec critère, niveau et flexibilité.
5. Sur la fonction « alimenter le système en énergie », proposer deux solutions techniques et
   justifier le choix en une phrase.
""",
            "corrige": """
**1. Bête à cornes**

- À qui rend-il service ? → **au propriétaire de l'animal** (et non au chat : c'est le propriétaire
  qui achète et qui a le problème à résoudre).
- Sur quoi agit-il ? → **les croquettes** (la matière d'œuvre est ce qui est transformé/déplacé).
- Dans quel but ? → **distribuer une ration déterminée à heure programmée en l'absence du propriétaire**.

*Erreur classique :* écrire « agit sur le chat ». Le produit n'agit pas sur l'animal, il agit sur la nourriture.

**2. Éléments du milieu extérieur**

Propriétaire — Croquettes — Chat — Sol de la cuisine — Énergie — Ambiance (humidité, poussière) —
Normes de sécurité alimentaire.

Le produit est au centre, une liaison par EME.

**3. Fonctions (syntaxe verbe à l'infinitif + complément)**

- **FP1** : Permettre au propriétaire de délivrer les croquettes au chat à heure programmée.
  *(relie deux EME : propriétaire et chat → c'est bien une fonction principale)*
- **FC1** : Stocker les croquettes à l'abri de l'humidité.
- **FC2** : Reposer de façon stable sur le sol de la cuisine.
- **FC3** : Fonctionner en autonomie énergétique pendant 72 h minimum.
- **FC4** : Résister aux tentatives d'ouverture par l'animal.
- **FC5** : Utiliser des matériaux de contact alimentaire.

**4. Caractérisation**

| Fonction | Critère | Niveau | Flexibilité | Classe |
|---|---|---|---|---|
| FP1 | Masse d'une ration | 60 g | ± 5 g | F1 |
| FP1 | Précision horaire sur 72 h | ≤ 5 min de dérive | maxi | F1 |
| FP1 | Nombre de rations programmables/jour | 4 | mini | F2 |
| FC3 | Autonomie | 72 h | mini, F0 | F0 |
| FC4 | Effort d'ouverture du couvercle | ≥ 40 N | mini | F0 |

*Justification de FC4 à 40 N :* un chat exerce en poussée de patte environ 10 à 20 N ; un coefficient
2 sur cette valeur garantit que le couvercle reste fermé.

**5. Solutions pour « alimenter en énergie »**

| Solution | Avantage | Inconvénient |
|---|---|---|
| 4 piles LR6 (6 V) | Aucun câble, coût faible, changement facile | Autonomie à vérifier, déchet |
| Batterie Li-ion rechargeable + USB | Rechargeable, plus compacte | Nécessite de penser à recharger avant l'absence |

**Choix retenu : piles LR6.** L'usage est **occasionnel** (départs en week-end) : une batterie
Li-ion se décharge lentement au repos et risque d'être vide au moment précis où on en a besoin,
alors que des piles neuves offrent une autonomie garantie et satisfont FC3 sans dépendre d'un
geste de l'utilisateur. C'est FC3 (classe F0) qui tranche, pas le coût.
""",
        },
        {
            "id": "1.2",
            "titre": "Lecture de plan : projections, coupes et sections",
            "duree": "10 h",
            "cours": """
### 1. Le principe de la projection orthogonale

Un dessin technique représente un volume 3D sur une feuille 2D. On projette la pièce sur les faces
d'un cube qui l'entoure, puis on **déplie** ce cube. En Europe on utilise la **méthode du premier
dièdre** (symbole ISO : un cône tronqué vu de face et de gauche).

Règle mnémotechnique du premier dièdre : **la vue se place du côté opposé au regard.**
Si je regarde la pièce **par la gauche**, je dessine cette vue **à droite** de la vue de face.

Disposition normalisée :

```
              vue de dessous
vue de droite   VUE DE FACE   vue de gauche
              vue de dessus                    (+ vue arrière à l'extrême droite)
```

**La vue de face** est choisie par le dessinateur : c'est celle qui montre le plus d'informations,
et généralement la pièce dans sa **position d'utilisation** ou **d'usinage** (un arbre se dessine
couché, axe horizontal, comme sur le tour).

### 2. Les traits normalisés (ISO 128)

| Type de trait | Emploi |
|---|---|
| Continu fort | Arêtes et contours **vus** |
| Interrompu fin (tirets) | Arêtes et contours **cachés** |
| Mixte fin (axe) | Axes de révolution, plans de symétrie |
| Mixte fin à éléments forts | Trace d'un **plan de coupe** |
| Continu fin | Lignes d'attache, de cote, hachures |
| Continu fin ondulé | Limite de vue ou de coupe partielle |

Règle de priorité quand deux traits se superposent : **vu > caché > axe**.

### 3. Les coupes

Une pièce creuse dessinée en vues extérieures devient illisible (forêt de tirets). On la **coupe**
par un plan imaginaire, on retire la partie avant, et on dessine ce qu'on voit.

Procédure en 4 temps :
1. Choisir le plan de coupe (il passe par les formes intéressantes : alésages, rainures).
2. Indiquer sa trace sur une autre vue par un trait mixte à éléments forts, avec deux flèches
   donnant le **sens d'observation**, et deux lettres majuscules (A-A).
3. Supprimer la matière située entre l'observateur et le plan.
4. **Hachurer les surfaces réellement coupées** (à 45°, régulières). La matière **derrière** le plan
   n'est pas hachurée mais reste dessinée en trait fort.

**Règle d'or à ne jamais oublier :** on ne coupe **jamais** dans le sens de la longueur une **vis,
un écrou, une rondelle, une goupille, une clavette, une bille ou un rayon de roue**. Ces éléments
sont dessinés **non coupés** — ils n'ont pas de forme intérieure à révéler, et les hachurer nuirait
à la lisibilité.

Variantes : **demi-coupe** (pièce symétrique, moitié en vue / moitié en coupe), **coupe brisée à
plans parallèles**, **coupe brisée à plans sécants** (le second plan est rabattu), **coupe locale**
(délimitée par un trait fin ondulé).

### 4. Les sections

La section ne dessine **que** la surface coupée, sans ce qui se trouve derrière. C'est plus léger
qu'une coupe et idéal pour montrer la forme d'un profil, d'une rainure de clavette ou d'un méplat
sur un arbre.

- **Section sortie** : dessinée à côté de la vue, contour en trait fort. Préférée car plus lisible.
- **Section rabattue** : dessinée directement sur la vue, contour en **trait fin**, en superposition.

### 5. Vues particulières

**Vue interrompue** (pièce très longue et de section constante), **vue partielle** (limitée par un
trait ondulé), **vue de détail agrandie** (repérée par un cercle et une lettre, avec l'échelle
indiquée : *Détail A — Échelle 5:1*), **demi-vue** pour les pièces symétriques.
""",
            "formules": """
**Échelle du dessin**

$$ \\text{Échelle} = \\frac{\\text{dimension sur le dessin}}{\\text{dimension réelle de l'objet}} $$

- Échelle **1:1** → vraie grandeur
- Échelle **1:2**, 1:5, 1:10 → **réduction** (l'objet est plus grand que le dessin)
- Échelle **2:1**, 5:1, 10:1 → **agrandissement**

⚠️ **Les cotes portées sur un dessin sont TOUJOURS les cotes réelles de la pièce**, jamais les cotes
mesurées à la règle sur le papier. L'échelle ne modifie pas les valeurs inscrites.

**Formats de papier normalisés (ISO 216)** — chaque format est le double du suivant :

| Format | Dimensions (mm) |
|---|---|
| A0 | 1189 × 841 |
| A1 | 841 × 594 |
| A2 | 594 × 420 |
| A3 | 420 × 297 |
| A4 | 297 × 210 |

**Correspondance entre vues (règle de construction)** — les vues sont **alignées** :
- vue de face et vues de gauche/droite : **même hauteur** (lignes de rappel horizontales)
- vue de face et vues de dessus/dessous : **même largeur** (lignes de rappel verticales)
- report entre vue de dessus et vue de gauche : par une **droite à 45°** ou un arc de cercle.
""",
            "exemple": """
**Cas industriel — Corps de palier en fonte EN-GJL-250**

La pièce est un bloc de 120 × 80 × 60 mm avec un alésage traversant Ø50 H7 pour le roulement, deux
trous de fixation Ø11 débouchants, un lamage Ø18 profondeur 8, et une rainure de graissage.

**Représentation retenue par le bureau d'études : 2 vues seulement.**

1. **Vue de face en coupe A-A** (plan vertical passant par l'axe de l'alésage) : elle montre d'un
   seul coup l'alésage Ø50, sa longueur, le lamage et la rainure de graissage. Sans la coupe, il
   aurait fallu 6 traits interrompus superposés → illisible.
2. **Vue de dessus** : elle montre l'entraxe des deux trous de fixation et la forme extérieure de la semelle.

**Décisions de dessinateur à comprendre :**
- La **vue de gauche n'est pas dessinée** : elle n'apporterait aucune information nouvelle (la pièce
  est symétrique). *Une vue qui n'apporte rien ne doit pas être tracée* — c'est un critère de notation.
- Les **nervures de renfort** sous la semelle, bien que traversées par le plan de coupe, sont
  représentées **non hachurées** lorsque la coupe est longitudinale : c'est la même logique que pour
  les vis, éviter de faire croire à un bloc massif.
- Un **détail B à l'échelle 5:1** est ajouté pour la gorge de dégagement de rectification en fond
  d'alésage (largeur 2 mm, rayon 0,4) : à l'échelle 1:1 elle serait invisible.
""",
            "exercice": """
**Exercice type examen — Chape de vérin**

On donne une pièce prismatique de base 70 × 40 × 25 mm. Elle comporte :
- un alésage traversant **Ø20 H8** dont l'axe est horizontal, à 30 mm du fond ;
- une **rainure en U** de largeur 22 mm et profondeur 35 mm, ouverte vers le haut, centrée ;
- deux trous **Ø9** débouchants dans la semelle, entraxe 50 mm ;
- un **chanfrein 2 × 45°** sur toutes les arêtes extérieures supérieures.

**Questions :**
1. Justifier le choix de la vue de face.
2. Combien de vues sont strictement nécessaires ? Lesquelles ? Justifier.
3. Sur la vue de face, faut-il une coupe ? Si oui, où placer le plan A-A et pourquoi ?
4. Dans cette coupe, les deux trous Ø9 de la semelle apparaissent-ils hachurés ? Justifier.
5. Une vis CHc M8 est montée dans l'un des trous, l'ensemble étant coupé longitudinalement.
   Comment représente-t-on la vis ? Énoncer la règle.
6. La pièce est dessinée sur un format A3 à l'échelle 2:1. Quelle valeur inscrit-on sur la cote
   de l'alésage, et quelle longueur mesure-t-on à la règle sur le papier ?
""",
            "corrige": """
**1. Choix de la vue de face**

On choisit la vue qui montre le **contour caractéristique en U** et qui correspond à la **position
d'utilisation** de la chape (rainure vers le haut, axe d'articulation horizontal). C'est la vue la
plus « parlante » : un lecteur reconnaît immédiatement une chape.

**2. Nombre de vues nécessaires : 2 vues.**

- **Vue de face (en coupe)** : donne la hauteur, la rainure en U, l'alésage Ø20 et sa position.
- **Vue de dessus** : donne la longueur 70, la largeur 40, l'entraxe 50 des trous Ø9 et la largeur
  22 de la rainure.

La **vue de gauche est inutile** : elle ne montrerait que la largeur 40 et la hauteur, déjà données
par les deux autres vues. *Règle : le nombre minimal de vues est celui qui permet de définir
complètement la pièce sans redondance.*

**3. Plan de coupe**

Oui, une coupe est nécessaire : sans elle l'alésage Ø20 et les trous Ø9 apparaîtraient en traits
interrompus, superposés aux arêtes de la rainure.

Le plan **A-A est vertical, longitudinal, passant par l'axe des deux trous Ø9 et par le plan de
symétrie de la rainure**. Sa trace est portée sur la **vue de dessus**, en trait mixte à éléments
forts, avec deux flèches indiquant le sens d'observation et deux lettres A.

⚠️ Attention : ce plan **ne passe pas** par l'axe de l'alésage Ø20 (qui est horizontal et
perpendiculaire). L'alésage Ø20 sera donc coupé **transversalement** et apparaîtra comme deux
surfaces hachurées de part et d'autre du U.

**4. Les trous Ø9 dans la coupe**

**Non, ils ne sont pas hachurés — ce sont des vides.** On hachure la **matière** rencontrée par le
plan de coupe, pas les trous. Concrètement : la semelle est hachurée, et le passage du trou Ø9
crée une **interruption des hachures** délimitée par deux traits forts verticaux distants de 9 mm.

*C'est l'erreur n°1 des débutants : hachurer le trou parce qu'il est « dedans ».*

**5. Représentation de la vis CHc M8**

**La vis est représentée NON COUPÉE**, c'est-à-dire dessinée en vue extérieure, sans hachures,
alors même que le plan de coupe la traverse dans sa longueur.

**Règle normalisée à citer :** *« Les pièces pleines (vis, écrous, rondelles, goupilles, clavettes,
rivets, billes, arbres pleins) ne sont jamais coupées longitudinalement. »* Justification : ces
éléments n'ont pas de forme intérieure à révéler ; les hachurer alourdirait le dessin sans apporter
d'information.

En revanche, si le plan de coupe était **perpendiculaire** à l'axe de la vis, elle serait **coupée
et hachurée** normalement (on verrait un disque). La règle ne concerne que la coupe *longitudinale*.

**6. Échelle 2:1**

- **Cote inscrite sur le dessin : Ø20 H8.** On inscrit **toujours la dimension réelle** de la pièce.
  L'échelle n'affecte jamais la valeur cotée.
- **Longueur mesurée à la règle sur le papier :**

$$ L_{papier} = L_{reel} \\times \\frac{2}{1} = 20 \\times 2 = \\mathbf{40\\ mm} $$

L'échelle **2:1** est un **agrandissement** : le dessin est deux fois plus grand que l'objet, ce qui
se justifie ici car la pièce (70 mm) tiendrait largement sur un A3 et les détails (chanfrein 2×45°)
gagnent en lisibilité.

*Vérification de cohérence : la pièce agrandie occupe 140 × 80 mm en vue de face, plus la vue de
dessus 140 × 50 mm. Le format A3 (420 × 297) est confortable. ✔️*
""",
        },
        {
            "id": "1.3",
            "titre": "Cotation dimensionnelle et états de surface",
            "duree": "8 h",
            "cours": """
### 1. Fonction de la cotation

Le dessin donne la **forme**, la cotation donne les **dimensions**. Une pièce mal cotée est une
pièce qui sera fabriquée hors service, même si le dessin est magnifique. La cotation doit être
**complète** (toutes les dimensions nécessaires), **non redondante** (chaque dimension une seule
fois) et **fonctionnelle** (cotée là où ça compte pour l'usage).

### 2. Éléments d'une cote

- **Ligne de cote** : parallèle à l'élément coté, terminée par deux flèches.
- **Lignes d'attache** : perpendiculaires, dépassant légèrement la ligne de cote, sans la toucher
  au départ (petit espace avec le contour de la pièce).
- **Valeur** : placée au-dessus et au milieu de la ligne de cote, lisible depuis le bas ou la droite.

**Règles à respecter :**
- Ne jamais coter sur des traits interrompus (traits cachés) : coter dans une coupe.
- Les lignes de cote ne se croisent pas ; les plus courtes sont les plus proches de la pièce.
- Une dimension n'apparaît **qu'une seule fois** sur l'ensemble du dessin.

### 3. Symboles normalisés

| Symbole | Signification | Exemple |
|---|---|---|
| **Ø** | Diamètre | Ø20 |
| **R** | Rayon | R5 |
| **SØ** / **SR** | Diamètre / rayon de sphère | SØ12 |
| **□** | Carré | □25 |
| **▽** ou ↧ | Profondeur | ↧15 |
| **⌴** | Lamage | ⌴Ø18↧8 |
| **⌵** | Fraisure (chanfrein conique) | ⌵Ø14×90° |
| **×** | Nombre d'éléments identiques | 4× Ø9 |
| **M** | Filetage métrique ISO | M8, M10×1,25 |
| **( )** | Cote auxiliaire (informative, non contrôlée) | (95) |

### 4. Modes de cotation

- **Cotation en série (à la chaîne)** : cotes bout à bout. ⚠️ Les tolérances **s'additionnent** :
  trois cotes à ±0,1 donnent ±0,3 sur la longueur totale. À éviter sur les fonctions précises.
- **Cotation en parallèle (depuis une origine commune)** : toutes les cotes partent d'une même
  référence. Les erreurs **ne se cumulent pas**. C'est le mode à privilégier.
- **Cotation par coordonnées (tabulée)** : un tableau X/Y/Ø, utilisé pour les tôles percées et la
  programmation CN.

### 5. Les états de surface (ISO 21920, ex-ISO 1302)

Une surface usinée n'est jamais parfaitement lisse : elle porte des irrégularités. On distingue les
**écarts de forme** (ordre 1), l'**ondulation** (ordre 2) et la **rugosité** (ordres 3 et 4).

**Ra — écart moyen arithmétique** : c'est le paramètre le plus utilisé, exprimé en **µm**. C'est la
moyenne des valeurs absolues des écarts par rapport à la ligne moyenne sur la longueur d'évaluation.

Le symbole de base est un « check » ; complété d'un trait horizontal il indique un **enlèvement de
matière obligatoire** ; complété d'un cercle, un **enlèvement de matière interdit** (surface brute).

**Ordres de grandeur à connaître par cœur :**

| Ra (µm) | Procédé typique | Application |
|---|---|---|
| 12,5 – 25 | Sciage, brut de fonderie | Surfaces libres |
| 6,3 | Fraisage / tournage d'ébauche | Faces d'appui non critiques |
| 3,2 | Tournage de finition | Portées courantes |
| 1,6 | Fraisage de finition, alésage | Portées de roulement, plans de joint |
| 0,8 | Rectification | Portées de roulement précises, glissières |
| 0,4 – 0,1 | Rectification fine, rodage | Portées hydrauliques, alésages de vérin |
| 0,05 | Superfinition, polissage | Miroirs, portées de joint dynamique |

**Règle économique fondamentale : diviser Ra par 2 double approximativement le coût de la surface.**
On ne demande donc Ra 0,4 que si la fonction l'exige réellement.
""",
            "formules": """
**Rugosité arithmétique Ra**

$$ R_a = \\frac{1}{l}\\int_0^l |y(x)|\\,dx \\quad \\approx \\quad \\frac{1}{n}\\sum_{i=1}^{n}|y_i| $$

où $y$ est l'écart au profil moyen, en **µm**, sur la longueur d'évaluation $l$.

**Rugosité totale Rz** (hauteur maximale du profil, moyenne sur 5 longueurs de base) :

$$ R_z = \\frac{1}{5}\\sum_{i=1}^{5}(y_{p_i} + y_{v_i}) $$

Relation empirique très utile en atelier : $ R_z \\approx 4 \\; \\text{à} \\; 6 \\times R_a $

**Rugosité théorique en tournage** (permet de choisir l'avance pour atteindre un Ra visé) :

$$ R_a \\approx \\frac{f^2}{32 \\, r_\\varepsilon} \\times 1000 \\quad (\\mu m) $$

avec $f$ l'avance par tour (mm/tr) et $r_\\varepsilon$ le rayon de bec de l'outil (mm).

*Exemple : $f = 0,2$ mm/tr, $r_\\varepsilon = 0,8$ mm → $R_a \\approx \\frac{0,04}{25,6}\\times 1000 = 1,56\\ \\mu m$.*

**Cumul de tolérances en cotation à la chaîne** (à connaître pour l'exercice de la fiche 2.1) :

$$ IT_{total} = \\sum_{i=1}^{n} IT_i $$
""",
            "exemple": """
**Cas industriel — Arbre de réducteur, choix des états de surface**

Un arbre en C45 traité comporte 5 zones fonctionnelles distinctes. Le bureau d'études attribue à
chacune un Ra **justifié par sa fonction**, et non « pour faire propre » :

| Zone | Fonction | Ra imposé | Justification |
|---|---|---|---|
| Portée de roulement Ø35 k6 | Reçoit la bague intérieure serrée | **0,8** | Un état grossier écraserait les aspérités au montage → perte de serrage → bague tournante. |
| Portée de joint à lèvre Ø30 | Étanchéité dynamique | **0,4** (sans stries hélicoïdales) | Une rugosité trop forte use la lèvre ; trop faible, elle empêche le film d'huile. Zone rectifiée en plongée, jamais en tournage hélicoïdal. |
| Rainure de clavette | Transmission de couple | **3,2** | Contact statique par flancs : la rugosité n'a aucun rôle. Exiger mieux serait du gaspillage. |
| Épaulement d'appui | Butée axiale de la bague | **1,6** + perpendicularité | Un appui rugueux se tasse et laisse l'arbre prendre du jeu axial. |
| Corps entre portées | Aucune | **6,3** ou brut | Zone non fonctionnelle : on laisse le tournage d'ébauche. |

**Chiffrage de la décision :** passer toutes les surfaces en Ra 0,4 « par sécurité » aurait multiplié
le temps de rectification par 3 et le coût pièce de 28 € à environ 70 €, pour aucun gain fonctionnel.
""",
            "exercice": """
**Exercice type examen — Cotation d'une entretoise et cumul de tolérances**

Une entretoise cylindrique doit positionner axialement une bague entre deux épaulements. Le
dessinateur a coté **à la chaîne** trois longueurs successives : $L_1 = 20 \\pm 0,1$,
$L_2 = 35 \\pm 0,15$, $L_3 = 15 \\pm 0,1$ (en mm).

Le cahier des charges impose que la **longueur totale** soit comprise entre **69,8 et 70,2 mm**.

**Questions :**
1. Calculer la longueur totale nominale.
2. Calculer l'intervalle de tolérance résultant sur la longueur totale.
3. La condition du cahier des charges est-elle respectée ? Conclure.
4. Proposer une correction en modifiant le **mode de cotation**, sans resserrer les tolérances
   d'usinage. Calculer le nouveau résultat.
5. La surface d'appui de l'entretoise doit assurer une portée plane sans matage. Choisir un Ra et
   le procédé associé, en justifiant. Que se passerait-il avec Ra 12,5 ?
""",
            "corrige": """
**1. Longueur totale nominale**

$$ L_{tot} = L_1 + L_2 + L_3 = 20 + 35 + 15 = \\mathbf{70\\ mm} $$

**2. Intervalle de tolérance résultant**

En cotation **à la chaîne**, les tolérances **s'additionnent** (cas le plus défavorable) :

$$ IT_{tot} = IT_1 + IT_2 + IT_3 = 0,2 + 0,3 + 0,2 = \\mathbf{0,7\\ mm} $$

Soit une longueur totale comprise entre :

$$ L_{min} = 19,9 + 34,85 + 14,9 = 69,65\\ mm $$
$$ L_{max} = 20,1 + 35,15 + 15,1 = 70,35\\ mm $$

Résultat : $ L_{tot} = 70 \\pm 0,35 $ mm.

**3. Conformité**

Le cahier des charges demande $70 \\pm 0,2$ mm, soit un IT de **0,4 mm**.
On obtient **0,7 mm**.

$$ 0,7 > 0,4 \\;\\Rightarrow\\; \\textbf{condition NON respectée} $$

Concrètement, une pièce peut sortir à 69,65 mm : la bague aurait alors **0,15 mm de jeu axial**
non prévu, ce qui génère du bruit, des chocs et une usure accélérée. **La cotation est à refaire.**

**4. Correction par changement de mode de cotation**

On passe en **cotation en parallèle** (depuis une origine commune) : on cote directement la
longueur totale **et** deux positions intermédiaires depuis la même face de référence.

Nouvelle cotation proposée :
- Cote **directe** de la longueur totale : $ 70 \\pm 0,2 $ *(cote fonctionnelle, celle du CdC)*
- Position 1 depuis la référence : $ 20 \\pm 0,1 $
- Position 2 depuis la référence : $ 55 \\pm 0,15 $
- La cote $L_3$ devient **auxiliaire**, écrite entre parenthèses : **(15)** — informative, non contrôlée.

Résultat :

$$ IT_{tot} = \\mathbf{0,2\\ mm \\; (\\pm 0,2)} \\;\\le\\; 0,4\\ mm \\;\\Rightarrow\\; \\textbf{condition respectée} $$

**Le point clé à retenir :** on n'a **pas** resserré les tolérances d'usinage (donc **pas augmenté
le coût**). On a simplement **coté la dimension qui compte fonctionnellement**, au lieu de la
laisser résulter d'une chaîne. C'est le principe de la **cotation fonctionnelle** : *on cote la
condition, pas le chemin.*

**5. État de surface de la portée d'appui**

**Choix : Ra 1,6 µm, obtenu par tournage de finition** (ou dressage de finition en une passe fine).

*Justification :* la portée transmet un **effort de serrage axial** sur une petite surface annulaire.
Un Ra 1,6 garantit un contact réparti sur une proportion suffisante de la surface apparente.
Descendre à Ra 0,8 (rectification) n'apporterait rien : le contact est **statique**, il n'y a ni
glissement, ni étanchéité, ni frottement à maîtriser. Ce serait un surcoût injustifié.

*Conséquence de Ra 12,5 :* les aspérités du profil ont une hauteur de l'ordre de
$R_z \\approx 5 \\times R_a = 62\\ \\mu m$. Le contact réel ne se ferait que sur les **sommets des
aspérités**, soit une fraction de la surface prévue. Sous l'effort de serrage, la pression locale
dépasserait la limite élastique du matériau : les sommets **s'écraseraient (matage)**. L'entretoise
se raccourcirait de plusieurs centièmes après quelques cycles, le serrage se relâcherait, et le
jeu axial réapparaîtrait — exactement le défaut que la question 4 cherchait à supprimer.
""",
        },
    ],
}


BLOC_2 = {
    "id": "bloc2",
    "titre": "Bloc 2 — Tolérancement dimensionnel et ajustements ISO",
    "resume": "Passer de la cote parfaite du modèle 3D à la cote réelle, fabricable et mesurable.",
    "fiches": [
        {
            "id": "2.1",
            "titre": "Tolérances dimensionnelles et système ISO 286",
            "duree": "8 h",
            "cours": """
### 1. Pourquoi tolérancer ?

Aucune machine ne peut produire une cote **exacte**. Demander « Ø20,000 » n'a pas de sens physique :
la pièce sortira à 20,003 ou 19,998. Le concepteur doit donc indiquer **entre quelles bornes** la
pièce reste acceptable. C'est la **tolérance**.

La règle économique fondamentale du métier :

> **Plus la tolérance est serrée, plus la pièce coûte cher.**
> Passer de IT11 à IT7 multiplie typiquement le coût d'usinage par 3 à 5.
> On ne resserre donc **jamais** « par sécurité » : on resserre **parce que la fonction l'exige**.

### 2. Vocabulaire normalisé (à maîtriser absolument)

Soit une cote **Ø20 +0,021 / 0** :

| Terme | Symbole (alésage / arbre) | Valeur |
|---|---|---|
| **Cote nominale** | $D$ / $d$ | 20 mm |
| **Écart supérieur** | $ES$ / $es$ | +0,021 mm (+21 µm) |
| **Écart inférieur** | $EI$ / $ei$ | 0 mm |
| **Cote maximale** | $D_{max}$ / $d_{max}$ | 20,021 mm |
| **Cote minimale** | $D_{min}$ / $d_{min}$ | 20,000 mm |
| **Intervalle de tolérance** | $IT$ | 0,021 mm (21 µm) |

**Convention absolue :** les **MAJUSCULES** désignent l'**alésage** (le contenant, la partie femelle,
le trou) ; les **minuscules** désignent l'**arbre** (le contenu, la partie mâle). C'est vrai pour les
écarts (ES/es) comme pour les lettres de position (H/h).

### 3. Le système ISO 286 : une lettre + un chiffre

Une cote tolérancée ISO s'écrit **Ø20 H7** ou **Ø20 g6** :

- **La LETTRE donne la POSITION** de la zone de tolérance par rapport à la ligne zéro
  (la cote nominale). Elle définit l'**écart fondamental**, c'est-à-dire l'écart le plus proche
  de la ligne zéro.
- **Le CHIFFRE donne la LARGEUR** de la zone, c'est-à-dire la valeur de l'IT. C'est le **grade**,
  de IT01 à IT18.

**Position des lettres (à visualiser mentalement) :**

```
                    ZONE AU-DESSUS (matière en plus)
 arbres :  ────────────────── k m n p r s t u v x y z
 LIGNE ZÉRO (cote nominale) ══════ h ══════ H ══════
 arbres :  a b c d e f g ──────────────────
                    ZONE EN-DESSOUS (matière en moins)
```

À retenir :
- **h** : arbre dont l'écart supérieur $es = 0$. C'est l'**arbre normal** : toujours plus petit ou égal au nominal.
- **H** : alésage dont l'écart inférieur $EI = 0$. C'est l'**alésage normal** : toujours plus grand ou égal au nominal.
- **js / JS** : tolérance **symétrique**, $\\pm IT/2$.
- De **a vers h**, l'arbre grossit ; de **k vers z**, il grossit encore et dépasse le nominal.

### 4. Les grades IT

Le grade fixe la précision. La valeur de l'IT dépend **aussi de la dimension** : à grade égal, une
pièce de Ø200 a une tolérance plus large qu'une pièce de Ø10 (il est plus difficile d'usiner
précisément une grande pièce).

| Grades | Précision | Procédé | Emploi |
|---|---|---|---|
| IT01 à IT4 | Très haute | Rodage, superfinition | Calibres, métrologie |
| **IT5 à IT7** | **Haute** | **Rectification, alésage** | **Portées de roulement, guidages** |
| **IT8 à IT11** | **Courante** | **Tournage, fraisage** | **Mécanique générale** |
| IT12 à IT18 | Grossière | Sciage, laminage, fonderie | Cotes libres, pièces brutes |

**Grades à mémoriser pour le BTS : IT6 et IT7 (précis), IT8/IT9 (courant), IT11 (grossier).**

### 5. Lire une table ISO

Exemple : **Ø20 H7**.
1. Dimension 20 mm → tranche **18 à 30 mm**.
2. Grade **IT7** → dans la table, tranche 18-30, colonne IT7 → **21 µm**.
3. Lettre **H** (alésage) → $EI = 0$ par définition.
4. Donc $ES = EI + IT = 0 + 21 = +21\\ \\mu m$.

→ **Ø20 H7 = Ø20 +0,021 / 0**, soit un alésage entre **20,000 et 20,021 mm**.
""",
            "formules": """
**Relations de base — ALÉSAGE (majuscules)**

$$ IT = ES - EI $$
$$ D_{max} = D + ES \\qquad D_{min} = D + EI $$
$$ IT = D_{max} - D_{min} $$

**Relations de base — ARBRE (minuscules)**

$$ IT = es - ei $$
$$ d_{max} = d + es \\qquad d_{min} = d + ei $$

**Cas particulier js / JS (tolérance symétrique)**

$$ es = +\\frac{IT}{2} \\qquad ei = -\\frac{IT}{2} $$

**Cas particuliers des lettres normales**

$$ \\text{Alésage } \\mathbf{H} : EI = 0 \\;\\Rightarrow\\; ES = +IT $$
$$ \\text{Arbre } \\mathbf{h} : es = 0 \\;\\Rightarrow\\; ei = -IT $$

**Passage écart ↔ cote (attention aux unités)**

Les tables ISO donnent les écarts en **µm**, les cotes sont en **mm** :

$$ 1\\ \\mu m = 0,001\\ mm \\qquad 21\\ \\mu m = 0,021\\ mm $$

⚠️ **C'est la source d'erreur n°1 en examen.** Toujours vérifier l'ordre de grandeur : un IT de
21 mm sur une pièce de 20 mm serait absurde.

**Extrait de table IT (µm) — à savoir retrouver**

| Tranche (mm) | IT6 | IT7 | IT8 | IT9 | IT11 |
|---|---|---|---|---|---|
| 3 à 6 | 8 | 12 | 18 | 30 | 75 |
| 6 à 10 | 9 | 15 | 22 | 36 | 90 |
| 10 à 18 | 11 | 18 | 27 | 43 | 110 |
| **18 à 30** | **13** | **21** | **33** | **52** | **130** |
| 30 à 50 | 16 | 25 | 39 | 62 | 160 |
| 50 à 80 | 19 | 30 | 46 | 74 | 190 |
| 80 à 120 | 22 | 35 | 54 | 87 | 220 |
""",
            "exemple": """
**Cas industriel — Pourquoi Ø40 H7 et pas Ø40 H9 sur un logement de roulement ?**

Un roulement à billes **6208** (alésage 40, extérieur 80, largeur 18) doit être monté dans un
carter en aluminium. Le fabricant du roulement (SKF, NSK…) impose dans son catalogue :
**logement en H7 pour une charge tournante sur l'arbre, bague extérieure fixe**.

Comparons les deux choix :

| | Ø80 **H7** | Ø80 **H9** |
|---|---|---|
| IT (tranche 50-80) | 30 µm | 74 µm |
| Alésage réel possible | 80,000 à 80,030 | 80,000 à 80,074 |
| Bague ext. du roulement (tolérance constructeur, environ h6 : 0 / −19 µm) | 79,981 à 80,000 | 79,981 à 80,000 |
| **Jeu résultant** | **0 à 49 µm** | **0 à 93 µm** |
| Procédé | Alésage à l'alésoir ou barre à aléser | Fraisage courant |
| Coût relatif | ×2,5 | ×1 |

**Analyse :** avec H9, le jeu peut atteindre 93 µm. La bague extérieure, non maintenue, se met à
**tourner lentement dans son logement** (phénomène de *rampement*). Elle use le carter en aluminium
— matériau tendre — et en quelques centaines d'heures le logement devient ovalisé et irrécupérable :
c'est le carter entier qu'il faut remplacer, pas le roulement.

**Conclusion :** le H7 n'est pas un excès de zèle, c'est **la condition de survie du carter**. Ici la
fonction impose le grade. À l'inverse, le perçage de fixation du carter (4× Ø9) est laissé en **IT13**
(cote libre) : sa précision n'a aucune incidence fonctionnelle.
""",
            "exercice": """
**Exercice type examen — Décodage et calcul de cotes tolérancées**

**Partie A.** Pour chacune des désignations suivantes, préciser s'il s'agit d'un arbre ou d'un
alésage, donner l'IT (µm), les écarts, et les cotes limites :

1. **Ø25 H8**
2. **Ø25 f7**
3. **Ø60 h9**
4. **Ø12 js6**

*Données : IT tranche 18-30 → IT7 = 21, IT8 = 33 ; tranche 50-80 → IT9 = 74 ;
tranche 10-18 → IT6 = 11. Écart fondamental de f pour la tranche 18-30 : es = −20 µm.*

**Partie B.** Un technicien mesure au comparateur 5 pièces censées être des **Ø25 f7**.
Il relève : 24,982 — 24,975 — 24,959 — 24,968 — 24,980 (mm).
Déterminer les pièces conformes et justifier chaque rebut.

**Partie C.** Le bureau des méthodes propose de remplacer le **Ø25 f7** par un **Ø25 f8**
pour réduire le coût. L'IT8 vaut 33 µm sur cette tranche. Calculer les nouvelles cotes limites
et indiquer combien de pièces de la partie B deviendraient conformes. Commenter le risque.
""",
            "corrige": """
**PARTIE A**

**1. Ø25 H8 — ALÉSAGE** (majuscule)

Tranche : $18 < 25 \\le 30$ → **IT8 = 33 µm = 0,033 mm**
Lettre H → par définition $EI = 0$
$$ ES = EI + IT = 0 + 33 = +33\\ \\mu m $$

$$ \\boxed{Ø25\\ H8 = Ø25\\ ^{+0,033}_{\\;\\;\\;0} \\;\\Rightarrow\\; 25,000 \\le D \\le 25,033\\ mm} $$

**2. Ø25 f7 — ARBRE** (minuscule)

Tranche 18-30 → **IT7 = 21 µm**
Lettre f, située **sous** la ligne zéro → l'écart fondamental est l'écart **supérieur** :
$es = -20\\ \\mu m$
$$ ei = es - IT = -20 - 21 = -41\\ \\mu m $$

$$ \\boxed{Ø25\\ f7 = Ø25\\ ^{-0,020}_{-0,041} \\;\\Rightarrow\\; 24,959 \\le d \\le 24,980\\ mm} $$

**3. Ø60 h9 — ARBRE**

Tranche : $50 < 60 \\le 80$ → **IT9 = 74 µm**
Lettre h → par définition $es = 0$
$$ ei = es - IT = 0 - 74 = -74\\ \\mu m $$

$$ \\boxed{Ø60\\ h9 = Ø60\\ ^{\\;\\;\\;0}_{-0,074} \\;\\Rightarrow\\; 59,926 \\le d \\le 60,000\\ mm} $$

**4. Ø12 js6 — ARBRE, tolérance symétrique**

Tranche : $10 < 12 \\le 18$ → **IT6 = 11 µm**
$$ es = +\\frac{11}{2} = +5,5\\ \\mu m \\qquad ei = -5,5\\ \\mu m $$

$$ \\boxed{Ø12\\ js6 = Ø12 \\pm 0,0055 \\;\\Rightarrow\\; 11,9945 \\le d \\le 12,0055\\ mm} $$

---

**PARTIE B — Contrôle des 5 pièces**

Intervalle de conformité : **24,959 ≤ d ≤ 24,980 mm** (bornes **incluses**).

| Pièce | Mesure | Verdict | Justification |
|---|---|---|---|
| 1 | 24,982 | ❌ **REBUT** | 24,982 > 24,980 → dépasse $d_{max}$ de 2 µm. Arbre **trop gros**. |
| 2 | 24,975 | ✅ **CONFORME** | Dans l'intervalle, bien centrée. |
| 3 | 24,959 | ✅ **CONFORME** | Égale exactement $d_{min}$ → **la borne est incluse**, la pièce est bonne. Mais elle est à la limite : usure d'outil probable. |
| 4 | 24,968 | ✅ **CONFORME** | Dans l'intervalle. |
| 5 | 24,980 | ✅ **CONFORME** | Égale exactement $d_{max}$ → conforme. |

**Résultat : 4 conformes sur 5, soit 80 % de rendement.**

*Analyse de production :* la pièce 1 est trop grosse et la pièce 3 en limite basse — la dispersion
(24,959 à 24,982, soit **23 µm**) est **supérieure à l'IT de 21 µm**. Le procédé n'est pas capable :
même bien réglé, il produira toujours des rebuts. Il faut soit fiabiliser le procédé (rectification
au lieu de tournage), soit renégocier la tolérance avec le BE.

---

**PARTIE C — Passage en f8**

Tranche 18-30 → **IT8 = 33 µm**. La lettre **f** ne change pas → $es = -20\\ \\mu m$ (l'écart
fondamental ne dépend **que de la lettre**, jamais du grade — point clé de l'examen).

$$ ei = es - IT = -20 - 33 = -53\\ \\mu m $$

$$ \\boxed{Ø25\\ f8 \\;\\Rightarrow\\; 24,947 \\le d \\le 24,980\\ mm} $$

**Reprise du contrôle :**

| Pièce | Mesure | f7 | f8 |
|---|---|---|---|
| 1 | 24,982 | ❌ | ❌ **toujours rebut** |
| 2 | 24,975 | ✅ | ✅ |
| 3 | 24,959 | ✅ | ✅ |
| 4 | 24,968 | ✅ | ✅ |
| 5 | 24,980 | ✅ | ✅ |

**Nombre de pièces devenues conformes : AUCUNE (toujours 4/5).**

**Commentaire — c'est le piège de l'exercice.** Élargir de f7 à f8 a **repoussé la borne
inférieure** (de 24,959 à 24,947) mais **la borne supérieure est restée à 24,980**, puisque
l'écart fondamental $es = -20$ µm est fixé par la lettre f seule.

Or la pièce rebutée était **trop grosse**. Élargir le grade n'y change rien.

**Risque supplémentaire à signaler :** ce Ø25 f7 est très probablement destiné à un ajustement
**H7/f7** (rotation lubrifiée). En passant en f8, le jeu maximal augmente de 12 µm. Si la fonction
est un palier lisse, ce jeu supplémentaire dégrade la précision de guidage et peut créer du
battement. **On ne modifie jamais un grade sans revérifier l'ajustement complet** — ce sera l'objet
de la fiche 2.2.
""",
        },
        {
            "id": "2.2",
            "titre": "Les ajustements : jeu, incertain, serrage",
            "duree": "10 h",
            "cours": """
### 1. Définition

Un **ajustement** est l'association d'un **alésage** et d'un **arbre de même cote nominale**,
destinés à être assemblés. Il s'écrit **Ø20 H7/g6** : d'abord l'alésage (majuscule), puis
l'arbre (minuscule), séparés d'une barre de fraction.

Le comportement de l'assemblage — libre, ajusté, ou bloqué — dépend **uniquement** de la position
relative des deux zones de tolérance.

### 2. Les trois natures d'ajustement

**a) Ajustement AVEC JEU** — la zone de l'arbre est **entièrement en dessous** de celle de l'alésage.
L'arbre est **toujours** plus petit : la pièce peut tourner ou coulisser.
> Exemples : H7/g6, H7/f7, H8/e8, H11/c11

**b) Ajustement AVEC SERRAGE** — la zone de l'arbre est **entièrement au-dessus**. L'arbre est
**toujours** plus gros : il faut de la presse ou de la dilatation pour assembler.
> Exemples : H7/p6, H7/s6, H7/u6

**c) Ajustement INCERTAIN** — les deux zones **se chevauchent**. Selon les pièces réellement
usinées, on obtient du jeu **ou** du serrage. Utilisé pour un positionnement précis avec montage
au maillet.
> Exemples : H7/k6, H7/m6, H7/js6

### 3. Système de l'alésage normal (H) — celui qu'on utilise à 95 %

On fixe l'alésage en **H** (donc $EI = 0$) et on fait varier la lettre de l'arbre pour obtenir
l'ajustement souhaité.

**Pourquoi ?** Parce qu'un **alésage est plus difficile et plus coûteux à ajuster qu'un arbre**.
Un arbre se retouche facilement au tour (quelques centièmes de passe). Un alésage exige un
alésoir ou un outil de barre à aléser dédié — un par cote. En travaillant en H, l'atelier n'a
besoin que d'un **jeu réduit d'alésoirs standards** (H7 principalement), et adapte l'arbre.

*(Le système de l'arbre normal — h — existe et sert quand l'arbre est un produit du commerce non
retouchable : barre calibrée, tige de vérin chromée, axe normalisé. On écrit alors D9/h9, F8/h6…)*

### 4. Tableau des ajustements courants — à connaître

| Ajustement | Nature | Application typique |
|---|---|---|
| **H11/c11** | Jeu très large | Chape mécano-soudée, pièce peinte, assemblage grossier |
| **H9/d9** | Jeu large | Rotation rapide, mauvais alignement, échauffement |
| **H8/e8** | Jeu moyen | Palier de moteur, rotation rapide bien lubrifiée |
| **H7/f7** | Jeu | Palier lisse, axe de bielle, rotation lente lubrifiée |
| **H7/g6** | Jeu faible | Coulisseau précis, pige de centrage, démontage à la main |
| **H7/h6** | Jeu quasi nul | Glissement gras, centrage précis démontable |
| **H7/js6** | Incertain | Centrage, démontage possible à la main ou au maillet léger |
| **H7/k6** | Incertain | **Bague intérieure de roulement, charge tournante** — montage au maillet |
| **H7/m6** | Incertain / serré | Moyeu d'engrenage, montage à la presse, démontable |
| **H7/p6** | Serrage | Bague de guidage, goupille — presse ou dilatation |
| **H7/s6** | Serrage fort | Couronne dentée frettée — montage à chaud obligatoire |
| **H7/u6** | Serrage très fort | Transmission de couple par **adhérence seule**, sans clavette |

### 5. Méthode de résolution en 5 étapes (à appliquer systématiquement)

1. **Repérer** la tranche de dimension et lire les deux IT dans la table.
2. **Placer** l'alésage : lettre H → $EI = 0$, $ES = +IT$.
3. **Placer** l'arbre : lire l'écart fondamental (es si a→h, ei si k→z), en déduire l'autre.
4. **Calculer** $J_{max}$ et $J_{min}$.
5. **Conclure** sur la nature et vérifier la cohérence avec la fonction demandée.
""",
            "formules": """
**Les deux formules à connaître par cœur**

$$ \\boxed{J_{max} = ES - ei} \\qquad \\boxed{J_{min} = EI - es} $$

*Aide mémoire :* le **jeu maximal** s'obtient avec le **plus grand alésage** et le **plus petit arbre**.
Le **jeu minimal** avec le **plus petit alésage** et le **plus gros arbre**.

$$ J_{max} = D_{max} - d_{min} \\qquad J_{min} = D_{min} - d_{max} $$

**Interprétation des signes**

| Condition | Nature de l'ajustement |
|---|---|
| $J_{min} \\ge 0$ | **JEU** (jeu garanti dans tous les cas) |
| $J_{max} \\le 0$ | **SERRAGE** (serrage garanti dans tous les cas) |
| $J_{min} < 0 < J_{max}$ | **INCERTAIN** |

**Serrages (jeu négatif changé de signe)**

$$ S_{max} = -J_{min} = es - EI \\qquad S_{min} = -J_{max} = ei - ES $$

**Tolérance de l'ajustement** (dispersion totale du jeu) :

$$ IT_{ajustement} = J_{max} - J_{min} = IT_{alésage} + IT_{arbre} $$

Cette relation est très utile : elle montre qu'**on ne peut pas resserrer le jeu d'un assemblage
sans resserrer au moins l'une des deux pièces**.

**Effort de montage à la presse (ajustement serré)** — ordre de grandeur :

$$ F = \\pi \\cdot d \\cdot L \\cdot p \\cdot f $$

avec $d$ le diamètre (m), $L$ la longueur d'emmanchement (m), $p$ la pression de contact (Pa),
$f$ le coefficient de frottement (≈ 0,12 acier/acier à sec).

**Température de montage par dilatation** (frettage) :

$$ \\Delta T = \\frac{S_{max} + j_{montage}}{\\alpha \\cdot d} $$

avec $\\alpha \\approx 11 \\times 10^{-6}\\ \\mathrm{K^{-1}}$ pour l'acier, $j_{montage}$ un jeu de
manœuvre (≈ 0,05 mm).
""",
            "exemple": """
**Cas industriel — Montage complet d'un roulement 6205 sur arbre de pompe**

Un roulement rigide à billes **6205** (d = 25, D = 52, B = 15) équipe une pompe centrifuge.
L'arbre tourne, le carter est fixe. La charge (poids du rotor + poussée hydraulique) est **fixe
en direction**.

**Analyse du problème — la règle des charges :**

| Bague | Type de charge subie | Conséquence | Ajustement imposé |
|---|---|---|---|
| **Intérieure** (sur arbre tournant) | **Charge tournante** : chaque point de la bague passe successivement sous la zone chargée | Elle « rampe » si elle n'est pas serrée | **Serrage nécessaire → arbre k6** |
| **Extérieure** (dans carter fixe) | **Charge fixe** : toujours la même zone chargée | Pas de tendance au rampement, on veut pouvoir la démonter et permettre la dilatation axiale | **Jeu léger → alésage H7** |

**Calcul côté arbre — Ø25 k6 (tranche 18-30) :**
- IT6 = 13 µm ; écart fondamental de k : $ei = +2\\ \\mu m$ → $es = +15\\ \\mu m$
- Arbre : **25,002 à 25,015 mm**
- Alésage de la bague intérieure (tolérance constructeur roulement, environ **0 / −10 µm**) :
  **24,990 à 25,000 mm**
- $J_{max} = 0 - 2 = -2\\ \\mu m$ → **serrage de 2 à 25 µm : serrage garanti** ✔️

**Calcul côté carter — Ø52 H7 (tranche 50-80) :**
- IT7 = 30 µm → alésage **52,000 à 52,030 mm**
- Bague extérieure du roulement (environ **0 / −13 µm**) : **51,987 à 52,000 mm**
- $J_{max} = 30 - (-13) = 43\\ \\mu m$ ; $J_{min} = 0 - 0 = 0$ → **jeu de 0 à 43 µm** ✔️

**Ce que le montage donne concrètement :**
La bague intérieure se monte **à la presse ou par chauffage à ~80 °C** (jamais au marteau
directement sur la bague extérieure : on marquerait les pistes et le roulement serait mort avant
d'avoir servi). La bague extérieure se glisse à la main dans le carter et peut coulisser
axialement de quelques centièmes pour absorber la **dilatation thermique de l'arbre** en
fonctionnement — c'est le **palier libre** du montage.

**Erreur classique en entreprise :** monter l'arbre en **m6 ou p6** « pour être sûr ». Le serrage
excessif **dilate la bague intérieure**, réduit le jeu interne du roulement jusqu'à l'annuler, et
le roulement chauffe puis grippe en quelques heures. Le catalogue constructeur fait autorité,
il n'y a pas de marge de créativité ici.
""",
            "exercice": """
**Exercice type examen — Étude d'un montage à trois ajustements**

Un bâti supporte un axe Ø30 sur lequel pivote un galet. L'axe est **immobilisé** dans le bâti et
**libre** dans le galet. Un anneau élastique bloque l'ensemble axialement.

Le bureau d'études propose : **liaison bâti/axe = Ø30 H7/p6** — **liaison axe/galet = Ø30 H8/f7**.

*Données, tranche 18-30 mm : IT6 = 13 µm, IT7 = 21 µm, IT8 = 33 µm.
Écarts fondamentaux : p → ei = +22 µm ; f → es = −20 µm.*

**Questions :**

1. Pour la liaison **bâti/axe (H7/p6)** : calculer les cotes limites de l'alésage et de l'arbre,
   puis $J_{max}$ et $J_{min}$. Conclure sur la nature.
2. Pour la liaison **axe/galet (H8/f7)** : mêmes calculs et même conclusion.
3. Vérifier la cohérence fonctionnelle : chaque ajustement remplit-il bien son rôle ?
4. Calculer la **tolérance de l'ajustement** H8/f7 et vérifier la relation
   $IT_{ajustement} = IT_{alésage} + IT_{arbre}$.
5. Un stagiaire propose d'inverser : H7/f7 pour le bâti et H8/p6 pour le galet.
   Décrire précisément ce qui se passerait au montage puis en fonctionnement.
6. Le montage en p6 doit se faire par dilatation du bâti (acier,
   $\\alpha = 11\\times10^{-6}\\ \\mathrm{K^{-1}}$). Calculer l'élévation de température nécessaire
   en prévoyant un jeu de manœuvre de 0,03 mm.
""",
            "corrige": """
**1. LIAISON BÂTI / AXE — Ø30 H7/p6**

*Tranche : $18 < 30 \\le 30$ → tranche **18 à 30 mm*** (la borne supérieure est incluse — piège fréquent).

**Alésage Ø30 H7** : IT7 = 21 µm, lettre H → $EI = 0$
$$ ES = 0 + 21 = +21\\ \\mu m \\;\\Rightarrow\\; \\boxed{30,000 \\le D \\le 30,021\\ mm} $$

**Arbre Ø30 p6** : IT6 = 13 µm, lettre p (au-dessus de la ligne zéro) → $ei = +22\\ \\mu m$
$$ es = ei + IT = 22 + 13 = +35\\ \\mu m \\;\\Rightarrow\\; \\boxed{30,022 \\le d \\le 30,035\\ mm} $$

**Jeux :**
$$ J_{max} = ES - ei = 21 - 22 = \\mathbf{-1\\ \\mu m} $$
$$ J_{min} = EI - es = 0 - 35 = \\mathbf{-35\\ \\mu m} $$

$J_{max} \\le 0$ → **AJUSTEMENT AVEC SERRAGE.**
Serrage compris entre $S_{min} = 1\\ \\mu m$ et $S_{max} = 35\\ \\mu m$.

---

**2. LIAISON AXE / GALET — Ø30 H8/f7**

**Alésage Ø30 H8** : IT8 = 33 µm, $EI = 0$
$$ ES = +33\\ \\mu m \\;\\Rightarrow\\; \\boxed{30,000 \\le D \\le 30,033\\ mm} $$

**Arbre Ø30 f7** : IT7 = 21 µm, lettre f (sous la ligne zéro) → $es = -20\\ \\mu m$
$$ ei = es - IT = -20 - 21 = -41\\ \\mu m \\;\\Rightarrow\\; \\boxed{29,959 \\le d \\le 29,980\\ mm} $$

**Jeux :**
$$ J_{max} = 33 - (-41) = \\mathbf{+74\\ \\mu m} $$
$$ J_{min} = 0 - (-20) = \\mathbf{+20\\ \\mu m} $$

$J_{min} > 0$ → **AJUSTEMENT AVEC JEU.** Jeu garanti de 0,020 à 0,074 mm.

---

**3. Cohérence fonctionnelle : ✅ les deux choix sont corrects.**

- **Bâti/axe en serrage (H7/p6)** : l'énoncé impose que l'axe soit **immobilisé** dans le bâti.
  Un serrage de 1 à 35 µm bloque l'axe par **adhérence**, sans vis ni goupille. ✔️
  *Remarque de conception :* $S_{min} = 1\\ \\mu m$ est **très faible**. Dans le pire cas
  statistique, le serrage est quasi nul et l'axe pourrait tourner. Si le couple parasite est
  significatif, on préférerait **H7/r6** ($ei = +28$, donc $S_{min} = 7\\ \\mu m$) pour une marge plus sûre.

- **Axe/galet en jeu (H8/f7)** : l'énoncé impose que le galet **pivote librement**. Un jeu de
  20 à 74 µm permet la rotation et le logement d'un film de graisse. ✔️
  Le grade H8 (plutôt que H7) est un bon choix économique : le galet est souvent une pièce
  frittée ou en polymère, où IT7 serait coûteux sans gain fonctionnel.

---

**4. Tolérance de l'ajustement H8/f7**

$$ IT_{ajustement} = J_{max} - J_{min} = 74 - 20 = \\mathbf{54\\ \\mu m} $$

Vérification par la relation :
$$ IT_{alésage} + IT_{arbre} = IT8 + IT7 = 33 + 21 = \\mathbf{54\\ \\mu m} \\quad ✔️ $$

**Interprétation :** le jeu réel varie de 20 à 74 µm selon les pièces, soit un rapport **de 1 à 3,7**.
Si la fonction exigeait un jeu mieux maîtrisé (guidage de précision), il faudrait resserrer :
H7/g6 donnerait $IT_{aj} = 21 + 13 = 34$ µm pour un jeu de 7 à 34 µm.

---

**5. Conséquences de l'inversion (H7/f7 au bâti, H8/p6 au galet)**

**Au bâti — H7/f7 :** $J_{max} = 21 + 41 = +62$ µm, $J_{min} = 0 + 20 = +20$ µm → **jeu**.
→ **L'axe n'est plus immobilisé dans le bâti.** Il devient libre de tourner et de se déplacer
axialement dans son logement.

**Au galet — H8/p6 :** $J_{max} = 33 - 22 = +11$ µm, $J_{min} = 0 - 35 = -35$ µm →
$J_{min} < 0 < J_{max}$ → **ajustement INCERTAIN**.
→ Selon les pièces, le galet sera soit légèrement libre (11 µm de jeu), soit **serré sur l'axe
jusqu'à 35 µm**.

**Scénario au montage :** le galet, serré sur l'axe, ne se monte plus à la main — il faut la presse,
au risque d'endommager le galet s'il est en fonte ou en polymère.

**Scénario en fonctionnement :** dans le cas le plus probable, le galet est **solidaire de l'axe**
par serrage, et c'est l'**axe qui tourne dans le bâti** (où il a maintenant du jeu). La rotation
se fait donc sur la **mauvaise interface** :
- le bâti n'est ni lubrifié, ni traité, ni dimensionné pour un contact glissant ;
- le contact acier/acier non lubrifié **grippe** rapidement ;
- l'alésage du bâti s'ovalise, le galet prend du battement et l'ensemble se dégrade.

**Conclusion :** l'inversion est **fonctionnellement inacceptable**. Elle illustre la règle
générale : *la pièce qui doit tourner reçoit le jeu ; la pièce qui doit être fixe reçoit le serrage.*

---

**6. Température de montage par dilatation du bâti**

On doit dilater l'alésage du bâti d'au moins le serrage maximal, augmenté d'un jeu de manœuvre :

$$ \\Delta d_{nécessaire} = S_{max} + j_{montage} = 0,035 + 0,030 = 0,065\\ mm $$

Loi de dilatation linéique :

$$ \\Delta d = \\alpha \\cdot d \\cdot \\Delta T \\;\\Rightarrow\\; \\Delta T = \\frac{\\Delta d}{\\alpha \\cdot d} $$

$$ \\Delta T = \\frac{0,065}{11\\times10^{-6} \\times 30} = \\frac{0,065}{330\\times10^{-6}} = \\mathbf{197\\ °C} $$

**Température de chauffe (bâti initialement à 20 °C) :**

$$ T = 20 + 197 \\approx \\mathbf{217\\ °C} $$

**Commentaire technique — indispensable pour avoir tous les points :**

Chauffer à 217 °C est **réalisable** (four ou plaque chauffante) mais soulève deux réserves :
- si le bâti est en **acier trempé-revenu**, dépasser la température de revenu (souvent 200 à 250 °C)
  **abaisse la dureté de façon irréversible** ;
- il est ici plus judicieux de **refroidir l'axe** à l'azote liquide (−196 °C, soit ΔT = 216 °C)
  ou au carboglace (−78 °C), ce qui **ne dégrade aucun traitement** du bâti.

En pratique industrielle, pour un serrage de 35 µm sur Ø30, on utiliserait simplement une
**presse hydraulique** : l'effort nécessaire reste modeste et le montage est instantané.
""",
        },
        {
            "id": "2.3",
            "titre": "Tolérancement géométrique (GPS) et cotation fonctionnelle",
            "duree": "10 h",
            "cours": """
### 1. Pourquoi les tolérances dimensionnelles ne suffisent pas

Un arbre coté **Ø20 h6** peut être parfaitement conforme au pied à coulisse en tout point… et être
une **banane**. La cote dimensionnelle contrôle un **diamètre local**, pas la **forme globale**.
De même, deux alésages parfaitement Ø10 H7 peuvent être **non parallèles** et rendre l'assemblage
impossible.

Le **tolérancement géométrique** (normes GPS — *Geometrical Product Specifications*, ISO 1101)
complète la cote en imposant des contraintes sur la **forme**, l'**orientation**, la **position**
et le **battement**.

### 2. Les quatre familles de tolérances

**a) Tolérances de FORME** (aucune référence nécessaire)

| Symbole | Nom | Ce qui est contrôlé |
|---|---|---|
| ⏤ | Rectitude | Une ligne doit rester entre deux droites parallèles |
| ⏥ | Planéité | Une surface doit rester entre deux plans parallèles |
| ○ | Circularité | Une section doit rester entre deux cercles concentriques |
| ⌭ | Cylindricité | Un cylindre entre deux cylindres coaxiaux |

**b) Tolérances d'ORIENTATION** (référence obligatoire)

| Symbole | Nom |
|---|---|
| ∥ | Parallélisme |
| ⊥ | Perpendicularité |
| ∠ | Inclinaison |

**c) Tolérances de POSITION** (référence obligatoire)

| Symbole | Nom |
|---|---|
| ⌖ | Localisation |
| ◎ | Concentricité / coaxialité |
| ⌯ | Symétrie |

**d) Tolérances de BATTEMENT** (référence obligatoire — axe de rotation)

| Symbole | Nom |
|---|---|
| ↗ | Battement simple (radial ou axial) |
| ⌰ | Battement total |

### 3. Le cadre de tolérance

Il se lit de gauche à droite, en trois cases :

```
┌────┬────────┬─────┐
│ ⊥  │ Ø0,05  │  A  │
└────┴────────┴─────┘
   1      2      3
```

1. **Symbole** de la caractéristique contrôlée (perpendicularité)
2. **Valeur** de la tolérance, précédée de **Ø** si la zone est **cylindrique** (sinon la zone est
   comprise entre deux plans ou deux droites parallèles)
3. **Lettre(s) de référence** (A, B, C…), dans l'ordre de priorité

Se lit : *« l'axe de cet élément doit être contenu dans un cylindre de Ø0,05 mm perpendiculaire à
la surface de référence A ».*

### 4. Les références (datums)

Une référence est matérialisée par un **triangle noirci** relié à un cadre lettré. Le choix des
références n'est **jamais arbitraire** : elles doivent reproduire la **mise en position réelle
de la pièce dans le mécanisme** (isostatisme).

- **Référence primaire (A)** : élimine 3 degrés de liberté — c'est en général la **grande surface
  d'appui** (mise en position par un plan).
- **Référence secondaire (B)** : élimine 2 degrés — souvent un **alésage** ou un **appui linéaire**.
- **Référence tertiaire (C)** : élimine le dernier degré — un **appui ponctuel**.

Ensemble : 3 + 2 + 1 = **6 degrés de liberté supprimés** → la pièce est **isostatiquement posée**.

### 5. L'exigence du maximum de matière Ⓜ

Symbole **Ⓜ** placé après la valeur : *« la tolérance indiquée s'applique lorsque la pièce est à
son état de maximum de matière ; si elle s'en écarte, la tolérance géométrique peut être
augmentée d'autant. »*

C'est un **bonus de tolérance** parfaitement légitime : si un trou de fixation est plus grand que
le minimum, il pardonne davantage de défaut de position. Utiliser Ⓜ sur les **trous de passage**
augmente le rendement sans aucun risque d'assemblage. C'est un réflexe d'économiste du BE.

$$ t_{réelle} = t_{indiquée} + |D_{réel} - D_{MMC}| $$
""",
            "formules": """
**Bonus de tolérance au maximum de matière (Ⓜ)**

Pour un **alésage** (le maximum de matière correspond au **plus petit** trou) :

$$ t_{disponible} = t_{spécifiée} + (D_{réel} - D_{min}) $$

Pour un **arbre** (le maximum de matière correspond au **plus gros** arbre) :

$$ t_{disponible} = t_{spécifiée} + (d_{max} - d_{réel}) $$

**Localisation en coordonnées cartésiennes → zone cylindrique**

Si un trou est mal placé de $\\Delta x$ et $\\Delta y$ par rapport à sa position théorique :

$$ \\text{écart radial} = \\sqrt{\\Delta x^2 + \\Delta y^2} $$

La pièce est conforme si : $ 2\\sqrt{\\Delta x^2 + \\Delta y^2} \\le t $ (avec $t$ le Ø de la zone).

**Conversion tolérance carrée → tolérance cylindrique**

Une tolérance $\\pm a$ en X et en Y définit un **carré** de côté $2a$. La zone cylindrique
circonscrite vaut :

$$ Ø_{zone} = 2a\\sqrt{2} \\approx 1,41 \\times 2a $$

C'est pourquoi **la localisation ⌖ avec zone cylindrique est 57 % plus permissive** que la cotation
en ±, à sécurité d'assemblage identique. Encore un gain gratuit.

**Battement radial et excentricité**

$$ \\text{Battement radial} = 2 \\times e \\quad (\\text{e = excentricité de l'axe}) $$

**Relation forme / dimension (principe de l'enveloppe, symbole Ⓔ)**

$$ \\text{défaut de forme} \\le IT_{dimensionnel} $$

Sans indication contraire, le défaut de forme est **implicitement limité par l'IT dimensionnel**
(principe de l'enveloppe, norme ISO 14405). On ne spécifie une tolérance de forme explicite que
si l'on veut la rendre **plus serrée** que l'IT.
""",
            "exemple": """
**Cas industriel — Bride de fixation d'un vérin sur bâti**

Une bride en acier S355 de 100 × 100 × 20 mm doit fixer un vérin. Elle comporte :
- un **alésage central Ø63 H8** recevant le nez du vérin (centrage) ;
- **4 trous Ø11** de fixation sur un carré de 80 mm ;
- une **face d'appui** plaquée contre le bâti.

**Cotation dimensionnelle seule (insuffisante) :** Ø63 H8, 4× Ø11, entraxes 80 ± 0,2.
Une bride ainsi cotée peut être conforme et **inutilisable** : la face d'appui gauchie, l'alésage
central non perpendiculaire, les trous mal orientés.

**Cotation GPS complète mise en place par le BE :**

| Spécification | Cadre | Justification fonctionnelle |
|---|---|---|
| Face d'appui = **référence A** | ⏥ 0,05 | La bride doit porter à plat, sinon le serrage des vis la déforme et désaligne le vérin. |
| Alésage Ø63 = **référence B** | ⊥ Ø0,03 A | Le nez du vérin doit être perpendiculaire au bâti ; sinon la tige travaille en flexion. |
| 4× Ø11 | ⌖ Ø0,4 **Ⓜ** A B | Les trous doivent laisser passer 4 vis M10 ; leur position exacte importe peu tant que ça passe. |
| Face arrière | ∥ 0,1 A | Assure une épaisseur régulière, évite le basculement. |

**Le gain apporté par Ⓜ, chiffré :**
- Trous à leur **minimum** (Ø11,0) → tolérance de position = **Ø0,4 mm**
- Trous à leur **maximum** (Ø11,43, IT13) → bonus = 11,43 − 11,00 = 0,43 mm
  → tolérance disponible = 0,4 + 0,43 = **Ø0,83 mm**, soit **plus du double**.

L'atelier peut percer avec un simple gabarit au lieu d'un centre d'usinage indexé. Le rendement
passe de 82 % à 99 %, **sans le moindre risque de non-assemblage** — car la condition Ⓜ garantit
mathématiquement que les vis passeront toujours.
""",
            "exercice": """
**Exercice type examen — Lecture et exploitation d'un tolérancement géométrique**

Une plaque de guidage porte deux alésages **Ø12 H7** destinés à recevoir deux colonnes de guidage
d'un outillage de presse. Le dessin porte les spécifications suivantes :

- La face inférieure est **référence A**, avec ⏥ **0,02**
- Alésage n°1 : ⊥ **Ø0,02 A**
- Alésage n°2 : ⌖ **Ø0,05 Ⓜ A B**, où **B** est l'axe de l'alésage n°1
- Entraxe théorique encadré : ⟦150⟧

**Questions :**

1. Traduire en français chacune des quatre spécifications.
2. Pourquoi l'entraxe 150 est-il **encadré** et non tolérancé en ± ?
3. Expliquer le choix de A comme référence primaire et de B comme référence secondaire.
4. L'alésage n°2 est mesuré à **Ø12,015 mm**. Calculer la tolérance de localisation réellement
   disponible.
5. Le centre mesuré de l'alésage n°2 se trouve à $\\Delta x = +0,022$ mm et $\\Delta y = -0,014$ mm
   de sa position théorique. La pièce est-elle conforme ? Justifier par le calcul.
6. Le BE envisage de remplacer ⌖ Ø0,05 Ⓜ par une cotation **150 ± 0,025**.
   Comparer les deux approches par le calcul et conclure.
""",
            "corrige": """
**1. Traduction des spécifications**

**a) ⏥ 0,02 (référence A)** — *« La face inférieure doit être comprise entre deux plans parallèles
distants de 0,02 mm. »* C'est une tolérance de **forme**, elle ne nécessite aucune référence.

**b) ⊥ Ø0,02 A (alésage n°1)** — *« L'axe de l'alésage n°1 doit être contenu dans un cylindre de
diamètre 0,02 mm, perpendiculaire au plan de référence A. »*
Le symbole **Ø** est essentiel : la zone est un **cylindre**, pas deux plans. Le défaut est donc
limité dans **toutes les directions**.

**c) ⌖ Ø0,05 Ⓜ A B (alésage n°2)** — *« L'axe de l'alésage n°2 doit être contenu dans un cylindre
de Ø0,05 mm, dont l'axe est à la position théorique exacte (150 mm de B, perpendiculaire à A),
cette tolérance pouvant être augmentée du bonus de matière lorsque l'alésage s'écarte de son
maximum de matière. »*

**d) ⟦150⟧** — cote **théorique exacte** (*basic dimension*). Elle définit la **position idéale**
et n'est **pas tolérancée** : c'est le cadre ⌖ qui porte toute la tolérance.

---

**2. Pourquoi l'entraxe est encadré**

Une cote encadrée est une **cote théorique exacte**. La tolérancer en ± reviendrait à définir
**deux fois** la même contrainte (une fois par le ±, une fois par le ⌖), ce qui créerait une
**ambiguïté de contrôle** : lequel des deux prévaut ?

La règle GPS est stricte : **quand une localisation ⌖ est utilisée, toutes les cotes de position
associées sont encadrées.** Cela garantit une définition unique et non ambiguë.

---

**3. Choix des références (isostatisme)**

- **A = face inférieure (référence primaire)** : c'est la surface par laquelle la plaque **repose
  réellement** sur le bâti de la presse. Un plan supprime **3 degrés de liberté**
  (1 translation + 2 rotations). C'est la surface la plus étendue → la plus stable.

- **B = axe de l'alésage n°1 (référence secondaire)** : une fois la plaque posée à plat, il reste
  3 degrés (2 translations + 1 rotation dans le plan). La première colonne, engagée dans
  l'alésage n°1, **supprime les 2 translations**. Il ne reste que la rotation autour de cet axe.

- Le second alésage, localisé par rapport à A **et** B, supprime le dernier degré.

**L'ordre A puis B n'est pas interchangeable** : il reproduit la **chronologie réelle du montage**
(on pose à plat, *puis* on engage la première colonne, *puis* la seconde). Inverser l'ordre
donnerait un contrôle qui ne correspond plus à la mise en position réelle.

---

**4. Tolérance disponible avec Ⓜ**

L'alésage n°2 est un **Ø12 H7** → tranche 10-18 → IT7 = 18 µm → **12,000 à 12,018 mm**.

Pour un **alésage**, le maximum de matière correspond au **plus petit diamètre** :
$$ D_{MMC} = D_{min} = 12,000\\ mm $$

Bonus obtenu :
$$ \\text{bonus} = D_{réel} - D_{MMC} = 12,015 - 12,000 = 0,015\\ mm $$

Tolérance de localisation réellement disponible :
$$ t_{disponible} = t_{spécifiée} + \\text{bonus} = 0,05 + 0,015 = \\mathbf{Ø0,065\\ mm} $$

*Soit 30 % de tolérance en plus, gratuitement.*

---

**5. Contrôle de conformité**

Écart radial du centre par rapport à la position théorique :

$$ e = \\sqrt{\\Delta x^2 + \\Delta y^2} = \\sqrt{0,022^2 + 0,014^2} = \\sqrt{0,000484 + 0,000196} $$
$$ e = \\sqrt{0,000680} = 0,0261\\ mm $$

L'axe réel doit être **dans** le cylindre de tolérance, donc son écart au centre doit être
inférieur au **rayon** de la zone :

$$ \\text{diamètre de la zone occupée} = 2e = 2 \\times 0,0261 = \\mathbf{0,0522\\ mm} $$

Comparaison :
$$ 0,0522\\ mm \\;\\le\\; 0,065\\ mm \\quad ✔️ $$

**La pièce est CONFORME.**

⚠️ **Point crucial :** sans le modificateur Ⓜ, la tolérance serait restée à Ø0,05 mm et
$0,0522 > 0,05$ → la pièce aurait été **REBUTÉE à tort**. C'est exactement le gain que Ⓜ apporte :
cette pièce s'assemble parfaitement, il n'y avait aucune raison de la jeter.

---

**6. Comparaison ⌖ Ø0,05 Ⓜ contre 150 ± 0,025**

**Approche par cotation ± :** la zone de tolérance est un **carré** de côté $2 \\times 0,025 = 0,05$ mm.
La diagonale de ce carré vaut :

$$ \\text{diagonale} = 0,05 \\times \\sqrt{2} = 0,0707\\ mm $$

**Approche par localisation ⌖ :** la zone est un **cylindre** de Ø0,05 mm (Ø0,065 avec le bonus).

**Comparaison chiffrée :**

| Critère | 150 ± 0,025 | ⌖ Ø0,05 Ⓜ |
|---|---|---|
| Forme de la zone | Carré 0,05 × 0,05 | Cylindre Ø0,05 (Ø0,065 avec bonus) |
| Surface de la zone | $0,05^2 = 0,0025\\ mm^2$ | $\\pi \\times 0,025^2 = 0,00196\\ mm^2$ (Ø0,05) |
| Écart maximal admis | 0,0354 mm (dans les coins) | 0,025 mm (Ø0,05) / 0,0325 mm (Ø0,065) |
| Isotropie | ❌ Non : plus permissif en diagonale qu'en X ou Y | ✅ Oui : même tolérance dans toutes les directions |
| Bonus de matière | ❌ Impossible | ✅ Oui |
| Notre pièce (e = 0,0261) | ✅ Conforme ($\\Delta x = 0,022 < 0,025$ et $\\Delta y = 0,014 < 0,025$) | ✅ Conforme grâce à Ⓜ |

**Conclusion : la localisation ⌖ Ø0,05 Ⓜ est nettement supérieure.**

Trois raisons :

1. **Elle est isotrope.** Le ± autorise 0,0354 mm en diagonale contre 0,025 mm sur les axes — un
   défaut de 41 % plus grand est accepté dans une direction sans aucune justification
   fonctionnelle. La colonne de guidage, elle, ne sait pas si elle est décalée « en diagonale ».

2. **Elle exploite le bonus de matière.** Le ± ne le permet pas : une pièce parfaitement
   assemblable peut être rebutée.

3. **Elle est non ambiguë au contrôle.** La localisation se vérifie par un **calibre fonctionnel**
   (un simple gabarit à deux pions) qui reproduit exactement la condition d'assemblage, alors que
   le ± exige une mesure sur MMT avec interprétation des références.

*Recommandation au BE : conserver ⌖ Ø0,05 Ⓜ A B.*
""",
        },
    ],
}
