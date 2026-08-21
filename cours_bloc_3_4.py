# -*- coding: utf-8 -*-
"""Blocs 3 et 4 du référentiel BTS CPI."""

BLOC_3 = {
    "id": "bloc3",
    "titre": "Bloc 3 — Matériaux : familles, désignation, traitements",
    "resume": "Savoir lire une désignation normalisée, comparer des matériaux et justifier un choix.",
    "fiches": [
        {
            "id": "3.1",
            "titre": "Familles de matériaux et propriétés mécaniques",
            "duree": "8 h",
            "cours": """
### 1. L'essai de traction : la source de tous les chiffres

Toutes les caractéristiques mécaniques d'un métal viennent d'un seul essai normalisé (ISO 6892) :
on tire sur une éprouvette calibrée et on trace la courbe **contrainte / déformation**.

```
σ (MPa)
  │        ╭──────╮
Rm├───────╱        ╲       ← résistance à la rupture
  │      ╱          ╲
Re├────╱  ← limite    ╲✕   ← rupture
  │   ╱     élastique
  │  ╱ ← domaine élastique (pente = E)
  │ ╱
  └────────────────────── ε (%)
        A% ────────────►
```

**Deux domaines à distinguer absolument :**

- **Domaine élastique** (jusqu'à $R_e$) : la déformation est **réversible**. On relâche, la pièce
  revient à sa forme initiale. La pente de la droite est le **module de Young E**.
- **Domaine plastique** (au-delà de $R_e$) : la déformation est **permanente**. La pièce reste
  déformée. En conception mécanique, **on n'y va jamais** (sauf en emboutissage, où c'est le but).

### 2. Les cinq grandeurs à connaître

| Grandeur | Symbole | Unité | Signification |
|---|---|---|---|
| **Limite élastique** | $R_e$ ou $R_{p0,2}$ | MPa | Contrainte au-delà de laquelle la déformation devient permanente. **C'est LA valeur de dimensionnement.** |
| **Résistance à la rupture** | $R_m$ | MPa | Contrainte maximale supportée avant striction et rupture. |
| **Module de Young** | $E$ | MPa ou GPa | **Rigidité** du matériau. Gouverne les déformations, pas la résistance. |
| **Allongement à la rupture** | $A$ | % | **Ductilité**. Un A élevé = matériau qui prévient avant de casser. |
| **Masse volumique** | $\\rho$ | kg/m³ | Détermine la masse de la pièce. |

**Le piège conceptuel à éliminer dès maintenant :**

> **E (rigidité) et Re (résistance) sont deux choses totalement indépendantes.**
> Tous les aciers, du S235 au 42CrMo4 trempé, ont **le même E ≈ 210 GPa**.
> Remplacer un S235 par un acier à haute résistance **ne réduit PAS la flèche d'une poutre** —
> ça permet seulement de supporter une charge plus forte avant déformation permanente.
> Pour réduire une flèche, on change la **géométrie** (inertie), pas la nuance.

### 3. Les grandes familles

**a) Aciers** (Fe + C < 2,1 %) — E ≈ 210 GPa, ρ = 7850 kg/m³
Le matériau de référence : bon compromis résistance/coût/usinabilité, soudable, traitable
thermiquement. Se corrode (sauf inox).

**b) Fontes** (Fe + C de 2,1 à 6,7 %) — E ≈ 110 à 170 GPa, ρ ≈ 7200 kg/m³
Excellente coulabilité (formes complexes), très bon amortissement des vibrations, bonne
usinabilité. **Fragile** en fonte grise (A ≈ 0 %). Bâtis de machines-outils, carters.

**c) Alliages d'aluminium** — E ≈ 70 GPa, ρ = 2700 kg/m³
**Trois fois plus léger que l'acier**, mais aussi **trois fois moins rigide**. Excellente
conductivité thermique, résistant à la corrosion (couche d'alumine). Aéronautique, carters,
profilés.

**d) Alliages cuivreux** — laitons (Cu-Zn), bronzes (Cu-Sn), ρ ≈ 8500 kg/m³
Excellent **coefficient de frottement** contre l'acier → coussinets, bagues de guidage.
Très bonne conductivité électrique et thermique. Chers.

**e) Polymères** — E ≈ 1 à 3,5 GPa, ρ ≈ 900 à 1400 kg/m³
Très légers, autolubrifiants, isolants, moulables en grande série à faible coût. Faible
résistance, **fluage** sous charge permanente, sensibles à la température et aux UV.

**f) Composites** (fibre + matrice) — propriétés **anisotropes**
Rapport résistance/masse exceptionnel dans le sens des fibres. Coût élevé, réparation difficile,
recyclage problématique.

### 4. Le raisonnement de choix : les indices de performance

On ne choisit pas « le plus résistant » mais **le meilleur rapport pour la contrainte dominante** :

| Objectif | Indice à maximiser |
|---|---|
| Pièce **légère et résistante** (traction) | $R_e / \\rho$ |
| Pièce **légère et rigide** (traction) | $E / \\rho$ |
| **Poutre** légère et rigide (flexion) | $E^{1/2} / \\rho$ |
| **Plaque** légère et rigide | $E^{1/3} / \\rho$ |
| **Ressort** (énergie élastique max) | $R_e^2 / E$ |
""",
            "formules": """
**Contrainte normale (traction / compression)**

$$ \\sigma = \\frac{F}{S} \\qquad [\\mathrm{MPa}] = \\frac{[\\mathrm{N}]}{[\\mathrm{mm^2}]} $$

⚠️ **Unité cohérente essentielle : 1 MPa = 1 N/mm².** En travaillant en **newtons** et
**millimètres**, le résultat sort directement en MPa. C'est la convention à adopter partout.

**Déformation relative (allongement unitaire)**

$$ \\varepsilon = \\frac{\\Delta L}{L_0} \\qquad \\text{(sans unité, ou en \\%)} $$

**Loi de Hooke** (valable uniquement dans le domaine élastique)

$$ \\boxed{\\sigma = E \\cdot \\varepsilon} \\;\\Longrightarrow\\; \\Delta L = \\frac{F \\cdot L_0}{E \\cdot S} $$

**Allongement à la rupture**

$$ A\\% = \\frac{L_u - L_0}{L_0} \\times 100 $$

**Coefficient de Poisson** (contraction transversale)

$$ \\nu = -\\frac{\\varepsilon_{transversal}}{\\varepsilon_{longitudinal}} \\qquad \\nu \\approx 0,3 \\;(\\text{acier}) $$

**Module de cisaillement (module de Coulomb)**

$$ G = \\frac{E}{2(1+\\nu)} \\qquad \\Rightarrow \\qquad G_{acier} \\approx \\frac{210\\,000}{2,6} \\approx 80\\,000\\ \\mathrm{MPa} $$

**Dilatation thermique**

$$ \\Delta L = \\alpha \\cdot L_0 \\cdot \\Delta T $$

| Matériau | $\\alpha$ (×10⁻⁶ K⁻¹) |
|---|---|
| Acier | 11 à 12 |
| Fonte | 10 |
| Aluminium | 23 |
| Laiton | 19 |
| Polymères | 70 à 150 |

**Masse d'une pièce**

$$ m = \\rho \\cdot V \\qquad [\\mathrm{kg}] = [\\mathrm{kg/m^3}] \\times [\\mathrm{m^3}] $$

**Valeurs de référence à mémoriser**

| Matériau | $R_e$ (MPa) | $R_m$ (MPa) | $E$ (GPa) | $\\rho$ (kg/m³) | $A$ (%) |
|---|---|---|---|---|---|
| S235 | 235 | 360-510 | 210 | 7850 | 26 |
| S355 | 355 | 470-630 | 210 | 7850 | 22 |
| C45 (normalisé) | 340 | 620-750 | 210 | 7850 | 16 |
| 42CrMo4 (trempé revenu) | 750 | 1000-1200 | 210 | 7850 | 11 |
| X5CrNi18-10 (inox 304) | 210 | 520-720 | 200 | 7900 | 45 |
| EN-GJL-250 (fonte grise) | — | 250 | 110 | 7200 | ≈0 |
| EN-GJS-500-7 (fonte GS) | 320 | 500 | 169 | 7100 | 7 |
| EN AW-6060 T6 | 150 | 190 | 69 | 2700 | 8 |
| EN AW-7075 T6 | 470 | 540 | 71 | 2810 | 7 |
| TA6V (titane) | 830 | 900 | 114 | 4430 | 10 |
| PA6-6 | — | 80 | 3,0 | 1140 | 50 |
| POM-C | — | 68 | 2,8 | 1410 | 35 |
""",
            "exemple": """
**Cas industriel — Alléger un bras de robot : acier ou aluminium ?**

Un bras de manipulateur de 800 mm de long, de section carrée creuse, subit une charge en bout.
Le bureau d'études veut réduire la masse mobile pour augmenter la cadence. Deux candidats :

| | **S355** | **EN AW-6082 T6** |
|---|---|---|
| $R_e$ | 355 MPa | 260 MPa |
| $E$ | 210 GPa | 70 GPa |
| $\\rho$ | 7850 kg/m³ | 2700 kg/m³ |
| $R_e/\\rho$ | **0,045** | **0,096** ✅ |
| $E/\\rho$ | 0,0268 | **0,0259** ≈ |
| $E^{1/2}/\\rho$ (flexion) | 0,0584 | **0,0980** ✅ |

**Lecture des indices — c'est le cœur du raisonnement :**

- Pour la **résistance** ($R_e/\\rho$) : l'aluminium est **2,1 fois meilleur**. À résistance égale,
  la pièce alu sera 2 fois plus légère.
- Pour la **rigidité en traction** ($E/\\rho$) : les deux sont **quasi équivalents**. C'est
  contre-intuitif, mais l'alu est 3× moins rigide **et** 3× moins dense : ça se compense exactement.
  *Retenir : à masse égale, une barre en alu et une barre en acier ont la même raideur en traction.*
- Pour la **rigidité en flexion** ($E^{1/2}/\\rho$) : l'aluminium est **1,7 fois meilleur**, parce
  qu'à masse égale on peut lui donner une section **plus épaisse**, et l'inertie croît en $h^3$.

**Décision du BE : EN AW-6082 T6.**

Résultat chiffré du redimensionnement : tube 60×60×5 en alu (masse 2,4 kg) au lieu de 50×50×3 en
acier (masse 3,5 kg), **à flèche identique** et avec un coefficient de sécurité supérieur.
Gain : **31 % de masse mobile**, ce qui permet d'augmenter l'accélération du robot de 20 %.

**Contreparties acceptées :** coût matière 3× supérieur (mais faible part du coût total),
soudage plus délicat (on passe au boulonnage), et **pas de limite d'endurance** en fatigue pour
l'aluminium — il faudra dimensionner sur une durée de vie finie, pas à l'infini.
""",
            "exercice": """
**Exercice type examen — Tirant de suspension**

Un tirant cylindrique plein soutient une charge suspendue. Données :
- Charge : $F = 45\\ \\mathrm{kN}$
- Longueur libre : $L_0 = 2\\,500\\ \\mathrm{mm}$
- Matériau envisagé : **S355** ($R_e = 355$ MPa, $E = 210$ GPa, $\\rho = 7850$ kg/m³)
- Coefficient de sécurité imposé : $s = 3$
- L'allongement sous charge ne doit pas dépasser **2 mm**

**Questions :**

1. Calculer la contrainte pratique admissible $R_{pe}$.
2. Déterminer la section minimale nécessaire pour satisfaire la condition de **résistance**,
   puis le diamètre correspondant. Choisir un diamètre normalisé supérieur.
3. Vérifier la condition de **rigidité** (allongement ≤ 2 mm) avec ce diamètre.
4. Si la condition de rigidité n'est pas satisfaite, déterminer le diamètre minimal qui la satisfait.
5. Calculer la masse du tirant retenu.
6. Le BE propose de passer en **42CrMo4** ($R_e = 750$ MPa, $E = 210$ GPa) pour alléger.
   Recalculer les deux conditions et conclure sur la pertinence de cette proposition.
""",
            "corrige": """
**1. Contrainte pratique admissible**

$$ R_{pe} = \\frac{R_e}{s} = \\frac{355}{3} = \\mathbf{118,3\\ \\mathrm{MPa}} $$

---

**2. Condition de RÉSISTANCE**

Condition à satisfaire : $\\sigma_{max} \\le R_{pe}$, avec $\\sigma = \\dfrac{F}{S}$

$$ \\frac{F}{S} \\le R_{pe} \\;\\Longrightarrow\\; S \\ge \\frac{F}{R_{pe}} = \\frac{45\\,000}{118,3} = 380,4\\ \\mathrm{mm^2} $$

Section circulaire : $S = \\dfrac{\\pi d^2}{4}$

$$ d \\ge \\sqrt{\\frac{4S}{\\pi}} = \\sqrt{\\frac{4 \\times 380,4}{\\pi}} = \\sqrt{484,4} = 22,0\\ \\mathrm{mm} $$

**Diamètre normalisé retenu : Ø25 mm** (série Renard R20 ; on ne prend pas Ø22 qui est trop juste).

$$ S_{réelle} = \\frac{\\pi \\times 25^2}{4} = \\mathbf{490,9\\ \\mathrm{mm^2}} $$

Vérification :
$$ \\sigma = \\frac{45\\,000}{490,9} = 91,7\\ \\mathrm{MPa} \\;\\le\\; 118,3\\ \\mathrm{MPa} \\quad ✔️ $$

Coefficient de sécurité réel : $s_{réel} = \\dfrac{355}{91,7} = \\mathbf{3,87}$

---

**3. Condition de RIGIDITÉ (Ø25)**

Loi de Hooke :
$$ \\Delta L = \\frac{F \\cdot L_0}{E \\cdot S} = \\frac{45\\,000 \\times 2\\,500}{210\\,000 \\times 490,9} $$

$$ \\Delta L = \\frac{112\\,500\\,000}{103\\,089\\,000} = \\mathbf{1,09\\ \\mathrm{mm}} $$

$$ 1,09\\ \\mathrm{mm} \\;\\le\\; 2\\ \\mathrm{mm} \\quad ✔️ \\;\\; \\textbf{CONDITION SATISFAITE} $$

**Conclusion : le Ø25 en S355 convient pour les deux conditions.** C'est la **résistance** qui a
été dimensionnante ici (elle imposait Ø22 alors que la rigidité seule aurait suffi avec un
diamètre plus petit — voir Q4).

---

**4. Diamètre minimal pour la seule condition de rigidité**

$$ \\Delta L \\le 2 \\;\\Longrightarrow\\; S \\ge \\frac{F \\cdot L_0}{E \\cdot \\Delta L_{max}} = \\frac{45\\,000 \\times 2\\,500}{210\\,000 \\times 2} $$

$$ S \\ge \\frac{112\\,500\\,000}{420\\,000} = 267,9\\ \\mathrm{mm^2} \\;\\Longrightarrow\\; d \\ge \\sqrt{\\frac{4 \\times 267,9}{\\pi}} = 18,5\\ \\mathrm{mm} $$

La rigidité seule imposerait **Ø18,5 mm**, la résistance imposait **Ø22,0 mm**.

$$ \\boxed{\\text{C'est la RÉSISTANCE qui dimensionne : } d_{min} = 22,0 \\to \\text{Ø25 retenu}} $$

---

**5. Masse du tirant**

$$ V = S \\times L_0 = 490,9 \\times 2\\,500 = 1\\,227\\,185\\ \\mathrm{mm^3} = 1,227 \\times 10^{-3}\\ \\mathrm{m^3} $$

$$ m = \\rho \\cdot V = 7\\,850 \\times 1,227\\times10^{-3} = \\mathbf{9,63\\ \\mathrm{kg}} $$

---

**6. Passage en 42CrMo4 — analyse critique**

**Condition de résistance :**
$$ R_{pe} = \\frac{750}{3} = 250\\ \\mathrm{MPa} \\;\\Longrightarrow\\; S \\ge \\frac{45\\,000}{250} = 180\\ \\mathrm{mm^2} $$
$$ d \\ge \\sqrt{\\frac{4 \\times 180}{\\pi}} = 15,1\\ \\mathrm{mm} $$

**Condition de rigidité :** $E$ est **inchangé** (210 GPa — c'est le point clé) :
$$ d \\ge \\mathbf{18,5\\ \\mathrm{mm}} \\quad \\text{(valeur identique à la Q4)} $$

**Le dimensionnement bascule : c'est désormais la RIGIDITÉ qui commande.**

Diamètre normalisé retenu : **Ø20 mm** ($S = 314,2\\ \\mathrm{mm^2}$)

Vérifications :
- Résistance : $\\sigma = \\dfrac{45\\,000}{314,2} = 143,2$ MPa $\\le 250$ MPa ✔️ ($s_{réel} = 5,2$)
- Rigidité : $\\Delta L = \\dfrac{45\\,000 \\times 2\\,500}{210\\,000 \\times 314,2} = 1,70$ mm $\\le 2$ mm ✔️

**Masse :** $m = 7\\,850 \\times 314,2 \\times 2\\,500 \\times 10^{-9} = \\mathbf{6,17\\ kg}$

**Bilan de la proposition :**

| | S355 Ø25 | 42CrMo4 Ø20 |
|---|---|---|
| Masse | 9,63 kg | **6,17 kg** (−36 %) |
| Allongement | 1,09 mm | 1,70 mm (+56 %) |
| Coeff. sécurité réel | 3,87 | 5,2 |
| Coût matière relatif | 1 | ≈ 3,5 |
| Soudabilité | Bonne | Médiocre (0,42 % C → préchauffage obligatoire) |

**Conclusion — la proposition est techniquement valide mais économiquement discutable :**

Le gain de masse est réel (−3,5 kg) mais **plafonné par la rigidité** : on ne peut pas descendre
sous Ø18,5 quelle que soit la nuance, puisque **tous les aciers ont le même module de Young**.
Le 42CrMo4 offre $R_e$ deux fois supérieur, mais on n'en exploite **qu'une partie** — le
coefficient de sécurité réel grimpe inutilement à 5,2.

**Recommandation :** conserver le **S355 Ø25** si la masse n'est pas critique (structure fixe :
3,5 kg n'ont aucune importance, et le S355 est 3,5× moins cher et soudable). N'envisager le
42CrMo4 que si le tirant est une **pièce mobile** dont la masse pénalise les performances, ou
s'il subit de la **fatigue** — domaine où sa limite d'endurance élevée devient le vrai argument.
""",
        },
        {
            "id": "3.2",
            "titre": "Désignation normalisée des matériaux",
            "duree": "6 h",
            "cours": """
### 1. Pourquoi une désignation normalisée

Écrire « acier dur » sur un plan n'a aucune valeur contractuelle. La désignation normalisée
(EN 10027) permet à un fournisseur en Algérie, en Chine ou en Allemagne de livrer **exactement**
le même matériau. **La désignation fait partie de la définition de la pièce, au même titre que
les cotes.**

### 2. Aciers d'usage général — désignation par la limite élastique

Format : **S** ou **E** + valeur de $R_e$ en MPa

- **S** = *Structural* (construction, charpente)
- **E** = *Engineering* (construction mécanique)
- **P** = appareils à pression, **L** = tubes de conduite

**Exemples :**
- **S235** → acier de construction, $R_e = 235$ MPa
- **S355JR** → $R_e = 355$ MPa ; **JR** = résilience 27 J à +20 °C
- **E335** → acier de construction mécanique, $R_e = 335$ MPa

Suffixes de résilience : **JR** (27 J à 20 °C), **J0** (27 J à 0 °C), **J2** (27 J à −20 °C),
**K2** (40 J à −20 °C).

### 3. Aciers non alliés spéciaux — désignation par le carbone

Format : **C** + (%C × 100)

- **C22** → 0,22 % de carbone. Cémentation, pièces peu sollicitées.
- **C35** → 0,35 % C. Compromis courant.
- **C45** → 0,45 % C. **Le plus utilisé en mécanique** : arbres, axes, engrenages.
- **C60** → 0,60 % C. Ressorts, outillage.

**Règle physique fondamentale :** plus %C augmente → **dureté et $R_e$ augmentent**, mais
**ductilité (A%), soudabilité et usinabilité diminuent**.

**Seuil de soudabilité : 0,25 % de carbone.** Au-delà, préchauffage obligatoire.

### 4. Aciers faiblement alliés (aucun élément ≥ 5 %)

Format : **(%C × 100) + symboles des éléments + teneurs × facteur**

Facteurs multiplicateurs (à connaître) :

| Éléments | Facteur |
|---|---|
| Cr, Co, Mn, Ni, Si, W | **× 4** |
| Al, Be, Cu, Mo, Nb, Pb, Ta, Ti, V, Zr | **× 10** |
| Ce, N, P, S | **× 100** |
| B | **× 1000** |

**Décodage de 42CrMo4 :**
- **42** → 42/100 = **0,42 % de carbone**
- **Cr** → chrome, premier élément cité donc le plus abondant
- **Mo** → molybdène
- **4** → se rapporte au **premier élément listé (Cr)** : 4/4 = **1 % de chrome**
- Le Mo est présent en faible quantité (non chiffrée car < seuil), typiquement 0,2 %

→ *Acier à 0,42 % C, 1 % Cr, traces de Mo.* Acier de traitement thermique par excellence
(arbres de transmission, vilebrequins).

**Autres à connaître :**
- **16MnCr5** → 0,16 % C, 1,25 % Mn (5/4), Cr. **Acier de cémentation** : cœur tenace, peau dure.
- **34CrMo4** → 0,34 % C, 1 % Cr, Mo. Version moins dure du 42CrMo4.
- **100Cr6** → 1 % C, 1,5 % Cr. **L'acier des roulements** (62 HRC après trempe).
- **35NiCrMo16** → 0,35 % C, 4 % Ni, Cr, Mo. Aciers à très haute résistance.

### 5. Aciers fortement alliés (au moins un élément ≥ 5 %)

Format : **X** + (%C × 100) + éléments + **teneurs réelles en %** (pas de facteur)

**Décodage de X5CrNi18-10 :**
- **X** → acier fortement allié
- **5** → 0,05 % C
- **Cr 18** → 18 % de chrome
- **Ni 10** → 10 % de nickel

→ C'est l'**inox austénitique 304**, le plus courant. Le chrome ≥ 10,5 % forme une couche passive
d'oxyde de chrome qui protège de la corrosion. Amagnétique, non trempant, très ductile (A = 45 %).

- **X2CrNiMo17-12-2** → inox **316L** : le Mo lui donne une résistance aux chlorures
  (milieu marin, agroalimentaire, médical). Le « 2 » de X2 signale un **très bas carbone**
  (soudabilité sans corrosion intergranulaire).
- **X12Cr13** → inox **martensitique**, trempable, utilisé pour la coutellerie et les axes inox durs.

### 6. Fontes (EN 1560)

Format : **EN-GJ** + type de graphite + caractéristiques

- **L** = lamellaire (fonte grise), **S** = sphéroïdal (fonte ductile), **M** = malléable

**EN-GJL-250** → fonte à graphite **lamellaire**, $R_m = 250$ MPa.
Fragile ($A ≈ 0$), mais **excellente capacité d'amortissement** (le graphite en lamelles absorbe
les vibrations) → bâtis de machines-outils.

**EN-GJS-500-7** → fonte à graphite **sphéroïdal**, $R_m = 500$ MPa, $A = 7$ %.
Le graphite en nodules ne fragilise plus la matrice → fonte **ductile**, presque un acier coulé.
Vilebrequins, moyeux, corps de vannes.

### 7. Aluminium (EN 573)

Format : **EN AW-** + 4 chiffres. Le **premier chiffre** donne la famille :

| Série | Élément principal | Trempant ? | Emploi |
|---|---|---|---|
| **1xxx** | Al pur ≥ 99 % | Non | Électricité, chimie |
| **2xxx** | Cuivre | **Oui** | Aéronautique (2017A = AU4G) |
| **3xxx** | Manganèse | Non | Emboutissage, canettes |
| **5xxx** | Magnésium | Non | Marine, soudage |
| **6xxx** | Mg + Si | **Oui** | **Profilés extrudés** (6060, 6082) |
| **7xxx** | Zinc | **Oui** | Haute résistance (7075) |

**États métallurgiques :** **O** (recuit), **H** (écroui), **T4** (trempé + mûri),
**T6** (trempé + revenu — état de résistance maximale).

**EN AW-6060 T6** → alliage Al-Mg-Si extrudé, trempé et revenu. C'est le matériau des
**profilés rainurés** d'atelier (type 40×40 rainure 8).
""",
            "formules": """
**Décodage systématique — méthode en 3 questions**

```
1. Y a-t-il un X au début ?
   → OUI : acier FORTEMENT allié, teneurs en % RÉEL
   → NON : passer à 2

2. Y a-t-il des symboles chimiques ?
   → OUI : acier FAIBLEMENT allié, appliquer les FACTEURS
   → NON : passer à 3

3. La désignation commence par C ?
   → OUI : acier non allié spécial, %C = nombre / 100
   → NON (S, E, P...) : acier d'usage général, le nombre est Re en MPa
```

**Calcul de la teneur en élément d'alliage (aciers faiblement alliés)**

$$ \\%\\,\\text{élément} = \\frac{\\text{nombre indiqué}}{\\text{facteur}} $$

**Carbone équivalent — soudabilité** (formule IIW, à connaître)

$$ C_{eq} = \\%C + \\frac{\\%Mn}{6} + \\frac{\\%Cr + \\%Mo + \\%V}{5} + \\frac{\\%Ni + \\%Cu}{15} $$

| $C_{eq}$ | Soudabilité |
|---|---|
| < 0,40 | Bonne, sans précaution |
| 0,40 à 0,60 | Préchauffage recommandé (100-200 °C) |
| > 0,60 | Difficile : préchauffage + post-chauffage obligatoires |

**Relation empirique dureté / résistance (aciers)**

$$ R_m \\approx 3,3 \\times HB \\qquad [\\mathrm{MPa}] $$

*Exemple : un acier à 200 HB a un $R_m \\approx 660$ MPa.*

**Conversion approximative HRC → HB** (domaine 20-40 HRC)

$$ HB \\approx 6 \\times HRC + 100 $$
""",
            "exemple": """
**Cas industriel — Lire une nomenclature de réducteur et comprendre chaque choix**

| Rep | Désignation | Décodage | Pourquoi ce matériau ? |
|---|---|---|---|
| 1 | Carter — **EN-GJL-250** | Fonte grise lamellaire, $R_m$ = 250 MPa | Forme complexe → moulage. Le graphite lamellaire **amortit les vibrations d'engrènement** : le réducteur est silencieux. Fragilité sans conséquence (pièce peu sollicitée). |
| 2 | Arbre d'entrée — **42CrMo4 trempé revenu** | 0,42 % C, 1 % Cr, Mo | Subit **torsion + flexion alternée** → fatigue. Le traitement porte $R_e$ à 750 MPa avec $A$ = 11 % (reste tenace). |
| 3 | Pignon — **16MnCr5 cémenté trempé** | 0,16 % C, 1,25 % Mn, Cr | **Cémentation** : peau à 0,8 % C durcie à 60 HRC (résiste à la pression de contact des dents), **cœur à 0,16 % C resté tenace** (encaisse les chocs sans casser). Un acier dur à cœur casserait net. |
| 4 | Coussinet — **CuSn8** | Bronze à 8 % étain | Faible coefficient de frottement contre l'acier, tolère un défaut de lubrification. **Sacrificiel** : c'est le coussinet qui s'use, pas l'arbre. |
| 5 | Bague de roulement — **100Cr6** | 1 % C, 1,5 % Cr | 62 HRC après trempe. Résiste à la **pression hertzienne** de plusieurs GPa sous les billes. |
| 6 | Joint — **NBR** | Nitrile | Élastomère résistant aux huiles minérales. |
| 7 | Vis CHc — **acier classe 8.8** | $R_m$ = 800 MPa, $R_e$ = 640 MPa | Classe normalisée ISO 898-1 : le premier chiffre × 100 = $R_m$ ; le produit des deux × 10 = $R_e$. |

**Le raisonnement transversal à retenir :** chaque pièce reçoit **le matériau minimal qui remplit
sa fonction**. Mettre du 42CrMo4 partout coûterait 4× plus cher, rendrait le carter infondable et
le coussinet abrasif pour l'arbre. **Un bon choix matériau, c'est souvent le moins cher qui passe.**

**Vérification de soudabilité du 42CrMo4** (si on voulait souder l'arbre) :

$$ C_{eq} = 0,42 + \\frac{0,75}{6} + \\frac{1,0 + 0,2}{5} = 0,42 + 0,125 + 0,24 = \\mathbf{0,785} $$

$C_{eq} > 0,60$ → **soudage difficile**, préchauffage à 250-300 °C et post-chauffage obligatoires.
D'où la règle du BE : *on ne soude pas un arbre de transmission, on l'usine dans la masse.*
""",
            "exercice": """
**Exercice type examen — Décodage et choix de matériau**

**Partie A — Décodage.** Pour chaque désignation, indiquer la famille, la composition et un emploi typique :

1. **S275JR**
2. **C40**
3. **25CrMo4**
4. **X6Cr17**
5. **EN-GJS-400-15**
6. **EN AW-2017A T4**
7. **51CrV4**

**Partie B — Soudabilité.** Un bureau d'études souhaite souder un support en **25CrMo4**
(composition : 0,25 % C ; 0,7 % Mn ; 1,0 % Cr ; 0,25 % Mo).
1. Calculer le carbone équivalent.
2. Conclure sur les précautions de soudage.
3. Proposer une nuance de substitution soudable sans précaution, de $R_e$ comparable.

**Partie C — Choix.** On doit concevoir l'**axe d'articulation** d'un vérin de benne de camion :
Ø30 mm, longueur 180 mm, subit un effort de cisaillement alterné de 60 kN, exposé à la pluie et
au sel de déneigement, sans possibilité de graissage régulier.
Proposer un matériau **et un traitement**, en justifiant par au moins trois critères.
""",
            "corrige": """
**PARTIE A — Décodage**

**1. S275JR**
- Famille : **acier d'usage général** (pas de X, pas de symbole chimique, commence par S)
- $R_e = 275$ MPa ; **JR** = résilience 27 J à +20 °C
- Emploi : charpente, mécano-soudure, châssis. Soudable sans précaution.

**2. C40**
- Famille : **acier non allié spécial** (commence par C)
- Composition : **0,40 % de carbone**
- Emploi : axes, arbres, pièces de mécanique générale traitables (trempe possible).
- $C = 0,40 > 0,25$ → soudabilité limitée, préchauffage conseillé.

**3. 25CrMo4**
- Famille : **acier faiblement allié** (symboles chimiques, pas de X)
- **25** → 0,25 % C
- **Cr** premier élément, **4** s'y rapporte, facteur 4 → **1 % de chrome**
- **Mo** → molybdène en faible teneur (≈ 0,25 %)
- Emploi : pièces de sécurité traitées, boulonnerie haute résistance, tubes hydrauliques.

**4. X6Cr17**
- Famille : **acier fortement allié** (commence par X) → teneurs en **% réel**
- **6** → 0,06 % C ; **Cr 17** → **17 % de chrome**
- Pas de nickel → c'est un **inox ferritique (type 430)**, magnétique, non trempant.
- Emploi : électroménager, décoration, échappement. Moins cher que le 304 (pas de nickel), mais
  résistance à la corrosion moindre et emboutissabilité limitée.

**5. EN-GJS-400-15**
- Famille : **fonte à graphite sphéroïdal** (GJ **S**)
- $R_m = 400$ MPa ; $A = 15$ %
- Emploi : pièces moulées **ductiles** — corps de vanne, moyeux, bras de suspension.
- Le fort allongement (15 %) en fait une fonte « ferritique », privilégiant la ténacité sur la dureté.

**6. EN AW-2017A T4**
- Famille : **alliage d'aluminium série 2xxx** → élément principal **cuivre** (ancien AU4G)
- État **T4** : mise en solution + trempe + **maturation naturelle** à température ambiante
- $R_e \\approx 280$ MPa, $R_m \\approx 430$ MPa — parmi les alu les plus résistants
- Emploi : pièces d'aéronautique, boulonnerie alu, décolletage.
- ⚠️ **Point important : mauvaise résistance à la corrosion** (le cuivre crée des piles
  galvaniques) et **non soudable**. Nécessite anodisation ou placage.

**7. 51CrV4**
- Famille : **acier faiblement allié**
- **51** → 0,51 % C ; **Cr** premier élément, **4** → 1 % Cr ; **V** → vanadium (≈ 0,15 %)
- Emploi : **acier à ressorts** par excellence (lames de suspension, ressorts de soupape, outillage
  à main). Le vanadium affine le grain et améliore la tenue en fatigue.

---

**PARTIE B — Soudabilité du 25CrMo4**

**1. Carbone équivalent (formule IIW)**

$$ C_{eq} = \\%C + \\frac{\\%Mn}{6} + \\frac{\\%Cr + \\%Mo + \\%V}{5} + \\frac{\\%Ni + \\%Cu}{15} $$

$$ C_{eq} = 0,25 + \\frac{0,70}{6} + \\frac{1,0 + 0,25 + 0}{5} + 0 $$

$$ C_{eq} = 0,25 + 0,1167 + 0,25 = \\mathbf{0,617} $$

**2. Conclusion sur le soudage**

$$ C_{eq} = 0,617 > 0,60 \\;\\Rightarrow\\; \\textbf{soudabilité DIFFICILE} $$

Précautions **obligatoires** :
- **Préchauffage à 200-250 °C** avant soudage, maintenu pendant toute l'opération
- **Électrodes basiques** à très bas hydrogène (type E7018), étuvées avant emploi
- **Post-chauffage / détensionnement** à 600-650 °C après soudage
- Refroidissement lent, sous couverture isolante

*Risque encouru sans ces précautions :* la zone affectée thermiquement refroidit vite et
**trempe spontanément** → formation de **martensite fragile** → **fissuration à froid** (retardée,
parfois 48 h après soudage). C'est un mode de rupture brutal et sans avertissement.

**3. Nuance de substitution**

Le 25CrMo4 recuit a $R_e \\approx 400$ MPa. Nuance soudable de résistance comparable :

> **S460ML** (acier de construction thermomécanique, $R_e = 460$ MPa)
> Composition typique : 0,16 % C max ; 1,7 % Mn ; microalliage Nb/V/Ti.
>
> $$ C_{eq} \\approx 0,16 + \\frac{1,7}{6} + \\frac{0,1}{5} = 0,16 + 0,283 + 0,02 = \\mathbf{0,463} $$
>
> $C_{eq} < 0,50$ → **soudable avec un préchauffage léger, voire sans** pour de faibles épaisseurs.

Le procédé thermomécanique obtient une haute limite élastique par **affinement du grain**
(loi de Hall-Petch) plutôt que par la teneur en carbone — d'où la soudabilité conservée.

---

**PARTIE C — Choix pour l'axe d'articulation de benne**

**Analyse des contraintes du cahier des charges :**

| Sollicitation | Conséquence sur le choix |
|---|---|
| Cisaillement **alterné** 60 kN | → **fatigue** : il faut une haute limite d'endurance, un état de surface soigné, pas d'entaille vive |
| Pluie + **sel de déneigement** | → corrosion sévère, milieu chloruré |
| **Pas de graissage** régulier | → contact acier/acier semi-sec, risque de **grippage et matage** |
| Pièce de **sécurité** (benne levée) | → coefficient de sécurité élevé, ténacité indispensable |

**Solution proposée : 42CrMo4 trempé revenu + chromage dur (ou nitruration).**

**Justification par les trois critères demandés :**

**1) Résistance mécanique et fatigue**
$R_e = 750$ MPa après traitement. Vérification rapide en cisaillement :
$$ S = \\frac{\\pi \\times 30^2}{4} = 706,9\\ \\mathrm{mm^2} \\;;\\; \\tau = \\frac{60\\,000}{706,9} = 84,9\\ \\mathrm{MPa} $$
Avec $R_{eg} \\approx 0,6 \\times R_e = 450$ MPa, le coefficient de sécurité vaut
$s = 450 / 84,9 = \\mathbf{5,3}$ — cohérent pour une pièce de sécurité en fatigue.
Le $A = 11$ % conservé garantit que l'axe **se déforme avant de rompre** (rupture ductile,
avertissement visible), au lieu de casser net.

**2) Tenue à la corrosion et au frottement**
Le 42CrMo4 nu rouillerait en une saison. Le **chromage dur** (épaisseur 20 à 50 µm, dureté
1000 HV) apporte simultanément :
- une **barrière à la corrosion** ;
- une **dureté de surface** qui résiste au matage sous 60 kN ;
- un **faible coefficient de frottement** (0,15 contre 0,6 pour acier/acier sec), ce qui compense
  l'absence de graissage.

**3) Coût et disponibilité**
Le 42CrMo4 est une nuance **de stock**, disponible en barres calibrées chez tout distributeur.
Le chromage dur est un traitement industriel courant et peu coûteux (quelques euros par pièce).

**Alternatives écartées — et pourquoi :**

| Solution | Motif du rejet |
|---|---|
| **Inox X5CrNi18-10** | $R_e$ = 210 MPa seulement → il faudrait Ø56 mm. De plus, l'inox austénitique **grippe** violemment contre l'acier en l'absence de lubrification (adhésion à froid). |
| **C45 trempé** | $R_e$ insuffisant en fatigue et **aucune** résistance à la corrosion. |
| **Inox X12Cr13 trempé** | Bon compromis résistance/corrosion, mais tenue aux **chlorures** médiocre (inox martensitique) → piqûration sous le sel. |
| **TA6V (titane)** | Excellent techniquement, mais coût matière ×15 et usinage difficile : injustifiable pour une benne de camion. |

**Recommandation complémentaire au BE :** prévoir un **rayon de raccordement** généreux
(R ≥ 2 mm) sous la tête de l'axe, et proscrire toute gorge à angle vif. En fatigue, c'est le
**coefficient de concentration de contrainte** qui tue la pièce, bien plus que le choix de nuance.
""",
        },
        {
            "id": "3.3",
            "titre": "Traitements thermiques et traitements de surface",
            "duree": "6 h",
            "cours": """
### 1. Le principe : modifier les propriétés sans changer la nuance

Un C45 peut avoir $R_e = 340$ MPa (à l'état normalisé) ou $R_e = 660$ MPa (trempé revenu) :
**c'est le même acier**. Le traitement thermique modifie la **structure cristalline**, donc les
propriétés mécaniques, sans toucher à la composition chimique.

**Condition indispensable : la trempe n'est efficace qu'à partir de ~0,3 % de carbone.**
Un S235 (0,15 % C) ne trempe pas. C'est pourquoi les pièces à tremper sont en C45, 42CrMo4, etc.

### 2. Les traitements dans la masse

**a) Trempe**
Chauffage au-dessus de 850 °C (domaine austénitique), maintien, puis **refroidissement rapide**
(eau, huile ou air selon la nuance). L'austénite n'a pas le temps de se transformer normalement :
elle se fige en **martensite**, structure très dure et très fragile.
→ Dureté maximale, mais pièce **cassante et sous contraintes internes**. Inutilisable telle quelle.

**b) Revenu** (toujours après une trempe)
Réchauffage **modéré** (150 à 650 °C) suivi d'un refroidissement lent. On « détend » la martensite :
on **perd un peu de dureté** pour **regagner beaucoup de ténacité**.
→ L'ensemble **trempe + revenu** s'appelle **trempe revenu** ou **amélioration**. C'est le
traitement standard des arbres et pièces sollicitées.

| Température de revenu | Effet |
|---|---|
| 150-250 °C | Dureté quasi conservée, léger gain de ténacité (outils, roulements) |
| 400-500 °C | Compromis dureté/ténacité (ressorts) |
| 550-650 °C | Ténacité maximale, dureté modérée (arbres, boulonnerie HR) |

**c) Recuit**
Chauffage puis refroidissement **très lent** (dans le four). Objectif : **adoucir** la pièce,
supprimer les contraintes internes, régénérer le grain, restaurer l'usinabilité.
→ Utilisé **avant usinage** d'une pièce écrouie ou après soudage.

**d) Normalisation**
Chauffage austénitique + refroidissement à l'air calme. Donne une structure **fine et homogène**.
C'est l'état de livraison courant des aciers de construction.

### 3. Les traitements superficiels (durcir la peau, garder le cœur tenace)

**Le problème à résoudre :** un pignon doit avoir une **surface très dure** (pression de contact
des dents) et un **cœur tenace** (chocs). Ces deux exigences sont contradictoires pour un acier
homogène. La solution : traiter **différemment la peau et le cœur**.

**a) Cémentation** (aciers **à bas carbone** : 16MnCr5, 20MnCr5, C10)
On enrichit la peau en carbone à 900-950 °C dans une atmosphère carburante, sur 0,3 à 2 mm de
profondeur, puis on trempe. La peau (0,8 % C) devient martensitique à **58-62 HRC**, le cœur
(0,16 % C) reste à **~30 HRC**, tenace.
→ **Pignons, arbres cannelés, cames.** Le traitement de référence en transmission de puissance.

**b) Nitruration** (aciers **alliés au Cr, Mo, Al** : 42CrMo4, 31CrMoV9)
Diffusion d'azote à **500-520 °C**, sur 0,1 à 0,6 mm. Dureté 1000-1200 HV.
**Avantage majeur : pas de trempe → aucune déformation.** La pièce peut être **usinée et
rectifiée avant** traitement, aux cotes finales.
→ Vilebrequins, vis sans fin, moules d'injection, tiges de vérin.

**c) Trempe superficielle** (par induction ou au chalumeau) — aciers **à 0,4-0,6 % C**
On chauffe très vite la seule couche superficielle et on trempe immédiatement. Pas de
modification chimique, uniquement structurale.
→ Portées d'arbres, chemins de roulement, dents de grande denture.

### 4. Les traitements de surface (revêtements)

| Traitement | Épaisseur | Apport |
|---|---|---|
| **Zingage** (électrolytique) | 5-25 µm | Protection anticorrosion **sacrificielle** (le zinc se corrode à la place de l'acier). Le moins cher. |
| **Galvanisation à chaud** | 50-100 µm | Anticorrosion durable (20-50 ans en extérieur). Charpente, mobilier urbain. |
| **Chromage dur** | 20-100 µm | Dureté 1000 HV, faible frottement, anticorrosion. **Tiges de vérin.** |
| **Nickelage chimique** | 10-50 µm | Dépôt d'épaisseur parfaitement uniforme, y compris dans les alésages. |
| **Anodisation** (aluminium) | 5-25 µm | Épaissit la couche d'alumine naturelle. Dur, isolant, colorable. |
| **Phosphatation** | 5-15 µm | Sous-couche d'accrochage pour peinture, ou aide au rodage. |
| **Peinture / époxy** | 50-200 µm | Anticorrosion + esthétique. Protection **barrière** (une rayure = corrosion locale). |

### 5. Le risque de déformation — un point de conception essentiel

Toute trempe déforme la pièce (le passage en martensite s'accompagne d'une **augmentation de
volume** d'environ 4 %). Conséquences pour le concepteur :

- Prévoir une **surépaisseur de rectification** (0,2 à 0,5 mm) sur les surfaces fonctionnelles.
- **Éviter les variations brutales de section** : elles refroidissent à des vitesses différentes
  → contraintes internes → **tapures de trempe** (fissures).
- Percer les trous **avant** trempe, mais **aléser après**.
- Préférer la **nitruration** quand la précision dimensionnelle est critique.
""",
            "formules": """
**Conversions de dureté (aciers, valeurs approchées)**

$$ R_m \\approx 3,3 \\times HB \\qquad [\\mathrm{MPa}] $$
$$ HB \\approx 6 \\times HRC + 100 \\qquad (\\text{valable de 20 à 40 HRC}) $$
$$ HV \\approx HB \\qquad (\\text{jusqu'à 400 HB environ}) $$

**Échelles de dureté et leur domaine**

| Échelle | Pénétrateur | Domaine | Emploi |
|---|---|---|---|
| **HB** (Brinell) | Bille carbure Ø10 | < 450 HB | Pièces brutes, fontes |
| **HRC** (Rockwell C) | Cône diamant 120° | 20 à 70 HRC | Aciers traités |
| **HV** (Vickers) | Pyramide diamant | Tout domaine | **Couches minces, nitruration** |

**Profondeur conventionnelle de cémentation** (à 550 HV) — loi de diffusion :

$$ e = k \\sqrt{t} $$

où $t$ est la durée de maintien (h) et $k$ un coefficient dépendant de la température
($k \\approx 0,5$ mm·h$^{-1/2}$ à 925 °C).

*Exemple : pour une profondeur de 1 mm à 925 °C → $t = (1/0,5)^2 = 4$ heures.*

**Limite d'endurance en fatigue (estimation)**

$$ \\sigma_D \\approx 0,5 \\times R_m \\quad (\\text{acier, flexion rotative, surface polie}) $$

Corrigée des facteurs réels :

$$ \\sigma_{D,réelle} = \\sigma_D \\times k_s \\times k_t \\times k_f $$

- $k_s$ : facteur d'état de surface (0,7 à 0,9 pour usiné ; 0,4 pour brut de forge)
- $k_t$ : facteur de taille (0,8 à 1 selon le diamètre)
- $k_f$ : facteur de concentration de contrainte (entailles, gorges)

**Gain apporté par un traitement superficiel :** la nitruration et la cémentation introduisent des
**contraintes résiduelles de compression** en surface, qui s'opposent à l'amorçage des fissures.
Gain typique sur la limite d'endurance : **+30 à +80 %**.

**Dilatation lors de la trempe (martensite)**

$$ \\frac{\\Delta V}{V} \\approx 4\\ \\% \\quad \\Rightarrow \\quad \\frac{\\Delta L}{L} \\approx 1,3\\ \\% $$
""",
            "exemple": """
**Cas industriel — Gamme complète d'un pignon de boîte de vitesses**

Pignon Ø80, 24 dents, module 3, en **16MnCr5**. Le bureau des méthodes établit la gamme suivante.
Chaque étape est justifiée par une contrainte physique précise.

| N° | Opération | Pourquoi à ce moment précis |
|---|---|---|
| 10 | Débit barre + **recuit d'adoucissement** | Le laminage a écroui la matière. Le recuit restaure l'usinabilité et évite l'usure prématurée des outils. |
| 20 | Tournage : ébauche + finition, **surépaisseur 0,3 mm** sur alésage et flancs | On usine **tendre** (bien plus rapide et moins coûteux que d'usiner à 60 HRC). La surépaisseur compense la déformation à venir. |
| 30 | Taillage de la denture (fraise-mère) | Idem : tailler dans du dur est impossible en production. |
| 40 | **CÉMENTATION** 925 °C, 4 h → profondeur 1 mm | Enrichit la peau à 0,8 % C. La denture et l'alésage sont concernés. |
| 45 | **Protection** de l'alésage par cuivrage | ⚠️ On **ne veut pas** durcir l'alésage : il doit rester usinable et tenace pour le montage serré sur l'arbre. Le cuivre bloque la diffusion du carbone. |
| 50 | **TREMPE** huile 850 °C | La peau enrichie devient martensite à 60 HRC ; le cœur à 0,16 % C reste à ~30 HRC. |
| 60 | **REVENU** 180 °C, 2 h | Élimine les contraintes de trempe et l'austénite résiduelle **sans perdre la dureté**. À 180 °C on conserve 58-60 HRC. |
| 70 | **Rectification** de l'alésage et des flancs de dents | Reprend les 0,3 mm de surépaisseur et **corrige la déformation de trempe**. C'est ici qu'on atteint le H7 et le Ra 0,8. |
| 80 | Contrôle : dureté HRC, profondeur cémentée (micrographie), **contrôle magnétoscopique** | Vérifie l'absence de tapures de trempe. |

**Résultat obtenu :**

| Zone | Dureté | Fonction |
|---|---|---|
| Flancs de dents | **60 HRC** (≈ 700 HV) | Résiste à la pression de contact (~1500 MPa) et à l'usure |
| Cœur | **30 HRC** (≈ 300 HB) | Encaisse les chocs de passage de vitesse sans rompre |
| Alésage (protégé) | **30 HRC** | Reste ajustable et tenace pour l'emmanchement |

**L'erreur à ne jamais commettre :** intervertir les étapes 30 et 40. Tailler une denture dans un
acier déjà cémenté-trempé à 60 HRC exigerait des outils CBN, un temps de cycle multiplié par 10,
et le résultat serait médiocre. **En traitement thermique, l'ordre des opérations n'est jamais
négociable : on usine tendre, on traite, on rectifie.**
""",
            "exercice": """
**Exercice type examen — Choix et implantation d'un traitement**

Une **tige de vérin hydraulique** doit être conçue. Données :
- Ø40 mm, longueur 900 mm, course 700 mm
- Effort de poussée maximal : 120 kN ; effort de traction : 85 kN
- Vitesse de sortie 0,3 m/s, 200 cycles/heure, service continu
- Matériau envisagé : **C45** ou **42CrMo4**
- Environnement : atelier, présence d'humidité et de poussière abrasive
- Étanchéité assurée par joints à lèvres sur la tige

**Questions :**

1. Calculer la contrainte de traction dans la tige et le coefficient de sécurité pour chaque
   nuance (C45 trempé revenu : $R_e$ = 660 MPa ; 42CrMo4 trempé revenu : $R_e$ = 750 MPa).
2. Quelle sollicitation supplémentaire, non mentionnée dans l'énoncé, doit impérativement être
   vérifiée sur une tige de vérin en poussée ? Expliquer physiquement.
3. Quelles sont les **trois exigences de surface** que doit satisfaire une tige de vérin ?
   Justifier chacune par le mode de défaillance qu'elle évite.
4. Proposer un traitement complet (masse + surface) et le placer dans une gamme d'usinage
   cohérente en 6 étapes.
5. Le fournisseur propose une variante « tige inox X20Cr13 trempée, sans revêtement ».
   Analyser cette proposition : avantages, inconvénients, contexte où elle serait pertinente.
6. Après 8 mois, une tige présente des **piqûres de corrosion** ponctuelles et le vérin fuit.
   Formuler deux hypothèses de cause et la contre-mesure associée à chacune.
""",
            "corrige": """
**1. Contrainte de traction et coefficients de sécurité**

Section de la tige :
$$ S = \\frac{\\pi d^2}{4} = \\frac{\\pi \\times 40^2}{4} = \\mathbf{1\\,256,6\\ \\mathrm{mm^2}} $$

Contrainte en traction (effort de 85 kN) :
$$ \\sigma = \\frac{F}{S} = \\frac{85\\,000}{1\\,256,6} = \\mathbf{67,6\\ \\mathrm{MPa}} $$

| Nuance | $R_e$ | $s = R_e / \\sigma$ |
|---|---|---|
| C45 trempé revenu | 660 MPa | $660/67,6 = \\mathbf{9,8}$ |
| 42CrMo4 trempé revenu | 750 MPa | $750/67,6 = \\mathbf{11,1}$ |

**Conclusion : les deux nuances sont largement suffisantes en traction pure.** Le dimensionnement
n'est manifestement **pas gouverné par la résistance en traction** — le diamètre de 40 mm est
imposé par autre chose (voir question 2). Un coefficient de 10 signale toujours qu'un autre
critère commande.

---

**2. Sollicitation supplémentaire : le FLAMBAGE (flambement)**

En **poussée**, la tige est une pièce **élancée comprimée**. Au-delà d'une charge critique, elle ne
cède pas par écrasement mais **s'incurve brutalement latéralement** — c'est une **instabilité
géométrique**, pas une rupture par dépassement de $R_e$.

**Explication physique :** un défaut de rectitude infime (inévitable) crée un bras de levier sous
la charge de compression. Ce bras de levier génère un moment de flexion, qui augmente la
déformation, qui augmente le bras de levier… La divergence est **auto-entretenue et brutale**.

**Charge critique d'Euler** — la tige d'un vérin est assimilable à une poutre **encastrée-guidée**
($L_f = 0,7L$ à $L$ selon le guidage) :

$$ F_c = \\frac{\\pi^2 E I}{L_f^2} \\quad \\text{avec} \\quad I = \\frac{\\pi d^4}{64} = \\frac{\\pi \\times 40^4}{64} = 125\\,664\\ \\mathrm{mm^4} $$

En prenant $L_f = 700$ mm (course sortie, cas défavorable) :

$$ F_c = \\frac{\\pi^2 \\times 210\\,000 \\times 125\\,664}{700^2} = \\frac{2,604 \\times 10^{11}}{490\\,000} = \\mathbf{531\\ \\mathrm{kN}} $$

Coefficient de sécurité au flambage :
$$ s_{flambage} = \\frac{531}{120} = \\mathbf{4,4} $$

✔️ Acceptable (on exige couramment 3 à 5 au flambage). **C'est ce critère qui a fixé le Ø40**, pas
la traction. Noter que $F_c$ dépend de $E$ et **pas du tout de $R_e$** : changer de nuance
d'acier ne change **rien** au flambage. Seul le **diamètre** compte (en $d^4$).

---

**3. Les trois exigences de surface d'une tige de vérin**

| Exigence | Valeur cible | Mode de défaillance évité |
|---|---|---|
| **Rugosité fine et contrôlée** | Ra 0,1 à 0,4 µm | Trop rugueux → les aspérités **cisaillent la lèvre du joint** en quelques milliers de cycles → fuite. Trop lisse (Ra < 0,05) → **le film d'huile ne se forme pas**, frottement sec, usure adhésive. Il existe un optimum. |
| **Dureté superficielle élevée** | ≥ 55 HRC ou ≥ 800 HV | La poussière abrasive de l'atelier se colle au film d'huile et **raye la tige** à chaque rentrée. Une surface tendre se marque définitivement, et chaque rayure devient un canal de fuite. |
| **Résistance à la corrosion** | Revêtement continu, ≥ 20 µm | La tige sort en permanence à l'air humide. Une piqûre de rouille de 0,1 mm suffit à **entailler le joint** au passage. |

*À ajouter, souvent oublié :* la tige doit aussi avoir une **rectitude** ≤ 0,1 mm/m (sinon le joint
travaille en excentré) et **pas de stries hélicoïdales** issues du tournage (elles agiraient comme
une vis d'Archimède et **pomperaient l'huile vers l'extérieur**). D'où la finition obligatoire par
**rectification en plongée puis galetage/polissage**, jamais par tournage seul.

---

**4. Traitement proposé et gamme d'usinage**

**Choix : 42CrMo4 trempé revenu (cœur) + CHROMAGE DUR 25 µm sur fond nitruré ou rectifié.**

*Justification de la nuance :* le 42CrMo4 est **nitrurable** (grâce au Cr et au Mo) et offre une
meilleure limite d'endurance que le C45 — la tige subit 200 cycles/h × 24 h, soit environ
**1,7 million de cycles par an** : on est en **fatigue à grand nombre de cycles**, domaine où le
42CrMo4 est nettement supérieur.

**Gamme d'usinage en 6 étapes :**

| N° | Opération | Justification |
|---|---|---|
| **10** | Débit + **trempe revenu à cœur** (850 °C huile, revenu 600 °C) | Traitement dans la masse **avant** usinage de finition : les déformations sont absorbées par les étapes suivantes. Revenu haut = ténacité maximale, indispensable en fatigue. |
| **20** | Tournage ébauche + finition, **surépaisseur 0,3 mm** ; usinage du filetage de tête et de la gorge de joint | On usine à ~30 HRC : possible et économique. La surépaisseur est réservée pour la rectification. |
| **30** | **Rectification cylindrique** à Ø40,05 (avant revêtement) | Corrige la déformation de trempe, donne la rectitude et un état de surface propre pour l'accrochage du chrome. |
| **40** | **CHROMAGE DUR** épaisseur 25 µm | Dureté 1000 HV + barrière anticorrosion + faible frottement. Réalisé après rectification car le dépôt épouse la surface. |
| **50** | **Rectification / polissage de finition** à Ø40 h8, **Ra 0,2 µm** | Le chromage brut est légèrement rugueux. Cette passe finale donne la cote et l'état de surface définitifs. |
| **60** | Contrôle : Ø, rectitude, Ra, épaisseur de chrome (Fischer), **contrôle des micro-fissures** | Le chrome dur est naturellement micro-fissuré ; on vérifie que le réseau reste fin et régulier. |

**Point clé de la gamme : on rectifie AVANT et APRÈS le revêtement.** Avant, pour la géométrie ;
après, pour l'état de surface. Omettre la seconde rectification est l'erreur classique.

---

**5. Analyse de la variante « inox X20Cr13 trempé, sans revêtement »**

**Décodage :** X → fortement allié ; 20 → 0,20 % C ; Cr 13 → 13 % chrome.
C'est un **inox martensitique**, donc **trempable** (contrairement au 304 austénitique).
Après trempe revenu : $R_e \\approx 600$ MPa, dureté **45-50 HRC**.

| ✅ Avantages | ❌ Inconvénients |
|---|---|
| **Corrosion résistante dans la masse** : une rayure n'expose pas d'acier nu, la couche passive se reforme seule | **Dureté plafonnée à ~50 HRC** contre 1000 HV (≈ 68 HRC équivalent) pour le chrome dur → **bien plus sensible à l'abrasion** |
| **Pas de risque de décollement** ou d'écaillage du revêtement | **Résistance aux chlorures médiocre** : les inox martensitiques piquent en milieu chloruré |
| Gamme simplifiée (pas d'étape de revêtement) | **Coût matière ×4** et usinabilité difficile (écrouissage sous l'outil) |
| Réparable par simple repolissage | $R_e$ inférieur → marge en fatigue réduite |

**Contexte où cette variante serait PERTINENTE :**

- **Agroalimentaire ou pharmaceutique** : lavages fréquents à la soude/acide, où un revêtement
  chromé finirait par se décoller et **contaminer le produit**. La réglementation impose souvent
  l'inox massif.
- **Milieu marin** ou immersion permanente, où la corrosion sous le revêtement (par une seule
  piqûre) est le mode de défaillance dominant.
- **Vérins à faible cadence** en environnement propre, où l'abrasion est négligeable.

**Dans le cas de l'énoncé (atelier poussiéreux, 200 cycles/h) : la variante est DÉCONSEILLÉE.**
Le facteur dominant est l'**abrasion par la poussière**, pas la corrosion chimique. Une surface à
50 HRC se rayera bien plus vite qu'un chrome dur à 1000 HV. On conserve le 42CrMo4 chromé.

---

**6. Diagnostic : piqûres de corrosion après 8 mois**

**Hypothèse A — Micro-fissuration du chrome traversante / épaisseur insuffisante**

*Mécanisme :* le chrome dur est intrinsèquement parcouru d'un réseau de micro-fissures. Si le
dépôt est trop mince (< 15 µm) ou mal maîtrisé, certaines fissures **traversent jusqu'au
substrat**. L'humidité y pénètre et amorce une corrosion **sous le revêtement**. Pire, le couple
galvanique chrome/acier est très défavorable : l'acier, moins noble, se corrode **en accéléré**
(effet de pile avec une petite anode et une grande cathode) — d'où des **piqûres profondes et
ponctuelles**, exactement le symptôme décrit.

*Contre-mesure :*
- Porter l'épaisseur de chrome à **40-50 µm minimum**.
- Mieux : adopter un **système duplex** — **nitruration** (0,3 mm, qui crée une couche de
  combinaison dense et une zone de diffusion) **puis chromage**. La couche nitrurée sert de
  barrière de secours si le chrome est percé.
- Alternative moderne : remplacer le chrome par une **projection HVOF de carbure de tungstène
  (WC-Co)**, non fissurée, désormais standard sur les vérins offshore.

**Hypothèse B — Endommagement mécanique du revêtement par la poussière abrasive**

*Mécanisme :* l'énoncé signale une **poussière abrasive**. Sans racleur efficace, les particules
s'incrustent dans le film d'huile, sont entraînées à la rentrée de tige et **rayent le chrome**.
Chaque rayure met l'acier à nu, la corrosion s'y amorce, et la piqûre qui en résulte devient à son
tour un site d'accrochage pour d'autres particules. Le processus est **auto-aggravant**. La fuite
constatée en est la conséquence directe : la lèvre du joint ne peut plus étancher sur une surface
piquée.

*Contre-mesure :*
- Monter un **joint racleur** (*scraper*) en amont du joint d'étanchéité, si absent — c'est la
  cause n°1 de ce défaut en atelier.
- Ajouter un **soufflet de protection** sur la course sortie.
- Instaurer un **nettoyage périodique** de la tige et un contrôle visuel mensuel.

**Démarche de diagnostic recommandée :** examiner la **répartition des piqûres**.
- Piqûres **réparties uniformément** sur toute la course, sans rayure visible → hypothèse A
  (défaut de revêtement).
- Piqûres **alignées longitudinalement**, associées à des rayures, concentrées sur la zone de
  course → hypothèse B (abrasion). C'est le cas le plus fréquent et le plus facile à corriger.
""",
        },
    ],
}


