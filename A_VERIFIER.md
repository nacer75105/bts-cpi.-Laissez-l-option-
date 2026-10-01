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
6. ✅ 18.12 méthode d'Euler — 7. ✅ 18.13 IC d'une proportion — 8. ✅ 18.14 tests sur une proportion / une moyenne —
9. ✅ 18.15 tests de comparaison — 10. ✅ 18.16 loi exponentielle — 11. ✅ 18.17 loi de Poisson — 12. ✅ 18.18 nombres
complexes (forme algébrique, Δ < 0) — 13. ✅ 18.19 équations différentielles du second ordre. **Plan terminé (13/13).**

Plan complémentaire « Analyse » (validé le 2026-09-28, pour les notions du référentiel que le plan des 13 ne
couvrait pas ; ordre d'écriture) : 1. ✅ 17.9 trigonométrie (courbes, dérivées et primitives de sin et cos) —
2. ✅ 17.12 calcul intégral (Chasles, linéarité, positivité, aire entre deux courbes ; méthodes approchées en
« pour aller plus loin ») — 3. ✅ 17.10 étude de fonction (racine carrée, dérivée de uⁿ, asymptote oblique) —
4. ✅ 17.11 équation f(x) = k (nombre de solutions, dichotomie). **Plan complémentaire terminé (4/4)** : ligne « Analyse » du
tableau de bord à « Complet », avertissement de la page Maths retiré. Aucun item évalué des modules
Fonctions, Calcul intégral et Équations différentielles ne reste sans fiche (bilan de la section 17.11).

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
- ✅ Interface vérifiée dans un vrai navigateur le 2026-09-27 : atelier at139 (pièges, bonnes valeurs, QCM, corrigé), gen_temps_decharge, figures exp_ln_courbes regardées dans l'app (voir « Dette d'interface 17.7 à 18.13 »).

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
- ✅ Interface vérifiée dans un vrai navigateur le 2026-09-27 : atelier at140 (pièges, bonnes valeurs, QCM, corrigé), gen_pente_moindres_carres, figures nuage_moindres_carres, linearisation_ln regardées dans l'app (voir « Dette d'interface 17.7 à 18.13 »).

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
- ✅ Interface vérifiée dans un vrai navigateur le 2026-09-27 : atelier at143 (pièges, bonnes valeurs, QCM, corrigé), gen_sigma_somme, gen_sigma_affine, figures quadrature_cotes, moyenne_se_resserre regardées dans l'app (voir « Dette d'interface 17.7 à 18.13 »).

### 18.12 — Méthode d'Euler (faite le 2026-09-25)

- Niveau vérifié dans l'annexe I (module Équations différentielles, commentaire) : « On présente
  sur un exemple la résolution approchée d'une équation différentielle par la méthode d'Euler » —
  pas une capacité exigible autonome. La fiche (2 h) présente la méthode sur la pièce de la 18.4
  et sur la charge d'un condensateur, sans théorie de l'erreur ; la section tableur couvre aussi la
  capacité « représenter à l'aide d'un logiciel la famille des courbes ».
- Placée en fin de bloc 18 (après 18.8), avec méthode, figures `euler_tangentes`, `euler_pas_h` et
  `euler_charge` (dédiée à l'atelier), atelier at144 (charge d'un condensateur, étapes 2 et 3
  déclarées avec `depend_de`), générateurs `gen_euler_pas` et `gen_euler_ecart`, 8 questions dans
  la banque « probabilités et équations différentielles » (bonne réponse en positions 1, 3, 0, 2,
  3, 0, 2, 1). Renvois ajoutés dans le « À retenir » des fiches 18.4 et 18.8 ; tableau de bord :
  la méthode d'Euler n'est plus dans les « non traités ».
- Quatre tours de relecture (justesse + clarté) jusqu'à zéro réserve. Points clés arbitrés par
  l'auteur : idée « la dérivée est une pente, on suit la tangente sur un pas h » ; après un pas, on
  n'est PLUS sur la courbe exacte, la pente est prise où l'on est et les erreurs s'accumulent (8 °C
  après 1 pas, 11,5 °C après 3) ; règle unique « Euler va trop vite vers l'équilibre »
  (1 − h/τ < e^(−h/τ)), avec la nuance h > τ (il dépasse l'équilibre, −33 °C) ; « pas ÷ 2 → écart
  ÷ 2 » illustré par de vrais facteurs 2 ; lien avec l'exponentielle en « pour aller plus loin » ;
  ancrage : logiciels de simulation, relais temporisé vérifié (h = 0,25 s donne une conclusion
  fausse, h = 0,1 s confirme ln 3 ≈ 1,10 s), atelier qui se réchauffe (34 °C au lieu des 28 °C
  crus). Newton et la dichotomie ne sont cités qu'au conditionnel (aucune fiche ne les traite).
- **Non vérifié** : atelier at144 et générateurs non cliqués dans l'interface (la fiche et la page
  Entraînement s'ouvrent sans erreur dans un AppTest ; outil d'audit : 0 défaut). La date 1768
  (Institutionum calculi integralis) et « Euler a choisi la lettre e » sont des connaissances, non
  recoupées par une source.
- ✅ Interface vérifiée dans un vrai navigateur le 2026-09-27 : atelier at144 (pièges, bonnes valeurs, QCM, corrigé), gen_euler_pas, gen_euler_ecart, figures euler_tangentes, euler_pas_h regardées dans l'app (voir « Dette d'interface 17.7 à 18.13 »).

### 18.13 — Intervalle de confiance d'une proportion (faite le 2026-09-25)

- Référentiel (annexe I, Statistique inférentielle) : IC d'une proportion (binomiale approximable
  par une normale), exploitation, taille d'échantillon pour une précision donnée ; commentaire
  « On distingue confiance et probabilité » (avant le tirage : probabilité 0,95 de la procédure ;
  après : confiance de 95 %) et « la simulation permet de mieux comprendre ».
- Placée après 18.7 (ordre affiché … 18.11 → 18.7 → 18.13 → 18.8 → 18.12), avec méthode, figures
  `proportion_en_cloche` et `ic_proportion_simulation` (40 intervalles simulés, graine fixe, 2
  manquent p), atelier at145 (réception d'un lot de joints, étapes 2 à 4 avec `depend_de`),
  générateurs `gen_ic_proportion` et `gen_taille_proportion`, 8 questions dans la banque
  « probabilités et équations différentielles » (bonne réponse en positions 2, 0, 3, 1, 0, 2, 1, 3).
- Retouches ailleurs : fiche 18.3 — « une fourchette qui a de fortes chances de contenir la vraie
  moyenne » (qui contredisait la 18.13) devient « calculée par une méthode qui réussit 95 fois sur
  100 à encadrer la vraie moyenne », avec renvoi, et nouvelle erreur classique 4 (« 95 % de
  chances ») ; fiche 18.7 — renvoi vers la 18.13 pour une proportion ; tableau de bord.
- Quatre tours de relecture (justesse + clarté) jusqu'à zéro réserve. Points clés arbitrés par
  l'auteur : POURQUOI la méthode réussit environ 95 fois sur 100 (f à moins de 0,035 de p ⇔ p à
  moins de 0,035 de f) ; F majuscule (avant le tirage, aléatoire) / f minuscule (mesuré) qui
  incarne probabilité / confiance ; la vraie erreur de formule est √(f(1 − f))/n (et non
  √(f(1 − f))/√n, qui est juste) ; contresens « un nouvel échantillon tombera dans l'intervalle
  avec 95 % de chances » (≈ 83 %, variances additionnées, fiche 18.11) ; formule avec n, variante
  n − 1 signalée (c'est le s/√n de la 18.3) ; couverture réelle ≈ 93 % (calcul exact binomial)
  en « pour aller plus loin ».
- **Non vérifié** : usage de n ou n − 1 dans les annales du BTS CPI (non consultées) ; atelier
  at145 et générateurs non cliqués dans l'interface (la fiche s'ouvre sans erreur dans un
  AppTest ; outil d'audit : 0 défaut).
- ✅ Interface vérifiée dans un vrai navigateur le 2026-09-27 : atelier at145 (pièges, bonnes valeurs, QCM, corrigé), gen_ic_proportion, gen_taille_proportion, figures proportion_en_cloche, ic_proportion_simulation regardées dans l'app (voir « Dette d'interface 17.7 à 18.13 »).

