# AV8 — Vérification indépendante des preuves (cellule audiovisuelle, mission 2)

Agent AV8 « Vérificateur de preuves ». Rédigé le 2026-10-14. Toutes les pages et données citées ont été consultées le **2026-10-14**.

Fichiers relus : `03_CAS_REELS/AV1_cas.md` à `AV6_The_Family_parcours_et_controverses.md`, `03_CAS_REELS/AV7_echecs.md`, `04_IDEES_STRATEGIQUES/AV1_idees.md` à `AV6_idees.md` et `AV7_idees_originales.md`. Les sources de ce rapport sont numérotées S-AV8-xx dans `_brut/sources_AV8.csv`.

## 1. Méthode

**Principe.** Chaque affirmation a été vérifiée **à nouveau, à la source**, sans reprendre les conclusions de l'agent qui l'avait rapportée. L'ordre de préférence des sources est le suivant :
1. registre ou donnée publique : BODACC (API open data), ratios INPI-BCE (comptes déposés), DVF (valeurs foncières de la DGFiP, fichiers Etalab), Companies House ;
2. comptes déposés lus en document ;
3. décision de justice en texte intégral ;
4. texte officiel : BOFiP, eCFR (règlement fédéral américain) ;
5. communiqué de l'émetteur ;
6. presse ;
7. propos d'un intervenant (transcription publiée).

**Verdicts.**

| Verdict | Signification |
|---|---|
| **CONFIRMÉ** | La source primaire dit la même chose, chiffres et dates compris. |
| **PARTIELLEMENT CONFIRMÉ** | Le fond est exact, mais un chiffre, une date ou une interprétation doit être corrigé, ou une partie reste non vérifiable. |
| **NON CONFIRMÉ** | Aucune source primaire ou indépendante n'a été trouvée. Le propos peut être exactement cité sans que le fait soit établi. |
| **CONTREDIT** | Une source primaire dit autre chose. |

**Contraintes respectées.**
- YouTube n'a pas été utilisé (HTTP 429).
- 8 WebSearch sur les 25 autorisés.
- Aucun blocage n'a été contourné : Telegraph (402), Spear's (403).
- Certains sites étaient injoignables depuis l'environnement : l'API Recherche d'entreprises, data.culture.gouv.fr (base Mérimée), ccomptes.fr et la Banque des Territoires (en maintenance).
- Les comptes scannés (Château du Theil, Blenheim) ont été lus page par page en image.

**Volets judiciaires.** Voir la section 6 sur la présomption d'innocence.

## 2. Synthèse

**35 affirmations structurantes sélectionnées :**

| Verdict | Nombre |
|---|---|
| CONFIRMÉ | 15 |
| PARTIELLEMENT CONFIRMÉ | 13 |
| NON CONFIRMÉ | 6 |
| CONTREDIT | 1 |

Sept sous-affirmations sont **contredites** à l'intérieur de lignes confirmées ou partiellement confirmées :
1. « aucune vente en DVF » pour Fontenay (V04) ;
2. « château 8 fois moins cher que ses terres » (V10) ;
3. « 1 250 ha » à Castillon (V31) ;
4. « 28 M€ » pour Fresnay (V34) ;
5. « environ 40 M€ » de CA 2024 pour Fontenille (V18) ;
6. Bevouac présentée comme une société d'« hébergements » (V05) ;
7. « 60 » ou « 73 » chambres au Barn (V16).

Cinq contrôles ponctuels complémentaires figurent en annexe : ils sont tous confirmés, et l'un d'eux appelle une nuance.

