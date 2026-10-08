# Corrections du brouillon 1.9 après relecture pédagogique (bloquants B1-B5 et améliorations retenues).
import os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'brouillon_1_9.py')
c = open(P, encoding='utf-8').read()


def R(a, b):
    global c
    assert c.count(a) == 1, (a[:70], c.count(a))
    c = c.replace(a, b)


# --- § 1 : image des vues, lexique, correspondances
R("""SysML est un langage normalisé par l'**OMG** (*Object Management Group*) ; la notation de cette fiche suit sa
spécification (version 1.6). Il complète l'analyse fonctionnelle des fiches 1.1 à 1.8 (bête à cornes,
pieuvre, FAST, cahier des charges) : celle-ci décrit le besoin et les fonctions d'une pièce ou d'un produit,
SysML décrit un **système** complet, avec ses exigences, ses constituants et son comportement.
""", """SysML est un langage normalisé par l'**OMG** (*Object Management Group*, un organisme international qui publie
la norme) ; la notation de cette fiche suit sa spécification officielle.

*Image à garder : un dessin technique montre la même pièce en vue de face, de dessus et en coupe ; aucune vue ne
suffit seule, c'est leur ensemble qui décrit la pièce. SysML fait pareil pour un système : plusieurs diagrammes
du même système, chacun répondant à une question.*

**Les mots à connaître, en français courant :**

| Mot | En français courant |
|---|---|
| **bloc** | un constituant (pièce, sous-ensemble, carte électronique, logiciel) : une **référence** |
| **partie** | un **exemplaire** d'un bloc, monté à une place précise du système |
| **multiplicité** | combien d'exemplaires (la colonne « Nb » d'une nomenclature) |
| **port** | un point de branchement : prise, bornier, arbre de sortie |
| **connecteur** | le trait qui relie deux ports : un câble, un arbre, une liaison radio |
| **flux d'éléments** | ce qui circule sur un connecteur : énergie, matière, information |
| **ligne de vie** | la « colonne » d'un élément dans un scénario ; elle descend avec le temps |
| **garde** | une condition qui doit être vraie pour qu'un changement d'état ait lieu |

**Pour se repérer avec ce que vous connaissez déjà** (correspondances approximatives, pas des équivalences) :
bête à cornes et pieuvre → **uc** (qui utilise le système, pour quoi) ; critère et niveau du cahier des charges →
**req** (une exigence chiffrée) ; nomenclature → **bdd** ; chaîne d'énergie et d'information → **ibd**.
""")

# --- § 2 : les mots entre crochets
R("""motorisé ». En trois mots, on sait de quoi parle le diagramme.
""", """motorisé ». En trois mots, on sait de quoi parle le diagramme. Entre crochets, le type de ce qui est décrit :
[block] = un constituant, [package] = un « classeur » qui regroupe des éléments, [interaction] = un scénario
d'échanges. Ce mot entre crochets est secondaire et peut être absent (« stm Portail ») : l'abréviation et le nom
suffisent pour s'orienter.
""")

# --- § 3 : relations, règle unique, critère et niveau
R("""- Les **relations** sont des flèches en pointillé, avec un mot-clé :
  - «**satisfy**» : un élément de conception (un bloc) **satisfait** l'exigence — la flèche va du bloc vers
    l'exigence (« le motoréducteur satisfait la durée d'ouverture ») ;
  - «**verify**» : un cas de test **vérifie** l'exigence — la flèche va du test vers l'exigence ;
  - «**deriveReqt**» : une exigence est **déduite** d'une autre — la flèche va de l'exigence dérivée vers
    l'exigence source ;
  - «**refine**» (précise), «**trace**» (lien de traçabilité), «**copy**» (copie) existent aussi.
""", """- Les **relations** sont des flèches en pointillé, avec un mot-clé. **Règle unique : la flèche pointe vers
  l'exigence de référence** — l'élément qui la satisfait, le test qui la vérifie, l'exigence qui en est déduite,
  tous la « montrent du doigt » :
  - «**satisfy**» : un **élément de conception** (une solution retenue, ici un bloc) **satisfait** l'exigence —
    la flèche va du bloc vers l'exigence (« le motoréducteur satisfait la durée d'ouverture ») ;
  - «**verify**» : un cas de test **vérifie** l'exigence — la flèche va du test vers l'exigence (un essai
    chronométré d'ouverture vérifierait l'exigence 1.1) ;
  - «**deriveReqt**» : une exigence est **déduite** d'une autre — la flèche va de l'exigence dérivée vers
    l'exigence source (pour un vantail de 4 m, « vitesse du vantail au moins 0,2 m/s » se déduit de
    « ouverture en 20 s au plus » : 4 m ÷ 20 s = 0,2 m/s) ;
  - d'autres mots-clés existent («refine», «trace», «copy») : si vous en croisez un, lisez-le comme un lien
    entre deux éléments dont le mot-clé dit la nature ; inutile de les apprendre.
""")
R("""et le réducteur doivent le permettre ; un essai le vérifiera). C'est la même idée que le critère, le niveau et
la flexibilité du cahier des charges fonctionnel (fiche 1.4).
""", """et le réducteur doivent le permettre ; un essai le vérifiera). C'est la même idée que le cahier des charges
fonctionnel (fiche 1.4) : dans « Ouverture complète en 20 s au plus », le **critère** est la durée d'ouverture et
le **niveau** est 20 s au maximum.
""")

