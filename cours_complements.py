# -*- coding: utf-8 -*-
"""
cours_complements.py — Matières et modules qui ne figuraient pas dans le
programme initial de l'application.

Ces blocs viennent APRÈS les six blocs de conception. Ils suivent exactement le
même format, donc l'application les affiche sans aucune modification.

Contenu :
    Bloc 7  — Mathématiques appliquées
    Bloc 8  — Physique appliquée
    Bloc 9  — Méthodologie de projet et SolidWorks guidé
    Bloc 10 — Anglais technique et économie-gestion
    Bloc 11 — Ce qui attend en deuxième année

Pour retirer un bloc : le supprimer de la liste BLOCS_COMPLEMENTAIRES en bas.
"""

BLOC_7 = {
    "id": 7,
    "titre": "Bloc 7 — Mathématiques appliquées",
    "resume": "Les seuls outils mathématiques réellement utilisés en conception mécanique.",
    "fiches": [
        {
            "id": "7.1",
            "titre": "Trigonométrie, vecteurs et géométrie du dessin",
            "duree": "8 h",
            "cours": """
### 1. À quoi ça sert vraiment

En conception, on ne fait pas des maths pour faire des maths. On en fait quand :

- une pièce est inclinée et qu'il faut calculer une longueur ou une hauteur ;
- une force ne tire pas droit et qu'il faut la décomposer ;
- il faut trouver un entraxe, un angle de dépouille, la longueur développée d'une tôle pliée.

Trois outils suffisent pour tout ça : la trigonométrie, les vecteurs, et le théorème de
Pythagore. Ce sont les mêmes qu'au lycée — mais appliqués à des pièces réelles.

### 2. La trigonométrie, en trois formules

Dans un triangle **rectangle**, pour un angle α :

| Formule | Mémo |
|---|---|
| **sin α = opposé / hypoténuse** | **SOH** |
| **cos α = adjacent / hypoténuse** | **CAH** |
| **tan α = opposé / adjacent** | **TOA** |

Et le théorème de Pythagore : **hyp² = opp² + adj²**.

**Exemple d'atelier.** Une nervure de renfort part du bas d'un montant vertical et rejoint un
bras horizontal à 250 mm du coin, avec un angle de 40°. Quelle est sa longueur ?

L'adjacent vaut 250 et on cherche l'hypoténuse : cos 40° = 250 / L, donc
**L = 250 / cos 40° = 326 mm**.

*Réflexe : on écrit d'abord ce qu'on connaît et ce qu'on cherche, puis on choisit la formule qui
relie exactement ces deux-là. Jamais l'inverse.*

### 3. Le piège des degrés et des radians

Votre calculatrice doit être en mode **DEG** pour les angles de plan (40°, 118°, 45°), et en
mode **RAD** quand vous travaillez avec des vitesses de rotation (ω en rad/s).

> **1 tour = 360° = 2π radians**, donc **1 rad ≈ 57,3°**.

Un résultat aberrant (une longueur négative, un angle de 3 000°) vient neuf fois sur dix de ce
réglage.

### 4. Les vecteurs : décomposer une force

[[FIG:decomposer_force]]

Une force qui tire de biais se décompose en deux forces perpendiculaires :

> **Fx = F × cos α**  et  **Fy = F × sin α**

**Exemple.** Une courroie tire sur une poulie avec 800 N, inclinés de 30° par rapport à
l'horizontale.

- Composante horizontale : Fx = 800 × cos 30° = **693 N**
- Composante verticale : Fy = 800 × sin 30° = **400 N**

C'est exactement ce qu'on fait avant tout calcul de RDM : on ramène les efforts obliques à des
efforts perpendiculaires aux pièces.

Et l'opération inverse, tout aussi utile : à partir de Fx et Fy, on retrouve
**F = √(Fx² + Fy²)** et **α = arctan (Fy / Fx)**.

### 5. Proportionnalité et pourcentages : le calcul le plus fréquent de tous

C'est banal, et c'est pourtant ce qu'on utilise le plus :

- **échelle** : à 1:2,5, une pièce de 400 mm est dessinée sur 160 mm ;
- **rapport de transmission** : 20 dents / 60 dents = 1/3 ;
- **retrait de fonderie** de 1 % : un modèle de 300 mm donne une pièce de 297 mm ;
- **rendement** : 4 kW en entrée, rendement 0,94, donc 3,76 kW en sortie.

### 6. Aires, volumes, masses

À connaître par cœur, parce qu'on les utilise chaque semaine :

| Forme | Aire | Volume |
|---|---|---|
| rectangle b × h | b h | prisme : b h L |
| disque Ø d | π d² / 4 | cylindre : π d² L / 4 |
| couronne (tube) | π (D² − d²) / 4 | tube : π (D² − d²) L / 4 |

**Et la masse : m = V × ρ.** Avec le volume en mm³ et la masse volumique en kg/dm³, pensez à
convertir : **1 dm³ = 1 000 000 mm³**.

*Exemple : un arbre acier Ø40 de 500 mm. V = π × 40² × 500 / 4 = 628 000 mm³ = 0,628 dm³.
m = 0,628 × 7,85 = **4,9 kg**.*

### 7. Les erreurs classiques

1. **Calculatrice en radians** pour un angle en degrés.
2. **Mélanger mm et m** dans une même formule.
3. **Utiliser la trigonométrie dans un triangle non rectangle** — il faut alors la loi des sinus
   ou celle des cosinus.
4. **Confondre diamètre et rayon** dans π d² / 4.
5. **Oublier de vérifier l'ordre de grandeur** : un arbre de 4,9 kg, c'est plausible ; 4 900 kg
   ne l'est pas.
""",
            "formules": """
**Trigonométrie** — sin α = opp/hyp · cos α = adj/hyp · tan α = opp/adj · hyp² = opp² + adj²

**Vecteurs** — Fx = F cos α · Fy = F sin α · F = √(Fx² + Fy²) · α = arctan(Fy/Fx)

**Angles** — 1 tour = 360° = 2π rad · 1 rad ≈ 57,3°

**Aires et volumes** — disque π d²/4 · couronne π(D²−d²)/4 · cylindre π d² L/4

**Masse** — m = V × ρ · 1 dm³ = 10⁶ mm³ · acier ρ = 7,85 kg/dm³ · alu 2,7 · POM 1,41
""",
            "exercice": """
**1.** Une rampe monte de 300 mm sur une longueur horizontale de 1 200 mm. Quel est son angle ?

**2.** Un effort de 1 500 N est incliné de 25° par rapport à l'axe d'une poutre. Décompose-le.

**3.** Calcule la masse d'une plaque d'aluminium 400 × 250 × 8 mm (ρ = 2,7 kg/dm³).

**4.** Un tube acier Ø extérieur 60, Ø intérieur 50, longueur 2 m. Quelle est sa masse ?

**5.** Une pièce moulée doit mesurer 240 mm après refroidissement. Le retrait de la fonte est de
1 %. Quelle dimension donner au modèle ?
""",
            "corrige": """
**1.** tan α = 300 / 1 200 = 0,25 → **α = arctan 0,25 = 14,0°**.
*Vérification de bon sens : une pente de 25 %, c'est raide mais crédible.*

**2.** Fx = 1 500 × cos 25° = **1 360 N** (le long de la poutre) ·
Fy = 1 500 × sin 25° = **634 N** (perpendiculaire, celle qui fait fléchir).
*C'est la composante perpendiculaire qui compte en flexion : les 634 N, pas les 1 500 N.*

**3.** V = 400 × 250 × 8 = 800 000 mm³ = 0,8 dm³ → m = 0,8 × 2,7 = **2,16 kg**.

**4.** Section = π (60² − 50²) / 4 = π (3 600 − 2 500) / 4 = **864 mm²**.
V = 864 × 2 000 = 1 728 000 mm³ = 1,728 dm³ → m = 1,728 × 7,85 = **13,6 kg**.
*Une barre pleine Ø60 de même longueur pèserait 44 kg : le tube est trois fois plus léger, pour
une résistance en flexion à peine inférieure.*

**5.** Le modèle doit être **plus grand** de 1 % : 240 × 1,01 = **242,4 mm**.
*Erreur classique : retrancher 1 % au lieu de l'ajouter. La pièce rétrécit en refroidissant,
donc le moule doit être plus grand.*
""",
            "exemple": """
**Cas industriel — Calculer la longueur développée d'une tôle pliée**

Une équerre en tôle de 3 mm : une aile de 80 mm, une aile de 50 mm, pli à 90°, rayon intérieur
de pliage 3 mm.

**Le problème.** Si on découpe une bande de 80 + 50 = 130 mm et qu'on la plie, on n'obtient pas
80 et 50 : la matière s'étire à l'extérieur du pli et se comprime à l'intérieur. La longueur
développée est **plus courte** que la somme des cotes.

**Le calcul.** On utilise la fibre neutre, située à environ 0,4 × épaisseur depuis l'intérieur
du pli (coefficient K = 0,4 pour l'acier doux) :

- rayon de la fibre neutre : r = 3 + 0,4 × 3 = **4,2 mm**
- longueur de l'arc à 90° : L_arc = 2π × 4,2 / 4 = **6,6 mm**
- longueurs droites : (80 − 3 − 3) + (50 − 3 − 3) = 74 + 44 = **118 mm**
- **développé total = 118 + 6,6 = 124,6 mm**

**Ce qu'il faut retenir.** On perd 5,4 mm par rapport à la somme naïve. Sur une pièce à quatre
plis, l'erreur atteindrait 2 cm : la pièce serait bonne à jeter.

En pratique, le logiciel de CAO calcule le développé automatiquement dès qu'on lui donne
l'épaisseur, le rayon et le coefficient K. Mais il faut savoir d'où vient le chiffre — et
vérifier que le coefficient correspond bien à la matière utilisée.
""",
        },
        {
            "id": "7.2",
            "titre": "Fonctions, dérivées et intégrales appliquées",
            "duree": "8 h",
            "cours": """
### 1. Pourquoi un mécanicien a besoin de dérivées

Parce que trois grandeurs qu'il manipule tous les jours sont liées par une dérivation :

> **position → (dériver) → vitesse → (dériver) → accélération**

Et dans l'autre sens, par une intégration : si vous connaissez l'accélération, vous remontez à
la vitesse, puis à la position.

C'est exactement ce qui se passe quand un vérin sort, quand un chariot démarre, quand une came
soulève un poussoir. Pas de dérivées, pas de calcul de came ni de profil de vitesse.

### 2. Lire une fonction avant de la calculer

Avant toute chose, sachez lire un graphe :

- **la pente** d'une courbe, c'est la dérivée. Pente forte = variation rapide.
- **l'aire sous la courbe**, c'est l'intégrale. Sous une courbe de vitesse, l'aire donne la
  distance parcourue.
- **un maximum ou un minimum** se trouve là où la dérivée s'annule.

Ce dernier point est capital en conception : chercher l'épaisseur qui minimise la masse, ou la
position où le moment fléchissant est maximal, c'est chercher **où la dérivée s'annule**.

### 3. Les dérivées à connaître

| Fonction | Dérivée |
|---|---|
| k (constante) | 0 |
| x | 1 |
| x² | 2x |
| xⁿ | n xⁿ⁻¹ |
| sin x | cos x |
| cos x | − sin x |
| k × f(x) | k × f'(x) |

Et deux règles : la dérivée d'une somme est la somme des dérivées ; pour un produit,
(uv)' = u'v + uv'.

### 4. Une application concrète : où le moment est-il maximal ?

Une poutre sur deux appuis de longueur L, chargée uniformément par q (N/mm). Le moment
fléchissant en un point x vaut :

> Mf(x) = (q L x / 2) − (q x² / 2)

Où est-il maximal ? Là où sa dérivée s'annule :

> Mf'(x) = qL/2 − qx = 0 → **x = L/2**

Le moment est donc maximal **au milieu** de la poutre, et vaut Mf = q L² / 8. C'est exactement
la formule du tableau de la fiche 4.3 — sauf qu'ici, vous savez d'où elle vient.

### 5. L'intégrale : cumuler

Intégrer, c'est additionner une infinité de petites contributions. Deux usages courants :

- **une vitesse intégrée donne une distance** : un chariot qui accélère de 0 à 0,5 m/s en 2 s
  parcourt l'aire du triangle, soit 0,5 × 2 / 2 = **0,5 m** ;
- **une aire intégrée donne un volume** : c'est ainsi que le logiciel de CAO calcule le volume
  d'une pièce de forme quelconque, puis sa masse et son centre de gravité.

Les primitives à connaître : celle de xⁿ est xⁿ⁺¹/(n+1), celle de cos x est sin x, celle de
sin x est −cos x.

### 6. Le profil de vitesse trapézoïdal

[[FIG:profil_trapezoidal]]

C'est l'application la plus utile de toute la fiche. Un axe motorisé ne démarre jamais
brutalement : il accélère, tient une vitesse constante, puis décélère. Le graphe de vitesse
forme un trapèze.

- **La pente** des rampes, c'est l'**accélération** (m/s²).
- **L'aire du trapèze**, c'est la **distance** parcourue.

Et l'accélération donne directement l'effort à fournir par le moteur : **F = m × a**, à ajouter
aux frottements et à la charge utile. C'est ainsi qu'on dimensionne un moteur d'axe.

### 7. Les erreurs classiques

1. **Dériver sans vérifier les unités** : une vitesse en mm/s dérivée donne des mm/s².
2. **Confondre la valeur d'une fonction et sa pente** : à la crête d'une courbe, la valeur est
   maximale et la pente est nulle.
3. **Oublier la constante** lors d'une intégration (la position initiale, la vitesse initiale).
4. **Chercher un maximum sans vérifier les bornes** : parfois, le maximum est à l'extrémité de
   l'intervalle, là où la dérivée ne s'annule pas.
""",
            "formules": """
**Cinématique** — v = dx/dt · a = dv/dt · x = ∫v dt · v = ∫a dt

**Mouvement uniformément accéléré** — v = v₀ + a t · x = x₀ + v₀ t + ½ a t²

**Dérivées** — (xⁿ)' = n xⁿ⁻¹ · (sin x)' = cos x · (cos x)' = −sin x

**Primitives** — ∫xⁿ dx = xⁿ⁺¹/(n+1) · ∫cos x dx = sin x · ∫sin x dx = −cos x

**Extremum** — maximum ou minimum là où f'(x) = 0

**Effort d'accélération** — F = m a (à ajouter aux frottements et à la charge)
""",
            "exercice": """
**1.** Un chariot part de l'arrêt et atteint 0,8 m/s en 1,5 s, avec une accélération constante.
Calcule l'accélération, puis la distance parcourue pendant cette phase.

**2.** Le chariot pèse 120 kg. Quel effort supplémentaire le moteur doit-il fournir pendant
l'accélération (frottements négligés) ?

**3.** Dérive la fonction Mf(x) = 500x − 2x² et trouve la valeur de x qui rend Mf maximal.

**4.** Quelle est la valeur de ce maximum ?

**5.** Un vérin sort de 200 mm en 1,2 s selon un profil trapézoïdal : 0,3 s d'accélération,
0,6 s à vitesse constante, 0,3 s de décélération. Quelle est la vitesse du palier constant ?
""",
            "corrige": """
**1.** a = Δv / Δt = 0,8 / 1,5 = **0,53 m/s²**.
Distance : x = ½ a t² = 0,5 × 0,53 × 1,5² = **0,60 m**.
*Vérification par l'aire du triangle : 0,8 × 1,5 / 2 = 0,6 m. Les deux méthodes concordent.*

**2.** F = m a = 120 × 0,53 = **64 N**.
*C'est l'effort d'accélération seul. En réalité, il faut y ajouter les frottements et, si le
chariot monte, la composante du poids.*

**3.** Mf'(x) = 500 − 4x. Elle s'annule pour **x = 125**.

**4.** Mf(125) = 500 × 125 − 2 × 125² = 62 500 − 31 250 = **31 250 N·mm**.
*La dérivée donne l'endroit du maximum ; il faut ensuite réinjecter cette valeur dans la fonction
d'origine pour connaître le maximum lui-même. Les deux étapes sont souvent confondues.*

**5.** L'aire du trapèze vaut la distance : 200 mm.
Aire = v × (durée totale + durée du palier) / 2 = v × (1,2 + 0,6) / 2 = 0,9 v
Donc v = 200 / 0,9 = **222 mm/s**, soit 0,22 m/s.
*Piège classique : diviser bêtement 200 par 1,2 donnerait 167 mm/s — la vitesse moyenne, pas la
vitesse du palier. Le moteur doit être dimensionné sur la vitesse maximale.*
""",
            "exemple": """
**Cas industriel — Dimensionner le moteur d'un axe linéaire**

Un axe motorisé déplace un plateau de **80 kg** sur **500 mm**, en **1,5 s** maximum, cycle
répété toutes les 6 secondes. Entraînement par vis à billes, rendement 0,9.

**ÉTAPE 1 — Choisir un profil de mouvement**

On retient un profil trapézoïdal en tiers : 0,5 s d'accélération, 0,5 s à vitesse constante,
0,5 s de décélération.

**ÉTAPE 2 — Vitesse du palier**

Aire du trapèze = 0,5 m : v × (1,5 + 0,5) / 2 = 0,5 → **v = 0,5 m/s**

**ÉTAPE 3 — Accélération**

a = v / t = 0,5 / 0,5 = **1 m/s²**

**ÉTAPE 4 — Effort à fournir**

- accélération : F = m a = 80 × 1 = 80 N
- frottements du guidage (coefficient 0,01) : 80 × 9,81 × 0,01 = 8 N
- **total ≈ 88 N** pendant la phase d'accélération

**ÉTAPE 5 — Puissance mécanique**

P = F × v = 88 × 0,5 = 44 W, divisé par le rendement 0,9 → **49 W**

**Ce que le cas apprend.** La puissance nécessaire est faible, mais c'est le **pic
d'accélération** qui dimensionne le moteur, pas la vitesse de croisière. Et si l'on divisait le
temps de montée en vitesse par deux, l'accélération — donc l'effort — doublerait.

C'est pour cette raison qu'en automatisme on cherche toujours à **allonger les rampes** autant
que le temps de cycle le permet : le moteur, la vis et les guidages en sortent moins chargés,
donc moins chers.
""",
        },
        {
            "id": "7.3",
            "titre": "Statistiques appliquées à la qualité",
            "duree": "6 h",
            "cours": """
### 1. Le lien direct avec la cotation

Vous avez appris qu'aucune pièce n'est exacte, et qu'on donne donc une fourchette. Mais comment
sait-on qu'un atelier est **capable** de tenir cette fourchette ? Et comment décide-t-on de la
tolérance à partir de ce que la machine sait faire ?

C'est le rôle des statistiques industrielles — la matière qui relie le bureau d'études à la
production.

### 2. Décrire un lot de pièces avec deux nombres

On mesure 50 pièces. Deux indicateurs suffisent pour tout dire :

- **la moyenne x̄** : le centre de la production. Si elle est décalée par rapport à la cote
  visée, la machine est **déréglée** — c'est facile à corriger.
- **l'écart-type σ** : la dispersion autour de cette moyenne. Il traduit la **capacité** de la
  machine. On ne le corrige pas par un réglage : il faut changer de moyen ou de méthode.

*Un décalage de moyenne se rattrape en tournant une manivelle. Une dispersion trop forte, non.
C'est toute la différence entre les deux.*

### 3. La courbe en cloche

Les mesures d'une production stable se répartissent selon une **loi normale**, la fameuse courbe
en cloche. Trois chiffres à retenir, et ils reviennent partout :

| Intervalle | Part de la production |
|---|---|
| x̄ ± 1 σ | 68 % |
| x̄ ± 2 σ | 95 % |
| **x̄ ± 3 σ** | **99,73 %** |

C'est de là que vient la règle des **6 sigma** : la production réelle occupe une largeur
d'environ 6σ. Pour qu'un atelier tienne une tolérance, il faut donc que **IT soit au moins égal
à 6σ**.

### 4. Les indicateurs de capabilité : Cp et Cpk

[[FIG:courbe_capabilite]]

**Cp** compare la largeur de la tolérance à celle de la production :

> **Cp = IT / (6 σ)**

- Cp < 1 : la machine produit plus large que la tolérance → **rebuts garantis**
- Cp = 1 : tout juste, sans marge
- **Cp ≥ 1,33** : c'est l'exigence usuelle en industrie

Mais Cp ne dit rien sur le **centrage**. Une production bien serrée mais décalée sur un bord
produira quand même des rebuts. D'où **Cpk**, qui tient compte du décalage :

> **Cpk = min(x̄ − cote mini, cote maxi − x̄) / (3 σ)**

- **Cp élevé et Cpk faible** → la machine est capable mais **déréglée** : on recentre.
- **Cp faible** → la machine n'est pas capable : changer de moyen, d'outil ou de méthode.

### 5. La carte de contrôle

Plutôt que de mesurer toutes les pièces, on prélève régulièrement un petit échantillon et on
reporte la moyenne sur un graphe muni de limites. Tant que les points restent entre les limites
et sans tendance, on ne touche à rien.

Les signaux d'alerte : un point hors limites, sept points consécutifs du même côté de la
moyenne, ou une dérive régulière — typiquement une **usure d'outil**.

Le principe est aussi ce qui distingue le contrôle moderne du tri : on **surveille le procédé**
au lieu de trier les pièces après coup.

### 6. Ce que ça change pour le concepteur

Voilà le point à retenir, celui qui vous servira en projet :

> **Une tolérance ne se choisit pas seulement en fonction de la fonction, mais aussi en fonction
> de ce que l'atelier sait tenir.**

Demander un IT de 0,02 mm à un atelier dont la dispersion réelle est de 0,05 mm, c'est
programmer des rebuts, des litiges et des retards. Un bon bureau d'études connaît les capabilités
de ses ateliers et de ses fournisseurs, et cote en conséquence.

### 7. Les erreurs classiques

1. **Confondre moyenne décalée et dispersion excessive** — les remèdes n'ont rien à voir.
2. **Se contenter du Cp** sans regarder le Cpk.
3. **Réagir à chaque point** d'une carte de contrôle : sur-régler une machine augmente sa
   dispersion.
4. **Coter sans se demander qui va fabriquer.**
""",
            "formules": """
**Moyenne** — x̄ = Σxᵢ / n

**Écart-type** — σ = √( Σ(xᵢ − x̄)² / (n−1) )

**Loi normale** — ±1σ : 68 % · ±2σ : 95 % · **±3σ : 99,73 %**

**Capabilité** — Cp = IT / (6σ) · Cpk = min(x̄ − Tmin ; Tmax − x̄) / (3σ)

**Seuils usuels** — Cp et Cpk ≥ 1,33 exigés · < 1 : rebuts certains

**Règle de conception** — IT ≥ 6σ de l'atelier
""",
            "exercice": """
Une cote est spécifiée **30 ± 0,15**. Un atelier produit avec une moyenne x̄ = 30,00 et un
écart-type σ = 0,04.

**1.** Quel est l'IT de cette cote ?

**2.** Calcule le Cp. L'atelier est-il capable ?

**3.** Calcule le Cpk. Que constate-t-on ?

**4.** La machine se dérègle : la moyenne passe à 30,08, l'écart-type ne change pas. Recalcule
Cp et Cpk. Que s'est-il passé, et que faut-il faire ?

**5.** Un second atelier propose de fabriquer la même pièce, avec σ = 0,07 et une moyenne
parfaitement centrée. Est-il acceptable ?
""",
            "corrige": """
**1.** IT = 30,15 − 29,85 = **0,30 mm**.

**2.** Cp = IT / (6σ) = 0,30 / (6 × 0,04) = 0,30 / 0,24 = **1,25**.
C'est supérieur à 1, donc l'atelier produit plus serré que la tolérance — mais **en dessous du
seuil usuel de 1,33**. Capable, mais sans grande marge.

**3.** Production centrée : les deux distances valent 0,15.
Cpk = 0,15 / (3 × 0,04) = 0,15 / 0,12 = **1,25**.
**Cpk = Cp** : c'est la signature d'une production **parfaitement centrée**.

**4.** Après dérèglement, x̄ = 30,08 :
- Cp est **inchangé : 1,25** — la dispersion n'a pas bougé.
- Cpk = min(30,08 − 29,85 ; 30,15 − 30,08) / (3 × 0,04) = min(0,23 ; **0,07**) / 0,12 = **0,58**

Cpk s'est effondré alors que Cp n'a pas bougé : la machine est **toujours aussi précise, mais
déréglée**. Il ne faut surtout pas changer de machine : il faut **recentrer le réglage** sur 30.

*C'est exactement pour repérer ce genre de situation qu'on calcule les deux indicateurs.*

**5.** Cp = 0,30 / (6 × 0,07) = **0,71**, et Cpk = 0,71 aussi puisque c'est centré.

**Inacceptable.** Avec un Cp inférieur à 1, la production est plus large que la tolérance : une
partie des pièces sera hors cote quoi qu'on fasse, même parfaitement centrée. Aucun réglage ne
sauvera ce procédé — il faut un autre moyen de production, ou négocier un élargissement de la
tolérance si la fonction le permet.
""",
            "exemple": """
**Cas industriel — Choisir une tolérance en connaissant l'atelier**

Un bureau d'études doit coter l'alésage d'un support de roulement. La fonction impose au minimum
un **H8**. Sur un Ø50, cela représente un IT de 0,039 mm.

**Les données de l'atelier** (relevées sur les six derniers mois, trois moyens différents) :

| Moyen | Écart-type σ | 6σ | Cp pour IT = 0,039 |
|---|---|---|---|
| tour CN, outil carbure | 0,012 mm | 0,072 | **0,54** → incapable |
| alésoir machine | 0,005 mm | 0,030 | **1,30** → juste acceptable |
| rectifieuse | 0,002 mm | 0,012 | **3,25** → très capable |

**Les décisions possibles**

1. **Tour seul** : rebuts massifs. Écarté.
2. **Tour + alésoir** : Cp = 1,30, tout juste sous le seuil de 1,33 habituellement exigé. Ça
   passe si le centrage est bien maîtrisé, à surveiller par carte de contrôle.
3. **Tour + rectification** : très confortable, mais une opération de plus, un temps machine plus
   long, et environ 40 % de coût en plus sur la pièce.

**Décision retenue.** Tour + alésoir, avec une carte de contrôle sur les vingt premières pièces
de chaque série. Si le Cpk mesuré descend sous 1,33, on passe en rectification.

**Ce que le cas apprend.** La tolérance du bureau d'études et la capabilité de l'atelier ne sont
pas deux mondes séparés. Un concepteur qui ignore ce que ses ateliers savent tenir produit des
plans irréalisables — ou fait payer une rectification inutile.
""",
        },
    ],
}


