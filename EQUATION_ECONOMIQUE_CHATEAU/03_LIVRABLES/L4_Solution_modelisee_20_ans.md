# L4 — La meilleure solution, modélisée sur 20 ans (domaine S2)

> **Statut de ce document**
> - Modèle complet de la solution retenue (L3, modèles 1 et 3, avec le socle d'activités calmes), en euros constants 2026.
> - Tous les chiffres viennent de la feuille `Proj_S2_solution` du classeur `02_MODELE/sorties/Modele_equation_chateau.xlsx`. Chaque cellule y est une formule, vérifiée par un calcul Python indépendant, et reproduite à l'identique par la simulation de Monte-Carlo sans chocs.
> - Les variantes S1 et S3 sont dans les feuilles `Proj_S1_solution` et `Proj_S3_solution`.
> - **Les montages juridiques et fiscaux décrits ici sont des pistes à faire valider** par un avocat fiscaliste, un notaire et un expert-comptable. Ils ne constituent pas un conseil juridique.

---

## 1. La solution en une page

**Le principe.** Le domaine ne vit pas de ses activités. Il vit d'un **fonds d'entretien** : un capital diversifié, séparé du patrimoine personnel, affecté au domaine et gouverné par des règles écrites. Pendant 10 ans, des **dividendes d'entreprises** complètent le fonds et laissent le capital grandir. Un **socle d'activités calmes** occupe et entretient les dépendances sans troubler la vie privée.

| Élément | Domaine S2 (central) |
|---|---|
| Besoin annuel du domaine | 1,25 M€ l'année 1, puis 1,38 M€ en année 20 avec les dérives réelles (salaires, travaux, énergie, assurances) |
| Fonds d'entretien au départ | **60 M€**, investi en actifs diversifiés, rendement réel net de 3 % (ESTIMATION) |
| Dividendes de transition | **1 M€ net par an pendant 10 ans**, versés par une holding d'au moins 5 PME sans dette (environ 2,5 M€ d'EBITDA) |
| Réserve de trésorerie | **1,5 M€**, soit environ 1,2 an de besoin |
| Fonds de travaux | Provision versée chaque année (313 → 361 k€) ; campagnes de 1,27 à 1,43 M€ tous les 4 ans |
| Activités sur place | Socle calme : logements, hivernage, bail solaire, forêt, pensions, tournages. Chiffre d'affaires d'environ 254 k€ HT par an, contribution de 70 k€, 49 k€ disponibles après impôts |
| Règle de dépense | Retrait annuel plafonné : 80 % du plafond précédent + 20 % × 2,75 % du fonds |
| Règles de tension | Si la réserve passe sous un an de besoin : −10 % de dépenses discrétionnaires, report de 30 % de la campagne, retrait d'urgence plafonné à 4 % |

**Résultats (modèle).**
- **Cas central** :
  - aucune année de déficit ;
  - le fonds passe de 60 M€ à **88 M€** en euros constants en année 20 ;
  - la capacité de financement (activités et plafond de retrait du fonds) dépasse les charges de 34 à 67 % selon les années.
- **Huit stress tests** : aucun déficit sur 20 ans. Dans le pire cas (cumul des chocs), le fonds finit à 60 M€ (L6, § 3).
- **Simulation sur 30 ans, avec des chocs tirés au hasard** : 4,3 % d'échec avant 20 ans et 11,1 % avant 30 ans (L6, § 4).

**Les trois conditions sans lesquelles la solution ne tient pas :**
1. **Un budget validé sur le bien réel.** Si le besoin réel se situe au haut de la fourchette de L1, le risque d'échec passe à 30 % sur 20 ans (L6, § 4.2).
2. **La discipline de dépense**, écrite et contrôlée par au moins une personne indépendante. Sans elle, le risque double.
3. **Un capital réellement constitué** avant d'engager le niveau de dépense complet (§ 6).

---

## 2. Architecture : qui détient quoi, qui paie quoi

