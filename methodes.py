# -*- coding: utf-8 -*-
"""
methodes.py — une fiche « la méthode, pas à pas » par fiche de cours.

Le cours explique pourquoi. La méthode dit **par où commencer** devant un
exercice ou devant une planche à dessin : les gestes numérotés, dans l'ordre,
chacun suivi de son application sur un cas chiffré.

Le mécanisme est celui de cours_debutant.py : appliquer(BLOCS) ajoute la clé
"methode" aux fiches dont l'identifiant figure ici. L'application fait alors
apparaître un onglet « Méthode », et l'aide-mémoire les rassemble toutes.
"""

METHODES = {}


def _m(fiche_id, titre, etapes, exemple):
    """Compose la fiche au format markdown attendu par l'application."""
    lignes = [f"### {titre}", ""]
    for i, e in enumerate(etapes, 1):
        lignes.append(f"{i}. {e}")
    lignes += ["", f"> **Sur un exemple.** {exemple}"]
    METHODES[fiche_id] = "\n".join(lignes)


# ===========================================================================
# BLOC 1 — ANALYSE FONCTIONNELLE ET LECTURE DE PLAN
# ===========================================================================

_m("1.1", "Rédiger un cahier des charges fonctionnel", [
    "**Poser la bête à cornes** : à qui le produit rend-il service, sur quoi agit-il, "
    "dans quel but ? Les trois réponses donnent la fonction globale.",
    "**Lister les éléments du milieu extérieur** : l'utilisateur, la pièce, l'énergie, "
    "la norme, l'ambiance, le budget. Rien n'est de trop à ce stade.",
    "**Tracer la pieuvre** : une fonction principale relie deux éléments entre eux ; "
    "une fonction contrainte relie le produit à un seul élément.",
    "**Écrire chaque fonction avec un verbe à l'infinitif**, et sans jamais nommer de "
    "solution technique. « Maintenir la pièce », pas « serrer avec un vérin ».",
    "**Caractériser chaque fonction** par un critère, un niveau et une flexibilité. "
    "Une fonction sans niveau chiffré n'est pas vérifiable, donc inutile.",
], "« Maintenir un capteur face à la ligne » — critère : distance capteur/bouteille ; "
   "niveau : 15 mm ± 2 ; flexibilité : F1. On peut désormais valider ou refuser une "
   "solution, ce qui était impossible avec « faire une équerre ».")

_m("1.2", "Lire un plan sans se tromper de vue", [
    "**Repérer la vue de face** : c'est celle qui montre le plus de détails et le moins "
    "de traits interrompus. Tout le reste se déduit d'elle.",
    "**Vérifier la disposition** : en projection européenne, la vue de gauche se dessine "
    "à droite. C'est l'inverse en projection américaine — le symbole en cartouche le dit.",
    "**Identifier la nature de chaque trait** : continu fort pour les arêtes vues, "
    "interrompu pour les arêtes cachées, mixte fin pour les axes.",
    "**Suivre un point d'une vue à l'autre** en traçant les lignes de rappel : un même "
    "point doit s'aligner horizontalement et verticalement entre les vues.",
    "**Lire les coupes en dernier** : les hachures signalent la matière réellement "
    "traversée, et le sens des flèches indique d'où l'on regarde.",
], "Un trou débouchant apparaît en deux traits interrompus parallèles sur la vue de face, "
   "et en un cercle continu sur la vue de dessus. Les deux se correspondent par les "
   "lignes de rappel : c'est ce recoupement qui confirme la lecture.")

_m("1.3", "Lire une cote et un état de surface", [
    "**Séparer la cote nominale des écarts** : dans 30 ±0,1, le 30 est la cote nominale, "
    "les ±0,1 sont les écarts.",
    "**Calculer les deux limites** : cote maxi et cote mini. Une pièce est bonne si sa "
    "mesure tombe entre les deux, bornes comprises.",
    "**Calculer l'intervalle de tolérance** : IT = cote maxi − cote mini. C'est lui qui "
    "décide du coût de fabrication.",
    "**Lire le symbole de rugosité** : le nombre porté est le Ra, en micromètres. Plus il "
    "est petit, plus la surface est lisse — et plus elle est chère.",
    "**Se demander à quoi sert la surface** avant d'exiger une rugosité : une portée de "
    "roulement demande Ra 0,8 ; une face brute d'appui se contente de Ra 6,3.",
], "30 ±0,1 donne une cote maxi de 30,1 et une cote mini de 29,9, soit IT = 0,2 mm "
   "= 200 µm. Une pièce mesurée à 30,15 est **rebutée**, même de peu.")


