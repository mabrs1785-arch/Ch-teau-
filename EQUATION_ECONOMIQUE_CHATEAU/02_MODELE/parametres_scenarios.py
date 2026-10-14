"""Paramètres physiques des trois domaines types (S1, S2, S3).

Ce sont des CHOIX DE SCÉNARIO (statut HYPOTHÈSE) ou des ESTIMATIONS géométriques
déduites de ces choix. Ils ne prétendent décrire aucun bien réel. La justification
de chaque valeur figure dans la note.
"""
from noyau import p

G = "Scénarios — description physique"

GEOMETRIE = (
    "Géométrie (ESTIMATION) : emprise ≈ plancher / nombre de niveaux ; toiture développée ≈ emprise × 1,4 "
    "(pente) ; façades ≈ périmètre × hauteur. Ordre de grandeur à remplacer par les métrés réels d'un bien."
)

# ---- Château et dépendances --------------------------------------------------
p("S1_surf_chateau", "S1 — surface de plancher du château", 900, unite="m²", groupe=G,
  note="Choix de scénario : petit château ou grande maison de maître, environ 700 m² habitables.")
p("S2_surf_chateau", "S2 — surface de plancher du château", 2000, unite="m²", groupe=G,
  note="Choix de scénario : château de taille moyenne à grande.")
p("S3_surf_chateau", "S3 — surface de plancher du château", 4500, unite="m²", groupe=G,
  note="Choix de scénario : grand château historique avec décors intérieurs.")
p("S1_surf_dep", "S1 — dépendances (écurie, grange)", 600, unite="m²", groupe=G)
p("S2_surf_dep", "S2 — dépendances (écuries historiques, communs, granges)", 2500, unite="m²", groupe=G)
p("S3_surf_dep", "S3 — dépendances (orangerie, communs, chapelle, logements, écuries)", 4000,
  unite="m²", groupe=G)
p("S1_surf_toits", "S1 — toitures développées (château et dépendances)", 1200, unite="m²",
  statut="ESTIMATION", groupe=G,
  note=GEOMETRIE + " Château : 3 niveaux, emprise ≈ 350 m² → ≈ 500 m² de toiture ; dépendances "
       "de plain-pied ≈ 600 m² d'emprise → ≈ 700 m².")
p("S2_surf_toits", "S2 — toitures développées", 3300, unite="m²", statut="ESTIMATION", groupe=G,
  note=GEOMETRIE + " Château ≈ 700 m² d'emprise → ≈ 1 000 m² ; dépendances ≈ 1 650 m² d'emprise → ≈ 2 300 m².")
p("S3_surf_toits", "S3 — toitures développées", 6000, unite="m²", statut="ESTIMATION", groupe=G,
  note=GEOMETRIE + " Château ≈ 1 500 m² d'emprise → ≈ 2 100 m² ; dépendances ≈ 2 800 m² d'emprise → ≈ 3 900 m².")
p("S1_surf_facades", "S1 — façades (château et dépendances)", 1800, unite="m²", statut="ESTIMATION",
  groupe=G, note=GEOMETRIE + " Château : périmètre ≈ 78 m × 12 m ; dépendances ≈ 150 m × 6 m.")
p("S2_surf_facades", "S2 — façades", 4000, unite="m²", statut="ESTIMATION", groupe=G,
  note=GEOMETRIE + " Château : ≈ 115 m × 14 m ; dépendances ≈ 350 m × 7 m.")
p("S3_surf_facades", "S3 — façades", 6200, unite="m²", statut="ESTIMATION", groupe=G,
  note=GEOMETRIE + " Château : ≈ 170 m × 16 m ; dépendances ≈ 500 m × 7 m.")
p("S1_nb_baies", "S1 — nombre de baies (fenêtres et portes-fenêtres)", 60, unite="unités",
  statut="ESTIMATION", groupe=G, note="Environ une baie pour 15 m² de plancher du château + dépendances.")
