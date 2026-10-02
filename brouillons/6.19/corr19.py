import os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'brouillon_6_19.py')
s = open(p, encoding='utf-8').read()


def R(a, b):
    global s
    assert s.count(a) == 1, (a[:90], s.count(a))
    s = s.replace(a, b)


# ---------------- figures
# rotule : vue en coupe, l'arbre et la bague intérieure s'inclinent (rotulage) ; embout : la tige pivote
a0 = s.index("    # roulement à rotule : bague extérieure sphérique, bague intérieure qui s'incline")
a1 = s.index("    p.append(_txt(205, 268, \"Usage : arbres longs, bâtis soudés, vérins articulés.\", 10, TRAIT, \"middle\"))")
s = s[:a0] + '''    # roulement à rotule, vu en coupe : la piste extérieure est un arc de sphère, l'arbre et la bague
    # intérieure s'inclinent dedans (rotulage)
    cx, cy = 120, 150
    p.append(f"<path d='M {cx - 34} {cy - 70} A 70 70 0 0 1 {cx + 34} {cy - 70}' fill='none' stroke='{TRAIT}' stroke-width='8'/>")
    p.append(f"<path d='M {cx - 34} {cy + 70} A 70 70 0 0 0 {cx + 34} {cy + 70}' fill='none' stroke='{TRAIT}' stroke-width='8'/>")
    p.append(f"<g><rect x='{cx - 80}' y='{cy - 10}' width='160' height='20' fill='#e2e8f0' stroke='{TRAIT}' stroke-width='1.6'/>"
             f"<rect x='{cx - 26}' y='{cy - 40}' width='52' height='30' fill='#cbd5e1' stroke='{TRAIT}'/>"
             f"<rect x='{cx - 26}' y='{cy + 10}' width='52' height='30' fill='#cbd5e1' stroke='{TRAIT}'/>"
             + "".join(f"<circle cx='{cx + dx}' cy='{cy + dy}' r='9' fill='#ffffff' stroke='{ALESAGE}' stroke-width='2'/>"
                       for dx in (-13, 13) for dy in (-52, 52))
             + f"<animateTransform attributeName='transform' type='rotate' values='0 {cx} {cy}; -6 {cx} {cy}; 6 {cx} {cy}; 0 {cx} {cy}' dur='3s' repeatCount='indefinite'/></g>")
    p.append(_txt(cx, 238, "roulement à rotule (coupe)", 11, ALESAGE, "middle", True))
    p.append(_txt(cx, 254, "l'arbre s'incline : la piste extérieure est sphérique", 9, FIN, "middle"))
    # embout à rotule : la sphère reste dans son logement, la tige pivote autour
    ex, ey = 290, 150
    p.append(f"<g><rect x='{ex - 6}' y='{ey + 26}' width='12' height='70' fill='#cbd5e1' stroke='{TRAIT}'/>"
             f"<circle cx='{ex}' cy='{ey}' r='30' fill='none' stroke='{TRAIT}' stroke-width='5'/>"
             f"<animateTransform attributeName='transform' type='rotate' values='0 {ex} {ey}; 12 {ex} {ey}; -12 {ex} {ey}; 0 {ex} {ey}' dur='3s' repeatCount='indefinite'/></g>")
    p.append(f"<circle cx='{ex}' cy='{ey}' r='20' fill='#fde68a' stroke='{ARBRE}' stroke-width='2'/>")
    p.append(_txt(ex, 92, "embout à rotule", 11, ALESAGE, "middle", True))
    p.append(_txt(ex, 106, "(bout de tige de vérin)", 10, FIN, "middle"))
''' + s[a1:]
R('''    p.append(_txt(46, 292, "Contact linéique des rouleaux : C plus de deux fois plus grand, et exposant 10/3 au lieu de 3.", 12, TRAIT, "start", True))''',
  '''    p.append(_txt(46, 292, "Contact sur une ligne (rouleaux) au lieu d'un point (billes) : C plus de deux fois plus grand, exposant 10/3.", 12, TRAIT, "start", True))''')
# précharge : le couple devient Cs
R('''    p.append(_txt(120, 62, "couple C", 11, OK, "end", True))''', '''    p.append(_txt(120, 62, "couple Cs", 11, OK, "end", True))''')
R('''                                   ("Ordre de grandeur : C ≈ 0,2 × d × F0", True, OK),''',
  '''                                   ("Ordre de grandeur : Cs ≈ 0,2 × d × F0", True, OK),''')