# ===========================================================================
# BLOC 2 — TOLÉRANCEMENT ET AJUSTEMENTS ISO
# ===========================================================================

_m("2.1", "Décoder une cote tolérancée ISO", [
    "**Séparer les trois éléments** : la cote nominale, la lettre, le grade. Dans "
    "⌀30 H7, la nominale vaut 30, la lettre est H, le grade 7.",
    "**Retenir la règle de casse** : une lettre **majuscule** désigne un alésage "
    "(un trou), une lettre **minuscule** un arbre (une pièce mâle).",
    "**Lire l'IT dans la table ISO 286-1** en croisant la tranche de dimension et le grade.",
    "**Lire l'écart de position** dans la table ISO 286-2, à la lettre. Pour H, l'écart "
    "inférieur vaut zéro : l'alésage part du nominal et ne peut qu'être plus grand.",
    "**Composer les deux cotes limites**, et vérifier que leur différence redonne bien "
    "l'IT lu à l'étape 3.",
], "⌀30 H7 : IT7 vaut 21 µm pour la tranche 18–30, et H impose EI = 0. L'alésage est "
   "donc compris entre 30,000 et 30,021 mm.")

_m("2.2", "Déterminer la nature d'un ajustement", [
    "**Décoder séparément l'alésage et l'arbre**, et écrire leurs quatre cotes limites.",
    "**Calculer le jeu maximal** : alésage **maxi** moins arbre **mini**. C'est le cas le "
    "plus favorable au mouvement.",
    "**Calculer le jeu minimal** : alésage **mini** moins arbre **maxi**. C'est le cas le "
    "plus serré.",
    "**Conclure sur la nature** : les deux positifs, c'est un ajustement avec jeu ; les "
    "deux négatifs, c'est un serrage ; de signes contraires, il est incertain.",
    "**Confronter au besoin** : un guidage tournant veut du jeu, un moyeu à emmancher "
    "veut du serrage, un centrage précis démontable veut de l'incertain.",
], "⌀30 H7/g6 : jeu maxi 41 µm, jeu mini 7 µm. Les deux sont positifs, donc jeu garanti "
   "en toutes circonstances : l'arbre tournera même sur les pièces les plus défavorables.")

_m("2.3", "Lire un cadre de tolérancement géométrique", [
    "**Lire les trois cases de gauche à droite** : le symbole de la spécification, la "
    "valeur de la zone, puis la ou les références.",
    "**Identifier ce qui est tolérancé** : ce que désigne la flèche du cadre — une "
    "surface, un axe, un plan médian.",
    "**Identifier la référence** : la lettre renvoie au triangle plein posé sur une "
    "surface. Sans référence, la spécification est de forme ; avec, elle est d'orientation "
    "ou de position.",
    "**Se représenter la zone de tolérance** : deux plans parallèles, deux droites, un "
    "cylindre — le symbole ⌀ devant la valeur signale une zone cylindrique.",
    "**Vérifier que la spécification est utile** : elle doit traduire une exigence "
    "fonctionnelle réelle, pas un réflexe de dessinateur.",
], "Un cadre « ⟂ 0,05 A » sur l'axe d'un alésage signifie : l'axe doit rester dans un "
   "espace de 0,05 mm de large, perpendiculaire au plan de référence A. Rien n'est dit "
   "de la position du trou, seulement de son orientation.")


# ===========================================================================
# BLOC 3 — MATÉRIAUX
# ===========================================================================

_m("3.1", "Choisir un matériau à partir du besoin", [
    "**Écrire la ou les exigences en clair** : tenir un effort ? rester léger ? résister "
    "à la corrosion ? conduire la chaleur ? tenir un prix ?",
    "**Traduire chaque exigence en propriété chiffrée** : effort → Re ; légèreté → masse "
    "volumique ; rigidité → module d'Young E.",
    "**Utiliser un indice de performance** quand deux exigences s'opposent : Re/ρ pour "
    "une pièce résistante et légère, E/ρ pour une pièce rigide et légère.",
    "**Comparer trois candidats seulement**, un par grande famille : un acier, un "
    "aluminium, un polymère ou composite.",
    "**Trancher avec les critères non mécaniques** : prix, disponibilité, usinabilité, "
    "soudabilité, aptitude au traitement.",
], "Pour un bras de robot, la rigidité et la légèreté comptent : l'aluminium 6060 "
   "(E/ρ ≈ 26) bat l'acier S235 (E/ρ ≈ 27 — comparable) sur la masse à section égale, "
   "mais l'acier reprend l'avantage dès que le prix au kilo pèse dans le choix.")

