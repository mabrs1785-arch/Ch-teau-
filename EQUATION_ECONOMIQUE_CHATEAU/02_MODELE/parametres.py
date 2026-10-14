"""Registre des hypothèses du modèle : source unique de vérité.

Chaque appel p(...) enregistre une hypothèse avec ses trois valeurs (favorable, centrale, défavorable),
son unité, son statut et ses sources (identifiants des fichiers 01_RECHERCHE/sources/*.csv).
Les paramètres physiques des domaines types sont dans parametres_scenarios.py.
"""
from noyau import p
import parametres_scenarios  # noqa: F401

IDS_CLES = {"S2_vr_m2", "taux_gros_entretien", "cout_jardinier", "assurance_taux"}

# =============================================================================
# BÂTI (sources : agent R1)
# =============================================================================
G = "Bâti"
p("S1_vr_m2", "S1 — valeur de reconstruction à l'identique du château", 3000, fav=2400, dfv=4000,
  unite="€/m²", statut="ESTIMATION", sources="R1-26; R1-27", groupe=G,
  note="Bornes sourcées : 2 400 €/m² (exemple d'un courtier, Figaro 2020, surface développée) et "
       "5 000-10 000 €/m² (courtier 2026, fiabilité faible). Château simple, non protégé ou inscrit : "
       "bas de la fourchette. Affectation par scénario = hypothèse.")
p("S2_vr_m2", "S2 — valeur de reconstruction à l'identique du château", 3700, fav=2800, dfv=5000,
  unite="€/m²", statut="ESTIMATION", sources="R1-26; R1-27", groupe=G,
  note="Château inscrit : entre l'exemple de 2020 actualisé et le bas du barème du courtier de 2026.")
p("S3_vr_m2", "S3 — valeur de reconstruction à l'identique du château", 7000, fav=5000, dfv=10000,
  unite="€/m²", statut="ESTIMATION", sources="R1-27", groupe=G,
  note="Château classé avec décors : fourchette du courtier (5 000 à 10 000 €/m²), fiabilité faible.")
p("vr_dep_ratio", "Valeur de reconstruction des dépendances / celle du château (au m²)", 0.5, fav=0.4,
  dfv=0.6, unite="ratio", statut="HYPOTHÈSE", sources="R1", groupe=G,
  note="Écuries, granges et communs, de construction plus simple. Aucune source.")
p("taux_entretien_courant", "Entretien courant annuel, en % de la valeur de reconstruction", 0.0075,
  fav=0.005, dfv=0.01, unite="% par an", statut="HYPOTHÈSE", sources="R1-07", groupe=G,
  note="Part « courante » dans la règle globale de 2 à 4 %. La ventilation n'est pas sourcée (R1 § 9.1).")
p("taux_gros_entretien", "Provision de gros entretien, en % de la valeur de reconstruction", 0.0225,
  fav=0.015, dfv=0.03, unite="% par an", statut="ESTIMATION", sources="R1-07; R1-08; R1-05", groupe=G,
  note="La règle du NRC (2 à 4 % de la valeur de remplacement pour l'entretien-réparation, « absolute "
       "minimum ») porte sur des bâtiments publics américains, transposition à valider. Recoupement : "
       "les maisons historiques britanniques dépensent ≈ 156-161 k£ TTC/an et accumulent pourtant ≈ 2 M£ "
       "de retard chacune (R1-05). Une dépense « normale » est donc insuffisante pour un état d'exception.")
p("taux_aleas_travaux", "Aléas de chantier et découvertes, en % du gros entretien", 0.15, fav=0.10,
  dfv=0.20, unite="% du gros entretien", statut="HYPOTHÈSE", sources="R1-05", groupe=G,
  note="Dépassement observé de +29 % sur un chantier britannique (devis 42 k£, facture 54 k£).")
