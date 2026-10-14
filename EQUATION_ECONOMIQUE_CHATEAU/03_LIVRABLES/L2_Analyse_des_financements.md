# L2 — Comment financer durablement ces coûts ? Analyse des solutions possibles

> **Statut et conventions**
> - Analyse fondée sur 8 agents de recherche (vague 1), 4 recherches ciblées (vague 2 : V2A, V2C, V2D, V2V), une équipe rouge (V2R) et le modèle `02_MODELE/sorties/Modele_equation_chateau.xlsx`, feuilles Moteurs et Modeles (11 814 formules, 0 écart avec le calcul Python).
> - Montants en € 2026. Les activités sont en HT, le besoin du domaine en TTC (propriétaire particulier).
> - Identifiants de sources entre crochets ; registre complet dans `04_SOURCES/`.

---

## 1. L'équation à résoudre

Chaque année :

```
Contributions nettes des activités  +  revenu net d'un moteur extérieur  +  aides notifiées
                                ≥  besoin du domaine (L1)  [+ dette éventuelle]
```

Le tout doit tenir **chaque année**, y compris en crise. Une réserve absorbe les écarts. Trois distorsions, détaillées dans `00_PILOTAGE/Cadre_analytique.md`, changent la lecture des chiffres.

1. **Le coin fiscal.** Le château est un lieu de vie : l'essentiel de son coût est privé. Il se paie donc avec de l'argent déjà taxé. Un euro de bénéfice d'une société à l'IS ne laisse que ≈ 0,51 € au propriétaire après IS (25 %) et PFU (31,4 % en 2026) [R3-16][R3-20][R3-57]. Avec les contributions sur les hauts revenus, il ne reste même qu'environ 0,46 € [V2R-04][V2R-05]. Le modèle applique une « fuite fiscale » de 40 % (25 à 54 %) aux bénéfices des activités qui servent à payer des coûts privés.
2. **Le coin de tranquillité.** Chaque activité fait venir des tiers, du bruit, de la circulation. Le propriétaire veut une partie « entièrement privée » et un domaine calme : cela plafonne mariages, hôtellerie et visites.
3. **Le coin de prestige.** Le niveau d'entretien exigé (jardins impeccables, personnel suffisant) fait le besoin. Certaines activités en profitent (réceptions, tournages), d'autres pas (forêt, loyers).

**Qualité des revenus.** Le modèle distingue quatre classes :

| Classe | Nature | Exemples |
|---|---|---|
| A | Contractuel | Baux, redevances |
| B | Récurrent opérationnel | Pensions de chevaux |
| C | Occasionnel | Réceptions, tournages |
| D | Financier ou extérieur | Dotation, dividendes |

**Principe de robustesse retenu.** Les charges fixes du domaine doivent être couvertes, en régime de croisière, par les classes A et D. Les classes B et C financent la réserve et le développement.

---

## 2. Ce que montrent les domaines réels

### 2.1 Les mécanismes qui fonctionnent (comptes publiés)

