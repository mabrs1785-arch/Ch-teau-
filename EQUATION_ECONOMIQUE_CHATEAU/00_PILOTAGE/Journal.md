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
