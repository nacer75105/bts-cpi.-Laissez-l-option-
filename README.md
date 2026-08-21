# BTS CPI — Application de révision et de calcul

Application Streamlit destinée à un étudiant entrant en 1re année de BTS Conception de Produits
Industriels. Elle regroupe le cours complet du référentiel, des quiz interactifs et les
calculateurs utilisés en bureau d'études.

## Contenu

**18 fiches de cours** réparties en 6 blocs, chacune avec 5 onglets : cours théorique, formules et
unités, exemple industriel chiffré, exercice type examen, corrigé pas à pas.

| Bloc | Thème | Fiches |
|---|---|---|
| 1 | Analyse fonctionnelle et lecture de plan | 1.1 à 1.3 |
| 2 | Tolérancement dimensionnel et ajustements ISO | 2.1 à 2.3 |
| 3 | Matériaux : familles, désignation, traitements | 3.1 à 3.3 |
| 4 | Résistance des matériaux | 4.1 à 4.3 |
| 5 | CAO et modélisation 3D | 5.1 à 5.3 |
| 6 | Liaisons mécaniques et conception | 6.1 à 6.3 |

**7 pages dans l'application :**

1. **Tableau de bord** — progression, blocs, réflexes méthodologiques
2. **Cours** — les 18 fiches, case « fiche lue », notes personnelles
3. **Quiz interactif** — 85 questions sur 10 thèmes, correction immédiate avec explication, score /20
4. **Calculateur d'ajustements ISO** — tables ISO 286 complètes de 0 à 500 mm, détail du calcul
   pas à pas, contrôle de conformité d'une pièce mesurée, ajustements recommandés
5. **Calculateurs RDM** — traction, cisaillement et matage, torsion, flexion (5 cas de charge),
   flambage, flexion + torsion combinées (Tresca et von Mises)
6. **Base matériaux** — 33 nuances, comparateur, indices de performance (Re/ρ, E/ρ, √E/ρ)
7. **Ma progression** — historique des quiz, fiches lues, graphiques

## Installation

Prérequis : Python 3.9 ou plus récent.

```bash
cd bts_cpi
pip install -r requirements.txt
```

## Lancement

**Windows** : double-cliquer sur `lancer.bat`

**Linux / macOS** :
```bash
./lancer.sh
```

**Ou manuellement** :
```bash
streamlit run app.py
```

Le navigateur s'ouvre sur `http://localhost:8501`.

## Enregistrement de la progression

Les fiches lues, les notes personnelles et les scores de quiz sont sauvegardés dans
`progression.json`, créé automatiquement à côté de `app.py`. Pour repartir de zéro, supprimer
ce fichier.

## Arborescence

```
bts_cpi/
├── app.py                      application principale
├── requirements.txt
├── lancer.bat / lancer.sh      scripts de lancement
├── test_validation.py          43 tests de calcul (ISO 286 et RDM)
├── test_pages.py               tests de chargement des 7 pages
└── donnees/
    ├── iso286.py               tables ISO 286-1 et 286-2
    ├── materiaux.py            base matériaux + moteur de calcul RDM
    ├── quiz.py                 85 questions
    ├── cours_bloc_1_2.py
    ├── cours_bloc_3_4.py
    └── cours_bloc_5_6.py
```

## Vérification

```bash
python3 test_validation.py   # 43 tests : valeurs ISO officielles et corrigés des fiches
python3 test_pages.py        # chargement des 7 pages et des 18 fiches
```

## Note d'usage

Les calculateurs donnent un **minimum théorique**, jamais une cote de plan. Le diamètre réel d'un
arbre sort de la combinaison des sollicitations, des concentrations de contrainte, des composants
standards disponibles et de la tenue en fatigue. C'est un point rappelé dans plusieurs corrigés.
