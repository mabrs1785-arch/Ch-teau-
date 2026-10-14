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

### 1.7 Crédits carbone (Label bas-carbone, LBC)

- Volumes du label [R8-13] (PAGE LUE, 2026-10-14) : « 2 522 » projets labellisés ; « 9 180 525 » crédits carbone potentiels ; « 144 917 » crédits carbone vérifiés ; la page précise que le suivi des financements « ne reflète donc pas encore la réalité de l'état de financement des projets ».
- Prix (I4CE, juin 2025, repris par Terre-net [R8-14], PAGE LUE) : « La tonne de carbone évitée a été payée en moyenne 35 € par les financeurs » ; « 1 685 projets Label Bas Carbone (LBC) sont validés, représentant un impact potentiel de 6,41 MtCO2eq » (au 31 mars 2025). EXTRAIT (recherche 7, DREAL Pays de la Loire, octobre 2025, PDF inaccessible) : prix « de 20 à 70 €/tCO2e » selon les projets.
- Méthode Boisement [R8-15] (PAGE LUE, V3 du 6 septembre 2025) : durée « 30 ans » ; « Le terrain n'était pas boisé durant les 10 ans précédant la notification » ; surface minimale « 0.5 ha » ; rabais « de 10% pour les risques généraux », « de 0 à 15% pour les risques d'incendies » ; vérification « au bout de 5 ans » ; aides publiques plafonnées à « 50% des coûts des travaux forestiers ».
- Crédits par hectare observés dans le registre [R8-16] (PAGE LUE ; ratios = ESTIMATION par division) :

| Projet (registre LBC) | Méthode | Surface | Crédits potentiels | Crédits/ha (calcul) |
|---|---|---|---|---|
| OKLIMA – Forêt de Quincampoix-Fleuzy | Boisement | 3 ha | 920 | ≈ 307 |
| Carbonapp n° 384 Carnoy-Mametz (80) | Boisement | 4,29 ha | 1 535 | ≈ 358 |
| Créquy (62) | Boisement | 1,91 ha | 703 | ≈ 368 |
| Montautour – Fransylva services | Boisement | 2,31 ha | 567 | ≈ 245 |
| SYLVO/UNISYLVA n° 31 Saint-Laurent-en-Gâtine | Boisement | 7 ha | 2 013 | ≈ 288 |
| Reforest'Action Aubigny-sur-Nère (18) | Boisement | 8 ha | 1 388 | ≈ 174 |
| Carbonapp n° 366 Baugé-en-Anjou (49) | Boisement | 4,5 ha | 983 | ≈ 218 |
| SYLVO/Forêt d'ici Beaufort-Blavincourt | Reboisement | 4,10 ha | 1 051 | ≈ 256 |
| Maa Biodiversity – Le Theillay (41, Sologne) | Gestion forestière à stock continu | 69 ha | 1 585 | ≈ 23 |

- ESTIMATION pour le modèle :
  - **Forêt existante gérée** (méthode « stock continu », exemple solognot) : ≈ 23 crédits/ha sur la durée du projet × 35 €/t ≈ **800 €/ha une seule fois**, soit pour S2 (30 ha de bois) ≈ 24 000 € sur la durée du projet, et pour S3 (120 ha) ≈ 97 000 €. Revenu **ponctuel**, pas annuel, et soumis à des engagements de gestion sur la durée du projet.
  - **Boisement** de terres agricoles : ≈ 170 à 370 crédits/ha × 35 € ≈ 6 000 à 13 000 €/ha, versés par des financeurs qui paient en pratique la plantation. Ce n'est **pas un revenu net** : c'est un financement du boisement. Et le boisement retire des prés à l'usage équestre.
  - Conclusion : piste d'image (RSE, mécénat d'entreprise) plus que de trésorerie récurrente.

---

## 2. Stockage et locations peu intensives des dépendances

### 2.1 Gardiennage de voitures de collection

- Belgique (Forbes Belgique, 16 août 2026 [R8-18], PAGE LUE) : La Cylindrerie (Mont-Saint-Guibert) : « on débute autour de 200 euros par mois pour un emplacement » ; Le Paddock (Bains de Spa) : « une vingtaine de véhicules de collection », « accès contrôlé et une surveillance 24 heures sur 24 et 7 jours sur 7 » ; DriveCity (Nivelles) : « plus de 200 véhicules de collection », projet de « 60 emplacements sécurisés supplémentaires », « une vingtaine de caméras de surveillance avec alarmes connectées instantanées ». Clientèle du Paddock : « les investisseurs privés ».
- Suisse (EXTRAIT, Comparis [R8-19]) : gardiennage « sécurisé et climatisé » à Saint-Sulpice (VD) annoncé « CHF 250.- par mois ».
- **France : aucun tarif trouvé** dans les résultats (INCONNU). Méthode : relever les tarifs de garages spécialisés (Île-de-France, Normandie, Val de Loire) et de clubs de collectionneurs.
- ESTIMATION (dépendance de 600 m², ≈ 20 m² bruts par voiture avec circulation — HYPOTHÈSE) : ≈ 25 à 30 places ; à 150-200 €/mois TTC (prix belge ramené à une zone rurale française — HYPOTHÈSE) et 70 % d'occupation → **≈ 32 000 à 50 000 € TTC/an** de chiffre d'affaires. À retrancher : assurance (responsabilité du dépositaire, incendie), alarme, vidéosurveillance, déshumidification, accueil des clients. Charge opérationnelle faible mais réelle (allées et venues, ce qui touche la tranquillité). Demande en zone rurale isolée : **non démontrée**.

