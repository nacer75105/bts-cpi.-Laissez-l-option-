# -*- coding: utf-8 -*-
# Corrections du brouillon 6.20 après relecture (relecteur-bts-meca B1-B2 + améliorations ;
# prof-pedagogue B1-B5 + améliorations). B3 du relecteur (fiche 8.11) : retouche soumise à l'auteur.
import os
ICI = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(ICI, 'brouillon_6_20.py')
c = open(F, encoding='utf-8').read()


def R(a, b, n=1):
    global c
    assert c.count(a) == n, (a[:80], c.count(a))
    c = c.replace(a, b)


# ---------------------------------------------------------------- figures
R('''    blocs = (("ALIMENTER", "réseau, batterie", ALESAGE),''', '''    blocs = (("ALIMENTER", "réseau, centrale hydr.", ALESAGE),''')
R('''    # pertes
    for i in (3, 4):''', '''    p.append(_txt(x0, 156, "puissance qui circule", 10, ALERTE, "start", True))
    # pertes
    for i in (2, 3, 4):''')
R('''    p.append(_txt(30, 220, "Au-dessus de chaque flèche : le couple « effort × flux » qui porte la puissance à cet endroit.", 11, FIN))''',
  '''    p.append(_txt(30, 214, "Au-dessus de chaque flèche : le couple « effort × flux » qui porte la puissance à cet endroit.", 11, FIN))
    p.append(_txt(30, 228, "Chaîne hydraulique : U × I → (moteur) → C × ω → (pompe) → p × Qv → (vérin) → F × v.", 11, OK, "start", True))''')
R('''    p.append(f"<rect x='30' y='234' width='730' height='52' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 256, "Chaque bloc''', '''    p.append(f"<rect x='30' y='238' width='730' height='52' rx='6' fill='{FOND}' stroke='{FIN}'/>")
    p.append(_txt(46, 260, "Chaque bloc''')
R('''    p.append(_txt(46, 276, "Le rendement global est le produit des rendements partiels (fiche 8.2).", 12, FIN))
    return _svg("".join(p), 790, 300)''', '''    p.append(_txt(46, 280, "Le rendement global est le produit des rendements partiels (fiche 8.2).", 12, FIN))
    return _svg("".join(p), 790, 304)''')
R('''        p.append(f"<rect x='{x + 20}' y='214' width='192' height='8' rx='4' fill='{c}' opacity='0.25'>"
                 f"<animate attributeName='opacity' values='0.25;0.7;0.25' dur='2.4s' begin='{0.8 * i}s' repeatCount='indefinite'/></rect>")''',
  '''        p.append(f"<rect x='{x + 20}' y='206' width='192' height='22' rx='4' fill='{c}' opacity='0.18'>"
                 f"<animate attributeName='opacity' values='0.18;0.45;0.18' dur='2.4s' begin='{0.8 * i}s' repeatCount='indefinite'/></rect>")
        p.append(_txt(x + 116, 221, "P = effort × flux, en W", 11, c, "middle", True))''')
R('''    types = (("CONSTANT", "C = constante", "levage, convoyeur, compresseur à piston", lambda u: 0.6),
             ("LINÉAIRE", "C proportionnel à n", "frottement visqueux, calandre", lambda u: 0.75 * u),
             ("QUADRATIQUE", "C proportionnel à n²", "ventilateur, pompe centrifuge", lambda u: 0.8 * u * u),
             ("HYPERBOLIQUE", "C × n = constante", "enrouleuse, broche à puissance constante", lambda u: min(0.9, 0.18 / max(u, 0.05))))
    for i, (nom, loi, ex, f) in enumerate(types):''',
  '''    types = (("CONSTANT", "C = constante", "levage, convoyeur, compresseur à piston", lambda u: 0.6, "P ∝ n"),
             ("LINÉAIRE", "C proportionnel à n", "frottement visqueux, calandre", lambda u: 0.75 * u, "P ∝ n²"),
             ("QUADRATIQUE", "C proportionnel à n²", "ventilateur, pompe centrifuge", lambda u: 0.8 * u * u, "P ∝ n³"),
             ("HYPERBOLIQUE", "C × n = constante", "enrouleuse, broche à puissance constante", lambda u: min(0.9, 0.18 / max(u, 0.05)), "P = constante"))
    for i, (nom, loi, ex, f, pl) in enumerate(types):''')
R('''        p.append(_txt(x0 + 87, 224, loi, 11, ARBRE, "middle", True))''',
  '''        p.append(_txt(x0 + 87, 224, loi, 11, ARBRE, "middle", True))
        p.append(_txt(x0 + 87, 76, pl, 11, OK, "middle", True))''')
R('''    p.append(_txt(ox + L, oy - 8, "vitesse n (tr/min)", 10, TRAIT, "end"))''',
  '''    p.append(_txt(ox + L, oy - 8, "vitesse n (tr/min)", 10, TRAIT, "end"))
    p.append(_txt(ox + 4, oy + 30, f"zoom : l'axe commence à {int(nmin)} tr/min", 9, FIN, "start"))''')
