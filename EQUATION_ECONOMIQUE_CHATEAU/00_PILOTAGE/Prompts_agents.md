# Missions détaillées des agents — Vague 1

Tous les agents commencent par lire :
- `00_PILOTAGE/Contexte_permanent.md` ;
- `00_PILOTAGE/Regles_agents.md`.

Avant le premier appel web, charge les outils avec ToolSearch : `select:WebSearch,WebFetch`.

Chemin racine : `/home/user/Ch-teau-/EQUATION_ECONOMIQUE_CHATEAU/`

Objectif commun : fournir des **données sourcées et chiffrées** qui permettront de construire :
- les budgets de fonctionnement S1, S2 et S3 ;
- les modèles de revenus.

Priorité aux chiffres exploitables, avec unité, année et périmètre, plutôt qu'aux généralités. Quand une donnée est introuvable, écris INCONNU et indique comment la vérifier.

---

## R1 — Coûts du bâti patrimonial

Fichier : `01_RECHERCHE/R1_couts_bati_patrimoine.md`. Sources : `01_RECHERCHE/sources/sources_R1.csv`.

### Questions

1. **Ratios globaux d'entretien des demeures historiques**
   - La Demeure Historique. Ouvre au moins :
     - https://www.demeure-historique.org/wp-content/uploads/2019/06/Note-DH-DNS-05062019.pdf (ordre de grandeur de 40 000 €/an minimum, à vérifier et à citer) ;
     - https://www.demeure-historique.org/wp-content/uploads/2022/05/La-transmission-des-monuments-historiques.pdf ;
     - https://www.demeure-historique.org/wp-content/uploads/2022/09/article-DH201-financement-public-des-travaux.pdf.
     Cherche aussi les études sur les dépenses annuelles de travaux des propriétaires privés.
   - Historic Houses (Royaume-Uni) : retard d'entretien (« repair backlog »), dépense moyenne de réparation par maison, structure des coûts.
   - National Trust, English Heritage et « Heritage Counts » : coûts d'entretien des bâtiments protégés.
   - Règles de pouce sourcées : entretien annuel en % de la valeur de reconstruction ou de restauration.
2. **Coûts de restauration par composant, en France, avec des exemples réels** : toiture en ardoise ou en tuile plate, charpente, maçonnerie en pierre de taille, menuiseries, façades, zinguerie, cheminées, réseaux (électricité, chauffage).
   - Donne des €/m² et des montants de chantiers datés : délibérations municipales, pages projets de la Fondation du patrimoine, presse.
   - Distingue un MH avec ACMH d'un bâtiment non protégé.
   - Durées de vie des composants (ardoise, zinc, charpente, menuiseries, installations techniques), selon des sources techniques.
3. **Énergie**
   - Consommations des bâtiments anciens (kWh/m²/an).
   - Exemples de coûts de chauffage de châteaux.
   - Prix 2025-2026 en France, sur sources officielles si possible : fioul (€/L), gaz (€/kWh), électricité (tarif réglementé), granulés (€/t), plaquettes forestières (€/MWh).
4. **Assurance** : exemples de primes pour châteaux et demeures (taux ou montants), assureurs spécialisés, responsabilité civile pour l'accueil du public.
5. **Taxe foncière** : exemples chiffrés de taxe foncière de châteaux et mode de calcul.
6. **Subventions de travaux**
   - Taux de la DRAC pour un monument classé ou inscrit, et base légale.
   - Cofinancements régionaux et départementaux.
   - Montants du programme 175.
   - Délais réels.
   - Fondation du patrimoine et Loto du patrimoine : montants par site.
7. **Imprévus** : sinistres (incendies, tempêtes), fréquence si elle existe, et pratique des provisions.
8. **Postes techniques récurrents** : sécurité (alarme, télésurveillance), contrôles obligatoires, paratonnerre, ramonage, assainissement, eau.

### Livrable

Un tableau de coûts annuels du bâti, au m² et par an, pour S1, S2 et S3. Distingue :
- l'entretien courant ;
- la provision de gros entretien ;
- l'énergie ;
- l'assurance ;
- les taxes ;
- les imprévus.

---

## R2 — Personnel, jardins, terres, équipements, chevaux

