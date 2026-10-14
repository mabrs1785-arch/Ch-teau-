# L3 — Les cinq modèles les plus prometteurs

> **Statut de ce document**
> - Sélection argumentée, en euros constants 2026, à partir de L1 (besoin), L2 (sources de financement), L6 (résistance) et du modèle.
> - Les montants de capital viennent de la simulation de Monte-Carlo : `02_MODELE/calculer_mc.py`, fonction `comparaison_modeles`, résultats dans `02_MODELE/sorties/mc_comparaison_modeles.json`. Ils indiquent le capital nécessaire pour avoir 95 % de chances de tenir 30 ans, sous les hypothèses du modèle (L6, § 2). Précision d'environ ±5 %.
> - Statuts : SOURCÉ, ESTIMATION, HYPOTHÈSE. Les montages juridiques et fiscaux cités sont **à valider** par un avocat fiscaliste et un notaire.

---

## 1. La réponse en une page

**Point de départ.** Aucune combinaison d'activités compatible avec une résidence calme ne couvre plus de 7 % du besoin de S2 dans le cas central (L2, § 3.6). La seule exception, le locataire d'ancrage (21 %), sacrifie la partie privée. Les cinq modèles retenus reposent donc tous sur un **capital affecté au domaine** : un fonds d'entretien qui produit un revenu sans le travail du propriétaire. Ils diffèrent par la manière de **constituer** ce capital et de **réduire** son montant.

| Rang | Modèle | Principe | Capital nécessaire en S2 (95 % de chances de tenir 30 ans) | Prix à payer | Pour quel propriétaire ou quel domaine |
|---|---|---|---:|---|---|
| **1** | **Hybride : entreprises → fonds d'entretien** | Une holding de PME verse des dividendes de transition, puis ses revenus sont convertis en fonds diversifié | **74,6 M€** de fonds au départ, plus 1 M€ de dividendes nets par an pendant 10 ans (56,8 M€ pour 95 % de chances de tenir 20 ans) | Dépendance au fondateur pendant la constitution ; défaillance des PME | Propriétaire entrepreneur, prêt à bâtir le capital avant d'engager toute la dépense |
| **2** | **Fonds d'entretien pur** | Un capital affecté dès le départ, géré avec une règle de dépense | **85,5 M€** (36,5 M€ pour une chance sur deux) | Immobiliser environ 70 fois le besoin annuel | Propriétaire qui dispose déjà du capital (héritage, vente d'entreprise) |
| **3** | **Domaine dimensionné à son capital** | Choisir le domaine et son train de vie en fonction du capital disponible | S1 : **22,9 M€** ; S2 avec les leviers vérifiés : **78,4 M€** | Moins de surface, de jardins réguliers ou de personnel de maison | Tous : c'est le levier le plus puissant, et il se joue **avant** l'achat |
| **4** | **Locataire d'ancrage + fonds réduit** | Bail de 15 à 30 ans à un exploitant de séminaires résidentiels | **69,7 M€** (S2, si les conditions sont réunies) ; S3 : 249,6 M€ au lieu de 271,3 M€ | Partie privée réduite, cohabitation avec 40 à 100 chambres, engagement de 15 à 30 ans | Grand domaine à moins de 90 km de Paris ou à moins de 45 minutes d'une gare TGV |
| **5** | **Vente d'une partie du domaine pour amorcer le fonds** | Céder des communs, un hameau ou des terres éloignés de la partie privée | Réduit le fonds du produit net de la vente ; **montant INCONNU** | Voisins permanents, cession définitive, urbanisme | Grand domaine dont des bâtiments sont dispersés et inutiles au propriétaire |

**Un socle commun d'activités calmes** s'ajoute à chaque modèle :
- logements dans les communs ;
- bail solaire hors du champ de visibilité ;
- forêt ;
- pension standard et pension de retraite au pré ;
- deux journées de tournage par an.

Il couvre environ 4 % du besoin de S2. Il sert surtout à **occuper et entretenir** des bâtiments qui coûteraient de toute façon (§ 4).

