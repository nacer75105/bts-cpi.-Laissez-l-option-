# -*- coding: utf-8 -*-
# Corrections du brouillon 3.5 après relecture (relecteur-bts-meca B1-B7 + améliorations ;
# prof-pedagogue B1-B7 + améliorations). Retouches de 3.1 et 4.1 : soumises à l'auteur, non faites ici.
import os
ICI = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(ICI, 'brouillon_3_5.py')
c = open(F, encoding='utf-8').read()


def R(a, b, n=1):
    global c
    assert c.count(a) == n, (a[:80], c.count(a))
    c = c.replace(a, b)


# ---------------------------------------------------------------- figures
# Wöhler : ligne Re, libellé de zone, palier « très grand nombre de cycles »
R('''    p.append(_txt(ox + 70, oy - H + 8, "rupture rapide", 9, FIN, "middle"))''',
  '''    p.append(f"<line x1='{ox}' y1='{oy - 200}' x2='{ox + 470}' y2='{oy - 200}' stroke='{ALERTE}' stroke-dasharray='6 4'/>")
    p.append(_txt(ox + 470, oy - 204, "Re (traction) : toute la courbe reste en dessous", 9, ALERTE, "end", True))
    p.append(_txt(ox + 70, oy - H + 22, "peu de cycles", 9, FIN, "middle"))''')
R('''    p.append(_txt(ox + 230, oy - H + 8, "endurance limitée", 9, FIN, "middle"))
    p.append(_txt(ox + 410, oy - H + 8, "endurance illimitée (acier)", 9, FIN, "middle"))''',
  '''    p.append(_txt(ox + 230, oy - H + 22, "endurance limitée", 9, FIN, "middle"))
    p.append(_txt(ox + 410, oy - H + 22, "endurance illimitée (acier)", 9, FIN, "middle"))''')
# fatigue_entaille : libellés
R('''    p.append(_txt(390, 74, "σ nominale", 10, ALERTE, "start"))''',
  '''    p.append(_txt(390, 74, "σ nominale", 10, ALERTE, "start"))
    p.append(_txt(40, 64, "contrainte en surface, le long de l'arbre", 9, ALERTE, "start"))''')
R('''    p.append(_txt(217, 86, "gorge (angle vif)", 10, ALERTE, "middle", True))''',
  '''    p.append(_txt(217, 86, "gorge (petit rayon)", 10, ALERTE, "middle", True))''')
R('''    p.append(_txt(120, 190, "arbre en flexion rotative", 10, TRAIT, "middle"))''',
  '''    p.append(_txt(120, 190, "arbre en flexion rotative (il tourne, chargé : chaque fibre passe", 9, TRAIT, "start"))
    p.append(_txt(120, 202, "de la traction à la compression à chaque tour)", 9, TRAIT, "start"))''')
R('''    p.append(_txt(cx + 40, cy - 86, "zone rugueuse : rupture finale", 10, TRAIT, "middle", True))''',
  '''    p.append(_txt(cx + 40, cy - 86, "zone rugueuse : rupture finale", 10, TRAIT, "middle", True))
    p.append(_txt(cx + 40, cy - 100, "cassure vue de face (coupe au fond de la gorge)", 9, FIN, "middle"))''')
# Charpy : cotes h0/h1, sens des températures
R('''    p.append(_txt(ax - 70, ay + 20, "départ : h0", 10, ALESAGE, "end", True))
    p.append(_txt(ax + 110, ay + 50, "remontée : h1", 10, ALESAGE, "start", True))''',
  '''    p.append(f"<line x1='{ax - 150}' y1='{ay + Lp + 5}' x2='{ax + 140}' y2='{ay + Lp + 5}' stroke='{FIN}' stroke-dasharray='3 3'/>")
    p.append(_txt(ax - 150, ay + Lp - 1, "point le plus bas", 8, FIN, "start"))
    p.append(f"<line x1='{ax - 150}' y1='{ay + 55}' x2='{ax - 80}' y2='{ay + 55}' stroke='{ALESAGE}' stroke-dasharray='3 3'/>")
    p.append(_k_fl(ax - 140, ay + Lp + 3, ax - 140, ay + 58, ALESAGE, "kb", 1.4))
    p.append(_txt(ax - 136, ay + 100, "h0 (départ)", 10, ALESAGE, "start", True))
    p.append(f"<line x1='{ax + 70}' y1='{ay + 95}' x2='{ax + 140}' y2='{ay + 95}' stroke='{ALESAGE}' stroke-dasharray='3 3'/>")
    p.append(_k_fl(ax + 130, ay + Lp + 3, ax + 130, ay + 98, ALESAGE, "kb", 1.4))
    p.append(_txt(ax + 126, ay + 125, "h1", 10, ALESAGE, "end", True))
    p.append(_txt(ax + 126, ay + 137, "(remontée)", 9, ALESAGE, "end"))''')
R('''    p.append(_txt(ox + L, oy + 18, "température d'essai", 10, TRAIT, "end"))''',
  '''    p.append(_txt(ox + L, oy + 18, "température d'essai :  ← plus froid · plus chaud →", 10, TRAIT, "end"))''')
# flexion
R('''    p = [_k_defs(), _txt(30, 24, "Essai de flexion trois points : pour les matériaux qu'on ne sait pas tirer", 13, TRAIT, "start", True)]''',
  '''    p = [_k_defs(), _txt(30, 24, "Essai de flexion trois points : l'essai de référence des céramiques", 13, TRAIT, "start", True)]''')