_m("3.2", "Décoder une désignation normalisée", [
    "**Regarder la première lettre** : S ou E pour un acier de construction, C pour un "
    "acier non allié, X pour un acier fortement allié, EN AW pour un aluminium corroyé.",
    "**Pour un S ou un E** : le nombre qui suit est la limite élastique Re en MPa. "
    "S235 tient 235 MPa.",
    "**Pour un C** : le nombre est la teneur en carbone en centièmes de pourcent. "
    "C45 contient 0,45 % de carbone.",
    "**Pour un X** : les nombres donnent, dans l'ordre, le carbone en centièmes puis la "
    "teneur des éléments d'alliage en pourcent.",
    "**Lire les suffixes** : JR, J0, J2 renseignent la résilience ; T6 est un état "
    "métallurgique pour l'aluminium.",
], "X5CrNi18-10 : acier fortement allié, 0,05 % de carbone, 18 % de chrome et 10 % de "
   "nickel — l'inox le plus courant. C45 : acier non allié à 0,45 % de carbone, "
   "trempable, celui des axes et des arbres.")

_m("3.3", "Choisir un traitement thermique ou de surface", [
    "**Nommer le défaut à corriger** : pièce trop tendre en surface ? trop fragile à "
    "cœur ? qui rouille ? qui frotte ?",
    "**Distinguer traitement dans la masse et traitement de surface** : la trempe change "
    "tout le volume, la cémentation ou la nitruration ne durcissent que la peau.",
    "**Se rappeler qu'une trempe sans revenu est inutilisable** : la pièce est dure mais "
    "cassante. Le revenu rend la ténacité au prix d'un peu de dureté.",
    "**Vérifier que le matériau accepte le traitement** : il faut au moins 0,3 % de "
    "carbone pour tremper un acier. Un S235 ne se trempe pas.",
    "**Placer le traitement au bon moment de la gamme** : l'usinage de finition vient "
    "après le traitement quand celui-ci déforme la pièce.",
], "Un pignon en 16MnCr5 est cémenté puis trempé : le cœur reste tenace pour encaisser "
   "les chocs, la peau devient très dure pour résister à l'usure des dents. Un C45 trempé "
   "à cœur serait dur partout — et casserait au premier choc.")


# ===========================================================================
# BLOC 4 — RÉSISTANCE DES MATÉRIAUX
# ===========================================================================

_m("4.1", "Dimensionner une pièce en traction", [
    "**Isoler la pièce et repérer la sollicitation** : traction pure si l'effort est "
    "porté par l'axe de la pièce et centré.",
    "**Calculer la contrainte admissible** : Rpe = Re / s. On ne dimensionne jamais sur "
    "Re, toujours sur Rpe.",
    "**Écrire la condition de résistance** : σ ≤ Rpe, c'est-à-dire N/S ≤ Rpe.",
    "**En déduire la section minimale** : S ≥ N / Rpe, puis remonter à la dimension par "
    "la géométrie (d = √(4S/π) pour un cylindre).",
    "**Prendre la valeur normalisée immédiatement supérieure**, et rappeler que ce "
    "résultat est un minimum théorique, jamais une cote de plan.",
], "N = 10 000 N, Re = 355 MPa, s = 3 → Rpe ≈ 118 MPa, donc S ≥ 84,5 mm², donc "
   "d ≥ 10,4 mm. On retiendra ⌀12, en vérifiant ensuite les concentrations de contrainte.")

