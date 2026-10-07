# -*- coding: utf-8 -*-
# Corrections du brouillon 13.7 après relecture (relecteur-bts-meca B1-B7 + améliorations ;
# prof-pedagogue B1-B4 + améliorations). Non repris faute de source vérifiée : seuil 450 °C du brasage,
# numéros de séries d'alliages d'aluminium, format 3MF.
import math, os
ICI = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(ICI, 'brouillon_13_7.py')
c = open(F, encoding='utf-8').read()


def R(a, b, n=1):
    global c
    assert c.count(a) == n, (a[:80], c.count(a))
    c = c.replace(a, b)


# ---------------------------------------------------------------- figures
R('''    p.append(f"<rect x='{x + 124}' y='118' width='44' height='18' fill='{ARBRE}'><animate attributeName='width' values='0;44;44' dur='3s' repeatCount='indefinite'/></rect>")''',
  '''    p.append(f"<rect x='{x + 124}' y='118' width='44' height='18' fill='{ARBRE}'><animate attributeName='width' values='0;44;44' dur='3s' repeatCount='indefinite'/></rect>")
    p.append(_txt(x + 150, 176, "profilé qui sort", 9, ARBRE, "middle", True))''')
R('''    p.append(_k_fl(x + 87, 214, x + 87, 196, ALERTE, "kr", 2))''',
  '''    p.append(_txt(x + 87, 150, "paraison", 9, ARBRE, "middle", True))
    p.append(_k_fl(x + 87, 214, x + 87, 196, ALERTE, "kr", 2))''')
R('''(585, "COMPRESSION", "pièce épaisse, thermodur."))''', '''(585, "COMPRESSION", "pièce épaisse, thermodurcissable"))''')
R('''    p.append(_txt(x + 87, 244, "pièces électriques, SMC", 9, TRAIT, "middle"))''',
  '''    p.append(_txt(x + 87, 244, "pièces électriques, composites SMC", 9, TRAIT, "middle"))''')
R('''("poudre + liant", "injection", "déliantage", "frittage"),''', '''("poudre + liant", "injection", "déliantage", "frittage = pièce"),''')
R('''    p = [_k_defs(), _txt(30, 24, "Assembler sans fondre les pièces : brasage, friction, ultrasons", 13, TRAIT, "start", True)]''',
  '''    p = [_k_defs(), _txt(30, 24, "Assembler sans arc ni métal fondu en masse : brasage, friction, ultrasons", 13, TRAIT, "start", True)]''')
R('''    p.append(_txt(147, 96, "manchon", 9, FIN, "middle"))''',
  '''    p.append(_txt(147, 96, "manchon", 9, FIN, "middle"))
    p.append(_txt(85, 146, "tube", 9, FIN, "middle"))
    p.append(_txt(232, 112, "jeu fin", 9, FIN, "start"))''')
R('''    p.append(f"<rect x='388' y='110' width='80' height='40' fill='#e2e8f0' stroke='{TRAIT}'/>")''',
  '''    p.append(f"<rect x='388' y='110' width='80' height='40' fill='#e2e8f0' stroke='{TRAIT}'/>")
    p.append(_txt(340, 134, "tourne", 9, FIN, "middle"))
    p.append(_txt(428, 134, "fixe", 9, FIN, "middle"))''')
R('''    p.append(_txt(392, 214, "se malaxe sans fondre, puis forge", 10, TRAIT, "middle"))''',
  '''    p.append(_txt(392, 214, "se malaxe sans fondre, puis on écrase", 10, TRAIT, "middle"))''')
R('''    p.append(_txt(637, 196, "la vibration fond l'interface,", 10, OK, "middle", True))''',
  '''    p.append(_txt(637, 196, "la vibration fond l'interface seule,", 10, OK, "middle", True))''')
R('''    p.append(_txt(46, 324, "Point commun : on évite de fondre les pièces — moins de déformation, des matériaux différents assemblables.", 12, TRAIT))''',
  '''    p.append(_txt(46, 324, "Point commun : peu ou pas de chaleur dans la masse des pièces — moins de déformation, matériaux différents assemblables.", 11, TRAIT))''')
# STL : rayons, demi-angle, R cos(π/n)
R('''    p.append(f"<line x1='{xc:.1f}' y1='{yc:.1f}' x2='{xm:.1f}' y2='{ym:.1f}' stroke='{ALERTE}' stroke-width='2.4'/>")''',
  '''    p.append(f"<line x1='{xc:.1f}' y1='{yc:.1f}' x2='{xm:.1f}' y2='{ym:.1f}' stroke='{ALERTE}' stroke-width='2.4'/>")
    x1_, y1_ = pts[0]
    x2_, y2_ = pts[1]
    p.append(f"<line x1='{cx}' y1='{cy}' x2='{x1_:.1f}' y2='{y1_:.1f}' stroke='{TRAIT}' stroke-width='1.2'/>")
    p.append(f"<line x1='{cx}' y1='{cy}' x2='{x2_:.1f}' y2='{y2_:.1f}' stroke='{TRAIT}' stroke-width='1.2'/>")
    p.append(f"<line x1='{cx}' y1='{cy}' x2='{xc:.1f}' y2='{yc:.1f}' stroke='{OK}' stroke-width='1.6' stroke-dasharray='4 3'/>")
    p.append(_txt(cx + 60, cy - 6, "R", 11, TRAIT, "middle", True))
    p.append(_txt(cx + 30, cy + 20, "π/n", 10, TRAIT, "middle", True))
    p.append(_txt(cx + 40, cy + 54, "R cos(π/n)", 10, OK, "middle", True))''')
