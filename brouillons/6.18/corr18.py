import os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'brouillon_6_18.py')
s = open(p, encoding='utf-8').read()


def R(a, b):
    global s
    assert s.count(a) == 1, (a[:90], s.count(a))
    s = s.replace(a, b)


# ---------------- figures
R('''            "En changeant la vitesse : courroie, chaîne, engrenages (fiches 6.11, 6.13, 12.5).",''',
  '''            "En changeant la vitesse : courroie, chaîne, engrenages (fiches 6.11, 6.13, 12.5).",''')
# embrayage : commande dessinée ; limiteur : garnitures, ressort, écrou ; frein : ressort dessiné
R('''    p.append(_txt(142, 120, "ressort", 9, FIN, "middle"))''',
  '''    p.append(_txt(142, 120, "ressort", 9, FIN, "middle"))
    p.append(_k_fl(122, 88, 150, 88, ALESAGE, "kb", 2))
    p.append(_txt(108, 84, "commande : écarte = débrayé", 9, ALESAGE, "start"))''')
R('''    p.append(_txt(387, 206, "couple de réglage", 11, ALERTE, "middle", True))''',
  '''    p.append(f"<circle cx='387' cy='138' r='30' fill='none' stroke='{ARBRE}' stroke-width='5' opacity='0.7'/>")
    p.append(_txt(340, 96, "garnitures", 9, ARBRE, "end"))
    p.append(_txt(440, 96, "ressort + écrou", 9, TRAIT, "start"))
    p.append(_txt(440, 108, "de réglage", 9, TRAIT, "start"))
    p.append(_txt(387, 192, "blocage → il glisse", 10, ALERTE, "middle", True))
    p.append(_txt(387, 206, "couple de réglage", 11, ALERTE, "middle", True))''')
R('''    p.append(f"<rect x='648' y='104' width='60' height='68' fill='#ffffff' stroke='{OK}' stroke-width='2'/>")''',
  '''    p.append(f"<path d='M 626 138 l 4 -8 l 4 16 l 4 -16 l 4 16 l 4 -8' fill='none' stroke='{TRAIT}' stroke-width='1.6'/>")
    p.append(_txt(634, 186, "ressort", 9, FIN, "middle"))
    p.append(f"<rect x='648' y='104' width='60' height='68' fill='#ffffff' stroke='{OK}' stroke-width='2'/>")''')
# vis : pente des filets double pour 2 filets
R('''            p.append(f"<line x1='{xx}' y1='154' x2='{xx + 12}' y2='120' stroke='{c}' stroke-width='2'/>")''',
  '''            p.append(f"<line x1='{xx}' y1='154' x2='{xx + 12 * nf}' y2='120' stroke='{c}' stroke-width='2'/>")''')
R('''    p.append(_txt(46, 324, "Plus l'hélice est inclinée (ph grand), plus la vis est rapide… et plus elle risque d'être réversible.", 12, FIN))''',
  '''    p.append(_txt(46, 324, "Plus l'hélice s'incline (ph grand), plus la vis est rapide… et plus elle risque d'être réversible.", 12, FIN))''')
# came : loi de levée en phase avec le dessin (le poussoir descend d'abord)
R('''    pts = " ".join(f"{gx + gw * i / 120:.1f},{gy - 45 - 40 * math.cos(2 * math.pi * i / 120):.1f}" for i in range(121))''',
  '''    pts = " ".join(f"{gx + gw * i / 120:.1f},{gy - 45 + 40 * math.sin(2 * math.pi * i / 120):.1f}" for i in range(121))''')
R('''    p.append(_txt(422, 240, "Came excentrique : levée quasi sinusoïdale. Une came de", 10, FIN))''',
  '''    p.append(_txt(422, 240, "Came excentrique : le poussoir monte et descend sans à-coup. Une came de", 10, FIN))''')
# figure à curseurs : pas limité, libellés
R('''    p = [_k_defs(), _txt(30, 24, f"Vis Ø 20, pas {_fr_court(P, 1)} mm, {nf} filet{'s' if nf > 1 else ''}, {int(N)} tr/min", 13, TRAIT, "start", True)]''',
  '''    p = [_k_defs(), _txt(30, 24, f"Exemple de calcul : vis de Ø 20, pas {_fr_court(P, 1)} mm, {nf} filet{'s' if nf > 1 else ''}, {int(N)} tr/min", 13, TRAIT, "start", True)]''')
R('''    p.append(_txt(30, 292, "Ajouter des filets accélère la vis, mais redresse l'hélice : au-delà de φ, elle devient réversible.", 11, FIN))''',
  '''    p.append(_txt(30, 292, "Ajouter des filets accélère la vis, mais incline davantage l'hélice : au-delà de φ, elle devient réversible.", 11, FIN))''')
