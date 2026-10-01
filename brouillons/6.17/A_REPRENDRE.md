# Fiche 6.17 — brouillon (sauvegardé le 2026-10-01) — INSÉRÉE dans app.py le 2026-10-02

**Titre :** Modéliser les liaisons : torseur transmissible, liaisons équivalentes, hyperstatisme
**Référentiel :** S3.2.1 (savoirs techniques CPI 2016, `.claude/referentiels/bts-cpi-meca/`, lignes ~489-510)
**État :** validée par l'auteur (seuil long/court : sans chiffre) et **insérée dans app.py** le 2026-10-02 par
`inserer17.py` ; ce dossier reste comme trace du brouillon relu. Copie de sauvegarde commitée le 2026-10-02 (commit « wip: brouillon fiche 6.17
liaisons ») ; les chemins des scripts sont relatifs au dépôt.

## Fichiers

| Fichier | Rôle |
|---|---|
| `brouillon_6_17.py` | le brouillon complet : 5 figures + figure à curseurs (deux listes de choix), FICHE_6_17, MTH_6_17, ateliers at160/at161, GENERATEUR (gen_hyperstatisme_paliers), QUIZ_LIAISONS (8 questions) |
| `apercu17.py` | aperçu Streamlit du brouillon : `python -m streamlit run brouillons/6.17/apercu17.py --server.port 8599` (lit app.py pour les fonctions communes) |
| `test_figs17.py` | à lancer depuis ce dossier (`python test_figs17.py`) : exécute les figures et les 16 états de la figure à curseurs, vérifie que le SVG est du XML valide, écrit `figs17/*.svg` |
| `figs/*.png` | rendus des figures au moment de la sauvegarde |
| `inserer_modele_6_16.py` | script d'insertion utilisé pour la 6.16, à adapter pour la 6.17 (ancres : fin de la 6.16 dans BLOC_6, figures avant « # 73. CARACTÉRISER », registre après `echelle_mur`, DYN après `potence_hauban_curseur`, ateliers après at159, quiz avant `QUIZ["Statique et frottement"]`, générateur avant `def gen_masse_piece`) |

## À reprendre demain, dans l'ordre

1. **Remontrer le brouillon** (aperçu ci-dessus).
2. **Question en suspens — seuil long / court des alésages.** Le cours dit « alésage long devant son
   diamètre = pivot glissant, court = linéaire annulaire », **sans seuil chiffré** (pas de source).
   Le relecteur-bts-meca propose « L ≥ 1,5 Ø long, L ≤ 0,8 Ø court », lui aussi sans source vérifiée.
   L'exercice et le quiz utilisent L = 2 × Ø (clairement long) pour ne pas dépendre du seuil.
   → Décision de l'auteur : garder sans chiffre, ou donner le repère utilisé en classe.
3. **Les bloquants trouvés en relecture** (tous corrigés dans le brouillon, à revoir ensemble) :
   - cas industriel : « bagues courtes + une butée » donne **h = 0** (2 + 2 + 1 − 6 + 1), pas 1 ;
   - figure `glissiere_deux_colonnes` : le galet était dessiné avec une normale qui passe par l'axe de la
     colonne (il n'arrête alors rien : m = 2, h = 1) → refaite avec une vue de dessus, règle devant la
     table, normale ⊥ au plan colonne–galet ;
   - at160 : un galet cylindrique sur une règle est un contact **linéique** (h = 1) → « galet bombé »
     (ponctuelle) ;
   - générateur : la conclusion citait des conditions inexistantes dans 9 tirages sur 12 → construite
     selon le tirage, elle redonne h dans les 16 cas ;
   - titre de la figure série/parallèle qui contredisait son piège (« en série on additionne… ») ;
   - §3 : dans le plan, une glissière transmet une force de direction connue mais de **position
     inconnue** (et non « pas un glisseur ») ;
   - quiz n°7 : distracteur « deux mouvements de trop » défendable → « deux mobilités en trop ».
4. Après validation : insérer (fin de bloc 6, id 6.17, sans renumérotation), ajouter la famille
   « Liaisons » au catalogue `fabriquer_exo` **et** à `FAMILLES_ENTRAINEMENT`, mettre à jour la ligne
   « Cinématique et Statique » de MATIERES_PROGRAMME, `python outils/compteurs.py --ecrire`, audit
   (`python outils/verifier_tolerances_ateliers.py`, code 0), parcours Selenium sur la vraie appli,
   résumé à l'auteur, puis commit + push. Entrée A_VERIFIER.md à rédiger.

## Vérifications déjà faites sur le brouillon

- Tous les h recalculés par une méthode indépendante (rang du système) : arbre sur deux paliers
  (16 combinaisons, h = 0 à 5), deux colonnes h = 3, colonne + ponctuelle bien orientée h = 0,
  broche h = 4 (h = 6 si l'épaulement était modélisé en appui plan), patin à rotule = ponctuelle +
  1 mobilité interne, convoyeur h = 4 puis 0.
- Générateur : 0 diagnostic dans la tolérance, 0 doublon (5 000 tirages).
- Ateliers : tous les pièges hors tolérance (tolérance absolue 0,1 sur des entiers).
- Quiz : bonne réponse en positions 2, 0, 3, 1, 1, 3, 0, 2.
- Figures : 21 SVG valides (5 figures + 16 états de la figure à curseurs).
