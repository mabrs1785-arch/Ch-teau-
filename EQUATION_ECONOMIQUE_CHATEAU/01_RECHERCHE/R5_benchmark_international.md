# R5 — Benchmark international des grands domaines (Royaume-Uni, Irlande, Italie, Espagne, États-Unis)

Agent : R5. Date de recherche : 2026-10-14. Rédaction en français, sources souvent en anglais.
Statuts : PAGE LUE (page ou PDF ouvert, citation exacte), EXTRAIT (vu dans un résultat de recherche), ESTIMATION, HYPOTHÈSE, INCONNU.
Monnaies : les montants sont laissés dans leur devise d'origine (GBP, EUR, USD) avec l'année. Aucune conversion n'est faite sauf mention explicite (ESTIMATION).

Avertissement de méthode : un domaine qui publie de gros chiffres d'affaires n'est pas forcément rentable, et la fortune d'une famille ne dit rien de la rentabilité de l'exploitation. Les comptes ci-dessous distinguent, quand la source le permet : recettes (income / turnover), résultat (surplus / profit) et trésorerie.

---

## Synthèse en bref

1. Le registre britannique Companies House a permis de lire les **comptes officiels** de 11 entités : Goodwood, Blenheim, Chatsworth, Burghley (fondation et concours complet), Badminton, Castle Howard, Longleat, Highclere, Northumberland Estates (famille d'Alnwick) et Wentworth Woodhouse. Neuf sont audités ; Badminton et Highclere sont non audités et sans compte de résultat. S'y ajoutent les comptes consolidés publiés de l'Irish National Stud.
2. **Aucun domaine ne finance son monument par la billetterie seule.** Même avec 700 000 visiteurs payants, la billetterie de Blenheim (Gift Aid compris) couvre 11,1 M£ sur 16,4 M£ de coûts d'exploitation et d'entretien du palais et du parc (2024-25).
3. Les domaines qui équilibrent leurs comptes reposent sur un **patrimoine immobilier productif**. À Burghley, l'immobilier net (3,52 M£) couvre environ 75 % des dépenses caritatives. À Goodwood, la location immobilière dégage 39 % de marge contre environ 2 % pour l'ensemble du groupe. La famille d'Alnwick s'est dotée d'une foncière qui verse 5 M£ de dividendes par an. Ailleurs, le relais vient de la **promotion foncière** reversée à une fondation (Blenheim : 2,7 M£ et 5,1 M£).
4. Les grandes machines touristiques ont des marges minces ou négatives : Goodwood + 2,0 % net (2025) ; Castle Howard – 2,0 M£ d'exploitation ; Longleat – 0,65 M£ net (2025).
5. **Côté chevaux** : le concours complet de Burghley réalise 6,3 M£ de CA pour 0,13 M£ de résultat. L'économie des étalons est une loterie (Irish National Stud : un étalon faisait 70 % du CA en 2017 et moins de 2 % en 2024 ; pendant cette transition, la perte avant impôt est d'environ 1,8 M€ par an en 2023 et 2024). Les centres équestres de Castle Leslie, Reschio, La Donaira et Biltmore sont des **atouts d'une offre hôtelière ou immobilière**, sans compte propre publié.
6. **Mécanisme le plus transposable** : Reschio (vente de fermes en ruine avec 1 ha et maîtrise architecturale) et Blenheim (promotion foncière versée à un fonds dédié). En France, ce montage bute sur la **préemption de la SAFER** (bâtiments utilisés pour l'agriculture dans les cinq ans précédant la vente ; vingt ans sur le littoral) et sur le **changement de destination** en zone A ou N (désignation par le PLU et avis conforme de la CDPENAF ou de la CDNPS).
7. **Échecs documentés** : Wentworth Woodhouse (rachetée par un trust de sauvegarde qui fait état d'une « material uncertainty » sur sa continuité) ; Adare Manor (trois ans de pertes) ; Mount Juliet (bénéfice 2023 dû à un abandon d'intérêts de 9,08 M€ par l'actionnaire) ; retard d'entretien de 2 Md£ chez les membres de Historic Houses.

---

## Journal de travail (mis à jour au fil de l'eau)

- Démarrage : lecture du contexte, des règles et de la mission R5.

- Le registre officiel des charities (register-of-charities.charitycommission.gov.uk) renvoie HTTP 403 à WebFetch, et le miroir findthatcharity.uk renvoie HTTP 502. Les comptes des charities devront venir des PDF publiés par les domaines eux-mêmes ou de Companies House (beaucoup de charities sont aussi des sociétés).
- Companies House fonctionne : la recherche interne et l'historique des dépôts se lisent avec WebFetch. Les PDF de comptes sont servis par une URL S3 signée (expiration 60 s) que WebFetch ne suit pas. Ils ont donc été **téléchargés avec curl depuis le lien officiel Companies House**, puis lus page par page (ce sont des scans, sans couche texte). Statut retenu : PAGE LUE (PDF officiel ouvert et lu).

- Bilan des outils : **15 WebSearch** (plafond atteint) ; environ 76 appels WebFetch (dont une douzaine en échec : 403, 502, 503, page vide, nom de domaine introuvable ou redirection signée impossible à suivre) ; 12 PDF de comptes téléchargés avec curl depuis Companies House et lus page par page (11 exploités).
- Sites inaccessibles pendant la session : registre des charities (403), findthatcharity.uk (502), falstaff.com (403), dewsburyreporter.co.uk (403), frpadvisory.com (403), safer.fr et plusieurs sites préfectoraux en .gouv.fr (503), media.wellingtoninternational.com (nom de domaine introuvable).

---

## 1. Royaume-Uni

### 1.1 Goodwood (West Sussex) — The Goodwood Estate Company Limited, n° 00553452 [R5-01] [R5-02]

Source : comptes consolidés audités de l'exercice clos le 31/12/2025, déposés à Companies House le 08/10/2026 (rapport signé le 30/09/2026 par le duc de Richmond and Gordon). Statut : PAGE LUE (PDF officiel, 53 pages).

**Modèle économique (citation exacte, p. 2)** : « Goodwood is principally focused on the leisure market: we deliver three of the major sporting events of the English summer: the Festival of Speed; the Qatar Goodwood Festival and; the Goodwood Revival meeting. The Group also operates a high-quality hotel, leisure club, two golf courses and the traditional estate operations include a property portfolio of residential estate properties and one of the UK's largest independent downland organic farms. The Group derives the majority of its revenue from attendance income, hospitality and sponsorship. »

**Compte de résultat consolidé (p. 15)**, en £ :

| Poste | 2025 | 2024 |
|---|---|---|
| Turnover (chiffre d'affaires) | 149 294 800 | 147 059 085 |
| Cost of sales | 117 261 903 | 112 940 654 |
| Gross profit | 32 032 897 | 34 118 431 |
| Administrative expenses | 29 363 300 | 25 221 627 |
| Impairment of freehold property | (1 183 798) [reprise] | 9 538 035 |
| Operating profit / (loss) | 4 221 912 | (598 374) |
| Profit / (loss) before taxation | 5 174 846 | (44 196) |
| Tax on profit | 2 139 320 | 2 551 412 |
| Profit / (loss) for the financial year | 3 035 526 | (2 595 608) |

**Ventilation par activité (note 3, p. 26)**, en £ :

| Activité | CA 2025 | CA 2024 | Résultat avant impôt 2025 | Résultat avant impôt 2024 |
|---|---|---|---|---|
| Management and letting of properties (gestion et location immobilière) | 4 639 246 | 4 326 388 | 1 808 631 | 1 268 070 |
| Leisure activities (événements, hôtel, golf, club, etc.) | 140 476 747 | 139 270 122 | 30 342 745 | 33 711 452 |
| Farming (agriculture) | 4 178 807 | 3 462 575 | (118 479) | (861 091) |
| Administrative costs (non ventilés) | — | — | (29 363 300) | (25 221 627) |

Lecture (ESTIMATION, calcul simple sur ces chiffres) :
- La location immobilière pèse **3,1 %** du chiffre d'affaires 2025 (4,64 / 149,3), mais dégage une marge avant frais centraux de **39 %** (1,81 / 4,64). C'est l'activité la plus rentable en proportion.
- L'**agriculture est déficitaire** les deux années (– 0,12 M£ en 2025, – 0,86 M£ en 2024), même avec des aides : « EC subsidies - area payments » 725 423 £ (2025) et 526 997 £ (2024) (note 6).
- Les loisirs font 94 % du chiffre d'affaires mais la marge globale est mince : résultat avant impôt de 5,2 M£ pour 149,3 M£ de CA, soit **3,5 %** en 2025, et une perte en 2024.

**Citations du rapport stratégique (p. 2-3)** :
- « Group revenue finished at £149.3m which is a £2.2m increase (1.5%) from 2024 (£147.1m). »
- « Cost of Sales at £117.3m were 3.8% higher than 2024 (£112.9m), as a percentage of revenue they were 79% (77% in 2024) [...] This resulted in a Gross profit of £32m [...] and an decrease in gross margin to 21% (23% in 2024). »
- « Adjusted for the Biomass impairment, the write-off of Hotel Masterplan professional fees and property revaluation movements totalling £1.9m, underlying trading profit for 2025 was £7.1m. This compares with £9.5m in 2024 [...] »
- « [...] the Group facilities in 2025 were a 7 year £18m rolling credit facility and a £5m overdraft facility. In addition, the Group has two AMC loans with balances of £3.0m and £2.6m [...] the former loan was procured to fund the Biomass boiler in 2020 [...] The latter loan was taken out to fund the Hotel re-purchase [...] »
- « The Group continues to invest in the fabric of the Estate with capital additions of £5.7m [...] »
- « The House and Hound Lodge businesses both performed strongly, partially offset by weaker trading at the Hotel and Kennels, where an increasingly competitive market, cost-of-living pressures and continued wage and cost inflation affected performance. »
- Énergie (p. 9) : « The group is operating a 3.5mW biomass boiler facility, which was commissioned in December 2021. It will generate enough renewable energy to supply both electricity and hot water for the Hotel and Goodwood House [...] » ; la chaudière a pourtant subi une dépréciation de 1,5 M£ en 2025.

**Personnel (note 5, p. 27)** : effectif mensuel moyen **1 123** (2025) et 1 178 (2024) ; charges de personnel totales **37 109 095 £** (2025) et 35 720 527 £ (2024). Le rapport (p. 6) parle aussi de « over 700 employees and casual workers at various points in our calendar ». Les deux chiffres divergent (définitions différentes) : on les garde tous les deux.

**Surface** : le même document donne « 11,500 acres on one site » (p. 5) et « the 12,000-acre Goodwood Estate » (p. 6). Divergence conservée (≈ 4 650 à 4 860 ha).

**Trésorerie (p. 20)** : « Cash generated from operations » 10 983 243 £ (2025) contre 34 749 166 £ (2024) ; achats d'immobilisations corporelles 5 143 725 £ (2025). Trésorerie fin 2025 : 33 535 189 £. Aucun dividende versé en 2025 ni 2024.

**Aides** : « Capital grants are received from the Horserace Betting Levy Board in respect of capital expenditure » (p. 26) ; compte de subventions au bilan 5 845 147 £ (2025).

**Usine Rolls-Royce sur le domaine** : les comptes lus ne chiffrent pas le loyer éventuel. INCONNU (à vérifier : notes sur les « operating lease premium », 368 517 £ en 2025, sans précision du locataire).

**Ce qu'il faut retenir pour le château** : même un domaine mondialement connu, avec trois événements majeurs, ne dégage qu'une marge avant impôt de 3,5 % en 2025 (bénéfice net 3,04 M£, soit 2,0 % du CA), après une perte en 2024. Le « underlying trading profit » revendiqué est de 7,1 M£, soit 4,8 % du CA (ESTIMATION). Et il dépend d'une machine de plus de 1 000 salariés. Ce modèle n'est **pas transposable à l'échelle d'un domaine de 50 à 300 ha**. Le seul élément transposable est la logique « immobilier locatif = petite part du CA, grosse part de la marge ».

### 1.2 Blenheim Palace (Oxfordshire) — Blenheim Palace Heritage Foundation, charity n° 1166164, société n° 09430048 [R5-03] [R5-04]

Source : rapport des trustees et comptes consolidés audités (BDO LLP) de l'exercice clos le 31/03/2025, déposés à Companies House le 12/11/2025. Statut : PAGE LUE (PDF officiel, 63 pages).

**Montage juridique (citation exacte, p. 5)** : « The Palace and its collection are held outside of the Charity; the Charity's primary purpose is to restore and preserve through funding from the visitor business and funding raised through the wider Estate's land development. » Et : « For the use of the Palace, the Charity pays a small annual rent to a related entity plus a significant maintenance obligation which it fulfils through its restoration programme. » La fondation détient 100 % de Blenheim Visitors Limited (restauration, boutiques, eau), qui « acts as a payroll bureau for the whole of Blenheim Estates » (p. 12).

**État des activités financières consolidé (p. 29)**, en milliers de £ :

| Poste | 2024-25 | 2023-24 |
|---|---|---|
| Donations and grants | 3 055 | 5 502 |
| Operation of the Palace and park (billetterie + Gift Aid) | 11 068 | 9 803 |
| Commercial trading operations | 16 832 | 13 580 |
| **Total income** | **30 955** | **28 885** |
| Dépenses commerciales | 11 427 | 10 592 |
| Operation of the Palace and park | 12 569 | 11 791 |
| Preservation and maintenance | 3 791 | 4 374 |
| **Total expenditure** | **27 787** | **26 757** |
| Net gains on investments | 536 | 420 |
| **Net income** | **3 704** | **2 548** |

**Détail des recettes commerciales (note 5, p. 42)**, en milliers de £ (2024-25 / 2023-24) : fonctions et événements dans le palais et le parc **3 841 / 2 618** ; **tournages (« Income from filming ») 1 140 / 211** ; recettes des filiales 10 924 / 9 797 ; intérêts 435 / 836 ; loyers 372 / 0 ; sapins de Noël 19 / 22.

**Billetterie (note 4)** : droits d'entrée et visites 9 546 k£ + Gift Aid récupéré 1 522 k£ = 11 068 k£. **Visiteurs payants : 700 000** (2024-25) contre 698 000 (p. 9). Objectif du plan à 10 ans : plus de 750 000.

**Les visites ne couvrent pas le coût du monument (note 7, p. 43)** : coûts des deux activités caritatives 16 360 k£, contre 11 068 k£ de billetterie et Gift Aid. Déficit avant dons : **– 5 292 k£** ; après dons et subventions : **– 2 237 k£** (« Net cost funded from other income »). Ce sont les profits commerciaux (restauration, boutiques, événements, tournages) et les dons d'entités liées qui comblent l'écart.

**Restauration et entretien** :
- « During the year to 31 March 2025, we have spent £2.5m (2024: £3.2m) on preservation and restoration work [...] We aim to spend an average of £4m each year on conservation and restoration. » (p. 10)
- « [...] a major restoration project focused on a significant section of the Palace roof. The works are expected to span two years with an allocated budget of £10.4m. » (p. 10)
- Engagement de 40 M£ de restauration sur le plan décennal lancé en 2017 (p. 5).
- Dépenses de « Preservation and maintenance » : 3 791 k£, dont restauration 2 452 k£ et entretien jardin et parc 1 035 k£ (note 6).

**Mécanisme clé : l'immobilier finance le monument** :
- Dons de « Blenheim Supporting Limited of £2.7m (2024: £nil), a related entity which donates its profits from land promotion to the Charity » (p. 15).
- « Designated funds have increased to £21.9m [...] predominantly due to the transfer of the £5.1m donation from the Park View development land drawdown to designated funds » (p. 16).
- Fonds dédié de 21 853 k£ au 31/03/2025 : immeubles de rapport 10 577 k£, fonds indiciels 832 k£, prêt à Blenheim Finance Limited 10 444 k£ (p. 11). « In the year ended 31 March 2024, the Charity purchased 18 residential investment properties » (p. 8). Objectif : 45 M£ en 2026 (p. 11).

**Maintenance fund britannique en action** : parmi les fonds affectés, « Maintenance Fund distribution of £133k for restoration and conservation of the Palace » (note 3, p. 41).

**Énergie** : « In the year ended 31 March 2025 the 7MW Weaveley solar park was completed and connected to the grid. The 20-acre solar park [...] » ; deux chaudières biomasse et une petite centrale hydroélectrique (p. 10). Revenu de l'énergie : INCONNU (non isolé dans les comptes de la fondation).

**Effectifs et coûts salariaux** : charges de personnel du groupe 12 846 k£ (2024-25). Effectif moyen : non relevé dans les pages lues (INCONNU ici).

**Échecs internes** : Blenheim Visitors Limited affiche des capitaux propres négatifs de – 992 k£ et sa filiale Love Water Limited de – 1 950 k£ au 31/03/2025 (note 5). L'activité d'eau a été vendue le 19/09/2025 « to a third-party buyer for £255k » (p. 14). Les réserves libres du groupe sont **négatives : – 1 521 k£** (p. 16). Le rapport l'assume : « Given the regularity of income streams and the availability of funding from related entities within the Blenheim Estate we do not think it is necessary to hold more than £1m of free reserves ».

**Leçon** : même avec 700 000 visiteurs payants, le monument coûte plus qu'il ne rapporte en billetterie. L'équilibre vient de trois béquilles : le commerce (restauration, boutiques, événements, tournages), le **développement foncier** du reste du domaine (profits de promotion reversés par une entité liée) et un fonds dédié investi en immobilier locatif.

### 1.3 Chatsworth (Derbyshire) — Chatsworth House Trust, charity n° 511149, société n° 01541046 [R5-05] [R5-06]

Source : rapport du Council of Management et comptes consolidés de l'exercice clos le 31/03/2025, déposés le 20/11/2025. Statut : PAGE LUE (PDF officiel, 62 pages).

**Montage (p. 4)** : « The charity holds a lease of Chatsworth House and its essential contents, with approximately 1,822 acres of land including the garden, park and woodland. » La charity est distincte du « Chatsworth Settlement » (trust familial) mais lui est liée : « The charity and its subsidiary are separate from but have an association with the Chatsworth Settlement » (p. 2). Le bailleur n'est pas nommé dans les pages lues (HYPOTHÈSE : le trust familial). Le personnel est « jointly employed by the charitable company and the Trustees of the Chatsworth Settlement » (p. 13).

**État des activités financières consolidé (p. 22)**, en milliers de £ :

| Poste | 2024-25 | 2023-24 |
|---|---|---|
| Donations and legacies | 587 | 490 |
| Charitable activities (billetterie maison, jardin, ferme) | 13 340 | 13 833 |
| Other trading activities (événements, franchise, sponsoring) | 4 825 | 4 563 |
| Investments | 600 | 518 |
| **Total income** | **19 352** | **19 404** |
| Raising funds | 2 186 | 2 470 |
| Charitable activities | 15 207 | 15 269 |
| **Total expenditure** | **17 393** | **17 739** |
| **Net income before net gains on investments** | **1 959** | **1 665** |

Citation (p. 12) : « The admissions income accounted for 69% (2023/24: 71%) of the charity's total incoming resources in 2024/25. » Et : « events operated by our subsidiary company Chatsworth House Enterprises Limited £2,087,000 (2023/24: £2,481,000), franchise income £1,025,000 (2023/24: £951,000), sponsorship of events and exhibitions £331,000 (2023/24: £239,000) and other income £1,382,000 (2023/24: £893,000). »

**Visiteurs (p. 11)** : 630 114 (2024-25), 611 130 (2023-24), 600 471 (2022-23), 573 686 (2021-22), 304 001 (2020-21, Covid). Les visiteurs du parc seul et des événements ne sont pas comptés.

**Événements équestres** : « Each year in the Park, the charity hosts a programme of popular events including the Chatsworth Country Fair and the Chatsworth International Horse Trials. These events are attended by over 130,000 people » (p. 10).

**Coûts d'entretien (note 9, p. 38)**, en milliers de £ 2024-25 : entretien jardin, parc et bois **1 781** ; entretien courant de la maison et des écuries **2 705** ; réparations **1 207** ; assurance 342 ; entretien des collections 412 ; frais de billetterie 4 255.

**Personnel (note 12, p. 40)** : effectif moyen 170 personnes (169), réparti ainsi : administration et direction 34, domestique 11, accueil et guides 43, **maintenance 32**, **jardins 29**, domaine 7, ferme pédagogique 14. Effectif mensuel moyen en tête : 348. Charges de personnel : 6 929 k£.

**Historique des travaux** : « The Master Plan was a major project of essential restoration and development [...] which lasted from 2007 to 2019 at a cost of £33.4m. » (p. 11)

**Réserves** : total 36 988 k£, réserves libres 12 202 k£ au 31/03/2025 (p. 13).

**Leçon** : Chatsworth vit d'abord de la billetterie (69 % des recettes) et dégage environ 2 M£ d'excédent par an pour 19 M£ de recettes, soit environ 10 % (ESTIMATION : 1 959 / 19 352). Le modèle suppose 600 000 visiteurs payants, hors de portée d'un domaine privé français de 50 à 300 ha.

### 1.4 Burghley (Lincolnshire) — Burghley House Preservation Trust Limited (société n° 00951524) et Burghley Horse Trials Limited (n° 07087188) [R5-07] [R5-08] [R5-09]

**a) La fondation (charity)** — rapport annuel 2026 et comptes consolidés de l'exercice clos le 31/01/2026, déposés le 17/08/2026. Statut : PAGE LUE (PDF officiel, 70 pages).

Modèle (p. 4-5) : « Burghley is one of England's great Treasure Houses, endowed with its own land and property portfolios. » Et : « The Estate's portfolio includes not only residential properties but farms and woodland, shops and commercial premises. The Estate provides an essential income to ensure that Burghley House can be preserved for future generations. The portfolio must evolve, mature and be re-endowed with assets to secure its future. The Trust's property subsidiaries will deliver quality development in and around the historic town of Stamford for the future of the House and Estate income. »

**État des activités financières consolidé (p. 39)**, en £ :

| Poste | 2025-26 (clos 31/01/2026) | 2024-25 |
|---|---|---|
| Donations and legacies | 788 641 (dont legs de 550 380 affecté) | 87 111 |
| Other trading activities (événements, Horse Trials, golf, commerces) | 10 112 615 | 9 313 395 |
| Income from investments (surtout l'immobilier) | 5 353 529 | 5 244 303 |
| Income from charitable activities | 1 476 255 | 1 390 356 |
| **Total income and endowments** | **17 731 040** | **16 035 165** |
| Expenditure on raising funds | 11 818 647 | 11 134 527 |
| Expenditure on charitable activities | 4 689 993 | 4 466 553 |
| **Total expenditure** | **16 508 640** | **15 601 080** |
| Net gains on investments (réévaluation) | 59 602 339 | 8 538 827 |

Citations (p. 24-26) :
- « Income for the year was nearly £18 million which was a 10% increase on the previous year. »
- « The investment property portfolio generated net revenue of £3,520,257 (2025: £3,196,593) » : l'immobilier locatif net couvre à lui seul environ 75 % des dépenses caritatives (ESTIMATION : 3,52 / 4,69).
- « The Trust showed an unrestricted fund surplus for the year of £1,098,526 (2025: surplus £821,147) ». L'excédent net affiché de 60,8 M£ vient presque entièrement de la **réévaluation** des immeubles (59,6 M£) : ce n'est **pas** de la trésorerie.
- « The focus for Governors continued with the investment of a new urban extension to the North of Stamford, this development will take many years to complete, but gives the Charity the opportunity to re-endow itself [...] » ; participation dans « Stamford North LLP » avec d'autres propriétaires (p. 26).
- « Mineral income fell this year, and Governors are conscious of the limited life of minerals. » ; « Filming income was substantially lower this year than in previous, and is somewhat hard to predict » (p. 24).
- Dette : « Advantage has been taken of affordable bank debt to provide working capital to finance the fulfilment of the objectives and property development and as a consequence the income account is overdrawn. » (p. 26)
- **Retard d'entretien non provisionné** : « The Governing Body do not consider it would be appropriate to make provision in the accounts for the significant cost of dealing with the backlog of dilapidations to property owned by the Charity. » (p. 25) Montant : INCONNU (non chiffré dans les pages lues).
- Risques listés (p. 27) : perte ou destruction du monument, « The ongoing liability to repair and restore Burghley House », baisse des visiteurs, baisse des loyers, « The loss of sponsorship of the Burghley Horse Trials ».
- Diversification : une partie du golf louée à un opérateur de padel (p. 7).

**b) Burghley Horse Trials Limited** — comptes audités (Saffery LLP) de l'exercice clos le 31/01/2026, déposés le 19/08/2026. Statut : PAGE LUE (PDF officiel, 16 pages). Activité : « the management of a four-star rated equestrian event » (sic ; le rapport de la fondation parle d'un « 5* equestrian sporting event »).

| Poste (en £) | 2025-26 | 2024-25 |
|---|---|---|
| Turnover | 6 296 253 | 6 052 701 |
| Cost of sales | (4 452 069) | (4 262 014) |
| Gross profit | 1 844 184 | 1 790 687 |
| Administrative expenses | (1 713 048) | (1 723 283) |
| Operating profit | 131 136 | 67 404 |
| Profit before taxation | 140 409 | 67 404 |
| Effectif mensuel moyen | 7 | 8 |

- Marge d'exploitation : **2,1 %** du CA en 2025-26 et 1,1 % en 2024-25 (ESTIMATION, calcul).
- Fonds propres **négatifs** : – 18 325 £ au 31/01/2026 (– 158 734 £ un an plus tôt ; – 226 138 £ au 01/02/2024).
- Note 9 : « During the year, Burghley Horse Trials Limited distributed profits of £399,882 (2025: £280,150) to the Trustees of the 6th Marquess of Exeter Will Trust. » La note 3 indique par ailleurs que les profits imposables sont versés en Gift Aid à la société mère. Le mécanisme exact de ces versements n'est pas expliqué : INCONNU.
- Le rapport de la fondation (p. 24) : « Overheads to set the event up are growing at a rate above inflation, driven partly due to increased labour costs. »

**Leçon pour un projet équestre** : un concours complet de niveau mondial, organisé depuis des décennies sur le parc d'un château, fait 6,3 M£ de chiffre d'affaires mais seulement **0,13 M£ de résultat d'exploitation**. Sa valeur pour le domaine tient surtout aux sommes reversées (Gift Aid, distributions) et à la notoriété, pas à une marge propre. Un événement équestre majeur n'est **pas** un moteur de rentabilité autonome.

### 1.5 Badminton Horse Trials Ltd (Gloucestershire), n° 03270324 [R5-10]

Source : comptes « total exemption full accounts » au 30/09/2025, déposés le 13/05/2026, signés par le duc de Beaufort. Statut : PAGE LUE (PDF officiel, 7 pages).

- La société **n'a pas déposé son compte de résultat** : « The company has taken advantage of section 444(1) of the Companies Act 2006 and opted not to deliver to the registrar a copy of the company's Profit and Loss Account. » Chiffre d'affaires et résultat : **INCONNU**.
- Bilan au 30/09/2025 : capitaux propres 2 919 882 £ (2 381 019 £ un an plus tôt), trésorerie 3 369 046 £. La hausse des réserves est de 538 863 £ sur l'exercice (ESTIMATION : bénéfice après impôt du même ordre, si aucun dividende n'a été versé ; non vérifiable).
- « Average number of employees, including directors, during the year was: 13 (2024: 13) ».
- Transactions avec « The Badminton Estate » non détaillées (« concluded under normal market conditions »).

