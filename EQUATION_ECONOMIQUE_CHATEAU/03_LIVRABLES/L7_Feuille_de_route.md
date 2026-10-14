# L7 — Feuille de route

> **Statut de ce document**
> - Plan d'action proposé au propriétaire. Il découle de L1 à L6. Les durées sont des ordres de grandeur (HYPOTHÈSES), pas des engagements.
> - Aucune démarche n'a été engagée : aucun contact pris, aucune dépense faite. Chaque étape qui implique un tiers ou une dépense demande l'accord du propriétaire.
> - Les coûts des professionnels (architecte du patrimoine, avocat, notaire…) ne sont pas publiés de façon fiable : ils sont indiqués « sur devis ».

---

## 1. Le principe : ne rien rendre irréversible avant d'avoir validé trois chiffres

La solution (L4) tient si trois chiffres sont justes. Ce sont aussi les trois premiers facteurs de risque mesurés par L6.

| Chiffre à valider | Valeur du modèle (S2) | Effet d'une erreur (L6) |
|---|---|---|
| **Le besoin annuel du bien réel** | 1,24 M€ (fourchette de 0,78 à 2,06 M€) | Au haut de la fourchette, l'échec avant 20 ans passe de 4 % à 30 % |
| **Le rendement réel net du fonds**, après impôts et frais, dans le véhicule retenu | 3 % par an | À 2 %, l'échec à 30 ans passe de 11 % à 19 % |
| **Le capital réellement affecté** au départ | 60 M€ et 1 M€ de dividendes par an pendant 10 ans | Avec 40 M€, l'échec avant 20 ans passe de 4 % à 17 % |

Tant que ces trois chiffres ne sont pas validés, éviter tout engagement difficile à défaire (§ 5).

---

## 2. Les phases

### Phase 0 — Cadrer (environ 0 à 6 mois)

| Action | Résultat attendu | Qui |
|---|---|---|
| Fixer le niveau d'exigence visé (S1, S2 ou S3), sur la base de L1 | Un budget cible, par exemple 1,24 M€ par an pour S2 | Propriétaire |
| Faire l'inventaire du capital qui pourrait être **affecté** au domaine, distinct du patrimoine personnel courant : liquidités, entreprises, actifs cessibles | Un montant de capital mobilisable et un calendrier | Propriétaire, conseiller indépendant |
| Appliquer la règle de dimensionnement (L3, modèle 3) : environ 70 fois le besoin annuel pour 95 % de chances de tenir 30 ans avec un fonds seul, ou environ 57 M€ et 1 M€ de dividendes pendant 10 ans pour 95 % de chances de tenir 20 ans en S2 | **La taille de domaine compatible avec le capital** | Propriétaire, avec le modèle |
| Choisir les conseils | Avocat fiscaliste, notaire, expert-comptable, architecte du patrimoine, conseiller en investissement indépendant | Propriétaire (sur devis) |

**Décision de fin de phase.** Si le capital affectable est très inférieur au besoin du domaine visé, viser un domaine plus petit (S1 demande environ 15 à 23 M€), ou décaler l'achat (phase 3).

### Phase 1 — Valider le budget sur un bien réel, avant l'achat (environ 6 à 18 mois)

| Action | Ce qu'elle remplace dans le modèle | Qui |
|---|---|---|
| Diagnostic de l'état sanitaire du bâti et plan pluriannuel de travaux sur 20 ans | Valeur de reconstruction au m² et taux de gros entretien (les deux paramètres les plus sensibles, L1, § 6) | Architecte du patrimoine (sur devis) |
| Proposition d'assurance sur la valeur de reconstruction | Taux d'assurance (3 ‰) et risque de non-assurabilité | Assureur ou courtier spécialisé |
| Comptes réels du vendeur sur 3 ans au moins : énergie, taxes, assurances, personnel, contrats | Énergie, taxes, contrats | Vendeur, notaire |
| Plan de gestion des jardins et du parc (zones de soin, prairies, sous-traitance) | Effectifs de jardiniers et coûts des jardins | Paysagiste ou jardinier en chef (sur devis) |
| Calcul de l'IFI et des taxes foncières sur le bien réel | IFI et taxes | Notaire, expert-comptable |
| **Recalcul du modèle avec les données réelles** | Toutes les hypothèses concernées | Modèle (`02_MODELE`) |

**Comment recalculer.**
- Pour les résultats déterministes (budget, projections, stress tests), il suffit de modifier les cellules bleues de la feuille Hypotheses du classeur : tout se recalcule.
- Pour mettre à jour les probabilités et les dotations nécessaires :
  1. modifier les mêmes valeurs dans les fichiers `parametres*.py` ;
  2. relancer `python3 construire_modele.py`, puis `python3 calculer_mc.py`.

