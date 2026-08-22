# -*- coding: utf-8 -*-
"""Banque de quiz BTS CPI. Chaque question : énoncé, options, index correct, explication."""


def q(txt, options, correct, expl, niveau="Base"):
    return {"question": txt, "options": options, "correct": correct,
            "explication": expl, "niveau": niveau}


QUIZ = {

    # =====================================================================
    "RDM — Notions de base": [
        q("Que vaut 1 MPa exprimé en unités de base de la mécanique ?",
          ["1 N/m²", "1 N/mm²", "1 kN/mm²", "1 N/cm²"], 1,
          "1 MPa = 1 N/mm². C'est LA conversion à connaître : en travaillant en newtons et en "
          "millimètres, la contrainte sort directement en MPa, sans conversion.",
          "Base"),

        q("La limite élastique Re représente :",
          ["La contrainte de rupture de la pièce",
           "La contrainte au-delà de laquelle la déformation devient permanente",
           "La rigidité du matériau",
           "L'allongement maximal avant rupture"], 1,
          "Re marque la frontière entre le domaine élastique (déformation réversible) et le "
          "domaine plastique (déformation permanente). C'est LA valeur de dimensionnement : on "
          "reste toujours en dessous. Rm est la contrainte de rupture, E la rigidité, A% "
          "l'allongement.",
          "Base"),

        q("Deux barres identiques, l'une en S235 (Re = 235 MPa), l'autre en 42CrMo4 "
          "(Re = 750 MPa). Sous la même charge de traction, laquelle s'allonge le plus ?",
          ["Le S235, car il est moins résistant",
           "Le 42CrMo4",
           "Les deux s'allongent exactement pareil",
           "Impossible à dire sans connaître la section"], 2,
          "PIÈGE CLASSIQUE. L'allongement dépend du module de Young E, pas de Re. "
          "Or TOUS les aciers ont E ≈ 210 GPa. Les deux barres s'allongent donc identiquement. "
          "Le 42CrMo4 supporte simplement une charge bien plus élevée avant de plastifier. "
          "Retenir : E = rigidité, Re = résistance. Ce sont deux propriétés indépendantes.",
          "Piège"),

        q("La formule de la contrainte en traction simple est :",
          ["σ = F × S", "σ = F / S", "σ = S / F", "σ = F × L / S"], 1,
          "σ = N/S. La contrainte est un effort RAPPORTÉ à une surface. Plus la section est "
          "grande, plus la contrainte est faible pour un même effort.",
          "Base"),

        q("Un coefficient de sécurité s = 3 signifie que :",
          ["La pièce peut supporter 3 fois la charge de service",
           "La contrainte admissible vaut Re/3",
           "La pièce a 3 chances sur 4 de tenir",
           "Les réponses A et B sont toutes deux correctes"], 3,
          "Rpe = Re/s = Re/3. Comme la contrainte est proportionnelle à la charge, dire que la "
          "contrainte admissible est divisée par 3 revient à dire que la pièce tiendrait 3 fois "
          "la charge avant d'atteindre Re. Les deux formulations sont équivalentes.",
          "Base"),

        q("Dans un calcul de traction sur une pièce percée, quelle section faut-il utiliser ?",
          ["La section brute, toujours",
           "La section nette (au droit du trou)",
           "La moyenne des deux",
           "La section du trou"], 1,
          "On calcule TOUJOURS au droit de la section la plus faible, donc la section nette "
          "(section brute moins la matière enlevée par le trou). En fatigue, il faut en plus "
          "appliquer le coefficient de concentration de contrainte Kt.",
          "Intermédiaire"),

        q("Une barre de 2 000 mm en acier (E = 210 GPa), section 500 mm², est tirée par 40 kN. "
          "Quel est son allongement ?",
          ["0,38 mm", "0,76 mm", "1,52 mm", "3,80 mm"], 1,
          "ΔL = N·L/(E·S) = 40 000 × 2 000 / (210 000 × 500) = 80 000 000 / 105 000 000 "
          "= 0,762 mm. Attention à exprimer E en MPa (210 000) et non en GPa.",
          "Calcul"),

        q("Le flambage concerne :",
          ["Les pièces en traction", "Les pièces élancées en compression",
           "Les pièces en torsion", "Les pièces en flexion pure"], 1,
          "Le flambage est une INSTABILITÉ GÉOMÉTRIQUE des pièces élancées comprimées : la pièce "
          "s'incurve brutalement latéralement avant d'atteindre Re. Une pièce en traction ne "
          "flambe jamais (elle se redresse).",
          "Base"),

        q("La charge critique de flambage d'Euler dépend :",
          ["De Re du matériau", "De E et du moment quadratique I",
           "De Rm uniquement", "De la section S uniquement"], 1,
          "Fc = π²EI/Lf². Elle ne dépend PAS de Re ! Changer de nuance d'acier ne change rien au "
          "flambage (E identique pour tous les aciers). Seule la géométrie (I) et la longueur "
          "libre agissent. C'est pourquoi on utilise des tubes plutôt que des barres pleines.",
          "Piège"),

        q("Pour une même masse, quelle section résiste le mieux au flambage ?",
          ["Une barre pleine", "Un tube", "Un profil plat", "C'est identique"], 1,
          "Le tube. À section (donc masse) égale, le tube a un moment quadratique I bien plus "
          "grand car la matière est éloignée de l'axe neutre, et I varie en d⁴. C'est le même "
          "principe qui explique les os creux, les cadres de vélo et les mâts d'éclairage.",
          "Intermédiaire"),
    ],

    # =====================================================================
    "RDM — Cisaillement et torsion": [
        q("Un axe monté dans une chape (entre deux flasques) travaille en :",
          ["Cisaillement simple", "Cisaillement double", "Traction", "Torsion"], 1,
          "Cisaillement DOUBLE : le plan de coupe traverse l'axe en DEUX endroits (entre chaque "
          "flasque et la pièce centrale). La formule devient τ = T/(2S). Oublier le facteur 2 "
          "conduit à surdimensionner l'axe d'environ 40 %.",
          "Base"),

        q("La contrainte en torsion est maximale :",
          ["Au centre de l'arbre", "À la périphérie de l'arbre",
           "À mi-rayon", "Uniformément répartie"], 1,
          "τ = Mt·ρ/I0 : la contrainte croît linéairement avec le rayon ρ. Elle est NULLE au "
          "centre et MAXIMALE à la périphérie. C'est pourquoi la matière centrale ne sert "
          "presque à rien, et pourquoi les arbres creux sont si efficaces.",
          "Base"),

        q("Pourquoi les arbres de transmission sont-ils toujours de section circulaire ?",
          ["Pour des raisons esthétiques",
           "Parce que la théorie de la torsion n'est valable que pour les sections circulaires",
           "Parce que c'est moins cher à usiner",
           "Pour équilibrer les masses"], 1,
          "Pour une section non circulaire, les sections droites GAUCHISSENT sous l'effet de la "
          "torsion et l'hypothèse de Navier-Bernoulli tombe : la théorie simple ne s'applique "
          "plus. La section circulaire est la seule où les sections restent planes.",
          "Intermédiaire"),

        q("Un moteur de 11 kW tourne à 1 500 tr/min. Quel couple transmet-il ?",
          ["70 N·m", "7,3 N·m", "700 N·m", "165 N·m"], 0,
          "ω = 2π×1500/60 = 157,1 rad/s. Mt = P/ω = 11 000/157,1 = 70,0 N·m. "
          "Attention : pour l'utiliser en calcul de contrainte (en mm), multiplier par 1000 "
          "→ 70 000 N·mm.",
          "Calcul"),

        q("Pour un axe cisaillé, on retient couramment Reg (résistance au glissement) égal à :",
          ["Re", "0,5 à 0,7 × Re", "2 × Re", "Rm"], 1,
          "Reg ≈ 0,5 Re pour les aciers doux, 0,6 Re pour les aciers alliés. La résistance au "
          "cisaillement est toujours inférieure à la résistance en traction. En l'absence "
          "d'indication de l'énoncé, préciser l'hypothèse retenue en copie.",
          "Base"),

        q("En dimensionnant un axe de chape, quelle vérification complémentaire au cisaillement "
          "faut-il TOUJOURS faire ?",
          ["Le flambage", "Le matage", "La torsion", "La fatigue thermique"], 1,
          "Le MATAGE : p = F/(d·e). L'axe peut résister au cisaillement mais écraser localement "
          "les alésages des pièces qu'il traverse, surtout si elles sont minces ou en matériau "
          "tendre (fonte, alu, polymère). Les deux vérifications sont indissociables.",
          "Intermédiaire"),

        q("L'angle de torsion d'un arbre est proportionnel à :",
          ["Mt × L / (G × I0)", "Mt × I0 / (G × L)",
           "G × I0 / (Mt × L)", "Mt × G / (L × I0)"], 0,
          "θ = Mt·L/(G·I0), en radians. L'angle croît avec le couple et la longueur, et décroît "
          "avec la rigidité en torsion G·I0. Sur les arbres longs, c'est souvent ce critère de "
          "rigidité — et non la résistance — qui dimensionne.",
          "Base"),

        q("Un arbre de transmission long résiste (τ < Rpg) mais tourne de 3°/m. Que conclure ?",
          ["Tout va bien, la résistance est vérifiée",
           "Il faut changer de matériau pour un acier plus résistant",
           "La condition de rigidité n'est pas satisfaite, il faut augmenter le diamètre",
           "Il faut réduire le couple"], 2,
          "La résistance et la rigidité sont DEUX conditions distinctes, à vérifier toutes les "
          "deux. Sur les arbres longs, la rigidité est presque toujours dimensionnante. Changer "
          "de nuance ne sert à rien (G identique pour tous les aciers) : il faut augmenter I0, "
          "donc le diamètre — ou fractionner l'arbre avec un palier intermédiaire.",
          "Piège"),
    ],

    # =====================================================================
    "RDM — Flexion": [
        q("Dans une poutre en flexion, la fibre neutre :",
          ["Subit la contrainte maximale", "Ne subit aucune contrainte normale",
           "Est toujours en compression", "Est toujours en traction"], 1,
          "La fibre neutre passe par le centre de gravité de la section et n'y subit AUCUNE "
          "contrainte normale (σ = Mf·y/I avec y = 0). C'est la raison pour laquelle on évide "
          "les poutres en leur centre : poutres en I, en U, tubes, caissons.",
          "Base"),

        q("Une poutre rectangulaire 40×80 posée sur chant (h = 80) est plus rigide que la même "
          "posée à plat (h = 40) d'un facteur :",
          ["2", "4", "8", "16"], 1,
          "I = bh³/12. Sur chant : 40×80³/12 = 1 706 667 mm⁴. À plat : 80×40³/12 = 426 667 mm⁴. "
          "Rapport = 4. La flèche étant inversement proportionnelle à I, elle est divisée par 4. "
          "Même matière, même masse, 4 fois plus rigide : c'est gratuit.",
          "Calcul"),

        q("La flèche d'une console chargée en bout varie en fonction de la longueur selon :",
          ["L", "L²", "L³", "L⁴"], 2,
          "f = FL³/(3EI). Doubler le porte-à-faux multiplie la flèche par 8 ! C'est le paramètre "
          "le plus sensible de toute la RDM. Face à un problème de flèche, le premier réflexe "
          "doit être : puis-je raccourcir la portée ?",
          "Base"),

        q("Pour réduire la flèche d'une poutre en acier, quelle solution est INEFFICACE ?",
          ["Augmenter la hauteur de la section",
           "Réduire la portée",
           "Remplacer le S235 par du 42CrMo4",
           "Passer d'une section pleine à un profilé en I de même masse"], 2,
          "PIÈGE MAJEUR. La flèche dépend de E·I. Tous les aciers ont E ≈ 210 GPa : changer de "
          "nuance ne change RIEN à la flèche. Il faut agir sur la géométrie (I) ou sur la "
          "portée (L). Un acier plus résistant permet simplement de supporter plus de charge "
          "avant plastification.",
          "Piège"),

        q("Le moment fléchissant maximal d'une poutre sur 2 appuis, charge F au milieu, vaut :",
          ["FL", "FL/2", "FL/4", "FL/8"], 2,
          "Mf max = FL/4, situé au milieu de la poutre (là où l'effort tranchant s'annule). "
          "À comparer avec la console : Mf = FL, soit 4 fois plus pour la même charge et la "
          "même longueur. L'encastrement est bien plus sollicité.",
          "Base"),

        q("Sur un arbre soumis à flexion ET torsion, on calcule le moment idéal de Tresca :",
          ["Mi = Mf + Mt", "Mi = √(Mf² + Mt²)",
           "Mi = √(Mf² + 0,75 Mt²)", "Mi = Mf × Mt"], 1,
          "Tresca : Mi = √(Mf² + Mt²). Von Mises donne √(Mf² + 0,75Mt²), légèrement moins "
          "conservatif. On dimensionne ensuite comme en flexion pure avec ce moment idéal. "
          "Sur un arbre de réducteur, Mf domine généralement Mt.",
          "Intermédiaire"),

        q("Une poutre bi-encastrée chargée au milieu a une flèche combien de fois plus faible "
          "qu'une poutre sur appuis simples ?",
          ["2 fois", "4 fois", "8 fois", "16 fois"], 1,
          "Appuis simples : f = FL³/(48EI). Bi-encastrée : f = FL³/(192EI). "
          "Rapport 192/48 = 4. L'encastrement est un levier de rigidification très puissant "
          "et souvent négligé en conception.",
          "Calcul"),
    ],

    # =====================================================================
    "Matériaux — Désignation": [
        q("Que signifie la désignation S355 ?",
          ["Acier à 3,55 % de carbone", "Acier de construction de limite élastique 355 MPa",
           "Acier allié à 355 % ... impossible", "Acier de résistance à la rupture 355 MPa"], 1,
          "Pour les aciers d'usage général (S, E, P, L), le nombre donne directement la LIMITE "
          "ÉLASTIQUE Re en MPa. S = Structural (construction), E = Engineering (mécanique).",
          "Base"),

        q("Que signifie la désignation C45 ?",
          ["45 % de carbone", "0,45 % de carbone", "Re = 45 MPa", "Résistance 450 MPa"], 1,
          "Aciers non alliés spéciaux : C suivi de (%C × 100). Donc C45 = 0,45 % de carbone. "
          "C'est l'acier le plus utilisé en mécanique générale (arbres, axes, engrenages).",
          "Base"),

        q("Dans 42CrMo4, que représente le chiffre 4 en fin de désignation ?",
          ["4 % de molybdène", "1 % de chrome (4 divisé par le facteur 4)",
           "4 % de chrome", "La classe de résistance"], 1,
          "Aciers faiblement alliés : la teneur se lit avec un facteur multiplicateur. Pour Cr, "
          "Co, Mn, Ni, Si, W le facteur est 4. Le chiffre 4 se rapporte au PREMIER élément cité "
          "(Cr) : 4/4 = 1 % de chrome. Le Mo est en faible teneur non chiffrée (≈ 0,2 %).",
          "Intermédiaire"),

        q("Que signifie le X au début de X5CrNi18-10 ?",
          ["Acier expérimental", "Acier fortement allié (teneurs en % réel)",
           "Acier extra-dur", "Acier pour exportation"], 1,
          "Le X indique un acier FORTEMENT allié (au moins un élément ≥ 5 %). Les teneurs sont "
          "alors données en pourcentage RÉEL, sans facteur : 18 % Cr et 10 % Ni. C'est l'inox "
          "austénitique 304.",
          "Base"),

        q("Quel est le seuil de carbone au-delà duquel la soudabilité devient problématique ?",
          ["0,10 %", "0,25 %", "0,45 %", "0,60 %"], 1,
          "0,25 % de carbone. Au-delà, la zone affectée thermiquement trempe spontanément en "
          "refroidissant, formant de la martensite fragile → risque de fissuration à froid. "
          "Préchauffage obligatoire. C'est pourquoi on ne soude pas un C45 ni un 42CrMo4.",
          "Intermédiaire"),

        q("EN-GJL-250 désigne :",
          ["Une fonte à graphite sphéroïdal de Rm = 250 MPa",
           "Une fonte à graphite lamellaire de Rm = 250 MPa",
           "Un acier moulé", "Un alliage d'aluminium"], 1,
          "GJ = fonte, L = graphite Lamellaire (S = Sphéroïdal, M = Malléable), 250 = Rm en MPa. "
          "La fonte grise est fragile (A ≈ 0) mais AMORTIT remarquablement les vibrations : "
          "d'où son emploi pour les bâtis de machines-outils.",
          "Base"),

        q("Dans EN AW-6082 T6, que signifie le premier chiffre 6 ?",
          ["6 % de magnésium", "Famille Al-Mg-Si (série 6xxx)",
           "6e génération", "Dureté 6 HB"], 1,
          "Le premier chiffre donne la famille : 1xxx = Al pur, 2xxx = Cu, 3xxx = Mn, "
          "5xxx = Mg, 6xxx = Mg+Si (profilés extrudés), 7xxx = Zn (haute résistance). "
          "T6 = trempé + revenu, l'état de résistance maximale.",
          "Intermédiaire"),

        q("Quel acier choisir pour un pignon d'engrenage devant avoir une peau très dure et un "
          "cœur tenace ?",
          ["C45 trempé à cœur", "16MnCr5 cémenté trempé",
           "S235 nu", "X5CrNi18-10"], 1,
          "16MnCr5 (0,16 % C) : la CÉMENTATION enrichit la peau en carbone (0,8 %) qui trempe à "
          "60 HRC, tandis que le cœur à 0,16 % C reste tenace (30 HRC) et encaisse les chocs. "
          "Un acier dur à cœur (C45 trempé) casserait net sous les chocs de transmission.",
          "Intermédiaire"),
    ],

    # =====================================================================
    "Matériaux — Propriétés et choix": [
        q("Le module de Young E de l'acier vaut environ :",
          ["70 GPa", "110 GPa", "210 GPa", "400 GPa"], 2,
          "E(acier) ≈ 210 GPa = 210 000 MPa. À comparer : aluminium 70 GPa (3 fois moins "
          "rigide), fonte grise 110 GPa, polymères 1 à 3,5 GPa. C'est une valeur à connaître "
          "par cœur.",
          "Base"),

        q("Comparé à l'acier, l'aluminium est :",
          ["3 fois plus léger et 3 fois plus rigide",
           "3 fois plus léger et 3 fois moins rigide",
           "3 fois plus lourd et plus rigide",
           "De masse et rigidité équivalentes"], 1,
          "ρ = 2700 contre 7850 kg/m³ (≈ 3× plus léger) et E = 70 contre 210 GPa (≈ 3× moins "
          "rigide). Conséquence remarquable : à MASSE ÉGALE, une barre alu et une barre acier "
          "ont la MÊME raideur en traction (E/ρ identique). En flexion, l'alu devient supérieur.",
          "Intermédiaire"),

        q("Pour concevoir une poutre légère ET rigide en flexion, quel indice maximiser ?",
          ["Re/ρ", "E/ρ", "E^(1/2)/ρ", "Rm × ρ"], 2,
          "Pour la flexion, l'indice de performance est E^(1/2)/ρ. C'est ce qui explique la "
          "supériorité de l'aluminium en flexion malgré son E trois fois plus faible : à masse "
          "égale on peut lui donner une section plus épaisse, et I croît en h³.",
          "Avancé"),

        q("Un allongement à la rupture A = 45 % indique un matériau :",
          ["Très fragile", "Très ductile", "Très dur", "Très rigide"], 1,
          "A% mesure la DUCTILITÉ. 45 % (cas de l'inox 304) est très élevé : le matériau se "
          "déforme énormément avant de rompre, ce qui donne un avertissement visible. À "
          "l'opposé, la fonte grise (A ≈ 0,5 %) casse net, sans prévenir.",
          "Base"),

        q("Quelle est la relation empirique entre dureté Brinell et résistance des aciers ?",
          ["Rm ≈ HB", "Rm ≈ 3,3 × HB", "Rm ≈ 10 × HB", "Rm ≈ HB/3"], 1,
          "Rm ≈ 3,3 × HB (en MPa). Un acier à 200 HB a donc un Rm d'environ 660 MPa. Cette "
          "relation permet d'estimer rapidement la résistance d'une pièce à partir d'un simple "
          "essai de dureté, non destructif.",
          "Intermédiaire"),

        q("Pourquoi le bronze est-il utilisé pour les coussinets ?",
          ["Il est très résistant", "Il a un faible coefficient de frottement contre l'acier",
           "Il est très léger", "Il est bon marché"], 1,
          "Le bronze offre un faible coefficient de frottement contre l'acier et tolère un "
          "défaut de lubrification. Il est aussi SACRIFICIEL : c'est le coussinet qui s'use, "
          "pas l'arbre — et on remplace une bague à quelques euros plutôt qu'un arbre usiné.",
          "Base"),

        q("Une pièce imprimée en 3D (FDM) sollicitée en flexion doit être orientée :",
          ["Peu importe, le matériau est isotrope",
           "Debout, pour minimiser les supports",
           "Couchée, pour que les couches soient parallèles aux contraintes de traction",
           "À 45° systématiquement"], 2,
          "Une pièce FDM est fortement ANISOTROPE : σZ ≈ 0,3 à 0,5 × σXY. La liaison entre "
          "couches est une soudure thermique partielle, bien plus faible que le filament "
          "continu. Il faut donc orienter la pièce pour que les contraintes de traction soient "
          "DANS le plan des couches, jamais perpendiculaires.",
          "Avancé"),
    ],

    # =====================================================================
    "Matériaux — Traitements": [
        q("À partir de quelle teneur en carbone un acier peut-il être trempé efficacement ?",
          ["0,05 %", "0,15 %", "0,30 %", "0,80 %"], 2,
          "Environ 0,30 % de carbone. En dessous, il n'y a pas assez de carbone pour former "
          "suffisamment de martensite : un S235 (0,15 % C) ne trempe pas. C'est pourquoi les "
          "pièces à tremper sont en C45, C60, 42CrMo4, etc.",
          "Intermédiaire"),

        q("Après une trempe, pourquoi effectue-t-on systématiquement un revenu ?",
          ["Pour augmenter encore la dureté",
           "Pour perdre un peu de dureté et regagner beaucoup de ténacité",
           "Pour changer la couleur de la pièce",
           "Pour améliorer l'usinabilité"], 1,
          "Après trempe, la martensite est très dure mais TRÈS FRAGILE et sous contraintes "
          "internes : la pièce est inutilisable telle quelle. Le revenu détend la structure : "
          "on perd un peu de dureté pour regagner beaucoup de ténacité. L'ensemble s'appelle "
          "trempe revenu ou amélioration.",
          "Base"),

        q("Quel traitement permet de durcir la surface SANS déformer la pièce ?",
          ["Cémentation", "Trempe à l'huile", "Nitruration", "Recuit"], 2,
          "La NITRURATION s'effectue à 500-520 °C, SANS trempe : il n'y a donc pas de "
          "déformation. La pièce peut être usinée et rectifiée aux cotes finales AVANT "
          "traitement. C'est son avantage décisif sur la cémentation, qui exige une trempe et "
          "donc une rectification après traitement.",
          "Intermédiaire"),

        q("Dans la gamme d'un pignon cémenté, à quel moment taille-t-on la denture ?",
          ["Après la cémentation et la trempe", "Avant la cémentation, sur acier tendre",
           "Pendant le traitement thermique", "Après la rectification"], 1,
          "On usine TENDRE, on traite, puis on rectifie. Tailler une denture dans un acier à "
          "60 HRC exigerait des outils CBN, un temps de cycle multiplié par 10, pour un "
          "résultat médiocre. L'ordre des opérations en traitement thermique n'est jamais "
          "négociable.",
          "Intermédiaire"),

        q("Le chromage dur sur une tige de vérin apporte principalement :",
          ["Uniquement une protection anticorrosion",
           "Uniquement de la dureté",
           "Dureté + anticorrosion + faible frottement",
           "Une meilleure soudabilité"], 2,
          "Le chromage dur (1000 HV, 20-50 µm) apporte simultanément trois fonctions : barrière "
          "anticorrosion, dureté superficielle contre l'abrasion, et faible coefficient de "
          "frottement (0,15 contre 0,6 acier/acier sec) qui compense l'absence de graissage.",
          "Intermédiaire"),

        q("Quel est le principal risque associé à une trempe sur une pièce à sections variables ?",
          ["Une perte de masse", "Des tapures de trempe (fissures)",
           "Une oxydation", "Une perte de dureté"], 1,
          "Les sections épaisses et minces refroidissent à des vitesses différentes, créant des "
          "contraintes internes qui peuvent fissurer la pièce : ce sont les TAPURES DE TREMPE. "
          "D'où la règle de conception : éviter les variations brutales de section sur une "
          "pièce destinée à être trempée.",
          "Avancé"),
    ],

    # =====================================================================
    "Ajustements ISO": [
        q("Dans la désignation Ø20 H7, que représente le chiffre 7 ?",
          ["La position de la zone de tolérance", "Le grade, donc la largeur de l'IT",
           "Le nombre de pièces", "L'écart supérieur en µm"], 1,
          "Le CHIFFRE (grade IT) donne la LARGEUR de la zone de tolérance. La LETTRE donne sa "
          "POSITION par rapport à la ligne zéro. Aide-mémoire : lettre = position, chiffre = "
          "largeur.",
          "Base"),

        q("Une lettre MAJUSCULE dans un ajustement désigne :",
          ["Un arbre", "Un alésage", "Une pièce importante", "Une cote critique"], 1,
          "Convention absolue : MAJUSCULES = ALÉSAGE (le contenant, la partie femelle, le trou). "
          "minuscules = arbre (le contenu, la partie mâle). Vrai pour les lettres de position "
          "(H/h) comme pour les écarts (ES/es, EI/ei).",
          "Base"),

        q("Pour un alésage H, quel est l'écart inférieur EI ?",
          ["EI = +IT", "EI = 0", "EI = -IT/2", "EI = -IT"], 1,
          "H est l'ALÉSAGE NORMAL : par définition EI = 0, donc ES = +IT. L'alésage est toujours "
          "supérieur ou égal à la cote nominale. Symétriquement, h est l'arbre normal : es = 0.",
          "Base"),

        q("Comment calcule-t-on le jeu maximal d'un ajustement ?",
          ["Jmax = ES - ei", "Jmax = EI - es", "Jmax = ES - es", "Jmax = EI - ei"], 0,
          "Jmax = ES - ei : le plus GRAND alésage avec le plus PETIT arbre. Et Jmin = EI - es : "
          "le plus petit alésage avec le plus gros arbre. Ce sont les deux formules à connaître "
          "par cœur.",
          "Base"),

        q("Un ajustement où Jmin < 0 < Jmax est dit :",
          ["Avec jeu", "Avec serrage", "Incertain", "Impossible"], 2,
          "INCERTAIN : selon les pièces réellement usinées, on peut obtenir du jeu ou du "
          "serrage. Exemples : H7/k6, H7/m6, H7/js6. Utilisé pour un positionnement précis avec "
          "montage au maillet ou à la presse légère.",
          "Base"),

        q("Pourquoi utilise-t-on majoritairement le système de l'alésage normal (H) ?",
          ["Par tradition",
           "Parce qu'un alésage est plus difficile et coûteux à ajuster qu'un arbre",
           "Parce que c'est plus précis",
           "Parce que la norme l'impose"], 1,
          "Un arbre se retouche facilement au tour (quelques centièmes de passe). Un alésage "
          "exige un alésoir dédié — un par cote. En travaillant en H, l'atelier n'a besoin que "
          "de quelques alésoirs standards et adapte l'arbre. C'est purement économique.",
          "Intermédiaire"),

        q("Quel ajustement choisir pour la bague INTÉRIEURE d'un roulement sur un arbre tournant, "
          "avec une charge fixe en direction ?",
          ["H7/g6 (jeu)", "Arbre en k6 (serrage léger)",
           "H11/c11 (jeu large)", "H7/f7 (jeu)"], 1,
          "La bague intérieure subit une CHARGE TOURNANTE (chaque point passe sous la zone "
          "chargée) : elle doit être SERRÉE, sinon elle rampe et use l'arbre. L'arbre est donc "
          "en k6. La bague extérieure, en charge fixe, reçoit un alésage H7 (jeu léger).",
          "Intermédiaire"),

        q("Ø30 H7 sur la tranche 18-30 mm (IT7 = 21 µm). Quelles sont les cotes limites ?",
          ["29,979 à 30,000", "30,000 à 30,021", "29,990 à 30,010", "30,021 à 30,042"], 1,
          "H → EI = 0 → ES = +21 µm = +0,021 mm. Donc l'alésage est compris entre 30,000 et "
          "30,021 mm. Attention : la tranche 18-30 inclut la borne 30 (borne inférieure exclue, "
          "supérieure incluse).",
          "Calcul"),

        q("On passe une cote de f7 à f8. Quelle borne change ?",
          ["La borne supérieure uniquement", "La borne inférieure uniquement",
           "Les deux bornes", "Aucune"], 1,
          "L'écart fondamental (es = -20 µm pour f) dépend UNIQUEMENT DE LA LETTRE, jamais du "
          "grade. En passant de f7 à f8, es reste à -20 µm : seule la borne inférieure "
          "(ei = es - IT) descend. Élargir le grade ne récupère donc pas une pièce trop grosse.",
          "Piège"),

        q("H7/p6 est un ajustement :",
          ["Avec jeu", "Incertain", "Avec serrage", "Impossible à réaliser"], 2,
          "p est situé au-dessus de la ligne zéro avec un écart fondamental important "
          "(ei = +22 µm sur Ø20-30) supérieur à l'ES de l'alésage H7 (+21 µm). L'arbre est donc "
          "toujours plus gros : serrage garanti. Montage à la presse ou par dilatation.",
          "Intermédiaire"),
    ],

    # =====================================================================
    "Lecture de plan et cotation": [
        q("En méthode du premier dièdre (européenne), où place-t-on la vue de gauche ?",
          ["À gauche de la vue de face", "À droite de la vue de face",
           "Au-dessus", "En dessous"], 1,
          "Premier dièdre : la vue se place du côté OPPOSÉ au regard. Si je regarde la pièce "
          "par la gauche, je dessine cette vue à DROITE de la vue de face. C'est l'inverse de "
          "la méthode américaine (troisième dièdre).",
          "Base"),

        q("Dans une coupe longitudinale, une vis est représentée :",
          ["Coupée et hachurée", "Non coupée",
           "Coupée mais non hachurée", "En traits interrompus"], 1,
          "Les pièces pleines (vis, écrous, rondelles, goupilles, clavettes, rivets, billes, "
          "arbres pleins) ne sont JAMAIS coupées longitudinalement : elles n'ont pas de forme "
          "intérieure à révéler. En revanche, si le plan est perpendiculaire à leur axe, elles "
          "sont coupées et hachurées normalement.",
          "Intermédiaire"),

        q("Sur un dessin à l'échelle 2:1, une cote de Ø20 signifie que la pièce mesure :",
          ["10 mm", "20 mm", "40 mm", "Cela dépend du format"], 1,
          "Les cotes portées sur un dessin sont TOUJOURS les dimensions RÉELLES de la pièce. "
          "L'échelle ne modifie jamais les valeurs inscrites : elle ne concerne que la taille "
          "du tracé sur le papier (ici, 40 mm mesurés à la règle).",
          "Piège"),

        q("Quel mode de cotation évite le cumul des tolérances ?",
          ["Cotation à la chaîne (en série)", "Cotation en parallèle (depuis une origine)",
           "Cotation aléatoire", "Les deux sont équivalents"], 1,
          "En cotation à la chaîne, les tolérances S'ADDITIONNENT (trois cotes à ±0,1 donnent "
          "±0,3). En cotation parallèle depuis une origine commune, les erreurs ne se cumulent "
          "pas. Principe de la cotation fonctionnelle : on cote la CONDITION, pas le chemin.",
          "Intermédiaire"),

        q("Un Ra de 0,8 µm correspond typiquement à quel procédé ?",
          ["Sciage", "Tournage d'ébauche", "Rectification", "Fonderie"], 2,
          "Ra 0,8 = rectification. Ordres de grandeur à connaître : 12,5-25 (sciage/brut), 6,3 "
          "(ébauche), 3,2 (tournage finition), 1,6 (fraisage finition, alésage), 0,8 "
          "(rectification), 0,4-0,1 (rectification fine, rodage).",
          "Intermédiaire"),

        q("Économiquement, diviser le Ra par deux revient à :",
          ["Diviser le coût par 2", "Ne rien changer au coût",
           "Doubler approximativement le coût de la surface", "Multiplier le coût par 10"], 2,
          "Règle empirique fondamentale : diviser Ra par 2 double environ le coût de la surface. "
          "On ne demande donc jamais un Ra serré 'par sécurité' : uniquement quand la fonction "
          "l'exige (étanchéité, portée de roulement, glissement).",
          "Intermédiaire"),

        q("Le symbole Ⓜ (maximum de matière) associé à une localisation permet :",
          ["De réduire la tolérance", "D'augmenter la tolérance quand la pièce s'écarte du MMC",
           "D'imposer un contrôle sur MMT", "De supprimer les références"], 1,
          "Ⓜ donne un BONUS de tolérance : si un trou est plus grand que son minimum, il "
          "pardonne davantage de défaut de position. t_disponible = t_spécifiée + (D_réel - "
          "D_min). Gratuit et sans risque d'assemblage : un réflexe d'économiste du BE.",
          "Avancé"),

        q("Une cote encadrée ⟦150⟧ sur un plan signifie :",
          ["Une cote très importante", "Une cote théorique exacte, non tolérancée directement",
           "Une cote en pouces", "Une cote de contrôle"], 1,
          "C'est une cote THÉORIQUE EXACTE (basic dimension). Elle définit la position idéale ; "
          "c'est le cadre de localisation ⌖ qui porte toute la tolérance. La tolérancer en ± "
          "créerait une double définition ambiguë.",
          "Avancé"),
    ],

    # =====================================================================
    "CAO et modélisation 3D": [
        q("Une esquisse SolidWorks affichée en BLEU est :",
          ["Entièrement contrainte", "Sous-contrainte", "Sur-contrainte", "Erronée"], 1,
          "Bleu = SOUS-CONTRAINTE : il reste des degrés de liberté, des entités peuvent bouger. "
          "Noir = entièrement contrainte (l'objectif). Jaune/rouge = sur-contrainte. Règle "
          "absolue : toujours contraindre à 100 % avant de créer la fonction volumique.",
          "Base"),

        q("Pourquoi faut-il éviter de créer une esquisse sur une FACE de la pièce plutôt que sur "
          "un plan de référence ?",
          ["C'est plus lent à calculer",
           "Cela crée une dépendance parent-enfant : si la face disparaît, l'esquisse casse",
           "Ce n'est pas autorisé par le logiciel",
           "Cela consomme plus de mémoire"], 1,
          "C'est la cause n°1 des modèles qui cassent. Une esquisse sur une face devient ENFANT "
          "de la fonction qui a créé cette face. Ancrer la géométrie sur les plans de référence "
          "et l'origine (qui ne disparaissent jamais) rend le modèle robuste.",
          "Intermédiaire"),

        q("Pour un perçage débouchant, quelle condition de fin choisir ?",
          ["Une profondeur numérique précise", "À travers tout",
           "Borgne", "Jusqu'au plan d'origine"], 1,
          "'À travers tout' est une condition LOGIQUE : le trou restera débouchant quelle que "
          "soit l'épaisseur future de la pièce. Une profondeur figée à 20 mm produirait des "
          "trous borgnes sur une pièce épaissie à 25 mm — défaut classique et coûteux.",
          "Base"),

        q("Quelle fonction utiliser pour créer 8 trous régulièrement répartis sur un cercle ?",
          ["8 enlèvements individuels", "Une répétition circulaire",
           "Une symétrie", "Un balayage"], 1,
          "La répétition circulaire : un seul trou modélisé, un paramètre pilote les 8 "
          "occurrences. Passer de 8 à 12 trous = changer un chiffre. Et la répartition régulière "
          "est mathématiquement garantie, pas dépendante de la précision des angles saisis.",
          "Base"),

        q("Où doit-on placer les congés et chanfreins dans l'arbre de construction ?",
          ["Au tout début", "Au milieu", "À la fin", "Peu importe"], 2,
          "À la FIN. Placés trop tôt, ils compliquent la sélection des faces pour les fonctions "
          "suivantes et ralentissent la régénération. On peut aussi les supprimer facilement "
          "pour un calcul par éléments finis simplifié.",
          "Intermédiaire"),

        q("Pour envoyer une pièce à un usineur CN, quel format d'échange utiliser ?",
          ["STL", "STEP", "DXF", "JPEG"], 1,
          "STEP : géométrie EXACTE (BREP), un cylindre reste un cylindre défini "
          "mathématiquement. Le STL n'est qu'un maillage de triangles APPROCHÉ, destiné à "
          "l'impression 3D. Envoyer un STL à un usineur est une faute professionnelle.",
          "Base"),

        q("Le fichier STEP suffit-il à définir contractuellement une pièce à fabriquer ?",
          ["Oui, il contient tout",
           "Non, il ne porte ni tolérances, ni états de surface, ni spécifications géométriques",
           "Oui, si on ajoute la matière",
           "Non, il faut un fichier natif"], 1,
          "Le STEP décrit une géométrie NOMINALE parfaite. Il ne dit pas si un Ø20 est en H7 ou "
          "en H11 (rapport de 1 à 6 sur la précision, 1 à 3 sur le coût). Seul le PLAN 2D coté "
          "est contractuel et opposable en cas de litige.",
          "Intermédiaire"),

        q("Dans un assemblage, quelles contraintes réalisent une liaison PIVOT ?",
          ["Une coaxialité seule", "Une coaxialité + une coïncidence de faces",
           "Trois coïncidences", "Une distance + un angle"], 1,
          "Coaxialité (supprime 4 DDL : 2 translations radiales + 2 rotations de basculement) + "
          "coïncidence de faces (supprime la translation axiale). Total 5 DDL supprimés, il "
          "reste 1 DDL : la rotation. Ajouter une 3e contrainte transformerait le pivot en "
          "encastrement.",
          "Intermédiaire"),

        q("La détection d'interférences en CAO permet de vérifier :",
          ["Le cumul des jeux d'ajustement", "Que les volumes nominaux ne se recouvrent pas",
           "La tenue mécanique", "Les défauts de forme"], 1,
          "Elle ne vérifie QUE la géométrie nominale. Elle est AVEUGLE aux tolérances, aux jeux "
          "d'ajustement, aux défauts de forme et d'orientation. Un assemblage 'sans "
          "interférence' peut parfaitement donner un mécanisme inutilisable. Il faut en plus "
          "une chaîne de cotes et un tolérancement GPS.",
          "Avancé"),
    ],

    # =====================================================================
    "Liaisons et conception": [
        q("Combien de degrés de liberté possède un solide libre dans l'espace ?",
          ["3", "4", "6", "12"], 2,
          "6 DDL : 3 translations (Tx, Ty, Tz) et 3 rotations (Rx, Ry, Rz). Une liaison "
          "mécanique en supprime un certain nombre ; le reste caractérise la liaison. "
          "Vérification systématique : DDL supprimés + DDL conservés = 6.",
          "Base"),

        q("Une liaison pivot possède combien de degrés de liberté ?",
          ["0", "1", "2", "3"], 1,
          "1 DDL : la rotation autour de son axe. À comparer : encastrement 0, glissière 1 "
          "(translation), pivot glissant 2, rotule 3 (trois rotations), appui plan 3, "
          "ponctuelle 5.",
          "Base"),

        q("Deux linéaires annulaires coaxiales montées en parallèle donnent une liaison :",
          ["Rotule", "Pivot", "Glissière", "Encastrement"], 1,
          "Chaque linéaire annulaire a 4 DDL, mais leur INTERSECTION (montage en parallèle) ne "
          "laisse que la rotation commune : c'est un PIVOT. C'est exactement le principe de "
          "deux roulements à billes sur un arbre.",
          "Intermédiaire"),

        q("Pourquoi un arbre monté sur deux roulements doit-il avoir un palier LIBRE ?",
          ["Pour faciliter le montage", "Pour absorber la dilatation thermique de l'arbre",
           "Pour réduire le coût", "Pour améliorer le rendement"], 1,
          "Si l'arbre est bloqué aux deux extrémités, sa dilatation empêchée génère un effort "
          "axial considérable (plusieurs dizaines de kN pour quelques dizaines de degrés) qui "
          "écrase les roulements et les détruit en quelques heures. Le palier libre coûte zéro : "
          "il suffit de ne pas mettre de circlips.",
          "Intermédiaire"),

        q("Sur le palier libre, quelle bague doit pouvoir coulisser ?",
          ["La bague intérieure", "La bague extérieure",
           "Les deux", "Aucune, c'est l'arbre qui coulisse"], 1,
          "La bague EXTÉRIEURE coulisse dans son logement (aucun blocage axial). Les deux bagues "
          "intérieures restent serrées et bloquées sur l'arbre. Confondre les deux est l'erreur "
          "la plus fréquente sur cette question.",
          "Piège"),

        q("Un montage HYPERSTATIQUE se caractérise par :",
          ["Trop de degrés de liberté", "Un même degré de liberté supprimé plusieurs fois",
           "Une absence de contraintes", "Un mécanisme bloqué"], 1,
          "Hyperstatique = un même DDL supprimé plusieurs fois. Résultat : plus rigide, mais "
          "exige des tolérances géométriques serrées (coaxialité, parallélisme). Sinon on force "
          "les pièces au montage, créant des contraintes internes. Ce n'est ni bon ni mauvais : "
          "c'est un arbitrage rigidité / précision de fabrication.",
          "Intermédiaire"),

        q("Deux roues dentées ne peuvent engrener que si elles ont :",
          ["Le même nombre de dents", "Le même module", "Le même diamètre", "la même largeur"], 1,
          "Le même MODULE m. C'est LA caractéristique d'une denture : d = m·Z. Le module fixe la "
          "taille de la dent. Valeurs normalisées : 0,5 - 0,8 - 1 - 1,25 - 1,5 - 2 - 2,5 - 3 - "
          "4 - 5...",
          "Base"),

        q("Un pignon de 20 dents entraîne une roue de 60 dents. Le rapport de transmission est :",
          ["3", "1/3", "1/2", "2/3"], 1,
          "r = Z_menante/Z_menée = 20/60 = 1/3. C'est un RÉDUCTEUR : la vitesse est divisée par "
          "3, le couple multiplié par 3 (au rendement près). Un rapport r < 1 signale toujours "
          "une réduction.",
          "Calcul"),

        q("En dessous de combien de dents apparaît l'interférence de taillage (denture droite, "
          "angle 20°) ?",
          ["10 dents", "17 dents", "25 dents", "40 dents"], 1,
          "17 dents. En dessous, la fraise-mère creuse le pied de la dent et l'affaiblit "
          "considérablement. Pour descendre plus bas, il faut appliquer un DÉPORT DE DENTURE.",
          "Intermédiaire"),

        q("Un système vis-écrou trapézoïdal a un rendement d'environ 35 %. C'est :",
          ["Un défaut de dimensionnement à corriger",
           "Le prix de l'irréversibilité, qui est une propriété de sécurité",
           "Dû à un mauvais graissage",
           "Normal mais sans intérêt"], 1,
          "C'est le MÊME frottement qui bloque la charge (irréversibilité) et qui consomme "
          "l'énergie. On ne peut pas avoir un système à la fois irréversible et à haut "
          "rendement. Sur une table élévatrice, cette irréversibilité évite un frein d'arrêt et "
          "constitue une sécurité intrinsèque, qui ne peut pas tomber en panne.",
          "Avancé"),

        q("Une vis à billes (rendement 92 %) sur un axe VERTICAL nécessite obligatoirement :",
          ["Un graissage renforcé", "Un frein d'arrêt",
           "Un capteur de position", "Un moteur plus puissant"], 1,
          "Un rendement élevé implique la RÉVERSIBILITÉ : la charge fait redescendre la vis dès "
          "que le moteur cesse de la retenir. Sur un axe vertical, un frein électromagnétique à "
          "manque de courant est obligatoire, et souvent aussi un dispositif anti-chute.",
          "Avancé"),

        q("La durée de vie L10h d'un roulement à billes varie avec la charge selon :",
          ["Une loi linéaire", "Le cube du rapport C/P",
           "La racine carrée de C/P", "Une loi exponentielle"], 1,
          "L10h = (10⁶/60N) × (C/P)³ pour les billes (exposant 10/3 pour les rouleaux). "
          "Conséquence : diviser la charge par 1,26 DOUBLE la durée de vie. À l'inverse, "
          "doubler la charge la divise par 8.",
          "Intermédiaire"),
    ],
}