R('''    for c_ch, col in ((lambda n: k * n * n, ARBRE), (lambda n: 20.0, OK)):
        n0 = _intersection(c_ch)
        p.append(f"<circle cx='{X(n0):.1f}' cy='{Y(c_ch(n0)):.1f}' r='6' fill='{col}'>"
                 "<animate attributeName='r' values='5;8;5' dur='1.6s' repeatCount='indefinite'/></circle>")''',
  '''    for c_ch, col, dy in ((lambda n: k * n * n, ARBRE, 22), (lambda n: 20.0, OK, -14)):
        n0 = _intersection(c_ch)
        p.append(f"<circle cx='{X(n0):.1f}' cy='{Y(c_ch(n0)):.1f}' r='6' fill='{col}'>"
                 "<animate attributeName='r' values='5;8;5' dur='1.6s' repeatCount='indefinite'/></circle>")
        p.append(_txt(X(n0) + 10, Y(c_ch(n0)) + dy, "point de fonctionnement", 9, col, "start", True))
    p.append(_txt(X(1395), Y(8), "moteur > charge : accélère →", 9, TRAIT, "middle"))
    p.append(_txt(X(1478), Y(31), "← charge > moteur", 9, TRAIT, "middle"))
    p.append(_txt(X(1478), Y(28), "ralentit", 9, TRAIT, "middle"))''')
R('''    p.append(_txt(30, 316, "Partie utile de la courbe du moteur, modélisée par une droite entre ns et le nominal ; le démarrage est traité en fiche 13.3.", 10, FIN))
    return _svg("".join(p), 790, 330)''',
  '''    p.append(_txt(30, 330, "Partie utile de la courbe du moteur, modélisée par une droite entre ns et le nominal ; le démarrage est traité en fiche 13.3.", 10, FIN))
    return _svg("".join(p), 790, 344)''')
R('''    p.append(_txt(30, 316, "Moteur (énoncé) : 4 kW, 1 440 tr/min, 4 pôles, 50 Hz. Partie utile de la courbe modélisée par une droite.", 10, FIN))
    return _svg("".join(p), 790, 330)''',
  '''    p.append(_txt(30, 330, "Moteur (énoncé) : 4 kW, 1 440 tr/min, 4 pôles, 50 Hz. Droite valable de la marche à vide à un peu au-delà du nominal.", 10, FIN))
    return _svg("".join(p), 790, 344)''')
R('''    p.append(_txt(46, 360, "IE4 depuis le 1er juillet 2023 pour les 2, 4 et 6 pôles de 75 à 200 kW.", 11, FIN))''',
  '''    p.append(_txt(46, 360, "IE4 depuis le 1er juillet 2023 pour les 2, 4 et 6 pôles de 75 à 200 kW (sauf exceptions du règlement).", 11, FIN))''')
# pompe : pertes, huile, règle
R('''    p.append(_txt(397, 128, "retour", 9, ALESAGE, "middle", True))''',
  '''    p.append(_txt(397, 128, "retour", 9, ALESAGE, "middle", True))
    p.append(_txt(397, 100, "huile", 9, FIN, "middle"))
    for xm in (280, 515):
        p.append(_k_fl(xm, 132, xm, 150, ALERTE, "kr", 1.6))
        p.append(_txt(xm, 160, "fuites (ηv), frottements (ηm) → chaleur", 9, ALERTE, "middle", True))''')
R('''    for i, (t, c, g) in enumerate((("Cylindrée Cyl : volume refoulé par tour (cm³/tr).", TRAIT, True),
                                   ("Pompe : Qv = Cyl × N × ηv  ·  C = p × Cyl / (2π × ηm)", ARBRE, True),
                                   ("Moteur hydraulique : N = Qv × ηv / Cyl  ·  C = p × Cyl × ηm / (2π)", OK, True),
                                   ("ηv (fuites internes) et ηm (frottements) : données du constructeur ou de l'énoncé ;", FIN, False),
                                   ("rendement de la pompe : η = ηv × ηm.", FIN, False))):
        p.append(_txt(x0 + 16, 170 + 22 * i, t, 12, c, "start", g))''',
  '''    for i, (t, c, g) in enumerate((("Cylindrée Cyl : volume d'huile chassé par tour (cm³/tr).", TRAIT, True),
                                   ("Sans pertes : C × ω = p × Qv, d'où Qv = Cyl × N et C = p × Cyl / (2π).", TRAIT, False),
                                   ("Les pertes jouent toujours contre toi : ce que la machine DONNE baisse (× η),", ALERTE, True),
                                   ("ce qu'elle DEMANDE augmente (÷ η). Rendement d'une machine : η = ηv × ηm.", ALERTE, True))):
        p.append(_txt(x0 + 16, 188 + 22 * i, t, 12, c, "start", g))''')
R('''"Pompe et moteur hydrauliques sont la même machine dans les deux sens : la pompe crée le débit, le moteur le reçoit."''',
  '''"Même principe (la cylindrée), en sens inverse : la pompe crée le débit, le moteur hydraulique le reçoit."''')

