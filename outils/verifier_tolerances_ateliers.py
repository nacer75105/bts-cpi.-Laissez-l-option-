# -*- coding: utf-8 -*-
"""Vérification des tolérances des ATELIERS et des GÉNÉRATEURS d'exercices de app.py.

À relancer après toute création ou modification d'atelier ou de générateur :

    python outils/verifier_tolerances_ateliers.py

Le script lit app.py sans lancer Streamlit (analyse du fichier source) et compte tous les
défauts ci-dessous dans son code de sortie : 0 si aucun défaut, sinon leur nombre.

1. ATELIERS (liste ATELIERS, page Ateliers)
-------------------------------------------
Le contrôleur accepte une réponse numérique quand |valeur − attendu| ≤ tol : `tol` est une
tolérance ABSOLUE, dans l'unité de l'étape. Jusqu'au 2026-09-25 il la lisait en relatif
(|attendu| × tol), ce qui faisait compter 42 pièges sur 194 étapes comme de bonnes réponses
(commit 34e7003). Pour chaque étape numérique :

  PIÈGE       un piège (valeur fausse prévisible) tombe dans la tolérance de la bonne réponse :
              l'élève qui fait CETTE erreur est déclaré juste. C'est le défaut le plus grave.
  IMPOSSIBLE  la bonne réponse ne peut pas être saisie : le champ n'affiche que le nombre de
              décimales du format de l'étape (clé "format", "%.4f" par défaut), et l'arrondi de
              la valeur attendue à ce nombre de décimales sort de la tolérance.
  LÂCHE       la tolérance dépasse 10 % de la valeur attendue, sans être déclarée voulue dans
              VOULU ci-dessous : presque n'importe quelle réponse serait acceptée.
  ZÉRO        tol = 0 sur une valeur non entière : seule une saisie parfaite, souvent
              impossible, serait acceptée.
  MASQUÉ      l'élève qui fait l'erreur d'un piège (tapée exactement, arrondie à la précision de
              l'étape, ou à 3 ou 4 chiffres quand cela reste dans la tolérance) reçoit le message
              d'un AUTRE piège. La page choisit le
              piège le plus proche dans sa fenêtre de ±2 % (diagnostic_le_plus_proche) ; avant
              le 2026-09-25 elle prenait le premier, et l'élève qui tapait 45 recevait le message
              du piège 45,025 (at2).
  ARRONDI     une étape déclare `"depend_de": {"etape": k, "formule": lambda v: ...}` (k = numéro
              de l'étape dont elle réutilise le résultat) : on prend les arrondis à 2, 3 et 4
              chiffres significatifs de la valeur attendue à l'étape k QUE CETTE ÉTAPE ACCEPTE,
              on leur applique la formule, et le résultat doit être accepté par l'étape courante.
              Sinon, l'élève qui a gardé un arrondi accepté plus haut est refusé plus bas (cas
              rencontré sur at143, fiche 18.11). À déclarer sur toute étape qui réutilise un
              résultat intermédiaire.

  SAUT        un texte de l'atelier (corrigé, énoncé, consigne, diagnostic…) contient un
              antislash suivi de n écrit en toutes lettres (deux antislashs puis n dans le
              source) au lieu d'un vrai saut de ligne : st.markdown l'affiche tel quel
              (« …50 MPa, antislash, n, antislash, n, Contrainte… »), et les étapes du corrigé se
              collent sur une ligne. Constaté à l'écran le 2026-09-25 sur 45 ateliers (73
              chaînes, 250 occurrences), corrigé le même jour. Les textes qui contiennent du LaTeX
              (entre dollars, où les commandes nu ou ne précédées d'un antislash sont légitimes)
              ne sont pas contrôlés.

Il affiche aussi, pour information, les tolérances entre 5 et 10 % (à vérifier une à une, mais
souvent normales : un entier demandé à ±0,1, une fourchette de cours).

Ce que cette partie ne voit pas, et qu'il faut contrôler à la main en relisant l'atelier : qu'une
réponse obtenue avec les arrondis de l'INDICE (par exemple 3 000/3,46 au lieu de 3 000/√12) reste
acceptée (cas at141, fiche 18.9) — sauf si l'étape le déclare par depend_de.

2. GÉNÉRATEURS (fonctions gen_*, page Entraînement)
---------------------------------------------------
Chaque générateur est rejoué TIRAGES fois (graines fixes), par tirer_exercice comme sur la page.
La page accepte la réponse quand
|valeur − rep| ≤ tol, et affiche la réponse avec decimales_affichage(tol) décimales. Jusqu'au
2026-09-25 elle l'affichait toujours avec 2 décimales : la réponse affichée était refusée dans
66 % des tirages de gen_proba_binomiale et 21 % de gen_proba_uniforme. Pour chaque tirage :

  AFFICHÉE    la réponse telle qu'elle est affichée, recopiée par l'élève (et lue par
              lire_nombre, comme sa saisie), est refusée par la tolérance.
  LECTURE     lire_nombre lit mal un nombre écrit normalement (contrôle de 100 000 entiers et
              de 20 000 décimaux formatés par fr) : jusqu'au 2026-09-25, « 5100 » était lu 5.
  DIAG        un diagnostic (valeur d'erreur prévisible) tombe dans la tolérance de la bonne
              réponse, même après les nouveaux tirages de tirer_exercice : fabriquer_exo le
              retirerait en silence, et l'erreur ne serait plus expliquée.
  MASQUÉ      l'élève qui fait l'erreur prévue par un diagnostic (et tape exactement sa valeur)
              ne reçoit pas SON message. Le contrôle rejoue la page : fusionner_diagnostics
              réunit les diagnostics confondus, diagnostic_le_plus_proche choisit le plus proche.
              Avant le 2026-09-25, le second de deux diagnostics égaux était jeté (cas
              gen_iso_jeu, 61 % des tirages).
  PLANTAGE    le générateur lève une exception.
  SAUT        un texte produit (titre, énoncé, corrigé, diagnostic, indice) contient un antislash
              suivi de n en toutes lettres, affiché tel quel (voir SAUT des ateliers).

Un générateur défectueux compte pour UN défaut (le nombre de tirages touchés est affiché).

3. BOUTONS IMBRIQUÉS (analyse statique de tout app.py)
------------------------------------------------------
  BOUTON      un st.button(...) (ou col.button, sidebar.button…) est créé à l'intérieur d'un
              « if » qui dépend d'un AUTRE bouton du même passage (« if st.button(…): » ou
              « _go = st.button(…) … if _go: »). Au rerun déclenché par le clic sur le bouton
              intérieur, le bouton extérieur vaut False : le bouton intérieur n'est pas recréé et
              son clic est perdu. Cas réel : « Voir la valeur et continuer » des ateliers et des
              exercices guidés, inopérant jusqu'au 2026-09-26 (l'élève restait bloqué). Remède :
              retenir l'état en session (clé propre à l'étape) et créer le bouton sous une
              condition sur cet état. Contrôle heuristique : il suit les noms affectés par un
              appel .button(...) dans la même fonction ; il peut signaler un faux positif, à
              examiner à la main.
"""
import ast
import io
import math
import os
import random
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.join(RACINE, "app.py")
TIRAGES = 2000