R('''    p.append(_txt(46, 298, "Contrôle : σ = F0 / As doit rester sous Re (classe de la vis) ; As = section résistante (ISO 898-1).", 12, TRAIT))''',
  '''    p.append(_txt(46, 298, "Contrôle : σ = F0 / As sous Re, avec une marge (la torsion de serrage s'ajoute) ; As : ISO 898-1.", 12, TRAIT))''')
# figure à curseurs
R('''              (f"L10 = (C/P)^n = {_fr_court(L10, 1)} Mtr", TRAIT, False),''',
  '''              (f"L10 = (C/P)^n = {_fr_court(L10, 1)} millions de tours", TRAIT, False),''')
R('''    p.append(_txt(x0, y0 + 72, "(échelle logarithmique)", 9, FIN))''',
  '''    p.append(_txt(x0, y0 + 72, "(échelle logarithmique : chaque graduation vaut 10 fois la précédente)", 9, FIN))''')

# ---------------- cours
R('''Les fiches 6.4 et 6.5 apprennent à **choisir le type** de roulement et à le monter. Il reste la question''',
  '''Les fiches 6.4 à 6.6 apprennent à **choisir le type** de roulement et à le monter. Il reste la question''')
R('''**à quel couple serrer** pour obtenir la précharge voulue ? Ce sont les deux calculs de pré-dimensionnement
de cette fiche, avec des valeurs lues dans des **catalogues de fabricants**.''',
  '''**à quel couple serrer** pour obtenir la précharge voulue ? Ce sont les deux calculs de **pré-dimensionnement**
de cette fiche (un premier calcul rapide, pour choisir une taille avant les vérifications détaillées),
avec des valeurs lues dans des **catalogues de fabricants**.''')
R('''Un roulement bien choisi, bien monté et bien lubrifié ne s'use pas : il finit par la **fatigue**. À force
de passages des billes, la piste s'écaille. Mais cent roulements identiques, sous la même charge, ne
lâchent pas tous au même moment. On définit donc :''',
  '''Un roulement bien choisi, bien monté et bien lubrifié ne meurt pas d'usure : il finit par la **fatigue**.
Comme un fil de fer qu'on plie et déplie jusqu'à ce qu'il casse : à chaque passage d'une bille, le métal
de la piste est écrasé puis relâché. Après des centaines de millions de passages, une petite fissure
apparaît, puis un éclat de métal se détache — l'**écaillage** : le roulement devient bruyant et vibre.
Mais cent roulements identiques, sous la même charge, ne lâchent pas tous au même moment. On définit donc :''')
R('''- **L10** : la durée (en **millions de tours**) atteinte ou dépassée par **90 %** des roulements d'un lot.
  C'est une fiabilité de 90 %, pas une durée « garantie » ;
- **C, la charge dynamique de base** : la charge pour laquelle L10 vaut exactement **1 million de tours**.
  C'est une caractéristique du roulement, **donnée par le catalogue du fabricant** ;''',
  '''- **L10** : la durée (en **millions de tours**) atteinte ou dépassée par **90 %** des roulements d'un lot.
  C'est une fiabilité de 90 %, pas une durée « garantie ». Pourquoi pas la moyenne ? Planifier la
  maintenance à la durée moyenne, ce serait accepter qu'environ la moitié des machines tombent en panne
  avant ; à L10, seulement 1 roulement sur 10 a lâché ;
- **C, la charge dynamique de base** : la charge radiale constante, de direction fixe, pour laquelle L10
  vaut exactement **1 million de tours** (norme ISO 281). C'est une caractéristique du roulement, **donnée
  par le catalogue du fabricant**. Attention, ce n'est **pas** une charge de service : 1 million de tours, à
  1 500 tr/min, c'est 1 000 000 / 1 500 ≈ 667 minutes, à peine 11 heures. C est une **charge de
  référence**, qui sert à comparer les roulements ; en service, P est bien plus petite que C ;''')
