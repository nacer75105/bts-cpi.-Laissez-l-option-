# -*- coding: utf-8 -*-
# Corrections du brouillon 6.21 après relecture (relecteur-bts-meca B1-B5 + améliorations ;
# prof-pedagogue B1-B5 + améliorations).
import os
ICI = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(ICI, 'brouillon_6_21.py')
c = open(F, encoding='utf-8').read()


def R(a, b, n=1):
    global c
    assert c.count(a) == n, (a[:80], c.count(a))
    c = c.replace(a, b)


# ---------------------------------------------------------------- figures
R('''    p.append(_txt(46, oy + 20 * k + 56, "xG = (m1 × x1 + m2 × x2) / (m1 + m2) = (1 600 × 100 × 50 + 400 × 60 × 130) / (1 600 × 100 + 400 × 60) ≈ 60,4 mm", 12, TRAIT, "start", True))''',
  '''    p.append(_txt(46, oy + 20 * k + 56, "xG = (m1 x1 + m2 x2) / (m1 + m2) = (40² × 100 × 50 + 20² × 60 × 130) / (40² × 100 + 20² × 60) ≈ 60,4 mm", 12, TRAIT, "start", True))''')
# inertie_repartition : moyeu à l'échelle, même vitesse, libellés
R('''           (520, "MASSE PRÈS DE L'AXE", "J petit (moyeu)", 0.12, None))''',
  '''           (520, "MASSE PRÈS DE L'AXE", "J petit : matière près de l'axe", 0.117, None))''')
R('''        g = f"<g><animateTransform attributeName='transform' type='rotate' values='0 {cx} {cy}; 360 {cx} {cy}' dur='{2 + 4 * f:.1f}s' repeatCount='indefinite'/>"''',
  '''        g = f"<g><animateTransform attributeName='transform' type='rotate' values='0 {cx} {cy}; 360 {cx} {cy}' dur='4s' repeatCount='indefinite'/>"''')
R('''            g += f"<circle cx='{cx}' cy='{cy}' r='26' fill='#94a3b8' stroke='{TRAIT}' stroke-width='2'/>"''',
  '''            g += f"<circle cx='{cx}' cy='{cy}' r='30' fill='#94a3b8' stroke='{TRAIT}' stroke-width='2'/>"''')
R('''        p.append(f"<circle cx='{cx}' cy='{cy}' r='4' fill='{TRAIT}'/>")
        p.append(_txt(cx, 236, form, 12, ARBRE, "middle", True))''',
  '''        p.append(f"<circle cx='{cx}' cy='{cy}' r='4' fill='{TRAIT}'/>")
        p.append(_txt(cx, cy + 82, "axe de rotation au centre ; rayon extérieur R", 9, FIN, "middle"))
        if typ is None:
            p.append(_txt(cx, cy - 68, "même rayon R (vide)", 9, FIN, "middle"))
        p.append(_txt(cx, 236 + 4, form, 12, ARBRE, "middle", True))''')
R('''        p.append(f"<rect x='{x0 + 20}' y='248' width='{185 * f:.0f}' height='12' rx='3' fill='{ARBRE}' opacity='0.7'/>")
        p.append(_txt(x0 + 20, 272, "inertie (barre proportionnelle)", 9, FIN))''',
  '''        p.append(f"<rect x='{x0 + 20}' y='250' width='{185 * f:.0f}' height='10' rx='3' fill='{ARBRE}' opacity='0.7'/>")
        p.append(_txt(x0 + 20, 272, "inertie (barre proportionnelle)", 9, FIN))''')
# huygens
R('''    p.append(_txt(cx, cy + 22, "G : axe (G)", 11, ALESAGE, "middle", True))''',
  '''    p.append(_txt(cx, cy + 22, "G : axe (G)", 11, ALESAGE, "middle", True))
    p.append(_txt(cx + 55, cy + 70, "axes perpendiculaires à l'écran", 9, FIN, "middle"))''')
# pfd_treuil : sens de Cm, T sur le tambour, cote r, animation à sens unique
R('''    p.append(f"<path d='M {cx + 18} {cy - 24} A 30 30 0 0 1 {cx + 24} {cy + 18}' fill='none' stroke='{ALESAGE}' stroke-width='2.4' marker-end='url(#kb)'/>")
    p.append(_txt(cx - 54, cy + 4, "Cm", 13, ALESAGE, "middle", True))''',
  '''    p.append(f"<path d='M {cx + 24} {cy + 18} A 30 30 0 0 0 {cx + 18} {cy - 24}' fill='none' stroke='{ALESAGE}' stroke-width='2.4' marker-end='url(#kb)'/>")
    p.append(_txt(cx + 2, cy - 14, "Cm", 12, ALESAGE, "middle", True))
    p.append(f"<line x1='{cx}' y1='{cy + 8}' x2='{cx + r}' y2='{cy + 8}' stroke='{TRAIT}' stroke-width='1'/>")
    p.append(_txt(cx + r / 2, cy + 22, "r", 11, TRAIT, "middle", True))
    p.append(_k_fl(cx + r + 4, cy + 6, cx + r + 4, cy + 44, OK, "kg", 2))
    p.append(_txt(cx - 2, cy + 62, "T tire le tambour vers le bas", 9, OK, "end", True))''')
