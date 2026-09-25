# À vérifier — Mathématiques BTS CPI (app.py, blocs 7, 17, 18, 19)

Chantier de relecture lancé le 2026-09-24 : pour chaque bloc évalué, fiche par fiche,
`relecteur-bts-maths` (justesse, calculs refaits en Python) et `prof-pedagogue` (clarté).
Les erreurs BLOQUANTES et les points de clarté importants sont corrigés dans `app.py` ;
ce fichier garde ce qui reste à faire ou à trancher. (Le suivi Part-66 est dans
`part66/A_VERIFIER.md`.)

Périmètre de l'examen : S10 du référentiel BTS CPI 2016 (voir
`.claude/referentiels/bts-cpi-maths/`). 9 modules évalués ; calcul matriciel et modélisation
géométrique = programme complémentaire non évalué.

## Chantier « notions manquantes » (lancé le 2026-09-25)

Une fiche à la fois, dans l'ordre du programme, chacune relue par les deux agents jusqu'à
zéro réserve avant insertion. Numérotation : nouveaux id à la suite (17.7, 17.8, 18.9 →
18.19), jamais de renumérotation — la progression est indexée par `"{bloc}#{id}"`
(fiches lues, notes, réponses) et la navigation retrouve les fiches par id, pas par
position ; une fiche peut donc être placée n'importe où dans la liste de son bloc. Bloc 18
laissé d'un seul tenant (pas de scission) pour ne pas toucher les clés.

Plan (le référentiel ne répartit pas les modules entre 1ʳᵉ et 2ᵉ année ; l'ordre suit les
prérequis et la répartition usuelle) :
1. ✅ 17.7 ln et exp — 2. ✅ 17.8 statistique à deux variables — 3. ✅ 18.9 loi uniforme —
4. ✅ 18.10 loi normale et approximation binomiale — 5. ✅ 18.11 somme de variables, limite centrée —
6. méthode d'Euler — 7. IC d'une proportion — 8. tests sur une proportion / une moyenne —
9. tests de comparaison — 10. loi exponentielle — 11. loi de Poisson — 12. nombres
complexes (forme algébrique, Δ < 0) — 13. équations différentielles du second ordre.

### 17.7 — Fonctions exponentielle et logarithme népérien (faite le 2026-09-25)

- Insérée après 17.1 (ordre affiché 17.0 → 17.1 → 17.7 → 17.2), avec méthode, figure
  `exp_ln_courbes`, atelier at139, générateur `gen_temps_decharge`, 8 questions dans
  « Mathématiques BTS CPI (examen) » (bonne réponse en positions 2, 0, 3, 1, 2, 0, 3, 1).
- Quatre tours de relecture (justesse + clarté) jusqu'à zéro réserve. Corrections de fond :
  la règle du produit (uv)' = u'v + uv' n'était enseignée NULLE PART dans l'application
  (7.2 renvoyait à 17.1, qui ne traite que le quotient) — elle est maintenant dans 17.7 §5,
  et le renvoi de 7.2 pointe vers 17.1 (quotients) et 17.7 (produits, ln, exp) ; le
  refroidissement est écrit sur l'écart T − T_amb, comme en 18.4.
- Mis à jour en même temps : résumé du bloc 17, tableau de bord (Analyse : ln et exp
  retirés des « non traités », 17.7 ajoutée), encart de la page Maths.
- **Non vérifié** : textes réglementaires cités de mémoire par le relecteur (NF EN 60204-1
  § 6.2.4 : 60 V en 5 s ; Code du travail R4431-2 et R4434-7 : 85 dB(A)) ; rendu visuel réel
  de la figure (coordonnées et chevauchements contrôlés par calcul uniquement) ; le corrigé
  progressif et l'atelier at139 n'ont pas été cliqués dans l'interface (la fiche s'ouvre sans
  erreur dans un AppTest Streamlit).

### 17.8 — Statistique à deux variables : ajustement affine et corrélation (faite le 2026-09-25)

