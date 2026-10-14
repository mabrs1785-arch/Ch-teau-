# L5 — Démonstration chiffrée : la solution couvre-t-elle vraiment tous les coûts ?

> **Statut de ce document**
> - Démonstration arithmétique, en euros constants 2026, à partir du classeur `02_MODELE/sorties/Modele_equation_chateau.xlsx` (feuilles Budget, Proj_* et ST_*) et des résultats de la simulation (`02_MODELE/sorties/mc_*.json`).
> - Elle prouve que la solution **équilibre l'équation** sous les hypothèses du modèle. Elle ne prouve pas que ces hypothèses sont justes. Le § 7 dit ce qui reste à démontrer sur un bien réel.

---

## 1. La réponse

**Oui, sous trois conditions** : un budget juste, un capital réellement constitué et une discipline de dépense.

- **Chaque année des 20 ans, dans le cas central, les ressources égalent exactement les besoins.** La capacité de financement (activités, dividendes et plafond de retrait) dépasse les charges d'au moins 51 % ; sans compter les dividendes, de 34 à 67 % selon les années (§ 3).
- **Sur 20 ans**, le domaine S2 dépense 26,2 M€. Ils sont couverts par :
  - 0,9 M€ d'activités (3,6 %) ;
  - 10 M€ de dividendes de transition (38,2 %) ;
  - 15,2 M€ de retraits sur le fonds d'entretien (58,2 %).
  - Le fonds finit à 88,1 M€, contre 60 M€ au départ (§ 4).
- **Dans les huit stress tests**, aucune année n'est découverte. La marge la plus faible est de 12 %, dans le cumul des chocs, en année 20 (§ 5).
- **Dans la simulation de 20 000 trajectoires**, la couverture tient 20 ans dans 95,7 % des cas et 30 ans dans 88,9 % des cas (L6).
- **Tous les postes du coût réel de L1 sont dans l'équation**, gros entretien, IFI et imprévus compris. Seuls l'achat, la restauration initiale et le train de vie personnel en sont exclus, comme le prévoit le brief (§ 2).

---

## 2. Tous les coûts sont-ils dans l'équation ?

| Poste de L1 (S2, central, an 1) | Montant | Où il est dans la projection | Couvert ? |
|---|---:|---|:---:|
| Entretien courant du bâti | 90 k€ | Charges courantes (autres) | oui |
| Provision de gros entretien et aléas de chantier | 311 k€ | Fonds de travaux, dépensé par campagnes tous les 4 ans | oui |
| Sécurité | 7 k€ | Charges courantes (autres) | oui |
| Personnel (10 ETP) | 404 k€ | Charges de personnel, avec une dérive de +0,5 % réel par an | oui |
| Jardins, parc, prairies, clôtures, bois | 44 k€ | Charges courantes (autres) | oui |
| Équipements (renouvellement, entretien, carburant) | 80 k€ | Charges courantes (autres) | oui |
| Chevaux du propriétaire et installations équestres | 70 k€ | Charges courantes (autres) | oui |
| Énergie et eau | 59 k€ | Énergie (+2 % réel par an) ; eau dans les autres charges | oui |
| Assurances | 45 k€ | Assurances (+1,85 % réel par an) | oui |
| Impôts et taxes, dont IFI | 29 k€ | Charges courantes (autres) | oui |
| Administration et suivi patrimonial | 31 k€ | Charges courantes (autres) | oui |
| Imprévus d'exploitation | 23 k€ | Charges courantes (autres) | oui |
| Investissements futurs | 47 k€ | Charges courantes (autres) | oui |
| **Total** | **1 239 k€** | **Charges du domaine : 1 246 k€ l'an 1 (avec la première année de dérive)** | **oui** |
| Investissement initial des activités (logements, hivernage) | 1 100 k€ | Prélevé sur le capital du fonds l'année 1 | oui |
| Dette d'acquisition (scénario complémentaire de L1) | 183 k€ par an | Option désactivée : l'achat est un problème distinct (brief) | non, par choix |
| Achat, restauration initiale, train de vie, chevaux de compétition | — | Hors périmètre (L1, § 8) | non, par choix |