CATEGORIES = list(QUIZ.keys())
NIVEAUX = ["Base", "Intermédiaire", "Calcul", "Piège", "Avancé"]


def toutes_les_questions():
    out = []
    for cat, questions in QUIZ.items():
        for i, question in enumerate(questions):
            item = dict(question)
            item["categorie"] = cat
            item["uid"] = f"{cat}#{i}"
            out.append(item)
    return out


def stats():
    total = sum(len(v) for v in QUIZ.values())
    par_cat = {k: len(v) for k, v in QUIZ.items()}
    par_niv = {}
    for question in toutes_les_questions():
        par_niv[question["niveau"]] = par_niv.get(question["niveau"], 0) + 1
    return {"total": total, "par_categorie": par_cat, "par_niveau": par_niv}


# ===========================================================================
# COMPLÉMENT DE QUESTIONS (ajouté après coup)
# Couvre les notions traitées dans les fiches réécrites : analyse
# fonctionnelle, cotation fonctionnelle, procédés, guidage.
# Pour retirer ce complément, il suffit de supprimer tout ce qui suit.
# ===========================================================================

QUIZ["Analyse fonctionnelle et cahier des charges"] = [
    q("Parmi ces formulations, laquelle est une FONCTION et non une solution ?",
      ["Utiliser un vérin pneumatique Ø32",
       "Maintenir la pièce pendant l'usinage",
       "Prévoir une clavette parallèle 8 × 7",
       "Monter un roulement à billes 6206"], 1,
      "Une fonction s'écrit avec un verbe à l'infinitif + un complément, sans jamais nommer de "
      "composant. Les trois autres réponses désignent déjà une solution technique : les écrire "
      "dans un cahier des charges interdirait de chercher mieux.", "Base"),

    q("Dans un diagramme pieuvre, une fonction qui relie le produit à UN SEUL élément du milieu "
      "extérieur est :",
      ["Une fonction principale (FP)", "Une fonction contrainte (FC)",
       "Une fonction technique", "Une solution constructive"], 1,
      "FP = relie DEUX éléments extérieurs en traversant le produit (sa raison d'être). "
      "FC = relie le produit à UN seul élément : c'est une contrainte subie (résister à "
      "l'humidité, respecter un budget, se fixer sur un support existant).", "Base"),

    q("Un client demande un carter « solide et facile à nettoyer ». Que manque-t-il ?",
      ["Rien, c'est exploitable tel quel",
       "Le nom du matériau",
       "Un critère, un niveau chiffré et une flexibilité pour chaque exigence",
       "Le prix de vente"], 2,
      "Une exigence non chiffrée n'est ni vérifiable ni contestable. Il faut : critère (énergie "
      "de choc), niveau (5 J sans déformation permanente), flexibilité (F0). Sinon, impossible "
      "de valider le produit en fin de projet ni de juger une offre fournisseur.", "Base"),

    q("La classe de flexibilité F0 signifie :",
      ["Fonction facultative", "Exigence impérative, non négociable",
       "Exigence négociable", "Fonction principale numéro 0"], 1,
      "F0 = impératif · F1 = peu négociable · F2 = négociable · F3 = simple souhait. Les "
      "exigences de sécurité et les contraintes d'interface avec l'existant sont typiquement "
      "en F0.", "Base"),

    q("Un distributeur automatique de croquettes pour chat : à QUI rend-il service ?",
      ["Au chat", "Au propriétaire", "Au fabricant", "Au vétérinaire"], 1,
      "PIÈGE FRÉQUENT. Le service est rendu à celui qui a le problème et qui achète : le "
      "propriétaire, qui veut partir en week-end. Le chat est la matière d'œuvre — l'élément "
      "sur lequel le produit agit.", "Piège"),

    q("Dans un diagramme FAST, où apparaît le nom d'un composant réel (roulement, vérin) ?",
      ["Dans la première colonne, avec la fonction de service",
       "Au milieu, avec les fonctions techniques",
       "À l'extrémité droite, dans les solutions techniques",
       "Nulle part, le FAST ne contient jamais de composant"], 2,
      "Le FAST se lit de gauche à droite en répondant à « comment ? ». Les composants réels "
      "n'apparaissent qu'à la dernière colonne. Écrire « roulement à billes » dans la première "
      "colonne, c'est avoir sauté toute l'analyse.", "Intermédiaire"),

    q("Quelle question NE fait PAS partie de la bête à cornes ?",
      ["À qui le produit rend-il service ?", "Sur quoi agit-il ?",
       "Dans quel but ?", "Avec quelle technologie ?"], 3,
      "La bête à cornes cadre le BESOIN, jamais la solution. La technologie viendra beaucoup "
      "plus tard, à l'extrémité droite du FAST.", "Base"),
]