p("S1_securite", "S1 — sécurité (télésurveillance, détection incendie, maintenance)", 2500, fav=1500,
  dfv=4000, unite="€/an TTC", statut="HYPOTHÈSE", sources="R1-26", groupe=G,
  note="Coûts introuvables (R1 § 8). Les courtiers recommandent ces dispositifs pour modérer la prime.")
p("S2_securite", "S2 — sécurité", 7000, fav=4000, dfv=12000, unite="€/an TTC", statut="HYPOTHÈSE",
  sources="R1-26", groupe=G)
p("S3_securite", "S3 — sécurité (dont rondes et système incendie)", 25000, fav=15000, dfv=40000,
  unite="€/an TTC", statut="HYPOTHÈSE", sources="R1-26", groupe=G)
p("S1_honoraires_patrimoine", "S1 — architecte du patrimoine : état sanitaire et suivi", 1500, fav=0,
  dfv=4000, unite="€/an TTC", statut="HYPOTHÈSE", sources="R1-05", groupe=G,
  note="Rapport d'état quinquennal annualisé (pratique britannique « quinquennial survey »).")
p("S2_honoraires_patrimoine", "S2 — architecte du patrimoine : état sanitaire et suivi", 6000,
  fav=3000, dfv=10000, unite="€/an TTC", statut="HYPOTHÈSE", sources="R1-05", groupe=G)
p("S3_honoraires_patrimoine", "S3 — architecte du patrimoine : état sanitaire et suivi", 15000,
  fav=8000, dfv=25000, unite="€/an TTC", statut="HYPOTHÈSE", sources="R1-05", groupe=G)

# =============================================================================
# ÉNERGIE ET EAU (sources : agent R1)
# =============================================================================
G = "Énergie et eau"
p("S1_surf_chauffee", "S1 — surface chauffée à confort", 450, fav=350, dfv=560, unite="m²",
  statut="HYPOTHÈSE", sources="R1", groupe=G, note="50 à 80 % des 700 m² habitables (R1 § 9.1).")
p("S2_surf_chauffee", "S2 — surface chauffée à confort", 1000, fav=800, dfv=1200, unite="m²",
  statut="HYPOTHÈSE", sources="R1", groupe=G, note="40 à 60 % du château.")
p("S3_surf_chauffee", "S3 — surface chauffée à confort", 1800, fav=1350, dfv=2250, unite="m²",
  statut="HYPOTHÈSE", sources="R1", groupe=G, note="30 à 50 % du château.")
p("chauffage_kwh_m2", "Consommation de chauffage et d'eau chaude par m² chauffé", 220, fav=150, dfv=300,
  unite="kWh/m²/an", statut="HYPOTHÈSE", sources="R1-21", groupe=G,
  note="Aucune mesure de château trouvée. Repère : le SDES juge « très énergivore » un logement "
       "au-delà de 450 kWh/m² d'énergie finale.")
p("horsgel_kwh_m2", "Consommation hors-gel par m² non habité du château", 30, fav=15, dfv=50,
  unite="kWh/m²/an", statut="HYPOTHÈSE", groupe=G, note="Maintien hors-gel et lutte contre l'humidité.")
p("prix_chaleur_kwh", "Prix de l'énergie de chauffage livrée", 0.15, fav=0.10, dfv=0.20,
  unite="€ TTC/kWh", statut="SOURCÉ", sources="R1-22; R1-25", groupe=G,
  note="Bornes : granulés en vrac 10,4 c€ TTC/kWh (2023, ADEME repris par un tiers) ; gaz, prix "
       "repère 19,49 c€ TTC/kWh au 1er novembre 2026.")
p("S1_elec_kwh", "S1 — électricité spécifique (maison, écurie, extérieurs)", 20000, fav=15000,
  dfv=30000, unite="kWh/an", statut="HYPOTHÈSE", groupe=G)
p("S2_elec_kwh", "S2 — électricité spécifique (dont manège éclairé, écuries, ateliers)", 60000,
  fav=40000, dfv=90000, unite="kWh/an", statut="HYPOTHÈSE", groupe=G)
