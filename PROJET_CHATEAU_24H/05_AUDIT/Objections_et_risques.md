# Objections et risques — Audit contradictoire indépendant (Agent 8)

Opération Château v2 · rédigé le 2026-10-14 · auditeur indépendant du directeur de recherche.
Sources propres : `_brut/sources_agent8.csv` (identifiants `A8-xx`). Les autres renvois pointent vers les livrables des agents 1 à 7 (`[A1]`, `[A2 montage n]`, `[A3 Hn]`, `[A4 §n]`, `[A6 §n]`, `[A7 CEn]`) et vers le modèle (`hypotheses.py`, `build_model.py`, numéros de ligne).

**Statuts** : **[PL]** page lue (ouverte et lue le 2026-10-14) · **[EX]** extrait de recherche seulement · **[EST]** estimation, raisonnement explicite · **[INC]** inconnu, avec la méthode pour vérifier · **[CALC]** calcul de l'auditeur sur une copie du modèle (voir §5.6).

> **Règle de lecture.** Cet audit cherche les raisons d'échouer, dans les deux sens : il signale aussi les hypothèses trop pessimistes. Aucun chiffre n'a été inventé ; aucun tiers n'a été contacté.

---

## 0. Verdict de l'auditeur (12 lignes)

1. **Sur le fond, le modèle a raison** : avec un dirigeant payé, l'exploitation type (pension + mariages + gîte) a un EBITDA proche de zéro (B : −7 k€ en année 5 ; A : −40 k€). Aucune dette ne peut être servie. Tous les montages endettés (A, B, club deal, crédit-vendeur, E central) sont **NON VIABLES**. Je les **élimine**.
2. Le seul diagnostic « sans dette » avec dirigeant payé (B_sans_dette) est lui aussi NON VIABLE (−127 k€). **Le domaine type ne se paie pas lui-même s'il paie quelqu'un pour le faire tourner.**
3. Les verdicts « VIABLE seulement avec dirigeant bénévole » (C central, C négocié, C optimiste et le diagnostic B frugal sans dette) sont **surévalués**. Ils cumulent quatre béquilles : (a) un loyer privé de 18 k€/an encaissé d'un fondateur non payé ; (b) un prix de box situé dans les **10 % les plus chers** hors Île-de-France ; (c) un effectif de soins inférieur au ratio de référence ; (d) une assurance de 7 k€.
4. Chacune de ces corrections, **prise seule**, fait perdre à C central son verdict « VIABLE » : il devient **FRAGILE**, et même NON VIABLE avec un soigneur de plus. Leur combinaison le rend **NON VIABLE** (−195 k€) [CALC].
5. Les propres stress tests du directeur le montrent déjà : **C central et C négocié ne passent aucun des 7 stress tests du modèle** (les 6 du brief et un cumul) : 4 NON VIABLE, 3 FRAGILE.
6. **Erreur de conception majeure de C** : 3,4 M€ de fonds propres (2,6 M€ en C négocié) venant d'une holding **non modélisée**. C'est **5 à 14 fois** ce que l'agent 2 estime réaliste en 2030-2031 (0,2-0,7 M€) [A2 montage 6]. Avec des fonds propres réalistes, C est NON VIABLE (−0,84 M€) [CALC].
7. E allégé est le scénario le moins coûteux (0,63 M€). Mais il est NON VIABLE tel quel, FRAGILE avec 200 k€ de réserve, et **ne réussit aucun des 6 stress tests** (5 NON VIABLE, 1 FRAGILE) [CALC]. Il n'y a ni site identifié, ni sécurité juridique pour une résidence privée.
8. **Benchmarks** : le bien de référence du modèle est Ygrande (03). Son hôtel a été mis en liquidation en 2025 et son haras liquidé pour insuffisance d'actif (clôture 2026) [A7 CE2]. Le modèle est cohérent avec ces échecs, pas avec les rares succès (Strawbridge, Guyot), qui reposent sur un prix d'entrée < 0,5 M€, du travail gratuit et un revenu média.
9. **Notes /100** (détail §6) : A 26-31 · B bancaire 23-29 · club deal 24 · crédit-vendeur 24 · E central 27 · E allégé 37 · C prudent 35 · C central 44 · C négocié 46 · C optimiste 47. **Aucun scénario n'atteint 50.** Les diagnostics sans dette sont notés à part (38-44).
10. **Aucun scénario n'est démontré viable.** Les seules voies qui restent font porter le château par une richesse extérieure (revenus ou holding du fondateur). L'activité équestre n'en finance qu'une partie.
11. Erreurs de modèle à corriger en priorité : loyer privé, fonds propres de C, critère de verdict, prix des pensions, effectif. Viennent ensuite l'assurance, le gros entretien, la valeur de sortie, les indicateurs de dette et la TVA (§5.1-5.2).
12. Biais pessimistes réels mais moins nombreux (§5.5) : écart d'inflation charges/prix, aucune subvention, régime fiscal MH ignoré, mariages prudents. Un test « haut » (18 mariages + indexation à 2,5 %) rend C robuste. L'incertitude joue dans les deux sens ; les biais optimistes sont plus nombreux et mieux documentés.

---

## 1. Méthode

- **Lu intégralement** :
  - `01_OPPORTUNITES/*` ;
  - `02_BENCHMARK/Modeles_equestres.md`, `Activites_complementaires.md`, `Domaines_remarquables.md` ;
  - `03_FINANCEMENT/*` ;
  - `05_AUDIT/Cadre_juridique_fiscal.md` ;
  - `hypotheses.py` (316 lignes) et `build_model.py` (482 lignes) ;
  - `comparaison.txt` et le classeur recalculé (détail annuel des feuilles B_central, C_central, B_frugal_sans_dette, E_allege).
- **Banc d'essai indépendant** :
  - copie du modèle dans un dossier personnel du scratchpad (empreintes SHA-256 identiques aux fichiers du projet) ;
  - **50 variantes** générées avec la fonction `build_scenario` d'origine, puis recalculées par LibreOffice ;
  - les 7 feuilles de référence reproduisent **à l'euro près** les résultats du directeur (vérifié), ce qui confirme que mes écarts viennent des hypothèses testées et non d'un calcul différent ;
  - **aucun fichier du projet ni d'un autre agent n'a été modifié**.
- **Recherches** : 15 recherches web sur 20 autorisées, pour chercher des preuves contraires. Pages lues via curl quand c'était possible. Les extraits non confirmés sont signalés [EX].
- **Échelle des risques** :
  - probabilité P de 1 (rare) à 5 (quasi certain) ;
  - impact I de 1 (gêne) à 5 (perte du domaine ou du projet) ;
  - **rédhibitoire** = impact fatal qu'aucune parade réaliste ne neutralise dans le périmètre du scénario.

---

## 2. Registre des risques (classé par probabilité × impact)