# figure à curseurs : f_max
R('''              ("tolérance visée (énoncé) : 0,01 mm", TRAIT, False),''', '''              ("tolérance visée f_max (énoncé) : 0,01 mm", TRAIT, False),''')
R('''              (f"nombre minimal : n ≥ π / arccos(1 − f / R) = {n_min}", ALESAGE, True), ("", TRAIT, False),
              ("Doubler n divise la flèche par environ 4 :", FIN, False),
              ("le fichier grossit vite pour un gain de précision faible.", FIN, False))''',
  '''              (f"nombre minimal : n ≥ π / arccos(1 − f_max / R) = {n_min}", ALESAGE, True), ("", TRAIT, False),
              ("Doubler n double le fichier et divise la flèche par 4.", FIN, False),
              ("Au-delà de la finesse de la machine, plus rien n'est gagné.", FIN, False))''')

# ---------------------------------------------------------------- cours
R('''il dépendent de la machine et de la matière : elles viennent du spécialiste ou du fournisseur, pas d'un cours.''',
  '''il dépendent de la machine et de la matière : elles viennent du spécialiste ou du fournisseur, pas d'un cours.''', 0) if False else None
R('''dépendent de la machine et de la matière : elles viennent du spécialiste ou du fournisseur, pas d'un cours.''',
  '''dépendent de la machine et de la matière : elles viennent du spécialiste ou du fournisseur, pas d'un cours.
« Petite » ou « grande » série n'est pas un nombre fixe : c'est le seuil de rentabilité (§6) qui dit, pour une
pièce donnée, à partir de combien d'exemplaires un moule devient rentable.''')
R('''**Extrusion.** Une vis tourne dans un fourreau chauffé, fait fondre les granulés et pousse la matière à
travers une **filière** qui lui donne sa section.''',
  '''**Extrusion.** Une vis tourne dans un fourreau chauffé, fait fondre les granulés et pousse la matière à
travers une **filière** qui lui donne sa section. *C'est le tube de dentifrice, ou la machine à pâtes fraîches :
ce qui sort a toujours la forme du trou ; changer de profil, c'est changer de filière, pas de machine.*''')
R('''- **Quand** : très grandes séries (production continue) ; thermoplastiques.
- **Limites** : la section ne varie pas le long de la pièce ; les détails (perçages, encoches) demandent une
  reprise.''',
  '''- **Quand** : très grandes séries (production continue) ; thermoplastiques (le même principe file aussi les
  profilés d'aluminium et les joints en caoutchouc).
- **Limites** : la section ne varie pas le long de la pièce ; les détails (perçages, encoches) demandent une
  opération supplémentaire après.''')
R('''**Soufflage.** Un tube de matière chaude (la **paraison**) ou une préforme injectée est enfermé dans un moule
en deux coquilles, puis gonflé à l'air comprimé contre ses parois.''',
  '''**Soufflage.** Un tube de matière chaude (la **paraison**) ou une préforme injectée est enfermé dans un moule
en deux coquilles, puis gonflé à l'air comprimé contre ses parois. *Comme un ballon qu'on gonfle à l'intérieur
d'une boîte : il en prend la forme. La préforme, c'est la petite « éprouvette » à goulot déjà fileté qu'on voit
avant qu'elle devienne bouteille d'eau : le goulot est injecté (précis), le corps est soufflé.*''')
R('''- **Limites** : on maîtrise la forme extérieure, pas l'intérieur ; l'épaisseur varie (plus mince là où la
  matière s'étire le plus).''',
  '''- **Limites** : on maîtrise la forme extérieure, pas l'intérieur ; l'épaisseur varie — comme un ballon, la
  paroi est plus fine là où elle a dû aller le plus loin, dans les coins.''')
R('''**Thermoformage.** Une plaque thermoplastique est chauffée jusqu'à se ramollir, puis plaquée sur un moule par
aspiration (vide) ou par pression.
- **À quoi** : les **coques minces** de grande surface : bacs, capots, habillages, emballages, coques de
  bateau de petite série.
- **Quand** : petites et moyennes séries ; l'outillage est simple (une seule face) et peu coûteux.
- **Limites** : une seule face est précise ; l'épaisseur diminue dans les angles et les fonds profonds ; il
  faut détourer la pièce après formage.''',
  '''**Thermoformage** (complément au programme). Une plaque thermoplastique est chauffée jusqu'à se ramollir, puis
plaquée sur un moule par aspiration (vide) ou par pression. *C'est le blister des piles, ou le pot de yaourt.*
- **À quoi** : les **coques minces** : bacs, capots, habillages, emballages.
- **Quand** : petites et moyennes séries pour les grandes pièces techniques (l'outillage, à une seule face, est
  simple et peu coûteux) ; très grandes séries pour les emballages minces, sur des machines alimentées en
  bobine.
- **Limites** : une seule face est précise (seule la face plaquée contre le moule en recopie la forme) ;
  l'épaisseur diminue dans les angles, parce que la plaque s'étire comme un chewing-gum ; il faut détourer la
  pièce après formage (découper le bord de plaque en trop).''')
