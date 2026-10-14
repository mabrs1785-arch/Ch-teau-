# L1 — Combien coûte réellement, chaque année, un grand château de prestige ?

> **Statut de ce document**
> - Estimation argumentée, en euros constants 2026, TTC pour un propriétaire particulier.
> - Les identifiants entre crochets ([R1-05], [R2-11]…) renvoient au registre des sources (`04_SOURCES/Registre_sources.csv`).
> - Les calculs sont dans `02_MODELE/sorties/Modele_equation_chateau.xlsx`, feuilles Hypotheses et Budget. Chaque cellule est une formule, vérifiée par un calcul Python indépendant (11 814 formules, 0 écart).
> - Version révisée après l'équipe rouge (V2R) : maîtrise d'œuvre et dommages-ouvrage ajoutés, soigneur de S1 porté à 1 ETP.
> - Statuts des hypothèses : SOURCÉ, ESTIMATION (raisonnement sur sources), HYPOTHÈSE (choix de modélisation à valider).

---

## 1. La réponse en une page

| Domaine type | Description résumée | Besoin annuel central | Fourchette (tout favorable – tout défavorable) |
|---|---|---:|---:|
| **S1 — relativement économique** | Château de 900 m², 600 m² de dépendances, 50 ha, 12 boxes, 2,5 salariés | **≈ 0,35 M€** | 0,21 – 0,60 M€ |
| **S2 — grand domaine équestre haut de gamme** | Château inscrit de 2 000 m², 2 500 m² de dépendances, 120 ha, manège, 40 boxes, 10 salariés | **≈ 1,27 M€** | 0,79 – 2,16 M€ |
| **S3 — domaine historique ultra-premium** | Château classé de 4 500 m² avec décors, 4 000 m² de dépendances, 300 ha, 10 ha de jardins réguliers, 29,5 salariés | **≈ 3,77 M€** | 2,20 – 6,80 M€ |

Ce besoin couvre tout ce que le brief demande de financer :
- entretien courant et gros entretien du bâti ;
- personnel ;
- jardins et terres ;
- énergie ;
- assurances ;
- équipements ;
- chevaux du propriétaire et installations ;
- impôts et taxes, IFI compris ;
- administration ;
- imprévus ;
- investissements futurs.

Il exclut l'achat, la restauration initiale et le train de vie personnel du propriétaire. Deux postes n'ont pas pu être chiffrés et n'y figurent pas non plus : les chevaux de sport (achat, renouvellement, transport, concours) et les infrastructures du domaine (murs d'enceinte, allées, réseaux, étangs, ponts) (§ 8).

**Six enseignements :**

1. **Un château entretenu sans retard coûte chaque année environ 8 à 11 % de sa valeur de reconstruction.** Pour S2, c'est environ un tiers du prix d'achat retenu (3,5 M€), **chaque année**. Sur 20 ans, le propriétaire dépense donc environ 7 fois le prix du château. La valeur de marché d'un château est très inférieure à son coût de reconstruction : selon un courtier, celui-ci peut valoir 10 fois le prix d'achat [R1-26]. C'est le « piège du château » : on l'achète au prix du marché, mais on l'entretient au prix de la reconstruction.
2. **Deux postes font l'essentiel.**
   - Le **bâti** représente 39 à 49 % du besoin. La provision de gros entretien en constitue la plus grande part.
   - Le **personnel** représente 21 à 32 % du besoin.
   - Énergie, taxes et assurances, réunies, n'en représentent qu'environ 10 à 13 %.
3. **Le gros entretien est le poste le plus incertain et le plus souvent sous-estimé.**
   - Les maisons historiques britanniques dépensent en moyenne ≈ 156 000 à 161 000 £ TTC par an pour leur seul bâtiment principal. Elles accumulent pourtant un retard d'entretien moyen d'environ 2 M£ chacune [R1-05].
   - Une dépense « normale » ne suffit donc pas à maintenir un état d'exception.
