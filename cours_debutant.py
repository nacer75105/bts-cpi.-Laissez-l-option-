# -*- coding: utf-8 -*-
"""
cours_debutant.py — Versions longues et progressives des fiches de cours.

Principe de rédaction, identique pour toutes les fiches :
    1. le problème concret d'abord, sans aucun mot technique
    2. l'idée en français courant
    3. le mot savant seulement à ce moment-là
    4. un exemple entièrement chiffré, tous les calculs écrits
    5. l'erreur que tout débutant commet
    6. un récapitulatif de fin

Les marqueurs [[FIG:cle]] appellent les schémas de figures.py.

Pour réécrire une autre fiche : ajouter une entrée dans FICHES ci-dessous,
avec l'identifiant exact de la fiche ("3.1", "4.2"...). Rien d'autre à modifier :
app.py applique automatiquement ce qui se trouve ici.
"""

FICHES = {}

# ===========================================================================
# FICHE 1.1 — ANALYSE DU BESOIN ET CAHIER DES CHARGES FONCTIONNEL
# ===========================================================================

FICHES["1.1"] = {"cours": """
### 1. Une histoire vraie, pour commencer

Un client téléphone à un bureau d'études et dit :

> « J'ai besoin d'une équerre en inox de 100 × 60, avec deux trous taraudés M6. »

Le dessinateur débutant ouvre SolidWorks et dessine l'équerre. Trois semaines plus tard,
la pièce est fabriquée, livrée… et le client rappelle : **ça ne marche pas.**

Que s'est-il passé ? Le client n'avait pas besoin d'une équerre. Il avait besoin de
**tenir un capteur en face des bouteilles qui défilent sur sa ligne d'embouteillage**.
L'équerre, c'était *sa* solution à lui — une idée qu'il avait eue, pas un besoin.
Et sa solution était mauvaise : à cet endroit, la ligne vibre, et l'équerre a bougé.

Si le dessinateur avait posé une seule question — « pour faire quoi ? » — il aurait
proposé un support avec un réglage et un contre-écrou, et le problème aurait été réglé.

**Toute la première partie de l'année de BTS CPI sert à ne plus jamais faire cette erreur.**

### 2. La distinction qui commande tout le reste

Il faut apprendre à séparer deux choses que tout le monde confond :

| On exprime… | Exemple | Comment ça s'appelle |
|---|---|---|
| ce que le produit doit **faire** | « maintenir la pièce pendant l'usinage » | une **fonction** — le *quoi* |
| **comment** il le fait | « avec un vérin pneumatique Ø32 » | une **solution technique** — le *comment* |

Une fonction s'écrit toujours de la même façon : **un verbe à l'infinitif + un complément**.
Aucun nom de composant, aucune marque, aucun matériau.

- Correct : « transmettre un couple de 12 N·m entre le moteur et le réducteur »
- Incorrect : « utiliser une clavette parallèle 8 × 7 » — ça, c'est déjà une solution

**Pourquoi c'est si important ?** Parce qu'en écrivant la solution dans le cahier des charges,
on s'interdit d'en trouver une meilleure. « Transmettre un couple » laisse la porte ouverte à
la clavette, aux cannelures, au frettage, à la goupille. « Utiliser une clavette » ferme
la porte avant même d'avoir cherché.

On dit qu'un cahier des charges bien écrit est **neutre technologiquement**.

### 3. La bête à cornes : cadrer le besoin en trois questions

C'est le premier outil, et le plus simple. Trois questions, dans cet ordre :

[[FIG:bete_a_cornes]]

La réponse à la troisième question — le but — s'appelle la **fonction globale** du produit.
C'est la phrase qu'on écrira tout en haut du cahier des charges.

Attention à un piège classique : **le service est rendu à celui qui a le problème**, pas
forcément à celui qui subit l'action. Pour un distributeur de croquettes, le produit rend
service **au propriétaire** (c'est lui qui part en week-end et qui achète l'appareil), pas
au chat. Le chat, lui, n'est même pas au courant.

**Valider le besoin — trois questions à connaître par cœur pour l'examen :**

1. *Pourquoi ce besoin existe-t-il ?* → sa cause
2. *Qu'est-ce qui pourrait le faire disparaître ?* → sa fin de vie
3. *Ce risque est-il probable ?* → sa robustesse

Exemple : le besoin d'un support de tablette dans un atelier disparaîtrait si l'entreprise
passait au plan papier ou aux lunettes connectées. Est-ce probable à court terme ? Non.
Le besoin est donc robuste, le projet a un sens.

### 4. Le diagramme pieuvre : trouver TOUTES les fonctions

La bête à cornes donne une seule fonction, la principale. Or un produit doit satisfaire bien
d'autres exigences : tenir dans un espace donné, résister à l'huile, respecter un budget,
être conforme à une norme…

On dessine donc le produit au centre, et tout ce qui l'entoure autour. Ces éléments
s'appellent les **éléments du milieu extérieur**, ou EME.

[[FIG:diagramme_pieuvre]]

Deux types de liaisons, et la différence tombe à tous les contrôles :

- **Fonction principale (FP)** : elle relie **deux** EME **en traversant** le produit.
  C'est la raison d'être du produit. *« Permettre à l'opérateur de serrer la pièce »* relie
  l'opérateur et la pièce : sans le produit, le lien n'existe pas.
- **Fonction contrainte (FC)** : elle relie le produit à **un seul** EME. C'est une obligation
  que le produit subit. *« Résister aux copeaux et au liquide de coupe »*, *« se fixer sur la
  table de la machine »*, *« ne pas dépasser 80 € »*.

Un produit a en général **une ou deux FP**, et **beaucoup de FC** — cinq, dix, parfois plus.
Si vous trouvez six FP, c'est presque sûrement que vous avez mal identifié les EME.

**Comment ne rien oublier ?** Passez en revue une liste type, toujours la même :
l'utilisateur, la matière d'œuvre, l'énergie, le support ou le bâti, l'ambiance
(température, humidité, poussière, produits chimiques), la maintenance, les normes et
la sécurité, le budget, l'esthétique, le recyclage en fin de vie.

### 5. Caractériser une fonction : critère, niveau, flexibilité

Une fonction non chiffrée ne sert à rien. « Le carter doit être solide » n'est ni vérifiable,
ni contestable, ni utile à un fournisseur. Chaque fonction reçoit donc trois éléments :

| Élément | Ce que c'est | Exemple |
|---|---|---|
| **critère** | la grandeur qu'on va observer | l'effort de serrage |
| **niveau** | la valeur à atteindre | 5 000 N |
| **flexibilité** | la tolérance acceptée sur ce niveau | ± 10 % |

À quoi s'ajoute une **classe de flexibilité**, qui dit à quel point c'est négociable :

- **F0** — impératif, aucune négociation possible (une exigence de sécurité, par exemple)
- **F1** — peu négociable
- **F2** — négociable
- **F3** — simple souhait

Reprenons l'exigence floue du début, et rendons-la exploitable :

> ❌ « le carter doit être solide et facile à nettoyer »

> ✅ **FC1 — résister aux chocs** : critère = énergie de choc, niveau = 5 J sans déformation
> permanente, flexibilité = F0.
> **FC2 — permettre le nettoyage** : critère = temps de nettoyage complet, niveau = moins de
> 10 minutes, aucun angle rentrant inférieur à 90°, flexibilité = F1.

Ce tableau n'est pas de la paperasse : **c'est lui qui servira à valider le produit à la fin**.
En fin de projet, on reprend le cahier des charges ligne par ligne, on mesure, et on coche.

### 6. Le FAST : passer enfin aux solutions

Une fois les fonctions écrites et chiffrées, on a le droit de chercher des solutions. Le
diagramme FAST sert à faire ce passage proprement, sans sauter d'étape.

[[FIG:diagramme_fast]]

On le lit de gauche à droite en se posant trois questions :

- **Pourquoi ?** — on remonte vers la gauche, vers le besoin
- **Comment ?** — on descend vers la droite, vers la solution
- **Quand ?** — les fonctions qui doivent être assurées en même temps, en branches verticales

Le nom d'un composant réel n'apparaît **qu'à l'extrémité droite**. Si vous écrivez
« roulement à billes » dans la première colonne, le FAST est faux.

### 7. Ce que contient le cahier des charges fonctionnel (CdCF)

C'est le document qui rassemble tout, et il est **contractuel** : c'est sur lui que le client
jugera le produit, et sur lui qu'on comparera les offres des fournisseurs.

1. Le contexte et le besoin (issus de la bête à cornes)
2. La liste des FP et FC (issues de la pieuvre)
3. Pour chacune : critère, niveau, flexibilité
4. Les contraintes de délai, de coût, de norme
5. Les conditions de recette : qui vérifie, comment, avec quel moyen de mesure

### 8. Les quatre erreurs classiques

1. **Écrire une solution à la place d'une fonction.** Dès qu'un nom de composant apparaît,
   c'est perdu.
2. **Oublier de chiffrer.** « Léger », « silencieux », « robuste » ne veulent rien dire.
   Combien de kilos ? Combien de décibels, mesurés à quelle distance ?
3. **Confondre FP et FC.** Une fonction qui ne relie le produit qu'à un seul élément
   extérieur est forcément une contrainte, jamais une fonction principale.
4. **Se tromper d'utilisateur.** Le service est rendu à celui qui a le problème et qui paie.

### 9. À retenir en cinq lignes

- On écrit ce que le produit doit **faire**, jamais **comment** il le fera.
- Une fonction = un verbe à l'infinitif + un complément.
- Bête à cornes : à qui, sur quoi, dans quel but.
- Pieuvre : FP relie deux EME à travers le produit, FC en relie un seul.
- Chaque fonction : un critère, un niveau chiffré, une flexibilité.
"""}


# ===========================================================================
# FICHE 1.2 — LECTURE DE PLAN : PROJECTIONS, COUPES ET SECTIONS
# ===========================================================================

FICHES["1.2"] = {"cours": """
### 1. À quoi sert un plan, exactement ?

Imaginez : vous avez une pièce dans les mains et vous devez la faire fabriquer par un atelier
à 800 km, sans jamais lui parler. Comment décrire précisément un objet en trois dimensions
sur une feuille plate ?

C'est tout le problème du dessin technique. Et la réponse tient en une idée : **on ne dessine
pas la pièce en perspective, on la regarde depuis plusieurs côtés et on note ce qu'on voit.**

Un plan n'est pas une illustration : c'est un **contrat**. Ce qui y est écrit sera fabriqué.
Ce qui n'y est pas écrit ne le sera pas. D'où des règles internationales très strictes : un
atelier à Alger, à Lyon ou à Shanghai doit comprendre exactement la même chose.

### 2. Le cube de verre : d'où viennent les vues

Imaginez la pièce enfermée dans un cube de verre. Depuis chaque face du cube, vous regardez
la pièce bien en face, et vous dessinez son contour sur le verre. Puis vous dépliez le cube
à plat sur la table. Vous obtenez jusqu'à six dessins : les **vues**.

[[FIG:projection_europeenne]]

Il y a deux façons de déplier ce cube, et il faut savoir laquelle on a sous les yeux :

- **Méthode européenne** (celle de la France, et celle de vos cours) : la vue se dessine
  **de l'autre côté**. Ce que vous voyez en regardant depuis la gauche se dessine **à droite**.
- **Méthode américaine** : exactement l'inverse. On la rencontre sur beaucoup de documents
  américains et asiatiques.

Comment savoir ? Un petit symbole en forme de cône tronqué figure dans le cartouche. Lire un
plan américain comme un plan européen, c'est fabriquer la pièce **en miroir** : erreur classique,
et coûteuse.

### 3. Choisir la vue de face, et le nombre de vues

La vue de face n'est pas « la vue de devant ». C'est **celle qui montre le plus de choses**,
la pièce étant dans sa position d'utilisation ou de fabrication. Un arbre se dessine
horizontal, comme il sera sur le tour.

Ensuite, règle d'économie : **on dessine le minimum de vues nécessaires**. Souvent deux,
parfois trois. Une pièce de révolution (un axe, une bague) se décrit entièrement avec une
seule vue plus le symbole Ø. Ajouter des vues inutiles alourdit le plan et multiplie les
risques de contradiction entre elles.

### 4. Les traits : quatre familles, pas une de plus

[[FIG:types_de_traits]]

Deux réflexes à prendre tout de suite :

- **tout trou rond et tout arbre possèdent un axe**, tracé en trait mixte fin qui dépasse
  légèrement le contour de part et d'autre. L'oublier est l'erreur la plus fréquente en devoir ;
- **quand deux traits se superposent**, on garde le plus important : le trait fort masque le
  trait fin.

### 5. Le problème des traits cachés — et sa solution

Prenez une pièce percée de plusieurs trous, avec des chambrages et des taraudages. Vue de
l'extérieur, elle devient un buisson de pointillés que plus personne ne sait lire.

La solution est brutale et efficace : **on scie la pièce en deux, et on jette la moitié qui
est entre l'œil et le plan de coupe.**

[[FIG:pourquoi_couper]]

Ce qui était caché devient visible, donc dessiné en trait fort. Les pointillés disparaissent.

**Les hachures.** Les surfaces réellement traversées par la scie reçoivent des hachures à 45°,
en trait continu fin, régulièrement espacées. Le vide, lui, reste blanc — on ne hachure jamais
un trou. Sur un dessin d'ensemble, deux pièces voisines portent des hachures d'inclinaison ou
d'espacement différents ; une même pièce garde partout les mêmes hachures. C'est comme ça
qu'on distingue les pièces les unes des autres.

**Comment on l'indique.** Sur une autre vue, on trace le plan de coupe en trait mixte renforcé
aux extrémités, avec deux flèches indiquant le sens du regard et deux lettres identiques.
La vue obtenue s'appelle alors **COUPE A-A**.

### 6. Les variantes utiles

- **Demi-coupe** : réservée aux pièces symétriques. Une moitié en vue extérieure, l'autre en
  coupe, séparées par l'axe. Deux informations pour le prix d'une seule vue.
- **Coupe locale** : on n'ouvre qu'une petite zone, limitée par un trait fin ondulé. Parfaite
  pour montrer un seul taraudage sans mutiler tout le dessin.
- **Coupe brisée** : le plan de coupe fait un ou plusieurs coudes pour traverser plusieurs
  détails intéressants qui ne sont pas alignés.
- **Section** : on ne dessine **que** la tranche, sans ce qu'il y a derrière. Idéale pour
  montrer la forme d'un profil ou d'une clavette. Sortie (à côté de la vue, contour fort) ou
  rabattue (sur la vue, contour fin).

### 7. Ce qu'on ne coupe JAMAIS dans le sens de la longueur

Par convention internationale, on ne hachure jamais, coupés en long :

> **vis, écrous, rondelles, goupilles, clavettes, arbres pleins, billes et rouleaux de
> roulement, nervures, bras de poulie.**

Pourquoi ? Parce que les hachurer n'apprendrait rien sur leur intérieur — ils sont pleins —
et brouillerait la lecture. Une vis dans l'axe du plan de coupe se dessine donc **entière et
non hachurée**, alors que la pièce percée autour d'elle est hachurée normalement.

En revanche, une coupe **transversale** de ces mêmes éléments est autorisée et fréquente.

### 8. Le cartouche : à lire en premier, toujours

En bas à droite de chaque plan : le titre, l'échelle, le symbole de projection, le format,
l'indice de révision, la matière, le nom, la date. Deux points qui piègent les débutants :

- **l'échelle** s'écrit dessin : réel. 1:2 réduit de moitié, 2:1 agrandit du double. Mais
  attention : **les cotes inscrites sont toujours les cotes réelles**. On lit une cote, on ne
  la mesure jamais à la règle sur la feuille.
- **l'indice de révision** : si vous travaillez avec l'indice B alors que l'atelier a reçu
  l'indice C, vous ne parlez pas de la même pièce.

### 9. Méthode : lire un plan inconnu en six étapes

1. Lire le **cartouche** : titre, échelle, matière, méthode de projection.
2. Repérer la **vue de face** et les vues qui l'accompagnent.
3. Repérer les **coupes** et où passent leurs plans.
4. Suivre **une forme à la fois** d'une vue à l'autre (un trou à la fois, un épaulement à la fois).
5. Lire les **cotes fonctionnelles** : celles qui portent des tolérances serrées sont les
   surfaces qui travaillent.
6. Lire les **états de surface** et les tolérances géométriques : ils disent où est la précision.

### 10. Les erreurs classiques

1. Oublier les axes des trous et des arbres.
2. Mal aligner les vues : une vue de dessus décalée de 3 mm et le plan devient faux.
3. Hachurer un vide, ou hachurer une nervure coupée en long.
4. Mesurer une cote à la règle sur la feuille au lieu de la lire.
5. Ne pas vérifier le symbole de projection sur un plan venu de l'étranger.
"""}


# ===========================================================================
# FICHE 1.3 — COTATION DIMENSIONNELLE ET ÉTATS DE SURFACE
# ===========================================================================

FICHES["1.3"] = {"cours": """
### 1. Coter, c'est donner des ordres à l'atelier

Un dessin sans cotes est un joli croquis : personne ne peut fabriquer avec. Coter, c'est
écrire les dimensions que l'ouvrier devra **obtenir puis contrôler**.

Et attention à l'état d'esprit : on ne cote pas « ce qu'on voit », on cote **ce qui doit être
garanti**. Ce n'est pas la même chose, et c'est ce qui sépare un débutant d'un technicien.

### 2. De quoi une cote est faite

[[FIG:elements_cotation]]

Quelques conventions d'écriture à connaître :

| Écriture | Signification |
|---|---|
| **Ø40** | un diamètre de 40 (surface cylindrique) |
| **R8** | un rayon de 8 (congé ou arrondi) |
| **2 × 45°** | un chanfrein de 2 mm à 45° |
| **M8** | un filetage métrique de diamètre 8 |
| **4 × Ø6** | quatre trous identiques de diamètre 6 |
| **□20** | une section carrée de 20 |

### 3. Les règles qui évitent 90 % des erreurs

1. **Une dimension n'est cotée qu'une seule fois** sur l'ensemble du plan. Deux cotes qui se
   contredisent, et l'atelier téléphone — ou pire, choisit tout seul.
2. **On ne cote jamais une dimension qui se déduit des autres.** Si vous cotez 30, 40 et le
   total 70, la troisième cote est en trop : c'est une **surabondance**, et elle sera fausse
   dès qu'une tolérance sera appliquée.
3. **Les cotes se lisent du bas ou de la droite de la feuille**, jamais à l'envers.
4. **On ne cote pas sur les traits cachés.** Si une dimension n'est visible qu'en pointillés,
   c'est le signe qu'il faut faire une coupe.
5. **On groupe les cotes d'une même fonction** au même endroit, plutôt que de les éparpiller.

### 4. Choisir ses surfaces de référence

Sur une pièce, certaines surfaces travaillent (elles appuient, elles guident, elles portent)
et d'autres non. On appelle **surface de référence** celle qui positionne la pièce dans le
mécanisme, et c'est **à partir d'elle** qu'on cote.

Prenons une plaque avec quatre trous de fixation. Deux façons de coter :

- **En chaîne** : 20, puis 30, puis 30, puis 20 à partir du trou précédent. Les erreurs
  s'additionnent : le dernier trou peut être décalé de la somme de toutes les tolérances.
- **À partir d'une référence unique** : 20, 50, 80, 100, tous mesurés depuis le même bord.
  Les erreurs ne s'accumulent plus.

**En cotation de fixation, on part toujours d'une référence unique.** La cotation en chaîne
n'est acceptable que pour des dimensions sans exigence, ou quand c'est justement l'écart entre
deux éléments voisins qui compte.

### 5. Toutes les cotes ne se valent pas

[[FIG:pourquoi_tolerance]]

Sur une pièce réelle, **environ 80 % des cotes n'ont aucune exigence particulière**. Elles
sont couvertes par une mention en cartouche, du type **ISO 2768-m** (tolérances générales,
classe moyenne) : par exemple ± 0,3 mm pour une cote entre 30 et 120 mm. Ce n'est donc pas
une cote « libre » : c'est une tolérance implicite, qui s'applique automatiquement.

Les 20 % restants sont les **cotes fonctionnelles** : celles qui garantissent que le mécanisme
marche. Elles seules reçoivent une tolérance chiffrée, et c'est là que passe l'argent.

Trois façons de l'écrire :

- **40 ± 0,1** — écriture symétrique, la plus lisible
- **40 +0,05 / −0,02** — écarts dissymétriques
- **40 H7** — écriture normalisée ISO, détaillée dans le bloc 2

### 6. L'état de surface : la finition n'est pas un détail

Deux pièces peuvent avoir exactement les mêmes cotes et l'une fuir, l'autre pas. La différence
se joue sur la rugosité de la surface.

[[FIG:rugosite_ra]]

Le symbole se pose sur la surface concernée, avec la valeur Ra en micromètres. Une barre
horizontale ajoutée au symbole signifie « enlèvement de matière obligatoire » ; un cercle
signifie au contraire « enlèvement de matière interdit » — la surface reste brute.

Quelques valeurs à retenir pour l'année :

| Où | Ra typique | Pourquoi |
|---|---|---|
| face non fonctionnelle | brut | personne ne la touche |
| face d'appui boulonnée | 3,2 | il suffit qu'elle porte à plat |
| surface qui frotte | 1,6 | limiter l'usure |
| portée de roulement, de joint | 0,8 | sinon la levée du joint s'use et ça fuit |
| glace optique, calibre | 0,1 | rodage, polissage |

**Demander Ra 0,8 partout, c'est tripler le prix de la pièce sans aucun gain.**

### 7. Méthode : coter une pièce en cinq étapes

1. **Identifier les surfaces fonctionnelles** : celles qui touchent une autre pièce.
2. **Choisir les références** : la face d'appui principale, puis un axe ou un bord.
3. **Coter les dimensions fonctionnelles** depuis ces références, avec leurs tolérances.
4. **Coter le reste** sans tolérance, en s'appuyant sur ISO 2768 au cartouche.
5. **Vérifier** : chaque dimension apparaît-elle une fois et une seule ? Peut-on fabriquer et
   contrôler la pièce avec ce plan, sans jamais téléphoner au bureau d'études ?

Ce test final — *l'atelier peut-il travailler sans me poser de question ?* — est le meilleur
critère de qualité d'un plan.

### 8. Les erreurs classiques

1. **Surabondance** : coter les trois dimensions d'une chaîne alors que deux suffisent.
2. **Coter en chaîne** des trous de fixation, et se retrouver avec un décalage cumulé.
3. **Serrer des tolérances sans raison** : chaque zéro après la virgule coûte cher.
4. **Oublier l'état de surface** sur une portée de roulement ou de joint.
5. **Coter depuis une surface brute de fonderie** : la référence doit être une surface usinée,
   sinon la précision demandée n'a aucun sens.

### 9. À retenir

- On cote ce qui doit être **garanti**, pas ce qu'on voit.
- Une dimension, une seule cote. Jamais de surabondance.
- Cotation fonctionnelle depuis une **référence unique**, pas en chaîne.
- 80 % des cotes relèvent des tolérances générales du cartouche.
- Ra 3,2 partout, Ra 0,8 seulement où ça porte, ça frotte ou ça étanche.
"""}


# ===========================================================================
# FICHE 2.1 — TOLÉRANCES DIMENSIONNELLES ET SYSTÈME ISO 286
# ===========================================================================

