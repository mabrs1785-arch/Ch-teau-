"""Projection sur 20 ans (euros constants 2026) et stress tests.

Les feuilles « Proj_* » partagent la même logique, écrite une seule fois ci-dessous :
- besoin du domaine : budget central du scénario, avec des dérives réelles (salaires, travaux, énergie) ;
- gros entretien : provision annuelle versée dans un fonds dédié, dépensé par campagnes tous les
  `campagne_periode` ans (travaux réels par à-coups, pas lissés) ;
- activités sur place : contributions des moteurs retenus (feuille Moteurs, cas central), avec montée
  en charge et multiplicateurs de stress par classe (A contractuel, B récurrent, C occasionnel) ;
- moteur extérieur : dividendes nets d'une entreprise pendant une période de transition, puis dotation
  financière avec une règle de dépense (retrait plafonné à `dot_taux_net` × capital de l'année précédente) ;
- réserve de trésorerie : absorbe les écarts ; les excédents alimentent la dotation ;
- options : dette d'acquisition (annuité nominale, donc décroissante en euros constants), avantage fiscal MH.

Chaque test de résistance a sa propre feuille, avec ses paramètres `st_<test>_*` nommés.
"""
from noyau import p

N_ANNEES = 20

# ---------------------------------------------------------------------------------------------------
# Hypothèses communes de projection
# ---------------------------------------------------------------------------------------------------
G = "Projection — dérives et règles"
p("g_salaires", "Dérive réelle annuelle des salaires (au-delà de l'inflation)", 0.005, fav=0.0, dfv=0.01,
  unite="% par an", statut="ESTIMATION", sources="D-01", groupe=G,
  note="Banque de France (sept. 2026) : salaire moyen par tête +2,0 %, +2,6 %, +2,4 % en 2026-2028, pour "
       "une inflation de 2,3 %, 1,9 %, 1,6 %, soit environ +0,4 % réel par an en moyenne.")
p("g_travaux", "Dérive réelle annuelle du coût des travaux", 0.005, fav=0.0, dfv=0.01, unite="% par an",
  statut="ESTIMATION", sources="D-04; D-01", groupe=G,
  note="BT01 +1,3 % en 2025 pour une inflation de 0,9 %.")
p("g_energie", "Dérive réelle annuelle du prix de l'énergie", 0.01, fav=0.0, dfv=0.025, unite="% par an",
  statut="HYPOTHÈSE", sources="R1-22; R1-24", groupe=G)
p("g_recettes", "Dérive réelle annuelle des prix des activités", 0.0, fav=0.005, dfv=-0.005, unite="% par an",
  statut="HYPOTHÈSE", groupe=G)
p("inflation", "Inflation annuelle (pour convertir une annuité nominale en euros constants)", 0.02,
  unite="% par an", statut="ESTIMATION", sources="D-01", groupe=G,
  note="Cible de la BCE ; projections de la Banque de France : 1,9 % (2027), 1,6 % (2028).")
p("campagne_periode", "Périodicité des campagnes de gros entretien", 4, unite="années", statut="HYPOTHÈSE",
  sources="R1-11; R1-14", groupe=G, note="Les toitures de châteaux privés sont refaites par tranches successives.")
p("rampe_an1", "Montée en charge des activités : année 1", 0.4, unite="%", statut="HYPOTHÈSE", groupe=G)
p("rampe_an2", "Montée en charge des activités : année 2", 0.75, unite="%", statut="HYPOTHÈSE", groupe=G)
p("taux_reserve", "Rendement réel de la réserve de trésorerie", 0.0, unite="% par an", statut="HYPOTHÈSE",
  groupe=G, note="Placement liquide ≈ inflation.")
p("dot_rendement", "Rendement réel net de frais et d'impôts de la dotation (moyenne)", 0.03, fav=0.035,
  dfv=0.0225, unite="% par an", statut="ESTIMATION", sources="R8-32; R8-34; R8-31", groupe=G,
  note="Actions mondiales : 3,5 % réel par an depuis 2000 (UBS 2025), avant impôt ; dotations américaines "
       "exonérées : cible inflation + 5 %. Portefeuille diversifié d'un résident français, après impôt : ≈ 3 %.")
