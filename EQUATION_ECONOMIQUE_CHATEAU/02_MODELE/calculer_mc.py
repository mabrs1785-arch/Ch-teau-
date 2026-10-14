"""Calculs Monte-Carlo de référence (dotations nécessaires, grille hybride, ruptures).

Usage : python3 calculer_mc.py  →  sorties/mc_*.json
"""
import json
import sys

sys.path.insert(0, ".")
import construire_modele as cm  # noqa: E402

# reconstruit le registre ET recalcule le classeur (sinon il resterait sans valeurs en cache)
cm.recalculer_et_verifier(cm.construire())
import monte_carlo as mc  # noqa: E402
from noyau import EXTRA  # noqa: E402

# réserves de trésorerie des solutions, lues dans le registre (feuille Hypotheses)
RESERVES = {s: mc._v(f"{s}_sol_reserve0") for s in ("S1", "S2", "S3")}
for s, r in RESERVES.items():   # garde-fou : une réserve sous un an de besoin déclenche la coupe dès l'année 1
    assert r >= EXTRA[f"bud_total_besoin_{s}"], f"réserve {s} inférieure à un an de besoin"


def dotations():
    res = {}
    for scen, r0 in RESERVES.items():
        B = EXTRA[f"bud_total_besoin_{scen}"]
        # « leviers » = leviers vérifiés par V2C (−7,5 % du besoin), sans l'avantage fiscal MH (V2R M4)
        for nom, kw, mult in (("pure", dict(div=0, div_annees=0), 1.0),
                              ("leviers", dict(div=0, div_annees=0, mh_actif=0), 0.925)):
            P = mc.parametres_solution(scen, reserve0=r0 * mult, mult_besoin=mult, **kw)
            k95 = mc.dotation_necessaire(P, cible=0.05, horizon=30, n=6000, borne_haute=1.5e9)
            k50 = mc.dotation_necessaire(P, cible=0.50, horizon=30, n=6000, borne_haute=1.5e9)
            assert k95 < 1.4e9, "borne haute atteinte : relever borne_haute"
            s = mc.simuler(dict(P, dot0=k95), annees=30, n=20000)
            res[f"{scen}_{nom}"] = {"besoin_B": round(B, -3), "dotation_95": round(k95, -5),
                                    "dotation_50": round(k50, -5), "ratio_95_sur_B": round(k95 / B, 1),
                                    "ratio_50_sur_B": round(k50 / B, 1), "p_echec_20_a_k95": round(s["p_echec_20"], 4),
                                    "p_echec_30_a_k95": round(s["p_echec_30"], 4)}
            print(scen, nom, res[f"{scen}_{nom}"])
    json.dump(res, open("sorties/mc_dotation_necessaire.json", "w"), indent=1, ensure_ascii=False)