Fichier : `01_RECHERCHE/R2_couts_personnel_jardins_equestre.md`. Sources : `sources_R2.csv`.

### Questions

1. **Coût du travail 2025-2026**
   - SMIC horaire et mensuel au 1er janvier 2026, et revalorisations éventuelles en 2026.
   - Taux de cotisations patronales.
   - Réforme de la réduction générale en 2026.
   - Coût employeur chargé à 1, 1,5 et 2,5 SMIC.
2. **Grilles conventionnelles et salaires de marché**
   - Salariés du particulier employeur (employé de maison, gardien, gouvernante, jardinier).
   - Entreprises du paysage.
   - Centres équestres (soigneur, palefrenier, enseignant).
   - Production agricole.
   - Salaires de marché, tirés d'annonces ou d'agences spécialisées, pour : régisseur de domaine, chef jardinier, majordome ou house manager, gouvernante, responsable d'écurie, cavalier.
3. **Jardins et parc**
   - Nombre de jardiniers par hectare selon le type d'espace : jardin régulier, potager, parc paysager, prairie fauchée. Exemples : Villandry, Vaux-le-Vicomte, Chantilly, Versailles, Courances, jardins du National Trust.
   - Coûts d'entretien des espaces verts en €/m²/an (références des collectivités, Plante & Cité).
   - Tarifs de sous-traitance : tonte, taille de haies, élagage.
4. **Équipements** : prix et durée de vie des tondeuses autoportées, microtracteurs, tracteurs, véhicules utilitaires, camion ou van à chevaux, matériel de carrière. En déduire un budget de renouvellement.
5. **Terres**
   - Prix des fermages : arrêtés préfectoraux, Agreste.
   - Coût de production du foin et prix du foin et de la paille en 2024-2025 (€/t).
   - Entretien des prairies et des clôtures (€/ml et durée de vie).
   - Forêt : coûts de gestion et revenu net par hectare (CNPF, Fransylva, ONF).
6. **Chevaux**
   - Coût annuel d'un cheval : alimentation, foin (kg/jour), litière, maréchal-ferrant, vétérinaire, dentiste, assurance. Références IFCE.
   - Coût annuel d'un box en écurie professionnelle.
   - Ratio de personnel : chevaux par soigneur.
7. **Installations équestres**
   - Coût de construction d'un box, d'une carrière (€/m²) et d'un manège (€/m², par exemple 60 × 25 m).
   - Réfection du sol, entretien, éclairage, clôtures.
   - Durées de vie.
8. **Flux de l'écurie** : eau, électricité, gestion du fumier (réglementation, coût d'évacuation ou revente).

### Livrable

Des tableaux d'effectifs et de coûts chargés pour S1, S2 et S3, ainsi qu'un coût annuel par cheval et par box.

---

## R3 — Cadre fiscal et juridique

Fichier : `01_RECHERCHE/R3_cadre_fiscal_juridique.md`. Sources : `sources_R3.csv`.

Légifrance est bloqué (403). Utilise en priorité :
- BOFiP (bofip.impots.gouv.fr) ;
- impots.gouv.fr ;
- service-public.fr et entreprendre.service-public.fr ;
- culture.gouv.fr ;
- les rapports du Sénat, de l'Assemblée nationale et de la Cour des comptes ;
- les textes reproduits par des sources fiables (notaires, ordres professionnels).

Cite l'article de loi chaque fois que possible.

### Questions

1. **Régime fiscal des monuments historiques pour un propriétaire privé**
   - Déduction des charges : article 156 du CGI, articles 41 E à 41 J de l'annexe III.
   - Conditions d'ouverture au public (nombre de jours) et pourcentage de déduction (100 % ou 50 %).
   - Traitement des travaux subventionnés et des recettes de visites.
   - SCI (article 156 bis) et engagement de conservation de 15 ans.
   - Changements apportés par les lois de finances 2024, 2025 et 2026.
   - Label de la Fondation du patrimoine pour les bâtiments non protégés : taux et conditions actuelles.
