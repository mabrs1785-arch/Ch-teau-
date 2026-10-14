# R4 — Domaines français : modèles réels, comptes, réussites, échecs

Agent R4 — démarré le 2026-10-14. Fichier écrit au fur et à mesure (état : EN COURS).
Sources : `01_RECHERCHE/sources/sources_R4.csv` (identifiants [R4-xx]).

## 0. Méthode et outils

- Comptes des sociétés : API officielle « Recherche d'entreprises » (recherche-entreprises.api.gouv.fr, alimentée par l'INSEE/INPI), ouverte avec WebFetch. Elle donne le SIREN, le code NAF, la tranche d'effectif salarié (codes INSEE) et, quand les comptes sont publiés (non confidentiels), le chiffre d'affaires (CA) et le résultat net de la dernière année déposée. Statut : PAGE LUE.
  - Codes de tranche d'effectif INSEE utilisés : 00 = 0 salarié ; 01 = 1-2 ; 02 = 3-5 ; 03 = 6-9 ; 11 = 10-19 ; 12 = 20-49 ; 21 = 50-99 ; 22 = 100-199 ; 31 = 200-249 ; 32 = 250-499 ; 41 = 500-999 ; NN = non renseigné.
  - `finances: null` = aucun compte publié dans la base (comptes confidentiels, non déposés ou société non commerciale). Cela ne dit rien de la rentabilité.
- Pappers renvoie 403 : non utilisé. Les extraits Pappers/societe.com vus en résultat de recherche ont le statut EXTRAIT.
- Rappel : le CA et le résultat d'une société d'exploitation ne disent rien de la fortune du propriétaire, et inversement.

## 1. Fiches par cas

(en cours de rédaction)

### 1.A Constat transversal sur les comptes publiés (registre officiel)

Les grands châteaux privés ouverts à la visite sont presque tous exploités par une **société civile** (SCI ou « autre société civile ») ou par le propriétaire en **entreprise individuelle**. Ces structures ne publient pas leurs comptes : `finances: null` dans le registre. Seules les sociétés commerciales satellites (restaurant, boutique, hôtel) publient un CA. Statut : PAGE LUE.

| Domaine | Entité d'exploitation principale (registre) | Forme | NAF | Effectif salarié (tranche INSEE, 2024) | Comptes publiés | Source |
|---|---|---|---|---|---|---|
| Vaux-le-Vicomte (77) | SCI VALTERRE, SIREN 393246418, siège Maincy | société civile (6599) | 91.03Z gestion de monuments | 21 = 50 à 99 salariés | non (null) ; commissaire aux comptes nommé | [R4-02] |
| Chenonceau (37) | CHATEAU DE CHENONCEAU, SIREN 775702509 | société civile (6599) | 91.03Z | 21 = 50 à 99 | non (null) | [R4-05] |
| Cheverny (41) | SCI CHATEAU DE CHEVERNY, SIREN 322423732 | société civile (6599) | 91.03Z | 12 = 20 à 49 | non (null) | [R4-03] |
| Villandry (37) | SCI DU CHATEAU DE VILLANDRY, SIREN 400292520 | société civile (6599) | 91.03Z | 12 = 20 à 49 | non (null) | [R4-04] |
| Brissac (49) | CHARLES DE BRISSAC, SIREN 440149557 | entreprise individuelle (1000) | 91.03Z | 02 = 3 à 5 | non | [R4-06] |
| Breteuil (78) | FRANCOIS LE TONNELIER DE BRETEUIL, SIREN 785049651 | entreprise individuelle (1000) | 91.03Z | 03 = 6 à 9 | non | [R4-13] |
| Courances (91) | SCI DU PARC DE COURANCES, SIREN 342293404 | société civile (6599) | 68.20B location | 03 = 6 à 9 | non | [R4-12] |
| Mothe-Chandeniers (86) | CHATEAU DE LA MOTHE-CHANDENIERS, SIREN 835113820, créée le 2018-02-01, présidée par la société DARTAGNANS | SAS (5710) | 91.03Z | 03 = 6 à 9 | non (null) ; commissaire aux comptes nommé | [R4-19] |