R('''**La charge équivalente P.** Si le roulement ne porte qu'un effort radial Fr, **P = Fr**. S'il porte aussi
un effort axial Fa : **P = X × Fr + Y × Fa**, où les coefficients X et Y dépendent du type de roulement et
du rapport des charges ; ils sont **donnés par le catalogue** (ou par l'énoncé), on ne les invente pas.''',
  '''**La charge équivalente P.** *Radial* : perpendiculaire à l'arbre, comme la tension d'une courroie qui tire
sur la poulie. *Axial* : le long de l'arbre, comme la poussée d'un pignon à denture hélicoïdale. Si le
roulement ne porte qu'un effort radial Fr, **P = Fr**. S'il porte aussi un effort axial Fa, on le remplace,
pour le calcul, par une seule charge radiale fictive qui le fatiguerait autant : **P = X × Fr + Y × Fa**.
Les coefficients X et Y dépendent du type de roulement et du rapport des charges ; ils sont **donnés par le
catalogue** (ou par l'énoncé), on ne les invente pas.''')
R('''**Pourquoi deux exposants ?** Une bille touche sa piste en un **point**, un rouleau sur une **ligne** : la
pression de contact ne réagit pas de la même façon à la charge. L'exposant traduit ce comportement ; il est
fixé par la norme de calcul utilisée par les fabricants.''',
  '''**D'où vient cette formule ? Vérifions-la sur la définition de C.** Si P = C, alors C/P = 1 et L10 = 1ⁿ =
1 million de tours : c'est la définition de C. Si on charge deux fois moins (P = C/2), C/P = 2 et, pour des
billes, L10 = 2³ = 8 millions de tours. Diviser la charge par 2 ne double pas la vie : cela la multiplie
par 8. L'effet est **beaucoup plus que proportionnel**, à cause de l'exposant.

**Pourquoi deux exposants ?** Une bille appuie sur sa piste comme un pointeau sur une tôle : toute la charge
passe par **un point**. Un rouleau appuie comme un rouleau de laminoir : la charge est **étalée sur une
ligne**. Les deux contacts ne réagissent pas de la même façon quand on charge plus ; les fabricants l'ont
mesuré par des essais d'endurance, et la norme ISO 281 résume ces essais par l'exposant. On ne le démontre
pas en BTS. On retient : **bille = point = 3 ; rouleau = ligne = 10/3**.''')
R('''**La conversion en heures, pas à pas** : L10 est en millions de tours, donc L10 × 10⁶ tours. À N tours par
minute, cela fait L10 × 10⁶ / N minutes, soit **L10 × 10⁶ / (60 N) heures**.''',
  '''**La conversion en heures, pas à pas** : L10 est en millions de tours, donc L10 × 10⁶ tours. Combien de
tours le roulement fait-il en une heure ? N tours par minute × 60 minutes = **60 N tours par heure** (à
1 500 tr/min : 90 000). Le nombre d'heures, c'est le total de tours divisé par les tours faits en une heure :
**L10h = L10 × 10⁶ / (60 N)**. Si l'on oublie le 60, on obtient des **minutes** : un résultat 60 fois trop
grand.''')
R('''  ≈ 10 900 millions de tours ; L10h ≈ **120 800 h**.''',
  '''  ≈ 10 900 millions de tours ; L10h ≈ **120 800 h**.

*Valeurs lues sur les fiches produit SKF (skf.com) : elles peuvent changer d'une édition du catalogue à
l'autre, et d'un fabricant à l'autre. **À la calculatrice**, tapez 16,25 ^ ( 10 ÷ 3 ) : les **parenthèses
autour de 10 ÷ 3 sont obligatoires** — sans elles, la calculatrice élève à la puissance 10 puis divise par 3.*''')
R('''On part de la **durée visée** (donnée par le cahier des charges, ou par les tableaux des catalogues selon
le type de machine) et on retourne la formule :''',
  '''On part de la **durée visée** (donnée par le cahier des charges, ou par les tableaux des catalogues selon
le type de machine) et on retourne la formule, en trois étapes : (C/P)ⁿ = L10 ; on « défait » la
puissance n en prenant la puissance 1/n des deux côtés, C/P = L10^(1/n) (pour n = 3, c'est la **racine
cubique**) ; on multiplie par P.''')
R('''il faut un roulement à billes plus chargeable dans le catalogue (de C ≥ 24,3 kN). À rouleaux :
C requis = 2 × 1 800^(0,3) ≈ **19,0 kN** — le NU 205 ECP (32,5 kN) suffit… **si la charge est purement
radiale** : un roulement NU n'a pas d'épaulement sur sa bague intérieure, il ne tient pas d'effort axial.*''',
  '''il faut un roulement à billes plus chargeable dans le catalogue (de C ≥ 24,3 kN). À rouleaux (1/n =
3/10 = 0,3) : C requis = 2 × 1 800^(0,3) ≈ **19,0 kN** — le NU 205 ECP (32,5 kN) suffit… **si la charge est
purement radiale** : un roulement NU n'a pas d'épaulement sur sa bague intérieure, il ne tient pas d'effort
axial. C'est d'ailleurs ce qui en fait un excellent **palier libre** : la dilatation de l'arbre se fait dans
le roulement (fiche 6.6). Les variantes NJ et NUP, avec épaulements, tiennent un effort axial modéré.*''')
R('''**Ce que le calcul ne dit pas.** L10 suppose une lubrification correcte et un roulement propre. Les
catalogues proposent une durée **corrigée**, qui tient compte de la lubrification, de la pollution et de la
fiabilité voulue : on la calcule avec les outils du fabricant. Pour un roulement qui tourne très lentement
ou qui reste chargé à l'arrêt, on vérifie aussi la **charge statique de base C0** (catalogue).''',
  '''**Ce que le calcul ne dit pas.** L10 suppose une lubrification correcte et un roulement propre. Les
catalogues proposent une durée **corrigée**, qui tient compte de la propreté du lubrifiant et de la
fiabilité voulue : on la calcule avec les logiciels du fabricant, pas à la main. Pour un roulement qui
tourne très lentement ou qui reste chargé à l'arrêt (pivot de grue, palier d'une porte lourde), on vérifie
aussi la **charge statique de base C0** : la charge supportée sans tourner sans que les billes s'impriment
dans les pistes (catalogue).''')
R('''### 5. Solutions constructives : la rotule et l'hélicoïdale

[[FIG:rotule_helicoidale_solutions]]''', '''### 5. Solutions constructives : la rotule et l'hélicoïdale

Une fois le roulement dimensionné, il reste à savoir **avec quel composant** réaliser les autres liaisons.
Deux cas reviennent souvent en bureau d'études : un arbre qui n'est pas parfaitement aligné (rotule), et
une translation commandée par une rotation (hélicoïdale).

[[FIG:rotule_helicoidale_solutions]]''')
R('''| **hélicoïdale** | **vis trapézoïdale + écrou** (souvent en bronze) | simple, économique, souvent irréversible ; jeu à rattraper, usure |
| **hélicoïdale** | **vis à billes** | rendement élevé, précise, sans usure notable ; réversible (frein sur axe vertical, fiche 6.18) ; jeu supprimé par un écrou préchargé |''',
  '''| **hélicoïdale** | **vis trapézoïdale + écrou** (souvent en bronze) | simple, économique, souvent **irréversible** (pousser sur l'écrou ne fait pas tourner la vis, comme un cric à vis) ; jeu à rattraper, usure |
| **hélicoïdale** | **vis à billes** | rendement élevé, précise ; **réversible** (une charge sur l'écrou fait tourner la vis : frein sur un axe vertical, fiche 6.18) ; jeu supprimé par un écrou préchargé |''')
R('''La loi v = ph × N et la réversibilité sont en fiche **6.18** ; le modèle de ces liaisons (rotule = 3 ddl,
hélicoïdale = 1 ddl) en fiches **6.1 et 6.17**. Ici, on choisit la **réalisation**.''',
  '''La loi v = ph × N (ph : pas de l'hélice, l'avance de l'écrou pour un tour) et la réversibilité sont en
fiche **6.18** ; le modèle de ces liaisons (rotule = 3 mouvements possibles, hélicoïdale = 1) en fiches
**6.1 et 6.17**. Ici, on choisit la **réalisation**.''')
R('''La fiche 6.9 l'a montré : une vis serrée est une vis **tendue**. C'est sa tension, la **précharge F0**, qui
plaque les pièces et les empêche de bouger. Deux questions :''',
  '''*Attention, ne pas confondre : dans cette fiche, **C** est la charge dynamique de base d'un roulement (en
kN) ; le couple de serrage d'une vis se note **Cs** (en N·m).*

La fiche 6.9 l'a montré : une vis serrée est une vis **tendue**. C'est sa tension, la **précharge F0**, qui
plaque les pièces et les empêche de bouger. Deux questions :''')
R('''- **Re** : la limite élastique de la classe (fiche 6.9) : classe 8.8 → 8 × 8 × 10 = **640 MPa**.''',
  '''- **Re** : la limite élastique de la classe (fiche 6.9) : classe 8.8 → 8 × 8 × 10 = **640 MPa** (la norme
  l'appelle Rp0,2).

**Avec une marge.** σ = F0 / As ne compte que la **traction**. Pendant le serrage, le couple tord aussi la
vis : la contrainte réelle est nettement plus haute que F0 / As. C'est pourquoi on ne vise jamais F0 / As
proche de Re.''')
R('''**2. À quel couple serrer pour obtenir F0 ?**

> **C ≈ 0,2 × d × F0** (d : diamètre nominal)

**Le 0,2 n'est qu'un ordre de grandeur.** Une grande partie du couple de serrage part en **frottement** :
sous la tête (ou l'écrou) et dans les filets ; le reste seulement tend la vis. Le coefficient dépend donc
de l'état des surfaces et de la lubrification. **Vis graissée : il baisse** — le même couple tend alors
davantage la vis, jusqu'à risquer de la plastifier. **Surfaces sèches ou rugueuses : il monte** — la vis
est moins serrée qu'on ne croit. Pour un serrage précis, on utilise les **tables de couples du fabricant de
visserie** ou une méthode de calcul détaillée, et on serre à la **clé dynamométrique**.

*Exemple : vis M10 classe 8.8, précharge visée F0 = 25 kN (donnée du bureau d'études). σ = 25 000 / 58 ≈
**431 MPa** < 640 MPa : la vis tient (67 % de Re). Couple : C ≈ 0,2 × 10 × 25 000 = 50 000 N·mm =
**50 N·m** — ordre de grandeur, à confirmer par la table du fabricant.*''',
  '''**2. À quel couple serrer pour obtenir F0 ?** Un couple, c'est une force × un bras de levier. Pour tendre
la vis à F0, il faut vaincre des frottements qui augmentent avec F0, et qui agissent à une distance de
l'axe de l'ordre du diamètre. Le couple est donc proportionnel à F0 × d :

> **Cs ≈ 0,2 × d × F0** (d : diamètre nominal ; avec d en mm et F0 en N, Cs sort en N·mm : ÷ 1 000 pour des N·m)

**Le 0,2 n'est qu'un ordre de grandeur** (il correspond à des surfaces sèches ou peu huilées). Une grande
partie du couple de serrage part en **frottement** : sous la tête (ou l'écrou) et dans les filets ; le reste
seulement tend la vis. **Vis graissée : le coefficient baisse** — le même couple tend alors davantage la
vis, jusqu'à dépasser Re : elle s'allonge **définitivement**, comme un ressort trop tiré, perd sa précharge
ou casse au resserrage. **Surfaces sèches ou rugueuses : il monte** — la vis est moins serrée qu'on ne croit.
Pour un serrage précis, on utilise les **tables de couples du fabricant de visserie** pour la lubrification
réelle, et on serre à la **clé dynamométrique**.

*Exemple : vis M10 classe 8.8, précharge visée F0 = 25 kN (donnée du bureau d'études). σ = 25 000 / 58 ≈
**431 MPa** < 640 MPa : en **traction seule**, la vis est à 67 % de Re — la torsion de serrage s'y ajoute.
Couple : Cs ≈ 0,2 × 10 × 25 000 = 50 000 N·mm = **50 N·m** — ordre de grandeur. Sur une vis huilée, ce même
couple tendrait davantage la vis et pourrait l'amener près de sa limite : le couple réel se prend dans la
table du fabricant, pour la lubrification réelle.*''')
R('''4. **Inventer C** : la charge dynamique de base se lit au catalogue, pour **une référence précise** — elle
   change même d'une génération de roulement à l'autre.''',
  '''4. **Inventer C** : la charge dynamique de base se lit au catalogue, pour **la marque et la référence
   exactes** — elle change d'un fabricant à l'autre et d'une génération à l'autre (les valeurs de la fiche
   10.1 ne sont qu'un exemple de lecture).''')