# Tolérances larges VOULUES : (id de l'atelier, numéro d'étape) -> raison.
VOULU = {
    ("at84", 3): "fourchette du cours (30 à 50 % du volume libre) : toute valeur de la fourchette "
                 "est juste",
}

CONTROLEUR_ABSOLU = "if abs(_val - _att) <= max(_tol, 1e-9):"
ANTISLASH_N = chr(92) + "n"


def sauts_litteraux(objet, chemin=""):
    """Chemins des textes (hors LaTeX) qui contiennent un antislash-n littéral, affiché tel quel."""
    if isinstance(objet, str):
        return [chemin] if ANTISLASH_N in objet and "$" not in objet else []
    if isinstance(objet, dict):
        return [c for k, v in objet.items() for c in sauts_litteraux(v, f"{chemin}.{k}")]
    if isinstance(objet, (list, tuple)):
        return [c for i, v in enumerate(objet) for c in sauts_litteraux(v, f"{chemin}[{i}]")]
    return []


def lire_source():
    return io.open(APP, encoding="utf-8").read()


# ---------------------------------------------------------------------------
# 1. Ateliers
# ---------------------------------------------------------------------------

def charger_ateliers(src):
    if CONTROLEUR_ABSOLU not in src:
        print("ATTENTION : le contrôleur des ateliers ne lit plus `tol` en absolu "
              f"(ligne attendue : {CONTROLEUR_ABSOLU!r}). Les résultats ci-dessous supposent une "
              "tolérance absolue.")
    for n in ast.parse(src).body:
        if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "ATELIERS":
            # certaines valeurs attendues sont des expressions (math.exp(-1), 3000 / math.sqrt(12))
            return eval(compile(ast.Expression(n.value), "ATELIERS", "eval"), {"math": math})
    raise SystemExit("liste ATELIERS introuvable dans app.py")