_m("4.2", "Vérifier un axe au cisaillement, puis au matage", [
    "**Compter les sections cisaillées** : un axe en chape travaille en **double** "
    "cisaillement, la section résistante est doublée.",
    "**Calculer la contrainte de cisaillement** : τ = T / S, avec S la somme des sections "
    "cisaillées.",
    "**Comparer à la résistance au glissement** : Rpg vaut environ 0,5 Re pour un acier, "
    "puis appliquer le coefficient de sécurité.",
    "**Ne pas s'arrêter là : vérifier le matage** de la pièce la plus tendre, sur la "
    "surface projetée d = diamètre × épaisseur.",
    "**Conclure sur les deux critères** : c'est presque toujours le matage, et non le "
    "cisaillement, qui impose le diamètre final.",
], "Axe ⌀10 en double cisaillement sous 8 000 N : S = 2 × 78,5 = 157 mm², donc "
   "τ = 51 MPa — largement admissible. Mais dans une chape en aluminium de 5 mm, la "
   "pression de matage vaut 8 000/(10 × 5) = 160 MPa : c'est elle qui coince.")

_m("4.3", "Dimensionner une poutre en flexion", [
    "**Identifier le cas de charge** : appuis ou encastrement, charge concentrée ou "
    "répartie. C'est lui qui choisit la formule du moment maximal.",
    "**Calculer le moment fléchissant maximal** : F·L/4 pour deux appuis et une charge "
    "centrée, F·L pour un encastrement avec charge à l'extrémité, q·L²/8 pour une charge "
    "répartie sur deux appuis.",
    "**Calculer le module de flexion I/v** de la section : bh²/6 pour un rectangle, "
    "πd³/32 pour un cercle plein.",
    "**Appliquer la condition de résistance** : σ = Mf / (I/v) ≤ Rpe.",
    "**Vérifier ensuite la flèche**, qui est souvent le critère le plus contraignant : "
    "une poutre peut résister et pourtant plier de façon inacceptable.",
], "F = 2 000 N, L = 500 mm, deux appuis : Mf max = 250 000 N·mm. Pour une section "
   "carrée de 30 mm, I/v = 4 500 mm³, donc σ = 55,6 MPa. Un S235 avec s = 2 admet "
   "117 MPa : la résistance est acquise, il reste à contrôler la flèche.")


# ===========================================================================
# BLOC 5 — CAO
# ===========================================================================

_m("5.1", "Contraindre complètement une esquisse", [
    "**Dessiner d'abord la forme approximative**, sans chercher les bonnes valeurs : la "
    "géométrie avant les cotes.",
    "**Poser les contraintes géométriques** : horizontal, vertical, parallèle, "
    "perpendiculaire, tangent, égal, coïncident. Elles remplacent souvent plusieurs cotes.",
    "**Ancrer l'esquisse à l'origine** : sans ce point fixe, elle flotte et l'esquisse ne "
    "sera jamais complètement contrainte.",
    "**Ajouter les cotes qui restent**, une par degré de liberté encore libre.",
    "**Vérifier l'état affiché** : « entièrement contrainte ». Une esquisse sous-contrainte "
    "bouge au moindre changement ; une esquisse sur-contrainte refuse de se modifier.",
], "Un rectangle libre a 8 degrés de liberté. Deux contraintes horizontal/vertical, une "
   "coïncidence à l'origine et deux cotes suffisent à le bloquer : l'esquisse devient noire "
   "et ne bougera plus toute seule.")

_m("5.2", "Construire une pièce par son arbre de création", [
    "**Partir du brut, puis enlever la matière** : extrusion du volume principal, puis "
    "perçages, poches et chanfreins. C'est l'ordre du fabricant.",
    "**Faire une fonction par intention de conception**, pas une fonction par forme : un "
    "perçage taraudé est une intention, ses trois diamètres ne sont pas trois pièces.",
    "**Nommer chaque fonction dans l'arbre**. Un arbre nommé se relit un an plus tard ; "
    "« Bossage-Extrusion7 » ne dit rien à personne.",
    "**Placer les congés et chanfreins en dernier**, sauf s'ils portent une fonction : "
    "ils alourdissent l'arbre et compliquent toute modification.",
    "**Tester la robustesse** en modifiant une cote de départ : si la pièce se casse "
    "entièrement, l'arbre est fragile et demande à être repris.",
], "Une équerre percée : extrusion de la semelle, extrusion de l'aile, perçage de fixation, "
   "congé de raccordement. Quatre fonctions nommées, et le passage de 60 à 80 mm de long "
   "ne casse rien.")

