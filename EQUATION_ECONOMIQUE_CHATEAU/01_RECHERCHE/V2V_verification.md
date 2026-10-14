# V2V — Vérification indépendante des chiffres les plus influents

Agent : V2V (vérification). Date : 2026-10-14. Statut du fichier : TERMINÉ.

## Méthode

- Pour chaque chiffre de la liste du directeur (`00_PILOTAGE/Prompts_agents.md`, section V2V), j'ai rouvert l'URL inscrite dans `01_RECHERCHE/sources/sources_*.csv`, sans réutiliser les fichiers téléchargés par les autres agents (dossier de travail propre : `scratchpad/v2v/`).
- PDF : téléchargés avec curl depuis l'URL officielle, texte extrait avec `pdftotext -layout`, puis recherche de la citation. Pages HTML : WebFetch, et curl quand il faut une citation mot pour mot.
- Verdicts :
  - **CONFIRMÉ** : chiffre, unité, année, périmètre et HT/TTC conformes à la source ;
  - **NUANCÉ** : chiffre présent, mais une précision change la lecture (périmètre, unité, année, HT/TTC, statut, arrondi) ;
  - **NON CONFIRMÉ** : chiffre absent de la source ou différent ;
  - **INACCESSIBLE** : source non ouverte ; aucune conclusion n'est tirée à sa place.
- Recommandation pour le modèle : garder / corriger (nouvelle valeur) / retirer.
- Les identifiants V2V-xx renvoient à `sources/sources_V2V.csv` (une ligne par URL rouverte).

## Résultats détaillés

### Item 1 — Entretien et réparation = 2 à 4 % de la valeur de remplacement par an, « minimum absolu » (R1-07, R1-08)

- Sources rouvertes : [V2V-01] (NRC 2001, p. 46), [V2V-02] (NRC 1990, p. xii), [V2V-03] (NRC 1990, p. 6-7 et 17-19). PAGE LUE. Sur le site, le texte de 1990 n'est disponible qu'en images de pages, que j'ai lues visuellement.
- Citations exactes :
  - NRC 1990, p. xii, recommandation 1 : « An appropriate budget allocation for routine M&R for a substantial inventory of facilities will typically be in the range of 2 to 4 percent of the aggregate current replacement value of those facilities (excluding land and major associated infrastructure). In the absence of specific information upon which to base the M&R budget, this funding level should be used as an absolute minimum value. Where neglect of maintenance has caused a backlog of needed repairs to accumulate, spending must exceed this minimum level until the backlog has been eliminated. »
  - NRC 1990, p. 18 : « the appropriate level of M&R spending should be, on average, in the range of 2 to 4 percent of current replacement value of the inventory », avec la note 12 : « This rule is based on the committee's combined judgment. » ; « for any one building may be outside the proposed range » ; « This 2 to 4 percent range is most valid as a budget guide for a large inventory of buildings and over time periods of several years » ; « even with small inventories the 2 to 4 percent rule of thumb may be applied over a longer period of time, such as 5 to 10 years ».
  - NRC 1990, p. 7 (définitions) : « Replacement is typically funded in maintenance and repair budgets. » ; les coûts d'« Operations » (énergie, nettoyage, etc.) et les « Alterations » (améliorations) « are not maintenance ».
  - NRC 2001, p. 46 : reprend la citation de 1990 ; les agences fédérales déclaraient un financement « less than 2 percent of the aggregate current replacement value ».
- Verdict : **CONFIRMÉ**. Chiffre, unité (% par an de la valeur de remplacement à neuf), année (1990, cité en 2001) et périmètre (parcs importants de bâtiments publics américains) conformes à ce qu'écrit R1. « Absolute minimum value » figure bien dans le texte, mais **sous condition** (« in the absence of specific information »). La règle relève du « jugement » du comité et non d'une mesure.
- Précisions utiles au modèle : la règle inclut le remplacement de composants (donc le gros entretien), exclut l'énergie, le ménage, les améliorations et la résorption d'un retard d'entretien. Le découpage du modèle (0,75 % courant + 2,25 % gros entretien = 3 %, énergie et améliorations comptées à part) est cohérent avec ces définitions.
- Recommandation : **garder** (2 à 4 %, central 3 %). Passer le statut de la citation « absolute minimum » de EXTRAIT à PAGE LUE. L'URL de R1-08 (chapitre 4, p. 17-20) ne contient pas cette phrase : elle se trouve p. xii (chapitre 1, « Front Matter », [V2V-02]). Ajouter dans la note du paramètre : « pour un seul bâtiment, la valeur peut sortir de la fourchette ; moyenne sur 5 à 10 ans ».

### Item 2 — Château de 2 500 m² acheté 600 000 €, valeur de reconstruction 6 M€ ; prime « rarement inférieure à 2 500 € » pour un bien classé (R1-26)

- Source rouverte : [V2V-04]. curl a été refusé (connexion réinitialisée) ; le PDF obtenu par WebFetch a été converti par pdftotext. PAGE LUE.
- Citations exactes (Le Figaro, 25/02/2020, journaliste Anne Michel, propos de D. de La Fouchardière, SLA-Verspieren) : « Selon Dominique de La Fouchardière, le niveau de la prime d'assurance annuelle pour un bien classé est rarement inférieur à 2500 € et il ne connaît pas de limite supérieure. Il l'estime justifié: «Un château de 2500 m2 acheté 600.000 €, par exemple, pourra avoir une valeur de reconstruction de 6 millions d'euros» ». Plus haut : « La surface développée, qui intègre tous les mètres carrés mesurés en extérieur des murs, y compris ceux des caves et greniers, est ici essentielle. »
- Verdict : **CONFIRMÉ** (chiffres, année 2020, périmètre « bien classé »). Deux précisions : (a) c'est un **exemple** de courtier (« par exemple »), pas une observation ; (b) l'article ne dit pas si les 2 500 m² de l'exemple sont une surface développée ou habitable. La note du paramètre `S1_vr_m2` (« surface développée ») ajoute donc une précision absente de la source. HT/TTC non précisé (une prime d'assurance n'est pas soumise à la TVA).
- Recommandation : **garder** comme borne basse, en corrigeant la note de `S1_vr_m2` : « exemple d'un courtier, type de surface non précisé ». Le ratio de 2 400 €/m² reste une ESTIMATION à partir d'un exemple unique de 2020.

### Item 3 — Reconstruction 5 000 à 10 000 €/m² ; prime ≈ 5 ‰ (R1-27)

- Source rouverte : [V2V-05]. PAGE LUE (page datée « 21 novembre 2025 », « Mis à jour le 25 mai 2026 »).
- Citations exactes : « La prime annuelle d'assurance château se calcule sur la base de 5 ‰ (0,5 %) de la valeur totale assurée, soit 15 000 à 30 000 € pour un château de 600 à 1 200 m² » ; « Le coût de reconstruction d'un château oscille entre 5 000 et 10 000 €/m², contre 1 200 à 1 800 €/m² pour une maison standard (source : Fédération Française du Bâtiment). »
- Verdict : **CONFIRMÉ** (chiffres présents tels quels). La fiabilité reste **faible** : contenu commercial d'un courtier. La mention « (source : Fédération Française du Bâtiment) » est placée après le chiffre de la maison standard : rien n'indique que la FFB soit la source du chiffre « château ». La « valeur totale assurée » inclut dépendances et objets d'art. La même page donne une formule « essentielle » à 8 000-15 000 € pour 2,5 à 4 M€ de valeur de reconstruction, soit 0,32 % à 0,375 %, donc **moins** que 5 ‰ : la page n'est pas cohérente avec elle-même.
- Recommandation : **garder** comme borne haute (scénario défavorable). Le modèle utilise déjà 3 ‰ en central et 5 ‰ en défavorable : c'est prudent et justifié.

### Item 4 — Dépense annuelle d'entretien et de réparation 156 067 à 160 686 £ TTC ; retard moyen ≈ 1 994 000 £ (R1-05)

- Source rouverte : [V2V-06]. PAGE LUE (pdftotext).
- Citations exactes : « The average reported VAT-inclusive expenditure on repair and maintenance of the respondents' main heritage asset was £156,067 per year. When the cases where there is a disparity […] are inflated […], the average annual expenditure increases to £160,686. These two figures represent the reasonable minimum and maximum possible average expenditures based on the reported data. » ; « Among these respondents, the average estaimted [sic] total repair need amounted to just under £1,994,000. » (88 réponses sur 115 propriétés ayant besoin de réparations) ; l'enquête a été ouverte « on 10 July 2024 and closed on 12 August 2024 » (121 réponses valides) ; la dépense porte sur « the last year ».
- Verdict : **CONFIRMÉ**. TVA comprise : oui (« VAT-inclusive »). Le taux de TVA effectif constaté est de 17,9 % à 18,5 % de la dépense **hors TVA** (méthode du rapport, §3.4.3), et non 20 % : une partie des dépenses n'est pas taxée au taux normal. Pour passer au hors TVA, diviser par ≈ 1,18 et non par 1,20. Le retard est déclaré par les propriétaires (près de 60 % sur leur seul jugement, d'après le rapport, qui y voit plutôt une sous-estimation).
- Recommandation : **garder**.

