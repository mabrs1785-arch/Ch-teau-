"""Lignes du budget annuel de fonctionnement des domaines types S1, S2 et S3.

Chaque ligne est un gabarit, avec la syntaxe définie dans noyau.py.
Les montants sont en € 2026, TTC pour un propriétaire particulier, qui ne récupère pas la TVA.
La colonne `tva` donne le taux de TVA contenu dans la ligne. Elle sert à calculer la vue
« portée par une société assujettie », où cette TVA devient récupérable.

Les catégories suivent la liste du brief :
- entretien courant et exceptionnel des bâtiments ;
- conservation ;
- personnel ;
- jardins et terres ;
- énergie et assurances ;
- équipements ;
- chevaux et installations ;
- impôts et taxes ;
- administration ;
- imprévus ;
- investissements futurs.
"""

# (id, libellé, gabarit, catégorie, taux de TVA contenu, nature)
# nature : "F" = charge de fonctionnement, "P" = provision (gros entretien, renouvellement),
#          "S" = sous-total ou total (pas de TVA propre)
LIGNES = [
    # --- A. Bâti -------------------------------------------------------------
    ("bati_courant", "Entretien courant du bâti (contrats, petites réparations, contrôles)",
     "({S}_surf_chateau+{S}_surf_dep)*bati_courant_m2{C}", "A. Bâti", 0.10, "F"),
    ("bati_ge_composants", "Provision de gros entretien — méthode des composants",
     "({S}_surf_toits*toit_cout_m2{C}/toit_vie{C}"
     "+{S}_surf_facades*facade_cout_m2{C}/facade_vie{C}"
     "+{S}_nb_baies*baie_cout{C}/baie_vie{C}"
     "+({S}_surf_chateau+{S}_surf_dep)*reseaux_cout_m2{C}/reseaux_vie{C}"
     "+{S}_surf_chateau*interieurs_cout_m2{C}/interieurs_vie{C})*{S}_coef_patrimoine{C}",
     "A. Bâti", 0.10, "P"),
    ("bati_ge_ratio", "Provision de gros entretien — méthode du ratio de la valeur de restauration (contrôle)",
     "({S}_surf_chateau*restau_m2_chateau{C}+{S}_surf_dep*restau_m2_dep{C})*taux_ge_annuel{C}",
     "A. Bâti", 0.10, "S"),
    ("bati_ge", "Provision de gros entretien retenue (la plus élevée des deux méthodes)",
     "MAX([bati_ge_composants],[bati_ge_ratio])", "A. Bâti", 0.10, "P"),
    ("securite", "Sécurité : alarme, télésurveillance, protection incendie",
     "{S}_securite{C}", "A. Bâti", 0.20, "F"),
    # --- B. Personnel ----------------------------------------------------------
    ("pers_direction", "Personnel : régisseur ou directeur de domaine",
     "{S}_etp_direction*cout_direction{C}", "B. Personnel", 0.0, "F"),
    ("pers_jardins", "Personnel : jardiniers (chef jardinier compris)",
     "{S}_etp_jardin*cout_jardinier{C}", "B. Personnel", 0.0, "F"),
    ("pers_entretien", "Personnel : agents d'entretien et de maintenance",
     "{S}_etp_entretien*cout_agent_entretien{C}", "B. Personnel", 0.0, "F"),
    ("pers_maison", "Personnel : maison (gouvernante, employés de maison, majordome)",
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
    ("parc", "Parc paysager : fournitures, fauche, sous-traitance",
     "{S}_ha_parc*parc_ha{C}", "C. Jardins et terres", 0.20, "F"),
    ("arbres", "Arbres : élagage, abattage, replantation",
     "{S}_ha_parc*arbres_ha{C}", "C. Jardins et terres", 0.20, "F"),
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
    ("chevaux", "Chevaux du propriétaire : alimentation, litière, maréchal, vétérinaire, assurance",
     "{S}_nb_chevaux*cheval_an{C}", "E. Chevaux", 0.20, "F"),
    ("installations_eq", "Installations équestres : sols, boxes, manège (provision)",
     "{S}_surf_pistes*sol_cout_m2{C}/sol_vie{C}+{S}_nb_boxes*box_entretien{C}"
     "+{S}_surf_manege*manege_cout_m2{C}/manege_vie{C}", "E. Chevaux", 0.20, "P"),
    # --- F. Énergie et eau -------------------------------------------------------
    ("chauffage", "Chauffage des surfaces habitées",
     "{S}_surf_chauffee*chauffage_kwh_m2{C}*prix_chaleur_kwh{C}", "F. Énergie", 0.20, "F"),
    ("hors_gel", "Hors-gel et tempérage des surfaces non habitées",
     "MAX(0,{S}_surf_chateau-{S}_surf_chauffee)*horsgel_kwh_m2{C}*prix_chaleur_kwh{C}",
     "F. Énergie", 0.20, "F"),
    ("electricite", "Électricité spécifique (éclairage, pompes, écuries, ateliers)",
     "{S}_elec_kwh*prix_elec_kwh{C}", "F. Énergie", 0.20, "F"),
    ("eau", "Eau et assainissement", "{S}_eau{C}", "F. Énergie", 0.10, "F"),
    # --- G. Assurances ---------------------------------------------------------
    ("assurance_bati", "Assurance multirisque des bâtiments et du contenu",
     "{S}_valeur_assuree*assurance_taux{C}", "G. Assurances", 0.0, "F"),
    ("assurance_autres", "Responsabilité civile, véhicules, chevaux",
     "{S}_assurances_autres{C}", "G. Assurances", 0.0, "F"),
    # --- H. Impôts et taxes ----------------------------------------------------
    ("taxe_fonciere", "Taxe foncière (bâti et non bâti)",
     "{S}_taxe_fonciere{C}", "H. Impôts et taxes", 0.0, "F"),
    # --- I. Administration -----------------------------------------------------
    ("admin", "Administration : expert-comptable, juridique, banque, informatique, télécoms",
     "{S}_admin{C}", "I. Administration", 0.20, "F"),
    ("honoraires_patrimoine", "Architecte du patrimoine : diagnostics et suivi annuel",
     "{S}_honoraires_patrimoine{C}", "I. Administration", 0.20, "F"),
    # --- Sous-totaux -------------------------------------------------------------
    ("st_fonctionnement", "Sous-total des charges de fonctionnement",
     "[bati_courant]+[securite]+[pers_direction]+[pers_jardins]+[pers_entretien]+[pers_maison]"
     "+[pers_equestre]+[pers_gardien]+[pers_admin]+[jardins_reguliers]+[parc]+[arbres]+[prairies]"
     "+[bois]+[equip_entretien]+[chevaux]+[chauffage]+[hors_gel]+[electricite]+[eau]"
     "+[assurance_bati]+[assurance_autres]+[taxe_fonciere]+[admin]+[honoraires_patrimoine]",
     "Totaux", 0.0, "S"),
    ("st_provisions", "Sous-total des provisions (gros entretien et renouvellements)",
     "[bati_ge]+[clotures]+[equip_renouv]+[installations_eq]", "Totaux", 0.0, "S"),
    # --- J. Imprévus et K. Investissements futurs -----------------------------------------------
    ("imprevus", "Imprévus (pourcentage des charges et provisions)",
     "([st_fonctionnement]+[st_provisions])*taux_imprevus{C}", "J. Imprévus", 0.0, "F"),
    ("invest_futurs", "Investissements futurs : améliorations et mises aux normes",
     "([st_fonctionnement]+[st_provisions])*taux_invest_futurs{C}", "K. Investissements futurs", 0.10, "P"),
    ("total_besoin", "BESOIN ANNUEL DE TRÉSORERIE (hors dette)",
     "[st_fonctionnement]+[st_provisions]+[imprevus]+[invest_futurs]", "Totaux", 0.0, "S"),
    ("dont_personnel", "dont personnel",
     "[pers_direction]+[pers_jardins]+[pers_entretien]+[pers_maison]+[pers_equestre]+[pers_gardien]+[pers_admin]",
     "Indicateurs", 0.0, "S"),
    ("part_personnel", "Part du personnel dans le besoin total",
     "[dont_personnel]/[total_besoin]", "Indicateurs", 0.0, "S"),
    ("besoin_par_m2", "Besoin total par m² de plancher du château (€/m²)",
     "[total_besoin]/{S}_surf_chateau", "Indicateurs", 0.0, "S"),
    ("dette_annuite", "Scénario complémentaire : annuité d'une dette d'acquisition",
     "-PMT(dette_taux{C},dette_duree{C},{S}_prix_achat*dette_quotite{C})", "Scénario dette", 0.0, "S"),
    ("total_avec_dette", "BESOIN ANNUEL AVEC DETTE D'ACQUISITION (scénario complémentaire)",
     "[total_besoin]+[dette_annuite]", "Scénario dette", 0.0, "S"),
]