- Insérée en fin de bloc 17 (ordre affiché … 17.6 → 17.8 → 18.1), avec méthode, figures
  `nuage_moindres_carres` et `linearisation_ln`, atelier at140 (étalonnage d'un capteur),
  générateur `gen_pente_moindres_carres`, 8 questions dans « Mathématiques BTS CPI (examen) »
  (bonne réponse en positions 1, 3, 0, 2, 3, 1, 0, 2).
- Quatre tours de relecture (justesse + clarté) jusqu'à zéro réserve. Points de fond :
  règle unique pour juger un modèle (écarts sans motif PUIS |r| proche de 1), appliquée à
  chaque exemple ; réflexe « corrélation n'est pas causalité » en trois questions (quel
  mécanisme ? qui d'autre ? quel essai ?) ; pont avec la 17.7 (multiplier par 0,6 = ajouter
  ln 0,6 ≈ −0,51 → pas constant → droite). Les premières données du refroidissement
  (exercice partie B) avaient des écarts en U, en contradiction avec la règle de la fiche :
  remplacées par D = 160 ; 98 ; 59 ; 37 ; 22 (écarts de signes alternés).
- Choix de l'auteur : « liaison » gardé (terme du référentiel), glosé « liaison statistique » ;
  calcul à la main de cov et a gardé, marqué « entraînement, à l'examen la calculatrice ».
- Mis à jour en même temps : résumé du bloc 17 (plus rien « à couvrir »), tableau de bord
  (Statistiques : 17.8 ajoutée, statistique à deux variables retirée des non traités), encart
  de la page Maths.
- **Non vérifié** : rendu visuel réel des deux figures (chevauchements estimés avec les
  métriques Segoe UI par le relecteur) ; corrigé progressif, atelier at140 et générateur non
  cliqués dans l'interface (la fiche s'ouvre sans erreur dans un AppTest Streamlit).

### Ateliers — tolérance absolue (corrigé le 2026-09-25, commit 34e7003)

- Le contrôleur des ateliers lisait `tol` en relatif (|valeur − attendu| ≤ |attendu| × tol),
  alors que les ateliers sont écrits en absolu : 42 pièges sur 194 étapes étaient comptés justes
  et 65 tolérances dépassaient ±10 %. Contrôleur passé en absolu ; `EXERCICES_GUIDES` (écrits
  en relatif, 2 %) inchangés. Corrigés en même temps : at30, at26 (saisie à 6 décimales), at58.
- **Audit à relancer après toute création ou modification d'atelier** :
  `python outils/verifier_tolerances_ateliers.py` (code de sortie = nombre de défauts ; il cherche
  les pièges dans la tolérance, les réponses impossibles à saisir avec le format de l'étape, les
  tolérances > 10 % non déclarées voulues, et tol = 0 sur une valeur non entière). Dernier
  passage (fiche 18.9 incluse) : 196 étapes, 140 ateliers, 0 défaut. Les tolérances de 5 à 10 %
  qu'il liste ont été vérifiées une à une (entiers à ±0,1, at84 = fourchette du cours).
- Règle pour les nouveaux ateliers : `tol` est une tolérance ABSOLUE dans l'unité de l'étape, et
  les valeurs données par l'indice (arrondis intermédiaires) doivent être acceptées.

### 18.11 — Somme de variables et théorème de la limite centrée (faite le 2026-09-25)

- Insérée après 18.10 (ordre affiché … 18.9 → 18.10 → 18.11 → 18.7), avec méthode, figures
  `quadrature_cotes` et `moyenne_se_resserre`, atelier at143 (chaîne de cotes, étapes 2 et 3
  déclarées avec `depend_de`), générateurs `gen_sigma_somme` et `gen_sigma_affine`, 8 questions
  dans la banque « probabilités et équations différentielles » (bonne réponse en positions 3, 1,
  0, 2, 1, 3, 2, 0). L'encadré de la 18.10 renvoie désormais à la 18.11 (« les vérifie »).
- Trois tours de relecture (justesse + clarté) jusqu'à zéro réserve. Choix de l'auteur, conforme
  au référentiel (« conjecturés par simulation, puis admis ») : la fiche VÉRIFIE les règles
  (énumération exacte des 36 cas de deux dés) et en donne le POURQUOI — (x + y)² = x² + y² + 2xy,
  2xy nul en moyenne pour des variables indépendantes, maximal (V = (σx + σy)², pire cas) si
  elles se trompent ensemble ; quadrature expliquée par Pythagore — sans démonstration générale.