_m("5.3", "Réussir une mise en plan", [
    "**Choisir la vue de face** : celle qui montre la pièce dans sa position d'usinage ou "
    "d'utilisation, avec le maximum d'informations.",
    "**Ajouter le minimum de vues nécessaires** : deux suffisent souvent, trois rarement. "
    "Une vue de plus est une occasion de contradiction en plus.",
    "**Couper plutôt que multiplier les traits interrompus** : une coupe bien placée "
    "remplace une vue illisible.",
    "**Coter fonctionnellement** : partir des surfaces qui servent, pas de la façon dont "
    "on a dessiné. Ne jamais surcoter — une cote de trop crée un conflit.",
    "**Remplir le cartouche et vérifier** : échelle, projection, matière, état de surface "
    "général, tolérances générales.",
], "Une pièce tournée se pose horizontalement, axe de rotation à l'horizontale, et se cote "
   "en chaîne depuis la face d'appui : c'est ainsi qu'elle sera prise en mandrin, et donc "
   "ainsi qu'elle sera mesurée.")


# ===========================================================================
# BLOC 6 — LIAISONS ET CONCEPTION
# ===========================================================================

_m("6.1", "Identifier une liaison et tracer un schéma cinématique", [
    "**Compter les degrés de liberté restants** entre les deux pièces : trois "
    "translations et trois rotations au départ, on retire ce que le contact bloque.",
    "**Nommer la liaison** à partir de ce décompte : 1 rotation seule → pivot ; "
    "1 translation seule → glissière ; 3 rotations → rotule ; 0 → encastrement.",
    "**Repérer le centre et l'axe** de la liaison : le schéma cinématique en dépend "
    "entièrement.",
    "**Tracer le schéma** avec le symbole normalisé, en respectant les positions "
    "relatives réelles des liaisons.",
    "**Vérifier la mobilité de l'ensemble** : le schéma doit permettre le mouvement voulu, "
    "et lui seul.",
], "Un arbre dans deux paliers alignés : les deux translations radiales et les deux "
   "rotations de basculement sont bloquées, la translation axiale l'est par un épaulement. "
   "Il reste une rotation : c'est une liaison pivot.")

_m("6.2", "Concevoir un guidage en rotation par roulements", [
    "**Choisir le type de roulement** selon les charges : à billes pour du radial pur, à "
    "rouleaux coniques dès qu'il y a de l'axial, à aiguilles quand la place manque.",
    "**Choisir le montage** : en O ou en X pour les coniques ; sinon un palier fixe et un "
    "palier libre, pour laisser la dilatation s'échapper.",
    "**Respecter la règle des ajustements** : la bague qui **tourne par rapport à la "
    "charge** est montée serrée, l'autre glissante. C'est la règle qui tombe à l'examen.",
    "**Prévoir les arrêts axiaux** : épaulement d'un côté, circlips ou écrou de l'autre. "
    "Un roulement qui se promène détruit son logement.",
    "**Ajouter l'étanchéité et la lubrification** : joint à lèvre, graisse, et un accès "
    "pour regraisser si la maintenance le demande.",
], "Arbre tournant sous charge fixe : la bague intérieure tourne par rapport à la charge, "
   "donc serrée sur l'arbre (k6) ; la bague extérieure est fixe par rapport à la charge, "
   "donc glissante dans le logement (H7).")

_m("6.3", "Dimensionner une transmission", [
    "**Remonter la chaîne d'énergie** : du besoin en sortie vers le moteur, et non "
    "l'inverse.",
    "**Calculer le couple utile en sortie** à partir de la puissance et de la vitesse : "
    "C = P/ω, avec ω = 2πN/60.",
    "**Appliquer le rapport de réduction** : la vitesse est divisée, le couple est "
    "multiplié — c'est le même échange que sur un vélo.",
    "**Tenir compte des rendements** à chaque étage : chaque engrenage, chaque courroie "
    "en prend sa part. Le moteur doit être dimensionné sur la puissance **absorbée**.",
    "**Vérifier l'arbre le plus sollicité** en torsion, et souvent en flexion+torsion "
    "combinées : c'est presque toujours l'arbre de sortie, le plus lent et le plus chargé.",
], "Un moteur de 3 kW à 1 500 tr/min développe 19,1 N·m. Après un réducteur 1/20 de "
   "rendement 0,9, la sortie tourne à 75 tr/min et transmet 19,1 × 20 × 0,9 ≈ 344 N·m. "
   "C'est cet arbre-là qu'il faut dimensionner.")