**Trois enseignements :**
1. **Le vrai prix d'un château de prestige n'est pas son prix d'achat, mais le capital qui le fait vivre.** Pour S2, ce capital vaut environ 20 fois le prix d'achat retenu (3,5 M€).
2. **Le premier levier se joue avant l'achat**, dans le choix du domaine. Chaque tranche de 100 000 € de besoin annuel demande environ 7 M€ de capital pour 95 % de chances de tenir 30 ans.
3. **Une entreprise peut constituer le capital, pas le remplacer.** Une holding de PME qui ne fait que distribuer ses dividendes échoue dans 67 à 91 % des cas sur 30 ans (L6, § 4.4). Sa valeur vient de sa **conversion** en fonds diversifié.

---

## 2. Méthode de sélection

Les modèles ont été jugés sur les critères du brief :

| Critère | Mesure utilisée |
|---|---|
| Couverture du besoin | Contribution centrale (modèle, feuilles Moteurs et Modeles) et capital nécessaire (Monte-Carlo) |
| Robustesse | Stress tests sur 20 ans et probabilité d'échec sur 30 ans (L6) |
| Qualité des revenus | Classes A (contractuel), B (récurrent), C (occasionnel) et D (financier ou extérieur) |
| Tranquillité et partie privée | Présence de tiers, fréquence, nuisances, engagement de durée |
| Prestige | Compatibilité avec un entretien d'exception et l'image du domaine |
| Dépendance au fondateur | Le revenu continue-t-il sans le travail du propriétaire ? |
| Faisabilité | Contraintes juridiques, fiscales et d'urbanisme (R3, V2A, V2D) |
| Preuves | Existence de cas réels documentés, avec des comptes publiés si possible |

Les modèles qui échouent sur la couverture ou sur la tranquillité sont écartés au § 5, avec leurs raisons.

---

## 3. Les cinq modèles

### 3.1 Modèle 1 — Hybride : des entreprises qui construisent un fonds d'entretien (recommandé)

**Principe.**
1. Le propriétaire détient, directement ou par une holding, plusieurs PME rentables et sans dette d'acquisition.
2. Pendant une **période de transition** d'environ 10 ans, leurs dividendes paient une partie du fonctionnement du domaine.
3. Ce qui n'est pas dépensé, puis les produits de cessions éventuelles, sont versés à un **fonds d'entretien diversifié**, géré avec une règle de dépense.
4. Le domaine n'engage son niveau de dépense complet qu'au moment où le fonds, avec sa règle, couvre le besoin (seuil de déclenchement, L2, § 6.3).

**Chiffres (S2, modèle).**
- Solution modélisée :
  - fonds de 60 M€ au départ ;
  - 1 M€ de dividendes nets par an pendant 10 ans ;
  - réserve de 1,5 M€.
- Probabilité d'échec : 4,3 % sur 20 ans et 11,1 % sur 30 ans (L6, § 4).
- Pour 95 % de chances de tenir 30 ans, il faudrait 74,6 M€ de fonds au départ ; pour 95 % sur 20 ans, 56,8 M€ suffisent (`mc_comparaison_modeles.json`).
- 1 M€ de dividendes nets suppose environ 2,5 M€ d'EBITDA, à raison de 0,396 € net par euro d'EBITDA après IS et PFU (ESTIMATION [R8-35] [R3-16] [R3-20]). Une entreprise de cette taille se paie environ 5 à 8 fois son EBITDA, soit environ 13 à 20 M€ (ESTIMATION sur la même source).
- En S3, avec 3 M€ de dividendes par an pendant 10 ans, il faut 237,3 M€ de fonds pour 95 % sur 30 ans, au lieu de 271,3 M€ sans dividendes.

**Preuves.**
- Northumberland Estates, propriété de la famille d'Alnwick, est une foncière diversifiée qui verse 5 M£ de dividendes par an [R5-14].
- En France, les domaines privés qui tiennent s'appuient en général sur un revenu extérieur : Caudalie à côté de Smith Haut Lafitte, l'activité d'un médecin à Gudanes [R4]. Au Domaine des Étangs, la famille couvre des pertes d'environ 7,6 M€ par an [R4-08].

