# R7 — Marchés de l'événementiel, de l'hébergement, des tournages et des visites

Agent : R7. Date de consultation des sources : 2026-10-14. Rédaction terminée le 2026-10-14.

Budget web consommé : **16 WebSearch**, soit **un dépassement d'une unité** du plafond de 15. Il vient d'une erreur de décompte de ma part : la 16e recherche portait sur les visites de châteaux privés et n'a produit que des EXTRAITS de faible portée.

S'y ajoutent environ 100 WebFetch, dont une vingtaine en échec (erreurs 403, 404, 503, 522). Ces appels incluent des API publiques officielles (BODACC open data, recherche-entreprises.api.gouv.fr) et des PDF extraits localement avec `pdftotext`.

**Résumé en 8 points** (détails et sources dans le corps du texte) :
1. Environ 251 000 mariages en 2025 (INSEE), dont 59 % de juin à septembre et 82 % le samedi. Budget moyen de 19 293 € (Mariages.net) ; 12 % des réceptions en château dans ce panel.
2. Forte concurrence : 1 382 châteaux et 3 769 domaines sur Mariages.net. Les monuments publics du CMN louent un week-end de mariage autour de 3 750 € HT.
3. La location d'un château pour un mariage, sans traiteur, se situe autour de 4 000 à 10 000 € (HT/TTC rarement précisé). Les sociétés d'exploitation font 60 000 à 600 000 € de chiffre d'affaires, avec une marge nette de 0 à 6 %.
4. Séminaires en château : 95 à 100 € HT par personne pour une journée d'étude, 160 à 275 € HT par personne et par jour en résidentiel. Le leader, Châteauform' France, fait 186 M€ de chiffre d'affaires avec une marge nette de 1,8 %.
5. Tournages : grille officielle du CMN de 2 500 à 9 000 € HT par jour pour la fiction selon la catégorie. Fréquence inconnue, donc revenu occasionnel.
6. Châteaux-hôtels : RevPAR haut de gamme de 100 à 180 € HT dans les départements de châteaux (2025) ; investissement de 350 000 à 700 000 € par chambre ; environ 1,65 salarié par chambre ; échecs nombreux (BODACC).
7. Gîtes : environ 45 % d'occupation par an. Location de luxe d'un château de 16 chambres : environ 56 000 à 62 000 € par semaine. Glamping : environ 22 000 € par module et par an.
8. Visites : 15 à 20 € par adulte dans les grands sites, mais environ 6 000 visiteurs en moyenne par monument privé ouvert. Les visites ne financent pas un domaine.

Statuts utilisés : PAGE LUE (page ouverte avec WebFetch, citation exacte), EXTRAIT (vu seulement dans un résultat de recherche), ESTIMATION (raisonnement explicite), HYPOTHÈSE (choix de modélisation), INCONNU.

Sources : `01_RECHERCHE/sources/sources_R7.csv` (identifiants R7-xx).

---

## 1. Mariages

### 1.1 Volume annuel (INSEE)

| Année | Mariages (France, tous couples) | Écart vs 2019 (ESTIMATION, calcul) | Statut | Source |
|---|---|---|---|---|
| 2019 | 224 740 | réf. | PAGE LUE | [R7-01] |
| 2020 | 154 581 | −31,2 % | PAGE LUE | [R7-01] |
| 2021 | 218 819 | −2,6 % | PAGE LUE | [R7-01] |
| 2022 | 241 710 | +7,6 % | PAGE LUE | [R7-01] |
| 2023 | 241 080 | +7,3 % | PAGE LUE | [R7-01] |
| 2024 | 248 174 | +10,4 % | PAGE LUE | [R7-01] |
| 2025 (provisoire) | 251 000 | +11,7 % | PAGE LUE | [R7-01] |

- Citation [R7-01] : « en 2025, 244 000 mariages ont été célébrés entre personnes de sexe différent et 7 000 entre personnes de même sexe. »
- Citation [R7-02] (Bilan démographique 2024) : le texte évoque « un recul historique des mariages en 2020 », puis des rebonds en 2021 et 2022, puis « une stabilisation en 2023 ». Il chiffre la hausse de 2024 à « +2 % » sur un an et note que 2024 dépasse de « 10 % » le niveau de 2019.
- Divergence à conserver : le Bilan 2024 [R7-02] donnait 247 000 mariages en 2024 (provisoire). La série révisée [R7-01] donne 248 174.
- Les pacs (≈ 197 000 en 2024 [R7-01]) ne génèrent pas, sauf exception, de réception en château. Ils sont exclus du marché adressable. C'est une HYPOTHÈSE.

### 1.2 Budget moyen, invités, type de lieu (Mariages.net, rapport 2026)

Source : Mariages.net, « Rapport sur le Secteur Nuptial 2026 » (3e édition, mise à jour le 11 mars 2026) [R7-03]. Méthode : « plus de 1 304 couples » mariés entre le 1er janvier et le 31 décembre 2025. **Biais** : ce sont des utilisateurs de la plateforme, donc plutôt des couples qui organisent une vraie réception. L'échantillon n'est pas représentatif des 251 000 mariages INSEE.

| Donnée | Valeur | Statut | Source |
|---|---|---|---|
| Budget moyen d'un mariage, hors bague et voyage de noces | 19 293 € (TTC implicite : dépense des ménages) | PAGE LUE | [R7-03] « Le coût moyen d'un mariage en France est de 19 293 euros » |
| Évolution du budget | −3 % par rapport à 2024 | PAGE LUE | [R7-03] |
| Coût par invité | 215 € | PAGE LUE | [R7-03] « un coût moyen de 215 euros par invité » |
| Invités en moyenne | 90 en 2025 (97 en 2024) | PAGE LUE | [R7-03] |
| Couples dépensant au moins 20 000 € / plus de 25 000 € | plus de 40 % / 25 % | PAGE LUE | [R7-03] |
| **Lieu de réception : domaine / salle de mariage / château** | **37 % / 26 % / 12 %** | PAGE LUE | [R7-03] |
| Même lieu pour la cérémonie et la réception | 44 % | PAGE LUE | [R7-03] |
| Durée moyenne de préparation | 15 mois (le plus souvent 12 à 18 mois) | PAGE LUE | [R7-03] |
| Région la plus chère | Nouvelle-Aquitaine, 21 641 € ; Île-de-France 20 794 € ; PACA 20 333 € | PAGE LUE | [R7-03] |

Autres budgets, à ne pas confondre :
- Étude Hyatt « Vows & Venues » : budget **rêvé** de 33 465 €. L'article précise qu'il « ne correspond pas au coût moyen réellement payé par les couples ». PAGE LUE [R7-04].
- Sofinco : « 7.781 euros pour 52 invités, soit 150 euros par personne ». PAGE LUE [R7-04].
- Ces écarts, de 7 800 à 19 300 € selon les études, reflètent des échantillons différents. Mariages.net surreprésente les mariages avec réception.

**ESTIMATION du nombre de réceptions en château** :
- Calcul : 12 % × 251 000 mariages = **≈ 30 000 par an**. Avec la catégorie « domaine », on obtient 37 % × 251 000 ≈ 93 000.
- Ce calcul suppose que la répartition des répondants de Mariages.net s'applique à tous les mariages. C'est une **borne haute** : une partie des mariages n'a pas de réception de ce type.

### 1.3 Concurrence : nombre de lieux référencés

| Plateforme / catégorie | Compteur affiché (14/10/2026) | Statut | Source |
|---|---|---|---|
| Mariages.net, « Château mariage » | « 1.382 résultats ». La FAQ de la même page dit « plus de 1100 » | PAGE LUE | [R7-05] |
| Mariages.net, « Domaine mariage » | « 3.769 résultats » | PAGE LUE | [R7-06] |

- **ESTIMATION de densité** :
  - ≈ 30 000 réceptions en château par an ÷ 1 382 châteaux référencés ≈ **22 mariages par château et par an** en moyenne.
  - ≈ 93 000 ÷ 3 769 domaines ≈ 25 par domaine.
  - Ce sont des ordres de grandeur. Des lieux ne sont pas référencés sur la plateforme, les catégories se recouvrent et la répartition par type de lieu est biaisée.
- **Lecture** : la saison concentre la demande sur les samedis de mai à septembre (voir 1.5), soit environ 20 à 22 samedis.
  - Ce nombre est une ESTIMATION calendaire : mai à septembre compte environ 22 samedis.
  - Une moyenne d'environ 22 mariages par lieu indique un marché **mature et concurrentiel**. Un nouveau château ne prend des dates qu'en les retirant à d'autres, sauf à se différencier par la gamme, la capacité d'hébergement ou la localisation.
