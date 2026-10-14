"""Lignes du budget annuel de fonctionnement des domaines types S1, S2 et S3.

Chaque ligne est un gabarit, dont la syntaxe est définie dans noyau.py.
Montants en € 2026, TTC pour un propriétaire particulier, qui ne récupère pas la TVA.
La colonne `tva` donne le taux de TVA moyen contenu dans la ligne. Elle sert à la vue
« portée par une société assujettie », dans laquelle cette TVA devient récupérable.

Méthode du bâti (voir 01_RECHERCHE/R1, § 9) :
- entretien et réparation = valeur de reconstruction × taux annuel ;
- règle de 2 à 4 % par an du National Research Council [R1-07, R1-08] ;
- valeurs de reconstruction : 2 400 €/m² (Figaro 2020) [R1-26] et 5 000 à 10 000 €/m² (courtier 2026) [R1-27].
"""

# (id, libellé, gabarit, catégorie, taux de TVA contenu, nature)
# nature : "F" = charge de fonctionnement ; "P" = provision (gros entretien, renouvellement) ;
#          "S" = sous-total, total ou indicateur
LIGNES = [
    # --- Base de calcul --------------------------------------------------------
    ("valeur_reconstruction", "Valeur de reconstruction à l'identique (château + dépendances), base de calcul",
     "{S}_surf_chateau*{S}_vr_m2{C}+{S}_surf_dep*{S}_vr_m2{C}*vr_dep_ratio{C}", "Base", 0.0, "S"),
    # --- A. Bâti -------------------------------------------------------------
    ("bati_courant", "Entretien courant du bâti (petites réparations, contrats, contrôles)",
     "[valeur_reconstruction]*taux_entretien_courant{C}", "A. Bâti", 0.10, "F"),
    ("bati_ge", "Provision de gros entretien et de conservation (campagnes de toiture, maçonnerie, menuiseries, réseaux)",
     "[valeur_reconstruction]*taux_gros_entretien{C}", "A. Bâti", 0.10, "P"),
    ("imprevus_travaux", "Aléas de chantier et découvertes (en % du gros entretien)",
     "[bati_ge]*taux_aleas_travaux{C}", "A. Bâti", 0.10, "P"),
    ("securite", "Sécurité : alarme, télésurveillance, protection incendie",
     "{S}_securite{C}", "A. Bâti", 0.20, "F"),
    # --- B. Personnel ----------------------------------------------------------
    ("pers_direction", "Personnel : régisseur ou directeur de domaine",
     "{S}_etp_direction*cout_direction{C}", "B. Personnel", 0.0, "F"),
    ("pers_jardins", "Personnel : jardiniers (chef jardinier compris)",
     "{S}_etp_jardin*cout_jardinier{C}", "B. Personnel", 0.0, "F"),
    ("pers_entretien", "Personnel : agents d'entretien et de maintenance",
     "{S}_etp_entretien*cout_agent_entretien{C}", "B. Personnel", 0.0, "F"),
    ("pers_maison", "Personnel : maison (gouvernante, employés de maison)",
     "{S}_etp_maison*cout_maison{C}", "B. Personnel", 0.0, "F"),
    ("pers_equestre", "Personnel : écurie (soigneurs, responsable d'écurie)",
     "{S}_etp_equestre*cout_soigneur{C}", "B. Personnel", 0.0, "F"),
    ("pers_gardien", "Personnel : gardiennage",
     "{S}_etp_gardien*cout_gardien{C}", "B. Personnel", 0.0, "F"),
    ("pers_admin", "Personnel : administration et comptabilité internes",
     "{S}_etp_admin*cout_admin{C}", "B. Personnel", 0.0, "F"),
    # --- C. Jardins, parc et terres (hors personnel) ---------------------------
    ("jardins_reguliers", "Jardins réguliers et potager : fournitures, végétaux, sous-traitance",
     "{S}_ha_jardins*jardin_ha{C}", "C. Jardins et terres", 0.20, "F"),
    ("parc", "Parc paysager : fournitures, fauche, élagage et replantation",
     "{S}_ha_parc*parc_ha{C}", "C. Jardins et terres", 0.20, "F"),
    ("prairies", "Prairies et paddocks : entretien, amendements, fauche",
     "{S}_ha_prairies*prairie_ha{C}", "C. Jardins et terres", 0.20, "F"),
    ("clotures", "Clôtures : provision de renouvellement",
     "{S}_ml_clotures*cloture_ml{C}/cloture_vie{C}", "C. Jardins et terres", 0.20, "P"),
    ("bois", "Bois : gestion courante (hors recettes de coupe)",
     "{S}_ha_bois*bois_cout_ha{C}", "C. Jardins et terres", 0.20, "F"),
    # --- D. Équipements --------------------------------------------------------
    ("equip_renouv", "Équipements : renouvellement (tracteurs, tondeuses, véhicules, camion)",
     "{S}_valeur_equip/equip_vie{C}", "D. Équipements", 0.20, "P"),
    ("equip_entretien", "Équipements : entretien et carburant",
     "{S}_valeur_equip*equip_entretien_taux{C}", "D. Équipements", 0.20, "F"),
    # --- E. Chevaux et installations ------------------------------------------
    ("chevaux", "Chevaux du propriétaire : alimentation, litière, maréchal, vétérinaire, assurance (hors personnel)",
     "{S}_nb_chevaux*cheval_an{C}", "E. Chevaux", 0.20, "F"),
    ("installations_eq", "Installations équestres : sols, boxes, bâtiment du manège (provision)",
     "{S}_surf_pistes*sol_cout_m2{C}/sol_vie{C}+{S}_nb_boxes*box_entretien{C}"
     "+{S}_surf_manege*manege_cout_m2{C}/manege_vie{C}", "E. Chevaux", 0.20, "P"),
    # --- F. Énergie et eau -------------------------------------------------------
    ("chauffage", "Chauffage et eau chaude des surfaces habitées",
     "{S}_surf_chauffee{C}*chauffage_kwh_m2{C}*prix_chaleur_kwh{C}", "F. Énergie", 0.20, "F"),
    ("hors_gel", "Hors-gel et tempérage des surfaces non habitées du château",
     "MAX(0,{S}_surf_chateau-{S}_surf_chauffee{C})*horsgel_kwh_m2{C}*prix_chaleur_kwh{C}",
     "F. Énergie", 0.20, "F"),
    ("electricite", "Électricité spécifique (éclairage, pompes, écuries, ateliers, extérieurs)",
     "{S}_elec_kwh{C}*prix_elec_kwh{C}", "F. Énergie", 0.20, "F"),
    ("eau", "Eau et assainissement", "{S}_eau{C}", "F. Énergie", 0.10, "F"),
    # --- G. Assurances ---------------------------------------------------------
    ("assurance_bati", "Assurance des bâtiments (en ‰ de la valeur de reconstruction)",
     "[valeur_reconstruction]*assurance_taux{C}", "G. Assurances", 0.0, "F"),
    ("assurance_autres", "Responsabilité civile, véhicules, chevaux, contenu",
     "{S}_assurances_autres{C}", "G. Assurances", 0.0, "F"),
    # --- H. Impôts et taxes ----------------------------------------------------
    ("taxe_fonciere_bati", "Taxe foncière sur les propriétés bâties",
     "{S}_surf_chateau*tf_chateau_m2{C}+{S}_surf_dep*tf_dep_m2{C}", "H. Impôts et taxes", 0.0, "F"),
    ("taxe_fonciere_non_bati", "Taxe foncière sur les propriétés non bâties",
     "({S}_ha_prairies+{S}_ha_bois+{S}_ha_parc+{S}_ha_jardins)*tfnb_ha{C}", "H. Impôts et taxes", 0.0, "F"),
    # --- I. Administration -----------------------------------------------------
    ("admin", "Administration : expert-comptable, juridique, banque, informatique, télécoms",
     "{S}_admin{C}", "I. Administration", 0.20, "F"),
    ("honoraires_patrimoine", "Architecte du patrimoine : état sanitaire et suivi (hors maîtrise d'œuvre des chantiers)",
     "{S}_honoraires_patrimoine{C}", "I. Administration", 0.20, "F"),
    # --- Sous-totaux -------------------------------------------------------------
    ("st_fonctionnement", "Sous-total des charges de fonctionnement",
     "[bati_courant]+[securite]+[pers_direction]+[pers_jardins]+[pers_entretien]+[pers_maison]"
     "+[pers_equestre]+[pers_gardien]+[pers_admin]+[jardins_reguliers]+[parc]+[prairies]"
     "+[bois]+[equip_entretien]+[chevaux]+[chauffage]+[hors_gel]+[electricite]+[eau]"
     "+[assurance_bati]+[assurance_autres]+[taxe_fonciere_bati]+[taxe_fonciere_non_bati]+[admin]"
     "+[honoraires_patrimoine]",
     "Totaux", 0.0, "S"),
    ("st_provisions", "Sous-total des provisions (gros entretien, aléas de chantier, renouvellements)",
     "[bati_ge]+[imprevus_travaux]+[clotures]+[equip_renouv]+[installations_eq]", "Totaux", 0.0, "S"),
    # --- J. Imprévus et K. Investissements futurs -----------------------------------------------
    ("imprevus", "Imprévus d'exploitation (en % des charges de fonctionnement)",
     "[st_fonctionnement]*taux_imprevus{C}", "J. Imprévus", 0.0, "F"),
    ("invest_futurs", "Investissements futurs : améliorations, mises aux normes, embellissements",
     "([st_fonctionnement]+[st_provisions])*taux_invest_futurs{C}", "K. Investissements futurs", 0.10, "P"),
    ("total_besoin", "BESOIN ANNUEL DE TRÉSORERIE DU DOMAINE (hors dette, hors activités)",
     "[st_fonctionnement]+[st_provisions]+[imprevus]+[invest_futurs]", "Totaux", 0.0, "S"),
    # --- Indicateurs ----------------------------------------------------------------------------------
    ("dont_personnel", "dont personnel",
     "[pers_direction]+[pers_jardins]+[pers_entretien]+[pers_maison]+[pers_equestre]+[pers_gardien]+[pers_admin]",
     "Indicateurs", 0.0, "S"),
    ("dont_bati", "dont bâti (entretien courant, gros entretien, aléas, assurance, taxe foncière bâtie, sécurité)",
     "[bati_courant]+[bati_ge]+[imprevus_travaux]+[assurance_bati]+[taxe_fonciere_bati]+[securite]",
     "Indicateurs", 0.0, "S"),
    ("part_personnel", "Part du personnel dans le besoin total",
     "[dont_personnel]/[total_besoin]", "Indicateurs", 0.0, "S"),
    ("part_bati", "Part du bâti dans le besoin total",
     "[dont_bati]/[total_besoin]", "Indicateurs", 0.0, "S"),
    ("besoin_ht_societe", "Besoin si les charges sont portées par une société assujettie (TVA récupérée, ordre de grandeur)",
     "[total_besoin]-([bati_courant]+[bati_ge]+[imprevus_travaux]+[eau]+[invest_futurs])*0.1/1.1"
     "-([securite]+[jardins_reguliers]+[parc]+[prairies]+[clotures]+[bois]+[equip_renouv]+[equip_entretien]"
     "+[chevaux]+[installations_eq]+[chauffage]+[hors_gel]+[electricite]+[admin]+[honoraires_patrimoine])*0.2/1.2",
     "Indicateurs", 0.0, "S"),
    ("besoin_par_m2", "Besoin total par m² de plancher bâti (château + dépendances), en €/m²",
     "[total_besoin]/({S}_surf_chateau+{S}_surf_dep)", "Indicateurs", 0.0, "S"),
    ("besoin_en_pct_valeur", "Besoin annuel en % de la valeur de reconstruction",
     "[total_besoin]/[valeur_reconstruction]", "Indicateurs", 0.0, "S"),
    # --- Scénario complémentaire : dette -------------------------------------------------------------
    ("dette_annuite", "Scénario complémentaire : annuité d'une dette d'acquisition",
     "-PMT(dette_taux{C},dette_duree{C},{S}_prix_achat*dette_quotite{C})", "Scénario dette", 0.0, "S"),
    ("total_avec_dette", "BESOIN ANNUEL AVEC DETTE D'ACQUISITION (scénario complémentaire)",
     "[total_besoin]+[dette_annuite]", "Scénario dette", 0.0, "S"),
]