p("S2_nb_baies", "S2 — nombre de baies", 130, unite="unités", statut="ESTIMATION", groupe=G)
p("S3_nb_baies", "S3 — nombre de baies", 260, unite="unités", statut="ESTIMATION", groupe=G)

# ---- Foncier ---------------------------------------------------------------------
p("S1_ha_jardins", "S1 — jardins entretenus (abords, potager)", 0.5, unite="ha", groupe=G)
p("S2_ha_jardins", "S2 — jardins réguliers et potager", 2, unite="ha", groupe=G)
p("S3_ha_jardins", "S3 — jardins réguliers, parterres, potager", 10, unite="ha", groupe=G)
p("S1_ha_parc", "S1 — parc et pelouses", 2.5, unite="ha", groupe=G)
p("S2_ha_parc", "S2 — parc paysager", 8, unite="ha", groupe=G)
p("S3_ha_parc", "S3 — parc paysager", 50, unite="ha", groupe=G)
p("S1_ha_prairies", "S1 — prés, paddocks et prairies de fauche", 35, unite="ha", groupe=G)
p("S2_ha_prairies", "S2 — prés, paddocks et prairies de fauche", 80, unite="ha", groupe=G)
p("S3_ha_prairies", "S3 — prés, paddocks et terres", 120, unite="ha", groupe=G)
p("S1_ha_bois", "S1 — bois", 12, unite="ha", groupe=G)
p("S2_ha_bois", "S2 — bois", 30, unite="ha", groupe=G)
p("S3_ha_bois", "S3 — bois", 120, unite="ha", groupe=G)
p("S1_ml_clotures", "S1 — clôtures équestres et périphériques", 3000, unite="ml", statut="ESTIMATION",
  groupe=G, note="Pour 35 ha de prés découpés en paddocks : ≈ 85 ml/ha.")
p("S2_ml_clotures", "S2 — clôtures", 7000, unite="ml", statut="ESTIMATION", groupe=G,
  note="Pour 80 ha de prés : ≈ 85 ml/ha.")
p("S3_ml_clotures", "S3 — clôtures", 10000, unite="ml", statut="ESTIMATION", groupe=G,
  note="Pour 120 ha : ≈ 85 ml/ha.")

# ---- Équestre ---------------------------------------------------------------------
p("S1_nb_boxes", "S1 — boxes", 12, unite="boxes", groupe=G)
p("S2_nb_boxes", "S2 — boxes", 40, unite="boxes", groupe=G)
p("S3_nb_boxes", "S3 — boxes", 50, unite="boxes", groupe=G)
p("S1_nb_chevaux", "S1 — chevaux appartenant au propriétaire", 4, unite="chevaux", groupe=G,
  note="Les autres boxes sont vides ou utilisés par une activité.")
p("S2_nb_chevaux", "S2 — chevaux appartenant au propriétaire", 8, unite="chevaux", groupe=G)
p("S3_nb_chevaux", "S3 — chevaux appartenant au propriétaire", 12, unite="chevaux", groupe=G)
p("S1_surf_pistes", "S1 — carrières (surface de sol équestre)", 1800, unite="m²", groupe=G,
  note="Une carrière de 60 × 30 m.")
p("S2_surf_pistes", "S2 — carrières et sol du manège", 7100, unite="m²", groupe=G,
  note="Deux carrières de 70 × 40 m et le sol d'un manège de 60 × 25 m.")
p("S3_surf_pistes", "S3 — carrières et sol du manège", 7500, unite="m²", groupe=G)
p("S1_surf_manege", "S1 — manège couvert (bâtiment)", 0, unite="m²", groupe=G)
p("S2_surf_manege", "S2 — manège couvert (bâtiment)", 1500, unite="m²", groupe=G)
p("S3_surf_manege", "S3 — manège couvert (bâtiment)", 1500, unite="m²", groupe=G)