**Forces.**
- Le rendement d'une PME achetée sans dette (5 à 8 % du capital investi) dépasse celui d'un portefeuille financier (2,75 % retirables).
- Le capital peut se constituer par le travail, sans dépendre d'un héritage.

**Faiblesses et risques.**
- Plus d'une transmission de PME sur cinq échoue dans les six ans (données OSEO 1997-2003) [R8-36].
- Une holding seule, sans conversion en fonds, échoue dans 67 à 91 % des cas sur 30 ans (L6, § 4.4).
- **Forte dépendance au fondateur pendant la constitution.** Sans dividendes, le risque à 30 ans passe de 11 à 17 % (L6, § 4.2).
- Une holding dont les revenus sont surtout passifs peut tomber sous la taxe de 20 % sur les holdings patrimoniales de la loi de finances 2026. Le château habité et les chevaux personnels ne doivent jamais y être logés [R3-18] (à valider).

**Conditions de succès.**
- Au moins cinq entreprises, sans dette d'acquisition au moment où elles financent le domaine.
- Des dirigeants salariés : le propriétaire ne doit pas être indispensable à leur marche.
- Une règle de conversion écrite : une part fixe des dividendes et tout produit de cession vont au fonds.
- Le seuil de déclenchement est respecté.

### 3.2 Modèle 2 — Fonds d'entretien pur (« maintenance fund » à la française)

**Principe.**
- Un capital diversifié, distinct du patrimoine personnel au sens courant, est **affecté** au domaine dès le départ.
- Le domaine retire chaque année au plus 2,75 % du capital, selon une règle lissée.
- Une réserve d'un an de besoin et un fonds de travaux absorbent les chocs.

