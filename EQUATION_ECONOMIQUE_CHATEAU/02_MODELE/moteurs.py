"""Moteurs de revenus : économie unitaire de chaque activité, à l'échelle d'un domaine S2.

Pour chaque moteur, le modèle calcule :
- le chiffre d'affaires HT ;
- les charges propres (variables et fixes, personnel compris) ;
- une provision de renouvellement de l'investissement propre ;
- la contribution nette avant impôt sur les sociétés, apportée à l'équation du domaine ;
- l'investissement initial à financer.

Règles communes :
- les installations déjà comptées dans le budget du domaine (écuries, carrières, manège) ne sont pas
  recomptées : la contribution d'une pension est donc une contribution marginale ;
- les prix publics TTC sont convertis en HT avec le taux de TVA applicable (R3 § Q6) ;
- classe de revenu : A contractuel, B récurrent opérationnel, C occasionnel, D financier ou extérieur.
"""
from noyau import p

# ---------------------------------------------------------------------------------------------------
# Paramètres
# ---------------------------------------------------------------------------------------------------
G = "Moteurs — équestre"
p("eq_std_boxes", "Pension standard : boxes proposés en pension", 30, unite="boxes", groupe=G,
  note="Capacité excédentaire d'un domaine S2 (40 boxes, dont 8 pour les chevaux du propriétaire).")
p("eq_std_prix_ht", "Pension standard (box hébergement) : prix mensuel HT", 368, fav=401, dfv=334,
  unite="€ HT/mois", statut="SOURCÉ", sources="R6-02", groupe=G,
  note="Cas-types 2025 du Réseau Équin : 334 € HT (périurbain) et 401 € HT (compétition).")
p("eq_std_occ", "Pension standard : taux d'occupation", 0.85, fav=0.92, dfv=0.75, unite="%",
  statut="HYPOTHÈSE", sources="R6-16", groupe=G,
  note="Vacance moyenne de 5 places sur 30 à 35 en pension retraite (IFCE, 2019).")
p("eq_std_cout_var", "Pension standard : charges opérationnelles par cheval présent", 893, fav=847,
  dfv=1000, unite="€/cheval/an", statut="ESTIMATION", sources="R6-03", groupe=G,
  note="770 € en 2021 (Réseau Équin, pensions hébergement) × 1,16 d'inflation 2021-2026.")
p("eq_std_cout_fixe", "Pension standard : structure et travail par box (personnel compris)", 3018,
  fav=2862, dfv=3600, unite="€/box/an", statut="ESTIMATION", sources="R6-03; R6-02", groupe=G,
  note="(1 449 € de structure + 1 153 € de travail non salarié valorisé) × 1,16. Le travail est payé.")
p("eq_hdg_boxes", "Pension haut de gamme : boxes proposés en pension", 30, unite="boxes", groupe=G)
p("eq_hdg_prix_ht", "Pension haut de gamme : prix mensuel HT", 700, fav=874, dfv=450,
  unite="€ HT/mois", statut="ESTIMATION", sources="R6-15; R3-22", groupe=G,
  note="Haras de Jardy (10 km de Paris) : 922,50 € TTC, soit 874 € HT à 5,5 % (pension accessoire à "
       "la pratique de l'équitation). Valeur centrale abaissée pour un domaine à 1 h-1 h 30 d'une métropole. "
       "Demande haut de gamme hors Île-de-France : non prouvée. Le tarif publié ne précise pas l'unité de "
       "temps : unité mensuelle supposée (V2V).")
p("eq_hdg_occ", "Pension haut de gamme : taux d'occupation", 0.85, fav=0.92, dfv=0.70, unite="%",
  statut="HYPOTHÈSE", sources="R6-16", groupe=G)
p("eq_hdg_cout_var", "Pension haut de gamme : charges opérationnelles par cheval présent", 2238,
  fav=2122, dfv=2500, unite="€/cheval/an", statut="ESTIMATION", sources="R6-03", groupe=G,
  note="1 929 € en 2021 (pensions travail) × 1,16.")
p("eq_hdg_cout_fixe", "Pension haut de gamme : structure et travail par box", 4545, fav=4300, dfv=5300,
  unite="€/box/an", statut="ESTIMATION", sources="R6-03", groupe=G,
  note="(2 836 € de structure + 1 082 € de travail non salarié valorisé) × 1,16.")