FICHES["2.1"] = {"cours": """
### 1. Le jour où l'on comprend que « 20 mm » n'existe pas

Demandez à un tourneur une pièce de 20 mm. Il en fabrique dix. Mesurez-les au micromètre :
19,98 — 20,01 — 19,99 — 20,03 — 20,00 — 19,97…

Ce n'est pas un mauvais ouvrier. **Aucune machine au monde ne sort deux pièces identiques.**
L'outil s'use, la matière chauffe et se dilate, la machine vibre, le brut n'est jamais deux
fois pareil. La cote exacte est une idée, pas une réalité d'atelier.

[[FIG:pourquoi_tolerance]]

Le concepteur ne peut donc pas se contenter d'écrire « 20 ». Il doit dire à l'atelier :
**entre quelles valeurs la pièce reste bonne**. Tout le reste de cette fiche découle de là.

### 2. Le vocabulaire, une fois pour toutes

Prenons une cote écrite **20 +0,05 / −0,02** :

| Terme | Sens | Valeur ici |
|---|---|---|
| cote nominale | la valeur de référence, celle qu'on lit sur le plan | 20 |
| écart supérieur | ce qu'on ajoute pour obtenir le maximum | +0,05 |
| écart inférieur | ce qu'on ajoute (ici on retire) pour le minimum | −0,02 |
| cote maxi | nominale + écart supérieur | 20,05 |
| cote mini | nominale + écart inférieur | 19,98 |
| **intervalle de tolérance (IT)** | la largeur de la zone acceptée | 20,05 − 19,98 = **0,07** |

Une convention à graver, car toute la norme repose dessus :

> **MAJUSCULES pour les alésages** (le trou, le contenant) : ES, EI
> **minuscules pour les arbres** (l'axe, le contenu) : es, ei

Astuce pour ne plus se tromper : la majuscule est **grande**, comme le trou qui doit accueillir
l'autre pièce.

### 3. Ce que coûte un zéro après la virgule

C'est le point que les débutants sous-estiment le plus. Voici l'ordre de grandeur réel :

| IT visé | Moyen de fabrication | Coût relatif |
|---|---|---|
| 0,2 mm | tournage ou fraisage standard | 1 |
| 0,05 mm | usinage soigné, contrôle au pied à coulisse | 2 à 3 |
| 0,02 mm | finition, contrôle au micromètre | 5 |
| 0,005 mm | rectification, atelier à température stable | 10 et plus |

D'où la règle de conception qui vous suivra toute votre carrière :

> **On ne serre une tolérance que si une fonction l'exige.**

Sur une pièce réelle, 80 % des cotes n'ont besoin d'aucune tolérance particulière : elles sont
couvertes par la mention **ISO 2768-m** du cartouche (± 0,3 mm entre 30 et 120 mm, par exemple).
Les 20 % restants sont les cotes fonctionnelles : c'est là qu'on met l'argent.

### 4. Le système ISO : une lettre et un chiffre

Écrire « trou de 30,000 à 30,021 » sur chaque plan serait long et source d'erreurs. La norme
ISO 286 a donc créé un code : **Ø30 H7**.

[[FIG:lettres_et_grades]]

- **La lettre** dit **où** se place la zone de tolérance par rapport à la cote nominale. C'est
  elle qui crée le jeu ou le serrage. Deux lettres particulières : **H** (alésage dont l'écart
  inférieur est nul : le trou part exactement du nominal) et **h** (arbre dont l'écart supérieur
  est nul : l'arbre ne dépasse jamais le nominal).
- **Le chiffre**, appelé **grade IT**, dit la **largeur** de la zone. IT6 est plus serré qu'IT7,
  lui-même plus serré qu'IT11.

Point qui surprend toujours : pour un même grade, **l'IT grandit avec le diamètre**. Un IT7 vaut
21 µm sur un Ø30, mais 35 µm sur un Ø100. C'est logique : il est plus difficile de tenir la même
précision sur une grosse pièce, qui chauffe et se déforme davantage.

### 5. Lire une table ISO 286 sans se tromper

[[FIG:calcul_ajustement_etapes]]

La table donne les valeurs en **micromètres** (µm), le plan est en **millimètres**.
1 000 µm = 1 mm. Une erreur d'un facteur mille est la faute la plus fréquente en devoir.

Marche à suivre :

1. Repérer la ligne du **groupe de dimensions** qui contient le diamètre (par exemple
   « au-dessus de 18 jusqu'à 30 » pour un Ø30).
2. Lire la valeur de l'IT dans la colonne du grade demandé → pour Ø30 IT7 : **21 µm = 0,021 mm**.
3. Trouver l'écart fondamental donné par la lettre. Pour H : EI = 0.
4. En déduire l'autre écart : ES = EI + IT = 0 + 0,021.

Résultat : **Ø30 H7 → de 30,000 à 30,021**.

Pour un arbre, même méthode, en faisant attention au sens : pour les lettres a à h, c'est
l'écart **supérieur** qui est donné par la table (il est négatif ou nul), et ei = es − IT. Pour
les lettres k à z, c'est l'écart **inférieur** (positif), et es = ei + IT.

Le **calculateur d'ajustements** de cette application fait ces lectures pour vous — mais il faut
savoir les faire à la main, parce que l'examen se passe avec la table papier.

### 6. Quelques valeurs à connaître par cœur

Pour un Ø30, qui revient sans arrêt en exercice :

| Grade | IT | Se fabrique par |
|---|---|---|
| IT6 | 13 µm | rectification, alésage fin |
| IT7 | 21 µm | usinage soigné : **le grade le plus courant en mécanique** |
| IT8 | 33 µm | usinage normal |
| IT11 | 130 µm | usinage courant, tolérances larges |
| IT13 | 330 µm | pièce brute, découpe |

Retenez au minimum : **IT7 ≈ 21 µm sur un Ø30**. C'est votre point de repère pour juger si une
tolérance qu'on vous impose est réaliste ou fantaisiste.

### 7. Les erreurs classiques

1. **Confondre µm et mm.** 21 µm, c'est 0,021 mm — pas 0,21.
2. **Confondre la lettre et le chiffre.** La lettre place la zone (le jeu), le chiffre en donne
   la largeur (la précision). Un H11 est aussi « en H » qu'un H7 : simplement beaucoup plus large.
3. **Serrer par précaution.** Mettre du H7 partout « pour être sûr » double la facture sans
   améliorer le fonctionnement.
4. **Oublier que l'IT dépend du diamètre.** Le même grade ne donne pas la même valeur sur Ø10
   et sur Ø200.
5. **Prendre l'écart de l'arbre pour celui de l'alésage.** Majuscule = trou, minuscule = arbre.

### 8. À retenir

- Aucune cote n'est exacte : on donne une zone, appelée intervalle de tolérance.
- IT = cote maxi − cote mini. Plus il est petit, plus la pièce coûte cher.
- Lettre = position de la zone. Chiffre = largeur de la zone.
- H : l'alésage part du nominal. h : l'arbre ne dépasse pas le nominal.
- Les tables sont en micromètres ; les plans, en millimètres.
"""}


# ===========================================================================
# FICHE 2.3 — TOLÉRANCEMENT GÉOMÉTRIQUE (GPS) ET COTATION FONCTIONNELLE
# ===========================================================================

FICHES["2.3"] = {"cours": """
### 1. Une pièce aux bonnes cotes… qui ne marche pas

Un tourneur vous livre un arbre. Vous le mesurez au pied à coulisse : 30 mm ici, 30 mm là,
30 mm partout. La cote est bonne. Vous essayez de le monter dans son palier : **il n'entre pas.**

[[FIG:defaut_geometrique]]

L'arbre est légèrement cintré. Chaque mesure isolée donne bien 30, mais l'ensemble n'est pas un
cylindre droit. Autre exemple courant : une face d'appui parfaitement à la bonne épaisseur, mais
gondolée — la pièce bascule dès qu'on la boulonne.

**Conclusion : la cotation dimensionnelle dit combien ça mesure, mais ne dit rien sur la forme
ni sur la position.** Il faut donc un second langage. C'est ce qu'on appelle le tolérancement
géométrique, ou GPS (spécification géométrique des produits).

### 2. Ce qu'est vraiment une tolérance géométrique

Une tolérance géométrique définit une **zone dans laquelle la surface réelle doit se trouver** :
l'espace entre deux plans parallèles, entre deux cylindres coaxiaux, ou l'intérieur d'un cylindre
de diamètre t. La surface a le droit d'onduler, à condition de rester dans cette zone.

### 3. Les quatre familles

| Famille | Ce qu'elle contrôle | Exemples | Référence ? |
|---|---|---|---|
| **Forme** | la surface toute seule | rectitude, planéité, circularité, cylindricité | non |
| **Orientation** | l'angle par rapport à une autre surface | parallélisme, perpendicularité, inclinaison | oui |
| **Position** | l'emplacement | localisation, coaxialité, symétrie | oui |
| **Battement** | ce que voit un comparateur quand la pièce tourne | battement radial, axial, total | oui |

La règle qui tombe à tous les contrôles : **les tolérances de forme n'ont jamais de référence,
les trois autres familles en ont toujours une.** C'est logique : être plan, c'est une propriété
de la surface elle-même ; être perpendiculaire, c'est forcément perpendiculaire *à quelque chose*.

### 4. Lire un cadre

[[FIG:cadre_tolerance]]

La **référence** est identifiée sur le dessin par un triangle plein posé sur la surface, relié à
une lettre encadrée. On choisit comme référence **la surface qui positionne réellement la pièce
dans le mécanisme** — presque toujours la face d'appui principale, et jamais une surface brute
de fonderie.

Quand plusieurs références apparaissent (A, B, C), **l'ordre compte** : A est posée en premier
sur le marbre, B bloque ensuite, C oriente. Inverser A et B, c'est mesurer autre chose.

### 5. Choisir la bonne exigence : trois cas concrets

- **Un alésage de roulement dans un carter.** Si l'axe du trou n'est pas perpendiculaire à la
  face d'appui, l'arbre entre de travers, le roulement travaille en coin, chauffe et casse.
  → **perpendicularité Ø0,03 par rapport à A**.
- **Une face d'appui de bride.** Si elle est gondolée, la bride bascule et tout le reste se
  désaligne. → **planéité 0,05**.
- **Quatre trous de fixation.** S'ils sont chacun décalés, les vis ne tombent pas en face des
  taraudages. → **localisation Ø0,2 par rapport à A et B**.

Dans les trois cas, aucune tolérance dimensionnelle n'aurait détecté le problème.

### 6. La cotation fonctionnelle : coter ce qui doit être garanti

Deuxième moitié de cette fiche, et changement de point de vue. Jusqu'ici on cotait des pièces.
Maintenant on part **du mécanisme monté**.

Exemple classique : une roue dentée doit pouvoir se dilater entre deux épaulements. Il faut
garantir un jeu axial **entre 0,1 et 0,4 mm**. Ce jeu ne dépend d'aucune pièce en particulier :
il dépend du carter, de la roue et du couvercle à la fois.

[[FIG:chaine_de_cotes]]

Ce jeu à garantir s'appelle une **condition fonctionnelle**, notée Ja. On la représente par un
vecteur, et on trace la **chaîne de cotes** : on part de l'origine du vecteur et on avance de
pièce en pièce, par les surfaces en contact, jusqu'à revenir à l'autre extrémité.

**Deux règles, et tout le reste en découle :**

1. Chaque pièce traversée fournit **une cote et une seule**. Si une pièce apparaît deux fois,
   la chaîne est fausse.
2. La chaîne doit **se refermer**. C'est votre autocontrôle.

**Les deux équations :**

- Cotes nominales : **Ja = somme des cotes dans le sens du vecteur − somme des cotes en sens inverse**
- Tolérances : **ITja = ITa + ITb + ITc + …** — toutes les tolérances **s'additionnent**, quel
  que soit le sens de la cote.

Sur l'exemple : Ja = 60 − 40 − 19,7 = 0,3 mm, et l'intervalle disponible vaut 0,4 − 0,1 = 0,3 mm,
soit 0,1 mm par cote si on répartit également.

### 7. La conséquence qui fait le bon concepteur

Puisque les tolérances s'additionnent, **plus la chaîne est longue, plus chaque pièce doit être
précise**, donc chère. Avec six pièces dans la chaîne au lieu de trois, chaque cote doit être
deux fois plus serrée pour le même résultat.

D'où deux réflexes de conception :

- **raccourcir la chaîne** : supprimer des pièces intermédiaires, regrouper deux fonctions sur
  une seule pièce ;
- **introduire une pièce de réglage** — cale d'épaisseur, entretoise usinée à la demande, écrou
  de réglage — qui absorbe toute la dispersion. Les grandes pièces peuvent alors rester larges.

Une cale à 3 € vaut souvent mieux que cinq pièces rectifiées.

### 8. Les erreurs classiques

1. **Mettre une référence sur une tolérance de forme.** Planéité 0,05 A n'a pas de sens.
2. **Choisir comme référence une surface brute.** La référence doit être usinée, sinon la
   précision demandée est illusoire.
3. **Oublier le signe Ø** devant la valeur, quand la zone est cylindrique.
4. **Croire que les tolérances se compensent** dans une chaîne. Elles s'additionnent, toujours.
5. **Faire passer la chaîne deux fois par la même pièce.**

### 9. À retenir

- Dimension = combien. Géométrie = quelle forme, à quelle place.
- Forme : sans référence. Orientation, position, battement : avec référence.
- Un cadre se lit : symbole | valeur | référence. Ø devant la valeur = zone cylindrique.
- Une condition fonctionnelle appartient au mécanisme, pas à une pièce.
- ITja = somme de tous les IT de la chaîne. Chaîne courte = pièces moins chères.
"""}


# ===========================================================================
# FICHE 3.1 — FAMILLES DE MATÉRIAUX ET PROPRIÉTÉS MÉCANIQUES
# ===========================================================================

FICHES["3.1"] = {"cours": """
### 1. Le vrai problème du concepteur

Vous devez dessiner un arbre de transmission. Question : en quoi ?

La réponse « en acier » ne veut rien dire — il existe des milliers de nuances d'acier, du plus
mou au plus dur, du plus cher au plus courant. Pour choisir, il faut savoir **quelles questions
poser au matériau**. Elles sont au nombre de cinq, et une seule expérience permet d'y répondre :
l'essai de traction.

### 2. L'essai de traction : d'où viennent tous les chiffres

On prend un barreau du matériau, on tire dessus de plus en plus fort, et on enregistre.

[[FIG:courbe_traction]]

Ce que la courbe raconte :

- **Au début, tout est réversible.** On tire, la pièce s'allonge ; on relâche, elle revient
  exactement à sa longueur initiale. C'est le **domaine élastique**. La pente de cette droite
  s'appelle le **module d'Young E** : plus elle est raide, moins le matériau plie.
- **Puis vient un point de non-retour.** Au-delà d'une certaine contrainte, la pièce reste
  déformée même après relâchement. Cette limite s'appelle la **limite élastique Re**. C'est
  elle qu'on utilise dans tous les calculs de dimensionnement, parce qu'une pièce déformée
  est une pièce perdue, même si elle n'est pas cassée.
- **Enfin la rupture.** La contrainte maximale atteinte avant de casser s'appelle la
  **résistance à la rupture Rm**.

### 3. Les cinq grandeurs à connaître

| Grandeur | Ce qu'elle dit | Unité | À quoi elle sert |
|---|---|---|---|
| **Re** | à partir de quand la pièce se déforme définitivement | MPa | dimensionner : σ ≤ Re / s |
| **Rm** | à partir de quand elle casse | MPa | connaître la marge avant rupture |
| **E** | à quel point elle plie sous charge | MPa | calculer une flèche, un allongement |
| **A %** | de combien elle s'allonge avant de casser | % | savoir si elle prévient avant de rompre |
| **résilience** | sa résistance aux **chocs** | J/cm² | pièces qui prennent des coups, froid |

À quoi s'ajoutent la **dureté** (résistance à la rayure et à l'usure, mesurée en HB, HRC ou HV)
et la **tenue en fatigue** — la capacité à supporter des millions de cycles de charge, souvent à
un niveau bien inférieur à Re.

### 4. La confusion qui coûte le plus cher aux débutants

**Résistance et rigidité ne sont pas la même chose.**

[[FIG:resistance_vs_rigidite]]

Regardez bien les barres bleues : le S235 et le 42CrMo4 traité ont le **même module d'Young**,
alors que leurs limites élastiques vont du simple au triple. Cela veut dire :

> Une pièce en acier traité **résiste** trois fois plus, mais **plie exactement autant** qu'une
> pièce identique en acier ordinaire.

Conséquence pratique : si une pièce plie trop, changer de nuance ne servira **strictement à rien**.
Il faut augmenter le moment quadratique — donc la hauteur, les nervures, un profil creux. C'est
une erreur qu'on voit tous les ans en projet de BTS.

Même chose pour l'aluminium : trois fois plus léger que l'acier, mais aussi **trois fois moins
rigide**. Une pièce alu qui remplace une pièce acier doit être nettement plus épaisse.

### 5. Les grandes familles, et ce qu'on leur demande

**Aciers** — le matériau de référence : E = 210 GPa, bon marché, disponibles partout, soudables
selon la nuance, traitables thermiquement. Inconvénient : ça rouille, sauf les inox.

**Fontes** — riches en carbone (plus de 2 %), donc coulées et non forgées. La fonte grise
**amortit remarquablement les vibrations** grâce à ses lamelles de graphite : c'est pour cela que
les bâtis de machines-outils sont en fonte. En contrepartie, elle est fragile et ne se soude
pratiquement pas. La fonte à graphite sphéroïdal (GJS) est bien plus ductile.

**Aluminium** — trois fois plus léger, ne rouille pas (couche d'oxyde naturelle), excellent
conducteur, se recycle bien. Mais trois fois moins rigide, plus difficile à souder, plus cher au
kilo, et il se déforme davantage à la chaleur.

**Polymères** — légers, isolants, moulables en formes complexes, souvent autolubrifiants
(POM, PA6). Mais E très faible (1 à 3 GPa), ils fluent sous charge permanente et vieillissent
aux UV. Rentables seulement en grande série, à cause du prix du moule.

**Composites** — très performants au rapport résistance/masse, mais chers, difficiles à réparer
et à contrôler.

### 6. Et le prix, dans tout ça ?

C'est un critère de conception à part entière, pas une préoccupation de comptable. Ordres de
grandeur au kilo, à retenir en relatif : acier de construction 1, acier allié traité 2 à 3,
inox 5 à 8, aluminium 3 à 4, polymère technique 5 à 15, composite carbone 50 et plus.

Ajoutez la **disponibilité locale** : une nuance parfaite sur le papier mais introuvable chez
les fournisseurs de votre région, avec quatre mois de délai, est un mauvais choix.

### 7. Méthode : choisir un matériau

[[FIG:choisir_materiau]]

En cinq questions :

1. **Quelles sollicitations ?** Traction, flexion, choc, fatigue, frottement, température.
2. **Quelle grandeur est critique ?** La résistance (Re), la rigidité (E), la masse, la dureté ?
3. **Quel environnement ?** Humidité, produits chimiques, alimentaire, extérieur, froid.
4. **Quel procédé de fabrication ?** Moulé, usiné, soudé, plié, injecté — tous les matériaux ne
   s'y prêtent pas.
5. **Quelle série et quel budget ?** Une pièce unique ou dix mille ?

Puis on vérifie par le calcul, et on retient la solution **la moins chère qui satisfait toutes
les exigences** — jamais la plus performante.

### 8. Les erreurs classiques

1. **Changer de nuance pour réduire une flèche.** Sans effet : c'est E qui commande, et E ne
   change pas.
2. **Choisir de l'inox par réflexe.** Il est cher, moins résistant que beaucoup d'aciers alliés,
   et il s'usine mal. On le réserve aux milieux corrosifs et à l'alimentaire.
3. **Oublier la résilience.** Une pièce dure et résistante peut casser net au premier choc.
4. **Négliger la fatigue.** Une pièce qui tourne casse à des contraintes bien inférieures à Re.
5. **Choisir une nuance introuvable localement.**

### 9. À retenir

- Re = déformation définitive. Rm = rupture. E = rigidité.
- On dimensionne sur Re, jamais sur Rm.
- E ne change pas avec la nuance ni avec le traitement : seule la forme raidit une pièce.
- Acier E = 210 GPa · aluminium 70 GPa · polymère 1 à 3 GPa.
- Le bon matériau est le moins cher qui satisfait toutes les exigences.
"""}


# ===========================================================================
# FICHE 3.2 — DÉSIGNATION NORMALISÉE DES MATÉRIAUX
# ===========================================================================