p("part_surplus_dotation", "Part des excédents annuels versée à la dotation", 1.0, unite="%",
  statut="HYPOTHÈSE", groupe=G)
p("subvention_taux", "Subventions de travaux : part moyenne des campagnes (scénario favorable seulement)",
  0.10, unite="%", statut="ESTIMATION", sources="R1-34; R1-33", groupe=G,
  note="DRAC : 20 % (inscrit) ou 40 % (classé) des travaux éligibles, crédits en baisse de 29 % en 2026. "
       "10 % du total, après prise en compte de la part non éligible et de la probabilité d'obtention.")
p("mh_tmi", "Avantage fiscal MH : taux marginal d'impôt sur le revenu du propriétaire", 0.41, fav=0.45,
  dfv=0.30, unite="%", statut="HYPOTHÈSE", sources="R3-02; R3-05", groupe=G)
p("mh_part_deductible", "Avantage MH : part du besoin constituée de charges déductibles (bâti, taxes, assurances)",
  0.45, unite="%", statut="HYPOTHÈSE", sources="R3-05", groupe=G,
  note="Réparations, entretien, amélioration, impôts fonciers, intérêts, primes d'assurance des MH (BOFiP). "
       "Le personnel de maison et les chevaux n'en font pas partie.")
p("mh_taux_deduction", "Avantage MH : taux de déduction (50 % fermé au public, 100 % ouvert 50 jours par an)",
  0.5, unite="%", statut="SOURCÉ", sources="R3-02; R3-04", groupe=G)

# ---------------------------------------------------------------------------------------------------
# Configurations (solution et variantes) et tests de résistance
# ---------------------------------------------------------------------------------------------------
# Moteurs sur place de la solution recommandée, par classe ; chaque moteur porte un facteur d'échelle
# par scénario (les contributions de la feuille Moteurs sont calculées à l'échelle d'un domaine S2).
SOLUTION_MOTEURS = {"A": ["log", "stock", "pv", "bois"], "B": ["eq_std", "eq_ret"], "C": ["tourn"]}
NOM_CONTRIB = {"log": "mot_log_cn", "stock": "mot_stock_cn", "pv": "mot_pv_cn", "bois": "mot_bois_cn",
               "eq_std": "mot_eq_std_cn", "eq_ret": "mot_eq_ret_cn", "tourn": "mot_tourn_cn"}
SOLUTION_INVEST = {"log": "mot_log_inv", "stock": "stock_capex"}
ECHELLES = {  # facteur d'échelle par rapport à S2 (HYPOTHÈSE cohérente avec la description physique)
    "S1": {"log": 0.25, "stock": 0.0, "pv": 0.4, "bois": 0.4, "eq_std": 0.267, "eq_ret": 0.333, "tourn": 0.5},
    "S2": {"log": 1.0, "stock": 1.0, "pv": 1.0, "bois": 1.0, "eq_std": 1.0, "eq_ret": 1.0, "tourn": 1.0},
    "S3": {"log": 2.0, "stock": 1.0, "pv": 2.0, "bois": 4.0, "eq_std": 1.267, "eq_ret": 1.333, "tourn": 1.5},
}
_JUSTIF = {"S1": "S1 : 8 boxes en pension (12 − 4 chevaux du propriétaire), 10 chevaux au pré, une maison de 150 m², "
                 "pas de grange disponible pour le stockage, 2 ha de solaire au mieux, 12 ha de bois.",
           "S2": "S2 : échelle de référence de la feuille Moteurs.",
           "S3": "S3 : 38 boxes en pension, 40 chevaux au pré, 1 200 m² de logements, 10 ha de solaire, 120 ha de bois."}

