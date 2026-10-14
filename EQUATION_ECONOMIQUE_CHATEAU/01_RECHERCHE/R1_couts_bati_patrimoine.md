# R1 — Coûts du bâti patrimonial

Agent : R1. Démarré le 2026-10-14. Fichier écrit au fur et à mesure.
Statuts : PAGE LUE (page ouverte avec WebFetch, citation exacte), EXTRAIT (vu dans un résultat de recherche), ESTIMATION, HYPOTHÈSE, INCONNU.
Sources : `01_RECHERCHE/sources/sources_R1.csv` (identifiants R1-xx).

> Avertissement de méthode : pour les **PDF**, le fichier téléchargé par WebFetch a été converti localement avec `pdftotext` ; les citations sont donc **exactes**. Pour les **pages HTML**, l'outil WebFetch passe par un modèle de synthèse : les citations entre guillemets sont celles qu'il a renvoyées comme exactes (limitées à 125 caractères, parfois paraphrasées, ce qui est signalé). Elles doivent être revérifiées sur la page originale avant toute publication externe.

## Journal d'avancement

- 2026-10-14 : squelette créé. Lecture des PDF de la Demeure Historique.
- 2026-10-14 : sections 1 à 9 et sections finales rédigées. **Terminé.** Budget web consommé : 15 WebSearch sur 15 ; 71 appels WebFetch (dont 20 en échec : erreurs 403, 404, 503, 504 ou redirections). 43 sources enregistrées dans `sources_R1.csv` (36 pages lues, 7 extraits).

## Résumé

1. Le plancher de la Demeure Historique (40 000 €/an hors restauration, 2019) est confirmé, mais il ne couvre pas le gros entretien.
2. Au Royaume-Uni, les grandes maisons protégées dépensent en moyenne ≈ 156 000-161 000 £ TTC/an pour le bâtiment principal et accumulent pourtant ≈ 2 M£ de retard chacune : la dépense « normale » observée est insuffisante.
3. Aucun prix au m² fiable n'existe en accès public pour les travaux sur MH ; seuls des montants globaux de chantiers ont été trouvés (≈ 40 000 à 400 000 € par tranche de toiture de château privé).
4. Le tableau S1/S2/S3 (§ 9) est une ESTIMATION fondée sur la règle de 2 à 4 % de la valeur de reconstruction ; budget central du bâti ≈ 0,2 M€ (S1), 0,52 M€ (S2), 2,0 M€ (S3) TTC/an, avec une fourchette d'un facteur 4.
5. Le paramètre décisif est la valeur de reconstruction au m² (2 400 contre 5 000-10 000 €/m² selon les sources) : il faut des devis d'assureurs et l'avis d'un ACMH ou d'un économiste.
6. Subventions de l'État : 20 % (inscrit) et 40 % (classé) en moyenne, non garanties, en forte baisse en 2026 (−29 % des crédits DRAC), versées avec retard.
7. Assurance : marché étroit, primes en hausse, cas réel de résiliation et de fermeture (Olhain, 2026).
8. Énergie et taxe foncière pèsent peu dans le total, mais restent mal documentées pour des châteaux.

## 1. Ratios globaux d'entretien des demeures historiques

### 1.1 La Demeure Historique (France)

Méthode de lecture : WebFetch n'a pas pu lire le texte des PDF (flux compressés). Les fichiers téléchargés par WebFetch ont été convertis localement avec `pdftotext`. Les citations ci-dessous sont copiées du texte extrait, donc exactes.

**Plancher de 40 000 €/an — confirmé** [R1-01] (note du 27 mai 2019, p. 2) — PAGE LUE :
> « En moyenne le coût d'entretien d'un monument (hors ouverture au public et travaux de restauration) est de 40 000 € / an minimum (assurance, impôts locaux, emploi d'un gardien, travaux minimum d'entretien…). »

Lecture critique :
- Le périmètre **exclut** l'ouverture au public **et les travaux de restauration**. C'est donc un plancher de fonctionnement courant, pas un coût complet du bâti.
- Il s'agit d'une moyenne pour l'ensemble des adhérents (« plus de 3000 monuments : manoirs ou châteaux, abbayes ou prieurés, ateliers ou forges, hôtels particuliers, jardins… »), tailles « très variables ». Ce n'est pas une donnée par m² ni spécifique à un grand château.
- Année : 2019. HT/TTC non précisé ; pour un particulier, il s'agit de dépenses supportées TTC (HYPOTHÈSE de lecture).
- Méthode de calcul non publiée dans la note : la source du chiffre (enquête, déclaratif) n'est pas donnée. Fiabilité moyenne.

Autres éléments de contexte de la même note [R1-01], PAGE LUE :
> « la moyenne de la fréquentation est établie à moins de 2 000 visiteurs par an, par monument. »
> « Pour 99,8 % des propriétaires, la seule activité d'ouverture à la visite n'est donc pas rentable et généralement déficitaire »
> « Au-dessous de 10 000 visiteurs payants annuels, le résultat coûts/recettes est toujours négatif. Au-delà, le bilan peut être positif sous réserve de ne prendre en compte que les charges courantes et directes de la visite, c'est-à-dire à l'exclusion des travaux de conservation, ou de mise en accessibilité ou sécurité. »
> « Généralement, les propriétaires-gestionnaires de ces monuments n'ont pas de personnel autre qu'eux-mêmes, aidés d'un ou plusieurs membres de la famille, parfois d'un gardien et éventuellement d'emplois saisonniers »

Le second document demandé, « La transmission des monuments historiques » [R1-02], est en réalité un **communiqué de presse d'une page** (21 octobre 2019) annonçant un travail de recherche avec l'université Paris-Sud. Il ne contient **aucun chiffre de coût**. PAGE LUE, sans donnée exploitable.

### 1.2 Historic Houses (Royaume-Uni)

Remarque : « Historic Houses Association » (HHA) est l'ancien nom de « Historic Houses ». Le moteur de recherche les a présentés à tort comme deux organisations distinctes ; ce point n'a pas été repris.

**a) Rapport Harlow Consulting pour Historic Houses, janvier 2025** [R1-05] — PAGE LUE (PDF téléchargé par WebFetch, texte extrait localement). Enquête 2024 auprès de 121 propriétés (84 % de maisons historiques ; 82 % au plus haut niveau de protection : Grade I et II* ou équivalents). Montants **TVA comprise** (TVA britannique 20 %), en livres sterling 2023-2024.

- Dépense annuelle moyenne d'entretien et de réparation du bâtiment principal :
  > « The average reported VAT-inclusive expenditure on repair and maintenance of the respondents' main heritage asset was £156,067 per year. When the cases where there is a disparity […] are inflated […], the average annual expenditure increases to £160,686. »
- Par catégorie :
  > « For the 80 VAT-registered properties the resulting average total reported VAT-inclusive expenditure was from £181,804 to £185,264. The corresponding figure for the 41 non-VAT-registered properties was from £105,848 to £112,731. The calculated average expenditure at the 67 open properties was estimated to be between £139,823 and £143,801, and the average expenditure at the 54 closed properties was estimated to be between £176,221 and £181,636. »
- Dépense prévue sur 5 ans :
  > « The total amount reported was just over £63 million, an average of just over £523,000 per property. This equates to nearly £105,000 per year. »
- Retard d'entretien par propriété :
  > « Among these respondents, the average estaimted [sic] total repair need amounted to just under £1,994,000. […] the average urgent repair need stood at just under £893,000. » (urgent = « within the next five years » ; n = 88 et 95)
  > « Those properties that are VAT-registered reported rather greater repair needs, at more than £2.5 million per property of outstanding repairs and just under £1.1 million of urgent needs. Properties currently open to the public reported similar figures: just over £2.7 million in total repair needs and £1.05 million of urgent repair needs. »
- Total du secteur :
  > « the reported backlog of repair and maintenance in member houses is now estimated to amount to some £2 billion. This is in spite of an annual repair and maintenance spend in the region of £160 million »
- Diagnostic et méthode :
  > « Just over a third (36%) of properties have a formal condition survey. » ; « the five-yearly ('quinquennial') cycle of updating condition surveys that is largely accepted as standard in historic building conservation »
  > « just under 60% were relying entirely on their own judgement » (pour estimer les coûts) → les auteurs estiment que cela conduit plus probablement à une **sous-estimation**.
- Limite majeure pour notre modèle : aucune surface (m²) n'est donnée. On ne peut pas en tirer un ratio €/m² sans HYPOTHÈSE de taille.

**b) Études de cas du même rapport** [R1-05], PAGE LUE :
- Kingston Russell House (Dorset, Grade I, « small », maison familiale non ouverte) :
  > « The yearly running cost of repairs (at 2024 prices) has normally been between £12,000 and £20,000, but a larger repair project has been needed around every 10 years or so and has cost between £50,000 and £100,000. »
  > « The cost of insurance on the house has more than doubled this year, and is now greater than all the other annual running cost of the house put together, partly because rebuilding costs have rocketed in recent years. […] Many insurers will not offer cover at all »
  > « Maintaining the 6 acres of formal gardens […] demands at least 4 days a week of help from a professional gardener »
- Boughton Monchelsea Place (Kent, Grade I, 12 chambres, activité événementielle) :
  > « The recurring cost for basic repair and maintenance of the house varies but is in the tens of thousands per year. The upkeep of the gardens is on top of this, with the annual cost in gardening staff and equipment maintenance reaching around £75,000 »
  > restauration d'une grange classée : devis « £42,000 », facture finale « nearly £54,000, with VAT adding a further £11,000 » (dépassement ≈ +29 %, ESTIMATION à partir des deux chiffres).
  > « Currently the owners are engaged in a comprehensive overhaul of the windows […] The cost for this is again likely to be around £50,000, plus VAT. »

**c) Presse et infographie** :
- [R1-04] Museums Journal, 18 novembre 2025, PAGE LUE : « the repair bill facing the sector has doubled to £2bn since the start of the Covid pandemic » ; « the average property spends about £160,000 on repairs and maintenance each year » ; « Historic Houses, which represents around 1,450 independently owned historic houses, castles and gardens across the UK ».
- [R1-06] Infographie Historic Houses 2025, PAGE LUE : « Our members reported a total backlog of Over £2 billion of repairs & maintenance work, despite a reported annual spend of around £160,000 each in 2024 » ; « 47% of Historic Houses places delayed or cancelled urgent repairs and maintenance works due to lack of funds between 2020 and 2022 ».

Incohérence relevée (conservée, non lissée) : 160 M£ de dépense annuelle totale pour ≈ 1 450 maisons donnent ≈ 110 000 £ par maison (ESTIMATION arithmétique), alors que la moyenne de l'échantillon est ≈ 156 000-161 000 £. Explication probable (non vérifiée) : l'échantillon de 121 répondants surreprésente les grandes maisons, ou les 160 M£ ont été extrapolés différemment.