R('''    p.append(f"<g><animateTransform attributeName='transform' type='translate' values='0,0; 0,-14; 0,0' dur='3s' repeatCount='indefinite'/>"''',
  '''    p.append(f"<g><animateTransform attributeName='transform' type='translate' values='0,0; 0,-14' dur='2s' repeatCount='indefinite'/>"''')
R('''    for i, (t, c, g) in enumerate((("1. J'isole la charge (translation) :", TRAIT, True),
                                   ("T − m g = m a  →  T = m (g + a)", OK, True), ("", TRAIT, False),''',
  '''    for i, (t, c, g) in enumerate((("1. J'isole la charge (+ vers le haut) :", TRAIT, True),
                                   ("T − m g = m a  →  T = m (g + a)", OK, True), ("", TRAIT, False),''')
# equilibrage
R('''    p = [_k_defs(), _txt(30, 24, "Équilibrage d'un rotor : statique (G sur l'axe) et dynamique (axe principal = axe de rotation)", 13, TRAIT, "start", True)]''',
  '''    p = [_k_defs(), _txt(30, 24, "Équilibrage d'un rotor : statique (G sur l'axe) et dynamique (les masses se compensent plan par plan)", 13, TRAIT, "start", True)]''')
R('''        p.append(_txt(ox + 8, oy + 34, "palier A", 9, FIN, "middle"))''',
  '''        p.append(_txt(ox + 8, oy + 34, "palier A", 9, FIN, "middle"))
        p.append(_txt(ox + 87, oy + 80, "rotor vu de côté (2 disques)", 9, FIN, "middle"))''')
R('''            p.append(_txt(ox + 87, oy + 66, "masse en trop (qui tourne)", 9, c, "middle", True))''',
  '''            p.append(_txt(ox + 87, oy + 66, "masse en trop (plan milieu)", 9, c, "middle", True))''')
R('''        if len(masses) == 2:
            p.append(_txt(ox + 87, oy - 62, "deux masses opposées, décalées", 9, c, "middle", True))''',
  '''        if len(masses) == 2:
            p.append(_txt(ox + 87, oy - 92, "deux masses opposées, décalées", 9, c, "middle", True))
            p.append(_k_fl(ox + 60, oy - 52, ox + 60, oy - 80, c, "ko", 2))
            p.append(_k_fl(ox + 115, oy + 52, ox + 115, oy + 74, c, "ko", 2))
            p.append(_txt(ox + 64, oy - 70, "F", 10, c, "start", True))
            p.append(_txt(ox + 119, oy + 70, "F", 10, c, "start", True))
            p.append(_txt(ox + 87, oy - 6, "z", 10, c, "middle", True))
            p.append(_txt(ox + 8, oy - 8, "↑", 12, c, "middle", True))
            p.append(_txt(ox + 167, oy + 30, "↓", 12, c, "middle", True))''')
R('''        p.append(_txt(x0 + 117, 258, ("" if nom == "ÉQUILIBRÉ" else ("test des couteaux : il roule" if "STATIQUE" in nom else "immobile sur couteaux, vibre en rotation")), 9, FIN, "middle"))''',
  '''        p.append(_txt(x0 + 117, 258, ("sur couteaux : ne roule pas ; en rotation : ne vibre pas" if nom == "ÉQUILIBRÉ" else ("test des couteaux : il roule" if "STATIQUE" in nom else "immobile sur couteaux, vibre en rotation")), 9, FIN, "middle"))''')
R('''    p.append(_txt(46, 342, "Dynamique : on annule aussi le couple — l'équilibreuse corrige dans DEUX plans.", 12, TRAIT, "start", True))''',
  '''    p.append(_txt(46, 342, "Dynamique : on annule aussi le couple (G sur l'axe ET masses compensées plan par plan) — DEUX plans.", 12, TRAIT, "start", True))''')
# dyn_balourd
R('''    p.append(f"<line x1='{ox}' y1='{oy}' x2='{ox + 320}' y2='{oy}' stroke='{TRAIT}' stroke-width='3'/>")
    for xp, nom, Rv in ((ox + 20, "A", RA), (ox + 300, "B", RB)):''',
  '''    p.append(f"<line x1='{ox}' y1='{oy}' x2='{ox + 320}' y2='{oy}' stroke='{TRAIT}' stroke-width='3'/>")
    p.append(_txt(ox + 320, oy - 6, "arbre", 9, FIN, "end"))
    for xp, nom, Rv in ((ox + 20, "A", RA), (ox + 300, "B", RB)):''')
R('''              (f"réaction tournante par palier : {_fr_court(RA, 0)} N", col, True), ("", TRAIT, False),''',
  '''              (f"effort tournant sur chaque palier : {_fr_court(RA, 0)} N", col, True),
              (("sur couteaux : il roule" if config == "statique" else "sur couteaux : il ne roule pas"), FIN, False),''')

