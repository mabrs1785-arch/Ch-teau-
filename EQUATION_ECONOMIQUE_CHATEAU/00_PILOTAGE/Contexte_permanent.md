# CONTEXTE PERMANENT — Mission « Équation économique d'un château » (v3)

Démarrée le 2026-10-14. Brief complet : `00_PILOTAGE/Brief_mission_original.txt`.
État d'avancement et instruction de reprise : `00_PILOTAGE/Etat_de_reprise.md`.

## 1. La mission en une phrase

Trouver un système économique capable de financer, année après année et pendant 20 à 30 ans, le **fonctionnement** d'un grand château français et de son domaine (idéalement > 50 ha), **sans dépendre de la fortune personnelle du propriétaire**, tout en préservant une résidence privée tranquille, un niveau d'entretien d'exception et une place importante pour les chevaux.

Hors périmètre : le financement de l'achat. Le service d'une dette d'acquisition est seulement un **scénario complémentaire**.

## 2. Ce qui distingue cette mission des travaux déjà présents dans le dépôt

- `PROJET_CHATEAU_24H/` porte sur l'**acquisition** avec un apport limité. La v1 a été faite sans accès web. La v2 a été relancée mais n'a laissé aucun résultat. Ces travaux **ne sont pas des sources**.
- `PODCASTS_CHATEAU_24H/` est une mission de veille audiovisuelle, sans lien direct.
- Leçons de méthode retenues de la v1. Ce sont des pièges à éviter, pas des faits :
  1. Ne pas traiter des prix publics TTC comme des montants HT.
  2. Si le propriétaire occupe un bien détenu par une société, il paie un loyer de marché. Il faut donc aussi une rémunération ou un revenu réel pour le payer.
  3. Le temps du fondateur est limité. Ne pas empiler les activités sur une seule personne.
  4. Les événements bruyants cohabitent mal avec les chevaux (feux d'artifice, musique) et avec les cavaliers présents le week-end.
  5. Louer des écuries à un cavalier professionnel peut être requalifié en bail rural.
  6. Une salle de réception de plus de 50 personnes relève des règles ERP, avec un investissement correspondant.
  7. Après gros entretien, un EBITDA positif peut cacher un flux de trésorerie négatif.

## 3. Profil et souhaits du propriétaire (données du brief)

- 26 ans, passionné de chevaux. Il veut vivre sur place, dans une partie **entièrement privée**.
- Patrimoine d'exception : château restauré, dépendances en excellent état, jardins impeccables, parc parfaitement entretenu, installations équestres de qualité, personnel suffisant.
- Domaine élégant, prestigieux et calme.
- Projet équestre commercial, événementiel ou partiellement privé. Les chevaux ne sont **pas** obligatoirement la source principale de revenus.
- Données inconnues : région, valeur du bien, revenus et patrimoine du propriétaire, expérience professionnelle. On les traite par **scénarios explicites**.

## 4. Les trois domaines types du budget

Ce sont des **paramètres de scénario** choisis pour structurer le calcul, pas des faits. Ils seront ajustés selon la recherche.

| Paramètre | S1 — Domaine relativement économique | S2 — Grand domaine équestre haut de gamme | S3 — Domaine historique ultra-premium |
|---|---|---|---|
| Château (surface de plancher) | ≈ 900 m² (≈ 700 m² habitables) | ≈ 2 000 m² | ≈ 4 500 m² avec décors intérieurs |
| Protection | non protégé ou inscrit MH | inscrit MH | classé MH |
| Toitures (surface développée) | ≈ 600 m² | ≈ 1 200 m² | ≈ 2 500 m² |
| Dépendances | ≈ 600 m² (écurie, grange) | ≈ 2 500 m² (écuries historiques, communs, granges) | ≈ 4 000 m² (orangerie, communs, chapelle, logements) |
| Foncier | 50 ha (35 prés/foin, 12 bois, 3 parc) | 120 ha (80 prés, 30 bois, 10 parc et jardins dont 2 ha à la française) | 300 ha (10 jardins réguliers et potager, 50 parc, 120 bois, 120 prés et terres) |
| Équestre | 12 boxes, carrière, paddocks | 40 boxes, manège couvert, 2 carrières, cross, pistes | 40 à 60 boxes, manège, carrières, piste, cross |
| Personnel (ordre de grandeur à vérifier) | 2 à 3 ETP | 8 à 12 ETP | 20 à 30 ETP |

## 5. Conventions de calcul (obligatoires pour tous)

- **Monnaie** : euros. Préciser l'année du prix. Les modèles travaillent en **€ constants 2026**, l'inflation est traitée à part.
- **HT / TTC** : toujours le préciser. Une activité assujettie à la TVA raisonne en HT. Un particulier propriétaire supporte le TTC, car il ne récupère pas la TVA.
- **Ne jamais confondre** chiffre d'affaires, EBE/EBITDA, résultat net comptable et trésorerie disponible (après impôts, remboursement de dette, renouvellement des investissements et gros entretien).
- **Revenus récurrents** (contrats, loyers, abonnements, pensions) **≠ revenus occasionnels** (événements, tournages, ventes ponctuelles).
- Préciser pour chaque chiffre : valeur, unité, année, périmètre (région, type de bien) et source.

## 6. Règles d'honnêteté (préférence explicite de l'utilisateur)

« N'invente rien. Si tu ne sais pas ou si tu as un doute, dis-le au lieu de donner des données fausses ou inventées. »

- Aucun chiffre, aucune source, aucune transaction, aucun client, aucune preuve de rentabilité inventés.
- Statut de chaque donnée :
  - **PAGE LUE** : page ouverte avec WebFetch, citation exacte.
  - **EXTRAIT** : vu seulement dans un résultat de recherche.
  - **ESTIMATION** : raisonnement explicite à partir de données sourcées.
  - **HYPOTHÈSE** : choix de modélisation assumé.
  - **INCONNU** : « Je ne sais pas », avec la méthode pour vérifier.
- Conserver les divergences entre sources au lieu de les lisser.

## 7. Environnement technique (vérifié le 2026-10-14)

- Accès web : WebSearch (quota limité, partagé entre agents, de l'ordre de 200 recherches par tour d'après la session précédente) et WebFetch.
- Bloqués ou inexploitables par WebFetch : legifrance.gouv.fr (403), pappers.fr (403), API recherche-entreprises (connexion coupée), annuaire-entreprises (contenu dynamique vide), recherche societe.com (vide).
- Sources lisibles probables (à essayer) : bofip.impots.gouv.fr, impots.gouv.fr, service-public.fr, entreprendre.service-public.fr, culture.gouv.fr, senat.fr, assemblee-nationale.fr, ccomptes.fr, ifce.fr, ffe.com, agreste.agriculture.gouv.fr, cre.fr, ecologie.gouv.fr, insee.fr, code.travail.gouv.fr, demeure-historique.org, vmfpatrimoine.org, fondation-patrimoine.org, Companies House (find-and-update.company-information.service.gov.uk), sites des domaines eux-mêmes, presse régionale et économique, PDF publics.
- Python 3.13 (pandas, numpy, openpyxl, xlsxwriter) et LibreOffice pour recalculer les classeurs. Pas de matplotlib (graphiques via xlsxwriter ou SVG).
- Persistance : git. Branche `claude/new-session-4wwka5`. Seul le directeur fait les commits.
