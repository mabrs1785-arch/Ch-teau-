# Stress tests — Opération Château v2 (modèle reconstruit après audit)

Source : `04_MODELES_ECONOMIQUES/Previsionnels_10_ans.xlsx`, version reconstruite (corrections M1 à M5 de l'auditeur, IS à 15/25 %, gros entretien sur bâti et travaux, crédit-vendeur aux conditions de marché), recalculée avec LibreOffice le 2026-10-14 : **0 erreur de formule sur 47 feuilles**.

**Règle de verdict** :
- **VIABLE** : trésorerie jamais négative ; trésorerie an 10 ≥ 150 k€ ; couverture de la dette (DSCR, après gros entretien) ≥ 1,2 et cash-flow libre ≥ 0 dès la 2e année d'exploitation ; TRI des investisseurs extérieurs ≥ 6 % ; dirigeant payé par le domaine.
- **NON AUTOFINANCÉ** : tout est rempli sauf la rémunération du dirigeant.
- **FRAGILE** : trésorerie positive, mais une autre condition manque.
- **NON VIABLE** : trésorerie négative à un moment.

## 1. Avant tout stress, les configurations de base

| Feuille | EBITDA an 10 | Trésorerie min. | Verdict |
|---|---|---|---|
| A central / prudent / optimiste | −78 / −185 / +4 k€ | −3,2 / −4,4 / −2,5 M€ | NON VIABLE |
| B central / prudent / optimiste | −68 / −166 / +8 k€ | −3,0 / −4,2 / −2,4 M€ | NON VIABLE |
| B club deal / crédit-vendeur | −68 k€ | −2,3 / −4,6 M€ | NON VIABLE |
| B sans dette (équipe normale) | −68 k€ | −0,80 M€ | NON VIABLE |
| B frugal sans dette (fondateur non payé, 0 dette) | +25 k€ | −0,01 M€ | NON VIABLE |
| C central (holding 3,4 M€, dette 0,4 M€) | +25 k€ | −0,19 M€ | NON VIABLE |
| C négocié (prix −20 %) | +25 k€ | −0,44 M€ | NON VIABLE |
| C optimiste | +97 k€ | 0 | NON AUTOFINANCÉ |
| C holding réaliste (0,7 M€ de fonds propres) | +25 k€ | −2,89 M€ | NON VIABLE |
| D château modeste (1,15 M€, 56,5 ha) | −15 k€ | −0,19 M€ | NON VIABLE |
| E bail emphytéotique / allégé | ≈ 0 | −1,86 / −0,77 M€ | NON VIABLE |

**Lecture.** Sur le modèle corrigé, **aucune configuration n'est viable avant même tout stress**. Seule C optimiste ressort « non autofinancé ». Le résultat de C central ne vient pas d'une erreur de dimensionnement : les 3,4 M€ de fonds propres couvrent l'achat, mais **l'exploitation consomme du cash chaque année**, d'environ 25 à 55 k€, gros entretien compris.

## 2. Stress tests sur C central (S_Cc_*), C négocié (S_Cn_*) et B frugal sans dette (S_Bfsd_*)

| Stress | C central | C négocié | B frugal sans dette |
|---|---|---|---|
| CA −30 % | NON VIABLE | NON VIABLE | NON VIABLE |
| Travaux +30 % | NON VIABLE | NON VIABLE | NON VIABLE |
| Ouverture retardée de 12 mois | NON VIABLE | NON VIABLE | NON VIABLE |
| Taux +2 points | NON VIABLE | NON VIABLE | NON VIABLE |
| Retrait de 50 % des fonds propres | NON VIABLE | NON VIABLE | NON VIABLE (sans effet, pas d'investisseurs) |
| Annulation de 40 % des événements | NON VIABLE | NON VIABLE | NON VIABLE |
| Cumul (CA −15 %, travaux +15 %, retard, taux +1 pt) | NON VIABLE | NON VIABLE | NON VIABLE |

## 3. Tests de l'auditeur (indépendants, recalculés sur une copie du modèle)
Corrections « cas d'audit » combinées : loyer privé 0, box à 450 €, assurance 12 k€, +0,5 ETP, gros entretien 1,5 %. Résultat : C −195 k€, C négocié −114 k€, B frugal sans dette −3 k€. **Tous NON VIABLES.**

Test « haut » de l'auditeur (18 mariages, prix +2,5 %/an) : C devient robuste. **L'incertitude joue dans les deux sens**, mais les biais optimistes sont plus nombreux et mieux documentés (`Objections_et_risques.md` §5).

## 4. Conclusions
1. **Le problème est économique, pas financier.** Avec un dirigeant payé, l'exploitation d'un domaine château-équestre type a un EBITDA négatif. Avec un dirigeant bénévole, elle couvre son fonctionnement mais pas le gros entretien.
2. **Toute dette au-delà de 0,3 à 0,5 M€ est insoutenable** pour un domaine type. Les montages bancaire, club deal, crédit-vendeur et obligataire sont éliminés.
3. **Variables les plus dangereuses** : le chiffre d'affaires (−30 %), le dépassement de travaux (+30 %), la disponibilité réelle des fonds propres et la masse salariale. Le taux d'intérêt ne compte presque pas, faute de capacité d'endettement.
4. **Le château est un coût de vie** : environ 25 à 65 k€ par an de soutien extérieur, plus le travail du fondateur, selon la taille du domaine et le nombre de salariés. Il faut le budgéter comme tel.

## 5. Limites
- Modèle annuel : le creux de trésorerie saisonnier (janvier-avril) n'est pas visible.
- TVA non récupérable sur les activités exonérées (gîte meublé non para-hôtelier) et sur le logis privé : non modélisée. Effet estimé à quelques pourcents des charges et travaux.
- Dette tirée en totalité l'année de l'achat (biais pessimiste) ; aucune subvention ; aucun avantage fiscal monument historique pour le fondateur (biais pessimistes).
- Multiples de reprise de PME (4,5 fois l'EBITDA) non sourcés : les feuilles H1-H3 sont des ordres de grandeur.