R('''                                   ("Pour les céramiques, fontes,", TRAIT, False),
                                   ("composites : une éprouvette de", TRAIT, False),
                                   ("traction se briserait dans les mors.", TRAIT, False), ("", TRAIT, False),''',
  '''                                   ("Pour les céramiques : une", TRAIT, False),
                                   ("éprouvette de traction se", TRAIT, False),
                                   ("briserait dans les mors.", TRAIT, False), ("", TRAIT, False),''')
R('''    p.append(_txt(46, 284, "Même formule que la RDM de la flexion (fiche 4.3) : M = F L / 4 au milieu, I/v = b h² / 6.", 12, TRAIT))''',
  '''    p.append(_txt(46, 284, "RDM de la flexion (fiche 4.3) : σ = Mf / (I/v), avec Mf = F L / 4 au milieu et I/v = b h² / 6.", 12, TRAIT))''')
# grenaillage
R('''                                   ("la surface, écrouie, voudrait", TRAIT, False),''',
  '''                                   ("la surface, martelée, voudrait", TRAIT, False),''')
# figure à curseurs : axe à 800, légende sans Kf
R('''    Y = lambda s: oy - min(s, 600) / 600 * H  # noqa: E731
    for s in (0, 200, 400, 600):''',
  '''    Y = lambda s: oy - min(s, 800) / 800 * H  # noqa: E731
    for s in (0, 200, 400, 600, 800):''')
R('''    p.append(_txt(30, 316, "Courbe schématique ; σD de la pièce (état de surface et taille compris) : donnée d'énoncé. Kt pris pour Kf : prudent.", 10, FIN))''',
  '''    p.append(_txt(30, 316, "Courbe schématique ; σD de la pièce (état de surface et taille compris) : donnée d'énoncé. On applique Kt tel quel : choix prudent.", 10, FIN))''')

# ---------------------------------------------------------------- cours
R('''fonctionnement, sous une charge **répétée** bien inférieure à Re : c'est la fatigue, la cause la plus
fréquente des ruptures de pièces mécaniques en service.''',
  '''fonctionnement, sous une charge **répétée** bien inférieure à Re : c'est la fatigue, l'une des toutes
premières causes de rupture des pièces mécaniques en service. Arbres de transmission, ressorts, bielles,
boulons de roue, cordons de soudure de châssis : quand une pièce mécanique casse en service, on pense d'abord
à la fatigue.''')
R('''Un arbre qui tourne en flexion voit chaque fibre passer de la traction à la compression **à chaque tour**.
Un ressort, une bielle, une dent d'engrenage subissent des millions de cycles. Même si chaque cycle reste
sous Re, la pièce s'use de l'intérieur :''',
  '''Un arbre qui tourne en flexion voit chaque fibre passer de la traction à la compression **à chaque tour**.
Un ressort, une bielle, une dent d'engrenage subissent des millions de cycles.

**Pourquoi une charge trop faible pour casser finit par casser.** *Pliez un trombone dans un sens puis dans
l'autre : au bout de quelques allers-retours il casse, alors qu'un seul pliage ne l'aurait jamais cassé.* La
fatigue, c'est le même phénomène, en invisible. Re est une valeur moyenne sur toute la section ; au fond d'une
rayure ou d'une gorge, à l'échelle de quelques grains de métal, la contrainte locale est plus forte. Quelques
grains glissent d'un micron dans un sens, puis dans l'autre, à chaque cycle : un trombone miniature. Après des
milliers de cycles, ce va-et-vient ouvre une microfissure ; et une fissure est elle-même une entaille
extrêmement aiguë, au bout de laquelle la contrainte se concentre encore plus : elle avance un peu à chaque
cycle. La pièce ne s'use pas dans la masse : elle se fissure **à partir de sa surface**, pour trois raisons :
en flexion et en torsion, la contrainte est maximale en surface (RDM) ; c'est en surface que se trouvent les
rayures, les marques d'outil et les gorges ; un grain de surface n'est soutenu que d'un côté.

La pièce s'endommage donc progressivement, en trois temps :''')
R('''**L'essai de fatigue.** On sollicite des éprouvettes identiques avec une contrainte alternée d'amplitude σa,
et on compte le nombre de cycles N jusqu'à la rupture.''',
  '''**Amplitude, alternée.** Une fibre d'un arbre qui tourne en flexion passe de +120 MPa (traction) à −120 MPa
(compression), puis revient à +120 MPa, à chaque tour : c'est une contrainte **alternée**, et 120 MPa est son
**amplitude σa** (l'écart entre le milieu du cycle, ici 0, et le sommet).

**Pourquoi une échelle logarithmique.** Les durées de vie vont de mille à cent millions de cycles : sur une
règle normale, tout se tasserait à gauche. L'axe avance donc d'une graduation à chaque **× 10** (10³, 10⁴,
10⁵…). *Pour fixer les idées : un arbre à 3 000 tr/min fait 180 000 cycles par heure ; il atteint 10⁷ cycles
en environ 55 heures de marche. C'est pour cela qu'en mécanique on vise une durée « illimitée ».*

**L'essai de fatigue.** On sollicite des éprouvettes identiques avec une contrainte alternée d'amplitude σa,
et on compte le nombre de cycles N jusqu'à la rupture.''')
R('''- **Pour les aciers**, la courbe présente un **palier** : sous une amplitude σD, la **limite d'endurance**,
  l'éprouvette ne casse plus, quel que soit le nombre de cycles. C'est l'objectif de dimensionnement : rester
  sous σD donne une **durée de vie illimitée**.''',
  '''- **Pour les aciers**, la courbe présente un **palier** : sous une amplitude σD, la **limite d'endurance**,
  l'éprouvette ne casse plus. En pratique, σD est définie pour un très grand nombre de cycles fixé par
  l'essai : en dessous, on considère la durée de vie comme **illimitée**. C'est l'objectif de
  dimensionnement.''')
