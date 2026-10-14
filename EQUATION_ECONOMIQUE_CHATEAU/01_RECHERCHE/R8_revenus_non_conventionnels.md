# R8 — Revenus non conventionnels, revenus fonciers et moteur extérieur

Agent : R8. Démarré le 2026-10-14. Fichier écrit au fur et à mesure.
Sources : `01_RECHERCHE/sources/sources_R8.csv` (identifiants R8-xx).

Statuts : PAGE LUE (page ouverte avec WebFetch, citation exacte) · EXTRAIT (vu seulement dans un résultat de recherche) · ESTIMATION (raisonnement explicite) · HYPOTHÈSE (choix de modélisation) · INCONNU.

> Rappel de périmètre (Contexte permanent) : S1 = 50 ha (35 prés, 12 bois, 3 parc) ; S2 = 120 ha (80 prés, 30 bois, 10 parc) ; S3 = 300 ha (120 prés et terres, 120 bois, 60 parc et jardins). Tous les montants en euros ; année, HT/TTC et périmètre précisés quand la source le permet.

---

## Journal d'avancement

- 2026-10-14 : lecture du contexte, des règles et de la mission. Squelette créé.

- WebSearch 1 (loyers PV au sol), 2 (agrivoltaïsme + chevaux), 3 (forêt) faits. Notes ci-dessous.

---

## 1. Revenus récurrents du foncier

### 1.1 Centrale solaire au sol : loyer versé au propriétaire

- Fourchettes relevées sur un site commercial [R8-01] (PAGE LUE, mise à jour du 8 janvier 2026, auteur non indiqué, fiabilité faible) :
  - « Les loyers moyens constatés se situent entre 1 500 et 6 000 € par hectare et par an » ;
  - « D'après Solaire Conseil, un hectare de panneaux solaires rapporte en moyenne 4 500 € par an » ;
  - « la majorité des projets aboutissent à un loyer annuel compris entre 2 000 et 6 000 € par hectare » ;
  - plafond évoqué : « la rémunération peut atteindre 8 000 €, voire 10 000 € par hectare et par an » ;
  - surface : « au moins 5 hectares sont fréquemment évoqués pour un projet au sol » ;
  - durée : « typiquement 20 à 30 ans voire davantage » (bail emphytéotique « par exemple 18 à 99 ans »). La page ne dit pas qui paie la taxe foncière ni le démantèlement.