Les deux montants de la dernière ligne du total diffèrent de 7 k€ : la projection applique dès l'année 1 les dérives réelles des salaires, des travaux, de l'énergie et des assurances.

---

## 3. L'équation, année par année (S2, cas central)

L'équation de L2 s'écrit : **activités + dividendes + retrait sur le fonds = charges du domaine** (gros entretien provisionné compris), avec une réserve qui absorbe les écarts.

| Années | Charges du domaine | Activités disponibles | Dividendes | Retrait sur le fonds | Solde de l'année | Plafond de retrait autorisé | Part du plafond utilisée |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 246 k€ | 20 k€ | 1 000 k€ | 226 k€ | 0 | 1 650 k€ | 14 % |
| 2 à 10 | 1 252 → 1 305 k€ | 37 → 49 k€ | 1 000 k€ | 215 → 255 k€ | 0 | 1 653 → 1 883 k€ | 12 à 14 % |
| 11 | 1 311 k€ | 49 k€ | 0 | 1 262 k€ | 0 | 1 928 k€ | 65 % |
| 12 à 20 | 1 318 → 1 377 k€ | 49 k€ | 0 | 1 269 → 1 328 k€ | 0 | 1 969 → 2 252 k€ | 59 à 64 % |

Le tableau complet, année par année, est dans L4 (§ 4.1).

**Lecture.**
- Le solde est nul chaque année : le retrait sur le fonds est exactement ce qui manque après les activités et les dividendes. La réserve reste à 1,5 M€.
- **La marge de sécurité est la part du plafond qui n'est pas utilisée.** Pendant la transition, le domaine n'utilise que 12 à 14 % du plafond : les dividendes font l'essentiel. Après l'année 10, il en utilise 59 à 65 %.
- La capacité de financement (activités, dividendes et plafond de retrait) dépasse les charges d'au moins 51 % chaque année. Ce minimum est atteint en année 11, au moment où les dividendes s'arrêtent.

---

## 4. Sources et emplois sur 20 ans

| | S1 | S2 | S3 |
|---|---:|---:|---:|
| **Charges du domaine sur 20 ans** | **6,89 M€** | **26,18 M€** | **77,21 M€** |
| dont charges courantes | 4,88 M€ | 19,45 M€ | 51,71 M€ |
| dont gros entretien (provisionné puis dépensé) | 2,02 M€ | 6,74 M€ | 25,49 M€ |
| **Financées par :** | | | |
| les activités sur place (après impôts) | 0,29 M€ (4 %) | 0,94 M€ (4 %) | 1,76 M€ (2 %) |
| les dividendes de transition | 4,00 M€ (58 %), dont 0,79 M€ d'excédents versés au fonds | 10,00 M€ (38 %) | — |
| les retraits sur le fonds d'entretien | 3,39 M€ (49 %) | 15,24 M€ (58 %) | 75,45 M€ (98 %) |
| **Fonds d'entretien** | | | |
| au départ | 15,0 M€ | 60,0 M€ | 210,0 M€ |
| rendement réel cumulé | 11,8 M€ | 44,4 M€ | 142,3 M€ |
| en année 20 | 23,9 M€ | 88,1 M€ | 274,6 M€ |

Notes :
- Pour S1, la somme des parts dépasse 100 % parce que 0,79 M€ de dividendes excédentaires sont reversés au fonds.
- **Contrôle de cohérence (S2)** : 60 M€ de départ + 44,4 M€ de rendement − 15,2 M€ de retraits − 1,1 M€ d'investissement des activités = 88,1 M€. C'est bien la valeur de l'année 20 du classeur.

**Ce que montre ce tableau.**
- Les activités sur place financent 2 à 4 % des charges. Ce chiffre confirme, sur 20 ans, le constat de L2.
- Le fonds rapporte en 20 ans de deux à trois fois et demie ce qu'il verse au domaine (S3 : 1,9 ; S2 : 2,9 ; S1 : 3,5). C'est la marge qui protège contre les mauvais scénarios (§ 5).

---

## 5. La couverture résiste-t-elle aux chocs ?

