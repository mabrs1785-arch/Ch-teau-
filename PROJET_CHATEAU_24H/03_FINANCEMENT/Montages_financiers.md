# Montages financiers — Opération Château (Agent 2, ingénierie financière)

Date : 2026-10-14. Sources : `_brut/sources_agent2.csv` (identifiants A2-Sxx).

## 0. Avertissements de méthode (à lire avant tout chiffre)

- **Conditions de recherche réelles** : ce jour, l'outil WebFetch était bloqué par le proxy réseau (erreur DNS sur tous les domaines, y compris Légifrance, EUR-Lex et culture.gouv.fr). Les faits ci-dessous viennent des **extraits renvoyés par le moteur WebSearch** pour les URL citées. Je n'ai donc pas lu les pages en entier. Le budget de recherche partagé entre agents (200 requêtes) a ensuite été **épuisé**. Plusieurs points demandés n'ont pas pu être sourcés : ils sont marqués **INCONNU / non vérifié ce jour**.
- Légende : **[FAIT]** sourcé (id A2-Sxx) ; **[ESTIMATION]** hypothèse explicite, avec son raisonnement ; **[INCONNU]** non trouvé, avec la méthode pour le vérifier ; **[MÉCANISME]** description juridique générale, sans chiffre et non sourcée ce jour, à faire valider par un notaire ou un avocat.
- Aucune subvention, aucun prêt et aucun intérêt d'investisseur n'est acquis. Les investisseurs cités ne sont **pas contactés**.
- Règle du contexte permanent : un EBITDA positif ne suffit pas, il faut un cash-flow positif. Chaque montage indique donc le **service de la dette annuel** que l'exploitation doit couvrir.

---

## 1. Faits de marché et de droit utiles au montage

### 1.1 Dette bancaire