R('''        [{"nom": "P", "label": "Pas apparent P (mm)", "min": 2.0, "max": 8.0, "defaut": 4.0, "pas": 1.0},''',
  '''        [{"nom": "P", "label": "Pas apparent P (mm)", "min": 2.0, "max": 5.0, "defaut": 4.0, "pas": 1.0},''')
R('''    p.append(_txt(46, 274, "k = N2 / N1 (rapport de transmission). Courroie lisse : silencieuse, amortit, peut patiner (protection naturelle).", 12, TRAIT))''',
  '''    p.append(_txt(46, 274, "r = N2 / N1 (rapport de transmission). Courroie lisse : silencieuse, amortit, peut patiner (protection non réglée).", 12, TRAIT))''')
R('''    p.append(_txt(142, 190, "k ≈ d1 / d2", 12, ARBRE, "middle", True))''', '''    p.append(_txt(142, 190, "r ≈ d1 / d2", 12, ARBRE, "middle", True))''')
R('''    p.append(_txt(387, 190, "k = Z1 / Z2", 12, ALESAGE, "middle", True))''', '''    p.append(_txt(387, 190, "r = Z1 / Z2", 12, ALESAGE, "middle", True))''')
R('''    p.append(_txt(632, 190, "k = Z1 / Z2", 12, OK, "middle", True))''', '''    p.append(_txt(632, 190, "r = Z1 / Z2", 12, OK, "middle", True))''')
R('''    p.append(_txt(142, 206, "C = n f F Rm", 13, ALESAGE, "middle", True))''', '''    p.append(_txt(142, 206, "C = n f F rmoy", 13, ALESAGE, "middle", True))''')

# ---------------- cours §1
R('''Deux grandeurs suivent toute la chaîne : la **puissance**, qui se perd un peu à chaque étage
(P sortie = η × P entrée, fiche 8.5), et la **réversibilité** : la sortie peut-elle entraîner l'entrée ?''',
  '''Deux grandeurs suivent toute la chaîne : la **puissance**, qui se perd un peu à chaque étage
(P sortie = η × P entrée, fiche 8.5), et la **réversibilité** : la sortie peut-elle entraîner l'entrée ?

*Exemple que tout le monde a manipulé : le **cric à vis** d'une voiture. Vous tournez la manivelle, la
voiture monte ; vous lâchez la manivelle, la voiture **reste en l'air** : son poids ne fait pas tourner la
vis. Ce cric est **irréversible**. À l'inverse, sur une vis à billes, lâchez le moteur et la charge
redescend en faisant tourner la vis toute seule : elle est **réversible**. Pour un axe vertical, c'est la
différence entre « la charge tient » et « la charge tombe » (voir le cas industriel).*''')

# §2 accouplements
R('''| **à soufflet, à lamelles** | petits défauts, sans jeu angulaire | positionnement précis (axe asservi, codeur) |
| **cardan** (joint de transmission) | grands angles | arbres volontairement non alignés |''',
  '''| **à soufflet, à lamelles** | petits défauts, **aucun jeu en rotation** : le moteur tourne de 1°, la vis tourne de 1° | positionnement précis, quand un capteur compte les tours pour connaître la position |
| **cardan** (joint de transmission) | grands angles, comme la rallonge à rotule d'une clé à cliquet | arbres volontairement non alignés (seul, il ne transmet pas une vitesse parfaitement constante : on les monte par paires) |''')
R('''**Le lien avec la fiche 6.17.** Un accouplement rigide entre deux arbres montés chacun sur deux paliers
rend l'ensemble **hyperstatique** : la coaxialité des deux arbres devient une condition à tenir. Si elle
ne l'est pas, le défaut se transforme en efforts sur les roulements. L'accouplement élastique supprime
ces conditions : c'est un choix d'isostatisme, pour quelques euros.''',
  '''**Le lien avec la fiche 6.17.** Image : une porte montée sur quatre gonds pas parfaitement alignés ; elle
force, grince et use ses gonds. Deux arbres reliés rigidement, chacun tenu par deux roulements, c'est
pareil : les deux axes doivent être exactement dans le prolongement l'un de l'autre (la **coaxialité**),
sinon ce sont les roulements qui encaissent l'écart — le montage est **hyperstatique**. L'accouplement
élastique est une articulation souple entre les deux : chaque arbre garde son alignement, l'élastomère
absorbe la différence. On ne demande plus au monteur un alignement parfait.''')

