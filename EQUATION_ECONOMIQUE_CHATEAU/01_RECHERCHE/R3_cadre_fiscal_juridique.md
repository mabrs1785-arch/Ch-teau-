# R3 — Cadre fiscal et juridique

Agent : R3. Démarré le 2026-10-14. Fichier écrit au fur et à mesure.
Sources : `01_RECHERCHE/sources/sources_R3.csv` (identifiants [R3-xx]).

Avertissement général : ce document n'est pas un avis juridique. Les règles sont citées d'après des sources officielles lisibles (BOFiP, service-public.fr, impots.gouv.fr, etc.). Légifrance renvoie 403 : les articles de loi sont cités d'après leur reproduction dans ces sources. Tout point marqué « À VALIDER » doit être confirmé par un avocat fiscaliste, un notaire ou un expert-comptable.

Statuts : PAGE LUE (page ouverte avec WebFetch, citation exacte) / EXTRAIT (vu dans un résultat de recherche) / ESTIMATION / HYPOTHÈSE / INCONNU.

## Journal de progression

- 2026-10-14 : squelette créé.
- 2026-10-14 : Q1 à Q10 rédigées ; synthèses, matrice, points à valider, contre-exemples, points de doute et chiffres clés ajoutés. 15 WebSearch utilisées sur 15 ; environ 117 WebFetch, dont une vingtaine en échec (403, 404, 503, maintenance, captcha). 63 sources : 58 pages lues, 5 extraits. Sites en erreur pendant la mission : legifrance (403), impots.gouv.fr (maintenance), ecologie.gouv.fr, associations.gouv.fr, senat.fr, préfectures (503), ADEME et DREAL (403).

## Q1. Régime fiscal des monuments historiques (propriétaire privé)

### 1.1 Base légale et principe