# ---------------------------------------------------------------- cours
R('''**Centre de gravité G** : le point où l'on peut considérer que tout le poids s'applique. Pour une pièce
composée de volumes simples, G est le **barycentre** des centres de gravité des morceaux, pondérés par
leurs masses (la notion de barycentre est celle des fiches 7.5 et 8.1) :''',
  '''**Centre de gravité G** : le point où l'on peut considérer que tout le poids s'applique — le point où il
faut accrocher l'élingue pour que la pièce levée reste horizontale. Pour une pièce composée de volumes
simples, G est le **barycentre** des centres de gravité des morceaux, pondérés par leurs masses (la notion
de barycentre est celle de la fiche 7.5) :''')
R('''Ø20 × 60 mm (G2 à x = 130 mm). Même matériau : les masses sont proportionnelles aux volumes, et le volume
d'un cylindre est proportionnel à d² × L.''',
  '''Ø20 × 60 mm (G2 à x = 130 mm). Le volume d'un cylindre vaut π/4 × d² × L et ρ est le même partout : π/4
et ρ apparaissent en haut et en bas de la fraction et se simplifient, il reste d² × L.''')
R('''**Une pièce creuse** se traite en retirant le trou : on compte sa « masse » en **négatif**.

*Pourquoi G compte : le poids s'applique en G (statique, fiche 6.16)''',
  '''**Une pièce percée** = la pièce pleine **moins** le cylindre de matière enlevé (le « bouchon ») : dans la
somme, la masse du bouchon entre avec un signe moins, à la position de son centre.

*Exemple (données d'énoncé) : le tronçon Ø40 × 100 seul, percé depuis la face gauche d'un trou borgne
Ø20 × 50 (centre du bouchon à x = 25 mm). xG = (40² × 100 × 50 − 20² × 50 × 25) / (40² × 100 − 20² × 50) ≈
**53,6 mm** : G s'éloigne du côté percé.*

*Pourquoi G compte : le poids s'applique en G (statique, fiches 12.1 et 6.16)''')
R('''> **J = Σ mi × ri²** (kg·m²)

[[FIG:inertie_repartition]]

**Formules classiques des solides homogènes** (autour de leur axe de symétrie) :

| Solide | Moment d'inertie |
|---|---|
| cylindre plein, disque (rayon R) | J = ½ m R² |
| tube, couronne (rayons R et r) | J = ½ m (R² + r²) |
| anneau mince (rayon R) | J ≈ m R² |
| barre mince de longueur L, autour de son milieu | J = m L² / 12 |
| petite masse à la distance d de l'axe | J = m d² |''',
  '''> **J = Σ mi × ri²** (kg·m²)

*Pourquoi le carré ? Une masse à la distance r de l'axe se déplace à la vitesse v = r × ω : deux fois plus
loin, elle va deux fois plus vite. Son énergie cinétique vaut ½ m v² = ½ m (r ω)² = ½ (m r²) ω² : une
rotation se paie en m r², et J est simplement ce qui remplace m dans ½ m v² (fiche 6.20). C'est pour la même
raison qu'on ferme une porte sans effort en poussant près de la poignée, difficilement près des gonds.*

[[FIG:inertie_repartition]]

**Formules classiques des solides homogènes** (autour de l'axe indiqué) :

| Solide | Moment d'inertie |
|---|---|
| cylindre plein, disque (rayon R), autour de son axe de révolution | J = ½ m R² |
| tube, couronne (rayons R et r), autour de son axe de révolution | J = ½ m (R² + r²) |
| anneau mince (rayon R), autour de son axe | J ≈ m R² |
| barre mince de longueur L, autour d'un axe perpendiculaire passant par son milieu | J = m L² / 12 |
| petite masse à la distance d de l'axe | J = m d² |''')
R('''150 mm) donnerait environ deux fois plus : 22,2 × 0,15² ≈ 0,50 kg·m².

**Le théorème de Huygens** : pour un axe Δ parallèle à l'axe passant par G, à la distance d,''',
  '''150 mm) donnerait environ deux fois plus : 22,2 × 0,15² ≈ 0,50 kg·m². *Ce que veut dire 0,25 kg·m² : avec
un couple de 10 N·m, ce disque prend α = 10 / 0,25 = 40 rad/s², soit environ 8 s pour atteindre 3 000 tr/min
(314 rad/s) ; matière en jante, il lui en faudrait environ 16.*

**Le théorème de Huygens.** Quand une pièce tourne autour d'un axe Δ qui ne passe pas par G, elle fait deux
choses à la fois : son centre G décrit un cercle de rayon d autour de Δ, comme si toute la masse était en G
(cela coûte m d²), et la pièce pivote sur elle-même d'un tour à chaque tour (cela coûte J_G). C'est le cas
d'une pièce bridée de façon décentrée sur le plateau d'un tour. Les deux coûts s'ajoutent : pour un axe Δ
parallèle à l'axe passant par G, à la distance d,''')
R('''autour de l'axe du disque : ½ × 0,888 × 0,03² + 0,888 × 0,1² ≈ 0,0093 kg·m². Disque allégé : J ≈ 0,2497 −
4 × 0,0093 ≈ **0,213 kg·m²** (−15 %), pour une masse de 22,2 − 4 × 0,888 ≈ 18,6 kg (−16 %).*''',
  '''autour de l'axe du disque : ½ × 0,888 × 0,03² + 0,888 × 0,1² ≈ 0,0093 kg·m². Comme pour G, un trou se compte
en négatif : J(disque percé) = J(disque plein) − 4 × J(un bouchon) ≈ 0,2497 − 4 × 0,0093 ≈ **0,213 kg·m²**
(−15 %), pour une masse de 22,2 − 4 × 0,888 ≈ 18,6 kg (−16 %). L'inertie baisse à peu près autant que la
masse parce que les trous sont à mi-rayon ; percés plus près de la jante, ils feraient gagner nettement plus
d'inertie pour la même masse retirée.*''')
R('''**La matrice d'inertie.** Pour un solide qui peut tourner autour de n'importe quel axe, l'inertie se range
dans un tableau 3 × 3 : sur la diagonale, les moments d'inertie autour des trois axes x, y, z ; hors
diagonale, les **produits d'inertie**, qui mesurent la dissymétrie de la répartition de matière. **Un plan de
symétrie de la pièce annule les produits d'inertie qui le concernent** ; avec deux plans de symétrie
(cas d'une pièce de révolution), la matrice est **diagonale** dans les axes de symétrie : ce sont les **axes
principaux d'inertie**. En pratique, le logiciel de CAO la donne directement (propriétés de masse) ; il
faut savoir la lire, pas la calculer à la main.''',
  '''**La matrice d'inertie.** Une pièce n'a pas une seule inertie : elle en a une par axe — une bielle tourne
facilement autour de sa longueur, beaucoup moins « en hélice ». Le logiciel de CAO range ces valeurs dans un
tableau 3 × 3 (menu « propriétés de masse ») :

- **sur la diagonale**, Jx, Jy, Jz : les moments d'inertie autour des trois axes — les J de cette section ;
- **hors diagonale**, les **produits d'inertie** (Jxy, Jyz, Jxz) : ils mesurent si la matière est « penchée »
  par rapport aux axes (plus de matière en haut à droite et en bas à gauche que l'inverse, par exemple).

**Le rôle des symétries.** Si la pièce a un plan de symétrie, chaque morceau de matière d'un côté a son
jumeau de l'autre : un plan de symétrie annule les deux produits d'inertie qui font intervenir l'axe
perpendiculaire à ce plan. Avec deux plans de symétrie perpendiculaires, la matrice calculée en G est
**diagonale** dans les axes formés par leur droite commune et leurs deux normales : ce sont les **axes
principaux d'inertie** (une pièce de révolution en a une infinité autour de son axe).

**Ce que vous en ferez.** Lire dans la CAO si les produits d'inertie sont nuls (ou négligeables) dans le
repère de l'axe de rotation, calculé en G. S'ils ne le sont pas, la pièce aura un balourd dynamique en
tournant (§6). On ne calcule jamais cette matrice à la main.''')
R('''Pour un solide isolé, le PFD généralise l'équilibre de la statique (fiche 6.16) : la somme des efforts
extérieurs n'est plus nulle, elle produit l'accélération.

> **Translation rectiligne : Σ F ext = m × aG** (en projection sur la direction du mouvement)
> **Rotation autour d'un axe fixe Δ : Σ M_Δ(F ext) = J_Δ × θ̈**, avec θ̈ = d²θ/dt² = α (rad/s²)''',
  '''Pour un solide isolé, le PFD généralise l'équilibre de la statique (fiches 12.1 et 6.16) : la somme des
efforts extérieurs n'est plus nulle, elle produit l'accélération.

> **Translation rectiligne : Σ F ext = m × aG** (en projection sur la direction du mouvement), et
> Σ M_G(F ext) = 0, puisque le solide ne tourne pas. aG : accélération du centre de gravité (en
> translation, tous les points ont la même).

> **Rotation autour d'un axe fixe Δ : Σ M_Δ(F ext) = J_Δ × α**, avec α en rad/s² (on trouve aussi la
> notation θ̈ = d²θ/dt²).''')
R('''- *Charge isolée : T − m g = m a → T = 200 × (9,81 + 0,5) = **2 062 N**.*
- *Tambour isolé : Cm − r × T = J × α, avec α = a / r = 5 rad/s² → Cm = 0,25 × 5 + 0,1 × 2 062 ≈
  **207,5 N·m**.*''',
  '''- *Charge isolée (on compte positif vers le haut, dans le sens de a) : T − m g = m a → T = 200 × (9,81 +
  0,5) = **2 062 N**.*
- *Tambour isolé : T tire le bord du tambour vers le bas, à la distance r de l'axe ; son moment r × T
  s'oppose à Cm, d'où le signe moins : Cm − r × T = J × α, avec α = a / r = 5 rad/s² → Cm = 0,25 × 5 + 0,1 ×
  2 062 ≈ **207,5 N·m**.*''')
