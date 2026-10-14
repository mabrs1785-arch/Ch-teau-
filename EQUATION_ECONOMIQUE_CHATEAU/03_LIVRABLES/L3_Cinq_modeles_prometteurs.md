# L3 — Les cinq modèles les plus prometteurs

> **Statut de ce document**
> - Sélection argumentée, en euros constants 2026, à partir de L1 (besoin), L2 (sources de financement), L6 (résistance) et du modèle.
> - Version révisée après l'équipe rouge (V2R) : rendement réel net du capital de 2 % au lieu de 3 %, sinistres et réserve corrigés, capital affecté reconnu comme la fortune du propriétaire.
> - Les montants de capital viennent de la simulation de Monte-Carlo (`02_MODELE/calculer_mc.py`, fonctions `comparaison_modeles` et `dotations` ; résultats dans `02_MODELE/sorties/mc_comparaison_modeles.json` et `mc_dotation_necessaire.json`). Ils indiquent le capital nécessaire pour avoir 95 % de chances de tenir 30 ans, sous les hypothèses du modèle (L6, § 2), avec une précision d'environ ±5 %.
> - Statuts : SOURCÉ, ESTIMATION, HYPOTHÈSE. Les montages juridiques et fiscaux cités sont **à valider** par un avocat fiscaliste et un notaire.

---

## 1. La réponse en une page

**Point de départ.**
- Aucune combinaison d'activités compatible avec une résidence calme ne couvre plus de 6 % du besoin de S2 dans le cas central (L2, § 3.6).
- La seule exception, le locataire d'ancrage (18 %), sacrifie la partie privée.
- Les cinq modèles retenus reposent donc tous sur un **capital affecté au domaine**, qui produit un revenu sans le travail du propriétaire. Ils diffèrent par la manière de **constituer** ce capital et de **réduire** son montant.
- **Ce capital reste juridiquement la fortune du propriétaire** : aucun véhicule français ne l'en sépare tout en laissant la jouissance privée du château (L2, § 6.3).

