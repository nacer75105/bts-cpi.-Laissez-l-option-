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
