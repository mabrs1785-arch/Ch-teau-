# V2C — Budgets réels déclarés et leviers de « prestige efficace »

Agent : V2C (vague 2). Démarré le 2026-10-14. Fichier écrit au fur et à mesure.
Sources : `sources/sources_V2C.csv` (identifiants V2C-xx). Les sources des agents de la vague 1 sont citées par leur identifiant d'origine (R1-xx, R2-xx, R4-xx, R5-xx).

Rappels de méthode :
- statuts : PAGE LUE, EXTRAIT, ESTIMATION, HYPOTHÈSE, INCONNU ;
- ce qui figure déjà dans R1 (bâti, énergie, assurance) et R2 (salaires, Villandry, synthèse des effectifs) n'est pas refait ; seuls les compléments sont ajoutés ;
- budget à confronter (vague 1) : S1 ≈ 0,33 M€, S2 ≈ 1,23 M€, S3 ≈ 3,4 M€ par an, tout compris avec provisions.

## Résumé

1. **Budgets déclarés** : aucun budget complet de domaine privé de taille S2 n'est publié en France ou en Belgique. Les cas réels sont partiels (énergie de 4 000 à 50 000 €/an, chantiers de 40 000 € à 1 M€) ou hors d'échelle (Vaux-le-Vicomte 8-9 M€/an, Chambord ≈ 30 M€/an). La seule évaluation d'ensemble (IGF-IGAC, 2020) chiffre la dépense des propriétaires privés de MH à au moins 535 M€/an (≈ 24 000 € par monument en moyenne) et juge leur modèle « de plus en plus difficilement viable ».
2. **Dépensé contre nécessaire** : les propriétaires réels dépensent moins que le besoin (retards d'entretien, monuments en péril). Le budget S1 (0,33 M€) dépasse de 4 à 22 fois les charges déclarées de petits châteaux : c'est un budget nécessaire, que les cas réels ne peuvent ni valider ni contredire. S3 (3,4 M€) reste inférieur aux deux seules références de grande taille (Vaux 8-9 M€ ; Chatsworth ≈ 6,7 M€ d'entretien), qui sont des sites de visite de masse : ordre de grandeur plausible, non validé.
3. **Ratios de jardiniers** : de 0,06 ETP/ha (parc extensif) à 1,4-1,7 ETP/ha (jardin très fleuri) ; jardin régulier de prestige ≈ 0,7-0,8 ETP/ha (Rennes, Vaux, Chatsworth). Appliqués aux scénarios, ils montrent que les 11 jardiniers de S3 retenus par R2 sont sous-estimés d'au moins 40 % (15,7 à 33,4 ETP selon le zonage).
4. **Leviers** : la gestion différenciée et la fauche tardive sont les seuls leviers qui changent l'ordre de grandeur (jusqu'à −89 % de main-d'œuvre par hectare converti ; ≈ −67 000 €/an en S2 et ≈ −445 000 €/an en S3 par rapport à un parc soigné partout). Les leviers énergétiques (bois, isolation, régulation) pèsent moins de 2 % des budgets S2 et S3. Plusieurs effets restent INCONNUS (buis, groupement d'employeurs, prix de la sous-traitance).
5. **Dérives sur 20 ans (INSEE)** : SMIC ≈ +0,4 %/an réel ; entretien du bâti +0,7 %/an réel (couverture +1,3 %) ; électricité +2,0 %, gaz +4,8 %, fioul +1,9 %, bois +0,9 %/an réel ; assurance habitation +1,9 %/an réel, avec +12,6 % en 2025.

---

## Journal d'avancement

- Lecture du contexte, des règles, de la mission V2C, des sections utiles de R1, R2, R4 et R5.
- Séries longues INSEE téléchargées par l'API officielle (BDM, SDMX) et calculées localement (script en annexe A) : question 4 traitée en premier, car elle ne consomme aucune recherche web.
- Questions 1 à 3 : 10 WebSearch, 41 WebFetch, téléchargements locaux de PDF (pdftotext) et lecture des Baromètres de Plante & Cité par leur API.
- Rédaction des sections finales et réorganisation du fichier (ordre 1, 2, 3, 4).

---

## 1. Budgets annuels déclarés : cas réels (France, Belgique, comparaison britannique)

### 1.1 Constat général

Les budgets **complets** déclarés par des propriétaires privés (tous postes, avec effectifs et surfaces) sont **très rares** dans les sources publiques. Trois recherches web ciblées (n° 1, 2 et 4), le rapport IGF-IGAC et les documents de la Demeure Historique n'ont donné que des montants **partiels** (énergie, un chantier, un poste). Le seul budget complet d'un grand domaine privé français reste celui de Vaux-le-Vicomte, déjà relevé par R4 [R4-30] [R4-31]. L'« enquête Tournelle » (DH, 2010, 513 monuments) n'est pas publiée en détail (R1, R4). Le dossier « Le financement privé des travaux » de la revue de la Demeure Historique (n° 202) a été lu : il traite du mécénat et du financement participatif et ne contient aucun budget annuel de propriétaire [V2C-10].

### 1.2 Rapport IGF-IGAC de février 2020 : la seule évaluation publique d'ensemble [V2C-07] — PAGE LUE (PDF, texte extrait localement)

- **Dépense totale des propriétaires privés** (p. 21) :
  > « Pour l'année 2016 (impôts payés en 2017), le premier montant est d'au moins 340 M€ et le second estimé à 195 M€ […]. Et encore ne tiennent-ils pas compte des charges non déductibles ni des propriétaires qui déclarent un bénéfice foncier. […] On peut donc considérer que les charges et travaux payés par les propriétaires de MH sont d'au moins 535 M€ par an. »
  Les monuments privés représentent « près de la moitié des 44 000 immeubles protégés » (synthèse). ESTIMATION : 535 M€ / ≈ 22 000 monuments privés ≈ **24 000 € par monument et par an en moyenne**, plancher (charges non déductibles exclues), tous types confondus (de la façade inscrite au grand château). Ce n'est **pas** un budget de grand domaine.
- **Aide publique** : « de l'ordre de 30 à 35 M€ par an » pour le patrimoine privé ; dépense fiscale « 84 M€, c'est-à-dire au plus 16 % » de la dépense des propriétaires (synthèse).
- **Subvention** : « la subvention de la DRAC est en moyenne de 30 % et n'excède jamais 50 % du coût total » (note 26, p. 9).
- **Cycle des toitures** : « les conservateurs des monuments historiques interrogés par la mission estiment que les toitures d'un monument doivent être restaurées tous les 70/80 ans » (note 25, p. 9).
- **Chantiers réels** (note 40, p. 21) : « Château de M, projet de réfection des toitures du châtelet, estimé à 350 000 euros » ; « Château de C, tour en 2008 : 370 000€, 40% d'aide de l'État » ; « Château de D, tour en 2015 : 450 000€, 40% d'aide de l'État » ; « Château de B, réfection des toitures et parties hautes, travaux sur les murs et les communs, 2003-2014 : 1,7M€ » ; pour le château de C, reste à charge « de 200 000 à 270 000 euros ».
- **Enquête de la Demeure Historique pour la mission** (187 propriétaires, 157 châteaux ou manoirs, p. 49-50) : « 60% ont moins de mille visiteurs par an et seulement 6 % plus de dix mille » ; « Sur 118 réponses, le chiffre d'affaires de la visite est inférieur à 5.000 euros pour 77, soit les deux tiers des répondants » ; « Même pour ceux, très rares, qui ont plus de 20.000 euros de recettes annuelles, cela ne représente que quelques dizaines de mètres carrés de toiture. »
- **Typologie des propriétaires** (p. 49), utile pour situer le projet :
  - « Résident » : « Moins de 1 500 visiteurs par an. Exploitation déficitaire. Propriétaire rémunéré par son activité professionnelle. S'il n'est pas fortuné, a du mal à - ou ne peut pas - assurer sa quote-part des travaux de restauration. »
  - « Artisan » : « 10 000 à 20 000 visiteurs payants » ; « Ne peut subvenir qu'à l'entretien courant et ne peut financer sa quote-part des gros travaux que s'il y affecte une partie de son patrimoine ou de ses revenus fonciers. »
  - « Startuper » : « Plusieurs dizaines de milliers de visiteurs. Exploitation bénéficiaire ou ayant vocation à le devenir rapidement. […] Sinon, revente envisageable. »
  - « Industriel » : « Plusieurs centaines de milliers de visiteurs. Exploitation rentable qui permet de financer l'entretien courant et de rémunérer le travail du propriétaire. »
  - La typologie exclut « les propriétaires très fortunés qui n'ont au demeurant pas besoin de faire visiter leur bien pour en alléger les charges ».
- **Rotation** : « plus de cinq cents châteaux et demeures historiques seraient actuellement mis à la vente et la durée moyenne de détention d'un monument après son acquisition serait tombée à sept ans » (p. 9, selon des agences immobilières ; chiffre non vérifié par la mission elle-même).

Lecture (ESTIMATION) : le projet de la mission (résidence privée calme, sans visite de masse) correspond au profil « résident » ou « artisan ». Le rapport public le plus complet dit que ces profils **ne financent pas leur quote-part des gros travaux** sans patrimoine ou revenus extérieurs.

### 1.3 Montants partiels déclarés par des propriétaires ou gestionnaires

- **Château de Meung-sur-Loire (Loiret, privé, ouvert à la visite)** [V2C-09], PAGE LUE (dépêche AFP, octobre 2022) : facture habituelle de chauffage, gaz et électricité de « 15 000 à 20 000 euros » avant la crise de 2022 ; hausse attendue : « Ça va être multiplié entre cinq et dix » ; environ les deux tiers de la superficie chauffés, en priorité les pièces visitées ; une fenêtre refaite selon le cahier des charges validé avec la DRAC coûte environ 10 000 €, et le château en compte 148.
- **Château de Cheverny (Loir-et-Cher, privé, ≈ 350 000 visiteurs selon R4)** [V2C-09], PAGE LUE : 30 000 à 40 000 litres de fioul par an ; aucune isolation prévue, chauffage réduit au minimum. ESTIMATION : à 10 kWh PCI par litre de fioul (HYPOTHÈSE de conversion usuelle), soit ≈ 300 à 400 MWh/an ; au prix 2023 de 12,6 c€ TTC/kWh [R1-22], ≈ 38 000 à 50 000 € TTC/an.
- **Domaine national de Chambord (public)** [V2C-09], PAGE LUE : budget d'environ 30 M€ par an ; facture d'énergie passée de 260 000 € à « plus de 600 000 » € dans le budget prévisionnel 2023 ; gestion technique centralisée qui abaisse le chauffage la nuit à 8 °C ; objectif de −10 % de consommation dès 2023 ; études de biomasse, géothermie et photovoltaïque, avec une scierie prévue pour valoriser le bois du domaine.
- **Château de Louvignies (Soignies, Belgique, privé, non classé)** [V2C-08], PAGE LUE (RTBF, mars 2025) : « l'entretien des 14 hectares de terrain » ; « Le chauffage coûte environ 4000 euros par hiver » ; rénovation de la toiture d'une tourelle « pour 40.000 euros » et d'un vitrail « pour 16.000 euros » ; château non classé, donc sans subvention.
- **Château de Trazegnies (Corroy-le-Château, Belgique)** [V2C-08], PAGE LUE : « La restauration du pont menant au château pourrait coûter un million d'euros » ; l'aide publique « peut couvrir jusqu'à 75% des travaux » si le château est classé comme patrimoine exceptionnel et accessible au public.
- **Agence Barnes (Belgique)** [V2C-08], PAGE LUE : « ces charges annuelles varient entre 20.000 et 80.000 euros, en fonction de l'état et de la taille du bien ». Estimation d'agence immobilière, sans surface ni postes : fiabilité faible, et vraisemblablement hors gros entretien (HYPOTHÈSE de lecture).

### 1.4 Tableau des cas réels (France, Belgique ; comparaison britannique)

Conversion des livres : 1 £ = 1,185 € (taux BCE du 14 octobre 2026, repris de R1 [R1-37]).

| Cas | Statut, taille | Effectif | Montant annuel déclaré | Postes couverts | Dépensé ou nécessaire | Année | Statut de la donnée | Source |
|---|---|---|---|---|---|---|---|---|
| Vaux-le-Vicomte (77) | privé (SCI) ; 33 ha de jardins, parc de 500 ha ; ≈ 300 000 visiteurs | « 70 personnes » (2016) ; 75 temps plein (Wikipédia, non daté) | 9 M€ « à trouver chaque année pour son entretien » (8 M€ selon Wikipédia) ; jardins et bassins : 10 % | tout le domaine, exploitation de la visite comprise | besoin déclaré (dépensé de fait) | 2016 | PAGE LUE | [V2C-24] [R4-30] [R4-31] |
| Domaine national de Chambord (41) | public ; forêt de 50 km² | INCONNU | budget ≈ 30 M€ ; énergie 260 000 € → « plus de 600 000 » € | tout ; énergie | dépensé, puis prévu (budget 2023) | 2022 | PAGE LUE | [V2C-09] |
| Château de Meung-sur-Loire (45) | privé, ouvert à la visite | INCONNU | énergie 15 000 à 20 000 € (avant 2022) ; 148 fenêtres à ≈ 10 000 € pièce | énergie ; menuiseries | dépensé ; nécessaire | 2022 | PAGE LUE | [V2C-09] |
| Château de Cheverny (41) | privé ; ≈ 350 000 visites (R4) | 20 à 49 salariés (SCI, R4) | 30 000 à 40 000 L de fioul (≈ 38 000 à 50 000 € TTC, ESTIMATION) | chauffage | dépensé | 2022 | PAGE LUE | [V2C-09] [R4-03] |
| Château de Louvignies (Soignies, BE) | privé, non classé ; 14 ha | INCONNU | chauffage ≈ 4 000 €/hiver ; tourelle 40 000 € ; vitrail 16 000 € | chauffage ; travaux ponctuels | dépensé ; nécessaire | 2025 | PAGE LUE | [V2C-08] |
| Château de Trazegnies (BE) | privé | INCONNU | pont ≈ 1 M€ ; aide « jusqu'à 75% » si classé et ouvert | travaux | nécessaire | 2025 | PAGE LUE | [V2C-08] |
| Agence Barnes (BE), estimation générale | châteaux en général | — | charges annuelles de 20 000 à 80 000 € | charges courantes (postes non précisés) | estimation d'agence | 2025 | PAGE LUE, fiabilité faible | [V2C-08] |
| Ensemble des MH privés (FR) | ≈ 22 000 monuments (≈ moitié de 44 000) | — | ≥ 535 M€/an, soit ≈ 24 000 €/monument (ESTIMATION) | charges et travaux non subventionnés déclarés au fisc | dépensé (plancher) | 2016-2017 | PAGE LUE | [V2C-07] |
| Châteaux « B », « C », « D » (FR, anonymes) | MH | — | tours : 370 000 € (2008) et 450 000 € (2015) ; toitures et communs : 1,7 M€ sur 2003-2014 (≈ 155 000 €/an, ESTIMATION) | gros travaux | dépensé | 2003-2015 | PAGE LUE | [V2C-07] |
| Monument privé moyen (DH) | adhérents DH | « pas de personnel autre qu'eux-mêmes » le plus souvent | ≥ 40 000 €/an | assurance, impôts locaux, gardien, entretien minimum ; hors restauration | dépensé (moyenne) | 2019 | PAGE LUE | [R1-01] |
| Petit château MH (62), annonce de vente | 512 m² habitables, 6,56 ha | — | ≈ 14 600 €/an (chauffage 3 978 €, assurance 2 198 €, taxe foncière 2 652 €, personnel 4 163 €) | charges courantes sans gros entretien | déclaré par le vendeur | non daté | PAGE LUE, fiabilité faible | [R1-32] |
| Maisons historiques britanniques (n = 121) | 82 % Grade I et II* | — | 156 067 à 160 686 £ TTC (≈ 185 000 à 190 000 €) pour le seul bâtiment principal ; retard moyen ≈ 1 994 000 £ | entretien et réparation | dépensé (insuffisant) contre nécessaire | 2024 | PAGE LUE | [R1-05] |
| Kingston Russell House (RU) | Grade I, « small », non ouverte ; jardins de 6 acres (≈ 2,4 ha) | jardinier professionnel « at least 4 days a week » | 12 000 à 20 000 £/an + 50 000 à 100 000 £ tous les ≈ 10 ans | réparations | dépensé | 2024 | PAGE LUE | [R1-05] |
| Boughton Monchelsea Place (RU) | Grade I, 12 chambres, événements | — | maison : « tens of thousands » £/an ; jardins ≈ 75 000 £/an (personnel et matériel) | réparations ; jardins | dépensé | 2024 | PAGE LUE | [R1-05] |
| Chatsworth (RU), charity | bail de ≈ 1 822 acres (≈ 737 ha) ; jardin de 105 acres ; 630 114 visiteurs | 170 en moyenne, dont 29 aux jardins et 32 à la maintenance | jardin, parc et bois 1 781 k£ ; maison et écuries 2 705 k£ ; réparations 1 207 k£ ; assurance 342 k£ | entretien complet | dépensé | 2024-25 | PAGE LUE | [R5-05] |
| Breteuil (78) ; Courances (91) | 75 ha ; parc de 86 ha (domaine ≈ 1 800 ha, EXTRAIT) | ≈ 10 ; 6 à 9 (SCI du parc) | INCONNU | — | — | 2020-2024 | PAGE LUE (effectifs) | [R4-13] [R4-82] [R4-12] |

### 1.5 Confrontation avec les budgets calculés S1, S2 et S3 (ESTIMATION)

- **S1 (≈ 0,33 M€/an)** : les montants déclarés pour des châteaux de cette taille sont de **15 000 à 80 000 €/an** de charges courantes (annonce de vente, Barnes, plancher DH), hors gros travaux. S1 est donc **4 à 22 fois** au-dessus du « dépensé » observé (ESTIMATION : 330 000 / 80 000 ≈ 4 ; 330 000 / 15 000 ≈ 22). L'écart s'explique par trois postes que les propriétaires réels ne paient pas ou ne provisionnent pas : le personnel (≈ 77 000 € en S1, R2), la provision de gros entretien (≈ 100 000 € centrale, R1) et le niveau d'entretien « d'exception ». Les cas réels montrent la conséquence de cette non-provision : retard d'entretien (≈ 2 M£ par maison au Royaume-Uni), monuments en péril à 42,9 % privés pour 37,4 % du parc protégé [V2C-07], chantiers de 370 000 à 450 000 € pour une seule tour [V2C-07]. S1 est un budget **nécessaire**, pas un budget **observé** : les cas réels ne le contredisent pas, mais ne peuvent pas le valider.
- **S2 (≈ 1,23 M€/an)** : **aucun budget complet** de domaine privé de cette taille n'a été trouvé, en France comme en Belgique. Seuls repères : une maison britannique moyenne dépense ≈ 185 000 à 190 000 € pour son seul bâtiment principal ; Boughton Monchelsea ≈ 89 000 € pour ses jardins (ESTIMATION : 75 000 £ × 1,185). S2 reste une ESTIMATION non validée par un cas réel.
- **S3 (≈ 3,4 M€/an)** : les deux seules références de grande taille sont **au-dessus**, pour des sites plus vastes et ouverts à la visite de masse. Vaux-le-Vicomte : 8 à 9 M€, 70 à 75 personnes, 33 ha de jardins, ≈ 300 000 visiteurs. Chatsworth : ≈ 2,1 M€ pour les jardins, le parc et les bois et ≈ 4,6 M€ pour l'entretien courant et les réparations de la maison et des écuries, soit ≈ 6,7 M€ (ESTIMATION : (1 781 ; 2 705 + 1 207) k£ × 1,185), pour ≈ 630 000 visiteurs. Pour les jardins de S3, le coût par hectare de Vaux (≈ 24 000 à 27 000 €/ha/an) appliqué aux 10 ha réguliers donne ≈ 0,24 à 0,27 M€/an, auxquels s'ajoute le parc (§ 3.3). L'ordre de grandeur de S3, pour un domaine fermé au public, est donc **plausible**, sans validation directe.
- **Dépensé contre nécessaire** : les seules sources qui distinguent les deux (Historic Houses, rapport IGF-IGAC) concluent que la dépense réelle est **inférieure** au besoin. Un modèle calé sur des dépenses déclarées sous-estimerait donc le coût d'un entretien « d'exception ».

---

## 2. Leviers de réduction du coût sans perte de prestige

Principe tiré des sections 3 et 4 (ESTIMATION) : le premier levier est le **choix du niveau de soin par zone**. Il fait varier la main-d'œuvre de jardinage d'un facteur 2 à 3 sur un grand parc. Les leviers énergétiques pèsent, eux, quelques milliers à quelques dizaines de milliers d'euros par an.

### 2.1 Espaces verts

**a) Gestion différenciée (zonage du niveau de soin)** — [V2C-21] PAGE LUE ; [V2C-11] PAGE LUE ; [V2C-15] EXTRAIT.
- Rennes (2012) : 800 h/ha/an en code 3, 250 en code 4, 90 en code 5 (§ 3.1). ESTIMATION : passer 1 ha du code 3 au code 4 économise 550 h/ha/an (−69 %), soit ≈ 11 100 €/ha/an au coût R2.
- Liffré (2021) : code 1 « Tonte ramassage (h=40 mm) […] Tous les 15 jours » ; code 2 « Tonte en mulching (h=60mm) […] Tous les 2/3 semaines » ; code 3 « Fauche 1 à 2 fois par an avec évacuation, zones d'éco-pâturage ».
- Dumbéa (Nouvelle-Calédonie, 2026) annonce une baisse attendue des coûts de 20 à 40 % : communiqué non lu (403), sans méthode : fiabilité faible.
- Effet sur les scénarios (§ 3.3, ESTIMATION) : S2 passe de 8 800 à 5 500 h/an, soit de 5,5 à 3,4 ETP (≈ −67 000 €/an) ; S3 de 53 600 à 31 600 h/an, soit de 33,4 à 19,7 ETP (≈ −445 000 €/an).
- Conditions pour garder le prestige (HYPOTHÈSE de conception) : codes 1-2 réservés aux abords du logis, aux parterres et aux grandes perspectives ; prairies et sous-bois au-delà. C'est d'ailleurs la composition classique d'un domaine (jardin régulier près du château, parc et bois au-delà, cf. Vaux : 33 ha de jardins dans 500 ha de parc [V2C-25]).