def verifier_ateliers(src):
    ateliers = charger_ateliers(src)
    g, definitions, _gens = espace_generateurs(src)
    definir(g, definitions, "diagnostic_le_plus_proche")
    plus_proche = g["diagnostic_le_plus_proche"]
    defauts, info, n_etapes = [], [], 0
    for a in ateliers:
        sauts = sauts_litteraux(a)
        if sauts:
            defauts.append(f"SAUT        {a['id']} : antislash-n affiché tel quel dans "
                           f"{', '.join(c.lstrip('.') for c in sauts[:4])}"
                           + (f" (+{len(sauts) - 4})" if len(sauts) > 4 else ""))
        for i, e in enumerate(a["etapes"], 1):
            if e.get("type", "numerique") != "numerique":
                continue
            n_etapes += 1
            att, tol = e["attendu"], e.get("tol", 0.02)
            cle = (a["id"], i)
            lieu = f"{a['id']} (fiche {a.get('fiche', '?')}), étape {i} « {e['label'][:45]} »"
            decimales = int(re.search(r"%\.(\d+)f", e.get("format", "%.4f")).group(1))
            for piege, _msg in e.get("pieges", []):
                if abs(piege - att) <= max(tol, 1e-9):
                    defauts.append(f"PIÈGE       {lieu} : le piège {piege:g} est accepté "
                                   f"(attendu {att:g} ± {tol:g})")
            if abs(round(att, decimales) - att) > max(tol, 1e-9):
                defauts.append(f"IMPOSSIBLE  {lieu} : {att:g} ne peut pas être saisi avec "
                               f"{decimales} décimales (± {tol:g})")
            if tol == 0 and not float(att).is_integer():
                defauts.append(f"ZÉRO        {lieu} : tol = 0 sur {att:g}")
            pieges = e.get("pieges", [])
            candidats = [(pv, max(abs(pv) * 0.02, 1e-9), pm) for pv, pm in pieges]  # comme la page
            dec_etape = max(0, math.ceil(-math.log10(tol) - 1e-9)) if tol > 0 else 6
            for pv, pm in pieges:
                # saisies plausibles de l'erreur : exacte, arrondie à la précision de l'étape, et
                # arrondie à 3 ou 4 chiffres quand cet arrondi reste dans la tolérance de l'étape
                saisies = [pv, round(pv, dec_etape)] + [
                    float(f"{pv:.{c}g}") for c in (3, 4) if abs(float(f"{pv:.{c}g}") - pv) <= tol]
                for tape in saisies:
                    if abs(tape - pv) > max(abs(pv) * 0.02, 1e-9):
                        continue  # saisie hors de la fenêtre de ce piège : pas une saisie de CETTE erreur
                    recu = plus_proche(tape, candidats)
                    if recu is not None and recu != pm:
                        defauts.append(f"MASQUÉ      {lieu} : l'élève qui fait l'erreur {pv:g} "
                                       f"(tape {tape:g}) reçoit le message d'un autre piège")
                        break
            dep = e.get("depend_de")
            if dep:
                prec = a["etapes"][dep["etape"] - 1]
                att_p, tol_p = prec["attendu"], prec.get("tol", 0.02)
                for chiffres in (2, 3, 4):
                    v = float(f"{att_p:.{chiffres}g}")
                    if abs(v - att_p) <= max(tol_p, 1e-9):
                        w = dep["formule"](v)
                        if abs(w - att) > max(tol, 1e-9):
                            defauts.append(f"ARRONDI     {lieu} : avec {v:g} (accepté à l'étape "
                                           f"{dep['etape']}), on obtient {w:.6g}, refusé ici "
                                           f"(attendu {att:.6g} ± {tol:g})")
            rel = tol / abs(att) if att else 0.0
            if rel > 0.10 and cle not in VOULU:
                defauts.append(f"LÂCHE       {lieu} : ± {tol:g} sur {att:g}, soit "
                               f"{100 * rel:.0f} %")
            elif rel > 0.05 or cle in VOULU:
                info.append(f"  {lieu} : ± {tol:g} sur {att:g} ({100 * rel:.0f} %)"
                            + (f" — voulu : {VOULU[cle]}" if cle in VOULU else ""))
    print(f"ATELIERS : {n_etapes} étapes numériques dans {len(ateliers)} ateliers.")
    if defauts:
        print(f"{len(defauts)} défaut(s) :")
        for d in defauts:
            print("  " + d)
    else:
        print("0 piège accepté, 0 piège masqué, 0 réponse impossible à saisir, 0 tolérance "
              "aberrante, 0 arrondi enchaîné refusé, 0 antislash-n affiché tel quel.")
    if info:
        print("Pour information, tolérances de 5 à 10 % (ou larges voulues), à vérifier une à une :")
        for x in info:
            print(x)
    return len(defauts)