Cette architecture reprend les recommandations de R3 (questions 1, 7 et 9). **Elle est à valider par un avocat fiscaliste et un notaire.**

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
             │        │                    │ puis conversion en fonds
   loyer de  │        │ retraits plafonnés │
   marché    │        │ (règle de dépense) ▼
 ┌───────────┴──┐   ┌─┴──────────────────────────────────────┐
 │ Société      │   │ Fonds d'entretien affecté au domaine   │
 │ d'exploitation│  │ (portefeuille diversifié ; véhicule à  │
 │ (pensions,   │   │ valider ; ni château ni chevaux dedans) │
 │ hivernage,   │   └────────────────────────────────────────┘
 │ tournages…)  │
 └──────────────┘
```

| Entité | Rôle | Points à valider |
|---|---|---|
| **SCI familiale à l'impôt sur le revenu** (ou détention directe) | Détient le château, le parc et la partie privée. Garde l'accès au régime fiscal des monuments historiques : la déduction n'est ouverte qu'en détention directe ou en SCI familiale [R3-04] [R3-06] | Ses recettes commerciales doivent rester sous 10 % de son chiffre d'affaires, sinon elle devient passible de l'IS [R3-59]. Engagement de conservation de 15 ans si le régime MH est utilisé [R3-06] |
| **Société d'exploitation** (par exemple une SAS) | Exploite les activités (pensions, hivernage, tournages) et paie un loyer de marché à la SCI | Un logement gratuit dans une société à l'IS est un acte anormal de gestion [R3-56]. Le bail des écuries peut être requalifié en bail rural (R3, question 7) |
| **Holding opérationnelle** | Détient les PME qui versent les dividendes de transition | Ne jamais y loger le château habité ni les chevaux personnels : taxe de 20 % sur les holdings patrimoniales (loi de finances 2026) [R3-18] |
| **Fonds d'entretien** | Capital diversifié affecté au domaine ; versements annuels plafonnés | **Véhicule et fiscalité à déterminer** : société à l'IS, société civile de portefeuille, contrat de capitalisation… Le rendement réel net de 3 % en dépend. Le fonds de dotation ne convient pas à une résidence privée (apport irrévocable, mission d'intérêt général) [R8-45] |
| **Comité du domaine** | Fait respecter la charte : règle de dépense, réserve, fonds de travaux, règles de tension | Composition (au moins une personne indépendante) et pouvoirs à écrire dans les statuts ou un pacte |

**La fuite fiscale.** Les contributions des activités qui paient des coûts privés perdent environ 30 % en impôts dans le modèle (de 15 à 49 % selon la structure, L2, § 1). Le rendement du fonds est déjà compté **net** d'impôt (3 % réel, retrait de 2,75 %). Une structure qui ferait perdre davantage réduirait le rendement net. L6 (§ 4.2) montre qu'un point de rendement en moins ajoute 7 à 8 points de risque à 30 ans.

---

## 3. La charte du domaine : les règles de fonctionnement

| Règle | Contenu | Pourquoi | Dans le modèle ? |
|---|---|---|---|
| **Règle de dépense** | Retrait annuel du fonds au plus égal au plafond lissé : 80 % du plafond précédent + 20 % × 2,75 % du fonds | Lisser les chocs de marché, ne pas manger le capital | Oui |
| **Réserve de trésorerie** | Au moins un an de besoin (1,5 M€ en S2), reconstituée chaque année | Absorber une mauvaise année sans vendre au pire moment | Oui |
| **Fonds de travaux** | Provision versée chaque année, même en tension ; campagnes tous les 4 ans | Ne jamais créer de retard d'entretien caché | Oui |
| **Règles de tension** | Si la réserve passe sous un an de besoin : −10 % de dépenses discrétionnaires, report de 30 % de la campagne (qui reste dû), retrait d'urgence plafonné à 4 % | Sans ces règles, le risque d'échec double (L6) | Oui |
| **Règle de conversion** | Les dividendes non dépensés et tout produit de cession d'entreprise ou de bâtiment vont au fonds | Transformer des revenus fragiles en capital durable | Partiellement (excédents versés au fonds) |
| **Seuil de déclenchement** | N'engager le niveau de dépense complet que si le fonds, avec sa règle, couvre le besoin net des activités, réserve constituée | Ne pas entretenir un domaine au-dessus de ses moyens | Non (condition de départ) |
| **Règle de l'excédent** | Si le fonds dépasse durablement le niveau requis (par exemple 1,5 fois), l'excédent peut financer une restauration exceptionnelle ou réduire les dividendes demandés aux entreprises | Le cas central accumule une marge (§ 4) ; elle doit rester disponible pour les mauvais scénarios | Non (proposition) |
| **Politique de placement** | Portefeuille diversifié, majoritairement en actions, à faibles frais ; pas d'immobilier soumis à l'IFI ; pas de concentration sur une entreprise | Viser 3 % réel net sur longue période | Hypothèse de rendement |
| **Pas de bruit en réponse à une crise** | Une année difficile se traite par la dépense, jamais par l'ouverture à des réceptions ou au public | Protéger la tranquillité ; ces revenus disparaissent d'ailleurs en crise (−80 %) | Oui (aucune activité ajoutée en tension) |

---

## 4. Projection sur 20 ans (cas central)

### 4.1 Année par année (k€, euros constants 2026)

| Année | Charges du domaine | dont provision de gros entretien | Travaux payés par le fonds de travaux | Activités (disponible) | Dividendes | Retrait sur le fonds | Plafond de retrait | Fonds d'entretien (fin d'année) | Fonds de travaux (fin d'année) | Réserve |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 246 | 313 | 0 | 20 | 1 000 | 226 | 1 650 | 60 474 | 313 | 1 500 |
| 2 | 1 252 | 316 | 0 | 37 | 1 000 | 215 | 1 653 | 62 073 | 629 | 1 500 |
| 3 | 1 258 | 318 | 0 | 49 | 1 000 | 209 | 1 663 | 63 726 | 948 | 1 500 |
| 4 | 1 265 | 321 | 1 268 | 49 | 1 000 | 216 | 1 681 | 65 423 | 0 | 1 500 |
| 5 | 1 271 | 323 | 0 | 49 | 1 000 | 222 | 1 705 | 67 163 | 323 | 1 500 |
| 6 | 1 278 | 325 | 0 | 49 | 1 000 | 229 | 1 733 | 68 950 | 648 | 1 500 |
| 7 | 1 284 | 328 | 0 | 49 | 1 000 | 235 | 1 766 | 70 783 | 976 | 1 500 |
| 8 | 1 291 | 330 | 1 307 | 49 | 1 000 | 242 | 1 802 | 72 665 | 0 | 1 500 |
| 9 | 1 298 | 333 | 0 | 49 | 1 000 | 249 | 1 841 | 74 596 | 333 | 1 500 |
| 10 | 1 305 | 335 | 0 | 49 | 1 000 | 255 | 1 883 | 76 578 | 668 | 1 500 |
| 11 | 1 311 | 338 | 0 | 49 | 0 | 1 262 | 1 928 | 77 613 | 1 006 | 1 500 |
| 12 | 1 318 | 340 | 1 346 | 49 | 0 | 1 269 | 1 969 | 78 672 | 0 | 1 500 |
| 13 | 1 326 | 343 | 0 | 49 | 0 | 1 276 | 2 008 | 79 756 | 343 | 1 500 |
| 14 | 1 333 | 345 | 0 | 49 | 0 | 1 284 | 2 045 | 80 865 | 688 | 1 500 |
| 15 | 1 340 | 348 | 0 | 49 | 0 | 1 291 | 2 081 | 82 001 | 1 036 | 1 500 |
| 16 | 1 347 | 351 | 1 387 | 49 | 0 | 1 298 | 2 116 | 83 163 | 0 | 1 500 |
| 17 | 1 354 | 353 | 0 | 49 | 0 | 1 305 | 2 150 | 84 352 | 353 | 1 500 |
| 18 | 1 362 | 356 | 0 | 49 | 0 | 1 313 | 2 184 | 85 570 | 709 | 1 500 |
| 19 | 1 369 | 359 | 0 | 49 | 0 | 1 320 | 2 218 | 86 817 | 1 068 | 1 500 |
| 20 | 1 377 | 361 | 1 429 | 49 | 0 | 1 328 | 2 252 | 88 093 | 0 | 1 500 |

Notes :
- Les charges du domaine comprennent la provision de gros entretien versée au fonds de travaux. Les travaux sont ensuite payés par ce fonds, tous les 4 ans.
- L'année 1, l'investissement des activités (1,1 M€ : logements et hivernage) est prélevé sur le capital du fonds.
- Les activités montent en charge : 40 % de leur régime l'année 1 et 75 % l'année 2.
- Chaque année, charges − activités = dividendes + retrait. Le solde de trésorerie est nul et la réserve reste à 1,5 M€.

### 4.2 Sur 20 ans : d'où vient l'argent, où va-t-il ?

| Emplois (20 ans) | M€ | Ressources (20 ans) | M€ |
|---|---:|---|---:|
| Charges courantes (personnel, énergie, assurances, entretien courant, jardins, chevaux, taxes, administration, imprévus, investissements futurs) | 19,45 | Activités sur place (disponible après impôts) | 0,94 (3,6 %) |
| Provision de gros entretien, entièrement dépensée en 5 campagnes | 6,74 | Dividendes de transition | 10,00 (38,2 %) |
| **Total des charges** | **26,18** | Retraits sur le fonds d'entretien | 15,24 (58,2 %) |
| | | **Total** | **26,18** |

Pendant ce temps, le fonds d'entretien :
- part de 60 M€ ;
- gagne 44,4 M€ de rendement réel ;
- verse 15,2 M€ au domaine ;
- finance l'investissement initial des activités (1,1 M€) ;
- finit à **88,1 M€** en euros constants.

**Pourquoi le fonds grossit-il dans le cas central ?** Parce qu'il est dimensionné pour les mauvais scénarios, pas pour le cas moyen. Dans le cumul des chocs, il finit à 60 M€. Dans 5 % des trajectoires simulées, il tombe sous 25 M€ en année 20 (L6, § 4.1). La marge du cas central est le prix de la sécurité. La règle de l'excédent (§ 3) permet de l'utiliser **après coup**, quand elle est acquise, jamais par anticipation.

### 4.3 Chiffre d'affaires, résultat, trésorerie : trois lectures d'une même année

Le brief demande de distinguer ces trois notions. Exemple de l'année 5 (régime de croisière) et de l'année 8 (année de campagne de travaux) :

| Lecture | Année 5 | Année 8 (campagne) | Commentaire |
|---|---:|---:|---|
| **Chiffre d'affaires des activités** (HT) | ≈ 254 k€ | ≈ 254 k€ | Pensions 169 k€, logements 55 k€, bail solaire 15 k€, tournages 7 k€, hivernage 6 k€, forêt (revenu net) 2 k€ |
| **Résultat des activités** (contribution avant impôt) | 70 k€ | 70 k€ | Marge d'environ 28 % : les pensions dégagent peu une fois le travail payé |
| **Résultat économique du domaine** (activités disponibles − charges, provision comprise) | −1 222 k€ | −1 242 k€ | Le domaine est structurellement déficitaire : c'est le fonds qui le finance |
| **Trésorerie décaissée par le domaine** (charges courantes + travaux de l'année) | 948 k€ + 0 | 961 k€ + 1 307 k€ | Les travaux ne sortent qu'une année sur quatre ; d'où le fonds de travaux distinct |
| **Financement** | dividendes 1 000 k€ + retrait 222 k€ | dividendes 1 000 k€ + retrait 242 k€ | Le retrait reste très en dessous du plafond (1 705 k€ et 1 802 k€) |

Le chiffre d'affaires des activités est calculé à partir de la feuille Moteurs : pension standard 112,6 k€, pension retraite 56,0 k€, logements 54,7 k€, hivernage 6,0 k€, bail solaire 15,0 k€, tournages 7,0 k€.

### 4.4 Revenus récurrents et occasionnels

Sur 20 ans, les ressources du domaine (contributions brutes des activités, dividendes et retraits : 26,6 M€) se répartissent ainsi :

| Classe | Ressource | Part |
|---|---|---:|
| A — contractuel | Logements, hivernage, bail solaire, forêt (1,05 M€ bruts) | ≈ 4 % |
| B — récurrent | Pensions (0,18 M€ bruts) | < 1 % |
| C — occasionnel | Tournages (0,11 M€ bruts) | < 0,5 % |
| D — financier et extérieur | Dividendes (10 M€) et retraits sur le fonds (15,2 M€) | ≈ 95 % |

Le principe de robustesse de L2 (§ 1) est respecté : les charges fixes sont couvertes par les classes A et D. Les revenus occasionnels ne financent rien d'indispensable.

---

## 5. Résistance de la solution (résumé de L6)

| Épreuve | Résultat |
|---|---|
| Activités −30 % | Aucun déficit ; fonds en année 20 : 87,7 M€ |
| Crise de type 2020 en année 5 | Aucun déficit ; le fonds perd 15 M€ dans l'année puis remonte à 61,8 M€ en année 20 |
| Sinistre non assuré de 600 k€ et campagnes +30 % | Aucun déficit ; fonds en année 20 : 85,8 M€ |
| Énergie ×2 pendant 3 ans | Aucun déficit ; fonds en année 20 : 87,8 M€ |
| Salaires +1,5 % réel par an | Aucun déficit ; fonds en année 20 : 86,9 M€ |
| Entreprises défaillantes dès l'année 3 et rendement de 2 % | Aucun déficit ; le fonds stagne à 60 M€ |
| Cumul des chocs | Aucun déficit ; le fonds revient à 60,3 M€ en année 20 ; marge réduite à 12 % |
| Monte-Carlo, 20 000 trajectoires | Échec : 4,3 % avant 20 ans, 11,1 % avant 30 ans ; 25 % des trajectoires connaissent au moins une année de tension |

---

## 6. Avant l'année 1 : constituer le capital

La projection commence **une fois le capital réuni**. C'est la partie la plus difficile, et le modèle ne peut pas la résoudre à la place du propriétaire. Il peut en revanche en donner les ordres de grandeur.

### 6.1 Ce qu'il faut réunir (S2)

- **60 M€ de fonds** et une holding capable de verser 1 M€ net par an pendant 10 ans, soit environ 2,5 M€ d'EBITDA. Cela donne 95 % de chances de tenir 20 ans.
- Ou bien **74,6 M€ de fonds** avec la même holding, pour 95 % de chances de tenir 30 ans.
- Ou bien **85,5 M€ de fonds seul**, sans entreprise, pour 95 % de chances de tenir 30 ans (L3).
- À comparer au prix d'achat retenu pour S2 : 3,5 M€ (HYPOTHÈSE de L1). Le capital de fonctionnement vaut environ **20 fois** le prix d'achat.

### 6.2 Combien de temps pour le constituer ? (calcul illustratif)

Pour accumuler 60 M€ en épargnant chaque année un montant constant, placé à 3 % réel :

| Épargne nette versée au fonds chaque année | Années nécessaires pour atteindre 60 M€ |
|---:|---:|
| 1 M€ | environ 35 ans |
| 2,5 M€ | environ 18 ans |
| 5 M€ | environ 10 ans |

Calcul : nombre d'années n tel que versement × ((1,03ⁿ − 1) ÷ 0,03) = 60 M€. C'est une ESTIMATION arithmétique, sans les chocs de marché.

La cession d'entreprises raccourcit fortement ces délais. Une entreprise de 2,5 M€ d'EBITDA vaut environ 13 à 20 M€ à 5 à 8 fois l'EBITDA (ESTIMATION [R8-35]), avant impôt sur la plus-value.

### 6.3 Trois façons de concilier le calendrier et le domaine

1. **Acheter le domaine que le capital peut entretenir aujourd'hui** (L3, modèle 3) : par exemple un S1, qui demande 15 M€ de fonds et 0,4 M€ de dividendes, puis changer d'échelle plus tard.
2. **Acheter le domaine visé plus tard**, une fois le fonds constitué. Le seuil de déclenchement le garantit.
3. **Amorcer le fonds par une vente partielle** (L3, modèle 5), si le domaine compte des bâtiments sans usage pour le propriétaire.

À éviter : acheter un S2 et l'entretenir au niveau d'un S1 en attendant. Le retard d'entretien qui s'accumulerait est précisément ce que les cas réels montrent : environ 2 M£ par maison historique britannique [R1-05].

---

## 7. Variantes S1 et S3

| | S1 — domaine relativement économique | S3 — domaine historique ultra-premium |
|---|---|---|
| Besoin annuel (année 1 → année 20) | 0,33 → 0,36 M€ | 3,66 → 4,07 M€ |
| Fonds d'entretien au départ | 15 M€ | 210 M€ |
| Dividendes de transition | 0,4 M€ par an pendant 10 ans | aucun |
| Réserve | 0,4 M€ | 4 M€ |
| Fonds en année 20 (cas central) | 23,9 M€ | 274,6 M€ |
| Pire stress test | Cumul : fonds à 16,1 M€ en année 20, aucun déficit | Non testé ; même niveau de risque simulé que S1 et S2 |
| Échec simulé avant 20 / 30 ans | 4,2 % / 10,9 % | 5,7 % / 11,9 % |
| Sur 20 ans : activités / dividendes / fonds | 0,29 / 4,0 / 3,4 M€, plus 0,8 M€ d'excédents de dividendes versés au fonds | 1,8 / 0 / 75,5 M€ |
| Option propre au scénario | Peu d'activités possibles ; pas de locataire d'ancrage (moins de 40 chambres) | Locataire d'ancrage possible si la localisation s'y prête : −8 % de capital nécessaire (L3, modèle 4) |

Pour S1, les dividendes de transition (0,4 M€) dépassent le besoin pendant 10 ans. L'excédent, environ 80 k€ par an, est versé au fonds, qui grossit plus vite.

---

## 8. Ce qui reste à valider avant tout engagement

| Point | Pourquoi c'est décisif | Qui peut le valider |
|---|---|---|
| Budget du bien réel (gros entretien, valeur de reconstruction, personnel) | C'est le premier facteur de risque : le haut de la fourchette multiplie le risque par 4 à 8 | Architecte du patrimoine, assureur, régisseur ; un an d'exploitation réelle |
| Véhicule du fonds d'entretien et sa fiscalité | Il détermine le rendement net (3 % retenu) | Avocat fiscaliste |
| Structure de détention (SCI, SAS, holding) et régime MH | Accès à la déduction, taxe sur les holdings, IFI, bail rural | Avocat fiscaliste, notaire, expert-comptable |
| Politique de placement et frais | Un point de rendement en moins ajoute 7 à 8 points de risque à 30 ans | Conseiller en investissement indépendant |
| Gouvernance (charte, comité, succession) | Sans discipline, le risque double ; le propriétaire a 26 ans | Notaire, avocat |
| Activités du socle : PLU, ABF, bail rural, performance énergétique des logements | Conditions de chaque revenu | Mairie, ABF, avocat |

La feuille de route (L7) organise ces validations dans le temps.