R('''  On choisit une **durée de vie visée** (un nombre de cycles) et on lit la contrainte admissible
  correspondante sur la courbe du fournisseur.''',
  '''  C'est un constat d'essai : en aluminium, toute pièce cyclée a une durée de vie finie, et c'est le
  concepteur qui la choisit. On fixe une **durée de vie visée** (un nombre de cycles) et on lit la contrainte
  admissible correspondante sur la courbe du fournisseur.''')
R('''son **état de surface** est moins bon, sa **taille** est plus grande (plus de chances d'y trouver un défaut), et''',
  '''son **état de surface** est moins bon (une rayure d'usinage est une minuscule gorge, un point de départ
possible pour la fissure ; une surface polie en a beaucoup moins), sa **taille** est plus grande (plus de
chances d'y trouver un défaut), et''')
R('''Au fond d'une gorge, d'un épaulement ou d'un trou, la contrainte locale dépasse la contrainte nominale
calculée en RDM :

> **σmax = Kt × σnom** — Kt : coefficient de concentration de contrainte (≥ 1), lu sur abaque selon la forme

En statique, un matériau ductile se plastifie localement et « oublie » le pic. **En fatigue, non** : la
fissure s'amorce précisément à ce pic. D'où la règle de vérification (en prenant Kt, ce qui est prudent) :

> **Kt × σa,nom ≤ σD de la pièce** (avec, en plus, le coefficient de sécurité demandé)''',
  '''Au fond d'une gorge, d'un épaulement ou d'un trou, la contrainte locale dépasse la contrainte nominale
calculée en RDM. *Les « lignes d'effort » traversent la pièce comme l'eau d'une rivière : devant une pile de
pont, l'eau se resserre et accélère sur les bords. Au fond d'une gorge, les lignes d'effort se resserrent de la
même façon : plus l'angle est vif, plus le resserrement est brutal ; plus le congé est grand, plus le passage
est doux.*

> **σmax = Kt × σnom** — c'est le coefficient Kt de la fiche 4.1 (σ réelle = Kt × σ calculée), lu sur abaque
> selon la forme et le type de sollicitation. σnom se calcule comme en RDM : pour un arbre en flexion rotative,
> σnom = Mf / (I/v) (fiche 4.3). Attention : σmax désigne ici le **pic au fond de la gorge** ; c'est toujours
> une amplitude de cycle, qu'on peut placer sur la courbe de Wöhler.

**Pourquoi le pic compte en fatigue et pas en statique.** En statique, chargé une seule fois, le petit volume
au fond de la gorge dépasse Re, se déforme un peu, « cède » et reporte l'effort sur le métal voisin : la pièce
s'en accommode. En fatigue, ce même petit volume est sollicité dans un sens puis dans l'autre des millions de
fois : c'est lui qui joue le trombone. D'où la règle de vérification :

> **Kt × σnom ≤ σD de la pièce** (et σD / s si l'énoncé impose un coefficient de sécurité s)

*En fatigue, l'effet réel d'une entaille, mesuré par essai et noté Kf, est inférieur ou égal à Kt : appliquer
Kt tel quel va dans le sens de la sécurité.*

**Domaine de validité.** Cette règle vaut pour une contrainte **purement alternée**, de moyenne nulle : c'est le
cas de l'arbre en flexion rotative. Si la contrainte oscille autour d'une valeur non nulle (ressort préchargé,
vis serrée, bielle), l'amplitude admissible est plus faible ; la valeur à utiliser est alors donnée par
l'énoncé ou par le fournisseur.''')
R('''*Exemple (données d'énoncé) : un arbre subit une contrainte alternée nominale de 140 MPa au droit d'une gorge à
angle vif (Kt = 2,5). La limite d'endurance de la pièce, corrections comprises, vaut 270 MPa. σmax = 2,5 × 140 =
**350 MPa** > 270 : **la pièce cassera en fatigue**. Avec un congé plus grand (Kt = 1,8), σmax = **252 MPa** <
270 : elle tient (de justesse).*''',
  '''*Exemple (données d'énoncé ; aucun coefficient de sécurité imposé, s = 1) : un arbre subit une contrainte
alternée nominale de 140 MPa au droit d'une gorge à petit rayon de fond (Kt = 2,5). La limite d'endurance de la
pièce, corrections comprises, vaut 270 MPa. σmax = 2,5 × 140 = **350 MPa** > 270 : **la pièce cassera en
fatigue**. Avec un congé plus grand (Kt = 1,8), σmax = **252 MPa** < 270 : elle tient — de justesse ; en bureau
d'études, une marge aussi faible serait le plus souvent refusée.*''')
R('''**L'essai** (ISO 148-1) : un mouton-pendule lâché d'une hauteur h0 frappe une éprouvette entaillée en V et la
casse ; il remonte moins haut, à h1. L'énergie qu'il a perdue a été absorbée par la rupture :

> **KV = m × g × (h0 − h1)** (en joules ; la norme corrige en plus les frottements)''',
  '''La **résilience**, c'est l'aptitude d'un matériau à encaisser un choc sans se fendre ; on la mesure par
l'énergie qu'il « boit » en cassant.

**L'essai** (ISO 148-1) : un mouton-pendule lâché d'une hauteur h0 frappe une éprouvette entaillée en V et la
casse ; il remonte moins haut, à h1 (h0 et h1 : hauteurs du centre de gravité du mouton au départ et à la
remontée). L'énergie qu'il a perdue a été absorbée par la rupture. L'entaille et le choc placent l'éprouvette
dans le pire cas (un défaut et un chargement brutal) : si le métal encaisse ça, il encaissera une rayure et
un coup en service.

> **KV = m × g × (h0 − h1)** (en joules ; la norme corrige en plus les frottements)

*Autrefois, on divisait cette énergie par la section sous l'entaille (0,8 cm² pour l'éprouvette normale) :
c'était la KCV, en J/cm², qu'on trouve encore dans de vieux documents. La norme actuelle donne KV en joules ;
c'est aussi en joules que la désignation garantit ses 27 J.*''')
R('''**La transition ductile-fragile.** Pour les aciers de construction, l'énergie absorbée chute quand la
température baisse : au-dessus de la **zone de transition**, rupture ductile ; en dessous, rupture fragile.
Un acier parfaitement correct en été peut casser net en hiver, au moindre choc — c'est ce qui est arrivé à
des navires soudés (fiche 3.1). Les aciers inoxydables austénitiques (304) et les alliages d'aluminium ne
présentent pas cette transition.''',
  '''**La transition ductile-fragile.** Pour les aciers de construction, l'énergie absorbée chute quand la
température baisse : au-dessus de la **zone de transition**, rupture ductile ; en dessous, rupture fragile.
*Une barre de chocolat sortie du congélateur casse net avec un « clac », alors qu'à température ambiante elle
se tord avant de céder : certains aciers font pareil.* En simplifiant : pour se déformer, les plans d'atomes du
métal doivent glisser les uns sur les autres ; au froid, ce glissement devient plus difficile pour les aciers
de construction, et quand glisser « coûte » plus que se fendre, le métal se fend. Un acier parfaitement
correct en été peut casser net en hiver, au moindre choc — c'est ce qui est arrivé à des navires soudés
(fiche 3.1). Les aciers inoxydables austénitiques (304) et les alliages d'aluminium ne présentent pas de
transition marquée.''')
R('''**Ce que garantit la désignation** (EN 10025-2, fiche 3.2) : les qualités JR, J0, J2 garantissent une énergie
minimale de **27 J** à une température d'essai donnée — **+20 °C** (JR), **0 °C** (J0), **−20 °C** (J2). *Un
garde-corps extérieur, une structure de levage utilisée l'hiver : on choisit la qualité dont la température
d'essai couvre la température de service la plus basse. Pour −10 °C, J0 ne garantit rien ; il faut J2.*''',
  '''**Ce que garantit la désignation** (EN 10025-2, fiche 3.2) : les qualités JR, J0, J2 garantissent une énergie
minimale de **27 J** à une température d'essai donnée — **+20 °C** (JR), **0 °C** (J0), **−20 °C** (J2) ; la
norme prévoit aussi une qualité K2 pour certaines nuances. *Un garde-corps extérieur, une structure de levage
utilisée l'hiver : règle simple et prudente, on choisit la qualité dont la température d'essai couvre la
température de service la plus basse. Pour −10 °C, la désignation J0 ne garantit plus rien ; il faut J2.* (En
charpente, le choix réglementaire dépend aussi de l'épaisseur et du niveau de contrainte.)

**Et la dureté ?** C'est l'autre essai du programme, déjà cité en fiche 3.1 : on enfonce un pénétrateur très
dur (bille pour Brinell, HB ; pyramide de diamant pour Vickers, HV ; cône de diamant pour Rockwell C, HRC) et
on mesure l'empreinte (taille ou profondeur). Plus elle est petite, plus le matériau est dur. Essai rapide,
presque non destructif, il sert à contrôler un traitement thermique (« 58 HRC » sur un plan, fiche 3.3) ;
l'échelle se choisit selon la dureté et l'épaisseur de la pièce.''')
R('''Pour les matériaux **fragiles** (céramiques, fontes grises, composites), l'essai de traction est délicat :
l'éprouvette se brise dans les mors. On la pose sur deux appuis et on charge au milieu (**flexion trois
points**). La contrainte maximale, sur la face tendue, vaut (section rectangulaire b × h, portée L) :

> **σmax = 3 F L / (2 b h²)**

C'est la RDM de la flexion (fiche 4.3) : moment maximal F L / 4 au milieu, module de flexion b h² / 6.''',
  '''Pour les matériaux **très fragiles** comme les céramiques, l'essai de traction est délicat : pour tirer une
éprouvette, il faut la serrer dans des mors, et ce serrage crée des points d'appui très durs ; le moindre défaut
d'alignement ajoute une petite flexion parasite ; elle casse là, et on ne mesure rien d'utile. On la pose donc
simplement sur deux appuis et on charge au milieu (**flexion trois points**). L'essai de flexion sert aussi,
pour les plastiques et les composites, à caractériser un matériau qui travaillera en flexion.

La contrainte maximale, sur la face tendue, vaut (section rectangulaire b × h, portée L) :

> **σmax = 3 F L / (2 b h²)**

C'est la RDM de la flexion (fiche 4.3) : σ = Mf / (I/v), avec Mf = F L / 4 au milieu et I/v = b h² / 6 pour un
rectangle ; donc σmax = (F L / 4) × 6 / (b h²) = 3 F L / (2 b h²). La formule suppose le matériau élastique
jusqu'à la rupture, ce qui est le cas des céramiques ; cette « résistance à la flexion » n'est pas Rm : seule une
petite zone est très sollicitée, ce qui la rend en général plus élevée.''')
R('''Alumine, carbure de silicium, nitrure de silicium, zircone… Ce sont des matériaux **très durs**, **très
rigides**, **réfractaires** (ils tiennent à haute température), souvent **isolants** et **inoxydables**. Mais
ils sont **fragiles** : aucune déformation plastique avant rupture, une rupture brutale à partir du moindre
défaut. Ils résistent beaucoup mieux en **compression** qu'en traction, et leur résistance est **dispersée**
d'une pièce à l'autre (elle dépend du plus gros défaut caché).

**Emplois** : plaquettes d'outils de coupe, billes de roulements hybrides, garnitures d'étanchéité,
isolateurs, revêtements anti-usure. **Règles de conception** : éviter la traction et les chocs, éviter les
angles vifs, préférer des formes simples (le matériau s'obtient par frittage de poudres, difficilement usinable
après), et faire travailler la pièce en compression.''',
  '''*Vous connaissez déjà une céramique : le carrelage, ou une tasse. C'est dur (un couteau ne la raye pas), ça ne
rouille pas, ça va au four… mais ça se brise si ça tombe.* Les céramiques techniques — alumine, carbure de
silicium, nitrure de silicium, zircone — ont les mêmes qualités et le même défaut, en beaucoup plus
performant : **très dures**, **très rigides**, **réfractaires** (elles tiennent à haute température), souvent
**isolantes** et **chimiquement inertes** (pas de corrosion). Mais **fragiles** : aucune déformation plastique
avant rupture, une rupture brutale à partir du moindre défaut. Leur résistance est **dispersée** d'une pièce à
l'autre (elle dépend du plus gros défaut caché).

**Compression oui, traction non.** Une fissure doit s'ouvrir pour avancer : la traction l'ouvre, la compression
la referme. Un matériau sans plasticité, qui ne peut pas « émousser » ses fissures, doit donc travailler en
compression.

**Emplois** : plaquettes d'outils de coupe, billes de roulements hybrides (bagues en acier, billes en
céramique), garnitures d'étanchéité, isolateurs, revêtements anti-usure. **Règles de conception** : éviter la
traction, les chocs et les **chocs thermiques** (chauffage ou refroidissement brutal), éviter les angles vifs,
préférer des formes simples (le matériau s'obtient par frittage : on presse de la poudre dans un moule puis on
la cuit, comme une brique ; il est difficile à usiner ensuite).''')
R('''- **Grenaillage** : projection de billes (acier, verre, céramique) à grande vitesse. La surface, martelée,
  voudrait s'étendre ; le cœur l'en empêche : elle reste en **compression**. Une fissure de fatigue doit
  s'ouvrir pour avancer : la compression la tient fermée. **Usage** : ressorts, engrenages, bielles,
  arbres, cordons de soudure.''',
  '''- **Grenaillage** : projection de billes (acier, verre, céramique) à grande vitesse. Chaque bille agit comme un
  petit coup de marteau : elle écrase et étire le métal juste sous la surface, comme un chaudronnier qui martèle
  une tôle. Cette fine peau voudrait s'agrandir, mais elle est collée au cœur, qui n'a pas bougé : elle reste en
  **compression**, comme un tapis trop grand coincé entre quatre murs. Le cycle de contrainte en surface est
  décalé vers la compression : la partie « traction » du cycle, celle qui ouvre la fissure, diminue. **Usage** :
  ressorts, engrenages, bielles, arbres, cordons de soudure. **Défauts induits** : il augmente la rugosité et
  peut déformer une pièce mince (c'est même un procédé de mise en forme) : on masque les portées
  fonctionnelles.''')