TESTS = {
    # identifiant : (libellé, paramètres de stress)
    "central": ("Projection centrale", {}),
    "ca30": ("Chiffre d'affaires des activités −30 % dès l'année 3", {"mult_A": 0.7, "mult_B": 0.7, "mult_C": 0.7, "debut_mult": 3}),
    "crise": ("Crise de type 2020 en année 5 (C −80 %, B −15 %, A −5 % ; dotation −25 % ; dividendes −50 %), reprise partielle en année 6",
              {"crise_an": 5}),
    "travaux": ("Sinistre ou découverte non assurés en année 6 (+600 000 €) et campagnes +30 %",
                {"choc_trav_an": 6, "choc_trav_montant": 600000, "mult_campagne": 1.3}),
    "energie": ("Prix de l'énergie ×2 pendant 3 ans (années 4 à 6)", {"energie_debut": 4, "energie_fin": 6, "energie_mult": 2.0}),
    "salaires": ("Salaires +1,5 % réel par an au lieu de +0,5 %", {"g_sal_extra": 0.01}),
    "moteur": ("Moteur extérieur défaillant : dividendes nuls dès l'année 3 et rendement de la dotation −1 point",
               {"div_fin": 2, "dot_rdt_delta": -0.01}),
    "cumul": ("Cumul défavorable : activités −30 %, crise en année 5, sinistre de 600 000 € en année 6, salaires +1,5 % réel",
              {"mult_A": 0.7, "mult_B": 0.7, "mult_C": 0.7, "debut_mult": 3, "crise_an": 5,
               "choc_trav_an": 6, "choc_trav_montant": 600000, "g_sal_extra": 0.01}),
}

DEFAUTS_STRESS = {"mult_A": 1.0, "mult_B": 1.0, "mult_C": 1.0, "debut_mult": 99, "crise_an": 0,
                  "choc_trav_an": 0, "choc_trav_montant": 0, "mult_campagne": 1.0, "energie_debut": 99,
                  "energie_fin": 0, "energie_mult": 1.0, "g_sal_extra": 0.0, "div_fin": 99, "dot_rdt_delta": 0.0}

G = "Stress tests"
for tid, (lib, vals) in TESTS.items():
    for k, defaut in DEFAUTS_STRESS.items():
        p(f"st_{tid}_{k}", f"Test « {tid} » — {k}", vals.get(k, defaut), unite="paramètre",
          statut="HYPOTHÈSE", groupe=G, note=lib)

G = "Projection — échelle des activités par scénario"
for _s, _d in ECHELLES.items():
    for _m, _f in _d.items():
        p(f"{_s}_ech_{_m}", f"{_s} — facteur d'échelle du moteur {_m} (par rapport à S2)", _f, unite="coefficient",
          statut="HYPOTHÈSE", groupe=G, note=_JUSTIF[_s])

# Paramètres des configurations par scénario
G = "Projection — moteur extérieur et options"
p("lissage_depense", "Règle de dépense lissée : poids du plafond de l'année précédente", 0.8, unite="%",
  statut="HYPOTHÈSE", sources="R8-34", groupe=G,
  note="Plafond(t) = 80 % × plafond(t−1) + 20 % × taux × dotation(t−1). Lisse les chocs de marché, sur le "
       "modèle des règles de dépense des grands fonds de dotation (cités par R8, sans détail de la règle).")
p("S2_sol_dotation0", "S2 — dotation affectée disponible à l'année 1", 30_000_000, unite="€",
  statut="HYPOTHÈSE", groupe=G,
  note="Dimensionnement testé, pas une ressource acquise. Voir le Monte-Carlo pour le capital qui donne "
       "95 % de probabilité de tenir 30 ans.")
p("S2_sol_div", "S2 — dividendes nets annuels de l'entreprise extérieure pendant la transition", 600_000,
  unite="€/an", statut="HYPOTHÈSE", groupe=G)
p("S2_sol_div_annees", "S2 — durée de la transition (années de dividendes)", 10, unite="années",
  statut="HYPOTHÈSE", groupe=G)
p("S2_sol_reserve0", "S2 — réserve de trésorerie initiale (≈ 12 mois de charges hors gros entretien)", 1_000_000,
  unite="€", statut="HYPOTHÈSE", groupe=G)
p("S1_sol_dotation0", "S1 — dotation affectée disponible à l'année 1", 8_000_000, unite="€",
  statut="HYPOTHÈSE", groupe=G)
p("S1_sol_div", "S1 — dividendes nets annuels pendant la transition", 200_000, unite="€/an",
  statut="HYPOTHÈSE", groupe=G)