- Base : CGI art. 156 (I-3° et II-1° ter), art. 156 bis ; annexe III art. 41 E à 41 J ; annexe IV art. 17 ter (conditions d'ouverture). La présentation générale du BOFiP renvoie aux articles 41 F, 41 G, 41 I et 41 I bis de l'annexe III [R3-07]. PAGE LUE.
- Trois situations distinguées par le BOFiP [R3-07] (PAGE LUE) : déduction du revenu global « lorsque l'immeuble ne lui procure aucune recette » ; déduction du revenu foncier « lorsque celui-ci donne lieu à la perception de recettes imposables et qu'il n'est pas occupé par le propriétaire » ; régime mixte quand l'immeuble « est occupé en partie par son propriétaire ».
- Exclusion importante [R3-04 § 40, R3-07 § 40] (PAGE LUE, citation exacte du texte extrait du PDF) : « Le dispositif ne concerne pas les immeubles ou parties d'immeubles utilisées par leurs propriétaires pour les besoins d'une entreprise industrielle, commerciale, artisanale, agricole ou pour l'exercice d'une profession non commerciale ». **Conséquence pour le modèle** : les parties du château affectées à une activité d'entreprise (hôtel, salle de réception exploitée en BIC, écurie agricole) sortent du régime MH des revenus fonciers et relèvent des règles des revenus professionnels.
- Champ : « À compter de l'imposition des revenus de l'année 2014, seuls les immeubles classés ou inscrits au titre des monuments historiques ou labellisés "Fondation du patrimoine" peuvent bénéficier des modalités dérogatoires » [R3-04 § 15]. PAGE LUE. Les anciens immeubles « agréés » n'en bénéficient plus.
- Classement partiel : le régime s'applique à l'ensemble de l'immeuble si la protection « vise la protection de l'ensemble architectural » et n'est pas « limité à des éléments isolés ou dissociables de l'ensemble immobilier, tels un escalier, des plafonds ou certaines salles » (RM Klifa 1997, CE 5 février 2009 n° 303425) [R3-04 § 80-90]. PAGE LUE.

### 1.2 Taux de déduction selon la situation (tableau synthétique BOFiP [R3-02], PAGE LUE)

| Situation | Règle (citation exacte ou fidèle) | Statut |
|---|---|---|
| Immeuble ne procurant aucune recette (habité par le propriétaire, fermé ou ouvert gratuitement) | Travaux subventionnés : 100 % nets de subvention ; autres dépenses : « déduction de 100 % lorsque l'immeuble est ouvert au public et de 50 % dans le cas contraire » ; pas de report de l'excédent | PAGE LUE [R3-02], confirmé [R3-05 § 130 : « la totalité du montant des dépenses concernées est déductible si le public est admis à visiter » / « la déduction est limitée à 50 % de ce montant si l'immeuble est fermé au public »] |
| Idem : excédent | « cet excédent ne peut pas dégager un déficit reportable sur le revenu global des années suivantes » [R3-05 § 1] | PAGE LUE |
| Idem : travaux subventionnés | réfaction « dont le taux est égal à celui de la subvention, quelle que soit la date de versement de celle-ci » [R3-05 § 120] | PAGE LUE |
| Idem : charges admises | réparation, entretien, amélioration ; « les impositions autres que celles incombant à l'occupant » ; « les intérêts de dettes contractées pour la conservation, l'acquisition, la réparation ou l'amélioration des propriétés » ; « les primes d'assurance afférentes aux monuments historiques » [R3-05 § 50] | PAGE LUE |
| Immeuble procurant des recettes, non occupé (loué en totalité ou ouvert à la visite payante sans usage privé) | Charges réelles ; « Déficit foncier imputable sans limitation sur le revenu global » ; excédent reportable sur le revenu global « des six années suivantes inclusivement » [R3-02, R3-04 § 10] | PAGE LUE |
| Immeuble procurant des recettes et occupé par le propriétaire (cas type d'un château habité et ouvert à la visite payante) | Charges liées aux visites et travaux subventionnés : 100 % ; autres charges foncières : « à titre de règle pratique 75 % des charges » en revenus fonciers ; partie privée : « (à titre de règle pratique, 25 % des charges) » déductibles du revenu global ; « Déficit foncier imputable sans limitation sur le revenu global » [R3-02] | PAGE LUE |
| Abattement forfaitaire pour frais de visite | « 1 525 € lorsque l'immeuble ne comprend ni parc, ni jardin ouvert au public ; 2 290 € dans le cas contraire. » Abattement « pratiqué sur le montant brut des recettes » ; option pour les frais réels possible, mais le régime ne peut être invoqué « pour prétendre que la visite de la propriété se traduit par un résultat déficitaire » [R3-04 § 120-130] | PAGE LUE |

Nature des recettes : les droits d'entrée et les subventions de travaux sont des recettes de **revenus fonciers** (déclaration 2044-SPE, « recettes brutes diverses ») [R3-04 § 60, 170, 220]. Les dons reçus de la Fondation du patrimoine pour des travaux sont aussi ajoutés aux recettes de l'année de perception [R3-04 § 60]. PAGE LUE.

Conditions d'ouverture au public (annexe IV, art. 17 ter, reproduit au BOFiP [R3-04 § 105], PAGE LUE, citation exacte) :
« sont réputés ouverts à la visite, les immeubles que le public est admis à visiter au moins : - soit cinquante jours par an, dont vingt-cinq jours non ouvrables, au cours des mois d'avril à septembre inclus ; - soit quarante jours pendant les mois de juillet, août et septembre. » Réduction possible « dans la limite de 10 jours par année civile » en cas de conventions de visites scolaires ou étudiantes de groupes d'« au moins vingt participants ». « Un jour d'ouverture doit compter l'accès effectif et immédiat du public aux biens en cause pendant au moins six heures. »

Bâches publicitaires sur échafaudage (C. patrimoine L. 621-29-8) : les recettes sont des revenus fonciers ; « depuis le 1er octobre 2007, les propriétaires de monuments historiques peuvent utiliser les bâches d'échafaudage installées lors de la réalisation de travaux de restauration comme espace publicitaire » [R3-04 § 190-200]. PAGE LUE. (Recette ponctuelle liée aux chantiers.)

### 1.3 Conditions de l'article 156 bis : conservation 15 ans, détention directe, copropriété [R3-06], PAGE LUE

- Engagement de conservation « pendant une période d'au moins quinze années à compter de leur acquisition » (§ 10), applicable « depuis l'imposition des revenus de l'année 2009 » (§ 1).
- Rupture : le revenu de l'année de rupture et des deux années suivantes « est majoré du tiers du montant des charges indûment imputées » (§ 100) ; exceptions : licenciement, invalidité, décès, donation avec reprise de l'engagement (§ 170-200).
- Détention par une société civile non soumise à l'IS : immeubles acquis à compter du 1er janvier 2009 « en principe exclus » (§ 230). Exceptions : SCI dont les associés sont « membres d'une même famille » (§ 280 ; parents en ligne directe, frères et sœurs, conjoints, enfants, § 290) ; immeuble classé affecté à « un espace culturel non commercial ouvert au public » pendant 15 ans (§ 300-340) ; depuis 2018, immeuble affecté à l'habitation pour au moins 75 % de ses surfaces habitables (§ 360-400, hors immeubles labellisés). Les associés conservent leurs parts 15 ans (§ 250, § 420).
- Copropriété : régime « pas ouvert aux immeubles ayant fait l'objet d'une division à compter du 1er janvier 2009 » sauf exceptions (agrément 2009-2017 ; affectation à l'habitation ≥ 75 % depuis 2018) (§ 460-550).
- Sociétés à l'IS : la doctrine ne vise que les sociétés civiles non soumises à l'IS [R3-06]. **Un château détenu par une société à l'IS n'entre pas dans ce régime de revenus fonciers** (déduction et amortissement selon les règles de l'IS). ESTIMATION fondée sur [R3-06] et [R3-04 § 40] ; À VALIDER par un fiscaliste.

### 1.4 Label de la Fondation du patrimoine (immeubles non protégés)

- Biens éligibles (site de la Fondation [R3-08], PAGE LUE) : biens de « propriétaires privés d'un site bâti ou non-bâti (parcs ou jardins) » ne relevant pas du régime MH ; « Visible de la voie publique ou rendu accessible au public » ; situé en zone rurale, bourg ou petite ville de « moins de 20 000 habitants », en site patrimonial remarquable (SPR) ou en site classé. Avis de l'architecte des Bâtiments de France (UDAP). Label « accordé pour une durée de 3 ans ». Aide « 2 à 20 % » (Fondation et collectivités partenaires).
- Taux de déduction (BOFiP [R3-02], [R3-05], PAGE LUE) : immeuble labellisé non ouvert : « déduction de 50 % des dépenses d'entretien et de réparation non subventionnées, portée à 100 % si la subvention couvre au moins 20 % de leur montant » (formulation du tableau, citée fidèlement). Pour les immeubles labellisés, les intérêts d'emprunt et les primes d'assurance ne sont pas déductibles [R3-05 § 160-230] (PAGE LUE, reformulation : citation exacte non obtenue). L'ouverture au public n'est pas exigée : « Il n'est pas en revanche exigé qu'il soit ouvert au public. » [R3-03 § 190].
- Le site de la Fondation indique « 50 à 100 % » du montant des travaux « déduit de votre revenu global imposable ou de vos revenus fonciers » [R3-08].
- Effet pour S1 (château non protégé) : seule voie de déduction des travaux sur le revenu global ; limitée aux travaux sur les parties extérieures visibles du label (à vérifier dans la doctrine : BOI-RFPI-SPEC-30-10 § 170 et suivants). À VALIDER.

### 1.5 Lois de finances 2024, 2025, 2026 : changements sur le régime MH

- Je n'ai trouvé **aucune modification** du régime de déduction MH (art. 156 et 156 bis) dans les lois de finances 2024, 2025 ou 2026. Les pages BOFiP du régime (BOI-RFPI-SPEC-30, -30-10, -30-20-10, -30-20-20, -30-30) sont toutes datées du 19/12/2018 et présentées comme versions en vigueur au 14/10/2026 [R3-03 à R3-07]. Statut : ESTIMATION (absence de mise à jour BOFiP ≠ preuve d'absence de changement législatif). À VÉRIFIER sur Légifrance (articles 156 et 156 bis CGI, version en vigueur) ou par un fiscaliste.
- PLF 2026 : un amendement visant à exonérer d'IFI et de taxe foncière les MH ouverts au public a été déposé à l'Assemblée et apparaît « Rejeté » dans un résultat de recherche [R3-12] (EXTRAIT).
- Crédits publics : selon la synthèse de l'avis du Sénat sur le PLF 2026 vue en résultat de recherche, baisse des crédits des monuments historiques de 209 M€ en autorisations d'engagement (-34 %) et de 114 M€ en crédits de paiement (-21 %) [R3-11] (EXTRAIT, à confirmer en ouvrant le PDF ; sujet traité par R1).

## Q2. Transmission : exonération de droits de mutation à titre gratuit (CGI art. 795 A)

Source principale : BOFiP BOI-ENR-DMTG-10-20-30-60, version en vigueur depuis le 06/11/2025 [R3-13] (PAGE LUE).

- Champ : immeubles « pour l'essentiel » classés ou inscrits, et meubles « qui en constituent le complément historique ou artistique » (§ 30). Exonération « applicable, sous conditions, aux parts de sociétés civiles représentatives de ces biens » (renvoi au BOI-ENR-DMTG-10-20-30-70, non lu).
- Convention « à durée indéterminée » avec l'État (ministres de la culture et des finances) prévoyant « le maintien dans l'immeuble des meubles et immeubles par destination exonérés », les modalités d'accès du public et les « conditions d'entretien des biens exonérés » (§ 90). La convention peut limiter « l'ouverture des lieux au public au parc entourant l'immeuble » (§ 45).
- Ouverture : depuis le décret n° 2023-103 du 16 février 2023, la convention type « aligne les conditions d'ouverture au public des monuments historiques » sur l'article 17 ter de l'annexe IV (50 jours dont 25 non ouvrables d'avril à septembre, ou 40 jours en juillet-août-septembre, 6 heures par jour) [R3-14] (PAGE LUE) et [R3-04 § 105].
- Procédure : la convention est « assimilée à un agrément fiscal » car c'est « une autorisation préalable donnée par l'administration » ; recouvrement différé « jusqu'à ce qu'il soit statué sur la demande de convention » ; droits exigibles si la demande est rejetée ou si la convention n'est pas déposée dans le délai d'un mois (§ 240, 260) [R3-13]. Note : selon deux décisions du Conseil d'État du 11 février 2022, la demande de convention n'est pas une demande d'agrément au sens de l'article 1649 nonies du CGI [R3-14].
- Sanction : en cas de manquement, les biens sont soumis aux droits sur « leur valeur au jour où la convention n'est pas respectée » (§ 290), avec intérêt de retard de l'article 1727 (§ 320) [R3-13].
- Effet chiffré : l'exonération porte sur 100 % de la valeur des biens couverts. ESTIMATION à partir de [R3-13] : pour un château transmis en ligne directe, l'économie est égale aux droits qui auraient été dus (barème progressif jusqu'à 45 %, non vérifié ici). Le coût est perpétuel : ouverture au public 50 jours/an et maintien du mobilier, ce qui pèse sur la tranquillité de la résidence privée.
- Usage commercial : la page ne traite pas des immeubles exploités commercialement (hôtel, réception). INCONNU ; à vérifier avec un notaire.

## Q3. IFI

- Seuil : assujettissement si la « valeur nette taxable » du patrimoine immobilier non professionnel est « supérieure à 1 300 000 € » au 1er janvier 2026 [R3-01] (PAGE LUE, page vérifiée le 06/03/2026).
- Barème 2026 [R3-15] (PAGE LUE) : 0 % jusqu'à 800 000 € ; 0,50 % de 800 001 à 1 300 000 € ; 0,70 % de 1 300 001 à 2 570 000 € ; 1 % de 2 570 001 à 5 000 000 € ; 1,25 % de 5 000 001 à 10 000 000 € ; 1,50 % au-delà. Décote entre 1,3 et 1,4 M€ : « 17 500 € - 1,25 % de la valeur nette taxable du patrimoine ». Réduction pour dons : 75 % des dons, plafond 50 000 €.
- **Monuments historiques : pas d'exonération.** La liste des biens à déclarer comprend les « Bâtiments classés monument historique » [R3-01] (PAGE LUE). Un amendement PLF 2026 d'exonération des MH ouverts au public a été rejeté [R3-12] (EXTRAIT).
- Résidence principale : abattement de 30 % sur sa valeur [R3-01] (PAGE LUE).
- Biens professionnels : « des exonérations partielles ou totales sont prévues pour les biens utilisés pour une activité professionnelle, sous conditions » ; « L'immobilier affecté à l'activité opérationnelle d'une société est exclu de l'assiette de l'IFI » [R3-01] (PAGE LUE). Détention indirecte : immobilier non pris en compte si le contribuable détient « moins de 10 % du capital » (sous d'autres conditions) [R3-01].
- Bois et forêts : exonération sous conditions lorsqu'ils sont « sous engagement d'exploitation ou à usage professionnel » ; biens ruraux : exonération partielle ou totale s'ils sont loués à long terme ou à usage professionnel [R3-01] (PAGE LUE). Les quotités exactes (3/4 de la valeur ; plafond pour les biens ruraux loués) ne figurent pas sur la page lue : INCONNU ici, à vérifier dans le BOFiP (série BOI-PAT-IFI-20-20) ou CGI art. 975-976.
- Château partiellement loué à une société d'exploitation : voir 3.1 ci-dessous.

### 3.1 Exemple chiffré (ESTIMATION, barème [R3-15])

Hypothèse : patrimoine immobilier taxable net = 5 M€ (château non résidence principale, pas de dette). IFI = 0,5 % × 500 000 + 0,7 % × 1 270 000 + 1 % × 2 430 000 = 2 500 + 8 890 + 24 300 = **35 690 €/an**. Si le château est la résidence principale (abattement 30 %, base 3,5 M€) : 2 500 + 8 890 + 1 % × 930 000 = **20 690 €/an**. Pour 10 M€ (S3, hors RP) : 35 690 + 1,25 % × 5 000 000 = **98 190 €/an**. Ces montants sont payés sur la fortune personnelle du propriétaire et doivent être couverts par le système économique s'il doit être autonome. ESTIMATION ; valeurs vénales = HYPOTHÈSES.

### 3.2 Château partiellement affecté à une société d'exploitation

- Règle lue : l'immobilier affecté à l'activité opérationnelle d'une société est exclu de l'assiette [R3-01]. Pour un immeuble détenu en direct et loué à la société d'exploitation du propriétaire, la qualification de bien professionnel dépend des conditions de l'article 975 CGI (fonctions de direction, activité principale, part détenue). INCONNU dans le détail ; À VALIDER par un fiscaliste. Hypothèse prudente pour le modèle : la partie louée reste taxable à l'IFI si le propriétaire n'exerce pas dans la société son activité professionnelle principale.

## Q4. Mécénat

### 4.1 Un MH privé peut-il recevoir des dons défiscalisés ? Oui, via la Fondation du patrimoine, sous conditions strictes

Source : BOFiP BOI-IR-RICI-250-10-20-30, version en vigueur depuis le 12/09/2012 [R3-10] (PAGE LUE). Le texte légal (CGI art. 200 et 238 bis ; C. patrimoine L. 143-2-1) n'a pas pu être lu sur Légifrance : vérifier qu'il n'a pas changé depuis 2012.
- Immeubles éligibles : « classés ou inscrits au titre des monuments historiques ou ayant reçu le label de la Fondation du patrimoine » (n° 200).
- Propriétaires : « Seuls les immeubles détenus en totalité par des personnes physiques » (n° 160) ; sociétés civiles admises seulement si elles ne comprennent que des personnes physiques et ont pour objet exclusif la gestion ou la location nue (n° 180) ; « Sont dès lors exclues toutes les sociétés commerciales » (n° 180).
- **Exploitation commerciale** : principe d'exclusion des immeubles procurant des recettes commerciales (n° 290) ; exception : « la visite payante du monument ne permet pas de considérer que l'immeuble fait l'objet d'une exploitation commerciale » (n° 300) ; autres activités tolérées si les recettes « n'excèdent pas 60 000 euros » HT sur l'année civile précédant le versement (n° 310) ; immeubles classés ou inscrits « utilisés par leurs propriétaires pour les besoins d'une entreprise agricole » admis (n° 290).
- Engagements (C. patrimoine L. 143-2-1, III) : « L'immeuble doit être conservé pendant au moins dix ans à compter de la date d'achèvement des travaux » (n° 430) ; parties protégées ouvertes au public pendant au moins dix ans (50 jours/an ou 40 jours en juillet-septembre), ou visibles depuis la voie publique (n° 450). Non applicables aux immeubles labellisés (n° 420).
- Donateur : ni le propriétaire, ni un parent en ligne directe ou collatéral, ni un donateur ayant lui-même conclu une telle convention pour son propre immeuble (n° 10).
- Avantage du donateur : IR « 66 % du montant des sommes versées dans la limite de 20 % du revenu imposable » ; entreprises 60 % (art. 238 bis) (n° 20). Selon la Fondation : 66 % IR, 60 % IS, 75 % IFI [R3-09] (PAGE LUE).
- Frais de la Fondation du patrimoine : 6 % des dons collectés ; 94 % vont aux travaux [R3-09] (PAGE LUE).
- Traitement chez le propriétaire : les dons reçus de la Fondation du patrimoine pour des travaux sont ajoutés aux recettes foncières de l'année de perception [R3-04 § 60] (PAGE LUE).
- **Conséquence pour le modèle** : si le domaine dégage plus de 60 000 € HT/an de recettes commerciales (réceptions, hébergement) ou si le château appartient à une société commerciale, la collecte défiscalisée via la Fondation est fermée (doctrine 2012, À VÉRIFIER sur le texte actuel de l'article 200 CGI). Les dons financent des travaux précis, pas le fonctionnement.

### 4.2 Fonds de dotation et avantage privé

- Pour ouvrir droit à réduction d'impôt, l'organisme doit être d'intérêt général : pas d'activité lucrative, pas de « gestion intéressée », pas de fonctionnement « au profit d'un cercle restreint de personnes » ; définition : « Un organisme fonctionne au profit d'un cercle restreint de personnes lorsqu'il poursuit des intérêts particuliers d'une ou plusieurs personnes clairement individualisables. » [R3-43 § 90, § 130] (PAGE LUE). « tous les versements faits directement à un particulier ou à une entreprise industrielle ou commerciale sont exclus » (§ 80).
- **Application (ESTIMATION, à valider par un avocat)** : un fonds de dotation qui porterait le château tout en logeant gratuitement son fondateur poursuivrait les intérêts particuliers d'une personne « clairement individualisable » : les dons perdraient leur caractère déductible et le fonds s'exposerait à une remise en cause. Un loyer de marché payé par le fondateur pour sa partie privée, une ouverture réelle au public et une gouvernance indépendante seraient des conditions minimales. La page associations.gouv.fr n'a pas pu être lue (erreur 503), mais la fiche service-public « Fonds de dotation » (vérifiée le 18/06/2025) l'a été [R3-58] (PAGE LUE) : « un organisme de mécénat » destiné à une œuvre ou mission d'intérêt général ; « une dotation initiale d'au moins 15 000 € » ; il « ne peut pas percevoir de subventions publiques » ; ressources : « Revenus de sa dotation », produits d'activités autorisées par les statuts, rétributions pour service rendu, appel à la générosité publique sur autorisation préfectorale ; commissaire aux comptes au-delà de 10 000 € de ressources ; comité consultatif au-delà de 1 000 000 € de dotation ; suspension possible par le préfet. La fiche ne dit rien sur l'immobilier ni sur l'avantage du fondateur. **Conséquence (ESTIMATION)** : un fonds de dotation ne peut pas recevoir de subventions publiques de travaux (DRAC, région) ; il peut porter un monument ouvert au public, mais l'usage privé par le fondateur est incompatible avec l'intérêt général sans loyer de marché ; À VALIDER par un avocat spécialisé.

### 4.3 Mécénat d'entreprise [R3-42] (PAGE LUE, vérifiée le 20/07/2026)

- Réduction d'impôt : 60 % du don jusqu'à 2 000 000 €, 40 % au-delà. Plafond : 20 000 € ou 5 ‰ du chiffre d'affaires HT si ce montant est plus élevé ; excédent reportable sur 5 exercices.
- Bénéficiaires : organismes d'intérêt général dont l'activité ne profite pas à « un cercle restreint » ; la Fondation du patrimoine figure dans la liste. Mécénat « sans aucune contrepartie » ; à distinguer du parrainage (contrepartie publicitaire, charge déductible).
- **Conséquence** : une entreprise ne peut pas faire un don défiscalisé directement au propriétaire privé ou à sa société d'exploitation ; seulement via la Fondation du patrimoine (conditions 4.1) ou un organisme d'intérêt général. Le parrainage d'événements (concours équestre) reste possible comme prestation commerciale (TVA 20 %).

## Q5. Fiscalité des activités et des structures (LF 2026, PFU, holdings, IS, meublés, SCI, mère-fille)

### 5.1 Loi de finances pour 2026

- Loi n° 2026-103 du 19 février 2026, publiée au JO du 20 février 2026, après une loi spéciale et l'engagement de la responsabilité du gouvernement ; décision du Conseil constitutionnel n° 2026-901 DC du 19 février 2026 [R3-18] (PAGE LUE, PDF de cabinet d'avocats, texte extrait). À confirmer sur Légifrance (bloqué ici).
- Mesures non adoptées citées : abattement forfaitaire des retraites, accélération de la suppression de la CVAE, ajustement de la franchise en base de TVA, « qui est finalement maintenu » [R3-18].
- Autres mesures citées utiles au projet : prorogation de la « contribution différentielle sur les hauts revenus » (taux effectif minimal de 20 % au-delà de 250 000 € de revenu fiscal de référence ajusté pour un célibataire, 500 000 € pour un couple) jusqu'au retour du déficit public à 3 % du PIB (art. 2) ; barème de l'IR revalorisé de 0,9 % (art. 4) ; Pacte Dutreil : les « biens somptuaires » de la société transmise ne sont plus exonérés sauf affectation exclusive à une activité opérationnelle, engagement individuel porté « de 4 à 6 ans » pour les transmissions dès le 21 février 2026 (art. 8) ; nouveau « statut du bailleur privé » (amortissement de 3,5 % ou 3 % sur 80 % du prix, location nue en résidence principale, acquisitions du 21/02/2026 au 31/12/2028) (art. 47) ; « réduction d'impôt en cas de participation à la restauration du château de Chambord » (art. 30) ; « ajustements des dispositifs de soutien au secteur agricole » (art. 31 à 36, contenu non détaillé) [R3-18] (PAGE LUE).
- Rien dans [R3-18] ni [R3-19] sur le régime MH, l'IFI (hors articulation avec la taxe holdings), la TVA équestre ou les meublés de tourisme. Le projet d'« impôt sur la fortune improductive » discuté à l'automne 2025 n'apparaît pas dans ces synthèses de la loi définitive : ESTIMATION « non adopté », À VÉRIFIER.

### 5.2 Taxe sur les actifs non professionnels des holdings patrimoniales (LF 2026, art. 7 ; CGI art. 235 ter C selon des extraits de recherche)

Sources : [R3-18] et [R3-19] (PAGE LUE). Le numéro d'article du CGI (235 ter C) n'apparaît que dans des résultats de recherche (EXTRAIT).
- Taux : « 20 % » (contre 2 % dans le projet initial) [R3-18].
- Sociétés visées : holdings à l'IS (de plein droit ou sur option) avec siège en France, ou holdings étrangères dont un associé personne physique est domicilié en France. Trois conditions cumulatives à la clôture : « La valeur vénale des actifs qu'elles détiennent doit être supérieure ou égale à 5 M€ » ; une personne physique détient au moins 50 % des droits (ou exerce en fait le pouvoir de décision) ; « revenus passifs correspondant à plus de 50 % du montant cumulé des produits d'exploitation et des produits financiers » [R3-18].
- Assiette (biens non affectés à une activité opérationnelle) : « les biens affectés à l'exercice de la chasse et de la pêche ; les véhicules qui ne sont pas affectés à une activité professionnelle [...] ; les bijoux et métaux précieux, sauf s'ils sont exposés ; **les chevaux de courses ou de concours** ; les vins et les autres alcools ; et **les logements dont une personne physique associée se réserve la jouissance** » [R3-18]. Précision [R3-19] : logements « occupés, à titre gratuit ou pour un loyer inférieur au prix du marché, à titre de résidence principale ou non » et « logements loués fictivement » ; bijoux exclus s'ils sont « affectés à l'exploitation d'un musée ou d'un monument historique ou exposés dans un lieu accessible au public ».
- Articulation : mécanisme anti-double imposition avec l'IFI pour les biens immobiliers ; taxe « pas déductible de l'assiette de l'impôt sur les sociétés » [R3-18].
- Entrée en vigueur : « exercices clos à compter du 31 décembre 2026 » [R3-18].
- **Conséquence pour le projet (ESTIMATION, à valider)** : loger le propriétaire gratuitement ou sous le prix du marché dans un château détenu par une holding patrimoniale à l'IS (actifs ≥ 5 M€, revenus majoritairement passifs) exposerait la société à 20 % par an de la valeur vénale du logement, et à 20 % de la valeur de chevaux de concours non affectés à une activité opérationnelle. Une société d'exploitation réellement active (revenus d'exploitation > 50 %) n'est pas visée. Le schéma « holding patrimoniale qui détient le château et loge le propriétaire » est donc à proscrire ou à faire valider.

### 5.3 PFU et prélèvements sociaux 2026

- LFSS 2026 : loi n° 2025-1403 du 30 décembre 2025, « Article 12 (hausse de la CSG) » [R3-16] (PAGE LUE, service-public vérifié le 30/06/2026).
- Revenus de placement (dont dividendes) 2026 : CSG 10,6 %, CRDS 0,5 %, prélèvement de solidarité 7,5 %, total **18,6 %** (17,2 % pour les revenus de 2025) [R3-16].
- Revenus fonciers et plus-values immobilières : total **17,2 %** (CSG 9,2 %) ; assurance-vie : 17,2 % [R3-16].
- PFU : « au taux de 31,4 % (ou de 30 %) » [R3-16] ; la fiche « Revenus du dirigeant d'une société » précise : « à un taux global de 31,4 %, c'est-à-dire 12,8 % au titre de l'impôt sur le revenu et 18,6 % de prélèvements sociaux. » [R3-57] (PAGE LUE).
- Que Choisir [R3-17] (PAGE LUE) : « Sont notamment visés par cette hausse les dividendes et distributions assimilées » ; « la loi exclut les revenus fonciers perçus par les propriétaires qui donnent en location des biens non meublés » ; pour les revenus du patrimoine (plus-values mobilières, LMNP), l'augmentation « concerne les revenus perçus dès 2025 ». **Divergence** : la page service-public ne mentionne pas de taux spécifique 2025 pour les revenus du patrimoine. À vérifier.
- Conséquence : 1 € de bénéfice d'une société à l'IS distribué au propriétaire en 2026 = 1 × (1 − 25 %) × (1 − 31,4 %) = **0,514 €** net (taux normal d'IS) ou (1 − 15 %) × (1 − 31,4 %) = 0,583 € (taux réduit). ESTIMATION arithmétique ; taux d'IS à confirmer (voir 5.4).

### 5.4 Impôt sur les sociétés

- Taux normal : « imposée au taux normal de 25 % » [R3-20] (PAGE LUE, vérifiée le 17/02/2026).
- Taux réduit de 15 % jusqu'à 42 500 € de bénéfice, si chiffre d'affaires ≤ 10 000 000 € et capital entièrement libéré et détenu à 75 % au moins par des personnes physiques (directement ou via une société elle-même détenue à 75 % par des personnes physiques) [R3-20] (PAGE LUE).
- Contribution sociale de 3,3 % : non mentionnée sur la page lue ; INCONNU ici (concerne seulement les grandes entreprises, à vérifier).

### 5.5 Meublés de tourisme, LMNP, chambres d'hôtes (loi Le Meur, LF 2025, LF 2026)

Loi n° 2024-1039 du 19 novembre 2024 « visant à renforcer les outils de régulation des meublés de tourisme à l'échelle locale » (dite loi Le Meur), JO du 20/11/2024 [R3-34] (PAGE LUE).

Seuils et abattements du micro-BIC (recettes HT) [R3-31], [R3-33], [R3-36] (PAGE LUE) :

| Activité | Revenus 2024 (ancien régime) | Revenus 2025 | Revenus 2026 |
|---|---|---|---|
| Meublé de tourisme non classé | 77 700 € / 50 % | **15 000 € / 30 %** | 15 000 € / 30 % |
| Meublé de tourisme classé | 188 700 € / 71 % | **77 700 € / 50 %** | **83 600 € / 50 %** |
| Chambre d'hôtes | 188 700 € / 71 % | 77 700 € / 50 % | 83 600 € / 50 % |
| Location meublée longue durée | 77 700 € / 50 % | 77 700 € / 50 % | 83 600 € / 50 % |
| Vente de marchandises, hébergement hors meublés de tourisme (hôtellerie) | — | 188 700 € / 71 % | 203 100 € / 71 % |
| Prestations de services BIC | — | 77 700 € / 50 % | 83 600 € / 50 % |

Remarques : abattement minimal de 305 € ; le loueur classé qui dépasse 77 700 € deux années consécutives passe au réel [R3-31] ; une année de tolérance en cas de premier dépassement [R3-36].

Autres règles lues :
- Régime réel LMNP : amortissement du logement et des meubles ; « le déficit s'impute sur les revenus de location meublée non professionnelle de la même année et des 10 années suivantes », pas sur le revenu global (sauf LMP) [R3-36] (reformulation fidèle).
- LMP : recettes du foyer > 23 000 € et supérieures aux autres revenus d'activité ; exonération de plus-value si recettes < 90 000 € HT et activité depuis 5 ans au moins (partielle entre 90 000 et 126 000 € HT ; 250 000 / 350 000 € HT pour la para-hôtellerie) [R3-32] (PAGE LUE).
- LF 2025 : pour les ventes réalisées depuis le 15 février 2025, les amortissements déduits en LMNP sont réintégrés dans le calcul de la plus-value, « sous certaines conditions » (exceptions non détaillées sur la page) [R3-37] (PAGE LUE, reformulation). Plus-value immobilière des particuliers : IR 19 % (exonération après 22 ans), prélèvements sociaux 17,2 % (exonération après 30 ans) [R3-37].
- Prélèvements sociaux sur les revenus LMNP : 18,6 % selon la logique de la LFSS 2026 (revenus du patrimoine hors revenus fonciers) [R3-16], [R3-17] ; la page F32744 ne donne pas le taux. ESTIMATION.
- Cotisations sociales : meublés de tourisme, cotisations Urssaf si les recettes de courte durée dépassent 23 000 € ; chambres d'hôtes, cotisations si le revenu imposable dépasse 13 % du PASS, « 6 123 € en 2025 » selon [R3-31] et « 6 248 € de revenus imposables en 2025 » selon [R3-35]. **Divergence non résolue** (6 248 € correspond probablement à 13 % du PASS 2026 : ESTIMATION).
- Le Meur, autres règles [R3-34] : DPE obligatoire pour les logements nouvellement proposés en meublé de tourisme soumis à changement d'usage ; « Depuis le 1er janvier 2025, les logements classés en catégorie G ne sont plus autorisés à la location » ; F exclus en 2028, seuls A à D en 2034 ; amendes jusqu'à 10 000 € (défaut d'enregistrement) et 20 000 € (fausse déclaration) ; résidences principales limitables à 90 jours ; quotas possibles. **Risque spécifique château** : des dépendances anciennes mal isolées converties en gîtes peuvent tomber sous l'interdiction DPE G puis F. ESTIMATION ; à vérifier logement par logement.

Chambres d'hôtes [R3-35] (PAGE LUE, vérifiée le 21/05/2026) :
- Définition : « chambre meublée chez l'habitant en vue d'accueillir des touristes à titre onéreux », petit-déjeuner compris ; « La capacité d'accueil ne doit pas dépasser 5 chambres ou 15 clients simultanément. »
- Au-delà : l'appellation ne peut plus être utilisée et il faut suivre « la réglementation des établissements recevant du public (ERP) ».
- Déclaration en mairie (cerfa n° 13566) ; activité « considérée comme une activité commerciale, quel que soit le montant des revenus générés » ; immatriculation ; micro-BIC à 50 %. Table d'hôtes facultative, menu unique, réservée aux occupants des chambres.
- Fiscalité : BIC ; seuils micro du tableau ci-dessus. TVA : régime de l'hébergement (franchise 85 000 € ; au-delà, 10 % si prestations para-hôtelières) [R3-24], [R3-27]. ESTIMATION pour l'application aux chambres d'hôtes.

### 5.6 SCI [R3-59] (PAGE LUE, vérifiée le 07/10/2025)

- Par défaut, la SCI relève de l'impôt sur le revenu : « Les bénéfices réalisés par la société ... sont imposés au nom personnel de chaque associé ».
- Option pour l'IS : « À l'expiration de ce délai, l'option est irrévocable. » ; à l'IS, les travaux d'amélioration sont amortissables ; le passage à l'IS entraîne en principe « l'imposition immédiate des bénéfices non encore taxés et des plus-values non encore imposées ».
- Activité commerciale : « au-delà de 10 % du chiffre d'affaires hors taxes, l'activité commerciale n'est plus accessoire » et la SCI devient passible de l'IS. **Conséquence** : une SCI à l'IR qui porte le château ne doit pas exploiter elle-même réceptions, gîtes ou hébergement au-delà de 10 % de son chiffre d'affaires HT ; l'exploitation doit être logée dans une société distincte qui paie un loyer.
- Responsabilité des associés indéfinie (non solidaire) [R3-59].
- Occupation gratuite par un associé : citée seulement à propos de l'exonération de plus-value de résidence principale [R3-59] ; règles fiscales détaillées : voir Q9.
- Régime MH : une SCI à l'IR n'en bénéficie que si elle est familiale (ou dans les autres exceptions) [R3-06] ; voir 1.3.

### 5.7 Régime mère-fille

- Régime optionnel (« Le régime fiscal des sociétés mères et filiales est optionnel. ») réservé aux sociétés soumises à l'IS au taux normal ; dividendes exonérés sauf une quote-part de frais et charges : « Cette quote-part est égale à 5 % du montant de ces produits, crédit d'impôt compris » (1 % dans certains cas de groupe) [R3-61] (PAGE LUE, version du 26/06/2024).
- Seuil de participation : 5 % du capital (condition de droits de vote supprimée depuis le 03/02/2016) [R3-62] (EXTRAIT). Durée de conservation des titres (deux ans selon l'usage) : non lue dans une source ; INCONNU ici, à vérifier (CGI art. 145).
- Effet chiffré (ESTIMATION) : 100 € de dividendes remontés à une holding = 5 € réintégrés × 25 % = 1,25 € d'IS, soit un coût fiscal de 1,25 %. Mais attention à la taxe sur les holdings patrimoniales (5.2) si la holding détient des actifs non professionnels.

## Q6. TVA 2025-2026

### 6.1 Activités équestres : le taux réduit a-t-il été rétabli ? Oui, partiellement, depuis le 1er janvier 2024

Source principale : BOFiP BOI-TVA-SECT-80-10-30-50, version en vigueur depuis le 25/03/2026 [R3-22] (PAGE LUE).
- « la France fait partiellement usage, depuis le 1er janvier 2024, de la possibilité qui lui est offerte » (directive 2006/112/CE modifiée par la directive (UE) 2022/542 du 5 avril 2022) ; base : CGI art. 278-0 bis, O [R3-22].
- **5,5 %** : « l'enseignement et la pratique de l'équitation » (§ 50) ; animations et démonstrations « indépendamment des buts et motivations du consommateur » (§ 60) ; accès aux manèges, carrières et écuries et « les mises à disposition d'équidés à des fins de pratique de l'équitation » (§ 70) ; « la prise en pension du cheval d'un client [...] relève du taux réduit de TVA de 5,5 % » lorsqu'elle « en constitue l'accessoire » (accès aux installations ou pratique de l'équitation) (§ 50) ; pensions dans le cadre de la production agricole et « livraison d'un équidé à des fins de reproduction » ; saillie sans acte vétérinaire (§ 10-20).
- **20 % (taux normal)** : « relèvent du taux normal de la TVA l'ensemble des ventes d'équidés et des prestations de services [...] telles que par exemple l'entraînement, le dressage ou la prise en pension » hors exceptions ci-dessus ; « La livraison de chevaux de course » (§ 90) ; « les prises en pension en vue de la valorisation des équidés à des fins commerciales » et chevaux mis à la retraite (§ 100) ; courtage de saillies, cession de poulains non destinés à la boucherie ou à l'agriculture (§ 120) ; « Les prestations de location de boxes, sans entretien du cheval, ne constituent pas une opération de prise en pension. » donc taux normal (§ 130).
- **Exonération** : « Les leçons ou cours d'équitation sont exonérés de la TVA » lorsqu'ils sont donnés par une personne physique rémunérée directement par ses élèves, sans salarié participant à l'enseignement [R3-22] (reformulation du résumé, première partie citée).
- Équidés destinés à la boucherie : 2,10 % (vendeurs au remboursement forfaitaire) ou 5,5 % (assujettis) (§ 40).
- Confirmation : la fiche service-public « Taux de TVA dans le secteur des loisirs » (vérifiée le 11/08/2026) indique 5,5 % pour les « Activités équestres (cours, pratique, accès aux installations destinées aux équidés) » [R3-26] (PAGE LUE).
- Historique : en février 2023, le Gouvernement jugeait l'extension à toute la filière « difficilement compatible avec le contexte très contraint de nos finances publiques » ; la doctrine alors opposable limitait le 5,5 % aux animations, démonstrations et à l'accès aux manèges, carrières ou écuries (BOI-TVA-SECT-80-10-30-50 § 20) ; coût estimé par la question écrite : 35 M€ [R3-21] (PAGE LUE).
- **Conséquence pour le modèle** : une pension « travail » où le propriétaire monte son cheval et utilise les installations est à 5,5 % ; une pension de valorisation commerciale, une pension retraite, une location de boxes « nus » (sans entretien) ou la vente de chevaux de sport sont à 20 %. Le prix public TTC d'une pension doit être converti en HT avec le bon taux. À VALIDER au cas par cas par un expert-comptable (frontière « accessoire » fragile).

### 6.2 Autres activités du domaine

| Activité | Taux | Statut et source |
|---|---|---|
| Droits d'entrée d'un château ou monument privé, parcs et jardins | **10 %** (CGI art. 279, b nonies) ; « sites patrimoniaux, monuments et bâtiments historiques » ; la non-inscription MH est sans incidence | PAGE LUE [R3-23 § 10, § 70] |
| Droits d'entrée des musées et monuments exploités par des établissements publics ou à but non lucratif | exonérés | PAGE LUE [R3-26] |
| Location d'un château ou d'une salle pour un événement (mariage, séminaire) | n'est pas un droit d'admission : « la location de salles ou châteaux afin d'y d'organiser des évènements (mariages, anniversaires, etc.) » est exclue du 10 % [R3-23 § 45] ; donc taux normal 20 % | PAGE LUE pour l'exclusion ; 20 % = ESTIMATION (taux normal) à confirmer |
| Forfait regroupant plusieurs prestations | taux « le plus élevé parmi les éléments qui ne peuvent être considérés comme accessoires » [R3-23 § 140] | PAGE LUE |
| Spectacles vivants et concerts | 5,5 % | PAGE LUE [R3-26] |
| Hôtels de tourisme classés | 10 % | PAGE LUE [R3-24] |
| Location meublée avec au moins 3 des 4 prestations (petit-déjeuner, linge, nettoyage régulier, réception) | soumise à TVA ; hébergement de type hôtelier à 10 % pour 30 nuits maximum | PAGE LUE [R3-24] |
| Location à usage d'habitation (nue ou meublée sans prestations) | « en général exonérée de TVA » | PAGE LUE [R3-24] |
| Restauration (repas servis sur place), petit-déjeuner | **10 %** : « Tous les plats servis dans la restauration sont facturés au taux intermédiaire de 10 % » ; boissons alcoolisées : « Toutes les boissons alcoolisées sont vendues au taux normal de 20 % » | PAGE LUE [R3-29] |
| Produits d'origine agricole (dont, probablement, foin et paille) | 5,5 % | PAGE LUE pour la catégorie [R3-25] ; application au foin = ESTIMATION |
| Travaux forestiers ; bois de chauffage | 10 % | PAGE LUE [R3-25] |
| Prestations de services agricoles | « en général, soumises à la TVA à 20 % » | PAGE LUE [R3-25] |
| Location de terres nues agricoles (bail rural) | exonération avec option possible (CGI art. 261 D et 260) | INCONNU dans les pages lues ; à vérifier (BOFiP série BOI-TVA-CHAMP-30-10-60) |
| Fourniture d'électricité | 20 % : « L'abonnement pour la livraison d'électricité ainsi que la consommation d'électricité sont soumis à la TVA à 20 % » (métropole). Le cas du producteur qui vend sa production (photovoltaïque, hydro) n'est pas traité sur la page : 20 % = ESTIMATION | PAGE LUE [R3-30] |
| Pose d'équipements photovoltaïques par un installateur qualifié | 5,5 % (LF 2026, art. 94) | PAGE LUE [R3-18] (synthèse d'avocats) |

Franchise en base de TVA 2026 [R3-27] (PAGE LUE, vérifiée le 01/01/2026) : « Pour l'année 2026, les seuils de franchise en base de TVA française applicables restent inchangés » : commerce et hébergement 85 000 € (tolérance 93 500 €) ; prestations de services 37 500 € (tolérance 41 250 €). Le projet de seuil unique de 25 000 € a été abandonné.

## Q7. Statut agricole, bail rural, risque de requalification

### 7.1 Activités équestres agricoles

- Le statut du fermage s'applique en totalité quand trois éléments sont réunis : « Mise à disposition d'un immeuble à usage agricole », exploitation pour une activité agricole, « Caractère onéreux du contrat » ; le loyer « est encadré par la loi » [R3-28] (PAGE LUE, vérifiée le 16/06/2025).
- La même fiche indique que « Certaines activités équestres (entretien et préparation des équidés, à l'exception des activités de spectacle) » sont soumises au statut en raison de la nature de l'activité [R3-28]. Base : C. rural art. L. 311-1 modifié par la loi du 23 février 2005 (texte non lu sur Légifrance) ; selon un commentaire d'avocat, depuis 2005 « les activités équestres sont classées comme des activités agricoles à l'exception des activités de spectacle » et un contrat de mise à disposition d'un immeuble à un centre équestre « est susceptible de relever du statut du fermage » [R3-45] (PAGE LUE, article de 2013).
- Conséquences fiscales et sociales (bénéfices agricoles, affiliation MSA) : non vérifiées dans une page lue lors de cette mission. INCONNU ; à vérifier sur msa.fr et dans le BOFiP (série BOI-BA-CHAMP).
- TVA : les pensions dans le cadre de la production agricole relèvent du 5,5 % [R3-22] ; voir Q6.

### 7.2 Risque de requalification en bail rural

| Situation | Règle ou jurisprudence | Statut |
|---|---|---|
| Vente d'herbe | « assimilées à des baux ruraux » lorsqu'elles sont consenties chaque année au même agriculteur ; pas si elles sont occasionnelles et à des acquéreurs différents [R3-28] | PAGE LUE (reformulation fidèle) |
| Location de boxes, sellerie, paddock à un professionnel | Tribunal paritaire de Senlis, confirmé par CA Amiens le 6 décembre 2016 : requalification portant sur « 14 boxes de chevaux, une sellerie et un paddock » [R3-47] | EXTRAIT (motivation non lue) |
| Boxes d'écuries de chevaux de course | La question écrite n° 31336 (2020) décrit des boxes d'écuries de chevaux de course soumis au fermage ; la réponse du ministère de la Justice rappelle que la sous-location est « par principe prohibée par le cinquième alinéa de l'article L. 411-35 » (ordre public, « nullité absolue », résiliation possible) [R3-48] | PAGE LUE |
| Gardiennage de chevaux seul | Cass. 3e civ., 13 mai 2009, n° 08-16.421 : « la seule activité de gardiennage de chevaux n'entre pas dans la classification des activités agricoles » ; requalification refusée aux preneurs qui ne justifiaient pas « de revenus provenant de leur exploitation » [R3-46] | PAGE LUE (commentaire de presse juridique) |
| Enseignement de l'équitation sans fourniture de chevaux | cité comme activité non agricole (arrêt de la Cour de cassation de 2007) [R3-45] | PAGE LUE (commentaire, référence exacte de l'arrêt à vérifier) |
| Bail commercial conclu pour une activité équestre | peut être requalifié en bail rural lors de son renouvellement ; règles impératives [R3-45] | PAGE LUE (commentaire 2013) |

Conséquences d'une requalification [R3-45] (PAGE LUE) : bail de neuf ans « renouvelable tacitement », fermage plafonné par arrêté préfectoral, règles impératives. Le droit de préemption du preneur n'est pas traité dans les pages lues (INCONNU ici). **Pour le propriétaire du château, une requalification signifie perdre durablement la maîtrise d'écuries et de prés au cœur du domaine.**

### 7.3 Alternatives contractuelles (à faire valider par un avocat en droit rural)

- Contrats exclus du statut [R3-28] (PAGE LUE) : « conventions d'occupation précaire », « conventions pluriannuelles d'exploitation agricole ou de pâturage », locations de forêts, baux emphytéotiques ; mise à disposition au profit de la SAFER (6 ans maximum, renouvelable une fois).
- Petites parcelles : application partielle du statut selon un seuil fixé par arrêté préfectoral ; un seuil « inférieure à 1 hectare » est fréquent selon [R3-45] ; exclu si la parcelle est indispensable à l'exploitation.
- Prestation de services plutôt que location : contrat de pension où le domaine assure les soins (alimentation, litière, surveillance) ; la jurisprudence de 2009 [R3-46] indique que le simple gardiennage n'est pas agricole, mais une pension de préparation ou d'entraînement l'est depuis 2005 [R3-28]. **Point incertain** : la frontière dépend des faits (qui soigne, qui entraîne, exclusivité des boxes, durée). ESTIMATION ; À VALIDER.
- Convention pluriannuelle de pâturage : limitée à certaines zones définies par arrêté préfectoral (montagne notamment) selon mes connaissances, non vérifié dans une page lue : INCONNU.
- Bail commercial : possible pour une activité non agricole (gardiennage seul, activités de spectacle), mais risque de requalification au renouvellement si l'activité devient agricole [R3-45].

## Q8. Urbanisme et réglementation

### 8.1 Zones A et N, changement de destination, STECAL

- Principe : « les zones agricoles ne sont pas constructibles » sauf projets « strictement encadrés » par le règlement du PLU ; « les constructions et les changements de destination doivent être compatibles avec l'exercice d'une activité agricole » ; extensions mesurées et annexes des constructions existantes possibles ; STECAL pour des « résidences démontables » ; « Dans les communes sans PLU, ni carte communale, les constructions sur des terrains cultivés ne sont pas autorisées. » Références citées : C. urb. L111-3 à L111-5, L151-11 à L151-13, R151-17 à R151-26 [R3-41] (PAGE LUE, vérifiée le 11/04/2025).
- Désignation des bâtiments pouvant changer de destination par le PLU et avis conforme de la CDPENAF (zone A) ou de la CDNPS (zone N) : non trouvés dans une page lue. INCONNU ici ; à vérifier sur le texte de l'article L151-11 du code de l'urbanisme (Légifrance) et dans le PLU de la commune.
- **Conséquence pour le modèle** : transformer une grange en salle de réception, en gîtes ou en bureaux exige (1) que le PLU ait désigné ce bâtiment, (2) un permis, (3) l'accord de l'ABF si le bâtiment est en abords ou protégé. Délai et aléa forts : à traiter comme HYPOTHÈSE à confirmer commune par commune.

### 8.2 Monuments historiques et abords

- Immeuble classé : il « ne peut être détruit ou déplacé ou être l'objet de travaux sans autorisation délivrée par le préfet de région » ; travaux sous « contrôle scientifique et technique » ; « La maîtrise d'œuvre de ces travaux doit être confiée à des catégories de professionnels spécialisés. » [R3-50] (PAGE LUE).
- Immeuble inscrit : travaux soumis « dans la plupart des cas, à un permis » ou « à une déclaration préalable », délivrés « après accord du préfet de région » ; contrôle scientifique et technique « tout au long des travaux » [R3-50].
- La protection « constitue une servitude d'utilité publique » ; en cas de vente, informer l'acquéreur et le préfet de région « dans les quinze jours » [R3-50].
- Abords : périmètre délimité ou, à défaut, immeubles « à moins de 500 mètres » dans le champ de visibilité ; travaux « soumis à une autorisation préalable nécessitant l'accord de l'architecte des Bâtiments de France » (loi n° 2016-925 du 7 juillet 2016) [R3-51] (PAGE LUE). Formulaire spécifique pour les travaux non soumis au code de l'urbanisme : cerfa 16291*01 [R3-49].
- Coût et délai : la maîtrise d'œuvre spécialisée (ACMH pour le classé) et l'accord de l'ABF allongent les délais et augmentent les coûts (chiffres : voir R1). ESTIMATION qualitative.

### 8.3 Sites classés

- Le régime MH des revenus fonciers exclut les sites classés, sauf s'ils sont aussi monuments historiques [R3-07 § 40] (PAGE LUE). Un bien en site classé peut recevoir le label de la Fondation du patrimoine [R3-08].
- Régime d'autorisation des travaux en site classé (C. env. L341-10) : la page du ministère de l'Écologie n'a pas pu être lue (erreur 503). INCONNU ; à vérifier sur ecologie.gouv.fr ou auprès de la DREAL.

### 8.4 ERP : catégories, seuils, obligations

- Définition : « des bâtiments, locaux ou enceintes dans lesquels le public a un accès gratuit ou payant » [R3-38] (PAGE LUE, vérifiée le 26/09/2025).
- Catégories : 1re > 1 500 personnes ; 2e 701 à 1 500 ; 3e 301 à 700 ; 4e jusqu'à 300 ; 5e en dessous des seuils fixés par type [R3-38].
- Seuils de la 5e catégorie (sous-sol / étages / ensemble) [R3-38] : type L salles de réunion et polyvalentes 100 / – / **200** ; type L salles de spectacles, projections, cabarets 20 / – / **50** ; type N restaurants 100 / 200 / **200** ; type O hôtels **100** ; type X sport couvert 100 / 100 / **200** ; type PA plein air **300** ; type CTS chapiteaux et tentes **50** ; type Y musées 100 / 100 / **200**. En 5e catégorie, le personnel n'est pas compté dans l'effectif.
- Gîtes : un gîte rural n'est ERP que si sa capacité de couchage dépasse 15 places ou s'il accueille plus de 7 mineurs sans leurs familles [R3-38]. Chambres d'hôtes au-delà de 5 chambres / 15 clients : réglementation ERP [R3-35].
- **Correction d'une leçon de la v1** : le seuil de « 50 personnes » ne vaut que pour les salles de spectacles (type L) et les chapiteaux (CTS). Une salle de réception polyvalente reste en 5e catégorie jusqu'à 200 personnes. Mais un lieu ouvert au public est ERP dès la première personne : il faut toujours respecter les règles de la 5e catégorie [R3-38]. Le classement exact (L, N, CTS) d'une salle de mariage dépend de l'usage : À VALIDER avec un bureau de contrôle.
- Sécurité incendie [R3-39] (PAGE LUE, vérifiée le 30/04/2025) : « au moins 1 extincteur portatif pour 300 m² et au moins 1 par niveau » ; « Tous les ERP sont équipés d'un système d'alarme » ; registre de sécurité ; vérifications périodiques par organismes agréés ; la commission (CCDSA) contrôle les ERP « tous les 3 ou 5 ans », mais « Les ERP de catégorie 5 sans locaux d'hébergement ne sont pas soumis à l'obligation périodique de visite de la CCDSA. » Avec locaux à sommeil (hébergement), pas de dispense de présence permanente du personnel.

### 8.5 Accessibilité (PMR)

- ERP existant de 5e catégorie : une « mesure de substitution » est obligatoire quand une partie n'est pas accessible ; dérogations possibles pour impossibilité technique, « Contraintes liées à la conservation du patrimoine », « Coût des travaux disproportionné » ; attestation d'accessibilité établie par l'exploitant lui-même en 5e catégorie ; registre public d'accessibilité obligatoire ; sanctions : fermeture, amende de 45 000 € (225 000 € pour une personne morale), remboursement de subventions [R3-40] (PAGE LUE, vérifiée le 28/11/2025).

### 8.6 Bruit : musique amplifiée (décret n° 2017-1244 du 7 août 2017)

Source : présentation officielle de la DGS et de la DGPR (2018) reproduisant le texte [R3-52] (PAGE LUE, texte extrait du PDF). L'arrêté d'application et l'état actuel du texte n'ont pas été vérifiés (Légifrance bloqué).
- Champ (CSP art. R. 1336-1) : « Lieux ouverts au public ou recevant du public, clos ou ouverts, accueillant des activités impliquant la diffusion de sons amplifiés » au-delà de la règle d'égale énergie fondée sur 80 dB(A) sur 8 heures. Applicable à tous les lieux, anciens et nouveaux, depuis le 1er octobre 2018.
- Seuils : « Ne dépasser, à aucun moment et en aucun endroit accessible au public, les niveaux de pression acoustique continus équivalents 102 dB(A) sur 15 minutes et 118 dB(C) sur 15 minutes » (94 dB(A) et 104 dB(C) pour les activités destinées aux enfants jusqu'à 6 ans).
- Obligations selon le lieu : lieux de capacité ≥ 300 personnes diffusant à titre habituel : enregistrement et affichage en continu des niveaux, information du public, protections auditives gratuites, zones ou périodes de repos auditif ; lieux < 300 personnes à titre habituel : seuils, information, protections, repos auditif ; à titre non habituel : respect des seuils seulement.
- Voisinage (C. env. R. 571-25 à R. 571-27) : pour les lieux clos, « Émergence globale de 3 dB(A) » et émergence spectrale maximale de 3 dB par octave (125 à 4 000 Hz) ; **étude de l'impact des nuisances sonores (EINS)** obligatoire pour les lieux « accueillant à titre habituel des activités de diffusion de sons amplifiés » et pour les festivals ; « La pose d'un limiteur peut être prescrite » ; sanctions : amende de 5e classe, confiscation du matériel (R. 571-96).
- **Conséquence pour un domaine de mariages (ESTIMATION)** : 20 à 40 réceptions par an avec DJ = diffusion « à titre habituel » probable ; prévoir une EINS par un acousticien, un limiteur, et souvent une salle isolée. Ce coût et la contrainte d'horaires pèsent sur la compatibilité avec les chevaux et la résidence privée. Le seuil exact de l'« habitude » n'est pas défini dans la source lue : À VALIDER.

### 8.7 Agrivoltaïsme (loi APER n° 2023-175 du 10 mars 2023, décret n° 2024-318 du 8 avril 2024)

Source : commentaire d'avocat [R3-44] (PAGE LUE) ; les textes officiels (C. énergie L. 314-36, R. 314-108 et suivants) n'ont pas été lus (Légifrance bloqué, sites ministériels en erreur 503).
- La production agricole doit rester principale : la surface rendue inexploitable « n'excède pas 10% » de la surface couverte ; hauteur et espacement compatibles avec une exploitation normale, « notamment la circulation, la sécurité et l'abri des animaux » ; rendement moyen par hectare « supérieure à 90 % » de celui d'une zone témoin ou d'un référentiel ; dérogations à la zone témoin pour un taux de couverture « inférieur à 40% » sous conditions [R3-44].
- L'élevage est visé (articles R. 314-114 « hors élevage » et R. 314-115) et le confort thermique des animaux est cité comme service rendu [R3-44].
- **Chevaux** : je n'ai trouvé aucune source lue précisant si le pâturage d'équins de loisir ou de sport est reconnu comme activité agricole « principale » pour l'agrivoltaïsme. INCONNU ; à vérifier auprès de la chambre d'agriculture et de la DDT (document-cadre départemental), et dans l'arrêté d'application du décret. Le taux maximal de couverture de 40 % pour les installations de plus de 10 MWc n'a pas été confirmé dans une source lue.
- Revenus (loyers €/ha) : traités par R8.

### 8.8 Petite hydroélectricité

- Droit fondé en titre : droits d'eau attachés aux moulins accordés sous l'Ancien Régime sur des cours d'eau non domaniaux et non abolis la nuit du 4 août 1789 ; consistance légale = « la puissance maximale dont il peut en théorie disposer » fixée par le document le plus ancien ; perte du droit si la force motrice n'est plus utilisable (ruine, changement d'affectation des ouvrages essentiels), mais une longue inutilisation ne suffit pas (CAA Nantes, 29/09/2017, n° 16NT00251 : 67 kW reconnus pour 75 kW revendiqués) [R3-53] (PAGE LUE). Exemple de litige : puissance fixée à 39 kW au lieu de 273 kW demandés (TA Poitiers, 26/12/2024) [R3-54] (EXTRAIT).
- **Point de vigilance** : la puissance reconnue d'un moulin de château est souvent de quelques dizaines de kW ; la preuve incombe au propriétaire. Obligation d'achat (arrêté tarifaire, durée, tarif) et obligations de continuité écologique : non lues dans une source officielle accessible (sites ADEME, DREAL et préfectures en erreur 403 ou 503). INCONNU ici ; voir R8 et le site de la CRE.

### 8.9 ICPE et écuries

- Aucune source lue ne traite du classement ICPE des écuries. INCONNU. À vérifier : nomenclature ICPE (rubriques 21xx « élevages ») sur aida.ineris.fr ; en l'absence de rubrique équine, les écuries relèvent du règlement sanitaire départemental (distances aux habitations, fumières), à confirmer auprès de la DDPP. Ne pas modéliser de coût ICPE sans vérification.

### 8.10 Photovoltaïque au sol en secteur protégé

- Hors secteur protégé : déclaration préalable de 3 kW à moins de 3 000 kW ; permis de construire à partir de 3 000 kW [R3-63] (PAGE LUE, vérifiée le 17/01/2025).
- En secteur protégé (sites patrimoniaux remarquables, abords d'un monument historique, sites classés, réserves naturelles, parcs nationaux) : « Vous devez déposer un permis de construire (PC). » dès 3 kW [R3-63]. Avec l'accord de l'ABF en abords (voir 8.2). **Conséquence** : un projet solaire au sol visible depuis un château protégé est exposé à un refus ; à traiter comme une option incertaine (voir R8 pour les revenus).

## Q9. Occupation privée d'un bien détenu par une société

| Structure | Règle lue | Conséquence | Statut |
|---|---|---|---|
| SCI non soumise à l'IS qui loge gratuitement un associé | Ces sociétés sont « considérées comme se réservant la jouissance de ces logements » : la valeur locative n'est pas une recette, mais « les charges afférentes au logement ne sont pas admises en déduction » (§ 170) | Pas de revenu foncier imposé, mais aucune charge déductible sur la partie privée (hors régime MH propre, voir 1.2) | PAGE LUE [R3-55] |
| Société à l'IS qui loue ou met à disposition un logement à un associé gratuitement ou sous le prix du marché | Revenus distribués (CGI art. 109) : attribution gratuite ou à prix réduit aux associés, notamment la jouissance d'un appartement consentie par une société immobilière soumise à l'IS (§ 70, reformulation du résumé de la page) ; « commet un acte anormal de gestion » sans contrepartie (§ 160) ; l'administration peut « réintégrer le montant dans les bénéfices sociaux » (§ 140) ; l'avantage est imposé chez l'associé comme « un revenu distribué » (§ 200) ; les charges d'un immeuble utilisé par le dirigeant « à des fins exclusivement privées » sont des revenus distribués (§ 110) | Double peine : IS sur le loyer manquant + imposition de l'avantage chez l'associé (31,4 % ou barème) | PAGE LUE [R3-56] |
| Holding patrimoniale à l'IS (≥ 5 M€ d'actifs, revenus passifs > 50 %) | Taxe de 20 % sur la valeur des « logements dont une personne physique associée se réserve la jouissance » (gratuit ou loyer sous le marché), à compter des exercices clos le 31/12/2026 | Coût annuel = 20 % de la valeur vénale du logement | PAGE LUE [R3-18], [R3-19] |
| Société d'exploitation (SAS, SARL) qui loge son dirigeant | Avantages en nature (« logement, voiture, etc. ») imposables comme traitements et salaires ; en SAS, cotisations sur la rémunération « et de ses avantages » | Avantage en nature soumis à IR et cotisations sociales | PAGE LUE [R3-57] |
| Abus de biens sociaux (C. com. L. 241-3 et L. 242-6) | Aucune page lue ne le détaille (la fiche [R3-57] ne mentionne que l'« abus de majorité ») | Risque pénal si l'usage privé est contraire à l'intérêt social ; montants des peines : INCONNU ici | INCONNU |

**Recommandation de structure (ESTIMATION, À VALIDER par un avocat fiscaliste)** : (1) partie privée détenue en direct ou via une SCI familiale à l'IR, sans exploitation commerciale (< 10 % du CA) ; (2) activités (réceptions, hébergement, écurie) dans une ou plusieurs sociétés d'exploitation qui paient un loyer de marché pour les seuls espaces exploités ; (3) si le propriétaire habite un bien détenu par une société à l'IS, il paie un loyer de marché, ce qui suppose un revenu personnel réel (leçon n° 2 du contexte). Dividendes : PFU de 31,4 % en 2026 [R3-57] (« à un taux global de 31,4 %, c'est-à-dire 12,8 % au titre de l'impôt sur le revenu et 18,6 % de prélèvements sociaux ») ; gérant majoritaire de SARL : pas de cotisations sur les dividendes tant qu'ils ne dépassent pas 10 % du capital social [R3-57].

## Q10. Droit du travail (essentiel)

- TO-DE (exonération de cotisations patronales pour l'embauche de travailleurs occasionnels par un employeur agricole) : « Ce dispositif appelé TO-DE est désormais pérenne. » [R3-60] (PAGE LUE, vérifiée le 23/12/2025). Plafonds (SMIC) et activités éligibles (dont, éventuellement, les activités équestres agricoles) non détaillés sur la page : INCONNU ici ; à vérifier sur msa.fr.
- Déclaration d'embauche en CDD agricole : titre emploi service agricole simplifié (Tesa-S) (fiche R17842 vue en résultat de recherche interne, non ouverte).
- Conventions collectives (production agricole, centres équestres), durée du travail, CDD saisonniers : non lus dans le cadre de cette mission. INCONNU ; sujet partagé avec R2 (coût du travail, RGDU 2026).
- Point de vigilance (ESTIMATION) : une écurie de pension ou de préparation est une activité agricole (Q7) ; ses salariés relèvent du régime agricole (MSA) et de la convention collective applicable aux centres équestres ou à la production agricole, à confirmer.

## Synthèse 1. Ce que la fiscalité MH vaut réellement pour l'équation économique

Formule (ESTIMATION, fondée sur [R3-02], [R3-04], [R3-05]) : économie d'impôt annuelle = charges éligibles × taux de déduction (100 % si ouvert, 50 % si fermé, ou règle 75 % / 25 % si habité et ouvert avec recettes) × taux marginal d'imposition du propriétaire.

Exemple (HYPOTHÈSES : 200 000 €/an de charges foncières éligibles sur un château inscrit habité ; taux marginal de 45 %, non vérifié dans une page lue) :
- fermé au public : 200 000 × 50 % × 45 % = **45 000 €/an** d'impôt en moins ;
- ouvert 50 jours par an sans droits d'entrée : 200 000 × 100 % × 45 % = **90 000 €/an** ;
- l'excédent de charges sur le revenu global n'est pas reportable quand le château ne procure aucune recette [R3-05 § 1].

Points critiques pour le modèle :
1. **Ce n'est pas un revenu du domaine.** C'est une réduction de l'impôt personnel du propriétaire. Elle ne vaut que s'il a un revenu imposable élevé au barème. Un propriétaire de 26 ans sans gros revenu personnel n'en tire presque rien. Cela contredit en partie l'objectif « sans fortune personnelle » : l'avantage MH profite surtout à un propriétaire riche en revenus.
2. Les dividendes taxés au PFU (31,4 %) ne passent pas par le barème : des charges déductibles du revenu global ne les réduisent pas, sauf option globale pour le barème. ESTIMATION fondée sur la nature forfaitaire du PFU ; À VALIDER par un fiscaliste.
3. Les loyers versés par une société d'exploitation au propriétaire (en direct ou via une SCI familiale à l'IR) sont des revenus fonciers : les charges MH s'y imputent et le déficit éventuel est « imputable sur le revenu global sans limite de montant » [R3-04 § 10]. C'est le montage le plus cohérent avec la doctrine lue, sous réserve de l'exclusion des parties « utilisées par leurs propriétaires pour les besoins d'une entreprise » [R3-04 § 40] et du risque de requalification d'une location équipée en BIC. À VALIDER.
4. L'ouverture 50 jours par an (6 heures par jour) est le prix de la déduction à 100 % et de l'exonération de droits de succession (795 A) : elle réduit la tranquillité de la résidence privée.

## Synthèse 2. Matrice « dispositif / effet chiffré / conditions / risque »

| Dispositif | Effet chiffré | Conditions principales | Risque ou limite | Sources |
|---|---|---|---|---|
| Déduction des charges MH (CGI 156) | 100 % des charges si ouvert au public, 50 % si fermé ; travaux subventionnés 100 % nets ; déficit foncier imputable sans limite si recettes | Classé ou inscrit ; ouverture 50 j/an (dont 25 non ouvrables avril-septembre) ou 40 j juillet-septembre, 6 h/j ; conservation 15 ans ; détention directe ou SCI familiale | Valeur nulle sans revenu imposable ; réintégration d'un tiers des charges sur 3 ans si vente avant 15 ans ; exclusion des parties affectées à une entreprise | [R3-02] [R3-04] [R3-05] [R3-06] |
| Abattement frais de visite | 1 525 € ou 2 290 € (avec parc ou jardin) sur les recettes brutes | Visites payantes | Ne peut créer un déficit sur la visite | [R3-04] |
| Label Fondation du patrimoine (non protégé) | 50 % des travaux déductibles, 100 % si subvention ≥ 20 % | Visible de la voie publique ; commune < 20 000 hab., SPR ou site classé ; avis ABF ; label 3 ans | Pas d'intérêts ni d'assurance déductibles ; travaux extérieurs | [R3-02] [R3-05] [R3-08] |
| Exonération DMTG (795 A) | 100 % des droits sur le château et le mobilier historique | Convention à durée indéterminée ; ouverture au public ; maintien des meubles ; entretien | Droits exigibles sur la valeur au jour du manquement ; contrainte perpétuelle | [R3-13] [R3-14] |
| Dons via la Fondation du patrimoine | Donateur : 66 % IR (plafond 20 % du revenu imposable), 60 % IS, 75 % IFI ; frais de la Fondation 6 % | Propriétaire personne physique ou SC de personnes physiques ; recettes commerciales ≤ 60 000 € HT/an (visites payantes non comptées) ; conservation 10 ans ; ouverture 10 ans | Financement de travaux, pas du fonctionnement ; doctrine de 2012 à vérifier | [R3-09] [R3-10] |
| Mécénat d'entreprise | 60 % du don (40 % au-delà de 2 M€) ; plafond 20 000 € ou 5 ‰ du CA | Bénéficiaire d'intérêt général, pas de cercle restreint | Impossible directement vers le propriétaire privé | [R3-42] [R3-43] |
| IFI | 0,5 % à 1,5 % au-delà de 800 000 € (seuil 1,3 M€) ; 30 % d'abattement résidence principale | Aucune exonération MH | Charge personnelle récurrente (ex. ≈ 36 000 €/an pour 5 M€) | [R3-01] [R3-15] |
| IS | 15 % jusqu'à 42 500 €, puis 25 % | PME : CA ≤ 10 M€, 75 % personnes physiques | — | [R3-20] |
| PFU 2026 | 31,4 % (12,8 % IR + 18,6 % PS) | Dividendes et produits de placement 2026 | 1 € de bénéfice IS distribué ≈ 0,51 € net | [R3-16] [R3-57] |
| Taxe sur les holdings patrimoniales (LF 2026) | 20 % par an de la valeur des logements occupés par un associé et des chevaux de course ou de concours non affectés à une activité opérationnelle | Holding IS ≥ 5 M€ d'actifs, contrôlée à 50 % par une personne physique, revenus passifs > 50 % ; exercices clos à partir du 31/12/2026 | Rend coûteux le château-résidence logé dans une holding | [R3-18] [R3-19] |
| TVA équestre | 5,5 % : enseignement, pratique, accès aux installations, pension accessoire à l'équitation ; 20 % : pension de valorisation ou de retraite, location de boxes sans entretien, vente de chevaux de sport | Depuis le 01/01/2024 (CGI 278-0 bis, O) | Frontière « accessoire » fragile | [R3-22] [R3-26] |
| TVA autres | Visites 10 % ; hébergement hôtelier 10 % ; restauration 10 % ; alcool 20 % ; location de salle pour événement : hors 10 % (donc 20 %, ESTIMATION) ; franchise 85 000 € / 37 500 € | — | Prix publics TTC à convertir | [R3-23] [R3-24] [R3-27] [R3-29] |
| Micro-BIC 2026 | Meublé classé et chambres d'hôtes : 83 600 € / 50 % ; meublé non classé : 15 000 € / 30 % | Loi Le Meur ; DPE (G interdit depuis 2025) | Dépendances mal isolées exclues de la location | [R3-31] [R3-33] [R3-34] [R3-36] |
| Chambres d'hôtes | ≤ 5 chambres et ≤ 15 clients | Chez l'habitant, petit-déjeuner, déclaration en mairie | Au-delà : ERP et autre statut | [R3-35] |
| Bail rural (risque) | Bail 9 ans minimum, renouvelable, fermage plafonné | Mise à disposition onéreuse d'un immeuble pour une activité agricole, y compris équestre (hors spectacle) | Perte durable de la maîtrise d'écuries et de prés | [R3-28] [R3-45] [R3-47] [R3-48] |
| ERP 5e catégorie | Salle de réunion ≤ 200 pers. ; spectacle ≤ 50 ; chapiteau ≤ 50 ; restaurant ≤ 200 ; hôtel ≤ 100 ; plein air ≤ 300 | Extincteurs, alarme, registre, vérifications | Visites périodiques CCDSA si hébergement | [R3-38] [R3-39] |
| Accessibilité | Amende 45 000 € (225 000 € personne morale) | Mesures de substitution, dérogation patrimoine possible | Fermeture administrative | [R3-40] |
| Musique amplifiée | 102 dB(A) et 118 dB(C) sur 15 min ; émergence 3 dB(A) ; EINS si diffusion habituelle | Lieux recevant du public, clos ou ouverts | Limiteur, isolation, conflits avec voisins et chevaux | [R3-52] |
| SCI à l'IR | Transparence ; activité commerciale ≤ 10 % du CA HT | Exploitation logée ailleurs | Bascule à l'IS au-delà | [R3-59] |
| Occupation gratuite d'un bien de société à l'IS | Loyer manquant réintégré + revenu distribué chez l'associé | — | Acte anormal de gestion ; risque pénal (abus de biens sociaux) non chiffré | [R3-56] [R3-57] |
| TO-DE | Exonération de cotisations patronales pour les saisonniers agricoles, « désormais pérenne » | Employeur agricole | Plafonds non lus | [R3-60] |

## Points à faire valider par un professionnel

Avocat fiscaliste :
1. Montage « château détenu en direct ou par SCI familiale à l'IR + société d'exploitation locataire » : les loyers sont-ils des revenus fonciers ouvrant droit au régime MH (déficit imputable sans limite) ou une location équipée imposable en BIC ? Portée de l'exclusion « besoins d'une entreprise » [R3-04 § 40].
2. Imputation des charges MH lorsque le propriétaire est imposé au PFU sur ses dividendes (option barème ou non).
3. Application de la taxe sur les holdings patrimoniales (LF 2026) à une société détenant le château et des chevaux de concours ; articulation avec l'IFI ; QPC éventuelles.
4. Texte actuel de l'article 200 CGI pour les dons via la Fondation du patrimoine (seuil de 60 000 € de recettes commerciales, doctrine de 2012).
5. Taux de TVA d'une pension « mixte » (travail et pré), d'une location de lieu pour événement avec prestations, et d'un forfait mariage (hébergement + salle + restauration).
6. Fonds de dotation portant tout ou partie du domaine : compatibilité avec l'occupation privée du fondateur.
7. IFI : qualification de bien professionnel pour la partie louée à la société d'exploitation (CGI art. 975), et quotités pour bois et biens ruraux (art. 976).

Notaire :
8. Convention 795 A : obligations concrètes, compatibilité avec une exploitation commerciale partielle, transmission aux héritiers.
9. Choix entre détention directe, SCI familiale et société à l'IS au regard de l'engagement de conservation de 15 ans et de la transmission.
10. Contrats d'occupation des prés et écuries (pension, convention d'occupation précaire, petites parcelles, bail commercial) pour éviter le statut du fermage.

Expert-comptable :
11. Ventilation des charges entre partie privée et parties exploitées (règle pratique 75 % / 25 %, prorata de surfaces).
12. Régimes micro ou réel, franchise de TVA et options pour chaque activité ; impact de la contribution différentielle sur les hauts revenus.
13. Coût social du propriétaire-dirigeant (SAS ou SARL) et des avantages en nature.

Avocat en droit rural ou de l'urbanisme, bureau de contrôle, acousticien :
14. Désignation des bâtiments dans le PLU pour un changement de destination (L151-11), avis CDPENAF ou CDNPS ; accord de l'ABF.
15. Classement ERP des salles (type L, N, CTS), accessibilité et dérogation patrimoniale.
16. Étude d'impact des nuisances sonores et limiteur pour les réceptions.

## Contre-exemples et cas d'échec trouvés

1. **Requalification d'écuries en bail rural** : le tribunal paritaire de Senlis, confirmé par la CA d'Amiens le 6 décembre 2016, a fait droit à une demande de requalification portant sur 14 boxes, une sellerie et un paddock [R3-47] (EXTRAIT ; motivation non lue). Cas d'échec typique pour un propriétaire qui loue ses écuries à un professionnel.
2. **Boxes de chevaux de course bloqués par le fermage** : la question écrite n° 31336 (2020) décrit « de nombreuses installations restées vacantes » faute de pouvoir sous-louer des boxes sous bail rural ; le ministère de la Justice confirme l'interdiction d'ordre public [R3-48] (PAGE LUE).
3. **Requalification refusée aux preneurs** (contre-exemple favorable au propriétaire) : Cass. 3e civ., 13 mai 2009, n° 08-16.421 : simple gardiennage de chevaux, pas d'activité agricole prouvée [R3-46] (PAGE LUE).
4. **Puissance hydroélectrique réduite** : un propriétaire de moulin demandait 273 kW et s'est vu fixer 39 kW (TA Poitiers, 26/12/2024) [R3-54] (EXTRAIT) ; 67 kW reconnus pour 75 kW revendiqués (CAA Nantes, 2017) [R3-53] (PAGE LUE).
5. **Exonération d'IFI des MH ouverts refusée** : amendement au PLF 2026 rejeté [R3-12] (EXTRAIT).
6. **TVA équestre** : en 2023, le Gouvernement refusait l'extension du taux réduit à toute la filière (coût estimé à 35 M€) [R3-21] ; extension partielle seulement depuis 2024 ; la vente de chevaux de sport et la pension de valorisation restent à 20 % [R3-22].
7. **Holdings patrimoniales** : la taxe de 20 % (LF 2026) rend coûteux un schéma courant (château et chevaux logés dans une holding qui loge l'associé) [R3-18].

## Points de doute / hypothèses non vérifiées

- Légifrance inaccessible : aucun article de loi lu dans sa version consolidée. Les règles viennent du BOFiP, de service-public.gouv.fr et de synthèses d'avocats. Plusieurs pages BOFiP datent de 2012 à 2018 (régime MH, dons Fondation du patrimoine) : leur maintien en vigueur est affiché, mais un changement législatif non encore commenté reste possible.
- LF 2026 : décrite d'après deux synthèses de cabinets (Simon Associés, Eurex) ; le numéro d'article CGI de la taxe sur les holdings (235 ter C) n'est qu'un EXTRAIT ; le header de la lettre Simon Associés indique « art. 7 » et le texte « L'article 3 » (numérotation du projet de loi probable).
- Prélèvements sociaux sur revenus LMNP et plus-values mobilières 2025 : divergence entre Que Choisir (hausse dès les revenus 2025) et la page service-public (pas de taux 2025 spécifique).
- Seuil de cotisations des chambres d'hôtes : 6 123 € [R3-31] contre 6 248 € [R3-35] pour 2025.
- Fiche F36065 : « Vérifié le 26 avril 2024 » mais contenu à jour du PFU 2026 (31,4 %) ; je retiens le contenu.
- Régime mère-fille : durée de détention de deux ans non lue.
- Location de salle pour événement à 20 % : déduit de l'exclusion du taux de 10 % [R3-23 § 45], pas lu explicitement.
- Exonération de TVA des locations de terres nues : non lue.
- Agrivoltaïsme avec chevaux : éligibilité non trouvée.
- ICPE des écuries : non trouvée.
- Fondation du patrimoine : seuil de 60 000 € de recettes commerciales tiré d'une doctrine de 2012.
- Crédits MH du PLF 2026 (-34 % en AE, -21 % en CP) : EXTRAIT, PDF du Sénat en erreur 503.
- Taux marginal de 45 % utilisé dans l'exemple de la synthèse 1 : HYPOTHÈSE non vérifiée dans une page lue.

## Chiffres clés pour le modèle

| Donnée | Valeur | Unité | Année | Statut | Source |
|---|---|---|---|---|---|
| Déduction des charges MH, immeuble ouvert au public | 100 | % des charges | règle en vigueur 2026 | PAGE LUE | [R3-02] [R3-05] |
| Déduction des charges MH, immeuble fermé au public | 50 | % des charges | 2026 | PAGE LUE | [R3-02] [R3-05] |
| Ouverture minimale pour être « ouvert au public » | 50 j/an dont 25 non ouvrables (avril-sept.) ou 40 j (juillet-sept.) ; 6 h/j | jours, heures | 2026 | PAGE LUE | [R3-04] |
| Règle pratique MH habité et ouvert avec recettes | 75 / 25 | % revenus fonciers / revenu global | 2026 | PAGE LUE | [R3-02] |
| Abattement forfaitaire frais de visite | 1 525 (sans parc ni jardin) / 2 290 (avec) | € par an | 2026 | PAGE LUE | [R3-04] |
| Engagement de conservation MH | 15 | ans | depuis 2009 | PAGE LUE | [R3-06] |
| Label Fondation du patrimoine : déduction des travaux | 50 (100 si subvention ≥ 20 %) | % | 2026 | PAGE LUE | [R3-02] [R3-08] |
| Dons via Fondation du patrimoine : plafond de recettes commerciales tolérées | 60 000 | € HT par an | doctrine 2012 | PAGE LUE (à vérifier) | [R3-10] |
| Frais de gestion Fondation du patrimoine sur collecte | 6 | % des dons | 2026 | PAGE LUE | [R3-09] |
| Réduction d'impôt du donateur particulier | 66 (plafond 20 % du revenu imposable) | % | 2026 | PAGE LUE | [R3-10] [R3-09] |
| Mécénat d'entreprise | 60 (40 au-delà de 2 M€) ; plafond 20 000 € ou 5 ‰ du CA | % | 2026 | PAGE LUE | [R3-42] |
| Seuil d'IFI | 1 300 000 | € patrimoine net taxable | 2026 | PAGE LUE | [R3-01] |
| Barème IFI | 0,5 / 0,7 / 1 / 1,25 / 1,5 | % par tranche (au-delà de 800 000 €) | 2026 | PAGE LUE | [R3-15] |
| Abattement IFI résidence principale | 30 | % | 2026 | PAGE LUE | [R3-01] |
| IS taux normal / taux réduit | 25 / 15 (jusqu'à 42 500 €) | % | 2026 | PAGE LUE | [R3-20] |
| PFU sur dividendes | 31,4 (12,8 IR + 18,6 PS) | % | revenus 2026 | PAGE LUE | [R3-16] [R3-57] |
| Prélèvements sociaux revenus fonciers | 17,2 | % | 2026 | PAGE LUE | [R3-16] |
| Taxe sur les holdings patrimoniales | 20 | % de la valeur vénale des actifs visés par an | exercices clos ≥ 31/12/2026 | PAGE LUE (synthèses d'avocats) | [R3-18] [R3-19] |
| Seuil d'actifs de la taxe holdings | 5 | M€ | 2026 | PAGE LUE | [R3-18] |
| TVA enseignement, pratique de l'équitation, pension accessoire | 5,5 | % | depuis 01/01/2024 | PAGE LUE | [R3-22] |
| TVA pension de valorisation ou de retraite, vente de chevaux de sport, location de boxes sans entretien | 20 | % | 2026 | PAGE LUE | [R3-22] |
| TVA droits d'entrée château, parc, jardin | 10 | % | 2026 | PAGE LUE | [R3-23] |
| TVA hébergement hôtelier / restauration | 10 / 10 | % | 2026 | PAGE LUE | [R3-24] [R3-29] |
| TVA location de lieu pour événement | 20 | % | 2026 | ESTIMATION | [R3-23 § 45] |
| Franchise en base de TVA | 85 000 (hébergement, ventes) / 37 500 (services) | € HT | 2026 | PAGE LUE | [R3-27] |
| Micro-BIC meublé classé et chambres d'hôtes | 83 600 / abattement 50 % | € / % | revenus 2026 | PAGE LUE | [R3-33] [R3-36] |
| Micro-BIC meublé non classé | 15 000 / abattement 30 % | € / % | revenus 2025-2026 | PAGE LUE | [R3-31] [R3-36] |
| Chambres d'hôtes : capacité maximale | 5 chambres ou 15 clients | unités | 2026 | PAGE LUE | [R3-35] |
| ERP 5e catégorie, salle de réunion polyvalente | 200 | personnes (hors personnel) | 2025 | PAGE LUE | [R3-38] |
| ERP 5e catégorie, salle de spectacle ou chapiteau | 50 | personnes | 2025 | PAGE LUE | [R3-38] |
| Gîte classé ERP au-delà de | 15 | places de couchage | 2025 | PAGE LUE | [R3-38] |
| Niveau sonore maximal (musique amplifiée) | 102 dB(A) et 118 dB(C) | sur 15 min | depuis 2018 | PAGE LUE | [R3-52] |
| SCI à l'IR : activité commerciale maximale | 10 | % du CA HT | 2025 | PAGE LUE | [R3-59] |
| Régime mère-fille : quote-part de frais et charges | 5 | % des dividendes | 2024-2026 | PAGE LUE | [R3-61] |
| Fonds de dotation : dotation minimale | 15 000 | € | 2025 | PAGE LUE | [R3-58] |
| Bail rural : durée minimale | 9 | ans | 2025 | PAGE LUE | [R3-28] [R3-45] |
| Exemple IFI pour 5 M€ (hors RP) / 3,5 M€ (RP) / 10 M€ | 35 690 / 20 690 / 98 190 | € par an | 2026 | ESTIMATION | [R3-15] |
