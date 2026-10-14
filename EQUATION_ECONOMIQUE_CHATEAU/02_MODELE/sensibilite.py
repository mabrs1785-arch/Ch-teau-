"""Sensibilité du besoin annuel (diagramme en tornade) : chaque hypothèse du budget, une à une.

Chaque hypothèse qui a des valeurs favorable et défavorable est placée à l'une puis à l'autre, toutes les
autres restant au cas central. On mesure l'écart du besoin annuel total par rapport au cas central.
Usage : python3 sensibilite.py  →  écrit sorties/sensibilite_budget.json
"""
from __future__ import annotations

import json
import os

import parametres  # noqa: F401  (remplit le registre)
import parametres_scenarios  # noqa: F401
from budget import LIGNES
from noyau import REGISTRE, evaluer, noms_utilises

ICI = os.path.dirname(os.path.abspath(__file__))


def besoin(scen: str) -> float:
    """Besoin annuel total du scénario au cas central, avec les valeurs centrales courantes du registre."""
    calc = {}
    for lid, _lib, gabarit, *_ in LIGNES:
        calc[lid] = evaluer(gabarit, scen, "cen", calc)
    return calc["total_besoin"]


def tornade(scen: str, nb: int = 12) -> dict:
    base = besoin(scen)
    utilises = set()
    for _lid, _lib, gabarit, *_ in LIGNES:
        utilises |= {n.replace("{S}", scen).replace("{C}", "") for n in noms_utilises(gabarit)}
    lignes = []
    for prm in REGISTRE.values():
        if prm.id not in utilises or (prm.fav == prm.cen and prm.dfv == prm.cen):
            continue
        cen = prm.cen
        try:
            prm.cen = prm.fav
            b_fav = besoin(scen)
            prm.cen = prm.dfv
            b_def = besoin(scen)
        finally:
            prm.cen = cen
        lignes.append([prm.id, prm.libelle, round(b_fav - base), round(b_def - base), round(abs(b_def - b_fav))])
    lignes.sort(key=lambda x: -x[4])
    return {"base": round(base), "tornado": lignes[:nb]}


if __name__ == "__main__":
    sortie = {scen: tornade(scen) for scen in ("S1", "S2", "S3")}
    with open(os.path.join(ICI, "sorties", "sensibilite_budget.json"), "w", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
    for scen, t in sortie.items():
        print(scen, t["base"])
        for ligne in t["tornado"][:8]:
            print("   ", ligne[0], ligne[2], ligne[3])