# ---------------------------------------------------------------- cours
R('''Le référentiel du BTS CPI le dit en ouverture du chapitre S3.1 : la consommation électrique des moteurs
représente **75 % de l'énergie consommée dans l'industrie**, et il est possible d'en économiser **30 %**
par un meilleur rendement, un dimensionnement correct et une régulation optimisée.''',
  '''Le référentiel du BTS CPI le dit en ouverture du chapitre S3.1, à propos de la motorisation électrique :
« Cette consommation électrique représente 75% de l'énergie consommée dans l'industrie. Sachant qu'il est
possible d'économiser 30% de cette énergie par l'amélioration du rendement, un dimensionnement correct
associé à des dispositifs de régulation optimisés, […] ».''')
R('''familles de moteurs et le calcul du démarrage (inertie ramenée). Cette fiche relie le tout''',
  '''familles de moteurs, le calcul du démarrage (inertie ramenée), le profil de commande et le choix du
rapport de réduction. Cette fiche relie le tout''')
R('''- **Transmettre** : adapter le mouvement à l'effecteur (réducteur, poulies, vis-écrou — fiche 6.18).

À chaque bloc, une partie de la puissance part en chaleur''',
  '''- **Transmettre** : adapter le mouvement à l'effecteur (réducteur, poulies, vis-écrou — fiche 6.18).

**Réversibilité.** Un actionneur est réversible s'il peut aussi recevoir la puissance de la charge : un
moteur électrique qui retient une charge en descente devient générateur (l'énergie est renvoyée au réseau
ou dissipée dans une résistance de freinage). Pour une transmission (vis irréversible, vis à billes), voir
la fiche 6.18.

À chaque bloc, une partie de la puissance part en chaleur''')
R('''| Hydraulique | pression p (Pa) | débit Qv (m³/s) | **P = p × Qv** |

*En alternatif triphasé, la puissance active s'écrit P = √3 × U × I × cos φ (fiche de l'électricité) : c'est
toujours un effort (U) par un flux (I), corrigé du déphasage.*

**Les unités le confirment** (équations aux dimensions)''',
  '''| Hydraulique | pression p (Pa) | débit Qv (m³/s) | **P = p × Qv** |

*En hydraulique, p est la **différence** de pression entre l'entrée et la sortie (le retour au réservoir
est pris à 0 bar relatif). Le débit est noté Qv ici, Q en fiche 8.2 : c'est la même grandeur.*

*En alternatif triphasé, la puissance électrique absorbée s'écrit P = √3 × U × I × cos φ (fiches 8.2 et
8.11 ; U : tension entre phases) : c'est toujours un effort (U) par un flux (I) ; cos φ tient compte du
fait que tension et courant n'atteignent pas leur maximum au même instant. La fiche 8.2 écrit
P = √3 U I cos φ × η pour la puissance mécanique utile : le η fait le passage.*

**Les unités le confirment** (vérification des unités)''')
R('''### 4. Énergie, travail et théorème de l'énergie cinétique

L'**énergie cinétique** est l'énergie que possède un solide parce qu'il bouge :

- en translation : **Ec = ½ × m × v²** ;
- en rotation autour d'un axe fixe : **Ec = ½ × J × ω²** (J : moment d'inertie, kg·m²).

Le **théorème de l'énergie cinétique** dit que la variation d'énergie cinétique d'un solide, entre deux
instants, est égale à la somme des travaux des efforts qui s'exercent sur lui :

> **ΔEc = Σ W** — ou, en puissance : **dEc/dt = Σ P** (puissance motrice − puissances résistantes)
''',
  '''### 4. Énergie, travail et théorème de l'énergie cinétique

*Pourquoi un moteur qui entraîne très bien sa charge une fois lancé peut-il peiner au démarrage ? Parce
qu'au démarrage, il doit en plus « remplir un réservoir » : l'énergie de mouvement des pièces. Une fois le
réservoir plein (vitesse atteinte), il ne paie plus que la charge.*

L'**énergie cinétique** est l'énergie que possède un solide parce qu'il bouge :

- en translation : **Ec = ½ × m × v²** ;
- en rotation autour d'un axe fixe : **Ec = ½ × J × ω²** (J : moment d'inertie, kg·m², noté I en fiche
  8.1).

Le **théorème de l'énergie cinétique** dit que la variation d'énergie cinétique d'un solide, entre deux
instants, est égale à la somme des travaux des efforts qui s'exercent sur lui :

> **ΔEc = Σ (travaux des efforts)**, en joules — ou, en puissance : **dEc/dt = Σ P** (la variation d'énergie
> cinétique par seconde = puissance motrice − puissances résistantes)

Chaque puissance du bilan est encore un effort × un flux : côté moteur C_m × ω, côté charge C_r × ω. Pour
un arbre entraîné, le théorème en puissance s'écrit donc **dEc/dt = (C_m − C_r) × ω**. Pour plusieurs
solides liés (moteur, réducteur, charge), on ajoute les puissances perdues dans les liaisons
(frottements) : c'est là qu'interviennent les rendements.
''')
R('''- **couple constant** — levage, convoyeur, compresseur à piston : le couple ne dépend pas de la vitesse
  (soulever une masse demande le même couple, qu'on monte vite ou lentement) ; la puissance croît avec n ;
- **couple linéaire** — frottement visqueux, calandre : C proportionnel à n ;
- **couple quadratique** — ventilateur, pompe centrifuge : C proportionnel à n² (l'air ou l'eau brassés
  résistent d'autant plus qu'on les brasse vite) ; la puissance varie comme n³ ;
- **couple hyperbolique** — enrouleuse à tension constante, broche à puissance constante : C × n =
  constante, donc la puissance est constante.''',
  '''- **couple constant** — levage, convoyeur, compresseur à piston : le couple ne dépend pas de la vitesse
  (soulever une masse demande le même couple, qu'on monte vite ou lentement). P = C × ω est un effort fixe
  multiplié par un flux qui augmente : la puissance croît comme n ;
- **couple linéaire** — C proportionnel à n. *Une cuillère dans du miel : deux fois plus vite, deux fois
  plus dur.* C'est le frottement visqueux, celui d'un fluide épais ; on le rencontre aussi sur une calandre
  (machine à rouleaux qui lamine du papier, du plastique ou du textile). P varie comme n² ;
- **couple quadratique** — ventilateur, pompe centrifuge : C proportionnel à n² (l'air ou l'eau brassés
  résistent d'autant plus qu'on les brasse vite). P = C × ω, avec C en n² et ω en n : **P varie comme n³** ;
- **couple hyperbolique** — C × n = constante. *Une enrouleuse de film plastique : le film doit défiler à
  vitesse constante et rester tendu pareil. Plus la bobine grossit, plus elle doit tourner lentement (son
  tour est plus long) et plus il faut de couple (le rayon, donc le bras de levier, augmente).* C × ω reste
  constant : la puissance ne bouge pas.''')
