# AV4 — Fiches d'analyse : acquisition et financement

Agent AV4 « Acquisition et financement » (cellule audiovisuelle, mission 2), le 14/10/2026.
Spécialités couvertes :
- (9) acquisitions d'actifs importants avec peu d'apport ;
- (10) private equity et family offices ;
- (11) immobilier entrepreneurial (hôtels, domaines, campings) ;
- (12) reprises d'entreprises comme levier de patrimoine.

Fichiers liés :
- catalogue : `_brut/catalogue_AV4.csv` (139 contenus, identifiants AV4-001 à AV4-139) ;
- sources et vérifications : `_brut/sources_AV4.csv` (S-AV4-01 à 65) ;
- cas réels : `03_CAS_REELS/AV4_cas.md` ;
- idées : `04_IDEES_STRATEGIQUES/AV4_idees.md`.

## Méthode et limites (à lire avant les fiches)

**Rien n'a été écouté ni regardé.** Aucun outil audio n'est disponible et aucun média n'a été téléchargé. Les niveaux d'accès réels sont les suivants.

| Niveau | Ce qui a été lu |
|---|---|
| TRANSCRIPTION TEXTE LUE (partielle) | Transcriptions publiées par l'hôte, lues par passages ciblés (recherche de mots-clés puis lecture des passages). Sources : Acquired (LVMH), Acquiring Minds (golf Quail Ridge, Galindo), BiggerPockets (#68 Deibel, Rookie 375), Defining Hospitality (#100 Chip Conley) |
| DESCRIPTION/CHAPITRES LUS | Notes d'épisode des sites (La Martingale, GDIY, Hospitality Insiders), flux RSS officiels des podcasts (timelines horodatées par les auteurs) et flux RSS officiels des chaînes YouTube (descriptions complètes) |
| Chapitres YouTube | Lus dans les pages de résultats de recherche YouTube, avant la consigne du directeur (429). L'origine « auteur » des chapitres n'est confirmée que pour GDIY, Richissime et Bpifrance (même minutage dans les notes de l'auteur). Pour les autres vidéos, elle est probable mais non prouvée |
| INACCESSIBLE (captcha / 429) | Toutes les pages vidéo YouTube (watch) : dates exactes et descriptions inaccessibles pour les vidéos anciennes |
| REPÉRÉ | Titre, chaîne, durée et ancienneté vus seulement dans un résultat de recherche |

Règles appliquées aux horodatages et aux chiffres :
- **Horodatages** : seuls des minutages écrits par les auteurs (chapitres ou timelines) sont cités. Les liens `&t=` sont dérivés des chapitres affichés par YouTube. Les minutages des timelines audio (flux RSS) ne valent que pour la version audio.
- **Chiffres** : chaque montant est classé selon l'un des statuts suivants.
  - **VÉRIFIÉ** : registre public (BODACC, API annuaire des entreprises) ou page officielle lue.
  - **RECOUPÉ** : deux sources concordantes.
  - **DÉCLARATIF** : propos de l'invité ou de l'hôte, non vérifié.
  - **CONTREDIT** : une source fiable dit autre chose.
- **Budget WebSearch** : 13 requêtes utilisées sur 25 (dont une en erreur). Les découvertes ont été faites surtout par les flux RSS, les recherches WordPress des sites d'émissions et l'API Apple Podcasts.
- **Podcasts du brief non trouvés** :
  - « J'ai un pote dans la finance » : aucun flux identifié via l'annuaire Apple ;
  - « Le Board » : le podcast trouvé sous ce nom concerne les freelances, il est hors sujet ;
  - « Le Podcast du repreneur » et « Search Fund Accelerator » : aucun flux identifié.

  Le contenu « reprise » vient donc de Bpifrance, du CRA, de GDIY, de Finscale, du Panier et de chaînes YouTube spécialisées.

---

## Tableau de vérification des affirmations « sans apport »

| Affirmation (contenu) | Ce qui a été vérifié | Verdict |
|---|---|---|
| « Ils ont acheté un château avec 10 000 euros » (La Martingale, AV4-002/003) | BODACC : la société d'exploitation SARTHE SOCIETY est créée au capital de **10 000 €** (annonce du 25/10/2023). L'extrait du 29/09/2026 précise **5 000 € par associé**. Le capital passe ensuite à **12 755 €** (BODACC du 13/03/2024) : les investisseurs détiennent 2 755/12 755 = **21,6 %**, ce qui correspond aux « 22 % contre 551 000 € » annoncés | **Exact sur l'apport personnel, trompeur sur l'effort.** Le château a mobilisé environ **1,24 M€ de capitaux tiers** : 551 k€ de fonds propres d'investisseurs et 690 k€ d'obligations à 7 %. Le budget annoncé est de 2 M€ |
| « Ils achètent un château sans les banques », « financer sans crédit » (Richissime, AV4-015) | Les 690 k€ levés sur Bricks sont de la **dette obligataire** à 7 % par an, plus des frais de plateforme (La Martingale ; communiqué de décembre 2023 lu par la mission 1, S36) | **Inexact sur « sans crédit »** : le crédit bancaire a été remplacé par un crédit participatif plus cher. Exact sur l'absence de banque au moment de l'acte |
| « Buying a $7.3m Golf Course with No Money Down » (Acquiring Minds, AV4-116) | Structure décrite par l'hôte et l'invité : SBA 504 (40 %), prêt bancaire (50 %), crédit-vendeur (10 %), amortissement sur 25 ans. Aucune source indépendante consultée | **Plausible mais exceptionnel.** Les conditions sont réunies : directeur en poste depuis des années, cash-flow de 500-700 k$, vendeurs motivés par la continuité, programme fédéral américain. **Sans équivalent direct en France** |
| « How to Buy a Business With No Money » et « for $0 in a Week » (Codie Sanchez, AV4-123/124) | Depuis le **01/06/2025** (SOP 50 10 8), un rachat financé par un prêt SBA 7(a) exige **au moins 10 % d'apport**. Le crédit-vendeur ne compte que s'il est en standby total (aucun paiement) pendant toute la durée du prêt, et pour au plus la moitié de l'apport (Whiteford, page lue) | **Obsolète pour les rachats SBA 7(a) depuis juin 2025** et non transposable en France. Ce sont des contenus d'appel pour des services payants |
| « 3x with a bank loan, 10% down » (Walker Deibel, BiggerPockets #68, AV4-119) | Transcription : l'hôte décrit son propre rachat financé par le vendeur. Acompte d'environ **30 %** (valeur du stock), 70 % payés sur 2 ans. Il demande si « no money down » est la norme ou si 10-20 % est normal | **Le témoignage contredit le mythe du zéro apport** |
| Motel financé par le vendeur (BiggerPockets Rookie 375, AV4-120) | Transcription : **50 k$ d'arrhes + 250 k$ d'apport = 300 k$** | **Crédit-vendeur ne signifie pas sans apport** |
| « Dimitri a repris sans apport », « Sarah et Clément : 3 entreprises sans apport », « 8 boîtes rentables sans cash perso » (1,18 M de vues), « sans apport et sans caution » (AV4-039/041/042/043) | Sociétés non nommées dans les métadonnées. Registre consulté pour « Alexandre Barthelemy » : nombreux homonymes, aucune société identifiable. Repère de place (CRA, page lue) : un crédit-vendeur couvre **30 à 50 %** du prix, sur 1 à 5 ans, et l'acheteur paie 50 à 70 % au closing | **Non vérifiable.** À traiter comme du marketing (chaînes vendant formation ou coaching) |
| « 85 % de survie en reprise vs 40 % en création » (webinaire Boring Business, AV4-054, chapitre 1:04:19) | INSEE Centre-Val de Loire : pérennité à 5 ans de **70 %** pour les entreprises reprises, contre **61 %** pour l'ensemble des entreprises classiques. INSEE national : 69 % des entreprises créées en 2018 encore actives à 5 ans (hors micro) | **CONTREDIT / exagéré.** L'écart réel est d'environ 8 à 16 points selon les cohortes, pas 45 |
| « Bâti un empire hôtelier à 25 ans sans le moindre sou » (titre Venture Social, AV4-136) | Wikipédia (qui cite le San Francisco Chronicle) : Chip Conley a **levé 1 M$** en 1987 pour acheter le Phoenix Hotel | **Trompeur.** Peu ou pas d'argent personnel, mais 1 M$ d'argent d'investisseurs |
| Arnault « a transformé 15 M$ en fortune » (Acquired, AV4-115) | Acquired : 15 M$ de la famille sur une offre de 60 M$. Wikipédia FR (qui cite Libération) : 90 MF de fortune familiale, 400 MF à réunir, plus des trois quarts apportés par le tour de table Lazard. L'État apportait 745 MF | **RECOUPÉ.** Ce n'est pas « sans apport » : environ 20-25 % de fonds propres, beaucoup d'argent des autres et un vendeur public aux objectifs non financiers |

**Constat transversal.** Aucun des cas vérifiés n'est réellement sans argent. Le schéma réel est toujours le même : un **petit apport du porteur**, puis **l'argent des autres** (investisseurs minoritaires, vendeur, plateforme, État) obtenu grâce à un **atout non financier**. Cet atout peut être une audience, une compétence d'exploitant, la confiance du vendeur ou un réseau bancaire.

---

## F01 — La Martingale #336 « Acheter un château : un investissement rentable ? » et extraits (Domaine de Fontenay)

### Identification

- **Réf. catalogue** : AV4-001 (audio), AV4-002 (vidéo), AV4-003 à 005 (extraits).
- **Titres** :
  - flux RSS : « #336 - Gagner de l'argent avec un château : la méthode complète - Jérémy Nabais » ;
  - page web : « Acheter un château : un investissement rentable ? » ;
  - vidéo : « Ils ont acheté un château avec 10 000 euros - Jérémy Nabais » ;
  - extraits : « Comment acheter un château quand on n'a que 10 000 euros d'apport ? », « Combien coûte un château une fois qu'on l'a acheté ? », « Questions pour un jeune châtelain ».
- **Intervenant** : Jérémy Nabais, créateur du podcast immobilier « Ça fait un bail ! » et cofondateur du Domaine de Fontenay avec Martin Menez. Hôte : Matthieu Stefani.
- **Chaîne** : La Martingale (Orso Media).
- **Date** : 24/09/2026 pour l'audio. Extraits YouTube du 29/09 et du 01/10/2026. Date exacte de la vidéo intégrale inaccessible (« il y a 2 semaines »).
- **Durée** : 1:02:26 (audio), 1:04:11 (vidéo).
- **URL** :
  - https://lamartingale.io/tous/acheter-un-chateau-un-investissement-rentable/
  - https://www.youtube.com/watch?v=-sDU8zOpqXQ
  - extraits : https://www.youtube.com/watch?v=NSogHMSmUhA , https://www.youtube.com/watch?v=vZ5qlVgZNnI , https://www.youtube.com/watch?v=8WFTmr1Nb70
- **Niveau d'accès** : DESCRIPTION/CHAPITRES LUS (notes détaillées du site, chapitres YouTube, descriptions des extraits via le flux RSS officiel de la chaîne). **Audio non écouté.**

### Analyse

**Résumé.** Deux trentenaires sans fortune achètent en 2023 un château médiéval de 12 ha dans la Sarthe, à 1h20 de Paris. Ils en font un lieu de séminaires, de mariages et de séjours privatisés. L'épisode raconte le financement, les travaux et les premiers revenus. Nabais parle de « rendement entrepreneurial » : créer la valeur autour du bien au lieu d'attendre sa revalorisation.

**Informations entrepreneuriales.**
- Positionnement « maison de famille » privatisée plutôt qu'hôtel classique.
- Priorité aux couchages : le pavillon est transformé en 13 chambres, 36 couchages et 11 salles de bain.
- Le levier du modèle, ce sont les séminaires clés en main (repas, activités, navettes), pas la simple location du lieu.
- Erreurs reconnues :
  - sous-estimation de l'entretien des 12 ha ;
  - matériel adapté acheté trop tard ;
  - premier salarié sur place recruté trop tard.

**Modèle économique.** Le domaine privatisé vend trois produits :
- séminaires de 5 000 à 31 000 € (record : 61 000 €) ;
- mariages à 13 500 € ;
- séjours de groupes.

Une salle de réception est en projet, et des cabanes en bord de rivière sont envisagées.

**Financement**

| Brique | Montant | Coût / contrepartie | Statut |
|---|---|---|---|
| Apport des fondateurs (2 × 5 000 €) | 10 000 € | capital social de la société d'exploitation | **VÉRIFIÉ** (BODACC : capital de création 10 000 €) |
| Levée en capital auprès d'investisseurs (33 selon Hospitality Insiders) | 551 000 € | environ 22 % du capital sur une valorisation d'environ 2 M€. Sortie promise en 2030-2035 avec un objectif de mise doublée | **RECOUPÉ** : BODACC, capital porté à 12 755 €, soit 21,6 % de nouveaux titres. Les 551 k€ impliquent une valorisation avant levée d'environ 2,0 M€, cohérente avec le chiffre annoncé |
| Financement bancaire | 0 € au closing | la banque se retire « quelques semaines » avant la signature (« trois semaines » selon Hospitality Insiders) | DÉCLARATIF, deux sources concordantes |
| Obligations Bricks (environ 2 048 prêteurs selon Hospitality Insiders ; « environ deux tiers » du montant grâce aux auditeurs selon La Martingale) | 690 000 € | 7 % par an + frais de plateforme. Liquidité visée au 31/01/2029 (communiqué de décembre 2023, mission 1) | **RECOUPÉ** (montant et taux) |
| Refinancement | — | refinancement bancaire visé « dès que l'exploitation le permettra » | intention |

**Structure juridique vérifiée** (annuaire des entreprises et BODACC) :
- deux holdings personnelles : JN FOX HOLDING (Nabais, SAS créée le 08/08/2023) et HOLDING AIGUILLE DES GLACIERS (Menez, SAS créée le 04/08/2023) ;
- une société d'exploitation : SARTHE SOCIETY (SAS, code NAF 55.20Z hébergement touristique, début d'activité le 01/09/2023), Nabais président, Menez directeur général ;
- une société civile immobilière : SCI CHATEAU DE FONTENAY (capital 1 000 €, immatriculée le 09/11/2023), cogérée par les deux associés. Elle a pour associés les deux holdings **et** SARTHE SOCIETY.

C'est un montage **holdings → SCI (murs) + SAS (exploitation)**. Le capital nominal minime (1 000 € et 10 000 €) n'empêche pas de lever de la prime d'émission.

**Difficultés évoquées.**
- Retrait de la banque juste avant l'acte, d'où une levée d'urgence de 690 k€.
- Coût de la dette participative (7 % + frais).
- Charges fixes d'environ 20 000 €/mois, dont environ 1 000 € d'assurance.
- Démarches ERP (« milliers de CERFA »).
- Entretien du parc.

**Chiffres cités et statut**

| Chiffre | Statut |
|---|---|
| Prix d'achat 780 000 € | DÉCLARATIF (non vérifié au fichier immobilier) |
| 426 000 € de travaux pour 400 m² (pavillon) | DÉCLARATIF |
| CA : 13 000 € (année 1), 116 000 € (année 2), environ 400 000 € attendus (2026) | DÉCLARATIF. Les comptes sont déposés (BODACC 2025 et 2026) mais leur contenu n'est pas visible dans l'API |
| Objectif d'EBITDA 100 000 € | objectif |
| Prévisions 500 k€ (2027) et 800 k€ (2028) | **projections, explicitement présentées comme telles** par La Martingale |

**Limites.**
- Résumé rédigé par l'émission, propos non entendus.
- Les comptes ne sont pas consultés.
- L'écart entre le budget de 2 M€ (Hospitality Insiders) et les ressources identifiées (environ 1,25 M€) n'est pas expliqué.
- La sortie promise aux investisseurs (doubler la mise en 2030-2035) et l'échéance obligataire de 2029 créent un **mur de refinancement**. Le documentaire s'intitule « On a 2 ans pour sauver ce château » : le lien avec cette échéance est une hypothèse, non une information.

**Application au projet.** C'est le **précédent français le plus proche** d'un jeune porteur sans patrimoine qui contrôle un château. Quatre enseignements :
1. **L'apport se remplace par une audience et une crédibilité.** Environ deux tiers des 690 k€ sont venus des auditeurs du podcast.
2. **La valorisation du projet** (2 M€ avant levée pour 10 k€ apportés) permet de garder environ 78 % du capital.
3. **Le montage holdings / SCI / SAS** est directement réutilisable.
4. **Le risque bancaire de dernière minute** impose un plan B financé avant le compromis.

Points d'écart avec le projet du client :
- un domaine équestre de plus de 50 ha coûtera plusieurs fois plus cher : à transposer en multipliant chaque brique ;
- l'habitation privée sur place doit être isolée juridiquement des investisseurs (voir idées I1 et I8) ;
- l'échelle de 12 ha et la cible de séminaires B2B à 1h20 de Paris sont des facteurs de succès à reproduire.

### Passages importants (chapitres YouTube de la vidéo intégrale)

- 10:15 — Les critères principaux pour ce type de projet : https://www.youtube.com/watch?v=-sDU8zOpqXQ&t=615s
- 18:49 — Le choix du positionnement et son impact : https://www.youtube.com/watch?v=-sDU8zOpqXQ&t=1129s
- 21:57 — Négociation et décryptage de l'investissement (prix, frais, charges) : https://www.youtube.com/watch?v=-sDU8zOpqXQ&t=1317s
- 24:16 — Les meilleures stratégies pour se faire financer : https://www.youtube.com/watch?v=-sDU8zOpqXQ&t=1456s
- 31:31 — Immersion dans les travaux du château : https://www.youtube.com/watch?v=-sDU8zOpqXQ&t=1891s
- 36:06 — Comment lever 690 000 euros en urgence : https://www.youtube.com/watch?v=-sDU8zOpqXQ&t=2166s
- 40:38 — Les étapes les plus importantes quand on rachète un château : https://www.youtube.com/watch?v=-sDU8zOpqXQ&t=2438s
- 48:06 — Le business plan : https://www.youtube.com/watch?v=-sDU8zOpqXQ&t=2886s
- 1:01:02 — Verdict : est-ce que ça vaut le coup ? : https://www.youtube.com/watch?v=-sDU8zOpqXQ&t=3662s

**Note : 95/100.** Témoignage le plus directement transposable de tout le corpus AV4, chiffré, et vérifié en partie par les registres.

---

## F02 — Corpus « Ça fait un bail ! » (podcast de Jérémy Nabais) sur l'achat de Fontenay

### Identification

- **Réf. catalogue** : AV4-007 à AV4-014.
- **Contenus** :

| Réf. | Titre | Date | Durée |
|---|---|---|---|
| AV4-007 | #128 « Acheter, Rénover et Rentabiliser un château ! Guide complet » (YouTube Uvjj7GlRjws, 24:52) | 03/09/2023 | 25:38 |
| AV4-008 | #140 « On achète un château médiéval avec vous ! » | 03/12/2023 | 1:38:54 |
| AV4-009 | « Visite audio-guidée du domaine de Fontenay » | 07/12/2023 | 18:12 |
| AV4-010 | « Financer son projet sans banque - Cédric O'Neill, fondateur de Bricks » | 31/03/2024 | 1:04:28 |
| AV4-011 à 013 | « Château Story », chapitres 1 à 3 | 05/05, 16/06 et 02/09/2024 | — |
| AV4-014 | « Acheter un château sans être millionnaires : tout ce qu'on aurait aimé savoir avant de se lancer » | 12/07/2026 | 49:58 |

- **Intervenants** : Jérémy Nabais, Martin Menez, Cédric O'Neill (Bricks).
- **Chaîne** : ÇA FAIT UN BAIL ! Podcast immobilier (Audiomeans) et chaîne YouTube de Jérémy Nabais.
- **URL** : flux https://feeds.audiomeans.fr/feed/730cd14a-b0d7-4a5c-82da-3f8eaf41cebb.xml ; vidéo https://www.youtube.com/watch?v=Uvjj7GlRjws
- **Niveau d'accès** : DESCRIPTION/CHAPITRES LUS (notes du flux RSS officiel, chapitres YouTube de #128). Le #140 n'a pas de description (« Pas de description, c'est LE podcast à ne pas manquer »).

### Analyse

**Chronologie reconstituée** (sources : descriptions datées et registres) :
- septembre 2023 : compromis signé, « la banque a validé le projet ». Les associés ouvrent le capital à « un petit groupe de personnes qui ont moyen d'apporter sur le projet (financement, expertise, marketing) », via un questionnaire en ligne ;
- 16/10/2023 : immatriculation de SARTHE SOCIETY ;
- 09/11/2023 : immatriculation de la SCI ;
- début décembre 2023 : épisode d'appel aux micro-investisseurs (#140). Le financement participatif démarre le vendredi 08/12/2023 ;
- 13/03/2024 : publication de l'augmentation de capital au BODACC ;
- 31/03/2024 : retour d'expérience avec le fondateur de Bricks sur « levée de fonds, financement participatif, contrat obligataire » ;
- 2024 : journal de chantier en épisodes. Recrutement d'un gérant de château en CDI ou en alternance. Tournage de « 66 minutes » (M6). Recherche d'un « business model 10x » ;
- 12/07/2026 : bilan à 2 ans. Chantier piloté avec un architecte des Monuments historiques, un maître d'œuvre et une décoratrice, piloté à distance, avec dépassements de budget et retards. Le couple d'associés cible désormais aussi « manoirs, fermes, hôtels, campings, Airbnb atypiques ».

**Méthode de recherche de biens** (#128) : « 29 ans qu'on en rêve, 2 ans qu'on cherche ». Sources citées :
- les **ventes du Domaine de l'État** (encheres-domaine.gouv.fr) ;
- l'**Observatoire du patrimoine religieux** (patrimoine religieux à vendre) ;
- l'agence spécialisée Patrice Besse.

Hospitality Insiders mentionne 18 sites visités.

**Modèle de financement.** Mêmes faits que F01. Le corpus ajoute la **séquence** : les investisseurs en capital ont été choisis avant l'acte, puis le public a été mobilisé par le média (épisode, visite audio, Instagram).

**Difficultés** : retrait bancaire, dépassements de budget et retards de chantier (bilan 2026), gestion à distance.

**Chiffres** : aucun chiffre nouveau dans les descriptions.

**Limites** :
- descriptions auto-promotionnelles ;
- le #140 et le retour d'expérience « sans banque » ne sont pas accessibles en texte ;
- les durées YouTube et audio diffèrent (montages différents).

**Application au projet.**
1. **Chercher hors des annonces classiques** : ventes de l'État, patrimoine religieux désacralisé, agences de niche.
2. **Annoncer publiquement le projet avant l'achat** pour pré-qualifier des investisseurs : questionnaire, cercle restreint, puis grand public.
3. **Documenter le projet** (épisodes « Château Story », documentaire) pour transformer les coûts de chantier en audience. L'audience sert ensuite les ventes (séminaires) et les levées suivantes.

### Passages importants (chapitres YouTube de #128, origine auteur non confirmée)

- 7:36 — Les recherches : https://www.youtube.com/watch?v=Uvjj7GlRjws&t=456s
- 8:45 — Les annonces : https://www.youtube.com/watch?v=Uvjj7GlRjws&t=525s
- 10:48 — Les critères : https://www.youtube.com/watch?v=Uvjj7GlRjws&t=648s
- 16:05 — Le Logis de Fontenay : https://www.youtube.com/watch?v=Uvjj7GlRjws&t=965s
- 19:43 — Faire rentrer les gens au capital : https://www.youtube.com/watch?v=Uvjj7GlRjws&t=1183s
- 21:15 — Le financement : https://www.youtube.com/watch?v=Uvjj7GlRjws&t=1275s
- 22:47 — La structuration : https://www.youtube.com/watch?v=Uvjj7GlRjws&t=1367s

**Note : 85/100.** Accès limité aux descriptions, mais séquence de montage très instructive.

---

## F03 — Richissime #120 « Ils achètent un château sans les banques - avec Jérémy Nabais »

### Identification

- **Réf.** : AV4-015.
- **Intervenants** : Jérémy Nabais ; hôte Delphine Pinon.
- **Chaîne** : Richissime (Audiomeans, YouTube HCdRHfdLR-0).
- **Date** : 30/04/2024.
- **Durée** : 1:55:18 (audio), 1:53:03 (YouTube).
- **URL** : https://www.youtube.com/watch?v=HCdRHfdLR-0 (flux https://feeds.audiomeans.fr/feed/236c1d74-6d8a-46a2-97a2-55e410e45277.xml).
- **Niveau d'accès** : DESCRIPTION/CHAPITRES LUS. Le chapitrage est rédigé par l'hôte et identique sur YouTube.

### Analyse

**Résumé.** Entretien long tenu six mois après l'achat. Il annonce « TOUS les chiffres du projet et financement » et « comment ils ont réussi à le financer sans crédit ». C'est la version la plus détaillée disponible, mais seulement en audio et en vidéo.

**Infos entrepreneuriales** : « unfair advantage » de Nabais (son média), rôle de son associé Martin Menez, cofondateur de Bevouac.

**Financement** : voir F01. **Correction importante** : « sans crédit » est inexact, puisque 690 k€ ont été levés en **obligations** à 7 %.

**Chiffres** : aucun dans la description.

**Limites** : chiffres annoncés mais inaccessibles en texte. Écoute à prévoir si un outil de transcription est autorisé un jour.

**Application** : entretien prioritaire à écouter par un humain, au chapitre 49:23.

### Passages importants (chapitrage de l'hôte)

- 10:12 — Son unfair advantage : https://www.youtube.com/watch?v=HCdRHfdLR-0&t=612s
- 23:22 — Son projet d'achat de château : https://www.youtube.com/watch?v=HCdRHfdLR-0&t=1402s
- 49:23 — Comment acheter un château sans banque ? : https://www.youtube.com/watch?v=HCdRHfdLR-0&t=2963s
- 1:27:59 — Soutien mutuel dans le projet difficile : https://www.youtube.com/watch?v=HCdRHfdLR-0&t=5279s

**Note : 80/100.**

---

## F04 — Hospitality Insiders, épisode 183 « Acheter un château avec ses auditeurs - Jérémy Nabais »

### Identification

- **Réf.** : AV4-016.
- **Intervenants** : Jérémy Nabais ; hôte Maxime Blot (Meilleur Ouvrier de France).
- **Chaîne** : Hospitality Insiders (Audiomeans, YouTube bDwhOJH9eWU).
- **Date** : 04/06/2026.
- **Durée** : 1:03:20 (audio), 1:04:22 (YouTube).
- **URL** : https://hospitalityinsiders.net/acheter-chateau-auditeurs-jeremy-nabais/
- **Niveau d'accès** : DESCRIPTION/CHAPITRES LUS (article résumé publié par l'hôte, chapitres YouTube). Bonus derrière formulaire e-mail : non consulté.

### Analyse

**Faits nouveaux par rapport à F01.**
- Projet **budgété à 2 M€**.
- **Club deal de 33 investisseurs pour 550 000 €**.
- La banque se rétracte **trois semaines** avant la signature.
- **2 048 prêteurs, 690 000 € en trois jours** sur Bricks.
- Château du XIVe siècle sur un éperon rocheux de 12 ha, 53 couchages.
- **Bénévolat** : des centaines de bénévoles recrutés via le compte Instagram « Château Story » (40 000 abonnés) peignent ou défrichent en échange du gîte, du couvert et de masterclasses immobilières.
- **Équipe minimale** : un seul salarié à temps plein, prestataires pour le ménage et la restauration.
- Outils de gestion de projet (Asana, Notion) pour environ 5 000 tâches.
- Modèle « maison de famille » privatisée, inspiré du livre *Unreasonable Hospitality* (Will Guidara).

**Statuts** :
- 33 investisseurs et 550 k€ : RECOUPÉ avec La Martingale et le BODACC ;
- 2 048 prêteurs : DÉCLARATIF ;
- 40 000 abonnés : DÉCLARATIF.

**Limites et risques juridiques à signaler.**
- Le **bénévolat au profit d'une société commerciale** peut être requalifié en travail dissimulé en droit français. Il exige aussi une couverture d'assurance des bénévoles. Le point n'est pas abordé dans le résumé : c'est une analyse d'AV4, à valider par un juriste.

**Application au projet.**
- L'audience sert aussi à **réduire le coût des travaux** (chantiers participatifs), à condition de les encadrer juridiquement (association de sauvegarde, chantiers de bénévoles agréés).
- Une équipe salariée minimale suffit au démarrage.

### Passages importants (chapitres YouTube)

- 2:00 — La genèse du projet et la rencontre des associés : https://www.youtube.com/watch?v=bDwhOJH9eWU&t=120s
- 12:00 — Le passage de l'immobilier à l'hospitalité : https://www.youtube.com/watch?v=bDwhOJH9eWU&t=720s
- 20:00 — Une ingénierie financière hybride et innovante : https://www.youtube.com/watch?v=bDwhOJH9eWU&t=1200s
- 26:00 — Opérations, rénovation communautaire et outils « geeks » : https://www.youtube.com/watch?v=bDwhOJH9eWU&t=1560s
- 35:00 — Vision future et l'importance du contenu : https://www.youtube.com/watch?v=bDwhOJH9eWU&t=2100s

**Note : 85/100.**

---

## F05 — Documentaire « On a 2 ans pour sauver ce château »

### Identification

- **Réf.** : AV4-006.
- **Intervenants** : Jérémy Nabais, Martin Menez ; réalisation Augustin Chenard.
- **Chaîne** : Jérémy Nabais (YouTube).
- **Date** : 06/10/2026 (flux RSS officiel).
- **Durée** : 1:03:08.
- **URL** : https://www.youtube.com/watch?v=rYmSCZXDXRQ
- **Niveau d'accès** : DESCRIPTION/CHAPITRES LUS (description complète via le flux RSS de la chaîne). Aucun chapitre.

### Analyse

- Trois ans de tournage : achat, travaux, « premières galères », financement, ouverture au public.
- Projeté au Grand Rex le 01/10/2026 devant 1 500 personnes (soirée payante, voir la vidéo « Comment NE PAS rentabiliser un Grand Rex »).
- Plus de 2 000 personnes ont participé au financement sur Bricks.
- 75 000 vues en 8 jours (compteur YouTube relevé le 14/10/2026).

**Limites** : contenu non vu. Le titre suggère une échéance à deux ans, peut-être liée au remboursement obligataire prévu au 31/01/2029 (hypothèse AV4, non confirmée).

**Application** : le documentaire est un **actif marketing** qui finance la notoriété du lieu et prépare les prochaines levées. Le projet du client pourrait le reproduire dès la recherche du domaine.

**Note : 80/100** (potentiel élevé, accès faible).

---

## F06 — Sans Pression Podcast : « Comment transformer un domaine en lieu de mariage rentable ? (avec Nicolas Tommasini) »

### Identification

- **Réf.** : AV4-023.
- **Intervenant** : Nicolas Tommasini (fondateur de « Domaines & Événements »).
- **Chaîne** : Sans Pression Podcast.
- **Date** : 20/03/2026 (flux RSS).
- **Durée** : 1:39:43.
- **URL** : https://www.youtube.com/watch?v=JVF3DbmEizg
- **Niveau d'accès** : chapitres YouTube (origine non confirmée). La description du flux RSS est vide.

### Analyse

**Résumé selon les chapitres.**
- Parcours dans l'immobilier « à grande échelle », puis une crise.
- « Déclic : les lieux de mariage ».
- Création de Domaines & Événements.
- Chapitre « Comment repérer et financer un bon domaine ».
- Mariages contre séminaires.

**Limites** : aucun chiffre accessible. Société non vérifiée.

**Application** : témoignage probablement très proche du projet (domaines événementiels). **À écouter en priorité** (chapitre 45:59) si un humain dispose d'une heure.

### Passages importants

- 29:34 — Déclic : les lieux de mariage : https://www.youtube.com/watch?v=JVF3DbmEizg&t=1774s
- 42:13 — Création de Domaines & Événements : https://www.youtube.com/watch?v=JVF3DbmEizg&t=2533s
- 45:59 — Comment repérer et financer un bon domaine : https://www.youtube.com/watch?v=JVF3DbmEizg&t=2759s
- 56:38 — Mariages vs séminaires : https://www.youtube.com/watch?v=JVF3DbmEizg&t=3398s
- 1:03:30 — Construire un business rentable et une vision long terme : https://www.youtube.com/watch?v=JVF3DbmEizg&t=3810s

**Note : 65/100.**

---

## F07 — La Martingale #95 « S'offrir un château pour toucher le gros lot ? » (monuments historiques)

### Identification

- **Réf.** : AV4-022.
- **Intervenants** : Mathieu Mars (conseiller en gestion de patrimoine, Institut du Patrimoine) ; hôte Matthieu Stefani.
- **Date** : 13/01/2022.
- **Durée** : 1:08:45.
- **URL** : https://lamartingale.io/tous/soffrir-un-chateau-pour-toucher-le-gros-lot/
- **Niveau d'accès** : DESCRIPTION/CHAPITRES LUS (notes détaillées du site).

### Analyse

**Points clés** (selon l'invité, qui vend ce type de produit) :
- deux voies : rénover seul avec subventions, ou **acheter une partie rénovée par un promoteur** que l'on rembourse ;
- travaux étalés sur environ 4 exercices ;
- location nue d'au moins 3 ans pour l'avantage fiscal ;
- conservation 15 ans ;
- classement en 3 à 5 ans ;
- avantage sans plafond, cumulable avec Pinel et Malraux.

**Limites** : discours commercial de 2022. La mission 1 a déjà détaillé et vérifié le régime MH (Montages_financiers.md §1.5) : détention directe ou SCI familiale non soumise à l'IS, et incompatibilité avec des investisseurs tiers à l'IS.

**Application** : le **montage « promoteur MH + copropriété d'investisseurs »** est une voie pour financer la restauration de **dépendances** par des contribuables fortement imposés, tout en gardant le corps principal. Il suppose un agrément pour les copropriétés et entre en conflit avec l'exploitation commerciale (voir mission 1).

**Note : 55/100.**

---

## F08 — GDIY #525 « Joseph Lasserre - Groupe Doumer - Racheter des entreprises dont personne ne veut »

### Identification

- **Réf.** : AV4-026.
- **Intervenants** : Joseph Lasserre (Groupe Doumer) ; hôte Matthieu Stefani.
- **Chaîne** : Génération Do It Yourself (GDIY).
- **Date** : 25/02/2026.
- **Durée** : 2:40:52 (audio), 2:42:30 (YouTube, « Les "BORING BUSINESSES" qui rapportent des MILLIONS », 209 000 vues).
- **URL** : https://www.gdiy.fr/podcast/joseph-lasserre/ et https://www.youtube.com/watch?v=ncsFmxXWiRs
- **Niveau d'accès** : DESCRIPTION/CHAPITRES LUS. Notes du site et du flux RSS, timeline de l'auteur, chapitres YouTube aux mêmes intitulés (origine auteur confirmée).

### Analyse

**Résumé.**
- 2009 : licencié d'un cabinet de conseil.
- Se lance dans le photovoltaïque avec deux associés, embauche des couvreurs et découvre les métiers du bâtiment.
- 2014 : rachète une première PME de plomberie.
- Aujourd'hui, selon l'épisode : Groupe Doumer, 7 entreprises du bâtiment (de la couverture à la métallerie), 150 salariés, 25 M€ de chiffre d'affaires.

**Infos entrepreneuriales** (sommaire de l'auteur) :
- valoriser et financer le rachat d'une PME du bâtiment ;
- trois critères d'une bonne acquisition ;
- mesurer et réduire les risques ;
- ce qu'on change et ce qu'on garde le premier jour ;
- danger d'une croissance trop rapide ;
- vérifier la valeur d'une entreprise sur le terrain.

Sujets cités : la « clause d'earn-out dans la transmission d'entreprise », le besoin en fonds de roulement, l'« opportunité de la décennie : les Boomer Boring Business ».

**Vérification au registre** (API annuaire des entreprises) :
- DOUMER HOLDING : SAS créée le 28/07/2014, Paris 16e, présidée par Joseph Lasserre.
- Elle préside des sociétés anciennes :
  - DOUMER SOLS, créée en 1966 ;
  - RIALLAND, créée en 1991, CA 2023 de 3,87 M€ pour un résultat net de 472 k€ ;
  - DOUMER ELECTRICITE / PERELEC, créée en 1998 ;
  - GECAPE, créée en 1976.
- Une SCI GROUPE DOUMER (2022) est gérée par Lasserre.

**La structure « holding de reprise qui rachète des PME anciennes » est VÉRIFIÉE.** Les chiffres consolidés (7 sociétés, 150 salariés, 25 M€) sont DÉCLARATIFS : les comptes ne sont pas tous publics et ceux du groupe n'ont pas été consultés.

**Modèle économique.** Racheter des PME artisanales rentables sans successeur, dans des secteurs jugés « peu attractifs » et donc moins chers. Créer de la valeur par la gestion, la mutualisation et la transformation des concurrents en partenaires.

**Financement.** Le détail n'est pas accessible en texte. Le chapitre « Combien ça coûte une entreprise de BTP ? » et la mention de l'earn-out indiquent un montage classique : holding, dette d'acquisition, complément de prix. Repère de place : les critères bancaires CRA (dette au plus égale à 70 % du prix, sur 7 ans) sont détaillés par la mission 1.

**Difficultés** : croissance trop rapide, direction d'équipes de métiers manuels « sans savoir faire ».

**Limites.** Récit de réussite, sans les échecs éventuels. Il a fallu 12 ans pour constituer le groupe.

**Application au projet.**
1. **Reprendre une PME de la filière patrimoine ou équestre** pour bâtir revenus, compétences et réseau avant l'achat du château. Exemples : couverture, charpente, menuiserie de restauration, sellerie, transport de chevaux.
2. Une entreprise de couverture ou de charpente donne un **accès privilégié aux artisans du bâti ancien**. Elle doit facturer le château **au prix de marché**, sinon il y a risque d'abus de biens sociaux. Point d'analyse AV4, non évoqué par l'invité.
3. **Rythme réaliste** : 1 PME en 2014, 7 en 2026. La mission 1 a montré qu'une seule reprise en LBO libère peu de cash avant 2031.

### Passages importants

Chapitres YouTube (minutage de la vidéo) :
- 17:59 — Combien ça coûte une entreprise de BTP ? : https://www.youtube.com/watch?v=ncsFmxXWiRs&t=1079s
- 33:51 — Le premier levier de la rentabilité pour les petites entreprises : https://www.youtube.com/watch?v=ncsFmxXWiRs&t=2031s
- 53:35 — Les 3 seuls critères qui comptent pour diriger une entreprise : https://www.youtube.com/watch?v=ncsFmxXWiRs&t=3215s
- 1:01:47 — Sa meilleure stratégie pour reprendre une entreprise : https://www.youtube.com/watch?v=ncsFmxXWiRs&t=3707s
- 1:13:04 — Transformer ses concurrents en partenaires long terme : https://www.youtube.com/watch?v=ncsFmxXWiRs&t=4384s
- 1:46:10 — Le danger d'une croissance trop rapide : https://www.youtube.com/watch?v=ncsFmxXWiRs&t=6370s
- 1:52:35 — Comment vérifier la valeur d'une boîte sur le terrain : https://www.youtube.com/watch?v=ncsFmxXWiRs&t=6755s
- 2:18:29 — Le conseil de Joseph pour les repreneurs d'entreprise : https://www.youtube.com/watch?v=ncsFmxXWiRs&t=8309s

Équivalences sur la version audio (timeline de l'auteur) : 00:19:02, 00:34:54, 01:02:50, 01:53:01, 02:18:55.

**Note : 85/100.**

---

## F09 — Bpifrance : financer une reprise (webinaire « Comment financer un projet de reprise d'entreprise ? » et Big 2026 « Reprendre une entreprise, l'autre voie pour entreprendre »)

### Identification

- **Réf.** : AV4-027 et AV4-030 (AV4-028, Big 2025 avec Pascal Legros, seulement repéré).
- **Intervenants** : intervenants Bpifrance et Réseau Entreprendre (AV4-027, noms non lus) ; Gabriel Strauss (entrepreneur et conseiller) et Fabrice Lundy (AV4-030).
- **Chaîne** : Bpifrance (YouTube).
- **Date** : AV4-027 inconnue (YouTube : « il y a 4 ans ») ; AV4-030 : environ le 08/10/2026 (« il y a 6 jours »).
- **Durée** : 1:15:55 et 31:11.
- **URL** : https://www.youtube.com/watch?v=g0soqDEdWRw et https://www.youtube.com/watch?v=NHqYBl21GJw
- **Niveau d'accès** : chapitres. Pour g0soqDEdWRw, le « Sommaire » horodaté figure dans la description, l'origine auteur est donc confirmée. AV4-027 compte 165 000 vues.

### Analyse

**Contenu.**
- AV4-027 suit le parcours de financement : business plan, renforcement de l'apport personnel (prêts d'honneur, Réseau Entreprendre), choix des prêteurs, financements et garanties Bpifrance.
- AV4-030 couvre les profils de repreneurs (cadres, jeunes, femmes), le « marché caché », la façon de convaincre le banquier et de préparer son apport, la « séduction du cédant » et la négociation du prix.

**Faits vérifiés sur les garanties** (Bpifrance Création, page lue, S-AV4-35) :
- garantie de Bpifrance sur les reprises **jusqu'à 70 % en cas d'intervention conjointe de la Région** ;
- opérations éligibles : **achat de titres de sociétés, achat de fonds de commerce, caution bancaire d'un crédit-vendeur** ;
- autres garants : SIAGI, SOCAMA, fonds de France Active (garantie Égalité femmes à 80 %) ;
- **avertissement de Bpifrance** : la garantie « ne réduit pas votre propre risque ». Elle couvre la banque, qui se tourne d'abord vers la caution personnelle de l'emprunteur.

Signal à suivre : la fiche « Garantie transmission » du catalogue bpifrance.fr affiche « Désolé, cette offre n'est plus disponible » au 14/10/2026 (S-AV4-36). Le produit est à reconfirmer auprès d'un chargé d'affaires.

**Limites.**
- Webinaire ancien pour AV4-027 (barèmes de 2022 environ).
- Aucun texte des interventions.
- Prêts d'honneur, quotités et critères bancaires (dette au plus égale à 70 % du prix sur 7 ans) déjà vérifiés par la mission 1 : ne pas dupliquer.

**Application au projet.**
- Si le château est acheté **via une société d'exploitation existante** (rachat des titres d'une SAS propriétaire-exploitante d'un domaine événementiel ou équestre), les outils de la **reprise d'entreprise** s'appliquent : garantie Bpifrance, prêts d'honneur, crédit-vendeur garanti.
- Un **pur achat immobilier** (SCI) n'y donne en principe pas accès. Point non tranché par la mission 1 (« INCONNU »).
- Le montage « reprise de titres d'un exploitant » est donc à privilégier (idée I4).

### Passages importants

Sommaire de l'auteur (AV4-027) :
- 6:23 — Le business plan de reprise : https://www.youtube.com/watch?v=g0soqDEdWRw&t=383s
- 11:14 — Comment renforcer son apport personnel ? : https://www.youtube.com/watch?v=g0soqDEdWRw&t=674s
- 26:09 — L'offre d'accompagnement de Réseau Entreprendre : https://www.youtube.com/watch?v=g0soqDEdWRw&t=1569s
- 43:10 — Vers qui vous tourner pour emprunter de l'argent ? : https://www.youtube.com/watch?v=g0soqDEdWRw&t=2590s
- 53:40 — Les solutions de financement et de garantie de Bpifrance : https://www.youtube.com/watch?v=g0soqDEdWRw&t=3220s

Chapitres YouTube (AV4-030) :
- 10:22 — Où trouver les entreprises ? Le marché caché : https://www.youtube.com/watch?v=NHqYBl21GJw&t=622s
- 11:55 — Convaincre le banquier et préparer son apport : https://www.youtube.com/watch?v=NHqYBl21GJw&t=715s
- 13:00 — La séduction du cédant : https://www.youtube.com/watch?v=NHqYBl21GJw&t=780s
- 29:48 — Négocier le prix : https://www.youtube.com/watch?v=NHqYBl21GJw&t=1788s

**Note : 75/100.**

---

## F10 — Search funds : corpus FR et EN, et chiffres de l'étude Stanford

### Identification

- **Réf.** : AV4-029, 032, 033, 034, 035, 118, 132, 133, 134.

| Réf. | Contenu | Date | Durée | Accès |
|---|---|---|---|---|
| AV4-029 | Bpifrance Big 2025, « Search fund : premier bilan… » (Ariane Olive, Spark Avocats) | inconnue (« il y a 1 an ») | 46:10 | REPÉRÉ |
| AV4-032 | Investisseurs 4.0 #207 (Ariane Olive) | inconnue | 1:19:28 | REPÉRÉ |
| AV4-033 | Pierre-Emmanuel Drochon | inconnue | 50:19 | chapitres |
| AV4-034 | Trophée CRA 2024, David Lescure | inconnue | 5:07 | REPÉRÉ |
| AV4-035 | Newfund, fonds minoritaire (Marjolaine Catil) | inconnue | 1:27:55 | chapitres |
| AV4-132 | Think Like an Owner EP.232 (Sara Heston, étude Stanford 2024) | 16/07/2024 | 38:33 | notes et topics horodatés |
| AV4-133 | EP.231 (Ruback et Yudkoff, Harvard) | 09/07/2024 | 49:55 | notes et topics horodatés |
| AV4-134 | Stanford GSB, panel « Search Funds » | inconnue (« il y a 17 ans ») | 1:14:17 | chapitres |
| AV4-118 | Acquiring Minds, Jenna Whigham | inconnue | 1:22:14 | chapitres |

- **URL** : voir le catalogue.
- **Niveau d'accès** : mixte (tableau ci-dessus).

### Analyse

**Définition** (Stanford GSB, page lue). Un search fund est un véhicule d'investissement, conçu en 1984. Des investisseurs y financent la recherche, puis le rachat et le développement d'une entreprise non cotée par un entrepreneur. Le modèle offre à des entrepreneurs « relativement inexpérimentés » et « aux ressources limitées » un accès rapide à la direction d'une entreprise dont ils détiennent une part significative.

**Chiffres VÉRIFIÉS** (étude Stanford 2026, page Insights lue, S-AV4-33). Périmètre : États-Unis et Canada, données au 31/12/2025.

| Indicateur | Valeur |
|---|---|
| Taux d'acquisition agrégé depuis 1996 | **58 %** |
| Fonds lancés en 2021-2024 ayant acquis | environ la moitié |
| Délai d'acquisition | environ **20 mois** |
| Prix médian d'acquisition (2024-25) | **16 M$** |
| TRI agrégé | **33,9 %** |
| Multiple | **4,75x** |
| PME (comparaison au marché coté) | 2,88 |

Il s'agit de rendements **agrégés pour les investisseurs**, tirés par les meilleurs cas. 42 % des searchers n'acquièrent rien.

**Adaptation française.**
- Le Big 2025 fait un « premier bilan d'un modèle en développement » ; l'extrait évoque un futur « France Search Fund » pour structurer les investisseurs.
- Newfund titre un chapitre « Pourquoi le Search Fund ne colle pas au système français ». Sa thèse alternative : un **fonds minoritaire** aux côtés d'un repreneur majoritaire, sur des « belles endormies », avec roll-up.

**Limites.**
- Aucun texte des interventions françaises.
- Les chiffres Stanford concernent des PME de services et de logiciels à environ 16 M$, très loin d'un château.

**Application au projet.**
- Le search fund classique ne finance **pas un château**, faute d'EBITDA stable et de taille suffisante.
- La logique est transposable sous deux formes :
  - **(a)** une « recherche financée » par quelques family offices pour trouver puis racheter un **domaine équestre ou événementiel déjà rentable**. Le porteur reçoit une part de capital liée à la réussite ;
  - **(b)** le modèle « fonds minoritaire et repreneur majoritaire » (Newfund), qui protège le contrôle du fondateur.
- Pour un jeune de 26 ans, le passage par un search fund d'une **PME classique** reste la voie la plus documentée pour devenir dirigeant-actionnaire vite. Le château vient après (idée I11).

### Passages importants

- Drochon, 13:29 — Sourcing, due diligence, stratégie terrain : https://www.youtube.com/watch?v=nVtY98zPGfg&t=809s
- Drochon, 27:55 — Montage Search Fund : https://www.youtube.com/watch?v=nVtY98zPGfg&t=1675s
- Newfund, 8:00 — Panorama des structures de financement en equity : https://www.youtube.com/watch?v=g19tFXfNpWc&t=480s
- Newfund, 18:00 — Pourquoi le Search Fund ne colle pas au système français : https://www.youtube.com/watch?v=g19tFXfNpWc&t=1080s
- Newfund, 1:12:00 — Roll-up assisté par un fonds minoritaire : https://www.youtube.com/watch?v=g19tFXfNpWc&t=4320s
- Stanford, 13:28 — Raising a search fund : https://www.youtube.com/watch?v=35rnr9Qcsxc&t=808s
- Stanford, 53:08 — Watch the seller : https://www.youtube.com/watch?v=35rnr9Qcsxc&t=3188s
- Whigham, 27:26 — Acquisition price & PE-backed structure : https://www.youtube.com/watch?v=MfJ44K8wjEU&t=1646s
- Think Like an Owner EP.232 (audio, topics de l'auteur) :
  - 00:03:13 — principaux enseignements de l'étude ;
  - 00:04:26 — pourquoi le nombre d'investisseurs a baissé ;
  - 00:26:24 — cohorte 2017-2020.

**Note : 65/100.**

---

## F11 — Corpus FR « reprendre sans apport / crédit-vendeur » : ce qui tient et ce qui ne tient pas

### Identification

- **Réf.** : AV4-038 à 049, AV4-052 à 054.
- **Chaînes** : Reprisedentreprise (Pedro Da Fonseca), Reprenariat, Alexandre Barthelemy, David Bonhomme, AH-STRATEGIS, Dougs Compta, Aurélien Schneider, Documentaire Société, Instinct d'entrepreneur, Boring Business.
- **Dates** : relatives (de 2 mois à 6 ans) sauf AV4-048, publié le 14/10/2026.
- **Durées** : de 7:18 à 1:14:26.
- **URL** : voir le catalogue.
- **Niveau d'accès** : chapitres YouTube (8 contenus) ou REPÉRÉ (les autres).

### Analyse

**Ce que promettent les titres** : « sans apport », « sans cash perso », « sans caution », « 0 € d'apport », « 20-30 k€ suffisent ». Plusieurs chaînes vendent des formations ou du coaching (« Mastermind des repreneurs », guide « rachat SANS APPORT », bootcamp).

**Ce qui a été vérifié.**
1. **Ordres de grandeur de place** (CRA, page lue, S-AV4-38) :
   - le crédit-vendeur couvre généralement **30 à 50 % du prix**, sur **1 à 5 ans**, à un taux proche des taux bancaires ;
   - l'acheteur règle souvent **50 à 70 % au closing** ;
   - garanties possibles : caution personnelle ou nantissement des titres ; acte notarié ;
   - exemple du CRA : boulangerie à 200 000 €, 100 000 € comptant et 100 000 € sur 4 ans à 3 %.
2. **Garantie Bpifrance** : elle peut couvrir la caution bancaire d'un crédit-vendeur (F09).
3. **Pérennité des reprises** (INSEE, pages lues) : 70 % à 5 ans pour les entreprises reprises, contre 61 % pour l'ensemble des entreprises classiques (Centre-Val de Loire). L'avantage existe, mais il est **sans commune mesure avec les « 85 % vs 40 % »** du webinaire Boring Business.
4. **Témoignages « sans apport »** : sociétés non nommées, donc non vérifiables (voir le tableau de vérification en tête de fichier).

**Ce qui est utile** :
- **AH-STRATEGIS** démonte la « technique internet » du « full crédit-vendeur » en trois problèmes (chapitres). C'est le seul contenu du corpus qui prend le contre-pied du marketing.
- **Dougs** (chapitres) : achat de titres ou de fonds, passif hérité en cas de rachat de titres, fiscalité du vendeur (art. 238 quindecies, « levier caché de la négo »), EBE retraité multiplié par un coefficient, capacité de la cible à rembourser la banque. Exemple : « 1,5 M€ de machines mais 870 k€ finançables ».
- **Boring Business** : les chapitres listent les aides (Bpifrance, prêts d'honneur, garanties). Les chiffres d'accroche restent à vérifier un par un.

**Limites** : aucun montage chiffré vérifiable dans ce corpus.

**Application au projet.**
1. **Ne pas croire au rachat 100 % vendeur** : un cédant prudent exige un acompte et des garanties.
2. La négociation fiscale avec le vendeur est un vrai levier : **abattements et exonérations du cédant** (par exemple le 238 quindecies cité par Dougs pour les entreprises). Pour un château détenu en direct, la fiscalité des plus-values immobilières est différente, à étudier avec un notaire.
3. Pour le client, le crédit-vendeur n'a de sens qu'adossé à un **apport réel**, à une **dette senior** et à des **quasi-fonds propres** (prêts d'honneur), selon les proportions du CRA.

### Passages importants

- AH-STRATEGIS, 4:06 — Le full crédit-vendeur : la technique internet : https://www.youtube.com/watch?v=X5MyvdIAUzY&t=246s
- AH-STRATEGIS, 10:46 — Le deuxième problème avec le « full crédit-vendeur » : https://www.youtube.com/watch?v=X5MyvdIAUzY&t=646s
- AH-STRATEGIS, 13:59 — Le troisième problème : https://www.youtube.com/watch?v=X5MyvdIAUzY&t=839s
- AH-STRATEGIS, 3:31, 8:59, 12:06 — Leviers financier, juridique et fiscal du LBO : https://www.youtube.com/watch?v=42TEFrVIIfM&t=211s
- Dougs, 3:50 — Fonds de commerce ou titres : https://www.youtube.com/watch?v=yfCYq2uuM2A&t=230s
- Dougs, 5:59 — Fiscalité du vendeur (238 quindecies) : https://www.youtube.com/watch?v=yfCYq2uuM2A&t=359s
- Dougs, 9:14 — EBE retraité et multiple : https://www.youtube.com/watch?v=yfCYq2uuM2A&t=554s
- Dougs, 11:10 — Ta future boîte pourra-t-elle vraiment rembourser la banque ? : https://www.youtube.com/watch?v=yfCYq2uuM2A&t=670s
- Dougs, 12:25 — 1,5 M€ de machines mais 870 k€ finançables : https://www.youtube.com/watch?v=yfCYq2uuM2A&t=745s
- Da Fonseca, 5:05 — Prix et financement (témoignage de Martin) : https://www.youtube.com/watch?v=BJ7fzqV3EpQ&t=305s
- Boring Business, 8:18 — « Cas réel : racheter une boîte avec 0 € d'apport » (affirmation à vérifier) : https://www.youtube.com/watch?v=gkiorJ_hWi4&t=498s
- Boring Business, 1:02:16 — Aides disponibles : BPI, prêts d'honneur, garanties : https://www.youtube.com/watch?v=gkiorJ_hWi4&t=3736s
- Boring Business, 1:04:19 — « 85 % de survie en reprise vs 40 % en création » (contredit par l'INSEE) : https://www.youtube.com/watch?v=gkiorJ_hWi4&t=3859s

**Note : 60/100** (pour le corpus : utile surtout par la vérification négative).

---

## F12 — Racheter des entreprises en difficulté : GDIY #554 (Patrick Sayer), GDIY #296 (Marion Carrette), Trophée CRA SN Alugo

### Identification

| Réf. | Contenu | Date | Durée | Accès |
|---|---|---|---|---|
| AV4-068 | GDIY #554, « Patrick Sayer - Président du Tribunal de Commerce de Paris - Comprendre les 70 000 faillites qui tuent la France » | 12/07/2026 | 2:21:38 | timeline de l'auteur (flux RSS) |
| AV4-057 | GDIY #296, « Marion Carrette - OuiCar & Anny Blatt » | 18/12/2022 | 2:29:54 | timeline de l'auteur (flux RSS) |
| AV4-036 | Trophée CRA, SN Alugo (YouTube dxU0jl7kiSw) | relative (« il y a 7 ans ») | 4:20 | REPÉRÉ |

### Analyse

**Patrick Sayer** : ancien banquier de Lazard, président du directoire d'Eurazeo pendant 16 ans, puis président du tribunal de commerce de Paris depuis 2023. Selon la description :
- environ **70 000 procédures collectives par an**, en hausse en 2026 (DÉCLARATIF) ;
- l'« arsenal juridique » français (sauvegarde accélérée, cessation des paiements et délai de 45 jours) est mal utilisé ;
- deux chapitres clés : « Les techniques pour (bien) racheter une entreprise en difficulté » et « L'importance de savoir déposer le bilan à temps » ;
- l'ouverture « On a inventé l'outil qui a permis à B. Arnault de prendre le contrôle de LVMH » renvoie au rôle de Lazard (voir F13).

**Marion Carrette** : reprise de la marque de tricot historique **Anny Blatt en liquidation judiciaire**, « avant que cette marque historique ne disparaisse ». L'épisode traite des erreurs à ne pas commettre en reprise et du décalage entre le web et un produit historique.

**SN Alugo** : société reprise « à la barre du tribunal », dont le repreneur a été primé par le CRA en 2019, cinq ans après la reprise selon l'extrait.

**Limites** : aucun prix ni montage chiffré accessible.

**Application au projet.** Les **procédures collectives** sont une source d'actifs décotés : châteaux-hôtels, domaines événementiels, centres équestres ou haras en redressement ou en liquidation. Trois voies :
- l'offre de reprise dans un plan de cession ;
- l'adjudication des immeubles en liquidation ;
- les ventes de l'État (déjà citées par Nabais).

Le revers : délais très courts, actifs dégradés, absence de garantie de passif, conditions sociales imposées.

Il faut se faire connaître des **administrateurs et mandataires judiciaires** et des chambres des commissaires de justice de la région cible. Les règles précises (articles du Code de commerce, conditions de l'offre) **n'ont pas été vérifiées** par AV4 et sont à faire valider par un avocat en procédures collectives.

### Passages importants (timelines audio des auteurs)

- #554, 00:00:00 — « On a inventé l'outil qui a permis à B. Arnault de prendre le contrôle de LVMH »
- #554, 00:47:53 — Pourquoi les entreprises font faillite
- #554, 01:56:04 — Les techniques pour (bien) racheter une entreprise en difficulté
- #554, 02:06:44 — L'importance de savoir déposer le bilan à temps
- #296, 00:17:32 — Rachat d'Anny Blatt
- #296, 00:59:25 — Lancer en plein confinement

**Note : 65/100.**