FICHES["3.2"] = {"cours": """
### 1. Pourquoi ces codes bizarres

Sur un plan, la case « matière » du cartouche contient quelque chose comme **42CrMo4** ou
**EN-GJS-400-15**. Ce n'est pas du jargon gratuit : c'est un code international qui dit
exactement de quoi la pièce est faite, sans ambiguïté et sans traduction.

Écrire « acier dur » sur un plan, c'est comme écrire « une vis » sur une commande : le
fournisseur ne peut pas deviner. La désignation normalisée supprime la devinette.

La bonne nouvelle : ces codes se lisent avec **quatre règles**, et elles couvrent 95 % de ce que
vous rencontrerez en première année.

[[FIG:decoder_designation]]

### 2. Règle 1 — Les aciers d'usage général : la lettre dit la limite élastique

Ce sont les aciers de charpente, de tôlerie, de mécano-soudé. On ne les traite pas
thermiquement, on les choisit pour leur résistance et leur soudabilité.

**S235** : S pour *structure*, 235 pour **Re = 235 MPa**.
**S355** : même famille, Re = 355 MPa.
**E295**, **E335** : E pour *construction mécanique*, même logique.

Le nombre est donc directement la valeur que vous utiliserez dans vos calculs. C'est la seule
famille où c'est le cas — attention à ne pas généraliser.

### 3. Règle 2 — Les aciers non alliés spéciaux : le nombre dit le carbone

Ce sont les aciers qu'on va **tremper**. Leur aptitude au traitement dépend du carbone.

**C45** : C pour acier non allié, 45 pour **0,45 % de carbone** (le nombre est en centièmes de
pour cent).

Repères utiles :

| Nuance | Carbone | Comportement |
|---|---|---|
| C22 | 0,22 % | doux, se soude bien, trempe mal |
| C45 | 0,45 % | le compromis classique : arbres, axes, pignons |
| C60 | 0,60 % | dur après trempe, mais fragile et difficile à souder |

Règle empirique : **plus de carbone = plus dur après trempe, mais moins soudable et plus fragile.**

### 4. Règle 3 — Les aciers faiblement alliés : le coefficient multiplicateur

Aucun élément d'alliage n'atteint 5 %. La désignation se lit en trois morceaux :

**42CrMo4** = 0,42 % de carbone · chrome et molybdène · le 4 concerne le **premier** élément cité.

Et voilà le piège : pour connaître la teneur réelle, il faut **diviser par un coefficient** qui
dépend de l'élément :

| Éléments | Coefficient |
|---|---|
| Cr, Co, Mn, Ni, Si, W | 4 |
| Al, Be, Cu, Mo, Nb, Pb, Ta, Ti, V, Zr | 10 |
| Ce, N, P, S | 100 |
| B | 1 000 |

Donc 42CrMo4 → 4 ÷ 4 = **environ 1 % de chrome**. Pas 4 % : c'est l'erreur numéro un de toute
la fiche.

Ces aciers, une fois trempés et revenus, atteignent 700 à 1 000 MPa de limite élastique. On les
utilise quand la place manque et qu'il faut une pièce fine et très chargée.

### 5. Règle 4 — Les aciers fortement alliés : le préfixe X

Dès qu'un élément dépasse 5 %, la désignation commence par **X**, et les teneurs sont alors
données **directement en pourcentage**, sans coefficient.

**X5CrNi18-10** = 0,05 % de carbone, 18 % de chrome, 10 % de nickel. C'est l'inox le plus
répandu, dit « 18/10 », amagnétique, celui de l'agroalimentaire et de la coutellerie.

**X2CrNiMo17-12-2** : le fameux 316L, avec du molybdène en plus, pour les milieux chlorés
(bord de mer, piscines, chimie).

Le chrome est ce qui rend l'acier inoxydable : au-delà de 10,5 %, il forme une couche d'oxyde
invisible qui se reconstitue toute seule quand on la raye. C'est la **passivation**.

### 6. Les fontes (EN 1560)

**EN-GJL-250** se lit ainsi : GJ pour fonte moulée, **L** pour graphite **lamellaire**,
250 pour Rm = 250 MPa.

**EN-GJS-400-15** : **S** pour graphite **sphéroïdal**, Rm = 400 MPa, allongement 15 %.

La différence entre L et S change tout : la lamellaire amortit très bien les vibrations mais
casse net ; la sphéroïdale se déforme avant de rompre. Bâti de machine → GJL. Pièce qui prend
des efforts et des chocs → GJS.

### 7. Les aluminiums (EN 573)

**EN AW-6060** : AW pour *aluminium corroyé* (laminé, extrudé), puis quatre chiffres dont le
premier donne la famille :

| Série | Élément principal | Emploi typique |
|---|---|---|
| 1000 | aluminium pur | conduction, chimie |
| 2000 | cuivre | aéronautique (mais mauvaise tenue à la corrosion) |
| 5000 | magnésium | tôlerie, marine, emboutissage |
| 6000 | magnésium + silicium | **profilés extrudés — le plus courant en mécanique** |
| 7000 | zinc | haute résistance : 7075, structures très chargées |

### 8. Méthode : décoder n'importe quelle désignation en trois secondes

1. **Ça commence par X ?** → acier fortement allié, teneurs en direct.
2. **Ça commence par S ou E ?** → le nombre est la limite élastique en MPa.
3. **Ça commence par C ?** → le nombre est le carbone en centièmes de pour cent.
4. **Ça commence par un nombre ?** → acier faiblement allié : carbone en centièmes, puis les
   éléments, puis les teneurs à diviser par leur coefficient.
5. **Ça commence par EN-GJ ?** → une fonte. **EN AW** ? → un aluminium.

### 9. Les erreurs classiques

1. Lire 42CrMo**4** comme 4 % de chrome au lieu de 1 %.
2. Croire que le nombre de C45 est une résistance : c'est du carbone.
3. Confondre GJL et GJS — l'une casse net, l'autre pas.
4. Oublier que S235 donne Re, mais que C45 ne donne rien de tel : la résistance du C45 dépend
   entièrement de son traitement thermique.

### 10. À retenir

- S / E → limite élastique en MPa. C → carbone en centièmes de %.
- Faiblement allié → teneurs à diviser par 4, 10, 100 ou 1 000.
- X → fortement allié, teneurs en direct. Inox à partir de 10,5 % de chrome.
- EN-GJL = lamellaire (amortit, fragile) · EN-GJS = sphéroïdal (ductile).
- EN AW 6000 = profilés · 7000 = haute résistance.
"""}


# ===========================================================================
# FICHE 3.3 — TRAITEMENTS THERMIQUES ET TRAITEMENTS DE SURFACE
# ===========================================================================

FICHES["3.3"] = {"cours": """
### 1. Changer les propriétés sans changer la nuance

Prenez deux barreaux de C45 issus de la même barre. Le premier casse à 620 MPa, le second à
900 MPa. Même matière, même désignation, même fournisseur.

La différence : le second a été **traité thermiquement**. En chauffant puis en refroidissant
l'acier selon un cycle précis, on réorganise sa structure interne — et on change radicalement
ses propriétés mécaniques, sans toucher à sa composition chimique.

C'est un levier considérable pour le concepteur : la même pièce, avec le même plan, peut être
deux fois plus résistante pour quelques euros de plus.

**Mais attention à une chose que le traitement ne change JAMAIS : le module d'Young E.** Une
pièce trempée résiste davantage, mais elle plie exactement autant. Aucun traitement thermique
ne raidit une pièce.

### 2. Les traitements dans la masse

Ils affectent toute l'épaisseur.

**La trempe** — on chauffe l'acier au rouge (environ 850 °C), on maintient, puis on refroidit
brutalement dans l'eau ou l'huile. La structure se fige dans un état très dur et très résistant.
Problème : la pièce devient aussi **fragile** et pleine de contraintes internes. Elle peut même
se fissurer toute seule. Une pièce simplement trempée n'est presque jamais utilisable telle quelle.

**Le revenu** — on la réchauffe ensuite, plus modérément (200 à 600 °C), et on laisse refroidir
lentement. On perd un peu de dureté et on regagne beaucoup de ténacité. **Trempe + revenu vont
toujours ensemble** : on parle d'acier « trempé revenu », ou d'acier « amélioré ».

Ordre de grandeur pour du C45 : brut Re ≈ 340 MPa, après trempe et revenu Re ≈ 600 MPa.

**Le recuit** — l'inverse : on chauffe puis on refroidit très lentement, pour **adoucir** la
pièce et supprimer les contraintes internes. On l'utilise avant un usinage de précision, ou
après une soudure, pour éviter que la pièce ne se déforme plus tard, une fois finie.

**Le normalisage** — un recuit plus court qui régularise la structure après forgeage ou soudage.

Condition indispensable pour tremper : **il faut au moins 0,3 % de carbone**. Un S235 ne trempe
pas, quoi qu'on fasse. C'est exactement pour cela que les arbres se font en C45 ou en 42CrMo4.

### 3. Les traitements superficiels : le meilleur des deux mondes

Voici le vrai problème d'un pignon : sa surface doit être **très dure** pour ne pas s'user, mais
son cœur doit rester **tenace** pour encaisser les chocs. Dur et tenace sont contradictoires.

La solution : durcir seulement la peau.

[[FIG:peau_dure_coeur_tenace]]

**La cémentation** — on place la pièce dans une atmosphère riche en carbone, à 900 °C. Le carbone
pénètre sur 0,5 à 1,5 mm, puis on trempe. Seule la peau, enrichie, durcit ; le cœur, resté pauvre
en carbone, garde sa ténacité. On part donc d'un acier **à faible teneur en carbone** :
16MnCr5, 18CrMo4. Emploi : pignons, cames, axes, arbres cannelés.

**La nitruration** — même idée avec de l'azote, à plus basse température (500 °C). Couche plus
fine mais extrêmement dure, et **très peu de déformation** puisqu'il n'y a pas de trempe. Plus
cher, réservé aux pièces de précision déjà finies.

**La trempe superficielle** (par induction ou au chalumeau) — on ne chauffe que la surface, très
vite, puis on refroidit. Pas d'apport de carbone : l'acier doit déjà en contenir. Idéal pour
durcir localement une portée ou une denture.

### 4. Les traitements de surface : contre la corrosion et l'usure

Ceux-là ne modifient pas l'acier, ils **ajoutent une couche**.

| Traitement | Sur quoi | Ce qu'il apporte |
|---|---|---|
| galvanisation à chaud | acier | zinc épais : charpente et pièces extérieures |
| zingage électrolytique | visserie | protection fine et bon marché |
| peinture époxy | acier, fonte | protection + aspect, épaisseur importante |
| anodisation | **aluminium seulement** | couche d'oxyde dure, colorable |
| passivation | inox | régénère la couche protectrice après usinage |
| chromage dur | acier | très dure, contre l'usure : tiges de vérin |
| phosphatation | acier | accroche de peinture, rodage |

Deux réflexes de conception : **prévoir l'épaisseur du revêtement** (une galvanisation ajoute
50 à 100 µm, ce qui bouche un ajustement serré), et ne jamais traiter une portée déjà rectifiée
sans avoir vérifié la cote finale.

### 5. Le piège des déformations

Toute trempe déforme. Une pièce longue et fine peut se cintrer de plusieurs dixièmes en sortant
du bain. D'où l'ordre des opérations, à connaître :

> **ébauche d'usinage → traitement thermique → finition (rectification)**

Si vous usinez à la cote finale avant de tremper, la pièce sortira du four hors tolérance et il
sera trop tard. Ce simple ordre est un des points les plus concrets de toute l'année.

### 6. Comment ça apparaît sur un plan

Le traitement se note dans le cartouche ou en note près de la pièce, avec la valeur à obtenir et
la zone concernée : *« trempé revenu, 45 HRC »*, *« cémenté trempé, profondeur 0,8 mm, 58 HRC en
surface »*, *« zingué blanc 8 µm »*.

Un traitement demandé sans valeur mesurable n'est pas contrôlable — donc pas contractuel.

### 7. Les erreurs classiques

1. **Demander une trempe sur un S235.** Sans carbone, rien ne se passe.
2. **Tremper sans faire de revenu.** La pièce est dure mais fragile, et peut se fissurer.
3. **Usiner à la cote finale avant traitement.** Les déformations rendent la pièce inutilisable.
4. **Anodiser autre chose que de l'aluminium.**
5. **Oublier l'épaisseur du revêtement** sur une cote ajustée.
6. **Croire que le traitement rend la pièce plus rigide.** Il augmente Re, jamais E.

### 8. À retenir

- Trempe = dur et fragile. Revenu = on récupère la ténacité. Les deux vont ensemble.
- Recuit = adoucir et détendre, avant usinage de précision ou après soudage.
- Il faut au moins 0,3 % de carbone pour tremper.
- Cémentation = peau dure + cœur tenace, sur acier à bas carbone.
- Ordre : ébauche → traitement → finition.
- Aucun traitement ne change E.
"""}


# ===========================================================================
# FICHE 4.1 — HYPOTHÈSES, EFFORTS INTÉRIEURS, TRACTION ET COMPRESSION
# ===========================================================================

FICHES["4.1"] = {"cours": """
### 1. La question à laquelle la RDM répond

Un client vous demande une potence murale pour soulever 200 kg. Vous dessinez un bras en acier.
Deux questions se posent, et une seule vous empêchera de dormir :

> **Est-ce que ça va casser ? Est-ce que ça va trop plier ?**

La résistance des matériaux (RDM) sert exactement à ça : prévoir par le calcul, **avant** de
fabriquer, ce que la pièce va supporter. Pas plus, pas moins.

### 2. Ce que la RDM suppose (et pourquoi il faut le savoir)

Les formules simples que vous allez apprendre ne sont valables que sous certaines conditions.
À citer en examen, mais surtout à connaître pour savoir **quand elles ne s'appliquent plus** :

- **la matière est homogène et isotrope** : mêmes propriétés partout et dans toutes les
  directions (faux pour un composite, faux pour une pièce imprimée en 3D) ;
- **les déformations sont petites** devant les dimensions ;
- **on reste dans le domaine élastique** : σ ≤ Re ;
- **la pièce est une poutre** : une dimension nettement plus grande que les deux autres ;
- **les sections planes restent planes** après déformation (hypothèse de Navier-Bernoulli) ;
- **on s'éloigne des points d'application** des efforts (principe de Saint-Venant).

Retenez le principe général : la RDM classique est faite pour des **poutres élancées**, chargées
modérément. Un carter massif ou une pièce imprimée relèvent du calcul par éléments finis.

### 3. La seule méthode : isoler et couper

C'est le geste fondateur, et il est toujours le même.

[[FIG:isoler_et_couper]]

Les efforts **extérieurs** (la charge, les appuis) se voient. Ce qui nous intéresse, c'est ce
qui se passe **à l'intérieur** de la matière : on coupe donc la pièce par la pensée, on garde un
morceau, et on écrit que ce morceau est en équilibre. Ce qui manque pour équilibrer, c'est
exactement ce que l'autre morceau exerce à travers la coupure : les **efforts intérieurs**
(ou torseur de cohésion).

Selon la composante qu'on trouve, on donne un nom à la sollicitation :

[[FIG:quatre_sollicitations]]

En pratique, en première année, on traite chaque sollicitation séparément, puis on les combine
quand elles coexistent (un arbre de transmission subit torsion **et** flexion en même temps).

### 4. Traction et compression : le cas le plus simple

L'effort intérieur est perpendiculaire à la section, et la contrainte se répartit uniformément :

> **σ = N / S**   avec σ en MPa (N/mm²), N en newtons, S en mm²

Une seule chose à surveiller : **les unités**. Si N est en newtons et S en mm², le résultat est
directement en MPa. Un effort de 8 000 N sur une section de 113 mm² donne 70,8 MPa.

**L'allongement** vient ensuite, et c'est là qu'intervient le module d'Young :

> **ΔL = N × L / (E × S)**

Notez bien : la déformation dépend de **E**, pas de Re. Changer de nuance ne change pas
l'allongement d'un iota.

### 5. Le coefficient de sécurité : pourquoi on ne calcule pas au plus juste

Vous ne travaillez jamais jusqu'à Re. Vous divisez :

> **Rpe = Re / s**   puis vous vérifiez que **σ ≤ Rpe**

Pourquoi cette marge ? Parce que la réalité ne ressemble jamais au calcul : la charge réelle
dépasse parfois la charge annoncée, la nuance livrée n'est pas toujours exactement celle
commandée, l'usinage laisse des défauts, la pièce vieillit, et vos hypothèses de calcul sont
approximatives.

Valeurs usuelles :

| s | Quand |
|---|---|
| 1,5 à 2 | charge parfaitement connue, statique, matériau maîtrisé |
| 3 à 4 | cas courant en construction mécanique |
| 5 à 8 | charge variable, chocs, sécurité des biens |
| 8 à 12 | levage de personnes, appareils de sécurité |

Un chiffre bien choisi n'est pas de la « marge par prudence » : c'est un aveu honnête de ce
qu'on ne maîtrise pas.

### 6. Le piège qui fait casser les pièces bien calculées

Vous avez fait un calcul propre, la contrainte est deux fois sous l'admissible… et la pièce casse
quand même. Presque toujours au même endroit : une gorge, un épaulement, un trou, un angle vif.

[[FIG:concentration_contrainte]]

La formule σ = N/S suppose que la contrainte est **uniforme**. Dès qu'il y a un changement brutal
de section, ce n'est plus vrai : les lignes de force se resserrent et la contrainte locale grimpe.
On l'exprime par un **coefficient de concentration Kt** :

> **σ réelle = Kt × σ calculée**

Kt vaut 2 à 3 pour un épaulement mal raccordé, jusqu'à 5 pour une arête vive. La parade ne coûte
rien : **un congé de raccordement au lieu d'un angle**. Plus le rayon est grand, plus Kt est petit.

C'est aussi pour cette raison qu'en fatigue — une pièce qui tourne, qui vibre — on soigne
particulièrement l'état de surface et les congés : une rayure d'usinage est une amorce de fissure.

### 7. La compression : attention au flambage

En compression, un piège supplémentaire vous attend. Une pièce **longue et fine** ne casse pas
par écrasement : elle **se dérobe latéralement** bien avant d'atteindre Re. C'est le flambage,
et c'est brutal — la ruine est instantanée, sans prévenir.

La règle : plus la pièce est élancée (longue par rapport à sa section), plus le flambage
gouverne. Le calculateur RDM de l'application traite ce cas dans son onglet dédié.

### 8. Méthode de résolution en six étapes

1. Faire un **schéma** propre de la pièce isolée, avec toutes les forces extérieures.
2. Écrire l'**équilibre** pour trouver les actions aux appuis.
3. **Couper** à l'endroit le plus sollicité et déterminer l'effort intérieur.
4. Calculer la **contrainte** : σ = N/S.
5. Calculer l'**admissible** : Rpe = Re / s.
6. **Comparer**, conclure, et si ça ne passe pas : augmenter la section, changer de nuance,
   ou réduire la portée.

### 9. Les erreurs classiques

1. **Mélanger les unités.** Des mètres avec des millimètres, des kN avec des N.
2. **Comparer σ à Rm** au lieu de Re. Une pièce déformée est déjà perdue.
3. **Oublier le coefficient de sécurité**, ou en prendre un au hasard.
4. **Ignorer les concentrations de contrainte** aux changements de section.
5. **Oublier le flambage** en compression sur une pièce élancée.

### 10. À retenir

- σ = N / S · ΔL = N L / (E S) · Rpe = Re / s · condition : σ ≤ Rpe.
- On isole, on coupe, on écrit l'équilibre. Toujours dans cet ordre.
- Un angle vif multiplie la contrainte réelle par 2 à 5 : mettez des congés.
- En compression, une pièce élancée flambe avant de s'écraser.
"""}


# ===========================================================================
# FICHE 4.2 — CISAILLEMENT ET TORSION
# ===========================================================================

FICHES["4.2"] = {"cours": """
### 1. Cisaillement : quand la pièce est tranchée

Prenez une paire de ciseaux, ou une poinçonneuse. Les deux lames exercent des efforts opposés,
très proches l'un de l'autre, et la matière est **tranchée** : les sections glissent l'une par
rapport à l'autre.

En mécanique, cette sollicitation apparaît dès qu'un **axe, une goupille, un rivet ou un boulon**
relie deux pièces qui tirent en sens contraire.

> **τ = T / S**   avec τ (tau) en MPa, T l'effort tranchant en newtons, S la section cisaillée

La contrainte de cisaillement se note τ, jamais σ : elle agit **dans le plan** de la section, pas
perpendiculairement.

### 2. Simple ou double cisaillement : l'erreur qui coûte cher

Voici le point qui fait perdre le plus de points en devoir.

Un axe monté dans une **chape** (une fourche à deux joues) est coupé par la matière en **deux
endroits** : deux sections travaillent en parallèle. La section résistante est donc **doublée**,
et la contrainte **divisée par deux** :

> Simple cisaillement : τ = T / S
> **Double cisaillement : τ = T / (2 S)**

Concrètement : un axe de Ø10 (S = 78,5 mm²) sous 15 000 N donne 191 MPa en simple cisaillement,
mais seulement 95,5 MPa en double. C'est le rapport entre une pièce qui casse et une pièce qui
tient. Regardez toujours le montage avant de calculer.

### 3. L'admissible en cisaillement

La matière résiste moins bien au cisaillement qu'à la traction. On utilise donc une limite
propre, **Rpg** (résistance pratique au glissement) :

> **Rpg ≈ 0,5 × Rpe** pour les aciers doux (0,6 à 0,7 pour les aciers alliés)

Condition de résistance : **τ ≤ Rpg**.

### 4. Le matage : l'autre défaillance, souvent oubliée

Un axe peut très bien résister au cisaillement… et détruire quand même son logement. Sous
l'effort, la surface de contact entre l'axe et le trou subit une **pression** élevée : le trou
s'ovalise, l'axe se marque. C'est le **matage**.

> **p = F / (d × e)**   avec d le diamètre de l'axe et e l'épaisseur de la pièce percée

On compare cette pression à une pression admissible (souvent 80 à 150 MPa selon les matériaux).
C'est ce qui explique pourquoi on allonge une clavette ou on épaissit une chape plutôt que
d'augmenter le diamètre : **on cherche de la surface de contact**, pas de la section.

### 5. Torsion : quand la pièce est tordue

Tenez une barre par une extrémité et faites tourner l'autre : vous la tordez. C'est exactement ce
que subit **tout arbre de transmission** : le moteur applique un couple d'un côté, la charge
résiste de l'autre.

La contrainte de torsion est nulle au centre et **maximale à la périphérie** — les fibres du
centre tournent presque sur elles-mêmes, celles du bord parcourent beaucoup de chemin :

> **τ maxi = Mt / (I₀ / v)**

avec Mt le moment de torsion (N·mm), I₀ le moment quadratique polaire (mm⁴) et v le rayon (mm).

Pour une section circulaire pleine de diamètre d :

> **I₀ = π d⁴ / 32**  et  **I₀ / v = π d³ / 16**

### 6. La conséquence : l'arbre creux

Puisque le centre ne travaille presque pas, **on peut l'enlever**. Un tube de diamètre extérieur
50 et intérieur 40 pèse deux fois moins qu'une barre pleine de 50, tout en conservant environ
**60 % de sa résistance en torsion**. À masse égale, le tube gagne largement.

C'est pourquoi les arbres de transmission d'automobile, les cadres de vélo et les mâts sont
creux. Retenez la logique : **en torsion comme en flexion, la matière utile est loin de l'axe.**

### 7. Le lien avec la puissance : la formule qui sert tous les jours

En pratique, on ne vous donne presque jamais le couple. On vous donne une **puissance moteur** et
une **vitesse de rotation**. Le passage se fait par :

> **P = C × ω**  avec P en watts, C en N·m, ω en rad/s
> **ω = 2 π N / 60**  avec N en tours/minute

Exemple complet, à savoir refaire : un moteur de 4 kW tourne à 1 500 tr/min.
ω = 2 × π × 1 500 / 60 = 157 rad/s, donc C = 4 000 / 157 = **25,5 N·m**.

Et le réflexe de conception qui va avec : dans un réducteur, la puissance se conserve (au
rendement près). **Si la vitesse est divisée par 5, le couple est multiplié par 5.** L'arbre de
sortie est donc toujours beaucoup plus gros que l'arbre d'entrée — ce n'est pas de la
surqualité, c'est de la nécessité.

### 8. L'angle de torsion

Comme en traction, il ne suffit pas de ne pas casser : un arbre trop souple se tord, et la pièce
entraînée prend du retard sur la commande. On limite donc aussi la **déformation angulaire**,
typiquement à 0,25° par mètre pour les arbres de machines-outils.

Le module qui intervient ici n'est plus E mais **G**, le module de cisaillement (environ
80 000 MPa pour l'acier, soit à peu près E/2,6).

### 9. Les erreurs classiques

1. **Oublier le double cisaillement** : la contrainte est deux fois trop élevée dans le calcul.
2. **Comparer τ à Rpe** au lieu de Rpg.
3. **Négliger le matage** : la pièce ne casse pas, elle s'ovalise, et le jeu apparaît.
4. **Se tromper d'unités sur ω** : des tr/min utilisés comme des rad/s donnent un couple faux
   d'un facteur 9,55.
5. **Utiliser I₀ (torsion) à la place de I (flexion)**, ou l'inverse. Torsion : d⁴/32. Flexion :
   d⁴/64.

### 10. À retenir

- τ = T / S · double cisaillement : S est doublée · Rpg ≈ 0,5 Rpe.
- Matage : p = F / (d × e) — c'est une pression, pas une contrainte de section.
- Torsion : τ maxi = Mt / (I₀/v), maximale en périphérie, nulle au centre.
- I₀/v = π d³ / 16 pour un rond plein · l'arbre creux est très efficace.
- P = C ω · ω = 2 π N / 60 · réduire la vitesse multiplie le couple d'autant.
"""}


# ===========================================================================
# FICHE 4.3 — FLEXION SIMPLE, MOMENT QUADRATIQUE ET FLÈCHE
# ===========================================================================