p("S1_sol_div_annees", "S1 — durée de la transition", 10, unite="années", statut="HYPOTHÈSE", groupe=G)
p("S1_sol_reserve0", "S1 — réserve de trésorerie initiale", 300_000, unite="€", statut="HYPOTHÈSE", groupe=G)
p("pilotage_actif", "Règles de pilotage en période de tension (1 = oui)", 1, unite="0/1", statut="HYPOTHÈSE", groupe=G,
  note="Si la réserve passe sous `flex_seuil` année(s) de besoin : coupe des dépenses discrétionnaires, "
       "report d'une partie de la campagne de travaux, retrait d'urgence plafonné.")
p("flex_seuil", "Pilotage : seuil de déclenchement (réserve en années de besoin)", 1.0, unite="années",
  statut="HYPOTHÈSE", groupe=G)
p("flex_taux", "Pilotage : coupe temporaire des dépenses discrétionnaires (en % du besoin)", 0.10, unite="%",
  statut="HYPOTHÈSE", groupe=G,
  note="Investissements futurs (4 %), imprévus d'exploitation (3 %) et report d'achats de matériel et de jardins (≈ 3 %).")
p("flex_report", "Pilotage : part de la campagne de gros entretien reportée", 0.3, unite="%", statut="HYPOTHÈSE",
  groupe=G, note="Le report est remis dans le fonds de travaux : il ne disparaît pas.")
p("retrait_urgence", "Pilotage : retrait d'urgence maximal sur la dotation (en % du capital)", 0.04, unite="%",
  statut="HYPOTHÈSE", groupe=G)
p("S3_sol_dotation0", "S3 — dotation affectée disponible à l'année 1", 120_000_000, unite="€",
  statut="HYPOTHÈSE", groupe=G)
p("S3_sol_div", "S3 — dividendes nets annuels pendant la transition", 0, unite="€/an", statut="HYPOTHÈSE", groupe=G)
p("S3_sol_div_annees", "S3 — durée de la transition", 0, unite="années", statut="HYPOTHÈSE", groupe=G)
p("S3_sol_reserve0", "S3 — réserve de trésorerie initiale", 2_500_000, unite="€", statut="HYPOTHÈSE", groupe=G)
p("dette_active", "Option dette d'acquisition (1 = oui)", 0, unite="0/1", statut="HYPOTHÈSE", groupe=G)
p("mh_actif", "Option avantage fiscal MH (1 = oui, suppose des revenus imposables au barème)", 0,
  unite="0/1", statut="HYPOTHÈSE", groupe=G,
  note="Désactivée par défaut : l'avantage réduit l'impôt personnel du propriétaire et suppose qu'il ait des "
       "revenus imposables au barème (R3).")
p("sub_actif", "Option subventions de travaux (1 = oui ; jamais dans le scénario central)", 0, unite="0/1",
  statut="HYPOTHÈSE", groupe=G)


