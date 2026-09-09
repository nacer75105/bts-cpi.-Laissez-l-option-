# Points à vérifier avant de considérer le contenu M10 comme définitif

Ce fichier liste les points où une source réglementaire précise n'a pas pu
être confirmée avec certitude au moment de la rédaction. Le principe
général reste solide (structure OACI/AESA, Part-M/145/66/147, catégories
Part-66, documents de bord, consignes de navigabilité) mais la référence
exacte (article, annexe précise) doit être confirmée avant un usage en
conditions d'examen réel.

## Questions concernées

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

## Point de configuration à confirmer (hors banque de questions)

- **Nombre de questions et durée de l'examen officiel du module M10** pour
  la licence B1.1 : la valeur utilisée par défaut dans `part66/logic.py`
  (32 questions / 40 minutes) est une valeur couramment citée mais non
  vérifiée sur une source officielle à jour (Appendix VIII du Part-66). À
  confirmer avant de s'appuyer sur l'examen blanc pour évaluer une réelle
  préparation à l'épreuve.

## Intitulés des modules non encore traités

Les intitulés de M5, M7A, M11A, M15 et M17A utilisés comme simples
libellés d'affichage (module « à venir ») dans `part66/logic.py`
viennent de la connaissance générale du référentiel Part-66 et doivent
être confirmés contre le syllabus officiel avant que ces modules ne
soient réellement construits (fiches + questions) :

- M5 : « Techniques numériques / systèmes d'instruments électroniques »
- M7A : « Pratiques de maintenance »
- M11A : « Aérodynamique, structures et systèmes — avion à turbine »
- M15 : « Turbomachines à gaz »
- M17A : « Hélices »

## Méthode

Avant tout commit d'un nouveau lot de questions, faire relire le lot par
le sous-agent `relecteur-part66` (voir `.claude/agents/relecteur-part66.md`).
Toute question sans source vérifiable doit être classée BLOQUANT par ce
relecteur, qu'elle soit listée ici ou non.