p("eq_pro_boxes", "Écuries louées à un professionnel : boxes", 20, unite="boxes", groupe=G)
p("eq_pro_loyer_box", "Redevance annuelle par box louée à un professionnel", 600, fav=1176, dfv=0,
  unite="€/box/an", statut="ESTIMATION", sources="R6-25; R6-17", groupe=G,
  note="Plafond observé : 80 000 €/an pour 68 boxes à Paris (≈ 1 176 €/box). Rural : inconnu, moitié "
       "retenue. Défavorable = départ du locataire (Lamballe 2025). Risque de requalification en bail rural (R3).")
p("eq_pro_cout_box", "Écuries louées : charges résiduelles du bailleur par box", 150, fav=100, dfv=250,
  unite="€/box/an", statut="HYPOTHÈSE", groupe=G)
p("eq_ret_chevaux", "Pension retraite au pré : chevaux accueillis", 30, unite="chevaux", groupe=G)
p("eq_ret_prix_ht", "Pension retraite au pré : prix mensuel HT", 183, fav=220, dfv=150, unite="€ HT/mois",
  statut="ESTIMATION", sources="R6-16; R3-22", groupe=G,
  note="« Pré été / rentré hiver » 220 €/mois (IFCE 2019, TTC probable) ; TVA 20 % pour la pension retraite.")
p("eq_ret_occ", "Pension retraite : taux d'occupation", 0.85, fav=0.92, dfv=0.70, unite="%",
  statut="HYPOTHÈSE", sources="R6-16", groupe=G, note="22 000 places vacantes en France (2019).")
p("eq_ret_cout", "Pension retraite : coût par cheval présent (travail, foin d'hiver, clôtures, divers)",
  1800, fav=1500, dfv=2100, unite="€/cheval/an", statut="ESTIMATION", sources="R6-16; R2-21; R2-11",
  groupe=G, note="4,8 h de travail par cheval et par mois (IFCE) à ≈ 25 €/h chargé, plus ≈ 1 t de foin.")
p("repro_contrib", "Centre de reproduction (si vétérinaire et étalon disponibles) : contribution nette",
  21100, fav=30000, dfv=0, unite="€/an", statut="ESTIMATION", sources="R6-26", groupe=G,
  note="EBE 74 449 € (Haras du Rond Pré, 2022) moins 1,8 UMO d'exploitants valorisées. Astreinte de 6 mois.")

G = "Moteurs — événements et hébergement"
p("evt_nb", "Réceptions privées (mariages) par an, plafonnées", 10, fav=14, dfv=5, unite="événements",
  statut="HYPOTHÈSE", sources="R7-05; R7-06; R7-15", groupe=G,
  note="Plafond choisi pour la tranquillité. Concurrence : 1 382 lieux dans la catégorie « château » et "
       "3 769 dans la catégorie « domaine » de Mariages.net (catégories commerciales, pas un recensement, V2V) ; "
       "≈ 22 samedis de mai à septembre.")
p("evt_prix_ht", "Location du lieu pour une réception (week-end, traiteur extérieur)", 6500, fav=10000,
  dfv=4500, unite="€ HT/événement", statut="ESTIMATION", sources="R7-07; R7-09; R7-10; R7-13", groupe=G,
  note="Observés : 4 000 à 10 000 € par week-end (HT/TTC rarement précisé) ; CMN : 2 425 à 3 750 € HT.")
p("evt_var", "Réceptions : charges variables en % du CA (ménage, extras, énergie, commissions)", 0.30,
  fav=0.25, dfv=0.35, unite="%", statut="HYPOTHÈSE", groupe=G)
p("evt_fixe", "Réceptions : charges fixes (coordination 0,5 ETP, marketing, acoustique, assurance)",
  30000, fav=22000, dfv=40000, unite="€/an", statut="HYPOTHÈSE", sources="R3-52", groupe=G,
  note="Étude d'impact acoustique et limiteur probables si les réceptions sont habituelles.")
p("evt_capex", "Réceptions : salle ERP dans une grange (aménagement, sanitaires, parking, acoustique)",
  400000, fav=250000, dfv=600000, unite="€", statut="HYPOTHÈSE", sources="R4-52; R8-24; R3-38", groupe=G,
  note="Cas réel : plus de 100 000 € de mise aux normes ERP pour une salle de 98 m². Transformation "
       "d'une grange : ≈ 1 556 €/m² HT (logement).")
