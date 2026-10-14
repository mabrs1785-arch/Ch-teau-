# L4 — La meilleure solution, modélisée sur 20 ans (domaine S2)

> **Statut de ce document**
> - Modèle complet de la solution retenue (L3, modèles 1 et 3, avec le socle d'activités calmes), en euros constants 2026.
> - Version révisée après l'équipe rouge (V2R) :
>   - rendement réel net du capital ramené de 3 % à 2 % ;
>   - sinistres payés en plus du fonds de travaux ;
>   - réserve reconstituée ;
>   - maîtrise d'œuvre ajoutée ;
>   - solution redimensionnée pour respecter le critère n° 6 du cadre analytique (au plus 5 % d'échec sur 20 et sur 30 ans).
> - Tous les chiffres viennent de la feuille `Proj_S2_solution` du classeur `02_MODELE/sorties/Modele_equation_chateau.xlsx`. Chaque cellule y est une formule, vérifiée par un calcul Python indépendant, et la simulation de Monte-Carlo sans chocs la reproduit à l'identique.
> - Les variantes S1 et S3 sont dans les feuilles `Proj_S1_solution` et `Proj_S3_solution`.
> - **Les montages juridiques et fiscaux décrits ici sont des pistes à faire valider** par un avocat fiscaliste, un notaire et un expert-comptable. Ce n'est pas un conseil juridique.

---

## 1. La solution en une page

**Le principe.** Le domaine ne vit pas de ses activités. Il vit d'un **capital affecté** : un portefeuille diversifié, réservé au domaine par une charte et, si possible, par une structure à statuts contraignants, et géré avec une règle de dépense.

Ce capital reste **juridiquement la fortune du propriétaire**. Aucun véhicule français ne l'en sépare tout en laissant la jouissance privée du château (L2, § 6.3).

Pendant 10 ans, des **dividendes d'entreprises** complètent ce capital et le laissent grandir. Un **socle d'activités calmes** occupe et entretient les dépendances, sans troubler la vie privée.

| Élément | Domaine S2 (cas central) |
|---|---|
| Besoin annuel du domaine | 1,28 M€ l'année 1, puis 1,42 M€ en année 20, avec les dérives réelles des salaires, des travaux, de l'énergie et des assurances |
| Capital affecté au départ | **120 M€**, soit environ 94 fois le besoin annuel et environ 34 fois le prix d'achat retenu (3,5 M€). Investi en actifs diversifiés ; rendement réel net de 2 % (ESTIMATION) |
| Dividendes de transition | **1 M€ net par an pendant 10 ans**, versés par une holding d'au moins 5 PME sans dette, soit environ 2,8 M€ d'EBITDA |
| Réserve de trésorerie | **1,5 M€** (environ 1,2 an de charges), reconstituée après usage et indexée sur les charges |
| Fonds de travaux | Provision versée chaque année (346 → 399 k€) ; campagnes de 1,40 à 1,58 M€ tous les 4 ans |
| Activités sur place | Socle calme : logements dans les communs, hivernage, bail solaire, forêt, pension de retraite au pré, tournages. Environ 141 k€ HT de chiffre d'affaires, 71 k€ de contribution et 43 k€ disponibles après impôts |
| Règle de dépense | Retrait annuel plafonné à 80 % du plafond précédent + 20 % × 1,75 % du capital |
| Règles de tension | Si la réserve passe sous un an de charges : −10 % de dépenses discrétionnaires, report de 30 % de la campagne et retrait d'urgence plafonné à 4 %. La réserve est ensuite reconstituée |

**Résultats du modèle.**
- **Cas central** :
  - aucune année de déficit ;
  - le capital passe de 120 M€ à **158 M€** en euros constants en année 20 ;
  - la capacité de financement (activités et plafond de retrait) dépasse les charges de 65 à 88 % selon les années.
- **Sept stress tests** : aucun déficit sur 20 ans. Dans le pire cas, le cumul des chocs, le capital finit à 112 M€ (L6, § 3).
- **Simulation sur 30 ans avec des chocs tirés au hasard** : 1,8 % d'échec avant 20 ans et environ 5 % avant 30 ans. Le critère n° 6 du cadre analytique est respecté (L6, § 4).

**Les quatre conditions sans lesquelles la solution ne tient pas :**
1. **Un budget validé sur le bien réel.** Si le besoin réel se situe au haut de la fourchette de L1, le risque d'échec passe à 11 % sur 20 ans et à 22 % sur 30 ans (L6, § 4.2).
2. **La discipline de dépense**, écrite et contrôlée par au moins une personne indépendante. Sans elle, le risque à 30 ans passe de 5 % à 16 %.
3. **Une transmission organisée.** Sans montage, un décès en année 15, et les droits de succession qui en découlent (environ 44 % du capital), fait passer le risque à 30 ans à 16 %.
4. **Un capital réellement constitué** avant d'engager le niveau de dépense complet (§ 6).

---

## 2. Architecture : qui détient quoi, qui paie quoi

Cette architecture reprend les recommandations de R3 (questions 1, 7 et 9) et les constats de l'équipe rouge (V2R C1, M5 et M6). **Elle est à valider par un avocat fiscaliste et un notaire.**

```
                    ┌─────────────────────────────────────────┐
                    │  Propriétaire (26 ans)                  │
                    └──────┬───────────────┬──────────────────┘
                           │               │
         ┌─────────────────▼──┐     ┌──────▼──────────────────────────┐
         │ SCI familiale à    │     │ Holding opérationnelle          │
         │ l'impôt sur le     │     │ (≥ 5 PME sans dette, dirigeants │
         │ revenu : château,  │     │ salariés)                       │
         │ parc, partie privée│     └──────┬──────────────────────────┘
         └───▲────────▲───────┘            │ dividendes de transition (10 ans),
             │        │                    │ puis conversion en capital
   loyer de  │        │ retraits plafonnés │
   marché    │        │ (règle de dépense) ▼
 ┌───────────┴──┐   ┌─┴──────────────────────────────────────────┐
 │ Société      │   │ Capital affecté au domaine                 │
 │ d'exploitation│  │ (patrimoine du propriétaire ; portefeuille │
 │ (pension     │   │ diversifié ; statuts contraignants ou      │
 │ retraite,    │   │ fiducie à étudier ; ni château ni chevaux) │
 │ hivernage…)  │   └────────────────────────────────────────────┘
 └──────────────┘
```

| Entité | Rôle | Points à valider |
|---|---|---|
| **SCI familiale à l'impôt sur le revenu** (ou détention directe) | Détient le château, le parc et la partie privée. Garde l'accès au régime fiscal des monuments historiques, qui n'est ouvert qu'en détention directe ou en SCI familiale [R3-04] [R3-06] | Recettes commerciales sous 10 % de son chiffre d'affaires, sinon IS [R3-59] ; engagement de conservation de 15 ans si le régime MH est utilisé [R3-06] |
| **Société d'exploitation** (par exemple une SAS) | Exploite les activités et paie un loyer de marché à la SCI | Logement gratuit dans une société à l'IS = acte anormal de gestion [R3-56] ; contrats de pension non requalifiables en bail rural (R3, question 7) |
| **Holding opérationnelle** | Détient les PME qui versent les dividendes de transition | Ne jamais y loger le château habité ni les chevaux personnels : taxe de 20 % sur les holdings patrimoniales [R3-18], dont l'assiette a changé en cours de vote [V2R-11] [V2R-12] |
| **Capital affecté** | Portefeuille diversifié réservé au domaine ; retraits annuels plafonnés | **Reste la fortune du propriétaire** (L2, § 6.3). Véhicule à choisir : compte-titres ou contrat de capitalisation sous charte, société civile avec un gérant indépendant, fiducie à expertiser. Sa fiscalité détermine le rendement net (2 % retenu). Le fonds de dotation ne convient pas (apport irrévocable, intérêt général) [V2R-02] [R8-45] |
| **Comité du domaine** | Fait respecter la charte : règle de dépense, réserve, fonds de travaux, règles de tension | Au moins une personne indépendante. Composition et pouvoirs écrits dans les statuts ou dans un pacte |
| **Notaire de la famille** | Transmission et régime matrimonial | Sans montage, environ 44 % du capital part en droits de succession à chaque génération [V2R-06] ; en communauté, les revenus réinvestis deviennent communs [V2R-07] |

**Les impôts.**
- Les contributions des activités qui paient des coûts privés perdent environ 40 % en impôts dans le modèle : de 25 à 54 % selon la structure (L2, § 1).
- Le rendement du capital est déjà compté **net** d'impôt et de frais : 2 % réel, pour un retrait de 1,75 %.
- Une structure qui ferait perdre davantage réduirait ce rendement. Pour S2, un demi-point de rendement en moins ajoute 20 à 28 % au capital nécessaire (L6, § 4.3).

---

## 3. La charte du domaine : les règles de fonctionnement

| Règle | Contenu | Pourquoi | Dans le modèle ? |
|---|---|---|---|
| **Règle de dépense** | Retrait annuel au plus égal au plafond lissé : 80 % du plafond précédent + 20 % × 1,75 % du capital | Lisser les chocs de marché, ne pas manger le capital | Oui |
| **Réserve de trésorerie** | Au moins un an de charges (1,5 M€ en S2), indexée sur les charges et reconstituée après usage ; placée hors des contrats d'assurance, dont les rachats peuvent être gelés en crise [V2R-10] | Absorber une mauvaise année sans vendre au pire moment | Oui (reconstitution et indexation) |
| **Fonds de travaux** | Provision versée chaque année, même en tension ; campagnes tous les 4 ans ; sinistres non assurés payés en plus, sans annuler de travaux | Ne jamais créer de retard d'entretien caché | Oui (après correction V2R M1) |
| **Règles de tension** | Si la réserve passe sous un an de charges : −10 % de dépenses discrétionnaires, report de 30 % de la campagne (qui reste dû), retrait d'urgence plafonné à 4 % | Sans ces règles, le risque d'échec à 30 ans passe de 5 % à 16 % (L6) | Oui |
| **Règle de conversion** | Les dividendes non dépensés et tout produit de cession d'entreprise ou de bâtiment vont au capital affecté | Transformer des revenus fragiles en capital durable | Partiellement (excédents versés au capital) |
| **Seuil de déclenchement** | N'engager le niveau de dépense complet que si le capital, avec sa règle, couvre le besoin net des activités, réserve constituée | Ne pas entretenir un domaine au-dessus de ses moyens | Non (condition de départ) |
| **Règle de l'excédent** | Si le capital dépasse durablement le niveau requis (par exemple 1,5 fois), l'excédent peut financer une restauration exceptionnelle | Le cas central accumule une marge (§ 4) ; elle doit d'abord protéger contre les mauvais scénarios | Non (proposition) |
| **Politique de placement** | Portefeuille diversifié, majoritairement en actions, à faibles frais ; pas d'immobilier soumis à l'IFI ; pas de concentration sur une entreprise | Viser 2 % réel net sur longue période | Hypothèse de rendement |
| **Transmission et régime matrimonial** | Montage successoral (démembrement, assurance-vie, donation-partage) et contrat de mariage, à établir avec un notaire | Sans eux, le capital perd environ 44 % par génération ; un divorce peut partager la part réinvestie | Test « décès en année 15 » seulement |
| **Pas de bruit en réponse à une crise** | Une année difficile se traite par la dépense, jamais par l'ouverture à des réceptions ou au public | Protéger la tranquillité ; ces revenus disparaissent d'ailleurs en crise (−80 %) | Oui (aucune activité ajoutée en tension) |

---

## 4. Projection sur 20 ans (cas central)

### 4.1 Année par année (k€, euros constants 2026)

| Année | Charges du domaine | dont provision de gros entretien | Travaux payés par le fonds de travaux | Activités (disponible) | Dividendes | Retrait sur le capital | Plafond de retrait | Capital (fin d'année) | Fonds de travaux (fin d'année) | Réserve |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 280 | 346 | 0 | 17 | 1 000 | 270 | 2 100 | 121 030 | 346 | 1 500 |
| 2 | 1 286 | 349 | 0 | 32 | 1 000 | 269 | 2 104 | 123 181 | 695 | 1 508 |
| 3 | 1 293 | 351 | 0 | 43 | 1 000 | 265 | 2 114 | 125 379 | 1 046 | 1 515 |
| 4 | 1 299 | 354 | 1 400 | 43 | 1 000 | 272 | 2 130 | 127 615 | 0 | 1 523 |
| 5 | 1 306 | 357 | 0 | 43 | 1 000 | 279 | 2 151 | 129 888 | 357 | 1 531 |
| 6 | 1 313 | 359 | 0 | 43 | 1 000 | 286 | 2 175 | 132 200 | 716 | 1 539 |
| 7 | 1 320 | 362 | 0 | 43 | 1 000 | 293 | 2 203 | 134 551 | 1 078 | 1 547 |
| 8 | 1 327 | 365 | 1 443 | 43 | 1 000 | 300 | 2 233 | 136 942 | 0 | 1 555 |
| 9 | 1 334 | 368 | 0 | 43 | 1 000 | 307 | 2 266 | 139 373 | 368 | 1 563 |
| 10 | 1 341 | 370 | 0 | 43 | 1 000 | 314 | 2 300 | 141 846 | 738 | 1 571 |
| 11 | 1 348 | 373 | 0 | 43 | 0 | 1 322 | 2 337 | 143 362 | 1 111 | 1 580 |
| 12 | 1 355 | 376 | 1 487 | 43 | 0 | 1 329 | 2 371 | 144 900 | 0 | 1 588 |
| 13 | 1 363 | 379 | 0 | 43 | 0 | 1 337 | 2 404 | 146 461 | 379 | 1 597 |
| 14 | 1 370 | 382 | 0 | 43 | 0 | 1 344 | 2 436 | 148 046 | 760 | 1 605 |
| 15 | 1 377 | 384 | 0 | 43 | 0 | 1 352 | 2 467 | 149 656 | 1 145 | 1 614 |
| 16 | 1 385 | 387 | 1 532 | 43 | 0 | 1 359 | 2 497 | 151 289 | 0 | 1 623 |
| 17 | 1 393 | 390 | 0 | 43 | 0 | 1 367 | 2 527 | 152 948 | 390 | 1 632 |
| 18 | 1 400 | 393 | 0 | 43 | 0 | 1 375 | 2 557 | 154 632 | 783 | 1 641 |
| 19 | 1 408 | 396 | 0 | 43 | 0 | 1 383 | 2 587 | 156 342 | 1 179 | 1 650 |
| 20 | 1 416 | 399 | 1 578 | 43 | 0 | 1 391 | 2 617 | 158 078 | 0 | 1 659 |

Notes :
- Les charges du domaine comprennent la provision de gros entretien (aléas et maîtrise d'œuvre compris), versée au fonds de travaux. Les travaux sont ensuite payés par ce fonds, tous les 4 ans.
- L'année 1, l'investissement des activités (1,1 M€ : logements et hivernage) est prélevé sur le capital.
- Les activités montent en charge : 40 % de leur régime l'année 1, 75 % l'année 2.
- Le retrait couvre ce qui manque après les activités et les dividendes, puis maintient la réserve à sa cible. Celle-ci est indexée sur les charges, et la trésorerie rapporte −0,5 % réel par an. Le solde net de l'année est donc légèrement positif, et la réserve monte de 1,5 à 1,66 M€.

### 4.2 Sur 20 ans : d'où vient l'argent, où va-t-il ?

| Emplois (20 ans) | M€ | Ressources (20 ans) | M€ |
|---|---:|---|---:|
| Charges courantes (personnel, énergie, assurances, entretien courant, jardins, chevaux, taxes, administration, imprévus, investissements futurs) | 19,47 | Activités sur place (disponible après impôts) | 0,81 (3,0 %) |
| Provision de gros entretien, entièrement dépensée en 5 campagnes | 7,44 | Dividendes de transition | 10,00 (36,7 %) |
| Hausse de la réserve et rendement négatif de la trésorerie | 0,32 | Retraits sur le capital affecté | 16,42 (60,3 %) |
| **Total des emplois** | **27,23** | **Total des ressources** | **27,23** |

Pendant ce temps, le capital affecté :
- part de 120 M€ ;
- gagne 55,6 M€ de rendement réel ;
- verse 16,4 M€ au domaine ;
- finance l'investissement initial des activités (1,1 M€) ;
- finit à **158,1 M€** en euros constants.

**Pourquoi le capital grossit-il dans le cas central ?** Parce qu'il est dimensionné pour les mauvais scénarios, pas pour le cas moyen.
- Dans le cumul des chocs, il finit à 112 M€.
- Dans 5 % des trajectoires simulées, il tombe sous 49 M€ en année 20 (L6, § 4.1).

La marge du cas central est le prix de la sécurité. La règle de l'excédent (§ 3) permet de l'utiliser **après coup**, quand elle est acquise, jamais par anticipation.

### 4.3 Chiffre d'affaires, résultat, trésorerie : trois lectures d'une même année

Le brief demande de distinguer ces trois notions. Exemple de l'année 5 (régime de croisière) et de l'année 8 (année de campagne de travaux) :

| Lecture | Année 5 | Année 8 (campagne) | Commentaire |
|---|---:|---:|---|
| **Chiffre d'affaires des activités** (HT) | ≈ 141 k€ | ≈ 141 k€ | Pension de retraite 56 k€, logements 55 k€, bail solaire 15 k€, tournages 7 k€, hivernage 6 k€, forêt (revenu net) 2 k€ |
| **Résultat des activités** (contribution avant impôt) | 71 k€ | 71 k€ | Environ la moitié du chiffre d'affaires ; 43 k€ restent disponibles après une fuite fiscale de 40 % |
| **Résultat économique du domaine** (activités disponibles − charges, provision comprise) | −1 263 k€ | −1 284 k€ | Le domaine est structurellement déficitaire : c'est le capital qui le finance |
| **Trésorerie décaissée par le domaine** (charges courantes + travaux de l'année) | 949 k€ + 0 | 962 k€ + 1 443 k€ | Les travaux ne sortent qu'une année sur quatre ; d'où le fonds de travaux distinct |
| **Financement** | dividendes 1 000 k€ + retrait 279 k€ | dividendes 1 000 k€ + retrait 300 k€ | Le retrait reste très en dessous du plafond (2 151 k€ et 2 233 k€) |

Le chiffre d'affaires des activités est calculé à partir de la feuille Moteurs : pension de retraite 56,0 k€, logements 54,7 k€, hivernage 6,0 k€, bail solaire 15,0 k€, tournages 7,0 k€.

### 4.4 Revenus récurrents et occasionnels

Sur 20 ans, les ressources du domaine (contributions brutes des activités, dividendes et retraits) totalisent 27,8 M€. Elles se répartissent ainsi :

| Classe | Ressource | Part |
|---|---|---:|
| A — contractuel | Logements, hivernage, bail solaire, forêt (1,05 M€ bruts) | ≈ 4 % |
| B — récurrent | Pension de retraite au pré (0,19 M€ bruts) | < 1 % |
| C — occasionnel | Tournages (0,11 M€ bruts) | < 0,5 % |
| D — financier et extérieur | Dividendes (10 M€) et retraits sur le capital (16,4 M€) | ≈ 95 % |

Le principe de robustesse de L2 (§ 1) est respecté : les charges fixes sont couvertes par les classes A et D. Les revenus occasionnels ne financent rien d'indispensable.

---

## 5. Résistance de la solution (résumé de L6)

| Épreuve | Résultat |
|---|---|
| Activités −30 % | Aucun déficit ; capital en année 20 : 157,8 M€ |
| Crise de type 2020 en année 5 | Aucun déficit ; le capital tombe à 97,5 M€ en année 5, puis remonte à 114,5 M€ en année 20 |
| Sinistre non assuré de 600 k€ et campagnes +30 % | Aucun déficit ; capital en année 20 : 154,7 M€ |
| Énergie ×2 pendant 3 ans | Aucun déficit ; capital en année 20 : 157,8 M€ |
| Salaires +1,5 % réel par an | Aucun déficit ; capital en année 20 : 156,9 M€ |
| Entreprises défaillantes dès l'année 3 et rendement de 1 % | Aucun déficit ; le capital stagne autour de 119 M€ |
| Cumul des chocs | Aucun déficit ; le capital finit à 112,2 M€ ; marge réduite à 28 % |
| Monte-Carlo, 20 000 trajectoires | Échec : 1,8 % avant 20 ans, environ 5 % avant 30 ans ; 20 % des trajectoires connaissent au moins une année de tension |
| Décennie perdue (rendement nul pendant 10 ans) | Échec à 30 ans : 8,6 % |
| Décès en année 15, droits de succession de 44 % | Échec à 30 ans : 15,9 % |

---

## 6. Avant l'année 1 : constituer le capital

La projection commence **une fois le capital réuni**. C'est la partie la plus difficile, et le modèle ne peut pas la résoudre à la place du propriétaire. Il peut en revanche en donner les ordres de grandeur.

### 6.1 Ce qu'il faut réunir (S2)

- **120 M€ de capital** et une holding capable de verser 1 M€ net par an pendant 10 ans, soit environ 2,8 M€ d'EBITDA. C'est le dimensionnement de la solution : environ 5 % d'échec sur 30 ans.
- Ou **85,8 M€** avec la même holding, si l'on se contente de 95 % de chances de tenir 20 ans. Le risque à 30 ans monte alors à environ 13 % (entre 14,9 % à 80 M€ et 8,6 % à 100 M€) : le critère du cadre n'est plus respecté.
- Ou **132,2 M€ de capital seul**, sans entreprise, pour 95 % de chances de tenir 30 ans (L3).
- À comparer au prix d'achat retenu pour S2 : 3,5 M€ (HYPOTHÈSE de L1). Le capital de fonctionnement vaut environ **34 fois** le prix d'achat.

### 6.2 Combien de temps pour le constituer ? (calcul illustratif)

Pour accumuler 120 M€ en épargnant chaque année un montant constant, placé à 2 % réel net :

| Épargne nette versée au capital chaque année | Années nécessaires pour atteindre 120 M€ |
|---:|---:|
| 1 M€ | environ 62 ans |
| 2,5 M€ | environ 34 ans |
| 5 M€ | environ 20 ans |
| 10 M€ | environ 11 ans |

Calcul : nombre d'années n tel que versement × ((1,02ⁿ − 1) ÷ 0,02) = 120 M€. C'est une ESTIMATION arithmétique, sans les chocs de marché.

**Lecture.**
- Hors héritage ou cession d'entreprise, la constitution prend des décennies : le seuil de déclenchement serait atteint vers 50 ou 60 ans, ou jamais (V2R M7).
- La cession d'entreprises raccourcit fortement ces délais. Une entreprise de 2,8 M€ d'EBITDA vaut environ 14 à 22 M€ à 5 à 8 fois l'EBITDA (ESTIMATION [R8-35]), avant impôt sur la plus-value.
- Pour S1, il faut 34 M€ : environ 26 ans d'épargne à 1 M€ par an, ou 12 ans à 2,5 M€ par an.

### 6.3 Trois façons de concilier le calendrier et le domaine

1. **Acheter le domaine que le capital peut entretenir aujourd'hui** (L3, modèle 3) : par exemple un S1, qui demande 34 M€ de capital et 0,4 M€ de dividendes pendant 10 ans, puis changer d'échelle plus tard.
2. **Acheter le domaine visé plus tard**, une fois le capital constitué. Le seuil de déclenchement le garantit.
3. **Amorcer le capital par une vente partielle** (L3, modèle 5), si le domaine compte des bâtiments sans usage pour le propriétaire.

À éviter : acheter un S2 et l'entretenir au niveau d'un S1 en attendant. Le retard d'entretien qui s'accumulerait est précisément ce que montrent les cas réels : environ 2 M£ par maison historique britannique [R1-05].

---

## 7. Variantes S1 et S3

| | S1 — domaine relativement économique | S3 — domaine historique ultra-premium |
|---|---|---|
| Besoin annuel (année 1 → année 20) | 0,35 → 0,39 M€ | 3,79 → 4,22 M€ |
| Capital affecté au départ | 34 M€ (≈ 98 fois le besoin) | 480 M€ (≈ 127 fois le besoin) |
| Dividendes de transition | 0,4 M€ par an pendant 10 ans | aucun |
| Réserve | 0,4 M€ | 4 M€ |
| Capital en année 20 (cas central) | 46,8 M€ | 614,1 M€ |
| Pire stress test | Cumul : capital à 33,1 M€ en année 20, aucun déficit, mais un retrait qui atteint 95 % du plafond l'année du sinistre de 600 k€ | Non testé ; même niveau de risque simulé que S1 et S2 |
| Échec simulé avant 20 / 30 ans | 1,8 % / environ 5 % | 2,5 % / environ 5 % |
| Sur 20 ans : activités / dividendes / retraits | 0,25 / 4,0 / 3,7 M€, plus 0,5 M€ d'excédents de dividendes versés au capital | 1,5 / 0 / 79,3 M€ |
| Option propre au scénario | Peu d'activités possibles ; pas de locataire d'ancrage (moins de 40 chambres) | Locataire d'ancrage possible si la localisation s'y prête : environ −5 % de capital nécessaire (L3, modèle 4) |

Pour S1, les dividendes de transition (0,4 M€) dépassent le besoin pendant 10 ans. L'excédent est versé au capital, qui grossit plus vite.

S3 demande un multiple plus élevé. Dans le modèle, la taille d'un sinistre non assuré est proportionnelle au gros entretien, qui pèse davantage dans le budget d'un grand monument classé.

---

## 8. Ce qui reste à valider avant tout engagement

| Point | Pourquoi c'est décisif | Qui peut le valider |
|---|---|---|
| Budget du bien réel (gros entretien, valeur de reconstruction, personnel, maîtrise d'œuvre, infrastructures) | C'est le premier facteur de risque : le haut de la fourchette multiplie le risque d'échec à 30 ans par plus de 4 | Architecte du patrimoine, assureur, régisseur ; un an d'exploitation réelle |
| Rendement réel net du capital et véhicule | 2 % retenu (1,5 à 2,5 %) ; un demi-point de moins ajoute 20 à 28 % au capital nécessaire | Avocat fiscaliste, conseiller en investissement indépendant |
| Affectation réelle du capital (statuts contraignants, fiducie) | Sans elle, la discipline ne repose que sur la volonté du propriétaire | Notaire, avocat |
| Transmission et régime matrimonial | Environ 44 % de droits par génération sans montage ; un divorce peut partager la part réinvestie | Notaire |
| Structure de détention (SCI, SAS, holding) et régime MH | Accès à la déduction, taxe sur les holdings, IFI, bail rural | Avocat fiscaliste, notaire, expert-comptable |
| Gouvernance (charte, comité) | Sans discipline, le risque à 30 ans passe de 5 % à 16 % ; le propriétaire a 26 ans | Notaire, avocat |
| Activités du socle : PLU, ABF, bail rural, performance énergétique des logements | Conditions de chaque revenu | Mairie, ABF, avocat |

La feuille de route (L7) organise ces validations dans le temps.
