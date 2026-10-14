# V2V — Vérification indépendante des chiffres les plus influents

Agent : V2V (vérification). Date : 2026-10-14. Statut du fichier : EN COURS (écrit au fur et à mesure).

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

- Sources rouvertes : [V2V-01] (NRC 2001, p. 46), [V2V-02] (NRC 1990, p. xii), [V2V-03] (NRC 1990, p. 6-7 et 17-19). PAGE LUE. Le texte de 1990 n'existe qu'en images de pages, lues visuellement.
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
- Verdict : **CONFIRMÉ**. Deux précisions : la moyenne de moins de 2 000 visiteurs exclut les zones très touristiques et les monuments emblématiques ; le « tableau en annexes » qui fonde les 99,8 % **ne figure pas** dans le PDF de 3 pages, donc la méthode n'est pas vérifiable. HT/TTC non précisé ; année 2019, à actualiser si le chiffre est utilisé en € 2026.
- Recommandation : **garder** (comme plancher, € 2019).

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
- Recommandation : **garder** ; signaler dans la note de `prix_chaleur_kwh` que 19,49 c€ est une valeur mensuelle haute (novembre 2026).

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