R('''mesure par essai** ; il ne se décrète pas. Les contraintes de compression sont **en surface** : un usinage
réalisé **après** les enlève ; un traitement thermique ou un soudage ultérieur peut les relâcher. Le
traitement se place donc **en fin de gamme**, et s'écrit sur le plan.''',
  '''mesure par essai** ; il ne se décrète pas. Les contraintes de compression sont **en surface** : un usinage
réalisé **après** les enlève ; un traitement thermique ou un soudage ultérieur peut les relâcher. Le
traitement se place donc **après les opérations d'usinage et de traitement thermique**, et s'écrit sur le
plan.''')
R('''*Exemple (prix au kilo : données d'énoncé ; Re et ρ : table des matériaux) : un tirant de 1 m doit porter
50 kN en traction, avec un coefficient de sécurité de 2. Section : S = F × s / Re ; masse : ρ × S × L.*''',
  '''*Exemple (prix au kilo : données d'énoncé ; Re et ρ : table des matériaux) : un tirant de 1 m doit porter
50 kN en traction, avec un coefficient de sécurité de 2. Section : S = F × s / Re ; masse : ρ × S × L. Ligne
S235 détaillée : S = 50 000 × 2 / 235 ≈ 426 mm² = 426 × 10⁻⁶ m² ; masse = 7 850 × 426 × 10⁻⁶ × 1 ≈ 3,34 kg ;
coût = 3,34 × 1,2 ≈ 4,0 €.*''')
R('''| 42CrMo4 trempé revenu | 750 | 133 | 1,05 | 3,2 | 3,4 |''', '''| 42CrMo4 trempé revenu | 750 | 133 | 1,05 | 3,2 | 3,3 |''')
R('''du S355 — sans compter son traitement thermique.* Le coût complet ajoute''',
  '''du S355 — sans compter son traitement thermique. Ce tirant est chargé en statique : s'il était cyclé, il
faudrait refaire la comparaison avec σD, pas avec Re.* Le coût complet ajoute''')
R('''- **σmax = Kt × σnom ≤ σD de la pièce** : la forme compte autant que le matériau.''',
  '''- **σmax = Kt × σnom ≤ σD de la pièce** (contrainte alternée) : la forme compte autant que le matériau.''')