FICHES["4.3"] = {"cours": """
### 1. La sollicitation qu'on rencontre partout

Une étagère qui porte des livres, un axe entre deux paliers, un bras de potence, un arbre chargé
par une courroie : dès qu'un effort est appliqué **perpendiculairement** à une pièce longue,
c'est de la flexion. C'est de loin le cas le plus fréquent, et le plus dimensionnant.

### 2. Ce qui se passe dans la matière

[[FIG:fibres_flexion]]

Quand la poutre plie, les fibres du dessus se raccourcissent (compression) et celles du dessous
s'allongent (traction). Entre les deux existe une couche qui ne change pas de longueur : **l'axe
neutre**, qui passe par le centre de gravité de la section.

Trois conséquences directes, et ce sont elles qui font la différence entre un bon et un mauvais
concepteur :

1. La contrainte est **maximale sur les faces extérieures** et nulle sur l'axe neutre.
2. La matière proche de l'axe neutre **ne sert presque à rien** → d'où les profils I, U, les
   tubes, les caissons et les nervures.
3. Une **rayure ou un angle vif** sur la face tendue est une amorce de rupture, puisque c'est là
   que la contrainte est la plus forte.

### 3. Le moment fléchissant

L'effort intérieur qui compte s'appelle le **moment fléchissant Mf**, en N·mm. Il varie le long
de la poutre : le dimensionnement se fait à l'endroit où il est **maximal**.

Les deux cas à connaître par cœur :

| Cas | Mf maxi | Où |
|---|---|---|
| poutre encastrée, charge F en bout | **F × L** | à l'encastrement |
| poutre sur 2 appuis, charge F au milieu | **F × L / 4** | sous la charge |
| poutre encastrée, charge répartie q | q L² / 2 | à l'encastrement |
| poutre sur 2 appuis, charge répartie q | q L² / 8 | au milieu |

Remarquez le rapport 4 entre les deux premiers cas : **une poutre encastrée d'un seul côté subit
quatre fois plus qu'une poutre appuyée aux deux bouts.** Ajouter un second appui est souvent la
solution la moins chère à un problème de résistance.

### 4. La formule centrale

> **σ maxi = Mf maxi / (I / v)**

- **I** : le moment quadratique de la section (mm⁴) — il dit comment la matière est répartie ;
- **v** : la distance de l'axe neutre à la fibre la plus éloignée (mm) ;
- **I / v** : le module de flexion, la vraie caractéristique de la section.

Les deux sections à connaître :

| Section | I | v |
|---|---|---|
| rectangle b × h (flexion selon h) | **b h³ / 12** | h / 2 |
| rond plein Ø d | **π d⁴ / 64** | d / 2 |

### 5. La règle qui vaut de l'or : la hauteur au cube

Regardez la formule du rectangle : la hauteur est **au cube**.

[[FIG:flexion_hauteur]]

- Doubler la largeur b → I doublé, et la masse doublée aussi.
- Doubler la hauteur h → I **multiplié par 8**, pour la même quantité de matière en plus.

C'est pour cette raison qu'une planche posée à plat plie mollement alors que la même planche
posée sur chant est presque rigide. Et c'est pourquoi les poutres de charpente sont hautes et
fines, jamais larges et plates.

**Réflexe de conception : pour résister à la flexion, on augmente la hauteur dans le sens de la
charge, et on éloigne la matière de l'axe neutre.**

### 6. La flèche : ne pas casser ne suffit pas

Une pièce peut résister parfaitement et rester inutilisable parce qu'elle plie trop. Un rail de
guidage qui fléchit de 3 mm, un arbre qui s'incurve entre ses paliers : la précision est perdue,
les roulements travaillent de travers.

La flèche f dépend de quatre choses :

> **f = k × F L³ / (E I)**

- elle grandit comme **L³** : doubler la portée multiplie la flèche par 8 ;
- elle diminue quand E augmente (mais E ne change pas avec la nuance) ;
- elle diminue quand I augmente : **encore la forme** ;
- k vaut 1/3 pour une poutre encastrée chargée en bout, 1/48 pour une poutre sur deux appuis
  chargée au milieu.

Critères usuels de flèche admissible : L/300 pour une charpente courante, L/500 pour un
guidage de machine, L/1000 pour un axe de précision.

### 7. Que faire quand ça ne passe pas

Dans l'ordre d'efficacité — et de coût :

1. **Réduire la portée L.** C'est de loin le plus efficace (L³ pour la flèche), et souvent
   gratuit : rapprocher les appuis, ajouter un palier intermédiaire.
2. **Augmenter la hauteur** de la section dans le sens de la charge (h³).
3. **Changer de forme** : profil I, U, tube, caisson, nervures.
4. **Passer d'un appui simple à deux appuis** : Mf divisé par 4.
5. **Changer de matériau** — en dernier, et uniquement pour la résistance : ça n'aura aucun effet
   sur la flèche entre deux aciers.

### 8. Flexion et torsion ensemble

Un arbre porte souvent une poulie ou un pignon : il subit **la torsion du couple** et **la flexion
de l'effort de courroie ou d'engrènement** en même temps. On ne peut pas additionner directement
σ et τ ; on utilise un critère d'équivalence (Tresca ou Von Mises) qui combine les deux en une
contrainte équivalente comparée à Rpe. C'est au programme de deuxième année, mais sachez déjà que
**vérifier seulement la torsion d'un arbre de transmission est faux**.

### 9. Les erreurs classiques

1. **Se tromper de cas de charge** : encastrée ou sur deux appuis, il y a un facteur 4.
2. **Confondre I et I₀** : flexion d⁴/64, torsion d⁴/32.
3. **Oublier v** et comparer Mf/I à Rpe.
4. **Changer de nuance pour réduire une flèche.** Sans effet.
5. **Ne vérifier que la résistance** en oubliant la flèche, ou l'inverse.
6. **Poser la section dans le mauvais sens** : un profil rectangulaire à plat perd presque tout.

### 10. À retenir

- σ maxi = Mf / (I/v) — et le dimensionnement se fait là où Mf est maximal.
- Rectangle I = b h³/12 · rond I = π d⁴/64.
- La hauteur compte **au cube** : doubler h multiplie la résistance par 8.
- Flèche f ∝ F L³ / (E I) : la portée compte au cube.
- Encastrée : Mf = F L · sur deux appuis : Mf = F L / 4.
"""}


# ===========================================================================
# FICHE 5.1 — ESQUISSE, CONTRAINTES ET DEGRÉS DE LIBERTÉ
# ===========================================================================

FICHES["5.1"] = {"cours": """
### 1. Ce que « paramétrique » veut vraiment dire

Dans un logiciel de dessin classique, vous tracez des traits : ce que vous dessinez est ce que
vous obtenez, et pour modifier, vous effacez et vous recommencez.

Dans un logiciel de CAO paramétrique — SolidWorks, CATIA, Inventor — vous ne dessinez pas des
traits : vous construisez un **historique de fonctions**. Chaque fonction s'appuie sur les
précédentes. Changez une cote au début, et tout se recalcule automatiquement jusqu'au bout.

C'est une puissance énorme… et un piège. Car un modèle mal construit **casse** à la première
modification : les fonctions tombent en erreur, l'arbre se remplit de points d'exclamation, et
il faut souvent tout refaire.

> **La qualité d'un modèle ne se juge pas à son apparence, mais à sa capacité à être modifié
> sans casser.** C'est le seul critère qui compte, en BTS comme en entreprise.

### 2. L'esquisse : la fondation

Tout part d'une esquisse : un dessin 2D, tracé sur un plan, qui sera ensuite extrudé, tourné ou
balayé pour créer du volume. Si l'esquisse est bancale, tout ce qui suit l'est aussi.

**Premier réflexe : choisir un plan de référence** (Face, Dessus, Droite) plutôt qu'une face de
la pièce. Une esquisse posée sur une face disparaît si la face disparaît — et une face disparaît
dès qu'on modifie la fonction qui l'a créée.

**Deuxième réflexe : centrer la pièce sur l'origine.** Cela facilite ensuite les symétries, les
répétitions, et surtout l'assemblage.

### 3. Contraindre : le point le plus important de la fiche

Une entité 2D possède des degrés de liberté : un point peut se déplacer en X et en Y, une ligne
peut en plus tourner et changer de longueur. **Contraindre, c'est supprimer ces libertés** une à
une, jusqu'à ce que la géométrie ne puisse plus bouger toute seule.

[[FIG:esquisse_contraintes]]

Le logiciel vous le dit par la couleur : bleu = il reste des libertés, noir = c'est verrouillé.

Deux familles de contraintes, et l'ordre compte :

1. **Les contraintes géométriques d'abord** : coïncidence, horizontalité, verticalité, tangence,
   parallélisme, perpendicularité, symétrie, égalité, concentricité. Elles ne coûtent rien, elles
   sont robustes, et elles portent l'intention de conception.
2. **Les cotes ensuite**, et seulement pour ce que la géométrie ne dit pas déjà.

L'erreur classique du débutant : tout coter, sans aucune contrainte géométrique. Le résultat
« marche » mais devient ingérable — quinze cotes là où une symétrie et deux cotes suffisaient.

### 4. Un exemple qui parle

Une plaque rectangulaire percée d'un trou au centre.

- **Mauvaise méthode** : quatre cotes pour les côtés, deux cotes pour positionner le trou depuis
  deux bords. Si on change la largeur, le trou n'est plus au centre : il faut corriger à la main.
- **Bonne méthode** : contrainte de symétrie du trou par rapport aux deux axes, puis deux cotes
  pour la plaque. Changez la largeur : le trou **reste au centre tout seul**, parce que c'est ça,
  votre intention.

C'est ce qu'on appelle **l'intention de conception** : le modèle doit se comporter, lors des
modifications, comme la pièce réelle devrait se comporter.

### 5. Les erreurs à éviter absolument

1. **Laisser une esquisse bleue.** Même si la forme est correcte aujourd'hui.
2. **Faire une esquisse géante** qui contient toute la pièce. Une esquisse simple par fonction :
   plus lisible, plus robuste, plus facile à corriger.
3. **S'appuyer sur des arêtes de fonctions tardives** (un congé, un chanfrein). Elles peuvent
   disparaître.
4. **Sur-contraindre** : ajouter une cote redondante avec une contrainte géométrique déjà posée.
   Le logiciel refuse, à juste titre.
5. **Ne pas nommer les fonctions.** Un arbre avec « Bossage-Extrusion12 » n'est repris par
   personne, pas même par vous dans trois mois.

### 6. Le paramétrage par équations

On peut aller plus loin et lier des cotes entre elles par des formules :
`"largeur" = "longueur" / 2`, ou `"nb_trous" = "longueur" / 50`.

C'est ce qui permet de créer une **famille de pièces** : une seule maquette qui décline vingt
tailles, pilotée par une table de paramètres. Très utilisé en entreprise pour les catalogues
(vérins, brides, supports) — et très apprécié en projet de BTS.

### 7. Méthode : construire une esquisse propre en cinq étapes

1. Choisir un **plan de référence**.
2. Tracer la forme **approximativement** — sans chercher les bonnes dimensions tout de suite.
3. Poser les **contraintes géométriques** (symétries, tangences, alignements).
4. Ajouter les **cotes** manquantes, en partant des dimensions fonctionnelles.
5. Vérifier que l'esquisse est **entièrement contrainte**, puis la nommer.

### 8. À retenir

- Un modèle paramétrique est un historique, pas un dessin.
- Une bonne esquisse est **totalement contrainte** : géométrie d'abord, cotes ensuite.
- Une esquisse simple par fonction, sur un plan de référence, centrée sur l'origine.
- L'intention de conception : le modèle doit réagir aux modifications comme la pièce réelle.
"""}


# ===========================================================================
# FICHE 5.2 — FONCTIONS VOLUMIQUES ET STRATÉGIE DE MODÉLISATION
# ===========================================================================

FICHES["5.2"] = {"cours": """
### 1. Quatre fonctions suffisent pour 90 % des pièces

Toutes les formes que vous aurez à modéliser en première année se construisent avec quatre
fonctions de base. Chacune répond à une question simple : **comment la matière est-elle créée ?**

| Fonction | Principe | Pièces typiques |
|---|---|---|
| **Extrusion** | l'esquisse avance en ligne droite | plaques, brides, entretoises, profilés |
| **Révolution** | l'esquisse tourne autour d'un axe | arbres, bagues, poulies, tout ce qui est tourné |
| **Balayage** | l'esquisse suit un chemin | tubes cintrés, joints, poignées |
| **Lissage** | on relie plusieurs esquisses différentes | transitions, conduits, formes ergonomiques |

Chacune a son inverse en **enlèvement de matière** : extrusion coupée (les perçages, les poches),
révolution coupée (les gorges), etc.

**Le bon réflexe : choisir la fonction qui correspond au procédé réel.** Une pièce tournée se
modélise par révolution, pas par vingt extrusions successives. Le modèle devient plus simple,
plus robuste, et plus facile à modifier.

### 2. Les fonctions d'habillage

Elles ne créent pas la forme : elles la finissent.

- **Congé** : arrondi entre deux faces. Indispensable — un angle intérieur vif n'existe pas en
  usinage (la fraise laisse toujours son rayon) et concentre les contraintes.
- **Chanfrein** : cassure d'arête, pour ne pas se couper et pour faciliter le montage.
- **Dépouille** : légère inclinaison des parois, obligatoire en moulage et en injection.
- **Coque** : évide la pièce en laissant une épaisseur constante. Une fonction, et un carter plein
  devient un carter creux.

### 3. Les fonctions de duplication : ne jamais copier à la main

- **Symétrie** : la moitié de la pièce, puis on la reflète.
- **Répétition linéaire ou circulaire** : une fois le trou fait, on le répète.

Douze trous répétés, c'est **une** fonction à modifier — pas douze. Copier-coller manuellement
douze perçages, c'est se condamner à douze corrections à chaque changement.

### 4. L'ordre des fonctions : la vraie compétence

[[FIG:arbre_de_creation]]

Les congés et chanfreins **doivent venir en fin d'arbre**. Placés trop tôt, ils font disparaître
les arêtes vives sur lesquelles s'appuient les fonctions suivantes, et le modèle s'effondre à la
première modification.

L'ordre type d'un modèle propre :

1. la forme générale (extrusion ou révolution) ;
2. les enlèvements de matière importants (poches, épaulements) ;
3. les perçages, faits avec **l'assistant de perçage** ;
4. les répétitions et symétries ;
5. les congés, chanfreins et dépouilles ;
6. la coque, si nécessaire.

**Pourquoi l'assistant de perçage plutôt qu'un cercle extrudé ?** Parce qu'il connaît les normes :
il crée un vrai taraudage M8, avec son lamage, sa profondeur de filetage et son fond de foret à
118°. Et surtout, cette information se retrouve automatiquement dans la mise en plan et la
nomenclature. Un cercle extrudé, lui, n'est qu'un trou anonyme.

### 5. Un mot sur la modélisation surfacique

L'approche volumique (« solide ») convient à toute la mécanique classique. Pour les formes
complexes — carrosserie, coques de produits, pièces de style — on travaille en **surfacique** :
on construit des peaux, on les raccorde, puis on les coud pour obtenir un volume fermé.

En première année, on en reste à la culture générale : savoir que ça existe, et que c'est le
domaine de CATIA dans l'automobile et l'aéronautique.

### 6. Le test de robustesse

Comment savoir si votre modèle est bon ? Faites ce test, il prend une minute :

> **Changez deux cotes majeures — la longueur, la hauteur, un diamètre — et regardez l'arbre.**
> Aucune erreur ? Le modèle est robuste. Des points d'exclamation ? Corrigez maintenant, pas
> dans six mois.

Ensuite, remettez les valeurs d'origine. Ce test coûte une minute et sauve des heures.

### 7. Les erreurs classiques

1. **Congés en début d'arbre.**
2. **Perçages faits au cercle extrudé** au lieu de l'assistant.
3. **Copies manuelles** au lieu de répétitions.
4. **Esquisses appuyées sur des faces** créées par des fonctions tardives.
5. **Un modèle en soixante fonctions** là où douze suffiraient : chaque fonction inutile est un
   point de rupture supplémentaire.
6. **Aucune fonction renommée.**

### 8. À retenir

- Quatre fonctions de base : extrusion, révolution, balayage, lissage.
- On modélise comme la pièce est fabriquée.
- Répétitions et symétries plutôt que copies manuelles.
- Congés, chanfreins, dépouilles **en fin d'arbre**, toujours.
- Test de robustesse : je change deux cotes, rien ne casse.
"""}


# ===========================================================================
# FICHE 5.3 — ASSEMBLAGES, MISE EN PLAN ET FORMATS D'ÉCHANGE
# ===========================================================================

FICHES["5.3"] = {"cours": """
### 1. Assembler, c'est reproduire les liaisons réelles

Un assemblage n'est pas un empilement de pièces posées côte à côte : c'est un **mécanisme**. Les
contraintes d'assemblage (coïncidence, concentricité, distance, angle) doivent reproduire les
liaisons réelles du mécanisme.

Le contrôle qui ne trompe pas :

> **Les degrés de liberté qui restent dans l'assemblage doivent être exactement ceux du schéma
> cinématique.**

Un arbre monté dans deux paliers doit pouvoir tourner et rien d'autre. Si vous pouvez encore le
faire coulisser à la souris, votre assemblage est incomplet — ou votre conception est fausse.
Dans les deux cas, il faut le savoir maintenant.

**Le premier composant est fixe** (ancré) : c'est le bâti. Tous les autres se positionnent par
rapport à lui.

### 2. Ascendant ou descendant

- **Ascendant (bottom-up)** : on modélise les pièces séparément, puis on les insère et on les
  contraint. C'est l'approche la plus courante, la plus stable, et celle qu'on attend de vous en
  première année.
- **Descendant (top-down)** : on crée les pièces directement dans le contexte de l'assemblage, en
  s'appuyant sur la géométrie des voisines. Très puissant pour qu'un carter épouse exactement son
  contenu, mais **fragile** : chaque référence externe est un lien qui peut casser. Si on modifie
  la pièce A, la pièce B tombe en erreur.

Le compromis professionnel : piloter l'ensemble par une **esquisse de layout** ou un squelette,
et par une table de paramètres, plutôt que par des références croisées entre pièces.

### 3. Ce que l'assemblage permet de vérifier avant de fabriquer

C'est tout l'intérêt de la maquette numérique :

- **détection d'interférences** : deux pièces qui occupent le même espace ;
- **simulation de mouvement** : on anime le mécanisme et on regarde s'il fonctionne sur toute la
  course, sans collision ;
- **accessibilité au montage** : peut-on réellement passer une clé ? Une vis inaccessible sur
  écran sera inaccessible en atelier ;
- **masse et centre de gravité**, calculés automatiquement.

Une heure de vérification sur maquette évite des semaines de reprise à l'atelier.

### 4. La mise en plan : le document qui engage

La mise en plan est générée **depuis** le modèle 3D : vues, coupes, sections, détails, vues
éclatées, tout est associatif — modifiez la pièce, le plan suit.

Mais la 3D ne contient pas tout. C'est vous qui ajoutez :

- la **cotation fonctionnelle** et les tolérances ;
- les **tolérances géométriques** et les états de surface ;
- la **matière**, les traitements, l'indice de révision ;
- la **nomenclature** avec ses bulles, sur un dessin d'ensemble.

> **La 3D montre, le plan coté engage.** En cas de litige avec un fournisseur, c'est le plan qui
> fait foi, pas le fichier 3D.

### 5. Les formats d'échange : le point qui piège tout le monde

[[FIG:formats_echange]]

Trois règles pratiques :

1. **On envoie du STEP** à un autre bureau d'études. Il contient la géométrie exacte et s'ouvre
   dans tous les logiciels.
2. **On envoie du STL** à une imprimante 3D — et uniquement là. Un STL est une peau de triangles :
   la géométrie n'est plus qu'approchée, et on ne remodélise jamais dessus. Si un fournisseur vous
   envoie un STL alors que vous devez modifier la pièce, **redemandez un STEP**.
3. **On envoie du DXF** au découpeur laser, accompagné du PDF du plan (rayons de pliage, sens des
   plis, matière, épaisseur).

### 6. Préparer une pièce pour l'impression 3D

Puisque c'est au programme et que votre fils en fera : quelques règles qui évitent l'échec.

- **Orienter la pièce** : une impression FDM est anisotrope, elle se sépare entre les couches.
  Les efforts doivent travailler **dans le plan des couches**, jamais perpendiculairement.
- **Limiter les porte-à-faux** au-delà de 45° : au-delà, il faut des supports, qui laissent des
  traces et se retirent mal.
- **Prévoir du jeu** : 0,2 à 0,4 mm entre deux pièces qui doivent s'emboîter. Une cote nominale
  exacte donnera un montage impossible.
- **Épaissir** : un mur de moins de 1,2 mm est fragile.

### 7. Les erreurs classiques

1. **Un assemblage sur-contraint** ou, pire, qui laisse des mouvements impossibles dans la réalité.
2. **Ne pas ancrer le premier composant.**
3. **Abuser du top-down** : la moindre modification propage des erreurs partout.
4. **Envoyer un STL à un bureau d'études** au lieu d'un STEP.
5. **Livrer seulement le 3D**, sans plan coté : rien n'est contractuel.
6. **Oublier de vérifier les interférences** avant de lancer la fabrication.

### 8. À retenir

- Les degrés de liberté restants = ceux du schéma cinématique.
- Premier composant ancré, ascendant par défaut, top-down avec prudence.
- Vérifier interférences, mouvement et accessibilité **avant** de fabriquer.
- STEP = échange exact · STL = impression · DXF = tôle à plat · PDF = diffusion.
- Le plan coté fait foi, pas le modèle 3D.
"""}


# ===========================================================================
# FICHE 6.1 — LIAISONS MÉCANIQUES ET SCHÉMA CINÉMATIQUE
# ===========================================================================