p("taux_renouv_capex", "Provision de renouvellement des investissements d'activité, en % par an", 0.025,
  fav=0.02, dfv=0.035, unite="% par an", statut="HYPOTHÈSE", groupe=G)
p("tourn_jours", "Tournages et prises de vue : jours par an", 2, fav=6, dfv=0, unite="jours",
  statut="HYPOTHÈSE", sources="R7-36; R7-37", groupe=G,
  note="Fréquence inconnue pour un château ordinaire ; plus de 50 % des tournages en Île-de-France.")
p("tourn_tarif", "Tournage : tarif journalier HT", 3500, fav=5500, dfv=2500, unite="€ HT/jour",
  statut="SOURCÉ", sources="R7-12", groupe=G,
  note="Grille du Centre des monuments nationaux (fiction), catégories B et C, prix plancher pour 12 h (V2V).")
p("tourn_var", "Tournages : charges variables", 0.15, unite="%", statut="HYPOTHÈSE", groupe=G)
p("semj_jours", "Séminaires de jour (journées d'étude) par an", 20, fav=40, dfv=0, unite="jours",
  statut="HYPOTHÈSE", sources="R7-74", groupe=G,
  note="Suppose une métropole à moins d'une heure ; 36 des 70 maisons du leader sont en Île-de-France.")
p("semj_pers", "Séminaires de jour : participants par journée", 20, fav=25, dfv=15, unite="personnes",
  statut="HYPOTHÈSE", groupe=G)
p("semj_prix", "Journée d'étude en château : prix par personne", 95, fav=100, dfv=85, unite="€ HT/pers.",
  statut="SOURCÉ", sources="R7-27; R7-28; R7-29", groupe=G)
p("semj_marge", "Séminaires de jour : marge après traiteur et personnel", 0.35, fav=0.45, dfv=0.25,
  unite="%", statut="HYPOTHÈSE", groupe=G)
p("gite_semaines", "Grande maison louée à la semaine : semaines louées par an", 23, fav=30, dfv=15,
  unite="semaines", statut="ESTIMATION", sources="R7-48; R7-50", groupe=G,
  note="Occupation annuelle des Gîtes de France : 44 à 47 %, soit ≈ 23 semaines.")
p("gite_prix_semaine", "Grande maison (12-15 personnes) : prix moyen par semaine", 3500, fav=6000,
  dfv=2500, unite="€ HT/semaine", statut="HYPOTHÈSE", groupe=G,
  note="Prix moyen inconnu (R7). À calibrer sur le marché local.")
p("gite_var", "Grande maison : charges variables (ménage, linge, commission, fluides)", 0.30, fav=0.25,
  dfv=0.35, unite="%", statut="HYPOTHÈSE", groupe=G)
p("gite_fixe", "Grande maison : charges fixes (entretien, mobilier, assurance)", 6000, fav=4000,
  dfv=9000, unite="€/an", statut="HYPOTHÈSE", groupe=G)
p("gite_capex", "Grande maison : rénovation d'une dépendance de 300 m²", 600000, fav=0, dfv=800000,
  unite="€ TTC", statut="ESTIMATION", sources="R8-24", groupe=G,
  note="≈ 2 000 €/m² TTC tout compris (cas réel 2022-2023). Favorable : maison déjà habitable.")
p("log_m2", "Logements locatifs créés dans les communs", 600, fav=800, dfv=400, unite="m²",
  statut="HYPOTHÈSE", groupe=G)
p("log_loyer_m2", "Loyer d'une maison en commune rurale, charges comprises", 8.0, fav=10.9, dfv=6.8,
  unite="€/m²/mois", statut="SOURCÉ", sources="R8-22; R8-23", groupe=G,
  note="Carte des loyers 2025 (ANIL, annonces) : 6,8 à 10,9 €/m²/mois couvre 75 % des communes ; médiane "
       "des communes regroupées (en général petites) : 8,63 €/m² (fichier complet relu par V2V). 8,0 reste prudent.")
