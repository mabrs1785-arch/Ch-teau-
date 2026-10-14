# L2 — Comment financer durablement ces coûts ? Analyse des solutions possibles

> **Statut et conventions**
> - Analyse fondée sur 8 agents de recherche (vague 1), 4 recherches ciblées (vague 2) et le modèle `02_MODELE/sorties/Modele_equation_chateau.xlsx`, feuilles Moteurs et Modeles.
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

1. **Le coin fiscal.** Le château est un lieu de vie : l'essentiel de son coût est privé. Il se paie donc avec de l'argent déjà taxé. Un euro de bénéfice d'une société à l'IS ne laisse que ≈ 0,51 € au propriétaire après IS (25 %) et PFU (31,4 % en 2026) [R3-16][R3-20][R3-57]. Le modèle applique une « fuite fiscale » de 30 % (15 à 49 %) aux bénéfices des activités qui servent à payer des coûts privés.
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
| Château-hôtel exploité | Sur 33 sociétés avec un CA ≥ 1 M€, 61 % sont en perte ; marge nette médiane de −6,3 % [R4-34][R4-35]. Au moins 15 liquidations de 2023 à 2026, et au moins 41 entités « château » de l'hôtellerie ou de la réception en procédure collective depuis 2024 [R4][R7-64]. Ygrande (hôtel et 26 boxes) en liquidation depuis le 28/10/2025 [R4][R7]. |
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
| Centre de reproduction (si vétérinaire et étalon) | B | 30 k€ | 21 k€ | 0 | 35 k€ |
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
  - Château-hôtel : 350 000 à 700 000 € d'investissement par chambre et ≈ 1,65 salarié par chambre [R7-41][R7-42][R7-43]. Projeté à 15 chambres, il **perd de l'argent dans le cas central**, ce que confirment les comptes réels (§ 2.2).

### 3.3 Foncier, énergie, dépendances [R8]

- **Logements dans les communs.**
  - Loyer de 6,8 à 10,9 €/m²/mois charges comprises en commune rurale [R8-22][R8-23].
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

### 3.4 Bail à un exploitant (« locataire d'ancrage »)

*Section complétée avec la recherche V2A (voir § 8).*

### 3.5 Libération de capital et location de luxe

*Section complétée avec la recherche V2D (voir § 8).*

### 3.6 Résultat : les activités sur place ne couvrent qu'une petite part du besoin

Six combinaisons comparées au besoin du domaine S2 (1,24 M€/an), après fuite fiscale :

| Modèle | Contribution disponible (central) | Couverture du besoin S2 (fav. / central / déf.) | Écart à financer (central) | Investissement |
|---|---:|---:|---:|---:|
| M1 — Socle contractuel et équestre standard | 49 k€ | 25 % / **4 %** / −1,5 % | 1 190 k€ | 1 100 k€ |
| M2 — Lieu d'exception à quota (M1 + réceptions, séminaires, grande maison) | 87 k€ | 53 % / **7 %** / −4 % | 1 152 k€ | 2 100 k€ |
| M3 — Équestre haut de gamme et services | 42 k€ | 21 % / **3 %** / −5 % | 1 197 k€ | 0 |
| M4 — Château-hôtel exploité + réceptions | −361 k€ | 88 % / **−29 %** / −57 % | 1 601 k€ | 7 900 k€ |
| M5 et M6 — Socle minimal + moteur extérieur | 5 k€ | 6 % / **0,4 %** / −2 % | 1 234 k€ | 0 |

**Lecture.** Le cas favorable cumule toutes les hypothèses heureuses. Même alors, aucune combinaison compatible avec une résidence calme ne couvre plus de la moitié du besoin. Dans le cas central, elles en couvrent **3 à 7 %**. Le château-hôtel peut couvrir l'essentiel dans le meilleur cas, mais il creuse le déficit dans le cas central, et les comptes réels confirment ce risque.

---

## 4. Leviers fiscaux, publics et juridiques [R3]