# ===========================================================================
# BLOC 7 — MATHÉMATIQUES APPLIQUÉES
# ===========================================================================

_m("7.1", "Résoudre un triangle de dessin technique", [
    "**Faire un croquis coté**, même grossier : la moitié des erreurs vient d'une figure "
    "jamais dessinée.",
    "**Repérer si le triangle est rectangle** : c'est le cas le plus fréquent en dessin, "
    "et le plus simple.",
    "**Dans un triangle rectangle**, choisir la relation d'après ce qu'on connaît : "
    "cosinus (adjacent/hypoténuse), sinus (opposé/hypoténuse), tangente (opposé/adjacent).",
    "**Sinon, utiliser Al-Kashi** : a² = b² + c² − 2bc·cos(A), qui contient Pythagore "
    "comme cas particulier quand l'angle vaut 90°.",
    "**Contrôler la vraisemblance** : le plus grand côté fait face au plus grand angle, "
    "et la somme des angles vaut 180°.",
], "Un perçage à 35 mm du centre, à 30° de l'horizontale : x = 35·cos(30°) = 30,31 mm et "
   "y = 35·sin(30°) = 17,50 mm. Ce sont les deux cotes à porter sur le plan.")

_m("7.2", "Optimiser une grandeur par la dérivée", [
    "**Écrire la grandeur à optimiser** en fonction d'une seule variable. C'est l'étape "
    "difficile, et souvent la seule qui compte vraiment.",
    "**Utiliser la contrainte** (un volume imposé, une longueur donnée) pour éliminer les "
    "variables en trop.",
    "**Dériver**, puis résoudre f'(x) = 0 : ce sont les candidats.",
    "**Vérifier qu'il s'agit d'un minimum** et non d'un maximum, par le signe de la "
    "dérivée de part et d'autre.",
    "**Revenir au problème concret** : arrondir à une valeur fabricable et vérifier que la "
    "contrainte est toujours respectée.",
], "Pour une boîte cylindrique de volume imposé, minimiser la tôle conduit à h = 2r : la "
   "hauteur égale le diamètre. C'est la forme la plus économique — et c'est bien celle des "
   "boîtes de conserve.")

_m("7.3", "Juger une production par sa capabilité", [
    "**Relever l'intervalle de tolérance** du plan : IT = cote maxi − cote mini.",
    "**Calculer la moyenne et l'écart-type** de l'échantillon mesuré.",
    "**Calculer Cp = IT / (6σ)** : il compare la dispersion de la machine à ce que le "
    "plan autorise, sans regarder si elle est bien centrée.",
    "**Calculer Cpk**, qui tient compte du décentrage : il vaut Cp si la production est "
    "parfaitement centrée, moins sinon.",
    "**Conclure** : on demande couramment Cpk ≥ 1,33. Un Cp élevé avec un Cpk faible "
    "signale une machine précise mais **déréglée** — un simple recentrage suffit.",
], "IT = 0,2 mm et σ = 0,02 mm donnent Cp = 1,67 : la machine est capable. Mais si la "
   "moyenne est décalée de 0,05 mm, Cpk tombe à 0,83 : on produit des rebuts alors que la "
   "machine n'y est pour rien.")


# ===========================================================================
# BLOC 8 — PHYSIQUE APPLIQUÉE
# ===========================================================================

_m("8.1", "Appliquer le principe fondamental de la dynamique", [
    "**Isoler le solide** et le nommer : tout ce qui suit ne concerne que lui.",
    "**Faire l'inventaire des forces** : d'abord les contacts, ensuite les forces à "
    "distance. Le poids ne s'oublie jamais.",
    "**Choisir le repère** en alignant un axe sur le mouvement : c'est ce qui simplifie "
    "les projections.",
    "**Écrire ΣF = m·a**, puis projeter sur chaque axe. Une équation par axe.",
    "**Résoudre, puis vérifier le signe** : une accélération négative sur l'axe du "
    "mouvement signifie un freinage, pas une erreur.",
], "Un chariot de 50 kg tiré par 200 N contre 80 N de frottement : ΣF = 120 N, donc "
   "a = 120/50 = 2,4 m/s². Positif : il accélère bien dans le sens de la traction.")

