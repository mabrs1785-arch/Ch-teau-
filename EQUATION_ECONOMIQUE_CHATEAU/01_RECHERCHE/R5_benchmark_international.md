# R5 — Benchmark international des grands domaines (Royaume-Uni, Irlande, Italie, Espagne, États-Unis)

Agent : R5. Date de recherche : 2026-10-14. Rédaction en français, sources souvent en anglais.
Statuts : PAGE LUE (page ou PDF ouvert, citation exacte), EXTRAIT (vu dans un résultat de recherche), ESTIMATION, HYPOTHÈSE, INCONNU.
Monnaies : les montants sont laissés dans leur devise d'origine (GBP, EUR, USD) avec l'année. Aucune conversion n'est faite sauf mention explicite (ESTIMATION).

Avertissement de méthode : un domaine qui publie de gros chiffres d'affaires n'est pas forcément rentable, et la fortune d'une famille ne dit rien de la rentabilité de l'exploitation. Les comptes ci-dessous distinguent, quand la source le permet : recettes (income / turnover), résultat (surplus / profit) et trésorerie.

---

## Journal de travail (mis à jour au fil de l'eau)

- Démarrage : lecture du contexte, des règles et de la mission R5.

- Le registre officiel des charities (register-of-charities.charitycommission.gov.uk) renvoie HTTP 403 à WebFetch, et le miroir findthatcharity.uk renvoie HTTP 502. Les comptes des charities devront venir des PDF publiés par les domaines eux-mêmes ou de Companies House (beaucoup de charities sont aussi des sociétés).
- Companies House fonctionne : la recherche interne et l'historique des dépôts se lisent avec WebFetch. Les PDF de comptes sont servis par une URL S3 signée (expiration 60 s) que WebFetch ne suit pas. Ils ont donc été **téléchargés avec curl depuis le lien officiel Companies House**, puis lus page par page (ce sont des scans, sans couche texte). Statut retenu : PAGE LUE (PDF officiel ouvert et lu).

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

**Montage (p. 4)** : « The charity holds a lease of Chatsworth House and its essential contents, with approximately 1,822 acres of land including the garden, park and woodland. » Le reste du domaine appartient au « Chatsworth Settlement » (trust familial). Le personnel est « jointly employed by the charitable company and the Trustees of the Chatsworth Settlement » (p. 13).

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
- Plusieurs sociétés du groupe Longleat ont été dissoutes en 2024-2026 (Longleat Bath Arms Limited, Longleat Bishopstrow Limited, Longleat Homewood Park Limited, Longleat International Ltd, Longleat LCS Ltd) [R5-09] : activités hôtelières ou annexes abandonnées ou restructurées. Raisons : INCONNU.

**Leçon** : une attraction de masse (zoo-safari + grottes) de 33 M£ de CA et près de 600 salariés reste à la merci d'un week-end de mauvais temps sur un événement clé. Modèle hors d'échelle et contraire au souhait de calme du propriétaire.

### 1.8 Highclere Castle (Hampshire) — Highclere Enterprises LLP, n° OC305641 [R5-13]

Source : comptes « filleted » non audités de l'exercice clos le 31/03/2025, déposés le 25/03/2026, signés par le comte de Carnarvon. Statut : PAGE LUE (PDF officiel, 8 pages).

- « In accordance with section 444 of the Companies Act 2006 (as applied to LLPs), the income statement has not been delivered. » Chiffre d'affaires et résultat : **INCONNU** dans les comptes publics.
- Effectif moyen : **106** (2024 : 108). Sommes dues aux membres au titre des bénéfices : 474 274 £ (2024 : 170 657 £). Actif net 640 770 £.
- Autres entités au registre : Highclere Castle Horse Feeds Limited (2010), Highclere Castle Media Limited (2021), deux sociétés « Highclere Castle Trustee » (2025) [R5-09].
- **Effet Downton Abbey** : non chiffrable avec les comptes publics. Voir la recherche presse plus bas (§ 1.10).

### 1.9 Alnwick (Northumberland) — Northumberland Estates Limited, n° 05941545 [R5-14]

Source : comptes consolidés audités (UNW LLP) de l'exercice clos le 31/03/2026, déposés le 21/09/2026. Statut : PAGE LUE (PDF officiel, 53 pages).

- Activité (p. 1) : « The principal activity of Northumberland Estates Limited company and its group is commercial and residential property investment and development in the UK, Europe and North America. » Le château d'Alnwick lui-même (visites, tournages Harry Potter) n'apparaît pas dans ce périmètre ; son entité d'exploitation n'a pas été identifiée : INCONNU.
- « Group revenues decreased compared to prior years to £18.9m (2025: £19.6m) in the year ended 31 March 2026. »
- Compte de résultat consolidé (p. 11), en £ : CA 18 923 012 ; **résultat d'exploitation courant 5 898 755** (2025 : 9 519 993) ; plus-value de réévaluation des immeubles 37 185 820 ; profit sur ventes de terrains à bâtir 136 709 (2025 : 2 526 243) ; résultat avant impôt 38 867 991 ; résultat net 31 225 555.
- « During the year a dividend of £5,000,000 was paid (2025: £5,000,000). » (p. 4)
- Stratégie (p. 1) : « [...] maintaining a mix of assets that generate a reliable and growing income stream, and in addition, to continue its development programme to generate capital receipts and / or rental income from its own land. » ; utilisation de pierre et de bois issus des carrières et forêts du domaine (p. 3).

**Leçon** : la famille propriétaire d'Alnwick a transformé une partie de son patrimoine en **foncière diversifiée** (commerce, logement, à l'étranger aussi), qui verse 5 M£ de dividendes par an. C'est le « moteur extérieur » le plus net de l'échantillon. Mais il repose sur un capital immobilier hérité considérable, pas sur l'exploitation du château.

