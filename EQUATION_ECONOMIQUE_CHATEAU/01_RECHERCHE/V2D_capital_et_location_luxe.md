# V2D — Libérer du capital et louer sans perdre la propriété : opérations MH, copropriétés, location de luxe

Agent : V2D (vague 2). Démarré le 2026-10-14. Fichier écrit au fur et à mesure.
Sources : `01_RECHERCHE/sources/sources_V2D.csv` (identifiants [V2D-xx]).

Statuts : PAGE LUE (page ouverte avec WebFetch, citation exacte) / EXTRAIT (vu dans un résultat de recherche) / ESTIMATION / HYPOTHÈSE / INCONNU.

Contexte repris sans le refaire :
- R3 Q1 : régime MH (art. 156 et 156 bis CGI), engagement de conservation de 15 ans, détention directe, copropriété autorisée depuis 2018 si l'habitation représente au moins 75 % des surfaces [R3-06] ; taux de déduction selon la situation [R3-02].
- R3 § 5.5 : seuils micro-BIC 2026 des meublés de tourisme (classé 83 600 € / 50 % ; non classé 15 000 € / 30 %) et loi Le Meur.
- R7 § 5.3 : prix Le Collectionist observés (Château Mansart, 16 chambres, 56 230 à 61 850 € par semaine).
- R8 § 6.3 : démembrement, règles civiles (grosses réparations à la charge du nu-propriétaire) ; barème de l'article 669 non lu.

Avertissement : ce document n'est pas un avis juridique ou fiscal. Tout montage cité doit être validé par un notaire, un avocat fiscaliste et un expert-comptable.

## Journal de progression

- 2026-10-14 : squelette créé.

## Q1. Opérations de défiscalisation « Monument historique » : vendre une partie du domaine à un opérateur

### 1.1 Qui sont les opérateurs ?