**Signal d'échecs dans le secteur** (registre Companies House, recherche « horse trials ») : plusieurs sociétés organisatrices de concours complets britanniques sont dissoutes, par exemple Gatcombe Horse Trials Limited (dissoute le 18/05/2021), Glamis Country Fair and Horse Trials Limited (02/07/2024), Goring Heath Horse Trials Limited (17/12/2024), Richmond Horse Trials Limited (07/07/2026). Une dissolution n'est **pas** forcément une faillite (réorganisation possible) : c'est un signal à vérifier, pas une preuve [R5-09].

### 1.6 Castle Howard (North Yorkshire) — Castle Howard Estate Limited, n° 00480214 [R5-11]

Source : comptes complets audités (BHP LLP) de l'exercice clos le 31/01/2025, déposés le 17/10/2025. Statut : PAGE LUE (PDF officiel, 37 pages).

Citations du rapport stratégique (p. 1) :
- « The Castle Howard Estate, featuring over 200 listed buildings and monuments, is approximately 8,800 acres, comprised of farmland, woodland and parkland. » (≈ 3 560 ha)
- « The business in many ways acts as a 'not for profit organisation' since it expends all free cashflow on essential repairs, conservation and restoration [...] »
- « [...] the number of visitors to the house and grounds increased by 13% to 296,740 (2024: 262,633) [...] Revenue relating to the visitor attraction grew by 19% to £9,528,182 (2024: £7,994,263). »
- « However, business interests across the wider estate faced greater challenges, with trading conditions in leisure accommodation and farming in particular having deteriorated year-on-year, which as a result caused total turnover for the Company to fall by 4% to £14,754,343 (2024: £15,421,794). »
- « [...] the loss on ordinary activities for the year amounted to (£280,439) (2024: £1,298,182 loss), after including an unrealized positive revaluation of the Company's investment property portfolio of £2,454,666 [...] which is 'paper-based' and not an actual cash item. »