**Ordre de grandeur pour le modèle (ESTIMATION)** : un grand domaine protégé au Royaume-Uni dépense en moyenne ≈ 156 000 à 161 000 £ TTC par an (jusqu'à ≈ 185 000 £ pour les propriétés assujetties à la TVA ; dépense prévue ≈ 105 000 £) pour l'entretien-réparation du seul bâtiment principal, alors qu'il accumule en même temps un retard moyen de ≈ 2 M£. Ce niveau de dépense est donc **insuffisant** : il ne constitue pas un budget d'entretien « d'exception ».

### 1.3 Règle de pouce : entretien annuel en % de la valeur de remplacement

- [R1-07] National Research Council (2001), *Deferred Maintenance Reporting for Federal Facilities*, chapitre « Inadequate Funding for Maintenance and Repair » — PAGE LUE. Le texte cite le rapport NRC de 1990 *Committing to the Cost of Ownership*. Citation partielle restituée par l'outil (limitée à 125 caractères) : « An appropriate budget allocation for routine M&R [maintenance and repair] » ; suite de la phrase restituée en paraphrase par l'outil : pour un parc important de bâtiments, l'allocation se situe généralement **entre 2 et 4 % de la valeur de remplacement à neuf cumulée** (« current replacement value »). La même page indique que les agences fédérales déclaraient financer l'entretien à moins de 2 % de cette valeur.
- [R1-08] EXTRAIT (résultat de recherche, non vérifié sur le texte de 1990) : le chiffre « excludes land and major associated infrastructure » ; « In the absence of specific information, this funding level should be the absolute minimum. Where neglect has built up a backlog, spending must exceed this minimum until the backlog is eliminated. »
- Limites : ratio conçu pour des **parcs de bâtiments publics américains**, pas pour des monuments historiques. Pour un petit nombre de bâtiments, il s'entend comme une **moyenne pluriannuelle**, pas comme une dépense de chaque année (EXTRAIT [R1-08], résumé d'un symposium NRC de 1997). Aucun ratio équivalent officiel n'a été trouvé pour les monuments historiques français : INCONNU. Pour vérifier : rapports de l'OPPIC ou du CMN sur l'entretien de leurs parcs, ou un ACMH.
- Usage dans le modèle : il faut une **valeur de reconstruction à l'identique** (€/m²) pour appliquer ce ratio. Cette valeur n'a pas été trouvée dans une source fiable à ce stade (voir § 4 Assurance).

### 1.4 Autres données françaises (Demeure Historique)

