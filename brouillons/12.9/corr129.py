# Corrections du brouillon 12.9 après les deux relectures (bloquants techniques B1-B8, pédagogiques B1-B5).
import os
ICI = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(ICI, 'brouillon_12_9.py')
c = open(P, encoding='utf-8').read()


def R(a, b, n=1):
    global c
    assert c.count(a) == n, (a[:70], c.count(a))
    c = c.replace(a, b)


# --- fiche entière remplacée par la version 2
i = c.index("FICHE_12_9 = {")
j = c.index("\n# ===========================================================================\n# 3. MÉTHODE")
c = c[:i] + open(os.path.join(ICI, 'fiche_v2.py'), encoding='utf-8').read().rstrip() + "\n" + c[j:]

# --- en-tête : sources
R("""# - σ éq ≤ Rpe = Re / s et Von Mises : fiche 12.2 de l'appli ; Kt et fatigue : fiche 3.5.""",
  """# - σ éq ≤ Rpe = Re / s et Von Mises : fiche 12.2 de l'appli ; Kt : fiche 4.1 ; fatigue : fiche 3.5 ;
#   I/v = b h²/6 : fiche 4.3 ; E = 210 000 MPa (acier) : table MATERIAUX ; STEP/STL : fiches 12.4 et 13.7.
# - Appuis trop étendus : la flèche est sous-estimée ; les contraintes sont faussées dans les deux sens
#   (vérifié par le relecteur sur un petit modèle éléments finis : pic artificiel au bord de la zone bloquée).""")

# --- B4/B5 : repères « élément » et « nœud » sur de vrais éléments
R("""    p.append(f"<polygon points='110,120 110,180 170,120' fill='#fde68a' stroke='{ARBRE}' stroke-width='1.4'/>")
    p.append(_k_fl(200, 150, 150, 148, ARBRE, "ko", 1.4))""",
  """    p.append(f"<polygon points='50,120 50,180 110,120' fill='#fde68a' stroke='{ARBRE}' stroke-width='1.4'/>")
    p.append(_k_fl(200, 150, 76, 146, ARBRE, "ko", 1.4))""")
R("""    p.append(_k_fl(200, 104, 174, 118, TRAIT, "kk", 1.4))""",
  """    p.append(_k_fl(200, 104, 114, 118, TRAIT, "kk", 1.4))""")

# --- conditions aux limites : la même pièce réelle, trois déclarations
R("""    p = [_k_defs(), _txt(30, 24, "Conditions aux limites : dire au logiciel comment la pièce est tenue et chargée", 13, TRAIT, "start", True)]""",
  """    p = [_k_defs(), _txt(30, 24, "Conditions aux limites : dire au logiciel comment la pièce est tenue et chargée", 13, TRAIT, "start", True),
         _txt(30, 38, "Même pièce réelle (tenue par 2 vis sur un bâti), trois façons de la déclarer au logiciel :", 10, FIN, "start", True)]""")
R("""    cadres = ((20, "JUSTE", OK), (280, "TROP RIGIDE", ARBRE), (540, "PAS TENUE", ALERTE))
    for x, titre, c in cadres:
        p.append(f"<rect x='{x}' y='40' width='250' height='250' rx='8' fill='#ffffff' stroke='{c}' stroke-width='1.8'/>")""",
  """    cadres = ((20, "JUSTE", OK), (280, "TROP RIGIDE", ARBRE), (540, "PAS TENUE", ALERTE))
    for x, titre, c in cadres:
        p.append(f"<rect x='{x}' y='46' width='250' height='244' rx='8' fill='#ffffff' stroke='{c}' stroke-width='1.8'/>")""")