p("log_vacance", "Logements : vacance", 0.05, fav=0.03, dfv=0.10, unite="%", statut="HYPOTHÈSE", groupe=G)
p("log_charges", "Logements : charges non récupérables, gestion, taxe foncière, entretien courant",
  0.20, fav=0.15, dfv=0.25, unite="% des loyers", statut="HYPOTHÈSE", groupe=G)
p("log_capex_m2", "Transformation de communs en logements", 1800, fav=1600, dfv=2200, unite="€ TTC/m²",
  statut="ESTIMATION", sources="R8-24", groupe=G)
p("stock_places", "Hivernage de camping-cars et caravanes (grange de 600 m²) : places", 20, fav=25, dfv=15,
  unite="places", statut="HYPOTHÈSE", groupe=G)
p("stock_prix", "Hivernage : prix annuel par place HT", 375, fav=460, dfv=290, unite="€ HT/an",
  statut="ESTIMATION", sources="R8-17", groupe=G, note="350 à 550 € TTC par an.")
p("stock_occ", "Hivernage : taux de remplissage", 0.80, fav=0.95, dfv=0.50, unite="%",
  statut="HYPOTHÈSE", groupe=G)
p("stock_capex", "Hivernage : aménagements (sol, portes, sécurité)", 20000, unite="€", statut="HYPOTHÈSE",
  groupe=G)
p("auto_places", "Gardiennage de voitures de collection (600 m²) : places", 18, unite="places",
  statut="HYPOTHÈSE", groupe=G)
p("auto_prix", "Gardiennage de voiture de collection : prix annuel HT", 2000, fav=2400, dfv=1500,
  unite="€ HT/an", statut="ESTIMATION", sources="R8-18", groupe=G,
  note="≈ 200 €/mois en Belgique (2026). Demande rurale française non démontrée.")
p("auto_occ", "Gardiennage de voitures : taux de remplissage", 0.60, fav=0.90, dfv=0.20, unite="%",
  statut="HYPOTHÈSE", groupe=G)
p("auto_fixe", "Gardiennage de voitures : sécurité, assurance du dépositaire, temps de présence", 12000,
  fav=9000, dfv=15000, unite="€/an", statut="HYPOTHÈSE", groupe=G)
p("auto_capex", "Gardiennage de voitures : alarme, vidéo, déshumidification, sol", 60000, unite="€",
  statut="HYPOTHÈSE", groupe=G)

G = "Moteurs — foncier, énergie"
p("pv_ha", "Solaire au sol ou agrivoltaïque hors champ de visibilité : surface louée", 5, fav=10, dfv=0,
  unite="ha", statut="HYPOTHÈSE", sources="R3-63; R3-44", groupe=G,
  note="Défavorable = refus (abords d'un MH : permis et accord de l'ABF dès 3 kW ; loi APER).")
p("pv_loyer_ha", "Loyer d'une centrale solaire au sol", 3000, fav=6000, dfv=1500, unite="€/ha/an",
  statut="ESTIMATION", sources="R8-01", groupe=G, note="1 500 à 6 000 €/ha/an : sources commerciales, fiabilité faible.")
p("bois_net_ha", "Forêt : revenu net des coupes", 75, fav=100, dfv=50, unite="€/ha/an",
  statut="HYPOTHÈSE", sources="R8-04; R8-05", groupe=G,
  note="Revenu net introuvable ; hypothèse de R8. Prix : forêt 4 950 €/ha, chêne −17 % en 2025.")

G = "Moteurs — bail d'ancrage et location de luxe (vague 2)"
p("anc_chambres", "Bail d'ancrage : chambres exploitées par un opérateur de séminaires résidentiels", 50,
  fav=60, dfv=0, unite="chambres", statut="HYPOTHÈSE", sources="V2A-13; V2A-54", groupe=G,
  note="Toutes les maisons Châteauform' en France ont au moins 40 chambres (médiane 61). S2 permettrait 40 à "
       "60 chambres en mobilisant l'essentiel des bâtiments (V2A § 4.3). Défavorable = conditions non réunies "
       "(plus de ≈ 90 km de Paris ou de 45 min d'une gare TGV, ou refus de cohabitation) : aucun exploitant.")