**Décision de fin de phase (go / no-go).** Acheter seulement si le besoin réel, multiplié par environ 70, reste compatible avec le capital affectable. Sinon, renégocier, chercher un bien déjà restauré ou plus petit, ou attendre.

### Phase 2 — Construire la structure et écrire la charte (en parallèle de la phase 1)

| Action | Points à trancher | Qui |
|---|---|---|
| Choisir la structure de détention du château et de la partie privée | Détention directe ou SCI familiale à l'impôt sur le revenu ; accès au régime fiscal des monuments historiques ; engagement de 15 ans [R3-04] [R3-06] | Avocat fiscaliste, notaire |
| Choisir le **véhicule du fonds d'entretien** et mesurer sa fiscalité | Rendement net attendu ; IFI (actifs financiers ou immobiliers) ; taxe de 20 % sur les holdings patrimoniales [R3-18] ; transmission | Avocat fiscaliste |
| Structurer la société d'exploitation des activités | Loyer de marché à la SCI ; plafond de 10 % de recettes commerciales dans une SCI à l'IR [R3-59] ; TVA équestre à 5,5 % ou 20 % [R3-22] | Expert-comptable, avocat |
| Rédiger la **charte du domaine** (L4, § 3) | Règle de dépense, réserve, fonds de travaux, règles de tension, conversion, excédent, placements | Propriétaire, avocat |
| Prévoir la gouvernance et la continuité | Comité avec au moins une personne indépendante ; que se passe-t-il en cas d'incapacité ou de décès du propriétaire ? | Notaire, avocat |

### Phase 3 — Constituer le capital (de quelques années à 15 ans ou plus, selon le point de départ)

| Action | Repère chiffré | Condition |
|---|---|---|
| Acquérir ou développer des PME rentables, **sans dette d'acquisition** au moment où elles financent le domaine | 1 M€ de dividendes nets par an ≈ 2,5 M€ d'EBITDA [R8-35] (ESTIMATION) | Au moins 5 entreprises ; dirigeants salariés |
| Appliquer la règle de conversion : dividendes non dépensés et produits de cession versés au fonds | 60 M€ demandent environ 10 ans à 5 M€ d'épargne par an, 18 ans à 2,5 M€, 35 ans à 1 M€ (L4, § 6.2) | Discipline écrite |
| Étudier, si le domaine s'y prête, la vente de bâtiments inutiles pour amorcer le fonds (L3, modèle 5) | Montant INCONNU, à faire estimer | PLU, ABF, Safer, notaire ; jamais à proximité de la partie privée |
| Placer le fonds selon la politique de placement | Rendement réel net visé : 3 % ; frais à minimiser | Conseiller indépendant, sans conflit d'intérêts |

**Déclencheur de la phase 4.** Le fonds et la réserve sont constitués au niveau requis pour le domaine visé : **seuil de déclenchement** de L4 (§ 3).

### Phase 4 — Acquérir et installer (année 1)

| Action | Point d'attention |
|---|---|
| Acquisition, idéalement d'un bien déjà restauré | Le rattrapage d'un retard d'entretien n'est pas dans le budget (L1, § 8) |
| Installer le socle d'activités calmes : logements dans les communs, hivernage, bail solaire, pensions | Changement de destination, PLU et ABF pour les logements ; performance énergétique (logements G interdits à la location) [R3-34] ; contrats de pension qui ne soient pas requalifiables en bail rural (R3, question 7) ; accord de l'ABF pour le solaire [R3-63] |
| Recruter l'équipe, à commencer par le régisseur | Personnel du domaine : 10 ETP en S2 |
| Ouvrir le fonds de travaux et y verser la première provision | Ne jamais l'utiliser pour autre chose que le gros entretien |
| **Mesurer les coûts réels pendant un an complet** | C'est la donnée la plus précieuse pour la suite |

### Phase 5 — Régime de croisière (années 2 à 10, dividendes de transition)

- Revue annuelle par le comité du domaine, à l'aide du tableau de bord du § 3.
- Campagnes de gros entretien tous les 4 ans, payées par le fonds de travaux.
- Recalcul du modèle avec les coûts réels de l'année : le budget et le capital requis sont mis à jour chaque année.
- Préparation de la fin des dividendes : vérifier en année 8 que le fonds couvre seul le besoin, avec sa règle de dépense.

### Phase 6 — Autonomie (au-delà de l'année 10)