BLOC_4 = {
    "id": "bloc4",
    "titre": "Bloc 4 — Résistance des matériaux (RDM)",
    "resume": "Vérifier qu'une pièce ne casse pas et ne se déforme pas trop, par le calcul.",
    "fiches": [
        {
            "id": "4.1",
            "titre": "Hypothèses, torseur de cohésion, traction et compression",
            "duree": "10 h",
            "cours": """
### 1. À quoi sert la RDM

La RDM répond à **deux questions**, et à deux questions seulement :

1. **La pièce va-t-elle casser ?** → condition de **résistance** ($\\sigma \\le R_{pe}$)
2. **La pièce va-t-elle trop se déformer ?** → condition de **rigidité** ($\\Delta L$ ou $f \\le$ limite)

Il faut **toujours vérifier les deux**. Comme vu en fiche 3.1, c'est tantôt l'une, tantôt l'autre
qui dimensionne.

### 2. Les hypothèses de la RDM (à citer en examen)

**Sur le matériau :**
- **Homogène** : mêmes propriétés en tout point
- **Isotrope** : mêmes propriétés dans toutes les directions *(faux pour un composite ou une pièce
  imprimée en 3D — point important pour le BTS CPI)*
- **Élastique linéaire** : la loi de Hooke s'applique ($\\sigma = E\\varepsilon$)

**Sur la géométrie :** on étudie des **poutres**, c'est-à-dire des solides dont une dimension
est **grande devant les deux autres** (rapport ≥ 10). La ligne moyenne doit être droite ou de
faible courbure, la section constante ou lentement variable.

**Sur les déformations :** elles restent **petites** (hypothèse des petits déplacements).

**Hypothèse de Navier-Bernoulli :** *les sections planes perpendiculaires à la ligne moyenne
restent planes et perpendiculaires après déformation.* C'est cette hypothèse qui permet toute la
théorie des poutres.

**Principe de Saint-Venant :** loin des points d'application des charges, les contraintes ne
dépendent que du torseur de cohésion, pas de la façon dont la charge est appliquée. **Corollaire
pratique : les résultats de RDM sont faux à proximité immédiate des appuis, des perçages et des
changements brusques de section** — ce sont précisément les zones de concentration de contrainte.

### 3. Le torseur de cohésion

On coupe la poutre par un plan fictif en un point G. Les efforts que la partie droite exerce sur
la partie gauche se réduisent à un **torseur** en G, comportant 6 composantes :

$$ \\{\\mathcal{T}_{coh}\\}_G = \\begin{Bmatrix} N & M_t \\\\ T_y & M_{fy} \\\\ T_z & M_{fz} \\end{Bmatrix} $$

| Composante | Nom | Sollicitation associée |
|---|---|---|
| $N$ | Effort **normal** | Traction (N>0) / Compression (N<0) |
| $T_y$, $T_z$ | Efforts **tranchants** | Cisaillement |
| $M_t$ | Moment de **torsion** | Torsion |
| $M_{fy}$, $M_{fz}$ | Moments de **flexion** | Flexion |

**Les sollicitations simples** correspondent au cas où une seule composante est non nulle.
Dans la réalité elles se combinent (flexion + torsion sur un arbre, par exemple).

### 4. Traction / compression simple

Seule composante : $N$. La contrainte est **normale**, **uniformément répartie** sur la section :

$$ \\sigma = \\frac{N}{S} $$

**Répartition uniforme** : c'est ce qui distingue la traction de la flexion (où la contrainte varie
linéairement dans la hauteur). En traction, **toute la matière travaille de façon identique** :
c'est la sollicitation la plus « efficace » en termes d'utilisation de matière.

### 5. Le coefficient de sécurité

$$ R_{pe} = \\frac{R_e}{s} $$

Le coefficient $s$ couvre : l'incertitude sur les charges réelles, la dispersion des propriétés
matériau, les approximations du modèle, les défauts de fabrication et la gravité des conséquences.

| $s$ | Contexte |
|---|---|
| 1,5 à 2 | Charges bien connues, matériau contrôlé, conséquences légères |
| 2 à 3 | **Mécanique générale (cas courant du BTS)** |
| 3 à 5 | Charges mal connues, chocs, fatigue |
| 5 à 12 | **Levage, sécurité des personnes** (réglementé) |

### 6. Concentration de contrainte

Un perçage, une gorge, un épaulement **perturbent localement** la répartition des contraintes :

$$ \\sigma_{max} = K_t \\times \\sigma_{nominale} $$

$K_t$ vaut typiquement **2 à 3** pour un trou circulaire, et peut dépasser **5** pour une gorge à
angle vif. **En statique sur un matériau ductile, on peut souvent négliger $K_t$** (la plastification
locale redistribue les contraintes). **En fatigue, jamais** : c'est là que les fissures s'amorcent.

*Règle de conception : mettre un rayon partout où c'est possible. Un R2 au lieu d'un angle vif
peut doubler la durée de vie d'une pièce.*
""",
            "formules": """
**TRACTION / COMPRESSION SIMPLE**

Contrainte normale :
$$ \\boxed{\\sigma = \\frac{N}{S}} \\qquad \\mathrm{[MPa]} = \\frac{\\mathrm{[N]}}{\\mathrm{[mm^2]}} $$

Condition de résistance :
$$ \\boxed{\\sigma_{max} \\le R_{pe} = \\frac{R_e}{s}} $$

Allongement (loi de Hooke) :
$$ \\boxed{\\Delta L = \\frac{N \\cdot L_0}{E \\cdot S}} $$

Raideur d'une barre en traction :
$$ k = \\frac{E \\cdot S}{L_0} \\qquad \\mathrm{[N/mm]} $$

**SECTIONS USUELLES**

| Section | Aire $S$ |
|---|---|
| Rectangle $b \\times h$ | $b h$ |
| Cercle plein Ø$d$ | $\\dfrac{\\pi d^2}{4}$ |
| Tube $D$ ext, $d$ int | $\\dfrac{\\pi(D^2 - d^2)}{4}$ |
| Carré creux $B$ ext, $b$ int | $B^2 - b^2$ |

**FLAMBAGE (compression de pièces élancées)**

Charge critique d'Euler :
$$ \\boxed{F_c = \\frac{\\pi^2 E I_{min}}{L_f^2}} $$

Longueur libre de flambage $L_f$ selon les liaisons :

| Liaisons | $L_f$ |
|---|---|
| Rotule – rotule | $L$ |
| Encastrement – libre | $2L$ |
| Encastrement – rotule | $0,7L$ |
| Encastrement – encastrement | $0,5L$ |

Élancement :
$$ \\lambda = \\frac{L_f}{\\rho} \\quad \\text{avec} \\quad \\rho = \\sqrt{\\frac{I_{min}}{S}} $$

⚠️ **Le flambage n'est à vérifier que si $\\lambda > \\lambda_c \\approx 100$ pour l'acier.**
En deçà, la ruine se produit par écrasement classique.

**CONCENTRATION DE CONTRAINTE**

$$ \\sigma_{max} = K_t \\cdot \\sigma_{nom} \\qquad \\text{avec} \\quad \\sigma_{nom} = \\frac{N}{S_{nette}} $$

$S_{nette}$ = section **réellement résistante** (section brute moins la matière enlevée par le trou).

**CONTRAINTE THERMIQUE** (barre bridée entre deux appuis rigides)

$$ \\sigma_{th} = E \\cdot \\alpha \\cdot \\Delta T $$

*Exemple frappant : une barre d'acier bridée chauffée de 50 °C développe
$\\sigma = 210\\,000 \\times 11\\times10^{-6} \\times 50 = 115$ MPa — sans aucune charge extérieure.
C'est la moitié de la limite élastique d'un S235.*
""",
            "exemple": """
**Cas industriel — Vérification d'une chape de levage percée**

Une chape en **S355** ($R_e = 355$ MPa) soulève une charge de **25 kN**. Elle est constituée d'une
tôle de **10 mm** d'épaisseur et **60 mm** de large, percée d'un trou **Ø20** pour l'axe.
Coefficient de sécurité réglementaire pour le levage : **s = 5**.

**Étape 1 — Contrainte pratique**
$$ R_{pe} = \\frac{355}{5} = 71\\ \\mathrm{MPa} $$

**Étape 2 — Section BRUTE (loin du trou)**
$$ S_{brute} = 60 \\times 10 = 600\\ \\mathrm{mm^2} \\;\\Rightarrow\\; \\sigma = \\frac{25\\,000}{600} = 41,7\\ \\mathrm{MPa} $$
$41,7 \\le 71$ ✔️ *Vérifié — mais ce n'est pas la zone critique.*

**Étape 3 — Section NETTE (au droit du trou) : c'est ici que ça se joue**
$$ S_{nette} = (60 - 20) \\times 10 = 400\\ \\mathrm{mm^2} $$
$$ \\sigma_{nom} = \\frac{25\\,000}{400} = 62,5\\ \\mathrm{MPa} $$
$62,5 \\le 71$ ✔️ *Encore vérifié, mais la marge fond : le coefficient réel n'est plus que
$355/62,5 = 5,7$.*

**Étape 4 — Concentration de contrainte**
Rapport $d/b = 20/60 = 0,33$ → abaque : $K_t \\approx 2,25$
$$ \\sigma_{max} = 2,25 \\times 62,5 = \\mathbf{140,6\\ MPa} $$

**Étape 5 — Interprétation, et c'est là que se joue la compétence du technicien**

| Cas de charge | Verdict | Raisonnement |
|---|---|---|
| **Charge statique** (levage occasionnel) | ✅ **Acceptable** | $140,6 < R_e = 355$. Le S355 est **ductile** ($A = 22$ %) : les 140 MPa de pic provoquent une plastification **très locale** au bord du trou, qui **redistribue** immédiatement la contrainte. La pièce ne casse pas. On dimensionne sur $\\sigma_{nom} = 62,5$ MPa. |
| **Charge cyclique** (palan en service continu) | ❌ **REFUSÉ** | En fatigue, la limite d'endurance du S355 vaut $\\sigma_D \\approx 0,5 R_m \\approx 235$ MPa, à corriger : surface découpée ($k_s = 0,7$), taille ($k_t = 0,9$) → $\\sigma_{D,réelle} \\approx 148$ MPa. On est à 140,6 MPa : **on frôle la limite**, sans aucune marge. Une fissure s'amorcera au bord du trou. |

**Correctifs proposés par le BE pour le cas cyclique :**
1. **Élargir la tôle à 80 mm** → $S_{nette} = 600$ mm², $\\sigma_{nom} = 41,7$, $\\sigma_{max} = 94$ MPa ✔️
2. **Alésage soigné + galetage du trou** : introduit des contraintes résiduelles de compression,
   $k_s$ passe de 0,7 à 0,9 et $K_t$ effectif diminue.
3. **Souder une bague de renfort** autour du trou (solution classique sur les chapes de levage).

**La leçon :** vérifier la section brute ne suffit jamais. *On calcule toujours au droit de la
section la plus faible, et on se demande si la charge est statique ou cyclique.*
""",
            "exercice": """
**Exercice type examen — Bielle de commande d'un mécanisme**

Une bielle relie un vérin à un levier. Elle est constituée d'un **tube en E335**
($R_e = 335$ MPa, $E = 210$ GPa) de diamètre extérieur **D = 30 mm**, épaisseur **e = 4 mm**,
longueur entre articulations **L = 600 mm**. Les deux extrémités sont montées sur **rotules**.

Efforts transmis : **traction 32 kN** ou **compression 32 kN** selon le sens de la manœuvre.
Coefficient de sécurité imposé : **s = 3**.

**Questions :**

1. Calculer la section $S$ et le moment quadratique $I$ du tube.
2. **Cas TRACTION** : calculer la contrainte et vérifier la condition de résistance.
3. Calculer l'allongement de la bielle sous cette traction.
4. **Cas COMPRESSION** : calculer l'élancement $\\lambda$ et déterminer s'il faut vérifier le flambage.
5. Si oui, calculer la charge critique d'Euler et le coefficient de sécurité au flambage. Conclure.
6. Le BE envisage de remplacer le tube par un **barreau plein de même masse**. Déterminer son
   diamètre, puis recalculer la charge critique de flambage. Commenter le résultat et en tirer une
   règle générale de conception.
""",
            "corrige": """
**1. Caractéristiques de la section**

Diamètre intérieur : $d = D - 2e = 30 - 2\\times4 = 22\\ \\mathrm{mm}$

**Aire :**
$$ S = \\frac{\\pi(D^2 - d^2)}{4} = \\frac{\\pi(30^2 - 22^2)}{4} = \\frac{\\pi(900 - 484)}{4} = \\frac{\\pi \\times 416}{4} $$
$$ \\boxed{S = 326,7\\ \\mathrm{mm^2}} $$

**Moment quadratique :**
$$ I = \\frac{\\pi(D^4 - d^4)}{64} = \\frac{\\pi(30^4 - 22^4)}{64} = \\frac{\\pi(810\\,000 - 234\\,256)}{64} = \\frac{\\pi \\times 575\\,744}{64} $$
$$ \\boxed{I = 28\\,258\\ \\mathrm{mm^4}} $$

---

**2. Cas TRACTION — condition de résistance**

$$ R_{pe} = \\frac{R_e}{s} = \\frac{335}{3} = 111,7\\ \\mathrm{MPa} $$

$$ \\sigma = \\frac{N}{S} = \\frac{32\\,000}{326,7} = \\mathbf{97,9\\ \\mathrm{MPa}} $$

$$ 97,9\\ \\mathrm{MPa} \\;\\le\\; 111,7\\ \\mathrm{MPa} \\quad ✔️ \\;\\; \\textbf{RÉSISTANCE VÉRIFIÉE} $$

Coefficient de sécurité réel : $s_{réel} = \\dfrac{335}{97,9} = \\mathbf{3,42}$

---

**3. Allongement sous traction**

$$ \\Delta L = \\frac{N \\cdot L}{E \\cdot S} = \\frac{32\\,000 \\times 600}{210\\,000 \\times 326,7} = \\frac{19\\,200\\,000}{68\\,607\\,000} $$

$$ \\boxed{\\Delta L = 0,28\\ \\mathrm{mm}} $$

Déformation relative : $\\varepsilon = 0,28/600 = 0,047\\ \\%$ — très faible, on reste largement dans
le domaine élastique (le S/E335 plastifie vers $\\varepsilon = 0,16$ %).

---

**4. Cas COMPRESSION — élancement**

Rayon de giration :
$$ \\rho = \\sqrt{\\frac{I}{S}} = \\sqrt{\\frac{28\\,258}{326,7}} = \\sqrt{86,5} = 9,30\\ \\mathrm{mm} $$

Liaisons **rotule–rotule** → $L_f = L = 600\\ \\mathrm{mm}$

$$ \\lambda = \\frac{L_f}{\\rho} = \\frac{600}{9,30} = \\mathbf{64,5} $$

**Faut-il vérifier le flambage ?**

$$ \\lambda = 64,5 \\;<\\; \\lambda_c \\approx 100 \\quad (\\text{acier}) $$

En toute rigueur, la formule d'Euler pure ne s'applique **pas** dans ce domaine (poutre
« moyennement élancée ») : on est dans la zone de **flambage plastique**, où l'on utilise des
formules empiriques (Rankine, Dutheil, ou les courbes de l'Eurocode 3).

**Néanmoins, l'énoncé demande la vérification et l'esprit du BTS est de calculer Euler comme
majorant de la charge critique.** Une valeur d'Euler très supérieure à la charge appliquée permet
de conclure sans ambiguïté. Procédons.

---

**5. Charge critique d'Euler**

$$ F_c = \\frac{\\pi^2 E I}{L_f^2} = \\frac{\\pi^2 \\times 210\\,000 \\times 28\\,258}{600^2} $$

$$ F_c = \\frac{9,8696 \\times 210\\,000 \\times 28\\,258}{360\\,000} = \\frac{5,857 \\times 10^{10}}{360\\,000} $$

$$ \\boxed{F_c = 162,7\\ \\mathrm{kN}} $$

**Coefficient de sécurité au flambage :**
$$ s_{flambage} = \\frac{F_c}{F} = \\frac{162,7}{32} = \\mathbf{5,08} $$

**Conclusion :** $s_{flambage} = 5,08$, supérieur au minimum usuel de 3 à 5 exigé au flambage. ✔️

⚠️ **Réserve à formuler pour avoir tous les points :** comme $\\lambda = 64,5 < 100$, la charge
critique **réelle** est **inférieure** à celle donnée par Euler (Euler surestime dans ce domaine,
car il ignore la plastification). Une vérification par la courbe de flambement de l'Eurocode 3
donnerait une charge admissible de l'ordre de **110 à 130 kN**, soit $s \\approx 3,4$ à $4,1$.
**La bielle reste acceptable**, mais la marge est plus mince qu'Euler ne le laisse croire.

*Vérification complémentaire, écrasement simple :* $\\sigma = 97,9$ MPa $\\le 111,7$ MPa ✔️ (identique
au cas traction, la compression pure ne pose pas de problème de résistance).

---

**6. Comparaison avec un barreau PLEIN de même masse**

**a) Diamètre du barreau plein**

Même masse ⟺ même volume ⟺ **même section** (longueur identique) :

$$ S_{plein} = S_{tube} = 326,7\\ \\mathrm{mm^2} = \\frac{\\pi d_p^2}{4} $$

$$ d_p = \\sqrt{\\frac{4 \\times 326,7}{\\pi}} = \\sqrt{415,9} = \\mathbf{20,4\\ \\mathrm{mm}} $$

**b) Moment quadratique du barreau plein**

$$ I_{plein} = \\frac{\\pi d_p^4}{64} = \\frac{\\pi \\times 20,4^4}{64} = \\frac{\\pi \\times 173\\,229}{64} = \\mathbf{8\\,502\\ \\mathrm{mm^4}} $$

**c) Charge critique du barreau plein**

$$ F_{c,plein} = \\frac{\\pi^2 \\times 210\\,000 \\times 8\\,502}{360\\,000} = \\frac{1,762\\times10^{10}}{360\\,000} = \\mathbf{48,9\\ \\mathrm{kN}} $$

$$ s_{flambage,plein} = \\frac{48,9}{32} = \\mathbf{1,53} \\quad ❌ \\;\\textbf{INSUFFISANT} $$

**d) Comparaison et règle générale**

| | Tube Ø30×4 | Barreau plein Ø20,4 |
|---|---|---|
| Section (donc **masse**) | 326,7 mm² | 326,7 mm² — **identique** |
| Résistance en traction | 97,9 MPa ✔️ | 97,9 MPa ✔️ — **identique** |
| Moment quadratique $I$ | **28 258 mm⁴** | 8 502 mm⁴ (**−70 %**) |
| Charge critique $F_c$ | **162,7 kN** ✔️ | 48,9 kN ❌ |
| Coefficient au flambage | **5,08** | 1,53 |

**Le tube est 3,3 fois plus résistant au flambage, à masse strictement identique.**

**Règle générale de conception à retenir :**

> **La résistance en traction ne dépend que de la SECTION. La résistance au flambage (et à la
> flexion) dépend du MOMENT QUADRATIQUE, qui croît en $d^4$.**
>
> Éloigner la matière de l'axe neutre augmente $I$ sans augmenter $S$. **D'où la supériorité
> systématique des sections creuses** — tubes, profilés, caissons — dès qu'il y a de la flexion,
> de la torsion ou du flambage.

*Applications de cette règle partout autour de nous :* cadres de vélo, mâts d'éclairage, bielles
de vérin, os longs du squelette (creux, remplis de moelle), tiges de golf, fuselages d'avion.
La nature l'avait trouvée avant les ingénieurs.

*Limite de la règle :* on ne peut pas amincir la paroi indéfiniment — apparaît alors le
**voilement local** (la paroi flambe sur elle-même). Règle empirique : conserver $D/e \\le 50$.
Ici $30/4 = 7,5$, très largement sûr.
""",
        },
        {
            "id": "4.2",
            "titre": "Cisaillement et torsion",
            "duree": "8 h",
            "cours": """
### 1. CISAILLEMENT SIMPLE

**Définition :** une poutre est cisaillée quand le torseur de cohésion se réduit à un **effort
tranchant** $T$ contenu dans le plan de la section.

**Modèle physique :** deux forces égales, opposées, **très proches**, perpendiculaires à la ligne
moyenne. C'est exactement ce que fait une paire de ciseaux, une cisaille guillotine, ou ce que
subit une goupille entre deux pièces qui glissent l'une sur l'autre.

**Contrainte tangentielle** (répartition supposée uniforme) :

$$ \\tau = \\frac{T}{S} $$

⚠️ **Hypothèse simplificatrice importante :** la répartition réelle de $\\tau$ n'est **pas
uniforme** (elle est parabolique, maximale au centre, nulle aux bords). Le modèle uniforme est
une approximation d'ingénieur, acceptée en BTS et en pratique industrielle pour les assemblages
(goupilles, rivets, boulons, clavettes) car les coefficients de sécurité la couvrent.

**Cisaillement simple ou double ?** C'est l'erreur n°1 des étudiants.

```
CISAILLEMENT SIMPLE (1 section)      CISAILLEMENT DOUBLE (2 sections)
   ┌──────┐                              ┌──┐    ┌──┐
───┤  ▓▓  ├───►                       ───┤▓▓├────┤▓▓├───►
   └──────┘                              └──┘    └──┘
   1 plan de coupe                       2 plans de coupe
   τ = T/S                               τ = T/(2S)
   (assemblage à recouvrement)           (chape, axe entre 2 flasques)
```

### 2. Loi de Hooke en cisaillement

$$ \\tau = G \\cdot \\gamma $$

où $\\gamma$ est l'**angle de glissement** (en radians) et $G$ le **module de Coulomb** :

$$ G = \\frac{E}{2(1+\\nu)} \\;\\approx\\; 80\\,000\\ \\mathrm{MPa} \\;\\text{pour l'acier} $$

**Résistance au glissement :** $R_{eg} \\approx 0,5$ à $0,7 \\times R_e$ selon les matériaux.
**En BTS, on retient $R_{eg} = 0,5 \\, R_e$ pour les aciers doux et $0,6 \\, R_e$ pour les aciers
alliés**, sauf indication contraire de l'énoncé.

### 3. TORSION SIMPLE

**Définition :** le torseur de cohésion se réduit à un **moment de torsion** $M_t$ porté par la
ligne moyenne. C'est la sollicitation des **arbres de transmission**.

**Hypothèse fondamentale :** la théorie exposée ici n'est valable que pour des **sections
circulaires** (pleines ou creuses). Pour une section quelconque, les sections **gauchissent** et
la théorie ne s'applique plus — c'est pourquoi **les arbres de transmission sont toujours
cylindriques**.

**Répartition de la contrainte :**

$$ \\tau(\\rho) = \\frac{M_t \\cdot \\rho}{I_0} $$

La contrainte est **nulle au centre** et **maximale à la périphérie** :

$$ \\tau_{max} = \\frac{M_t \\cdot v}{I_0} = \\frac{M_t}{I_0/v} $$

**Conséquence de conception majeure :** puisque la matière au centre de l'arbre ne travaille
presque pas, **un arbre creux est bien plus efficace qu'un arbre plein à masse égale**. C'est le
même raisonnement qu'au flambage (fiche 4.1), pour la même raison : la grandeur qui compte croît
en $d^4$.

**Angle de torsion :**

$$ \\theta = \\frac{M_t \\cdot L}{G \\cdot I_0} \\qquad \\mathrm{[rad]} $$

En transmission de puissance, on limite couramment l'angle de torsion **unitaire** à
**0,25°/m** pour les arbres de précision (sinon le mouvement perd sa fidélité).

### 4. Le lien avec la puissance transmise

C'est la relation qui sert de point de départ à tout dimensionnement d'arbre :

$$ P = M_t \\cdot \\omega $$

$$ \\text{avec} \\quad \\omega = \\frac{2\\pi N}{60} \\quad (N \\text{ en tr/min}) $$

### 5. Concentration de contrainte en torsion

Les gorges, rainures de clavette et épaulements sont **particulièrement pénalisants en torsion** :

| Détail | $K_t$ en torsion |
|---|---|
| Rainure de clavette (fond arrondi) | 1,6 à 2,0 |
| Rainure de clavette (fond vif) | 2,5 à 3,5 |
| Épaulement $r/d = 0,05$ | ≈ 1,8 |
| Épaulement $r/d = 0,2$ | ≈ 1,2 |

**Règle de conception :** toujours prévoir un **congé de raccordement généreux** aux épaulements
d'arbre ($r \\ge 0,1 d$ si possible), et proscrire les fonds de rainure à angle vif.
""",
            "formules": """
**CISAILLEMENT**

$$ \\boxed{\\tau = \\frac{T}{S}} \\quad \\text{(simple)} \\qquad \\boxed{\\tau = \\frac{T}{2S}} \\quad \\text{(double)} $$

Condition de résistance :
$$ \\boxed{\\tau_{max} \\le R_{pg} = \\frac{R_{eg}}{s}} \\qquad \\text{avec} \\quad R_{eg} \\approx 0,5\\ \\text{à}\\ 0,7\\ R_e $$

Loi de Hooke : $\\tau = G\\gamma$ ; module de Coulomb : $G = \\dfrac{E}{2(1+\\nu)}$

**Matage** (à vérifier systématiquement avec le cisaillement d'un axe) :
$$ \\boxed{p = \\frac{F}{d \\cdot e} \\le p_{adm}} $$
$d$ = diamètre de l'axe, $e$ = épaisseur de la pièce percée.
$p_{adm} \\approx 0,8 \\times R_e$ pour un acier ; 40 à 80 MPa pour une fonte.

---

**TORSION**

Contrainte maximale :
$$ \\boxed{\\tau_{max} = \\frac{M_t \\cdot v}{I_0}} \\qquad v = \\frac{d}{2} \\;\\text{(rayon extérieur)} $$

Moment quadratique polaire :

| Section | $I_0$ | $I_0/v$ (module de torsion) |
|---|---|---|
| Cercle plein Ø$d$ | $\\dfrac{\\pi d^4}{32}$ | $\\dfrac{\\pi d^3}{16}$ |
| Tube $D$/$d$ | $\\dfrac{\\pi(D^4-d^4)}{32}$ | $\\dfrac{\\pi(D^4-d^4)}{16D}$ |

Relation utile : $I_0 = I_{Gy} + I_{Gz} = 2I$ pour une section circulaire.

Angle de torsion :
$$ \\boxed{\\theta = \\frac{M_t \\cdot L}{G \\cdot I_0}} \\quad \\mathrm{[rad]} \\qquad \\theta° = \\theta_{rad} \\times \\frac{180}{\\pi} $$

Angle unitaire : $\\theta_u = \\dfrac{M_t}{G I_0}$ [rad/mm]

---

**PUISSANCE ET COUPLE**

$$ \\boxed{P = M_t \\cdot \\omega} \\qquad \\boxed{\\omega = \\frac{2\\pi N}{60} = \\frac{\\pi N}{30}} $$

$$ \\boxed{M_t = \\frac{30 P}{\\pi N}} \\qquad [\\mathrm{N \\cdot m}] = \\frac{[\\mathrm{W}]}{[\\mathrm{rad/s}]} $$

⚠️ **Piège d'unités classique :** $P$ en **watts**, $N$ en **tr/min**, $M_t$ en **N·m**.
Pour utiliser $M_t$ dans les formules de contrainte (en mm), **multiplier par 1000** :
$1\\ \\mathrm{N \\cdot m} = 1\\,000\\ \\mathrm{N \\cdot mm}$.

**Rendement d'une transmission :** $P_{sortie} = \\eta \\cdot P_{entrée}$

**Formule de pré-dimensionnement rapide d'un arbre plein en torsion :**
$$ d \\ge \\sqrt[3]{\\frac{16 M_t}{\\pi R_{pg}}} $$
""",
            "exemple": """
**Cas industriel — Dimensionnement complet d'un arbre de transmission**

Un moteur de **7,5 kW** tournant à **1 450 tr/min** entraîne une pompe via un accouplement. L'arbre
est en **42CrMo4** trempé revenu ($R_e = 750$ MPa). Une rainure de clavette est nécessaire.
Coefficient de sécurité : **s = 4** (service continu, chocs modérés).

**Étape 1 — Couple à transmettre**
$$ \\omega = \\frac{2\\pi \\times 1450}{60} = 151,8\\ \\mathrm{rad/s} $$
$$ M_t = \\frac{P}{\\omega} = \\frac{7\\,500}{151,8} = 49,4\\ \\mathrm{N \\cdot m} = \\mathbf{49\\,400\\ N \\cdot mm} $$

**Étape 2 — Contrainte pratique de glissement**
Pour un acier allié : $R_{eg} = 0,6 \\times 750 = 450$ MPa
$$ R_{pg} = \\frac{450}{4} = 112,5\\ \\mathrm{MPa} $$

**Étape 3 — Pré-dimensionnement (sans rainure)**
$$ d \\ge \\sqrt[3]{\\frac{16 M_t}{\\pi R_{pg}}} = \\sqrt[3]{\\frac{16 \\times 49\\,400}{\\pi \\times 112,5}} = \\sqrt[3]{2\\,237} = 13,1\\ \\mathrm{mm} $$

**Étape 4 — Prise en compte de la rainure de clavette (l'étape que les débutants oublient)**
Rainure à fond arrondi : $K_t \\approx 1,8$
$$ d_{corrigé} \\ge 13,1 \\times \\sqrt[3]{1,8} = 13,1 \\times 1,216 = 15,9\\ \\mathrm{mm} $$

**Étape 5 — Choix normalisé : Ø25 mm**
Pourquoi si loin au-dessus des 16 mm calculés ? Trois raisons **de terrain** :
- l'arbre subit aussi de la **flexion** (poids du rotor, tension de courroie éventuelle) ;
- le **diamètre normalisé d'arbre moteur** pour 7,5 kW en CEI est de 38 mm côté moteur, il faut
  une continuité dimensionnelle cohérente ;
- il faut loger un **roulement** : le plus petit roulement raisonnable ici est un 6205 (d = 25).

**Vérification finale à Ø25 :**
$$ \\frac{I_0}{v} = \\frac{\\pi \\times 25^3}{16} = 3\\,068\\ \\mathrm{mm^3} $$
$$ \\tau_{nom} = \\frac{49\\,400}{3\\,068} = 16,1\\ \\mathrm{MPa} \\;;\\quad \\tau_{max} = 1,8 \\times 16,1 = \\mathbf{29,0\\ MPa} $$
$$ s_{réel} = \\frac{450}{29,0} = \\mathbf{15,5} \\quad ✔️ $$

**Étape 6 — Vérification de l'angle de torsion sur 400 mm**
$$ I_0 = \\frac{\\pi \\times 25^4}{32} = 38\\,349\\ \\mathrm{mm^4} $$
$$ \\theta = \\frac{49\\,400 \\times 400}{80\\,000 \\times 38\\,349} = 0,00644\\ \\mathrm{rad} = \\mathbf{0,37°} $$
Soit **0,92°/m**. Acceptable pour une pompe (on tolère jusqu'à 1°/m) ; ce serait **refusé** sur un
axe de machine-outil de précision (limite 0,25°/m).

**La leçon du cas :** le calcul de torsion pure donne 16 mm, la réalité impose 25 mm. **Le calcul
RDM fournit un minimum, jamais le diamètre final.** Ce sont les composants standards (roulements,
accouplements) et les sollicitations combinées qui fixent la cote réelle.
""",
            "exercice": """
**Exercice type examen — Axe de chape et arbre creux**

**PARTIE A — Axe de chape (cisaillement + matage)**

Un axe cylindrique en **C35** ($R_e = 300$ MPa) assemble une tige de vérin (épaisseur 20 mm) entre
les **deux flasques d'une chape** (épaisseur 12 mm chacune). L'effort transmis est **F = 48 kN**.
Coefficient de sécurité : **s = 3**. On prendra $R_{eg} = 0,5 R_e$ et $p_{adm} = 0,8 R_e$.

1. S'agit-il de cisaillement simple ou double ? Justifier par un schéma décrit.
2. Déterminer le diamètre minimal de l'axe vis-à-vis du **cisaillement**.
3. Vérifier la **pression de matage** sur la tige de vérin, puis sur un flasque de chape.
   Quelle est la condition la plus contraignante ?
4. Choisir un diamètre normalisé et conclure.

**PARTIE B — Arbre creux (torsion)**

Un arbre de transmission doit transmettre **P = 22 kW** à **N = 750 tr/min**.
Matériau : **34CrMo4** ($R_e = 650$ MPa, $G = 80\\,000$ MPa). Coefficient **s = 5**,
$R_{eg} = 0,6 R_e$. Longueur de l'arbre : **1 200 mm**.

5. Calculer le couple à transmettre.
6. Dimensionner un **arbre plein** et retenir un diamètre normalisé.
7. Dimensionner un **arbre creux** de rapport $d/D = 0,7$, à contrainte maximale identique.
8. Comparer les **masses** des deux solutions et calculer le gain en pourcentage.
9. Vérifier l'angle de torsion de l'arbre creux et conclure sur son acceptabilité
   (limite retenue : 0,5°/m).
"""
,
            "corrige": """
**PARTIE A — AXE DE CHAPE**

**1. Nature du cisaillement**

Configuration : `flasque (12) | tige (20) | flasque (12)`

La tige, chargée vers le haut, tend à glisser entre les deux flasques qui la retiennent vers le
bas. L'axe est donc coupé **en deux endroits** : une fois entre le flasque gauche et la tige, une
fois entre la tige et le flasque droit.

$$ \\boxed{\\textbf{CISAILLEMENT DOUBLE — 2 sections résistantes}} $$

*C'est le montage systématique en chape : il équilibre l'effort et évite de faire travailler l'axe
en flexion, ce qui serait le cas avec un seul flasque.*

---

**2. Diamètre minimal — cisaillement**

$$ R_{eg} = 0,5 \\times 300 = 150\\ \\mathrm{MPa} \\qquad R_{pg} = \\frac{150}{3} = 50\\ \\mathrm{MPa} $$

Condition, en cisaillement double :
$$ \\tau = \\frac{F}{2S} \\le R_{pg} \\;\\Longrightarrow\\; S \\ge \\frac{F}{2 R_{pg}} = \\frac{48\\,000}{2 \\times 50} = 480\\ \\mathrm{mm^2} $$

$$ d \\ge \\sqrt{\\frac{4 \\times 480}{\\pi}} = \\sqrt{611,2} = \\mathbf{24,7\\ \\mathrm{mm}} $$

*Remarque : si l'on avait traité l'exercice en cisaillement simple par erreur, on aurait trouvé
$S \\ge 960$ mm² soit $d \\ge 35$ mm — un axe surdimensionné de 40 %, et une chape entière à redessiner.*

---

**3. Vérification au matage**

$$ p_{adm} = 0,8 \\times 300 = 240\\ \\mathrm{MPa} $$

*(On applique ici la pression admissible directement, comme le veut l'usage pour le matage ;
certains énoncés demandent d'y appliquer aussi le coefficient de sécurité — le préciser en copie.)*

**a) Matage sur la TIGE de vérin (épaisseur 20 mm, reprend la totalité de F) :**
$$ p_{tige} = \\frac{F}{d \\cdot e_{tige}} = \\frac{48\\,000}{d \\times 20} \\le 240 $$
$$ d \\ge \\frac{48\\,000}{240 \\times 20} = \\mathbf{10,0\\ \\mathrm{mm}} $$

**b) Matage sur UN FLASQUE de chape (épaisseur 12 mm, reprend F/2 = 24 kN) :**
$$ p_{flasque} = \\frac{F/2}{d \\cdot e_{flasque}} = \\frac{24\\,000}{d \\times 12} \\le 240 $$
$$ d \\ge \\frac{24\\,000}{240 \\times 12} = \\mathbf{8,3\\ \\mathrm{mm}} $$

**Condition la plus contraignante :**

| Critère | $d_{min}$ |
|---|---|
| **Cisaillement double** | **24,7 mm** ⬅️ **dimensionnant** |
| Matage sur tige | 10,0 mm |
| Matage sur flasque | 8,3 mm |

$$ \\boxed{\\textbf{C'est le CISAILLEMENT qui dimensionne l'axe}} $$

*C'est le cas général pour un axe court et fortement chargé. Le matage devient dimensionnant
lorsque les pièces assemblées sont minces ou en matériau tendre (fonte, aluminium, polymère) —
d'où l'obligation de toujours vérifier les deux.*

---

**4. Choix et conclusion**

**Diamètre normalisé retenu : Ø28 mm** (au-dessus des 24,7 mm requis ; Ø25 serait trop juste).

Vérifications finales :
$$ S = \\frac{\\pi \\times 28^2}{4} = 615,8\\ \\mathrm{mm^2} $$
$$ \\tau = \\frac{48\\,000}{2 \\times 615,8} = 39,0\\ \\mathrm{MPa} \\le 50\\ \\mathrm{MPa} \\;✔️ \\quad (s_{réel} = 150/39,0 = 3,85) $$
$$ p_{tige} = \\frac{48\\,000}{28 \\times 20} = 85,7\\ \\mathrm{MPa} \\le 240\\ \\mathrm{MPa} \\;✔️ $$

**Recommandations de conception à ajouter :** prévoir un **jeu H11/c11** entre axe et alésages
(l'articulation doit tourner librement), une **immobilisation axiale** par anneau élastique ou
goupille, et un **graisseur** si l'articulation travaille en continu.

---

**PARTIE B — ARBRE CREUX EN TORSION**

**5. Couple à transmettre**

$$ \\omega = \\frac{2\\pi N}{60} = \\frac{2\\pi \\times 750}{60} = 78,54\\ \\mathrm{rad/s} $$

$$ M_t = \\frac{P}{\\omega} = \\frac{22\\,000}{78,54} = 280,1\\ \\mathrm{N \\cdot m} = \\mathbf{280\\,100\\ N \\cdot mm} $$

---

**6. Arbre PLEIN**

$$ R_{eg} = 0,6 \\times 650 = 390\\ \\mathrm{MPa} \\qquad R_{pg} = \\frac{390}{5} = 78\\ \\mathrm{MPa} $$

$$ \\tau_{max} = \\frac{M_t}{\\pi d^3/16} \\le R_{pg} \\;\\Longrightarrow\\; d \\ge \\sqrt[3]{\\frac{16 M_t}{\\pi R_{pg}}} $$

$$ d \\ge \\sqrt[3]{\\frac{16 \\times 280\\,100}{\\pi \\times 78}} = \\sqrt[3]{\\frac{4\\,481\\,600}{245,04}} = \\sqrt[3]{18\\,289} = 26,3\\ \\mathrm{mm} $$

**Diamètre normalisé retenu : Ø30 mm**

Vérification : $\\dfrac{I_0}{v} = \\dfrac{\\pi \\times 30^3}{16} = 5\\,301\\ \\mathrm{mm^3}$ →
$\\tau = \\dfrac{280\\,100}{5\\,301} = 52,8\\ \\mathrm{MPa} \\le 78$ ✔️

---

**7. Arbre CREUX avec $d/D = 0,7$**

Module de torsion d'un tube :
$$ \\frac{I_0}{v} = \\frac{\\pi(D^4 - d^4)}{16D} = \\frac{\\pi D^3 (1 - (d/D)^4)}{16} = \\frac{\\pi D^3 (1 - 0,7^4)}{16} $$

$$ 0,7^4 = 0,2401 \\;\\Longrightarrow\\; 1 - 0,2401 = 0,7599 $$

$$ \\frac{I_0}{v} = \\frac{\\pi D^3 \\times 0,7599}{16} = 0,1492\\, D^3 $$

Condition : $\\tau_{max} = \\dfrac{M_t}{0,1492 D^3} \\le 78$

$$ D^3 \\ge \\frac{280\\,100}{0,1492 \\times 78} = \\frac{280\\,100}{11,64} = 24\\,064 $$

$$ D \\ge \\sqrt[3]{24\\,064} = 28,86\\ \\mathrm{mm} $$

**Retenons D = 32 mm, d = 0,7 × 32 = 22,4 → arrondi à d = 22 mm** (tube Ø32 × ép. 5 mm).

Vérification :
$$ \\frac{I_0}{v} = \\frac{\\pi(32^4 - 22^4)}{16 \\times 32} = \\frac{\\pi(1\\,048\\,576 - 234\\,256)}{512} = \\frac{\\pi \\times 814\\,320}{512} = 4\\,996\\ \\mathrm{mm^3} $$
$$ \\tau_{max} = \\frac{280\\,100}{4\\,996} = \\mathbf{56,1\\ MPa} \\le 78\\ \\mathrm{MPa} \\quad ✔️ $$

---

**8. Comparaison des masses**

Les deux arbres ont la même longueur (1 200 mm) et le même matériau : **comparer les masses revient
à comparer les sections.**

**Arbre plein Ø30 :**
$$ S_{plein} = \\frac{\\pi \\times 30^2}{4} = \\mathbf{706,9\\ \\mathrm{mm^2}} $$
$$ m_{plein} = 7\\,850 \\times 706,9 \\times 1\\,200 \\times 10^{-9} = \\mathbf{6,66\\ kg} $$

**Arbre creux Ø32/Ø22 :**
$$ S_{creux} = \\frac{\\pi(32^2 - 22^2)}{4} = \\frac{\\pi(1\\,024 - 484)}{4} = \\frac{\\pi \\times 540}{4} = \\mathbf{424,1\\ \\mathrm{mm^2}} $$
$$ m_{creux} = 7\\,850 \\times 424,1 \\times 1\\,200 \\times 10^{-9} = \\mathbf{4,00\\ kg} $$

**Gain de masse :**
$$ \\text{gain} = \\frac{6,66 - 4,00}{6,66} \\times 100 = \\mathbf{40,0\\ \\%} $$

| | Arbre plein Ø30 | Arbre creux Ø32×5 |
|---|---|---|
| Section | 706,9 mm² | **424,1 mm²** |
| Masse (1,2 m) | 6,66 kg | **4,00 kg** |
| $\\tau_{max}$ | 52,8 MPa | 56,1 MPa |
| Encombrement radial | Ø30 | Ø32 (+7 %) |

**Analyse :** on gagne **40 % de masse** en n'augmentant le diamètre extérieur que de 2 mm, à
contrainte quasi identique. La raison est celle déjà vue en fiche 4.1 : **la matière centrale ne
travaille pratiquement pas en torsion** ($\\tau$ y est proche de zéro). La retirer ne coûte
presque rien en résistance et économise beaucoup en masse.

*Contreparties à mentionner :* coût du tube supérieur à celui du barreau, usinage des portées de
roulement plus délicat (paroi mince), et impossibilité d'usiner des rainures profondes.

---

**9. Angle de torsion de l'arbre creux**

$$ I_0 = \\frac{\\pi(D^4 - d^4)}{32} = \\frac{\\pi(1\\,048\\,576 - 234\\,256)}{32} = \\frac{\\pi \\times 814\\,320}{32} = 79\\,929\\ \\mathrm{mm^4} $$

$$ \\theta = \\frac{M_t \\cdot L}{G \\cdot I_0} = \\frac{280\\,100 \\times 1\\,200}{80\\,000 \\times 79\\,929} = \\frac{3,361 \\times 10^8}{6,394 \\times 10^9} $$

$$ \\theta = 0,05256\\ \\mathrm{rad} = 0,05256 \\times \\frac{180}{\\pi} = \\mathbf{3,01°} $$

**Angle unitaire :**
$$ \\theta_u = \\frac{3,01°}{1,2\\ \\mathrm{m}} = \\mathbf{2,51°/m} $$

**Comparaison à la limite :**
$$ 2,51°/\\mathrm{m} \\;>\\; 0,5°/\\mathrm{m} \\quad ❌ \\;\\; \\textbf{CONDITION DE RIGIDITÉ NON SATISFAITE} $$

**Conclusion et correction :**

L'arbre **résiste** (56 MPa < 78 MPa ✔️) mais **se déforme cinq fois trop**. C'est exactement la
situation annoncée en introduction du bloc : *il faut toujours vérifier les deux conditions, et
c'est souvent la rigidité qui commande.*

**Redimensionnement sur le critère de rigidité :**

$$ \\theta_u \\le 0,5°/\\mathrm{m} = \\frac{0,5 \\times \\pi/180}{1\\,000} = 8,727 \\times 10^{-6}\\ \\mathrm{rad/mm} $$

$$ I_0 \\ge \\frac{M_t}{G \\cdot \\theta_u} = \\frac{280\\,100}{80\\,000 \\times 8,727\\times10^{-6}} = \\frac{280\\,100}{0,6982} = 401\\,200\\ \\mathrm{mm^4} $$

Avec $d/D = 0,7$ : $I_0 = \\dfrac{\\pi D^4 (1 - 0,2401)}{32} = 0,07459\\, D^4$

$$ D^4 \\ge \\frac{401\\,200}{0,07459} = 5\\,378\\,700 \\;\\Longrightarrow\\; D \\ge \\sqrt[4]{5\\,378\\,700} = \\mathbf{48,2\\ mm} $$

**Solution retenue : tube Ø50 × Ø35 (épaisseur 7,5 mm).**

Vérifications finales :
- $I_0 = \\dfrac{\\pi(50^4 - 35^4)}{32} = \\dfrac{\\pi(6\\,250\\,000 - 1\\,500\\,625)}{32} = 466\\,300\\ \\mathrm{mm^4}$
- $\\theta_u = \\dfrac{280\\,100}{80\\,000 \\times 466\\,300} \\times 1\\,000 \\times \\dfrac{180}{\\pi} = \\mathbf{0,43°/m}$ ✔️
- $\\tau_{max} = \\dfrac{280\\,100 \\times 25}{466\\,300} = 15,0\\ \\mathrm{MPa}$ → $s_{réel} = 26$ ✔️ (très large)
- Masse : $S = \\dfrac{\\pi(50^2-35^2)}{4} = 1\\,001\\ \\mathrm{mm^2}$ → **9,43 kg**

**Bilan final — et c'est le message essentiel de l'exercice :**

En imposant la rigidité, l'arbre devient **plus lourd** que l'arbre plein initial (9,43 kg contre
6,66 kg). Le coefficient de sécurité en contrainte grimpe à 26, ce qui est absurde du point de vue
de la résistance seule.

> **Ce n'est pas une erreur : c'est la réalité des arbres de transmission longs.**
> Au-delà de ~1 m, la **rigidité en torsion** est presque toujours le critère dimensionnant, pas
> la résistance. C'est pourquoi les longues lignes d'arbre sont **fractionnées en tronçons courts
> avec des paliers intermédiaires**, plutôt que d'être surdimensionnées.

*Recommandation au BE : plutôt que d'adopter le Ø50, découper la transmission en deux tronçons de
600 mm avec un palier intermédiaire. L'angle serait alors divisé par 2 par tronçon, et l'arbre
Ø32×5 initial (4 kg) redeviendrait acceptable.*
""",
        },
        {
            "id": "4.3",
            "titre": "Flexion simple, moment quadratique et flèche",
            "duree": "12 h",
            "cours": """
### 1. La sollicitation la plus fréquente

La flexion est la sollicitation dominante de la mécanique : arbres, axes, poutres de charpente,
bras de robot, tablettes, essieux. C'est aussi celle qui **produit les plus grandes contraintes
pour un effort donné**, à cause de l'effet de **bras de levier**.

Un effort de 100 N appliqué en bout d'une poutre de 500 mm crée un moment de 50 N·m à
l'encastrement — bien plus destructeur que les 100 N de traction pure.

### 2. Torseur et diagrammes

En flexion simple, deux composantes sont non nulles : l'**effort tranchant** $T$ et le **moment
fléchissant** $M_f$. On trace systématiquement les deux diagrammes le long de la poutre.

**Relations fondamentales entre les diagrammes :**

$$ \\frac{dM_f}{dx} = T(x) \\qquad \\frac{dT}{dx} = -q(x) $$

**Conséquences pratiques (à exploiter en examen) :**
- $M_f$ est **maximal là où $T$ s'annule ou change de signe**. C'est la section dangereuse.
- Sous charge répartie, $T$ est linéaire et $M_f$ parabolique.
- Sous charge ponctuelle, $T$ est constant par morceaux et $M_f$ linéaire par morceaux.

### 3. Répartition de la contrainte : la clé de tout

$$ \\sigma(y) = \\frac{M_f \\cdot y}{I_{Gz}} $$

La contrainte varie **linéairement** dans la hauteur de la section :

```
        ┌───────────┐  ← σ MAXI (traction)
        │╲          │
   h    │  ╲        │
        ├────╲──────┤  ← FIBRE NEUTRE : σ = 0
        │      ╲    │
        │        ╲  │
        └───────────┘  ← σ MAXI (compression)
```

**La fibre neutre passe par le centre de gravité de la section, et n'y subit AUCUNE contrainte.**

**Les deux conséquences de conception qui découlent de cette figure :**

1. **La matière proche de la fibre neutre ne sert à rien** → on la retire.
   → poutres en **I**, en **U**, tubes, caissons.
2. **Il faut éloigner la matière de la fibre neutre** → l'inertie croît en $h^3$.
   → **doubler la hauteur d'une poutre rectangulaire multiplie sa résistance par 4 et sa
   rigidité par 8.**

**Corollaire immédiat, à ne jamais oublier :** une poutre rectangulaire posée **sur chant** est
bien plus performante que la même posée **à plat**. Pour une section 40×80 :
- sur chant ($h = 80$) : $I = \\frac{40 \\times 80^3}{12} = 1\\,706\\,667\\ \\mathrm{mm^4}$
- à plat ($h = 40$) : $I = \\frac{80 \\times 40^3}{12} = 426\\,667\\ \\mathrm{mm^4}$
→ **rapport 4** en rigidité, pour exactement la même quantité de matière.

### 4. La flèche

La flèche $f$ est le déplacement maximal de la poutre. Elle se calcule par intégration double de
l'équation de la déformée :

$$ E I \\frac{d^2 y}{dx^2} = M_f(x) $$

En pratique, **on utilise le formulaire** (voir onglet Formules). Il faut savoir **retrouver la
structure** de ces formules :

$$ f = k \\cdot \\frac{F L^3}{E I} \\qquad \\text{ou} \\qquad f = k \\cdot \\frac{q L^4}{E I} $$

**Points essentiels à retenir sur la flèche :**
- Elle varie en **$L^3$** (charge ponctuelle) ou **$L^4$** (charge répartie) : **doubler la portée
  multiplie la flèche par 8 ou 16.** C'est le paramètre le plus sensible, de très loin.
- Elle est inversement proportionnelle à **$E \\cdot I$**, appelée **rigidité en flexion**.
- **Changer de nuance d'acier ne change RIEN à la flèche** ($E$ identique). Il faut agir sur $I$
  (géométrie) ou sur $L$ (portée).

### 5. Critères usuels de flèche admissible

| Application | Flèche admissible |
|---|---|
| Charpente, plancher | $L/200$ à $L/300$ |
| Structure de machine | $L/500$ |
| Arbre de transmission (entre paliers) | $L/3000$ |
| Arbre portant un engrenage | **0,01 × module** au droit de la denture |
| Glissière de machine-outil | $L/5000$ |

### 6. Flexion combinée à d'autres sollicitations

En réalité, un arbre subit **flexion + torsion** simultanément. On calcule alors un **moment
idéal** (critère de Tresca ou de von Mises) :

$$ M_{idéal} = \\sqrt{M_f^2 + M_t^2} \\quad \\text{(Tresca)} $$

puis on dimensionne comme en flexion pure avec ce moment idéal. C'est la méthode employée dans
tous les bureaux d'études pour les arbres de réducteur.
""",
            "formules": """
**CONTRAINTE EN FLEXION**

$$ \\boxed{\\sigma_{max} = \\frac{M_f \\cdot v}{I_{Gz}} = \\frac{M_f}{I_{Gz}/v}} $$

$v$ = distance de la fibre neutre à la fibre la plus éloignée.
$I_{Gz}/v$ s'appelle le **module de flexion** (noté aussi $W$).

Condition de résistance : $\\sigma_{max} \\le R_{pe} = \\dfrac{R_e}{s}$

---

**MOMENTS QUADRATIQUES DES SECTIONS USUELLES**

| Section | $I_{Gz}$ | $v$ | $I_{Gz}/v$ |
|---|---|---|---|
| Rectangle $b \\times h$ | $\\dfrac{b h^3}{12}$ | $\\dfrac{h}{2}$ | $\\dfrac{b h^2}{6}$ |
| Cercle plein Ø$d$ | $\\dfrac{\\pi d^4}{64}$ | $\\dfrac{d}{2}$ | $\\dfrac{\\pi d^3}{32}$ |
| Tube $D$/$d$ | $\\dfrac{\\pi(D^4-d^4)}{64}$ | $\\dfrac{D}{2}$ | $\\dfrac{\\pi(D^4-d^4)}{32D}$ |
| Carré creux $B$/$b$ | $\\dfrac{B^4-b^4}{12}$ | $\\dfrac{B}{2}$ | $\\dfrac{B^4-b^4}{6B}$ |
| Rect. creux ext $b\\times h$, int $b_i \\times h_i$ | $\\dfrac{bh^3 - b_i h_i^3}{12}$ | $\\dfrac{h}{2}$ | — |

**Théorème de Huygens** (section composée, axe décalé de $d$) :
$$ I_{\\Delta} = I_G + S \\cdot d^2 $$

---

**FORMULAIRE DES FLÈCHES ET MOMENTS**

**Poutre sur 2 appuis, charge ponctuelle F au milieu**
$$ M_{f,max} = \\frac{FL}{4} \\quad (\\text{au milieu}) \\qquad f_{max} = \\frac{F L^3}{48 E I} $$

**Poutre sur 2 appuis, charge ponctuelle F à la distance $a$ (et $b = L-a$)**
$$ M_{f,max} = \\frac{F a b}{L} \\qquad f \\approx \\frac{F a^2 b^2}{3 E I L} \\;(\\text{sous la charge}) $$

**Poutre sur 2 appuis, charge répartie $q$ (N/mm)**
$$ M_{f,max} = \\frac{q L^2}{8} \\qquad f_{max} = \\frac{5 q L^4}{384 E I} $$

**Console (encastrée-libre), charge F en bout**
$$ M_{f,max} = F L \\quad (\\text{à l'encastrement}) \\qquad f_{max} = \\frac{F L^3}{3 E I} $$

**Console, charge répartie $q$**
$$ M_{f,max} = \\frac{q L^2}{2} \\qquad f_{max} = \\frac{q L^4}{8 E I} $$

**Poutre encastrée aux 2 extrémités, charge F au milieu**
$$ M_{f,max} = \\frac{FL}{8} \\qquad f_{max} = \\frac{F L^3}{192 E I} $$

*Noter le facteur 4 sur la flèche par rapport aux appuis simples : **l'encastrement rigidifie
énormément**. C'est un levier de conception souvent négligé.*

---

**FLEXION + TORSION COMBINÉES (arbres)**

Moment idéal de Tresca :
$$ \\boxed{M_{idéal} = \\sqrt{M_f^2 + M_t^2}} $$

Moment idéal de von Mises :
$$ M_{idéal} = \\sqrt{M_f^2 + 0,75\\, M_t^2} $$

Diamètre d'arbre plein :
$$ d \\ge \\sqrt[3]{\\frac{32 M_{idéal}}{\\pi R_{pe}}} $$

---

**RELATIONS DIAGRAMMES**

$$ \\frac{dM_f}{dx} = T(x) \\qquad \\frac{dT}{dx} = -q(x) \\qquad M_f = \\int T\\,dx $$
""",
            "exemple": """
**Cas industriel — Bras support de caméra de contrôle qualité**

Un bras en porte-à-faux supporte une caméra de **3,5 kg** en bout. Il est boulonné sur un montant
vertical (**encastrement**). Longueur **L = 650 mm**. Le cahier des charges impose une flèche
**≤ 0,3 mm** (au-delà, l'image se décale hors du champ de contrôle et le système de vision
déclenche des faux rejets).

Trois solutions sont mises en concurrence, **à masse voisine** :

| | **A** — Barre pleine acier | **B** — Tube acier | **C** — Profilé alu 40×40 |
|---|---|---|---|
| Section | Ø25 plein, S355 | Ø30×3, S355 | 40×40 rainuré, ép. 2, 6060 T6 |
| $S$ | 490,9 mm² | 254,5 mm² | ≈ 305 mm² |
| $I$ | 19 175 mm⁴ | 25 621 mm⁴ | ≈ 78 000 mm⁴ |
| $E$ | 210 000 MPa | 210 000 MPa | 69 000 MPa |
| $E\\!\\cdot\\!I$ | $4,03\\times10^9$ | $5,38\\times10^9$ | $5,38\\times10^9$ |
| Masse (0,65 m) | **2,50 kg** | **1,30 kg** | **0,54 kg** |

**Calcul de la flèche** — console avec charge en bout, $F = 3,5 \\times 9,81 = 34,3\\ \\mathrm{N}$ :

$$ f = \\frac{F L^3}{3 E I} = \\frac{34,3 \\times 650^3}{3 \\times E I} = \\frac{9,42 \\times 10^9}{3\\, E I} $$

| Solution | $f$ (charge seule) | Verdict |
|---|---|---|
| **A** — Ø25 plein | $\\dfrac{9,42\\times10^9}{1,21\\times10^{10}} = 0,78$ mm | ❌ **Refusé** (2,6× la limite) |
| **B** — Tube Ø30×3 | $\\dfrac{9,42\\times10^9}{1,61\\times10^{10}} = 0,58$ mm | ❌ Refusé |
| **C** — Profilé alu | $\\dfrac{9,42\\times10^9}{1,61\\times10^{10}} = 0,58$ mm | ❌ Refusé |

**Aucune ne passe !** Et il faut encore ajouter le **poids propre du bras**, qui aggrave la flèche.

**L'analyse qui fait la différence :** les solutions B et C ont **exactement la même rigidité
$E\\!\\cdot\\!I$**. L'aluminium compense son $E$ trois fois plus faible par un $I$ trois fois plus
grand — pour **2,4 fois moins de masse**. C'est l'indice $E^{1/2}/\\rho$ de la fiche 3.1 en action.

**Solution retenue par le BE : profilé aluminium 45×90 (rainuré, ép. 2,5)**
$$ I \\approx 640\\,000\\ \\mathrm{mm^4} \\;\\Rightarrow\\; f = \\frac{9,42\\times10^9}{3 \\times 69\\,000 \\times 640\\,000} = \\mathbf{0,071\\ mm} \\;✔️ $$
Masse : **1,05 kg**. Marge suffisante pour absorber le poids propre et les vibrations.

**Les trois leviers d'action mis en évidence, par ordre d'efficacité :**

| Levier | Effet sur la flèche | Coût de mise en œuvre |
|---|---|---|
| **Réduire la portée $L$** | en $L^3$ : passer de 650 à 500 mm divise $f$ par **2,2** | Souvent gratuit — repenser l'implantation |
| **Augmenter la hauteur de section $h$** | en $h^3$ | Faible — changer de profilé |
| **Rigidifier l'encastrement** ou ajouter un hauban | facteur 4 possible | Faible |
| **Changer de nuance d'acier** | **AUCUN effet** ($E$ identique) | Inutile |

**La conclusion opérationnelle :** face à un problème de flèche, le premier réflexe du concepteur
doit être *« puis-je raccourcir le porte-à-faux ? »* — pas *« quel acier plus résistant ? »*.
""",
            "exercice": """
**Exercice type examen — Poutre de manutention et arbre de réducteur**

**PARTIE A — Poutre de palan**

Une poutre en **IPE 160** (acier S275, $R_e = 275$ MPa, $E = 210$ GPa) repose sur **deux appuis**
distants de **L = 4 000 mm**. Un palan roule dessus et peut se positionner **au milieu**. Il
soulève une charge de **1 200 kg**.

*Caractéristiques de l'IPE 160 : $I_{Gz} = 8\\,690\\,000\\ \\mathrm{mm^4}$ ; $h = 160$ mm ;
masse linéique = 15,8 kg/m.*

Coefficient de sécurité (levage) : **s = 5**. Flèche admissible : **L/500**.

1. Calculer la charge $F$ appliquée (prendre $g = 9,81$ m/s²) et le poids propre réparti $q$.
2. Calculer le moment fléchissant maximal en cumulant la charge ponctuelle et le poids propre.
   Où se situe-t-il ?
3. Vérifier la condition de résistance.
4. Calculer la flèche totale et vérifier la condition de rigidité. Conclure.
5. Le service maintenance veut porter la charge à **2 000 kg**. Est-ce possible sans changer la
   poutre ? Si non, proposer **deux** solutions distinctes et chiffrer la plus efficace.

**PARTIE B — Arbre de réducteur (flexion + torsion)**

Un arbre en **42CrMo4** ($R_e = 750$ MPa) porte un pignon à mi-distance entre deux paliers
espacés de **L = 300 mm**. Il transmet **P = 15 kW** à **N = 900 tr/min**.
L'effort radial du pignon sur l'arbre vaut **F = 4 800 N**. Coefficient **s = 4**.

6. Calculer le couple de torsion $M_t$ et le moment fléchissant maximal $M_f$.
7. Calculer le moment idéal de Tresca.
8. Déterminer le diamètre minimal de l'arbre. Choisir un diamètre normalisé.
9. Une rainure de clavette ($K_t = 2,0$) est usinée au droit du pignon. Reprendre le calcul et
   conclure sur le diamètre définitif.
""",
            "corrige": """
**PARTIE A — POUTRE DE PALAN**

**1. Charges appliquées**

Charge ponctuelle du palan :
$$ F = m \\cdot g = 1\\,200 \\times 9,81 = \\mathbf{11\\,772\\ \\mathrm{N}} $$

Poids propre réparti (15,8 kg/m sur 4 m) :
$$ q = \\frac{15,8 \\times 9,81}{1\\,000} = \\mathbf{0,155\\ \\mathrm{N/mm}} $$
$$ \\text{soit un poids total de } 0,155 \\times 4\\,000 = 620\\ \\mathrm{N} $$

---

**2. Moment fléchissant maximal**

Les deux chargements produisent leur maximum **au milieu de la poutre** : on peut donc les
**superposer directement** (principe de superposition, valable en élasticité linéaire).

*Charge ponctuelle au milieu :*
$$ M_{f1} = \\frac{F L}{4} = \\frac{11\\,772 \\times 4\\,000}{4} = 11\\,772\\,000\\ \\mathrm{N\\cdot mm} $$

*Charge répartie :*
$$ M_{f2} = \\frac{q L^2}{8} = \\frac{0,155 \\times 4\\,000^2}{8} = \\frac{0,155 \\times 16\\times10^6}{8} = 310\\,000\\ \\mathrm{N\\cdot mm} $$

**Moment total :**
$$ M_{f,max} = 11\\,772\\,000 + 310\\,000 = \\mathbf{12\\,082\\,000\\ N\\cdot mm} = 12,08\\ \\mathrm{kN\\cdot m} $$

**Localisation : au MILIEU de la poutre** (x = 2 000 mm), là où l'effort tranchant s'annule.

*Le poids propre ne représente que 2,6 % du moment total — il est ici marginal, mais on l'inclut
par rigueur. Sur une poutre de 10 m, il deviendrait dominant.*

---

**3. Condition de résistance**

$$ R_{pe} = \\frac{R_e}{s} = \\frac{275}{5} = 55\\ \\mathrm{MPa} $$

Module de flexion de l'IPE 160 :
$$ v = \\frac{h}{2} = \\frac{160}{2} = 80\\ \\mathrm{mm} \\qquad \\frac{I_{Gz}}{v} = \\frac{8\\,690\\,000}{80} = 108\\,625\\ \\mathrm{mm^3} $$

$$ \\sigma_{max} = \\frac{M_{f,max}}{I_{Gz}/v} = \\frac{12\\,082\\,000}{108\\,625} = \\mathbf{111,2\\ \\mathrm{MPa}} $$

$$ 111,2\\ \\mathrm{MPa} \\;>\\; 55\\ \\mathrm{MPa} \\quad ❌ \\;\\; \\textbf{RÉSISTANCE NON VÉRIFIÉE} $$

Coefficient de sécurité réel :
$$ s_{réel} = \\frac{275}{111,2} = \\mathbf{2,47} \\quad \\text{au lieu des 5 exigés} $$

**La poutre est en dépassement d'un facteur 2.** En levage, ce coefficient de 5 n'est pas une marge
de confort : il est **réglementaire** (sécurité des personnes sous la charge). La configuration est
**non conforme en l'état**.

---

**4. Condition de rigidité**

Flèche admissible :
$$ f_{adm} = \\frac{L}{500} = \\frac{4\\,000}{500} = 8\\ \\mathrm{mm} $$

*Flèche due à la charge ponctuelle :*
$$ f_1 = \\frac{F L^3}{48 E I} = \\frac{11\\,772 \\times 4\\,000^3}{48 \\times 210\\,000 \\times 8\\,690\\,000} $$
$$ f_1 = \\frac{11\\,772 \\times 6,4\\times10^{10}}{8,76\\times10^{13}} = \\frac{7,534\\times10^{14}}{8,76\\times10^{13}} = 8,60\\ \\mathrm{mm} $$

*Flèche due au poids propre :*
$$ f_2 = \\frac{5 q L^4}{384 E I} = \\frac{5 \\times 0,155 \\times 4\\,000^4}{384 \\times 210\\,000 \\times 8\\,690\\,000} $$
$$ f_2 = \\frac{0,775 \\times 2,56\\times10^{11}}{7,008\\times10^{14}} = \\frac{1,984\\times10^{11}}{7,008\\times10^{14}} = 0,28\\ \\mathrm{mm} $$

**Flèche totale :**
$$ f_{tot} = 8,60 + 0,28 = \\mathbf{8,88\\ mm} $$

$$ 8,88\\ \\mathrm{mm} \\;>\\; 8\\ \\mathrm{mm} \\quad ❌ \\;\\; \\textbf{RIGIDITÉ NON VÉRIFIÉE} $$

**CONCLUSION GÉNÉRALE : l'IPE 160 est INSUFFISANT sur les deux critères.**
La résistance est dépassée d'un facteur 2, la flèche de 11 %. **La poutre doit être changée.**

---

**5. Passage à 2 000 kg — analyse et solutions**

Nouvelle charge :
$$ F' = 2\\,000 \\times 9,81 = 19\\,620\\ \\mathrm{N} \\quad (\\times 1,67) $$

$$ M_{f}' = \\frac{19\\,620 \\times 4\\,000}{4} + 310\\,000 = 19\\,620\\,000 + 310\\,000 = 19\\,930\\,000\\ \\mathrm{N\\cdot mm} $$

$$ \\sigma' = \\frac{19\\,930\\,000}{108\\,625} = 183,5\\ \\mathrm{MPa} \\;\\gg\\; 55\\ \\mathrm{MPa} $$

$$ f' = 8,60 \\times \\frac{19\\,620}{11\\,772} + 0,28 = 14,33 + 0,28 = 14,6\\ \\mathrm{mm} \\;\\gg\\; 8\\ \\mathrm{mm} $$

$$ \\boxed{\\textbf{IMPOSSIBLE sans modification. Dépassement d'un facteur 3,3 en contrainte.}} $$

---

**SOLUTION 1 — Changer de profilé**

Il faut satisfaire **les deux** conditions ; on retient l'exigence la plus forte.

*Critère de résistance :*
$$ \\frac{I}{v} \\ge \\frac{M_f'}{R_{pe}} = \\frac{19\\,930\\,000}{55} = 362\\,364\\ \\mathrm{mm^3} $$

*Critère de rigidité :*
$$ I \\ge \\frac{F' L^3}{48 E f_{adm}} + \\text{(part du poids propre)} \\approx \\frac{19\\,620 \\times 6,4\\times10^{10}}{48 \\times 210\\,000 \\times 8} = \\frac{1,256\\times10^{15}}{8,064\\times10^{7}} $$
$$ I \\ge 15\\,575\\,000\\ \\mathrm{mm^4} $$

**Choix : IPE 270** ($I = 57\\,900\\,000\\ \\mathrm{mm^4}$ ; $I/v = 428\\,900\\ \\mathrm{mm^3}$ ; 36,1 kg/m)

Vérifications :
- Résistance : $\\sigma = \\dfrac{19\\,930\\,000 + \\text{poids propre majoré}}{428\\,900} \\approx 47,0\\ \\mathrm{MPa} \\le 55$ ✔️
- Rigidité : $f = \\dfrac{19\\,620 \\times 6,4\\times10^{10}}{48 \\times 210\\,000 \\times 57\\,900\\,000} + f_{pp} = 2,15 + 0,10 = \\mathbf{2,25\\ mm} \\le 8$ ✔️

*Marge très confortable ; on pourrait tenter l'IPE 240, mais l'IPE 270 est un profilé courant et
la différence de prix est faible au regard de l'enjeu sécurité.*

---

**SOLUTION 2 — Réduire la portée en ajoutant un appui intermédiaire**

En plaçant un poteau au milieu, on obtient **deux travées de 2 000 mm**. Pour une charge ponctuelle
au milieu d'une travée de $L/2$ :

$$ M_f'' = \\frac{F' \\times (L/2)}{4} = \\frac{19\\,620 \\times 2\\,000}{4} = 9\\,810\\,000\\ \\mathrm{N\\cdot mm} $$

$$ \\sigma'' = \\frac{9\\,810\\,000 + 78\\,000}{108\\,625} = \\mathbf{91,0\\ MPa} $$

Toujours $> 55$ MPa ❌ — **insuffisant seul**, mais la flèche s'effondre :

$$ f'' = \\frac{19\\,620 \\times 2\\,000^3}{48 \\times 210\\,000 \\times 8\\,690\\,000} = \\frac{1,57\\times10^{14}}{8,76\\times10^{13}} = \\mathbf{1,79\\ mm} \\;✔️ $$

*(divisée par 8, conformément à la loi en $L^3$)*

---

**Comparaison chiffrée des deux solutions**

| | **Solution 1** — IPE 270 | **Solution 2** — Appui central |
|---|---|---|
| Contrainte | 47,0 MPa ✔️ | 91,0 MPa ❌ |
| Flèche | 2,25 mm ✔️ | 1,79 mm ✔️ |
| Masse d'acier | 144 kg (36,1 × 4) | 63 kg + poteau |
| Coût | Poutre neuve + dépose/repose | Poteau + génie civil |
| **Contrainte d'usage** | Aucune | **Le poteau coupe l'aire de travail en deux** |
| Conformité finale | ✅ **Conforme** | ❌ Non conforme seule |

**RECOMMANDATION : Solution 1 (IPE 270).**

*Justification :* la solution 2 divise la flèche par 8 mais la contrainte seulement par 2 — elle ne
suffit pas à atteindre le coefficient réglementaire de 5. Surtout, le poteau central **obstrue
l'aire de manutention**, ce qui est rédhibitoire pour un palan dont l'intérêt est précisément de
balayer toute la travée.

**Enseignement à tirer :** l'appui intermédiaire est un levier **spectaculaire sur la flèche**
($\\div 8$) mais **modeste sur la contrainte** ($\\div 2$). Quand c'est la résistance qui pèche —
comme ici — **il faut changer la section**, pas la portée.

---

**PARTIE B — ARBRE DE RÉDUCTEUR**

**6. Couple et moment fléchissant**

*Couple de torsion :*
$$ \\omega = \\frac{2\\pi \\times 900}{60} = 94,25\\ \\mathrm{rad/s} $$
$$ M_t = \\frac{P}{\\omega} = \\frac{15\\,000}{94,25} = 159,2\\ \\mathrm{N\\cdot m} = \\mathbf{159\\,200\\ N\\cdot mm} $$

*Moment fléchissant* (charge au milieu de deux appuis) :
$$ M_f = \\frac{F L}{4} = \\frac{4\\,800 \\times 300}{4} = \\mathbf{360\\,000\\ N\\cdot mm} $$

*Observation :* $M_f$ est **2,3 fois plus grand** que $M_t$. C'est le cas général sur un arbre de
réducteur : **la flexion domine la torsion**. Négliger la flexion serait une faute grave.

---

**7. Moment idéal de Tresca**

$$ M_{idéal} = \\sqrt{M_f^2 + M_t^2} = \\sqrt{360\\,000^2 + 159\\,200^2} $$

$$ M_{idéal} = \\sqrt{1,296\\times10^{11} + 2,534\\times10^{10}} = \\sqrt{1,549\\times10^{11}} $$

$$ \\boxed{M_{idéal} = 393\\,600\\ \\mathrm{N\\cdot mm}} $$

---

**8. Diamètre minimal**

$$ R_{pe} = \\frac{R_e}{s} = \\frac{750}{4} = 187,5\\ \\mathrm{MPa} $$

$$ \\sigma = \\frac{M_{idéal}}{\\pi d^3/32} \\le R_{pe} \\;\\Longrightarrow\\; d \\ge \\sqrt[3]{\\frac{32 M_{idéal}}{\\pi R_{pe}}} $$

$$ d \\ge \\sqrt[3]{\\frac{32 \\times 393\\,600}{\\pi \\times 187,5}} = \\sqrt[3]{\\frac{12\\,595\\,200}{589,05}} = \\sqrt[3]{21\\,382} $$

$$ d \\ge \\mathbf{27,7\\ \\mathrm{mm}} $$

**Diamètre normalisé retenu (avant prise en compte de la clavette) : Ø30 mm.**

---

**9. Prise en compte de la rainure de clavette ($K_t = 2,0$)**

La rainure est **au droit du pignon**, c'est-à-dire exactement à l'endroit où $M_f$ est maximal.
Le cumul est donc le plus défavorable possible.

**Méthode 1 — vérification du Ø30 :**
$$ \\frac{I}{v} = \\frac{\\pi \\times 30^3}{32} = 2\\,650\\ \\mathrm{mm^3} $$
$$ \\sigma_{nom} = \\frac{393\\,600}{2\\,650} = 148,5\\ \\mathrm{MPa} $$
$$ \\sigma_{max} = K_t \\times \\sigma_{nom} = 2,0 \\times 148,5 = \\mathbf{297\\ MPa} $$

$$ 297\\ \\mathrm{MPa} \\;>\\; 187,5\\ \\mathrm{MPa} \\quad ❌ \\;\\; \\textbf{INSUFFISANT} $$

**Méthode 2 — recalcul direct du diamètre :**
$$ d \\ge \\sqrt[3]{\\frac{32 \\times K_t \\times M_{idéal}}{\\pi R_{pe}}} = 27,7 \\times \\sqrt[3]{2,0} = 27,7 \\times 1,26 = \\mathbf{34,9\\ mm} $$

**Diamètre définitif retenu : Ø40 mm.**

*Pourquoi Ø40 et pas Ø35 ?*
- Ø35 satisfait tout juste le calcul (34,9 mm), sans marge ;
- **Ø40 correspond à un roulement standard** (6208, 6008) et à une clavette normalisée 12×8 ;
- l'arbre subit de la **fatigue** (rotation → flexion alternée), domaine où $K_t$ agit pleinement
  et où toute marge supplémentaire est bienvenue.

**Vérification finale à Ø40 :**
$$ \\frac{I}{v} = \\frac{\\pi \\times 40^3}{32} = 6\\,283\\ \\mathrm{mm^3} $$
$$ \\sigma_{nom} = \\frac{393\\,600}{6\\,283} = 62,6\\ \\mathrm{MPa} \\;;\\quad \\sigma_{max} = 2,0 \\times 62,6 = 125,2\\ \\mathrm{MPa} $$
$$ 125,2 \\le 187,5 \\quad ✔️ \\qquad s_{réel} = \\frac{750}{125,2} = \\mathbf{6,0} $$

---

**SYNTHÈSE DE L'EXERCICE — les trois réflexes à retenir**

| Étape | Diamètre | Ce que révèle l'étape |
|---|---|---|
| Torsion seule | ~21 mm | Très insuffisant — **ne jamais s'arrêter là** |
| Flexion + torsion (Tresca) | 27,7 mm | La flexion domine sur un arbre de réducteur |
| **+ concentration de contrainte** | **34,9 → Ø40** | **La clavette impose +26 % de diamètre** |

> **Le message central du bloc RDM :** un calcul de sollicitation simple donne un **ordre de
> grandeur**, jamais une cote de plan. Le diamètre réel sort de la combinaison des sollicitations,
> des concentrations de contrainte, des composants standards disponibles, et — pour une pièce
> tournante — de la tenue en fatigue.

**Recommandation de conception :** utiliser une clavette à **fond arrondi** ($K_t = 1,6$ au lieu de
2,0) permettrait de revenir à Ø35. Encore mieux : remplacer la clavette par un **frettage** ou un
**moyeu conique**, qui supprime totalement l'entaille — c'est la solution retenue sur les
transmissions à fort couple et haute fiabilité.
""",
        },
    ],
}