R('''7. **Prendre C ≈ 0,2 × d × F0 pour une valeur exacte** : c'est un ordre de grandeur, qui dépend du
   frottement.''', '''7. **Prendre Cs ≈ 0,2 × d × F0 pour une valeur exacte** : c'est un ordre de grandeur, qui dépend du
   frottement. Et oublier que la torsion de serrage s'ajoute à F0 / As.''')
R('''- Vis : **σ = F0 / As < Re** ; couple **C ≈ 0,2 × d × F0**, **ordre de grandeur** qui dépend du frottement.''',
  '''- Vis : **σ = F0 / As < Re**, avec une marge (la torsion de serrage s'ajoute) ; couple **Cs ≈ 0,2 × d × F0**,
  **ordre de grandeur** qui dépend du frottement.''')
R('''**Vis : précharge** — σ = F0 / As < Re · As (ISO 898-1) : M8 36,6 mm², M10 58,0 mm², M12 84,3 mm² ·
classe 8.8 : Re = 640 MPa''', '''**Vis : précharge** — σ = F0 / As < Re, avec une marge (torsion de serrage) · As (ISO 898-1) : M8 36,6 mm²,
M10 58,0 mm², M12 84,3 mm² · classe 8.8 : Re = 640 MPa''')
R('''**Couple de serrage** — C ≈ 0,2 × d × F0 : **ordre de grandeur**, le coefficient dépend du frottement''',
  '''**Couple de serrage** — Cs ≈ 0,2 × d × F0 : **ordre de grandeur**, le coefficient dépend du frottement''')