- Les prix « À partir de » affichés sur Mariages.net pour les premiers châteaux de la liste vont de 1 200 € à 5 882 € [R7-05], et pour les domaines de 800 € à 8 000 € [R7-06].
  - Exemples : Château des Bordes (Nièvre) « À partir de 1.200€ » ; Château La Beaume (Dordogne) « À partir de 5.500€ » ; Château de la Noé Sèche (Côtes-d'Armor) « À partir de 5.882€ ».
  - La page ne dit pas ce que couvre le prix, ni s'il est HT ou TTC. Statut : PAGE LUE.

### 1.4 Tarifs observés de location pour un mariage

| Lieu | Formule | Prix | HT/TTC | Statut | Source |
|---|---|---|---|---|---|
| Château de Picomtal, monument historique inscrit, petit château | « Mariage classique » : du samedi après-midi au dimanche 14 h ; 60 personnes au dîner ; nuitée pour 25 personnes au plus (9 chambres) | 5 600 € (25 pers.) ; 6 100 € (45 pers.) ; 6 700 € (45 à 60 pers.) | non précisé | PAGE LUE (PDF) | [R7-07] |
| Château de Picomtal | Mariage avec cérémonie laïque, sur 3 jours | 7 100 € à 8 400 € | non précisé | PAGE LUE (PDF) | [R7-07] |
| Château de Picomtal | Privatisation en soirée sans hébergement | 3 900 € à 5 100 € | non précisé | PAGE LUE (PDF) | [R7-07] |
| Château de Picomtal | Privatisation en journée | 1 200 € à 2 500 € | non précisé | PAGE LUE (PDF) | [R7-07] |
| Château de Picomtal | Séance photo en intérieur | 150 € pour 1 h 30 | non précisé | PAGE LUE (PDF) | [R7-07] |
| Château de Berne (Var), hôtel 5 étoiles | « Wedding package » : 10 chambres, 2 nuits au minimum, traiteur libre | « from €19,500 including VAT » | TTC | PAGE LUE | [R7-08] |
| Château de Berne | Privatisation du domaine : 34 chambres, 2 nuits au minimum, 120 invités, traiteur du domaine avec un minimum de 36 000 € TTC | « from €95,500 including VAT » | TTC | PAGE LUE | [R7-08] |
| Château des Pères (Ille-et-Vilaine), via Bridebook | Forfait « Usage exclusif », 1 à 3 jours, jusqu'à 350 invités, hébergement non inclus | 4 000 à 9 500 € | non précisé | PAGE LUE | [R7-09] |
| Fourchette générique « Château / Manoir », location seule | — | « 4 000 € – 10 000 €+ » ; le lieu pèse « entre 5 500 € et 6 500 € » dans le budget moyen (d'après Mariee.fr) | non précisé | PAGE LUE (blog commercial, fiabilité faible) | [R7-10] |

Remarques :
- Picomtal : ces tarifs sont « valables jusqu'à fin 2027 ». La brochure prévoit « -10% sur le tarif pour les mariages en mai et en octobre ». Les prestataires ne sont pas inclus : « Traiteur (+ staff de service), musique, fleuriste, et photographe ne sont pas inclus ni imposés ». Le règlement de la maison rappelle que « Le château est un monument historique inscrit ».
- Château de Berne : la FAQ précise que ces prix sont « valid for April 2024 ». Ce chiffre de 2024 est donc présenté sur une page de 2026.
- La page bordelaise de 1001 Salles, qui annonçait un week-end privatisé à 25 000-45 000 € avec hébergement et restauration (EXTRAIT de la recherche) [R7-11], n'a pas pu être ouverte (erreur 522). Ce chiffre reste un EXTRAIT, de fiabilité faible.

**Lecture pour le modèle** : on distingue trois gammes. Ce classement est une ESTIMATION fondée sur les exemples ci-dessus.
1. **Location « nue » d'un château**, sans traiteur, avec peu ou pas de chambres : environ 4 000 à 10 000 € le week-end.
2. **Location avec 10 à 25 couchages sur 2 nuits** : environ 6 000 à 20 000 €.
3. **Privatisation hôtelière complète**, de 30 chambres ou plus, avec traiteur imposé : souvent plus de 50 000 €. Exemple : Berne, 95 500 € TTC hors minimum traiteur.

La TVA n'est pas précisée dans la plupart des grilles. Le caractère HT ou TTC n'est clair que pour Berne.

### 1.4 bis Référence publique : tarifs de privatisation des châteaux du Centre des monuments nationaux (CMN)

Source : CMN, « Grilles tarifaires privatisation » (PDF créé en novembre 2025) [R7-13]. Ce sont des **prix planchers HT et TTC**. Le PDF précise : « Tous les tarifs donnés sont des prix planchers et sont susceptibles d'évoluer selon la nature des évènements. »

Ces tarifs publics, bas, fixent un **plafond de prix** pour un château privé de gamme moyenne situé à proximité d'un monument du CMN qui accepte les mariages.

| Monument du CMN | Espace et durée | HT (à partir de) | TTC (à partir de) | Statut |
|---|---|---|---|---|
| Château de La Motte Tilly (parc de 60 ha) | « Mariage » : Orangerie, terrasse et verger, samedi | 2 425 € | 2 910 € | PAGE LUE (PDF) [R7-13] |
| Château de La Motte Tilly | Mariage, samedi et veille pour l'installation | 2 600 € | 3 120 € | PAGE LUE (PDF) [R7-13] |
| Château de La Motte Tilly | Mariage, « Week-end : 3 jours » | 3 750 € | 4 500 € | PAGE LUE (PDF) [R7-13] |
| Château de Haroué (mariages acceptés) | Vestibule, grand salon et salon Alexandre, 18 h à 4 h | 4 175 € | 5 010 € | PAGE LUE (PDF) [R7-13] |
| Château de Pierrefonds (mariages acceptés) | Salle des gardes, cour d'honneur et cuisines, 18 h à 7 h | 4 350 € | 5 220 € | PAGE LUE (PDF) [R7-13] |
| Château de Bouges (parc de 80 ha) | Orangerie de 224 places assises, « Week-end » : samedi 18 h à 6 h et dimanche 10 h à 17 h | 3 000 € | 3 600 € | PAGE LUE (PDF) [R7-13] |
| Château de Champs-sur-Marne | Salons du château, 4 heures, 18 h à 2 h | 4 400 € | 5 280 € | PAGE LUE (PDF) [R7-13] |
| Château de Maisons | Du vestibule d'honneur à la salle de bal, 18 h à 1 h, événement d'entreprise | 8 000 € | 9 600 € | PAGE LUE (PDF) [R7-13] |
| Château de Chareil-Cintrat (mariages acceptés) | Salle polyvalente, 3 h | 1 250 € | 1 500 € | PAGE LUE (PDF) [R7-13] |

Autres éléments de la grille :
- Le forfait inclut des agents de surveillance, le nettoyage et parfois le chauffage.
- Visite privée : 550 € HT pour 1 à 30 personnes, à Champs-sur-Marne et à Azay-le-Rideau.

**Lecture** :
- Un monument public prestigieux loue un week-end de mariage autour de 3 000 à 5 000 € HT pour l'espace seul, sans hébergement.
- Un château privé ne peut donc pas facturer beaucoup plus cher la seule location d'espaces. La valeur se construit sur :
  - l'**hébergement sur place** ;
  - l'**exclusivité du domaine** ;
  - le **service**.
- Cette lecture est une ESTIMATION.

### 1.5 Saisonnalité des mariages (INSEE)

Source : Insee Focus n° 225, « Se marier en été est une habitude récente : 150 ans de saisonnalité des mariages », 11/02/2021 [R7-15].

| Donnée (année 2019) | Valeur | Statut | Source |
|---|---|---|---|
| Mariages de juin à septembre | « 132 200 mariages ont été célébrés, soit 59 % du total de l'année » | PAGE LUE | [R7-15] |
| Juin | « 42 100 mariages » | PAGE LUE | [R7-15] |
| Juillet, août | plus de 30 000 chacun : « Plus de 30 000 couples se sont dit “oui” en juillet et autant en août. » | PAGE LUE | [R7-15] |
| Janvier, février | 5 900 et 6 900 ; le premier trimestre regroupe 10 % des mariages | PAGE LUE | [R7-15] |
| Part des mariages un samedi | « 82 % en 2019 » ; maximum en 2007 (85 %) ; 78 % en 2020 | PAGE LUE | [R7-15], [R7-16] |
| Jour le plus choisi | 8 juin 2019, 8 800 mariages | PAGE LUE | [R7-15] |

Autres sources :
- 1001 Salles : dates prisées « entre mai et septembre », réservation « 12 à 18 mois à l'avance » [R7-10].
- Picomtal applique −10 % en mai et en octobre [R7-07]. Ce rabais signale la moindre valeur des ailes de saison.

**Conséquence pour la capacité, en ESTIMATION** :
- Un lieu qui ne fait qu'un mariage par week-end est limité à environ **17 samedis de haute saison** (juin à septembre).
- Il atteint au plus environ **22 samedis** de mai à septembre, et environ **26 à 30** en comptant les ailes de saison, avril et octobre, à prix réduit.
- Au-delà, il faut des mariages en semaine, rares, ou d'autres événements.
- Un château qui vise 20 à 25 mariages par an doit donc capter **la quasi-totalité des samedis d'été**. C'est un objectif ambitieux face à environ 1 400 châteaux et 3 800 domaines référencés (§1.3).
- Il en résulte un conflit direct avec les week-ends équestres, comme les concours et les cavaliers propriétaires présents le samedi. Voir le Contexte permanent, leçon n° 4.

### 1.6 Mariages de destination (étrangers qui se marient en France)

- **INCONNU** : je n'ai trouvé **aucune statistique publique** sur le nombre de mariages d'étrangers célébrés en France ni sur leur budget.
  - Atout France n'a pas d'étude chiffrée en ligne (recherche interne sur atout-france.fr [R7-17]).
  - Atout France fait en revanche de la **promotion de ce segment** :
    - Salon EPEX 2025 consacré au tourisme d'affaires et au « segment de mariage “destination weddings” », participation à « 7200€ HT » [R7-18] ;
    - opération « Wedding Planner Event avec Business France » du 28/06/2027 au 02/07/2027, avec pour objectif de « Renforcer l'attrait de la France en tant que destination idéale pour les mariages indiens » [R7-19].
  - Statut : PAGE LUE.
- Étude Hyatt « Vows & Venues », citée par la presse : la France est « citée par 79% des répondants comme destination de rêve ».
  - Ni l'échantillon, ni la méthode, ni la nationalité des répondants ne sont précisés. C'est donc un indicateur d'image, pas une mesure de marché. Statut : PAGE LUE [R7-04].
- Méthode pour vérifier :
  - demander à Atout France (service Études et publications, marché Inde) ;
  - consulter les rapports annuels de plateformes internationales (Zankyou, The Knot Destination Wedding Study) ;
  - interroger des agences de wedding planners haut de gamme (Provence, Bordelais, Loire), ce qui sort du périmètre de cet agent car aucun contact n'est autorisé.
- **Lecture qualitative** : c'est un segment haut de gamme (anglo-saxons, Inde, Moyen-Orient), concentré sur la Provence, la Côte d'Azur, le Bordelais, la Loire et Paris. Les mariages durent plusieurs jours et demandent un hébergement sur place. C'est une HYPOTHÈSE à vérifier, car aucun chiffre ne l'étaie.

### 1.7 Contrainte ERP pour une salle de réception : un cas documenté

La Demeure Historique décrit le cas d'un propriétaire-gestionnaire, « Monsieur N. » [R7-23] (dossier d'octobre 2017, PAGE LUE) :
- « la seule ouverture à la visite s'avère déficitaire. Il décide donc de réhabiliter les communs pour en faire un lieu de réceptions. »
- La salle « ne fait que 98 m2 ». Elle relève d'abord de la 5e catégorie ERP. Après un an et demi d'activité, la commission de sécurité la reclasse « en 4e catégorie », avec une « liste de travaux surréalistes et disproportionnés ».
- « L'affaire a duré plus de deux ans. »
- « Plus de 100 000 euros ont été investis dans les travaux de mise en conformité. »

Pour le modèle, cela donne deux paramètres :
- une **ligne d'investissement ERP de 100 000 € ou plus** pour une salle de réception, même petite. C'est une ESTIMATION fondée sur un seul cas, à confirmer par R3 et par un bureau de contrôle ;
- un **délai administratif** de 1 à 2 ans.

### 1.8 Comptes publiés de sociétés de lieux de réception et de séminaires en château

Source : API officielle « recherche-entreprises.api.gouv.fr », qui reprend les comptes déposés et publiés [R7-63]. Statut : PAGE LUE, données d'API officielle. Montants en euros, sans indication HT. Le chiffre d'affaires d'une société est normalement HT.

| Société (commune, code NAF) | Année | Chiffre d'affaires | Résultat net | Marge nette (ESTIMATION, calcul) | Effectif (tranche INSEE) |
|---|---|---|---|---|---|
| SARL Château du Vau Réception (Ballan-Miré, 37 ; 93.29Z) | 2022 | 129 521 € | 443 € | 0,3 % | 1 à 2 salariés |
| Château du Taillis (Duclair, 76 ; 82.30Z) | 2021 | 77 147 € | 20 879 € | 27,1 % | 3 à 5 |
| Château de Vauloge Promotion (Fercé-sur-Sarthe, 72 ; 82.30Z) | 2023 | 128 589 € | 3 823 € | 3,0 % | 1 à 2 |
| Sté du Château de Chambly (siège à Rueil-Malmaison, 92 ; 82.30Z) | 2022 | 272 531 € | 14 594 € | 5,4 % | 3 à 5 |
| Château Blanc (Neuville-Bosc, 60 ; 82.30Z) | 2020 | 64 178 € | 1 599 € | 2,5 % | non renseigné |
| Chevillon Réception (Auxerre, 89 ; 93.29Z) | 2016 | 595 971 € | 38 265 € | 6,4 % | 3 à 5 |
| Châteauform' France (82.30Z), leader des séminaires | 2025 | 186 366 960 € | 3 406 336 € | 1,8 % | code « 42 » |
| Groupe Châteauform (70.22Z, holding) | 2025 | 18 155 685 € | 5 608 044 € | — | — |

Le code « 42 » correspond à 1 000 à 1 999 salariés dans la nomenclature INSEE. Cette correspondance est à vérifier.

**Lecture** (ESTIMATION) :
- Les sociétés d'exploitation de châteaux de réception de taille familiale réalisent un **chiffre d'affaires de 60 000 à 600 000 € par an**, avec une **marge nette faible**, souvent de 0 à 6 %.
- Ces chiffres ne mesurent pas la rentabilité pour le propriétaire.
  - La société d'exploitation peut verser un loyer à une SCI propriétaire.
  - Le résultat est après rémunération éventuelle des dirigeants.
  - Ce chiffre d'affaires ne couvre pas le gros entretien du château.
- Ordre de grandeur cohérent : 20 mariages × 5 000 à 10 000 € de location, plus quelques séminaires, donnent **100 000 à 250 000 € de chiffre d'affaires**. C'est très en dessous du coût de fonctionnement d'un domaine S2 ou S3 tel que décrit dans le Contexte permanent.
- Le Château des Lys (Paris, traiteur et événements) affichait 1,49 M€ de chiffre d'affaires en 2020. Il apparaît ensuite au BODACC avec une interdiction de gérer de 5 ans pour son dirigeant, le 18/11/2025 [R7-64]. Ce n'est pas un château au sens patrimonial.

---

## 2. Séminaires et événements d'entreprise

### 2.1 Taille du marché et acteur dominant

| Donnée | Valeur | Statut | Source |
|---|---|---|---|
| Chiffre d'affaires de la filière événementielle française en 2023 : organisateurs, agences, gestionnaires de sites, design de stands, prestataires | « Une filière de 10,4 milliards d'euros de chiffre d'affaires ». Ce périmètre est bien plus large que les séminaires en château | PAGE LUE | [R7-24] |
| Intentions des entreprises | « 44 % des entreprises utilisatrices prévoient d'investir dans les événements professionnels en 2026 » | PAGE LUE | [R7-24] |
| **Taille du marché des séminaires résidentiels en France** | **INCONNU** : aucune donnée publique trouvée. Pour vérifier : Event Data Book d'Unimev (PDF non lié sur la page), études Xerfi (payantes), Coesio | INCONNU | — |
| Châteauform', leader des séminaires en « maisons » : chiffre d'affaires en 2024 | « Ce sera notre meilleure année, avec un chiffre d'affaires proche des 300 millions d'euros. » (propos du dirigeant, 06/01/2025, donc avant la clôture des comptes) | PAGE LUE | [R7-25] |
| Châteauform' : chiffre d'affaires 2019 et 2020 | « un chiffre d'affaires de 80 millions d'euros en 2020, contre 255 millions en 2019 ». Divergence : un résultat de recherche donne 237,6 M€ pour 2019 | PAGE LUE (255 M€) / EXTRAIT (237,6 M€) | [R7-26] |
| Châteauform' : nombre de séminaires | « 7 000 séminaires l'an dernier [2020], contre 20 000 un an auparavant [2019] » | PAGE LUE | [R7-26] |
| Châteauform' : parc de maisons | « près de 70 adresses » en 2021, dont 36 à Paris et en Île-de-France. Chiffre de 2021, non actualisé ; la croissance continue en Allemagne (« six maisons aujourd'hui, et donc neuf très bientôt ») | EXTRAIT (70 adresses) / PAGE LUE (Allemagne) | [R7-25] |
| Tendance des formats | Clients cherchant à « pouvoir réunir 50 ou 80 personnes » ; « les gens veulent la moitié de l'espace pour le double d'expérience » | PAGE LUE | [R7-25] |