p("S3_elec_kwh", "S3 — électricité spécifique", 150000, fav=100000, dfv=220000, unite="kWh/an",
  statut="HYPOTHÈSE", groupe=G)
p("prix_elec_kwh", "Prix moyen de l'électricité", 0.238, fav=0.20, dfv=0.28, unite="€ TTC/kWh",
  statut="ESTIMATION", sources="R1-24", groupe=G,
  note="Tarif réglementé au 1er août 2026 : 1 072 € TTC pour 4,5 MWh, soit ≈ 238 €/MWh, abonnement compris.")
p("S1_eau", "S1 — eau et assainissement", 2500, fav=1500, dfv=4000, unite="€/an TTC",
  statut="HYPOTHÈSE", sources="R1-32", groupe=G,
  note="Repère : 432 €/an pour un petit château sans chevaux (déclaration d'un vendeur).")
p("S2_eau", "S2 — eau et assainissement", 7000, fav=4000, dfv=12000, unite="€/an TTC",
  statut="HYPOTHÈSE", groupe=G)
p("S3_eau", "S3 — eau et assainissement (dont arrosage des jardins)", 18000, fav=10000, dfv=30000,
  unite="€/an TTC", statut="HYPOTHÈSE", groupe=G)

# =============================================================================
# ASSURANCES, TAXES, ADMINISTRATION (sources : agent R1 ; R3 pour la fiscalité)
# =============================================================================
G = "Assurances, taxes, administration"
p("assurance_taux", "Prime d'assurance des bâtiments, en ‰ de la valeur de reconstruction", 0.003,
  fav=0.0015, dfv=0.005, unite="taux par an", statut="ESTIMATION", sources="R1-26; R1-27; R1-28; R1-32",
  groupe=G,
  note="Barème d'un courtier : ≈ 5 ‰ (fiabilité faible). Cas observés 3 à 10 fois plus bas (petit château "
       "MH : 2 198 €/an ; Olhain : ≈ 7 500 €/an en moyenne sur 40 ans). Taux central retenu entre les deux. "
       "Risque de résiliation documenté (Olhain, 2026). À remplacer par des devis.")
p("S1_assurances_autres", "S1 — RC, véhicules, chevaux, contenu", 3500, fav=2000, dfv=6000,
  unite="€/an TTC", statut="HYPOTHÈSE", sources="R1-27", groupe=G)
p("S2_assurances_autres", "S2 — RC, véhicules, chevaux, contenu", 9000, fav=5000, dfv=15000,
  unite="€/an TTC", statut="HYPOTHÈSE", sources="R1-27", groupe=G)
p("S3_assurances_autres", "S3 — RC, véhicules, chevaux, contenu, œuvres", 20000, fav=12000, dfv=35000,
  unite="€/an TTC", statut="HYPOTHÈSE", sources="R1-27", groupe=G)
p("tf_chateau_m2", "Taxe foncière bâtie du château, par m² de plancher", 6, fav=3, dfv=10,
  unite="€/m²/an", statut="HYPOTHÈSE", sources="R1-30; R1-31; R1-32", groupe=G,
  note="Un seul repère : 2 652 € pour 512 m² habitables (≈ 5,2 €/m²). La taxe dépend de la catégorie "
       "cadastrale fixée en 1970 et du taux communal, pas de la surface.")
p("ifi_abattement_rp", "IFI : abattement sur la résidence principale", 0.30, fav=0.30, dfv=0.0, unite="%",
  statut="SOURCÉ", sources="R3-01; R3-15", groupe=G,
  note="Barème 2026 : seuil 1,3 M€, taux de 0,5 % à 1,5 % ; aucune exonération pour les MH (amendement rejeté). "
       "Défavorable : château non résidence principale. La valeur retenue est le prix d'achat du scénario (valeur vénale).")
