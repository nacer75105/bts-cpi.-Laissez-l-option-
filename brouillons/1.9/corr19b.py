# Corrections du brouillon 1.9 après relecture technique (bloquants B1-B7 et améliorations retenues).
import os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'brouillon_1_9.py')
c = open(P, encoding='utf-8').read()


def R(a, b, n=1):
    global c
    assert c.count(a) == n, (a[:70], c.count(a))
    c = c.replace(a, b)


# --- en-tête de cadre : seule l'abréviation (diagramKind) en gras (SysML 1.6 : « The diagramKind is bolded »)
R('''    p.append(_txt(x + 6, y + 16, entete, 11, TRAIT, "start", True))''',
  '''    ab, _, reste = entete.partition(" ")
    p.append(_txt(x + 6, y + 16, f"<tspan font-weight='700'>{ab}</tspan> {reste}", 11, TRAIT, "start"))''')
R('''#   * en-tête de cadre : « diagramKind [modelElementType] modelElementName [diagramName] », type en gras ;''',
  '''#   * en-tête de cadre : « diagramKind [modelElementType] modelElementName [diagramName] », diagramKind en gras ;''')
R('''#   * abréviations : req, uc, bdd, ibd, sd, stm (et act, par, pkg) ;''',
  '''#   * abréviations : req, uc, bdd, ibd, sd, stm (et act, par, pkg : neuf types en tout) ;
#   * dépendances (satisfy, include…) : trait pointillé à pointe OUVERTE (règle UML reprise par SysML, non relue
#     dans le texte extrait, cohérente avec « allocate … dashed line with an open arrow head ») ; la pointe noire
#     pleine est réservée au flux d'éléments ;''')

# --- B1 : le référentiel dit « décoder ou modifier » (S1.1.3)
R('''un diagramme fourni — jamais à en dessiner un.''',
  '''et à **exploiter** un diagramme fourni. Le référentiel n'exige pas d'en créer un de toutes pièces, mais un sujet
peut demander de le compléter ou de le modifier (S1.1.3 : « décoder ou modifier ces différents diagrammes
SysML »).''')
R('''Cette fiche apprend donc à **lire**
et à **exploiter**''', '''Cette fiche apprend donc à **lire**
et à **exploiter**''')
R('''"Au BTS CPI, ces diagrammes sont FOURNIS avec le sujet : on apprend à les lire, pas à les dessiner."''',
  '''"Au BTS CPI, ces diagrammes sont FOURNIS : on les lit, on les exploite, on peut avoir à les compléter."''')
R('''7. **Vouloir redessiner le diagramme** : au BTS, on le lit et on l'exploite, on ne le produit pas.''',
  '''7. **Vouloir tout redessiner** : on lit, on exploite, et l'on ne modifie que ce que l'énoncé demande.''')
R('''- SysML (norme OMG) : diagrammes **fournis** dans le sujet, à **lire**.''',
  '''- SysML (norme OMG) : diagrammes **fournis** dans le sujet, à **lire** et exploiter (parfois à compléter).''')

# --- B2 : renvoi critère/niveau -> fiches 1.3 et 1.6 ; A10 : analyse fonctionnelle = 1.1 à 1.6
R('''C'est la même idée que le cahier des charges
fonctionnel (fiche 1.4) :''', '''C'est la même idée que la caractérisation des
fonctions et le cahier des charges fonctionnel (fiches 1.3 et 1.6) :''')

# --- A11 : neuf diagrammes, six au programme ; A1/A3 : en-tête
R('''| états-transitions | **stm** | Dans quels états peut-il être, et qu'est-ce qui le fait changer d'état ? |
''', '''| états-transitions | **stm** | Dans quels états peut-il être, et qu'est-ce qui le fait changer d'état ? |

*SysML compte neuf types de diagrammes ; trois ne sont pas au programme du BTS CPI : activité (act),
paramétrique (par) et paquetage (pkg).*
''')
R('''haut à gauche, on lit d'abord **l'abréviation** (req, bdd…), puis entre crochets le type d'élément décrit, puis
son nom.''', '''haut à gauche, on lit d'abord **l'abréviation** (en gras : req, bdd…), puis, entre crochets et parfois omis, le
type d'élément décrit, puis son nom.''')
R('''[block] = un constituant, [package] = un « classeur » qui regroupe des éléments, [interaction] = un scénario
d'échanges. Ce mot entre crochets est secondaire et peut être absent (« stm Portail ») : l'abréviation et le nom
suffisent pour s'orienter.''', '''[block] = un constituant, [package] = un « classeur » qui regroupe des éléments, [interaction] = un scénario
d'échanges, [state machine] = une machine à états. Ce mot entre crochets est secondaire et peut être omis :
l'abréviation et le nom suffisent pour s'orienter.''')
R('''_cadre(p, 530, 40, 240, 290, "stm Portail")''', '''_cadre(p, 530, 40, 240, 290, "stm [state machine] Portail")''')