### 2.2 Hivernage de camping-cars, caravanes et bateaux

- Wikicampers, 30 novembre 2025 [R8-17] (PAGE LUE) : hangar agricole « Le prix moyen se situe autour de 350 € par an » (« sans services supplémentaires ») ; intérieur (hangar ou entrepôt) « de 70 € à 110 € TTC par mois » et « de 350 € à 550 € TTC/an » ; centre professionnel couvert « autour de 550 € par an » ; extérieur sous abri « de 200 € à 400 € TTC / an » ; extérieur non protégé « de 150 € TTC/an à 450 € TTC/an ».
- ESTIMATION (grange de 600 m², ≈ 30 m² par camping-car avec manœuvre — HYPOTHÈSE) : ≈ 20 véhicules × 350 à 550 € TTC/an = **7 000 à 11 000 € TTC/an**. Très faible charge (2 mouvements par an et par véhicule). Contraintes : sol, hauteur de porte (≥ 3,5 m), accès poids lourd, assurance, changement d'usage éventuel d'un bâtiment agricole (à vérifier avec R3).

### 2.3 Stockage de vins de collection

- Les Chais de France (Issy-les-Moulineaux, message de l'entreprise du 18 septembre 2020 [R8-20], PAGE LUE, fiabilité faible) : « Pour une cave privative de capacité 1200 bouteilles », « il faut compter 240 € TTC/Mois », avec « Livraisons illimitées et gratuites », « Pas de frais de sortie. » Le même fil évoque « 1€ la bouteille » chez Bourdin (caves naturelles).
- ESTIMATION : 240 € × 12 / 1 200 bouteilles = **2,40 € TTC par bouteille et par an, soit ≈ 29 € TTC par caisse de 12 et par an** (offre urbaine haut de gamme, 2020). Caves naturelles : ≈ 1 € par bouteille et par an (≈ 12 €/caisse), non daté précisément.
- Conditions techniques (iDealwine [R8-21], PAGE LUE) : « entre 12 et 14°C », hygrométrie « d'environ 70% », « à l'abri de la lumière et des vibrations » ; « Les vins sont assurés et remboursés en cas de sinistre. » iDealwine ne publie pas son tarif.
- ESTIMATION de potentiel : une cave voûtée de château de 100 m² peut contenir de l'ordre de 10 000 à 20 000 bouteilles (HYPOTHÈSE de densité) → à 1 à 2,4 €/bouteille/an, **10 000 à 48 000 € TTC/an** au maximum, si la clientèle existe. Clientèle locale de collectionneurs **non démontrée** ; responsabilité et assurance lourdes (valeur des stocks).

### 2.4 Garde-meubles et stockage d'œuvres d'art

- **INCONNU** (aucune recherche dédiée, faute de budget). Méthode : grilles tarifaires publiques des réseaux de self-stockage (€/m²/mois) et devis de transporteurs d'art (conditions muséales, agrément des assureurs). Point d'attention : le stockage d'œuvres d'art exige climatisation, détection intrusion et incendie, et l'accord des assureurs ; investissement lourd pour une demande rurale incertaine.

---

## 3. Locations longues

### 3.1 Loyers résidentiels ruraux (€/m²/mois)

- Source officielle [R8-22] (PAGE LUE) : « Carte des loyers » 2025 du ministère de la Transition écologique, indicateurs « estimés par l'ANIL » à partir d'annonces leboncoin et SeLoger (« 9,1 millions d'annonces locatives », période 2019-2025) ; « Les indicateurs de loyers sont fournis charges comprises » ; biens « mis en location au 3ème trimestre 2025 » ; maison de référence : « surface de 92 m² ».
- Échantillon lu dans le fichier « maisons » [R8-23] (PAGE LUE, 40 premières lignes ; colonne `loypredm2`, loyer d'annonce charges comprises en €/m²/mois — unité mensuelle implicite) :

| Zone (communes rurales) | Département | Loyer prédit maison (€/m²/mois, CC) | Intervalle de prédiction |
|---|---|---|---|
| Druye, Rivarennes, Vallères, Saché, Bréhémont… (Touraine, maille) | 37 | 8,96 | 6,95 – 11,55 |
| Azay-le-Rideau (commune) | 37 | 9,24 | 7,18 – 11,89 |
| Gâtine (Clavé, Vasles, Ménigoute…) | 79 | 6,82 | 5,26 – 8,83 |
| Saint-Sornin, Orgedeuil… (maille) | 16 | 7,54 | 6,05 – 9,40 |
| La Rochefoucauld-en-Angoumois (commune) | 16 | 8,03 | 6,45 – 10,00 |
| Bas-Vivarais / Gard rhodanien (maille) | 07 / 30 / 84 | 10,50 | 7,94 – 13,89 |
| Pont-Saint-Esprit (commune) | 30 | 10,91 | 8,24 – 14,46 |

- Lecture : en zone rurale, une maison se loue **≈ 7 à 11 €/m²/mois charges comprises** (annonces 2025). Ce sont des loyers d'annonce, pas des loyers signés. L'échantillon n'est pas représentatif de toute la France (fichier trié par zone ; lecture limitée aux 40 premières lignes). Le fichier complet (4,7 millions de caractères) n'a pas pu être téléchargé (connexion coupée par le proxy).
- ESTIMATION (S2 : transformer 600 m² de communs en 6 logements de 100 m²) : 600 m² × 8 €/m²/mois × 12 = **57 600 €/an de loyers charges comprises**, avant vacance (HYPOTHÈSE 5 %), charges récupérables, entretien, gestion, taxe foncière et impôt. Revenu **récurrent**, faible charge opérationnelle, mais présence permanente de tiers sur le domaine (vie privée).

### 3.2 Coût de transformation de bâtiments agricoles en logements ou bureaux (€/m²)

- Cas réel documenté (CAUE de Haute-Savoie, « Références 2025 » [R8-24], PAGE LUE) : réhabilitation d'une ancienne ferme de 1875 au Biot (74), « rénovation à coût serré », maître d'ouvrage privé : « SURFACE DE PLANCHER 165 m2 I COÛT DES TRAVAUX : 256 755 € HT I COÛT DE L'OPÉRATION (HORS FONCIER) 322 205 € TTC », livraison avril 2023.
  - ESTIMATION : **≈ 1 556 €/m² HT de travaux** et **≈ 1 953 €/m² TTC tout compris** (honoraires inclus, hors foncier), valeur 2022-2023, montagne.
- EXTRAIT (recherche 10, Habitatpresto [R8-25], non vérifié) : rénovation d'une bâtisse ancienne « en moyenne entre 800 et 1 500 € / m² » ; un témoignage de forum évoque 2 200 €/m² habitable pour un vieux bâtiment en pierre (ancien, non retenu).
- Pas de chiffre trouvé pour la transformation en **bureaux** (INCONNU ; la mise aux normes ERP/code du travail ajoute des coûts — voir R3).
- ESTIMATION de rentabilité (logement locatif dans des communs, S2) : coût 1 600 à 2 000 €/m² TTC (HYPOTHÈSE calée sur le cas du Biot) ; loyer 7 à 11 €/m²/mois CC (§3.1) soit 84 à 132 €/m²/an ; **rendement brut ≈ 4 à 8 %** avant charges non récupérables, gros entretien, vacance et impôt. Pour 600 m² : investissement ≈ 1,0 à 1,2 M€ pour ≈ 50 000 à 79 000 €/an de loyers bruts. La rentabilité nette est modeste ; l'intérêt principal est d'entretenir et d'occuper des bâtiments qui coûteraient de toute façon (couverts, toitures). Contraintes : changement de destination au PLU, avis ABF en abords ou bâtiment protégé, assainissement.

### 3.3 Ateliers d'artisans, bureaux, domaines qui louent leurs dépendances

- Pas de recherche dédiée (budget). Loyers de bureaux ou d'ateliers ruraux : **INCONNU**. Méthode : annonces de locaux d'activité en zone rurale (€/m²/an HT), ou observatoires des CCI. Pour le Royaume-Uni, voir R5 (location commerciale des dépendances par les « estates »).

---

## 4. Locataires institutionnels (écoles, formation, fondations, tournages)

- **Château de Ferrières (Seine-et-Marne)** [R8-26] (Wikipédia, PAGE LUE) : propriétaire actuel « Commune de Ferrières-en-Brie » ; « légué en 1975 à la chancellerie des universités de Paris par le baron Guy de Rothschild » ; « rétrocédé en 2012 aux ayants droit des donataires », qui le rétrocèdent « à la commune de Ferrières-en-Brie » ; « En juillet 2013, le château est confié par la commune à une société privée pour y créer l'école Ferrières », ouverte « en octobre 2015 » (« gastronomie, hôtellerie et luxe ») ; parc « à l'anglaise de 125 hectares ». **Conditions financières (bail, redevance, durée, travaux) : INCONNU** — la recherche 11 n'a rien trouvé. Méthode : délibérations du conseil municipal de Ferrières-en-Brie de 2013, registre des actes.
- **Institut Lyfe (ex-Institut Paul Bocuse), château du Vivier à Écully** [R8-27] (Wikipédia, PAGE LUE) : « Le campus de l'école gravite autour du château du Vivier situé dans le parc du Vivier de 7 hectares » ; « plus de 1 200 étudiants, de plus de 75 nationalités » (donnée signalée sans source secondaire). Propriété du château et loyer : **INCONNU** (non indiqués).
- **École nationale supérieure de pâtisserie (Ducasse), château de Montbarnier à Yssingeaux** [R8-28] (Wikipédia, PAGE LUE) : château « racheté en 1963 par la commune d'Yssingeaux » ; « Les bâtiments restent propriété de la ville d'Yssingeaux » ; liquidation judiciaire en 2007 puis reprise par Alain Ducasse et Yves Thuriès (51 % / 49 %) ; « Elle forme plus de 1 500 personnes par an ». Loyer : **INCONNU**.
- Constat : dans les trois cas trouvés, **le propriétaire du château est une collectivité** (ou l'école elle-même), pas un particulier, et l'école apporte l'exploitation. Aucun exemple n'a été trouvé d'un propriétaire privé qui vit dans le château tout en louant le reste à une école. Une école ou un centre de formation suppose : ERP de type R, hébergement, restauration, flux quotidien de centaines de personnes → **incompatible avec la « partie entièrement privée » et le calme** souhaités, sauf à céder l'usage de l'essentiel du domaine.
- Pensionnats internationaux, colonies de vacances, centres de formation d'entreprise, studios de tournage : **non documentés ici** (budget de recherche épuisé ; tournages traités par R7). INCONNU.

---

## 7. Moteur extérieur (capital financier, immobilier, entreprise, dotation)

### 7.1 Taux de dépense soutenable d'une dotation perpétuelle

- NACUBO-Commonfund, exercice 2025 (1er juillet 2024 – 30 juin 2025) [R8-34] (PAGE LUE, PDF) : 657 institutions, « $944.3 billion » d'actifs ; « Institutions' average annual effective spending rate increased moderately to 4.9 percent from 4.8 percent in FY24 » ; taux prévus par les règles de dépense (« Policy Rates ») : 4,6 % (FY24) et 4,7 % (FY25) ; « Average target nominal return » 7,3 % ; écart moyen visé au-dessus de l'inflation 4,9 % ; « The conventional approach for many endowments is to set CPI or HEPI +5% (i.e., inflation plus a spending/distribution percentage) as a return target ». Rendements moyens annualisés (graphique) : 1 an 10,9 % (FY25) ; 10 ans 7,7 % (FY25) contre 6,8 % (FY24) (lecture du graphique, confirmée par l'EXTRAIT de la recherche 12).
- UBS Global Investment Returns Yearbook 2025 [R8-32] (PAGE LUE) : depuis 2000, « global equity investors still enjoyed an annualized real return of 3.5% and an equity risk premium relative to bills of 4.3% » ; base de « 23 marchés » de 1900 à 2024. Les rendements réels depuis 1900 ne sont pas affichés sur la page (INCONNU ici).
- Jordà et al., « The Rate of Return on Everything, 1870–2015 » [R8-33] : le résumé NBER ne donne pas de chiffre (INCONNU ici).
- Lecture : les grandes dotations américaines dépensent ≈ 4,5 à 5 % par an, mais visent pour cela inflation + ≈ 5 % de rendement, avec une forte part de capital-investissement, **sans impôt** (institutions exonérées) et en dollars. Un particulier ou une société française supporte l'impôt (§7.2), ce qui réduit le taux soutenable.
- ESTIMATION (taux de retrait net soutenable pour un patrimoine financier diversifié détenu par un particulier résident français) : rendement réel avant impôt d'un portefeuille équilibré ≈ 3 à 4 % (HYPOTHÈSE, cohérente avec 3,5 % réel pour les actions mondiales depuis 2000 et une part obligataire) ; fiscalité ≈ 31,4 % sur les revenus et plus-values **nominaux** réalisés (§7.2), soit, avec 2 % d'inflation, une ponction de l'ordre de 1,0 à 1,5 point par an si tout le rendement était réalisé chaque année (moins si plus-values latentes ou enveloppes fiscales) → **taux de retrait réel net soutenable ≈ 2,5 à 3 %** du capital (HYPOTHÈSE de travail, à stress-tester).

### 7.2 Fiscalité française des revenus financiers (2026)

- Service-public, fiche F2613, « Vérifié le 15 avril 2026 » [R8-31] (PAGE LUE) : « Le prélèvement forfaitaire unique est constitué de l'impôt sur le revenu (12,8 %) et des prélèvements sociaux. » « Le taux des prélèvements sociaux sur les revenus de placements passe à 18,6 % à compter du 1er janvier 2026. » Des « règles particulières s'appliquent à certains placements ». Option possible pour le barème progressif (abattement de 40 % sur les dividendes).
- ESTIMATION : taux global du PFU en 2026 = 12,8 % + 18,6 % = **31,4 %** (addition, la page n'écrit pas ce total). Le taux applicable aux revenus fonciers, à l'assurance-vie et aux plus-values immobilières n'a pas été vérifié ici (à confirmer par R3).

### 7.3 Rendement des SCPI (ASPIM)

- Année 2025 (ASPIM, communiqué du 9 février 2026 [R8-29], PAGE LUE) : « le taux de distribution pondéré par la capitalisation, toutes catégories confondues, s'établit à 4,91 % », « en progression de 0,19 point par rapport à 2024 » (donc ≈ 4,72 % en 2024, ESTIMATION par soustraction) ; « le prix de part moyen pondéré par la capitalisation recule de 3,45 % » ; « les SCPI affichent une performance globale de +1,46 % en 2025 » ; « 14 SCPI à capital variable ont diminué leur prix de souscription » ; 50 % des SCPI ont réduit leur dividende ; capitalisation « 89 milliards € ».
- Premier semestre 2026 (ASPIM, 5 août 2026 [R8-30], PAGE LUE) : taux de distribution semestriel « 2,30 % » (2,29 % au 1er semestre 2025) ; « le prix de part moyen de l'ensemble des SCPI, pondéré par la capitalisation, diminue ainsi de 2,4 % » ; SCPI à capital fixe : prix moyen « en repli de 33 % depuis le début de l'année » ; capitalisation « 86 milliards d'euros ».
- Lecture : un taux de distribution de ≈ 4,9 % brut s'accompagne d'une **érosion du capital** (−3,45 % en 2025, −2,4 % au S1 2026) : la performance globale (+1,46 % en 2025) est très inférieure au taux de distribution. Les revenus de SCPI détenues en direct sont des revenus fonciers (barème + prélèvements sociaux) et entrent dans l'IFI.
- ESTIMATION (particulier à la tranche marginale de 45 %, prélèvements sociaux 17,2 % ou 18,6 % selon le régime applicable — à vérifier) : 4,91 % × (1 − 0,45 − 0,172) ≈ **1,9 % net** (hors IFI et hors frais d'entrée de ≈ 8-10 %, HYPOTHÈSE). Pour 1,2 M€ net par an, il faudrait ≈ 65 M€ de SCPI : **piste peu efficace pour un contribuable fortement imposé**.

### 7.4 Rendements de l'immobilier commercial et résidentiel

- Proxy immobilier tertiaire grand public : SCPI, ≈ 4,9 % de distribution en 2025 mais performance globale +1,46 % (§7.3).
- Résidentiel rural : rendement brut ≈ 4 à 8 % sur des logements créés dans des communs (§3.2, ESTIMATION). Rendements « prime » des bureaux et commerces : **INCONNU** (pas de recherche dédiée ; à prendre dans les notes trimestrielles des grands conseils immobiliers).

### 7.5 Reprise d'une PME comme moteur de revenus

- Multiples de valorisation (Argos Index® mid-market, 2e trimestre 2026 [R8-35], PAGE LUE, PDF) : l'indice « mesure l'évolution de la valorisation des PME non cotées de la zone euro » ; « L'Argos Index® a progressé de 2,3% pour s'établir à 8,8x l'EBITDA » ; « Les multiples médians des fonds d'investissement ont augmenté à 10,2x l'EBITDA et ceux des acquéreurs stratégiques à 7,9x » ; le segment inférieur « (15 à 150 millions d'euros) est resté globalement stable » ; « La part des opérations effectuées sur des multiples inférieurs à 7x l'EBITDA a augmenté à 27% ». Le périmètre (transactions de 15 à 500 M€) est **au-dessus** de la PME qu'un particulier reprend seul ; les multiples des petites PME (valeur < 15 M€) ne sont pas dans cette source (INCONNU ici).
- Taux d'échec des reprises :
  - Question écrite AN n° 75244, publiée le 11 octobre 2005 [R8-36] (PAGE LUE) : « D'après une récente étude de la nouvelle banque publique d'aide aux PME (OSEO-BDPME), plus d'une transmission sur cinq échoue dans les six ans et le risque de défaillance augmente lorsque la cession est précipitée ou que le repreneur n'a aucun lien avec l'entreprise. Cette étude a pour base un échantillon de 3 000 dossiers représentatifs des 27 000 transmissions de PME référencées de 1997 à 2003 par OSEO. » Les PME reprises sont « fragilisées par le remboursement de la dette liée au financement de la reprise ».
  - EXTRAIT (recherche 14, Banque des Territoires [R8-37], page en maintenance, non vérifié) : « 71 % des établissements repris en 2011 existent toujours cinq ans après, contre 51 % des créations de la même année ».
  - Lecture : ≈ 20 % d'échec à 5-6 ans (donnée ancienne, 1997-2003). Pas de chiffre récent vérifié.
- ESTIMATION — capacité de distribution d'une PME détenue sans dette d'acquisition (chaîne fiscale : IS 25 % puis PFU 31,4 % sur dividendes) : 1 € de résultat avant impôt → 0,75 € après IS → 0,75 × (1 − 0,314) ≈ **0,51 € net** pour l'actionnaire personne physique.
  - Pour 0,3 / 0,6 / 1,2 M€ nets par an : résultat avant impôt distribuable ≈ 0,58 / 1,17 / 2,33 M€, après investissements de maintien et rémunération d'un dirigeant salarié (le propriétaire de 26 ans ne peut pas diriger à la fois l'entreprise et le domaine — leçon n° 3 du contexte).
  - Avec un EBITDA ≈ 1,3 × le résultat avant impôt (HYPOTHÈSE : amortissements et frais financiers ≈ 25 % de l'EBITDA), EBITDA nécessaire ≈ 0,8 / 1,5 / 3,0 M€. À 7,9x (multiple médian des acquéreurs stratégiques, mid-market), valeur d'entreprise ≈ **6 / 12 / 24 M€** ; à 5x (HYPOTHÈSE pour une petite PME, non sourcée), ≈ 4 / 7,5 / 15 M€.
  - Avec dette d'acquisition (LBO), la trésorerie sert d'abord au remboursement pendant 5 à 7 ans : **distribution quasi nulle au début** — incompatible avec un besoin annuel immédiat.
  - Risque : ≈ 1 reprise sur 5 échoue en 6 ans (donnée ancienne) ; concentration du risque sur une seule entreprise. Un moteur crédible passe par la **diversification** (plusieurs participations ou portefeuille financier) ou par la conversion progressive des dividendes en dotation.

### 1.3 Hangars photovoltaïques financés par un tiers

- **INCONNU** (pas de recherche dédiée, budget de 15 recherches atteint). Méthode : conditions types des développeurs (bail emphytéotique ou droit de superficie de 20 à 30 ans, hangar livré en échange de la toiture), avis des chambres d'agriculture. Point d'attention : un hangar neuf à proximité d'un monument protégé passe par l'avis de l'ABF (à confirmer par R3).

### 1.9 Sapins de Noël, vente de foin, fumier, miel

- **INCONNU** pour les prix et volumes (pas de recherche dédiée). La vente de foin dépend du rendement des prés et du prix local ; le prix d'achat du foin pour les chevaux doit être pris chez R2 (coût) et non compté deux fois. Le fumier de cheval et le miel (ruches prêtées à un apiculteur) relèvent de l'ordre de quelques centaines à quelques milliers d'euros (HYPOTHÈSE non sourcée, à ne pas modéliser sans vérification).

### 1.5 bis Forêt : hypothèse de revenu net

- Faute de source, **HYPOTHÈSE de travail à valider** : revenu net de 50 à 100 €/ha/an (ce qui correspondrait à ≈ 1 à 2 % d'un prix moyen de 4 950 €/ha). Non sourcé : à vérifier dans l'indicateur 2025 complet de la Société Forestière ou auprès d'un expert forestier. Soit S1 (12 ha) ≈ 600-1 200 €/an ; S2 (30 ha) ≈ 1 500-3 000 €/an ; S3 (120 ha) ≈ 6 000-12 000 €/an. Revenu irrégulier (coupes), exposé au dépérissement (mortalité « plus que doublé en dix ans ») et à la baisse du chêne (−17 % en 2025).

---

## 5. Clubs privés (équestres, polo, golf, « country club »)

- **Polo de Paris** [R8-38] (Wikipédia, PAGE LUE, données de 2010) : « En 2010 le Polo de Paris comptait 3 250 membres » (« environ 6 000 personnes en tenant compte des familles ») ; admission : « deux parrains » et « la liste d'attente » ; « s'acquitter des droits d'admission de 15 000 euros » (« Par famille et à vie ») ; « une cotisation annuelle de 875 euros » ; surface « 86 720 mètres carrés », en location auprès du conseil municipal de Paris ; polo, tennis, équitation, golf, natation.
  - ESTIMATION : 3 250 × 875 € ≈ 2,84 M€/an de cotisations (2010), plus les droits d'entrée. Mais c'est un club **urbain** (bois de Boulogne) avec un bassin de clientèle parisien ; non transposable tel quel à un château rural.
- **Soho House / Soho Farmhouse** [R8-39] (Wikipedia, PAGE LUE) : Soho Farmhouse (Oxfordshire) « since 2015 » ; « In June 2015, Soho House had over 50,000 members and a global waiting list of over 30,000 » ; 270 000 membres en 2025 (encadré) ; 2023 : chiffre d'affaires « US$1.14 billion », résultat d'exploitation « US$−20 million », résultat net « US$−118 million » ; « Soho House had never made a profit; pre-tax losses for 2024 were forecast to be about $73 million » ; « In August 2025, it publicly announced plans to go private in a $2.7 billion deal led by New York-based MCR Hotels ». Cotisations : non indiquées sur la page (INCONNU ici).
  - Lecture : le modèle « club de campagne » le plus célèbre repose sur un réseau mondial de 270 000 membres, des investissements hôteliers lourds et **n'a jamais été rentable au niveau du groupe**. C'est un contre-exemple pour un domaine isolé.
- Clubs équestres ou de golf privés en zone rurale française : **cotisations INCONNUES** (le site du Polo Club du Domaine de Chantilly n'a pas été trouvé ; pas de recherche dédiée). Méthode : grilles tarifaires publiques de golfs privés (cotisation annuelle + droit d'entrée) et de clubs de polo de province.
- **Effet sur la tranquillité** : un club suppose une fréquentation régulière (week-ends), des événements et un parc de stationnement ; il est **antinomique d'une résidence entièrement privée**, sauf si le club occupe un site séparé du domaine (communs éloignés, terrains de polo à l'écart). Le polo et l'équitation sont toutefois cohérents avec la passion du propriétaire.

---

## 6. Libération de capital par l'immobilier

### 6.1 Modèle de Castello di Reschio (Ombrie)

- Site du domaine [R8-40] (PAGE LUE) : « from 50 ruins, 31 houses have metamorphosised into stunning architecturally designed houses » (présentation d'un livre) ; les Bolza arrivent « in 1984 » ; projet « shaped over more than three decades ».
- Resident [R8-41] (PAGE LUE, URL datée du 4 juin 2026) : « A 3,400-acre private estate, it was acquired by Count Antonio Bolza in the 1990s » (≈ 1 376 ha, ESTIMATION par conversion) ; restauré « over three decades by his son, architect Count Benedikt Bolza » ; le domaine « functions simultaneously as a working estate, a hotel, and a collection of individually designed private villas » ; mobilier « produced in Bolza's own on-site studio ».
- Wikipedia [R8-43] (PAGE LUE) : « In 1994, count Benedikt Bolza purchased the estate. » **Divergence** entre sources sur la date (1984 / années 1990 / 1994) et sur l'acheteur (Antonio ou Benedikt). EXTRAIT (recherche 15) : le site indiquerait un domaine de 1 500 ha.
- Country Life [R8-42] (EXTRAIT, texte non lisible) : « of the 50 farmhouses on the estate, almost half have already been converted, and 10 remain for sale » ; ventes en pleine propriété, par Knight Frank.
- **Prix de vente des ruines et des maisons restaurées : INCONNU.**
- Mécanique du modèle (ESTIMATION à partir des sources) : (1) un très grand foncier (≈ 1 400-1 500 ha) avec **50 ruines dispersées** ; (2) vente des ruines avec un terrain à des acheteurs fortunés ; (3) marge sur la conception et la restauration (studio d'architecture et ateliers sur place) ; (4) services récurrents aux propriétaires et hôtel dans le château (ouvert en 2021 d'après l'EXTRAIT de Cultured) ; (5) le château et le cœur du domaine restent à la famille.
- Transposition en France (ESTIMATION) : les domaines S1-S3 n'ont pas 50 fermes dispersées ; S3 (300 ha, 4 000 m² de dépendances) pourrait en avoir quelques-unes. Chaque vente d'une dépendance avec terrain suppose : changement de destination autorisé au PLU, division (et régime du lotissement si plusieurs lots à bâtir), droit de préemption de la Safer pour les biens agricoles, abords de monument historique (ABF), servitudes de passage. **Ces règles n'ont pas pu être vérifiées ici** (service-public n'a pas de fiche Safer ; safer.fr indisponible) : à confirmer par R3. Prix des dépendances vendues : à estimer par les valeurs foncières locales (DVF), INCONNU ici.
- Effet sur la vie privée : la vente crée des **voisins permanents** à l'intérieur du domaine ; à Reschio, c'est accepté parce que l'échelle est très grande (≈ 1 400 ha).

### 6.2 Équivalents français trouvés

- Aucun exemple français documenté de domaine de château finançant son entretien par la vente de hameaux restaurés n'a été trouvé (pas de recherche dédiée). INCONNU.

### 6.3 Démembrement de propriété (nue-propriété / usufruit)

- Service-public, fiche F33076, « Vérifié le 06 décembre 2024 » [R8-44] (PAGE LUE) : l'usufruitier peut utiliser le bien, l'habiter ou le louer et percevoir les loyers ; il doit « faire toutes les réparations d'entretien » ; « Les grosses réparations sont à la charge du nu-propriétaire sauf si elles résultent du manque d'entretien » ; pour un immeuble, les grosses réparations « ne concernent que le gros-œuvre ».
- Barème fiscal de l'usufruit (article 669 du CGI) : **non lu** (le simulateur de service-public ne l'affiche pas ; legifrance inaccessible). À reprendre de R3.
- Usage possible comme outil de financement (ESTIMATION, aucun exemple trouvé pour un château) : vendre la nue-propriété d'un bien de rapport (dépendances louées) à un investisseur en gardant l'usufruit apporte un capital immédiat, mais le propriétaire perd la valeur future du bien. Par défaut, le gros œuvre incombe au nu-propriétaire (citation ci-dessus), ce qui peut **transférer une partie du gros entretien** à l'investisseur — point à vérifier juridiquement, car les conventions peuvent répartir autrement les charges (R3). Marché d'investisseurs pour la nue-propriété d'un château : non démontré.

### 6.4 Fonds de dotation ou fondation portant un domaine

- Règles (Wikipédia [R8-45], PAGE LUE ; certaines sections sont signalées comme à sourcer, et la page mentionne encore l'ISF, supprimé — à recouper avec R3) : forme issue de la loi n° 2008-776 du 4 août 2008 (article 140) ; « Le fonds de dotation est une personne morale de droit privé à but non lucratif qui reçoit et gère, en les capitalisant, des biens et droits de toute nature qui lui sont apportés à titre gratuit et irrévocable » et « utilise les revenus de la capitalisation en vue de la réalisation d'une œuvre ou d'une mission d'intérêt général » ; « la dotation initiale étant fixée à 15 000 € minimum » ; fonds publics interdits sauf dérogation ; commissaire aux comptes « dès que ses ressources excèdent […] plus de 10 000 euros » ; dons des particuliers : « 66 % du montant du don est déductible de l'impôt sur le revenu, dans la limite de 20 % du revenu imposable » ; entreprises : « 60 % ». Recensement 2024 : « 4 628 fonds de dotation », « dont environ 3 000 réellement en activité ». Exemple patrimonial cité : « Fonds de dotation Marc Ladreit de Lacharrière pour l'Abbaye romane de Lubilhac ».
- Exemple de domaine porté par une fondation : **Fondation de Coubertin** [R8-46] (PAGE LUE) : devenue « en 1973 la Fondation de Coubertin, immédiatement reconnue d'utilité publique » ; « Le domaine de Coubertin (80 hectares » ; « un château de la fin du XVIIe siècle » ; « fonderie de Coubertin, pour la chaudronnerie et la fonte d'art » ; « L'institution reçoit chaque année une trentaine de jeunes gens » issus des Compagnons du devoir ; exposition annuelle de sculpture et jardin de sculptures. Modèle économique et chiffres : INCONNU (non indiqués).
- Lecture (ESTIMATION, à confirmer par R3) : l'apport est **gratuit et irrévocable** et le fonds doit poursuivre une mission d'intérêt général. C'est un outil de **transmission et de pérennisation** du domaine (et de collecte de mécénat), pas un moyen de financer une résidence privée : la jouissance privative du fondateur est a priori incompatible avec l'intérêt général. Un montage hybride (château ou parc ouvert au public porté par le fonds, logement privé conservé en propre) serait à étudier juridiquement.

### 7.6 Capital ou entreprise nécessaires pour produire 0,3 / 0,6 / 1,2 M€ par an de trésorerie disponible après impôts

Toutes les lignes sont des **ESTIMATIONS** calculées à partir des données sourcées ci-dessus et d'hypothèses explicites. Montants en M€ constants 2026.

| Véhicule | Hypothèse de rendement net d'impôt | 0,3 M€/an | 0,6 M€/an | 1,2 M€/an | Sources |
|---|---|---|---|---|---|
| Portefeuille financier diversifié détenu par un particulier | retrait réel net soutenable 3 % (bas) à 2,5 % (prudent) — HYPOTHÈSE §7.1 | 10 à 12 | 20 à 24 | 40 à 48 | [R8-31] [R8-32] [R8-34] |
| Repère « dotation universitaire américaine » (exonérée d'impôt) | 4,9 % de dépense effective — non applicable tel quel à un contribuable français | 6,1 | 12,2 | 24,5 | [R8-34] |
| SCPI détenues en direct (TMI 45 % + prélèvements sociaux 17,2 %) | 4,91 % × (1 − 0,622) ≈ 1,86 % net, avant IFI et frais d'entrée ; capital en érosion | ≈ 16 | ≈ 32 | ≈ 65 | [R8-29] |
| PME rachetée sans dette (dividendes : IS 25 % puis PFU 31,4 %) | 1 € de résultat avant impôt → 0,51 € net ; EBITDA ≈ 1,3 × résultat avant impôt (HYPOTHÈSE) | EBITDA ≈ 0,76 ; valeur ≈ 3,8 (5x, HYPOTHÈSE) à 6,0 (7,9x) | EBITDA ≈ 1,5 ; valeur ≈ 7,6 à 12,0 | EBITDA ≈ 3,0 ; valeur ≈ 15 à 24 | [R8-31] [R8-35] |
| PME rachetée avec dette d'acquisition (LBO) | trésorerie absorbée par le remboursement pendant 5 à 7 ans (HYPOTHÈSE) | ≈ 0 au début | ≈ 0 au début | ≈ 0 au début | [R8-36] |

Conditions de pérennité (synthèse) :
1. **Règle de dépense** fixe et lissée (par exemple un pourcentage d'une moyenne de valeur sur 3 ans, comme les dotations), avec réserve de liquidité pour les années de baisse ; ne jamais dépenser plus que le rendement réel net attendu.
2. **Diversification** : une seule PME concentre le risque (≈ 1 reprise sur 5 échoue en 6 ans, donnée 1997-2003) ; un portefeuille large réduit ce risque.
3. **Gouvernance indépendante du fondateur** : la PME doit être dirigée par un dirigeant salarié (rémunération à déduire), sinon le propriétaire n'a plus de temps pour le domaine.
4. **Fiscalité** : le taux de 31,4 % (2026) peut encore évoluer ; une détention via une holding à l'IS ou des enveloppes (assurance-vie) change le calcul (à modéliser avec R3).
5. **Inflation** : le budget du château croît avec l'inflation du BTP et des salaires ; le capital doit être investi en actifs réels pour suivre.
6. Le capital nécessaire (≈ 10 à 48 M€) suppose une fortune déjà constituée : ce « moteur » ne répond à la contrainte « sans recourir à la fortune personnelle » que si cette fortune est **séparée et affectée** au domaine (dotation dédiée), ou si l'entreprise est bâtie par le propriétaire avec son travail.

---

## 8. Autres pistes inhabituelles

### 8.1 CFA dans les métiers du cheval ou du patrimoine : niveaux de prise en charge (NPEC) 2026

- Référentiel unique des NPEC « applicables au 1er septembre 2026 », « conformément au Décret n° 2026-832 du 29 août 2026 » [R8-47] (fichier officiel téléchargé depuis francecompetences.fr [R8-48] et lu ; onglet « Global », montants en € par contrat, unité annuelle **à confirmer**) :

| Certification (RNCP) | Diplôme | NPEC – CPNE des entreprises équestres | NPEC – CPNE de l'agriculture | NPEC – CPNE du BTP |
|---|---|---|---|---|
| Palefrenier soigneur (RNCP38389) | CAPA | 6 324 € | 5 994 € | 6 137 € |
| Animateur d'équitation (RNCP37414/42622) | Titre | 7 101 € | 6 731 € | 6 576 € |
| Responsable d'entreprise hippique (RNCP40797) | BP | 7 150 € | 6 412 € | — |
| Conduite et gestion de l'entreprise hippique (RNCP38076) | Bac pro | 8 100 € | 7 633 € | — |
| Éducation et travail des jeunes équidés (RNCP39679/42019) | CS | 8 407 € | 8 202 € | — |
| Perfectionnement sportif mention sports équestres (RNCP39573) | DEJEPS | 10 550 € | 8 663 € | 8 663 € |
| Lad-cavalier d'entraînement (RNCP38387) | CAPA | 10 871 € | 10 871 € | 15 529 € |
| Maréchal-ferrant (RNCP38388) | CAPA | 5 669 € | 5 669 € | 7 928 € |
| Maçon du bâti ancien (RNCP39178) | TP | 7 745 € | 6 385 € | 7 745 € |
| Tailleur de pierre / Appareilleur monuments historiques (RNCP40194) | BP | 10 132 € | 10 132 € | 10 132 € |
| Ouvrier professionnel en restauration du patrimoine (RNCP37516) | Titre | 14 137 € | 14 137 € | 14 137 € |
| Interventions sur le patrimoine bâti (RNCP41014) | Bac pro | 8 444 € | 8 444 € | 8 444 € |
| Jardinier-paysagiste (RNCP38386) | CAPA | 4 033 € | 5 761 € | 5 761 € |

- Lecture (ESTIMATION) : le NPEC finance la formation (formateurs, locaux, plateau technique) ; ce n'est pas une marge. Ouvrir un CFA suppose une certification qualité, des formateurs, des salles et, pour l'équitation, un plateau technique et une cavalerie : une **activité à part entière**, avec flux quotidien d'apprentis. Une version légère consiste à **accueillir des apprentis** (palefreniers, jardiniers) comme employeur, ce qui réduit le coût du personnel du domaine (aides à l'embauche d'apprentis : montants 2026 non vérifiés, INCONNU).

### 8.2 Pôle d'artisans du patrimoine

- Exemple : Fondation de Coubertin [R8-46] (domaine de 80 ha, château, fonderie d'art, une trentaine de jeunes compagnons par an), porté par une fondation reconnue d'utilité publique depuis 1973. Loyers ou modèle économique : INCONNU. Aucun exemple de pôle d'artisans **locataires** dans les communs d'un château privé n'a été trouvé (pas de recherche dédiée).

### 8.3 Coaching par le cheval pour dirigeants

- **INCONNU** (pas de recherche dédiée, budget épuisé). Méthode : relever les tarifs publics de séminaires d'« équicoaching » (€ par participant et par jour) et le nombre de sessions par an d'un praticien. Activité compatible avec la passion équestre et à faible nuisance, mais dépendante d'un praticien certifié.

### 8.4 Partenariats avec des maisons de luxe

- **INCONNU** (pas de recherche dédiée). Les montants des locations pour défilés, shootings ou événements de marques ne sont généralement pas publics ; R7 traite les tournages et événements.