### Figures à curseurs dans les fiches : pilote sur la 17.9 (2026-09-29) — À JUGER EN LIGNE

- Mécanisme : repère [[DYN:cle]] dans un texte de fiche, registre DYNAMIQUES (titre, fonction, curseurs),
  affichage par afficher_dynamique() : un st.slider (ou st.select_slider) par paramètre, puis la figure
  redessinée en SVG par la fonction Python, comme sur la page « Schémas interactifs ». La fonction a des
  valeurs par défaut ; l'audit (contrôle FIGURE) l'exécute avec ces valeurs puis à chaque combinaison des
  positions extrêmes des curseurs, et vérifie que chaque repère [[FIG:…]] / [[DYN:…]] désigne une figure.
- Pilote unique : `sinusoide_curseurs` (fiche 17.9, § 3, après la figure des trois réglages) :
  y = A cos(ωt + φ), curseurs A (0,5 à 3), ω (0,5 à 4 rad/s), φ (−π à π par pas de π/4) ; cos t en gris
  pour référence ; période, fréquence, maximum le plus proche de 0 (t₀ = −φ/ω) affichés.
- Réactivité mesurée en local : figure redessinée 0,3 s environ après chaque pas de curseur. **À juger sur
  l'application en ligne (Render, serveur gratuit, plus lent) avant d'en faire d'autres** : une figure qui
  rame au curseur serait pire que pas de figure. Candidates si le pilote convient : droite y = k (17.11),
  bornes de l'aire (17.12), écart à l'asymptote (17.10), loi normale μ/σ (18.10), amortissement (18.19).
- Réactivité jugée en ligne (Render gratuit) : environ 1 s par cran. Décision de l'auteur : garder la
  sinusoïde, n'ajouter que des figures « par crans » où l'on s'arrête pour lire (pas de balayage continu).
  Deuxième figure : `droite_k_curseur` (17.11), la droite y = k déplacée par crans de 0,5 de −4 à 5 sur
  x³ − 3x² + 2, nombre de solutions et décompte par intervalle + extremums (0,68 s par cran en local, page
  plus lourde que la 17.9). Écartée pour l'instant : l'amortissement de la 18.19 (son intérêt est le
  balayage continu), gardé en figures statiques. À voir : aire (17.12), loi normale (18.10).
- Trouvé en testant le pilote, corrigé à part (commit fix) : sur la page Cours, les listes Bloc et Fiche
  n'avaient pas de clé ; après un saut « Aller directement à une fiche », la moindre interaction sur la
  fiche (curseur, bouton « Enregistrer la note ») ramenait à la première fiche du premier bloc.

### 17.11 — Équation f(x) = k : nombre de solutions et dichotomie (faite le 2026-09-29)

- Référentiel (annexe I, Fonctions) : « exploiter le tableau de variation pour obtenir le nombre de solutions
  d'une équation f(x) = k » et « mettre en œuvre un procédé de recherche d'une valeur approchée d'une racine »
  (le commentaire cite balayage, dichotomie, Newton et demande au moins un algorithme : dichotomie en langage
  naturel et en Python, balayage et Newton cités). Dernières capacités évaluées manquantes.
- Placée après la 17.10. D'abord COMBIEN (lecture du tableau, théorème des valeurs intermédiaires en
  filigrane), puis OÙ (dichotomie). Figures `nombre_solutions` (x³ − 3x² + 2, fonction de la 17.4, droites
  k = 5, 2, 0, −3) et `dichotomie_etapes` ; cas industriel : bac plié, x(30 − 2x)² = 1 500, deux cotes (2,34 et
  8,26 cm) ; atelier at155 : réservoir en capsule de 50 L, rayon ≈ 14,2 cm ; générateurs `gen_nombre_solutions`
  et `gen_dichotomie` ; 10 questions.
- Règles fixées après relecture :
  - nombre de solutions : sur chaque intervalle OUVERT où f est strictement monotone, une solution si k est
    STRICTEMENT entre les valeurs aux bouts, plus 1 par extremum où f vaut exactement k (« k entre les
    valeurs aux bouts » donnait 1 ou 3 pour k = 2, au lieu de 2) ;
  - dichotomie : test du CHANGEMENT DE SIGNE, (f(a) − k) × (f(m) − k) < 0 → b ← m, sinon a ← m. Le
    raccourci « f(m) − k > 0 → a ← m » ne marche que pour une fonction décroissante et perd la solution pour
    une croissante (exécuté : [2 ; 2,001] pour x³ − 3x² + 2 depuis [2 ; 3]). Le premier jet du corrigé de
    l'exercice 4 affirmait l'inverse : erreur de l'auteur, trouvée par les deux relecteurs.
- Trouvé par l'audit : des « < » bruts dans la figure `dichotomie_etapes` (image vide), corrigés en &lt;.
- Bilan final du référentiel (relecteur justesse) : chaque contenu et capacité évalués des modules
  Fonctions, Calcul intégral et Équations différentielles a sa fiche. Deux notions couvertes mais sans
  exemple travaillé, à enrichir un jour si besoin (compléments optionnels, pas des trous) :
  - primitives de u′uⁿ avec n entier négatif (couvertes par la formule « n ≠ −1 » de la 17.2) ;
  - limites et opérations : pas de tableau des opérations ni des formes indéterminées (la règle du terme de
    plus haut degré est appliquée en 17.1 et 17.10).

### 17.10 — Étude de fonction : racine carrée, dérivée de uⁿ, asymptote oblique (faite le 2026-09-29)

- Référentiel (annexe I, Fonctions) : fonction racine carrée (fonction de référence) ; dérivée de x ↦ uⁿ(x)
  (n entier naturel non nul) et limites de uⁿ ; « limite infinie à l'infini, cas d'une asymptote oblique »
  (le commentaire exige des indications de méthode : la fiche part de f = ax + b + r(x), puis donne la méthode
  générale a = lim f(x)/x, b = lim (f(x) − ax)). La dérivée de √u n'est pas au programme : non traitée.
- Placée après la 17.4, qu'elle complète avec la 17.1 sans les reprendre. Figures `racine_carree_courbe`
  (symétrique de x², tangente de pente 1/4 en 4, tangente verticale en 0) et `asymptote_oblique` (écarts
  chiffrés) ; cas industriel : vidange d'une cuve (Torricelli, débit théorique) ; atelier at154 : coût par
  pièce selon la taille de lot, C(q) = 0,5q + 10 + 200/q (asymptote oblique, lot optimal q = √400 = 20) ;
  générateurs `gen_derivee_puissance` ((ax + b)ⁿ, (x² + c)ⁿ, k√x) et `gen_asymptote_oblique` (b d'une fonction
  rationnelle, écart à l'asymptote) ; 9 questions (bonne réponse en positions 2, 0, 1, 3, 1, 0, 2, 3, 1).
- Deux tours de relecture. 1ᵉʳ tour : 6 bloquants, dont deux pièges de at154 dont la valeur ou le message ne
  correspondait pas à l'erreur visée (2 010 au lieu de 2 015 pour 200 × 10), la règle √(ab) = √a √b utilisée
  sans être énoncée, et la conclusion du cas industriel qui se lisait comme une contradiction (vitesse qui
  baisse dans le temps contre perte par centimètre de niveau). Générateur : 2,7 % de tirages dégénérés (la
  « courbe » était la droite elle-même), exclus.

### 17.12 — Calcul intégral : propriétés de l'intégrale et aire entre deux courbes (faite le 2026-09-29)

- Référentiel (annexe I, Calcul intégral) : propriétés de l'intégrale (relation de Chasles, linéarité,
  positivité), aire du domaine {a ≤ x ≤ b, f(x) ≤ y ≤ g(x)} (capacité attendue, y compris le cas où f ou g
  est la fonction nulle) ; méthodes approchées (point-milieu, trapèzes, Monte-Carlo) citées dans les
  commentaires : traitées au § 6 comme « pas une capacité exigée, mais un sujet peut faire lire ou compléter
  un algorithme ».