def grille():
    out = {}
    for scen, divs, k0s in (("S1", [0, 250_000, 400_000], [10e6, 15e6, 20e6, 25e6, 30e6, 35e6, 40e6]),
                            ("S2", [0, 1_000_000, 1_500_000], [40e6, 60e6, 80e6, 100e6, 120e6, 140e6, 160e6])):
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
    for scen in ("S2", "S1", "S3"):
        base = mc.parametres_solution(scen)
        N = 10000

        def pe(P, **kw):
            s = mc.simuler(P, annees=30, n=N, ent_n=5, **kw)
            return {"echec_20": round(s["p_echec_20"], 3), "echec_30": round(s["p_echec_30"], 3),
                    "annees_tension_20": round(s["part_annees_tension_20"], 3)}
        k = base["dot0"] / 1e6
        out = {"configuration": f"{scen} : dotation {k:.0f} M€, dividendes {base['div'] / 1e6:.2f} M€/an pendant "
                                f"{base['div_n']:.0f} ans, réserve {base['res0'] / 1e6:.2f} M€",
               "reference": pe(base)}
        out["dotation_initiale"] = {f"{f * k:.0f} M€": pe(dict(base, dot0=f * base["dot0"])) for f in (0.5, 0.67, 0.83, 1.0, 1.17, 1.33)}
        out["rendement_reel_net"] = {str(r): pe(dict(base, dot_rdt=r)) for r in (0.015, 0.02, 0.025, 0.03)}
        out["derive_salaires_reelle"] = {str(g): pe(dict(base, g_sal=g)) for g in (0.0, 0.005, 0.01, 0.015)}
        out["sans_regles_de_pilotage"] = pe(dict(base, pilotage=0))
        out["frequence_des_crises"] = {"1 tous les 20 ans": pe(base, p_crise=1 / 20), "1 tous les 12 ans": pe(base, p_crise=1 / 12),
                                       "1 tous les 8 ans": pe(base, p_crise=1 / 8)}
        out["sinistres_par_an"] = {str(l): pe(base, lambda_sinistre=l) for l in (0.05, 0.10, 0.20)}
        m = 1.2
        # la réserve suit le besoin (un peu plus d'un an de besoin), sinon la coupe de pilotage jouerait en permanence
        out["besoin_plus_20_pct"] = pe(dict(base, pers=base["pers"] * m, energie=base["energie"] * m, ge=base["ge"] * m,
                                            autres=base["autres"] * m, assur=base["assur"] * m, B0=base["B0"] * m,
                                            res0=base["res0"] * m))
        out["sans_dividendes_de_transition"] = pe(dict(base, div=0, div_n=0))
        out["decennie_perdue_0pct_10ans"] = pe(base, rdt_debut=0.0, n_debut=10)
        out["deces_annee_15_droits_44pct"] = pe(base, choc_dot_an=15, choc_dot_taux=0.443)
        Bc = EXTRA[f"bud_total_besoin_{scen}"]
        out["besoin_fourchette_L1"] = {
            nom: dict(pe(mc.parametres_solution(scen, mult_besoin=EXTRA[f"bud_total_besoin_{scen}{suf}"] / Bc,
                                                reserve0=base["res0"] * EXTRA[f"bud_total_besoin_{scen}{suf}"] / Bc)),
                      besoin=round(EXTRA[f"bud_total_besoin_{scen}{suf}"], -3))
            for nom, suf in (("favorable", "_fav"), ("defavorable", "_def"))}
        md = EXTRA[f"bud_total_besoin_{scen}_def"] / Bc
        Pd = mc.parametres_solution(scen, mult_besoin=md, reserve0=base["res0"] * md, div=0, div_annees=0)
        out["dotation_95_si_besoin_defavorable_sans_dividendes"] = round(
            mc.dotation_necessaire(Pd, cible=0.05, horizon=30, n=6000, borne_haute=8e8), -5)
        out["une_seule_entreprise"] = pe(base) if base["div"] == 0 else {
            k2: v for k2, v in mc.simuler(base, annees=30, n=N, ent_n=1).items() if k2 in ("p_echec_20", "p_echec_30")}
        print(scen, json.dumps(out, ensure_ascii=False)[:600])
        json.dump(out, open(f"sorties/mc_ruptures_{scen}.json", "w"), indent=1, ensure_ascii=False)


def holding():
    """Holding de PME qui ne fait que distribuer ses dividendes pendant 30 ans, avec une petite dotation."""
    out = {}
    for scen, cas in (("S1", [(300_000, 3, 3_000_000), (400_000, 3, 2_000_000), (250_000, 1, 3_000_000)]),
                      ("S2", [(1_000_000, 5, 10_000_000), (1_200_000, 5, 8_000_000), (1_000_000, 1, 10_000_000),
                              (1_400_000, 6, 5_000_000)])):
        for div, n_pme, k0 in cas:
            P = mc.parametres_solution(scen, dotation0=k0, div=div, div_annees=30, reserve0=RESERVES[scen])
            s = mc.simuler(P, annees=30, n=20000, ent_n=n_pme)
            cle = f"{scen}_div{div // 1000}k_{n_pme}pme_dot{k0 // 1_000_000}M"
            out[cle] = {k: (round(v, 4) if abs(v) < 10 else round(v, -5)) for k, v in s.items()
                        if k in ("p_echec_20", "p_echec_30", "dotation_20_p05", "dotation_20_p50",
                                 "dotation_fin_p05", "dotation_fin_p50", "reserve_min_p05")}
            print(cle, out[cle])
    json.dump(out, open("sorties/mc_holding_hybride.json", "w"), indent=1, ensure_ascii=False)


