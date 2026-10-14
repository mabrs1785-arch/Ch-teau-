# Montages financiers — Opération Château v2 (Agent 2, ingénierie financière)

Date : 2026-10-14. Sources : `_brut/sources_agent2.csv` (identifiants S01…S50).
Statuts : **PAGE LUE** (page ouverte et lue — via `curl` + extraction texte, car l'outil WebFetch échouait en DNS ce jour-là) / **EXTRAIT** (vu seulement dans un résultat de recherche) / **ESTIMATION** (raisonnement explicite) / **INCONNU**.

> Avertissement : aucun financeur n'a été contacté. **Aucun financeur n'a exprimé d'intérêt réel.** Tous les montants « investisseurs » ci-dessous sont des hypothèses de structure, pas des apports acquis.

---

## 0. Synthèse en 12 lignes

1. Avec **50 k€** d'apport, **aucun** montage d'acquisition en pleine propriété d'un château à 2-5 M€ n'est finançable par la dette : le CRA indique que les banques limitent le prêt à 70 % de la valeur d'achat (S04, PAGE LUE). Seuls restent des montages **sans acquisition** (bail emphytéotique, location-gérance, bail rural) ou **communautaires** (co-châtelains, dons).
2. Avec **250 k€**, l'acquisition n'est possible que si **quelqu'un d'autre porte le risque** : un vendeur (crédit-vendeur, vente à terme), des investisseurs majoritaires dans la société qui détient les murs (PropCo), ou une collectivité (bail).
3. Avec **1 M€**, un montage bancaire classique séparant les murs (PropCo) et l'exploitation (OpCo) devient **plausible** pour un projet de 4-4,5 M€. Il faut que l'exploitation génère environ **300 k€ d'EBITDAR**, c'est-à-dire avant loyer (ESTIMATION). Ce point est à valider par l'Agent 5.
4. Taux de référence : coût moyen des nouveaux crédits bancaires aux entreprises **3,66 % en août 2026** (S02, EXTRAIT). Taux moyen des nouveaux crédits aux PME en France **3,64 % en juin 2026** (S01, PAGE LUE). J'ai retenu **4,0 %** dans les montages et **5,5 %** en stress (ESTIMATION : prime de risque hôtellerie/événementiel et commission de garantie).
5. Le régime fiscal des Monuments historiques (MH) est puissant : 100 % des charges sont déductibles du revenu global si le monument est ouvert à la visite (S12). Il est en revanche **incompatible avec des investisseurs tiers dans une société à l'IS**, car il exige une détention directe ou une SCI non soumise à l'IS, familiale ou agréée, conservée 15 ans (S13, PAGE LUE).
6. Le mécénat via la Fondation du patrimoine est **exclu dès que les recettes commerciales du lieu dépassent 60 000 € HT par an**. On additionne pour cela toutes les activités, quel que soit l'exploitant, ce qui interdit de contourner la règle avec une OpCo séparée (S14, PAGE LUE). C'est un conflit majeur avec un modèle mariages/séminaires.
7. Exception utile : les MH utilisés pour une **entreprise agricole** peuvent recevoir ces dons (S14). L'activité équestre de préparation et d'entraînement est agricole depuis 2005 (S45, PAGE LUE). C'est une piste réelle, à faire valider par rescrit.
8. Crowdfunding immobilier : 20 à 25 % des projets avaient plus de 6 mois de retard au S1 2025 (baromètre Forvis Mazars cité par S23, PAGE LUE). L'investisseur rationnel a aujourd'hui peur de ce produit.
9. Le précédent le plus proche, Château Fontenay (Sarthe), a levé **690 k€ d'obligations à 7 %** sur Bricks, avec liquidité prévue le 31/01/2029 (S36, PAGE LUE). Son issue est **INCONNUE**.
10. La « holding LBO d'abord » (montage 6) ne finance **pas** un château d'ici 2031. Pendant les 7 ans du prêt, le cash libéré est faible : quelques dizaines de k€ par an pour une PME rachetée environ 1 M€ (ESTIMATION à partir des critères CRA, S04).
11. Les montages les plus crédibles sont, à mon avis, les **montages 3 (crédit-vendeur), 4 (bail emphytéotique ou location) et 1 (si apport ≥ 1 M€)**. Le montage 5 (communauté + agricole + GFA) est original mais dilue fortement le contrôle.
12. **Pourquoi un investisseur rationnel ?** Réponse courte (détail au §5) : pas pour du capital (equity) d'exploitation. Éventuellement pour une **dette senior sur des murs à LTV ≤ 50 %** (LTV = prêt / valeur du bien), pour du **foncier agricole ou forestier transmissible** (GFA), ou pour un **usage** (pension de ses chevaux, accès, événements). Le projet n'a aucun avantage financier pur face à l'immobilier coté ou à une SCPI.

---

## 1. Briques de financement vérifiées

### 1.1 Dette bancaire professionnelle

| Paramètre | Valeur | Statut / source |
|---|---|---|
| Coût moyen des nouveaux crédits bancaires aux sociétés non financières, août 2026 | 3,66 % (juillet : 3,75 %) | EXTRAIT, S02 (page BdF bloquée en 403) |
| Taux moyen des nouveaux crédits aux PME, France, juin 2026 | 3,64 % (zone euro : 3,96 %) | PAGE LUE, S01 |
| Crédits < 1 M€ / > 1 M€, août 2026 | 3,84 % / 3,54 % | EXTRAIT, S03 |
| PME ayant obtenu ≥ 75 % du crédit demandé (S2 2025) | 76 % en France | PAGE LUE, S01 |
| Critères bancaires pour une reprise de TPE par une personne physique | prêt ≤ 7 ans, prêt ≤ 70 % de la valeur d'achat, annuité ≤ 70 % du cash dégagé | PAGE LUE, S04 |
| Apport usuel en SCI patrimoniale | 10-20 % (source de courtage) | EXTRAIT, S48 (faible) |
| Durées normatives Bpifrance | travaux sans hypothèque 7 ans, **avec hypothèque 15 ans** | PAGE LUE, S06 |

**Apport et LTV réalistes pour un château à vocation commerciale** (ESTIMATION) : les sources lues ne donnent aucun barème « château » ou « hôtellerie ». J'en déduis qu'un projet de domaine événementiel ou équestre sera traité comme un actif d'exploitation spécialisé, peu liquide. Je retiens donc :
- un apport de **25 à 35 %** du coût total ;
- une **LTV de 50 à 65 %** sur la valeur d'expertise ;
- une durée de **15 ans** (20 ans au mieux sur les murs) ;
- une **caution personnelle** et une **hypothèque de 1er rang**.

À vérifier par 3 consultations bancaires (méthode au §7).

### 1.2 Garantie Bpifrance (elle protège la banque, pas l'emprunteur)

Source : webinaire Bpifrance Création de février 2025 (S06, PAGE LUE).
- **Prêts ≤ 200 k€** : contrat de garantie, quotité **jusqu'à 70 %** (fixe), commission selon barème.
- **Prêts > 200 k€** : garantie notifiée, quotité **jusqu'à 80 %** (modulable).
- **Cautions personnelles limitées à 50 %**, résidence du dirigeant protégée.
- Commissions dans les exemples (taux de 4 %) : **0,55 % à 1,02 %**. La « garantie verte » coûte 20 à 30 % de moins.
- Garanties spécifiques plafonnées à **50 k€ de montant garanti** pour la création/reprise, commission 2,5 %. La Garantie Égalité Accès vise notamment les jeunes de moins de 26 ans ; l'entrepreneur en a 26, éligibilité INCONNUE.

Un blog d'expertise comptable situe la quotité à **40-70 %** et précise : « La garantie n'a pas d'intérêt dans tous les cas » quand l'actif est un immobilier revendable (S07, PAGE LUE).

**Point de doute** : je n'ai pas pu vérifier si l'activité de location immobilière pure (une PropCo/SCI) est exclue de la garantie Bpifrance. En pratique, la garantie concernera surtout l'**OpCo**, c'est-à-dire la société d'exploitation (INCONNU, à vérifier sur bpifrance.fr ou auprès d'un chargé d'affaires).

### 1.3 Quasi-fonds propres personnels

| Outil | Montant | Statut |
|---|---|---|
| Prêt d'honneur Initiative France | taux 0, sans garantie, **montant moyen 10 000 €** | PAGE LUE, S09 |
| Prêt d'honneur Création-Reprise Bpifrance (via Initiative France ou Réseau Entreprendre) | **1 000 à 80 000 €**, taux 0, 1 à 7 ans, différé 0-24 mois, au plus 1/3 du total des financements (50 % en reprise) | PAGE LUE, S08 |
| Réseau Entreprendre | aucun montant affiché sur l'accueil | PAGE LUE, S10 → montant INCONNU |

Ordre de grandeur pour le montage : **30 à 100 k€** de prêts d'honneur cumulés (ESTIMATION). Cela fait levier sur la dette bancaire, mais pèse peu face à 2-5 M€.

### 1.4 Crédit-bail immobilier, cession-bail (sale & leaseback), PropCo/OpCo

- **Crédit-bail immobilier Bpifrance** : il couvre **100 % de l'investissement immobilier, frais compris**. Durée **8 à 15 ans**, loyers constants ou dégressifs. L'entreprise devient propriétaire **pour un montant symbolique** en fin de contrat (S11, PAGE LUE).
  - Pour un château : c'est le crédit-bailleur qui achète, donc il regardera la **revendabilité**. Probabilité d'accord pour un château + événementiel : **faible à moyenne** (ESTIMATION, aucun cas réel trouvé).
  - Plus réaliste pour une **construction neuve d'écuries ou d'un manège** sur le domaine.
- **Cession-bail (sale & leaseback)** : vendre les murs une fois restaurés à un investisseur et les relouer par bail commercial. Cela libère du capital mais **fait perdre la propriété**. Utile comme **sortie** du montage 1 (refinancement), pas comme entrée. Aucun cas « château » documenté dans mes sources (INCONNU).
- **PropCo/OpCo et bail commercial** :
  - La PropCo (SCI) détient les murs, l'OpCo (SAS) exploite et paie un loyer.
  - Le bail commercial apporte au locataire un droit au renouvellement et une durée de 9 ans (règle du code de commerce connue ; la page service-public consultée renvoyait une 404, donc **non vérifié aujourd'hui**).
  - Intérêt : la banque prête aux murs sur un **loyer contractuel**, et la résidence privée reste dans la PropCo.
  - **Attention** : le loyer doit être soutenable par l'OpCo, sinon le montage est circulaire. C'est le fondateur qui paie le fondateur.

### 1.5 Fiscalité Monuments historiques et patrimoine

| Règle | Contenu | Statut |
|---|---|---|
| CGI art. 156 II-1° ter et ann. III art. 41 F | MH sans recettes : charges déductibles du **revenu global** à **100 % si ouvert à la visite, 50 % si fermé**. Un excédent ne crée pas de déficit reportable. Réservé aux propriétaires qui **s'en réservent la jouissance** | PAGE LUE, S12 |
| MH avec recettes (loué, non occupé) | imputation sur le revenu foncier, avec un déficit imputable sur le revenu global selon le régime spécial | PAGE LUE, S13 (renvoi au BOI-RFPI-SPEC-30-20) |
| CGI art. 156 bis (depuis 2009) | conserver **15 ans**. **Détention directe**, ou **SCI non soumise à l'IS** agréée ou dont les associés sont **membres d'une même famille**. Pas de copropriété sauf agrément | PAGE LUE, S13 |
| Label Fondation du patrimoine (immeuble sans recettes) | déduction de **50 %** des travaux éligibles, **100 %** si subventionnés à ≥ 20 % | PAGE LUE, S12 |
| Subvention de la Fondation liée au label | **au moins 2 %** des travaux | EXTRAIT, S19 |
| Dons à la Fondation pour un MH privé (art. 200 et 238 bis f) | **exclus en cas d'exploitation commerciale**. Tolérance : recettes commerciales ≤ **60 000 € HT/an**, toutes activités du lieu et de ses dépendances additionnées **« sans qu'il soit tenu compte de la personnalité juridique de l'exploitant »**. Sont exclues du calcul : la billetterie imposée en revenus fonciers, les souvenirs et 6 manifestations de bienfaisance. **Exception : MH utilisé pour une entreprise agricole.** Conservation **10 ans** après les travaux. **Si l'immeuble est détenu par une société, les associés doivent aussi conserver leurs titres 10 ans.** Ouverture au public des parties restaurées : **50 jours/an** (dont 25 jours non ouvrables d'avril à septembre) **ou 40 jours** en juillet-septembre, pendant 10 ans. Doctrine « en vigueur du 12/09/2012 à aujourd'hui » | PAGE LUE, S14 |
| Mécénat d'entreprise (238 bis) | **60 %** du don, plafond **20 000 € ou 0,5 % du CA**, report sur 5 ans. Particuliers : 66 % (20 % du revenu imposable). IFI : 75 % jusqu'à 50 000 € | PAGE LUE, S16 |
| Mission Patrimoine (Loto, « Mission Bern ») | aide **plafonnée à 300 000 € par site**, en complément des aides publiques. Édition 2025 : 29,1 M€ au total. Exemple : Château d'Escorolles (15) 230 000 € | PAGE LUE, S17 |
| Mission Patrimoine, éligibilité | édifices bâtis, parcs, jardins. Le propriétaire candidate ou délègue | PAGE LUE, S18 |
| Subventions DRAC (travaux sur MH classés ou inscrits) | taux et plafonds 2026 **INCONNUS** (non vérifiés) | à vérifier auprès de la DRAC de la région cible |
| GFA, transmission (art. 793 / 793 bis) | exonération de **75 %** jusqu'à **300 000 €** (seuil relevé par la loi de finances 2019), 50 % au-delà, si bail à long terme | PAGE LUE, S20 |
| SAFER | droit de préemption sur le foncier agricole (règle connue, **page non chargée** aujourd'hui) | INCONNU dans le détail, à vérifier sur safer.fr |

**Conséquence structurante** (déduction de S13 et S14) : le cumul **MH à 100 % + investisseurs tiers + événementiel > 60 k€** est impossible. Il faut choisir l'un des trois profils suivants :
- **(a) Patrimonial familial** : SCI à l'IR, famille, MH ouvert à la visite, peu de commercial.
- **(b) Commercial** : société à l'IS, investisseurs, événementiel, sans avantage MH sur le revenu global. Les subventions de travaux restent possibles.
- **(c) Agricole et équestre** : exploitation agricole dans des MH, ce qui préserve l'éligibilité au mécénat (S14), avec un événementiel plafonné.

### 1.6 Holding de reprise (LBO) : remontée de cash

- **Régime mère-fille** (S15, PAGE LUE) : les dividendes reçus sont exonérés, sauf une **quote-part de frais et charges de 5 %**, ramenée à **1 %** dans un groupe fiscalement intégré.
- **Intégration fiscale** : elle exige une détention de **95 %** (S15 et résumé de recherche). Elle permet d'imputer les intérêts de la dette d'acquisition de la holding sur le résultat de la cible.
- **Contraintes bancaires** (S04) : 7 ans, ≤ 70 % du prix, annuité ≤ 70 % du cash dégagé. Autrement dit, **au moins 70 % du cash libre de la cible sert à rembourser** pendant 7 ans.
- **Prix demandés** (S05, PAGE LUE ; ce sont des prix demandés, pas conclus) : valeur demandée de 39 à 48 % du CA dans 3 annonces CRA. Le CRA 2023 donne des ratios valeur demandée / CA de 51 % (bâtiment) à 87 % (services) en 2022 (S04).
- **Apport des repreneurs** : 60 % disposent de **100 à 500 k€**. En dessous de 100 k€, le CRA « conseille d'ouvrir la recherche vers le monde de la franchise » (S04, PAGE LUE).

---

## 2. Mécanismes alternatifs d'acquisition ou de contrôle (sans prix de marché vérifié)

| Mécanisme | Principe | Intérêt pour le projet | Limite | Statut |
|---|---|---|---|---|
| **Crédit-vendeur** | le vendeur accepte d'être payé en partie à terme, avec privilège du vendeur et/ou clause résolutoire | réduit le besoin bancaire initial | le vendeur doit accepter le risque. La banque des travaux exigera de passer en 1er rang (subordination) | ESTIMATION (mécanisme connu, aucun cas château chiffré trouvé) |
| **Vente à terme** | transfert de propriété différé ou paiement échelonné sans rente viagère | idem, adapté à un vendeur âgé qui veut un revenu | prix souvent majoré | ESTIMATION |
| **Viager** | bouquet + rente jusqu'au décès du crédirentier. En viager **occupé**, le vendeur reste dans les lieux | prix d'entrée faible | **viager occupé ≈ incompatible avec « y vivre en 2030 »**, sauf partage des lieux. Exemple réel : domaine valorisé **7 000 000 €**, acquisition possible avec **2 500 000 € d'apport + rente** (viager **libre**) | PAGE LUE, S39 |
| **Location-gérance** | on loue le fonds de commerce d'un château-hôtel ou d'un lieu de réception existant | apport minimal, test du marché | aucune propriété, durée courte | ESTIMATION |
| **Location avec option d'achat / promesse unilatérale de vente** | bail de 3 à 7 ans + option d'achat à prix fixé, une partie des loyers venant en déduction du prix | laisse le temps de prouver le modèle et de constituer l'apport | rare. Le propriétaire doit attendre. Prix fixé d'avance | ESTIMATION |
| **Bail emphytéotique (privé ou administratif)** | droit réel de 18 à 99 ans, hypothécable, le preneur restaure et exploite | contrôle long sans achat | cahier des charges public, risque politique | PAGE LUE (exemples S40-S42) |
| **Bail rural (statut du fermage)** sur les terres | une activité équestre agricole peut relever du bail rural | sécurise **le foncier des chevaux** sans l'acheter | propriétaire distinct. Contrôle des structures, SAFER | PAGE LUE, S45 (qualification agricole) |

---

## 3. Projet de référence pour les montages (ESTIMATION à remplacer par les données des Agents 1, 3, 4 et 5)

| Emplois — cas central | Montant |
|---|---|
| Prix du château + environ 50 ha (cas central de la fourchette 2-5 M€) | 2 500 000 € |
| Frais d'acquisition (droits de mutation + notaire ≈ 7,5 %, ESTIMATION) | 190 000 € |
| Travaux bâti phase 1 (clos-couvert, mise aux normes ERP, résidence privée) | 900 000 € |
| Équipements équestres (écuries, carrière, paddocks) | 300 000 € |
| Lancement (mobilier, marketing, pré-ouverture) | 200 000 € |
| Trésorerie de démarrage (12 mois de pertes et BFR) | 300 000 € |
| **Total** | **4 390 000 €** |

Le cas haut (prix de 5 M€ et 2,5 M€ de travaux) double les besoins ; aucun montage à apport ≤ 250 k€ n'y résiste. Le cas bas (prix de 2 M€ et travaux limités) rend le montage 1 accessible avec environ 700-800 k€ d'apport.

---

## 4. Les six montages chiffrés

Convention : les annuités sont des remboursements constants, calculés au taux de 4,0 % (stress à 5,5 %). Toutes les répartitions sont des **ESTIMATIONS**.

### Montage 1 — PropCo/OpCo bancaire classique (apport 1 M€)

**Structure.**
- **PropCo** : SCI à l'IR détenue par le fondateur (et sa famille). Elle détient le château et les terres et peut utiliser le régime MH sur la partie résidence si le monument est protégé.
- **OpCo** : SAS détenue à 100 % par le fondateur. Elle exploite l'équestre et l'événementiel via un **bail commercial** sur les dépendances.
- La résidence privée reste dans la PropCo.

| Sources | Montant | Emplois | Montant |
|---|---|---|---|
| Apport fondateur → PropCo | 900 000 € | Prix + frais | 2 690 000 € |
| Prêt hypothécaire PropCo, 20 ans, 4 % | 2 400 000 € | Travaux bâti | 900 000 € |
| Subventions travaux (DRAC, Région, Fondation du patrimoine — **non acquises**) | 290 000 € | | |
| Apport fondateur → OpCo | 100 000 € | Équipements équestres | 300 000 € |
| Prêts d'honneur (personnels, apportés en compte courant) | 50 000 € | Lancement | 200 000 € |
| Prêt OpCo garanti Bpifrance (≤ 70-80 %), 7 ans | 350 000 € | Trésorerie | 300 000 € |
| Crédit-bail mobilier / matériel équestre | 150 000 € | | |
| Acomptes clients (mariages réservés d'avance) | 150 000 € | | |
| **Total** | **4 390 000 €** | **Total** | **4 390 000 €** |

- **Service de la dette.** Annuité PropCo **176 596 €/an** (200 830 € à 5,5 %). Annuité OpCo **58 313 €/an** sur 7 ans.
  - La PropCo a donc besoin d'un loyer d'au moins environ **190-200 k€/an**, assurance et taxe foncière comprises.
  - L'OpCo doit dégager un **EBITDAR ≥ 300 k€** pour payer ce loyer, son propre prêt et une réserve (ESTIMATION).
- **Dilution** : 0 %.
- **Garanties** :
  - hypothèque de 1er rang sur le château ;
  - caution personnelle (limitée à 50 % sur la partie garantie Bpifrance, S06) ;
  - nantissement du fonds de l'OpCo.
- **LTV** : 2,4 M€ / environ 3,4 M€ de valeur post-travaux = environ **70 %**, ce qui est **trop élevé** pour un actif spécialisé (ESTIMATION). Une banque demandera probablement un apport supplémentaire de 300-500 k€, ou une durée plus courte.
- **Perte de contrôle** : **aucune tant que la dette est servie**. Le risque est la **saisie** : en cas de défaut, la banque réalise l'hypothèque et le fondateur perd tout, y compris sa résidence.
- **Faisabilité par apport** :
  - 50 k€ : ✗ ;
  - 250 k€ : ✗ ;
  - 1 M€ : **◐ plausible** si l'Agent 5 démontre l'EBITDAR et si la banque accepte une LTV de 60-65 %.

### Montage 2 — Club deal : investisseurs majoritaires dans la PropCo, fondateur opérateur (apport 250 k€)

**Structure.**
- **PropCo** : SAS à l'IS, capitalisée par 5 à 15 investisseurs privés (family offices, entrepreneurs cavaliers). Le régime MH est **perdu**, puisque la société est à l'IS et non familiale (S13).
- **OpCo** : 100 % fondateur, bail commercial de 9 ans sur l'ensemble des activités.
- Résidence du fondateur : **bail d'habitation** consenti par la PropCo (loyer de marché), ou logement de fonction de l'OpCo.

| Sources PropCo | Montant | Emplois PropCo | Montant |
|---|---|---|---|
| Fonds propres investisseurs (**non acquis**) | 1 640 000 € | Prix + frais + travaux bâti | 3 590 000 € |
| Fonds propres fondateur | 150 000 € | | |
| Dette bancaire 20 ans (LTV ≈ 50 %) | 1 800 000 € | | |
| **Total** | **3 590 000 €** | | |

OpCo (800 k€) : apport fondateur 100 k€ + prêts d'honneur 80 k€ + prêt garanti Bpifrance 350 k€ + crédit-bail 120 k€ + acomptes 150 k€.

- **Service de la dette PropCo** : **132 447 €/an** (150 623 € à 5,5 %).
- **Rendement investisseurs.** Loyer OpCo supposé de 200 k€ (5,6 % du coût, ESTIMATION). Après annuité, il reste environ 50-65 k€/an de cash pour les actionnaires de la PropCo, soit **environ 3 %** sur 1,79 M€. Le reste du rendement dépend d'une **plus-value hypothétique** sur un actif peu liquide. **Ce rendement est insuffisant** face à une SCPI ou à de la dette privée.
- **Ce que le fondateur peut offrir pour compenser** (ESTIMATION) :
  - un intéressement au résultat (« promote ») de 20 % de la plus-value au-delà d'un TRI de 6 % ;
  - des **droits d'usage** (pension de chevaux, X nuitées, événements privés) ;
  - une **option d'achat** progressive du fondateur sur les actions de la PropCo, à valeur d'expertise.
- **Dilution** : le fondateur détient **≈ 8 % de la PropCo** (+ promote) et 100 % de l'OpCo.
- **Droits des investisseurs** (ESTIMATION) : majorité au conseil, veto sur dette et cession, clause de sortie forcée (drag-along) après 10-12 ans, information trimestrielle.
- **Perte de contrôle : ÉLEVÉE.** Les investisseurs majoritaires peuvent vendre le château. Le bail commercial protège l'**exploitation** (droit au renouvellement), mais **pas la résidence du fondateur**. C'est l'opposé de l'objectif « posséder ou contrôler durablement ».
- **Faisabilité** :
  - 50 k€ : ◐ (avec moins de parts) ;
  - 250 k€ : ◐ ;
  - 1 M€ : ✓ (fondateur à ≈ 40 %).
  - Condition commune : **trouver les investisseurs**. Aucun n'est identifié avec un intérêt réel.

### Montage 3 — Crédit-vendeur ou vente à terme + phasage des travaux (apport 250 k€)

**Cible** : un château en vente depuis longtemps, avec un vendeur âgé ou une succession qui cherche un revenu plutôt qu'un capital immédiat. L'Agent 1 doit identifier des annonces anciennes ou des baisses de prix successives.

| Sources | Montant | Emplois | Montant |
|---|---|---|---|
| Apport fondateur | 250 000 € | Prix | 2 500 000 € |
| Prêts d'honneur | 80 000 € | Frais | 190 000 € |
| Prêt bancaire 15 ans (acquisition partielle + travaux) | 750 000 € | Travaux phase 1 (sécurisation + résidence + écuries minimales) | 600 000 € |
| **Crédit-vendeur 12 ans à 3 %** (privilège du vendeur subordonné à la banque, **à négocier**) | 1 500 000 € | Équipements équestres minimaux | 150 000 € |
| Obligations OpCo via une plateforme agréée PSFP (type Fontenay/Bricks, 7-9 %, 5 ans) | 500 000 € | Lancement | 150 000 € |
| Prêt OpCo garanti Bpifrance 7 ans | 350 000 € | Trésorerie | 300 000 € |
| Subventions (non acquises) | 60 000 € | Travaux phase 2 (années 3-6, autofinancés) | (hors total) |
| **Total** | **3 490 000 €** | **Total** | **3 890 000 €** → **écart de 400 k€** |

**Constat honnête : le montage ne boucle pas** au cas central sans l'une des 3 solutions suivantes :
- une **baisse de prix** de 15 % (2,1 M€) ;
- un crédit-vendeur porté à 1,9 M€ ;
- la suppression de la trésorerie de démarrage, ce qui serait dangereux.

**Charges annuelles** : crédit-vendeur 150 693 € + banque 67 456 € + prêt OpCo 58 313 € + intérêts obligataires 40 000 € (remboursement in fine de 500 k€ à 5 ans) = **≈ 316 k€/an**, puis un mur de remboursement de **500 k€ en année 5**.

- **Dilution** : 0 %. Les obligataires n'ont aucun droit de vote.
- **Garanties** : privilège du vendeur + clause résolutoire, hypothèque bancaire, sûretés éventuelles pour les obligataires (**pas de garantie = sous-investissement**, S27 : « les obligations ne sont pas garanties »).
- **Perte de contrôle : MOYENNE.** La clause résolutoire du vendeur permet de **reprendre le château** en cas d'impayé, y compris après des travaux financés par le fondateur. Il faut négocier un plafonnement de cette clause et un délai de grâce.
- **Faisabilité** :
  - 50 k€ : ✗ ;
  - 250 k€ : **◐ (dépend entièrement d'un vendeur coopératif)** ;
  - 1 M€ : ✓ (moins de crédit-vendeur).

### Montage 4 — Bail emphytéotique ou location longue d'un château public, ou d'un domaine équestre public (apport 50-250 k€)

**Précédents réels** :
- **Villa Valmer** (Marseille) : bail emphytéotique de **60 ans** à une SAS hôtelière, résilié en 2022 puis rétabli par médiation (S40, PAGE LUE).
- **Château de Gaillon** : l'État le confie à une agglomération pour **99 ans** par bail emphytéotique administratif de valorisation, entre personnes publiques (S42, PAGE LUE).
- **Château de la Poupée / Lacroix-Laval** : la Métropole de Lyon a lancé une consultation d'opérateurs, en refusant « de privatiser ce lieu de 5 000 m² ou d'en faire un hôtel » (S41, PAGE LUE).
- **Haras des Bréviaires** : cédé **2 430 000 €** à un repreneur de la filière (S43, EXTRAIT).
- **Haras du Pin** : débat sur une « privatisation » (S44, PAGE LUE).

Ces exemples montrent que **des sites équestres publics changent d'opérateur**, mais rarement en faveur d'un particulier.

| Sources | Montant | Emplois | Montant |
|---|---|---|---|
| Apport fondateur | 50 000 € → 250 000 € | Droit d'entrée / redevance capitalisée | INCONNU (0 à quelques centaines de k€) |
| Prêts d'honneur | 80 000 € | Travaux à la charge du preneur | 1 500 000 € |
| Prêt bancaire 15 ans garanti par hypothèque **du droit réel emphytéotique** (si autorisé par le bailleur public) | 900 000 € | Lancement | 300 000 € |
| Obligations ou prêts participatifs (PSFP) | 400 000 € | Trésorerie | 200 000 € |
| Subventions mobilisées **par le propriétaire public** (Mission Patrimoine ≤ 300 k€, S17 ; DRAC) | 300 000 € | | |
| Prêt OpCo garanti Bpifrance | 270 000 € → 70 000 € | | |
| **Total** | **2 000 000 €** | **Total** | **2 000 000 €** |

- **Annuité bancaire** : **80 947 €/an** (89 663 € à 5,5 %), plus la redevance (INCONNUE).
- **Dilution** : 0 %. **Propriété : jamais.** **Contrôle : 50-99 ans**, encadré par un cahier des charges.
- **Garanties** : hypothèque sur le droit au bail, caution.
- **Perte de contrôle** : par **résiliation** pour manquement au cahier des charges ou par alternance politique (cas Valmer). En fin de bail, les améliorations reviennent au bailleur.
- **Atout** : coût d'entrée environ 2 fois plus faible que l'achat. Le château lui-même reste éligible aux subventions que porte le propriétaire public.
- **Faisabilité** :
  - 50 k€ : **◐** ;
  - 250 k€ : **◐/✓** ;
  - 1 M€ : ✓.
  - Facteur limitant : **trouver un site** avec château + 50 ha + vocation équestre + résidence possible. Aucun appel à projets actif n'a été trouvé aujourd'hui (INCONNU, veille à mettre en place sur les sites des départements, de l'IFCE et des Domaines).

### Montage 5 — « Domaine en communauté » : SAS de co-châtelains + exploitation agricole équestre + GFA (apport 50 k€)

**Principe**, inspiré de Dartagnans et de La Mothe-Chandeniers, mais avec un fondateur exploitant :
- **SAS Château** : capitalisée par des milliers de petits actionnaires, 50 € à quelques milliers d'euros.
  - Précédents : **La Mothe-Chandeniers**, prix 500 k€, plus de **1,6 M€** réunis auprès de près de **25 000** copropriétaires (S33-S34, PAGE LUE).
  - **Château du Theil** : environ **1 M€** apporté par environ **300 actionnaires**, mise de base 100 €, contrepartie un accès gratuit à vie (S35, PAGE LUE).
- **GFA** : détient les 50 ha, financé par des investisseurs patrimoniaux qui cherchent l'exonération de 75 % jusqu'à 300 000 € par bénéficiaire (S20). Il loue les terres par **bail rural à long terme** à l'**EARL ou SAS agricole équestre du fondateur**. L'équestre est une activité agricole (S45), donc le fondateur obtient un **contrôle d'usage de 18-25 ans** très protégé.
- **Événementiel** limité à **60 000 € HT/an** de recettes commerciales sur le site, pour conserver l'éligibilité aux **dons défiscalisés** via la Fondation du patrimoine (S14). Sinon on renonce aux dons.
- Deux contraintes supplémentaires si la SAS reçoit ces dons (S14) :
  - **tous les associés** doivent conserver leurs titres 10 ans, donc aucune liquidité pour les co-châtelains ;
  - les parties restaurées doivent être ouvertes au public 40 à 50 jours par an.

| Sources (cas 50 k€) | Montant | Emplois | Montant |
|---|---|---|---|
| Campagne d'actions de la SAS Château (règles PSFP si offre au public, ≤ 5 M€/12 mois, S21-S22) | 1 500 000 € (**non acquis**) | Château (prix hors terres, ESTIMATION) | 1 800 000 € |
| Parts de GFA (investisseurs patrimoniaux) | 700 000 € (**non acquis**) | 50 ha de terres + frais | 750 000 € |
| Dons via la Fondation du patrimoine (si éligible) + Mission Patrimoine | 400 000 € (**non acquis**) | Frais d'acquisition château | 140 000 € |
| Prêt bancaire SAS Château 15 ans | 600 000 € | Travaux phase 1 | 900 000 € |
| Apport fondateur + prêts d'honneur → exploitation agricole | 130 000 € | Équipements équestres (exploitation) | 300 000 € |
| Prêt bancaire / MiiMOSA → exploitation agricole | 400 000 € | Lancement + trésorerie | 330 000 € |
| **Total** | **3 730 000 €** | **Total** | **4 220 000 €** → écart de 490 k€ (phasage obligatoire) |

- **Annuité SAS Château** : 53 965 €/an (600 k€ sur 15 ans).
- **Dilution** : fondateur **< 5 %** de la SAS Château. La **gouvernance** doit être verrouillée par des **actions de préférence** et des statuts (président désigné, droits de vote plafonnés). C'est faisable en SAS, mais la contestation est probable.
- **Droits des contributeurs** : actionnaires sans dividende attendu, droits d'usage (visites, accès), assemblée générale. La Mothe prévoyait un conseil, une AG annuelle et un comité exécutif (S34).
- **Contrôle** : le fondateur **ne possède pas** le château. Il contrôle l'**usage des terres** via le bail rural et l'**exploitation**, et peut être **président** de la SAS. Sa résidence privée doit être prévue dans les statuts ou par un bail, ce qui crée un conflit d'intérêts visible pour les co-châtelains.
- **Faisabilité** :
  - 50 k€ : **◐ (seul montage d'acquisition accessible à 50 k€)** ;
  - 250 k€ : ◐ ;
  - 1 M€ : ✓.
  - Risque principal : la **collecte**, car Dartagnans a des années de marque et de communauté, et une commission d'environ 8 % (S37).

### Montage 6 — Séquentiel : holding de reprise 2026-2030, château 2030-2031 (apport 250 k€ → 1 M€)

**Étape 1 (2026-2027).** Rachat d'une PME rentable par la holding (exemple ESTIMATION) :
- prix **1 000 000 €** (cible d'environ 1,7-2,2 M€ de CA d'après les ratios CRA, S04-S05) ;
- financement : 250 k€ d'apport + 50 k€ de prêts d'honneur (via Initiative/Réseau Entreprendre, plafond 80 k€, S08) + 700 k€ de dette bancaire sur 7 ans ;
- annuité holding : **116 627 €/an**.

**Contraintes.** D'après la règle CRA (annuité ≤ 70 % du cash), la cible doit dégager au moins **≈ 167 k€ de cash distribuable**, soit un EBE d'environ 250-280 k€ (ESTIMATION). Cela donne :
- dividendes remontés : ≈ 170 k€/an ;
- IS sur la quote-part : environ 2 k€/an (5 % × 25 % × 170 k€), ou quasi nul en intégration fiscale (S15) ;
- **cash libre de la holding ≈ 50 k€/an pendant 7 ans**.

**Cumul fin 2030** : ≈ **200-250 k€** de cash libre (4-5 exercices, ESTIMATION), plus une valeur nette des titres de la PME (dette remboursée ≈ 450 k€) **mobilisable seulement par refinancement**, ce qui ajoute du levier et du risque.

**Conclusion chiffrée** : une reprise d'environ 1 M€ **double à peu près l'apport** d'ici 2030-2031. Elle **ne suffit pas** pour le montage 1. Il faudrait :
- une **reprise plus grosse** (3-5 M€ de prix, apport ≈ 0,5-1 M€) ;
- ou **2 à 3 reprises** ;
- ou une **cession** de la PME vers 2030.

Il y a aussi un conflit de temps : **diriger une PME et lancer un domaine en même temps** n'est pas compatible.

**Intérêt réel** : montrer aux banques des **revenus récurrents de la holding**. La holding peut aussi **se porter caution** ou recevoir un **loyer** d'une activité équestre filiale.

**Perte de contrôle** : faible. Le risque porte sur la PME elle-même : le CRA estime qu'un repreneur doit avoir au moins 100 k€ d'apport (S04).

**Faisabilité** :
- 50 k€ : ✗ (franchise selon le CRA) ;
- 250 k€ : ✓ (étape 1 seulement) ;
- 1 M€ : ✓.

### 4.7 Tableau de synthèse

| Montage | 50 k€ | 250 k€ | 1 M€ | Dilution fondateur | Propriété du château | Risque de perte de contrôle | Dépendance principale |
|---|---|---|---|---|---|---|---|
| 1 PropCo/OpCo bancaire | ✗ | ✗ | ◐ | 0 % | Oui | Saisie si défaut | EBITDAR ≥ 300 k€, banque |
| 2 Club deal PropCo | ◐ | ◐ | ✓ | 60-92 % sur les murs | Minoritaire | **Élevé** | Investisseurs à trouver |
| 3 Crédit-vendeur | ✗ | ◐ | ✓ | 0 % | Oui (sous condition résolutoire) | Moyen | Vendeur coopératif |
| 4 Bail emphytéotique | ◐ | ◐/✓ | ✓ | 0 % | **Non** (droit réel 50-99 ans) | Moyen (politique) | Disponibilité d'un site |
| 5 Communauté + agricole + GFA | ◐ | ◐ | ✓ | > 95 % sur le château | Non (président) | Moyen-élevé (gouvernance) | Collecte grand public |
| 6 Holding LBO puis château | ✗ | ✓ (étape 1) | ✓ | 0 % | Plus tard | Faible | Performance de la PME, délai |

Combinaisons recommandées (ESTIMATION) :
- **250 k€** : montage 6 (2026-2030) **puis** montage 3 ou 4 (2030-2031).
- **1 M€** : montage 1 avec un volet 3 (crédit-vendeur partiel) pour réduire la dette.
- **50 k€** : montage 4 ou 5, après 2-3 ans d'expérience d'exploitation équestre salariée ou en location-gérance.

---

## 5. « Pourquoi un investisseur rationnel financerait-il ce projet plutôt qu'un autre ? »

**Réponse honnête : en capital d'exploitation, il n'a aujourd'hui aucune raison financière de le faire.** Les arguments contre :

1. **Rendement** : le montage 2 offre environ **3 % de rendement en cash** aux actionnaires de la PropCo (ESTIMATION §4). En face :
   - une plateforme comme Anaxago affiche un **TRI net constaté de 8,7 %** sur 684 M€ d'opérations immobilières (S26, auto-déclaré) ;
   - les obligations immobilières en ligne affichent 10-12 % (S27, S30) ;
   - le coût moyen du crédit bancaire aux entreprises est d'environ 3,7 % (S01-S02). C'est l'ordre de grandeur qu'obtient un prêteur sur des risques bien plus diversifiés qu'un château unique.
2. **Liquidité** : un château n'est ni coté ni fractionnable. La revente prend des années et la sortie dépend d'un unique acheteur (INCONNU sur les délais, à fournir par l'Agent 1).
3. **Risque opérationnel concentré** : un seul site et un fondateur de 26 ans sans historique d'exploitation documenté. Contre-exemples :
   - **Château de Lacan** : hôtel de luxe en redressement judiciaire malgré « de nombreux évènements » (S46) ;
   - **Château de Rochegude** : liquidation judiciaire du fonds en 2023 (S47) ;
   - le cas le plus médiatisé de château financé par la foule, **La Mothe-Chandeniers**, racheté en 2017 avec plus de 1,6 M€ collectés : son dirigeant déclarait en décembre 2025 « On est très légèrement bénéficiaires pour la première fois » (S51, PAGE LUE), soit environ 8 ans après le rachat.
4. **Risque du crowdfunding immobilier** : 20-25 % de retards de plus de 6 mois et 4-6 % de pertes au S1 2025 (S23). Les investisseurs particuliers sont échaudés.
5. **Conflit d'intérêts** : le fondateur veut **habiter** le château. Les investisseurs y verront un usage privatif financé par eux.

**Les seules raisons rationnelles qui tiennent** :
- **(a) Dette senior bien sécurisée.** Un prêteur en 1er rang, à **LTV ≤ 50 %** (montage 2, ou montage 1 avec plus d'apport), est protégé par la valeur du foncier et du bâti. C'est un placement de crédit, pas un pari sur le projet.
- **(b) Foncier agricole ou forestier transmissible.** Pour une famille fortunée, des parts de **GFA** donnant **75 % d'exonération** de droits jusqu'à 300 000 € (S20), louées à long terme à un exploitant équestre sérieux, sont un **outil de transmission**. Le rendement est secondaire.
- **(c) Rendement en usage, non financier.** Pension de ses propres chevaux, accès privilégié, événements privés, nom associé à une restauration MH. C'est la logique Dartagnans et Theil (accès à vie, S35). Ce n'est **pas** un investissement financier au sens de l'AMF, et il ne faut pas le présenter comme tel.
- **(d) Défiscalisation encadrée.** Le mécénat donne une réduction de 60 % (entreprise) ou 66-75 % (particulier/IFI) (S16), **seulement** si le site reste sous 60 k€ de recettes commerciales ou relève de l'exception agricole (S14). C'est un **don**, pas un investissement.
- **(e) Option sur un actif décoté.** Si l'Agent 1 démontre que les châteaux se vendent nettement **sous leur coût de reconstruction** et que le projet crée de la valeur par la restauration, une **promote** et une **option d'achat** du fondateur peuvent intéresser un family office patient. Cette décote est **non démontrée ici (INCONNU)**.

**Ce qui rendrait le dossier finançable** :
1. un **historique d'exploitation** équestre ou événementielle chiffré (2-3 ans, même en location) ;
2. des **pré-réservations** signées (mariages, pensions, stages) ;
3. un **apport significatif** (≥ 15-25 % du total) ;
4. une **séparation claire** entre résidence privée (payée au prix du marché) et exploitation ;
5. un **rapport d'architecte du patrimoine** chiffrant les travaux ;
6. des **sûretés réelles** et des clauses de sortie.

---

## 6. Ce que je ne recommande pas

- Présenter les campagnes de co-châtelains comme un « investissement » : les contributeurs achètent un **usage ou une symbolique**, pas un rendement (S33-S35). À ne pas confondre avec du crowdequity rémunéré.
- Monter une SCI familiale MH **et** faire entrer des investisseurs tiers sans agrément : risque de perte du régime 156 bis (S13).
- Monter une OpCo distincte pour « contourner » le seuil de 60 k€ : le BOFiP additionne les recettes **quel que soit l'exploitant** (S14).
- Émettre des obligations non garanties remboursables in fine à 5 ans pour un projet dont le cash-flow d'exploitation n'est pas démontré : cela crée un **mur de refinancement**.

---

## 7. Points de doute / hypothèses non vérifiées

1. **Taux bancaires** : le 3,66 % d'août 2026 provient d'un résumé de recherche (page BdF bloquée, S02). Le 3,64 % (S01) est lu. Les taux réels pour un château + hôtellerie sont **INCONNUS**. Méthode : 3 rendez-vous bancaires (banque mutualiste régionale, banque privée, Bpifrance) avec un dossier type.
2. **Apport, LTV et durée pour un château commercial** : aucune source spécifique trouvée. Mes 25-35 % d'apport et 50-65 % de LTV sont des ESTIMATIONS.
3. **Garantie Bpifrance** : source de 2025 (S06). Barème 2026 et exclusion éventuelle des sociétés immobilières non vérifiés.
4. **Crédit-bail immobilier pour un château** : aucun cas trouvé. Barème lu sur un annuaire tiers (S11), pas sur bpifrance.fr.
5. **Subventions DRAC** : taux et plafonds non vérifiés (INCONNU).
6. **SAFER** : page non chargée. Droit de préemption non détaillé.
7. **Règlement (UE) 2020/1503** : le texte EUR-Lex n'a pas pu être ouvert (bot challenge). Plafond de 5 M€ et protections des non-avertis vérifiés via 2 cabinets d'avocats (S21-S22) seulement.
8. **Château Fontenay (Bricks)** : issue inconnue. Remboursement ? Retard ? À vérifier sur la page du projet Bricks ou au BODACC.
9. **Mothe-Chandeniers** : je n'ai pas vérifié l'évolution juridique récente de la SAS ni la valeur actuelle des actions.
10. **Exception agricole au mécénat** (S14) : son application à un château dont les écuries sont utilisées par une activité équestre agricole est **une interprétation**, à confirmer par **rescrit fiscal**. Par ailleurs, la doctrine S14 est datée du 12/09/2012, même si elle est affichée « en vigueur ». Le seuil de 60 000 € et les autres conditions sont à recouper avec le CGI en vigueur (Legifrance inaccessible aujourd'hui : 403).
11. **Montage 6** : les marges et prix de PME sont issus de prix **demandés** (S05) et de l'observatoire CRA 2023 (données 2022). Les observatoires 2024/2025 n'ont pas été trouvés en PDF.
12. **Contre-exemples** : Lacan (redressement, S46) et Rochegude (liquidation, S47) confirment le risque des châteaux-hôtels. Aucune perte documentée de co-châtelains n'a été trouvée, ce qui n'est pas une preuve d'absence.
13. Tous les montants « investisseurs », « subventions », « dons » et « collecte » des montages sont des **hypothèses non acquises**.
