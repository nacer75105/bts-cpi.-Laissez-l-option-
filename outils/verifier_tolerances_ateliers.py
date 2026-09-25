# -*- coding: utf-8 -*-
"""Vérification des tolérances des ATELIERS (liste ATELIERS de app.py).

À relancer après toute création ou modification d'atelier :

    python outils/verifier_tolerances_ateliers.py

Le contrôleur des ateliers (page Ateliers, app.py) accepte une réponse numérique quand
|valeur − attendu| ≤ tol : `tol` est une tolérance ABSOLUE, dans l'unité de l'étape. Jusqu'au
2026-09-25 il la lisait en relatif (|attendu| × tol), ce qui faisait compter 42 pièges sur 194
étapes comme de bonnes réponses (commit 34e7003). Ce script garantit que cela ne revient pas.

Il lit ATELIERS sans lancer Streamlit (analyse du fichier source), puis cherche, pour chaque
étape numérique, quatre défauts, tous comptés dans le code de sortie :

  PIÈGE       un piège (valeur fausse prévisible) tombe dans la tolérance de la bonne réponse :
              l'élève qui fait CETTE erreur est déclaré juste. C'est le défaut le plus grave.
  IMPOSSIBLE  la bonne réponse ne peut pas être saisie : le champ n'affiche que le nombre de
              décimales du format de l'étape (clé "format", "%.4f" par défaut), et l'arrondi de
              la valeur attendue à ce nombre de décimales sort de la tolérance.
  LÂCHE       la tolérance dépasse 10 % de la valeur attendue, sans être déclarée voulue dans
              VOULU ci-dessous : presque n'importe quelle réponse serait acceptée.
  ZÉRO        tol = 0 sur une valeur non entière : seule une saisie parfaite, souvent
              impossible, serait acceptée.

Il affiche aussi, pour information, les tolérances entre 5 et 10 % (à vérifier une à une, mais
souvent normales : un entier demandé à ±0,1, une fourchette de cours).

Ce que ce script ne voit pas, et qu'il faut contrôler à la main en relisant l'atelier : qu'une
réponse obtenue avec les arrondis intermédiaires de l'indice (par exemple 3 000/3,46 au lieu de
3 000/√12) reste acceptée. Cas rencontré sur at141 (fiche 18.9).

Code de sortie : 0 si aucun défaut, sinon le nombre de défauts.
"""
import ast
import io
import math
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.join(RACINE, "app.py")

# Tolérances larges VOULUES : (id de l'atelier, numéro d'étape) -> raison.
VOULU = {
    ("at84", 3): "fourchette du cours (30 à 50 % du volume libre) : toute valeur de la fourchette "
                 "est juste",
}

CONTROLEUR_ABSOLU = "if abs(_val - _att) <= max(_tol, 1e-9):"


def charger_ateliers():
    src = io.open(APP, encoding="utf-8").read()
    if CONTROLEUR_ABSOLU not in src:
        print("ATTENTION : le contrôleur des ateliers ne lit plus `tol` en absolu "
              f"(ligne attendue : {CONTROLEUR_ABSOLU!r}). Les résultats ci-dessous supposent une "
              "tolérance absolue.")
    for n in ast.parse(src).body:
        if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "ATELIERS":
            # certaines valeurs attendues sont des expressions (math.exp(-1), 3000 / math.sqrt(12))
            return eval(compile(ast.Expression(n.value), "ATELIERS", "eval"), {"math": math})
    raise SystemExit("liste ATELIERS introuvable dans app.py")


def main():
    ateliers = charger_ateliers()
    defauts, info, n_etapes = [], [], 0
    for a in ateliers:
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
            rel = tol / abs(att) if att else 0.0
            if rel > 0.10 and cle not in VOULU:
                defauts.append(f"LÂCHE       {lieu} : ± {tol:g} sur {att:g}, soit "
                               f"{100 * rel:.0f} %")
            elif rel > 0.05 or cle in VOULU:
                info.append(f"  {lieu} : ± {tol:g} sur {att:g} ({100 * rel:.0f} %)"
                            + (f" — voulu : {VOULU[cle]}" if cle in VOULU else ""))
    print(f"{n_etapes} étapes numériques dans {len(ateliers)} ateliers.")
    if defauts:
        print(f"\n{len(defauts)} défaut(s) :")
        for d in defauts:
            print("  " + d)
    else:
        print("0 piège accepté, 0 réponse impossible à saisir, 0 tolérance aberrante.")
    if info:
        print("\nPour information, tolérances de 5 à 10 % (ou larges voulues), à vérifier une à une :")
        for x in info:
            print(x)
    return len(defauts)


if __name__ == "__main__":
    sys.exit(main())
