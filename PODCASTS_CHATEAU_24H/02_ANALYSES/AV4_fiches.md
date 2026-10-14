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

### Passages importants (chapitres YouTube de la vidéo intégrale ; minutage identique à la timeline audio publiée par l'auteur dans le flux RSS, donc origine auteur confirmée)

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

---

## F13 — Acquired « LVMH » : Bernard Arnault et la reprise de Boussac (1984)

### Identification

- **Réf.** : AV4-115.
- **Intervenants** : Ben Gilbert et David Rosenthal (hôtes).
- **Chaîne** : Acquired.
- **Date** : 21/02/2023 (flux RSS).
- **Durée** : 3:25:04.
- **URL** : https://www.acquired.fm/episodes/lvmh
- **Niveau d'accès** : TRANSCRIPTION TEXTE LUE (partielle). Transcription publiée par l'émission ; passages Boussac, Lazard, structure de holdings et coentreprise Guinness lus après recherche par mots-clés.

### Analyse

**Résumé du passage utile** (paraphrase fidèle).
- L'empire textile Boussac, propriétaire de Christian Dior, fait faillite en 1978, passe aux frères Willot, puis retombe sous administration publique.
- Bernard Arnault, issu d'une entreprise familiale de construction et passé par les États-Unis, monte une offre avec la banque Lazard (Antoine Bernheim).
- Selon Acquired : **offre d'environ 60 M$**, dont **15 M$ apportés par la famille Arnault** et **45 M$ réunis par Lazard** auprès d'investisseurs. Boussac réalisait alors plus d'un milliard de dollars de chiffre d'affaires, mais perdait de l'argent.
- Arnault restructure : environ 9 000 suppressions de postes sur 20 000, selon les hôtes. Le groupe redevient rentable en deux ans.
- Il **revend les actifs non stratégiques** : la division couches Peaudouce pour environ 400 M$, plus de 500 M$ au total. Il ne garde que Dior et Le Bon Marché.
- Il empile une **structure en « poupées russes »** : holding familiale (Groupe Arnault), puis Agache (ancienne holding de Boussac), puis Dior. En cotant des minorités à chaque étage, il lève des capitaux sans perdre le contrôle.
- En 1987-1988, une **coentreprise avec Guinness** (60/40, contrôlée par Arnault) lui sert de levier pour monter au capital de LVMH. Les hôtes résument : « le capital de Guinness n'est plus que du levier pour Arnault ».
- Conclusion des hôtes : le levier « marche quand on a raison ». Mais, ajoute l'un d'eux, la plupart des histoires de levier finissent mal et ne sont jamais racontées.

**Recoupement** (Wikipédia FR, Boussac Saint-Frères, qui cite Libération du 04/11/2010).
- L'État (gouvernement Fabius) apporte **745 MF**.
- Arnault doit réunir **400 MF** qu'il « ne possède pas ». La fortune familiale mobilisable est de **90 MF**.
- Le tour de table d'Antoine Bernheim (Lazard, Banque Worms, Total, Elf Aquitaine) apporte **plus des trois quarts**.
- Il emprunte ensuite **400 MF au Crédit lyonnais** (banque publique) pour racheter discrètement les parts des Willot et devenir majoritaire « au détriment de ses partenaires financiers ».
- Condition de la reprise : conserver l'intégralité du groupe. Il revendra pourtant l'essentiel.

**Statut : RECOUPÉ.** Ordre de grandeur cohérent : environ 20-25 % de fonds propres familiaux, le reste en argent des autres.

**Mécanismes identifiés.**
1. Un **vendeur public aux objectifs non financiers** (emplois, éviter une faillite symbolique) accepte un repreneur en échange d'engagements.
2. **Argent des partenaires** réuni par une banque d'affaires de confiance.
3. **Deuxième étage de levier** (dette) pour racheter les coactionnaires et prendre le contrôle.
4. **Revente d'actifs non stratégiques** pour rembourser.
5. **Cascade de holdings** pour lever des minoritaires sans perdre le contrôle.

**Limites.**
- Récit d'hôtes américains, montants en dollars approximatifs.
- Contexte de 1984 (nationalisations, politique industrielle) non reproductible.
- Engagements envers l'État non tenus, avec un coût de réputation.
- Biais du survivant reconnu par les hôtes eux-mêmes.

**Application au projet** (à petite échelle).
- **(a)** Chercher des **vendeurs à motivation non financière** : commune, État (ventes du Domaine), hôpital, diocèse, famille sans successeur. Négocier sur les **conditions** (cahier des charges, ouverture au public, emplois, entretien) plutôt que sur le seul prix.
- **(b)** **Revendre le non-stratégique** : forêt, terres excédentaires, dépendances, mobilier. Voir l'idée I9.
- **(c)** Garder le **contrôle via la holding** quand on accueille des minoritaires dans la SCI et la société d'exploitation (voir Fontenay, F01).
- **(d)** Ne jamais prendre d'engagements qu'on ne tiendra pas : sur un patrimoine local, la réputation est un actif.

### Passages importants

La transcription publiée n'a pas d'horodatage : aucun minutage n'est cité.

**Note : 85/100.**

---

## F14 — La Martingale × Fundora : LBO, échecs et réussites du private equity (hors-séries #2, #5, #6)

### Identification

| Réf. | Contenu | Date | Durée |
|---|---|---|---|
| AV4-061 | #2 « 55 milliards pour Electronic Arts : anatomie du plus gros LBO de l'histoire » (page : « LBO : comment fonctionne vraiment l'effet de levier en private equity ? ») | 31/08/2026 | 35:40 |
| AV4-062 | #5 « Comment ce deal a failli faire disparaître la Ligue 1 » | 21/09/2026 | 33:18 |
| AV4-063 | #6 « L'opération légendaire qui a sauvé Burger King de la faillite » | 28/09/2026 | 38:11 |

