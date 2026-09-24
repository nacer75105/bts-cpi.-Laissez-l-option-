# À vérifier — Mathématiques BTS CPI (app.py, blocs 7, 17, 18, 19)

Chantier de relecture lancé le 2026-09-24 : pour chaque bloc évalué, fiche par fiche,
`relecteur-bts-maths` (justesse, calculs refaits en Python) et `prof-pedagogue` (clarté).
Les erreurs BLOQUANTES et les points de clarté importants sont corrigés dans `app.py` ;
ce fichier garde ce qui reste à faire ou à trancher. (Le suivi Part-66 est dans
`part66/A_VERIFIER.md`.)

Périmètre de l'examen : S10 du référentiel BTS CPI 2016 (voir
`.claude/referentiels/bts-cpi-maths/`). 9 modules évalués ; calcul matriciel et modélisation
géométrique = programme complémentaire non évalué.

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
  - Probabilités 1 : loi uniforme, loi normale comme loi de probabilité (au-delà de la règle
    des 3σ), approximation d'une binomiale par une loi normale, théorème de la limite centrée ;
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

- **Contenus évalués ABSENTS** : fonctions ln et exp (limites, dérivées de ln u et eᵘ, étude
  complète) et statistique à deux variables (nuage de points, ajustement affine par moindres
  carrés, coefficient de corrélation) — aucune fiche ne les traite. Le résumé du bloc 17 le dit
  désormais. Les primitives de 1/x, eˣ, u'/u, u'eᵘ ont été ajoutées au tableau de 17.2.
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