**b) Fauche tardive (prairies au lieu de pelouses)** — [V2C-21] [V2C-11] PAGE LUE ; [R2-30].
- Code 4 → code 5 : −160 h/ha/an (−64 %), ≈ 3 200 €/ha/an ; code 3 → code 5 : −710 h/ha/an (−89 %), ≈ 14 400 €/ha/an (ESTIMATION).
- Fréquence : 1 à 2 fauches par an [V2C-11] au lieu d'une tonte tous les 15 jours à 3 semaines.
- Condition : le matériel de fauche coûte cher s'il sert peu (R2 : faucheuse 30,2 €/ha sous 100 ha/an contre 6,6 €/ha au-delà de 250 ha/an [R2-30]). Il vaut mieux confier la fauche à un agriculteur voisin ou à une entreprise, ou la faire avec le matériel déjà utilisé pour le foin des chevaux (HYPOTHÈSE).
- Synergie possible avec l'écurie : le foin des prairies du parc peut nourrir les chevaux (HYPOTHÈSE : la valeur alimentaire d'un foin fauché tard est plus faible, non chiffrée ici).

**c) Éco-pâturage (moutons, chèvres ; chevaux du domaine)** — [V2C-13] [V2C-14] PAGE LUE.
- Avignon (2020) : convention de 3 ans avec un éleveur ; 13 ha sur 9 sites ; 75 animaux (« 65 moutons et brebis et 10 chèvres ») du 16 mai au 31 octobre ; « 7 / ha » en début de saison, jusqu'à « 25 moutons/ha » ; coût pour la Ville : « 0 » ; « économie annuelle estimée à plus de 12 000 euros », sur la base « du taux horaire des agents, l'investissement des machines et leur entretien, le carburant ». ESTIMATION : ≈ 920 €/ha/an économisés, du même ordre que le coût d'un code 5 (≈ 1 800 €/ha/an de main-d'œuvre à Rennes).
- Rouen (2016) : la Métropole met « gratuitement à disposition » des herbages pour des éleveurs, associations ou particuliers.
- Conditions et risques : clôtures, eau et surveillance (à la charge de l'éleveur à Avignon) ; protection des arbres ; refus de pâturage à faucher. **Risque juridique** (leçon 5 du contexte) : une mise à disposition de terres à un éleveur peut être requalifiée en bail rural si elle comporte une contrepartie : à confirmer par R3. Pâturage par les chevaux du domaine dans le parc : effet non chiffré (INCONNU).

**d) Buis malades (pyrale, champignons)** — [V2C-25] [V2C-34] PAGE LUE ; EXTRAIT du résultat de recherche n° 7.
- Cas réel : Vaux-le-Vicomte, « En 2019, le domaine a procédé au remplacement des buis des parterres des boulingrins par une œuvre d'art temporaire : les Rubans Éphémères », faite de « 390 plaques d'aluminium inclinées » [V2C-25]. La page ne donne ni la cause ni le coût.
- Méthodes citées par une association de jardins (2015) : traitement « insecticide bio à base de bacillus thu[ringiensis] » quand les buis sont nombreux, ramassage à la main sinon ; « vous pouvez essayer l'ilex crenata ou houx crénelé voisin du buis » [V2C-34].
- Limite : d'après le résultat de recherche (bulletin de santé du végétal de la DRAAF Bretagne, mars 2024, non ouvert), la pyrale a aussi attaqué *Ilex crenata* en France. Le remplaçant n'est donc pas immunisé (EXTRAIT).
- Coût d'un traitement annuel ou d'un remplacement au mètre linéaire : **INCONNU**. Pour vérifier : devis d'entreprise ; programme SaveBuxus de Plante & Cité.
- Condition patrimoniale : dans un jardin protégé, le remplacement d'essence ou de motif relève d'une autorisation (à confirmer par R3).