2. **Transmission** : exonération de droits de mutation à titre gratuit avec convention (article 795 A du CGI).
3. **IFI**
   - Situation des MH (existe-t-il une exonération ?).
   - Abattement de 30 % sur la résidence principale.
   - Biens professionnels.
   - Château partiellement loué à une société d'exploitation.
4. **Mécénat**
   - Un MH privé peut-il recevoir des dons défiscalisés ? Conditions de la Fondation du patrimoine (convention, ouverture, affectation).
   - Fonds de dotation : un fonds peut-il porter un domaine habité par son fondateur ? Interdiction de l'avantage privé.
   - Mécénat d'entreprise : réduction de 60 % et conditions.
5. **Fiscalité des activités**
   - IS (15 % et 25 %).
   - Taux du prélèvement forfaitaire unique sur les dividendes en 2026 : vérifie la loi de finances 2026, dont toute hausse de la CSG sur les revenus du capital.
   - Régime mère-fille.
   - SCI à l'IR ou à l'IS.
   - Meublés de tourisme et LMNP : loi Le Meur de 2024, seuils et abattements du micro-BIC, loi de finances 2025.
   - Chambres d'hôtes : définition (5 chambres, 15 personnes) et fiscalité.
   - Toute taxe nouvelle sur les holdings patrimoniales détenant des biens non professionnels (loi de finances 2026).
6. **TVA 2025-2026**
   - Activités équestres : enseignement, pension, location d'installations, vente de chevaux. Le taux réduit a-t-il été rétabli ?
   - Hébergement, restauration.
   - Location de salle ou de lieu pour réception.
   - Droits d'entrée aux visites de monuments.
   - Location de terres nues.
   - Vente d'électricité.
7. **Statut agricole**
   - Activités équestres agricoles (article L311-1 du Code rural) et conséquences : bénéfices agricoles, MSA.
   - Statut du fermage et risque de requalification d'une location d'écurie ou d'une vente d'herbe en bail rural (jurisprudence).
   - Alternatives : convention de pâturage, prestations de services, bail commercial.
