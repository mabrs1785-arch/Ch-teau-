# Objections et risques — Audit contradictoire indépendant (Agent 8)

> Rédigé le 2026-10-14 par l'Agent 8 (auditeur contradicteur), indépendant du directeur.
> Documents audités : `01_OPPORTUNITES/*`, `02_BENCHMARK/*`, `03_FINANCEMENT/*`, `05_AUDIT/Cadre_juridique_fiscal.md`, `05_AUDIT/Verifications_vague2.md`, `05_AUDIT/Stress_tests.md`, `04_MODELES_ECONOMIQUES/hypotheses.py` et `build_model.py`. J'ai aussi relu les lignes année par année du classeur recalculé (LibreOffice, 0 erreur de formule).
> Sources propres : `_brut/sources_agent8.csv` (identifiants **A8-xx**). Les identifiants A1-A7, V2-xx renvoient aux registres des autres agents.
> Légende : **FAIT SOURCÉ** (extrait WebSearch consulté ce jour, page non lue en entier car WebFetch est bloqué) / **ESTIMATION** (raisonnement explicite) / **INCONNU** (« Je ne sais pas » + méthode de vérification) / **CALCUL** (fait par moi à partir des sorties du modèle).

---

## 0. Verdict de l'auditeur en une page

1. **Le problème n'est pas le montage financier, c'est l'économie du domaine.** Le modèle le montre lui-même : B financé sans aucune dette reste NON VIABLE (trésorerie −0,49 M€). Avec une équipe normale, l'EBITDA est proche de zéro. Je confirme cette conclusion du directeur et je la durcis.
2. **La seule configuration jugée « VIABLE » (B_frugal_sans_dette) ne l'est pas après correction de trois erreurs du modèle.** Les prix de pension et de mariage sont des prix TTC traités comme HT. Le fondateur paie 24 k€ de loyer sans être rémunéré. Les investisseurs perdent de l'argent (TRI −4,7 %). Après correction, l'EBITDA an 5 passe d'environ 125 k€ à environ 55 k€. Le cash-flow libre tombe autour de 0 (CALCUL, §3.3).
3. **Fait nouveau, défavorable (A8-01, A8-02) : le bien de référence des scénarios A et B (Ygrande, 2,65 M€) est vendu après la liquidation de son exploitant.** La SAS Groupe Cœur et Détente (hôtellerie, restauration, loisirs, bien-être), domiciliée à Ygrande, a été placée en liquidation judiciaire le 28/10/2025 (TC de Cusset, cessation des paiements au 01/09/2025). La SAFER AURA remet le domaine en vente (référence 03 ET 26 YGR1, datée du 02/07/2026). Un exploitant professionnel a donc **déjà échoué sur ce site précis** avec un modèle proche du scénario B. C'est aussi un levier de négociation sur le prix, que le modèle ignore.
4. **Je rejette le scénario A sous toutes ses variantes de financement, ainsi que B (central, prudent, optimiste, frugal), C central, C_frugal_holding et D tel que modélisé** (justification en §5).
5. **Je ne garde que C_cible, et sous condition.** C'est la seule voie qui préserve le contrôle. Mais c'est un achat de consommation patrimoniale financé par des PME, pas un projet qui s'autofinance. Elle suppose 3,15 M€ de fonds propres de holding disponibles en 2031, ce que le montage E de l'agent 2 juge lui-même hors de portée d'un seul LBO (≈ 40 k€/an de marge après dette). Elle est aussi contradictoire en temps de dirigeant : piloter des PME reprises tout en exploitant un domaine loué dès l'an 1 n'est pas tenable.
6. **Là où l'équipe est trop pessimiste** (§6), sans que cela change le verdict :
   - prix d'achat non négocié malgré la liquidation d'Ygrande et la décote de Hus ;
   - équipements existants recomptés en capex (Ygrande a déjà un manège couvert, 24 boxes et une capacité annoncée de plus de 80 chevaux) ;
   - taxe foncière de 15 k€ contre 3 à 8 k€ observés ;
   - aucune reprise d'un fonds événementiel déjà en activité.
7. **Mes notes indépendantes sur 100** (§7) : C_cible **47**, C_frugal_holding 38, C_central 33, B_frugal 30, D 29, A_frugal 28, B_central 26, A_central 24. B_frugal_sans_dette obtient 30, comme simple diagnostic. **Aucun scénario n'atteint 50.** L'incertitude est de ±8 à ±12 points selon les cas.

---

## 1. Méthode et limites

- J'ai fait 17 recherches WebSearch (sur 20 autorisées). WebFetch est bloqué : je n'ai lu aucune page en entier, seulement les extraits renvoyés par le moteur. Fiabilité plafonnée à « moyenne ».
- J'ai vérifié la logique des formules dans `build_model.py`, puis relu les lignes annuelles de A_central, B_central, B_frugal, B_frugal_sans_dette, C_central, C_cible et D_bien_modeste dans le classeur recalculé.
- Je n'ai pas modifié le modèle. Les corrections chiffrées du §3.3 sont des **calculs à la main**, sur l'an 5, à partir des lignes du classeur. Elles sont à refaire dans le modèle.
- Échelles du registre : probabilité et impact de 1 (faible) à 5 (très élevé). **Criticité = P × I.** « Rédhibitoire » signifie que, si le risque se réalise, le scénario ne peut pas être sauvé par un ajustement.

---

## 2. Registre des risques classés

