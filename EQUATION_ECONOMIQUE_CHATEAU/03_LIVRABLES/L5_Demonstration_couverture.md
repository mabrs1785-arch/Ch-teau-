# L5 — Démonstration chiffrée : la solution couvre-t-elle vraiment tous les coûts ?

> **Statut de ce document**
> - Démonstration arithmétique, en euros constants 2026, à partir du classeur `02_MODELE/sorties/Modele_equation_chateau.xlsx` (feuilles Budget, Proj_* et ST_*) et des résultats de la simulation (`02_MODELE/sorties/mc_*.json`).
> - Version révisée après l'équipe rouge (V2R) : rendement réel net du capital de 2 % au lieu de 3 %, sinistres payés en plus du fonds de travaux, réserve reconstituée, solution S2 redimensionnée à 120 M€.
> - Elle prouve que la solution **équilibre l'équation** sous les hypothèses du modèle. Elle ne prouve pas que ces hypothèses sont justes. Le § 7 dit ce qui reste à démontrer sur un bien réel.

---

## 1. La réponse

**Oui, sous quatre conditions** : un budget juste, un capital réellement constitué, une transmission organisée et une discipline de dépense. Ce capital reste la fortune du propriétaire (L2, § 6.3).

- **Chaque année des 20 ans, dans le cas central, les ressources couvrent les charges du domaine et maintiennent la réserve à son niveau.**
  - La capacité de financement (activités, dividendes et plafond de retrait) dépasse les charges d'au moins 77 %.
  - Sans compter les dividendes, les activités et le plafond de retrait couvrent à eux seuls 165 à 188 % des charges selon les années (§ 3).
- **Sur 20 ans**, le domaine S2 consomme 27,2 M€ : 26,9 M€ de charges et 0,3 M€ pour maintenir la réserve. Ils sont couverts par :
  - 0,8 M€ d'activités (3 %) ;
  - 10 M€ de dividendes de transition (37 %) ;
  - 16,4 M€ de retraits sur le capital affecté (60 %).
  - Le capital finit à 158,1 M€, contre 120 M€ au départ (§ 4).
- **Dans les sept stress tests**, aucune année n'est découverte. La marge la plus faible est de 28 %, dans le cumul des chocs, en année 20 (§ 5).
- **Dans la simulation de 20 000 trajectoires**, la couverture tient 20 ans dans 98,2 % des cas et 30 ans dans 95,2 % des cas (L6, § 4.1).
- **Tous les postes du coût réel de L1 sont dans l'équation** : gros entretien avec maîtrise d'œuvre, IFI et imprévus compris. En sont exclus l'achat, la restauration initiale et le train de vie personnel, comme le prévoit le brief. Les chevaux de sport et les infrastructures du domaine (murs, allées, réseaux) ne sont pas chiffrés (§ 2).

---

## 2. Tous les coûts sont-ils dans l'équation ?