FICHES["6.1"] = {"cours": """
### 1. Décrire un mécanisme sans dessiner les pièces

Imaginez que vous deviez expliquer au téléphone comment fonctionne un étau. Vous n'allez pas
décrire la forme des pièces : vous allez dire **ce qui tourne, ce qui coulisse, ce qui est fixe**.
C'est exactement ce que fait le schéma cinématique : il décrit les **mouvements**, pas les formes.

Deux mécanismes très différents d'aspect peuvent avoir le même schéma. Et inversement, deux
pièces qui se ressemblent peuvent avoir des liaisons totalement différentes.

### 2. Compter ce qui peut bouger

Un solide libre dans l'espace possède **six degrés de liberté** (ddl) : trois translations et
trois rotations. Une liaison mécanique supprime certains de ces mouvements, et **ce qui reste
donne son nom à la liaison**.

[[FIG:liaisons_de_base]]

Les liaisons à connaître en première année :

| Liaison | ddl | Ce qui reste possible | Exemple |
|---|---|---|---|
| encastrement | 0 | rien | pièces vissées, soudées |
| pivot | 1 | une rotation | arbre sur roulements, charnière |
| glissière | 1 | une translation | tiroir, table de fraiseuse |
| pivot glissant | 2 | rotation + translation, même axe | tige de vérin dans son guide |
| hélicoïdale | 1 | rotation **liée** à une translation | système vis-écrou |
| rotule | 3 | trois rotations | rotule de direction |
| appui plan | 3 | deux translations + une rotation | pièce posée sur un marbre |
| linéaire annulaire | 4 | — | contact court sur un arbre |
| ponctuelle | 5 | — | contact en un point |

Un cas particulier utile : la liaison **hélicoïdale** n'a qu'un seul degré de liberté, parce que
la rotation et la translation ne sont pas indépendantes — c'est le pas de la vis qui les lie.

### 3. La méthode en trois temps

**Temps 1 — les classes d'équivalence.** On regroupe toutes les pièces qui n'ont **aucun
mouvement relatif** entre elles. La visserie, les rondelles, les clavettes, les goupilles
disparaissent : elles ne servent qu'à réaliser un encastrement. Un étau se ramène ainsi à trois
groupes, pas à quinze pièces.

**Temps 2 — le graphe des liaisons.** Un cercle par classe, un trait par liaison, le nom et l'axe
sur le trait. C'est un brouillon, mais il évite d'oublier une liaison.

**Temps 3 — le schéma.** On remplace chaque trait par le symbole normalisé, en respectant la
position relative réelle des liaisons. Avec un repère, propre, et les classes numérotées.

### 4. Isostatique ou hyperstatique : le point qui compte vraiment

Un montage est **isostatique** quand chaque mouvement est supprimé **une seule fois**. Il est
**hyperstatique** quand plusieurs liaisons suppriment le même mouvement.

[[FIG:isostatique_hyperstatique]]

Pourquoi c'est un vrai problème :

- il faut des **tolérances beaucoup plus serrées** (donc plus chères) pour que les pièces
  s'assemblent quand même ;
- les pièces se **contraignent entre elles** : elles se déforment, forcent, chauffent ;
- la dilatation n'est plus absorbée.

**La parade classique** : on remplace une liaison par une liaison à moins de contacts. Deux
paliers dont un libre axialement, un roulement à rotule sur un arbre long, un appui ponctuel
plutôt qu'un appui plan.

Nuance importante : l'hyperstatisme n'est pas interdit. Il est parfois voulu, pour la rigidité
(un bâti de machine-outil). Mais il doit être **choisi**, jamais subi par ignorance.

### 5. La mise en position isostatique : la règle 3-2-1

Pour poser une pièce de façon parfaitement définie — en montage d'usinage comme en conception —
on supprime les six degrés de liberté avec six points d'appui, répartis ainsi :

- **3 points** sur la face principale : elle supprime une translation et deux rotations ;
- **2 points** sur une face latérale : une translation et une rotation ;
- **1 point** sur la dernière face : la dernière translation.

C'est la règle **3-2-1**. Elle explique pourquoi les tables de fraiseuse et les montages d'usinage
sont conçus comme ils le sont, et pourquoi une pièce posée sur quatre points bascule toujours.

### 6. Les erreurs classiques

1. **Faire apparaître la visserie** sur le schéma : elle fait partie d'une classe d'équivalence.
2. **Confondre pivot et pivot glissant.** Si la pièce peut aussi coulisser, ce n'est pas un pivot.
3. **Oublier de vérifier les ddl restants** : ils doivent correspondre aux mouvements réels.
4. **Bloquer deux fois le même mouvement** sans s'en rendre compte.
5. **Dessiner des formes** sur un schéma cinématique : il ne montre que des liaisons.

### 7. À retenir

- 6 ddl : 3 translations + 3 rotations. La liaison se nomme par ce qui reste.
- Méthode : classes d'équivalence → graphe → schéma.
- La visserie n'apparaît jamais.
- Isostatique = chaque mouvement supprimé une seule fois.
- Mise en position : règle 3-2-1.
"""}


# ===========================================================================
# FICHE 6.2 — GUIDAGE EN ROTATION : PALIERS ET ROULEMENTS
# ===========================================================================

FICHES["6.2"] = {"cours": """
### 1. Faire tourner un arbre : trois familles de solutions

**Contact direct (palier lisse, coussinet, bague bronze ou polymère).** L'arbre frotte
directement dans une bague. C'est silencieux, très compact radialement, insensible aux chocs et à
la poussière, et bon marché. En contrepartie : frottement plus élevé, échauffement, vitesse
limitée, et il faut lubrifier. Idéal pour les mouvements lents, alternatifs, ou en milieu sale.

**Roulement.** On remplace le frottement de glissement par du roulement de billes ou de rouleaux.
Rendement excellent, guidage précis, vitesses élevées, entretien réduit. Mais : plus encombrant,
sensible aux chocs, au désalignement et à la pollution, et plus cher.

**Film fluide (palier hydrodynamique).** L'arbre flotte sur un coin d'huile. Réservé aux très
grandes vitesses et fortes charges : turbines, vilebrequins de moteurs thermiques.

En première année, on conçoit surtout avec des roulements, et c'est là que se concentrent les
règles à connaître.

### 2. Choisir un type de roulement

| Type | Charge radiale | Charge axiale | Quand l'utiliser |
|---|---|---|---|
| billes à gorge profonde | moyenne | moyenne, deux sens | **le choix par défaut** : simple, économique |
| rouleaux cylindriques | forte | aucune | fortes charges radiales, palier libre |
| billes à contact oblique | moyenne | forte, **un sens** | charges combinées — **toujours par paire** |
| rouleaux coniques | forte | forte, un sens | roues de véhicules, broches — **par paire** |
| à rotule | moyenne | faible | arbres longs, carters peu précis (désalignement) |
| butée | aucune | forte | charge purement axiale, ne guide pas |

Retenez le réflexe : **on part toujours du roulement à billes à gorge profonde**, et on ne change
que si une contrainte l'impose.

### 3. La règle des charges : quelle bague serrer ?

C'est le point le plus important de toute la fiche, et celui qui distingue un montage qui dure
d'un montage qui se détruit en quelques semaines.

[[FIG:regle_des_charges]]

Formulée simplement :

> **La bague qui tourne par rapport à la direction de la charge est montée SERRÉE.**
> **La bague qui reste fixe par rapport à la charge est montée GLISSANTE.**

Cas courant — arbre tournant, charge fixe (un réducteur, une pompe) : bague intérieure serrée
(**arbre en k6** ou m6), bague extérieure glissante (**alésage en H7**).

Cas inverse — moyeu tournant, charge fixe (un tambour de convoyeur, une roue folle) : bague
extérieure serrée (**alésage en M7** ou N7), bague intérieure glissante (**arbre en h6** ou g6).

Et le pourquoi : si la bague qui devrait être serrée est montée avec du jeu, elle tourne
lentement sur sa portée — on dit qu'elle **flue**. La portée est matée, du jeu apparaît, et le
montage est détruit.

### 4. Palier fixe, palier libre

Sur un arbre à deux paliers, **un seul** assure le positionnement axial. L'autre doit pouvoir
coulisser pour absorber la dilatation thermique et les écarts de longueur.

Le rappel visuel est dans la fiche 6.1 : deux paliers bloqués, c'est la précontrainte, puis
l'échauffement, puis le grippage.

Comment réaliser le palier libre ? Trois façons : laisser la bague extérieure libre dans son
alésage (le plus courant), utiliser un roulement à rouleaux cylindriques dont les rouleaux
coulissent, ou monter une bague avec un jeu axial contrôlé.

### 5. Lubrification et étanchéité

**Graisse** : simple, reste en place, protège de la pollution. On remplit environ **un tiers du
volume libre**, jamais plus : trop de graisse chauffe autant que pas assez. Suffisante jusqu'à
des vitesses moyennes.

**Huile** : nécessaire à haute vitesse, et quand il faut évacuer la chaleur (réducteurs par
barbotage).

**Étanchéité** : joint à lèvres (portée d'arbre rectifiée **Ra 0,8**, lèvre orientée vers
l'intérieur pour retenir l'huile), déflecteur, chicane, ou roulement étanche 2RS pour les cas
simples et sans entretien.

### 6. Les détails de montage qui font la différence

- Le **rayon du congé d'épaulement** de l'arbre doit être **inférieur** au rayon de la bague,
  sinon la bague porte sur le congé et non sur l'épaulement.
- On **ne monte jamais un roulement en frappant sur la bague opposée** : l'effort doit passer par
  la bague qu'on emmanche, sinon les pistes sont marquées (brinelling).
- Prévoir un **chanfrein d'introduction** sur l'arbre pour ne pas couper la lèvre du joint.
- Prévoir la **dépose** : un roulement se démonte à l'extracteur, il faut de la place pour ses
  griffes.

### 7. Les erreurs classiques

1. **Deux paliers bloqués axialement.**
2. **Inverser la règle des charges** : la bague tournante montée glissante.
3. **Portée d'arbre brute** sous un joint à lèvres : le joint fuit en quelques heures.
4. **Trop de graisse.**
5. **Roulement à contact oblique monté seul.**
6. **Épaulement avec un congé trop grand.**

### 8. À retenir

- Par défaut : roulement à billes à gorge profonde.
- Charge tournante par rapport à la bague → serrée. Charge fixe → glissante.
- Cas courant : arbre k6, alésage H7.
- Un seul palier fixe par arbre.
- Graisse : un tiers du volume. Joint à lèvres : portée Ra 0,8.
"""}


# ===========================================================================
# FICHE 6.3 — GUIDAGE EN TRANSLATION, ASSEMBLAGES ET TRANSMISSION
# ===========================================================================

FICHES["6.3"] = {"cours": """
### 1. Guider en translation

Faire coulisser une pièce proprement demande deux choses : **guider** (empêcher tous les
mouvements sauf un) et **éviter l'arc-boutement**.

L'arc-boutement, c'est ce qui se passe quand un tiroir se coince parce qu'on tire d'un seul côté.
La règle est géométrique : **la longueur de guidage doit valoir environ 1,5 à 2 fois la course**,
ou au moins le double de la distance entre le point d'application de l'effort et l'axe de
guidage. Un guidage trop court se coince, quel que soit le soin apporté à l'usinage.

Les solutions courantes, du plus simple au plus performant : glissière prismatique ou en queue
d'aronde (machines-outils, réglable par lardon), arbre et douille (simple, économique), douille à
billes (frottement très faible), rail à patins à billes (précision et rigidité, standard de
l'industrie), et guidage par galets pour les grandes courses.

### 2. La visserie : ce qui tient vraiment un assemblage

Un point contre-intuitif : dans un assemblage boulonné correct, **ce ne sont pas les vis qui
travaillent en cisaillement**. Le serrage étire la vis, qui se comporte comme un ressort tendu :
cette **précharge** plaque les pièces l'une contre l'autre, et c'est **l'adhérence** entre les
pièces qui transmet l'effort.

D'où trois conséquences :

- un serrage insuffisant est **la première cause de desserrage** sous vibrations ;
- on serre à la **clé dynamométrique**, avec le couple correspondant à la classe de la vis ;
- la rondelle plate **ne freine rien** : elle répartit la pression sous la tête.

**Boulon, vis ou goujon ?** Boulon (vis + écrou) quand on accède des deux côtés : le plus
économique. Vis dans un taraudage quand on n'accède que d'un côté. **Goujon** quand la pièce
taraudée est en aluminium et qu'on démonte souvent : le goujon reste en place, le démontage se
fait sur l'écrou, et le taraudage fragile est préservé.

**Classe de qualité** : 8.8, 10.9, 12.9. Le premier nombre × 100 donne Rm en MPa, le produit des
deux × 10 donne Re. Une 8.8 : Rm = 800 MPa, Re = 640 MPa.

**Freinages** : par obstacle (goupille fendue, fil frein, rondelle arrêtoir) ou par adhérence
(écrou Nylstop, rondelle à dents, frein filet chimique).

### 3. Transmettre le couple entre un arbre et un moyeu

[[FIG:liaison_arbre_moyeu]]

Le point à ne pas confondre :

> **La clavette transmet le couple. Elle ne maintient JAMAIS le moyeu axialement.**

L'arrêt axial se fait par un épaulement (le plus solide), un anneau élastique, un écrou, une
entretoise ou une vis en bout d'arbre. Et le **centrage** vient de l'ajustement — typiquement
H7/j6 ou H7/k6 — pas de la clavette.

Une clavette travaille par **matage sur ses flancs** : elle est ajustée sans jeu latéralement,
mais avec du jeu en fond de rainure. La remplacer par une plus courte fait grimper la pression,
mate les rainures et finit par casser.

### 4. Transmettre la puissance entre deux arbres

| Solution | Rendement | Points forts | Limites |
|---|---|---|---|
| engrenages | 0,97 par étage | compact, rapport rigoureux | bruyant, carter lubrifié, entraxe précis |
| courroie | 0,95 | silencieuse, amortit, grand entraxe, patine en cas de blocage | glissement (sauf crantée), tension sur les paliers |
| chaîne | 0,96 | pas de glissement, milieux difficiles | bruyante, lubrification, rattrapage de tension |
| roue et vis sans fin | 0,5 à 0,8 | grand rapport en un étage, renvoi à 90°, souvent irréversible | rendement faible, échauffement |

[[FIG:engrenage_module]]

Les formules de l'engrenage droit, à savoir de tête :

- rapport **r = Z menante / Z menée** — et pour un train, on multiplie les rapports ;
- diamètre primitif **d = m × Z** ; entraxe **a = m (Z1 + Z2) / 2** ;
- deux roues qui engrènent ont **obligatoirement le même module** ;
- environ **17 dents minimum** pour éviter l'interférence de taillage.

Et le lien avec la puissance, déjà vu en RDM : **P = C ω**, donc **diviser la vitesse par 5
multiplie le couple par 5**. L'arbre de sortie d'un réducteur est toujours nettement plus gros
que celui d'entrée.

### 5. L'étanchéité

- **Statique** (entre deux pièces fixes) : joint plat, joint torique dans sa gorge, pâte à joint.
  Le joint torique doit être **comprimé de 15 à 30 %**, jamais écrasé à fond.
- **Dynamique** (une pièce bouge) : joint à lèvres pour un arbre tournant, joint racleur pour une
  tige de vérin, chicane ou déflecteur quand il n'y a pas de contact.

Réflexe de conception : partout où il y a un joint dynamique, la portée doit être **rectifiée
Ra 0,8**, avec un chanfrein d'introduction.

### 6. Les erreurs classiques

1. **Guidage trop court** par rapport à la course : arc-boutement garanti.
2. **Compter sur la clavette pour tenir axialement.**
3. **Serrer au jugé** au lieu de la clé dynamométrique.
4. **Croire qu'une rondelle plate freine.**
5. **Oublier que la tension d'une courroie charge les paliers** — parfois plus que le couple.
6. **Monter deux roues de modules différents** : elles ne peuvent pas engrener.

### 7. À retenir

- Longueur de guidage ≈ 1,5 à 2 × course, sinon arc-boutement.
- C'est la précharge qui tient un assemblage vissé, pas le cisaillement des vis.
- Classe 8.8 → Re = 640 MPa · 10.9 → Re = 900 MPa.
- La clavette transmet le couple ; l'épaulement tient axialement ; l'ajustement centre.
- d = m Z · a = m (Z1+Z2)/2 · même module obligatoire · r = Z menante / Z menée.
"""}


# ===========================================================================
# FICHE 2.2 — LES AJUSTEMENTS (version regroupée ici avec les autres)
# ===========================================================================

FICHES["2.2"] = {"cours": """
### 1. Le problème, avant tout vocabulaire

Tu dois faire tourner un axe de 30 mm dans un trou de 30 mm.

Question toute bête : est-ce que ça tourne ?

**Non.** Si le trou fait exactement 30 et l'axe exactement 30, l'axe entre en force,
ou n'entre pas du tout. Pour que ça tourne, il faut **du vide entre les deux**.

Deuxième problème : aucune machine ne sort du 30,000 exact. Chaque pièce sort un peu
différente de la précédente.

[[FIG:pourquoi_tolerance]]

Le concepteur ne peut donc pas écrire « 30 » sur son plan. Il doit écrire :
**« fais-moi un trou entre telle et telle valeur, et un axe entre telle et telle valeur,
et je te garantis que ça tournera à tous les coups »**.

### 2. Trois situations possibles, pas une de plus

Quand on assemble un trou et un axe fabriqués chacun dans leur fourchette, il n'y a que
trois résultats possibles.

[[FIG:trois_ajustements]]

- **Il reste toujours du vide** → la pièce tourne ou coulisse. On dit qu'il y a du **jeu**.
- **L'axe est toujours trop gros** → il faut le forcer à la presse. On dit qu'il y a **serrage**.
- **Ça dépend de la pièce qu'on prend** → parfois un peu de vide, parfois un peu de serrage.
  On dit que c'est **incertain**.

C'est tout. Un montage de mécanique, c'est forcément l'un de ces trois cas.

Le mot qui désigne cette association trou + axe s'appelle un **ajustement**.
Tu viens de comprendre la chose avant d'apprendre le mot : c'est le bon ordre.

### 3. Comment on l'écrit sur un plan

Écrire à chaque fois « trou entre 30,000 et 30,021 » serait long. La norme ISO a donc
inventé un code, toujours le même :

[[FIG:lire_h7g6]]

Les tables ISO donnent ensuite les valeurs exactes, et le **calculateur d'ajustements**
de cette application les affiche directement.

### 4. Le seul calcul à savoir faire

Deux soustractions, et rien d'autre :

- **Le vide le plus grand possible** = le plus grand trou − le plus petit axe
- **Le vide le plus petit possible** = le plus petit trou − le plus gros axe

Pour Ø30 H7/g6 :

| | plus petit | plus grand |
|---|---|---|
| Trou (H7) | 30,000 | 30,021 |
| Axe (g6) | 29,980 | 29,993 |

- Vide maxi = 30,021 − 29,980 = **0,041 mm**
- Vide mini = 30,000 − 29,993 = **0,007 mm**

Il reste donc **toujours** entre 7 et 41 millièmes de millimètre de vide. Ça tourne, quelle
que soit la pièce qu'on attrape dans le bac. C'est exactement ce qu'on voulait.

*Si un résultat sort négatif, ce n'est pas une erreur : ça veut dire que l'axe est plus gros
que le trou. Ce n'est plus du vide, c'est du serrage.*

### 5. Les trois ajustements à connaître par cœur en première année

| Écriture | Ce que ça fait | Où on le trouve |
|---|---|---|
| **H7/g6** | ça tourne librement | un axe dans son palier, une tige de vérin |
| **H7/k6** | ça se centre bien, ça se démonte au maillet | une bague de roulement sur son arbre |
| **H7/p6** | c'est bloqué, il faut une presse | une bague montée à demeure |

Retiens la logique plutôt que la liste : **plus la lettre de l'axe avance dans l'alphabet,
plus l'axe est gros, et plus on serre.**

### 6. L'erreur que tout le monde fait la première fois

Confondre la majuscule et la minuscule. **H7 c'est le trou, g6 c'est l'axe.** Inversés, le
montage prévu pour tourner devient un montage bloqué — et la pièce part à la benne.

Moyen mnémotechnique : la majuscule est **grande**, comme le trou qui doit accueillir l'autre.
"""}


# ===========================================================================
# EXERCICES D'ÉCHAUFFEMENT — BLOC 1
# Ajoutés AVANT l'exercice de niveau examen, qui reste en place.
# ===========================================================================

FICHES["1.1"]["exercice_avant"] = """
### Exercice d'échauffement — Un support de vélo dans un couloir d'immeuble

*Celui-ci se traite en dix minutes, avec le cours sous les yeux. Il sert à prendre le geste
avant l'exercice de niveau examen qui suit.*

Un habitant en a assez de laisser son vélo dans l'entrée, où il gêne le passage. Il veut le
suspendre au mur du couloir, à un endroit où passent aussi ses voisins.

**1.** Écris la bête à cornes : à qui le produit rend-il service ? Sur quoi agit-il ? Dans quel but ?

**2.** Parmi ces trois phrases, une seule est une fonction correctement écrite. Laquelle, et
pourquoi les deux autres sont-elles fausses ?
   - a) « Utiliser deux crochets en acier galvanisé »
   - b) « Maintenir le vélo en hauteur contre le mur »
   - c) « Le support doit être solide »

**3.** Cite **trois** éléments du milieu extérieur autres que l'utilisateur et le vélo.

**4.** La phrase « ne pas gêner le passage des voisins » est-elle une FP ou une FC ? Justifie en
une ligne.

**5.** Rends cette exigence exploitable : « le support doit être facile à utiliser ». Donne un
critère, un niveau chiffré et une flexibilité.
"""

FICHES["1.1"]["corrige_avant"] = """
### Corrigé de l'exercice d'échauffement

**1. Bête à cornes**

- **À qui rend-il service ?** À l'habitant (celui qui a le problème et qui achète).
- **Sur quoi agit-il ?** Le vélo — c'est la matière d'œuvre.
- **Dans quel but ?** Ranger le vélo en hauteur pour libérer le passage dans le couloir.

*Le piège habituel serait de répondre « sur le mur ». Le mur n'est pas ce qu'on veut déplacer :
c'est un élément du milieu extérieur, pas la matière d'œuvre.*

**2. La bonne réponse est la b)**

- a) est une **solution technique** : elle nomme des composants et un matériau. En l'écrivant
  dans le cahier des charges, on s'interdit de proposer une sangle, un rail ou une potence.
- b) est correcte : **verbe à l'infinitif + complément**, aucune technologie imposée.
- c) n'est **pas chiffrée** : solide comment ? Combien de kilos, pendant combien d'années ?
  Ce n'est ni vérifiable, ni contestable.

**3. Trois éléments du milieu extérieur** (parmi d'autres possibles)

Le mur (nature, résistance de la fixation) — les voisins et le passage — le sol et la peinture
(traces, rayures) — l'humidité du couloir — le budget — le règlement de copropriété.

**4. C'est une fonction contrainte (FC)**

Elle relie le produit à **un seul** élément du milieu extérieur : les voisins. Une FP traverse
le produit et relie deux éléments — ici, ce serait « permettre à l'habitant de ranger son vélo »,
qui relie l'habitant et le vélo.

**5. Exigence rendue exploitable**

> **FC — Permettre l'accrochage sans effort excessif.**
> Critère : effort de levage à exercer par l'utilisateur.
> Niveau : ≤ 12 kg soulevés à moins de 1,60 m de hauteur.
> Flexibilité : F1 (peu négociable).

On pourrait ajouter un second critère : temps d'accrochage inférieur à 10 secondes, sans outil.
Deux exigences chiffrées valent mieux qu'une phrase vague.
"""

FICHES["1.2"]["exercice_avant"] = """
### Exercice d'échauffement — Lire une pièce simple

*À faire avec le cours ouvert. Une feuille de brouillon et un crayon suffisent.*

Une pièce en L : une semelle de **80 × 50**, épaisseur **12**, et un dos vertical de **50** de
haut sur toute la largeur, épaisseur **12**. La semelle est percée d'un trou débouchant **Ø10**,
situé à 20 mm du bord droit et centré en largeur. Le dos porte un trou borgne **Ø8**, profond
de 8 mm, au centre.

**1.** Combien de vues sont nécessaires pour définir complètement cette pièce ? Laquelle choisis-tu
comme vue de face, et pourquoi ?

**2.** Sur la vue de dessus, avec quel type de trait apparaissent : le contour de la semelle ?
Le trou Ø10 ? Le trou borgne Ø8 du dos ?

**3.** Où se place la vue de dessus par rapport à la vue de face, et pourquoi ?

**4.** On veut montrer clairement le trou borgne du dos sans couvrir le dessin de pointillés.
Que proposes-tu ?

**5.** Le plan est à l'échelle 1:2. Sur la feuille, tu mesures 40 mm entre deux arêtes. Quelle
cote est inscrite sur le plan ?
"""

