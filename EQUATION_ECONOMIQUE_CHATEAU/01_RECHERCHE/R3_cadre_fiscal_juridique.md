# R3 — Cadre fiscal et juridique

Agent : R3. Démarré le 2026-10-14. Fichier écrit au fur et à mesure.
Sources : `01_RECHERCHE/sources/sources_R3.csv` (identifiants [R3-xx]).

Avertissement général : ce document n'est pas un avis juridique. Les règles sont citées d'après des sources officielles lisibles (BOFiP, service-public.fr, impots.gouv.fr, etc.). Légifrance renvoie 403 : les articles de loi sont cités d'après leur reproduction dans ces sources. Tout point marqué « À VALIDER » doit être confirmé par un avocat fiscaliste, un notaire ou un expert-comptable.

Statuts : PAGE LUE (page ouverte avec WebFetch, citation exacte) / EXTRAIT (vu dans un résultat de recherche) / ESTIMATION / HYPOTHÈSE / INCONNU.

## Journal de progression

- 2026-10-14 : squelette créé.

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
- Taux de déduction (BOFiP [R3-02], [R3-05], PAGE LUE) : immeuble labellisé non ouvert : « déduction de 50 % des dépenses d'entretien et de réparation non subventionnées, portée à 100 % si la subvention couvre au moins 20 % de leur montant » (formulation du tableau, citée fidèlement). Pour les immeubles labellisés, « les intérêts d'emprunt et les primes d'assurance ne sont pas déductibles » [R3-05 § 160-230, reformulation du résumé de la page]. L'ouverture au public n'est pas exigée : « Il n'est pas en revanche exigé qu'il soit ouvert au public. » [R3-03 § 190].
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