p("tf_dep_m2", "Taxe foncière bâtie des dépendances, par m²", 2, fav=1, dfv=3, unite="€/m²/an",
  statut="HYPOTHÈSE", sources="R1", groupe=G)
p("S1_admin", "S1 — administration (comptabilité, banque, informatique, télécoms)", 7000, fav=4000,
  dfv=12000, unite="€/an TTC", statut="HYPOTHÈSE", groupe=G)
p("S2_admin", "S2 — administration", 25000, fav=15000, dfv=40000, unite="€/an TTC",
  statut="HYPOTHÈSE", groupe=G)
p("S3_admin", "S3 — administration", 70000, fav=40000, dfv=110000, unite="€/an TTC",
  statut="HYPOTHÈSE", groupe=G)
p("taux_imprevus", "Imprévus d'exploitation, en % des charges de fonctionnement", 0.03, fav=0.02,
  dfv=0.05, unite="%", statut="HYPOTHÈSE", groupe=G,
  note="Absences, pannes, hausses ponctuelles. Les gros sinistres non assurés sont simulés à part (Monte-Carlo).")
p("taux_invest_futurs", "Investissements futurs, en % des charges et provisions", 0.04, fav=0.02,
  dfv=0.06, unite="%", statut="HYPOTHÈSE", groupe=G,
  note="Améliorations, mises aux normes, embellissements. Le brief exige de les financer.")

# =============================================================================
# SCÉNARIO COMPLÉMENTAIRE : DETTE D'ACQUISITION
# =============================================================================
G = "Scénario dette"
p("S1_prix_achat", "S1 — prix d'achat", 1_200_000, unite="€", statut="HYPOTHÈSE", sources="D-02",
  groupe=G, note="Marché : prix affichés de 920 k€ à 20 M€, prix de vente moyen de 2,415 M€ (Kretz, 2026).")
p("S2_prix_achat", "S2 — prix d'achat", 3_500_000, unite="€", statut="HYPOTHÈSE", sources="D-02",
  groupe=G)
p("S3_prix_achat", "S3 — prix d'achat", 9_000_000, unite="€", statut="HYPOTHÈSE", sources="D-02",
  groupe=G)
p("dette_quotite", "Part du prix financée par emprunt", 0.70, fav=0.50, dfv=0.80, unite="%",
  statut="HYPOTHÈSE", groupe=G)
p("dette_taux", "Taux d'intérêt de l'emprunt", 0.042, fav=0.035, dfv=0.055, unite="% par an",
  statut="ESTIMATION", sources="D-05", groupe=G,
  note="Crédits immobiliers aux particuliers : 3,27 % sur 20 ans (août 2026). Prime ajoutée pour un "
       "bien atypique ou un emprunteur professionnel.")
p("dette_duree", "Durée de l'emprunt", 20, fav=25, dfv=15, unite="années", statut="HYPOTHÈSE", groupe=G)

# =============================================================================
# PERSONNEL (sources : agent R2 — coûts employeur issus du simulateur officiel URSSAF, 2026)
# Effectifs = HYPOTHÈSES : domaine et chevaux du propriétaire seulement (pas d'activité commerciale).
# =============================================================================
G = "Personnel — coûts employeur annuels"
NOTE_URSSAF = ("Coût employeur annuel calculé par R2 avec le simulateur officiel URSSAF (RGDU 2026, SMIC à "
               "12,31 €/h depuis le 01/06/2026). Le niveau de salaire en multiple du SMIC est une HYPOTHÈSE, "
               "faute de salaires de marché publiés.")
p("S2_cout_direction", "S2 — régisseur de domaine (2,0 / 2,5 / 3,0 SMIC)", 79253, fav=62277, dfv=96730,
  unite="€/ETP/an", statut="ESTIMATION", sources="R2-11; R2-07", groupe=G, note=NOTE_URSSAF)