# --- A4 : valeurs id/text entre guillemets droits (les chevrons « » sont réservés aux stéréotypes)
R('''f"id = « {ident} »"''', '''f'id = "{ident}"\'''')
R('''f"text = « {texte} »"''', '''f'text = "{texte}"\'''')

# --- B4 : fin de course émise par un capteur de fin de course (bdd + sd)
R('''    enfants = ((40, 120, "Vantail", "1"), (190, 130, "Motoréducteur", "1"), (350, 140, "Carte de commande", "1"),
               (510, 110, "Galet de guidage", "4"), (640, 120, "Capteur d'obstacle", "1"))''',
  '''    enfants = ((34, 85, "Vantail", "1"), (127, 115, "Motoréducteur", "1"), (250, 125, "Carte de commande", "1"),
               (383, 105, "Galet de guidage", "4"), (496, 120, "Capteur d'obstacle", "1"),
               (624, 140, "Capteur fin de course", "2"))''')
R('''    p.append(_txt(40, 206, "les morceaux", 9, FIN, "start"))''', '''    p.append(_txt(36, 200, "les morceaux", 9, FIN, "start"))''')
# A6 : losange Motoréducteur -> Moteur lisible, multiplicité 1
R('''    _bloc(p, 195, 286, 120, 44, "Moteur")
    p.append(f"<line x1='255' y1='286' x2='255' y2='270' stroke='{TRAIT}' stroke-width='1.2'/>")
    p.append(f"<polygon points='255,270 249,278 255,286 261,278' fill='{TRAIT}'/>")
    p.append(_txt(266, 284, "1", 11, ALERTE, "start", True))''',
  '''    _bloc(p, 124, 296, 120, 40, "Moteur")
    p.append(f"<line x1='184' y1='286' x2='184' y2='296' stroke='{TRAIT}' stroke-width='1.2'/>")
    p.append(f"<polygon points='184,270 178,278 184,286 190,278' fill='{TRAIT}'/>")
    p.append(_txt(190, 294, "1", 11, ALERTE, "start", True))''')
R('''    p.append(_txt(40, 290, "Les nombres en rouge", 9, ALERTE, "start", True))
    p.append(_txt(40, 302, "(multiplicités) : combien", 9, ALERTE, "start", True))
    p.append(_txt(40, 314, "d'exemplaires.", 9, ALERTE, "start", True))''',
  '''    p.append(_txt(270, 300, "Les nombres en rouge (multiplicités) : combien d'exemplaires de chaque bloc.", 9, ALERTE, "start", True))''')
R('''1 carte, 4 galets, 1 capteur."''', '''1 carte, 4 galets, 1 + 2 capteurs."''')
R('''| 1 | Capteur d'obstacle |
''', '''| 1 | Capteur d'obstacle |
| 2 | Capteur de fin de course |
''')
# sd à quatre lignes de vie
R('''    for x, n in ((310, "utilisateur"), (395, "carte"), (480, "motoréd.")):
        p.append(f"<rect x='{x - 34}' y='74' width='68' height='22' fill='#ffffff' stroke='{OK}'/>")
        p.append(_txt(x, 89, n, 9, OK, "middle", True))
        p.append(f"<line x1='{x}' y1='96' x2='{x}' y2='316' stroke='{FIN}' stroke-dasharray='4 3'/>")
    p.append(_txt(352, 110, "message", 8, FIN, "middle"))
    for x1, x2, y, t in ((310, 395, 134, "appuyer()"), (395, 480, 174, "démarrer(sens)"),
                         (480, 395, 220, "fin de course"), (395, 480, 260, "arrêter()")):
        _fl_ouverte(p, x1, y, x2, y, TRAIT, False, 1.3)
        p.append(_txt((x1 + x2) / 2, y - 6, t, 9, TRAIT, "middle"))
    p.append(_txt(314, 290, "ligne de vie", 8, FIN, "start"))
    p.append(_txt(440, 312, "le temps descend ↓", 8, FIN, "middle"))''',
  '''    for x, n in ((304, "utilisateur"), (364, "carte"), (424, "motoréd."), (486, "capteur FdC")):
        p.append(f"<rect x='{x - 29}' y='74' width='58' height='22' fill='#ffffff' stroke='{OK}'/>")
        p.append(_txt(x, 89, n, 8, OK, "middle", True))
        p.append(f"<line x1='{x}' y1='96' x2='{x}' y2='304' stroke='{FIN}' stroke-dasharray='4 3'/>")
    p.append(_txt(334, 110, "message", 8, FIN, "middle"))
    for x1, x2, y, t in ((304, 364, 134, "appuyer()"), (364, 424, 174, "démarrer(sens)"),
                         (486, 364, 220, "finDeCourse()"), (364, 424, 260, "arrêter()")):
        _fl_ouverte(p, x1, y, x2, y, TRAIT, False, 1.3)
        p.append(_txt((x1 + x2) / 2, y - 6, t, 8, TRAIT, "middle"))
    p.append(_txt(300, 296, "ligne de vie", 8, FIN, "end"))
    p.append(_txt(395, 320, "le temps descend ↓", 8, FIN, "middle"))''')

