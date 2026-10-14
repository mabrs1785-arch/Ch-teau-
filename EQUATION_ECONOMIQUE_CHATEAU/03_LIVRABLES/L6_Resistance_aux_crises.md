# L6 — Le modèle résiste-t-il aux crises ? Stress tests sur 20 ans et simulation sur 30 ans

> **Statut de ce document**
> - Résultats calculés, en euros constants 2026. Ce sont des **simulations conditionnelles** : elles décrivent ce qui arrive **si** les hypothèses sont justes. Ce ne sont pas des prévisions.
> - Version révisée après l'équipe rouge (V2R) :
>   - rendement réel net du capital ramené de 3 % à 2 %, et taux de retrait de 2,75 % à 1,75 % ;
>   - sinistres non assurés payés en plus du fonds de travaux ;
>   - réserve reconstituée après usage ;
>   - deux tests ajoutés : décennie perdue et décès du propriétaire ;
>   - solutions redimensionnées pour respecter le critère n° 6 du cadre analytique.
> - Projections déterministes : `02_MODELE/sorties/Modele_equation_chateau.xlsx`, feuilles `Proj_*`, `ST_*` et `Stress_synthese`. Le classeur compte 11 814 formules recalculées, sans erreur ni écart avec le calcul Python indépendant (`sorties/verification.json`).
> - Simulation de Monte-Carlo : `02_MODELE/monte_carlo.py` et `02_MODELE/calculer_mc.py`, avec les résultats dans `02_MODELE/sorties/mc_*.json`. Sans chocs aléatoires, la simulation reproduit les projections du classeur à moins d'un millionième d'euro près (contrôle automatique `verifier_jumeau`).
> - Les identifiants entre crochets renvoient au registre des sources. Statuts : SOURCÉ, ESTIMATION (raisonnement sur sources), HYPOTHÈSE (choix de modélisation à valider).

---

## 1. La réponse en une page

### Sans moteur extérieur, il n'y a rien à stresser

Le domaine S2 est en déficit dès la première année.
- Les activités sur place apportent en moyenne 41 k€ par an.
- Le besoin passe de 1,28 à 1,42 M€ en 20 ans.
- La réserve de 1,5 M€ ne couvre pas la première année, puisqu'il faut aussi financer 1,1 M€ d'investissement initial des activités.
- Le déficit cumulé atteint 22,3 M€ en année 20 (feuille `Proj_S2_sans_moteur`).

### La solution recommandée passe les sept stress tests sur 20 ans

Le montage S2 réunit :
- un capital affecté de 120 M€ ;
- des dividendes de transition de 1 M€ par an pendant 10 ans ;
- une réserve de trésorerie de 1,5 M€ ;
- des règles de pilotage écrites.

Aucune année n'est en déficit, ni même en tension, y compris quand les chocs sont cumulés : activités −30 %, crise de type 2020, sinistre de 600 k€ et salaires +1,5 % par an au-delà de l'inflation.

C'est le **capital** qui encaisse les chocs, pas la trésorerie. Dans le pire cas testé, il finit l'année 20 à 112 M€, contre 158 M€ dans le cas central.

### Sur 30 ans, avec des chocs tirés au hasard, le risque d'échec est d'environ 5 %

Sur 20 000 trajectoires simulées pour S2 :
- **1,8 %** échouent avant 20 ans ;
- **4,8 %** échouent avant 30 ans (5,0 % sur un autre tirage de 10 000 trajectoires).

Le critère n° 6 du cadre analytique (au plus 5 % d'échec sur 20 et sur 30 ans) est donc respecté, mais **au plus juste**. Les trois solutions (34, 120 et 480 M€) ont été dimensionnées pour cela : ce sont les plus petites valeurs rondes qui le respectent (`sorties/mc_dimensionnement.json`).

Un « échec » signifie qu'une année donnée, la réserve de trésorerie devient négative. Ni le capital (dans la limite de sa règle et du retrait d'urgence), ni les dividendes, ni la réserve ne suffisent. Il faut alors remettre de l'argent extérieur ou réduire durablement le niveau d'entretien.

### Ce qui fait vraiment rompre le modèle : le budget, le capital, la succession et la discipline

| Facteur (domaine S2, 10 000 trajectoires par ligne) | Échec avant 20 ans | Échec avant 30 ans |
|---|---:|---:|
| **Solution de référence** | **1,8 %** | **5,0 %** |
| Capital de 60 M€ au lieu de 120 M€ | 14,4 % | 28,3 % |
| Besoin réel au haut de la fourchette de L1 (2,16 M€ au lieu de 1,27 M€) | 11,2 % | 22,4 % |
| Décès du propriétaire en année 15, sans montage successoral (droits de 44 %) | 4,5 % | 15,9 % |
| Aucune règle de pilotage | 6,8 % | 16,0 % |
| Capital de 80 M€ au lieu de 120 M€ | 6,3 % | 14,6 % |
| Besoin réel supérieur de 20 % | 3,3 % | 8,8 % |
| Décennie perdue : rendement réel moyen nul pendant les 10 premières années | 3,0 % | 8,6 % |
| Sinistres non assurés deux fois plus fréquents | 3,0 % | 7,0 % |
| Pas de dividendes de transition | 2,9 % | 6,7 % |
| Rendement réel net de 1,5 % au lieu de 2 % | 2,2 % | 6,6 % |
| Une crise tous les 8 ans au lieu de tous les 12 ans | 2,3 % | 5,9 % |
| Salaires +1,5 % réel par an au lieu de +0,5 % | 2,0 % | 5,8 % |
| Énergie ×2 pendant 3 ans, ou activités −30 % (tests déterministes) | aucun déficit | — |

Sources : `sorties/mc_ruptures_S2.json` et feuilles `ST_*`.