| # | Risque | Catégorie | P | I | P×I | Rédhibitoire ? | Preuve / raisonnement | Test ou mitigation |
|---|---|---|---|---|---|---|---|---|
| R1 | **Dette bancaire refusée** : 2,0-2,1 M€ demandés pour un actif dont l'EBITDA projeté est ≤ 0 (A, B central) ou ≤ 130 k€ (variantes frugales) | Financement | 5 | 5 | **25** | **Oui** (A, B, D) | Le modèle calcule lui-même une « dette soutenable » de 0 € (A/B central) à 0,88 M€ (B_frugal). Apport usuel de 20-40 % pour un château (V2-05) et de 30-50 % en hôtellerie (A8-19, A8-20) ; un projet de création sans historique est en bas de l'échelle | Ne présenter à une banque que la dette couverte par un EBITDA démontré (DSCR ≥ 1,2 après gros entretien) |
| R2 | **Aucun investisseur rationnel** : TRI investisseurs négatif ou non calculable dans **toutes** les feuilles (au mieux −4,7 %) | Financement | 5 | 5 | **25** | **Oui** (A, B) | Lignes « TRI investisseurs » du modèle. Agent 2, §4 : « un investisseur purement financier ne le ferait probablement pas » | Seul un investisseur « émotionnel » (usage, chevaux, fiscalité MH à l'IR) est concevable. Aucun n'est identifié |
| R3 | **Économie structurellement déficitaire** : EBITDA ≈ 0 avec une équipe normale ; même sans dette, la trésorerie devient négative (B_sans_dette −0,49 M€) | Économie | 4 | 5 | **20** | **Oui** | Modèle. Benchmarks concordants : centre équestre type à EBE/PB ≈ 22 %, exploitant sous le SMIC (A3-29) ; château événementiel de Chazemais à 139-189 k€ de CA (V2-54) ; Sarthe 90 k€ de CA pour 56 événements (V2-53) ; « la majorité des hôtels-châteaux de moins de 15 chambres sous le seuil de rentabilité » (V2-09) | Aucune mitigation financière ne compense un EBITDA nul |
| R4 | **Holding incapable d'apporter 2,2 à 3,15 M€ en 2031** (C) | Financement | 5 | 5 | **25** | **Oui** (C) | Agent 2, montage E : un LBO de 600 k€ d'EBITDA laisse ≈ 40 k€/an après dette pendant 7 ans. Les cibles reprises en LBO font plus souvent défaut que des entreprises comparables (A8-17). Les faillites de reprises externes passent par le marché, l'endettement et le management (A8-18) | Décaler l'achat à 2033-2036 ; n'acheter que si la holding a la trésorerie en banque (pas en prévision) |
| R5 | **Saturation du fondateur** : en version frugale, il tient seul (avec 1,5 soigneur) environ 45 chevaux, 18 mariages, 10 journées d'étude, le gîte, la commercialisation, et en C une holding de PME | Opérationnel | 5 | 4 | **20** | Oui pour C en parallèle ; non sinon | ESTIMATION : 45 chevaux 365 j/an avec 1,5 ETP soumis au repos hebdomadaire, donc les trous sont comblés par le fondateur ; les week-ends de mai à septembre sont pris par les mariages. Un repreneur de PME doit être à plein temps dans sa cible (A8-18 : le management est l'une des 3 filières de défaillance) | Séquencer (PME **ou** domaine, pas les deux) ; budgeter un vrai salaire de dirigeant et un remplaçant |
| R6 | **Revenus surestimés par la TVA** : 550 €/mois et 5 500 €/mariage sont des prix publics TTC, modélisés en HT | Modèle | 5 | 3 | **15** | Non, mais fait basculer B_frugal_sans_dette | Tableaux de l'agent 3 en « € TTC/mois ». La pension pure n'est pas au taux réduit selon l'ancienne doctrine, tolérance 50/50 (A8-05, A8-06, A8-07). Mariages : ESTIMATION 20 % | Recalculer tous les prix en HT (§3.1, E2) |
| R7 | **Précédent d'échec sur le site de référence** (liquidation de l'exploitant d'Ygrande en 10/2025) | Marché | 4 (déjà réalisé) | 3 | **12** | Non (levier de prix) | A8-01, A8-02. Le domaine comprend château, restaurant, piscine, manège, piste de galop (A8-02, A8-03) | Obtenir les comptes 2022-2024 de la SAS liquidée (Pappers/Infogreffe) et le rapport du liquidateur : pourquoi a-t-elle échoué ? |
| R8 | **Changement de destination / PLU non « étoilé »** : salle de réception ou gîte impossible | Juridique | 3 | 5 | **15** | **Oui** pour B (sans salle, pas de mariages) | Art. L.151-11 C. urb. (agent 6) | Condition suspensive dans le compromis ; lecture du PLU avant toute offre |
| R9 | **Cohabitation mariages / chevaux / pensionnaires** : musique jusqu'à 2-5 h, 80-150 voitures, feux d'artifice ; **les propriétaires de chevaux en pension viennent surtout le week-end, les jours mêmes des mariages** | Opérationnel | 4 | 3 | **12** | Non | Juges : plafonds en dB chez le voisin avec astreinte de 1 250 € par manquement (Orléans 2026, A8-10) ; fermeture municipale de 30 jours d'une salle de réception attaquée sans succès (TA Versailles 2023, A8-11). Feux d'artifice incompatibles avec les chevaux (agent 6) | Salle à plus de 300 m des écuries, limiteur, étude d'impact ; réserver des week-ends « cavaliers » (donc moins de 18 mariages) |
| R10 | **Requalification en bail rural** de l'écurie louée à un cavalier pro (A) ou des ventes d'herbe répétées | Juridique | 3 | 4 | **12** | Non (mais perte durable de maîtrise d'une partie du domaine) | Requalification d'un bail verbal portant sur 14 boxes, une sellerie et un paddock confirmée en appel (CA Amiens, 06/12/2016, A8-12). Ventes d'herbe (V2-27) | Prestation de services avec accès planifié, ou société commune ; jamais de mise à disposition exclusive sans avocat rural |
| R11 | **Perte du lieu de vie** : clause résolutoire du crédit-vendeur, hypothèque, nantissement des parts, caution personnelle, remboursement in fine des obligations | Contrôle | 3 | 5 | **15** | **Oui** si réalisé | B_central : 300 k€ d'obligations à rembourser en an 8, alors que la trésorerie modélisée est déjà de −2,5 M€ ; crédit-vendeur amorti sur 5 ans (≈ 87 k€/an) dès l'an 1 | Pas de crédit-vendeur avec clause résolutoire sur la partie habitée ; pas d'in fine sans source de remboursement identifiée |
| R12 | **Perte de contrôle actionnariale** : 35 % du capital et 51 % des votes via actions de préférence, alors que les tiers apportent 85 % (B) à 94 % (B_sans_dette) de l'argent | Contrôle | 4 | 4 | **16** | Non, mais vide la promesse « contrôler durablement » | Calcul sur le modèle. Un investisseur qui finance 85-94 % exigera une clause de liquidité (drag-along, sortie forcée) : la sortie, c'est la vente du château, donc du domicile du fondateur | Si investisseurs : seulement à l'OpCo ou dans une PropCo d'activité, jamais sur le logis |
| R13 | **Illiquidité pour les investisseurs** : ni dividendes ni sortie avant l'an 10 ; une vente de château prend 18-24 mois, environ 400 transactions par an (A8-16) ; Hus −35 % en un an (agent 7) | Financement | 5 | 3 | **15** | Non (mais aggrave R2) | A8-16 ; engagement de conservation MH de 15 ans si ce régime est utilisé (agent 6) | Ne pas promettre de liquidité ; préférer la dette amortissable ou les préventes |
| R14 | **ABS / acte anormal de gestion** sur la résidence privée | Juridique | 3 | 4 | **12** | Non si loyer de marché payé | Agent 6, §2 | SCI familiale à l'IR pour le logis ; loyer payé sur des revenus **réels** du fondateur |
| R15 | **SAFER** : préemption, ou cahier des charges d'attribution (Ygrande est vendu par la SAFER, qui propose de trouver un agriculteur partenaire, A8-02) | Juridique | 3 | 3 | 9 | Non | Durée et contenu du cahier des charges : **INCONNU** (méthode : demander le projet de cahier des charges à la SAFER AURA, par écrit, via un notaire) | Projet agricole crédible (élevage, préparation de chevaux) porté par le fondateur |
| R16 | **Travaux sous-évalués** (pas de devis, pas de diagnostic, facteur 2 à 3 selon l'agent 1) | Capex | 4 | 4 | **16** | Non pour un écart de +30 % ; oui pour un facteur 2 sans réserve | Stress test Travaux +30 % : trou de trésorerie de 0,2-0,4 M€ même sans dette. L'agent 2 juge son propre chiffrage « probablement sous-estimé » | Diagnostic d'architecte du patrimoine avant l'offre, enveloppe d'aléas de 20 % hors budget |
| R17 | **Dépendance à quelques clients** : 1 cavalier pro (A : 10 boxes), 1-2 marchands pour les showcases, plateformes de mariage, quelques propriétaires de chevaux de valeur | Marché | 3 | 3 | 9 | Non | ESTIMATION | Plafonner chaque client à 15 % du CA |
| R18 | **Saisonnalité** : 60 % des mariages de juin à septembre (A4-03) ; foin acheté en été pour l'hiver ; le modèle annuel avec BFR négatif (−3 % du CA) masque un creux de trésorerie de janvier à avril | Trésorerie | 4 | 2 | 8 | Non | Le BFR négatif ne vaut qu'en saison ; stock de foin non modélisé (ESTIMATION) | Plan de trésorerie mensuel ; ligne de crédit de campagne |
| R19 | **Charges patrimoniales mal calibrées** : gros entretien de 1 % appliqué à une base qui inclut le foncier, pour un château de 1835 de plus de 1 500 m² | Capex | 3 | 3 | 9 | Non | Règle « ancien non rénové ≈ 2 % » (V2-11) ; « au moins 40 k€/an hors travaux » par monument selon la Demeure Historique (A8-04) | Diagnostic de couverture et de charpente ; provision de 1,5-2 % sur le bâti |
| R20 | **Taxe de 20 % sur les holdings patrimoniales (art. 235 ter C)** si la holding détient le château habité (C) | Fiscal | 2 | 4 | 8 | Non (structuration) | Agent 6 : inclusion du logement **INCONNUE** | Consultation écrite d'un avocat fiscaliste avant structuration |
| R21 | **Enseignement sans diplôme** (stages équestres de A) | Juridique | 3 | 3 | 9 | Non | Art. L.212-1 C. sport (agent 6) | Salarier un diplômé : la charge fixe est absente du modèle A |
| R22 | **Coûts du foin et de la paille** (sécheresse) sur 45-50 chevaux | Économie | 3 | 2 | 6 | Non | Prix du foin : **INCONNU** (FranceAgriMer / cotations des Chambres) | Autoproduction de foin sur le domaine, stock tampon |

**Lecture du registre.** Cinq risques sont rédhibitoires et très probables : R1, R2, R3, R4 et R5 pour C mené en parallèle. Ils touchent tous la **capacité du domaine à produire du cash**, ou la **capacité du fondateur à apporter des fonds propres**. Les risques juridiques (R8, R10, R14, R15, R20) sont réels mais gérables par des diligences et des conditions suspensives.

---

## 3. Critique du modèle financier

### 3.1 Erreurs à corriger en priorité (ordre d'importance)

| # | Erreur | Où | Effet | Sens du biais | Correction proposée |
|---|---|---|---|---|---|
| **E1** | **Loyer privé du fondateur (24 k€/an) compté en CA, alors que le fondateur n'a pas de quoi le payer.** En central, sa rémunération chargée de 30 k€ (≈ 18 k€ net, ESTIMATION) est inférieure au loyer. **Dans les variantes frugales, sa rémunération est supprimée mais le loyer est conservé.** Le loyer subit en plus la montée en charge, l'inflation et le stress CA −30 %, ce qui n'a pas de sens pour un loyer | Lignes « Loyer de la partie privée » de toutes les feuilles ; fonction `frugal()` | +26 k€ d'EBITDA an 5 sans contrepartie économique, soit **21 % de l'EBITDA de B_frugal** | **Optimiste** | Sortir ce loyer du CA, ou le garder mais ajouter une rémunération du dirigeant au moins égale au loyer + 18 k€ de reste à vivre ; l'exclure du multiplicateur `ca_mult` et de la montée en charge |
| **E2** | **Prix TTC modélisés comme HT** (« TVA neutre, montants HT »). Pension : 430-700 € « TTC/mois » (agent 3) ; pension pure à 20 % dans l'ancienne doctrine, tolérance 50/50 entre 5,5 % et 20 % (A8-05 à A8-07). Mariages : tarifs publics des châteaux, a priori TTC (ESTIMATION) | Lignes de revenus | −25,6 k€ (pension, taux mixte ≈ 12,75 %) et −17,9 k€ (mariages à 20 %) en an 5, soit **≈ −43 k€ d'EBITDA** | **Optimiste** | Diviser les prix publics par (1 + taux) : pension ≈ 550/1,1275 ≈ 488 € HT ; mariage ≈ 5 500/1,2 ≈ 4 583 € HT |
| **E3** | **Partage du capital incohérent dans les variantes sans dette** : `part_fondateur` reste à 35 % alors que les investisseurs apportent 4,2 M€ contre 0,25 M€ pour le fondateur. D'où un « TRI fondateur » de 17 % (B_sans_dette) et 21,7 % (B_frugal_sans_dette) **purement artificiel**, et un TRI investisseurs de −4,7 % à −8,3 % | `hypotheses.feuilles()`, B_sans_dette | Donne une image flatteuse du projet pour le fondateur | **Optimiste** | Recalculer la part au prorata des apports (ou avec une prime d'industrie explicite et plafonnée) : ≈ 6 % pour 0,25/4,45 M€ |
| **E4** | **Le verdict « VIABLE » ignore la rémunération des investisseurs et du dirigeant.** Une feuille où les investisseurs perdent 4,7 %/an et où le dirigeant n'est pas payé est jugée VIABLE | Formule du verdict | Le seul « VIABLE » du classeur est un artefact | **Optimiste** | Ajouter deux conditions : TRI des apporteurs externes ≥ cible (ex. 5 %), ou absence d'apporteurs externes ; rémunération du dirigeant ≥ seuil |
| **E5** | **Fonds propres nécessaires sous-estimés** : la formule (emplois + réserve − dette soutenable) ignore les pertes de montée en charge (B_frugal : −95 k€ puis −29 k€ d'EBITDA les années 1-2) et le différé | KPI `k_fp_nec` | 0,1 à 0,4 M€ de besoin oublié | **Optimiste** | Ajouter la somme des flux d'exploitation négatifs jusqu'au premier flux positif |
| **E6** | **Stress « Retard 12 mois » mal posé pour C** : il **améliore** la trésorerie (−2,05 M€ contre −2,15 M€ en central), car le loyer du domaine n'est dû qu'à partir de l'ouverture. Un bailleur ne donne pas une année gratuite | Ligne « Loyer des murs » : condition `n_exp > 0` | Le stress est sans valeur pour C | **Optimiste** | Le loyer court dès la signature du bail (an 1), indépendamment de l'ouverture |
| **E7** | **Événements sans capex ERP** : C fait 10 mariages et 6 journées d'étude pendant la location, sans salle (« salle ERP après acquisition seulement ») ; A organise 6 réceptions, 8 showcases et 3 concours avec un « salon (pas de salle ERP > 50 pers.) ». Or une salle à usages multiples sort de la 5e catégorie dès 50 personnes (agent 6) | Revenus de A et C | CA événementiel de A et C partiellement impossible | **Optimiste** | Soit retirer ces lignes, soit ajouter un capex ou une location de structure (régime CTS, coût **INCONNU**) |
| **E8** | **Valeur de sortie gonflée** : le gros entretien annuel est capitalisé dans `cum_capex`, puis valorisé à 80 % dans la valeur de sortie (l'entretien ne crée pas de valeur de marché) ; pas de frais de cession (agence, diagnostics) ni de délai de vente (18-24 mois, A8-16) | `v_actif` | Quelques centaines de k€ sur la valeur an 10 ; TRI légèrement flatté | **Optimiste** | Exclure le gros entretien de la base ; −5 % de frais de cession ; tester une valeur de sortie à 60 % (Hus −35 % en un an) |
| **E9** | **Libellé trompeur du TRI** : quand il n'y a pas d'investisseurs (C, holding à 100 %), la cellule affiche « perte quasi totale (TRI non calculable) » | `k_tri_inv` | Confusion de lecture dans la Comparaison | Neutre | Afficher « sans objet » si le flux d'entrée est nul |
| **E10** | **DSCR calculé sans le gros entretien** (EBITDA − IS) ; une banque déduirait le capex de maintien | Ligne DSCR | DSCR surestimé d'environ 40-50 k€/an au numérateur. Le verdict reste prudent grâce au test de FCF | **Optimiste** (faible) | DSCR sur (EBITDA − IS − gros entretien) |
| **E11** | **Stock de foin et charges payées d'avance non modélisés** ; BFR uniformément négatif à −3 % du CA | BFR | Creux d'hiver masqué (R18) | **Optimiste** (faible) | BFR saisonnier, ou + 1 mois de charges de cavalerie en stock |
| **E12** | **Prix d'achat fixe en C** : 2,65 M€ nominal en an 5 sans option négociée, et les 4 ans de loyer (≈ 415 k€) ne s'imputent pas sur le prix | Inputs C | Hypothèse favorable si une option à prix fixe est obtenue, défavorable si les loyers pouvaient être imputés. Option **non acquise** | Indéterminé | Afficher explicitement « option à prix fixe : non acquise » ; tester un prix +10 % et une imputation de 50 % des loyers |

**Ce que j'ai vérifié et trouvé correct** (pas d'erreur détectée) :
- échéancier bancaire : annuité constante via PMT sur (durée − différé), différé d'un an, intérêts sur le capital de début ;
- crédit-vendeur amortissable ;
- obligations in fine à la date absolue `oc_ech` ;
- report déficitaire illimité ; l'IS n'est jamais dû dans les feuilles déficitaires, donc la simplification (pas de taux réduit de 15 %, pas de plafond d'imputation) est sans effet ici ;
- amortissement du bâti (50 % du prix + frais, sur 30 ans) et des travaux (15 ans, sans prorata, effet mineur) ;
- flux d'exploitation = EBITDA − IS − ΔBFR ;
- cohérence emplois / ressources / trésorerie ;
- dette soutenable = PV(taux, durée, (EBITDA an 6 − gros entretien)/1,2).

**Incohérence relevée dans `Stress_tests.md` (§5.4)** : le texte conclut que l'annulation d'événements plaide pour une base équestre récurrente, puis que « le scénario A pur est le plus exposé ». Or A est équestre à 86 % : c'est le **moins** exposé à l'annulation d'événements (S_A_Annul40evt : EBITDA an 5 de −70 k€ contre −47 k€ en central, soit −23 k€ ; B : −45 k€). A est le plus exposé à la baisse du CA récurrent et au coût de main-d'œuvre, pas à l'annulation d'événements. À reformuler.

### 3.2 Biais optimistes du modèle (hypothèses, pas formules)

1. **Pension box à 550 €** : c'est le haut de la fourchette, appliqué à un site rural de l'Allier. Grilles observées en rural : 435 €/mois box-paddock et 325 €/mois paddock individuel (La Gosnière 2025-2026, A8-13) ; pension travail en Normandie 480-550 € (A8-14). **ESTIMATION** : 450-480 € TTC est plus défendable à Ygrande sans clientèle de sport établie.
2. **Pension au pré à 280 €** : les références sont de 120-250 € (médiane 165 €, INRAE 2012, A8-15) et de 130-220 € (Oise 2020, V2-28). 280 € suppose une prestation « retraite » soignée dont la demande n'est **pas prouvée** (la seule source mentionne des places vacantes, A3-41).
3. **Montée en charge à 90 % d'occupation dès la 3e année**, sans clientèle ni réputation ; et 18 mariages/an alors que 781 châteaux de mariage sont référencés sur une seule plateforme (A4-19).
4. **Showcases B2B (4 à 8 par an à 5 000 €)** : aucune preuve de demande pour un lieu privé (agent 3). Je les mettrais à 0 en central.
5. **Concours** : budget **INCONNU**, marge supposée faible, et 3 jours à 8 000 € qui ne rapportent presque rien après 85 % de coûts. Ligne inoffensive, mais elle mobilise le fondateur.
6. **Aucun coût de structuration ni de multi-entités** (PropCo, OpCo, SCI, holding : avocats, notaire, expert-comptable × 3, éventuel CAC) au-delà de 15 k€/an « comptabilité, juridique ». ESTIMATION : 30-60 k€ de frais initiaux non modélisés.
7. **Pas de remplacement du fondateur** (maladie, accident de cheval) dans les variantes frugales : risque d'homme-clé non couvert.

### 3.3 Effet cumulé sur la seule feuille « VIABLE » (CALCUL, an 5, B_frugal_sans_dette)

| Étape | EBITDA an 5 | Commentaire |
|---|---|---|
| Modèle tel quel | 125,0 k€ | |
| − Loyer privé du fondateur (E1) | 99,0 k€ | −26,0 k€ |
| − TVA sur la pension (taux mixte 12,75 %, E2) | 73,4 k€ | −25,6 k€ sur 226,8 k€ de pensions |
| − TVA sur les mariages (20 %, E2) | 55,5 k€ | −17,9 k€ sur 107,2 k€ |
| − Gros entretien an 5 (≈ 43,9 k€) | **≈ 11,6 k€ de cash-flow libre** | Avant toute rémunération du dirigeant |
| − Rémunération minimale du dirigeant (30 k€ chargés indexés) | **≈ −21 k€** | Le fondateur doit bien vivre et payer son loyer |
| + Correction pessimiste : taxe foncière 16,6 → ~6 k€ (V2-06, V2-14) | ≈ −11 k€ | Voir §6 |

**Conclusion** : une fois les erreurs corrigées, même financé à 100 % en fonds propres, le domaine-type B **ne dégage pas de cash-flow libre positif** si le dirigeant est payé. Le verdict « VIABLE » doit devenir **« NON VIABLE, ou FRAGILE au mieux »**.

---

## 4. Objections par scénario

### Scénario A — Château équestre événementiel (central, prudent, optimiste, frugal)
- **Économie** : EBITDA an 5 de −47 k€ (central), +34 k€ (optimiste), +74 k€ (frugal) ; service de la dette de 165 à 270 k€/an. DSCR minimum de −0,39 à +0,17. **Aucune variante ne couvre la dette, même en optimiste.**
- **Réalité équestre** : c'est le scénario le plus « cheval » (86 % du CA). Mais :
  - ses lignes les plus distinctives (showcases, réceptions équestres, stages haut de gamme, concours) sont les **moins prouvées** ;
  - l'« écurie louée à un pro » est exposée à la requalification en bail rural (A8-12) ;
  - les stages supposent un enseignant diplômé non budgété (R21) ;
  - le benchmark rappelle qu'**aucun modèle équestre seul ne finance un château** (A3-29) et que le Haras de Hus, porté par un entrepreneur fortuné, a cessé son activité et décoté de 35 % (agent 7).
- **Capex** : 450 k€ d'équestre (dont un manège de 150 k€) alors que le bien de référence **a déjà** un manège couvert et une piste de galop (A8-02). Double comptage probable (biais pessimiste), mais sans effet sur le verdict.
- **Contrôle** : 35 % du capital, 51 % des votes « non acquis », crédit-vendeur avec clause résolutoire, obligations in fine de 300 k€ en an 8, alors que la trésorerie est déjà à −2,75 M€.
- **Verdict auditeur : ÉLIMINÉ** dans toutes ses variantes d'acquisition à crédit. À conserver comme **module d'exploitation** (pension box + pré) pour un domaine financé autrement.

### Scénario B — Château premium multiactivité (central, prudent, optimiste, frugal, sans dette)
- **Économie** :
  - EBITDA an 5 : −5 k€ (central), +82 k€ (optimiste), +125 k€ (frugal) ;
  - la dette de 2,8 M€ (banque + crédit-vendeur + obligations) coûte 270 k€/an pendant 5 ans ;
  - **B_optimiste reste NON VIABLE** (trésorerie −2,1 M€) : même avec +15 % de volumes et +8 % de prix, le montage ne tient pas.
- **Marché** : le CA non équestre modélisé (≈ 193 k€ en an 5) a le même ordre de grandeur que le CA **total** déclaré d'un château événementiel en activité dans l'Allier, Chazemais (139-189 k€, V2-54). C'est plausible, mais cela suppose d'atteindre en 4 ans ce qu'un lieu installé réalise.
- **Juridique** : PLU et changement de destination (R8), ERP type L (agent 6), bruit (R9), conflit d'usage du week-end entre mariés et pensionnaires (R9).
- **Précédent** : l'exploitant hôtelier d'Ygrande a été liquidé en 2025 (A8-01). **Je ne sais pas** pourquoi : comptes et rapport du liquidateur non consultés (méthode : Pappers/Infogreffe, BODACC, greffe du TC de Cusset).
- **B_sans_dette / B_frugal_sans_dette** : ce ne sont **pas des scénarios de financement** mais des diagnostics. Ils supposent 4,2 M€ d'investisseurs qui acceptent de perdre de l'argent (TRI −4,7 % à −8,3 %). Après correction (§3.3), même l'exploitation frugale ne s'autofinance pas.
- **Verdict auditeur : ÉLIMINÉ** (central, prudent, optimiste, frugal). B_frugal_sans_dette est **rétrogradé** de « VIABLE » à « NON VIABLE / FRAGILE » et ne doit pas être présenté comme une piste.

### Scénario C — Location puis acquisition via holding (central, frugal_holding, cible)
- **Phase locative (an 1 à 4)** : elle n'est **pas** le « test à faible risque » annoncé.
  - Pertes cumulées : −626 k€ d'EBITDA en central ; −138 k€ en C_cible (frugal) sur les années 1-4.
  - Cause : le locataire porte énergie, jardinier, parc, personnel **et** 100 k€ de loyer, sur un domaine dont il ne maîtrise pas les travaux.
  - Le loyer de 100 k€ (3,8 % de la valeur) n'est **pas sourcé**. Les exemples trouvés vont de 1 €/an (bail emphytéotique contre 3 M€ de travaux) à 80 k€/an + 7 % du CA (V2-36 à V2-38).
  - Je n'ai trouvé **aucune** offre de location-gérance d'un château avec redevance (A8-22 : uniquement des ventes de fonds + murs).
- **Option d'achat** : non acquise ; prix futur inconnu ; un bailleur qui voit le domaine valorisé par le locataire peut relever le prix ou refuser.
- **Holding** : 1,5 M€ (central), 2,2 M€ (frugal_holding) ou 2,9 M€ + 0,25 M€ (cible) à mobiliser **en 2031**, à partir de reprises de PME non encore faites (R4). Le TRI fondateur de C_cible est de −5,4 % : la holding transfère ≈ 3,15 M€ de valeur de PME dans un actif qui vaut ≈ 2,35 M€ en fonds propres en an 10. C'est un **choix de vie financé par des PME**, ce qui est légitime à condition d'être assumé comme tel.
- **Opérationnel** : reprendre et redresser des PME (2027-2031) **tout en** exploitant un domaine loué dès l'an 1, c'est deux métiers à plein temps (R5).
- **C_cible après stress** : NON VIABLE sous 7 stress sur 7 (`Stress_tests.md` §4), avec un cash-flow libre négatif dès l'an 8 même sans stress.
- **Verdict auditeur** :
  - C_central et C_frugal_holding : **ÉLIMINÉS** (trésorerie négative) ;
  - C_cible : **CONSERVÉ SOUS CONDITIONS**, avec un séquencement modifié :
    1. PME d'abord, sans exploiter de domaine en parallèle ;
    2. éventuellement un petit test équestre (pension) sur une structure louée sans château ;
    3. achat seulement quand la trésorerie de la holding est **disponible et non nantie**, et quand une réserve de 0,4 à 0,6 M€ est constituée.

### Variante D — Bien modeste et isolé (~1,4 M€, Aubusson-type)
- Trésorerie −1,85 M€, DSCR 0,62 en régime. Le ticket est plus bas, mais le capex est plus lourd (1,3 M€ : château du XVe à restaurer, écuries à créer). Le bassin de clientèle pour les pensions premium et les mariages est le plus faible (Creuse).
- Annonce convertie de la livre sterling, disponibilité non vérifiée (agent 1).
- **Pessimisme possible** : un bien de 85 ha de prairies sans écuries peut porter un modèle **pension au pré / retraite + élevage** à capex faible (30-80 k€ selon l'agent 3), au lieu d'un capex équestre de 400 k€. Le modèle D n'a pas testé cette version.
- **Verdict auditeur : ÉLIMINÉ tel que modélisé.** À retester en version « sans dette, capex minimal, pension au pré » (§8).

---

## 5. Scénarios que j'élimine (avec justification)

| Scénario | Décision | Justification principale |
|---|---|---|
| A_central, A_prudent, A_optimiste, A_frugal | **Éliminés** | DSCR max 0,17 ; aucune variante ne couvre la dette ; dépendance aux lignes équestres les moins prouvées ; TRI investisseurs non calculable (perte) |
| B_central, B_prudent, B_optimiste | **Éliminés** | Même l'optimiste brûle 2,1 M€ ; la dette de 2,8 M€ est 3 à 7 fois la dette soutenable |
| B_frugal | **Éliminé** | DSCR 0,34-0,80 ; trésorerie −1,74 M€ ; fondateur non payé |
| B_sans_dette, B_frugal_sans_dette | **Rétrogradés en simples diagnostics** | Investisseurs à TRI négatif ; après correction des erreurs E1-E4, plus de cash-flow libre |
| C_central, C_frugal_holding | **Éliminés** | Trésorerie négative ; phase locative coûteuse ; holding non constituée |
| D_bien_modeste | **Éliminé tel quel** | DSCR 0,62 ; trésorerie −1,85 M€ ; à retester autrement |
| **C_cible** | **Conservé sous 5 conditions** (§8) | Seule voie qui garde le contrôle ; dette ≤ dette soutenable ; mais fonds propres non acquis et C_cible FRAGILE même sans stress |

Je contredis donc toute présentation qui ferait de B_frugal_sans_dette le scénario recommandé : **il ne l'est pas après correction.**

---

## 6. Où l'équipe a pu être TROP pessimiste

| # | Biais pessimiste | Preuve | Effet estimé | Change-t-il le verdict ? |
|---|---|---|---|---|
| P1 | **Prix d'achat non négocié** alors que le vendeur sort d'une liquidation (Ygrande, A8-01) ; Hus −35 % en un an ; vente d'un château en 18-24 mois (A8-16) | A8-01, A8-16, agent 7 | −15 à −30 % de prix, soit −0,4 à −0,8 M€ d'emplois (ESTIMATION) | Non pour A/B (le problème est l'EBITDA) ; **oui en partie pour C_cible** (fonds propres requis ramenés vers 2,4-2,7 M€) |
| P2 | **Équipements existants recomptés** : Ygrande a un manège couvert, des carrières, une piste de galop, 24 boxes, une capacité de plus de 80 chevaux, un restaurant et 16-19 chambres (A8-02, A8-03), mais A prévoit 450 k€ et B 250 k€ de capex équestre, plus 480 k€ d'événementiel | A8-02, A8-03 | −150 à −400 k€ de capex (ESTIMATION, sans visite) | Non (le capex n'est pas le facteur limitant) |
| P3 | **Taxe foncière à 15 k€** contre 2,6-4,0 k€ dans deux annonces de châteaux (V2-06, V2-14) et 3-8 k€ estimés par la vague 2 | V2-06, V2-14 | +7 à +12 k€ d'EBITDA/an | Non |
| P4 | **Hébergement existant inexploité** : les 16-19 chambres du bien de référence pourraient porter des forfaits mariage avec nuitées (les tarifs observés « avec hébergement » vont jusqu'à 7 000-12 325 €, A4-11) | Agent 4, A8-02 | +20 à +50 k€ de CA potentiel (ESTIMATION) | Non, et c'est précisément le modèle (hôtel, restaurant) qui a échoué sur ce site |
| P5 | **Plafond de 18 mariages** : des lieux déclarent 10-30 ou 30-50 mariages par an (fiches Bridebook, déclaratif, A8-09) ; un guide commercial cite 25-50 (A8-08, fiabilité faible) | A8-08, A8-09 | +5 à +10 mariages, soit +25 à +50 k€ de CA HT | Non, et cela aggrave R9 (vie privée, chevaux) |
| P6 | **Pas de reprise d'un fonds événementiel déjà en activité** (avec comptes, avis et réservations) : de tels biens existent sur le marché (annonce d'un domaine événementiel « clé en main » dans la vallée de la Loire, ≈ 750 demandes de réservation par an, A8-22, faible) | A8-22, V2-54 | Montée en charge supprimée ; dossier bancaire avec historique | **Oui potentiellement** pour la bancabilité, mais au prix d'achat d'un fonds et en s'éloignant du cheval |
| P7 | **Subventions à zéro** (règle de prudence correcte) : DRAC 20-40 % sur parties protégées, régions jusqu'à 300 k€ / 10 ans (agent 2) | Agent 2 | −0 à −20 % du capex si MH (non acquis) | Non |
| P8 | **Effet ciseau** inflation des charges 2,5 % contre prix 2 % sur 10 ans | Hypothèse | ≈ −5 % de marge cumulée | Non |

**Bilan** : les biais pessimistes valent au plus +20 à +60 k€ d'EBITDA/an et −0,5 à −1,2 M€ de besoin d'investissement. Les biais optimistes (E1, E2, §3.2) valent environ −70 à −110 k€ d'EBITDA/an. **Le solde reste défavorable.** Le levier pessimiste le plus utile est le prix d'achat (P1) : il aide C_cible, pas A ni B.

---

## 7. Notation indépendante sur 100

Grille : Faisabilité du financement /25, Résilience économique /25, Qualité et réalité de l'activité équestre /20, Contrôle patrimonial /15, Faisabilité juridique et opérationnelle /10, Potentiel de développement /5.

| Scénario | Fin. /25 | Résil. /25 | Équestre /20 | Contrôle /15 | Jur./op. /10 | Dév. /5 | **Total** | Incertitude |
|---|---|---|---|---|---|---|---|---|
| A_central (et prudent) | 2 | 1 | 11 | 4 | 3 | 3 | **24** | ±8 |
| A_optimiste | 2 | 3 | 11 | 4 | 3 | 3 | **26** | ±8 |
| A_frugal | 3 | 4 | 11 | 4 | 2 | 4 | **28** | ±8 |
| B_central (et prudent) | 2 | 2 | 9 | 4 | 4 | 5 | **26** | ±8 |
| B_optimiste | 2 | 5 | 9 | 4 | 4 | 5 | **29** | ±8 |
| B_frugal | 3 | 6 | 9 | 4 | 3 | 5 | **30** | ±8 |
| B_frugal_sans_dette (diagnostic) | 1 | 10 | 9 | 2 | 3 | 5 | **30** | ±10 |
| C_central | 4 | 2 | 10 | 11 | 3 | 3 | **33** | ±10 |
| C_frugal_holding | 5 | 6 | 10 | 11 | 3 | 3 | **38** | ±10 |
| **C_cible** | 7 | 11 | 10 | 12 | 4 | 3 | **47** | ±12 |
| D_bien_modeste | 4 | 5 | 8 | 5 | 4 | 3 | **29** | ±10 |

**Justification par critère :**

- **Financement**
  - A et B : dette 3 à 7 fois supérieure à la dette soutenable, investisseurs à TRI négatif. Je ne mets pas zéro uniquement parce qu'un vendeur motivé (Ygrande en liquidation) peut accepter un crédit-vendeur. B_frugal_sans_dette (1) : 4,2 M€ de fonds propres externes à TRI négatif, sans aucune source identifiée.
  - C : la dette demandée est raisonnable (0,9-1,9 M€) et une holding peut se porter caution, mais 1,5 à 3,15 M€ de fonds propres de holding **n'existent pas aujourd'hui**. C_cible (7) a la meilleure note parce que sa dette est calibrée sur la capacité de remboursement.
- **Résilience**
  - Fondée sur la trésorerie minimale, le DSCR et les stress tests, après mes corrections E1-E2.
  - C_cible (11) : DSCR 1,21 sans stress, mais NON VIABLE sous 7 stress sur 7.
  - B_frugal_sans_dette (10) : aucune dette, mais cash-flow libre ≈ 0 après correction.
- **Activité équestre**
  - A a le plus de cheval, mais la moitié est spéculative (showcases, concours, stages) : 11/20.
  - B et C reposent sur la pension box et pré, réelle et récurrente, mais sur des prix surestimés : 9-10/20.
  - D : écuries à créer dans un bassin faible : 8/20.
- **Contrôle**
  - A et B : 35 % du capital, 51 % des votes non acquis, clause résolutoire, nantissements, sortie forcée des investisseurs : 4/15.
  - B_frugal_sans_dette : environ 6 % du capital en partage équitable : 2/15.
  - C : 100 % via la holding, mais sans maîtrise de l'actif pendant la location et option non acquise : 11-12/15.
- **Juridique et opérationnel** : PLU, ERP, SAFER, bruit et bail rural pèsent sur tous les scénarios. Les variantes frugales perdent 1 point (fondateur saturé). C perd des points pour le cumul PME + domaine.
- **Développement** : B, le plus diversifié, a la meilleure note ; C et D ont le moins de leviers.

**Sources d'incertitude des notes** : pas de bien réel visité ; pas de devis ; prix de pension locaux inconnus ; apport réel du fondateur inconnu (S2 = hypothèse) ; raison de la liquidation d'Ygrande inconnue ; montant réel de la TVA applicable (pension « accessoire indissociable » à 5,5 % possible si le contrat est bien rédigé : un écart d'environ ±13 % sur le prix net, selon l'agent 3).

**Aucun scénario n'atteint 50/100.** Pour l'auditeur, aucun ne mérite en l'état d'engager l'apport du fondateur dans une acquisition.

---

## 8. Conditions minimales pour qu'un scénario redevienne défendable (tests go / no-go)

1. **Fonds propres disponibles, pas prévus** : trésorerie de holding ou apport en banque ≥ (prix négocié + frais + travaux + 0,5 M€ de réserve − dette soutenable). Sinon : no-go.
2. **Dette ≤ dette soutenable** calculée sur un EBITDA **HT, corrigé de E1-E2, après gros entretien et après rémunération du dirigeant**.
3. **Due diligence du site** avant offre :
   - PLU « étoilé » ou STECAL ;
   - avis SDIS sur la salle ;
   - diagnostic d'architecte du patrimoine ;
   - cahier des charges SAFER ;
   - **comptes et rapport du liquidateur** si le bien est Ygrande.
4. **Preuve de demande équestre locale** : relever 20 grilles de pension dans un rayon de 30 km (méthode de l'agent 3), et obtenir des lettres d'intention de propriétaires de chevaux (sans contact pendant cette mission : action à mener plus tard par le porteur).
5. **Séquencement** : pas d'exploitation d'un domaine en parallèle d'une reprise de PME. Un test équestre éventuel se fait sur une petite structure louée sans château (loyer et charges faibles), pas sur un château loué à 100 k€/an.

Scénarios à **ajouter au modèle** pour vérifier si l'équipe est trop pessimiste :
- (i) C_cible avec prix −20 % et capex −30 % (équipements existants) ;
- (ii) D en version « pension au pré + élevage », sans dette, capex équestre ≤ 100 k€ ;
- (iii) reprise d'un domaine événementiel déjà exploité (fonds + murs), sur comptes réels, avec ajout progressif des chevaux.

---

## 9. Points de doute / hypothèses non vérifiées

1. **WebFetch bloqué** : toutes mes sources sont des extraits de moteur. La liquidation de Groupe Cœur et Détente (A8-01) vient d'une base juridique privée (doctrine.fr) : à confirmer au BODACC.
2. **Identité Ygrande** : je **déduis** que la SAS liquidée exploitait le domaine aujourd'hui vendu par la SAFER (même commune, même activité hôtelière et équestre, vente SAFER en 07/2026). Le lien exact (propriétaire des murs ≠ exploitant ?) est **INCONNU**. Vérification : annonce SAFER 03 ET 26 YGR1, matrice cadastrale, BODACC.
3. **TVA** : la doctrine trouvée (BOFiP 2021, actualité 2024) exclut la pension du taux réduit dans sa version ancienne. La version 2026 n'a pas été lue. Mon correctif E2 (taux mixte ≈ 12,75 %) est une ESTIMATION fondée sur la tolérance 50/50. Les tarifs de mariage sont supposés TTC, sans vérification lieu par lieu.
4. **Volumes de mariages par lieu** (A8-08, A8-09) : déclaratifs ou commerciaux, fiabilité faible. L'attribution exacte de la fiche Bridebook qui donne « 10-30 / 30-50 mariages » n'est pas certaine.
5. **Délai de vente de 18-24 mois et ≈ 400 transactions/an** : chiffres d'une agence (Kretz) relayés par la presse (A8-16).
6. **Défaillance des reprises de PME** : aucun taux chiffré pour les repreneurs personnes physiques n'a été trouvé (A8-17 porte sur des LBO 2000-2010). Je ne sais pas quel est ce taux. Méthode : observatoire CRA, études Bpifrance « transmission ».
7. **Apport bancaire usuel** : sources commerciales (A8-19, A8-20), fiabilité faible ; elles concordent avec V2-05 et V2-48.
8. **Salaire et coût employeur** : SMIC 2026 de 12,31 €/h selon une source non officielle (A8-21), à vérifier sur service-public.fr. Le coût chargé de 25 k€ par soigneur reste plausible (22,6-25 k€/an, mon calcul sur les fourchettes trouvées).
9. Mes corrections chiffrées (§3.3) sont des **calculs manuels sur l'an 5**. Elles doivent être réintégrées dans `hypotheses.py` / `build_model.py` puis recalculées.
10. **Contre-hypothèse (règle 8)** : je n'ai trouvé **aucun cas** documenté de château équestre de plus de 40 ha, acheté à crédit par un primo-entrepreneur sans fortune, qui couvre sa dette par son exploitation. Les seuls cas proches (Chazemais, Sarthe, Bourneau) affichent des CA de 90-190 k€, incompatibles avec un service de dette de plus de 150 k€/an.