| # | Risque | Scénarios touchés | Mécanisme et preuve | P | I | P×I | Rédhibitoire ? | Parade | Statut |
|---|---|---|---|---|---|---|---|---|---|
| R1 | **L'exploitation ne porte pas le château si le dirigeant est payé** | Tous | EBITDA an 5 : A −40 k€, B −7 k€ ; B sans dette NON VIABLE (−127 k€). Benchmarks : Ygrande (EBE −0,10 à +0,06 M€ pour ≈1,1 M€ de CA, puis liquidations), Hus (EBE cumulé −15,8 M€), La Cense (EBE −0,3 M€), Mercuès (résultat ≈ 0 pour 2 M€ de CA) [A7] | 5 | 5 | **25** | **OUI** pour tout montage avec dette | Financement extérieur du château (revenus ou holding du fondateur) ; dirigeant payé hors domaine | Modèle + [PL] A7 |
| R2 | **Dette bancaire non obtenable** | A, B, B crédit-vendeur, E | LTV ≈ 70 % jugée trop élevée par l'agent 2 [A2 montage 1]. DSCR minimal de −1,06 (A prudent) à 0,31 (A frugal). L'agent 2 exige ≈ 300 k€ d'EBITDAR pour le montage 1 ; le modèle en donne −7 à +73 k€ | 5 | 5 | **25** | **OUI** | Apport couvrant ≥ 85-90 % des emplois | Modèle + [PL] A2 |
| R3 | **Fonds propres de la holding (C) non constitués d'ici 2031** | C (tous cas) | Hypothèse de 3,4 M€ (2,6 M€ négocié). L'agent 2 estime 50 k€/an de cash libre pour une reprise d'1 M€, soit ≈ 0,2-0,25 M€ fin 2030, plus ≈ 0,45 M€ mobilisables par refinancement [A2 montage 6]. Stress RetraitFP50 → NON VIABLE | 5 | 5 | **25** | **OUI** pour C tel que défini | Modéliser la holding ; viser un bien bien moins cher ; décaler l'achat | [PL] A2 + modèle |
| R4 | **Perte de contrôle dans le club deal** | B club deal | Fondateur à 18 % du capital et 10 % des votes ; majorité, veto et sortie forcée (drag-along) des investisseurs [A2 montage 2]. Le bail commercial ne protège pas la résidence | 5 | 4 | **20** | **OUI** (contraire à l'objectif « posséder ou contrôler durablement ») | Aucune dans ce montage | [PL] A2 |
| R5 | **Subvention personnelle cachée du fondateur** | C, B frugal, A frugal, E | Ventilation détaillée à la ligne suivante | 4 | 5 | **20** | OUI faute de revenu extérieur | Revenu extérieur documenté, ou dirigeant payé dans le modèle | Modèle + [CALC] |
| | ↳ détail de R5 | | **Loyer privé** : le fondateur paie 18 k€/an indexés (≈ 202 k€ sur 10 ans) alors qu'il n'est pas rémunéré.<br>**Travail gratuit** : ≈ 35 k€/an chargés (≈ 357 k€ sur 10 ans).<br>**Sans loyer privé** : C central passe FRAGILE (trésorerie an 10 : 69 k€ ; DSCR 0,73) [CALC] | | | | | | |
| R6 | **Fondateur seul surchargé, accident** (personne-clé) | C, E, variantes frugales, A frugal | 54 équidés pour 1 ETP + extras + fondateur, contre une référence de 17-20 équidés par ETP [A3 H13]. Le fondateur porte aussi les mariages (≈ 25 h par mariage [A4]), le gîte, le commercial et le parc. Secteur « entraînement, dressage, haras » : **1er taux de fréquence d'accidents du travail des salariés agricoles, 74,7 contre 25 tous secteurs** (moyenne 2019-2023) [A8-10, PL]. Avec +1 ETP, C passe NON VIABLE [CALC] | 4 | 5 | **20** | Non (mitigable, mais la parade détruit la viabilité de C) | +1 ETP ; assurance homme-clé ; remplaçant formé | [PL] + [CALC] |
| R7 | **Prix de pension surestimés et demande locale insuffisante en zone rurale** | Tous | Annuaire de 402 tarifs [A3 S16], recalculé par l'auditeur [A8-12]. **Hors Île-de-France** (Centre, Pays de la Loire, Normandie) : box ou box + paddock médiane **375 € TTC**, 3e quartile 438 €, **10 % des offres ≥ 520 €** (prix du modèle). Pension travail : médiane 535 €, 3e quartile 612 €, 17 % ≥ 656 € (prix de A). À 420 € TTC, C passe FRAGILE [CALC]. Les clients de pension viennent monter souvent : la zone de chalandise est locale [EST], or les châteaux bon marché sont isolés (Ygrande à 3 h 45 de Paris [A1]) | 4 | 4 | **16** | Non | Pré-contrats ; site à ≤ 45 min d'un bassin cavalier | [PL] + [CALC] + [EST] |
| R8 | **Travaux sous-évalués** | A, B, C | Ventilation détaillée à la ligne suivante | 4 | 4 | **16** | Non | Diagnostic d'architecte du patrimoine avant l'offre + 30 % d'aléas | [EST] + modèle |
| | ↳ détail de R8 | | **Restauration** : 500 k€ achetés sans visite pour un château d'≈1 500 m² + dépendances, soit ≈ 330 €/m², bas de la fourchette « rafraîchissement » (300-600 €/m²) [A1 §8].<br>**Salle ERP + gîte** : 250 k€ dans le modèle, 550 k€-1,2 M€ selon l'agent 4 [A4 §13.2].<br>**Toiture** : ardoise naturelle 95-145 €/m² posée en maison courante [A8-09, PL] ; un château coûte plus (échafaudages, charpente, ABF) [INC].<br>Le stress Travaux +30 % du directeur rend déjà C NON VIABLE | | | | | | |
| R9 | **Mur de refinancement des obligations in fine** | B crédit-vendeur (500 k€ en an 6), E (400 k€ en an 7) | Remboursement d'un bloc par une exploitation sans cash-flow libre démontré [A2 §6] | 4 | 4 | **16** | Non (mais aggrave R2) | Ne pas émettre | Modèle |
| R10 | **Clause résolutoire ou hypothèque légale du vendeur** : reprise du château après les travaux | B crédit-vendeur | C. civ. 1654 et 2402 [A6 §11]. Le vendeur et la banque ne peuvent pas être tous deux au 1er rang | 3 | 5 | **15** | Non (négociable) | Plafonnement, délai de grâce, accord de rang | [PL] A6 |
| R11 | **Blocage d'urbanisme ou d'ERP** | B, C, E | Changement de destination soumis à l'avis conforme CDPENAF/CDNPS ; ABF dans les abords ; une soirée dansante peut faire basculer la salle en type P (seuil 5e catégorie : 120 personnes) [A4 §2.4, A6 §6-7]. Mariages, gîte, séminaires et tournages = **34 % du CA de B** | 3 | 4 | **12** | Non | Certificat d'urbanisme opérationnel et lecture du PLU avant l'offre | [PL] A4, A6 |
| R12 | **SAFER** : préemption partielle des terres, cahier des charges | Tous ; E en particulier | Préemption partielle possible (L.143-1-1). Droit d'opposition sur les baux emphytéotiques de terres agricoles depuis le 20/08/2026 (L.451-1-1) [A6 §10] | 3 | 4 | **12** | Non | Candidature à la rétrocession avec un projet agricole équestre | [PL] A6 |
| R13 | **Bail rural non voulu** | Montages PropCo/OpCo, club deal, location à un cavalier pro | Statut d'ordre public. Toute mise à disposition onéreuse pour une activité équestre agricole en relève (L.411-1). Le loyer est alors plafonné par arrêté (bâtiments 0,29-4,94 €/m²/an dans l'Orne [A4 §8.2]). **Cela rend illusoire le loyer de 190-200 k€/an** qu'une OpCo équestre verserait à la PropCo [A2 montage 1] | 3 | 4 | **12** | Non | Exploitation directe ; contrats de prestation | [PL] A6, A4 |
| R14 | **Logement privé dans un bail emphytéotique d'intérêt général ; résiliation politique ; réversion des travaux** | E | Le BEA (CGCT L.1311-2) vise une mission de service public ou une opération d'intérêt général : une résidence privée s'y prête mal [EST, à valider]. Cas Valmer : bail résilié en 2022 [A2]. En fin de bail, les améliorations reviennent au bailleur | 3 | 4 | **12** | Potentiellement | Bail de droit commun sur le domaine privé de la collectivité [EST] ; clauses de résidence et d'indemnisation | [EST] |
| R15 | **Illiquidité de la sortie** | Investisseurs, fondateur | Haras de Hus en vente depuis 2020, de 21,2 M€ à 12,9 M€ (ce dernier prix en EX) [A7 CE1]. Annonces dupliquées avec 5 % d'écart [A1 §7] | 4 | 3 | **12** | Non | Horizon de détention ≥ 15 ans ; pas d'investisseur exigeant une sortie | [PL]/[EX] |
| R16 | **Conflit entre vie privée et exploitation** | B, C, E | Jusqu'à 54 propriétaires de chevaux sur le site (ESTIMATION : surtout le soir et le week-end), 12 week-ends de mariage, un gîte de 15 personnes, des équipes de tournage de 30 à 80 personnes [A4]. Contraire à la « résidence privée indépendante » du brief | 5 | 2 | **10** | Non | Accès séparés ; plafonds d'événements | [PL] A4 + [EST] |
| R17 | **Taxe CGI 235 ter C** : 20 % par an de la valeur du logement privé | C si la holding à l'IS détient le château ; club deal mal structuré | Trois conditions cumulées : actifs ≥ 5 M€, contrôle ≥ 50 %, revenus passifs > 50 % [A6 §3]. Une holding de PME (dividendes) qui détient aussi le château remplit les trois [EST]. Commentaires BOFiP non publiés en avril 2026 [A8-11, EX] | 2 | 5 | **10** | Potentiellement | SCI à l'IR, société active ou loyer de marché | [PL] A6 |
| R18 | **Requalification de la TVA à 20 %** (pensions box et pré) | A, B, C, E | Le taux de 5,5 % exige une pension indissociable de la pratique ; la pension « simple » relève de 20 % [A3 §7, A6 §9]. Le modèle applique 5,5 % aussi au pré. À 20 %, C passe FRAGILE [CALC] | 3 | 3 | **9** | Non | Contrats « pension + accès aux installations » ; rescrit | [PL] + [CALC] |
| R19 | **Abus de biens sociaux, acte anormal de gestion** (logement, énergie privée, chevaux personnels) | Tous | Les charges de la partie privée (énergie, assurance, taxes) sont portées par la société. Les chevaux du fondateur ne sont pas modélisés [A6 §3] | 3 | 3 | **9** | Non | Loyer de marché expertisé ; refacturation ; convention réglementée | [PL] A6 |
| R20 | **Assurance sous-estimée** | Tous | 7 k€ dans le modèle. Un courtier spécialisé annonce 15-30 k€/an pour 600-1 200 m², soit 0,5 % de la valeur assurée, et +30 à 60 % en usage commercial [A8-03, PL, source commerciale]. À 15 k€, C passe FRAGILE [CALC] | 4 | 2 | **8** | Non | Devis de 2 assureurs spécialisés | [PL] fiabilité faible-moyenne |
| R21 | **Sécheresse et fourrage** ; surchargement | Tous | Pousse des prairies **−33 % au 10/08/2026** par rapport à 1989-2018 ; stocks épuisés [A8-07, PL]. Foin à plus de 200 €/t en 2026 [A8-08, EX]. Le modèle met 54 équidés et 10 ha loués sur un domaine de 40-50 ha (Ygrande : 27 ha de pâtures). Cela fait 1,6 à 2 équidés/ha, contre 0,6-1,2 en référence [A3 H29] | 4 | 2 | **8** | Non | Stock tampon ; contrats d'achat de foin ; 45 équidés au plus | [PL] + [EST] |
| R22 | **Dépendance à quelques acteurs** | A (cavalier pro), E (bailleur), B crédit-vendeur (vendeur) | La pension travail et les gains de compétition de A dépendent d'un seul cavalier. E dépend d'un seul bailleur public | 3 | 3 | **9** | Non | Contrats longs ; deuxième cavalier | [EST] |
| R23 | **Hausse des taux** | Scénarios endettés | Stress +2 points : C central passe FRAGILE (DSCR 1,19) | 3 | 3 | **9** | Non | Taux fixe | Modèle |
| R24 | **Gros entretien ponctuel** (toiture, menuiseries) | Tous | Demeure Historique : **au moins 40 k€/an** d'entretien courant d'un monument, hors restauration (assurance, impôts locaux, gardien, entretien minimum) [A8-04, PL, 2019]. Le modèle en couvre l'ordre de grandeur, mais lisse sur 1,2 % du prix d'achat un risque très irrégulier | 3 | 3 | **9** | Non | Provision 1,5-2 % ; diagnostic de toiture | [PL] |
| R25 | **Conformité équestre** | Tous | Diplôme pour enseigner (1 an d'emprisonnement et 15 000 €), SIRE, MSA, contrôle des structures pour un pluriactif [A6 §9] | 2 | 3 | **6** | Non | Enseignant diplômé ; démarches | [PL] A6 |
| R26 | **Saisonnalité** | B, C, E | 68 % des mariages entre mai et septembre [A4] ; foin acheté l'été. Le modèle est annuel et ne voit pas les creux intra-annuels | 5 | 1 | **5** | Non | Réserve ≥ 150 k€ | [PL] A4 |
| R27 | **Prêts d'honneur traités en fonds propres** | B crédit-vendeur, E | Ce sont des prêts personnels remboursables sur 1 à 7 ans [A2 §1.3] | 5 | 1 | **5** | Non | Les modéliser comme dettes du fondateur | [PL] A2 |

**Lecture.** Les quatre risques rédhibitoires (R1-R4) suffisent à éliminer tous les montages endettés et le club deal. R3 et R5 touchent le cœur du scénario C : son verdict « VIABLE » repose sur de l'argent non démontré (holding) et sur une subvention personnelle non financée (loyer privé + travail gratuit).

---

## 3. Objections par scénario

### 3.1 Scénario A — château équestre « sport » (bancaire, apport 1 M€ ; prudent, optimiste, frugal)
- **Le modèle donne** : NON VIABLE dans les quatre cas. Trésorerie an 10 entre −1,5 M€ (frugal) et −3,9 M€ (prudent). DSCR minimal ≤ 0,31.
- **Objections supplémentaires**, qui aggravent le constat :
  - **Prix** : la pension travail à 656 € TTC est au-dessus du 3e quartile hors Île-de-France (612 €). Seulement 17 % des offres l'atteignent [CALC sur A3 S16].
  - **Volumes** : remplir 20 places de travail sans cavalier connu, en zone rurale, n'est pas démontré [EST].
  - **Valorisation** : 3 jeunes chevaux par an supposent un **stock de chevaux** (≈ 3 × 16,8 k€ d'achat, immobilisés 1 à 2 ans) absent du BFR. Il faut y ajouter le risque de blessure ou de vice caché [A3 §8 n°5].
  - **Gains de compétition** (12,25 k€) : ils supposent un cavalier de niveau pro. Dans A frugal, ce cavalier est le fondateur bénévole, ce qui cumule les risques R5 et R6.
  - **Ventes privées B2B** : tarif INCONNU [A3 §8 n°10].
  - **Benchmarks contraires** : le sport et l'élevage haut de gamme perdent de l'argent même adossés à une fortune (Hus, EBE négatif 10 années sur 10 ; La Cense) [A7].
- **Test de l'auditeur** : A frugal financé sans dette (3,9 M€ de fonds propres) est « VIABLE bénévole » (trésorerie an 10 : 736 k€). A sans dette mais dirigeant et cavalier payés est NON VIABLE (−471 k€) [CALC]. L'économie de A repose donc entièrement sur un fondateur qui est à la fois cavalier professionnel, chef d'écurie et gérant, sans salaire.
- **Avis de l'auditeur** : **ÉLIMINÉ** dans toutes ses variantes de financement.

### 3.2 Scénario B — multiactivité (bancaire, apport 1 M€ ; prudent, optimiste, frugal)
- **Le modèle donne** : NON VIABLE partout. Trésorerie an 10 de −1,62 M€ (frugal) à −3,50 M€ (prudent). Même l'optimiste (−1,67 M€) ne sert pas sa dette (DSCR 0,21).
- **Objections** :
  - Prix de box dans le décile le plus cher hors Île-de-France (R7).
  - Effectif de soins à 27 équidés par ETP (R6).
  - Assurance à 7 k€ (R20).
  - Activités soumises à urbanisme et ERP (R11).
  - Vie privée incompatible avec 54 clients, 12 mariages et un gîte (R16).
  - **Écart entre vision et modèle** : un jardinier (un demi en frugal) pour un parc « parfaitement entretenu » et 40-50 ha. La vision du brief (allées, haies, pelouses impeccables) coûterait 1 à 3 ETP de plus [EST]. Le modèle finance un domaine **entretenu**, pas un domaine **de prestige**.
  - **Cohérence avec les benchmarks** (point positif) : les activités non équestres apportent ≈ 50 k€ de contribution, comme le calcule l'agent 4. Elles couvrent moins de la moitié des charges structurelles, ce qui est cohérent [A4 §1].
- **Avis** : **ÉLIMINÉ** (B central, prudent, optimiste, frugal bancaire).

### 3.3 B — club deal (apport 250 k€, investisseurs 1,64 M€, dette 1,8 M€)
- **Le modèle donne** : NON VIABLE (−1,64 M€). TRI des investisseurs : « perte quasi totale ». Fondateur : 18 % du capital, 10 % des votes.
- **Objections** :
  - **Aucun investisseur rationnel** : rendement en cash ≈ 3 % selon l'agent 2, contre 8,7 % de TRI net affiché par Anaxago ou 3,7 % pour de la dette bancaire [A2 §5].
  - **Liquidité** : sortie forcée après 10-12 ans sur un actif illiquide (R15).
  - **Perte de contrôle** (R4) : la majorité peut vendre le château où vit le fondateur.
  - **Réglementation** : moins de 150 investisseurs non qualifiés, risque de requalification en FIA [A6 §11].
  - **Bail rural** entre la PropCo des investisseurs et l'OpCo équestre : loyer plafonné, ce qui détruit leur rendement (R13).
  - **Variante frugale** testée : toujours NON VIABLE (−0,90 M€) [CALC].
- **Avis** : **ÉLIMINÉ**. Le montage est contraire à l'objectif de contrôle et sans attrait pour les investisseurs.

### 3.4 B — crédit-vendeur (apport 330 k€ dont 80 k€ de prêts d'honneur ; crédit-vendeur 1,5 M€ ; banque 1,1 M€ ; obligations 0,5 M€)
- **Le modèle donne** : NON VIABLE (−3,83 M€), l'un des pires résultats du classeur (seul A prudent fait pire, −3,92 M€).
- **Objections** :
  - **Conditions hors marché**. La pratique observée est la suivante [A8-05, A8-06, PL] :
    - crédit-vendeur couvrant ≈ 30 % (au plus 50 %) du prix ;
    - durée de 1 à 5 ans le plus souvent ;
    - taux égal ou supérieur à celui des banques.
    
    Le modèle suppose **60 % du prix, 12 ans, 3 %**, soit moins cher que la banque. Aucun cas de château vendu ainsi n'a été trouvé, ni par l'agent 2, ni par l'auditeur [EX].
  - **Rang des garanties** : la banque des travaux et le vendeur (hypothèque légale) se disputent le 1er rang (R10).
  - **Mur de refinancement** : 500 k€ d'obligations à rembourser en année 6 (R9).
  - **Prêts d'honneur** comptés en fonds propres (R27).
  - **Le montage ne boucle pas**, de l'aveu même de l'agent 2 : écart de 400 k€ [A2 montage 3].
  - **Variante frugale** testée : −3,08 M€ [CALC].
- **Avis** : **ÉLIMINÉ**.

### 3.5 Diagnostics sans dette (3,9 M€ de fonds propres)
Ce ne sont pas des scénarios finançables : 3,9 M€ dépassent le plus haut scénario d'apport du brief (1 M€). Ils servent à isoler l'économie de l'exploitation.

- **B_sans_dette (dirigeant payé)** : NON VIABLE (−127 k€). **C'est le diagnostic le plus important du classeur.** Sans dette, avec un dirigeant payé 35 k€ chargés, le domaine type ne couvre pas son gros entretien.
- **B_frugal_sans_dette** : « VIABLE bénévole » au modèle (trésorerie an 10 : 620 k€). Mes tests :

| Correction testée | Trésorerie an 10 | Verdict |
|---|---|---|
| Loyer privé retiré | 419 k€ | toujours VIABLE |
| +1 ETP de soins | 314 k€ | toujours VIABLE |
| **Les deux corrections** | 113 k€, cash-flow libre négatif 8 années | **FRAGILE** |
| **Cas d'audit combiné** (§5.6) | −3 k€ | **NON VIABLE** |

  - **TRI du fondateur** : −1,3 % au modèle, −2,1 % si la valeur de sortie exclut le gros entretien capitalisé, −2,75 % si l'on compte le loyer qu'il paie [CALC].
  - **Coût caché** : ≈ 0,56 M€ sur 10 ans (loyer 0,20 M€ + travail non payé 0,36 M€).
- **Conclusion des diagnostics** : l'exploitation type ne crée pas de valeur financière. Elle **réduit** le coût de possession d'un château, elle ne le **finance** pas.

### 3.6 Scénario C — « le capital d'abord » (achat en 2031 avec les fonds propres d'une holding)

| Cas | Modèle | Stress du directeur (7 tests) | Objection principale de l'auditeur |
|---|---|---|---|
| C central | VIABLE bénévole ; trésorerie an 10 : 196 k€ ; DSCR minimal 1,40 ; TRI fondateur −4,8 % | **0 test réussi** : 4 NON VIABLE (CA −30 %, travaux +30 %, retrait de 50 % des fonds propres, cumul), 3 FRAGILE | Une seule correction suffit à le faire basculer (§5.6). 3,4 M€ de holding non démontrés |
| C négocié | VIABLE bénévole ; trésorerie an 10 : 269 k€ | **0 test réussi** (4 NON VIABLE, 3 FRAGILE) | Combinaison prix −20 % et travaux −30 % non prouvée : un vendeur en difficulté laisse en général **plus** de travaux différés. L'exemple cité, Ygrande, est affiché à 2,65 M€, au-dessus de la base de 2,5 M€ [A1] |
| C prudent | NON VIABLE (−626 k€) | — | Montre que C n'a pas de marge de sécurité |
| C optimiste | VIABLE bénévole ; trésorerie an 10 : 635 k€ | — | Volumes +15 % et prix +8 % appliqués à des prix déjà dans le décile le plus cher : improbable |

**Objections de fond :**
1. **La source des fonds n'existe pas dans le modèle (R3).** `hypotheses.py` l.140 écrit lui-même « un LBO de ~1 M€ ne libère que ~50 k€/an [A2 montage 6] », puis suppose 3,4 M€. Cela représente 5 à 14 fois l'estimation de l'agent 2 pour 2030-2031.
   - Avec 0,95 M€ de fonds propres réalistes (0,25 M€ d'apport + ≈ 0,7 M€ de holding) et le solde en dette : **NON VIABLE, −0,84 M€** [CALC].
   - Selon le scénario d'apport : impossible avec 50 k€ (le CRA conseille la franchise sous 100 k€ [A2 §1.6]) ; ≈ 0,7 M€ au mieux avec 250 k€ ; peut-être 1,5-2,5 M€ avec 1 M€, et seulement avec une reprise de 3-5 M€ performante ou cédée [EST].
2. **Le fondateur ne peut pas tout faire.** Jusqu'en 2030, il dirige une ou plusieurs PME sous LBO. À partir de 2031, il est soigneur et gérant bénévole, et paie 18 k€ de loyer. Qui dirige alors la holding, et de quoi vit le fondateur ? Le modèle ne le dit pas [A2 : « diriger une PME et lancer un domaine en même temps n'est pas compatible »].
3. **Le château détenu par la holding à l'IS** expose le logement privé à la taxe 235 ter C : 20 % par an (R17).
4. **Point fort réel** : c'est le seul scénario où le fondateur garde 100 % du contrôle avec peu de dette, et où l'achat peut attendre la preuve du capital. **Si** le capital existait, C serait la meilleure structure. D'où une note supérieure à celle des autres (§6), mais sous 50.
- **Avis** : **NON DÉMONTRÉ, à reconstruire** (non éliminé). Le verdict « VIABLE » doit devenir « FRAGILE, conditionné à des fonds propres non démontrés ».

### 3.7 Scénario E — bail emphytéotique (central : 1,5 M€ de travaux) et E allégé (0,6 M€)
- **E central** : NON VIABLE (−1,17 M€).
  - 900 k€ de dette hypothéquée sur un droit réel, que le bailleur public doit autoriser.
  - 400 k€ d'obligations remboursées en une fois en année 7.
  - Aucune valeur de sortie (réversion au bailleur).
  - **Avis : ÉLIMINÉ.**
- **E allégé** : NON VIABLE tel que modélisé (trésorerie minimale −123 k€). La raison principale : aucune réserve pour absorber les pertes des années 1-2. Mes tests [CALC] :
  - avec 200 k€ de réserve : FRAGILE (trésorerie an 10 : 138 k€ ; DSCR 0,75 en 2e année d'exploitation) ;
  - avec réserve et sans loyer privé : NON VIABLE ;
  - **stress du brief avec réserve** : CA −30 % → −505 k€ ; travaux +30 % → −118 k€ ; retard de 12 mois → minimum −44 k€ ; annulation de 40 % des événements → −17 k€ ; cumul → −426 k€ ; taux +2 points → FRAGILE. **Aucun des 6 tests n'est réussi (5 NON VIABLE, 1 FRAGILE).**
- **Objections spécifiques à E** :
  1. **Aucun site identifié.** Aucun appel à projets actif trouvé [A2 montage 4]. Les exemples sont des baux entre personnes publiques (Gaillon, Neuenbourg) [A2, A8 : recherche sans cas d'un particulier logé].
  2. **Résidence privée juridiquement fragile** dans un BEA d'intérêt général (R14). La SAFER peut s'opposer depuis 2026 si les terres sont agricoles (R12).
  3. **Sélection adverse** : « site public déjà entretenu » (`hypotheses.py` l.277) est une hypothèse favorable. Une collectivité confie d'abord les sites qu'elle n'a pas les moyens de restaurer [EST].
  4. **Sourcing** : la redevance de 20 k€ s'appuie sur des exemples « PL v1 » (`hypotheses.py` l.259). La version 1 est **exclue comme source** par `CONTEXTE_PERMANENT.md`. Statut correct : INCONNU, de 1 €/an à 80 k€ + 7 % du CA.
  5. **Subvention implicite** : en E central, 0,3 M€ de subventions publiques sont déduits des travaux (l.264). C'est contraire à la règle « aucune subvention acquise ».
  6. **Entretien** : le preneur d'une emphytéose supporte toutes les réparations, grosses et menues [EST, art. L.451-8 c. rural, non relu ici]. L'assiette du gros entretien doit couvrir **tout le château**, pas seulement les travaux.
- **Avis** : E central **ÉLIMINÉ**. E allégé **NON DÉMONTRÉ** : piste à documenter (site, statut juridique de la résidence, redevance), pas un plan.

---

## 4. Scénarios éliminés et scénarios maintenus sous condition

| Scénario | Statut auditeur | Justification chiffrée |
|---|---|---|
| A central, prudent, optimiste | **ÉLIMINÉ** | Trésorerie an 10 de −2,0 à −3,9 M€ ; DSCR ≤ 0,02 ; EBITDA an 5 négatif sauf optimiste (+36 k€) ; dette inaccessible (R1, R2) |
| A frugal (bancaire) | **ÉLIMINÉ** | −1,50 M€ ; DSCR 0,31 ; fondateur à la fois cavalier pro et soigneur bénévole |
| B central, prudent, optimiste, frugal (bancaire) | **ÉLIMINÉ** | −1,62 à −3,50 M€ ; DSCR ≤ 0,23 |
| B club deal | **ÉLIMINÉ** | −1,64 M€ ; investisseurs en perte quasi totale ; fondateur à 10 % des votes (R4) |
| B crédit-vendeur | **ÉLIMINÉ** | −3,83 M€ ; conditions hors marché ; montage qui ne boucle pas (−400 k€) |
| E central | **ÉLIMINÉ** | −1,17 M€ ; pas de valeur de sortie ; doute juridique sur la résidence |
| C prudent | Indicateur de fragilité, NON VIABLE | −626 k€ |
| C central, C négocié, C optimiste | **NON DÉMONTRÉ** (à reconstruire) | 0 stress test réussi sur 7 ; basculent sur une seule correction ; fonds propres de holding non modélisés et 4 à 14 fois l'estimation de l'agent 2 |
| E allégé | **NON DÉMONTRÉ** (piste) | NON VIABLE sans réserve ; FRAGILE avec ; aucun des 6 stress réussi (5 NON VIABLE) ; pas de site |
| B sans dette, B frugal sans dette (diagnostics) | Hors financement (3,9 M€) | Le premier montre que l'exploitation ne paie pas de dirigeant ; le second ne survit pas au cas d'audit combiné |

---

## 5. Critique du modèle

### 5.1 Erreurs et simplifications à corriger EN PRIORITÉ (elles changent les verdicts)

| # | Problème | Où | Effet mesuré [CALC] | Sens | Correction proposée |
|---|---|---|---|---|---|
| M1 | **Loyer privé encaissé alors que le fondateur n'est pas payé.** Il gonfle le résultat, le flux d'exploitation, la trésorerie, le **DSCR** (numérateur) et la « dette soutenable », sans aucune source de financement modélisée | `build_model.py` l.276-277, 326, 342, 359-361 ; `hypotheses.py` l.43 | C central : de VIABLE à **FRAGILE** (trésorerie an 10 : 196 → 69 k€ ; DSCR 1,40 → 0,73 ; 4 années de cash-flow libre négatif). C négocié : FRAGILE. Dette soutenable de C : 531 → 276 k€ | Optimiste | Si `dirigeant_paye = 0`, mettre le loyer à 0 ou ajouter un bloc « budget personnel du fondateur » (revenu extérieur ≥ loyer + coût de vie). Compter le loyer comme un flux du fondateur dans son TRI. L'exclure du DSCR bancaire |
| M2 | **Fonds propres de C (3,4 M€ ; 2,6 M€ négocié) non modélisés**, contredits par la source citée | `hypotheses.py` l.139-140, 253 | Avec 0,95 M€ de fonds propres et le solde en dette : **−0,84 M€, NON VIABLE** | Optimiste | Modéliser la holding (cash-flow du LBO 2026-2030, covenants, nantissements) ou fixer les fonds propres à une valeur sourcée (0,2-0,7 M€) et afficher le **trou de financement** |
| M3 | **Le verdict ignore la destruction de valeur et la subvention du fondateur.** « VIABLE » coexiste avec un TRI fondateur négatif partout (−1,3 % à −4,8 %) et avec ≈ 55-60 k€/an de soutien personnel | `build_model.py` l.416-422 | — | Optimiste (présentation) | Ajouter deux critères : valeur des fonds propres an 10 ≥ fonds propres investis (ou TRI fondateur ≥ 0) et subvention personnelle affichée. Renommer « VIABLE seulement avec dirigeant bénévole » en **« NON AUTOFINANCÉ — porté par le fondateur »** |
| M4 | **Prix de pension dans le haut de la distribution** : box 520 € TTC (10 % des offres hors Île-de-France ; médiane 375 €, 3e quartile 438 €) ; pré 230 € (37 % des offres) ; travail 656 € (17 % des offres). Occupation de 92 % dès l'année 3, sans donnée publiée [A3 H7] | `hypotheses.py` l.66-69, 111-112 | Box à 420 € TTC : C passe **FRAGILE** (trésorerie an 10 : 73 k€ ; DSCR 0,75) | Optimiste | Base au 3e quartile régional (≈ 440-450 € TTC) ; le premium devient une variante « hausse » conditionnée à des pré-contrats ; occupation à 85 % sans pré-contrats |
| M5 | **Effectif de soins sous-dimensionné**, avec 7 j/7 et congés à couvrir : 2 ETP pour 54 équidés (27 par ETP) ; 1 ETP + extras + fondateur en frugal ; référence 17-20 équidés par ETP [A3 H13] ; risque d'accident du travail 3 fois la moyenne [A8-10] | `hypotheses.py` l.91, 185 | +1 ETP (30 k€) : C passe **NON VIABLE** (−16 k€) ; C négocié FRAGILE | Optimiste | Dimensionner sur la référence, fondateur compris pour 0,5 ETP au plus ; ligne « remplacements » |

### 5.2 Corrections importantes (P2 : ensemble, elles font basculer les cas limites)

| # | Problème | Où | Effet / preuve | Sens | Correction |
|---|---|---|---|---|---|
| M6 | **Assurance à 7 k€** pour un château d'≈1 000-1 500 m² avec usage commercial | `hypotheses.py` l.85 | Courtier spécialisé : 15-30 k€/an, +30 à 60 % en usage commercial [A8-03, PL, source commerciale]. À 15 k€, C passe FRAGILE (DSCR 1,10) | Optimiste | 12-20 k€ en central [EST] ; devis |
| M7 | **Gros entretien = 1,2 % de (prix d'achat + travaux)**. Le prix d'achat d'un château est très inférieur à sa valeur de reconstruction [A4 §11 : 0,6 M€ d'achat pour 6 M€ de reconstruction] ; aucun choc ponctuel | `build_model.py` l.286-287 | À 2 % : C passe FRAGILE (DSCR 0,42). Demeure Historique : ≥ 40 k€/an hors restauration [A8-04] | Optimiste | 1,5-2 % + stress « toiture » ponctuel (200-400 k€ [EST]) |
| M8 | **La valeur de sortie inclut le gros entretien capitalisé.** C'est de la maintenance, pas une création de valeur | `build_model.py` l.288-290, 371 | TRI fondateur : B frugal sans dette −1,3 % → −2,1 % ; C −4,8 % → −5,7 % | Optimiste | Assiette = prix + travaux initiaux, ou valeur de marché |
| M9 | **Indicateur « dette soutenable » trop indulgent** : calculé sur l'EBITDA de l'**année 10** (indexé, à maturité) avec le loyer privé et sans IS ; **le DSCR minimal exclut la 1re année d'exploitation** (C an 5 : −2,02) | `build_model.py` l.394-395, 402-403 | C : 531 k€ affichés, 276 k€ sans loyer privé | Optimiste | EBITDA moyen des années 2-4 sans loyer privé ; DSCR sur toutes les années portant un service de dette |
| M10 | **TVA « neutre » à tort** : travaux de la partie privée (TVA non récupérable) ; gîte exonéré (meublé sans prestations para-hôtelières [A4]), donc TVA non déductible sur son capex ; préfinancement du crédit de TVA (≈ 180 k€ sur 0,9 M€ de travaux) absent du BFR | `hypotheses.py` l.7 | ≈ 30-70 k€ de surcoût définitif [EST] + besoin de trésorerie temporaire | Optimiste | Part de TVA non récupérable ; décalage du remboursement de crédit de TVA |
| M11 | **Prêts d'honneur (80 k€) comptés en apport** ; **stock de chevaux** absent du BFR dans A | `hypotheses.py` l.218, 266, 115-116 | Faible (A : ≈ 50 k€ immobilisés [EST]) | Optimiste | Dette du fondateur ; BFR « chevaux » |
| M12 | **C négocié : prix −20 % ET travaux −30 %** sans preuve (corrélation inverse probable) | `hypotheses.py` l.248-253 | — | Optimiste | Prix −20 % avec travaux inchangés ou +30 % |
| M13 | **Crédit-vendeur à 60 % du prix, 12 ans, 3 %** : hors pratique de marché (30-50 %, 1-5 ans, taux ≥ banque) | `hypotheses.py` l.221-222 | Scénario déjà NON VIABLE | Optimiste | Aligner sur le marché ; modéliser le rang des garanties |
| M14 | **Sources de E** : redevance « PL v1 » (source interdite) ; 0,3 M€ de subvention publique implicite ; assiette du gros entretien | `hypotheses.py` l.259, 264, 271, 279 | — | Optimiste / règle de sourcing | Redevance [INC] avec fourchette ; travaux sans subvention ; gros entretien sur tout le château |
| M15 | **Chargement en chevaux et fourrage** : 54 équidés + 10 ha loués pour 1,5 k€/an ; le libellé « Fermage » créerait un **bail rural** de 9 ans pour 1 500 €/an [A4 §8.2] | `hypotheses.py` l.78 | Foin acheté non explicité ; stress sécheresse absent | Optimiste (faible) | Bilan fourrager ; libellé « vente d'herbe / convention précaire » ; stress foin (+10-20 k€ [EST]) |
| M16 | **Stress tests incomplets** : appliqués seulement à Cc, Cn et Bfsd. Rien sur E allégé (5 NON VIABLE et 1 FRAGILE sur 6 quand il est doté d'une réserve), ni chocs de coûts (assurance, énergie, foin), ni loyer privé à 0, ni valeur de sortie | `hypotheses.py` l.283-297 | — | Optimiste (par omission) | Ajouter ces stress |

### 5.3 Points mineurs ou latents (P3)

- **M17 — IS** : taux unique de 25 % sans le taux de 15 % jusqu'à 42 500 € [A6 §12]. Biais **pessimiste** mais sans effet, l'IS étant nul partout à cause des déficits et des amortissements. Les déficits sont reportés sans plafond, ce qui est sans effet aux montants en jeu.
- **M18 — Trésorerie négative sans intérêts de découvert** : optimiste pour les scénarios NON VIABLES, sans effet sur le verdict.
- **M19 — Bug latent** : `oc_ech` et `annee_ouv` sont des années absolues. Un scénario à achat tardif (C) avec des obligations rembourserait ou paierait les coupons au mauvais moment. Non déclenché aujourd'hui (C n'a pas d'obligations).
- **M20 — Indexation incohérente dans C** : les travaux sont indexés à 2031 (`idx_c`), pas le prix du château (2,5 M€ nominal en 2031). Effet neutre à incertain.
- **M21 — Modèle annuel** : la saisonnalité intra-annuelle (mariages en mai-septembre, foin l'été) n'apparaît pas. Les creux de trésorerie sont donc sous-estimés.
- **M22 — Coût privé non ventilé** : énergie, assurance et taxes de la partie privée sont portées par la société (voir R19).

### 5.4 Synthèse des biais OPTIMISTES (par ordre d'importance)

1. Fonds propres de C non démontrés (M2).
2. Loyer privé payé par un fondateur non payé (M1).
3. Prix de pension et taux d'occupation (M4).
4. Effectif de soins et parc (M5, écart avec la vision du brief).
5. Travaux achetés sans visite (R8) et assurance (M6).
6. Gros entretien sur le prix d'achat (M7) et valeur de sortie (M8).
7. Indicateurs de dette (M9) et TVA (M10).
8. Montages au-delà des pratiques de marché (M12, M13) et sources de E (M14).

### 5.5 Synthèse des biais PESSIMISTES (à corriger aussi)

1. **Ciseau d'inflation** : charges +2,5 %/an contre prix +2 %/an (`hypotheses.py` l.60). En année 10, l'écart réduit les charges fixes « absorbables » d'≈ 4,5 %, soit ≈ 9-13 k€/an. Défendable (SMIC, énergie), mais à mettre en sensibilité. Un test avec prix à +2,5 % est intégré au test « hausse » (§5.6).
2. **Dette tirée en totalité l'année d'acquisition**, alors que 40 % des travaux sont payés en années 2-3 (`build_model.py` l.349). Cela ajoute ≈ 15-20 k€ d'intérêts [EST].
3. **Aucune subvention ni aide**, ce qui est prudent mais pessimiste :
   - DJA de 25 500 à 47 000 € en Bourgogne-Franche-Comté, mais **projets de « centre ou pension équestre » exclus** dans cette région [A8-01, PL] ; diplôme agricole de niveau 4 exigé ;
   - subventions MH indicatives de 20-40 % des travaux éligibles, mises aux normes exclues [A6 §5] ;
   - majorations FEADER.
   
   Ordre de grandeur possible : 0-200 k€ selon le bien et la région [EST].
4. **Fiscalité personnelle ignorée.** Le régime MH (CGI 156 et 156 bis) permet de déduire 50 % (fermé) à 100 % (ouvert 50 jours par an) des charges foncières du château du **revenu global**. Conditions : bien protégé, détenu en direct ou en SCI à l'IR, conservé 15 ans [A2 §1.5, A6 §5].
   - C'est **le principal mécanisme réel de financement des châteaux privés en France**. Il peut valoir plusieurs dizaines de k€/an à un fondateur fortement imposé [EST].
   - Il est **incompatible avec la société à l'IS** du modèle et avec des investisseurs tiers. Il ne profite qu'à un fondateur à hauts revenus, donc plutôt à C qu'aux scénarios à apport limité.
   - Seuls 2 des 29 biens repérés sont protégés et dans le budget : Saintes (3,57 M€) et Sablé (1,79 M€, 18 ha) [A1].
5. **Mariages prudents** : 12 par an à la médiane du marché, contre ≈ 30 par an à Moliens [A4 §2.3].

**Test « hausse »** [CALC] : 18 mariages à 5 220 € HT + prix indexés à 2,5 %. C central devient confortable (trésorerie an 10 : 401 k€ ; DSCR minimal 2,30). B frugal sans dette atteint 916 k€.

**Conclusion** : l'incertitude est réelle dans les deux sens, et le résultat de C se joue à ± 20-40 k€ d'EBITDA par an. Mais les biais optimistes sont plus nombreux, mieux documentés et touchent des postes plus sûrs (charges, effectif, prix observés) que les biais pessimistes (mariages, subventions non acquises).

### 5.6 Tests de sensibilité de l'auditeur [CALC]

Mode opératoire :
- copie du modèle, 50 variantes, recalcul par LibreOffice ;
- les feuilles de référence R_* reproduisent exactement le tableau du directeur ;
- trésorerie en k€ ; DSCR = minimum à partir de la 2e année d'exploitation.

| Variante | C central : tréso an 10 / DSCR / verdict | C négocié : tréso an 10 / verdict | B frugal sans dette : tréso an 10 / verdict |
|---|---|---|---|
| Référence (modèle du directeur) | 196 / 1,40 / VIABLE bénévole | 269 / VIABLE bénévole | 620 / VIABLE bénévole |
| M1 : loyer privé à 0 | 69 / 0,73 / **FRAGILE** | 142 / **FRAGILE** | 419 / VIABLE bénévole |
| M4 : box à 420 € TTC (médiane régionale) | 73 / 0,75 / **FRAGILE** | 146 / **FRAGILE** | 435 / VIABLE bénévole |
| R18 : pensions box et pré à TVA 20 % | 85 / 0,83 / **FRAGILE** | 158 / **FRAGILE** | 452 / VIABLE bénévole |
| M5 : +1 ETP de soins (30 k€) | −16 / 0,29 / **NON VIABLE** | 57 / **FRAGILE** | 314 / VIABLE bénévole |
| M6 : assurance à 15 k€ | 139 / 1,10 / **FRAGILE** | 212 / **FRAGILE** | 531 / VIABLE bénévole |
| M7 : gros entretien à 2 % | 96 / 0,42 / **FRAGILE** | 192 / **FRAGILE** | 399 / VIABLE bénévole |
| M1 + M5 (loyer 0 et +1 ETP) | — | — | 113 / **FRAGILE** |
| **Cas d'audit combiné** (détail ci-dessous) | **−195 / NON VIABLE** | **−114 / NON VIABLE** | **−3 / NON VIABLE** |
| Hausse : 18 mariages à 5 220 € HT + prix à +2,5 %/an | 401 / 2,30 / VIABLE bénévole | 474 / VIABLE bénévole | 916 / VIABLE bénévole |
| C avec fonds propres réalistes (0,95 M€) et 2,85 M€ de dette | −835 / NON VIABLE | — | — |
| C avec dirigeant payé et effectif normal | −312 / NON VIABLE | — | — |

Le **cas d'audit combiné** retient :
- loyer privé à 0 ;
- box à 450 € TTC ;
- assurance à 12 k€ ;
- +0,5 ETP de soins ;
- gros entretien à 1,5 %.

Autres tests :
- **A frugal sans dette** : 736 / VIABLE bénévole.
- **A sans dette, dirigeant et cavalier payés** : −471 / NON VIABLE.
- **Club deal frugal** : −895 / NON VIABLE.
- **Crédit-vendeur frugal** : −3 078 / NON VIABLE.
- **E allégé** : voir §3.7.
- **Esquisse « petit château ≈ 1,15 M€ »** (type Sainte-Hermine, 56,5 ha [A1]), toutes hypothèses de l'auditeur [EST] :
  - 14 box, 23 places au pré, 9 retraites, 2 logements en gîte ;
  - EBITDA ≈ 16-17 k€ en frugal ;
  - NON VIABLE avec 0,55 à 1,1 M€ de dette.
  
  Ce n'est qu'un test exploratoire, mais il montre qu'un château moins cher ne règle pas le problème si l'on garde de la dette. **La pension rémunère à peine le travail de l'exploitant** (EBE médian de 34-53 k€ par exploitant [A3 §4]).

### 5.7 Ce que le modèle fait bien (à conserver)
- Toutes les cellules de calcul sont des formules et les hypothèses sont éditables et sourcées. Le statut « NON ACQUIS » est affiché sur chaque financement.
- Les verdicts NON VIABLE sont francs, sans maquillage. Le gros entretien est inclus dans le DSCR. Les déficits sont reportés.
- Les conversions TTC → HT sont justes :
  - box : 520/1,055 = 493 € ;
  - pré : 230/1,055 = 218 € ;
  - retraite : 210/1,20 = 175 € ;
  - travail : 656/1,20 = 547 € ;
  - mariage : 3 400/1,2 + 1 500/1,1 = 4 197 €.
- Le calibrage équestre est cohérent avec le Réseau Équin : EBE équestre de B ≈ 36 % du produit équestre, pour une référence de 36-38 % [A3 H10]. Le calibrage des activités l'est avec l'agent 4 (≈ 50 k€ de contribution).
- Le diagnostic « B sans dette NON VIABLE » est la bonne question posée au bon endroit.

---

## 6. Notation indépendante /100

Barème :
- **Financement** (25) : 0-5 inaccessible ; 6-12 possible seulement avec de lourdes hypothèses non acquises ; 13-19 plausible sous conditions ; 20-25 démontré.
- **Résilience** (25) : NON VIABLE 0-5 ; FRAGILE ou « bénévole » qui bascule aux corrections 6-13 ; viable robuste 18-25.
- **Équestre** (20) : demande prouvée, place structurante, qualité.
- **Contrôle** (15) : propriété, sûretés, risque de dépossession.
- **Juridique et opérationnel** (10).
- **Potentiel** (5).

| Scénario | Fin. /25 | Rés. /25 | Équ. /20 | Ctrl /15 | Jur.-op. /10 | Pot. /5 | **Total** | Incertitude | Justification courte |
|---|---|---|---|---|---|---|---|---|---|
| A central | 3 | 1 | 13 | 5 | 5 | 3 | **30** | ± 5 | Équestre le plus structurant, mais prix au-dessus du 3e quartile, cavalier clé ; dette inaccessible ; saisie probable |
| A prudent | 3 | 0 | 12 | 4 | 5 | 2 | **26** | ± 5 | −3,9 M€ |
| A optimiste | 3 | 2 | 13 | 5 | 5 | 3 | **31** | ± 5 | DSCR 0,02 |
| A frugal (bancaire) | 3 | 3 | 12 | 5 | 4 | 3 | **30** | ± 5 | Fondateur cavalier pro bénévole ; −1,5 M€ |
| B central | 3 | 1 | 11 | 5 | 4 | 3 | **27** | ± 5 | EBITDA ≈ 0 ; pension réelle mais « écurie de pension » plutôt que prestige |
| B prudent | 3 | 0 | 10 | 4 | 4 | 2 | **23** | ± 5 | −3,5 M€ |
| B optimiste | 3 | 2 | 11 | 5 | 4 | 3 | **28** | ± 5 | Ne sert pas sa dette même en cas favorable |
| B frugal (bancaire) | 3 | 3 | 11 | 5 | 4 | 3 | **29** | ± 5 | −1,6 M€ |
| B club deal | 4 | 2 | 11 | 2 | 3 | 2 | **24** | ± 4 | Investisseurs irrationnels ; 10 % des votes ; drag-along |
| B crédit-vendeur | 3 | 0 | 11 | 4 | 4 | 2 | **24** | ± 4 | −3,8 M€ ; conditions hors marché ; clause résolutoire |
| E central | 5 | 1 | 11 | 5 | 3 | 2 | **27** | ± 6 | Pas de site ; dette sur un droit réel ; aucune sortie |
| E allégé | 10 | 6 | 11 | 5 | 3 | 2 | **37** | ± 10 | Montant accessible (0,63 M€) mais pas de site, pas de réserve, aucun des 6 stress réussi, résidence juridiquement fragile |
| C central | 4 | 9 | 11 | 12 | 4 | 4 | **44** | ± 10 | Meilleure structure si le capital existait ; 3,4 M€ non démontrés ; 0 stress réussi sur 7 ; bascule sur une seule correction |
| C négocié | 5 | 10 | 11 | 12 | 4 | 4 | **46** | ± 10 | 2,6 M€ non démontrés ; décote −20 % et travaux −30 % non prouvés |
| C prudent | 4 | 3 | 10 | 11 | 4 | 3 | **35** | ± 8 | NON VIABLE |
| C optimiste | 4 | 12 | 11 | 12 | 4 | 4 | **47** | ± 10 | Hypothèses de prix et volumes improbables |
| *Diag. B sans dette* | *2* | *4* | *11* | *14* | *4* | *3* | ***38*** | ± 5 | 3,9 M€ hors scénarios d'apport ; NON VIABLE avec dirigeant payé |
| *Diag. B frugal sans dette* | *2* | *10* | *11* | *14* | *4* | *3* | ***44*** | ± 8 | VIABLE bénévole au modèle, NON VIABLE au cas d'audit |

**Notes de lecture.**
- **Aucune note n'atteint 50/100.** Les notes de C (44-47) récompensent une structure saine (peu de dette, 100 % de contrôle), pas une faisabilité démontrée.
- Le critère « financement » est faible partout pour la même raison : **aucun scénario n'a de source de fonds propres acquise**.
- **Obstacles rédhibitoires**, qu'aucune note ne doit masquer :
  - R1-R2 pour tout montage endetté ;
  - R3 pour C ;
  - R4 pour le club deal.

---

## 7. Conditions go / no-go

### 7.1 NO-GO : une seule condition suffit à ne pas signer
1. **La dette dépasse la dette soutenable recalculée** (EBITDA moyen des années 2-4, sans loyer privé, DSCR ≥ 1,3). Pour le domaine type, cette capacité est de l'ordre de 0 à 0,5 M€ selon les corrections retenues [CALC]. Cela exclut tout achat à ≈ 2,5 M€ avec moins de ≈ 3,3-3,6 M€ de fonds propres réellement disponibles.
2. **Le fondateur détient moins de 50 % des votes** de la société qui possède sa résidence (club deal).
3. **Crédit-vendeur avec clause résolutoire non plafonnée**, sans délai de grâce ni accord de rang avec la banque.
4. **Obligations in fine** remboursées par une exploitation dont le cash-flow libre n'est pas démontré.
5. **Offre d'achat sans certificat d'urbanisme opérationnel** positif pour les changements de destination (salle, gîte), sans lecture du PLU et, en abords de MH, sans échange avec l'UDAP.
6. **Offre sans diagnostic** d'architecte du patrimoine ou de bureau de contrôle chiffrant clos-couvert, ERP et réseaux (± 30 %).
7. **Château ou logement privé dans une société à l'IS** de ≥ 5 M€ d'actifs, majoritairement passive, logeant le fondateur sous le prix du marché (235 ter C).
8. **Fondateur bénévole sans revenu extérieur** documenté couvrant loyer et coût de vie (≈ 40-50 k€ nets/an [EST]).
9. **Bail emphytéotique** sans clause écrite autorisant la résidence du preneur, ou portant sur des terres agricoles sans information préalable de la SAFER (2 mois, à peine de nullité).

### 7.2 GO : toutes les conditions sont requises avant une offre
1. **Fonds propres prouvés** par des relevés, couvrant prix + frais + travaux + 12-18 mois de pertes + réserve ≥ 150 k€, avec une dette au plus égale à la dette soutenable.
2. **Preuve de demande** : pré-contrats ou lettres d'intention pour ≥ 60 % des places de pension au prix cible, dans un rayon de 30-45 minutes. À défaut, reprise d'une écurie déjà occupée (fichier clients, comptes).
3. **Historique d'exploitation du fondateur** : 2-3 ans de gestion d'une écurie (location-gérance, salariat ou association) avec des comptes. Les banques et l'agent 2 le demandent [A2 §5].
4. **Bien déjà équipé** :
   - au moins 20 box en état, une carrière et, idéalement, un manège ;
   - salle ERP existante ou dépendance convertible avec certificat d'urbanisme positif ;
   - résidence séparée des flux clients ;
   - ≤ 45 équidés pour 50 ha utiles.
5. **Modèle corrigé** au moins de M1 à M5, puis **stress passés** séparément : CA −30 %, travaux +30 %, retard de 12 mois, assurance ×2, sécheresse (foin +20 k€). Critère : trésorerie toujours ≥ 0.
6. **Structure validée** par un avocat fiscaliste, un notaire et un avocat en droit rural :
   - logement privé hors IS ou loyer de marché expertisé ;
   - absence de bail rural non voulu ;
   - stratégie SAFER ;
   - ventilation de la TVA ;
   - conventions réglementées.
7. **SAFER** : projet agricole équestre crédible pour la rétrocession ou la non-préemption des 50 ha.
8. **Pour C** :
   - holding ayant **effectivement** généré le cash (comptes certifiés, après remboursement des dettes LBO et sans nantissement bloquant) ;
   - organisation permettant au fondateur de quitter l'opérationnel des PME ;
   - château **hors de la holding à l'IS** si celle-ci est majoritairement passive.
9. **Personne-clé** : un salarié capable de tenir l'écurie seul, assurance homme-clé et prévoyance du fondateur (risque d'accident sectoriel 3 fois la moyenne [A8-10]).

### 7.3 Jalons suggérés (ESTIMATION de l'auditeur)
- **2026-2028** : capital ou revenus (holding, carrière), plus une expérience équestre gérée et chiffrée, sans achat de château.
- **2028-2029** : le modèle corrigé est rejoué avec le bien réel et des devis ; veille BODACC, SAFER et collectivités (piste E).
- **2030-2031** : achat seulement si 7.2 est entièrement rempli ; à défaut, location ou bail emphytéotique d'un site équipé.

---

## 8. Points de doute / hypothèses non vérifiées

1. **Distribution des prix de pension** : recalcul de l'auditeur sur le jeu déclaratif de l'agent 3 (402 tarifs, 114 écuries, 4 régions). L'Auvergne (Allier, où se trouvent Ygrande et Treteau), la Vendée intérieure et la Nouvelle-Aquitaine **ne sont pas couvertes**. Les tarifs déclarés ne sont pas des prix encaissés. Méthode : relever 30 tarifs dans le département cible et interroger 5 écuries (aucun contact n'a été pris ici).
2. **Zone de chalandise des pensions** : aucune enquête trouvée sur la distance entre le domicile du propriétaire et l'écurie (1 recherche). L'affirmation « clientèle locale » est une **ESTIMATION**. Méthode : licenciés FFE par commune, enquête IFCE, entretiens.
3. **Assurance** : la seule fourchette chiffrée récente (15-30 k€) vient d'un courtier qui vend ces contrats [A8-03]. Le Figaro 2020 disait « rarement < 2 500 € » [A4 §11]. Ma valeur de 12-20 k€ est une **ESTIMATION** ; des devis sont nécessaires.
4. **Demeure Historique** : le minimum de 40 k€/an date de 2019 et concerne des monuments de tailles variées [A8-04]. Ce n'est pas une enquête de coûts détaillée.
5. **Toiture** : 95-145 €/m² est un prix de maison courante [A8-09]. Le coût d'un château ou d'un MH est **INCONNU** (devis d'entreprise qualifiée MH).
6. **Crédit-vendeur** : les pratiques (30-50 %, 1-5 ans) viennent de courtiers et d'un portail immobilier [A8-05, A8-06], pas d'une statistique notariale. L'absence de cas « château » n'est pas une preuve d'inexistence.
7. **Accidents du travail** : le taux de 74,7 (entraînement, dressage, haras) concerne les **salariés**. Le classement des non-salariés figure dans la même étude mais n'a pas été extrait en détail [A8-10].
8. **BEA et résidence privée** : mon objection (intérêt général, CGCT L.1311-2 ; possibilité d'un bail de droit commun sur le domaine privé ; art. L.451-8 sur l'entretien) est un **raisonnement juridique non validé**. Les articles n'ont pas été relus sur Légifrance par l'auditeur. À valider par un avocat en droit public.
9. **DJA** : seule la fiche de Bourgogne-Franche-Comté (2024) a été lue. La note bretonne, qui semble admettre la pension avec valorisation, n'a été vue qu'en extrait (protection anti-robot) [A8-02]. Les règles 2026 de la région cible sont **INCONNUES**.
10. **Fiscalité MH personnelle** : l'ordre de grandeur de l'économie d'impôt (« plusieurs dizaines de k€/an ») est une **ESTIMATION** qui dépend du TMI, de l'ouverture au public et de la protection du bien. Non modélisée.
11. **Esquisse « petit château »** : toutes ses hypothèses sont celles de l'auditeur [EST]. Elle ne constitue pas un scénario recommandé.
12. **Variantes [CALC]** : elles réutilisent la mécanique du directeur. Une erreur commune au modèle, non détectée ici, se retrouverait dans mes tests. J'ai vérifié manuellement le compte de résultat de B_central (CA 318 k€ en euros 2026, marge 230,7 k€, charges fixes 232,4 k€), ainsi que les échéanciers de dette et l'IS.
13. **Ygrande** : le lien entre l'exploitant liquidé et l'enseigne repose en partie sur un extrait [A7 CE2]. Le statut actuel de l'annonce SAFER n'a pas été revérifié par l'auditeur. *Mise à jour du 14/10/2026 (étude de cas `02_BENCHMARK/Cas_Ygrande/`) : le lien est confirmé par France 3 (29/10/2025, page lue) ; le domaine est en vente en 2026 par quatre canaux, dont la SAFER.*
14. **Sécheresse 2026** : le −33 % de pousse des prairies est cité par la presse d'après le ministère [A8-07]. Le prix du foin (> 200 €/t) est un **EXTRAIT** (la page Réussir renvoyait une erreur 404).
15. **Contre-exemples cherchés et non trouvés** :
    - un château vendu avec un crédit-vendeur important ;
    - un particulier logé dans un château public sous bail emphytéotique ;
    - une statistique annuelle de mariages par château.
    
    L'absence de preuve n'est pas une preuve d'absence.

---

*Fichiers de travail de l'auditeur (non livrables, dossier temporaire personnel du scratchpad) : `variants.py`, `variants2.py`, classeurs recalculés `variantes_audit*.xlsx`. Chaque variante est décrite au §5.6 et peut être rejouée dans le classeur du projet en modifiant les cellules jaunes correspondantes.*