R('''- **Charpy** (ISO 148-1) : **KV = m g (h0 − h1)** ; transition ductile-fragile au froid ; JR, J0, J2 = 27 J à
  +20, 0, −20 °C.''',
  '''- **Charpy** (ISO 148-1) : **KV = m g (h0 − h1)**, en joules ; transition ductile-fragile au froid ; JR, J0,
  J2 = 27 J à +20, 0, −20 °C. **Dureté** : empreinte d'un pénétrateur (HB, HV, HRC).''')
R('''**Concentration de contrainte** — σmax = Kt × σnom · fatigue : Kt × σa,nom ≤ σD (pièce) / s''',
  '''**Concentration de contrainte** — σmax = Kt × σnom · fatigue (contrainte alternée) : Kt × σnom ≤ σD (pièce) / s''')

# ---------------------------------------------------------------- cas industriel
R('''### Cas industriel — Le ressort de soupape qui cassait au bout de six mois''',
  '''### Cas industriel — Le ressort de clapet qui cassait au bout de six mois''')
R('''**L'analyse.** Le ressort travaille à chaque cycle du compresseur : des centaines de millions de cycles en
quelques mois.''',
  '''**L'analyse.** Le ressort travaille à chaque cycle du compresseur. À 1 500 cycles par minute en service
continu (donnée d'énoncé), cela fait plus de 2 millions de cycles par jour, et environ 3,9 × 10⁸ en six mois.''')
R('''- Vérification en fatigue sur la limite d'endurance donnée par le fournisseur du fil ;
- **grenaillage** du ressort fini (compression en surface), en dernière opération ;''',
  '''- vérification en fatigue sur les données du fournisseur du fil, qui tiennent compte de la précharge (la
  contrainte du ressort ne revient pas à zéro : la règle « Kt × σnom ≤ σD » ne s'applique pas telle quelle) ;
- **grenaillage** du ressort après enroulement et traitement thermique, écrit sur le plan ;''')