**Lecture rapide.**
- Les chiffres tirés de registres par les agents sont exacts : environ 90 montants et dates recontrôlés, aucune erreur de chiffre.
- Les erreurs portent sur :
  - des **périodes** mal étiquetées (exercice d'Arqana, date de parution BODACC) ;
  - des **interprétations** (« 8 fois moins cher », taux de prélèvement d'Arqana, règles SBA) ;
  - des **prix relayés par la presse**, que les valeurs foncières (DVF) ou une interview corrigent : Fontenay, Strawbridge, Fresnay-le-Buffard.
- Les chiffres d'exploitation **annoncés en podcast** sont presque tous invérifiables : remplissage, répartition des recettes, chiffre d'affaires, fréquentation.

## 3. Tableau de vérification

Agents sources : AV1 (châteaux français), AV2 (domaines britanniques et irlandais, haras), AV3 (business du cheval), AV4 (acquisition et financement), AV5 (modèles premium), AV6 (The Family), AV7 (échecs).

| # | Affirmation vérifiée (agent) | Source primaire consultée | Verdict | Explication | URL principale | Consulté |
|---|---|---|---|---|---|---|
| V01 | Fontenay : apport des fondateurs de 10 000 € (AV1, AV4) | BODACC, SARTHE SOCIETY SAS (980 419 436) et SCI CHATEAU DE FONTENAY (981 167 232) | **CONFIRMÉ** | Capital de 10 000 € à l'immatriculation (16/10/2023 ; président J. Nabais, DG M. Menez). La SCI a un capital de 1 000 € ; ses associés sont Sarthe Society et deux holdings. Le registre montre le capital, pas d'éventuels comptes courants. | https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records?where=registre%20like%20%22980419436%22 | 2026-10-14 |
| V02 | Fontenay : club deal de 550-551 k€ auprès de 33 investisseurs pour environ 22 % (AV1, AV4) | BODACC, augmentation de capital | **PARTIELLEMENT CONFIRMÉ** | Capital porté de 10 000 € à 12 755 €, soit 21,6 % de titres nouveaux, ce qui est cohérent avec « 22 % ». Le montant (prime comprise) et le nombre d'investisseurs ne sont pas publiés. Parution BODACC le 13/03/2024. Le « 19/12/2023 » d'AV1 n'apparaît pas dans l'avis : c'est peut-être la date de décision, non vérifiable. | idem V01 | 2026-10-14 |
| V03 | Fontenay : obligations Bricks de 690 k€ à 7 %, liquidité au 31/01/2029 (AV1, AV4) | Communiqué de l'émetteur (Galivel, 12/12/2023, PDF) | **CONFIRMÉ** (conditions de l'offre) | Objectif de 690 000 €, taux fixe de 7 %, « date de liquidité fixée au 31 janvier 2029 ». **Émetteur : Sarthe Society SAS**, la société d'exploitation. Le montant réellement collecté et les « 2 048 prêteurs » restent déclaratifs. | https://galivel.com/media/files/12__cp__ils_le__vent_310_000__en_12h___booster_son_e__pargne_tout_en_sauvegardant_le_patrimoine.pdf | 2026-10-14 |
| V04 | Fontenay : prix d'achat de 780 k€ (AV4). Selon AV1, prix inconnu et « aucune vente en DVF » | DVF 2023, Sarthe (DGFiP) | **PARTIELLEMENT CONFIRMÉ** | Le **20/12/2023**, deux ventes contiguës ont lieu à Fontenay-sur-Vègre et Asnières-sur-Vègre (lieux-dits Le Logis et Moulin de Fontenay) : **498 800 € et 247 800 €, soit 746 600 € pour 11,61 ha**, avec une maison de 377 m² et une de 255 m². La surface correspond aux 11,6 ha du communiqué et la date suit la collecte Bricks. Le DVF n'identifie pas l'acheteur. L'écart avec 780 k€ (environ 33 k€) peut venir du mobilier ou des frais. **L'affirmation d'AV1 est CONTREDITE.** | https://files.data.gouv.fr/geo-dvf/latest/csv/2023/departements/72.csv.gz | 2026-10-14 |
| V05 | Fontenay : liquidation de la société d'un associé, Bevouac (AV1, AV4) | BODACC et ratios INPI, BEVOUAC (830 549 333) | **CONFIRMÉ** | Redressement judiciaire le 03/06/2025 (cessation des paiements au 07/05/2025), liquidation judiciaire le 31/10/2025, fonds acheté par DS IMMO (acte du 28/01/2026). En 2023 : CA de 2,11 M€, RN de 164 915 €. Le prix de 105 k€ ne figure pas dans l'avis BODACC lu. Bevouac est une société de **conseil en investissement immobilier**, pas d'« hébergements » comme l'écrit AV4. Elle n'est pas associée des sociétés de Fontenay, mais partage leur siège. | https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records?where=registre%20like%20%22830549333%22 | 2026-10-14 |
| V06 | Fontenay : CA de 13 k€, puis 116 k€, puis 400 k€ attendus ; château « classé monument historique » (AV4, communiqué) | BODACC (dépôts de comptes) ; Wikipédia, faute d'accès à la base Mérimée | **NON CONFIRMÉ** | Les comptes 2024 et 2025 de Sarthe Society sont déposés **avec déclaration de confidentialité** : le CA est invérifiable. Aucune notice de protection n'a été trouvée (AV1 non plus) et Wikipédia cite le logis sans protection. Ce sont des propos du porteur. | idem V01 | 2026-10-14 |
| V07 | Château du Theil : comptes 2024 (AV1) | Comptes annuels déposés (PDF, p. 4 à 7) ; ratios INPI ; BODACC | **CONFIRMÉ** | Résultat de **−276 413 €** ; bilan de **6 131 332 €** ; prêt du Crédit Agricole de 1 000 k€ (février 2024, 156 mois, hypothèque) ; prêt de La Première Brique de 605 k€ (hypothèque de second rang et 3 cautions personnelles et solidaires) ; compte courant bloqué de 1,2 M€ sur 7 ans ; crédit-bail de 351 k€ ; subvention de 215 k€ ; ouvertures le 12/09/2024 et le 08/10/2024. Capital : 200 k€ (2019), 526 k€ (2020), puis 1,73 M€ (2025). | https://actes.ccm2.net/bilan-financier/1ba55343-6790-449d-97f3-9ad1edd2471e | 2026-10-14 |
| V08 | Château du Theil : achat pour « environ 160 000 € » (AV1) | Comptes 2024 ; BODACC (mise en activité le 31/12/2019) | **NON CONFIRMÉ** | Seul l'entretien avec le porteur donne ce chiffre. Au bilan, les terrains valent 125 449 €, ce qui est compatible sans le prouver. Le DVF en ligne ne couvre que 2021-2025. | idem V07 | 2026-10-14 |
| V09 | Dampierre : lot château adjugé 675 000 € (AV1) | DVF 2021, Aube | **CONFIRMÉ** | Adjudication du 23/04/2021 : 675 000 € pour 11,97 ha, dont 9,21 ha de parc. | https://files.data.gouv.fr/geo-dvf/latest/csv/2021/departements/10.csv.gz | 2026-10-14 |
| V10 | Dampierre : domaine vendu 5,4 M€ en 6 lots ; « le château valait 8 fois moins que ses terres » (AV1) | DVF 2021 (Aube et Marne) ; France 3 du 23/04/2021 | **PARTIELLEMENT CONFIRMÉ** | France 3 annonce 5,4 M€, mais ses propres lots totalisent **5,185 M€**. Le DVF montre 4 adjudications pour 3,125 M€ : 675 k€, 640 k€ (75 ha de bois à Vaucogne), 30 k€ et **1,78 M€ pour 81 ha** (environ 21 900 €/ha). La forêt de 210 ha à 2,1 M€ et le lot de 40 k€ sont introuvables. Le ratio réel est de 3,6 à 7 selon la base retenue : **« 8 fois » est CONTREDIT**. | idem V09 ; https://france3-regions.franceinfo.fr/grand-est/aube/aube-un-domaine-de-pres-de-1000-ans-vendu-aux-encheres-pour-plus-de-5-millions-d-euros-2059618.html | 2026-10-14 |
| V11 | Castle Leslie : reconstitution par morceaux ; rénovation de 10 M€ cofinancée (AV2) | Document de l'entreprise ; transcription publiée ; Wikipédia | **PARTIELLEMENT CONFIRMÉ** | Rachat du Lodge et du centre équestre en 2004. Rénovation de « €10million » lancée en janvier 2006, aidée par l'État irlandais et cofinancée par l'UE (Plan national de développement 2000-2006, via Fáilte Ireland). Rachat des parts familiales : propos de S. Leslie (« I bought out all the freehold from everybody », 00:38:39). Le montant de l'aide est inconnu et la source est intéressée. | https://www.castleleslie.com/wp-content/uploads/2022/06/Regeneration-History.pdf | 2026-10-14 |
| V12 | Quétiéville : de 0 à 50 chevaux en pension en 13 mois, remplissage de 100 % (AV2) | MySweetImmo et Lyonmag (données du porteur et de Bricks) ; BODACC | **NON CONFIRMÉ** | Chiffres fournis par le porteur et la plateforme. **Tony Parker est « investisseur et ambassadeur de Bricks.co »** (Lyonmag) : conflit d'intérêts. Au registre : **SCEA Domaine de Quétiéville** (903 790 491, 2021, associés Infinity Nine Promotion et NBA Participations) et **GFA Domaine de Quétiéville**. Ces sociétés civiles ne publient pas de comptes. Date de reprise : 2021 selon Lyonmag, 15/11/2022 selon Bricks. | https://www.mysweetimmo.com/2024/02/05/immobilier-tony-parker-ouvre-linvestissement-dans-son-haras-de-chevaux-des-10e/ | 2026-10-14 |
| V13 | Quétiéville : 1,072 M€ levés auprès de 2 808 prêteurs ; taux (AV2) | MySweetImmo 23/02/2024 ; Lyonmag ; 1 WebSearch | **PARTIELLEMENT CONFIRMÉ** | Les mêmes chiffres apparaissent dans plusieurs médias, mais tous viennent de la communication de Bricks. Obligations avec intérêts mensuels. **Taux, échéance et société émettrice introuvables.** | https://www.mysweetimmo.com/2024/02/23/immobilier-le-haras-de-tony-parker-finance-par-2-808-personnes-en-50-minutes-pour-107-million-deuros/ | 2026-10-14 |
| V14 | Polo de Chantilly : 50 % des recettes en pensions, 25 % en engagements, 25 % pour le reste (AV5) | Transcription publiée (Buzzsprout) ; BODACC | **NON CONFIRMÉ** (propos exact) | La citation est fidèle (directeur, 1:07:35 : « 50% of the incomes are coming from the stabling horses… 25%… the rest of the 25% more or less »). Aucune structure exploitante ni aucun compte n'ont été trouvés. C'est un ordre de grandeur déclaratif. | https://www.buzzsprout.com/1546234/17774798/transcript | 2026-10-14 |
| V15 | Polo de Chantilly : terres louées à l'Institut de France, bail de 50 ans signé en 1995, environ 200 ha (AV5) | Transcription ; communiqué (Horse Times) ; PoloPlus10 ; site du club | **PARTIELLEMENT CONFIRMÉ** | « We rent a part of the land given to the French Academy » (1:12:58) ; « farmland belonging to the Institut de France » ; Ferme d'Apremont « spanning 200 hectares ». **Le bail de 50 ans signé en 1995 n'a été trouvé dans aucune page lue.** | https://poloplus10.com/the-legends-when-palermo-comes-to-chantilly/ | 2026-10-14 |
| V16 | Le Barn : holding, société des murs et société d'exploitation (AV5, AV3) | BODACC (3 sociétés) ; site officiel | **CONFIRMÉ** | Barn Holding (ex-Bretigny, 822 248 274, président W. Kriegel) préside Hameau de la Cense (murs) et Barn Bonnelles (exploitation, créée en 2022). **Apport partiel d'actif du 22/06/2022** : actif de 2,23 M€, passif de 2,14 M€. Le site officiel annonce **72 chambres** (AV3 en donne 60, AV5 73) et un domaine de **165 ha**. | https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records?where=registre%20like%20%22915113211%22 | 2026-10-14 |
| V17 | Le Barn : loyer d'environ 1,08 M€ versé aux murs (AV5, déduction) | Ratios INPI | **PARTIELLEMENT CONFIRMÉ** | Hameau de la Cense facture **exactement 1 081 000 € en 2024 et en 2025**, avec une marge d'EBE de 87 à 91 %. C'est un profil de loyer fixe, mais le bail n'est pas publié. Barn Bonnelles en 2025 : CA de 5,997 M€, RN de −333 k€. Total des deux sociétés : environ −0,48 M€ en 2025. | https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/ratios_inpi_bce/records?where=siren%3D%22799342704%22&limit=50 | 2026-10-14 |
| V18 | Fontenille : LVMH minoritaire ; Caisse des Dépôts au capital ; comptes 2024 (AV5, AV4) | Page Caisse des Dépôts du 16/02/2024 ; TourMaG ; ratios INPI (comptes consolidés) | **CONFIRMÉ** (avec nuance) | LVMH devient minoritaire et « actionnaire principal » (décembre 2024, avec Anaïs Ventures). La Banque des Territoires crée une **société commune**, Les Domaines de Fontenille France : Manoir du Sphinx, fonds propres et prêt du Crédit Agricole. C'est une co-entreprise, pas la preuve d'une part dans la holding du groupe. Comptes consolidés 2024 : CA de 33,8 M€, EBE de +0,7 M€, RN de −2,9 M€. Les « environ 40 M€ » annoncés par la presse sont contredits. | https://www.caissedesdepots.fr/eclairage/actualites/reinventer-lhotellerie-et-renover-le-patrimoine-avec-les-domaines-de-fontenille | 2026-10-14 |
| V19 | Bolesworth : 150 locataires commerciaux et plus de 1 100 emplois (AV3) | Communiqué de British Showjumping (2019) ; site du domaine (2026) ; Companies House | **NON CONFIRMÉ** (auto-déclaration) | Le chiffre est repris à l'identique en 2019 et en 2026 (« over 150 thriving businesses »). Les comptes de Bolesworth Estate Company (00569378) sont des comptes de petite société, sans détail exploitable. | https://britishshowjumping.co.uk/news/the-barbour-family-launch-a-brave-new-era-for-bolesworth-estate- | 2026-10-14 |
| V20 | Arqana : CA de 32,9 M€ pour 210,8 M€ adjugés en 2024, soit 15,6 % (AV3) | Ratios INPI (438 241 788) ; statistiques officielles d'Arqana | **CONFIRMÉ** (chiffres), interprétation à corriger | CA de 32 908 424 € et RN de 6 054 778 €, mais pour l'**exercice clos le 31/03/2025** (avril 2024 à mars 2025). Volume 2024 (enchères et ventes amiables) : 210 814 300 €. Le ratio de 15,6 % rapproche deux périodes différentes et inclut des recettes hors commissions. Ce n'est pas un taux de commission. | https://www.arqana.com/statistiques_annuelles.html | 2026-10-14 |
| V21 | Quail Ridge : SBA 504 (40 %), banque (50 %), crédit-vendeur (10 %), sans apport personnel (AV4) | Page du podcast (transcription) ; règlement fédéral 13 CFR 120.910 et 120.912 | **PARTIELLEMENT CONFIRMÉ** | Le schéma 50/40/10 est standard. **L'apport de l'emprunteur peut être emprunté à un tiers**, à condition d'être subordonné (120.912). Il doit atteindre **15 %** pour un bâtiment à usage unique ou spécialisé (120.910), ce qui pourrait viser un golf. Le montage reste déclaratif. Les règles de crédit-vendeur citées par AV4 (SOP 50 10 8, juin 2025) concernent le **programme 7(a)**, pas le 504. | https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-13?part=120&section=120.910 | 2026-10-14 |
| V22 | Régime 150-0 B ter 2026 : 70 % réinvestis en 3 ans, conservation 5 ans, exclusions (AV4) | BOFiP BOI-RPPM-PVBMI-30-10-60-20-20260810 | **CONFIRMÉ** | Applicable aux cessions à partir du 21/02/2026 (loi n° 2026-103, art. 11). Sont **aussi exclues** : les activités immobilières, la construction en vue de la vente ou de la location, et les activités à **revenus garantis par un tarif réglementé de rachat ou un complément de rémunération** (cas de l'électricité solaire). Le rachat de titres existants doit conférer le contrôle. | https://bofip.impots.gouv.fr/bofip/12039-PGP.html/identifiant=BOI-RPPM-PVBMI-30-10-60-20-20260810 | 2026-10-14 |
| V23 | Strawbridge : château acheté 280 000 £ en 2015 (AV1, mission 1) | Guardian 2016 et 2022 ; Wikipédia (citant le Telegraph, payant) | **PARTIELLEMENT CONFIRMÉ** | Le Guardian de 2016 donne bien 280 000 £. Interview de 2022 : **345 000 € en octobre 2014, plus 50 000 € pour une parcelle du jardin clos**. 280 000 £ est une conversion approximative, et 2015 correspond à l'emménagement. | https://www.theguardian.com/lifeandstyle/2022/oct/29/castle-life-whats-next-for-esacpe-to-the-chateaus-dick-and-angel | 2026-10-14 |
| V24 | The Family : jugements des îles Caïmans (AV6) | Décisions du 04/12/2023 et du 06/08/2024 (PDF intégraux) | **CONFIRMÉ** | Jugement **par défaut** (défendeurs absents) : 3 420 969,75 € « misappropriated » et 3 946 818,22 € de manque à gagner. Sur 3 969 422 € reçus, 818 236 € ont été investis (Unison). Le 06/08/2024, les demandes de M. Ammar sont rejetées pour abus de procédure. | https://judicial.ky/n0c-storage/judgments-repository2/23-12-04-The-Family-Global-Godfathers-SPC-et-al-v-Oussama-Ammar-et-al-FSD-36-of-2022-RPJ-Judgment.pdf | 2026-10-14 |
| V25 | The Family : décisions de Londres (AV6) | [2026] EWHC 2433 (Comm), texte intégral | **CONFIRMÉ** | Jugement du 12/07/2024, rendu après non-respect d'une *unless order* du 06/06/2024. Montant fixé le 03/03/2025 : 6 488 497,92 £. Le 22/09/2026, M. Ammar est jugé en *contempt* sur les griefs 1, 5, 6, 7 et 12 (en partie). Peine à fixer ; appel possible. | https://caselaw.nationalarchives.gov.uk/ewhc/comm/2026/2433 | 2026-10-14 |
| V26 | The Family : liquidation judiciaire du 30/08/2022 (AV6) | BODACC (790 749 337 et 793 823 436) | **CONFIRMÉ** | The Family (Paris) SAS : cessation des paiements au 01/03/2021. TFMM : cessation au 28/07/2022. Liquidateur : Selarl Axyme. | https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records?where=registre%3D%22790749337%22 | 2026-10-14 |
| V27 | Domaine d'Ablon : Cottage Consulting et Théléma (AV6) | BODACC (851 220 053 et 424 579 837) | **CONFIRMÉ** | Théléma : créée en 2019 (président O. Ammar), administrateur provisoire en 2023, redressement judiciaire le 04/02/2026. Cottage Consulting : redressement judiciaire **dès le 12/01/2018**, plan de 9 ans arrêté le 12/06/2019, liquidation judiciaire le 16/10/2024. **Extension** le 11/03/2026 à la SCI Ablon et à la SCI Garnier ; liquidation judiciaire des Terres d'Ablon le 22/04/2026. | https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records?where=registre%20like%20%22424579837%22 | 2026-10-14 |
| V28 | Burghley Horse Trials : 5,35 M£ de CA et 22,5 k£ de résultat d'exploitation (AV2) | Comptes audités iXBRL, exercice clos le 31/01/2024 | **CONFIRMÉ** | CA de 5 350 245 £, marge brute de 1 543 313 £, résultat d'exploitation de 22 500 £ (468 078 £ l'année précédente). Bénéfices versés à la charity mère par Gift Aid. Les opérations avec la société mère ne sont pas publiées (exemption FRS 102) : le résultat de la filiale sous-estime peut-être l'apport du concours au domaine. | https://find-and-update.company-information.service.gov.uk/company/07087188/filing-history/MzQzODcxNzQxNGFkaXF6a2N4/document?format=xhtml&download=1 | 2026-10-14 |
| V29 | Castle Howard : perte d'exploitation malgré une fréquentation en hausse (AV2) | Comptes iXBRL, exercice clos le 31/01/2025 | **CONFIRMÉ** | 296 740 visiteurs (+13 %), CA de 14 754 343 £ (−4 %), perte d'exploitation de −2 020 253 £, réévaluation de +2 454 666 £, résultat de −280 439 £, 236 salariés. | https://find-and-update.company-information.service.gov.uk/company/00480214/filing-history/MzQ4NTM0NjMxOGFkaXF6a2N4/document?format=xhtml&download=1 | 2026-10-14 |
| V30 | Pitchford Hall : rachat en 2016 ; un revenu solaire qui permet d'emprunter (AV2) | Communiqué de SAVE (05/10/2016) ; Companies House (08751648) ; site du domaine | **PARTIELLEMENT CONFIRMÉ** | Rachat de 2016 confirmé. Une société **PITCHFORD (CONDOVER AIRFIELD & STOCKBATCH) LIMITED** existe depuis 2013 : production d'électricité (code 35110), contrôlée par Viners Energy Ltd (écosystème Octopus). Stockbatch est une propriété du domaine. Une centrale sur les terres du domaine est donc plausible, mais elle appartient à un tiers. Que son revenu (sans doute un loyer) ait servi de levier d'emprunt reste un propos. | https://find-and-update.company-information.service.gov.uk/company/08751648 | 2026-10-14 |
| V31 | Haras de Castillon : 250 ha selon TDN, contre 1 250 ha selon The Owner Breeder (AV2) | TDN (20/10/2025) ; The Owner Breeder (08/12/2025) | **PARTIELLEMENT CONFIRMÉ** (250 ha) | Citation de B. Jeffroy dans TDN : « 30 hectares, and now we're pretty much up to 250 hectares ». The Owner Breeder écrit « nearly 1,250 hectares » : **CONTREDIT** (incohérent avec 30 ou 35 ha en 2015). Aucune source au registre. | https://wp.tdn.pmadv.com/?p=494552 | 2026-10-14 |
| V32 | Blenheim : « a million visitors a year » (propos de podcast, signalé par AV2) | Comptes de la Blenheim Palace Heritage Foundation au 31/03/2025 (p. 12, lue en image) | **CONTREDIT** | « Paying visitor numbers… totalled 700,000 (2024: 698,000) ». Ce chiffre couvre le palais, le parc et les jardins. Le « million » ne vaut au mieux qu'en ajoutant des entrées non payantes, sans source. | https://find-and-update.company-information.service.gov.uk/company/09430048/filing-history/MzQ4ODEzMTc4M2FkaXF6a2N4/document?format=pdf&download=0 | 2026-10-14 |
| V33 | Highclere : le tournage aurait peu rapporté (AV2, non vérifié) | Spear's (403, non contourné) ; Henley Standard (27/10/2025) ; PBS ; The Ringer ; 2 WebSearch | **NON CONFIRMÉ** | Aucun montant de cachet et aucune citation trouvés. Henley Standard : « not only the money that filming would bring… But the money is useful too ». The Ringer : 1 200 visiteurs par jour à 26 $, environ 2 mois par an. | https://www.henleystandard.co.uk/news/literature/700462/wined-and-dined-for-downton.html | 2026-10-14 |
| V34 | Haras de Fresnay-le-Buffard : vente à Al Wathba Stud ; 26,8 M€ affichés, 28 M€ « reported » ; environ 80 à 86 k€/ha (AV2) | Communiqué d'Addleshaw Goddard (06/01/2025) ; DVF 2024, Orne | **PARTIELLEMENT CONFIRMÉ** | Acquéreur confirmé, bien « mis en vente pour 26 millions ». DVF du 26/12/2024 : **21 546 500 € pour 214,4 ha** (Neuvy-au-Houlme, qui inclut l'ancienne commune de Fresnay-le-Buffard, Habloville, Ri, Rônai et Monts-sur-Orne), avec 23 logements distincts, 3 dépendances et 2 locaux. C'est très probablement le haras, soit environ 100 k€/ha. **Les 28 M€ sont CONTREDITS**, sous réserve de lots vendus à part. Le DVF exclut le mobilier et le cheptel. | https://files.data.gouv.fr/geo-dvf/latest/csv/2024/departements/61.csv.gz | 2026-10-14 |
| V35 | Haras nationaux de Bretagne : cédés 400 k€ (Lamballe) et 750 k€ (Hennebont) en 2016 ; 27 M€ de gestion entre 2017 et 2023 (AV2) | Breizh-info (28/04/2025, citant la chambre régionale des comptes) ; extrait Banque des Territoires (2016) | **PARTIELLEMENT CONFIRMÉ** | Les deux prix sont recoupés par une dépêche de 2016 (extrait de recherche ; site en maintenance). Le rapport de la chambre régionale des comptes n'a pu être ouvert (ccomptes.fr injoignable). Les 27 M€, les valeurs estimées et les 53 000 visiteurs restent de seconde main. Un autre article Breizh-info parle de 22 000 visiteurs payants en 2022 : l'indicateur n'est pas le même. | https://www.breizh-info.com/2025/04/28/246377/haras-nationaux-de-bretagne-une-reconversion-couteuse-et-encore-inaboutie/ | 2026-10-14 |

## 4. Corrections importantes à reporter dans les recommandations

1. **Fontenay : le prix réel est d'environ 0,75 M€, pas 2 M€.**
   - D'après le DVF, l'acquisition du 20/12/2023 vaut 746 600 € pour 11,61 ha.
   - Le communiqué parlait d'un château « d'une valeur d'environ 2 millions d'euros », et le club deal a valorisé le projet à environ 2 M€ avant levée, soit environ 2,7 fois le prix d'achat.
   - Le « montage Fontenay » a donc fait payer aux investisseurs une valorisation de projet (travaux, audience, prime des porteurs), et non un actif.
   - Les obligations sont dues par la **société d'exploitation** (Sarthe Society, capital de 12 755 €) à l'échéance du 31/01/2029.
   - **Le mur de refinancement est confirmé.**
2. **Fontenay : promesse incohérente.** Le communiqué présente un « objectif de doubler » l'investissement à propos d'obligations à 7 % fixe remboursables vers 5 ans. Même capitalisé, 7 % sur 5 ans donne au plus 1,40 fois la mise. Il ne faut pas reprendre cette promesse.
3. **Dampierre : ne pas écrire « 8 fois ».**
   - Le château vaut entre 3,6 et 7 fois moins que les autres lots.
   - Le prix de référence des terres de l'Aube (2021) est d'environ **21 900 €/ha** (DVF), et non de 21 000 €/ha.
   - La forêt de 210 ha à 2,1 M€ n'est pas documentée dans le DVF.
4. **Le Barn :**
   - 72 chambres et un domaine de 165 ha d'après le site officiel (et non 60 ou 73 chambres, 250 ha ou 500 acres) ;
   - la séparation entre les murs et l'exploitation date d'un **apport partiel d'actif de 2022** ;
   - en 2025, les deux sociétés perdent ensemble environ 0,48 M€.
5. **Arqana : exercice d'avril à mars.** Le ratio CA/volume de 15,6 % n'est pas un taux de prélèvement. Commissions annoncées : 6 % côté vendeur et 6 % côté acheteur, plus d'autres recettes.
6. **Quail Ridge.** Le montage « sans apport » du programme SBA 504 repose sur un apport **emprunté et subordonné**, que le règlement autorise. Il n'y a **pas d'équivalent français** à cette garantie fédérale sur 25 ans. Le garde-fou SOP 50 10 8 cité par AV4 concerne le programme 7(a).
7. **150-0 B ter : ajouter deux exclusions.**
   - Les **activités immobilières** sont exclues, comme la location meublée. Gîtes et chambres d'hôtes louées « nues » risquent donc d'être exclus.
   - Les **revenus à tarif réglementé** sont exclus. L'agrivoltaïsme sous obligation d'achat ou complément de rémunération ne peut pas recevoir ces fonds (lien avec l'idée 3 d'AV2).
8. **Strawbridge : 345 000 € en octobre 2014, plus 50 000 €** (Guardian, 2022), au lieu de « 280 000 £ en 2015 ».
9. **Fresnay-le-Buffard.** Environ 21,5 M€ pour 214 ha d'après le DVF, soit environ 100 k€/ha. Les 28 M€ ne sont pas confirmés. Il faut recalculer le repère à l'hectare d'AV2.
10. **Bevouac** est une société de conseil en investissement immobilier en liquidation. Ce n'est **pas** une société d'hébergement, ni une associée des sociétés de Fontenay. Sarthe Society, la SCI et Bevouac déclarent cependant **le même siège** (22 rue de l'Abbé Groult, Paris 15e). C'est un point de gouvernance à surveiller, sans conséquence juridique établie.
11. **Fontenille.** La Caisse des Dépôts intervient par une **co-entreprise** dédiée aux acquisitions françaises. Il n'est pas prouvé qu'elle détienne une part de la holding du groupe. Le CA 2024 est de 33,8 M€, et non « environ 40 M€ ».
12. **Quétiéville.** La structure est un groupement foncier agricole (GFA) pour les terres et une société civile d'exploitation agricole (SCEA) pour l'activité : c'est le montage agricole français classique, transposable. Les performances annoncées viennent d'un porteur qui est aussi **investisseur et ambassadeur de la plateforme** qui collecte.

## 5. Affirmations relevant du « marketing » non étayé

À ne pas reprendre comme des faits dans les recommandations finales :

| Affirmation | Origine | Statut AV8 |
|---|---|---|
| Château de Fontenay « d'une valeur d'environ 2 millions d'euros », « classé monument historique », « objectif de doubler » l'investissement | communiqué des porteurs, 2023 | prix réel de 0,75 M€ (DVF) ; protection non trouvée ; promesse incohérente avec 7 % |
| Fontenay : CA de 13 k€, 116 k€ puis 400 k€, « 2 048 prêteurs en 3 jours », « 310 000 € en 12 h » | podcasts et communiqué | comptes confidentiels, chiffres invérifiables |
| Quétiéville : de 0 à 50 chevaux, 100 % de remplissage, 1 M€ « en 50 minutes » | Bricks et Tony Parker (investisseur et ambassadeur de Bricks) | source unique et intéressée |
| Blenheim : « a million visitors a year » | podcast (Skip the Queue) | contredit : 700 000 visiteurs payants |
| Polo de Chantilly : répartition 50/25/25 | directeur du club | propos exact, aucun compte |
| Bolesworth : « over 150 commercial tenants », plus de 1 100 emplois | communiqué et site du domaine | auto-déclaration constante, non auditée |
| Castle Leslie : mariage McCartney « vu par 800 millions » de personnes | document de l'entreprise | chiffre de communication |
| Spruce Meadows : plus de 210 M$ de dotations ; LGCT : renouvellement Longines à plus de 100 M€ | intervenants et presse de seconde main (AV3) | non vérifiés |
| Milandes : de 45 000 à 193 000 visiteurs ; Camp Chateau : « second site financé en sept jours » | intervenants (AV1) | non vérifiés |
| The Family : alumni ayant levé « plus d'1,5 milliard de dollars » ; C. Delaune : « de 0 à 180 millions en 3 ans » | auto-déclarations (AV6) | non vérifiés. Au registre, la société d'exploitation d'Ablon, présidée par C. Delaune en 2016, était en redressement judiciaire dès 2018 |
| Fontenille : « environ 40 M€ » de CA en 2024 | presse (TourMaG), projection | contredit : 33,8 M€ en consolidé |
| Highclere : le tournage « n'a pas beaucoup rapporté » | résumé de moteur de recherche (Spear's) | non confirmé |

## 6. Volets judiciaires : présomption d'innocence

- Les décisions des îles Caïmans (V24) et de Londres (V25) sont **civiles**.
  - Les montants ont été fixés **par défaut** ou à la suite d'une **sanction procédurale**, sans procès contradictoire sur le fond.
  - La décision du 22/09/2026 applique le standard de preuve pénal, mais porte **sur l'outrage au tribunal** (gel d'avoirs, déclarations), **pas sur le détournement**.
  - La peine n'est pas fixée et un appel est possible.
- **En France, aucune condamnation pénale de M. Ammar dans l'affaire The Family n'est connue à ce jour.**
  - La garde à vue de février 2025 et l'enquête du parquet national financier sont rapportées par la presse ; AV8 ne les a pas revérifiées.
  - Une garde à vue n'est ni une mise en examen ni une condamnation.
  - La condamnation de 2018 (affaire Be Sport) reste **non vérifiée**, et les sources de presse se contredisent.
- Les procédures collectives d'Ablon (V27) ne disent rien des causes : le BODACC ne publie pas les motifs.

## 7. Annexe : contrôles ponctuels complémentaires (hors sélection)

| Contrôle | Source | Résultat |
|---|---|---|
| Les Kasteliades (AV1), exercice clos le 31/10/2023 | ratios INPI 507 673 655 | CA de 701 564 €, résultat d'exploitation de −215 734 €, RN de +3 € : **confirmé**. **Nuance** : l'EBE est **positif à +155 225 €** (22 % du CA). Le déficit d'exploitation vient des amortissements, pas de l'activité courante. |
| Hickstead (AV3), exercice clos le 31/01/2026 | comptes iXBRL 00659028 | « amount due to the directors was £1,500,000 », 22 salariés : **confirmé** |
| Haras de Divona et sa foncière ; Prello (AV7) | BODACC | Liquidation judiciaire de l'exploitation le 07/12/2021, puis redressement de la foncière le 21/02/2023 et liquidation le 02/07/2024. Prello : redressement judiciaire le 13/02/2025, liquidation le 17/04/2025. **Confirmé.** Le lien capitalistique Divona reste « probable », comme l'écrit AV7. |
| Tableau d'AV5 (La Coste, Étangs, Crayères, Primard) | ratios INPI | La Coste (consolidé 2024) : 36,6 M€, EBE de 10,9 M€, RN de −8,9 M€. Étangs (2025) : 3,47 M€, RN de −3,2 M€. Crayères (2024) : 17,8 M€, RN de +1,31 M€. Primard (2025) : 6,67 M€, RN de −1,69 M€. **Tout est exact.** |
| Châteaux des Langues ; Castel Naustra (AV1) | ratios INPI | Châteaux des Langues : RN de 18 498 € (2024) et 19 520 € (2025), **confirmé**. Castel Naustra : RN 2024 de 220 630 € au registre INPI ; le chiffre 2025 d'AV1 (222 296 €) n'y figure pas encore. |

## 8. Conclusion : fiabilité globale du corpus

**1. Les faits de registre sont fiables.**
- Tous les montants issus de BODACC, de l'INPI, de Companies House et des décisions de justice se sont révélés **exacts au chiffre près** : comptes du Theil, de Burghley, de Castle Howard, de Blenheim, d'Arqana, du Barn et de Fontenille ; procédures The Family et Ablon.
- Les écarts relevés sont des **étiquettes** (exercice décalé d'Arqana, date de parution BODACC) et non des erreurs de chiffres.

**2. Le marquage des statuts par les agents est globalement honnête.** Les chiffres déclaratifs étaient presque toujours signalés comme tels (DÉCLARÉ, AFFIRMÉ, REPÉRÉ). Trois faiblesses :
- (a) **deux affirmations d'absence** se sont révélées fausses : la vente de Fontenay est bien en DVF ; le domaine de Dampierre n'est documenté qu'en partie ;
- (b) quelques **ratios d'interprétation** sont abusifs : « 8 fois moins cher », « prélèvement de 15,6 % » ;
- (c) un **conflit d'intérêts** n'a pas été relevé : le porteur de Quétiéville est investisseur dans la plateforme qui collecte.

**3. Les chiffres d'exploitation venus des podcasts sont structurellement invérifiables.**
- Remplissage, chiffre d'affaires, répartition des recettes, nombre de locataires : les sociétés concernées publient des comptes confidentiels ou sont des sociétés civiles.
- Quand une vérification a été possible, le chiffre de communication était **surévalué** : Blenheim, valeur de Fontenay, Fresnay, Castillon.

**4. Les prix relayés par la presse doivent être recoupés avec le DVF** à chaque fois que c'est possible (ventes françaises depuis 2021). Le DVF a corrigé ou précisé trois prix sur quatre testés : Fontenay, Dampierre, Fresnay.

**Appréciation par agent** (sur l'échantillon contrôlé) :

| Agent | Appréciation | Points d'attention |
|---|---|---|
| AV5 | très bonne | nombre de chambres du Barn ; nature de l'entrée de la Caisse des Dépôts |
| AV6 | très bonne | décisions exactes ; présomption d'innocence respectée |
| AV2 | très bonne | repère à l'hectare de Fresnay à recalculer ; conflit d'intérêts de Quétiéville non signalé |
| AV1 | bonne | absence de vente en DVF fausse ; « 8 fois » ; date de parution BODACC ; EBE positif omis pour les Kasteliades |
| AV4 | bonne | activité de Bevouac ; règles 7(a) appliquées au 504 ; exclusions 150-0 B ter incomplètes |
| AV3 | bonne | exercice d'Arqana ; nombre de chambres du Barn |
| AV7 | bonne | petit échantillon, entièrement confirmé |

**Verdict global.** Le corpus est **utilisable pour des recommandations**, à deux conditions :
1. ne retenir comme base chiffrée que les lignes **CONFIRMÉ** et **PARTIELLEMENT CONFIRMÉ**, avec les corrections de la section 4 ;
2. présenter tous les indicateurs d'exploitation tirés des podcasts comme des **hypothèses d'entretien**, jamais comme des preuves.

**Limites de cette vérification.**
- L'API Recherche d'entreprises, la base Mérimée et ccomptes.fr étaient injoignables. Le statut de monument historique de Fontenay et le rapport de la chambre régionale des comptes sur les haras bretons restent à vérifier.
- Le DVF n'identifie pas les acquéreurs : les rapprochements Fontenay et Fresnay reposent sur la date, le lieu, la surface et la composition des biens.
- Aucun document de la plateforme Bricks (document d'information des offres) n'a été trouvé en accès libre.
