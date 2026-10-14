"""Monte-Carlo de la solution : jumeau stochastique exact de la projection (feuilles Proj_*).

Avec `chocs=False`, la simulation reproduit la projection déterministe du classeur (contrôle dans
verifier_jumeau). Avec `chocs=True`, elle tire au sort, chaque année et pour chaque trajectoire :

1. Crises macroéconomiques : probabilité annuelle `p_crise`, 1/12 par défaut (HYPOTHÈSE : deux crises
   majeures, 2008 et 2020, en environ 25 ans). Impacts identiques à la projection : classe C −80 %,
   B −15 %, A −5 %, dotation −25 % et dividendes −50 % l'année de crise ; reprise partielle l'année suivante.
2. Rendement de la dotation : loi normale (moyenne = rendement réel net, écart-type `sigma_dot`).
3. Bruit propre aux activités : lognormal de moyenne 1 (σ = 5 % pour A, 10 % pour B, 35 % pour C).
4. Sinistres ou découvertes non assurés : processus de Poisson (λ par an), montant lognormal de médiane
   égale à une année de provision de gros entretien.
5. Dépassement des campagnes de travaux : lognormal de médiane 1 (σ = 20 %).
6. Prix de l'énergie : choc lognormal annuel (σ = 20 %).
7. Dérive réelle des salaires : tirée une fois par trajectoire, N(g_salaires ; 0,4 point).
8. Défaillance de l'entreprise extérieure : probabilité annuelle `p_defaillance_ent`, 3,5 % par défaut,
   soit environ 1 sur 5 en 6 ans [R8-36]. Les dividendes cessent alors définitivement.
"""
from __future__ import annotations

import numpy as np

from noyau import EXTRA, REGISTRE


def _v(nom):
    if nom in EXTRA:
        return EXTRA[nom]
    return REGISTRE[nom].cen


def parametres_solution(scen: str, dotation0=None, div=None, div_annees=None, reserve0=None,
                        mh_actif=None, sub_actif=None, dette_active=None, sans_moteur=False,
                        mult_besoin=1.0):
    """Rassemble les montants de base (cas central) de la projection pour un scénario."""
    from projection import NOM_CONTRIB, SOLUTION_INVEST, SOLUTION_MOTEURS
    P = {
        "pers": _v(f"bud_dont_personnel_{scen}") * mult_besoin,
        "energie": (_v(f"bud_chauffage_{scen}") + _v(f"bud_hors_gel_{scen}") + _v(f"bud_electricite_{scen}")) * mult_besoin,
        "ge": (_v(f"bud_bati_ge_{scen}") + _v(f"bud_imprevus_travaux_{scen}")) * mult_besoin,
        "autres": (_v(f"bud_total_besoin_{scen}") - _v(f"bud_dont_personnel_{scen}") - _v(f"bud_bati_ge_{scen}")
                   - _v(f"bud_imprevus_travaux_{scen}") - _v(f"bud_chauffage_{scen}") - _v(f"bud_hors_gel_{scen}")
                   - _v(f"bud_electricite_{scen}")) * mult_besoin,
        "A": sum(_v(f"{scen}_ech_{m}") * _v(NOM_CONTRIB[m]) for m in SOLUTION_MOTEURS["A"]),
        "B": sum(_v(f"{scen}_ech_{m}") * _v(NOM_CONTRIB[m]) for m in SOLUTION_MOTEURS["B"]),
        "C": sum(_v(f"{scen}_ech_{m}") * _v(NOM_CONTRIB[m]) for m in SOLUTION_MOTEURS["C"]),
        "capex": sum(_v(f"{scen}_ech_{m}") * _v(nom) for m, nom in SOLUTION_INVEST.items()),
        "lissage": _v("lissage_depense"),
        "pilotage": _v("pilotage_actif"), "flex_seuil": _v("flex_seuil"), "flex_taux": _v("flex_taux"),
        "flex_report": _v("flex_report"), "urgence": _v("retrait_urgence"),
        "B0": _v(f"bud_total_besoin_{scen}") * mult_besoin,
        "g_sal": _v("g_salaires"), "g_trav": _v("g_travaux"), "g_en": _v("g_energie"), "g_rec": _v("g_recettes"),
        "inflation": _v("inflation"), "periode": int(_v("campagne_periode")),
        "rampe1": _v("rampe_an1"), "rampe2": _v("rampe_an2"), "fuite": _v("fuite_fiscale"),
        "dot_rdt": _v("dot_rendement"), "dot_taux": _v("dot_taux_net"), "taux_res": _v("taux_reserve"),
        "part_surplus": _v("part_surplus_dotation"),
        "dot0": 0.0 if sans_moteur else (dotation0 if dotation0 is not None else _v(f"{scen}_sol_dotation0")),
        "div": 0.0 if sans_moteur else (div if div is not None else _v(f"{scen}_sol_div")),
        "div_n": 0 if sans_moteur else (div_annees if div_annees is not None else _v(f"{scen}_sol_div_annees")),
        "res0": reserve0 if reserve0 is not None else _v(f"{scen}_sol_reserve0"),
        "sub": (sub_actif if sub_actif is not None else _v("sub_actif")) * _v("subvention_taux"),
        "mh": (mh_actif if mh_actif is not None else _v("mh_actif")) * _v("mh_tmi") * _v("mh_part_deductible") * _v("mh_taux_deduction"),
        "dette": 0.0,
    }
    if (dette_active if dette_active is not None else _v("dette_active")):
        t, n, va = _v("dette_taux"), _v("dette_duree"), _v(f"{scen}_prix_achat") * _v("dette_quotite")
        P["dette"] = va * t / (1 - (1 + t) ** (-n))
        P["dette_n"] = int(n)
    return P