**e) Sous-traitance contre salariat** — [V2C-20] [V2C-05] PAGE LUE ; [R2-30] ; [R2-13].
- Dérive : les prix des services d'aménagement paysager ont crû de 1,84 %/an de 2010 à 2025 (tous marchés), le SMIC de 2,0 à 2,2 %/an (§ 4). Sur longue période, aucune des deux formules ne dérive nettement plus vite que l'autre.
- Niveau : coût salarié d'un jardinier ≈ 20,24 €/h (R2). Prix horaire d'une entreprise du paysage : **INCONNU** (aucun barème public fiable lu). Pour vérifier : trois devis, ou BPU de marchés publics.
- Matériel : son coût horaire chute avec l'usage (R2, réseau CUMA : broyeur d'accotement 56,4 €/h sous 50 h/an contre 14,3 €/h au-delà de 150 h/an ; tracteur 34,4 €/h sous 400 h/an contre 19,1 €/h au-delà de 700 h/an [R2-30]).
- Règle proposée (ESTIMATION) : salarier le soin quotidien des zones de prestige (présence, sécurité, savoir-faire) ; sous-traiter les tâches saisonnières à gros matériel (fauche, élagage, grandes haies, broyage).
- Le crédit d'impôt pour l'emploi à domicile (50 % de 5 000 € de dépenses de jardinage au plus [R2-13]) est marginal à cette échelle.

