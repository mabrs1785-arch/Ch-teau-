# Château d'Ygrande : immobilier, vente, aides publiques et financement (agent Y3)

Date de travail : 14/10/2026. Domaine étudié : lieu-dit le Mont, 03160 Ygrande (Allier).
Statuts utilisés : **page lue** (URL ou fichier réellement ouvert), **extrait** (vu seulement dans un résultat de recherche), **ESTIMATION** (raisonnement explicite), **INCONNU** (non établi, avec la façon de vérifier).
Budget : 23 recherches WebSearch sur 25. Les pages ont été ouvertes avec curl et les fichiers analysés en Python (scripts dans `scripts/`, téléchargements bruts dans `dl/` et `dvf/`).
Personnes privées : aucun nom de personne physique n'est relevé ici, ni celui du gérant (cité dans les mentions légales du site et dans des pages commerciales), ni ceux des négociateurs ou des agents commerciaux.

---

## 0. Synthèse

1. **Les murs et les terres n'appartiennent pas aux sociétés liquidées.** Au 1er janvier 2025, le **GFA « DOMAINE DU MONT » (SIREN 322579483)** est propriétaire de 33 parcelles (39,66 ha) qui forment le domaine, château compris. Il l'était déjà en 2019 et en 2021 [Y3-42, Y3-44, Y3-45, page lue]. Ni la SAS Groupe Coeur et Détente ni les deux EARL ne possèdent de parcelle ou de local dans l'Allier [Y3-42, Y3-43, page lue].
2. **Deux petites parcelles bâties situées au centre du site (C1246 et C1248, 958 m²) sont sorties du GFA entre 2021 et 2025.** Aucune vente n'apparaît dans DVF. Le propriétaire actuel est INCONNU : ce n'est pas une personne morale, donc probablement une ou plusieurs personnes physiques (ESTIMATION). La surface annoncée par Barnes (397 607 m²) correspond exactement à la contenance du GFA en 2021, ces deux parcelles comprises [Y3-12, Y3-45, page lue].
3. **Le domaine est en vente par au moins quatre canaux depuis mars 2026 au plus tard.** Le prix net vendeur est d'environ **2,5 M€** : 2 500 000 € chez le notaire et chez Barnes, 2 525 000 € chez Capifrance. La SAFER affiche 2 650 000 € hors frais SAFER. Aucune baisse de prix n'est observée [Y3-08, Y3-10, Y3-12, Y3-16, page lue].
4. **Aucune annonce de vente antérieure à la liquidation (28/10/2025) n'a été trouvée.** Le premier jalon daté est le DPE, réalisé le 06/01/2026 [Y3-16, page lue].
5. **DVF 2021-2025 : aucune mutation onéreuse sur les parcelles du domaine.** Repère de prix : les terres nues de 2 ha et plus se vendent environ 3 500 €/ha à Ygrande [Y3-03, page lue].
6. **Activité actuelle sur le site** : au 14/10/2026, le site chateauygrande.fr (CGU publiées le 02/10/2026) appartient à l'EARL Écuries du Château d'Ygrande. Il présente, sous le nom commercial « Château d'Ygrande », une offre de chambres d'hôtes, de restauration légère, d'écuries et de séminaires [Y3-22, Y3-23, page lue]. La date de reprise effective de l'activité est INCONNUE.
7. **Aides publiques** : aucune aide trouvée dans le module de transparence de la Commission européenne (TAM), ni du côté de la Région, du Département, de LEADER, de Bpifrance ou du financement participatif. Le site de transparence PAC est **inaccessible**. En revanche, le registre parcellaire graphique (RPG) montre qu'environ 26,9 ha de prairies du domaine ont été **déclarés à la PAC en 2023 et en 2024** [Y3-34, page lue].

---

## 1. Annonces de vente, passées et présentes

### 1.1 Inventaire des annonces