R("""    p.append(_txt(145, 206, "fixée là où sont les vis,", 10, TRAIT, "middle"))
    p.append(_txt(145, 220, "force répartie sur la vraie", 10, TRAIT, "middle"))
    p.append(_txt(145, 234, "surface d'appui", 10, TRAIT, "middle"))
    p.append(_txt(145, 262, "déformée (pointillé) réaliste", 10, OK, "middle", True))
    # TROP RIGIDE : toute la moitié gauche encastrée
    _fe_hachures(p, 290, 150, 130, 30)
    _fe_plaque(p, 290, 134, False)
    p.append(f"<path d='M 420 142 Q 470 143 510 154' fill='none' stroke='{ALERTE}' stroke-width='1.2' stroke-dasharray='5 3'/>")
    p.append(_txt(405, 206, "toute une face bloquée alors", 10, TRAIT, "middle"))
    p.append(_txt(405, 220, "que la pièce ne tient que", 10, TRAIT, "middle"))
    p.append(_txt(405, 234, "par deux vis", 10, TRAIT, "middle"))
    p.append(_txt(405, 256, "pièce plus raide qu'en réalité :", 10, ARBRE, "middle", True))
    p.append(_txt(405, 270, "flèche et contraintes sous-estimées", 10, ARBRE, "middle", True))
    # PAS TENUE : aucune fixation
    _fe_plaque(p, 560, 134, False)""",
  """    p.append(_txt(145, 206, "déclarée fixée sur les trous de vis,", 10, TRAIT, "middle"))
    p.append(_txt(145, 220, "en appui sur le bâti ; force sur", 10, TRAIT, "middle"))
    p.append(_txt(145, 234, "la vraie surface d'appui", 10, TRAIT, "middle"))
    p.append(_txt(145, 262, "déformée calculée réaliste", 10, OK, "middle", True))
    # TROP RIGIDE : même bâti, mêmes vis ; mais la moitié gauche est DÉCLARÉE bloquée
    _fe_hachures(p, 290, 150, 60, 30)
    _fe_plaque(p, 290, 134, False)
    for xv in (304, 334):
        p.append(f"<line x1='{xv}' y1='126' x2='{xv}' y2='176' stroke='{TRAIT}' stroke-width='3'/>")
    p.append(f"<rect x='290' y='130' width='120' height='24' fill='{ARBRE}' fill-opacity='0.35' stroke='{ARBRE}' stroke-dasharray='4 2'/>")
    p.append(_txt(350, 124, "zone déclarée bloquée", 9, ARBRE, "middle", True))
    p.append(f"<path d='M 410 142 Q 470 143 510 154' fill='none' stroke='{ALERTE}' stroke-width='1.2' stroke-dasharray='5 3'/>")
    p.append(_txt(470, 168, "déformée calculée", 9, ALERTE, "middle"))
    p.append(_txt(320, 196, "bâti + vis", 9, FIN, "middle"))
    p.append(_txt(405, 214, "toute une zone bloquée alors", 10, TRAIT, "middle"))
    p.append(_txt(405, 228, "que la pièce ne tient que par", 10, TRAIT, "middle"))
    p.append(_txt(405, 242, "deux vis : modèle trop raide", 10, TRAIT, "middle"))
    p.append(_txt(405, 260, "flèche sous-estimée,", 10, ARBRE, "middle", True))
    p.append(_txt(405, 274, "contraintes faussées", 10, ARBRE, "middle", True))
    # PAS TENUE : même pièce, aucune fixation déclarée (bâti dessiné en pointillé : ignoré par le logiciel)
    p.append(f"<rect x='570' y='150' width='60' height='30' fill='none' stroke='{FIN}' stroke-dasharray='4 3'/>")
    p.append(_txt(600, 196, "bâti non déclaré", 9, FIN, "middle"))
    _fe_plaque(p, 560, 134, False)""")
R("""    p.append(_txt(665, 206, "aucune fixation déclarée :", 10, TRAIT, "middle"))
    p.append(_txt(665, 220, "la pièce peut se déplacer", 10, TRAIT, "middle"))
    p.append(_txt(665, 234, "librement sous la force", 10, TRAIT, "middle"))""",
  """    p.append(_txt(665, 214, "aucune fixation déclarée :", 10, TRAIT, "middle"))
    p.append(_txt(665, 228, "la pièce peut glisser en bloc", 10, TRAIT, "middle"))
    p.append(_txt(665, 242, "sous la force", 10, TRAIT, "middle"))""")