BLOC_8 = {
    "id": 8,
    "titre": "Bloc 8 — Physique appliquée",
    "resume": "Mécanique, énergie et électricité : ce qu'un concepteur doit savoir pour dialoguer avec les autres métiers.",
    "fiches": [
        {
            "id": "8.1",
            "titre": "Cinématique et dynamique des mécanismes",
            "duree": "8 h",
            "cours": """
### 1. Deux questions différentes

- **Cinématique** : *comment ça bouge ?* Vitesses, trajectoires, accélérations — sans se demander
  pourquoi.
- **Dynamique** : *quels efforts faut-il pour que ça bouge ainsi ?* C'est là qu'interviennent les
  masses et les moteurs.

On fait toujours la cinématique en premier : elle donne les vitesses, dont la dynamique a besoin.

### 2. Le mouvement de rotation

[[FIG:quatre_sollicitations]]

C'est le plus courant en mécanique. Trois grandeurs, et les conversions qui vont avec :

| Grandeur | Symbole | Unité | Conversion |
|---|---|---|---|
| fréquence de rotation | N | tr/min | ce que dit la plaque du moteur |
| vitesse angulaire | ω | rad/s | **ω = 2π N / 60** |
| vitesse d'un point | v | m/s | **v = ω × R** (R en mètres) |

**Exemple.** Une meule Ø300 tourne à 2 800 tr/min. Quelle est la vitesse en périphérie ?

ω = 2π × 2 800 / 60 = 293 rad/s, et v = 293 × 0,15 = **44 m/s**.

*C'est cette vitesse périphérique qui est limitée par les fabricants de meules — pas la
fréquence de rotation. Une meule usée, plus petite, tourne donc moins vite en périphérie : c'est
pourquoi on peut augmenter N quand le diamètre diminue.*

### 3. Le principe fondamental de la dynamique

En translation : **F = m × a** (newton, kilogramme, mètre par seconde carrée).

En rotation, l'équivalent : **C = J × α**, où J est le moment d'inertie (kg·m²) et α
l'accélération angulaire (rad/s²).

Le moment d'inertie joue en rotation le rôle que la masse joue en translation. Et il dépend
fortement du **rayon** : pour un cylindre plein, J = m R² / 2. Doubler le rayon multiplie J
par 4, à masse égale.

*Conséquence de conception : pour qu'une machine accélère vite, on ne cherche pas seulement à
alléger les pièces tournantes — on cherche à rapprocher leur masse de l'axe.*

### 4. Le poids n'est pas la masse

Une confusion permanente, et une source d'erreurs de calcul :

> **La masse m est en kilogrammes. Le poids P est une force, en newtons : P = m × g**, avec
> g = 9,81 m/s².

Une charge de 200 kg exerce un poids de **1 962 N**, soit environ 2 000 N. Dans toutes vos
formules de RDM, ce sont des newtons qu'il faut mettre, jamais des kilogrammes.

### 5. Énergie, travail, puissance

| Grandeur | Formule | Unité |
|---|---|---|
| travail d'une force | W = F × d | joule (J) |
| énergie cinétique | Ec = ½ m v² | joule |
| énergie potentielle | Ep = m g h | joule |
| **puissance** | **P = W / t = F × v** | watt (W) |
| puissance en rotation | **P = C × ω** | watt |

**Le principe de conservation** : l'énergie ne se crée pas, elle se transforme et se dégrade.
Un moteur de 4 kW ne fournira jamais 5 kW en sortie de réducteur ; il en fournira 3,8 environ,
le reste partant en chaleur.

### 6. Rendement : pourquoi il faut toujours le prévoir

> **η = puissance utile / puissance absorbée**

Ordres de grandeur : engrenage 0,97 par étage · courroie 0,95 · chaîne 0,96 · vis à billes 0,90 ·
roue et vis sans fin 0,5 à 0,8 · moteur électrique 0,85 à 0,92.

Les rendements se **multiplient** en cascade. Un moteur (0,9) entraînant un réducteur à deux
étages (0,97 × 0,97) puis une courroie (0,95) donne un rendement global de
0,9 × 0,94 × 0,95 = **0,80**. Il faut donc absorber 25 % de plus que ce qu'on veut délivrer.

### 7. Les erreurs classiques

1. **Mettre des kilogrammes** dans une formule qui attend des newtons.
2. **Confondre N (tr/min) et ω (rad/s)** — facteur 9,55 d'écart.
3. **Oublier les rendements**, et sous-dimensionner le moteur.
4. **Ignorer l'inertie** dans un mouvement qui démarre et s'arrête souvent : le couple
   d'accélération peut dépasser largement le couple utile.
""",
            "formules": """
**Rotation** — ω = 2π N / 60 · v = ω R · N en tr/min, ω en rad/s, R en m

**Dynamique** — F = m a · C = J α · P = m g (g = 9,81 m/s²)

**Inertie** — cylindre plein : J = m R² / 2 · cylindre creux : J = m (R₁² + R₂²) / 2

**Énergie** — W = F d · Ec = ½ m v² · Ep = m g h

**Puissance** — P = F v (translation) · P = C ω (rotation) · 1 kW = 1 000 W

**Rendement** — η = P utile / P absorbée · les rendements se multiplient en cascade
""",
            "exercice": """
**1.** Un tambour de convoyeur Ø400 tourne à 60 tr/min. Quelle est la vitesse linéaire de la
bande, en m/s puis en m/min ?

**2.** La bande transporte 350 kg. Quel est le poids de cette charge, en newtons ?

**3.** Le convoyeur monte de 3 m sur sa longueur. Quelle énergie faut-il pour monter cette charge ?

**4.** Si la montée se fait en 25 s, quelle puissance utile faut-il ?

**5.** La transmission comporte un motoréducteur (η = 0,75) et une chaîne (η = 0,96). Quelle
puissance le moteur doit-il absorber ?
""",
            "corrige": """
**1.** ω = 2π × 60 / 60 = **6,28 rad/s**
v = ω × R = 6,28 × 0,20 = **1,26 m/s**, soit **75 m/min**.
*Attention au rayon : Ø400 donne R = 0,2 m, pas 0,4.*

**2.** P = m g = 350 × 9,81 = **3 434 N**, soit environ 3,4 kN.

**3.** W = P × h = 3 434 × 3 = **10 302 J**, soit environ 10,3 kJ.

**4.** Puissance utile = W / t = 10 302 / 25 = **412 W**.
*Autre méthode, qui donne le même résultat : P = F × v vertical. La charge monte de 3 m en 25 s,
soit 0,12 m/s → 3 434 × 0,12 = 412 W.*

**5.** Rendement global = 0,75 × 0,96 = **0,72**
Puissance absorbée = 412 / 0,72 = **572 W**

On choisira donc un moteur normalisé de **0,75 kW**, la taille au-dessus.

*Ce que montre l'exercice : 28 % de la puissance part en pertes. Négliger les rendements, c'est
choisir un moteur de 0,37 kW qui calera en charge.*
""",
            "exemple": """
**Cas industriel — Pourquoi le moteur cale au démarrage**

Un convoyeur fonctionne correctement en régime établi, mais **disjoncte une fois sur trois au
démarrage**, surtout quand il est chargé. Le bureau d'études avait pourtant vérifié la puissance.

**Le calcul d'origine (régime établi)**

- charge : 350 kg, montée de 3 m, vitesse 0,12 m/s vertical
- puissance utile : 412 W, rendement 0,72 → **572 W absorbés**
- moteur choisi : 0,75 kW → correct **en régime établi**

**Ce qui avait été oublié : le démarrage**

Au démarrage, il faut en plus :

1. **accélérer la charge** : 350 kg de 0 à 1,26 m/s en 0,8 s → a = 1,58 m/s²,
   soit F = 350 × 1,58 = **553 N**, à ajouter aux 3 434 N du poids ;
2. **vaincre l'inertie des pièces tournantes** : tambours, réducteur, accouplement ;
3. **décoller le convoyeur** : le frottement statique est supérieur au frottement dynamique.

Le couple demandé au démarrage atteint ainsi **1,8 à 2 fois** le couple nominal — d'où le
déclenchement de la protection.

**Les solutions retenues**

- passer au moteur normalisé supérieur (1,1 kW), le plus simple ;
- ou installer un **variateur de fréquence** avec une rampe d'accélération de 3 s : l'inertie est
  vaincue progressivement, le pic disparaît, et on gagne au passage un démarrage en douceur pour
  la bande et le produit transporté.

**Ce que le cas apprend.** On dimensionne un entraînement sur **deux points de fonctionnement** :
le régime établi et le démarrage. C'est presque toujours le second qui commande le choix du
moteur.
""",
        },
        {
            "id": "8.2",
            "titre": "Énergie, thermique et mécanique des fluides",
            "duree": "7 h",
            "cours": """
### 1. Trois sujets, une seule logique

L'énergie se conserve mais se dégrade — presque toujours en chaleur. Cette phrase résume les
trois sujets de cette fiche : le frottement chauffe, un fluide sous pression pousse, et un carter
mal ventilé accumule ce que le mécanisme dissipe.

### 2. La chaleur : d'où elle vient, où elle va

Dans une machine, la chaleur est le déchet de tous les rendements imparfaits. Un réducteur de
4 kW à rendement 0,94 dissipe 240 W en chaleur — l'équivalent de deux ampoules dans un carter
fermé.

Trois modes de transfert :

- **conduction** : à travers la matière (l'arbre chauffe le roulement) ;
- **convection** : par un fluide en mouvement (l'air autour du carter, l'huile qui circule) ;
- **rayonnement** : à distance, sans support — dominant seulement à haute température.

Deux formules à connaître :

> **Q = m c ΔT** — l'énergie qu'il faut pour élever la température d'une masse
> **Φ = k S ΔT** — le flux thermique évacué par une surface

La conséquence pratique : la chaleur s'évacue **par les surfaces**. Doubler la puissance dissipée
sans augmenter la surface d'échange, c'est doubler l'échauffement. D'où les ailettes des carters
de réducteurs — elles ne sont pas décoratives.

### 3. La dilatation : la cause n° 1 des grippages

[[FIG:isostatique_hyperstatique]]

> **ΔL = L₀ × α × ΔT**

Coefficients à retenir : acier **12 × 10⁻⁶ /°C** · aluminium **23 × 10⁻⁶** · polymères 70 à 150.

**Exemple.** Un arbre acier de 800 mm qui passe de 20 à 70 °C s'allonge de
800 × 12·10⁻⁶ × 50 = **0,48 mm**.

Un demi-millimètre : c'est bien plus que le jeu d'un roulement. Voilà pourquoi un arbre bloqué
axialement aux deux extrémités grippe — et pourquoi l'aluminium, qui se dilate deux fois plus
que l'acier, pose des problèmes de montage mixte.

### 4. Hydraulique et pneumatique : la pression

[[FIG:effort_verin]]

> **p = F / S**, en pascals (1 Pa = 1 N/m²), mais on travaille en **bars** : **1 bar = 10⁵ Pa**.
> Astuce : **1 bar sur 1 cm² donne 10 N**.

**L'effort d'un vérin** est le calcul le plus utile de la fiche :

> **F = p × S**, avec S la section du piston

*Exemple : un vérin pneumatique Ø32 à 6 bars. S = π × 32² / 4 = 804 mm² = 8,04 cm².
F = 6 × 8,04 × 10 = **482 N**.*

Point important : **en rentrée, la tige occupe une partie de la section**, donc l'effort est plus
faible. Un vérin ne pousse pas aussi fort qu'il ne tire.

### 5. Débit et vitesse

> **Q = S × v** — le débit se conserve dans une canalisation

Si la section diminue, la vitesse augmente d'autant. C'est ce qui règle la vitesse de sortie d'un
vérin : le débit d'air divisé par la section du piston.

Et c'est pourquoi on règle la vitesse d'un vérin par un **limiteur de débit**, pas en jouant sur
la pression : la pression donne l'effort, le débit donne la vitesse.

### 6. Pneumatique ou hydraulique ?

| | Pneumatique | Hydraulique |
|---|---|---|
| pression usuelle | 6 à 8 bars | 100 à 300 bars |
| effort | modéré | très élevé |
| vitesse | rapide | modérée, très contrôlable |
| souplesse | l'air se comprime : mouvement élastique | l'huile est incompressible : position précise |
| propreté | fuite = rien | fuite = pollution |

En conception industrielle courante, on prend du pneumatique pour serrer, éjecter, indexer ; de
l'hydraulique dès qu'il faut plusieurs tonnes ou un positionnement précis sous charge.

### 7. Les erreurs classiques

1. **Confondre bars et pascals** (facteur 100 000).
2. **Calculer l'effort en rentrée avec la section pleine** : il faut retrancher la section de la
   tige.
3. **Vouloir régler une vitesse avec la pression.**
4. **Oublier la dilatation** sur les grandes pièces ou les montages mixtes acier-aluminium.
5. **Enfermer un mécanisme sans prévoir l'évacuation de la chaleur.**
""",
            "formules": """
**Thermique** — Q = m c ΔT · Φ = k S ΔT · ΔL = L₀ α ΔT

**Coefficients de dilatation** — acier 12·10⁻⁶ /°C · alu 23·10⁻⁶ · inox 16·10⁻⁶

**Pression** — p = F / S · 1 bar = 10⁵ Pa · 1 bar sur 1 cm² = 10 N

**Vérin** — F sortie = p × S piston · F rentrée = p × (S piston − S tige)

**Débit** — Q = S v · Q en L/min, S en cm², v en m/min

**Repère** — un vérin Ø32 à 6 bars pousse environ 480 N
""",
            "exercice": """
**1.** Un vérin pneumatique Ø50 travaille à 6 bars. Quel effort développe-t-il en sortie ?

**2.** Sa tige fait Ø20. Quel effort développe-t-il en rentrée ?

**3.** Un arbre en aluminium de 1 200 mm passe de 15 °C à 65 °C. De combien s'allonge-t-il ?
(α = 23·10⁻⁶ /°C)

**4.** Le même arbre en acier : quel allongement ? Que conclus-tu pour un montage mixte ?

**5.** Un réducteur transmet 5,5 kW avec un rendement de 0,95. Quelle puissance part en chaleur ?
""",
            "corrige": """
**1.** S = π × 50² / 4 = 1 963 mm² = **19,63 cm²**
F = 6 bars × 19,63 cm² × 10 = **1 178 N**, soit environ 120 kg de poussée.

**2.** Section utile = section piston − section tige
S tige = π × 20² / 4 = 314 mm² → S utile = 1 963 − 314 = 1 649 mm² = 16,49 cm²
F = 6 × 16,49 × 10 = **989 N**

*Soit 16 % de moins qu'en sortie. C'est pourquoi on oriente toujours un vérin de bridage de façon
à ce que le serrage se fasse **en poussant**, pas en tirant.*

**3.** ΔL = 1 200 × 23·10⁻⁶ × 50 = **1,38 mm**

**4.** ΔL = 1 200 × 12·10⁻⁶ × 50 = **0,72 mm**

**Conclusion :** l'aluminium s'allonge presque **deux fois plus** que l'acier. Dans un montage
mixte — carter aluminium, arbre acier — les jeux évoluent fortement avec la température : un jeu
correct à froid peut devenir un serrage ou un jeu excessif à chaud.

*C'est pour cette raison qu'on choisit les ajustements d'un carter aluminium en tenant compte de
la température de service, et non à 20 °C seulement.*

**5.** Pertes = 5 500 × (1 − 0,95) = **275 W**

*275 W dans un carter fermé, c'est presque trois ampoules à incandescence. Sans ailettes ni
ventilation, l'huile monte au-delà de 90 °C, se dégrade, et la durée de vie des roulements
s'effondre.*
""",
            "exemple": """
**Cas industriel — Dimensionner un bridage pneumatique**

Sur un poste d'assemblage, une pièce doit être **maintenue à 800 N** pendant le vissage. Le
réseau d'air comprimé de l'atelier délivre **6 bars**. Le vérin pousse un levier qui multiplie
l'effort par **1,6** (bras de levier).

**ÉTAPE 1 — Effort demandé au vérin**

F vérin = 800 / 1,6 = **500 N**

**ÉTAPE 2 — Section nécessaire**

S = F / p = 500 / (6 × 10) = **8,3 cm²**, soit Ø = √(4 × 830 / π) = **32,5 mm**

**ÉTAPE 3 — Choix dans la gamme normalisée**

Les alésages normalisés sont 12, 16, 20, 25, **32**, 40, 50, 63, 80, 100 mm. Le Ø32 donne 482 N
— tout juste insuffisant. On prend donc un **Ø40** : F = 6 × 12,57 × 10 = **754 N**, soit
1 206 N au niveau de la pièce.

**ÉTAPE 4 — Vérifier le sens de travail**

Le serrage se fait **en poussée** : on dispose bien des 754 N. S'il avait fallu serrer en
rentrée, avec une tige Ø16, l'effort serait tombé à 634 N.

**ÉTAPE 5 — Régler la vitesse**

On installe deux **limiteurs de débit** sur les orifices d'échappement : la vitesse d'approche
est ralentie pour ne pas marquer la pièce, la vitesse de retour est laissée rapide pour ne pas
allonger le temps de cycle.

**Ce que le cas apprend.** La pression donne l'**effort**, le débit donne la **vitesse**. Et l'on
ne choisit jamais un diamètre exact : on prend la taille normalisée immédiatement supérieure, ce
qui laisse une marge pour une chute de pression réseau — fréquente quand plusieurs machines
démarrent en même temps.
""",
        },
        {
            "id": "8.3",
            "titre": "Électricité, capteurs et actionneurs",
            "duree": "6 h",
            "cours": """
### 1. Pourquoi un mécanicien doit s'y intéresser

Parce qu'une machine moderne est **pluritechnique** : le concepteur mécanicien choisit un moteur,
prévoit la place d'un capteur, dimensionne un passage de câble, et discute avec l'automaticien.
Ne rien comprendre à l'électricité, c'est concevoir des pièces qu'il faudra reprendre.

### 2. Les trois grandeurs de base

| Grandeur | Symbole | Unité | Image mentale |
|---|---|---|---|
| tension | U | volt (V) | la pression dans le tuyau |
| intensité | I | ampère (A) | le débit qui circule |
| résistance | R | ohm (Ω) | l'étranglement du tuyau |

> **Loi d'Ohm : U = R × I**
> **Puissance : P = U × I** (en continu)

En triphasé — le cas de tous les moteurs industriels :
**P = √3 × U × I × cos φ**, où cos φ est le facteur de puissance (0,8 environ).

### 3. Le moteur asynchrone triphasé

[[FIG:plaque_moteur]]

C'est **le** moteur de l'industrie : robuste, bon marché, sans entretien. Sur sa plaque
signalétique, on lit :

- **puissance** en kW — la puissance mécanique disponible sur l'arbre ;
- **tension** 230/400 V — selon le couplage, triangle ou étoile ;
- **intensité** nominale — utile pour le câble et la protection ;
- **vitesse** en tr/min : 2 850, 1 450, 950… — jamais un chiffre rond, à cause du glissement ;
- **cos φ** et **rendement**.

**Pourquoi 1 450 et non 1 500 ?** La vitesse de synchronisme d'un moteur 4 pôles sur un réseau
50 Hz est de 1 500 tr/min. Le rotor tourne toujours un peu moins vite : c'est le **glissement**,
sans lequel aucun couple ne serait produit.

**Le variateur de fréquence** permet de faire varier cette vitesse en changeant la fréquence
d'alimentation. Il apporte aussi les rampes d'accélération, qui suppriment les pics de couple au
démarrage — le problème rencontré dans le cas du convoyeur.

### 4. Choisir un actionneur

| Solution | Points forts | Limites |
|---|---|---|
| **moteur asynchrone** | robuste, économique, puissant | vitesse peu réglable sans variateur |
| **motoréducteur** | couple élevé, faible vitesse, compact | rendement du réducteur |
| **servomoteur** | position et vitesse précises, dynamique | cher, nécessite un variateur et un codeur |
| **moteur pas à pas** | positionnement simple sans capteur | perd le pas s'il est surchargé |
| **vérin pneumatique** | rapide, simple, économique | deux positions seulement, effort limité |
| **vérin électrique** | positions multiples, propre | plus lent, plus cher |

### 5. Les capteurs : savoir ce qui se passe

- **Détecteur inductif** : détecte un métal sans contact, à quelques millimètres. Le plus courant.
- **Détecteur capacitif** : détecte aussi les matières non métalliques (liquide, plastique).
- **Cellule photoélectrique** : détecte à distance, par faisceau lumineux.
- **Fin de course mécanique** : contact physique, très fiable, mais s'use.
- **Codeur incrémental ou absolu** : mesure une position ou un angle avec précision.

**Ce que le mécanicien doit prévoir :** la **fixation** du capteur (rigide, réglable), la
**distance de détection** (quelques millimètres, pas plus), une **cible métallique** propre en
face, et le **passage du câble** — un capteur bien choisi mais dont le câble frotte sur une pièce
mobile tombera en panne en un mois.

### 6. Sécurité électrique : les bases à respecter

- **Indice de protection IP** : deux chiffres. Le premier concerne les solides (poussières), le
  second l'eau. **IP65** = étanche à la poussière et aux jets d'eau ; IP69K = lavage haute
  pression, l'agroalimentaire.
- **Consignation** : avant toute intervention mécanique, la machine est mise hors énergie et
  verrouillée. Une conception doit permettre cette consignation.
- **Séparation des flux** : on ne fait pas passer les câbles électriques dans le même chemin que
  les circuits hydrauliques, et on éloigne les câbles de puissance des câbles de signal.

### 7. Les erreurs classiques

1. **Placer un capteur inaccessible** : personne ne pourra le régler ni le remplacer.
2. **Oublier le passage et la fixation des câbles** dans la conception mécanique.
3. **Choisir un moteur sur sa seule puissance**, sans regarder la vitesse ni le couple de
   démarrage.
4. **Mettre un détecteur inductif face à une pièce en plastique** — il ne verra rien.
5. **Négliger l'indice IP** dans un environnement de lavage.
""",
            "formules": """
**Continu** — U = R I · P = U I

**Triphasé** — P = √3 U I cos φ · cos φ ≈ 0,8 pour un moteur asynchrone

**Vitesse de synchronisme** — Ns = 60 f / p (f = 50 Hz, p = nombre de paires de pôles)
2 pôles : 3 000 · 4 pôles : 1 500 · 6 pôles : 1 000 tr/min

**Glissement** — g = (Ns − N) / Ns, quelques % en charge

**Puissance mécanique** — P = C ω, avec ω = 2π N / 60

**Indice IP** — 1er chiffre : solides · 2e chiffre : eau · IP65 courant en industrie
""",
            "exercice": """
**1.** Un moteur porte sur sa plaque : 4 kW, 400 V, 8,3 A, 1 445 tr/min, cos φ 0,82. Vérifie la
cohérence entre puissance électrique absorbée et puissance mécanique annoncée.

**2.** Quel est le couple nominal de ce moteur ?

**3.** Combien de pôles a-t-il, et quel est son glissement ?

**4.** On veut faire tourner la machine à 700 tr/min. Deux solutions : réducteur ou variateur.
Que choisis-tu, et pourquoi ?

**5.** Un détecteur inductif doit repérer le passage d'un galet en polyamide. Est-ce possible ?
""",
            "corrige": """
**1.** Puissance absorbée = √3 × U × I × cos φ = 1,732 × 400 × 8,3 × 0,82 = **4 716 W**
Puissance mécanique = 4 000 W → rendement = 4 000 / 4 716 = **0,85**

*C'est cohérent : un moteur de cette taille a un rendement de 0,85 à 0,90. Les 716 W de
différence partent en chaleur dans le moteur — d'où son ventilateur.*

**2.** ω = 2π × 1 445 / 60 = 151,3 rad/s
C = P / ω = 4 000 / 151,3 = **26,4 N·m**

**3.** La vitesse est proche de 1 500 tr/min → **4 pôles** (2 paires).
Glissement = (1 500 − 1 445) / 1 500 = **3,7 %**

*Un glissement de 3 à 5 % en charge est normal. S'il dépasse 8 %, le moteur est en surcharge.*

**4.** Cela dépend de l'usage :

- **Réducteur** si la vitesse de 700 tr/min est **définitive** : rendement meilleur, coût plus
  faible, et le couple est multiplié par le rapport — un vrai avantage.
- **Variateur** si la vitesse doit être **réglable** en production, ou si l'on veut des rampes
  d'accélération. Mais attention : à basse vitesse, un moteur asynchrone ventile mal et chauffe ;
  au-delà d'un rapport 3, il faut une ventilation forcée.

*En pratique, on combine souvent les deux : un motoréducteur piloté par variateur.*

**5. Non.** Un détecteur **inductif** ne réagit qu'aux **métaux**. Face à un galet en polyamide,
il ne verra rien.

Trois solutions : un détecteur **capacitif** (qui voit toute matière), une **cellule
photoélectrique**, ou — le plus simple et le plus fiable — **ajouter une cible métallique** sur
la pièce mobile, en face du détecteur inductif.
""",
            "exemple": """
**Cas industriel — Concevoir l'implantation d'un capteur de position**

Un chariot de manutention doit s'arrêter précisément devant trois postes. L'automaticien demande
trois détecteurs de position ; le mécanicien doit les implanter.

**Les contraintes que le mécanicien doit intégrer**

| Contrainte | Conséquence sur la conception |
|---|---|
| distance de détection : 4 mm ± 1 | il faut une cible métallique tenue à 4 mm, sans vibration |
| réglage nécessaire | fixation **par trou oblong**, jamais par trou lisse |
| environnement : copeaux et huile | IP67 minimum, capteur orienté vers le bas |
| câble mobile | chaîne porte-câbles, rayon de courbure respecté |
| maintenance | accès à la main, capteur remplaçable sans démonter le chariot |

**Les décisions retenues**

1. **Cible en acier de 3 mm** vissée sur le chariot, plutôt que de détecter la structure en
   aluminium — l'inductif détecte mal l'aluminium et à distance réduite.
2. **Équerre de fixation avec oblongs** dans les deux directions : réglage en hauteur et en
   position longitudinale, sans démontage.
3. **Capteurs déportés vers l'extérieur**, hors de la zone de chute des copeaux, avec un petit
   déflecteur au-dessus.
4. **Chemin de câbles** intégré dès la conception du bâti, avec un rayon de courbure de 10 fois
   le diamètre du câble.

**Ce que le cas apprend.** Un capteur ne se rajoute pas à la fin : sa fixation, son réglage, sa
protection et le passage de son câble sont des **contraintes de conception mécanique**. Les
oublier, c'est livrer une machine qui fonctionne à la mise en service et qui tombe en panne au
bout d'un mois.
""",
        },
    ],
}