| Canal | Référence | Prix affiché | Net vendeur ou frais | Dates connues | Statut de la source |
|---|---|---|---|---|---|
| Notaire, office CRPCEN 77041 à Souppes-sur-Loing (77), sur immobilier.notaires.fr | 77041/150, annonce 1922569 | 2 625 000 € | Émoluments de négociation de 125 000 € (4,8 %) **à la charge du vendeur**, d'où un net de 2 500 000 € (calcul). Mandat non exclusif | Créée et activée le **24/03/2026**, mise à jour le 27/08/2026, en ligne le 14/10/2026. DPE réalisé le **06/01/2026** | [Y3-15, Y3-16, page lue] |
| Belles Demeures, même annonce notariale | 260969897 (URL probable, l'attribution aux deux URL vues en extrait est incertaine) | 2 625 000 € (25 pièces, 968 m²) | INCONNU | INCONNU | [Y3-18, extrait] (page bloquée par un anti-robot). Le même prix et la même surface (« Pro ») apparaissent chez l'agrégateur Zimo [Y3-21, extrait] |
| Barnes Centre Sologne Val de Loire | APM-86277778 | 2 650 000 € | Net 2 500 000 €, honoraires de 6 % TTC à la charge de l'acquéreur | En ligne le 14/10/2026, date de mise en ligne INCONNUE | [Y3-12, Y3-13, page lue] |
| Capifrance, sur ma-propriete.fr | 340938977058 | 2 650 000 € | Net 2 525 000 €, honoraires de 4,95 % TTC à la charge de l'acquéreur, **mandat simple** | En ligne le 14/10/2026 | [Y3-08, page lue] |
| Capifrance, sur ParuVendu (même annonce, autre conseiller du réseau) | 992784942831 | 2 650 000 € | Net 2 525 000 € | Mise à jour le 14/10/2026 à 13 h 43 | [Y3-14, page lue] |
| Capifrance, site propre | 209870 | INCONNU (l'extrait affiche « 407000 », vraisemblablement la surface en m²) | INCONNU | INCONNU | [Y3-20, extrait] (page bloquée par Cloudflare) |
| SAFER Auvergne-Rhône-Alpes, service départemental de l'Allier, sur proprietes-rurales.com | **03 ET 26 YGR1** (VN31895) | **2 650 000 € HFS**, c'est-à-dire hors frais de SAFER | Frais SAFER en sus, barème non indiqué | En ligne le 14/10/2026. Le « 26 » de la référence désigne probablement l'année 2026 (ESTIMATION) | [Y3-09, Y3-10, page lue] |
| SAFER, via Green-Acres et French-Property | 03et26ygr1 | 2 650 000 € | INCONNU | INCONNU | [Y3-07, page lue] |
| Belles Demeures (annonce à 1 425 m²) | tp-14-pl-1960 (page Ygrande du site) | 2 650 000 € (24 pièces, 1 425 m²) | INCONNU | INCONNU | [Y3-17, extrait] |
| Bellespierres | 1434538 | INCONNU | INCONNU | INCONNU | [Y3-19, extrait] (accès restreint) |
| Leboncoin, Propriétés de France, Patrice Besse | aucune | aucune annonce trouvée | | | Leboncoin bloqué (403). Propriétés de France : certificat TLS non conforme, non contourné. Patrice Besse : seule une annonce bourbonnaise **non liée** a été vue (château inscrit MH de 21 ha à 695 000 €) [Y3-51, page lue] |

La synthèse est aussi disponible dans `annonces_prix_synthese.csv`.

### 1.2 Historique des prix demandés

- **Avant le 28/10/2025 (liquidation de la SAS) : aucune annonce trouvée.** Recherches web sans résultat [Y3-48, extrait]. Les archives web.archive.org sont **inaccessibles depuis cet environnement** (connexion coupée par le proxy de sortie). Seule l'API de disponibilité d'archive.org répond : elle signale un instantané de chateau-ygrande.com de 2011, sans rapport avec une vente [Y3-58, page lue]. **INCONNU** : pour vérifier, consulter web.archive.org depuis un autre réseau, sur les URL des annonces et sur proprietes-rurales.com.
- **06/01/2026** : réalisation du DPE, un préalable obligatoire à toute annonce [Y3-16, page lue].
- **24/03/2026** : mise en ligne de l'annonce notariale à **2 625 000 €**, frais compris à la charge du vendeur, soit 2 500 000 € net [Y3-16, page lue].
- **2026, date exacte INCONNUE** : annonce SAFER à **2 650 000 € HFS** [Y3-10, page lue]. Annonces Barnes à **2 650 000 € FAI** (2 500 000 € net) et Capifrance à **2 650 000 € FAI** (2 525 000 € net) [Y3-12, Y3-08, page lue].
- **27/08/2026** : mise à jour de l'annonce notariale, toujours à 2 625 000 €. Le champ « variation » de l'API vaut INCONNU, ce qui ne signale aucune baisse [Y3-15, page lue].
- **14/10/2026** : toutes les annonces sont en ligne au même niveau de prix. **Aucune baisse observée.** Aucun article de presse sur la mise en vente n'a été trouvé [Y3-49, extrait].

### 1.3 Inventaire et surfaces selon les sources

- **Annonce SAFER** [Y3-10, page lue] :
  - Château de style Directoire construit en 1835, d'environ 1 500 m² sur trois niveaux.
  - 16 chambres climatisées avec salle de bains, hall, trois salons et salles à manger, bibliothèque, cuisine professionnelle, caves.
  - Maison de jardin avec 3 chambres d'hôtel, plus une partie d'environ 115 m² comprenant 2 chambres.
  - Maison des cavaliers d'environ 130 m² et maison du personnel d'environ 130 m² (5 chambres).
  - Restaurant gastronomique et piscine chauffée de 6 × 12 m.
  - Installations équestres : 24 boxes, 6 stabulations, 3 selleries, club-house et 2 bureaux, 2 carrières, manège couvert, rond de longe, piste de galop d'environ 750 m, marcheur couvert, paddocks.
  - Bâtiment de stockage d'environ 800 m² à toiture photovoltaïque et grange d'environ 100 m².
  - Foncier : 40 ha d'un seul tenant, dont environ 27 ha de pâtures, environ 10 ha de bois et un étang d'environ 3,7 ha.
  - Surface habitable totale : 1 760 m².
  - Le bien est présenté comme « exploité depuis plus de vingt-cinq ans ».
- **Annonce Capifrance** [Y3-08, page lue] :
  - Château d'environ 1 000 m² habitables, 1 425 m² au total, 40,7 ha, 24 pièces dont 19 chambres.
  - Maison de jardin de 195 m², maison des cavaliers de 118 m², maison du personnel de 110 m² (rénovation à prévoir).
  - Carrières de 30 × 60 m et 20 × 40 m, manège de 20 × 40 m.
  - Domaine : 27 ha de pâtures, **5 ha de bois**.
  - Chauffage au gaz, DPE de 251 kWh/m²/an et 38 kg CO₂/m²/an.
- **Annonce Barnes** [Y3-12, page lue] : 19 chambres, 19 salles de bains, 1 500 m², **397 607 m²** de terrain, étang d'environ **1,7 ha**, capacité de « plus de 80 chevaux », DPE **E** et GES **D**, dépense énergétique estimée à **41 320 €/an au minimum** (référence 2023).
- **Annonce notariale** [Y3-16, page lue] : 968 m², 40 ha, 25 pièces, 19 chambres, 20 places de stationnement, état « bon », 3 étages, classe énergie **D** pour 251 kWh/m²/an, dépenses d'énergie de 40 000 à 42 000 €/an (référence 2023).
- **Cadastre** (GFA DOMAINE DU MONT, situation au 01/01/2025) [Y3-42, page lue] : 39,66 ha au total, répartis ainsi :
  - terres : 14,01 ha ;
  - prés : 14,00 ha ;
  - taillis sous futaie : 4,92 ha ;
  - terrains d'agrément : 2,79 ha ;
  - sols (bâti et cours) : 1,67 ha ;
  - **eaux : 1,38 ha** ;
  - peupleraie : 0,53 ha ;
  - jardins : 0,36 ha.
- **Bâti cadastré** (couche « bâtiments » Etalab) sur les parcelles ygrandaises du domaine : 16 bâtiments pour **environ 3 600 m² d'emprise au sol** [Y3-47, page lue].
  - Bâtiment « dur » de 527 m² sur C0093, une parcelle qui porte 4 locaux du GFA selon le fichier des locaux. C'est le candidat probable pour le château (ESTIMATION).
  - Bâtiment de 910 m² sur C0095/C0096, peut-être le manège ou le hangar photovoltaïque (ESTIMATION).
  - Bâtiment léger de 589 m² sur C1246 et bâtiment léger de 132 m² sur C1248.
  - Certains bâtiments récents peuvent ne pas être dessinés au cadastre, et la partie située sur Saint-Aubin-le-Monial n'a pas été analysée.

### 1.4 La SAFER : rôle, conditions et statut

- Rôle affiché : « La Safer Auvergne Rhône-Alpes **accompagne la cession** de cette propriété rurale à vocation d'accueil et d'hébergement touristique ». Le prix est donné « **HFS** », c'est-à-dire hors frais de SAFER. Contact : service départemental de l'Allier (SD03). L'annonce mentionne aussi la possibilité d'« accompagner le porteur de projet dans la recherche d'un **agriculteur partenaire** » pour l'entretien des terres [Y3-10, page lue].
- Conditions générales des SAFER [Y3-11, page lue] :
  - l'attribution se fait par rétrocession ou par substitution, après avis du comité technique départemental et approbation des commissaires du Gouvernement ;
  - l'attribution peut être assortie d'un **cahier des charges**, d'au moins 10 ans en cas d'exonération des droits d'enregistrement ;
  - des frais SAFER s'ajoutent, selon un barème fixé par le conseil d'administration.
- **Appel à candidatures, cahier des charges propre à ce bien et date limite : non trouvés.**
  - Les pages « appels à candidatures » et « annonces légales » de safer-aura.fr chargent leur contenu depuis `iframe-annonces-legales.safer.fr/ara`, qui est **inaccessible** depuis cet environnement (connexion réinitialisée) [Y3-24, page lue].
  - Aucune recherche web n'a trouvé d'avis concernant Ygrande [Y3-54, extrait].
- **La SAFER est-elle propriétaire ?** Non au 01/01/2025 : aucun droit de la SAFER n'apparaît sur les parcelles dans le fichier DGFiP des personnes morales [Y3-42, page lue]. DVF ne montre aucune vente en 2025 [Y3-03, page lue]. Les mentions « accompagne la cession » et « HFS », ainsi que l'annonce notariale dont les frais sont payés par le vendeur, plaident pour une **intermédiation** (promesse avec faculté de substitution ou mandat), sans achat ni préemption (ESTIMATION). L'état en 2026 est **INCONNU** et se vérifie au service de publicité foncière (voir § 5).
- La SAFER AuRA tiendra un stand au salon EQUITA Lyon du 28/10 au 01/11/2026 [Y3-24, page lue]. Rien ne relie explicitement ce stand à ce bien.

### 1.5 Ventes aux enchères et liquidateur

- **Licitor** : la page Auvergne des prochaines ventes ne liste qu'une vente dans l'Allier, un immeuble à Montluçon. L'historique donne accès à 33 annonces distinctes, dont 12 dans l'Allier. Aucune ne concerne Ygrande ni un château de l'Allier. La couverture de l'historique est partielle, car la pagination n'a pas répondu [Y3-25, page lue].
- **Avoventes** : 231 ventes listées, aucune à Ygrande [Y3-26, page lue].
- **encheres-publiques.com** : **inaccessible** (Cloudflare) [Y3-27, page lue].
- **Tribunaux de Moulins, Cusset et Montluçon** : aucune liste de ventes trouvée [Y3-57, extrait].
- **Liquidateur de la SAS** : « SELARL MJ de l'Allier », d'après une page Doctrine reprenant le BODACC [Y3-28, extrait], à confirmer par le directeur. La plateforme de cession d'actifs des AJ/MJ (actify.fr) est **inaccessible** (Cloudflare) [Y3-52, page lue]. Aucune annonce de cession du fonds ou des actifs n'a été trouvée [Y3-28, extrait].
- ESTIMATION : la SAS n'étant pas propriétaire de l'immobilier (§ 2), le liquidateur ne peut vendre que les actifs de la SAS (fonds de commerce, mobilier, matériel), pas les murs. Une vente judiciaire de l'immeuble supposerait une procédure visant le propriétaire, ou une saisie immobilière par un créancier titulaire d'une sûreté sur le bien. Ni l'une ni l'autre n'est observée.

### 1.6 Statut actuel

- **Le bien est en vente**, sans indice de mention « sous offre » ou « vendu » sur les pages lues au 14/10/2026 [Y3-08, Y3-10, Y3-12, Y3-14, Y3-16, page lue].
  - Le champ `bienRetire = OUI` de l'API des notaires contredit `statut = LIGNE`. Ce champ semble propre aux ventes aux enchères. Sens INCONNU.
- **Le site est exploité.** Le site web chateauygrande.fr (chateau-ygrande.com y redirige) appartient à l'**EARL Écuries du Château d'Ygrande**, d'après ses mentions légales [Y3-22, Y3-23, page lue] :
  - SIRET 82073287300014, capital de 7 500 €, NAF 8551Z, RCS Cusset, nom commercial « Château d'Ygrande » ;
  - conditions générales « publiées le 02/10/2026 » ;
  - activité : « chambres d'hôtes de luxe » de 18 à 37 m², restauration légère, hammam, piscine, écuries de **26 boxes**, séminaires (bibliothèque de 70 m², salons jusqu'à 50 personnes) ;
  - pas de réservation en ligne.
- Le titre d'occupation de l'EARL (bail rural, commercial, commodat…) est **INCONNU**.
- Un extrait mapstr indique que « Le Haras du Château d'Ygrande devient Les Écuries du Château d'Ygrande » [Y3-50, extrait].

---

## 2. Qui possède les murs et les terres

### 2.1 Le propriétaire principal : GFA « DOMAINE DU MONT »

Le **fichier DGFiP des parcelles des personnes morales** (MAJIC, « situation au 1er janvier de l'année » selon le descriptif [Y3-46, page lue]) a été lu pour trois millésimes [Y3-42, Y3-44, Y3-45, page lue] :

| Situation au | Désignation | Parcelles | Contenance |
|---|---|---|---|
| 01/01/2019 | « GFA DOMAINE DU MONT », forme SC, SIREN vide | 32 | 397 577 m² |
| 01/01/2021 | GFA « DOMAINE DU MONT », SIREN **322579483** | 35 | **397 607 m²** |
| 01/01/2025 | GFA « DOMAINE DU MONT », SIREN 322579483 | 33 | 396 649 m² |

- Lieux-dits : Ygrande (section C : « Le Château du Mont », « Popinière », « La Bacharde ») et Saint-Aubin-le-Monial (section B : « La Chaume »).
- Code droit : P, c'est-à-dire propriétaire, sur toutes les lignes.
- La parcelle **C1245 « Le Château du Mont »** (5 400 m², sols), où se trouve le point BAN « Le Château du Mont » [Y3-05, Y3-06, page lue], appartient au GFA.
- **Locaux** au 01/01/2025 : le GFA est propriétaire de 6 locaux, 4 sur C0093, 1 sur C1245 et 1 sur C1249. Aucun autre titulaire de droits, par exemple un preneur à bail à construction pour du photovoltaïque, n'apparaît [Y3-43, page lue].
- La liste détaillée des parcelles figure dans `ppm_gfa_domaine_du_mont_parcelles_2019_2021_2025.csv`.
- Une recherche web sur « GFA Domaine du Mont » n'a rien donné [Y3-56, extrait].
- **À vérifier par le directeur au registre** : statut, associés, gérance et procédure collective éventuelle du GFA (SIREN 322579483).

### 2.2 Les parcelles C1246 et C1248 sorties du GFA entre 2021 et 2025

- Entre le 01/01/2019 et le 01/01/2021, les parcelles C0079 (6 080 m²) et C0080 (7 165 m²) sont remplacées par C1245 à C1249, toutes au GFA en 2021 [Y3-44, Y3-45, page lue].
- Au 01/01/2025, **C1246 (671 m²) et C1248 (287 m²) ne sont plus détenues par aucune personne morale** [Y3-42, page lue].
- Le cadastre Etalab y montre un **bâtiment léger d'environ 589 m² au sol** sur C1246 et un bâtiment léger d'environ 132 m² sur C1248 [Y3-47, page lue].
- **Aucune mutation DVF 2021-2025** ne concerne ces parcelles [Y3-03, page lue].
- ESTIMATION : il s'agit d'une sortie hors vente onéreuse (donation, partage, apport à une personne physique…) ou d'un acte non repris dans DVF, au profit probable d'une ou plusieurs personnes physiques.
- Barnes annonce 397 607 m², soit la surface du GFA en 2021, C1246 et C1248 comprises. L'offre semble donc englober ces deux parcelles, et la vente pourrait impliquer **au moins deux propriétaires** (ESTIMATION).
- Identité du propriétaire actuel : **INCONNU** (voir § 5 pour la démarche).

### 2.3 Les sociétés liquidées et la SAFER

- La SAS GROUPE COEUR ET DETENTE (421318247), l'EARL Haras d'Ygrande (447907064) et l'EARL Écuries du Château (820732873) n'apparaissent **sur aucune parcelle ni sur aucun local de l'Allier** dans les fichiers des personnes morales de 2025 [Y3-42, Y3-43, page lue].
- ESTIMATION : l'hôtel liquidé occupait l'immobilier du GFA au titre d'un bail ou d'une mise à disposition. Le contrat est INCONNU.
- SAFER : voir § 1.4. Elle n'est pas propriétaire au 01/01/2025.
- Une page commerciale de réservation (Teritoria ou une reprise de sa fiche ; la page exacte est incertaine) présente le gérant comme « propriétaire » [Y3-53, extrait]. Cette mention est non fiable et contredite par le cadastre, qui désigne un GFA.

### 2.4 Autres sociétés repérées, à vérifier par le directeur

| Société | SIREN | Constat | Lien avec le domaine |
|---|---|---|---|
| **GFA DOMAINE DU MONT** | **322579483** | Propriétaire du domaine en 2019, 2021 et 2025 | **Lien direct** |
| SELARL MJ de l'Allier | inconnu | Liquidateur de la SAS [Y3-28, extrait] | Lien procédural |
| GFA DE LA BACHARDE | 326793619 | Propriétaire de parcelles voisines (La Bacharde, Les Rouches) | Aucun lien établi |
| GFA DU PRESSOIR | 399674431 | Propriétaire de parcelles voisines (Popinière, Le Pressoir) | Aucun lien établi |
| SCI YGRANDE | 930427869 | 4 petites parcelles au bourg (rue Émile Guillaumin, rue Charles Madet, Beauregard ; 797 m²) | Aucun lien établi |

Aucune SCI ni holding liée au château n'a été trouvée par recherche web [Y3-55, extrait].

---

## 3. DVF (demandes de valeurs foncières)

- **Code INSEE d'Ygrande : 03320** (code postal 03160, 762 habitants, 5 329,57 ha) [Y3-01, page lue].
- Années disponibles dans geo-dvf « latest » : **2021 à 2025** [Y3-02, page lue]. Les fichiers 03320 de 2021 à 2025 ont été téléchargés [Y3-03, page lue], ainsi que ceux des deux communes voisines touchées par le domaine ou proches, Saint-Aubin-le-Monial (03218) et Bourbon-l'Archambault (03036) [Y3-04, page lue]. La dernière mutation d'Ygrande est datée du 24/12/2025.
- **Ygrande : 466 lignes, 106 mutations, toutes de nature « Vente »** : 31 en 2021, 18 en 2022, 14 en 2023, 26 en 2024 et 17 en 2025.
- **Aucune mutation au lieu-dit le Mont.** Aucune voie DVF ne contient « MONT ». Croisement par identifiant de parcelle avec les 338 parcelles cadastrales d'une boîte d'environ 2 km × 2 km autour du château (API Carto IGN [Y3-06, page lue]) : **aucune mutation sur une parcelle d'Ygrande de la section C du secteur, ni sur aucune des 35 parcelles du GFA**, y compris C1246 et C1248. Les seules mutations dans la boîte concernent des maisons et des prés de Saint-Aubin-le-Monial (La Chaume, Monchereux), non liés au domaine [Y3-03, Y3-04, page lue].
- **Mutation la plus proche à Ygrande** : 23/01/2025, 11 420 € pour 2,85 ha de prés à La Rouche, à 1,4 km [Y3-03, page lue].
- **Plus grosses mutations d'Ygrande**, toutes à plus de 2 km et non liées au domaine [Y3-03, page lue] :
  - 650 000 € le 15/05/2021 : 7,75 ha de terres sans local à La Feurtrie et au Grand Villier, soit environ 84 000 €/ha, une valeur atypique ;
  - 472 200 € le 25/11/2022 : 2 maisons et 3,8 ha aux Chaumes ;
  - 427 060 € le 21/11/2025 : 2 maisons et 9,6 ha à Coupied ;
  - 350 000 € le 13/09/2024 : 9,9 ha et du bâti au Fayard et à La Maillerie.
- **Repère de prix des terres** : pour les terres nues de 2 ha et plus (18 mutations, hors valeur atypique), la médiane est de **3 500 €/ha** (Q1 3 391 €, Q3 3 927 €) [Y3-03, page lue]. ESTIMATION : au prix agricole, les quelque 37 ha non bâtis du domaine vaudraient de l'ordre de 130 000 €. L'essentiel des 2,5 M€ demandés porte donc sur le bâti et l'activité.
- **Ce que DVF couvre** : les mutations à titre onéreux publiées au service de publicité foncière (vente, VEFA, vente de terrain à bâtir, adjudication, échange, expropriation), avec la valeur, la date, les parcelles, la nature de culture et les surfaces, sur les 5 dernières années (ici du 01/01/2021 au 31/12/2025). La France entière est couverte, sauf l'Alsace-Moselle et Mayotte.
- **Ce que DVF ne couvre pas** :
  - le nom des parties ;
  - les donations, successions, partages et apports ;
  - les **cessions de parts de société** (parts du GFA ou d'une SCI) ;
  - les baux, hypothèques et privilèges ;
  - les mutations antérieures à 2021 dans geo-dvf (l'achat initial du domaine est hors champ) ;
  - les ventes de 2026.
- **Fichiers produits** :
  - `dvf_ygrande_mutations_resume_2021_2025.csv` : les 106 mutations ;
  - `dvf_rayon_2_5km_chateau_ygrande_et_voisins.csv` : 36 mutations dans un rayon de 2,5 km ;
  - `dvf_ygrande_lignes_secteur_le_mont.csv` ;
  - `dvf_ygrande_terres_nues_2ha_prix_ha_2021_2025.csv` ;
  - `dvf_ygrande_mutations_150k_et_plus_2021_2025.csv` ;
  - en complément : `ppm_2025_personnes_morales_parcelles_autour_chateau.csv`, `ppm_2025_personnes_morales_locaux_autour_chateau.csv`, `ppm_gfa_domaine_du_mont_parcelles_2019_2021_2025.csv` et `cadastre_batiments_domaine_ygrande.csv`.

---

## 4. Aides publiques et financement

| Piste | Résultat | Détail |
|---|---|---|
| (a) TAM de la Commission européenne, aides d'État de plus de 100 000 € (dont COVID) | **Non trouvé** | Recherches pour la France par SIREN (421318247, 447907064, 820732873) et par nom (« COEUR ET DETENTE », « GROUPE COEUR », « YGRANDE ») : « Aucun résultat trouvé ». Contrôle positif réussi : le nom « AIR FRANCE » et le SIREN 420495178 renvoient bien des résultats [Y3-29, page lue]. Le seuil de publication est en général de 100 000 € par aide. Les versements mensuels du fonds de solidarité restent en dessous de ce seuil (ESTIMATION). |
| (a') Fonds de solidarité par entreprise | **Non consultable** | Le jeu Etalab ne publie que des agrégats par région ou département, croisés avec le code NAF, la forme juridique ou l'effectif [Y3-30, page lue]. |
| (b) Aides PAC des EARL (site de transparence) | **Inaccessible** | Le lien officiel donné par la Commission [Y3-32, page lue] mène à agriculture.gouv.fr, qui renvoyait une page « momentanément indisponible » (503) lors de 3 essais le 14/10/2026. Les URL telepac redirigent vers la page de connexion [Y3-31, Y3-33, page lue]. Un agrégateur (farmsubsidy.org) renvoie une erreur 404. Indice indirect : selon le **RPG 2023 et 2024**, 2 parcelles PAC de prairie permanente (PPH), soit **26,9 ha**, ont leur centre sur les parcelles ygrandaises du domaine. Ces terres ont donc été déclarées à la PAC les deux années [Y3-34, page lue]. Le RPG ne donne pas l'identité du déclarant (probablement l'EARL, ESTIMATION) ni les montants (INCONNU). Une recherche web ciblée n'a rien donné [Y3-36, extrait]. |
| (c) Région Auvergne-Rhône-Alpes | **Non trouvé** | Le catalogue data.gouv de la Région compte 2 048 jeux de données : 2 031 portent sur les marchés publics (« données essentielles »), les autres sur les transports et la loi AGEC. Il ne contient **aucun jeu sur les subventions** [Y3-38, page lue]. Les délibérations de la commission permanente sont publiées séance par séance sur edelib et n'ont pas été fouillées en plein texte. Les recherches web sur « Coeur et Détente » et sur « Château d'Ygrande » croisés avec subvention, Région, LEADER, FEADER ou Bpifrance n'ont rien donné [Y3-39, extrait]. |
| (c) Département de l'Allier, commission permanente | **Non trouvé** | Recherche web restreinte à allier.fr, auvergnerhonealpes.fr et aux sites de tourisme : seules des fiches de dispositifs génériques et des fiches touristiques des écuries et du restaurant sont ressorties [Y3-39, extrait]. |
| (c) LEADER | **Non trouvé** | Il existe un GAL « Auvergne-Rhône-Alpes des Terroirs Bourbonnais » pour 2023-2027 [Y3-40, page lue], mais l'appartenance d'Ygrande à son périmètre n'est pas vérifiée. Aucun projet LEADER lié au château n'a été trouvé. Les bénéficiaires FEADER figurent normalement sur le site de transparence PAC, inaccessible ici. |
| (c) Bpifrance | **Non trouvé** | Bpifrance ne publie pas de liste de bénéficiaires. Aucune mention n'a été trouvée [Y3-39, extrait]. |
| (d) Ulule | **Non trouvé** | L'API renvoie 0 projet pour « ygrande », contre 137 pour « haras » en contrôle [Y3-35, page lue]. |
| (d) Miimosa, KissKissBankBank | **Non trouvé** | Leurs recherches internes fonctionnent en JavaScript et ne sont pas exploitables, aucune conclusion n'en est tirée [Y3-35, page lue]. Une recherche web restreinte à ces domaines n'a rien donné [Y3-37, extrait]. |
| (d) Dartagnans, WiSEED, Tudigo, Lendosphere, Bluebees, Anaxago, Enerfip, Lita | **Non trouvé** | Recherche web restreinte à ces domaines [Y3-37, extrait]. |
| (d) HelloAsso | **Inaccessible** | Bloqué par Cloudflare. |
| Photovoltaïque (registre national ODRÉ) | **Non concluant** | 28 lignes « solaire » à Ygrande. Aucune n'est nommée « Mont » ou « Château », et plusieurs sont « Confidentiel » [Y3-41, page lue]. Le propriétaire de la toiture photovoltaïque et le contrat d'achat de l'électricité sont INCONNUS. Le fichier des locaux 2025 ne montre aucun tiers titulaire d'un droit sur les locaux du GFA [Y3-43, page lue]. |

ESTIMATION sur le financement :

- Le montage reposait sur une séparation entre un **GFA propriétaire**, une **SAS d'exploitation hôtelière** et des **EARL équestres**. Ce schéma est classique pour isoler le foncier, notamment pour la transmission, car les parts de GFA dont les terres sont louées par bail à long terme bénéficient d'avantages fiscaux.
- Les dettes de la SAS (taux d'endettement de 439 % à 1 482 % selon les ratios déjà établis) ne grèvent donc pas directement le foncier, sauf garanties consenties par le GFA, comme une hypothèque ou une caution réelle. Leur existence est INCONNUE et se vérifie au service de publicité foncière.

---

## 5. Ce qui n'est pas consultable gratuitement, et comment l'obtenir

Aucune de ces démarches n'a été lancée.

1. **Hypothèques, privilèges, servitudes, baux de plus de 12 ans** (bail rural à long terme, bail ou servitude photovoltaïque), **titre de propriété du GFA** et **acte de sortie de C1246 et C1248** :
   - déposer une demande de renseignements « hors formalité » au **service de publicité foncière compétent pour Ygrande et Saint-Aubin-le-Monial** (Allier), avec le formulaire **3233-SD** ; une copie d'acte se demande avec le formulaire 3236-SD ;
   - parcelles à viser : Ygrande C0051, C0077, C0078, C0081 à C0086, C0088 à C0097, C0230, C0839, C0841, C1245 à C1249 ; Saint-Aubin-le-Monial B0030, B0051 à B0055, B0959, B1014 ;
   - le service est **payant** (contribution de sécurité immobilière, article 881 S du CGI) et la demande peut se faire en ligne ou par courrier.
2. **Identité du propriétaire de C1246 et C1248**, probablement une personne physique : demander un relevé de propriété au centre des finances publiques (service foncier ou cadastre), au titre de l'article L107 A du LPF (communication ponctuelle et limitée), ou par la fiche immeuble du point 1.
3. **Statuts, associés et gérance du GFA (SIREN 322579483)** : consulter le RNE ou l'INPI (vérification par le directeur). Un GFA est une société civile qui **ne dépose pas ses comptes**, qui ne sont donc pas publics.
4. **Comptes détaillés de la SAS** : comptes confidentiels, seuls les ratios INPI sont disponibles. Pour la liquidation :
   - l'**état des créances** est déposé au greffe du tribunal de commerce de Cusset et consultable par tout intéressé (article R624-8 du code de commerce). Il permettrait d'identifier les **PGE** et les prêts bancaires, l'URSSAF, la DGFiP et les fournisseurs ;
   - les ordonnances du juge-commissaire relatives à la cession des actifs mobiliers ou du fonds sont au même greffe ;
   - les rapports du liquidateur ne sont pas publics.
5. **PGE et aides COVID par entreprise** : il n'existe pas de liste publique (secret fiscal et bancaire), en dehors du TAM au-delà de 100 000 €. Voie possible : l'état des créances (point 4).
6. **Montants PAC** : réessayer le site de transparence (lien sur la page « beneficiaries » de la Commission européenne). Les données publiées couvrent les deux dernières années seulement. À défaut, les comptes des EARL, qui ne sont en principe pas déposés.
7. **SAFER** : appel à candidatures, cahier des charges, prix et frais. Ces informations relèvent de la publicité légale (affichage en mairie à Ygrande et Saint-Aubin-le-Monial, iframe des annonces légales SAFER). Réessayer `iframe-annonces-legales.safer.fr/ara` depuis un autre réseau. Le contact direct avec la SAFER est exclu par les consignes.
8. **Archives des annonces (web.archive.org)** : réessayer depuis un autre réseau. Archives Leboncoin : non accessibles.
9. **DVF antérieures à 2021** : absentes de geo-dvf. Pour 2014-2020, le DVF+ open data du Cerema (non téléchargé ici). Avant 2014, uniquement le fichier immobilier du service de publicité foncière (point 1).

---

## 6. Contradictions, doutes et inconnues

**Contradictions entre sources**

- **Prix net vendeur** : 2 500 000 € (notaire [Y3-16] et Barnes [Y3-12]), 2 525 000 € (Capifrance [Y3-08]) et 2 650 000 € hors frais SAFER (SAFER [Y3-10]). Le net est-il identique pour la SAFER ? INCONNU.
- **Surface bâtie** : 968 m² (notaire), « environ 1 000 m² » pour le château (Capifrance), 1 425 m² (Capifrance), 1 500 m² (Barnes et SAFER pour le château), 1 760 m² habitables au total (SAFER).
- **Surface du terrain** : 39,66 ha au cadastre du GFA en 2025 [Y3-42], 39,76 ha en 2021 (identique au chiffre Barnes), 40 ha (SAFER, notaire), 40,7 ha (Capifrance). Les 0,9 ha d'écart avec Capifrance sont inexpliqués.
- **Bois** : 10 ha selon la SAFER, 5 ha selon Capifrance, 5,45 ha au cadastre (4,92 ha de taillis et 0,53 ha de peupleraie).
- **Étang** : 3,7 ha selon la SAFER, environ 1,7 ha selon Barnes, 1,38 ha de « eaux » au cadastre. Les natures cadastrales peuvent être anciennes.
- **Boxes** : 24 dans les annonces, 26 sur le site de l'EARL [Y3-22].
- **Classe DPE** : E selon Barnes, D selon l'API des notaires, pour la même consommation de 251 kWh/m²/an. Avec la méthode 2021, 251 kWh/m²/an relève de la classe E (ESTIMATION).
- **Annonce notariale** : `statut = LIGNE` mais `bienRetire = OUI`.
- **Belles Demeures** : l'attribution des deux annonces (2 625 000 € et 968 m² ; 2 650 000 € et 1 425 m²) à leurs URL respectives est incertaine (extraits seulement).
- **Numéro de TVA** affiché sur le site de l'EARL (FR048207322873) : il compte un chiffre de trop par rapport à la forme attendue, FR + clé + SIREN 820732873.
- **Date de construction** : 1835 dans les annonces, 1876 selon une page de réservation (extrait vu en recherche). Hors du périmètre de Y3, signalé à Y1.

**Doutes**

- **C1246 et C1248** : ces parcelles bâties appartenaient au GFA en 2021 et à aucune personne morale en 2025, sans vente dans DVF. La nature de l'acte, sa date et le bénéficiaire sont **INCONNUS**. On ne sait pas non plus si elles font partie de la vente (indice : la surface Barnes).
- L'interprétation « la SAFER intermédiaire et non propriétaire » est une ESTIMATION fondée sur la mention HFS, la formule « accompagne la cession », l'absence de droits SAFER au 01/01/2025 et l'absence de vente DVF en 2025.
- L'identification du bâtiment du château (527 m² au sol sur C0093) est une ESTIMATION.

**Inconnues**

- **Mise en vente avant la liquidation** : INCONNU. Aucune annonce trouvée et archives inaccessibles. Le premier jalon daté est le 06/01/2026 (DPE).
- Statut et associés du GFA DOMAINE DU MONT, et procédure collective éventuelle : à vérifier par le directeur.
- Sûretés sur le foncier (hypothèques, privilèges), baux en cours (bail rural de l'EARL ? droit de préemption du preneur en place, prioritaire sur la SAFER ?) et contrat photovoltaïque : INCONNUS, à vérifier au service de publicité foncière.
- Le prix comprend-il le mobilier, le matériel ou le fonds, dont certains éléments appartiennent peut-être à la SAS liquidée et relèvent alors du liquidateur ? INCONNU.
- Montants PAC (site inaccessible), aides COVID et PGE de la SAS (non publics) : INCONNUS.
- Rattachement d'Ygrande à un GAL LEADER pour 2014-2020 et 2023-2027 : non vérifié.
- Couverture partielle : Licitor (historique non paginé), Belles Demeures, Bellespierres, Capifrance, Leboncoin, encheres-publiques, Actify et HelloAsso sont bloqués par des protections anti-robot. Aucun contournement n'a été tenté.
