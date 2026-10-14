# Y2 — Château d'Ygrande : offre, prix et fonctionnement

Recherche du 14/10/2026, agent Y2. Statuts : **PAGE LUE** (URL ouverte avec curl), **EXTRAIT** (vu seulement dans un résultat de recherche), **ESTIMATION** (raisonnement explicite), **INCONNU**. Les identifiants renvoient à `sources.csv`.

## 0. Méthode et limites

- 15 recherches WebSearch utilisées sur les 25 autorisées. Pages ouvertes avec curl, texte extrait par un script Python (`python3 -I`).
- **web.archive.org est resté inaccessible pendant toute la session** : la connexion TLS est coupée juste après le ClientHello (« connection reset », environ 15 essais entre 20h00 et 20h30 UTC). L'API de disponibilité d'archive.org répondait et confirme l'existence de captures, mais je n'ai pu lire **aucun contenu archivé** du site [Y2-40, page lue, métadonnées seulement]. Les prix saisonniers de l'époque hôtelière restent donc INCONNUS à partir du site officiel, et je les ai reconstitués avec des sources tierces.
- Pages bloquées, notées sans contournement : Booking (défi anti-robot, code 202), TripAdvisor (403), Petit Futé (403), lastminute (403), Bridebook (403), gites.fr (403), Foodle (403), GreenGo (429), Aleou (429), Expedia TH (429), Facebook (connexion obligatoire), IFCE Info chevaux (anti-robot Incapsula), Common Crawl (connexion coupée).

## 1. Site officiel et versions archivées

### 1.1 Domaine et éditeur actuel

- Le domaine officiel est **www.chateauygrande.fr**. Gault&Millau y renvoie (`/fr/chambres-hotel-4-etoiles-auvergne`), Atout France aussi (`/fr/hotel-charme-auvergne`) [Y2-18, page lue] [Y2-17, page lue]. Le site des écuries est **www.ecuriesduchateaudygrande.com** [Y2-01, page lue].
- Le site actuel (WordPress, réalisé par Diadao, hébergé chez o2switch) a été refondu récemment. Les dates de mise à jour (lastmod) du sitemap vont du 22/09/2026 au 07/10/2026 [Y2-04, page lue].
- **Éditeur actuel** : selon les CGU, le site est « la propriété de la société EARL Écuries du Château d'Ygrande ». Les CGU donnent le SIRET 820 732 873 00014, le RCS Cusset 820732873 et un capital de 7 500 €. Le responsable de la publication est Pierre-Marie Tissier, « en qualité de Gérant » [Y2-02, page lue]. C'est donc l'EARL créée en 2016, et non la SAS liquidée, qui publie en 2026 le site du château.
- Les données structurées de la page d'accueil déclarent le type schema.org **BedAndBreakfast**, avec la description « Chambre d'hôtes de luxe au Château d'Ygrande » [Y2-01, page lue].
- Selon les CGU, le site « ne propose ni réservation ni paiement en ligne ». Les demandes passent par formulaire ou par e-mail [Y2-02, page lue]. Le site des écuries mentionnait encore le moteur de réservation ReservIt pour « les services de réservation en ligne » [Y2-14, page lue].

### 1.2 Offre affichée en 2026 (après la liquidation de l'exploitant hôtelier)

- **Six types de chambres**, avec des prix « à partir de » [Y2-01, page lue] :
  - Chambre Pavillon : 18 m², 1 à 2 personnes, 90 €. Plain-pied, accessible PMR, accès direct aux écuries, animaux admis.
  - Chambre Classique : 22 m², 1 à 3 personnes, 110 €. Côté nord, vue sur les pistes d'entraînement.
  - Chambre Confort : 26 m², 1 à 3 personnes, 130 €. Côté sud.
  - Chambre Supérieure : 27 m², 1 à 3 personnes, 150 €.
  - Suite Familiale : 37 m², 1 à 4 personnes, 180 €. Suite unique.
  - Suite de Luxe : 35 m², 1 à 3 personnes, 190 €. Suite unique avec cheminée.
- Le nombre de chambres par type n'est pas publié. Les chambres sont « réparties entre le château et le pavillon de jardin » [Y2-01, page lue].
- **Restauration** : « Le Château d'Ygrande ne propose pas de restaurant ». Le petit-déjeuner est servi chaque matin. Le soir, « La petite table du Château » propose des planches de charcuterie et de fromages et des soupes du potager, sur réservation au moins 24 h à l'avance, au prix de **20 € pour 2 personnes** pour la planche apéritive. Un coin cuisine est à la disposition des hôtes. Il n'y a pas de bar, mais des boissons en libre accès [Y2-01, page lue] [Y2-03, page lue].
- **Forfaits** [Y2-01, page lue] :
  - « Séjour équestre » à **126 € par personne**, avec 2 h d'équitation par jour en cours particulier ou petit groupe. L'unité (par jour ou par nuit) n'est pas précisée.
  - « Restez une nuit de plus » : 20 € de moins par nuit dès 2 nuits. La vignette affiche « 70 EUR / 2 pers. », un chiffre ambigu.
  - « Partez en vacances avec votre cheval » : sans prix sur la page d'accueil. La FAQ indique la location d'un box **30 € par jour** et un coaching possible sur réservation [Y2-03, page lue].