# A13 : frontière du système en trait plein
R('''    p.append(f"<rect x='90' y='80' width='160' height='220' fill='none' stroke='{FIN}' stroke-dasharray='4 3'/>")''',
  '''    p.append(f"<rect x='90' y='80' width='160' height='220' fill='none' stroke='{FIN}' stroke-width='1.2'/>")''')

# --- texte du sd : capteur de fin de course, parenthèses (pas de convention inventée)
R('''Les
parenthèses marquent un ordre envoyé ; ce qui est dedans le précise (« démarrer(sens) » = démarrer, dans le sens
ouverture ou fermeture). On lit l'histoire d'un scénario : l'utilisateur appuie, la carte démarre le
motoréducteur, le motoréducteur signale la fin de course à la carte, la carte l'arrête.''',
  '''Entre
les parenthèses d'un message, ce qui le précise (« démarrer(sens) » = démarrer, dans le sens ouverture ou
fermeture). On lit l'histoire d'un scénario : l'utilisateur appuie, la carte démarre le motoréducteur, le
capteur de fin de course signale la fin de course à la carte, la carte arrête le motoréducteur.''')
# A16 : pseudo-état initial
R('''le **disque noir** marque l'état initial ;''',
  '''le **disque noir** est le **pseudo-état initial** : il désigne l'état par lequel le système démarre ;''')

# --- A8 : chaîne d'information définie
R('''Et la
**chaîne d'information** : l'ordre radio et la présence d'obstacle arrivent à la carte, qui commande le moteur.*''',
  '''Et la
**chaîne d'information** (le trajet des ordres et des mesures) : l'ordre radio et la présence d'obstacle arrivent
à la carte, qui commande le moteur.*''')
R('''- Les **connecteurs** sont les traits qui relient les ports :''', '''- Les **connecteurs** sont les traits qui relient les ports (ou directement les parties) :''')

# --- A9 : « ne cite pas » (un référentiel antérieur n'a pas été vérifié) ; énergie W -> flux
R('''Le référentiel 2016 du BTS CPI ne cite plus le SADT : pour
décrire un système, il demande de lire des diagrammes **SysML** (S1.1).''',
  '''Le référentiel 2016 du BTS CPI ne cite pas le SADT : pour
décrire un système, il demande de lire des diagrammes **SysML** (S1.1).''')

# --- exercice/corrigé : 4 messages, capteur
R('''**5.** L'événement « **appui** » (sur la télécommande), à condition''', '''**5.** L'événement « **appui** » (sur la télécommande), à condition''')

# --- at178 : piège étape 2 ; répartition des bonnes réponses
R('''             "pieges": [(1, "1 : c'est la multiplicité du vantail ou du moteur. Près du galet, on lit 4.")],''',
  '''             "pieges": [(1, "1 : c'est la multiplicité du vantail, du motoréducteur ou de la carte. Près du galet, "
                            "on lit 4.")],''')
R('''             "options": ["L'ordre des messages échangés", "De quoi le portail motorisé est composé",
                         "Les exigences du portail"], "bonne": 1,
             "indice": "bdd = diagramme de définition de blocs : la liste des constituants.",
             "diagnostics": {0: "L'ordre des messages, c'est le diagramme de séquence (sd).",
                             2: "Les exigences sont dans le diagramme d'exigences (req)."}},''',
  '''             "options": ["De quoi le portail motorisé est composé", "L'ordre des messages échangés",
                         "Les exigences du portail"], "bonne": 0,
             "indice": "bdd = diagramme de définition de blocs : la liste des constituants.",
             "diagnostics": {1: "L'ordre des messages, c'est le diagramme de séquence (sd).",
                             2: "Les exigences sont dans le diagramme d'exigences (req)."}},''')