R('''- le **TEC** parle d'**énergie** et de **puissance** : il donne directement une vitesse atteinte ou une
  puissance, sans passer par les efforts intérieurs, qui ne travaillent pas.

**Le lien.** Multiplier le PFD par la vitesse donne le TEC en puissance : F × v = m × a × v = d(½ m v²)/dt,
et de même en rotation, C × ω = J × α × ω = d(½ J ω²)/dt.

*Vérification sur le treuil, à l'instant où la charge monte à v = 1 m/s (ω = v / r = 10 rad/s) :
puissance du moteur Cm × ω = 207,45 × 10 ≈ 2 075 W. Variation d'énergie par seconde : J ω α + m v a + m g v
= 0,25 × 10 × 5 + 200 × 1 × 0,5 + 200 × 9,81 × 1 = 12,5 + 100 + 1 962 ≈ **2 075 W**. Même résultat : les
deux portes mènent au même endroit.*''',
  '''- le **TEC** parle d'**énergie** et de **puissance** : il donne directement une vitesse atteinte ou une
  puissance, sans passer par les efforts intérieurs, dont la puissance totale est nulle tant que les
  liaisons sont sans frottement.

*Le PFD, c'est le détail des virements (qui pousse, avec quelle force) ; le TEC, c'est le relevé de compte
(combien d'énergie entre, où elle va). Au bureau d'études, le PFD donne le **couple** et la **tension**, qui
servent à choisir le réducteur et à dimensionner le câble et l'arbre ; le TEC donne la **puissance**, qui
sert à choisir le moteur sur sa plaque.*

**Le lien.** Une puissance est une force × une vitesse (fiche 6.20). Multiplions le PFD de la charge par sa
vitesse v : (T − m g) × v = m a × v. Le membre de droite, m a v, est l'énergie cinétique gagnée par seconde :
pendant un petit instant Δt, la vitesse passe de v à v + a Δt, et ½ m v² augmente d'environ m v a Δt. Donc
T v = m v a + m g v : la puissance fournie par le câble remplit l'énergie cinétique (m v a) **et** l'énergie
de position (la charge monte de v mètres par seconde et gagne m g v joules chaque seconde). Même chose en
rotation : C × ω = J α ω, l'énergie cinétique du tambour gagnée par seconde.

*Vérification sur le treuil, à l'instant où la charge monte à v = 0,8 m/s (ω = v / r = 8 rad/s) : le moteur
fournit Cm × ω = 207,45 × 8 ≈ 1 660 W. Où va cette puissance ? J ω α = 0,25 × 8 × 5 = 10 W pour faire tourner
le tambour plus vite ; m v a = 200 × 0,8 × 0,5 = 80 W pour faire aller la charge plus vite ; m g v = 200 × 9,81
× 0,8 ≈ 1 570 W pour la monter. Total ≈ **1 660 W** : les deux portes mènent au même endroit.*

*Pourquoi le TEC « saute » la tension du câble : si l'on regarde tout le treuil d'un coup (tambour + câble +
charge), T devient un effort intérieur. Il donne T × v à la charge et en reprend exactement autant au tambour
(r × T × ω = T × v) : dans le bilan global, il s'annule. Le PFD oblige à couper le système en morceaux, et
c'est pour ça qu'il donne T.*''')
R('''Une pièce qui tourne n'est jamais parfaitement répartie autour de son axe. Le défaut se modélise par une
petite masse en trop mb à la distance r de l'axe : c'est le **balourd**. En rotation, cette masse décrit un
cercle : elle a une accélération centripète r × ω², donc l'arbre doit la retenir par une force''',
  '''Une pièce qui tourne n'est jamais parfaitement répartie autour de son axe. Le défaut se modélise par une
petite masse en trop mb à la distance r de l'axe : c'est le **balourd**, chiffré par U = mb × r (en g·mm), qui
ne dépend pas de la vitesse. *Faites tourner un seau d'eau à bout de bras : votre main doit tirer en
permanence vers le centre, de plus en plus fort quand vous accélérez.* En rotation, la masse en trop décrit
un cercle : elle a une accélération centripète r × ω², donc l'arbre doit la retenir par une force''')
R('''> **F = mb × r × ω²** — une force qui **tourne avec la pièce**, et qui croît comme le carré de la vitesse.''',
  '''> **F = mb × r × ω²** — la **force de balourd** : elle **tourne avec la pièce** (en haut, sur le côté, en
> bas, à chaque tour) et croît comme le carré de la vitesse.''')
R('''**Équilibrage statique : ramener G sur l'axe.** Si G n'est pas sur l'axe, la pièce posée sur deux
**couteaux** horizontaux roule''',
  '''**Équilibrage statique : ramener G sur l'axe.** Si G n'est pas sur l'axe, la pièce posée sur deux
**couteaux** (deux règles d'acier horizontales à arête fine, sur lesquelles on pose les tourillons de
l'arbre : il y roule presque sans frottement) roule''')
R('''**Équilibrage dynamique : l'axe principal d'inertie confondu avec l'axe de rotation.** Deux balourds égaux,
opposés, mais situés dans des plans différents : G reste sur l'axe (la pièce ne roule pas sur les couteaux),
mais en rotation les deux forces forment un **couple qui tourne** et secoue les deux paliers en opposition.
Ce défaut ne se voit qu'en rotation. En termes d'inertie : un produit d'inertie n'est pas nul, l'axe de
rotation n'est pas un axe principal. On le corrige en ajoutant (ou retirant) de la matière dans **deux
plans** : c'est le travail d'une **équilibreuse**, qui mesure les efforts aux paliers en rotation. Obligatoire
pour une pièce longue (rotor de moteur, arbre de transmission, cylindre).''',
  '''**Équilibrage dynamique : l'axe de rotation confondu avec un axe principal central d'inertie** (un axe
principal qui passe par G). Deux balourds égaux, opposés, mais situés dans des plans différents : G reste sur
l'axe, mais en rotation les deux forces forment un **couple qui tourne** et secoue les deux paliers en
opposition.

**Pourquoi les couteaux ne voient rien.** Sur couteaux, la pièce est presque immobile : la seule force qui
agit est son poids, et le poids ne « voit » que la position de G. Or deux masses égales et opposées laissent G
sur l'axe : rien ne fait rouler la pièce. Les forces mb r ω², elles, n'existent qu'en rotation. Une fois la
pièce lancée, chaque masse tire vers l'extérieur dans son propre plan ; comme les deux plans sont décalés le
long de l'axe, les deux tractions ne s'annulent pas : elles forment un couple qui cherche à faire **basculer**
l'arbre. *Prenez un manche à balai par les deux bouts, poussez un bout vers le haut et l'autre vers le bas :
le balai ne monte pas, il pivote.* Les paliers doivent empêcher ce basculement, et comme le couple tourne avec
la pièce, ils sont secoués à chaque tour.

**Ce que veut dire « axe principal central ».** L'axe est principal et passe par G quand la matière est
« rangée en paires » autour de lui : à chaque petite masse correspond une masse jumelle diamétralement
opposée, **dans le même plan**. En rotation, les tractions des jumelles s'annulent plan par plan : ni force ni
couple. Le balourd statique, c'est une masse sans jumelle (une force) ; le balourd dynamique, ce sont des
jumelles **décalées de plan** (un couple). Le produit d'inertie mesure ce décalage : pour les deux balourds de
l'exemple ci-dessous, à y = +150 mm, z = +20 mm et y = −150 mm, z = −20 mm, Σ m y z = 2 × 0,010 × 0,15 × 0,02 ≠
0 ; ramenés dans le même plan (z = 0), ce produit est nul et le couple disparaît.

*L'image du garagiste : pour équilibrer une roue de voiture, on pose des masses de plomb sur le bord
intérieur et sur le bord extérieur de la jante : ce sont les deux plans de correction.*

**Pourquoi deux plans.** Une seule masse corrective peut annuler la force ou le couple, pas les deux. On
corrige donc dans **deux plans** : c'est le travail d'une **équilibreuse**, qui mesure les efforts aux paliers
en rotation. Obligatoire pour une pièce longue (rotor de moteur, arbre de transmission, cylindre) : le couple
vaut F × z, et plus la pièce est longue, plus deux défauts peuvent être éloignés. Sur un disque mince, z ≈ 0 :
le couple reste négligeable et un équilibrage statique suffit.''')
R('''*Exemple (données d'énoncé) : deux balourds de 10 g à 150 mm, opposés, sur les deux faces du rotor (40 mm
d'écart). Résultante nulle ; couple tournant 148 × 0,04 ≈ **5,9 N·m** ; avec des paliers à 200 mm l'un de
l'autre, chacun reçoit ≈ 5,9 / 0,2 ≈ **30 N**, en sens opposés, qui tournent.*''',
  '''*Exemple (données d'énoncé ; calcul d'ordre de grandeur pour comprendre — en BTS, l'équilibrage se traite à
l'équilibreuse ou au logiciel) : deux balourds de 10 g à 150 mm, opposés, sur les deux faces du rotor (40 mm
d'écart). Résultante nulle ; couple tournant 148 × 0,04 ≈ **5,9 N·m**. Les paliers doivent opposer un couple
égal et contraire : deux forces R opposées, distantes de L = 0,2 m, donnent R × L = C, donc R = C / L ≈ 5,9 /
0,2 ≈ **30 N** par palier, en sens opposés, qui tournent.*''')
R('''**La tolérance d'équilibrage** se choisit avec la norme ISO 21940-11, selon le type de machine et sa vitesse :
on ne vise jamais un balourd nul, mais un balourd résiduel admissible.''',
  '''**La tolérance d'équilibrage** se choisit avec la norme ISO 21940-11 (rotors à comportement rigide) : le
balourd résiduel admissible, en g·mm, dépend du type de machine (classe de qualité G), de sa vitesse maximale
de service et de la masse du rotor. On ne vise jamais un balourd nul : il est inaccessible et coûterait de
plus en plus cher à approcher ; on vise ce que la machine supporte à sa vitesse.''')
R('''1. **Calculer xG avec les volumes de matériaux différents** : il faut les masses (ρ × V).
2. **Oublier le carré** dans J = m r² ou dans F = mb r ω² : doubler la vitesse multiplie le balourd par 4.
3. **Appliquer Huygens entre deux axes dont aucun ne passe par G** : la formule part toujours de J_G.''',
  '''1. **Pondérer par les volumes quand les matériaux sont différents** : il faut les masses (ρ × V).
2. **Oublier le carré** dans J = m r² ou dans F = mb r ω² : doubler la vitesse multiplie la force de balourd
   par 4.
3. **Appliquer Huygens entre deux axes dont aucun ne passe par G** : la formule part toujours de J_G. Pour
   aller d'un axe A à un axe B, passer par G : on retire m d_A², puis on ajoute m d_B².''')