**f) Mutualisation de personnel (groupement d'employeurs) et de matériel** — [V2C-29] PAGE LUE.
- Cadre : « Un groupement d'employeurs peut être constitué entre plusieurs entreprises » pour embaucher des salariés et les mettre à disposition de ses membres ; « Le salarié bénéficie de l'égalité de traitement par rapport aux autres salariés » des entreprises utilisatrices (fiche vérifiée le 12 juin 2026 ; articles L1253-1 et L1253-9 à L1253-15 du Code du travail).
- Conséquence (ESTIMATION) : le gain ne vient pas d'un salaire plus bas (égalité de traitement), mais du partage de compétences rares (arboriste, chef jardinier, responsable d'écurie) et de l'emploi à temps plein de besoins à temps partiel.
- Effet chiffré : **INCONNU** (aucun cas de groupement entre domaines trouvé). Accès d'un particulier employeur à un groupement : INCONNU ; le domaine doit sans doute être exploité par une société (HYPOTHÈSE, à confirmer par R3).

### 2.2 Énergie

**g) Chaudière bois ou plaquettes du domaine, réseau de chaleur** — [V2C-32] [V2C-33] EXTRAIT ; [V2C-30] [V2C-31] [V2C-04] [V2C-09] PAGE LUE.
- Cas réels de petites chaufferies (fiches ADEME PACA et chambre d'agriculture, vues seulement en extrait, pages refusées en lecture) : Saignon (84), 100 kW, « Économie par rapport à la solution de référence fioul : 10 927 €/an », avec une aide de l'ADEME de 28 500 € ; Luceram (06), 90 kW, économie ≈ 7 800 €/an pour un investissement de 245 000 € HT et 31 % de subventions ; Selonnet (04), 110 kW, investissement de 79 718 € HT, fioul ≈ 10 000 € TTC/an auparavant, économie nette ≈ 7 700 €/an ; Notre-Dame du Laus (05), 2 × 200 kW, économie prévisionnelle de 35 000 €/an. Retour simple sur investissement brut (ESTIMATION) : ≈ 10 ans (Selonnet) à ≈ 31 ans (Luceram, avant subventions).
- Dérive de prix favorable : bois et granulés +0,9 %/an réel sur 20 ans, contre +1,9 % pour le fioul et +4,8 % pour le gaz (§ 4.1).
- Ressource du domaine : production nette des forêts françaises « 4,4 m³/ha/an » en moyenne (2014-2022), de « moins de 1 à plus de 7 » selon les régions [V2C-30]. ESTIMATION : S2 (30 ha de bois) ≈ 130 m³/an d'accroissement net ; S3 (120 ha) ≈ 530 m³/an. La part utilisable en plaquettes (le reste étant du bois d'œuvre mieux valorisé) est **INCONNUE**.
- Ordre de grandeur des besoins (ESTIMATION) : dans le Morvan, ≈ 70 000 t de bois par an équivalent à 19 millions de litres de fioul [V2C-31], soit ≈ 270 litres de fioul par tonne de plaquettes. Les 30 000 à 40 000 litres de fioul de Cheverny [V2C-09] correspondraient à ≈ 110 à 150 t de plaquettes par an.
- Conditions : local de chaufferie, silo, réseau enterré jusqu'au château (autorisations en abords ou sur un MH), main-d'œuvre de déchiquetage et de manutention (coût **INCONNU**), appoint au fioul. Chambord étudie « le chauffage à la biomasse, avec une scierie prévue pour valoriser le bois » [V2C-09].

**h) Isolation des combles** — [R1-09] [R1-05] [V2C-27] PAGE LUE.
- Effet annoncé (propos oral du directeur général des patrimoines, sans étude citée) : « Si les combles sont isolés, on peut gagner 60% de la consommation énergétique » [R1-09].
- Obligation : l'isolation est obligatoire lors d'une réfection d'« au moins 50 % de l'ensemble de la couverture », mais les « Monuments historiques classés ou inscrits à l'inventaire » sont exclus. Une dispense existe aussi si le « temps de retour sur investissement est supérieur à 10 ans » [V2C-27]. Pour un château non protégé (cas possible en S1), l'isolation devient donc obligatoire à la prochaine grande réfection de toiture.
- Contre-témoignage : pour une maison classée Grade I, « it is impossible to increase the insulation or to draught-proof effectively within listed-building constraints » [R1-05].
- Effet chiffré (ESTIMATION, borne haute) : appliqué à l'énergie centrale de R1 (S1 17 800 €, S2 39 100 €, S3 70 400 € TTC/an), un gain de 60 % donnerait au plus ≈ 10 700 €, 23 500 € et 42 200 €/an. Le gain réel sur un château dont seule une partie est chauffée sous les combles est **INCONNU**. Coût des travaux : INCONNU (R1).

**i) Zonage et régulation du chauffage** — [V2C-26] [V2C-09] PAGE LUE.
- ADEME, citée par Service-public (février 2026) : une régulation automatique par pièce « peut entraîner jusqu'à 15 % d'économie d'énergie de chauffage ». Obligation pour les logements existants reportée au 1er janvier 2030 (décret n° 2025-1343).
- Pratiques réelles : Meung-sur-Loire ne chauffe qu'« environ les deux tiers » de la surface ; Chambord abaisse le chauffage la nuit à 8 °C par gestion technique centralisée et vise −10 % dès 2023 ; Cheverny réduit le chauffage « au minimum » [V2C-09].
- Effet chiffré (ESTIMATION) : −10 à −15 % de l'énergie centrale R1, soit ≈ 1 800-2 700 € (S1), 3 900-5 900 € (S2), 7 000-10 600 € (S3) par an. Le zonage plus large (pièces de réception chauffées seulement les jours d'événement) est déjà intégré dans les hypothèses de surface chauffée de R1 (40 à 60 % en S2, 30 à 50 % en S3).

### 2.3 Tableau des leviers

| Levier | Effet chiffré | Statut | Sources | Conditions, risques pour le prestige |
|---|---|---|---|---|
| Gestion différenciée (codes de soin par zone) | −550 h/ha/an (code 3 → 4), ≈ −11 100 €/ha/an ; S2 ≈ −67 000 €/an ; S3 ≈ −445 000 €/an par rapport à un parc soigné partout | ESTIMATION sur PAGE LUE | [V2C-21] [V2C-11] | Garder les codes 1-2 près du logis et sur les perspectives ; plan de gestion écrit ; acceptation du « naturel » au loin |
| Fauche tardive | −160 h/ha/an (code 4 → 5) ; −710 h/ha/an (code 3 → 5), ≈ −14 400 €/ha/an | ESTIMATION sur PAGE LUE | [V2C-21] [V2C-11] | Matériel peu utilisé coûteux : sous-traiter ; foin réutilisable pour l'écurie (valeur non chiffrée) |
| Éco-pâturage par un éleveur | ≈ −920 €/ha/an (Avignon : > 12 000 €/an sur 13 ha, coût nul pour la Ville) | ESTIMATION sur PAGE LUE | [V2C-13] [V2C-14] | Convention gratuite ; risque de requalification en bail rural (R3) ; arbres à protéger ; cohabitation avec les chevaux non étudiée |
| Pâturage par les chevaux du domaine | INCONNU | INCONNU | — | Refus, tassement, arbres ; à évaluer avec R6 |
| Remplacement des buis | Coût INCONNU ; cas réel de Vaux (2019) | PAGE LUE (cas), INCONNU (coût) | [V2C-25] [V2C-34] | *Ilex crenata* aussi attaqué (EXTRAIT) ; autorisation en jardin protégé |
| Sous-traitance des tâches saisonnières | Matériel : 56,4 → 14,3 €/h (broyeur) selon l'usage ; prix d'entreprise INCONNU | PAGE LUE (R2) / INCONNU | [R2-30] [V2C-20] | Garder le soin quotidien en interne ; dérives voisines sur 15 ans |
| Groupement d'employeurs entre domaines | INCONNU | INCONNU (cadre légal PAGE LUE) | [V2C-29] | Égalité de traitement ; domaine exploité en société (HYPOTHÈSE) |
| Chaufferie à plaquettes | −7 700 à −10 900 €/an (90-110 kW) ; −35 000 €/an (2 × 200 kW) ; investissement 80 000 à 245 000 € HT | EXTRAIT | [V2C-32] [V2C-33] | Silo, réseau, autorisations MH, travail de déchiquetage ; dérive du bois +0,9 %/an réel contre +1,9 à +4,8 % (fioul, gaz) [V2C-04] |
| Isolation des combles | Au plus −60 % de l'énergie (propos oral) ; borne haute S2 ≈ −23 500 €/an | ESTIMATION (borne) | [R1-09] [V2C-27] [R1-05] | MH exclus de l'obligation ; faisabilité contestée en bâti protégé |
| Régulation et zonage du chauffage | Jusqu'à −15 % (ADEME) ; S2 ≈ −3 900 à −5 900 €/an | ESTIMATION sur PAGE LUE | [V2C-26] [V2C-09] | Confort des pièces d'apparat ; protection des décors et du mobilier contre l'humidité (non chiffré) |