Conséquence pour le modèle : **les chiffres d'affaires et résultats des grands châteaux-monuments privés ne sont pas publics**. Toute valeur de CA citée dans la presse pour ces domaines est déclarative (propriétaire ou journaliste) et doit garder le statut de la source qui la rapporte. Statut de ce constat : PAGE LUE (registre) + ESTIMATION (interprétation : société civile non tenue de publier ses comptes).

Sociétés satellites avec comptes publiés (dernière année disponible dans le registre) :

| Société | Rôle (d'après NAF et siège) | Année | CA (€) | Résultat net (€) | Effectif (tranche) | Source |
|---|---|---|---|---|---|---|
| CHENONCEAU CASTELLUM (SIREN 778115063), siège « Château de Chenonceau », gérante Pauline Menier | restauration (56.10A) sur le site | 2025 | 5 638 275 | 1 108 319 | 12 = 20 à 49 | [R4-05] |
| SERV - Sté d'exploitation de la restauration de Vaux-le-Vicomte (SIREN 510258296), gérant J.-C. de Vogüé | restauration (56.10A) | 2025 | 2 674 622 | -2 475 | 12 = 20 à 49 | [R4-02] |
| SEG - Sté d'étude et de gestion du domaine de Vaux-le-Vicomte (SIREN 784956609) | gestion de monument (91.03Z) | 2025 | 0 (*) | -29 136 | 11 = 10 à 19 | [R4-02] |
| ORANGERIE DU CHATEAU DE CHEVERNY (SIREN 950062901) | commerce de détail (47.78C) | 2024 | 0 (*) | 147 063 | 12 = 20 à 49 | [R4-03] |
| AU JARDIN DE VILLANDRY (SIREN 429478456), président H. Carvallo | restauration (56.10A) | 2024 | 0 (*) | 18 286 | 03 = 6 à 9 | [R4-04] |

(*) Un CA de 0 associé à 20-49 salariés est invraisemblable : il s'agit très probablement d'un compte de résultat déposé en option de confidentialité ou d'une donnée manquante. **Ne pas lire « 0 » comme un CA nul.** Statut : ESTIMATION.

Autres faits de registre utiles :
- Chenonceau : la société civile CHATEAU DE CHENONCEAU a, parmi ses dirigeants inscrits, la société « TRAJECTOIRE » en qualité d'**« Administrateur provisoire »** [R4-05]. Un administrateur provisoire est en général désigné par un tribunal en cas de blocage de la gouvernance (à vérifier dans la presse). Statut : PAGE LUE pour la mention ; ESTIMATION pour l'interprétation.
- Vaux-le-Vicomte : l'exploitation agricole est logée à part (SCEA TROIS FRERES, NAF 01.11Z céréales, 1 à 2 salariés), ainsi que l'immobilier (SCI ONZEBIS) [R4-02]. Schéma typique : monument / restauration / agriculture / immobilier dans des entités séparées.
- Cheverny : un GIE DU DOMAINE DE CHEVERNY (6 à 9 salariés) mutualise des fonctions entre la SCI, CHEVERNY EXPO, AU GRAND CHANCELIER et l'Orangerie [R4-03]. Le golf du château est exploité par une société tierce (SOCIETE NOUVELLE DU GOLF DU CHATEAU DE CHEVERNY : CA 2025 = 1 464 739 €, résultat net = -29 850 €, 10 à 19 salariés) [R4-03].
- Brissac : un GROUPEMENT FORESTIER DOMAINE DE BRISSAC (1 à 2 salariés) porte les bois [R4-06].
- Courances : maraîchage logé dans LES JARDINS DE COURANCES (EARL, NAF 01.13Z), locatif dans LES MAISONS DE COURANCES (SCI) [R4-07] [R4-12].