- **Intervenants** : Bradley Lafond (directeur général de Fundora, plateforme d'investissement) ; hôte Matthieu Stefani.
- **URL** : https://lamartingale.io/tous/lbo-comment-fonctionne-vraiment-leffet-de-levier-en-private-equity/ (et pages #5 et #6).
- **Niveau d'accès** : DESCRIPTION/CHAPITRES LUS (notes détaillées pour #2, timelines de l'auteur pour #2, #5 et #6). Série sponsorisée par une plateforme qui vend du non-coté.

### Analyse

**Mécanique LBO** (page #2) :
- **LBO minoritaire** : un fondateur à 100 % d'une société valorisée 10 M€ vend 30 %, encaisse 3 M€ (« cash-out ») et garde 70 %. Le fonds peut aussi injecter de l'argent dans la société (« cash-in »).
- **LBO majoritaire** : le fonds prend le contrôle.
- La dette amplifie les gains et les pertes. Cas **TXU** : environ 45 Md$, dont environ 8 Md$ de fonds propres et 37 Md$ de dette. La chute des prix du gaz l'a mené au Chapter 11.
- Distinction **TRI** (taux de rendement interne annuel) et **multiple** : le temps compte.

**#5** : accord CVC-LFP après Mediapro ; gérer une erreur d'investissement ; risque acceptable.

**#6** : 3G Capital rachète Burger King en 2010. « Investissement multiplié par 28 », selon l'épisode : DÉCLARATIF, non vérifié.

**Limites** : contenu pédagogique et sponsorisé, sans rapport direct avec l'immobilier ou les PME.

**Application au projet.**
- La levée de Fontenay est en fait un **« cash-in minoritaire »** : 22 % cédés aux investisseurs.
- La promesse faite aux investisseurs, « doubler la mise » entre 2030 et 2035 (soit 7 à 12 ans après 2023), équivaut à un **TRI d'environ 6 à 10 % par an** (calcul AV4 : 2^(1/12) − 1 ≈ 5,9 % ; 2^(1/7) − 1 ≈ 10,4 %).
- C'est l'ordre de grandeur à proposer à des investisseurs patrimoniaux, à comparer aux 10 % visés par les club deals hôteliers (F17).
- Le cas TXU rappelle qu'un domaine à revenus saisonniers ne supporte pas une dette calibrée sur un scénario optimiste.

### Passages importants (timelines audio des auteurs)

- #2, 00:05:19 — Comment les grandes entreprises se font racheter
- #2, 00:14:00 — Les avantages et les risques d'un LBO
- #2, 00:25:51 — La liquidité et le rendement du non coté
- #5, 00:05:39 — Comment gérer une erreur d'investissement ?
- #5, 00:13:55 — Private equity : quel est le risque acceptable ?
- #6, 00:04:49 — Rachat par des fonds : l'alignement d'intérêts
- #6, 00:29:50 — L'horizon d'investissement

**Note : 60/100.**

---

## F15 — Family offices (corpus FR) : Stérin (Otium), Benabou, Biousse, Mulliez, Afflelou, Agami, Weil, Herrmann

### Identification

| Réf. | Contenu | Date | Durée | Accès |
|---|---|---|---|---|
| AV4-065 | GDIY #284, Pierre-Édouard Stérin (Otium Capital) | 16/10/2022 | 2:27:56 | notes et timeline (flux RSS GDIY) |
| AV4-066 | GDIY #252, Michaël Benabou (Financière Saint James) | 06/04/2022 | 3:04:28 | notes et timeline |
| AV4-067 | GDIY #249, Frédéric Biousse (Experienced Capital, Domaines de Fontenille) | 20/03/2022 | 2:37:36 | notes et timeline |
| AV4-069 | GDIY #499, Alexandre Mulliez (FC Versailles) | 26/10/2025 | 2:55:19 | notes et timeline |
| AV4-077 | Finscale HS #12, Romain Afflelou (AA&Sons) | 17/12/2022 | 37:00 | notes |
| AV4-078 | Finscale HS #6, Laurent de Swarte (Agami) | 01/01/2022 | 30:10 | notes |
| AV4-075 | LEVERAGE MEDIA, Pierre-Emmanuel Weil | inconnue (« il y a 8 mois ») | 1:10:08 | REPÉRÉ |
| AV4-079 | Jérémy Nabais × Thierry Herrmann (foncière familiale) | 11/10/2026 | 48:49 | description complète et chapitres |
| AV4-064 | La Martingale #269, Eric Tréguier | 12/06/2025 | 1:21:26 | notes |

### Analyse

**Ce que disent les descriptions.**
- **Stérin** : fortune faite avec Smartbox, puis investissement via Otium Capital. Philanthropie : sa fortune est léguée au Fonds du Bien Commun. Chapitres « La vente de Smartbox » et « Otium Capital ».
- **Benabou** : cofondateur de Vente-Privée. Il crée une **holding patrimoniale** (Financière Saint James) pour « revaloriser le potentiel des biens immobiliers ». Business angel.
- **Biousse** : codirige le fonds **Experienced Capital** (marques de consommation) et crée **des hôtels dans des domaines** avec son conjoint Guillaume Foucher. Chapitre « Décomplexer le luxe en hôtellerie ». La Caisse des Dépôts cofinance ces domaines, selon un résultat de recherche (voir F21).
- **Mulliez** (petit-fils de Gérard Mulliez) rachète le FC Versailles, qui perdait 7,5 M€ par saison selon la description. Il **documente tout** (série « Le Club ») : « build in public ».
- **Afflelou** : family office familial. Philosophie, gouvernance, suivi des participations ; « le maître mot, c'est la transmission ».
- **Agami** : multi family office. Différence single/multi, honoraires, montée du non-coté.
- **Herrmann** : foncière familiale fondée en 1946. Description : « 100 M€ d'acquisitions et de cessions par an ». Club deals et co-investissement, effet de levier et diversification vers l'hôtellerie, achat d'indivisions décotées revendues « x2 », vente à perte pour couper ses pertes.

**Critères implicites des family offices** (synthèse AV4 à partir des descriptions, non une citation) :
- horizon long et transmission ;
- gouvernance et alignement avec l'entrepreneur ;
- préférence pour des **actifs tangibles avec un opérateur fort** (Herrmann, Biousse, Gloaguen en F20) ;
- co-investissement en club deal plutôt que fonds aveugle.

**Limites** : aucune interview n'est accessible en texte ; ce sont des intentions déclarées.

**Application au projet.** Un family office peut financer un domaine équestre si trois conditions sont réunies :
- **(a)** un opérateur crédible ;
- **(b)** un actif patrimonial transmissible (foncier, bâti historique) ;
- **(c)** un **usage** possible : chevaux, séminaires, réceptions familiales. La mission 1 parlait déjà d'« investisseur-usager ».

Les cibles naturelles : foncières familiales régionales (type Herrmann), holdings d'entrepreneurs ayant vendu leur société (Benabou ; Anne-Laure Constanza, AV4-058, qui a repris Toulemonde Bochart après la vente d'Envie de Fraise), family offices passionnés de cheval (à identifier). La « transparence totale » (Mulliez, Nabais) sert d'outil de confiance.

### Passages importants (timelines audio des auteurs ; chapitres YouTube pour Herrmann)

- #284, 00:21:00 — La vente de Smartbox ; 00:46:00 — Otium Capital
- #252, 01:46:06 — Business angel : comment aider les entrepreneurs à réussir
- #249, 01:55:20 — Décomplexer le luxe en hôtellerie
- #499, 01:29:32 — Le rachat express du FC Versailles ; 01:38:11 — Assumer son ambition et choisir de TOUT montrer
- Herrmann, 11:06 — Club deals et co-investissement : https://www.youtube.com/watch?v=OoLm1Lt5-ug&t=666s
- Herrmann, 15:03 — Effet de levier et diversification d'actifs : https://www.youtube.com/watch?v=OoLm1Lt5-ug&t=903s
- Herrmann, 20:46 — Indivision : acheter décoté, revendre x2 : https://www.youtube.com/watch?v=OoLm1Lt5-ug&t=1246s

**Note : 60/100.**

---

## F16 — GDIY #461 « Sébastien Bazin - PDG du groupe Accor » : séparer les murs de l'exploitation

### Identification

- **Réf.** : AV4-070.
- **Intervenants** : Sébastien Bazin ; hôte Matthieu Stefani.
- **Date** : 06/04/2025.
- **Durée** : 2:18:46.
- **URL** : https://www.gdiy.fr/podcast/sebastien-bazin/
- **Niveau d'accès** : DESCRIPTION/CHAPITRES LUS (flux RSS).

### Analyse

- Accor s'est séparé de son immobilier pour se concentrer sur l'exploitation (stratégie « asset light »). Selon la description, ce choix lui a permis de survivre au Covid.
- Le montant cité dans la description (« 180 milliards d'actifs immobiliers ») **n'est pas vérifié et paraît peu plausible**. À ne pas reprendre.
- Chapitres sur les facteurs clés de succès en hôtellerie et sur l'impact d'Airbnb et de Booking.

**Application au projet.** Le cœur de l'hôtellerie moderne repose sur la **dissociation entre propriétaires de murs et exploitants**. Pour un domaine, cela rend crédible :
- **(a)** un montage où des investisseurs détiennent les murs et le porteur l'exploitation (mais l'habitation privée se complique) ;
- **(b)** l'inverse : le porteur garde les murs et confie l'exploitation hôtelière à un opérateur sous bail ou contrat de gestion.

Le choix dépend du profil du client (opérateur ou propriétaire).

### Passages importants (timeline audio de l'auteur)

- 00:31:01 — Le pari qui a sauvé Accor pendant le Covid
- 01:19:21 — Les facteurs clé de succès en hôtellerie
- 01:22:46 — Ce que Airbnb et Booking ont changé pour toujours

**Note : 50/100.**

---

## F17 — La Martingale #311 « Investir dans l'hôtellerie à partir de 1000€ » (Steve Lepine, Monolithe)

### Identification

- **Réf.** : AV4-080.
- **Intervenants** : Steve Lepine (fondateur de Monolithe, plateforme d'investissement hôtelier) ; hôte Matthieu Stefani.
- **Date** : 02/04/2026.
- **Durée** : 1:00:30.
- **URL** : https://lamartingale.io/tous/investir-dans-lhotellerie-a-partir-de-1-000e/ (et site https://monolithe.co/).
- **Niveau d'accès** : DESCRIPTION/CHAPITRES LUS (notes détaillées du site de l'émission). Site de Monolithe lu (PAGE LUE).

### Analyse

**Résumé.** Plaidoyer pour l'investissement hôtelier en « murs + fonds » : les investisseurs détiennent les murs **et** l'exploitation. Ils encaissent donc le chiffre d'affaires et captent la hausse de rendement liée à une meilleure gestion. Le risque est plus élevé que dans un bail classique.

**Règles d'or** (selon l'invité) :