4. **La trésorerie n'est pas lisse.** Les provisions de gros entretien se dépensent par campagnes de travaux. En S2, la projection donne des campagnes d'environ 1,40 à 1,58 M€ tous les quatre ans. Il faut un **fonds de travaux** distinct de la trésorerie courante.
5. **Les « budgets déclarés » sont trompeurs.** Un vendeur de petit château MH (512 m² habitables) déclare environ 14 600 €/an de charges, mais sans aucun gros entretien [R1-32]. La Demeure Historique avance un plancher de 40 000 €/an par monument, **hors restauration** [R1-01]. Ces chiffres mesurent ce que les propriétaires dépensent, pas ce que coûte un état d'exception.
6. **Les deux paramètres qui font varier le résultat** sont la valeur de reconstruction au m² et le taux annuel de gros entretien. Pour S2, ils déplacent chacun le besoin d'environ ±0,12 à 0,17 M€ (§ 6). Ce sont les premières données à faire chiffrer par un architecte du patrimoine et un assureur sur un bien réel.

---

## 2. Méthode

1. **Trois domaines types** décrits physiquement : surfaces, toitures, façades, hectares par usage, boxes, effectifs. Ce sont des choix de scénario, documentés dans la feuille Hypotheses, groupe « Scénarios — description physique ».
2. **Un budget ligne par ligne**, chaque ligne = quantité × coût unitaire sourcé. Par exemple, effectif × coût employeur URSSAF, ou surface chauffée × consommation × prix du kWh.
3. **Trois cas par hypothèse** : favorable, central, défavorable. Les colonnes « favorable » et « défavorable » cumulent toutes les bornes dans le même sens. Ce sont donc des **bornes extrêmes**, peu probables, pas des intervalles de confiance.
4. **Le gros entretien** est calculé comme la valeur de reconstruction × un taux annuel. On retient la règle du National Research Council, pour qui l'entretien et la réparation d'un parc de bâtiments exigent 2 à 4 % de la valeur de remplacement [R1-07][R1-08]. Le NRC présente ce taux comme un minimum « en l'absence d'information spécifique », valable pour un parc de bâtiments et en moyenne sur 5 à 10 ans ; un bâtiment isolé peut sortir de la fourchette [V2V-02].
   - Faute de prix au m² publics et fiables pour les travaux sur monuments historiques, la méthode par composants (toiture, façades, menuiseries) n'a pas pu être sourcée [R1, § 2.1]. Elle n'est utilisée que comme contrôle qualitatif.
5. **Euros constants 2026, TTC.** Un particulier ne récupère pas la TVA. Une ligne indique le besoin si une société assujettie portait les charges et récupérait la TVA.

---

## 3. Les trois domaines types

| Paramètre | S1 | S2 | S3 |
|---|---|---|---|
| Château (surface de plancher) | 900 m² | 2 000 m² (inscrit MH) | 4 500 m² (classé MH, décors) |
| Dépendances | 600 m² | 2 500 m² | 4 000 m² |
| Toitures développées (estimation géométrique) | ≈ 1 200 m² | ≈ 3 300 m² | ≈ 6 000 m² |
| Foncier | 50 ha (35 de prés, 12 de bois, 3 de parc) | 120 ha (80 prés, 30 bois, 8 parc, 2 jardins réguliers) | 300 ha (120 prés, 120 bois, 50 parc, 10 jardins réguliers) |
| Équestre | 12 boxes, carrière ; 4 chevaux du propriétaire | 40 boxes, manège, 2 carrières ; 8 chevaux | 50 boxes, manège ; 12 chevaux |
| Personnel du domaine (hors activité commerciale) | 2,5 ETP | 10 ETP | 29,5 ETP |
| Prix d'achat retenu (HYPOTHÈSE ; marché : prix affichés de 920 k€ à 20 M€ [D-02]) | 1,2 M€ | 3,5 M€ | 9 M€ |