BLOC_9 = {
    "id": 9,
    "titre": "Bloc 9 — Méthodologie de projet et SolidWorks guidé",
    "resume": "Mener un projet du cahier des charges à la soutenance, et modéliser proprement pas à pas.",
    "fiches": [
        {
            "id": "9.1",
            "titre": "Conduire un projet technique de A à Z",
            "duree": "8 h",
            "cours": """
### 1. Pourquoi les projets échouent

Presque jamais par manque de compétence technique. Presque toujours pour trois raisons :

- **le besoin n'a pas été clarifié** au départ, et on découvre à trois semaines de la fin qu'on
  n'a pas fait ce qu'il fallait ;
- **le temps a été mal réparti** : trois mois sur la modélisation, trois jours sur le dossier ;
- **rien n'a été écrit au fil de l'eau**, et il faut tout reconstituer de mémoire à la fin.

Ces trois causes sont évitables avec un peu de méthode. C'est l'objet de cette fiche — et c'est
exactement ce qui sera évalué en deuxième année.

### 2. Les cinq phases d'un projet

| Phase | Ce qu'on y fait | Ce qui en sort |
|---|---|---|
| **1. Analyse du besoin** | comprendre le problème, pas la solution | le cahier des charges fonctionnel |
| **2. Recherche de solutions** | plusieurs pistes, comparées | un tableau comparatif, un choix argumenté |
| **3. Conception détaillée** | calculs, CAO, choix des composants | maquette 3D, notes de calcul |
| **4. Industrialisation** | plans, gamme, devis, approvisionnement | dossier de fabrication |
| **5. Réalisation et validation** | montage, essais, mesures | rapport d'essais, dossier final |

**La règle des 20 %.** La phase 1 doit occuper environ un cinquième du temps total. C'est
contre-intuitif — on a envie de dessiner tout de suite — mais une erreur d'analyse coûte cent
fois plus cher corrigée en phase 5 qu'en phase 1.

### 3. Le planning : Gantt et jalons

[[FIG:planning_projet]]

Un diagramme de **Gantt**, c'est simplement le temps en horizontal et les tâches en vertical,
chacune représentée par une barre.

Trois notions à maîtriser :

- **l'antériorité** : certaines tâches ne peuvent commencer qu'après d'autres. On ne commande pas
  la matière avant d'avoir choisi le matériau.
- **le chemin critique** : la suite de tâches qui détermine la durée totale. Tout retard sur ce
  chemin retarde le projet entier ; un retard ailleurs peut être absorbé.
- **les jalons** : des dates de validation, où l'on vérifie avant de continuer.

**Conseil pratique :** planifiez à rebours depuis la date de soutenance, et gardez **15 % de
marge** en fin de parcours. Les fournisseurs livrent en retard, les pièces arrivent non conformes,
les essais révèlent des surprises. C'est la règle, pas l'exception.

### 4. Comparer des solutions objectivement

Ne dites jamais « j'ai choisi la solution B parce qu'elle me paraissait mieux ». Construisez un
**tableau multicritère** :

1. lister les critères issus du cahier des charges (coût, masse, précision, délai, maintenance) ;
2. leur donner un **poids** selon leur importance ;
3. noter chaque solution de 1 à 5 sur chaque critère ;
4. multiplier, additionner, comparer.

Le tableau ne décide pas à votre place : il **rend votre raisonnement visible et discutable**.
C'est précisément ce qu'un jury cherche.

### 5. Tracer et archiver

Trois habitudes qui sauvent un projet :

- **un cahier de projet** — daté, où l'on note les décisions et leurs raisons. « Passé de l'alu à
  l'acier le 12/03 car flèche 2,3 mm > 0,5 mm exigé. » Trois mois plus tard, vous ne vous en
  souviendrez plus.
- **une nomenclature tenue à jour**, pas reconstituée à la fin.
- **des indices sur les plans** : A, B, C… avec la date et la nature de la modification.

### 6. Travailler à plusieurs

En projet de BTS, vous serez plusieurs. Les règles qui évitent les catastrophes :

- **un responsable par lot**, écrit noir sur blanc ;
- **un seul dossier de référence**, jamais des fichiers dupliqués sur cinq clés USB ;
- **une convention de nommage** : `support_capteur_v03.sldprt`, pas `piece_final_final2.sldprt` ;
- **un point d'avancement hebdomadaire**, court, avec ce qui bloque.

### 7. Les erreurs classiques

1. **Commencer par la CAO.** Le logiciel est un outil de conception, pas un outil de réflexion.
2. **Une seule solution étudiée.** Un jury demandera toujours : « et pourquoi pas autrement ? »
3. **Sous-estimer les délais d'approvisionnement** — souvent 3 à 6 semaines.
4. **Écrire le dossier à la fin.** Il faut l'écrire au fil de l'eau.
5. **Ne pas mesurer** le résultat : sans essais chiffrés, on ne peut pas prouver que ça marche.
""",
            "formules": """
**Répartition du temps** — analyse 20 % · solutions 15 % · conception 30 % · industrialisation
20 % · essais et dossier 15 %

**Marge de sécurité** — garder 15 % du planning en réserve en fin de projet

**Note multicritère** — Σ (poids × note) pour chaque solution comparée

**Indices de plan** — A, B, C… avec date et nature de la modification

**Nommage** — nom_fonction_version.extension, jamais « final », « final2 », « vraifinal »
""",
            "exercice": """
Un projet de 16 semaines : concevoir et réaliser un poste de contrôle d'étanchéité.

**1.** Répartis les 16 semaines entre les cinq phases.

**2.** La matière est livrée en 4 semaines et l'usinage prend 2 semaines. À quelle semaine, au
plus tard, faut-il avoir figé le choix du matériau ? (le montage commence en semaine 13)

**3.** Trois solutions sont envisagées pour la détection de fuite : capteur de pression,
débitmètre, bulle dans l'eau. Cite trois critères de comparaison issus d'un cahier des charges
industriel.

**4.** Ton binôme modifie une pièce sans te le dire, et l'assemblage ne se monte plus. Quelle
règle de travail a été enfreinte ?

**5.** À la soutenance, le jury demande : « pourquoi de l'aluminium ? » Que devrais-tu pouvoir
sortir immédiatement ?
""",
            "corrige": """
**1. Répartition sur 16 semaines**

| Phase | Durée | Semaines |
|---|---|---|
| analyse du besoin | 3 sem. | 1 à 3 |
| recherche de solutions | 2,5 sem. | 4 à 6 |
| conception détaillée | 5 sem. | 6 à 10 |
| industrialisation | 3 sem. | 10 à 13 |
| réalisation, essais, dossier | 2,5 sem. | 13 à 16 |

*Avec un chevauchement volontaire : on ne finit jamais une phase à 100 % avant d'entamer la
suivante.*

**2. Semaine 7 au plus tard**

Il faut remonter le temps depuis le montage : 13 − 2 (usinage) − 4 (livraison) = **semaine 7**.
Et comme il faut prévoir une marge, on vise **la semaine 6**.

*C'est exactement ce que fait un chemin critique : il impose des dates qu'on ne choisit pas.*

**3. Trois critères possibles**

- **précision de détection** : quel débit de fuite minimal doit être vu ?
- **temps de cycle** : combien de secondes par pièce ?
- **coût** d'investissement et de maintenance.

*On pourrait ajouter : la fiabilité de la mesure, la facilité d'interprétation par l'opérateur,
l'encombrement, la nécessité de sécher la pièce après contrôle.*

**4. Le dossier de référence unique et l'indiçage**

Chacun travaillait sur sa copie, sans indice ni information de modification. La règle : **un seul
dossier de référence**, et toute modification est indicée et signalée.

*C'est le problème le plus fréquent en projet à plusieurs — et celui qui coûte le plus de temps.*

**5. Le tableau comparatif et la note de calcul**

Il faut pouvoir montrer :
- le **tableau multicritère** où l'aluminium a été comparé à l'acier et à un composite ;
- la **note de calcul** de flèche qui montre que la section retenue satisfait l'exigence ;
- la **ligne du cahier de projet** datée, qui explique la décision.

*Un « ça me semblait bien » vaut zéro devant un jury. Une décision tracée et chiffrée vaut tous
les points.*
""",
            "exemple": """
**Cas industriel — Un projet de BTS qui a mal tourné, et pourquoi**

Un binôme doit concevoir et réaliser un **système de convoyage pour pièces de fonderie**.
16 semaines. Voici ce qui s'est réellement passé, semaine par semaine.

| Sem. | Ce qu'ils ont fait | Le problème caché |
|---|---|---|
| 1-2 | lecture rapide du sujet, ouverture de SolidWorks | aucun cahier des charges écrit |
| 3-7 | modélisation détaillée d'un convoyeur à bande | la solution n'a jamais été comparée à d'autres |
| 8 | le client précise : les pièces sortent **à 180 °C** | la bande caoutchouc ne tient pas |
| 9-11 | tout reprendre : convoyeur à chaîne métallique | 5 semaines de travail perdues |
| 12 | commande de la chaîne | délai annoncé : 6 semaines |
| 13-15 | montage partiel avec une chaîne de récupération | essais non représentatifs |
| 16 | rédaction du dossier en deux jours | dossier incomplet, aucune mesure |

**Le diagnostic**

Une seule erreur explique toute la cascade : **la phase 1 a duré deux jours au lieu de trois
semaines**. La température des pièces figurait dans le sujet ; personne ne l'a relevée parce que
personne n'a écrit de cahier des charges fonctionnel.

**Ce qu'il aurait fallu faire**

1. **Semaines 1 à 3** : bête à cornes, pieuvre, cahier des charges avec critères chiffrés. La
   contrainte « pièces à 180 °C » serait apparue en FC1, en flexibilité F0.
2. **Semaines 4 à 6** : trois solutions comparées — bande, chaîne métallique, rouleaux gravitaires.
3. **Semaine 6** : choix figé, matière commandée immédiatement.
4. Le reste du planning tenait sans difficulté.

**Ce que le cas apprend.** Le temps passé à comprendre le besoin n'est jamais du temps perdu :
c'est le seul moment du projet où corriger une erreur ne coûte rien.
""",
        },
        {
            "id": "9.2",
            "titre": "SolidWorks pas à pas : trois pièces guidées",
            "duree": "12 h",
            "cours": """
### 1. Comment utiliser cette fiche

Elle ne remplace pas le cours de CAO — elle le met en pratique. Ouvrez SolidWorks, suivez les
étapes dans l'ordre, et surtout **respectez l'ordre des fonctions**, même si un autre chemin
semble plus rapide. C'est l'ordre qui rend un modèle robuste.

Trois pièces, de difficulté croissante : une entretoise, une équerre percée, un support de
palier.

### 2. Les réflexes à prendre dès la première pièce

[[FIG:arbre_de_creation]]

Avant de commencer quoi que ce soit :

1. **Choisir le plan** : Face, Dessus ou Droite — jamais une face de la pièce si on peut l'éviter.
2. **Dessiner approximativement**, sans chercher les cotes exactes.
3. **Poser les contraintes géométriques** : symétrie, coïncidence, tangence.
4. **Coter** ce qui reste.
5. **Vérifier que l'esquisse est noire** (totalement contrainte) avant de fermer.
6. **Renommer la fonction** dans l'arbre.

Ces six gestes, répétés à chaque fonction, séparent un modèle professionnel d'un modèle
d'amateur.

### 3. PIÈCE 1 — Une entretoise (30 minutes)

*Un cylindre Ø30, longueur 40, percé d'un trou axial Ø12, avec un chanfrein 1×45° aux deux
extrémités.*

| Étape | Action | Le piège à éviter |
|---|---|---|
| 1 | Plan de **Droite**, esquisse d'un rectangle 15 × 40 collé à l'axe | ne pas dessiner le rectangle entier : on va faire une révolution |
| 2 | Contraindre : un côté sur l'axe vertical, symétrie par rapport à l'origine | esquisse noire avant de continuer |
| 3 | **Révolution** autour de l'axe | vérifier le sens : 360° |
| 4 | **Assistant de perçage** Ø12 débouchant, sur la face avant, concentrique | ne PAS extruder un cercle |
| 5 | **Chanfrein** 1×45° sur les arêtes extérieures | en dernier, toujours |
| 6 | Renommer : *Corps révolution*, *Perçage axial*, *Chanfreins* | |

**Test de robustesse :** changez la longueur de 40 à 70. Rien ne doit casser.

### 4. PIÈCE 2 — Une équerre percée (1 heure)

*Semelle 100 × 60 × 10, dos vertical 60 de haut × 10 d'épaisseur, 2 trous M8 dans la semelle,
1 alésage Ø20 H8 dans le dos, congés R5.*

| Étape | Action | Pourquoi ainsi |
|---|---|---|
| 1 | Plan de **Face**, esquisse du profil en L | une seule esquisse pour toute la forme générale |
| 2 | Symétrie par rapport à l'origine, puis cotes 100, 60, 10 | la pièce restera centrée si les cotes changent |
| 3 | **Extrusion symétrique** de 60 | « plan milieu » plutôt que « borgne » : la pièce reste centrée |
| 4 | **Assistant de perçage** M8 taraudé, deux trous | placés par cotes depuis l'origine |
| 5 | **Répétition linéaire** si les trous sont identiques | jamais deux perçages indépendants |
| 6 | **Assistant de perçage** Ø20 H8 dans le dos | avec la tolérance renseignée dans l'assistant |
| 7 | **Congés R5** sur l'angle intérieur et les arêtes | en fin d'arbre |

**Test de robustesse :** passez la semelle de 100 à 140 et la hauteur de 60 à 80. Les trous
doivent suivre, les congés se recalculer, aucune erreur dans l'arbre.

### 5. PIÈCE 3 — Un support de palier (2 heures)

*Semelle 140 × 80 × 15 avec 4 trous Ø11 oblongs, corps vertical avec alésage Ø52 H7 à 90 mm du
sol, nervure de renfort triangulaire, congés R3.*

| Étape | Action | Le point délicat |
|---|---|---|
| 1 | Plan de **Face**, profil du corps + semelle, symétrique | penser la pièce comme un profil extrudé |
| 2 | **Extrusion symétrique** 80 | |
| 3 | **Assistant de perçage** Ø52 H7 traversant | la cote fonctionnelle de la pièce |
| 4 | Esquisse du **triangle de nervure** sur le plan de Droite | s'appuyer sur le plan, pas sur une face |
| 5 | Fonction **Nervure** (pas une extrusion) épaisseur 8, plan milieu | la fonction Nervure gère seule le raccordement |
| 6 | **Trous oblongs** de la semelle par assistant, puis symétrie | oblongs = réglage possible au montage |
| 7 | **Congés R3** partout, en une seule fonction multi-arêtes | |
| 8 | Renommer toutes les fonctions | |

**Test de robustesse :** faites passer la hauteur d'axe de 90 à 120 mm. C'est la modification la
plus probable en vraie vie — le modèle doit l'encaisser sans broncher.

### 6. Passer à la mise en plan

[[FIG:esquisse_contraintes]]

Pour chaque pièce, sortez un plan :

1. Vue de face + vue de dessus, alignées automatiquement.
2. **Coupe A-A** passant par l'alésage.
3. Cotation : d'abord les cotes fonctionnelles avec tolérances, puis le reste.
4. États de surface : Ra 0,8 dans l'alésage, Ra 3,2 sur l'appui.
5. Cartouche : matière, échelle, indice, ISO 2768-m.

### 7. Les erreurs qui reviennent en TP

1. **Esquisse posée sur une face** au lieu d'un plan de référence.
2. **Cercle extrudé** au lieu de l'assistant de perçage.
3. **Congés placés trop tôt**, qui empêchent les fonctions suivantes.
4. **Extrusion « borgne »** au lieu de « plan milieu », ce qui décentre la pièce.
5. **Aucune fonction renommée** : un arbre illisible dans deux semaines.
6. **Ne jamais tester** : la robustesse ne se voit qu'en modifiant.
""",
            "formules": """
**L'ordre canonique d'un arbre de création**

1. forme générale (extrusion ou révolution)
2. enlèvements de matière importants (poches, épaulements)
3. perçages — toujours par l'assistant
4. répétitions et symétries
5. nervures et coques
6. **congés, chanfreins, dépouilles — en dernier**

**Les six gestes de chaque esquisse** — plan de référence · tracé approximatif · contraintes
géométriques · cotes · vérifier « totalement contrainte » · renommer

**Test de robustesse** — changer deux cotes majeures, l'arbre ne doit signaler aucune erreur
""",
            "exercice": """
**1.** Tu dois modéliser une poulie Ø120 avec une gorge trapézoïdale, un moyeu Ø40 et une rainure
de clavette. Quelle fonction de base utilises-tu pour la forme générale, et pourquoi ?

**2.** Dans quel ordre places-tu : la rainure de clavette, la gorge de courroie, les congés,
l'alésage Ø25 ?

**3.** Ton esquisse de profil ne peut pas être révolutionnée : SolidWorks refuse. Cite deux
causes probables.

**4.** Tu dois créer 8 trous Ø9 répartis sur un cercle Ø100. Combien de fonctions, et lesquelles ?

**5.** Après avoir changé une cote, trois fonctions passent en erreur avec un point
d'exclamation. Par laquelle commences-tu la correction ?
""",
            "corrige": """
**1. La révolution**

Une poulie est une pièce **de révolution** : un seul profil, tourné autour de l'axe, crée d'un
coup le corps, la gorge et le moyeu. C'est aussi ainsi qu'elle est fabriquée, au tour.

*Faire la même pièce par extrusions successives donnerait un modèle deux fois plus long et bien
plus fragile.*

**2. L'ordre correct**

1. **Révolution** du profil : elle inclut déjà la gorge de courroie et l'alésage Ø25, puisqu'ils
   font partie du profil.
2. **Rainure de clavette** : extrusion coupée, ou fonction dédiée.
3. **Congés** en dernier.

*Point important : dans une révolution, tout ce qui est axisymétrique se dessine dans le profil.
On ne crée pas la gorge après coup — c'est une erreur de débutant qui alourdit l'arbre.*

**3. Deux causes probables**

- **le profil est ouvert** : pour une révolution, il doit être fermé (ou fermé par l'axe) ;
- **le profil traverse l'axe de révolution** : la matière se recouvrirait elle-même, ce que le
  logiciel refuse.

*Une troisième cause fréquente : l'axe de révolution n'a pas été désigné, ou l'esquisse contient
des entités en double.*

**4. Deux fonctions**

1. **un perçage Ø9** par l'assistant, positionné sur le cercle de répartition ;
2. **une répétition circulaire** de 8 occurrences sur 360°.

*Jamais 8 perçages séparés : le jour où le nombre passe à 12, on modifie un chiffre au lieu d'en
créer quatre de plus.*

**5. Par la PREMIÈRE erreur dans l'arbre, en partant du haut**

Les erreurs se propagent en cascade : une fonction en erreur casse toutes celles qui s'appuient
dessus. Très souvent, corriger la première fait disparaître les deux autres.

*Réflexe : on remonte toujours à la source, jamais on ne corrige la dernière erreur visible.*
""",
            "exemple": """
**Cas industriel — Modéliser une pièce à partir d'un plan de fournisseur**

Un fournisseur envoie le **plan papier** d'un support qu'il faut intégrer dans un assemblage. Il
n'a pas de fichier 3D. Voici la méthode professionnelle pour le remodéliser, en 45 minutes.

**ÉTAPE 1 — Lire le plan avant de toucher au clavier (10 min)**

- repérer la vue de face, les coupes, le symbole de projection ;
- identifier les **surfaces fonctionnelles** : celles qui portent une tolérance serrée ou un état
  de surface. Elles indiquent ce qui compte vraiment ;
- repérer la **cote qui risque de changer** — celle qui dépend de l'environnement.

**ÉTAPE 2 — Décider de la stratégie de modélisation (5 min)**

Sur ce support : un corps prismatique extrudé, un alésage, une nervure, des perçages. Donc :
extrusion symétrique, puis perçages, puis nervure, puis congés.

*Cette réflexion de cinq minutes évite une heure de reprise.*

**ÉTAPE 3 — Modéliser (25 min)**

En suivant l'ordre canonique, avec les six gestes à chaque esquisse. On renseigne les
**tolérances dans l'assistant de perçage** au moment où on crée les trous : elles se retrouveront
automatiquement dans la mise en plan.

**ÉTAPE 4 — Vérifier (5 min)**

- comparer les cotes du modèle avec celles du plan, une à une ;
- **mesurer la masse** dans le logiciel et la comparer à celle du plan si elle est indiquée. Un
  écart révèle une erreur de forme ou de matière ;
- lancer le test de robustesse.

**Ce que le cas apprend.** On ne modélise jamais « en lisant les cotes au fur et à mesure ». On
lit d'abord, on décide d'une stratégie, puis on exécute. Et la masse calculée est le meilleur
autocontrôle qui existe : c'est un chiffre unique qui vérifie tout le modèle d'un coup.
""",
        },
        {
            "id": "9.3",
            "titre": "Dossier technique et soutenance orale",
            "duree": "6 h",
            "cours": """
### 1. Ce qui est réellement évalué

Un jury de BTS n'évalue pas seulement ce que vous avez fabriqué. Il évalue **votre capacité à
expliquer ce que vous avez fait et pourquoi**. Un projet moyen très bien défendu obtient souvent
une meilleure note qu'un projet brillant mal expliqué.

Trois questions reviennent systématiquement :

- « **Pourquoi ce choix** plutôt qu'un autre ? »
- « **Comment avez-vous vérifié** que ça fonctionne ? »
- « **Qu'est-ce que vous feriez différemment** si c'était à refaire ? »

Préparez ces trois réponses, elles tomberont.

### 2. La structure du dossier technique

| Partie | Contenu | Volume indicatif |
|---|---|---|
| présentation | le contexte, l'entreprise, le besoin | 1 à 2 pages |
| cahier des charges | fonctions, critères, niveaux, flexibilité | 2 pages |
| solutions étudiées | plusieurs pistes, tableau comparatif, choix argumenté | 3 pages |
| conception | calculs, extraits de CAO, choix des composants | 6 à 10 pages |
| industrialisation | plans, gamme, nomenclature, coûts | 4 pages |
| essais et résultats | protocole, mesures, comparaison au cahier des charges | 3 pages |
| bilan | ce qui a marché, ce qui n'a pas marché, perspectives | 1 page |

**La règle d'or : chaque affirmation est étayée.** « La pièce résiste » ne vaut rien ; « σ = 37,5
MPa < Rpe = 78,3 MPa, calcul en annexe 4 » vaut tout.

### 3. Les figures : ce qui fait la différence

Un dossier technique se lit d'abord **en diagonale, par ses figures**. Soignez-les :

- chaque figure porte un **numéro, un titre et une légende** ;
- chaque figure est **appelée dans le texte** : « voir figure 7 » ;
- une capture d'écran de CAO se recadre et s'annote — on ne colle jamais l'écran entier avec les
  menus ;
- un tableau vaut mieux qu'un paragraphe pour comparer.

### 4. Préparer la soutenance

[[FIG:structure_soutenance]]

**Le format habituel** : 20 minutes de présentation, 20 minutes de questions.

**Le plan qui marche**, en 12 à 15 diapositives :

1. le besoin, en une phrase (30 s) ;
2. le cahier des charges, ramené à 4 ou 5 exigences chiffrées (2 min) ;
3. les solutions envisagées et le tableau de choix (3 min) ;
4. la solution retenue, en image (3 min) ;
5. **deux ou trois points techniques approfondis** — vos calculs, vos choix (6 min) ;
6. la réalisation et les essais, avec des mesures (4 min) ;
7. le bilan, honnête (2 min).

**Ce qui plombe une soutenance** : lire ses diapositives, montrer trente vues de CAO sans les
commenter, dépasser le temps, et surtout ne pas savoir répondre à « pourquoi ».

### 5. Répondre aux questions

- **Écoutez la question en entier** avant de répondre. Reformulez-la si besoin.
- **Si vous ne savez pas, dites-le** : « je ne l'ai pas vérifié, mais je procéderais ainsi ».
  Un jury respecte l'honnêteté ; il déteste l'invention.
- **Assumez les échecs.** « Cette solution n'a pas fonctionné, voilà pourquoi, et voilà ce que
  j'en ai tiré » est une excellente réponse. Un projet sans difficulté n'existe pas.
- **Ramenez à vos preuves** : sortez le tableau comparatif, la note de calcul, la courbe d'essai.

### 6. Ce qu'il faut mesurer et montrer

Un projet validé, c'est un projet **mesuré**. Reprenez chaque exigence chiffrée du cahier des
charges et mettez en face la valeur obtenue :

| Exigence | Niveau demandé | Mesuré | Verdict |
|---|---|---|---|
| effort de serrage | ≥ 800 N | 830 N | ✅ |
| temps de cycle | ≤ 6 s | 6,4 s | ❌ à améliorer |
| flèche du bras | ≤ 0,3 mm | 0,18 mm | ✅ |

Ce tableau, seul, peut faire une diapositive entière — c'est souvent la plus convaincante de
toute la soutenance.

### 7. Les erreurs classiques

1. **Rédiger le dossier à la fin**, de mémoire.
2. **Aucune mesure** : rien ne prouve que ça marche.
3. **Cacher un échec.** Le jury le verra, et l'absence d'analyse sera plus pénalisée que l'échec
   lui-même.
4. **Diapositives surchargées** de texte lu à voix haute.
5. **Ne pas répéter à voix haute**, chronomètre en main. Le temps se maîtrise en répétant, pas en
   espérant.
""",
            "formules": """
**Structure du dossier** — contexte · cahier des charges · solutions comparées · conception ·
industrialisation · essais · bilan

**Répartition d'une soutenance de 20 min** — besoin 1 min · CdC 2 · solutions 3 · retenue 3 ·
technique 6 · essais 4 · bilan 2

**Les trois questions du jury** — pourquoi ce choix ? · comment l'avez-vous vérifié ? · que
feriez-vous autrement ?

**La règle d'or** — chaque affirmation est étayée par un calcul, une mesure ou une source

**Tableau de validation** — exigence · niveau demandé · valeur mesurée · verdict
""",
            "exercice": """
**1.** Réécris cette phrase de dossier pour qu'elle soit recevable : « Nous avons choisi
l'aluminium car c'est plus léger et ça suffisait. »

**2.** Le jury demande : « pourquoi ne pas avoir mis un roulement à billes plutôt qu'un
coussinet ? ». Structure ta réponse en trois temps.

**3.** Ton essai montre un temps de cycle de 6,4 s alors que le cahier des charges impose 6 s.
Que fais-tu : tu le caches, tu l'écris, tu l'écris et tu l'analyses ?

**4.** Tu as 20 minutes et 34 diapositives préparées. Quel est le problème, et que fais-tu ?

**5.** Cite trois éléments à avoir sous la main pendant les questions.
""",
            "corrige": """
**1. Version recevable**

> « L'aluminium 6060 a été retenu après comparaison avec l'acier S235 et un composite verre-époxy
> (tableau 3). Il réduit la masse mobile de 2,4 kg à 0,9 kg, ce qui permet de tenir le temps de
> cycle de 6 s (calcul § 4.2). La flèche calculée, 0,18 mm, reste inférieure aux 0,3 mm exigés
> (annexe 4). »

*Ce qui change : les alternatives sont citées, les chiffres remplacent les impressions, et
chaque affirmation renvoie à une preuve.*

**2. Réponse en trois temps**

1. **Le critère qui a tranché** : « la vitesse de rotation est faible, 40 tr/min, et
   l'environnement est chargé en poussière abrasive » ;
2. **La comparaison** : « un roulement y aurait une durée de vie réduite par la pollution, alors
   qu'un coussinet bronze tolère bien les particules » ;
3. **La vérification** : « la pression de contact calculée est de 4,2 MPa, très inférieure aux
   10 MPa admissibles pour ce bronze ».

*Structure universelle : le critère, la comparaison, la preuve.*

**3. Tu l'écris ET tu l'analyses**

C'est la seule bonne réponse. Par exemple :

> « Le temps de cycle mesuré est de 6,4 s contre 6 s exigés. L'écart provient de la temporisation
> de 0,5 s ajoutée en fin de course pour laisser le vérin se stabiliser. Deux pistes : réduire la
> vitesse d'approche pour supprimer le rebond, ou passer à un vérin avec amortissement réglable. »

*Un écart analysé prouve que vous comprenez votre système. Un écart caché, découvert par le jury,
détruit la confiance sur tout le reste.*

**4. Trop de diapositives — il faut couper**

Le rythme raisonnable est d'environ **une diapositive par minute**, soit 15 à 20 au maximum.

Ce qu'on garde : le besoin, le cahier des charges résumé, le tableau de choix, la solution en
image, deux ou trois points techniques approfondis, les essais, le bilan.
Ce qu'on déplace **en annexe** — pour les questions : toutes les vues de CAO supplémentaires,
les notes de calcul détaillées, les plans.

**5. Trois éléments à avoir sous la main**

- le **tableau comparatif** des solutions ;
- les **notes de calcul** (RDM, ajustements, dimensionnement moteur) ;
- le **tableau de validation** exigences / mesures, et les plans cotés.

*Sortir le bon document en trois secondes fait une impression considérable sur un jury.*
""",
            "exemple": """
**Cas industriel — Deux soutenances, deux notes**

Deux binômes présentent un projet équivalent : un poste de contrôle dimensionnel.

**Binôme A — projet techniquement plus abouti, note moyenne**

- 32 diapositives, dont 18 vues de CAO enchaînées sans commentaire ;
- aucune mention des solutions écartées : « on a fait comme ça » ;
- essais : « ça fonctionne bien » — aucun chiffre ;
- question du jury : « pourquoi un guidage à billes plutôt qu'une glissière ? » → « c'est ce
  qu'on avait au magasin » ;
- dépassement de 6 minutes, bilan bâclé.

**Binôme B — projet plus modeste, très bonne note**

- 14 diapositives, dont une seule vue d'ensemble et deux zooms sur les points délicats ;
- une diapositive entière sur le **tableau comparatif** des trois solutions envisagées ;
- une diapositive de **calcul** : la flèche du bras support, avec l'hypothèse et le résultat ;
- une diapositive de **validation** : exigences du cahier des charges d'un côté, mesures de
  l'autre, dont **un écart assumé** (répétabilité 0,04 mm au lieu de 0,03) avec l'explication et
  deux pistes d'amélioration ;
- réponses courtes, appuyées sur les annexes sorties immédiatement.

**Ce qui a fait la différence.** Le binôme B n'a pas montré plus de travail : il a montré un
**raisonnement**. Le jury a pu suivre le chemin qui va du besoin à la solution, vérifier que les
choix étaient fondés, et constater que les écarts étaient compris.

**La leçon.** Votre dossier et votre soutenance ne racontent pas ce que vous avez **fait**, mais
comment vous avez **décidé**. C'est cela, le métier de technicien supérieur.
""",
        },
    ],
}