- [R1-10] Dossier « législatives 2017 », PAGE LUE :
  > « Actuellement, plus de 1 000 monuments historiques sont en vente sur le territoire, et la durée moyenne de détention se réduit à 7 ans après l'acquisition d'un monument historique, du fait des difficultés croissantes que rencontrent les porteurs de projets. »
  (Affirmation d'une association de plaidoyer ; méthode non publiée. À traiter comme un signal, pas comme une statistique.)
  > « La dépense fiscale afférente au patrimoine monumental est stable et représente environ 58 millions d'euros (source : la Demeure Historique) ou 59 millions d'euros (source : PLF 2012), ce qui représente moins de 3 000 euros par an en moyenne par monument historique privé »
  > Enquête « Tournelle » : « basée sur les montants des recettes et des charges de 513 monuments historiques en 2010 ». Les comptes détaillés par monument ne sont pas publiés dans ce document : INCONNU (à demander à la Demeure Historique si la mission l'autorisait, ce qui n'est pas le cas).
  > Cas d'un propriétaire transformant des communs en salle de réception (ERP) : « Plus de 100 000 euros ont été investis dans les travaux de mise en conformité. » ; « L'affaire a duré plus de deux ans. »
- [R1-09] 98e congrès (document de février 2023), PAGE LUE — propos du directeur général des patrimoines : « l'essentiel de la déperdition passe par le toit. Si les combles sont isolés, on peut gagner 60% de la consommation énergétique. » (affirmation orale, non chiffrée par une étude citée ; fiabilité moyenne).

**Dépenses des propriétaires privés français** : Aucune statistique récente et consolidée des dépenses annuelles de travaux des propriétaires privés français n'a été trouvée : INCONNU. Pour vérifier : étude biennale de la Demeure Historique sur les cofinancements publics (édition la plus récente), rapport de la Cour des comptes 2022 sur la politique des monuments historiques, rapport IGAC-IGF 2020 sur l'ouverture au public (cités dans [R1-09]).

### 1.5 National Trust, English Heritage, Heritage Counts

- **Heritage Counts (Historic England)** : la page https://historicengland.org.uk/research/heritage-counts/ a renvoyé une erreur 403 ; aucune donnée lue. **INCONNU.** Pour vérifier : rapports « Heritage Counts » (volet « Heritage and the Economy », dépenses de réparation et d'entretien du bâti ancien dans la production du BTP).
- **National Trust** : seule donnée lue, de seconde main, sur ses **ressources** et non sur ses coûts d'entretien [R1-34], PAGE LUE : « Cette organisation philanthropique britannique détient environ 500 sites patrimoniaux bâtis ou naturels et en assure la gestion, avec, pour 2025, des ressources de 874 millions d'euros issues des cotisations de ses 5,7 millions de membres, de la billetterie de chaque site et de levées de fonds. » Dépense annuelle de conservation par site : **INCONNU** (à lire dans le rapport annuel du National Trust).
- **English Heritage** : aucune donnée trouvée dans le budget de recherche imparti. **INCONNU.**
- Contexte français [R1-34] : la ministre de la Culture s'est déclarée favorable fin 2024 à un « National trust » à la française ; une mission de préfiguration a remis un rapport à l'été 2025.


## 2. Coûts de restauration par composant (France)

### 2.1 Constat principal : pas de prix au m² fiable et public pour un MH

Trois recherches ciblées (délibérations, pages projets de la Fondation du patrimoine, prix unitaires de marchés) n'ont fourni **aucun prix au m² vérifiable** pour une couverture de monument historique sous maîtrise d'œuvre d'un ACMH. Les montants publiés sont des **montants globaux d'opération**, sans surface. Le guide technique officiel du ministère [R1-18] (août 2011) contient bien un « bordereau de prix unitaire » et un « mode de métré », mais **sans aucun prix** : c'est une trame de marché. **Prix au m² d'une couverture MH : INCONNU.**

Comment le vérifier : (1) avis d'attribution des marchés de restauration de MH publics (BOAMP, profils d'acheteurs des communes, du CMN ou de l'OPPIC), lot « couverture », rapportés à la surface du DCE ; (2) devis d'entreprises qualifiées MH (Qualibat 2194 ou équivalent) ; (3) consultation d'un ACMH ou d'un économiste de la construction spécialisé.

### 2.2 Montants réels de chantiers datés (montants globaux, HT/TTC non précisés sauf mention)

| Site | Statut | Propriétaire | Travaux | Montant | Année | Source |
|---|---|---|---|---|---|---|
| Donjon du château fort de Sedan (Ardennes) | MH, propriété publique | Ville de Sedan | clos et couvert (charpente, couverture en ardoises violine, maçonneries) | « 966 147 euros », dont DRAC « 386 458 euros » (= 40,0 %, calcul) | 2023-2025 | [R1-17] PAGE LUE |
| Château de Bas, Champigneulles (54) | non précisé ; vendu à la commune en 1951 | commune (probable) | toiture en ardoise et zingueries « à l'identique », cheminées, lucarnes, charpente | « Montant global : 392 724 € », dont Loto du patrimoine « 280 000 € » | 2023 | [R1-12] PAGE LUE |
| Château de Vauville (50) | « Inscrit […] depuis 1972 » | privé (famille) | toiture en lauzes de schiste (« 80 % […] gravement endommagée ») | « 165 340 € », dont Loto du patrimoine « 165 000 € » | sélection sept. 2025 | [R1-13] PAGE LUE |
| Château de Meung-sur-Loire (45) | non précisé (« demeure privée ouverte à la visite ») | privé | charpente, couverture, maçonneries, menuiseries | « Montant global : 310 995 € », dont Loto « 148 000 € » ; « environ 18 mois » de travaux | 2020-2021 | [R1-16] PAGE LUE |
| Château de Montautre, Fromental (87) | non précisé | privé | remplacement de plaques de fibrociment par ardoises « pose cloutée, brouillée » | « Montant global : 130 805 € » ; 14 mois | 2023-2027 | [R1-14] PAGE LUE |
| Château de Jarnioux (69) | non précisé | famille (« depuis plus de 250 ans ») | couverture en tuiles canal sur charpente chêne, par phases | phase 1 « 127 501,80 € » dont couverture « 113 393,20 € » ; phase 2 couverture « 42 847 € » ; phase 3 couverture « 55 964 € » | 2021-2023 | [R1-11] PAGE LUE |
| Château de Grainville (27) | non précisé | privé | toitures d'ardoise du corps central et d'un pavillon, lucarnes zinc | « Montant global : 42 331 € » | 2026 | [R1-15] PAGE LUE |

Lecture (ESTIMATION) : pour des châteaux privés modestes, une tranche de toiture se chiffre entre ≈ 40 000 € et ≈ 400 000 €, souvent réalisée par **phases successives** sur plusieurs années, faute de trésorerie. Ce sont des montants de **restauration ponctuelle**, pas des coûts annuels.

Cas britanniques comparables (Grade I) [R1-05], PAGE LUE : grange restaurée « nearly £54,000, with VAT adding a further £11,000 », pour un devis initial de « £42,000 » (dépassement ≈ +29 %) ; réfection complète des fenêtres « around £50,000, plus VAT ».

### 2.3 Prix grand public (bâtiment non protégé)

Seuls des comparateurs commerciaux donnent des prix au m² (EXTRAITS, fiabilité faible, non vérifiés par lecture) : ardoise posée « environ 130 €/m² » [R1-39] ; rénovation de toiture « entre 79 € et 360 € du m² » [R1-40] ; dépose de la couverture et déchets « entre 20 et 30 €/m² » [R1-41]. Ces chiffres ne valent **pas** pour un MH (ardoise naturelle choisie, pose au clou, échafaudages, ACMH). Ils ne sont pas retenus dans le tableau final.

### 2.4 Entretien courant des couvertures (principe)

[R1-18] guide du ministère, § 6.6, PAGE LUE :
> « L'entretien le plus élémentaire consiste alors à remplacer les ardoises en mauvais état, déplacées ou manquantes. »
> « les dégradations dues à une absence régulière d'entretien sont imputables au propriétaire. Cet entretien régulier est donc vivement conseillé »
> « Une note de visite technique peut être rédigée à l'attention du maître d'ouvrage sur l'état de la toiture et les anomalies constatées. »
Fréquence et coût de cette visite : non indiqués (INCONNU).

### 2.5 Durées de vie des composants

| Composant | Durée de vie | Source | Statut |
|---|---|---|---|
| Ardoise (couverture) | « Ardoise \| 100 ans » | [R1-20] industriel, 2025 | PAGE LUE, fiabilité faible |
| Zinc (couverture) | « 100 ans en moyenne » ; « la garantie de durée de vie du zinc est d'une quarantaine d'années minimum » | [R1-20] | PAGE LUE, fiabilité faible |
| Tuiles terre cuite | « Entre 30 et 100 ans » | [R1-20] | PAGE LUE, fiabilité faible |
| Chaudière gaz classique / à condensation | 10 à 20 ans / 15 à 25 ans | TotalEnergies [R1-42] | EXTRAIT, fiabilité faible |
| Fenêtres ; installation électrique du chauffage | 25 ans ; 20 ans | tableau suisse ImmoWorld/Helvetia [R1-43] (page en erreur 504) | EXTRAIT, fiabilité faible |
| Charpente | — | aucune source trouvée | INCONNU |

Le « tableau paritaire des amortissements » suisse (ASLOCA), source de référence entre bailleurs et locataires, n'a pas pu être lu (erreur serveur 503, quatre tentatives). Pour vérifier : relire https://cd.asloca.ch/sites/default/files/2024-08/Tabelle_amortissements.pdf, ou les tables BCIS/RICS « Life Expectancy of Building Components » (Royaume-Uni), ou le guide « Durées de vie des ouvrages » de l'Agence Qualité Construction.

Point de méthode : sur un monument, la durée de vie réelle dépend surtout de l'**entretien** (crochets et clous, noues, solins, gouttières) plus que du matériau lui-même. La charpente, les maçonneries et les décors n'ont pas de « durée de vie » au sens d'un renouvellement programmé ; ils ont des **cycles de restauration** (HYPOTHÈSE de modélisation, voir § 9).

## 3. Énergie

### 3.1 Performance du bâti ancien (statistique publique)

[R1-21] SDES / ONRE, « Le parc de logements par classe de performance énergétique au 1er janvier 2025 » (novembre 2025), PAGE LUE (PDF, texte extrait localement) :
> « les logements plus anciens, en particulier ceux construits avant 1975, ont une proportion plus élevée de passoires énergétiques (26,7 % pour les logements contruits avant 1948 et 18,3 % pour les logements construits entre 1948 et 1974). »
> « Au sein des résidences principales, les logements chauffés au fioul sont environ 42 % à être classés F ou G (et environ 67 % en incluant l'étiquette E) »
> « 19,9 % des logements de moins de 30 m² ont une étiquette F ou G, contre seulement 9,9 % des logements de plus de 100 m². »
> Résidences secondaires : taux de passoires de 25,6 % au 1er janvier 2025 (tableau).

Limite : statistique sur les **logements**, pas sur les châteaux. Aucune consommation mesurée en kWh/m²/an pour de grandes demeures historiques n'a été trouvée : INCONNU (les hypothèses de consommation retenues pour le tableau sont en § 9.1).

Propos du directeur général des patrimoines au congrès de la Demeure Historique [R1-09], PAGE LUE : « l'essentiel de la déperdition passe par le toit. Si les combles sont isolés, on peut gagner 60% de la consommation énergétique. » (affirmation orale, sans étude citée).

Témoignage britannique [R1-05], PAGE LUE (Kingston Russell House, Grade I) : « it is impossible to increase the insulation or to draught-proof effectively within listed-building constraints […] There is no viable alternative to fossil fuels. »

**DPE et monuments historiques** — [R1-38] Service-public, fiche F16096 (vérifiée le 1er janvier 2026), PAGE LUE : les monuments historiques classés ou inscrits ne sont pas concernés par le DPE (« Il en est de même, notamment, des monuments historiques classés ou inscrits. ») ; « Depuis le 1er janvier 2025, la location d'un logement classé G est interdite » ; F à partir de 2028, E à partir de 2034. Conséquence (à confirmer par R3) : un château **non protégé** (cas possible en S1) qui loue des logements ou gîtes est exposé au calendrier des interdictions de location ; un MH ne l'est pas au titre du DPE. Les seuils chiffrés des classes A à G ne figurent pas sur la fiche (non relevés ici).

Contexte budgétaire [R1-34], PAGE LUE : « les exercices budgétaires 2025 et 2026 constituent deux années blanches pour la transition énergétique du bâti ancien ».

### 3.2 Prix des énergies

**Série 2018-2023, en centimes d'euro TTC par kWh PCI livré** — [R1-22], PAGE LUE (site commercial qui reprend l'« Enquête sur les prix des combustibles bois en 2023 » de l'ADEME ; la source primaire n'a pas pu être téléchargée car l'ADEME exige une adresse e-mail [R1-23]) :

| Énergie (c€ TTC/kWh PCI) | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 |
|---|---|---|---|---|---|---|
| Bois-bûches 33 cm | 3,9 | 3,8 | 4,2 | 4,1 | 4,4 | 4,9 |
| Granulés de bois en vrac | 6,2 | 6,1 | 6,6 | 6,3 | 11,6 | 10,4 |
| Gaz naturel | 7,1 | 7,9 | 7,9 | 6,8 | 8,5 | 11,8 |
| Fioul domestique | 9,1 | 9,4 | 8,2 | 8,9 | 15,1 | 12,6 |
| Propane | 13,4 | 14,9 | 14,6 | 14,8 | 16,1 | 16,9 |
| Électricité | 16,2 | 16,7 | 17,7 | 17,9 | 19,2 | 23,3 |

**Prix officiels 2026** :
- Électricité, tarifs réglementés [R1-24], PAGE LUE (21 juillet 2026) : « augmentation moyenne de + 2,5 % des tarifs réglementés de l'électricité au 1er août 2026 » ; « Le niveau moyen des TRVE est relevé de + 5,98 € TTC/mégawattheure. » ; pour 4,5 MWh/an, « la facture TTC passera de 1 046 € à 1 072 € ». ESTIMATION : 1 072 € / 4,5 MWh ≈ **238 € TTC/MWh** tout compris (abonnement inclus), pour un petit consommateur résidentiel. Un château avec une puissance souscrite élevée aura un coût moyen différent (non vérifié).
- Gaz, prix repère [R1-25], PAGE LUE (12 octobre 2026) : « 194,90 € TTC par mégawattheure (MWh) » au 1er novembre 2026, contre « 182,88 € TTC/MWh » en octobre 2026. Prix repère pour clients résidentiels (abonnement inclus selon la méthode de la CRE — non vérifié).
- Fioul domestique 2025-2026 : **INCONNU**. Les pages officielles (ecologie.gouv.fr, prix des produits pétroliers) ont renvoyé une erreur 503 ; le moteur interne de l'INSEE n'a rien renvoyé. Pour vérifier : bulletin hebdomadaire des prix des produits pétroliers de la DGEC, ou base Pégase du SDES.
- Granulés 2024-2025 : **INCONNU** (enquête ADEME 2024 publiée le 29/10/2025, accessible seulement contre adresse e-mail). Dernière valeur sourcée : 10,4 c€ TTC/kWh en 2023 (vrac).
- Plaquettes forestières (€/MWh) : **INCONNU**. Le volet « chauffage collectif et industriel » de l'enquête ADEME 2024 contient ces prix, mais il n'est pas accessible sans formulaire.

Conséquence pour le modèle (ESTIMATION) : avec les prix 2023-2026 trouvés, le coût de l'énergie livrée (kWh PCI) va d'environ 5 c€/kWh (bûches, 2023) à 24 c€/kWh (électricité, 2026). Le choix d'énergie fait varier la facture d'un facteur 2 à 5 à consommation livrée égale (rendements des appareils non pris en compte).

## 4. Assurance

### 4.1 Données sourcées

- **Prime minimale pour un bien classé** — [R1-26] Le Figaro, 25 février 2020, PAGE LUE (propos de D. de La Fouchardière, directeur général du courtier SLA-Verspieren) :
  > « le niveau de la prime d'assurance annuelle pour un bien classé est rarement inférieur à 2500 € et il ne connaît pas de limite supérieure. »
  > « Un château de 2500 m2 acheté 600.000 €, par exemple, pourra avoir une valeur de reconstruction de 6 millions d'euros »
  > « Les valeurs les plus importantes d'un bâtiment résident dans les toitures et les charpentes »
  > « En cas de sinistre, la compagnie d'assurances aura en effet l'obligation de le reconstruire à l'identique. Et cette reconstruction doit être effectuée suivant les instructions de l'architecte des bâtiments de France. »
  > La surface prise en compte est la « surface développée, qui intègre tous les mètres carrés mesurés en extérieur des murs, y compris ceux des caves et greniers ».
  ESTIMATION : 6 M€ / 2 500 m² = **2 400 €/m²** de valeur de reconstruction dans cet exemple (2020). La valeur de reconstruction peut valoir **10 fois** le prix d'achat.
- **Barème commercial d'un courtier** — [R1-27] France Épargne, guide mis à jour le 25 mai 2026, PAGE LUE (fiabilité faible : chiffres commerciaux sans source) :
  - prime ≈ « 5 ‰ (0,5 %) de la valeur totale assurée » (approximation) ;
  - « Le coût de reconstruction d'un château oscille entre 5 000 et 10 000 €/m² » ;
  - fourchettes annoncées : château moyen 600 m² usage privé 15 000-20 000 €/an ; grand château non classé 900 m² 20 000-30 000 €/an ; château MH 800 m² usage privé 25 000-35 000 €/an ; château MH 1 200 m² usage commercial 40 000-55 000 €/an ; hausse de prime de 30 à 50 % pour un bien classé et de 15 à 25 % pour un inscrit ;
  - RC « 5 à 9 millions d'euros » de plafond ; RC professionnelle en usage commercial 2 000 à 5 000 €/an ;
  - « Seuls 4 à 5 assureurs en France possèdent une véritable expertise » sur les châteaux classés ;
  - exemple restitué par l'outil (paraphrase) : toiture de 500 m² ≈ 250 000 € en construction classique contre 375 000 € « sous prescription ABF », soit ≈ 500 et 750 €/m² (ESTIMATION arithmétique ; chiffres non sourcés par le courtier).
- **Divergence à conserver** : valeur de reconstruction 2 400 €/m² (Figaro 2020, un exemple) contre 5 000-10 000 €/m² (courtier 2026). Écart d'un facteur 2 à 4. Les coûts de construction ont augmenté entre 2020 et 2026, mais cela n'explique pas tout l'écart (HYPOTHÈSE). Valeur de reconstruction d'un château : **non établie** de façon fiable.
- **Surprime catastrophes naturelles** — [R1-29], PAGE LUE (courtier, reprenant l'arrêté du 22 décembre 2023) : le taux de la prime additionnelle CatNat est passé « de 12 % à 20 % » « à compter du 1er janvier 2025 ». Nouvelle carte du retrait-gonflement des argiles au 1er juillet 2026 : « 55 % du territoire métropolitain en aléa moyen ou fort, contre 48 % en 2020 ». Coût moyen d'un sinistre argiles « environ 24 000 euros ».
- **Risque de non-assurabilité (cas réel)** — [R1-28] Assemblée nationale, question écrite n° 12985 (JO 17 février 2026, réponse 28 avril 2026), PAGE LUE : château d'Olhain (Pas-de-Calais), géré par une association et ouvert au public :
  > « Par courrier en date du 27 octobre 2025, l'assureur du site a décidé de résilier le contrat d'assurance […] sans mentionner de motif particulier. Depuis le 1er janvier 2026, le site est dépourvu de couverture assurantielle, ce qui a conduit à sa fermeture totale au public pour une durée indéterminée. »
  > « Aucun sinistre n'a été déclaré sur le site depuis 2015. Plus de 300 000 euros de cotisations ont été versés à l'assureur au cours des quarante dernières années. »
  Réponse du gouvernement : « le Gouvernement n'a pas connaissance d'un retrait significatif des assureurs du marché des monuments historiques » ; aucun dispositif public n'est jugé nécessaire.
- **Royaume-Uni** [R1-05], PAGE LUE : une maison Grade I (Kingston Russell) voit sa prime « more than doubled this year » ; elle dépasse désormais toutes les autres dépenses annuelles de la maison réunies ; « Many insurers will not offer cover at all ».

### 4.2 Lecture pour le modèle (ESTIMATION)

Formule de travail proposée : prime annuelle TTC ≈ taux × valeur de reconstruction assurée. Le seul taux trouvé est « 5 ‰ », donné par un courtier [R1-27] comme approximation. Le Figaro [R1-26] ne donne qu'un plancher (« rarement inférieur à 2500 € ») sans valeur assurée associée : on ne peut pas en déduire de taux. Taux fiable : **INCONNU**, à remplacer par 3 devis de courtiers spécialisés. Ordres de grandeur avancés par le courtier [R1-27] pour 2026 : 15 000 à 55 000 €/an pour des châteaux de 600 à 1 200 m². Aucune source indépendante ne confirme ces montants pour des surfaces de 2 000 à 4 500 m² (S2, S3).

## 5. Taxe foncière

### 5.1 Mode de calcul (source officielle)

[R1-30] Service-public, fiche F59 (vérifiée le 25 septembre 2026), PAGE LUE :
> « La base d'imposition de la TFPB est égale à la moitié de la valeur locative cadastrale. »
> « Cette valeur locative est revalorisée chaque année, en particulier pour tenir compte de l'augmentation des prix. »
> « Les taux d'imposition sont votés par les collectivités territoriales. »
> « Le montant de la TFPB s'obtient en appliquant le taux à la base d'imposition. »
La fiche ne mentionne **aucune exonération** propre aux monuments historiques. La taxe d'enlèvement des ordures ménagères (TEOM) figure sur le même avis.
Taux de revalorisation 2025 et 2026 : non donnés par la page (INCONNU ici ; à lire dans la loi de finances ou sur impots.gouv.fr).

### 5.2 Cas particulier des monuments : la catégorie « maisons exceptionnelles »

[R1-31] La Demeure Historique, fiche F/7 (juin 2003), PAGE LUE :
> « L'administration utilise actuellement les valeurs locatives de 1970, mises à jour chaque année par des taux d'actualisation forfaitaires »
> « La valeur locative de ces derniers a été fixée par référence à celle d'un monument-type situé dans la même région ou le même département. A défaut de monument-type comparable, elle a été calculée en appliquant à la valeur vénale 1970 du monument un taux d'intérêt de 6,50 %, puis en actualisant la somme obtenue »
> « En général, mais pas toujours, la valeur locative d'une maison exceptionnelle, au m2, est sensiblement inférieure à celle d'un logement ordinaire. »
> « Un nombre significatif de monuments situés hors des villes (la proportion n'est pas connue) ont été évalués en 1970 comme logements ordinaires. »
> L'instruction fiscale retient la « superficie développée » ; elle cite « 500 m2 à 600 m2 » comme exemple de « constructions importantes », sans seuil strict.
> Jurisprudence : château de Chalaines (Meuse), inscrit, « surface développée de 1200 m2 », reconnu « local exceptionnel » (TA Nancy, 11 mars 2003).
> « tous les changements de consistance depuis 1970 (par exemple, les transformations de combles ou de communs en locaux habitables) devaient être déclarés aux services du Cadastre. »

Conséquences pour le modèle (ESTIMATION) :
- La taxe foncière d'un château **ne se déduit pas** de sa surface ni de son prix. Elle dépend de la catégorie cadastrale retenue en 1970 (maison exceptionnelle ou logement ordinaire) et du taux communal. Deux châteaux semblables peuvent payer des montants très différents.
- Risque : la transformation de communs en gîtes, salles ou logements crée un « changement de consistance » à déclarer, donc une hausse de la valeur locative et de la taxe.
- Si une activité est exploitée, les locaux affectés à cette activité relèvent probablement d'une autre méthode d'évaluation (locaux professionnels) : point non sourcé ici, à confirmer par R3.

### 5.3 Exemples chiffrés

- [R1-32] Annonce immobilière (château « historic monument », Erny-Saint-Julien, Pas-de-Calais, « Habitable Size: 512 m² », « Land Size: 6.56 ha »), PAGE LUE, déclaratif du vendeur, année non indiquée : « the Tax Foncier, which is only EUR 2,652 ». La même annonce déclare d'autres charges annuelles (voir § 9.3).
- Aucun exemple vérifié de taxe foncière pour un château de 2 000 à 4 500 m² : **INCONNU**. Pour vérifier : demander l'avis de taxe foncière des biens visités (pièce standard d'un dossier de vente), ou l'extrait cadastral et le taux communal (data.gouv.fr publie les taux votés par commune).

## 6. Subventions de travaux

### 6.1 Taux légaux et taux pratiqués (source : Demeure Historique, revue n° 201, 2016) [R1-03] — PAGE LUE

Attention : données de 2014-2016. À actualiser (voir 6.2 et suivants).

- Base légale des monuments **inscrits** (citation de l'article L.621-29 du code du patrimoine reprise par l'article) :
  > « L'autorité administrative est autorisée à subventionner dans la limite de 40 % de la dépense effective, les travaux d'entretien et de réparation que nécessite la conservation des immeubles ou parties d'immeubles inscrits au titre des monuments historiques ».
- Monuments **classés** et taux réels :
  > « Pour les monuments classés, l'État est en théorie autorisé à subventionner jusqu'à 100 %. En pratique, les taux moyens d'intervention se situent autour de 30 % pour les monuments classés et 15 % pour les inscrits. »
  (note 6 de l'article : décret n° 2000-1022 du 17 octobre 2000, pris en application du décret n° 99-1060 du 16 décembre 1999. Ces textes ont pu être modifiés ou remplacés depuis 2016 : non vérifié ici, à confirmer par R3.)
- Revendication de l'association (donc **pas** le taux en vigueur) : « que les taux de subvention alloués à ce secteur soient à hauteur de 60 % pour les monuments classés et 40 % pour les monuments inscrits, en l'absence d'intervention des collectivités ».
- Dépenses éligibles (art. 2 du décret n° 99-1060, cité) : « les études, les acquisitions immobilières, les travaux de construction ou d'aménagement, les grosses réparations, l'équipement en matériel à l'exclusion du simple renouvellement. » ; « les assurances travaux ne sont pas des dépenses subventionnées, contrairement à l'assistance à la maitrise d'ouvrage (AMO). »
- Délais et trésorerie :
  > « La décision de subvention a une durée de validité de deux ans (sauf prorogation exceptionnelle) et sa liquidation intervient dans un délai de quatre ans à partir de la date de démarrage de l'opération. »
  > « il est possible d'obtenir dans certains cas le versement d'une avance […] dans la limite de 30 % du montant prévisionnel de la subvention (voire 50 % dans certains cas). » (art. R.621-78 du code du patrimoine)
  > « Attention : Aucune subvention ne peut être accordée si les travaux ont commencé. »
  Conséquence pour le modèle (ESTIMATION) : le propriétaire préfinance l'essentiel des travaux ; la subvention arrive avec un décalage pouvant aller jusqu'à plusieurs années. Il faut une ligne de trésorerie (fonds de roulement) dédiée.

### 6.2 Montants publics (données 2014-2016, [R1-03], PAGE LUE)

- Programme 175 « Patrimoines », loi de finances 2016 : « 873,64 millions d'euros dont 312,88 millions affectés à la restauration des monuments historiques publics ou privés » ; « 157,89 millions d'euros ont été prévus pour les monuments n'appartenant pas à l'État ».
- Crédits de l'État versés aux **MH privés** en 2014 : **25,44 M€**, « soit 9,8 % des crédits monuments historiques » (crédits de paiement effectivement versés).
- Moyenne par opération DRAC (2014) : Île-de-France « 3,97 millions pour 89 opérations (soit une moyenne de 44 668 euros par opération) » ; Haute-Normandie « 651 000 euros […] pour 33 opérations (soit une moyenne de 19 727 euros par opération) » ; dotation moyenne par DRAC « 1,34 million d'euros pour 57 opérations ».
- Régions : « En 2014, les conseils régionaux ont versé 3,12 millions d'euros aux monuments historiques privés, pour un total de 157 opérations » ; moyenne 2003-2014 « environ 20 830 euros par opération » ; « onze n'ont aucune politique de financement en faveur des monuments historiques privés, soit 52 % des régions interrogées » (21 régions de l'époque).
- Départements : « La somme totale versée par les conseils départementaux en 2014 est de 4,70 millions d'euros. Trente-huit conseils départementaux n'interviennent pas en faveur des monuments historiques privés […] c'est-à-dire 41 % des départements interrogés. »
- Collectivités au total : « En 2014, le cumul de l'enveloppe affectée aux propriétaires privés s'élevait à 7,82 millions d'euros pour 437 opérations, contre 11,84 millions d'euros en 2003. »

Lecture pour le modèle (ESTIMATION) : en 2014, l'argent public total vers les MH privés était de l'ordre de 25,44 + 7,82 ≈ 33 M€/an pour toute la France. Les subventions sont donc rares, plafonnées et non automatiques : elles ne doivent pas être comptées comme un revenu récurrent garanti.

### 6.3 Taux pratiqués actuellement et budget 2026 (sources parlementaires 2025)

**Taux moyens de l'État (DRAC)** — [R1-34] Sénat, avis sur le PLF 2026 (3 décembre 2025), PAGE LUE :
> « Ces crédits sont attribués à des collectivités territoriales ou à des particuliers pour les travaux d'entretien ou de restauration réalisés sur les monuments dont ils sont propriétaires et dont ils assurent la maîtrise d'ouvrage […]. Le taux de participation aux projets est en moyenne de 20 % pour les monuments inscrits et de 40 % pour les monuments classés. »
Divergence conservée : la Demeure Historique écrivait en 2016 « autour de 30 % pour les monuments classés et 15 % pour les inscrits » [R1-03]. Le chantier public de Sedan (2024) a reçu exactement 40,0 % [R1-17].

**Budget 2026 en forte baisse** — [R1-34] et [R1-33], PAGES LUES :
- Programme 175 (PLF 2026) : « 1 047,38 millions d'euros en autorisations d'engagement (AE) et 1 145,32 millions d'euros en crédits de paiement (CP) », soit « -232 millions d'euros, soit -18 % » en AE et « 106 millions d'euros (-8 %) » en CP par rapport à 2025 [R1-33], [R1-34].
- Action 1 « Monuments historiques » : 609,6 → 400,2 M€ en AE (−34 %) ; 551,5 → 437,1 M€ en CP (−21 %) [R1-34, tableau].
- « Les crédits d'intervention des directions régionales des affaires culturelles (Drac) seront en baisse de 38 % en AE (-163 millions d'euros) et de 29 % en CP (-172 millions d'euros). » [R1-34] ; montant 2026 : « 91,5 millions d'euros en AE et 112 millions d'euros en CP » [R1-33].
- DGPA citée par le Sénat : le resserrement obligera les DRAC à prioriser selon « le niveau de maturité des chantiers, la complétude du tour de table financier et l'état sanitaire des biens » ; « le financement de nombreux chantiers s'en trouvera reporté ».
- Sort final de ces crédits après le vote de la loi de finances 2026 : non vérifié (INCONNU). À vérifier dans la loi de finances promulguée et les éventuels décrets d'annulation.

**Fonds incitatif et partenarial (FIP)** — réservé aux **petites communes** (pas aux propriétaires privés en tant que tels, sauf si le monument est situé dans une petite commune éligible : à confirmer) :
- [R1-34] : « le soutien aux projets des petites communes cofinancés au moins à 15 % par la région peut être porté au-delà des taux habituels d'intervention » ; « 1035 projets depuis sa création en 2018 » ; crédits « diminués de moitié », à « 10 millions d'euros en AE comme en CP » en 2026.
- [R1-33] : « En 2024, 160 opérations ont été cofinancées par les Drac au titre du FIP pour un budget de 20 millions d'euros en AE. »
- [R1-09] (propos du DGPA, 2022) : « si la région apporte 15% de subvention, l'État peut donner un complément financier (le plus souvent jusqu'à 80%) » — formulation ambiguë (80 % de financement public cumulé ?) ; à vérifier.

**Loto du patrimoine / Mission Patrimoine en péril** :
- [R1-34] : « 182 millions d'euros collectés via le Loto du patrimoine entre 2017 et 2024, et 312 millions d'euros mobilisés en incluant le mécénat d'entreprise et le soutien du ministère de la Culture » ; « Depuis 2018, 15 millions d'euros annuels permettent de compléter le financement des chantiers sélectionnés […]. Inscrits pour la première fois en LFI en 2025, ces crédits ne sont pas reconduits pour 2026. » ; convention tripartite (ministère, Fondation du patrimoine, FDJ) « renouvelée pour quatre ans en janvier 2025 ».
- Montants par site (pages projets, PAGES LUES) : château de Bas (54) « Loto du patrimoine : 280 000 € » sur 392 724 € [R1-12] ; château de Vauville (50) « 165 000 € » sur 165 340 € [R1-13] ; château de Meung-sur-Loire (45) « 148 000 € » sur 310 995 € [R1-16].
- Lecture (ESTIMATION) : un site sélectionné reçoit typiquement de l'ordre de 150 000 à 300 000 € **une seule fois** ; la sélection est concurrentielle et ponctuelle. Ce n'est pas une ressource récurrente.

**État sanitaire du parc (contexte)** — [R1-34] : « environ 18 % des 36 512 monuments évalués (sur 45 070) sont en mauvais état, et 5 % en état de péril » (bilan publié en mai 2025, période 2019-2024) ; « En 2024, les crédits dédiés à la conservation préventive des monuments représentaient un peu moins de 18 % de ceux alloués à leur restauration. » [R1-33] : « sur les 1 789 monuments historiques classés comme étant en péril », « plus de 55 % appartiennent à des propriétaires privés ».

### 6.4 Délais réels

- Règles : validité de la décision de subvention « deux ans », liquidation « dans un délai de quatre ans », avance « dans la limite de 30 % » [R1-03] ; « Aucune subvention ne peut être accordée si les travaux ont commencé. » [R1-03].
- Exemples de durée de chantier : Meung-sur-Loire « environ 18 mois » [R1-16] ; Montautre 14 mois par phase, programme étalé de 2022 à 2027 [R1-14] ; Sedan de décembre 2023 à mars 2025 [R1-17] ; cas ERP « plus de deux ans » de procédure [R1-10].
- Délai moyen entre la demande de subvention et le versement : **INCONNU** (aucune statistique trouvée). Pour vérifier : rapport annuel de performance du programme 175 (indicateurs de délai), ou la DRAC de la région ciblée.

### 6.5 Synthèse pour le modèle (ESTIMATION)

- Taux attendu sur les travaux **éligibles** : 20 % (inscrit) à 40 % (classé), en moyenne, si le dossier est retenu ; 0 % pour un bâtiment non protégé (hors Fondation du patrimoine et collectivités).
- En 2026, les crédits DRAC baissent de 29 % (CP) : probabilité d'obtention et délais à dégrader.
- Régions et départements : aides très inégales selon le territoire (52 % des régions et 41 % des départements n'aidaient pas les MH privés en 2014 [R1-03] ; donnée ancienne).
- Traitement recommandé : modéliser les subventions comme un **scénario favorable** appliqué au seul gros entretien éligible, avec décalage de trésorerie de 1 à 4 ans, et non comme un revenu de base.

## 7. Imprévus et sinistres

### 7.1 Fréquence des sinistres dans les monuments historiques

- [R1-35] Ministère de la Culture, « Bilans des sinistres dans les monuments historiques » — EXTRAIT seulement (la page n'a pas pu être ouverte : URL en 404, deux URL alternatives essayées sans succès). Chiffres vus dans le résultat de recherche : en 2025, « 67 sinistres » recensés dans les immeubles classés ou inscrits, publics ou privés, dont 16 incendies, 33 événements climatiques et 15 dégradations ; causes des 16 incendies : 9 inconnues, 2 dysfonctionnements électriques, 3 travaux ou point chaud, 1 foudre, 1 malveillance. Sur 2013-2025, « 295 sinistres » (≈ 22,7 par an). Incohérence apparente entre 67 en 2025 et une moyenne de 22,7/an : soit forte hausse du recensement, soit le total de 295 porte sur une seule catégorie. **À vérifier sur le document original.**
- ESTIMATION (très fragile) : rapportés aux ≈ 45 070 immeubles protégés [R1-34], 67 sinistres recensés par an donnent une probabilité de l'ordre de 0,15 % par monument et par an, dont ≈ 0,04 % pour l'incendie. Il s'agit de sinistres **déclarés au ministère**, donc probablement sous-estimés. Aucune statistique propre aux châteaux privés n'a été trouvée : INCONNU.
- Argiles : nouvelle carte au 1er juillet 2026, « 55 % du territoire métropolitain en aléa moyen ou fort » ; coût moyen d'un sinistre argiles « environ 24 000 euros » [R1-29] (source de courtier reprenant des données publiques).

### 7.2 Dépassements et travaux d'urgence (cas réels)

- [R1-05] Boughton Monchelsea Place : devis « £42,000 », facture « nearly £54,000 » hors TVA après découvertes en cours de chantier (≈ +29 %, ESTIMATION) ; mur d'enceinte renversé par le vent : devis « in excess of £5,000 », réalisé pour « £4,000 ».
- [R1-05] Kingston Russell House : infiltration due à la pluie et au vent dans la galerie supérieure, « extensive structural and decorative damage » ; fenêtres déposées et refaites « pane by pane, a process that took many months ».
- [R1-05] Rapport Harlow : la dépense prévue (≈ 105 000 £/an) est inférieure à la dépense constatée (≈ 156 000-161 000 £/an), notamment parce que « planned expenditure may not include adequate contingency for unanticipated emergency works ».

### 7.3 Pratique des provisions

- Aucune source trouvée sur la pratique réelle de provision des propriétaires de châteaux en France : **INCONNU**. Pour vérifier : la Demeure Historique (guides de gestion), un expert-comptable spécialisé MH ; aspects comptables et fiscaux (provision pour gros entretien d'une société) : voir R3.
- Pratique britannique documentée : l'état sanitaire est revu selon un cycle « quinquennial » (rapport d'état tous les cinq ans), mais seuls 36 % des propriétaires interrogés en disposent [R1-05].
- HYPOTHÈSE de modélisation proposée (non sourcée) : réserve pour aléas = 10 à 20 % du budget annuel de gros entretien, plus la franchise d'assurance annualisée, plus un fonds de réserve plafonné équivalent à 1 an de gros entretien. Le cas britannique (+29 %) se situe au-dessus de cette fourchette.

## 8. Postes techniques récurrents

| Poste | Obligation / fréquence | Coût | Statut |
|---|---|---|---|
| Assainissement non collectif (fosse, filtre) | Contrôle du SPANC « au moins tous les 10 ans » ; travaux de mise en conformité « dans un délai de 4 ans » en cas de danger sanitaire ; vidange quand les boues dépassent « en général » 50 % du volume utile [R1-36] | Contrôle « obligatoire et payant », tarif non précisé | PAGE LUE (règles) ; coût INCONNU |
| Ramonage des conduits | Obligation fixée par le règlement sanitaire départemental (fréquence non vérifiée ici) | INCONNU | INCONNU — vérifier le RSD du département visé |
| Entretien annuel de chaudière | Obligation non vérifiée dans une source lue | INCONNU | INCONNU |
| Paratonnerre | Aucune source lue (règles ERP à voir avec R3) | INCONNU | INCONNU |
| Alarme intrusion et incendie, télésurveillance | Recommandée par les courtiers pour modérer la prime [R1-26] : « Installer des dispositifs de prévention (détecteurs de fumée, système de télésurveillance, aménagement d'une entrée pour les pompiers…) aidera aussi à modérer le coût de l'assurance » | INCONNU | PAGE LUE (principe) ; coût INCONNU |
| Sûreté lors d'ouvertures au public | La Demeure Historique signale que des équipements de sûreté (portiques, vidéosurveillance) « restent difficile à financer » [R1-01] | INCONNU | PAGE LUE (principe) |
| Eau, électricité hors chauffage, internet (petit château) | — | déclaré par un vendeur pour un château de 512 m² habitables : eau « EUR 432 », électricité « EUR 746 », internet « EUR 468 » par an [R1-32] | PAGE LUE, fiabilité faible |

Pour vérifier les coûts : demander des devis (contrat de télésurveillance, vérification de paratonnerre, ramonage, entretien de chaudière) pour un bâtiment type ; consulter le règlement sanitaire départemental et le règlement du SPANC de la commune.

## 9. Livrable : tableau des coûts annuels du bâti S1, S2, S3

Statut global du tableau : **ESTIMATION**, construite à partir de quelques paramètres sourcés et de plusieurs HYPOTHÈSES explicites. Calcul reproductible : paramètres en 9.1, code complet du script `r1_budget.py` en 9.5. Montants en € 2026, **TTC** (un particulier ne récupère pas la TVA ; HYPOTHÈSE de lecture : les valeurs de reconstruction des assureurs sont des coûts TTC). Aucune actualisation n'a été appliquée à la valeur de reconstruction de 2020 (indice du coût de la construction non relevé).

**Hors périmètre de ce tableau** : personnel (gardien, jardiniers, etc. → R2), jardins, parc, terres et installations équestres (→ R2, R6), taxe foncière sur le **non bâti** (→ R2/R8), assurance du **mobilier et des œuvres**, mises aux normes ERP et accessibilité liées à une activité (→ R3, R7), investissements de transformation (gîtes, salles), rattrapage d'un éventuel retard d'entretien à l'achat.

### 9.1 Paramètres et statut

| Paramètre | Valeur retenue | Statut | Source / justification |
|---|---|---|---|
| Surfaces château / dépendances | S1 900 / 600 m² ; S2 2 000 / 2 500 m² ; S3 4 500 / 4 000 m² | HYPOTHÈSE de scénario | Contexte_permanent § 4 |
| Valeur de reconstruction du château | S1 et S2 : 2 400 à 5 000 €/m² ; S3 : 5 000 à 10 000 €/m² | bornes sourcées, affectation par scénario = HYPOTHÈSE | 2 400 €/m² : exemple Figaro 2020 [R1-26] ; 5 000-10 000 €/m² : courtier 2026 [R1-27] (fiabilité faible) |
| Valeur de reconstruction des dépendances | 50 % de celle du château au m² | HYPOTHÈSE (non sourcée) | constructions plus simples (écuries, granges) |
| Entretien et réparation total (courant + gros entretien) | 2 à 4 % de la valeur de reconstruction par an | sourcé (contexte différent) | NRC, bâtiments publics américains [R1-07], « absolute minimum » [R1-08] |
| Part « entretien courant » | 0,5 à 1 % de la valeur de reconstruction ; le reste = provision de gros entretien | HYPOTHÈSE | aucune source de ventilation trouvée |
| Surface chauffée équivalente | S1 : 50 à 80 % des 700 m² habitables ; S2 : 40 à 60 % du château ; S3 : 30 à 50 % du château | HYPOTHÈSE | résidence privée + pièces de réception chauffées par intermittence |
| Consommation de chauffage et d'eau chaude | 150 à 300 kWh d'énergie finale par m² chauffé et par an | HYPOTHÈSE | aucune mesure de château trouvée ; le SDES qualifie de « très énergivores » les logements au-delà de 450 kWh/m² d'énergie finale [R1-21] |
| Prix de l'énergie de chauffage | 0,10 à 0,20 € TTC/kWh | sourcé (bornes) | granulés en vrac 10,4 c€ (2023) [R1-22] ; gaz, prix repère 19,49 c€ (nov. 2026) [R1-25] |
| Électricité spécifique | 15 à 30 kWh par m² chauffé, à 0,238 € TTC/kWh | consommation = HYPOTHÈSE ; prix = ESTIMATION | 1 072 € / 4,5 MWh [R1-24] |
| Assurance | 5 ‰ de la valeur de reconstruction totale | sourcé, fiabilité faible | courtier [R1-27] ; observations réelles bien plus basses (voir 9.3) |
| Taxe foncière bâtie | château 3 à 10 €/m² ; dépendances 1 à 3 €/m² | HYPOTHÈSE | un seul repère : 2 652 € pour 512 m² habitables ≈ 5,2 €/m² [R1-32] |
| Imprévus | 10 à 20 % de la provision de gros entretien | HYPOTHÈSE | dépassement observé de +29 % sur un chantier britannique [R1-05] |

### 9.2 Résultats par scénario (€ TTC 2026 par an ; fourchette basse – centrale – haute)

La valeur basse combine toutes les bornes basses, la haute toutes les bornes hautes ; la centrale utilise les paramètres médians.

**S1 — Domaine relativement économique** (château 900 m², dépendances 600 m², total bâti 1 500 m² ; valeur de reconstruction 2,9 à 6,0 M€, centrale 4,4 M€)

| Poste | Basse | Centrale | Haute | €/m² bâti/an (bas – haut) |
|---|---|---|---|---|
| Entretien courant | 14 400 | 33 300 | 60 000 | 9,6 – 40,0 |
| Provision de gros entretien | 43 200 | 99 900 | 180 000 | 28,8 – 120,0 |
| Énergie | 6 500 | 17 800 | 37 600 | 4,3 – 25,1 |
| Assurance | 14 400 | 22 200 | 30 000 | 9,6 – 20,0 |
| Taxe foncière bâtie | 3 300 | 7 000 | 10 800 | 2,2 – 7,2 |
| Imprévus | 4 300 | 15 000 | 36 000 | 2,9 – 24,0 |
| **Total bâti** | **86 100** | **195 200** | **354 400** | **57 – 236** |

**S2 — Grand domaine équestre haut de gamme** (château 2 000 m², dépendances 2 500 m², total 4 500 m² ; valeur de reconstruction 7,8 à 16,3 M€, centrale 12,0 M€)

| Poste | Basse | Centrale | Haute | €/m² bâti/an (bas – haut) |
|---|---|---|---|---|
| Entretien courant | 39 000 | 90 200 | 162 500 | 8,7 – 36,1 |
| Provision de gros entretien | 117 000 | 270 600 | 487 500 | 26,0 – 108,3 |
| Énergie | 14 900 | 39 100 | 80 600 | 3,3 – 17,9 |
| Assurance | 39 000 | 60 100 | 81 200 | 8,7 – 18,1 |
| Taxe foncière bâtie | 8 500 | 18 000 | 27 500 | 1,9 – 6,1 |
| Imprévus | 11 700 | 40 600 | 97 500 | 2,6 – 21,7 |
| **Total bâti** | **230 100** | **518 600** | **936 800** | **51 – 208** |

**S3 — Domaine historique ultra-premium** (château 4 500 m², dépendances 4 000 m², total 8 500 m² ; valeur de reconstruction 32,5 à 65 M€, centrale 48,8 M€)

| Poste | Basse | Centrale | Haute | €/m² bâti/an (bas – haut) |
|---|---|---|---|---|
| Entretien courant | 162 500 | 365 600 | 650 000 | 19,1 – 76,5 |
| Provision de gros entretien | 487 500 | 1 096 900 | 1 950 000 | 57,4 – 229,4 |
| Énergie | 25 100 | 70 400 | 151 100 | 2,9 – 17,8 |
| Assurance | 162 500 | 243 800 | 325 000 | 19,1 – 38,2 |
| Taxe foncière bâtie | 17 500 | 37 200 | 57 000 | 2,1 – 6,7 |
| Imprévus | 48 800 | 164 500 | 390 000 | 5,7 – 45,9 |
| **Total bâti** | **903 800** | **1 978 400** | **3 523 100** | **106 – 415** |

### 9.3 Repères observés pour juger ces ordres de grandeur (conversion à 1 £ = 1,185 €, taux BCE du 14 octobre 2026 [R1-37])

| Repère | Montant | Statut / source | Comparaison |
|---|---|---|---|
| Dépense moyenne d'entretien-réparation du bâtiment principal, maisons historiques britanniques (2024) | 156 067 à 160 686 £ TTC ≈ 185 000 à 190 000 € | PAGE LUE [R1-05] | Proche du bas de la fourchette S2 (entretien courant + gros entretien : 156 000 à 650 000 €). Dépense jugée **insuffisante** par le rapport (retard moyen ≈ 1 994 000 £ ≈ 2,36 M€). |
| Besoin de réparations urgentes (5 ans), même échantillon | ≈ 893 000 £ ≈ 1,06 M€, soit ≈ 212 000 €/an | PAGE LUE [R1-05] ; annualisation = ESTIMATION | S'ajoute en partie à la dépense courante (lien exact non établi). |
| Plancher Demeure Historique (hors restauration et ouverture) | 40 000 €/an minimum (2019) | PAGE LUE [R1-01] | Comparable à S1 bas (entretien courant + assurance + taxe ≈ 32 000 €), mais le chiffre DH inclut aussi un gardien. |
| Petite maison Grade I (Kingston Russell) | 12 000-20 000 £/an + 50 000-100 000 £ tous les ≈ 10 ans ≈ 20 000 à 36 000 €/an | PAGE LUE [R1-05] ; annualisation = ESTIMATION | Nettement sous S1 bas (57 600 € d'entretien total), pour une maison plus petite (surface non publiée) et avec des travaux différés (pierre, fenêtres). |
| Petit château MH (512 m² habitables, 6,56 ha) : charges déclarées par le vendeur | ≈ 14 600 €/an (dont chauffage 3 978 €, assurance 2 198 €, taxe foncière 2 652 €, personnel 4 163 €), sans gros entretien | PAGE LUE, fiabilité faible [R1-32] | Montre l'écart entre charges **déclarées à la vente** et coût complet d'un entretien d'exception. |
| Château d'Olhain : cotisations d'assurance | > 300 000 € en 40 ans, soit ≈ 7 500 €/an en moyenne nominale | PAGE LUE [R1-28] ; moyenne = ESTIMATION | Très en dessous de la formule courtier (5 ‰) : sous-assurance possible ou barème courtier élevé. **Divergence non résolue.** |

### 9.4 Lecture pour le modèle

1. **Le gros entretien domine** : 51 à 55 % du total central dans les trois scénarios. C'est le poste le plus incertain, car il repose sur deux paramètres faibles : la valeur de reconstruction au m² (facteur 2 à 4 entre les sources) et le ratio de 2 à 4 % (conçu pour des bâtiments publics américains). Ce résultat va dans le sens de l'hypothèse H2, sans la démontrer.
2. **Énergie et taxe foncière pèsent peu** : énergie 4 à 9 % et taxe foncière 2 à 4 % du total central. L'énergie peut toutefois doubler selon le combustible (bois ou granulés contre gaz ou fioul).
3. **Assurance** : 11 à 12 % du total central. La formule du courtier donne des primes de 3 à plus de 10 fois supérieures aux cas observés : à remplacer en priorité par des devis.
4. **Flux de trésorerie** : la provision de gros entretien n'est pas décaissée régulièrement. Elle se matérialise en chantiers de 40 000 à 400 000 € (S1-S2, cf. § 2.2), à préfinancer, les subventions arrivant avec retard (§ 6). Le modèle doit prévoir une **réserve de liquidité** (cf. leçon 7 du contexte : EBITDA positif mais trésorerie négative après gros entretien).
5. **Subventions** : en cas de succès, 20 % (inscrit, S2) à 40 % (classé, S3) du gros entretien **éligible** sur le monument protégé [R1-34] ; 0 % en S1 si le château n'est pas protégé. Sur la valeur centrale, l'allègement maximal théorique serait de l'ordre de 54 000 €/an en S2 (20 % × 270 600) et 439 000 €/an en S3 (40 % × 1 096 900), à **réduire** pour tenir compte de la part non éligible (dépendances non protégées, entretien courant), de la probabilité d'obtention et des délais (ESTIMATION). Non retenu dans le total.
6. **Rattrapage initial** : si le domaine acquis présente un retard d'entretien comparable à la moyenne britannique (≈ 2 M£ par maison), ce montant s'ajoute aux besoins. Il relève du plan d'investissement initial, pas du budget annuel de fonctionnement ci-dessus.

### 9.5 Script de calcul du tableau (Python, reproductible)

Exécution : `python3 r1_budget.py`. Les commentaires indiquent le statut de chaque paramètre (S = sourcé, H = hypothèse, E = estimation).

```python
# R1 — calcul traçable du tableau des coûts annuels du bâti (S1, S2, S3)
# Statuts : chaque paramètre est marqué S (sourcé), H (hypothèse) ou E (estimation dérivée).
SCEN = {
 # surfaces = paramètres de scénario (Contexte_permanent.md §4) -> H
 "S1": dict(chateau=900, dep=600, hab=700, crv_lo=2400, crv_hi=5000, heat_lo=0.50, heat_hi=0.80, heat_base="hab"),
 "S2": dict(chateau=2000, dep=2500, hab=None, crv_lo=2400, crv_hi=5000, heat_lo=0.40, heat_hi=0.60, heat_base="chateau"),
 "S3": dict(chateau=4500, dep=4000, hab=None, crv_lo=5000, crv_hi=10000, heat_lo=0.30, heat_hi=0.50, heat_base="chateau"),
}
DEP_RATIO = 0.5          # H : valeur de reconstruction des dépendances = 50 % de celle du château au m²
MR_LO, MR_HI = 0.02, 0.04  # S [R1-07] : entretien-réparation = 2 à 4 % de la valeur de remplacement
COUR_LO, COUR_HI = 0.005, 0.010  # H : part "entretien courant" dans ce total (le reste = gros entretien)
KWH_LO, KWH_HI = 150, 300  # H : kWh d'énergie finale chauffage+ECS par m² chauffé (seuil "très énergivore" > 450, S [R1-21])
P_LO, P_HI = 0.10, 0.20    # S/E : €/kWh TTC (granulés 2023 10,4 c€ ; gaz prix repère nov. 2026 19,49 c€) [R1-22][R1-25]
ELEC_KWH_LO, ELEC_KWH_HI = 15, 30  # H : kWh d'électricité spécifique par m² chauffé
P_ELEC = 0.238             # E : 1 072 € / 4,5 MWh [R1-24]
INS_RATE = 0.005           # S (courtier, fiabilité faible) [R1-27] : 5 ‰ de la valeur assurée
TF_CH_LO, TF_CH_HI = 3, 10 # H : taxe foncière €/m² de plancher du château (repère unique 5,2 €/m² hab. [R1-32])
TF_DEP_LO, TF_DEP_HI = 1, 3# H : taxe foncière €/m² de dépendances
IMP_LO, IMP_HI = 0.10, 0.20# H : aléas = 10 à 20 % du gros entretien

def r(x): return int(round(x, -2))
rows = []
for s, p in SCEN.items():
    crv_ch_lo = p["chateau"]*p["crv_lo"]; crv_ch_hi = p["chateau"]*p["crv_hi"]
    crv_dep_lo = p["dep"]*p["crv_lo"]*DEP_RATIO; crv_dep_hi = p["dep"]*p["crv_hi"]*DEP_RATIO
    crv_lo = crv_ch_lo + crv_dep_lo; crv_hi = crv_ch_hi + crv_dep_hi
    mr_lo = crv_lo*MR_LO; mr_hi = crv_hi*MR_HI
    cour_lo = crv_lo*COUR_LO; cour_hi = crv_hi*COUR_HI
    ge_lo = mr_lo - cour_lo; ge_hi = mr_hi - cour_hi
    base = p["hab"] if p["heat_base"]=="hab" else p["chateau"]
    heat_lo = base*p["heat_lo"]; heat_hi = base*p["heat_hi"]
    en_lo = heat_lo*KWH_LO*P_LO + heat_lo*ELEC_KWH_LO*P_ELEC
    en_hi = heat_hi*KWH_HI*P_HI + heat_hi*ELEC_KWH_HI*P_ELEC
    ins_lo = crv_lo*INS_RATE; ins_hi = crv_hi*INS_RATE
    tf_lo = p["chateau"]*TF_CH_LO + p["dep"]*TF_DEP_LO; tf_hi = p["chateau"]*TF_CH_HI + p["dep"]*TF_DEP_HI
    imp_lo = ge_lo*IMP_LO; imp_hi = ge_hi*IMP_HI
    tot_lo = cour_lo+ge_lo+en_lo+ins_lo+tf_lo+imp_lo; tot_hi = cour_hi+ge_hi+en_hi+ins_hi+tf_hi+imp_hi
    surf = p["chateau"]+p["dep"]
    print(f"== {s}: château {p['chateau']} m², dépendances {p['dep']} m², total bâti {surf} m²")
    print(f"   Valeur de reconstruction: château {crv_ch_lo/1e6:.2f}-{crv_ch_hi/1e6:.2f} M€ ; dépendances {crv_dep_lo/1e6:.2f}-{crv_dep_hi/1e6:.2f} M€ ; total {crv_lo/1e6:.2f}-{crv_hi/1e6:.2f} M€")
    print(f"   Surface chauffée équivalente: {heat_lo:.0f}-{heat_hi:.0f} m²")
    for name, lo, hi in [("Entretien courant", cour_lo, cour_hi), ("Provision gros entretien", ge_lo, ge_hi),
                         ("Énergie", en_lo, en_hi), ("Assurance", ins_lo, ins_hi), ("Taxe foncière bâtie", tf_lo, tf_hi),
                         ("Imprévus", imp_lo, imp_hi), ("TOTAL", tot_lo, tot_hi)]:
        print(f"   {name:26s} {r(lo):>10,} – {r(hi):>10,} €/an | {lo/surf:6.1f} – {hi/surf:6.1f} €/m² bâti/an | {lo/p['chateau']:6.1f} – {hi/p['chateau']:6.1f} €/m² château/an".replace(",", " "))

print("\n== VALEURS CENTRALES (paramètres médians, ESTIMATION)")
for s, p in SCEN.items():
    crv_m = (p["crv_lo"]+p["crv_hi"])/2
    crv = p["chateau"]*crv_m + p["dep"]*crv_m*DEP_RATIO
    mr = crv*(MR_LO+MR_HI)/2; cour = crv*(COUR_LO+COUR_HI)/2; ge = mr-cour
    base = p["hab"] if p["heat_base"]=="hab" else p["chateau"]
    heat = base*(p["heat_lo"]+p["heat_hi"])/2
    en = heat*(KWH_LO+KWH_HI)/2*(P_LO+P_HI)/2 + heat*(ELEC_KWH_LO+ELEC_KWH_HI)/2*P_ELEC
    ins = crv*INS_RATE
    tf = p["chateau"]*(TF_CH_LO+TF_CH_HI)/2 + p["dep"]*(TF_DEP_LO+TF_DEP_HI)/2
    imp = ge*(IMP_LO+IMP_HI)/2
    tot = cour+ge+en+ins+tf+imp
    surf = p["chateau"]+p["dep"]
    print(f"{s}: CRV {crv/1e6:.2f} M€ | courant {r(cour):,} | gros entretien {r(ge):,} | énergie {r(en):,} | assurance {r(ins):,} | TF {r(tf):,} | imprévus {r(imp):,} | TOTAL {r(tot):,} €/an | {tot/surf:.0f} €/m² bâti | {tot/p['chateau']:.0f} €/m² château".replace(",", " "))
# Repères de comparaison
GBP_EUR = 1/0.84385  # S [R1-37] BCE 14/10/2026
print("\n== REPÈRES")
print(f"1 £ = {GBP_EUR:.3f} € (BCE 14/10/2026)")
for lbl, gbp in [("HH moyenne dépense R&M bât. principal bas", 156067), ("HH moyenne haut", 160686), ("HH VAT-registered haut", 185264),
                 ("HH prévu/an", 105000), ("HH urgent/an (893k/5)", 893000/5), ("HH retard total moyen", 1994000),
                 ("Kingston Russell routine bas", 12000), ("Kingston Russell routine haut", 20000)]:
    print(f"   {lbl:45s} {gbp:>12,.0f} £ = {gbp*GBP_EUR:>12,.0f} €".replace(",", " "))
print(f"   Kingston Russell total annualisé (routine + projet décennal) : {(12000+50000/10)*GBP_EUR:,.0f} – {(20000+100000/10)*GBP_EUR:,.0f} €/an".replace(",", " "))
print(f"   Annonce Erny-St-Julien total charges déclarées : {2652+3978+746+432+2198+4163+468:,} €/an".replace(",", " "))
print(f"   Olhain : cotisations moyennes ≈ {300000/40:,.0f} €/an (nominal, 40 ans)".replace(",", " "))
```

## Contre-exemples et cas d'échec trouvés

1. **Château d'Olhain (Pas-de-Calais) — perte d'assurance et fermeture** [R1-28], PAGE LUE : contrat résilié par l'assureur par courrier du 27 octobre 2025, « sans mentionner de motif particulier » ; site « dépourvu de couverture assurantielle » depuis le 1er janvier 2026, d'où une « fermeture totale au public pour une durée indéterminée », alors qu'« Aucun sinistre n'a été déclaré sur le site depuis 2015 ». Le gouvernement refuse tout dispositif public (avril 2026).
2. **Maisons historiques britanniques — retard d'entretien qui se creuse malgré la dépense** [R1-04], [R1-05], [R1-06], PAGES LUES : retard total « doubled to £2bn since the start of the Covid pandemic » ; retard moyen ≈ 1 994 000 £ par propriété malgré ≈ 156 000-161 000 £ dépensés par an ; « 47% of Historic Houses places delayed or cancelled urgent repairs and maintenance works due to lack of funds between 2020 and 2022 ». Dépense prévue (≈ 105 000 £/an) inférieure à la dépense passée.
3. **Rotation rapide des monuments achetés** [R1-10], PAGE LUE (affirmation d'association, 2017) : « plus de 1 000 monuments historiques sont en vente » ; « la durée moyenne de détention se réduit à 7 ans après l'acquisition d'un monument historique ».
4. **La visite seule ne paie pas** [R1-01], PAGE LUE : « Pour 99,8 % des propriétaires, la seule activité d'ouverture à la visite n'est donc pas rentable et généralement déficitaire » ; « Au-dessous de 10 000 visiteurs payants annuels, le résultat coûts/recettes est toujours négatif ».
5. **Mise aux normes ERP d'une salle de réception dans des communs** [R1-10], PAGE LUE : reclassement de 5e en 4e catégorie par la commission de sécurité, procédure de « plus de deux ans », « Plus de 100 000 euros » de travaux de conformité, propriétaire menacé de devoir « vendre le château ».
6. **Désengagement public** : collectivités 11,84 M€ (2003) → 7,82 M€ (2014) pour les MH privés [R1-03] ; en 2026, crédits d'intervention des DRAC −29 % en CP, FIP divisé par deux, compensation de 15 M€/an liée au Loto du patrimoine non reconduite [R1-34].
7. **Dépassement de devis** [R1-05] : grange classée, devis 42 000 £, facture ≈ 54 000 £ + TVA (≈ +29 %).
8. **Assurance qui explose** [R1-05] : prime d'une maison Grade I « more than doubled this year », devenue supérieure à toutes les autres charges annuelles de la maison ; « Many insurers will not offer cover at all ».
9. **Entretien sacrifié au profit de la restauration, y compris par l'État** [R1-34] : conservation préventive < 18 % des crédits de restauration en 2024 ; aile François Ier de Chambord « en état de péril », besoin de « 37 millions d'euros ».

## Points de doute / hypothèses non vérifiées

1. **Prix au m² des travaux sur MH** (couverture, pierre de taille, menuiseries, réseaux) : aucun prix vérifié. Seuls des montants globaux de chantiers ont été trouvés. Le seul ratio de toiture (≈ 500 €/m² classique contre ≈ 750 €/m² « sous prescription ABF ») vient d'un courtier, sans source.
2. **Valeur de reconstruction au m²** : 2 400 €/m² (un exemple de 2020) contre 5 000 à 10 000 €/m² (courtier 2026). Ce paramètre pilote l'entretien courant, le gros entretien, l'assurance et les imprévus, soit ≈ 87 à 95 % du total central du tableau § 9 (ESTIMATION : S1 87 %, S2 89 %, S3 95 %).
3. **Ratio de 2 à 4 %** : établi pour des parcs de bâtiments publics américains ; sa transposition à un monument est une HYPOTHÈSE. Aucun ratio français officiel trouvé.
4. **Ventilation entretien courant / gros entretien** (0,5-1 % contre le reste) : HYPOTHÈSE non sourcée.
5. **Assurance** : écart non résolu entre la formule du courtier (5 ‰) et les primes observées (≈ 2 200 €/an pour 512 m² habitables ; ≈ 7 500 €/an en moyenne pour Olhain). Possible sous-assurance des cas observés, ou barème commercial élevé.
6. **Taxe foncière** : un seul exemple (annonce de vendeur) ; dépend de la catégorie cadastrale fixée en 1970 et du taux communal. Fourchette du tableau = HYPOTHÈSE.
7. **Énergie** : aucune consommation mesurée de château ; surfaces chauffées et kWh/m² = HYPOTHÈSES. Prix 2025-2026 du fioul, des granulés et des plaquettes forestières non trouvés (sources ADEME derrière un formulaire, pages ministérielles en erreur 503).
8. **Sinistres** : chiffres du ministère vus seulement en extrait, avec une incohérence interne (67 en 2025 contre 295 sur 2013-2025).
9. **Chiffre de 40 000 €/an (Demeure Historique)** : méthode non publiée ; moyenne tous monuments confondus ; 2019.
10. **Données britanniques** : déclaratives (60 % des répondants estiment « au jugé »), échantillon de 121 propriétés, pas de surfaces ; conversion au taux BCE de 2026 appliquée à des montants 2023-2024.
11. **Durées de vie** : uniquement des sources commerciales de faible fiabilité ; le tableau paritaire suisse (ASLOCA) n'a pas pu être lu (erreur 503 à quatre reprises).
12. **Taux de subvention** : moyennes nationales (20 % / 40 %), non garanties ; sort final des crédits 2026 après vote non vérifié ; éligibilité d'un propriétaire privé au FIP non confirmée.
13. **Pages projets de la Fondation du patrimoine** : HT ou TTC non précisé ; statut de protection souvent absent.
14. **Postes techniques** (ramonage, chaudière, paratonnerre, alarme, télésurveillance) : obligations et coûts non vérifiés, sauf le contrôle de l'assainissement.
15. **Outil de lecture** : pour les pages HTML, les citations sont restituées par le modèle de synthèse de WebFetch (limitées à 125 caractères, parfois paraphrasées) ; pour les PDF, le texte a été extrait localement avec `pdftotext` et les citations sont exactes. Recommandation : revérifier les citations HTML avant toute diffusion externe.

## Chiffres clés pour le modèle

| # | Donnée | Valeur | Unité | Année | Statut | Source |
|---|---|---|---|---|---|---|
| 1 | Coût d'entretien moyen d'un monument privé, hors restauration et hors ouverture (assurance, impôts locaux, gardien, travaux minimum) | 40 000 (minimum) | €/an | 2019 | PAGE LUE | [R1-01] |
| 2 | Dépense moyenne d'entretien-réparation du bâtiment principal, maisons historiques britanniques (n = 121) | 156 067 – 160 686 | £ TTC/an | 2024 | PAGE LUE | [R1-05] |
| 3 | Retard d'entretien moyen par propriété britannique (total ; dont urgent sous 5 ans) | ≈ 1 994 000 ; ≈ 893 000 | £ | 2024 | PAGE LUE | [R1-05] |
| 4 | Budget d'entretien-réparation recommandé (parcs de bâtiments publics) | 2 – 4 | % de la valeur de remplacement par an | 1990 (cité en 2001) | PAGE LUE (+ EXTRAIT « absolute minimum ») | [R1-07], [R1-08] |
| 5 | Valeur de reconstruction d'un château | 2 400 (exemple) ; 5 000 – 10 000 (courtier) | €/m² | 2020 ; 2026 | PAGE LUE (divergence) | [R1-26] ; [R1-27] |
| 6 | Prime d'assurance | ≥ 2 500 (bien classé) ; ≈ 5 ‰ de la valeur assurée (courtier) | €/an ; ‰ | 2020 ; 2026 | PAGE LUE (fiabilité moyenne ; faible) | [R1-26] ; [R1-27] |
| 7 | Taux moyen de subvention de l'État (DRAC) | 20 (inscrit) ; 40 (classé) | % des travaux subventionnés | 2025 | PAGE LUE | [R1-34] |
| 8 | Plafond légal pour un MH inscrit (art. L.621-29) | 40 | % de la dépense effective | texte cité en 2016 | PAGE LUE | [R1-03] |
| 9 | Crédits d'intervention des DRAC (entretien et restauration des MH non État) | 112 M€ en CP, soit −29 % (−172 M€) | M€ | PLF 2026 | PAGE LUE | [R1-33], [R1-34] |
| 10 | Aide du Loto du patrimoine par site (exemples de châteaux) | 148 000 – 280 000 | € par site, une fois | 2020-2025 | PAGE LUE | [R1-12], [R1-13], [R1-16] |
| 11 | Montants de chantiers de toiture de châteaux privés (globaux) | 42 331 – 392 724 | € par opération | 2020-2026 | PAGE LUE | [R1-11] à [R1-16] |
| 12 | Prix de l'électricité (TRVE, petit consommateur, tout compris) | ≈ 238 | € TTC/MWh | août 2026 | ESTIMATION (1 072 € / 4,5 MWh, PAGE LUE) | [R1-24] |
| 13 | Prix repère du gaz | 194,90 | € TTC/MWh | nov. 2026 | PAGE LUE | [R1-25] |
| 14 | Prix des granulés en vrac ; du fioul domestique | 10,4 ; 12,6 | c€ TTC/kWh PCI | 2023 | PAGE LUE (source secondaire de l'ADEME) | [R1-22] |
| 15 | Part de passoires (F ou G) parmi les logements construits avant 1948 ; parmi les logements chauffés au fioul | 26,7 ; ≈ 42 | % | 1er janv. 2025 | PAGE LUE | [R1-21] |
| 16 | Taxe foncière : base | 50 % de la valeur locative cadastrale × taux votés | — | 2026 | PAGE LUE | [R1-30] |
| 17 | Taxe foncière d'un petit château MH (512 m² habitables) | 2 652 | €/an | non datée | PAGE LUE (déclaratif vendeur, fiabilité faible) | [R1-32] |
| 18 | Surprime catastrophes naturelles | 12 → 20 | % de la prime dommages | depuis le 1er janv. 2025 | PAGE LUE (courtier citant l'arrêté) | [R1-29] |
| 19 | Sinistres recensés dans les MH (dont incendies) | 67 (16) | sinistres/an | 2025 | EXTRAIT | [R1-35] |
| 20 | Subvention : validité de la décision ; délai de liquidation ; avance maximale | 2 ans ; 4 ans ; 30 % | — | règles citées en 2016 | PAGE LUE | [R1-03] |
| 21 | **Budget annuel du bâti S1** (basse – centrale – haute) | 86 100 – 195 200 – 354 400 | € TTC/an | 2026 | ESTIMATION (§ 9) | calcul R1 |
| 22 | **Budget annuel du bâti S2** | 230 100 – 518 600 – 936 800 | € TTC/an | 2026 | ESTIMATION (§ 9) | calcul R1 |
| 23 | **Budget annuel du bâti S3** | 903 800 – 1 978 400 – 3 523 100 | € TTC/an | 2026 | ESTIMATION (§ 9) | calcul R1 |
| 24 | Part du gros entretien dans le budget du bâti (central) | 51 – 55 | % | 2026 | ESTIMATION (§ 9) | calcul R1 |
