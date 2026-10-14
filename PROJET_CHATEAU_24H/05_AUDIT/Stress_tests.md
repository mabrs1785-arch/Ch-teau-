# Stress tests — Opération Château

Source des chiffres : `04_MODELES_ECONOMIQUES/Previsionnels_10_ans.xlsx`, recalculé avec LibreOffice le 2026-10-14 (0 erreur de formule). Tous les montants sont des **sorties de modèle fondées sur des hypothèses en grande partie non vérifiées** (cf. `Hypotheses_non_verifiees.md`). Ils servent à comparer les scénarios entre eux, pas à prédire un résultat.

Règle du verdict automatique : VIABLE si la trésorerie n'est jamais négative, si la trésorerie de l'an 10 atteint au moins la réserve cible (150 k€), si le DSCR reste ≥ 1,2 et si le cash-flow libre d'exploitation est ≥ 0 sur les années 4 à 10. FRAGILE si la trésorerie reste positive sans remplir les autres conditions. NON VIABLE sinon.

---

## 1. Résultat préalable : les scénarios « classiques » échouent avant tout stress

| Feuille | CA an 5 | EBITDA an 5 | Trésorerie min. sur 10 ans | Verdict |
|---|---|---|---|---|
| A_central (équestre événementiel, ~4,25 M€ levés dont 2,7 M€ de dettes) | 416 k€ | −47 k€ | −3,28 M€ | NON VIABLE |
| A_optimiste | 510 k€ | +34 k€ | −2,47 M€ | NON VIABLE |
| B_central (multiactivité) | 441 k€ | −5 k€ | −2,96 M€ | NON VIABLE |
| B_optimiste | 542 k€ | +82 k€ | −2,10 M€ | NON VIABLE |
| C_central (location puis achat an 5) | 383 k€ | −44 k€ | −2,15 M€ | NON VIABLE |
| B_sans_dette (B financé à 100 % en fonds propres) | 441 k€ | −5 k€ | −0,49 M€ | NON VIABLE |

**Lecture.** Avec une équipe salariée normale (12 postes de charges fixes, dont 3,5 ETP et une rémunération du dirigeant), l'exploitation d'un domaine de ce type dégage un EBITDA proche de zéro, **même sans dette**. Ce n'est donc pas un problème de montage financier : c'est un problème de modèle économique. Les stress tests n'ont de sens que sur les configurations qui passent sans stress.

## 2. Les deux seules configurations qui passent

| Feuille | Description | EBITDA an 5 | Cash-flow libre an 5 | Trésorerie an 10 | Verdict |
|---|---|---|---|---|---|
| **B_frugal_sans_dette** | Exploitation B ; le fondateur tient l'écurie et les événements sans salaire ; 1,5 soigneur ; jardinier à mi-temps ; acquisition et travaux (~4,2 M€) financés **à 100 % en fonds propres** | 125 k€ | 83 k€ | 732 k€ | VIABLE sous hypothèses |
| **C_cible** | Location d'un domaine années 1 à 4, achat en an 5 ; holding du fondateur qui apporte **2,9 M€** ; dette limitée à 0,9 M€ ; exploitation frugale | 85 k€ | 45 k€ (puis −27 k€ dès l'an 8) | 8 k€ | FRAGILE |

**Lecture.** L'exploitation « frugale » dégage environ 85 à 130 k€ d'EBITDA pour 3,9 à 4,2 M€ immobilisés, soit environ 2 à 3 % de rendement brut sur l'actif, avant gros entretien. Elle peut porter au maximum **0,8 à 0,9 M€ de dette** (DSCR 1,2, 4,5 %, 20 ans). Il reste donc **3,1 à 3,5 M€ de fonds propres** à trouver pour un domaine à 2,65 M€.

## 3. Stress tests sur B frugal sans dette (feuilles S_Bfsd_*)

