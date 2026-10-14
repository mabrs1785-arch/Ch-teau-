# Domaines remarquables — benchmark et intelligence économique (Agent 7)

Date de recherche : 2026-10-14. Toutes les références [Sxx] renvoient à `_brut/sources_agent7.csv`.
Statuts : **PAGE LUE** (page ou registre ouvert et lu), **EXTRAIT** (résultat de recherche seulement), **ESTIMATION** (calcul ou raisonnement explicite), **INCONNU**.

> **Avertissement de lecture.** Le chiffre d'affaires (CA) n'est pas la rentabilité, et la rentabilité n'est pas la fortune des propriétaires. Un CA de 2 M€ avec un résultat net nul (Mercuès) n'a rien d'une réussite financière. Une fortune personnelle qui absorbe 1,5 M€ de pertes par an (Haras de Hus) ne prouve pas que le domaine soit viable.

---

## 0. Méthode et accès aux comptes (ce qui a marché / échoué)

| Registre | Accès le 2026-10-14 | Usage |
|---|---|---|
| Pappers.fr | **403 refusé** (outil WebFetch et curl) | non utilisé |
| annuaire-entreprises.data.gouv.fr | bloqué (protection anti-robot, boucle de redirections) | non utilisé |
| **recherche-entreprises.api.gouv.fr** (API officielle) | OK mais instable (coupures fréquentes) | identification des SIREN [S01] |
| **data.economie.gouv.fr, jeu « ratios_inpi_bce »** | OK | **CA, EBE et résultat net sur plusieurs années, issus des comptes déposés à l'INPI** [S02-S13] |
| **BODACC (API opendatasoft DILA)** | OK | procédures collectives, cessions de fonds, dépôts de comptes [S14-S23] |
| societe.com | OK par moments (429 puis 200) | contrôle croisé [S24-S26] : chiffres **identiques** aux ratios INPI |
| **Companies House (UK)** | OK. Les comptes sont des PDF scannés, lus par OCR (rapidocr) | comptes UK [S27-S34] |
| **Charity Commission (UK)** | OK | revenus et dépenses sur 5 ans [S35-S38] |
| CRO (Irlande, core.cro.ie) | **403 refusé** | comptes irlandais pris dans la presse qui les cite [S51, S53] |
| WebFetch (outil) | échec DNS sur tous les domaines | remplacé par curl via le proxy |

**Pièges de lecture identifiés :**
1. Dans le jeu INPI, une société qui opte pour la **confidentialité du compte de résultat** (art. L.232-25) affiche CA = 0 et EBE = 0, alors que son résultat net reste visible au bilan. **Un CA = 0 signifie « non communiqué » (NC)**, pas une activité nulle : societe.com affiche « NC » pour les mêmes années [S24, S25].
2. Type de bilan : « C » = comptes sociaux, « K » = comptes consolidés (cas Fontenille).
3. Au Royaume-Uni, les petites sociétés ne déposent pas leur compte de résultat. Quand seul le bilan est disponible, je déduis le résultat de la **variation du report à nouveau** (« profit and loss reserve »). Cette variation est égale au bénéfice diminué des distributions. Je le signale par « déduit du bilan ».

**Classement demandé.** **A** = excédent **récurrent** démontré par des comptes (au moins 2 exercices récents positifs). **B** = CA connu, rentabilité inconnue, nulle ou négative. **C** = aucun chiffre d'exploitation vérifiable.

---

## 1. Tableau de synthèse

