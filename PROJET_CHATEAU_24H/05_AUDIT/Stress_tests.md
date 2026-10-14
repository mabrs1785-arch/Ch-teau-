# Stress tests — Opération Château (version corrigée après audit)

Source : `04_MODELES_ECONOMIQUES/Previsionnels_10_ans.xlsx`, **version corrigée** (corrections d'audit E1 à E4 et suivantes : prix convertis en HT, loyer privé du fondateur sorti du CA, capital du fondateur calculé au prorata des apports, DSCR après gros entretien, frais de cession, verdict exigeant un TRI investisseur ≥ 6 % et un dirigeant payé). Recalculé avec LibreOffice le 2026-10-14, 0 erreur de formule.

Tous les montants sont des **sorties de modèle fondées sur des hypothèses en grande partie non vérifiées** (voir `Hypotheses_non_verifiees.md`). Ils servent à comparer, pas à prédire.

Verdict automatique :
- **VIABLE** : trésorerie jamais négative ; trésorerie an 10 ≥ réserve de 150 k€ ; DSCR (après gros entretien) ≥ 1,2 ; cash-flow libre ≥ 0 sur les années 4 à 10 ; TRI des investisseurs extérieurs ≥ 6 % ; dirigeant payé par le domaine.
- **FRAGILE** : trésorerie positive, mais au moins une autre condition manque.
- **NON VIABLE** : trésorerie négative à un moment.

---

## 1. Avant tout stress : les scénarios « classiques » échouent déjà

| Feuille | Montage | CA an 5 (HT) | EBITDA an 5 | Trésorerie min. | Verdict |
|---|---|---|---|---|---|
| A_central | Équestre événementiel ; 4,25 M€ levés dont 2,7 M€ de dettes | 379 k€ | −75 k€ | −3,30 M€ | NON VIABLE |
| A_optimiste | idem, volumes +15 %, prix +8 % | 470 k€ | +3 k€ | −2,53 M€ | NON VIABLE |
| B_central | Multiactivité ; 4,45 M€ levés dont 2,8 M€ de dettes | 386 k€ | −50 k€ | −3,12 M€ | NON VIABLE |
| B_optimiste | | 479 k€ | +29 k€ | −2,35 M€ | NON VIABLE |
| C_central | Location puis achat an 5 ; dette 1,9 M€ | 335 k€ | −82 k€ | −2,41 M€ | NON VIABLE |
| B_sans_dette | B financé à 100 % en fonds propres | 386 k€ | −50 k€ | −0,65 M€ | NON VIABLE |

**Lecture.** Avec une équipe salariée normale (environ 3,5 ETP plus un dirigeant payé), l'exploitation est **déficitaire avant toute dette**. Le problème n'est pas le montage, c'est le modèle économique : 12 postes de charges fixes (environ 290 k€/an) face à environ 390 k€ de CA HT, dont environ 30 % de coûts variables.

## 2. Les configurations qui ne sont pas en trésorerie négative

| Feuille | Description | EBITDA an 5 | Cash-flow libre an 8-10 | Trésorerie an 10 | Verdict |
|---|---|---|---|---|---|
| B_frugal_sans_dette | Fondateur bénévole ; 1,5 soigneur ; jardinier à mi-temps ; 4,2 M€ en fonds propres externes | 80 k€ | ≈ +56 k€ | 570 k€ | **FRAGILE** (TRI investisseurs ≈ −3 %) |
| C_cible | Bail modéré (40 k€/an) années 1-4, achat an 5 ; holding 3,4 M€ ; dette 0,4 M€ ; fondateur payé par la holding, pas par le domaine | 48 k€ | ≈ −6 k€ | 218 k€ | **FRAGILE** |
| C_cible_negocie | Idem, prix −20 % (2,12 M€), travaux −30 % ; holding 2,6 M€ | 48 k€ | ≥ 0 | 336 k€ | **FRAGILE** (DSCR 1,12) |

**Enseignement central.** Dans la meilleure configuration, le domaine **s'autofinance tout juste** : son exploitation couvre le fonctionnement et le gros entretien, avec un fondateur non payé et une dette quasi nulle. **Dette soutenable** (DSCR 1,2 après gros entretien, an 10) : **0,28 à 0,60 M€**. **Fonds propres nécessaires** : environ **2,9 M€** (bien négocié à 2,1 M€) à **3,8 M€** (bien à 2,65 M€), réserve comprise.

## 3. Stress tests sur B frugal sans dette (feuilles S_Bfsd_*)

| Stress | EBITDA an 5 | Trésorerie min. | Trésorerie an 10 | Verdict |
|---|---|---|---|---|
| Référence | 80 k€ | 201 k€ | 570 k€ | FRAGILE |
| CA −30 % | 1 k€ | −93 k€ | −93 k€ | **NON VIABLE** |
| Travaux +30 % | 80 k€ | −203 k€ | 134 k€ | **NON VIABLE** (trou pendant les travaux) |
| Ouverture retardée de 12 mois | 53 k€ | 88 k€ | 400 k€ | FRAGILE |
| Taux +2 points | 80 k€ | 201 k€ | 570 k€ | FRAGILE (sans dette, aucun effet) |
| Retrait de 50 % des investisseurs | 80 k€ | −1,90 M€ | −1,53 M€ | **NON VIABLE** (rédhibitoire) |
| Annulation de 40 % des événements | 41 k€ | 152 k€ | 247 k€ | FRAGILE |
| Cumul (CA −15 %, travaux +15 %, retard 12 mois, taux +1 point) | 18 k€ | −172 k€ | −112 k€ | **NON VIABLE** |

## 4. Stress tests sur C cible (feuilles S_Ccib_*)

| Stress | EBITDA an 5 | DSCR min. | Trésorerie min. | Verdict |
|---|---|---|---|---|
| Référence | 48 k€ | 0,80 | 186 k€ | FRAGILE |
| CA −30 % | −21 k€ | −1,60 | −440 k€ | **NON VIABLE** |
| Travaux +30 % | 48 k€ | 0,69 | −111 k€ | **NON VIABLE** |
| Ouverture retardée de 12 mois | 48 k€ | 0,80 | 142 k€ | FRAGILE |
| Taux +2 points | 48 k€ | 0,68 | 182 k€ | FRAGILE |
| Holding n'apporte que 50 % | 48 k€ | 0,80 | −1,48 M€ | **NON VIABLE** (rédhibitoire) |
| Annulation de 40 % des événements | 22 k€ | −0,09 | −26 k€ | **NON VIABLE** |
| Cumul | 13 k€ | −0,42 | −332 k€ | **NON VIABLE** |

## 5. Conclusions

1. **Aucun scénario financé principalement par de la dette ou par des investisseurs extérieurs ne survit, même sans stress.** La dette demandée (2 à 2,9 M€) est 4 à 10 fois supérieure à la dette soutenable.
2. **Les variables qui tuent**, dans l'ordre :
   - (a) la disponibilité réelle des fonds propres : un retrait d'investisseur ou une holding qui apporte moitié moins est rédhibitoire ;
   - (b) le chiffre d'affaires : −30 % est rédhibitoire ;
   - (c) le dépassement de travaux : +30 % crée un trou de 0,1 à 0,2 M€ ;
   - (d) la masse salariale : c'est la différence entre « central » et « frugal ».

   Le taux d'intérêt compte peu, **parce que les configurations survivantes n'empruntent presque pas**.
3. **Réserve indispensable** : 0,4 à 0,6 M€ de liquidités ou une ligne garantie par la holding, au-delà des fonds propres d'acquisition.
4. **Les événements sont le revenu le plus volatil.** Correction suite à l'audit : le scénario A (86 % de CA équestre, peu de mariages) est *moins* exposé à l'annulation des mariages que B ou C. Il est en revanche exposé à la défection d'un cavalier professionnel locataire et à l'absence de preuve de demande pour les showcases. Dans tous les cas, la base récurrente (pensions) doit primer.
5. Prendre un vendeur en difficulté (−20 % sur le prix) et réutiliser l'existant (−30 % de travaux) font plus pour la viabilité que tout montage financier : ils réduisent les fonds propres nécessaires d'environ 0,9 à 1 M€.

## 6. Limites
- Charges indexées à 2,5 % contre 2 % pour les prix (effet ciseau prudent).
- IS simplifié (25 %, sans taux réduit ni plafonnement des déficits) ; montants HT, TVA neutre.
- Gros entretien = 1 %/an de (prix + travaux) : règle empirique, à remplacer par un diagnostic d'architecte du patrimoine. La Demeure Historique cite « au moins 40 k€/an hors travaux » par monument (A8-04), ordre de grandeur cohérent.
- Modèle annuel : le creux de trésorerie de janvier à avril (saisonnalité) n'est pas visible, d'où la réserve.