p("anc_ca_chambre", "Bail d'ancrage : chiffre d'affaires annuel de l'exploitant par chambre", 70000, fav=72400,
  dfv=68800, unite="€ HT/chambre/an", statut="ESTIMATION", sources="V2A-14; V2A-01", groupe=G,
  note="Château de Méry (70 chambres) : 72 400 € en 2024 ; campus Saint-Just (148 chambres) : 68 800 € en "
       "2025. Deux maisons proches de Paris, non transposables à une région éloignée.")
p("anc_taux_loyer", "Bail d'ancrage : loyer en % du chiffre d'affaires de l'exploitant", 0.10, fav=0.12,
  dfv=0.08, unite="%", statut="ESTIMATION", sources="V2A-29; V2A-31", groupe=G,
  note="Pratique hôtelière : 10-15 % du CA pour un indépendant ; plafond économique 8-14 % (couverture du "
       "loyer de 1,8 fois). V2A retient 8-15 % (central 12 %) ; ramené ici vers le bas parce que l'exploitant "
       "finance la transformation (abattement de 5 à 50 % selon les travaux, V2A § 7). Aucun loyer réel de "
       "château loué à un exploitant n'a été trouvé.")
p("anc_frais_bailleur", "Bail d'ancrage : frais du bailleur (gestion, juristes, assurance, impôts non refacturés)",
  0.10, fav=0.05, dfv=0.15, unite="% du loyer", statut="HYPOTHÈSE", groupe=G)
p("anc_part_transferee", "Bail d'ancrage : part de l'énergie et de l'entretien courant du bâti reprise par l'exploitant",
  0.25, fav=0.40, dfv=0.0, unite="%", statut="HYPOTHÈSE", sources="V2A-38", groupe=G,
  note="Dans un bail commercial, l'entretien courant et les fluides de la zone louée sont au preneur ; les "
       "grosses réparations (toiture, murs porteurs) restent toujours au bailleur.")
p("lux_semaines", "Location de luxe de la partie privée : semaines louées par an", 3, fav=6, dfv=2,
  unite="semaines", statut="HYPOTHÈSE", sources="V2D-26; V2D-28", groupe=G,
  note="Aucun chiffre réel trouvé. Le Collectionist : ≈ 2 réservations par propriété et par an ; Oliver's "
       "Travels exige 6 semaines disponibles en juillet-août. Le propriétaire doit quitter les lieux.")
p("lux_prix_semaine", "Location de luxe : prix d'une semaine (château de 10 à 14 chambres)", 30000, fav=45000,
  dfv=20000, unite="€/semaine", statut="ESTIMATION", sources="V2D-35; V2D-36; V2D-37; V2D-38; V2D-25", groupe=G,
  note="Prix publiés : 12 755 à 46 860 € par semaine pour 8 à 14 chambres ; prix moyen de la plateforme ≈ "
       "25 000 € (2020). Régime de TVA non précisé : montant traité comme hors taxe.")
p("lux_commission", "Location de luxe : commission de la plateforme", 0.22, fav=0.20, dfv=0.22, unite="%",
  statut="SOURCÉ", sources="V2D-24; V2D-25", groupe=G, note="Le Collectionist : 20 % (2017), 22 % (2020).")
p("lux_var", "Location de luxe : charges variables (ménage, gardien, linge, fluides, usure)", 0.15, fav=0.10,
  dfv=0.20, unite="%", statut="HYPOTHÈSE", sources="V2D-24", groupe=G,
  note="Les services compris dans le prix (ménage, jardiniers) sont fournis par le propriétaire.")
p("lux_fixe", "Location de luxe : charges fixes (assurance RC, comptabilité au réel, entretien de la piscine)",
  10000, fav=5000, dfv=20000, unite="€/an", statut="HYPOTHÈSE", sources="V2D-28; V2D-32", groupe=G)
p("lux_capex", "Location de luxe : mise aux standards (piscine, une salle de bains par chambre)", 300000,
  fav=100000, dfv=600000, unite="€", statut="HYPOTHÈSE", sources="V2D-40; V2D-41", groupe=G,
  note="Exigences observées : piscine dans tous les châteaux de la plateforme, 0,75 à 1 salle de bains par "
       "chambre. Coût INCONNU (V2D) : ordre de grandeur à remplacer par des devis.")