# §3 embrayage
R('''**L'embrayage : relier ou séparer en marche.** Le moteur tourne, la machine s'arrête ou repart à la
demande. Un **embrayage à friction** presse des disques les uns contre les autres : il démarre en douceur
en glissant au début. Un **embrayage à crabots** (dents frontales) ne glisse jamais, mais s'enclenche à
l'arrêt ou à vitesses égales. Un **coupleur hydraulique** transmet par un fluide : démarrage très
progressif des grosses inerties (convoyeurs, broyeurs).''',
  '''**L'embrayage : relier ou séparer en marche** (embrayer = relier ; débrayer = séparer). Pourquoi ne pas
simplement arrêter le moteur ? Parce que certains moteurs ne peuvent pas démarrer en charge, ou mettent du
temps à se lancer. L'exemple connu est la **voiture** : le moteur tourne au ralenti au feu rouge, la pédale
sépare moteur et roues ; au démarrage, on relâche doucement, les disques glissent puis « collent ». En
atelier, sur une **presse à volant**, le volant reste lancé en permanence et l'embrayage ne le relie au
coulisseau que le temps d'un coup de presse.

- **embrayage à friction** : des disques pressés les uns contre les autres ; il démarre en douceur en
  glissant au début ;
- **embrayage à crabots** : deux couronnes à dents frontales qui s'emboîtent, comme les doigts de deux mains
  croisées ; il ne glisse jamais, mais s'enclenche à l'arrêt ou à vitesses égales, sinon les dents se
  cognent ;
- **coupleur hydraulique** : deux roues à aubes face à face dans un carter plein d'huile ; la première
  brasse l'huile, qui entraîne la seconde. Démarrage très progressif des machines lourdes à lancer
  (convoyeur chargé, broyeur).''')
R('''> **C = n × f × F × Rm**

- **n** : le nombre de surfaces frottantes (un disque pris entre deux plateaux : n = 2) ;
- **f** : le coefficient de frottement des garnitures (donné par le fabricant ou l'énoncé) ;
- **F** : l'effort presseur (le ressort) ;
- **Rm** : le rayon moyen des garnitures, **(R + r) / 2** (garniture usée de façon uniforme).

*D'où vient la formule ? Chaque surface frotte avec une force tangentielle f × F (loi de Coulomb, fiche
12.1), appliquée en moyenne à la distance Rm de l'axe : f × F × Rm. Avec n surfaces, on multiplie par n.*

*Exemple : n = 2, f = 0,3, F = 1 500 N, garnitures de R = 60 mm et r = 40 mm. Rm = 50 mm = 0,05 m.
C = 2 × 0,3 × 1 500 × 0,05 = **45 N·m**.*''',
  '''> **C = n × f × F × rmoy**

- **n** : le nombre de surfaces frottantes (un disque pris entre deux plateaux : n = 2) ;
- **f** : le coefficient de frottement des **garnitures** — les couronnes de matériau de friction fixées
  sur le disque, l'équivalent des plaquettes de frein — donné par le fabricant ou l'énoncé ;
- **F** : l'effort presseur (le ressort) ;
- **rmoy** : le rayon moyen des garnitures, **(R + r) / 2**, où l'on considère que tout le frottement
  s'applique (hypothèse retenue pour une garniture rodée).

*D'où vient la formule ? Chaque surface frotte avec une force tangentielle f × F (loi de Coulomb, fiche
12.1), appliquée en moyenne à la distance rmoy de l'axe : f × F × rmoy. Avec n surfaces, on multiplie par n.*

*Exemple : n = 2, f = 0,3, F = 1 500 N, garnitures de R = 60 mm et r = 40 mm. rmoy = 50 mm = 0,05 m.
C = 2 × 0,3 × 1 500 × 0,05 = **45 N·m**.*''')
R('''monte jusqu'à casser ce maillon. Le limiteur **glisse** (à friction) ou **se déclenche** (à billes,
il désaccouple) au-delà d'un couple réglé. Sa règle de réglage :''',
  '''monte jusqu'à casser ce maillon. Le limiteur **glisse** (à friction) ou **se déclenche** au-delà d'un
couple réglé. Le limiteur à billes fonctionne comme une clé dynamométrique à déclenchement : des billes
poussées par des ressorts sont logées dans des creux ; au-delà du couple réglé, elles sortent des creux
(« clac ») et la transmission est coupée net ; on le réarme ensuite. Sa règle de réglage :''')
R('''**Le frein : ralentir, arrêter, maintenir.** Il transforme l'énergie cinétique (½ m v², ½ I ω², fiche
8.1) en chaleur,''', '''**Le frein : ralentir, arrêter, maintenir.** Il transforme l'énergie cinétique (½ m v², ½ I ω², fiche
8.1 ; I : moment d'inertie, la « masse » d'un objet qui tourne) en chaleur,''')