p("S3_cout_direction", "S3 — directeur de domaine (2,5 / 3,0 / 3,5 SMIC)", 96730, fav=79253, dfv=115000,
  unite="€/ETP/an", statut="ESTIMATION", sources="R2-11", groupe=G,
  note=NOTE_URSSAF + " Valeur défavorable extrapolée (au-delà des points du simulateur).")
p("S1_cout_direction", "S1 — régisseur (sans objet)", 0, unite="€/ETP/an", statut="HYPOTHÈSE", groupe=G)
p("cout_admin_salarie", "Assistant(e) administratif(ve) / comptable (1,4 / 1,5 / 1,6 SMIC)", 44289,
  fav=40479, dfv=48000, unite="€/ETP/an", statut="ESTIMATION", sources="R2-11; R2-05", groupe=G,
  note=NOTE_URSSAF)
p("cout_chef_jardinier", "Chef jardinier (1,5 / 1,75 / 2,0 SMIC)", 53470, fav=44289, dfv=62277,
  unite="€/ETP/an", statut="ESTIMATION", sources="R2-11; R2-07", groupe=G, note=NOTE_URSSAF)
p("cout_jardinier", "Jardinier qualifié (1,1 / 1,2 / 1,3 SMIC)", 32531, fav=28346, dfv=36566,
  unite="€/ETP/an", statut="ESTIMATION", sources="R2-11; R2-07", groupe=G,
  note=NOTE_URSSAF + " Grille du paysage O.4 à O.6 = 12,59 à 13,56 €/h.")
p("cout_agent_entretien", "Gardien, homme d'entretien (1,2 / 1,3 / 1,4 SMIC)", 36566, fav=32531,
  dfv=40479, unite="€/ETP/an", statut="ESTIMATION", sources="R2-11", groupe=G, note=NOTE_URSSAF)
p("cout_ouvrier_agricole", "Ouvrier agricole qualifié (1,1 / 1,2 / 1,3 SMIC)", 32531, fav=28346,
  dfv=36566, unite="€/ETP/an", statut="ESTIMATION", sources="R2-11; R2-09", groupe=G, note=NOTE_URSSAF)
p("cout_soigneur", "Soigneur, palefrenier (1,0 / 1,0 / 1,1 SMIC)", 23973, fav=23853, dfv=28216,
  unite="€/ETP/an", statut="ESTIMATION", sources="R2-11; R2-05", groupe=G, note=NOTE_URSSAF)
p("cout_resp_ecurie", "Responsable d'écurie, cavalier (1,3 / 1,4 / 1,5 SMIC)", 40479, fav=36566,
  dfv=44289, unite="€/ETP/an", statut="ESTIMATION", sources="R2-11; R2-05", groupe=G, note=NOTE_URSSAF)
p("cout_maison", "Employé(e) de maison, particulier employeur (1,0 / 1,1 / 1,2 SMIC × 1,30)", 32038,
  fav=29125, dfv=34950, unite="€/ETP/an", statut="ESTIMATION", sources="R2-03; R2-12", groupe=G,
  note="Particulier employeur : pas de RGDU ; coût estimé à brut × 1,30 par R2 (fragile, à vérifier "
       "avec le simulateur CESU).")
p("S1_cout_gouvernance", "S1 — gouvernante (sans objet)", 0, unite="€/ETP/an", statut="HYPOTHÈSE", groupe=G)
p("S2_cout_gouvernance", "S2 — gouvernante (1,3 / 1,4 / 1,5 SMIC × 1,30)", 40776, fav=37863, dfv=43688,
  unite="€/ETP/an", statut="ESTIMATION", sources="R2-03; R2-12", groupe=G)
p("S3_cout_gouvernance", "S3 — majordome et gouvernante, coût moyen par ETP", 58251, fav=50000,
  dfv=66000, unite="€/ETP/an", statut="ESTIMATION", sources="R2-03; R2-12", groupe=G,
  note="Moyenne d'un majordome à 2,5 SMIC (72 814 €) et d'une gouvernante à 1,5 SMIC (43 688 €), selon R2 § 9.4.")

