# Journal de la mission « Équation économique d'un château »

## 2026-10-14

- **Démarrage.** Lecture du brief. Le dépôt contient deux missions antérieures :
  - `PROJET_CHATEAU_24H`, consacrée à l'acquisition (v1 faite sans accès web ; v2 relancée sans laisser de résultats) ;
  - `PODCASTS_CHATEAU_24H`.

  Le nouveau brief traite un problème distinct : les coûts de fonctionnement et le financement pérenne. D'où la création d'un dossier dédié, `EQUATION_ECONOMIQUE_CHATEAU/`.
- **Leçons de méthode reprises de la v1** (audit contradictoire de la v1, commit bd10d76) :
  - distinguer TTC et HT ;
  - prévoir un loyer privé pour le fondateur et le rémunérer en conséquence ;
  - tenir compte de la saturation du fondateur ;
  - risque de requalification en bail rural ;
  - obligations ERP ;
  - calculer le DSCR après gros entretien.

  Aucun chiffre de la v1 n'est repris.
- **Tests d'environnement :**
  - Légifrance et Pappers renvoient 403 à WebFetch ;
  - l'API recherche-entreprises est coupée par le proxy ;
  - annuaire-entreprises et la recherche societe.com renvoient un contenu vide.

  Une première recherche web confirme l'existence d'une note de La Demeure Historique (2019) évoquant « 40 000 € par an au minimum » hors ouverture et hors restauration. C'est un extrait, à lire en entier par l'agent R1.
- **Vague 1 lancée** : 8 agents en parallèle (R1 à R8). Les missions sont décrites dans `Prompts_agents.md`.
- **En parallèle** : architecture du modèle financier dans `02_MODELE/`.
- **Vague 1 terminée** : 8 rapports (R1 à R8), environ 440 sources. Constat central : les activités compatibles avec une résidence calme ne couvrent qu'une petite part du besoin ; les domaines qui tiennent s'appuient sur un patrimoine de rapport dédié (Burghley, Blenheim, Northumberland) ou sur un revenu extérieur.
- **Modèle v2** (`02_MODELE/`) :
  - budget S1/S2/S3 en trois cas ;
  - moteurs de revenus et modèles M1 à M6 ;
  - projections sur 20 ans avec fonds de travaux, dotation et règles de pilotage ;
  - 8 stress tests ;
  - jumeau Monte-Carlo exact.
  - Chaque formule Excel est vérifiée par un calcul Python.
- **Corrections du modèle** :
  - annuité de dette (PMT) ;
  - drapeau de crise en année 1 ;
  - investissement prélevé sur le capital ;
  - facteurs d'échelle par scénario ;
  - calibrage des rendements (moyenne géométrique) ;
  - réserves supérieures à un an de besoin.
- **Livrables L1 et L2 (partie 1)** rédigés.

## 2026-10-14 (suite) — vague 2, livrables

- **Vague 2 reçue** :
  - **V2A** (bail à un exploitant) : conditions d'entrée des exploitants de séminaires, loyer estimé, cadre juridique ;
  - **V2C** (budgets réels et leviers) : rapport IGF-IGAC de 2020, temps d'entretien des jardins de la Ville de Rennes, dérives INSEE sur 20 ans ;
  - **V2D** (libérer du capital, location de luxe) : opérations MH, démembrement, copropriété ;
  - **V2V** (vérification) : 90 chiffres clés, 81 confirmés, 9 nuancés, aucun faux.
- **Modèle mis à jour** :
  - dérives réelles recalées sur les séries INSEE : travaux +0,75 %, énergie +2 %, assurances +1,85 % (nouvel indice) ;
  - jardiniers de S3 portés de 11 à 16 ETP ;
  - nouveaux moteurs « bail d'ancrage » et « location de luxe », avec les modèles M7 et M8 ;
  - notes et statuts corrigés selon V2V.
- **Corrections de logique** :
  - sans dotation, l'investissement de l'année 1 est pris sur la réserve (il disparaissait) ;
  - la réserve de S3, passée sous un an de besoin, déclenchait la coupe de pilotage en permanence : elle est portée à 4 M€ ;
  - dans les tests de besoin, la réserve suit désormais le besoin ;
  - `calculer_mc.py` recalcule le classeur (il le laissait sans valeurs en cache).
- **Ajouts** :
  - `verifier_jumeau` : le Monte-Carlo sans chocs reproduit les projections à moins de 10⁻⁶ € ;
  - `sensibilite.py` : la tornade du besoin est reproductible ;
  - `04_SOURCES/consolider.py` : registre de 636 sources, format contrôlé.
- **Solution dimensionnée** au même niveau de risque pour les trois scénarios (environ 4 à 6 % d'échec avant 20 ans, 11 à 12 % avant 30 ans) :
  - S1 : 15 M€ + 0,4 M€ par an pendant 10 ans ;
  - S2 : 60 M€ + 1 M€ par an pendant 10 ans ;
  - S3 : 210 M€.
- **Livrables rédigés** : L1 et L2 mis à jour, L3, L4, L5, L6, L7 et le README.
- **Équipe rouge (V2R)** lancée ; ses constats doivent être intégrés avant L8.