def _lignes(scen: str, tid: str, avec_moteur: bool = True):
    """Lignes de projection pour un scénario (S1/S2/S3) et un test de résistance."""
    st = lambda k: f"st_{tid}_{k}"  # noqa: E731
    def somme(moteurs):
        return "+".join(f"{scen}_ech_{m}*{NOM_CONTRIB[m]}" for m in moteurs)
    A, B, C = (somme(SOLUTION_MOTEURS[k]) for k in "ABC")
    inv = "+".join(f"{scen}_ech_{m}*{nom}" for m, nom in SOLUTION_INVEST.items())
    dot0 = f"{scen}_sol_dotation0" if avec_moteur else "0"
    div = f"{scen}_sol_div" if avec_moteur else "0"
    div_n = f"{scen}_sol_div_annees" if avec_moteur else "0"
    res0 = f"{scen}_sol_reserve0"
    L = []
    a = L.append
    # ---- indices de dérive réelle
    a(("idx_sal", "Indice des salaires (réel)", "1", f"[idx_sal@-1]*(1+g_salaires+{st('g_sal_extra')})", "nb"))
    a(("idx_trav", "Indice des travaux (réel)", "1", "[idx_trav@-1]*(1+g_travaux)", "nb"))
    a(("idx_en", "Indice de l'énergie (réel)", "1", "[idx_en@-1]*(1+g_energie)", "nb"))
    a(("idx_rec", "Indice des prix des activités (réel)", "1", "[idx_rec@-1]*(1+g_recettes)", "nb"))
    a(("idx_cpi", "Indice des prix à la consommation (pour la dette)", "1", "[idx_cpi@-1]*(1+inflation)", "nb"))
    a(("crise", "Année de crise (1) ou de reprise (2)", None,
       f"IF({st('crise_an')}>0,IF({{T}}={st('crise_an')},1,IF({{T}}={st('crise_an')}+1,2,0)),0)", "nb"))
    a(("tension", "Tension de trésorerie (1 = réserve sous le seuil de pilotage)", None,
       f"pilotage_actif*IF([reserve@-1]<flex_seuil*bud_total_besoin_{scen},1,0)", "nb"))
    # ---- besoin du domaine
    a(("b_pers", "Personnel du domaine", None, f"bud_dont_personnel_{scen}*[idx_sal]", "eur"))
    a(("b_energie", "Énergie", None,
       f"(bud_chauffage_{scen}+bud_hors_gel_{scen}+bud_electricite_{scen})*[idx_en]"
       f"*IF(AND({{T}}>={st('energie_debut')},{{T}}<={st('energie_fin')}),{st('energie_mult')},1)", "eur"))
    a(("b_autres", "Autres charges courantes (entretien courant, jardins, matériel, chevaux, assurances, taxes, administration, imprévus, investissements futurs)",
       None, f"bud_total_besoin_{scen}-bud_dont_personnel_{scen}-bud_bati_ge_{scen}-bud_imprevus_travaux_{scen}"
             f"-bud_chauffage_{scen}-bud_hors_gel_{scen}-bud_electricite_{scen}", "eur"))
    a(("b_ge_prov", "Provision de gros entretien versée au fonds de travaux", None,
       f"(bud_bati_ge_{scen}+bud_imprevus_travaux_{scen})*[idx_trav]", "eur"))
    a(("total_charges", "TOTAL DU BESOIN ANNUEL DU DOMAINE", None, "[b_pers]+[b_energie]+[b_autres]+[b_ge_prov]", "eur"))
    # ---- fonds de gros entretien
    a(("campagne", "Campagne de gros entretien (dépense du fonds)", None,
       f"IF(MOD({{T}},campagne_periode)=0,([fonds_ge@-1]+[b_ge_prov])*{st('mult_campagne')}*(1-[tension]*flex_report),0)", "eur"))
    a(("choc_trav", "Sinistre ou découverte non assurés", None,
       f"IF({{T}}={st('choc_trav_an')},{st('choc_trav_montant')},0)", "eur"))
    a(("depassement_trav", "Dépassement de travaux à financer hors fonds", None,
       "MAX(0,[campagne]+[choc_trav]-[fonds_ge@-1]-[b_ge_prov])", "eur"))
    a(("fonds_ge", "Fonds de gros entretien (fin d'année)", "0",
       "MAX(0,[fonds_ge@-1]+[b_ge_prov]-[campagne]-[choc_trav])", "eur"))
    a(("subvention", "Subventions de travaux encaissées (option)", None, "sub_actif*subvention_taux*[campagne]", "eur"))
    # ---- activités sur place
    a(("rampe", "Montée en charge des activités", None, "IF({T}=1,rampe_an1,IF({T}=2,rampe_an2,1))", "pct"))
    for k, lst, nom in (("A", A, "contractuelles (classe A)"), ("B", B, "récurrentes opérationnelles (classe B)"),
                        ("C", C, "occasionnelles (classe C)")):
        crise_k = {"A": "0.05", "B": "0.15", "C": "0.8"}[k]
        repr_k = {"A": "0.02", "B": "0.05", "C": "0.3"}[k]
        a((f"act_{k}", f"Contribution des activités {nom}", None,
           f"({lst})*[rampe]*[idx_rec]*IF({{T}}>={st('debut_mult')},{st('mult_' + k)},1)"
           f"*IF([crise]=1,1-{crise_k},IF([crise]=2,1-{repr_k},1))", "eur"))
    a(("act_brute", "Contribution brute des activités sur place", None, "[act_A]+[act_B]+[act_C]", "eur"))
    a(("act_nette", "Contribution des activités après fuite fiscale", None,
       "IF([act_brute]>0,[act_brute]*(1-fuite_fiscale),[act_brute])", "eur"))
    a(("capex_act", "Investissements des activités (année 1, prélevés sur le capital de la dotation)", None,
       f"IF({{T}}=1,{inv},0)", "eur"))
    # ---- options
    a(("dette", "Annuité de la dette d'acquisition, en euros constants (option)", None,
       f"dette_active*IF({{T}}<=dette_duree,-PMT(dette_taux,dette_duree,{scen}_prix_achat*dette_quotite)/[idx_cpi],0)", "eur"))
    a(("avantage_mh", "Avantage fiscal MH sur l'impôt personnel (option)", None,
       "mh_actif*mh_tmi*mh_part_deductible*mh_taux_deduction*[total_charges]", "eur"))
    a(("economie_pilotage", "Économies de pilotage (coupe temporaire des dépenses discrétionnaires)", None,
       f"[tension]*flex_taux*bud_total_besoin_{scen}", "eur"))
    # ---- besoin net à couvrir par le moteur extérieur
    a(("besoin_net", "Besoin net à couvrir hors activités (charges courantes + provision + dépassements + investissements + dette − activités − aides)",
       None, "[b_pers]+[b_energie]+[b_autres]+[b_ge_prov]+[depassement_trav]+[dette]-[act_nette]-[subvention]-[avantage_mh]-[economie_pilotage]", "eur"))
    # ---- moteur extérieur
    a(("dividendes", "Dividendes nets de l'entreprise extérieure", None,
       f"IF(AND({{T}}<={div_n},{{T}}<={st('div_fin')}),{div}*IF([crise]=1,0.5,1),0)", "eur"))
    a(("rdt_dot", "Rendement réel de la dotation de l'année", None,
       f"dot_rendement+{st('dot_rdt_delta')}+IF([crise]=1,-0.25,0)", "pct"))
    a(("plafond", "Plafond de retrait de la règle de dépense lissée", f"dot_taux_net*{dot0}",
       "lissage_depense*[plafond@-1]+(1-lissage_depense)*dot_taux_net*MAX(0,[dotation_fin@-1])", "eur"))
    a(("retrait", "Retrait sur la dotation (plafonné par la règle de dépense)", None,
       "MIN(MAX(0,[besoin_net]-[dividendes]),IF([tension]=1,MAX([plafond],retrait_urgence*MAX(0,[dotation_fin@-1])),[plafond]))", "eur"))
    a(("flux_solde", "SOLDE DE TRÉSORERIE DE L'ANNÉE (après moteur extérieur)", None,
       "[dividendes]+[retrait]-[besoin_net]", "eur"))
    a(("apport_dot", "Excédent versé à la dotation", None,
       "IF(AND([flux_solde]>0,[reserve@-1]>0),[flux_solde]*part_surplus_dotation,0)", "eur"))
    a(("dotation_fin", "DOTATION (fin d'année)", dot0,
       "MAX(0,[dotation_fin@-1])*(1+[rdt_dot])-[retrait]+[apport_dot]-[capex_act]", "eur"))
    a(("reserve", "RÉSERVE DE TRÉSORERIE (fin d'année)", res0,
       "[reserve@-1]*(1+taux_reserve)+[flux_solde]-[apport_dot]", "eur"))
    a(("kpi_liquidite", "Liquidité totale (réserve + fonds de travaux)", None, "[reserve]+[fonds_ge]", "eur"))
    a(("kpi_couverture", "Couverture du besoin par activités + règle de dépense de la dotation (hors dividendes)",
       None, "([act_nette]+[plafond])/[total_charges]", "pct"))
    a(("kpi_autonome", "Autonomie sans dividendes (1 = les activités et la dotation suffisent)", None,
       "IF([plafond]>=[besoin_net],1,0)", "nb"))
    a(("kpi_deficit", "Année en déficit de réserve (1 = réserve négative)", None, "IF([reserve]<0,1,0)", "nb"))
    return L