# §4 courroies et chaînes
R('''Le **rapport de transmission** k = N2 / N1 (sortie sur entrée). Pour deux poulies ou deux pignons, la
vitesse linéaire de la courroie ou de la chaîne est la même aux deux bouts : π d1 N1 = π d2 N2, d'où
**k = d1 / d2 = Z1 / Z2** (petit qui mène un grand → la sortie ralentit, le couple augmente : C2 = C1 × η / k).''',
  '''Le **rapport de transmission** r = N2 / N1 (sortie sur entrée), comme en fiche 6.11. Un maillon de la
chaîne passe à la même vitesse sur les deux pignons, sinon la chaîne casserait ou ferait du mou : π d1 N1
= π d2 N2, d'où **r = N2 / N1 = d1 / d2 = Z1 / Z2**. Les indices s'inversent : le petit tourne vite, le
grand lentement (la poulie de 24 dents fait 2 tours pendant que celle de 48 en fait 1).

**Le couple, par la puissance** : P = C × ω passe d'un bout à l'autre, moins les pertes : C2 × ω2 = η × C1 ×
ω1, d'où **C2 = C1 × η / r**. Image : le vélo — sur le grand pignon arrière, on monte la côte lentement
mais facilement. Ce qu'on perd en vitesse, on le gagne en couple.''')
R('''| Lien | Principe | Rapport | Pour | Contre |
|---|---|---|---|---|
| **courroie trapézoïdale, poly-V** | adhérence (flancs coincés dans la gorge) | approché (léger glissement) | silencieuse, amortit, **patine si blocage** | tension sur les paliers (fiche 6.11) |
| **courroie crantée** | obstacle (dents) | **exact** | synchronisme, peu de tension | un blocage la fait sauter ou casser |
| **chaîne à rouleaux** | obstacle (rouleaux sur pignon) | **exact** (vitesse moyenne) | gros couples, milieux difficiles | bruit, lubrification, légère ondulation de vitesse sur petit pignon |''',
  '''| Lien | Principe | Rapport | Ce que ça change pour la conception |
|---|---|---|---|
| **courroie plate, trapézoïdale, poly-V** (plate à petites nervures en V, celle de l'alternateur d'une voiture) | **adhérence** (flancs coincés dans la gorge) | approché (léger glissement) | **patine si blocage** : protection non réglée, qui use et échauffe la courroie |
| **courroie crantée** | **obstacle** (dents) | **exact** | synchronisme ; tension de pose plus faible qu'une trapézoïdale ; un blocage la fait sauter ou casser |
| **chaîne à rouleaux** | **obstacle** (rouleaux sur pignon) | **exact** en moyenne | gros couples ; sur un petit pignon, la chaîne s'enroule « par facettes » et la vitesse de sortie fluctue un peu à chaque dent |

Rendements, encombrement, tension sur les paliers : **fiche 6.11**.''')

# §5 vis-écrou
R('''- **n, le nombre de filets** : une vis peut avoir plusieurs hélices intercalées. Sur la désignation, une vis
  **Tr 20 × 8 (P4)** a un pas apparent de 4 mm et un pas d'hélice de 8 mm : **2 filets** ;
- **ph = P × n** : l'avance réelle pour un tour. C'est lui qui compte dans v = ph × N.''',
  '''- **n, le nombre de filets** : une vis peut avoir plusieurs hélices intercalées. Regardez le goulot d'un pot
  de confiture : plusieurs débuts de filet tout autour, et un quart de tour suffit pour fermer. Plusieurs
  filets, c'est beaucoup d'avance par tour sans filet grossier ;
- **ph = P × n** : l'avance réelle pour un tour. C'est lui qui compte dans v = ph × N.

**Lire une désignation : Tr 20 × 8 (P4)** — **Tr** : filet trapézoïdal (flancs en trapèze, pour transmettre
des efforts) ; **20** : diamètre nominal, en mm ; **8** : pas de l'hélice ph ; **(P4)** : pas apparent,
4 mm. Donc **2 filets**. Sans parenthèse (« Tr 20 × 4 »), la vis n'a qu'un filet et les deux pas sont égaux.''')
R('''**La réversibilité : la charge peut-elle faire tourner la vis ?** Déroulez un tour d'hélice : c'est un
plan incliné de pente **tan α = ph / (π d2)** (d2 : diamètre moyen du filet). Comme une caisse sur une
pente (fiche 12.1), la charge ne glisse pas tant que la pente reste sous l'angle de frottement :

> **irréversible si α ≤ φ**, avec tan φ = f''',
  '''**La réversibilité : la charge peut-elle faire tourner la vis ?** Deux étapes.

*L'angle de frottement, par l'expérience.* Posez une caisse sur une planche et soulevez lentement un bout.
Tant que la pente est faible, la caisse reste en place ; à un angle précis, elle se met à glisser. Cet angle
limite est **l'angle de frottement φ** ; il ne dépend que des deux matériaux, et **tan φ = f** (fiche
12.1). Pour f = 0,15, φ = arctan 0,15 ≈ 8,5°.

*Le filet est une rampe.* Enroulez un triangle de papier autour d'un crayon : son grand côté dessine une
hélice. Une vis, c'est cela à l'envers : « déroulé » à plat, un tour de filet devient une **rampe** de
longueur **π × d2** (d2 : diamètre moyen du filet, **d2 = d − 0,5 P** pour un filet trapézoïdal ; Tr 20 au
pas de 4 : d2 = 18 mm) et de hauteur **ph**. Sa pente : **tan α = ph / (π d2)**. L'écrou chargé est posé sur
cette rampe comme la caisse sur la planche : si la rampe est plus raide que l'angle de frottement, la
charge « glisse » le long du filet, et pour glisser elle doit faire tourner la vis.

> **irréversible si α ≤ φ**, avec tan φ = f

*(Modèle simplifié, comme si le filet était carré. Sur un filet trapézoïdal, l'inclinaison des flancs
augmente un peu le frottement apparent : la conclusion est la même, avec une marge légèrement plus grande.)*''')
R('''| **à billes** (à roulement) | élevé (de l'ordre de 0,9, fiche 13.3) | **réversible** | rapide, précise ; **un axe vertical exige un frein** |''',
  '''| **à billes** (à roulement) | élevé (de l'ordre de 0,9, valeur de catalogue constructeur) | **réversible** | rapide, précise ; **un axe vertical exige un frein** |''')