**Chiffres (dotation seule, avec le socle d'activités).**

| Domaine | Besoin annuel | Une chance sur deux de tenir 30 ans | 95 % de chances |
|---|---:|---:|---:|
| S1 | 0,33 M€ | 9,6 M€ | 22,9 M€ |
| S2 | 1,24 M€ | 36,5 M€ | 85,5 M€ |
| S3 | 3,64 M€ | 108,7 M€ | 271,3 M€ |

Le seuil d'une chance sur deux n'est pas un objectif : le domaine y vit en mode de tension (L6, § 4.3).

**Preuves.**
- **Burghley** : la fondation est « endowed with its own land and property portfolios ». Son revenu immobilier net de 3,52 M£ couvre environ 75 % de ses dépenses caritatives [R5-07].
- **Blenheim** : un fonds dédié de 21,9 M£, avec un objectif de 45 M£ [R5-03].
- Les fonds de dotation universitaires américains dépensent environ 4,9 % par an, mais ils sont exonérés d'impôt [R8-34]. En France, avec un PFU de 31,4 % [R8-31], le taux retenu est de 2,75 % (ESTIMATION).

**Forces.**
- C'est le modèle le plus simple et le plus robuste à capital égal : aucune dépendance à une activité ni au fondateur, et aucun tiers sur le domaine.
- Les actifs financiers ne sont pas soumis à l'IFI, contrairement à l'immobilier [R3-01] (à valider selon la forme retenue).

**Faiblesses et risques.**
- Il exige un capital considérable, environ 70 fois le besoin annuel.
- Le **véhicule juridique** n'a pas d'équivalent direct du « maintenance fund » britannique. Un fonds de dotation exige un apport gratuit et irrévocable et une mission d'intérêt général, a priori incompatibles avec une jouissance privée [R8-45]. La forme retenue (holding, société civile de portefeuille, contrat de capitalisation) détermine la fiscalité, donc le rendement net : **à valider par un avocat fiscaliste**.
- Le rendement réel net de 3 % est l'hypothèse la plus sensible après le budget (L6, § 5).

### 3.3 Modèle 3 — Dimensionner le domaine à son capital (sobriété choisie)

**Principe.** Le besoin annuel est la variable qui pèse le plus sur le capital nécessaire. Il faut donc choisir le domaine et son train de vie **en fonction du capital disponible**, et non chercher le capital une fois le domaine acheté.

**Chiffres.**
- Pour 95 % de chances de tenir 30 ans, il faut environ 70 fois le besoin annuel. Chaque tranche de 100 000 € de besoin coûte donc environ 7 M€ de capital.
- S1 demande 22,9 M€, S2 85,5 M€, S3 271,3 M€.
- Avec les leviers vérifiés par V2C (environ −7,5 % du besoin, sans avantage fiscal), S2 demande 78,4 M€ au lieu de 85,5 M€ (`mc_comparaison_modeles.json`).
- **Une erreur de budget pèse plus que tout le reste.** Si le besoin réel de S2 se situe au haut de la fourchette de L1, il faut environ 143 M€ (L6, § 4.2).

**Leviers disponibles** (L2, § 5) :
- gestion différenciée du parc (déjà intégrée au budget) ;
- choix de la chaudière et zonage du chauffage ;
- arbitrage sur le personnel de maison et le nombre d'hectares de jardins réguliers ;
- achat d'un bien **déjà restauré**, qui évite un rattrapage d'entretien (L1, § 8).

**Forces.** C'est le seul levier gratuit, et il se joue avant l'achat.

**Faiblesses.** Il réduit la surface, les jardins réguliers ou le personnel. Ce sont des éléments du brief (« jardins impeccables, personnel suffisant »). Le propriétaire doit arbitrer.

### 3.4 Modèle 4 — Locataire d'ancrage et fonds réduit (pour un grand domaine bien situé)

**Principe.** Une partie importante des bâtiments est louée pour 15 à 30 ans à un exploitant de séminaires résidentiels. L'exploitant paie un loyer et prend en charge l'énergie et l'entretien courant de la zone louée. Le propriétaire garde une aile ou une maison privée et le gros entretien (L2, § 3.4).

**Chiffres.**
- Contribution centrale : 0,35 M€ par an pour 50 chambres (ESTIMATION fragile : aucun loyer réel de château trouvé).
- Le loyer est prudemment traité comme un revenu récurrent de classe B, qui baisse de 15 % en crise, et non comme un revenu contractuel, parce que des loyers ont été suspendus en 2020-2021 [V2A-31] [V2A-62].
- Capital nécessaire pour 95 % de chances de tenir 30 ans :
  - S2 : 69,7 M€ au lieu de 85,5 M€ (−18 %) ;
  - S3, avec 80 chambres : 249,6 M€ au lieu de 271,3 M€ (−8 %).

**Conditions cumulatives** [V2A-13] [V2A-54] :
- moins de 90 km de Paris, ou moins de 45 minutes d'une gare TGV ou d'un aéroport de métropole ;
- au moins 40 chambres ;
- un exploitant qui finance la transformation.

**Forces.** C'est la seule activité sur place à la bonne échelle. Le revenu est contractuel, et l'exploitant porte l'exploitation.

**Faiblesses et risques.**
- **Incompatible avec une partie entièrement privée en S2**, puisqu'il faudrait mobiliser l'essentiel des bâtiments.
- Engagement quasi irréversible : refuser le renouvellement coûte une indemnité d'éviction.
- Le gros entretien reste au propriétaire.
- Le bail peut être repris par un exploitant non choisi [V2A-36] [V2A-38] [V2A-39].
- Aucun cas documenté d'un propriétaire vivant à côté d'un tel exploitant n'a été trouvé.

### 3.5 Modèle 5 — Vendre une partie du domaine pour amorcer le fonds

**Principe.** Le propriétaire cède définitivement des bâtiments ou des terres dont il n'a pas l'usage, à l'écart de la partie privée (communs, hameau, fermes, parcelles), et verse le produit net au fonds d'entretien. Plusieurs voies sont possibles :
- une vente directe ;
- une vente à un opérateur qui divise en logements sous le régime des monuments historiques ;
- une promotion foncière.

**Chiffres.**
- Chaque million d'euros net versé au fonds réduit d'autant le capital à trouver par ailleurs, et finance environ 27 500 € de besoin par an.
- Le **prix obtenu est INCONNU** dans les sources : aucun opérateur ne publie ce qu'il paie au propriétaire, et aucun exemple français de domaine vendant ses communs en gardant le château n'a été trouvé [V2D § 1.7] [R8 § 6.2].

**Preuves.**
- **Blenheim** alimente son fonds dédié par la promotion foncière du domaine [R5-03].
- **Castello di Reschio**, en Ombrie : sur environ 1 400 ha, des fermes en ruine sont vendues et restaurées pour des acquéreurs, pendant que la famille garde le château [R8-40] à [R8-43]. Les prix sont inconnus.

**Conditions** (à valider par un notaire) :
- urbanisme : changement de destination, PLU, avis de l'architecte des Bâtiments de France ;
- droit de préemption de la Safer pour les biens agricoles ;
- en cas de division d'un immeuble protégé, 75 % d'habitation dans les 2 ans pour que les acquéreurs gardent le régime fiscal [V2D-16].

**Faiblesses.**
- La vente est définitive et crée des voisins permanents.
- L'appétit des opérateurs n'est pas acquis : le leader a publié de fortes pertes en 2025 [V2D-42].
- Les opérations peuvent être politiquement sensibles [V2D-17].
- Le modèle n'a de sens que pour un **grand** domaine aux bâtiments dispersés, comme une variante de S3.

---

## 4. Le socle commun : des activités calmes qui entretiennent le domaine

| Activité (échelle S2) | Classe | Contribution centrale | Rôle |
|---|:---:|---:|---|
| Logements dans les communs (600 m²) | A | 33 k€ | Occuper et entretenir des bâtiments ; rendement d'environ 3 % sur 1,08 M€ d'investissement |
| Hivernage de camping-cars (600 m²) | A | 5 k€ | Utiliser une grange sans travaux lourds |
| Bail solaire (5 ha hors du champ de visibilité) | A | 15 k€ | Revenu contractuel long ; accord de l'architecte des Bâtiments de France nécessaire [R3-63] |
| Forêt (30 ha) | A | 2 k€ | Gestion durable du bois ; peut alimenter une chaufferie |
| Pension standard et pension de retraite au pré | B | 9 k€ | Partager les installations et le personnel équestres ; revenu stable en 2020 [R6-27] |
| Tournages (2 jours par an) | C | 6 k€ | Image et revenu occasionnel, sans engagement |
| **Total disponible après fuite fiscale** (modèle M1) | | **49 k€** | **4 % du besoin de S2** |

**Règles du socle :**
- **pas de réception ni de public** dans le socle ;
- un revenu ne doit jamais servir à couvrir des charges fixes s'il est de classe C ;
- les logements doivent respecter les règles de performance énergétique : les logements classés G ne peuvent plus être loués, et les F ne le pourront plus dès 2028 [R3-34].

---

## 5. Modèles écartés et pourquoi

| Modèle ou piste | Raison principale | Références |
|---|---|---|
| Château-hôtel exploité (M4) | Contribution négative dans le cas central (−29 % du besoin) ; 7,5 M€ d'investissement ; 54 à 61 % des sociétés de châteaux-hôtels en perte selon la période des comptes | L2 § 2.2 et 3.6 ; [R4-34] ; V2V |
| Lieu d'exception à quota : réceptions, séminaires, grande maison (M2) | Seulement +38 k€ par an par rapport au socle, pour 1 M€ d'investissement de plus et des nuisances ; revenus qui disparaissent en crise (−80 %) | L2 § 3.6 ; L6 § 7 |
| Équestre haut de gamme et reproduction (M3) | Couvre 3 % du besoin ; demande non prouvée hors de l'ouest parisien ; dépend d'un vétérinaire ou du talent du propriétaire | L2 § 3.1 ; [R6-15] |
| Ouverture à la visite | « Pour 99,8 % des propriétaires », la seule ouverture à la visite n'est pas rentable [R1-01] ; foule incompatible avec la tranquillité | L2 § 2.2 |
| Location de luxe de la partie privée (M8) | 39 k€ par an dans le cas central ; le propriétaire doit quitter sa maison l'été ; environ 2 réservations par an et par propriété chez la plateforme leader | L2 § 3.5 ; [V2D-26] |
| Copropriété ou partage entre familles | Les exemples reposent sur des pièces communes, incompatibles avec une partie entièrement privée | [V2D-43] [V2D-44] |
| Vente de la nue-propriété | Au mieux 20 % de la valeur à 26 ans ; aucun marché identifié ; perte définitive pour les héritiers | [V2D-19] [V2D-30] |
| Mécénat, financement participatif | Tout usage privé est exclu (La Mothe-Chandeniers) ; plafond de 60 000 € de recettes commerciales pour le mécénat de la Fondation du patrimoine | [R4] ; [R3-10] |
| Fonds de dotation ou fondation propriétaire du domaine | Apport gratuit et irrévocable, mission d'intérêt général : outil de transmission, pas de financement d'une résidence privée | [R8-45] [R8-46] |
| École ou locataire institutionnel | Flux quotidien de centaines de personnes ; tous les exemples trouvés ont une collectivité pour propriétaire | [R8-26] à [R8-28] |
| Club privé (polo, campagne) | Fréquentation régulière et événements ; le modèle le plus connu, Soho House, n'a jamais été rentable au niveau du groupe | [R8-38] [R8-39] |
| Dette participative | C'est une dette (exemple : 7 % par an), qui ne finance pas un déficit de fonctionnement | [V2D-45] |
| Pistes inhabituelles de petite taille : hydroélectricité, truffière, stockage de vins, crédits carbone, chasse, apprentis | Quelques milliers à quelques dizaines de milliers d'euros, souvent ponctuels ou conditionnés (moulin et droit d'eau, sol, clientèle) | R8 § 1 et § 8 |