| Levier | Effet | Conditions | Limites |
|---|---|---|---|
| **Régime fiscal des MH** (CGI art. 156) | Charges foncières déductibles du **revenu global** : 100 % si le château est ouvert au public, 50 % s'il est fermé. Travaux subventionnés : 100 % [R3-02][R3-05] | Classé ou inscrit ; ouverture de 50 jours par an dont 25 non ouvrables d'avril à septembre, ou de 40 jours de juillet à septembre, 6 h par jour [R3-04] ; détention directe ou SCI familiale ; conservation 15 ans [R3-06] | Réduit l'**impôt personnel** : suppose des revenus imposables au barème. Exclut les parties exploitées commercialement [R3-04 § 40]. Pas d'excédent reportable si l'immeuble ne produit pas de recettes |
| **Subventions des DRAC** | 20 % (inscrit) à 40 % (classé) des travaux éligibles en moyenne [R1-34] | Dossier avant tout commencement de travaux [R1-03] | Crédits −29 % en 2026 [R1-33] ; versement avec plusieurs années de retard ; **jamais acquises** : à exclure du scénario central |
| **Loto du patrimoine, Fondation du patrimoine** | 148 000 à 280 000 € pour un site sélectionné, **une seule fois** [R1-12][R1-13][R1-16] | Sélection concurrentielle | Pas un revenu récurrent |
| **Mécénat via la Fondation du patrimoine** | Les donateurs déduisent 66 % de leur don de l'IR | Propriétaire personne physique ; **recettes commerciales ≤ 60 000 € HT par an** ; conservation et ouverture 10 ans [R3-10] | Fermé dès qu'il y a une vraie activité commerciale ; finance des travaux précis, pas le fonctionnement |
| **Exonération de droits de succession** (CGI art. 795 A) | 100 % de la valeur transmise exonérée | Convention perpétuelle : ouverture 50 jours par an, maintien du mobilier [R3-13][R3-14] | Pèse durablement sur la tranquillité ; sert la transmission, pas le fonctionnement |
| **TVA équestre à 5,5 %** (depuis 2024) | Pension « accessoire à la pratique », enseignement, accès aux installations [R3-22] | Frontière fragile avec la pension à 20 % (valorisation, retraite, box sans soins) | À valider par un expert-comptable |
| **IFI** | Aucune exonération pour les MH ; abattement de 30 % sur la résidence principale [R3-01][R3-15] | — | 10 550 €/an en S2, 51 940 € en S3 (résidence principale) |
| **Taxe de 20 % sur les holdings patrimoniales** (LF 2026) | — | Holding ≥ 5 M€ d'actifs, revenus passifs > 50 % [R3-18] | Vise les **logements réservés à l'associé** et les **chevaux de concours**. Ne jamais loger le château habité ni les chevaux personnels dans une telle holding |
| **Structure** | Partie privée en direct ou en SCI familiale à l'IR ; activités en société d'exploitation payant un loyer de marché [R3, Q9] | SCI à l'IR : activité commerciale < 10 % de son CA [R3-59] | Logement gratuit dans une société à l'IS : acte anormal de gestion et revenu distribué [R3-56] |

**Effet chiffré du levier MH.** Hypothèses : taux marginal de 41 %, 45 % du besoin en charges déductibles, déduction de 50 % (château fermé au public). L'économie d'impôt est d'environ 9 % du besoin, soit ≈ 115 k€/an en S2. C'est un levier réel **pour un propriétaire qui a de gros revenus imposables**. Ce n'est pas une recette du domaine. Le Monte-Carlo l'intègre dans la variante « leviers » (§ 6).

---

## 5. Leviers de réduction du besoin (« prestige efficace »)

*Section complétée avec la recherche V2C (voir § 8).*