R('''- **PFD** : Σ F = m aG (translation), Σ M_Δ = J θ̈ (rotation) ; méthode de la statique, « = m a » au lieu de
  « = 0 ».''',
  '''- **PFD** : Σ F = m aG (translation), Σ M_Δ = J α (rotation) ; méthode de la statique, « = m a » au lieu de
  « = 0 ».''')
R('''- **Balourd : F = mb r ω²**, force tournante. Statique : G sur l'axe (un plan) ; dynamique : axe principal
  = axe de rotation (deux plans).''',
  '''- **Balourd U = mb r** ; **force de balourd F = mb r ω²**, tournante. Statique : G sur l'axe (un plan) ;
  dynamique : G sur l'axe **et** produits d'inertie nuls — l'axe de rotation est un axe principal central
  (deux plans).''')
R('''**PFD** — translation : Σ F ext = m aG · rotation autour d'un axe fixe : Σ M_Δ = J_Δ θ̈ (θ̈ = α, rad/s²)''',
  '''**PFD** — translation : Σ F ext = m aG (et Σ M_G = 0) · rotation autour d'un axe fixe : Σ M_Δ = J_Δ α (rad/s²)''')
R('''**Balourd** — F = mb r ω² (ω = 2πN/60) · couple de deux balourds opposés distants de z : C = F z''',
  '''**Balourd** — U = mb r (g·mm) · force F = mb r ω² (ω = 2πN/60) · deux balourds opposés distants de z :
couple C = F z, repris par deux paliers distants de L : R = C / L''')