R('''*Conséquence importante pour un ventilateur ou une pompe centrifuge : comme la puissance varie comme n³,
réduire un peu la vitesse réduit beaucoup la puissance.''',
  '''*Conséquence importante pour un ventilateur ou une pompe centrifuge : comme la puissance varie comme n³,
réduire un peu la vitesse réduit beaucoup la puissance (à 80 % de la vitesse : 0,8³ ≈ 0,51).''')
R('''Un moteur asynchrone ne tourne pas à une vitesse fixe : sa vitesse dépend du couple qu'on lui demande.
Sa **vitesse de synchronisme** vaut **ns = 60 × f / p** (f : fréquence du réseau, p : nombre de **paires** de
pôles) ; à vide, il tourne presque à ns ; plus on le charge, plus il ralentit. Dans sa partie utile (autour
du point nominal), sa courbe couple-vitesse est presque une **droite** qui passe par (ns ; 0) et par le
point nominal (nn ; Cn).''',
  '''Un moteur asynchrone ne tourne pas à une vitesse fixe : sa vitesse dépend du couple qu'on lui demande.
Sa **vitesse de synchronisme** — celle du champ tournant — vaut **ns = 60 × f / p** (f : fréquence du
réseau, p : nombre de **paires** de pôles ; fiche 8.11). À vide, il tourne presque à ns ; plus on le
charge, plus il ralentit : pour produire un couple, le rotor doit tourner un peu moins vite que le champ,
parce que c'est ce retard qui crée les courants dans le rotor. Ce retard relatif est le **glissement**
g = (ns − n) / ns (fiche 13.3).

Dans sa partie utile, de la marche à vide jusqu'un peu au-delà du nominal, sa courbe couple-vitesse est
presque une **droite** qui passe par (ns ; 0) et par le point nominal (nn ; Cn). Cette droite ne vaut
plus près du couple maximal du moteur (couple de décrochage) : en dessous de la vitesse de ce maximum, la
courbe s'effondre et le modèle est faux.''')
R('''**Pourquoi là ?** Si le moteur tourne plus vite que ce point, la charge demande plus que ce qu'il fournit :
il ralentit. S'il tourne moins vite, il fournit plus que ce que la charge demande : il accélère. Le point
de fonctionnement est un équilibre : c'est le théorème de l'énergie cinétique avec dEc/dt = 0.''',
  '''Le moteur et la charge sont sur le même arbre : ils partagent forcément le même flux, la vitesse. Le point
de fonctionnement, c'est le flux auquel l'effort que le moteur peut donner égale l'effort que la charge
réclame.

**Pourquoi là ?** Reprenons le théorème de l'énergie cinétique : dEc/dt = (C_m − C_r) × ω.

- C_m > C_r : la différence de couple sert à accélérer, la vitesse monte.
- C_m < C_r : le moteur puise dans l'énergie cinétique, la vitesse baisse.
- C_m = C_r : Ec ne change plus, la vitesse est stable.

*Image : une voiture en côte, accélérateur bloqué. Elle accélère tant que la poussée du moteur dépasse la
résistance, ralentit si la pente durcit, et se stabilise à la vitesse où les deux se valent. Personne ne
« règle » cette vitesse : c'est l'équilibre qui la fixe.* Ce raisonnement vaut parce que, dans la partie
utile, le couple du moteur baisse plus vite avec n que le couple de la charge : le point est stable.''')
R('''*Exemple (plaque d'énoncé) : moteur 4 kW, 1 440 tr/min, 4 pôles (p = 2), 50 Hz → ns = 60 × 50 / 2 =
1 500 tr/min ; Cn = 4 000 / (2π × 1 440 / 60) ≈ **26,5 N·m**. Entre ns et le nominal :
C moteur(n) = 26,5 × (1 500 − n) / 60.*

- *Convoyeur, couple constant de 20 N·m (ramené à l'arbre moteur) : 26,5 × (1 500 − n) / 60 = 20 → n ≈
  **1 455 tr/min**, P ≈ 20 × 152,3 ≈ **3 050 W**.*
- *Ventilateur, couple quadratique valant 18 N·m à 1 450 tr/min : l'équation est du second degré ; sa
  solution est n ≈ **1 459 tr/min**, C ≈ 18,2 N·m, P ≈ **2 780 W**.*''',
  '''*Exemple (plaque d'énoncé) : moteur 4 kW, 1 440 tr/min, 4 pôles (p = 2), 50 Hz → ns = 60 × 50 / 2 =
1 500 tr/min ; glissement nominal g = (1 500 − 1 440) / 1 500 = 4 % ; Cn = 4 000 / (2π × 1 440 / 60) ≈
**26,5 N·m**. La droite du moteur :*

> *C moteur(n) = 26,5 × (1 500 − n) / (1 500 − 1 440), où le dénominateur 1 500 − 1 440 = 60 tr/min est
> l'écart ns − nn — pas une conversion de tr/min en rad/s. Vérification : n = 1 500 donne C = 0 (à vide) ;
> n = 1 440 donne C = 26,5 (nominal).*

- *Convoyeur, couple constant de 20 N·m (ramené à l'arbre moteur) : 26,5 × (1 500 − n) / (1 500 − 1 440) =
  20 → n ≈ **1 455 tr/min** ; ω = 2π × 1 455 / 60 ≈ 152,3 rad/s ; P ≈ 20 × 152,3 ≈ **3 050 W**.*
- *Ventilateur, couple quadratique valant 18 N·m à 1 450 tr/min : 26,5 × (1 500 − n) / (1 500 − 1 440) =
  18 × (n / 1 450)². C'est une équation du second degré, qu'on résout à la calculatrice — ou qu'on lit sur la
  figure à curseurs ci-dessous : n ≈ **1 459 tr/min**, C ≈ 18,2 N·m, P ≈ **2 780 W**.*''')
