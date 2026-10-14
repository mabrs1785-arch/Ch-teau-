"""Comparaison des modèles économiques face au besoin du domaine S2.

Un modèle est une combinaison de moteurs (feuille Moteurs), décrite par une matrice de configuration.
Les coefficients sont dans la feuille Hypotheses, groupe « Configuration des modèles » : 1 = moteur
retenu, 0 = moteur absent.

Pour chaque modèle et chaque cas (favorable, central, défavorable), on calcule :
- la contribution brute des activités sur place (avant impôt) ;
- la contribution disponible pour le domaine, après la « fuite fiscale » (IS, puis PFU ou impôt sur
  les loyers, pour financer des coûts privés) ;
- la couverture du besoin annuel du domaine S2 ;
- l'écart restant ;
- le capital de dotation, ou l'EBITDA d'entreprise extérieure, nécessaire pour combler cet écart ;
- l'investissement initial des activités ;
- la part de revenus récurrents (classes A et B).
"""
from noyau import p

MOTEURS = {  # code : (nom de la contribution sur la feuille Moteurs, classe, investissement éventuel)
    "EQ_STD": ("mot_eq_std_cn", "B", None),
    "EQ_HDG": ("mot_eq_hdg_cn", "B", None),
    "EQ_PRO": ("mot_eq_pro_cn", "A", None),
    "EQ_RET": ("mot_eq_ret_cn", "B", None),
    "REPRO": ("mot_repro_cn", "B", None),
    "EVT": ("mot_evt_cn", "C", "mot_evt_inv"),
    "TOURN": ("mot_tourn_cn", "C", None),
    "SEMJ": ("mot_semj_cn", "C", None),
    "GITE": ("mot_gite_cn", "C", "mot_gite_inv"),
    "LOG": ("mot_log_cn", "A", "mot_log_inv"),
    "STOCK": ("mot_stock_cn", "A", "stock_capex"),
    "AUTO": ("mot_auto_cn", "A", "auto_capex"),
    "PV": ("mot_pv_cn", "A", None),
    "BOIS": ("mot_bois_cn", "A", None),
    "HOTEL": ("mot_hot_cn", "B", "mot_hot_inv"),
    "ANC": ("mot_anc_cn", "A", None),
    "LUX": ("mot_lux_cn", "C", "lux_capex"),
}

MODELES = {
    "M1": ("Socle contractuel et équestre standard (résidence calme)",
           ["EQ_STD", "EQ_RET", "LOG", "STOCK", "PV", "BOIS", "TOURN"]),
    "M2": ("Lieu d'exception à quota (M1 + réceptions, séminaires, grande maison)",
           ["EQ_STD", "EQ_RET", "LOG", "STOCK", "PV", "BOIS", "TOURN", "EVT", "SEMJ", "GITE"]),
    "M3": ("Équestre haut de gamme et services (pension, retraite, reproduction)",
           ["EQ_HDG", "EQ_RET", "REPRO", "BOIS", "TOURN"]),
    "M4": ("Château-hôtel opéré (15 chambres) + réceptions et séminaires",
           ["HOTEL", "EVT", "SEMJ", "EQ_STD", "BOIS", "TOURN"]),
    "M5": ("Socle minimal + dotation financière extérieure",
           ["EQ_STD", "BOIS", "TOURN"]),
    "M6": ("Socle minimal + entreprise extérieure",
           ["EQ_STD", "BOIS", "TOURN"]),
    "M7": ("Locataire d'ancrage : bail à un exploitant de séminaires + socle foncier",
           ["ANC", "EQ_RET", "PV", "BOIS"]),
    "M8": ("Socle M1 + location de luxe de la partie privée quelques semaines par an",
           ["EQ_STD", "EQ_RET", "LOG", "STOCK", "PV", "BOIS", "TOURN", "LUX"]),
}