G = "Moteurs — extérieurs"
p("dot_taux_net", "Dotation financière : taux de retrait réel net d'impôt soutenable", 0.0275,
  fav=0.03, dfv=0.025, unite="% du capital", statut="ESTIMATION", sources="R8-31; R8-32; R8-34", groupe=G,
  note="Dotations américaines (exonérées) : 4,9 % ; actions mondiales : 3,5 % réel par an depuis 2000 ; "
       "fiscalité française de 31,4 % sur les revenus nominaux. Fourchette de R8 : 2,5 à 3 %.")
p("ent_conversion", "Entreprise extérieure : dividende net par euro d'EBITDA", 0.396, fav=0.45, dfv=0.33,
  unite="€/€", statut="ESTIMATION", sources="R3-16; R3-20; R8-35", groupe=G,
  note="EBITDA → résultat avant impôt ≈ 0,77 (hypothèse de R8) × (1 − IS 25 %) × (1 − PFU 31,4 %).")

G = "Moteurs — château-hôtel"
p("hot_chambres", "Château-hôtel : nombre de chambres", 15, unite="chambres", statut="HYPOTHÈSE", groupe=G)
p("hot_revpar", "Château-hôtel : revenu par chambre disponible (RevPAR) HT", 130, fav=184, dfv=102,
  unite="€ HT/nuit", statut="SOURCÉ", sources="R7-38", groupe=G,
  note="Haut de gamme 2025 : Indre-et-Loire 102 €, Gironde 146 €, Calvados 184 €.")
p("hot_autres_recettes", "Château-hôtel : autres recettes (restauration, événements) en % de l'hébergement",
  0.6, fav=0.9, dfv=0.4, unite="%", statut="HYPOTHÈSE", groupe=G)
p("hot_etp_chambre", "Château-hôtel : salariés par chambre", 1.65, fav=1.2, dfv=1.9,
  unite="personnes/chambre", statut="ESTIMATION", sources="R7-41; V2V-30", groupe=G,
  note="Cas Louise de La Vallière : effectif projeté à l'ouverture de 33 personnes, dont 19 en cuisine, "
       "restaurant et bar (V2V). Sans restaurant, l'ordre de grandeur serait d'environ 0,7.")
p("hot_cout_etp", "Château-hôtel : coût employeur moyen par ETP", 38000, fav=34000, dfv=42000,
  unite="€/ETP/an", statut="ESTIMATION", sources="R2-11", groupe=G, note="≈ 1,25 à 1,4 SMIC chargé.")
p("hot_autres_charges", "Château-hôtel : autres charges d'exploitation en % du CA", 0.35, fav=0.30, dfv=0.40,
  unite="%", statut="HYPOTHÈSE", groupe=G)
p("hot_capex_chambre", "Château-hôtel : investissement par chambre", 500000, fav=350000, dfv=700000,
  unite="€/chambre", statut="SOURCÉ", sources="R7-41; R7-42; R7-43", groupe=G,
  note="Hors prix d'achat (≈ 750 000 €/chambre en l'incluant) ; restaurant, spa, piscine et parc compris (V2V).")

