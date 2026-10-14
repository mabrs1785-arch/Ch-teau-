# R4 — Domaines français : modèles réels, comptes, réussites, échecs

Agent R4 — 2026-10-14. Fichier écrit au fur et à mesure (état : TERMINÉ, 21 cas documentés, 24 liquidations sourcées, 3 échantillons de comptes).
Sources : `01_RECHERCHE/sources/sources_R4.csv` (identifiants [R4-xx]).

## 0. Méthode et outils

- Comptes des sociétés : API officielle « Recherche d'entreprises » (recherche-entreprises.api.gouv.fr, alimentée par l'INSEE/INPI), ouverte avec WebFetch. Elle donne le SIREN, le code NAF, la tranche d'effectif salarié (codes INSEE) et, quand les comptes sont publiés (non confidentiels), le chiffre d'affaires (CA) et le résultat net de la dernière année déposée. Statut : PAGE LUE.
  - Codes de tranche d'effectif INSEE utilisés : 00 = 0 salarié ; 01 = 1-2 ; 02 = 3-5 ; 03 = 6-9 ; 11 = 10-19 ; 12 = 20-49 ; 21 = 50-99 ; 22 = 100-199 ; 31 = 200-249 ; 32 = 250-499 ; 41 = 500-999 ; NN = non renseigné.
  - `finances: null` = aucun compte publié dans la base (comptes confidentiels, non déposés ou société non commerciale). Cela ne dit rien de la rentabilité.
- Pappers renvoie 403 : non utilisé. Les extraits Pappers/societe.com vus en résultat de recherche ont le statut EXTRAIT.
- Rappel : le CA et le résultat d'une société d'exploitation ne disent rien de la fortune du propriétaire, et inversement.

## 1. Données de registre, échantillons et premières fiches

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

### 1.B Échantillon systématique : châteaux-hôtels avec comptes publiés

Méthode : registre officiel filtré sur le mot « château », le code NAF 55.10Z (hôtels) et un CA ≥ 1 M€ [R4-34] [R4-35]. 105 sociétés répondent. J'ai relevé les 33 sociétés des deux premières pages dont le nom désigne clairement un château-hôtel (exclues : un hôtel parisien, une résidence de tourisme, l'hôtel d'HEC, des groupes hôteliers). Données : dernière année publiée (2017 à 2025 selon la société). Calcul Python sur les chiffres lus (fichier de travail dans le scratchpad).

| Indicateur (33 châteaux-hôtels, CA ≥ 1 M€) | Valeur | Statut |
|---|---|---|
| Sociétés en perte nette la dernière année publiée | 20 sur 33 (61 %) | ESTIMATION (calcul sur PAGE LUE) |
| CA médian | 2,18 M€ | ESTIMATION |
| Marge nette médiane (résultat net / CA) | -6,3 % | ESTIMATION |
| Sous-échantillon des comptes 2023-2025 (26 sociétés) | 14 en perte ; marge nette médiane -4,5 % | ESTIMATION |
| Résultat net cumulé hors Messardière (32 sociétés) | -14,6 M€ pour 103,4 M€ de CA cumulé | ESTIMATION |

Exemples (CA / résultat net, en €, année) — PAGE LUE [R4-34] [R4-35] :
- Pertes lourdes : Château de Saint-Sylvestre (47) 2 038 158 / -2 704 803 (2025) ; Hôtel Château Landon (35) 1 456 887 / -2 276 529 (2023) ; Château Margui Holdings (83) 4 152 917 / -4 170 429 (2025) ; Château Saint-Jean & Spa (Montluçon, 03) 2 698 066 / -1 769 348 (2024) ; Château de Grand-Lucé (72) 1 876 596 / -1 098 989 (2024) ; Château Louise & Louis (37) 2 429 145 / -1 196 730 (2025) ; Château Lafaurie-Peyraguey hôtel-restaurant (33) 3 815 732 / -635 473 (2025) ; Château des Vigiers golf (24) 6 827 590 / -504 894 (2025, 50 à 99 salariés).
- Rentables : Château de la Messardière (Saint-Tropez) 58 120 817 / +7 941 954 (2024) ; Château Saint-Martin & Spa (Vence) 11 423 480 / +924 751 (2024) ; Château de Villiers-le-Mahieu (78, séminaires, 50 à 99 salariés) 11 134 957 / +1 246 209 (2025) ; Hôtelière Château Bougon (44) 4 378 676 / +477 830 (2025) ; Hostellerie du Château de Fère (02) 1 340 118 / +308 614 (2025) ; Château Les Reynats (24) 2 095 620 / +162 108 (2024).
- Sociétés fermées (état « C ») dans l'échantillon : Château de Roussan (13), Château de Locguénolé (56), Château de Beaulieu (37), Château D L P (21) [R4-35]. La fermeture administrative ne prouve pas une faillite (vente, fusion ou cessation volontaire possibles).

Lecture (ESTIMATION) : un château-hôtel isolé de 1 à 7 M€ de CA est **plus souvent déficitaire que rentable** au niveau du résultat net. Les cas rentables sont soit très grands et situés sur des marchés de luxe littoraux (Saint-Tropez, Vence), soit des châteaux de séminaires proches de Paris avec un fort volume (Villiers-le-Mahieu). Limites : biais de sélection (seules les sociétés qui publient leurs comptes ; nom contenant « château » ; tri par pertinence de l'API), années hétérogènes, résultat net après amortissements et frais financiers (il ne mesure ni l'EBE ni la trésorerie ; un propriétaire peut financer les pertes par compte courant).

### 1.C Échantillon : lieux de réception et séminaires (NAF 82.30Z)

PAGE LUE [R4-37] (CA / résultat net, €) :
- Château Saint-Just (Belle-Église, 60) : 10 175 439 / +2 273 984 (2025).
- Château de Méry (Méry-sur-Oise, 95) : 5 069 906 / -562 515 (2024).
- Château de la Bussière (21) : 2 477 139 / -929 093 (2023).
- Places of Events (Château de Rajat, 69) : 1 075 761 / +19 061 (2023), 3 à 5 salariés.
- Les Kasteliades (71) : 701 564 / +3 (2023).
- Château Duvivier (83) : 312 489 / -86 550 (2023).
- CHATEAUFORM' FRANCE (réseau de châteaux et maisons de séminaires) : 186 366 960 / +3 406 336 (2025), tranche 22 = 100 à 199 salariés (tranche telle qu'inscrite). Marge nette ≈ 1,8 % (ESTIMATION). Modèle d'opérateur spécialisé, à creuser par R7.
- Château de Valmy (Argelès, 66 ; NAF 68.20B) : 1 746 064 / -726 220 (2024) [R4-38].

### 1.D Échantillon : haras et écuries privés avec comptes publiés

PAGE LUE [R4-26] [R4-39] [R4-40] (CA / résultat net, €) :
- SARL DE CHAMBURE (Étreham, 14 ; NAF 01.43Z élevage de chevaux ; gérants Éric et Nicolas Pelletier de Chambure ; 20 à 49 salariés) : 12 962 066 / -384 707 (2024). Le lien avec le « Haras d'Étreham » repose sur le siège à Étreham et la famille dirigeante : ESTIMATION à confirmer.
- Haras de Hus (Petit-Mars, 44 ; NAF 85.51Z) : 1 770 735 / -2 936 478 (2024).
- Écurie Haras Bouquetot (Clarbec, 14 ; dirigeants qataris) : 2 100 850 / -3 832 332 (2025).
- Haras de Beaumont (Allauch, 13) : 5 329 898 / -1 784 625 (2025).
- Rentables, de taille modeste : Haras du Cadran (61) 2 508 281 / +230 103 (2025) ; SARL Haras du Berlais (86) 2 090 585 / +300 127 (2025) ; Haras du Bois Margot (77) 1 217 830 / +308 961 (2022) ; Haras de la Vallée des Haflinger (72) 1 456 870 / +34 876 (2024) ; Écurie Alexis Grimault (53) 914 128 / +223 872 (2024).

Domaines équestres privés (registre, PAGE LUE) [R4-92] [R4-93] :
- LE HARAS DE LA CENSE (SARL, Rochefort-en-Yvelines, NAF 85.51Z, 10 à 19 salariés, commissaire aux comptes) : résultat net 2025 = +4 960 € (CA non lisible) ; il s'appuie sur un restaurant, une ancienne société d'hébergement et **un fonds de dotation créé en 2018 (LA CENSE FONDS DE DOTATION)**.
- DOMAINE EQUESTRE DE LA BONDE (Saint-Denis-le-Ferment, 27 ; NAF 55.10Z hôtel ; 10 à 19 salariés) : CA 2024 = 2 120 767 € ; résultat net = +105 361 € (≈ 5 %). Exemple rare d'hébergement équestre rentable (modestement).
- VILLAGE EQUESTRE (Le Val-Doré, 27 ; NAF 93.29Z ; 10 à 19 salariés) : CA 2023 = 1 304 982 € ; résultat net = -183 409 €.

Lecture (ESTIMATION) : trois grandes structures équestres « vitrines » affichent des pertes de 1,8 à 3,8 M€ par an, supérieures à leur CA dans deux cas. Des pertes de cette ampleur ne peuvent être couvertes que par les associés : c'est de la consommation de fortune, pas un modèle d'autofinancement. Les structures rentables sont des entreprises de taille moyenne (1 à 2,5 M€ de CA), spécialisées (élevage, valorisation, pension), sans château à porter.

### 1.E Fiches détaillées par cas

#### Cas 1 — Domaine de Chantilly (60) : le modèle « mécène unique », et ce qui se passe quand il part