G = "Configuration des modèles"
for m, (titre, retenus) in MODELES.items():
    for code in MOTEURS:
        p(f"cfg_{m}_{code}", f"{m} — moteur {code} retenu (1) ou non (0)", 1 if code in retenus else 0,
          unite="coefficient", statut="HYPOTHÈSE", groupe=G, note=f"{m} : {titre}")

p("fuite_fiscale", "Fuite fiscale sur les contributions sur place utilisées pour des coûts privés",
  0.30, fav=0.15, dfv=0.486, unite="%", statut="ESTIMATION", sources="R3-16; R3-20; R3-57", groupe=G,
  note="Chaîne complète IS 25 % puis PFU 31,4 % = 48,6 % (défavorable). Une part des contributions finance "
       "des coûts professionnels déductibles (loyers payés à la SCI, entretien des espaces exploités) et "
       "subit moins d'impôt : 15 à 30 %. Calcul consolidé exact dans la projection sur 20 ans.")


def _lignes():
    lignes = []
    for m, (titre, _r) in MODELES.items():
        somme = "+".join(f"cfg_{m}_{c}{{C}}*{nom}{{C}}" for c, (nom, _k, _i) in MOTEURS.items())
        somme_ab = "+".join(f"cfg_{m}_{c}{{C}}*{nom}{{C}}" for c, (nom, k, _i) in MOTEURS.items() if k in "AB")
        inv = "+".join(f"cfg_{m}_{c}{{C}}*{i}{{C}}" for c, (_n, _k, i) in MOTEURS.items() if i)
        lignes += [
            (f"{m}_brute", f"{m} — contribution brute des activités sur place (avant impôt)", somme, titre, 0, "S"),
            (f"{m}_nette", f"{m} — contribution disponible pour le domaine (après fuite fiscale)",
             f"IF([{m}_brute]>0,[{m}_brute]*(1-fuite_fiscale{{C}}),[{m}_brute])", titre, 0, "S"),
            (f"{m}_besoin", f"{m} — besoin annuel du domaine S2 (feuille Budget)", "bud_total_besoin_S2{C}", titre, 0, "S"),
            (f"couv_{m}", f"{m} — couverture du besoin par les activités sur place", f"[{m}_nette]/[{m}_besoin]", titre, 0, "S"),
            (f"{m}_ecart", f"{m} — écart restant à financer", f"MAX(0,[{m}_besoin]-[{m}_nette])", titre, 0, "S"),
            (f"{m}_dotation", f"{m} — capital de dotation nécessaire pour combler l'écart",
             f"[{m}_ecart]/dot_taux_net{{C}}", titre, 0, "S"),
            (f"{m}_ebitda", f"{m} — ou EBITDA d'entreprise extérieure nécessaire",
             f"[{m}_ecart]/ent_conversion{{C}}", titre, 0, "S"),
            (f"{m}_invest", f"{m} — investissement initial des activités", inv, titre, 0, "S"),
            (f"part_{m}_recurrent", f"{m} — part des contributions récurrentes (classes A et B)",
             f"IF([{m}_brute]>0,({somme_ab})/[{m}_brute],0)", titre, 0, "S"),
        ]
    return lignes


LIGNES = _lignes()


def ecrire(wb):
    from excel_outils import ecrire_tableau_gabarits
    colonnes = [("Favorable", None, "fav"), ("Central", None, "cen"), ("Défavorable", None, "def")]
    _, controle = ecrire_tableau_gabarits(
        wb, "Modeles", "COMPARAISON DES MODÈLES ÉCONOMIQUES — domaine S2 (€ 2026 par an)", LIGNES, colonnes,
        prefixe_noms="mod_",
        note=("Chaque modèle combine des moteurs de la feuille Moteurs (matrice de configuration dans la feuille "
              "Hypotheses). Couverture = contribution disponible ÷ besoin annuel du domaine S2. L'écart restant "
              "doit être financé par un moteur extérieur : capital de dotation (au taux de retrait net "
              "soutenable) ou EBITDA d'une entreprise (dividende net par euro d'EBITDA)."))
    return controle