# ---------------------------------------------------------------------------------------------------
# Lignes : (id, libellé, gabarit, catégorie, TVA, nature). Catégorie = code du moteur.
# ---------------------------------------------------------------------------------------------------
LIGNES = [
    # Pension standard
    ("eq_std_ca", "Pension standard — CA HT", "eq_std_boxes{C}*eq_std_occ{C}*12*eq_std_prix_ht{C}", "EQ_STD", 0, "F"),
    ("eq_std_ch", "Pension standard — charges", "eq_std_boxes{C}*eq_std_occ{C}*eq_std_cout_var{C}+eq_std_boxes{C}*eq_std_cout_fixe{C}", "EQ_STD", 0, "F"),
    ("eq_std_cn", "Pension standard — CONTRIBUTION NETTE", "[eq_std_ca]-[eq_std_ch]", "EQ_STD", 0, "S"),
    # Pension haut de gamme
    ("eq_hdg_ca", "Pension haut de gamme — CA HT", "eq_hdg_boxes{C}*eq_hdg_occ{C}*12*eq_hdg_prix_ht{C}", "EQ_HDG", 0, "F"),
    ("eq_hdg_ch", "Pension haut de gamme — charges", "eq_hdg_boxes{C}*eq_hdg_occ{C}*eq_hdg_cout_var{C}+eq_hdg_boxes{C}*eq_hdg_cout_fixe{C}", "EQ_HDG", 0, "F"),
    ("eq_hdg_cn", "Pension haut de gamme — CONTRIBUTION NETTE", "[eq_hdg_ca]-[eq_hdg_ch]", "EQ_HDG", 0, "S"),
    # Écuries louées
    ("eq_pro_ca", "Écuries louées à un professionnel — redevances", "eq_pro_boxes{C}*eq_pro_loyer_box{C}", "EQ_PRO", 0, "F"),
    ("eq_pro_cn", "Écuries louées — CONTRIBUTION NETTE", "[eq_pro_ca]-eq_pro_boxes{C}*eq_pro_cout_box{C}", "EQ_PRO", 0, "S"),
    # Pension retraite
    ("eq_ret_ca", "Pension retraite au pré — CA HT", "eq_ret_chevaux{C}*eq_ret_occ{C}*12*eq_ret_prix_ht{C}", "EQ_RET", 0, "F"),
    ("eq_ret_cn", "Pension retraite — CONTRIBUTION NETTE", "[eq_ret_ca]-eq_ret_chevaux{C}*eq_ret_occ{C}*eq_ret_cout{C}", "EQ_RET", 0, "S"),
    # Reproduction
    ("repro_cn", "Centre de reproduction — CONTRIBUTION NETTE (si vétérinaire et étalon)", "repro_contrib{C}", "REPRO", 0, "S"),
    # Réceptions
    ("evt_ca", "Réceptions privées — CA HT", "evt_nb{C}*evt_prix_ht{C}", "EVT", 0, "F"),
    ("evt_ch", "Réceptions — charges (variables + fixes)", "[evt_ca]*evt_var{C}+evt_fixe{C}", "EVT", 0, "F"),
    ("evt_rv", "Réceptions — provision de renouvellement de la salle", "evt_capex{C}*taux_renouv_capex{C}", "EVT", 0, "P"),
    ("evt_cn", "Réceptions — CONTRIBUTION NETTE", "[evt_ca]-[evt_ch]-[evt_rv]", "EVT", 0, "S"),
    ("evt_inv", "Réceptions — investissement initial (salle ERP)", "evt_capex{C}", "EVT", 0, "S"),
    # Tournages
    ("tourn_cn", "Tournages et prises de vue — CONTRIBUTION NETTE", "tourn_jours{C}*tourn_tarif{C}*(1-tourn_var{C})", "TOURN", 0, "S"),
    # Séminaires de jour
    ("semj_ca", "Séminaires de jour — CA HT", "semj_jours{C}*semj_pers{C}*semj_prix{C}", "SEMJ", 0, "F"),
    ("semj_cn", "Séminaires de jour — CONTRIBUTION NETTE", "[semj_ca]*semj_marge{C}", "SEMJ", 0, "S"),
    # Grande maison à la semaine
    ("gite_ca", "Grande maison à la semaine — CA HT", "gite_semaines{C}*gite_prix_semaine{C}", "GITE", 0, "F"),
    ("gite_cn", "Grande maison — CONTRIBUTION NETTE",
     "[gite_ca]*(1-gite_var{C})-gite_fixe{C}-gite_capex{C}*taux_renouv_capex{C}", "GITE", 0, "S"),
    ("gite_inv", "Grande maison — investissement initial", "gite_capex{C}", "GITE", 0, "S"),
    # Logements locatifs
    ("log_ca", "Logements locatifs — loyers annuels", "log_m2{C}*log_loyer_m2{C}*12*(1-log_vacance{C})", "LOG", 0, "F"),
    ("log_cn", "Logements locatifs — CONTRIBUTION NETTE",
     "[log_ca]*(1-log_charges{C})-log_m2{C}*log_capex_m2{C}*0.01", "LOG", 0, "S"),
    ("log_inv", "Logements locatifs — investissement initial", "log_m2{C}*log_capex_m2{C}", "LOG", 0, "S"),
    ("log_rdt", "Logements locatifs — rendement net sur investissement", "[log_cn]/[log_inv]", "LOG", 0, "S"),
    # Stockage
    ("stock_cn", "Hivernage de véhicules — CONTRIBUTION NETTE",
     "stock_places{C}*stock_occ{C}*stock_prix{C}*0.85-stock_capex{C}*taux_renouv_capex{C}", "STOCK", 0, "S"),
    ("auto_cn", "Gardiennage de voitures de collection — CONTRIBUTION NETTE",
     "auto_places{C}*auto_occ{C}*auto_prix{C}-auto_fixe{C}-auto_capex{C}*taux_renouv_capex{C}", "AUTO", 0, "S"),
    # Foncier
    ("pv_cn", "Bail solaire — CONTRIBUTION NETTE", "pv_ha{C}*pv_loyer_ha{C}", "PV", 0, "S"),
    ("bois_cn", "Forêt (S2, 30 ha) — CONTRIBUTION NETTE", "S2_ha_bois*bois_net_ha{C}", "BOIS", 0, "S"),
    # Château-hôtel
    ("hot_ca", "Château-hôtel (15 chambres) — CA HT",
     "hot_chambres{C}*365*hot_revpar{C}*(1+hot_autres_recettes{C})", "HOTEL", 0, "F"),
    ("hot_ch", "Château-hôtel — charges (personnel + autres)",
     "hot_chambres{C}*hot_etp_chambre{C}*hot_cout_etp{C}+[hot_ca]*hot_autres_charges{C}", "HOTEL", 0, "F"),
    ("hot_rv", "Château-hôtel — provision de renouvellement",
     "hot_chambres{C}*hot_capex_chambre{C}*taux_renouv_capex{C}", "HOTEL", 0, "P"),
    ("hot_cn", "Château-hôtel — CONTRIBUTION NETTE", "[hot_ca]-[hot_ch]-[hot_rv]", "HOTEL", 0, "S"),
    ("hot_inv", "Château-hôtel — investissement initial", "hot_chambres{C}*hot_capex_chambre{C}", "HOTEL", 0, "S"),
    # Bail d'ancrage (vague 2, V2A)
    ("anc_loyer", "Bail d'ancrage — loyer brut versé par l'exploitant",
     "anc_chambres{C}*anc_ca_chambre{C}*anc_taux_loyer{C}", "ANC", 0, "F"),
    ("anc_eco", "Bail d'ancrage — charges du domaine reprises par l'exploitant",
     "anc_part_transferee{C}*(bud_chauffage_S2{C}+bud_hors_gel_S2{C}+bud_electricite_S2{C}+bud_bati_courant_S2{C})",
     "ANC", 0, "F"),
    ("anc_cn", "Bail d'ancrage — CONTRIBUTION NETTE (si localisation et taille le permettent)",
     "[anc_loyer]*(1-anc_frais_bailleur{C})+[anc_eco]", "ANC", 0, "S"),
    # Location de luxe de la partie privée (vague 2, V2D)
    ("lux_ca", "Location de luxe — recettes brutes", "lux_semaines{C}*lux_prix_semaine{C}", "LUX", 0, "F"),
    ("lux_cn", "Location de luxe — CONTRIBUTION NETTE",
     "[lux_ca]*(1-lux_commission{C}-lux_var{C})-lux_fixe{C}-lux_capex{C}*taux_renouv_capex{C}", "LUX", 0, "S"),
    # Extérieurs (par million d'euros)
    ("dot_cn_par_m", "Dotation financière — revenu net par million € de capital", "1000000*dot_taux_net{C}", "DOT", 0, "S"),
    ("ent_cn_par_m", "Entreprise extérieure — dividende net par million € d'EBITDA", "1000000*ent_conversion{C}", "ENT", 0, "S"),
]


def ecrire(wb):
    from excel_outils import ecrire_tableau_gabarits
    colonnes = [("Favorable", None, "fav"), ("Central", None, "cen"), ("Défavorable", None, "def")]
    _, controle = ecrire_tableau_gabarits(
        wb, "Moteurs", "MOTEURS DE REVENUS — économie unitaire à l'échelle d'un domaine S2 (€ 2026 HT, par an)",
        LIGNES, colonnes, prefixe_noms="mot_",
        note=("Contribution nette = chiffre d'affaires HT − charges propres (personnel compris) − provision de "
              "renouvellement des investissements propres, avant impôt sur les sociétés. Les installations déjà "
              "financées par le budget du domaine (écuries, manège) ne sont pas recomptées. Classe : voir la "
              "feuille Modeles."))
    return controle