- Le résultat de la recherche 1 (EXTRAIT, non vérifié) mentionnait aussi « 1 000-4 500 € de loyer /ha/an » (selectra.info) et « 2 000 à 6 000 € » (LouerSonTerrain). L'article de Reporterre n'a pas pu être lu (HTTP 403).
- **Aucune source officielle ni étude indépendante** (chambre d'agriculture, Safer, CRE) n'a été trouvée sur le niveau des loyers. Divergence forte entre sources : de 1 000 à 10 000 €/ha/an.
- **Contrainte décisive** : depuis la loi APER (2023) et le décret n° 2024-318 d'avril 2024, le photovoltaïque au sol « classique » sur terres agricoles est conditionné à des « documents-cadres » départementaux recensant les surfaces réputées incultes [R8-03]. Des prés de fauche ou des pâtures de chevaux ne sont pas des terres incultes : sur S1/S2/S3, le PV au sol n'est envisageable qu'en **agrivoltaïsme** (voir 1.2) ou sur une friche réellement inculte. ESTIMATION qualitative, à confirmer par R3.

### 1.2 Agrivoltaïsme avec pâturage

- Cadre (Wikipédia [R8-03], PAGE LUE, fiabilité moyenne, legifrance inaccessible) : la loi APER de 2023 (article 11) « encadre cette pratique pour ne pas nuire à l'activité agricole, prioritaire sur la production électrique » ; le décret n° 2024-318 « limite à 40 % la densité maximale des panneaux solaires autorisée dans les installations agrivoltaïques » ; « chute de rendement de maximum 10 % » tolérée ; contrôles « tous les trois ans » ; arrêté du 5 juillet 2024 sur les garanties financières de démantèlement ; l'appel d'offres « agrivoltaïque » « impose la présence d'une zone agricole témoin ».
- Pâturage : les exemples trouvés sont **ovins** (et quelques bovins). Exemple Réussir Pâtre [R8-02] (PAGE LUE, 2021) : un éleveur fait pâturer 71 ha de centrale ; « l'éleveur reçoit entre 150 et 300 euros à l'hectare par an » pour l'entretien ; chargement « en moyenne de cinq brebis par hectare » ; centrales entourées de « clôtures grillagées de deux mètres de haut ». Ce montant rémunère l'éleveur, pas le propriétaire foncier.
- Résultat de la recherche 2 (EXTRAIT) : Neoen indique « quinze centrales solaires couvrant près de 240 hectares qui sont pâturés par les moutons » ; démonstrateurs bovins à Laqueuille et La Bouzule ; projet Lightsource bp à Decize avec trackers à 2,50 m pour vaches allaitantes.
- **Chevaux : aucun exemple trouvé** (recherche web + moteur interne de l'IFCE vide). INCONNU. Hypothèse de prudence : les développeurs privilégient les ovins ; la compatibilité des chevaux (taille, frottements, coups de pied, câblage, clôtures) n'est pas documentée. À vérifier auprès de l'IFCE ou d'un développeur.
- Conséquence pour le modèle : un projet agrivoltaïque sur des prés **retire ces prés de l'usage équestre** ou impose des ovins ; il entre en conflit direct avec le projet du propriétaire et avec l'esthétique des abords d'un monument (covisibilité, avis de l'architecte des Bâtiments de France en abords MH — à confirmer par R3).

### 1.5 Forêt

- Prix du foncier forestier 2025 (Safer et Société Forestière, « Le marché des forêts en 2025 », publié le 21 mai 2026, repris par France Épargne [R8-04], PAGE LUE) : « Le prix moyen s'établit à 4 950 euros l'hectare, en hausse de 2,5 % » ; écart entre « le Massif central à 2 850 euros » et « le nord du Bassin parisien à 7 880 euros » ; 23 030 transactions.
- Prix des bois sur pied en forêt privée [R8-05] (PAGE LUE, communiqué France Bois Forêt du 26 mai 2026) : « Le prix moyen du bois d'oeuvre, toutes essences confondues, s'établit ainsi à 86 €/m³ en 2025 contre 90 €/m³ en 2024 ». Chêne 190 €/m³ en 2025 (228 € en 2024, −17 %) ; hêtre 49 € ; douglas 93 € ; épicéa commun 69 € ; peuplier 62 € ; pin sylvestre 44 €. Base : « ventes groupées de bois sur pied réalisées par les Experts Forestiers de France » (lots commercialisés, donc pas le prix moyen de tout le bois récolté).
- Croissance biologique (DG Trésor, note n° 399 du 3 septembre 2026, citée par [R8-04]) : la croissance « est passée de 5,8 mètres cubes par hectare et par an entre 2005 et 2013 » à un niveau inférieur (la phrase est tronquée dans l'article) ; mortalité « plus que doublé en dix ans » (IGN).
- **Revenu net forestier en €/ha/an : non trouvé à ce stade.** L'indicateur 2020 du marché des forêts [R8-06] (64 pages, lu en entier) ne donne aucun taux de rendement ni revenu net.
- Revenu net forestier : un indicateur courant serait le taux de rendement des groupements forestiers ou une étude de la Société Forestière ; non trouvé à ce stade (voir fin de fichier si complété).

### 1.6 Location de chasse

- WebSearch 4 (Sologne, €/ha/an) : **aucun prix de location à l'hectare** dans les résultats ; seulement des annonces de vente de territoires (Capifrance, Belles Demeures, Patrice Besse) et un cahier des charges préfectoral du Bas-Rhin (droit local) qui renvoie à une « moyenne » locale des loyers à l'hectare issue des adjudications. L'annonce Capifrance « Territoire de chasse de 171 hectares en Sologne » (Brinon-sur-Sauldre) est inaccessible (HTTP 403).
- ONF [R8-07] (PAGE LUE) : « Six adjudications, correspondant à une ou plusieurs régions administratives, ont eu lieu en mars 2025. » « Les prochaines adjudications seront organisées en 2028. » **La page ne publie ni prix à l'hectare ni recettes.**
- **Statut : INCONNU** pour le loyer de chasse en €/ha/an (Sologne ou ailleurs). Méthode pour vérifier : résultats d'adjudications ONF 2025 (catalogues régionaux), fédérations départementales des chasseurs (41, 45, 18), agences spécialisées en Sologne, préfectures d'Alsace-Moselle (baux communaux 2024-2033, droit local), rapport de la Cour des comptes sur l'ONF (recettes de chasse / surface louée).

### 1.8 Truffières

- Terre-net [R8-08] (PAGE LUE, article du 2 octobre 2026, chiffres attribués à la chambre d'agriculture de la Somme et Agri-Truffe) :
  - « le coût d'implantation est estimé à 6 148 €/ha pour la truffe noire et à 11 272 €/ha pour la truffe de Bourgogne » ;
  - « des frais d'entretien compris entre 800 et 1 500 €/ha par an » ;
  - « les premières récoltes interviennent généralement entre 5 et 7 ans après la plantation » ;
  - « une parcelle favorable et irriguée peut produire en moyenne entre 10 et 20 kg/ha » ;
  - prix : « de 400 à 700 €/kg sur les marchés de gros », « plus de 1 000 €/kg pour des truffes de très belle qualité vendues au détail » ;
  - « une marge brute moyenne à 18 500 €/ha/an, sans compter le coût du réensemencement et du chien truffier » ;
  - risque : « Cette année, beaucoup de truffières non irriguées ne produiront pas du tout ».
- Que Choisir [R8-09] (PAGE LUE, 18 décembre 2024) : « les rendements variant de 1 à 80 kg/ha en fonction des années » ; « rares sont ceux qui tirent un salaire de cette production ».
- EXTRAIT (résultat de recherche 5, non vérifié) : FranceAgriMer situerait les rendements entre 0,5 et 5 kg/ha ; le ministère de l'Agriculture donnerait 500 à 900 €/kg et 5 000 à 10 000 €/ha d'installation (page agriculture.gouv.fr inaccessible, HTTP 503).
- **Divergence majeure** : 0,5-5 kg/ha (moyenne nationale, EXTRAIT) contre 10-20 kg/ha (parcelle favorable et irriguée). La marge brute de 18 500 €/ha/an ne vaut que pour le haut de fourchette.
- ESTIMATION pour le modèle (2 ha de truffière irriguée, sol calcaire favorable — HYPOTHÈSE forte : sol adapté, ce que l'on ne sait pas) :
  - investissement : 2 × 6 148 ≈ 12 300 € (hors irrigation, clôture anti-sangliers et terrain) ;
  - entretien : 1 600 à 3 000 €/an ;
  - production année 7+ : bas = 2 ha × 2 kg × 400 € ≈ 1 600 €/an ; haut = 2 ha × 15 kg × 550 € ≈ 16 500 €/an ;
  - contribution nette : de −1 400 € à +13 500 €/an, très aléatoire, nulle pendant 5 à 7 ans. **Piste marginale** à l'échelle d'un château ; intérêt surtout d'image (produit du domaine).

### 1.4 Petite hydroélectricité (moulin, 30 à 300 kW)

- Cadre de soutien (CRE, délibération n° 2026-58 du 5 mars 2026 [R8-10], PAGE LUE) : arrêté tarifaire du 13 décembre 2016 dit « H16 » ; « les nouvelles installations d'une puissance installée strictement inférieure à 200 kW peuvent bénéficier d'un contrat d'obligation d'achat » (seuil « porté à 200 kW à partir du 1er janvier 2026 par le décret n° 2025-498 du 5 juin 2025 ») ; « les nouvelles installations d'une puissance installée strictement inférieure à 1 MW peuvent bénéficier d'un contrat de complément de rémunération » ; « les installations existantes d'une puissance installée strictement inférieure à 1 MW peuvent bénéficier d'un contrat de CR, sous réserve de l'engagement du producteur à réaliser un programme d'investissement ». Plafond de l'énergie rémunérée au tarif : « 120 000 heures équivalentes pleine puissance sur la durée du contrat de soutien pour les installations de basse chute, soit 6 000 hepp/an » ; au-delà, rachat « au prix fixe de 40 €/MWh (non indexé) ». La CRE recommande d'abaisser le plafond à 4 000 hepp/an. Les installations aidées par d'autres régimes (subventions) perdent l'éligibilité (installations neuves) ou voient leur tarif réduit (rénovées).
- Niveau du tarif (réponse ministérielle publiée au JO le 12 décembre 2023 [R8-11], PAGE LUE) : « Aujourd'hui, un producteur d'une installation d'une centaine de kilowatts peut espérer, grâce au H16, un tarif d'environ 170€/MWh produit. » Même source : 463 installations hydroélectriques de moins de 150 kW raccordées, pour « environ 43 MW » au total (soit ≈ 93 kW en moyenne, ESTIMATION par division).
- Coûts et rentabilité (CRE, rapport du 30 janvier 2020 [R8-12], PAGE LUE) :
  - « les coûts d'investissements […] varient entre 2 100 et 5 600 €/kW pour 75 % des installations neuves » ;
  - « Les coûts annuels de fonctionnement (charges d'exploitation et fiscales) se situent quant à eux entre 50 et 180 €/kW pour 75 % des installations », hors gros entretien et renouvellement, qui représentent « de l'ordre de 2 à 4 % des coûts d'investissements initiaux », « 2 à 3 fois au cours des 15 premières années » ;
  - productible « entre 2 000 et 4 300 heures annuelles d'équivalent pleine puissance pour 75 % des installations » ;
  - LCOE des installations neuves « de 37 à plus de 200 €/MWh » ; rénovées « quasi-exclusivement en dessous de la barre des 100 €/MWh » ;
  - « la moitié des installations pour lesquelles la rentabilité a pu être calculée présente des taux de rentabilité interne (TRI) avant impôt insuffisants, voire négatifs » ; « le TRI moyen étant de 14,1 % pour ces installations [rénovées] contre 2,5 % pour les installations neuves » ;
  - l'arrêté H16 « impose un montant minimum d'investissements de rénovation de 500 €/kW ».
- ESTIMATION (moulin existant rénové de 100 kW, droit d'eau supposé valide — HYPOTHÈSE) :
  - production : 100 kW × 2 000 à 4 300 h = 200 à 430 MWh/an ;
  - chiffre d'affaires HT : × ≈ 170 €/MWh (ordre de grandeur 2023 pour ≈ 100 kW ; le tarif réel d'une rénovation dépend de l'investissement) = **34 000 à 73 000 €/an** ;
  - charges de fonctionnement : 100 kW × 50 à 180 €/kW = 5 000 à 18 000 €/an ;
  - excédent avant amortissement : ≈ **16 000 à 68 000 €/an** ; investissement de rénovation ≥ 50 000 € (500 €/kW minimum), installation neuve 210 000 à 560 000 €.
  - Pour 30 kW : diviser par ≈ 3,3. Pour 300 kW : plus d'obligation d'achat (seuil 200 kW) ; complément de rémunération avec vente sur le marché.
- Condition préalable : une chute d'eau et un droit d'eau existants sur le domaine. **Piste réservée aux domaines qui ont déjà un moulin ou un seuil** ; à ne pas intégrer par défaut dans S1/S2/S3.