R('''             "question": "Sur le diagramme d'exigences, une flèche pointillée «satisfy» relie le Motoréducteur à "
                         "l'exigence « Durée d'ouverture ». Comment la lire ?",
             "options": ["L'exigence satisfait le motoréducteur",
                         "Le motoréducteur satisfait l'exigence de durée d'ouverture",
                         "Le motoréducteur est vérifié par un essai"], "bonne": 1,
             "indice": "La flèche «satisfy» part de l'élément de conception.",
             "diagnostics": {0: "Sens inverse : c'est l'élément de conception (le bloc) qui satisfait l'exigence.",
                             2: "Un essai qui vérifie une exigence se lit avec «verify», pas «satisfy»."}},''',
  '''             "question": "Sur le diagramme d'exigences (figure du § 3 de la fiche), une flèche pointillée «satisfy» "
                         "va du Motoréducteur vers l'exigence « Durée d'ouverture ». Comment la lire ?",
             "options": ["L'exigence satisfait le motoréducteur",
                         "Le motoréducteur est vérifié par un essai",
                         "Le motoréducteur satisfait l'exigence de durée d'ouverture"], "bonne": 2,
             "indice": "La flèche «satisfy» part de l'élément de conception.",
             "diagnostics": {0: "Sens inverse : c'est l'élément de conception (le bloc) qui satisfait l'exigence.",
                             1: "Un essai qui vérifie une exigence se lit avec «verify», pas «satisfy»."}},''')

# --- at179 : étape 2 (réponse non donnée par la consigne), répartition des bonnes réponses
R('''             "options": ["Le motoréducteur commande la carte",
                         "L'énergie électrique circule de la carte vers le motoréducteur",
                         "La carte est composée du motoréducteur"], "bonne": 1,
             "indice": "Pointe noire sur un connecteur = flux d'éléments, vers le bloc qui reçoit.",
             "diagnostics": {0: "La pointe est dirigée vers le motoréducteur : c'est lui qui reçoit.",
                             2: "La composition se lit sur le bdd (losange noir), pas sur un connecteur d'ibd."}},''',
  '''             "options": ["L'énergie électrique circule de la carte vers le motoréducteur",
                         "Le motoréducteur commande la carte",
                         "La carte est composée du motoréducteur"], "bonne": 0,
             "indice": "Pointe noire sur un connecteur = flux d'éléments, vers le bloc qui reçoit.",
             "diagnostics": {1: "La pointe est dirigée vers le motoréducteur : c'est lui qui reçoit.",
                             2: "La composition se lit sur le bdd (losange noir), pas sur un connecteur d'ibd."}},''')
R('''            {"type": "numerique", "label": "Nombre de messages",
             "unite": "messages", "attendu": 4, "tol": 0.1,
             "consigne": "Le diagramme de séquence « Ouvrir » montre appuyer(), démarrer(sens), fin de course, "
                         "arrêter(). Combien de messages comporte ce scénario ?",
             "indice": "Compte les flèches horizontales.",
             "pieges": [(3, "3 : n'oublie pas le message du motoréducteur vers la carte (fin de course).")],
             "aide": "4 messages."},''',
  '''            {"type": "numerique", "label": "Messages reçus par le motoréducteur",
             "unite": "messages", "attendu": 2, "tol": 0.1,
             "consigne": "Sur le diagramme de séquence « Ouvrir » (figure affichée), combien de messages la carte "
                         "envoie-t-elle au motoréducteur ?",
             "indice": "Ne compte que les flèches qui partent de la ligne de vie « carte » et arrivent sur celle du "
                       "motoréducteur.",
             "pieges": [(4, "4 : c'est le nombre total de messages du scénario. Ne garde que ceux de la carte vers le "
                            "motoréducteur : démarrer(sens) et arrêter()."),
                        (3, "3 : finDeCourse() va du capteur vers la carte, pas de la carte vers le motoréducteur.")],
             "aide": "démarrer(sens) et arrêter() : 2 messages."},''')
R('''             "options": ["Il est écrit plus à gauche", "Il est placé plus haut : le temps s'écoule de haut en bas",
                         "Il est plus court"], "bonne": 1,''',
  '''             "options": ["Il est écrit plus à gauche", "Il est placé plus haut : le temps s'écoule de haut en bas",
                         "Il est plus court"], "bonne": 1,''')
R(''""""calcul": "**énergie électrique de la carte vers le motoréducteur** ; **4 messages** ;""",
  '''"calcul": "**énergie électrique de la carte vers le motoréducteur** ; **2 messages** de la carte vers le "
                     "motoréducteur ;''')

open(P, 'w', encoding='utf-8').write(c)
print('ok')