# ---------------------------------------------------------------------------
# 2. Générateurs
# ---------------------------------------------------------------------------

def espace_generateurs(src):
    """Prépare un espace de noms où l'on définit À LA DEMANDE les fonctions et constantes de
    niveau module de app.py dont les générateurs ont besoin, sans exécuter la page Streamlit."""
    arbre = ast.parse(src)
    definitions = {}
    for n in arbre.body:
        if isinstance(n, ast.FunctionDef):
            definitions[n.name] = n
        elif isinstance(n, ast.Assign):
            for cible in n.targets:
                if isinstance(cible, ast.Name):
                    definitions.setdefault(cible.id, n)
    g = {"math": math, "random": random, "re": re, "__name__": "audit"}
    gens = [nom for nom, n in definitions.items()
            if isinstance(n, ast.FunctionDef) and nom.startswith("gen_")]
    return g, definitions, gens


def definir(g, definitions, nom, profondeur=0):
    """Exécute la définition de `nom` (fonction sans ses décorateurs, ou affectation), en
    définissant d'abord, récursivement, les noms dont elle a besoin."""
    if profondeur > 40:
        raise RuntimeError(f"dépendances trop profondes autour de {nom}")
    n = definitions[nom]
    if isinstance(n, ast.FunctionDef):
        n = ast.FunctionDef(name=n.name, args=n.args, body=n.body, decorator_list=[],
                            returns=n.returns, type_comment=None, type_params=[])
        ast.copy_location(n, definitions[nom])
    for _ in range(40):
        try:
            exec(compile(ast.fix_missing_locations(ast.Module([n], [])), APP, "exec"), g)
            return
        except NameError as err:
            manquant = re.search(r"name '(\w+)' is not defined", str(err))
            if not manquant or manquant.group(1) not in definitions:
                raise
            definir(g, definitions, manquant.group(1), profondeur + 1)
    raise RuntimeError(f"impossible de définir {nom}")


def appeler(g, definitions, fonction):
    """Appelle le générateur ; sur un nom manquant, le définit depuis app.py et réessaie."""
    if fonction not in g:
        definir(g, definitions, fonction)
    for _ in range(40):
        try:
            return g[fonction]()
        except NameError as err:
            manquant = re.search(r"name '(\w+)' is not defined", str(err))
            if not manquant or manquant.group(1) not in definitions:
                raise
            definir(g, definitions, manquant.group(1))
    raise RuntimeError("trop de noms manquants")