_m("8.2", "Faire un bilan d'énergie ou de débit", [
    "**Délimiter le système** et dire ce qui entre, ce qui sort, ce qui s'accumule.",
    "**Choisir la grandeur conservée** : l'énergie pour un bilan thermique ou mécanique, "
    "le débit-volume pour un circuit hydraulique.",
    "**Écrire l'égalité** : ce qui entre = ce qui sort + ce qui est stocké ou perdu.",
    "**Convertir toutes les unités avant de calculer** : des litres par minute en m³/s, "
    "des kilowatts en watts, des minutes en secondes.",
    "**Interpréter la perte** : elle n'est jamais nulle, et sa valeur est le rendement du "
    "système.",
], "Un vérin ⌀50 alimenté à 10 L/min : la section vaut 19,6 cm², donc la vitesse de tige "
   "est 10/60 dm³/s ÷ 0,196 dm² ≈ 0,85 dm/s, soit 85 mm/s.")

_m("8.3", "Choisir et exploiter un capteur", [
    "**Nommer la grandeur physique à mesurer** : présence, position, effort, température, "
    "pression.",
    "**Choisir la technologie selon la cible** : inductif pour un métal, capacitif pour "
    "tout matériau, photoélectrique pour la longue portée, ILS pour un vérin.",
    "**Vérifier la portée et la précision** dans la documentation, en tenant compte du "
    "facteur de correction lié au matériau détecté.",
    "**Regarder le type de sortie** : PNP ou NPN, NO ou NF. Une erreur ici et l'automate "
    "lit l'inverse de la réalité.",
    "**Traduire la sortie en grandeur physique** quand le signal est analogique : une "
    "sortie 4–20 mA se convertit par une simple proportionnalité.",
], "Un capteur 4–20 mA mesurant 0–10 bar : à 12 mA, on est au milieu de la plage de "
   "courant, donc à 5 bar. Le 4 mA à zéro permet de détecter un fil coupé, qui donnerait "
   "0 mA — impossible en fonctionnement normal.")


# ===========================================================================
# BLOC 9 — PROJET, CAO GUIDÉE, SOUTENANCE
# ===========================================================================

_m("9.1", "Conduire un projet technique de bout en bout", [
    "**Reformuler le besoin** avant toute chose, et le faire valider par écrit. Un besoin "
    "mal compris ne se rattrape pas plus tard.",
    "**Découper en tâches** avec, pour chacune, un livrable et une durée. Une tâche sans "
    "livrable ne se termine jamais.",
    "**Ordonner les tâches** en repérant celles qui en bloquent d'autres : c'est le chemin "
    "critique, celui où tout retard se répercute.",
    "**Fixer des points d'étape** avec un critère de passage clair, et non une date seule.",
    "**Tenir un journal de projet** : décisions prises, raisons, essais ratés. C'est la "
    "matière première du dossier technique et de la soutenance.",
], "Sur un projet de huit semaines, la commande des roulements est sur le chemin critique : "
   "trois semaines de délai fournisseur. Elle se lance en semaine 1, avant même que la "
   "conception soit figée.")

_m("9.2", "Modéliser une pièce dans SolidWorks", [
    "**Choisir le plan de départ** en pensant à la position d'utilisation : cela évite des "
    "acrobaties à la mise en plan.",
    "**Esquisser la forme principale et la contraindre entièrement**, puis extruder.",
    "**Enlever la matière dans l'ordre du fabricant** : perçages, poches, rainures.",
    "**Renseigner le matériau** : la masse et le centre de gravité deviennent alors "
    "exploitables, et l'étude statique aussi.",
    "**Contrôler avant de fermer** : masse plausible, arbre sans erreur, esquisses toutes "
    "contraintes, fichier nommé selon la nomenclature du projet.",
], "Une chape : esquisse en U contrainte, extrusion 40 mm, perçage ⌀10 traversant, congés "
   "de 3 mm. Quatre fonctions, et la masse annoncée par le logiciel donne tout de suite un "
   "ordre de grandeur à confronter au bon sens.")

