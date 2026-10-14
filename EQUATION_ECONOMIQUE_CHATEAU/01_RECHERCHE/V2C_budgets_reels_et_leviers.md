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