R('''**Durée de vie** — L10 = (C / P)ⁿ (millions de tours) · n = 3 (billes), 10/3 (rouleaux) ·''',
  '''**Durée de vie (ISO 281)** — L10 = (C / P)ⁿ (millions de tours) · n = 3 (billes), 10/3 (rouleaux) ·''')

# ---------------- cas industriel (scénario cohérent)
a0 = s.index('''    "exemple": """''')
a1 = s.index('''    "exercice": """''')
s = s[:a0] + '''    "exemple": """
### Cas industriel — Le roulement qui tenait 9 mois au lieu de 3 ans

**Le symptôme.** Un ventilateur de séchage tourne à 1 500 tr/min, 16 h par jour. Le roulement côté turbine,
un SKF 6205 (C = 14,8 kN), devait durer plus de trois ans ; il lâche au bout de neuf mois. Le lot suivant
fait pareil : ce n'est pas un défaut de fabrication.

**Ce qu'annonçait le calcul de conception.** L'effort sur le roulement avait été estimé à **1,2 kN** :
L10 = (14,8 / 1,2)³ ≈ 1 880 millions de tours, soit L10h = 1 880 × 10⁶ / (60 × 1 500) ≈ **20 800 h**. À 16 h
par jour, cela fait environ 1 300 jours : **3,6 ans**. D'où l'attente de la maintenance.

**Ce qui se passe vraiment.** La turbine s'encrasse : la poussière collée d'un seul côté des pales décentre
la masse — un **balourd**. À chaque tour, la turbine « tire » sur l'arbre comme une machine à laver qui
essore avec le linge en boule, et cet effort s'ajoute. Mesuré sur site, l'effort atteint **2 kN** :
L10 = (14,8 / 2)³ ≈ 405 millions de tours, soit **4 500 h** — environ 280 jours à 16 h par jour : **neuf
mois**. Exactement la durée observée.

**Ce que le calcul montre.** L'effort n'a augmenté que de 67 %, mais la durée de vie a été divisée par
(2 / 1,2)³ ≈ **4,6**. C'est l'exposant 3 qui rend le roulement si sensible à la charge.

**Les corrections**, par ordre d'efficacité :

| Action | Effet |
|---|---|
| **nettoyer et équilibrer la turbine**, puis contrôler la vibration | supprime la surcharge à la source |
| choisir un roulement de C plus grand au catalogue, pour la charge réelle | marge sur la charge |
| estimer la durée attendue par la durée **corrigée** (logiciel du fabricant), avec la vraie lubrification | une attente réaliste pour la maintenance |

**Ce que le cas apprend.** Une durée de vie se calcule avec la **charge réelle**, pas avec la charge
nominale du cahier des charges. Et une petite surcharge coûte cher : l'exposant amplifie tout.
""",
''' + s[a1:]