R('''**Compression.** La matière est déposée dans un moule chauffé, puis pressée par un poinçon jusqu'au
durcissement.
- **À quoi** : pièces **épaisses** en **thermodurcissables** (pièces électriques isolantes) et composites à
  fibres préimprégnés (SMC, fiche 13.1).''',
  '''**Compression.** La matière est déposée dans un moule chauffé, puis pressée par un poinçon jusqu'au
durcissement. *Comme un gaufrier : on dépose la pâte dosée, on ferme, on chauffe ; un thermodurcissable « cuit »
et ne refondra plus jamais, comme la gaufre.*
- **À quoi** : pièces **épaisses** en **thermodurcissables** (pièces électriques isolantes) et composites en
  **SMC** (*Sheet Moulding Compound* : feuille de résine chargée de fibres de verre coupées, prête à mouler :
  capots, boîtiers électriques).''')
R('''*Retenir la logique : profil constant → extrusion ; creux fermé → soufflage ; coque mince et grande, petite
série → thermoformage ; pièce complexe de grande série → injection (fiche 13.1) ; thermodurcissable épais →
compression.*''',
  '''*Retenir la logique : profil constant → extrusion ; creux fermé → soufflage ; coque mince → thermoformage ;
pièce complexe de grande série → injection (fiche 13.1) ; thermodurcissable épais → compression.*''')
R('''**Le principe commun : le frittage.** Une poudre métallique, mise en forme, est chauffée **sous son point de
fusion** : les grains se soudent entre eux à leurs points de contact. On obtient une pièce sans jamais avoir
fondu le métal.''',
  '''**Le principe commun : le frittage.** Une poudre métallique, mise en forme, est chauffée **sous son point de
fusion** : les grains se soudent entre eux à leurs points de contact. *Pensez à la neige d'une piste : tassée,
puis laissée au froid, elle devient une plaque dure sans jamais avoir fondu.* Pourquoi ne pas fondre
complètement ? Un métal liquide coulerait et perdrait la forme donnée par la matrice : en restant sous la
fusion, la pièce garde sa forme. (Les céramiques techniques de la fiche 3.5 sont aussi frittées.)''')
R('''- **À quoi** : engrenages, cames, pièces de serrures, **coussinets autolubrifiants** (la porosité retient
  l'huile).''',
  '''- **À quoi** : engrenages, cames, pièces de serrures, **coussinets autolubrifiants** (la porosité retient
  l'huile, comme une éponge imbibée qui la rend quand l'arbre tourne).''')
R('''- **Limites** : la pièce sort de la matrice dans un seul sens : pas de contre-dépouille perpendiculaire à
  l'axe de compression ; la pièce reste un peu **poreuse**, donc moins résistante qu'une pièce forgée.''',
  '''- **Limites** : on tasse la poudre comme le café dans le porte-filtre d'un expresso — on ne peut presser que de
  haut en bas, et la pastille ressort par le haut : pas de contre-dépouille (gorge ou trou sur le côté, qui
  accrocherait la pièce dans la matrice) ; la pièce reste un peu **poreuse**, donc moins résistante qu'une
  pièce forgée.''')
R('''- **Limites** : le **retrait** au frittage est important — le moule est fait plus grand, d'une valeur donnée
  par le fournisseur ; pièces de petite taille ; moule coûteux, donc rentable seulement en série (§6).''',
  '''- **Limites** : le **retrait** au frittage est important. Pourquoi : après déliantage, il reste un
  « squelette » de grains avec des vides là où était le plastique ; au frittage, les grains se rapprochent pour
  les combler, et toute la pièce rétrécit. Le moule est donc fait plus grand, d'une valeur donnée par le
  fournisseur. Pièces de petite taille ; moule coûteux, donc rentable seulement en série (§6).''')