**Compte de résultat (p. 9)**, en £ :

| Poste | 2024-25 | 2023-24 |
|---|---|---|
| Turnover | 14 754 343 | 15 421 794 |
| Cost of sales | (14 370 254) | (14 496 537) |
| Gross profit | 384 089 | 925 257 |
| Administrative expenses | (2 629 083) | (2 253 923) |
| Other operating income (subventions) | 224 741 | 163 213 |
| **Operating loss** | **(2 020 253)** | **(1 165 453)** |
| Réévaluation des immeubles de placement | 2 454 666 | (175 541) |
| Profit / (loss) before taxation | 77 157 | (1 654 558) |
| **Loss for the financial year** | **(280 439)** | **(1 298 182)** |

Divergence interne : le rapport des administrateurs (p. 4) écrit « The loss for the year, after taxation, amounted to £1,298,182 », soit le chiffre de l'exercice précédent. Le compte de résultat audité donne – 280 439 £. On retient le compte de résultat.

**Ventilation du CA (note 3, p. 21)**, en £ (2024-25 / 2023-24) : ventes de biens et services 12 170 889 / 12 691 626 ; **loyers 1 870 999 / 1 916 871** ; subventions 125 955 / 160 252 ; commissions 30 057 / 8 138 ; autres 556 443 / 644 907. Les loyers font **12,7 %** du CA (ESTIMATION).

**Personnel (note 5, p. 22)** : 236 personnes en moyenne (109 temps plein, 127 temps partiel) ; charges de personnel 5 405 623 £.

Activités citées : attraction (maison et jardins), « Lakeside Holiday Park, the Tents & Tourers site and our portfolio of Holiday Cottages », agriculture (via un « farming contractor »), immobilier résidentiel (« real estate strategy »). Une fondation (« Castle Howard Foundation », n° 15265260) a été créée le 07/11/2023, ainsi que « Castle Howard Developments Limited » (06/11/2023) [R5-09] : rôle exact INCONNU.

**Leçon** : 3 560 ha, près de 300 000 visiteurs, 236 salariés, 14,8 M£ de CA… et une **perte d'exploitation de 2,0 M£**. L'hébergement de loisirs et l'agriculture ont reculé. Le bilan ne tient que grâce aux réévaluations immobilières, qui ne sont pas de la trésorerie.

### 1.7 Longleat (Wiltshire) — Longleat Enterprises Limited, n° 00789512 [R5-12]

Source : comptes complets audités (Saffery LLP) de l'exercice clos le 31/12/2025, déposés le 14/09/2026. Statut : PAGE LUE (PDF officiel, 33 pages).

- Activité : « the management of cave exhibiting at Cheddar Gorge, tourist attractions at Longleat and associated business activities at both sites » (p. 3). Le parc safari et les animaux sont le cœur du modèle (« over 90 births and introduction of eight new species », p. 1).
- **CA 2025 : 33 338 474 £** (2024 : 32 437 240 £), dont biens 9 746 694 £ et services 23 591 780 £ (note 3).
- « LEL recorded a loss before taxation of £0.3m in 2025, due to adverse weather impacting a key event during the year along with the challenging headwinds and above inflation cost base increases. » (p. 1)
- « The company made a net loss for the year of £653,941 (2024: profit of £988,160). » (p. 3)
- Investissement : « £3.6m of fixed asset investment in 2025 », dont un nouvel enclos pour hippopotames.
- **Effectif moyen : 584** (540 en exploitation, 44 en administration) ; charges de personnel 13 124 453 £ (note 7).
- Charges de location simple (« operating lease charges ») : 3 299 256 £ en 2025. Le bénéficiaire n'est pas précisé ; il pourrait s'agir du loyer versé au domaine propriétaire du site : HYPOTHÈSE non vérifiée.
- Autres revenus : loyers 149 955 £, aides agricoles « Rural basic payment scheme » 59 390 £.
- Plusieurs sociétés du groupe Longleat ont été dissoutes en 2024-2026 (Longleat Bath Arms Limited, Longleat Bishopstrow Limited, Longleat Homewood Park Limited, Longleat International Ltd, Longleat LCS Ltd) [R5-09]. Certains noms évoquent des hôtels ou auberges (HYPOTHÈSE). Raisons des dissolutions : INCONNU.