_m("9.3", "Préparer un dossier et une soutenance", [
    "**Partir du besoin, pas de la solution** : les premières minutes doivent expliquer "
    "**pourquoi** le produit existe.",
    "**Montrer une solution écartée** et dire pourquoi elle l'a été. C'est ce qui prouve "
    "une démarche de conception, et c'est ce que le jury cherche.",
    "**Chiffrer au moins un dimensionnement** de bout en bout, avec ses hypothèses.",
    "**Préparer une image par idée** : un schéma cinématique, une vue éclatée, une courbe. "
    "Jamais de diapositive couverte de texte.",
    "**Répéter à voix haute, minuté**, et préparer trois questions gênantes avec leur "
    "réponse : « pourquoi ce matériau ? », « et si la charge double ? », « combien ça coûte ? »",
], "Une soutenance qui commence par « j'ai modélisé une équerre » perd le jury. La même qui "
   "commence par « le capteur bougeait à cause des vibrations de la ligne » le tient "
   "jusqu'au bout.")


# ===========================================================================
# BLOC 10 — ANGLAIS ET ÉCONOMIE-GESTION
# ===========================================================================

_m("10.1", "Lire une documentation technique en anglais", [
    "**Repérer d'abord la structure**, sans lire : titres, tableaux, schémas, unités. La "
    "moitié de l'information est là.",
    "**Lire les valeurs numériques et leurs unités** avant les phrases : elles sont "
    "universelles, et elles cadrent le sens.",
    "**Se méfier du point décimal** : en anglais, 1,000 signifie mille et 1.5 signifie un "
    "et demi. Une confusion ici fausse tout un dimensionnement.",
    "**Traduire les faux amis du métier** : *rate* est un débit, *sensitive* veut dire "
    "sensible, *actual* signifie réel et non actuel.",
    "**Reformuler en une phrase française** ce que la documentation autorise et ce qu'elle "
    "interdit. Si on n'y arrive pas, on n'a pas compris.",
], "« Max. operating pressure: 1,000 psi » veut dire mille psi, soit environ 69 bar — et "
   "non un psi. L'écart de lecture serait d'un facteur mille.")

_m("10.2", "Calculer le coût de ce qu'on dessine", [
    "**Séparer les trois postes** : la matière, la main-d'œuvre et les frais de structure. "
    "Chacun se calcule à part.",
    "**Chiffrer la matière** à partir du volume de la pièce, de la masse volumique et du "
    "prix au kilo — sans oublier la chute, souvent 20 à 40 %.",
    "**Chiffrer la main-d'œuvre** en multipliant le temps de gamme par le taux horaire du "
    "poste, réglage compris.",
    "**Ajouter les frais** en pourcentage, puis la marge.",
    "**Comparer deux variantes de conception** : c'est là que le calcul devient utile. Un "
    "congé qui évite une reprise d'usinage vaut souvent plus que dix grammes de matière.",
], "Une pièce de 0,8 kg en acier à 1,20 €/kg coûte 0,96 € de matière, mais 12 minutes de "
   "fraisage à 60 €/h en coûtent 12. Alléger la pièce n'a aucun intérêt : c'est le temps "
   "d'usinage qu'il faut attaquer.")


# ===========================================================================
# BLOC 11 — DEUXIÈME ANNÉE
# ===========================================================================

_m("11.1", "Organiser ses révisions sur l'année", [
    "**Repérer les notions qui reviennent partout** : ISO 286, RDM, liaisons. Elles "
    "servent en cours, en TP, en projet et à l'examen.",
    "**Réviser par la pratique**, pas par la relecture : refaire un exercice bat relire "
    "une fiche, à temps égal.",
    "**Utiliser la révision espacée** : laisser les questions ratées revenir d'elles-mêmes, "
    "à intervalles croissants.",
    "**Se mettre en conditions réelles** une fois par mois avec le mode contrôle : "
    "chronomètre, sans corrigé sous les yeux.",
    "**Tenir un carnet d'erreurs** : une ligne par erreur commise et sa cause. C'est le "
    "document le plus utile de la semaine précédant l'examen.",
], "Trois séances de trente minutes réparties sur la semaine font retenir bien plus qu'une "
   "séance de deux heures la veille — et c'est exactement ce que la révision espacée "
   "organise à votre place.")


def appliquer(blocs):
    """Ajoute la clé 'methode' aux fiches dont l'identifiant figure ici."""
    ajoutees = 0
    for bloc in blocs:
        fiches = bloc.get("fiches", [])
        if isinstance(fiches, dict):
            fiches = list(fiches.values())
        for fiche in fiches:
            texte = METHODES.get(fiche.get("id"))
            if texte:
                fiche["methode"] = texte
                ajoutees += 1
    return ajoutees