| # | Domaine (pays) | Acquéreur / porteur et situation de départ | Prix d'achat connu | Activités | CA vérifiable | Résultat vérifiable | Classe |
|---|---|---|---|---|---|---|---|
| 1 | Château de la Motte-Husson (FR-53) | Dick & Angel Strawbridge, couple britannique (TV, pâtisserie) | **£280 000** (2015) [S41] | mariages, événements, gîtes, TV | NC (confidentiel) | SARL DA2AD : **RN +811 k€ (2022)**, +5,6 k€ (2023) [S13, S26]. Chateau Television Ltd : capitaux propres £845 k [S27] | **A** (CA inconnu) |
| 2 | La Mothe-Chandeniers (FR-86) | Dartagnans (start-up) + 18 558 internautes | **500 000 €** (2017) [S39] | visites, chantier participatif | NC (comptes confidentiels) [S21] | INCONNU | **C** |
| 3 | Saint-Fargeau (FR-89) | Frères Michel et Jacques Guyot, sans fortune connue | **500 000 F ≈ 280 k€** (1979) [S42] | visites, son et lumière (60 cavaliers), chambres | INCONNU (entreprise individuelle) | INCONNU | **C** |
| 4 | Guédelon (FR-89) | Michel Guyot, Maryline Martin (création ex nihilo) | sans objet | visites (≈265-300 k visiteurs), pédagogie | **6,33 M€ (2024)** [S02, S24] | **RN +333 k€ (2024)**, +879 k€ (2023). Cumul 2016-2025 : **+4,43 M€** | **A** |
| 5 | Château de Bourneau (FR-85) | Couple de 31 ans (2018) | INCONNU (≈500 k€ estimé par le journaliste) [S57] | gîtes, chambres d'hôtes, réceptions | NC | NC (comptes déposés chaque année jusqu'à 2025, confidentiels) [S22] | **C** |
| 6 | Château de Fabiargues (FR-30) | Jeune couple parisien (≈2020) | INCONNU | 5 chambres d'hôtes, salle de réception | INCONNU | INCONNU (prêt d'honneur 20 k€) [S56] | **C** |
| 7 | Gwrych Castle (UK-Pays de Galles) | Mark Baker, trust caritatif fondé par un passionné | INCONNU (achat 2018 financé par une subvention du NHMF) [S43] | visites, tournage TV (« I'm a Celebrity ») | revenus £0,61-0,97 M/an [S38] | excédent 4 années sur 5 (2024 : +£42 k) | **A** (charity) |
| 8 | Castle Leslie (IE) | Sammy Leslie, héritière d'un domaine sans trésorerie | hérité | hôtel, **centre équestre**, mariages, spa | **≈10 M€** (presse, 2019) [S52] | « désormais rentable » (presse, sans comptes) | **B** |
| 9 | Vaux-le-Vicomte (FR-77) | Famille Sommier puis de Vogüé (achat 1875) | non pertinent | visites (300 k), événements, restauration | SEG ≈1,6-2,1 M€, SERV ≈2,4 M€ (2016-19) [S03, S04] | positif 2016-2023, **légèrement négatif 2024-2025** | **A → B** |
| 10 | Domaine de Chantilly, Grandes Écuries (FR-60) | Fondation créée en 2005 avec l'Aga Khan | non pertinent | château, musée du Cheval, spectacles équestres | 3,5 M€ (domaine annexe, Wikipédia) [S44] | RN 1,4-1,5 M€ (même source, non datée) | **B** |
| 11 | Château de Mercuès (FR-46) | Famille Vigouroux (vins de Cahors), depuis 1983 [S60] | INCONNU | hôtel de 30 chambres, vignoble | **≈2,0-2,2 M€/an** [S05] | RN entre -126 k€ et +326 k€. Cumul 2017-2024 : +0,10 M€ | **B** |
| 12 | Les Domaines de Fontenille (FR) | F. Biousse et G. Foucher (anciens dirigeants du textile) | INCONNU | collection d'hôtels dans des demeures historiques | **33,8 M€ consolidé (2024)** [S07] | RN consolidé **-2,9 M€ (2024)**, -6,8 M€ (2023) | **B (négatif)** |
| 13 | Haras de la Cense (FR-78) — **équestre** | William Kriegel, industriel (achat en 1980) [S46] | INCONNU | formation en équitation éthologique, hébergement | ≈1,1-1,2 M€ (2023-24) [S11] | pertes de 0,57 à 1,15 M€/an (2015-2020), ≈0 depuis 2022 | **B** |
| 14 | Hickstead (UK) — **équestre** | Douglas Bunn, fortune faite dans les caravanes [S47] | INCONNU | concours de saut d'obstacles, réceptions | NC | +£205 k sur l'exercice clos au 31/01/2026 (déduit du bilan) [S32] | **A partiel** |
| 15 | Badminton Horse Trials (UK) — **équestre** | Société du domaine | sans objet | concours complet international | NC | +£539 k sur l'exercice clos au 30/09/2025 (déduit du bilan) [S31] | **A partiel** |
| 16 | Burghley House et Horse Trials (UK) — **équestre** | Trust caritatif familial | sans objet | visites, événements, concours complet | trust £17,7 M. Concours **£5,35 M** [S37, S30] | trust : excédent £1,2 M. Concours : **+£22,5 k** (0,4 %) | **A** |
| 17 | Blenheim et Chatsworth (UK) | Trusts caritatifs | sans objet | visites, commerce, événements | £31,0 M et £19,4 M [S36, S35] | excédents de £3,2 M et £2,0 M | **A** (repère d'échelle) |
| 18 | Highclere Castle (UK) | Famille Carnarvon (« Downton Abbey ») | sans objet | visites (≈70 jours/an), mariages | INCONNU | INCONNU | **C** |

**Contre-exemples** (détail en section 3) :

| # | Domaine | Issue | Chiffres clés |
|---|---|---|---|
| CE1 | Haras de Hus (FR-44) — **équestre** | élevage arrêté et domaine mis en vente | **EBE cumulé 2015-2024 : -15,8 M€** [S08] |
| CE2 | Château d'Ygrande (FR-03) — **hôtel avec centre équestre** | **liquidation judiciaire de l'hôtel (2025)**, liquidation du haras clôturée pour insuffisance d'actif (2026) | CA ≈1,1 M€, EBE entre -0,10 et +0,06 M€ [S09, S14, S15] |
| CE3 | Château de Brindos (FR-64) | sauvegarde (2017), redressement (2018), **liquidation (2019)** | CA ≈2 M€, RN de -0,6 à -0,87 M€/an [S10, S16] |
| CE4 | Château de Bricquebec (FR-50), hôtel | redressement (2021), **liquidation (2022)**, clôture pour insuffisance d'actif (2024) | fonds acheté **395 k€** (2017), revendu **200 k€** (2021) [S17] |
| CE5 | Château de Charfetain (FR-69), gîtes et réceptions | créée en 2019, **liquidation (2025)** | aucun compte public [S18] |
| CE6 | Château de Bernesq | créée en 2021, **liquidation simplifiée (2026)** | aucun compte public [S19] |
| CE7 | Ballyfin (IE) | rentable de justesse en 2025 | CA 8,1 M€, bénéfice 32 k€, **pertes cumulées 37,6 M€** [S51] |
| CE8 | Adare Manor (IE) | pertes 2023, 2024 et 2025 | achat **30 M€** + **≈50 M€** de travaux [S53, S54] |
| CE9 | Bolesworth Events (UK) — **équestre** | capitaux propres **-£4,5 M** | perte d'environ £551 k sur l'exercice clos au 31/03/2025 (déduit du bilan) [S33] |
| CE10 | Gwrych avant 2018 (UK) | deux acquéreurs privés en échec (1989, 2007), dont un placé sous administration judiciaire | £750 k (1989), £850 k (2007) [S43] |

---

## 2. Fiches des cas

### Cas 1 — Château de la Motte-Husson (Martigné-sur-Mayenne) — Strawbridge — **A (CA inconnu)**
- **Acquéreur et départ :** Dick Strawbridge et Angela (« Angel ») Adoree, couple britannique avec deux jeunes enfants. Ils cherchaient d'abord de petites fermes, puis ont compris qu'au prix du marché français ils pouvaient acheter un château [S41, PAGE LUE]. Wikipédia relie Angel à l'entreprise « Vintage Patisserie » et à l'émission Dragons' Den : ce sont des entrepreneurs, pas des héritiers connus (patrimoine initial INCONNU).
- **Achat :** en 2015 pour **£280 000** : 12 acres (4,9 ha), 45 pièces, 7 dépendances, potager clos, douves. Château inhabité depuis quarante ans [S41].
- **Financement et chronologie :** Channel 4 diffuse la série « Escape to the Chateau » à partir de juin 2016. La chaîne a payé pour filmer le chantier, ce qui « a couvert une partie des dépenses », et l'émission a fait la publicité de l'activité mariages [S41]. Pas de mariages en 2020-2021 (Covid), reprise en 2022 [S41].
- **Structures (registres) :**
  - Chateau-De-La-Motte Husson Ltd (UK, 2017, aujourd'hui dissoute ; mandat de Richard Strawbridge [S29]) : capitaux propres de **-£19 230** en 2021, quasi dormante [S28].
  - **Chateau Television Ltd** (UK, 2020) : au 31/12/2025, capitaux propres **£845 298** (contre £793 796 un an plus tôt, soit **+£51,5 k**), trésorerie **£1,84 M**, 2 salariés. Le compte de résultat n'est pas déposé [S27, OCR].
  - **DA2AD SARL** (FR, créée en avril 2022, capital 2 400 €, gérants Richard et Angela Strawbridge) : événements, gîtes, chambres d'hôtes, contenus audiovisuels [S23]. Compte de résultat confidentiel. **Résultat net 2022 : +811 446 €. 2023 : +5 632 €** [S13]. Le chiffre 2023 est confirmé par societe.com [S26].
- **Leçon :** une entrée très bon marché, des années de travaux faits en grande partie par le couple, et surtout un **revenu média** qu'un projet ordinaire ne peut pas reproduire. Les résultats visibles proviennent pour partie de la société de télévision. Le CA de l'activité château reste INCONNU.

### Cas 2 — Château de La Mothe-Chandeniers (Les Trois-Moutiers) — financement participatif — **C**
- **Montage :** Dartagnans et l'association Adopte un château lancent en 2017 une campagne de financement participatif. Prix d'achat **500 000 €**, atteint le 1/12/2017. La campagne se clôt le 25/12/2017 à **1 617 000 €** versés par **18 558 contributeurs** de 115 pays. Une SAS est créée le 5/02/2018 : chaque donateur peut en devenir actionnaire, à 1 € la part [S39, PAGE LUE].
- **Suite :** 2e campagne en 2018, **474 000 €**, pour la chapelle, 2,1 ha de parc et des dépendances. 3e campagne en décembre 2020. Travaux phase 1 (sécurisation) : budget **850 000 €** à partir de janvier 2019. Chantier global estimé à **7 ans** [S39].
- **Difficultés :** en mars 2021, l'hebdomadaire le7.info enquête sur des actionnaires qui critiquent une gestion « trop éloignée des promesses initiales ». Le responsable du développement et l'association Adopte un château quittent le projet, notamment après l'achat du château de Vibrac par Dartagnans en 2020. D'anciens stagiaires décrivent des conditions de travail difficiles. Le site compte de nombreux bénévoles [S55, PAGE LUE].
- **Comptes :** déposés (exercice 2024 déposé en 2026) **avec déclaration de confidentialité** [S21]. Ni CA ni résultat accessibles. Augmentation de capital en 2026 [S21].
- **Leçon :** la foule peut financer l'achat et les premiers travaux, mais pas l'exploitation. La gouvernance devient un sujet à part entière.

### Cas 3 — Château de Saint-Fargeau (Yonne) — frères Guyot — **C**
- **Achat :** en 1979, Michel et Jacques Guyot achètent le château et le domaine, avec le soutien des collectivités locales, pour **500 000 F, soit environ 280 000 €** hors jardins. Une société belge propriétaire depuis 1968 venait de renoncer devant l'ampleur des travaux [S42, PAGE LUE].
- **Transformation :** réfection complète des toitures, ouverture à la visite, location de chambres. Un **son et lumière** est organisé par l'association « Les Amis du château » pour financer la restauration : 600 acteurs et **soixante cavaliers** [S42]. En 1987, Jacques reprend La Ferté-Saint-Aubin [S42]. Michel Guyot cofonde ensuite Guédelon (cas 4).
- **Comptes :** Michel Guyot apparaît au BODACC comme entreprise individuelle à Saint-Fargeau (348654369) [S74]. Le lien avec l'exploitation du château est probable mais non vérifié. Il n'y a **pas de comptes publics** : le CA et le résultat sont INCONNUS.
- **Leçon :** c'est le modèle historique de « l'acquéreur non fortuné » : achat bas, soutien local, **bénévolat associatif** et spectacle équestre pour générer des recettes, sur des décennies.

### Cas 4 — Guédelon (Treigny) — **A**
- **Nature :** ce n'est pas un rachat mais une création entrepreneuriale autour d'un château : un chantier médiéval ouvert en 1998. La SAS (créée en 2006) a remplacé l'association. Elle est détenue principalement par Michel Guyot et Maryline Martin et **ne reçoit pas de subventions** [S40]. Selon societe.com, le fonds a été acquis auprès de l'association « Les Amis du Chantier Médiéval » pour 246 000 € [S24]. Une « Société civile des salariés de Guédelon » existe [S01].
- **Fréquentation :** 80 000 visiteurs la première année, plus de 300 000 en 2015, 265 000 en 2022. Plus de 100 emplois et 650 bénévoles (2018) [S40].
- **Comptes (INPI, PAGE LUE)** [S02], contrôlés sur societe.com [S24] :

| Exercice | CA | EBE | Résultat net |
|---|---|---|---|
| 2016 | 4,38 M€ | 0,59 M€ | 0,27 M€ |
| 2019 | 6,35 M€ | 1,24 M€ | 0,49 M€ |
| 2020 (Covid) | 2,88 M€ | 0,07 M€ | 0,005 M€ |
| 2023 | 6,03 M€ | 1,43 M€ | 0,88 M€ |
| 2024 | 6,33 M€ | 0,84 M€ | 0,33 M€ |
| 2025 | NC | NC | 0,45 M€ |

  Résultat net positif **10 années sur 10**. Cumul 2016-2025 : **+4,43 M€** (ESTIMATION par somme). Marge nette généralement de 5 à 15 % (0,2 % en 2020, 23 % en 2021). L'autonomie financière passe de 45 % à 79 %.
- **Leçon :** un **produit de visite unique** associé à une masse de visiteurs (300 k), sans hébergement, peut s'autofinancer. Cela suppose une échelle touristique qu'un domaine équestre privé n'atteindra pas.

### Cas 5 — Château de Bourneau (Vendée) — couple de 31 ans — **C**
- Jean-Baptiste Fois et sa compagne Erin, 31 ans, achètent en 2018 le château et **16 ha**. Ce n'est « ni un héritage ni un gain au Loto ». Les dépendances sont habitables, le corps principal est à refaire en entier. Le projet combine réceptions et mariages, chambres d'hôtes et location des dépendances. Les travaux sont faits eux-mêmes, avec des connaissances payées en séjours gratuits [S57, PAGE LUE]. **Prix non communiqué** : les « ≈500 000 € » sont une estimation du journaliste, non vérifiée.
- **Société probable :** SARL « Bourneau Événements » (842171712), capital **3 000 €**, créée en 2018, siège transféré en 2019 au 14 rue du Château à Bourneau. Activité : gîtes, chambres d'hôtes, location. Comptes **déposés chaque année jusqu'à l'exercice clos le 30/06/2025, en mode confidentiel** [S22]. Le lien avec le couple est déduit de l'adresse et de l'activité (non confirmé nommément).
- **Leçon :** la structure est encore en activité 7 ans après l'achat, ce qui indique une survie. Sa rentabilité est inconnue.

### Cas 6 — Château de Fabiargues (Saint-Ambroix, Gard) — jeune couple — **C**
- Ève et Joane Dupuis, couple d'origine parisienne, achètent vers 2020 une bâtisse du XIXe siècle : une ancienne maison de retraite abandonnée au milieu des années 2010, dans un parc de près de **2 ha**. Ils rénovent pendant deux ans, en partie eux-mêmes avec des amis et en partie avec des artisans locaux. Ouverture en avril 2022 de **5 chambres d'hôtes et d'une salle de réception**. Un traiteur occupe les anciennes cuisines du domaine. Ils obtiennent un **prêt d'honneur à 0 % de 20 000 €** d'Initiative Gard, qualifié de « décisif » [S56, PAGE LUE, article partiellement payant].
- Société non identifiée. Chiffres INCONNUS.
- **Leçon :** les dispositifs d'accompagnement (prêt d'honneur, Initiative France) existent pour ce type de projet, mais pour des montants modestes.

### Cas 7 — Gwrych Castle (Abergele, Pays de Galles) — Mark Baker — **A (charity)**
- Mark Baker, historien, milite pour sauver le château **depuis l'âge de 12 ans**. Le trust qu'il a fondé achète en 2018 le château et environ **200 acres** (80 ha) grâce à **une subvention du National Heritage Memorial Fund**. Une partie du domaine est louée à Natural Resources Wales pour 999 ans [S43, PAGE LUE]. Le château sert de décor à l'émission d'ITV « I'm a Celebrity… » en 2020-2021 [S43].
- **Comptes (Charity Commission, PAGE LUE)** [S38] :

| Exercice | Revenus | Dépenses | Solde |
|---|---|---|---|
| 2020 | £628 k | £287 k | +£342 k |
| 2021 | £965 k | £598 k | +£368 k |
| 2022 | £611 k | £880 k | **-£269 k** |
| 2023 | £627 k | £443 k | +£184 k |
| 2024 | £765 k | £723 k | +£42 k |

- **Leçon :** le montage « trust caritatif + subvention patrimoniale + effet média » permet à un passionné sans capital de **contrôler** un grand domaine, sans en être propriétaire à titre personnel.

### Cas 8 — Castle Leslie Estate (Glaslough, Irlande) — **centre équestre** — **B**
- Domaine de 1 000 acres, dans la famille Leslie depuis 1665. Sammy Leslie le reprend à son père Desmond. Elle comprend qu'en l'ouvrant à une activité commerciale elle peut le sauvegarder et le rénover avec les bénéfices. Elle ajoute « un centre équestre de niveau international », des soins et une école de cuisine [S52, PAGE LUE].
- **Chiffres (presse, pas de comptes) :** une « entreprise de **10 M€** » en 2019, avec une croissance du CA de **300 %** sur la décennie précédente. Elle est décrite comme « désormais rentable », ce qui a permis d'obtenir des financements pour 21 chambres supplémentaires (le Lodge) [S52]. « Le rêve de Sammy : de grands chevaux, de la bonne cuisine et l'hospitalité à l'ancienne » [S52].
- **Comptes :** le registre irlandais (CRO) est inaccessible (403). La rentabilité n'est **pas vérifiée par des comptes**.
- **Leçon :** **c'est le modèle le plus proche du projet**, des chevaux au cœur d'une offre hôtelière. Il a demandé environ 25-30 ans et une base foncière héritée.

### Cas 9 — Vaux-le-Vicomte (Maincy) — **A puis B**
- Propriété privée depuis l'achat d'Alfred Sommier en juillet 1875, aujourd'hui portée par la SCI Valterre (famille de Vogüé). Budget annuel de **8 M€**, 75 salariés à temps plein, plus de 300 000 visiteurs [S45, PAGE LUE].
- **Comptes partiels (INPI)** :
  - SEG Domaine de Vaux-le-Vicomte (784956609) : CA de 1,60 à 2,07 M€ entre 2016 et 2019, RN de +52 k€ à +140 k€. Puis 2024 : -9,7 k€, 2025 : -29 k€ [S03].
  - SERV, restauration (510258296) : CA 2,43 M€ et RN +278 k€ en 2018. CA 2,67 M€ et RN -2,5 k€ en 2025 [S04].
  - Cumul 2016-2025 : SEG +0,71 M€, SERV +1,00 M€ (ESTIMATION).
- **Leçon :** même un monument majeur et très fréquenté dégage des marges faibles, avec des pertes légères récentes. Le périmètre des comptes trouvés ne couvre pas tout le domaine.

### Cas 10 — Domaine de Chantilly et Grandes Écuries — **équestre** — **B**
- En 2005, face aux difficultés de gestion de l'Institut de France, une fondation est créée « à l'initiative et avec le soutien financier » de l'Aga Khan. Elle gère le château, le parc et les **Grandes Écuries avec le Musée du Cheval**. **20 M€** d'investissements de restauration, soutenus par la Région et le Département [S44, PAGE LUE].
- Les autres terrains (golf, polo, pistes de France Galop, hippodrome) génèrent **3,5 M€ de CA et 1,4-1,5 M€ de résultat net**, entièrement reversés à la fondation [S44]. Ces chiffres ne sont **pas datés** et ne sont pas confirmés par des comptes. Les comptes de la fondation (SIREN 488607581) ne figurent pas dans le jeu INPI.
- **Leçon :** le pôle équestre spectaculaire est **adossé à des loyers fonciers** (golf, polo, galop) et au mécénat d'une grande fortune.

### Cas 11 — Château de Mercuès (Lot) — **B**
- Propriété de la famille Vigouroux (vins de Cahors) depuis 1983. Hôtel de **30 chambres** et suites, restaurant, vignoble [S60, PAGE LUE].
- **Société hôtelière (328400106)** [S05] : CA 2,15 M€ (2019), 1,48 M€ (2020), **2,18 M€ et RN +326 k€ (2021)**, puis 2,15 M€ et -39 k€ (2022), 2,10 M€ et +1,2 k€ (2023), **2,01 M€ et -126 k€ (2024)**. Taux d'endettement entre 178 % et 1 343 %.
- **Groupe Georges Vigouroux SAS** : CA 3,74 M€ et **RN -1,32 M€ en 2024**, capitaux propres négatifs [S06].
- **Leçon :** un hôtel-château de 30 chambres, bien établi, **tourne autour de 2 M€ de CA et d'un résultat proche de zéro**.

### Cas 12 — Les Domaines de Fontenille — **B (négatif)**
- Groupe fondé en 2015 par Frédéric Biousse et Guillaume Foucher. Ils ont « toujours acheté les murs », ce qui représente « un investissement conséquent (acquisition et travaux) ». Ils évoluent vers un modèle à moindre investissement (location des murs, contrats de gestion) et indiquent que 55 % du CA vient de clients déjà venus [S58, PAGE LUE].
- **Comptes consolidés (type K)** [S07] : 2023 : CA **31,7 M€**, EBE -2,43 M€, **RN -6,78 M€**. 2024 : CA **33,8 M€**, EBE +0,70 M€, **RN -2,89 M€**. La holding (comptes sociaux) cumule environ -11,4 M€ entre 2016 et 2024 (ESTIMATION).
- **Leçon :** **33 M€ de CA ne font pas une rentabilité**. Acheter les murs et les rénover pèse plusieurs années sur les résultats.

### Cas 13 — Haras de la Cense (Rochefort-en-Yvelines) — **équestre** — **B**
- William Kriegel, industriel, achète La Cense en 1980 à Raymond Loewy. Il y fonde un élevage de quarter horses en 1985, arrêté en 2009. Le domaine se consacre à l'équitation éthologique à partir de 2000 et obtient l'agrément de la FFE en 2003 [S46, PAGE LUE].
- **Le Haras de la Cense (350681524)** [S11] : RN -905 k€ (2015), -830 k€ (2016), -1 147 k€ (2019), -568 k€ (2020), puis +54 k€ (2022). En 2023-2024 : **CA 1,14-1,17 M€, EBE -0,36 à -0,29 M€, RN ≈ 0**. L'équilibre n'est atteint qu'au niveau du résultat net, probablement grâce à des éléments non opérationnels (non vérifié).
- **Hameau de la Cense (799342704)**, société immobilière et d'hébergement (enseigne « Le Barn » citée au BODACC) : CA de 1,1 à 4,8 M€ (2018-2025), **résultat négatif 8 années sur 9**, dont **-4,06 M€ en 2023** [S12].
- **Leçon :** même avec une marque reconnue et un fondateur fortuné, **l'activité équestre seule ne dégage pas d'EBE positif**.

### Cas 14 — Hickstead (West Sussex) — **équestre** — **A partiel**
- Douglas Bunn, « ancien avocat devenu multimillionnaire grâce aux caravanes », achète Hickstead Place et ouvre en 1960 le premier terrain permanent de saut d'obstacles du pays : 6 carrières, plus de 5 000 places assises, 26 loges de réception [S47, PAGE LUE].
- **Hickstead Ltd, au 31/01/2026** [S32, OCR] : capitaux propres **£2,35 M**, immobilisations £3,97 M (dont ≈£1,20 M d'acquisitions dans l'année), 22 salariés. Le report à nouveau passe de -£331 805 à -£127 176, soit **+£205 k** (déduit du bilan, compte de résultat non déposé).
- **Leçon :** un **événementiel équestre de marque**, construit sur 60 ans, peut être bénéficiaire. Le report à nouveau encore négatif montre une histoire de pertes passées.

### Cas 15 — Badminton Horse Trials — **équestre** — **A partiel**
- **Badminton Horse Trials Ltd, au 30/09/2025** [S31, OCR] : trésorerie **£3,37 M**, report à nouveau **£2,92 M** contre £2,38 M un an plus tôt, soit **+£539 k** (déduit du bilan). 13 salariés.
- **Leçon :** un concours de très haut niveau, avec une marque mondiale, est rentable. Ce n'est pas transposable à un nouvel entrant.

### Cas 16 — Burghley (trust + Horse Trials) — **équestre** — **A**
- **Burghley House Preservation Trust (charity 258489)**, exercice clos fin janvier 2026 : revenus **£17,73 M**, dépenses £16,51 M, soit **un excédent de £1,22 M**. Les revenus financiers (**£5,35 M**) en représentent **30 %**, le commerce £10,11 M [S37, PAGE LUE].
- **Burghley Horse Trials Ltd** (exercice clos au 31/01/2024, comptes complets) : CA **£5 350 245** pour un « concours complet classé quatre étoiles ». Coût des ventes £3,81 M, frais administratifs £1,52 M, **bénéfice £22 500 (0,4 %)**, contre £447 557 l'année précédente (9,2 %). Capitaux propres **négatifs (-£226 k)**. Les bénéfices remontent au trust parent par Gift Aid [S30, OCR].
- **Leçon :** l'équilibre du domaine repose sur un **patrimoine financier**. Le concours équestre, pourtant mondialement connu, a une **marge très volatile**.

### Cas 17 — Blenheim et Chatsworth (repères d'échelle) — **A**
- **Blenheim Palace Heritage Foundation (1166164)**, exercice clos au 31/03/2025 : revenus **£30,96 M**, dépenses £27,79 M, soit **+£3,17 M**. Commerce £16,02 M. Les dons sont passés de £11,78 M (2021) à £3,06 M (2025) [S36, PAGE LUE].
- **Chatsworth House Trust (511149)**, exercice clos au 31/03/2025 : revenus **£19,35 M**, dépenses £17,39 M, soit **+£1,96 M**. Exercice 2021 (Covid) : £7,44 M de revenus pour £10,08 M de dépenses, soit **un déficit de £2,64 M** [S35, PAGE LUE].
- **Leçon :** à grande échelle, l'excédent représente environ 10 % des revenus, et une seule mauvaise année efface plusieurs années d'excédents.

### Cas 18 — Highclere Castle (« Downton Abbey ») — **C**
- Ouvert au public en 1988, environ 70 jours par an. Selon Lady Carnarvon, le tournage n'a « pas tant profité financièrement » au château. Le domaine est géré comme une entreprise [S68, S69, EXTRAITS]. Sociétés trouvées : Highclere Castle Horse Feeds Ltd, Highclere Castle Media Ltd, Trustee 1 et 2 Ltd (2025) [S72]. **Aucun compte d'exploitation du château trouvé.**

---

## 3. Contre-exemples (liquidations, ventes forcées, pertes)

### CE1 — Haras de Hus (Petit-Mars, Loire-Atlantique) — **élevage et sport équestre**
- Xavier Marie, fondateur de Maisons du Monde, crée le haras et le centre équestre en 2004-2005. Il investit des millions dans le cheptel, dont la jument Poetin achetée **900 000 €** en 2005, fourbue trois mois plus tard. Les succès sportifs sont réels (Silvana, or par équipes aux Jeux équestres mondiaux de 2010) [S49, PAGE LUE].
- Mise en vente en 2020 : 120 ha, le château de Pont-Hus, le centre équestre et les chevaux (prix confidentiel). En 2023, la propriété seule est proposée à **21,2 M€ honoraires inclus** [S49]. En 2024 : arrêt des activités, vente de tous les chevaux, de la semence et des embryons [S50, PAGE LUE]. Un communiqué Barnes d'octobre 2024 cite 128 ha à 12,9 M€ [S64, EXTRAIT, non vérifié].
- **Comptes (478488687)** [S08] :

| Exercice | CA | EBE | RN |
|---|---|---|---|
| 2015 | 0,79 M€ | -0,96 M€ | -1,71 M€ |
| 2019 | 0,57 M€ | -2,22 M€ | -2,11 M€ |
| 2021 | 1,30 M€ | -2,00 M€ | -2,38 M€ |
| 2023 | 2,08 M€ | -1,40 M€ | -3,17 M€ |
| 2024 | 1,77 M€ | -2,90 M€ | -2,94 M€ |

  **EBE négatif 10 années sur 10. Cumul 2015-2024 : EBE -15,8 M€, RN -16,0 M€** (ESTIMATION par somme). Capitaux propres négatifs depuis 2022. La fiche Xerfi donne les mêmes chiffres pour 2024 [S63, EXTRAIT].
- **Ce que ça contredit :** l'idée qu'un élevage ou une écurie de sport de haut niveau puisse financer un domaine. Même un fondateur fortuné y perd environ 1,6 M€ par an.

### CE2 — Château d'Ygrande (Allier) — **hôtel-château avec centre équestre**
- Hôtel-château 4 étoiles de **19 chambres** près de la forêt de Tronçais (classement Atout France du 27/06/2022 ; les « 5 chambres » de The Hotel Guru sont une erreur), avec restaurant gastronomique et **ses propres écuries** : cours, pension, séjours équestres, étang, piscine [S59 ; Cas_Ygrande, PAGE LUE].
- **Exploitant : SAS Groupe Cœur et Détente (421318247)**, hôtel-restaurant au lieu-dit le Mont, 20 à 49 salariés en 2024 selon l'INSEE (10 à 19 selon Société.com) [S25 ; Cas_Ygrande]. CA 1,02 M€ (2017), 1,10 M€ (2018), 1,13 M€ (2019). EBE +62 k€, +8 k€, **-101 k€**, subventions d'exploitation comprises : environ 38, 24 puis 3 k€ (calcul à partir des ratios ; sans elles, l'EBE 2017 n'aurait été que d'environ 24 k€). RN +38 k€, -12 k€, +23 k€, puis 2021 +47 k€ et 2022 **-102 k€**. **Taux d'endettement de 439 % à 1 482 %, autonomie financière de 3,6 % à 11 %** [S09]. Comptes confidentiels en 2016 et à partir de 2020, comptes 2024 non déposés [S14 ; Cas_Ygrande]. La dette financière ne tourne qu'autour de 0,2 M€ en 2017-2019 (calcul à partir des ratios) : ces taux élevés viennent surtout de fonds propres quasi nuls, devenus négatifs fin 2022.
- **Liquidation judiciaire le 28/10/2025**, avec cessation des paiements au 01/09/2025, au tribunal de commerce de Cusset [S14, S25]. Le lien avec l'enseigne est confirmé par France 3 (29/10/2025). L'article cite un « prêt à l'état » en 2020, très probablement un PGE (prêt bancaire garanti par l'État), un second prêt en 2024, deux procès perdus aux prud'hommes en appel et une dette d'environ 800 000 € [Cas_Ygrande, PAGE LUE]. Les murs et les 40 ha appartiennent au GFA Domaine du Mont, qui n'est pas liquidé ; le domaine est en vente à environ 2,5 M€ net vendeur en 2026.
- **Volet équestre :** l'EARL « Le Haras du Château d'Ygrande », devenue « Haras d'Ygrande » (447907064, gérée depuis 2013 par une associée distincte du dirigeant de l'hôtel), est mise en **liquidation judiciaire le 06/06/2024** (cessation des paiements au 06/12/2022). La procédure est **clôturée pour insuffisance d'actif le 02/04/2026**, avec radiation d'office [S15]. Une autre EARL, « Écuries du Château » (820732873), créée en 2016 à la même adresse pour des « activités équestres », est encore active, avec le même dirigeant que l'hôtel : le centre équestre continue après la liquidation de l'hôtel [S01, S15 ; Cas_Ygrande].
- **Ce que ça contredit :** l'idée qu'un **château-hôtel équestre** de petite taille s'autofinance. Il atteint environ 1 M€ de CA, mais avec un EBE quasi nul et des fonds propres quasi inexistants, ce qui mène à la liquidation des deux activités (hôtel et haras).

### CE3 — Château de Brindos (Anglet) — hôtel de luxe
- **SAS Château de Brindos (431703610)** : CA 2,00 M€, 2,10 M€ et 1,81 M€ (exercices clos fin septembre 2016 à 2018). **RN -591 k€, -618 k€ et -869 k€**. Capitaux propres négatifs [S10].
- Procédure de sauvegarde le 24/04/2017, convertie en redressement judiciaire le 22/10/2018, puis **liquidation judiciaire le 14/10/2019**. Le fonds est revendu **200 000 €** (2021-2022, acquéreurs « C Le Lac » puis « BMF Brindos Anglet ») [S16].
- Réouverture le 15/04/2022 en hôtel 5* Relais & Châteaux par le groupe Millésime [S61, PAGE LUE]. Selon des sources non lues, Serge Blanco était propriétaire depuis 2000 [S65, EXTRAIT], et BMF Hospitality reprend la gestion directe en 2026 [S71, EXTRAIT].
- **Ce que ça contredit :** l'idée qu'un nom et un site d'exception suffisent. Le domaine perdait 30 à 48 % de son CA chaque année.

### CE4 — Le Château de Bricquebec (Manche) — hôtel-restaurant
- Société créée fin 2016. Elle achète le fonds de l'hôtel-restaurant **395 000 €** en 2017. Elle cède un fonds à CSPINS pour **200 000 €** en 2021. Redressement judiciaire le 08/11/2021 (cessation des paiements au 15/06/2020), **liquidation le 10/01/2022**, clôture pour **insuffisance d'actif** le 09/09/2024 [S17].
- **Ce que ça contredit :** la valeur d'un fonds hôtelier de château n'est pas stable. Elle a été divisée par deux en 4 ans, avant une liquidation sans actif.

### CE5 — Château de Charfetain (Brullioles, Rhône) — gîtes et réceptions
- Société créée en 2019 pour l'hébergement touristique, la location de salles de réception et de gîtes, et l'organisation d'événements [S18]. Cessation des paiements le 10/01/2024, **liquidation judiciaire le 10/07/2025**, clôture **pour extinction du passif** le 29/09/2026 : les créanciers ont été payés, vraisemblablement par la réalisation d'actifs (non vérifié) [S18]. Le lieu est affiché sur une plateforme de mariage (160 places assises, à partir de 3 860 €) [S70, EXTRAIT].
- **Ce que ça contredit :** le modèle « mariages + gîtes » n'est pas sûr par nature. Cette affaire a cessé ses paiements moins de 5 ans après sa création.

### CE6 — Château de Bernesq
- Société créée en 2021, **liquidation judiciaire simplifiée le 07/05/2026** (cessation des paiements au 17/10/2025) [S19]. L'activité exacte est INCONNUE. C'est un simple point de données.

### CE7 — Ballyfin Demesne (Co. Laois, Irlande)
- Domaine acheté en 2002 par Fred et Kay Krehbiel (américains), aujourd'hui détenu par leurs fils. Plus de 600 acres [S51, PAGE LUE].
- Comptes 2025 cités par l'Irish Times : CA **8,1 M€** (+24 %), dont hébergement ≈5 M€, restauration 2,3 M€ et activités de plein air 0,77 M€. **Bénéfice 32 078 €** contre une perte de 389 281 € en 2024. 106 salariés, masse salariale 3,6 M€, taux d'occupation 60 %. **Pertes cumulées : 37,6 M€** [S51]. Selon la presse, le domaine avait déjà été bénéficiaire en 2021 (786 923 € avant impôts) [S66, EXTRAIT], puis la perte de 2024 est confirmée [S67, EXTRAIT] : un profil en dents de scie.
- **Ce que ça contredit :** l'idée que le luxe garantisse la rentabilité. Plus de 20 ans après l'achat, le domaine reste en pertes cumulées.

### CE8 — Adare Manor (Co. Limerick, Irlande)
- J.P. McManus l'achète **environ 30 M€** en 2014 et y dépense **environ 50 M€** [S53, PAGE LUE]. L'exploitant, Tizzard Holdings UC, a un statut « unlimited » et ne dépose donc pas ses comptes. Les rapports d'audit confirment des **pertes en 2018, 2023, 2024 et 2025** [S53, S54]. Les chambres sont vendues à partir de 750 € la nuit [S53].
- **Ce que ça contredit :** même avec un prix de vente très élevé et la Ryder Cup 2027, l'exploitation est déficitaire. Il s'agit de mécénat ou de prestige, pas d'un modèle autofinancé.

### CE9 — Bolesworth Events Ltd (château de Bolesworth, Cheshire) — **concours équestre**
- Bolesworth Castle appartient à la famille Barbour depuis 1856 : un domaine de 6 000 acres qui accueille le Bolesworth International Horse Show [S48, PAGE LUE].
- **Bolesworth Events Ltd** (2020), au 31/03/2025 : **capitaux propres -£4,50 M** contre -£3,95 M un an plus tôt, soit une perte d'environ £551 k (déduite du bilan). Dettes à plus d'un an : £4,36 M. La continuité d'exploitation repose sur le « soutien des sociétés liées » [S33, OCR].
- **Ce que ça contredit :** un grand concours hippique international dans un château peut **perdre de l'argent durablement**, avec le domaine comme filet de sécurité.

### CE10 — Gwrych avant 2018 : échecs d'acquéreurs privés
- 1989 : rachat par un homme d'affaires américain pour **£750 000**, avec un projet de centre d'opéra jamais réalisé. Le château est pillé. 2007 : Clayton Hotels l'achète **£850 000** après un échec aux enchères (réserve de £1,5 M), annonce un hôtel de 90 chambres pour **£6 M**, dépense environ **£500 000**, puis **est placé sous administration judiciaire**. Un nouveau permis obtenu en 2012 reste sans suite [S43, PAGE LUE].
- **Ce que ça contredit :** un prix d'achat bas ne protège de rien si le projet suppose un financement lourd qui n'arrive jamais.

---

## 4. Synthèse

### 4.1 Facteurs de succès communs (cas A et B solides)
1. **Prix d'entrée très bas par rapport à la taille du bien** : Saint-Fargeau ≈280 k€ (1979), Motte-Husson £280 k (2015), Mothe-Chandeniers 500 k€. Les travaux sont faits par tranches, financés au fil des recettes, avec beaucoup de travail personnel non rémunéré (Strawbridge, Bourneau, Fabiargues) ou bénévole (650 bénévoles à Guédelon, chantiers bénévoles à Mothe-Chandeniers).
2. **Un moteur d'audience** qui sert à la fois de recette et de marketing : la télévision (Channel 4 pour Strawbridge, ITV pour Gwrych, la BBC pour Guédelon), un spectacle (le son et lumière à 60 cavaliers de Saint-Fargeau) ou un événement de marque (Hickstead, Badminton, Burghley).
3. **Des capitaux non commerciaux** : subventions patrimoniales (NHMF pour Gwrych, collectivités pour Saint-Fargeau, Région pour Chantilly), mécénat (Aga Khan), financement participatif (≈2,1 M€ à Mothe-Chandeniers), dotations financières (30 % des revenus de Burghley), prêt d'honneur (20 k€ à Fabiargues).
4. **Des structures séparées** : société civile propriétaire des murs et société d'exploitation (Vaux, Mercuès, La Cense), trust caritatif au Royaume-Uni, société média distincte (Strawbridge).
5. **Des recettes diversifiées et à faible coût fixe** : visites et événements plutôt qu'un hôtel lourd. Les seuls excédents réguliers vérifiés en France viennent de **la visite** (Guédelon) et de **l'événementiel et du média** (Strawbridge), pas de l'hôtellerie.
6. **Un horizon de 10 à 30 ans** : Castle Leslie a mis plus de 25 ans pour atteindre 10 M€, Hickstead affiche encore un report à nouveau négatif après 60 ans, Saint-Fargeau tient depuis 45 ans.
7. **Le cheval comme atout de l'offre, pas comme centre de profit** : à Castle Leslie, le centre équestre attire la clientèle de l'hôtel. Dans les cas rentables, les chevaux font partie du spectacle (Saint-Fargeau, Chantilly) ou de l'événement de marque (Badminton, Hickstead). Ils ne sont jamais un élevage ou une écurie autonome.

### 4.2 Ordres de grandeur (vérifiés sauf mention)
| Indicateur | Valeur | Source / statut |
|---|---|---|
| Château d'attraction (300 k visiteurs) | CA ≈ 6 M€, marge nette de 5 à 15 % | Guédelon [S02], PAGE LUE |
| Hôtel-château de 30 chambres | CA ≈ 2 M€, RN ≈ 0 (de -0,13 à +0,33 M€) | Mercuès [S05], PAGE LUE |
| Petit hôtel-château équestre | CA ≈ 1,1 M€, EBE de -0,1 à +0,06 M€, fonds propres ≤ 11 % du bilan → liquidation | Ygrande [S09], PAGE LUE |
| Hôtel-château de luxe en difficulté | CA ≈ 2 M€, pertes de 0,6 à 0,9 M€ par an | Brindos [S10], PAGE LUE |
| Élevage et écurie de sport haut de gamme | EBE de -0,6 à -2,9 M€ par an | Haras de Hus [S08], PAGE LUE |
| Centre d'équitation éthologique de renom | CA ≈ 1,1 M€, EBE ≈ -0,3 M€ | La Cense [S11], PAGE LUE |
| Concours complet 4-5* | CA ≈ £5,4 M, marge de 0,4 à 9 % | Burghley HT [S30], PAGE LUE (OCR) |
| Grand domaine caritatif britannique | revenus de £17 à 31 M, excédent ≈ 7-10 % | [S35-S37], PAGE LUE |
| Domaine de luxe reconstruit (Irlande) | CA 8 M€, pertes cumulées 37,6 M€ | Ballyfin [S51], PAGE LUE |
| Valeur d'un fonds d'hôtel-château en difficulté | 200 à 395 k€ | Bricquebec, Brindos [S16, S17], PAGE LUE |
| Prix d'achat des cas « non fortunés » | 280 à 500 k€, hors travaux | [S39, S41, S42], PAGE LUE |
| Travaux de première urgence | 850 k€ (phase 1 de Mothe-Chandeniers) | [S39], PAGE LUE |

### 4.3 Ce que les contre-exemples contredisent
- **« Il suffit d'avoir de l'argent »** : faux. Adare (30 M€ + 50 M€, en pertes), Ballyfin (-37,6 M€ cumulés), Haras de Hus (-16 M€ en 10 ans) et Fontenille (33 M€ de CA, résultat négatif) montrent qu'un capital abondant ne crée pas de rentabilité. Il permet seulement d'**absorber** les pertes.
- **« Les chevaux paieront le château »** : faux dans tous les cas vérifiés. Hus, La Cense, le haras d'Ygrande (liquidé sans actif) et Bolesworth Events (-£4,5 M de capitaux propres) sont en pertes. Seuls des événements anciens et de marque mondiale (Badminton, Hickstead) dégagent des excédents.
- **« L'hôtel dans le château s'autofinance »** : faux en petite taille. Ygrande, Brindos et Bricquebec ont été liquidés, Mercuès est à l'équilibre au mieux. L'hôtellerie de château cumule des coûts fixes élevés, une forte saisonnalité et des dettes.
- **« Mariages et gîtes, c'est sans risque »** : Charfetain a cessé ses paiements moins de 5 ans après sa création.
- **« Un prix d'achat bas protège »** : à Gwrych, deux acheteurs privés à £750-850 k ont échoué. Le prix bas n'est qu'une condition nécessaire.
- **« Le financement participatif règle le problème »** : à Mothe-Chandeniers, la foule a financé l'achat et la sécurisation, mais les comptes sont confidentiels, des actionnaires contestent la gestion et le chantier est prévu sur 7 ans.
- **« La télévision fait la fortune »** : à Highclere, la propriétaire dit le contraire (EXTRAIT). Le cas Strawbridge reste une exception qui n'est pas reproductible à volonté.

### 4.4 Implications pour le projet (entrepreneur de 26 ans, apport limité, chevaux)
1. **Les seuls précédents vérifiés d'acquéreurs non fortunés** ont acheté entre 280 et 500 k€ de petits domaines (5 à 16 ha) ou des ruines. Le critère « plus de 50 ha » a été atteint par des trusts subventionnés (Gwrych, ≈80 ha) ou par héritage (Castle Leslie, Burghley), **jamais de façon documentée par un entrepreneur seul et sans capital** dans l'échantillon (la surface de Saint-Fargeau est INCONNUE).
2. **Le cheval doit être une composante de l'offre** (randonnées, pension, cours vendus avec l'hébergement ou les événements), pas une activité d'élevage ou de sport haut de gamme. Les comptes de Hus, de La Cense et d'Ygrande le démontrent.
3. **Il faut éviter un hôtel endetté**. Les profils qui survivent ont peu de dettes, une SARL ou SAS d'exploitation séparée, et beaucoup de travail personnel non payé.
4. **Il faut prévoir un « moteur d'audience »** (contenu vidéo, événement de marque) et des **capitaux non bancaires** (prêt d'honneur, Fondation du patrimoine, financement participatif, association, subventions).
5. **L'horizon réaliste est de 10 à 25 ans** pour un domaine autofinancé. L'échéance 2030-2031 est compatible avec **la possession ou le contrôle** d'un domaine, beaucoup moins avec un **excédent démontré**.

