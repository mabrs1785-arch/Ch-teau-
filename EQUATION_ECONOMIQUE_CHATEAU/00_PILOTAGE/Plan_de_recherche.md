# Programme de recherche — Mission « Équation économique d'un château »

## 1. Question centrale

Combien coûte réellement, chaque année, un grand domaine de château entretenu à un niveau d'exception ? Quel mécanisme économique peut produire durablement cette trésorerie, après impôts, renouvellement des investissements, gros entretien et aléas, sans compromettre la vie privée du propriétaire ?

## 2. Hypothèses de départ à tester

Ce sont des hypothèses, pas des conclusions. Chacune doit être confirmée ou réfutée avec des preuves.

| # | Hypothèse | Comment la tester |
|---|---|---|
| H1 | Le besoin annuel de trésorerie d'un domaine S2 se situe entre 0,5 et 1,5 M€, provisions comprises | Budget poste par poste (R1, R2) |
| H2 | Le gros entretien du bâti est le poste le plus souvent sous-estimé | Ratios de la Demeure Historique, de Historic Houses (Royaume-Uni), cycles de vie des composants (R1) |
| H3 | Les activités classiques (mariages, chambres d'hôtes, séminaires, visites) couvrent rarement les coûts d'un domaine S2 ou S3 sans sacrifier la tranquillité | Comptes réels, saturation du marché (R4, R7) |
| H4 | Une activité équestre finance au mieux ses propres installations, rarement le château | Références économiques de la filière (R6) |
| H5 | Les revenus contractuels (baux, pensions, redevances) dégagent moins de marge, mais résistent mieux, que l'exploitation directe | Comparaison des structures de revenus (R4, R5, R8) |
| H6 | Un grand foncier (> 200 ha) apporte des revenus récurrents significatifs (forêt, chasse, énergie, fermage) | Prix de marché sourcés (R2, R8) |
| H7 | La vente ou la location longue d'une partie du patrimoine (dépendances, hameaux) peut constituer une dotation en capital (modèle de Castello di Reschio) | Exemples réels et contraintes françaises : SAFER, PLU (R5, R8, R3) |
| H8 | Une entreprise ou un portefeuille extérieurs au domaine forment un moteur plus robuste que l'exploitation sur place, sous conditions (diversification, conversion en dotation, gouvernance) | Données de rendement, taux de retrait soutenables, défaillance des PME (R8) |
| H9 | La fiscalité (régime des monuments historiques, déductibilité des charges via une société, TVA) change fortement le besoin réel de trésorerie | Textes officiels (R3) |
| H10 | Le système le plus résilient combine un socle contractuel, un cœur d'activité maîtrisé et une réserve de liquidité | Modèle sur 20 ans et Monte-Carlo (phase de modélisation) |

## 3. Vague 1 — Exploration documentée (8 agents en parallèle)

| ID | Thème | Livrable |
|---|---|---|
| R1 | Coûts du bâti patrimonial : entretien, restauration par composant, cycles de vie, assurance, énergie, taxe foncière, subventions | `01_RECHERCHE/R1_couts_bati_patrimoine.md` |
| R2 | Coûts du personnel, des jardins, des terres, des équipements et des chevaux | `01_RECHERCHE/R2_couts_personnel_jardins_equestre.md` |
| R3 | Cadre fiscal et juridique : régime MH, IFI, TVA, structures, baux, urbanisme, ERP, mécénat | `01_RECHERCHE/R3_cadre_fiscal_juridique.md` |
| R4 | Domaines français : modèles réels, comptes publiés, réussites et échecs | `01_RECHERCHE/R4_benchmark_france.md` |
| R5 | Domaines étrangers : Royaume-Uni, Irlande, Italie, États-Unis, etc. | `01_RECHERCHE/R5_benchmark_international.md` |
| R6 | Économie équestre : sport, loisir, course, élevage, services, événements | `01_RECHERCHE/R6_economie_equestre.md` |
| R7 | Marchés de l'événementiel, de l'hébergement, des tournages et des visites | `01_RECHERCHE/R7_marches_evenementiel_hebergement.md` |
| R8 | Revenus non conventionnels, revenus fonciers et moteur extérieur (entreprise, dotation) | `01_RECHERCHE/R8_revenus_non_conventionnels.md` |

## 4. Vagues suivantes

- **Synthèse 1 (directeur)** : budgets S1, S2, S3 et premier inventaire des moteurs de revenus, avec leur contribution nette.
- **Modèle v1 (directeur)** : code Python traçable (`02_MODELE/`), puis classeur Excel avec formules.
- **Vague 2** :
  - équipe rouge : chaque modèle candidat est attaqué par un agent indépendant ;
  - vérification croisée des 30 chiffres les plus influents ;
  - approfondissement de la demande pour le meilleur modèle.
- **Reconstruction** : correction des modèles, puis projection sur 20 ans, stress tests et Monte-Carlo.
- **Livrables** : `03_LIVRABLES/L1` à `L8`, plus le registre des sources consolidé.

## 5. Critères de comparaison des modèles

1. Contribution nette de trésorerie, après impôts, renouvellement des investissements et rémunération du travail.
2. Récurrence et prévisibilité des revenus.
3. Résistance à une baisse de 30 % du chiffre d'affaires et à une crise de type 2020.
4. Investissement initial et délai de montée en charge.
5. Personnel nécessaire et dépendance au fondateur.
6. Compatibilité avec la vie privée, le prestige et la tranquillité.
7. Risques réglementaires.
8. Durabilité sur 20 à 30 ans.
9. Preuves de demande solvable.