| Stress | EBITDA an 5 | Trésorerie min. | Trésorerie an 10 | Verdict |
|---|---|---|---|---|
| Référence | 125 k€ | 185 k€ | 732 k€ | VIABLE |
| CA −30 % | 30 k€ | −71 k€ | −71 k€ | **NON VIABLE** (cash-flow libre négatif 7 ans sur 7) |
| Travaux +30 % | 125 k€ | −219 k€ | 296 k€ | **NON VIABLE** (trou de trésorerie pendant les travaux, à couvrir par +0,4 M€ de fonds propres) |
| Ouverture retardée de 12 mois | 93 k€ | 38 k€ | 509 k€ | VIABLE (de justesse) |
| Taux +2 points | 125 k€ | 185 k€ | 732 k€ | VIABLE (sans dette, aucun effet) |
| Retrait de 50 % des investisseurs | 125 k€ | −1,91 M€ | −1,37 M€ | **NON VIABLE** (rédhibitoire) |
| Annulation de 40 % des événements | 80 k€ | 130 k€ | 350 k€ | VIABLE |
| Cumul (CA −15 %, travaux +15 %, retard 12 mois, taux +1 pt) | 50 k€ | −220 k€ | −65 k€ | **NON VIABLE** |

## 4. Stress tests sur C cible (feuilles S_Ccib_*)

| Stress | EBITDA an 5 | DSCR min. | Trésorerie min. | Verdict |
|---|---|---|---|---|
| Référence | 85 k€ | 1,21 | 8 k€ | FRAGILE |
| CA −30 % | 2 k€ | −0,04 | −785 k€ | **NON VIABLE** |
| Travaux +30 % | 85 k€ | 1,21 | −321 k€ | **NON VIABLE** |
| Ouverture retardée de 12 mois | 85 k€ | 1,21 | −8 k€ | **NON VIABLE** (de justesse) |
| Taux +2 points | 85 k€ | 1,03 | −72 k€ | **NON VIABLE** |
| Holding n'apporte que 50 % | 85 k€ | 1,21 | −1,44 M€ | **NON VIABLE** (rédhibitoire) |
| Annulation de 40 % des événements | 56 k€ | 0,79 | −272 k€ | **NON VIABLE** |
| Cumul | 44 k€ | 0,56 | −569 k€ | **NON VIABLE** |

## 5. Conclusions des stress tests

1. **Aucun scénario financé principalement par de la dette ou par des investisseurs extérieurs ne résiste**, même sans stress. Le service d'une dette de 2 à 2,9 M€ (environ 170 à 270 k€/an) dépasse durablement l'EBITDA atteignable (estimé à moins de 130 k€).
2. **Les variables qui tuent** sont, dans l'ordre : (a) la disponibilité des fonds propres (retrait d'investisseur = rédhibitoire), (b) le chiffre d'affaires (−30 % = rédhibitoire), (c) le dépassement de travaux (+30 % = trou de trésorerie de 0,2 à 0,3 M€), (d) le coût de la masse salariale. Le taux d'intérêt compte peu, parce que la dette soutenable est de toute façon faible.
3. **La condition de survie est une réserve de liquidité de 0,4 à 0,6 M€** en plus des fonds propres d'acquisition, ou une ligne de crédit garantie par la holding.
4. **L'annulation d'événements est mieux absorbée que la baisse de la base récurrente** (pensions, gîte). Cela plaide pour une base de revenus récurrents équestres plutôt que pour un modèle dominé par l'événementiel (le scénario A pur est le plus exposé).
5. Le stress « hausse du coût de financement » est quasi neutre dans les configurations viables. Ce n'est pas une bonne nouvelle : cela signifie qu'elles ne sont viables **que parce qu'elles n'empruntent presque pas**.

## 6. Limites du modèle (rappel)

- Charges indexées à 2,5 % et prix à 2 % : l'effet de ciseau est volontairement prudent.
- IS simplifié (25 %, sans taux réduit, sans plafonnement des déficits) ; TVA neutre.
- Le gros entretien (1 %/an de la valeur) est une règle empirique non sourcée ; un diagnostic d'architecte du patrimoine peut le multiplier ou le diviser par deux.
- La valeur de sortie (80 % du coût) est arbitraire ; voir les critiques de l'auditeur dans `Objections_et_risques.md`.