FICHES["1.2"]["corrige_avant"] = """
### Corrigé de l'exercice d'échauffement

**1. Deux vues suffisent**

Une vue de face (la pièce vue de côté, qui montre le L) et une vue de dessus. On choisit comme
vue de face **celle qui montre le plus de détails significatifs** : ici, le profil en L, qui
donne d'un coup les deux épaisseurs et la hauteur du dos.

*Ajouter une troisième vue ne serait pas faux, mais inutile : chaque vue en trop est une occasion
de contradiction entre les vues.*

**2. Les traits sur la vue de dessus**

- Contour de la semelle (80 × 50) : **trait continu fort** — c'est vu.
- Trou Ø10 : il traverse la semelle de haut en bas, donc on le voit réellement d'en haut :
  **trait continu fort**, plus ses **deux axes en trait mixte fin**.
- Trou borgne Ø8 du dos : il est percé horizontalement dans le dos ; vu de dessus, il est
  **caché** dans la matière → **traits interrompus fins**, avec son axe en trait mixte fin.

**3. La vue de dessus se place EN DESSOUS de la vue de face**

Parce qu'on travaille en **méthode européenne** : l'observateur regarde d'en haut et la vue se
projette derrière la pièce. Les largeurs restent rigoureusement alignées avec celles de la vue
de face — jamais de décalage.

**4. Une coupe locale**

Le trou borgne est un détail isolé : une **coupe locale** (ou partielle), limitée par un trait
continu fin ondulé, ouvre juste la zone du trou. On y voit alors le perçage en trait fort, avec
sa profondeur et le fond conique laissé par le foret.

Une coupe complète serait exagérée : elle supprimerait de la matière sur tout le dessin pour un
seul détail.

**5. La cote inscrite est 80**

À l'échelle 1:2, la pièce est dessinée **deux fois plus petite** : 40 mm sur la feuille
correspondent à 80 mm en réalité. Et sur le plan, on inscrit **toujours la cote réelle**.

*Retenir : une cote se lit, elle ne se mesure jamais à la règle sur la feuille.*
"""

FICHES["1.3"]["exercice_avant"] = """
### Exercice d'échauffement — Coter une plaque de fixation

*Objectif : distinguer ce qui doit être coté précisément de ce qui ne le mérite pas.*

Une plaque rectangulaire **120 × 60**, épaisseur 8, en S235. Elle est percée de :
- **4 trous Ø6,5** pour la fixer par des vis M6 sur un carter existant, dont les taraudages sont
  espacés de 100 mm en longueur et 40 mm en largeur ;
- **1 alésage central Ø25 H7** qui reçoit une bague de guidage montée serrée.

La plaque appuie sur le carter par sa grande face. Les bords extérieurs ne touchent rien.

**1.** Quelles sont les surfaces **fonctionnelles** de cette pièce ? Quelles sont celles qui ne
le sont pas ?

**2.** Pour positionner les 4 trous, vaut-il mieux coter en chaîne (de trou à trou) ou depuis une
référence unique ? Pourquoi ?

**3.** Quelle rugosité Ra demandes-tu sur : la face d'appui ? L'alésage Ø25 H7 ? Les chants
extérieurs ?

**4.** Les cotes 120 et 60 doivent-elles porter une tolérance chiffrée ? Justifie.

**5.** Un collègue a coté : 20 — 100 — 20 en longueur, **et** la cote totale 120. Qu'en penses-tu ?
"""

FICHES["1.3"]["corrige_avant"] = """
### Corrigé de l'exercice d'échauffement

**1. Les surfaces fonctionnelles**

Fonctionnelles (elles touchent une autre pièce ou assurent une fonction) :
- la **grande face d'appui** sur le carter ;
- l'**alésage Ø25 H7**, qui reçoit la bague ;
- la **position des 4 trous**, qui doit correspondre aux taraudages existants.

Non fonctionnelles : les chants extérieurs, la face opposée, l'épaisseur exacte de la plaque.
Elles ne touchent rien : elles resteront en tolérances générales.

**2. Depuis une référence unique**

En cotation en chaîne, chaque tolérance s'ajoute à la précédente : le dernier trou peut se
retrouver décalé de la somme des dispersions, et les vis ne tombent plus en face des taraudages.

En partant d'un même bord (ou mieux, de l'axe de symétrie de la plaque), les erreurs **ne
s'accumulent plus** : chaque trou est positionné indépendamment.

*C'est la règle générale pour tout ce qui doit s'assembler avec l'existant.*

**3. Les états de surface**

| Surface | Ra | Pourquoi |
|---|---|---|
| face d'appui | **3,2** | elle doit porter à plat, un fraisage de finition suffit |
| alésage Ø25 H7 | **0,8** | portée d'une bague montée serrée : il faut une surface fine |
| chants extérieurs | **brut** | ils ne touchent rien |

Demander Ra 0,8 partout imposerait une rectification générale : le prix de la pièce serait
multiplié sans aucun gain.

**4. Non, pas de tolérance chiffrée sur 120 et 60**

Ces dimensions ne conditionnent aucun assemblage. Elles relèvent des **tolérances générales**
mentionnées au cartouche (ISO 2768-m), soit environ ± 0,3 mm ici. Ce n'est pas une cote « libre » :
c'est une tolérance implicite, contractuelle elle aussi.

**5. C'est une surabondance : il faut supprimer une cote**

20 + 100 + 20 = 120. La quatrième cote se déduit des trois autres. Elle est donc **en trop**, et
surtout **contradictoire** dès qu'on applique les tolérances : si chaque cote a ± 0,2, la somme
peut donner 119,4 comme 120,6, alors que la cote totale impose 120 ± 0,2.

L'atelier ne saurait plus laquelle respecter. On garde les cotes fonctionnelles (l'entraxe des
trous) et on supprime la cote qui se déduit.
"""


# ===========================================================================
# EXERCICES D'ÉCHAUFFEMENT — BLOC 2
# ===========================================================================

FICHES["2.1"]["exercice_avant"] = """
### Exercice d'échauffement — Lire et calculer des tolérances

*Cinq questions courtes, avec le cours et la table ISO sous les yeux.*

**1.** Une cote est écrite **50 +0,08 / −0,03**. Donne la cote maxi, la cote mini et l'IT.

**2.** Une autre cote est écrite **50 H8**, avec IT8 = 39 µm pour ce diamètre. Entre quelles
valeurs la pièce est-elle bonne ?

**3.** Deux ateliers proposent la même pièce : l'un tient un IT de 0,20 mm, l'autre un IT de
0,02 mm. Lequel est le plus cher, et environ combien de fois ?

**4.** Sur un plan, une cote de 80 ne porte aucune tolérance, et le cartouche indique
**ISO 2768-m**. L'atelier a-t-il le droit de livrer une pièce à 80,4 ? (tolérance générale de
± 0,3 pour cette plage)

**5.** Dans les écritures **Ø40 H7** et **Ø40 h7**, qu'est-ce qui change ? Les deux zones sont-elles
au même endroit ?
"""

FICHES["2.1"]["corrige_avant"] = """
### Corrigé de l'exercice d'échauffement

**1. Cote 50 +0,08 / −0,03**

- Cote maxi = 50 + 0,08 = **50,08**
- Cote mini = 50 − 0,03 = **49,97**
- IT = 50,08 − 49,97 = **0,11 mm**, soit 110 µm.

*L'IT est toujours une largeur, donc toujours positif : c'est une soustraction maxi − mini,
jamais l'inverse.*

**2. Cote 50 H8**

La lettre **H** impose EI = 0 : l'alésage part exactement du nominal.
Donc **50,000 à 50,039** (39 µm = 0,039 mm).

*Le piège est ici : la table donne des micromètres, le plan des millimètres. 39 µm ne s'écrit
pas 0,39.*

**3. Le second atelier, environ 5 fois plus cher**

Un IT de 0,20 mm s'obtient au tournage ou au fraisage standard. Un IT de 0,02 mm demande une
finition soignée et un contrôle au micromètre, avec des reprises et des rebuts.

*Règle à garder : chaque zéro gagné après la virgule coûte un multiple, pas quelques pourcents.*

**4. Non, 80,4 est refusée**

ISO 2768-m signifie que les cotes sans tolérance sont quand même tolérancées : ici ± 0,3, donc
la pièce est acceptée **entre 79,7 et 80,3**. À 80,4, elle est hors tolérance.

*Une cote sans indication n'est jamais une cote libre : le cartouche fait foi.*

**5. La majuscule change tout**

- **Ø40 H7** désigne un **alésage** (un trou). Sa zone part du nominal **vers le haut** : 40,000
  à 40,025.
- **Ø40 h7** désigne un **arbre**. Sa zone part du nominal **vers le bas** : 39,975 à 40,000.

Les deux zones sont donc symétriques par rapport à la ligne zéro, et de part et d'autre. C'est
d'ailleurs ce qui fait de H et h la base des deux systèmes normalisés : alésage normal et arbre
normal.
"""

FICHES["2.2"]["exercice_avant"] = """
### Exercice d'échauffement — Trois montages à analyser

*On applique la même méthode à chaque fois. Table ISO nécessaire pour la question 4.*

**1.** Pour chacun de ces trois besoins, dis s'il faut du **jeu**, du **serrage** ou de
l'**incertain** :
   - a) un axe de charnière de portail qui doit tourner librement ;
   - b) une bague de bronze montée à demeure dans un carter ;
   - c) une poulie qu'on démonte tous les six mois pour changer la courroie.

**2.** Classe ces quatre ajustements du plus « glissant » au plus « serrant » :
**H7/p6 · H7/g6 · H7/k6 · H8/f7**.

**3.** Un montage donne Jmax = +0,050 mm et Jmin = −0,010 mm. Comment s'appelle ce type
d'ajustement, et que se passe-t-il concrètement à l'atelier ?

**4.** Calcule l'ajustement **Ø20 H7/f7**, sachant que pour Ø20 : IT7 = 21 µm et que l'écart
supérieur de f vaut −20 µm.

**5.** Un technicien lit **Ø25 H7/k6** et monte l'arbre au maillet, sans effort. Est-ce normal ?
"""

FICHES["2.2"]["corrige_avant"] = """
### Corrigé de l'exercice d'échauffement

**1. Le bon type d'ajustement**

- a) **Jeu** — ça doit tourner, donc il faut toujours du vide (type H7/g6 ou H8/f7).
- b) **Serrage** — la bague ne doit jamais bouger dans son logement (type H7/p6).
- c) **Incertain** — il faut centrer précisément, mais pouvoir démonter (type H7/j6 ou H7/k6).

**2. Du plus glissant au plus serrant**

**H8/f7** (jeu large) → **H7/g6** (jeu faible) → **H7/k6** (incertain) → **H7/p6** (serrage).

*La logique : plus la lettre de l'arbre avance dans l'alphabet, plus l'arbre est gros, donc plus
on serre. Après h, on entre dans le serrage.*

**3. C'est un ajustement INCERTAIN**

Jmax positif = du jeu possible ; Jmin négatif = du serrage possible. Selon les pièces qu'on
attrape dans le bac, le montage se fait à la main ou demande un maillet.

*Concrètement à l'atelier : certains montages glissent, d'autres résistent. C'est voulu quand on
cherche un centrage précis mais démontable — jamais quand la pièce doit tourner.*

**4. Calcul de Ø20 H7/f7**

[[FIG:calcul_ajustement_etapes]]

Même méthode que dans le schéma ci-dessus, avec nos valeurs :

- Alésage H7 : EI = 0 → **20,000 à 20,021**
- Arbre f7 : es = −0,020, et IT7 = 0,021 → **19,959 à 19,980**
- Jeu maxi = 20,021 − 19,959 = **0,062 mm**
- Jeu mini = 20,000 − 19,980 = **0,020 mm**

Il y a donc toujours entre 20 et 62 µm de jeu : c'est un **jeu franc**, typique d'un arbre
tournant dans un coussinet lubrifié.

**5. Non, ce n'est pas normal — il faut vérifier**

k6 est un ajustement **incertain à tendance serrage** : le montage doit demander un effort, au
maillet ou à la presse. S'il glisse tout seul, deux hypothèses :

- l'arbre a été usiné **sous** la cote (trop petit) ;
- ou l'alésage est **au-dessus** de sa cote maxi.

Dans les deux cas, la pièce est hors tolérance. Si c'est une portée de roulement, la bague fluera
et matera l'arbre en quelques dizaines d'heures : il faut refuser la pièce.
"""

FICHES["2.3"]["exercice_avant"] = """
### Exercice d'échauffement — Géométrie et chaîne de cotes

**1.** Pour chacun de ces défauts, dis s'il faut une tolérance de **forme**, d'**orientation** ou
de **position**, et si une référence est nécessaire :
   - a) une face d'appui gondolée ;
   - b) un alésage percé de travers par rapport à la face d'appui ;
   - c) quatre trous décalés par rapport aux taraudages en face.

**2.** Traduis ce cadre en français courant : **⊥ | Ø0,05 | A**.

**3.** Une condition de jeu Ja doit rester entre **0,15 et 0,55 mm**. Quel est l'intervalle
disponible ITja ?

**4.** La chaîne comporte 3 cotes. En répartition uniforme, quelle tolérance pour chacune ?

**5.** Vrai ou faux : « en allongeant la chaîne de 3 à 6 pièces, on peut garder les mêmes
tolérances sur chaque pièce ». Justifie.
"""

FICHES["2.3"]["corrige_avant"] = """
### Corrigé de l'exercice d'échauffement

**1. Le bon type de tolérance**

- a) Face gondolée → **PLANÉITÉ**, tolérance de **forme**, **sans référence** (une surface est
  plane ou non, indépendamment du reste).
- b) Alésage de travers → **PERPENDICULARITÉ**, tolérance d'**orientation**, **avec référence**
  (perpendiculaire *à quoi* ? à la face d'appui A).
- c) Trous décalés → **LOCALISATION**, tolérance de **position**, **avec référence(s)** — souvent
  deux : la face d'appui A, puis un axe ou un bord B.

*La règle générale : seule la famille « forme » se passe de référence.*

**2. Traduction du cadre ⊥ | Ø0,05 | A**

« L'axe de cet élément doit rester à l'intérieur d'un **cylindre de 0,05 mm de diamètre**,
**perpendiculaire** à la surface de référence **A**. »

*Le Ø est essentiel : sans lui, la zone serait comprise entre deux plans, et la tolérance ne
serait pas la même dans toutes les directions.*

**3. Intervalle disponible**

ITja = 0,55 − 0,15 = **0,40 mm**.

**4. Répartition uniforme sur 3 cotes**

ITja = ITa + ITb + ITc, donc 0,40 ÷ 3 ≈ **0,13 mm par cote**.

*C'est confortable : de l'usinage courant suffit. Si le résultat avait donné 0,02 mm par cote,
il aurait fallu revoir la conception — chaîne plus courte ou cale de réglage.*

**5. FAUX**

Les tolérances **s'additionnent** : ITja = somme de tous les IT. Avec 6 cotes au lieu de 3 pour
le même intervalle disponible, chaque cote doit être **deux fois plus serrée**.

C'est exactement pour cette raison qu'un concepteur cherche toujours à **raccourcir la chaîne**,
ou à introduire une **cale de réglage** qui absorbe la dispersion. Une cale à 3 € remplace
avantageusement cinq pièces rectifiées.
"""


# ===========================================================================
# EXERCICES D'ÉCHAUFFEMENT — BLOC 3
# ===========================================================================

FICHES["3.1"]["exercice_avant"] = """
### Exercice d'échauffement — Lire une courbe et choisir

**1.** Sur une courbe d'essai de traction, où se lit **Re** ? Où se lit **Rm** ? À quoi correspond
la **pente** de la partie droite ?

**2.** Une barre en S235 (Re = 235 MPa) de section 200 mm² supporte 30 000 N. Calcule la
contrainte et dis si la pièce tient avec un coefficient de sécurité de 3.

**3.** On remplace cette barre par du 42CrMo4 (Re = 750 MPa), même section, même charge.
Deux questions : la pièce résiste-t-elle mieux ? S'allonge-t-elle moins ?

**4.** Une pièce en aluminium plie trop. Un collègue propose de passer du 6060 (Re = 160 MPa) au
7075 (Re = 460 MPa). Bonne idée ?

**5.** Classe ces matériaux du plus rigide au plus souple : POM · acier C45 · aluminium 6060 ·
fonte GJL.
"""

FICHES["3.1"]["corrige_avant"] = """
### Corrigé de l'exercice d'échauffement

**1. Lecture de la courbe**

- **Re** se lit à la fin de la partie droite : c'est la contrainte au-delà de laquelle la
  déformation devient **permanente**.
- **Rm** est le **point le plus haut** de la courbe : la contrainte maximale avant rupture.
- La **pente** de la partie droite, c'est **E**, le module d'Young : la rigidité du matériau.

**2. Vérification de la barre**

σ = N / S = 30 000 / 200 = **150 MPa**
Rpe = Re / s = 235 / 3 = **78,3 MPa**

150 > 78,3 : **la pièce ne tient pas.** Il faut augmenter la section, réduire la charge, ou
choisir une nuance plus résistante.

**3. Avec du 42CrMo4**

- **Résiste-t-elle mieux ? OUI.** Rpe = 750 / 3 = 250 MPa, et 150 < 250 : cette fois ça passe,
  avec de la marge.
- **S'allonge-t-elle moins ? NON — exactement pareil.** L'allongement dépend de E, et tous les
  aciers ont E ≈ 210 000 MPa.

*C'est le point le plus important de la fiche : Re et E sont deux propriétés indépendantes.*

**4. Non, mauvaise idée**

La flèche dépend de **E** et de la forme, pas de Re. Tous les alliages d'aluminium ont
E ≈ 70 000 MPa : le 7075 pliera exactement autant que le 6060, pour un prix bien plus élevé.

Les vraies solutions : augmenter la hauteur de la section, ajouter des nervures, passer à un
profil creux, réduire la portée — ou passer à l'acier, trois fois plus rigide.

**5. Du plus rigide au plus souple**

| Rang | Matériau | E approximatif |
|---|---|---|
| 1 | acier C45 | 210 000 MPa |
| 2 | fonte GJL | 105 000 MPa |
| 3 | aluminium 6060 | 70 000 MPa |
| 4 | POM | 3 000 MPa |

*Un polymère est environ 70 fois plus souple que l'acier : une pièce plastique doit être
massivement plus épaisse ou nervurée pour la même rigidité.*
"""

FICHES["3.2"]["exercice_avant"] = """
### Exercice d'échauffement — Décoder six nuances

**1.** Décode : **S355**, **C22**, **34CrMo4**, **X2CrNiMo17-12-2**.

**2.** Laquelle de ces nuances peut être trempée : S235, C45, S355 ? Pourquoi ?

**3.** Dans **25CrMo4**, quelle est la teneur réelle en chrome ?

**4.** Que signifient les désignations **EN-GJL-200** et **EN-GJS-500-7** ? Laquelle choisirais-tu
pour un bâti de machine, laquelle pour un levier qui prend des chocs ?

**5.** Un fournisseur propose **EN AW-6060** pour un profilé de structure. Est-ce cohérent ?
"""

FICHES["3.2"]["corrige_avant"] = """
### Corrigé de l'exercice d'échauffement

**1. Décodage**

- **S355** : acier de **structure**, limite élastique **Re = 355 MPa**. Soudable, pour charpente
  et mécano-soudé chargé.
- **C22** : acier **non allié** à **0,22 % de carbone**. Doux, soudable, trempe médiocre.
- **34CrMo4** : acier **faiblement allié**, **0,34 % de carbone**, chrome et molybdène, avec
  34/… non : le 4 final concerne le chrome → **≈ 1 % de chrome** (4 ÷ 4).
- **X2CrNiMo17-12-2** : acier **fortement allié** (préfixe X), 0,02 % de carbone, **17 % de
  chrome, 12 % de nickel, 2 % de molybdène**. C'est l'inox 316L, pour milieux chlorés.

**2. Seul le C45 se trempe vraiment**

Il faut **au moins 0,3 % de carbone** pour qu'une trempe ait un effet. S235 et S355 sont des
aciers de structure à faible carbone : on peut les chauffer et les refroidir, il ne se passera
pratiquement rien.

*C'est exactement pour cela que les arbres et les axes se font en C45 ou en 42CrMo4, jamais en
S235.*

**3. Teneur en chrome de 25CrMo4**

Le chiffre final, 4, se divise par le coefficient du **premier élément cité**, ici Cr, dont le
coefficient est **4** : 4 ÷ 4 = **environ 1 % de chrome**.

*L'erreur la plus fréquente est de lire 4 %. Coefficients à connaître : 4 pour Cr, Mn, Ni, Si ;
10 pour Mo, V, Al, Cu, Ti ; 100 pour P, S, N ; 1 000 pour B.*

**4. Les deux fontes**

- **EN-GJL-200** : fonte à graphite **lamellaire**, Rm = 200 MPa. Elle **amortit très bien les
  vibrations** mais casse net → **bâti de machine**.
- **EN-GJS-500-7** : fonte à graphite **sphéroïdal**, Rm = 500 MPa, allongement 7 %. Bien plus
  **ductile** → **levier qui prend des chocs**.

**5. Oui, c'est cohérent**

La série **6000** (alliage aluminium-magnésium-silicium) est celle des **profilés extrudés** :
c'est exactement l'usage visé. Le 6060 est la nuance la plus répandue pour les structures en
profilé aluminium d'atelier.
"""

FICHES["3.3"]["exercice_avant"] = """
### Exercice d'échauffement — Traitements : quel effet, dans quel ordre

**1.** Une pièce sort de trempe : elle est très dure. Peut-on la monter telle quelle ? Que
manque-t-il ?

**2.** Un pignon doit résister à l'usure des dents **et** aux chocs. Quel traitement, et sur quel
type d'acier ?

**3.** Range ces trois opérations dans le bon ordre : *rectification · trempe et revenu · ébauche
d'usinage*. Explique pourquoi cet ordre.

**4.** Un client demande une pièce en aluminium **anodisée** et une pièce en acier **anodisée**.
Où est le problème ?

**5.** Une portée d'arbre est rectifiée à Ø30 k6, puis on décide de la faire **zinguer** (8 µm par
face). Quelle conséquence ?
"""

FICHES["3.3"]["corrige_avant"] = """
### Corrigé de l'exercice d'échauffement

**1. Non — il manque le revenu**

Une pièce seulement trempée est dure **mais fragile**, et pleine de contraintes internes : elle
peut se fissurer toute seule, et casser net au premier choc.

Le **revenu** (réchauffage modéré à 200-600 °C puis refroidissement lent) fait perdre un peu de
dureté et regagner beaucoup de ténacité. **Trempe et revenu vont toujours ensemble.**

**2. Cémentation puis trempe, sur un acier à bas carbone**

On enrichit la **peau** en carbone sur 0,5 à 1,5 mm, puis on trempe : la surface durcit, le
**cœur reste tenace** parce qu'il est resté pauvre en carbone.

Aciers concernés : **16MnCr5**, 18CrMo4 — reconnaissables à leur faible teneur en carbone.
Un C45 trempé à cœur serait dur partout… et casserait au premier choc.

**3. L'ordre correct**

> **1. Ébauche d'usinage → 2. Trempe et revenu → 3. Rectification**

Parce que **toute trempe déforme** : une pièce longue peut se cintrer de plusieurs dixièmes en
sortant du bain. Si on usine à la cote finale avant de tremper, la pièce sort du four hors
tolérance, et il est trop tard. On laisse donc une surépaisseur, et la finition rattrape les
déformations.

**4. L'anodisation ne s'applique qu'à l'aluminium**

C'est une couche d'oxyde formée électrolytiquement **sur l'aluminium**. Sur l'acier, ça n'a aucun
sens : les protections adaptées sont la galvanisation, le zingage, la peinture époxy ou le
chromage dur.

**5. La cote finale est dépassée**

Un zingage de 8 µm par face ajoute **16 µm au diamètre** : Ø30 k6 (30,002 à 30,015) devient
30,018 à 30,031. La portée sort de la tolérance, et le roulement ne se montera plus correctement.

Deux solutions : usiner la portée **en tenant compte du revêtement**, ou — plus courant —
**masquer la portée** pendant le traitement et ne zinguer que le reste.

*Réflexe général : un revêtement a une épaisseur, et cette épaisseur se retrouve sur les cotes
ajustées.*
"""


