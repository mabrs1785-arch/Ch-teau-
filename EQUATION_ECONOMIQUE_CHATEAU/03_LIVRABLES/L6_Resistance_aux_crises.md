# L6 — Le modèle résiste-t-il aux crises ? Stress tests sur 20 ans et simulation sur 30 ans

> **Statut de ce document**
> - Résultats calculés, en euros constants 2026. Ce sont des **simulations conditionnelles** : elles décrivent ce qui arrive **si** les hypothèses sont justes. Ce ne sont pas des prévisions.
> - Projections déterministes : `02_MODELE/sorties/Modele_equation_chateau.xlsx`, feuilles `Proj_*`, `ST_*` et `Stress_synthese`. Le classeur compte 11 301 formules recalculées, sans erreur ni écart avec le calcul Python indépendant.
> - Simulation de Monte-Carlo : `02_MODELE/monte_carlo.py` et `02_MODELE/calculer_mc.py`, avec les résultats dans `02_MODELE/sorties/mc_*.json`. Sans chocs aléatoires, la simulation reproduit les projections du classeur à moins d'un millionième d'euro près (contrôle automatique `verifier_jumeau`, consigné dans `sorties/verification.json`).
> - Les identifiants entre crochets renvoient au registre des sources. Statuts : SOURCÉ, ESTIMATION (raisonnement sur sources), HYPOTHÈSE (choix de modélisation à valider).

---

## 1. La réponse en une page

### Sans moteur extérieur, il n'y a rien à stresser

Le domaine S2 est en déficit dès la première année. Les activités sur place apportent en moyenne 47 k€ par an, pour un besoin qui passe de 1,25 à 1,38 M€ en 20 ans. La réserve de 1,5 M€ ne couvre même pas la première année, puisqu'il faut aussi financer 1,1 M€ d'investissement initial des activités. Le déficit cumulé atteint 22,5 M€ en année 20 (feuille `Proj_S2_sans_moteur`).

### La solution recommandée passe les huit stress tests sur 20 ans

Le montage S2 réunit :
- une dotation affectée de 60 M€ ;
- des dividendes de transition de 1 M€ par an pendant 10 ans ;
- une réserve de trésorerie de 1,5 M€ ;
- des règles de pilotage écrites.

Aucune année n'est en déficit, y compris quand tous les chocs sont cumulés : activités −30 %, crise de type 2020, sinistre de 600 k€ et salaires +1,5 % par an au-delà de l'inflation. C'est le **capital de la dotation** qui encaisse les chocs, pas la trésorerie. Dans le pire cas testé, la dotation finit l'année 20 à 60 M€, contre 88 M€ dans le cas central.

### Sur 30 ans, avec des chocs tirés au hasard, le risque d'échec est d'environ 1 sur 9

Sur 20 000 trajectoires simulées, environ **4 à 6 %** échouent avant 20 ans et environ **11 à 12 %** avant 30 ans. Le niveau est le même pour S1, S2 et S3, parce que les trois solutions ont été dimensionnées pour cela.

Un « échec » signifie qu'une année donnée, ni la dotation (dans la limite de sa règle), ni les dividendes, ni la réserve ne suffisent. Il faut alors remettre de l'argent extérieur ou réduire durablement le niveau d'entretien.

### Ce qui fait vraiment rompre le modèle, c'est le dimensionnement, pas la crise

| Facteur (domaine S2) | Échec avant 20 ans | Échec avant 30 ans |
|---|---:|---:|
| **Solution de référence** | **4,3 %** | **11,1 %** |
| Besoin réel au haut de la fourchette de L1 (2,06 M€ au lieu de 1,24 M€) | 30,5 % | 44,6 % |
| Dotation de 40 M€ au lieu de 60 M€ | 17,3 % | 29,9 % |
| Aucune règle de pilotage | 11,1 % | 21,5 % |
| Besoin réel supérieur de 20 % | 9,8 % | 19,7 % |
| Rendement réel net de 2 % au lieu de 3 % | 7,3 % | 18,9 % |
| Pas de dividendes de transition | 8,0 % | 16,6 % |
| Une crise tous les 8 ans au lieu de tous les 12 ans | 5,6 % | 13,0 % |
| Énergie ×2 pendant 3 ans, ou activités −30 % (tests déterministes) | aucun déficit | — |

Sources : `sorties/mc_ruptures_S2.json` (10 000 trajectoires par ligne) et feuilles `ST_*`.

### Trois conclusions