def verifier_generateurs(src):
    g, definitions, gens = espace_generateurs(src)
    for aide in ("fr", "lire_nombre", "decimales_affichage", "tirer_exercice",
                 "fusionner_diagnostics", "diagnostic_le_plus_proche"):
        if aide not in definitions:
            raise SystemExit(f"fonction {aide} introuvable dans app.py")
        definir(g, definitions, aide)
    fr, lire, dec, tirer = g["fr"], g["lire_nombre"], g["decimales_affichage"], g["tirer_exercice"]
    fusionner, plus_proche = g["fusionner_diagnostics"], g["diagnostic_le_plus_proche"]
    defauts = []
    for nom in gens:
        affichee = diag_dans_tol = masque = saut = 0
        exemple = ""
        try:
            appeler(g, definitions, nom)  # définit le générateur et ses dépendances
            for graine in range(TIRAGES):
                random.seed(graine)
                ex = tirer(g[nom])  # exactement le tirage de fabriquer_exo
                if sauts_litteraux({k: ex.get(k) for k in ("titre", "enonce", "corr", "diag",
                                                           "indice", "unite")}):
                    saut += 1
                tol = ex.get("tol", 0.001)
                texte = fr(ex["rep"], dec(tol))
                v = lire(texte)
                if v is None or abs(v - ex["rep"]) > tol:
                    affichee += 1
                    exemple = exemple or f"graine {graine} : affiché {texte}, réponse {ex['rep']:.6g}, tol {tol:g}"
                for d in ex.get("diag", []):
                    if d.get("v") is not None and abs(d["v"] - ex["rep"]) <= tol:
                        diag_dans_tol += 1
                        exemple = exemple or f"graine {graine} : diagnostic {d['v']:.6g} dans ± {tol:g}"
                        break
                # comme la page : fusion des diagnostics confondus, puis le plus proche de la saisie
                affiches = fusionner(ex.get("diag", []), ex["rep"], tol)
                candidats = [(d["v"], max(tol, abs(d["v"]) * 0.005), d["m"]) for d in affiches]
                for d in ex.get("diag", []):
                    if d.get("v") is None or abs(d["v"] - ex["rep"]) <= tol:
                        continue
                    recu = plus_proche(d["v"], candidats)
                    if recu is None or d["m"] not in recu:
                        masque += 1
                        exemple = exemple or (f"graine {graine} : l'erreur {d['v']:.6g} reçoit un "
                                              f"autre message")
                        break
        except Exception as err:  # noqa: BLE001 — on veut signaler tout plantage
            defauts.append(f"PLANTAGE    {nom} : {type(err).__name__} : {err}")
            continue
        if affichee:
            defauts.append(f"AFFICHÉE    {nom} : réponse affichée refusée dans {affichee}/{TIRAGES} "
                           f"tirages ({exemple})")
        if masque:
            defauts.append(f"MASQUÉ      {nom} : deux diagnostics confondus dans {masque}/{TIRAGES} "
                           f"tirages ({exemple})")
        if diag_dans_tol:
            defauts.append(f"DIAG        {nom} : diagnostic dans la tolérance dans "
                           f"{diag_dans_tol}/{TIRAGES} tirages ({exemple})")
        if saut:
            defauts.append(f"SAUT        {nom} : antislash-n affiché tel quel dans {saut}/{TIRAGES} "
                           f"tirages")
    mal_lus = [n for n in range(100000) if lire(str(n)) != n]
    alea = random.Random(1)
    for _ in range(20000):
        x = alea.uniform(-2000, 2000) * alea.choice([1, 0.01, 0.0001])
        d = alea.randint(2, 5)
        y = lire(fr(x, d))
        if y is None or abs(y - x) > 0.51 * 10 ** -d:
            mal_lus.append(fr(x, d))
    if mal_lus:
        defauts.append(f"LECTURE     lire_nombre lit mal {len(mal_lus)} nombres (ex. {mal_lus[:4]})")
    print(f"GÉNÉRATEURS : {len(gens)} générateurs, {TIRAGES} tirages chacun ; lecture de 120 000 "
          f"nombres par lire_nombre.")
    if defauts:
        print(f"{len(defauts)} défaut(s) :")
        for d in defauts:
            print("  " + d)
    else:
        print("0 réponse affichée refusée, 0 diagnostic dans la tolérance, 0 diagnostic masqué, "
              "0 plantage, 0 nombre mal lu, 0 antislash-n affiché tel quel.")
    return len(defauts)