R('''### 4. Assembler sans fondre les pièces

[[FIG:assemblages_sans_fusion]]

Le soudage à l'arc (fiche 13.2) fond les bords des pièces. Trois familles l'évitent :''',
  '''### 4. Assembler sans arc ni métal fondu en masse

[[FIG:assemblages_sans_fusion]]

Le soudage à l'arc (fiches 12.3 et 13.2) fond les bords des pièces. Trois familles évitent de fondre la masse
des pièces : le brasage (seul l'apport fond), la friction (soudage à l'état solide, sans fusion), les ultrasons
(fusion très localisée de l'interface des plastiques, sans apport ni chauffage extérieur).''')
R('''**Brasage.** Un **métal d'apport**, qui fond à une température plus basse que celle des pièces, est fondu et
s'infiltre par **capillarité** dans le jeu entre les pièces ; les pièces, elles, ne fondent pas.''',
  '''**Brasage.** Un **métal d'apport**, qui fond à une température plus basse que celle des pièces, est fondu et
s'infiltre par **capillarité** dans le jeu entre les pièces ; les pièces, elles, ne fondent pas. *Comme le sucre
trempé dans le café, qui « boit » le liquide par le bas : un liquide monte tout seul dans un passage très fin.
D'où un jeu faible et régulier : trop large, le métal fondu n'est plus aspiré et le joint reste creux. Le fer à
souder de l'électronicien fait d'ailleurs du brasage tendre : la « soudure à l'étain » ne fond jamais les pattes
du composant.*''')
R('''- **Quand** : assembler des **matériaux différents** (cuivre sur acier, plaquette de carbure sur un corps
  d'outil), des pièces minces, des tubes.
- **Limites** : joint moins résistant que les pièces ; il faut un jeu faible et régulier (capillarité) et des
  surfaces propres.''',
  '''- **À quoi** : tuyauteries de climatisation, plaquettes de carbure sur un corps d'outil, électronique.
- **Quand** : assembler des **matériaux différents** (cuivre sur acier, carbure sur acier), des pièces minces,
  des tubes.
- **Limites** : le métal d'apport est moins résistant que les pièces — on compense par un recouvrement
  (emboîtement) suffisant ; il faut un jeu faible et régulier et des surfaces propres.''')
R('''**Soudage par friction.** Une pièce tourne contre l'autre sous poussée ; le frottement chauffe l'interface, la
matière se ramollit et se malaxe **sans fondre**, puis on arrête la rotation et on forge.
- **Quand** : pièces de **révolution** (arbres, axes, soupapes), y compris de matériaux différents ; la
  variante **FSW** (friction-malaxage), avec un outil tournant qui avance le long du joint, assemble des
  tôles d'aluminium difficiles à souder à l'arc.''',
  '''**Soudage par friction.** Une pièce tourne contre l'autre sous poussée ; le frottement chauffe l'interface (comme
des mains frottées très vite), la matière se ramollit et se malaxe **sans fondre** ; puis on arrête la rotation et
on pousse fort une dernière fois : les deux matières s'écrasent l'une dans l'autre et se soudent.
- **À quoi** : arbres, axes, soupapes bimétal.
- **Quand** : pièces de **révolution**, y compris de matériaux différents ; la variante **FSW**
  (friction-malaxage), avec un outil tournant qui avance le long du joint comme une cuillère qui touille une
  pâte épaisse, assemble des tôles d'aluminium sans les fondre : moins de déformation, et possibilité de souder
  certains alliages réputés difficiles à souder à l'arc.''')
