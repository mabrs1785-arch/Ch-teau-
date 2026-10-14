# État de reprise — Mission « Équation économique d'un château »

Dernière mise à jour : 2026-10-14 (après la vague 1, le modèle v2 et le Monte-Carlo)

## Où en est-on ?

| Étape | Statut |
|---|---|
| Structure, contexte, règles, plan, cadre analytique | FAIT |
| Vague 1 : 8 agents (R1 à R8), environ 440 sources | FAIT |
| Modèle Excel et Python (`02_MODELE/`) : budget S1/S2/S3, 19 moteurs, 6 modèles, projections sur 20 ans, 8 stress tests | FAIT (10 491 formules, 0 erreur, 0 écart Excel/Python) |
| Jumeau Monte-Carlo exact de la projection, puis dotation nécessaire (50 % et 95 %) et grille hybride | FAIT (`02_MODELE/sorties/mc_*.json`) |
| Vague 2 : V2A (bail à un exploitant), V2C (budgets réels et leviers), V2D (opérations MH, location de luxe) | EN COURS |
| Vague 2 bis : équipe rouge et vérification des chiffres clés | À FAIRE après V2A, V2C, V2D |
| Livrables L1 à L8, README, registre des sources | À FAIRE |

## Résultats provisoires (cas central, € 2026)

- **Besoin annuel** : S1 ≈ 0,33 M€, S2 ≈ 1,23 M€, S3 ≈ 3,41 M€. Fourchettes : S1 0,19-0,56 M€ ; S2 0,77-2,03 M€ ; S3 1,97-6,1 M€.
- **Activités sur place** : elles couvrent moins de 10 % du besoin S2 dans le cas central (M1 : 4 % ; M2 : 7 % ; château-hôtel : négatif).
- **Dotation nécessaire sur 30 ans, avec règles de pilotage** :
  - S1 : 9 M€ (50 %), 20 M€ (95 %) ;
  - S2 : 36 M€ (50 %), 76 M€ (95 %) ;
  - S3 : 102 M€ (50 %), 224 M€ (95 %).

## Instruction de reprise

1. Lire `00_PILOTAGE/Contexte_permanent.md`, `Cadre_analytique.md`, ce fichier et `Journal.md`.
2. Reconstruire le modèle : `cd 02_MODELE && python3 construire_modele.py` (recalcul LibreOffice et vérification automatiques).
3. Si V2A, V2C ou V2D manquent (fichiers `01_RECHERCHE/V2*_*.md` sans section « Chiffres clés »), les relancer. Les consignes sont dans `Prompts_agents.md`.
4. Lancer ensuite l'équipe rouge et la vérification, puis rédiger les livrables dans `03_LIVRABLES/`.