| Donnée | Valeur | Statut |
|---|---|---|
| Coût moyen des nouveaux crédits bancaires aux SNF, juillet 2026 | 3,75 % (3,69 % en juin) | [FAIT] A2-S01 |
| Taux des nouveaux financements aux SNF, août 2026 | 3,73 % | [FAIT] A2-S02 |
| Avril 2026 : crédits d'équipement / crédits immobiliers aux entreprises | 3,57 % / 3,52 % | [FAIT] A2-S03 (extrait moteur) |
| Taux moyen des nouveaux crédits aux entreprises en France, juin 2026 (FBF) | 3,64 % (zone euro 3,96 %) | [FAIT] A2-S04 |
| PME, février 2026 (BdF citée par Tide) / avril 2026 (série BdF) | 3,49 % / 3,547 % | [FAIT, source secondaire] A2-S55, A2-S56 |
| Accès au crédit T1 2026 : PME obtenant la totalité ou plus de 75 % du crédit demandé | 98 % | [FAIT] A2-S05 |
| Taux directeur BCE | 2,15 % « depuis juin 2025 » selon une source commerciale, contredit par une note IEDOM qui évoque une remontée en juin 2026 | [FAIT incertain] A2-S06 |
| **Taux réellement proposé à un primo-entrepreneur de 26 ans pour un château** | 4,0–5,5 % | **[ESTIMATION]** : les moyennes ci-dessus incluent des entreprises établies. Un projet atypique, sans historique et avec un actif illiquide, paiera vraisemblablement une prime de risque. Hypothèse retenue dans les calculs : **4,5 % sur 20 ans** (murs) et **5 % sur 7 ans** (exploitation). |
| **Apport usuel exigé par les banques (murs + exploitation)** | **[INCONNU]** ce jour, aucune source consultée. **[ESTIMATION]** de travail : 20–30 % du besoin total, plutôt 30 % ou plus pour un actif atypique. | Vérification : demander en rendez-vous à 2 ou 3 banques (dont Crédit Agricole, très présent dans le rural et l'équin) leur grille « hôtellerie / immobilier d'exploitation ». Consulter aussi les publications de la Fédération bancaire française. |
| Durées usuelles | **[ESTIMATION]** murs 15–20 ans, matériel et fonds 5–7 ans | Non sourcé ce jour |
| Ratio de couverture de la dette (DSCR) exigé | **[ESTIMATION]** ≥ 1,2–1,3 | Non sourcé ce jour |

**Annuités calculées** (formule d'annuité constante) : 1 M€ sur 20 ans à 3,75 % = 71 962 €/an ; à 4,5 % = 76 876 €/an. 1 M€ sur 7 ans à 5 % = 172 820 €/an.

### 1.2 Garanties et quasi-fonds propres

- **Garantie Bpifrance** [FAIT] A2-S07, A2-S08 : création 60 % (création ex nihilo, ou intervention conjointe avec la Région), sinon 50 % ; transmission 50 %, ou 70 % si la Région intervient. La garantie couvre la banque, **pas l'emprunteur** : la caution personnelle reste en général demandée ([ESTIMATION], usage bancaire non sourcé).
- **Initiative France** [FAIT] A2-S09 : en 2019, 208 M€ de prêts d'honneur ont permis 1,6 Md€ de prêts bancaires associés. Le prêt d'honneur moyen était de 9 700 €. Le levier calculé est d'environ 7,7 (mon calcul). En 2025, le réseau a financé et accompagné 20 299 entreprises (A2-S10). Fourchette 3 000–50 000 € selon une source secondaire (A2-S11, fiabilité faible).
- **Réseau Entreprendre** [FAIT] A2-S12 : en 2024, 37 500 € de financement moyen par projet (prêt d'honneur + prêt Bpi), levier x13, 26 M€ de prêts d'honneur engagés. L'antenne de Paris annonce 15 000–50 000 € (A2-S13). Le plafond légal du prêt d'honneur est cité à 80 000 € puis 90 000 € dans la même source (A2-S11) : **contradictoire, [INCONNU]**.
- **Conséquence** [ESTIMATION] : les prêts d'honneur cumulés (2 réseaux, éventuellement 2 associés) apportent **au mieux 50–100 k€**. C'est utile comme levier sur l'exploitation, mais négligeable face à un besoin de 3–5 M€. Ces réseaux financent surtout des entreprises créatrices d'emplois, pas l'achat d'une résidence.

### 1.3 Régime fiscal des Monuments historiques (MH) et du label Fondation du patrimoine

- **Déduction des charges** (art. 156 CGI, II-1° ter) [FAIT] A2-S38, A2-S39, A2-S42 :
  - Propriétaire non occupant, immeuble ouvert au public : 100 % des charges imputables sur le revenu global.
  - Propriétaire non occupant, immeuble fermé au public : 50 %.
  - Partie occupée par le propriétaire (classé ou inscrit) : charges déductibles en totalité, ou forfait de 25 % des charges foncières (A2-S38).
  - Ouverture au public exigée : 40 jours du 1er juillet au 30 septembre, ou 50 jours par an dont 25 jours fériés du 1er avril au 30 septembre. Au moins 6 h d'ouverture effective par jour. Déclaration avant le 1er février (A2-S38).
  - Les sources divergent sur le report du déficit (A2-S38 contre Capifrance) : **à vérifier**.
- **Engagement de conservation de 15 ans** (art. 156 bis CGI) [FAIT] A2-S40 : il court à compter de l'acquisition. Les associés de SCI s'engagent aussi à conserver leurs parts 15 ans. Depuis les revenus 2014, le régime est réservé aux immeubles classés ou inscrits et aux immeubles labellisés Fondation du patrimoine. Le BOFiP consulté est en version 2018 : **à reconfirmer**.
- **Restrictions sur les sociétés** (SCI, copropriété, agrément ministériel) : **[INCONNU]** ce jour (recherche non aboutie, budget épuisé). Point crucial pour les montages OpCo/PropCo, à vérifier dans le BOI-RFPI-SPEC-30-10 en vigueur. Le régime vise l'impôt sur le revenu des personnes physiques. **[ESTIMATION]** Une PropCo soumise à l'IS ne transmet pas cet avantage aux associés.
- **Label Fondation du patrimoine** [FAIT] A2-S44, A2-S45, A2-S46 :
  - Déduction de 50 % des travaux si la subvention atteint au moins 2 %, de 100 % si elle atteint au moins 20 %.
  - Label valable 5 ans. Conservation de 15 ans.
  - Communes de moins de 20 000 habitants, zone rurale ou site protégé.
  - **Immeubles à usage commercial ou professionnel exclus.** Un domaine équestre exploité commercialement risque donc d'être inéligible pour la partie exploitée.
- **Convention Fondation du patrimoine** [FAIT] A2-S47 : ouverture au public pendant au moins 10 ans après les travaux (décret de 2008).
- **Qui en profite réellement** [ESTIMATION] : la déduction sur le revenu global n'a de valeur que pour un contribuable fortement imposé à l'IR. Un porteur de 26 ans aux revenus modestes en tire peu. Le régime **intéresse surtout un co-investisseur personne physique fortement imposé**. Il lui impose en revanche 15 ans de blocage et l'ouverture au public.

### 1.4 Subventions

- **DRAC** [FAIT] A2-S32 : taux moyens de 40 % pour un immeuble classé et 20 % pour un inscrit. Pour un inscrit, le plafond est de 40 % de la dépense (art. L.621-29 du code du patrimoine). L'assiette ne couvre que les parties protégées et se calcule TTC pour un propriétaire privé. **La subvention n'est pas un droit** : elle dépend des crédits disponibles. Une aide jusqu'à 100 % est possible par dérogation exceptionnelle pour un classé (A2-S33).
- **Régions** : exemple des Pays de la Loire, 1–20 % selon le taux de l'État, plafonné à 300 000 € sur 10 ans pour un particulier [FAIT] A2-S34. Les règles varient selon la région.
- **Loto du patrimoine / Mission Bern 2025** [FAIT] A2-S35, A2-S36 : 29,1 M€ reversés à la Fondation pour 120 lauréats (18 emblématiques et 102 départementaux). Les sites départementaux se partagent 21,4 M€, avec un plafond de 300 000 € par site. Exemple : le domaine de Plaisir (78) reçoit 155 000 € (A2-S37). La sélection est compétitive : **ne jamais budgéter**.
- **Décalage de trésorerie** [ESTIMATION] : les subventions sont en général versées sur factures acquittées, une fois les travaux réalisés. Il faut donc un **crédit-relais** ou de la trésorerie pour les préfinancer.

### 1.5 Mécénat et dons

- **Mécénat d'entreprise** (art. 238 bis CGI) [FAIT] A2-S50, A2-S51, A2-S52 : réduction d'impôt de 60 % jusqu'à 2 M€ de dons, 40 % au-delà. Plafond : 20 000 € ou 0,5 % du chiffre d'affaires HT, le plus élevé des deux. Report possible sur 5 ans. Un don à une personne physique n'ouvre pas droit à la réduction.
- **[ESTIMATION / MÉCANISME]** Une société commerciale (OpCo ou PropCo) ne peut pas recevoir de mécénat défiscalisé. Le canal possible est une **souscription Fondation du patrimoine** pour un MH privé sous convention, avec ouverture au public. Le taux de 66 % des dons des particuliers est couramment cité mais **non vérifié ce jour**.

### 1.6 Foncier agricole (GFA, SAFER)

- **GFA** (art. 793 CGI) [FAIT] A2-S53, A2-S54 : les parts sont exonérées des 3/4 des droits de mutation à titre gratuit pour les biens loués par bail à long terme, dans la limite de 500 000 € depuis la loi de finances 2023. Conditions : conservation de 5 ans, et en principe détention de 2 ans. Les statuts doivent interdire le faire-valoir direct.
- **Utilité pour le projet** [ESTIMATION] : un GFA (familial ou mutualiste) peut **porter les terres** (prairies, paddocks) séparément du château et les louer par bail rural long à l'exploitation équestre. Cela fait baisser le ticket d'acquisition du château et attire des épargnants intéressés par la transmission.
- **Points non vérifiés ce jour** : l'éligibilité des activités équestres au bail rural, les règles de la SAFER (droit de préemption, possibilité de portage) et les GFA mutualistes régionaux. Vérification : SAFER régionale, chambre d'agriculture, articles L.311-1 et L.143-1 du code rural sur Légifrance.

### 1.7 Holding et LBO

- **Régime mère-fille** [FAIT] A2-S48, A2-S49 : détention d'au moins 5 % du capital pendant 2 ans. Les dividendes sont exonérés hors quote-part de frais et charges de 5 %, soit un coût effectif d'environ 1,25 % avec un IS à 25 %. La quote-part tombe à 1 % au sein d'un groupe fiscalement intégré.
- Seuil de détention de l'intégration fiscale (couramment 95 %) : **non vérifié ce jour** (art. 223 A CGI).
- **Abus de biens sociaux** [MÉCANISME, non sourcé ce jour, à vérifier : art. L.241-3 (SARL) et L.242-6 (SA/SAS) du code de commerce] : utiliser les fonds ou les biens d'une société à des fins personnelles, contraires à l'intérêt social, est pénalement sanctionné. Concrètement :
  - Le château acheté par une filiale et **habité par le dirigeant** suppose un **loyer de marché** ou un avantage en nature déclaré.
  - L'exploitation équestre doit être **réelle et autonome** et viser un résultat.
  - Les chevaux personnels sont facturés en pension.
  - Côté fiscal, il existe aussi un risque d'« acte anormal de gestion ».

---

## 2. Base de besoin commune [ESTIMATION]

Hypothèses : prix d'acquisition de **2,5 M€** (bas de la fourchette 2–5 M€ du brief), domaine supposé non classé ou simplement inscrit, travaux de phase 1 seulement. Le chiffrage réel dépend des agents « Marché » et « Exploitation ».

| Emplois | Montant (M€) | Raisonnement |
|---|---|---|
| Prix d'acquisition | 2,50 | Hypothèse brief |
| Frais d'acquisition (droits + notaire) | 0,19 | ≈7,5 % du prix, ordre de grandeur des droits de mutation de l'ancien. **À vérifier** sur le barème départemental. |
| Travaux phase 1 (clos-couvert, mise aux normes ERP, logement) | 1,00 | Hypothèse. Un château demande souvent bien plus : à affiner avec un architecte du patrimoine. |
| Infrastructures équestres (≈30 boxes, carrière, clôtures, sellerie) | 0,35 | Hypothèse |
| Frais de lancement (marketing, recrutement, honoraires, assurances) | 0,11 | Hypothèse |
| Trésorerie et BFR (18–24 mois de montée en charge) | 0,35 | Hypothèse prudente |
| **Total** | **4,50** | |

---

## 3. Les six montages

### Montage A — Holding (S3, apport 1 M€) + PropCo/OpCo + dette bancaire classique

**Structure** [MÉCANISME] : la holding du porteur détient 100 % de la **PropCo**, une SAS ou SCI à l'IS qui achète les murs et les terres. Elle détient aussi la majorité de l'**OpCo** (SAS d'exploitation : pension, enseignement, séjours, événements). Les deux sont liées par un **bail commercial** (9 ans, loyer de marché). Ce bail donne à la banque un flux locatif identifiable et sépare le risque d'exploitation de l'actif.

| Sources | M€ | Conditions [ESTIMATION sauf mention] |
|---|---|---|
| Apport holding (capital + comptes courants) | 1,00 | Remontée de dividendes en régime mère-fille ([FAIT] A2-S48) |
| Prêt bancaire PropCo (murs + travaux) | 2,40 | 20 ans à 4,5 %, hypothèque ou privilège de prêteur de deniers |
| Prêt bancaire OpCo (équipement + lancement) | 0,50 | 7 ans à 5 %, garantie Bpifrance 50–70 % ([FAIT] A2-S07/S08) |
| Crowdlending obligataire (travaux) | 0,30 | 4 ans in fine, ≈9 % (cf. Analyse_crowdfunding.md) |
| Subvention DRAC (si inscrit : ≈20 % de 0,5 M€ de travaux éligibles) | 0,10 | **Non acquise**, versée après travaux, crédit-relais nécessaire ([FAIT] A2-S32) |
| Prêts d'honneur (personnels, réinjectés) | 0,05 | Initiative France / Réseau Entreprendre ([FAIT] A2-S09/S12) |
| Souscription ou mécénat via Fondation du patrimoine | 0,05 | Seulement si MH sous convention et ouvert au public. **Non acquis.** |
| Love money / comptes courants de proches | 0,10 | Sans dilution s'il s'agit de prêts |
| **Total** | **4,50** | |

- **Service de la dette** (années 1–4) : 184,5 k€ (PropCo) + 86,4 k€ (OpCo) + 27 k€ d'intérêts obligataires ≈ **298 k€/an**. Il faut ensuite rembourser 0,30 M€ in fine en année 4.
- **EBITDA consolidé requis** avec un DSCR de 1,25 : environ **370 k€/an** dès la stabilisation. [ESTIMATION] À comparer aux projections de l'agent « Exploitation ». Si l'EBITDA réaliste est inférieur, il faut réduire le prix ou les travaux, ou phaser.
- **Dilution** : nulle au niveau de la PropCo. Possible à l'OpCo si des business angels entrent.
- **Garanties** : hypothèque de premier rang, nantissement des parts PropCo/OpCo, caution personnelle probable du porteur, garantie Bpifrance.
- **Risque de perte de contrôle** : faible tant que les échéances sont honorées. En cas de défaut, la saisie et la vente forcée du château sont possibles.
- **Faisabilité** : la plus « bancable » des six, mais elle **suppose que la holding dispose réellement d'1 M€ libre en 2030** (voir montage E).

### Montage B — Apport 250 k€ (S2) + crédit-vendeur + phasage

**Structure** [MÉCANISME] : le vendeur, motivé (indivision successorale, bien longtemps invendu), accepte d'être payé à terme pour une partie du prix (crédit-vendeur garanti par le privilège du vendeur et une clause résolutoire). Une **vente à terme** est une variante : transfert immédiat de la jouissance, propriété ou paiement échelonnés. Un **viager occupé** est une autre variante : le vendeur âgé garde l'usage d'une aile, l'acheteur verse un bouquet et une rente. **Aucun exemple réel de viager ou de vente à terme de château n'a été trouvé ce jour : [INCONNU].** Prix retenu : 2,0 M€, en supposant une décote négociée.

| Emplois | M€ |
|---|---|
| Prix | 2,00 |
| Frais | 0,15 |
| Travaux phase 1 (réduits) | 0,60 |
| Infrastructures équestres | 0,25 |
| Lancement | 0,08 |
| Trésorerie | 0,25 |
| **Total** | **3,33** |

| Sources | M€ | Conditions [ESTIMATION] |
|---|---|---|
| Apport personnel | 0,25 | S2 |
| Prêts d'honneur | 0,05 | Faits A2-S09/S12 |
| Business angels / love money en capital OpCo | 0,15 | Dilution de l'OpCo de 20–35 % |
| Crédit-vendeur | 0,60 | 30 % du prix, 8 ans, 0–3 %, rang 2 |
| Prêt bancaire PropCo | 1,60 | 20 ans à 4,5 % |
| Prêt OpCo garanti Bpifrance | 0,35 | 7 ans à 5 % |
| Crowdlending | 0,25 | 4 ans in fine, ≈9 % |
| Préventes (pensions annuelles prépayées, séjours, événements) | 0,08 | Engagements clients à documenter |
| **Total** | **3,33** | |

- **Service de la dette** : 123,0 k€ (banque) + 75 k€ (crédit-vendeur sans intérêt sur 8 ans) + 60,5 k€ (OpCo) + 22,5 k€ (intérêts obligataires) ≈ **281 k€/an**. L'EBITDA requis est d'environ **350 k€**.
- **Honnêteté** : l'apport propre ne représente que 7,5 % du besoin, et la dette totale (2,8 M€) dépasse la valeur d'achat. **Une banque refusera probablement** sans garantie supplémentaire : caution d'un tiers fortuné ou nantissement d'actifs extérieurs. Le crédit-vendeur doit souvent être **subordonné** à la banque, ce que le vendeur refuse fréquemment. [ESTIMATION]
- **Garanties** : hypothèque bancaire de premier rang, privilège du vendeur, **clause résolutoire** (en cas d'impayé, le vendeur peut reprendre le bien : **risque majeur de perte de contrôle**).
- **Droits des investisseurs** : business angels minoritaires à l'OpCo avec pacte d'associés (sortie, préemption, bad leaver).

### Montage C — Apport 50 k€ (S1) : investisseurs propriétaires des murs, porteur exploitant

**Structure** [MÉCANISME] : une PropCo (SCI à l'IR si l'on vise le régime MH pour les associés personnes physiques, sous réserve des restrictions [INCONNUES] sur les SCI) est détenue par un **club deal** de 5 à 15 investisseurs ou par un family office. Le porteur crée l'OpCo et loue le domaine par bail commercial, ou par bail emphytéotique ou rural selon les biens. Il négocie un **droit de préférence** ou une **promesse unilatérale de vente** à prix fixé ou indexé (option d'achat). Il peut obtenir des BSA ou une « sweat equity » de 5–10 % de la PropCo, conditionnée à la performance. Il **vit sur place** au titre d'un logement de fonction loué par l'OpCo (loyer de marché).

| PropCo — emplois | M€ | PropCo — sources | M€ |
|---|---|---|---|
| Prix + frais | 2,69 | Fonds propres du club deal / family office | 1,74 |
| Travaux | 1,00 | Prêt bancaire PropCo (≈50 % de LTV) | 2,00 |
| Infrastructures équestres immobilières | 0,35 | Crowdlending | 0,30 |
| **Total** | **4,04** | **Total** | **4,04** |

| OpCo — emplois | M€ | OpCo — sources | M€ |
|---|---|---|---|
| Lancement | 0,11 | Apport du porteur | 0,05 |
| Trésorerie / BFR | 0,35 | Prêts d'honneur | 0,05 |
| | | Business angels (capital OpCo) | 0,10 |
| | | Prêt garanti Bpifrance, 7 ans | 0,16 |
| | | Préventes | 0,10 |
| **Total** | **0,46** | **Total** | **0,46** |

- **Loyer nécessaire** : la PropCo supporte 153,8 k€ d'annuité bancaire et 27 k€ d'intérêts obligataires. Les investisseurs visent, par exemple, 4 % de rendement courant sur 1,74 M€ (≈70 k€, [ESTIMATION] sans source de rendement cible). Il faut donc un **loyer d'environ 250 k€/an**, plus les charges du propriétaire. L'OpCo doit dégager un **EBITDA avant loyer d'au moins 300 k€**, auquel s'ajoute son propre prêt (27,7 k€/an).
- **Dilution** : le porteur détient 0–10 % de la PropCo et 60–80 % de l'OpCo.
- **Perte de contrôle** : **maximale sur l'actif**. Le porteur « contrôle durablement » le château seulement par le bail, qui protège le droit au renouvellement d'un bail commercial, et par l'option d'achat. En cas de conflit ou de vente de la PropCo, il peut perdre son lieu de vie.
- **Conformité au brief** : c'est la seule voie réaliste avec 50 k€ pour un actif de 2–5 M€. **Elle suppose des investisseurs qui, à ce jour, n'existent pas** (tous non contactés).

### Montage D — Rachat collectif sur le modèle Dartagnans (S1)

Référence factuelle [FAIT] A2-S19 à A2-S25 : Mothe-Chandeniers (objectif de 500 k€ atteint, puis plus de 1,6 M€ et environ 25 000 copropriétaires de 115 pays) ; Ebaupinay (416 k€ réunis sur 650 k€ à la date d'un article) ; Vibrac (1,24 M€ visés, plus de 175 k€ fin 2019). Contreparties : parts sociales, droit de vote, accès au domaine. Détails dans `Analyse_crowdfunding.md`.

| Emplois [ESTIMATION] | M€ | Sources [ESTIMATION] | M€ |
|---|---|---|---|
| Château dégradé (prix inférieur à 2 M€, moins de 50 ha probablement) | 1,00 | Parts sociales collectées auprès du public (SAS / coopérative) | 1,50 |
| Frais | 0,08 | Apport du porteur | 0,05 |
| Commission de plateforme | **[INCONNU]** | Dons via Fondation du patrimoine (si MH) | 0,10 (non acquis) |
| Travaux d'urgence | 0,50 | Subventions | 0,13 (non acquises) |
| Écuries | 0,20 | | |
| Trésorerie | 0,20 | | |
| **Total (hors commission)** | **1,98** | **Total** | **1,78**, soit un **trou de 0,20 M€** à combler par un prêt ou à réduire |

- **Remboursement** : aucun. Les parts ne sont pas rémunérées (logique de sauvegarde, non financière).
- **Contrôle** : la gouvernance appartient à la structure collective et au promoteur de la plateforme, **pas au porteur**. Le porteur pourrait être gérant ou locataire exploitant, à condition que la communauté le choisisse.
- **Compatibilité avec « vivre au milieu des chevaux »** : douteuse. L'objet de ces campagnes est patrimonial et ouvert au public, pas un domaine équestre privé.

### Montage E — Holding de reprise (LBO) puis financement du château (chemin vers S3, 2026–2031)

**Mécanisme** :
1. Une holding personnelle rachète 1 à 3 PME rentables avec une dette d'acquisition.
2. Les dividendes des filiales remontent en régime mère-fille (exonérés à 95 %, [FAIT] A2-S48) et remboursent la dette.
3. Une fois la dette désendettée, les dividendes libres financent l'apport de la PropCo château, sous forme de filiale ou de participation.
4. L'intégration fiscale (seuil de 95 % à vérifier) permet d'imputer les déficits de démarrage de l'OpCo château sur les bénéfices des PME.

**Simulation [ESTIMATION]** : la holding rachète des PME totalisant 600 k€ d'EBITDA pour 5x l'EBITDA, soit 3 M€. Elle finance 70 % par dette senior (2,1 M€ sur 7 ans à 5 % = **362,9 k€/an**) et 30 % de fonds propres (0,9 M€, **à trouver** : investisseurs ou crédit-vendeur des cédants).
- Après IS et investissements de maintien, le cash disponible des filiales pourrait être de l'ordre de **400 k€/an**. Hypothèse : 600 k€ d'EBITDA, moins ≈ 60 k€ de maintien, moins ≈ 140 k€ d'IS hors effet du levier.
- La marge après service de la dette serait donc d'environ **40 k€/an** pendant 7 ans.
- **Conclusion chiffrée** : un seul LBO de cette taille **ne libère pas 1 M€ d'ici 2030**. Il faudrait soit des PME plus grandes (≈1,5 M€ d'EBITDA cumulé), soit la revente d'une filiale avec plus-value, soit l'acceptation d'un calendrier 2033–2035.
- **Risques** :
  - Le LBO lui-même : covenants, dépendance au dirigeant, ralentissement économique.
  - L'**abus de biens sociaux** si le château sert d'abord de résidence privée (loyer de marché obligatoire, réalité de l'exploitation équestre).
  - Les banques des filiales peuvent bloquer les dividendes par covenant.
- **Avantage** : c'est le seul montage où le porteur **garde 100 % du contrôle** sans dépendre d'investisseurs patrimoniaux.

### Montage F — Location-gérance / bail avec option d'achat (S1–S2, entrée progressive)

**Mécanisme** [MÉCANISME, non sourcé ce jour] :
- Le porteur reprend en **location-gérance** l'exploitation d'un domaine équestre existant (centre équestre, pension, château-hôtel avec écuries) ou loue un domaine par bail commercial, sans acheter les murs.
- Une **promesse unilatérale de vente** (location avec option d'achat) fixe un prix d'achat exerçable dans 3 à 5 ans.
- Le propriétaire perçoit une redevance. Le porteur construit 3 ans de comptes certifiés, qui forment le dossier bancaire, puis achète vers 2030 avec un historique (retour au montage A ou B).

| Emplois [ESTIMATION] | M€ | Sources [ESTIMATION] | M€ |
|---|---|---|---|
| Dépôt de garantie / indemnité d'immobilisation de l'option | 0,05 | Apport | 0,05 (S1) à 0,25 (S2) |
| Cheptel et matériel | 0,10 | Prêts d'honneur | 0,05 |
| BFR / trésorerie | 0,10 | Prêt OpCo garanti Bpifrance | 0,15 (25,9 k€/an sur 7 ans à 5 %) |
| Lancement | 0,05 | | |
| **Total** | **0,30** | **Total** | **0,25–0,45** |

- **Avantages** : risque limité, apprentissage, et preuve de rentabilité avant l'achat.
- **Inconvénients** : il faut trouver un propriétaire qui accepte (aucun exemple réel trouvé ce jour, **[INCONNU]**). On ne contrôle pas l'actif. La redevance peut absorber la marge.
- **[ESTIMATION]** C'est le **meilleur premier pas pour S1** combiné au montage C ou E ensuite.

### Synthèse comparative

| Montage | Apport | Besoin total (M€) | Contrôle de l'actif | Service de dette / loyer annuel | Bancabilité [ESTIMATION] |
|---|---|---|---|---|---|
| A Holding + PropCo/OpCo | 1 M€ | 4,50 | Total | ≈298 k€ | Moyenne-bonne si l'EBITDA est démontré |
| B Crédit-vendeur | 250 k€ | 3,33 | Total, mais clause résolutoire | ≈281 k€ | Faible |
| C Investisseurs aux murs | 50 k€ | 4,50 | Aucun sur l'actif (bail + option) | Loyer ≈250 k€ | Dépend des investisseurs (non identifiés) |
| D Rachat collectif | 50 k€ | ≈2 | Aucun | 0 (pas de rendement) | Sans objet |
| E LBO puis château | 0 → 1 M€ | 3 + 4,5 | Total | 363 k€ (LBO) puis ≈298 k€ | Le LBO est bancable, mais l'horizon 2030 est serré |
| F Location-gérance + option | 50–250 k€ | 0,3 | Différé | Redevance (inconnue) + 26 k€ | Bonne (petit ticket) |

---

## 4. « Pourquoi un investisseur rationnel financerait-il ce projet plutôt qu'un autre ? »

**Réponse honnête : en l'état (porteur de 26 ans sans historique, actif non identifié, EBITDA non démontré), un investisseur purement financier ne le ferait probablement pas.**

Raisons :
1. **Rendement** : un prêteur obtient environ 3,75 % en moyenne sur les crédits aux entreprises (A2-S01). Le crowdlending immobilier affiche environ 11 % brut en 2025, mais avec 25–30 % de projets en retard de plus de 6 mois (A2-S28, fiabilité faible). Un loyer de château exploité sous les 5 % de rendement brut sur actif illiquide (ESTIMATION) ne rémunère pas le risque.
2. **Sûreté de l'actif** : un château est illiquide, coûteux à entretenir et a peu d'acheteurs. Sa valeur en cas de saisie est incertaine ([ESTIMATION], aucune donnée de décote de vente forcée trouvée).
3. **Risque porteur** : il n'existe aucun historique d'exploitation.
4. **Avantage fiscal MH** : il est réel (100 % de déduction si ouvert au public), mais réservé aux propriétaires personnes physiques à l'IR, avec 15 ans de blocage et l'ouverture au public (A2-S38, A2-S40). Il n'est **pas transmissible via une société à l'IS**.

**Il le ferait SAUF SI une ou plusieurs de ces conditions sont réunies :**
- **Décote d'achat démontrée** : prix nettement sous la valeur de marché ou de reconstruction, par exemple une indivision pressée ou un bien longtemps invendu. Cela crée une sûreté en capital (LTV inférieur à 50 %).
- **Sûreté de premier rang** sur l'actif, avec un bail commercial à loyer couvrant l'annuité et un garant crédible.
- **Track record** : le porteur prouve 2–3 ans d'exploitation rentable (montage F) avant de demander des fonds.
- **Avantage fiscal ciblé** : un co-investisseur fortement imposé à l'IR détient directement (ou via une structure transparente admise) une quote-part d'un MH ouvert au public.
- **Usage et dividende non financier** : séjours, pension de ses propres chevaux, chasse, événements privés. C'est la motivation typique d'un family office passionné, d'où le terme de « dividende émotionnel ». [ESTIMATION] Aucun cas réel documenté ce jour.
- **Mission patrimoniale** : la logique Dartagnans ou Fondation du patrimoine attire des donateurs, pas des investisseurs. Elle finance la sauvegarde, pas un projet de vie privée.

---

## 5. Recommandation de séquence [ESTIMATION]

1. **2026–2028** : constituer l'historique et la capacité. Deux voies, combinables :
   - Montage F (exploitation équestre en location-gérance ou bail).
   - Montage E (holding de reprise d'une PME rentable).
2. **2028–2029** : identifier un bien avec décote (agent « Marché ») et préparer le dossier MH, DRAC et Fondation du patrimoine si le bien est protégé.
3. **2030** : achat via le montage A (si la holding a dégagé l'apport) ou C (club deal + option d'achat), avec le terrain agricole porté par un GFA.

---

## Points de doute / hypothèses non vérifiées

- **WebFetch bloqué et budget WebSearch épuisé** : tous les faits reposent sur des extraits du moteur, pas sur la lecture intégrale des pages. Les textes officiels (CGI art. 156, 156 bis, 223 A, 238 bis, 200 ; règlement UE 2020/1503 art. 21 ; code de commerce L.241-3 / L.242-6) **doivent être relus sur Légifrance et EUR-Lex**.
- **Non sourcé ce jour** : apport bancaire usuel, durées, DSCR, crédit-bail immobilier et sale & leaseback (non traités faute de sources : mécanismes à documenter), viager et vente à terme de château, location-gérance, seuil de 95 % de l'intégration fiscale, restrictions SCI/agrément du régime MH, taux de 66 % des dons des particuliers, règles SAFER et GFA mutualistes.
- Les versions du BOFiP sur les MH trouvées datent de 2012–2018. Une réforme a pu intervenir depuis.
- Le taux réellement proposé au porteur (4,5 % / 5 %) est une hypothèse : les moyennes BdF portent sur des entreprises établies.
- Le prix de 2,5 M€, les 1,0 M€ de travaux et les 0,35 M€ d'infrastructures équestres sont des hypothèses de travail sans comparable. Le chiffrage des travaux est probablement **sous-estimé** pour un château.
- La simulation LBO (EBITDA de 600 k€, multiple de 5x, IS approximatif) est grossière.
- Tous les investisseurs sont **non contactés**. Aucune subvention n'est acquise.
- **Contre-exemples à garder en tête** : retards massifs du crowdfunding immobilier (A2-S28/S29), défaillance du promoteur Terlat chez WiSEED (A2-S27), campagnes Dartagnans loin d'un modèle rentable.