- **Services** : navette depuis la gare de Moulins (30 km) pour **60 €** [Y2-03, page lue].
- **Bien-être et loisirs** : hammam, **piscine chauffée ouverte de juin à septembre**, massages sur réservation, salons, bibliothèque, billard, système Sonos. Les 40 ha comprennent un bois, des pâtures, un étang, un potager, un verger et un poulailler [Y2-01, page lue].
- **Séminaires** : la Bibliothèque fait 70 m² (six fenêtres, triple exposition). Le site renvoie à une demande de devis, sans prix affiché [Y2-01, page lue].
- **Réceptions** : les salons en enfilade accueillent « jusqu'à 50 personnes assises ». Le domaine peut être entièrement privatisé, avec la piscine en saison et un barnum possible sur l'esplanade sud. Les repas sont confiés à des traiteurs partenaires. Un team building autour du cheval est possible avec un prestataire. Les types d'événements proposés dans le formulaire sont « Séminaires, Journées d'étude, Mariages, Privatisation de l'hôtel, Réunions » [Y2-01, page lue].
- **Écuries** (description du site du château) : 26 boxes, manège couvert, deux carrières en micro-sable, paddocks, chemins. Les écuries proposent baptêmes, cours particuliers ou en groupes de 6 au maximum, stages, petites randonnées et baignades à cheval dans l'étang. L'équipe est présentée comme « expérimentée en CSO, Hunter et dressage » [Y2-01, page lue] [Y2-05, page lue].

### 1.3 Versions archivées (web.archive.org)

Captures confirmées par l'API de disponibilité d'archive.org [Y2-40, page lue, métadonnées seulement] :

| Capture | URL archivée |
|---|---|
| 17/12/2009 | http://www.chateauygrande.fr/ |
| 10/03/2015 | http://www.chateauygrande.fr/ |
| 15/05/2017 | /fr/hotel-4-etoiles-auvergne |
| 06/07/2017 | /fr/hotel-charme-auvergne |
| 08/12/2022 | https://www.chateauygrande.fr/fr/hotel-charme-auvergne |
| 01/02/2023 | https://www.chateauygrande.fr/fr/chambres-hotel-4-etoiles-auvergne |

Le contenu de ces captures est INCONNU, car web.archive.org était inaccessible. Pour vérifier, il faut ouvrir à la main, depuis un autre réseau, `https://web.archive.org/web/2017*/chateauygrande.fr*` et `https://web.archive.org/web/2019*/chateauygrande.fr*`, puis relever la grille tarifaire, les menus et la page séminaires.

### 1.4 Offre de l'époque hôtelière (1998 à 2025), d'après des sources tierces

- **2003** (fiche LesRestos « mise à jour le 06/09/2003 ») [Y2-20, page lue] :
  - Hôtel : « 16 chambres de 90 € à 160 € ».
  - Restaurant de cuisine traditionnelle : repas de 20 à 32 €, menu « région gourmande » à 32 €, menu enfant à 14 €. Service de 12h à 14h et de 19h à 21h30.
  - Fermetures : chaque semaine le dimanche soir et le lundi, sauf du 1er mai au 30 septembre. **Fermeture annuelle en janvier et février.**
- **Description générale** (Voyage Privé, non datée) [Y2-22, page lue] :
  - Château construit en 1835 et relais de chasse jusqu'à la fin du XXe siècle. Il est devenu un hôtel en 1998.
  - Chambres Classique (13 à 22 m²) et Confort (16 à 26 m²), chambre individuelle avec supplément.
  - Dîner sur réservation, avec un menu qui change chaque mois (entrée, plat et dessert, dont une option végétale).
  - Équipements : piscine extérieure chauffée de début juin à fin septembre, hammam, modelages, **pêche et canotage sur l'étang**, prêt de vélos, billard, bibliothèque, potager pédagogique.
  - Arrivée à 15h, départ à 12h. Taxe de séjour d'environ 1 € par chambre et par nuit. Animaux « non acceptés » à l'époque.
- **Séminaires, réceptions et restaurant** (ABC Salles, non daté, mentionne un « service 4 étoiles ») [Y2-26, page lue] :
  - Tarifs indicatifs : **séminaire résidentiel à partir de 201 €, journée d'étude à partir de 69,50 €, banquet à partir de 36 € par personne hors boissons**.
  - 4 espaces pour 180 m² au total : Bibliothèque (75 m², 48 personnes), Directoire (35 m², 30), Salon de chasse (35 m², 30) et Salon du milieu (35 m², 20). Capacité affichée de 2 à 110 personnes.
  - 19 chambres et 38 couchages. Restauration non imposée et traiteur extérieur autorisé. Parking de 40 places.
  - Restaurant : « Nos menus : 27 €, 41 €, 50 €, 64 € », avec un chef présenté comme « jeune Toques d'Auvergne ».
- **Capacités des salons** (Naboo, mise à jour du 19/11/2024) [Y2-25, page lue] :
  - Bibliothèque, 75 m² : 30 en conseil, 30 en classe, 40 en théâtre, 20 en U, 48 en îlots.
  - Directoire et Salon de chasse, 35 m² chacun : 16 en conseil, 20 en classe, 24 en théâtre, 14 en U, 30 en îlots.
  - Salon du milieu, 35 m² : 10 en conseil, 10 en classe, 16 en théâtre, 8 en U, 20 en îlots.
  - Capacité maximale de 48 personnes, 19 chambres.
- **Autres plateformes de réception** :
  - Bridebook annonce « 60 invités » et la Bibliothèque de 75 m² pour 48 personnes en cocktail [Y2-38, extrait, page bloquée en 403].
  - Aleou indique une capacité maximale de 40 personnes et « 4 salons modulables » [Y2-39, extrait, page bloquée en 429].
  - Aucun tarif de mariage ni de privatisation n'a été trouvé (INCONNU).
- **Article de Yonder du 02/07/2024** [Y2-24, page lue] :
  - Hôtel « membre des Collectionneurs », 19 chambres de 13 à 35 m², restaurant Art déco.
  - « Les 2 Toques Gault et Millau accordées au chef », cours de cuisine.
  - Piscine extérieure chauffée, massages et hammam dans l'espace bien-être au premier étage, billard.
  - « 40 hectares de parc, dont 30 en pâture » et « l'un des 40 chevaux qui vivent sur le domaine ». Le haras y est décrit comme « le dada du proprio Pierre-Marie Tissier ».
- **Gault&Millau 2025**, catégorie « Hôtel de Prestige » [Y2-18, page lue] :
  - Budget de **131 € par nuit sans petit-déjeuner**.
  - « 19 chambres et suites », « écuries comptant 26 boxes, un manège couvert », piscine extérieure, sauna et hammam, soins et modelages.
  - Cours d'équitation et « poney club du domaine ».
