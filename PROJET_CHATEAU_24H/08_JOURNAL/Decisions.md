# Journal des décisions

| # | Date | Décision | Justification |
|---|------|----------|---------------|
| D1 | 2026-10-14 | Exécution via sous-agents parallèles (outil Agent) plutôt que 24 h continues | Aucune garantie d'exécution continue ; la qualité prime sur la durée (brief §15). |
| D2 | 2026-10-14 | Le modèle financier (Agent 5) est construit par le directeur après réception des hypothèses des agents 3, 4, 2 | Éviter des chiffres inventés : le modèle doit s'appuyer sur des hypothèses sourcées. |
| D3 | 2026-10-14 | Trois scénarios d'apport explicites (50 k€ / 250 k€ / 1 M€) | Apport réel inconnu (brief §1). |
| D4 | 2026-10-14 | Ajout de deux documents non prévus : 02_BENCHMARK/Activites_complementaires.md et 05_AUDIT/Cadre_juridique_fiscal.md | Les livrables des agents 4 et 6 n'avaient pas d'emplacement dans l'arborescence imposée. |
| D5 | 2026-10-14 | Toutes les données web sont issues d'extraits de moteur de recherche, pas de pages consultées | Constaté : WebFetch et curl bloqués par la politique réseau de l'environnement (ENOTFOUND / proxy 403, ex. www.insee.fr). Fiabilité des chiffres plafonnée à « moyenne » ; vérification manuelle des pages requise. |
| D6 | 2026-10-14 | Prévoir une 2e vague de recherche ciblée pour les trous | Quota de recherches web (≈200 par tour, partagé entre agents) atteint pendant la 1re vague. |
| D7 | 2026-10-14 | Stress tests appliqués aux configurations survivantes (B frugal sans dette, C cible), pas aux cas centraux | Les cas centraux sont non viables avant tout stress : les stresser n'apprend rien. |
| D8 | 2026-10-14 | Corrections de modèle exigées par l'auditeur, toutes appliquées (prix HT, loyer privé hors CA, capital au prorata, DSCR après gros entretien, frais de cession, verdict incluant TRI investisseur et rémunération du dirigeant, loyer non décalé par le stress de retard, dette soutenable base an 10) | Biais optimistes démontrés ; règle « ne jamais masquer les hypothèses nécessaires à la rentabilité ». |
| D9 | 2026-10-14 | Séquencement de C changé : PME d'abord, domaine ensuite (plus d'exploitation de château loué en parallèle) | Objection R5 de l'auditeur (saturation du dirigeant) jugée fondée. |
| D10 | 2026-10-14 | Le directeur ne re-note pas les scénarios ; les notes de l'auditeur sont publiées telles quelles | Conserver l'indépendance de l'audit (brief §14 : garder les divergences). |
| D11 | 2026-10-14 | Horizon de pleine propriété annoncé : 2033-2036, pas 2031 | Fonds propres requis de 2,9 à 3,8 M€, hors de portée d'un seul LBO selon l'agent 2. |
