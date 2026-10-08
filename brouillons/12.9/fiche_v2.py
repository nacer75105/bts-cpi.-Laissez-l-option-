FICHE_12_9 = {
    "id": "12.9",
    "titre": "Simulation numérique et chaîne numérique : lire et critiquer un calcul, gérer les données",
    "duree": "6 h",
    "cours": """### 1. Pourquoi cette fiche

Avant de fabriquer une pièce, le bureau d'études la **valide** : va-t-elle tenir ? Pour une pièce simple, le
calcul de RDM à la main suffit (blocs 4 et 12). Pour une forme compliquée — un carter, une équerre, une pièce
moulée — on passe par une **simulation par éléments finis**.

Le programme du BTS fixe le niveau : pour des **cas simples**, le technicien propose la modélisation et conduit
lui-même la simulation ; pour les **cas complexes**, il **dialogue avec un spécialiste** (le calculateur) à qui il
la confie ; dans tous les cas, il **interprète les résultats en autonomie**. La taille et le type de maillage sont
**donnés** dans le sujet. Cette fiche se concentre sur la **lecture critique** d'un résultat fourni ; la mise en
œuvre du logiciel se pratique en TP.

*Le piège classique, que toute la fiche combat : croire le calcul parce que l'image est belle. Un logiciel
calcule exactement ce qu'on lui a décrit — si la description est fausse, le résultat est faux, avec de jolies
couleurs.*

**Les mots à connaître, en français courant :**

| Mot | En français courant |
|---|---|
| **maillage** | le découpage de la pièce en petits morceaux simples (les éléments) |
| **élément** | un petit morceau du maillage : triangle en 2D, tétraèdre (petite pyramide à 4 faces) en 3D |
| **nœud** | un sommet d'élément : c'est là que le logiciel calcule les déplacements |
| **conditions aux limites** | comment la pièce est tenue (fixations, appuis) et chargée (forces, pressions) |
| **contrainte de Von Mises** | la contrainte équivalente (fiche 12.2), affichée en couleurs sur toute la pièce |
| **singularité** | un point où le modèle affiche une contrainte sans limite, qui n'existe pas en réalité |
| **convergence** | la valeur ne change presque plus quand on affine le maillage : on peut lui faire confiance |
| **calculateur** | la **personne** (ingénieur ou technicien) spécialiste de la simulation — pas la machine |
| **PDM** | le logiciel qui range, suit et protège toutes les données d'un projet |

### 2. Le principe : découper pour calculer

[[FIG:fem_maillage]]

Le logiciel ne sait pas calculer directement une forme compliquée. Il la **découpe** en milliers de petits
**éléments** simples, accrochés les uns aux autres par leurs sommets, les **nœuds**. *Image : chaque élément se
comporte comme un petit ressort ; la pièce maillée devient un grand réseau de ressorts accrochés par leurs nœuds,
comme un sommier.* Le logiciel cherche de combien chaque nœud **se déplace** sous la charge ; il en déduit les
**déformations** (comme ε = ΔL / L en traction), puis les **contraintes** (σ = E ε, loi de Hooke).

- **Maillage grossier** : peu d'éléments, calcul rapide, résultat approximatif — il peut « rater » un pic de
  contrainte dans un petit congé.
- **Maillage fin** : plus précis, mais calcul plus long (sauf sur une singularité, § 5, où la valeur grimpe sans
  fin). Sur une note de calcul, **vérifie** que le maillage est plus fin aux congés, trous et changements de
  section : sinon, un pic a pu passer inaperçu.

*Image : c'est comme dessiner un cercle avec des segments. Avec 6 segments, on a un hexagone ; avec 100, on ne
voit plus la différence. Le maillage approche la pièce de la même façon.*

**Ce qu'on peut simuler** (le programme cite plusieurs types de logiciels) : le comportement **mécanique**
(statique, cinématique, dynamique), le **calcul de structures** — modèle **poutre** ou modèle **volumique** (les
modèles surfaciques ne sont pas exigés) —, la **simulation de procédés** (par exemple le remplissage d'un moule,
bloc 13) et l'**ergonomie** (réalité virtuelle). Cette fiche traite du calcul de structure volumique, le plus
courant en bureau d'études mécanique. Dans tous les cas, le résultat dépend des **données d'entrée** :
géométrie, matériau (E, Re), conditions aux limites, maillage.

### 3. Les conditions aux limites : là où tout se joue

[[FIG:fem_conditions_limites]]

Il faut dire au logiciel **comment la pièce est tenue** (fixations, appuis) et **comment elle est chargée**
(forces, pressions, couples). C'est la traduction des **liaisons** et des **actions mécaniques** de la statique
(blocs 6 et 12). La figure montre **la même pièce réelle**, tenue par deux vis, déclarée de trois façons :

- **Juste** : fixée sur les trous de vis, en appui sur la face du bâti ; la force sur la surface où elle
  s'applique vraiment.
- **Trop rigide** : bloquer toute une face alors que la pièce ne tient que par deux vis rend le modèle plus raide
  que la réalité. La **flèche est sous-estimée**, et les **contraintes sont faussées** : celles qui comptent,
  autour des vis, ne sont pas calculées, et un pic artificiel apparaît souvent au bord de la zone bloquée.
  *Image : un plongeoir boulonné au bord de la piscine par deux boulons. Si on déclare au logiciel qu'il est
  collé sur la moitié de sa longueur, sa partie libre est raccourcie : il plie beaucoup moins qu'en vrai. La pièce
  calculée n'est plus celle qu'on fabriquera.*
- **Pas tenue** : le logiciel cherche de combien la pièce se déforme. Une pièce qu'aucune fixation ne retient
  glisse en bloc sous la force, comme un carton poussé sur de la glace : le calcul ne peut pas aboutir (message
  d'erreur ou résultat absurde).
- **Force en un point** : σ = F / S ; si la force est appliquée sur un seul nœud, la surface S est presque nulle,
  donc σ devient énorme sous ce point — l'effet d'une pointe de punaise. Une vraie force s'applique toujours sur
  une surface.

*C'est pourquoi un mauvais appui fausse tout : le logiciel n'invente rien, il calcule la pièce qu'on lui a
décrite — pas celle qu'on fabriquera.*

### 4. Lire une carte de Von Mises

[[FIG:fem_von_mises]]

Le résultat le plus courant est une **cartographie** (le programme cite les textes, courbes et cartographies) :
la pièce colorée selon la **contrainte équivalente de Von Mises**, la même que celle de la fiche 12.2, calculée
en chaque point. Ce critère convient aux matériaux **ductiles** (aciers, alliages d'aluminium) ; une pièce en
matériau fragile, comme une fonte, se juge autrement.

**Comment la lire, dans l'ordre :**
1. **Lire l'échelle** : quelles valeurs, en quelle unité (MPa), du bleu (faible) au rouge (fort) ? Les couleurs
   seules ne disent rien : un rouge vaut peut-être 20 MPa sur une pièce, 400 MPa sur une autre. Si l'échelle va
   jusqu'au maximum affiché, un pic de singularité « écrase » toutes les autres couleurs, et la pièce paraît
   bleue.
2. **Repérer le maximum** et **où** il se trouve : c'est la **zone critique**.
3. **Se demander si ce maximum est crédible** (§ 5 : singularité ou vraie concentration ?).
4. **Conclure avec la condition de résistance** (fiche 12.2) : σ éq ≤ Rpe = Re / s, où **Rpe** est la
   résistance pratique, la contrainte qu'on s'autorise. Autrement dit : **s obtenu = Re / σ éq** doit être au
   moins égal au **s exigé** par le cahier des charges.

**Pourquoi Re, et pas Rm ?** Au-delà de Re, la pièce reste tordue une fois la charge retirée, comme un trombone
trop plié : on veut qu'elle revienne à sa forme. Et le calcul lui-même suppose ce comportement de ressort.

**Toujours vérifier par un ordre de grandeur à la main.** Exemple : un **plat** (barre méplate) en S235
(Re = 235 MPa), de section 30 × 8 mm (largeur 30 mm, épaisseur 8 mm dans le sens de la force), encastré, reçoit
F = 500 N à 100 mm de l'encastrement. À la main (fiche 4.3) : M = F × L = 500 × 100 = 50 000 N·mm ;
I/v = b h²/6 = 30 × 8² / 6 = 320 mm³ (I/v : module de flexion) ; σ = M / (I/v) = 50 000 / 320 ≈ **156 MPa**, sur
les faces haute et basse de la section d'encastrement. La carte affiche environ 150 MPa à cet endroit : le calcul
et la simulation se confirment. s obtenu = 235 / 156,25 ≈ **1,50**.

**Les déplacements aussi se lisent.** Le logiciel affiche une carte de **déplacements** (en mm). Sur ce même plat,
la flèche au bout se calcule à la main : f = F L³ / (3 E I), avec I = b h³/12 = 30 × 8³ / 12 = 1 280 mm⁴ et
E = 210 000 MPa (acier) : f = 500 × 100³ / (3 × 210 000 × 1 280) ≈ **0,62 mm**. La carte de déplacements doit
afficher environ 0,6 mm au bout libre.

> **La main et la simulation se contrôlent l'une l'autre.**
> - Le calcul à la main donne la contrainte **nominale**, celle de la poutre « idéale », sans trou ni congé.
> - La simulation voit en plus les détails de forme : près d'un congé ou d'un trou, elle doit trouver **un peu
>   plus** que la main — c'est le Kt des fiches 4.1 et 3.5. C'est normal, et c'est même ce qu'on attend d'elle.
> - Si elle trouve **nettement moins** que la main dans la section la plus chargée, quelque chose l'a « aidée » à
>   tort : un appui trop étendu, une force mal saisie, une erreur d'unité. Un petit écart est normal (les deux
>   méthodes ne font pas les mêmes approximations) ; un écart important doit être **expliqué** avant de conclure ;
>   un facteur 2 ou 10 trahit presque toujours une erreur grossière.
> - Tant que l'écart n'est pas expliqué, on retient la valeur **la plus défavorable** : c'est elle qui donne le
>   plus petit s. Ce n'est jamais « la simulation qui a raison parce qu'elle est plus précise ».

### 5. Les limites du modèle : un résultat de calcul n'est pas la réalité

[[FIG:fem_singularite]]

**La singularité à l'angle vif.** Un **angle rentrant**, c'est un coin creux vu depuis la matière, comme le coin
intérieur d'une équerre en L. Dans le modèle du calcul (l'**élasticité linéaire** : contrainte proportionnelle à
la déformation, loi de Hooke), la contrainte au sommet d'un angle rentrant **parfaitement vif** est
théoriquement **infinie** (résultat établi par M. L. Williams en 1952). Le logiciel ne peut pas afficher l'infini :
il affiche une grande valeur, **qui augmente à chaque fois qu'on affine le maillage** (380, puis 520, puis
700 MPa…).

*Image : la loupe sans fin. Zoomer sur un congé, c'est finir par voir un arrondi d'une certaine taille : la valeur
se fixe. Zoomer sur un angle parfaitement vif, c'est retrouver toujours le même coin pointu, quel que soit le
grossissement. Chaque raffinement du maillage est un zoom de plus : le pic monte encore.*

> **Pic qui grimpe, pic qui trompe ; pic qui se pose, pic qui compte.**

**Comment reconnaître une singularité :**
- le pic est **ponctuel**, exactement sur un angle vif, sous une force appliquée en un point, sur une fixation
  ponctuelle, ou au bord d'une zone déclarée bloquée (là où le bord bloqué rejoint le bord libre) ;
- il **grimpe sans se stabiliser** quand on raffine le maillage.

**Attention : c'est le chiffre qui est faux, pas le danger.** Un vrai coin n'est jamais parfaitement vif : il a
toujours un petit rayon (d'usinage, de moulage) — c'est pourquoi la fiche 4.1 donne à une arête vive réelle un
Kt **fini**. Seul le modèle, parfaitement vif, donne l'infini. Ce coin concentre bien les contraintes, et c'est là
que démarre une fissure de fatigue. On n'écrit donc pas « 700 MPa » dans la note, mais on demande un congé.

**La vraie concentration de contrainte.** Avec un **congé** de rayon réel, le pic devient fini : sur les derniers
maillages, la valeur se **stabilise** (170, 174, 175 MPa) — on dit que le calcul **converge**. Celle-là est
**réelle** : c'est la concentration de contrainte des fiches 4.1 et 3.5 (σ maxi = Kt × σ nominale). Elle compte
**double** : elle réduit le coefficient de sécurité, et elle marque l'endroit où une fissure de **fatigue**
démarrerait. Une contrainte sous Re ne casse pas la pièce du premier coup ; répétée des milliers de fois
(vibrations, charges qui vont et viennent), elle peut faire naître une fissure (fiche 3.5).

**Ce qu'on fait d'une singularité :** on ne la prend pas pour la contrainte de la pièce ; on **demande au
calculateur** de modéliser le vrai congé et de montrer que la valeur se stabilise. Ici, le maillage est donné :
il ne s'agit pas de mener une étude de convergence, mais de **lire** celle qu'on vous fournit.

**Les autres limites à garder en tête :**
- **maillage trop grossier** : un pic réel dans un petit congé peut être « lissé » et passer inaperçu ;
- **hypothèses du modèle** : comportement élastique, matériau homogène, géométrie idéale — sans défauts de
  fabrication, sans contraintes résiduelles de soudage ;
- **données d'entrée** : un mauvais matériau (Re, module d'Young) ou une force fausse donnent un résultat faux ;
- d'où la **comparaison au réel** demandée par le programme : un essai sur prototype confirme ou non.

> **Les cinq questions à poser au calculateur avant de signer :**
> 1. Où as-tu mis les fixations, et est-ce là que la pièce est vraiment tenue ?
> 2. Sur quelle surface est appliquée la force, et avec quelle valeur ?
> 3. Quel matériau, et quel Re, as-tu saisis ?
> 4. Le maximum se stabilise-t-il quand on affine le maillage ?
> 5. Sur quelle révision de la maquette as-tu fait le calcul ?

### 6. La chaîne numérique et le PDM

[[FIG:pdm_versions]]

La **chaîne numérique**, c'est l'enchaînement des étapes qui partent toutes du **même modèle 3D** : maquette
numérique → simulation → prototype → outillage → production → qualification (contrôle), avec une **boucle
d'optimisation** (ce qu'on apprend en simulation ou à l'essai revient modifier la maquette). Voir aussi la figure
de la fiche 12.4 :

[[FIG:chaine_numerique]]

Pour que tout le monde travaille sur la bonne version, les données sont gérées dans un **PDM** (*Product Data
Management*). Un **PLM** (*Product Lifecycle Management*) étend cette gestion à tout le cycle de vie du produit,
jusqu'à la maintenance et la fin de vie. Le PDM assure, selon le programme :
- les **livrables** : les fichiers exigés par le cahier des charges (modèles, plans, notes de calcul) ;
- les **plannings** (diagramme de **Gantt**) : les tâches du projet et leurs échéances, reliées aux livrables ;
- le **suivi et l'archivage** : chaque document a des **révisions** et un **historique**. L'**indice de
  révision**, c'est la lettre (A, B, C…) que tu vois dans le cartouche de tes plans ;
- le **processus de validation** : un document passe par « en cours → en validation → validé » ; un document
  validé n'est plus modifié — on crée une **nouvelle révision**, et l'ancienne reste lisible ;
- les **droits des intervenants** : qui peut lire, modifier, valider. Un document « réservé » par une personne ne
  peut pas être modifié en même temps par une autre — comme un livre emprunté à la bibliothèque ;
- les **liens entre données** : dans SolidWorks, l'assemblage du support appelle les fichiers de ses pièces
  (équerre, plat, vis). Si quelqu'un remplace le fichier de l'équerre sans le dire, l'assemblage change sans que
  personne ne le voie. Dans le PDM, la nomenclature du support indique « équerre, révision C » : si l'équerre passe
  en D, le PDM signale qu'il faut mettre l'assemblage à jour ;
- l'**import/export** : passer d'un logiciel à un autre par un format neutre — **STEP** (norme ISO 10303) pour
  la 3D, STL pour l'impression (fiches 12.4 et 13.7) — en surveillant la **précision** : un STL, c'est le cercle
  dessiné avec des segments du § 2, une surface approchée par de petits triangles plats.

**Une semaine dans le PDM.**
- Lundi, le dessinateur **réserve** le plan de l'équerre et crée la **révision C** (« en cours ») pour ajouter un
  congé. Personne d'autre ne peut la modifier.
- Mardi, le calculateur ouvre la C **en lecture** et relance le calcul.
- Mercredi, le responsable **valide** la C. La B passe en « archivée », toujours lisible.
- Jeudi, l'atelier, qui ne voit que les versions validées, reçoit la C.

*Pourquoi c'est vital : une simulation faite sur la révision B d'une pièce ne vaut rien si l'atelier fabrique la
révision C. Le PDM dit qui a modifié quoi, quand, et quelle version est en vigueur.*

### 7. Les erreurs classiques

1. **Faire une confiance aveugle au calcul** : une belle image n'est pas une preuve ; on vérifie par un ordre de
   grandeur à la main.
2. **Prendre une singularité pour la contrainte de la pièce** : un pic ponctuel sur un angle vif, qui grimpe
   quand on affine le maillage, n'est pas physique.
3. **Négliger une vraie concentration** au prétexte que « c'est peut-être une singularité » : si la valeur se
   stabilise au congé, elle est réelle (fiches 4.1 et 3.5).
4. **Lire les couleurs sans lire l'échelle** : le rouge n'a pas de valeur fixe.
5. **Bloquer trop de choses** dans les conditions aux limites : modèle trop raide, flèche sous-estimée,
   contraintes mal placées.
6. **Comparer Von Mises à Rm** au lieu de Re (ou de Re / s) : on vérifie que la pièce reste élastique.
7. **Garder la valeur la plus flatteuse** quand la main et la simulation divergent : on retient la plus
   défavorable tant que l'écart n'est pas expliqué.
8. **Modifier un plan validé** au lieu de créer une nouvelle révision dans le PDM.

### 8. À retenir

- Simulation par éléments finis : **maillage** (donné au BTS), **conditions aux limites**, résultats en
  **cartographies** (Von Mises, déplacements).
- Lecture : échelle → maximum → crédible ? → **s obtenu = Re / σ éq ≥ s exigé**.
- **Toujours** recouper par un calcul à la main ; si la simulation trouve nettement moins, chercher l'erreur.
- **Pic qui grimpe, pic qui trompe ; pic qui se pose, pic qui compte** : singularité à un angle vif → pas
  physique (mais le coin reste à risque) ; congé qui converge → réel (Kt, fatigue).
- **PDM** : livrables, Gantt, révisions, historique, validation, droits ; format neutre **STEP** (ISO 10303).
""",
    "formules": """
**Condition de résistance** (fiche 12.2) — σ éq (Von Mises) ≤ Rpe = Re / s · s obtenu = Re / σ éq ≥ s exigé

**Ordre de grandeur à la main** (fiche 4.3) — plat encastré, section b × h (h dans le sens de la force) :
M = F × L · I/v = b h² / 6 · σ = M / (I/v) · flèche au bout f = F L³ / (3 E I), I = b h³ / 12

**Concentration réelle** (fiches 4.1 et 3.5) — σ maxi = Kt × σ nominale

**Lire une carte** — échelle → maximum et zone critique → singularité ou vraie concentration ? → s obtenu

**Singularité** — pic ponctuel (angle vif, force ou fixation ponctuelle, bord de zone bloquée) qui augmente à
chaque raffinement · **Convergence** — la valeur se stabilise quand on raffine

**Main contre simulation** — la simulation trouve un peu plus près d'un congé (Kt) : normal ; nettement moins :
erreur à chercher ; tant que ce n'est pas expliqué, valeur la plus défavorable

**PDM** — livrables · Gantt · révision (A, B, C…) · historique · en cours → en validation → validé · droits
(lire / modifier / valider) · format neutre STEP (ISO 10303)
""",
    "exemple": """
### Cas industriel — Valider une équerre avant de la fabriquer

**La situation.** Une équerre de fixation en S235 (Re = 235 MPa) est modélisée et calculée par le calculateur
de l'entreprise. Son aile, de section 30 × 8 mm, se comporte comme un plat encastré dans la jambe et reçoit
F = 500 N à 100 mm de l'angle (les mêmes valeurs qu'au § 4). Le cahier des charges impose **s ≥ 1,5** (donnée
d'énoncé). Le technicien reçoit la note de calcul et doit dire si la pièce peut partir en fabrication.

**Ce que montre la note (résultats fournis).**
- Carte de Von Mises : environ **150 MPa** dans la section de l'angle, sur les faces haute et basse de l'aile ; un
  **pic rouge de 380 MPa** exactement dans l'angle intérieur, dessiné **vif** sur la maquette.
- Calcul relancé avec un maillage deux fois plus fin : le pic passe à **520 MPa**.

**La lecture critique.**
1. **Ordre de grandeur** : à la main, σ ≈ 156 MPa dans la section de l'angle — cohérent avec les 150 MPa de la
   carte. Le modèle est crédible.
2. **Le pic de 380 MPa** est ponctuel, sur un angle vif, et grimpe à 520 MPa quand on affine : c'est une
   **singularité**, pas la contrainte réelle. On ne conclut pas « la pièce casse », mais on ne l'ignore pas non
   plus : la vraie pièce aura un rayon, qu'il faut **dessiner** et calculer.
3. **Le congé est ajouté** sur la maquette (nouvelle **révision** dans le PDM) et le calcul relancé : sur les
   derniers maillages, **170, 174, 175 MPa** — la valeur **converge**. C'est une vraie concentration de
   contrainte, un peu au-dessus des 156 MPa nominaux, comme attendu (Kt).
4. **Conclusion** : s obtenu = 235 / 175 ≈ **1,34**, inférieur au s exigé de 1,5. **Refusé en l'état** : le
   technicien demande d'augmenter l'épaisseur ou le rayon du congé, puis un nouveau calcul. Ce pic au congé est
   aussi l'endroit où démarrerait une fissure de fatigue si la charge est répétée (fiche 3.5).

**Ce que le cas apprend.** La simulation n'a pas « donné la réponse » : c'est la **lecture critique** — ordre de
grandeur, singularité, convergence, coefficient de sécurité — qui a permis de décider. Et c'est le PDM qui
garantit que l'atelier fabriquera bien la révision avec le congé.
""",
    "exercice": """
### Exercice — Lire et critiquer une note de calcul

Un plat en **S355** (Re = 355 MPa), de section **40 × 10 mm** (épaisseur 10 mm dans le sens de la force), est
encastré et reçoit une force **F = 1 200 N** à **150 mm** de l'encastrement. Le s exigé est **s ≥ 2** (données
d'énoncé). La simulation fournie affiche environ **165 MPa** sur la face supérieure, **dans la section
d'encastrement**, à quelques millimètres de l'angle vif ; et un pic de **610 MPa** dans l'angle vif lui-même, qui
passe à **830 MPa** avec un maillage plus fin.

**1.** Calcule à la main la contrainte de flexion dans la section d'encastrement.

**2.** La simulation est-elle cohérente avec ce calcul ? Que faut-il faire de l'écart ?

**3.** Que penser du pic de 610 MPa ? Justifie avec deux indices.

**4.** Entre la valeur de la simulation (165 MPa) et ton calcul à la main, laquelle retiens-tu pour conclure, et
pourquoi ? Calcule le coefficient de sécurité correspondant et dis si la pièce peut partir en fabrication.

**5.** Le dessinateur modifie la pièce et crée la révision C du plan. Pourquoi ne modifie-t-il pas directement la
révision B, déjà validée ?
""",
    "corrige": """
### Corrigé, en six temps

#### 1. Ce que dit l'énoncé

Plat S355 (Re = 355 MPa), section 40 × 10 mm, F = 1 200 N à L = 150 mm, s exigé ≥ 2. Simulation : ≈ 165 MPa dans
la section d'encastrement ; pic de 610 puis 830 MPa à l'angle vif.

#### 2. Quelle règle, et pourquoi

> σ = M / (I/v), avec M = F × L et I/v = b h² / 6 ; s obtenu = Re / σ éq ≥ s exigé ;
> une singularité est un pic ponctuel, sur un angle vif, qui grimpe quand on affine le maillage ;
> si la simulation trouve nettement moins que la main dans la section la plus chargée, on cherche l'erreur et,
> tant qu'elle n'est pas expliquée, on retient la valeur la plus défavorable.

#### 3. Les conversions

Tout en N et mm : les contraintes sortent en N/mm² = MPa.

#### 4. Le remplacement

M = 1 200 × 150 = 180 000 N·mm ; I/v = 40 × 10² / 6 = 4 000 / 6 ≈ 666,7 mm³.

#### 5. Le calcul (et la lecture)

**1.** σ = 180 000 / 666,7 ≈ **270 MPa**.

**2.** **Non.** Dans la section d'encastrement, la simulation devrait trouver au moins la valeur nominale (un peu
plus près de l'angle) ; elle trouve 165 MPa, près de 40 % de moins. C'est un écart important : il faut
l'**expliquer** avant de conclure. Pistes à vérifier avec le calculateur : une zone bloquée qui déborde au-delà
du vrai encastrement (elle raccourcit le bras de levier, donc le moment), une force mal placée ou mal saisie, une
erreur d'unité.

**3.** C'est une **singularité** : le pic est **ponctuel, sur un angle vif**, et il **grimpe** (610 → 830 MPa)
quand on affine le maillage au lieu de se stabiliser. Ce n'est pas une contrainte physique — mais le coin devra
recevoir un congé sur la vraie pièce, car c'est une zone à risque en fatigue.

**4.** On retient **270 MPa**, la valeur la plus défavorable, tant que l'écart n'est pas expliqué : le calcul à la
main repose sur trois données que l'on peut vérifier ligne par ligne, alors que le modèle contient des dizaines de
réglages qu'on ne voit pas sur l'image. s obtenu = 355 / 270 ≈ **1,31** < 2 : **refusé en l'état**. Le technicien
renvoie la note au calculateur avec deux demandes : vérifier les conditions aux limites, puis proposer une
modification (épaisseur, congé) avec un nouveau calcul. *Avec les 165 MPa de la simulation, on aurait trouvé
s ≈ 2,15 et accepté la pièce à tort : c'est exactement le piège de la confiance aveugle.*

**5.** Parce qu'un document **validé** ne se modifie plus : on crée une **nouvelle révision** (C) qui suit à son
tour le circuit de validation, et la révision B reste **lisible et archivée** — on sait ce qui a été fabriqué ou
calculé avec B, et qui a changé quoi.

#### 6. La vérification

**Unités** : N·mm / mm³ = N/mm² = MPa. **Ordre de grandeur** : 270 MPa reste sous Re = 355 MPa, la pièce ne
plastifie pas, mais la marge exigée (s ≥ 2) n'est pas atteinte.
""",
}