# --- § 4 : bdd
R("""- Un **bloc** («block») est un constituant du système : une pièce, un sous-ensemble, un logiciel, une personne
  même.
- Le **losange noir**, côté bloc « composé », se lit « **est composé de** » : le portail est composé d'un vantail,
  d'un motoréducteur, d'une carte de commande…
- Les **nombres** près des blocs (les **multiplicités**) disent **combien** d'exemplaires : « 4 » près du galet =
  4 galets de guidage.
- Un bloc peut lui-même être décomposé : le motoréducteur contient un moteur.

*C'est une **nomenclature** dessinée : lire un bdd, c'est savoir de quels constituants le système est fait,
et combien il en faut.*
""", """- Un **bloc** («block») est un constituant du système : une pièce, un sous-ensemble, une carte, un logiciel.
- Le **losange noir** est collé au **tout** ; les traits partent vers les **morceaux**. On lit en partant du
  losange : « le portail **est composé de** » un vantail, un motoréducteur, une carte de commande…
- Les **nombres** près des blocs (les **multiplicités**) disent **combien** d'exemplaires : « 4 » près du galet =
  4 galets de guidage.
- Un bloc peut lui-même être décomposé : le motoréducteur contient un moteur.

*C'est une **nomenclature** dessinée. Le bdd du portail, transposé :*

| Nb | Désignation |
|---|---|
| 1 | Vantail |
| 1 | Motoréducteur (dont 1 moteur) |
| 1 | Carte de commande |
| 4 | Galet de guidage |
| 1 | Capteur d'obstacle |
""")

# --- § 5 : ibd (B3 bloc/partie, B4 réseau et capteur, A8, A9)
R("""- Le cadre est le système (ici le portail) ; à l'intérieur, chaque **partie** est un rectangle « nom : Bloc »
  (« moteur : Motoréducteur » = la partie appelée moteur, qui est un motoréducteur).
- Les **ports** sont les petits carrés sur le bord des blocs : les points de passage (une prise, un arbre de
  sortie, une connexion).
- Les **connecteurs** sont les traits qui relient les ports : les liaisons physiques ou logiques.
- Une **pointe de flèche noire posée sur un connecteur** est un **flux d'éléments** : elle indique **ce qui
  circule** et dans quel sens — énergie électrique de la carte vers le moteur, mouvement du moteur vers le
  vantail, ordre radio de l'extérieur vers la carte.

*Le bdd dit « de quoi c'est fait » ; l'ibd dit « comment c'est branché ». On y retrouve la **chaîne d'énergie**
(fiche 6.20 : alimenter, distribuer, convertir, transmettre) et la **chaîne d'information** (acquérir, traiter,
communiquer) : lire un ibd, c'est suivre l'énergie, la matière et l'information à travers le système.*
""", """- Le cadre est le système (ici le portail) ; à l'intérieur, chaque **partie** est un rectangle « nom : Bloc »
  (« motoréducteur : Motoréducteur » se lit « l'exemplaire appelé motoréducteur, qui est un Motoréducteur »).
- **Bloc ou partie ?** Un **bloc**, c'est une **référence de catalogue** (« Motoréducteur », comme « Vis CHc
  M8×20 ») ; une **partie**, c'est **un exemplaire monté à une place précise** de ce système (la vis repère 12
  qui tient le carter). Le bdd parle de références, l'ibd parle d'exemplaires montés et branchés.
- Les **ports** sont les petits carrés sur le bord des parties ou du cadre : les points de branchement (une
  prise, un bornier, un arbre de sortie).
- Les **connecteurs** sont les traits qui relient les ports : un câble, un arbre, un engrènement, ou une liaison
  sans contact comme la radio.
- Une **pointe de flèche noire posée sur un connecteur** est un **flux d'éléments** : comme la flèche sur une
  canalisation, elle dit **ce qui circule** et dans quel sens — énergie électrique du réseau vers la carte, puis
  de la carte vers le motoréducteur ; mouvement du motoréducteur vers le vantail ; présence d'obstacle du capteur
  vers la carte ; ordre radio de la télécommande vers la carte. Le réseau et la télécommande sont **hors du
  système étudié** : leurs flux arrivent par des ports posés sur le bord du cadre.

*On y lit la **chaîne d'énergie** (fiche 6.20) : le réseau **alimente**, la carte **distribue**, le
motoréducteur **convertit** (moteur) et **transmet** (réducteur), le vantail est mis en mouvement. Et la
**chaîne d'information** : l'ordre radio et la présence d'obstacle arrivent à la carte, qui commande le moteur.*

**Au premier coup d'œil :** le **bdd** est un **arbre** — un bloc en haut, ses constituants en dessous, des
losanges noirs, des nombres ; l'**ibd** est un **plan de branchement** — des boîtes rangées DANS le cadre du
système, des petits carrés sur leurs bords, des traits entre eux, des pointes noires, et des noms de la forme
« nom : Bloc ». *Le bdd est la liste des pièces d'un kit ; l'ibd est le schéma de câblage du même kit.*
""")