---

## 6. Grille de comparaison

Notation qualitative : ●●● favorable, ●● moyen, ● défavorable. Elle résume les sections précédentes ; ce n'est pas un score calculé.

| Critère | 1. Hybride | 2. Fonds pur | 3. Domaine dimensionné | 4. Locataire d'ancrage | 5. Vente partielle |
|---|:---:|:---:|:---:|:---:|:---:|
| Couverture du besoin (une fois constitué) | ●●● | ●●● | ●●● (besoin réduit) | ●● (21 % + fonds) | ● seul, ●●● avec le fonds |
| Capital à réunir au départ | ●● | ● | ●● à ●●● | ●● | ●●● si la vente a lieu |
| Robustesse aux crises (L6) | ●● | ●●● | ●●● | ●● | ●●● une fois versé |
| Tranquillité, partie privée | ●●● | ●●● | ●●● | ● | ●● |
| Prestige du domaine | ●●● | ●●● | ●● | ●● | ●● |
| Indépendance vis-à-vis du fondateur | ● pendant 10 ans, puis ●●● | ●●● | ●●● | ●●● | ●●● |
| Faisabilité juridique et fiscale | ●● (holdings, à valider) | ●● (véhicule à valider) | ●●● | ●● (bail commercial) | ● (urbanisme, Safer, ABF) |
| Preuves réelles | ●● (Northumberland) | ●●● (Burghley, Blenheim) | ●● (budgets réels de V2C) | ● (aucune cohabitation documentée) | ●● (Blenheim, Reschio) |

---

## 7. Ce qu'on en retient pour la solution (L4)

- **Pour S2**, la solution combine :
  - le modèle 3 : valider le budget sur le bien réel et appliquer les leviers vérifiés ;
  - le modèle 1 : constituer le fonds par des entreprises, puis convertir leurs revenus ;
  - le socle d'activités calmes.
  - Le modèle 5 s'ajoute si le domaine compte des bâtiments sans usage, éloignés de la partie privée. Le modèle 4 n'est retenu que si la localisation s'y prête et si le propriétaire accepte de réduire sa partie privée.
- **Pour S1**, le même schéma, à une échelle environ quatre fois plus petite : un fonds de 15 M€ et 0,4 M€ de dividendes pendant 10 ans donnent le même niveau de risque que la solution S2 (L6, § 4.1).
- **Pour S3**, le modèle 4 devient une option sérieuse, car la taille permet de garder une aile privée. Le fonds nécessaire reste de l'ordre de 180 à 270 M€, selon le montage et l'horizon visé (20 ou 30 ans).

L4 détaille la solution S2 sur 20 ans : montage, flux annuels, règles et indicateurs.