Lecture (ESTIMATION) : seuls les leviers d'espaces verts changent l'ordre de grandeur du budget de S2 (≈ 5 à 7 % de 1,23 M€) et de S3 (≈ 13 à 17 % de 3,4 M€), et **seulement par rapport à un parc entretenu partout comme un jardin**. Par rapport aux effectifs déjà économes retenus par R2, ils ne dégagent pas d'économie : ils sont la **condition** pour que ces effectifs suffisent (§ 3.3). Les leviers énergétiques pèsent moins de 2 % des budgets S2 et S3.

---

## 3. Ratios réels jardiniers / hectare et temps d'entretien au m²

### 3.1 La référence la plus solide : temps de travaux par code de gestion différenciée (Ville de Rennes) [V2C-21] — PAGE LUE

Source : Plante & Cité, Baromètres, « Parcs et jardins : Temps de travaux pour l'entretien », données de la Ville de Rennes (« Coûts de maintenance », 2012), issues de la comptabilité analytique. Citations :
> « En espaces verts, la main d'œuvre représente 80 à 99% des coûts d'entretien. »
> Les temps « correspondent au temps annuel cumulé des équipes de terrain sur les espaces concernés, et des services "support" de la Ville (notamment élagage et transport, et dans une moindre mesure production de végétaux, surveillance, magasin etc.). L'ensemble représente environ 95 % des coûts de maintenance des parcs et jardins. »
> « Ces chiffres sont donnés à titre indicatif, les références sur les coûts d'entretien en espaces verts étant rares. »

| Code de gestion (Rennes, 2012) | Moyenne h/ha/an (min – max) | Nombre de sites | ETP/ha (ESTIMATION, 1 607 h/ETP) | Hectares par ETP | Main-d'œuvre €/ha/an (ESTIMATION, 20,24 €/h) |
|---|---|---|---|---|---|
| Code 1 — jardins structurés très fleuris | 2 800 (2 500 – 4 600) | 7 | 1,74 | 0,6 | ≈ 56 700 |
| Code 2 — jardins structurés | 1 200 (750 – 1 200) | 80 | 0,75 | 1,3 | ≈ 24 300 |
| Code 3 — jardins d'accompagnement | 800 (450 – 1 400) | 979 | 0,50 | 2,0 | ≈ 16 200 |
| Code 4 — jardins champêtres | 250 (200 – 450) | 198 | 0,16 | 6,4 | ≈ 5 100 |
| Code 5 — jardins de nature | 90 (70 – 200) | 39 | 0,06 | 17,9 | ≈ 1 800 |

Conventions (HYPOTHÈSES, identiques à R2) : 1 607 heures travaillées par ETP et par an ; coût horaire d'un jardinier à 1,2 SMIC = 32 531 € / 1 607 h ≈ 20,24 €/h (coût employeur R2 § 9.3). La valeur maximale du code 2 (1 200) égale sa moyenne : c'est ce que la page affiche, sans explication.

Limites : parcs **publics urbains** (propreté, aires de jeux, fréquentation, services support), mesurés en 2012. Un parc privé fermé au public demande probablement moins de temps à code égal (HYPOTHÈSE non vérifiée). Les codes de Rennes ne correspondent pas exactement aux zones d'un château.

### 3.2 Ratios observés (sites réels)

| Site | Surface | Effectif | ETP/ha (ESTIMATION) | h/ha/an équivalent | Type d'entretien | Statut / source |
|---|---|---|---|---|---|---|
| Jardins de Villandry (37), privé | 7 ha | 10 jardiniers | 1,43 | ≈ 2 300 | jardin Renaissance et potager décoratif (≈ code 1-2) | PAGE LUE [R2-15] |
| Jardin du Luxembourg (Sénat, Paris) | 23 ha | « 60 jardiniers en 2016 » | 2,6 | ≈ 4 200 | jardin public très fleuri, serres et collections | PAGE LUE, « réf. nécessaire » [V2C-28], fiabilité faible |
| Chatsworth (Royaume-Uni), charity | jardin de 105 acres (≈ 42,5 ha), plus parc et bois | 29 (personnel « jardins ») | 0,68 | ≈ 1 100 | grand jardin ouvert à ≈ 630 000 visiteurs | PAGE LUE [R5-05] |
| Château de Robersart (Wambrechies, 59), municipal | parc de 9 ha + jardin de 5 500 m² (ancien potager) | « quatre jardiniers » depuis 2016 | 0,42 | ≈ 670 | parc de château et potager | PAGE LUE (Wikipédia) [V2C-17] |
| Ville de Thouars (79), label 4 fleurs | 65 ha d'espaces verts | 34 jardiniers | 0,52 | ≈ 840 | ville très fleurie | PAGE LUE (Wikipédia, 2025) [V2C-16] |
| Ville de Marmande (47), tous espaces | 193,21 ha | 32 agents | 0,17 | ≈ 270 | mélange (voir détail) | PAGE LUE [V2C-12] |
| — dont espaces verts urbains | 10,35 ha | 17 | 1,64 | ≈ 2 640 | fleurissement, désherbage, production florale | idem |
| — dont cimetières | 8,85 ha | 4 | 0,45 | ≈ 730 | — | idem |
| — dont terrains de sport et golf | 72,9 ha | 7 (3 + 4) | 0,10 | ≈ 150 | tonte de grandes surfaces | idem |
| — dont parcs (Filhole, Carroussel, Trec) | 67,8 ha | 4 | 0,06 | ≈ 95 | grands parcs extensifs | idem |
| Ville d'Avignon, surfaces tondues ou fauchées | ≈ 100 ha | 8 agents, passages toutes les 2 à 4 semaines | 0,08 | ≈ 130 | tonte et fauche extensives | PAGE LUE [V2C-13] |
| Vaux-le-Vicomte (77), privé | 33 ha de jardins (parc de 500 ha) | INCONNU (75 salariés au total selon Wikipédia [R4-30] ; « 70 personnes » en 2016 [V2C-24]) | — | ≈ 1 200 à 1 350 si les 10 % du budget étaient entièrement de la main-d'œuvre (ESTIMATION) | jardins structurés et « vingtaine de bassins » | PAGE LUE [V2C-24] [V2C-25] |
| Versailles | 830 ha (Wikipédia) | INCONNU (« une quarantaine aujourd'hui » selon un extrait d'Hérodote, non vérifié) | — | — | — | EXTRAIT [V2C-18], fiabilité faible |
| Chantilly, Courances, Breteuil | 115 ; 75 à 86 ; 75 ha (R2, R4) | INCONNU | — | — | — | sites ouverts sans chiffre (503 ou 404 pour Chantilly et Courances) |

**Budget des jardins de Vaux-le-Vicomte** [V2C-24], PAGE LUE (dossier de presse France 5, 2016 ; même document que [R4-31], relu pour les jardins et l'effectif) : « 10 % du budget annuel sont consacrés à l'entretien des jardins à la française et de la vingtaine de bassins qui subsistent », pour « 9 millions d'euros à trouver chaque année ». ESTIMATION : ≈ 0,8 à 0,9 M€/an pour 33 ha, soit **≈ 24 000 à 27 000 € par hectare et par an**, bassins compris. Ce niveau correspond au **code 2** de Rennes (≈ 24 300 €/ha/an de main-d'œuvre) : les deux sources indépendantes se recoupent.

Lecture (ESTIMATION) :
1. Les ratios s'étagent de **0,06 ETP/ha** (grand parc extensif) à **1,4-1,7 ETP/ha** (jardin très fleuri ou potager décoratif), soit un facteur 25 à 30. Le niveau de soin choisi pèse donc plus que la surface.
2. Un jardin régulier « de prestige » sans fleurissement saisonnier se situe autour de **0,7 à 0,8 ETP/ha** (Rennes code 2, Chatsworth, équivalent Vaux). Villandry (1,4) se situe entre les codes 1 et 2 : c'est un plafond pour un jardin régulier privé, pas un maximum absolu (Rennes code 1 : 1,74 ; Luxembourg : 2,6, source faible).
3. Un parc paysager fauché tardivement ou pâturé se situe autour de **0,06 à 0,16 ETP/ha** (codes 4-5, parcs de Marmande, Avignon).

### 3.3 Application aux surfaces des scénarios (ESTIMATION sur HYPOTHÈSES de répartition)

Main-d'œuvre de jardinage hors chef jardinier, hors matériel, au coût R2 (20,24 €/h) :