QUIZ["Cotation fonctionnelle et chaînes de cotes"] = [
    q("Dans une chaîne de cotes, l'intervalle de tolérance de la condition ITja vaut :",
      ["La somme de tous les IT de la chaîne", "La différence entre le plus grand et le plus petit IT",
       "La moyenne des IT", "L'IT de la pièce la plus grande"], 0,
      "Les dispersions s'ACCUMULENT toujours : ITja = ITa + ITb + ITc + … quel que soit le sens "
      "des cotes. Conséquence directe : plus la chaîne est longue, plus chaque pièce doit être "
      "précise, donc chère.", "Base"),

    q("Une condition fonctionnelle Ja doit rester entre 0,2 et 0,8 mm. La chaîne comporte 4 "
      "cotes. En répartition uniforme, quelle tolérance par cote ?",
      ["0,15 mm", "0,6 mm", "0,05 mm", "0,3 mm"], 0,
      "ITja = 0,8 − 0,2 = 0,6 mm, réparti sur 4 cotes → 0,15 mm chacune. C'est très large : "
      "aucun usinage spécial n'est nécessaire.", "Calcul"),

    q("Dans une chaîne de cotes, combien de cotes une même pièce peut-elle fournir ?",
      ["Autant que nécessaire", "Une seule", "Deux au maximum", "Cela dépend de sa taille"], 1,
      "Chaque pièce traversée fournit UNE cote et une seule, entre ses deux surfaces d'appui. "
      "Si une pièce apparaît deux fois, le trajet n'est pas le plus direct ou une surface de "
      "contact a été mal identifiée.", "Base"),

    q("Toutes les cotes d'un sous-ensemble sont très serrées à cause d'une chaîne de 6 pièces. "
      "Quelle est la solution la plus économique ?",
      ["Rectifier toutes les pièces",
       "Introduire une cale de réglage qui absorbe la dispersion",
       "Changer de matériau", "Augmenter le coefficient de sécurité"], 1,
      "Une cale ou une entretoise usinée à la demande absorbe toute la dispersion : les autres "
      "cotes redeviennent larges. Raccourcir la chaîne est l'autre levier. Rectifier six pièces "
      "coûte infiniment plus cher qu'une cale à 3 €.", "Intermédiaire"),

    q("Une tolérance de PLANÉITÉ nécessite-t-elle une référence ?",
      ["Oui, toujours", "Non, jamais", "Seulement si la surface est grande",
       "Seulement sur un dessin d'ensemble"], 1,
      "Les tolérances de FORME (rectitude, planéité, circularité, cylindricité) se suffisent à "
      "elles-mêmes. Ce sont les tolérances d'orientation, de position et de battement qui "
      "exigent une référence.", "Base"),

    q("Dans un cadre de tolérance, le signe Ø placé devant la valeur signifie :",
      ["La cote concernée est un diamètre", "La zone de tolérance est cylindrique",
       "La tolérance est doublée", "La surface doit être tournée"], 1,
      "Sans Ø, la zone est comprise entre deux plans parallèles. Avec Ø, elle devient un "
      "cylindre de diamètre t — écriture typique de la localisation d'un axe de perçage.", "Intermédiaire"),

    q("Un arbre coté Ø20 h6 mesure 20 mm en tout point au micromètre, mais n'entre pas dans son "
      "alésage. Cause la plus probable ?",
      ["Une erreur de mesure", "Un défaut de forme : l'arbre est cintré ou ovale",
       "L'alésage est trop petit", "La matière a gonflé"], 1,
      "La cotation dimensionnelle ne dit rien sur la FORME. Chaque section peut mesurer 20 sans "
      "que l'ensemble soit un cylindre droit. D'où l'ajout d'une tolérance de rectitude ou de "
      "cylindricité.", "Piège"),
]

