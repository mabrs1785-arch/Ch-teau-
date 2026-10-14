# Journal des agents

## Session 1 — 2026-10-14
Règles communes : `_brut/REGLES_AGENTS.md`.

| Agent | Mission | Livrables | Statut |
|---|---|---|---|
| 1 Chasse immobilière | Jusqu'à 30 biens réels vérifiés | 01_OPPORTUNITES/* | terminé |
| 2 Ingénierie financière | Montages, crowdfunding, investisseurs, fiscalité MH | 03_FINANCEMENT/* | terminé |
| 3 Économie équestre | 10 modèles équestres, hypothèses chiffrées | 02_BENCHMARK/Modeles_equestres.md | terminé |
| 4 Développement commercial | Mariages, séminaires, hébergement, agriculture… | 02_BENCHMARK/Activites_complementaires.md | terminé |
| 6 Juridique/fiscal | Textes officiels, risques, validations à faire | 05_AUDIT/Cadre_juridique_fiscal.md | terminé |
| 7 Benchmark | 10–15 cas réels + contre-exemples | 02_BENCHMARK/Domaines_remarquables.md | terminé |
| 5 Modélisation | Excel 10 ans, 3 scénarios | 04_MODELES_ECONOMIQUES/* | terminé (directeur) |
| 8 Auditeur | Objections, stress tests | 05_AUDIT/* | terminé |
| Vague 2 vérification | Charges château, fermage, loyers, apports bancaires | 05_AUDIT/Verifications_vague2.md | terminé |

## Incidents
- Ouverture de pages (WebFetch, curl) bloquée par la politique réseau : tous les agents ont travaillé sur les extraits de recherche.
- Quota de recherches web atteint pendant la vague 1 (≈ 200 requêtes partagées) : trous comblés partiellement par la vague 2 (45 requêtes).
- Bug de modèle (collision de clé « loyer_prive ») détecté au recalcul, corrigé, garde-fou ajouté.