Un opérateur identifié et vérifié : **Histoire & Patrimoine**, filiale du groupe Altarea.
- Présentation : « Spécialiste de la rénovation et de la réhabilitation de l'immobilier ancien du groupe ALTAREA » [V2D-03] (PAGE LUE). Dispositifs proposés : Monument historique, Malraux, Denormandie, déficit foncier [V2D-03].
- Taille revendiquée : « + de 500 Demeures déjà sauvées de l'oubli », « + de 10 000 logements réhabilités », « + de 1,5 milliard d'euros déjà investis », « + de 30ans d'expérience » [V2D-04] (PAGE LUE ; chiffres déclaratifs de l'opérateur, non audités).
- Société de gestion du groupe : ALTAREA GESTION IMMOBILIERE (HISTOIRE & PATRIMOINE GESTION), SIREN 401165089, code NAF 68.32A, créée le 20/04/1995 ; chiffre d'affaires 2025 publié : **11 347 170 €** ; résultat net 2025 : **−298 458 €** [V2D-10] (PAGE LUE, API officielle). C'est la société de gestion locative des lots.
- **Comptes 2025 publiés des autres sociétés du groupe** (API Recherche d'entreprises, champ « finances », année « 2025 ») [V2D-42] (PAGE LUE) :

| Société | SIREN | Activité (NAF) | Chiffre d'affaires 2025 | Résultat net 2025 |
|---|---|---|---|---|
| HISTOIRE & PATRIMOINE | 480309731 | 41.10A (promotion immobilière) | 13 307 € | −31 598 228 € |
| HISTOIRE & PATRIMOINE PROMOTION | 792751992 | 68.31Z | 14 805 200 € | −18 926 589 € |
| HISTOIRE & PATRIMOINE MANAGEMENT (créée en 2023) | 977624931 | 68.10Z | 29 057 956 € | −25 964 960 € |
| HISTOIRE & PATRIMOINE VAUBAN | 490743101 | 68.10Z | 2 579 213 € | −2 413 501 € |
| HISTOIRE & PATRIMOINE MANSART | 825208093 | 68.10Z | 449 183 € | −4 319 155 € |
| HISTOIRE & PATRIMOINE GUIMARD | 788652568 | 68.10Z | 586 175 € | −2 167 851 € |
| HISTOIRE & PATRIMOINE VIOLLET-LE-DUC | 803307354 | 68.10Z | 21 250 € | −238 633 € |

  Total des résultats nets de ces sept sociétés et de la société de gestion : environ **−86 M€** en 2025 (ESTIMATION, simple somme ; des flux internes au groupe, des provisions ou des dépréciations peuvent expliquer une partie des pertes, et la consolidation n'est pas connue). **Lecture prudente** : l'opérateur leader vérifié a publié de lourdes pertes en 2025. Son appétit pour de nouvelles acquisitions, et donc la possibilité de lui vendre des dépendances, n'est pas acquis. Les causes sont INCONNUES ; il faudrait lire le document d'enregistrement universel 2025 d'Altarea.
- Un lien « Proposer un bâtiment » renvoie vers altarea-partenaires.com [V2D-03]. Cette page ne donne **aucun critère** d'achat (type de bien, surface, localisation, prix) : c'est un portail pour les partenaires commerciaux (conseillers en gestion de patrimoine), joignable par courriel [V2D-11] (PAGE LUE). Les critères d'acquisition de l'opérateur restent INCONNUS.
- Autre diffuseur vu : Euodia, site de conseil en défiscalisation, qui commercialise un programme au « Château de Chassagny » à Montagny (Rhône) : T1 « à partir de 84 800 € », T2 « à partir de 129 500 € », livraison « 4ème trimestre 2024 » ; l'opérateur et le vendeur du château ne sont pas nommés ; la page mélange « Monument Historique » et « loi Malraux » [V2D-01] (PAGE LUE, fiabilité faible).
- D'autres opérateurs existent sans doute (le marché MH est animé par des promoteurs et des réseaux de conseillers), mais je n'en ai pas vérifié d'autre : INCONNU au-delà d'Histoire & Patrimoine.

### 1.2 Quels biens les opérateurs achètent-ils ? Typologie observée (octobre 2026)

Les 12 programmes en vente chez Histoire & Patrimoine [V2D-07] (PAGE LUE) sont surtout des **bâtiments urbains ou périurbains** : Hôtel-Dieu (Dourdan, Clermont-Ferrand, Blois), couvent (Melun), séminaire (Sommervieu), îlots urbains (Rodez, Troyes, Avignon, Carcassonne). Seuls trois sont des « domaines » ou « châteaux » :

| Programme | Lieu | Nature | Logements | Dispositif | Prix d'entrée | Structure du simulateur | Statut |
|---|---|---|---|---|---|---|---|
| Domaine de Wendel | Hayange (Moselle), « À 30 min de Luxembourg » | ancien siège industriel (bureaux de 1892, aile de 1926) | 125, « du studio au 4 pièces » | MH + déficit foncier | « Dès 305 700 € » | travaux 78 % (195 000 €) / foncier 22 % (55 000 €), déduction « sur la durée des travaux (maximum 4 ans) » | PAGE LUE [V2D-05] |
| Château Bon Air | Mérignac, « à 10 minutes de Bordeaux » | « Prestigieux château du 18ème siècle » | « 15 appartement » | **déficit foncier** (pas MH) | « Dès 387 800 € » | travaux 87 % (217 500 €) / foncier 13 % (32 500 €) ; total 250 000 €, différent du prix d'entrée (non expliqué) | PAGE LUE [V2D-09] |
| Domaine Motte-Cordonnier | Armentières (Nord) | domaine (nature non précisée) | INCONNU | INCONNU | « 255 100 € » | INCONNU | PAGE LUE (liste) [V2D-07] |

Exemple livré : **Manoir de la Paclais**, Saint-Herblain, « à 10 kilomètres en voiture du centre-ville de Nantes » : manoir du XVe siècle « inscrit à l'inventaire des Monuments Historiques », « au cœur d'un parc boisé », transformé en « 7 appartements » du T1 au T4, « Rehabilité en 2026 » ; jardins, parterres et allées restaurés ; vendeur, prix et montant des travaux non publiés [V2D-08] (PAGE LUE).

**Lecture** (ESTIMATION) : les exemples vérifiés sont tous **à 10-30 minutes d'une métropole** (Nantes, Bordeaux, Luxembourg) ou en ville. La logique du montage l'explique : l'investisseur loue son lot pour transformer les travaux en déficit foncier imputable sur son revenu global (voir 1.4). Il faut donc un marché locatif. La page de Wendel met en avant un « Marché locatif tendu » [V2D-05]. Un château isolé à la campagne, loin d'un bassin d'emploi, est a priori peu adapté. Je n'ai **aucune preuve** qu'un opérateur achète des dépendances de château en zone rurale isolée : INCONNU.

Deuxième opérateur vérifié : **Buildinvest**. Communiqué de presse de 2020 (agence Galivel) [V2D-13] (PAGE LUE, PDF converti localement) : « Spécialiste de la rénovation lourde de biens immobiliers depuis 50 ans » ; groupe familial de « 350 salariés » ; « 4.500 logements rénovés sur près de 350.000 m² » en cumul. Trois programmes MH cités en 2020, tous urbains :
- Pont-Audemer (Eure), « une maison cœur de ville du XVIème siècle de 105 m² » : « Le budget global est de 397.000 € (150.000 € de foncier + 247.000 € de travaux) ». Soit (ESTIMATION, calcul) 3 781 €/m² au total, dont 1 429 €/m² de foncier et 2 352 €/m² de travaux ; **foncier 38 %, travaux 62 %**.
- Caen, Résidence de la Visitation (ancien couvent et caserne de cavalerie) : « 37 appartements (du T1 au T5) et les 34 parkings », prix « de 165.000 € à 440.000 € (foncier + travaux + parking) ».
- Châtellerault, Résidence Sully (hôtel particulier du XVIe) : « 18 logements dont les prix iront de 105.000 € à 245.000 € (foncier + travaux) ».
- Le BODACC ne montre aucune procédure collective pour BUILDINVEST S.A./SAS (SIREN 330434531) : 70 annonces au nom « BUILDINVEST » (dépôts de comptes, modifications, cessions), aucune de la famille « procédures collectives » [V2D-14] (PAGE LUE, API ouverte).

### 1.3 Prix de vente au m² et part foncier / travaux : ce que l'on sait

| Programme | Prix total | Foncier | Travaux | Part foncier | Statut | Source |
|---|---|---|---|---|---|---|
| Pont-Audemer, maison XVIe, 105 m² (2020) | 397 000 € (3 781 €/m²) | 150 000 € | 247 000 € | 38 % | PAGE LUE (calcul au m² : ESTIMATION) | [V2D-13] |
| Domaine de Wendel (simulateur indicatif) | 250 000 € | 55 000 € | 195 000 € | 22 % | PAGE LUE | [V2D-05] |
| Château Bon Air (simulateur, déficit foncier) | 250 000 € | 32 500 € | 217 500 € | 13 % | PAGE LUE | [V2D-09] |
| Page générique MH (simulateur) | 250 000 € | 50 000 € | 200 000 € | 20 % | PAGE LUE | [V2D-06] |
| Annonce d'appartement dans un château divisé (vue en résultat de recherche, page inaccessible) | 718 900 € | 174 600 € | 544 300 € | 24 % | EXTRAIT (Leggett, page protégée, non ouverte ; à vérifier) | [V2D-15] |

**Lecture** (ESTIMATION) : dans les exemples vérifiés, le **foncier représente 13 à 38 % du prix payé par l'investisseur**, les travaux 62 à 87 %. Le « foncier » vendu à l'investisseur inclut la marge et les frais de l'opérateur ; ce n'est **pas** le prix payé au propriétaire initial. Le prix au m² global (foncier + travaux) n'est vérifié que pour un seul bien (3 781 €/m² en 2020, Pont-Audemer) : **aucune moyenne fiable**.

**Prix d'achat du bâtiment par l'opérateur au propriétaire d'origine** : **INCONNU**. Aucune des pages lues ne le publie. Méthode pour vérifier : rechercher la mutation dans DVF (valeurs foncières, data.gouv.fr) à partir des parcelles cadastrales du monument (base Mérimée), ou dans les actes publiés au service de la publicité foncière.

### 1.4 Règles fiscales pour l'investisseur, rappelées par la doctrine (complément à R3 Q1)

Doctrine BOFiP BOI-RFPI-SPEC-30-30 [V2D-16] (PAGE LUE, relecture ciblée de la source [R3-06]) :
- Définition : « La division consiste à répartir par lots la propriété d'un immeuble entre plusieurs personnes », chaque lot comprenant « une partie privative et une quote-part de parties communes » (§ 480).
- Principe : le régime « n'est pas ouvert aux immeubles ayant fait l'objet d'une division à compter du 1er janvier 2009 » (§ 460).
- Exceptions : divisions de 2009 à 2017 avec agrément ministériel (§ 490-510) ; depuis le 1er janvier 2018, plus d'agrément, mais l'immeuble doit être « affecté à l'habitation pour au moins 75 % de ses surfaces habitables » (§ 490, § 520). Les immeubles seulement labellisés par la Fondation du patrimoine sont exclus de cette exception (§ 530).
- **Les locaux commerciaux ou professionnels ne comptent pas comme habitation** : sont exclus du numérateur « les immeubles ou fractions d'immeubles destinés à une exploitation à caractère commercial ou professionnel » (§ 540).
- Délai : la condition doit être remplie « au plus tard dans les deux ans qui suivent la date de la division » (§ 550). La page ne dit pas pendant combien de temps elle doit être maintenue ensuite : INCONNU.
- Conservation : « les copropriétaires doivent prendre l'engagement de conserver la propriété de leur quote-part de l'immeuble » pendant « au moins quinze années à compter de leur acquisition » (§ 500). En cas de rupture, le revenu de l'année et des deux suivantes est majoré du tiers des charges indûment déduites (§ 560, renvoi au § 100).

Ce que disent les opérateurs (PAGE LUE, sources commerciales) :
- Pas d'obligation de louer : « Pas de contraintes, donc, dans ce dispositif, liées à un engagement de location ou à des plafonds de loyers ou de revenus. Le propriétaire peut occuper le bien ou le louer » [V2D-13]. Mais R3 [R3-02] montre que, si le lot ne procure aucune recette, les travaux non subventionnés ne sont déductibles qu'à 50 % lorsque l'immeuble est fermé au public, et que l'excédent ne crée pas de déficit reportable. **En pratique, l'avantage complet suppose de louer le lot** (déficit foncier imputable sans limite sur le revenu global). ESTIMATION fondée sur [R3-02].
- Hors plafonnement des niches fiscales : « L'avantage fiscal MH n'entre pas dans le plafond des niches fiscales de 10.000 € /an » [V2D-13] ; « Déplafonnement de l'avantage fiscal » [V2D-06].
- Cible : contribuables à « TMI » de 41 % ou 45 % [V2D-06] ; « taux marginal d'imposition supérieur à 30 % » selon [V2D-13].
- Report de l'excédent : « neuf années consécutives » selon l'opérateur [V2D-12] ; « 6 années suivantes » selon [V2D-13] ; la doctrine dit « des six années suivantes inclusivement » [R3-02]. **Divergence** : je retiens la doctrine (6 ans).

### 1.5 Le cadre a changé en 2017, et cela a fait débat

Question écrite n° 43918 de Brigitte Kuster (AN, JO du 1er février 2022, p. 588) [V2D-17] (PAGE LUE, PDF) : elle alerte sur « la suppression en décembre 2017 d'un agrément préalable du Gouvernement pour la mise en société civile ou la mise en copropriété d'immeubles historiques », qui « favorise la défiscalisation des travaux de lotissement des monuments historiques ». Exemple cité : le domaine de Grignon (Yvelines), « son château Louis XIII, ses dépendances et ses deux cent soixante hectares de terres agricoles et de bois », qui « ont failli faire l'objet d'une cession de l'État au profit d'un promoteur immobilier », pour le « transformer en résidences et lieux de séminaires », avec un changement du PLU « auquel la commune s'opposait ». Elle demande de « réintroduire ces agréments préalables ». La question a été **retirée le 21 juin 2022 (fin de mandat), sans réponse**.

**Lecture** (ESTIMATION) : le lotissement d'un domaine historique par un promoteur est **juridiquement possible** depuis 2018, mais il est **politiquement sensible** et dépend du PLU (accord de la commune) et de l'architecte des Bâtiments de France. C'est un risque de réputation et de délai.

### 1.6 Prix payé par un opérateur au propriétaire : une piste DVF non concluante

Méthode testée : les valeurs foncières publiques (DVF, fichiers « geo-dvf » de data.gouv.fr) de Saint-Herblain (INSEE 44162), années 2021 à 2025 [V2D-18] (fichiers lus) :
- le 19/02/2021, une vente de **930 000 €** au lieu-dit « LA PACLAIS », parcelles DZ 1 et DZ 2 : une « Maison » de **308 m²** de surface bâtie (9 pièces) et environ 2,7 ha de terrains (prés, terrains d'agrément, sols) ;
- le 30/08/2021, une vente de 998 950 € sur des parcelles voisines (DZ 9 à 21 ; taillis, eaux, terrains d'agrément, deux petites maisons de 65 m² et des locaux d'activité) ;
- aucune revente de lots d'appartements n'apparaît ensuite sur la section DZ entre 2022 et 2025.

**Je ne peux pas affirmer** que la vente de 930 000 € est celle du Manoir de la Paclais à l'opérateur : DVF ne donne ni le nom de l'acheteur ni celui du monument, et je n'ai pas pu lire les parcelles cadastrales du monument (base Mérimée : portail en JavaScript, connexion coupée vers data.gouv.fr). Statut : **INCONNU** pour l'attribution. Si l'attribution se confirmait, cela ferait environ 3 000 €/m² bâti, parc compris (ESTIMATION conditionnelle). Pour vérifier : relever les parcelles du manoir dans Mérimée (POP), puis demander l'acte au service de la publicité foncière.

### 1.7 Un propriétaire peut-il vendre ses dépendances à une telle opération et garder le château ?

Je n'ai trouvé **aucun exemple publié** d'un propriétaire privé qui vend ses communs ou ses écuries à un opérateur MH tout en gardant et en habitant le château. Statut : INCONNU (deux recherches ciblées, plus la revue des programmes et réalisations d'Histoire & Patrimoine [V2D-07], [V2D-08] et des programmes de Buildinvest [V2D-13]).

Ce que les règles impliquent (ESTIMATION, à valider par un notaire et un fiscaliste) :
1. **Si les dépendances forment un bâtiment distinct**, détaché par division cadastrale et vendu entier à l'opérateur, puis divisé en appartements, la condition des 75 % d'habitation ne porte a priori que sur ce bâtiment [V2D-16 § 480-550]. Un programme de logements la remplit facilement. Le château n'est pas divisé. Mais la notion d'« immeuble » doit être confirmée quand la protection MH couvre l'ensemble (château et communs).
2. **Si le château et les dépendances sont mis en copropriété ensemble**, le propriétaire devient copropriétaire avec 7 à 125 investisseurs (nombre de logements des programmes observés [V2D-08], [V2D-05]). Les locaux commerciaux, comme une salle de réception ou un hôtel exploités au château, **ne comptent pas comme habitation** [V2D-16 § 540]. Une activité commerciale importante peut donc faire échouer la condition des 75 %, et **tous les copropriétaires** perdraient alors le régime MH. Ce montage est incompatible avec un modèle événementiel lourd.
3. **Effets sur le domaine** : voisins permanents (locataires des investisseurs), accès et stationnement, servitudes de passage et de réseaux, charges communes du parc, gouvernance (syndicat de copropriétaires ou association syndicale libre, ASL ; montage cité par l'extrait de recherche [V2D-15], non vérifié), engagements de 15 ans de chaque investisseur. Pour un propriétaire qui veut une partie « entièrement privée » et des chevaux au calme, c'est un **coût de tranquillité élevé**. Les programmes observés comptent entre 7 et 125 logements ; un programme de 7 à 15 logements dans des communs de 600 à 2 500 m² est plausible en surface (HYPOTHÈSE de 50 à 80 m² par logement, non vérifiée).
4. **Urbanisme** : changement de destination de bâtiments agricoles ou d'écuries en logements, avis de l'architecte des Bâtiments de France, PLU. Le cas de Grignon montre qu'une commune peut s'y opposer [V2D-17].
5. **Capital libéré pour le propriétaire** : le prix payé par l'opérateur pour le bâtiment existant est INCONNU (§ 1.3, § 1.6). On sait seulement que la part « foncier » payée par l'investisseur final, marge de l'opérateur comprise, représente 13 à 38 % de son prix total [V2D-05], [V2D-09], [V2D-13]. Le propriétaire touche moins que cette part foncier.

## Q2. Loi Malraux et label de la Fondation du patrimoine : utiles à ce montage ?

- Malraux : la réduction d'impôt peut atteindre « 30% du montant des travaux engagés sur un bien éligible », pour des « bâtiments anciens situés dans un site patrimonial remarquable (SPR) » [V2D-12] (PAGE LUE, source d'opérateur). Un domaine rural de plus de 50 ha est rarement situé dans un SPR (ESTIMATION). Dispositif **marginal pour ce projet**. Ses autres règles (plafond, engagement de location) n'ont pas été vérifiées ici, faute d'utilité.
- Label de la Fondation du patrimoine : traité par R3 (§ 1.4). Point nouveau : les immeubles seulement labellisés sont **exclus** de l'exception « 75 % d'habitation » pour les divisions [V2D-16 § 530]. Un château non protégé (scénario S1) ne peut donc pas être divisé en lots défiscalisés sous ce régime.

## Q3. Démembrement de propriété : vendre la nue-propriété, ou céder un usufruit temporaire

### 3.1 Barème fiscal (article 669 du CGI)

Doctrine BOFiP BOI-ENR-DMTG-10-40-10-50, en vigueur depuis le 23/12/2013 [V2D-19] (PAGE LUE), § 30 :

| Âge de l'usufruitier (révolu) | Usufruit | Nue-propriété |
|---|---|---|
| moins de 21 ans | 90 % | 10 % |
| moins de 31 ans | **80 %** | **20 %** |
| moins de 41 ans | 70 % | 30 % |
| moins de 51 ans | 60 % | 40 % |
| moins de 61 ans | 50 % | 50 % |
| moins de 71 ans | 40 % | 60 % |
| moins de 81 ans | 30 % | 70 % |
| moins de 91 ans | 20 % | 80 % |
| 91 ans et plus | 10 % | 90 % |

- Usufruit à durée fixe (§ 70) : « 23 % de la valeur de la propriété entière pour chaque période de dix ans », « sans fraction et sans égard à l'âge de l'usufruitier ». Un usufruit accordé à une personne morale ne peut dépasser 30 ans, soit 69 % au plus (§ 80).
- Portée : le barème sert « pour la liquidation des droits d'enregistrement et de la taxe de publicité foncière » [V2D-19]. **Ce n'est pas un prix de marché.** Dans une vente, le prix de la nue-propriété se négocie ; aucun prix de marché pour des châteaux n'a été trouvé (voir 3.4).

### 3.2 Application au propriétaire de 26 ans (ESTIMATION, calcul sur le barème)

**Option A — vendre la nue-propriété et garder l'usufruit à vie.**
- Valeur fiscale de la nue-propriété : **20 %** de la pleine propriété.
- L'investisseur attendrait environ 50 à 60 ans pour récupérer le bien, selon l'espérance de vie (HYPOTHÈSE). Un investisseur rationnel paierait sans doute **moins** que 20 %, car il supporterait en plus le risque d'entretien et l'absence de revenu (ESTIMATION).
- Exemple : pour un château évalué 5 M€, environ 1 M€ au mieux, contre une perte définitive de la propriété pour les héritiers.
- IFI : en cas de vente à une personne qui n'est ni héritier présomptif ni donataire, l'usufruitier n'est plus imposé sur la pleine propriété. Les deux parties sont imposées selon l'article 669 (§ 160-170) [V2D-20] (PAGE LUE). Le propriétaire de 26 ans resterait imposé sur **80 %** de la valeur. **Gain d'IFI faible.**

**Option B — garder la propriété et céder un usufruit temporaire** d'une partie du domaine (par exemple les communs, un pavillon, une aile) à un exploitant ou à un investisseur pendant 10 à 30 ans.
- Valeur fiscale : 23 % par période de dix ans (§ 70) [V2D-19]. Exemples : 23 % pour 10 ans, 46 % pour 11 à 20 ans, 69 % pour 21 à 30 ans.
- À la fin, la pleine propriété revient au propriétaire, sans indemnité. C'est le seul sens du démembrement **compatible avec « garder la propriété »**.
- **Fiscalité lourde** : le prix de la première cession d'un usufruit temporaire, réalisée depuis le 14 novembre 2012, est imposé comme un **revenu** de l'année d'encaissement, dans la catégorie des revenus que produit le bien : revenus fonciers pour un bien loué nu, BIC pour un bien meublé, revenus fonciers par défaut pour un immeuble (§ 1, § 130-140, § 220) [V2D-21] (PAGE LUE). S'y ajoutent les prélèvements sociaux (§ 230) et la contribution sur les hauts revenus (§ 240).
- Conséquence (ESTIMATION) : pour une personne physique, l'essentiel du capital libéré serait taxé au barème de l'impôt sur le revenu l'année de la vente. Un capital de 1 M€ pourrait ainsi perdre près de la moitié de sa valeur en impôts. Cette fraction n'a pas été calculée finement ; le calcul est à confier à un fiscaliste.
- Le même texte exclut de cette règle les cédants soumis à l'IS (§ 20). Une société à l'IS qui céderait un usufruit temporaire relèverait d'autres règles, non vérifiées ici : INCONNU.

### 3.3 Qui paie le gros entretien ?

Rappel de R8 [R8-44] : « Les grosses réparations sont à la charge du nu-propriétaire sauf si elles résultent du manque d'entretien », et pour un immeuble elles « ne concernent que le gros-œuvre ».
- **Option A** : le gros œuvre passerait à l'investisseur nu-propriétaire. C'est séduisant pour un château, mais l'investisseur l'intégrerait dans son prix (ESTIMATION).
- **Option B** : le propriétaire, qui garde la nue-propriété, reste chargé du gros œuvre des parties démembrées.
- Je n'ai pas vérifié si le nu-propriétaire peut être **contraint** d'exécuter les grosses réparations, ni comment une convention peut répartir autrement les charges. À VALIDER par un notaire.

### 3.4 Le marché existe-t-il pour des châteaux ?

Voir 3.5 (résultat de la recherche ciblée).

### 3.5 Le marché existe-t-il pour des châteaux ? (résultat)

- Recherche ciblée (viager, nue-propriété, château) : les résultats ne décrivent que le mécanisme général du viager et de la nue-propriété pour des logements ordinaires, avec une « décote de l'ordre de 30 % en moyenne » [V2D-30] (EXTRAIT). **Aucun exemple** de château vendu en nue-propriété à un investisseur, ni d'investisseur institutionnel acheteur de nues-propriétés de châteaux. R8 était arrivé au même constat [R8 § 6.3].
- Le seul marché institutionnel du démembrement que confirme la doctrine est l'**usufruit locatif social** : des bailleurs sociaux détiennent l'usufruit de logements (CCH L.253-1 à L.253-8), cité dans [V2D-21 § 20]. Il porte sur des logements sociaux, pas sur des demeures historiques.
- Conclusion : **marché non démontré pour un château. Statut : INCONNU**, avec une présomption défavorable. Pour un propriétaire de 26 ans, vendre la nue-propriété libérerait au plus de l'ordre de 20 % de la valeur (barème) et ferait perdre définitivement le bien aux héritiers. Céder un usufruit temporaire d'une partie du domaine est juridiquement possible, mais le prix est taxé comme un revenu (§ 3.2). Aucun exemple réel trouvé.

## Q4. Location de luxe à la semaine de la partie privée pendant les absences du propriétaire

### 4.1 Tarifs observés pour des châteaux de 8 à 16 chambres (Le Collectionist, octobre 2026)

Complément aux prix de R7 § 5.3 [R7-54]. Prix pour 7 nuits, « Taxe de séjour non incluse ». Le site ne précise pas le régime de TVA. La part reversée au propriétaire n'est pas publiée.

| Propriété (région) | Chambres / salles de bains | Voyageurs | Surface | Prix par semaine | Inclus | Statut | Source |
|---|---|---|---|---|---|---|---|
| Château Montravel (environs de Bordeaux) | 8 / 7 | 15 | 800 m² | 15 570 € (basse saison), 21 050 € (début d'été, début d'automne), 29 335 € (environ 10 juillet au 21 août) | « Gardien », ménage « 3x/semaine », concierge ; chef et personnel en plus | PAGE LUE | [V2D-35] |
| Château Renaissance (Dordogne) | 9 / 9 | 20 | 720 m² | 12 755 € (octobre) à 15 045 € (autres semaines disponibles) ; prix d'été non affichés | ménage 3 fois par semaine, concierge ; chef en plus | PAGE LUE | [V2D-36] |
| Château de la Belle (Dordogne) | 11 / 9 | 22 | 1 850 m² | 35 265 € (15-22 octobre 2026) à 46 860 € (juillet-août) | préparation du petit-déjeuner, ménage 2 fois par semaine, concierge ; chef et personnel en plus | PAGE LUE | [V2D-37] |
| Château Hippolyte (environs de Bordeaux) | 14 / 14 | 33 | 945 m² | 36 615 € (même prix sur toutes les semaines affichées) | ménage « 7x/semaine », concierge ; chef et personnel en plus | PAGE LUE | [V2D-38] |
| Château Mansart (Calvados), rappel R7 | 16 | 40 | — | 56 230 à 61 850 € | — | PAGE LUE | [R7-54] |

Autres plateformes :
- **Oliver's Travels** : six châteaux mis en avant en France, pour 10 à 20 personnes ; les prix ne sont pas affichés sur la page [V2D-29] (PAGE LUE).
- **Abercrombie & Kent Villas et Airbnb Luxe** : non vérifiés (voir 4.2).

### 4.2 Commission des plateformes

| Plateforme | Commission | Année | Statut | Source |
|---|---|---|---|---|
| Le Collectionist | « The platform takes a 20% commission on the rentals » ; le prix « includes basic services, including housekeeping and gardeners, provided by the property owners » | 2017 | PAGE LUE | [V2D-24] |
| Le Collectionist | « The company takes a 22% commission from the rental » | 2020 | PAGE LUE | [V2D-25] |
| Le Collectionist (page propriétaires 2026) | non publiée | 2026 | PAGE LUE (absence) | [V2D-23] |
| Oliver's Travels | « We operate purely on commission » ; « There's no fee to join » ; taux non publié | 2026 | PAGE LUE | [V2D-28] |
| Airbnb (offre standard) | « Most hosts pay 15.5% » (frais payés par l'hôte seul) ; « Most hosts pay a 3% service fee » quand les frais sont partagés avec le voyageur | 2026 | PAGE LUE | [V2D-31] |
| Airbnb Luxe | INCONNU (la page des frais n'en parle pas) | — | INCONNU | [V2D-31] |
| Abercrombie & Kent Villas | INCONNU | — | INCONNU | — |

**Point important** : chez Le Collectionist, c'est le **propriétaire** qui fournit et paie les services de base compris dans le prix (ménage, jardiniers) [V2D-24]. Les fiches de 2026 confirment que le ménage (2 à 7 fois par semaine), un gardien ou la préparation du petit-déjeuner sont inclus dans le prix affiché [V2D-35] à [V2D-38]. La conciergerie est en partie assurée par la plateforme, et la conciergerie supplémentaire est facturée au client : « plus an extra €5,000 for concierge service » en moyenne en 2020 [V2D-25].

Comptes de Le Collectionist : société LE COLLECTIONIST, SIREN 789370152, créée le 12/11/2012 ; **finances non publiées** dans l'API (comptes probablement confidentiels) [V2D-27]. INCONNU.

### 4.3 Nombre de semaines réellement louées

**Aucun témoignage ni rapport** donnant le nombre de semaines louées par an pour un château n'a été trouvé, malgré une recherche ciblée [V2D-39] (EXTRAIT : les résultats ne portent que sur l'achat, l'entretien et les événements). **INCONNU.**

Deux indications indirectes :

1. **Moyennes de Le Collectionist** (ESTIMATION, calcul sur des données de presse) : « 160 millions d'euros de volume brut de réservations (GBV) » prévus pour 2024, « plus de 3 000 propriétés », « environ 5 000 réservations sur l'exercice 2023 » [V2D-26] (PAGE LUE).
   - Cela donne environ 53 000 € de réservations par propriété et par an, et 1,7 à 2 réservations par propriété et par an, si l'on retient 2 300 à 3 000 propriétés.
   - Avec un séjour moyen d'environ « 25,000 a week » [V2D-25] ou « €26,000 on average for a 10 night stay » [V2D-24], la propriété moyenne serait louée **environ 2 semaines par an**.
   - Limites : les années ne coïncident pas (2023, 2024, 2025), et beaucoup de propriétés sont des résidences secondaires que leurs propriétaires n'ouvrent que quelques semaines.
   - **Ce n'est pas un taux d'occupation**, mais cela montre que l'hypothèse de 8 à 12 semaines retenue par R7 [R7 § 5.3] est **très au-dessus de la moyenne de la plateforme**.
   - Autres ordres de grandeur par maison, tirés des acquisitions de la plateforme : Vallat (France) « 3,9 millions d'euros de GBV » pour « 90 maisons », soit environ 43 000 € par maison ; Bramble Ski (Suisse) « 24,2 millions d'euros » pour « 142 maisons », soit environ 170 000 € ; The Greek Villas « 7 millions d'euros » pour « 400 maisons », soit environ 17 500 € [V2D-26] (calculs : ESTIMATION).
2. **Études de cas d'Oliver's Travels** pour des maisons de 4 à 6 chambres : occupation « typically » d'environ 62 à 80 %, par exemple Dordogne (4 chambres) environ 65 % pour 4 300 £ par semaine, Provence (4 chambres) environ 70 % pour 7 300 £, Côte d'Azur (4 chambres) environ 76 % pour 9 200 £ [V2D-28] (PAGE LUE).
   - Le dénominateur n'est pas défini. C'est probablement la part des semaines ouvertes à la location (ESTIMATION).
   - Ces données de communication commerciale portent sur de petites maisons, pas sur des châteaux de 8 à 16 chambres, dont la clientèle est beaucoup plus étroite (groupes de 15 à 40 personnes).

**HYPOTHÈSE de travail proposée pour le modèle** : 2 à 6 semaines louées par an pour un château de 10 à 15 chambres ouvert surtout l'été. Elle s'appuie sur la moyenne de la plateforme (environ 2) et sur une part d'occupation de 60 à 70 % des semaines d'été ouvertes (6 à 8 semaines). Elle est à confirmer par des propriétaires ou des agences ; ce n'est pas un fait.

### 4.4 Exigences (piscine, salles de bains, conciergerie)

- **Piscine** : les 9 châteaux ou domaines de Dordogne et les 6 des environs de Bordeaux proposés par Le Collectionist ont **tous** une piscine (extérieure, chauffée, à débordement ou naturelle) [V2D-40], [V2D-41] (PAGE LUE).
- **Salles de bains** : environ une par chambre, de 0,75 à 1 salle de bains par chambre. Exemples : Château de la Belle, 11 chambres et 9 salles de bains ; Domaine Aglaé, 12 et 11 ; Château Hippolyte, 14 et 14 [V2D-40], [V2D-41].
- **Services inclus** : ménage plusieurs fois par semaine, concierge, gardien selon le cas ; chef et personnel de maison en supplément [V2D-35] à [V2D-38].
- **Disponibilité** : Oliver's Travels exige, pour la France et l'Italie, « a minimum of 6 weeks of availability in July and August » (formulation reprise du résumé de la page), une assurance de responsabilité civile d'au moins 2 millions de livres et le haut débit. Le propriétaire peut habiter le bien une partie de l'année si ces minimums sont respectés [V2D-28] (PAGE LUE).
- **Sélectivité** : Le Collectionist retient environ 10 biens sur 100 demandes de propriétaires selon son dirigeant en 2020 [V2D-25].
- **Cohabitation** : une fiche (Château Montravel) précise que « L'employé de maison réside sur la propriété dans un logement indépendant » et que « L'intimité des hôtes est néanmoins garantie » [V2D-35]. Une présence permanente sur le domaine, dans un logement séparé, est donc compatible avec ce marché. Je n'ai trouvé **aucune fiche** où le propriétaire habite une aile du château loué : INCONNU.
- **Conséquence pour le projet** (ESTIMATION) : louer la **partie privée** suppose que le propriétaire la quitte entièrement pendant les semaines louées, et que ses chevaux et son personnel restent discrets. La période la plus demandée (juillet-août) est aussi celle des concours et de la vie privée estivale. Louer un bâtiment séparé (pavillon, aile autonome, communs rénovés) aux standards observés (piscine, une salle de bains par chambre) est plus cohérent avec la vie privée, mais demande un investissement.

### 4.5 Fiscalité et règles pour un particulier

Rappel de R3 § 5.5 [R3-31] [R3-33] [R3-36] : micro-BIC 2026 limité à 83 600 € de recettes avec un abattement de 50 % pour un meublé de tourisme classé, et à 15 000 € avec 30 % pour un meublé non classé. Au-delà, régime réel. LMP si les recettes du foyer dépassent 23 000 € et les autres revenus d'activité. Cotisations sociales au-delà de 23 000 € de recettes de courte durée.

Points nouveaux [V2D-32] (PAGE LUE, fiche F33175 « Vérifié le 21 mai 2026 ») :
- Une résidence principale est un « Logement occupé au moins 8 mois par an ». Le propriétaire qui y vit ne peut donc pas la louer plus de 4 mois environ.
- Dans les communes qui l'imposent, la durée de location de la résidence principale « varie entre 90 et 120 jours par année civile ». Dépasser la limite expose à « une amende civile de 10 000 € ». Le défaut de déclaration est puni d'une amende civile « pouvant aller jusqu'à 5 000 € ».
- Immatriculation obligatoire au répertoire Sirene (numéro SIRET, gratuit).
- Application au projet (ESTIMATION) :
  - 4 semaines louées à 35 000 € rapportent 140 000 € de recettes, ce qui dépasse le plafond du micro-BIC. Il faut donc passer au régime réel, avec amortissement possible et déficit imputable seulement sur les revenus de location meublée [R3-36].
  - Ces recettes, si elles dépassent les autres revenus d'activité du foyer, font basculer le propriétaire en **LMP**, avec des cotisations sociales.
  - Le seuil de franchise de TVA et l'option des services para-hôteliers sont à examiner (R3 § 6).
- **Interaction avec le régime MH** (À VALIDER) : la doctrine exclut du régime les parties d'immeuble utilisées « pour les besoins d'une entreprise industrielle, commerciale » [R3-04 § 40]. La location meublée relève des BIC. Je ne sais pas si quelques semaines de location meublée de la partie privée suffisent à faire sortir cette partie du régime MH ou à changer la règle de déduction (100 %, 75 % ou 50 %). INCONNU, question pour un fiscaliste.
- **Société civile** : si le château est détenu par une SCI, la location meublée saisonnière peut être jugée commerciale. Le notaire Wargny-Lelong écrit : l'objet de la SCI « ne doit pas être commercial – attention notamment à la location en meublé saisonnière, qui peut être considérée comme telle » [V2D-34] (PAGE LUE). Au-delà de 10 % du chiffre d'affaires, la SCI devient passible de l'IS [R3-59].

## Q5. Copropriété ou partage d'un château entre plusieurs familles

### 5.1 Exemples réels trouvés en France

| Cas | Montage | Chiffres | Gouvernance, difficultés | Statut | Source |
|---|---|---|---|---|---|
| **Château de Panat**, L'Isle-Jourdain (Gers), XIXe siècle | Collectif lié à l'association Alter-Habitat Lislois (créée en 2011), acquisition le 10 septembre 2019 ; « coopérative d'habitants », présentée comme la première du Gers | « 14 logements » sur « 1 500 m² » intérieurs, avec espaces communs ; travaux « 1,5 million d'euros », en partie en auto-réhabilitation ; prix d'achat non publié | Propriété collective, gestion non lucrative, loyers selon les revenus ; le projet a connu « 7 ans de reports et de revirements » avant de se porter sur le château | PAGE LUE | [V2D-43] |
| **Château Monboucher**, à 10 km de Bergerac (Dordogne) | Château divisé en copropriété de 12 logements vendus à des particuliers, avec des pièces communes dans le château | Du « 50 m² » à la maison de « 270 m² » ; prix affichés 640 000 € (appartement) et 960 000 € (maison) ; surfaces incohérentes dans le texte (160 m² et 240 m²) | Salon, salle à manger, cuisine et salle de réception partagés ; concierge pour les jardins ; parcelle privative à louer ; charges et règlement non publiés | PAGE LUE (contenu d'agence, fiabilité faible) | [V2D-44] |
| **Domaine de Courances** (Essonne) | Domaine familial géré par dix cousins copropriétaires (rappel R4) | Environ 1 800 ha (EXTRAIT R4) | Partage de la gestion ; séminaires confiés à un opérateur ; appartements loués dans la ferme (« La Ferme - Les Appartements INSEAD », intitulé du menu du site) | EXTRAIT [R4-89] ; menu du site lu, pages internes en erreur 404 | [R4-89], [V2D-47] |
| **Chenonceau** (rappel R4) | Propriété familiale | — | Conflit familial, administrateur provisoire | voir R4 | [R4-05] |

Modèles commerciaux de « résidence secondaire partagée » (pas des châteaux) : Lazazu propose l'achat à plusieurs de maisons de luxe en France, en Espagne et au Portugal, via une SCI ; « une maison égale 8 parts », entrée « à partir de 250 000 € » ; charges, impôts et travaux au prorata des parts, sauf le ménage ; calendrier d'occupation par saison et algorithme en cas de litige [V2D-33] (PAGE LUE). Je n'ai trouvé **aucun château** proposé dans ce modèle : INCONNU.

### 5.2 Gouvernance : ce que dit un notaire [V2D-34] (PAGE LUE)

- **Indivision** :
  - « Nul ne peut être contraint à demeurer dans l'indivision » ; « Le partage peut toujours être provoqué (article 815 du C.C) ».
  - Décisions importantes à « l'unanimité des indivisaires ».
  - Actes d'administration à « une majorité des 2/3 » (article 815-3).
  - Une convention d'indivision « est par ailleurs conclue pour une durée de 5 années maximum », et « L'unanimité sera nécessaire pour la renouveler ».
- **SCI** :
  - Elle permet « d'acquérir, à plusieurs, un bien immobilier en évitant les inconvénients de l'indivision ».
  - Les clauses d'agrément contrôlent « toute entrée dans le capital ».
  - Le gérant peut recevoir « les pouvoirs les plus larges ».
  - Contreparties : « Les droits des minoritaires sont moins protégés » ; les associés répondent du passif « sans limite de montant », chacun à proportion de sa part.
  - Un associé qui veut sortir peut être bloqué ; si l'agrément est refusé, les associés doivent racheter les parts.
- **Usage** : assemblée générale annuelle, « répartition du temps selon la méthode du « mini-timeshare » », rotation conseillée du gérant.
- **Limite importante pour un château qui loue** : l'objet de la SCI « ne doit pas être commercial – attention notamment à la location en meublé saisonnière, qui peut être considérée comme telle ».

### 5.3 Ce que cela vaut pour le projet (ESTIMATION)

- **Partager la propriété du château entre plusieurs familles** libère du capital (vente de lots ou de parts), mais contredit l'objectif d'une partie « entièrement privée » et d'un domaine calme. Les exemples trouvés ont des **pièces communes partagées** (Monboucher) ou une **vie collective** (Panat).
- Le capital libéré dépend du prix de marché des lots. Le seul repère trouvé est Monboucher, avec des prix affichés de 640 000 € à 960 000 € par logement, sans preuve de vente : INCONNU pour les prix réels. Ces prix pourraient être vérifiés dans DVF après les ventes.
- La forme la plus compatible avec le projet serait la cession de **bâtiments séparés**, communs ou maisons du domaine, avec un règlement strict : accès séparés, servitudes limitées, interdiction des nuisances, pacte de préférence. Mais aucun exemple chiffré n'a été trouvé. Les règles de copropriété (lot du propriétaire, charges du parc) et de l'association syndicale libre sont à faire rédiger par un notaire.
- Si les bâtiments sont protégés MH et que les acheteurs veulent déduire leurs travaux, il faut respecter la règle des 75 % d'habitation [V2D-16] (§ 1.4).

## 6. Autre mécanisme rencontré : la dette participative (financement participatif en obligations)

Château Fontenay (Sarthe), communiqué du 12/12/2023 [V2D-45] (PAGE LUE, source promotionnelle, fiabilité faible) :
- Montage : la société « Sarthe Society SAS » lève « 690.000 € » auprès de particuliers sur la plateforme Bricks.co, « sous forme d'obligations (investissement minimum de 10 €) », à « 7% de taux d'intérêt fixes », avec une liquidité fixée au « 31 janvier 2029 ».
- Le titre du fichier annonce 310 000 € levés en 12 heures (non vérifié dans le texte).
- Le bien : château « classé au titre des monuments historiques », « D'une valeur d'environ 2 millions d'euros », sur « 11,6 hectares ». Projet de 200 convives, hôtel, tentes et cabanes.
- BODACC : la société (SIREN 980419436), créée en 2023, a déposé ses comptes en 2025 et 2026 ; **aucune procédure collective** publiée [V2D-46] (PAGE LUE). Résultat économique du projet : INCONNU.
- **Lecture** (ESTIMATION) : ce n'est pas une libération de capital, c'est une **dette** à 7 % par an, remboursable en 5 ans. Elle peut financer un investissement productif (hébergement, salle), jamais le déficit de fonctionnement courant. Pour notre domaine, emprunter 700 000 € à 7 % coûte environ 49 000 € d'intérêts par an, avant remboursement.