# --- § 6 : comportement (B1 include, B2 garde, B4 fin de course, A10)
R("""(« Ouvrir », « Fermer »). Un trait relie l'acteur aux services qu'il utilise. Une flèche pointillée «include»
dit qu'un cas en inclut un autre à chaque fois (ouvrir inclut toujours détecter un obstacle). *C'est l'équivalent
SysML de la frontière de l'étude et des fonctions de service (bête à cornes, pieuvre).*
""", """(« Ouvrir », « Fermer »). Un trait relie l'acteur aux services qu'il utilise. Une flèche pointillée «include»
dit qu'un cas en inclut un autre à chaque fois : ici, **fermer** le portail inclut toujours **détecter un
obstacle** — on ne referme jamais sans surveiller le passage. La flèche part du cas qui inclut et pointe vers le
cas inclus. *C'est l'équivalent SysML de la frontière de l'étude et des fonctions de service (bête à cornes,
pieuvre).*
""")
R("""**Diagramme de séquence (sd) — dans quel ordre.** Chaque élément a une **ligne de vie** verticale en
pointillé ; les **messages** sont des flèches horizontales de l'émetteur vers le récepteur ; **le temps s'écoule
de haut en bas**. On lit l'histoire d'un scénario : l'utilisateur appuie, la carte démarre le moteur, le capteur
de fin de course prévient la carte, la carte arrête le moteur.
""", """**Diagramme de séquence (sd) — dans quel ordre.** Chaque élément a une **ligne de vie** verticale en
pointillé : elle représente l'élément pendant toute la durée du scénario (d'où « de vie »). Les **messages** sont
des flèches horizontales de l'émetteur vers le récepteur ; **le temps s'écoule de haut en bas**, comme dans un fil
de messages de groupe où chaque colonne est un interlocuteur et le plus ancien message est en haut. Les
parenthèses marquent un ordre envoyé ; ce qui est dedans le précise (« démarrer(sens) » = démarrer, dans le sens
ouverture ou fermeture). On lit l'histoire d'un scénario : l'utilisateur appuie, la carte démarre le
motoréducteur, le motoréducteur signale la fin de course à la carte, la carte l'arrête.
""")
R("""**Diagramme d'états-transitions (stm) — dans quel état.** Les **états** sont des rectangles aux coins arrondis
(« Fermé », « En ouverture », « Ouvert ») ; le **disque noir** marque l'état initial ; les **flèches** sont les
**transitions**, étiquetées « **événement [garde] / effet** » : l'événement qui déclenche le passage, une
condition entre crochets (facultative), l'action réalisée (facultative). *Exemple : « appui [portail fermé] /
démarrer moteur ».* On lit : « depuis Fermé, un appui fait passer En ouverture ».
""", """**Diagramme d'états-transitions (stm) — dans quel état.** Les **états** sont des rectangles aux coins arrondis
(« Fermé », « En ouverture », « Ouvert ») ; le **disque noir** marque l'état initial ; les **flèches** sont les
**transitions**, étiquetées « **événement [garde] / effet** » : l'événement qui déclenche le passage, une
condition entre crochets (facultative), l'**effet** — ce que le système fait au moment où il change d'état
(facultatif). *Exemple : « appui [aucun obstacle] / démarrer moteur ».* On lit : « depuis Fermé, un appui fait
passer En ouverture, **à condition** qu'aucun obstacle ne soit détecté ; au moment du passage, la carte démarre le
moteur ». La garde, c'est comme un gardien à l'entrée : l'événement frappe à la porte, et la transition n'a lieu
que si le gardien dit oui. Si un obstacle est là, l'appui ne fait rien : le portail reste Fermé. *Le diagramme
de la figure est simplifié : la fermeture n'y est pas représentée.*
""")