| Critère | Repère |
|---|---|
| Segment | 2 à 4 étoiles |
| Taille idéale | **20 à 50 chambres** (moins de 20 : pas d'économies d'échelle ; plus de 50-60 : concurrence des chaînes, prix d'acquisition élevés) |
| Taux d'occupation minimal | 70-75 % en ville, 50-60 % en station saisonnière |
| Coût par chambre | **environ 100 000 € en province** (exemple : Narbonne, nuitées à 80-100 €) ; 350 000 à 500 000 € à Paris en 3 étoiles |

**Montage type** (notes de l'épisode) :
- environ **2 M€ de fonds propres** d'investisseurs, plus **50-60 % de dette bancaire**, pour des actifs de **4-5 M€** ;
- horizon de 5 ans ;
- objectif d'environ **10 % par an**, soit environ 5 % distribués et 5 % capitalisés à la revente ;
- frais : 3-4 % à l'entrée, une part du chiffre d'affaires pour la gestion, et un « carried » (intéressement du gérant) de 15-20 % au-delà de l'objectif.

**Site de Monolithe** (S-AV4-46) :
- chaque club deal est une émission obligataire (document d'information AMF), hors IFI ;
- « la plupart des investissements » seraient éligibles au **150-0 B ter** (réinvestissement du produit de cession par les entrepreneurs qui vendent leur société) ;
- pour posséder seul un hôtel, il faut **20 à 30 % d'apport**, soit au moins 1,5 M€ à Paris, ou « à partir de 500 k€ » en région pour « quelques rares hôtels ».

**Statut.**
- Repères et rendements : DÉCLARATIF (plateforme intéressée).
- La règle 150-0 B ter est VÉRIFIÉE sur le BOFiP (version 2026). Depuis le 21/02/2026, le réinvestissement doit atteindre **70 % en 3 ans** (et non plus 60 % en 2 ans), avec conservation 5 ans. L'activité doit être commerciale, agricole, etc. La **gestion de son propre patrimoine immobilier, y compris la location meublée, est exclue**. Les biens immobiliers nécessaires à l'exploitation sont admis.
- Le site de Monolithe n'a pas été vérifié sur l'éligibilité de chaque opération.

**Application au projet.**
1. Pour être « investissable » par des **club deals hôteliers**, la partie hébergement du domaine doit viser **au moins 20 chambres** et un exploitant crédible.
2. Avec environ 100 k€ par chambre en province, 20-25 chambres représentent 2-2,5 M€ de valeur hôtelière. C'est l'ordre de grandeur d'un montage « 1 M€ de fonds propres d'investisseurs + 1-1,5 M€ de dette » (ESTIMATION AV4).
3. L'objectif d'environ 10 % par an des investisseurs donne le **coût du capital** à battre.
4. Le **150-0 B ter** ouvre un vivier d'investisseurs (voir l'idée I8), à condition que la société soit **exploitante intégrée** et que **l'habitation privée en soit exclue**.

### Passages importants

Aucun horodatage publié (ni page ni flux RSS).

**Note : 80/100.**

---

## F18 — Extendam : un fonds qui achète des hôtels avec leurs exploitants (Kapi Club EP.5 et HospitalityON)

### Identification

| Réf. | Contenu | Date | Durée |
|---|---|---|---|
| AV4-081 | Kapi Club EP.5, « Créer le leader européen de l'investissement hôtelier et gérer plus de 350 hôtels - JM Palhon » (hôte Lauren Dannay) | inconnue (« il y a 2 ans ») | 47:50 |
| AV4-083 | HospitalityON, « EXTENDAM, Bpifrance et Solanet signent le plus gros deal de l'année » | inconnue (« il y a 5 ans ») | 5:12 |

- **URL** : https://www.youtube.com/watch?v=Fi433rXPRks et https://www.youtube.com/watch?v=Qi484fH4wVM (site https://www.extendam.com/).
- **Niveau d'accès** : chapitres YouTube (origine non confirmée). Site d'Extendam lu.

### Analyse

**Modèle.** Site lu : Extendam acquiert « les murs et fonds de commerce d'hôtels » de milieu et de haut de gamme en Europe, et prend des participations « dans des PME propriétaires d'hôtels ». Ses équipes interviennent du sourcing à l'exploitation.

Le reportage HospitalityON décrit un **rachat de la holding familiale SCSP** (plusieurs hôtels) par un trio : fonds hôtelier, Bpifrance et exploitant (Solanet Gestion Hôtelière).

Chapitres de l'entretien : du fonds PME généraliste au fonds hôtelier, modèle Extendam, avantages « murs et exploitation », cycles, taux d'occupation, **rendement cible d'un hôtel**.

**Limites.** Aucun chiffre accessible. « Leader européen » et « 350 hôtels » sont des affirmations de l'intéressé.

**Application au projet.** Le montage **fonds spécialisé + exploitant + Bpifrance** est la voie institutionnelle pour racheter un **hôtel ou un domaine familial à transmettre**. Le porteur apporte l'exploitation et une petite part du capital ; le fonds porte l'essentiel des fonds propres.

Pour un domaine équestre, il faudrait :
- un **volet hôtelier significatif** (plus de 20 chambres) ;
- un exploitant hôtelier associé, si le client n'en a pas l'expérience.

### Passages importants

- Kapi Club, 15:05 — Le modèle Extendam : https://www.youtube.com/watch?v=Fi433rXPRks&t=905s
- Kapi Club, 20:20 — Les avantages de l'investissement en hôtellerie : murs et exploitation : https://www.youtube.com/watch?v=Fi433rXPRks&t=1220s
- Kapi Club, 28:20 — Les cycles dans l'hôtellerie : https://www.youtube.com/watch?v=Fi433rXPRks&t=1700s
- Kapi Club, 35:30 — Quel est le rendement cible d'un investissement dans un hôtel ? : https://www.youtube.com/watch?v=Fi433rXPRks&t=2130s
- HospitalityON, 3:35 — Pourquoi vos deux sociétés se sont alliées ? : https://www.youtube.com/watch?v=Qi484fH4wVM&t=215s

**Note : 70/100.**

---

## F19 — Kapi Club EP.3 « Créer un groupe de 12 hôtels parisiens en partant de 0 ! » (Yohann Benhamou, Malone Hotels)

### Identification

- **Réf.** : AV4-082.
- **Date** : inconnue (« il y a 2 ans »).
- **Durée** : 49:57.
- **URL** : https://www.youtube.com/watch?v=Jfd_r9VcNUc
- **Niveau d'accès** : chapitres et extrait de description (« néophyte dans le secteur et sans réseau »).

### Analyse

Entrepreneur entré dans l'hôtellerie **sans expérience ni réseau**, à la tête de 12 hôtels parisiens selon le titre.

Chapitres :
- étudier les dossiers avant d'investir ;
- **TRI cibles pour un hôtel** ;
- impact des Jeux olympiques ;
- lutte avec Booking, Expedia et Google ;
- **« Le ratio financement bancaire sur les dossiers »** ;
- comment se lancer.

**Limites** : aucun chiffre accessible. Contexte parisien (valeurs très supérieures à la province).

**Application.** Contre-exemple au préjugé « il faut venir du métier ». À écouter pour les ratios bancaires réels (chapitre 41:30) avant de bâtir le plan de financement d'un volet hôtelier.

### Passages importants

- 7:00 — Comment étudier les dossiers avant d'investir : https://www.youtube.com/watch?v=Jfd_r9VcNUc&t=420s
- 17:20 — Quels sont les TRI cibles pour un hôtel ? : https://www.youtube.com/watch?v=Jfd_r9VcNUc&t=1040s
- 41:30 — Le ratio financement bancaire sur les dossiers : https://www.youtube.com/watch?v=Jfd_r9VcNUc&t=2490s
- 45:20 — Comment se lancer dans l'hôtellerie ? : https://www.youtube.com/watch?v=Jfd_r9VcNUc&t=2720s

**Note : 70/100** (pertinence élevée, accès faible).

---

## F20 — BUILD : « Entrepreneuriat hôtelier : comment bâtir une marque d'hôtels design à Paris » (Adrien Gloaguen, Touriste et Campings Liberté)

### Identification

- **Réf.** : AV4-084.
- **Intervenants** : Adrien Gloaguen ; hôte Xavier Rodriguez (PDG du groupe Jarnias).
- **Chaîne** : BUILD (Ausha et YouTube 3jeYoAxFhPA).
- **Date** : 01/10/2025 (flux RSS). La vidéo YouTube est indiquée « il y a 1 an ».
- **Durée** : 1:17:03.
- **URL** : https://podcast.ausha.co/build/adrien-gloaguen-comment-il-est-devenu-le-proprietaire-des-hotels-les-plus-styles-de-paris
- **Niveau d'accès** : DESCRIPTION/CHAPITRES LUS. Les chapitres YouTube, détaillés, sont d'origine non confirmée. Article TourMaG lu pour la vérification.

### Analyse

**Points de la description** :
- refuser la standardisation ;
- **« s'associer à des family office plutôt qu'à des gros fonds »** ;
- le premium à prix accessible ;
- viser **au moins 40 % d'EBITDA par hôtel**.

**Vérification** (TourMaG, page lue) :
- groupe Touriste **fondé en 2008** ;
- 4 hôtels parisiens (Panache, Bienvenue, Beaurepaire, Deux Gares) et un hôtel en cours d'ouverture à Londres ;
- **première ouverture de capital : 2,4 M€ apportés par Bpifrance**. Un résultat de recherche (CFNews) indique que le groupe était détenu à 100 % par son dirigeant jusque-là : non vérifié.

**Statuts** :
- 2,4 M€ de Bpifrance : VÉRIFIÉ ;
- family offices et 40 % d'EBITDA : DÉCLARATIF.

**Chapitres YouTube utiles** :
- financement du premier hôtel ;
- partenariat avec des family offices ;
- achat du fonds de commerce ou des murs ;
- diversification dans les campings et **intérêt pour les campings municipaux**.

**Limites** : le récit du financement du premier hôtel n'est pas accessible en texte.

**Application au projet.**
1. Le modèle **« opérateur + family offices au capital des murs »** est la version hôtelière du club deal de Fontenay.
2. **Bpifrance investit en fonds propres minoritaires** dans des groupes touristiques en croissance.
3. Les **campings municipaux** (délégation de service public) sont une porte d'entrée peu capitalistique, voir F25.
4. L'objectif de 40 % d'EBITDA donne la mesure de l'exigence opérationnelle attendue par ces partenaires.

### Passages importants (chapitres YouTube, origine non confirmée)

- 4:21 — Premier hôtel repris : https://www.youtube.com/watch?v=3jeYoAxFhPA&t=261s
- 6:08 — Financement du premier hôtel : https://www.youtube.com/watch?v=3jeYoAxFhPA&t=368s
- 17:26 — Retour sur investissement et business model : https://www.youtube.com/watch?v=3jeYoAxFhPA&t=1046s
- 20:33 — Financement des hôtels et partenariat avec des family offices : https://www.youtube.com/watch?v=3jeYoAxFhPA&t=1233s
- 53:02 — Achat du fonds de commerce ou des murs : https://www.youtube.com/watch?v=3jeYoAxFhPA&t=3182s
- 56:36 — Diversification avec les campings : https://www.youtube.com/watch?v=3jeYoAxFhPA&t=3396s
- 59:27 — Intérêt pour les campings municipaux : https://www.youtube.com/watch?v=3jeYoAxFhPA&t=3567s

**Note : 80/100.**

---

## F21 — Banque des Territoires : l'investisseur public au capital des sociétés immobilières touristiques

### Identification

- **Réf.** : AV4-085, « Financement d'un hôtel – Région Normandie ».
- **Chaîne** : Banque des Territoires (YouTube).
- **Date** : inconnue (« il y a 4 ans »).
- **Durée** : 1:42.
- **URL** : https://www.youtube.com/watch?v=MCJRqI0nbZo
- **Niveau d'accès** : REPÉRÉ (extrait de description). Sources complémentaires : pages de la Caisse des Dépôts et de la Banque des Territoires **INACCESSIBLES (maintenance)** le 14/10/2026. Leur contenu n'est connu que par des **résumés de résultats de recherche** (S-AV4-56 à 58).

### Analyse

**Extrait de la description** : la Banque des Territoires « a investi dans le programme hôtelier en montant au capital de la SCI qui porte le projet ». Le montant est tronqué dans l'extrait.

**Informations secondaires** (résultats de recherche, **à confirmer**) :
- la Banque des Territoires se positionne en **co-investisseur minoritaire en fonds propres** dans des sociétés propriétaires d'hébergements touristiques ;
- elle a créé une **société commune avec Les Domaines de Fontenille** pour la croissance externe du groupe. Première acquisition : le Manoir du Sphinx (Perros-Guirec), financé par ses fonds propres et un prêt du Crédit Agricole ;
- en **Bourgogne-Franche-Comté**, une **foncière hôtelière** (SAS de 5 M€) a été créée : Banque des Territoires 39 %, Région 20 %, Batifranc 20 %, banques régionales 21 %. Elle investit dans des murs d'hôtels ou dans des sociétés immobilières à objet hôtelier ;
- à Bayeux, la Banque des Territoires a **prêté** 498 290 € à une SCI pour rénover un hôtel (projet de 2,8 M€).

**Limites** : sources inaccessibles. À revérifier quand les sites seront rétablis.

**Application au projet.** Si le domaine comprend un **volet hébergement touristique exploité par un opérateur qui porte le risque commercial**, une **foncière publique ou parapublique** peut réduire de manière significative les fonds propres à trouver. Le montant exact dépend de chaque dossier.

**Le choix de la région** (encore inconnu, mission 1) peut tenir compte de l'existence de ces outils. La Bourgogne-Franche-Comté en a un, selon le résultat de recherche.

### Passages importants

Aucun (vidéo de 1:42 non accessible).

**Note : 65/100** (piste institutionnelle forte, à confirmer).

---

## F22 — La Vie : « HÔTELLERIE : Comment reprendre un petit hôtel de campagne ? » (documentaire)

### Identification

- **Réf.** : AV4-087.
- **Chaîne** : La Vie (YouTube).
- **Date** : inconnue (« il y a 5 mois »).
- **Durée** : 54:49.
- **URL** : https://www.youtube.com/watch?v=JZzrqb6uIec
- **Niveau d'accès** : chapitres YouTube (origine non confirmée).

### Analyse

Portraits de repreneurs de petits hôtels ruraux :
- « Auvergne : l'investissement de 60 000 € de Laura et Richard » ;
- un hôtel de 150 ans relancé ;
- un 3 étoiles familial sur trois générations ;
- des reconversions ;
- cabanes finlandaises en kit ;
- **« Chantier : quand le budget travaux triple »** ;
- diversification en club de vacances.

**Limites** : la nature de l'investissement de 60 000 € (fonds de commerce, apport, travaux ?) est inconnue.

**Application.**
- Le multiplicateur de dépassement de budget (×3 dans un cas filmé) rejoint les dépassements de Fontenay (F02). Il faut prévoir **une réserve pour imprévus d'au moins 30 %** (repère AV4) dans le plan de financement.
- Des **hébergements légers** (cabanes en kit) permettent d'ajouter des couchages à faible coût.

### Passages importants

- 0:00 — Auvergne : l'investissement de 60 000 € de Laura et Richard : https://www.youtube.com/watch?v=JZzrqb6uIec&t=0s
- 17:33 — Bretagne : construire ses cabanes finlandaises en kit : https://www.youtube.com/watch?v=JZzrqb6uIec&t=1053s
- 22:05 — Chantier : quand le budget travaux triple : https://www.youtube.com/watch?v=JZzrqb6uIec&t=1325s
- 28:33 — Diversification : transformer un hôtel en club de vacances : https://www.youtube.com/watch?v=JZzrqb6uIec&t=1713s

**Note : 65/100.**

---

## F23 — S'endetter jeune : Jonathan Anguelov (#119) et Léo Nardecchia (#197), « Ça fait un bail ! »

### Identification

| Réf. | Contenu | Date | Durée |
|---|---|---|---|
| AV4-092 | « Acheter des hôtels et monter des licornes - Jonathan Anguelov (Aircall, Aguesseau Capital) #119 » | 25/06/2023 | 51:00 |
| AV4-094 | « Investir à 25 ans avec 1 Million d'euros de dette - Léo Nardecchia #197 » | 18/11/2025 | 53:47 |

- **Niveau d'accès** : DESCRIPTION/CHAPITRES LUS (notes du flux RSS).

### Analyse

**Anguelov.** À 19 ans, « plusieurs prêts étudiants » pour acheter 10 chambres de bonne à Paris exploitées en location saisonnière. Puis marchand de biens, achat de plusieurs hôtels (Maison Barbès, ouverte en plein Covid). Cofondateur d'Aircall. Montée en gamme des hôtels (gagner des étoiles).

**Nardecchia.** À 25 ans, **1 M€ de dette levée**. Plus de 30 biens locatifs, des dizaines d'opérations de marchand de biens, plus de 300 investisseurs accompagnés comme chasseur immobilier. Il évoque une « levée de dettes intelligente ».

**Statut** : DÉCLARATIF pour l'ensemble.

**Limites.**
- Contextes de taux bas, au moins pour le premier.
- Le prêt étudiant détourné vers l'immobilier est un montage risqué, à ne pas recommander.

**Application au projet.** À 26 ans, le levier bancaire reste accessible si **chaque opération est autoportante**. Une **activité de chasse ou de marchand de biens** constitue à la fois un historique bancaire, une épargne et un **réseau d'investisseurs** : c'est le même schéma que Nabais. Ce peut être une étape 2026-2029 avant le château.

### Passages importants

Aucun horodatage publié.

**Note : 55/100.**

---

## F24 — Outils de financement du foncier : club deals (Wevest #250), marchand de biens (#258), terres agricoles (Hectarea #279), home equity (#290), Kapi (#268)

### Identification

| Réf. | Contenu | Date |
|---|---|---|
| AV4-096 | La Martingale #250 | 30/01/2025 |
| AV4-095 | La Martingale #258 | 27/03/2025 |
| AV4-098 | La Martingale #279 | 21/08/2025 |
| AV4-100 | La Martingale #290 | 06/11/2025 |
| AV4-097 | La Martingale #268 | 05/06/2025 |
| AV4-099 | La Martingale #326 (forêt) | 16/07/2026 (repéré) |

- **URL** : voir le catalogue.
- **Niveau d'accès** : DESCRIPTION/CHAPITRES LUS (notes du site) sauf #326.

### Analyse

**Club deal immobilier** (#250, Hugo Wind, Wevest) :
- une **société dédiée par projet** ;
- l'analyse porte sur le porteur (expérience, capacité financière, implication), la structure financière (dette, apport, garanties) et le projet ;
- **fonds débloqués par étapes** : acte notarié pour l'achat, devis pour les travaux ;
- garanties : **hypothèque de 1er rang ou fiducie-sûreté** ;
- risques : perte, retard, illiquidité ;
- rendements « parfois 10-12 % » (DÉCLARATIF).

**Marchand de biens** (#258, Yoni Buchsbaum) :
- valeur créée par les travaux, le **changement de destination**, la **division** et le déblocage juridique ou administratif ;
- marges « pouvant dépasser 20 % » (DÉCLARATIF, formateur).

**Terres agricoles** (#279, Paul Rodrigues, Hectarea) :
- investissement fractionné **dès 500 €** via des **obligations garanties par une hypothèque de 1er rang** ;
- rendement global visé 4-7 % ;
- prix moyen **6 000 à 8 000 €/ha** ;
- passage obligé par la **SAFER** (droit de préemption) ;
- « 30 % des terres acquises par des non-agriculteurs » : DÉCLARATIF.

**Home equity** (#290) : un financeur paie la rénovation contre une part de la valeur future.

**Kapi** (#268) : cercle privé d'investissement immobilier (club deals, crowdfunding, fractionné).

**Limites.** Discours de plateformes qui vendent leurs produits. Les garanties de 1er rang réclamées par les club deals **entrent en concurrence** avec celles des banques.

**Application au projet.**
1. **Découper le financement par nature d'actif.** Le foncier agricole (une partie des 50 ha et plus) peut être porté par des investisseurs « terres », remboursés par un fermage payé par l'activité équestre agricole. Les bâtiments le sont par la SCI, l'exploitation par la SAS.
2. **Revendre ou valoriser l'excédent** (logique de marchand de biens, idée I9).
3. Si un club deal intervient, le **rang des sûretés** doit être négocié dès l'origine : la banque voudra le 1er rang.

### Passages importants

Aucun horodatage publié sur ces pages.

**Note : 60/100.**

---

## F25 — Campings : Huttopia (délégations de service public), Radio Camping, reportages

### Identification

- **Réf.** : AV4-101 à 113 (Huttopia : 101 à 103 ; Radio Camping : 105 à 110 ; « Vous avez dit petit camping » : 104 ; reportages : 111 à 113).
- **Dates** : flux Radio Camping de 2022 à 2025 ; YouTube relatives.
- **Niveau d'accès** : DESCRIPTION LUE pour Radio Camping, REPÉRÉ pour les vidéos. Article TourMaG lu.

### Analyse

**Huttopia** (TourMaG, page lue) :
- Huttopia reprend le réseau **OnlyCamp** (8 campings en Centre-Val de Loire et Pays de la Loire, créé par Récréa, spécialiste des délégations de service public) ;
- Huttopia annonce développer ce réseau « par la reprise de campings via des **délégations de service public** ou par rachat ». « Trois campings ont déjà été repris dans ce cadre ».

Autres éléments, seulement repérés :
- un résultat de recherche (Modern Campground) mentionne un projet sur un **terrain privé de 27 ha avec un bail de 50 ans** (4-6 M€ d'investissement annoncés) ;
- le reportage TVBA montre le **camping municipal d'Arcachon** devenu un Huttopia après un an de travaux.

**Radio Camping** :
- courtier spécialisé dans le **financement de l'achat de campings** (Coventis) ;
- vente et valorisation de campings (Concerto, Cabinet Cantais, BDO) ;
- **parcs résidentiels de loisirs (PRL)**, où les vacanciers sont propriétaires de leur parcelle ;
- couple en reconversion ayant acheté un camping.

**Limites** : aucun chiffre (descriptions sans montants).

**Application au projet.**
1. **Exploiter sans acheter.** Délégation de service public, concession ou bail emphytéotique sur un domaine public : la mission 1 a déjà relevé des exemples de baux emphytéotiques. Un château communal à restaurer peut se négocier ainsi.
2. **Bail de longue durée sur le terrain d'autrui** (50 ans, Huttopia) : adaptable aux prairies et aux dépendances d'un domaine dont le propriétaire ne veut pas vendre.
3. L'hôtellerie de plein air est un **secteur bancable** avec ses courtiers spécialisés. Un volet « glamping » ou cabanes adossé au domaine sera plus facile à financer que le château lui-même (voir aussi les lodges du château de Villeneuve, AV4-019).
4. Le modèle **PRL** (parcelles vendues à des propriétaires) peut financer des équipements. Il suppose des autorisations d'urbanisme lourdes, point non vérifié.

### Passages importants

Aucun horodatage publié dans les descriptions consultées.

**Note : 55/100.**

---

## F26 — Acquiring Minds « Buying a $7.3m Golf Course with No Money Down » (Kyle Holmes, Quail Ridge Golf Club)

### Identification

- **Réf.** : AV4-116.
- **Intervenants** : Kyle Holmes (directeur, puis copropriétaire) ; hôte Will Smith.
- **Chaîne** : Acquiring Minds.
- **Date** : 24/09/2026.
- **Durée** : 1:30:04.
- **URL** : https://acquiringminds.co/articles/kyle-holmes-quail-ridge-golf-club
- **Niveau d'accès** : TRANSCRIPTION TEXTE LUE (partielle : passages sur le financement, la valeur du terrain et les motivations des vendeurs), plus le résumé détaillé publié par l'hôte.

### Analyse

**Résumé.**
- Kyle Holmes dirige depuis des années le golf public de Quail Ridge, près de Grand Rapids (Michigan). Le golf a été construit en 1998 par 23 investisseurs ; au moment de la vente, il en restait 8, dont 3 majoritaires.
- Les propriétaires lui proposent de racheter. Avec le surintendant du parcours (Tim), il achète pour **7,3 M$ sans argent personnel**. Closing le 27/01/2025.

**L'actif.**
- 275 acres (environ 111 ha), dont environ 160 acres de parcours, un club-house, une structure événementielle et un atelier ;
- environ 45 000 parcours par an ;
- recettes : environ 70 % golf, 10 % practice, 6-7 % restaurant, le reste en événements.

**Le prix.**
- Cash-flow avant vente : 500 à 700 k$ par an les meilleures années.
- Les golfs se vendent 4 à 9 fois l'EBITDA.
- **Le terrain seul vaudrait au moins 10 M$** selon l'invité, mais il n'est pas entièrement constructible (zones humides, moitié d'un lac).
- Offre à 6,5 M$, contre-offre à 7,3 M$ acceptée. Expertise d'un évaluateur spécialisé à exactement 7,3 M$ après trois semaines d'attente.

**Plan de financement (capital stack).**

| Brique | Part | Remarque |
|---|---|---|
| Prêt SBA 504 | 40 % | programme fédéral américain |
| Prêt bancaire classique | 50 % | |
| Crédit-vendeur (seller note) | 10 % | |
| Amortissement | 25 ans, étendu à la part bancaire | environ 42 k$/mois, soit environ 500 k$/an. Des durées classiques de 5 à 10 ans auraient rendu l'opération impossible |

**Première année** (DÉCLARATIF) :
- 3,3 M$ de recettes et 2,1 M$ de charges, soit 1,2 M$ de résultat d'exploitation (NOI) ;
- un peu moins de 700 k$ de cash après intérêts, amortissements et location des voiturettes ;
- soit l'équivalent de la meilleure année des vendeurs, malgré 350-400 k$ d'intérêts supplémentaires.

**Motivation des vendeurs** : ils ont préféré leurs deux cadres à un groupe local de rachat de golfs, pour que le club reste indépendant et local. Selon l'hôte, le prix « optimisé » aurait été la vente du terrain à un promoteur.

**Gouvernance** :
- 50/50 entre les deux associés, Holmes ayant la voix prépondérante ;
- **aucune distribution de dividendes pendant 5 ans**, inscrite dans les statuts (operating agreement) : salaires de marché seulement.

**Développement prévu** :
- simulateurs autofinancés pour l'hiver ;
- salle de banquet ouverte toute l'année pour tripler les événements ;
- **promotion résidentielle sur 30 acres inutilisés** ;
- objectif : multiplier le chiffre d'affaires par 2,5 d'ici 2031-2032.

**Statuts.**
- Tous les montants sont DÉCLARATIFS (invité et hôte). Aucune source indépendante consultée.
- Les règles du programme SBA 504 (apport exigé, crédit-vendeur compté comme apport) n'ont **pas** été vérifiées.
- Contexte : le durcissement du programme SBA 7(a) au 01/06/2025 (Whiteford, page lue) est postérieur à ce closing.

**Limites.** Récit d'un succès, programme public américain, un seul cas.

**Transposabilité en France.**

Ce qui ne se transpose pas : il n'existe **pas d'équivalent au SBA 504** (prêt garanti par l'État fédéral, amorti sur 25 ans, sur un actif d'exploitation). Les équivalents partiels, vérifiés par la mission 1 ou par AV4 :
- prêts hypothécaires de 15 ans (Bpifrance, durée normative avec hypothèque) ;
- crédit-bail immobilier de 8 à 15 ans ;
- garantie Bpifrance de 50 à 70 % sur les reprises ;
- crédit-vendeur de 30 à 50 % sur 1 à 5 ans (CRA), sécurisé par l'**hypothèque légale spéciale du vendeur**. Comme celle-ci prime le prêteur de deniers, une subordination est à négocier (notaire, page lue).

Ce qui se transpose :
- **devenir l'exploitant avant d'être l'acheteur** ;
- **viser des vendeurs attachés à la continuité** ;
- **faire valoir la valeur foncière supérieure au prix** comme garantie auprès des banques françaises (qui prêtent sur la valeur du bien) ;
- **interdire les distributions** pendant la phase de remboursement ;
- **monétiser le foncier inutilisé**, sous réserve du PLU.

**Application au projet.**
- Une famille propriétaire d'un domaine équestre ou d'un château-hôtel sans successeur est la cible idéale.
- Le client se positionne d'abord comme **directeur ou gérant** (voir l'idée I3). Il négocie ensuite un rachat progressif avec crédit-vendeur et dette longue adossée aux murs.

### Passages importants

La transcription publiée n'a pas d'horodatage : aucun minutage n'est cité.

**Note : 90/100.** Montage le plus proche de « gros actif foncier de loisirs acquis sans argent personnel par un opérateur ».

---

## F27 — Acquiring Minds « How 1 SBA Loan Brought Down 2 Businesses » (Edgar Galindo) : l'échec

### Identification

- **Réf.** : AV4-117.
- **Date** : 30/07/2026.
- **Durée** : 1:34:37.
- **URL** : https://acquiringminds.co/articles/edgar-galindo-structure-landscapes
- **Niveau d'accès** : TRANSCRIPTION TEXTE LUE (partielle) et résumé de l'hôte.

### Analyse

**Faits** (DÉCLARATIFS) :

| Étape | Détail |
|---|---|
| 1er rachat (Austin, paysagiste) | CA de 4,8 M$, environ 900 k$ de bénéfice disponible pour le propriétaire (SDE). Prix d'environ 3,15 M$ (3,5 fois le SDE), dont 500 k$ de crédit-vendeur. Galindo apporte 50 k$ pour 25 % (option jusqu'à 50 %) et **signe une caution personnelle** sur le prêt SBA |
| 2e rachat, six mois plus tard (Dallas) | CA d'environ 6 M$, SDE de 950 k$ |
| Problèmes du 2e rachat | commission cachée de 100 k$ (soit environ 350 k$ surpayés au multiple), litige avec le vendeur (plus de 160 k$ d'avocats), départs de salariés, clients détournés, concurrent créé |
| Issue | la dette du 2e rachat pèse sur le 1er. **Les deux sociétés ferment**, faillite personnelle |

**Leçons tirées par l'invité** :
- interroger les salariés pendant l'audit (due diligence) ;
- se méfier du vendeur qui refuse cet accès ;
- « le plus grand risque n'était pas d'acheter la mauvaise entreprise, mais de faire confiance au mauvais vendeur » (paraphrase).

**Application au projet** (transposition française, analyse AV4) :
- **Caution personnelle** : la garantie Bpifrance limite les cautions à 50 % (mission 1) mais ne les supprime pas. La garantie couvre la banque, pas l'emprunteur (Bpifrance Création).
- **Contamination entre sociétés** : ne jamais faire garantir la dette de l'exploitation par la SCI qui détient le château, ni l'inverse, sans mesurer le risque de perdre le domaine.
- **Audit et garantie d'actif et de passif** : un crédit-vendeur peut servir de levier de négociation en cas de passif caché. L'articulation entre les deux est à faire valider par un avocat.

### Passages importants

Aucun horodatage publié.

**Note : 60/100.**

---

## F28 — BiggerPockets Business #68 « Buy Then Build Your Business With Best-Selling Author Walker Deibel »

### Identification

- **Réf.** : AV4-119.
- **Intervenants** : Walker Deibel ; hôtes J Scott et Carol Scott.
- **Date** : 11/08/2020 (date de publication de la page).
- **Durée** : 1:26:39 (YouTube).
- **URL** : https://www.biggerpockets.com/blog/biggerpockets-business-podcast-68-walker-deibel
- **Niveau d'accès** : TRANSCRIPTION TEXTE LUE (partielle ciblée).

### Analyse

**Thèses de Deibel** (paraphrase) :
- racheter une entreprise apporte à l'entrepreneuriat la **mécanique de l'immobilier** : apport, dette, revenus des clients qui remboursent la dette, plus la croissance que l'on contrôle ;
- grille de lecture en quatre familles : rentable durable, redressement, forte croissance, plateforme ;
- la prospection directe de vendeurs est difficile : un cédant met 9 à 18 mois à « s'éduquer » sur la valeur de son entreprise ;
- l'intermédiaire représente le vendeur ;
- « si vous ne faites pas confiance au vendeur, partez » ;
- on peut acheter « à 3x avec un prêt bancaire et 10 % d'apport » (contexte SBA de 2020) ;
- commencer par une seule entreprise et la diriger environ 7 ans.

Il revendique un **rendement annuel composé de 52 %** sur sa mise en 4,5 ans : DÉCLARATIF, non vérifié.

**Témoignage de l'hôte (J Scott)** : rachat d'une entreprise de travaux.
- Acompte égal à la **valeur du stock (environ 30 % du prix)**, 70 % payés sur 2 ans au vendeur.
- Le vendeur reste titulaire de la licence professionnelle pendant 18 mois.
- Ce choix a été fait parce que le prêt SBA aurait demandé environ 6 mois (embouteillage lié aux prêts Covid).
- L'hôte souligne que le « no money down » n'est pas la norme.

**Limites.** Contexte américain de 2020 (SBA, taux bas). Promotion d'un livre et d'un programme.

**Application.**
- Le **crédit-vendeur court (2 ans), adossé à un acompte de 30 %**, est cohérent avec les repères français du CRA (30-50 % sur 1-5 ans).
- La logique « dette remboursée par les revenus de l'actif » est celle que le client doit démontrer à ses banques.

### Passages importants

Transcription sans horodatage.

**Note : 70/100.**

---

## F29 — BiggerPockets Real Estate Rookie 375 « Making $160K/Year From ONE "Rare" Property Thanks to Seller Financing » (Adam Howard, motel de 13 unités)

### Identification

- **Réf.** : AV4-120.
- **Intervenants** : Adam Howard ; hôtes Ashley Kehr et Tony J. Robinson.
- **Date** : 04/03/2024.
- **Durée** : inconnue.
- **URL** : https://www.biggerpockets.com/blog/rookie-375
- **Niveau d'accès** : TRANSCRIPTION TEXTE LUE (partielle ciblée).

### Analyse

**Faits** (DÉCLARATIFS) :
- ancien entraîneur de football universitaire, investisseur depuis 3 ans, 49 ans ;
- repère un **motel de 13 unités** au bord d'un lac (État de New York), mal référencé comme maison individuelle (« 1.3 million » affiché) ;
- le vendeur, dernier actif à liquider, encaissait beaucoup d'espèces : ses comptes ne justifiaient pas un prêt bancaire. D'où le **financement par le vendeur** ;
- **50 k$ d'arrhes, puis 250 k$ d'apport, soit 300 k$** ;
- un associé financier apporte une partie de l'apport ;
- objectif : **refinancer auprès d'une banque après environ 2 ans** de comptes propres ;
- après rénovation (climatisation, kitchenettes), le prix moyen par nuit passe de 70-80 $ à 149-189 $ ;
- l'actif est aussi un lieu de vie familial.

**Limites.**
- Montants non vérifiés.
- L'**argument « espèces non déclarées »** est inutilisable en France : c'est de la fraude, à exclure absolument.

**Application.** Ce qui se transpose : **le vendeur finance une période de transition**, puis la banque refinance une fois l'historique d'exploitation constitué (comptes certifiés, 2 exercices). C'est exactement le problème de Fontenay, qui veut refinancer ses obligations par une banque.

Pour un domaine sans historique commercial, il faut négocier avec le vendeur :
- un crédit-vendeur de 2-3 ans ;
- ou une location avec option d'achat (idée I5).

### Passages importants

Transcription sans horodatage.

**Note : 70/100.**

---

## F30 — Defining Hospitality #100 « Joie de Vivre - Chip Conley » : un motel en faillite racheté à 26 ans

### Identification

- **Réf.** : AV4-135 (et AV4-136, AV4-137).
- **Intervenants** : Chip Conley ; hôte Dan Ryan.
- **Date** : 05/04/2023.
- **Durée** : 1:06:00 (YouTube i_sah7Jx150).
- **URL** : https://defininghospitality.transistor.fm/100/transcript
- **Niveau d'accès** : TRANSCRIPTION TEXTE LUE (partielle). Recoupement sur Wikipédia (page lue).

### Analyse

**Ce que dit Conley** (paraphrase de la transcription) :
- à 26 ans, il achète un **motel délabré, loué à l'heure, en faillite**, et le transforme en hôtel « rock and roll » rebaptisé le Phoenix ;
- avant cela, il travaillait dans une société de promotion immobilière. Il y a découvert l'hôtellerie de charme en analysant un dossier hôtelier en 1985. Son patron refusant de créer une division dédiée, il part ;
- **il possède toujours l'immobilier du Phoenix** 35-36 ans plus tard. Il a vendu en 2010 la **marque et la société de gestion**, pas les murs ;
- son nouveau projet (Modern Elder Academy) prévoit un **ranch équestre « régénératif » de 2 600 acres** près de Santa Fe, avec deux centres de séminaires et du résidentiel.

**Recoupement** (Wikipédia EN, page lue) :
- Joie de Vivre est fondée en 1987, quand Conley a 26 ans ;
- **1 M$ levé en 1987** pour acheter le Phoenix (référence au San Francisco Chronicle) ;
- 2010 : participation majoritaire cédée à **Geolo Capital** (société d'investissement de John Pritzker, héritier Hyatt), avec un fonds de 150 M$ pour acheter d'autres hôtels.

**Statut** : RECOUPÉ (âge, faillite, 1 M$ levé, cession de 2010).

**Limites.** San Francisco des années 1980. Le montage exact (dette, investisseurs) n'est pas détaillé.

**Application au projet.**
1. Un **actif hôtelier en faillite**, racheté jeune avec l'argent d'investisseurs, devient le socle d'une chaîne.
2. Le **schéma de sortie « vendre l'exploitation, garder les murs »** protège le patrimoine du fondateur. C'est l'inverse d'Accor (F16) et le pendant de la séparation SCI / SAS de Fontenay.
3. Le **ranch équestre transformé en lieu de séminaires et de transmission** (Modern Elder Academy) est un modèle hybride « cheval + formation + hébergement » à creuser par AV5 et AV7.

### Passages importants

La transcription comporte des marqueurs [00:02:00], [00:35:00], etc. :
- entre [00:02:00] et [00:03:00] — rachat du motel en faillite à 26 ans, rebaptisé Phoenix ;
- [00:35:00] environ — de 26 ans « fresh out of Stanford business school » à la vente ;
- [01:00:00] environ — l'origine dans la promotion immobilière et le refus de son patron.

Ces marqueurs sont ceux de la transcription publiée (version audio).

**Note : 70/100.**

---

## F31 — Corpus anglophone « no money down » : Codie Sanchez, Sieva Kozinsky, Acquisitions Anonymous, BiggerPockets #799, Walker Deibel 2.0

### Identification

- **Réf.** : AV4-122 à AV4-131.
- **Chaînes** : Codie Sanchez (Contrarian Thinking), POWERS Pod, Flippa, Acquisitions Anonymous, BiggerPockets, Walker Deibel.
- **Dates** : relatives (de 4 mois à 11 ans).
- **Niveau d'accès** : chapitres YouTube (AV4-122, 124, 126, 128, 131) ou REPÉRÉ.

### Analyse

**Promesses.**
- Codie Sanchez, 0,3 à 1 million de vues par vidéo : « How to Buy a Business With No Money in 2024 », « How to Buy a Business for $0 in a Week? », « with Other Peoples Money ».
- Les chapitres portent sur la **prospection** (réseau, bases de données, « Expertise to Equity »), la **conversation avec le vendeur** et le « Venmo Challenge ».
- Les liens de description mènent à une consultation payante et à un guide « Buy a Biz for $0 ».

**Vérification** (Whiteford, page lue). Le SOP 50 10 8 de la SBA, en vigueur au **01/06/2025**, a durci les règles des prêts 7(a) :
- **apport minimal de 10 %** pour les rachats ;
- le crédit-vendeur ne compte que s'il est en **standby total (ni intérêts ni capital) pendant toute la durée** du prêt (généralement 10 ans), et pour **au plus la moitié** de l'apport ;
- les rachats partiels doivent se faire par achat de titres, avec caution de tous les associés pendant 2 ans ;
- le vendeur qui reste associé doit se porter caution.

Les contenus « $0 » de 2022-2024 sont donc **dépassés pour les prêts 7(a)**. Le chapitre « Seller-note on full standby » de Kozinsky (49:29) est cohérent avec cette contrainte.

**Ce qui reste utile.**
- La méthode de **prospection hors marché** (réseau, bases de données, transformer une expertise en part de capital).
- La **holding à capital permanent** de Kozinsky : acheter des entreprises et les garder.

**Application.** Rien de directement transposable sur le financement. Utile comme méthode de **recherche de vendeurs** (familles propriétaires de domaines) et comme mise en garde contre le marketing.

### Passages importants (chapitres YouTube, origine non confirmée)

- Codie Sanchez, 3:49 — How to Have The Conversation : https://www.youtube.com/watch?v=3Gy33tFXmJE&t=229s
- Codie Sanchez, 11:42 — The Personal P&L Review : https://www.youtube.com/watch?v=3Gy33tFXmJE&t=702s
- Codie Sanchez, 46:06 — Expertise to Equity : https://www.youtube.com/watch?v=acEy2I7__Uc&t=2766s
- Kozinsky, 47:25 — How do you incentivize someone to stay on in a long-term hold scenario? : https://www.youtube.com/watch?v=9IyYN3_O80Q&t=2845s
- Kozinsky, 49:29 — Seller-note on full standby : https://www.youtube.com/watch?v=9IyYN3_O80Q&t=2969s
- Acquisitions Anonymous, 25:54 — Working Capital Adjustment : https://www.youtube.com/watch?v=mfhX-LiOfmI&t=1554s
- BiggerPockets #799, 21:45 — 3 Simple Steps to Seller Financing : https://www.youtube.com/watch?v=ifOTmf12uGw&t=1305s

**Note : 45/100.**

---

## Récapitulatif des fiches

| Fiche | Contenu | Note |
|---|---|---|
| F01 | La Martingale #336, Domaine de Fontenay | 95 |
| F26 | Acquiring Minds, golf Quail Ridge (rachat par le directeur, 0 $ personnel) | 90 |
| F02 | Corpus « Ça fait un bail ! », Fontenay | 85 |
| F04 | Hospitality Insiders #183, Fontenay | 85 |
| F08 | GDIY #525, Joseph Lasserre (reprises de PME du BTP) | 85 |
| F13 | Acquired, LVMH (Boussac 1984) | 85 |
| F03 | Richissime #120, Fontenay | 80 |
| F05 | Documentaire Fontenay | 80 |
| F17 | La Martingale #311, Monolithe (hôtellerie murs et fonds) | 80 |
| F20 | BUILD, Adrien Gloaguen (Touriste) | 80 |
| F09 | Bpifrance : financer une reprise | 75 |
| F18 | Extendam | 70 |
| F19 | Kapi Club, Yohann Benhamou | 70 |
| F28 | BiggerPockets, Walker Deibel | 70 |
| F29 | BiggerPockets Rookie 375, motel | 70 |
| F30 | Chip Conley, Phoenix Hotel | 70 |
| F06 | Sans Pression, Nicolas Tommasini | 65 |
| F10 | Search funds | 65 |
| F12 | Rachat d'entreprises en difficulté | 65 |
| F21 | Banque des Territoires | 65 |
| F22 | La Vie, petits hôtels de campagne | 65 |
| F11 | Corpus FR « sans apport » | 60 |
| F14 | La Martingale × Fundora (LBO) | 60 |
| F15 | Family offices FR | 60 |
| F24 | Outils de financement du foncier | 60 |
| F27 | Galindo (échec) | 60 |
| F07 | La Martingale #95, monuments historiques | 55 |
| F23 | Anguelov et Nardecchia | 55 |
| F25 | Campings | 55 |
| F16 | Sébastien Bazin, Accor | 50 |
| F31 | Corpus anglophone « no money down » | 45 |