R('''**Le point de conception.** Le point de fonctionnement doit tomber **sous** le couple nominal (en régime
permanent) : au-delà, le moteur fournit plus que ce pour quoi il est construit et chauffe au-delà de sa
classe d'isolation. Trop loin en dessous, il est surdimensionné : plus cher et souvent moins efficace.''',
  '''**Le point de conception.** En régime permanent, le couple au point de fonctionnement doit être **plus
faible que Cn** — donc la vitesse un peu plus élevée que nn : à droite du point nominal sur le graphe.
Au-delà, le moteur fournit plus que ce pour quoi il est construit et chauffe au-delà de sa classe
d'isolation (la classe thermique des isolants du bobinage, qui fixe l'échauffement admissible).

**Choisir le moteur, en quatre questions.**

1. **Quel couple la charge demande-t-elle, ramené à l'arbre, vers la vitesse prévue ?** Lire sa famille
   (§5) et sa valeur.
2. **Je prends dans le catalogue le premier moteur dont Cn dépasse ce couple**, puis je calcule (ou je
   trace) le point de fonctionnement.
3. **Couple au point plus grand que Cn ?** Le moteur chaufferait en continu : je passe à la taille
   au-dessus et je recommence.
4. **Le démarrage passe-t-il ?** Énergie cinétique à fournir (§4), méthode complète en fiche 13.3.

*Pourquoi pas « beaucoup plus gros, pour être tranquille » ? Un moteur a des pertes presque fixes : il faut
aimanter le fer et faire tourner son ventilateur, quelle que soit la charge. Peu chargé, il paie ces pertes
pour peu de puissance utile, et son rendement baisse — comme un bus qui roule avec deux passagers consomme
presque autant que plein.*''')
R('''La norme **IEC 60034-30-1** classe les moteurs asynchrones selon leur rendement minimal à pleine charge :''',
  '''La norme **IEC 60034-30-1** classe les moteurs à courant alternatif alimentés directement par le réseau
(des asynchrones pour l'essentiel) selon leur rendement minimal à pleine charge :''')
R('''IE3 ≥ 91,4 %, IE4 ≥ 93,3 %.

*Ce que ça représente : à pleine charge, un IE1 de 11 kW absorbe au moins 11 000 / 0,876 ≈ 12 557 W, un IE3
11 000 / 0,914 ≈ 12 035 W. Sur 4 000 h de fonctionnement par an (donnée d'énoncé), la différence vaut
(12 557 − 12 035) × 4 000 ≈ **2 090 kWh par an**, pour un seul moteur.*''',
  '''IE3 ≥ 91,4 %, IE4 ≥ 93,3 %.

Le rendement d'un moteur compare encore deux produits effort × flux : η = (C × ω) / (√3 × U × I × cos φ).
Le moteur reçoit de la tension et du courant, et rend du couple et de la vitesse ; ce qui manque est devenu
chaleur.

*Ce que ça représente : à pleine charge, un IE1 de 11 kW absorbe **au plus** 11 000 / 0,876 ≈ 12 557 W, un
IE3 **au plus** 11 000 / 0,914 ≈ 12 035 W. En comparant ces deux seuils sur 4 000 h de fonctionnement par
an (donnée d'énoncé) : (12,557 − 12,035) kW × 4 000 h ≈ **2 090 kWh par an** d'écart estimé, pour un seul
moteur.*''')
R('''le 1er juillet 2023, les moteurs 2, 4 et 6 pôles de 75 à 200 kW doivent être **IE4**. Un concepteur ne
« choisit » donc plus un IE1 : il choisit entre IE3 et mieux, et il dimensionne juste, parce qu'un moteur
très peu chargé travaille loin de son rendement de plaque.''',
  '''le 1er juillet 2023, les moteurs 2, 4 et 6 pôles de 75 à 200 kW doivent être **IE4** (sauf exceptions
prévues par le règlement). Un concepteur ne « choisit » donc plus un IE1 : il choisit entre IE3 et mieux,
et il dimensionne juste, parce qu'un moteur très peu chargé travaille loin de son rendement de plaque
(l'image du bus, §6).''')
R('''Une **pompe hydraulique volumétrique** convertit la puissance mécanique du moteur qui l'entraîne (C × ω) en
puissance hydraulique (p × Qv). Un **moteur hydraulique** fait l'inverse. Les deux se caractérisent par
leur **cylindrée** Cyl : le volume d'huile déplacé par tour.

- **Débit d'une pompe** : **Qv = Cyl × N × ηv** (ηv : rendement volumétrique, dû aux fuites internes).
- **Couple absorbé par la pompe** : **C = p × Cyl / (2π × ηm)** (ηm : rendement mécanique).
- Rendement de la pompe : **η = ηv × ηm**.
- **Moteur hydraulique** : N = Qv × ηv / Cyl et C = p × Cyl × ηm / (2π).

*Exemple (données d'énoncé) : pompe de 16 cm³/tr entraînée à 1 450 tr/min, ηv = 0,95, ηm = 0,90, sous
150 bar. Qv = 16 × 1 450 × 0,95 = 22 040 cm³/min ≈ **22,0 L/min**. P hydraulique = 150 × 10⁵ × 22,04 × 10⁻³ / 60
≈ **5 510 W**. Couple absorbé : 150 × 10⁵ × 16 × 10⁻⁶ / (2π × 0,90) ≈ 42,4 N·m, soit une puissance
mécanique de 42,4 × 151,8 ≈ **6 440 W**. Rendement : 5 510 / 6 440 ≈ 0,855 = 0,95 × 0,90 ✔.*''',
  '''Une **pompe hydraulique volumétrique** convertit la puissance mécanique du moteur qui l'entraîne (C × ω) en
puissance hydraulique (p × Qv). Un **moteur hydraulique** fait l'inverse : même principe, en sens inverse
(certaines machines sont réversibles, mais une pompe ne s'utilise pas forcément en moteur).

**D'abord la machine idéale, sans pertes.** *Une pompe volumétrique, c'est une pompe à vélo qu'on
actionnerait en tournant : à chaque tour, elle chasse toujours le même volume d'huile, la **cylindrée**
Cyl (par exemple 16 cm³/tr).* À N tours par minute, elle débite donc **Qv = Cyl × N**. Et puisque, sans
pertes, effort × flux se conserve : C × ω = p × Qv, avec ω = 2π × N (N en tr/s) et Qv = Cyl × N, d'où
C × 2π × N = p × Cyl × N : le N se simplifie, **C = p × Cyl / (2π)** (p en Pa, Cyl en m³/tr).

**Ensuite les pertes. Une seule règle : elles jouent toujours contre toi.**

- **ηv, rendement volumétrique** : les fuites internes — la pompe à vélo dont le joint fuit.
- **ηm, rendement hydromécanique** : les frottements et pertes internes — une partie du couple sert à les
  vaincre.

| | Pompe (reçoit C × ω, donne p × Qv) | Moteur hydraulique (reçoit p × Qv, donne C × ω) |
|---|---|---|
| ηv | elle **donne** moins de débit : Qv = Cyl × N **× ηv** | une partie du débit fuit sans le faire tourner : N = Qv **× ηv** / Cyl |
| ηm | elle **demande** plus de couple : C = p × Cyl / (2π) **÷ ηm** | il **donne** moins de couple : C = p × Cyl / (2π) **× ηm** |

*Pour vérifier : ce que la machine donne baisse (× η) ; ce qu'elle demande augmente (÷ η). Rendement d'une
machine : η = ηv × ηm.*

*Exemple (données d'énoncé) : pompe de 16 cm³/tr entraînée à 1 450 tr/min, ηv = 0,95, ηm = 0,90, sous
150 bar. Qv = 16 × 1 450 × 0,95 = 22 040 cm³/min ≈ **22,0 L/min**. P hydraulique = p × Qv = 150 × 10⁵ ×
22,04 × 10⁻³ / 60 ≈ **5 510 W**. Couple absorbé : 150 × 10⁵ × 16 × 10⁻⁶ / (2π × 0,90) ≈ 42,4 N·m ; avec
ω = 2π × 1 450 / 60 ≈ 151,8 rad/s, la puissance mécanique vaut C × ω ≈ 42,4 × 151,8 ≈ **6 440 W**.
Rendement : 5 510 / 6 440 ≈ 0,855 = 0,95 × 0,90 ✔ — effort × flux d'un côté, effort × flux de l'autre.*''')
R('''3. **Prendre ns pour la vitesse du moteur** : un asynchrone tourne sous ns, d'autant plus bas qu'il est
   chargé.''', '''3. **Prendre ns pour la vitesse du moteur** : un asynchrone tourne sous ns, d'autant plus bas qu'il est
   chargé.
4. **Lire le 60 de la droite du moteur comme une conversion** : dans C = Cn × (ns − n) / (ns − nn), il vaut
   ns − nn.''')