# ===========================================================================
# EXERCICES D'ÉCHAUFFEMENT — BLOC 4 (RDM)
# ===========================================================================

FICHES["4.1"]["exercice_avant"] = """
### Exercice d'échauffement — Traction : trois vérifications

*Calculatrice nécessaire. On applique la même méthode à chaque fois : σ = N/S, puis Rpe = Re/s,
puis on compare.*

**1.** Une tige ronde de **Ø16** est tendue par **20 000 N**. Calcule la section, puis la
contrainte.

**2.** La tige est en S235 (Re = 235 MPa), coefficient de sécurité **s = 2**. Passe-t-elle ?

**3.** Même tige, mais on l'utilise pour lever une charge au-dessus d'un poste de travail. Le
coefficient passe à **s = 8**. Passe-t-elle encore ? Que faut-il faire ?

**4.** Cette tige mesure 1 200 mm. De combien s'allonge-t-elle sous les 20 000 N ?
(E = 210 000 MPa)

**5.** La tige comporte un épaulement à arête vive, avec Kt ≈ 3. Quelle est la contrainte réelle
à cet endroit ? Conclusion ?
"""

FICHES["4.1"]["corrige_avant"] = """
### Corrigé de l'exercice d'échauffement

**1. Section et contrainte**

S = π d² / 4 = π × 16² / 4 = **201 mm²**
σ = N / S = 20 000 / 201 = **99,5 MPa**

*En travaillant en newtons et en millimètres, le résultat sort directement en MPa.*

**2. Avec s = 2 : ça passe**

Rpe = 235 / 2 = **117,5 MPa**. Comme 99,5 < 117,5, **la condition est vérifiée**.
On utilise 85 % de l'admissible : c'est correct, mais sans grande marge.

**3. Avec s = 8 : ça ne passe plus**

Rpe = 235 / 8 = **29,4 MPa**, et 99,5 ≫ 29,4. **Refusé.**

Trois solutions possibles :
- **augmenter la section** : il faudrait S ≥ 20 000 / 29,4 = 680 mm², soit un Ø30 environ ;
- **changer de nuance** : avec du 42CrMo4 traité (Re = 750), Rpe = 94 MPa — encore un peu juste ;
- **combiner les deux**, ce qui est le choix habituel en levage.

*Retenir : le coefficient de sécurité n'est pas un détail administratif. Passer de 2 à 8
quadruple la section nécessaire.*

**4. Allongement**

ΔL = N L / (E S) = 20 000 × 1 200 / (210 000 × 201) = **0,57 mm**

*Sur 1,2 m, c'est un demi-millimètre. Négligeable pour un tirant, mais pas pour un axe de
précision : c'est pour ça qu'on vérifie toujours la déformation en plus de la résistance.*

**5. Contrainte réelle à l'épaulement**

σ réelle = Kt × σ = 3 × 99,5 = **298 MPa**

C'est **au-dessus de Re** (235 MPa) : la matière plastifie localement, et en service alterné,
une fissure s'amorce à cet endroit précis.

**Conclusion :** la pièce est correcte « en moyenne » et défaillante à l'épaulement. La parade
ne coûte rien : **remplacer l'arête vive par un congé de raccordement généreux**, ce qui fait
tomber Kt vers 1,5.
"""

FICHES["4.2"]["exercice_avant"] = """
### Exercice d'échauffement — Cisaillement, matage, couple

**1.** Un axe de **Ø12** relie une chape à une biellette. L'effort transmis est de **18 000 N**.
L'axe travaille en **double cisaillement**. Calcule la contrainte τ.

**2.** Même axe, mais monté en **simple cisaillement** : que devient τ ?

**3.** Rpg = 90 MPa. Lequel des deux montages est acceptable ?

**4.** L'axe Ø12 traverse une joue de **8 mm** d'épaisseur sous 18 000 N. Calcule la pression de
matage. La pression admissible est de 120 MPa : est-ce acceptable ?

**5.** Un moteur de **5,5 kW** tourne à **1 450 tr/min**. Calcule le couple qu'il délivre.
"""

FICHES["4.2"]["corrige_avant"] = """
### Corrigé de l'exercice d'échauffement

**1. Double cisaillement**

Section d'une coupe : S = π × 12² / 4 = **113 mm²**
En double cisaillement, **deux sections** résistent : S totale = 2 × 113 = **226 mm²**
τ = T / S = 18 000 / 226 = **79,6 MPa**

**2. Simple cisaillement**

Une seule section travaille : τ = 18 000 / 113 = **159 MPa**

*C'est exactement le double. Se tromper sur ce point, c'est se tromper d'un facteur 2 — la
différence entre une pièce qui tient et une pièce qui casse.*

**3. Comparaison à Rpg = 90 MPa**

- Double cisaillement : 79,6 < 90 → **acceptable**, avec une petite marge.
- Simple cisaillement : 159 > 90 → **refusé**, largement.

*D'où l'intérêt du montage en chape, qu'on retrouve partout sur les tiges de vérin, les
biellettes et les articulations.*

**4. Pression de matage**

p = F / (d × e) = 18 000 / (12 × 8) = **187,5 MPa**

187,5 > 120 : **ce n'est pas acceptable.** L'axe ne cassera pas, mais le trou va s'ovaliser, du
jeu va apparaître, et l'articulation deviendra bruyante puis imprécise.

Solutions : **épaissir la joue** (à 14 mm : p = 107 MPa, ça passe), augmenter le diamètre de
l'axe, ou monter une **bague de bronze** dans le trou.

*C'est un mode de défaillance qu'on oublie très souvent : on vérifie le cisaillement et on
néglige le matage.*

**5. Couple du moteur**

ω = 2 π N / 60 = 2 × π × 1 450 / 60 = **151,8 rad/s**
C = P / ω = 5 500 / 151,8 = **36,2 N·m**

*Ordre de grandeur à retenir : environ 6,6 N·m par kW à 1 450 tr/min. Si vous trouvez 5 500 ou
0,006, vous avez confondu tr/min et rad/s.*
"""

FICHES["4.3"]["exercice_avant"] = """
### Exercice d'échauffement — Flexion : la forme avant la matière

**1.** Une poutre rectangulaire **b = 30, h = 60** en S235. Calcule I, puis le module de flexion I/v.

**2.** Elle est encastrée dans un mur et porte **1 500 N** à **600 mm**. Calcule Mf maxi, puis σ maxi.

**3.** Avec s = 3, la pièce tient-elle ?

**4.** On pose la même poutre **à plat** (b = 60, h = 30). Recalcule I et σ. Que constates-tu ?

**5.** La même charge de 1 500 N est maintenant appliquée au milieu d'une poutre **sur deux
appuis** de 600 mm. Que devient Mf maxi ?
"""

FICHES["4.3"]["corrige_avant"] = """
### Corrigé de l'exercice d'échauffement

**1. Moment quadratique, poutre sur chant**

I = b h³ / 12 = 30 × 60³ / 12 = 30 × 216 000 / 12 = **540 000 mm⁴**
v = h / 2 = **30 mm**
I / v = 540 000 / 30 = **18 000 mm³**

**2. Moment fléchissant et contrainte**

Poutre encastrée, charge en bout : Mf = F × L = 1 500 × 600 = **900 000 N·mm**
σ = Mf / (I/v) = 900 000 / 18 000 = **50 MPa**

**3. Vérification**

Rpe = 235 / 3 = **78,3 MPa**. Comme 50 < 78,3, **la condition est vérifiée** : la poutre travaille
à 64 % de l'admissible.

**4. La même poutre posée à plat**

I = 60 × 30³ / 12 = 60 × 27 000 / 12 = **135 000 mm⁴**
v = 15 mm → I / v = **9 000 mm³**
σ = 900 000 / 9 000 = **100 MPa**

100 > 78,3 : **la pièce ne tient plus.**

**Constat : exactement la même barre, exactement la même matière — mais la contrainte a doublé
simplement parce qu'on l'a tournée de 90°.** C'est la conséquence directe du h³ : diviser la
hauteur par deux divise I par 8, et le module de flexion par 4.

*C'est pour cette raison qu'une planche posée sur chant est rigide et que la même planche à plat
plie mollement. Et c'est pourquoi on ne pose jamais un profil rectangulaire au hasard.*

**5. Poutre sur deux appuis**

Mf = F L / 4 = 1 500 × 600 / 4 = **225 000 N·mm**

C'est **quatre fois moins** que dans le cas encastré. Avec la poutre sur chant, σ tombe à
225 000 / 18 000 = 12,5 MPa.

*Ajouter un second appui est souvent la solution la moins chère à un problème de résistance :
elle ne coûte qu'un support, pas de la matière.*
"""


# ===========================================================================
# EXERCICES D'ÉCHAUFFEMENT — BLOC 5 (CAO)
# ===========================================================================

FICHES["5.1"]["exercice_avant"] = """
### Exercice d'échauffement — Diagnostiquer une esquisse

*Ces questions se répondent sans logiciel, mais elles décrivent exactement ce qui se passe devant
l'écran.*

**1.** Ton esquisse est encore **bleue** alors que la forme paraît correcte. Que se passera-t-il
dans trois mois, quand quelqu'un modifiera une cote en amont ?

**2.** Tu dois dessiner une plaque avec un trou **au centre**. Deux méthodes : coter le trou
depuis deux bords, ou poser une contrainte de symétrie. Laquelle choisis-tu et pourquoi ?

**3.** Une esquisse a été tracée **sur une face** de la pièce, créée par une extrusion. Cette
extrusion est ensuite supprimée. Que devient l'esquisse ?

**4.** Le logiciel refuse une cote en indiquant « sur-contrainte ». Qu'est-ce que ça signifie, et
que fais-tu ?

**5.** Dans quel ordre poses-tu les contraintes : cotes d'abord ou contraintes géométriques
d'abord ? Justifie en une phrase.
"""

FICHES["5.1"]["corrige_avant"] = """
### Corrigé de l'exercice d'échauffement

**1. L'esquisse peut dériver silencieusement**

Une entité sous-contrainte garde des degrés de liberté : lors d'une modification en amont, elle
peut **se déplacer toute seule**. La géométrie change sans que personne ne le remarque, et le
plan coté qui en découle devient faux.

*C'est le pire type d'erreur : elle ne provoque aucun message, elle produit une pièce fausse.*

**2. La contrainte de symétrie**

Avec deux cotes depuis les bords, si on change la largeur de la plaque, **le trou n'est plus au
centre** : il faut corriger à la main, et on oubliera.

Avec une symétrie par rapport aux axes, le trou **reste au centre automatiquement**. Le modèle
se comporte comme la pièce réelle devrait se comporter : c'est ce qu'on appelle l'**intention de
conception**.

**3. L'esquisse tombe en erreur**

Elle perd son plan support, et toutes les fonctions qui en dépendent s'effondrent en cascade.

*D'où la règle : on part d'un **plan de référence** (Face, Dessus, Droite) chaque fois que c'est
possible. Un plan de référence, lui, ne disparaît jamais.*

**4. La cote est redondante**

« Sur-contrainte » signifie que l'information est **déjà donnée** par une autre contrainte ou une
autre cote. Exemple : deux lignes sont déjà contraintes égales, et on cote les deux longueurs.

On supprime alors soit la cote en trop, soit la contrainte géométrique — mais on garde de
préférence la contrainte géométrique, qui porte mieux l'intention.

**5. Les contraintes géométriques d'abord**

Elles ne coûtent rien, elles sont robustes, et elles décrivent l'intention (symétrie, tangence,
alignement). Les cotes ne viennent qu'ensuite, **pour ce que la géométrie ne dit pas déjà**.

*Un débutant cote tout et n'utilise aucune contrainte : il se retrouve avec quinze cotes là où
une symétrie et deux cotes suffisaient.*
"""

FICHES["5.2"]["exercice_avant"] = """
### Exercice d'échauffement — Construire proprement

**1.** Une bague cylindrique avec un épaulement et une gorge. Quelle **fonction de base** utilises-tu
pour la créer, et pourquoi celle-là ?

**2.** Une pièce comporte **12 trous identiques** répartis sur un cercle. Combien de fonctions
crées-tu ? Que se passe-t-il si tu les fais un par un ?

**3.** Tu places les congés R2 juste après l'extrusion du corps, puis tu perces. Quel problème
risques-tu ?

**4.** Pourquoi utiliser l'**assistant de perçage** plutôt qu'un cercle extrudé pour un taraudage M8 ?

**5.** Ton modèle est terminé. Quel test fais-tu, en une minute, pour savoir s'il est robuste ?
"""

FICHES["5.2"]["corrige_avant"] = """
### Corrigé de l'exercice d'échauffement

**1. La révolution**

La bague est une pièce **de révolution** : une seule esquisse de son profil, tournée autour de
l'axe, crée d'un coup le cylindre, l'épaulement et la gorge.

*Principe général : on modélise **comme la pièce est fabriquée**. Une pièce tournée se fait par
révolution, pas par cinq extrusions successives. Le modèle est plus simple, plus lisible et plus
facile à modifier.*

**2. Deux fonctions : un perçage + une répétition circulaire**

Si tu les crées un par un, tu auras **12 fonctions** dans l'arbre. Le jour où le diamètre change,
il faudra faire **12 modifications** — et il suffit d'en oublier une.

Avec une répétition, tu modifies **une seule fonction**, et les 12 trous suivent. Tu peux même
changer leur nombre en tapant un chiffre.

**3. Les congés font disparaître les arêtes**

Les fonctions suivantes s'appuient souvent sur des arêtes ou des faces. Un congé placé trop tôt
les remplace par des surfaces courbes : les esquisses suivantes perdent leurs références, et le
modèle tombe en erreur à la première modification.

*Règle : congés, chanfreins et dépouilles **en fin d'arbre**, toujours.*

**4. L'assistant connaît les normes**

Il crée un vrai taraudage M8 : diamètre de perçage correct, profondeur de filetage, lamage,
fond de foret à 118°. Et surtout, **cette information se retrouve automatiquement dans la mise en
plan et la nomenclature**.

Un cercle extrudé n'est qu'un trou anonyme : il faudra tout réécrire à la main sur le plan, et
personne ne saura qu'il devait être taraudé.

**5. Le test de robustesse**

> Je change **deux cotes majeures** — la longueur, la hauteur, un diamètre — et je regarde l'arbre.

Aucune erreur ? Le modèle est bon. Des points d'exclamation ? Je corrige **maintenant**, pendant
que je sais encore comment le modèle est construit. Puis je remets les valeurs d'origine.

*Une minute de test évite des heures de reprise.*
"""

FICHES["5.3"]["exercice_avant"] = """
### Exercice d'échauffement — Assemblage et échange de fichiers

**1.** Tu assembles un arbre dans deux paliers. Une fois contraint, tu peux encore le faire
**coulisser** à la souris. Est-ce normal ? Comment le sais-tu ?

**2.** Le premier composant que tu insères dans un assemblage doit-il être fixe ou mobile ?
Pourquoi ?

**3.** Un fournisseur t'envoie un fichier **.stl** et tu dois modifier un perçage. Que fais-tu ?

**4.** Tu dois faire découper une pièce en tôle pliée chez un sous-traitant laser. Quels fichiers
lui envoies-tu, et pourquoi deux ?

**5.** Vrai ou faux : « puisque le modèle 3D contient tout, le plan coté n'est plus nécessaire ».
"""

FICHES["5.3"]["corrige_avant"] = """
### Corrigé de l'exercice d'échauffement

**1. Non, ce n'est pas normal**

Un arbre monté sur deux paliers réalise une liaison **pivot** : il ne doit rester qu'**une
rotation**. S'il coulisse encore, c'est que l'arrêt axial manque — dans le modèle, et peut-être
aussi dans la conception réelle.

*Le contrôle qui ne trompe pas : **les degrés de liberté restants doivent être exactement ceux du
schéma cinématique**. C'est l'un des grands intérêts de la maquette numérique.*

**2. Fixe (ancré)**

Le premier composant sert de **bâti** : tous les autres se positionnent par rapport à lui. S'il
est laissé libre, tout l'assemblage flotte dans l'espace et les contraintes se comportent de
façon imprévisible.

**3. Redemander un fichier STEP**

Un **.stl** n'est qu'un **maillage de triangles** : plus d'historique, plus de fonctions, plus de
surfaces exactes. La géométrie n'est même qu'approchée. Modifier proprement un perçage dessus est
pratiquement impossible.

Le format d'échange correct entre bureaux d'études est le **.step**, qui conserve la géométrie
exacte.

**4. Le DXF du développé, plus le PDF du plan**

- le **DXF à plat** alimente directement la machine de découpe ;
- le **PDF du plan** de la pièce **pliée** donne ce que le DXF ne contient pas : les rayons de
  pliage, le sens des plis, la matière, l'épaisseur, les tolérances.

*Envoyer seulement le DXF, c'est laisser le sous-traitant deviner comment plier.*

**5. FAUX**

Le modèle 3D ne contient ni les tolérances, ni les états de surface, ni les tolérances
géométriques, ni la matière, ni l'indice de révision. Et surtout : **c'est le plan coté qui fait
foi contractuellement**. En cas de litige avec un fournisseur, c'est lui qu'on ressort.

*Formule à retenir : la 3D montre, le plan coté engage.*
"""


# ===========================================================================
# EXERCICES D'ÉCHAUFFEMENT — BLOC 6 (CONCEPTION)
# ===========================================================================

FICHES["6.1"]["exercice_avant"] = """
### Exercice d'échauffement — Nommer les liaisons

**1.** Pour chaque cas, donne le nom de la liaison et le nombre de degrés de liberté restants :
   - a) une porte sur ses gonds ;
   - b) un tiroir dans son meuble ;
   - c) une tige de vérin libre de tourner dans son guide ;
   - d) deux tôles assemblées par quatre vis.

**2.** Une vis et son écrou : combien de degrés de liberté ? Attention, la réponse surprend.

**3.** Un ensemble comprend : un carter, un mors fixe vissé dessus, trois vis et deux goupilles.
Combien de classes d'équivalence ?

**4.** Un arbre est monté sur deux roulements, **tous deux bloqués axialement**. Que va-t-il se
passer en fonctionnement ? Comment corriges-tu ?

**5.** Combien de points d'appui faut-il pour positionner complètement une pièce, et comment se
répartissent-ils ?
"""

FICHES["6.1"]["corrige_avant"] = """
### Corrigé de l'exercice d'échauffement

**1. Les quatre liaisons**

| Cas | Liaison | ddl |
|---|---|---|
| a) porte sur ses gonds | **pivot** | 1 (une rotation) |
| b) tiroir | **glissière** | 1 (une translation) |
| c) tige de vérin libre en rotation | **pivot glissant** | 2 (rotation + translation, même axe) |
| d) deux tôles vissées | **encastrement** | 0 |

**2. La liaison hélicoïdale n'a qu'UN seul degré de liberté**

C'est le piège. On voit une rotation **et** une translation, donc on répond 2. Mais les deux ne
sont **pas indépendantes** : le pas de la vis les lie. Tourner d'un tour, c'est avancer d'un pas,
obligatoirement.

Un seul mouvement peut être commandé librement → **1 ddl**.

**3. Une seule classe d'équivalence**

Le carter, le mors fixe, les trois vis et les deux goupilles n'ont **aucun mouvement relatif** :
ils forment un seul groupe.

*La visserie ne réalise jamais une liaison sur un schéma cinématique : elle crée un encastrement,
donc elle disparaît dans une classe d'équivalence.*

**4. Le montage va gripper**

L'arbre chauffe en fonctionnement et cherche à s'allonger. Comme il ne le peut pas, il
**précontraint les roulements** : le frottement augmente, donc la température, donc la dilatation.
C'est un emballement qui finit par le grippage.

**Correction : libérer axialement un des deux paliers** — bague extérieure libre de coulisser dans
son alésage. Règle absolue : **un seul palier fixe par arbre**.

**5. Six points, répartis 3 - 2 - 1**

- **3 points** sur la face principale : suppriment une translation et deux rotations ;
- **2 points** sur une face latérale : une translation et une rotation ;
- **1 point** sur la dernière face : la dernière translation.

*C'est la règle 3-2-1. Elle explique pourquoi une pièce posée sur quatre points bascule toujours :
le quatrième point est en trop, et c'est le défaut de planéité qui décide sur lequel elle repose.*
"""

FICHES["6.2"]["exercice_avant"] = """
### Exercice d'échauffement — Monter un roulement correctement

**1.** Un arbre de pompe tourne, la charge (le poids de la poulie et la tension de courroie) reste
fixe. Quelle bague est montée serrée ? Quel ajustement pour l'arbre et pour l'alésage ?

**2.** Sur une roue de brouette, c'est la **roue** qui tourne autour d'un axe fixe. Quelle bague
est serrée cette fois ?

**3.** Un mécanicien monte un roulement en frappant au maillet sur la **bague extérieure** pour
l'emmancher sur l'arbre. Pourquoi est-ce une faute grave ?

**4.** L'épaulement de l'arbre a été usiné avec un congé R2, et le rayon de la bague vaut R1.
Quel problème ?

**5.** Quelle quantité de graisse mettre, et pourquoi pas plus ?
"""

FICHES["6.2"]["corrige_avant"] = """
### Corrigé de l'exercice d'échauffement

**1. Arbre tournant, charge fixe**

La **bague intérieure** tourne par rapport à la direction de la charge : elle est montée
**SERRÉE**.

- arbre : **k6** (ou m6 si la charge est forte)
- alésage du carter : **H7**, bague extérieure glissante

*C'est le cas le plus fréquent en mécanique : réducteurs, pompes, ventilateurs.*

**2. Roue tournante, axe fixe : c'est l'inverse**

La **bague extérieure**, solidaire de la roue, tourne par rapport à la charge : c'est elle qui est
**SERRÉE** dans le moyeu de la roue (**M7** ou N7). La bague intérieure est **glissante** sur
l'axe fixe (**h6** ou g6).

*La question à se poser est toujours la même : quelle bague tourne par rapport à la direction de
la charge ?*

**3. L'effort traverse les billes**

En frappant sur la bague extérieure pour emmancher la bague intérieure, tout l'effort de montage
passe **par les billes et les pistes**. Elles reçoivent des impacts ponctuels qui marquent les
chemins de roulement : c'est le **brinelling**.

Le roulement tournera d'abord normalement, puis deviendra bruyant, puis se détruira. Le défaut
est invisible au montage — d'où sa gravité.

**Règle : l'outil de montage doit porter sur la bague qu'on emmanche, jamais sur l'autre.**

**4. La bague porte sur le congé, pas sur l'épaulement**

Si le rayon de l'épaulement (R2) est **plus grand** que celui de la bague (R1), la bague vient
buter sur l'arrondi : elle n'est plus perpendiculaire à l'axe, elle se coince en biais et le
positionnement axial est faux.

**Règle : rayon du congé d'arbre < rayon de la bague.** C'est une cote à vérifier sur le
catalogue du fabricant, pas à improviser.

**5. Environ un tiers du volume libre**

Trop de graisse est brassée en permanence par les éléments roulants : elle s'échauffe, se dégrade
et fait chauffer le roulement — exactement comme un manque de graisse.

*« Bien graisser » ne veut pas dire « remplir ».*
"""

FICHES["6.3"]["exercice_avant"] = """
### Exercice d'échauffement — Guider, assembler, transmettre

**1.** Un chariot doit coulisser sur une course de **300 mm**. Quelle longueur de guidage
prévois-tu au minimum, et que se passe-t-il si elle est trop courte ?

**2.** Un assemblage boulonné se desserre malgré des **rondelles plates**. Deux causes possibles,
et la correction.

**3.** Une vis de classe **10.9** : quelles sont ses valeurs de Rm et de Re ?

**4.** Un technicien remplace une clavette cassée par une **plus courte** trouvée en stock.
Qu'est-ce qui va se passer ?

**5.** Un pignon de **20 dents** entraîne une roue de **60 dents**, module **3**. Calcule le
rapport, les deux diamètres primitifs et l'entraxe.
"""