| Poste de L1 (S2, central) | Montant annuel | Où il est dans la projection | Couvert ? |
|---|---:|---|:---:|
| Entretien courant du bâti | 90 k€ | Charges courantes (autres) | oui |
| Provision de gros entretien, aléas de chantier et maîtrise d'œuvre | 344 k€ | Fonds de travaux, dépensé par campagnes tous les 4 ans | oui |
| Sécurité | 7 k€ | Charges courantes (autres) | oui |
| Personnel (10 ETP) | 404 k€ | Charges de personnel, avec une dérive de +0,5 % réel par an | oui |
| Jardins, parc, prairies, clôtures, bois | 44 k€ | Charges courantes (autres) | oui |
| Équipements (renouvellement, entretien, carburant) | 80 k€ | Charges courantes (autres) | oui |
| Chevaux du propriétaire et installations équestres | 70 k€ | Charges courantes (autres) | oui |
| Énergie et eau | 59 k€ | Énergie (+2 % réel par an) | oui |
| Assurances | 45 k€ | Assurances (+1,85 % réel par an) | oui |
| Impôts et taxes, dont IFI | 29 k€ | Charges courantes (autres) | oui |
| Administration et suivi patrimonial | 31 k€ | Charges courantes (autres) | oui |
| Imprévus d'exploitation | 23 k€ | Charges courantes (autres) | oui |
| Investissements futurs | 48 k€ | Charges courantes (autres) | oui |
| **Total** | **1 273 k€** | **Charges du domaine : 1 280 k€ l'an 1** | **oui** |
| Sinistres et dépassements de travaux non assurés | variable | Payés en plus du fonds de travaux (tests « travaux » et Monte-Carlo) | oui |
| Investissement initial des activités (logements, hivernage) | 1 100 k€ | Prélevé sur le capital l'année 1 | oui |
| Dette d'acquisition (scénario complémentaire de L1) | 183 k€ par an | Option désactivée : l'achat est un problème distinct (brief) | non, par choix |
| Achat, restauration initiale, train de vie personnel | — | Hors périmètre (L1, § 8) | non, par choix |
| Chevaux de sport : achat, renouvellement, transport, concours | INCONNU (+15 à 40 k€ par an selon une HYPOTHÈSE non sourcée de l'équipe rouge) | Non compté (L1, § 8) | **non** |
| Infrastructures du domaine : murs, allées, voirie, réseaux, étangs, ponts | INCONNU | Non compté (L1, § 8) | **non** |

Le total de L1 (1 273 k€) et les charges de l'année 1 (1 280 k€) diffèrent de 7 k€ : la projection applique dès l'année 1 les dérives réelles des salaires, des travaux, de l'énergie et des assurances.

Les deux dernières lignes sont de vrais trous du budget, pas des choix de périmètre. Elles doivent être chiffrées sur le bien réel (L7, phase 1).

---

## 3. L'équation, année par année (S2, cas central)

L'équation de L2 s'écrit :

**activités + dividendes + retrait sur le capital = charges du domaine + maintien de la réserve**

Les charges comprennent le gros entretien provisionné. Le maintien de la réserve est le petit montant qui la garde à sa cible : celle-ci suit les charges, et la trésorerie perd 0,5 % réel par an.

| Années | Charges du domaine | Activités disponibles | Dividendes | Retrait sur le capital | Maintien de la réserve | Plafond de retrait autorisé | Part du plafond utilisée |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 280 k€ | 17 k€ | 1 000 k€ | 270 k€ | 7 k€ | 2 100 k€ | 13 % |
| 2 à 10 | 1 286 → 1 341 k€ | 32 → 43 k€ | 1 000 k€ | 265 à 314 k€ | 15 → 16 k€ | 2 104 → 2 300 k€ | 13 à 14 % |
| 11 | 1 348 k€ | 43 k€ | 0 | 1 322 k€ | 16 k€ | 2 337 k€ | 57 % |
| 12 à 20 | 1 355 → 1 416 k€ | 43 k€ | 0 | 1 329 → 1 391 k€ | 16 → 17 k€ | 2 371 → 2 617 k€ | 53 à 56 % |

Le tableau complet, année par année, est dans L4 (§ 4.1). L'investissement initial des activités (1,1 M€, année 1) est prélevé directement sur le capital : il n'apparaît pas dans ce tableau.

**Lecture.**
- Le retrait sur le capital est exactement ce qui manque après les activités et les dividendes, plus le maintien de la réserve. La réserve passe de 1,50 à 1,66 M€ en 20 ans, au rythme des charges.
- **La marge de sécurité est la part du plafond qui n'est pas utilisée.**
  - Pendant la transition, le domaine n'utilise que 13 à 14 % du plafond : les dividendes font l'essentiel.
  - Après l'année 10, il en utilise 53 à 57 %.
- La capacité de financement (activités, dividendes et plafond de retrait) dépasse les charges d'au moins 77 % chaque année. Ce minimum est atteint en année 11, au moment où les dividendes s'arrêtent.

---

## 4. Sources et emplois sur 20 ans

| | S1 | S2 | S3 |
|---|---:|---:|---:|
| **Charges du domaine sur 20 ans** | **7,33 M€** | **26,91 M€** | **79,96 M€** |
| dont charges courantes | 5,10 M€ | 19,47 M€ | 51,81 M€ |
| dont gros entretien (provisionné, puis entièrement dépensé en 5 campagnes) | 2,23 M€ | 7,44 M€ | 28,15 M€ |
| Maintien de la réserve (hausse et rendement réel négatif de la trésorerie) | 0,08 M€ | 0,32 M€ | 0,87 M€ |
| Excédents de dividendes versés au capital | 0,52 M€ | — | — |
| **Total des emplois** | **7,93 M€** | **27,23 M€** | **80,83 M€** |
| **Financés par :** | | | |
| les activités sur place (après impôts) | 0,25 M€ (3 %) | 0,81 M€ (3 %) | 1,52 M€ (2 %) |
| les dividendes de transition | 4,00 M€ (50 %) | 10,00 M€ (37 %) | — |
| les retraits sur le capital affecté | 3,68 M€ (46 %) | 16,42 M€ (60 %) | 79,32 M€ (98 %) |
| **Capital affecté** | | | |
| au départ | 34,0 M€ | 120,0 M€ | 480,0 M€ |
| rendement réel cumulé (2 % par an) | 16,2 M€ | 55,6 M€ | 215,6 M€ |
| investissement initial des activités | 0,3 M€ | 1,1 M€ | 2,2 M€ |
| en année 20 | 46,8 M€ | 158,1 M€ | 614,1 M€ |

**Contrôles de cohérence** (valeurs du classeur, en M€ arrondis au centième) :
- **Capital de S2** : 120 de départ + 55,59 de rendement − 16,42 de retraits − 1,10 d'investissement = 158,07, soit 158,1 M€. C'est bien la valeur de l'année 20 du classeur.
- **Capital de S1** : 34 + 16,23 − 3,68 + 0,52 d'excédents − 0,27 ≈ 46,8 M€.
- **Capital de S3** : 480 + 215,57 − 79,32 − 2,18 = 614,07, soit 614,1 M€.
- **Ressources de S2** : 0,81 + 10,00 + 16,42 = 27,23 M€, égal au total des emplois.

**Ce que montre ce tableau.**
- Les activités sur place financent 2 à 3 % des ressources. Ce chiffre confirme, sur 20 ans, le constat de L2.
- Dans le cas central, le capital rapporte en 20 ans de 2,7 à 4,4 fois ce qu'il verse au domaine (S3 : 2,7 ; S2 : 3,4 ; S1 : 4,4).
- Cette croissance n'est pas un surplus à dépenser : c'est la marge qui protège contre les mauvais scénarios (§ 5 et L6). Dans 5 % des trajectoires simulées, le capital de S2 tombe sous 49 M€ en année 20.

---

## 5. La couverture résiste-t-elle aux chocs ?

| Projection (20 ans) | Années découvertes | Marge de capacité minimale (année) | Part maximale du plafond utilisée | Capital en année 20 |
|---|---:|---:|---:|---:|
| S2, cas central | 0 | 77 % (an 11) | 57 % | 158,1 M€ |
| Activités −30 % | 0 | 76 % (an 11) | 57 % | 157,8 M€ |
| Crise de type 2020 en année 5 | 0 | 40 % (an 19) | 72 % | 114,5 M€ |
| Sinistre de 600 k€ et campagnes +30 % | 0 | 33 % (an 12) | 75 % | 154,7 M€ |
| Énergie ×2 pendant 3 ans | 0 | 76 % (an 11) | 56 % | 157,8 M€ |
| Salaires +1,5 % réel par an | 0 | 70 % (an 11) | 59 % | 156,9 M€ |
| Entreprises défaillantes et rendement de 1 % | 0 | 50 % (an 20) | 67 % | 118,5 M€ |
| **Cumul des chocs** | **0** | **28 % (an 20)** | **79 %** | **112,2 M€** |
| S1, cas central | 0 | 89 % (an 11) | 53 % | 46,8 M€ |
| S1, cumul des chocs | 0 | 4 % (an 6, année du sinistre) | 95 % | 33,1 M€ |
| S3, cas central | 0 | 122 % (an 2) | 45 % | 614,1 M€ |

Définitions :
- « Marge de capacité » = (activités + dividendes + plafond de retrait − charges et dépassements de travaux) ÷ (charges et dépassements de travaux).
- « Part du plafond utilisée » = retrait de l'année ÷ plafond de la règle de dépense.

**Lecture.**
- Dans aucun test le domaine n'a besoin du retrait d'urgence. La réserve ne descend jamais sous un an de charges.
- Le cumul des chocs consomme une grande partie de la marge à la fin des 20 ans (28 %). La simulation sur 30 ans mesure ce qui se passe au-delà : environ 5 % d'échec pour S2 (L6, § 4).
- **Pour S1, l'année du sinistre est la plus serrée de toutes** : il ne reste que 4 % de marge. Ce sont les dividendes de transition qui évitent la tension. Un petit domaine supporte mal un gros sinistre non assuré.

---

## 6. Contrôles de fiabilité du calcul

| Contrôle | Résultat |
|---|---|
| Recalcul complet du classeur par LibreOffice | 11 814 formules, 0 erreur |
| Comparaison cellule par cellule entre Excel et un calcul Python indépendant | 0 écart (tolérance de 0,50 €) |
| Simulation de Monte-Carlo sans chocs, comparée aux 4 projections centrales | Écart maximal inférieur à un millionième d'euro (`sorties/verification.json`) |
| Identité annuelle : activités + dividendes + retrait = charges + maintien de la réserve | Vérifiée chaque année |
| Identité du capital (S1, S2, S3) : départ + rendement − retraits + excédents − investissement = fin | Vérifiée au dixième de million près (§ 4) |
| Vérification indépendante de 90 chiffres clés à la source (V2V) | 81 confirmés, 9 nuancés, aucun faux |
| Équipe rouge (V2R) : 29 constats sur le modèle et les livrables | Corrections reportées dans le modèle ; traitement détaillé dans L8, § 6 |
| Sensibilité du besoin, hypothèse par hypothèse | Recalculée par `02_MODELE/sensibilite.py` (`sorties/sensibilite_budget.json`) |

---

## 7. Ce que cette démonstration ne prouve pas

1. **Que le budget est juste.** Le besoin de L1 est un budget **nécessaire**, calculé, pas un budget **observé** : aucun budget complet de domaine privé de cette taille n'est publié [V2C]. Au haut de la fourchette de L1 (2,16 M€ pour S2), la solution échoue dans 11 % des cas avant 20 ans et dans 22 % avant 30 ans (L6, § 4.2). Deux postes ne sont pas chiffrés du tout : les chevaux de sport et les infrastructures du domaine (§ 2).
2. **Que le rendement réel net de 2 % est atteignable.**
   - Il dépend du véhicule juridique et fiscal du capital, de l'allocation et des frais.
   - L'équipe rouge l'estime entre 1,1 et 1,8 % en détention directe (V2R C2).
   - À 1,5 %, avec un retrait adapté, il faut 168,6 M€ de capital seul au lieu de 132,2 M€ pour S2 (L6, § 4.3).
3. **Que le capital peut être réuni.**
   - La démonstration commence une fois le capital constitué.
   - À 2 % réel, réunir 120 M€ prend environ 62 ans d'épargne à 1 M€ par an, 34 ans à 2,5 M€ par an, 20 ans à 5 M€ par an et 11 ans à 10 M€ par an (L4, § 6).
   - Hors héritage ou cession d'entreprise, c'est l'obstacle principal.
4. **Que le capital est séparé de la fortune du propriétaire.**
   - Aucun véhicule français ne l'en sépare tout en lui laissant la jouissance du château (L2, § 6.3).
   - La démonstration suppose que ce capital ne sert qu'au domaine. Juridiquement, il reste exposé aux droits de succession (environ 44 % sans montage [V2R-06]) et, selon le régime matrimonial, au partage des revenus réinvestis [V2R-07].
5. **Que les règles seront respectées pendant 30 ans.** La simulation suppose que la charte est appliquée. Sans elle, le risque d'échec à 30 ans passe de 5 à 16 % pour S2 (L6, § 6).

Ces cinq points sont les étapes de validation de la feuille de route (L7).
