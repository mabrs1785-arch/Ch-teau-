# V2C — Budgets réels déclarés et leviers de « prestige efficace »

Agent : V2C (vague 2). Démarré le 2026-10-14. Fichier écrit au fur et à mesure.
Sources : `sources/sources_V2C.csv` (identifiants V2C-xx). Les sources des agents de la vague 1 sont citées par leur identifiant d'origine (R1-xx, R2-xx, R4-xx, R5-xx).

Rappels de méthode :
- statuts : PAGE LUE, EXTRAIT, ESTIMATION, HYPOTHÈSE, INCONNU ;
- ce qui figure déjà dans R1 (bâti, énergie, assurance) et R2 (salaires, Villandry, synthèse des effectifs) n'est pas refait ; seuls les compléments sont ajoutés ;
- budget à confronter (vague 1) : S1 ≈ 0,33 M€, S2 ≈ 1,23 M€, S3 ≈ 3,4 M€ par an, tout compris avec provisions.

## Journal d'avancement

- Lecture du contexte, des règles, de la mission V2C, des sections utiles de R1, R2, R4 et R5.

- Séries longues INSEE téléchargées par l'API officielle (BDM, SDMX) et calculées localement (script en annexe A) : question 4 traitée en premier, car elle ne consomme aucune recherche web.

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
5. **Assurance des monuments** : aucune série publique propre aux monuments. Meilleur indicateur officiel disponible : l'assurance habitation des ménages (§ 4.3).

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

## 1. Budgets annuels déclarés : cas réels (France, Belgique, comparaison britannique)

### 1.1 Constat général

Les budgets **complets** déclarés par des propriétaires privés (tous postes, avec effectifs et surfaces) sont **très rares** dans les sources publiques. Quatre recherches web et la lecture des documents de la Demeure Historique n'ont donné que des montants **partiels** (énergie, un chantier, un poste). Le seul budget complet d'un grand domaine privé français reste celui de Vaux-le-Vicomte, déjà relevé par R4 [R4-30] [R4-31]. L'« enquête Tournelle » (DH, 2010, 513 monuments) n'est pas publiée en détail (R1, R4).

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
- **Château de Trazegnies (Corroy-le-Château, Belgique)** [V2C-08], PAGE LUE : « La restauration du pont menant au château pourrait coûter un million d'euros » ; l'aide publique wallonne « peut couvrir jusqu'à 75% des travaux » si le château est classé comme patrimoine exceptionnel et accessible au public.
- **Agence Barnes (Belgique)** [V2C-08], PAGE LUE : « ces charges annuelles varient entre 20.000 et 80.000 euros, en fonction de l'état et de la taille du bien ». Estimation d'agence immobilière, sans surface ni postes : fiabilité faible, et vraisemblablement hors gros entretien (HYPOTHÈSE de lecture).

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

**Budget des jardins de Vaux-le-Vicomte** [V2C-24], PAGE LUE (dossier de presse France 5, 2016) : « 10 % du budget annuel sont consacrés à l'entretien des jardins à la française et de la vingtaine de bassins qui subsistent », pour « 9 millions d'euros à trouver chaque année ». ESTIMATION : ≈ 0,8 à 0,9 M€/an pour 33 ha, soit **≈ 24 000 à 27 000 € par hectare et par an**, bassins compris. Ce niveau correspond au **code 2** de Rennes (≈ 24 300 €/ha/an de main-d'œuvre) : les deux sources indépendantes se recoupent.

Lecture (ESTIMATION) :
1. Les ratios s'étagent de **0,06 ETP/ha** (grand parc extensif) à **1,4-1,7 ETP/ha** (jardin très fleuri ou potager décoratif), soit un facteur 25 à 30. Le niveau de soin choisi pèse donc plus que la surface.
2. Un jardin régulier « de prestige » sans fleurissement saisonnier se situe autour de **0,7 à 0,8 ETP/ha** (Rennes code 2, Chatsworth, équivalent Vaux). Villandry (1,4) est bien un plafond, comme l'indiquait R2.
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