| Mécanisme | Preuves | Transposable à un domaine privé de 50 à 300 ha ? |
|---|---|---|
| **Patrimoine de rapport dédié (dotation)** | **Burghley** : « endowed with its own land and property portfolios » ; revenu immobilier net de 3,52 M£, soit ≈ 75 % des dépenses caritatives [R5-07]. **Blenheim** : fonds dédié de 21,9 M£ (objectif 45 M£), alimenté par la promotion foncière du domaine [R5-03]. **Northumberland Estates** (famille d'Alnwick) : foncière diversifiée qui verse 5 M£ de dividendes par an [R5-14]. | **Oui, c'est le mécanisme central**, mais il suppose de **constituer** ce capital : ces familles en ont hérité. |
| **Revenus locatifs des dépendances et maisons du domaine** | **Goodwood** : location immobilière à 39 % de marge, contre 2 % pour l'ensemble du groupe [R5-01]. **Castle Howard** : loyers de 1,87 M£ [R5-11]. **Holkham** : l'agriculture passe de 70 % à ≈ 20 % des revenus, au profit du logement et de l'hébergement [R5-45]. | Oui à petite échelle : quelques logements dans les communs. Changement de destination soumis au PLU et à l'ABF [R3, Q8]. |
| **Visite de masse d'un monument de rang mondial** | **Vaux-le-Vicomte** : ≈ 300 000 visiteurs, budget de 8 à 9 M€ [R4-30][R4-31]. **Chenonceau** : ≈ 900 000 [R4]. **Chatsworth** : 630 000 [R5-05]. Mais à **Blenheim**, 700 000 visiteurs ne couvrent que 11,1 M£ sur 16,4 M£ de coûts du palais [R5-03]. | **Non** : il faut un monument célèbre et une foule incompatible avec une résidence calme. La moyenne d'un monument privé ouvert est de ≈ 6 000 visiteurs [R4-51][R7-20]. |
| **Échelle industrielle de séminaires près de Paris** | **Châteauform' France** : 186,4 M€ de CA, 1,8 % de marge nette (2025) [R7-63]. **Château de Villiers-le-Mahieu** : 11,1 M€ de CA, + 1,25 M€ de résultat (2025) [R4-34]. | Seulement pour un grand château confié à un exploitant (§ 3.4). |
| **Moteur extérieur au domaine** | Caudalie à côté de Smith Haut Lafitte, revenu d'un médecin à Gudanes, télévision à la Motte-Husson [R4]. Domaine des Étangs : pertes d'environ 7,6 M€ par an couvertes par la famille [R4-08]. | **Oui, c'est le cas général des domaines privés qui tiennent**, à condition de séparer et d'organiser ce moteur (§ 6). |

### 2.2 Les mécanismes qui échouent

| Mécanisme | Preuves |
|---|---|
| Château-hôtel exploité | Sur 33 sociétés avec un CA ≥ 1 M€, 61 % sont en perte ; marge nette médiane de −6,3 % [R4-34][R4-35]. Sur les seuls comptes 2023-2025 (26 sociétés) : 54 % en perte, marge médiane de −4,5 % [V2V]. Au moins 15 liquidations de 2023 à 2026, et au moins 41 entités « château » de l'hôtellerie ou de la réception en procédure collective depuis 2024 [R4][R7-64]. Ygrande (hôtel et 26 boxes) en liquidation depuis le 28/10/2025 [R4][R7]. |
| Lieux de réception | Marge nette de 0 à 6 % ; 1 382 châteaux et 3 769 domaines référencés sur une seule plateforme [R7-05][R7-06][R7-63]. |
| Ouverture à la visite | « Pour 99,8 % des propriétaires, la seule activité d'ouverture à la visite n'est donc pas rentable » ; résultat toujours négatif sous 10 000 visiteurs payants [R1-01]. |
| Haras « vitrines », grands événements équestres | Haras de Hus : CA de 1,77 M€, résultat de −2,94 M€ (2024) ; Pôle international du cheval : −0,26 M€ [R4-39][R4-15]. Burghley Horse Trials : 6,3 M£ de CA pour 0,13 M£ de résultat d'exploitation [R5-08]. Haras national de Lamballe : déficitaire de 130 673 € en 2025 et 3 écuries résidentes parties [R6-17]. |
| Financement participatif | La Mothe-Chandeniers : ≈ 4,4 M€ collectés en 7 ans auprès de ≈ 25 000 copropriétaires ; tout usage privé est exclu [R4]. |
| Dépendance à un mécène unique | Chantilly : besoin de 68 M€ sur 10 ans après le retrait de l'Aga Khan, pour 12,7 M€ de recettes [R4-46]. |

---

## 3. Inventaire chiffré des sources de revenus sur place

Contribution nette annuelle de chaque activité, à l'échelle d'un domaine S2, avant IS. Les installations déjà financées par le budget (écuries, manège) ne sont pas recomptées : c'est une **contribution marginale**. Tableau généré depuis le modèle.

| Activité (échelle S2) | Classe | Favorable | Central | Défavorable | Investissement |
|---|:---:|---:|---:|---:|---:|
| Pension standard (30 boxes) | B | 24 k€ | −1 k€ | −40 k€ | — |
| Pension haut de gamme (30 boxes) | B | 102 k€ | 21 k€ | −98 k€ | — |
| Écuries louées à un professionnel (20 boxes) | A | 22 k€ | 9 k€ | −5 k€ | — |
| Pension retraite au pré (30 chevaux) | B | 31 k€ | 10 k€ | −6 k€ | — |
| Centre de reproduction (si vétérinaire et étalon) | B | 30 k€ | 21 k€ | 0 | INCONNU |
| Réceptions privées plafonnées (10 par an) | C | 78 k€ | 6 k€ | −46 k€ | 400 k€ |
| Tournages et prises de vue (2 jours par an) | C | 28 k€ | 6 k€ | 0 | — |
| Séminaires de jour (20 jours par an) | C | 45 k€ | 13 k€ | 0 | — |
| Grande maison louée à la semaine | C | 131 k€ | 35 k€ | −13 k€ | 600 k€ |
| Logements locatifs dans les communs (600 m²) | A | 73 k€ | 33 k€ | 13 k€ | 1 080 k€ |
| Hivernage de camping-cars (600 m²) | A | 9 k€ | 5 k€ | 1 k€ | 20 k€ |
| Gardiennage de voitures de collection | A | 29 k€ | 8 k€ | −12 k€ | 60 k€ |
| Bail solaire (5 ha hors champ de visibilité) | A | 60 k€ | 15 k€ | 0 | — |
| Forêt (30 ha) | A | 3 k€ | 2 k€ | 2 k€ | — |
| Château-hôtel exploité (15 chambres) | B/C | 623 k€ | **−388 k€** | −1 095 k€ | 7 500 k€ |
| Bail d'ancrage à un exploitant de séminaires (50 chambres, si les conditions sont réunies, § 3.4) | A | 521 k€ | **350 k€** | 0 | à la charge de l'exploitant |
| Location de luxe de la partie privée (3 semaines par an, § 3.5) | C | 182 k€ | 39 k€ | −18 k€ | 300 k€ |

### 3.1 Activités équestres [R6]

- **La pension standard ne dégage rien une fois tout le travail payé.**
  - Prix rural ou périurbain : 334 à 401 € HT/mois (cas-types 2025) [R6-02].
  - Les écuries de référence vivent grâce au bénévolat (60 à 70 % des pensions) et à un exploitant qui se paie peu : revenu disponible médian de 9 437 à 18 265 € [R6-03].
- **La pension haut de gamme exige une clientèle aisée à moins d'une heure.**
  - Haras de Jardy, à 10 km de Paris : 922,50 € TTC/mois, soit 874 € HT au taux de 5,5 % applicable à une pension accessoire à la pratique [R6-15][R3-22].
  - Hors de l'ouest parisien, aucune preuve publique de demande n'a été trouvée.
  - L'offre nationale est excédentaire : 22 000 places de pension retraite vacantes en 2019 [R6-16].
- **Atout majeur : la pension est le revenu le plus résistant aux crises.** En 2020, il est resté stable ou a progressé jusqu'à +10 % en Normandie, quand les centres équestres perdaient 15 % [R6-27].
- **Écuries louées à un professionnel : revenu faible et risque juridique.**
  - Plafond observé : 80 000 €/an pour 68 boxes en plein Paris [R6-25].
  - Les locataires partent facilement (Lamballe) [R6-17].
  - Risque de requalification en bail rural, qui fait perdre durablement la maîtrise des écuries [R3, Q7].
- **Élevage, courses, étalons, polo, grands concours : activités de passion, pas de financement.**
  - Yearlings : médiane de 23 000 € HT pour une moyenne de 66 317 € [R6-08].
  - Allocations et primes de France Galop : −4,6 % en 2025 [R6-06].

**Conclusion.** L'équestre peut **autofinancer une partie de la passion** du propriétaire : des pensionnaires partagent les installations et le personnel. Il ne finance pas le château.

### 3.2 Événements, hébergement, visites [R7]

- **Mariages.**
  - 251 000 par an en France, dont 59 % de juin à septembre et 82 % le samedi [R7-01][R7-15].
  - Location du lieu seul : 4 000 à 10 000 € le week-end [R7-07][R7-09][R7-10].
  - Concurrence massive [R7-05][R7-06].
  - Salle ERP à aménager : plus de 100 000 € pour 98 m² dans un cas documenté [R4-52].
  - Étude d'impact acoustique si les réceptions avec musique sont habituelles [R3-52].
  - **Plafonnées à 10 par an, elles rapportent au mieux quelques dizaines de milliers d'euros**, et parfois rien.
- **Séminaires de jour.** 95 à 100 € HT par personne [R7-27][R7-28][R7-29]. Seulement à moins d'une heure d'une métropole.
- **Tournages.** Grille du CMN : 2 500 à 5 500 € HT par jour [R7-12]. Revenu imprévisible : à Blenheim, 1,14 M£ une année et 0,21 M£ l'année précédente [R5-03].
- **Hébergement.**
  - Gîtes : 44 à 47 % d'occupation sur l'année [R7-48][R7-50].
  - Les logements classés G ne peuvent plus être loués (F dès 2028) : risque pour des communs anciens [R3-34].
  - Château-hôtel : 350 000 à 700 000 € d'investissement par chambre, hors prix d'achat [R7-41][R7-42][R7-43]. Environ 1,65 personne par chambre, restaurant compris : c'est un effectif projeté de 33 personnes, dont 19 en cuisine, restaurant et bar [V2V]. Projeté à 15 chambres, il **perd de l'argent dans le cas central**, ce que confirment les comptes réels (§ 2.2).

### 3.3 Foncier, énergie, dépendances [R8]

- **Logements dans les communs.**
  - Loyer de 6,8 à 10,9 €/m²/mois charges comprises en commune rurale [R8-22][R8-23]. Cette fourchette couvre 75 % des communes ; la médiane des petites communes est de 8,63 €/m² [V2V].
  - Transformation : ≈ 1 600 à 2 200 € TTC/m² [R8-24].
  - Rendement net de **3 % environ** (central). C'est surtout un moyen de faire entretenir et occuper des bâtiments qui coûteraient de toute façon.
- **Solaire.**
  - Loyers de 1 500 à 6 000 €/ha/an [R8-01], sources commerciales.
  - Autour d'un monument historique : permis de construire dès 3 kW et accord de l'ABF [R3-63].
  - Loi APER : agrivoltaïsme seulement si l'activité agricole reste principale [R3-44].
- **Forêt, chasse, carbone.**
  - Forêt : quelques dizaines d'euros par hectare et par an.
  - Chasse : loyer INCONNU.
  - Crédits carbone : ≈ 800 €/ha, **une seule fois** [R8-14][R8-16].
- **Petite hydroélectricité.** 16 000 à 68 000 €/an pour 100 kW, mais seulement s'il existe un moulin avec un droit fondé en titre. La moitié des installations ont une rentabilité insuffisante [R8-11][R8-12][R3-53].
- **Stockage** (camping-cars, voitures de collection) : quelques milliers à quelques dizaines de milliers d'euros. Demande rurale non démontrée [R8-17][R8-18].

### 3.4 Bail à un exploitant (« locataire d'ancrage ») [V2A]

**Qui exploite, qui possède.**
- Châteauform', principal exploitant de maisons de séminaires, est surtout **exploitant**. Dans les cas où le propriétaire des murs est identifiable, ce sont des tiers : une foncière du groupe Batipart, une foncière du groupe Eurosic, Icade, une SA immobilière, un trust [V2A-01] [V2A-03] [V2A-14] [V2A-54].
- Contrats observés :
  - rachat du fonds de commerce (350 000 et 500 000 € en 2017) [V2A-02] [V2A-03] ;
  - bail commercial ;
  - concessions de 5 ans (Institut de France) et de 12 ans (Belgique, où l'exploitant investit plus de 1,1 M€) [V2A-10] [V2A-54].
- Son dirigeant indique signer « pour des périodes de 15 ou 30 ans » [V2A-54]. **Aucun montant de loyer n'est publié.**

**Conditions d'entrée** (données du site de l'exploitant, PAGE LUE, et calculs de V2A) :
- **Au moins 40 chambres** : c'est le minimum des maisons françaises de Châteauform', la médiane étant de 61 [V2A-13].
- **Une localisation proche de Paris ou d'une gare.** 24 maisons sur 29 sont à 88 km ou moins de Paris. Les 5 autres sont à 35-50 minutes d'une gare TGV ou d'un aéroport de Lyon, Bordeaux ou Aix-Marseille. La proximité d'une gare devient un critère important [V2A-13] [V2A-54].
- Conséquences par scénario (HYPOTHÈSES de capacité) :
  - S1 est hors champ ;
  - S2 est à la limite, car il faudrait mobiliser l'essentiel des bâtiments ;
  - S3 est plausible, en gardant une aile privée.

**Loyer possible** (ESTIMATION fragile : aucun loyer réel de château loué à un exploitant n'a été trouvé) :
- chiffre d'affaires de l'exploitant : environ 70 000 € HT par chambre et par an (Méry 72 400 €, Saint-Just 68 800 €) [V2A-14] [V2A-01] ;
- loyer : 8 à 15 % de ce chiffre d'affaires, selon les usages hôteliers et la capacité de paiement de l'exploitant [V2A-29] [V2A-31] ;
- soit 0,22 à 0,63 M€ brut par an pour S2 (40 à 60 chambres), et 0,34 à 1,05 M€ pour S3 (60 à 100 chambres).
- Si l'exploitant finance la transformation, le loyer se place en bas de fourchette. Le modèle retient 10 % du chiffre d'affaires et 50 chambres, soit 0,35 M€ de loyer brut. Après les frais du bailleur (10 %) et avec les charges du domaine reprises par l'exploitant (énergie et entretien courant de la zone louée, environ 35 k€), la contribution centrale reste d'environ 0,35 M€. Le cas défavorable vaut 0 : sans localisation adéquate, aucun exploitant de cette taille ne viendra.

**Cadre juridique** (fiches Service Public, à valider par un avocat) :
- le bail commercial dure au moins 9 ans et donne droit au renouvellement ;
- refuser ce renouvellement coûte une indemnité d'éviction de l'ordre de la valeur du fonds [V2A-36] [V2A-41] ;
- les **grosses réparations** (toiture, murs porteurs) restent **toujours** à la charge du bailleur [V2A-38] ;
- en cas de procédure collective, le bail est en principe cédé avec l'entreprise, à un repreneur que le propriétaire n'a pas choisi [V2A-39].

**Contre-exemples** :
- la société d'exploitation du château de Méry a perdu 0,56 M€ en 2024, perte portée par son actionnaire foncier [V2A-14] ;
- loyers variables de Covivio : −67 % au premier semestre 2020 [V2A-31] ;
- des gestionnaires de résidences Pierre et Vacances ont suspendu leurs loyers ; près de 20 000 bailleurs étaient sans paiement depuis janvier 2021 [V2A-62] ;
- des exploitants hôteliers se sont succédé aux Mesnuls, au Tremblay et à Herces [V2A-51] [V2A-52].

**Cohabitation.**
- **Aucun cas documenté** d'un propriétaire vivant au château à côté d'un exploitant de 40 chambres ou plus n'a été trouvé.
- Le cas le plus proche est Courances. Un opérateur y exploite les dépendances (7 maisons, 39 personnes) pendant que le château reste privé, mais le contrat est inconnu [V2A-21].
- Ce format de location de dépendances génère environ 12 000 € de chiffre d'affaires par chambre côté opérateur, soit six fois moins qu'une maison de séminaires [V2A-17].

**Verdict.**
- C'est la seule activité sur place qui change l'ordre de grandeur : un revenu de classe A de 20 à 50 % du besoin.
- Elle exige trois conditions cumulatives : la localisation, au moins 40 chambres et un exploitant qui finance la transformation.
- Elle immobilise l'essentiel des bâtiments pendant 15 à 30 ans, au détriment de la partie privée et du calme.
- **Option sérieuse pour un grand domaine (S3) bien situé ; incompatible avec le cahier des charges de S2.** Elle est évaluée comme modèle M7.

### 3.5 Libération de capital et location de luxe [V2D]

| Mécanisme | Ce qu'il rapporte | Conditions et coûts | Verdict |
|---|---|---|---|
| **Vendre des dépendances à un opérateur « Monument historique »** qui les divise en logements défiscalisés | Capital ponctuel, **montant INCONNU**. Le prix payé au propriétaire d'origine n'est publié nulle part. La part « foncier » revendue aux investisseurs, marge de l'opérateur comprise, vaut 13 à 38 % de leur prix [V2D-05] [V2D-09] [V2D-13] | Deux opérateurs vérifiés (Histoire & Patrimoine, Buildinvest), dont tous les programmes sont en ville ou à 10-30 minutes d'une métropole [V2D-07] [V2D-13]. L'immeuble divisé doit être à 75 % en habitation dans les 2 ans, locaux commerciaux exclus [V2D-16]. Pertes cumulées d'environ −86 M€ en 2025 pour les sociétés du leader (simple somme) [V2D-42]. Opérations politiquement sensibles (Grignon) [V2D-17] | **Aucun exemple** d'un propriétaire qui vend ses communs et garde le château. Perte définitive des bâtiments ; 7 à 125 ménages voisins |
| **Vendre la nue-propriété** et garder l'usufruit à vie | Valeur fiscale de la nue-propriété à 26 ans : **20 %** du bien (barème de l'article 669) [V2D-19] ; prix de marché inconnu, sans doute plus bas | Aucun marché identifié pour des châteaux [V2D-30] ; IFI encore dû sur 80 % [V2D-20] | Perte définitive pour les héritiers, pour au mieux 20 % de la valeur |
| **Céder un usufruit temporaire** d'une partie (10 à 30 ans) | Valeur fiscale : 23 % par période de 10 ans [V2D-19] | Le prix est **imposé comme un revenu** l'année de l'encaissement [V2D-21] | Juridiquement compatible avec « garder la propriété », mais fiscalement coûteux ; aucun exemple |
| **Copropriété ou partage entre familles** | Vente de lots ; seuls prix trouvés : 640 000 à 960 000 € **affichés** par logement à Monboucher [V2D-44] | Indivision instable ; SCI qui loue en saisonnier jugée commerciale [V2D-34] | Les exemples (Panat, Monboucher) reposent sur des pièces communes : incompatible avec une partie entièrement privée |
| **Location de luxe de la partie privée** à la semaine | 12 755 à 61 850 € par semaine pour 8 à 16 chambres [V2D-35] à [V2D-38] [R7-54] ; commission de 20 à 22 % [V2D-24] [V2D-25] | Environ 2 réservations par propriété et par an chez la plateforme leader [V2D-26] ; piscine et une salle de bains par chambre [V2D-40] [V2D-41] ; 6 semaines disponibles en juillet-août chez un autre acteur [V2D-28] ; location d'une résidence principale limitée à 90-120 jours dans certaines communes [V2D-32] | Seul revenu récurrent, mais modeste. Le modèle retient 3 semaines à 30 000 € : **39 k€ de contribution centrale** (−18 à +182 k€). Le propriétaire doit quitter sa maison l'été. Évaluée comme modèle M8 |
| **Dette participative** (obligations) | Exemple : 690 000 € à 7 % sur 5 ans pour un château classé [V2D-45] | Environ 48 000 € d'intérêts par an | C'est une dette, pas un financement du fonctionnement |

**Conclusion.**
- Aucun de ces mécanismes ne finance durablement le fonctionnement.
- Ceux qui libèrent du capital le font une seule fois, en cédant une partie de la propriété ou de la tranquillité, et pour un montant que les sources ne permettent pas de chiffrer.
- Leur seul usage cohérent : **verser le capital libéré au capital affecté** (§ 6). Chaque million d'euros versé finance environ 17 500 € de besoin par an (règle de dépense de 1,75 %).

### 3.6 Résultat : les activités sur place ne couvrent qu'une petite part du besoin

Huit combinaisons comparées au besoin du domaine S2 (1,27 M€/an), après une fuite fiscale de 40 %. La pension standard ne fait plus partie du socle : elle ne rapporte rien dans le cas central et fait venir 25 à 30 propriétaires de chevaux chaque semaine (V2R m8).

| Modèle | Contribution disponible (central) | Couverture du besoin S2 (fav. / central / déf.) | Écart à financer (central) | Investissement |
|---|---:|---:|---:|---:|
| M1 — Socle contractuel et pension de retraite au pré | 43 k€ | 20 % / **3 %** / 0,2 % | 1 231 k€ | 1 100 k€ |
| M2 — Lieu d'exception à quota (M1 + réceptions, séminaires, grande maison) | 75 k€ | 44 % / **6 %** / −2 % | 1 198 k€ | 2 100 k€ |
| M3 — Équestre haut de gamme et services | 36 k€ | 19 % / **3 %** / −5 % | 1 237 k€ | 0 |
| M4 — Château-hôtel exploité + réceptions | −361 k€ | 76 % / **−28 %** / −55 % | 1 635 k€ | 7 900 k€ |
| M5 et M6 — Socle minimal + moteur extérieur | 11 k€ | 6 % / **0,9 %** / −0,2 % | 1 262 k€ | 0 |
| M7 — Locataire d'ancrage + socle foncier (§ 3.4) | 227 k€ | 59 % / **18 %** / −0,2 % | 1 046 k€ | à la charge de l'exploitant |
| M8 — Socle M1 + location de luxe de la partie privée (§ 3.5) | 66 k€ | 37 % / **5 %** / −0,4 % | 1 207 k€ | 1 400 k€ |

**Lecture.**
- Le cas favorable cumule toutes les hypothèses heureuses. Même alors, aucune combinaison compatible avec une résidence calme ne couvre plus de la moitié du besoin.
- Dans le cas central, elles en couvrent **1 à 6 %**.
- Le château-hôtel peut couvrir l'essentiel dans le meilleur cas, mais il creuse le déficit dans le cas central, et les comptes réels confirment ce risque.
- Le locataire d'ancrage (M7) est la seule exception : 18 % dans le cas central, jusqu'à 59 % dans le meilleur cas. Il suppose de confier l'essentiel des bâtiments à un exploitant pendant 15 à 30 ans, et il tombe à zéro si la localisation ne convient pas.

---

## 4. Leviers fiscaux, publics et juridiques [R3]

| Levier | Effet | Conditions | Limites |
|---|---|---|---|
| **Régime fiscal des MH** (CGI art. 156) | Charges foncières déductibles du **revenu global** : 100 % si le château est ouvert au public, 50 % s'il est fermé. Travaux subventionnés : 100 % [R3-02][R3-05] | Classé ou inscrit ; ouverture de 50 jours par an dont 25 non ouvrables d'avril à septembre, ou de 40 jours de juillet à septembre, 6 h par jour [R3-04] ; détention directe ou SCI familiale ; conservation 15 ans [R3-06] | Réduit l'**impôt personnel** : suppose des revenus imposables au barème. Exclut les parties exploitées commercialement [R3-04 § 40]. Pas d'excédent reportable si l'immeuble ne produit pas de recettes |
| **Subventions des DRAC** | 20 % (inscrit) à 40 % (classé) des travaux éligibles en moyenne [R1-34] | Dossier avant tout commencement de travaux [R1-03] | Crédits en baisse dans le projet de loi de finances 2026 : −29 % en crédits de paiement selon le Sénat, −13 % sur un périmètre plus étroit selon l'Assemblée [R1-33][R1-34][V2V] ; versement avec plusieurs années de retard ; **jamais acquises** : à exclure du scénario central |
| **Loto du patrimoine, Fondation du patrimoine** | 148 000 à 280 000 € pour un site sélectionné, **une seule fois** [R1-12][R1-13][R1-16] | Sélection concurrentielle | Pas un revenu récurrent |
| **Mécénat via la Fondation du patrimoine** | Les donateurs déduisent 66 % de leur don de l'IR | Propriétaire personne physique ; **recettes commerciales ≤ 60 000 € HT par an** ; conservation et ouverture 10 ans [R3-10] | Fermé dès qu'il y a une vraie activité commerciale ; finance des travaux précis, pas le fonctionnement |
| **Exonération de droits de succession** (CGI art. 795 A) | 100 % de la valeur transmise exonérée | Convention perpétuelle : ouverture 50 jours par an, maintien du mobilier [R3-13][R3-14] | Pèse durablement sur la tranquillité ; sert la transmission, pas le fonctionnement |
| **TVA équestre à 5,5 %** (depuis 2024) | Pension « accessoire à la pratique », enseignement, accès aux installations [R3-22] | Frontière fragile avec la pension à 20 % (valorisation, retraite, box sans soins) | À valider par un expert-comptable |
| **IFI** | Aucune exonération pour les MH ; abattement de 30 % sur la résidence principale [R3-01][R3-15] | — | 10 550 €/an en S2, 51 940 € en S3 (résidence principale) |
| **Taxe de 20 % sur les holdings patrimoniales** (LF 2026) | — | Holding ≥ 5 M€ d'actifs, revenus passifs > 50 % [R3-18] | Vise les **logements réservés à l'associé** et les **chevaux de concours**. Ne jamais loger le château habité ni les chevaux personnels dans une telle holding |
| **Structure** | Partie privée en direct ou en SCI familiale à l'IR ; activités en société d'exploitation payant un loyer de marché [R3, Q9] | SCI à l'IR : activité commerciale < 10 % de son CA [R3-59] | Logement gratuit dans une société à l'IS : acte anormal de gestion et revenu distribué [R3-56] |

**Effet chiffré du levier MH.**
- Hypothèses : taux marginal de 41 %, 45 % du besoin en charges déductibles, déduction de 50 % (château fermé au public).
- L'économie d'impôt est d'environ 9 % du besoin, soit environ 115 k€ par an en S2.
- C'est un levier réel, mais **seulement pour un propriétaire qui a de gros revenus imposés au barème** : il faut environ 0,36 M€ de revenus au barème pour absorber la déduction (ESTIMATION, V2R M4). Or, dans la solution, les revenus du propriétaire sont surtout des revenus de capitaux imposés au PFU, qui n'entrent pas dans ce calcul.
- L'excédent de déduction ne se reporte pas [R3-05]. L'effet de la contribution différentielle sur les hauts revenus est INCONNU.
- Ce levier n'est donc **plus compté** dans les capitaux nécessaires du § 6. Il reste une option, sous condition de revenus.

---

## 5. Leviers de réduction du besoin (« prestige efficace ») [V2C]

**Le premier levier est le niveau de soin choisi pour chaque zone.**
- Les temps d'entretien mesurés par la Ville de Rennes vont de 2 800 h/ha/an (jardin très fleuri) à 90 h/ha/an (prairie fauchée), soit un facteur 30 [V2C-21].
- La main-d'œuvre représente 80 à 99 % du coût des espaces verts [V2C-21].
- Les jardins de Vaux-le-Vicomte coûtent environ 24 000 à 27 000 € par hectare et par an, ce qui correspond au code « jardin structuré » de Rennes [V2C-24].

| Levier | Effet chiffré | Statut | Conditions et risques pour le prestige |
|---|---|---|---|
| **Gestion différenciée** (soin maximal près du château et sur les perspectives, prairies au-delà) | Passer 1 ha de « jardin d'accompagnement » à « jardin champêtre » économise 550 h/an, soit environ 11 100 €. Par rapport à un parc soigné partout : environ −67 k€/an en S2 et −445 k€/an en S3 [V2C-21] [V2C-11] | ESTIMATION | Plan de gestion écrit ; accepter le « naturel » au loin, ce qui est la composition classique d'un domaine |
| **Fauche tardive** (prairies au lieu de pelouses) | −710 h/ha/an par rapport à un jardin d'accompagnement, soit environ 14 400 €/ha [V2C-21] | ESTIMATION | Sous-traiter la fauche, ou la faire avec le matériel de fenaison des chevaux |
| **Éco-pâturage** par un éleveur | Environ −920 €/ha/an (Avignon : plus de 12 000 €/an sur 13 ha, coût nul pour la Ville) [V2C-13] | ESTIMATION | Risque de requalification en bail rural [R3] ; protection des arbres ; cohabitation avec les chevaux non étudiée |
| **Chaufferie à plaquettes** du bois du domaine | −7 700 à −10 900 €/an pour 90-110 kW ; investissement de 80 000 à 245 000 € HT [V2C-32] [V2C-33] | EXTRAIT | Silo, réseau, autorisations en abords de monument ; le bois a dérivé de +0,9 %/an réel contre +1,9 % (fioul) et +4,8 % (gaz) [V2C-04] |
| **Régulation et zonage du chauffage** | Jusqu'à −15 % de l'énergie de chauffage (ADEME), soit −3,9 à −5,9 k€/an en S2 [V2C-26] | ESTIMATION | Protéger les décors et le mobilier de l'humidité |
| **Isolation des combles** | Au plus −60 % de l'énergie selon un propos oral, sans étude [R1-09] ; les monuments historiques sont exclus de l'obligation d'isoler [V2C-27] | ESTIMATION (borne) | Faisabilité contestée sur un bâti protégé [R1-05] |
| **Personnel** | Supprimer la gouvernante et l'ouvrier agricole, et sous-traiter la fenaison : −50 à 70 k€/an en S2 [R2-11] | ESTIMATION | Choix de train de vie |
| **Sous-traitance des tâches saisonnières** (fauche, élagage, broyage) | Coût horaire du matériel divisé par 2 à 4 quand il est bien employé [R2-30] ; prix des entreprises du paysage INCONNU | PAGE LUE / INCONNU | Garder en interne le soin quotidien des zones de prestige |

**Lecture.**
- Seuls les leviers d'espaces verts changent l'ordre de grandeur, et seulement par rapport à un parc soigné partout. Le budget de L1 les **intègre déjà** : il suppose une gestion différenciée en S2, et 16 jardiniers au lieu de 33 en S3. Ils sont la **condition** pour que ces effectifs suffisent, pas une économie supplémentaire.
- Les leviers énergétiques pèsent moins de 2 % du besoin de S2 et de S3.
- Au-delà, réduire le besoin relève de **choix de train de vie** : moins de jardins réguliers, moins de personnel de maison. Ces choix contredisent en partie le brief, qui demande des jardins impeccables et un personnel suffisant.
- Par rapport au budget central, les leviers vérifiés représentent environ **5 à 8 % du besoin de S2**. La variante « leviers » du § 6, qui suppose un besoin réduit de 15 %, est donc une **borne optimiste**.

---

## 6. Le moteur extérieur : un capital affecté, éventuellement constitué par des entreprises

### 6.1 Combien faut-il ?

Le modèle simule 30 ans de vie du domaine, avec 6 000 à 20 000 trajectoires par cas. Aléas tirés au sort :
- crises (une tous les 12 ans en moyenne) ;
- rendements de marché ;
- bruit propre aux activités ;
- sinistres non assurés, payés en plus du fonds de travaux ;
- dépassements de travaux ;
- prix de l'énergie ;
- dérive des salaires.

**Hypothèses retenues pour le capital :**
- **Rendement réel net de 2 % par an** (ESTIMATION, fourchette de 1,5 à 2,5 %).
  - La seule donnée sourcée est le rendement des actions mondiales depuis 2000 : 3,5 % réel par an, avant frais et impôts [R8-32] [V2R-08].
  - Il faut en retirer des frais de 0,4 à 0,6 point et un impôt de 30 à 38,6 % sur les revenus nominaux. Le PFU est de 31,4 % ; s'y ajoutent les contributions sur les hauts revenus [V2R-03] [V2R-04] [V2R-05] [V2R-16].
  - La version précédente de ce dossier retenait 3 %. L'équipe rouge l'a jugé incompatible avec la fiscalité et les frais (V2R C2).
- **Retrait annuel encadré par une règle de dépense lissée.** Le plafond vaut 1,75 % du capital, soit 0,25 point sous le rendement attendu.
- **Règles de pilotage en période de tension**, déclenchées quand la réserve passe sous un an de charges :
  - coupe temporaire de 10 % des dépenses discrétionnaires ;
  - report de 30 % d'une campagne de travaux ;
  - retrait d'urgence plafonné à 4 %.
- La réserve est ensuite **reconstituée**.

**Échec** = réserve de trésorerie négative. C'est la définition du critère n° 6 du cadre analytique.

| Domaine | Besoin annuel | Capital pour 1 chance sur 2 de tenir 30 ans | Capital pour 95 % de chances | Avec les leviers vérifiés (besoin −7,5 %) : 50 % / 95 % |
|---|---:|---:|---:|---:|
| S1 | 0,35 M€ | 14,1 M€ (≈ 41 fois le besoin) | 37,9 M€ (≈ 110 fois) | 13,0 / 35,1 M€ |
| S2 | 1,27 M€ | 50,1 M€ (≈ 39 fois) | 132,2 M€ (≈ 104 fois) | 46,3 / 122,1 M€ |
| S3 | 3,77 M€ | 165,9 M€ (≈ 44 fois) | 491,6 M€ (≈ 130 fois) | 153,4 / 454,3 M€ |

Fichier `02_MODELE/sorties/mc_dotation_necessaire.json`, produit par `calculer_mc.py`. Le capital nécessaire est estimé par dichotomie sur 6 000 trajectoires, avec une précision d'environ ±5 %.

S3 demande un multiple plus élevé que S1 et S2. Dans le modèle, la taille d'un sinistre non assuré est proportionnelle au gros entretien, qui pèse davantage dans le budget d'un grand monument classé.

**Règle d'or qui en découle :**
- il faut environ **40 fois le besoin annuel** pour avoir une chance sur deux de tenir 30 ans ;
- il en faut environ **100 fois** pour être raisonnablement sûr (95 %), et jusqu'à 130 fois pour un grand monument classé.

Trois précisions :
- **Le seuil d'une chance sur deux n'est pas un objectif.** À 40 fois le besoin, le plafond normal de retrait (1,75 % du capital) ne couvre que 70 % du besoin. Le domaine vit alors en mode de tension, sur des retraits d'urgence (L6, § 4.3).
- **Le multiple dépend surtout du rendement.** Pour S2, avec un capital seul et 95 % de chances de tenir 30 ans, il faut :
  - 94,8 M€ à 3 % de rendement réel net ;
  - 109,5 M€ à 2,5 % ;
  - 132,2 M€ à 2 % ;
  - 168,6 M€ à 1,5 % (`sorties/mc_sensibilite_rendement.json`).
- **Les coûts montent plus vite que l'inflation** : salaires +0,5 %, travaux +0,75 %, énergie +2 % et assurances +1,85 % réels par an, d'après les séries de l'INSEE [V2C-03] [V2C-04] [V2C-05] [V2C-19].

**Le risque principal reste l'erreur de budget.** Si le besoin réel se situe au haut de la fourchette de L1, il faut environ 67 M€ en S1, 225 M€ en S2 et 890 M€ en S3, avec un capital seul (L6, § 4.2). Le budget doit donc être validé sur un bien réel avant de dimensionner le capital.

### 6.2 Entreprise extérieure ou holding de PME

- **Rendement plus élevé que celui d'un portefeuille.** Une PME reprise sans dette rapporte à son propriétaire environ 0,355 € net de dividende par euro d'EBITDA [R8-35] [R3-16] [R3-20] [V2R-04] [V2R-05] (ESTIMATION). C'est ce qui reste après l'IS, le PFU et les contributions sur les hauts revenus. Rachetée 5 à 8 fois son EBITDA, elle rend donc 4,4 à 7,1 % du capital investi. Un portefeuille financier permet de retirer environ 1,75 % par an.
- **Mais elle est fragile seule.** Plus d'une transmission de PME sur cinq échoue dans les six ans (données OSEO 1997-2003, souvent des reprises endettées) [R8-36]. Le modèle suppose 3,5 % de défaillance par entreprise et par an. Une holding **passive** de 1 à 6 PME, qui ne fait que distribuer ses dividendes, sans réinvestir, remplacer les entreprises disparues ni les revendre, échoue alors dans 85 à 98 % des cas sur 30 ans, même avec une petite dotation de 2 à 10 M€ (`mc_holding_hybride.json`). Un groupe géré activement ferait mieux, mais ce cas n'est pas modélisé.
- **Elle dépend du fondateur.** Il faut des dirigeants salariés, des réinvestissements et une surveillance permanente.
- **Elle doit être sans dette d'acquisition** au moment où elle finance le domaine. Une PME en LBO ne distribue presque rien pendant 5 à 7 ans [R8].

**Conséquence.** L'entreprise est le meilleur **outil pour construire le capital**, mais pas une rente perpétuelle. La pérennité vient de la **conversion progressive des dividendes en capital diversifié** (§ 6.3).

### 6.3 Le capital affecté reste la fortune du propriétaire : aucun véhicule ne l'en sépare

C'est la principale correction apportée par l'équipe rouge (V2R C1). Aucun outil français ne réunit à la fois trois propriétés : une affectation réelle au domaine, la jouissance privée du propriétaire et des revenus défiscalisés.

| Véhicule | Peut-il financer la partie privée d'un domaine habité ? | Fiscalité des revenus du capital | L'affectation au domaine est-elle réelle ? |
|---|---|---|---|
| Fonds de dotation, fondation | **Non.** Apport « à titre gratuit et irrévocable », revenus utilisés pour une mission d'intérêt général [V2R-02] [R8-45] ; un logement gratuit du fondateur profite à un cercle restreint [R3-43] | Pas d'IS si la gestion est désintéressée | Oui, mais au profit de l'intérêt général, plus du propriétaire |
| Holding à l'IS (société de portefeuille) | Seulement par distribution : payer des charges privées sans distribuer est un acte anormal de gestion [R3-56] | IS puis PFU : 48,6 %, jusqu'à 54 % avec les contributions sur les hauts revenus [R3-20] [R3-57] [V2R-05] | Faible : l'associé majoritaire peut changer les statuts |
| Compte-titres personnel | Oui | Jusqu'à 38,6 % des revenus nominaux [V2R-04] [V2R-05] [V2R-16] | Aucune |
| Société civile de portefeuille à l'IR | Oui | Transparente, comme le compte-titres (HYPOTHÈSE) | Faible : dépend des statuts et de la gérance |
| Assurance-vie, contrat de capitalisation | Oui | Gains imposés au rachat (12,8 % ou 7,5 %, plus 17,2 % de prélèvements sociaux) ; imposition différée [V2R-03] | Aucune ; rachats limitables jusqu'à 6 mois en crise systémique [V2R-10] |
| Fiducie-gestion | Probablement (le constituant peut être bénéficiaire) ; régime actuel INCONNU | Transparente [V2R-14] | **Réelle** : « patrimoine d'affectation » confié à un fiduciaire [V2R-13] ; coût INCONNU |
| « Maintenance fund » britannique (pour comparaison) | Pas d'équivalent en droit français. Au Royaume-Uni, il exige un accès du public et interdit tout contrôle du constituant ainsi que le logement gratuit [V2R-01] | Revenus imposés ; exonération de droits de succession | Totale, sous contrôle de l'administration fiscale |

**Ce que cela change.**
- Le « capital affecté » de ce dossier reste **juridiquement le patrimoine du propriétaire**, ou d'une société qu'il contrôle.
- Son affectation au domaine ne repose que sur une **discipline volontaire** : une charte, un comité, des statuts contraignants. Une fiducie pourrait la rendre réelle, mais son coût reste à établir.
- **La solution suppose donc de disposer d'une fortune d'environ 100 fois le besoin annuel du domaine.** C'est précisément la dépendance à la fortune personnelle que le brief voulait éviter. Aucune solution qui s'en affranchisse n'a été trouvée (L8).

### 6.4 Conditions de pérennité d'un capital affecté

1. **Règle de dépense écrite** : plafond lissé de 1,75 % du capital en temps normal.
2. **Réserve de liquidité** d'au moins un an de charges, reconstituée après usage et placée hors des contrats d'assurance, dont les rachats peuvent être gelés [V2R-10]. Un **fonds de travaux** séparé.
3. **Diversification** : des actifs financiers diversifiés, pas une seule entreprise ni un seul immeuble. Ces actifs ne sont pas soumis à l'IFI, contrairement à l'immobilier [R3-01].
4. **Une structure à statuts contraignants**, pour que la discipline ne dépende pas de la seule volonté du propriétaire : société civile avec un gérant indépendant, ou fiducie. À valider par un notaire et un avocat.
5. **Une gouvernance qui survit au fondateur** : comité avec au moins une personne indépendante, mandat de gestion, plan en cas d'incapacité.
6. **Une transmission organisée.**
   - Sans montage, les droits de succession en ligne directe prélèveraient environ **44 %** du capital à chaque génération [V2R-06] (ESTIMATION).
   - L'exonération de l'article 795 A ne vise que le monument et son mobilier [R3-13].
   - Dans la simulation, un décès en année 15 fait passer le risque d'échec à 30 ans de 5 % à 16 % (L6).
   - Pistes à étudier avec un notaire : démembrement, assurance-vie, donation-partage.
7. **Un contrat de mariage adapté.** En communauté réduite aux acquêts, les revenus réinvestis deviennent des biens communs [V2R-07] (à valider par un notaire).
8. **Une fiscalité organisée** :
   - château habité en direct ou en SCI familiale ;
   - jamais de logement de l'associé ni de chevaux de concours dans une holding patrimoniale (taxe de 20 %, dont l'assiette a déjà changé en cours de vote [R3-18] [V2R-11] [V2R-12]) ;
   - choix du véhicule du capital validé par un avocat fiscaliste.