| Projection (20 ans) | Années découvertes | Marge minimale de capacité, et année | Part maximale du plafond utilisée | Fonds en année 20 |
|---|---:|---:|---:|---:|
| S2, cas central | 0 | 51 % (an 11) | 65 % | 88,1 M€ |
| Activités −30 % | 0 | 49 % (an 11) | 66 % | 87,7 M€ |
| Crise de type 2020 en année 5 | 0 | 22 % (an 14) | 82 % | 61,8 M€ |
| Sinistre de 600 k€ et campagnes +30 % | 0 | 16 % (an 12) | 86 % | 85,8 M€ |
| Énergie ×2 pendant 3 ans | 0 | 50 % (an 11) | 66 % | 87,8 M€ |
| Salaires +1,5 % réel par an | 0 | 45 % (an 11) | 68 % | 86,9 M€ |
| Entreprises défaillantes et rendement de 2 % | 0 | 24 % (an 20) | 80 % | 59,9 M€ |
| **Cumul des chocs** | **0** | **12 % (an 20)** | **89 %** | **60,3 M€** |
| S1, cas central | 0 | 52 % (an 11) | 65 % | 23,9 M€ |
| S1, cumul des chocs | 0 | 11 % (an 6, année du sinistre) | 86 % | 16,1 M€ |
| S3, cas central | 0 | 59 % (an 1) | 63 % | 274,6 M€ |

« Marge de capacité » = (activités + dividendes + plafond de retrait − charges et dépassements de travaux) ÷ (charges et dépassements de travaux).

**Lecture.**
- Dans aucun test le domaine n'a besoin du retrait d'urgence. La réserve ne descend jamais sous un an de besoin.
- Le cumul des chocs consomme presque toute la marge à la fin des 20 ans (12 %). Au-delà, une nouvelle crise déclencherait les règles de tension. C'est ce que la simulation sur 30 ans mesure : 11,1 % d'échec pour S2 (L6, § 4).

---

## 6. Contrôles de fiabilité du calcul

| Contrôle | Résultat |
|---|---|
| Recalcul complet du classeur par LibreOffice | 11 301 formules, 0 erreur |
| Comparaison cellule par cellule entre Excel et un calcul Python indépendant | 0 écart (tolérance de 0,50 €) |
| Simulation de Monte-Carlo sans chocs, comparée aux 4 projections centrales | Écart maximal inférieur à un millionième d'euro |
| Identité annuelle : activités + dividendes + retrait = charges | Vérifiée chaque année (solde nul, réserve constante) |
| Identité du fonds (S2) : départ + rendement − retraits − investissement = fin | 60 + 44,4 − 15,2 − 1,1 = 88,1 M€ |
| Vérification indépendante de 90 chiffres clés à la source (V2V) | 81 confirmés, 9 nuancés, aucun faux |
| Sensibilité du besoin, hypothèse par hypothèse | Recalculée par `02_MODELE/sensibilite.py` ; mêmes résultats que la version précédente pour S1 et S2 |

---

## 7. Ce que cette démonstration ne prouve pas

1. **Que le budget est juste.** Le besoin de L1 est un budget **nécessaire**, calculé, pas un budget **observé** : aucun budget complet de domaine privé de cette taille n'est publié [V2C]. Au haut de la fourchette de L1 (2,06 M€ pour S2), la solution échoue dans 30 % des cas avant 20 ans (L6, § 4.2).
2. **Que le rendement réel net de 3 % est atteignable.** Il dépend du véhicule juridique et fiscal du fonds, de l'allocation et des frais. À 2 %, le risque à 30 ans passe d'environ 11 à 19 %.
3. **Que le capital peut être réuni.** La démonstration commence une fois le fonds constitué. L4 (§ 6) montre qu'il faut 10 à 35 ans d'épargne selon son rythme, sauf cession d'entreprise ou de bâtiments.
4. **Qu'un fonds d'entretien privé de cette taille existe en France.** Les exemples documentés sont britanniques : Burghley [R5-07], Blenheim [R5-03] et Northumberland [R5-14]. Le véhicule français est à construire avec un avocat fiscaliste (L4, § 2).
5. **Que les règles seront respectées pendant 30 ans.** La simulation suppose que la charte est appliquée. Sans elle, le risque double.

Ces cinq points sont les étapes de validation de la feuille de route (L7).