# --- § 7 : SADT, correspondance sur le portail (A11, sans affirmation non sourcée)
R("""La fiche 1.5 présente le **SADT** (actigramme). Le référentiel 2016 du BTS CPI ne cite plus le SADT : pour
décrire un système, il demande de lire des diagrammes **SysML** (S1.1). Les deux ne se superposent pas
exactement : l'actigramme SADT montre une **activité** avec ses entrées, ses sorties, ses contrôles et ses
supports ; en SysML, ce qui circule entre les constituants se lit plutôt sur l'**ibd** (flux d'éléments), et le
déroulement sur les diagrammes de **séquence** et d'**états**.
""", """La fiche 1.5 présente le **SADT** (actigramme). Le référentiel 2016 du BTS CPI ne cite plus le SADT : pour
décrire un système, il demande de lire des diagrammes **SysML** (S1.1). La fiche 1.5 est gardée comme
complément, pas à réviser pour l'examen.

Les deux ne se superposent pas exactement. Sur le portail, un actigramme « Ouvrir le portail » mettrait tout sur
**une seule boîte** : entrée « portail fermé », sortie « portail ouvert » ; en haut, W (énergie électrique) et E
(ordre de l'utilisateur) ; en bas, le mécanisme (motoréducteur, carte). SysML **répartit** ces informations sur
plusieurs diagrammes : les états Fermé → Ouvert sur le **stm**, l'énergie et l'ordre radio comme flux sur l'**ibd**,
le motoréducteur et la carte comme blocs du **bdd**. *Attention : en SADT, l'énergie va en haut, jamais en
entrée ; sur un ibd, elle circule sur un connecteur comme n'importe quel flux. Ce n'est pas une contradiction :
ce sont deux conventions différentes.*
""")

# --- § 8 erreur 2 : repère visuel
R("""2. **Confondre bdd et ibd** : le bdd dit de quoi le système est composé ; l'ibd dit comment ses parties sont
   reliées.""", """2. **Confondre bdd et ibd** : le bdd (un arbre, des losanges, des nombres) dit de quoi le système est
   composé ; l'ibd (des boîtes « nom : Bloc » dans le cadre, des ports, des connecteurs) dit comment ses parties
   sont reliées.""")

# --- cas industriel : capteur présent dans le bdd
R("""  l'exigence 1.2 (« arrêt si un obstacle est détecté ») impose qu'un capteur et la carte agissent sur le moteur.""",
  """  l'exigence 1.2 (« arrêt si un obstacle est détecté ») impose que le capteur d'obstacle et la carte agissent sur
  le moteur.""")
R("""- **ibd** : le motoréducteur reçoit l'énergie électrique de la carte et transmet le mouvement au vantail. Le
  support doit donc laisser passer le câble d'alimentation et garder l'alignement entre la sortie du réducteur et
  la crémaillère du vantail.""", """- **ibd** : le motoréducteur reçoit l'énergie électrique de la carte et transmet le mouvement au vantail. Le
  support doit donc laisser passer le câble d'alimentation et garder l'alignement entre la sortie du réducteur et
  la crémaillère du vantail (une crémaillère n'est pas dessinée sur l'ibd simplifié de la fiche : c'est le
  dossier complet qui la précise).""")

# --- exercice / corrigé
R("""**6.** Dans le diagramme de séquence, quel message la carte envoie-t-elle en premier au moteur ? Comment sait-on
qu'il précède « arrêter() » ?""", """**6.** Dans le diagramme de séquence, quel message la carte envoie-t-elle en premier au motoréducteur ? Comment
sait-on qu'il précède « arrêter() » ?""")
R("""**5.** L'événement « **appui** » (sur la télécommande).""",
  """**5.** L'événement « **appui** » (sur la télécommande), à condition qu'aucun obstacle ne soit détecté (la garde
[aucun obstacle]) ; l'effet est « démarrer moteur ».""")
R("""#### 5. Le calcul
""", """#### 5. Le calcul (ici : la lecture)
""")