R('''4. **Confondre p (paires de pôles) et le nombre de pôles**''', '''5. **Confondre p (paires de pôles) et le nombre de pôles**''')
R('''5. **Choisir le moteur sur la seule puissance''', '''6. **Choisir le moteur sur la seule puissance''')
R('''6. **Croire que le rendement de plaque vaut à toutes les charges** : la classe IE est définie à pleine
   charge.
7. **Additionner les rendements**''', '''7. **Croire que le rendement de plaque vaut à toutes les charges** : la classe IE est définie à pleine
   charge.
8. **Additionner les rendements**''')
R('''- **TEC** : ΔEc = Σ W ; Ec = ½ m v² (translation), ½ J ω² (rotation). Le démarrage coûte de l'énergie.''',
  '''- **TEC** : ΔEc = Σ travaux ; en puissance, dEc/dt = (C_m − C_r) × ω ; Ec = ½ m v², ½ J ω². Le démarrage
  coûte de l'énergie.''')
R('''- **Point de fonctionnement** = intersection moteur / charge ; il doit rester sous le nominal.
  ns = 60 f / p.''', '''- **Point de fonctionnement** = intersection moteur / charge ; couple au point plus faible que Cn, sinon
  moteur plus gros. ns = 60 f / p ; le moteur tourne sous ns (glissement).''')
R('''- Pompe : **Qv = Cyl × N × ηv**, η = ηv × ηm ; le moteur hydraulique fait l'inverse.''',
  '''- Pompe : **Qv = Cyl × N × ηv**, η = ηv × ηm ; le moteur hydraulique fait l'inverse. Les pertes : ce que
  la machine donne × η, ce qu'elle demande ÷ η.''')