CONFIGS = [
    # (nom de feuille, scénario, test, avec moteur, titre)
    ("Proj_S2_sans_moteur", "S2", "central", False,
     "S2 — activités sur place seules, sans moteur extérieur (démonstration de l'écart)"),
    ("Proj_S2_solution", "S2", "central", True, "S2 — solution recommandée, projection centrale"),
] + [(f"ST_S2_{tid}", "S2", tid, True, f"S2 — solution recommandée, stress test : {TESTS[tid][0]}")
     for tid in TESTS if tid != "central"] + [
    ("Proj_S1_solution", "S1", "central", True, "S1 — solution recommandée, projection centrale"),
    ("ST_S1_cumul", "S1", "cumul", True, "S1 — solution recommandée, stress test cumulé"),
    ("Proj_S3_solution", "S3", "central", True, "S3 — solution recommandée, projection centrale"),
]

NOTE = ("Euros constants 2026, cas central des hypothèses. Le besoin vient de la feuille Budget ; les contributions "
        "des activités viennent de la feuille Moteurs. Le gros entretien est provisionné chaque année dans un fonds "
        "et dépensé par campagnes. Le moteur extérieur verse des dividendes pendant la transition, puis la dotation "
        "prend le relais avec un retrait plafonné. Toute année où la réserve devient négative est un échec du modèle.")