- Cas industriel : la chaîne de cotes de l'exercice guidé eg6 au pire cas (±0,15 mm) et en
  tolérancement statistique (±0,087 mm) ; le gain de 73 % sur l'IT des pièces a un prix (0,27 %
  des assemblages hors plage) ; coefficient de sécurité 1,5 (méthode dite de Bender) chiffré.
- Relecture : étymologie de « limite centrée » corrigée (Pólya, 1920, « central » au sens de
  « fondamental ») ; la page Entraînement et l'outil d'audit ont été renforcés en amont (commit
  f59acad) après que l'audit eut laissé passer deux défauts de cette fiche (diagnostics
  confondus, arrondis enchaînés).
- **Non vérifié** : rendu visuel réel des deux figures ; atelier at143 et générateurs non cliqués
  dans l'interface (la fiche et la page Entraînement s'ouvrent sans erreur dans un AppTest ;
  outil d'audit : 0 défaut sur 202 étapes et 20 générateurs).

### Diagnostics masqués et arrondis enchaînés (corrigé le 2026-09-25)

- Pièges d'atelier : la page prenait le PREMIER piège dont la fenêtre de ±2 % contenait la saisie ;
  sur des cotes (at1, at2, at3), l'élève qui tapait 45 recevait le message du piège 45,025. Elle
  prend désormais le PLUS PROCHE (`diagnostic_le_plus_proche`), comme la page Entraînement.
- Générateurs : deux diagnostics de même valeur (7 générateurs, jusqu'à 61 % des tirages de
  gen_iso_jeu) — le second était jeté. `fusionner_diagnostics` réunit désormais leurs messages.
- L'outil d'audit contrôle aussi : pièges et diagnostics MASQUÉS (en rejouant la logique de la
  page), et arrondis enchaînés d'une étape à l'autre (clé facultative `depend_de` sur une étape
  d'atelier : `{"etape": k, "formule": lambda v: ...}`), à déclarer sur toute étape qui réutilise
  un résultat intermédiaire. Contrôles validés en réintroduisant chaque défaut sur une copie.

### 18.10 — Loi normale et approximation d'une loi binomiale (faite le 2026-09-25)

- Insérée après 18.9 (ordre affiché … 18.6 → 18.9 → 18.10 → 18.7), avec méthode, figures
  `somme_uniformes_cloche`, `aire_sous_cloche`, `binomiale_continuite`, atelier at142 (poste de
  reprise, tolérances absolues, valeurs écrites avec `math` seulement pour l'outil d'audit),
  aide `_phi` et générateurs `gen_borne_continuite`, `gen_proba_normale`, 9 questions dans la
  banque « probabilités et équations différentielles » (bonne réponse en positions 1, 2, 0, 3, 2,
  0, 3, 1, 0).
- Trois tours de relecture (justesse + clarté) jusqu'à zéro réserve. Points de fond : même idée
  « probabilité = aire » qu'en 18.9, sur une cloche ; la règle 68 / 95 / 99,7 % de la 7.3 relue
  comme trois aires, sans la réintroduire ; correction de continuité par un tableau à six lignes
  avec les mots de l'énoncé (« moins de » / « plus de » excluent la borne) ; binomiale en cloche
  expliquée par le contrôleur qui écrit 1 ou 0 (X = somme de 100 contributions).
- Choix de l'auteur : la simulation par 12 ALEA() est en encadré « Pour aller plus loin »,
  facultatif, avec les règles d'addition des espérances et des variances ADMISES (la fiche 5 du
  chantier les montrera) et le piège 12 × 0,29 désamorcé ; le chiffrage en euros du cas
  industriel est présenté comme une hypothèse (12 € l'arbre).
- Le relecteur a relevé que la TI française appelle la fonction normalFRép (normalcdf en
  anglais) : la fiche donne les deux.
- **Non vérifié** : rendu visuel réel des trois figures ; ordre de saisie exact sur NumWorks ;
  atelier at142 et générateurs non cliqués dans l'interface (la fiche et la page Entraînement
  s'ouvrent sans erreur dans un AppTest ; l'outil d'audit : 0 défaut sur 199 étapes et
  18 générateurs).

### Entraînement — réponse affichée et saisie (corrigé le 2026-09-25)

