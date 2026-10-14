# Journal — cellule audiovisuelle v2

## Capacités constatées (14/10/2026)
- Accès web ouvert par l'utilisateur en cours de session ; WebFetch échoue (DNS) mais curl via le proxy fonctionne.
- **Aucun outil de transcription audio** (installation refusée par l'utilisateur) et **aucun téléchargement de média**. Aucun contenu regardé ni écouté.
- YouTube a renvoyé des erreurs HTTP 429 sur l'adresse IP partagée à partir de ~17 h 48 : aucun contournement ; seuls les flux RSS officiels des chaînes ont été utilisés ensuite.
- Pages bloquées : Le Monde (paywall), Pappers et annuaire-entreprises (anti-robot), Légifrance (403), Medium, Happy Scribe, BAILII.
- Persistance : commits git réguliers sur la branche de travail.

## Agents (20 spécialités du brief regroupées en 8 agents + directeur)
| Agent | Spécialités | Contenus catalogués | Livrables | Statut |
|---|---|---|---|---|
| AV1 | 1-2 châteaux français, patrimoine | 182 | fiches, 14 cas, 15 idées | terminé |
| AV2 | 3-4 domaines britanniques et irlandais, haras | 171 | 36 fiches, 22 cas, 15 idées | terminé |
| AV3 | 5-8 business du cheval | 151 | 24 fiches, 18 cas, 14 idées | terminé |
| AV4 | 9-12 acquisition et financement | 139 | 31 fiches, 13 cas, 13 idées + garde-fous | terminé |
| AV5 | 13-16 modèles premium | 93 | 15 fiches, 19 cas, 15 idées | terminé |
| AV6 | The Family (demande de l'utilisateur) | 98 | 12 fiches, dossier procédures, 14 idées | terminé |
| AV7 | 17-18 idées originales et échecs | 44 | fiches, 12 échecs, 12 idées | terminé |
| AV8 | 19 vérification des preuves | — | 35 affirmations vérifiées (15 ✅, 13 ◐, 6 non confirmées, 1 ✗) | terminé |
| Directeur | 20 synthèse stratégique, interface | — | 05_RECOMMANDATIONS, index, synthèse des modèles, interface.html | terminé |

## Volumes réels (après dédoublonnage)
- 836 contenus identifiés (478 vidéos, 286 podcasts, 72 autres).
- 38 transcriptions publiées lues (10 complètes, 28 partielles) ; 390 descriptions ou chapitres lus ; 51 métadonnées ; 50 sources secondaires ; 307 seulement repérés (dont 130 pages inaccessibles).
- 121 passages horodatés réels (issus de transcriptions ou de chapitres publiés).
- Objectifs indicatifs du brief : 200 identifiés (atteint), 100 analysés (atteint si l'on compte descriptions et chapitres ; **non atteint** pour une analyse complète à partir de transcriptions : 38), 30 interviews intéressantes (97 contenus ≥ 70/100), 20 modèles (atteint), 15 mécanismes de financement (atteint), 10 idées originales, 5 stratégies approfondies, 3 recommandations prioritaires (livrés).

## Erreurs et incidents
- Collisions de fichiers temporaires entre agents (scripts écrasés) : règle ajoutée (sous-dossier personnel).
- AV8 a corrigé plusieurs chiffres d'agents (Fontenay, Dampierre, Strawbridge, Fresnay, Blenheim, Castillon, Arqana) : les recommandations finales utilisent les valeurs corrigées.
- Relecture du directeur avant publication : la mention « aucune condamnation pénale connue en France » était trop large dans la découverte n° 18 et dans l'index des cas. Elle est précisée en « dans l'affaire The Family », avec un renvoi à la condamnation de 2018 (affaire Be Sport) rapportée par la presse mais non vérifiée et contredite (AV6 §4.3, AV8 §6). Même correction dans le rapport exécutif de la mission 1.

## Reprise
- Pour enrichir : relancer en vague C l'analyse des contenus « repérés » à forte pertinence quand YouTube sera de nouveau accessible, ou, si l'utilisateur l'autorise, installer un outil de transcription locale pour les podcasts diffusés par flux RSS public.
- Régénérer l'interface : `python3 build_interface.py`.