R('''**Soudage par ultrasons.** Une **sonotrode** fait vibrer une pièce contre l'autre à haute fréquence ; le
frottement fond localement l'interface de deux **thermoplastiques**, en un cycle très court, sans apport.
- **Quand** : boîtiers plastiques, filtres, emballages ; fils et feuilles métalliques minces (connectique).
- **Limites** : pièces de petite taille, matières compatibles ; le joint se prépare au dessin (une nervure en
  pointe, le « directeur d'énergie », concentre la fusion).''',
  '''**Soudage par ultrasons.** Une **sonotrode** fait vibrer une pièce contre l'autre à haute fréquence : c'est comme
frotter les deux pièces des milliers de fois par seconde ; seule l'interface de deux **thermoplastiques** chauffe
jusqu'à fondre, en un cycle très court, sans apport, le reste de la pièce restant froid.
- **À quoi** : boîtiers plastiques, filtres, emballages ; sur des fils et feuilles métalliques minces
  (connectique), la liaison se fait sans fusion.
- **Limites** : pièces de petite taille, matières compatibles ; le joint se prépare au dessin (une nervure en
  pointe, le « directeur d'énergie », concentre la vibration sur une ligne, comme la pointe d'une punaise
  concentre l'effort).

**Quel assemblage ?** Deux métaux identiques et épais, qu'on peut fondre : soudage à l'arc. Deux matériaux
différents, des pièces minces ou des tubes : brasage. Deux pièces de révolution, ou des tôles d'aluminium :
friction, FSW. Deux petites pièces thermoplastiques : ultrasons.''')
R('''**Le STL, format pivot de la fabrication additive.** Une imprimante 3D ne lit pas un modèle CAO : elle lit une
surface découpée en **facettes triangulaires**. Chaque facette est décrite par ses **trois sommets** et sa
**normale** (le vecteur qui indique le côté extérieur de la matière). Le logiciel de l'imprimante tranche ce
maillage en couches.''',
  '''*Un ballon de football est fait de pièces plates cousues : de loin il paraît rond, de près on voit des
facettes. Le STL, c'est pareil, avec des triangles.*

**Le STL, format pivot de la fabrication additive.** Le logiciel de préparation de l'imprimante (le
**trancheur**) ne lit pas un modèle CAO : le modèle CAO décrit des formes exactes par leurs paramètres (un
cylindre = un axe et un rayon), dans un format propre à chaque logiciel. Le trancheur a besoin d'une
description simple et universelle qu'il peut couper en tranches : une surface découpée en **facettes
triangulaires** (fiche 9.7). Chaque facette est décrite par ses **trois sommets** et sa **normale** (une petite
flèche qui pointe vers l'extérieur de la matière). Le trancheur coupe ce maillage en couches et produit le
programme de la machine.''')
R('''**Ce que le STL ne contient pas** : ni unité, ni cote, ni tolérance, ni matière, ni historique de construction.
C'est pour cela qu'on n'envoie jamais un STL à un usineur (fiche 12.4) : on lui envoie un STEP et un plan.''',
  '''**Ce que le STL ne contient pas** : ni unité, ni cote, ni tolérance, ni matière, ni historique de construction.
*Le STL est à la CAO ce qu'une photo pixelisée est à un dessin coté : on voit la forme, mais on ne peut pas y
lire « Ø20 H7 ». L'alésage y est devenu un polygone : l'usineur ne retrouve ni son vrai diamètre ni son axe, et
ne sait même pas si « 20 » veut dire 20 mm ou 20 pouces.* C'est pour cela qu'on n'envoie jamais un STL pour
usiner une pièce cotée (fiche 12.4) : on envoie un **STEP** (format d'échange qui garde les vraies surfaces,
lisible par tous les logiciels de CAO et de FAO) et un plan.''')
R('''**Ce qu'il exige** : un volume **fermé** (« étanche » : aucun trou entre facettes) et des normales cohérentes ;
sinon le trancheur ne sait plus où est la matière.''',
  '''**Ce qu'il exige** : un volume **fermé** (« étanche » : aucun trou entre facettes — comme un ballon, un seul trou
et on ne sait plus ce qui est dedans ou dehors) et des normales cohérentes ; sinon le trancheur ne sait plus où
est la matière.''')
R('''**La finesse du maillage.** Une surface courbe est remplacée par des cordes : l'écart maximal entre le cercle et
une corde s'appelle la **flèche** (ou écart de corde). Pour un cercle de rayon R découpé en n facettes :

> **f = R × (1 − cos(π / n))**

*Exemple : un cercle de rayon 20 mm, avec une tolérance de corde de 0,01 mm (donnée d'énoncé) : il faut
n ≥ π / arccos(1 − 0,01 / 20) ≈ 99,3, soit **100 facettes** sur le tour. Avec 36 facettes, la flèche vaut
20 × (1 − cos(5°)) ≈ 0,076 mm : un cylindre visiblement facetté.* À l'export, le logiciel de CAO demande cette
tolérance de corde et un écart angulaire ; plus on les resserre, plus le fichier est lourd.''',
  '''**La finesse du maillage.** Une surface courbe est remplacée par des cordes : l'écart maximal entre le cercle et
une corde s'appelle la **flèche** (ou écart de corde). *Pensez à un arc de tir : la flèche est posée au milieu
de la corde et pointe vers le bois de l'arc. Ici, c'est la distance entre le milieu de la corde (la facette) et
l'arc de cercle.*

**D'où vient la formule**, en trois étapes : (1) n facettes se partagent le tour : chacune occupe un angle 2π/n
vu depuis le centre ; (2) le rayon qui coupe la facette en son milieu forme, avec la demi-corde, un triangle
rectangle dont l'angle au centre vaut π/n : le centre est à R × cos(π/n) du milieu de la corde ; (3) le cercle,
lui, est à R du centre ; l'écart entre les deux est la flèche :

> **f = R − R cos(π / n) = R × (1 − cos(π / n))** · nombre minimal de facettes pour une flèche maximale admise
> f_max : **n ≥ π / arccos(1 − f_max / R)** (calculatrice en radians), arrondi à l'entier supérieur

*Exemple : un cercle de rayon 20 mm, avec une flèche maximale admise f_max = 0,01 mm (donnée d'énoncé) : il faut
n ≥ π / arccos(1 − 0,01 / 20) ≈ 99,3, soit **100 facettes** sur le tour. Avec 36 facettes (π/36 rad, soit 5°), la
flèche vaut 20 × (1 − cos 5°) ≈ 0,076 mm : un cylindre visiblement facetté.* À l'export, le logiciel de CAO
demande cette tolérance de corde et un **écart angulaire** (le « pli » maximal autorisé entre deux facettes
voisines, qui évite que les petits rayons soient trop facettés). Doubler n double le fichier et divise la flèche
par 4 : c'est payant au début ; mais une fois la flèche plus fine que ce que l'imprimante sait reproduire
(épaisseur de couche, diamètre de buse), ajouter des facettes n'apporte plus rien.''')
R('''**La numérisation 3D** fait le chemin inverse : on part d'une pièce réelle.''',
  '''**Encadré : le chemin inverse, la numérisation 3D.** On part d'une pièce réelle.''')
R('''- **Limites** : surfaces brillantes ou transparentes difficiles à scanner ; trous profonds et zones cachées
  non relevés ; un maillage n'est pas un modèle CAO utilisable pour usiner.''',
  '''- **Limites** : surfaces brillantes ou transparentes difficiles à scanner ; trous profonds et zones cachées
  non relevés ; un maillage n'est pas un modèle CAO utilisable pour usiner une pièce cotée et tolérancée.''')