R('''charge.*

**La came : un mouvement imposé.**''', '''charge.*

**Irréversible, donc peu efficace.** C'est le même frottement qui tient la charge et qui consomme
l'énergie : avec f = 0,15, cette Tr 20 a un rendement d'environ 0,32 à un filet et 0,47 à deux filets. Une
vis irréversible a toujours un rendement inférieur à 50 % (approfondissement : η = tan α / tan(α + φ)).

**La came : un mouvement imposé.**''')
R('''arrêts, descentes — la **loi de levée**. Le cas le plus simple est la **came excentrique** : un disque
circulaire monté décalé de **e** sur son axe ; le poussoir fait une **course de 2e**, en un mouvement
quasi sinusoïdal.''', '''arrêts, descentes — la **loi de levée**. Le cas le plus simple est la **came excentrique** : un disque
circulaire monté décalé de **e** sur son axe ; le poussoir fait une **course de 2e** et monte et descend
sans à-coup, comme un piston. Pourquoi 2e ? Quand le décalage pointe vers le poussoir, le bord du disque est
à r0 + e de l'axe (poussoir au plus haut) ; un demi-tour plus tard, à r0 − e (au plus bas). La différence
vaut 2e : le rayon r0 du disque s'élimine.''')
R('''- **Bielle-manivelle** : rotation de la manivelle ↔ translation alternative du piston, **course = 2r**.
  Deux points morts par tour, où le piston s'arrête. Sa cinématique (vitesses, CIR, loi entrée-sortie
  non linéaire) est traitée en fiche **6.15** : on ne la refait pas ici. Un **excentrique** est une
  bielle-manivelle dont la manivelle est remplacée par un disque décalé de e (course 2e) : plus compact,
  plus robuste, pour les petites courses (pompes, presses).
- **Quadrilatère articulé** (quatre barres) : transforme une rotation continue en **oscillation** (essuie-
  glace, mécanisme de pelle).
- **Genouillère** : près du point mort, un petit effort d'entrée donne un **très grand effort** de sortie
  (bridage, presse, sertisseuse). C'est la même géométrie que la bielle-manivelle, utilisée au voisinage
  de l'alignement.''',
  '''- **Bielle-manivelle** : rotation de la manivelle ↔ translation alternative du piston, **course = 2r**.
  Deux points morts par tour, où bielle et manivelle sont alignées : pousser sur le piston ne fait plus
  tourner la manivelle (d'où le volant d'inertie des moteurs, qui passe les points morts sur son élan).
  Sa cinématique (vitesses, CIR, loi entrée-sortie non linéaire) est traitée en fiche **6.15** : on ne la
  refait pas ici. Un **excentrique à collier** (différent de la came excentrique : ici une bielle entoure
  le disque, au lieu d'un poussoir qui le touche) remplace la manivelle par un disque décalé de e
  (course 2e) : plus compact, plus robuste, pour les petites courses (pompes, presses).
- **Quadrilatère articulé** : quatre barres reliées par quatre articulations, dont une fixe. Le moteur
  d'essuie-glace tourne toujours dans le même sens ; une petite manivelle fait le tour complet et pousse
  une biellette qui fait aller et venir le bras du balai : une rotation continue devient une
  **oscillation**, sans inverser le moteur.
- **Genouillère** : vous l'avez en main avec la **pince-étau** — en fin de fermeture, les biellettes
  s'alignent presque, et la main suffit à serrer un écrou grippé. Pourquoi ? Près de l'alignement, un
  grand mouvement de la poignée ne fait plus avancer les mors que de quelques centièmes ; or le travail se
  conserve (aux pertes près) : effort × déplacement en entrée = effort × déplacement en sortie. Si la
  sortie bouge 50 fois moins, elle pousse environ 50 fois plus fort. Usages : bridage rapide, presse,
  sertisseuse.''')
