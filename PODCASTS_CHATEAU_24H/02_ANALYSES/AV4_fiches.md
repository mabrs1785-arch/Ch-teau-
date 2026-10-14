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