def ecrire(wb):
    from openpyxl.workbook.defined_name import DefinedName
    from excel_outils import ecrire_projection
    from noyau import EXTRA
    controle = {}
    resume = {}
    for (nom, scen, tid, avec, titre) in CONFIGS:
        lignes = _lignes(scen, tid, avec)
        ws, ctrl, valeurs = ecrire_projection(wb, nom, titre, lignes, N_ANNEES, 1, note=NOTE)
        controle.update(ctrl)
        # noms de plages pour la synthèse (années 1 à 20)
        ligne_de = {lid: 5 + i for i, (lid, *_r) in enumerate(lignes)}
        for lid in ("reserve", "dotation_fin", "flux_solde", "kpi_couverture", "kpi_deficit", "total_charges",
                    "act_nette", "kpi_liquidite"):
            r = ligne_de[lid]
            nom_plage = f"prj_{nom}_{lid}"
            wb.defined_names[nom_plage] = DefinedName(nom_plage, attr_text=f"'{nom}'!$E${r}:$X${r}")
            EXTRA[nom_plage] = [valeurs[k][lid] for k in range(1, N_ANNEES + 1)]
        resume[nom] = valeurs
    controle.update(_ecrire_synthese(wb))
    return controle


def _ecrire_synthese(wb):
    from excel_outils import ecrire_tableau_gabarits
    lignes = []
    for (nom, scen, tid, avec, titre) in CONFIGS:
        lignes += [
            (f"{nom}_min_res", f"{titre} — réserve minimale sur 20 ans", f"MIN(prj_{nom}_reserve)", nom, 0, "S"),
            (f"{nom}_res20", f"{nom} — réserve en année 20", f"INDEX(prj_{nom}_reserve,1,20)", nom, 0, "S"),
            (f"{nom}_dot20", f"{nom} — dotation en année 20", f"INDEX(prj_{nom}_dotation_fin,1,20)", nom, 0, "S"),
            (f"{nom}_def", f"{nom} — nombre d'années avec réserve négative", f"SUM(prj_{nom}_kpi_deficit)", nom, 0, "S"),
            (f"{nom}_act", f"{nom} — contribution moyenne des activités sur place", f"AVERAGE(prj_{nom}_act_nette)", nom, 0, "S"),
        ]
    colonnes = [("Valeur", None, "cen")]
    _, controle = ecrire_tableau_gabarits(
        wb, "Stress_synthese", "SYNTHÈSE DES PROJECTIONS ET DES STRESS TESTS (€ 2026)", lignes, colonnes,
        note="Indicateurs calculés sur les feuilles Proj_* et ST_* (années 1 à 20). Un modèle échoue si la réserve devient négative.")
    return controle