### Item 5 — « 40 000 € / an minimum » hors ouverture et restauration ; moins de 2 000 visiteurs par monument ; 99,8 % non rentables (R1-01)

- Source rouverte : [V2V-07]. PAGE LUE (pdftotext ; note datée du 27 mai 2019).
- Citations exactes : « En moyenne le coût d'entretien d'un monument (hors ouverture au public et travaux de restauration) est de 40 000 € / an minimum (assurance, impôts locaux, emploi d'un gardien, travaux minimum d'entretien…). » ; « en dehors des zones touristiques très fréquentées, et des monuments emblématiques qui accueillent quasiment l'ensemble des visiteurs, la moyenne de la fréquentation est établie à moins de 2 000 visiteurs par an, par monument. » ; « Pour 99,8 % des propriétaires, la seule activité d'ouverture à la visite n'est donc pas rentable et généralement déficitaire (cf. tableau en annexes). »
- Verdicts :
  - 40 000 €/an minimum : **CONFIRMÉ** (HT/TTC non précisé ; € 2019, à actualiser en € 2026) ;
  - moins de 2 000 visiteurs : **NUANCÉ**. La source limite cette moyenne aux monuments situés « en dehors des zones touristiques très fréquentées » et non « emblématiques », restriction absente de la citation de R1. Sur l'ensemble des adhérents, la moyenne est plus élevée : la même note indique que « près de la moitié » des plus de 3 000 monuments accueillent ensemble « plus de 9 millions de visiteurs » ;
  - 99,8 % : **CONFIRMÉ** (citation exacte), mais le « tableau en annexes » qui fonde ce chiffre **ne figure pas** dans le PDF de 3 pages : la méthode n'est pas vérifiable.
- Recommandation : **garder** les trois chiffres ; compléter la citation des 2 000 visiteurs par sa restriction (R1, §1.1 et contre-exemple 4).

### Item 6 — Taux moyens de la DRAC 20 % (inscrit) et 40 % (classé) ; crédits d'intervention −29 % en CP en 2026 (R1-34)

- Sources rouvertes : [V2V-08] (Sénat) ; contrôle croisé avec [V2V-09] (Assemblée nationale, R1-33). PAGE LUE.
- Citations exactes (Sénat) : « Les crédits d'intervention des directions régionales des affaires culturelles (Drac) seront en baisse de 38 % en AE (-163 millions d'euros) et de 29 % en CP (-172 millions d'euros). » ; « Le taux de participation aux projets est en moyenne de 20 % pour les monuments inscrits et de 40 % pour les monuments classés. »
- Citation (Assemblée nationale, R1-33) : « Ces crédits, qui s'élevaient à 143 millions d'euros en AE et 128,7 millions d'euros en CP dans le PLF 2025, s'élèvent à 91,5 millions d'euros en AE et 112 millions d'euros en CP dans le PLF 2026, soit une baisse de plus d'un tiers des crédits (– 36 %) en AE et de 13 % en CP. »
- Verdict :
  - taux 20 % / 40 % : **CONFIRMÉ**. Ce sont des taux moyens **sur les projets subventionnés** : ils ne s'appliquent ni à toute la dépense d'entretien ni à tous les propriétaires ;
  - −29 % en CP : **NUANCÉ**. Le chiffre figure bien dans l'avis du Sénat, mais il s'agit du **projet** de loi de finances (PLF 2026), pas de la loi votée. L'Assemblée nationale donne, pour les « crédits déconcentrés consacrés aux dépenses d'intervention » sur les monuments, orgues et objets mobiliers, **−13 % en CP** (128,7 → 112 M€). Les deux périmètres diffèrent : −172 M€ représentant 29 %, la base du Sénat est d'environ 593 M€ (ESTIMATION arithmétique), bien plus large que les 128,7 M€ de l'Assemblée.
- Correction à apporter : la ligne 9 des « Chiffres clés » de R1 (« 112 M€ en CP, soit −29 % (−172 M€) ») associe deux sources de périmètres différents. C'est arithmétiquement impossible (112 M€ ne peut pas résulter d'une baisse de 172 M€ égale à 29 %). Écrire : « −29 % en CP (−172 M€) selon le Sénat, périmètre large ; 128,7 → 112 M€ en CP (−13 %) selon l'Assemblée nationale, crédits d'intervention déconcentrés ; PLF, montants votés non vérifiés ».
- Recommandation : **garder** 20 % / 40 % ; **corriger** la formulation du −29 % comme ci-dessus. Le modèle ne retient pas la subvention dans le total : pas d'impact chiffré.

### Item 7 — Résiliation de l'assurance du château d'Olhain, fermeture au 01/01/2026 (R1-28)

- Source rouverte : [V2V-10]. PAGE LUE.
- Citation exacte : « Par courrier en date du 27 octobre 2025, l'assureur du site a décidé de résilier le contrat d'assurance le liant à l'association gestionnaire, sans mentionner de motif particulier. Depuis le 1er janvier 2026, le site est dépourvu de couverture assurantielle, ce qui a conduit à sa fermeture totale au public pour une durée indéterminée. » ; « Aucun sinistre n'a été déclaré sur le site depuis 2015. Plus de 300 000 euros de cotisations ont été versés à l'assureur au cours des quarante dernières années. » Question publiée au JO le 17 février 2026, réponse le 28 avril 2026.
- Verdict : **CONFIRMÉ**. Ce sont les affirmations du député ; la réponse du gouvernement ne les conteste pas. La moyenne de 7 500 €/an tirée par R1 est un minimum nominal (« plus de 300 000 € » sur 40 ans).
- Recommandation : **garder**.

### Item 8 — Électricité : 1 072 € pour 4,5 MWh ; gaz : prix repère 194,90 €/MWh au 1er novembre 2026 (R1-24, R1-25)

- Sources rouvertes : [V2V-11], [V2V-12]. PAGE LUE.
- Citations exactes : « Le niveau moyen des TRVE est relevé de + 5,98 € TTC/mégawattheure. Cela représente une augmentation moyenne nette de la facture d'électricité d'environ 26 € TTC par an (exemple : pour une consommation moyenne de 4,5 MWh par an, la facture TTC passera de 1 046 € à 1 072 €). » (publié le 21 juillet 2026, hausse au 1er août 2026) ; « le prix repère de vente de gaz s'établira à 194,90 € TTC par mégawattheure (MWh), contre 182,88 € TTC/MWh en octobre » ; le prix repère « représente une estimation moyenne des coûts supportés par les fournisseurs au titre de la fourniture de gaz naturel pour un client résidentiel ».
- Verdict : **CONFIRMÉ** (montants, TTC, dates). Précisions : l'électricité est celle d'un client résidentiel au tarif réglementé (238 €/MWh abonnement compris = ESTIMATION de R1) ; le prix repère du gaz est **indicatif** et **mensuel** (+6,3 % en octobre, +6,6 % en novembre 2026). Retenir une valeur de novembre comme constante 2026 est un choix de modélisation volatil.
- Recommandation : **garder** ; signaler dans la note de `prix_chaleur_kwh` que 19,49 c€ est la valeur d'un seul mois (novembre 2026), après deux hausses successives.

### Item 9 — SMIC 12,31 €/h au 01/06/2026 ; RGDU : coefficient 0,3981 (R2-01, R2-02)

- Sources rouvertes : [V2V-13], [V2V-14]. PAGE LUE.
- Citations exactes : tableau « Montants du Smic » : « Smic horaire 12,31 € » brut, « Smic mensuel 1 867,02 € », « Smic annuel 22 404,20 € » (page « Vérifié le 01 juin 2026 », référence « Arrêté du 22 mai 2026 relatif au relèvement du salaire minimum de croissance ») ; RGDU : « Le coefficient ne peut toutefois pas excéder la somme des valeurs T min et T delta , soit 0,3981 » (moins de 50 salariés ; 0,4021 à partir de 50 salariés) ; « Il a été décidé de conserver la valeur du Smic applicable au 1 er janvier 2026 » dans la formule (SMIC annuel de référence 21 876,40 €).
- Verdict : **CONFIRMÉ** pour les deux chiffres. Précision : 0,3981 est le coefficient **maximal**, atteint à un salaire égal au SMIC de **janvier**. Comme la formule garde le SMIC de janvier, un salarié payé au SMIC de juin (1 867,02 €) a un coefficient d'environ **0,375** (calcul : 700,13 / 1 867,02, montant confirmé par le simulateur URSSAF, item 10). Le modèle utilise les coûts du simulateur et non le coefficient : aucun impact.
- Recommandation : **garder** ; préciser « coefficient maximal » partout où 0,3981 est cité.

