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
  qualité ») — La terminologie « système de gestion de la qualité » de
  l'organisme Part-145 pourrait être périmée : un règlement modificatif du
  Part-145 applicable fin 2022 aurait remplacé le « quality system » par un
  « management system ». Ni confirmé ni infirmé. À vérifier dans le texte
  consolidé avant de garder cette formulation, et à corriger question et
  fiche ensemble si confirmé.

- **M10-0029** (et la fiche **M10.6**, même formulation) — L'option/le
  texte disent que la catégorie C du Part-66 est « réservée » à des
  titulaires expérimentés d'une licence B1 ou B2. La relecture signale
  qu'une voie académique alternative (diplôme + expérience en environnement
  de maintenance civile) pourrait exister pour l'accès à la catégorie C
  sans passer par B1/B2, ce qui rendrait « réservée » trop absolu. Non
  vérifié — à confirmer dans 66.A.30 avant de corriger la question et la
  fiche ensemble.

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