# cas industriel
R('''Mais la roue est large (deux flasques espacées)''', '''Mais la roue est large (deux flasques — les deux disques latéraux entre lesquels sont fixées les aubes —
espacées)''')

# exercice / corrigé
R('''**4.** Le défaut est en réalité deux balourds de 10 g, opposés, sur les deux faces du disque. Le rotor
roule-t-il sur couteaux ? Que reçoivent les paliers en rotation ?
""",''',
  '''**4.** Le défaut est en réalité deux balourds de 10 g, opposés, sur les deux faces du disque. Le rotor
roule-t-il sur couteaux ? Que reçoivent les paliers en rotation ?

**5.** Pour l'alléger, on perce le disque de 4 trous Ø60 traversants, dont les axes sont à 100 mm de son axe.
Calculer sa nouvelle masse et son nouveau moment d'inertie (théorème de Huygens).
""",''')
R('''> m = ρ V ; **J = ½ m R²** ; **PFD en rotation : C = J α** ; **TEC : Ec = ½ J ω²** ; **balourd : F = mb r ω²** ;
> deux balourds opposés décalés de z : **couple F × z**, réparti sur les paliers.''',
  '''> m = ρ V ; **J = ½ m R²** ; **PFD en rotation : C = J α** ; **TEC : Ec = ½ J ω²** ; **force de balourd :
> F = mb r ω²** ; deux balourds opposés décalés de z : **couple F × z**, repris par les paliers : **R = F z / L** ;
> **Huygens : J_Δ = J_G + m d²** (un trou se compte en négatif).''')
R('''**1.** m ≈ **22,2 kg** ; J ≈ ½ × 22,2 × 0,0225 ≈ **0,250 kg·m²**.

**2.** α = 314,2 / 2 ≈ **157,1 rad/s²** ; C = 0,250 × 157,1 ≈ **39,2 N·m**. TEC : Ec = ½ × 0,250 × 314,2² ≈
12 320 J ; puissance moyenne 12 320 / 2 ≈ **6 160 W** — et C × ω moyen = 39,2 × 157,1 ≈ 6 160 W : même
résultat.''',
  '''**1.** m ≈ **22,2 kg** ; J ≈ ½ × 22,2 × 0,0225 ≈ **0,2497 kg·m²** (≈ 0,25).

**2.** α = 314,2 / 2 ≈ **157,1 rad/s²** ; C = 0,2497 × 157,1 ≈ **39,2 N·m**. TEC : Ec = ½ × 0,2497 × 314,2² ≈
12 330 J ; puissance moyenne ≈ 12 330 / 2 ≈ **6 160 W**. Par le PFD : l'accélération étant constante, ω croît
régulièrement de 0 à 314,2 rad/s, sa valeur moyenne est la moitié, 157,1 rad/s ; C × ω moyen = 39,2 × 157,1 ≈
6 160 W : même résultat.''')
R('''en sens opposés, tournant à 50 Hz : balourd **dynamique**, à corriger dans deux plans.''',
  '''en sens opposés, tournant à 50 Hz : balourd **dynamique**, à corriger dans deux plans.

**5.** Un bouchon : m_t = 7 850 × π × 0,03² × 0,04 ≈ 0,888 kg ; J d'un bouchon autour de l'axe du disque :
½ × 0,888 × 0,03² + 0,888 × 0,1² ≈ 0,0093 kg·m². Disque allégé : m ≈ 22,2 − 4 × 0,888 ≈ **18,6 kg** ;
J ≈ 0,2497 − 4 × 0,0093 ≈ **0,213 kg·m²**.''')
R('''quatre fois plus faible (≈ 37 N).''', '''la force de balourd serait quatre fois plus faible (≈ 37 N).''')
R('''**Unités** : kg × m × (rad/s)² = N. **Bon sens** : le balourd croît comme ω² — à 1 500 tr/min, il serait
la force de balourd serait quatre fois plus faible (≈ 37 N).''',
  '''**Unités** : kg × m × (rad/s)² = N. **Bon sens** : la force de balourd croît comme ω² — à 1 500 tr/min, elle
serait quatre fois plus faible (≈ 37 N).''')