- Placée juste après la 17.2, qu'elle complète sans la reprendre. Figures `chasles_integrale`,
  `aire_entre_courbes` (zone sous f grisée « à retrancher »), `courbes_qui_se_croisent`, `methode_trapezes` ;
  atelier at153 (patin de guidage en lentille entre deux arcs, sans figure) ; générateurs
  `gen_aire_entre_courbes` (courbes données dans un ordre aléatoire, corrigé en fractions exactes) et
  `gen_chasles_linearite` ; 9 questions (bonne réponse en positions 1, 2, 0, 3, 1, 0, 2, 3, 1).
- Méthode en quatre gestes : résoudre g = f TOUJOURS (bornes, ou croisement où couper), une valeur test par
  morceau, ∫ (haut − bas), contrôle (positive ; « rectangle de contrôle » = largeur × plus grande
  épaisseur, l'aire en vaut exactement 2/3 quand l'épaisseur est une arche de parabole nulle aux bornes).
- Deux tours de relecture. 1ᵉʳ tour : 3 bloquants, dont un corrigé d'atelier dont les lignes se collaient
  (antislash suivi d'un vrai retour à la ligne, continuation Python, invisible pour l'audit : contrôle
  CONTINUATION ajouté, commit séparé f9ff112), l'avertissement de la page Maths qui annonçait à tort du
  calcul intégral manquant, et une méthode qui ne disait pas comment repérer un croisement quand les
  bornes sont données. 2ᵉ tour : 0 bloquant, 14 retouches (corrigé du générateur en fractions exactes :
  « 3,33 − (−3,33) = 6,67 » affiché faux dans 16 % des tirages…).
- Hors fiche, commits séparés : « 26 fiches » du parcours « Avant de commencer » (8e0ea98), signe moins de la
  ligne « Réponse » (b47ad3a).
- Inventaires : ligne « Analyse » du tableau de bord (17.12 ajoutée, calcul intégral complet), résumé du bloc
  17, avertissement de la page Maths (plus que des notions sur les fonctions), étape 3 du parcours.

### 17.9 — Trigonométrie : courbes, dérivées et primitives de sin et cos (faite le 2026-09-28)

- Référentiel : fonctions sinus et cosinus comme fonctions de référence (« exploiter la courbe pour retrouver
  des propriétés »), dérivées, primitives de cos(ωt + φ) et sin(ωt + φ) (complément du module Calcul
  intégral), valeur moyenne. La dérivée de cos(ωt + φ) n'est citée explicitement que dans le module
  « signal », hors liste CPI : elle est gardée comme outil de vérification des primitives et prérequis de la
  18.19 (statut évalué, avis du relecteur justesse).