| Scénario et répartition (HYPOTHÈSE) | Heures/an | ETP | €/an | Effectif retenu par R2 (§ 9) |
|---|---|---|---|---|
| S1 — parc 3 ha : 0,5 ha code 3 + 2,5 ha code 4 | 1 025 | 0,6 | ≈ 20 700 | 1,0 (jardinier-homme d'entretien) |
| S1 — variante soignée : 0,5 ha code 2 + 2,5 ha code 3 | 2 600 | 1,6 | ≈ 52 600 | idem |
| S2 — 10 ha : 2 ha code 2 + 8 ha code 3 (tout le parc soigné) | 8 800 | 5,5 | ≈ 178 000 | 2 jardiniers + 1 chef |
| S2 — 2 ha code 2 + 2 ha code 3 + 6 ha code 4 | 5 500 | 3,4 | ≈ 111 000 | idem |
| S2 — 2 ha code 2 + 2 ha code 3 + 6 ha code 5 (prairie fauchée ou pâturée) | 4 540 | 2,8 | ≈ 92 000 | idem |
| S3 — 60 ha : 1 ha code 1 (potager décoratif) + 9 ha code 2 + 50 ha code 3 | 53 600 | 33,4 | ≈ 1 085 000 | 8 + 3 jardiniers + 1 chef |
| S3 — 1 ha code 1 + 9 ha code 2 + 10 ha code 3 + 40 ha code 4 | 31 600 | 19,7 | ≈ 640 000 | idem |
| S3 — 1 ha code 1 + 9 ha code 2 + 10 ha code 3 + 40 ha code 5 | 25 200 | 15,7 | ≈ 510 000 | idem |

Conséquences pour le modèle (ESTIMATION) :
- **S2** : les 2 jardiniers et le chef de R2 ne suffisent que si 6 ha du parc sont en prairie (code 4-5). Un parc soigné partout demande ≈ 5,5 ETP.
- **S3** : les 11 jardiniers de R2 sont **sous-estimés** d'au moins 40 % (15,7 ETP dans la variante la plus extensive), et du triple si le parc est entretenu comme un jardin d'accompagnement. Le surcoût par rapport à R2 va de ≈ +150 000 à +700 000 €/an (ESTIMATION : (15,7 − 11) × 32 531 ≈ 153 000 € ; (33,4 − 11) × 32 531 ≈ 729 000 €).
- Ces chiffres sont des ordres de grandeur : parc public urbain, données 2012, conversion au coût R2.

### 3.4 Coût au m² des espaces verts des collectivités

- **Coût global au m² : INCONNU.** L'observatoire des coûts de Plante & Cité est réservé aux adhérents (R2). Les avis du BOAMP ouverts [V2C-35] donnent des montants de marchés (par exemple un accord-cadre de 600 000 € au maximum à Panazol) mais **ni surfaces ni prix unitaires** : ils ne permettent pas de calculer un €/m². Pour vérifier : télécharger le BPU ou la DPGF d'un dossier de consultation sur un profil acheteur, ou rapprocher le budget d'un service espaces verts de ses surfaces.
- **Ordre de grandeur indirect (ESTIMATION)** : la main-d'œuvre représente 80 à 99 % du coût [V2C-21]. Le coût complet vaut donc 1,01 à 1,25 fois les montants de main-d'œuvre du tableau 3.1, soit ≈ 0,18 à 0,23 €/m²/an (code 5) et ≈ 5,7 à 7,1 €/m²/an (code 1), au coût salarial R2.
- **Désherbage des allées** [V2C-22], PAGE LUE (observations 2011, coûts 2013) : désherbage total d'une allée de parc, coût annuel moyen **23 €/100 m²** en chimique (1 à 173), **130 €/100 m²** en manuel (9 à 658), **101 €/100 m²** au brûleur (6 à 453) ; « la main d'œuvre représente 60 à 99 % des coûts » [V2C-23]. ESTIMATION : 1 ha d'allées gravillonnées tenues « zéro herbe » à la main ≈ 13 000 €/an (valeur 2013), contre ≈ 2 300 €/an en chimique. Le cadre légal applicable à un parc privé (usage des produits phytosanitaires) n'a pas été vérifié ici : à confirmer par R3.

---

## 4. Évolution de long terme des coûts (calibrage des dérives sur 20 ans)

Méthode : séries officielles de l'INSEE lues par l'API de la Banque de données macro-économiques [V2C-01] à [V2C-06], PAGE LUE (données brutes). Moyennes annuelles calculées localement (script en annexe A). TCAM = taux de croissance annuel moyen. « Réel » = TCAM déflaté par l'indice des prix à la consommation (IPC) d'ensemble [V2C-04]. Toutes les lignes ci-dessous sont des **ESTIMATIONS arithmétiques sur données officielles PAGE LUE**.

### 4.1 Tableau des dérives observées

| Poste | Série INSEE | Valeur début | Valeur fin | Facteur | TCAM nominal 20 ans | TCAM nominal 10 ans | TCAM réel 20 ans |
|---|---|---|---|---|---|---|---|
| Inflation (IPC ensemble) | 001759970 [V2C-04] | 87,85 (moy. 2005) | 120,95 (moy. 2025) | × 1,38 | 1,61 % | 1,92 % | — |
| SMIC horaire brut | 000822484 [V2C-05] | 8,03 € (janv. 2006) | 12,02 € (janv. 2026) ; 12,31 € (juin 2026) | × 1,50 | 2,04 % | 2,20 % (janv. 2016 : 9,67 €) | ≈ 0,4 % (SMIC 2006-01 → 2025-12 : 1,99 %/an contre IPC 1,59 %/an) |
| Salaires horaires des ouvriers et employés, « services administratifs et de soutien » (NAF NZ, qui comprend l'aménagement paysager 81.30) | 010562769 [V2C-06] | 100 (T2 2017) | 125,5 (T2 2026) | × 1,255 en 9 ans | — | 2,56 % (sur 9 ans) | INCONNU (série base 2017 seulement) |
| Entretien-amélioration des bâtiments, résidentiel (IPEA) | 011779962 [V2C-03] | 74,18 (moy. 2005) | 118,42 (moy. 2025) ; 121,0 (T2 2026) | × 1,60 | 2,37 % | 2,67 % | 0,74 % |
| IPEA résidentiel — couverture | 011779978 [V2C-03] | 68,45 | 120,95 | × 1,77 | 2,89 % | 3,55 % | 1,26 % |
| IPEA résidentiel — menuiserie | 011779972 [V2C-03] | 68,05 | 126,33 | × 1,86 | 3,14 % | 3,84 % | 1,51 % |
| IPEA résidentiel — plomberie, chauffage | 011779966 [V2C-03] | 69,55 | 119,42 | × 1,72 | 2,74 % | 2,42 % | 1,11 % |
| Index BT01 tous corps d'état (construction neuve) | 000008631 puis 001710986 [V2C-01] [V2C-02] | 687,4 (moy. 2005, base 1974) | 133,01 (moy. 2025, base 2010) ; 138,9 (juil. 2026) | × 1,62 (chaînage, voir note) | 2,45 % | 2,47 % (2015 : 104,26) | ≈ 0,8 % |
| Électricité (IPC) | 001763554 [V2C-04] | 71,55 | 146,92 | × 2,05 | 3,66 % | 3,92 % | 2,02 % |
| Gaz naturel (IPC) | 001763557 [V2C-04] | 60,98 | 213,23 | × 3,50 | 6,46 % | 7,87 % | 4,77 % |
| Combustibles liquides, c.-à-d. fioul (IPC) | 001763559 [V2C-04] | 81,24 | 163,29 | × 2,01 | 3,55 % | 5,03 % | 1,91 % |
| Autres combustibles solides (bois, granulés : contenu exact non vérifié) (IPC) | 001763562 [V2C-04] | 79,91 | 131,19 | × 1,64 | 2,51 % | 2,75 % | 0,88 % |
| Ensemble électricité, gaz et combustibles (IPC) | 001763553 [V2C-04] | 68,15 | 164,53 | × 2,41 | 4,51 % | 5,11 % | 2,85 % |

Note BT01 : l'ancienne série (base 100 en janvier 1974) s'arrête en septembre 2014 (881,6) et la nouvelle (base 2010) commence en octobre 2014 (105,1). Le coefficient officiel de raccordement n'a pas pu être lu (page INSEE dynamique, vide en lecture). Le chaînage utilise le rapport observé entre ces deux mois (8,388), ce qui suppose une variation nulle entre septembre et octobre 2014 : ESTIMATION. Le TCAM sur 10 ans (2,47 %) ne dépend pas de ce raccord.

Volatilité (moyennes annuelles, même source [V2C-04]) : le fioul passe de 126,5 (2021) à 210,0 (2022) puis 172,0 (2024) ; le gaz de 121,8 (2021) à 196,2 (2023) ; l'électricité de 118,9 (2021) à 166,8 (2024) ; le bois et les granulés de 106,6 (2021) à 150,3 (2023) puis 135,5 (2024). Le BT01 gagne 16 % entre 2020 (112,3) et 2023 (130,1), puis ralentit (133,0 en 2025).

### 4.2 Lecture pour le modèle (ESTIMATION)

1. **Personnel** : une masse salariale proche du SMIC suit le SMIC, soit ≈ +2,0 à 2,2 %/an nominal, ≈ +0,4 %/an réel sur 20 ans. Ce chiffre porte sur le salaire brut. Le coût employeur dépend en plus des allègements de charges, réformés en 2026 (RGDU, voir R2 § 1.2) : risque politique non mesurable sur données passées.
2. **Bâti** : les prix de l'entretien-amélioration ont crû ≈ 0,7 %/an plus vite que l'inflation (1,3 %/an pour la couverture, 1,5 %/an pour la menuiserie). Après 20 ans, le coût des travaux dépasse donc de **16 à 35 %** une provision de gros entretien simplement indexée sur l'IPC, qui n'en couvre plus que 74 à 86 % (ESTIMATION : 1,0074^20 = 1,16 ; 1,0151^20 = 1,35). Les métiers des monuments historiques (taille de pierre, couverture en ardoise ou plomb, menuiserie à l'identique) n'ont **pas d'indice public** : leur dérive propre est INCONNUE.
3. **Énergie** : +2 %/an réel pour l'électricité, ≈ +4,8 %/an réel pour le gaz, avec des chocs de +40 à +66 % en un à trois ans (fioul +66 % de 2021 à 2022 ; gaz +61 % de 2021 à 2023 ; électricité +40 % de 2021 à 2024). Le bois et les granulés ont la dérive la plus faible (≈ +0,9 %/an réel) mais ont aussi connu un choc (+41 % de 2021 à 2023).
4. Proposition de paramètres de dérive réelle pour le modèle (HYPOTHÈSES appuyées sur ces séries) : personnel +0,5 %/an ; bâti +1,0 %/an ; énergie +2,0 %/an avec un choc de +50 % une année sur dix ; inflation générale traitée à part.
5. **Salaires agricoles** : aucune série longue n'a été lue (les indices ACEMO de l'INSEE couvrent le secteur non agricole). Les grilles de la production agricole commencent au SMIC (R2 § 1.4) : le SMIC sert donc de repère (HYPOTHÈSE).
6. **Assurance des monuments** : aucune série publique propre aux monuments. Meilleur indicateur officiel disponible : l'assurance habitation des ménages (§ 4.3).

### 4.3 Assurance et prestations de jardinage : deux séries complémentaires

| Poste | Série INSEE | 2005 (moy.) | 2015 (moy.) | 2025 (moy.) | TCAM nominal | TCAM réel |
|---|---|---|---|---|---|---|
| Assurance habitation (IPC, COICOP 12.5.2) | 001763819 [V2C-19] | 73,45 | 100,00 | 145,88 | 3,49 %/an sur 20 ans ; 3,85 %/an sur 10 ans | 1,85 %/an sur 20 ans |
| Services d'aménagement paysager, prix de production, tous marchés (CPF 81.30) | 010766745 [V2C-20] | — (série depuis 2010 : 95,35 en 2010) | 92,42 | 125,25 (128,3 au T2 2026) | 1,84 %/an sur 15 ans (2010-2025) ; 3,09 %/an sur 10 ans | ≈ 0,2 %/an sur 15 ans (IPC : 1,64 %/an) |
| Idem, clients entreprises seulement (BtoB) | 010766608 [V2C-20] | — (96,0 en 2010) | 92,70 | 119,58 | 1,47 %/an sur 15 ans ; 2,58 %/an sur 10 ans | ≈ −0,2 %/an sur 15 ans |

Accélération récente de l'assurance habitation (moyennes annuelles, [V2C-19]) : +0,9 % (2021), +1,9 % (2022), **+5,6 % (2023), +8,1 % (2024), +12,6 % (2025)**. Cette série porte sur les contrats des ménages, pas sur les monuments. Elle confirme toutefois la tendance relevée par R1 : surprime catastrophes naturelles portée de 12 à 20 % au 1er janvier 2025 [R1-29], prime d'une maison Grade I britannique « more than doubled » [R1-05], résiliation du château d'Olhain [R1-28].

Lecture (ESTIMATION) :
- **Assurance** : dérive réelle de l'ordre de +1,9 %/an sur 20 ans, avec une accélération à +5 à +13 %/an nominal depuis 2023. Pour un monument, la valeur assurée suit en plus le coût de reconstruction (BT01, IPEA : +0,7 à +1,5 %/an réel). HYPOTHÈSE proposée pour le modèle : +2 %/an réel, avec un scénario de choc (+30 à +100 % en une fois, ou non-assurabilité).
- **Prestations de jardinage sous-traitées** : les prix ont **baissé** de 2010 à 2015, puis augmenté de ≈ 3 %/an de 2015 à 2025. Sur 15 ans, ils suivent à peu près l'inflation. Le salariat direct (SMIC +2,0 à 2,2 %/an) et la sous-traitance ont donc dérivé à des rythmes voisins sur longue période. Le choix entre les deux se joue sur le niveau de prix, pas sur la dérive (voir § 2).

---

## Contre-exemples et cas d'échec trouvés

1. **Modèle des propriétaires privés jugé « de plus en plus difficilement viable »** [V2C-07], PAGE LUE : « Les recettes générées par l'exploitation parviennent rarement à équilibrer les dépenses » ; le « résident » et l'« artisan » ne financent pas leur quote-part des gros travaux sans patrimoine ou revenus extérieurs ; « les monuments en état de péril sont à 42,9 % détenus par des propriétaires privés, alors que ceux-ci ne détiennent que 37,4 % du patrimoine protégé ».
2. **La visite ne finance pas le monument** [V2C-07] : « 60% ont moins de mille visiteurs par an » ; pour 77 propriétaires sur 118, le chiffre d'affaires de la visite est « inférieur à 5.000 euros » ; « Même pour ceux, très rares, qui ont plus de 20.000 euros de recettes annuelles, cela ne représente que quelques dizaines de mètres carrés de toiture. »
3. **Rotation des propriétaires** [V2C-07] : « plus de cinq cents châteaux et demeures historiques seraient actuellement mis à la vente » ; détention moyenne « tombée à sept ans » (chiffre d'agences, non vérifié par la mission IGF-IGAC).
4. **Choc énergétique de 2022** [V2C-09] [V2C-04] : Meung-sur-Loire attendait une facture « multipliée entre cinq et dix » ; Chambord a vu son budget énergie passer de 260 000 € à plus de 600 000 € ; l'indice du fioul a pris +66 % entre 2021 et 2022.
5. **Assurance qui accélère** [V2C-19] : +5,6 % (2023), +8,1 % (2024), +12,6 % (2025) pour l'assurance habitation des ménages ; s'ajoute la résiliation du château d'Olhain (R1 [R1-28]).
6. **Château non classé, donc sans aide** [V2C-08] : Louvignies (Belgique, 14 ha) finance seul une tourelle à 40 000 € et un vitrail à 16 000 €.
7. **Disparition d'un parterre historique** [V2C-25] : Vaux-le-Vicomte a remplacé en 2019 les buis des parterres des boulingrins par une œuvre temporaire en aluminium (cause non indiquée sur la page).
8. **Remplaçant du buis non immunisé** (EXTRAIT, bulletin DRAAF Bretagne 2024) : la pyrale attaque aussi *Ilex crenata* en France.
9. **Retour sur investissement long des petites chaufferies bois** [V2C-32] (EXTRAIT) : ≈ 31 ans avant subventions à Luceram (245 000 € HT pour ≈ 7 800 €/an d'économie, ESTIMATION).
10. **Dépense insuffisante malgré l'effort** (R1 [R1-05]) : maisons historiques britanniques à ≈ 156 000-161 000 £/an de dépense et ≈ 2 M£ de retard chacune.

## Points de doute / hypothèses non vérifiées

1. **Budgets complets** : aucun budget complet de domaine privé de taille S2 n'a été trouvé, ni en France ni en Belgique. Les cas réels sont partiels (énergie, un chantier, un poste) ou hors d'échelle (Vaux, Chambord, Chatsworth). L'enquête « Tournelle » n'est pas publiée en détail.
2. **535 M€ (IGF-IGAC)** : plancher fiscal (déductions déclarées pour 2016), qui inclut ≈ 60 M€ de travaux labellisés par la Fondation du patrimoine et exclut les charges non déductibles. La moyenne par monument (≈ 24 000 €) mélange tous les types de biens et repose sur un nombre de monuments privés approché (« près de la moitié » de 44 000).
3. **Ratios de Rennes** : parcs publics urbains, données 2012, temps des services support inclus ; les codes ne correspondent pas exactement aux zones d'un château ; anomalie affichée pour le code 2 (maximum égal à la moyenne).
4. **Conversions** : 1 607 heures par ETP et 20,24 €/h sont des conventions reprises de R2 (HYPOTHÈSES).
5. **Sources Wikipédia** : Thouars, Robersart (fiabilité moyenne) ; Luxembourg (« réf. nécessaire », fiabilité faible).
6. **Vaux** : la part de 10 % date de 2016 ; budget de 8 ou 9 M€ selon la source ; l'équivalent par hectare suppose que toute la dépense des jardins porte sur les 33 ha.
7. **Chaufferies bois** : chiffres vus seulement en EXTRAIT (fiches refusées, 403 ou 404) ; année des prix du fioul de référence inconnue ; coût de déchiquetage du bois du domaine INCONNU ; part de l'accroissement forestier utilisable en plaquettes INCONNUE ; conversion de 270 L de fioul par tonne tirée d'un agrégat (humidité non précisée).
8. **Séries INSEE** : l'IPC mesure les prix payés par les ménages (énergie, assurance habitation), pas les tarifs d'un château ou d'un professionnel ; l'IPEA porte sur des travaux courants, pas sur les métiers des monuments historiques ; le BT01 sur 20 ans repose sur un raccordement sans coefficient officiel lu ; le contenu exact de « autres combustibles solides » n'a pas été vérifié.
9. **Salaires** : la série ACEMO « services administratifs et de soutien » inclut l'aménagement paysager sans s'y limiter ; aucune série longue de salaires agricoles n'a été lue.
10. **Éco-pâturage** : l'économie d'Avignon est une estimation de la Ville avant la saison, pas un bilan constaté.
11. **Gestion différenciée** : la baisse de 20 à 40 % annoncée par Dumbéa n'a pas été lue (EXTRAIT).
12. **Isolation des combles** : le gain de 60 % est un propos oral sans étude citée ; le coût des travaux en bâti protégé est INCONNU.
13. **Questions juridiques renvoyées à R3** : requalification d'une convention de pâturage en bail rural ; règles phytosanitaires applicables à un parc privé ; adhésion d'un domaine à un groupement d'employeurs ; autorisations pour modifier un jardin protégé (buis) ou installer une chaufferie en abords de MH.
14. **Outil de lecture** : pour les pages HTML, les citations sont restituées par l'outil de synthèse de WebFetch (parfois paraphrasées) ; pour les PDF et les données INSEE ou Plante & Cité, le texte a été extrait localement et les citations sont exactes.

## Chiffres clés pour le modèle

| # | Donnée | Valeur | Unité | Année | Statut | Source |
|---|---|---|---|---|---|---|
| 1 | SMIC horaire brut : croissance nominale ; réelle | 2,04 (2006-2026) ; ≈ 0,4 | %/an | 2006-2026 | ESTIMATION sur PAGE LUE | [V2C-05] [V2C-04] |
| 2 | Entretien-amélioration des bâtiments (IPEA résidentiel) : nominal ; réel | 2,37 ; 0,74 (couverture 2,89 ; 1,26) | %/an | 2005-2025 | ESTIMATION sur PAGE LUE | [V2C-03] |
| 3 | Index BT01 : 20 ans (chaîné) ; 10 ans | 2,45 ; 2,47 | %/an | 2005-2025 | ESTIMATION sur PAGE LUE | [V2C-01] [V2C-02] |
| 4 | Énergie (IPC), dérive réelle : électricité ; gaz ; fioul ; bois et granulés | 2,02 ; 4,77 ; 1,91 ; 0,88 | %/an | 2005-2025 | ESTIMATION sur PAGE LUE | [V2C-04] |
| 5 | Assurance habitation (IPC) : nominal 20 ans ; réel ; hausse 2025 | 3,49 ; 1,85 ; +12,6 | %/an ; % | 2005-2025 | ESTIMATION sur PAGE LUE | [V2C-19] |
| 6 | Prix des services d'aménagement paysager | 1,84 (2010-2025) ; 3,09 (2015-2025) | %/an | 2010-2025 | ESTIMATION sur PAGE LUE | [V2C-20] |
| 7 | Temps d'entretien par code de gestion (Rennes) : codes 1 à 5 | 2 800 ; 1 200 ; 800 ; 250 ; 90 | h/ha/an | 2012 | PAGE LUE | [V2C-21] |
| 8 | Part de la main-d'œuvre dans le coût d'entretien des espaces verts | 80 à 99 | % | 2012-2017 | PAGE LUE | [V2C-21] |
| 9 | Ratio jardiniers : jardin régulier de prestige ; parc extensif ; jardin très fleuri | ≈ 0,7-0,8 ; ≈ 0,06-0,16 ; ≈ 1,4-1,7 | ETP/ha | 2012-2025 | ESTIMATION (Rennes, Vaux, Chatsworth, Villandry, Marmande) | [V2C-21] [V2C-24] [R5-05] [R2-15] [V2C-12] |
| 10 | Coût des jardins de Vaux-le-Vicomte (33 ha et ≈ 20 bassins) | ≈ 24 000 à 27 000 | €/ha/an | 2016 | ESTIMATION sur PAGE LUE | [V2C-24] |
| 11 | Jardiniers nécessaires S2 (10 ha) selon le zonage | 2,8 à 5,5 (hors chef) | ETP | 2026 | ESTIMATION | § 3.3 |
| 12 | Jardiniers nécessaires S3 (60 ha) selon le zonage ; R2 en retenait 11 | 15,7 à 33,4 (hors chef) | ETP | 2026 | ESTIMATION | § 3.3 |
| 13 | Économie de main-d'œuvre : code 3 → 4 ; code 3 → 5 | ≈ 11 100 ; ≈ 14 400 | €/ha/an | 2026 | ESTIMATION | § 2.1 |
| 14 | Désherbage total d'allées : manuel ; chimique | 130 ; 23 | €/100 m²/an | 2013 | PAGE LUE | [V2C-22] |
| 15 | Éco-pâturage par un éleveur (Avignon) | ≈ 920 d'économie, coût nul pour la Ville | €/ha/an | 2020 | ESTIMATION sur PAGE LUE | [V2C-13] |
| 16 | Chaufferie plaquettes 90-110 kW : économie ; investissement | 7 700 à 10 900 ; 80 000 à 245 000 HT | €/an ; € | non daté | EXTRAIT | [V2C-32] [V2C-33] |
| 17 | Accroissement net des forêts françaises | 4,4 (de < 1 à > 7 selon les régions) | m³/ha/an | 2014-2022 | PAGE LUE | [V2C-30] |
| 18 | Régulation du chauffage par pièce | jusqu'à −15 | % de l'énergie de chauffage | 2026 | PAGE LUE (ADEME citée) | [V2C-26] |
| 19 | Dépense des propriétaires privés de MH ; moyenne par monument | ≥ 535 M€ ; ≈ 24 000 € | par an | 2016-2017 | PAGE LUE ; moyenne = ESTIMATION | [V2C-07] |
| 20 | Subvention DRAC moyenne ; cycle de restauration des toitures | 30 % (jamais > 50 %) ; 70 à 80 ans | — | 2020 | PAGE LUE | [V2C-07] |
| 21 | Vaux-le-Vicomte : budget annuel ; personnes | 9 M€ (8 selon Wikipédia) ; 70 (2016) à 75 | €/an ; personnes | 2016 | PAGE LUE | [V2C-24] [R4-30] |
| 22 | Chambord : énergie | 260 000 → > 600 000 (budget ≈ 30 M€) | €/an | 2021-2023 | PAGE LUE | [V2C-09] |
| 23 | Charges annuelles d'un château (agence, Belgique) | 20 000 à 80 000 | €/an | 2025 | PAGE LUE, fiabilité faible | [V2C-08] |

## Journal d'utilisation web (agent V2C)

- **WebSearch : 10 sur 10 autorisées** : (1) budgets déclarés par des propriétaires ; (2) enquêtes DH et VMF ; (3) jardiniers des grands domaines ; (4) budgets de châteaux nommés ; (5) gestion différenciée et coût au m² ; (6) éco-pâturage ; (7) pyrale du buis ; (8) chaufferies bois ; (9) prix unitaires des marchés d'espaces verts ; (10) jardiniers de Vaux-le-Vicomte.
- **WebFetch : 41 appels** : 12 avec des données utilisées, 9 utiles seulement pour trouver des liens (pages d'accueil, moteurs internes), 20 échecs ou pages sans donnée (403, 404, 503, pages dynamiques vides, maintenance).
- **Autres requêtes (curl) : 75** :
  - 25 requêtes à l'API publique de l'INSEE (BDM, SDMX), dont 5 erreurs de syntaxe corrigées ;
  - 33 téléchargements de PDF ou de pages publiques, convertis avec pdftotext (rapport IGF-IGAC, documents de Liffré, Marmande, Avignon, Rouen, CAUE 54, Parc du Morvan, IGN, Comité des parcs et jardins, avis du BOAMP), dont 16 refusés ou inutilisables (403, 404, 503, connexion coupée, HTML au lieu du PDF) ;
  - 12 requêtes au site et à l'API WordPress des Baromètres de Plante & Cité ;
  - 5 requêtes à l'API de Wikipédia, dont 4 refusées ou vides (excès de requêtes).
- Aucun contact, formulaire, achat, création de compte ni commande git.

## Annexe A — Scripts de calcul (reproductibles)

Données : API INSEE BDM (`https://bdm.insee.fr/series/sdmx/data/...`), séries citées en § 4. Scripts exécutés avec Python 3.13.

### A.1 Dérives de long terme (`derives.py`, extrait des formules)

```python
# moyenne annuelle d'une série mensuelle ou trimestrielle, puis TCAM et TCAM réel
def avg(s, year): v = [x for p, x in s.items() if p.startswith(str(year))]; return sum(v) / len(v)
def cagr(a, b, n): return (b / a) ** (1 / n) - 1
# TCAM nominal 20 ans = cagr(avg(serie, 2005), avg(serie, 2025), 20)
# TCAM réel = (1 + TCAM nominal) / (1 + TCAM de l'IPC ensemble 001759970) - 1
# BT01 : facteur 2005-2025 = (ancienne 2014-09 / moyenne ancienne 2005) * (moyenne nouvelle 2025 / nouvelle 2014-10)
```

### A.2 Jardins (`jardins.py`, extrait des formules)

```python
H_ETP = 1607                 # HYPOTHÈSE (R2)
EUR_H = 32531 / H_ETP        # 20,24 €/h, coût employeur d'un jardinier à 1,2 SMIC (R2 § 9.3)
codes = {1: 2800, 2: 1200, 3: 800, 4: 250, 5: 90}   # h/ha/an, Rennes 2012 [V2C-21]
# heures d'un scénario = somme(surface_ha * h_par_ha) ; ETP = heures / H_ETP ; coût = heures * EUR_H
# ex. S3 extensif : 1*2800 + 9*1200 + 10*800 + 40*90 = 25 200 h = 15,7 ETP ≈ 510 000 €/an
```