# --- B3 : carte de Von Mises en vue de côté, σ = M y / I (nulle sur la fibre neutre)
R("""    n = 11
    for k in range(n):
        frac = 1 - (k + 0.5) / n          # 1 à l'encastrement, 0 au bout
        sig = 156 * frac                  # MPa, données d'énoncé (calcul à la main du § 4)
        idx = min(6, int(sig / (240 / 7)))
        p.append(f"<rect x='{x0 + k * L / n:.1f}' y='{y}' width='{L / n + 0.5:.1f}' height='{h}' fill='{_FE_COUL[idx]}'/>")""",
  """    n, nr = 11, 6
    for k in range(n):
        for j in range(nr):
            yrel = max(abs(j / nr - 0.5), abs((j + 1) / nr - 0.5)) * 2
            sig = 156 * (1 - k / n) * yrel      # σ = M y / I : maxi sur les faces, nulle sur la fibre neutre
            idx = min(6, int(sig / (240 / 7)))
            p.append(f"<rect x='{x0 + k * L / n:.1f}' y='{y + j * h / nr:.1f}' width='{L / n + 0.5:.1f}' "
                     f"height='{h / nr + 0.5:.1f}' fill='{_FE_COUL[idx]}'/>")""")
R("""    p.append(_txt(154, 84, "pic rouge à l'angle vif : 380 MPa affichés", 10, ALERTE, "start", True))""",
  """    p.append(_txt(154, 84, "pic rouge au coin plat / bâti (angle vif) : 380 MPa affichés", 10, ALERTE, "start", True))""")
R("""    p.append(_txt(x0 + 75, y + h + 22, "zone la plus sollicitée :", 10, TRAIT, "middle", True))
    p.append(_txt(x0 + 75, y + h + 36, "près de l'encastrement", 10, TRAIT, "middle"))
    p.append(_txt(x0 + 75, y + h + 50, "≈ 150 MPa (orange-jaune)", 10, TRAIT, "middle"))""",
  """    p.append(_txt(x0 + 90, y + h + 22, "zone la plus sollicitée : faces haute et", 10, TRAIT, "middle", True))
    p.append(_txt(x0 + 90, y + h + 36, "basse près de l'encastrement ≈ 150 MPa (jaune)", 10, TRAIT, "middle"))
    p.append(_txt(x0 + 90, y + h + 50, "fibre neutre (milieu) : presque 0", 10, TRAIT, "middle"))""")
R("""    p.append(_txt(x0 + L / 2, y + h / 2 + 4, "plaque en S235 (Re = 235 MPa)", 10, "#ffffff", "middle", True))""",
  """    p.append(_txt(x0 + L / 2, y - 8, "plat en S235 (Re = 235 MPa), vu de côté", 10, TRAIT, "middle", True))""")
R("""    p.append(_txt(46, 328, "Exemple pédagogique : résultats fournis (données d'énoncé).", 10, FIN, "start"))""",
  """    p.append(_txt(46, 328, "Exemple pédagogique (données d'énoncé). Échelle arrêtée à 240 MPa pour lire la pièce : le pic de 380 la dépasse.", 10, FIN, "start"))""")
R('''"plaque en porte-à-faux de 220 × 16''', '''"plat en porte-à-faux de 220 × 16''') if '"plaque en porte-à-faux de 220 × 16' in c else None
R("""    p.append(_txt(500, 222, "congé : se stabilise (≈ 175)", 10, OK, "end", True))""",
  """    p.append(_txt(500, 222, "congé : se stabilise (≈ 175) — pic qui se pose, pic qui compte", 10, OK, "end", True))""")
R("""    p.append(_txt(430, 70, "angle vif : ne se stabilise jamais", 10, ALERTE, "end", True))""",
  """    p.append(_txt(430, 70, "angle vif : ne se stabilise jamais — pic qui grimpe, pic qui trompe", 10, ALERTE, "end", True))""")
# PDM : maillon « Qualification », PDM relié aux maillons
R('''    maillons = ("Maquette 3D", "Simulation", "Prototype", "Outillage", "Production", "Contrôle")''',
  '''    maillons = ("Maquette 3D", "Simulation", "Prototype", "Outillage", "Production", "Qualification")''')
