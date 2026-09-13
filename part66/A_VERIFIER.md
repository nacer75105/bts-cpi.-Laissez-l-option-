# Points à vérifier avant de considérer le contenu Part-66 comme définitif

Ce fichier liste, module par module, les points qui n'ont pas pu être
confirmés avec certitude au moment de la rédaction. Pour un module
réglementaire (M10) il s'agit le plus souvent d'une référence légale
précise (article, annexe) à retrouver ; pour un module technique (M5) il
s'agit plutôt d'un point de contenu plus spécifiquement avionique, sur
lequel la confiance est moindre que sur les bases scientifiques
universelles du module (voir la section « Nature des sources » du module
M5 ci-dessous). Le principe général de chaque question concernée reste
solide ; c'est la précision de la référence ou de la formulation qui doit
être confirmée avant un usage en conditions d'examen réel.

## Audit de couverture du syllabus officiel EASA — feuille de route (2026-09-13)

Après l'enrichissement de M17A à partir d'une fiche externe (voir plus
bas), l'utilisateur a demandé un audit de couverture des 6 modules
construits contre le syllabus officiel EASA — *Easy Access Rules for
Continuing Airworthiness (Regulation (EU) No 1321/2014)*, révision
**septembre 2025**, Appendix I to Part-66 (section AMC1, la plus
détaillée : sous-thèmes en prose par item, pas seulement les intitulés).
Même document déjà utilisé pour sourcer les niveaux M7A et le format
d'examen des 6 modules (voir plus bas dans ce fichier). Colonne **B1.1**
utilisée partout (licence préparée par ce projet).

**Ceci est un état des lieux, pas un plan de correction.** Rien n'a été
modifié suite à cet audit ; c'est une feuille de route pour de futures
sessions, à traiter module par module, probablement en plusieurs
chantiers séparés compte tenu du volume. Un item listé « non couvert »
n'est pas nécessairement urgent — le classement par niveau (1/2/3) aide à
prioriser : un manque sur un item niveau 3 pèse plus qu'un manque sur un
item niveau 1.

**Réserve méthodologique sur M11A** : l'extraction texte de la section
détaillée désaligne par endroits les colonnes de niveaux sur les items à
nombreuses sous-parties (11.7, 11.9, 11.13, 11.14 notamment) — les
niveaux cités pour M11A s'appuient sur le tableau réglementaire compact,
plus fiable, mais restent à confirmer visuellement avant de prioriser
finement dessus.

### M5 — Techniques numériques / systèmes d'instruments électroniques (9 fiches / 15 items officiels)

**Non couvert :**
- **5.4** Réseau avionique/Ethernet (AFDX) — M5.7 couvre ARINC 429 mais
  pas les réseaux modernes de type Ethernet embarqué.
- **5.11** Principes de fonctionnement des technologies d'affichage
  (CRT/LED/LCD) — M5.9 décrit le glass cockpit fonctionnellement, jamais
  comment ces écrans fonctionnent réellement.