| Rang | Modèle | Principe | Capital nécessaire en S2 (95 % de chances de tenir 30 ans) | Prix à payer | Pour quel propriétaire ou quel domaine |
|---|---|---|---:|---|---|
| **1** | **Hybride : entreprises → capital affecté** | Une holding de PME verse des dividendes de transition, puis ses revenus sont convertis en capital diversifié | **117,6 M€** au départ, plus 1 M€ de dividendes nets par an pendant 10 ans. La solution retient 120 M€ | Dépendance au fondateur pendant la constitution ; défaillance des PME | Propriétaire entrepreneur, prêt à bâtir le capital avant d'engager toute la dépense |
| **2** | **Capital affecté seul** | Un capital diversifié réservé au domaine dès le départ, géré avec une règle de dépense | **132,2 M€** (50,1 M€ pour une chance sur deux) | Immobiliser environ 100 fois le besoin annuel | Propriétaire qui dispose déjà du capital (héritage, vente d'entreprise) |
| **3** | **Domaine dimensionné à son capital** | Choisir le domaine et son train de vie en fonction du capital disponible | S1 : **37,9 M€** (ou 34 M€ et 0,4 M€ de dividendes pendant 10 ans) ; S2 avec les leviers vérifiés : **122,1 M€** | Moins de surface, de jardins réguliers ou de personnel de maison | Tous : c'est le levier le plus puissant, et il se joue **avant** l'achat |
| **4** | **Locataire d'ancrage + capital réduit** | Bail de 15 à 30 ans à un exploitant de séminaires résidentiels | **114,9 M€** (S2, si les conditions sont réunies) ; S3 : 465,5 M€ au lieu de 491,6 M€ | Partie privée réduite, cohabitation avec 40 à 100 chambres, engagement de 15 à 30 ans | Grand domaine à moins de 90 km de Paris, ou à moins de 45 minutes d'une gare TGV |
| **5** | **Vente d'une partie du domaine pour amorcer le capital** | Céder des communs, un hameau ou des terres éloignés de la partie privée | Réduit le capital à trouver du produit net de la vente ; **montant INCONNU** | Voisins permanents, cession définitive, urbanisme | Grand domaine dont des bâtiments sont dispersés et inutiles au propriétaire |

**Un socle commun d'activités calmes** s'ajoute à chaque modèle :
- logements dans les communs ;
- hivernage de véhicules ;
- bail solaire hors du champ de visibilité ;
- forêt ;
- pension de retraite au pré ;
- deux journées de tournage par an.

Il couvre environ 3 % du besoin de S2. Il sert surtout à **occuper et entretenir** des bâtiments qui coûteraient de toute façon (§ 4).

**Trois enseignements :**
1. **Le vrai prix d'un château de prestige n'est pas son prix d'achat, mais le capital qui le fait vivre.** Pour S2, ce capital vaut environ 34 à 38 fois le prix d'achat retenu (3,5 M€).
2. **Le premier levier se joue avant l'achat**, dans le choix du domaine. Chaque tranche de 100 000 € de besoin annuel demande environ 10 M€ de capital pour 95 % de chances de tenir 30 ans.
3. **Une entreprise peut constituer le capital, pas le remplacer.** Une holding passive de PME, qui ne fait que distribuer ses dividendes, échoue dans 85 à 98 % des cas sur 30 ans (L6, § 4.4). Sa valeur vient de sa **conversion** en capital diversifié.

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
| Faisabilité | Contraintes juridiques, fiscales et d'urbanisme (R3, V2A, V2D, V2R) |
| Preuves | Existence de cas réels documentés, avec des comptes publiés si possible |

Les modèles qui échouent sur la couverture ou sur la tranquillité sont écartés au § 5, avec leurs raisons.

---

## 3. Les cinq modèles

### 3.1 Modèle 1 — Hybride : des entreprises qui construisent le capital (recommandé)

**Principe.**
1. Le propriétaire détient, directement ou par une holding, plusieurs PME rentables et sans dette d'acquisition.
2. Pendant une **période de transition** d'environ 10 ans, leurs dividendes paient une partie du fonctionnement du domaine.
3. Ce qui n'est pas dépensé, puis les produits de cessions éventuelles, sont versés au **capital affecté**, diversifié et géré avec une règle de dépense.
4. Le domaine n'engage son niveau de dépense complet que lorsque ce capital, avec sa règle, couvre le besoin. C'est le seuil de déclenchement (L2, § 6.4).

**Chiffres (S2, modèle).**
- Solution retenue (L4) :
  - capital de 120 M€ au départ ;
  - 1 M€ de dividendes nets par an pendant 10 ans ;
  - réserve de 1,5 M€ ;
  - probabilité d'échec : 1,8 % sur 20 ans et environ 5 % sur 30 ans (L6, § 4).
- Pour 95 % de chances de tenir 30 ans, il faut 117,6 M€ de capital au départ. Pour 95 % sur 20 ans, 85,8 M€ suffisent (`mc_comparaison_modeles.json`).
- 1 M€ de dividendes nets suppose environ 2,8 M€ d'EBITDA, à raison de 0,355 € net par euro d'EBITDA après IS, PFU et contributions sur les hauts revenus (ESTIMATION [R8-35] [V2R-04] [V2R-05]). Une telle entreprise se paie environ 5 à 8 fois son EBITDA, soit 14 à 22 M€.
- En S3, avec 3 M€ de dividendes par an pendant 10 ans, il faut 424,8 M€ de capital pour 95 % sur 30 ans, au lieu de 491,6 M€ sans dividendes.

**Preuves.**
- Northumberland Estates, propriété de la famille d'Alnwick, est une foncière diversifiée qui verse 5 M£ de dividendes par an [R5-14].
- En France, les domaines privés qui tiennent s'appuient en général sur un revenu extérieur : Caudalie à côté de Smith Haut Lafitte, l'activité d'un médecin à Gudanes [R4]. Au Domaine des Étangs, la famille couvre des pertes d'environ 7,6 M€ par an [R4-08].

**Forces.**
- Le rendement d'une PME achetée sans dette (4,4 à 7,1 % du capital investi) dépasse celui d'un portefeuille (1,75 % retirables).
- Le capital peut se constituer par le travail, sans dépendre d'un héritage.

**Faiblesses et risques.**
- Plus d'une transmission de PME sur cinq échoue dans les six ans (données OSEO 1997-2003, souvent des reprises endettées) [R8-36].
- **Forte dépendance au fondateur pendant la constitution.** Sans dividendes, le risque à 30 ans passe de 5 à 7 % (L6, § 4.2).
- **Le délai.** Il faut environ 34 ans d'épargne à 2,5 M€ par an pour réunir 120 M€ à 2 % réel, sauf cession d'entreprise (L4, § 6.2).
- Une holding dont les revenus sont surtout passifs peut tomber sous la taxe de 20 % sur les holdings patrimoniales (loi de finances 2026). Le château habité et les chevaux personnels ne doivent jamais y être logés [R3-18] (à valider).

**Conditions de succès.**
- Au moins cinq entreprises, sans dette d'acquisition au moment où elles financent le domaine, et des dirigeants salariés.
- Une règle de conversion écrite : une part fixe des dividendes et tout produit de cession vont au capital affecté.
- Le seuil de déclenchement est respecté.

### 3.2 Modèle 2 — Capital affecté seul

**Principe.**
- Un capital diversifié est **réservé** au domaine dès le départ, par une charte et, si possible, par des statuts contraignants ou une fiducie (L2, § 6.4).
- Le domaine retire chaque année au plus 1,75 % du capital, selon une règle lissée.
- Une réserve d'un an de charges et un fonds de travaux absorbent les chocs.

**Chiffres (capital seul, avec le socle d'activités).**

| Domaine | Besoin annuel | Une chance sur deux de tenir 30 ans | 95 % de chances |
|---|---:|---:|---:|
| S1 | 0,35 M€ | 14,1 M€ | 37,9 M€ |
| S2 | 1,27 M€ | 50,1 M€ | 132,2 M€ |
| S3 | 3,77 M€ | 165,9 M€ | 491,6 M€ |

Le seuil d'une chance sur deux n'est pas un objectif : à ce niveau, le domaine vit en mode de tension (L6, § 4.3).

**Preuves.**
- **Burghley** : la fondation est « endowed with its own land and property portfolios ». Son revenu immobilier net de 3,52 M£ couvre environ 75 % de ses dépenses caritatives [R5-07].
- **Blenheim** : un fonds dédié de 21,9 M£, avec un objectif de 45 M£ [R5-03].
- Ces fonds britanniques bénéficient d'un régime qui **n'existe pas en France**. Il exige d'ailleurs un accès du public et interdit au constituant de contrôler le fonds [V2R-01].
- Les fonds de dotation universitaires américains dépensent environ 4,9 % par an, mais ils sont exonérés d'impôt [R8-34].

**Forces.**
- C'est le modèle le plus simple et le plus robuste à capital égal : aucune dépendance à une activité ni au fondateur, et aucun tiers sur le domaine.
- Les actifs financiers ne sont pas soumis à l'IFI, contrairement à l'immobilier [R3-01].

**Faiblesses et risques.**
- Il exige un capital considérable, environ 100 fois le besoin annuel, qui reste **la fortune du propriétaire** (L2, § 6.3).
- Le rendement réel net de 2 % est la deuxième hypothèse la plus sensible après le budget. Pour S2 :
  - à 1,5 %, il faut 168,6 M€ ;
  - à 2,5 %, 109,5 M€ (L6, § 4.3).
- Sans montage successoral, environ 44 % du capital part en droits à chaque génération [V2R-06]. Sans contrat de mariage adapté, les revenus réinvestis peuvent devenir communs [V2R-07].

### 3.3 Modèle 3 — Dimensionner le domaine à son capital (sobriété choisie)

**Principe.** Le besoin annuel est la variable qui pèse le plus sur le capital nécessaire. Il faut donc choisir le domaine et son train de vie **en fonction du capital disponible**, et non chercher le capital une fois le domaine acheté.

**Chiffres.**
- Pour 95 % de chances de tenir 30 ans, il faut environ 100 fois le besoin annuel. Chaque tranche de 100 000 € de besoin coûte donc environ 10 M€ de capital.
- Capital seul : S1 demande 37,9 M€, S2 132,2 M€ et S3 491,6 M€.
- Avec les leviers vérifiés par V2C (environ −7,5 % du besoin, sans avantage fiscal), S2 demande 122,1 M€ au lieu de 132,2 M€.
- **Une erreur de budget pèse plus que tout le reste.** Si le besoin réel de S2 se situe au haut de la fourchette de L1, il faut environ 225 M€ (L6, § 4.2).

**Leviers disponibles** (L2, § 5) :
- gestion différenciée du parc (déjà intégrée au budget) ;
- choix de la chaudière et zonage du chauffage ;
- arbitrage sur le personnel de maison et sur le nombre d'hectares de jardins réguliers ;
- achat d'un bien **déjà restauré**, qui évite un rattrapage d'entretien (L1, § 8).

**Forces.** C'est le seul levier gratuit, et il se joue avant l'achat.

**Faiblesses.** Il réduit la surface, les jardins réguliers ou le personnel, qui sont des éléments du brief (« jardins impeccables, personnel suffisant »). Le propriétaire doit arbitrer.

### 3.4 Modèle 4 — Locataire d'ancrage et capital réduit (pour un grand domaine bien situé)

**Principe.** Une partie importante des bâtiments est louée pour 15 à 30 ans à un exploitant de séminaires résidentiels. L'exploitant paie un loyer et prend en charge l'énergie et l'entretien courant de la zone louée. Le propriétaire garde une aile ou une maison privée, ainsi que le gros entretien (L2, § 3.4).

**Chiffres.**
- Contribution centrale : 0,35 M€ par an pour 50 chambres (ESTIMATION fragile : aucun loyer réel de château n'a été trouvé).
- Par prudence, le loyer est traité comme un revenu récurrent de classe B, qui baisse de 15 % en crise, et non comme un revenu contractuel : des loyers ont été suspendus en 2020-2021 [V2A-31] [V2A-62].
- Capital nécessaire pour 95 % de chances de tenir 30 ans :
  - S2 : 114,9 M€ au lieu de 132,2 M€ (−13 %) ;
  - S3, avec 80 chambres : 465,5 M€ au lieu de 491,6 M€ (−5 %).

**Conditions cumulatives** [V2A-13] [V2A-54] :
- moins de 90 km de Paris, ou moins de 45 minutes d'une gare TGV ou d'un aéroport de métropole ;
- au moins 40 chambres ;
- un exploitant qui finance la transformation.

**Forces.** C'est la seule activité sur place à la bonne échelle. Le revenu est contractuel, et l'exploitant porte l'exploitation.

**Faiblesses et risques.**
- **Incompatible avec une partie entièrement privée en S2**, puisqu'il faudrait y mobiliser l'essentiel des bâtiments.
- Engagement quasi irréversible : le refus de renouvellement coûte une indemnité d'éviction [V2A-36].
- Le gros entretien reste au propriétaire [V2A-38].
- Le bail peut être repris par un exploitant que le propriétaire n'a pas choisi [V2A-39].
- Aucun cas documenté d'un propriétaire vivant à côté d'un tel exploitant n'a été trouvé.

### 3.5 Modèle 5 — Vendre une partie du domaine pour amorcer le capital

**Principe.** Le propriétaire cède définitivement des bâtiments ou des terres dont il n'a pas l'usage, à l'écart de la partie privée (communs, hameau, fermes, parcelles), et verse le produit net au capital affecté. Trois formes sont possibles : vente directe, vente à un opérateur qui divise en logements sous le régime des monuments historiques, ou promotion foncière.

**Chiffres.**
- Chaque million d'euros net versé au capital réduit d'autant le capital à trouver par ailleurs, et finance environ 17 500 € de besoin par an.
- Le **prix obtenu est INCONNU** dans les sources. Aucun opérateur ne publie ce qu'il paie au propriétaire, et aucun exemple français de domaine vendant ses communs tout en gardant le château n'a été trouvé [V2D § 1.7] [R8 § 6.2].

**Preuves.**
- **Blenheim** alimente son fonds dédié par la promotion foncière du domaine [R5-03].
- **Castello di Reschio**, en Ombrie : sur environ 1 400 ha, des fermes en ruine sont vendues et restaurées pour des acquéreurs, pendant que la famille garde le château [R8-40] à [R8-43]. Prix inconnus.

**Conditions** (à valider par un notaire) :
- urbanisme : changement de destination, PLU, avis de l'architecte des Bâtiments de France ;
- droit de préemption de la Safer pour les biens agricoles ;
- en cas de division d'un immeuble protégé, 75 % d'habitation dans les 2 ans pour que les acquéreurs gardent le régime fiscal [V2D-16].

**Faiblesses.**
- La vente est définitive et crée des voisins permanents.
- L'appétit des opérateurs n'est pas acquis : le leader a publié de fortes pertes en 2025 [V2D-42].
- Ces opérations peuvent être politiquement sensibles [V2D-17].
- Le modèle n'a de sens que pour un **grand** domaine aux bâtiments dispersés, comme une variante de S3.

---

## 4. Le socle commun : des activités calmes qui entretiennent le domaine

| Activité (échelle S2) | Classe | Contribution centrale | Rôle |
|---|:---:|---:|---|
| Logements dans les communs (600 m²) | A | 33 k€ | Occuper et entretenir des bâtiments ; rendement d'environ 3 % sur 1,08 M€ d'investissement |
| Hivernage de camping-cars (600 m²) | A | 5 k€ | Utiliser une grange sans travaux lourds |
| Bail solaire (5 ha hors du champ de visibilité) | A | 15 k€ | Revenu contractuel long ; accord de l'architecte des Bâtiments de France nécessaire [R3-63] |
| Forêt (30 ha) | A | 2 k€ | Gestion durable du bois ; peut alimenter une chaufferie |
| Pension de retraite au pré | B | 10 k€ | Chevaux au pré, peu de passage ; revenu stable en 2020 [R6-27] |
| Tournages (2 jours par an) | C | 6 k€ | Image et revenu occasionnel, sans engagement |
| **Total disponible après fuite fiscale (modèle M1)** | | **43 k€** | **3 % du besoin de S2** |

**Ce qui a changé après l'équipe rouge.** La pension standard (30 boxes) a été retirée du socle. Elle ne rapporte rien dans le cas central (−1 k€), elle peut coûter 40 k€ dans le cas défavorable, et elle fait venir 25 à 30 propriétaires de chevaux chaque semaine, week-ends compris (V2R m8).

**Règles du socle :**
- pas de réception ni de public ;
- un revenu de classe C ne doit jamais servir à couvrir des charges fixes ;
- les logements doivent respecter les règles de performance énergétique : les logements classés G ne peuvent plus être loués, et les F ne le pourront plus dès 2028 [R3-34].

---

## 5. Modèles écartés et pourquoi

| Modèle ou piste | Raison principale | Références |
|---|---|---|
| Château-hôtel exploité (M4) | Contribution négative dans le cas central (−28 % du besoin) ; 7,5 M€ d'investissement ; 54 à 61 % des sociétés de châteaux-hôtels en perte selon la période des comptes | L2 § 2.2 et 3.6 ; [R4-34] ; V2V |
| Lieu d'exception à quota : réceptions, séminaires, grande maison (M2) | Seulement +32 k€ par an par rapport au socle, pour 1 M€ d'investissement de plus, avec des nuisances ; revenus qui disparaissent en crise (−80 %) | L2 § 3.6 ; L6 § 7 |
| Équestre haut de gamme et reproduction (M3) | Couvre 3 % du besoin ; demande non prouvée hors de l'ouest parisien ; dépend d'un vétérinaire ou du talent du propriétaire | L2 § 3.1 ; [R6-15] |
| Ouverture à la visite | « Pour 99,8 % des propriétaires », la seule ouverture à la visite n'est pas rentable [R1-01] ; foule incompatible avec la tranquillité | L2 § 2.2 |
| Location de luxe de la partie privée (M8) | 39 k€ par an de contribution dans le cas central ; le propriétaire doit quitter sa maison l'été ; environ 2 réservations par an et par propriété chez la plateforme leader | L2 § 3.5 ; [V2D-26] |
| Copropriété ou partage entre familles | Les exemples reposent sur des pièces communes, incompatibles avec une partie entièrement privée | [V2D-43] [V2D-44] |
| Vente de la nue-propriété | Au mieux 20 % de la valeur à 26 ans ; aucun marché identifié ; perte définitive pour les héritiers | [V2D-19] [V2D-30] |
| Mécénat, financement participatif | Tout usage privé est exclu (La Mothe-Chandeniers) ; plafond de 60 000 € de recettes commerciales pour le mécénat de la Fondation du patrimoine | [R4] ; [R3-10] |
| Fonds de dotation ou fondation propriétaire du domaine | Apport gratuit et irrévocable, mission d'intérêt général : c'est un outil de transmission, pas de financement d'une résidence privée | [R8-45] [R8-46] [V2R-02] |
| École ou locataire institutionnel | Flux quotidien de centaines de personnes ; tous les exemples trouvés ont une collectivité pour propriétaire | [R8-26] à [R8-28] |
| Club privé (polo, campagne) | Fréquentation régulière et événements ; le modèle le plus connu, Soho House, n'a jamais été rentable au niveau du groupe | [R8-38] [R8-39] |
| Dette participative | C'est une dette (exemple : 7 % par an), qui ne finance pas un déficit de fonctionnement | [V2D-45] |
| Pistes inhabituelles de petite taille : hydroélectricité, truffière, stockage de vins, crédits carbone, chasse, apprentis | Quelques milliers à quelques dizaines de milliers d'euros, souvent ponctuels ou conditionnés (moulin et droit d'eau, sol, clientèle) | R8 § 1 et § 8 |

---

## 6. Grille de comparaison

Notation qualitative : ●●● favorable, ●● moyen, ● défavorable. Elle résume les sections précédentes ; ce n'est pas un score calculé.

| Critère | 1. Hybride | 2. Capital seul | 3. Domaine dimensionné | 4. Locataire d'ancrage | 5. Vente partielle |
|---|:---:|:---:|:---:|:---:|:---:|
| Couverture du besoin (une fois constitué) | ●●● | ●●● | ●●● (besoin réduit) | ●● (18 % + capital) | ● seul, ●●● avec le capital |
| Capital à réunir au départ | ●● | ● | ●● à ●●● | ●● | ●●● si la vente a lieu |
| Robustesse aux crises (L6) | ●● | ●●● | ●●● | ●● | ●●● une fois versé |
| Tranquillité, partie privée | ●●● | ●●● | ●●● | ● | ●● |
| Prestige du domaine | ●●● | ●●● | ●● | ●● | ●● |
| Indépendance vis-à-vis du fondateur | ● pendant 10 ans, puis ●●● | ●●● | ●●● | ●●● | ●●● |
| Indépendance vis-à-vis de la fortune personnelle | ● (le capital reste à lui) | ● (le capital reste à lui) | ● | ● | ●● (le domaine finance une partie) |
| Faisabilité juridique et fiscale | ●● (holdings, à valider) | ●● (véhicule à valider) | ●●● | ●● (bail commercial) | ● (urbanisme, Safer, ABF) |
| Preuves réelles | ●● (Northumberland) | ●● (Burghley, Blenheim, sous un régime britannique) | ●● (budgets réels de V2C) | ● (aucune cohabitation documentée) | ●● (Blenheim, Reschio) |

---

## 7. Ce qu'on en retient pour la solution (L4)

- **Pour S2**, la solution combine trois éléments :
  - le modèle 3 : valider le budget sur le bien réel et appliquer les leviers vérifiés ;
  - le modèle 1 : constituer le capital par des entreprises, puis convertir leurs revenus ;
  - le socle d'activités calmes.

  Le modèle 5 s'y ajoute si le domaine compte des bâtiments sans usage, éloignés de la partie privée. Le modèle 4 n'est retenu que si la localisation s'y prête et si le propriétaire accepte de réduire sa partie privée.
- **Pour S1**, le même schéma, à une échelle environ 3,5 fois plus petite : 34 M€ de capital et 0,4 M€ de dividendes pendant 10 ans donnent le même niveau de risque que la solution S2 (L6, § 4.1).
- **Pour S3**, le modèle 4 devient une option sérieuse, car la taille permet de garder une aile privée. Le capital nécessaire reste de l'ordre de 330 à 490 M€, selon le montage et l'horizon visé (20 ou 30 ans).

L4 détaille la solution S2 sur 20 ans : montage, flux annuels, règles et indicateurs.