R('''| protéger la transmission en cas de blocage | limiteur de couple (ou courroie lisse qui patine) |''',
  '''| protéger la transmission en cas de blocage | limiteur de couple (une courroie lisse qui patine protège aussi, sans réglage) |''')
R('''- **Embrayage à friction** : C = n f F Rm, Rm = (R + r) / 2. **Limiteur** : couple utile maxi < réglage <''',
  '''- **Embrayage à friction** : C = n f F rmoy, rmoy = (R + r) / 2. **Limiteur** : couple utile maxi < réglage <''')
R('''- **Courroie, chaîne** : k = N2 / N1 = d1 / d2 = Z1 / Z2 ; trapézoïdale = adhérence (glisse), crantée et
  chaîne = obstacle (rapport exact).''', '''- **Courroie, chaîne** : r = N2 / N1 = d1 / d2 = Z1 / Z2 ; trapézoïdale = adhérence (glisse), crantée et
  chaîne = obstacle (rapport exact).''')
R('''- **Vis-écrou** : v = ph × N, **ph = P × nombre de filets** ; irréversible si α ≤ φ (tan α = ph / π d2) ;''',
  '''- **Vis-écrou** : v = ph × N, **ph = P × nombre de filets** ; irréversible si α ≤ φ (tan α = ph / π d2,
  d2 = d − 0,5 P) ;''')
# formules
R('''**Embrayage, limiteur à friction** — C = n × f × F × Rm · Rm = (R + r) / 2 · n : nombre de surfaces
frottantes''', '''**Embrayage, limiteur à friction** — C = n × f × F × rmoy · rmoy = (R + r) / 2 · n : nombre de surfaces
frottantes''')
R('''**Courroie, chaîne** — k = N2 / N1 = d1 / d2 = Z1 / Z2 · C2 = C1 × η / k''',
  '''**Courroie, chaîne** — r = N2 / N1 = d1 / d2 = Z1 / Z2 · C2 = C1 × η / r''')
R('''**Vis-écrou** — v = ph × N · ph = P × n (pas apparent × nombre de filets) · tan α = ph / (π d2) ·
irréversible si α ≤ φ, tan φ = f''', '''**Vis-écrou** — v = ph × N · ph = P × n (pas apparent × nombre de filets) · tan α = ph / (π d2),
d2 = d − 0,5 P · irréversible si α ≤ φ, tan φ = f''')

# corrigé exercice
R('''> **k = Z1 / Z2** (courroie crantée).''', '''> **r = Z1 / Z2** (courroie crantée).''')
R('''positive. On le place en général sur le moteur, là où le couple à tenir est le plus faible.''',
  '''positive. On le place souvent sur le moteur : avant la courroie 24/48, le couple à tenir est deux fois
plus faible que sur la vis, et un frein plus petit coûte moins cher (d'où les moteurs à frein intégré).
Mais la courroie devient alors un maillon dont dépend la sécurité : si elle casse, la charge tombe. Sur un
axe vertical, on préfère un frein côté vis, ou bien une surveillance de rupture de courroie.''')
R('''**Ordres de grandeur** : 62,5 mm/s, une course en 4 s, cohérent pour un axe de dépose. **Puissance** :
29 W pour lever 40 kg à 6 cm/s, c'est peu''', '''**Ordres de grandeur** : 62,5 mm/s, une course en 4 s, cohérent pour un axe de dépose. **Puissance** :
29 W pour lever 400 N (environ 40 kg) à 6 cm/s, c'est peu''')
R('''    "**Calculer les vitesses étage par étage** : k = Z1 / Z2 (courroie, chaîne), v = ph × N avec "''',
  '''    "**Calculer les vitesses étage par étage** : r = Z1 / Z2 (courroie, chaîne), v = ph × N avec "''')