8. **Urbanisme et réglementation**
   - Changement de destination en zone A ou N (article L151-11 du Code de l'urbanisme), STECAL.
   - ERP : catégories, seuil de la 5e catégorie, obligations.
   - Accessibilité des personnes à mobilité réduite.
   - Bruit des musiques amplifiées (décret 2017-1244).
   - Abords des MH et avis de l'architecte des Bâtiments de France.
   - Sites classés.
   - Agrivoltaïsme : loi APER de 2023 et décret de 2024.
   - Petite hydroélectricité : droit fondé en titre, obligation d'achat.
   - Statut ICPE éventuel des écuries.
9. **Occupation privée d'un bien détenu par une société** : avantage en nature, loyer de marché, acte anormal de gestion, abus de biens sociaux, SCI familiale à l'IR pour la partie privée.
10. **Droit du travail** : saisonniers et temps de travail dans les secteurs agricole et équestre, seulement pour l'essentiel.

### Livrable

Une matrice « dispositif / effet chiffré / conditions / risque ». Ajoute une liste des points à faire valider par un avocat fiscaliste, un notaire ou un expert-comptable.

---

## R4 — Domaines français : modèles réels, comptes, réussites, échecs

Fichier : `01_RECHERCHE/R4_benchmark_france.md`. Sources : `sources_R4.csv`.

### Cas à étudier

Vise **12 à 20 cas documentés**.

- **Grands domaines privés ou fondations** : Vaux-le-Vicomte, Domaine de Chantilly (fondation, Grandes Écuries, musée du Cheval, déficits et soutien du mécène), Cheverny, Chenonceau, Villandry, Brissac, Courances, Breteuil, Champ de Bataille.
- **Domaines financés par un produit** : Château Smith Haut Lafitte et Caudalie, Château de Pommard, Puy du Fou comme exemple extrême.
- **Hôtellerie et événementiel** : Domaine des Étangs, châteaux-hôtels, lieux de réception exclusifs.
- **Financement participatif** : Château de la Mothe-Chandeniers.
- **Équestre** : Haras de Jardy, Haras du Pin, Pôle international du cheval de Deauville, haras privés normands (Etreham, Montaigu, Logis Saint-Germain, Quesnay, Bonneval, Fresnay-le-Buffard…), domaines équestres privés.

### Pour chaque cas

- Situation initiale et acquisition.
- Activités et chronologie.
- Visiteurs, chiffre d'affaires et résultat s'ils sont publiés. Les extraits de Pappers, societe.com ou verif.com vus en résultat de recherche ont le statut EXTRAIT ; essaie d'ouvrir la fiche de la société.
- Effectifs.
- Financement des restaurations.
- Difficultés rencontrées.
- Ce qui est transposable ou non.

**Sépare toujours la fortune du propriétaire de la rentabilité d'exploitation.**

### Échecs (au moins 5 cas sourcés)

- Liquidations de sociétés de château-hôtel, de lieu de réception ou d'écurie (BODACC, presse). Par exemple : la société exploitant un domaine équestre et hôtelier à Ygrande (Allier), qui aurait été liquidée en 2025, à vérifier.
- Châteaux revendus rapidement. La Demeure Historique évoque plus de 1 000 MH en vente et une durée moyenne de détention de 7 ans, à vérifier.
- Château de Gudanes.
- Château de la Motte-Husson (« Escape to the Chateau ») : modèle économique et difficultés publiques.

### Livrable

- Un tableau comparatif des cas.
- Les mécanismes économiques qui marchent et ceux qui échouent.

---

## R5 — Domaines étrangers : Royaume-Uni, Irlande, Italie, Espagne, États-Unis

Fichier : `01_RECHERCHE/R5_benchmark_international.md`. Sources : `sources_R5.csv`.

Companies House (find-and-update.company-information.service.gov.uk) et les rapports annuels des « charities » publiés en PDF donnent souvent des comptes réels. Essaie de les ouvrir.

### Cas à étudier

**Royaume-Uni**
- Blenheim Palace : fondation, recettes, visiteurs, diversification (immobilier résidentiel, énergie, événements).
- Chatsworth (Chatsworth House Trust).
- Burghley : la fondation de préservation et la société du Burghley Horse Trials.
- Badminton Horse Trials.
- Goodwood : société, chiffre d'affaires et résultat ; usine Rolls-Royce sur le domaine.
- Holkham.
- Highclere : effet Downton Abbey.
- Longleat.
- Castle Howard.
- Alnwick.
- Historic Houses (association) : structure des recettes des membres, retard d'entretien, et régime britannique des « maintenance funds ».

**Irlande** : Castle Leslie (hôtel et centre équestre), Adare Manor, Mount Juliet, Coolmore, Irish National Stud.

**Italie** : Castello di Reschio (famille Bolza : restauration et vente de fermes, services de gestion, hôtel, centre équestre). C'est un cas prioritaire, avec des chiffres si possible. Aussi Castiglion del Bosco.

**Espagne** : La Donaira (chevaux et hôtellerie).

**États-Unis** : Biltmore Estate (The Biltmore Company : recettes, visiteurs, effectifs, activités), haras du Kentucky (économie des étalons), Wellington en Floride (immobilier équestre).

### Ce qu'il faut en tirer

- Part des revenus locatifs (résidentiel et commercial) dans les grands domaines.
- Développement immobilier.
- Événements équestres.
- Tournages.
- Hôtellerie.
- Revenus de l'énergie.

Ajoute les difficultés et les échecs : maisons vendues ou cédées faute de moyens, dettes, hôtels en difficulté.

### Livrable

Un tableau comparatif et les mécanismes transposables en France, avec leurs limites juridiques (SAFER, urbanisme).

---

## R6 — Économie équestre

Fichier : `01_RECHERCHE/R6_economie_equestre.md`. Sources : `sources_R6.csv`.

### Questions

1. **Chiffres clés de la filière**
   - IFCE et Observatoire économique et social du cheval : effectifs d'équidés, établissements, emplois, poids économique.
   - Évolution des licences de la FFE.
2. **Références économiques des entreprises équestres**
   - Cas types de l'IFCE et du réseau REFErences : centre équestre, écurie de pension, élevage de chevaux de sport, valorisation, entraîneur.
   - Chiffre d'affaires, EBE, chevaux par ETP, revenu de l'exploitant.
3. **Pension**
   - Prix par région et par niveau de service en 2024-2026, en précisant TTC ou HT.
   - Haut de gamme près de Paris, Chantilly, Fontainebleau, Deauville.
   - Pension retraite.
   - Taux d'occupation et preuves de demande (listes d'attente, places vacantes).