### Item 10 — Coût employeur à 1 ; 1,5 et 2,5 SMIC = 23 853 € ; 44 118 € ; 78 982 € (R2-11)

- Source rouverte : [V2V-15]. Trois calculs refaits par l'API publique du simulateur (CDI, temps plein, effectif 10, autres paramètres par défaut, « date » renvoyée : 01/07/2026, SMIC du moteur : 1 867,02 €/mois).
- Résultats obtenus :
  - 1 SMIC (1 867,02 €/mois) : coût total employeur 1 987,76 €/mois, soit **23 853,17 €/an** ; RGDU 700,13 €/mois ;
  - 1,5 SMIC (2 800,53 €) : 3 676,54 €/mois, soit **44 118,48 €/an** ;
  - 2,5 SMIC (4 667,55 €) : 6 581,79 €/mois, soit **78 981,51 €/an**.
- Verdict : **CONFIRMÉ** (trois points sur trois, au centime près). Rappel du périmètre : régime général, hors convention collective, hors MSA (salariés agricoles et équestres), hors primes et 13e mois.
- Recommandation : **garder**.

### Item 11 — Villandry : 10 jardiniers pour 7 ha (R2-15)

- Source rouverte : [V2V-16]. PAGE LUE (WebFetch et curl).
- Citations exactes : « Combien de jardiniers pour s'occuper du jardin de Villandry ? » — « Ils sont dix à s'en occuper au quotidien, même l'hiver ! » ; « Soit, au total, 7 hectares de jardin. » (article du 17/01/2024, propos d'Henri Carvallo, propriétaire).
- Verdict : **CONFIRMÉ**. Les 7 ha comprennent le potager décoratif (1 ha), le jardin d'ornement, la pièce d'eau et le jardin du soleil. « Dix » est un effectif déclaré, pas un nombre d'ETP publié.
- Recommandation : **garder** (comme plafond, ainsi que R2 le fait).

### Item 12 — Tracteur de 100 à 140 ch : 101 464 € HT, 10,7 ans (R2-30)

- Source rouverte : [V2V-17]. PAGE LUE (pdftotext, fiche p. 49).
- Citation exacte (fiche « TRACTEUR 100 - 140 CV ») : « prix d'achat moyen 83 098 € […] 101 464 € » (colonne « simulation 2026 », « simulation des coûts sur la base des prix récents constatés ») ; « durée d'amortissement 10,7 ans » ; échantillon 335 ; utilisation annuelle 576 h.
- Verdict : **CONFIRMÉ**. 10,7 ans est la durée d'amortissement **moyenne du parc** (2023-2024) ; 101 464 € est le prix **récent simulé** pour 2026. La mention HT n'est pas écrite sur cette fiche (elle l'est sur d'autres fiches du guide) : HT par cohérence, comme l'a noté R2. Le guide couvre les régions de l'Est, pas toute la France.
- Recommandation : **garder**.

### Item 13 — Blenheim : billetterie 11 068 k£, coûts 16 360 k£, 700 000 visiteurs, « restauration » 2,5 M£ (objectif 4 M£), toiture 10,4 M£ (R5-03)

- Source rouverte : [V2V-18]. PAGE LUE (scan lu en image, pages 9, 10, 29 et 43).
- Citations exactes : état des activités, « Operation of the Palace and park 11,068 » (£000, 2025) ; note 7 : « Costs (16,360) », « Admission charges 9,546 », « Gift aid recovered on donated admissions 1,522 », « Net cost funded from other income (2,237) » ; p. 9 : « Paying visitor numbers for the year ended 31 March 2025 totalled 700,000 (2024: 698,000). » ; p. 10 : « we have spent £2.5m (2024: £3.2m) on preservation and restoration work (note 6). We aim to spend an average of £4m each year on conservation and restoration. » et « a major restoration project focused on a significant section of the Palace roof. The works are expected to span two years with an allocated budget of £10.4m. »
- Verdict : **CONFIRMÉ**. Précisions de lecture : les 11 068 k£ comprennent 1 522 k£ de Gift Aid (avantage fiscal britannique), pas seulement des billets ; « restauration » signifie ici **travaux de conservation**, pas la restauration commerciale ; les 10,4 M£ de toiture sont un budget de projet **sur deux ans**.
- Recommandation : **garder**.

### Item 14 — Chatsworth : 630 114 visiteurs ; entretien des jardins, du parc et des bois 1 781 k£ ; 29 jardiniers (R5-05)

- Source rouverte : [V2V-19]. PAGE LUE (scan lu en image ; la pagination imprimée est décalée de 2 pages par rapport au PDF).
- Citations exactes : p. 11 : « Visitor Numbers 630,114 » (2025) ; « Visitor numbers shown are visitors to the House, the Garden and/or the Farmyard and include visits by holders of Estate Passes (members of staff, pensioners and some tenants) and Friends of Chatsworth. Visitors to the park only and to events taking place in the park are not included » ; note 9 : « Maintenance of the garden, park and woods 1,781 » (£000, 2025) ; note 12 : « The average number of persons employed by the Charity during the year » : « Gardens 29 » (total 170 ; « average monthly head count was 348 staff »).
- Verdict : **CONFIRMÉ**. Précision : les 630 114 visiteurs **ne sont pas tous payants** (détenteurs de pass et « Friends » inclus). La « leçon » de R5 (« 600 000 visiteurs payants ») est donc légèrement inexacte. Les 29 sont des personnes employées en moyenne, pas des ETP publiés.
- Recommandation : **garder** ; dans R5, remplacer « visiteurs payants » par « visiteurs (pass et membres inclus) ».

### Item 15 — Burghley : revenu immobilier net 3,52 M£ ; dépenses caritatives 4,69 M£ (R5-07)