# ---------------------------------------------------------------- exercice / corrigé
R('''**1.** Avec un épaulement à angle vif (Kt = 2,4), calculer σmax. L'arbre tient-il en fatigue ?''',
  '''**1.** Avec un épaulement à petit congé (Kt = 2,4), calculer σmax. L'arbre tient-il en fatigue (aucun coefficient
de sécurité imposé) ?''')
R('''**5.** Lors d'un essai Charpy, un mouton de 20 kg lâché de 1,5 m remonte à 1,3 m. Calculer l'énergie absorbée.
L'éprouvette satisfait-elle le niveau de 27 J ?''',
  '''**5.** Lors d'un essai Charpy réalisé à −20 °C sur une éprouvette de la tôle livrée, un mouton de 20 kg lâché de
1,5 m remonte à 1,3 m. Calculer l'énergie absorbée. La tôle respecte-t-elle la garantie de la qualité choisie en 4 ?''')
R('''**5.** KV = 20 × 9,81 × 0,2 ≈ **39,2 J** ≥ 27 J : l'éprouvette satisfait le niveau (à sa température d'essai).''',
  '''**5.** KV = 20 × 9,81 × 0,2 ≈ **39,2 J** ≥ 27 J à −20 °C : la tôle respecte bien la garantie J2 choisie en 4.''')
R('''compte autant que le matériau. **Unités** : J = N × m. **Prudence** : un Charpy ne vaut qu'à la température à
laquelle il a été fait.''',
  '''compte autant que le matériau. **Unités** : J = N × m. **Prudence** : un Charpy ne renseigne pas sur les
températures plus basses que celle de l'essai.''')

# ---------------------------------------------------------------- méthode
R('''    "**Repérer si la pièce est cyclée** (rotation en flexion, vibrations, charge qui va et vient) : si oui, le "
    "critère n'est pas Re mais la limite d'endurance.",''',
  '''    "**Repérer si la pièce est cyclée** (rotation en flexion, vibration autour de zéro : contrainte alternée) : "
    "si oui, le critère n'est pas Re mais la limite d'endurance. Contrainte qui ne revient pas à zéro (ressort "
    "préchargé, vis serrée) : utiliser les données de l'énoncé ou du fournisseur.",''')
R('''], "Arbre : σnom = 120 MPa, épaulement vif Kt = 2,4 → σmax = 288 MPa > σD = 250 MPa : refusé. Congé plus grand, "
   "Kt = 1,6 → 192 MPa : accepté.")''',
  '''], "Arbre : σnom = 120 MPa, épaulement à petit congé Kt = 2,4 → σmax = 288 MPa > σD = 250 MPa (s = 1, énoncé) : "
   "refusé. Congé plus grand, Kt = 1,6 → 192 MPa : accepté.")''')