# méthode
R('''   "= 2 062 N. Tambour : Cm = J a / r + r T ≈ 1,25 + 206,2 ≈ 207,5 N·m. À v = 1 m/s : 2 075 W des deux côtés.")''',
  '''   "= 2 062 N. Tambour : Cm = J a / r + r T ≈ 1,25 + 206,2 ≈ 207,5 N·m. À v = 0,8 m/s : ≈ 1 660 W des deux côtés.")''')

# ateliers
R('''            {"type": "numerique", "label": "Puissance motrice à v = 1 m/s",
             "unite": "W", "attendu": 2074.5, "tol": 5,
             "consigne": "À l'instant où la charge monte à 1 m/s, calcule la puissance du moteur Cm × ω.",
             "indice": "ω = v / r.",
             "pieges": [(207.45, "207 : tu as gardé ω = 1. ω = v / r = 1 / 0,1 = 10 rad/s.")],
             "aide": "ω = 10 rad/s ; P = 207,45 × 10 ≈ 2 075 W."},''',
  '''            {"type": "numerique", "label": "Puissance motrice à v = 0,8 m/s",
             "unite": "W", "attendu": 1659.6, "tol": 5,
             "consigne": "À l'instant où la charge monte à 0,8 m/s, calcule la puissance du moteur Cm × ω.",
             "indice": "ω = v / r.",
             "pieges": [(165.96, "166 : tu as gardé ω = 0,8. ω = v / r = 0,8 / 0,1 = 8 rad/s.")],
             "aide": "ω = 8 rad/s ; P = 207,45 × 8 ≈ 1 660 W."},''')