**Effectifs.** Les effectifs ne couvrent que le domaine et les chevaux du propriétaire.
- L'agent R2 obtient 13 ETP pour S2 et 29 ETP pour S3 s'il compte une écurie pleine de 40 à 50 chevaux. Cet excédent relève d'une activité de pension, traitée comme un moteur de revenus (livrable L2).
- La composition des effectifs (régisseur, chef jardinier, jardiniers, maintenance, ouvrier agricole, soigneur, responsable d'écurie, gouvernance de maison, employés de maison) est détaillée dans la feuille Hypotheses.
- **Jardiniers, après la vague 2.** L'agent V2C a appliqué aux surfaces des scénarios les temps d'entretien mesurés par la Ville de Rennes [V2C-21]. Ces temps vont de 2 800 h/ha/an pour un jardin très fleuri à 90 h/ha/an pour une prairie fauchée.
  - En S2, les 2 jardiniers et le chef jardinier suffisent à condition de gérer 6 des 10 ha du parc en prairie ou en pelouse champêtre (gestion différenciée). Un parc soigné partout demanderait environ 5,5 ETP.
  - En S3, les 11 jardiniers retenus par R2 étaient sous-estimés. Il en faut au moins 15,7 dans la variante la plus extensive. Le modèle retient désormais **16 jardiniers**, plus le chef, ce qui relève le besoin de S3 d'environ 0,17 M€.
  - Le budget suppose donc partout une **gestion différenciée** : soin maximal près du château et sur les perspectives, prairies au-delà. C'est d'ailleurs la composition classique d'un domaine (Vaux-le-Vicomte : 33 ha de jardins dans un parc de 500 ha [V2C-25]).

---

## 4. Résultats détaillés

Tableau généré depuis le modèle (`02_MODELE/tableaux.py`) :

| Poste (€ 2026 TTC par an, cas central) | S1 | S2 | S3 |
|---|---:|---:|---:|
| Bâti : entretien courant | 27 k€ | 90 k€ | 341 k€ |
| Bâti : provision de gros entretien, aléas de chantier et maîtrise d'œuvre | 103 k€ | 344 k€ | 1 300 k€ |
| Sécurité | 2 k€ | 7 k€ | 25 k€ |
| Personnel | 73 k€ | 404 k€ | 1 110 k€ |
| Jardins, parc, prairies, clôtures, bois (hors personnel) | 16 k€ | 44 k€ | 133 k€ |
| Équipements (renouvellement, entretien, carburant) | 27 k€ | 80 k€ | 106 k€ |
| Chevaux du propriétaire et installations équestres | 24 k€ | 70 k€ | 91 k€ |
| Énergie et eau | 24 k€ | 59 k€ | 125 k€ |
| Assurances | 14 k€ | 45 k€ | 156 k€ |
| Impôts et taxes (foncières, IFI) | 7 k€ | 29 k€ | 91 k€ |
| Administration et suivi patrimonial | 8 k€ | 31 k€ | 85 k€ |
| Imprévus d'exploitation | 6 k€ | 23 k€ | 64 k€ |
| Investissements futurs | 13 k€ | 48 k€ | 143 k€ |
| **Besoin annuel total (central)** | **346 k€** | **1 273 k€** | **3 771 k€** |
| Fourchette favorable – défavorable | 208 k€ – 603 k€ | 787 k€ – 2 158 k€ | 2 204 k€ – 6 802 k€ |
| Effectif salarié (ETP) | 2,5 | 10,0 | 29,5 |
| Part du personnel / part du bâti | 21,0 % / 43,3 % | 31,7 % / 38,8 % | 29,4 % / 48,7 % |
| Valeur de reconstruction retenue | 3,6 M€ | 12,0 M€ | 45,5 M€ |
| Besoin en % de la valeur de reconstruction | 9,6 % | 10,6 % | 8,3 % |
| Besoin par m² bâti | 230 €/m² | 283 €/m² | 444 €/m² |
| Si porté par une société assujettie (TVA récupérée) | 315 k€ | 1 179 k€ | 3 506 k€ |
| Scénario complémentaire : + annuité de dette (70 % du prix, 20 ans, 4,2 %) | 63 k€ | 183 k€ | 472 k€ |
| Total avec dette | 409 k€ | 1 457 k€ | 4 242 k€ |

### 4.1 Justification des principaux postes

**Bâti.**
- Valeur de reconstruction retenue :
  - S1 : 3 000 €/m² ;
  - S2 : 3 700 €/m² ;
  - S3 : 7 000 €/m² ;
  - dépendances : à 50 % de ces valeurs.
- Ces valeurs sont encadrées par deux sources :
  - 2 400 €/m² de surface développée, dans l'exemple d'un courtier publié par le Figaro en 2020 [R1-26] ;
  - 5 000 à 10 000 €/m², selon le barème d'un courtier en 2026 (fiabilité faible) [R1-27].
- Entretien courant : 0,75 % de cette valeur par an. Gros entretien : 2,25 %. Aléas de chantier : 15 % du gros entretien, à comparer au dépassement de +29 % observé sur un chantier britannique [R1-05].
- **Maîtrise d'œuvre, diagnostics, coordination de sécurité et assurance dommages-ouvrage : 12 % du gros entretien** (HYPOTHÈSE, 8 à 18 %), soit 10 / 32 / 123 k€ par an pour S1 / S2 / S3. Sur un monument classé, l'architecte est obligatoire, le diagnostic préalable aussi, et l'assurance dommages-ouvrage est obligatoire [V2R-09]. Aucun barème public n'a été trouvé, et on ignore si la règle du NRC inclut déjà ces coûts : ils sont donc ajoutés par prudence (constat de l'équipe rouge, V2R M8).
- Montants réels de chantiers : une tranche de toiture d'un château privé coûte de 42 000 à 393 000 € par opération, souvent réalisée en plusieurs phases faute de trésorerie [R1-11 à R1-16]. À Blenheim, la seule tranche de toiture en cours représente 10,4 M£ sur deux ans [R5-03].

**Personnel.**
- Coût employeur calculé par l'agent R2 avec le simulateur officiel de l'URSSAF, réforme des allègements de 2026 comprise [R2-11]. Un salaire au SMIC (12,31 €/h depuis juin 2026) coûte environ 23 900 €/an à l'employeur ; un salaire à 2,5 SMIC, environ 79 000 €.
- Le personnel de maison employé à titre privé ne bénéficie pas des allègements ; il est compté au brut × 1,30, estimation fragile [R2-12].
- En S1, le soigneur est compté à temps plein (1 ETP) : un cheval se soigne 365 jours par an, et 0,6 ETP aurait laissé le reste au propriétaire (V2R m13).
- Les niveaux de salaire (multiples du SMIC) sont des hypothèses : aucun salaire de marché publié n'a été trouvé pour les régisseurs, chefs jardiniers ou majordomes [R2, § 2.2].
- Repères d'effectifs :
  - Villandry : 10 jardiniers pour 7 ha de jardins réguliers, soit environ 1,4 par ha, un plafond [R2-15] ;
  - Chatsworth : 29 jardiniers et 32 agents de maintenance en moyenne [R5-05] ;
  - jardins de Vaux-le-Vicomte : environ 24 000 à 27 000 € par hectare et par an, bassins compris, ce qui correspond au code 2 « jardin structuré » des temps de Rennes [V2C-24] [V2C-21].

**Énergie.**
- Surfaces chauffées : 450 / 1 000 / 1 800 m².
- Consommation : 220 kWh/m², une hypothèse, car aucune mesure de château n'a été trouvée.
- Prix de la chaleur : 0,15 € TTC/kWh, entre les granulés (10,4 c€ en 2023 [R1-22]) et le gaz (19,49 c€ au 1er novembre 2026 [R1-25]).
- Électricité : 0,238 € TTC/kWh [R1-24].
- L'énergie pèse peu (3 à 7 % du besoin), mais un changement de combustible fait varier la facture d'un facteur 2.
- Le prix repère du gaz (19,49 c€) est celui du seul mois de novembre 2026, après deux hausses successives [V2V].

**Assurances.**
- Taux retenu : 3 ‰ de la valeur de reconstruction. Il se situe entre deux repères qui divergent :
  - le barème d'un courtier, d'environ 5 ‰ [R1-27] ;
  - des cas observés 3 à 10 fois plus bas [R1-28][R1-32].
- Le risque de non-assurabilité est réel : l'assureur du château d'Olhain a résilié son contrat, et le site est fermé au public depuis le 1er janvier 2026 [R1-28].

**Impôts.**
- Taxe foncière : la base est la moitié de la valeur locative cadastrale, et la catégorie des monuments a été fixée en 1970 [R1-30][R1-31]. Un seul repère a été trouvé : 2 652 € pour 512 m² habitables [R1-32]. L'hypothèse retenue est de 6 €/m² pour le château et 2 €/m² pour les dépendances.
- IFI : les monuments historiques n'en sont pas exonérés. Le calcul applique le barème 2026, avec un abattement de 30 % puisque le château est la résidence principale [R3-01][R3-15]. Il donne :
  - S1 : 0 € (sous le seuil) ;
  - S2 : 10 550 € ;
  - S3 : 51 940 €/an.
  Hors résidence principale : 20 690 € (S2) et 85 690 € (S3).
  - Simplification à corriger sur un bien réel : l'abattement de 30 % ne vise que la résidence principale, alors que le modèle l'applique à tout le prix d'achat. Les terres, les bois et les biens ruraux loués ont leurs propres régimes [R3-01] ; l'écart est de quelques milliers d'euros par an (V2R m11).

**Chevaux et équipements.**
- Environ 4 000 € par cheval et par an hors personnel : alimentation, litière, maréchal, vétérinaire, assurance. Les prix IFCE de 2012 sont actualisés d'environ 20 % [R2-17][R2-18][R2-24].
- Matériel valorisé selon le guide des coûts des CUMA 2025-2026 (tracteur de 100 à 140 ch : 101 464 € HT, amorti en 10,7 ans) [R2-30]. Le renouvellement du matériel représente 17 à 66 k€/an selon le scénario.

---

## 5. Recoupements avec des cas réels

| Repère | Montant | Comparaison avec le modèle |
|---|---|---|
| Plancher de La Demeure Historique, hors ouverture et hors restauration (2019) [R1-01] | ≥ 40 000 €/an | Dans le modèle, S1 coûte 346 k€ ; mais, en ne gardant que l'entretien courant, les assurances, les taxes et un homme d'entretien, on obtient environ 80 k€. Le plancher de la DH est cohérent avec ce périmètre restreint. |
| Maisons historiques britanniques, dépense annuelle d'entretien et de réparation du bâtiment principal (2024) [R1-05] | 156 000 à 161 000 £ TTC (≈ 185 000 à 190 000 €), avec un retard moyen d'environ 2 M£ | Le modèle S2 prévoit 434 k€/an pour le bâti hors assurance et taxes (entretien courant, gros entretien, aléas et maîtrise d'œuvre), soit environ le double de ce qui est réellement dépensé au Royaume-Uni. Cette dépense observée y est jugée insuffisante. |
| Chatsworth (2024-25) [R5-05] | Jardins, parc et bois : 1 781 k£ ; entretien courant de la maison et des écuries : 2 705 k£ ; réparations : 1 207 k£ ; assurance : 342 k£ | Ordre de grandeur cohérent avec S3, pour un domaine plus grand (environ 1 822 acres gérés par la fondation). |
| Blenheim (2024-25) [R5-03] | Conservation et entretien : 3 791 k£, objectif de 4 M£/an de restauration ; toiture : 10,4 M£ sur 2 ans | Confirme l'ordre de grandeur du gros entretien des grands monuments (au-delà de S3). |
| Vaux-le-Vicomte [R4-30][R4-31] | Budget de 8 à 9 M€/an, 75 ETP, tourisme compris | Monument hors norme : le budget inclut l'exploitation touristique. |
| Chantilly [R4-46][R4-47] | Charges ≈ 13 M€ (2020, extrait) ; besoin de restauration de 68 M€ sur 10 ans | Échelle d'un monument national. |
| Petit château MH, 512 m² habitables, charges déclarées par le vendeur [R1-32] | ≈ 14 600 €/an, sans gros entretien | Illustre l'écart entre charges déclarées et coût complet. |
| Rapport IGF-IGAC sur les monuments historiques privés (février 2020) [V2C-07] | Dépense des propriétaires privés : au moins 535 M€/an, soit environ 24 000 € par monument ; modèle jugé « de plus en plus difficilement viable » | Seule évaluation publique d'ensemble. Le profil « résident », le plus proche de notre propriétaire, ne finance pas sa part des gros travaux sans revenus extérieurs. |
| Charges courantes déclarées pour de petits châteaux (annonces, courtier, plancher de La Demeure Historique) [V2C] | 15 000 à 80 000 €/an, hors gros travaux | S1 (346 k€) est 4 à 23 fois au-dessus : c'est un budget **nécessaire**, pas un budget **observé**. |

**Lecture.** Le modèle est **plus exigeant que les dépenses réellement observées**. C'est voulu : le brief demande un château restauré et maintenu dans un état d'exception. Les dépenses observées correspondent à des propriétaires qui, en moyenne, accumulent du retard d'entretien. Un propriétaire réel peut dépenser beaucoup moins pendant quelques années (au Royaume-Uni, la dépense observée pour le bâtiment principal représente environ la moitié de ce que le modèle S2 prévoit pour le bâti, voir le tableau), mais il **consomme alors son patrimoine** : le retard s'accumule et se paiera plus tard.

---

## 6. Ce qui fait varier le besoin

Les hypothèses sont modifiées **une à une**, de leur valeur favorable à leur valeur défavorable. L'écart est mesuré par rapport au besoin central. Script : `02_MODELE/sensibilite.py` ; résultats : `02_MODELE/sorties/sensibilite_budget.json`.

| Hypothèse | S1 | S2 | S3 |
|---|---:|---:|---:|
| Valeur de reconstruction du château (€/m²) | −29 / +49 k€ | −120 / +173 k€ | −532 / +799 k€ |
| Taux de gros entretien (1,5 % – 3 %) | ±36 k€ | ±119 k€ | ±451 k€ |
| Valeur des dépendances (40 – 60 % du château) | ±7 k€ | ±38 k€ | ±115 k€ |
| Entretien courant (0,5 – 1 %) | ±10 k€ | ±32 k€ | ±122 k€ |
| Investissements futurs (2 – 6 %) | ±7 k€ | ±24 k€ | ±71 k€ |
| Taux d'assurance (1,5 – 5 ‰) | −6 / +8 k€ | −19 / +26 k€ | −73 / +97 k€ |
| Maîtrise d'œuvre et dommages-ouvrage (8 – 18 % du gros entretien) | −3 / +5 k€ | −11 / +17 k€ | −43 / +64 k€ |
| Coût d'un jardinier (1,1 – 1,3 SMIC) | ±4 k€ | ±9 k€ | −72 / +69 k€ |
| Prix et consommation de chauffage | prix ±6 k€ ; consommation −5 / +6 k€ | prix ±13 k€ ; consommation −11 / +13 k€ | prix ±26 k€ ; consommation −20 / +23 k€ |

**Les effectifs ne sont pas un paramètre incertain : c'est un choix de train de vie.** Chaque ETP ajouté coûte de 24 k€ (soigneur) à 79 k€ (régisseur). Supprimer le poste de gouvernante (≈ 41 k€) et celui d'ouvrier agricole (≈ 33 k€, diminué du coût de la fenaison sous-traitée) réduirait le besoin S2 d'environ 50 à 70 k€/an (livrable L2, leviers « prestige efficace »).

---

## 7. Trésorerie réelle : le gros entretien par campagnes

La projection sur 20 ans (feuilles `Proj_*`) verse chaque année la provision dans un fonds de travaux, dépensé tous les 4 ans :

| | Provision annuelle (an 1 → an 20) | Campagnes projetées |
|---|---|---|
| S1 | 104 → 119 k€ | ≈ 0,42 à 0,47 M€ tous les 4 ans |
| S2 | 346 → 399 k€ | ≈ 1,40 à 1,58 M€ tous les 4 ans |
| S3 | 1 310 → 1 510 k€ | ≈ 5,3 à 6,0 M€ tous les 4 ans |

La provision augmente de 0,75 % par an au-delà de l'inflation, au rythme de l'indice INSEE de l'entretien-amélioration des bâtiments sur 2005-2025 [V2C-03]. La couverture a dérivé plus vite (+1,26 % par an), et les métiers des monuments historiques n'ont pas d'indice public.

La provision comprend désormais les aléas de chantier et la maîtrise d'œuvre. Chaque campagne dépense quatre années de provisions, ce qui suppose un fonds constitué à temps. Si la réserve tombe sous un an de charges, les règles de pilotage du modèle reportent 30 % de la campagne (L6). Un sinistre non assuré est payé **en plus** du fonds de travaux : il ne remplace pas des travaux prévus (correction V2R M1).

**Conséquence.**
- Il faut constituer le fonds **avant** la première campagne, ou acheter un bien déjà restauré.
- Les subventions des DRAC s'ajoutent rarement, avec retard, et ne sont jamais acquises :
  - taux moyen de 20 % pour un monument inscrit et 40 % pour un classé [R1-34] ;
  - crédits en baisse dans le projet de loi de finances pour 2026 : −29 % en crédits de paiement selon le Sénat ; −13 % (de 128,7 à 112 M€) sur un périmètre plus étroit selon l'Assemblée nationale [R1-33][R1-34]. Les deux chiffres ne portent pas sur le même périmètre [V2V] ;
  - aucune subvention si les travaux ont commencé [R1-03].

---

## 8. Ce que ce budget n'inclut pas

- **L'achat et la restauration initiale.** Un château mis en vente peut porter un retard d'entretien élevé : environ 2 M£ en moyenne dans l'échantillon britannique [R1-05]. Ce rattrapage relève du plan d'acquisition.
- **Le train de vie personnel** du propriétaire.
- **Les chevaux de sport** : achat et renouvellement des chevaux, camion de transport, engagements et déplacements en concours. Le budget ne compte que l'entretien courant de 4 à 12 chevaux du propriétaire (environ 4 000 € par cheval et par an hors personnel). Pour un propriétaire passionné, ce poste peut ajouter plusieurs dizaines de milliers d'euros par an (HYPOTHÈSE de l'équipe rouge : +15 à 40 k€ en S2, non sourcée).
- **Les infrastructures du domaine** : murs d'enceinte, allées, voirie, réseaux, assainissement, étangs et ponts. La règle du NRC exclut ces ouvrages, et aucun ordre de grandeur sourcé n'a été trouvé : leur coût est INCONNU et doit être chiffré sur métré pour un bien réel (V2R m10).
- **Les mises aux normes liées à une activité** : salle ERP, accessibilité. Elles sont comptées dans les moteurs de revenus (L2).
- **L'avantage fiscal MH** (déduction des charges du revenu global), qui réduit l'impôt du propriétaire mais ne diminue pas les dépenses. Il est traité dans L2 et L4.

---

## 9. Incertitudes et vérifications prioritaires

| Donnée | Pourquoi elle compte | Comment la vérifier |
|---|---|---|
| Valeur de reconstruction au m² | Premier facteur de variation : −0,03 / +0,05 M€ par an pour S1, −0,12 / +0,17 M€ pour S2, −0,53 / +0,80 M€ pour S3 (§ 6) | Estimation par l'assureur (valeur à neuf ou valeur agréée), au moins 3 devis de courtiers spécialisés |
| État sanitaire et taux de gros entretien | Second facteur | Diagnostic quinquennal par un architecte du patrimoine. Au Royaume-Uni, seuls 36 % des propriétaires en ont un [R1-05] |
| Prime d'assurance | Divergence non résolue d'un facteur 3 à 10 | Devis réels |
| Taxe foncière d'un grand château | Un seul repère | Avis de taxe foncière du bien visité, à demander dans le dossier de vente |
| Salaires de marché de l'encadrement | Aucune source publique | 20 à 30 annonces datées, ou un cabinet de recrutement |
| Consommation d'énergie réelle | Aucune mesure publiée | Factures des trois dernières années du bien visité |

**Conclusion de L1.** Un grand château de prestige, entretenu au niveau exigé par le brief, coûte **environ 1,3 M€ par an pour un domaine équestre haut de gamme (S2)**, avec une fourchette de 0,8 à 2,2 M€. Il coûte environ 0,35 M€ pour un domaine plus modeste et 3,8 M€ pour un grand monument classé. Ces montants sont des besoins de trésorerie : il faut les produire chaque année après impôts, quelle que soit la conjoncture. C'est l'objet des livrables L2 à L6.