# ---------------- at162
R('''        "enonce": "Une table de machine est déplacée par une vis trapézoïdale Tr 20 × 8 (P4) qui tourne "
                  "à N = 300 tr/min. Le diamètre moyen du filet vaut d2 = 18 mm ; le coefficient de "
                  "frottement vis-écrou est donné : f = 0,15.",''',
  '''        "enonce": "Le chariot d'un axe vertical est déplacé par une vis trapézoïdale Tr 20 × 8 (P4) qui "
                  "tourne à N = 300 tr/min. Le diamètre moyen du filet vaut d2 = 18 mm ; le coefficient "
                  "de frottement vis-écrou est donné : f = 0,15.",''')
R('''"label": "Vitesse de la table",''', '''"label": "Vitesse du chariot",''')
R('''             "consigne": "Calcule la vitesse de la table, en mm/s.",''', '''             "consigne": "Calcule la vitesse du chariot, en mm/s.",''')
R('''             "pieges": [(4.05, "4,05° : tu as pris le pas apparent (4 mm) au lieu du pas de l'hélice "
                               "(8 mm).")],''',
  '''             "pieges": [(4.05, "4,05° : tu as pris le pas apparent (4 mm) au lieu du pas de l'hélice "
                               "(8 mm)."),
                        (7.26, "7,26° : tu as pris le diamètre nominal (20 mm). L'hélice se déroule sur le "
                               "diamètre moyen d2 = 18 mm."),
                        (0.1405, "0,1405 : ta calculatrice est en radians. Passe-la en degrés.")],''')
R('''             "pieges": [(0.15, "0,15, c'est f lui-même. L'angle de frottement est arctan f, en degrés.")],''',
  '''             "pieges": [(0.15, "0,15, c'est f lui-même. L'angle de frottement est arctan f, en degrés."),
                        (0.1489, "0,1489 : ta calculatrice est en radians. Passe-la en degrés.")],''')
R('''             "question": "α = 8,05° et φ = 8,53°. Que conclure pour la table, montée sur un axe vertical ?",''',
  '''             "question": "α = 8,05° et φ = 8,53°. Que conclure pour ce chariot vertical ?",''')

# ---------------- at163 : rmoy, et QCM final reformulé (doublon avec le quiz n°8)
R('''            ("Rayon moyen Rm",
             "la distance moyenne des garnitures à l'axe : (R + r) / 2."),''',
  '''            ("Rayon moyen rmoy",
             "la distance moyenne des garnitures à l'axe : (R + r) / 2."),''')
R('''             "consigne": "Calcule le rayon moyen des garnitures Rm.",
             "indice": "Rm = (R + r) / 2.",''', '''             "consigne": "Calcule le rayon moyen des garnitures rmoy.",
             "indice": "rmoy = (R + r) / 2.",''')
R('''             "aide": "Rm = (60 + 40) / 2 = 50 mm."},''', '''             "aide": "rmoy = (60 + 40) / 2 = 50 mm."},''')
R('''             "indice": "C = n × f × F × Rm, avec Rm en mètres.",''', '''             "indice": "C = n × f × F × rmoy, avec rmoy en mètres.",''')
R('''                        (45000, "45 000, c'est en N·mm : Rm doit être en mètres (0,05 m).")],''',
  '''                        (45000, "45 000, c'est en N·mm : rmoy doit être en mètres (0,05 m).")],''')
R('''             "indice": "F = C / (n × f × Rm).",''', '''             "indice": "F = C / (n × f × rmoy).",''')
R('''                        (1.833, "1,833 : Rm est en mm dans ton calcul ; il doit être en mètres.")],''',
  '''                        (1.833, "1,833 : rmoy est en mm dans ton calcul ; il doit être en mètres.")],''')
R('''            {"type": "qcm", "label": "Pourquoi un limiteur",
             "question": "Le convoyeur est entraîné par une chaîne. Pourquoi lui ajouter un limiteur, "
                         "alors qu'une courroie trapézoïdale n'en aurait pas forcément besoin ?",
             "options": ["Parce qu'une chaîne ne glisse pas : en cas de blocage, rien ne cède avant "
                         "une pièce", "Parce que la chaîne est moins rapide",
                         "Parce que la chaîne a un meilleur rendement"], "bonne": 0,
             "indice": "Que se passe-t-il quand le convoyeur se bloque, avec une courroie lisse ? avec "
                       "une chaîne ?",
             "diagnostics": {1: "La vitesse ne change rien au problème : c'est la façon de transmettre "
                                 "(obstacle ou adhérence) qui compte.",
                             2: "Le rendement est sans rapport avec la protection : une chaîne transmet "
                                "par obstacle et ne patine pas en cas de blocage."}},''',
  '''            {"type": "qcm", "label": "Après un blocage",
             "question": "Une pièce se coince dans le convoyeur. Le limiteur glisse. Que doit faire "
                         "l'opérateur ?",
             "options": ["Arrêter le convoyeur, dégager la pièce : le limiteur à friction se remet à "
                         "transmettre de lui-même", "Remplacer le limiteur, qui est détruit",
                         "Augmenter l'effort presseur pour que le convoyeur force le passage"], "bonne": 0,
             "indice": "Un limiteur à friction glisse sans casser ; c'est la goupille de cisaillement "
                       "qui se remplace.",
             "diagnostics": {1: "C'est la goupille de cisaillement (limiteur « fusible ») qui se remplace. "
                                 "Le limiteur à friction glisse, chauffe un peu, et retransmet une fois le "
                                 "blocage dégagé.",
                             2: "Serrer davantage, c'est remonter le couple de réglage vers celui qui casse "
                                "la clavette : on supprime la protection au lieu de traiter la cause."}},''')