# --- at178 : indice bdd, télécommandes -> capteur
R(""""indice": "bdd = block definition diagram.",""",
  """"indice": "bdd = diagramme de définition de blocs : la liste des constituants.",""")
R("""            {"type": "numerique", "label": "Nombre total de télécommandes et de galets",
             "unite": "pièces", "attendu": 6, "tol": 0.1,
             "consigne": "Combien faut-il commander de galets et de télécommandes au total pour un portail ?",
             "indice": "Additionne les deux multiplicités.",
             "pieges": [(2, "2 : ce sont les télécommandes seules. Ajoute les 4 galets.")],
             "aide": "4 galets + 2 télécommandes = 6."},""",
  """            {"type": "numerique", "label": "Nombre total de galets et de capteurs",
             "unite": "pièces", "attendu": 5, "tol": 0.1,
             "consigne": "Combien faut-il commander de galets de guidage et de capteurs d'obstacle au total pour un "
                         "portail ?",
             "indice": "Additionne les deux multiplicités.",
             "pieges": [(4, "4 : ce sont les galets seuls. Ajoute le capteur d'obstacle (multiplicité 1).")],
             "aide": "4 galets + 1 capteur = 5."},""")
R(""""calcul": "**bdd** = composition du portail ; **4 galets** ; **6 pièces** (4 galets + 2 télécommandes) ; \"""",
  """"calcul": "**bdd** = composition du portail ; **4 galets** ; **5 pièces** (4 galets + 1 capteur) ; \"""")

# --- at179 : figure, garde, messages
R(""""figure": "sysml_ibd",
        "vocabulaire": [
            ("Flux d'éléments",""", """"figure": "sysml_comportement",
        "vocabulaire": [
            ("Flux d'éléments",""")
R("""             "consigne": "Le diagramme de séquence « Ouvrir » montre appuyer(), démarrer(sens), fin de course, "
                         "arrêter(). Combien de messages comporte ce scénario ?",""",
  """             "consigne": "Le diagramme de séquence « Ouvrir » montre appuyer(), démarrer(sens), fin de course, "
                         "arrêter(). Combien de messages comporte ce scénario ?",""")
R("""             "pieges": [(3, "3 : n'oublie pas le message du moteur vers la carte (fin de course).")],""",
  """             "pieges": [(3, "3 : n'oublie pas le message du motoréducteur vers la carte (fin de course).")],""")
R("""                         "l'étiquette « appui [portail fermé] / démarrer moteur ». Que représente « [portail fermé] » ?",""",
  """                         "l'étiquette « appui [aucun obstacle] / démarrer moteur ». Que représente « [aucun obstacle] » ?",""")
R(""""calcul": "**énergie électrique de la carte vers le motoréducteur** ; **4 messages** ; ordre lu **de haut en "
                     "bas** ; **[portail fermé] = garde**.",""",
  """"calcul": "**énergie électrique de la carte vers le motoréducteur** ; **4 messages** ; ordre lu **de haut en "
                     "bas** ; **[aucun obstacle] = garde** : sans elle vraie, l'appui ne fait rien.",""")

# --- quiz
R("""    ("Sur un bdd, un losange noir relie le bloc « Portail » à quatre autres blocs. Comment le lire ?",""",
  """    ("Sur un bdd, un losange noir relie le bloc « Portail » à plusieurs autres blocs. Comment le lire ?",""")
R("""    ("Dans un diagramme d'états, une transition porte « appui [portail fermé] / démarrer moteur ». Quel est "
     "l'événement déclencheur ?",
     ["appui", "portail fermé", "démarrer moteur", "Il n'y en a pas"], 0,
     "Syntaxe : événement [garde] / effet. « portail fermé » est la condition (garde), « démarrer moteur » l'action.",""",
  """    ("Dans un diagramme d'états, une transition porte « appui [aucun obstacle] / démarrer moteur ». Quel est "
     "l'événement déclencheur ?",
     ["appui", "aucun obstacle", "démarrer moteur", "Il n'y en a pas"], 0,
     "Syntaxe : événement [garde] / effet. « aucun obstacle » est la condition (garde), « démarrer moteur » l'effet.",""")

open(P, 'w', encoding='utf-8').write(c)
print('ok')