9. **Un seuil de déclenchement.** N'engager le niveau de dépense d'un domaine que lorsque le capital en place, avec sa règle de dépense, couvre le besoin, réserve comprise.

---

## 7. Synthèse : qui peut financer quoi ?

| Source | Échelle de contribution | Récurrence | Résistance aux crises | Tranquillité | Dépendance au fondateur | Verdict |
|---|---|---|---|---|---|---|
| Capital affecté (actifs financiers, patrimoine du propriétaire) | **Illimitée** (≈ 1,75 % du capital) | Élevée (règle de dépense) | Moyenne : baisse des marchés, amortie par la réserve | Totale | Faible une fois constitué, sauf succession et gouvernance (§ 6.4) | **Socle de la solution** |
| Holding de PME | Élevée (4,4 à 7,1 % du capital) | Moyenne | Faible à moyenne | Totale | **Forte** | **Moteur de constitution du capital** |
| Logements, stockage, solaire, forêt | 0,02 à 0,1 M€ (S2) | Élevée (classe A) | Bonne | Bonne si zonée | Faible | Complément utile |
| Pensions de chevaux | ≈ 0 à 0,1 M€ | Élevée (classe B), très résistante en crise | Très bonne | Bonne | Moyenne | Autofinance une partie de la passion |
| Réceptions, séminaires, tournages, grande maison | 0 à 0,25 M€, très variable | Faible (classe C) | Mauvaise (−80 % en crise) | Médiocre | Moyenne à forte | Option plafonnée, jamais pour les charges fixes |
| Château-hôtel exploité | −1,1 à +0,6 M€ | Moyenne | Mauvaise | **Incompatible** | Forte | Rejeté comme moteur |
| Locataire d'ancrage (bail à un exploitant de séminaires) | 0,2 à 0,6 M€ brut en S2, 0,3 à 1,0 M€ en S3, si les conditions sont réunies ; 0 sinon | Élevée (classe A), sauf défaillance de l'exploitant | Moyenne : loyers variables −67 % en 2020 | **Faible** : 40 à 60 chambres d'hôtes, 15 à 30 ans | Faible | Option pour un grand domaine bien situé (S3) ; incompatible avec la partie privée de S2 |
| Location de luxe de la partie privée | −0,02 à +0,18 M€ (S2) | Faible (classe C) | Mauvaise | Le propriétaire quitte sa maison l'été | Moyenne | Complément marginal |
| Libération de capital (vente de communs, démembrement, copropriété) | Ponctuelle, montant INCONNU | Non | — | Voisins permanents, perte définitive | Faible | À verser à la dotation si l'opération a lieu |
| Visites | ≈ 0 ou négatif hors monuments célèbres | Saisonnière | Mauvaise | Médiocre | Moyenne | Rejeté comme moteur |
| Avantage fiscal MH | ≈ 9 % du besoin (S2, propriétaire très imposé) | Annuel | Dépend des revenus du propriétaire | Ouverture de 50 j/an pour 100 % | — | Levier, pas une recette |
| Subventions, Loto du patrimoine | Ponctuel | Non | — | — | — | Jamais dans le scénario central |