Leviers déjà quantifiés par le modèle :
- **Personnel.** Chaque ETP coûte de 24 k€ (soigneur) à 79 k€ (régisseur) [R2-11]. Gouvernante et ouvrier agricole supprimés, avec fenaison sous-traitée : −50 à 70 k€/an en S2.
- **Jardins.** Les jardins réguliers concentrent le personnel : jusqu'à 1,4 jardinier par hectare [R2-15]. Ramener 2 ha de jardins réguliers à 0,5 ha, autour du château, et traiter le reste en parc pâturé réduit le besoin d'environ 1 à 2 ETP.
- **Énergie.** Zonage du chauffage (chauffer 700 m² au lieu de 1 000 m²) et bois ou plaquettes du domaine : −10 à 20 k€/an.

---

## 6. Le moteur extérieur : dotation affectée ou entreprise

### 6.1 Combien faut-il ?

Le modèle simule 30 ans de vie du domaine, 6 000 à 20 000 trajectoires par cas. Aléas tirés au sort :
- crises (une tous les 12 ans en moyenne) ;
- rendements de marché ;
- bruit propre aux activités ;
- sinistres non assurés ;
- dépassements de travaux ;
- prix de l'énergie ;
- dérive des salaires.

Le capital de la dotation est investi en actifs financiers diversifiés, avec un rendement réel net de 3 % annualisé [R8-32][R8-34]. Retraits encadrés par une **règle de dépense lissée** (plafond de 2,75 % du capital), plus des **règles de pilotage** en période de tension :
- coupe temporaire de 10 % des dépenses discrétionnaires ;
- report de 30 % d'une campagne de travaux ;
- retrait d'urgence plafonné à 4 %.

**Échec** = réserve de trésorerie négative.

| Domaine | Besoin annuel | Dotation : 1 chance sur 2 de tenir 30 ans | Dotation : 95 % de chances | Variante leviers (MH + besoin −15 %) : 50 % / 95 % |
|---|---:|---:|---:|---:|
| S1 | 0,33 M€ | 9 M€ (≈ 28 × le besoin) | 22 M€ (≈ 67 ×) | 7 M€ / 16 M€ |
| S2 | 1,24 M€ | 35 M€ (≈ 28 ×) | 82 M€ (≈ 66 ×) | 26 M€ / 61 M€ |
| S3 | 3,47 M€ | 101 M€ (≈ 29 ×) | 255 M€ (≈ 73 ×) | 75 M€ / 193 M€ |

Fichier `02_MODELE/sorties/mc_dotation_necessaire.json`, produit par `calculer_mc.py`. Le seuil de 95 % est estimé par dichotomie sur 6 000 trajectoires, avec une précision d'environ ±5 %.

**Règle d'or qui en découle :**
- il faut environ **30 fois le besoin annuel** pour avoir une chance sur deux de tenir 30 ans ;
- il en faut environ **65 à 70 fois** pour être raisonnablement sûr (95 %).

Le multiple dépasse le simple « besoin ÷ 2,75 % » (36 ×) pour deux raisons :
- les coûts du domaine montent plus vite que l'inflation (salaires +0,5 % réel par an [D-01], énergie, travaux) ;
- les mauvaises années de marché arrivent parfois au mauvais moment.

### 6.2 Entreprise extérieure ou holding de PME

- **Rendement brut plus élevé.** Une PME reprise sans dette rapporte au propriétaire ≈ 0,40 € net de dividende par euro d'EBITDA (IS puis PFU) [R8-35][R3-16][R3-20]. Rachetée à 5 à 8 fois l'EBITDA, elle rend donc 5 à 8 % du capital investi, contre 2,75 % pour une dotation financière.
- **Mais elle est fragile seule.** Plus d'une transmission de PME sur cinq échoue dans les six ans (données OSEO 1997-2003) [R8-36]. Modélisé à 3,5 % de défaillance par entreprise et par an, une holding de 5 PME qui ne fait que distribuer ses dividendes échoue dans 65 à 87 % des cas sur 30 ans : les entreprises disparaissent une à une (`mc_holding_hybride.json`).
- **Elle dépend du fondateur.** Il faut des dirigeants salariés, des réinvestissements et une surveillance permanente.
- **Elle doit être sans dette d'acquisition** au moment où elle finance le domaine. Une PME en LBO ne distribue presque rien pendant 5 à 7 ans [R8].