### Quatre conclusions

1. **La première protection est un budget juste.**
   - Si le besoin réel se situe au haut de la fourchette de L1, le risque d'échec à 30 ans est multiplié par environ 4,5.
   - Pour retrouver 95 % de chances de tenir 30 ans avec un capital seul, il faudrait alors 225 M€, contre 132 M€ avec le budget central.
   - Le capital ne doit donc pas être dimensionné avant que le budget ait été validé par des devis et par un an d'exploitation réelle (L7, phase 1).
2. **La deuxième protection est une transmission organisée.** Sans montage successoral, un décès en année 15 triple le risque à 30 ans (§ 6).
3. **La troisième est la discipline de dépense.** Sans règles de pilotage écrites et respectées, le risque à 30 ans triple aussi (§ 6).
4. **Les activités sur place ne protègent de rien.** Leur effondrement ne change presque rien, parce qu'elles pèsent peu. Le château-hôtel aggraverait au contraire le risque, puisqu'il perd de l'argent même en année normale (L2, § 3.6).

---

## 2. Méthode

### 2.1 Projection déterministe sur 20 ans (Excel)

- **Besoin annuel** : celui de L1, en euros constants 2026 (1,27 M€ pour S2 dans le cas central).
- **Dérives réelles annuelles** (au-delà de l'inflation), calées sur les séries de l'INSEE de 2005 à 2025. Ce sont des ESTIMATIONS :
  - salaires : +0,5 % [V2C-05] [D-01] ;
  - travaux : +0,75 % [V2C-03] ;
  - énergie : +2 % [V2C-04] ;
  - assurances : +1,85 % [V2C-19].
- **Gros entretien** : provisionné chaque année dans un fonds de travaux et dépensé par campagnes tous les 4 ans (HYPOTHÈSE). Un sinistre non assuré est payé **en plus** du fonds, sans annuler de travaux (correction V2R M1).
- **Activités sur place** : socle calme de la solution (L3, § 4). Montée en charge : 40 % de leur régime l'année 1, 75 % l'année 2. La contribution perd 40 % en impôts (ESTIMATION, de 25 à 54 % selon la structure, L2 § 1). L'investissement initial des activités (1,1 M€) est prélevé sur le capital l'année 1.
- **Capital affecté** : rendement réel net de 2 % par an (ESTIMATION, fourchette de 1,5 à 2,5 %) [R8-32] [V2R-03] [V2R-04] [V2R-05] [V2R-08] [V2R-16]. Le retrait est plafonné par une règle de dépense lissée (HYPOTHÈSE inspirée des fonds de dotation [R8-34]) :
  - plafond de l'année = 80 % × plafond de l'année précédente + 20 % × 1,75 % × capital de l'année précédente.
- **Réserve de trésorerie** : 1,5 M€ au départ pour S2, soit environ 1,2 an de besoin. Sa cible est indexée sur les charges. Elle est reconstituée par le retrait, dans la limite du plafond (correction V2R M2). La trésorerie rapporte −0,5 % réel par an [V2R-08]. Les excédents sont versés au capital.

**Échec** : la réserve de trésorerie devient négative. C'est la définition du critère n° 6 du cadre analytique.

**Tension** : la réserve est passée sous un an de charges de l'année précédente. Les règles de pilotage incluses dans le modèle (HYPOTHÈSES) s'appliquent alors :
- couper 10 % du besoin en dépenses discrétionnaires : investissements futurs, imprévus, achats reportables ;
- reporter 30 % de la campagne de travaux en cours (le report reste dû et retourne au fonds de travaux) ;
- autoriser un retrait d'urgence plafonné à 4 % du capital.

### 2.2 Les sept stress tests et la projection sans moteur

| Test | Choc appliqué | Calibrage |
|---|---|---|
| Activités −30 % | Contribution des activités −30 % dès l'année 3 | Demandé par le brief |
| Crise de type 2020 | Année 5 : activités occasionnelles −80 %, récurrentes −15 %, contractuelles −5 % ; rendement du capital −25 points (soit −23 % l'année de la crise) ; dividendes −50 %. Reprise partielle en année 6 | CA de Châteauform' −69 % en 2020 [R7-26] ; loyers variables de Covivio −67 % au premier semestre 2020 [V2A-31] ; mariages en chute en 2020 [R7-16]. Les chocs de −15 %, −5 %, −25 points et −50 % sont des HYPOTHÈSES |
| Travaux | Sinistre ou découverte non assurés de 600 k€ en année 6 ; campagnes de gros entretien +30 % | HYPOTHÈSE ; chantiers réels de 370 000 à 450 000 € pour une seule tour [V2C-07] |
| Énergie | Prix de l'énergie ×2 des années 4 à 6 | Plus dur que les chocs observés en 2021-2024, de +40 à +66 % [V2C-04] |
| Salaires | +1,5 % par an au-delà de l'inflation, au lieu de +0,5 % | SMIC 2006-2026 : environ +0,4 % réel par an [V2C-05] |
| Moteur défaillant | Dividendes nuls dès l'année 3 ; rendement du capital réduit d'un point (1 % réel) | Défaillance des entreprises ou du fondateur |
| Cumul | Activités −30 %, crise, sinistre de 600 k€ et salaires +1,5 % | — |
| Sans moteur (démonstration) | Ni capital ni dividendes | Mesure de l'écart à combler |

### 2.3 Simulation de Monte-Carlo sur 30 ans

Les résultats reposent sur 20 000 trajectoires, ou 10 000 pour les analyses de sensibilité. Chaque année et pour chaque trajectoire, le programme tire au sort les éléments suivants (`monte_carlo.py`) :
- **Crise** : probabilité de 1 sur 12. HYPOTHÈSE : deux crises majeures, 2008 et 2020, en environ 25 ans. Ses impacts sont ceux du stress test « crise ».
- **Rendement du capital** : loi normale d'écart-type 10 points. Elle est calée pour que le rendement réel annualisé de long terme, crises comprises, soit de 2 % (HYPOTHÈSE).
- **Bruit sur chaque classe d'activités** : écart-type de 5 % pour les revenus contractuels, 10 % pour les récurrents et 35 % pour les occasionnels.
- **Sinistres non assurés** : en moyenne un tous les 10 ans, d'un montant médian égal à une année de provision de gros entretien. Ils sont payés en plus du fonds de travaux.
- **Campagnes de travaux** : dépassement d'écart-type 20 %.
- **Prix de l'énergie** : choc annuel d'écart-type 20 %.
- **Dérive réelle des salaires** : tirée une fois par trajectoire, autour de +0,5 % (écart-type 0,4 point).
- **Entreprises qui versent les dividendes** : holding de 5 PME. Chaque entreprise a 3,5 % de risque de défaillance par an, soit environ une sur cinq en six ans [R8-36] (ESTIMATION). Les dividendes sont divisés par deux l'année d'une crise.

Deux tests ajoutés à la demande de l'équipe rouge (V2R M5 et M9) :
- **Décennie perdue** : rendement réel moyen nul pendant les 10 premières années, avec la même volatilité.
- **Décès du propriétaire en année 15** : 44 % du capital part en droits de succession [V2R-06] (ESTIMATION, en l'absence de tout montage).

**Erreur d'échantillonnage** : environ ± 0,3 point sur une probabilité de 5 % avec 20 000 trajectoires, et ± 0,4 point avec 10 000. Les écarts de 0,1 à 0,2 point entre deux tableaux ne sont que du bruit.

---

## 3. Résultats des stress tests (20 ans)

### 3.1 Domaine S2

| Projection | Capital au plus bas (année) | Capital en année 10 | Capital en année 20 | Retrait annuel maximal | Part maximale du plafond utilisée | Années en déficit |
|---|---:|---:|---:|---:|---:|---:|
| Sans moteur extérieur | — | — | — | — | — | **20** (réserve à −22,3 M€ en année 20) |
| Solution, cas central | 121,0 M€ (an 1) | 141,8 M€ | 158,1 M€ | 1,39 M€ | 57 % | 0 |
| Activités −30 % | 121,0 M€ (an 1) | 141,7 M€ | 157,8 M€ | 1,40 M€ | 57 % | 0 |
| Crise de type 2020 en année 5 | 97,5 M€ (an 5) | 106,1 M€ | 114,5 M€ | 1,39 M€ | 72 % | 0 |
| Sinistre de 600 k€ et campagnes +30 % | 121,0 M€ (an 1) | 140,3 M€ | 154,7 M€ | 1,86 M€ | 75 % | 0 |
| Énergie ×2 pendant 3 ans | 121,0 M€ (an 1) | 141,6 M€ | 157,8 M€ | 1,39 M€ | 56 % | 0 |
| Salaires +1,5 % réel par an | 121,0 M€ (an 1) | 141,5 M€ | 156,9 M€ | 1,50 M€ | 59 % | 0 |
| Moteur extérieur défaillant | 118,5 M€ (an 20) | 120,1 M€ | 118,5 M€ | 1,39 M€ | 67 % | 0 |
| **Cumul défavorable** | **97,4 M€ (an 5)** | **105,0 M€** | **112,2 M€** | **1,51 M€** | **79 %** | **0** |

La « part maximale du plafond utilisée » est le plus fort rapport, sur les 20 ans, entre le retrait de l'année et le plafond de la règle de dépense. Aucune projection de la solution ne connaît d'année de tension.

Lecture :

1. **La réserve de trésorerie ne baisse jamais : le choc se lit dans le capital.** La réserve reste au moins à 1,5 M€, car le retrait la reconstitue chaque année. Elle monte à 1,66 M€ en année 20, ou 1,77 M€ quand les salaires dérivent, parce que sa cible suit les charges.
2. **La crise est le choc le plus coûteux.**
   - L'année de la crise, le capital perd 30 M€ (de 127,6 à 97,5 M€), car son rendement tombe à −23 %.
   - Les dividendes sont divisés par deux, et le retrait monte à 0,78 M€.
   - Grâce au lissage, le plafond de retrait ne baisse que progressivement : de 2,15 M€ en année 5 à 1,89 M€ en années 12 et 13.
   - Après la fin des dividendes (année 11), les retraits (1,32 à 1,39 M€) utilisent au plus 72 % du plafond.
   - En année 20, le capital vaut 43,6 M€ de moins que dans le cas central, soit −28 %.
3. **La défaillance des entreprises ne fait pas échouer le domaine, mais elle arrête la croissance du capital.**
   - Le domaine ne reçoit que 2 M€ de dividendes au lieu de 10, et le rendement tombe à 1 %. Le capital stagne alors autour de 120 M€ et finit à 118,5 M€, alors que les charges augmentent de 11 % en 20 ans.
   - Le rapport entre les ressources disponibles (plafond de retrait et activités) et les charges passe de 1,66 à 1,50.
   - Avec un rendement durablement inférieur au taux de retrait, le capital s'érode lentement : le problème serait reporté sur la génération suivante.
4. **Le cumul laisse le capital sous son niveau de départ (112,2 M€ en année 20).**
   - Le domaine a été financé pendant 20 ans, mais avec une marge réduite : ses charges ont crû de 18 % (de 1,28 à 1,51 M€).
   - En année 20, les ressources disponibles (plafond de retrait et activités) ne dépassent plus les charges que de 28 %, et le retrait utilise 79 % du plafond.
5. **Le sinistre et les dépassements de travaux sont payés par le capital.**
   - Le sinistre de 600 k€ est payé en plus du fonds de travaux : le retrait de l'année 6 passe de 0,29 à 0,89 M€.
   - Les campagnes majorées de 30 % dépassent le fonds de 0,42 à 0,47 M€ chacune. Après l'année 10, le retrait atteint 1,78 à 1,86 M€ les années de campagne, soit au plus 75 % du plafond.
   - Coût total en année 20 : 3,4 M€ de capital.
6. **Les activités, l'énergie et les salaires pèsent peu sur 20 ans.**
   - Leurs chocs coûtent entre 0,3 et 1,2 M€ de capital final, soit moins de 1 %.
   - L'énergie ne représente qu'environ 5 % du besoin de S2 (L1). Les activités ne rapportent que 41 k€ par an en moyenne.

### 3.2 Domaines S1 et S3

| Projection | Capital initial | Capital au plus bas | Capital en année 10 | Capital en année 20 | Part maximale du plafond utilisée | Années en déficit |
|---|---:|---:|---:|---:|---:|---:|
| S1, cas central (dividendes de 0,4 M€ par an pendant 10 ans) | 34 M€ | 34,5 M€ (an 1) | 41,7 M€ | 46,8 M€ | 53 % | 0 |
| S1, cumul défavorable | 34 M€ | 28,1 M€ (an 5) | 30,6 M€ | 33,1 M€ | 95 % (an 6) | 0 |
| S3, cas central (sans dividendes) | 480 M€ | 483,6 M€ (an 1) | 540,3 M€ | 614,1 M€ | 45 % | 0 |

Pour S1, les dividendes de transition (0,4 M€) dépassent le besoin (environ 0,35 M€) pendant les 10 premières années. Le capital n'est pas sollicité, et l'excédent, environ 0,5 M€ en 10 ans, lui est versé.

L'année du sinistre de 600 k€ (année 6 du cumul), le besoin net de S1 atteint 0,95 M€, soit près de trois fois le besoin normal. Le retrait (0,56 M€) utilise 95 % du plafond, et les dividendes paient le reste. **Pour un petit domaine, un gros sinistre non assuré est un choc proportionnellement beaucoup plus fort.** Sans les dividendes de transition, la réserve de 0,4 M€ aurait dû absorber environ 0,36 M€ (0,95 M€ de besoin moins 0,59 M€ de plafond) : elle serait tombée sous un an de charges, ce qui déclenche les règles de tension (calcul arithmétique, non simulé).

---

## 4. Résultats de la simulation (30 ans)

### 4.1 Probabilité d'échec des trois solutions

| Indicateur (20 000 trajectoires) | S1 | S2 | S3 |
|---|---:|---:|---:|
| Capital initial | 34 M€ | 120 M€ | 480 M€ |
| Dividendes de transition | 0,4 M€ par an pendant 10 ans | 1 M€ par an pendant 10 ans | aucun |
| Capital rapporté au besoin annuel | 98 fois | 94 fois | 127 fois |
| **Échec avant 20 ans** | **1,8 %** | **1,8 %** | **2,5 %** |
| **Échec avant 30 ans** | **4,6 %** | **4,8 %** | **5,0 %** |
| Année médiane du premier échec, quand il y en a un | 23 | 23 | 20 |
| Trajectoires avec au moins une année de tension sur 20 ans | 17 % | 20 % | 18 % |
| Nombre moyen d'années de tension sur 20 ans | 0,3 | 0,4 | 0,3 |
| Capital en année 20 : 5 % des cas les plus bas / médiane / 5 % les plus hauts | 14,7 / 45,2 / 113,9 M€ | 48,7 / 153,5 / 390,6 M€ | 197 / 607 / 1 535 M€ |
| Capital en année 30 : 5 % les plus bas / médiane / 5 % les plus hauts | 11,1 / 50,6 / 161,8 M€ | 36,3 / 170,9 / 553,1 M€ | 156 / 691 / 2 191 M€ |
| Part des trajectoires où le capital de l'année 20 est inférieur au capital initial | 32 % | 35 % | 35 % |
| … ou inférieur à la moitié du capital initial | 7 % | 8 % | 8 % |

Source : `sorties/mc_distribution_solutions.json`.

Lecture :
- **Les échecs se concentrent après la vingtième année.**
  - Les dividendes de transition s'arrêtent en année 10, et les dérives de coûts s'accumulent.
  - Le risque à 30 ans vaut 2 à 2,7 fois celui à 20 ans.
  - Un horizon de 20 ans ne suffit donc pas pour juger un montage patrimonial destiné à durer une vie entière.
- **La médiane cache une forte dispersion.**
  - Dans la moitié des cas, le capital de S2 dépasse 153 M€ en année 20.
  - Dans 5 % des cas, il tombe sous 49 M€.
  - C'est le propre d'un capital investi en actifs risqués : la règle de dépense lissée protège le domaine, pas le niveau du capital.
- **Les années de tension sont rares mais possibles.** Une trajectoire sur cinq connaît au moins une année où il faut appliquer les règles d'économie. Le propriétaire doit savoir à l'avance que cela peut arriver.

### 4.2 Ce qui fait rompre le modèle

| Facteur testé (10 000 trajectoires par ligne) | S1 : échec 20 / 30 ans | S2 : échec 20 / 30 ans | S3 : échec 20 / 30 ans |
|---|---:|---:|---:|
| **Référence** | **1,8 / 4,7 %** | **1,8 / 5,0 %** | **2,5 / 4,8 %** |
| Besoin au bas de la fourchette de L1 (0,21 / 0,79 / 2,20 M€) | 0,3 / 0,7 % | 0,3 / 0,7 % | 0,4 / 0,7 % |
| Besoin au haut de la fourchette de L1 (0,60 / 2,16 / 6,80 M€) | 11,3 / 22,6 % | 11,2 / 22,4 % | 13,8 / 23,5 % |
| Besoin +20 % | 3,1 / 8,1 % | 3,3 / 8,8 % | 4,1 / 8,3 % |
| Capital initial divisé par deux | 11,9 / 24,7 % (17 M€) | 14,4 / 28,3 % (60 M€) | 17,6 / 29,0 % (240 M€) |
| Capital initial réduit d'un tiers | 5,6 / 13,2 % (23 M€) | 6,3 / 14,6 % (80 M€) | 8,2 / 15,0 % (322 M€) |
| Capital initial augmenté d'un tiers | 0,8 / 2,0 % (45 M€) | 0,7 / 2,0 % (160 M€) | 1,0 / 2,0 % (638 M€) |
| Décès en année 15, droits de succession de 44 % | 4,0 / 14,1 % | 4,5 / 15,9 % | 3,8 / 12,5 % |
| Aucune règle de pilotage | 5,6 / 14,0 % | 6,8 / 16,0 % | 4,4 / 10,4 % |
| Décennie perdue (rendement moyen nul pendant 10 ans) | 2,8 / 7,8 % | 3,0 / 8,6 % | 3,6 / 7,8 % |
| Sinistres deux fois plus fréquents | 3,1 / 6,8 % | 3,0 / 7,0 % | 5,1 / 8,5 % |
| Pas de dividendes de transition | 3,0 / 6,8 % | 2,9 / 6,7 % | sans objet |
| Rendement réel net de 1,5 % (retrait inchangé) | 2,1 / 6,1 % | 2,2 / 6,6 % | 2,7 / 6,1 % |
| Rendement réel net de 2,5 % | 1,5 / 3,6 % | 1,5 / 3,7 % | 2,2 / 3,9 % |
| Rendement réel net de 3 % | 1,3 / 2,7 % | 1,4 / 3,0 % | 2,0 / 3,2 % |
| Une crise tous les 8 ans | 2,2 / 5,6 % | 2,3 / 5,9 % | 2,6 / 5,3 % |
| Une crise tous les 20 ans | 1,6 / 3,8 % | 1,5 / 4,0 % | 2,3 / 4,4 % |
| Sinistres deux fois moins fréquents | 1,2 / 3,1 % | 1,2 / 3,5 % | 1,5 / 3,0 % |
| Salaires +1,5 % réel par an | 1,9 / 5,1 % | 2,0 / 5,8 % | 2,5 / 5,2 % |
| Une seule entreprise au lieu de cinq | 2,0 / 4,7 % | 2,0 / 5,0 % | sans objet |

Sources : `sorties/mc_ruptures_S1.json`, `mc_ruptures_S2.json` et `mc_ruptures_S3.json`. Quand le besoin change, la réserve de trésorerie est ajustée dans la même proportion.

**Classement des risques, du plus au moins grave :**
1. **Une erreur de budget.**
   - Le haut de la fourchette de L1 multiplie le risque par 5,5 à 6,3 à 20 ans, et par 4,5 à 4,9 à 30 ans.
   - Pour tenir 30 ans à 95 % avec un besoin au niveau défavorable, il faudrait, avec un capital seul :
     - environ 67 M€ en S1 ;
     - environ 225 M€ en S2 ;
     - environ 890 M€ en S3.
   - C'est toujours 100 à 130 fois le besoin annuel.
2. **Un capital insuffisant.** Un capital divisé par deux multiplie le risque à 30 ans par 5 à 6.
3. **Un décès sans montage successoral.** Si 44 % du capital part en droits en année 15, le risque à 30 ans est multiplié par 2,6 à 3,2.
4. **L'absence de discipline.** Sans règles de pilotage, le risque à 30 ans est multiplié par 2,2 à 3,2.
5. **Une décennie perdue sur les marchés au départ.** Elle ajoute 3 à 3,6 points de risque à 30 ans : les premières années pèsent plus que les suivantes.
6. **Les sinistres.** Deux fois plus de sinistres non assurés ajoutent environ 2 points de risque à 30 ans en S1 et S2, et près de 4 points en S3, où le gros entretien pèse plus lourd.
7. **La fin prématurée des dividendes.** Pour S1 et S2, le risque à 30 ans augmente de 2 points environ. Le nombre d'entreprises dans la holding compte peu, parce que les dividendes ne pèsent que pendant les 10 premières années.
8. **Le rendement, à règle de retrait inchangée.** Un demi-point de moins n'ajoute que 1,3 à 1,6 point de risque **sur 30 ans**. Mais si le rendement reste sous le taux de retrait (1,75 %), le capital s'érode en euros constants. Le risque n'apparaît alors qu'après 30 ans, pour la génération suivante. Le § 4.3 donne le capital nécessaire quand le retrait est adapté au rendement.
9. **La fréquence des crises et la dérive des salaires.** Chacune ajoute moins d'un point à 30 ans.

### 4.3 Combien de capital pour quel niveau de sécurité ?

Le tableau suivant porte sur un capital seul, sans dividendes, avec les règles de pilotage, sur 30 ans (`sorties/mc_dotation_necessaire.json`). Le capital nécessaire est estimé par dichotomie sur 6 000 trajectoires, avec une précision d'environ ±5 %.

| Domaine | Besoin annuel | Capital pour 1 chance sur 2 de tenir 30 ans | Capital pour 95 % de chances | Avec les leviers vérifiés : 50 % / 95 % |
|---|---:|---:|---:|---:|
| S1 | 0,35 M€ | 14,1 M€ (41 fois le besoin) | 37,9 M€ (110 fois) | 13,0 / 35,1 M€ (38 / 102 fois) |
| S2 | 1,27 M€ | 50,1 M€ (39 fois) | 132,2 M€ (104 fois) | 46,3 / 122,1 M€ (36 / 96 fois) |
| S3 | 3,77 M€ | 165,9 M€ (44 fois) | 491,6 M€ (130 fois) | 153,4 / 454,3 M€ (41 / 121 fois) |

« Avec les leviers vérifiés » signifie que le besoin est réduit de 7,5 %. C'est le milieu de la fourchette des leviers du « prestige efficace » vérifiés par V2C (5 à 8 % du besoin de S2, L2 § 5). L'avantage fiscal des monuments historiques n'est pas compté : il réduit l'impôt personnel du propriétaire et suppose des revenus imposables au barème (V2R M4).

Règle simple à retenir :
- **environ 40 fois le besoin annuel** pour une chance sur deux de tenir 30 ans ;
- **environ 100 fois** pour 95 % de chances, et jusqu'à 130 fois pour un grand monument classé.

Comment lire ces multiples :
- **Le seuil d'une chance sur deux n'est pas un objectif.**
  - À 40 fois le besoin, le plafond normal de retrait (1,75 % du capital) ne couvre que 70 % du besoin.
  - Toutes les trajectoires simulées connaissent alors des années de tension, et 55 à 57 % des années sont en tension sur 20 ans (`sorties/mc_tension_seuils.json`). Le domaine vit en permanence sur des retraits d'urgence et des économies.
  - À 95 % de chances, seules 16 à 20 % des trajectoires connaissent au moins une année de tension, et 2 % au plus des années sont en tension.
- **Pourquoi environ 100 fois ?** Avec 57 fois le besoin (1 ÷ 1,75 %), le plafond normal couvrirait juste le besoin de l'année 1. Le capital doit en plus absorber la dérive des coûts (+11 % en 20 ans pour S2), les crises, les sinistres et la dispersion des rendements.

**Le capital nécessaire dépend surtout du rendement réel net.** Pour S2, avec un capital seul et 95 % de chances de tenir 30 ans (`sorties/mc_sensibilite_rendement.json`) :

| Rendement réel net | Taux de retrait adapté (rendement − 0,25 point) | Capital nécessaire | Écart avec le cas central |
|---:|---:|---:|---:|
| 1,5 % | 1,25 % | 168,6 M€ | +28 % |
| **2 %** | **1,75 %** | **132,2 M€** | — |
| 2,5 % | 2,25 % | 109,5 M€ | −17 % |
| 3 % | 2,75 % | 94,8 M€ | −28 % |
| 3,5 % | 3,25 % | 83,4 M€ | −37 % |

Autour du cas central (entre 1,5 et 2,5 %), chaque demi-point de rendement en moins ajoute 20 à 28 % au capital nécessaire.

Si l'on gardait un taux de retrait de 2,75 % avec un rendement de 1,5 %, 123,8 M€ suffiraient pour tenir 30 ans. Ce chiffre plus bas est trompeur : le domaine mangerait alors son capital, et le problème serait reporté sur la génération suivante.

### 4.4 Les autres modèles résistent-ils ?

- **Holding de PME qui ne fait que distribuer ses dividendes**, avec une petite dotation de 2 à 10 M€ (`sorties/mc_holding_hybride.json`) :
  - S1 : de 63 à 76 % d'échec avant 20 ans, et de 85 à 92 % avant 30 ans ;
  - S2 : de 70 à 90 % avant 20 ans, et de 88 à 98 % avant 30 ans.
  - Les défaillances d'entreprises, la volatilité des dividendes et l'absence de capital tampon rendent ce montage fragile. La holding peut **constituer** le capital, mais elle ne peut pas le **remplacer** (L2, § 6.2).
- **Modèles fondés sur les activités sur place** (M1 à M3, M7, M8) : ils couvrent dans le cas central entre 2,8 et 17,8 % du besoin de S2. Une crise de type 2020 supprime l'essentiel des revenus occasionnels (−80 %).
- **Locataire d'ancrage (M7).** Il apporte des revenus contractuels, mais deux exemples montrent que ces loyers aussi peuvent s'arrêter :
  - au premier semestre 2020, les loyers variables de Covivio ont baissé de 67 % [V2A-31] ;
  - des gestionnaires de résidences Pierre et Vacances ont suspendu leurs loyers à partir de 2020, et près de 20 000 bailleurs étaient sans paiement depuis janvier 2021 [V2A-62] [V2A-63].
- **Capital nécessaire selon le modèle** (S2, 95 % de chances de tenir 30 ans, `sorties/mc_comparaison_modeles.json`, L3 § 6) :
  - capital seul : 132,2 M€ ;
  - leviers vérifiés : 122,1 M€ ;
  - hybride avec 1 M€ de dividendes pendant 10 ans : 117,6 M€ ;
  - locataire d'ancrage : 114,9 M€.
  - Aucun modèle ne descend sous 90 fois le besoin annuel de S2.
- **Château-hôtel (M4).**
  - Sa contribution est négative dans le cas central (−28 % du besoin) et dans le cas défavorable (−55 %). Il ajoute un risque au lieu d'en retirer.
  - Dans l'échantillon de la vague 1, 20 sociétés de châteaux-hôtels sur 33 étaient en perte [R4-34].
  - La vérification indépendante retrouve ce résultat. Sur les seuls comptes 2023-2025 (26 sociétés), la part en perte est de 54 % et la marge nette médiane de −4,5 % [V2V].

---

## 5. Tenir 20 à 30 ans : ce que les chiffres ne montrent pas

1. **La dérive des coûts est lente mais certaine.**
   - Dans le cas central, les charges de S2 augmentent de 11 % en euros constants en 20 ans (de 1,28 à 1,42 M€). Avec des salaires à +1,5 % par an, la hausse atteint 18 %.
   - Les métiers des monuments historiques (taille de pierre, couverture, menuiserie à l'identique) n'ont pas d'indice public : leur dérive propre est INCONNUE [V2C-03].
   - La règle de dépense, elle, ne croît que si le capital croît.
2. **Le rendement réel net de 2 % est l'hypothèse la plus sensible après le budget.**
   - La seule donnée sourcée est le rendement des actions mondiales depuis 2000 : 3,5 % réel par an, avant frais et impôts [R8-32] [V2R-08].
   - Il faut en retirer des frais de 0,4 à 0,6 point, et un impôt de 30 à 38,6 % sur les revenus nominaux (PFU de 31,4 % et contributions sur les hauts revenus) [V2R-03] [V2R-04] [V2R-05] [V2R-16].
   - Selon l'équipe rouge, le rendement net serait de 1,1 à 1,8 % en détention directe, et presque nul via une holding à l'IS (V2R C2). Les 2 % retenus supposent une imposition en partie différée et une allocation majoritairement en actions.
   - Le véhicule juridique et fiscal du capital est discuté dans L2 (§ 6.3). Il doit être validé par un avocat fiscaliste avant tout engagement.
3. **L'inflation n'est représentée que par ses effets.**
   - Le modèle raisonne en euros constants.
   - Une longue période d'inflation forte avec des rendements réels négatifs n'est pas simulée en tant que telle. Le test de la décennie perdue en donne un ordre de grandeur : 8,6 % d'échec à 30 ans pour S2, au lieu de 5 %.
4. **Un sinistre total (incendie) n'est pas modélisé.**
   - Il est supposé couvert par l'assurance (3 ‰ de la valeur de reconstruction, L1). Un défaut d'assurabilité ou une sous-assurance changerait tout. Exemples :
     - la résiliation de l'assurance du château d'Olhain [R1-28] ;
     - le relèvement de la surprime « catastrophes naturelles » de 12 à 20 % en 2025 [R1-29].
   - La réserve doit être placée hors des contrats d'assurance-vie et de capitalisation, dont les rachats peuvent être limités jusqu'à 6 mois en cas de crise systémique [V2R-10].
5. **Les risques juridiques et politiques ne sont pas simulés.**
   - Exemples : changement du régime des monuments historiques, de l'IFI ou de la taxation des holdings. La taxe de 20 % sur les holdings patrimoniales de la loi de finances 2026 [R3-18] a vu son assiette changer en cours de vote [V2R-11] [V2R-12] ; le texte définitif doit être validé par un fiscaliste.
   - Leur effet passe par le besoin ou par le rendement, qui sont tous deux testés ci-dessus.
6. **Le régime matrimonial n'est pas simulé.** En communauté réduite aux acquêts, les revenus réinvestis deviennent des biens communs [V2R-07] (à valider par un notaire). Un divorce pourrait donc partager la part du capital constituée pendant le mariage.
7. **Les chocs sont indépendants entre eux**, sauf à travers la variable de crise, qui frappe ensemble les activités, le capital et les dividendes. En réalité, une hausse des taux ou de l'inflation pourrait frapper en même temps les rendements, les coûts de travaux et l'énergie.

---

## 6. Dépendance au fondateur

Le propriétaire a 26 ans. Un horizon de 30 ans le mène à 56 ans et traverse les événements d'une vie : mariage, enfants, séparation, maladie, succession. Le modèle mesure quatre canaux de dépendance.

1. **Les entreprises extérieures.**
   - Les dividendes de transition dépendent de l'activité d'entreprises, et souvent de la personne qui les dirige.
   - S'ils s'arrêtent dès l'année 3, le domaine ne fait pas faillite, mais son capital cesse de croître (§ 3.1). Sans aucun dividende, le risque à 30 ans passe de 5,0 à 6,7 % pour S2.
   - Une holding passive, sans capital tampon, échoue dans 85 à 98 % des cas sur 30 ans (§ 4.4).
   - **Conclusion** : la pérennité ne doit pas reposer sur un flux qui exige le travail du fondateur. Elle doit reposer sur un capital qui produit un revenu sans lui. La transition sert à **convertir** les revenus d'entreprise en capital.
2. **La discipline de dépense.**
   - Sans règles de pilotage, le risque à 30 ans passe de 5,0 à 16,0 % pour S2.
   - Or ces règles exigent de dire non, une année difficile, à une dépense de prestige. Un propriétaire seul qui décide de tout est exposé à la tentation inverse.
   - **Conclusion** : la règle de dépense, le seuil de réserve et les mesures de tension doivent être écrits dans des statuts ou dans une charte. Leur application doit être contrôlée par au moins une personne indépendante (comité, gérant ou administrateur extérieur). Le montage exact relève d'un notaire et d'un avocat (L7).
3. **Le décès ou l'incapacité.**
   - Le capital affecté reste la fortune du propriétaire (L2, § 6.3). À son décès, il entre dans sa succession.
   - Sans montage, environ 44 % du capital partirait en droits de succession [V2R-06] (ESTIMATION). Un décès en année 15 fait alors passer le risque à 30 ans de 5,0 à 15,9 % pour S2.
   - L'exonération de l'article 795 A ne vise que le monument et son mobilier, pas le capital qui le fait vivre [R3-13].
   - **Conclusion** : le montage successoral (démembrement, assurance-vie, donation-partage) et un plan en cas d'incapacité doivent être établis avec un notaire, dès la constitution du capital.
4. **Le régime matrimonial** (non simulé) : voir le § 5, point 6.

Les activités qui reposent sur la présence ou le talent personnel du propriétaire ont été écartées du socle de la solution :
- la pension haut de gamme ;
- la reproduction, qui exige un vétérinaire et un étalon (L2, § 3.1).

---

## 7. Tranquillité : ce que les crises font au calme du domaine

- **Le socle de la solution est calme.** Il comprend :
  - des revenus contractuels : logements dans les communs, hivernage de camping-cars, bail solaire, forêt ;
  - une pension de retraite au pré ;
  - deux journées de tournage par an.
  - Il ne comprend ni réception ni public. La pension standard en a été retirée : sa contribution est nulle dans le cas central, et elle ferait venir 25 à 30 propriétaires de chevaux chaque semaine (V2R m8).
- **En crise, la variable d'ajustement est la dépense, pas l'ouverture du domaine.** Les règles de pilotage coupent les dépenses discrétionnaires et reportent des travaux. Elles n'ajoutent aucune activité.
- **Ouvrir le domaine en cas de difficulté rapporterait peu.**
  - Ajouter des réceptions, des séminaires et la location d'une grande maison (modèle M2 par rapport à M1) n'apporte qu'environ 32 k€ par an dans le cas central, soit 2,5 points de couverture du besoin de S2.
  - Cela demande 1 M€ d'investissement de plus et apporte des nuisances.
  - Ces revenus occasionnels sont aussi les premiers à disparaître en crise (−80 %).
- **La seule activité qui change l'ordre de grandeur, le locataire d'ancrage (M7), est incompatible avec une partie entièrement privée en S2.**
  - Elle apporterait environ 0,23 M€ disponibles par an dans le cas central.
  - Elle suppose de confier 40 à 60 chambres à un exploitant de séminaires pendant 15 à 30 ans.
  - Aucun cas lu ne documente la cohabitation d'un propriétaire résidant avec un exploitant de 40 chambres ou plus (V2A).
  - Elle n'est envisageable que si la localisation et la taille le permettent, ce qui est plus plausible en S3. Même alors, elle ne réduit le capital nécessaire que d'environ 5 % en S3 (L3, modèle 4).

---

## 8. Règles de pilotage recommandées

Les règles marquées « simulée » sont incluses dans le modèle et dans la simulation de Monte-Carlo. Les autres sont des recommandations de bon sens qui n'ont **pas** été simulées.

| Indicateur | Seuil | Action | Statut |
|---|---|---|---|
| Réserve de trésorerie | Moins d'un an de charges | Couper 10 % du besoin en dépenses discrétionnaires ; reporter 30 % de la campagne de travaux ; retrait d'urgence plafonné à 4 % du capital ; puis reconstituer la réserve | simulée |
| Retrait annuel sur le capital | Plafond lissé : 80 % du plafond précédent + 20 % × 1,75 % × capital | Ne jamais dépasser le plafond en dehors des années de tension | simulée |
| Fonds de travaux | Provision versée chaque année, même en tension | Le report d'une campagne reste dû ; un sinistre est payé en plus, sans annuler de travaux | simulée |
| Placement de la réserve | — | Hors contrats d'assurance-vie et de capitalisation, dont les rachats peuvent être gelés [V2R-10] | non simulée |
| Capital réel | Moins de 80 % du capital initial, en euros constants | Revoir le budget ; suspendre les investissements futurs et les achats de prestige | non simulée |
| Rendement réel moyen sur 5 ans | Moins de 1,5 % par an | Revoir l'allocation et les frais ; ramener le taux de retrait vers 1,25 % | non simulée |
| Besoin réel mesuré | Plus de 10 % au-dessus du budget pendant 2 ans | Recalculer le capital nécessaire ; activer les leviers du « prestige efficace » (L2, § 5) | non simulée |
| Dividendes de transition | Moins de 50 % du prévu pendant 2 ans | Ne pas compenser par des activités bruyantes ; allonger la constitution du capital | non simulée |
| Événement familial | Mariage, naissance, séparation, maladie | Revoir le montage successoral et le régime matrimonial avec le notaire | non simulée |

Un seuil à 80 % du capital initial serait souvent franchi : dans 35 % des trajectoires simulées, le capital de S2 est inférieur au capital initial en année 20 (§ 4.1). Ce n'est pas un échec, mais un signal de vigilance.

---

## 9. Limites et prochaines vérifications

- **Calibrage du Monte-Carlo.** La fréquence des crises (1 sur 12), leur ampleur (−25 points de rendement), l'écart-type des rendements (10 points), les sinistres et la défaillance des entreprises sont des HYPOTHÈSES. Les probabilités ci-dessus sont donc **relatives** : elles servent à comparer des montages et à classer des risques, pas à promettre un niveau de sécurité.
- **Critère n° 6 respecté au plus juste.** Les solutions échouent dans environ 5 % des cas sur 30 ans. Un besoin réel supérieur de 20 % suffit à porter ce risque à 8 ou 9 %. Le respect du critère dépend donc de la validation du budget.
- **Le budget reste l'incertitude principale.** La fourchette de L1 (0,79 à 2,16 M€ pour S2) est plus large que tous les chocs testés. Le rapport public IGF-IGAC de 2020 et les cas réels ne permettent ni de valider ni d'infirmer le budget de S2 [V2C-07]. C'est la priorité de la phase 1 de la feuille de route (L7).
- **Contrôles externes.**
  - La vérification indépendante de 90 chiffres clés (`01_RECHERCHE/V2V_verification.md`) n'a trouvé aucun chiffre faux. Elle a nuancé 9 chiffres (périmètres, unités, statuts), sans changer de valeur du modèle.
  - L'équipe rouge (`01_RECHERCHE/V2R_equipe_rouge.md`) a formulé 29 constats, dont 2 critiques. Ses corrections ont été reportées dans le modèle et dans ce document. Leur traitement est détaillé dans L8, § 6.