def distribution():
    """Distribution des trajectoires des trois solutions (30 ans, 20 000 tirages) : dotation, tensions, échecs."""
    import numpy as np
    out = {}
    for scen in ("S1", "S2", "S3"):
        P = mc.parametres_solution(scen)
        s = mc.simuler(P, annees=30, n=20000, ent_n=5, detail=True)
        dot = s["traj"]["dotation"]
        tension = s["traj"]["tension"][:, :20] > 0   # années où les règles de pilotage s'appliquent
        d20, d30 = dot[:, 19], dot[:, 29]
        out[scen] = {
            "p_echec_20": round(s["p_echec_20"], 3), "p_echec_30": round(s["p_echec_30"], 3),
            "annee_mediane_premier_echec": s["annee_mediane_echec"],
            "part_traj_au_moins_1_annee_tension_20ans": round(float(tension.any(axis=1).mean()), 3),
            "nb_moyen_annees_tension_20ans": round(float(tension.sum(axis=1).mean()), 2),
            "dotation_an20_M": {f"p{x:02d}": round(float(np.percentile(d20, x)) / 1e6, 1) for x in (5, 25, 50, 75, 95)},
            "dotation_an30_M": {f"p{x:02d}": round(float(np.percentile(d30, x)) / 1e6, 1) for x in (5, 25, 50, 75, 95)},
            "dotation0_M": P["dot0"] / 1e6,
            "part_dotation_an20_sous_dotation0": round(float((d20 < P["dot0"]).mean()), 3),
            "part_dotation_an20_sous_moitie": round(float((d20 < 0.5 * P["dot0"]).mean()), 3),
        }
        print(scen, out[scen])
    json.dump(out, open("sorties/mc_distribution_solutions.json", "w"), indent=1, ensure_ascii=False)


def comparaison_modeles():
    """Dotation nécessaire pour chaque modèle candidat de L3 (30 ans, 50 % et 95 % de chances de tenir).

    - A : dotation seule, avec le socle d'activités calmes de la solution ;
    - B : hybride, dividendes de transition de la holding (5 PME) puis dotation ;
    - C : locataire d'ancrage (bail à un exploitant de séminaires) + socle foncier, puis dotation. Le loyer est
      traité en classe B (choc de crise de −15 % au lieu de −5 %), par prudence (loyers suspendus en 2020-2021) ;
      pour S3, le moteur S2 (50 chambres) est multiplié par 1,6 (80 chambres, valeur centrale de V2A) ;
    - D : réduction du besoin par les leviers vérifiés par V2C (−7,5 %), sans avantage fiscal MH.
    """
    out = {}
    v = mc._v

    def k(P, cible, horizon=30, **kw):
        return round(mc.dotation_necessaire(P, cible=cible, horizon=horizon, n=6000, borne_haute=8e8, **kw), -5)

    for scen in ("S2", "S3"):
        B = EXTRA[f"bud_total_besoin_{scen}"]
        r0 = RESERVES[scen]
        # A — dotation seule
        PA = mc.parametres_solution(scen, div=0, div_annees=0, reserve0=r0)
        out[f"A_dotation_seule_{scen}"] = {"k50": k(PA, 0.50), "k95": k(PA, 0.05)}
        # B — hybride : dividendes de 1 M€ (S2) pendant 10 ans, 5 PME
        div = 1_000_000 if scen == "S2" else 3_000_000
        PB = mc.parametres_solution(scen, div=div, div_annees=10, reserve0=r0)
        out[f"B_hybride_{scen}"] = {"dividendes": div, "k95_30ans": k(PB, 0.05, ent_n=5),
                                    "k95_20ans": k(PB, 0.05, horizon=20, ent_n=5)}
        # C — locataire d'ancrage
        f_anc = 1.0 if scen == "S2" else 1.6
        ech = (lambda m: v(f"{scen}_ech_{m}"))
        PC = dict(PA)
        PC["A"] = ech("pv") * v("mot_pv_cn") + ech("bois") * v("mot_bois_cn")
        PC["B"] = f_anc * v("mot_anc_cn") + ech("eq_ret") * v("mot_eq_ret_cn")
        PC["C"] = 0.0
        PC["capex"] = 0.0
        out[f"C_ancrage_{scen}"] = {"contribution_brute_activites": round(PC["A"] + PC["B"], -3),
                                    "k50": k(PC, 0.50), "k95": k(PC, 0.05)}
        # D — leviers vérifiés (−7,5 % du besoin), sans avantage MH
        PD = mc.parametres_solution(scen, div=0, div_annees=0, reserve0=r0, mult_besoin=0.925, mh_actif=0)
        out[f"D_leviers_verifies_{scen}"] = {"k50": k(PD, 0.50), "k95": k(PD, 0.05)}
        for cle in [c for c in out if c.endswith(scen)]:
            print(cle, out[cle])
    json.dump(out, open("sorties/mc_comparaison_modeles.json", "w"), indent=1, ensure_ascii=False)


