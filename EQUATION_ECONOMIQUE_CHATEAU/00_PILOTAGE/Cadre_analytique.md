# Cadre analytique — L'équation économique du domaine

Ce document fixe les **définitions** et la **méthode** utilisées dans les modèles et les livrables. Il ne contient pas de données chiffrées, sauf mention contraire. Les données arrivent par les agents R1 à R8.

---

## 1. L'équation fondamentale (une année t)

```
Flux disponible(t) = Σ CN_i(t)  +  RD(t)  +  SUB(t)  −  B(t)  −  DETTE(t)

Réserve(t) = Réserve(t−1) × (1 + r_réserve)  +  Flux disponible(t)

Contraintes : Réserve(t) ≥ 0 chaque année, y compris dans les années de crise.
              Une réserve négative est un ÉCHEC (critère n° 6 du § 5).
Objectif de gestion : Réserve(t) ≥ Réserve_minimale (12 mois de charges de l'année précédente).
              Passer sous ce seuil n'est pas un échec mais une TENSION, qui déclenche les règles de pilotage
              (coupe des dépenses discrétionnaires, report partiel des travaux, retrait d'urgence plafonné),
              puis la reconstitution de la réserve.
```

Précision ajoutée après l'équipe rouge (V2R M3) : la version précédente de cette ligne faisait de la réserve minimale de 12 mois une contrainte, alors que le modèle et le critère n° 6 définissent l'échec comme une réserve négative. Les deux notions sont désormais distinctes, et le modèle publie à la fois la probabilité d'échec et la fréquence des tensions.

| Terme | Définition |
|---|---|
| **B(t)** — besoin de trésorerie du domaine | Toutes les dépenses nécessaires pour que le domaine existe au niveau de prestige choisi, qu'il y ait des activités ou non : bâti (entretien courant + provision de gros entretien), personnel, jardins, parc et terres, énergie, assurances, impôts et taxes, équipements (renouvellement), chevaux et installations privées, administration, imprévus, investissements de développement. |
| **CN_i(t)** — contribution nette de l'activité i | Chiffre d'affaires HT − charges variables − charges fixes propres (y compris le personnel dédié) − renouvellement de ses investissements − usure supplémentaire qu'elle cause au domaine − impôt qui lui est attribuable **+ économies qu'elle procure sur B**. Exemple : des chevaux en pension qui pâturent le parc réduisent les fauches ; une activité qui exige des jardins impeccables finance une partie des jardiniers. |
| **RD(t)** — revenu d'un moteur extérieur | Dividendes d'une entreprise extérieure ou retrait soutenable d'une dotation financière, **nets d'impôts**. |
| **SUB(t)** — subventions encaissées | Seulement celles qui sont **notifiées**. Une subvention espérée n'est jamais comptée dans le scénario central. |
| **DETTE(t)** | Service d'une dette d'acquisition ou de travaux. Scénario complémentaire seulement. |

Trois règles de lecture :

1. **Chiffre d'affaires ≠ EBE ≠ résultat ≠ trésorerie.** Seule la trésorerie disponible, après impôts, renouvellement des investissements et gros entretien, compte dans l'équation.
2. **Une activité n'aide le domaine que si sa contribution nette est positive.** Elle doit couvrir aussi les coûts qu'elle ajoute (normes ERP, usure, personnel, assurance), pas seulement ses coûts directs.
3. **Le gros entretien n'est pas lissé dans la réalité.** Une toiture se refait par campagnes. Le modèle provisionne chaque année dans un **fonds de gros entretien**, puis y puise lors des campagnes. On vérifie que ce fonds ne devient jamais négatif.

---

## 2. Les trois « coins » qui déforment l'équation

### 2.1 Le coin fiscal : qui paie les coûts, avant ou après impôt ?

Une même dépense ne coûte pas la même chose selon qu'elle est :
- **professionnelle** : déductible, donc payée avant impôt ;
- **privée** : payée sur un revenu déjà imposé.

Pour couvrir 1 € de dépense privée, il faut produire un revenu brut nettement supérieur :

| Canal | Logique | Revenu brut nécessaire pour 1 € privé |
|---|---|---|
| Dividende d'une société à l'IS | 1 / ((1 − IS) × (1 − PFU)) | Environ 1,9 € avec IS 25 % et PFU 30 %. Taux 2026 à confirmer par R3. |
| Salaire | Charges patronales et salariales, puis impôt sur le revenu au taux marginal | Plus de 2 €. Calcul à faire avec les taux de R2 et R3. |
| Charges d'un MH déductibles du revenu global | Réduit le coût net au taux marginal du propriétaire | Suppose que le propriétaire **a** des revenus imposables. C'est une forme de dépendance à ses revenus personnels. |

**Conséquence de conception.** Il faut répartir explicitement chaque coût du domaine entre :
- la part liée à une activité réelle (déductible, financée par des clients) ;
- la part privée (logis du propriétaire, chevaux personnels, jardins privatifs).

La part privée doit être **financée après impôt** : c'est le vrai « coût de la vie de château ». Une société qui supporte des coûts privés du propriétaire sans contrepartie s'expose à l'acte anormal de gestion et à l'abus de biens sociaux (à valider par R3).

### 2.2 Le coin de tranquillité : chaque euro d'activité consomme du calme