1. **La première protection est un budget juste.** Une erreur de 20 % sur le besoin double à peu près le risque. Si le besoin réel se situe au haut de la fourchette, le risque est multiplié par quatre à sept. Pour retrouver 95 % de chances de tenir 30 ans avec une dotation seule, il faudrait alors environ 143 M€, contre 85,5 M€ avec le budget central. Le capital ne doit donc pas être dimensionné avant que le budget ait été validé par des devis et par un an d'exploitation réelle (L7, phase 1).
2. **La deuxième protection est la discipline de dépense.** Sans règles de pilotage écrites et respectées, le risque double. C'est là que se loge la dépendance au fondateur (§ 6).
3. **Les activités sur place ne protègent de rien.** Leur effondrement ne change presque rien, parce qu'elles pèsent peu. Le château-hôtel aggraverait au contraire le risque, puisqu'il perd de l'argent même en année normale (L2, § 3.6).

---

## 2. Méthode

### 2.1 Projection déterministe sur 20 ans (Excel)

- **Besoin annuel** : celui de L1, en euros constants 2026.
- **Dérives réelles annuelles** (au-delà de l'inflation), calées sur les séries de l'INSEE 2005-2025 :
  - salaires : +0,5 % [V2C-05] [D-01] ;
  - travaux : +0,75 % [V2C-03] ;
  - énergie : +2 % [V2C-04] ;
  - assurances : +1,85 % [V2C-19].
  - Ce sont des ESTIMATIONS.
- **Gros entretien** : provisionné chaque année dans un fonds de travaux et dépensé par campagnes tous les 4 ans (HYPOTHÈSE).
- **Activités sur place** : montée en charge (40 % de leur régime l'année 1, 75 % l'année 2). La contribution est diminuée d'une fuite fiscale de 30 % (ESTIMATION, L2 § 4).
- **Dotation** : rendement réel net de 3 % par an [R8-32] [R8-34] (ESTIMATION). Le retrait est plafonné par une règle de dépense lissée (HYPOTHÈSE de règle inspirée des fonds de dotation [R8-34]) :
  - plafond de l'année = 80 % × plafond de l'année précédente + 20 % × 2,75 % × dotation.
- **Réserve de trésorerie** : maintenue à au moins un an de besoin. Les excédents et les déficits passent par la dotation.

**Échec** : la réserve de trésorerie devient négative.

**Règles de pilotage incluses dans le modèle** (HYPOTHÈSES). Quand la réserve passe sous un an de besoin :
- on coupe 10 % du besoin en dépenses discrétionnaires : investissements futurs, imprévus, achats reportables ;
- on reporte 30 % de la campagne de travaux en cours (le report reste dû) ;
- on autorise un retrait d'urgence plafonné à 4 % du capital.

### 2.2 Les huit stress tests

| Test | Choc appliqué | Calibrage |
|---|---|---|
| Activités −30 % | Contribution des activités −30 % dès l'année 3 | Demandé par le brief |
| Crise de type 2020 | Année 5 : activités occasionnelles −80 %, récurrentes −15 %, contractuelles −5 % ; rendement de la dotation −25 points ; dividendes −50 %. Reprise partielle en année 6 | CA de Châteauform' −69 % en 2020 [R7-26] ; loyers variables de Covivio −67 % au premier semestre 2020 [V2A-31] ; mariages en chute en 2020 [R7-16]. Les chocs de −15 %, −5 %, −25 points et −50 % sont des HYPOTHÈSES |
| Travaux | Sinistre ou découverte non assurés de 600 k€ en année 6 ; campagnes de gros entretien +30 % | HYPOTHÈSE ; chantiers réels de 370 000 à 450 000 € pour une seule tour [V2C-07] |
| Énergie | Prix de l'énergie ×2 des années 4 à 6 | Plus dur que les chocs observés en 2021-2024, de +40 à +66 % [V2C-04] |
| Salaires | +1,5 % par an au-delà de l'inflation, au lieu de +0,5 % | SMIC 2006-2026 : environ +0,4 % réel par an [V2C-05] |
| Moteur défaillant | Dividendes nuls dès l'année 3 ; rendement de la dotation réduit d'un point (2 % réel) | Défaillance de l'entreprise extérieure ou du fondateur |
| Cumul | Activités −30 %, crise, sinistre de 600 k€ et salaires +1,5 % | — |
| Sans moteur | Ni dotation ni dividendes | Démonstration de l'écart |

### 2.3 Simulation de Monte-Carlo sur 30 ans

Les résultats reposent sur 20 000 trajectoires, ou 10 000 pour les analyses de sensibilité. Chaque année et pour chaque trajectoire, le programme tire au sort les éléments suivants (`monte_carlo.py`, en-tête) :
- **Crise** : probabilité de 1 sur 12. HYPOTHÈSE : deux crises majeures, 2008 et 2020, en environ 25 ans. Ses impacts sont ceux du stress test « crise ».
- **Rendement de la dotation** : loi normale d'écart-type 10 points, calée pour que le rendement réel annualisé de long terme, crises comprises, soit de 3 % (HYPOTHÈSE).
- **Bruit sur chaque classe d'activités** : écart-type de 5 % pour les revenus contractuels, 10 % pour les récurrents et 35 % pour les occasionnels.
- **Sinistres non assurés** : en moyenne un tous les 10 ans, d'un montant médian égal à une année de provision de gros entretien.
- **Campagnes de travaux** : dépassement d'écart-type 20 %.
- **Prix de l'énergie** : choc annuel d'écart-type 20 %.
- **Dérive réelle des salaires** : tirée une fois par trajectoire, autour de +0,5 % (écart-type 0,4 point).
- **Entreprises qui versent les dividendes** : défaillance de 3,5 % par an et par entreprise, dans une holding de 5 PME. Ce taux correspond à environ une entreprise sur cinq en six ans [R8-36] (ESTIMATION).

**Erreur d'échantillonnage** : environ ± 0,3 à 0,6 point sur une probabilité de 5 à 10 %.

---

## 3. Résultats des stress tests (20 ans)

### 3.1 Domaine S2

| Projection | Dotation au plus bas (année) | Dotation en année 10 | Dotation en année 20 | Retrait annuel maximal | Années en déficit |
|---|---:|---:|---:|---:|---:|
| Sans moteur extérieur | — | — | — | — | **20** (réserve à −22,5 M€ en année 20) |
| Solution, cas central | 60,5 M€ (an 1) | 76,6 M€ | 88,1 M€ | 1,33 M€ | 0 |
| Activités −30 % | 60,5 M€ (an 1) | 76,4 M€ | 87,7 M€ | 1,34 M€ | 0 |
| Crise de type 2020 en année 5 | 50,3 M€ (an 5) | 57,0 M€ | 61,8 M€ | 1,33 M€ | 0 |
| Sinistre de 600 k€ et campagnes +30 % | 60,5 M€ (an 1) | 75,9 M€ | 85,8 M€ | 1,76 M€ | 0 |
| Énergie ×2 pendant 3 ans | 60,5 M€ (an 1) | 76,4 M€ | 87,8 M€ | 1,33 M€ | 0 |
| Salaires +1,5 % réel par an | 60,5 M€ (an 1) | 76,3 M€ | 86,9 M€ | 1,43 M€ | 0 |
| Moteur extérieur défaillant | 59,9 M€ (an 20) | 60,7 M€ | 59,9 M€ | 1,33 M€ | 0 |
| **Cumul défavorable** | **50,2 M€ (an 5)** | **56,7 M€** | **60,3 M€** | **1,44 M€** | **0** |

Lecture :

1. **La réserve de trésorerie ne baisse jamais : le choc se lit dans le capital.** La réserve reste à 1,5 M€ parce que la dotation la reconstitue chaque année.
2. **La crise est le choc le plus coûteux.**
   - L'année de la crise, la dotation perd 15 M€ (de 65,4 à 50,3 M€), car son rendement tombe à −22 %.
   - Les dividendes sont divisés par deux et le retrait monte à 0,73 M€.
   - Grâce au lissage, le plafond de retrait ne baisse que progressivement : de 1,71 M€ à 1,55 M€ en année 10.
   - Après la fin des dividendes (année 11), les retraits (1,26 à 1,33 M€) restent environ 20 % sous le plafond.
   - En année 20, la dotation vaut 26 M€ de moins que dans le cas central, soit −30 %.
3. **La défaillance du moteur extérieur ne fait pas échouer le domaine, mais elle supprime la marge.**
   - Sans dividendes dès l'année 3 et avec un rendement de 2 %, la dotation stagne autour de 60 M€, alors que les charges augmentent de 10 % en 20 ans.
   - Le rapport entre les ressources disponibles (plafond de retrait et activités) et les charges passe de 1,34 à 1,24.
4. **Le cumul ramène la dotation à son niveau de départ (60,3 M€) après 20 ans.**
   - Le domaine a été financé pendant 20 ans, mais sans marge : ses charges ont crû de 18 % (de 1,25 à 1,48 M€).
   - En année 20, les ressources disponibles (plafond de retrait et activités) ne dépassent plus les charges que de 12 %. Une nouvelle crise dans la décennie suivante mettrait le domaine en tension.
5. **Le sinistre est absorbé par le fonds de travaux, puis par la dotation.**
   - Le sinistre de 600 k€ vide presque le fonds en année 6 (il n'y reste que 48 k€). La campagne suivante est réduite d'autant.
   - Les campagnes majorées de 30 % dépassent le fonds de 0,21 à 0,43 M€ chacune. Les dividendes, puis la dotation, paient ces dépassements. Après l'année 10, le retrait atteint 1,67 à 1,76 M€ les années de campagne, sous un plafond de 1,96 à 2,21 M€.
6. **Les activités, l'énergie et les salaires pèsent peu sur 20 ans.**
   - Leurs chocs coûtent entre 0,3 et 1,2 M€ de capital final, soit moins de 2 %.
   - L'énergie ne représente qu'environ 5 % du besoin de S2 (L1). Les activités ne pèsent que 47 k€ par an.

### 3.2 Domaines S1 et S3

| Projection | Dotation initiale | Dotation au plus bas | Dotation en année 10 | Dotation en année 20 | Années en déficit |
|---|---:|---:|---:|---:|---:|
| S1, cas central (dividendes de 0,4 M€ par an pendant 10 ans) | 15 M€ | 15,3 M€ (an 1) | 20,7 M€ | 23,9 M€ | 0 |
| S1, cumul défavorable | 15 M€ | 13,1 M€ (an 5) | 15,0 M€ | 16,1 M€ | 0 |
| S3, cas central (sans dividendes) | 210 M€ | 210,5 M€ (an 1) | 237,4 M€ | 274,6 M€ | 0 |

Pour S1, les dividendes de transition (0,4 M€) dépassent le besoin (environ 0,32 M€) pendant les 10 premières années. L'excédent, d'environ 80 k€ par an, renforce la dotation.

L'année du sinistre de 600 k€ (année 6 du cumul), le besoin net atteint 0,74 M€, soit 1,8 fois le plafond de retrait (0,42 M€). Ce sont les dividendes qui comblent la différence. Pour un petit domaine, un gros sinistre non assuré représente donc un choc proportionnellement beaucoup plus fort.

---

## 4. Résultats de la simulation (30 ans)

### 4.1 Probabilité d'échec des trois solutions

| Indicateur (20 000 trajectoires) | S1 | S2 | S3 |
|---|---:|---:|---:|
| Dotation initiale | 15 M€ | 60 M€ | 210 M€ |
| Dividendes de transition | 0,4 M€ par an pendant 10 ans | 1 M€ par an pendant 10 ans | aucun |
| Dotation rapportée au besoin annuel | 46 fois | 48 fois | 58 fois |
| **Échec avant 20 ans** | **4,2 %** | **4,5 %** | **5,7 %** |
| **Échec avant 30 ans** | **10,9 %** | **11,2 %** | **11,9 %** |
| Année médiane du premier échec, quand il y en a un | 22 | 22 | 21 |
| Trajectoires avec au moins une année de tension sur 20 ans | 25 % | 25 % | 34 % |
| Nombre moyen d'années de tension sur 20 ans | 1,7 | 1,7 | 3,2 |
| Dotation en année 20 : 5 % des cas les plus bas / médiane / 5 % les plus hauts | 6,9 / 22,5 / 58,4 M€ | 25 / 84 / 221 M€ | 78 / 272 / 724 M€ |
| Part des trajectoires où la dotation de l'année 20 est inférieure à la dotation initiale | 27 % | 31 % | 35 % |
| … ou inférieure à la moitié de la dotation initiale | 6 % | 8 % | 10 % |

Source : `sorties/mc_distribution_solutions.json`. Une « année de tension » est une année où la réserve est passée sous un an de besoin, ce qui déclenche les règles de pilotage.

Lecture :
- **Les échecs se concentrent après la vingtième année.** Les dividendes de transition s'arrêtent en année 10, et les dérives de coûts s'accumulent. Le risque à 30 ans est 2 à 2,6 fois celui à 20 ans. Un horizon de 20 ans ne suffit donc pas pour juger un montage patrimonial destiné à durer une vie entière.
- **La médiane cache une forte dispersion.** Dans la moitié des cas, la dotation de S2 dépasse 84 M€ en année 20. Dans 5 % des cas, elle tombe sous 25 M€. C'est le propre d'un capital investi en actifs risqués : la règle de dépense lissée protège le domaine, pas le niveau du capital.
- **Les années de tension sont rares mais attendues.** Un quart des trajectoires connaissent au moins une année où il faut appliquer les règles d'économie. Le propriétaire doit savoir à l'avance que cela arrivera probablement une ou deux fois en 20 ans.

### 4.2 Ce qui fait rompre le modèle

| Facteur testé (10 000 trajectoires par ligne) | S1 : échec 20 / 30 ans | S2 : échec 20 / 30 ans | S3 : échec 20 / 30 ans |
|---|---:|---:|---:|
| **Référence** | **4,2 / 10,7 %** | **4,3 / 11,1 %** | **5,3 / 11,7 %** |
| Besoin au bas de la fourchette de L1 (0,20 / 0,78 / 2,17 M€) | 0,3 / 1,4 % | 0,4 / 1,7 % | 0,7 / 1,8 % |
| Besoin au haut de la fourchette de L1 (0,56 / 2,06 / 6,41 M€) | 33,5 / 48,3 % | 30,5 / 44,6 % | 30,1 / 43,2 % |
| Besoin +20 % | 9,4 / 19,0 % | 9,8 / 19,7 % | 10,6 / 19,5 % |
| Dotation initiale réduite d'un tiers | 15,0 / 27,7 % (10 M€) | 17,3 / 29,9 % (40 M€) | 20,6 / 32,2 % (141 M€) |
| Dotation initiale augmentée d'un tiers | 1,4 / 4,7 % (20 M€) | 1,3 / 4,5 % (80 M€) | 1,8 / 4,8 % (279 M€) |
| Rendement réel net de 2 % | 6,8 / 18,3 % | 7,3 / 18,9 % | 8,4 / 19,3 % |
| Rendement réel net de 3,5 % | 3,2 / 8,1 % | 3,3 / 8,3 % | 4,4 / 8,9 % |
| Aucune règle de pilotage | 10,8 / 21,0 % | 11,1 / 21,5 % | 12,2 / 22,3 % |
| Pas de dividendes de transition | 10,3 / 19,6 % | 8,0 / 16,6 % | sans objet |
| Salaires +1,5 % réel par an | 4,8 / 12,8 % | 5,6 / 14,4 % | 6,5 / 14,5 % |
| Une crise tous les 8 ans | 5,4 / 13,0 % | 5,6 / 13,0 % | 6,6 / 13,7 % |
| Une crise tous les 20 ans | 3,3 / 8,7 % | 3,3 / 8,9 % | 4,6 / 9,8 % |
| Deux fois plus de sinistres non assurés | 5,1 / 11,8 % | 5,1 / 11,6 % | 7,9 / 14,1 % |
| Une seule entreprise au lieu de cinq | 4,5 / 10,8 % | 4,5 / 10,9 % | sans objet |

Sources : `sorties/mc_ruptures_S1.json`, `mc_ruptures_S2.json` et `mc_ruptures_S3.json`. Quand le besoin change, la réserve de trésorerie est ajustée dans la même proportion. Pour S3, la référence de cette table (5,3 / 11,7 %) diffère légèrement de celle du § 4.1 (5,7 / 11,9 %) : ce n'est que du bruit d'échantillonnage, les calculs étant faits sur 10 000 et 20 000 trajectoires.

Classement des risques, du plus au moins grave :
1. **Une erreur de budget.** Le haut de la fourchette de L1 multiplie le risque par 4 à 8. Pour tenir 30 ans à 95 % avec un besoin au niveau défavorable, il faudrait, avec une dotation seule :
   - environ 40 M€ en S1 ;
   - environ 143 M€ en S2 ;
   - environ 480 M€ en S3.
   C'est toujours environ 70 fois le besoin annuel.
2. **Un capital insuffisant.** Un tiers de moins multiplie le risque à 20 ans par 3 à 4.
3. **L'absence de discipline.** Sans règles de pilotage, le risque double.
4. **Le rendement.** Un point de rendement réel en moins augmente le risque à 30 ans de 7 à 8 points. Une hausse de la fiscalité du capital agirait de la même façon (§ 5).
5. **La fin prématurée des dividendes.** Pour S2, le risque passe de 11 à 17 % à 30 ans. Le nombre d'entreprises dans la holding compte peu, parce que les dividendes ne pèsent que pendant les 10 premières années.
6. **La fréquence des crises, les sinistres et les salaires.** Chacun ajoute de 0,5 à 3,5 points à 30 ans.

### 4.3 Combien de capital pour quel niveau de sécurité ?

Le tableau suivant porte sur une dotation seule, sans dividendes, avec les règles de pilotage, sur 30 ans (`sorties/mc_dotation_necessaire.json`).

| Domaine | Besoin annuel | Dotation pour 1 chance sur 2 de tenir 30 ans | Dotation pour 95 % de chances | Avec les leviers : 50 % / 95 % |
|---|---:|---:|---:|---:|
| S1 | 0,33 M€ | 9,6 M€ (29 fois le besoin) | 22,9 M€ (70 fois) | 7,2 / 17,1 M€ (22 / 53 fois) |
| S2 | 1,24 M€ | 36,5 M€ (29 fois) | 85,5 M€ (69 fois) | 27,3 / 64,0 M€ (22 / 52 fois) |
| S3 | 3,64 M€ | 108,7 M€ (30 fois) | 271,3 M€ (74 fois) | 82,0 / 204,0 M€ (22 / 56 fois) |

« Avec les leviers » signifie deux choses à la fois :
- le besoin est réduit de 15 % par le « prestige efficace » (L2, § 5) ;
- l'avantage fiscal lié au régime des monuments historiques est activé (L2, § 4).

C'est une **borne optimiste**. Les leviers vérifiés par V2C représentent environ 5 à 8 % du besoin de S2, et l'avantage fiscal suppose de gros revenus imposables au barème (L2, § 4 et § 5).

Règle simple à retenir :
- **environ 30 fois le besoin annuel** pour une chance sur deux de tenir 30 ans ;
- **environ 70 fois** pour 95 % de chances ;
- **22 fois et 50 à 55 fois** avec les leviers.

Comment lire ces multiples :
- **Le seuil d'une chance sur deux n'est pas un objectif.** À 29-30 fois le besoin, le plafond normal de retrait (2,75 % du capital, soit environ 0,8 fois le besoin) ne couvre pas le besoin. Le domaine vit alors la plupart du temps en mode de tension, sur des retraits d'urgence.
- **Pour 95 % de chances, il faut environ deux fois l'inverse du taux de retrait** (1 ÷ 2,75 % = 36 fois). La dotation doit en effet absorber à la fois la dérive des coûts, les crises et la dispersion des rendements.

### 4.4 Les autres modèles résistent-ils ?

- **Holding de PME qui ne fait que distribuer ses dividendes**, avec une petite dotation de 2 à 10 M€ (`sorties/mc_holding_hybride.json`) :
  - de 45 à 77 % d'échec avant 20 ans ;
  - de 67 à 91 % avant 30 ans.
  - Les défaillances d'entreprises, la volatilité des dividendes et l'absence de capital tampon rendent ce montage fragile. La holding peut **constituer** le capital, mais elle ne peut pas le **remplacer** (L2, § 6.2).
- **Modèles fondés sur les activités sur place** (M1 à M3, M7, M8) : ils couvrent dans le cas central entre 3 et 21 % du besoin de S2. Une crise de type 2020 supprime l'essentiel des revenus occasionnels (−80 %). Le locataire d'ancrage (M7) apporte des revenus contractuels, mais deux exemples montrent que ces loyers aussi peuvent s'arrêter :
  - au premier semestre 2020, les loyers variables de Covivio ont baissé de 67 % [V2A-31] ;
  - des gestionnaires de résidences Pierre et Vacances ont suspendu leurs loyers à partir de 2020, et près de 20 000 bailleurs étaient sans paiement depuis janvier 2021 [V2A-62] [V2A-63].
- **Château-hôtel (M4)** : sa contribution est négative dans le cas central (−29 % du besoin) et dans le cas défavorable (−57 %). Il ajoute un risque au lieu d'en retirer. Dans l'échantillon de la vague 1, 20 sociétés de châteaux-hôtels sur 33 étaient en perte [R4-34]. La vérification indépendante retrouve ce résultat. Sur les seuls comptes 2023-2025 (26 sociétés), la part en perte est de 54 % et la marge nette médiane de −4,5 % [V2V].

---

## 5. Tenir 20 à 30 ans : ce que les chiffres ne montrent pas

1. **La dérive des coûts est lente mais certaine.**
   - Dans le cas central, les charges de S2 augmentent de 10,5 % en euros constants en 20 ans (de 1,25 à 1,38 M€). Avec des salaires à +1,5 % par an, la hausse atteint 18 %.
   - Les métiers des monuments historiques (taille de pierre, couverture, menuiserie à l'identique) n'ont pas d'indice public : leur dérive propre est INCONNUE [V2C-03].
   - La règle de dépense, elle, ne croît que si le capital croît.
2. **Le rendement réel net de 3 % est l'hypothèse la plus sensible après le budget.**
   - Il suppose un portefeuille diversifié, majoritairement en actions, géré à faible coût, et la fiscalité française actuelle (PFU de 31,4 % [R8-31]).
   - Une hausse de la fiscalité du capital, des frais de gestion élevés ou une allocation trop prudente le ramèneraient vers 2 %. Le risque à 30 ans passerait alors d'environ 11 % à environ 19 %.
   - Le véhicule juridique et fiscal de la dotation est discuté dans L2 (§ 6) et doit être validé par un avocat fiscaliste avant tout engagement.
3. **La simulation représente l'inflation par les crises et la dispersion des rendements.**
   - Le modèle raisonne en euros constants.
   - Une longue période d'inflation forte avec des rendements réels négatifs n'est pas simulée séparément. Elle ressemblerait à une suite de mauvaises années, et c'est précisément le cas où la dotation sort au bas de la distribution.
4. **Le modèle suppose qu'un sinistre consomme le fonds de travaux.** La campagne suivante est réduite d'autant, ce qui revient à reporter des travaux. L'effet d'un retard d'entretien n'est pas chiffré.
5. **Un sinistre total (incendie) n'est pas modélisé.** Il est supposé couvert par l'assurance (3 ‰ de la valeur de reconstruction, L1). Un défaut d'assurabilité ou une sous-assurance changerait tout. Exemples :
   - la résiliation de l'assurance du château d'Olhain [R1-28] ;
   - le relèvement de la surprime « catastrophes naturelles » de 12 à 20 % en 2025 [R1-29].
6. **Les risques juridiques et politiques ne sont pas simulés.** Changement du régime des monuments historiques, de l'IFI ou de la taxation des holdings (taxe de 20 % sur les holdings patrimoniales de la loi de finances 2026 [R3-18], texte officiel non lu, à faire valider par un fiscaliste [V2V-47]) : leur effet passe par le besoin ou par le rendement, qui sont tous deux testés ci-dessus.

---

## 6. Dépendance au fondateur

Le propriétaire a 26 ans. Un horizon de 30 ans le mène à 56 ans et traverse les événements d'une vie : mariage, enfants, séparation, maladie, succession. Le modèle mesure deux canaux de dépendance.

1. **L'entreprise extérieure.** Les dividendes de transition dépendent de l'activité d'entreprises, et souvent de la personne qui les dirige. Si les dividendes s'arrêtent dès l'année 3, le domaine ne fait pas faillite, mais il perd toute marge (§ 3.1). Sans aucun dividende, le risque à 30 ans passe de 11 à 17 % pour S2. **Conclusion** : la pérennité ne doit pas reposer sur un flux qui exige le travail du fondateur. Elle doit reposer sur un capital qui produit un revenu sans lui. La transition doit servir à **convertir** les revenus d'entreprise en capital.
2. **La discipline de dépense.** C'est le canal le plus important : sans règles de pilotage, le risque double (11 % au lieu de 4 % à 20 ans pour S2). Or ces règles exigent de dire non, une année difficile, à une dépense de prestige. Un propriétaire seul qui décide de tout est exposé à la tentation inverse. **Conclusion** : la règle de dépense, le seuil de réserve et les mesures de tension doivent être écrits dans les statuts ou dans une charte. Leur application doit être contrôlée par au moins une personne indépendante (comité d'investissement, administrateur extérieur). Le montage exact relève d'un notaire et d'un avocat (L7).

Les activités qui reposent sur la présence ou le talent personnel du propriétaire ont été écartées du socle de la solution :
- la pension haut de gamme ;
- la reproduction, qui exige un vétérinaire et un étalon (L2, § 3.1).

---

## 7. Tranquillité : ce que les crises font au calme du domaine

- **Le socle de la solution est calme.** Il comprend :
  - des revenus contractuels (logements dans les communs, hivernage de véhicules, bail solaire, forêt) ;
  - une pension standard et une pension de retraite au pré ;
  - deux journées de tournage par an.
  - Il ne comprend ni réception ni public.
- **En crise, la variable d'ajustement est la dépense, pas l'ouverture du domaine.** Les règles de pilotage coupent les dépenses discrétionnaires et reportent des travaux. Elles n'ajoutent aucune activité.
- **Ouvrir le domaine en cas de difficulté rapporterait peu.** Ajouter des réceptions, des séminaires et la location d'une grande maison (modèle M2 par rapport à M1) n'apporte qu'environ 38 k€ par an dans le cas central, soit 3 points de couverture du besoin de S2. Cela demande 1 M€ d'investissement de plus et apporte des nuisances. Ces revenus occasionnels sont aussi les premiers à disparaître en crise (−80 %).
- **La seule activité qui change l'ordre de grandeur, le locataire d'ancrage (M7), est incompatible avec une partie entièrement privée en S2.** Elle apporterait environ 0,26 M€ disponibles par an dans le cas central, mais suppose de confier 40 à 60 chambres à un exploitant de séminaires pendant 15 à 30 ans, avec une cohabitation quotidienne. Aucun cas documenté d'un propriétaire vivant au château à côté d'un tel exploitant n'a été trouvé [V2A § 3]. Elle n'est envisageable que si la localisation et la taille le permettent, ce qui est plus plausible en S3.

---

## 8. Règles de pilotage recommandées

Les règles marquées « simulée » sont incluses dans le modèle et dans la simulation de Monte-Carlo. Les autres sont des recommandations de bon sens qui n'ont **pas** été simulées.

| Indicateur | Seuil | Action | Statut |
|---|---|---|---|
| Réserve de trésorerie | Moins d'un an de besoin | Couper 10 % du besoin en dépenses discrétionnaires ; reporter 30 % de la campagne de travaux ; retrait d'urgence plafonné à 4 % du capital | simulée |
| Retrait annuel sur la dotation | Plafond lissé : 80 % du plafond précédent + 20 % × 2,75 % × dotation | Ne jamais dépasser le plafond en dehors des années de tension | simulée |
| Fonds de travaux | Provision annuelle versée chaque année, même en tension | Le report d'une campagne reste dû et revient au fonds | simulée |
| Dotation réelle | Moins de 80 % de la dotation initiale, en euros constants | Revoir le budget, suspendre les investissements futurs et les achats de prestige | non simulée |
| Rendement réel moyen sur 5 ans | Moins de 2 % par an | Revoir l'allocation et les frais ; ramener le taux de retrait vers 2,5 % | non simulée |
| Besoin réel mesuré | Plus de 10 % au-dessus du budget pendant 2 ans | Recalculer la dotation nécessaire ; activer les leviers du « prestige efficace » (L2, § 5) | non simulée |
| Dividendes de transition | Moins de 50 % du prévu pendant 2 ans | Ne pas compenser par des activités bruyantes ; allonger la constitution du capital | non simulée |

---

## 9. Limites et prochaines vérifications

- **Calibrage du Monte-Carlo.** La fréquence des crises (1 sur 12), leur ampleur (−25 points de rendement), l'écart-type des rendements (10 points), les sinistres et la défaillance des entreprises sont des HYPOTHÈSES. Les probabilités ci-dessus sont donc **relatives** : elles servent à comparer des montages et à classer des risques, pas à promettre un niveau de sécurité.
- **Corrélations.** Les chocs sont indépendants entre eux, sauf à travers la variable de crise, qui frappe ensemble les activités, la dotation et les dividendes. En réalité, une hausse des taux ou de l'inflation pourrait frapper en même temps les rendements, les coûts de travaux et l'énergie.
- **Le budget reste l'incertitude principale.** La fourchette de L1 (0,78 à 2,06 M€ pour S2) est plus large que tous les chocs testés. Le rapport public IGF-IGAC de 2020 et les cas réels ne permettent ni de valider ni d'infirmer le budget de S2 [V2C-07]. C'est la priorité de la phase 1 de la feuille de route (L7).
- **Contrôle externe.** La vérification indépendante de 90 chiffres clés (`01_RECHERCHE/V2V_verification.md`) n'a trouvé aucun chiffre faux. Elle a nuancé 9 chiffres (périmètres, unités, statuts), sans changer de valeur du modèle. L'équipe rouge (`01_RECHERCHE/V2R_equipe_rouge.md`) attaque le modèle et les livrables ; ses corrections seront reportées dans le modèle et dans ce document.