**Leçon** : une attraction de masse (zoo-safari + grottes) de 33 M£ de CA et près de 600 salariés reste à la merci d'un week-end de mauvais temps sur un événement clé. Modèle hors d'échelle et contraire au souhait de calme du propriétaire.

### 1.8 Highclere Castle (Hampshire) — Highclere Enterprises LLP, n° OC305641 [R5-13]

Source : comptes « filleted » non audités de l'exercice clos le 31/03/2025, déposés le 25/03/2026, signés par le comte de Carnarvon. Statut : PAGE LUE (PDF officiel, 8 pages).

- « In accordance with section 444 of the Companies Act 2006 (as applied to LLPs), the income statement has not been delivered. » Chiffre d'affaires et résultat : **INCONNU** dans les comptes publics.
- Effectif moyen : **106** (2024 : 108). Sommes dues aux membres au titre des bénéfices : 474 274 £ (2024 : 170 657 £). Actif net 640 770 £.
- Autres entités au registre : Highclere Castle Horse Feeds Limited (2010), Highclere Castle Media Limited (2021), deux sociétés « Highclere Castle Trustee » (2025) [R5-09].
- **Effet Downton Abbey** : non chiffrable avec les comptes publics. Voir la recherche presse plus bas (§ 1.11).

### 1.9 Alnwick (Northumberland) — Northumberland Estates Limited, n° 05941545 [R5-14]

Source : comptes consolidés audités (UNW LLP) de l'exercice clos le 31/03/2026, déposés le 21/09/2026. Statut : PAGE LUE (PDF officiel, 53 pages).

- Activité (p. 1) : « The principal activity of Northumberland Estates Limited company and its group is commercial and residential property investment and development in the UK, Europe and North America. » Le château d'Alnwick lui-même (visites, tournages Harry Potter) n'apparaît pas dans ce périmètre ; son entité d'exploitation n'a pas été identifiée : INCONNU.
- « Group revenues decreased compared to prior years to £18.9m (2025: £19.6m) in the year ended 31 March 2026. »
- Compte de résultat consolidé (p. 11), en £ : CA 18 923 012 ; **résultat d'exploitation courant 5 898 755** (2025 : 9 519 993) ; plus-value de réévaluation des immeubles 37 185 820 ; profit sur ventes de terrains à bâtir 136 709 (2025 : 2 526 243) ; résultat avant impôt 38 867 991 ; résultat net 31 225 555.
- « During the year a dividend of £5,000,000 was paid (2025: £5,000,000). » (p. 4)
- Stratégie (p. 1) : « [...] maintaining a mix of assets that generate a reliable and growing income stream, and in addition, to continue its development programme to generate capital receipts and / or rental income from its own land. » ; utilisation de pierre et de bois issus des carrières et forêts du domaine (p. 3).

**Leçon** : la famille propriétaire d'Alnwick a transformé une partie de son patrimoine en **foncière diversifiée** (commerce, logement, à l'étranger aussi), qui verse 5 M£ de dividendes par an. C'est le « moteur extérieur » le plus net de l'échantillon. Mais il repose sur un capital immobilier hérité considérable, pas sur l'exploitation du château.

### 1.10 Historic Houses (association des maisons historiques privées) et régime des « maintenance funds » [R5-15] [R5-16] [R5-17] [R5-18] [R5-19]

**a) Chiffres du secteur — fiche « UK key stats 2025 » de Historic Houses** (PDF lu) [R5-15]. Citations exactes :
- « Historic Houses members welcomed over 19 million visits in 2024 — an average of 44,500 visits per property ».
- « Generated around £1 billion in expenditure for the UK economy » ; « Directly employed over 12,000 staff ».
- « Our members reported a total backlog of £2 billion of repairs & maintenance work, despite a reported annual spend of around £160,000 each in 2024 ».
- « Over 47% of Historic Houses places delayed or cancelled urgent repairs and maintenance works due to lack of funds between 2020 and 2022 ».
- Budget d'octobre 2024 (réforme des abattements de droits de succession) : « 87% of Historic Houses members say they will be negatively affected by changes to IHT reliefs announced » ; « 54% say changes to IHT reliefs will leave them unable to develop/diversify their business » ; « 41% say they will have to make redundancies or freeze hiring due to changes made in the Budget ».
- Sources citées par la fiche : « Historic Houses Member Survey 2024/25 » ; enquête « Impacts of the 2024 Budget », décembre 2024 ; étude TVA Harlow Consulting, janvier 2025 ; étude Saffery Champness/Nordicity 2022.

Lecture (ESTIMATION) : un retard d'entretien de 2 Md£ réparti sur environ 1 450 membres donne **environ 1,4 M£ de travaux en retard par maison en moyenne**, soit près de 9 ans de dépense annuelle moyenne (160 000 £). La maison « moyenne » reçoit 44 500 visites par an, loin des 300 000 à 700 000 des grandes maisons ci-dessus.

Divergence : un résultat de recherche (EXTRAIT, document non ouvert) [R5-51] parle d'une dépense annuelle d'entretien de « £160 million » pour l'ensemble des membres. La fiche lue dit « around £160,000 each ». Avec 1 450 membres, les deux ne concordent pas (1 450 × 160 000 £ ≈ 232 M£). On retient le chiffre de la page lue.

**b) Rapport de novembre 2025 sur le Culture Recovery Fund** (article de la Museums Association, 18/11/2025, page lue) [R5-16] : rapport « From Crisis to Recovery: the Impact of the Culture Recovery Fund on Independent Heritage Five Years Later ». Le coût du retard de réparations « has doubled to £2bn since the start of the Covid pandemic ». Quatre-vingt-neuf membres ont reçu 12,5 M£ au total. Environ 80 % des membres ouverts au public sont assujettis à la TVA.

**c) Le régime britannique des « heritage maintenance funds »** (manuels HMRC et guide officiel, pages lues) [R5-17] [R5-18] [R5-19] :
- Définition (TSEM5800) : « Trusts that hold funds to pay for the maintenance of historic property are known as heritage maintenance funds (HMFs). » Le fonds détient d'autres actifs productifs de revenus pour financer l'entretien.
- Base légale : Inheritance Tax Act 1984, Schedule 4 (direction « paragraph 1 ») ; IHTA 1984 s. 27 (exonération de droits sur les biens apportés au fonds) (IHTM11250).
- Règles d'emploi (guide « Capital Taxation and the National Heritage », chapitre 8, page lue, reformulé par l'outil de lecture) : pendant les **six premières années**, le capital ne peut servir qu'à des fins patrimoniales (entretien, réparation, préservation du bien, accès du public, gestion du fonds) ; ensuite, le capital peut être retiré, mais une sortie non patrimoniale déclenche une taxation (paragraphes 8 et suivants de la Schedule 4) ; prêts sans intérêt et logement gratuit au profit du constituant interdits ; plus-values en report possible (TCGA 1992 s. 260).
- Exemple concret relevé dans les comptes de Blenheim : « Maintenance Fund distribution of £133k for restoration and conservation of the Palace » (2024-25) [R5-03].

**Transposition en France** : il n'existe pas, à notre connaissance, de fonds d'entretien défiscalisé identique. Les pistes à faire vérifier par R3 sont l'exonération de droits de mutation des monuments historiques sous convention avec l'État, le fonds de dotation et la fondation abritée (HYPOTHÈSE de travail ; non vérifiée ici).

### 1.11 Highclere — l'« effet Downton Abbey » selon la propriétaire [R5-20]

Source : Spear's, « How Lady Carnarvon turned Highclere Castle, the real 'Downton Abbey', into one of the most successful country homes », Tanya Ghahremani, 07/02/2022. Statut : PAGE LUE.
- Travaux : « the castle was in dire need of nearly £12 million in repairs, £1.8 million of which were urgently required » (situation de 2009, chiffre rapporté par le journaliste).
- Contre l'idée reçue : « the filming of Downton itself didn't benefit the castle financially all that much » (propos de Lady Carnarvon rapportés).
- Modèle : la famille doit « run the estate as a business », ce qui est nécessaire « unless you have the most immense private income » ; activités citées : « books, a gin brand, podcasts, and historic tours » ; café dans l'ancienne remise à voitures. Domaine : « the 6,000-acre estate » (≈ 2 430 ha).
- Lien avec les chevaux : la famille a une société d'aliments pour chevaux (Highclere Castle Horse Feeds Limited, au registre depuis 2010) [R5-09] ; chiffres : INCONNU.

**Leçon** : un tournage mondialement célèbre a surtout un effet de **notoriété**, qui se monétise ensuite par les visites et les produits dérivés. Le cachet de tournage lui-même ne finance pas un programme de travaux de 12 M£.

### 1.12 Holkham (Norfolk) — domaine agricole devenu foncier, tourisme et hébergement [R5-45] [R5-46] [R5-49]