Chaque activité a un coût en tranquillité : présence de tiers, bruit, circulation, intrusion visuelle, dépendance aux week-ends.

Deux leviers permettent de concilier revenus et vie privée :
- **Zonage** : zone privée, zone d'activités, accès séparés, distance minimale entre les événements et le logis ou les écuries.
- **Calendrier** : plafonds de jours d'événements, saisons réservées.

Un grand domaine (S2, S3) peut accueillir plus d'activité à tranquillité égale qu'un petit domaine.

Le modèle attribue à chaque activité une **note de tranquillité** de 1 à 5. Il élimine les combinaisons qui dépassent la tolérance fixée.

### 2.3 Le coin de prestige : le niveau d'entretien fait exploser B

Passer d'un parc fauché à des jardins réguliers impeccables multiplie le personnel et les fournitures. Certaines activités **exigent** ce niveau (réceptions, hôtellerie, tournages) et peuvent en financer une part. D'autres n'en tirent aucun bénéfice (forêt, baux, stockage).

Le niveau de prestige est donc un **choix économique**, pas seulement esthétique.

---

## 3. Qualité des revenus (classement utilisé partout)

| Classe | Nature | Exemples | Volatilité | Sensibilité aux crises | Charge opérationnelle |
|---|---|---|---|---|---|
| **A — Contractuel** | Loyers et redevances fixés par contrat pluriannuel | Baux commerciaux ou ruraux, bail à un exploitant hôtelier ou scolaire, loyer d'une centrale solaire, locations résidentielles longues, contrats de stockage | Faible | Faible à moyenne (risque de défaillance du locataire, vacance) | Faible |
| **B — Récurrent opérationnel** | Clients abonnés ou présents toute l'année | Pensions de chevaux, pension de poulinières, adhésions à un club, clients réguliers | Moyenne | Moyenne | Forte (personnel 365 jours par an) |
| **C — Transactionnel ou occasionnel** | Ventes ponctuelles | Mariages, séminaires, tournages, visites, concours, ventes de chevaux | Forte | Forte (2020 : arrêt quasi total des événements, à chiffrer par R7) | Forte et saisonnière |
| **D — Financier ou extérieur** | Dotation, portefeuille, dividendes d'une entreprise extérieure | Retrait soutenable, dividendes | Selon l'allocation | Corrélée aux marchés | Faible sur le domaine, mais dépend de la gouvernance |

**Principe de robustesse retenu.** C'est une hypothèse de méthode, testée ensuite par les stress tests :
- les **charges fixes** du domaine (B hors gros travaux exceptionnels) doivent être couvertes **en régime de croisière** par les classes A et D ;
- les classes B et C financent la réserve, le gros entretien et le développement.

Un modèle qui couvre ses charges fixes seulement grâce à la classe C est jugé **fragile**, même s'il est rentable sur le papier.

---

## 4. Mathématique d'un moteur extérieur

### Dotation financière

Le capital nécessaire est :

```
K = B_privé_net / s_net
```

où s_net est le taux de retrait soutenable **réel**, après frais et impôts.

Exemple d'ordre de grandeur, à remplacer par les données de R8 : avec s_net = 3 %, il faut 33 € de capital par euro de besoin annuel.

### Entreprise extérieure

```
Trésorerie distribuable ≈ EBE − investissements de maintien − IS − service de la dette
```

Elle doit couvrir B_privé × 1/(1 − PFU), plus une marge de sécurité.

Trois risques :
- la dépendance au fondateur ;
- le cycle du secteur ;
- la vente de l'entreprise.

D'où une condition de pérennité à tester : **convertir progressivement** les dividendes en dotation diversifiée, pour que le domaine ne dépende plus de l'entreprise à l'horizon de 15 à 20 ans.

---

## 5. Critères de résilience (appliqués à chaque modèle)

1. **Taux de couverture des charges fixes par les revenus A et D** : cible ≥ 1,0 en régime de croisière, minimum 0,7.
2. **Réserve de liquidité** : 12 à 24 mois de charges fixes.
3. **Chiffre d'affaires −30 %** pendant 3 ans : la réserve reste positive.
4. **Crise de type 2020** (événementiel et hôtellerie quasi à l'arrêt pendant 1 an, partiellement la 2e année) : la réserve reste positive.
5. **Gros travaux imprévus** (sinistre non couvert, découverte structurelle) : absorbés par le fonds de gros entretien ou par la réserve.
6. **Monte-Carlo sur 20 et 30 ans** : probabilité que la réserve devienne négative ≤ 5 % pour le modèle recommandé.
7. **Dépendance au fondateur** : le modèle continue-t-il de fonctionner si le propriétaire est indisponible pendant 6 mois ?
8. **Tranquillité** : le propriétaire peut-il vivre normalement, sans tiers dans sa zone privée et avec une limite de jours d'activité par an ?

---

## 6. Horizons temporels

| Horizon | Enjeux |
|---|---|
| **0 à 5 ans** | Courbe en J : investissements, montée en charge, saturation du fondateur, apprentissage. |
| **5 à 15 ans** | Régime de croisière, premières campagnes de gros entretien, concurrence, usure des installations. |
| **15 à 30 ans** | Renouvellement des toitures et réseaux, évolution des goûts (mariages, équitation), climat (sécheresses et foin, chaleur), réformes fiscales possibles (le régime des MH n'est pas garanti), étapes de vie du propriétaire. |