**ESTIMATIONS** :
- Revenu moyen par séminaire chez Châteauform' en 2019 : 255 M€ ÷ 20 000 = **environ 12 750 € HT par séminaire**. Avec 237,6 M€, on obtient environ 11 900 €.
- On suppose que le chiffre d'affaires est HT et entièrement lié aux séminaires. C'est une hypothèse : le groupe a d'autres activités.
- Chute de 2020 : −69 % en chiffre d'affaires (255 → 80 M€) et −65 % en nombre de séminaires (20 000 → 7 000).

### 2.2 Prix observés (HT, par personne)

| Lieu | Formule | Prix | Statut | Source |
|---|---|---|---|---|
| Château de La Roche-Guyon (Val-d'Oise, à 1 h 30 de Paris) | Forfait journée avec déjeuner buffet, café d'accueil et 2 pauses, base de 20 personnes | « À partir de 95€ HT par personne » (fiche de 2023) | PAGE LUE (PDF) | [R7-27] |
| Château de La Roche-Guyon | Location de salle seule | 250 € HT la demi-journée (32 m²) ; 400 € HT la demi-journée (galerie de 120 m²) | PAGE LUE (PDF) | [R7-27] |
| Château de Châtenay (Val-d'Oise), 33 chambres et 45 couchages, jusqu'à 180 participants | Journée d'étude / séminaire résidentiel | 100 € HT (« À partir de ») / 275 € HT | PAGE LUE (Funbooker, sans date) | [R7-28] |
| Château de Couches (Saône-et-Loire), 3 chambres | Séminaire résidentiel / demi-journée d'étude | 160 € HT par personne / 490 € HT (incohérence sur la page : « À partir de 200 € ») | PAGE LUE (Funbooker, sans date) | [R7-29] |
| L'Ermitage (Rhône, hôtel 4 étoiles, ce n'est pas un château) | Journée d'étude / séminaire résidentiel | 69 € HT / 238 € HT | EXTRAIT | [R7-30] |
| Repère générique « Unimev » cité par 1001 Salles | Budget moyen d'un séminaire, tous postes confondus | 285 € HT par personne et par jour | EXTRAIT (page en erreur 522, chiffre non vérifié à la source) | [R7-31] |
| Centre des monuments nationaux, Château de Maisons | Salles pour un événement d'entreprise, le mardi de 9 h à 18 h | 3 500 € HT / 4 200 € TTC (prix plancher) | PAGE LUE (PDF) | [R7-13] |

**Lecture pour le modèle** (ESTIMATION) :
- **Journée d'étude** en château : environ 70 à 100 € HT par personne. Elle inclut la restauration, donc une marge brute limitée si le château n'a pas de cuisine propre.
- **Séminaire résidentiel** : environ 160 à 275 € HT par personne et par jour, avec une nuit.
- Un séminaire résidentiel de 25 personnes sur 2 jours rapporte environ 25 × 2 × 200 à 275 €, soit **10 000 à 14 000 € HT**. C'est cohérent avec la moyenne d'environ 12 000 € par séminaire chez Châteauform'.
- Il faut au moins une vingtaine de chambres, une cuisine professionnelle et du personnel de service. C'est une activité **hôtelière**, pas une simple location.

**Saisonnalité** : pas de statistique trouvée. Qualitativement, les séminaires se tiennent en semaine, hors juillet-août et hors fêtes de fin d'année. Ils sont donc complémentaires des mariages, qui ont lieu le samedi en été. C'est une HYPOTHÈSE classique non sourcée ici.

**Concurrence** :
- Le leader, Châteauform', exploite environ 70 lieux en propre (donnée de 2021) avec une marque nationale.
- Les plateformes (Funbooker, 1001 Salles, Bird Office) référencent de nombreux châteaux. Je n'ai pas de compteur lu ; c'est INCONNU.
- Un château isolé à plus de 1 h 30 de Paris ou d'une métropole a peu de chances de capter des séminaires résidentiels réguliers. C'est une HYPOTHÈSE à vérifier, par exemple par la répartition géographique des maisons Châteauform', dont 36 sur 70 sont en Île-de-France [R7-25].

---

## 3. Tournages et prises de vue

### 3.1 Grille officielle du Centre des monuments nationaux (référence de prix)

Source : « Grille tarifaire tournages et prises de vue CMN 2024 » (PDF modifié en novembre 2025) [R7-12], lié depuis la page « Tournage et prise de vue » du CMN [R7-14]. Ce sont des tarifs « À PARTIR DE », HT et TTC (TVA 20 %).

Les monuments sont classés en trois catégories :
- **A** : Arc de Triomphe, Panthéon, Sainte-Chapelle…
- **B** : notamment les châteaux de Champs-sur-Marne, Maisons, Azay-le-Rideau, Pierrefonds, Bouges, La Motte-Tilly, Haroué.
- **C** : notamment Chareil-Cintrat, Talcy, Fougères-sur-Bièvre, Villeneuve-Lembron, Cadillac, Assier, Gramont.

**Tournages, forfait de 12 h avec 1 agent inclus** :

| Nature | Cat. A HT | Cat. B HT | Cat. C HT |
|---|---|---|---|
| Publicité, bande-annonce | 15 000 € | 7 000 € | 3 800 € |
| Long métrage | 9 000 € | 5 500 € | 3 500 € |
| Téléfilm, série TV, docu-fiction, web-série… | 6 000 € | 3 500 € | 2 500 € |
| Clip, court métrage | 2 500 € | 2 500 € | 2 500 € |

**Tournages légers, forfait de 8 h, équipe de moins de 5 personnes** : émission, documentaire ou film institutionnel, 1 300 € (A), 1 000 € (B) et 850 € (C) HT.

**Prises de vue photo, forfait de 8 h** :

| Nature | Cat. A HT | Cat. B HT | Cat. C HT |
|---|---|---|---|
| Publicité | 7 000 € | 5 000 € | 3 000 € |
| Reportage de magazine ou catalogue (« mode, auto, décoration, parfum, bijoux, chaussures, cosmétique… ») | 3 000 € | 2 000 € | 1 700 € |
| Photo de mariage, forfait de 2 h | 150 € | 150 € | 150 € |

Statut de toutes les valeurs : PAGE LUE (PDF) [R7-12].

**Lecture** :
- Pour un château privé de gamme « B ou C », le **tarif plancher de place** se situe autour de 2 500 à 5 500 € HT par jour de tournage de fiction, et autour de 1 700 à 3 000 € HT par jour pour une prise de vue de marque (catalogue).
- Un château privé peut viser plus haut, car il offre l'exclusivité, des intérieurs meublés et l'absence de visiteurs. La grille du CMN reste un repère que les régisseurs connaissent.
- Cette lecture est une ESTIMATION.

### 3.2 Marché privé : plateformes et exemples

| Donnée | Valeur | Statut | Source |
|---|---|---|---|
| Giggster, catégorie « Château » en France : 20 annonces visibles | De 60 €/h (manoir à Barzy-sur-Marne) à 1 235 €/h (grand domaine près de Pouancé) ; château de luxe à Bouffémont 1 000 €/h ; château en Provence (Sarrians) 895 €/h ; « Petit château » (Abjat-sur-Bandiat) 150 €/h. HT ou TTC non précisé | PAGE LUE | [R7-32] |
| Giggster, coût moyen sur toute la plateforme | 273 €/h | PAGE LUE | [R7-32] |
| Château de Gudanes (Ariège) : tournages et photos | Aucun tarif publié : frais « sur mesure ». Clients cités : Zimmermann, Cire Trudon, Dôen, Sézane, Mango Home… Chaque réservation inclut la « privatisation exclusive du château » | PAGE LUE | [R7-33] |
| Château de Picomtal : photos en intérieur | 150 € par séance de 1 h 30 | PAGE LUE | [R7-07] |
| Fondation du Château de Chillon (Suisse, pour comparaison) | CHF 1 000 par journée de tournage non promotionnel (2025) ; CHF 500 en 2020 | EXTRAIT | [R7-34] |
| « Château lambda » : 4 500 € par jour (article de Slate, ancien) | 4 500 € par jour | EXTRAIT (page en 403) | [R7-35] |

### 3.3 Concurrence et fréquence

| Donnée | Valeur | Statut | Source |
|---|---|---|---|
| Part des tournages français réalisés en Île-de-France | « La région Île-de-France concentre plus de 50% des tournages en France » (section « En 2025 ») | PAGE LUE | [R7-36] |
| Décors référencés par Film Paris Region | « plus de 2300 décors » ; « Châteaux et domaines historiques » est cité comme style disponible, sans compteur | PAGE LUE | [R7-37] |
| Lieux accompagnés en 2025 | « Film Paris Region a accompagné 400 oeuvres, référencé 263 lieux accueillant des tournages » | PAGE LUE | [R7-36] |
| **Fréquence réaliste de tournages pour un château ordinaire** | **INCONNU** : aucune statistique publique trouvée | INCONNU | — |

Pour la fréquence, je propose une HYPOTHÈSE de modélisation non sourcée, à valider auprès de régisseurs ou d'agences de décors :
- château à moins d'1 h 30 de Paris, bien référencé (Film Paris Region, plateformes, agences) : **2 à 6 jours de tournage ou de shooting par an** ;
- château en province : **0 à 2 jours par an**, avec une forte irrégularité, certaines années à zéro.

Pour le modèle, je préconise de traiter les tournages comme un revenu **occasionnel et non garanti**, sans le compter dans le socle récurrent. Le montant indicatif serait de 0 à 20 000 € HT par an, soit 0 à 4 jours à environ 3 000-5 000 € HT. C'est une ESTIMATION fondée sur la grille du CMN.

Méthodes pour vérifier :
- interroger les commissions régionales du film (Film Paris Region, Ciclic en Centre-Val de Loire, Normandie Images) sur le nombre de demandes portant sur des châteaux privés ;
- consulter les études Audiens sur les jours de tournage.

**Contraintes** :
- Un tournage mobilise le lieu plusieurs jours (préparation, tournage, remise en état).
- Il entraîne des risques pour les intérieurs (assurance, état des lieux) et un fort trafic de véhicules techniques.
- Il est peu compatible avec des chevaux au pré près des zones de tournage : bruit, groupes électrogènes. C'est une HYPOTHÈSE.
- Les **shootings de marques de luxe** sont courts (1 jour), mieux payés au jour et discrets. Gudanes en est un exemple, mais son tarif n'est pas publié.

---

## 4. Châteaux-hôtels

### 4.1 Performances de l'hôtellerie en 2025 (MKG pour l'UMIH, In Extenso)

Source principale : « Observatoire mensuel des performances hôtelières UMIH – GNC, Décembre 2025 », données MKG_destination. Les prix moyens et le RevPAR sont **en euros HT**, en **cumul janvier-décembre 2025** [R7-38]. Statut : PAGE LUE (PDF extrait localement).

**Limite** : la catégorie « Haut de Gamme » de MKG n'est pas définie dans le document. Il s'agit probablement des 4 et 5 étoiles ; c'est une HYPOTHÈSE à vérifier. L'échantillon est surtout urbain : ce ne sont **pas** des chiffres spécifiques aux châteaux-hôtels de campagne.

| Zone, catégorie « Haut de Gamme », 2025 | Taux d'occupation | Prix moyen HT | RevPAR HT |
|---|---|---|---|
| France | 71,7 % | 299,3 € | 214,6 € |
| Paris | 78,5 % | 372,7 € | 292,5 € |
| Indre-et-Loire (Val de Loire) | 72,6 % | 140,6 € | 102,1 € |
| Calvados (Normandie) | 65,1 % | 282,6 € | 183,8 € |
| Ille-et-Vilaine | 67,7 % | 236,2 € | 160,0 € |
| Marne (Champagne) | 73,4 % | 410,8 € | 301,4 € |
| Gironde | 65,1 % | 224,9 € | 146,4 € |
| Var | 53,7 % | 491,2 € | 263,8 € |
| Vaucluse | 62,3 % | 187,7 € | 116,9 € |
| Alpes-Maritimes | 65,4 % | 429,7 € | 280,9 € |
| Pyrénées-Atlantiques | 62,1 % | 403,5 € | 250,5 € |
| Val-d'Oise | 75,0 % | 123,9 € | 92,9 € |

| Ensemble des catégories, 2025 | Taux d'occupation | Prix moyen HT | RevPAR HT |
|---|---|---|---|
| France | 66,2 % | 126,9 € | 84,0 € (+1,4 %) |
| Province | 63,1 % | 108,5 € | 68,5 € (+2,7 %) |

Citation [R7-38] : « La Province clôture 2025 sur un bilan positif (+2,7%), malgré le repli des grandes métropoles de l'intérieur : le haut de gamme et les territoires « loisirs », littoraux ou de montagne, y ont porté la croissance. »

In Extenso, bilan 2025 publié le 09/02/2026 [R7-39], [R7-40], PAGE LUE :
- France : taux d'occupation de 63 % [R7-39] ou 64 % [R7-40], selon l'article. La divergence est conservée.
- Prix moyen de 133 € ; RevPAR de 85 €.
- Paris : taux d'occupation de 82 %, prix moyen de 239 €.
- Côte d'Azur : taux d'occupation de 68 %, prix moyen de 226 €, RevPAR de 154 €, RevPAR du segment luxe +9 %.
- Offre nouvelle : « Environ 150 créations d'hôtels par an, soit 7 000 chambres », et 835 projets actifs représentant 64 000 chambres [R7-40].

**Lecture pour un château-hôtel de campagne** (ESTIMATION) :
- Hors littoral, Paris, Champagne et Côte d'Azur, le haut de gamme départemental en zone de châteaux se situe autour de **140 à 230 € HT de prix moyen** et **100 à 160 € HT de RevPAR**. Exemples : l'Indre-et-Loire (140,6 € de prix moyen) et la Gironde (224,9 €).
- Un château-hôtel de 15 à 20 chambres à 65 % d'occupation et 250 € HT de prix moyen génère **environ 1,0 à 1,2 M€ HT de chiffre d'affaires d'hébergement** par an. Calcul : 15 × 365 × 0,65 × 250 = 0,89 M€ ; 20 × 365 × 0,65 × 250 = 1,19 M€.
- S'y ajoutent la restauration et les événements.

### 4.2 Coût d'investissement par chambre : exemples réels

| Projet | Investissement | Chambres | Ratio par chambre (ESTIMATION, calcul) | Statut | Source |
|---|---|---|---|---|---|
| Château Louise de La Vallière (Reugny, Indre-et-Loire), Relais & Châteaux, ouvert le 15/10/2022, parc de 19 ha | « 13,5 M€ y ont été investis » | « 20 chambres et suites » | **≈ 675 000 € par chambre** | PAGE LUE | [R7-41] |
| Même établissement : effectif et prix | « L'effectif total projeté compte 33 personnes » ; « Les prix des chambres varient de 440 € pour une chambre à 850 € pour une suite » (TTC implicite, prix public) | — | ≈ 1,65 salarié par chambre | PAGE LUE | [R7-41] |
| Château de Lignan (Hérault), LJ Hôtels, montée en gamme vers le 5 étoiles | « plus de 20 millions d'euros » | 37 clés (4 étoiles avant les travaux) | ≈ 540 000 € par clé ou plus | EXTRAIT (page en 503) | [R7-42] |
| Château de Portereau (Vertou), futur 4 étoiles | 9 à 10 M€ | 26 chambres | ≈ 350 000 à 385 000 € par chambre | EXTRAIT (page en 503) | [R7-43] |
| Château d'Eza (Alpes-Maritimes), passage au 5 étoiles en 2011 | 2 M€ | 11 chambres et suites | ≈ 180 000 € par chambre (rénovation partielle, 2011) | EXTRAIT | [R7-44] |

**Lecture** :
- La transformation d'un château en hôtel haut de gamme coûte **350 000 à 700 000 € par chambre**. Ces montants s'entendent hors acquisition, avec un spa et un restaurant gastronomique dans les projets les plus chers. C'est une ESTIMATION fondée sur 3 projets récents.
- Pour 20 chambres, il faut prévoir **7 à 14 M€**. C'est hors de portée sans investisseur ni emprunt, et ce n'est pas compatible avec l'objectif de ne pas recourir à la fortune personnelle, sauf en confiant l'hôtel à un opérateur qui investit, par bail ou concession.

### 4.3 Contrats de gestion et baux

| Donnée | Valeur | Statut | Source |
|---|---|---|---|
| Redevance de base d'un contrat de gestion (Europe) | « Base fees typically range from 2% to 4% of total revenue. » | PAGE LUE (article HVS de 2007, ancien) | [R7-45] |
| Redevance d'incitation (incentive fee) | « a set incentive fee of about 10% of GOP was typical » ; jusqu'à « 15% of GOP » si la base est plus faible | PAGE LUE (2007) | [R7-45] |
| Durée des contrats | « Initial terms usually last ten, 15 or 20 years » ; moyenne actuelle d'environ « 15 years » ; environ 50 ans pour les opérateurs les plus prestigieux | PAGE LUE (2007) | [R7-45] |
| **Loyer d'un bail hôtelier en % du chiffre d'affaires (France)** | **INCONNU** : aucune source lue. Pour vérifier : expertises hôtelières (In Extenso, Christie & Co, MKG), baux publics de châteaux concédés (exemple de la concession hôtelière de Versailles : bail de 40 ans selon un EXTRAIT [R7-46]) | INCONNU | — |

### 4.4 Marge d'exploitation (GOP)

- **INCONNU** : je n'ai trouvé aucun taux de GOP public pour l'hôtellerie de luxe en France ou à la campagne. La recherche a été faite.
  - Ces ratios sont dans des études payantes (HotStats, MKG, CBRE, In Extenso, Deloitte).
  - Pour vérifier : demander à un expert-comptable spécialisé, ou lire les comptes publiés de sociétés d'hôtels-châteaux (greffe ; Pappers étant bloqué, passer par data.inpi.fr ou Infogreffe).
- Contexte qualitatif :
  - Hospitality ON (EXTRAIT, citant MKG) : 2025 confirme « la résilience structurelle du segment upper-upscale et luxe, porté surtout par les prix plutôt que par le volume » [R7-47].
  - La phrase « Côte d'Azur et montagne » décrites comme des « moteurs très rentables » vient aussi d'un EXTRAIT [R7-47].
- **Signal de coût** : Louise de La Vallière prévoit 33 salariés pour 20 chambres [R7-41].
  - Coût annuel, en ESTIMATION : 33 × environ 40 000 à 45 000 € de coût employeur chargé ≈ **1,3 à 1,5 M€**. Le coût unitaire est une HYPOTHÈSE à recaler sur les données de R2.
  - Chiffre d'affaires d'hébergement possible : 20 chambres × 365 × 65 % × environ 500 € HT ≈ **2,4 M€**. Le taux d'occupation et le prix sont des HYPOTHÈSES.
  - Conclusion : la masse salariale absorbe une grande part du chiffre d'affaires. Un château-hôtel de moins de 20 chambres est fragile.

### 4.5 Concurrence (châteaux-hôtels)

- Offre nouvelle importante : environ 150 créations d'hôtels par an et 64 000 chambres en projet en France [R7-40].
- **INCONNU** : le nombre exact de châteaux-hôtels en France. Pour vérifier : compter les membres français des labels Relais & Châteaux et Châteaux & Hôtels Collection (sites non ouverts ici, faute de budget).

---

## 5. Gîtes, chambres d'hôtes, grandes maisons, location de luxe à la semaine

### 5.1 Gîtes de France : occupation et saisonnalité

| Donnée | Valeur | Statut | Source |
|---|---|---|---|
| Réseau Gîtes de France en 2024 : propriétaires, nuitées, occupation | 42 000 propriétaires, 27,2 millions de nuitées (+3 %), « taux d'occupation […] stable, à 47% » | EXTRAIT (page en 403) | [R7-48] |
| Été 2025 (juillet-août) | « un taux d'occupation national de 86% » ; août à 90 %, juillet à 82 % ; Normandie, Corse et Hauts-de-France à 90 %, Centre-Val de Loire à 85 % ; clientèle étrangère à 20 % des séjours | PAGE LUE (03/09/2025) | [R7-49] |
| Ardèche, 354 gîtes en centrale de réservation exclusive Gîtes de France | « Le taux d'occupation moyen sur l'année est de 44% ». Définition : semaines louées ÷ semaines louables, soit environ 23 semaines par an (ESTIMATION, calcul) ; 263 000 nuitées en 2024 | PAGE LUE (PDF) | [R7-50] |
| Ardèche : offre de meublés de tourisme (concurrence) | « 4 900 meublés de tourisme gérés par 3 300 entités de gestion », 24 300 lits, soit 21 % des lits marchands du département ; 48 meublés 5 étoiles | PAGE LUE (PDF) | [R7-50] |
| Panier moyen d'un gîte rural / d'une chambre d'hôtes | 733 € par séjour / 217 € | EXTRAIT (source commerciale non officielle, fiabilité faible) | [R7-51] |
| **Revenu moyen annuel d'un propriétaire de gîte** | **INCONNU** : non publié en ligne d'après mes recherches. Pour vérifier : rapport annuel de la Fédération nationale des Gîtes de France, ou relais départementaux | INCONNU | — |

### 5.2 Cadre réglementaire des meublés de tourisme (fiche officielle vérifiée le 21 mai 2026)

Source [R7-52], PAGE LUE. La synthèse est fidèle, mais la page a été restituée en résumé et non en citation exacte. La fiscalité (abattements micro-BIC, loi Le Meur) relève de R3.

- Déclaration en mairie obligatoire :
  - « déclaration simple » (cerfa n° 14004), amende jusqu'à 450 € en cas d'absence ;
  - « déclaration avec enregistrement » dans les communes qui l'imposent, avec un numéro à 13 caractères et une amende jusqu'à 5 000 € en cas d'absence.
- En régime d'enregistrement, avec autorisation de changement d'usage, le DPE doit être classé de A à E en métropole, puis de A à D à partir de 2034. Exploiter sans autorisation expose à une amende jusqu'à 100 000 €.
- Classement de 1 à 5 étoiles facultatif et payant, valable 5 ans. Il donne un abattement forfaitaire plus favorable en micro-entreprise et des exonérations possibles en zone France Ruralités Revitalisation (ZFRR).
- Taxe de séjour et fiche de police pour la clientèle étrangère.

**Point d'attention pour un château** : un château énergivore (DPE F ou G) peut être **interdit de location en meublé de tourisme** dans les communes à enregistrement, et à terme plus largement. Il faut vérifier les règles exactes avec R3. C'est un vrai risque pour le scénario « gîte dans les communs » si ces derniers ne sont pas rénovés. Cette lecture est une ESTIMATION.

### 5.3 Location de luxe à la semaine (Le Collectionist, octobre 2026)

Le site revendique « 2 300 propriétés à louer », toutes destinations confondues [R7-53]. Les prix ci-dessous sont **par semaine**. Le site ne précise pas s'ils sont HT ou TTC, ni s'ils incluent sa commission. La part reversée au propriétaire est **INCONNUE**.

| Propriété (région) | Capacité | Prix par semaine | Statut | Source |
|---|---|---|---|---|
| Château Mansart (Calvados) | 40 voyageurs, 16 chambres | 56 230 à 61 850 € | PAGE LUE | [R7-54] |
| Manoir Alméra (Deauville) | 12 voyageurs, 8 chambres | 27 075 à 29 690 € | PAGE LUE | [R7-54] |
| Manoir Alex (Trouville) | 12 voyageurs, 6 chambres | 12 755 à 19 130 € | PAGE LUE | [R7-54] |
| Mas, bastides et domaines de Provence (17 fiches) | 8 à 22 voyageurs, 4 à 9 chambres | de 6 500 € (minimum, Mas Lauria) à 38 650 € (maximum, Mas Estia) | PAGE LUE | [R7-55] |
| Dordogne (12 propriétés, dont « Château de la Belle » pour 22 personnes et « Château Renaissance » pour 20) | — | prix affichés seulement avec des dates | PAGE LUE | [R7-56] |
| Région de Bordeaux (9 propriétés, dont « Château Hippolyte » pour 33 personnes et 14 chambres) | — | prix affichés seulement avec des dates | PAGE LUE | [R7-57] |

**Concurrence** : 17 propriétés en Normandie, 12 en Dordogne et 9 dans le Bordelais sur cette plateforme, qui est **très sélective**. Le segment des châteaux loués à la semaine avec service est étroit, mais la clientèle est internationale et à très haut pouvoir d'achat.

**ESTIMATION de revenu brut pour un château de 15 chambres et 40 personnes** :
- Au prix de Château Mansart, 8 semaines louées rapportent environ **450 000 à 495 000 €**. Avec 12 semaines, on atteint environ 675 000 €.
- Il faut déduire la commission de la plateforme (INCONNUE), la conciergerie, le ménage, le linge, le personnel et l'énergie.
- Le nombre de semaines est une HYPOTHÈSE. Je n'ai aucune donnée d'occupation pour ce segment ; c'est INCONNU.
- **Incompatible avec la résidence privée** pendant les semaines louées si l'on loue le château principal. C'est compatible si l'on loue une **dépendance autonome** : une aile ou des communs rénovés.

---

## 6. Hébergements insolites et glamping

| Donnée | Valeur | Statut | Source |
|---|---|---|---|
| Marché français (étude Protourisme pour Hôtes-Insolites, 2022) | « un chiffre d'affaires global de 220 millions d'euros » ; « 3 026 sites d'hébergements insolites en France pour un total de presque 10 000 modules » ; « un budget pour une nuit de 142€ » ; « une durée de séjour de 1,7 nuit ». Méthode : 370 répondants sur 3 000 | PAGE LUE (20/07/2022) | [R7-58] |
| Observatoire de l'Insolite (Unic Stay / AbracadaRoom et Alliances, décembre 2024) | volume d'affaires de 430 M€ pour 2 226 sites professionnels (+65 % par rapport à 2021) ; prix moyen de 301 € pour les cabanes et de 265 € toutes typologies | EXTRAIT (page en 403) | [R7-59] |
| Prix observés en Tarn-et-Garonne (« à partir de », par nuit) | de 75 € (cabane, Belvèze) à 316,10 € (cabane et spa, Labastide-de-Penne) ; 102 hébergements insolites recensés dans le département | PAGE LUE | [R7-60] |
| Taux d'occupation d'un glamping | environ 45 % la première année, puis 60 à 75 % (éditeur de logiciel, sans source primaire) | EXTRAIT (fiabilité faible) | [R7-61] |
| **Urbanisme** : permis d'aménager exigé pour la « Création ou agrandissement d'un terrain permettant l'accueil de plus de 20 personnes ou de plus de 6 hébergements de loisirs constitués de tentes, de caravanes, de résidences mobiles de loisirs ou d'habitations légères de loisirs » | seuils de 20 personnes et 6 hébergements | PAGE LUE (fiche vérifiée le 13/02/2026) | [R7-62] |
| **Investissement par unité (cabane, lodge, bulle)** | **INCONNU** : aucune donnée sourcée trouvée. Pour vérifier : devis de fabricants (cabanes perchées, tentes lodge), guides CCI ou ADT | INCONNU | — |

**ESTIMATIONS (calculs sur l'étude de 2022)** :
- Chiffre d'affaires moyen par module : 220 M€ ÷ environ 10 000 = **environ 22 000 € par module et par an**, soit environ 72 700 € par site.
- À 142 € par nuit, cela fait environ 155 nuits vendues par module, soit environ **42 % d'occupation**. Le résultat est cohérent avec les 44-47 % d'occupation des gîtes.
- Avec l'Observatoire 2024, on obtient 430 M€ ÷ 2 226 ≈ 193 000 € par site professionnel. Les périmètres diffèrent ; la divergence est conservée.

**Lecture pour le domaine** :
- 5 ou 6 cabanes, sous le seuil de 6 hébergements, pourraient produire environ **100 000 à 130 000 € de chiffre d'affaires HT par an**. Calcul : 6 × 22 000 = 132 000 €.
- Avec des prix plus élevés, autour de 250-300 € la nuit pour un positionnement château, on obtient davantage, sans donnée d'occupation pour ce positionnement.
- Charges importantes : ménage à chaque départ (séjours courts de 1,7 nuit), linge, petit-déjeuner, accueil.
- Effet sur la tranquillité : flux de clients chaque jour, surtout le week-end. Il est modéré si les unités sont regroupées loin de la partie privée et des écuries.
- Concurrence : 2 200 à 3 000 sites en France, en forte croissance depuis 2021. Le marché est **en voie de saturation** dans les zones touristiques ; c'est une HYPOTHÈSE.

---

## 7. Visites

### 7.1 Fréquentation et contexte

| Donnée | Valeur | Statut | Source |
|---|---|---|---|
| Monuments adhérents de La Demeure Historique | « plus de 3 000 monuments », « dont près de la moitié accueille chaque année plus de 9 millions de visiteurs » | PAGE LUE | [R7-20] (dossier de presse du 31/03/2026), [R7-22] |
| Monuments et jardins privés référencés sur la plateforme « Châteaux près d'ici » | « près de 500 monuments et jardins historiques privés participants » | PAGE LUE | [R7-20] |
| Arrêtés de protection monuments historiques en France | « Sur les 44 675 arrêtés de protection pris par l'État, près de la moitié concernent des monuments historiques protégés appartenant à des propriétaires privés » | PAGE LUE | [R7-23] (2017) |
| Monuments historiques en vente ou sans repreneur | « plus de 1 000 monuments historiques sont en vente ou en manque de repreneurs » ; « la durée moyenne de détention se réduit à 7 ans » | PAGE LUE | [R7-23] (2017, chiffre ancien et non actualisé) |
| Rentabilité de l'exploitation | La Demeure Historique parle d'une exploitation « structurellement déficitaire » | PAGE LUE | [R7-23] |

**ESTIMATION de la fréquentation moyenne** :
- 9 millions de visiteurs ÷ environ 1 500 monuments ouverts (« près de la moitié » de 3 000) = **environ 6 000 visiteurs par monument et par an** en moyenne.
- La distribution est très asymétrique. Quelques grands sites (Chenonceau, Vaux-le-Vicomte, Cheverny, Villandry, Brissac) concentrent une part importante des visiteurs. Je n'ai pas leurs chiffres ici : ce sont des cas de R4.
- La **médiane** est donc probablement bien inférieure à 6 000. C'est une HYPOTHÈSE.
- **INCONNU** : la répartition des monuments privés par tranche de fréquentation. Je n'ai trouvé aucune statistique publique ; la recherche a été faite.
  - Pour vérifier, consulter l'enquête de La Demeure Historique auprès de ses adhérents (non publiée en ligne d'après mes recherches) ou les données de fréquentation du ministère de la Culture (publication « Patrimostat »).


### 7.2 Prix des billets observés (octobre 2026)

| Site | Billet | Prix | HT/TTC | Statut | Source |
|---|---|---|---|---|---|
| Château de Cheverny (privé, ouvert 365 jours par an [R7-73]) | Château et jardins, adulte / réduit | 15,5 € / 11,5 € ; visite guidée +5 € ; avec exposition et bateaux électriques : 26 € | non précisé (prix public, donc TTC implicite) | PAGE LUE | [R7-67] |
| Château de Breteuil (privé, ouvert toute l'année) | Château, jardins et scènes de contes / parc seul, adulte | 19,50 € / 13,50 € | non précisé (TTC implicite) | PAGE LUE | [R7-69] |
| Château d'Ormesson (privé, ouverture exceptionnelle à l'été 2026) | Visite de l'oratoire | 15 € par personne | non précisé | EXTRAIT | [R7-71] |
| Château de Sarzay (Indre) | Visite libre | « 14 euros pour deux adultes » (avis d'internaute) | non précisé | EXTRAIT (fiabilité faible) | [R7-72] |
| CMN (Champs-sur-Marne, Azay-le-Rideau) | Visite privée de 1 à 30 personnes, 2 h, hors guide | 550 € HT / 660 € TTC | HT et TTC | PAGE LUE | [R7-13] |

Autres activités tarifées par les grands sites privés :
- Cheverny loue des salles : 500 à 950 € HT (90 m², 49 personnes au plus, « No dancing possible ») ; 675 à 1 700 € HT (150 m², 150 personnes) ; salle à manger du château 2 500 € HT pour 2 à 25 personnes au dîner [R7-68].
- Breteuil propose mariages, séminaires, « Dîners d'Exception », tournages et un appartement à louer, tous sur devis [R7-70].

Le taux de TVA applicable aux droits d'entrée relève de R3 et n'est pas vérifié ici.

### 7.3 Coûts d'ouverture et seuil de rentabilité

- **Données sourcées** :
  - La Demeure Historique cite un propriétaire pour qui « la seule ouverture à la visite s'avère déficitaire » [R7-23].
  - Elle parle aussi d'une exploitation des monuments « structurellement déficitaire » [R7-23].
  - **Aucun coût d'ouverture chiffré** n'a été trouvé ; c'est INCONNU.
- **ESTIMATION illustrative**, à recaler avec R2 (salaires) et R3 (TVA, ERP) :
  - Ouverture d'environ 100 jours par an : juillet-août et week-ends de mai, juin et septembre.
  - Personnel : 2 agents d'accueil ou guides saisonniers pendant environ 4 mois, plus billetterie, assurance de responsabilité civile, sanitaires, signalétique et communication. Coût direct d'environ **40 000 à 60 000 € par an**. C'est une HYPOTHÈSE non sourcée.
  - Recette nette par visiteur d'environ 9 € HT, pour un billet de 10 à 12 € TTC, après TVA, gratuités et réductions. C'est une HYPOTHÈSE.
  - **Seuil de rentabilité direct d'environ 4 500 à 6 500 visiteurs par an**, soit environ la moyenne estimée des monuments adhérents de La Demeure Historique (environ 6 000, §7).
  - Conclusion : pour un château « ordinaire », les visites couvrent au mieux leurs propres coûts. Elles **ne financent pas** le domaine.
  - Leur intérêt est surtout **fiscal**, par le régime des monuments historiques ouverts au public (voir R3), et lié à l'**image**.
- Pour la tranquillité, l'ouverture fait entrer le public dans la propriété pendant les jours d'ouverture. Elle est incompatible avec l'usage privé des pièces visitées pendant ces jours.

---

## 8. Chocs : 2020, rebond, assurance annulation

| Donnée | Valeur | Statut | Source |
|---|---|---|---|
| Mariages en 2020 | « la chute observée en 2020 est inédite et s'élève à − 31,2 % » (154 581 contre 224 740) | PAGE LUE | [R7-16], [R7-01] |
| Premier confinement | « Durant le premier confinement, seuls 538 mariages ont été célébrés » ; avril 2020 : 226 (15 928 en avril 2019) ; mai 2020 : 803 (18 334 en mai 2019) | PAGE LUE | [R7-16] |
| Été 2020 (juin à août) | 62 000 mariages contre 104 000 en 2019, soit −40 % (ESTIMATION, calcul) | PAGE LUE | [R7-16] |
| Rebond | 2021 : +42 % sur 2020, sans retrouver le niveau de 2019 (218 819) ; 2022 : 241 710, soit +7,6 % sur 2019 | PAGE LUE | [R7-16], [R7-01] |
| Séminaires, Châteauform' | chiffre d'affaires de 80 M€ en 2020 contre 255 M€ en 2019 (−69 %) ; 7 000 séminaires contre 20 000 (−65 %) | PAGE LUE | [R7-26] |
| Séminaires, rebond | Châteauform' France : 186,4 M€ de chiffre d'affaires en 2025 [R7-63] ; groupe : « proche des 300 millions d'euros » en 2024 [R7-25] | PAGE LUE | [R7-63], [R7-25] |
| Monuments historiques privés (31/03/2021) | « Un an après le début de la crise sanitaire, seuls les parcs et jardins historiques peuvent rouvrir » ; « Il n'y a pas une semaine où je ne reçois pas un coup de fil d'un propriétaire me disant qu'il jette l'éponge, qu'il va vendre son bien car il ne peut plus payer l'entretien et les charges. » (président de La Demeure Historique) | PAGE LUE | [R7-21] |
| Assurance annulation (mariage ou événement) : prix, couverture des pandémies | **INCONNU** : aucune source lue, faute de budget de recherche. Pour vérifier : conditions générales des assureurs du mariage et clauses d'acompte et de report des contrats de lieux | INCONNU | — |

**Lecture pour les stress tests** (ESTIMATION) :
- Un choc de type 2020 retire **30 à 70 % du chiffre d'affaires événementiel** pendant un an : −31 % pour les mariages au niveau national, −40 % pour les mariages d'été, −69 % pour le leader des séminaires.
- Le retour au niveau antérieur prend 1 à 2 ans.
- Les acomptes reportés (« reports ») créent un problème de trésorerie plus qu'une perte définitive pour les mariages, qui ont été reportés en 2021-2022. C'est une HYPOTHÈSE cohérente avec le rebond INSEE de 2022.

---

## 9. Livrable : synthèse par activité

Conventions :
- Montants HT sauf mention contraire.
- « E » signale une ESTIMATION, « H » une HYPOTHÈSE, « ? » une donnée INCONNUE.
- Les sources sont détaillées dans les sections précédentes.

| Activité | Chiffre d'affaires par unité | Marge contributive | Investissement | Personnel | Saisonnalité | Impact sur la tranquillité | Concurrence |
|---|---|---|---|---|---|---|---|
| **Mariages, location du lieu « nu » ou avec couchage** | 4 000 à 10 000 € par week-end sans hébergement (HT/TTC non précisé) [R7-07][R7-09][R7-10] ; 6 000 à 20 000 € avec 10 à 25 couchages (E) ; référence publique du CMN 2 400 à 4 400 € HT [R7-13]. Volume réaliste de 15 à 25 par an (E) | ? Marge nette des sociétés d'exploitation : 0 à 6 % [R7-63]. Marge contributive avant frais fixes : ? | Salle ERP : 100 000 € ou plus (1 cas, [R7-23]) ; sanitaires, parking, limiteur de son (?) | 0,5 à 1 ETP de coordination, plus des extras (H) | 59 % des mariages de juin à septembre ; 82 % le samedi [R7-15] | **Fort** : jusqu'à 3 h 30 du matin [R7-07], 60 à 150 invités, conflit avec les chevaux et la résidence | **Forte** : 1 382 châteaux et 3 769 domaines sur Mariages.net [R7-05][R7-06] ; environ 22 mariages par château et par an (E) |
| **Séminaires** | Journée d'étude : 70 à 100 € HT par personne ; résidentiel : 160 à 275 € HT par personne et par jour [R7-27][R7-28][R7-29] ; environ 10 000 à 14 000 € par séminaire résidentiel (E) | Marge nette de Châteauform' France : 1,8 % (2025) [R7-63] ; marge contributive : ? | Lourd : 20 chambres ou plus, cuisine professionnelle, salles équipées (H) | Hôtelier : environ 93 000 à 186 000 € de chiffre d'affaires par salarié chez Châteauform' France (E : 186,4 M€ ÷ 1 000 à 1 999 salariés, tranche INSEE « 42 » à vérifier) | Semaine, hors juillet-août (H) | **Moyen** : en semaine, avec des soirées possibles | **Forte** : leader d'environ 70 lieux, dont 36 en Île-de-France (2021) [R7-25] ; la proximité de Paris est décisive (H) |
| **Tournages et shootings** | Fiction : 2 500 à 5 500 € HT par jour ; catalogue : 1 700 à 3 000 € HT par jour (CMN B/C) [R7-12] ; Giggster : 60 à 1 235 € par heure [R7-32] | Élevée, avec peu de coûts directs (H) | Quasi nul : assurance, référencement | Présence du régisseur (H) | Irrégulière (?) | **Moyen** : ponctuel mais intense, avec camions et équipes | Plus de 2 300 décors en Île-de-France [R7-37] ; plus de 50 % des tournages en Île-de-France [R7-36] ; fréquence ? (H : 0 à 6 jours par an) |
| **Château-hôtel** | RevPAR haut de gamme de 100 à 160 € HT dans les départements de châteaux hors littoral [R7-38], soit 36 500 à 58 400 € HT par chambre et par an (hébergement seul, E) ; prix publics de 440 à 850 € (Louise de La Vallière) [R7-41] | GOP : ? ; contrat de gestion : base de 2 à 4 % du chiffre d'affaires et incentive d'environ 10 % du GOP [R7-45] | **350 000 à 700 000 € par chambre** [R7-41][R7-42][R7-43] | Environ 1,65 salarié par chambre (Louise de La Vallière) [R7-41] | Annuelle, avec un creux en hiver hors fêtes (H) | **Très fort** : flux permanent ; compatible seulement avec une séparation stricte | Environ 150 créations d'hôtels par an [R7-40] ; échecs nombreux (Brindos, La Barge, Bricquebec…) [R7-64] |
| **Gîtes et grandes maisons dans les communs** | Occupation des Gîtes de France : 44 à 47 % par an (environ 23 semaines) [R7-48][R7-50] ; 86 % en juillet-août [R7-49] ; prix moyen : ? | ? | Rénovation des communs (voir R1, R8) ; DPE de A à E exigé dans les communes à enregistrement, de A à D en 2034 [R7-52] | Ménage et accueil, sous-traitables (H) | Été très fort, ailes de saison moyennes | **Faible à moyen** si l'unité est autonome et éloignée | 4 900 meublés en Ardèche, par exemple [R7-50] ; marché très diffus |
| **Location de luxe à la semaine (Le Collectionist)** | Château de 16 chambres pour 40 personnes : 56 230 à 61 850 € par semaine ; manoirs de 6 à 8 chambres : 12 755 à 29 690 € ; mas de Provence : 6 500 à 38 650 € [R7-54][R7-55] (HT/TTC et commission non précisés) | ? Commission de la plateforme : ? | Mobilier et décoration haut de gamme, piscine, service (H) | Conciergerie et personnel de maison pendant les séjours (H) | Été (H) ; nombre de semaines vendues : ? | **Incompatible** avec la résidence privée si l'on loue le château ; compatible pour une aile ou une maison séparée | Offre sélective : 17 biens en Normandie, 12 en Dordogne, 9 dans le Bordelais [R7-54][R7-56][R7-57] |
| **Glamping, hébergements insolites** | Environ 22 000 € par module et par an (E, 2022) ; 142 € par nuit ; 1,7 nuit en moyenne [R7-58] ; 265 à 301 € par nuit en 2024 [R7-59] | ? | Par unité : ? ; permis d'aménager au-delà de 20 personnes ou de 6 hébergements [R7-62] | Ménage à chaque départ (H) | Avril à octobre, surtout le week-end (H) | **Moyen** : flux quotidiens, à isoler | 2 226 à 3 026 sites en France [R7-58][R7-59] ; forte croissance |
| **Visites** | 13,5 à 19,5 € TTC par adulte (Breteuil, Cheverny) [R7-67][R7-69] ; visite privée à 550 € HT pour 30 personnes (CMN) [R7-13] | Proche de zéro ou négative pour un château moyen (E et [R7-23]) | ERP, accessibilité, sanitaires (voir R3) : ? | 2 saisonniers ou plus (H) | Été et week-ends | **Fort** pendant les jours d'ouverture | Environ 1 500 monuments de La Demeure Historique ouverts au public, plus de 9 millions de visiteurs [R7-20] ; environ 6 000 visiteurs en moyenne par monument (E) |

**Conclusion de R7** (ESTIMATION) :

1. **Aucune activité de ce périmètre ne finance seule un domaine S2 ou S3.**
   - Les mariages et les locations nues rapportent environ 100 000 à 250 000 € de chiffre d'affaires par an, avec une marge faible.
   - Les tournages et les visites restent marginaux.

2. **Les activités qui produisent des volumes importants sont lourdes en capital et en personnel.**
   - Un château-hôtel génère plus de 1 M€ de chiffre d'affaires, mais exige 350 000 à 700 000 € d'investissement par chambre et environ 1,65 ETP par chambre.
   - Les séminaires résidentiels suivent la même logique hôtelière.
   - Ces activités sont incompatibles avec la tranquillité d'une résidence privée, sauf séparation physique stricte.

3. **Les combinaisons les plus compatibles avec un domaine équestre calme** :
   - location à la semaine de dépendances autonomes (gîtes ou grande maison) ;
   - quelques shootings et tournages ;
   - séminaires de jour en semaine ;
   - un nombre **plafonné** de mariages, par exemple 8 à 12 par an, sans feux d'artifice et loin des écuries.
   Ce sont des revenus **d'appoint**, de l'ordre de quelques centaines de milliers d'euros de chiffre d'affaires au plus, pas un moteur de financement.

4. **La concurrence est forte et documentée.**
   - 1 382 châteaux sont référencés pour les mariages.
   - Les monuments publics louent à bas prix.
   - Au moins 41 entités « château » de l'hôtellerie et de la réception ont fait l'objet d'une procédure collective depuis 2024.

---

## Contre-exemples et cas d'échec trouvés

### A. Procédures collectives de sociétés « château » de l'hôtellerie, de la réception et de l'hébergement (BODACC, 2024-2026)

Source : API open data du BODACC (DILA) [R7-64]. Statut : PAGE LUE, données officielles. Comptes tirés de l'API recherche-entreprises [R7-63].

**Comptage** :
- **41 entités distinctes** ont publié au moins une annonce de procédure collective entre le 01/01/2024 et le 14/10/2026. Critères : le nom contient « château » et le texte de l'annonce mentionne mariage, réception, hôtel, hôtes, séminaire ou hébergement.
- Ce comptage est une **borne basse** : les sociétés dont le nom ne contient pas « château » ne sont pas captées, par exemple Groupe Cœur et Détente.
- C'est aussi un comptage **brut** : il inclut des redressements et des sauvegardes qui ne sont pas des faillites définitives, et peut-être quelques domaines viticoles.

| Société (lieu, activité) | Procédure et dates | Comptes connus | Source |
|---|---|---|---|
| S.A.S. Château de Brindos (Anglet, hôtel ; SIREN 431 703 610) | Liquidation judiciaire : liste des créances publiée le 13/09/2026 | 2018 : chiffre d'affaires de 1 809 262 €, **résultat net de −869 031 €** | [R7-64], [R7-63] |
| Château de la Barge (Chaintré, hôtel-restaurant ; SIREN 450 011 820) | Liquidation judiciaire : liste des créances publiée le 07/06/2024. Sa holding a été clôturée pour insuffisance d'actif le 11/10/2024 | 2017 : chiffre d'affaires de 1 363 739 €, résultat net de −62 541 € | [R7-64], [R7-63] |
| Groupe Cœur et Détente (Ygrande, Allier, 55.10Z, 20 à 49 salariés ; « Château d'Ygrande » selon un EXTRAIT [R7-66]) | « Jugement d'ouverture de liquidation judiciaire » le 28/10/2025 ; cessation des paiements le « 01 Septembre 2025 » ; activité « Hôtels et hébergement similaire », séminaires, séjours à thème | 2022 : résultat net de −102 330 € (chiffre d'affaires publié à 0, probablement non communiqué) | [R7-64], [R7-63] |
| Château de Lucheux (Somme, acquisition, mise en valeur, exploitation, location) | Redressement judiciaire le 25/10/2024 (cessation au 25/04/2023), converti en liquidation le 20/12/2024, clôturé pour insuffisance d'actif le 19/12/2025 | — | [R7-64] |
| Rêve de Château (Barsac : chambres d'hôtes, séminaires, réceptions, mariages) | Clôture pour insuffisance d'actif le 05/01/2026 | — | [R7-64] |
| Un Passage au Château (Varennes-lès-Mâcon : restaurant, séminaires, mariages, réceptions, chambres d'hôtes) | Liquidation judiciaire : liste des créances du 22/12/2025 | — | [R7-64] |
| Château Saint-Michel et SCI homonyme (Rully, hôtel) | Liquidation judiciaire : liste des créances du 29/07/2025 | — | [R7-64] |
| Le Château de Bricquebec (Manche, hôtel) | Clôture pour insuffisance d'actif le 09/09/2024, puis liste des créances en liquidation le 02/10/2024. Données incohérentes, à vérifier | — | [R7-64] |
| Château-Hôtel Le Boisniard et Relais du Château Boisniard (Chambretaud : hôtel, restaurant, séminaires, réceptions, spa) | Dépôt de l'état des créances le 19/09/2025 | — | [R7-64] |
| Château de Collias (Gard, hôtel-restaurant) | Redressement judiciaire le 04/06/2025, cessation au 15/04/2025 | — | [R7-64] |
| Ragny le Château (Yonne : hébergement touristique, réceptions, mariages) | Redressement judiciaire le 05/10/2026, cessation au 05/04/2025 | — | [R7-64] |
| Le Château de Busset (Allier, hôtel) | Liquidation judiciaire : liste des créances du 25/01/2024 | — | [R7-64] |
| Château de Charge (Razines, Indre-et-Loire) | Liquidation judiciaire le 07/05/2024, cessation au 07/11/2022 | — | [R7-64] |
| Laetitia Bataillé Events (Var : mariages, location de salles, séminaires ; société récente) | Liquidation judiciaire le 28/07/2026, cessation au 23/07/2026 | — | [R7-65] |
| **Issues non fatales** : Château de Quinéville (Manche, hôtel) ; Château Floridis (Deauville) ; Château du Bois-Guy (chambres d'hôtes) | Quinéville : liquidation puis « clôture pour extinction du passif » le 04/11/2024. Floridis : plan de sauvegarde de 10 ans le 03/09/2025. Bois-Guy : plan de redressement le 27/06/2025 | — | [R7-64] |

**Lecture** : les échecs touchent surtout des **châteaux-hôtels et restaurants** de 1 à 2 M€ de chiffre d'affaires, en perte récurrente (Brindos, La Barge), et de petits lieux mixtes (chambres d'hôtes, réceptions, mariages). Le modèle « château + hôtellerie-restauration » n'est **pas** une garantie de pérennité.

### B. Autres contre-exemples documentés

- **Mise aux normes ERP** d'une salle de réception de 98 m² dans un monument historique : plus de 100 000 € de travaux, plus de deux ans de procédure, un propriétaire qui a « failli arrêter à plusieurs reprises » [R7-23].
- La **visite seule est déficitaire** pour un propriétaire cité par La Demeure Historique [R7-23].
- En 2017, La Demeure Historique comptait « plus de 1 000 monuments historiques […] en vente ou en manque de repreneurs » et une « durée moyenne de détention [qui] se réduit à 7 ans » [R7-23]. Ce chiffre est ancien et non actualisé.
- **Choc de 2020** : −31,2 % de mariages [R7-16] ; −69 % de chiffre d'affaires chez Châteauform' [R7-26]. Témoignage de La Demeure Historique en 2021 : des propriétaires qui « jette[nt] l'éponge » [R7-21].
- **Contraintes d'usage dans les grands sites** : « No dancing possible » dans la salle de 90 m² de Cheverny [R7-68] ; règlement de Picomtal (monument inscrit) interdisant nourriture et boissons dans les salons [R7-07]. Ce sont des limites concrètes à l'usage événementiel des intérieurs historiques.

---

## Points de doute / hypothèses non vérifiées

1. **Répartition Mariages.net** (12 % en château, 37 % en domaine) : l'échantillon de 1 304 couples utilisateurs d'une plateforme n'est pas représentatif. L'extrapolation à 251 000 mariages, soit environ 30 000 réceptions en château, est une **borne haute**.
2. **HT ou TTC** : la plupart des grilles de mariage (Picomtal, Bridebook, Mariages.net, 1001 Salles) et les prix du Collectionist ne précisent pas la TVA. Seuls le CMN, Berne, Cheverny (salles) et les fiches de séminaire sont explicites.
3. **Grilles du CMN** : ce sont des **prix planchers** (« à partir de »), et leur millésime est 2024-2025.
4. **Données MKG** : la définition de la catégorie « Haut de Gamme » n'est pas donnée dans le PDF. L'échantillon est majoritairement urbain ; les chiffres départementaux ne décrivent pas les châteaux-hôtels de campagne.
5. **Divergences conservées** :
   - taux d'occupation 2025 de 63 % ou 64 % selon les articles sur In Extenso ;
   - chiffre d'affaires 2019 de Châteauform' de 255 M€ (page lue) ou 237,6 M€ (extrait) ;
   - mariages 2024 : 247 000 (bilan provisoire) ou 248 174 (série révisée).
6. **Tranches d'effectif INSEE** (« 42 » = 1 000 à 1 999 salariés, « 12 » = 20 à 49) : correspondance de mémoire, à vérifier dans la nomenclature INSEE.
7. **API recherche-entreprises** : un chiffre d'affaires publié à « 0 » peut signifier des comptes non communiqués ou confidentiels, pas une activité nulle. Les comptes sont parfois anciens (2016-2023). L'API a été intermittente (erreurs 503).
8. **Comptage BODACC** : le filtre sur le nom (« château ») et la recherche plein texte de l'activité sont imparfaits. Le résultat de 41 entités est une **indication**, pas une statistique.
9. **Glamping** : 22 000 € par module est une moyenne calculée à partir d'une étude de 2022 à faible taux de réponse (370 sur 3 000). Le coût d'investissement par unité n'est pas trouvé.
10. **Fréquence des tournages** (0 à 6 jours par an) : HYPOTHÈSE sans source.
11. **Seuil de rentabilité des visites** : fondé sur des HYPOTHÈSES de coûts (40 000 à 60 000 €) et de recette nette (9 € HT par visiteur), à recaler avec R2 et R3.
12. **Château de Berne** : les prix de 2024 (« valid for April 2024 ») sont publiés dans un article de 2026.
13. **Prix des séminaires** de Funbooker : non datés. La fiche de La Roche-Guyon date de 2023.
14. **Restent INCONNUS** :
    - nombre de mariages de destination et budget ;
    - taille du marché des séminaires résidentiels ;
    - taux de GOP des hôtels de luxe à la campagne ;
    - loyer d'un bail hôtelier en % du chiffre d'affaires ;
    - revenu moyen d'un gîte ;
    - commission du Collectionist et semaines louées ;
    - coût d'investissement en glamping ;
    - prix de l'assurance annulation ;
    - répartition de la fréquentation des monuments historiques privés par tranche ;
    - nombre de châteaux-hôtels en France.
15. **Budget** : 16 WebSearch ont été consommées, soit une de plus que le plafond de 15 (erreur de décompte). Plusieurs pistes n'ont pas pu être creusées : Relais & Châteaux, Châteaux & Hôtels Collection, assurance annulation, conditions de Gîtes de France, commissions des plateformes.

---

## Chiffres clés pour le modèle

| # | Donnée | Valeur | Unité | Année | Statut | Source |
|---|---|---|---|---|---|---|
| 1 | Mariages célébrés en France | 251 000 (provisoire) ; 248 174 en 2024 | mariages par an | 2025 | PAGE LUE | [R7-01] |
| 2 | Choc de 2020 sur les mariages | −31,2 % ; été (juin-août) −40 % (E) | % par rapport à 2019 | 2020 | PAGE LUE | [R7-16] |
| 3 | Part des mariages de juin à septembre / le samedi | 59 % / 82 % | % | 2019 | PAGE LUE | [R7-15] |
| 4 | Budget moyen d'un mariage, hors bague et voyage | 19 293 € (215 € par invité, 90 invités) | € TTC (dépense des ménages) | 2025 (rapport 2026) | PAGE LUE | [R7-03] |
| 5 | Lieu de réception : domaine / salle / château | 37 % / 26 % / 12 % | % des couples du panel | 2025 | PAGE LUE | [R7-03] |
| 6 | Châteaux / domaines référencés sur Mariages.net | 1 382 / 3 769 | lieux | octobre 2026 | PAGE LUE | [R7-05], [R7-06] |
| 7 | Mariages par château référencé | environ 22 | mariages par an | 2025-2026 | ESTIMATION | §1.3 |
| 8 | Location d'un château pour un mariage, week-end, sans traiteur | 5 600 à 6 700 (Picomtal, 60 pers.) ; 4 000 à 9 500 (Bridebook) ; 4 000 à 10 000 et plus (générique) | € (HT/TTC non précisé) | 2026-2027 | PAGE LUE | [R7-07], [R7-09], [R7-10] |
| 9 | Privatisation hôtelière complète d'un château pour un mariage (Berne, 34 chambres) | à partir de 95 500 € TTC, plus un minimum traiteur de 36 000 € TTC | € TTC | prix d'avril 2024 | PAGE LUE | [R7-08] |
| 10 | Mariage dans un château du CMN (La Motte Tilly), week-end de 3 jours | 3 750 € HT / 4 500 € TTC (plancher) | € | 2025-2026 | PAGE LUE | [R7-13] |
| 11 | Journée d'étude / séminaire résidentiel en château | 95 à 100 € / 160 à 275 € | € HT par personne et par jour | 2023-2026 | PAGE LUE | [R7-27], [R7-28], [R7-29] |
| 12 | Châteauform' France : chiffre d'affaires et résultat net | 186,4 M€ / 3,4 M€ (1,8 %) | € | 2025 | PAGE LUE | [R7-63] |
| 13 | Tournage de fiction, monument du CMN de catégorie B / C (12 h) | long métrage 5 500 / 3 500 ; série TV 3 500 / 2 500 ; publicité 7 000 / 3 800 | € HT par jour | grille 2024 | PAGE LUE | [R7-12] |
| 14 | Prise de vue catalogue (mode, luxe), CMN catégorie B / C (8 h) | 2 000 / 1 700 | € HT par jour | grille 2024 | PAGE LUE | [R7-12] |
| 15 | Hôtellerie haut de gamme, Indre-et-Loire : occupation / prix moyen / RevPAR | 72,6 % / 140,6 € / 102,1 € | %, € HT | 2025 | PAGE LUE | [R7-38] |
| 16 | Hôtellerie haut de gamme, Gironde / Calvados : RevPAR | 146,4 € / 183,8 € | € HT | 2025 | PAGE LUE | [R7-38] |
| 17 | Coût de transformation d'un château en hôtel haut de gamme | environ 675 000 (Louise de La Vallière : 13,5 M€ pour 20 chambres) ; environ 350 000 à 540 000 (autres projets) | € par chambre | 2022-2026 | PAGE LUE / EXTRAIT | [R7-41], [R7-42], [R7-43] |
| 18 | Effectif d'un château-hôtel Relais & Châteaux de 20 chambres | 33 salariés, soit environ 1,65 par chambre | ETP | 2022 | PAGE LUE | [R7-41] |
| 19 | Contrat de gestion hôtelière : base / incentive | 2 à 4 % du chiffre d'affaires / environ 10 % du GOP (jusqu'à 15 %) | % | 2007 (référence ancienne) | PAGE LUE | [R7-45] |
| 20 | Taux d'occupation annuel des gîtes (Gîtes de France national / Ardèche) | 47 % / 44 % ; juillet-août 86 % | % | 2024-2025 | EXTRAIT / PAGE LUE | [R7-48], [R7-50], [R7-49] |
| 21 | Location de luxe d'un château de 16 chambres pour 40 personnes (Le Collectionist, Calvados) | 56 230 à 61 850 | € par semaine (HT/TTC et commission non précisés) | 2026 | PAGE LUE | [R7-54] |
| 22 | Hébergement insolite : chiffre d'affaires par module / prix par nuit / durée de séjour | environ 22 000 € (E) / 142 € / 1,7 nuit | € par an, € par nuit | 2022 | PAGE LUE et ESTIMATION | [R7-58] |
| 23 | Seuil du permis d'aménager (camping, HLL) | plus de 20 personnes ou plus de 6 hébergements | seuil | 2026 | PAGE LUE | [R7-62] |
| 24 | Prix d'entrée dans un grand château privé (Cheverny / Breteuil) | 15,5 € / 19,5 € (adulte) | € TTC implicite | 2026 | PAGE LUE | [R7-67], [R7-69] |
| 25 | Fréquentation moyenne d'un monument de La Demeure Historique ouvert au public | environ 6 000 (plus de 9 millions ÷ environ 1 500) | visiteurs par an | 2026 | ESTIMATION | [R7-20] |
| 26 | Investissement de mise aux normes ERP d'une salle de 98 m² (cas) | plus de 100 000 € | € | 2017 | PAGE LUE | [R7-23] |
| 27 | Sociétés « château » de l'hôtellerie et de la réception en procédure collective | au moins 41 entités | entités, du 01/2024 au 10/2026 | 2024-2026 | PAGE LUE (comptage par API) | [R7-64] |
| 28 | Chiffre d'affaires d'une société d'exploitation de château de réception de taille familiale | 64 000 à 600 000 € ; marge nette de 0 à 6 % (un cas à 27 %) | € par an | 2016-2023 | PAGE LUE | [R7-63] |
| 29 | Choc de 2020 sur les séminaires (Châteauform') | −69 % de chiffre d'affaires ; −65 % de séminaires | % | 2020 | PAGE LUE | [R7-26] |