# ---------------------------------------------------------------- ateliers (données différentes du cours)
R('''        "enonce": "Un arbre tourne en flexion rotative. Au droit d'une gorge, la contrainte alternée nominale vaut "
                  "140 MPa. La limite d'endurance de la pièce, corrections comprises, vaut 270 MPa (données d'énoncé).",''',
  '''        "enonce": "Un arbre tourne en flexion rotative. Au droit d'une gorge, la contrainte alternée nominale vaut "
                  "130 MPa. La limite d'endurance de la pièce, corrections comprises, vaut 270 MPa ; la limite "
                  "élastique du matériau vaut 600 MPa (données d'énoncé ; aucun coefficient de sécurité imposé).",''')
R('''             "unite": "MPa", "attendu": 350, "tol": 1,
             "consigne": "La gorge est à angle vif (Kt = 2,5). Calcule σmax = Kt × σnom.",
             "indice": "σmax = 2,5 × 140.",
             "pieges": [(140, "140 MPa, c'est la contrainte nominale : au fond de la gorge, elle est multipliée par Kt.")],
             "aide": "2,5 × 140 = 350 MPa."},''',
  '''             "unite": "MPa", "attendu": 325, "tol": 1,
             "consigne": "La gorge a un petit rayon de fond (Kt = 2,5). Calcule σmax = Kt × σnom.",
             "indice": "σmax = 2,5 × 130.",
             "pieges": [(130, "130 MPa, c'est la contrainte nominale : au fond de la gorge, elle est multipliée par Kt.")],
             "aide": "2,5 × 130 = 325 MPa."},''')
R('''             "question": "σmax = 350 MPa pour σD = 270 MPa. Que se passe-t-il ?",
             "options": ["Rien : 350 MPa reste sous Re, la pièce est sûre",''',
  '''             "question": "σmax = 325 MPa pour σD = 270 MPa (et Re = 600 MPa). Que se passe-t-il ?",
             "options": ["Rien : 325 MPa reste sous Re, la pièce est sûre",''')
R('''                             2: "Non : 350 MPa ne casse pas la pièce d'un coup. La fatigue est progressive : la "
                                "fissure avance cycle après cycle."}},''',
  '''                             2: "Non : 325 MPa ne casse pas la pièce d'un coup. La fatigue est progressive : la "
                                "fissure avance cycle après cycle."}},''')
R('''             "unite": "MPa", "attendu": 252, "tol": 1,
             "consigne": "On remplace l'angle vif par un congé de grand rayon (Kt = 1,8). Calcule σmax.",
             "indice": "σmax = 1,8 × 140.",
             "pieges": [(350, "350, c'est l'ancien Kt (2,5). Le congé fait baisser Kt à 1,8.")],
             "aide": "1,8 × 140 = 252 MPa < 270 MPa : la pièce tient."},''',
  '''             "unite": "MPa", "attendu": 234, "tol": 1,
             "consigne": "On remplace la gorge par un congé de grand rayon (Kt = 1,8). Calcule σmax.",
             "indice": "σmax = 1,8 × 130.",
             "pieges": [(325, "325, c'est l'ancien Kt (2,5). Le congé fait baisser Kt à 1,8.")],
             "aide": "1,8 × 130 = 234 MPa < 270 MPa : la pièce tient."},''')
R('''             "unite": "", "attendu": 1.071, "tol": 0.005,
             "consigne": "Calcule le rapport σD / σmax avec le congé.",
             "indice": "270 / 252.",
             "pieges": [(0.933, "0,933 : rapport inversé. La marge, c'est σD / σmax.")],
             "aide": "270 / 252 ≈ 1,07 : la pièce tient, mais de justesse."},''',
  '''             "unite": "", "attendu": 1.154, "tol": 0.005,
             "consigne": "Calcule le rapport σD / σmax avec le congé.",
             "indice": "270 / 234.",
             "pieges": [(0.867, "0,867 : rapport inversé. La marge, c'est σD / σmax.")],
             "aide": "270 / 234 ≈ 1,15 : la pièce tient, avec une marge encore faible."},''')
R('''            "enonce": "σnom = 140 MPa alternée, σD de la pièce = 270 MPa ; gorge vive Kt = 2,5, puis congé Kt = 1,8.",''',
  '''            "enonce": "σnom = 130 MPa alternée, σD de la pièce = 270 MPa ; gorge à petit rayon Kt = 2,5, puis congé Kt = 1,8.",''')
R('''            "remplacement": "2,5 × 140 ; 1,8 × 140 ; 270 / 252.",
            "calcul": "**350 MPa** (refusé) → **252 MPa** (accepté) ; marge **1,07**.",''',
  '''            "remplacement": "2,5 × 130 ; 1,8 × 130 ; 270 / 234.",
            "calcul": "**325 MPa** (refusé) → **234 MPa** (accepté) ; marge **1,15**.",''')
R('''        "enonce": "Essai Charpy : le mouton, de masse 20 kg, est lâché d'une hauteur de 1,5 m et remonte à 1,3 m après "
                  "rupture (données d'énoncé ; g = 9,81 m/s² ; frottements négligés). La passerelle doit rester sûre "
                  "jusqu'à −15 °C.",''',
  '''        "enonce": "Essai Charpy : le mouton, de masse 25 kg, est lâché d'une hauteur de 1,5 m et remonte à 1,32 m après "
                  "rupture (données d'énoncé ; g = 9,81 m/s² ; frottements négligés). La passerelle doit rester sûre "
                  "jusqu'à −15 °C.",''')