BLOC_10 = {
    "id": 10,
    "titre": "Bloc 10 — Anglais technique et économie-gestion",
    "resume": "Lire une documentation en anglais, et comprendre le coût de ce qu'on dessine.",
    "fiches": [
        {
            "id": "10.1",
            "titre": "Anglais technique : lire une documentation",
            "duree": "6 h",
            "cours": """
### 1. L'anglais dont vous avez besoin n'est pas celui du lycée

Un technicien n'a pas besoin de parler de littérature. Il a besoin de :

- **lire** une fiche technique, un catalogue de roulements, une notice de montage ;
- **comprendre** un plan reçu d'un client étranger ;
- **écrire** un courriel court et clair à un fournisseur ;
- **présenter** brièvement son travail.

Le vocabulaire utile tient en quelques centaines de mots — et ce sont toujours les mêmes.

### 2. Le vocabulaire du dessin technique

| Français | Anglais |
|---|---|
| plan, dessin | drawing |
| vue de face / dessus / gauche | front / top / left view |
| coupe, section | section view, cut |
| cote | dimension |
| tolérance | tolerance |
| ajustement | fit |
| alésage | bore, hole |
| arbre | shaft |
| jeu / serrage | clearance / interference |
| état de surface | surface finish |
| échelle | scale |
| cartouche | title block |
| nomenclature | bill of materials (BOM), parts list |

### 3. Le vocabulaire des pièces et des matériaux

[[FIG:decoder_designation]]

| Français | Anglais |
|---|---|
| roulement | bearing |
| palier | housing, bearing block |
| engrenage, pignon | gear, pinion |
| courroie / chaîne | belt / chain |
| vis / écrou / rondelle | screw / nut / washer |
| clavette | key |
| ressort | spring |
| joint | seal, gasket |
| acier / fonte | steel / cast iron |
| aluminium / laiton / bronze | aluminium / brass / bronze |
| trempe / revenu | quenching / tempering |
| limite élastique | yield strength |
| résistance à la rupture | tensile strength |

### 4. Le vocabulaire des procédés

| Français | Anglais |
|---|---|
| usinage | machining |
| tournage / fraisage | turning / milling |
| perçage / taraudage | drilling / tapping |
| rectification | grinding |
| moulage | casting |
| injection | injection moulding |
| pliage / emboutissage | bending / stamping |
| soudage | welding |
| impression 3D | 3D printing, additive manufacturing |

### 5. Les pièges de traduction

Quelques faux amis qui coûtent cher :

- **« to control »** ne veut pas dire contrôler au sens de vérifier, mais **commander, piloter**.
  Vérifier se dit **to check** ou **to inspect**.
- **« a plan »** est un projet, pas un dessin. Un plan de fabrication est **a drawing**.
- **« an engine »** est un moteur thermique ; un moteur électrique est **a motor**.
- **« rigid »** signifie raide, mais aussi rigide au sens strict — la rigidité au sens mécanique
  est **stiffness**, à ne pas confondre avec **strength**, la résistance. C'est exactement la
  distinction Re / E de la fiche 3.1.
- **« a hole »** est un trou quelconque ; **a bore** est un alésage usiné avec précision.

### 6. Lire les unités anglo-saxonnes

Les documents américains utilisent encore les pouces et les livres :

| Unité | Conversion |
|---|---|
| 1 inch (1″) | 25,4 mm |
| 1 foot (1′) | 304,8 mm |
| 1 pound (lb) | 0,454 kg |
| 1 psi | 6 895 Pa ≈ 0,069 bar |
| 1 lbf·in | 0,113 N·m |

Et attention à la notation décimale : les Anglo-Saxons écrivent **1.5** là où nous écrivons
**1,5**. Sur un plan, cette différence peut faire un facteur 10 sur une cote.

### 7. Écrire un courriel professionnel court

La structure attendue, en quatre lignes :

> **Subject:** Request for quotation — 50 pcs support bracket
>
> Dear Sir or Madam,
>
> We are looking for a quotation for 50 pieces of the attached part (drawing SB-042, rev. B),
> material: aluminium EN AW-6060, anodised.
> Could you please confirm your price and lead time?
>
> Best regards,

Trois expressions qui servent tout le temps : **lead time** (délai de livraison), **quotation**
(devis), **drawing rev.** (indice du plan).
""",
            "formules": """
**Conversions** — 1 inch = 25,4 mm · 1 foot = 304,8 mm · 1 lb = 0,454 kg · 1 psi ≈ 0,069 bar

**Notation** — décimale anglo-saxonne : 1.5 = 1,5 · séparateur de milliers : 1,000 = 1 000

**Faux amis** — control = piloter (vérifier = to check) · engine = moteur thermique ·
stiffness = rigidité ≠ strength = résistance

**Courriel** — quotation (devis) · lead time (délai) · purchase order (commande) ·
drawing rev. (indice)
""",
            "exercice": """
**1.** Traduis : « L'alésage Ø50 H7 reçoit un roulement à billes ; état de surface Ra 0,8. »

**2.** Une documentation indique : *« Shaft tolerance: k6. Housing tolerance: H7. »* Que signifie
cette phrase pour le monteur ?

**3.** Un plan américain porte la cote **2.500 in**. Quelle est la cote en millimètres ?

**4.** Un catalogue annonce *« max. operating pressure: 145 psi »*. Convertis en bars.

**5.** Un fournisseur écrit : *« Lead time is 6 weeks from receipt of purchase order. »*
Que comprends-tu, et quelle question poses-tu ?
""",
            "corrige": """
**1.** *« The Ø50 H7 bore houses a ball bearing; surface finish Ra 0.8. »*

*Notez le point décimal, pas la virgule : Ra 0.8. Et « bore » plutôt que « hole », parce qu'il
s'agit d'un alésage usiné avec tolérance.*

**2.** Cela signifie que **la bague intérieure est montée serrée sur l'arbre** (k6) et que **la
bague extérieure est glissante dans le logement** (H7).

C'est le cas classique de l'arbre tournant sous charge fixe. Pour le monteur, cela veut dire :
l'arbre demande un effort de montage (presse ou maillet et douille), le logement se fait à la
main.

**3.** 2,500 × 25,4 = **63,5 mm**.

*Piège : la cote s'écrit 2.500 avec un point. Un lecteur pressé pourrait lire « deux mille cinq
cents ». Et 63,5 mm n'est pas une valeur ronde — signe qu'il faudra peut-être adapter le
composant en face.*

**4.** 145 × 0,069 = **10 bars** environ.

*Repère utile à retenir : 145 psi ≈ 10 bars, et 1 bar ≈ 14,5 psi.*

**5.** Le délai est de **6 semaines à compter de la réception de la commande** — pas à compter de
la demande de devis.

La question à poser : *« Could you confirm whether this lead time includes surface treatment and
delivery? »* — le délai annoncé exclut souvent le traitement de surface et le transport, ce qui
peut ajouter deux semaines.
""",
            "exemple": """
**Cas industriel — Décoder une fiche technique de roulement**

Extrait typique d'un catalogue anglophone :

> **Deep groove ball bearing 6205-2RS**
> Bore: 25 mm · Outside diameter: 52 mm · Width: 15 mm
> Dynamic load rating C: 14.0 kN · Static load rating C₀: 7.80 kN
> Limiting speed (grease): 14 000 rpm
> Recommended shaft tolerance: k6 (rotating inner ring load)
> Recommended housing tolerance: H7 (stationary outer ring load)
> Sealing: contact seals both sides

**La traduction, ligne par ligne**

| Anglais | Français | Ce que ça implique |
|---|---|---|
| deep groove ball bearing | roulement à billes à gorge profonde | le type le plus courant |
| 2RS | joints d'étanchéité des deux côtés | graissé à vie, sans entretien |
| bore 25 | alésage 25 | l'arbre doit faire Ø25 |
| dynamic load rating C | charge dynamique de base | sert au calcul de durée de vie |
| static load rating C₀ | charge statique | pour un roulement à l'arrêt ou très lent |
| limiting speed | vitesse limite | 14 000 tr/min avec de la graisse |
| rotating inner ring load | charge tournante sur bague intérieure | **la fameuse règle des charges** |

**Ce que le concepteur en tire immédiatement**

1. L'arbre doit être coté **Ø25 k6** et l'alésage du carter **Ø52 H7** — c'est écrit noir sur
   blanc dans la fiche, pas à deviner.
2. Le roulement étant **2RS**, il ne faut ni graisseur ni joint supplémentaire.
3. La vitesse limite de 14 000 tr/min est très supérieure à un usage courant : aucune
   contrainte de ce côté.

**Ce que le cas apprend.** Une fiche technique de roulement contient déjà tous les ajustements à
respecter. Beaucoup d'erreurs de montage viennent simplement du fait que personne ne l'a lue —
souvent parce qu'elle était en anglais.
""",
        },
        {
            "id": "10.2",
            "titre": "Économie-gestion : le coût de ce qu'on dessine",
            "duree": "6 h",
            "cours": """
### 1. Un concepteur engage de l'argent à chaque trait

C'est la réalité que découvrent tous les jeunes techniciens : **80 % du coût d'un produit est
figé pendant la conception**, alors que la conception ne représente que 5 à 10 % des dépenses.

Un congé oublié, une tolérance serrée sans raison, un matériau exotique, une pièce impossible à
monter : chacune de ces décisions se paie ensuite, multipliée par la série.

Savoir combien coûte ce qu'on dessine n'est donc pas un souci de comptable : c'est une compétence
de concepteur.

### 2. De quoi est fait le prix d'une pièce

| Composante | Ce qu'elle recouvre | Part typique |
|---|---|---|
| **matière** | le brut, moins les chutes | 15 à 40 % |
| **main-d'œuvre** | le temps passé, au taux horaire | 20 à 40 % |
| **machine** | l'amortissement, l'énergie, l'outillage | 15 à 30 % |
| **outillage spécifique** | moule, gabarit, montage d'usinage | selon la série |
| **frais généraux** | bâtiment, encadrement, qualité | 15 à 25 % |
| **marge** | le bénéfice de l'entreprise | 5 à 15 % |

**Coût de revient = matière + main-d'œuvre + machine + frais généraux.**
**Prix de vente = coût de revient + marge.**

### 3. Le rôle décisif de la série

[[FIG:seuil_rentabilite]]

C'est le paramètre qui change tout. L'outillage spécifique se répartit sur les pièces produites :

> **coût unitaire = coût variable + (coût d'outillage / nombre de pièces)**

**Exemple.** Un carter, deux procédés possibles :

| | Usinage dans la masse | Moulage sous pression |
|---|---|---|
| outillage | 0 € | 12 000 € (le moule) |
| coût par pièce | 85 € | 9 € |
| pour 10 pièces | 850 € | 12 090 € → **1 209 €/pièce** |
| pour 500 pièces | 42 500 € | 16 500 € → **33 €/pièce** |
| pour 5 000 pièces | 425 000 € | 57 000 € → **11,40 €/pièce** |

**Le seuil de rentabilité** se situe ici vers **160 pièces**. En dessous, on usine ; au-dessus,
on moule. C'est le genre de calcul qu'on attend d'un technicien supérieur.

### 4. Les décisions de conception qui coûtent cher

| Décision | Effet sur le coût |
|---|---|
| resserrer un IT de 0,2 à 0,02 mm | × 3 à × 5 sur l'opération concernée |
| demander Ra 0,8 au lieu de Ra 3,2 | ajoute une opération de rectification |
| ajouter une reprise d'usinage sur une autre face | + 15 à 30 % de temps machine |
| choisir de l'inox au lieu d'un acier ordinaire | × 5 à × 8 sur la matière, usinage plus lent |
| dessiner un angle intérieur vif | infaisable : reprise ou électroérosion |
| oublier une dépouille en moulage | outillage à modifier, plusieurs milliers d'euros |

À l'inverse, les décisions **gratuites** qui font gagner : normaliser les diamètres de perçage,
réutiliser un composant du catalogue existant, regrouper les usinages sur une seule face,
concevoir la pièce pour qu'elle se monte dans un seul sens.

### 5. Faire ou faire faire

Une question qui revient sans arrêt en entreprise. On compare :

- **en interne** : coût horaire de l'atelier × temps, plus la matière, plus la charge des
  machines. Avantage : maîtrise, réactivité.
- **en sous-traitance** : le devis, plus le transport, plus le temps de gestion et le risque de
  délai. Avantage : pas d'investissement, capacité disponible.

Le critère caché, souvent décisif : **la charge de l'atelier**. Une machine déjà saturée fait
partir la pièce à l'extérieur, même si le calcul brut disait l'inverse.

### 6. Lire un devis fournisseur

Trois pièges classiques :

1. **Le prix unitaire dépend de la quantité.** Un devis « 32 € l'unité » n'a de sens qu'avec la
   quantité en face.
2. **Les frais d'outillage sont parfois cachés** dans une ligne « frais de mise en route ».
3. **Le délai annoncé démarre à la commande**, pas au devis — et exclut souvent le traitement de
   surface et le transport.

Comparer deux devis, c'est donc comparer **prix unitaire + outillage + transport + délai**, à
quantité identique.

### 7. Les erreurs classiques

1. **Coter serré partout** « par sécurité ».
2. **Ne pas se demander combien de pièces** seront produites avant de choisir un procédé.
3. **Comparer deux devis** sur le seul prix unitaire.
4. **Ignorer le coût de montage** : une pièce moins chère mais deux fois plus longue à assembler
   coûte plus cher au final.
5. **Oublier le coût de non-qualité** : un rebut, c'est la matière **et** le temps déjà passé.
""",
            "formules": """
**Coût de revient** = matière + main-d'œuvre + machine + frais généraux
**Prix de vente** = coût de revient + marge

**Coût unitaire avec outillage** = coût variable + (outillage / quantité)

**Seuil de rentabilité entre deux procédés** — quantité N telle que
outillage₂ / N + variable₂ = variable₁

**Ordres de grandeur** — resserrer un IT d'un facteur 10 : × 3 à × 5 · inox vs acier : × 5 à × 8
sur la matière · 80 % du coût est figé en conception
""",
            "exercice": """
Une pièce peut être obtenue de deux façons :

- **Usinage** : pas d'outillage, 46 € la pièce.
- **Fonderie** : moule 8 500 €, puis 7 € la pièce.

**1.** Coût total pour 50 pièces dans chaque cas ?

**2.** Coût total pour 1 000 pièces ?

**3.** À partir de combien de pièces la fonderie devient-elle intéressante ?

**4.** Le bureau d'études propose de resserrer une tolérance de IT11 à IT7 sur trois cotes, sans
justification fonctionnelle. Sachant que l'opération concernée représente 12 € par pièce, quel
surcoût sur une série de 1 000 pièces si le facteur est de 3 ?

**5.** Deux devis pour 200 pièces : A = 28 € l'unité, outillage 0, délai 8 semaines. B = 19 €
l'unité, outillage 2 400 €, délai 5 semaines. Lequel choisis-tu ?
""",
            "corrige": """
**1. Pour 50 pièces**

- Usinage : 50 × 46 = **2 300 €**
- Fonderie : 8 500 + 50 × 7 = 8 500 + 350 = **8 850 €**

→ L'usinage est nettement moins cher.

**2. Pour 1 000 pièces**

- Usinage : 1 000 × 46 = **46 000 €**
- Fonderie : 8 500 + 7 000 = **15 500 €**

→ La fonderie coûte trois fois moins cher.

**3. Le seuil de rentabilité**

On cherche N tel que les deux coûts s'égalisent :
46 N = 8 500 + 7 N → 39 N = 8 500 → **N ≈ 218 pièces**

*En dessous de 218 pièces, on usine. Au-dessus, on moule. Et près du seuil, on regarde les
critères secondaires : délai, souplesse en cas de modification, capacité de l'atelier.*

**4. Surcoût du resserrement**

Surcoût par pièce : 12 € × 3 − 12 € = **24 €**
Sur 1 000 pièces : **24 000 €**

*Vingt-quatre mille euros pour trois tolérances resserrées « par précaution ». C'est très exactement
ce que signifie « 80 % du coût est figé en conception ».*

**5. Comparaison des deux devis**

- Devis A : 200 × 28 = **5 600 €**, délai 8 semaines
- Devis B : 2 400 + 200 × 19 = 2 400 + 3 800 = **6 200 €**, délai 5 semaines

**Sur ce volume, A est moins cher de 600 €**, malgré son prix unitaire plus élevé : l'outillage
de B n'est pas amorti sur 200 pièces.

**Mais** : si une seconde série de 200 pièces est probable, B devient gagnant dès la deuxième
commande (l'outillage étant déjà payé : 3 800 € contre 5 600 €). Et B livre trois semaines plus
tôt.

*La bonne réponse en entreprise : demander au client s'il y aura une réanalyse. Un devis ne se
compare jamais sans connaître l'horizon.*
""",
            "exemple": """
**Cas industriel — Réduire de 40 % le coût d'un support sans changer sa fonction**

Un support de capteur est produit à **2 000 exemplaires par an**. Coût actuel : **31 € la pièce**.
La direction demande de descendre à 20 €. Le bureau d'études reprend le dossier.

**L'analyse du coût actuel**

| Poste | Coût | Observation |
|---|---|---|
| matière : inox X5CrNi18-10 | 9 € | choisi « parce que c'est dans un atelier » |
| usinage 5 faces | 13 € | 3 reprises, donc 3 montages |
| rectification d'une face | 4 € | Ra 0,8 demandé sur un appui boulonné |
| perçages : 4 diamètres différents | 3 € | 4 changements d'outil |
| traitement, contrôle | 2 € | |

**Les six modifications décidées**

1. **Matière** : l'environnement n'est ni humide ni alimentaire → acier S355 zingué.
   *Économie : 6 €.*
2. **Ra 0,8 → Ra 3,2** sur l'appui boulonné : la fonction ne l'exige pas.
   *Économie : 4 € (rectification supprimée).*
3. **Regrouper les usinages** sur 2 faces au lieu de 5, en redessinant la pièce.
   *Économie : 5 €.*
4. **Normaliser les perçages** : 2 diamètres au lieu de 4.
   *Économie : 1,5 €.*
5. **Congés au lieu d'angles vifs** : plus de reprise à l'outil fin.
   *Économie : 1 €.*
6. **Trous oblongs** plutôt que lisses : le réglage au montage remplace une tolérance serrée.
   *Économie : 1 € et un gain de temps au montage.*

**Résultat : 31 € → 12,5 € de gain, soit 18,50 € la pièce.** Objectif dépassé, et
**37 000 € économisés par an**, pour deux jours de travail de bureau d'études.

**Ce que le cas apprend.** Aucune de ces six modifications n'a changé la fonction du support.
Elles ont seulement supprimé des exigences qui n'étaient justifiées par rien — l'habitude, la
précaution, ou l'absence de question. C'est exactement ce qu'on appelle l'**analyse de la
valeur**.
""",
        },
    ],
}