- **Restaurant « L & Luy au Château d'Ygrande »** [Y2-19, extrait] : note de 14/20, prix de 33 à 64 € par personne hors boissons, cuisine végétale nourrie par le potager. La fiche renvoie une erreur 404 le 14/10/2026 [Y2-19, page lue : 404].
  - GreenGo indique que le restaurant est ouvert « tous les midis et soirs du mercredi au dimanche » et affiche « à partir de 152 € / nuit » [Y2-37, extrait].
  - Un échange de questions-réponses daté d'octobre 2021 indique un service du dîner de 19h à 20h30 et un restaurant fermé « uniquement le lundi et mardi midi » [Y2-30, page lue, fiabilité faible : agrégateur aux dates incohérentes].
- **Petit-déjeuner** :
  - Buffet de 7h30 à 10h30 à **20 € par adulte** [Y2-28, page lue]. HalalBooking (données de type Expedia) donne aussi 20 € par personne, une taxe de séjour de 1,10 € par personne, des animaux à 10 € par jour et un lit d'appoint à 25 € [Y2-31, page lue].
  - Un agrégateur donne 16 € par personne et des lits d'appoint à 12 € (date inconnue) [Y2-30, page lue, fiabilité faible].
- **Fermeture annuelle** : « The property is closed during January and February » ; réception ouverte de 8h30 à 22h [Y2-29, page lue] [Y2-28, page lue].
- **Offre senior** (désormais supprimée) : 30 % de remise sur la chambre et un apéritif offert aux plus de 65 ans, du dimanche soir au jeudi soir. L'article a été publié le 26/03/2014 et modifié le 24/07/2026. Il mentionne 19 chambres climatisées [Y2-21, page lue].
- **Demi-pension** : aucun tarif public de l'hôtel n'a été trouvé (INCONNU). Le seul indice est le forfait « En solo » des écuries : 2 jours et 1 nuit en basse saison, en **demi-pension**, avec 2 h d'équitation, à partir de **305 €** [Y2-11, page lue].
- **Prix « à partir de » relevés sur des comparateurs, à des dates inconnues** :
  - The Hotel Guru : « from $133 » [Y2-23, page lue].
  - Cityzeum : « à partir de 120 € » [Y2-41, page lue, fiabilité faible].
  - Kayak : 306 $ pour la nuit du 21 au 22/10/2026, en chambre standard, un prix probablement issu d'un stock d'agence non mis à jour [Y2-27, page lue].

## 2. Centre équestre

### 2.1 Affiliation FFE

- Le localisateur public de clubs de la FFE (service utilisé par ffe.com/trouver-un-club) a été interrogé le 14/10/2026 [Y2-16, page lue] :
  - Nom : « ECURIES DU CHATEAU D YGRANDE », Château d'Ygrande, Le Mont, 03160 Ygrande. Site déclaré : ecuriesduchateaudygrande.com.
  - Numéro public **0316005** et statut **CLAG**. Il s'agit, à ma connaissance, du statut de club agréé, c'est-à-dire d'une structure commerciale, par opposition au statut CLAF des associations. Cette interprétation est à confirmer.
  - Labels : **École Française d'Équitation, Poney Club de France, Cheval Club de France, Bien-être animal**.
  - **Pas de label Cheval Étape ni de label de tourisme équestre.** Pour comparaison, le Country Pony Ranch, autre club d'Ygrande, détient les labels Cheval Étape et Centre de Tourisme Équestre.
- L'activité de compétition est confirmée par le championnat départemental de dressage organisé le 21/04/2024, avec des épreuves Poney 3 à Poney Élite et Club 4 à Club Élite et un engagement sur « FFE club SIF » [Y2-13, page lue]. Les tarifs club incluent par ailleurs licences et examens fédéraux [Y2-07, page lue].

### 2.2 Activités et tarifs du club

La page n'est pas datée. Son contenu date probablement de 2023-2024, car le site présente des événements de 2022 à 2024 [Y2-07, page lue].

| Prestation | Tarif |
|---|---|
| Cours collectif (1 h, 6 cavaliers au maximum) | 25 € par personne |
| Cours particulier à 2 cavaliers (1 h) | 30 € par personne |
| Cours particulier individuel (1 h) | 35 € |
| Carnet famille poney (10 h, valable 3 mois) | 185 € |
| Carnet famille cheval (10 h, valable 3 mois) | 205 € |
| Promenade adulte (1 h, 3 à 6 cavaliers, tarif réservé aux adhérents) | 34 € par personne |
| Petite randonnée (2 h) | 58 € par personne |
| Promenade « poney en main » (30 min) | probablement 16 € par enfant |
| Baignade à cheval | probablement 34 € par personne |
| Adhésion au club | 50 € |
| Licence FFE junior / senior | 29 € / 40 € |
| Examen fédéral | 8 € |

- L'ordre des lignes sur la page rend ambiguë l'attribution des prix du poney en main et de la baignade.
- Le club utilise le logiciel **Kavalog** pour la gestion des cours. Il enseigne le saut d'obstacles, le dressage et la promenade, et accompagne en concours club et amateur. Le responsable des écuries est un cavalier professionnel de CSO et de jeunes chevaux, de niveau DEJEPS [Y2-07, page lue] [Y2-13, page lue].
- **Randonnées** : le site de 2026 précise « Il ne s'agit pas d'un raid itinérant sur plusieurs jours ». Les sorties se font dans le domaine et la campagne proche. La forêt de Tronçais est située « à une trentaine de kilomètres » et n'est pas présentée comme un terrain de sortie régulier [Y2-05, page lue].
- **Stages d'hiver de CSO** à partir du 22/10/2023 : 30 € la séance avec l'enseignant maison, 55 € avec un cavalier professionnel invité. **« Test of Choice »** le 03/03/2024 : 25 € par passage, box à 27 €, repas « proposé par le Chef des cuisines du Château d'Ygrande**** » à 25 € [Y2-13, page lue].
- **Location d'un camion pour chevaux** via Renteo : à partir de 135 € par jour en semaine (200 km inclus) et 280 € le week-end (400 km inclus) [Y2-15, page lue].