---

## 5. Pistes non abouties
- **Domaine d'Ablon (Calvados)** : SAS Le Domaine d'Ablon (882523186, créée en 2020, RN 2020 : -64 k€) et « The Riding Stable Corp » (911034197, créée en 2022, enseignement de l'équitation) [S01, S73]. Aucun compte récent public, concept non vérifié. **C.**
- **Château de Gudanes (Ariège)** : une société « CHATEAU DE GUDANES » (hébergement touristique) a été créée le 22/05/2026 [S01]. Histoire de l'acquéreur non vérifiée.
- **Castle Leslie, Ballyfin, Adare** : le registre irlandais (CRO) est bloqué (403). La méthode serait d'acheter les documents déposés sur core.cro.ie (≈ quelques euros par document).
- **Chatsworth, Burghley et Blenheim (comptes de groupe détaillés)** : les PDF sont scannés (plus de 60 pages). Seuls les résumés de la Charity Commission ont été exploités.
- **Fondation de Chantilly** : comptes à chercher au Journal officiel des associations et fondations (non consulté).
- **Entités sans données dans le jeu INPI** (confidentialité ou absence de dépôt) : Mothe-Chandeniers, Dartagnans, The Riding Stable Corp, EARL Écuries du Château [S75].

## 6. Points de doute / hypothèses non vérifiées
1. **Strawbridge.** Le résultat 2022 de DA2AD (+811 k€) provient du jeu INPI (résultat publié au bilan, compte de résultat confidentiel). Seul le chiffre 2023 (5 632 €) a été recoupé sur societe.com. La part qui vient de la télévision ou de l'activité château est INCONNUE.
2. **Bourneau.** Le lien entre la SARL Bourneau Événements et le couple Fois est déduit de l'adresse (« rue du Château ») et de l'activité, sans document nominatif. Le prix d'achat est INCONNU.
3. **Ygrande** (mis à jour le 14/10/2026 après l'étude de cas). Le lien entre Groupe Cœur et Détente et l'enseigne « Château d'Ygrande » est confirmé par France 3 (29/10/2025, PAGE LUE). L'hôtel compte 19 chambres (classement Atout France). Le château a été acheté en 1998 par le couple fondateur, à un prix INCONNU. Étude complète : `Cas_Ygrande/Topo_Ygrande.md`.
4. **Résultats britanniques déduits du bilan** (Hickstead, Badminton, Bolesworth, Chateau Television) : ils supposent qu'aucun autre mouvement de capitaux propres n'a eu lieu. Ce sont des minorants du bénéfice si des dividendes ont été versés. L'OCR peut contenir des erreurs : les montants ont été relus sur des lignes cohérentes (totaux égaux).
5. **Haras de Hus.** Les résultats positifs de 2016 (+1,47 M€) et 2020 (+0,26 M€), alors que l'EBE est négatif, viennent probablement d'éléments exceptionnels (ventes de chevaux, abandons de créances). Hypothèse non vérifiée. Le prix et le périmètre de vente varient selon les sources (21,2 M€ pour 120 ha en 2023 ; 12,9 M€ pour 128 ha selon un EXTRAIT de 2024). **Aucune annonce n'a été ouverte**, je n'affirme donc pas que le bien est encore en vente.
6. **Chantilly.** Les chiffres de 3,5 M€ de CA et de 1,4-1,5 M€ de résultat viennent de Wikipédia, ne sont pas datés et n'ont pas été recoupés par des comptes.
7. **Castle Leslie.** Le CA de ≈10 M€ et la « rentabilité » proviennent d'un article de 2019 republié par le domaine lui-même. Pas de comptes consultés.
8. **Vaux-le-Vicomte.** Les deux sociétés trouvées ne couvrent qu'une partie du budget de 8 M€ (Wikipédia). D'autres entités du domaine (SCI Valterre, etc.) n'ont pas été consultées.
9. **Brindos.** La propriété de Serge Blanco (2000-2019) et le rachat par Millésime ou BMF en 2020 reposent sur des EXTRAITS (Slate et Tendance Hôtellerie non lisibles directement).
10. **Charfetain.** La « clôture pour extinction du passif » suggère que l'actif a couvert les dettes. La cause (vente du bien ou autre) n'est pas vérifiée. Le prix « à partir de 3 860 € » est un EXTRAIT.
11. **Couverture régionale française des jeunes couples.** La presse régionale est en grande partie payante (Ouest-France, Objectif Gard). Seuls deux cas (Bourneau, Fabiargues) ont été trouvés avec des pages lisibles, et aucun ne combine château, chevaux et comptes publics.
12. **Biais de survie.** Les cas « réussis » sont visibles parce qu'ils sont médiatisés. Les échecs de petits porteurs en entreprise individuelle n'apparaissent pas au BODACC sous un nom contenant « château ». Le taux d'échec réel est donc probablement **sous-estimé** dans cet échantillon.