R('''             "unite": "J", "attendu": 39.24, "tol": 0.1,
             "consigne": "Calcule KV = m × g × (h0 − h1).",
             "indice": "h0 − h1 = 0,2 m.",
             "pieges": [(294.3, "294,3 J : c'est m g h0, l'énergie de départ. Ce qui compte, c'est ce que le mouton a "
                                "perdu : h0 − h1."),
                        (4, "4 : tu as oublié g. KV = m × g × Δh.")],
             "aide": "20 × 9,81 × 0,2 ≈ 39,2 J."},''',
  '''             "unite": "J", "attendu": 44.145, "tol": 0.1,
             "consigne": "Calcule KV = m × g × (h0 − h1).",
             "indice": "h0 − h1 = 0,18 m.",
             "pieges": [(367.88, "367,9 J : c'est m g h0, l'énergie de départ. Ce qui compte, c'est ce que le mouton a "
                                 "perdu : h0 − h1."),
                        (323.73, "323,7 J, c'est l'énergie restante à la remontée (m g h1) ; l'énergie absorbée est la "
                                 "différence."),
                        (4.5, "4,5 : tu as oublié g. KV = m × g × Δh.")],
             "aide": "25 × 9,81 × 0,18 ≈ 44,1 J."},''')
R('''             "question": "KV ≈ 39 J à la température d'essai. Que peut-on conclure ?",
             "options": ["L'acier est sûr à toutes les températures",
                         "Il dépasse 27 J à la température d'essai, et seulement à celle-là",
                         "Il est fragile"], "bonne": 1,''',
  '''             "question": "KV ≈ 44 J à la température d'essai. Que peut-on conclure ?",
             "options": ["L'acier est sûr à toutes les températures",
                         "Il dépasse 27 J à la température d'essai ; on ne peut rien en conclure pour une température plus basse",
                         "Il est fragile"], "bonne": 1,''')
R('''             "diagnostics": {0: "Non : sous la zone de transition, l'énergie absorbée chute. Un Charpy ne vaut qu'à sa "
                                 "température d'essai.",
                             2: "39 J dépassent le niveau de 27 J : à cette température, la rupture absorbe assez "
                                "d'énergie."}},''',
  '''             "diagnostics": {0: "Non : sous la zone de transition, l'énergie absorbée chute. Un Charpy ne renseigne pas "
                                 "sur les températures plus basses que celle de l'essai.",
                             2: "44 J dépassent le niveau de 27 J : à cette température, la rupture absorbe assez "
                                "d'énergie."}},''')
R('''            "enonce": "Mouton 20 kg, h0 = 1,5 m, h1 = 1,3 m ; service jusqu'à −15 °C.",''',
  '''            "enonce": "Mouton 25 kg, h0 = 1,5 m, h1 = 1,32 m ; service jusqu'à −15 °C.",''')
R('''            "remplacement": "KV = 20 × 9,81 × 0,2.",
            "calcul": "**KV ≈ 39,2 J** ; qualité **S355J2**.",''',
  '''            "remplacement": "KV = 25 × 9,81 × 0,18.",
            "calcul": "**KV ≈ 44,1 J** ; qualité **S355J2**.",''')
R('''            ("Résilience (KV)",
             "l'énergie absorbée par la rupture d'une éprouvette entaillée en V, mesurée à l'essai Charpy (ISO 148-1)."),''',
  '''            ("Résilience (KV)",
             "l'aptitude à encaisser un choc : l'énergie absorbée par la rupture d'une éprouvette entaillée en V, "
             "mesurée en joules à l'essai Charpy (ISO 148-1)."),''')

# ---------------------------------------------------------------- générateurs et quiz
R('''    b = random.choice([4, 5, 6, 8, 10])
    h = random.choice([3, 4, 5, 6])
    L = random.choice([30, 40, 50, 60, 80])
    F = random.choice([100, 150, 200, 250, 400, 500])''',
  '''    b = random.choice([6, 8, 10])
    h = random.choice([4, 5, 6])
    L = random.choice([30, 40, 50, 60])
    F = random.choice([100, 150, 200, 250, 300, 400])''')
R('''            (F * L / (4 * b * h ** 2), "Il manque le module de flexion b h² / 6 : σ = M / (b h² / 6), avec M = F L / 4."),''',
  '''            (F * L / (4 * b * h ** 2), "Tu as divisé M par b h² : le module de flexion vaut b h² / 6, donc σ = (F L / 4) "
                                      "× 6 / (b h²)."),''')
R('''     ["Il durcit tout le cœur de la pièce", "Il augmente la limite élastique du matériau",''',
  '''     ["Il durcit tout le cœur de la pièce", "Il augmente la limite élastique de toute la pièce",''')
R('''    ("Une structure en acier doit rester sûre jusqu'à −15 °C. Quelle qualité choisir parmi JR, J0, J2 ?",
     ["JR", "J0", "N'importe laquelle : 27 J dans tous les cas", "J2"], 3,
     "27 J sont garantis à +20 °C (JR), 0 °C (J0), −20 °C (J2). Seule J2 couvre −15 °C.", "Piège"),''',
  '''    ("Une structure en acier doit rester sûre jusqu'à −5 °C. Quelle qualité choisir parmi JR, J0, J2 ?",
     ["JR", "J0", "N'importe laquelle : 27 J dans tous les cas", "J2"], 3,
     "27 J sont garantis à +20 °C (JR), 0 °C (J0), −20 °C (J2). −5 °C est plus froid que 0 °C : seule J2 couvre "
     "−5 °C.", "Piège"),''')

open(F, 'w', encoding='utf-8').write(c)
print("corrigé")