### 2.3 Pension et travail du cheval (tarifs à partir de, par mois)

| Formule | Contenu | Tarif mensuel |
|---|---|---|
| Pension au pré | | 170 € |
| Pension au box | 2 repas de foin et 5 de floconnés par jour, sortie quotidienne | 410 € |
| Pension coaching et valorisation | box et paddock, plus travail du cheval | 565 € |
| Pension débourrage et pré-entraînement | | 750 € |

- Équipements mis en avant : carrières, rond de longe, marcheur et piste de galop [Y2-08, page lue].
- Formules de séjour avec cheval (site des écuries) : box à **30 € par nuit**, plus 45 € pour la mise sur copeaux. Le transport du cheval est possible sur demande [Y2-11, page lue].

### 2.4 Chevaux et installations

- **Cavalerie** : « 25 chevaux et poneys de loisir et de sport ». Races : Selle Français, ibériques, Pur-sang, Connemara, Poney Français de Selle et Shetland [Y2-10, page lue]. Yonder parle en 2024 de « 40 chevaux qui vivent sur le domaine », un chiffre qui inclut sans doute l'élevage et les pensions (ESTIMATION) [Y2-24, page lue].
- **Installations** (site des écuries) [Y2-10, page lue] :
  - Manège couvert de 20 × 40 m et deux carrières de 30 × 60 m et 20 × 40 m, avec arrosage automatique.
  - Marcheur couvert de 4 places et rond de longe.
  - **23 boxes** de 3 × 3 m.
  - **Piste de galop de 800 m**, **26 ha de pâtures** et paddocks de 300 à 800 m².
  - Étang « pour les baignades avec les chevaux ».
- Ces chiffres diffèrent selon les sources : 26 boxes [Y2-01, page lue] [Y2-18, page lue], et 24 boxes, environ 750 m de piste et environ 27 ha selon l'annonce SAFER (déjà établi). Voir la section des contradictions.

### 2.5 Élevage

- La page « Élevage » du site des écuries, écrite en 2024, liste [Y2-09, page lue] :
  - les naissances 2024 (2 poulains et 1 à venir) ;
  - les poulains de 1 an (1), de 2 ans (2) et de 3 ans (3) ;
  - les chevaux de 4 ans (3) et de 5 ans (1).
- La date d'écriture se déduit des initiales des noms, qui suivent l'alphabet annuel français : O pour 2024, N pour 2023… jusqu'à J pour 2019 (ESTIMATION).
- **Orientation dressage et sport** :
  - Étalons utilisés : Qlassic Bois Margot, Bon Cœur, Glamourdale, Conte Bellini, Negro, Bakou du Rouet, Herald d'Émeraude.
  - Trois poulinières reviennent dans les pedigrees, ce qui suggère un petit élevage d'environ 1 à 3 naissances par an (ESTIMATION).
  - Résultats : 1er, 2e et 3e prix en finale régionale France Dressage (Vichy) pour des 4 ans, et 13e place en finale du Concours Selle Français des 3 ans à Fontainebleau.
  - Plusieurs jeunes chevaux ont été « vendu(e)s ». La page « Chevaux à vendre » affichait deux chevaux à 3 000 € et 12 000 € [Y2-13, page lue].
- **Affixe** : aucun affixe visible, car les noms ne portent pas de suffixe d'élevage. Les données IFCE et SIRE (naisseur, propriétaire) sont INCONNUES : infochevaux.ifce.fr a renvoyé une page anti-robot, et je n'ai pas cherché à la contourner. Pour vérifier, il faut chercher à la main dans Info chevaux les noms des chevaux nés en 2019-2020, puis lire le champ « naisseur ».

### 2.6 Événements accueillis par les écuries (2022 à 2024)

- 2022 : « Entraînements du Château » avec un juge national élite (repas du samedi soir à 16 €) et journée portes ouvertes.
- 2023 : France Dressage (SHF) le 08/07, portes ouvertes le 10/09, journée d'approbation des éleveurs Barock Pinto le 21/09, stages de CSO d'hiver à partir du 22/10.
- 2024 : Test of Choice le 03/03, championnat départemental de dressage le 21/04, France Dressage le 07/07.

Ces événements sont décrits sur les pages du site des écuries [Y2-13, page lue].

### 2.7 Rôle des structures équestres et imbrication avec l'hôtel

- **Haras du Château d'Ygrande** : en 2011, un commentaire d'annuaire évoque des services pour **chevaux de course** : « débourrage, pré-entraînement et pensions-propriétaires » [Y2-33, page lue]. La piste de galop de 800 m est cohérente avec ce passé (ESTIMATION).
- **Passage aux « Écuries du Château d'Ygrande »** : un texte non daté, sans doute repris d'une fiche Google, indique : « Le Haras du Château d'Ygrande devient Les Écuries du Château d'Ygrande. Un nouveau moniteur a été recruté et la cavalerie entièrement renouvelée. Les Écuries travaillent désormais main dans la main avec l'hôtel-restaurant… » [Y2-32, page lue]. Ce passage est cohérent avec la création de l'EARL Écuries du Château en 2016 (registre, déjà établi).
- **EARL Écuries du Château** : le pied de page du site des écuries indique un capital de 7 500 €, le SIRET 820 732 873 00014 et le code **APE 8551Z** (enseignement de disciplines sportives et de loisirs) [Y2-06, page lue]. Ses activités publiées sont les suivantes [Y2-06 à Y2-15, page lue] :
  - club FFE ;
  - pensions, débourrage et valorisation ;
  - élevage et vente de chevaux ;
  - organisation de concours ;
  - séjours équestres vendus avec les chambres du château ;
  - location de camion.
  En 2026, elle édite aussi le site du château et commercialise les chambres en « chambres d'hôtes » [Y2-02, page lue].
