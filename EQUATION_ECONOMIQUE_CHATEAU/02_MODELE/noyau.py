"""Noyau du modèle : registre des hypothèses et formules à double évaluation.

Principe de traçabilité
-----------------------
Chaque hypothèse est enregistrée une seule fois, avec :
- trois valeurs (cas favorable, central, défavorable pour l'équilibre du domaine) ;
- une unité ;
- un statut (SOURCÉ, ESTIMATION, HYPOTHÈSE) ;
- des identifiants de sources renvoyant aux fichiers 01_RECHERCHE/sources/*.csv.

Chaque ligne de calcul est écrite une seule fois, sous forme de **gabarit de formule**.
Ce gabarit sert deux fois :
1. il est traduit en formule Excel, avec des noms définis : le classeur reste vivant et modifiable ;
2. il est évalué en Python : on obtient une valeur de contrôle.

Le script `verifier.py` recalcule le classeur avec LibreOffice et compare les deux résultats.

Syntaxe des gabarits
--------------------
- `{S}` : préfixe du domaine type (S1, S2 ou S3).
- `{C}` : suffixe du cas. Il vaut "" pour le cas central, "_fav" pour le favorable, "_def" pour le défavorable.
- `[ligne]` : référence à une autre ligne de la même colonne du même tableau.
- Noms nus : hypothèses du registre.
- Fonctions autorisées : MAX, MIN, IF. Pas d'opérateur `^`, pas de comparaison `=` ou `<>`.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

CAS = {"fav": "_fav", "cen": "", "def": "_def"}
LIBELLES_CAS = {"fav": "Favorable", "cen": "Central", "def": "Défavorable"}

STATUTS = {"SOURCÉ", "ESTIMATION", "HYPOTHÈSE", "CALCUL"}


@dataclass
class Param:
    id: str
    libelle: str
    fav: float
    cen: float
    dfv: float
    unite: str
    statut: str
    sources: str
    note: str
    groupe: str

    def valeur(self, cas: str) -> float:
        return {"fav": self.fav, "cen": self.cen, "def": self.dfv}[cas]


REGISTRE: dict[str, Param] = {}
EXTRA: dict[str, float] = {}   # valeurs de cellules calculées et nommées (liens entre feuilles)
_NOM_VALIDE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def p(id, libelle, cen, fav=None, dfv=None, unite="", statut="HYPOTHÈSE",
      sources="", note="", groupe=""):
    """Enregistre une hypothèse. Si fav ou dfv manquent, ils prennent la valeur centrale."""
    if id in REGISTRE:
        raise ValueError(f"hypothèse en double : {id}")
    if not _NOM_VALIDE.match(id):
        raise ValueError(f"nom invalide pour Excel : {id}")
    if statut not in STATUTS:
        raise ValueError(f"statut inconnu {statut} pour {id}")
    if statut == "SOURCÉ" and not sources:
        raise ValueError(f"{id} est SOURCÉ mais sans source")
    REGISTRE[id] = Param(id, libelle,
                         cen if fav is None else fav,
                         cen,
                         cen if dfv is None else dfv,
                         unite, statut, sources, note, groupe)
    return REGISTRE[id]


# --------------------------------------------------------------------------
# Évaluation Python des gabarits
# --------------------------------------------------------------------------

def _IF(cond, a, b):
    return a if cond else b


def _PMT(taux, n, va):
    """Équivalent de la fonction Excel PMT (versement négatif si va > 0)."""
    if taux == 0:
        return -va / n
    return -va * taux / (1 - (1 + taux) ** (-n))


def _MIN(*a):
    return min(a[0]) if len(a) == 1 and isinstance(a[0], (list, tuple)) else min(a)


def _MAX(*a):
    return max(a[0]) if len(a) == 1 and isinstance(a[0], (list, tuple)) else max(a)


def _INDEX(plage, i, j=None):
    return plage[(j if j is not None else i) - 1]


FONCTIONS = {"MAX": _MAX, "MIN": _MIN, "IF": _IF, "PMT": _PMT, "MOD": lambda a, b: a % b,
             "AND": lambda *a: all(a), "OR": lambda *a: any(a), "INDEX": _INDEX,
             "SUM": lambda x: sum(x), "AVERAGE": lambda x: sum(x) / len(x)}

_EGAL = re.compile(r"(?<![<>=!])=(?!=)")


def vers_python(expr: str) -> str:
    """Traduit les comparaisons Excel (= et <>) en Python (== et !=)."""
    return _EGAL.sub("==", expr.replace("<>", "!="))
_REF_LIGNE = re.compile(r"\[([A-Za-z0-9_]+)\]")


def instancier(gabarit: str, scen: str | None, cas: str) -> str:
    """Remplace {S} et {C} dans un gabarit."""
    txt = gabarit.replace("{C}", CAS[cas])
    if scen is not None:
        txt = txt.replace("{S}", scen)
    elif "{S}" in txt:
        raise ValueError(f"gabarit dépendant du scénario sans scénario : {gabarit}")
    return txt


def espace_noms(cas_global: str = "cen") -> dict:
    """Espace de noms Python : chaque hypothèse dans ses trois variantes."""
    ns = {}
    for prm in REGISTRE.values():
        ns[prm.id] = prm.cen
        ns[prm.id + "_fav"] = prm.fav
        ns[prm.id + "_def"] = prm.dfv
    ns.update(EXTRA)
    ns.update(FONCTIONS)
    return ns


def evaluer(gabarit: str, scen: str | None, cas: str, lignes_calculees: dict) -> float:
    expr = instancier(gabarit, scen, cas)
    expr = _REF_LIGNE.sub(lambda m: f"__L_{m.group(1)}", expr)
    ns = espace_noms()
    for k, v in lignes_calculees.items():
        ns[f"__L_{k}"] = v
    if "^" in expr:
        raise ValueError("opérateur ^ interdit dans les gabarits")
    return float(eval(vers_python(expr), {"__builtins__": {}}, ns))  # noqa: S307 (gabarits internes)


def vers_excel(gabarit: str, scen: str | None, cas: str, adresse_ligne) -> str:
    """Traduit un gabarit en formule Excel. `adresse_ligne(id)` renvoie l'adresse de la cellule."""
    expr = instancier(gabarit, scen, cas)
    expr = _REF_LIGNE.sub(lambda m: adresse_ligne(m.group(1)), expr)
    return "=" + expr


def noms_utilises(gabarit: str) -> set[str]:
    """Hypothèses référencées par un gabarit (pour vérifier qu'elles existent toutes)."""
    sans_refs = _REF_LIGNE.sub("", gabarit)
    jetons = set(re.findall(r"[A-Za-z_{}][A-Za-z0-9_{}]*", sans_refs))
    return {j for j in jetons if j not in FONCTIONS and not j.startswith(("mot_", "bud_"))}