FICHES["6.3"]["corrige_avant"] = """
### Corrigé de l'exercice d'échauffement

**1. Environ 450 à 600 mm de guidage**

La règle : **longueur de guidage ≈ 1,5 à 2 fois la course**. Pour 300 mm de course, il faut
compter 450 à 600 mm.

Si le guidage est trop court, le chariot **s'arc-boute** : il se coince dès qu'on pousse d'un
seul côté, exactement comme un tiroir tiré par un coin. Aucun soin d'usinage ne rattrape une
géométrie de guidage insuffisante.

**2. Précharge insuffisante, ou tassement**

- **Cause 1 : le serrage est insuffisant.** Un assemblage vissé tient par la **précharge** : la
  vis étirée plaque les pièces l'une contre l'autre. Une rondelle plate ne freine rien, elle
  répartit seulement la pression. Correction : serrer à la **clé dynamométrique**, au couple
  correspondant à la classe de la vis.
- **Cause 2 : un élément souple se tasse** — peinture épaisse, joint, revêtement. La précharge
  chute toute seule après quelques heures. Correction : supprimer l'élément souple sous la tête,
  ou reprendre le serrage après rodage.

Si les vibrations persistent, ajouter un **vrai freinage** : écrou Nylstop, frein filet, rondelle
à dents ou goupille.

**3. Classe 10.9**

- Rm = 10 × 100 = **1 000 MPa**
- Re = 10 × 9 × 10 = **900 MPa**

*Même méthode pour la 8.8 : Rm = 800 MPa, Re = 640 MPa.*

**4. La rainure va être matée, puis la clavette cassera**

Une clavette travaille **par matage sur ses flancs**. La pression est inversement proportionnelle
à la surface de contact, donc à la longueur.

Une clavette plus courte fait grimper la pression : elle mate la rainure de l'arbre et celle du
moyeu, du jeu apparaît, le moyeu commence à cogner à chaque inversion de couple, et l'ensemble
casse.

**Il faut respecter la longueur d'origine**, ou refaire le calcul de pression de matage.

**5. Engrenage 20/60, module 3**

- Rapport : r = Z menante / Z menée = 20 / 60 = **1/3** — la roue tourne trois fois moins vite,
  et le couple est multiplié par 3.
- d1 = m × Z1 = 3 × 20 = **60 mm**
- d2 = m × Z2 = 3 × 60 = **180 mm**
- Entraxe : a = (d1 + d2) / 2 = (60 + 180) / 2 = **120 mm**

*Et les deux roues tournent en sens inverse. Pour retrouver le même sens, il faudrait une roue
intermédiaire — qui ne changerait pas le rapport.*
"""


# ===========================================================================
# MISES EN SITUATION — placées AVANT les cas industriels d'origine
# Objectif : planter le décor et décoder le vocabulaire technique du cas,
# pour qu'un débutant puisse le lire sans buter sur les sigles.
# ===========================================================================

FICHES["1.1"]["exemple_avant"] = """
### Avant de lire le cas : de quoi parle-t-on ?

**La situation.** Une usine embouteille des jus de fruits. Sur la ligne, un petit capteur doit
« voir » passer chaque bouteille pour les compter et détecter les manquantes. Ce capteur doit
être tenu en place, toujours à la même distance des bouteilles. C'est ce support qu'il faut
concevoir.

**Le vocabulaire du cas, en clair :**

| Terme | Ce que ça veut dire |
|---|---|
| **répétabilité** | si on démonte puis on remonte, retrouve-t-on la même position ? |
| **IP69K** | un indice d'étanchéité : résiste au nettoyage au jet haute pression et chaud |
| **X2CrNiMo17-12-2** | un inox au molybdène, celui qui tient face aux produits chlorés |
| **profilé 40×40 rainure 8** | les barres d'aluminium standard des lignes de production |

**Ce qu'il faut observer en lisant.** Le client arrive avec **sa** solution (« une équerre inox
avec deux trous M6 »). Regardez comment le concepteur la met de côté pour écrire d'abord ce que
le support doit **faire** — et ce que ça change au résultat final.
"""

FICHES["1.2"]["exemple_avant"] = """
### Avant de lire le cas : de quoi parle-t-on ?

**La situation.** Un corps de palier, c'est le bloc de fonte dans lequel on loge un roulement
pour qu'un arbre puisse tourner. On en trouve sur toutes les machines : convoyeurs, pompes,
ventilateurs.

**Le vocabulaire du cas, en clair :**

| Terme | Ce que ça veut dire |
|---|---|
| **alésage Ø50 H7** | le trou qui reçoit le roulement, avec une tolérance serrée |
| **lamage Ø18 prof. 8** | un élargissement du trou en surface, pour noyer la tête de vis |
| **rainure de graissage** | une gorge par laquelle la graisse arrive au roulement |
| **EN-GJL-250** | fonte grise : elle amortit les vibrations et s'usine bien |

**Ce qu'il faut observer en lisant.** Le bureau d'études n'a dessiné que **deux vues** alors que
la pièce est complexe. Cherchez la justification de chaque choix : pourquoi la coupe, pourquoi
la vue de gauche est absente. C'est exactement le raisonnement qu'on vous demandera de tenir.
"""

FICHES["1.3"]["exemple_avant"] = """
### Avant de lire le cas : de quoi parle-t-on ?

**La situation.** Une même pièce peut coûter du simple au triple selon la façon dont elle est
cotée. Le cas qui suit compare deux versions d'un même plan : une version « par précaution », où
tout est serré, et une version réfléchie, où seules les cotes qui ont une fonction sont serrées.

**Le vocabulaire du cas, en clair :**

| Terme | Ce que ça veut dire |
|---|---|
| **cote fonctionnelle** | une cote dont dépend le bon fonctionnement du mécanisme |
| **ISO 2768-m** | les tolérances qui s'appliquent d'office aux cotes sans indication |
| **surface de référence** | la surface qui positionne la pièce, et depuis laquelle on cote |
| **Ra** | la rugosité : la hauteur moyenne des aspérités, en micromètres |

**Ce qu'il faut observer en lisant.** Repérez, pour chaque cote, la question posée : *« qu'est-ce
qui se passerait si cette cote était fausse de 0,3 mm ? »*. Si la réponse est « rien », la cote
n'a pas besoin d'être serrée.
"""

FICHES["2.1"]["exemple_avant"] = """
### Avant de lire le cas : de quoi parle-t-on ?

**La situation.** Un roulement doit être logé dans un carter. Le fabricant du roulement impose
une tolérance précise pour ce logement : H7. Le cas explique **pourquoi** cette exigence n'est
pas négociable, et ce qui se passe si on livre du H9 « parce que c'est moins cher ».

**Le vocabulaire du cas, en clair :**

| Terme | Ce que ça veut dire |
|---|---|
| **roulement 6208** | un roulement à billes normalisé : trou 40, extérieur 80, largeur 18 |
| **logement** | le trou du carter qui reçoit la bague extérieure du roulement |
| **catalogue constructeur** | SKF, NSK, FAG… ils imposent les ajustements à respecter |
| **fluage de bague** | la bague qui tourne lentement sur sa portée et la détruit |

**Ce qu'il faut observer en lisant.** Comparez les chiffres : H7 et H9 ont la même lettre, donc
la même position — seule la **largeur** de la zone change. Et regardez ce que cette largeur
implique concrètement pour la tenue du roulement.
"""

FICHES["2.2"]["exemple_avant"] = """
### Avant de lire le cas : de quoi parle-t-on ?

**La situation.** Une pompe centrifuge : un moteur fait tourner un arbre, qui porte une roue
(le rotor) brassant le liquide. L'arbre tourne dans deux roulements. Le cas déroule le montage
complet, ajustement par ajustement.

**Le vocabulaire du cas, en clair :**

| Terme | Ce que ça veut dire |
|---|---|
| **roulement 6205** | trou 25, extérieur 52, largeur 15 |
| **poussée hydraulique** | l'effort axial créé par le liquide sur la roue |
| **charge fixe en direction** | le poids et la poussée tirent toujours dans le même sens |
| **portée** | la partie de l'arbre ou du carter sur laquelle la bague est montée |

**Ce qu'il faut observer en lisant.** Une seule question gouverne tout le montage : *quelle bague
tourne par rapport à la direction de la charge ?* Vérifiez que chaque ajustement du cas découle
bien de cette réponse.
"""

FICHES["2.3"]["exemple_avant"] = """
### Avant de lire le cas : de quoi parle-t-on ?

**La situation.** Un vérin doit être fixé sur un bâti de machine. Entre les deux, une bride :
une plaque percée qui centre le nez du vérin et le boulonne au bâti. Si le centrage est de
travers, la tige de vérin travaille en biais et s'use en quelques mois.

**Le vocabulaire du cas, en clair :**

| Terme | Ce que ça veut dire |
|---|---|
| **nez du vérin** | la partie cylindrique à l'avant, qui vient se centrer dans la bride |
| **alésage Ø63 H8** | le trou de centrage, avec sa tolérance |
| **perpendicularité Ø0,05 A** | l'axe du trou doit rester dans un cylindre de 0,05 mm, droit par rapport à A |
| **localisation** | l'exigence qui garantit que les trous tombent en face des taraudages |

**Ce qu'il faut observer en lisant.** Pour chaque exigence géométrique, cherchez la panne qu'elle
évite. Une tolérance géométrique ne s'ajoute jamais « pour faire sérieux » : elle empêche une
défaillance précise.
"""

FICHES["3.1"]["exemple_avant"] = """
### Avant de lire le cas : de quoi parle-t-on ?

**La situation.** Un bras de robot manipulateur déplace des pièces. Plus il est léger, plus il
peut accélérer, donc plus la machine produit. Le bureau d'études compare deux matériaux pour ce
bras : acier ou aluminium.

**Le vocabulaire du cas, en clair :**

| Terme | Ce que ça veut dire |
|---|---|
| **masse mobile** | la masse que le moteur doit accélérer et freiner à chaque cycle |
| **section carrée creuse** | un tube carré : la matière est loin de l'axe neutre, donc efficace |
| **flèche en bout** | de combien le bras s'affaisse sous la charge |
| **cadence** | le nombre de pièces traitées par heure |

**Ce qu'il faut observer en lisant.** Deux critères s'opposent : la **résistance** (Re) et la
**rigidité** (E). L'aluminium gagne sur la masse mais perd sur la rigidité — et c'est souvent la
flèche, pas la rupture, qui décide. Regardez comment le cas tranche.
"""

FICHES["3.2"]["exemple_avant"] = """
### Avant de lire le cas : de quoi parle-t-on ?

**La situation.** On ouvre un réducteur — la boîte qui, entre un moteur et une machine, réduit
la vitesse et augmente le couple. On regarde la nomenclature, pièce par pièce, et on décode
pourquoi chaque matériau a été choisi.

**Le vocabulaire du cas, en clair :**

| Terme | Ce que ça veut dire |
|---|---|
| **nomenclature** | la liste numérotée des pièces d'un ensemble, avec leur matière |
| **repère (Rep)** | le numéro qui relie une ligne de la liste à une bulle sur le plan |
| **carter** | l'enveloppe qui contient les engrenages et retient l'huile |
| **cémenté trempé** | peau dure pour l'usure, cœur tenace pour les chocs |

**Ce qu'il faut observer en lisant.** Chaque ligne suit la même logique : quelle sollicitation
subit la pièce, quel procédé la fabrique, donc quelle nuance. C'est le raisonnement complet du
bloc 3, appliqué à un objet réel.
"""

FICHES["3.3"]["exemple_avant"] = """
### Avant de lire le cas : de quoi parle-t-on ?

**La situation.** On suit un pignon de boîte de vitesses depuis la barre d'acier brute jusqu'à
la pièce finie. Ce parcours s'appelle une **gamme de fabrication** : la liste ordonnée des
opérations, chacune à sa place pour une raison précise.

**Le vocabulaire du cas, en clair :**

| Terme | Ce que ça veut dire |
|---|---|
| **gamme** | la suite ordonnée des opérations de fabrication |
| **ébauche** | le premier usinage, rapide, qui laisse de la matière en trop |
| **surépaisseur** | la matière laissée exprès, qui sera enlevée à la finition |
| **16MnCr5** | un acier à bas carbone, prévu pour être cémenté |
| **taillage** | l'usinage des dents de l'engrenage |

**Ce qu'il faut observer en lisant.** Un seul principe explique presque toute la gamme :
**le traitement thermique déforme**. Repérez où il se place, et ce qu'on fait juste après.
"""


# ===========================================================================
# MISES EN SITUATION — BLOCS 4, 5 et 6
# ===========================================================================

FICHES["4.1"]["exemple_avant"] = """
### Avant de lire le cas : de quoi parle-t-on ?

**La situation.** Une **chape**, c'est une fourche métallique percée d'un trou : on y passe un
axe pour accrocher une charge. On en trouve au bout des palans, des vérins, des élingues. Ici,
elle doit soulever 25 kN — environ 2,5 tonnes.

**Le vocabulaire du cas, en clair :**

| Terme | Ce que ça veut dire |
|---|---|
| **25 kN** | 25 000 newtons, soit à peu près 2 500 kg suspendus |
| **section nette** | la section qui reste vraiment, une fois le trou enlevé |
| **coefficient réglementaire** | en levage, ce n'est pas le concepteur qui le choisit : la norme l'impose |
| **matage** | l'ovalisation du trou sous la pression de l'axe |

**Ce qu'il faut observer en lisant.** Le trou enlève de la matière **là où l'effort passe**. On
ne calcule donc pas sur la section pleine, mais sur ce qui reste. Et le coefficient de sécurité
est bien plus élevé que d'habitude : au-dessus d'une charge suspendue, on ne discute pas.
"""

FICHES["4.2"]["exemple_avant"] = """
### Avant de lire le cas : de quoi parle-t-on ?

**La situation.** Un moteur électrique de 7,5 kW entraîne une pompe. Entre les deux, un arbre
transmet le mouvement. Quel diamètre lui donner ? Trop fin, il casse ou se tord ; trop gros, on
paie de la matière et des roulements pour rien.

**Le vocabulaire du cas, en clair :**

| Terme | Ce que ça veut dire |
|---|---|
| **accouplement** | la pièce qui relie deux arbres bout à bout |
| **42CrMo4 trempé revenu** | un acier allié traité : Re ≈ 750 MPa, trois fois le S235 |
| **rainure de clavette** | la gorge usinée dans l'arbre pour loger la clavette |
| **moment de torsion Mt** | le couple que l'arbre doit transmettre, en N·m |

**Ce qu'il faut observer en lisant.** Deux choses tuent les arbres de transmission : la
**rainure de clavette**, qui enlève de la matière et concentre les contraintes, et le fait que
l'arbre subit **torsion et flexion en même temps**. Regardez comment le cas en tient compte.
"""

FICHES["4.3"]["exemple_avant"] = """
### Avant de lire le cas : de quoi parle-t-on ?

**La situation.** Sur une ligne de contrôle qualité, une caméra photographie chaque pièce qui
passe. Elle est tenue par un bras horizontal boulonné sur un montant. Si le bras s'affaisse
ne serait-ce que d'un demi-millimètre, l'image se décale et le contrôle devient faux.

**Le vocabulaire du cas, en clair :**

| Terme | Ce que ça veut dire |
|---|---|
| **porte-à-faux** | le bras n'est tenu que d'un seul côté, comme un plongeoir |
| **encastrement** | la liaison qui bloque tout : ici, le boulonnage sur le montant |
| **flèche** | de combien le bout du bras descend sous la charge |
| **3,5 kg en bout** | soit environ 35 N — c'est peu, et pourtant… |

**Ce qu'il faut observer en lisant.** Ici, ce n'est **pas la rupture** qui dimensionne : le bras
résisterait largement. C'est la **flèche** imposée par le cahier des charges. C'est très souvent
le cas en conception de précision, et c'est ce qui explique des sections apparemment
surdimensionnées.
"""

FICHES["5.1"]["exemple_avant"] = """
### Avant de lire le cas : de quoi parle-t-on ?

**La situation.** Une même équerre de fixation doit exister en six tailles. Deux façons de s'y
prendre : dessiner six fichiers séparés, ou construire **un seul modèle piloté par des
paramètres**. Le cas compare les deux, notamment le jour où le client demande une modification.

**Le vocabulaire du cas, en clair :**

| Terme | Ce que ça veut dire |
|---|---|
| **paramètre** | une valeur nommée (« longueur », « épaisseur ») qu'on peut piloter |
| **équation** | une cote calculée à partir d'une autre : largeur = longueur / 2 |
| **table de paramètres** | un tableau qui décline les tailles, comme un catalogue |
| **famille de pièces** | l'ensemble des variantes issues d'un même modèle |

**Ce qu'il faut observer en lisant.** Comptez le nombre de modifications à faire dans chaque
approche quand le client change d'avis. C'est là que tout se joue — pas dans le temps de
modélisation initial.
"""

FICHES["5.2"]["exemple_avant"] = """
### Avant de lire le cas : de quoi parle-t-on ?

**La situation.** Un carter de pompe en aluminium moulé : une pièce complexe, avec un corps
cylindrique, une bride, un canal courbe pour le liquide, des pattes et des nervures. C'est
typiquement la pièce qui décourage un débutant — parce qu'il ne sait pas par quel bout commencer.

**Le vocabulaire du cas, en clair :**

| Terme | Ce que ça veut dire |
|---|---|
| **volute** | le canal en spirale dans lequel le liquide est accéléré |
| **nervure** | une cloison mince ajoutée pour rigidifier sans alourdir |
| **patte de fixation** | l'oreille percée qui sert à boulonner le carter |
| **alésage Ø52 H7** | le logement du roulement, la seule cote vraiment précise |

**Ce qu'il faut observer en lisant.** L'ordre de l'arbre de création. La règle générale : le
**volume principal d'abord**, les détails ensuite, les **congés et dépouilles en dernier**.
Regardez aussi comment les fonctions sont nommées : un collègue doit pouvoir reprendre le modèle.
"""

FICHES["5.3"]["exemple_avant"] = """
### Avant de lire le cas : de quoi parle-t-on ?

**La situation.** Un support de capteur suit deux chemins en parallèle : un **prototype imprimé
en 3D** pour vérifier tout de suite qu'il se monte bien sur la machine, et une **série usinée**
pour la production définitive. Le cas suit la chaîne complète, de la maquette au fichier envoyé
au sous-traitant.

**Le vocabulaire du cas, en clair :**

| Terme | Ce que ça veut dire |
|---|---|
| **BE** | bureau d'études — l'équipe qui conçoit |
| **implantation** | la vérification que la pièce se place bien dans son environnement |
| **prototype** | une pièce d'essai, pas destinée à la production |
| **STEP / STL / DXF** | les trois formats d'échange, chacun pour un usage précis |

**Ce qu'il faut observer en lisant.** À chaque étape, demandez-vous **quel fichier part, et à
qui**. C'est exactement ce qu'on attendra de votre fils en stage : envoyer le bon format à la
bonne personne, accompagné du plan coté.
"""

FICHES["6.1"]["exemple_avant"] = """
### Avant de lire le cas : de quoi parle-t-on ?

**La situation.** Un dispositif de **bridage** sert à maintenir une pièce pendant qu'une machine
travaille dessus. Ici, un vérin pneumatique pousse une tige, qui fait pivoter une biellette, qui
fait basculer un levier venant serrer la pièce. Cinq éléments, quatre liaisons.

**Le vocabulaire du cas, en clair :**

| Terme | Ce que ça veut dire |
|---|---|
| **bâti** | la partie fixe de la machine, la référence de tout le mécanisme |
| **biellette** | une barre articulée aux deux bouts, qui transmet un mouvement |
| **tige + piston** | l'ensemble mobile du vérin, qui sort et rentre |
| **classe d'équivalence** | un groupe de pièces qui ne bougent pas les unes par rapport aux autres |

**Ce qu'il faut observer en lisant.** Suivez la méthode dans l'ordre : d'abord les **groupes** de
pièces solidaires, ensuite les liaisons entre ces groupes, et seulement à la fin le schéma. Et
remarquez que la visserie n'apparaît nulle part.
"""

FICHES["6.2"]["exemple_avant"] = """
### Avant de lire le cas : de quoi parle-t-on ?

**La situation.** Dans un réducteur à deux étages, l'arbre du milieu — dit **arbre
intermédiaire** — porte deux pignons : l'un reçoit le mouvement du premier étage, l'autre le
transmet au second. Il est donc chargé des deux côtés, et doit être monté avec soin.

**Le vocabulaire du cas, en clair :**

| Terme | Ce que ça veut dire |
|---|---|
| **effort d'engrènement** | la force que les dents exercent l'une sur l'autre |
| **charge radiale** | l'effort perpendiculaire à l'arbre, qui le fait fléchir |
| **charge axiale** | l'effort le long de l'arbre, qui cherche à le pousser de côté |
| **palier** | l'ensemble roulement + logement qui soutient l'arbre |

**Ce qu'il faut observer en lisant.** Trois décisions structurent tout le montage : quelle bague
est serrée, quel palier est fixe, et comment l'étanchéité est assurée en sortie. Chacune découle
d'une règle vue dans le cours, pas d'une habitude.
"""

FICHES["6.3"]["exemple_avant"] = """
### Avant de lire le cas : de quoi parle-t-on ?

**La situation.** Un moteur de 4 kW tourne à 1 450 tr/min, et le tapis a besoin d'environ
290 tr/min. Il faut donc **diviser la vitesse par cinq** — et au passage, le couple sera
multiplié par cinq. Le cas conçoit cet étage de réduction de bout en bout.

**Le vocabulaire du cas, en clair :**

| Terme | Ce que ça veut dire |
|---|---|
| **rapport de réduction** | le rapport entre vitesse de sortie et vitesse d'entrée |
| **module** | la taille d'une dent — deux roues qui engrènent ont le même |
| **entraxe** | la distance entre les deux axes des roues |
| **motoréducteur** | l'ensemble moteur + réducteur monté en un seul bloc |

**Ce qu'il faut observer en lisant.** Le déroulé est celui d'un vrai calcul de conception :
rapport, puis nombres de dents, puis module, puis entraxe, puis couple de sortie, puis diamètre
d'arbre. Chaque étape s'appuie sur la précédente — c'est la méthode à reproduire en projet.
"""


def appliquer(blocs):
    """Remplace ou complète le contenu des fiches réécrites.

    Deux mécanismes :
      - une clé normale ("cours", "exemple"...) REMPLACE le contenu d'origine ;
      - une clé suffixée "_avant" ("exercice_avant") est AJOUTÉE EN TÊTE du contenu
        d'origine, qui est conservé. C'est ce qui permet de proposer un exercice
        d'échauffement avant l'exercice de niveau examen déjà présent.
    """
    remplacees = 0
    for bloc in blocs:
        for fiche in bloc.get("fiches", []):
            nouveau_contenu = FICHES.get(fiche.get("id"))
            if not nouveau_contenu:
                continue
            for cle, valeur in nouveau_contenu.items():
                if cle.endswith("_avant"):
                    base = cle[:-len("_avant")]
                    fiche[base] = valeur + "\n\n---\n" + fiche.get(base, "")
                else:
                    fiche[cle] = valeur
            remplacees += 1
    return remplacees