4. **Location d'écuries à des cavaliers professionnels**
   - Prix d'un box ou d'une écurie.
   - Économie du commerce de chevaux.
   - Rentabilité de l'élevage de chevaux de sport.
   - Ventes aux enchères de chevaux de sport.
5. **Course et pur-sang**
   - France Galop et LeTrot : enjeux du PMU de 2022 à 2025, allocations, primes aux éleveurs et aux propriétaires (en %).
   - Ventes Arqana.
   - Services d'un haras : pension de poulinière (€/jour, en Normandie), poulinage, préparation des yearlings, commissions de vente.
   - Économie d'une station d'étalons (prix de saillie).
   - Comptes de haras (extraits).
6. **Services à forte valeur**
   - Centres de rééducation : tarifs.
   - Cliniques.
   - Centres de reproduction.
   - Quarantaine et export.
   - Transport.
   - « Hôtels à chevaux ».
7. **Événements équestres**
   - Économie d'un organisateur de concours : engagements, dotations, sponsors.
   - Budgets et subventions de grands événements : Mondial du Lion, Grand Complet du Haras du Pin, Pau, Jumping de Chantilly ou Longines, Saut Hermès, Dinard.
   - Polo : Polo Club du Domaine de Chantilly, Deauville (cotisations, recettes).
8. **Risques** : épizooties (rhinopneumonie de 2021), responsabilité, TVA, saisonnalité.

### Livrable

Un tableau des modèles équestres, avec pour chacun :
- le revenu par cheval ou par box ;
- la marge ;
- le personnel ;
- l'investissement ;
- la récurrence ;
- les preuves de demande.

Conclus : quel modèle équestre peut dégager une contribution nette au domaine ?

---

## R7 — Marchés de l'événementiel, de l'hébergement, des tournages et des visites

Fichier : `01_RECHERCHE/R7_marches_evenementiel_hebergement.md`. Sources : `sources_R7.csv`.

### Questions

1. **Mariages**
   - Nombre par an (INSEE, 2023-2025) et budget moyen.
   - Part des mariages en château ou en domaine.
   - Tarifs de location exclusive d'un château pour un week-end, par région et par gamme, en précisant HT ou TTC.
   - Saisonnalité.
   - Nombre de châteaux référencés sur les plateformes, ce qui mesure la concurrence.
   - Mariages de destination d'étrangers en France (Atout France, études).
   - Tendances.
   - Marges d'un lieu loué « nu ».
   - Comptes de sociétés de lieux de réception (extraits).
2. **Séminaires et événements d'entreprise** : taille du marché, prix d'une journée d'étude et d'un séminaire résidentiel en château, clients, saisonnalité.
3. **Tournages et prises de vue**
   - Tarifs de location par jour : grille du Centre des monuments nationaux, commissions du film, exemples.
   - Fréquence réaliste pour un château ordinaire.
   - Shootings de marques de luxe.