- La réponse affichée après deux essais avait toujours 2 décimales : refusée par sa propre
  tolérance dans 66 % des tirages de gen_proba_binomiale et 21 % de gen_proba_uniforme.
  Affichage désormais au nombre de décimales qu'impose la tolérance (`decimales_affichage`).
- `lire_nombre` lisait un nombre contenant « 10 » comme une puissance de 10 (« 5100 » → 5,
  « 0,0106 » → 0) : 1 890 entiers de 0 à 99 999 mal lus. Le signe × est désormais obligatoire
  dans l'écriture 6,02x10^23.
- Diagnostics égaux à la bonne réponse (retirés en silence par fabriquer_exo) : `tirer_exercice`
  refait le tirage ; gen_proba_binomiale ne propose plus un diagnostic égal à la réponse (les
  exercices à p = 0,5 sont conservés).
- L'outil `outils/verifier_tolerances_ateliers.py` contrôle aussi les 16 générateurs (réponse
  affichée acceptée, aucun diagnostic dans la tolérance, pas de plantage) et la lecture de 120 000
  nombres. Dernier passage : 0 défaut.

### 18.9 — Loi uniforme, première loi à densité (faite le 2026-09-25)

- Insérée après 18.6 (ordre affiché … 18.6 → 18.9 → 18.7), avec méthode, figures
  `histogramme_vers_densite` et `aire_uniforme`, atelier at141 (inclusion sur une barre, en
  tolérances absolues), générateur `gen_proba_uniforme`, 8 questions dans la banque
  « probabilités et équations différentielles » (bonne réponse en positions 2, 0, 3, 1, 1, 3, 0, 2).
- Trois tours de relecture (justesse + clarté) jusqu'à zéro réserve. Points de fond :
  « probabilité = aire » démontré par un tableau des mêmes 1 000 attentes en classes de
  2 / 1 / 0,5 / 0,1 min (la fréquence change, la hauteur fréquence ÷ largeur reste 0,10) ;
  masse linéique pour « la densité n'est pas une probabilité » ; E(X) par le rectangle en
  équilibre et la valeur moyenne de 17.5 ; cas industriel sur l'incertitude de résolution
  q/√12 (règle « de l'ordre d'un dixième de la tolérance, règle courante en contrôle »).
  Erreurs rattrapées : moyenne simulée 5,78 incompatible avec la fiche 18.3 (→ 5,90) ; renvois
  vers des fiches inexistantes ; tolérance de l'étape σ de l'atelier refusant la valeur de
  l'indice (3 000/3,46).
- Mis à jour : résumé du bloc 18, tableau de bord (loi uniforme retirée des non traités,
  18.9 ajoutée).
- **Non vérifié** : rendu visuel réel des deux figures ; corrigé progressif, atelier at141 et
  générateur non cliqués dans l'interface (la fiche s'ouvre sans erreur dans un AppTest).

## Bloc 19 — marquage hors épreuve (fait)

- 19.1–19.4 (matrices, Bézier) : programme complémentaire, marquées « hors épreuve ».
- 19.5 (produit scalaire et vectoriel) : **évaluée** (module Calcul vectoriel).
- 19.6 (droites, plans, distance point-plan) : hors référentiel, marquée « hors épreuve ».
- Reste : la catégorie de quiz « Mathématiques BTS CPI — calcul matriciel et modélisation
  géométrique » n'est pas marquée hors épreuve (la renommer risquerait de casser la
  progression enregistrée, qui utilise le nom de catégorie comme clé). À faire par un libellé
  d'affichage séparé si besoin.

## Bloc 7 — reste à faire

- **Non vérifié** : le rendu visuel réel des figures (seuls les textes et nombres affichés ont
  été contrôlés) ; la valeur réglementaire « rampe PMR limitée à 5 % » (7.1, cours §2), non
  vérifiable par calcul.
- **T = dMf/dx** : la fiche 7.2 dit maintenant « au signe près ». La même identité apparaît
  hors du bloc maths (fiches RDM) : à harmoniser avec la convention de signe de la fiche 4.3.