---

## 8. Ce que la vague 2 a changé

| Recherche | Apport | Effet sur le modèle et les conclusions |
|---|---|---|
| **V2A — bail à un exploitant** | Conditions d'entrée des exploitants de séminaires, loyer estimé, cadre juridique, contre-exemples (§ 3.4) | Nouveau moteur « bail d'ancrage » et modèle M7. Seule activité sur place à la bonne échelle, mais conditionnée par la localisation et incompatible avec une partie entièrement privée en S2 |
| **V2C — budgets réels et leviers** | Aucun budget complet de domaine privé de taille S2 publié ; rapport IGF-IGAC de 2020 ; temps d'entretien des jardins ; dérives INSEE sur 20 ans (§ 5) | Jardiniers de S3 portés de 11 à 16 (besoin de S3 de 3,47 à 3,64 M€) ; dérives réelles des travaux (+0,75 %/an), de l'énergie (+2 %/an) et des assurances (+1,85 %/an) recalées ; dotations recalculées (§ 6.1) |
| **V2D — libérer du capital, louer** | Opérations MH, démembrement, copropriété, location de luxe, dette participative (§ 3.5) | Nouveau moteur « location de luxe » et modèle M8. Aucun mécanisme ne finance durablement le fonctionnement ; le capital libéré une fois doit aller à la dotation |
| **V2V — vérification** | 90 chiffres clés vérifiés à la source : 81 confirmés, 9 nuancés, aucun faux | Notes et statuts corrigés dans le modèle (effectif du château-hôtel, échantillon des châteaux-hôtels, crédits des DRAC, prix du gaz, loyers ruraux) ; aucune valeur centrale modifiée |
| **V2R — équipe rouge** | 29 constats, dont 2 critiques : aucun véhicule juridique ne sépare le capital de la fortune du propriétaire ; le rendement net de 3 % n'était pas justifié (fichier `01_RECHERCHE/V2R_equipe_rouge.md`) | Rendement ramené à 2 % et retrait à 1,75 % ; sinistres payés en plus du fonds de travaux ; réserve reconstituée ; maîtrise d'œuvre ajoutée ; solutions redimensionnées à 5 % d'échec sur 30 ans ; § 6.3 et 6.4 réécrits (véhicules, succession, mariage). Le capital nécessaire passe d'environ 70 à environ 100 fois le besoin |

**Ce que la vague 2 confirme.** Les activités compatibles avec une résidence calme couvrent quelques pour cent du besoin. Le fonctionnement durable d'un grand domaine repose sur un **capital affecté**, constitué une fois puis géré avec une règle de dépense. Ce capital reste la fortune du propriétaire, et il est plus grand qu'annoncé avant l'équipe rouge : environ 100 fois le besoin annuel pour 95 % de chances de tenir 30 ans. Son dimensionnement dépend d'abord de la justesse du budget et du rendement net réellement obtenu.