G = "Personnel — effectifs (ETP) du domaine"
NOTE_ETP = ("HYPOTHÈSE d'effectif pour le domaine et les chevaux du propriétaire uniquement. R2 compte "
            "13 ETP en S2 et 29 ETP en S3 avec une écurie pleine de 40 à 50 chevaux : l'excédent relève "
            "d'une activité de pension, modélisée à part comme moteur de revenus.")
for scen, vals in {
    "S1": dict(direction=0, admin=0, chef_jardinier=0, jardin=1.0, entretien=0, agricole=0, soigneur=0.6,
               resp_ecurie=0, gouvernance=0, maison=0.5),
    "S2": dict(direction=1, admin=0, chef_jardinier=1, jardin=2, entretien=1, agricole=1, soigneur=1,
               resp_ecurie=1, gouvernance=1, maison=1),
    "S3": dict(direction=1, admin=1, chef_jardinier=1, jardin=16, entretien=2, agricole=2, soigneur=1.5,
               resp_ecurie=1, gouvernance=2, maison=2),
}.items():
    for role, etp in vals.items():
        if scen == "S3" and role == "jardin":
            p(f"{scen}_etp_{role}", f"{scen} — ETP {role.replace('_', ' ')}", etp, unite="ETP",
              statut="ESTIMATION", sources="V2C-21; R2", groupe=G,
              note="R2 retenait 11 jardiniers. V2C (temps d'entretien de la Ville de Rennes) : 15,7 ETP pour 60 ha "
                   "en gestion différenciée (1 ha très fleuri, 9 ha de jardin régulier, 10 ha d'accompagnement, "
                   "40 ha de prairie fauchée), 19,7 ETP avec 40 ha de pelouse champêtre, 33,4 ETP si tout le parc "
                   "est soigné. Le budget suppose donc une gestion différenciée.")
        else:
            p(f"{scen}_etp_{role}", f"{scen} — ETP {role.replace('_', ' ')}", etp, unite="ETP",
              statut="HYPOTHÈSE", sources="R2" + ("; V2C-21" if role == "jardin" else ""), groupe=G, note=NOTE_ETP)

# =============================================================================
# JARDINS, TERRES, ÉQUIPEMENTS, CHEVAUX (sources : agent R2)
# =============================================================================
G = "Jardins, terres, équipements, chevaux"
p("jardin_ha", "Jardins réguliers : fournitures, végétaux, traitements, sous-traitance (hors personnel)",
  5000, fav=3000, dfv=8000, unite="€/ha/an TTC", statut="HYPOTHÈSE", sources="R2", groupe=G,
  note="Coûts au m² introuvables (Plante & Cité réservé aux adhérents). Hypothèse à remplacer par des devis.")
p("parc_ha", "Parc : fauche, élagage par arboriste, replantation (hors personnel)", 800, fav=500,
  dfv=1500, unite="€/ha/an TTC", statut="HYPOTHÈSE", sources="R2", groupe=G)
p("prairie_ha", "Prairies : entretien hors récolte", 180, fav=120, dfv=250, unite="€/ha/an",
  statut="ESTIMATION", sources="R2-17; R2-26", groupe=G,
  note="Repères : 120 €/ha (2012, entretien par un professionnel) et 185 €/ha/an (2008, hors récolte).")
p("cloture_ml", "Clôture équestre de qualité posée", 35, fav=20, dfv=60, unite="€/ml",
  statut="HYPOTHÈSE", sources="R2", groupe=G, note="Fourchette proposée par R2 sans source (20 à 60 €/ml).")
p("cloture_vie", "Durée de vie des clôtures", 20, fav=25, dfv=15, unite="années", statut="HYPOTHÈSE",
  sources="R2", groupe=G)
p("bois_cout_ha", "Bois : gestion courante", 30, fav=15, dfv=60, unite="€/ha/an", statut="HYPOTHÈSE",
  groupe=G, note="À recouper avec R8 (revenu forestier net).")