**Conséquence.** L'entreprise est le meilleur **outil pour construire le capital**, mais pas une rente perpétuelle. La pérennité vient de la **conversion progressive des dividendes en dotation diversifiée** (§ 6.3).

### 6.3 Conditions de pérennité d'un moteur extérieur

1. **Séparation et affectation.** Le capital est logé dans une structure dédiée au domaine. Ce n'est pas la fortune personnelle au sens courant : c'est une dotation affectée, sur le modèle des « maintenance funds » britanniques [R5-17][R5-18].
2. **Règle de dépense écrite** : plafond lissé de 2,75 % du capital, pas plus en temps normal.
3. **Réserve de liquidité** d'au moins un an de besoin, et **fonds de travaux** séparé.
4. **Diversification** : actifs financiers diversifiés, pas une seule entreprise ni un seul immeuble. Ces actifs **ne sont pas soumis à l'IFI**, contrairement à l'immobilier locatif.
5. **Gouvernance indépendante du fondateur** : mandat de gestion, comité, règles écrites. L'objectif est que le domaine survive à une incapacité du propriétaire.
6. **Fiscalité organisée** :
   - château habité en direct ou en SCI familiale ;
   - jamais dans une holding patrimoniale (taxe de 20 % [R3-18]) ;
   - enveloppes de capitalisation pour la dotation, à valider par un fiscaliste.
7. **Seuil de déclenchement.** N'engager le niveau de dépense d'un domaine que lorsque le moteur en place couvre au moins 100 % du besoin résiduel avec la règle de dépense, plus la réserve.

---

## 7. Synthèse : qui peut financer quoi ?

| Source | Échelle de contribution | Récurrence | Résistance aux crises | Tranquillité | Dépendance au fondateur | Verdict |
|---|---|---|---|---|---|---|
| Dotation affectée (actifs financiers) | **Illimitée** (≈ 2,75 % du capital) | Élevée (règle de dépense) | Moyenne : baisse des marchés, amortie par la réserve | Totale | Faible une fois constituée | **Socle de la solution** |
| Holding de PME | Élevée (5 à 8 % du capital) | Moyenne | Faible à moyenne | Totale | **Forte** | **Moteur de constitution du capital** |
| Logements, stockage, solaire, forêt | 0,02 à 0,1 M€ (S2) | Élevée (classe A) | Bonne | Bonne si zonée | Faible | Complément utile |
| Pensions de chevaux | ≈ 0 à 0,1 M€ | Élevée (classe B), très résistante en crise | Très bonne | Bonne | Moyenne | Autofinance une partie de la passion |
| Réceptions, séminaires, tournages, grande maison | 0 à 0,25 M€, très variable | Faible (classe C) | Mauvaise (−80 % en crise) | Médiocre | Moyenne à forte | Option plafonnée, jamais pour les charges fixes |
| Château-hôtel exploité | −1,1 à +0,6 M€ | Moyenne | Mauvaise | **Incompatible** | Forte | Rejeté comme moteur |
| Visites | ≈ 0 ou négatif hors monuments célèbres | Saisonnière | Mauvaise | Médiocre | Moyenne | Rejeté comme moteur |
| Avantage fiscal MH | ≈ 9 % du besoin (S2, propriétaire très imposé) | Annuel | Dépend des revenus du propriétaire | Ouverture de 50 j/an pour 100 % | — | Levier, pas une recette |
| Subventions, Loto du patrimoine | Ponctuel | Non | — | — | — | Jamais dans le scénario central |

---

## 8. Compléments de la vague 2

*Cette section intègre les recherches ciblées V2A (bail à un exploitant), V2C (budgets réels et leviers) et V2D (opérations MH, démembrement, location de luxe, copropriété).*