R('''**Énergie cinétique** — translation : Ec = ½ m v² · rotation : Ec = ½ J ω² · **TEC : ΔEc = Σ W**''',
  '''**Énergie cinétique** — translation : Ec = ½ m v² · rotation : Ec = ½ J ω² · **TEC : ΔEc = Σ travaux** ·
en puissance : dEc/dt = (C_m − C_r) × ω''')
R('''**Vitesse de synchronisme** — ns = 60 f / p (p : paires de pôles)''',
  '''**Vitesse de synchronisme** — ns = 60 f / p (p : paires de pôles) · glissement g = (ns − n) / ns''')

# ---------------------------------------------------------------- cas industriel
R('''- **Convertir** : à pleine charge, un IE1 de 11 kW 4 pôles a un rendement d'au moins 87,6 % ; un IE3, d'au
  moins 91,4 % (IEC 60034-30-1). Remplacer le moteur fait passer la puissance absorbée de 12 557 W à
  12 035 W environ : environ 520 W d'économie, à vitesse égale.
- **Distribuer** : le volet freine l'air, mais le ventilateur tourne toujours à la même vitesse. Or la
  charge est **quadratique** : son couple varie comme n², sa puissance comme n³. Avec un variateur, on
  règle le débit en baissant la vitesse au lieu de fermer le volet.

**Le calcul qui convainc.** Un débit réduit à 80 % s'obtient, pour un ventilateur, avec 80 % de la
vitesse ; la puissance demandée par le ventilateur devient alors 0,8³ ≈ **0,51** fois la puissance à
pleine vitesse (loi de similitude des ventilateurs, conséquence du couple quadratique) : près de la moitié.''',
  '''- **Convertir** : à pleine charge (on suppose ici le moteur à pleine charge, donnée d'énoncé), un IE1 de
  11 kW 4 pôles a un rendement d'au moins 87,6 % ; un IE3, d'au moins 91,4 % (IEC 60034-30-1). Remplacer le
  moteur fait passer la puissance absorbée **maximale** de 12 557 W à 12 035 W : environ 520 W d'économie
  estimée, à vitesse égale.
- **Distribuer et réguler** : aujourd'hui, on règle le débit par un volet, une perte volontaire dans le
  circuit d'air ; le ventilateur tourne toujours à la même vitesse. Côté air, la puissance est encore un
  effort × un flux : P = Δp × Qv. Le volet crée une chute de pression, et la puissance correspondante est
  brûlée dans le volet, pour rien — comme rouler pied au plancher en tenant sa vitesse avec le frein. Un
  variateur, placé dans le bloc Distribuer, règle plutôt la vitesse.

**Le calcul qui convainc.** Chaque tour de roue du ventilateur pousse à peu près le même volume d'air : sur
un réseau d'air inchangé (volet ouvert en grand, pas de pression statique à vaincre), les **lois de
similitude** des ventilateurs donnent débit ∝ n, pression ∝ n², puissance ∝ n³. Un débit de 80 % s'obtient
donc à 80 % de la vitesse, et la puissance tombe à 0,8³ ≈ **0,51** fois celle à pleine vitesse. Avec le
volet, la puissance baisse aussi un peu, mais beaucoup moins : l'écart entre les deux réglages est le gain
du variateur.''')

# ---------------------------------------------------------------- exercice / corrigé / méthode
R('''0,2 kg·m² (donnée d'énoncé). Quelle énergie cinétique faut-il leur donner pour atteindre la vitesse de
fonctionnement ?''', '''0,2 kg·m² (donnée d'énoncé ; inertie du rotor du moteur négligée). Quelle énergie cinétique faut-il leur
donner pour atteindre la vitesse de fonctionnement ?''')
R('''ns = 60 × 50 / 2. Cn = 4 000 / (2π × 1 440 / 60). Cn × (1 500 − n) / 60 = 22.''',
  '''ns = 60 × 50 / 2. Cn = 4 000 / (2π × 1 440 / 60). Cn × (1 500 − n) / (1 500 − 1 440) = 22.''')
R('''**2.** 26,53 × (1 500 − n) / 60 = 22 → 1 500 − n = 22 × 60 / 26,53 ≈ 49,8 → n ≈ **1 450 tr/min**.''',
  '''**2.** 26,53 × (1 500 − n) / (1 500 − 1 440) = 22 → 1 500 − n = 22 × 60 / 26,53 ≈ 49,8 (le 60 est
ns − nn) → n ≈ **1 450 tr/min**.''')
R('''**4.** P absorbée ≤ 4 000 / 0,886 ≈ **4 515 W** à la charge nominale.''',
  '''**4.** P absorbée ≤ 4 000 / 0,886 ≈ **4 515 W** à la charge nominale. La classe IE ne garantit le
rendement qu'à pleine charge : au point de fonctionnement (3 340 W), on ne pourrait que l'estimer — c'est
pour cela que la question porte sur le point nominal.''')
R('''    "**Écrire la droite du moteur** dans sa partie utile : C(n) = Cn × (ns − n) / (ns − nn).",''',
  '''    "**Écrire la droite du moteur** dans sa partie utile : C(n) = Cn × (ns − n) / (ns − nn) (le dénominateur "
    "est l'écart ns − nn, pas une conversion).",''')
R('''    "**Conclure** : vitesse, couple, puissance au point ; vérifier que le couple reste sous Cn.",
], "Moteur 4 kW, 1 440 tr/min, 4 pôles, 50 Hz : ns = 1 500 tr/min, Cn ≈ 26,5 N·m. Charge constante "
   "22 N·m : 26,5 × (1 500 − n) / 60 = 22 → n ≈ 1 450 tr/min, P ≈ 3 340 W, sous le nominal.")''',
  '''    "**Conclure** : vitesse, couple, puissance au point. Si le couple dépasse Cn : moteur de taille "
    "supérieure, puis recalculer ; vérifier ensuite le démarrage (fiche 13.3).",
], "Moteur 4 kW, 1 440 tr/min, 4 pôles, 50 Hz : ns = 1 500 tr/min, Cn ≈ 26,5 N·m. Charge constante "
   "22 N·m : 26,5 × (1 500 − n) / (1 500 − 1 440) = 22 → n ≈ 1 450 tr/min, P ≈ 3 340 W, sous le nominal.")''')