# ---------------- exercice / corrigé
R('''> **L10 = (C/P)ⁿ**, n = 3 (billes), 10/3 (rouleaux) ; **L10h = L10 × 10⁶ / (60 N)** ; **C requis =
> P × L10^(1/n)**. Vis : **σ = F0 / As < Re** ; **C ≈ 0,2 × d × F0** (ordre de grandeur).''',
  '''> **L10 = (C/P)ⁿ**, n = 3 (billes), 10/3 (rouleaux) ; **L10h = L10 × 10⁶ / (60 N)** ; **C requis =
> P × L10^(1/n)**. Vis : **σ = F0 / As < Re** (avec une marge) ; couple **Cs ≈ 0,2 × d × F0** (ordre de grandeur).''')
R('''C requis = 1,6 × 1 152^(1/3). Rouleaux : L10 = (32,5 / 1,6)^(10/3). Vis : σ = 20 000 / 58 ; C ≈ 0,2 × 10 ×
20 000.''', '''C requis = 1,6 × 1 152^(1/3). Rouleaux : L10 = (32,5 / 1,6)^(10/3). Vis : σ = 20 000 / 58 ; Cs ≈ 0,2 × 10 ×
20 000.''')
R('''**5.** L10 = (32,5 / 1,6)^(10/3) = 20,3^(10/3) ≈ 22 900 millions de tours ; L10h ≈ **397 000 h** : très''',
  '''**5.** L10 = (32,5 / 1,6)^(10/3) = 20,31^(10/3) ≈ 22 900 millions de tours ; L10h ≈ **397 000 h** : très''')