QUIZ["Procédés et conception pour la fabrication"] = [
    q("Pourquoi une dépouille est-elle obligatoire en moulage et en injection ?",
      ["Pour rigidifier la pièce", "Pour permettre le démoulage",
       "Pour améliorer l'aspect", "Pour réduire la masse"], 1,
      "Sans angle de dépouille (1 à 3°), la pièce se coince ou se raye dans le moule. C'est la "
      "première chose que vérifie un mouliste sur un plan.", "Base"),

    q("Une pièce injectée présente une marque creuse exactement en face d'une nervure "
      "intérieure. De quoi s'agit-il ?",
      ["D'une bavure", "D'une retassure due à une nervure trop épaisse",
       "D'une ligne de soudure", "D'un défaut de moule"], 1,
      "La matière en excès à la jonction refroidit plus lentement, se contracte et tire la "
      "surface. Correction : nervure à 50-60 % de l'épaisseur de la paroi, congé modéré à la "
      "base.", "Intermédiaire"),

    q("Quel format envoyer à un bureau d'études qui doit MODIFIER la géométrie ?",
      [".stl", ".step", ".pdf", ".dxf"], 1,
      "STEP conserve la géométrie exacte (surfaces et volumes) et s'ouvre dans tous les "
      "logiciels. STL n'est qu'un maillage de triangles destiné à l'impression : on ne "
      "remodélise jamais dessus.", "Base"),

    q("En impression FDM, dans quelle direction la pièce est-elle la plus fragile ?",
      ["Dans le plan des couches", "Perpendiculairement aux couches",
       "Elle est isotrope", "Cela dépend uniquement du matériau"], 1,
      "La liaison entre couches est le point faible : la pièce se sépare comme un mille-feuille. "
      "Il faut orienter la pièce pour que les efforts travaillent DANS le plan des couches.", "Intermédiaire"),

    q("Un angle intérieur parfaitement vif est-il réalisable en fraisage ?",
      ["Oui, avec une fraise adaptée", "Non : une fraise laisse toujours un rayon égal au sien",
       "Oui, mais seulement dans l'aluminium", "Oui, en deux passes"], 1,
      "Un outil rotatif ne peut pas créer un angle intérieur vif. Il faut donc dessiner le congé "
      "sur le plan — sinon l'atelier le fera à sa façon, et la cote ne sera pas celle prévue.", "Base"),

    q("Une tôle de 2 mm doit être percée à 4 mm d'un pli à 90°. Quel problème ?",
      ["Aucun", "Le trou tombe dans la zone déformée et devient ovale",
       "Le pli sera trop grand", "La tôle va casser au pliage"], 1,
      "Règle : distance du bord du trou au pli supérieure à environ 2,5 × épaisseur + rayon, "
      "soit 5 à 7 mm ici. Sinon, percer après pliage ou prévoir un dégagement.", "Intermédiaire"),
]

