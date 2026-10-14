"""Calculs Monte-Carlo de référence (dotations nécessaires, grille hybride, ruptures).

Usage : python3 calculer_mc.py  →  sorties/mc_*.json
"""
import json
import sys

sys.path.insert(0, ".")
import construire_modele as cm  # noqa: E402

cm.construire()
import monte_carlo as mc  # noqa: E402
from noyau import EXTRA  # noqa: E402

RESERVES = {"S1": 400_000, "S2": 1_500_000, "S3": 3_500_000}


def dotations():
    res = {}
    for scen, r0 in RESERVES.items():
        B = EXTRA[f"bud_total_besoin_{scen}"]
        for nom, kw, mult in (("pure", dict(div=0, div_annees=0), 1.0),
                              ("leviers", dict(div=0, div_annees=0, mh_actif=1), 0.85)):
            P = mc.parametres_solution(scen, reserve0=r0, mult_besoin=mult, **kw)
            k95 = mc.dotation_necessaire(P, cible=0.05, horizon=30, n=6000, borne_haute=4e8)
            k50 = mc.dotation_necessaire(P, cible=0.50, horizon=30, n=6000, borne_haute=4e8)
            s = mc.simuler(dict(P, dot0=k95), annees=30, n=20000)
            res[f"{scen}_{nom}"] = {"besoin_B": round(B, -3), "dotation_95": round(k95, -5),
                                    "dotation_50": round(k50, -5), "ratio_95_sur_B": round(k95 / B, 1),
                                    "ratio_50_sur_B": round(k50 / B, 1), "p_echec_20_a_k95": round(s["p_echec_20"], 4),
                                    "p_echec_30_a_k95": round(s["p_echec_30"], 4)}
            print(scen, nom, res[f"{scen}_{nom}"])
    json.dump(res, open("sorties/mc_dotation_necessaire.json", "w"), indent=1, ensure_ascii=False)


def grille():
    out = {}
    for scen, divs, k0s in (("S1", [0, 250_000, 400_000], [6e6, 8e6, 10e6, 12e6, 15e6, 20e6]),
                            ("S2", [0, 1_000_000, 1_500_000], [25e6, 35e6, 45e6, 55e6, 60e6, 70e6, 80e6])):
        for div in divs:
            ligne = {}
            for k0 in k0s:
                P = mc.parametres_solution(scen, dotation0=k0, div=div, div_annees=10 if div else 0,
                                           reserve0=RESERVES[scen])
                s = mc.simuler(P, annees=30, n=10000, ent_n=5)
                ligne[f"{k0 / 1e6:.0f} M€"] = {"echec_20": round(s["p_echec_20"], 3), "echec_30": round(s["p_echec_30"], 3)}
            out[f"{scen} — dividendes {div / 1e6:.2f} M€/an pendant 10 ans"] = ligne
            print(scen, div, ligne)
    json.dump(out, open("sorties/mc_grille_hybride.json", "w"), indent=1, ensure_ascii=False)


def ruptures():
    for scen in ("S2", "S1"):
        base = mc.parametres_solution(scen)
        N = 10000

        def pe(P, **kw):
            s = mc.simuler(P, annees=30, n=N, ent_n=5, **kw)
            return {"echec_20": round(s["p_echec_20"], 3), "echec_30": round(s["p_echec_30"], 3)}
        k = base["dot0"] / 1e6
        out = {"configuration": f"{scen} : dotation {k:.0f} M€, dividendes {base['div'] / 1e6:.2f} M€/an pendant "
                                f"{base['div_n']:.0f} ans, réserve {base['res0'] / 1e6:.2f} M€",
               "reference": pe(base)}
        out["dotation_initiale"] = {f"{f * k:.0f} M€": pe(dict(base, dot0=f * base["dot0"])) for f in (0.5, 0.67, 0.83, 1.0, 1.17, 1.33)}
        out["rendement_reel_net"] = {str(r): pe(dict(base, dot_rdt=r)) for r in (0.02, 0.025, 0.03, 0.035)}
        out["derive_salaires_reelle"] = {str(g): pe(dict(base, g_sal=g)) for g in (0.0, 0.005, 0.01, 0.015)}
        out["sans_regles_de_pilotage"] = pe(dict(base, pilotage=0))
        out["frequence_des_crises"] = {"1 tous les 20 ans": pe(base, p_crise=1 / 20), "1 tous les 12 ans": pe(base, p_crise=1 / 12),
                                       "1 tous les 8 ans": pe(base, p_crise=1 / 8)}
        out["sinistres_par_an"] = {str(l): pe(base, lambda_sinistre=l) for l in (0.05, 0.10, 0.20)}
        m = 1.2
        out["besoin_plus_20_pct"] = pe(dict(base, pers=base["pers"] * m, energie=base["energie"] * m, ge=base["ge"] * m,
                                            autres=base["autres"] * m, B0=base["B0"] * m))
        out["sans_dividendes_de_transition"] = pe(dict(base, div=0, div_n=0))
        out["une_seule_entreprise"] = pe(base) if base["div"] == 0 else {
            k2: v for k2, v in mc.simuler(base, annees=30, n=N, ent_n=1).items() if k2 in ("p_echec_20", "p_echec_30")}
        print(scen, json.dumps(out, ensure_ascii=False)[:600])
        json.dump(out, open(f"sorties/mc_ruptures_{scen}.json", "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    dotations()
    grille()
    ruptures()
