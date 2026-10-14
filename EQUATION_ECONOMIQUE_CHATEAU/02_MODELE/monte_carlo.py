"""Simulation de Monte-Carlo de la trésorerie du domaine, en euros constants 2026.

Le modèle annuel simplifié est le « jumeau stochastique » de la projection déterministe :
avec tous les chocs à zéro, il doit reproduire la projection centrale. C'est vérifié dans `executer()`.

Mécanismes aléatoires (paramètres documentés dans la configuration) :
1. Crises macroéconomiques. Un processus de Bernoulli annuel déclenche une crise. Chaque classe de
   revenus perd une fraction de sa contribution l'année de la crise, puis une fraction moindre l'année
   suivante. La dotation subit une baisse de valeur.
2. Bruit propre à chaque activité : choc multiplicatif lognormal annuel, de moyenne 1.
3. Gros travaux imprévus, non couverts par l'assurance : processus de Poisson, montant lognormal.
4. Dérive réelle des coûts : salaires au-dessus de l'inflation, énergie volatile.
5. Rendement réel de la dotation : loi normale, plus le choc de crise.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np


@dataclass
class Flux:
    nom: str
    classe: str                    # "A", "B", "C" ou "D"
    contribution: float            # contribution nette en régime de croisière (€ 2026 / an)
    montee: list = field(default_factory=lambda: [1.0])   # fraction atteinte en années 1, 2, …
    sigma: float = 0.10            # volatilité annuelle idiosyncratique (lognormale)
    tendance: float = 0.0          # croissance réelle annuelle moyenne (négative = érosion)
    debut: int = 1                 # première année de flux


@dataclass
class ConfigMC:
    flux: list
    charges_fixes: float           # besoin annuel du domaine hors gros travaux imprévus (€ 2026)
    part_salaires: float = 0.45    # part des charges indexée sur les salaires
    derive_salaires: float = 0.005 # croissance réelle annuelle des salaires
    part_energie: float = 0.08
    sigma_energie: float = 0.20
    reserve_initiale: float = 0.0
    taux_reserve: float = 0.0      # rendement réel de la réserve de trésorerie
    dotation_initiale: float = 0.0
    rendement_dotation: float = 0.035   # rendement réel espéré
    sigma_dotation: float = 0.11
    retrait_dotation: float = 0.0  # retrait annuel (€ 2026), plafonné à la valeur disponible
    apports_dotation: dict = field(default_factory=dict)   # {année: montant}
    proba_crise: float = 1 / 12
    impact_crise: dict = field(default_factory=lambda: {"A": 0.05, "B": 0.15, "C": 0.70, "D": 0.0})
    impact_crise_an2: dict = field(default_factory=lambda: {"A": 0.02, "B": 0.05, "C": 0.30, "D": 0.0})
    choc_dotation_crise: float = -0.25
    lambda_travaux: float = 0.10   # nombre moyen de sinistres ou découvertes non assurés par an
    travaux_mediane: float = 150_000.0
    travaux_sigma: float = 0.9
    annees: int = 20
    seuil_alerte: float = 0.0      # la réserve ne doit pas descendre sous ce seuil


def simuler(cfg: ConfigMC, n: int = 20_000, graine: int = 2026, chocs: bool = True) -> dict:
    rng = np.random.default_rng(graine)
    T = cfg.annees
    reserve = np.full(n, cfg.reserve_initiale, dtype=float)
    dotation = np.full(n, cfg.dotation_initiale, dtype=float)
    min_reserve = reserve.copy()
    premier_defaut = np.full(n, -1)
    crise_prec = np.zeros(n, dtype=bool)
    traj_reserve = np.zeros((n, T))
    flux_libre = np.zeros((n, T))
    for t in range(1, T + 1):
        crise = (rng.random(n) < cfg.proba_crise) if chocs else np.zeros(n, dtype=bool)
        recettes = np.zeros(n)
        for f in cfg.flux:
            if t < f.debut:
                continue
            k = t - f.debut
            frac = f.montee[k] if k < len(f.montee) else f.montee[-1]
            base = f.contribution * frac * (1 + f.tendance) ** (t - 1)
            if chocs:
                bruit = rng.lognormal(-0.5 * f.sigma ** 2, f.sigma, n) if f.sigma > 0 else 1.0
                perte = np.where(crise, cfg.impact_crise.get(f.classe, 0.0),
                                 np.where(crise_prec, cfg.impact_crise_an2.get(f.classe, 0.0), 0.0))
                recettes += base * bruit * (1 - perte)
            else:
                recettes += base
        # charges : part salariale avec dérive réelle, part énergie volatile
        part_autres = 1 - cfg.part_salaires - cfg.part_energie
        charges = cfg.charges_fixes * (cfg.part_salaires * (1 + cfg.derive_salaires) ** (t - 1) + part_autres)
        if chocs:
            energie = cfg.charges_fixes * cfg.part_energie * rng.lognormal(
                -0.5 * cfg.sigma_energie ** 2, cfg.sigma_energie, n)
            nb_sinistres = rng.poisson(cfg.lambda_travaux, n)
            sinistres = np.zeros(n)
            for i in np.nonzero(nb_sinistres)[0]:
                sinistres[i] = rng.lognormal(np.log(cfg.travaux_mediane), cfg.travaux_sigma,
                                             nb_sinistres[i]).sum()
        else:
            energie = cfg.charges_fixes * cfg.part_energie
            sinistres = 0.0
        charges = charges + energie + sinistres
        # dotation : rendement, apports, retrait
        if cfg.dotation_initiale > 0 or cfg.apports_dotation:
            if chocs:
                rdt = rng.normal(cfg.rendement_dotation, cfg.sigma_dotation, n)
                rdt = np.where(crise, rdt + cfg.choc_dotation_crise, rdt)
            else:
                rdt = np.full(n, cfg.rendement_dotation)
            dotation = dotation * (1 + rdt) + cfg.apports_dotation.get(t, 0.0)
            retrait = np.minimum(cfg.retrait_dotation, np.maximum(dotation, 0))
            dotation = dotation - retrait
        else:
            retrait = 0.0
        fl = recettes + retrait - charges
        reserve = reserve * (1 + cfg.taux_reserve) + fl
        flux_libre[:, t - 1] = fl
        traj_reserve[:, t - 1] = reserve
        min_reserve = np.minimum(min_reserve, reserve)
        nouveaux = (reserve < cfg.seuil_alerte) & (premier_defaut < 0)
        premier_defaut[nouveaux] = t
        crise_prec = crise
    defaut = premier_defaut > 0
    q = lambda a, x: float(np.percentile(a, x))  # noqa: E731
    return {
        "n": n,
        "annees": T,
        "proba_reserve_negative": float(defaut.mean()),
        "annee_mediane_premier_defaut": (float(np.median(premier_defaut[defaut])) if defaut.any() else None),
        "reserve_finale_p05": q(reserve, 5),
        "reserve_finale_p50": q(reserve, 50),
        "reserve_finale_p95": q(reserve, 95),
        "reserve_min_p05": q(min_reserve, 5),
        "reserve_min_p50": q(min_reserve, 50),
        "dotation_finale_p05": q(dotation, 5),
        "dotation_finale_p50": q(dotation, 50),
        "flux_libre_moyen_p50": q(flux_libre.mean(axis=1), 50),
        "pire_annee_p05": q(flux_libre.min(axis=1), 5),
        "trajectoire_reserve_p05": [q(traj_reserve[:, t], 5) for t in range(T)],
        "trajectoire_reserve_p50": [q(traj_reserve[:, t], 50) for t in range(T)],
    }


def reserve_necessaire(cfg: ConfigMC, cible: float = 0.05, n: int = 10_000, borne_haute: float = 2e7) -> float:
    """Plus petite réserve initiale qui ramène la probabilité de réserve négative sous `cible` (dichotomie)."""
    bas, haut = 0.0, borne_haute
    for _ in range(25):
        milieu = (bas + haut) / 2
        cfg.reserve_initiale = milieu
        if simuler(cfg, n=n)["proba_reserve_negative"] <= cible:
            haut = milieu
        else:
            bas = milieu
    cfg.reserve_initiale = haut
    return haut