R('''**6.** σ = 20 000 / 58 ≈ **345 MPa** < 640 MPa : les vis tiennent (54 % de Re). Couple ≈ 0,2 × 10 ×
20 000 = 40 000 N·mm ≈ **40 N·m**, **ordre de grandeur** à confirmer dans la table du fabricant de visserie.''',
  '''**6.** σ = 20 000 / 58 ≈ **345 MPa** < 640 MPa : en traction seule, les vis sont à 54 % de Re, ce qui
laisse la marge nécessaire pour la torsion de serrage. Couple Cs ≈ 0,2 × 10 × 20 000 = 40 000 N·mm ≈
**40 N·m**, **ordre de grandeur** à confirmer dans la table du fabricant de visserie.''')
R('''**Sensibilité** : la durée calculée (13 700 h) est 0,69 fois la durée visée ; il faudrait C multiplié par
0,69^(−1/3) ≈ 1,13, soit 14,8 × 1,13 ≈ 16,8 kN : même résultat qu'en question 4.''',
  '''**Sensibilité** : il manque 20 000 / 13 700 ≈ 1,46 fois la durée. Comme la durée varie comme C³, il faut
multiplier C par la racine cubique de 1,46, soit environ 1,13 : 14,8 × 1,13 ≈ 16,8 kN. On retrouve la
question 4.''')

# ---------------- at164
R('''             "pieges": [(288153, "288 000 : tu n'as pas divisé par 60.''', '''             "pieges": [(288159, "288 000 : tu n'as pas divisé par 60.''')
R('''             "pieges": [(2160, "2 160 : tu as multiplié P par L10. Il faut la racine cubique de L10 : "
                               "C = P × L10^(1/3).")],''',
  '''             "pieges": [(2160, "2 160 : tu as multiplié P par L10. Il faut la racine cubique de L10 : "
                               "C = P × L10^(1/3)."),
                        (19.01, "19,0 : tu as pris 1/n = 0,3, celui des rouleaux. Billes : racine cubique, "
                                "L10^(1/3).")],''')
R('''            "calcul": "**L10 ≈ 207,5 Mtr** ; **L10h ≈ 4 803 h** : insuffisant ; **C requis ≈ 23,8 kN**.",''',
  '''            "calcul": "**L10 ≈ 207,5 millions de tours** ; **L10h ≈ 4 803 h** : insuffisant ; **C requis ≈ 23,8 kN**.",''')

# ---------------- at165
R('''            ("Classe 8.8",
             "Rm = 8 × 100 = 800 MPa ; Re = 8 × 8 × 10 = 640 MPa."),''',
  '''            ("Classe 8.8",
             "Rm (résistance à la rupture) = 8 × 100 = 800 MPa ; Re (limite élastique : au-delà, la vis "
             "reste allongée) = 8 × 8 × 10 = 640 MPa."),''')