def sensibilite_rendement():
    """Dotation nécessaire (S2, fonds seul, 30 ans) selon le rendement réel net et la règle de retrait.

    Deux règles : taux de retrait fixe de 2,75 %, ou taux adapté au rendement (rendement − 0,25 point).
    Le rendement réel net dépend du véhicule du fonds et de sa fiscalité (à valider, L4 § 2).
    """
    out = {}
    base = mc.parametres_solution("S2", div=0, div_annees=0, reserve0=RESERVES["S2"])
    for r in (0.015, 0.02, 0.025, 0.03, 0.035):
        for nom, taux in (("retrait_fixe_2.75", 0.0275), ("retrait_adapte", max(0.01, r - 0.0025))):
            P = dict(base, dot_rdt=r, dot_taux=taux)
            k95 = mc.dotation_necessaire(P, cible=0.05, horizon=30, n=6000, borne_haute=1.5e9)
            k50 = mc.dotation_necessaire(P, cible=0.50, horizon=30, n=6000, borne_haute=1.5e9)
            out[f"rendement_{r:.3f}_{nom}"] = {"rendement_reel_net": r, "taux_retrait": round(taux, 4),
                                               "k50": round(k50, -5), "k95": round(k95, -5)}
            print(r, nom, out[f"rendement_{r:.3f}_{nom}"])
    json.dump(out, open("sorties/mc_sensibilite_rendement.json", "w"), indent=1, ensure_ascii=False)


def dimensionnement():
    """Dotation des solutions telle que l'échec reste sous 5 % sur 20 ET 30 ans (critère n° 6 du Cadre)."""
    out = {}
    for scen in ("S1", "S2", "S3"):
        P = mc.parametres_solution(scen)
        k30 = mc.dotation_necessaire(P, cible=0.05, horizon=30, n=10000, borne_haute=1.5e9, ent_n=5)
        k20 = mc.dotation_necessaire(P, cible=0.05, horizon=20, n=10000, borne_haute=1.5e9, ent_n=5)
        out[scen] = {"dividendes": P["div"], "annees_dividendes": P["div_n"], "reserve": P["res0"],
                     "besoin": round(P["B0"], -3), "dotation_5pct_30ans": round(k30, -5),
                     "dotation_5pct_20ans": round(k20, -5), "dotation_actuelle": P["dot0"]}
        print(scen, out[scen])
    json.dump(out, open("sorties/mc_dimensionnement.json", "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    dotations()
    grille()
    ruptures()
    holding()
    distribution()
    comparaison_modeles()
    sensibilite_rendement()