R('''    p.append(_txt(400, 162, "toutes les données du projet, rangées et suivies", 10, TRAIT, "middle"))''',
  '''    p.append(_txt(400, 162, "chaque maillon y dépose et y lit ses fichiers", 10, TRAIT, "middle"))
    for xm in (85, 335, 465, 715):
        p.append(f"<line x1='{xm}' y1='104' x2='{250 if xm < 400 else 550}' y2='150' stroke='{ARBRE}' stroke-width='0.8'/>")''')
R('''    p.append(_txt(46, 338, "Échange entre logiciels : format neutre STEP (ISO 10303) pour la 3D, STL pour l'impression (fiche 13.7).", 12, TRAIT, "start", True))''',
  '''    p.append(_txt(46, 338, "Échange : format neutre STEP (ISO 10303) pour la 3D, STL pour l'impression (fiches 12.4, 13.7). PLM : tout le cycle de vie.", 11, TRAIT, "start", True))''')

# --- méthode
R("""    "**Recouper à la main** : un ordre de grandeur de RDM (σ = M / (I/v)…) doit retrouver la simulation loin des "
    "singularités.",""",
  """    "**Recouper à la main** : un ordre de grandeur de RDM (σ = M / (I/v)…) doit retrouver la simulation loin des "
    "singularités ; si la simulation trouve nettement moins, chercher l'erreur et garder la valeur la plus défavorable.",""")
R("""    "→ vraie concentration (fiche 3.5, fatigue).",""", """    "→ vraie concentration (fiches 4.1 et 3.5, fatigue).",""")
R("""    "**Conclure** : s = Re / σ éq comparé au coefficient exigé ; si refusé, proposer une modification (épaisseur, "
    "congé) et une nouvelle révision dans le PDM.",""",
  """    "**Conclure** : s obtenu = Re / σ éq comparé au s exigé ; si refusé, proposer une modification (épaisseur, "
    "congé) et une nouvelle révision dans le PDM.",""")
R("""   "singularité ; congé ajouté : 170, 174, 175 MPa (converge) ; s = 235/175 ≈ 1,34 < 1,5 → refusé.")""",
  """   "singularité ; congé ajouté : 170, 174, 175 MPa (converge) ; s obtenu = 235/175 ≈ 1,34 < 1,5 exigé → refusé.")""")

# --- at180
R(""""enonce": "Une plaque en S235 (Re = 235 MPa), de section b × h = 30 × 8 mm, est encastrée et reçoit une \"""",
  """"enonce": "Un plat en S235 (Re = 235 MPa), de section b × h = 30 × 8 mm (h dans le sens de la force), est \"""")
R("""                  "force F = 500 N à L = 100 mm de l'encastrement. La simulation fournie (figure) affiche environ "
                  "150 MPa près de l'encastrement et un pic de 380 MPa à l'angle vif de la fixation (données "
                  "d'énoncé).",""",
  """                  "encastré et reçoit une force F = 500 N à L = 100 mm de l'encastrement. La simulation fournie "
                  "(figure) affiche environ 150 MPa sur les faces haute et basse de la section d'encastrement et un "
                  "pic de 380 MPa à l'angle vif de la fixation (données d'énoncé).",""")
R("""             "aide": "s = 235 / 156,25 ≈ 1,50."},""",
  """             "aide": "s = 235 / 156,25 ≈ 1,50.",
             "depend_de": {"etape": 2, "formule": lambda v: 235 / v}},""")
R(""""calcul": "σ = 50 000 / 320 ≈ **156 MPa** ; s = 235 / 156 ≈ **1,50** ; le pic est une **singularité**.",""",
  """"calcul": "σ = 50 000 / 320 ≈ **156 MPa** ; s = 235 / 156,25 ≈ **1,50** ; le pic est une **singularité**.",""")
R(""""enonce": "Plaque S235, 30 × 8 mm,""", """"enonce": "Plat S235, 30 × 8 mm,""")