def simuler(P: dict, annees: int = 30, n: int = 20000, graine: int = 2026, chocs: bool = True,
            p_crise: float = 1 / 12, sigma_dot: float = 0.10, lambda_sinistre: float = 0.10,
            sigma_sinistre: float = 0.8, sigma_campagne: float = 0.20, sigma_energie: float = 0.20,
            sigma_g_sal: float = 0.004, p_defaillance_ent: float = 0.035, ent_n: int = 1,
            sigma_ent: float = 0.15,
            sigma_classes=(0.05, 0.10, 0.35), detail: bool = False):
    rng = np.random.default_rng(graine)
    T = annees
    idx_sal = np.ones(n); idx_trav = 1.0; idx_en = 1.0; idx_rec = 1.0; idx_cpi = 1.0
    g_sal = P["g_sal"] + (rng.normal(0, sigma_g_sal, n) if chocs else 0.0)
    fonds = np.zeros(n); dot = np.full(n, P["dot0"], dtype=float); res = np.full(n, P["res0"], dtype=float)
    plafond = np.full(n, P["dot_taux"] * P["dot0"], dtype=float)
    ent_vivantes = np.full(n, ent_n, dtype=float)   # nombre de PME encore en vie dans la holding
    crise_prec = np.zeros(n, dtype=bool)
    premier_deficit = np.full(n, -1)
    traj = {k: np.zeros((n, T)) for k in ("reserve", "dotation", "solde", "total_charges", "act")}
    impact = {"A": (0.05, 0.02), "B": (0.15, 0.05), "C": (0.80, 0.30)}
    for t in range(1, T + 1):
        idx_sal = idx_sal * (1 + g_sal); idx_trav *= (1 + P["g_trav"]); idx_en *= (1 + P["g_en"])
        idx_rec *= (1 + P["g_rec"]); idx_cpi *= (1 + P["inflation"])
        crise = (rng.random(n) < p_crise) if chocs else np.zeros(n, dtype=bool)
        reprise = crise_prec & ~crise
        tension = (P["pilotage"] * (res < P["flex_seuil"] * P["B0"])).astype(float)
        pers = P["pers"] * idx_sal
        en = P["energie"] * idx_en * (rng.lognormal(-0.5 * sigma_energie ** 2, sigma_energie, n) if chocs else 1.0)
        ge = P["ge"] * idx_trav
        autres = P["autres"]
        total = pers + en + autres + ge
        # fonds de gros entretien et campagnes
        if t % P["periode"] == 0:
            mult = rng.lognormal(-0.5 * sigma_campagne ** 2, sigma_campagne, n) if chocs else 1.0
            campagne = (fonds + ge) * mult * (1 - tension * P["flex_report"])
        else:
            campagne = np.zeros(n)
        if chocs:
            nb = rng.poisson(lambda_sinistre, n)
            sinistre = np.zeros(n)
            for i in np.nonzero(nb)[0]:
                sinistre[i] = rng.lognormal(np.log(P["ge"]), sigma_sinistre, nb[i]).sum()
        else:
            sinistre = np.zeros(n)
        depassement = np.maximum(0, campagne + sinistre - fonds - ge)
        fonds = np.maximum(0, fonds + ge - campagne - sinistre)
        subvention = P["sub"] * campagne
        # activités
        rampe = P["rampe1"] if t == 1 else (P["rampe2"] if t == 2 else 1.0)
        act = np.zeros(n)
        for k, s in zip("ABC", sigma_classes):
            base = P[k] * rampe * idx_rec
            mult = np.where(crise, 1 - impact[k][0], np.where(reprise, 1 - impact[k][1], 1.0))
            bruit = rng.lognormal(-0.5 * s ** 2, s, n) if chocs else 1.0
            act = act + base * mult * bruit
        act_nette = np.where(act > 0, act * (1 - P["fuite"]), act)
        capex = P["capex"] if t == 1 else 0.0
        dette = (P["dette"] / idx_cpi) if (P["dette"] and t <= P.get("dette_n", 0)) else 0.0
        avantage_mh = P["mh"] * total
        besoin_net = (pers + en + autres + ge + depassement + dette - act_nette - subvention - avantage_mh
                      - tension * P["flex_taux"] * P["B0"])
        # moteur extérieur
        if chocs:
            ent_vivantes = ent_vivantes - rng.binomial(ent_vivantes.astype(int), p_defaillance_ent)
            bruit_ent = rng.lognormal(-0.5 * sigma_ent ** 2, sigma_ent, n)
        else:
            bruit_ent = 1.0
        div = (np.where(t <= P["div_n"], P["div"], 0.0) * (ent_vivantes / ent_n) * bruit_ent
               * np.where(crise, 0.5, 1.0))
        # rendement : la moyenne de long terme inclut déjà les crises ; on relève donc la moyenne des années
        # normales de 0,25 × p_crise pour ne pas compter deux fois le choc de crise.
        if chocs:
            # `dot_rdt` est un rendement réel ANNUALISÉ (moyenne géométrique de long terme, crises comprises).
            # Moyenne arithmétique ≈ géométrique + variance / 2 ; variance = bruit normal + sauts de crise.
            var = sigma_dot ** 2 + p_crise * (1 - p_crise) * 0.25 ** 2
            rdt = rng.normal(P["dot_rdt"] + var / 2 + 0.25 * p_crise, sigma_dot, n) + np.where(crise, -0.25, 0.0)
        else:
            rdt = np.full(n, P["dot_rdt"])
        if t > 1:
            plafond = P["lissage"] * plafond + (1 - P["lissage"]) * P["dot_taux"] * np.maximum(0, dot)
        plafond_eff = np.where(tension == 1, np.maximum(plafond, P["urgence"] * np.maximum(0, dot)), plafond)
        retrait = np.minimum(np.maximum(0, besoin_net - div), plafond_eff)
        solde = div + retrait - besoin_net
        apport = np.where((solde > 0) & (res > 0), solde * P["part_surplus"], 0.0)
        dot = np.maximum(0, dot) * (1 + rdt) - retrait + apport - capex
        res = res * (1 + P["taux_res"]) + solde - apport
        nouveaux = (res < 0) & (premier_deficit < 0)
        premier_deficit[nouveaux] = t
        crise_prec = crise
        for k, v in (("reserve", res), ("dotation", dot), ("solde", solde), ("total_charges", total), ("act", act_nette)):
            traj[k][:, t - 1] = v
    def q(a, x):
        return float(np.percentile(a, x))
    sortie = {
        "n": n, "annees": T,
        "p_echec_20": float(((premier_deficit > 0) & (premier_deficit <= 20)).mean()),
        "p_echec_30": float((premier_deficit > 0).mean()) if T >= 30 else None,
        "annee_mediane_echec": float(np.median(premier_deficit[premier_deficit > 0])) if (premier_deficit > 0).any() else None,
        "reserve_min_p05": q(traj["reserve"].min(axis=1), 5),
        "dotation_20_p05": q(traj["dotation"][:, min(19, T - 1)], 5),
        "dotation_20_p50": q(traj["dotation"][:, min(19, T - 1)], 50),
        "dotation_fin_p05": q(traj["dotation"][:, -1], 5),
        "dotation_fin_p50": q(traj["dotation"][:, -1], 50),
        "pire_solde_p05": q(traj["solde"].min(axis=1), 5),
    }
    if detail:
        sortie["traj"] = traj
    return sortie


def dotation_necessaire(P: dict, cible: float = 0.05, horizon: int = 30, n: int = 8000,
                        borne_haute: float = 2e8, **kw) -> float:
    """Plus petite dotation initiale qui ramène la probabilité d'échec sur `horizon` ans sous `cible`."""
    bas, haut = 0.0, borne_haute
    cle = "p_echec_30" if horizon >= 30 else "p_echec_20"
    for _ in range(22):
        milieu = (bas + haut) / 2
        Q = dict(P, dot0=milieu)
        if simuler(Q, annees=horizon, n=n, **kw)[cle] <= cible:
            haut = milieu
        else:
            bas = milieu
    return haut