QUIZ["Guidage et montage de roulements"] = [
    q("Arbre tournant, charge radiale fixe. Comment monte-t-on la bague intérieure ?",
      ["Glissante", "Serrée", "Collée", "Avec un jeu de 0,1 mm"], 1,
      "La bague tourne par rapport à la direction de la charge : elle doit être SERRÉE (arbre en "
      "k6 ou m6). Montée avec du jeu, elle fluerait sur sa portée et la materait en quelques "
      "dizaines d'heures.", "Base"),

    q("Sur un tambour de convoyeur, c'est le tambour qui tourne et la charge (le poids de la "
      "bande) qui reste fixe. Quelle bague est serrée ?",
      ["La bague intérieure", "La bague extérieure", "Les deux", "Aucune"], 1,
      "C'est l'inverse du cas classique : la bague EXTÉRIEURE, solidaire du tambour, tourne par "
      "rapport à la charge → serrée dans le tambour (M7 ou N7). La bague intérieure est "
      "glissante sur l'arbre fixe (h6 ou g6).", "Piège"),

    q("Sur un arbre à deux paliers, combien de paliers doivent être bloqués axialement ?",
      ["Aucun", "Un seul", "Les deux", "Cela dépend de la longueur"], 1,
      "Un seul palier fixe positionne l'arbre ; l'autre doit rester libre pour absorber la "
      "dilatation. Deux paliers bloqués = précontrainte, échauffement, puis grippage.", "Base"),

    q("Un montage à deux roulements bloqués des deux côtés grippe après 20 minutes. Pourquoi ?",
      ["Manque de graisse", "L'arbre se dilate sans pouvoir s'allonger et précontraint les roulements",
       "Les roulements sont trop petits", "La vitesse est trop élevée"], 1,
      "C'est un emballement : la précontrainte augmente le frottement, donc la température, donc "
      "la dilatation. Correction : libérer axialement un des deux paliers.", "Intermédiaire"),

    q("Quelle rugosité viser sur une portée d'arbre recevant un joint à lèvres ?",
      ["Ra 12,5", "Ra 6,3", "Ra 3,2", "Ra 0,8"], 3,
      "Une surface trop rugueuse abrase la lèvre en élastomère en quelques heures et le joint "
      "fuit. Il faut Ra 0,8 environ, sans stries hélicoïdales, avec un chanfrein d'introduction "
      "pour le montage.", "Base"),

    q("Un roulement à rouleaux coniques peut-il être monté seul ?",
      ["Oui, comme un roulement à billes", "Non, il se monte obligatoirement par paire",
       "Oui, s'il n'y a pas de charge axiale", "Oui, en le collant"], 1,
      "Il n'encaisse l'axial que dans UN sens : il faut un second roulement opposé, monté en X "
      "ou en O. Même règle pour les roulements à billes à contact oblique.", "Intermédiaire"),

    q("Quelle quantité de graisse mettre dans un roulement ?",
      ["Le remplir complètement", "Environ un tiers du volume libre",
       "Le minimum possible", "Aux deux tiers"], 1,
      "Trop de graisse chauffe autant que pas assez : elle est brassée en permanence et "
      "s'échauffe. Un tiers du volume libre est la règle usuelle.", "Base"),

    q("La clavette parallèle sert à :",
      ["Maintenir le moyeu axialement", "Transmettre le couple",
       "Centrer le moyeu sur l'arbre", "Rattraper le jeu"], 1,
      "Elle transmet le COUPLE par ses flancs. Le centrage vient de l'ajustement (H7/j6 par "
      "exemple), l'arrêt axial d'un épaulement, d'un anneau élastique ou d'une vis de bout "
      "d'arbre.", "Base"),
]

CATEGORIES = list(QUIZ.keys())