# --- at181 : B1 et B2
R(""""enonce": "L'équerre en S235 (Re = 235 MPa) de la fiche est recalculée avec un congé à la place de l'angle vif. "
                  "Le cahier des charges exige s ≥ 1,5 (données d'énoncé).",""",
  """"enonce": "L'équerre en S235 (Re = 235 MPa) de la fiche est recalculée avec un congé à la place de l'angle vif. "
                  "Le modèle retenu fixe l'équerre sur ses deux trous de vis, en appui sur le bâti. Le cahier des "
                  "charges exige s ≥ 1,5 (données d'énoncé).",""")
R("""             "question": "Dans le modèle, toute la face arrière de l'équerre est bloquée, alors que la vraie pièce ne "
                         "tient que par deux vis. Quel est l'effet sur le résultat ?",
             "options": ["Aucun : le logiciel corrige de lui-même",
                         "Le modèle est trop raide : flèche et contraintes sont sous-estimées",
                         "Le modèle est trop souple : les contraintes sont surestimées"], "bonne": 1,
             "indice": "Bloquer plus que la réalité, c'est rendre la pièce plus rigide.",
             "diagnostics": {0: "Le logiciel calcule exactement ce qu'on lui décrit ; il ne devine pas les vraies "
                                "fixations.",
                             2: "C'est l'inverse : bloquer davantage rigidifie le modèle, donc les contraintes "
                                "paraissent plus faibles."}},""",
  """             "question": "Un collègue propose de bloquer toute la face arrière de l'équerre, alors que la vraie pièce "
                         "ne tient que par deux vis. Quel serait l'effet sur le résultat ?",
             "options": ["Aucun : le logiciel corrige de lui-même",
                         "Le modèle serait trop raide : la flèche serait sous-estimée et les contraintes autour des "
                         "vis ne seraient pas représentées",
                         "Le modèle serait trop souple : la flèche serait surestimée"], "bonne": 1,
             "indice": "Bloquer plus que la réalité, c'est rendre la pièce plus rigide.",
             "diagnostics": {0: "Le logiciel calcule exactement ce qu'on lui décrit ; il ne devine pas les vraies "
                                "fixations.",
                             2: "C'est l'inverse : bloquer davantage rigidifie le modèle ; la pièce plie moins qu'en "
                                "réalité."}},""")
R("""             "aide": "s = 235 / 175 ≈ 1,34 : inférieur à 1,5, la pièce est refusée en l'état."},""",
  """             "aide": "s = 235 / 175 ≈ 1,34 : inférieur à 1,5, la pièce est refusée en l'état."},""")
R(""""regle": "**Appuis trop rigides** → contraintes sous-estimées ;""",
  """"regle": "**Appuis trop étendus** → modèle trop raide, flèche sous-estimée, contraintes faussées ;""")
R(""""calcul": "Modèle **trop raide** ; **175 MPa** exploitable ;""", """"calcul": "Modèle **trop raide** (à refuser) ; **175 MPa** exploitable ;""")
R("""                            "(σ maxi = Kt × σ nominale, fiche 3.5, avec Kt un peu supérieur à 1).",""",
  """                            "(σ maxi = Kt × σ nominale, fiches 4.1 et 3.5, avec Kt un peu supérieur à 1).",""")

# --- générateurs
R('''    sig = random.choice([v for v in range(90, 260, 5) if Re / v >= 1.05])
    pic = random.choice([v for v in range(int(Re * 1.4), int(Re * 2.6), 10)])''',
  '''    sig = random.choice([v for v in range(90, 260, 5) if Re / v >= 1.05])
    pic = random.choice([v for v in range(int(Re * 1.4), int(Re * 2.6), 10) if abs(Re / v - sig / Re) > 0.02])''')
R('''                   "raffinement. Quel est le coefficient de sécurité de la pièce ?"),''',
  '''                   "raffinement. Quel est le coefficient de sécurité de la pièce (arrondi au centième) ?"),''')