# ---------------------------------------------------------------------------
# 3. Boutons imbriqués
# ---------------------------------------------------------------------------

def _est_bouton(noeud):
    """Appel de la forme X.button(...) (st.button, col.button, st.sidebar.button…)."""
    return isinstance(noeud, ast.Call) and isinstance(noeud.func, ast.Attribute) \
        and noeud.func.attr == "button"


def _boutons_dans(noeuds):
    """Appels .button(...) contenus dans ces instructions (sans descendre dans les fonctions)."""
    trouves = []
    pile = list(noeuds)
    while pile:
        n = pile.pop()
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
            continue
        if _est_bouton(n):
            trouves.append(n)
        pile.extend(ast.iter_child_nodes(n))
    return trouves


# Boutons imbriqués VOULUS (inoffensifs), repérés par leur libellé -> raison.
BOUTONS_VOULUS = {
    "Carte suivante": "page « À revoir » : le bouton ne fait que st.rerun(), ce que produit déjà "
                      "n'importe quel clic ; la carte a été mise à jour (srs_maj) au passage "
                      "précédent, la suivante s'affiche donc bien",
}


def verifier_boutons(src):
    arbre = ast.parse(src)
    defauts = []
    voulus = []
    portees = [arbre] + [n for n in ast.walk(arbre)
                         if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    for portee in portees:
        corps = portee.body
        # noms affectés par un appel .button(...) dans cette portée
        noms = set()
        pile = list(corps)
        while pile:
            n = pile.pop()
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if isinstance(n, ast.Assign) and _est_bouton(n.value):
                noms.update(t.id for t in n.targets if isinstance(t, ast.Name))
            pile.extend(ast.iter_child_nodes(n))
        pile = list(corps)
        while pile:
            n = pile.pop()
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if isinstance(n, ast.If):
                test_bouton = any(_est_bouton(x) for x in ast.walk(n.test)) or any(
                    isinstance(x, ast.Name) and x.id in noms for x in ast.walk(n.test))
                if test_bouton:
                    for b in _boutons_dans(n.body):
                        libelle = b.args[0].value if b.args and isinstance(b.args[0], ast.Constant) \
                            else ""
                        if libelle in BOUTONS_VOULUS:
                            voulus.append(f"  ligne {b.lineno}, « {libelle} » — voulu : "
                                          f"{BOUTONS_VOULUS[libelle]}")
                            continue
                        defauts.append(f"BOUTON      ligne {b.lineno} : bouton créé sous le « if » "
                                       f"de la ligne {n.lineno}, qui dépend d'un autre bouton : "
                                       "son clic sera perdu")
            pile.extend(ast.iter_child_nodes(n))
    defauts = sorted(set(defauts), key=lambda d: int(re.search(r"ligne (\d+)", d).group(1)))
    print("BOUTONS : analyse de tous les st.button de app.py.")
    if defauts:
        print(f"{len(defauts)} défaut(s) :")
        for d in defauts:
            print("  " + d)
    else:
        print("0 bouton créé sous un autre bouton.")
    for v in sorted(set(voulus)):
        print("Pour information, bouton imbriqué déclaré inoffensif :")
        print(v)
    return len(defauts)


def main():
    src = lire_source()
    n = verifier_ateliers(src)
    print()
    n += verifier_generateurs(src)
    print()
    n += verifier_boutons(src)
    print(f"\nTotal : {n} défaut(s).")
    return n


if __name__ == "__main__":
    sys.exit(main())