- Le domaine vit du fonds et du socle d'activités.
- Règle de l'excédent : si le fonds dépasse durablement le niveau requis (par exemple 1,5 fois), l'excédent peut financer une restauration exceptionnelle.
- Préparer la transmission avec le notaire. L'exonération de droits de succession de l'article 795 A suppose une convention d'ouverture au public de 50 jours par an [R3-13] [R3-14] : c'est un choix qui touche la tranquillité.

---

## 3. Tableau de bord annuel et déclencheurs

| Indicateur | Seuil | Action | Simulée dans le modèle ? |
|---|---|---|---|
| Réserve de trésorerie | Moins d'un an de besoin | Couper 10 % du besoin en dépenses discrétionnaires ; reporter 30 % de la campagne ; retrait d'urgence plafonné à 4 % du capital | oui |
| Retrait sur le fonds | Au-dessus du plafond lissé hors tension | Interdit par la charte | oui |
| Fonds de travaux | Provision non versée | Interdit : la provision est versée même en tension | oui |
| Fonds d'entretien réel (euros constants) | Moins de 80 % du niveau de départ | Revoir le budget ; suspendre les investissements futurs et les achats de prestige | non |
| Rendement réel moyen sur 5 ans | Moins de 2 % par an | Revoir l'allocation et les frais ; ramener le taux de retrait vers 2,5 % | non |
| Besoin réel mesuré | Plus de 10 % au-dessus du budget pendant 2 ans | Recalculer le capital nécessaire ; activer les leviers du « prestige efficace » (L2, § 5) | non |
| Dividendes de transition | Moins de 50 % du prévu pendant 2 ans | Allonger la constitution du capital ; ne pas compenser par des activités bruyantes | non |
| Couverture sans dividendes (activités + plafond de retrait, rapportés aux charges) | Moins de 1,1 | Alerte : la marge de sécurité est presque consommée (cas du cumul des chocs, L5, § 5) | indicateur calculé |
| Assurance | Hausse de prime de plus de 30 % ou refus de renouvellement | Remise en concurrence ; mesures de prévention ; révision du budget | non |

---

## 4. Calendrier synthétique (ordre de grandeur, HYPOTHÈSE)

```
Phase 0  Cadrer                         ████
Phase 1  Valider le budget (bien réel)      ████████
Phase 2  Structure et charte                ████████
Phase 3  Constituer le capital          ████████████████████████  (durée selon le point de départ)
Phase 4  Acquérir et installer                                    ██
Phase 5  Croisière (dividendes)                                     ████████████████████
Phase 6  Autonomie (fonds seul)                                                         ████████→
```

La durée de la phase 3 dépend entièrement de la situation du propriétaire, que ce dossier ne connaît pas. Si le capital existe déjà, les phases 0 à 2 peuvent tenir en 12 à 18 mois.

---

## 5. Décisions à ne pas prendre trop tôt

| Décision | Pourquoi elle est difficile à défaire | Quand la prendre |
|---|---|---|
| Signer un bail commercial avec un exploitant (locataire d'ancrage) | 9 ans au moins, droit au renouvellement, indemnité d'éviction de l'ordre de la valeur du fonds [V2A-36] [V2A-41] | Seulement après la validation du budget et si la localisation s'y prête (S3) ; tester d'abord par un bail dérogatoire de 3 ans au plus [V2A-40] |
| Vendre des communs ou des terres | Définitif ; voisins permanents | Seulement pour des bâtiments éloignés de la partie privée, après estimation et accord de l'urbanisme |
| Opter pour le régime fiscal des monuments historiques | Engagement de conservation de 15 ans [R3-06] | Quand la structure de détention est arrêtée |
| Signer la convention de l'article 795 A (exonération de droits de succession) | Ouverture au public de 50 jours par an, maintien du mobilier [R3-13] | Au moment de préparer la transmission |
| Mettre des terres ou des écuries à disposition d'un tiers | Risque de bail rural, qui fait perdre durablement la maîtrise (R3, question 7) | Avec un contrat rédigé par un avocat |
| Emprunter pour l'achat | L'annuité ajoute 15 % au besoin de S2 (L1) ; le brief traite la dette comme un scénario complémentaire | Seulement si le fonds couvre aussi l'annuité |

---

## 6. Ce que le propriétaire peut faire dès maintenant, sans engager de dépense

1. Relire L1 et fixer son niveau d'exigence (S1, S2 ou S3).
2. Estimer, pour lui seul, le capital qu'il pourrait affecter au domaine et à quel rythme.
3. Appliquer la règle d'environ 70 fois le besoin pour vérifier la cohérence entre le domaine rêvé et le capital disponible.
4. Lister les questions de L4 (§ 8) à poser aux conseils lors des premiers rendez-vous.