R('''    b = random.choice([20, 25, 30, 40, 50])
    h = random.choice([6, 8, 10, 12])
    F = random.choice([200, 300, 500, 800, 1000, 1200])
    L = random.choice([60, 80, 100, 120, 150])
    M = F * L
    w = b * h * h / 6
    sig = M / w''',
  '''    while True:   # pièce réaliste : poutre élancée (L/h ≥ 8) et contrainte comprise entre 30 et 250 MPa
        b = random.choice([20, 25, 30, 40, 50])
        h = random.choice([6, 8, 10])
        F = random.choice([200, 300, 500, 800, 1000, 1200])
        L = random.choice([60, 80, 100, 120, 150])
        M = F * L
        w = b * h * h / 6
        sig = M / w
        if L / h >= 8 and 30 <= sig <= 250:
            break''')
R('''                   f"(largeur × épaisseur fléchie) est encastrée et reçoit **{fr(F, 0)} N** à **{L} mm** de "''',
  '''                   f"(largeur × épaisseur h dans le sens de la force) est encastrée et reçoit **{fr(F, 0)} N** à **{L} mm** de "''')
R('''            _diag(M / (b * b * h / 6), "Tu as inversé b et h : c'est l'épaisseur fléchie h qui est au carré, "
                                       "I/v = b h² / 6."),''',
  '''            _diag(M / (b * b * h / 6), "Tu as inversé b et h : c'est l'épaisseur h, dans le sens de la force, "
                                       "qui est au carré : I/v = b h² / 6."),''')
R('''            f"**Le module de flexion.** I/v = b h² / 6 = {b} × {h}² / 6 = {fr(w, 1)} mm³.",''',
  '''            f"**Le module de flexion** (I/v, fiche 4.3). I/v = b h² / 6 = {b} × {h}² / 6 = {fr(w, 1)} mm³.",''')
R('''            "**À quoi ça sert.** Loin des angles vifs, la carte de Von Mises doit afficher une valeur proche. Un "
            "écart d'un facteur 2 ou 10 signale une erreur de modèle (appuis, force, unités) à chercher.",''',
  '''            "**À quoi ça sert.** Loin des angles vifs, la carte de Von Mises doit afficher une valeur proche (un peu "
            "plus près d'un congé : Kt). Si elle affiche nettement moins, l'écart doit être expliqué (appuis, force, "
            "unités) ; en attendant, on garde la valeur la plus défavorable.",''')
R(''""""encastrée et reçoit **{fr(F, 0)} N**""", """"encastrée et reçoit **{fr(F, 0)} N**""") if False else None

# --- quiz
R('''      "Le modèle est trop raide : flèche et contraintes sont sous-estimées"], 3,
     "Bloquer plus que la réalité rigidifie le modèle ; la pièce paraît plus solide qu'elle n'est.", "Piège"),''',
  '''      "Le modèle est trop raide : la flèche est sous-estimée et les contraintes sont faussées"], 3,
     "Bloquer plus que la réalité rigidifie le modèle : la pièce plie moins qu'en vrai, les contraintes autour des "
     "vis ne sont pas calculées et un pic artificiel apparaît souvent au bord de la zone bloquée.", "Piège"),''')
R('''     ["Les contraintes sont surestimées", "Le calcul ne peut pas aboutir", "Aucune, le logiciel corrige",''',
  '''     ["Le modèle est trop souple : la flèche est surestimée", "Le calcul ne peut pas aboutir",
      "Aucune, le logiciel corrige",''')
R('''     "S3.2 : le technicien interprète les résultats des simulations ; la taille et le type de maillage sont donnés "
     "(S3.2.6) ; pour les cas complexes, il dialogue avec un spécialiste.", "Base"),''',
  '''     "Le programme demande d'interpréter les résultats en autonomie ; la taille et le type de maillage sont donnés ; "
     "pour les cas simples on conduit la simulation, pour les cas complexes on dialogue avec un spécialiste.", "Base"),''')
R('''     ["Savoir programmer le solveur", "Savoir interpréter et critiquer le résultat, et dialoguer avec un spécialiste",''',
  '''     ["Savoir programmer le solveur", "Savoir interpréter et critiquer le résultat, et dialoguer avec un spécialiste",''')
R('''     "importante en fatigue.", "Intermédiaire"),''', '''     "importante en fatigue (fiches 4.1 et 3.5).", "Intermédiaire"),''')

open(P, 'w', encoding='utf-8').write(c)
print('ok')