Sources : page « Holkham Hall » du site touristique du Borough Council of King's Lynn & West Norfolk (page lue, sans date de publication visible) ; résultats de recherche (EXTRAIT) ; registre Companies House.
- « a thriving 25,000 acre estate » (≈ 10 100 ha).
- **Bascule des revenus** : « In 1996, 70% of the income at Holkham was derived from agriculture. » ; « Now that figure has reduced to a little more than 20%. » Activités citées : « Pinewoods Holiday Park and The Victoria Inn ».
- EXTRAIT (annonce d'une conférence de 2017, non ouverte) : hôtel-boutique, parc de vacances, projets d'énergie renouvelable, réserve naturelle nationale, plus de 300 maisons du domaine, près d'un million de visiteurs par an (chiffre promotionnel).
- EXTRAIT (octobre 2024) : rachat de six parcs de caravanes (McDonnell Caravans), montant non publié. La page du conseiller (FRP Advisory) renvoie HTTP 403.
- Comptes : Coke Estates Limited (n° 01171497) et Holkham Holiday Parks Limited (n° 11802261) déposent des comptes « total exemption full accounts » (régime des petites sociétés). Non ouverts ; pour Badminton et Highclere, ce régime n'a livré **aucun compte de résultat**. Chiffre d'affaires de Holkham : INCONNU.

**Leçon** : sur 25 ans, un très grand domaine agricole a fait passer l'agriculture de 70 % à environ 20 % de ses revenus, au profit du **logement locatif et de l'hébergement touristique** (parcs de vacances, auberge, hôtel). Cette trajectoire confirme celles de Goodwood (agriculture déficitaire) et de Castle Howard (agriculture en recul).

---

## 2. Irlande

### 2.1 Irish National Stud (Kildare) — société publique, haras et attraction touristique [R5-21] [R5-22]

Source principale : comptes consolidés 2024 de The Irish National Stud Designated Activity Company (PDF publié sur irishnationalstud.ie, 43 pages, texte extrait). Statut : PAGE LUE.

| Poste (en €) | 2024 | 2023 |
|---|---|---|
| Turnover | 7 005 632 | 7 039 147 |
| dont « Stud and farm » (saillies, pension des juments, ventes de chevaux, ferme) | 4 435 312 | 4 589 866 |
| dont « Tourism » (visites, boutique, restauration) | 2 570 320 | 2 449 281 |
| Administration expenses | (8 790 105) | (8 776 731) |
| **Operating loss** | **(1 784 473)** | **(1 737 584)** |
| Loss before tax | (1 805 887) | (1 824 611) |
| Effectif moyen (42 temps plein + 32 saisonniers en ETP) | 74 | 79 |
| Charges de personnel | 3 015 589 | 2 959 498 |

Citations du rapport du président (p. 3) :
- Dépendance à un étalon vedette : « In 2017 he [Invincible Spirit] was responsible for approximately 70% of the entire company's revenue. As recently as 2020 this was 40%. In 2024, Invincible Spirit was responsible for less than 2% of income. »
- « Our greatest challenge remains the development of stallion income to replace Invincible Spirit. Progress has been made but the reality is that investments in stallions are for the long term and take time to bear fruit. »
- Pension des juments : « 277 foals were born in our foaling unit (2023: 319). There has been strong growth in international boarding clients from France and Germany [...] »
- « In 2024 we welcomed over 144,000 visitors (2023: 152,000). »
- Amortissements 2024 : 1 337 462 € ; trésorerie générée par l'exploitation : 59 445 € seulement (1 619 544 € en 2023).

Mise à jour 2025 (The Irish Field, 10/07/2026, page lue) [R5-22] : chiffre d'affaires 6,7 M€ (– 4 %), perte d'exploitation avant amortissements 140 538 €, perte avant impôt 1,5 M€, 4 M€ de recettes de haras et 2,62 M€ de tourisme, plus de 146 000 visiteurs, effectif de 74 à 78.

**Leçon pour le projet équestre** : même un haras national prestigieux, avec 140 000 à 150 000 visiteurs par an, perd de l'argent dès que son étalon vedette décline. Le revenu d'étalonnage est **très concentré et non récurrent à long terme**. Le tourisme (≈ 37 % du CA) amortit le choc sans le compenser.

### 2.2 Castle Leslie Estate (Monaghan) — château-hôtel familial avec grand centre équestre [R5-23] [R5-24]

Sources : « Castle Leslie Estate Hospitality Year End Report 2023 » (PDF de 47 pages publié par le domaine, version « No financials », rédigée par le CEO Brian Baldwin, janvier-mars 2024 ; texte extrait) et page « Equestrian » du site officiel. Statut : PAGE LUE.

- Domaine : « Castle Leslie Estate, in County Monaghan, Ireland is nestled on the 1,000 acres of undulating Irish countryside [...] It is one of the last great Irish castle estates still in the hands of its founding family. » (≈ 405 ha)
- Hébergement : le château, « twenty-one unique bedrooms » ; le Lodge, « 50 rooms (additional 21 rooms added in July 2019) » ; maisons en location autonome (« Old Stable Mews ») ; spa, pavillon de mariage, restaurant, activités (pêche, ball-trap, fauconnerie).
- **Résultat : aucun chiffre publié.** Seule déclaration : « We achieved our highest ever revenue for the estate, coupled with our highest ever ebitda, since opening in 1992. » Chiffre d'affaires et EBITDA : INCONNU (registre irlandais CRO payant, non consulté).
- **Inflation des coûts 2023 contre 2019** (citation du rapport) : « Insurance increased by 121.5% », « Electricity increased by 72.38% », « Gas increased by 13% », « Payroll increased by 19% », « Rates increased by 38.8% », « Laundry Increased by 30% », « Credit Card Commission Increased by 62% », « Cleaning Supplies Increased by 72% ».
- Rotation du personnel : « All 91 new employees in 2023 undertook our induction » ; objectif « reduce our staff turnover by 15% ». Le graphique des âges totalise environ 219 personnes (ESTIMATION lue sur un graphique, à confirmer).
- **Centre équestre** (page officielle) : « 300 cross-country jumps », « 21 miles (34km) of bridleways », « a 1.6km all-weather gallop », « 56 stables », « a 50m x 30m indoor arena » ; promenades, cours, séjours équestres, attelage ; cavaliers à partir de 7 ans. Pas de pension de chevaux de propriétaires mentionnée.

**Leçon** : le cas le plus proche, par la taille (≈ 400 ha), du scénario S2-S3. Le centre équestre y est un **produit d'appel intégré à l'hôtellerie** (séjours, balades, cross), et non une activité isolée. Mais le modèle suppose un hôtel d'environ 70 chambres (21 au château, 50 au Lodge) et environ 200 salariés (ESTIMATION), et ses comptes ne sont pas publics.

### 2.3 Adare Manor (Limerick) et Mount Juliet (Kilkenny) — grands hôtels-golfs de domaine [R5-42] [R5-43] [R5-44]

**Adare Manor** (propriété de JP McManus ; exploitant Tizzard Holdings Unlimited Company) — Travel Extra, 31/07/2026, page lue : la société « operated at a loss for the financial year ending 30 December 2025 », troisième année de perte consécutive. Le rapport de l'auditeur (BDO) fait quatre pages. Aucun montant n'est public : la société est « unlimited » et, selon un résultat de recherche (EXTRAIT) [R5-52], n'est pas tenue de déposer ses comptes. Elle investit avant d'accueillir la Ryder Cup 2027. **Leçon** : un domaine-hôtel ultra-premium peut perdre de l'argent plusieurs années de suite. Il est porté par la fortune de son propriétaire, ce qui est exactement ce que le projet veut éviter.

**Mount Juliet** — Travel Extra, 29/11/2024, page lue : « recorded pre-tax profits of €9.38m in 2023 » après « a €1.7m loss in 2022 », grâce à « a €9.08m gain on shareholder loan interest write-off ». Résultat d'exploitation : « The resort's operating profits increased by 44% to €1.2m. » Le domaine a été vendu pour près de 50 M€ (Tetrarch Capital et Emmet O'Neill, vendeurs, à Tipberry Ltd, acheteur). Chiffre d'affaires (EXTRAIT, article de l'Irish Times non ouvert) : 19,47 M€ en 2023, contre 17,6 M€. ESTIMATION : marge d'exploitation ≈ 6 % (1,2 / 19,47). **Leçon** : le bénéfice affiché venait d'un **abandon d'intérêts par l'actionnaire**, et non de l'exploitation.

**Coolmore** : société privée sans comptes publics trouvés ; non traité faute de budget de recherche. INCONNU.

---

## 3. Italie

### 3.1 Castello di Reschio (Ombrie) — famille Bolza [R5-25] [R5-26] [R5-27] [R5-28]

Sources : Lampoon Magazine, « Chronicles from Reschio: 1500 Hectares of Regenerated Forest », Carlo Mazzoni, 15/08/2025 (page lue) ; site officiel reschio.com (pages d'accueil, « Own a House », « Horses », lues). L'article de Falstaff renvoie HTTP 403.

Citations et faits :
- Taille : « Reschio is a 3,700 acres private estate in the Umbrian hills » (site officiel) ; « the Reschio Estate stretches over 1,500 hectares » (Lampoon). Les deux concordent (≈ 1 500 ha). Un résultat de recherche (EXTRAIT) [R5-29] donne aussi 1 200 ha : divergence conservée.
- **Mécanisme central : vente de ruines avec projet de restauration.** Benedikt Bolza : « I have restored 31 houses to date, out of 50 existing ruins. » (Lampoon, 2025). Le domaine a attribué « one hectare of land to each » ferme, dessiné les plans de restauration et vendu les maisons avec ces plans. Les acheteurs sont liés par une clause de préemption et des contrats qui « fix both the completion date and the final cost, with penalties for delays ».
- Le site officiel : « Buying a house at Reschio may begin with a ruin or, increasingly, with a house already brought to life. » ; maisons « restored and furnished by BB for Reschio Architecture and Design Studio » ; services aux propriétaires décrits sans chiffres (« We accompany each owner with an attentive, almost invisible presence »).
- Prix : « restored farmhouses at Reschio often reach around €10 million », chiffre que l'article attribue lui-même à la presse financière et aux annonces haut de gamme. Statut : PAGE LUE, mais fiabilité faible (chiffre de seconde main).
- Hôtel : château « Restored and reopened as a hotel in 2021 » ; 36 chambres selon un résultat de recherche (EXTRAIT) [R5-29].
- **Chevaux** (site officiel, page « Horses ») : élevage de « purebred Spanish horses » lancé au début des années 2000 par le comte Antonio Bolza avec un étalon et deux poulinières de « Yeguada Candau, a renowned stable near Seville » ; environ 40 poulains nés depuis ; manège « Teatro Equestre » aux deux tiers couvert, qui sert de cinéma en plein air l'été ; cours et promenades pour les clients.
- Emploi : « Reschio employs about 230 people » (Lampoon).
- **Comptes : INCONNU** (aucun chiffre d'affaires ni résultat public trouvé ; le registre italien des entreprises est payant).

**Leçon (mécanisme le plus transposable de R5)** : le propriétaire **vend des bâtiments en ruine du domaine avec un hectare chacun**, garde la maîtrise architecturale (préemption, plans imposés, prix et délais fixes) et facture ensuite la conception, les travaux, puis les services aux propriétaires (gestion, location, hôtel, équitation). L'argent de la vente des fermes finance la restauration du cœur (château-hôtel) sans puiser dans la fortune familiale. **Limites en France** : la division et la vente de bâtiments agricoles avec terrain se heurtent au droit de préemption de la SAFER, au changement de destination (PLU, zones A et N, avis CDPENAF) et aux règles de division en lotissement. À instruire par R3 et R8 avant toute transposition.

### 3.2 Castiglion del Bosco (Toscane)

Non traité faute de budget de recherche : INCONNU. Piste : registre italien des entreprises (payant) et presse économique italienne.

---

## 4. Espagne

### 4.1 La Donaira (Serranía de Ronda, Málaga) — hôtel de 9 chambres, élevage de lusitaniens, ferme biologique [R5-30] [R5-31] [R5-32] [R5-33]

Sources : snobb.net, « La Donaira – pure luxury, pure nature and pure conscience », Karethe Linaae, 01/07/2020 (page lue) ; site officiel ladonaira.com, pages d'accueil, « Lusitanos » et « Lusitanos for sale » (lues).

- Achat et taille : « The land was purchased by the current owner in 2002 » ; domaine « situated on 1700-acres » (≈ 690 ha) (snobb, 2020). Le site parle de poulains « born on a 700-hectare farm ». Divergence modérée (≈ 690 contre 700 ha) conservée.
- Agriculture : « In 2005, 700 hectares of the land was cultivated following the biodynamic principles of Rudolf Steiner. » ; « La Dehesa Biodinámica produces 95% of what is consumed on the estate. » (snobb, 2020).
- Hébergement : « Nine unique spaces, each with soul. » (site officiel, 2026) ; en 2020 : « seven distinct guest quarters in addition to two 50-m2 yurts ».
- **Chevaux** : « 81 thoroughbred Lusitano horses » (snobb, 2020) ; « More than ninety horses live free-roaming, forming a dynamic and socially rich herd. » (site officiel, 2026). Dressage classique et compétition, éthologie (« natural horsemanship » depuis 2005), **vente de chevaux** (rubrique « Lusitanos for Sale » : étalons et hongres montés, poulinières et jeunes chevaux ; prix non publiés).
- Autres produits : spa, mariages, privatisation complète (« exclusive use »), écomarathon annuel.
- **Comptes : INCONNU** (aucun chiffre public trouvé ; registre espagnol payant).

**Leçon** : La Donaira est un **projet de passion** (plus de 90 chevaux, 9 chambres). Que l'hôtel et les ventes de chevaux couvrent le coût d'un troupeau de cette taille reste à démontrer ; sans comptes, rien ne permet de l'affirmer (HYPOTHÈSE : forte dépendance au propriétaire). C'est le modèle le plus proche du goût du propriétaire, mais **pas** une preuve de rentabilité.

---

## 5. États-Unis

### 5.1 Biltmore Estate (Asheville, Caroline du Nord) — The Biltmore Company [R5-34] [R5-35]

Source principale : fiche « Biltmore House by the Numbers » (PDF du site biltmore.com, créé le 12/02/2018, texte extrait). Statut : PAGE LUE.
- « Biltmore estate encompasses more than 8,000 acres » (≈ 3 240 ha), contre 125 000 acres à l'origine, dont 87 000 vendus à l'État fédéral (forêt de Pisgah).
- Diversification : « Antler Hill Village, which features the award-winning Winery and Antler Hill Farm; the four-star Inn on Biltmore Estate; Village Hotel on Biltmore Estate; Equestrian Center; numerous restaurants; event and meeting venues; and Biltmore For Your Home, the company's licensed products division. »
- Financement : « Biltmore does not receive any governmental funding or grants, making it one of the United States' most significant National Historic Landmarks that is preserved solely through private funding. »
- « Biltmore employs approximately 2,300 people in Buncombe County and the surrounding counties. » ; « Annual visitation to Biltmore more than 1 million » ; « Number of estate employees in 1894: 438 ».
- Propriété : « The Biltmore Company is owned by the descendants of George Washington Vanderbilt. »

Données plus récentes, vues seulement en résultat de recherche (EXTRAIT, page non lisible par l'outil) [R5-35] : rapport communautaire 2024 (exercice 2023) donnant environ **1,4 million de visiteurs**, un impact économique de 828 M$, 6 353 emplois induits et 515,4 M$ de dépenses directes.

**Chiffre d'affaires et résultat : INCONNU** (société privée, aucun compte public). Le chiffre de « plus de 250 M$ de revenus » qui circule sur des sites secondaires n'est pas vérifié et n'est pas retenu.

**Leçon** : Biltmore est l'exemple le plus abouti d'un monument privé financé sans argent public, par une **marque de destination** : vin, hôtels, restauration, produits sous licence, centre équestre intégré. Mais l'échelle (1 à 1,4 million de visiteurs, 2 300 salariés) est sans rapport avec le projet.

### 5.2 Kentucky — l'économie des étalons (exemple de Spendthrift Farm, Lexington) [R5-36] [R5-37]

Sources : TrueNicks, « Into Mischief, Vekoma Lead 2026 Spendthrift Stud Roster », 07/10/2025 ; WKYT, 01/05/2026. Statut : PAGE LUE.
- « roster of 29 stallions » pour la saison 2026. Tarifs de saillie (« stands and nurses ») : de **5 000 $** (4 étalons) à **250 000 $** (Into Mischief). Viennent ensuite Vekoma 100 000 $, Omaha Beach 75 000 $ et Yaupon 60 000 $.
- ESTIMATION (calcul sur les 27 tarifs publiés) : tarif médian **15 000 $** ; un seul étalon au-dessus de 100 000 $ ; 10 étalons sur 27 à 7 500 $ ou moins.
- Trajectoire d'un succès : « the stallion's initial stud fee was $12,500 » ; « His stud fee has climbed to $250,000 » (WKYT, citant Ned Toffey de Spendthrift). Into Mischief a dépassé 225 M$ de gains cumulés de sa descendance (TrueNicks).

**Leçon** : l'économie des étalons est un **marché où le gagnant prend presque tout**. Un étalon vedette peut changer l'économie d'un haras, mais c'est une loterie, et sa chute est brutale (voir Invincible Spirit à l'Irish National Stud, de 70 % du CA en 2017 à moins de 2 % en 2024). Ce n'est **pas** une base de revenu récurrent pour un château.

### 5.3 Wellington (Floride) — immobilier équestre adossé à un pôle de compétition [R5-38] [R5-39]

Sources : The Land Report, « Wellington Equestrian Market Jumps to $692,000 Per Acre », Cary Estes, 01/05/2023 ; Town-Crier, 05/09/2025, sur l'étude d'impact du Winter Equestrian Festival (WEF) 2025. Statut : PAGE LUE. Le PDF de l'étude d'impact (media.wellingtoninternational.com) n'a pas pu être ouvert (nom de domaine introuvable).

- Prix du foncier équestre (Wellington Land Report, courtier Brad Scherer, cité par The Land Report) : « $383,000 per acre » sur l'exercice 2019-2020, puis « $692,000 per acre » l'année précédant l'article (≈ 2022) ; « 93 transactions » pour « approximately 926 acres » et « $641 million ». Vente notable : l'International Polo Club, 160 acres, acheté 110 M$ par la fédération américaine de polo. ESTIMATION : 692 000 $/acre ≈ 1,7 M$/ha.
- WEF 2025 : « $538.2 million in economic impact » pour le comté de Palm Beach (403,6 M$ en 2024) ; « 13-week event running January through March » ; « 31,000 competitors from more than 50 countries » ; « 4,869 jobs » ; « 210,911 paid room nights » ; les dépenses liées aux chevaux « accounts for 63 percent of the total GDP impact ». Une autre source (communiqué de Wellington International, EXTRAIT) donne 536,2 M$ : divergence conservée.

**Leçon** : la valeur du foncier équestre vient du **pôle de compétition** voisin, qui attire chaque hiver des cavaliers fortunés pendant trois mois. Un château isolé ne peut pas reproduire cet effet, mais un domaine situé près d'un grand site de compétition français peut louer ou vendre des écuries saisonnières plus cher (HYPOTHÈSE, à vérifier par R6).

---

## 6. Cas d'échec détaillé : Wentworth Woodhouse

### 6.1 Wentworth Woodhouse (South Yorkshire) — maison rachetée par un trust de sauvegarde, lui-même en difficulté [R5-40] [R5-41]

Contexte (EXTRAIT de recherche, article de presse non ouvert, HTTP 403) : la maison a été vendue **7 M£** à un trust de sauvegarde (date non confirmée par une page lue), avec un besoin de réparations estimé à environ **42 M£ sur 15 à 20 ans**. À confirmer.

Comptes consolidés audités (BHP LLP) de Wentworth Woodhouse Preservation Trust (société n° 08809187, charity n° 1155374), exercice clos le 31/03/2025, déposés le 11/12/2025. Statut : PAGE LUE (PDF officiel, 49 pages). Citations exactes :
- « Total income amounted to £7,131,715 (2024: £7,242,339). Included in total income is unrestricted income of £3,200,340 (2024: £2,316,573). »
- « We did however see a significant fall in filming income, as we had no major film contract during 24/25. »
- « Total expenditure was £7,489,501 (2024: £7,259,707) resulting in net expenditure of £357,786 [...] This has therefore led to a deficit on unrestricted funds of £14,867 this year. »
- « The Trust reported an unrestricted deficit of £14,867 for the year ending 31 March 2025, with free reserves amounting to £173,908 as of the same date. »
- **Continuité d'exploitation menacée** : « The extent of required income which is still to be secured for the year to 31 March 2027 indicates the existence of a material uncertainty which may cast significant doubt on the group's and parent charitable company's ability to continue as a going concern. »
- Registre des risques : « Fundraising committee fails, costs cannot be met, Wentworth Woodhouse fails and closes. »
- Dépendance aux subventions (tableau « Grants Awarded ») : National Trust, « Core Costs » 250 000 £ ; National Lottery Heritage Fund, « Survive & Thrive » 248 220 £ ; Arts Council England 99 999 £ ; etc.
- Recette de location d'une aile à une autre fondation : « income from Landmark Trust totalling £135,000 which was received following the signing of the heads of terms agreement for the lease of South Tower ».
- Ordre de grandeur des travaux : « Our in-house team completed full repairs to two of the sash windows on the West Front, just a further 998 to go! » (page imprimée à l'envers dans le PDF, lecture attentive).
- Budget de l'exercice clos le 31/03/2026 : recettes 3,46 M£, coûts 3,43 M£, excédent prévu 21 000 £.

**Leçon** : une très grande maison sans foncier productif ni fonds de dotation vit **d'une année sur l'autre** grâce aux subventions et aux tournages. Une année sans tournage suffit à créer un déficit et un doute sur la survie. C'est l'exact contraire du modèle recherché.

---

## 7. Tableau comparatif

Devises d'origine, sans conversion. « Recettes » = turnover d'une société ou total income d'une charity. Le périmètre comptable n'est souvent **pas** celui du domaine entier (voir les notes de chaque cas).

| Domaine (pays) | Surface | Visiteurs par an | Recettes (exercice) | Résultat (exercice) | Effectif | Poids de l'immobilier locatif | Volet équestre | Statut |
|---|---|---|---|---|---|---|---|---|
| Goodwood (RU) | 11 500 à 12 000 acres (≈ 4 650 à 4 860 ha) | INCONNU | 149,3 M£ (2025) | avant impôt + 5,17 M£ (2025) ; – 0,04 M£ (2024) | 1 123 | 3,1 % du CA ; 39 % de marge du segment | courses hippiques (19 jours de courses) | PAGE LUE |
| Blenheim, fondation (RU) | parc et jardins de plus de 2 000 acres | 700 000 payants | 31,0 M£ (2024-25) | + 3,70 M£ | INCONNU (charges de personnel 12,8 M£) | loyers 0,37 M£ ; fonds dédié 21,9 M£ dont 10,6 M£ d'immeubles | accueille un concours complet international | PAGE LUE |
| Chatsworth, trust (RU) | 1 822 acres loués (≈ 737 ha) | 630 114 | 19,35 M£ (2024-25) | + 1,96 M£ avant plus-values | 170 (348 personnes en moyenne mensuelle) | revenus de placements 0,6 M£ | accueille un concours complet international | PAGE LUE |
| Burghley, trust (RU) | INCONNU | INCONNU | 17,7 M£ (2025-26) | excédent libre + 1,10 M£ | INCONNU | immobilier net 3,52 M£ | Burghley Horse Trials : 6,30 M£ de CA, 0,13 M£ de résultat d'exploitation | PAGE LUE |
| Castle Howard (RU) | 8 800 acres (≈ 3 560 ha) | 296 740 | 14,75 M£ (2024-25) | exploitation – 2,02 M£ | 236 | loyers 1,87 M£ (12,7 % du CA) | — | PAGE LUE |
| Longleat Enterprises (RU) | INCONNU | INCONNU | 33,3 M£ (2025) | net – 0,65 M£ | 584 | loyers 0,15 M£ | — | PAGE LUE |
| Highclere (RU) | 6 000 acres (≈ 2 430 ha) | INCONNU | INCONNU | INCONNU | 106 | INCONNU | société d'aliments pour chevaux | PAGE LUE (partiel) |
| Northumberland Estates, famille d'Alnwick (RU) | INCONNU | — | 18,9 M£ (2025-26) | exploitation 5,90 M£ ; dividende 5 M£ | INCONNU | foncière (activité principale) | — | PAGE LUE |
| Holkham (RU) | 25 000 acres (≈ 10 100 ha) | près d'un million (EXTRAIT) | INCONNU | INCONNU | INCONNU | agriculture passée de 70 % (1996) à « a little more than 20% » des revenus | — | PAGE LUE et EXTRAIT |
| Wentworth Woodhouse, trust (RU) | INCONNU | INCONNU | 7,13 M£ (2024-25) | – 0,36 M£ ; doute sur la continuité | INCONNU | aile louée : 0,135 M£ | — | PAGE LUE |
| Irish National Stud (IE) | INCONNU | 144 000 (2024) | 7,01 M€ (2024) | exploitation – 1,78 M€ | 74 | — | haras public : étalons, pension, ventes | PAGE LUE |
| Castle Leslie (IE) | 1 000 acres (≈ 405 ha) | INCONNU | INCONNU (« highest ever revenue ») | INCONNU (« highest ever ebitda ») | ≈ 219 (ESTIMATION) | — | 56 boxes, 300 obstacles de cross, 34 km d'allées cavalières | PAGE LUE |
| Adare Manor (IE) | INCONNU | — | INCONNU | pertes en 2023, 2024 et 2025 | INCONNU | — | — | PAGE LUE |
| Mount Juliet (IE) | INCONNU | — | 19,47 M€ (2023, EXTRAIT) | exploitation + 1,2 M€ (2023) | INCONNU | — | — | PAGE LUE et EXTRAIT |
| Reschio (IT) | ≈ 1 500 ha | — | INCONNU | INCONNU | ≈ 230 | vente de fermes en ruine : 31 restaurées sur 50, 1 ha chacune | élevage de chevaux espagnols, ≈ 40 poulains depuis le début des années 2000 | PAGE LUE |
| La Donaira (ES) | ≈ 690 à 700 ha | — | INCONNU | INCONNU | INCONNU | — | plus de 90 lusitaniens, vente de chevaux | PAGE LUE |
| Biltmore (US) | 8 000 acres (≈ 3 240 ha) | plus d'un million (2018) ; ≈ 1,4 million (2023, EXTRAIT) | INCONNU | INCONNU | ≈ 2 300 | — | centre équestre intégré | PAGE LUE et EXTRAIT |

---

## 8. Mécanismes transposables en France et limites juridiques

Classement du plus robuste au plus fragile, d'après les comptes lus. Les limites juridiques françaises citées sont celles que R5 a pu sourcer. Le cadre complet relève de R3.

**8.1 Immobilier locatif dans les dépendances et maisons du domaine (revenu récurrent)**
- Preuves : Goodwood, location immobilière 4,64 M£ de CA pour 1,81 M£ de résultat avant frais centraux (39 %) ; Castle Howard, loyers de 1,87 M£ (12,7 % du CA) ; Burghley, immobilier de placement 3,52 M£ net, soit environ 75 % des dépenses caritatives (ESTIMATION) ; Blenheim, 18 logements achetés pour le fonds dédié ; Holkham, plus de 300 maisons (EXTRAIT).
- Transposition : c'est le revenu **le plus stable et le plus rentable** de l'échantillon. À l'échelle de 50 à 300 ha, il s'agit de quelques logements dans les communs. C'est un appoint, pas l'équilibre complet.
- Limites en France : transformer une grange ou une écurie en logement, en zone agricole (A) ou naturelle (N), suppose que le PLU désigne le bâtiment. Réponse ministérielle publiée au JO le 13/09/2016 [R5-48] : « l'article L. 151-11 dispose que dans les zones agricoles, naturelles ou forestières, le règlement du plan local d'urbanisme (PLU) peut désigner [...] les bâtiments qui peuvent faire l'objet d'un changement de destination, dès lors que ce changement de destination ne compromet pas l'activité agricole ou la qualité paysagère du site. Le changement de destination est soumis, en zone agricole, à l'avis conforme de la commission départementale de la préservation des espaces agricoles, naturels et forestiers [...] et, en zone naturelle, à l'avis conforme de la commission départementale de la nature, des paysages et des sites. » S'y ajoute le risque, déjà identifié, de requalification en bail rural pour des écuries louées (contexte permanent, leçon n° 5).

**8.2 Promotion foncière et vente d'une partie du bâti (capital occasionnel, à transformer en dotation)**
- Preuves : Blenheim, 2,7 M£ reversés par l'entité de promotion foncière et 5,1 M£ de la vente du terrain « Park View » versés au fonds de restauration ; Burghley, extension urbaine « Stamford North » ; Northumberland Estates, 2,53 M£ de profits sur ventes de terrains à bâtir en 2024-25 ; Reschio, 31 fermes en ruine sur 50 restaurées et vendues avec 1 ha chacune.
- Transposition : un capital ponctuel. Il ne finance durablement le château que s'il est **placé** (fonds dédié, immeubles de rapport), comme à Blenheim et Burghley.
- Limites en France (SAFER) : réponse ministérielle publiée au JO le 28/04/2026 [R5-47] : « le droit de préemption s'exerce sur les bâtiments d'habitation, qui font partie de l'exploitation agricole, sur les bâtiments situés dans certaines zones et qui ont été utilisés pour une activité agricole au cours des cinq années précédant l'aliénation à condition de leur restituer un usage agricole ». Dans les communes littorales, la fenêtre est de vingt ans (loi n° 2019-469 du 20 mai 2019). Depuis l'arrêt de la Cour de cassation du 15/02/2024, la SAFER peut demander une révision du prix d'un bâtiment dont le changement de destination est illégal. Un article d'avocat de 2007 [R5-50] confirme le principe (bâtiments ayant conservé leur usage agricole). **Conséquence pour un montage à la Reschio** : vendre des corps de ferme du domaine expose à la préemption de la SAFER si les bâtiments ont servi à l'agriculture dans les cinq ans, et au refus du changement de destination si le PLU ne les a pas désignés. Abords de monument historique, division foncière et lotissement : non sourcés ici, à faire vérifier par R3 (INCONNU).

**8.3 Séparer le monument, la famille et le commerce**
- Preuves : à Blenheim, la fondation exploite le palais pour « a small annual rent » plus une obligation d'entretien ; à Chatsworth, la charity détient un bail sur la maison et environ 1 822 acres (bailleur non nommé dans les pages lues) ; les filiales commerciales reversent leurs profits par Gift Aid (Chatsworth House Enterprises, Burghley Horse Trials).
- Transposition : en France, un montage SCI, société d'exploitation et fondation ou fonds de dotation est envisageable. Le Gift Aid est un dispositif britannique sans équivalent identique identifié ici : la fiscalité du mécénat et la règle du loyer de marché pour le propriétaire occupant sont à étudier par R3.

**8.4 Fonds d'entretien dédié**
- Preuves : régime britannique des maintenance funds (capital bloqué six ans pour l'entretien, exonération de droits de succession) ; fonds dédié de Blenheim, 21,9 M£ avec un objectif de 45 M£ ; distribution de 133 k£ d'un maintenance fund à Blenheim.
- Transposition : l'équivalent français (fonds de dotation, convention monument historique) reste à vérifier par R3 (HYPOTHÈSE).

**8.5 Événements équestres de prestige**
- Preuves : Burghley Horse Trials, 6,30 M£ de CA, 0,13 M£ de résultat d'exploitation, 7 salariés ; Badminton, 13 salariés, compte de résultat non publié ; Chatsworth, 130 000 personnes avec la Country Fair. Plusieurs organisateurs de concours complets britanniques ont été dissous.
- Transposition : apport de notoriété, marge propre faible, des décennies pour construire l'événement, foule et bruit incompatibles avec une résidence calme (contexte, leçon n° 4). À exclure du scénario de base. Un petit concours régional reste possible en option (chiffrage par R6).

**8.6 Centre équestre intégré à une offre d'hébergement ou de résidences**
- Preuves : Castle Leslie (56 boxes, cross, séjours équestres, hôtel d'environ 70 chambres) ; Reschio (élevage de chevaux espagnols, cours et promenades) ; La Donaira (plus de 90 lusitaniens, vente de chevaux, 9 chambres) ; Biltmore (« Equestrian Center »).
- Transposition : les chevaux y sont un **argument de vente** des séjours et des maisons, jamais un centre de profit démontré. Aucun compte isolant l'activité équestre n'a été trouvé : INCONNU.

**8.7 Haras et étalons** : loterie, où le gagnant prend presque tout (Spendthrift : tarif médian de saillie de 15 000 $ contre 250 000 $ pour la vedette ; Irish National Stud : 70 % du CA en 2017 apportés par un seul étalon, moins de 2 % en 2024). À exclure du scénario de base.

**8.8 Tournages** : revenu occasionnel et volatil. Blenheim : 1,14 M£ en 2024-25 contre 0,21 M£ l'année précédente. Wentworth est en déficit faute de tournage. Burghley les juge « hard to predict ». À Highclere, Downton n'a « pas beaucoup » aidé financièrement selon la propriétaire. À ne modéliser qu'en variante haute.

**8.9 Énergie** : Blenheim (parc solaire de 7 MW sur 20 acres) et Goodwood (chaudière biomasse de 3,5 MW, dépréciée de 1,5 M£ en 2025). Ce sont surtout des outils d'autoconsommation et de baisse des coûts ; les revenus ne sont pas isolés (INCONNU). À chiffrer par R8.

**8.10 Hôtellerie** : forte intensité en capital et en main-d'œuvre, marges minces. Mount Juliet : environ 6 % de marge d'exploitation (ESTIMATION). Adare Manor : trois ans de pertes. Castle Leslie : assurance + 121,5 % et masse salariale + 19 % entre 2019 et 2023. L'hôtel de Goodwood est en recul. À chiffrer par R7.

**8.11 Agriculture** : déficitaire à Goodwood, en recul à Castle Howard, et passée de 70 % à environ 20 % des revenus à Holkham. Elle ne finance pas un château ; c'est une charge d'entretien du paysage, partiellement aidée.

---

## Contre-exemples et cas d'échec trouvés

| Domaine | Fragilité documentée | Source |
|---|---|---|
| Castle Howard | Perte d'exploitation de 2,02 M£ (2024-25) ; hébergement de loisirs et agriculture en recul ; résultat sauvé « sur le papier » par la réévaluation des immeubles | [R5-11] |
| Longleat | Perte nette de 0,65 M£ en 2025 à cause de la météo sur un événement clé ; cinq sociétés du groupe dissoutes en 2024-2026 (raisons inconnues) | [R5-12] [R5-09] |
| Goodwood | Perte de 2,6 M£ en 2024 (dépréciation immobilière de 9,5 M£) ; agriculture déficitaire deux années de suite ; dépréciation de 1,5 M£ de la chaudière biomasse en 2025 | [R5-01] |
| Blenheim | Filiale commerciale et filiale « eau » en fonds propres négatifs ; activité « eau » revendue 255 k£ ; réserves libres négatives | [R5-03] |
| Burghley | Retard d'entretien (« backlog of dilapidations ») non provisionné ; compte courant à découvert financé par l'emprunt ; revenus miniers et de tournage en déclin ou imprévisibles | [R5-07] |
| Burghley Horse Trials | Marge d'exploitation de 1 à 2 % ; fonds propres encore négatifs au 31/01/2026 (– 18 325 £) | [R5-08] |
| Irish National Stud | Pertes avant impôt d'environ 1,8 M€ par an en 2023 et 2024 (1,5 M€ en 2025), pendant le déclin des revenus de son étalon vedette | [R5-21] [R5-22] |
| Highclere | Besoin de travaux de près de 12 M£ en 2009 ; le tournage de Downton n'a « pas beaucoup » aidé financièrement selon la propriétaire | [R5-20] |
| Secteur (Historic Houses) | Retard d'entretien de 2 Md£ ; 47 % des maisons ont reporté des travaux urgents entre 2020 et 2022 | [R5-15] |
| Concours complets | Plusieurs sociétés organisatrices dissoutes (Gatcombe, Glamis, Goring Heath, Richmond) : signal, pas preuve | [R5-09] |
| Wentworth Woodhouse | Maison rachetée 7 M£ par un trust de sauvegarde (EXTRAIT ; raisons de la vente non sourcées) ; trust repreneur en déficit, réserves libres de 173 908 £, « material uncertainty » sur la continuité d'exploitation | [R5-40] [R5-41] |
| Adare Manor | Trois exercices de perte consécutifs (2023 à 2025), montants non publiés | [R5-42] |
| Mount Juliet | Perte de 1,7 M€ en 2022 ; bénéfice 2023 dû à un abandon d'intérêts de 9,08 M€ par l'actionnaire ; domaine revendu | [R5-43] |

Constat transversal : **aucun** des domaines dont les comptes ont été lus ne finance son monument par la seule billetterie. Ceux qui équilibrent leurs comptes (Burghley, Chatsworth, Blenheim, Northumberland) s'appuient tous sur un **patrimoine immobilier productif** (location ou promotion) ou sur un très grand volume de visiteurs (600 000 à 700 000). Ceux qui n'en ont pas (Wentworth Woodhouse) vivent de subventions et de tournages, avec un doute sur leur survie.

---

## Points de doute / hypothèses non vérifiées

1. **Méthode de lecture des PDF de Companies House** : ce sont des scans sans couche texte. Ils ont été téléchargés avec curl depuis le lien officiel (WebFetch ne suit pas la redirection signée), puis lus visuellement page par page. Les chiffres clés ont été recoupés entre le texte du rapport et les tableaux (Goodwood, Burghley, Castle Howard), mais une erreur de lecture d'un chiffre isolé reste possible. Le statut PAGE LUE est donc attribué à des PDF lus par cette voie et non par WebFetch.
2. **Périmètres** : la fondation de Blenheim n'est pas tout le domaine ; Chatsworth House Trust n'est pas tout le Devonshire Group ; Northumberland Estates n'inclut pas l'exploitation du château d'Alnwick ; Longleat Enterprises n'est pas le domaine entier ; Highclere Enterprises LLP n'est qu'une entité. Les comparaisons de surfaces et d'effectifs sont donc approximatives.
3. **Revenus de l'énergie, loyer Rolls-Royce à Goodwood, effectif de Blenheim, retard d'entretien chiffré de Burghley** : INCONNU.
4. **Comptes non publics** : Reschio, La Donaira, Castle Leslie, Adare Manor, Biltmore, Holkham, Highclere et Badminton (pas de compte de résultat). Aucune conclusion sur leur rentabilité n'est possible.
5. **Chiffres vus seulement en extrait de recherche** : prix de vente de Wentworth Woodhouse (7 M£) et besoin de travaux (42 M£) ; 1,4 million de visiteurs à Biltmore ; CA de Mount Juliet (19,47 M€) ; 36 chambres à Reschio ; près d'un million de visiteurs à Holkham ; rachat de parcs de caravanes par Holkham ; obligation de dépôt des comptes d'Adare Manor.
6. **Divergences conservées** : Historic Houses, « £160,000 each » (page lue) contre « £160 million » (extrait) ; Goodwood, 11 500 ou 12 000 acres et 1 123 salariés ou « over 700 employees and casual workers » ; Reschio, 1 200 ou 1 500 ha ; La Donaira, 81 chevaux (2020) ou plus de 90 (2026), 7 ou 9 hébergements ; WEF 2025, 538,2 ou 536,2 M$.
7. **Irish National Stud 2025** : la « perte d'exploitation » de 140 538 € citée par la presse est rapprochée de la perte « before taxation and depreciation » de 2024 (447 011 €). Cette équivalence de définition est déduite, pas vérifiée.
8. **Castle Leslie** : l'effectif d'environ 219 personnes est lu sur un graphique d'âges (ESTIMATION).
9. **Burghley Horse Trials** : coexistence de versements en Gift Aid à la société mère et de « distributed profits » au trust testamentaire du 6e marquis d'Exeter. Mécanisme non expliqué.
10. **Longleat** : le bénéficiaire des 3,3 M£ de loyers d'exploitation n'est pas identifié (HYPOTHÈSE : le domaine propriétaire).
11. **Droit français** : textes lus par l'intermédiaire de réponses ministérielles (2016 et 2026) et d'un article d'avocat de 2007, Légifrance étant inaccessible (403). Versions en vigueur de L. 151-11 du Code de l'urbanisme et de L. 143-1 du Code rural à confirmer par R3. Abords de monuments historiques, lotissement et division foncière : non traités (INCONNU).
12. **TVA** : les chiffres d'affaires britanniques sont en principe hors TVA (mention explicite seulement chez Burghley Horse Trials : « net of VAT »). Non vérifié pour chaque cas.
13. **Transposition d'échelle** : les domaines étudiés font de 400 ha (Castle Leslie) à 10 000 ha (Holkham), soit 2 à 200 fois S1 à S3. Les ratios (marge du locatif, coût d'entretien par jardinier, etc.) sont plus transposables que les montants.

---

## Chiffres clés pour le modèle

| Indicateur | Valeur | Unité | Année | Statut | Source |
|---|---|---|---|---|---|
| Marge du segment location immobilière, Goodwood (1,81 / 4,64) | 39 | % du CA du segment, avant frais centraux | 2025 | ESTIMATION sur PAGE LUE | R5-01 |
| Marge nette du groupe Goodwood (3,04 / 149,3) | 2,0 | % du CA | 2025 | ESTIMATION sur PAGE LUE | R5-01 |
| Résultat de l'activité agricole, Goodwood | – 118 479 (2025) ; – 861 091 (2024) | £ | 2024-2025 | PAGE LUE | R5-01 |
| Billetterie et Gift Aid de Blenheim, contre coûts du monument | 11 068 contre 16 360 (déficit – 5 292) | k£ | 2024-25 | PAGE LUE | R5-03 |
| Dépense de restauration visée par Blenheim | 4 (réalisé 2,5) | M£ par an | 2024-25 | PAGE LUE | R5-03 |
| Recettes de tournage de Blenheim | 1 140 (contre 211 l'année précédente) | k£ | 2024-25 | PAGE LUE | R5-03 |
| Entretien jardin, parc et bois de Chatsworth (jardin de 105 acres ; bail d'environ 1 822 acres de jardin, parc et bois) | 1 781 | k£ par an | 2024-25 | PAGE LUE | R5-05 |
| Personnel jardins et maintenance de Chatsworth | 29 et 32 | personnes (moyenne) | 2024-25 | PAGE LUE | R5-05 |
| Part de la billetterie dans les recettes de Chatsworth | 69 | % | 2024-25 | PAGE LUE | R5-05 |
| Revenu net de l'immobilier de placement de Burghley, contre dépenses caritatives | 3,52 contre 4,69 (≈ 75 %) | M£ | 2025-26 | PAGE LUE (ratio : ESTIMATION) | R5-07 |
| Burghley Horse Trials : CA et résultat d'exploitation | 6,30 et 0,13 (2,1 %) | M£ | 2025-26 | PAGE LUE | R5-08 |
| Castle Howard : loyers et résultat d'exploitation | 1,87 (12,7 % du CA) et – 2,02 | M£ | 2024-25 | PAGE LUE | R5-11 |
| Dépense moyenne annuelle d'entretien par maison historique britannique | ≈ 160 000 | £ par maison et par an | 2024 | PAGE LUE | R5-15 |
| Retard d'entretien moyen par maison (2 Md£ / ≈ 1 450 membres) | ≈ 1,4 | M£ par maison | 2024-25 | ESTIMATION sur PAGE LUE | R5-15, R5-16 |
| Visites moyennes par maison historique britannique | 44 500 | visites par an | 2024 | PAGE LUE | R5-15 |
| Part de l'étalon vedette dans le CA de l'Irish National Stud | 70 (2017) ; 40 (2020) ; < 2 (2024) | % | 2017-2024 | PAGE LUE | R5-21 |
| Résultat d'exploitation de l'Irish National Stud | – 1,78 sur 7,01 de CA | M€ | 2024 | PAGE LUE | R5-21 |
| Tarif médian de saillie chez Spendthrift (27 tarifs publiés) | 15 000 (de 5 000 à 250 000) | $ | 2026 | ESTIMATION sur PAGE LUE | R5-36 |
| Hausse des coûts de Castle Leslie entre 2019 et 2023 | assurance + 121,5 ; électricité + 72,38 ; masse salariale + 19 | % | 2023 | PAGE LUE | R5-23 |
| Part de l'agriculture dans les revenus de Holkham | 70 (1996) ; « a little more than 20% » (aujourd'hui) | % | 1996 et années 2020 | PAGE LUE | R5-45 |
| Fermes en ruine restaurées et vendues à Reschio | 31 sur 50, 1 ha chacune | maisons | 2025 | PAGE LUE | R5-25 |
| Dividende annuel de la foncière Northumberland Estates | 5 | M£ par an | 2024-25 et 2025-26 | PAGE LUE | R5-14 |
| Prix du foncier équestre à Wellington (Floride) | 692 000 (383 000 en 2019-20) | $ par acre | ≈ 2022 | PAGE LUE | R5-38 |
| Wentworth Woodhouse : recettes, résultat, réserves libres | 7,13 M£ ; – 0,36 M£ ; 173 908 £ | £ | 2024-25 | PAGE LUE | R5-40 |