R('''Les deux droites se croisent au **seuil de rentabilité** N* :

> **N* = (outillage B − outillage A) / (coût unitaire A − coût unitaire B)**

*Exemple (données d'énoncé) : une petite pièce en acier, usinée pour 12 € pièce sans outillage, ou en MIM avec un
moule de 25 000 € et 2 € par pièce. N* = 25 000 / (12 − 2) = **2 500 pièces**.''',
  '''Appelons A le procédé sans (ou presque sans) outillage, par exemple l'usinage, et B le procédé à moule, par
exemple le MIM. Au **seuil de rentabilité** N*, les deux factures sont égales :

> outillage A + N × coût unitaire A = outillage B + N × coût unitaire B, d'où
> **N* = (outillage B − outillage A) / (coût unitaire A − coût unitaire B)** = surcoût du moule / économie par pièce

*Exemple (données d'énoncé) : une petite pièce en acier, usinée pour 12 € pièce sans outillage, ou en MIM avec un
moule de 25 000 € et 2 € par pièce. Chaque pièce faite en MIM fait économiser 12 − 2 = 10 € ; il en faut 25 000 /
10 = **2 500** pour que ces économies « remboursent » le moule — le calcul d'un abonnement de salle de sport
comparé aux entrées à l'unité.''')
R('''**La grille de choix d'un concepteur** — à appliquer dans cet ordre :''',
  '''**La grille de choix d'un concepteur** — ordre conseillé, avec retours en arrière quand une exigence (contact
alimentaire, température) impose le matériau :''')
R('''4. **Les exigences** : précision, état de surface, résistance (une pièce frittée est poreuse, une pièce
   thermoformée a une seule face précise).''',
  '''4. **Les exigences** : précision, état de surface, résistance (une pièce frittée est poreuse, une pièce
   thermoformée a une seule face précise).

| Ma pièce est… | Matériau | Procédé à envisager | La limite à vérifier sur le dessin |
|---|---|---|---|
| un profil de section constante, long (tube, joint) | thermoplastique | extrusion | section identique partout ; perçages après |
| un corps creux fermé (flacon, réservoir) | thermoplastique | soufflage | seul l'extérieur est précis ; épaisseur variable |
| une coque mince (bac, capot, emballage) | thermoplastique en plaque | thermoformage | une seule face précise ; amincissement dans les angles |
| une pièce plastique complexe, grande série | thermoplastique | injection (13.1) | dépouilles, épaisseur régulière |
| une pièce épaisse qui ne doit pas refondre | thermodurcissable, SMC | compression | formes simples ; bavure au plan de joint |
| une pièce métallique qui sort de la matrice dans un seul sens (pignon, came) | poudre métallique | compression + frittage | pas de contre-dépouille ; pièce poreuse |
| une petite pièce métallique de forme 3D complexe, grande série | poudre métallique | MIM | retrait au frittage ; petite taille |
| une pièce unitaire ou en très petite série, cotes serrées | métal, plastique | usinage (12.4) | coût par pièce élevé |
| un prototype, une forme impossible à mouler | plastique, métal | fabrication additive (9.7, 13.6), fichier STL | facettage, état de surface |''')
R('''6. **Exporter un STL trop grossier** : cylindres facettés ; ou trop fin : fichier énorme sans gain utile.''',
  '''6. **Exporter un STL trop grossier** : cylindres facettés ; ou trop fin : fichier énorme, plus fin que ce que la
   machine sait faire.''')
R('''5. **Envoyer un STL pour usinage** : pas de cote, pas de tolérance.''',
  '''5. **Envoyer un STL pour usiner une pièce cotée** : pas de cote, pas de tolérance, pas d'unité.''')
R('''- **Brasage** (apport seul fondu, capillarité), **friction** (malaxage sans fusion, révolution ; FSW pour
  l'aluminium), **ultrasons** (thermoplastiques, cycle court).''',
  '''- **Brasage** (apport seul fondu, capillarité), **friction** (malaxage sans fusion, révolution ; FSW pour
  l'aluminium), **ultrasons** (fusion locale de l'interface des thermoplastiques, cycle court).''')
R('''- **STL** : facettes triangulaires (3 sommets + normale), sans unité ni tolérance ; volume étanche ; flèche
  **f = R (1 − cos(π/n))**.''',
  '''- **STL** : facettes triangulaires (3 sommets + normale), sans unité ni tolérance ; volume étanche ; flèche
  **f = R (1 − cos(π/n))**, et **n ≥ π / arccos(1 − f_max / R)**.''')
R('''**Flèche d'un maillage** — f = R × (1 − cos(π / n)) · nombre minimal de facettes : n ≥ π / arccos(1 − f / R)''',
  '''**Flèche d'un maillage** — f = R × (1 − cos(π / n)) · nombre minimal de facettes pour une flèche maximale admise
f_max : n ≥ π / arccos(1 − f_max / R), en radians, arrondi à l'entier supérieur''')
R('''**Seuil de rentabilité** — coût total = outillage + N × coût unitaire · N* = (outillage B − outillage A) / (coût unitaire A − coût unitaire B)''',
  '''**Seuil de rentabilité** — coût total = outillage + N × coût unitaire · A sans outillage, B à moule :
N* = (outillage B − outillage A) / (coût unitaire A − coût unitaire B) = surcoût du moule / économie par pièce''')