4. **Châteaux-hôtels**
   - Performances de l'hôtellerie de luxe à la campagne en 2024-2025 : prix moyen, occupation, RevPAR (MKG, In Extenso, Atout France).
   - Marge d'exploitation (GOP).
   - Coût d'investissement par chambre.
   - Contrats de gestion et loyers (en % du chiffre d'affaires).
   - Exemples de comptes et fermetures.
5. **Gîtes, chambres d'hôtes, grandes maisons**
   - Revenus moyens (Gîtes de France).
   - Effets de la loi Le Meur.
   - Location saisonnière de luxe de châteaux à la semaine (Le Collectionist et équivalents) : tarifs observés.
   - Gîtes de groupe.
6. **Hébergements insolites et glamping** : chiffre d'affaires par unité, occupation, investissement, réglementation.
7. **Visites**
   - Répartition de la fréquentation des MH privés (statistiques de La Demeure Historique).
   - Prix des billets.
   - Coûts d'ouverture.
   - Seuil de rentabilité.
   - Exemples chiffrés.
8. **Chocs** : effet de 2020 sur les mariages et l'événementiel (en %), rebond, assurance annulation.

### Livrable

Pour chaque activité :
- le chiffre d'affaires par unité ;
- la marge contributive ;
- l'investissement ;
- le personnel ;
- la saisonnalité ;
- l'impact sur la tranquillité ;
- l'intensité de la concurrence.

---

## R8 — Revenus non conventionnels, revenus fonciers et moteur extérieur

Fichier : `01_RECHERCHE/R8_revenus_non_conventionnels.md`. Sources : `sources_R8.csv`.

### Questions

1. **Revenus récurrents du foncier**
   - Loyer d'une centrale solaire au sol (€/ha/an, 2024-2026).
   - Agrivoltaïsme avec pâturage : règles, loyers, exemples avec des chevaux.
   - Hangars photovoltaïques financés par un tiers : conditions.
   - Petite hydroélectricité : tarifs et revenu type pour 30 à 300 kW.
   - Forêt : revenu net €/ha/an.
   - Location de chasse (€/ha/an, par région, en Sologne, grand ou petit gibier).
   - Crédits carbone : prix par tonne et volumes par hectare du Label bas-carbone.
   - Truffières : rendement, prix, délai, risques.
   - Sapins de Noël, vente de foin, fumier, miel.
2. **Stockage et locations peu intensives des dépendances**
   - Gardiennage de voitures de collection (€/mois).
   - Hivernage de camping-cars, caravanes et bateaux (€/an).
   - Stockage de vins de collection (€/caisse/an).
   - Garde-meubles et stockage d'œuvres d'art.
   - Pour chacun : demande, exemples, exigences de sécurité et d'assurance.
3. **Locations longues**
   - Loyers résidentiels ruraux (€/m²/mois).
   - Coût de transformation de bâtiments agricoles en logements ou en bureaux (€/m²).
   - Ateliers d'artisans et bureaux.
   - Domaines qui louent leurs dépendances, en France et au Royaume-Uni.
4. **Locataires institutionnels**
   - Écoles installées dans des châteaux : Institut Lyfe au château du Vivier, École Ducasse à Yssingeaux, Ferrières (à vérifier), pensionnats internationaux, colonies de vacances.
   - Centres de formation d'entreprise, fondations.
   - Montants de loyers connus, par exemple dans des délibérations publiques.
   - Studios de tournage.
5. **Clubs**
   - Clubs privés équestres, de polo, de golf ou de campagne : cotisations observées en France.
   - Modèle de Soho Farmhouse.
   - Effet sur la tranquillité.
6. **Libération de capital par l'immobilier**
   - Modèle de Castello di Reschio.
   - Équivalents français : division et vente de dépendances, hameaux.
   - Contraintes : SAFER, PLU, lotissement.
   - Démembrement de propriété (nue-propriété et usufruit) comme outil de financement.
7. **Moteur extérieur**
   - Taux de dépense soutenable d'une dotation perpétuelle (règles des fonds universitaires, rendements réels de long terme).
   - Fiscalité française des revenus financiers.
   - Rendements des SCPI en 2024-2025 (ASPIM).
   - Rendements de l'immobilier commercial et résidentiel.
   - Reprise de PME : multiples de valorisation (indice Argos), taux de défaillance des PME reprises, capacité de distribution.
   - Fonds de dotation ou fondation portant un domaine : règles et exemples.
8. **Autres pistes inhabituelles**, à n'inclure que s'il existe des preuves :
   - coaching par le cheval pour dirigeants ;
   - CFA dans les métiers du cheval ou du patrimoine (niveaux de prise en charge 2025-2026) ;
   - pôle d'artisans du patrimoine ;
   - partenariats avec des maisons de luxe.

### Livrable

Pour chaque piste :
- le revenu annuel réaliste pour S1, S2 ou S3 ;
- l'investissement ;
- la charge opérationnelle ;
- la récurrence ;
- les contraintes ;
- les preuves.

Pour le moteur extérieur : le capital ou l'entreprise nécessaires pour produire 0,3, 0,6 ou 1,2 M€ par an de trésorerie disponible après impôts, avec les conditions de pérennité.