p("S1_valeur_equip", "S1 — parc de matériel à neuf (tracteur compact, broyeur, épandeur, tondeuses, utilitaire)",
  170000, unite="€ HT", statut="ESTIMATION", sources="R2-30", groupe=G,
  note="≈ 130 000 € selon le guide des cuma 2025-2026, plus ≈ 40 000 € de tondeuses et d'utilitaire (hypothèse).")
p("S2_valeur_equip", "S2 — parc de matériel à neuf (2 tracteurs, télescopique, fenaison, épandeur, tondeuses, utilitaires)",
  500000, unite="€ HT", statut="ESTIMATION", sources="R2-30", groupe=G,
  note="≈ 436 000 € selon le guide des cuma, plus ≈ 60 000 € de tondeuses et de véhicules (hypothèse).")
p("S3_valeur_equip", "S3 — parc de matériel à neuf", 665000, unite="€ HT", statut="ESTIMATION",
  sources="R2-30", groupe=G, note="≈ 565 000 € selon le guide des cuma, plus ≈ 100 000 € (hypothèse).")
p("equip_vie", "Durée de renouvellement moyenne du matériel", 10, fav=12, dfv=8, unite="années",
  statut="SOURCÉ", sources="R2-30", groupe=G, note="Durées d'amortissement des cuma : 8,2 à 10,7 ans.")
p("equip_entretien_taux", "Entretien, réparations et carburant du matériel, en % de sa valeur", 0.06,
  fav=0.04, dfv=0.08, unite="% par an", statut="HYPOTHÈSE", sources="R2-30", groupe=G)
p("cheval_an", "Coût annuel d'un cheval au box hors personnel (alimentation, litière, maréchal, vétérinaire, assurance, eau)",
  4000, fav=2900, dfv=5500, unite="€/cheval/an TTC", statut="ESTIMATION",
  sources="R2-17; R2-18; R2-24; R2-21", groupe=G,
  note="Alimentation + litière 1 000 à 2 000 € ; maréchal 525 à 1 040 € ; soins 270 à 500 € ; aléas 300 à "
       "500 € ; assurance 450 à 750 € (prix de 2012 majorés d'environ 20 %). Hors compétition.")
p("sol_cout_m2", "Réfection des sols équestres (sable fibré, nivellement)", 12, fav=8, dfv=18,
  unite="€/m²", statut="ESTIMATION", sources="R2-27", groupe=G,
  note="Sable classique 3 à 8 €/m², fibré 10 à 15 €/m² (site commercial, fiabilité faible).")
p("sol_vie", "Durée de vie d'un sol équestre", 10, fav=12, dfv=8, unite="années", statut="HYPOTHÈSE",
  groupe=G, note="Durée de vie introuvable (R2).")
p("box_entretien", "Entretien et renouvellement d'un box", 500, fav=300, dfv=900, unite="€/box/an",
  statut="ESTIMATION", sources="R2-28", groupe=G, note="Box de 8 000 à 25 000 € sur 25 ans.")
p("manege_cout_m2", "Manège couvert : coût de construction", 180, fav=150, dfv=250, unite="€/m²",
  statut="ESTIMATION", sources="R2-27", groupe=G, note="220 000 à 305 000 € pour 60 × 25 m (fiabilité faible).")
p("manege_vie", "Durée de vie d'un manège", 30, fav=35, dfv=25, unite="années", statut="SOURCÉ",
  sources="R2-27", groupe=G, note="Acier galvanisé 30 à 40 ans ; bois 20 à 30 ans.")
p("tfnb_ha", "Taxe foncière sur le non bâti", 12, fav=6, dfv=25, unite="€/ha/an", statut="HYPOTHÈSE",
  groupe=G, note="Aucune donnée trouvée ; exonérations partielles possibles pour les terres agricoles (à vérifier, R3).")