# ---------------------------------------------------------------- ateliers
R('''"ramené à l'arbre moteur, un couple constant de 22 N·m. Partie utile de la courbe du moteur : "
                  "droite passant par (ns ; 0) et (1 440 ; Cn).",''',
  '''"ramené à l'arbre moteur, un couple constant de 22 N·m. Partie utile de la courbe du moteur : "
                  "droite passant par (ns ; 0) et (1 440 ; Cn), soit C(n) = Cn × (ns − n) / (ns − 1 440).",''')
R('''             "consigne": "Résous Cn × (1 500 − n) / 60 = 22.",''', '''             "consigne": "Résous Cn × (1 500 − n) / (1 500 − 1 440) = 22.",''')
R('''"remplacement": "ns = 60 × 50 / 2 ; Cn = 4 000 / (2π × 1 440 / 60) ; 26,53 × (1 500 − n) / 60 = 22.",''',
  '''"remplacement": "ns = 60 × 50 / 2 ; Cn = 4 000 / (2π × 1 440 / 60) ; 26,53 × (1 500 − n) / (1 500 − 1 440) = 22.",''')
R('''            ("Rendement mécanique ηm",
             "la part du couple qui n'est pas perdue en frottements."),''',
  '''            ("Rendement hydromécanique ηm",
             "la part du couple qui n'est pas perdue en frottements et pertes internes. Règle : ce que la "
             "machine donne × η, ce qu'elle demande ÷ η."),''')
R('''             "pieges": [(440.8, "440,8 : tu as oublié le rendement volumétrique du moteur : une partie du débit "
                                "fuit sans le faire tourner.")],''',
  '''             "pieges": [(440.8, "440,8 : tu as oublié un des deux rendements volumétriques (celui de la pompe ou "
                                "celui du moteur) : il faut 16 × 1 450 × 0,95 × 0,95 / 50.")],''')
R('''             "aide": "15 × 10⁶ × 3,673 × 10⁻⁴ ≈ 5 510 W."},''',
  '''             "aide": "15 × 10⁶ × 3,673 × 10⁻⁴ ≈ 5 510 W."},
            {"type": "numerique", "label": "Couple absorbé par la pompe",
             "unite": "N·m", "attendu": 42.44, "tol": 0.2,
             "consigne": "Calcule le couple que le moteur électrique doit fournir à la pompe : C = p × Cyl / (2π × ηm).",
             "indice": "La pompe DEMANDE du couple : les frottements l'augmentent, on divise par ηm.",
             "pieges": [(34.38, "34,4 : tu as multiplié par ηm. La pompe REÇOIT le couple : les frottements en "
                                "demandent plus, on divise."),
                        (38.2, "38,2, c'est le couple de la pompe idéale, sans frottements.")],
             "aide": "15 × 10⁶ × 16 × 10⁻⁶ / (2π × 0,90) ≈ 42,4 N·m ; × 151,8 rad/s ≈ 6 440 W absorbés."},''')
R('''             "question": "La puissance de sortie vaut environ 4 710 W pour 6 440 W absorbés par la pompe. Que "
                         "devient la différence ?",''',
  '''             "question": "La puissance de sortie vaut environ 4 710 W (107,4 N·m × 43,85 rad/s), pour 6 440 W "
                         "absorbés par la pompe (42,4 N·m × 151,8 rad/s). Que devient la différence ?",''')
R('''"calcul": "**Qv ≈ 22,0 L/min** ; **P hydraulique ≈ 5 510 W** ; **N ≈ 419 tr/min** ; **C ≈ 107,4 N·m** ; "
                     "P sortie ≈ 107,4 × 43,85 ≈ 4 710 W.",''',
  '''"calcul": "**Qv ≈ 22,0 L/min** ; **P hydraulique ≈ 5 510 W** ; **C pompe ≈ 42,4 N·m** (6 440 W absorbés) ; "
                     "**N ≈ 419 tr/min** ; **C ≈ 107,4 N·m** ; P sortie ≈ 107,4 × 43,85 ≈ 4 710 W.",''')
R('''"regle": "**Pompe : Qv = Cyl × N × ηv** ; **P = p × Qv** ; **moteur : N = Qv ηv / Cyl** ; "
                    "**C = p Cyl ηm / (2π)**.",''',
  '''"regle": "**Pompe : Qv = Cyl × N × ηv**, **C = p Cyl / (2π ηm)** ; **P = p × Qv** ; **moteur : N = Qv ηv / "
                    "Cyl**, **C = p Cyl ηm / (2π)** — ce que la machine donne × η, ce qu'elle demande ÷ η.",''')

# générateur : tolérance
R('''        "rep": round(Q, 3), "tol": 0.05, "unite": "L/min",''', '''        "rep": round(Q, 3), "tol": 0.1, "unite": "L/min",''')
R('''        if abs(val - Q) > 0.05 and all(abs(val - d["v"]) > 0.05 for d in diag):''',
  '''        if abs(val - Q) > 0.12 and all(abs(val - d["v"]) > 0.05 for d in diag):''')

open(F, 'w', encoding='utf-8').write(c)
print("corrigé")