- Source rouverte : [V2V-20]. PAGE LUE (scan lu en image ; pagination imprimée décalée d'une page).
- Citations exactes : p. 26 : « The investment property portfolio generated net revenue of £3,520,257 (2025: £3,196,593) » ; p. 39 (état consolidé, exercice clos le 31/01/2026) : « Expenditure on charitable activities […] 4,689,993 » (total) ; « Income from investments 5,353,529 ».
- Verdict : **CONFIRMÉ**. Les 4,69 M£ ne couvrent que les activités caritatives : les coûts des activités commerciales (11,82 M£, « raising funds ») sont à part.
- Recommandation : **garder**.

### Item 16 — Pensions des cas-types 2025 : 334 / 401 / 568 € HT par mois (R6-02)

- Source rouverte : [V2V-21]. PAGE LUE (pdftotext).
- Citation exacte (« Tableau 9 — Référentiel de produits 2025 ») : « Pension box hébergement (en €HT/mois) […] 334 € [EQCE2] 401 € [EQCE3] » ; « Pension box travail (en €HT/mois) […] 568 € [EQCE3] » ; repères EQCE3 : « TARIFS PENSION (€ HT) Pension hébergement 401 / Pension travail 568 / Pension avec une séance […] 457 ». Les tarifs « ont été établis à partir des tarifs observés sur le terrain en fonction de la qualité des prestations proposées ».
- Verdict : **CONFIRMÉ** (montants, HT, mensuel, campagne 2025). Rappel : un cas-type n'est pas une moyenne ; ses performances sont « favorables ».
- Recommandation : **garder** (`eq_std_prix_ht` : 334 / 368 / 401).

### Item 17 — Haras de Jardy : 922,50 € TTC (Hauts-de-Seine) et 1 002,71 € TTC (extérieurs) (R6-15)

- Sources rouvertes : [V2V-22] (plaquette JPG lue en image) et [V2V-23] (page « Les pensions », pour chercher l'unité). PAGE LUE.
- Citation exacte (plaquette) : ligne « Pension de votre cheval au boxe / Accès aux installations » : « Tarifs TTC Hauts-de-Seine 922.50 € » ; « Tarifs TTC Extérieurs 1002.71 € » ; inclus : paddocks, gestion des couvertures, « 1 séance / semaine de 1 heure réservée aux propriétaires », accès mensuel à un parcours ; « - 50% sur le prix TTC » des activités du club.
- Verdict : **NUANCÉ**. Montants et TTC confirmés. En revanche, **aucune unité de temps n'est écrite**, ni sur la plaquette ni sur la page « Les pensions ». La lecture « par mois » est quasi certaine (cohérente avec tous les autres tarifs), mais reste une HYPOTHÈSE, ce que R6 indiquait déjà. Le libellé « Hauts-de-Seine / Extérieurs » ne précise pas le critère (résidence du propriétaire, probablement). La plaquette n'est pas datée (fichier mis en ligne en mars 2026).
- Recommandation : **garder** (le modèle convertit 922,50 € TTC en 874 € HT à 5,5 %, taux de la pension accessoire à l'équitation selon R3-22, non revérifié ici). Mentionner « unité mensuelle supposée » dans la note de `eq_hdg_prix_ht`.

### Item 18 — Réseau Équin 2021 : charges de structure 1 449 € et 2 836 € par équidé ; 1 UMO pour 19,4 et 15 équidés ; revenu disponible médian 9 437 € et 18 265 € (R6-03)

- Source rouverte : [V2V-24]. PAGE LUE (pdftotext).
- Citations exactes : « Les charges de structure (hors amort. Et F.F.) par équidé présent observées sont importantes : de 2 836 €/équidé en pension travail et 1 449 €/équidé en pension hébergement. » ; « en pension travail, 1 UMO pour 15 équidés contre 1 UMO pour 19,4 équidés présents en pension hébergement » ; tableau « Résultats économiques globaux des 26 écuries de pension » : « Revenu Disponible / UMO exploitant (€) 12 924 [moyenne] 9 437 [médiane] [pension travail] 23 955 [moyenne] 18 265 [médiane] [pension hébergement] ».
- Verdict : **CONFIRMÉ** (six valeurs). Les charges de structure sont des **moyennes** et les revenus disponibles des **médianes**, comme R6 l'indique ; données 2021, 13 + 13 écuries sélectionnées pour leur viabilité.
- Recommandation : **garder**.

### Item 19 — Cartoucherie : redevance minimale de 80 000 €/an, 68 boxes (25 + 43) (R6-25)

- Source rouverte : [V2V-25]. PAGE LUE (pdftotext).
- Citations exactes : « La redevance fixe forfaitaire annuelle perçue par la Ville de Paris ne pourra être inférieure à (quatre-vingt mille euros) 80 000 euros (valeur au 1er janvier 2021). » ; une « redevance variable assise sur l'ensemble du chiffre d'affaires HT » s'y ajoute ; « 25 boxes » au rez-de-chaussée et « 43 boxes extérieurs répartis en trois modules » ; durée « maximale de 10 ans » ; travaux d'entretien à la charge de l'occupant.
- Verdict : **CONFIRMÉ**. C'est un **plancher** fixé par un appel à candidatures, pas un loyer constaté. Il couvre un ensemble plus large que les boxes : manège de 458 m², club-house de 223 m² avec cuisine, carrière, deux logements, en plein Paris.
- Recommandation : **garder** comme plafond (le modèle retient 600 €/box en central, 1 176 € en favorable).

### Item 20 — 1 382 châteaux et 3 769 domaines sur Mariages.net (R7-05, R7-06)

- Sources rouvertes : [V2V-26], [V2V-27] (WebFetch ; curl renvoie 403). PAGE LUE le 14/10/2026.
- Citations : « 1.382 résultats » (« Voir résultats (1.382) ») ; FAQ de la même page : « Sur Mariages.net, vous en trouverez plus de 1100 à votre disposition. » ; « 3.769 résultats » pour la catégorie « Domaine ».
- Verdict : **NUANCÉ**. Les compteurs sont exacts, mais ce sont des **catégories commerciales** : parmi les cinq premiers lieux de la catégorie « château » figure « Les Granges de Mauriac », qui n'en est pas un. Un même lieu peut aussi figurer dans les deux catégories. Ce n'est donc ni un recensement de châteaux ni un total additionnable. Le compteur évolue dans le temps.
- Recommandation : **garder** comme indicateur de concurrence, avec le libellé « 1 382 lieux dans la catégorie château et 3 769 dans la catégorie domaine de Mariages.net (octobre 2026) » (note de `evt_nb`).

### Item 21 — Châteauform' France 2025 : CA 186,4 M€, résultat net 3,4 M€ (R7-63)

- Source rouverte : [V2V-28] (API officielle recherche-entreprises, requête « chateauform »).
- Données : SIREN 402559595, « CHATEAUFORM' FRANCE », NAF 82.30Z, tranche d'effectif « 42 » (1 000 à 1 999 salariés) : finances 2025, « ca »: 186366960, « resultat_net »: 3406336.
- Verdict : **CONFIRMÉ**. Il s'agit de la société d'exploitation française, pas du groupe (la holding « GROUPE CHATEAUFORM » : CA 18,2 M€, résultat 5,6 M€ en 2025).
- Recommandation : **garder**.

### Item 22 — RevPAR haut de gamme 2025 HT : Indre-et-Loire 102,1 €, Gironde 146,4 €, Calvados 183,8 € (R7-38)

- Source rouverte : [V2V-29]. PAGE LUE (pdftotext).
- Citations (tableaux « Résultats CUMULES d'activité hôtelière », cumul à fin décembre 2025, ligne « Haut de Gamme ») : Indre-et-Loire « 72,6 % […] 140,6 […] 102,1 » ; Calvados « 65,1 % […] 282,6 […] 183,8 » ; Gironde « 65,1 % […] 224,9 […] 146,4 ». Mention : « Prix moyen et RevPAR en euros HT - Source: MKG_destination ».
- Verdict : **CONFIRMÉ** (valeurs, HT, cumul annuel 2025). La catégorie « Haut de Gamme » n'est pas définie dans le document, et l'échantillon est surtout urbain : ce ne sont pas des chiffres de châteaux-hôtels, comme R7 l'avait noté.
- Recommandation : **garder** (`hot_revpar` 102 / 130 / 184).

### Item 23 — Louise de La Vallière : environ 675 000 € par chambre (13,5 M€ pour 20 chambres), 33 salariés (R7-41)

- Source rouverte : [V2V-30]. PAGE LUE (article du 18 octobre 2022).
- Citations exactes : « La propriétaire suisse du site, Mira Grebenstein, qui l'a acheté il y a quatre ans pour 1,5 M€, l'a conçu et y a engagé des moyens à la hauteur : 13,5 M€ y ont été investis. » ; « les 20 chambres et suites ainsi que le spa » ; « L'effectif total projeté compte 33 personnes dont 5 majordomes, 9 personnes dédiées à l'hôtel, 11 en cuisine et 8 au service du restaurant et du bar. »
- Verdicts :
  - 675 000 €/chambre : **CONFIRMÉ** (13,5 M€ / 20, calcul). Précisions : hors prix d'achat (1,5 M€ : 750 000 €/chambre en l'incluant) ; restaurant gastronomique, bar, spa, piscine et parc de 19 ha compris ; HT/TTC non précisé ;
  - 33 salariés : **NUANCÉ**. C'est un effectif **projeté** à l'ouverture (« une partie du personnel est encore en cours de recrutement »), en **personnes** et non en ETP, dont **19 en cuisine, restaurant et bar**. Hors restauration : 14 personnes, soit 0,7 par chambre.
- Recommandation : **garder** 1,65 dans `hot_etp_chambre`, à condition de le requalifier : « effectif projeté (personnes), restaurant gastronomique compris ; cas unique », statut ESTIMATION et non SOURCÉ. C'est cohérent avec le modèle, qui compte aussi les recettes de restauration (`hot_autres_recettes`). Préciser « hors prix d'achat » dans la note de `hot_capex_chambre`.

### Item 24 — Grille de tournage du CMN : fiction de 2 500 à 5 500 € HT par jour selon la catégorie (R7-12)

- Source rouverte : [V2V-31]. PAGE LUE (pdftotext).
- Citation (« Forfait pour 12h d'occupation avec 1 agent inclus », colonnes HT « À PARTIR DE ») : « Long-métrage 9 000 € [A] […] 5 500 € [B] […] 3 500 € [C] » ; « Téléfilm, série-télévisée, docu-fiction, jeu-vidéo, web-série […] 6 000 € [A] […] 3 500 € [B] […] 2 500 € [C] ».
- Verdict : **CONFIRMÉ** pour les catégories **B et C**, celles que R7 retient pour un château privé. En catégorie A, la fiction va de 6 000 à 9 000 € HT. Ce sont des prix **planchers** (« à partir de ») pour 12 h avec un agent.
- Recommandation : **garder** (`tourn_tarif` 2 500 / 3 500 / 5 500 € HT).

### Item 25 — Domaine des Étangs : hôtel CA 3,47 M€ et résultat −3,20 M€ (2025) ; agriculture CA 1,82 M€ et résultat −4,36 M€ (2024) (R4-08)

- Source rouverte : [V2V-32] (API officielle, même requête que R4).
- Données : « DOMAINE DES ETANGS », SIREN 814032967, NAF 55.10Z, tranche 12 : 2025 « ca »: 3468619, « resultat_net »: -3203191 ; « DOMAINE DES ETOILES (DOMAINE DES ETANGS) », SIREN 572046852, NAF 01.42Z, tranche 11 : 2024 « ca »: 1823631, « resultat_net »: -4357639.
- Verdict : **CONFIRMÉ** (quatre valeurs). Les années diffèrent (2025 et 2024) : la somme de 7,6 M€ de pertes faite par R4 additionne deux exercices différents, ce que R4 signale.
- Recommandation : **garder**.

### Item 26 — 33 sociétés de châteaux-hôtels : 61 % en perte, marge médiane −6,3 % (R4-34, R4-35)

- Sources rouvertes : [V2V-33] (pages 1 et 2 de la requête de R4) et [V2V-34] (pages 3 à 5, contrôle). Calcul refait (script `scratchpad/v2v/scripts/sample33.py`).
- Reconstitution : en appliquant le critère de R4 (nom désignant clairement un château-hôtel, hors hôtel parisien, résidence de tourisme, hôtel d'HEC et groupes), j'obtiens **exactement 33 sociétés** parmi les 50 premiers résultats sur 105.
- Résultats : **20 en perte sur 33 (60,6 %)**, marge nette médiane **−6,3 %** (17e valeur : Château de Mercuès), CA médian 2,18 M€ ; hors Messardière, CA cumulé 103,4 M€ et résultat cumulé −14,6 M€. Le calcul de R4 est reproduit à l'identique.
- Limites de la méthode :
  - le classement par pertinence de l'API n'est pas un tirage aléatoire ; seules les sociétés qui publient leurs comptes sont visibles ;
  - les exercices vont de **2017 à 2025** : 7 sociétés sur 33 ont des comptes antérieurs à 2023, dont 4 sociétés fermées (état « C » dans le registre) et 2 sociétés en liquidation selon R7 (Brindos, La Barge ; BODACC non revérifié ici), ce qui alourdit la part de pertes ;
  - le résultat net intègre amortissements et frais financiers : ce n'est ni l'EBE ni la trésorerie ;
  - l'échantillon mélange des cas hétérogènes (une holding, un golf, un hôtel dans un château fort).
- Sensibilité : sur les seuls comptes 2023-2025 (26 sociétés) : **14 en perte (53,8 %), marge médiane −4,5 %** (R4 le donne aussi). En ajoutant trois châteaux nommés entre parenthèses (Varennes, les Ayes, Primard) : 21/36 (58 %), −5,4 %. Les pages 3 à 5 ne contiennent presque plus de châteaux-hôtels.
- Verdict : **NUANCÉ**. Les chiffres sont exacts, mais 61 % et −6,3 % représentent la borne pessimiste d'un échantillon hétérogène.
- Recommandation : **corriger la présentation** dans R4 (ligne 12 des « Chiffres clés ») et dans les livrables : valeur centrale « environ 54 % en perte, marge nette médiane −4,5 % (26 sociétés, comptes 2023-2025) » ; 61 % et −6,3 % en version large (2017-2025). Le modèle n'utilise pas ces chiffres en calcul : pas d'impact numérique.

### Item 27 — Loyers de maisons rurales 6,8 à 10,9 €/m²/mois charges comprises ; grange transformée 1 556 €/m² HT de travaux (R8-22, R8-23, R8-24)

- Sources rouvertes : [V2V-35] (page du jeu de données), [V2V-36] (fichier CSV **complet**, 34 900 communes, alors que R8 n'en avait lu que 40 lignes), [V2V-37] (fiche du CAUE 74). PAGE LUE.
- Citations exactes : « Les indicateurs de loyers sont fournis charges comprises pour des biens types loués vides et mis en location au 3ème trimestre 2025 » ; « Pour une maison : surface de 92 m² » ; CAUE : « SURFACE DE PLANCHER 165 m2 I COÛT DES TRAVAUX : 256 755 € HT I COÛT DE L'OPÉRATION (HORS FONCIER) 322 205 € TTC », livraison 04/2023.
- Contrôles : les valeurs citées par R8 sont exactes (Druye 8,96 ; Azay-le-Rideau 9,24 ; Clavé 6,82 ; Saint-Sornin (16) 7,54 ; La Rochefoucauld-en-Angoumois 8,03 ; Pont-Saint-Esprit 10,91). Sur toute la France : médiane 8,75 €/m²/mois (1er décile 6,97, 9e décile 12,03) ; pour les 30 673 communes estimées par « maille » (communes voisines regroupées faute d'annonces suffisantes, donc en général petites), médiane 8,63 €/m²/mois ; **75 % des communes** sont entre 6,8 et 10,9 €/m²/mois. 256 755 / 165 = 1 556 €/m² HT.
- Verdict : **CONFIRMÉ** (les deux chiffres). La fourchette de R8, tirée de 40 lignes, s'avère représentative ; la valeur centrale du modèle (8,0 €/m²) est un peu sous la médiane des communes estimées par maille (8,6). Le coût de 1 556 €/m² HT repose sur **un seul** chantier « à coût serré », en montagne, en 2022-2023.
- Recommandation : **garder**. Option : relever `log_loyer_m2` central de 8,0 à 8,5 €/m² si l'on veut coller à la médiane nationale des communes estimées par maille. Ce n'est pas une erreur, c'est un choix prudent.

### Item 28 — NACUBO 4,9 % ; UBS 3,5 % réel par an depuis 2000 ; Argos 8,8x (fonds 10,2x, stratégiques 7,9x) ; « plus d'une transmission sur cinq échoue dans les six ans » (R8-34, R8-32, R8-35, R8-36)

- Sources rouvertes : [V2V-38], [V2V-39] (WebFetch, curl renvoie 403), [V2V-40], [V2V-41]. PAGE LUE.
- Citations exactes :
  - NACUBO (exercice 2025) : « Institutions' average annual effective spending rate increased moderately to 4.9 percent from 4.8 percent in FY24. » ;
  - UBS : « Measured since the start of 2000 » … « global equity investors still enjoyed an annualized real return of 3.5% » (prime de risque de 4,3 % sur les bons du Trésor) ; « Of the 35 markets covered, 23 have 125-year histories from 1900 to 2024 » ;
  - Argos (T2 2026) : « L'Argos Index® a progressé de 2,3% pour s'établir à 8,8x l'EBITDA » ; « Les multiples médians des fonds d'investissement ont augmenté à 10,2x l'EBITDA et ceux des acquéreurs stratégiques à 7,9x » ; périmètre : opérations mid-market de 15 à 500 M€ de la zone euro, multiple médian EV/EBITDA sur 6 mois glissants ;
  - question écrite n° 75244 (2005) : « D'après une récente étude de la nouvelle banque publique d'aide aux PME (OSEO-BDPME), plus d'une transmission sur cinq échoue dans les six ans […]. Cette étude a pour base un échantillon de 3 000 dossiers représentatifs des 27 000 transmissions de PME référencées de 1997 à 2003 par OSEO. »
- Verdict : **CONFIRMÉ** (six valeurs). Rappels de périmètre, déjà notés par R8 : dotations américaines exonérées d'impôt ; rendement des actions mondiales avant frais et impôts ; transactions de 15 à 500 M€, bien au-dessus d'une petite PME ; taux d'échec cité de seconde main, sur des transmissions de 1997-2003.
- Recommandation : **garder**.

### Item 29 — PFU 31,4 % (12,8 % + 18,6 %) ; barème de l'IFI 2026 ; ouverture au public 50 jours (dont 25 non ouvrables, avril-septembre) ou 40 jours (juillet-septembre) (R3-16, R3-57, R3-01, R3-15, R3-04)

- Sources rouvertes : [V2V-42], [V2V-43], [V2V-44], [V2V-45], [V2V-46]. PAGE LUE.
- Citations exactes :
  - F36065 : « prélèvement forfaitaire unique à un taux global de 31,4 % , c'est-à-dire 12,8 % au titre de l'impôt sur le revenu et 18,6 % de prélèvements sociaux » (la page affiche « Vérifié le 26 avril 2024 », mais son contenu est à jour) ; F2329 (vérifiée le 30/06/2026) : CSG 10,6 % + CRDS 0,5 % + prélèvement de solidarité 7,5 % = « TOTAL 18,6 % » ; « flat tax au taux de 31,4 % (ou de 30 %) » ;
  - F138 (vérifiée le 06/03/2026) : « Jusqu'à 800 000 € 0 % | Entre 800 001 € et 1 300 000 € 0,50 % | Entre 1 300 001 € et 2 570 000 € 0,70 % | Entre 2 570 001 € et 5 000 000 € 1 % | Entre 5 000 001 € et 10 000 000 € 1,25 % | Supérieure à 10 000 000 € 1,50 % » ; décote « 17 500 € - 1,25 % » entre 1,3 et 1,4 M€ ; F563 : seuil « 1 300 000 € », abattement « de 30 % » sur la résidence principale, « Bâtiments classés monument historique » dans les biens à déclarer ;
  - BOFiP BOI-RFPI-SPEC-30-20-10-20181219, § 105 : « soit cinquante jours par an, dont vingt-cinq jours non ouvrables, au cours des mois d'avril à septembre inclus ; - soit quarante jours pendant les mois de juillet, août et septembre » ; « pendant au moins six heures » ; réduction possible de 10 jours au plus (visites scolaires).
- Verdict : **CONFIRMÉ** (trois chiffres ou barèmes).
- Recommandation : **garder**.

### Item 30 — Taxe de 20 % sur les actifs non professionnels des holdings patrimoniales : conditions (5 M€, 50 %, revenus passifs > 50 %), logement réservé à l'associé, chevaux de concours (R3-18)

- Source rouverte : [V2V-47]. PAGE LUE (pdftotext).
- Citations exactes : « le taux de la taxe est égal à 20 %, contre 2 % dans le projet de loi originel » ; « La valeur vénale des actifs qu'elles détiennent doit être supérieure ou égale à 5 M€ » ; « Au moins une personne physique doit détenir, de manière directe ou indirecte, une fraction des droits de vote ou des droits financiers égale ou supérieure à 50 % » ; « des revenus passifs correspondant à plus de 50 % du montant cumulé des produits d'exploitation et des produits financiers » ; assiette : « les chevaux de courses ou de concours ; les vins et les autres alcools ; et les logements dont une personne physique associée se réserve la jouissance » ; « due au titre des exercices clos à compter du 31 décembre 2026 ».
- Verdict : **CONFIRMÉ** (quatre éléments), **par rapport à la source citée**, qui est une synthèse de cabinet d'avocats. Le texte officiel (CGI, Légifrance) reste **INACCESSIBLE** depuis cet environnement (403), et je n'ai pas trouvé de doctrine BOFiP par le moteur interne. La synthèse elle-même mentionne « art.7 » dans le titre et « L'article 3 de la loi de finances pour 2026 » dans le texte : la numérotation de l'article est incohérente. Le texte lu ne dit pas « par an » : la taxe est due au titre de chaque exercice, ce qui revient à une taxe annuelle.
- Recommandation : **garder**, avec le statut « À VALIDER sur le CGI par un fiscaliste ».

### Item 31 — Banque de France (septembre 2026) : IPCH 2,3 / 1,9 / 1,6 % ; salaire moyen par tête 2,0 / 2,6 / 2,4 %. Kretz : environ 400 transactions par an, prix de vente moyen 2,415 M€ (D-01, D-02)

- Sources rouvertes : [V2V-48] (page HTML par WebFetch, puis PDF officiel converti par pdftotext ; curl renvoie 403) et [V2V-49]. PAGE LUE.
- Citations exactes :
  - Banque de France, PDF du 15 septembre 2026 : « En 2026, l'inflation totale (IPCH) s'établirait à 2,3 % en moyenne annuelle, après 0,9 % en 2025 » ; « En 2027, l'inflation totale se replierait à 1,9 % » ; « En 2028, l'inflation totale diminuerait à 1,6 % » ; « Notre projection de croissance du salaire moyen par tête nominal (SMPT) […] s'établit à 2,0 %, 2,6 % et 2,4 % respectivement en 2026, 2027 et 2028. » ;
  - MySweetImmo (17/09/2026) : « environ 1 500 châteaux sont actuellement proposés à la vente, pour quelque 400 transactions par an ces dernières années, selon les chiffres communiqués par Kretz Real Estate » ; « Le réseau indique un prix moyen de 5 millions d'euros pour les châteaux de son portefeuille et un prix de vente moyen de 2,415 millions d'euros. »
- Verdict : **CONFIRMÉ** (huit valeurs). Précisions : ce sont les projections du **scénario de base**, publiées avec d'autres scénarios énergétiques, et elles s'arrêtent en 2028 (au-delà, la dérive salariale du modèle est une hypothèse). Les 400 transactions sont une estimation d'un réseau d'agences, pas une statistique publique. Le prix de vente moyen de 2,415 M€ vient du portefeuille d'un seul réseau haut de gamme, dont le prix **affiché** moyen est de 5 M€.
- Recommandation : **garder** ; ajouter le prix affiché moyen de 5 M€ dans la note de `S1_prix_achat` à `S3_prix_achat`.

## Tableau récapitulatif

| n° | Chiffre vérifié (source) | Verdict | Citation ou donnée relevée (extrait) | Recommandation |
|---|---|---|---|---|
| 1 | 2 à 4 % de la valeur de remplacement par an, « minimum absolu » (R1-07, R1-08) | CONFIRMÉ | « 2 to 4 percent of the aggregate current replacement value […] should be used as an absolute minimum value » (NRC 1990, p. xii) | Garder ; R1-08 passe de EXTRAIT à PAGE LUE (p. xii) |
| 2 | 2 500 m², 600 000 €, 6 M€ ; prime ≥ 2 500 € si classé (R1-26) | CONFIRMÉ | « rarement inférieur à 2500 € » ; « Un château de 2500 m2 acheté 600.000 € […] 6 millions d'euros » | Garder ; note `S1_vr_m2` : type de surface non précisé |
| 3 | 5 000-10 000 €/m² ; 5 ‰ (R1-27) | CONFIRMÉ (fiabilité faible) | « 5 ‰ (0,5 %) de la valeur totale assurée » ; « entre 5 000 et 10 000 €/m² » | Garder comme borne haute |
| 4 | 156 067-160 686 £ TTC/an ; retard ≈ 1 994 000 £ (R1-05) | CONFIRMÉ | « VAT-inclusive expenditure […] £156,067 per year […] £160,686 » ; « just under £1,994,000 » | Garder |
| 5 | 40 000 €/an min. ; < 2 000 visiteurs ; 99,8 % (R1-01) | CONFIRMÉ (×2), NUANCÉ (visiteurs) | « 40 000 € / an minimum » ; « en dehors des zones touristiques très fréquentées […] moins de 2 000 visiteurs » | Garder ; ajouter la restriction de périmètre |
| 6 | DRAC 20 % / 40 % ; −29 % en CP (R1-34) | CONFIRMÉ (taux), NUANCÉ (−29 %) | « en moyenne de 20 % […] et de 40 % » ; « de 29 % en CP (-172 millions d'euros) » (PLF) ; Assemblée : 128,7 → 112 M€ (−13 %) | Garder les taux ; corriger la ligne 9 des chiffres clés de R1 |
| 7 | Olhain : résiliation, fermeture au 01/01/2026 (R1-28) | CONFIRMÉ | « Depuis le 1er janvier 2026, le site est dépourvu de couverture assurantielle » | Garder |
| 8 | 1 072 € TTC pour 4,5 MWh ; gaz 194,90 € TTC/MWh (R1-24, R1-25) | CONFIRMÉ | « la facture TTC passera de 1 046 € à 1 072 € » ; « 194,90 € TTC par mégawattheure » | Garder ; signaler la volatilité mensuelle du gaz |
| 9 | SMIC 12,31 €/h ; RGDU 0,3981 (R2-01, R2-02) | CONFIRMÉ | « Smic horaire 12,31 € » ; « soit 0,3981 » (maximum, < 50 salariés, SMIC de janvier) | Garder ; écrire « coefficient maximal » |
| 10 | 23 853 / 44 118 / 78 982 €/an (R2-11) | CONFIRMÉ | API : 1 987,76 ; 3 676,54 ; 6 581,79 €/mois (règles au 01/07/2026) | Garder |
| 11 | Villandry : 10 jardiniers pour 7 ha (R2-15) | CONFIRMÉ | « Ils sont dix à s'en occuper au quotidien » ; « 7 hectares de jardin » | Garder |
| 12 | Tracteur 100-140 CV : 101 464 € HT, 10,7 ans (R2-30) | CONFIRMÉ | « 101 464 € » (simulation 2026) ; « durée d'amortissement 10,7 ans » | Garder |
| 13 | Blenheim : 11 068 k£, 16 360 k£, 700 000, 2,5 M£ (obj. 4 M£), toiture 10,4 M£ (R5-03) | CONFIRMÉ | « Paying visitor numbers […] 700,000 » ; « spent £2.5m […] average of £4m » ; « allocated budget of £10.4m » | Garder (Gift Aid inclus ; « restauration » = conservation) |
| 14 | Chatsworth : 630 114 visiteurs ; 1 781 k£ ; 29 jardiniers (R5-05) | CONFIRMÉ | « 630,114 » (pass et « Friends » inclus) ; « Maintenance of the garden, park and woods 1,781 » ; « Gardens 29 » | Garder ; corriger « payants » dans R5 |
| 15 | Burghley : 3,52 M£ net ; 4,69 M£ (R5-07) | CONFIRMÉ | « net revenue of £3,520,257 » ; « Expenditure on charitable activities […] 4,689,993 » | Garder |
| 16 | Pensions 334 / 401 / 568 € HT/mois (R6-02) | CONFIRMÉ | Tableau 9 « Référentiel de produits 2025 » | Garder |
| 17 | Jardy 922,50 / 1 002,71 € TTC (R6-15) | NUANCÉ | « Tarifs TTC Hauts-de-Seine 922.50 € » ; « Extérieurs 1002.71 € » ; unité de temps non écrite | Garder ; préciser « mensuel supposé » |
| 18 | Réseau Équin 2021 : 1 449 / 2 836 € ; 19,4 / 15 ; 9 437 / 18 265 € (R6-03) | CONFIRMÉ | « 2 836 €/équidé en pension travail et 1 449 €/équidé en pension hébergement » ; « 1 UMO pour 15 […] 19,4 » ; tableau 9 437 / 18 265 (médianes) | Garder |
| 19 | Cartoucherie : 80 000 €/an min. ; 68 boxes (R6-25) | CONFIRMÉ | « ne pourra être inférieure à […] 80 000 euros » ; « 25 boxes » + « 43 boxes extérieurs » | Garder (plancher d'appel d'offres) |
| 20 | Mariages.net : 1 382 / 3 769 (R7-05, R7-06) | NUANCÉ | « 1.382 résultats » ; « 3.769 résultats » ; catégories commerciales | Garder ; libeller « lieux par catégorie » |
| 21 | Châteauform' France 2025 : CA 186,4 M€, RN 3,4 M€ (R7-63) | CONFIRMÉ | API : ca 186 366 960 ; resultat_net 3 406 336 | Garder |
| 22 | RevPAR HT 2025 : 102,1 / 146,4 / 183,8 € (R7-38) | CONFIRMÉ | Lignes « Haut de Gamme », cumul à fin décembre 2025, « en euros HT » | Garder |
| 23 | 675 000 €/chambre ; 33 salariés (R7-41) | CONFIRMÉ (capex), NUANCÉ (effectif) | « 13,5 M€ y ont été investis » ; « L'effectif total projeté compte 33 personnes dont […] 11 en cuisine et 8 au service du restaurant et du bar » | Garder ; requalifier `hot_etp_chambre` |
| 24 | CMN fiction 2 500-5 500 € HT/jour (R7-12) | CONFIRMÉ (catégories B et C) | « Long-métrage […] 5 500 € » (B) ; « Téléfilm, série […] 2 500 € » (C) ; A : 6 000-9 000 € | Garder |
| 25 | Domaine des Étangs : 3,47 / −3,20 M€ (2025) ; 1,82 / −4,36 M€ (2024) (R4-08) | CONFIRMÉ | API : 3 468 619 / −3 203 191 ; 1 823 631 / −4 357 639 | Garder |
| 26 | 33 châteaux-hôtels : 61 % en perte, marge médiane −6,3 % (R4-34, R4-35) | NUANCÉ | Calcul reproduit : 20/33, −6,3 % ; comptes 2023-2025 : 14/26 (54 %), −4,5 % | Corriger la présentation (54 % / −4,5 % en central) |
| 27 | Loyers 6,8-10,9 €/m²/mois CC ; grange 1 556 €/m² HT (R8-22 à R8-24) | CONFIRMÉ | Valeurs exactes ; 75 % des communes dans la fourchette ; « 256 755 € HT » pour 165 m² | Garder (option : central 8,5 €/m²) |
| 28 | NACUBO 4,9 % ; UBS 3,5 % ; Argos 8,8x (10,2x / 7,9x) ; échec > 1 sur 5 en 6 ans (R8-32 à R8-36) | CONFIRMÉ | « effective spending rate […] 4.9 percent » ; « annualized real return of 3.5% » ; « 8,8x l'EBITDA » ; « plus d'une transmission sur cinq échoue dans les six ans » | Garder |
| 29 | PFU 31,4 % ; barème IFI 2026 ; 50 j / 40 j (R3-01, R3-04, R3-15, R3-16, R3-57) | CONFIRMÉ | « 31,4 % , c'est-à-dire 12,8 % […] et 18,6 % » ; barème 0 / 0,5 / 0,7 / 1 / 1,25 / 1,5 % ; « cinquante jours […] quarante jours » | Garder |
| 30 | Taxe holdings 20 % ; 5 M€, 50 %, revenus passifs > 50 % ; logement ; chevaux (R3-18) | CONFIRMÉ (par rapport à la synthèse d'avocats) | « le taux de la taxe est égal à 20 % » ; « supérieure ou égale à 5 M€ » ; « les chevaux de courses ou de concours » ; « les logements dont une personne physique associée se réserve la jouissance » | Garder, « À VALIDER sur le CGI » (Légifrance inaccessible) |
| 31 | IPCH 2,3 / 1,9 / 1,6 % ; SMPT 2,0 / 2,6 / 2,4 % ; Kretz 400 ventes/an, 2,415 M€ (D-01, D-02) | CONFIRMÉ | « 2,3 % en moyenne annuelle » ; « 2,0 %, 2,6 % et 2,4 % respectivement en 2026, 2027 et 2028 » ; « prix de vente moyen de 2,415 millions d'euros » | Garder ; ajouter le prix affiché moyen (5 M€) |

## Décompte

Décompte par chiffre (90 valeurs distinctes dans la liste du directeur ; un barème ou une liste de conditions compte pour un) :

| Verdict | Nombre | Détail |
|---|---|---|
| CONFIRMÉ | 81 | — |
| NUANCÉ | 9 | 5 (moins de 2 000 visiteurs), 6 (−29 % en CP), 17 (922,50 € et 1 002,71 €), 20 (1 382 et 3 769), 23 (33 salariés), 26 (61 % et −6,3 %) |
| NON CONFIRMÉ | 0 | — |
| INACCESSIBLE | 0 | Toutes les sources de la liste ont été rouvertes. Seul le **texte officiel** de la taxe sur les holdings (CGI, Légifrance) reste inaccessible : la source listée (R3-18) a, elle, été lue. |

Par item : 25 items entièrement confirmés, 6 items avec au moins une nuance (5, 6, 17, 20, 23, 26).

**Aucun chiffre du modèle ne doit changer de valeur.** Les corrections portent sur des libellés, des périmètres, des statuts et la présentation de deux résultats (items 6 et 26).

## Corrections recommandées

### Au modèle (`02_MODELE/`, notes et statuts, sans changement de valeur)

1. `parametres.py`, `taux_entretien_courant` et `taux_gros_entretien` : ajouter à la note « NRC 1990, p. xii : “absolute minimum value” en l'absence d'information spécifique ; règle de jugement, valable en moyenne pour un parc de bâtiments et sur 5 à 10 ans ; un bâtiment isolé peut sortir de la fourchette » [V2V-02, V2V-03].
2. `parametres.py`, `S1_vr_m2` : remplacer « (exemple d'un courtier, Figaro 2020, surface développée) » par « (exemple d'un courtier, Figaro 2020, type de surface non précisé) » [V2V-04].
3. `parametres.py`, `prix_chaleur_kwh` : préciser que 19,49 c€ TTC/kWh est le prix repère **mensuel** du gaz de novembre 2026, en hausse de 6,3 % en octobre puis de 6,6 % en novembre [V2V-12].
4. `moteurs.py`, `hot_etp_chambre` : garder 1,65 ; changer l'unité en « personnes par chambre (effectif projeté à l'ouverture, restaurant gastronomique et bar compris : 19 des 33) » et le statut SOURCÉ en ESTIMATION (cas unique). Pour un hôtel sans restaurant, l'ordre de grandeur serait de 14 / 20 = 0,7 [V2V-30].
5. `moteurs.py`, `hot_capex_chambre` : préciser « hors prix d'achat du château (1,5 M€, soit 750 000 €/chambre en l'incluant) ; restaurant, spa, piscine et parc compris ; HT/TTC non précisé » [V2V-30].
6. `moteurs.py`, `eq_hdg_prix_ht` : ajouter « unité mensuelle supposée (non écrite sur la plaquette) » [V2V-22, V2V-23].
7. `moteurs.py`, `evt_nb` : remplacer « 1 382 châteaux et 3 769 domaines » par « 1 382 lieux dans la catégorie château et 3 769 dans la catégorie domaine de Mariages.net (catégories commerciales, recouvrement possible, octobre 2026) » [V2V-26, V2V-27].
8. `moteurs.py`, `tourn_tarif` : préciser « grille CMN, catégories B et C, prix “à partir de” pour 12 h avec un agent » [V2V-31].
9. `parametres.py`, `S1_prix_achat` à `S3_prix_achat` : ajouter « prix affiché moyen du portefeuille Kretz : 5 M€ ; 400 ventes par an = estimation d'un réseau d'agences » [V2V-49].
10. Option, sans erreur constatée : `moteurs.py`, `log_loyer_m2` central de 8,0 à 8,5 €/m²/mois, pour se rapprocher de la médiane nationale des communes estimées par maille (8,63) [V2V-36].

### Aux fichiers de recherche (à faire par le directeur ; V2V ne modifie pas les fichiers des autres agents)

11. R1, §6.3 et ligne 9 des « Chiffres clés » : remplacer « 112 M€ en CP, soit −29 % (−172 M€) » par « Sénat : −29 % en CP (−172 M€), périmètre large des crédits d'intervention des DRAC ; Assemblée nationale : 128,7 → 112 M€ en CP (−13 %), crédits déconcentrés d'intervention (monuments, orgues, objets) ; montants du PLF, non votés » [V2V-08, V2V-09].
12. R1, §1.1 et contre-exemple 4 : compléter la citation « moins de 2 000 visiteurs » par « en dehors des zones touristiques très fréquentées, et des monuments emblématiques » [V2V-07].
13. R1, source R1-08 : statut EXTRAIT → PAGE LUE ; URL de la citation « absolute minimum » : https://www.nationalacademies.org/read/9807/chapter/1 (p. xii) [V2V-02].
14. R1, §1.2 (Harlow) : le taux de TVA effectif est de 17,9 à 18,5 % de la dépense hors TVA ; pour convertir en HT, diviser par ≈ 1,18 et non 1,20 [V2V-06].
15. R2, §1.2 et chiffres clés : écrire « coefficient **maximal** 0,3981 (moins de 50 salariés, salaire égal au SMIC de janvier 2026) ; ≈ 0,375 au SMIC de juin, car la formule garde le SMIC de janvier » [V2V-14, V2V-15].
16. R4, §1.B et ligne 12 des « Chiffres clés » : présenter en central « 54 % en perte, marge nette médiane −4,5 % (26 sociétés, comptes 2023-2025) » et en version large « 61 %, −6,3 % (33 sociétés, comptes 2017-2025, dont 4 sociétés fermées et 2 en liquidation selon R7) » ; ajouter les biais : classement par pertinence, sociétés publiant leurs comptes, résultat net et non EBE [V2V-33, V2V-34].
17. R5, §1.3 (leçon) : « 600 000 visiteurs payants » → « environ 630 000 visiteurs, détenteurs de pass et membres compris » [V2V-19].
18. R7, chiffres clés n° 18 : « 33 salariés […] ETP » → « effectif projeté de 33 personnes, dont 19 en restauration » [V2V-30].
19. R3, taxe sur les holdings : signaler la numérotation incohérente de la source (« art.7 » / « article 3 ») et garder « À VALIDER sur le CGI » [V2V-47].

## Contre-exemples et cas d'échec trouvés

- Aucun nouveau cas : la vérification confirme les cas d'échec déjà décrits, à savoir la perte d'assurance d'Olhain [V2V-10], les pertes du Domaine des Étangs [V2V-32] et les comptes déficitaires de Brindos (−0,87 M€ en 2018) et de La Barge (−0,06 M€ en 2017), présents dans l'échantillon de châteaux-hôtels [V2V-33] ; leur liquidation est rapportée par R7 (BODACC), non revérifiée ici.
- Constat de méthode : l'échantillon de châteaux-hôtels contient 4 sociétés fermées et des comptes de 2017-2019 ; la part de pertes est plus faible sur les comptes récents (54 % au lieu de 61 %), mais elle reste majoritaire.

## Points de doute et limites de cette vérification

- Lectures en image (pas de reconnaissance de caractères disponible) : NRC 1990 (images GIF des pages), comptes de Blenheim, Chatsworth et Burghley (scans), plaquette de Jardy. Les pages étaient nettes ; un risque d'erreur de lecture reste possible mais faible.
- Lectures par WebFetch, qui passe par un modèle de synthèse : Mariages.net et UBS (curl refusé avec 403). Pour la Banque de France, le PDF officiel a été converti par pdftotext : citations exactes.
- L'API recherche-entreprises ne donne que le chiffre d'affaires et le résultat net, sans le détail des comptes (EBE, amortissements, dettes).
- Le texte officiel de la taxe sur les holdings (CGI) n'a pas pu être lu (Légifrance 403 ; recherche BOFiP non trouvée).
- Le taux de TVA de 5,5 % utilisé pour convertir le tarif de Jardy (R3-22) n'était pas dans ma liste : non revérifié.

## Chiffres clés pour le modèle (après vérification)

| Chiffre | Valeur | Unité | Année | Statut | Source |
|---|---|---|---|---|---|
| Entretien-réparation (règle NRC, minimum en l'absence d'information) | 2 à 4 | % de la valeur de remplacement par an | 1990 | PAGE LUE | [V2V-02], [V2V-03] |
| Dépense d'entretien des maisons historiques britanniques | 156 067 à 160 686 | £ TTC/an | 2024 | PAGE LUE | [V2V-06] |
| Plancher Demeure Historique | 40 000 | €/an | 2019 | PAGE LUE | [V2V-07] |
| Taux moyens de subvention DRAC (inscrit / classé) | 20 / 40 | % des projets subventionnés | 2025 | PAGE LUE | [V2V-08] |
| Coût employeur à 1 / 1,5 / 2,5 SMIC | 23 853 / 44 118 / 78 982 | €/an | règles au 01/07/2026 | PAGE LUE (calcul API refait) | [V2V-15] |
| Pension box HT (cas-types) | 334 / 401 / 568 | € HT/mois | 2025 | PAGE LUE | [V2V-21] |
| Pension Jardy | 922,50 / 1 002,71 | € TTC (mensuel supposé) | 2026 | PAGE LUE (unité HYPOTHÈSE) | [V2V-22] |
| RevPAR haut de gamme (37 / 33 / 14) | 102,1 / 146,4 / 183,8 | € HT | 2025 | PAGE LUE | [V2V-29] |
| Effectif d'un château-hôtel de 20 chambres | 33 (dont 19 en restauration) | personnes (projeté) | 2022 | PAGE LUE | [V2V-30] |
| Châteaux-hôtels en perte (comptes 2023-2025 / 2017-2025) | 54 / 61 | % | 2017-2025 | ESTIMATION (calcul reproduit) | [V2V-33] |
| Marge nette médiane (2023-2025 / 2017-2025) | −4,5 / −6,3 | % du CA | 2017-2025 | ESTIMATION (calcul reproduit) | [V2V-33] |
| Loyer de maison, médiane des communes estimées par « maille » (en général petites) | 8,63 (75 % des communes entre 6,8 et 10,9) | €/m²/mois CC | T3 2025 | PAGE LUE (fichier complet) | [V2V-36] |
| PFU | 31,4 (12,8 + 18,6) | % | 2026 | PAGE LUE | [V2V-42], [V2V-43] |
| IPCH 2026 / 2027 / 2028 | 2,3 / 1,9 / 1,6 | % | projection sept. 2026 | PAGE LUE | [V2V-48] |
| Salaire moyen par tête 2026 / 2027 / 2028 | 2,0 / 2,6 / 2,4 | % | projection sept. 2026 | PAGE LUE | [V2V-48] |

## Usage des outils web

- WebSearch : 0 (aucune URL morte à retrouver).
- WebFetch : 9 (NRC ×2, Figaro, Villandry, Mariages.net ×2, UBS, Banque de France HTML et PDF).
- curl : environ 100 requêtes, nouvelles tentatives comprises (PDF officiels, pages HTML, 25 images de pages du rapport NRC de 1990, API recherche-entreprises, 4 requêtes à l'API URSSAF, fichier CSV de la carte des loyers).
