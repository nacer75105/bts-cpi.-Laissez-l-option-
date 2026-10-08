# Insère le brouillon 1.9 dans app.py (ancres textuelles uniques) + statut « hors référentiel 2016 » de la 1.5.
import json, os, re, textwrap

ICI = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(ICI, '..', '..', 'app.py')
app = open(APP, encoding='utf-8').read()
br = open(os.path.join(ICI, 'brouillon_1_9.py'), encoding='utf-8').read()


def seg(debut, fin):
    i = br.index(debut); j = br.index(fin, i)
    return br[i:j]


def avant(ancre, texte):
    global app
    assert app.count(ancre) == 1, ancre[:60]
    app = app.replace(ancre, texte + ancre)


def apres(ancre, texte):
    global app
    assert app.count(ancre) == 1, ancre[:60]
    app = app.replace(ancre, ancre + texte)


def remplacer(ancien, nouveau, n=1):
    global app
    assert app.count(ancien) == n, (ancien[:70], app.count(ancien))
    app = app.replace(ancien, nouveau)


# 1. figures statiques
avant("# ===========================================================================\n# 73. CARACTÉRISER UNE FONCTION",
      "# ===========================================================================\n"
      "# 72m. SYSML EN LECTURE — exigences, bdd, ibd, cas d'utilisation, séquence, états (fiche 1.9)\n"
      "#      Notation : spécification OMG SysML 1.6 (formal/19-11-01). Portail : exemple pédagogique.\n"
      "# ===========================================================================\n\n"
      + seg("def _sy_cadre(", "FIGURES_NOUVELLES = {").rstrip() + "\n\n\n")

# 2. registre FIGURES
entrees = re.findall(r'^    "(\w+)": \("([^"]+)", (\w+)\),$', seg("FIGURES_NOUVELLES = {", "}\n"), re.M)
assert len(entrees) == 5, entrees
apres('    "grille_amdec": ("La grille AMDEC", grille_amdec),\n',
      "".join(f'    "{k}": ("{t}", {f}),\n' for k, t, f in entrees))

# 3. la fiche, en fin de bloc 1 (après la 1.8)
lignes, dans = [], False
for ligne in seg("FICHE_1_9 = {", "\n# ====").rstrip().split("\n"):
    lignes.append(("        " + ligne if ligne.strip() else ligne) if not dans else ligne)
    if ligne.count('"""') % 2 == 1:
        dans = not dans
assert not dans
lignes[0] = "        {"
i18 = app.index("            \"id\": '1.8',")
fin1 = app.index('        },\n    ],\n}\n', i18)
assert fin1 < app.index('    "id": "bloc2",', i18)
app = app[:fin1 + len('        },\n')] + "\n".join(lignes) + ",\n" + app[fin1 + len('        },\n'):]

# 4. fiche 1.5 : statut hors référentiel 2016
i15 = app.index("            \"id\": '1.5',")
remplacer("            \"id\": '1.5',\n            \"titre\": 'SADT et actigramme : modéliser ce que fait le système',\n"
          "            \"duree\": '4 h',\n",
          "            \"id\": '1.5',\n            \"titre\": 'SADT et actigramme : modéliser ce que fait le système',\n"
          "            \"duree\": '4 h',\n"
          "            \"hors_referentiel\": \"Le SADT ne figure pas au référentiel 2016 du BTS CPI : pour décrire un "
          "système, le référentiel (S1.1) demande de lire des diagrammes SysML (fiche 1.9). **Pas à réviser pour "
          "l'examen** : fiche gardée comme complément.\",\n")

# 5. affichage : nouveau statut, distinct de « hors épreuve »
remplacer('''        if fiche.get("hors_epreuve"):
            st.warning("🎯 **Hors épreuve, pour aller plus loin.** " + fiche["hors_epreuve"])
''', '''        if fiche.get("hors_epreuve"):
            st.warning("🎯 **Hors épreuve, pour aller plus loin.** " + fiche["hors_epreuve"])
        if fiche.get("hors_referentiel"):
            st.warning("📌 **Hors référentiel 2016.** " + fiche["hors_referentiel"])
''')

# 6. méthode
mth = seg("MTH_1_9 = (", "\n# ====").rstrip()
avant('_mth("3.5", "Vérifier une pièce en fatigue", [', "_mth(" + mth[len("MTH_1_9 = ("):] + "\n\n")

# 7. ateliers : at178 et at179 après at177 (dernier élément)
i177 = app.index('        "id": "at177",')
fin_at = app.index("\n    },\n]\n", i177)
at = seg("ATELIERS_NOUVEAUX = [\n", "\n]\n")[len("ATELIERS_NOUVEAUX = [\n"):].rstrip().rstrip(",")
app = app[:fin_at] + "\n    },\n" + at + "," + app[fin_at + len("\n    },"):]


# 8. quiz
def chaine(txt, retrait, largeur=96):
    morceaux = textwrap.wrap(txt, largeur - retrait, break_long_words=False, drop_whitespace=False)
    return ("\n" + " " * retrait).join(json.dumps(m, ensure_ascii=False) for m in morceaux)


g = {}
exec(seg("QUIZ_SYSML = [", "\n]\n") + "\n]\n", g)
qs = []
for question, options, bonne, expl, niveau in g["QUIZ_SYSML"]:
    ops = ",\n       ".join(chaine(o, 7) for o in options)
    qs.append(f"    q({chaine(question, 6)},\n      [{ops}], {bonne},\n      {chaine(expl, 6)},\n"
              f"      {json.dumps(niveau, ensure_ascii=False)}),\n")
avant('QUIZ["Roulements et visserie : dimensionner"] = [',
      'QUIZ["SysML en lecture"] = [\n' + "\n".join(qs) + "]\n\n")

# 9. carte du programme : ligne « Analyse fonctionnelle »
remplacer('''         "Bête à cornes, pieuvre, FAST, SADT/actigramme, cahier des charges fonctionnel complet.",
         [("bloc1", ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.8"])]),''',
          '''         "Bête à cornes, pieuvre, FAST, cahier des charges fonctionnel complet, lecture des diagrammes SysML "
         "(exigences, blocs, cas d'utilisation, séquence, états) ; SADT/actigramme hors référentiel 2016.",
         [("bloc1", ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.8", "1.9"])]),''')

compile(app, APP, "exec")
open(APP, 'w', encoding='utf-8', newline='\n').write(app)
print("inséré")