- **5.15** Sur ~11 systèmes nommés par le syllabus (ACARS, FBW, FMS, IRS,
  GNSS, TCAS, avionique modulaire intégrée, systèmes cabine, systèmes
  d'information...), seuls 3 sont couverts (EFIS, ECAM, EICAS) dans M5.9.

**Superficiel :** 5.14 (EMC/HIRF couverts, mais protection foudre et le
sigle EMI distinctement nommé absents).

### M7A — Pratiques de maintenance (10 fiches + mémo / 21 items officiels)

Le déficit le plus large du lot (syllabus très dense, 21 items dont
plusieurs jamais traités).

**Non couvert :**
- **7.1** : sécurité fosse à carburant (accès en espace confiné),
  aéronefs équipés d'un parachute de secours balistique.
- **7.3** : instruments de mesure de précision (pied à coulisse,
  micromètre) et matériel électrique de test — jamais traités en fiche.
- **7.14** : les 3 sous-items (tôlerie, composite, fabrication additive)
  — absents en bloc (7.14.3 déjà noté par ailleurs dans ce fichier,
  7.14.1 et 7.14.2 identifiés seulement par cet audit).
- **7.17** : remorquage/roulage, calage/blocage, ravitaillement/dépose
  carburant, groupes de parc électrique/hydraulique/pneumatique — seule
  la manutention générique est couverte (ajout du 2026-09-13).
- **7.19** (événements anormaux : foudre, atterrissage dur), **7.20**
  (procédures de maintenance : planification, modification, pièces à
  vie limitée), **7.21** (documentation/communication) — trois items
  entiers absents.

**Superficiel :** 7.18 (CND décrit génériquement, sans nommer les 5
méthodes du syllabus dont le ressuage magnétoscopique).

### M10 — Législation aéronautique (8 fiches / 10 items officiels, très denses)

**→ Comblé le 2026-09-13** (13 fiches, mapping officiel 10.1-10.10 complet)
— voir la section dédiée « M10 — comblement des manques du syllabus
(2026-09-13) » plus bas pour le détail fiche par fiche, les sources
utilisées, et les deux limites de sourçage assumées (CDL, EMAR).

**Le module le plus daté par rapport à la réforme (UE) 2023/989** — déjà
pressenti lors du travail sur le format d'examen (voir plus bas), confirmé
ici sur le fond :

- **10.4 Personnel certificateur indépendant (niveau 3, le plus élevé du
  module)** — absent en totalité.
- **10.1** : Part 21, Part-T, Part-ML, **Part-CAMO, Part-CAO** (la
  scission CAMO/CAO hors du Part-M — cohérente avec le doute déjà noté
  sur M10-0017/M10-0020 et sur le rattachement du CAMO en M17A), règlement
  Air Ops (UE 965/2012), règlement Air Crew (UE 1178/2011), *soft law*
  (AMC/GM/CS) vs *hard law*, signalement d'événements (UE 376/2014),
  accords bilatéraux — aucun mentionné.
- **10.5** : AOC, MEL/CDL, placardage, ARC (*Airworthiness Review
  Certificate* — document différent du CofA, jamais mentionné), Permit
  to Fly, licence radio — absents (seuls CofA/CofR/masse-centrage/bruit
  sont couverts).
- **10.6** Part 21 et spécifications de certification (CS-23/25/27...) —
  absent.
- **10.10** Cybersécurité en maintenance — absent (item récent, ajouté
  par la réforme 2023/989).

**Superficiel :** 10.2 (licences/privilèges décrits sans profondeur
d'exercice), 10.7 (Part-M couvert mais hors cadre Part-ML/CAMO/CAO).

### M11A — Aérodynamique, structures et systèmes (25 fiches / ~21 items, 60+ sous-thèmes — audité par un agent dédié)

**7 chapitres ATA entiers non couverts** : ATA 25 (équipements/
aménagements cabine), ATA 33 (éclairage), ATA 38 (eau/déchets), ATA 42
(avionique modulaire intégrée), ATA 44 (systèmes cabine), ATA 45
(systèmes de maintenance embarqués), ATA 46 (systèmes d'information).

**Dispositifs isolés non couverts**, dont plusieurs classiquement testés
en examen : *gust lock*, *yaw damper*, *Mach trim*, équilibrage/rigging
des gouvernes (11.9, niveau 3), largage carburant d'urgence (11.10),
*tail skids*/*autobraking*/pneus/détection air-sol (11.13), dispositifs de
remorquage planeur (11.3.1, niveau 3), classification structurale
primaire/secondaire/tertiaire et concepts *fail-safe*/*safe-life*/
*damage-tolerance* (11.2).

**Superficiel :** communications/navigation individuelles non nommées
(11.5.2 : VHF, HF, SATCOM, CPDLC, ELT, CVR, VOR, ADF, ILS, MLS, DME,
transpondeur, TCAS, radar météo, radioaltimètre), inertage réservoir
(11.10), onduleurs/régulation de tension (11.6), système de chargement
du fret (11.3.1(c), niveau 3), protection de surface — chromatation/
anodisation (11.2(c)).

**Le cœur technique reste solide** : hydraulique, train d'atterrissage
(hors pneus/autobraking), conditionnement d'air, givre/pluie, carburant
cellule (hors largage/inertage), instruments de vol, incendie, portes
(hors sièges/fenêtres), maintenance cellule/CND — bien couverts, parfois
au-delà du niveau exigé. Les manques se concentrent sur le confort
cabine/avionique récente et une poignée de dispositifs de sécurité en
commandes de vol.

### M15 — Turbomachines à gaz (14 fiches / 22 items officiels)

**Non couvert :**
- **15.2** Performances moteur (poussée brute/nette, taux de dilution,
  consommation spécifique, régimes/limitations) — jamais traité comme
  sujet propre.
- **15.15** Architectures alternatives (turbofan à réducteur, open rotor,
  hybride électrique).
- **15.16 / 15.17 / 15.18** Turbopropulseurs, turbomoteurs, APU —
  chacun absent comme sujet dédié (l'APU n'apparaît qu'en passant comme
  source d'air de démarrage en M15.9).
- **15.19** Installation motrice (pare-feu, supports moteur, câblage,
  points de levage).
- **15.22** Stockage et conservation du moteur (l'équivalent existe pour
  l'hélice en M17A.14, pas pour le moteur).

**Superficiel :**
- **15.1** : le terme « cycle de Brayton » n'est jamais nommé ; les 5
  architectures moteur (turboréacteur/turbofan/turbopropulseur/
  turbomoteur/geared turbofan) ne sont jamais comparées comme
  fondamentaux.
- **15.4** : contrôle de l'écoulement (vannes de décharge, aubes de
  stator/entrée variables) absent.
- **15.9** : propriétés/spécifications des carburants et lubrifiants
  (grades, additifs) non traitées — seule l'architecture des circuits
  est couverte.
- **15.21 (niveau 3, le plus élevé du module)** : lavage/nettoyage du
  compresseur absent ; le run-up comme procédure formelle sous-développé
  malgré le niveau exigé.

### M17A — Hélices (15 fiches / 7 items officiels — le mieux couvert après l'enrichissement du 2026-09-13)

**Superficiel seulement**, tout le reste étant désormais couvert en
profondeur après les ajouts du jour (construction, commande de pas,
synchronisation, givre, entretien, stockage) :
- **17.1** : « angle d'attaque » n'est jamais nommé comme tel (choix
  délibéré, déjà documenté plus bas — cohérence du vocabulaire du module
  privilégiée à la reprise littérale de la fiche externe) ; vibrations/
  résonance et le repère visuel de l'arc rouge au compte-tours ne sont
  pas traités (présents dans la fiche externe analysée, non retenus lors
  de l'intégration sélective du 2026-09-13).

### Priorisation suggérée pour une reprise future

Par ordre approximatif d'impact (item niveau 3 absent > item niveau 2
absent en bloc > superficiel) : ~~**M10** (10.4 niveau 3 absent, plus tout
le paysage réglementaire post-2023/989 jamais intégré)~~ **comblé le
2026-09-13** (voir section dédiée) et **M7A** (3
items entiers absents sur un total de seulement 21, dont un impact
pratique direct — sécurité fosse carburant, outillage de mesure) semblent
les chantiers les plus rentables à reprendre en premier. **M11A**, malgré
son volume de manques bruts, a un cœur technique déjà solide — les
manques y sont plus concentrés sur du contenu périphérique (confort
cabine, avionique récente) que sur la sécurité de vol directe, à
l'exception du groupe commandes de vol (11.9). **M15** et **M5** ont des
manques ciblés, plus rapides à combler individuellement. **M17A** peut
attendre.

## M10 — comblement des manques du syllabus (2026-09-13)

Chantier demandé explicitement pour combler les manques identifiés par
l'audit de couverture ci-dessus, sur la base des 4 documents EASA
officiels téléchargés cette session (aucune affirmation réglementaire
issue de la mémoire — chaque point cite un article vérifié) :

- `easa_2025.txt` — *Easy Access Rules for Continuing Airworthiness*
  (Reg. 1321/2014), rév. sept. 2025.
- `part21_2025.txt` — *Easy Access Rules for Initial Airworthiness and
  Environmental Protection* (Reg. 748/2012), rév. 28 nov. 2025.
- `airops_2026.txt` — *Easy Access Rules for Air Operations*
  (Reg. 965/2012), rév. 27 mars 2026.
- `aircrew_2025.txt` — *Easy Access Rules for Aircrew* (Reg. 1178/2011),
  rév. 26 nov. 2025.

**Trouvaille clé** : le texte intégral et officiel du syllabus Module 10
(Appendix I à l'Annexe III, p.601-603 de `easa_2025.txt`) était présent
dans le document déjà téléchargé — avec les niveaux exacts par item. Il a
remplacé toute estimation antérieure. Deux items officiels (**10.8**
« Oversight principles » et **10.9** « Maintenance beyond current EU
regulations ») n'étaient PAS dans la liste de manques initiale de
l'utilisateur : ils ont été découverts pendant la recherche et ajoutés
au chantier avec son accord explicite.

### Mapping fiche ↔ item officiel (13 fiches, décision structurelle)

Les identifiants de fiche (M10.1-M10.13) restent **séquentiels**, pas
renumérotés pour coller 1:1 aux items officiels (l'item 10.1 couvre à
lui seul 3 fiches historiques, et M10.7/Part-147 ne correspond à aucun
item officiel isolé). À la place, chaque fiche affiche désormais un
badge **« Item officiel »** dans sa légende (voir `part66/ui.py`,
champ `item_syllabus` ajouté au schéma des fiches, à côté du niveau) :

| Fiche | Item officiel | Niveau | Statut |
|---|---|---|---|
| M10.1 OACI | 10.1 | 1 | inchangée |
| M10.2 AESA/DGAC | 10.1 | 1 | étendue (hard/soft law, 376/2014, accords bilatéraux) |
| M10.3 Vue d'ensemble 1321/2014 | 10.1 | 1 | étendue (Part-T/ML/CAMO/CAO, Basic Reg, Air Ops/Air Crew) |
| M10.4 Part-M/ML/CAMO/CAO | 10.7 | 2 | **corrigée** (règle de responsabilité M.A.201) + étendue (AMP, AD/bulletin déplacés depuis M10.8) |
| M10.5 Part-145/Part-CAO | 10.3 | 2 | étendue (Part-CAO) |
| M10.6 Part-66 catégories | 10.2 | 2 | inchangée |
| M10.7 Part-147 | 10.1 (complément) | 1 | inchangée |
| M10.8 Air operations | 10.5 | 1 | **réécrite** (AOC, auto-déclaration, ETOPS/CAT II-III/BRNAV, MEL/CDL, placardage, ARC, Permit to Fly, licence radio) |
| M10.9 Personnel certificateur indépendant *(nouvelle)* | 10.4 | 3 | créée |
| M10.10 Part 21 + CS *(nouvelle)* | 10.6 | 2 | créée |
| M10.11 Principes de surveillance *(nouvelle)* | 10.8 | 1 | créée |
| M10.12 Maintenance au-delà de la réglementation UE *(nouvelle)* | 10.9 | 1 | créée, contenu volontairement minimal |
| M10.13 Cybersécurité *(nouvelle)* | 10.10 | 1 | créée |

### Correction factuelle appliquée

M10.4 affirmait que l'**exploitant** (ou le propriétaire pour l'aviation
légère) est responsable par défaut du maintien de navigabilité. C'est
l'inverse de M.A.201(a) : le **propriétaire** est responsable par
défaut ; le transfert à l'exploitant ne se fait que dans des cas définis
(location M.A.201(b), transporteur licencié 1008/2008 M.A.201(e)). Même
erreur, même référence, que celle déjà trouvée et corrigée cette session
dans un sujet de rédaction M7A — jamais corrigée ici jusqu'à présent. La
banque de questions (M10-0016) avait déjà la bonne règle ; seule la
fiche était fausse.

### Deux limites de sourçage assumées (contenu volontairement minimal)

- **CDL (Configuration Deviation List)** : aucun article de définition
  autonome trouvé dans `airops_2026.txt`, contrairement au MEL
  (ORO.MLR.105) — le CDL n'y apparaît que par référence croisée
  opérationnelle (ex. CAT.OP.MPA.175(b)(2)). La fiche M10.8 la mentionne
  donc de façon générale, sans article dédié à l'appui.
- **EMAR 66 / aéronefs Annexe I (item 10.9)** : le sigle EMAR
  n'apparaît que dans la phrase même du syllabus officiel
  (`easa_2025.txt`, Appendix I, item 10.9) — aucun article de fond,
  dans aucun des 4 documents, ne le développe. La fiche M10.12 reste
  donc délibérément générale sur ce point (pas d'organisme gestionnaire
  cité, pas de détail sur la liste des aéronefs Annexe I), conformément
  à la règle du chantier : si la source ne précise pas, on ne l'invente
  pas.

### Contenu ajouté

- 5 fiches créées (M10.9 à M10.13), 5 fiches étendues (M10.2, M10.3,
  M10.4, M10.5, M10.8 réécrite), 1 correction factuelle (M10.4), 10
  schémas HTML/CSS/JS créés (2 par nouvelle fiche, aucun `<svg>`, aucune
  génération de DOM à l'exécution — vérifié par sweep `grep -l "<svg"`),
  50 nouvelles questions après relecture (banque totale : 37 → 87 ; un
  doublon supprimé sur les 51 créées initialement), 2 questions
  existantes (M10-0038 AD, M10-0039 bulletin de service) retaguées de
  `sous_chapitre: "M10.8"` vers `"M10.4"` pour suivre le déplacement du
  paragraphe correspondant dans la fiche.
- Format d'examen (`nb_questions_examen`/`duree_examen_min` dans
  `logic.py`) inchangé : ces valeurs viennent d'Appendix II du même
  document officiel et ne dépendent pas du nombre de fiches ou de
  questions en banque.
- Test headless (`AppTest`) : aucune exception sur les 6 modules
  (rendu initial) ni sur le rendu complet des 13 fiches + 10 schémas de
  M10 (onglet Cours).

### Relecture `relecteur-part66` (2026-09-13) — 10 BLOQUANT corrigés

- **Date fausse** : la fiche M10.3 et la question M10-0044 disaient
  « réforme de 2023 » pour l'ajout de Part-T/ML/CAMO/CAO — en réalité
  Part-T vient du règlement (UE) 2015/1536 et Part-ML/CAMO/CAO du
  règlement (UE) 2019/1383. Corrigé dans la fiche et la question.
- **Exemple d'accord bilatéral faux** (M10.2, M10-0043) : Part-T
  s'applique quand la surveillance d'un aéronef pays tiers **n'a pas**
  été déléguée à un État membre (Articles 1(b)/3(6) du 1321/2014
  lui-même), pas en vertu d'un accord bilatéral. Remplacé par
  l'exemple réellement sourcé (TSO FAA acceptés par l'AESA).
- **« Just culture »** (M10.2, M10-0042) : le détail « sauf négligence
  grave ou faute intentionnelle » n'est écrit nulle part dans les 4
  documents sourcés — c'était une affirmation issue de la mémoire,
  malgré la règle absolue du chantier. Retiré ; reformulé sur ce qui
  est réellement vérifiable (confidentialité, signalement franc).
- **DOA présenté comme systématiquement obligatoire** (M10.10,
  M10-0074, `schemas/M10.10.html`) : 21.A.14(b)/(c) prévoit des voies
  allégées pour les ELA1/ELA2, moteurs à pistons, hélices à pas
  fixe/réglable. Fiche, question et schéma corrigés.
- **CS-STAN** (M10-0073) : l'explication disait à tort qu'elle ne vise
  « aucun segment d'aéronefs en particulier » — 21.A.90B(a)(1) la
  limite au contraire à un segment précis (≤ 5 700 kg, etc.). Corrigé.
- **Mauvais alinéa** (M10-0065) : CAO.A.040(b), pas (c).
- **Confusion entre deux délais distincts de M.A.801(c)** (M10.9,
  M10-0063) : la nouvelle APRS de contrôle (7 jours à compter de la
  première APRS) et la notification à l'organisme CAM/autorité (7
  jours à compter de l'autorisation) sont deux obligations séparées,
  fusionnées à tort dans la fiche et la question. Fiche réécrite avec
  le détail complet de M.A.801(c) (qui peut être autorisé par le
  propriétaire, à quelles conditions).
- **Mauvaises références MEL/placardage** (M10-0056) : AMC1
  ORO.MLR.105(d)(1) point (f), pas (d)(3) ; M.A.901(m)(1) concerne les
  marquages de la définition de type lors de la revue de navigabilité,
  pas le placardage MEL — retiré, gardé seulement la référence exacte.
- **Restricted CofA confondu avec Permit to Fly** (M10.8) : ce sont
  deux documents différents (21.A.173(b) vs 21.A.701(a)) — scindés en
  deux puces distinctes.
- **Appendice VII mal illustré** (`schemas/M10.9-2.html`) : une roue
  figure bien au point 1(r) de l'Appendice VII — la nuance est la
  **méthode** (rivetage/collage/soudage), pas la pièce elle-même ;
  l'équilibrage d'hélice a deux exceptions explicites (statique exigé
  par le manuel, dynamique sur hélice installée avec équipement
  électronique) qui n'étaient pas mentionnées. Corrigé.

Corrections mineures appliquées en plus : sources complétées
(M10-0041, M10-0023 — TODO remplacé), doublon supprimé (M10-0051,
recoupait M10-0045), M10-0048 reformulée (source non réglementaire
remplacée par M.A.302(c), angle distinct de M10-0019), cohérence
M10-0011/M10-0044 (4 annexes historiques « parmi les huit »), et un
passage de reformulation sur ~20 questions pour retirer des mots
absolus (« Uniquement », « Systématiquement », « sans exception ») ou
des distracteurs trop absurdes, qui rendaient certaines questions
devinables sans connaissance du domaine.

Deux limites de sourçage assumées (CDL, EMAR 66) confirmées non
signalées comme trous par la relecture — conformes à la règle du
chantier.

### Reste à faire avant commit

`eleve-adversaire` sur les 87 questions (banque finale), puis test
local par l'utilisateur avant tout push (consigne explicite de ce
chantier).

## Module M10 — questions concernées

Relecture du 2026-09-09 par le sous-agent `relecteur-part66` (3 rounds) :
13 questions ont un champ `source` marqué `"TODO: source à vérifier
manuellement"` dans `questions.json`. Le contenu (question, options, bonne
réponse, explication) n'est pas remis en cause sur le principe — seule la
référence réglementaire précise manque, ou un doute ponctuel sur une
terminologie ou une formulation est signalé. Personne n'a réécrit ces
sources depuis la mémoire d'un modèle : elles doivent être confirmées
directement dans les textes avant d'être considérées comme fiables pour un
usage en conditions d'examen réel.

**Point confirmé (retiré de cette liste)** : la correspondance annexe I →
Part-M, annexe II → Part-145, annexe III → Part-66, annexe IV → Part-147 du
règlement (UE) n° 1321/2014 a été vérifiée manuellement par l'utilisateur
(2026-09-09) et est confirmée exacte. M10-0014 et les questions qui citent
cette correspondance dans leur source n'ont plus besoin de vérification sur
ce point précis.

- **M10-0002** — L'obligation de transposition/notification des Annexes
  OACI est correcte sur le principe, mais figure probablement dans le corps
  de la Convention de Chicago (articles 37/38), pas dans les Annexes
  elles-mêmes comme le dit actuellement la source. Non vérifié.

- **M10-0003** — Siège de l'OACI à Montréal : référence exacte à retrouver
  (probablement Convention de Chicago, article sur le siège de
  l'organisation).

- **M10-0004** — Le statut d'institution spécialisée des Nations unies de
  l'OACI découle probablement de l'accord ONU/OACI qui a suivi la
  Convention de Chicago, pas de la Convention seule comme le dit
  actuellement la source. Non vérifié.

- **M10-0005** — Le mécanisme de notification des différences à l'OACI
  existe bien (un État qui s'écarte d'un standard OACI doit le signaler),
  mais le numéro exact de l'article de la Convention de Chicago
  (probablement l'article 38) n'est pas confirmé.

- **M10-0007** — Statut de la DGAC comme autorité nationale : texte précis
  (code des transports, décret d'organisation) à retrouver.

- **M10-0009** — L'usage des JAR (Joint Aviation Requirements) comme cadre
  de référence en France avant l'harmonisation EASA est correct sur le
  principe, mais la référence historique précise (textes, dates de
  transition) n'est pas confirmée.

- **M10-0017** — Définition du CAMO : la relecture signale que le
  rattachement réglementaire indiqué (Part-M) pourrait être devenu obsolète
  suite à un règlement modificatif postérieur (les exigences CAMO auraient
  été déplacées vers une annexe dédiée). À confirmer directement dans le
  texte en vigueur avant de corriger la fiche M10.4 en conséquence.

- **M10-0036** — Texte précis fondant le certificat de navigabilité (CofA)
  à retrouver (probablement dans les textes de certification, hors du seul
  règlement de base).

- **M10-0037** — Texte précis fondant le certificat d'immatriculation à
  retrouver (probablement lié aux Annexes OACI sur les marques de
  nationalité, et au droit national d'immatriculation).

- **M10-0038 / M10-0039** — Le caractère obligatoire des consignes de
  navigabilité (CN), et le fait qu'un bulletin de service ne devient
  obligatoire que s'il est repris par une CN, sont corrects sur le
  principe. Mais le règlement (UE) 2018/1139 cité est le règlement de
  base : la relecture signale qu'un texte plus précis (probablement dans
  les règlements de certification/maintien de navigabilité) définit
  réellement la CN et son caractère obligatoire. À retrouver avant de
  figer la source.

- **M10-0023** (et la fiche **M10.5**, même formulation : « sa gestion
  qualité ») — **Résolu le 2026-09-13.** Confirmé par `relecteur-part66` :
  le règlement d'exécution (UE) 2021/1963, applicable depuis le
  2026-12-02 2022, a bien introduit 145.A.200 « Management system », qui
  énumère explicitement une fonction de suivi de conformité (*compliance
  monitoring*) parmi les composantes du système de gestion. La question a
  été reformulée (« son système de gestion, suivi de conformité inclus »)
  pour refléter ce texte. Reste à aligner la fiche **M10.5** sur la même
  formulation si elle porte encore « gestion qualité ». Le champ `source`
  reste TODO (référence 145.A.200(a)(6) à y inscrire), hors périmètre de
  la réécriture anti-triche ci-dessous.

- **M10-0029** (et la fiche **M10.6**, même formulation) — **Résolu le
  2026-09-13.** La question a été reformulée (« L'accès à la catégorie C
  du Part-66 passe le plus souvent par... ») pour ne plus affirmer que la
  catégorie C est strictement « réservée » aux titulaires B1/B2 :
  `relecteur-part66` a confirmé l'existence d'une voie académique
  alternative (66.A.30(a)(7) : diplôme technique reconnu + trois ans
  d'expérience en environnement de maintenance civile, dont une période
  d'observation en maintenance de base). Reste à aligner la fiche
  **M10.6** sur la même nuance si elle porte encore « réservée ». Le champ
  `source` reste TODO, hors périmètre de la réécriture ci-dessous.

## Module M10 — réécriture anti-triche (2026-09-13) : plafond structurel documenté

Demande initiale : faire relire les 37 questions de M10 par le sous-agent
`eleve-adversaire` (qui tente de répondre sans aucune connaissance du
domaine, par seule élimination logique) et corriger ce qui ressort. Quatre
passages ont été faits dans la même session, avec relecture de fond
(`relecteur-part66`) entre chaque réécriture de contenu. Décision de
l'utilisateur après le 3e passage (score encore à ~90 %) : un seul passage
de restructuration supplémentaire, priorité absolue à la justesse
pédagogique sur le score adversarial, arrêt documenté après ce dernier
passage quel que soit le résultat obtenu — c'est cet arrêt qui est
documenté ici.

**Chronologie des scores mesurés par `eleve-adversaire`** (devinées sans
aucune connaissance du domaine / 37 questions) :

1. **Lot original : 37/37 (100 %).** Cause principale : l'index de bonne
   réponse suivait un cycle parfait 0→1→2→0→1→2 sur tout le fichier (une
   rotation mécanique introduite par un commit antérieur pour équilibrer
   13/12/12, en fait pire qu'un déséquilibre aléatoire), combiné à des
   distracteurs à mots absolus (« uniquement », « aucun », « tous ») et des
   échos littéraux énoncé → bonne réponse.
2. **Après réécriture n°1 (positions vraiment randomisées + mots absolus
   explicites supprimés) : 34/37 (92 %).** Les positions ne sont plus
   exploitables (distribution 13/13/11, aucun cycle ni motif local
   détecté) — point acquis et jamais régressé depuis. Mais des
   qualificatifs asymétriques plus subtils (« directement », « seulement »,
   « quel que soit », « sans conséquence »...), présents à 100 % du temps
   sur les mauvaises réponses, ont pris le relais comme indice.
3. **Après réécriture n°2 (qualificatifs asymétriques supprimés,
   distracteurs hors-domaine remplacés par des notions réglementaires
   réelles, tells grammaticaux et paires miroirs corrigés) : 33/37 (89 %).**
   `relecteur-part66` a trouvé et fait corriger 3 erreurs bloquantes
   introduites par cette réécriture (voir plus bas). Le score adversarial
   n'a presque pas bougé : remplacer un distracteur absurde par une notion
   réglementaire réelle règle l'absurdité mais réintroduit une fuite
   croisée, car cette notion réelle est presque toujours la bonne réponse
   d'une autre question du même fichier (le module ne couvre qu'une
   dizaine de notions fermées : OACI/AESA/DGAC/BEA, Part-M/145/66/147,
   CAMO/CRS/CofA/immatriculation/CN/BS, catégories A/B1.1-B1.4/B2/C).
4. **Après réécriture n°3 (distracteurs des questions « grille » reformulés
   pour porter sur le même sujet que la bonne réponse — mauvaise portée,
   mauvais seuil, mauvaise condition — plutôt que sur une autre vraie
   notion du module) : 34/37 (92 %), soit un score quasi identique à la
   fin de l'étape 2, mais pour une raison différente.** `relecteur-part66`
   a immédiatement repéré, avant même le test adversarial final, que cette
   technique avait produit un nouveau gabarit systématique : sur 7
   questions (0011, 0015, 0022, 0023, 0026, 0027, 0030), les trois options
   partagent la même tête de phrase et seuls les distracteurs portent une
   clause de retranchement (« seulement », « les seuls », « à l'exclusion
   de ») — la règle « choisir l'option qui ne retranche rien » suffit à
   toutes les résoudre. `eleve-adversaire` a confirmé ce motif de façon
   indépendante lors du 4e passage, avec le même score final.

**Ce qui est acquis et solide** (vérifié aux 4 passages, jamais régressé) :
- Positions des bonnes réponses : équilibrées 13/13/11, aucun cycle,
  aucune répétition locale de motif — la faille structurelle initiale
  (100 % devinable par la seule position) est éliminée.
- Mots absolus explicites (« uniquement », « aucun », « tous », « toujours »,
  « jamais ») : absents des 37 questions.
- 4 erreurs factuelles introduites par les réécritures ont été détectées
  par `relecteur-part66` et corrigées avant tout commit :
  - **M10-0016** : la réécriture n°2 avait inventé un critère « aviation
    légère » pour le partage de responsabilité exploitant/propriétaire.
    Corrigé sur la base de M.A.201 (le propriétaire est responsable par
    défaut ; transfert à l'exploitant si aéronef loué ou exploité par un
    transporteur aérien licencié au titre du règlement (CE) 1008/2008).
  - **M10-0026 / M10-0027** : la réécriture n°2/3 employait « systèmes
    électromécaniques » (B1.1) et « systèmes... électroniques » (B2), des
    termes absents de 66.A.20 et contredisant la fiche M10.6. Corrigé en
    « systèmes mécaniques et électriques », terminologie exacte de
    66.A.20(a)(2)-(3).
  - **M10-0033** : double négation (énoncé négatif + réponse négative).
    Reformulée en énoncé et réponse positifs, même contenu.

**Ce qui reste ouvert (non traité, hors périmètre du seul passage de
restructuration autorisé)** — liste issue de la relecture de fond du
2026-09-13, à reprendre si une nouvelle itération sur M10 est décidée :
- **M10-0011** — la liste de 4 annexes se lit comme exhaustive alors que
  le règlement 1321/2014 consolidé en compte d'autres (Part-T, Part-ML,
  Part-CAMO, Part-CAO). L'explication reste prudente (« en font partie »),
  donc pas faux, mais à clarifier.
- **M10-0015** — quasi-doublon de M10-0011 (même quatuor d'annexes).
- **M10-0017 / M10-0020** — le rattachement du CAMO au Part-M est
  peut-être obsolète depuis l'introduction d'un Part-CAMO dédié (déjà
  signalé plus haut pour M10-0017 ; possible que M10-0020 ait le même
  souci).
- **M10-0018** — contenu confirmé exact (145.A.50(a) : le CRS est signé par
  du personnel certificateur habilité), mais la source ne cite que
  « annexe I (Part-M) » sans article ; la règle directement applicable est
  145.A.50 (et M.A.801 hors organisme agréé).
- **M10-0019** — distracteur « laissé à l'appréciation du mécanicien »
  jugé trop faible/absurde par la relecture.
- **M10-0028 / M10-0030** — les explications généralisent au Part-66 dans
  son ensemble une règle qui n'est vraie que pour la sous-catégorie visée
  (pas de seuil de masse/nombre de moteurs pour A/B1.1/B1.2/B2), alors que
  la catégorie B3 (pistons non pressurisés ≤ 2 000 kg) et la catégorie C
  (*large aircraft* > 5 700 kg) sont bien définies par un seuil de masse
  ailleurs dans le Part-66. À nuancer (« pour cette sous-catégorie »).
- **M10-0029** — la marge entre la bonne réponse et le distracteur « examen
  d'entrée... sans lien avec une licence B1/B2 » est jugée trop fine
  depuis l'admission de la voie académique (66.A.30(a)(7)) ; « B1 ou B2 »
  omet B3, admis pour la catégorie C *non-large aircraft* (66.A.30(a)(6)).
- **M10-0034** — le distracteur « supports de cours mis à jour » recoupe
  une exigence réelle des organismes Part-147 (147.A.105) ; seuls les mots
  ajoutés (« normalisés », « annuellement ») le rendent faux — marge
  jugée trop fine.
- **M10-0036** — définition du CofA incomplète (conformité au type
  certifié **et** aptitude au vol en sécurité ; validité subordonnée au
  maintien de la navigabilité) : l'explication actuelle ne garde que le
  premier volet.
- **M10-0038 / M10-0039** — contenu confirmé juste, mais indices de
  structure résiduels (deux distracteurs de 0038 partagent le même moule ;
  une clause de 0039 se contredit dans sa propre phrase).
- **M10-0012 / M10-0020 / M10-0024 / M10-0031** — fuite croisée résiduelle
  entre les *explications* (pas les questions elles-mêmes) : chacune
  redonne, en passant, la réponse d'une autre question du même quatuor
  Part-M/145/66/147. Contenu juste partout ; c'est la rédaction des
  explications qui mériterait d'être assainie si une prochaine itération
  a lieu.

**Score final mesuré et décision d'arrêt** : 34/37 (92 %) de devinabilité
sans connaissance du domaine, mesuré par `eleve-adversaire` le 2026-09-13
sur le lot après les 4 corrections factuelles ci-dessus. Très au-dessus du
seuil visé (< 40 %). Conformément à la décision explicite de l'utilisateur,
**la session s'arrête ici** : pas de 5e itération sans une demande
explicite. Le diagnostic transversal (confirmé indépendamment par
`relecteur-part66` et par 4 passages successifs d'`eleve-adversaire`) est
qu'un module qui teste, par 37 questions, une taxonomie fermée d'une
dizaine de notions (OACI/AESA/DGAC/BEA, Part-M/145/66/147,
CAMO/CRS/CofA/immatriculation/CN/BS, catégories A-C) produit
mécaniquement une fuite croisée dès que le lecteur traite les 37 questions
comme un seul corpus : chaque bonne réponse ailleurs redevient un
distracteur ici, et réciproquement. Trois familles de correctifs
successives (mots absolus → qualificatifs asymétriques → distracteurs
« même sujet, mauvaise portée ») ont chacune réglé le problème qu'elles
visaient sans faire baisser durablement le score global, parce que
chacune a fait apparaître un nouveau motif systématique repérable à
l'échelle du fichier entier. Une amélioration réelle sous 40 % demanderait
vraisemblablement une refonte plus profonde que du rewording de
distracteurs — par exemple réduire le nombre de questions qui testent la
même grille de notions sous plusieurs angles, ou changer de méthode de
génération des distracteurs (valeurs numériques tirées aléatoirement
plutôt que dérivées mécaniquement de la bonne réponse) — hors périmètre de
cette session.

## M10 — relecture adversariale de la banque finale à 87 questions (2026-09-13)

Étape « reste à faire avant commit » du chantier de comblement ci-dessus,
exécutée dans la même session après une fermeture accidentelle de
terminal (le travail de comblement avait entièrement survécu, non
commité).

**Passe 1 (`eleve-adversaire`, 87 questions) :** 83/87 (95 %) de
devinabilité sans connaissance du domaine, décomposé à la demande de
l'utilisateur en deux populations :
- **37 anciennes (M10.1-M10.8) : 35/37 (95 %)**, dans la zone du plafond
  déjà documenté (taxonomie fermée du module) — pas retouché.
- **50 nouvelles (M10.9-M10.13) : 48/50 (96 %)**, pas meilleur en score
  brut, mais pour un mécanisme différent et jugé corrigible par l'agent :
  un carrousel de 5 valeurs numériques/dates réutilisées à l'identique
  entre 5 questions (7 jours / 3 mois / 1 an / 22 février 2026),
  plusieurs paires de questions se répondant mutuellement par
  construction (options dupliquées ou auto-contradictoires), et des
  échos littéraux énoncé→réponse.

**Correctifs round 1** : 14 questions retouchées (M10-0041, 0044, 0046,
0053, 0062, 0063, 0064, 0065, 0072, 0073, 0077, 0078, 0081, 0088) —
carrousel numérique cassé, auto-contradictions supprimées, échos
atténués. Aucun changement de fond réglementaire visé.

**Relecture `relecteur-part66` sur ces 14 questions — 2 BLOQUANT
trouvés et corrigés :**
- **M10-0053** : le nouveau distracteur (« exploitants d'aéronefs non
  complexes en exploitation commerciale ») était en réalité **vrai**
  (ORO.DEC.100 couvre aussi les opérations spécialisées commerciales,
  majoritairement non complexes) — la fiche M10.8 l'enseigne
  explicitement. Remplacé par un distracteur réellement faux
  (transport aérien commercial de passagers, qui exige un AOC quel que
  soit l'aéronef).
- **M10-0081** : le champ `source` citait un item de syllabus
  inexistant (« Appendix I Module 10 item 10.9 ») comme fondement
  réglementaire. Corrigé en citant le texte réel (règlement (UE)
  2018/1139, Article 2(3)(d) et Annexe I) — le contenu de la question
  était déjà exact, seule la source était fausse.

6 autres corrections mineures appliquées suite à cette relecture (option
englobante sur M10-0044, auto-élimination sur M10-0046/0072, paire
miroir sur M10-0062, explications de M10-0057/0061/0077 qui révélaient
la réponse d'une question voisine, distracteur trop absurde sur
M10-0088).

**Passe 2 (`eleve-adversaire`, 50 nouvelles questions seulement) :
46/50 (92 %) — gain net d'une seule question (M10-0072) sur les 14
retouchées.** Diagnostic de l'agent, confirmé en relisant son rapport :
3 des correctifs du round 1 avaient **régressé** en introduisant une
nouvelle asymétrie de longueur/qualification entre la bonne réponse et
les distracteurs (M10-0078 : qualificatif ajouté uniquement sur la
bonne réponse ; M10-0088 : clause auto-disqualifiante ajoutée au
distracteur ; M10-0046 : distracteur rendu implausible par surenchère).
**Ces 3 régressions ont été corrigées dans la foulée** (retour à des
options de longueur/registre comparables, sans réintroduire les défauts
d'origine — carrousel, auto-contradiction, écho).

**Diagnostic transversal (le point important pour la suite) :** une fois
le carrousel numérique, les auto-contradictions et les échos corrigés,
le canal de devinabilité dominant sur les 50 nouvelles questions n'est
**ni la taxonomie fermée (le plafond des 37 anciennes) ni les nombres
partagés** — c'est la **mise en forme des options** : la bonne réponse y
est structurellement plus longue, plus composée (deux notions liées par
« et »/apposition) ou plus qualifiée/nuancée que ses distracteurs, qui
sont souvent des paires quasi redondantes ou portent un marqueur absolu
disqualifiant (« Limitées à... », « Reste soumise », « uniquement »).
Le rapport le décrit comme **diffus** (46 questions sur 50 tombent,
réparties sur tous les sous-chapitres) plutôt que concentré sur un motif
isolé — et le corrige, question par question, referait remonter un motif
différent à chaque fois, comme observé sur les 4 passages de
l'anti-triche originale (voir section précédente). Les deux seules
questions jugées solides du lot (M10-0066, M10-0074) le sont parce
qu'elles inversent délibérément l'indice de longueur (la bonne réponse y
est la plus courte) — modèle à généraliser si une nouvelle itération est
décidée.

**Score final mesuré à l'arrêt de cette session : 46/50 (92 %) sur les
50 nouvelles, 35/37 (95 %) sur les 37 anciennes (inchangé).** Toujours
très au-dessus du seuil visé (< 40 %). **Décision non prise dans cette
session** — contrairement au chantier anti-triche original où l'arrêt
après 4 passages avait été validé explicitement par l'utilisateur, la
question n'a pas encore été posée ici : reprendre une itération de fond
(harmoniser longueur/structure des options sur l'ensemble des 50
questions, à l'image de M10-0066/0074) ou accepter ce second plateau et
committer en l'état, comme pour les 37 anciennes.

**Décision de l'utilisateur (2026-09-13)** : accepter ce second plateau
et committer en l'état — même arbitrage que pour les 37 anciennes
questions. Raison donnée : chaque itération de fond coûte cher en risque
d'erreur factuelle (2 BLOQUANT trouvés dès le premier round de
retouches ci-dessus) pour un gain marginal (+1 question nette sur 14
retouchées, avec 3 régressions au passage). **Aucune 3e itération sans
demande explicite.**

**Pour une reprise future**, si elle est décidée : le canal de
devinabilité dominant identifié est la **mise en forme des options**, pas
leur contenu factuel — donc une itération efficace porterait sur la
forme (longueur, structure syntaxique, degré de qualification des 3
options), pas sur une nouvelle recherche de faits. Modèle concret à
généraliser, tiré des 2 questions jugées solides du lot :
- **M10-0066** (Part-145, personnel d'un État tiers) : le distracteur
  faux est à la fois le plus long ET celui qui fait écho littéral à
  « État tiers » de l'énoncé — les deux indices que l'agent utilise par
  réflexe (longueur, écho) pointent activement vers la mauvaise réponse.
- **M10-0074** (capacité de conception moteur/hélice) : la bonne réponse
  est la plus **courte** des trois, à contre-courant du réflexe
  « la plus longue/la plus qualifiée est la bonne réponse » qui fait
  tomber le reste du lot.
Concrètement : viser des options de longueur comparable à chaque
question, éviter qu'un distracteur soit une négation strict miroir de la
bonne réponse (paire « plus étroit / plus large », « limité à / non
limité »), et de temps en temps inverser délibérément l'indice de
longueur pour casser l'habitude.

## Positions des bonnes réponses corrigées sur 5 modules (2026-09-13)

Le même bug que celui trouvé et corrigé sur M10 (cycle mécanique
0→1→2→0→1→2 sur l'index `bonne`, exploitable à 100 % par une règle
`(n-1) mod 3` sans aucune connaissance du domaine) a été recherché et
confirmé présent, sous forme de cycles locaux redémarrant par
sous-chapitre, dans les 5 modules à choix multiples du projet : **M5**
(44 questions), **M7A** (50), **M11A** (225), **M15** (124) et **M17A**
(116). M17A présentait en plus un déséquilibre global sévère (64/37/15
sur les trois index).

Correctif appliqué : randomisation réelle de l'ordre des options (script
Python, `random.shuffle` par question, avec vérification systématique
après coup : aucun cycle sur tout le fichier, aucune tuile locale de
période 2 ou 3 répétée 3 fois, aucune série de 5 réponses identiques
consécutives, distribution globale des trois index à ±25 % de
l'équidistribution). **Seul l'ordre des options et l'index `bonne` ont
changé** : `question`, le texte de chaque option (comme ensemble),
`explication`, `source`, `sous_chapitre` et `uid` sont strictement
identiques à l'original sur les 5 modules — vérifié par comparaison
champ à champ avec la version précédente de chaque fichier.

Distributions finales mesurées (index 0/1/2) : M5 = 11/17/16 (n=44),
M7A = 18/13/19 (n=50), M11A = 90/74/61 (n=225), M15 = 48/37/39 (n=124),
M17A = 44/29/43 (n=116).

**Point de vigilance pour toute réécriture future de contenu sur ces
modules** : une explication ne doit jamais désigner un distracteur par
sa position (« la première option », « l'option ci-dessus »...) plutôt
que par son contenu — une permutation ultérieure des options rendrait
alors l'explication fausse sans toucher au texte des options elles-mêmes.
C'est exactement le défaut trouvé et corrigé sur M10-0002 lors du travail
sur M10 (2026-09-13, voir plus haut). Une relecture `relecteur-part66`
ciblée sur ce seul point a été demandée sur les 5 modules après cette
correction de position.

## Module M15 — dette connue : gabarit de rédaction systémique (2026-09-13)

Contexte : après la correction de position ci-dessus, une relecture
`eleve-adversaire` des 124 questions de M15 a mesuré une devinabilité de
100 % par le contenu seul (indépendamment de la position, déjà saine).
Contrairement à M10, l'agent a établi que ce n'est **pas** un plafond de
domaine : trois questions (**M15-0011**, **M15-0014**, **M15-0065**) ont
résisté à toute tentative de devinette sans connaissance technique,
prouvant que l'espace de distracteurs plausibles existe bien dans ce
module — il est simplement inutilisé ailleurs.

Une tentative de correction a été lancée (remplacement des marqueurs
absolus dans les distracteurs — « aucun », « jamais », « uniquement »,
« purement », « en réalité »... —, cassage du motif « les deux
distracteurs nient la prémisse de l'énoncé », rééquilibrage des
longueurs, suppression des échos littéraux énoncé → bonne réponse) puis
**annulée sur décision de l'utilisateur** avant d'être menée à terme :
elle avait déjà commencé à modifier le texte de 99 questions sur 124
quand le score n'était descendu qu'à 97,6 % (contre 100 % initialement).
Le fichier a été restauré au contenu original (seule la position reste
corrigée, comme pour les 4 autres modules ci-dessus).

**Diagnostic du gabarit systémique**, tel qu'observé par l'agent qui a
mené la tentative de correction avant d'être arrêté : sur la quasi-
totalité des 124 questions, **la bonne réponse est rédigée pour
paraître vraie** (elle explique un mécanisme, avec une clause causale du
type « … ce qui … », « … malgré … », « … par exemple … ») **et les deux
distracteurs sont rédigés pour paraître faux** (affirmations sèches, sans
justification). Ce déséquilibre de registre reste lisible même après
avoir supprimé tous les mots absolus explicites : il transparaît par la
longueur, le registre grammatical, et le simple fait qu'une bonne
réponse justifiée se distingue structurellement d'un distracteur qui ne
l'est pas.

**Ce que ça implique pour une correction future** : substituer des mots
dans la structure actuelle (ce qui a été tenté ici, et qui avait
suffisamment bien marché sur M10 pour justifier l'essai) ne suffit pas
sur M15 — deux passages de retouche de distracteurs n'y ont fait bouger
le score que de ~2 points. Il faudrait réécrire les 124 questions selon
une méthode différente : les trois options rédigées avec la **même
densité de justification et le même registre grammatical**, sur le
modèle de M15-0011/0014/0065 qui résistent déjà. C'est un chantier plus
lourd qu'une passe de retouche de distracteurs, non entrepris à ce jour
faute de budget dans cette session — à reprendre si une nouvelle
itération sur M15 est décidée.

## Questions supprimées du lot (round de correction du 2026-09-09)

Trois questions ont été retirées définitivement de `questions.json` plutôt
que reformulées une nouvelle fois, après que deux tentatives successives de
les désambiguïser par rapport à des doublons aient chacune recréé un
chevauchement avec une autre question du lot (voir l'historique de
relecture) :

- **M10-0010** (répartition AESA/DGAC — avait fini par chevaucher M10-0008)
- **M10-0013** (garanties d'un organisme Part-147 — l'explication révélait
  les réponses de M10-0032 et M10-0034)
- **M10-0035** (qui délivre la licence Part-66 — avait fini par chevaucher
  M10-0033)

Le lot compte donc 37 questions. Ces trois emplacements pourront être
comblés par du contenu neuf (pas une reformulation des mêmes questions)
lors d'un futur élargissement de la banque M10, en même temps que les
thèmes du syllabus encore absents (MEL/CDL, ETOPS, Part-21/formulaire
EASA 1, privilèges et validité de la licence 66.A.20, ARC).

**Rééquilibrage de la position de la bonne réponse (audit technique du
2026-09-13)** : un audit du projet a trouvé que les 37 questions du lot
étaient réparties 31/6/0 sur les positions 0/1/2 — la position 2 n'était
utilisée dans aucune question, un déséquilibre plus sévère que celui déjà
documenté pour d'autres modules (M7A, M17A). Sans effet sur l'élève
(les options sont mélangées à l'affichage par session, `part66/ui.py`),
mais un vrai défaut du fichier source. Corrigé par permutation mécanique
des options (contenu inchangé, même principe que le rééquilibrage déjà
appliqué à M17A lot 3) : nouvelle répartition 13/12/12. Une exception
trouvée au passage et corrigée à la main plutôt que mécaniquement :
l'explication de **M10-0002** désignait ses distracteurs par leur
position (« ce qui écarte la première option », « troisième option »)
plutôt que par leur contenu — une formulation qui serait devenue fausse
après permutation. Reformulée pour désigner chaque distracteur par ce
qu'il affirme, avant d'appliquer le rééquilibrage. Un balayage des 37
explications n'a trouvé aucune autre occurrence de ce type.

## Module M5 — Techniques numériques / systèmes d'instruments électroniques

Construit le 2026-09-09 (9 fiches, 45 questions à la rédaction initiale,
**44 après suppression de M5-0035** — voir ci-dessous), sur le même
gabarit que M10 et avec les mêmes principes : QCM à 3 options, position
de la bonne réponse répartie dès la rédaction, mélange à l'affichage pour
éviter le biais de position, aucune source inventée à partir de la
mémoire du modèle.

**Round de correction du 2026-09-09 (relecture round 1)** : 2 questions
étaient BLOQUANT — M5-0012 (deux réponses vraies pour la porte OU, énoncé
reformulé) et M5-0025 (explication affirmant à tort qu'une fréquence
d'horloge plus élevée n'augmente pas la consommation d'énergie, alors que
c'est l'inverse qui est vrai pour un circuit numérique) — corrigées. Les
fuites d'explications entre questions miroir (une question révélait la
réponse de sa question jumelle : ADC/DAC, ET/OU, RAM/ROM, bus série/
parallèle, bus de données/bus d'adresse, UAL/registre) ont été corrigées en
rendant chaque explication autosuffisante. **M5-0035**, jugée redondante
avec M5-0031 + M5-0032 (aucune connaissance nouvelle), a été supprimée
plutôt que reformulée une nouvelle fois — le lot compte donc **44
questions**. Plusieurs distracteurs trop faibles (motif « Uniquement... »
ou hors-sujet) ont été renforcés par des confusions plus réalistes
(M5-0015, 0024, 0026, 0039, 0041-0045).

**Découpage en sous-chapitres (M5.1 à M5.9)** : comme pour M10, c'est un
découpage pédagogique maison, pas la numérotation officielle de
l'Appendice I du Part-66. Ce point a été tranché explicitement avec
l'utilisateur (choix du découpage maison, plus rapide) plutôt que
d'attendre une vérification de la liste exacte des sous-parties 5.1–5.15 et
de leur niveau de connaissance B1.1.

**Nature des sources** : contrairement à M10 (module réglementaire, sources
= textes de loi), M5 est un module technique (électronique numérique,
bases physiques/informatiques). La plupart des questions citent une source
générique du type « Notions générales d'électronique numérique — [sujet] »
plutôt qu'un texte réglementaire : ce n'est pas une source manquante, c'est
la nature du contenu (mathématiques binaires, algèbre de Boole, structure
d'un ordinateur...) qui ne relève d'aucun texte de loi à citer.

**Exception : le critère 2bis SÉCURITÉ PHYSIQUE de l'agent relecteur
prime sur cette tolérance.** Depuis le 2026-09-09
(`.claude/agents/relecteur-part66.md`), toute question portant sur une
procédure de sécurité concrète (ESD, distances/risques CEM-HIRF, risques
électriques, outillage, urgence) doit être jugée avec un niveau d'exigence
supérieur : une source encore en TODO sur ce type de contenu n'est plus
une simple tolérance documentée, c'est un motif de blocage tant que le
contenu testé n'a pas été adouci pour ne plus reposer sur un point de
précision non vérifié (voir le round de correction ci-dessous).

**Précision sur le périmètre de 2bis** (relecture de vérification du
2026-09-09) : 2bis vise la sécurité **physique** au sens strict (ESD,
CEM/HIRF, risque électrique, outillage, urgence) — la gestion de
configuration logicielle (M5-0043/M5-0044) n'en relève pas, malgré la
proximité de vocabulaire avec « traçabilité » et « contrôle ». Ces deux
questions relèvent du critère 2 JUSTESSE (recherche d'une source
réglementaire précise), pas de 2bis. Elles ont été rejugées sous ce
critère lors de la relecture complète finale du même jour : voir
l'entrée M5-0043/M5-0044 plus bas (aucune action supplémentaire requise
avant commit).

**Round de correction du 2026-09-09 (relecture ciblée 2bis, fiches M5.6
ESD et M5.8 CEM/HIRF)** : 5 points BLOQUANT ont été corrigés par
adoucissement du contenu plutôt que par ajout de précisions non
vérifiées (aucune valeur, norme ou référence technique inventée) :
- Fiche **M5.6** — le bracelet antistatique n'est plus décrit comme
  « relié à la masse » (formulation pouvant laisser croire à une liaison
  directe, dangereuse pour le porteur) mais comme du matériel ESD dédié,
  dont le détail relève de la documentation constructeur/atelier.
  L'ambiguïté « boîtier d'origine » (composant ou emballage ?) est levée
  en faveur de « conditionnement d'origine ». L'équivalence implicite entre
  emballage simplement antistatique/dissipatif et protection contre une
  décharge externe (qui demande en réalité un emballage blindant, non
  confirmé) est retirée : le texte renvoie désormais à la recommandation
  du fabricant plutôt que d'affirmer une catégorie précise.
- **M5-0027** — la bonne réponse ne mentionne plus « relié à la masse »,
  même correctif que la fiche.
- **M5-0028** — la bonne réponse et l'explication renvoient désormais à
  « l'emballage recommandé par le fabricant » plutôt que d'affirmer
  qu'un emballage « conducteur ou dissipatif » suffit en toute
  circonstance.
- **M5-0039 (HIRF)** — les distracteurs « foudre » et « champ magnétique
  terrestre » ont été retirés : ils demandaient une distinction physique
  fine (statique/continu vs rayonné) que l'explication précédente
  formulait de façon inexacte (comparaison d'intensités entre deux types
  de champs non comparables). Remplacés par des distracteurs hors du
  domaine électromagnétique (vibrations moteur, pressurisation cabine),
  qui ne demandent plus cette distinction. La définition générale du
  HIRF reste correcte sur le principe, mais reste en TODO — voir
  ci-dessous.

**Correction d'une régression (relecture finale du 2026-09-09)** : le
premier adoucissement de la fiche M5.6 et de M5-0027 avait remplacé
« relié à la masse » par une nouvelle affirmation tout aussi non fondée
(« le matériel ESD intègre les protections nécessaires pour rester sûr
pour le porteur » / « sans exposer le technicien lui-même à un risque
électrique »), non sourcée et donc tout aussi non conforme au critère
2bis qu'elle était censée corriger. Corrigé
en retirant cette clause plutôt qu'en la reformulant : la fiche et
M5-0027 renvoient maintenant explicitement les précautions vis-à-vis du
risque électrique du poste de travail à la documentation
fabricant/atelier, sans affirmer un niveau de sécurité non vérifié.
Même round : M5-0028 ne présente plus un sachet plastique standard
comme simplement « sans protection » (formulation qui le faisait
passer pour un repli neutre) mais comme un emballage qui « ne convient
pas », plus conforme à l'esprit du critère 2bis.

4 questions ont une source marquée `TODO: source à vérifier
manuellement` dans `questions.json`, portant sur des points plus
spécifiquement avioniques (donc moins universellement certains que les
bases d'électronique numérique) :

- **M5-0033** — Caractéristiques précises du bus ARINC 429 (liaison
  unidirectionnelle, un émetteur vers plusieurs récepteurs) : correcte sur
  le principe général, mais non vérifiée directement sur la norme ARINC.

- **Fiche M5.1** (texte, pas une question) — affirmation ajoutée le
  2026-09-10 : « le numéro de label d'un mot de données ARINC 429
  s'exprime traditionnellement en octal ». C'est une convention
  largement documentée dans la littérature avionique généraliste, mais
  elle n'a pas été vérifiée directement sur la norme ARINC 429 elle-même
  — même statut de prudence que M5-0033 ci-dessus, à confirmer avant de
  la considérer comme définitivement établie.

- **Fiche M5.9** (texte, pas une question) — affirmation ajoutée le
  2026-09-10 : le glass cockpit se serait généralisé dans l'aviation
  commerciale « à partir des années 1980 ». Fait d'histoire de
  l'aviation largement cité dans la littérature généraliste (première
  génération d'EFIS sur des appareils commerciaux de cette décennie),
  mais non vérifié sur une source précise. Sans effet sur la justesse
  technique du reste de la fiche ni sur aucune question du lot ; à
  confirmer ou à assouplir (« à partir des années 1980 » → « depuis
  plusieurs décennies ») si un doute apparaît.

**Round d'enrichissement majeur de M5.1, M5.4, M5.9 (2026-09-10)** :
texte doublé (paragraphes « pourquoi », exemples progressifs
supplémentaires, questions rhétoriques, rappels) et schémas agrandis
(bandeaux, tables de référence permanentes, sous-légendes visibles sans
clic, étapes/scénarios supplémentaires) sur ces 3 fiches. Une relecture
complète a trouvé 3 BLOQUANT, tous corrigés avant commit par retrait ou
atténuation (aucune donnée nouvelle non vérifiée ajoutée en
remplacement) :
- Fiche M5.9 — « des instruments de secours **purement mécaniques**
  restent présents » (généralisation fausse pour une bonne partie de la
  flotte moderne, qui utilise des instruments de secours électroniques)
  corrigé en « mécaniques ou électroniques selon l'appareil ». Absolu
  « ne repose **jamais** sur un seul écran » restreint à l'aviation
  commerciale.
- Fiche M5.9 — « un logiciel […] peut être modifié **à distance**,
  rapidement, sans démontage » : « à distance » retiré (affirmation
  opérationnelle non sourcée et inexacte pour de l'avionique certifiée,
  chargée normalement lors d'une opération de data loading sur
  l'aéronef, pas à distance).
- `schemas/M5.4.html` — le bouton « Écrire une nouvelle donnée en RAM »
  interdisait toute réécriture dans le même cycle d'alimentation
  (« la RAM contient déjà une donnée »), ce qui contredisait
  directement le texte de la fiche (valeurs « remplacées en continu »
  en RAM) et la nature même d'une mémoire vive. Corrigé en deux temps :
  la garde JS a d'abord été retirée, mais l'attribut HTML `disabled` du
  bouton avait été oublié (une vérification l'a détecté et il a été
  retiré à son tour) — la RAM peut désormais être réécrite librement
  tant qu'elle est alimentée, dès le chargement de la page ; seule une
  coupure d'alimentation la vide. Le message affiché référence la
  valeur réellement présente avant chaque écriture ou coupure (au lieu
  d'une valeur « 42 » écrite en dur, qui devenait fausse après
  plusieurs cycles), avec une formulation dédiée pour le cas où la RAM
  était déjà vide au moment de l'action (pas de citation incohérente
  du type « elle contenait « — vide — »  »).

Correctif mineur associé : `schemas/M5.1.html`, la table des exposants
(`SUP_DIGITS`) ne couvrait que les positions 0 à 4 ; le nouveau preset à
8 bits (11001101) affichait un mélange d'exposants typographiques et de
notation `2^7` en texte brut. Étendue aux positions 0 à 9.

**Dette assumée supplémentaire, non corrigée** :
- `fiches.json` — les durées `duree_min` de M5.1, M5.4 et M5.9 ont été
  révisées à la hausse (8/10/10 → 16/15/16 minutes) pour refléter le
  doublement du contenu ; ces valeurs restent des estimations internes,
  non chronométrées.
- `schemas/M5.1.html` — un `&lt;br&gt;` dans la table de référence
  hexadécimale est sans effet dans le conteneur flex (le retour à la
  ligne se fait naturellement par le wrap) : purement cosmétique, rendu
  inchangé.
- Fiche M5.4 — « une simple coupure d'alimentation ne suffit **jamais**,
  à elle seule, à effacer une configuration permanente » reste un
  absolu, mais vrai par définition du non-volatile et jugé acceptable
  au niveau B1.1.

- **M5-0039** — Définition générale du risque HIRF (champ électromagnétique
  de forte intensité) : correcte sur le principe, mais la définition
  précise et sa distinction avec d'autres phénomènes électromagnétiques
  (foudre, champ magnétique terrestre) n'ont pas été confirmées sur un
  texte de référence. Le contenu testé a été volontairement limité à la
  définition générale (voir round de correction ci-dessus) pour rester
  sous le seuil de précision non vérifiée que le critère 2bis interdit.

- **M5-0043 / M5-0044** — Cadre précis de traçabilité et de contrôle des
  modifications du logiciel embarqué (gestion de configuration logicielle) :
  correctes sur le principe général (le logiciel se trace et se modifie
  sous contrôle, comme une pièce matérielle), mais le texte de référence
  précis (guidance AESA sur la gestion logicielle) n'a pas été confirmé.
  **Rejugées sous le critère 2 JUSTESSE (pas 2bis) lors de la relecture
  complète finale du 2026-09-09** : pas de problème de justesse identifié,
  les deux distracteurs de chaque question sont faux sans ambiguïté ; le
  TODO reste donc un TODO documenté (même statut que M5-0033), sans action
  supplémentaire requise avant commit. Une source précise reste bienvenue
  si elle est trouvée plus tard, mais n'est plus un prérequis au commit.

**Dette de qualité assumée (non bloquante, décidée avec l'utilisateur le
2026-09-09)** — points identifiés lors des relectures successives, non
corrigés avant ce commit, à traiter dans un round ultérieur :

- **M5-0015 → M5-0023** — fuite marginale résiduelle : l'option/explication
  de M5-0015 mentionnant un « signal d'horloge de synchronisation » donne
  un indice sur le rôle de l'horloge testé par M5-0023. Impact jugé faible
  (sous-chapitres différents, M5.3 et M5.5).

- **5 paires miroir non explicitement documentées comme choix de gabarit**
  (M5-0006/M5-0007 ADC-DAC, M5-0011/M5-0012 ET-OU, M5-0016/M5-0017 RAM-ROM,
  M5-0019/M5-0020 bus données-adresse, M5-0031/M5-0032 série-parallèle —
  soit 10 questions sur 44 qui testent chacune un seul fait sous deux
  angles opposés). Ce choix de gabarit est en tension avec la suppression
  de M5-0035 pour absence de connaissance nouvelle par rapport à
  M5-0031+M5-0032 : si ce critère était appliqué strictement, une partie de
  ces paires serait aussi redondante. Assumé pour l'instant, à trancher
  explicitement (garder le gabarit en paires, ou le remettre en cause) lors
  d'un futur élargissement de la banque M5.

- **M5-0040** — le distracteur restant (« Un allongement des câbles, sans
  autre protection ») est faible/facilement éliminable, ce qui réduit le
  pouvoir discriminant de la question à un seul distracteur réellement
  fort. Assumé : toute tentative de renforcement devra éviter une
  technique CEM réellement valide (éloignement, torsadage, séparation des
  faisceaux), qui recréerait le BLOQUANT déjà rencontré deux fois sur
  cette question — voir le round de correction ci-dessus.

- **M5-0039** — pouvoir discriminant faible : les distracteurs
  (vibrations moteur, pression cabine) sont volontairement hors du domaine
  électromagnétique, pour ne pas reposer sur une distinction physique fine
  non vérifiée (foudre vs HIRF vs champ magnétique terrestre). Compromis
  assumé du round de correction 2bis, à revoir seulement si la source HIRF
  finit par être confirmée.

**Round d'enrichissement « débutant complet » des 9 fiches (2026-09-09)** :
chaque fiche a reçu un exemple concret, une méthode ou un moyen
mnémotechnique, et/ou une clarification de vocabulaire, sans rien retirer
de l'existant (M5.1 : méthodes de conversion décimal↔binaire↔hexadécimal
chiffrées ; M5.2 : exemple capteur + mnémotechnique ADC/DAC ; M5.3 : tables
de vérité ET/OU/XOR/NON + exemple voyant train/hauteur sol ; M5.4 :
analogies tableau blanc/livre/colis postal pour RAM/ROM/bus ; M5.5 :
exemple fetch-decode-execute détaillé ; M5.6 : reformulation qualitative
de l'imprévisibilité d'une décharge ESD, sans aucun seuil chiffré ; M5.7 :
image route/autoroute pour série/parallèle ; M5.8 : image lampe torche/
morse pour la fibre optique ; M5.9 : contraste instruments à aiguille vs
écrans, analogie éditions de livre pour les versions logicielles).

Deux relectures ciblées ont suivi cet enrichissement et ont donné lieu aux
corrections suivantes, toutes appliquées :
- M5.1 — précision ajoutée sur le complément par des zéros quand le
  dernier groupe de bits est incomplet.
- M5.2 — mnémotechnique ADC/DAC corrigé (la mise en gras portait sur la
  mauvaise lettre).
- M5.3 — « altitude » remplacé par « hauteur au-dessus du sol » (terme
  exact pour ce type d'exemple), puis la valeur (« 500 pieds ») explicitement
  qualifiée de valeur d'illustration pour ne pas être mémorisée comme un
  seuil réel par un débutant.
- M5.4 — analogie RAM reformulée (un tableau blanc effacé à chaque coupure
  d'alimentation, plutôt qu'une lumière qu'on éteint).
- M5.6 — « peut suffire à endommager » harmonisé entre le corps du texte
  et le paragraphe « À retenir » (qui disait encore « détruit »).
- M5.9 — périmètre de l'EFIS corrigé : les paramètres moteurs et alertes
  (ECAM/EICAS) en sont explicitement exclus, pour rester cohérent avec
  l'explication de M5-0042 (une première version de la fiche les incluait
  implicitement dans l'EFIS, contredisant cette question).
- M5-0036 — les deux distracteurs se lisaient tous les deux comme des
  inconvénients face à un énoncé demandant un « avantage », rendant la
  question résoluble par la seule lecture. Un distracteur remplacé par une
  fausse qualité plausible (immunité totale aux dommages mécaniques).

Toutes ces corrections ont été vérifiées par relecture avant ce commit ;
aucune erreur factuelle n'a été trouvée dans le contenu enrichi.

**Round « pourquoi / exemples progressifs / transitions » + 6 nouveaux
schémas interactifs (2026-09-09)**, suite au retour utilisateur après test
des 3 premiers schémas (M5.1, M5.3, M5.7) en navigateur : approche
conservée, étendue aux 6 fiches restantes.

- **Texte des 9 fiches** : chacune a reçu un paragraphe « pourquoi » en
  ouverture (à quoi sert la notion avant de la définir), un ou deux
  exemples progressifs supplémentaires, et une phrase de transition vers
  la fiche suivante. Chaîne de transitions complète M5.1→M5.2→...→M5.9,
  à une exception près : le maillon M5.3→M5.4 n'a pas reçu de phrase de
  liaison explicite (mineur, à compléter dans un round ultérieur).

- **6 nouveaux schémas interactifs**, même technique que les 3 premiers
  (fichier `.html` autonome dans `part66/data/M5/schemas/`, rendu via
  `st.html(..., unsafe_allow_javascript=True)`, aucune dépendance
  externe, aucune communication Python) : M5.2 (simulateur ADC avec
  effet de quantification), M5.4 (parcours animé d'une donnée capteur →
  bus → RAM → CPU), M5.5 (cycle fetch-decode-execute animé), M5.6 et
  M5.8 (schémas **volontairement qualitatifs**, sans aucun chiffre ni
  norme, conformément au critère 2bis), M5.9 (bascule visuelle
  instruments classiques / glass cockpit). Les 9 fiches ont désormais
  chacune leur schéma.

- **5 explications de questions renforcées** (M5-0001, M5-0013, M5-0021,
  M5-0030, M5-0038) : elles justifiaient déjà la bonne réponse mais
  dismissaient les distracteurs trop sèchement ; elles expliquent
  maintenant plus clairement pourquoi chaque distracteur est faux.

- **5 points BLOQUANT trouvés et corrigés par une première relecture
  complète de ce round**, tous par atténuation du contenu (aucune
  donnée nouvelle non vérifiée ajoutée en remplacement) :
  - Fiche M5.2 — confusion technique corrigée (l'automanette ne pilote
    pas de gouverne ; le nouvel exemple attribue ce rôle à un
    calculateur de commandes de vol).
  - Fiche M5.8 — retrait d'une affirmation de « exigence de
    certification » non sourcée, remplacée par une formulation sans
    prétention réglementaire.
  - Fiche M5.9 — retrait d'un absolu non sourcé (« de la même manière
    stricte ») sur la procédure de modification logicielle.
  - `schemas/M5.6.html` — régression 2bis : le panneau nommait le
    bracelet seul comme suffisant (perdant le qualificatif « dédié » et
    les autres précautions de la fiche), et l'issue de la « panne » était
    présentée comme certaine plutôt que possible. Panneau reformulé
    pour lister les précautions de la fiche, issue mise au conditionnel.
  - `schemas/M5.8.html` — régression 2bis : l'efficacité du blindage
    était présentée comme totale (« arrive intact ») et un détail
    d'installation non vérifié avait été ajouté (« gaine métallique
    reliée à la masse »). Reformulé en « limite la sensibilité, ne
    l'annule pas », détail d'installation retiré.

  Une relecture de vérification a confirmé les 5 corrections
  effectives, sans nouvelle régression.

- **Points « À REVOIR » traités dans la foulée** (non bloquants mais
  corrigés par prudence) : cas de tension ambiguë du simulateur ADC
  (2,5 V → 2,4 V, plus d'égalité exacte entre deux marches, robustesse
  ajoutée au cas où), bug d'affichage de fin de cycle sur
  `schemas/M5.5.html` (dernière case restait jaune au lieu de passer
  verte), cadran « Attitude » de `schemas/M5.9.html` remplacé par
  « Variomètre » (plus fidèle à un instrument réellement à aiguille),
  disclaimer « valeurs illustratives » rendu visible sur les deux vues
  de ce même schéma, paragraphe « pourquoi » ajouté à la fiche M5.6
  (seule fiche qui n'en avait pas), transitions manquantes ajoutées
  entre fiches (dont M5.3→M5.4, complétant la chaîne M5.1→...→M5.9),
  formulations de M5-0030/M5-0038 allégées d'une clause qui révélait la
  technique de rédaction du QCM plutôt que d'enseigner.

**Dette de qualité assumée, round texte enrichi + 6 schémas (décidée
avec l'utilisateur le 2026-09-10)** — points mineurs identifiés par la
relecture finale, non corrigés, à traiter dans un round ultérieur :

- **Fiche M5.7** — la phrase « c'est ce compromis, favorable au
  câblage, qui explique le choix du série en avionique » présente le
  poids du câblage comme la seule raison du choix du bus série, alors
  que l'intégrité du signal en haute fréquence en est une autre. Le
  calcul chiffré associé (32 bits : 32 fils/1 instant en parallèle vs
  1 fil/32 instants en série) reste exact ; seule la formulation de la
  causalité est à nuancer.

- **Fiche M5.8** — l'exemple d'ouverture (grésillement d'un téléphone
  portable près d'une enceinte) est un phénomène réel mais surtout
  associé aux anciens réseaux 2G/GSM, de moins en moins observé
  aujourd'hui : risque de ne plus évoquer grand-chose à un candidat
  jeune. À remplacer par un exemple plus intemporel si l'occasion se
  présente.

- **`schemas/M5.4.html`** — le diagramme est câblé Capteur → ADC → Bus
  → RAM → CPU avec des flèches uniquement de gauche à droite, alors que
  l'étape 7 (relecture par le CPU) décrit un flux RAM → CPU qui remonte
  visuellement à contre-sens des flèches dessinées. Les 7 étapes
  restent correctes sur le fond ; seul le rendu visuel de la dernière
  étape peut prêter à confusion.

- **`schemas/M5.6.html`** — le badge du panneau « sans précaution »
  affiche un résultat déterministe (« Composant : en panne ») alors
  que la légende qui l'accompagne dit bien « peut tomber en panne ».
  La légende rattrape le sens correctement (aucune procédure ni aucun
  équipement n'est mal décrit), mais un badge du type « en panne (dans
  ce scénario) » lèverait ce flottement résiduel.

**Second schéma ajouté sur 3 fiches (2026-09-10)**, suite à une revue de
priorisation demandée à l'utilisateur (une notion importante par fiche
restait mal couverte par le seul premier schéma) :

- `schemas/M5.1.html` — devient à onglets (Binaire→Décimal déjà
  existant et inchangé, + Décimal→Binaire par divisions successives,
  + Binaire→Hexadécimal par regroupement en quartets, avec gestion du
  complément par des zéros quand le dernier groupe est incomplet).
- `schemas/M5.4.html` — ajout d'une deuxième expérience (bouton
  « couper l'alimentation ») qui vide visuellement une case RAM tout en
  laissant une case ROM intacte, pour rendre concrète la distinction
  volatile/non volatile déjà testée par M5-0016/M5-0017.
- `schemas/M5.9.html` — ajout d'un deuxième schéma sur la gestion des
  versions logicielles : deux scénarios comparables (mise à jour
  cosmétique vs mise à jour qui change un calcul) remplissent tous deux
  la même fiche de traçabilité, pour illustrer sans absolu le paragraphe
  déjà présent dans le texte de la fiche.

Une relecture de ce round a trouvé 2 BLOQUANT, tous deux corrigés avant
commit : `schemas/M5.9.html` réintroduisait l'absolu « la même procédure
d'approbation est suivie » que le round précédent avait justement retiré
de la fiche (corrigé en « passe par une procédure approuvée », sans
comparatif) ; `schemas/M5.4.html` laissait le bouton « Remettre sous
tension » afficher une coupure d'alimentation qui n'avait pas eu lieu si
on le cliquait sans avoir d'abord coupé (garde d'état symétrique
ajoutée, comme celle qui existait déjà sur « Couper l'alimentation »).
Corrections mineures associées : persistance visuelle de l'explication
du complément par des zéros dans le mode Binaire→Hexadécimal de
`schemas/M5.1.html` (elle disparaissait auparavant dès le premier clic),
accord grammatical corrigé, et donnée de la case RAM de `schemas/M5.4.html`
reliée au thème du premier schéma (température plutôt qu'un nombre
isolé).

Une vérification finale a confirmé les 2 BLOQUANT effectivement corrigés
(pas seulement documentés) et relevé 4 points mineurs supplémentaires,
non corrigés, versés à la dette assumée :

- ~~`schemas/M5.4.html` — après un second cycle Couper→Remettre→Couper,
  la légende affirmait « la RAM a perdu son contenu » alors que la case
  était déjà vide avant cette coupure.~~ **Corrigé le 2026-09-10** lors
  du round d'enrichissement majeur : le handler distingue désormais si
  la RAM était déjà vide avant l'action (message dédié), voir plus haut.
- `schemas/M5.1.html` — la phrase « Le nombre d'origine (1101101, 7
  bits) n'est pas un multiple de 4 » attribue au nombre une propriété
  qui concerne en réalité son nombre de bits (glissement valeur/longueur).
  Sens et calcul restent corrects, seule la formulation est ambiguë.
- `schemas/M5.9.html` — les deux scénarios de la fiche de traçabilité
  affichent une carte visuellement identique (mêmes numéros de version
  1.0→1.1 dans les deux cas), ce qui peut se lire comme « la procédure
  est visuellement la même » même si le texte ne l'affirme plus.
- `A_VERIFIER.md` (ce fichier, plus haut) — la formulation « complément
  par des zéros quand le dernier groupe est incomplet » omet « à
  gauche » ; le schéma et la fiche M5.1, eux, sont explicites sur ce
  point.

**Améliorations futures identifiées mais non traitées (priorité jugée
plus faible, décidé avec l'utilisateur le 2026-09-10)** — un schéma
existe déjà pour l'exemple simple de chacune de ces fiches, mais pas
pour l'exemple progressif le plus avancé du texte :

- **M5.3 (portes logiques)** — le schéma ne gère qu'une porte à la fois ;
  l'exemple du texte qui chaîne deux portes (ET puis OU) n'a pas
  d'équivalent interactif.
- **M5.5 (microprocesseurs)** — le schéma anime un seul cycle
  fetch-decode-execute (une addition) ; l'exemple à 3 cycles enchaînés
  du texte (lire un capteur, comparer à un seuil, décider) n'est pas
  représenté.
- **M5.7 (bus série/parallèle)** — le schéma anime la différence de
  timing série/parallèle, mais pas la topologie particulière d'ARINC 429
  (un seul émetteur vers plusieurs récepteurs), testée par M5-0033.
- **M5.8 (fibre optique/CEM)** — le schéma qualitatif couvre le blindage
  d'un câble électrique, mais pas l'immunité de la fibre optique
  elle-même (absence de courant électrique), qui reste seulement décrite
  par l'analogie texte (lampe torche/morse).

**Trois autres points mineurs, non corrigés (dette assumée) :**

- `schemas/M5.1.html` — dans le mode Binaire→Hexadécimal, le chiffre
  hexadécimal résultat de chaque groupe est affiché avec la classe
  `.m51-pow` (petit, gris), initialement prévue pour les exposants de 2 :
  purement cosmétique, mais ça affaiblit visuellement un résultat qui
  mériterait d'être mis en avant plutôt qu'en retrait.
- **Standard inégal sur « relié à la masse »** — le round de correction
  2bis avait retiré de `schemas/M5.8.html` la mention « gaine métallique
  reliée à la masse » comme détail d'installation non vérifié, mais la
  fiche M5.8 et l'option correcte de M5-0040 conservent « boîtiers
  métalliques reliés (électriquement) à la masse » pour le blindage. Le
  principe relève de notions d'électronique générales, mais le critère
  appliqué au schéma n'est pas appliqué de la même façon à la fiche et à
  la question qu'il illustre : à trancher une fois pour les trois
  emplacements.
- **M5-0004** — l'énoncé « Un chiffre hexadécimal (un « quartet »)
  représente exactement : » assimile le chiffre hexadécimal au quartet,
  alors qu'un quartet est le groupe de 4 bits *représenté par* ce
  chiffre (la fiche M5.1 est correcte sur ce point). Sans effet sur la
  bonne réponse ; à reformuler dans un round de finition.

**Renvoi fabriqué trouvé et corrigé (audit technique du 2026-09-13)** :
la fiche M5.9 affirmait « la réponse tient à un principe déjà vu
ailleurs dans ce module (M5.4) : la redondance », alors que le mot
« redondance » n'apparaît nulle part dans la fiche M5.4 (vérifié par
recherche exacte dans le texte) — le seul autre usage du mot dans le
module, en M5.1, désigne un sens différent (le fait d'apprendre trois
systèmes de numération n'est « pas une redondance »), pas le principe
de tolérance de panne développé en M5.9. Ce renvoi n'a été détecté par
aucun round de relecture antérieur (M5 a été construit avant que la
vérification systématique des renvois croisés ne devienne une étape
obligatoire de relecture, contrairement aux modules construits à partir
de M17A). Corrigé en retirant le renvoi inventé plutôt qu'en lui
trouvant une fausse cible de remplacement : la fiche M5.9 introduit
maintenant la redondance comme un principe expliqué sur place, sans
prétendre qu'il a été vu plus tôt dans le module.

## Point de configuration à confirmer (hors banque de questions)

- **Nombre de questions et durée de l'examen officiel du module M10** pour
  la licence B1.1 : la valeur utilisée par défaut dans `part66/logic.py`
  (32 questions / 40 minutes) est une valeur couramment citée mais non
  vérifiée sur une source officielle à jour (Appendix VIII du Part-66). À
  confirmer avant de s'appuyer sur l'examen blanc pour évaluer une réelle
  préparation à l'épreuve.

- **Nombre de questions et durée de l'examen officiel du module M5** : la
  valeur utilisée par défaut dans `part66/logic.py` (20 questions /
  25 minutes) est une estimation provisoire, non vérifiée sur une source
  officielle (Appendix VIII du Part-66). Même statut que la valeur M10
  ci-dessus : à confirmer avant usage en conditions d'examen réel.

- **Nombre de questions et durée de l'examen officiel du module M7A** : la
  valeur utilisée par défaut dans `part66/logic.py` (25 questions /
  30 minutes) est une estimation provisoire, non vérifiée sur une source
  officielle (Appendix VIII du Part-66). Même statut que M10 et M5
  ci-dessus : à confirmer avant usage en conditions d'examen réel.

## Intitulés des modules non encore traités

Les intitulés de M7A, M11A, M15 et M17A utilisés comme simples libellés
d'affichage (module « à venir ») dans `part66/logic.py` viennent de la
connaissance générale du référentiel Part-66 et doivent être confirmés
contre le syllabus officiel avant que ces modules ne soient réellement
construits (fiches + questions) :

- M7A : « Pratiques de maintenance »
- M11A : « Aérodynamique, structures et systèmes — avion à turbine »
- M15 : « Turbomachines à gaz »
- M17A : « Hélices »

## M7A — construction en cours

Le module M7A (« Pratiques de maintenance ») est en cours de construction,
fiche par fiche. Le syllabus officiel EASA du module 7A compte, dans les
versions généralement citées, une quinzaine de sous-chapitres distincts ;
pour rester sur un format proche de celui de M5 (9-10 fiches), la
répartition retenue ici **regroupe** plusieurs sous-chapitres officiels par
fiche plutôt que de créer une fiche par sous-chapitre. Cette répartition en
10 fiches (M7A.1 à M7A.10) est une construction éditoriale de ce projet,
pas une nomenclature officielle recopiée du syllabus EASA : à confirmer
contre le syllabus officiel avant de considérer la couverture du module
comme complète.

Trois sous-chapitres officiels du module 7A ne sont couverts par aucune des
10 fiches actuellement prévues et doivent être ajoutés dans une extension
ultérieure du module (nouvelles fiches, ou nouveau module dédié) :
- les **matériaux composites** (structure, réparation de base, précautions
  de mise en œuvre) ;
- le **soudage et le brasage** (welding, brazing, soldering) ;
- le **contrôle non destructif (CND)** (non-destructive inspection/testing).

### M7A.1-M7A.5 — round 1 de relecture (dette mineure assumée)

Le lot M7A.1-M7A.5 (5 fiches + 25 questions) a été relu par le sous-agent
`relecteur-part66` avant commit. Les 4 points bloquants relevés (rallonge
vs adaptateur déporté sur M7A.2/M7A-0009, cartouche/nom du dessinateur sur
M7A-0013, distracteur ambigu sur la cote nominale de M7A-0018, résidu de
poudre décrit à tort comme conducteur sur le schéma M7A.1) ont été corrigés
avant commit, de même que les 3 questions à double distracteur non
plausible signalées en priorité (M7A-0007, M7A-0015, M7A-0019).

Un round 2 de relecture, ciblé sur la vérification de ces correctifs, a
trouvé un 5ᵉ point bloquant (le schéma `M7A.3.html` grisait le tronçon de
fil situé en amont de l'interrupteur exactement comme le tronçon en aval,
alors que le premier reste sous tension même circuit ouvert — corrigé par
un code couleur à trois états : sous tension/pas de courant, parcouru par
un courant, ni l'un ni l'autre) et plusieurs raffinements mineurs, tous
corrigés avant commit : le schéma `M7A.2.html` illustre maintenant les deux
sens possibles de l'effet d'un adaptateur déporté (couple réel supérieur
*ou* inférieur, pas seulement supérieur) ; M7A-0009 est reformulée en
question ouverte pour que ses trois options soient grammaticalement
homogènes ; l'explication de M7A-0018 ne décrit plus la méthode de montage
par dilatation thermique (elle révélait la réponse de M7A-0020, même
sous-chapitre) ; le distracteur de M7A-0020 ne mélange plus « cote
nominale » et « cote réelle » ; les distracteurs de M7A-0007 et M7A-0015
ont été encore affinés pour ne plus être éliminables par la seule lecture
de l'énoncé.

Restent, en dette mineure assumée (même statut que les points similaires
documentés pour M5) :
- des distracteurs trop peu plausibles sur une dizaine d'autres questions
  (M7A-0004, M7A-0005, M7A-0010, M7A-0011, M7A-0016, M7A-0021, M7A-0023,
  M7A-0024, M7A-0025) — à muscler lors d'un futur round de finition ;
- un léger doublon thématique entre M7A-0001 et M7A-0005 (l'eau comme
  mauvais agent extincteur, sur deux types de feu différents) ;
- la position de la bonne réponse suit un cycle 0/1/2 régulier sur une
  bonne partie du fichier source (neutralisé à l'affichage par le mélange
  par session dans `part66/ui.py`, mais à casser dans le fichier source
  lors d'un prochain passage) ;
- couverture non testée par une question : l'ajustement incertain
  (*transition fit*, fiche M7A.4), les consignes d'urgence (fiche M7A.1)
  et le test de traction/*pull test* (fiche M7A.5) ;
- nuance à apporter à l'explication de M7A-0016 : l'existence même d'une
  tolérance tient à la variabilité de fabrication, mais le choix de sa
  largeur peut aussi tenir compte du coût — l'explication actuelle rejette
  le lien au coût de façon trop catégorique ;
- FOD (M7A-0006) ne retient que l'acception *Foreign Object Damage* ; le
  sigle recouvre aussi couramment *Foreign Object Debris* selon les
  sources.

### M7A.6-M7A.10 — round de relecture du module complet (dette mineure assumée)

À la clôture du module (10 fiches, 50 questions), une relecture complète a
porté un regard neuf sur M7A.6 à M7A.10 et un contrôle de cohérence sur
l'ensemble. Deux points bloquants ont été trouvés et corrigés avant
commit : la fiche M7A.6 décrivait la mécanique de pose du rivet plein à
l'envers (la bouterolle est l'outil de la riveteuse appliqué côté tête
d'usine, pas l'outil qui « soutient » cette tête — c'est le tas à river,
côté tige, qui forme la tête d'atelier), corrigé dans la fiche, dans
M7A-0026 et dans le schéma `M7A.6.html` ; et la fiche M7A.9 donnait le
sens inverse de celui du schéma `M7A.9.html` sur l'effet du froid sur la
tension d'un câble de commande (le schéma était juste : un refroidissement
détend le câble, la structure se contractant davantage que lui), corrigé
dans la fiche.

Restent, en dette mineure assumée :
- une dizaine de distracteurs trop peu plausibles sur le lot M7A.6-M7A.10
  (M7A-0026, M7A-0027, M7A-0033, M7A-0034, M7A-0039, M7A-0041, M7A-0046,
  M7A-0048, M7A-0050) ;
- un gabarit répété sur 4 questions (M7A-0019, M7A-0029, M7A-0032,
  M7A-0047) où la bonne réponse est systématiquement celle qui cite un
  document de référence (dessin/AMM/SRM), reconnaissable sans connaître le
  sujet ;
- plusieurs fuites d'explication entre questions du même sous-chapitre ou
  de sous-chapitres différents pouvant tomber dans le même examen blanc :
  M7A-0045 → M7A-0038 (brinelling), M7A-0031 → M7A-0021 (fatigue par
  flexion répétée), M7A-0030 → M7A-0027 (durcissement structural) ;
- une paire miroir M7A-0026/M7A-0028 (accès un côté vs deux côtés d'un
  rivet), même statut que les paires miroir déjà assumées pour M5 ;
- le cycle de position de la bonne réponse (dette déjà notée pour
  M7A.1-M7A.5) concerne également M7A.6-M7A.10 ;
- M7A-0050 (pesée simultanée aux points d'appui) reste peu discriminante :
  la vraie raison (les charges aux différents points d'appui doivent être
  saisies au même instant et dans la même assiette pour qu'un centre de
  gravité calculé à partir d'elles ait un sens) n'est qu'esquissée par la
  bonne réponse actuelle ;
- `schemas/M7A.7.html`, cas « traversée de cloison pare-feu » : la
  justification a été complétée (mouvement du moteur + exigence de tenue
  au feu du flexible), mais reste résumée par rapport à la réalité du
  sujet.

### Réforme du syllabus « Module 7 » (12 juin 2024) — dette documentée, non traitée

Recherche menée le 2026-09-13 (chantier « sujets de rédaction M7A + niveau
syllabus »), source : EASA *Easy Access Rules for Continuing Airworthiness
(Regulation (EU) No 1321/2014)*, révision **septembre 2025** (la plus
récente disponible), téléchargée directement depuis
https://www.easa.europa.eu/en/downloads/95788/en — 1265 pages, extraction
`pdftotext -table` sur les pages 573-575 (Module 7) et 632-634 (nombre de
questions par module).

**Constat : nos 10 fiches M7A suivent l'ancienne structure « Module 7A /
Module 7B »**, remplacée par le règlement **(UE) 2023/989** (applicable
depuis le **12 juin 2024**), qui a fusionné 7A et 7B en un seul « Module 7 »
et renuméroté ses items internes (7.1 à 7.21, avec 7.4 et 7.15
« Reserved »). Conséquences concrètes pour notre contenu :

- Les 3 lacunes déjà notées ci-dessus (matériaux composites, soudage/
  brasage, contrôle non destructif) doivent être **réévaluées à la
  lumière de la réforme**, pas simplement comblées telles quelles :
  - le **soudage, brasage et bonding** (ancien 7.15 dans la structure
    2020) est désormais **« (Reserved) »** dans le Module 7 actuel — ce
    n'est donc probablement plus une lacune à combler, sous réserve de
    confirmer que « Reserved » signifie bien « retiré du syllabus » et
    non « renvoyé à un autre module » ;
  - le **contrôle non destructif** est maintenant un alinéa du groupe
    7.18(c) *Disassembly, Inspection, Repair and Assembly Techniques*,
    donc potentiellement déjà dans le périmètre visé de la fiche M7A.10
    (« Démontage, inspection, réparation, remontage »), à vérifier
    précisément ;
  - les **matériaux composites** restent un vrai point non couvert
    (item 7.14.2 *Composite and non-metallic*, niveau B1 = 2).
- **Deux items ajoutés par la réforme n'ont aucun équivalent dans nos 10
  fiches** : **7.14.3 Fabrication additive** (*additive manufacturing*,
  niveau B1 = 1) et **7.21 Documentation & communication** (niveau B1 =
  2). Ce sont des ajouts récents du syllabus, pas des oublis d'une
  construction antérieure — à traiter comme une extension du module, pas
  une correction.

**Non traité dans cette session** (décision explicite de l'utilisateur :
prioriser la correction du format d'examen ci-dessous et les sujets de
rédaction ; cette réforme est documentée pour une reprise ultérieure, pas
corrigée maintenant). Avant toute extension du module sur ces deux points,
revérifier aussi que les 10 fiches existantes correspondent bien aux bons
items numérotés du Module 7 actuel (mapping fait par déduction thématique
lors de cette recherche, à valider fiche par fiche — voir aussi le mapping
niveau 1/2/3 plus bas dans ce fichier une fois renseigné).

### Niveaux de connaissance (1/2/3) — sourcés et renseignés le 2026-09-13

Champ `"niveau"` (1, 2 ou 3) ajouté à chaque fiche de
`part66/data/M7A/fiches.json`, affiché dans l'onglet Cours
(`part66/ui.py`, `_page_cours`) avec une légende expliquant les 3
niveaux. Validé par l'utilisateur avant écriture : *« La source EASA
Easy Access Rules est la référence de la profession, ça suffit »*.

**Source** : même document que ci-dessus (EASA *Easy Access Rules for
Continuing Airworthiness*, révision septembre 2025), Appendix I, Module
7 « Maintenance Practices », colonne catégorie B1 (identique à B3 dans
ce document — une seule colonne numérique sert aux deux). Définitions
génériques des niveaux extraites verbatim de la section 1 du même
Appendix I.

**Mapping retenu** (déduction thématique de ce projet, pas une
nomenclature officielle — voir la réforme de juin 2024 ci-dessus, qui
peut avoir déplacé certains items) :

| Fiche M7A | Item(s) Module 7 | Niveau B1 |
|---|---|---|
| M7A.1 Sécurité en atelier | 7.1 | 3 |
| M7A.2 Pratiques d'atelier et outillage | 7.2, 7.3 | 3 |
| M7A.3 Dessins techniques, schémas et normes | 7.5 | 2 |
| M7A.4 Ajustements et tolérances | 7.6 | 2 |
| M7A.5 Câbles et connecteurs électriques | 7.7 (EWIS) | 3 |
| M7A.6 Rivetage | 7.8 | 2 |
| M7A.7 Tuyauteries et flexibles | 7.9 | 2 |
| M7A.8 Ressorts, roulements et transmissions | 7.10, 7.11, 7.12 | 2 |
| M7A.9 Câbles de commande et manutention | 7.13, 7.17 | 2 |
| M7A.10 Démontage/inspection/réparation/pesée | 7.16, 7.18 | 2, **sauf 7.18(a) type de défauts/inspection visuelle = 3** |

M7A.10 est affichée avec ce cas mixte explicite (champ `niveau_note`
dans `fiches.json`, affiché sous la légende principale dans l'appli) :
un simple badge « Niveau 2 » aurait été trompeur pour cette fiche.

**Réserves conservées** (l'utilisateur a validé la source comme
suffisante ; ces points restent notés pour référence future, pas pour
bloquer l'usage actuel) :
- Cette publication EASA est la consolidation de référence de la
  profession, mais reste juridiquement une compilation non-officielle
  (le texte contraignant est EUR-Lex, non récupéré en seconde source
  faute d'un outil de récupération adapté à sa taille).
- Extraction automatisée (`pdftotext -table`), pas de vérification
  visuelle pixel par pixel du tableau original (aucun outil de rendu de
  page PDF disponible dans cet environnement).
- La correspondance fiche ↔ item officiel 7.x est une inférence
  thématique de ce projet, pas une donnée du document lui-même.

**Autres modules** : le mécanisme d'affichage (`_page_cours`, légende
comprise) fonctionne pour n'importe quel module dont les fiches
porteraient un champ `"niveau"`, mais seul M7A en a été doté pour
l'instant. Les autres modules (M5, M10, M11A, M15, M17A) n'affichent
aucun niveau tant que la même recherche sourcée n'aura pas été menée et
validée pour chacun.

### Format d'examen (nb. de questions / durée) — corrigé le 2026-09-13

`part66/logic.py` (dict `MODULES`) donnait, pour les 6 modules construits,
des valeurs non sourcées (souvent des estimations ou des valeurs recopiées
d'un module à l'autre). Corrigées sur la même source que ci-dessus
(section « Number of questions per module », colonne catégorie B1 ou
B1.1 selon le module) :

| Module | Ancienne valeur (fausse) | Valeur officielle (B1/B1.1) |
|---|---|---|
| M10 | 32 questions / 40 min | **44 / 55** |
| M5  | 20 questions / 25 min | **40 / 50** |
| M7A | 25 questions / 30 min | **80 / 100** (+ 2 questions rédactionnelles de 20 min chacune, non simulées par l'examen blanc QCM) |
| M11A | 140 questions / 175 min | **140 / 175** — déjà correcte, désormais confirmée par la source officielle |
| M15 | 25 questions / 30 min | **92 / 115** |
| M17A | 25 questions / 30 min | **32 / 40** |

**Point additionnel trouvé en vérifiant ces chiffres, non corrigé ici** :
la taille réelle de la banque de questions ne couvre pas encore le tirage
officiel sur 2 modules — M7A (50 questions disponibles pour un tirage de
80) et M10 (37 disponibles pour un tirage de 44). `construire_examen_blanc`
(logic.py) gère déjà ce cas sans planter (`nb = min(nb_questions_examen,
len(questions))`), donc l'examen blanc reste utilisable, mais il tire
alors moins de questions que l'épreuve réelle sur ces deux modules — à
traiter en écrivant des questions supplémentaires, chantier séparé de
celui d'aujourd'hui.

## M17A — construction en cours (Lot 1 : M17A.1-M17A.5)

Module M17A (« Hélices »), calibré selon le nouveau standard ci-dessous
(12 fiches minimum, 8-10 questions/fiche, 2 schémas/fiche quand justifié,
texte 6000+ caractères dès la V1). Plan validé avec l'utilisateur le
2026-09-11 : 14 fiches au total, construites en 3 lots avec relecture et
validation utilisateur après chacun. `disponible: False` dans
`part66/logic.py` jusqu'à validation finale complète du module par
l'utilisateur (test en local requis avant tout push).

**Découpage en 14 fiches** : construction éditoriale de ce projet (comme
pour M5 et M7A), pas une nomenclature officielle recopiée du syllabus
EASA 17A — à confirmer contre le syllabus officiel avant de considérer
la couverture du module comme complète. « Régulation et gouverneur »
(M17A.8) est notamment scindée du reste de la commande de pas (M17A.6,
M17A.7) pour un découpage plus fin que les 7 sous-chapitres officiels
généralement cités.

### Lot 1 (M17A.1-M17A.5, 5 fiches, 43 questions, 10 schémas) — 5 rounds de relecture + reconstruction complète des schémas

Relu par `relecteur-part66` en 5 rounds successifs avant commit —
nettement plus que M5/M7A (1-2 rounds), reflet direct de la complexité
du contenu (deux moments de torsion opposés sur la pale, nouveau
mécanisme à 2 schémas/fiche) : chaque round de correction a corrigé les
BLOQUANT signalés, mais en a parfois introduit de nouveaux (erreur de
sens physique, contradiction entre légende et code d'un schéma,
citation fragile par uid de question). Round 5 : plus aucun BLOQUANT,
lot jugé commitable sur le fond (fiches + questions).

**Test en local (2026-09-11) : schémas signalés absents ou incomplets par
l'utilisateur.** Diagnostic : les 7 schémas du lot 1 étaient tous
construits autour d'une balise `<svg>`, silencieusement supprimée au
rendu par `st.html` (voir la contrainte technique ajoutée dans
`C:\Users\pc\CLAUDE.md` et le point 3 du standard ci-dessus). Les 54
schémas existants de M5 et M7A n'utilisaient déjà aucune balise `<svg>`
— une convention jusque-là non documentée, mais qui s'est révélée être
la seule raison pour laquelle ils fonctionnaient. **Les 7 schémas du lot
1 ont été intégralement reconstruits en HTML/CSS/JS pur** (barres,
aiguilles en `div` tournées par `transform: rotate()`, cadrans
circulaires), et complétés à 2 par fiche (10 schémas au total, contre 7
avant) conformément au standard révisé : M17A.1-2 (comparaison hélice
tractive/propulsive), M17A.4-2 (réparabilité selon matériau et type de
dommage), M17A.5-2 (comparaison bipale/tripale/quadripale) sont
nouveaux ; les 7 autres reprennent le contenu pédagogique déjà validé
par la relecture, seule la technique de rendu change.

Deux rounds de relecture supplémentaires sur les 10 schémas reconstruits :
round 1 a trouvé 2 BLOQUANT (`M17A.1-2.html` — flèche « sens de vol »
statique contredisant la position de l'hélice dans au moins un des deux
modes ; `M17A.4-2.html` — description d'un limage de pale métallique
résumée à tort à « restaurer un profil lisse », sans préciser qu'il faut
retirer entièrement la matière endommagée) et 7 À REVOIR (disclaimers
« illustration » manquants sur plusieurs schémas, libellé ambigu sur la
barre de torsion combinant deux couples opposés, superlatif non
soutenu sur le glissement en croisière, nuances « généralement »/
revêtement de bord d'attaque manquantes sur la coupe composite,
accroche ambiguë et renvoi circulaire sur M17A.5-2) — tous corrigés.
Round 2 (vérification ciblée) a trouvé 1 BLOQUANT résiduel (le
rééquilibrage après réparation métallique était mentionné dans le
schéma `M17A.4-2.html` mais pas dans la fiche M17A.4 — harmonisé) et 3
points mineurs (formulation « en atelier » trop absolue, assouplie en
« selon une procédure approuvée et par du personnel habilité » dans la
fiche et le schéma ; position de la bande de bord d'attaque incohérente
entre les coupes bois et composite du schéma `M17A.4.html`, uniformisée ;
disque « H » de `M17A.1-2.html` non légendé, légende ajoutée) — tous
corrigés. **Lot 1 jugé commitable** après ce second round, sous réserve
de la portée annoncée par le relecteur (round ciblé sur les fichiers
touchés, pas une relecture complète de l'ensemble du lot).

**Points BLOQUANT trouvés et corrigés au fil des rounds** (résumé) :
- Fiche M17A.2 — sens du couple de torsion aérodynamique initialement
  inversé (corrigé : pousse vers un pas plus gros, pas vers un pas
  fin) ; couple de torsion centrifuge absent du texte initial, ajouté
  (pousse vers un pas fin, généralement dominant) ; une première
  reformulation de sa justification physique était elle-même inversée
  (« cherche à se rapprocher de l'axe » corrigé en « à s'éloigner de
  l'axe »).
- `schemas/M17A.3-2.html` — étiquettes pied/extrémité de pale inversées
  par rapport à l'effet réel d'un calage constant (corrigées), puis
  illisibles (texte blanc hors de leur repère) une fois le sens corrigé
  (recentrées, couleur foncée).
- `schemas/M17A.2.html` — affirmait que la force centrifuge « croît plus
  vite » que les trois autres forces représentées, alors que les quatre
  croissent selon la même loi qualitative (seule l'intensité relative
  diffère, à tout régime) ; légende et code désynchronisés sur ce point
  pendant un round.
- Fiche M17A.4 + `schemas/M17A.4.html` + M17A-0030 — pale métallique
  décrite comme « insensible à l'humidité » alors que sa vulnérabilité
  annoncée (la corrosion) est justement favorisée par l'humidité :
  contradiction corrigée par nuance (« ne gonfle pas, ne se délamine
  pas » plutôt qu'« insensible »).
- `schemas/M17A.5.html` — le changement de pas était d'abord représenté
  par un basculement de la pale dans le plan de la vue de dessus (lu
  comme un battement, pas un changement d'angle de calage) ; puis, une
  fois corrigé par une vue en coupe séparée, cette vue ne comportait
  aucune référence au plan de rotation et affichait un calage nul en
  « pas fixe » (laissant croire qu'une hélice à pas fixe n'a pas
  d'angle de calage).
- M17A-0017 — le distracteur « desserrage progressif de la fixation »
  était défendable comme vrai avec un énoncé en « peut provoquer »
  (un desserrage sous vibration est un phénomène réel) : question
  recentrée sur l'effet propre au matériau de la pale.
- M17A-0036 — le distracteur de remplacement confondait battement
  (hors du plan de rotation, propre aux rotors d'hélicoptère) et
  traînée/*lead-lag* (dans le plan de rotation) : terminologie corrigée.
- Plusieurs fuites d'explication entre questions (M17A-0004→0005,
  0019→0023, 0028→0029, 0033→0034, 0010→0014/0015) et un doublon
  déplacé plutôt que résolu au premier passage (M17A-0040 dupliquait
  M17A-0035 après une première réécriture ; recentrée sur le rôle
  secondaire du spinner dans l'équilibrage).

**Dette mineure assumée, non corrigée** (signalée par le relecteur aux
rounds 3-4, jugée non bloquante) :
- `schemas/M17A.2-2.html` — la bande rouge « plage à éviter » est une
  zone fixe du graphique, sans correspondance réelle avec l'axe de
  régime (curseur) ; la légende de résonance (v∈[50,62]) et la forme de
  la courbe ne coïncident pas exactement à la limite des deux bornes.
- `schemas/M17A.2.html` — le plancher de longueur minimale des flèches
  n'est appliqué qu'à la force centrifuge et à la traînée, pas à la
  flexion et à la torsion (tracées à `lLin * 0.6`, sans plancher
  propre) : aux tout petits régimes, les quatre flèches peuvent
  paraître d'intensité comparable, contredisant brièvement le message
  du schéma avant qu'il ne devienne net à régime plus élevé.
- `schemas/M17A.5.html` — l'angle de corde affiché reste visuellement
  plus grand en « pas variable » (−50°) qu'en « pas fixe » (−20°) ; la
  légende précise que ce n'est qu'un exemple parmi une plage possible,
  mais le visuel seul pourrait laisser croire que pas variable signifie
  systématiquement un plus gros pas.
- Déséquilibre de la position de la bonne réponse dans le fichier
  source (23× index 0, 16× index 1, 4× index 2) — neutralisé à
  l'affichage par le mélange par session (`part66/ui.py`), même statut
  que la dette déjà documentée pour M7A.

### Lot 2 (M17A.6-M17A.10, 5 fiches, 41 questions, 10 schémas) — construit
sans balise `<svg>` dès le départ, 3 rounds de relecture

Contrairement au lot 1, les 10 schémas de ce lot ont été construits
directement en HTML/CSS/JS pur (barres, cadrans en `border-radius:50%`,
aiguilles tournées par `transform: rotate()`), sans jamais passer par
une version SVG — la contrainte technique documentée dans
`C:\Users\pc\CLAUDE.md` a été respectée dès la rédaction, pas découverte
après coup.

**BLOQUANT trouvés et corrigés au fil des 3 rounds** : le sujet du lot
(mécanisme hydraulique de calage) introduit une relation physique
précise — les contrepoids poussent la pale vers un pas plus gros
(jusqu'au drapeau), la pression d'huile vers un pas plus fin, en sens
opposés — qui doit rester cohérente à travers 4 fiches, plusieurs
schémas et une douzaine de questions. Une première rédaction a mélangé
cette relation (contrepoids ↔ pas fin au lieu de pas gros) dans les
fiches M17A.7/M17A.8, le schéma `M17A.7.html`, la question M17A-0061 et,
par ricochet, la fiche M17A.6 et la question M17A-0051 (formulation
imprécise des deux couples de torsion opposés de M17A.2) ; corrigé au
round 1 en fixant une seule convention et en la propageant partout.
Round 2 a trouvé que la correction n'avait pas été propagée à un
triplet resté sur l'ancienne logique inversée (fiche M17A.9, question
M17A-0070, schéma `M17A.9-2.html` — tous trois présentaient encore une
« fuite d'huile » comme cause de survitesse, alors que dans le modèle
retenu une perte de pression d'huile laisse les contrepoids l'emporter
et pousse au contraire vers un pas plus gros, donc pas vers une
survitesse) : corrigé en remplaçant l'exemple de panne par un grippage
qui bloquerait le mécanisme en position de pas fin, cohérent avec le
reste du lot. Deux erreurs isolées corrigées au round 1 : une
régression du BLOQUANT « la force centrifuge croît plus vite que les
autres forces » déjà corrigé au lot 1, réapparue par erreur dans la
fiche M17A.9 (reformulée en « intensité largement supérieure », comme
dans `schemas/M17A.2.html`) ; une description auto-contradictoire du
dispositif de survitesse (« une voie de décharge qui envoie davantage
de pression » — corrigée en « qui réduit la pression »). Un bug
d'affichage sans lien avec la physique (zone rouge de survitesse rendue
invisible par un défaut d'empilement CSS dans `M17A.9.html` et
`M17A.9-2.html`, la piste opaque recouvrant la zone) corrigé par un
`z-index` au round 2, vérifié effectif au round 3.

**Dette mineure assumée** : quelques renvois entre questions gardent un
recouvrement conceptuel léger, jugé acceptable (même statut que les
recouvrements déjà admis pour M5/M7A) ; les sources restent génériques
(« Notions générales de construction aéronautique — … »), conforme au
traitement des modules techniques (voir section Méthode).

### Lot 3 (M17A.11-M17A.14, 4 fiches, 32 questions, 8 schémas) — dernier
lot, module complet à 14 fiches, 5 rounds de relecture

Dégivrage/antigivrage, inspection, équilibrage, stockage. Schémas
construits directement en HTML/CSS/JS pur dès le départ, comme le lot 2.

**BLOQUANT trouvés et corrigés au fil des rounds** : une contradiction
avec le lot 1 déjà commité (la fiche M17A.5 attribue les masses logées
dans le spinner à l'équilibrage *dynamique* ; une première version de
M17A.13 les attribuait à tort à l'équilibrage *statique* — corrigé en
retirant la mention du spinner du paragraphe statique et en la
déplaçant vers le paragraphe dynamique, seul endroit cohérent avec
M17A.5) ; un schéma (`M17A.13.html`) où la masse d'équilibrage
s'affichait visuellement du côté lourd de la balance au lieu du côté
léger ; un geste concret de sécurité (rotation manuelle de l'hélice)
enseigné sans aucun garde-fou, contraire au critère 2bis — retiré au
profit du seul principe général, renvoyé au manuel constructeur et aux
procédures de sécurité applicables (retiré en deux temps : une
première correction avait laissé une mention résiduelle dans le
paragraphe de traçabilité, trouvée au round suivant) ; un ressuage
présenté à tort comme applicable au bois (corrigé : rattaché
spécifiquement au métal, le bois n'étant pas sujet à la corrosion) ;
un terme inventé sans signification (« roue à roue ») pour décrire une
méthode de tracking ; une composition de fluide antigivrage affirmée
catégoriquement (« à base de glycol ») alors que plusieurs produits
coexistent selon l'installation ; un schéma (`M17A.11.html`) dont le
mode « antigivrage par fluide » représentait à tort un dégivrage après
coup (pale givrée puis traitée) plutôt qu'une prévention (pale déjà
protégée, jamais givrée) — contredisant directement les questions
testant cette distinction ; un verdict de schéma (`M17A.14-2.html`)
affirmant qu'un contrôle de routine est catégoriquement « suffisant »
sans renvoi au programme d'entretien ; un superlatif non soutenu
(« le plus probablement ») sur la localisation d'une corrosion de
stockage ; un schéma (`M17A.12.html`) dont la mise en page (trois zones
côte à côte, « Pied — Bord d'attaque — Extrémité ») suggérait à tort
que le bord d'attaque est un tronçon entre les deux autres zones, alors
qu'il court sur toute la longueur de la pale — corrigé par réordonnancement
et légende explicite ; une contradiction interne à la fiche M17A.14
(la phrase d'ouverture affirmait que « le temps, à lui seul, peut
dégrader » l'hélice, contredisant mot pour mot le paragraphe suivant
et la question testant précisément ce point).

**Problème systémique trouvé et corrigé** : les 32 questions du lot
avaient toutes leur bonne réponse à l'index 0 des options (contrairement
au simple déséquilibre, tolérable, déjà documenté pour les lots
précédents). Corrigé par un rééquilibrage mécanique (permutation
d'options, contenu inchangé) plutôt qu'une réécriture manuelle,
donnant une répartition 11/11/10 sur les trois index.

**Dette mineure assumée** : le rééquilibrage des positions suit un
cycle 0/1/2/0/1/2 strictement régulier (prévisible en théorie, neutralisé
en pratique par le mélange à l'affichage dans `part66/ui.py`) plutôt
qu'une permutation aléatoire — même statut que la dette de position déjà
documentée pour M7A et les lots précédents de M17A ; quelques distracteurs
restent plus faibles que la moyenne du lot (signalés en relecture,
non corrigés individuellement) ; un léger recouvrement conceptuel
persiste entre certaines questions de la fiche M17A.14 (stockage),
comme pour les lots précédents.

### M17A — enrichissement à partir d'une fiche externe non sourcée (2026-09-13)

L'utilisateur a déposé un fichier `fiche-m17a-externe.md` (racine du
projet), une fiche M17A produite par un autre assistant, non sourcée,
contenant au moins une erreur déjà démontrée (elle annonce ~20
questions pour l'examen M17A ; la source officielle EASA vérifiée le
même jour donne 32 questions/40 min pour B1.1/B1.2/B3 — voir plus haut
dans ce fichier). Une analyse comparative point par point (vrais
manques, divergences de fond, affirmations non sourcées, éléments
pédagogiques réutilisables) a été produite, montrée à l'utilisateur
avant toute écriture, puis reprise sélectivement sur décision explicite.

**Repris et intégré dans les 14 fiches existantes**, reformulé à notre
standard (vulgarisation, « pourquoi » avant « comment »), jamais copié
tel quel : prop strike et règles de réparation (sans chiffre de
tolérance ni règle universelle — expliqués sur le principe, renvoi
systématique au motoriste/constructeur, conformément au critère 2bis),
dédrapeautage, autofeather, sécurités du pas reverse (*squat switch*,
butée de petit pas), hélice à action double, tiroir distributeur et
pompe de gavage, balais et bagues collectrices du dégivrage électrique,
tapotement (*coin tap*) pour le délaminage composite, désactivation du
synchrophaseur au décollage/atterrissage, grille anti-foudre sur pale
composite, station de pale, vocabulaire intrados/extrados/*shank*,
règles de reprofilage (sens de l'envergure, quantité comparable sur
toutes les pales). Un tableau récapitulatif des trois états du
régulateur (on-speed/over-speed/under-speed) a été ajouté à M17A.8, et
une nouvelle fiche **M17A.15 — Mémo express**, condensé de rappels
avant examen couvrant tout le module, a été ajoutée à la fin.

**Délibérément écarté** : la fiche externe affirme, de façon
catégorique et avec des marques citées (Hartzell/McCauley), qu'une
hélice monomoteur va toujours au pas gros (jamais au drapeau) sur perte
de pression d'huile, et qu'une hélice bimoteur va toujours au drapeau.
Notre fiche M17A.7 reste volontairement plus prudente sur ce point
(« un comportement de repli délibérément sûr... reste une
caractéristique de conception à confirmer dans la documentation de
chaque installation plutôt qu'à supposer universelle »). La
distinction externe est plausible et même probablement plus utile
pédagogiquement, mais elle n'est pas sourcée : **conservée en l'état,
non durcie**, tant qu'une source fiable ne confirme pas qu'il s'agit
d'une règle générale plutôt que d'une convention de conception
répandue mais non universelle.

**Autres points de la fiche externe, non repris**, réserves déjà
listées dans l'analyse comparative montrée à l'utilisateur : formule
« vitesse de rotation = 2πrN » (unité de N ambiguë, tr/min vs tr/s) ;
acier comme quatrième famille de matériau de pale (pertinence actuelle
non confirmée) ; statistique de prévalence du dégivrage cyclique
(« quasi-totalité des hélices ») ; position de stockage alu/bois
présentée comme règle générale plutôt que propre au constructeur ;
terminologie « face = toujours arrière » reprise avec un degré de
confiance moindre que les autres ajouts, faute de source citée.

**Relecture `relecteur-part66` de ces ajouts (2026-09-13) : 6 BLOQUANT
et 7 points à revoir corrigés avant commit.** Bloquants : la pompe de
gavage (M17A.8) était décrite en amont du régulateur au lieu d'un
composant intégré à celui-ci ; l'exemple de synthèse de M17A.10
contredisait la règle de désactivation du synchrophaseur au décollage
qui venait d'être ajoutée juste au-dessus (déplacé en croisière) ; le
mémo M17A.15 présentait à tort l'autofeather comme « l'équivalent »
du dispositif de survitesse, alors que M17A.9 dit explicitement que ce
n'est pas la même fonction (déclenchement par perte de couple, pas par
survitesse) ; le même mémo citait une taxonomie « à quatre familles »
de pas (fixe/réglable au sol/variable/vitesse constante) que ne
couvrent ni M17A.5 ni M17A.6, la vitesse constante étant un cas du pas
variable détaillé en M17A.8, pas une famille parallèle ; les sécurités
du pas reverse (M17A.7) étaient présentées de façon trop catégorique
(« la plus courante », « butée mécanique », synonyme *beta stop* non
sourcé) pour un point de sécurité — dé-catégorisé, renvoyé à l'AMM de
chaque installation ; la ligne « reprofilage » du mémo durcissait la
règle de M17A.4 en supprimant la clause de limite documentaire et de
procédure approuvée, transformant une bonne pratique encadrée en
instruction sèche sur des pales saines.

Corrections mineures (cohérence/vocabulaire) : ajout d'une réserve
dans M17A.13 notant qu'un déséquilibre résiduel peut subsister même en
suivant la nouvelle règle de M17A.4 (retirer une quantité comparable
sur chaque pale) ; glose de « hélice tractive » ajoutée en M17A.1 là où
le terme est utilisé avant sa définition complète plus bas dans la
fiche ; condition d'armement ajoutée à la description de l'autofeather
en M17A.9 ; renvoi croisé ajouté en M17A.12 vers l'essai moteur
(run-up) de M17A.9 ; mémo M17A.15 aligné sur le vocabulaire réel du
module (« orientation efficace par rapport à l'air », pas « angle
d'attaque », terme jamais défini dans les 14 fiches) et sur la
prudence de M17A.7 (« certains turbopropulseurs », pas « gros
turbopropulseurs »).

**Point signalé par la relecture et non traité aujourd'hui** :
`M17A.11` décrit les éléments chauffants du dégivrage électrique comme
« intégrés » au bord d'attaque, alors qu'il s'agit le plus souvent de
tapis (*boots*) collés en surface — imprécision préexistante,
antérieure à l'ajout balais/bagues collectrices d'aujourd'hui, qui la
rend seulement plus visible. À corriger lors d'un prochain passage sur
M17A.11, pas traité dans ce chantier.

**Dette assumée sur M17A.15 (nouvelle fiche « Mémo express »)** : à la
différence des 14 autres fiches du module, elle ne porte ni question
ni schéma associés (`charger_schemas` renvoie une liste vide sans
plantage ; elle n'apparaît donc pas dans le suivi de progression par
sous-chapitre, qui se construit à partir de `questions.json`). C'est
volontaire — un condensé de rappels n'a pas vocation à être interrogé
comme les autres fiches — mais ça l'écarte du standard habituel du
module (8-10 questions/fiche, 2 schémas/fiche), à assumer explicitement
plutôt qu'à corriger.

## M15 — module complet (« Turbomachines à gaz »)

Plan validé avec l'utilisateur le 2026-09-11 : 14 fiches (M15.1 à
M15.14, découpage maison à confirmer contre le syllabus officiel EASA,
même statut que M11A/M17A), calibrées selon le standard ci-dessous dès
la V1, construites en 3 lots (M15.1-M15.5, M15.6-M15.10,
M15.11-M15.14) avec relecture et validation utilisateur après chacun,
même méthode que M17A. Module complet et validé par l'utilisateur
(tests locaux inclus) le 2026-09-11 ; `disponible: True` dans
`part66/logic.py`.

**Lot 3 (M15.11-M15.14)** : relu en 2 rounds par `relecteur-part66`.
Le premier round a trouvé 7 BLOQUANT — deux renvois croisés faux vers
d'autres fiches du module (le FOD attribué à tort à M15.6 au lieu de
M15.2 ; l'analyse spectrométrique d'huile attribuée à tort à M15.7, qui
ne parle que du détecteur de particules magnétique), une formulation
auto-contradictoire sur le régime de référence (« régime maximal
certifié » présenté comme le 100 % de N, incompatible avec la phrase
suivante sur la comparaison aux limites certifiées), une phrase
impliquant à tort qu'un dépassement de régime serait sans risque, un
chiffrage non sourcé et douteux sur le nombre de bouteilles
d'extinction (« souvent deux par moteur »), une logique de
déclenchement de l'extinction énoncée comme un principe technique alors
qu'elle relève du seuil/de la procédure d'urgence hors du périmètre
autorisé sur M15.13, et une séquence d'actions (coupure carburant →
isolement circuits → décharge extincteur) répétée invariablement à 6
endroits qui enseignait de fait un ordre malgré son disclaimer. Tous
corrigés ; un round de vérification ciblée a trouvé un correctif
incomplet (le renvoi croisé de M15.14 vers M15.7 n'avait été qu'à
moitié corrigé) et deux régressions mineures (distracteurs trop faibles
sur la question réécrite M15-0110, ordre non varié dans un des
schémas), tous corrigés à leur tour et revérifiés directement dans les
fichiers.

**Schéma M15.11 (tableau de bord moteur), retour utilisateur après
test local** : les valeurs chiffrées affichées (régime 91 %, TGT
640 °C, débit 1 240 kg/h), bien que marquées « illustratives »,
restaient le genre de valeurs qu'un débutant risque de mémoriser comme
un repère réel. Remplacées par des indications qualitatives (barre de
niveau sans valeur affichée, libellés « Plage normale » / « Débit
stable » / « Faible ») plutôt que par un chiffre, même fictif.

Table des 14 fiches (fige les titres et numéros pour tous les renvois
croisés entre fiches, afin d'éviter toute incohérence comme celle
relevée en relecture du lot 1 sur M15.9) :

| Lot | Fiche | Titre |
|---|---|---|
| 1 | M15.1 | Principe du cycle du turboréacteur |
| 1 | M15.2 | Entrée d'air (inlet) |
| 1 | M15.3 | Compresseurs |
| 1 | M15.4 | Chambre de combustion |
| 1 | M15.5 | Turbine |
| 2 | M15.6 | Tuyère d'échappement |
| 2 | M15.7 | Système d'huile |
| 2 | M15.8 | Système carburant |
| 2 | M15.9 | Démarrage anormal (allumage et démarrage — principe, sans procédure pilote) |
| 2 | M15.10 | Régulation moteur |
| 3 | M15.11 | Indications moteur (poste de pilotage) |
| 3 | M15.12 | Inversion de poussée |
| 3 | M15.13 | Protection incendie moteur |
| 3 | M15.14 | Surveillance et entretien |

**Consigne de portée explicite de l'utilisateur, à respecter sur les
fiches M15.9 (démarrage anormal) et M15.13 (protection incendie
moteur) :** ces deux fiches touchent à des situations d'urgence
réelles. Le contenu doit enseigner le principe technique — ce qui se
passe, pourquoi c'est grave, ce que cela implique côté entretien —
**mais jamais la procédure pilote elle-même**, qui relève du manuel de
vol propre à chaque appareil. Le critère 2bis s'applique pleinement :
aucune séquence d'actions pilote, aucun seuil d'alarme précis, aucune
procédure d'urgence à reproduire ne doit figurer dans ces deux fiches
ni dans leurs schémas ou questions.

## M11A — construction en cours (module « Aérodynamique, structures et
systèmes — avion à turbine »)

Plan validé avec l'utilisateur le 2026-09-11 : de loin le plus gros
module du parcours (140 questions à l'examen réel, contre 32 pour
M17A ou 25 pour M15/M7A) — **25 fiches, construites en 5 lots de 5**
plutôt que les 3 lots utilisés pour M15/M17A, calibrées selon le
standard de la section ci-dessous dès la V1. Relecture et validation
utilisateur après chaque lot, même méthode que M15/M17A.
`disponible: False` dans `part66/logic.py` jusqu'à validation finale
complète du module.

Découpage éditorial de ce projet, pas la nomenclature officielle EASA
du syllabus 11A — même statut que M5/M7A/M15/M17A, à confirmer contre
le syllabus officiel avant de considérer la couverture du module comme
complète.

Table des 25 fiches (fige les titres et numéros pour tous les renvois
croisés entre fiches) :

| Lot | Fiche | Titre |
|---|---|---|
| 1 | M11A.1 | Forces aérodynamiques fondamentales (portance, traînée, profil, incidence) |
| 1 | M11A.2 | Décrochage et stabilité |
| 1 | M11A.3 | Vol à grande vitesse (compressibilité, effets Mach — spécificité avion à turbine) |
| 1 | M11A.4 | Principes et matériaux de structure (charges, contraintes, métal/composite) |
| 1 | M11A.5 | Éléments structuraux (fuselage, voilure, empennage, assemblage) |
| 2 | M11A.6 | Commandes de vol : gouvernes principales et secondaires (trims, compensateurs) |
| 2 | M11A.7 | Systèmes d'actionnement des commandes (mécanique, hydraulique, électrique/fly-by-wire) |
| 2 | M11A.8 | Dispositifs hypersustentateurs (volets, becs, spoilers) |
| 2 | M11A.9 | Circuits hydrauliques : principes (pression, pompes, actionneurs) |
| 2 | M11A.10 | Circuits hydrauliques : architecture et redondance |
| 3 | M11A.11 | Train d'atterrissage : structure et fonctionnement |
| 3 | M11A.12 | Train d'atterrissage : extension/rétraction et secours |
| 3 | M11A.13 | Circuits pneumatiques (air prélevé / bleed air) |
| 3 | M11A.14 | Conditionnement d'air |
| 3 | M11A.15 | Pressurisation |
| 4 | M11A.16 | Protection contre le givre et la pluie |
| 4 | M11A.17 | Circuit carburant (cellule : réservoirs, transfert, jaugeage) |
| 4 | M11A.18 | Génération électrique (générateurs, batteries, alimentation de secours) |
| 4 | M11A.19 | Réseau, distribution et protection des circuits électriques |
| 4 | M11A.20 | Instruments de vol |
| 5 | M11A.21 | Avionique et gestion de vol |
| 5 | M11A.22 | Protection incendie (cellule, hors moteur déjà couvert en M15) |
| 5 | M11A.23 | Oxygène |
| 5 | M11A.24 | Portes et issues |
| 5 | M11A.25 | Maintenance de la cellule (inspection, corrosion, CND) |

**Consigne de portée explicite de l'utilisateur, même principe que
M15.9/M15.13 — à respecter sur M11A.9/M11A.10 (hydraulique haute
pression), M11A.12 (train : extension/rétraction et secours),
M11A.15 (pressurisation), M11A.22 (protection incendie cellule),
M11A.23 (oxygène) et M11A.24 (portes et issues) :** ces fiches
touchent à des systèmes à haute énergie ou à des situations
d'urgence réelles. Le contenu doit enseigner le principe technique —
ce qui se passe, pourquoi c'est grave, ce que cela implique côté
entretien — **mais jamais la procédure d'équipage ni un geste qui
pourrait être reproduit sans les précautions complètes** (isolement
de pression avant intervention, consignation, équipement de
protection...), qui relèvent du manuel de vol ou de la documentation
constructeur propre à chaque appareil. Le critère 2bis s'applique
pleinement sur ces six fiches : aucune séquence d'actions
équipage/mécanicien, aucun seuil précis (pression, altitude cabine,
durée), aucune procédure à reproduire ne doit figurer dans leur texte,
leurs schémas ou leurs questions.

### Lot 1 (M11A.1-M11A.5, 5 fiches, 45 questions, 10 schémas) — validé, 2 rounds de relecture

Relu par `relecteur-part66` : le premier round a trouvé 5 BLOQUANT —
un sophisme du « temps de transit égal » dans l'explication de la
portance (M11A.1, contredit par le schéma lui-même) ; l'avantage de
l'empennage en T énoncé à l'envers sur son point critique (M11A.5 et
M11A-0043 : l'éloignement du sillage est un avantage en vol normal,
pas à fort angle d'incidence, où c'est l'inverse qui se produit) ; un
renvoi fabriqué vers le module M5 (M11A.3, qui ne parle jamais de
vitesse air) ; une courbe de portance qui chutait avant l'angle
critique dans un schéma (`M11A.1-2.html`) ; un schéma de comparaison
d'oscillations (`M11A.2-2.html`) rendu illisible par un `clip-path`
en pourcentages sur un élément de 2px de haut. Tous corrigés ; un
round de vérification a confirmé les 5 correctifs et trouvé 2
régressions mineures introduites par les correctifs eux-mêmes
(sequence d'amplitude plafonnée dans `M11A.2-2.html`, formulation
ambiguë dans `M11A.1-2.html`), également corrigées. Plusieurs points
À REVOIR traités dans la foulée : terminologie traction/poussée
harmonisée avec M15, distracteurs faibles renforcés sur 4 questions,
un doublon remplacé, deux questions « méta » reformulées, et le
schéma des 5 sollicitations structurales (`M11A.4.html`) reconstruit
pour que cisaillement/flexion/torsion soient visuellement
distinguables plutôt que rendus par les seules flèches et le texte.

**Retour utilisateur après test local (2026-09-12) : les 10 schémas
manquaient de légendes permanentes et de texte d'explication initial
utile.** Corrigé sur les 10 fichiers : chaque élément visuel porte
désormais un libellé texte visible en permanence (pas seulement au
clic), et la zone d'explication affiche dès le chargement une phrase
qui décrit l'état montré et invite explicitement à cliquer pour
comparer. Cette double exigence est désormais documentée comme
contrainte permanente dans `C:\Users\pc\CLAUDE.md` (section
« Contrainte de contenu : schémas interactifs Part-66 — légendes
permanentes et texte initial non vide ») et s'applique dès la
rédaction de tout schéma des lots suivants, pas seulement en
correction a posteriori. **Lot 1 validé par l'utilisateur, tests
locaux inclus, le 2026-09-12.**

### Lot 2 (M11A.6-M11A.10, 5 fiches, 45 questions, 10 schémas) — validé

Commandes de vol (gouvernes principales/secondaires, trims,
servo-tabs), systèmes d'actionnement (mécanique, hydraulique assisté,
électrique/fly-by-wire), dispositifs hypersustentateurs (volets, becs,
spoilers), circuits hydrauliques (principes, puis architecture et
redondance). M11A.9 et M11A.10 soumises à la même consigne de portée
stricte que M15.9/M15.13 (principe et conséquences entretien
uniquement, jamais de valeur de pression ni de procédure d'isolement
détaillée).

Relu par `relecteur-part66` : 3 BLOQUANT trouvés et corrigés — un
renvoi fabriqué vers M11A.5 dans M11A.7 (même motif que le lot 1) ;
une légende de schéma (`M11A.9-2.html`) affirmant que dépressuriser et
isoler « rend une intervention sûre », un raccourci trop absolu compte
tenu de l'énergie résiduelle possible d'un accumulateur — corrigé, et
la fiche M11A.9 complétée d'une phrase de principe sur cette énergie
résiduelle ; trois schémas (`M11A.6-2.html`, `M11A.8.html`,
`M11A.8-2.html`) où un élément visible dès le chargement (trim, bec,
volet, spoiler) n'était pourtant nommé qu'après un clic, contraire à
la contrainte de légendes permanentes tout juste adoptée — corrigé en
rendant ces libellés visibles en permanence. Coquilles corrigées suite
à un retour utilisateur : « different » → « différent » (M11A.9),
anglicisme « near » → « près de » (M11A.6). Plusieurs points À REVOIR
traités dans la foulée : deux doublons de questions remplacés, trois
questions « méta » reformulées, un jeu de distracteurs auto-réfutants
corrigé, six distracteurs trop faibles (« à des fins esthétiques »,
« par confort », etc.) renforcés, et deux incohérences visuelles
mineures corrigées (`M11A.6-2.html` : la gouverne reste maintenant
visiblement braquée dans les deux vues ; `M11A.7-2.html` : l'aiguille
de sensation garde le même angle entre les deux vues, seule son
origine change). **Lot 2 validé par l'utilisateur le 2026-09-12.**

**Point de configuration (hors banque de questions)** : `nb_questions_examen: 140`
confirmé par l'utilisateur. `duree_examen_min: 175` = 75 secondes par
question × 140, règle générale Part-66 pour les QCM — valeur
retenue sur cette base mais **non vérifiée sur l'Appendix VIII
officiel**, même statut TODO que les autres modules.

### Lot 3 (M11A.11-M11A.15, 5 fiches, 45 questions, 10 schémas) — relu, 4 BLOQUANT corrigés

Train d'atterrissage (structure, extension/rétraction et moyen de secours),
circuits pneumatiques (air prélevé), conditionnement d'air, pressurisation.
M11A.12 et M11A.15 soumises à la même consigne de portée stricte que
M11A.9/M11A.10 (principe et conséquences entretien uniquement, jamais de
seuil précis ni de procédure d'équipage/mécanicien reproductible) — relu et
jugé conforme.

Relu par `relecteur-part66` : 4 BLOQUANT trouvés et corrigés avant commit —
quatre explications de questions (M11A-0094, M11A-0113, M11A-0116,
M11A-0127) réfutaient un distracteur imaginaire au lieu du distracteur
réellement présent dans les options, laissant ce dernier sans réfutation
(même motif que les « renvois inventés » des lots précédents, transposé aux
options) ; la répartition énergétique de l'amortisseur oléopneumatique
(fiche M11A.11 et M11A-0093) attribuait à tort au gaz comprimé l'essentiel
de l'absorption d'énergie, alors que c'est le passage forcé du fluide
hydraulique dans l'orifice calibré qui dissipe l'essentiel de l'énergie en
chaleur (le gaz, lui, l'encaisse et la restitue comme un ressort) — reformulé
dans les deux emplacements ; le schéma `M11A.11.html` contredisait sa
propre légende en vue « Classique » (le marqueur CG et sa légende n'étaient
jamais repositionnés par le script, plaçant le CG sur une roue principale
au lieu de le montrer en arrière des roues principales comme l'annonce la
légende) et la caption annonçait un avion « cabré au sol » sans qu'aucune
inclinaison ne soit représentée — corrigé (CG et légendes repositionnés par
mode, fuselage incliné par `transform: rotate()` en vue classique, technique
déjà validée dans le projet pour les angles) ; `schemas/M11A.13.html`
présentait une divergence entre le texte HTML statique et le texte JS de
l'état par défaut (bug explicitement documenté comme à éviter dans
`C:\Users\pc\CLAUDE.md`) — harmonisés.

Plusieurs points À REVOIR traités dans la foulée : distracteurs
auto-réfutés par la prémisse même de la question ou franchement absurdes
renforcés sur 7 questions (M11A-0096, M11A-0103, M11A-0119, M11A-0121,
M11A-0135, M11A-0136, et M11A-0109 reformulée) ; deux questions « méta »
supplémentaires (M11A-0109, M11A-0132, portant sur ce que « la fiche »
couvre ou non) reformulées en questions directes sur la répartition des
responsabilités constructeur/manuel de vol, dans le même esprit que les
questions méta déjà reformulées au lot 1 ; une troisième (M11A-0133)
allégée de sa référence explicite à « la fiche » sans changer la
connaissance testée ; indice de longueur de la bonne réponse atténué sur 4
questions par allongement mesuré des distracteurs (M11A-0100, M11A-0117,
M11A-0126, M11A-0134) ; légende « Voilure » de `M11A.12.html` repositionnée
sur l'aile réellement centrée par le flex (elle flottait à gauche dans le
vide) ; chevauchement texte/barre corrigé dans `M11A.13-2.html` (le statut
passe désormais sous le cadre plutôt que par-dessus, même convention que
`M11A.15-2.html`) ; `M11A.14.html` affichait deux flèches consécutives en
vue par défaut (une flèche jamais masquée par le script, qui ne la
référençait même pas) — corrigé, la flèche suit maintenant le même
affichage/masquage que les autres éléments de l'étape turbine.

Restent, en dette mineure assumée (même statut que les points similaires
documentés pour M5/M7A/M17A) :
- `schemas/M11A.11-2.html` — la coexistence gaz/fluide de l'amortisseur est
  représentée par un simple rectangle bleu dont seule la hauteur varie, sans
  chambre de gaz, chambre d'huile ni orifice identifiables ; la roue n'a pas
  de libellé permanent. À enrichir dans un round de finition.
- `schemas/M11A.15.html` — la « valve de contrôle de sortie » n'existe que
  comme libellé texte, sans élément visuel associé, alors qu'elle est le
  mécanisme central de la fiche.
- `schemas/M11A.15-2.html` — une soupape unique y protège « dans un sens
  comme dans l'autre », simplification d'un mécanisme qui comporte en
  réalité des soupapes distinctes pour la surpression et la dépression ; la
  fiche parle bien de « valves » au pluriel, seul le schéma simplifie à une
  seule.
- `schemas/M11A.14.html` — le ventilateur entraîné par la turbine, mentionné
  dans la caption et testé par M11A-0121, n'apparaît pas visuellement dans
  le diagramme.
- `fiches.json` (M11A.14) — la machine à cycle d'air est décrite en cycle
  simple (turbine entraînant un seul ventilateur), alors que la plupart des
  avions de transport modernes utilisent une machine bootstrap à 3-4 roues
  où la turbine entraîne aussi un compresseur ; acceptable au niveau B1.1
  mais à noter explicitement si le sujet est approfondi plus tard.
- Léger recouvrement de connaissance entre M11A-0128 (principe de la valve
  de contrôle de sortie) et M11A-0134 (comportement de cette même valve en
  montée) — pas un doublon strict, mais une distinction fine.
- Numérotation : uid `M11A-0089` inexistant (saut hérité du lot 2 entre
  0088 et 0090) et `M11A-0135`/`M11A-0136` insérés hors séquence au milieu
  du lot 3 — sans effet fonctionnel, mais nuit à la traçabilité par uid.

**Lot 3 relu et corrigé le 2026-09-13 ; reste à tester en local et faire
valider par l'utilisateur avant de passer `disponible` à `True`** (même
étape que les lots précédents — voir le retour utilisateur du lot 1 sur les
légendes permanentes, qui n'était apparu qu'au test réel en navigateur).

### Lot 4 (M11A.16-M11A.20, 5 fiches, 45 questions, 10 schémas) — relu, 2 rounds de correction

Protection contre le givre et la pluie, circuit carburant de la cellule
(réservoirs, transfert, jaugeage), génération électrique, réseau/
distribution/protection électrique, instruments de vol. Lot rédigé après
une coupure de connexion qui a interrompu la session juste avant l'écriture
des fichiers (aucun fichier du lot 4 n'existait encore à la reprise) —
repris de zéro sur la base du plan déjà établi.

Relu par `relecteur-part66` en 3 rounds (1 relecture complète + 2
vérifications ciblées) : le premier round a trouvé 4 BLOQUANT — la sonde
Pitot décrite comme mesurant la « pression dynamique » au lieu de la
« pression totale » (fiche M11A.20, M11A-0173, M11A-0175, caption de
`M11A.20.html`), le terme « cavitation » employé à tort pour la
vaporisation du carburant en conduite (en réalité un bouchon de vapeur/
vapor lock, fiche M11A.17, M11A-0149, M11A-0150), le schéma
`M11A.17-2.html` représentant deux pompes d'alimentation montées en série
alors que la fiche parle de pompes indépendantes (donc en parallèle), et
les 45 questions du lot ayant toutes `"bonne": 0` (violation du standard
du projet qui demande une répartition dès la rédaction). Un premier
correctif a résolu 3 de ces 4 points mais introduit une régression sur le
quatrième (la correction Pitot avait remplacé l'erreur de terminologie par
une sur-généralisation — « les trois instruments exploitent les deux
pressions », contredite par le développement de la fiche elle-même qui dit
l'inverse pour l'altimètre et le variomètre) et laissé passer une
occurrence résiduelle dans un distracteur (M11A-0174) ainsi qu'une
contradiction nouvelle entre la fiche M11A.18 (nouvellement corrigée pour
distinguer CSD et IDG) et M11A-0155 (qui citait encore l'IDG comme exemple
de « dispositif d'entraînement »). Un second correctif a résolu ces quatre
points ; un troisième round de vérification n'a trouvé aucun BLOQUANT
restant.

Points À REVOIR traités dans la foulée des deux rounds de correction :
plusieurs distracteurs absurdes ou auto-réfutés renforcés
(M11A-0141, 0143, 0146, 0153, 0167, 0168, 0171, 0177) ; deux questions
retravaillées pour ne plus se chevaucher (M11A-0149/M11A-0150) ; un renvoi
croisé pointant la mauvaise fiche corrigé (M11A.17 renvoyait à M11A.4 au
lieu de M11A.5 pour les longerons/nervures de la voilure) ; le mécanisme de
réduction de la flexion de l'aile par le carburant en voilure reformulé
(l'ancienne formulation, « poids réparti près du centre de portance »,
restait physiquement approximative) ; la distinction avion à hélice/avion
à turbine remplacée par turbopropulseur/avion à réaction pour la
comparaison boots pneumatiques vs anti-givrage continu (un turbopropulseur
est aussi un avion à turbine) ; la phrase de la fiche M11A.17 qui évitait
de nommer le risque d'inflammabilité des vapeurs de carburant reformulée
pour le nommer explicitement, sans détail de procédure ; deux divergences
caption/libellé statique-JS corrigées (`M11A.17.html`, `M11A.20-2.html`,
même classe de bug que celle documentée dans `C:\Users\pc\CLAUDE.md`) ;
libellés de `M11A.19-2.html` renommés pour désigner les bons éléments
(un segment de câble plutôt que « le bus » ou « l'équipement » eux-mêmes) ;
un repère permanent ajouté sur `M11A.19.html` pour préciser ce que
représente la hauteur des barres. Une régression JavaScript (apostrophe
non échappée dans une chaîne à guillemets simples, introduite par un
correctif de libellé sur `M11A.19-2.html`) a été détectée par un contrôle
de syntaxe systématique (Node `new Function()` sur le contenu de chaque
`<script>`) et corrigée avant le round de vérification suivant — ce
contrôle de syntaxe est désormais recommandé après toute modification de
libellé dans un schéma existant.

Restent, en dette mineure assumée :
- M11A-0150 — le critère de vaporisation du carburant est simplifié en
  « pression du carburant maintenue au-dessus de la pression atmosphérique
  environnante » ; le critère physique réel est la tension de vapeur du
  carburant à sa température, un point plus fin qu'il n'a pas paru utile
  de développer au niveau B1.1.
- Léger recouvrement entre M11A-0146 (pourquoi la voilure humide existe :
  poids + structure) et M11A-0153 (mécanisme précis de réduction de la
  flexion) — pas un doublon strict, la frontière entre les deux s'est
  resserrée après reformulation.
- `schemas/M11A.16.html` — le libellé « Givre » masqué par `opacity: 0`
  plutôt que `display: none` en vue anti-givrage : invisible à l'écran
  mais techniquement présent et sélectionnable dans le DOM. Cosmétique.

**Lot 4 relu et corrigé le 2026-09-13 ; reste à tester en local et faire
valider par l'utilisateur avant de passer `disponible` à `True`.**

### Lot 5 (M11A.21-M11A.25, 5 fiches, 45 questions, 10 schémas) — dernier lot du module, relu et corrigé sur 5 rounds

Avionique et gestion de vol (FMS, IRS/GPS, autothrust), protection
incendie de la cellule hors moteur (soute, APU, cabine — complète
M15.13), oxygène, portes et issues, maintenance de la cellule
(inspection, corrosion, contrôle non destructif). Ce lot referme le
module M11A à 25/25 fiches. M11A.22, M11A.23 et M11A.24 soumises à la
consigne de portée stricte (même niveau que M11A.9/M11A.10/M11A.12/
M11A.15) : principe technique et implications d'entretien uniquement,
aucune procédure d'équipage/mécanicien, aucun seuil précis (pression,
composition d'agent extincteur). Ce lot a en outre construit dès la
rédaction la répartition 0/1/2 de la position de la bonne réponse
(15/15/15), plutôt que de la corriger après coup comme au lot 4.

Relu par `relecteur-part66` sur 5 rounds (1 relecture complète + 4
vérifications ciblées, un nombre inhabituel reflétant la difficulté
propre à ce lot — avionique de précision et mécanismes physiques peu
intuitifs comme la porte à obturateur) :

- **Round 1** a trouvé 7 BLOQUANT : la fiche M11A.21 attribuait à tort
  aux gyroscopes de l'IRS le principe de « rigidité gyroscopique » des
  instruments mécaniques de M11A.20, alors qu'une IRS moderne mesure
  directement la rotation de l'avion (gyromètres) — corrigé en
  distinguant explicitement les deux principes ; la fiche M11A.22 et
  M11A-0193 justifiaient la décharge prolongée d'agent extincteur en
  soute par une comparaison de facilité de ventilation avec le
  compartiment moteur, un raisonnement physiquement inversé — corrigé
  en expliquant que le contenu d'une soute, contrairement à un
  incendie moteur privé de son carburant, ne peut pas être coupé de ce
  qui l'alimente ; `schemas/M11A.22.html` présentait la détection du
  compartiment moteur comme « tardive », contredisant la fiche
  elle-même — schéma reconstruit ; `schemas/M11A.25.html` affichait un
  état initial vide (aucun défaut ni libellé visible avant clic),
  contraire à la caption qui annonçait déjà une fissure révélée —
  reconstruit pour que les deux défauts restent visibles en
  permanence, seul un badge « Détecté »/« Non détecté » basculant
  selon la méthode ; `schemas/M11A.24.html` (porte à obturateur)
  présentait une cinématique et un sens de vue incohérents avec sa
  propre caption — reconstruit en vue de dessus explicite avec des
  repères « Intérieur cabine »/« Extérieur » ; la fiche M11A.24
  contenait un renvoi fabriqué vers M15.11 (qui ne traite que des
  indications moteur, pas des indicateurs de position de porte),
  corrigé en M11A.20 ; `schemas/M11A.23-2.html` (illustration
  qualitative de l'oxygène comme comburant) omettait de préciser
  qu'une combustion dans l'air ambiant nécessite une source
  d'allumage, contrairement à l'oxygène concentré — précisé.
- **Round 2** (vérification des 7 points) a confirmé 4 corrections
  effectives et trouvé 3 résidus/régressions introduits par le
  premier correctif lui-même : la reconstruction de `M11A.24.html`
  avait corrigé le sens de vue mais laissait une géométrie fausse (la
  porte débordait très majoritairement hors du cadre, et aucune
  ouverture n'était visuellement représentée, juste une barre pleine)
  — reconstruit une seconde fois avec des coordonnées explicites
  (deux segments de paroi séparés par un vide de 80 px, une porte de
  100 px qui les chevauche des deux côtés) ; la reconstruction de
  `M11A.25.html` avait involontairement fait dire au badge de l'état
  Ultrasons qu'une fissure de surface n'est « jamais » détectée par
  cette méthode, une affirmation catégorique et fausse — adouci en
  « méthode non privilégiée », aligné sur la formulation de la fiche
  (« ultrasons pour une fissure plus profonde ») ; un renvoi vers
  M11A.19 (redondance électrique de l'éclairage de secours), jugé
  incohérent avec le reste du module qui associe cette redondance à
  M11A.18, était resté dans l'explication de M11A-0214 après avoir été
  corrigé dans la fiche — propagé à la question.
- **Round 3** (vérification des 3 résidus) a confirmé 2 corrections
  effectives et trouvé 1 problème de rendu introduit par le correctif
  du round 2 : le nouveau texte du badge « Méthode non privilégiée »,
  plus long que l'ancien, débordait sur le badge voisin dans
  `M11A.25.html`, et le libellé permanent « Pièce inspectée (coupe) »
  se superposait déjà au badge de la fissure de surface dans l'état
  par défaut (un problème préexistant, pas une régression) — les deux
  badges raccourcis (« Peu adapté » au lieu de « Méthode non
  privilégiée ») et repositionnés, le libellé de la pièce déplacé plus
  haut.
- **Round 4** (vérification du repositionnement) a trouvé un
  chevauchement résiduel de ~2 px entre les badges repositionnés et la
  pointe du marqueur de fissure de surface, introduit par le
  repositionnement lui-même — badges redescendus de 4 px.
- **Round 5** (vérification finale) a confirmé l'absence de
  chevauchement calculable dans les deux états, sous réserve d'une
  dépendance non neutralisée à la hauteur de ligne héritée du thème
  Streamlit (`st.html` insère son contenu directement dans le DOM,
  sans iframe) — `line-height: 1.2` ajouté explicitement à la règle du
  badge pour rendre le résultat indépendant du thème plutôt que de
  laisser cette marge de 2 px reposer sur un calcul non garanti.

Plusieurs points À REVOIR traités dans la foulée des rounds 1-2 :
harmonisation de la terminologie « poussée » (plutôt que « régime »)
entre l'autothrust de M11A.21 et la régulation moteur de M15.10 ;
trois questions quasi identiques testant « qui définit la procédure
suivie par l'équipage » (motif déjà utilisé pour M11A-0109 au lot 3)
réduites à une seule occurrence dans ce lot, les deux autres
recentrées sur un contenu distinct déjà présent dans leur fiche
(indépendance des boucles/bouteille incendie de l'APU ; second usage
du toboggan comme radeau flottant) ; deux autres recouvrements de
questions (FMS/pilote automatique ; plaquage de la porte par la
pression) résolus en recentrant l'une des deux questions sur un angle
distinct déjà présent dans la fiche mais pas encore testé (rôle de
l'IRS/GPS pendant l'exemple de descente ; état du toboggan pendant
l'exemple de la porte) ; la fiche M11A.22 complétée d'une mention de
l'extincteur automatique de la poubelle des essuie-mains des
toilettes (équipement standard non mentionné dans la première
version), avec le distracteur de M11A-0196 renforcé en conséquence.

Restent, en dette mineure assumée :
- `schemas/M11A.21.html` — les valeurs « 250 nœuds »/« 300 nœuds »
  initialement utilisées pour illustrer un reroutage ont été
  remplacées par « vitesse cible initiale »/« vitesse cible
  recalculée » (un reroutage n'implique pas nécessairement une
  augmentation de vitesse, et 250 kt évoque une limite réglementaire
  sans rapport avec l'exemple) — dette déjà résolue au moment de la
  rédaction, mentionnée ici pour mémoire.
- `schemas/M11A.25.html` — la boîte du libellé « Pièce inspectée
  (coupe) » ne laisse qu'une marge réduite avant un éventuel retour à
  la ligne si la taille de police héritée du thème dépassait largement
  16px ; `white-space:nowrap` a été ajouté pour neutraliser ce risque,
  mais sans garantie absolue sur un thème très éloigné du défaut.

**Lot 5 relu et corrigé le 2026-09-13. Le module M11A est maintenant
complet à 25/25 fiches, 225 questions, 50 schémas. Module validé par
l'utilisateur, test local complet inclus, le 2026-09-13 ; `disponible`
passé à `True` dans `part66/logic.py`.**

## M5.1 / M5.5 / M15.1-2 — bug résolu : génération de DOM à l'exécution
(investigation menée le 2026-09-11, cause identifiée et corrigée)

**Symptôme :** dans les fiches M5.1, M5.5, puis plus tard M15.1 (second
schéma), les boutons des schémas interactifs ne répondaient à aucun
clic (ou, pour M15.1-2, le bouton réagissait visuellement mais le
contenu en dessous restait vide), sans aucune erreur en console —
reproduit en local et sur le déploiement Streamlit Cloud, y compris en
navigation privée.

**Un bug distinct, corrigé en premier et sans rapport avec la cause
finale :** `st.expander()` était appelé sans `key=` explicite dans
`part66/ui.py` (`_page_cours`), ce qui laissait Streamlit réutiliser
l'identité d'un expander par position plutôt que par contenu réel lors
d'un changement de module — la fiche M7A.9 affichait par moments le
schéma de M5.9. **Corrigé** en ajoutant
`key=f"p66_expander_{module}_{fiche['id']}"` à l'appel de
`st.expander()`. Confirmé par test utilisateur.

**Hypothèses explorées puis chacune invalidée par un test, avant de
trouver la vraie cause :**

1. *Cache/session* — écarté : reproduit en navigation privée, sur deux
   environnements différents (local et Streamlit Cloud).
2. *Bug JS dans le fichier du schéma* — écarté : testé via `jsdom` en
   simulant le mécanisme de montage de Streamlit ; aucune erreur
   détectée (ce test ne pouvait pas révéler le vrai problème, qui
   n'est pas une erreur JS mais un contenu qui ne s'affiche pas).
3. *Collision entre scripts de schémas différents partageant la page*
   — écarté : aucun identifiant dupliqué trouvé entre les fichiers de
   schémas des 4 modules construits.
4. *Contenu HTML non à jour côté serveur* — écarté : confirmé à jour à
   plusieurs reprises via des marqueurs de test visibles à l'écran.
5. *Longueur/complexité du schéma* — écarté : des schémas réécrits
   nettement plus courts sont restés tout aussi cassés.
6. *Emplacement de la fiche dans la liste* — écarté par un test
   décisif : le contenu exact d'un schéma fonctionnel (M5.9), placé
   dans l'emplacement de schéma de M5.1, a répondu normalement aux
   clics.

**Cause réelle, identifiée par comparaison différentielle sur un cas
neuf (M15.1, second schéma — comparaison, moteur à pistons vs
turboréacteur) :** ce schéma construisait tout son contenu visuel **au
moment de l'exécution**, via une chaîne HTML assemblée en boucle puis
assignée à `.innerHTML`, générant de nouveaux éléments DOM qui
n'existaient pas dans le HTML statique d'origine. Le schéma voisin qui
fonctionnait (le premier schéma de M15.1, cycle en 4 étapes) avait au
contraire tout son contenu visuel **déjà présent dans le HTML statique**
— le script se contentant de basculer des classes et du texte sur des
éléments déjà existants. Ce même motif est celui que suivait le contenu
fonctionnel de M5.9 utilisé dans le test différentiel du point 6
ci-dessus (bascule de `style.display`/`className`/`textContent` sur des
éléments pré-existants, jamais de génération dynamique de DOM).

**Corrigé** en réécrivant M15.1-2 pour pré-rendre statiquement les deux
vues (piston/turbine), le script ne faisant plus que basculer
`style.display`, `className` et `textContent`. **Confirmé par
l'utilisateur : le second schéma de M15.1 fonctionne.** Le même
correctif a ensuite été appliqué à M5.1 et M5.1-2 (nombre fixe
d'emplacements de bits/groupes pré-rendus, cachés/affichés via
`style.display` plutôt que créés/détruits dynamiquement) ; M5.5 et
M5.5-2 suivaient déjà ce motif sûr sans modification nécessaire.
Règle permanente documentée dans `C:\Users\pc\CLAUDE.md` (section
« Contrainte technique : schémas interactifs Part-66 — jamais de
génération de DOM à l'exécution »).

**Audit des schémas déjà en ligne (M7A, M17A), même motif détecté par
recherche de `innerHTML`/`appendChild`, puis corrigé et testé (jsdom +
retour utilisateur en navigateur) — les 6 fichiers suivants ont tous été
réécrits en contenu pré-rendu statiquement, script limité au basculement
`style.display`/`className`/`textContent` :**
- `part66/data/M7A/schemas/M7A.5.html` (sertissage) — construisait chaque
  bouton de réponse via `appendChild`/`createElement`/
  `createTextNode` dans une boucle, au montage. **Corrigé.**
- `part66/data/M7A/schemas/M7A.6.html` (rivetage) — construisait chaque
  bouton de réponse via `btn.innerHTML = '<div>...</div>' + label`
  dans une boucle, au montage. **Corrigé.**
- `part66/data/M7A/schemas/M7A.10.html` — `flange.appendChild(b)`
  dans `render()`, appelé au montage et à chaque navigation d'étape.
  **Corrigé** (6 positions de boulon pré-calculées par trigonométrie et
  figées en `div` statiques à position fixe).
- `part66/data/M17A/schemas/M17A.4.html` (matériaux/coupe de pale) —
  `coupeStripes.innerHTML=''` puis boucle `appendChild`, dans
  `render(mat)`, appelé au montage (`render('bois')`) et au clic.
  **Corrigé.**
- `part66/data/M17A/schemas/M17A.5-2.html` (nombre de pales) —
  `fan.appendChild(blade)` dans `render(n)`, appelé au montage
  (`render(2)`) et au clic. **Corrigé.**
- `part66/data/M17A/schemas/M17A.6.html` (diagramme de chaîne) —
  `diagram.innerHTML=''` puis boucle `appendChild`, dans `render(fam)`,
  appelé au montage (`render('meca')`) et au clic. **Corrigé** (5
  emplacements de boîte + 4 flèches pré-rendus, affichés selon le
  nombre réel d'éléments de la chaîne).

**Deux vagues de découverte supplémentaires, après ce premier audit —
preuve que l'audit initial (recherche manuelle guidée par le rapport de
relecture) n'était pas exhaustif :**

1. **M15.3, M15.3-2, M15.4-2** — signalés cassés par l'utilisateur lors
   du test en local du lot 1 de M15 (même symptôme : bouton actif
   visuellement, contenu vide en dessous), alors que ces 3 fichiers
   avaient été écrits *avant* que la cause ne soit comprise, dans la
   même session que le lot 1. `M15.3.html` construisait ses 5 marches
   d'escalier via `stairs.innerHTML = html` assemblé en boucle ;
   `M15.3-2.html` construisait ses deux chaînes de boîtes/flèches
   (axial/centrifuge) via `flow.innerHTML = '<div>...</div>' + ...` ;
   `M15.4-2.html` construisait ses 3 visualisations (tubulaire/
   annulaire/tubo-annulaire) via `viz.innerHTML = data[f].viz`, une
   chaîne elle-même assemblée par une fonction `tubes(n,size)` en
   boucle. **Les trois corrigés** : marches, boîtes/flèches et tubes
   tous pré-rendus statiquement, cachés/affichés par `display`.
2. **M5.7.html** (bus série/parallèle) — trouvé par un balayage
   systématique `grep` du motif sur les 4 modules entiers (M5, M7A,
   M15, M17A, 69 fichiers), demandé explicitement par l'utilisateur
   après la découverte du point 1 ci-dessus, pour ne plus dépendre
   d'un audit manuel partiel. `buildTracks()` vidait puis reconstruisait
   1 ou 8 pistes via `createElement`/`appendChild` selon le mode ;
   `send()` créait les bits à envoyer de la même façon (un par un en
   série via une chaîne de `setTimeout`, ou tous en parallèle en une
   boucle). **Corrigé** : 8 pistes et leurs bits pré-rendus
   statiquement (`display:none` par défaut), le mode série réutilise/
   repositionne le bit de la piste 0 en 8 étapes successives, le mode
   parallèle affiche les 8 bits pré-existants simultanément.

**Confirmation finale (2026-09-11)** : après ces deux vagues de
correction, un balayage `grep -rn "innerHTML\s*=\|appendChild\|
createElement\|insertAdjacentHTML\|insertBefore"` sur l'intégralité de
`part66/data/*/schemas/*.html` (69 fichiers, les 4 modules construits)
ne retourne **plus aucune occurrence**. Un test complémentaire (montage
jsdom identique au mécanisme réel de `st.html`, puis clic simulé sur
chaque bouton de chaque fichier) confirme 0 erreur de montage, 0
exception au clic, et 0 fichier sans le moindre changement de DOM après
clic — les 15 fichiers sans `<button>` utilisent tous un `input
type="range"` comme seul contrôle, confirmé interactif. **Ce test jsdom
ne peut cependant pas, par construction, détecter à lui seul ce bug
précis** (il ne l'a jamais détecté sur aucun des fichiers cassés
ci-dessus, y compris a posteriori) : c'est le balayage `grep`, pas le
test jsdom, qui constitue la confirmation faisant autorité qu'aucun
autre schéma du projet ne reproduit ce motif.

## Standard de calibrage du contenu (décidé avec l'utilisateur le
2026-09-11, applicable à partir de M17A)

À partir du module M17A, le calibrage suivant devient le standard du
projet pour tout nouveau module. Il remplace le calibrage plus léger
utilisé pour M10, M5 et M7A (8-10 fiches, 5 questions/fiche, 1 schéma/
fiche, texte de premier jet) :

1. **Découpage plus fin** — 12 fiches minimum par module. Un sous-thème
   trop large se scinde en plusieurs fiches plutôt que d'être condensé
   (ex. principes aérodynamiques séparés des forces subies par la pièce ;
   inspection visuelle séparée de l'équilibrage ; chaque famille de
   mécanisme dans sa propre fiche).
2. **Plus de questions par fiche** — 8 à 10 questions par fiche (au lieu
   de 5). Motif explicite : avec 5 questions/fiche, l'examen blanc
   retire quasiment toujours les mêmes questions, problème déjà identifié
   sur M10.
3. **Deux schémas interactifs minimum par fiche, systématiquement** (un
   pour le principe, un pour l'application concrète, le cas de panne ou
   la comparaison) — révisé le 2026-09-11 après retour utilisateur sur le
   lot 1 de M17A : « quand le sujet le justifie » abandonné, le minimum de
   deux schémas s'applique à toute fiche de tout module construit ou
   complété à partir de cette date. **Contrainte technique impérative,
   découverte le 2026-09-11 lors de ce même retour utilisateur : aucun
   schéma ne doit utiliser de balise `<svg>`** — voir la note dans
   `C:\Users\pc\CLAUDE.md` (« Contrainte technique : schémas interactifs
   Part-66 — jamais de `<svg>` ») pour le détail technique (DOMPurify,
   configuré par `st.html` avec `USE_PROFILES: {html:true}`, supprime
   silencieusement tout `<svg>` au rendu, y compris avec
   `unsafe_allow_javascript=True`) et les techniques de remplacement
   (barres, aiguilles en `div` tournées par `transform: rotate()`,
   cadrans circulaires).
4. **Texte substantiellement développé dès la première version** — viser
   le niveau des versions enrichies de M5.1/M5.4/M5.9 (6000+ caractères
   par fiche) dès la rédaction initiale, pas au terme d'un round
   d'enrichissement séparé.
5. **Vulgarisation systématique** — chaque terme technique ou sigle est
   expliqué en mots simples à sa première apparition, avec une analogie
   concrète quand c'est possible. Rédaction pour un débutant complet
   découvrant l'aéronautique, pas pour un technicien confirmé qui
   réviserait.

**Application rétroactive à M10, M5 et M7A** : décidée en principe, mais
**différée** à un chantier ultérieur, après la construction de M17A. Ne
pas la traiter avant que M17A ne soit terminé, relu et validé.

## Méthode

Avant tout commit d'un nouveau lot de questions, faire relire le lot par
le sous-agent `relecteur-part66` (voir `.claude/agents/relecteur-part66.md`).

Pour un module **réglementaire** (comme M10), toute affirmation qui cite un
texte de loi doit renvoyer à une référence précise et vérifiable ; une
source manquante ou approximative sur ce type d'affirmation doit être
classée BLOQUANT par le relecteur, qu'elle soit déjà listée dans ce fichier
ou non.

Pour un module **technique** (comme M5), une source générique du type
« Notions générales d'électronique numérique — [sujet] » est acceptable et
n'est pas un motif de blocage en soi : ce qui doit être vérifié dans ce cas
est l'**exactitude technique** de l'affirmation elle-même, pas la présence
d'un texte à citer. Seuls les points les plus spécifiquement avioniques
(protocoles, guidance AESA...) appellent une source précise ; documente-les
en TODO comme le reste de ce fichier plutôt que de les bloquer par défaut,
sauf doute réel sur le fond.