# ---------------------------------------------------------------- cas industriel
R('''### Cas industriel — Le bouchon de réservoir qui coûtait trop cher''',
  '''### Cas industriel — Le réservoir qui fuyait : deux coques injectées remplacées par une pièce soufflée''')
R('''- **Exigences** : l'étanchéité est assurée par construction (une seule pièce, plus de joint) ; l'intérieur
  n'a pas besoin d'être précis.''',
  '''- **Exigences** : l'étanchéité au liquide est assurée par construction (une seule pièce, plus de joint) ;
  l'intérieur n'a pas besoin d'être précis. (Un réservoir de carburant demande en plus une couche barrière
  contre la perméation des vapeurs : c'est l'affaire du spécialiste du soufflage.)''')
R('''**Le bouchon, lui, reste injecté** : il porte un filetage et des clips précis, que le soufflage ne sait pas faire.
Pour la petite bride métallique de fixation, très découpée, l'usinage revenait cher : la quantité annuelle
dépassant le seuil de rentabilité calculé avec les devis (données de l'entreprise), elle passe en **MIM**.''',
  '''**Le bouchon, lui, reste injecté** : ce n'est pas un corps creux fermé, et son filetage intérieur et ses clips sont
des formes intérieures que le soufflage ne maîtrise pas (seule la forme extérieure l'est). Le goulot fileté du
réservoir, lui, sort du moule de soufflage. Pour le petit levier de verrouillage métallique (forme 3D complexe :
crochet, ergot, perçage oblique), l'usinage revenait cher : avec les devis (données d'énoncé : usinage 7 € la
pièce ; MIM : moule 20 000 € + 1 € la pièce), le seuil vaut 20 000 / 6 ≈ 3 300 pièces ; à 5 000 leviers par an,
il passe en **MIM**.''')

# ---------------------------------------------------------------- exercice / corrigé
R('''**5.** Pour la gâchette (question 3), deux devis : usinage à 6 € pièce sans outillage, ou MIM avec un moule de
40 000 € et 1,50 € par pièce (données d'énoncé). Calculer le seuil de rentabilité. Le MIM est-il justifié pour
50 000 pièces par an ?
""",''',
  '''**5.** Pour la gâchette (question 3), deux devis : usinage à 6 € pièce sans outillage, ou MIM avec un moule de
40 000 € et 1,50 € par pièce (données d'énoncé). Calculer le seuil de rentabilité. Le MIM est-il justifié pour
50 000 pièces par an ?

**6.** Il faut fixer une plaquette de carbure sur un corps d'outil en acier : quel assemblage, et pourquoi pas le
soudage à l'arc ?
""",''')
R('''justifié (coût total : usinage 300 000 €, MIM 40 000 + 75 000 = 115 000 € la première année).''',
  '''justifié (coût total : usinage 300 000 €, MIM 40 000 + 75 000 = 115 000 € la première année).

**6.** **Brasage fort** : deux matériaux différents, et le carbure ne doit pas fondre ; seul le métal d'apport
fond et s'infiltre par capillarité. Prévoir un jeu fin et régulier et des surfaces propres.''')

# ---------------------------------------------------------------- ateliers
R('''             "pieges": [(3333.3, "3 333 : tu as divisé par 9 au lieu de 9 − 1,50. Ce qui compte, c'est l'économie "
                                 "par pièce."),
                        (20000, "20 000 : tu as divisé par 1,50. L'outillage s'amortit grâce à la DIFFÉRENCE de coût "
                                "par pièce.")],''',
  '''             "pieges": [(3333.3, "3 333 : tu as divisé par 9 au lieu de 9 − 1,50. Ce qui compte, c'est l'économie "
                                 "par pièce."),
                        (20000, "20 000 : tu as divisé par 1,50. L'outillage s'amortit grâce à la DIFFÉRENCE de coût "
                                "par pièce."),
                        (2857.1, "2 857 : tu as additionné 9 + 1,50 ; c'est l'économie par pièce, 9 − 1,50, qui amortit "
                                 "le moule.")],''')
R('''             "pieges": [(3000, "3 000 € : tu as oublié le moule (30 000 €).")],''',
  '''             "pieges": [(3000, "3 000 € : tu as oublié le moule (30 000 €)."),
                        (18000, "18 000 €, c'est le coût de l'usinage (2 000 × 9). La question porte sur le MIM.")],''')
R('''             "pieges": [(1.363, "1,36 : tu as pris cos(2π / n) au lieu de cos(π / n) : la flèche se mesure au milieu "
                                 "de la corde, soit un demi-angle.")],''',
  '''             "pieges": [(1.363, "1,36 : tu as pris cos(2π / n) au lieu de cos(π / n) : la flèche se mesure au milieu "
                                 "de la corde, soit un demi-angle."),
                        (0.0001044, "0,0001 : calculatrice en degrés alors que π / 24 est en radians (ou calcule "
                                    "cos 7,5° en degrés).")],''')
R('''             "unite": "", "attendu": 63, "tol": 0.5,
             "consigne": "Calcule le nombre minimal de facettes : n ≥ π / arccos(1 − f / R), arrondi à l'entier "
                         "supérieur.",''',
  '''             "unite": "facettes", "attendu": 63, "tol": 0.1,
             "consigne": "Calcule le nombre minimal de facettes : n ≥ π / arccos(1 − f_max / R), arrondi à l'entier "
                         "supérieur.",''')