- Placée juste après la 17.7 dans BLOC_17 (pas de code de tri : l'ordre d'affichage est l'ordre de la
  liste). Figures `sin_cos_courbes`, `parametres_sinusoide` (graduations π, 2π, 4π) et `lire_sinusoide`
  (goulotte vibrante, x(t) = 2 cos(50π t − π/4), réponse dans le cadre du bas) ; atelier at152 (lire la
  vibration d'une goulotte vibrante, sans figure : `lire_sinusoide` donnerait la réponse) ; générateurs
  `gen_periode_frequence` (T, f ou vitesse maximale) et `gen_primitive_trig` (intégrale de K cos(ωt) ou
  K sin(ωt)) ; 9 questions (bonne réponse en positions 0, 1, 2, 0, 3, 1, 2, 1, 3).
- Choix validés par l'auteur : pas de figure pour at152 ; seuil d'alerte de 7 mm/s présenté comme choix du
  service maintenance, en valeur crête, sans citer ISO 10816 (ses zones sont en valeur efficace) ; tension
  redressée double alternance (2A/π) gardée au § 5, nommée et rattachée à la 17.5 ; pas de définition du
  radian (supposée installée par la 7.2).
- Trois tours de relecture. 1ᵉʳ tour : 5 bloquants, dont une broche vibrant à ±2 mm (314 mm/s, 5 g)
  incompatible avec le seuil de 7 mm/s de la même fiche (l'objet devient une goulotte vibrante, où 5 g est
  voulu ; le cas industriel garde la broche) ; une règle « le 1ᵉʳ maximum arrive quand ωt + φ = 0 » fausse
  dès que φ > 0 ; une intégrale de 0 à π/2 de cos t présentée comme « demi-période » (c'est un quart) ; une
  égalité fausse dans le corrigé de gen_periode_frequence. 2ᵉ tour : 2 bloquants (égalité fausse résiduelle ;
  cas de l'avance inapplicable devant un écran, remplacé par t₀ = 1re crête visible − T, avec l'exercice
  1 bis). 3ᵉ tour : 0 bloquant, 8 retouches (contrôle du signe de φ par x′(0), car x(0) = A cos(±φ) ne le
  tranche pas ; « 0,64 = 2/π » corrigé en « 2/π ≈ 0,64 »…).
- Règle de lecture de φ harmonisée partout : t₀ = instant du maximum le plus proche de t = 0.
- π gardé exact : principe posé au § 3 et en erreur classique n° 7 ; consigne dans l'énoncé des générateurs
  (« Simplifie les π » ou « Garde π exact »). Arrondis intermédiaires : 0 refus avec ω à 2 décimales,
  sin/cos à 3 décimales et k/ω exact ou à 3 décimales (10 000 tirages) ; π ≈ 3,14 reste refusé à 0,1 près,
  et l'énoncé le déconseille.
- ✅ Vérifiée le 2026-09-28 dans un vrai navigateur, 32 contrôles OK : at152 en entier (chaque piège puis la
  bonne valeur, les deux QCM, corrigé déroulé), les deux générateurs, les trois figures, les six onglets sans
  marque de rendu ratée ; tableau des paramètres, cas de l'avance et § 6 regardés à l'œil.
- Inventaires : résumé du bloc 17, ligne « Analyse » du tableau de bord (17.9 ajoutée ; courbes de sin et cos
  et primitives de cos(ωt + φ) retirées des non-traités ; statut toujours « Incomplet »), avertissement de la
  page Maths gardé jusqu'à la fin du plan complémentaire.

### Analyse (Fonctions, Calcul intégral) : notions du référentiel non traitées (relevé du 2026-09-28)

Le plan de 13 fiches est terminé, mais il ne couvrait pas tout le référentiel : la ligne « Analyse » du
tableau de bord reste « Incomplet ». Relevé par le relecteur justesse (recherche par mots-clés dans les
blocs 7, 17 et 18), vérifié dans le texte de l'annexe I. Liste brute, sans ordre de priorité (l'ordre de
traitement viendra du plan complémentaire).

Au programme (contenu ou capacité attendue), absent de l'app :
- asymptote oblique (contenu « Limite infinie d'une fonction à l'infini. Cas d'une asymptote oblique ») ;
- nombre de solutions d'une équation f(x) = k à partir du tableau de variation (capacité attendue) ;
- procédé de recherche d'une valeur approchée d'une racine (capacité attendue ; le commentaire cite
  balayage, dichotomie, Newton, et demande au moins un algorithme) ;
- dérivée de x ↦ uⁿ(x) (contenu ; seule la primitive de u′uⁿ est traitée, en 17.2) ;
- fonction racine carrée comme fonction de référence (contenu) ;
- fonctions sinus et cosinus comme fonctions de référence, courbes (contenu ; seules les dérivées sin′ et
  cos′ figurent, en 7.2) ; ✅ traité en 17.9 ;
- propriétés de l'intégrale : relation de Chasles, linéarité, positivité (contenu) ;
- aire entre deux courbes, {a ≤ x ≤ b et f(x) ≤ y ≤ g(x)} (capacité attendue) ;
- primitives de t ↦ cos(ωt + φ) et t ↦ sin(ωt + φ) (contenu, « complément ») ; ✅ traité en 17.9.

Cité en exemple dans les commentaires (non exigible) :
- méthodes élémentaires d'approximation d'une intégrale (point-milieu, trapèzes, Monte-Carlo), avec des
  algorithmes.

### 18.19 — Équations différentielles du second ordre (faite le 2026-09-28)

- Référentiel (annexe I, module Équations différentielles) : a y″ + b y′ + c y = d(t) à coefficients
  constants, d polynôme, e^(λt), cos(ωt + φ) ou sin(ωt + φ) ; « les indications permettant d'obtenir une
  solution particulière sont données » ; résolution à la main dans les cas simples, par calcul formel dans
  tous les cas ; conditions initiales ; famille de courbes. La résonance est en « pour aller plus loin »,
  non exigible (forme donnée par l'énoncé).
- Placée en fin de bloc 18, après 18.18, avec méthode, figures `famille_second_ordre` (x(0) = 2, 1, −1,5),
  `regime_force` (y″ + 2y′ + 5y = 10 cos t : régime imposé + partie homogène qui s'éteint) et
  `pied_equilibre_poids` (X = 10,7 + écart qui s'éteint ; équilibre X_p = mg/k, bande ± 0,1 mm, 0,75 s),
  atelier at151 (balance de contrôle, 2x″ + 16x′ + 320x = 0, sans figure), générateurs `gen_constantes_ci`
  (A ou B dans les trois cas de Δ, « avec r₁ > r₂ » pour Δ > 0, diagnostic d'inversion des racines) et
  `gen_solution_particuliere` (constante, affine, cos), 9 questions (bonne réponse en positions 1, 2, 3, 0,
  1, 3, 0, 1, 2).
- Choix validés par l'auteur : synthèse du bloc des équations différentielles (18.4 : une exponentielle par
  racine réelle ; 18.8 : équilibre + écart qui s'éteint, y_p ↔ y_eq ; 18.18 : équation caractéristique,
  α ± βi) ; notations de la 18.18 ; pas de renvoi à une fiche « systèmes 2×2 » (il n'y en a pas) : A et B
  se trouvent l'un après l'autre ; cas industriel = le pied antivibratile de la 18.18 résolu pour de bon
  (x(t) = e^(−4t)(2 cos 30t + 0,267 sin 30t), 0,75 s, écrasement statique 10,7 mm = X_p = mg/k).
- Deux tours de relecture : 7 bloquants au 1ᵉʳ (dont l'ordre des racines non précisé dans
  gen_constantes_ci, qui faisait refuser 99 % des élèves choisissant l'autre ordre ; le lien 18.4 non
  exploité ; les 10,7 mm noyés dans une incise), 2 au 2ᵉ (dont, dans gen_solution_particuliere, un B
  calculé à partir d'un A arrondi qui faisait refuser 6,3 % des cas cos-B : le corrigé calcule désormais
  chaque inconnue depuis les valeurs exactes). Simulation d'un élève qui recopie les valeurs arrondies
  affichées dans le corrigé : 0 refus sur 10 000 tirages, dans chacun des 11 cas (constante, affine K/L,
  cos A/B ; Δ > 0, = 0, < 0 pour A et B).
- Trouvé avant insertion : un « < » brut dans la légende de la nouvelle figure (« écart < 0,1 mm »),
  attrapé par le contrôle d'audit FIGURE ajouté la veille.
- ✅ Vérifié le 2026-09-28 dans un vrai navigateur, 32 contrôles OK : at151 en entier (chaque piège puis la
  bonne valeur, les deux QCM, corrigé déroulé), les deux générateurs (ligne « Réponse » propre), les trois
  figures affichées et regardées, les six onglets sans marque de rendu ratée ; tableau de contrôle
  « y(0) / y′(0) » et paragraphe « Pour aller plus loin — la résonance (non exigible) » regardés à l'œil.
- Non vérifié en exécution : la commande Xcas `desolve([...], t, y)` (Xcas absent de la machine) ; trace,
  pas une dette bloquante.
- Inventaires : résumé du bloc 18 (« les quatre modules sont traités »), ligne « Analyse » du tableau de bord
  (second ordre ajouté, liste des notions non traitées, statut « Incomplet »), avertissement de la page
  Maths remis (notions de fonctions et de calcul intégral non traitées).

### 18.18 — Nombres complexes, prérequis du second ordre (faite le 2026-09-27)

- Référentiel (annexe I, module Équations différentielles) : les complexes sont introduits « pour
  disposer de l'équation caractéristique d'une équation différentielle linéaire du second ordre » ;
  forme algébrique, somme, produit, conjugué ; « on se limite à l'écriture algébrique » ; résoudre une
  équation du second degré à coefficients réels. Ni module, ni argument, ni forme trigonométrique ou
  exponentielle, ni quotient : ils ne sont pas au programme et ne servent pas à la 18.19.
- Placée en fin de bloc 18, après 18.12 (juste avant la future 18.19), avec méthode, figures
  `second_degre_trois_cas` (Δ > 0, = 0, < 0 ; axe de symétrie = partie réelle) et
  `oscillateur_trois_cas` (x″ + c x′ + 26 x = 0 pour c = 12, 2, 0 : retour sans osciller, oscillation
  amortie, oscillation sans fin ; enveloppe ±√1,04·e^(−t)), atelier at150 (pied antivibratile,
  25 r² + 200 r + 22 900 = 0, racines −4 ± 30i, 4,8 Hz), générateurs `gen_calcul_complexe` (somme,
  différence, produit, z × z̄ ; affichage des termes signés par `_termes`) et `gen_racines_complexes`
  (partie réelle ou imaginaire, a = 1, 2, 4, cas b = 0), 9 questions (bonne réponse en positions 1, 0,
  2, 1, 3, 0, 1, 3, 2).
- Choix validés par l'auteur : fiche annoncée comme prérequis de la 18.19 (§ 1 : du système
  masse-ressort-amortisseur à l'équation caractéristique par x = e^(rt), même outil exponentiel qu'en
  18.4 et 18.16) ; c reste l'amortissement (lettre des cours de mécanique), l'ambiguïté avec le c de
  Δ = b² − 4ac étant levée par un encadré AVANT le premier calcul (Δ = c² − 4mk), les racines notées
  α ± βi (produit α² + β² = k/m, somme −c/m) ; somme et produit des racines démontrés avant d'être
  utilisés ; ancrage CPI : impédances (notation j), vibrations (tôle frappée : β la note, α la vitesse
  d'extinction).
- Deux tours de relecture (justesse + clarté) : 4 bloquants au 1ᵉʳ (double sens de c ; somme et produit
  des racines utilisés sans être introduits ; « −2² + 3² = 13 » et « + − » dans les corrigés des
  générateurs), aucun au 2ᵉ.
- Trouvé au premier rendu dans l'app : les deux figures s'affichaient vides (16 px) à cause de « Δ < 0 »
  écrit tel quel dans leur SVG ; corrigé (&lt;) et devenu un contrôle d'audit (commit séparé).
- ✅ Vérifié le 2026-09-27 dans un vrai navigateur, 32 contrôles OK : at150 en entier (chaque piège puis
  la bonne valeur, les deux QCM, corrigé déroulé), les deux générateurs (ligne « Réponse » propre), les
  deux figures affichées à leur taille (436 px et 370 px) et regardées, les six onglets sans marque de
  rendu ratée.
- Tableau de bord : ligne « Analyse » complétée (nombres complexes) ; reste « Non traitées : équations
  différentielles du second ordre » (fiche 18.19, annoncée « en préparation »).

### 18.17 — Loi de Poisson, compter des événements rares (faite le 2026-09-27)

- Référentiel (annexe I, Probabilités 2) : loi de Poisson introduite comme nombre de réalisations sur
  une durée quand l'attente entre deux réalisations suit une loi exponentielle ; représenter la loi,
  calculer à la calculatrice ou au tableur, interpréter E et σ, déterminer le paramètre de la loi de
  Poisson approchant une binomiale. Expression explicite « non attendue » (donnée pour information) ;
  conditions d'approximation « non exigibles ».
- Placée après 18.16 (… 18.11 → 18.16 → 18.17 → 18.7 …), avec méthode, figures `poisson_processus`
  (six années simulées, graine 3 : 10, 6, 8, 4, 4, 7 pannes ; attente exponentielle et nombre de
  Poisson sur le même axe), `poisson_batons` (m = 6,4, stock de 11) et `poisson_binomiale`
  (B(2 000 ; 0,001 5) contre Poisson(3), B(20 ; 0,3) contre Poisson(6)), atelier at149 (cordons de
  soudure, 0,04 défaut par mètre, étapes 2 à 5 avec `depend_de`), générateurs `gen_proba_poisson`
  (traduction exactement / au plus / moins de / au moins / plus de) et `gen_parametre_poisson`
  (taux × durée avec conversion, densité × surface, np limité à 10, parc de machines), 9 questions
  (bonne réponse en positions 1, 2, 3, 0, 3, 0, 1, 2, 1).
- Promesse de la 18.16 tenue : m = 40 × 0,16 = 6,4 remplacements, stock de 11 (P(X ≤ 10) ≈ 0,939,
  P(X ≤ 11) ≈ 0,969) ; P(X = 0) = e^(−0,16) ≈ 0,852, la fiabilité sur un an de la 18.16. Les « à
  venir » de la 18.16 sont retirés.
- Choix validés par l'auteur : paramètre noté m (λ sur TI et NumWorks, μ sur Casio : expliqué dès le
  § 2) ; les deux faces du même processus rendues explicites (tableau, pont P(X = 0) = P(T > t),
  encadré « Laquelle des deux ? Faites le tri », question de quiz à réponse exponentielle ; critère :
  regarder ce que l'on cherche, un nombre ou une durée) ; les deux approximations d'une binomiale
  distinguées (tableau « Quelle approximation choisir ? », réflexe « np d'abord » en trois cas) ; les
  4 questions de choix Poisson/normale gardées avec la mention « pour comprendre : à l'examen,
  l'énoncé précise la loi ».
- Chiffres de la simulation des 1 000 années (moyenne 6,49, écart-type 2,56, 38 années au-delà de 11
  pannes) : attentes exponentielles de moyenne 625 h cumulées sur 4 000 h, `random.Random(2026)`.
- Deux tours de relecture (justesse + clarté) : 4 bloquants au 1ᵉʳ (dont « 2 défauts, le cas le plus
  fréquent » alors que P(X = 1) = P(X = 2) pour m = 2), aucun au 2ᵉ.
- ✅ Vérifié le 2026-09-27 dans un vrai navigateur, 32 contrôles OK : at149 en entier (chaque piège
  puis la bonne valeur, les deux QCM, corrigé déroulé), les deux générateurs (ligne « Réponse »
  propre), les trois figures chargées et regardées, les six onglets sans marque de rendu ratée ;
  formule `=-625*LN(ALEA())` affichée entière.
- Tableau de bord : « Statistiques et Probabilités » passé à « Complet » (contenu évalué des modules
  Statistique descriptive, Probabilités 1, Probabilités 2 hors processus aléatoires et Statistique
  inférentielle vérifié dans les fiches).
- Reste à faire, commits séparés : marge de 1e-9 dans les comparateurs (|1,49 − 1,5| vaut
  0,010 000 000 000 000 009 en machine : réponse au bord de la tolérance refusée) ; notation P_A(B)
  du référentiel à mentionner dans la 18.5.

### 18.16 — Loi exponentielle, durée de vie sans usure (faite le 2026-09-26)

- Référentiel (annexe I, Probabilités 2) : simuler la loi exponentielle à partir de la loi uniforme,
  représenter la densité, calculer une probabilité, interpréter l'espérance et l'écart-type
  (fiabilité, désintégration radioactive). E(T) = 1/λ admis (intégration par parties hors
  programme) ; loi de Weibull signalée hors programme.
- Placée après 18.11 (… 18.10 → 18.11 → 18.16 → 18.7 → 18.13 …), avec méthode, figures
  `exponentielle_densite` (quatre points λ, 0,67 λ, 0,37 λ, 0,14 λ ; aires 63,2 % / 36,8 % ; E(T) et
  médiane) et `exponentielle_simulation` (1 000 durées, graine 2026), atelier at148 (24 modules
  d'entrées/sorties, 6 000 h par an, étapes 2 à 4 avec `depend_de`), générateurs
  `gen_proba_exponentielle` et `gen_duree_fiabilite`, 9 questions (bonne réponse en positions 1, 3, 0,
  2, 2, 0, 3, 1, 1).
- Choix validés par l'auteur : densité construite comme l'histogramme des pannes (raisonnement heure
  par heure, tableau à 6 colonnes) ; primitive notée G, F réservée à la fonction de répartition ;
  notation P(B | A) ; E(T) rattachée à la constante de temps τ de la 18.4 (repères 37 % et 5 % à 3τ),
  jamais aux repères 68/95 % de la loi normale ; repère E ± 2σ rattaché à la LOI (comptage binomial
  en cloche, moyenne par la limite centrée), pas à la valeur ; cas industriel en binomiale
  B(40 ; 0,148), stock de 10, avec pont vers la 18.17 (Poisson, stock de 11) ; pas de formule tableur
  =-25000*LN(1-ALEA()).
- Consigne « garde toutes les décimales de la calculatrice dans les calculs intermédiaires » dans les
  deux générateurs, tolérances NON élargies : sans elle, un quotient d'exponentielles arrondies au
  millième était refusé dans 11 % des tirages de `gen_proba_exponentielle` (cas « déjà âgé »). at148
  étape 3 : « Garde au moins 4 décimales », piège 0,89 (arrondi trop tôt).
- Cinq tours de relecture (justesse + clarté) jusqu'à zéro réserve. Relevé tardivement (4ᵉ tour) : la
  liste « le composant s'use-t-il ? » du § 6 avait ses réponses inversées (oui → exponentielle).
- ✅ Vérifié le 2026-09-26 dans un vrai navigateur (Edge sans fenêtre, clics et frappes via DevTools) :
  at148 en entier, 19 contrôles OK (pièges 0,0002, 8,33, règle de trois 0,88, arrondi trop tôt 0,89,
  2,88 de Poisson ; les deux QCM, mauvaise option puis bonne ; corrigé déroulé, 2,71 modules, sans
  antislash-n) ; `gen_proba_exponentielle` (cas « déjà âgé » : diagnostic « sans mémoire » ; cas
  « entre » : « Or il est neuf ») et `gen_duree_fiabilite` (règle de trois diagnostiquée, « Réponse :
  446 h » à l'heure près). Le parcours a révélé le défaut transversal des astérisques de la ligne
  « Réponse » (corrigé à part).
- ✅ Dette transversale corrigée le 2026-09-26 (commit séparé) : la réponse affichée de
  `gen_duree_fiabilite` sortait avec 2 décimales (« 5 268,03 h ») alors que l'énoncé dit « à l'heure
  près ». Voir « Réponse affichée : la précision suit l'énoncé » ci-dessous.

### Dette d'interface 17.7 à 18.13 (close le 2026-09-27)

- Passe groupée dans un vrai navigateur (Edge sans fenêtre, clics et frappes via DevTools), menée à
  partir des données de app.py : pour chaque étape d'atelier, le premier piège (message attendu
  vérifié) puis la bonne valeur ; pour chaque QCM, une mauvaise option (diagnostic vérifié) puis la
  bonne ; corrigé déroulé jusqu'à « À retenir ».
- Ateliers at139 à at145 : 99 contrôles OK, aucun défaut propre à un atelier.
- 11 générateurs des fiches 17.7 à 18.13 : tous tirés, ligne « Réponse » propre (sans astérisques),
  aucune marque de rendu ratée.
- Figures : les 16 figures des fiches 17.7 à 18.13 et 18.16, et les 5 figures d'ateliers, chargées et
  regardées une à une dans l'app (rien de tronqué, pas de chevauchement gênant).
- Texte des 8 fiches (6 onglets chacune) balayé : « ** » visibles, antislash-n, LaTeX involontaire,
  None, accolades. A révélé les formules de tableur faussées (corrigé à part, voir section suivante).
- Cosmétique, non bloquant (laissé en l'état, tout reste lisible) :
  - 18.9, figure `histogramme_vers_densite` : l'étiquette « 3 barres ≈ 30 % » passe sur le bas des
    barres orange ;
  - 18.16, figure `exponentielle_simulation` : la courbe orange coupe l'étiquette « 140 » de la
    2ᵉ barre ;
  - 18.10, figure `binomiale_continuite` : graduations « 24,5 / 25 / 25,5 » serrées.

### Figures : chaque SVG doit être du XML valide (contrôle ajouté le 2026-09-27)

- Les figures sont affichées en <img src="data:image/svg+xml;base64,…"> : un SVG qui n'est pas du XML
  valide donne une image VIDE (16 px de haut), sans aucune erreur. Cas réel : « Δ < 0 » écrit tel quel
  dans les deux figures de la 18.18 (corrigé par &lt; avant son commit). Les 171 autres figures étaient
  valides.
- Outil d'audit : contrôle FIGURE, qui exécute chaque fonction de FIGURES et lit son SVG comme du XML.
  Test par mutation : « Δ < 0 » remis brut → FIGURE sur exactement les deux figures ; 0 sur l'app
  corrigée (173 figures).

### Formules de tableur affichées faussées par le Markdown (corrigé le 2026-09-27)

- Trouvé au parcours navigateur de la dette 17.7 à 18.13 ; invisible à la relecture du source.
- `$F$1` (référence absolue) : Streamlit lit « $F$ » comme une formule LaTeX (F mathématique en
  italique, gras cassé, « ** » visibles). Fiche 18.12 (cours, formulaire, corrigé) et une question du
  quiz (options passées par `st.radio`, qui interprète aussi le Markdown). Écrit `\\$F\\$1` dans le
  source.
- `*` de multiplication : deux `*` du même paragraphe forment un italique et disparaissent. L'élève
  lisait des formules FAUSSES : 18.12, `=B2+$F$1(-(B2-(20+0,2A2))/15)` ; 18.16 (Formulaire, retouche
  J-A3 du 3ᵉ tour), `=-E(T)LN(ALEA()), par exemple =-25000LN(ALEA())`. Écrit `\\*` dans les formules
  de tableur de tous les textes Markdown (13 formules). Pas dans les figures SVG (`_txt`, `_svg`) ni
  les titres de FIGURES, affichés en HTML : l'antislash y serait visible.
- Outil d'audit : contrôles DOLLAR et ETOILE ; test par mutation sur l'ancien app.py : 5 DOLLAR et
  13 ETOILE.
- ✅ Vérifié dans un vrai navigateur : toutes les formules de tableur des fiches 18.12 et 18.16 (cours,
  formulaire, exercice) s'affichent entières, `*` compris, sans antislash ni italique. Non vu au
  navigateur : les options du quiz corrigées (même rendu Markdown que les fiches).

### Ligne « Réponse » : astérisques affichés sans unité (corrigé le 2026-09-26)

- Trouvé au parcours navigateur de la 18.16 : un générateur sans unité affichait
  « **Réponse : 0,449 ** » en clair (espace avant les ** fermants : Markdown ne reconnaît pas le
  gras). 14 générateurs touchés, presque tout le bloc 18 (probabilités, tests, intervalles).
- Correctif : `ligne_reponse(ex)` n'ajoute l'espace et l'unité que si l'unité existe.
- Outil d'audit : nouveau contrôle GRAS (ligne « Réponse » qui n'est pas un gras Markdown valide) ;
  test par mutation : l'ancien code → GRAS sur 14 générateurs.
- ✅ Vérifié dans un vrai navigateur : « Réponse : 0,126 » (sans unité), « Réponse : 2 231 h » et
  « Réponse : 28,01 N·m » (avec unité).

### Réponse affichée : la précision suit l'énoncé, pas la tolérance (corrigé le 2026-09-26)

- Un générateur peut déclarer `"decimales": n` quand son énoncé impose une précision ; sinon la page
  garde `decimales_affichage(tol)` (fonction `decimales_reponse`). Seul `gen_duree_fiabilite` le fait
  (`"decimales": 0`, « à l'heure près »).
- Piste écartée : « tolérance ≥ 1 → affichage entier ». Mesuré sur 3 000 tirages : six générateurs
  atteignent tol ≥ 1, dont quatre par tolérance RELATIVE (grande réponse), sans consigne d'entier.
  La règle aurait affiché 72 N·m pour 72,44 (`gen_couple_puissance`), 85 g pour 84,70
  (`gen_masse_piece`), 64 MPa pour 63,66 (`gen_traction_sigma`).
- L'outil d'audit lit la réponse affichée avec `decimales_reponse` (contrôle AFFICHÉE, y compris avec
  le champ) et signale un champ invalide (contrôle DÉCIMALES) ; test par mutation : `"decimales": 0`
  sur un générateur au millième → AFFICHÉE 2000/2000, `"decimales": 1.5` → DÉCIMALES.
- ✅ Vérifié dans un vrai navigateur (9 contrôles OK) : `gen_duree_fiabilite` affiche « Réponse :
  1 116 h » et « 410 h » (entiers acceptés), `gen_couple_puissance` garde « 28,65 N·m » et
  « 18,76 N·m ».

### 18.15 — Comparer deux proportions ou deux moyennes (faite le 2026-09-26)

- Référentiel (annexe I, Statistique inférentielle) : « tests bilatéraux et unilatéraux de
  comparaison de deux proportions ou de deux moyennes dans le cadre de la loi normale ». Les
  échantillons appariés ne sont pas mentionnés : non traités (décision de l'auteur).
- Placée après 18.14 (… 18.13 → 18.14 → 18.15 → 18.8 → 18.12), avec méthode, figure
  `comparaison_difference` (différence centrée sur 0, zone verte bilatérale, zone ERRONÉE obtenue en
  additionnant les écarts-types, d entre les deux), atelier at147 (deux presses, proportion commune,
  étapes 2 et 3 avec `depend_de`), générateurs `gen_comparaison_moyennes` (en unilatéral, question
  posée en mots : l'élève traduit lui-même le sens) et `gen_comparaison_proportions`, 9 questions
  (bonne réponse en positions 2, 0, 3, 1, 3, 1, 0, 2, 1).
- Choix validés par l'auteur : notation f pour la proportion commune (« parfois notée p̂ ») ;
  conditions vérifiées sur chacun des deux échantillons observés, en nombre de pièces, pas avec f ;
  σ(X̄₁ − X̄₂) et σ(F₁ − F₂) (graphie de la 18.14) ; encadré « Ordre » (écrire D avant H₁) ;
  pièges conceptuels dans l'atelier (proportion commune, moyenne simple, ordre, 1,645 en bilatéral
  sur les mêmes presses que l'exercice unilatéral), pièges techniques dans les générateurs ; question
  du test toujours fixée AVANT le contrôle (Protocole de la 18.14), y compris dans les exemples.
- Trois tours de relecture (justesse + clarté) jusqu'à zéro réserve. Relevé au passage : un premier
  exemple de proportions trop équilibré (400/500) remplacé par 300/700, où la moyenne simple se
  distingue nettement de la proportion commune ; l'argument « soustraire les variances donnerait
  σ(D) = 0 » précisé (à effectifs égaux).
- ✅ Vérifié le 2026-09-26 dans un vrai navigateur (Edge sans fenêtre, clics et frappes via DevTools,
  36 contrôles OK) : at147 en entier (pièges f₁, moyenne simple, f₁/f₂ séparés, 1,645, ordre f₁ − f₂ ;
  les deux QCM avec une mauvaise option puis la bonne ; corrigé déroulé, sans antislash-n) ;
  `gen_comparaison_moyennes` en bilatéral (écarts-types additionnés diagnostiqués), en unilatéral
  « plus » et « moins » (le signe opposé donne « Tu as traduit la question dans l'autre sens », ligne
  « Côté » du corrigé affichée, seuil négatif accepté) ; `gen_comparaison_proportions` (f₁ et f₂ séparés
  diagnostiqués, bonne réponse acceptée).
- Formulation unilatérale : balayage de 5 000 tirages, seules « plus résistant » (1 250) et « moins
  résistant » (1 266) sortent — jamais « aussi… que », « équivalent », « comparable » (le gabarit n'a
  que ces deux mots). Aucune dette de formulation.
- Dette mineure (toute l'application, page Entraînement) : la ligne « Réponse : -6,92 MPa » affiche un
  tiret ASCII, alors que la méthode écrit « −6,92 » avec le vrai signe moins. À uniformiser au fil.

### 18.14 — Tests d'hypothèse sur une proportion et sur une moyenne (faite le 2026-09-26)

- Référentiel (annexe I, Statistique inférentielle, Tests d'hypothèse) : tests bilatéraux et
  unilatéraux sur une proportion (loi binomiale, puis binomiale approximable par une normale) et
  sur une moyenne ; région de rejet et règle de décision ; choix fournis dans les cas délicats ;
  risques de 1ʳᵉ et 2ᵉ espèce ; puissance abordée. Les tests de COMPARAISON de deux échantillons
  restent à faire (fiche 9 du plan).
- Placée après 18.13 (ordre affiché … 18.7 → 18.13 → 18.14 → 18.8 → 18.12), avec méthode, figures
  `test_region_rejet` (zone où l'on garde H₀ et région critique d'un test unilatéral) et
  `risques_alpha_beta` (α et β sur deux cloches), atelier at146 (machine à 50,00 mm, étapes 2 et 3
  avec `depend_de`), générateurs `gen_test_moyenne` et `gen_test_proportion`, 9 questions dans la
  banque « probabilités et équations différentielles » (bonne réponse en positions 1, 3, 0, 2, 2,
  0, 3, 1, 2), dont une sur la puissance.
- Notation : σ(F) = √(p₀(1 − p₀)/n) et σ(X̄) = σ/√n, graphie de la 18.11 ; la 18.13 note désormais
  aussi σ(F) dans ses formules. (Le « σF » de la 17.8 est l'écart-type d'une force, sans rapport.)
- Retouches ailleurs : 18.13 § 7 renvoie à la 18.14 ; 18.11 (navette) aussi ; résumé du bloc 18,
  encart de la page Maths et tableau de bord : seuls les tests de comparaison restent non traités.
- Trois tours de relecture (justesse + clarté) jusqu'à zéro réserve. Points arbitrés par l'auteur :
  raisonnement à contre-courant et image du procès menée jusqu'aux deux risques (condamner un
  innocent = α, acquitter un coupable = β) ; H₀ par défaut parce qu'elle fixe un nombre ; zone du
  test = zone verte de la 18.13 centrée sur p₀ en bilatéral, ouverte d'un côté en unilatéral ;
  bilatéral/unilatéral choisi d'après la question (choix a posteriori : risque réel 10 %) et
  encadré « Protocole » au § 6 ; β calculé en imaginant une dérive (48 % pour 20,02 mm, 15 % pour
  20,03 mm), « β dépend de la dérive supposée », puissance 85 % / 52 %, compromis α/β (β ≈ 72 % à
  α = 1 %) et rôle de n ; petit échantillon traité par la loi binomiale exacte (rejet à partir de
  5 défectueuses sur 50) et exercé dans l'exercice.
- ✅ **Vérifié dans l'interface le 2026-09-26** (dette de la 18.14 close) : atelier at146 et
  générateurs `gen_test_moyenne` / `gen_test_proportion` parcourus dans l'application réelle, dans
  un vrai navigateur (Edge sans fenêtre, clics souris et frappes clavier via le protocole DevTools,
  captures d'écran) : 21 contrôles OK sur 21 — pièges et diagnostics affichés (σ au lieu de σ(X̄),
  1,96 au lieu de 1,645), arrondis de l'indice acceptés (50,02 ; 49,98), les deux QCM avec
  diagnostic, corrigé en six temps (vrais sauts de ligne), réponse des générateurs acceptée et
  affichée à la même précision que la saisie. Relevé au passage et corrigé : la cote nominale de
  `gen_test_moyenne` s'affichait « 40 mm » (désormais « 40,00 mm »). **Limite** : le parcours
  exhaustif par AppTest (tous les pièges, toutes les options de QCM, 3 tirages × chaque diagnostic
  des deux générateurs) n'a pas convergé en 55 min (environ 40 lancements complets de
  l'application) et a été arrêté sans résultat ; à relancer avec une session factorisée et un
  test rapide séparé du test complet. L'outil d'audit couvre déjà, lui, tous les diagnostics des
  générateurs sur 2 000 tirages (0 défaut).

### Bouton « Voir la valeur / la réponse et continuer » inopérant (corrigé le 2026-09-26)

- Constat dans un vrai navigateur : après une mauvaise réponse, un clic sur « Voir la valeur et
  continuer » ne faisait PAS avancer l'étape (la page revenait sur la même étape, le message
  d'erreur disparaissait) — l'élève en difficulté, à qui ce bouton est destiné, restait bloqué.
  Touchés : les 145 ateliers guidés (valeur fausse et QCM faux) et les exercices guidés (« Voir
  la bonne réponse / la valeur correcte et continuer »), ainsi que les exercices générés depuis un
  document importé (même moteur). Cause : bouton créé seulement sous « if Valider » ; au rerun
  déclenché par son clic, Valider vaut False, le bouton n'est pas recréé et le clic est perdu.
- Correctif : l'erreur est retenue en session dans une clé propre à l'étape
  (`{préfixe}_at_erreur_{étape}` pour les ateliers, `{préfixe}_erreur_{étape}` pour les exercices
  guidés), effacée quand l'élève franchit l'étape, et toutes les clés d'erreur du préfixe sont
  purgées par « ↺ Recommencer » et « ← Étape précédente ».
- Vérifié dans un vrai navigateur (34 contrôles OK) : at6 (ancien) et at146, eg1, eg23 (le plus
  récent) et eg17 (QCM) — l'étape avance, la valeur donnée apparaît dans l'historique, aucune
  erreur fantôme à l'étape suivante ; « Recommencer » et « Étape précédente » effacent l'erreur.
- Outil d'audit : nouveau contrôle BOUTON (analyse statique de tous les st.button de app.py) ;
  il relevait les 4 cas corrigés et un 5ᵉ, « Carte suivante » (page À revoir), déclaré
  inoffensif (il ne fait que st.rerun(), la carte suivante s'affiche bien) et laissé tel quel.

### Corrigés d'ateliers : « \n\n » affiché en toutes lettres (corrigé le 2026-09-25)

- Constat à l'écran (page de test rendant le corrigé réel avec st.markdown, comme la page
  Ateliers) : dans 45 ateliers (at1 à at144), les textes du corrigé en six temps contenaient un
  antislash-n écrit en toutes lettres au lieu d'un vrai saut de ligne. Markdown l'affichait tel
  quel (« σ = 2000 / 40 = 50 MPa\n\nContrainte admissible… ») et les étapes se collaient sur une
  seule ligne. 73 chaînes, 250 occurrences, dans les champs calcul, remplacement, verification,
  regle et conversions.
- Correction au niveau des chaînes (ast) : seules les constantes du champ `corrige` des ateliers
  ont été modifiées, valeurs vérifiées une à une après remplacement ; affichage revérifié à
  l'écran (at6 et at144). Les 7 autres antislash-n de app.py sont légitimes et n'ont pas été
  touchés : 2 expressions régulières de `decouper_corrige` et 5 commandes LaTeX (\nu, \ne).
- L'outil d'audit signale désormais ce défaut (contrôle SAUT, ateliers et textes produits par
  les générateurs) : sur l'ancien app.py il relève les 45 ateliers, sur le corrigé 0 défaut.
- Règle pour les nouveaux ateliers : écrire les sauts de ligne des corrigés avec un seul
  antislash dans le source (vrai saut de ligne), jamais deux.

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
- ✅ Interface vérifiée dans un vrai navigateur le 2026-09-27 : atelier at142 (pièges, bonnes valeurs, QCM, corrigé), gen_borne_continuite, gen_proba_normale, figures somme_uniformes_cloche, aire_sous_cloche, binomiale_continuite regardées dans l'app (voir « Dette d'interface 17.7 à 18.13 »).

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
  - Statistique inférentielle : entièrement traitée depuis le 2026-09-26 (18.13 intervalle de
    confiance d'une proportion, 18.14 tests sur une proportion ou une moyenne, 18.15 tests de
    comparaison) ;
  - Équations différentielles : second ordre à coefficients constants (la méthode d'Euler est
    traitée depuis le 2026-09-25, fiche 18.12).
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
- ✅ Interface vérifiée dans un vrai navigateur le 2026-09-27 : atelier at141 (pièges, bonnes valeurs, QCM, corrigé), gen_proba_uniforme, figures histogramme_vers_densite, aire_uniforme regardées dans l'app (voir « Dette d'interface 17.7 à 18.13 »).


## Mécanique et CAO (blocs 0 à 6, 9, 12 à 15) — relecture lancée le 2026-09-30

Relecteurs : `relecteur-bts-meca` (justesse, calculs refaits en Python, normes ISO GPS, savoirs
S1 à S7 du référentiel dans `.claude/referentiels/bts-cpi-meca/`) et `prof-pedagogue`.
Attention : les fiches 2.1 à 2.3, 3.1 à 3.3 et 4.1 à 4.3 sont surchargées au chargement par
`FICHES[...]` (fonction `appliquer`) ; le texte des `BLOC_*` correspondant n'est pas affiché.

### Correctifs du 2026-09-30 (erreurs en ligne)

Indépendance ISO 8015 / enveloppe Ⓔ (2.3) ; blocs « Erreurs / À retenir » recopiés sur 16
fiches (1.1-1.4, 1.6, 6.1-6.11) ; 15 renvois « fiche 6.x » d'avant le découpage du bloc 6 (et
5.2 → 5.5) ; Ra 3,2 d'une portée brute de tournage ; remplissage de graisse 30 à 50 % ; tri
croisé 1.3 (total impossible) ; modèle d'un roulement à billes seul = rotule (6.1, 6.3, at80) ;
arc-boutement 6.8 (condition L > 2 f a, la force n'intervient pas). Commits « fix: » séparés.

### Améliorations relevées, non traitées (à reprendre au fil des fiches concernées)

- 6.9 : « M8 8.8, ≈ 25 N·m pour ≈ 15 000 N » ne vaut qu'avec C = 0,2 × F × d ; avec la VDI 2230
  (μ = 0,12) on trouve ≈ 18 kN (78 % de Re). Écrire « 15 000 à 18 000 N ».
- 6.5 : durée du fluage d'une bague variable selon l'onglet (« dizaines d'heures », « semaines »,
  « semaines à mois ») ; corrigé « deux bagues serrées : impossible à assembler » exagéré.
- 6.4 : les formules découpent les trois familles autrement que le cours (contact direct / palier
  lisse / roulement contre contact direct ou palier lisse / roulement / film fluide) ; le cours
  (« il faut donc un second roulement opposé ») ne mentionne pas le cas d'un seul oblique associé
  à un gorge profonde, pourtant retenu dans le cas industriel.
- 6.11 : le cas industriel traite un montage de poulie, qui relève plutôt de la 6.10.
- Rugosité : la figure etats_surface_cout met Ra 3,2 pour le « fraisage de finition », le quiz
  classe Ra 1,6 en finition ; « Ra 6,3 ou brut de tournage » (5.13, atelier) peut se lire comme
  une équivalence ; portée de joint à lèvres : préciser « Ra 0,2 à 0,8, rectifié en plongée ».
- 2.3 (texte affiché) : Ⓔ ne s'applique qu'à un élément de taille (cylindre, deux plans
  parallèles) ; les plans ASME appliquent l'enveloppe par défaut (Rule #1) — à signaler pour la
  lecture de plans étrangers.
- 1.3 : « F3 » écrit « simple souhait » dans le cours et autrement dans les formules : harmoniser.
- 2.1 et 5.3 : listes « À retenir » semblables à 76 % (ISO 286) — pas identiques, à vérifier que
  chacune reste propre à sa fiche.
- Renvois : 711 renvois « fiche X.Y » dans app.py ; seuls ceux vers 6.x ont été contrôlés un par
  un. Un contrôle systématique (voire un contrôle automatique dans l'audit) reste à faire.
- 6.8 : le repère L ≥ 1,5 à 2 × a est une marge de conception (sûr jusqu'à f = 0,75), pas une
  valeur normalisée ; source bibliographique à trouver si possible.

### 6.15 — Cinématique du solide : vitesses, CIR et loi entrée-sortie (faite le 2026-10-01)

- Référentiel S3.2.2 et S3.2.3 (savoirs techniques CPI 2016) : référentiel et repère, translation et
  rotation autour d'un axe fixe (position, vitesse, accélération ; mouvements uniformes ou uniformément
  variés), champ des vitesses, équiprojectivité, CIR, composition des vitesses (glissement, roulement),
  trajectoires, enveloppe, lois entrée-sortie (analytiques pour les cas plans simples seulement, logiciel
  au-delà). Aucun torseur cinématique (limite de S3.2.1). Non exigible, présenté comme lecture de figure :
  la vitesse maximale du piston (1,30 m/s vers 77°) et la courbe V(B)(θ).
- Placée EN FIN de bloc 6 (après la 6.14), id 6.15 sans renumérotation (progression.json, renvois) : un
  « 6.3, 6.15, 6.4 » à l'affichage aurait dérouté l'élève. Ligne « Cinématique et Statique » de la carte
  du programme mise à jour (six fiches).
- Contenu : cinq figures (champ_vitesses_solide, equiprojectivite_bielle, cir_construction,
  roulement_sans_glissement, composition_vitesses_pont) et une figure à curseur (bielle_manivelle_curseur :
  CIR qui se déplace, V(A), V(B), contrôle V(A) × IB / IA, courbe de la loi entrée-sortie) ; méthode ;
  ateliers at156 (compresseur, vitesse du piston par le CIR, deux QCM pour construire I, depend_de sur les
  deux étapes enchaînées) et at157 (roue d'AGV, puis la même roue qui patine) ; générateur
  gen_bielle_manivelle (famille « Cinématique » de l'Entraînement, IA/IB arrondis au mm et réponse
  calculée depuis ces valeurs) ; 8 questions dans la nouvelle catégorie « Cinématique du solide » (bonne
  réponse en positions 2, 0, 3, 1, 2, 0, 3, 1).
- Choix validés par l'auteur : le CIR défini comme le point de vitesse NULLE (deux sens : le CIR est
  immobile ; un point immobile est le CIR), ce qui sert ensuite au point mort et à la roue ; le 0 au
  contact du roulement sans glissement DÉMONTRÉ par la composition (V − ω R en bas, V au centre, V + ω R
  en haut), pas affirmé ; l'équiprojectivité montrée comme un geste (équerre, compas : ombre AH reportée
  en BK), le calcul par cosinus restant une vérification facultative.
- Relecture (relecteur-bts-meca + prof-pedagogue) avant insertion. Mécanique : ~60 valeurs recalculées en
  Python, 3 bloquants corrigés — la bonne réponse du quiz n°8 (« maximale un peu avant que la manivelle
  soit perpendiculaire à la bielle ») était fausse : le maximum vient APRÈS cette position (76,7° contre
  76,0° pour L = 4 r) et AVANT 90° ; trois opérations affichées qui ne redonnaient pas le résultat écrit
  (1,26 / 0,312 ≠ 4,02 → 1,257 / 0,3124) ; format des registres. Pédagogie : 6 points de priorité 1, dont
  les trois choix ci-dessus.
- Trouvé en préparant le parcours : la famille « Cinématique » était dans le catalogue de fabriquer_exo
  mais pas dans FAMILLES_ENTRAINEMENT (liste du menu « Thème ») — le générateur n'aurait été tiré que par
  « Mélange ». Les deux listes sont séparées : l'audit ne le voit pas.
- Audit : code 0 (156 ateliers, 45 générateurs × 2 000 tirages, 192 figures + 3 à curseurs). Information :
  at157 étape 5, ± 0,008 sur 0,14 m/s (6 %), voulu : les pièges sont à 0 et 1,34.
- ✅ Vérifié le 2026-10-01 dans un vrai navigateur (Chrome headless piloté par Selenium, captures d'écran),
  49 contrôles OK sur la vraie appli : 6.15 en dernière position du bloc 6 ; les six onglets remplis (corrigé
  déroulé par « Tout afficher ») ; les 5 figures et la figure à curseur chargées ; curseur déplacé à 90°
  (translation instantanée, V(B) = V(A)), 180° (point mort) et 120° (CIR dessiné), figure redessinée à
  chaque fois ; at156 et at157 en entier (un piège par atelier avec son diagnostic, puis chaque bonne
  valeur, les QCM, corrigé dévoilé) ; quiz « Cinématique du solide », 8 questions répondues avec
  explication ; Entraînement, famille « Cinématique » : exercice de gen_bielle_manivelle, réponse calculée
  depuis l'énoncé acceptée ; aucune erreur dans la console.