- **7.1 / corrigé Q5 (retrait)** : 240 × 1,01 = 242,4 suppose le retrait rapporté à la cote
  finale ; rapporté à la cote du modèle, on aurait 240 / 0,99 = 242,42. Écart < 0,1 mm,
  convention à préciser si le cours de fonderie (fiche 12.3) en retient une.
- **Quiz d'examen, valeur moyenne d'une température** : l'ambiguïté (deux bonnes réponses) est
  levée en précisant le profil. L'option « Impossible à calculer sans plus d'informations »
  reste défendable au sens strict (la valeur exacte demande la fonction) ; à reformuler si un
  élève conteste.
- **Onglet Méthode 7.1** : cite toujours Al-Kashi ; il est désormais présenté dans le cours
  (§5), rien à faire sauf relecture.

## Bloc 18 — reste à faire

- **Contenus évalués ABSENTS de l'application** (décision de l'auteur : créer des fiches ?).
  Le S10 2016 et l'annexe I rendent évalués, sans qu'aucune fiche ne les traite :
  - Probabilités 1 : entièrement traité depuis le 2026-09-25 (18.9 loi uniforme, 18.10 loi
    normale et approximation binomiale, 18.11 aX + b, X ± Y et limite centrée) ;
  - Probabilités 2 : loi exponentielle, loi de Poisson, approximation binomiale → Poisson ;
  - Statistique inférentielle : intervalle de confiance d'une proportion, tests d'hypothèse
    (bilatéraux, unilatéraux, comparaison de deux moyennes ou proportions) ;
  - Équations différentielles : second ordre à coefficients constants, méthode d'Euler.
  Le résumé du bloc 18, l'encart de la page Maths et le tableau de bord
  (`MATIERES_PROGRAMME`, statut « Incomplet (à enrichir) ») le disent désormais.
- **Quiz** : aucune question des banques « Mathématiques BTS CPI (examen) » et « Mathématiques
  appliquées » ne porte sur le bloc 18 (seule la banque « probabilités et équations
  différentielles » le couvre).
- **Non vérifié** : fin de l'atelier at30 (champs `verification` et `a_retenir`) ; rendu
  visuel des figures (arbre, Venn, exponentielle, intervalle de confiance) — seuls leurs textes
  ont été corrigés.
- **Notation** : T_amb / T_eq / y_eq / P_eq coexistent encore entre cours, méthodes et
  ateliers at22/at30 ; les formules générales disent maintenant « y_eq = valeur d'équilibre,
  par ex. T_amb ». Harmonisation complète à faire.
- **18.2** : le nom exact des menus de loi binomiale dépend de la calculatrice (Casio / TI /
  NumWorks) ; la fiche reste générique.

## Bloc 17 — reste à faire

- **Contenus évalués** : tous traités depuis le 2026-09-25 — fonctions ln et exp (fiche 17.7),
  statistique à deux variables (fiche 17.8). Les primitives de 1/x, eˣ, u'/u, u'eᵘ ont été
  ajoutées au tableau de 17.2.
- **Générateurs** (justes sur 300 tirages, mais à polir) :
  - `gen_discriminant` : affichage « 1x² + (-8)x + (-8) » et « (0)x » ; quand a·c = 0, les deux
    diagnostics sont filtrés et l'exercice n'en a plus. Formater les coefficients, exclure c = 0.
  - `gen_signe_affine` : mélange de tirets ASCII « - » et de « − ».
  - `gen_valeur_moyenne` : ne tire que des fonctions affines, alors que la fiche 17.5 montre que
    (f(a)+f(b))/2 suffit dans ce cas ; tirer aussi des trinômes.
- **Figures** : l'atelier at46 (tableau de signes) affiche la figure d'un tableau de variations ;
  la fiche 17.3 n'a plus de figure (l'ancienne, une courbe de capabilité, a été remplacée par un
  diagramme en boîte en texte) ; 17.2 et 17.5 n'affichent plus la figure « profil
  trapézoïdal », qui ne correspondait pas au texte. Des figures dédiées (aire sous 6x − x²,
  rectangle de même aire, boîte à moustaches) seraient un plus.
- **Non vérifié** : rendu visuel réel des figures (seules les coordonnées ont été contrôlées, et
  les fonctions exécutées) ; appartenance du BTS CPI à un « groupement C1 » (mention retirée,
  aucune source dans le dépôt).