R('''             "question": "Cette puissance vaut 12,5 + 100 + 1 962 W. Que représentent ces trois termes ?",
             "options": ["Les pertes du moteur, du réducteur et du câble",
                         "Les puissances de trois moteurs différents",
                         "Ec du tambour par seconde, Ec de la charge par seconde, et l'énergie potentielle gagnée par seconde"],''',
  '''             "question": "Cette puissance vaut 10 + 80 + 1 570 W. Que représentent ces trois termes ?",
             "options": ["Les pertes du moteur, du réducteur et du câble",
                         "Les puissances de trois moteurs différents",
                         "Variation par seconde de l'Ec du tambour (J ω α), de l'Ec de la charge (m v a), et "
                         "énergie potentielle gagnée par seconde (m g v)"],''')
R('''            "remplacement": "T = 200 × 10,31 ; α = 0,5 / 0,1 ; Cm = 0,25 × 5 + 0,1 × 2 062 ; P = Cm × 10.",
            "calcul": "**T = 2 062 N** ; **α = 5 rad/s²** ; **Cm ≈ 207,5 N·m** ; **P ≈ 2 075 W**.",
            "verification": "TEC : 0,25 × 10 × 5 + 200 × 1 × 0,5 + 200 × 9,81 × 1 = 12,5 + 100 + 1 962 ≈ 2 075 W : "
                            "les deux portes donnent la même puissance.",''',
  '''            "remplacement": "T = 200 × 10,31 ; α = 0,5 / 0,1 ; Cm = 0,25 × 5 + 0,1 × 2 062 ; P = Cm × 8.",
            "calcul": "**T = 2 062 N** ; **α = 5 rad/s²** ; **Cm ≈ 207,5 N·m** ; **P ≈ 1 660 W**.",
            "verification": "TEC : 0,25 × 8 × 5 + 200 × 0,8 × 0,5 + 200 × 9,81 × 0,8 = 10 + 80 + 1 569,6 ≈ 1 660 W : "
                            "les deux portes donnent la même puissance.",''')
R('''                             1: "Un seul moteur : ce sont trois destinations de la même puissance (J ω α, m v a, "
                                "m g v)."}},''', '''                             1: "Un seul moteur : ce sont trois destinations de la même puissance (J ω α, m v a, "
                                "m g v)."}},''')
R('''            ("Équilibrage dynamique",
             "rendre l'axe de rotation axe principal d'inertie : correction dans deux plans."),''',
  '''            ("Équilibrage dynamique",
             "faire en sorte que les masses se compensent plan par plan (axe de rotation = axe principal d'inertie "
             "passant par G) : ni force ni couple tournants ; correction dans deux plans."),''')
R('''             "pieges": [(74.02, "74 N, c'est la moitié de F : ce serait le cas d'un balourd STATIQUE (une seule masse, "
                                "partagée entre les deux paliers). Ici, les deux forces forment un couple.")],''',
  '''             "pieges": [(74.02, "74 N, c'est la moitié de F : ce serait le cas d'un balourd STATIQUE (une seule masse, "
                                "partagée entre les deux paliers). Ici, les deux forces forment un couple."),
                        (5.92, "5,92, c'est le couple tournant, en N·m. Chaque palier le reprend avec un bras de levier "
                               "de 0,2 m : R = C / 0,2."),
                        (14.8, "14,8 N : tu as encore partagé en deux. Le couple est repris en entier par le couple des "
                               "deux réactions, R × 0,2 = C.")],''')

# générateurs
R('''        if abs(val - F) > max(0.5, F * 0.02) * 2 and all(abs(val - d["v"]) > 0.5 for d in diag):''',
  '''        if abs(val - F) > max(0.05, F * 0.02) * 2 and all(abs(val - d["v"]) > 0.05 for d in diag):''')
R('''        "rep": round(F, 2), "tol": max(0.5, F * 0.02), "unite": "N",''',
  '''        "rep": round(F, 2), "tol": max(0.05, F * 0.02), "unite": "N",''')
R('''            "**Ce que cela apprend.** La force croît comme le carré de la vitesse : doubler N multiplie le balourd "
            "par 4. C'est pourquoi une machine rapide exige un équilibrage plus soigné.",''',
  '''            "**Ce que cela apprend.** Le balourd (mb × r) ne change pas, mais sa force croît comme le carré de la "
            "vitesse : doubler N multiplie la force de balourd par 4. C'est pourquoi une machine rapide exige un "
            "équilibrage plus soigné.",''')
R('''            f"**Les poids relatifs.** d1² × L1 = {v1} ; d2² × L2 = {v2}.",''',
  '''            f"**Les parts de masse (∝ d² × L).** d1² × L1 = {v1} ; d2² × L2 = {v2}.",''')
R('''        "titre": "Dynamique — centre de gravité d'un arbre étagé",''',
  '''        "titre": "Géométrie des masses — centre de gravité d'un arbre étagé",''')

open(F, 'w', encoding='utf-8').write(c)
print("corrigé")
