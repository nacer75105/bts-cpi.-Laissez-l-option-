# BTS CPI — Application de révision et de calcul

Application Streamlit destinée à un étudiant de BTS Conception de Produits Industriels.
Elle regroupe le cours du référentiel, des quiz, des exercices générés à la volée et les
calculateurs utilisés en bureau d'études.

**150 fiches de cours** réparties en 31 blocs (des modules débutants 0A-0L jusqu'au bloc 19) ·
**363 questions de quiz** · **143 schémas dessinés par le code, tous animés** · **33 nuances de
matériaux** · tables ISO 286 complètes (0 à 500 mm) · calculateurs RDM.

Matières couvertes : conception mécanique et RDM, CAO et lecture de plan, matériaux, procédés
de fabrication et automatismes, mathématiques, physique-chimie, anglais technique, culture
générale et expression, économie-gestion.

> `app.py` est un fichier unique et auto-suffisant (c'est volontaire, pour n'avoir qu'un seul
> fichier à déployer) : il contient tout le code et tout le contenu. Les anciennes versions
> modulaires (`figures.py`, `quiz.py`, `cours_*.py`, `methodes.py`, `options.py`,
> `materiaux.py`, `iso286.py`) ont été retirées du dépôt le 2026-09-04 : elles n'étaient plus
> chargées par l'application depuis la consolidation en fichier unique, et leur contenu avait
> divergé de `app.py`. Seul `app.py` est exécuté par `streamlit run app.py`, et c'est le seul
> fichier à modifier pour changer le contenu ou le comportement de l'application.

---

## Les pages de l'application

| Page | Ce qu'on y fait |
|---|---|
| **Tableau de bord** | progression, blocs, réflexes méthodologiques |
| **Cours** | les 150 fiches, par matière (voir plus bas) |
| **Mathématiques / Physique-Chimie / Anglais technique / Culture générale / Économie-gestion** | vue filtrée du cours par matière |
| **Quiz interactif** | 363 questions, correction immédiate et explication |
| **Exercices guidés** | des exercices résolus pas à pas, avec auto-évaluation |
| **Ateliers guidés** | des mises en situation pratiques, rattachées aux fiches |
| **Schémas interactifs** | cinq schémas à curseurs (ajustements, flexion, IT, roulements, engrenages) |
| **Importer un cours (IA)** | analyse un PDF/image/.docx et propose une fiche — nécessite une clé `ANTHROPIC_API_KEY` dans `st.secrets`, ainsi que les paquets optionnels `anthropic` et `python-docx` (absents de `requirements.txt` : la page fonctionne sans, mais reste masquée/inactive tant qu'ils ne sont pas installés) |
| **Calculateur d'ajustements ISO** | tables ISO 286 de 0 à 500 mm, calcul détaillé, contrôle de conformité |
| **Calculateurs RDM** | traction, cisaillement, matage, torsion, flexion, flambage, combiné |
| **Base matériaux** | 33 nuances, comparateur, indices de performance |
| **Formulaire** | l'ensemble des formules, cherchable |
| **Ma progression** | historique des quiz et des contrôles, fiches lues, notes |
| **À revoir** | révision espacée : les questions ratées reviennent d'elles-mêmes |
| **Mode contrôle** | devoir chronométré, noté sur 20, corrigé question par question |
| **Aide-mémoire** | toutes les formules et toutes les méthodes, réunies |
| **Entraînement illimité** | exercices tirés au hasard, corrigés en six étapes |

## Les onglets d'une fiche

Chaque fiche affiche 5 onglets, plus un 6ᵉ (« Méthode ») quand il existe pour cette fiche :

1. **Cours** — le pourquoi d'abord, le vocabulaire ensuite, l'exemple chiffré toujours
2. **Formules** — les relations et leurs unités (ou, pour les fiches non calculatoires comme
   l'anglais ou la culture générale, les phrases-outils et repères méthodologiques à retenir)
3. **Cas industriel** — la même notion, en situation professionnelle réelle
4. **Exercice** — de niveau examen
5. **Corrigé** — **dévoilé étape par étape**, pour pouvoir s'arrêter dès qu'on a compris
6. **Méthode** *(sur certaines fiches)* — les gestes numérotés à faire devant un exercice

Un expander « Vidéos » est disponible sous les onglets de chaque fiche (ce n'est pas un onglet
à part entière) — voir plus bas.

---

## Les fonctions ajoutées

### La révision espacée

Chaque question ratée, au quiz comme en contrôle, devient une carte. Elle revient au bout
d'un jour, puis trois, sept, seize, trente-cinq, soixante-dix — et disparaît quand elle est
acquise. Une question réussie fait monter sa carte d'un cran ; une question ratée la
ramène au premier.

C'est la façon la plus économique de retenir : trois séances courtes réparties dans la
semaine valent mieux que deux heures la veille.

### Le mode contrôle

Un devoir chronométré, sans correction en direct, noté sur 20. On peut naviguer entre les
questions et revenir en arrière tant qu'il reste du temps. La correction complète arrive à
la fin, question par question, et les erreurs partent automatiquement en révision espacée.

### L'entraînement illimité

Des exercices tirés au hasard sur cinq thèmes : ajustements ISO, résistance des matériaux,
transmission de puissance, matériaux et masses, unités et conversions.

Les nombres changent à chaque tirage, mais **les diagnostics d'erreur sont recalculés avec
eux** : si l'on oublie le facteur 4 dans πd²/4, le message le dit précisément, avec les
nombres de l'exercice en cours. Chaque corrigé se déroule en six étapes : ce que dit
l'énoncé, quelle relation et pourquoi, les conversions, le remplacement, le calcul, la
vérification.

### Les vidéos

Chaque fiche a son onglet vidéo, avec la marche à suivre :

1. un bouton ouvre la **recherche YouTube déjà remplie** avec le titre de la fiche ;
2. on choisit une vidéo et on l'ouvre ;
3. on copie l'adresse depuis la barre du navigateur, et on la colle dans l'application.

YouTube (par son domaine sans cookie), Vimeo, Dailymotion et les fichiers `.mp4` sont
acceptés ; le reste est refusé avec une explication. L'aperçu se fait à la frappe.

> **Aucun lien n'est fourni d'avance**, et c'est délibéré : une adresse de vidéo inventée
> mène à une page morte, ce qui serait pire que pas de vidéo du tout.

---

## Installation

Prérequis : Python 3.9 ou plus récent.

```bash
pip install -r requirements.txt
```

## Lancement

```bash
streamlit run app.py
```

Le navigateur s'ouvre sur `http://localhost:8501`.

---

## Arborescence

```
bts-cpi/
├── app.py                  LE fichier exécuté par `streamlit run` : tout le code et
│                            tout le contenu (cours, quiz, schémas, calculateurs, pages)
├── requirements.txt        dépendances minimales (streamlit, pandas)
└── README.md
```

**Pour modifier l'application, c'est toujours `app.py` qu'il faut éditer.** Les anciennes
versions modulaires (`options.py`, `methodes.py`, `figures.py`, `materiaux.py`, `iso286.py`,
`quiz.py`, `cours_debutant.py`, `cours_complements.py`, `cours_bloc_1_2.py`, `cours_bloc_3_4.py`,
`cours_bloc_5_6.py`) ont été retirées du dépôt le 2026-09-04 : leur contenu avait été
progressivement recopié et enrichi directement dans `app.py`, elles n'étaient plus importées par
le programme depuis longtemps et avaient divergé de leur contenu d'origine. Elles restent
consultables dans l'historique Git si besoin (`git log --diff-filter=D`).

## Enregistrement de la progression

Fiches lues, notes, scores de quiz, contrôles, cartes de révision et vidéos sont
enregistrés dans `progression.json`, créé à côté de `app.py`. Pour repartir de zéro,
supprimer ce fichier.

> Sur Streamlit Community Cloud, le disque est réinitialisé à chaque redémarrage de
> l'application : la progression y est conservée tant que l'application tourne, mais pas
> au-delà d'un redéploiement.

## Note d'usage

Les calculateurs donnent un **minimum théorique**, jamais une cote de plan. Le diamètre
réel d'un arbre sort de la combinaison des sollicitations, des concentrations de
contrainte, des composants standards disponibles et de la tenue en fatigue. C'est un point
rappelé dans plusieurs corrigés et dans les fiches méthode.