R('''             "pieges": [(62, "62 : on arrondit à l'entier SUPÉRIEUR, sinon la flèche dépasse la tolérance.")],''',
  '''             "pieges": [(62, "62 : on arrondit à l'entier SUPÉRIEUR, sinon la flèche dépasse la tolérance."),
                        (126, "126 : tu as pris 2π au lieu de π : la flèche se mesure au milieu de la corde.")],''')
R('''            "regle": "**f = R (1 − cos(π / n))** ; **n ≥ π / arccos(1 − f / R)**, arrondi à l'entier supérieur.",''',
  '''            "regle": "**f = R (1 − cos(π / n))** ; **n ≥ π / arccos(1 − f_max / R)**, arrondi à l'entier supérieur.",''')
R('''            "remplacement": "f(24) = 40 × (1 − cos(π / 24)) ; n ≥ π / arccos(1 − 0,05 / 40).",''',
  '''            "remplacement": "f(24) = 40 × (1 − cos(π / 24)) ; n ≥ π / arccos(1 − 0,05 / 40) (radians).",''')

# ---------------------------------------------------------------- générateurs
R('''        "enonce": (f"Une pièce peut être usinée pour **{fr(ca, 2)} € pièce** sans outillage, ou moulée avec un outillage "
                   f"de **{out} €** et **{fr(cb, 2)} € par pièce**. À partir de combien de pièces le moulage "
                   "devient-il le moins cher ?"),
        "rep": round(N, 1), "tol": 1.0, "unite": "pièces",''',
  '''        "enonce": (f"Une pièce peut être usinée pour **{fr(ca, 2)} € pièce** sans outillage, ou moulée avec un outillage "
                   f"de **{fr(out, 0)} €** et **{fr(cb, 2)} € par pièce**. Calcule le seuil de rentabilité N* (nombre "
                   "de pièces pour lequel les deux coûts totaux sont égaux)."),
        "rep": round(N, 1), "tol": 1.0, "unite": "pièces", "decimales": 1,''')
R('''            f"**Ce que dit l'énoncé.** Usinage {fr(ca, 2)} €/pièce ; moulage : outillage {out} € + {fr(cb, 2)} €/pièce.",''',
  '''            f"**Ce que dit l'énoncé.** Usinage {fr(ca, 2)} €/pièce ; moulage : outillage {fr(out, 0)} € + {fr(cb, 2)} €/pièce.",''')
R('''            f"**Le calcul.** N* = {out} / ({fr(ca, 2)} − {fr(cb, 2)}) = {fr(N, 1)} pièces.",''',
  '''            f"**Le calcul.** N* = {fr(out, 0)} / ({fr(ca, 2)} − {fr(cb, 2)}) = {fr(N, 1)} pièces.",''')
R('''            "**La règle.** f = R (1 − cos(π / n)), donc n ≥ π / arccos(1 − f / R).",''',
  '''            "**La règle.** f = R (1 − cos(π / n)), donc n ≥ π / arccos(1 − f_max / R) (radians).",''')
R('''        "indice": "n ≥ π / arccos(1 − f / R), arccos en radians, arrondi à l'entier supérieur.",''',
  '''        "indice": "n ≥ π / arccos(1 − f_max / R), arccos en radians, arrondi à l'entier supérieur.",''')

# ---------------------------------------------------------------- quiz
R('''     ["Parce qu'il donne deux faces précises", "Parce qu'il travaille les thermodurcissables",''',
  '''     ["Parce qu'il donne deux faces précises sans aucune reprise après formage", "Parce qu'il travaille les thermodurcissables",''')
R('''    ("Dans le brasage, qu'est-ce qui fond ?",
     ["Les deux pièces", "La pièce la plus fine", "Rien : c'est une colle", "Seulement le métal d'apport"], 3,
     "Le métal d'apport fond à plus basse température que les pièces et s'infiltre par capillarité ; les pièces ne "
     "fondent pas. C'est ce qui permet d'assembler des matériaux différents.", "Piège"),''',
  '''    ("Il faut fixer une plaquette de carbure sur un corps d'outil en acier. Quel assemblage choisir ?",
     ["Le soudage à l'arc", "Le soudage par ultrasons", "Le soudage par friction", "Le brasage fort"], 3,
     "Deux matériaux différents, et le carbure ne doit pas fondre : seul le métal d'apport fond et s'infiltre par "
     "capillarité. Les ultrasons visent les thermoplastiques ; la friction, des pièces de révolution.", "Piège"),''')
R('''    ("Usinage : 10 € pièce sans outillage. Moulage : outillage de 20 000 € et 2 € pièce. À partir de combien de "
     "pièces le moulage est-il le moins cher ?",''',
  '''    ("Usinage : 10 € pièce sans outillage. Moulage : outillage de 20 000 € et 2 € pièce. Quel est le seuil de "
     "rentabilité (nombre de pièces pour lequel les deux coûts totaux sont égaux) ?",''')

open(F, 'w', encoding='utf-8').write(c)
print("corrigé")