- **Imbrication** entre l'hôtel et les écuries :
  - Ils partagent le même téléphone et le même domaine de messagerie (equitation@, club@ et reservation@chateauygrande.fr) [Y2-06, page lue].
  - Les mentions légales du site des écuries indiquent « Nom juridique de l'établissement : Groupe Cœur et Détente SARL – Nom commercial : Écuries du Château », avec le SIRET de l'EARL. Il s'agit probablement d'un copier-coller des mentions de l'hôtel [Y2-14, page lue].
  - La page « Équipe » présente le gérant comme « Directeur et Propriétaire des Écuries du Château d'Ygrande et du Château d'Ygrande Chambre d'hôtes ». Une seconde personne y est présentée comme copropriétaire (profession médicale). Je ne reprends pas son nom : il figure sur la page, et le directeur peut le vérifier au registre [Y2-12, page lue].
- **Conséquence pour l'analyse** : le chiffre d'affaires du cheval (leçons, pensions, élevage) était porté par les EARL, et non par la SAS hôtelière. Le chiffre d'affaires d'environ 1,1 M€ de la SAS ne contient donc au plus que la part hébergement des forfaits équestres (ESTIMATION, voir la section 6).

## 3. Classement et réseaux

- **Atout France** (jeu de données « Hébergements touristiques classés en France », fichier mis à jour le 13/10/2026) [Y2-17, page lue] :
  - Ligne « HÔTEL CHÂTEAU D'YGRANDE », Le Mont, 03160 Ygrande : hôtel de tourisme **4 étoiles**, **classé le 27/06/2022**.
  - **19 chambres**, **capacité de 43 personnes**, « classement prorogé : non ».
  - L'hôtel figure toujours dans le fichier au 13/10/2026, alors que l'exploitant a été liquidé et que le site se présente désormais comme une maison d'hôtes.
  - Dans le même secteur, le Grand Hôtel Montespan Talleyrand à Bourbon-l'Archambault est aussi classé 4 étoiles (17 chambres).
- **Les Collectionneurs, devenu Teritoria** :
  - Yonder (2024) le présente comme « membre des Collectionneurs » [Y2-24, page lue]. Trip.com l'affiche sous le nom « Château d'Ygrande - Teritoria », avec une URL contenant « les-collectionneurs » [Y2-28, page lue].
  - La fiche teritoria.com renvoie une **erreur 404** le 14/10/2026 [Y2-36, page lue]. D'après les résultats de recherche, elle mentionnait « 18 chambres - Château » et les 2 toques du chef [Y2-36, extrait].
- **Logis, Relais du Silence, Châteaux & Hôtels Collection** : aucune trace trouvée [recherches WebSearch n°6 et n°12]. Cette absence ne prouve pas que l'hôtel n'en a jamais été membre (INCONNU).
- **Guides** :
  - **Gault&Millau** : hôtel « Hôtel de Prestige » en 2025 [Y2-18, page lue]. Restaurant noté 14/20 [Y2-19, extrait], avec « 2 Toques » selon Yonder (2024) [Y2-24, page lue]. Foodle date les 2 toques de 2021 [Y2-43, extrait, page bloquée en 403]. La fiche LesRestos de 2003 citait déjà le guide [Y2-20, page lue].
  - **Michelin** : aucune mention trouvée (INCONNU). La page Michelin testée a renvoyé un défi anti-robot.
  - **Petit Futé** : la fiche existe (n° 699484), avec une note de 4,5/5 sur 19 avis [Y2-35, extrait]. La page est bloquée (403).

## 4. Avis clients

| Plateforme | Note | Nombre d'avis | Remarque | Source |
|---|---|---|---|---|
| Google (widget du site officiel) | 4,3/5 | 458 | Plateforme déduite des couleurs du logo SVG ; date de collecte inconnue | [Y2-01, page lue] |
| TripAdvisor (widget du site officiel) | 4,2/5 | 671 | Logo vert #34E0A1 | [Y2-01, page lue] |
| TripAdvisor (via lastminute) | 4,2/5 | 671 | Sous-notes : propreté 4,4, service 4,4, emplacement 4,4, **chambre 3,9, qualité/prix 3,9** | [Y2-34, extrait] |
| Kayak | 8,0/10 | 199 | Répartition : 89 « Wonderful », 39 « Very good », 35 « Good », 14 « Okay », 6 « Fair », 8 « Mediocre », 8 « Poor » | [Y2-27, page lue] |
| Kayak (autre extrait) | 7,9/10 | 214 | | [Y2-27, extrait] |
| Naboo | 4,3 | 415 | Plateforme d'origine non précisée | [Y2-25, page lue] |
| Trip.com | 8,0/10 | 14 | | [Y2-28, page lue] |
| icastelli.net | 8,3/10 | 99 | Fiabilité faible | [Y2-30, page lue] |
| Petit Futé | 4,5/5 | 19 | | [Y2-35, extrait] |
| Booking | INCONNU | INCONNU | Page bloquée ; un extrait cite seulement une note de 8,0 pour le petit-déjeuner | [Y2-42, extrait] |

