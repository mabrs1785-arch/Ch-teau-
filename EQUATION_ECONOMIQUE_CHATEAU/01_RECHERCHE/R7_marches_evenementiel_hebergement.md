# R7 — Marchés de l'événementiel, de l'hébergement, des tournages et des visites

Agent : R7. Date de consultation des sources : 2026-10-14. Rédaction en cours (fichier écrit au fur et à mesure).

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
- La page bordelaise de 1001 Salles, qui annonçait un week-end privatisé à 25 000-45 000 € avec hébergement et restauration (EXTRAIT de la recherche), n'a pas pu être ouverte (erreur 522). Ce chiffre reste un EXTRAIT, de fiabilité faible.

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

---

## 7. Visites (première partie : fréquentation et contexte)

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