BLOC_11 = {
    "id": 11,
    "titre": "Bloc 11 — Ce qui attend en deuxième année",
    "resume": "Panorama du programme de 2e année et préparation de l'épreuve de projet.",
    "fiches": [
        {
            "id": "11.1",
            "titre": "Panorama de la deuxième année et de l'examen",
            "duree": "4 h",
            "cours": """
### 1. Ce qui change entre la première et la deuxième année

La première année apprend les **outils** : lire un plan, coter, calculer, modéliser, choisir un
matériau. La deuxième année apprend à **les combiner sur un problème réel**, sous contrainte de
temps, en équipe, et à en rendre compte.

Concrètement : moins d'exercices isolés, plus d'études de cas complètes, et un projet qui occupe
une grande partie de l'année.

### 2. Les approfondissements techniques

[[FIG:fibres_flexion]]

**Mécanique et RDM.** On sort des sollicitations simples : sollicitations composées (flexion +
torsion, très fréquent sur un arbre), critères de Tresca et de Von Mises, calcul en fatigue,
flambement approfondi. Et surtout, une notion nouvelle : la **durée de vie**. Un roulement ne se
choisit pas seulement pour qu'il tienne, mais pour qu'il tienne 20 000 heures.

**Transmission de puissance.** Dimensionnement complet des engrenages (module par le calcul, et
non par estimation), trains épicycloïdaux, embrayages et freins, accouplements, choix d'un
motoréducteur sur catalogue.

**Conception de systèmes.** Étanchéité, lubrification, guidages de précision, systèmes
hydrauliques et pneumatiques complets, automatismes simples.

**Modélisation avancée.** Surfacique, tôlerie paramétrée, assemblages de grande taille,
simulation par éléments finis (SolidWorks Simulation) — avec l'esprit critique qui va avec : un
calcul par éléments finis mal posé donne une belle image et un résultat faux.

**Industrialisation.** Gammes complètes, montages d'usinage, cotation de fabrication, chiffrage,
qualité et métrologie tridimensionnelle.

### 3. Le projet : le cœur de la deuxième année

C'est l'épreuve la plus lourde, et celle qui laisse le plus de souvenirs. Un vrai sujet, souvent
proposé par une entreprise, mené en équipe sur plusieurs mois, avec un dossier et une soutenance
devant jury.

Ce qui est évalué : l'analyse du besoin, la pertinence des solutions, la qualité des calculs et
de la CAO, la réalisation, et la capacité à **expliquer ses choix**. Toute la fiche 9.1 et la
fiche 9.3 servent directement ici.

**Le conseil qui compte :** commencez à repérer des sujets et des entreprises **dès la fin de la
première année**. Les binômes qui trouvent un bon sujet tôt travaillent sereinement ; les autres
courent après.

### 4. Le stage

Un stage en entreprise, généralement de 4 à 8 semaines, donne lieu à un rapport et à une
soutenance. Deux conseils :

- **Cherchez tôt.** Les bonnes places partent en janvier pour un stage de printemps.
- **Tenez un carnet dès le premier jour.** Rédiger un rapport de stage trois mois après, de
  mémoire, est un supplice — et le résultat se voit.

### 5. Les épreuves de l'examen

Sans entrer dans le détail réglementaire, qui peut évoluer, la structure générale comporte :

- des épreuves **scientifiques et techniques** (mathématiques, physique, conception) ;
- une épreuve de **conception détaillée** ou de préparation d'une industrialisation ;
- le **projet** avec dossier et soutenance ;
- le **stage** avec rapport ;
- les épreuves **générales** : culture générale et expression, anglais, économie-gestion.

*Le détail exact des coefficients et des durées figure au référentiel officiel du BTS CPI :
c'est le seul document qui fait foi, et il faut le lire une fois en début de deuxième année.*

### 6. Après le BTS

Trois voies, toutes ouvertes :

- **l'emploi direct** : dessinateur-projeteur, technicien bureau d'études, technicien
  méthodes — le BTS CPI est un diplôme qui embauche ;
- **la licence professionnelle** (conception, industrialisation, maintenance) en un an, souvent
  en alternance ;
- **l'école d'ingénieurs** par admission parallèle, ou une classe préparatoire ATS en un an.

### 7. Les cinq conseils pour aborder la deuxième année

1. **Ne pas oublier la première année.** Tout s'appuie dessus : la cotation, la RDM, les
   ajustements reviennent en permanence.
2. **Chercher un sujet de projet tôt.**
3. **Travailler la méthode, pas seulement la technique.** La différence se fait sur l'analyse et
   la restitution.
4. **Soigner l'anglais** : les documentations, les catalogues et beaucoup de logiciels sont en
   anglais.
5. **Se constituer un carnet de références** : les ajustements courants, les formules, les
   ordres de grandeur. C'est ce carnet qui servira ensuite en entreprise.
""",
            "formules": """
**Ce qui revient de la 1re année** — σ = N/S · σ = Mf/(I/v) · Rpe = Re/s · ITja = Σ IT ·
d = m Z · P = C ω · règle des charges des roulements

**Ce qui s'y ajoute en 2e année** — sollicitations composées · Von Mises · durée de vie des
roulements · module d'engrenage calculé · éléments finis

**Le calendrier à anticiper** — sujet de projet repéré en fin de 1re année · stage cherché dès
janvier · référentiel officiel lu en début de 2e année
""",
            "exercice": """
**1.** Cite trois notions de première année dont tu es sûr qu'elles reviendront en deuxième
année, et dis dans quel contexte.

**2.** Un arbre de transmission subit à la fois de la torsion et de la flexion. Pourquoi ne
peut-on pas simplement additionner les deux contraintes ?

**3.** Pourquoi chercher un sujet de projet dès la fin de la première année ?

**4.** Tu dois choisir un roulement pour une machine qui doit fonctionner 8 heures par jour
pendant 10 ans. Quelle notion, absente de la première année, devient indispensable ?

**5.** Cite deux raisons pour lesquelles un calcul par éléments finis peut donner un résultat
faux tout en produisant une image convaincante.
""",
            "corrige": """
**1. Trois notions et leur retour**

- **Les ajustements ISO** : dans tout montage de roulement, d'engrenage, de guidage.
- **La RDM de base** (σ = N/S, σ = Mf/(I/v)) : c'est le socle des sollicitations composées.
- **La cotation fonctionnelle et les chaînes de cotes** : indispensables en cotation de
  fabrication et en contrôle tridimensionnel.

*On pourrait ajouter : le choix des matériaux, les procédés, la méthode de modélisation
paramétrique.*

**2. Parce que σ et τ n'agissent pas dans la même direction**

La contrainte normale de flexion est perpendiculaire à la section ; la contrainte de torsion agit
dans le plan de la section. Les additionner n'aurait pas de sens physique.

On utilise donc un **critère d'équivalence** (Von Mises ou Tresca) qui les combine en une
**contrainte équivalente** comparable à Rpe. Par exemple, selon Von Mises :
σ éq = √(σ² + 3τ²).

*C'est exactement pour cela que la fiche 4.3 précisait qu'on ne vérifie jamais un arbre en
torsion seule.*

**3. Parce que le sujet conditionne toute l'année**

Un bon sujet — problème réel, entreprise motivée, moyens disponibles — permet de travailler
sereinement. Un sujet trouvé en novembre oblige à improviser, et les meilleures entreprises sont
déjà prises.

*Le temps gagné en amont est le seul temps qu'on ne rattrape pas en aval.*

**4. La durée de vie des roulements**

8 h/jour × 250 jours × 10 ans = **20 000 heures** de fonctionnement. Le catalogue permet de
calculer la durée de vie L₁₀ (durée atteinte par 90 % des roulements) en fonction de la charge et
de la vitesse.

En première année, on choisit un roulement qui « tient ». En deuxième année, on choisit un
roulement qui tient **le temps demandé** — c'est ce qui distingue un dimensionnement d'une
estimation.

**5. Deux causes de résultat faux**

- **Les conditions aux limites sont mal posées** : un encastrement modélisé là où la pièce est en
  réalité simplement appuyée change tout le champ de contraintes.
- **Le maillage est trop grossier aux endroits critiques**, précisément là où les contraintes se
  concentrent — congés, gorges, angles.

*On pourrait ajouter : un matériau mal renseigné, une charge appliquée sur une surface trop
grande, ou une interprétation naïve des couleurs sans regarder l'échelle.*

**La règle à retenir : un calcul par éléments finis se vérifie toujours par un calcul à la main
en ordre de grandeur.** Si les deux ne concordent pas, c'est le calcul informatique qui a tort
jusqu'à preuve du contraire.
""",
            "exemple": """
**Cas industriel — Ce qu'on demande vraiment à un technicien en bureau d'études**

Voici, dans le désordre, cinq demandes typiques adressées à un jeune technicien en bureau
d'études, et les compétences que chacune mobilise. C'est l'aboutissement concret des deux années.

**Demande 1 — « Ce carter fuit sur trois machines. Trouve pourquoi. »**
→ Étanchéité, états de surface, tolérances géométriques, analyse de défaillance.
*Compétence clé : remonter d'un symptôme à une cause, sans changer tout au hasard.*

**Demande 2 — « Il faut réduire le prix de cette pièce de 20 %. »**
→ Analyse de la valeur, procédés, cotation, coût de revient.
*Compétence clé : distinguer ce qui est fonctionnel de ce qui est de l'habitude.*

**Demande 3 — « Le client veut la même chose, mais deux fois plus rapide. »**
→ Cinématique, dynamique, dimensionnement moteur, inertie, rigidité.
*Compétence clé : savoir que doubler la vitesse quadruple souvent les efforts d'accélération.*

**Demande 4 — « Ce fournisseur chinois nous envoie ce plan. Il est bon ? »**
→ Lecture de plan, méthode de projection, anglais technique, tolérances.
*Compétence clé : vérifier le symbole de projection avant toute chose.*

**Demande 5 — « Prépare le dossier pour la revue de conception de jeudi. »**
→ Méthodologie de projet, argumentation, communication technique.
*Compétence clé : présenter un raisonnement, pas un résultat.*

**Ce que le cas apprend.** Aucune de ces demandes ne se résout avec une seule matière. Elles
mobilisent toutes, à la fois, la conception, le calcul, les matériaux, les procédés, le coût et
la communication.

C'est précisément pour cela que le programme est organisé en blocs séparés pendant l'année, puis
réuni dans un projet à la fin : les blocs sont un moyen d'apprendre, jamais une façon de
travailler.
""",
        },
    ],
}


BLOCS_COMPLEMENTAIRES = [BLOC_7, BLOC_8, BLOC_9, BLOC_10, BLOC_11]