- **Thèmes récurrents** : **je n'ai lu en entier que 3 avis** (Trip.com). Ce n'est pas suffisant pour dégager des thèmes, et je ne généralise pas.
- **Synthèse automatique de Kayak** (générée par IA, ce n'est pas ma lecture) [Y2-27, page lue] :
  - Points appréciés : emplacement (9,5/10), service (8,5) et restaurant (8,5).
  - Points faibles : taille des chambres (3/10) et petit-déjeuner (3/10). Le rapport qualité/prix est critiqué, et « some guests reported a lack of support and a rude attitude from the staff at the stables ».
  - Ces scores IA vont dans le même sens que les sous-notes TripAdvisor (chambres et qualité/prix plus faibles), mais ce sont des données de plateforme, pas une analyse des avis.
- **Avis non accessibles** : TripAdvisor (403), Booking (anti-robot), Facebook (connexion obligatoire), Google (pas d'accès direct).

## 5. Contradiction : 5 chambres (The Hotel Guru) ou 16 chambres (annonce de vente)

| Source | Année | Chambres | Statut |
|---|---|---|---|
| Atout France (registre officiel du classement) | 2022 | 19 chambres, capacité 43 personnes | [Y2-17, page lue] |
| Gault&Millau | 2025 | 19 chambres et suites | [Y2-18, page lue] |
| Yonder | 2024 | 19 chambres de 13 à 35 m² | [Y2-24, page lue] |
| Naboo, Kayak, Trip.com, ABC Salles | | 19 chambres (38 couchages selon ABC Salles) | [Y2-25, Y2-27, Y2-28, Y2-26, page lue] |
| Annonce SAFER (déjà établi) | | 16 chambres dans le château et 3 dans la maison de jardin, soit **19** | |
| Site de 2026 | 2026 | Chambres « réparties entre le château et le pavillon de jardin » ; chambres Pavillon de plain-pied | [Y2-01, page lue] |
| LesRestos | 2003 | 16 chambres | [Y2-20, page lue] |
| The Hotel Guru | | « 5 rooms in this hotel » (numberOfRooms : 5 dans ses données) | [Y2-23, page lue] |
| Teritoria, icastelli | | « 18 chambres - Château » | [Y2-36, extrait] [Y2-30, page lue] |
| GreenGo | | « 3 chambres d'hôtel » | [Y2-37, extrait] |

**Résolution :**
- Le chiffre officiel est **19 chambres** : 16 dans le château et 3 dans le pavillon (ou maison) de jardin. C'est cohérent avec le registre Atout France et l'annonce SAFER.
- Les « 16 chambres » de l'annonce correspondent au seul château. Le chiffre de 2003 laisse penser que les 3 chambres du pavillon ont été ajoutées après 2003 (hypothèse, date INCONNUE).
- Le chiffre de **5 de The Hotel Guru est isolé et vraisemblablement erroné**. Mon hypothèse : il correspond au nombre de catégories de chambres du château (Classique, Confort, Supérieure, Suite familiale, Suite de luxe, la catégorie Pavillon s'y ajoutant en 2026). C'est une hypothèse non vérifiée.
- Les « 18 » de Teritoria pourraient correspondre à 18 chambres et 1 suite (INCONNU). Les « 3 » de GreenGo correspondent peut-être aux seules chambres du pavillon (INCONNU).

## 6. ESTIMATION : répartition du chiffre d'affaires d'environ 1,1 M€ (2017-2019, SAS hôtel-restaurant)

**Cette section est une ESTIMATION**. Elle s'appuie sur des prix relevés à des dates différentes (2003 à 2026) et sur des hypothèses de fréquentation. Ce n'est pas une donnée comptable.

**Hypothèses** (calcul : `scripts/estimation.py`)

- **Capacité** :
  - 19 chambres [Y2-17].
  - Ouverture de 365 − 59 = 306 jours, en raison de la fermeture en janvier et février [Y2-20, Y2-29].
  - Cela donne **5 814 nuitées-chambres disponibles** par an.
- **Prix moyen des chambres, hors petit-déjeuner** :
  - Fourchette retenue : 130, 150 ou 170 € TTC selon le scénario, soit environ 118 à 155 € HT avec une TVA de 10 %.
  - Repères : 90 à 160 € en 2003 [Y2-20] ; 131 € « sans petit-déjeuner » en 2025 [Y2-18] ; « à partir de 152 € » chez GreenGo [Y2-37] ; 90 à 190 € « à partir de » en 2026 [Y2-01].
- **Taux d'occupation** : 35 %, 45 % ou 60 %. C'est une fourchette posée à titre d'hypothèse pour un hôtel rural saisonnier, fermé deux mois et dépendant des week-ends. Ce n'est pas une donnée sourcée.
- **Petit-déjeuner** : 1,8 personne par chambre et 80 % de preneurs, à 16-20 € TTC [Y2-28, Y2-30, Y2-31].
- **Restaurant** :
  - Ticket moyen avec boissons de 45, 55 ou 65 € TTC. Repères : menus de 27 à 64 € [Y2-26] et prix de 33 à 64 € hors boissons [Y2-19].
  - Clients de l'hôtel qui dînent sur place : 40 à 60 %.
  - Couverts extérieurs : 1 500 à 4 500 par an.
- **Événements** (montant net, hors chambres déjà comptées) : 30 à 120 k€. Repères : banquet à partir de 36 €, journée d'étude à partir de 69,50 €, résidentiel à partir de 201 € [Y2-26], et au plus environ 48 places assises.
  - Exemple pour le scénario médian : 25 événements de 30 personnes à environ 95 € par personne, soit environ 70 k€.
- **Cheval** : seule la part refacturée dans les forfaits vendus par l'hôtel compte. Les leçons et les pensions relèvent des EARL (section 2.7). L'hypothèse retenue va de 0 à 40 k€.

**Résultats** (k€ HT)

| Poste | Bas (35 % d'occupation, 130 €) | Médian (45 %, 150 €) | Haut (60 %, 170 €) | Calé sur 1,1 M€ (55 %, 160 €) |
|---|---|---|---|---|
| Nuitées vendues | 2 035 | 2 616 | 3 488 | 3 198 |
| Chambres | 240 (54 %) | 357 (45 %) | 539 (41 %) | 465 (43 %) |
| Petits-déjeuners | 43 (10 %) | 62 (8 %) | 91 (7 %) | 80 (7 %) |
| Restaurant | 120 (27 %), 2 965 couverts | 264 (33 %), 5 355 couverts | 482 (37 %), 8 267 couverts | 369 (34 %), 6 966 couverts |
| Séminaires, banquets, réceptions | 30 (7 %) | 70 (9 %) | 120 (9 %) | 100 (9 %) |
| Bien-être, bar, divers | 15 (3 %) | 30 (4 %) | 45 (3 %) | 40 (4 %) |
| Cheval (forfaits) | 0 | 15 (2 %) | 40 (3 %) | 20 (2 %) |
| **Total** | **448** | **798** | **1 317** | **1 073** |

**Exemple de calcul (scénario calé)**

| Poste | Calcul | Résultat |
|---|---|---|
| Chambres | 5 814 × 55 % = 3 198 nuitées × (160 / 1,10 = 145,5 € HT) | 465 k€ |
| Petits-déjeuners | 3 198 × 1,8 × 0,8 × (19 / 1,10) | 80 k€ |
| Restaurant | (3 198 × 1,8 × 0,55 = 3 166 couverts de clients de l'hôtel) + 3 800 couverts extérieurs = 6 966 couverts × (59 / 1,115 = 52,9 € HT) | 369 k€ |

Le scénario calé correspond à environ 23 couverts par jour d'ouverture.

**Lecture :**
- Pour atteindre environ **1,1 M€**, il faut se placer dans le haut de la fourchette. Cela suppose environ 55 % d'occupation à environ 160 € TTC et un restaurant gastronomique qui attire une clientèle extérieure réelle (environ 7 000 couverts par an).
- Contrôle inverse : 1,1 M€ ÷ 5 814 nuitées-chambres disponibles = **189 € HT de chiffre d'affaires total par chambre disponible et par nuit**, et 225 € HT si l'on ne compte que 16 chambres. Ce niveau élevé pour 19 chambres montre que la restauration et les événements pesaient lourd.
- **Répartition probable** :
  - hébergement (chambres et petits-déjeuners) : environ **45 à 55 %** ;
  - restaurant : environ **30 à 35 %** ;
  - séminaires et réceptions : environ **7 à 10 %** ;
  - bien-être et divers : environ **3 à 4 %** ;
  - cheval : **0 à 3 %** au maximum dans les comptes de la SAS, puisque l'activité équestre est comptabilisée dans les EARL.
- Repère supplémentaire : avec 10 à 19 salariés (registre), le chiffre d'affaires par salarié était d'environ 58 à 110 k€.

## Tableau de l'offre et des prix par période

| Période | Hébergement | Restauration | Événements et séminaires | Bien-être et loisirs | Cheval | Fermetures | Sources |
|---|---|---|---|---|---|---|---|
| 1998 | Le relais de chasse devient un hôtel | | | | | | [Y2-18, Y2-22] |
| 2003 | 16 chambres, de 90 à 160 € | Cuisine traditionnelle ; menus de 20 à 32 € ; « région gourmande » à 32 € ; menu enfant à 14 € | | | | Dimanche soir et lundi (sauf 1/5-30/9) ; janvier et février | [Y2-20] |
| Vers 2011 | | | | | Haras : débourrage, pré-entraînement et pension pour chevaux de course | | [Y2-33] |
| 2014 à ? | Offre senior de -30 % du dimanche au jeudi | Apéritif offert | | | | | [Y2-21] |
| Vers 2016 | | | | | Le Haras devient les « Écuries du Château » : nouveau moniteur, cavalerie renouvelée | | [Y2-32] |
| Époque 4 étoiles, non datée (vers 2017-2022 ?) | 19 chambres, 38 couchages ; Classique de 13 à 22 m² et Confort de 16 à 26 m² | Menus de 27, 41, 50 et 64 € ; menu du dîner mensuel ; petit-déjeuner à 16 € (agrégateur) | 4 salles (180 m²) ; résidentiel à partir de 201 € ; journée d'étude à partir de 69,50 € ; banquet à partir de 36 € | Piscine chauffée de juin à septembre ; hammam ; sauna ; pêche et canotage ; vélos ; billard | Centre équestre sur place | Janvier et février | [Y2-26, Y2-22, Y2-30] |
| Octobre 2021 | | Dîner de 19h à 20h30 ; fermé le lundi et le mardi midi | | | | | [Y2-30] (faible) |
| 27/06/2022 | Classement 4 étoiles, 19 chambres, 43 personnes | | | | | | [Y2-17] |
| 2023-2024 | Forfait « À deux » 2 j/1 n en basse saison à partir de 480 € ; « Solo » en demi-pension à partir de 305 € | Repas du chef à 25 € lors des événements équestres | | | Cours de 25 à 35 € ; pension de 170 à 750 € par mois ; box de passage à 30 € la nuit ; concours | | [Y2-11, Y2-07, Y2-08, Y2-13] |
| 2024 | 19 chambres de 13 à 35 m² ; Les Collectionneurs | Restaurant « L & Luy », 2 toques Gault&Millau ; cours de cuisine | Salons de 10 à 48 personnes (Naboo, 19/11/2024) | Piscine, hammam, massages | Environ 40 chevaux sur le domaine | | [Y2-24, Y2-25] |
| 2025 | « Hôtel de Prestige » Gault&Millau, budget de 131 € par nuit sans petit-déjeuner ; petit-déjeuner buffet à 20 € | Restaurant de 33 à 64 € (14/20), ouvert du mercredi au dimanche midi et soir | | Piscine, sauna, hammam | 26 boxes, poney club | Janvier et février | [Y2-18, Y2-19, Y2-28, Y2-29, Y2-37] |
| 28/10/2025 | Liquidation de la SAS (registre, déjà établi) | | | | | | |
| Septembre-octobre 2026 | « Chambre d'hôtes de luxe » éditée par l'EARL Écuries du Château d'Ygrande ; 6 types de 90 à 190 € « à partir de » ; -20 € par nuit dès 2 nuits ; pas de réservation en ligne | Pas de restaurant ; planche à 20 € pour 2 ; coin cuisine | Bibliothèque de 70 m² sur devis ; salons pour 50 personnes assises ; privatisation ; traiteurs | Hammam ; piscine chauffée de juin à septembre ; massages | Séjour équestre à 126 € par personne ; box à 30 € par jour ; coaching | INCONNU | [Y2-01, Y2-02, Y2-03] |

## Contradictions, doutes et inconnues

**Contradictions**

1. **Nombre de chambres** : 3, 5, 16, 18 ou 19 selon les sources. La résolution figure en section 5 : 19 chambres, dont 16 dans le château et 3 dans le pavillon.
2. **Nombre de boxes** : 23 sur le site des écuries [Y2-10], 24 dans l'annonce SAFER, 26 sur le site du château en 2026 et chez Gault&Millau [Y2-01, Y2-18]. Les écarts peuvent venir de dates différentes ou de boxes comptés hors écurie principale.
3. **Piste de galop** : 800 m [Y2-10] contre environ 750 m (SAFER). **Pâtures** : 26 ha [Y2-10], environ 27 ha (SAFER) ou 30 ha [Y2-24].
4. **Nombre de chevaux** : 25 pour la cavalerie de club [Y2-10] et 40 sur le domaine [Y2-24]. Ce ne sont pas les mêmes périmètres.
5. **Salle de séminaire** : la Bibliothèque fait 70 m² selon le site de 2026 [Y2-01], et 75 m² selon Naboo, ABC Salles et hotels.com.au [Y2-25, Y2-26, Y2-29].
6. **Jours d'ouverture du restaurant** :
   - 2003 : fermé le dimanche soir et le lundi hors saison [Y2-20] ;
   - 2021 : fermé « uniquement le lundi et mardi midi » [Y2-30] ;
   - selon GreenGo : ouvert du mercredi au dimanche [Y2-37].
   Ces informations correspondent à des périodes différentes.
7. **Prix du petit-déjeuner** : 16 € [Y2-30] ou 20 € [Y2-28, Y2-31], probablement à des dates différentes.
8. **Date de construction** : 1835 [Y2-22] ou 1836 [Y2-24], ce qui relève du travail de Y1. Le nom du chef est orthographié de deux façons selon les sources.
9. **Note Kayak** : 8,0 sur 199 avis (page lue) contre 7,9 sur 214 avis (extrait). Kayak affiche aussi un tarif de 306 $ pour octobre 2026, ce qui est douteux après la liquidation.
10. **Mentions légales du site des écuries** : elles citent « Groupe Cœur et Détente **SARL** » alors que le registre indique une SAS, et associent ce nom au SIRET de l'EARL [Y2-14]. Il s'agit d'une erreur de rédaction, mais elle illustre l'imbrication des deux entités.
11. **Classement Atout France** : l'hôtel est toujours listé en 4 étoiles au 13/10/2026 [Y2-17], alors que le site se présente comme une maison d'hôtes sans restaurant [Y2-01]. Le classement d'hôtel de tourisme n'a probablement plus d'objet. Ce point est à vérifier auprès d'Atout France.
12. **Code postal** : 03320 sur la fiche LesRestos de 2003, contre 03160 partout ailleurs.

**Doutes**

- Les prix « à partir de » des comparateurs (GreenGo 152 €, Hotel Guru 133 $, Cityzeum 120 €) ne sont pas datés et ne donnent pas de prix moyen.
- Les tarifs du club et des pensions ne sont pas datés. Ils sont probablement de 2023-2024, d'après les événements et l'élevage présentés sur le même site. La correspondance entre les prix du poney en main et de la baignade reste ambiguë.
- Pour l'offre de 2026, l'unité du « Séjour équestre 126 €/pers. » et le sens de « 70 EUR / 2 pers. » ne sont pas clairs.
- L'identification de Google et TripAdvisor dans le widget d'avis du site officiel repose sur les couleurs des logos SVG (inférence). La date de collecte de ces notes est inconnue.
- L'agrégateur icastelli.net affiche des dates incohérentes : des échanges de l'époque du Covid sont datés du « 3 octobre 2026 ». Il est classé en fiabilité faible.
- Cityzeum présente un texte générique, probablement automatique. Il est classé en fiabilité faible.

**Inconnues, avec la manière de vérifier**

- **Prix des chambres par saison de 2009 à 2025, tarif de la demi-pension, formules et jours du restaurant par année, tarifs mariages et privatisation** : INCONNUS. Il faut consulter à la main les captures web.archive.org listées en 1.3, depuis un réseau où le site répond, ou interroger l'API CDX (`https://web.archive.org/cdx/search/cdx?url=chateauygrande.fr&matchType=domain&output=json&collapse=timestamp:6`).
- **Taux d'occupation, prix moyen réel et nombre de couverts** : INCONNUS. Ces chiffres figurent seulement dans la comptabilité ou dans le dossier du liquidateur (mandataire du tribunal de commerce de Cusset).
- **Données IFCE** (naisseur, propriétaire, affixe) : INCONNUES, la page IFCE étant protégée par un anti-robot. Il faut faire une recherche manuelle dans Info chevaux sur les noms des chevaux nés en 2019 et 2020.
- **Nombre de licenciés du club FFE** : INCONNU, car non publié dans le localisateur. Il faut le demander au comité départemental d'équitation de l'Allier ou consulter la fiche du club.
- **Notes Booking et Google détaillées, et texte des avis** : INCONNUS, les pages étant bloquées. Il faut les consulter à la main dans un navigateur.
- **Appartenance à Logis, Relais du Silence ou Châteaux & Hôtels Collection, et mention au guide Michelin** : aucune trace trouvée, mais l'absence n'est pas prouvée.
- **Dates d'entrée et de sortie du réseau Les Collectionneurs/Teritoria** : INCONNUES. La fiche renvoie une erreur 404 au 14/10/2026.
- **Date d'ajout des 3 chambres du pavillon** (entre 2003 et 2022) : INCONNUE.
- **Statut juridique de l'exploitation des chambres en 2026** par l'EARL (maison d'hôtes, déclaration en mairie, régime fiscal agricole ou commercial) : INCONNU. Le directeur peut le vérifier au registre (activités déclarées de l'EARL) et auprès de la mairie d'Ygrande.