R('''             "options": ["La vis casse", "La vis tient : environ 67 % de sa limite élastique",
                         "On ne peut pas conclure sans le couple de serrage"], "bonne": 1,''',
  '''             "options": ["La vis casse",
                         "La vis tient en traction (environ 67 % de Re) ; la torsion de serrage s'y ajoute, "
                         "d'où la marge",
                         "On ne peut pas conclure sans le couple de serrage"], "bonne": 1,''')
R('''             "consigne": "Donne l'ordre de grandeur du couple de serrage : C ≈ 0,2 × d × F0, en N·m.",''',
  '''             "consigne": "Donne l'ordre de grandeur du couple de serrage : Cs ≈ 0,2 × d × F0, en N·m.",''')
R('''             "aide": "C ≈ 0,2 × 10 × 25 000 = 50 000 N·mm = 50 N·m."},''', '''             "aide": "Cs ≈ 0,2 × 10 × 25 000 = 50 000 N·mm = 50 N·m."},''')
R('''            "regle": "**σ = F0 / As < Re** ; **C ≈ 0,2 × d × F0** (ordre de grandeur, dépend du "
                    "frottement).",''', '''            "regle": "**σ = F0 / As < Re**, avec une marge ; **Cs ≈ 0,2 × d × F0** (ordre de grandeur, "
                    "dépend du frottement).",''')
R('''            "conversions": "C en N·mm → N·m : ÷ 1 000.",''', '''            "conversions": "Cs en N·mm → N·m : ÷ 1 000.",''')
R('''            "remplacement": "Re = 8 × 8 × 10 ; σ = 25 000 / 58 ; C = 0,2 × 10 × 25 000.",''',
  '''            "remplacement": "Re = 8 × 8 × 10 ; σ = 25 000 / 58 ; Cs = 0,2 × 10 × 25 000.",''')
R('''            "calcul": "**Re = 640 MPa** ; **σ ≈ 431 MPa** (67 % de Re) ; **C ≈ 50 N·m**.",''',
  '''            "calcul": "**Re = 640 MPa** ; **σ ≈ 431 MPa** (67 % de Re, en traction seule) ; **Cs ≈ 50 N·m**.",''')
R('''            "verification": "Le 0,2 n'est qu'un ordre de grandeur : la table du fabricant de visserie, "
                            "pour la lubrification réelle, donne le couple à appliquer. Un graissage non "
                            "prévu augmente la précharge pour le même couple.",''',
  '''            "verification": "Le 0,2 n'est qu'un ordre de grandeur : la table du fabricant de visserie, "
                            "pour la lubrification réelle, donne le couple à appliquer. Pendant le serrage, "
                            "la torsion s'ajoute à la traction : 67 % de Re en traction seule ne laisse pas "
                            "une si grande marge. Un graissage non prévu augmente la précharge pour le même "
                            "couple.",''')
R('''        "a_retenir": "À retenir : on vérifie la vis sur sa précharge (σ = F0 / As < Re), puis on cherche "
                     "le couple qui donne cette précharge — C ≈ 0,2 × d × F0 n'est qu'un ordre de "
                     "grandeur.",''', '''        "a_retenir": "À retenir : on vérifie la vis sur sa précharge (σ = F0 / As < Re, avec une marge), "
                     "puis on cherche le couple qui donne cette précharge — Cs ≈ 0,2 × d × F0 n'est qu'un "
                     "ordre de grandeur.",''')

# ---------------- générateur : charges réalistes selon le roulement
R('''    nom, C, n, type_ = random.choice([("SKF 6205", 14.8, 3, "à billes"),
                                      ("SKF NU 205 ECP", 32.5, 10 / 3, "à rouleaux cylindriques")])
    P = random.choice([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0])''',
  '''    nom, C, n, type_ = random.choice([("SKF 6205", 14.8, 3, "à billes"),
                                      ("SKF NU 205 ECP", 32.5, 10 / 3, "à rouleaux cylindriques")])
    # charges réalistes pour chaque roulement (des durées de plusieurs siècles n'apprennent rien)
    P = random.choice([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0] if n == 3 else [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])''')

# ---------------- quiz : couple Cs
R('''    ("La formule C ≈ 0,2 × d × F0 donne le couple de serrage :",''',
  '''    ("La formule Cs ≈ 0,2 × d × F0 donne le couple de serrage :",''')
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print("ok")