- **Statut et propriété** : domaine « légué en 1884 à l'Institut de France par le duc d'Aumale », avec « un parc de 140 ha dessiné par André Le Nôtre » (réponse ministérielle, JO Sénat 10/09/2020) [R4-45]. Gestion confiée à la FONDATION POUR LA SAUVEGARDE ET LE DEVELOPPEMENT DU DOMAINE DE CHANTILLY (SIREN 488607581, fondation, NAF 91.03Z, aucun compte dans le registre) [R4-29]. PAGE LUE.
- **Mécénat** : partenariat depuis 2006 avec la fondation présidée par l'Aga Khan, avec « un investissement de 30 M sur la période 2006-2025 » (unité monétaire non affichée sur la page, vraisemblablement des euros) [R4-45]. PAGE LUE. Un résultat de recherche indique que le prince aurait « injecté 70 millions d'euros dans la restauration » avant de dissoudre la fondation en 2020 [R4-47/R4-48]. EXTRAIT. **Divergence non résolue : 30 M€ d'engagement prévu (source officielle) contre 70 M€ effectivement injectés (presse)**. Les deux peuvent être vrais (engagement initial dépassé), mais je ne l'ai pas vérifié.
- **Départ du mécène** : la fondation a annoncé fin 2019 son retrait et « s'est engagée à solder les opérations en cours à l'issue de la convention de partenariat en 2025 » [R4-45]. Le sénateur de l'Oise écrit qu'après « quinze ans d'un soutien financier exceptionnel », « l'investissement de l'État et des collectivités ne peut raisonnablement compenser ce départ » [R4-45]. PAGE LUE. Time Out (2026) parle de « l'arrêt du financement par l'Aga Khan fin 2020 » [R4-46]. PAGE LUE.
- **Soutien public** : l'État (DRAC) s'est engagé sur dix ans après 2016 pour « 0,8 M par an », soit « 40 % du montant des travaux envisagés » [R4-45]. PAGE LUE. La réponse ministérielle invite l'Institut à « développer des activités génératrices de revenus » et cite l'étude d'un hôtel dans le château d'Enghien, en concession à un opérateur privé [R4-45].
- **Exploitation** : « les 658 000 visiteurs ont généré 12,7 millions d'euros de recettes » (année 2025, chiffre de The Independent repris par Time Out, 09/02/2026) [R4-46]. PAGE LUE (source secondaire). Soit ≈ 19,3 € de recettes par visiteur (ESTIMATION : 12,7 M€ / 658 000).
- **Déficit** : « 13 M€ de charges annuelles pour les frais généraux et le personnel » et « un déficit d'exploitation de 6 M€ en 2020 », d'après l'administrateur général de l'époque [R4-47]. EXTRAIT (année de crise sanitaire, non représentative).
- **Besoin de restauration** : « 68 millions d'euros seront nécessaires au cours de la prochaine décennie », dont « 22,9 millions d'euros » pour le château principal et « 33 millions » pour des « urgences structurelles » [R4-46]. PAGE LUE. Soit ≈ 6,8 M€/an de travaux sur 10 ans (ESTIMATION), à rapprocher des 12,7 M€ de recettes annuelles.
- **Équestre** : Grandes Écuries (« ouvrage d'art imaginé par Louis-Henri de Bourbon, VIIe prince de Condé, en 1719 ») et musée du Cheval ; lignée d'écuyers jusqu'à Yves Bienaimé ; spectacle créé en 2019 pour le tricentenaire, joué « du 12 septembre au 31 octobre 2021 » (Revue Conflits, 26/09/2021) [R4-90]. PAGE LUE. Résultats de recherche (EXTRAIT [R4-91]) : spectacle d'été 2025 « Kalendae » du 12 juillet au 17 août, quatre jours par semaine à 14 h 30 ; distribution de huit cavaliers, une voltigeuse et des acrobates, quinze chevaux, cinq poneys et un âne ; tarifs 2024 : 24 € plein / 19 € réduit, 32 € / 26 € avec le château. **Coût de la cavalerie, CA du spectacle, fréquentation du musée : INCONNUS.** Lecture (ESTIMATION) : à Chantilly, le cheval est un **produit de visite** intégré au billet, avec une troupe d'une vingtaine d'équidés ; c'est un modèle de spectacle à forte fréquentation, pas d'écurie privée.
- **Ce qui est transposable** : même avec ≈ 650 000 visiteurs et plus de 12 M€ de recettes, un très grand domaine patrimonial n'autofinance ni ses charges courantes en période de crise ni son gros entretien. Le modèle a reposé sur un mécène unique pendant environ 15 ans ; son départ a ouvert un trou que ni l'État ni les collectivités ne comblent. **Leçon : la dépendance à une source unique (fortune d'un mécène) n'est pas un modèle durable.**

#### Cas 2 — Domaine des Étangs (Massignac, 16) : hôtel de luxe sur un très grand domaine, pertes couvertes par une fortune familiale

- **Propriété et histoire** : « Garance Primat and her seven siblings grew up playing ball games on the castle lawns » ; la famille a « opened up their holiday home as a hotel in 2015 » ; Garance Primat est la fille du milliardaire Didier Primat (Robb Report, 22/11/2023) [R4-49]. PAGE LUE.
- **Taille** : « Set on 1,012 hectares » ; « A boutique resort of just 17 rooms, suites, and cottages » ; « six restored barns » ; « the property's 600-strong herd of ginger-coated Limousin cows » ; le château « became Auberge Resorts' first property in France in April » (année non précisée dans l'article de novembre 2023) [R4-49]. PAGE LUE. Divergence : Country Life annonçait 29 chambres [R4-50] (EXTRAIT), contre 17 pour Robb Report en 2023.
- **Comptes (registre)** [R4-08] PAGE LUE :
  - Société hôtelière DOMAINE DES ETANGS (SAS, SIREN 814032967, NAF 55.10Z, 20 à 49 salariés) : **CA 2025 = 3 468 619 € ; résultat net 2025 = -3 203 191 €**.
  - Société agricole DOMAINE DES ETOILES (SAS, SIREN 572046852, NAF 01.42Z élevage de bovins, 10 à 19 salariés, présidente de la société hôtelière) : **CA 2024 = 1 823 631 € ; résultat net 2024 = -4 357 639 €**.
  - Les deux sociétés ont un commissaire aux comptes (In Extenso IDF Audit).
- **Lecture** (ESTIMATION) : en additionnant les dernières années publiées (2025 pour l'hôtel, 2024 pour l'agriculture, donc pas la même année), le domaine perd de l'ordre de **7,6 M€ par an** pour ≈ 5,3 M€ de CA. La perte de l'hôtel (-3,2 M€) est presque égale à son CA (3,5 M€). Un hôtel de 17 à 29 clés, même au sommet du marché, ne finance pas un domaine de 1 000 ha avec cheptel et bâtiments restaurés : il est financé par la fortune familiale. Les amortissements des lourds investissements de rénovation expliquent probablement une part des pertes (HYPOTHÈSE non vérifiée, comptes détaillés non consultés).
- **Transposable** : non comme modèle de financement. Utile comme borne : l'hôtellerie ultra-luxe sur domaine isolé, même adossée à une marque internationale (Auberge), reste structurellement déficitaire à cette échelle.

#### Cas 3 — Château d'Ygrande (Allier) : hôtel + centre équestre, liquidation en 2025 (ÉCHEC)

- **Le lieu** : « un domaine de quarante hectares », « 26 boxes », chambres « à partir de » 90 € à 190 €, « Séjour équestre : 126 € par personne » (site du domaine consulté le 2026-10-14) [R4-23]. PAGE LUE.
- **Structure** : deux sociétés au même siège (« Le Mont, 03160 Ygrande ») et avec le même gérant (Pierre-Marie Tissier) [R4-09] [R4-11] :
  - GROUPE COEUR ET DETENTE (SAS, SIREN 421318247, créée le 1998-12-21, NAF 55.10Z hôtels, tranche 12 = 20 à 49 salariés en 2024, catégorie PME ; dernier résultat publié : -102 330 € en 2022, CA non publié) [R4-22]. PAGE LUE.
  - EARL ECURIES DU CHATEAU D'YGRANDE (SIREN 820732873, NAF 85.51Z enseignement sportif, 6 à 9 salariés), éditrice du site internet [R4-10] [R4-24]. PAGE LUE.
- **Procédure collective** (BODACC) [R4-18] PAGE LUE : « Jugement d'ouverture de liquidation judiciaire » du **28/10/2025**, tribunal de commerce de Cusset ; « date de cessation des paiements le 01 Septembre 2025 » ; liquidateur SELARL MJ de l'Allier ; état des créances déposé le 16/09/2026. Le BODACC liste 17 avis de dépôt des comptes publiés entre 2009 et 2025 (pas d'avis en 2011, 2013, 2015 ni 2024). Un moteur juridique privé titre « GROUPE COEUR ET DETENTE (CHATEAU D'YGRANDE) Liquidation judiciaire » [R4-25] (EXTRAIT), ce qui confirme le rattachement de la société au château.
- **Situation actuelle** : le site internet, édité par l'EARL équestre (non liquidée), propose toujours chambres et séjours équestres [R4-23] [R4-24]. Repreneur, montant du passif, cause de la défaillance : **INCONNU**. Vérification : presse régionale (La Montagne), état des créances au greffe de Cusset, annonces de cession du liquidateur.
- **Leçon** (ESTIMATION) : la combinaison hôtel + équitation sur un domaine de 40 ha en zone rurale peu touristique n'a pas suffi à faire vivre une société de 20 à 49 salariés. Le schéma « deux sociétés » (hôtel / écuries) a permis à l'activité équestre de survivre à la liquidation de l'hôtel : séparer juridiquement les activités limite la contagion d'un échec.

#### Contexte — Ce que disent les propriétaires de monuments privés eux-mêmes (La Demeure Historique)

Documents de plaidoyer (donc orientés), mais ce sont les seules données agrégées trouvées. PAGE LUE (texte extrait des PDF) [R4-51] [R4-52].
- **Reventes rapides** : 2017 : « Actuellement, plus de 1 000 monuments historiques sont en vente sur le territoire, et la durée moyenne de détention se réduit à 7 ans après l'acquisition d'un monument historique, du fait des difficultés croissantes que rencontrent les porteurs de projets » [R4-52]. 2022 : « En quelques années, le nombre de monuments à vendre sur le territoire est passé de 800 à 1 500, et la durée moyenne de détention se réduit (de l'ordre de 7 ans) » [R4-51]. **La méthode de calcul de ces 7 ans n'est pas publiée** : chiffre déclaratif d'une association, à ne pas traiter comme une statistique officielle. Pour mémoire, le régime fiscal MH impose depuis 2009 un « engagement durable de conservation de 15 ans » [R4-51] : un engagement deux fois plus long que la détention moyenne alléguée.
- **Rentabilité** : les propriétaires-gestionnaires sont « en grande majorité très déficitaires, en particulier en milieu rural » ; les visites culturelles sont « le plus généralement déficitaires compte tenu notamment des coûts d'entretien et de restauration » ; « Pour être rentable, un monument historique privé doit se réinventer, trouver un nouvel usage, voire même développer plusieurs activités » [R4-52]. Le même document mentionne des prix faussés par « quelques achats « coup de cœur » de divers « oligarques » qui peuvent supporter d'importants déficits » [R4-52] : la DH distingue elle-même fortune et rentabilité.
- **Ordres de grandeur** : 45 275 monuments historiques, dont « 45 % de ce patrimoine protégé » appartient à des personnes privées (Chiffres-clés 2021 du ministère) ; « 9 millions de visiteurs accueillis dans près de 1 500 monuments et jardins historiques privés » [R4-51]. Soit **≈ 6 000 visiteurs par an en moyenne par monument privé ouvert** (ESTIMATION : 9 000 000 / 1 500). Au regard de ce chiffre, Vaux (≈ 300 000) et Chantilly (≈ 658 000) sont des exceptions extrêmes.
- **Aide publique par monument** : dépense fiscale MH « évaluée dans le projet de loi de finances 2022 à environ 35 millions d'euros, ce qui représente moins de 1 750 euros par an en moyenne par monument historique privé » [R4-51]. Part des crédits MH allant aux monuments privés : 7,9 % en 2012, 12,1 % en 2016, 9,8 % en 2019 [R4-51].
- **Étude « Tournelle »** (DH, 2010) : recettes et charges de 513 monuments déclarées confidentiellement par les adhérents ; seules des conclusions agrégées sur les flux fiscaux sont publiées (déductions ≈ 44 M€ ; impôts et cotisations versés ≈ 89 M€) [R4-52]. Les comptes d'exploitation moyens d'un monument privé ne sont pas publiés : INCONNU. Vérification : demander l'étude complète à la DH (contact interdit pour cette mission).
- **Cas « Monsieur N. »** (exemple anonyme de la DH) : visite seule « déficitaire », transformation des communs en salle de réception, litige avec la commission de sécurité ERP de plus de deux ans, « Plus de 100 000 euros ont été investis dans les travaux de mise en conformité » ; le propriétaire dit qu'il aurait été « obligé de vendre le château » sans compromis [R4-52]. Illustration directe de la leçon 6 du contexte (ERP).
- La DH regroupait en 2017 « plus de 3 000 châteaux, manoirs, abbayes ou hôtels particuliers, dont 1 300 sont aujourd'hui ouverts au public » [R4-52].

#### Cas 4 — Château de la Motte-Husson (Martigné-sur-Mayenne, 53) : le château comme décor d'une entreprise de médias

- **Achat** : « In 2015, for £280,000 (equivalent to £386,777 in 2025), they purchased a chateau » ; « on a 12-acre (4.9-hectare) property, that listed forty-five rooms, seven outbuildings and a walled garden » (Wikipedia EN, phrase sans note) [R4-44]. PAGE LUE, fiabilité moyenne.
- **Activités** : lieu de mariages et d'événements dont la notoriété vient en partie de l'émission ; activité d'accueil d'Angel (« The Vintage Patisserie ») transférée au château en 2015 ; séries dérivées (« Escape to the Chateau DIY », où le couple conseille d'autres expatriés « trying to run businesses from châteaux ») ; podcast ; livres [R4-44] ; l'éditeur présente le lancement de leur « wedding business » [R4-61] (EXTRAIT, texte promotionnel). L'émission a été présentée comme terminée après la saison 9, puis « in October 2025, a tenth series was announced » [R4-44]. PAGE LUE.
- **Structure (registres)** :
  - Royaume-Uni [R4-55] à [R4-60], PAGE LUE : CHATEAU-DE-LA-MOTTE HUSSON LIMITED (n° 10674609), constituée le 16/03/2017, **dissoute le 08/08/2023**, derniers comptes au 30/09/2021, mode de dissolution non indiqué ; ESCAPE TO THE CHATEAU LIMITED (n° 12032099), constituée le 04/06/2019, SIC 58110 « Book publishing », ex-« The Chateau Publishing Limited » jusqu'au 24/06/2025 ; CHATEAU TELEVISION LIMITED (n° 12462133), constituée le 13/02/2020, comptes « Total exemption full accounts » (comptes abrégés, sans compte de résultat public), contrôlée depuis le 05/04/2023 par la holding « Da2Ad Limited ».
  - France [R4-21], PAGE LUE : SARL DA2AD (SIREN 912302825, créée le 06/04/2022, NAF 93.29Z, gérants Angela et Richard Strawbridge), résultat net 2023 = 5 632 € (CA non publié) ; Angela Strawbridge en entreprise individuelle de location (NAF 68.20B).
- **Chiffre d'affaires, rentabilité des mariages** : **INCONNU**. Les comptes britanniques sont abrégés et le document des comptes n'a pas pu être ouvert (redirection vers un stockage signé). Vérification : télécharger manuellement les comptes de Chateau Television Ltd sur Companies House.
- **Difficultés publiques** (The Independent, 20/05/2023) [R4-94] PAGE LUE : l'émission a duré « nine seasons beginning in 2016 and ending in December 2022 » ; Channel 4 a annoncé : « Following a review, we have taken the decision not to work with Dick and Angel on any new productions in the future », après une « independent HR investigation » demandée à la suite d'inquiétudes du producteur Two Rivers Media ; des sources évoquaient « a deteriorating relationship between Two Rivers and Dick and Angel's Chateau TV » ; en 2021, d'anciens membres de la société de production Spark Media avaient accusé le couple de harcèlement (« anxiety-inducing ordeal »), ce que le couple a démenti. Aucune procédure judiciaire ni difficulté financière n'est mentionnée. La même rupture est titrée « Channel 4 drops Escape to the Chateau stars Dick and Angel Strawbridge after bullying claims » par la presse régionale britannique [R4-95] (EXTRAIT). Une dixième saison a été annoncée en octobre 2025 (Wikipedia, citant le site du couple thechateau.tv) [R4-44] : le couple semble être passé à une diffusion par ses propres moyens (ESTIMATION). La dissolution le 08/08/2023 de la société britannique portant le nom du château est un fait de registre, sans cause connue [R4-60].
- **Risque révélé** (ESTIMATION) : un modèle fondé sur la notoriété télévisuelle dépend d'un **diffuseur** et de relations de travail tendues avec des équipes de tournage ; la rupture avec Channel 4 en 2023 a coupé le canal principal. Ce n'est pas une faillite, mais c'est la fragilité principale du modèle.
- **Leçon** (ESTIMATION) : le moteur économique n'est pas le château mais la **notoriété audiovisuelle** (télévision, livres, produits, podcast). Les mariages profitent de cette notoriété. Ce modèle n'est pas transposable à un propriétaire qui veut préserver sa vie privée : il exige une exposition médiatique permanente de la famille.

#### Cas 5 — Château de Gudanes (Château-Verdun, 09) : restauration financée par un revenu professionnel extérieur

- **Origine** : Karina et Craig Waters, australiens, arrivés en 2013 ; château « classified as a ruin and listed as a class one historic building » ; « the roof had collapsed, taking out five storeys in places » ; 12 acres (≈ 4,9 ha) de terrain ; travaux commencés en décembre 2013 (The Connexion, 2022, mis à jour 2025) [R4-54]. PAGE LUE. Prix d'achat : non communiqué par les propriétaires (INCONNU).
- **Financement** : « Craig, a doctor, spends most of his time in Australia working so we can pay for it all » ; recettes d'un livre (publié en octobre 2018, « nearly over 10,000 copies ») réinvesties : « The money goes towards ongoing works » ; depuis 2018, séjours de trois à sept nuits et ateliers [R4-54]. Audience : « 380,000 followers on Instagram and 408,000 on Facebook » [R4-54]. PAGE LUE.
- Wikipédia FR n'a pas d'article sur ce château (404) [R4-43].
- **Registre** [R4-20] PAGE LUE : SAS CHATEAU DE GUDANES (SIREN 106121783) créée seulement le **22/05/2026**, NAF 55.20Z (hébergement touristique de courte durée), présidée par Karina Waters ; SCI LES TORRENTS D'ASTON (2013) au nom du couple.
- **Difficultés** : aucune source trouvée sur des dettes, un arrêt du chantier ou une vente (une recherche). Le seul obstacle documenté est administratif (visa) [R4-54]. Pas d'échec démontré.
- **Leçon** (ESTIMATION) : le château est porté par un **moteur extérieur** (revenu médical en Australie) complété par la notoriété numérique ; c'est une illustration de l'hypothèse H8 (moteur hors domaine), mais avec une dépendance totale au travail d'une seule personne.

#### Cas 6 — Château de la Mothe-Chandeniers (Les Trois-Moutiers, 86) : le financement participatif

- **Acquisition** : « Le prix d'achat du château est de 500 000 euros, somme atteinte le 1er décembre 2017 » (Wikipédia, citant Le Point du 04/12/2017) ; clôture de la campagne le 25/12/2017 avec « plus de 1 617 000 euros et 18 558 contributeurs de 115 pays » ; deuxième campagne (chapelle et ≈ 2,1 ha de parc) close en juin 2018 « avec plus de 474 000 euros récoltés » ; troisième campagne en décembre 2020 [R4-41] (article de France 3 cité par Wikipédia, non accessible [R4-64]). PAGE LUE (source secondaire). Fin 2024 : « près de 4 400 000 € » collectés au total et « 25000 co-châtelains de 183 pays » (Paris ZigZag, mis à jour le 09/12/2024) [R4-62]. PAGE LUE.
- **Structure** : SAS CHATEAU DE LA MOTHE-CHANDENIERS (SIREN 835113820), présidée par la société Dartagnans, commissaire aux comptes nommé, 6 à 9 salariés (2024) [R4-19]. **Capital social inscrit : 1 050 € (2018), 5 529,45 € (2019), 12 943,05 € (avril 2026)** [R4-63] : l'essentiel des sommes versées par les « co-châtelains » n'est donc pas du capital social (prime d'émission ou autre forme ; la ventilation est INCONNUE). Comptes 2024 déposés avec une « déclaration de confidentialité » [R4-63]. PAGE LUE.
- **Travaux** : phase 1 avec « un budget prévisionnel de 850 000 euros » (mise en sécurité, cour, tour de l'horloge, escalier d'honneur), démarrée en janvier 2019 ; durée totale des travaux estimée à 7 ans (projection de 2019) [R4-41]. Avancement réel depuis 2019 : INCONNU.
- **Exploitation** : visites ouvertes fin juin 2018 ; 4 296 visiteurs en 2018 et 15 000 en 2019 [R4-41] ; « quatre écolodges » « à partir de 135€ la nuit » ; « des milliers de visiteurs chaque année » [R4-62]. PAGE LUE. CA et résultat : INCONNUS (comptes confidentiels).
- **Lecture** (ESTIMATION) : le financement participatif a très bien fonctionné pour **l'achat et les premières urgences** (≈ 4,4 M€ en sept ans, soit ≈ 0,6 M€ par an en moyenne), grâce à un récit médiatique exceptionnel. Il ne finance pas un fonctionnement courant : il faut relancer des campagnes. Ce succès a été obtenu sur une ruine romantique, pas sur une résidence privée ; il n'est pas transposable à un domaine où le propriétaire veut garder l'usage privé.

#### Cas 7 — Haras national du Pin (Orne) : un domaine équestre historique que l'État n'a pas su rentabiliser

- **Le lieu** : « Versailles du cheval », château construit de 1715 à 1730 ; « Il attire chaque année près de 50 000 visiteurs » (Acteurs publics, 22/02/2012) [R4-65]. PAGE LUE. Surface « 1100 hectares » d'après un résultat de recherche (source ancienne) [R4-66/67] : EXTRAIT.
- **Retrait de l'État** : en 2012, réforme des haras nationaux avec « Des missions non rentables appelées à être privatisées ou à disparaître » ; « Au haras national du Pin, l'étalonnage devrait être repris par le privé » ; le président du conseil général de l'Orne propose que le haras « soit transféré aux collectivités locales » [R4-65]. PAGE LUE.
- **Structures successives (registre)** [R4-16] PAGE LUE : établissement public « HARAS NATIONAL DU PIN » (SIREN 130021231) créé le 04/07/2015, **fermé le 30/06/2022** ; « SYNDICAT MIXTE DU HARAS NATIONAL DU PIN » (SIREN 200102689) créé le **01/01/2024**. D'après un résultat de recherche citant l'étude d'impact d'un projet de loi de 2020, l'EPA devait être dissous, ses biens mobiliers transférés au département de l'Orne et ses immeubles à l'État [R4-66]. EXTRAIT.
- **Budget** : un document du ministère de l'Agriculture donnerait un budget prévisionnel 2016 « d'environ 1,16 million d'euros » en dépenses et en recettes [R4-67]. EXTRAIT, non vérifié. Plus de 7 M€ investis depuis 2010 par la Région (2,2 M€) et le Département (4 M€), le reste par l'État (phrase tronquée) : EXTRAIT. Budget actuel, déficit, effectif : **INCONNU**. Vérification : délibérations du conseil départemental de l'Orne, budget du syndicat mixte.
- **Leçon** (ESTIMATION) : même un domaine équestre prestigieux de plus de 1 000 ha avec château, ≈ 50 000 visiteurs et des événements de niveau international a été jugé « non rentable » par l'État et transféré, après dix ans d'instabilité institutionnelle, à un syndicat de collectivités. Les chevaux et le patrimoine y sont un **service public subventionné**, pas une activité qui finance le domaine.

#### Cas 8 — Pôle international du cheval Longines (Goustranville, Calvados) : équipement public d'événements équestres

- **Structure** : SAEML POLE INTERNATIONAL DU CHEVAL (SIREN 508592342, société d'économie mixte créée le 01/10/2008, NAF 93.19Z, 10 à 19 salariés). Administrateurs : élus, CCI Seine Estuaire, comité régional d'équitation de Normandie, banque CIC Nord Ouest, une agence de services hippiques ; commissaire aux comptes KPMG [R4-15]. PAGE LUE.
- **Comptes** : **CA 2024 = 1 943 816 € ; résultat net 2024 = -259 557 €** [R4-15]. PAGE LUE.
- **Lecture** (ESTIMATION) : un site d'événements équestres de niveau international, construit par la puissance publique, réalise moins de 2 M€ de CA et reste déficitaire **sans même porter le coût de son investissement initial** (non connu ici). L'événementiel équestre seul ne finance pas des installations lourdes.

#### Cas 9 — Haras de Jardy (Marnes-la-Coquette, 92) : centre équestre public

- Données faibles (Wikipédia avec bandeau « sources insuffisantes ») [R4-68] : surface « 75 hectares » (ou « près de 90 hectares » selon un autre passage) ; « 2 500 cavaliers et 200 chevaux » ; golf de 9 trous et 20 courts de tennis ; acquis par l'État en décembre 1979, ouvert au public en 1981, « racheté par le Conseil général des Hauts-de-Seine en novembre 2006 ». PAGE LUE, fiabilité faible.
- Golf et tennis exploités par une société privée (GOLF ET TENNIS DES HARAS DE JARDY, SNC, 20 à 49 salariés, comptes non publiés) [R4-17]. Mode de gestion de la partie équestre, budget, redevance : **INCONNU**. Vérification : délibérations du conseil départemental des Hauts-de-Seine (contrat de délégation).
- **Leçon** (ESTIMATION) : les grands complexes équestres « vitrines » d'Île-de-France sont des équipements de collectivités. Jardy combine équitation de masse (2 500 cavaliers), compétitions et golf : c'est un modèle de **volume** aux portes de Paris, incompatible avec un domaine privé calme.

#### Cas 10 — Haras privés normands et autres haras (comptes publiés)

- Voir le tableau du § 1.D. SARL DE CHAMBURE (Étreham) : 12,96 M€ de CA et -0,38 M€ de résultat net en 2024 [R4-26]. C'est le plus gros CA équestre privé trouvé, mais il s'agit d'élevage et de commerce de pur-sang (étalons, ventes), un métier de spécialistes, à forte intensité de capital et très cyclique. Autres haras normands (registre, PAGE LUE) :
  - HARAS DU LOGIS SAINT GERMAIN (SIREN 452606981, Putot-en-Auge, NAF 01.43Z, 10 à 19 salariés) : **CA 2024 = 829 370 € ; résultat net 2024 = -718 297 €** [R4-70].
  - HARAS DE MONTAIGU (SIREN 813561172, Nonant-le-Pin, NAF 01.62Z, 10 à 19 salariés ; gérantes de la famille Guerlain) : comptes non publiés [R4-69].
  - SARL HARAS DU QUESNAY (SIREN 498560069, siège à Gouvieux, gérant Frédéric Head) : comptes non publiés [R4-71].
  - HARAS DE SON ALTESSE L'AGA KHAN (SIREN 341272698, Mézidon Vallée d'Auge, 20 à 49 salariés, commissaire aux comptes KPMG) : comptes non publiés ; le rattachement au haras de Bonneval est une ESTIMATION (requête « haras de bonneval ») [R4-72].
  - FRESNAY LE BUFFARD UAE (SIREN 993312693, Neuvy-au-Houlme) et WATHBA STUD FARM (SIREN 341611515, Ménil-Froger, 20 à 49 salariés), présidées par un même dirigeant émirien : comptes non publiés [R4-73].
  - Constat (ESTIMATION) : plusieurs des grands haras normands appartiennent à des fortunes étrangères ou dynastiques (Aga Khan, investisseurs des Émirats, propriétaires qataris de Bouquetot). Les seuls comptes publiés montrent des pertes (Étreham, Logis Saint-Germain, Bouquetot). L'élevage de pur-sang de haut niveau est un **usage de fortune**, pas une source de financement d'un domaine.

## 2. Échecs : liquidations judiciaires de châteaux-hôtels, lieux de réception et centres équestres (BODACC, 2023-2026)

Méthode : interrogation du BODACC officiel (API open data de la DILA) : procédures collectives publiées depuis le 01/01/2023, nom contenant « château », jugement contenant « liquidation ». 327 annonces au total, dont une majorité sans rapport (épiceries « Château Rouge », Châteaubriant, garages…) et de nombreuses exploitations viticoles bordelaises [R4-74] [R4-75] [R4-76]. J'ai lu environ 250 annonces sur 327 (pages tronquées). Activités : telles que déclarées au BODACC (résumées par l'outil de lecture). PAGE LUE. **C'est une borne basse** : beaucoup de sociétés de châteaux n'ont pas « château » dans leur nom (exemple : Ygrande).

| Société (commune) | Activité déclarée | Événement BODACC (date du jugement) | Source |
|---|---|---|---|
| GROUPE COEUR ET DETENTE - Château d'Ygrande (03) | hôtel ; écuries dans une EARL séparée | liquidation judiciaire (28/10/2025) | [R4-18] |
| CHATEAU LA CAZINE (Noth, 23) | hôtels et hébergement similaire | résolution du plan et liquidation (21/10/2025) | [R4-75] |
| LE CHATEAU DE FRAMBOISE (Dumes, 40) | hébergement touristique | liquidation (10/10/2025), clôture pour insuffisance d'actif (24/04/2026) | [R4-74] [R4-75] |
| CHATEAU DE CHARFETAIN (Brullioles, 69) | hébergement touristique de courte durée | liquidation (10/07/2025), clôture pour extinction du passif (29/09/2026) | [R4-74] [R4-75] |
| CHATEAU DE LA MONTMARIE (Olliergues, 63) | hébergement touristique | liquidation (03/07/2025) | [R4-75] |
| CHATEAU SAINT MICHEL (Rully) | hôtels et hébergement similaire | extension de liquidation (27/02/2025) | [R4-75] |
| REVE DE CHATEAU (Barsac) | chambres et tables d'hôtes, réceptions, mariages | liquidation (30/04/2025), clôture pour insuffisance d'actif (05/01/2026) | [R4-74] [R4-75] |
| CHATEAU DE SALLES (Vézac) puis SALLESA | hôtellerie, restauration, formation, événements | conversion en liquidation (11/03/2025) ; SALLESA : conversion en liquidation (23/06/2026) | [R4-74] [R4-75] |
| CHATEAU DE SAINT PRIEST (Saint-Priest) | restauration, organisation d'événements | plan de cession puis conversion en liquidation (04/03/2025) | [R4-75] |
| SAS CBA - CHATEAU DE BEL AVENIR (La Chapelle-de-Guinchay, 71) | négoce de vins, hôtellerie, restauration | conversion en liquidation (28/02/2025) | [R4-75] |
| CHATEAU DE COLLIAS (30) | hôtel-restaurant | conversion en liquidation (27/01/2026) | [R4-74] |
| CHATEAU DESPLATS (Macau, 33) | restaurant-hôtel | liquidation (15/11/2023), clôture pour insuffisance d'actif (06/07/2026) | [R4-74] [R4-76] |
| CHARMING CHATEAU (Servian, 34) | hébergement touristique | clôture pour insuffisance d'actif (12/11/2025) | [R4-74] |
| UN PASSAGE AU CHATEAU (Varennes-lès-Mâcon, 71) | restaurant, séminaires, mariages, hébergement, chambres d'hôtes | liquidation (08/04/2024) | [R4-76] |
| ESPRIT DE CHÂTEAU (Paris) | traiteur, noces, banquets, réceptions | liquidation (04/10/2023), clôture pour insuffisance d'actif (02/04/2024) | [R4-76] |
| LE CHATEAU DES LYS (Paris) | traiteur et organisation d'événements | liquidation (18/09/2024), clôture pour insuffisance d'actif (30/09/2025) | [R4-75] [R4-76] |
| SAS CHATEAU DE FONTAGES (Onet-le-Château, 12) | hôtels et hébergement similaire | conversion en liquidation (05/07/2024) | [R4-76] |
| LE CHATEAU DE GARREVAQUES (Puylaurens, 81) | hôtels et hébergement similaire | conversion en liquidation (05/04/2024) | [R4-76] |
| LE CHATEAU DE BRICQUEBEC (50) | hôtels et hébergement similaire | clôture pour insuffisance d'actif (09/09/2024) | [R4-76] |
| SOCIETE HOTELIERE DU COTENTIN / CHATEAU DE QUINEVILLE SAS (50) | hôtels | extension de liquidation (13/10/2023) | [R4-76] |
| LE CHATEAU DE PRIVAT (Beaucaire) | club privé, hôtellerie, restauration | clôture pour insuffisance d'actif (13/12/2023) | [R4-76] |
| EARL SOCIETE HIPPIQUE DE TRIE CHATEAU (60) | centre équestre | liquidation simplifiée (21/05/2024), clôture pour insuffisance d'actif (10/03/2026) | [R4-74] [R4-76] |
| FONDS DE DOTATION CHATEAU ROYAL DE MONTARGIS (45) | fonds de dotation d'un château | conversion en liquidation (18/12/2025) | [R4-74] |
| DUPLESSIS / SA IDCL / association CHATEAUX EN VIE (Saint-Benin-d'Azy, 58) | réceptions et traiteur ; location de logements | extension de liquidation (26/11/2025) | [R4-74] |

Autres signaux (procédures collectives sans liquidation lue, ou dépôt de l'état des créances) : CHATEAU DE BRINDOS (Anglet, hôtel ; liste des créances 01/09/2026 ; comptes 2018 : CA 1,81 M€, perte 0,87 M€) ; CHATEAU DE LA BARGE (Chaintré, hôtel-restaurant ; avis de dépôt 21/05/2024) ; LE CHATEAU DE BUSSET (03, hôtel ; avis de dépôt 25/01/2024) [R4-74] [R4-76]. Domaines viticoles « château » en liquidation 2025-2026 (crise viticole) : Château de Piègue (49 : société d'exploitation, groupement foncier et holding, 06/05/2026), Château Lamothe (Cissac), Château Hourtin-Ducasse, Château Seguelongue, Château Menota, Château La Rayre, Château Lagarrigue, Château d'Hugues, entre autres [R4-74] [R4-75]. **Un domaine financé par un produit agricole peut lui-même faire faillite.**

Lecture (ESTIMATION) :
- Les défaillances touchent surtout des **châteaux-hôtels de taille moyenne** et des **lieux de réception / mariages / chambres d'hôtes** en zone rurale, et pas seulement des projets naissants (Château de la Barge et Château de Brindos publiaient déjà des comptes déficitaires en 2017-2018).
- Plusieurs dossiers passent par un plan (redressement, cession) avant la liquidation : l'échec est souvent lent.
- Il existe au moins un cas de **fonds de dotation de château** liquidé (Montargis) : la structure de dotation ne protège pas contre l'insuffisance de ressources.
- Je n'ai pas cherché les causes une par une (pas de budget de recherche) : elles sont **INCONNUES** dans ce fichier.

## 3. Fiches des grands domaines privés ouverts au public et des domaines financés par un produit

#### Cas 11 — Vaux-le-Vicomte (Maincy, 77) : le grand monument privé « autofinancé » à 300 000 visiteurs

- **Propriété** : branche cadette des Vogüé ; propriétaire inscrit « Société privée (SCI Valterre) », gérée par Ascanio de Vogüé avec ses frères Alexandre et Jean-Charles [R4-30] ; SCI VALTERRE : 50 à 99 salariés en 2024, commissaire aux comptes, comptes non publiés [R4-02]. PAGE LUE. Parc d'environ 500 ha « clos par un mur d'enceinte de 13 km » [R4-30]. Domaine de « près de 1 000 hectares » acheté en 1875 par Alfred Sommier [R4-30]. Ouvert au public en 1968 à l'initiative de Patrice de Vogüé (EXTRAIT [R4-86], source exacte non identifiée).
- **Budget et emploi** : « Soit 9 millions d'euros à trouver chaque année pour son entretien » ; « 10 % du budget annuel sont consacrés à l'entretien des jardins à la française » ; « seulement 4 % proviennent d'aides de l'État » (dossier de presse France 5, 2016) [R4-31]. Wikipédia : « un budget annuel de 8 millions d'euros, emploie 75 salariés à temps plein » (sans date ni note) [R4-30]. PAGE LUE. **Divergence 8 / 9 M€ conservée.** Un compte rendu universitaire indique que les charges de personnel représentent environ 41 % des dépenses et que billetterie, boutiques et restaurants sont la première ressource [R4-32] : EXTRAIT, fiabilité faible.
- **Fréquentation** : 261 000 visiteurs en 2008 [R4-30] ; « 300 000 visiteurs par an » (2016) [R4-31] ; objectif de 400 000 en 2020 (EXTRAIT [R4-86]).
- **Activités** : visite, soirées aux chandelles, restauration (« 600 personnes par jour en 2018 » [R4-30]), privatisations (mariages, dîners d'entreprise), tournages (plus de 30 films listés, de 1952 à 2026, et la série *Versailles*) [R4-30] [R4-31] ; mécénat de statues, de mobilier et parrainage d'arbres [R4-31] ; association des Amis (prêt de 60 objets grâce à 2 700 membres) [R4-30]. Société de restauration SERV : CA 2025 = 2 674 622 €, résultat net -2 475 € [R4-02].
- **Ratios (ESTIMATION)** : 8 à 9 M€ de budget pour ≈ 300 000 visiteurs, soit **27 à 30 € de dépense annuelle par visiteur** ; jardins ≈ 0,8 à 0,9 M€/an (10 %) ; personnel ≈ 3,3 à 3,7 M€/an si la part de 41 % est juste (non vérifié).
- **Transposable ?** Le modèle repose sur une notoriété mondiale (Fouquet, Le Nôtre), la proximité de Paris (Seine-et-Marne), 300 000 visiteurs et 75 salariés : **inaccessible** à un domaine sans ce rang. À retenir : même ici, l'aide publique ne couvre que ≈ 4 % des besoins, et la famille sépare monument, restauration, agriculture et immobilier dans des sociétés distinctes. La résidence privée cohabite avec une exploitation de masse, ce que le propriétaire de la mission ne souhaite pas.

#### Cas 12 — Chenonceau (37) : premier château privé de la Loire, gouvernance sous administration provisoire

- **Propriété** : famille Menier depuis 1913 (Wikipédia, partie historique) [R4-33]. Société civile CHATEAU DE CHENONCEAU (SIREN 775702509, créée en 1955) : 50 à 99 salariés (2024), associés Laure, Cosima, Henri et Pauline Menier (gérante), **administrateur provisoire inscrit : la société TRAJECTOIRE** [R4-05] [R4-01]. PAGE LUE.
- **Satellite publié** : CHENONCEAU CASTELLUM (restauration sur le site, gérante Pauline Menier) : **CA 2025 = 5 638 275 € ; résultat net = 1 108 319 €** (marge nette ≈ 19,7 %, ESTIMATION) [R4-05]. C'est le seul satellite de grand château privé trouvé avec une rentabilité nette élevée.
- **Fréquentation** : « appréciés chaque année par près de 900 000 visiteurs », « dont 40 % de visiteurs étrangers issus de 150 nationalités » (ministère de la Culture, DRAC Centre-Val de Loire, 11/07/2017) [R4-87]. PAGE LUE. Un résultat de recherche donne environ 800 000 visiteurs en 2007 (EXTRAIT). **CA du monument : INCONNU** (société civile, comptes non publiés). Deux recherches n'ont rien donné sur la gouvernance. Ratio (ESTIMATION) : le restaurant seul réalise ≈ 6,3 € de CA par visiteur (5,64 M€ / ≈ 900 000).
- **Difficultés** : la présence d'un administrateur provisoire au registre signale un blocage de gouvernance (ESTIMATION) ; cause et date : INCONNUES. Vérification : extrait Kbis / annonces BODACC de la société civile, presse régionale (La Nouvelle République).
- **Leçon** (ESTIMATION) : même un monument très fréquenté et rentable dans ses activités annexes reste exposé au **risque de gouvernance familiale** (indivision, succession, désaccords).

#### Cas 13 — Cheverny (41) : visite + chenil de vènerie + Tintin + orangerie événementielle

- **Faits** : ouvert au public en 1922 ; « la famille y habite toujours » ; « plus de 350 000 visites chaque année » ; fréquentation 340 000 (2011), 335 000 (2012), 331 650 (2013), 335 960 (2014), 337 640 (2015), 349 200 (2016) ; collection Tintin depuis 2001 ; orangerie restaurée en 1979 qui « accueille aujourd'hui congrès, séminaires, et mariages » ; parc de près de 100 ha ; meute de chiens de chasse [R4-84]. PAGE LUE (Wikipédia, sources citées : France 3, ADT 41). Selon l'ADT du Loir-et-Cher, la fréquentation 2023 de Cheverny est « non communiquée » [R4-36] (EXTRAIT).
- **Registre** [R4-03] PAGE LUE : SCI CHATEAU DE CHEVERNY (20 à 49 salariés, siège administratif à Paris, gérée par la société CHEVERNY GESTION) ; ORANGERIE DU CHATEAU DE CHEVERNY (SAS, 20 à 49 salariés ; résultat net 2024 = +147 063 €, CA non lisible) ; LES VIGNES DU CHATEAU DE CHEVERNY (2015) ; GIE de moyens (6 à 9 salariés) ; golf exploité par un tiers (CA 2025 = 1,46 M€, résultat -29 850 €).
- **Lecture** (ESTIMATION) : modèle de **grand site de visite familial** très diversifié (visite, exposition sous licence, événementiel d'entreprise, vigne, golf en concession), avec une famille résidente. La vènerie, activité équestre traditionnelle, y est une **attraction** et non une source de revenus en soi (aucun chiffre trouvé).

#### Cas 14 — Villandry (37) : les jardins comme produit

- **Faits** : jardins de « plus de six hectares agencés sur quatre niveaux de terrasses » ; propriété privée d'Henri Carvallo et de deux de ses sœurs ; reconstitution depuis 1906 par Joachim Carvallo [R4-85]. Joachim Carvallo a fondé La Demeure Historique en 1924 [R4-52]. PAGE LUE.
- **Registre** [R4-04] PAGE LUE : SCI DU CHATEAU DE VILLANDRY (20 à 49 salariés en 2024), comptes non publiés ; restaurant AU JARDIN DE VILLANDRY (6 à 9 salariés, résultat net 2024 = +18 286 €, CA non lisible).
- **Fréquentation, CA** : **INCONNU** (non trouvés). Vérification : communiqués du château, CRT Centre-Val de Loire.
- **Leçon** (ESTIMATION) : un jardin d'exception peut être le cœur du produit de visite, mais il exige une équipe permanente (20 à 49 salariés pour l'ensemble de la SCI).

#### Cas 15 — Breteuil (Choisel, 78) : petite équipe, visite familiale et vente d'un trésor national

- **Faits** [R4-82] PAGE LUE (Wikipédia, citant Le Figaro Magazine 2021 sans lien) : parc de 75 ha ; ouvert au public depuis 1967 « afin de payer les frais de restauration » ; 120 000 visiteurs par an avant la crise sanitaire ; 50 personnages de cire du musée Grévin illustrant les contes de Perrault ; réceptions et réunions professionnelles ; nombreux tournages ; pendant la crise sanitaire, « son équipe de dix employés » au chômage partiel, et en 2020 « Breteuil voit son chiffre d'affaires divisé par deux » ; projet de gîte reporté ; **en 2014, vente de la « table de Teschen », trésor national, acquise par le Louvre**.
- **Registre** [R4-13] PAGE LUE : exploitation en entreprise individuelle du propriétaire (FRANCOIS LE TONNELIER DE BRETEUIL, NAF 91.03Z, 6 à 9 salariés) ; restauration dans une petite SAS (CA 2019 = 53 369 €).
- **Lecture** (ESTIMATION) : 120 000 visiteurs avec une dizaine de salariés permanents ; la vente d'un meuble classé montre qu'un domaine familial peut devoir **céder du capital patrimonial** pour tenir. CA du domaine : INCONNU.

#### Cas 16 — Brissac (49) : le château-résidence ducal, événements et tournages

- **Faits** [R4-83] PAGE LUE : propriété et résidence des ducs de Brissac (Charles-André de Cossé-Brissac) ; classé MH ; ouvert au public ; marché de Noël, chasse aux œufs, festival de fleurs, départs de montgolfières (dont le championnat de France) ; tournages télévisés et cinéma (*Secrets d'Histoire* 2016 et 2018, un long métrage annoncé pour 2026).
- **Registre** [R4-06] PAGE LUE : exploitation en entreprise individuelle (CHARLES DE BRISSAC, NAF 91.03Z, 3 à 5 salariés) ; GROUPEMENT FORESTIER DOMAINE DE BRISSAC (1 à 2 salariés).
- **Fréquentation, CA** : **INCONNU**.
- **Lecture** (ESTIMATION) : structure très légère (3 à 5 salariés), revenus événementiels ponctuels et bois logés dans un groupement forestier (outil classique de transmission). Rien ne permet de juger l'équilibre financier.

#### Cas 17 — Courances (91) : parc, potager, polo, bien-être et maisons à louer

- **Faits** : parc de 86 ha classé « jardin remarquable », à 47 km de Paris ; décor de tournages (*Le Sens de la fête*, 2016 ; *Molière*, 2007) [R4-80]. Le site du domaine présente : visite du parc et du château, potager et plaine, salon de thé « La Foulerie », polo, « Vivier du Bien-être », « Le Fenil », hébergement (« Les Maisons de Courances », « La Cour de ferme »), séminaires et hébergements opérés par « Pierres d'Histoire » [R4-81]. PAGE LUE.
- **Registre** [R4-07] [R4-12] PAGE LUE : SCI DU PARC DE COURANCES (1976 ; 6 à 9 salariés ; comptes non publiés), LES MAISONS DE COURANCES (SCI, locatif), LES JARDINS DE COURANCES (EARL, maraîchage).
- **Agriculture** [R4-88] PAGE LUE : « a 600-hectare agricultural plain » ; « several market gardening plots (3 x 3 ha) » ; « 1,800 trees in lines in the fields and restored hedges » (agroforesterie lancée en 2014-2015) ; « a 600-strong flock » de moutons avec un berger salarié. D'après des résultats de recherche [R4-89] (EXTRAIT) : domaine d'environ 1 800 ha « moitié bois, moitié champs », géré par dix cousins copropriétaires ; potager certifié bio en 2015 ; 10 chambres et suites et 2 appartements aménagés dans les dépendances ; parc ouvert les week-ends et jours fériés d'avril à début novembre.
- **Lecture** (ESTIMATION) : un modèle **multi-activités de proximité parisienne, adossé à un grand foncier agricole et forestier (≈ 1 800 ha, EXTRAIT) et à une copropriété familiale élargie**, avec un **polo** (activité équestre de haut de gamme) et des séminaires confiés à un opérateur extérieur. C'est le cas le plus proche, dans sa logique, du domaine visé par la mission (prestige, cheval, activités maîtrisées). Mais aucun chiffre économique n'est disponible : INCONNU. Vérification : comptes des SCI non publiés ; seule une interview des propriétaires renseignerait.

#### Cas 18 — Champ de Bataille (Le Neubourg, 27) : la fortune d'un décorateur au service d'un jardin

- **Faits** [R4-79] PAGE LUE : château revendu en 1992 « au décorateur Jacques Garcia » ; « plus de 180 hectares de domaine » dont des jardins de 45 ha ; ouvert à la visite depuis 1957 ; golf créé en 1990 dans le parc ; jardins anglo-indiens « ouverts au public depuis le 3 juin 2023 » ; un palais moghol « accueille des événements privés ». Aucune vente postérieure mentionnée.
- **Registre** [R4-14] PAGE LUE : aucune société d'exploitation du château identifiée ; golf et restaurant du golf exploités par des sociétés tierces ; société d'architecture d'intérieur JACQUES GARCIA (20 à 49 salariés ; résultat net 2025 = +160 288 €). Une SAS « Les Forières (Les Gîtes du Champ de Bataille) » (Épégard, NAF 55.20Z, créée en 2022) est fermée depuis le 28/02/2024, avec un liquidateur personne physique inscrit (vraisemblablement une liquidation amiable, non vérifié) : lien avec le domaine NON VÉRIFIÉ.
- **Lecture** (ESTIMATION) : un domaine de 180 ha porté par la **notoriété et l'activité professionnelle du propriétaire**, avec une ouverture au public comme vitrine. Coûts et recettes : INCONNUS.

#### Cas 19 — Château Smith Haut Lafitte et Caudalie (Martillac, 33) : le domaine viticole qui engendre une marque

- **Faits** [R4-77] PAGE LUE : « racheté en 1991 pour 250 millions de francs par Daniel Cathiard » ; « Le domaine de 130 hectares, dont 78 sont plantés de vignes » ; ≈ 200 000 bouteilles par an.
- **Registre** [R4-27] PAGE LUE : SOCIETE CIVILE DU CHATEAU SMITH HAUT LAFITTE (comptes non publiés) ; **CAUDALIE (SAS, tranche 41 = 500 à 999 salariés en 2024)**, directrice générale Mathilde Thomas (née Cathiard), comptes non publiés dans le registre.
- **Lecture** (ESTIMATION) : le domaine vit d'un **produit de grande valeur** (son vin), et la famille dirige à côté une entreprise de cosmétiques qui emploie 500 à 999 salariés selon le registre. Caudalie n'est pas une activité « du domaine » : c'est une entreprise autonome. Le lien d'origine entre la marque et le vignoble n'a pas été vérifié dans les pages lues (HYPOTHÈSE courante, non sourcée ici). Cas d'école de l'hypothèse H8 (moteur extérieur), mais avec des entrepreneurs aguerris et un capital de départ très élevé (250 MF en 1991). Non transposable sans ces deux conditions.

#### Cas 20 — Château de Pommard (21) : domaine viticole et œnotourisme racheté par un entrepreneur de la tech, en perte

- **Faits** [R4-78] PAGE LUE (Wikipédia, citant Le Figaro 2014) : racheté en septembre 2014 par Michael Baum, entrepreneur de la Silicon Valley ; à l'époque « chiffre d'affaires annuel de 6 millions d'euros » et « 35 000 visiteurs par an » ; clos de 20 ha d'un seul tenant ; musée de la vigne et du vin depuis 2006.
- **Registre** [R4-28] PAGE LUE : CHATEAU DE POMMARD (SAS, NAF 47.91B vente à distance, 20 à 49 salariés, présidée par JAZ INTERNATIONAL INC, société américaine) : **résultat net 2025 = -1 156 774 €** (CA non lisible) ; CHATEAU DE POMMARD WINES (SAS, NAF 01.21Z viticulture, 10 à 19 salariés) : **résultat net 2025 = -3 214 472 €** (CA non lisible). Une SAS « Château de Pommard Development » créée le 28/10/2025 est déjà fermée.
- **Lecture** (ESTIMATION) : ≈ **-4,4 M€ de pertes nettes cumulées en 2025** pour un domaine qui affichait 6 M€ de CA en 2014. Un grand domaine viticole avec visite, vente directe et vente à distance ne garantit pas la rentabilité ; ici, les pertes sont portées par l'actionnaire.

#### Cas 21 — Puy du Fou (85) : l'exemple extrême, non transposable

- **Faits** [R4-42] PAGE LUE (Wikipédia, lecture partielle) : 81 000 visiteurs la première année (1978) pour un point mort visé à 40 000 ; 2,8 millions de visiteurs en 2024 et environ 3 millions en 2025 ; CA de 112 M€ en 2018 et 114 M€ en 2019 ; en 2020, CA en baisse d'environ 43 % à 70,7 M€ et perte de 23 M€ ; prêts garantis de 34 M€ (21 M€ de l'État, 13 M€ de la BEI) en 2020 ; environ 4 000 bénévoles « Puyfolais » pour la Cinéscénie ; propriétaire : SAS Puy du Fou France. Château Renaissance inachevé, racheté au département de la Vendée en 2012 et restauré en 2013-2014.
- **Lecture** (ESTIMATION) : le château n'est qu'un prétexte historique ; le modèle est un parc à spectacles de masse, porté par une communauté de bénévoles. Il montre la **sensibilité aux chocs** (2020 : -43 % de CA et 23 M€ de pertes en une saison) même pour un leader. Aucun élément transposable à une résidence privée calme.

## 4. Tableau comparatif des cas

Légende « Transposable » : au projet de la mission (château > 50 ha, résidence privée calme, chevaux, sans recours à la fortune du propriétaire). CA et résultats en M€ ; « n.p. » = non publié. La colonne « Qui finance l'équilibre ? » est une interprétation (ESTIMATION) à partir des faits cités dans les fiches.

| # | Cas | Type | Échelle | CA connu | Résultat net connu | Effectif | Qui finance l'équilibre ? | Statut principal | Transposable |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Chantilly (60) | fondation, monument + écuries | parc 140 ha ; 658 000 visiteurs (2025) | 12,7 recettes (2025) | déficit 6 (2020, EXTRAIT) | n.p. | mécène unique 2006-2020/2025, puis État 0,8/an + dons | PAGE LUE / EXTRAIT | non (échelle) ; leçon sur la dépendance |
| 2 | Domaine des Étangs (16) | hôtel ultra-luxe + élevage | 1 012 ha ; 17 clés | 3,47 hôtel (2025) + 1,82 agri (2024) | -3,20 et -4,36 | 20-49 + 10-19 | fortune familiale (Primat) | PAGE LUE | non |
| 3 | Ygrande (03) | hôtel + écuries | 40 ha ; 26 boxes | n.p. | -0,10 (2022) | 20-49 | — | PAGE LUE | ÉCHEC (liquidation 2025) |
| 4 | Motte-Husson (53) | mariages + médias | 4,9 ha | n.p. | n.p. | n.p. | notoriété TV, livres | PAGE LUE | non (exposition médiatique) |
| 5 | Gudanes (09) | restauration + séjours | ≈ 4,9 ha | n.p. | n.p. | n.p. | revenu médical extérieur, livre | PAGE LUE | partiel (logique de moteur extérieur) |
| 6 | Mothe-Chandeniers (86) | SAS participative | ruine + parc | n.p. (confidentiel) | n.p. | 6-9 | 25 000 co-châtelains (≈ 4,4 M€ collectés) | PAGE LUE | non (pas d'usage privé) |
| 7 | Haras du Pin (61) | haras public historique | ≈ 1 100 ha (EXTRAIT) ; ≈ 50 000 visiteurs (2012) | budget ≈ 1,16 (2016, EXTRAIT) | INCONNU | INCONNU | État puis collectivités | PAGE LUE / EXTRAIT | non |
| 8 | Pôle international du cheval (14) | SEM d'événements équestres | site public | 1,94 (2024) | -0,26 | 10-19 | collectivités actionnaires | PAGE LUE | non |
| 9 | Jardy (92) | centre équestre public + golf | 75-90 ha ; 2 500 cavaliers | INCONNU | INCONNU | n.p. | département | PAGE LUE (faible) | non |
| 10 | Haras normands (Étreham, Logis St-Germain…) | élevage pur-sang | — | 12,96 ; 0,83 | -0,38 ; -0,72 | 20-49 ; 10-19 | associés | PAGE LUE | non (métier de spécialiste) |
| 11 | Vaux-le-Vicomte (77) | monument privé, visite de masse | parc ≈ 500 ha ; ≈ 300 000 visiteurs | budget 8-9 | n.p. | 75 ETP (50-99) | recettes propres et mécénat (aides de l'État ≈ 4 %) | PAGE LUE | non (rang mondial) |
| 12 | Chenonceau (37) | monument privé, visite de masse | ≈ 900 000 visiteurs (2017) | restaurant 5,64 (2025) | restaurant +1,11 | 50-99 + 20-49 | INCONNU (recettes propres probables) | PAGE LUE | non |
| 13 | Cheverny (41) | visite + vènerie + événements | ≈ 100 ha ; ≈ 350 000 visiteurs | n.p. | orangerie +0,15 (2024) | 20-49 + 20-49 | INCONNU (recettes propres probables) | PAGE LUE | non |
| 14 | Villandry (37) | jardins | 6 ha de jardins | n.p. | restaurant +0,02 | 20-49 | INCONNU | PAGE LUE | non |
| 15 | Breteuil (78) | visite familiale + réceptions | 75 ha ; 120 000 visiteurs | n.p. (divisé par 2 en 2020) | n.p. | ≈ 10 | recettes + vente d'un meuble classé (2014) | PAGE LUE | partiel |
| 16 | Brissac (49) | résidence ducale + événements | INCONNU | n.p. | n.p. | 3-5 | INCONNU | PAGE LUE | partiel |
| 17 | Courances (91) | parc + agriculture + polo + séjours | parc 86 ha ; ≈ 1 800 ha (EXTRAIT) | n.p. | n.p. | 6-9 (SCI du parc) | foncier agricole + activités + opérateur de séminaires | PAGE LUE / EXTRAIT | **le plus proche** (logique), chiffres inconnus |
| 18 | Champ de Bataille (27) | jardins + événements privés | 180 ha | n.p. | n.p. | n.p. | activité professionnelle du propriétaire | PAGE LUE | non |
| 19 | Smith Haut Lafitte / Caudalie (33) | vin + marque de cosmétiques | 130 ha (78 de vignes) | n.p. | n.p. | Caudalie 500-999 | produit (vin) + entreprise séparée | PAGE LUE | partiel (logique H8) |
| 20 | Château de Pommard (21) | vin + œnotourisme + vente à distance | clos de 20 ha ; 35 000 visiteurs (2014) | 6 (2014) | -4,37 cumulé (2025) | 20-49 + 10-19 | actionnaire américain | PAGE LUE | non |
| 21 | Puy du Fou (85) | parc à spectacles | 2,8 M visiteurs (2024) | 114 (2019) ; 70,7 (2020) | -23 (2020) | n.p. | recettes, bénévoles, prêts garantis | PAGE LUE (Wikipédia) | non |
| — | 33 châteaux-hôtels (échantillon) | hôtels | CA médian 2,18 | — | 61 % en perte ; marge médiane -6,3 % | — | associés | ESTIMATION | défavorable |
| — | 24 liquidations BODACC 2023-2026 | hôtels, réceptions, équestre | — | — | — | — | — | PAGE LUE | contre-exemples |

## 5. Mécanismes économiques : ce qui marche, ce qui échoue

### Ce qui marche (avec preuves)
1. **La visite de masse d'un monument de rang mondial** finance l'essentiel du fonctionnement : Vaux (≈ 300 000 visiteurs, aides de l'État ≈ 4 % des besoins) [R4-31] ; Chenonceau (≈ 900 000 visiteurs ; restaurant rentable : +1,11 M€ pour 5,64 M€ de CA) [R4-87] [R4-05]. Conditions : notoriété exceptionnelle, proximité d'un grand bassin touristique, 50 à 100 salariés. Incompatible avec une résidence calme.
2. **Le séminaire d'entreprise à grande échelle près de Paris**, exploité de façon professionnelle : Château de Villiers-le-Mahieu (CA 11,1 M€, +1,25 M€) ; Château Saint-Just (CA 10,2 M€, +2,27 M€) ; réseau Châteauform' (CA 186 M€, marge ≈ 1,8 %) [R4-34] [R4-37]. C'est un métier d'opérateur, avec un fort volume.
3. **La séparation juridique des activités** (monument / restauration / agriculture / immobilier / écuries) : Vaux, Cheverny, Courances, Brissac (groupement forestier), Ygrande [R4-02] [R4-03] [R4-07] [R4-06] [R4-24]. À Ygrande, l'EARL équestre a survécu à la liquidation de la société hôtelière.
4. **Le grand foncier agricole et forestier** comme socle (Courances ≈ 1 800 ha, 600 ha de plaine cultivée ; Vaux SCEA ; Brissac groupement forestier) [R4-88] [R4-89] [R4-02] [R4-06]. Les revenus n'en sont pas publiés (INCONNU), mais ce socle est présent chez les familles qui durent.
5. **Un moteur économique extérieur au domaine** : revenu professionnel (Gudanes) [R4-54] ; entreprise séparée (Caudalie) [R4-27] ; activité du propriétaire (Jacques Garcia) [R4-14] ; médias (Motte-Husson) [R4-44]. C'est l'hypothèse H8, mais chaque exemple dépend d'une personne ou d'une marque.
6. **Le financement participatif pour l'acquisition et les urgences** (Mothe-Chandeniers : ≈ 4,4 M€ en sept ans) [R4-62] : efficace pour un récit collectif de sauvetage, sans usage privé.
7. **Les activités annexes à fort volume** (restauration sur site) : rentables si la fréquentation est très élevée (Chenonceau, marge nette ≈ 20 %), proches de l'équilibre sinon (Vaux : -2 475 € pour 2,67 M€ de CA) [R4-05] [R4-02].

### Ce qui échoue (avec preuves)
1. **Le château-hôtel isolé de taille moyenne** : 61 % de l'échantillon en perte, marge nette médiane -6,3 % ; au moins 15 châteaux-hôtels ou hébergements de château en liquidation dans le BODACC 2023-2026 [R4-34] [R4-35] [R4-74] [R4-75] [R4-76].
2. **Le lieu de réception / mariages / chambres d'hôtes** : liquidations de Rêve de Château, Un Passage au Château, Esprit de Château, Château des Lys, Château de Saint-Priest… [R4-74] à [R4-76] ; coûts ERP élevés et procédures longues (cas « Monsieur N. » : plus de 100 000 € et plus de deux ans) [R4-52].
3. **L'hôtellerie ultra-luxe sur très grand domaine** (Domaine des Étangs : perte ≈ CA) [R4-08].
4. **L'équestre « vitrine »** : Haras de Hus (-2,94 M€ pour 1,77 M€ de CA), Bouquetot (-3,83 M€ pour 2,10 M€), Beaumont (-1,78 M€), Logis Saint-Germain (-0,72 M€ pour 0,83 M€), Étreham (-0,38 M€) [R4-39] [R4-70] [R4-26] ; équipements publics déficitaires (Pôle international du cheval : -0,26 M€) [R4-15] ; Haras du Pin abandonné par l'État comme « non rentable » [R4-65] ; centre équestre de Trie-Château liquidé [R4-74].
5. **La dépendance à un mécène unique** (Chantilly) [R4-45] [R4-46].
6. **La dépendance à un diffuseur** (Motte-Husson après la rupture avec Channel 4 en 2023) [R4-94].
7. **Le domaine viticole comme « produit »** n'est pas une garantie : Château de Pommard (-4,37 M€ en 2025) ; vague de liquidations de châteaux viticoles en 2025-2026 [R4-28] [R4-74] [R4-75].
8. **La gouvernance familiale est un risque** : administrateur provisoire à Chenonceau [R4-05]. À Courances, la gestion est partagée entre dix cousins (EXTRAIT [R4-89]) : ce n'est pas un échec, mais cela montre qu'un grand domaine transmis devient vite une copropriété familiale.
9. **Les structures de dotation sans ressources** : fonds de dotation du château royal de Montargis liquidé (2025) [R4-74].
10. **La détention courte** : ≈ 7 ans en moyenne selon La Demeure Historique, contre un engagement fiscal de 15 ans [R4-51] [R4-52].

### Conséquences pour la mission (ESTIMATION)
- Aucun cas français trouvé ne montre un domaine de type S2 qui finance durablement son fonctionnement **avec une résidence privée calme et sans fortune extérieure**. Les domaines qui s'autofinancent le font par la visite de masse (incompatible avec la tranquillité) ; les autres reposent sur une fortune, un mécène, un moteur extérieur ou un grand foncier.
- Les hypothèses H3 (activités classiques insuffisantes) et H4 (l'équestre finance au mieux ses installations) sont **confortées** par les comptes publiés. H8 (moteur extérieur) est illustrée par plusieurs cas durables qui ne vivent pas de la visite de masse (Gudanes, Smith Haut Lafitte et Caudalie, Champ de Bataille, Motte-Husson), mais chaque exemple repose sur une personne ou une marque.

## Contre-exemples et cas d'échec trouvés

Échecs et difficultés sourcés (au moins 5 exigés ; ici plus de 30) :
1. **Château d'Ygrande** (03) : hôtel + écuries, liquidation judiciaire le 28/10/2025, cessation des paiements le 01/09/2025 [R4-18] [R4-22] [R4-23] [R4-24] [R4-25].
2. **24 liquidations BODACC 2023-2026** de châteaux-hôtels, d'hébergements, de lieux de réception, d'un centre équestre et d'un fonds de dotation de château (tableau § 2) [R4-74] [R4-75] [R4-76].
3. **Domaine des Étangs** : pertes de 3,2 M€ (hôtel, 2025) et 4,4 M€ (agriculture, 2024) [R4-08].
4. **Château de Pommard** : -4,37 M€ de pertes nettes cumulées en 2025 [R4-28].
5. **Haras de Hus, Écurie Haras Bouquetot, Haras de Beaumont, Haras du Logis Saint-Germain, SARL de Chambure (Étreham)** : pertes 2024-2025 [R4-26] [R4-39] [R4-70].
6. **Domaine de Chantilly** : départ du mécène, besoin de 68 M€ sur dix ans, déficit d'exploitation de 6 M€ en 2020 (EXTRAIT) [R4-45] [R4-46] [R4-47].
7. **Haras national du Pin** : missions jugées « non rentables », EPA fermé en 2022, syndicat mixte créé en 2024 [R4-16] [R4-65].
8. **Pôle international du cheval** : -0,26 M€ en 2024 [R4-15].
9. **Motte-Husson** : rupture avec Channel 4 en mai 2023 après une enquête RH ; société britannique au nom du château dissoute en 2023 [R4-94] [R4-60].
10. **Reventes rapides de monuments historiques** : ≈ 7 ans de détention moyenne, 800 puis 1 500 MH en vente selon la DH (chiffre déclaratif) [R4-51] [R4-52].
11. **Échantillon de 33 châteaux-hôtels** : 20 en perte [R4-34] [R4-35].
12. **Breteuil** : CA divisé par deux en 2020 ; vente d'un trésor national au Louvre en 2014 [R4-82].
13. **Puy du Fou** : -43 % de CA et 23 M€ de pertes en 2020 [R4-42].
14. **Chenonceau** : administrateur provisoire inscrit au registre (cause inconnue) [R4-05].

Contre-exemples (réussites qui nuancent le constat) :
- Château de la Messardière (CA 58,1 M€, +7,9 M€), Château Saint-Martin & Spa (11,4 M€, +0,9 M€), Château de Villiers-le-Mahieu (11,1 M€, +1,25 M€), Château Saint-Just (10,2 M€, +2,27 M€) [R4-34] [R4-35] [R4-37] : la rentabilité existe, à grande échelle, avec un opérateur professionnel et sur un marché porteur (luxe littoral, séminaires franciliens).
- Chenonceau Castellum (+1,11 M€ pour 5,64 M€) [R4-05] : restauration très rentable sur un site à ≈ 900 000 visiteurs.
- Domaine équestre de la Bonde (CA 2,12 M€, +0,11 M€), Haras du Cadran (+0,23 M€), Haras du Berlais (+0,30 M€) [R4-39] [R4-93] : des entreprises équestres moyennes et spécialisées peuvent être rentables, sans château à porter.
- Gudanes : aucun échec documenté ; le projet avance grâce à un revenu extérieur [R4-54].
- Mothe-Chandeniers : réussite du financement participatif de l'acquisition et des premières tranches [R4-41] [R4-62].

## Points de doute / hypothèses non vérifiées

1. **« CA = 0 » dans le registre** : interprété comme un compte de résultat confidentiel ou absent, pas comme un CA nul (ESTIMATION).
2. **Rattachements société ↔ domaine** déduits du nom, du siège et des dirigeants, non confirmés par un document : SARL de Chambure = Haras d'Étreham ; Haras de S.A. l'Aga Khan = Bonneval ; Fresnay le Buffard UAE = haras de Fresnay-le-Buffard ; Chenonceau Castellum = restauration du château ; Domaine des Étoiles = volet agricole du Domaine des Étangs (lien confirmé par le registre : présidente de la société hôtelière).
3. **Divergences conservées** : Vaux 8 M€ (Wikipédia, sans date) contre 9 M€ (France 5, 2016) ; Chantilly 30 M€ d'engagement (source officielle) contre 70 M€ injectés (presse, EXTRAIT) ; Domaine des Étangs 17 clés (2023) contre 29 (Country Life, EXTRAIT) ; Chenonceau ≈ 800 000 visiteurs (2007, EXTRAIT) contre ≈ 900 000 (2017).
4. **Durée moyenne de détention de 7 ans** : chiffre de plaidoyer de La Demeure Historique, méthode non publiée. Un rapport public sur les monuments privés (vie-publique.fr) n'a pas pu être ouvert (HTTP 503) [R4-53].
5. **BODACC** : lecture d'environ 250 annonces sur 327 ; activités résumées par l'outil de lecture ; seules les sociétés dont le nom contient « château » ; causes des défaillances non recherchées.
6. **Échantillon de châteaux-hôtels** : biais de sélection (comptes publiés, nom, tri par pertinence), années hétérogènes (2017-2025) ; le résultat net n'est ni l'EBE ni la trésorerie.
7. **Sources secondaires** : plusieurs faits viennent de Wikipédia (fiabilité moyenne à faible) ; les chiffres 2025 de Chantilly viennent de The Independent, repris par Time Out.
8. **Chenonceau** : la signification exacte de l'administrateur provisoire (date, juridiction, motif) est inconnue.
9. **Haras du Pin** : budget, déficit et effectif actuels inconnus ; chiffres 2016 au statut EXTRAIT.
10. **Jardy** : mode de gestion et budget inconnus.
11. **Aucun compte d'exploitation complet** d'un domaine privé de type S2 n'a été trouvé : les budgets S1/S2 devront être construits poste par poste (R1, R2) et non par analogie avec ces cas.
12. Les recettes de l'agriculture, de la forêt et des locations dans les grands domaines familiaux (Courances, Brissac, Vaux) sont **INCONNUES** : leurs sociétés ne publient pas de comptes.

## Chiffres clés pour le modèle

| # | Donnée | Valeur | Unité | Année | Statut | Source |
|---|---|---|---|---|---|---|
| 1 | Budget annuel d'entretien de Vaux-le-Vicomte | 9 (8 selon Wikipédia) | M€/an | 2016 (n.d.) | PAGE LUE | [R4-31] [R4-30] |
| 2 | Part des aides de l'État dans ce budget (Vaux) | 4 | % | 2016 | PAGE LUE | [R4-31] |
| 3 | Part des jardins à la française dans le budget (Vaux) | 10 | % | 2016 | PAGE LUE | [R4-31] |
| 4 | Salariés de Vaux-le-Vicomte | 75 ETP (tranche 50-99) | ETP | n.d. / 2024 | PAGE LUE | [R4-30] [R4-02] |
| 5 | Dépense annuelle par visiteur à Vaux | 27 à 30 | €/visiteur | 2016 | ESTIMATION | [R4-30] [R4-31] |
| 6 | Recettes et visiteurs de Chantilly | 12,7 M€ pour 658 000 visiteurs (≈ 19 €/visiteur) | M€ ; visiteurs | 2025 | PAGE LUE (secondaire) | [R4-46] |
| 7 | Besoin de restauration de Chantilly | 68 sur 10 ans (≈ 6,8/an) | M€ | 2026 | PAGE LUE | [R4-46] |
| 8 | Charges annuelles et déficit d'exploitation de Chantilly | 13 ; -6 | M€ | 2020 | EXTRAIT | [R4-47] |
| 9 | Fréquentation moyenne d'un monument privé ouvert | ≈ 6 000 | visiteurs/an | 2022 | ESTIMATION (9 M / 1 500) | [R4-51] |
| 10 | Dépense fiscale MH par monument privé | < 1 750 | €/an | PLF 2022 | PAGE LUE | [R4-51] |
| 11 | Durée moyenne de détention d'un MH privé | ≈ 7 | ans | 2017 et 2022 | PAGE LUE (chiffre déclaratif) | [R4-51] [R4-52] |
| 12 | Châteaux-hôtels (CA ≥ 1 M€) en perte | 61 % (20/33) ; marge nette médiane -6,3 % ; CA médian 2,18 M€ | % ; € | 2017-2025 | ESTIMATION | [R4-34] [R4-35] |
| 13 | Domaine des Étangs, société hôtelière | CA 3,47 ; RN -3,20 | M€ | 2025 | PAGE LUE | [R4-08] |
| 14 | Domaine des Étangs, société agricole | CA 1,82 ; RN -4,36 | M€ | 2024 | PAGE LUE | [R4-08] |
| 15 | Restauration de Chenonceau (Chenonceau Castellum) | CA 5,64 ; RN +1,11 | M€ | 2025 | PAGE LUE | [R4-05] |
| 16 | Fréquentation de Chenonceau | ≈ 900 000 | visiteurs/an | 2017 | PAGE LUE | [R4-87] |
| 17 | Fréquentation de Cheverny | 349 200 | visiteurs | 2016 | PAGE LUE (Wikipédia) | [R4-84] |
| 18 | Breteuil : visiteurs et équipe | 120 000 ; 10 salariés | visiteurs/an ; salariés | avant 2020 | PAGE LUE (Wikipédia) | [R4-82] |
| 19 | Séminaires en château, grande échelle (Villiers-le-Mahieu) | CA 11,13 ; RN +1,25 | M€ | 2025 | PAGE LUE | [R4-34] |
| 20 | Opérateur Châteauform' France | CA 186,4 ; RN +3,4 (≈ 1,8 %) | M€ | 2025 | PAGE LUE | [R4-37] |
| 21 | Pôle international du cheval (SEM) | CA 1,94 ; RN -0,26 | M€ | 2024 | PAGE LUE | [R4-15] |
| 22 | Haras d'Étreham (SARL de Chambure) | CA 12,96 ; RN -0,38 | M€ | 2024 | PAGE LUE (rattachement : ESTIMATION) | [R4-26] |
| 23 | Haras de Hus | CA 1,77 ; RN -2,94 | M€ | 2024 | PAGE LUE | [R4-39] |
| 24 | Domaine équestre de la Bonde (hôtel équestre) | CA 2,12 ; RN +0,105 | M€ | 2024 | PAGE LUE | [R4-93] |
| 25 | Château de Pommard (deux sociétés) | RN cumulé -4,37 | M€ | 2025 | PAGE LUE | [R4-28] |
| 26 | Mothe-Chandeniers : achat ; collecte totale | 0,5 ; ≈ 4,4 (25 000 co-châtelains) | M€ | 2017 ; 2017-2024 | PAGE LUE | [R4-41] [R4-62] |
| 27 | Mise aux normes ERP d'une salle de réception (cas DH) | > 100 000 € ; > 2 ans de procédure | € ; ans | 2017 | PAGE LUE | [R4-52] |
| 28 | Choc de type 2020 sur un leader (Puy du Fou) | CA -43 % ; perte 23 M€ | % ; M€ | 2020 | PAGE LUE (Wikipédia) | [R4-42] |
| 29 | Ygrande (hôtel + écurie liquidé en 2025) : domaine, écurie, effectif | 40 ha ; 26 boxes ; 20-49 salariés (société hôtelière) | ha ; boxes ; salariés | effectif 2024 ; site consulté en 2026 | PAGE LUE | [R4-23] [R4-22] |
| 30 | Soutien de l'État à Chantilly | 0,8 M€/an = 40 % des travaux prévus | M€/an | 2016-2026 | PAGE LUE | [R4-45] |

## 6. Bilan d'outillage

- WebSearch : 15 sur 15 autorisées.
- WebFetch : 99 appels (dont environ 16 sans contenu exploitable : 403, 404, 502, 503, DNS, redirection, page fermée). Les moteurs internes utilisés sont ceux de sites officiels (API Recherche d'entreprises, API BODACC de la DILA, Companies House), conformément aux règles.
- Deux PDF de La Demeure Historique ont été extraits localement (pdftotext) après téléchargement par WebFetch, dans un dossier isolé du scratchpad.
- Aucune commande git, aucun contact, aucun formulaire.


## Errata après vérification indépendante (V2V, 2026-10-14)

Ajouté par le directeur de mission. Le texte ci-dessus n'est pas modifié ; ces précisions s'appliquent à sa lecture.

- Échantillon de 33 sociétés de châteaux-hôtels (§ 1.B et ligne 12 des chiffres clés) : V2V retrouve exactement les mêmes 33 sociétés et le même résultat (20 en perte, 61 %, marge nette médiane −6,3 %), mais sur des comptes de 2017 à 2025, dont 4 sociétés fermées et 2 en liquidation selon R7. Sur les seuls comptes 2023-2025 (26 sociétés) : 54 % en perte, marge nette médiane −4,5 %. Biais à signaler : classement par pertinence, seules les sociétés qui publient leurs comptes, résultat net et non EBE [V2V-33] [V2V-34].