R('''            "regle": "**C = n × f × F × Rm**, Rm = (R + r) / 2. Réglage : **couple utile maxi < "''',
  '''            "regle": "**C = n × f × F × rmoy**, rmoy = (R + r) / 2. Réglage : **couple utile maxi < "''')
R('''            "conversions": "Rm = 50 mm = 0,05 m.",''', '''            "conversions": "rmoy = 50 mm = 0,05 m.",''')
R('''            "calcul": "**Rm = 50 mm** ; **C = 45 N·m** ;''', '''            "calcul": "**rmoy = 50 mm** ; **C = 45 N·m** ;''')
R('''        "a_retenir": "À retenir : un limiteur se règle entre le couple de service et le couple qui "
                     "casse le maillon faible ; une transmission par obstacle (chaîne, crantée) en a "
                     "besoin, une courroie lisse patine d'elle-même.",''',
  '''        "a_retenir": "À retenir : un limiteur se règle entre le couple de service et le couple qui "
                     "casse le maillon faible ; à friction, il glisse sans casser et retransmet une fois "
                     "le blocage dégagé.",''')

# ---------------- générateur : désignation seulement pour Tr 20 au pas de 4 (cas du cours)
R('''    # diamètres et pas usuels de la série principale des vis trapézoïdales
    d, P = random.choice([(16, 4), (20, 4), (24, 5), (32, 6), (40, 7)])
    nf = random.choice([1, 2, 2, 3])''',
  '''    P = random.choice([2, 3, 4, 4, 5, 6])
    nf = random.choice([1, 2, 2, 3])''')
R('''    desig = f"Tr {d} × {ph} (P{P})" if nf > 1 else f"Tr {d} × {P}"''',
  '''    # la désignation n'est écrite que pour la vis du cours (Tr 20 au pas de 4) ; sinon, pas de diamètre
    if P == 4:
        desig = f"**Tr 20 × {ph} (P4)**" if nf > 1 else "**Tr 20 × 4**"
    else:
        desig = (f"trapézoïdale à **{nf} filets**, de pas apparent **{P} mm**," if nf > 1
                 else f"trapézoïdale à **un filet**, de pas **{P} mm**,")''')
R('''        "enonce": (f"Une vis **{desig}** tourne à **{N} tr/min**. À quelle vitesse l'écrou avance-t-il, "
                   "en mm/s ?"),''', '''        "enonce": (f"Une vis {desig} tourne à **{N} tr/min**. À quelle vitesse l'écrou avance-t-il, "
                   "en mm/s ?"),''')
R('''            f"**Ce que dit l'énoncé.** Une vis {desig} à {N} tr/min. On cherche la vitesse de l'écrou.",
            "**La désignation.** " + (f"{desig} : pas de l'hélice {ph} mm, pas apparent {P} mm, "
                                      f"donc {nf} filets." if nf > 1 else
                                      f"{desig} : un seul filet, le pas de l'hélice égale le pas, {P} mm."),''',
  '''            f"**Ce que dit l'énoncé.** Une vis à {nf} filet{'s' if nf > 1 else ''}, de pas apparent {P} mm, "
            f"à {N} tr/min. On cherche la vitesse de l'écrou.",
            "**Le pas de l'hélice.** " + (f"Avec {nf} filets, l'écrou avance de {nf} pas apparents par tour."
                                          + (f" (Tr 20 × {ph} (P4) : {ph} = pas de l'hélice, P4 = pas apparent.)"
                                             if P == 4 else "") if nf > 1 else
                                          "Un seul filet : le pas de l'hélice égale le pas apparent."),''')
R('''            f"**Le calcul.** v = {ph} × {N} = {ph * N} mm/min, soit {fr(v, 2)} mm/s.",''',
  '''            f"**Le calcul.** v = {ph} × {N} = {fr(ph * N, 0)} mm/min, soit {fr(v, 2)} mm/s.",''')
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print("ok")
