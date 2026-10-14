# Analyse immobilière — Agent 1 « Chasse immobilière » (Opération Château v2)

Date de vérification : 2026-10-14. Fichiers liés : `Domaines_identifies.csv` (29 fiches classées), `_brut/sources_agent1.csv` (69 sources).

Légende des statuts : **PAGE LUE** (page ouverte le 2026-10-14), **EXTRAIT** (vu seulement dans un résultat de recherche), **ESTIMATION** (raisonnement explicite), **INCONNU**.

---

## 1. Méthode

- **Budget de recherche** : 16 WebSearch sur 25 autorisées. L'outil WebFetch échouait sur la résolution DNS dans cet environnement : toutes les pages ont donc été téléchargées avec `curl`, à travers le proxy, puis converties en texte. C'est équivalent à une lecture de page. Chaque fiche du CSV correspond à une annonce **réellement ouverte le 2026-10-14** et qui affichait encore le bien (pas de mention « annonce supprimée »).
- **Sources réellement exploitées (PAGE LUE)** :
  - Patrice Besse : rubrique équestre, 16 biens, dont 5 annonces ouvertes.
  - French-Property, agrégateur qui reprend Green-Acres, Leggett, Mercure, Maxwell-Baynes/Christie's, Prestige Property Group, etc. : recherche filtrée « château, ≥ 30 ha, 0,7-6,5 M€ » (34 résultats, 25 lus), puis « château, 15-30 ha, mot-clé boxes » (6 résultats).
  - ma-propriete.fr : rubriques haras, propriétés équestres, domaines agricoles et châteaux, avec leur observatoire de prix DVF/SAFER.
  - proprietes-rurales.com, portail national des **SAFER** : vocations « activités équestres », « patrimoine/MH » et « tourisme ».
  - Licitor et Avoventes pour les ventes judiciaires.
  - Presse et données d'entreprise : MySweetImmo, Eurodressage, Xerfi, BOAMP.
- **Sites bloqués** :
  - Belles Demeures et Capifrance renvoient un HTTP 403 (anti-robot). Les biens Capifrance ont été lus via ma-propriete.fr.
  - Propriétés Le Figaro, Barnes, Sotheby's, Emile Garcin et Mercure Forbes n'ont pas été interrogés en direct, faute de budget de recherche et d'URL de recherche exploitable. Leurs biens apparaissent en partie via les agrégateurs.
  - Equirodi et Cheval Annonce n'ont pas été couverts. C'est une lacune.
- **Classement** (note /10, ESTIMATION) : château ou grande demeure, ≥ 30 ha disponibles, écuries existantes, outil d'hébergement ou d'événementiel déjà en place, prix compatible avec 1-6 M€, CAPEX raisonnable, et existence d'un montage atypique.
- **Pas de remplissage** : 29 fiches. Les biens dont l'annonce était supprimée, ou qui n'ont été vus qu'en extrait, sont listés à part (§7) et ne figurent pas dans le CSV.

## 2. État du marché (prix/ha observés)

**Châteaux ≥ 30 ha à vendre entre 0,7 et 6,5 M€** (19 biens distincts lus sur French-Property, ESTIMATION statistique faite par moi) :

| Indicateur | Valeur |
|---|---|
| Prix médian | **2,5 M€** (quartiles 1,29 / 3,07 M€) |
| Prix total ÷ surface, bâti inclus | **médiane ≈ 59 000 €/ha**, min ≈ 14 200 €/ha (Treteau 03, 69 ha, 980 k€), max ≈ 191 000 €/ha (château de mariage près de Bordeaux, 6 M€) |
| Quartiles prix/ha | 34 800 / 59 100 / 78 600 €/ha |

Ce ratio « €/ha » est surtout porté par le bâti. Le foncier nu pèse peu, comme le montrent les repères ci-dessous (PAGE LUE, observatoire ma-propriete.fr du 24/09/2026, chiffres DVF 2025 et barème SAFER 2025) :

- **Terres agricoles en France (DVF 2025)** : médiane **5 307 €/ha**, moyenne 6 059 €/ha, 14 328 ventes.
- **Barème SAFER 2025** : terres et prés libres 6 460 €/ha, terres louées 5 350 €/ha, soit environ 17 % de décote quand un fermier est en place.
- **Terres libres par région** (SAFER 2025) : Normandie 9 610 €/ha, Pays de la Loire 4 100, Nouvelle-Aquitaine 5 770, Centre-Val de Loire 6 260, Bourgogne-Franche-Comté 2 740, Auvergne-Rhône-Alpes 5 100.
- **Grandes demeures rurales de plus de 300 m² (DVF 2025)** : 981 ventes, médiane **822 000 €**, moyenne 1,32 M€, 2 308 €/m².
- **Haras listés sur ma-propriete.fr** : médiane **880 000 €**, médiane 27 ha.
- **Propriétés équestres listées sur ma-propriete.fr** : médiane 650 000 €, médiane 5,3 ha.

**Lecture (ESTIMATION)** : sur 50 ha, la terre ne représente qu'environ 0,25-0,5 M€. Tout le reste du prix paie le château et les installations. C'est donc **le bâti qui fait le prix, et le CAPEX qui fait le risque**.

Les vraies « affaires » de surface se trouvent :
- dans le Bourbonnais, l'Allier, la Vendée et le Sud-Ouest intérieur (Dordogne, Lot-et-Garonne, Gers, Aude) ;
- sur les biens grevés d'un bail rural (Treteau) ;
- sur les biens vendus par la SAFER (prix affichés hors frais).

## 3. Top 5 commenté

1. **Ygrande (03) — château Directoire + haras touristique, 40,7 ha, 2 650 000 € (vente SAFER ARA)** — PAGE LUE (deux annonces).
   - **Ce qu'il y a** : c'est le seul bien qui coche toutes les cases à la fois. Château d'environ 1 500 m² avec **16 chambres climatisées** et une cuisine pro. Côté chevaux : 24 boxes, manège couvert, 2 carrières, piste de galop d'environ 750 m, marcheur et environ 27 ha de pâtures.
   - **Limites** :
     - Le vendeur est la Safer. L'attribution passe donc par son comité, avec un cahier des charges probable sur le maintien agricole des terres. L'annonce propose d'ailleurs d'associer un agriculteur partenaire.
     - Isolement : 3 h 45 de Paris.
     - État réel inconnu.
   - **CAPEX (ESTIMATION)** : 0,15 à 0,7 M€.
2. **Charente méridionale (16) — château de 850 m², 36,8 ha (+7 ha loués), 3 150 000 €** — PAGE LUE.
   - **Atouts** : outil équestre clé en main (16 boxes de 20 m² avec paddock, manège 25 × 50 m, marcheur 8 places) et maison d'hôtes communicante de 150 m². Le bien est annoncé « en parfait état ».
   - **Limites** : prix élevé, et commune exacte non publiée.
3. **Sainte-Hermine (85) — château XIXe de 670 m² sur 56,5 ha, 1 150 000 € hors frais Safer** — PAGE LUE.
   - **Atouts** : meilleur rapport surface/prix pour un vrai château de plus de 50 ha. Deux logements sont déjà restaurés.
   - **Limites** : écuries et sellerie (300 m²) à rénover, aucune carrière.
   - **Coût total (ESTIMATION)** : environ 1,25 M€ frais Safer compris, plus 0,25 à 0,7 M€ de CAPEX. C'est une cible plausible pour un dossier « jeune porteur de projet » présenté à la Safer.
4. **Château Napoléon III (Fougères/Mayenne) — 32,2 ha, 2 530 000 €** — PAGE LUE.
   - **Atouts** : activité mariages et séminaires en place (jusqu'à 400 couverts sous chapiteau, grange, orangerie), 4 maisons d'amis, écuries sur plus de 10 ha. C'est le modèle « l'événementiel finance les chevaux » prêt à fonctionner.
   - **Limites** : chiffre d'affaires inconnu, localisation incohérente dans l'annonce.
5. **Sandillon (45) — château XVIIIe, activité événementielle, 11 ha** — PAGE LUE.
   - **Prix** : **2 420 000 €, ou 1 050 000 € en achetant les parts de la SCI avec reprise des emprunts à 1,36 % fixe**. C'est le ticket d'entrée le plus bas observé pour un château exploité.
   - **Limites** : 11 ha seulement, aucune écurie décrite, vente entre particuliers. Comptes, capital restant dû et passif de la SCI sont tous INCONNUS : un audit est indispensable.

Mention « prix plancher » : **Treteau (03)**, château XVIIIe de 440 m² sur 69 ha pour **980 000 €**. Mais 66 ha sont affermés jusqu'en décembre 2033 et le DPE est en classe F. Le calendrier « vivre au château vers 2030-2031, terres libérées en 2034 » est cohérent, mais il faut un plan pour les chevaux sur le parc et les dépendances d'ici là.

## 4. Typologie de domaine à rechercher (recommandation, ESTIMATION)

- **Demeure** : château ou grande demeure de 400 à 900 m² habitables. Au-delà, le chauffage et l'entretien explosent : à Montluçon, l'annonce affiche 18 à 25 k€/an d'énergie pour 1 150 m².
- **Foncier** : 30 à 70 ha, dont au moins 20 ha de prairies d'un seul tenant. Éviter les domaines majoritairement boisés (le château de la Double, en Dordogne, a 70 ha de bois sur 92). Vérifier l'absence de bail rural, ou son échéance.
- **Écuries existantes** : au moins 10 boxes, ou des dépendances convertibles. Une carrière coûte peu à créer. Un manège coûte cher : le prendre existant si possible.
- **Brique de revenu déjà en place** : gîtes ou chambres d'hôtes, ou salle de réception. Cela évite une période sans recettes.
- **Prix « château + 30 ha »** : sous environ 1,5 M€ hors travaux. Sinon, recourir à un montage (SCI, crédit-vendeur, location).
- **Écarter** :
  - les châteaux « coquille vide » ou en DPE G (Auch : 675 k€ d'achat, mais 0,9 à 2 M€ de restauration en ESTIMATION) ;
  - les classements MH sans projet de défiscalisation adapté.

## 5. Régions cheval (lecture du marché observé)

- **Normandie** (Orne, Calvados, Pays d'Auge) : écosystème le plus dense (cliniques, étalons, ventes), mais terres les plus chères (environ 9 600 €/ha libre). Biens surtout orientés élevage pro. Exemple : haras Safer du Pays d'Auge, 25,7 ha, 2,1 M€, sans demeure.
- **Pays de la Loire / Sarthe / Mayenne / Maine-et-Loire** : bon compromis entre accès à Paris (Sablé est à 55 min en TGV), foncier modéré (environ 4 100 €/ha) et château équestre disponible (Sablé, Challain, Fougères/Mayenne, Sainte-Hermine).
- **Centre-Val de Loire / Berry / Sologne** : châteaux nombreux avec des écuries historiques (Bourges, Chabris, Sandillon). La clientèle chasse et événements de la Sologne est un atout.
- **Allier / Bourbonnais** : rapport prix/surface le plus favorable pour un château (Ygrande, Treteau), à proximité de pôles équestres. Faiblesse : l'isolement.
- **Nouvelle-Aquitaine intérieure et Lot-et-Garonne** : beaucoup d'offre entre 1 et 1,5 M€ pour plus de 30 ha (Penne-d'Agenais, Bergerac, Charente), et un vivier anglophone pour l'hébergement.
- **Oise / Chantilly** : pôle courses et galop. Les biens sont plutôt des haras que des châteaux (exemple : 32 ha et 24 boxes pour 1,595 M€).

## 6. Biens pour montages atypiques

| Montage | Bien(s) | Ce qui est vérifié | À vérifier |
|---|---|---|---|
| **Achat de parts de société (SCI) avec reprise de dette** | Sandillon (45) | PAGE LUE : « 1 050 000 € avec reprise des emprunts en cours… taux fixe 1,36 % », ou 2 420 000 € pour le domaine seul | Capital restant dû, garanties, passif, bail entre la SCI et la société d'exploitation |
| **Vente SAFER** (attribution sur projet, cahier des charges) | Ygrande, Sainte-Hermine, Double (24), Lalinde (24), haras du Pays d'Auge | PAGE LUE. Pour le haras normand : frais Safer 8,4 % TTC, et « opération exonérée des droits d'enregistrement par l'engagement du maintien de la destination agricole » | Si l'exonération s'applique aussi aux autres biens ; durée de l'engagement ; critères d'attribution (jeune agriculteur ?) |
| **Bien grevé d'un bail rural** (décote, revenu de fermage) | Treteau (03), 66 ha affermés jusqu'en déc. 2033 | PAGE LUE | Montant du fermage ; conditions de reprise des terres |
| **Division d'un grand domaine** (acheter seulement le haras, ou s'associer à un hôtelier) | Poitiers 112 ha, 10,3 M€ : le haras XIXe de 22 boxes et sa maison de 350 m² ont une entrée indépendante | PAGE LUE (configuration) | Que le vendeur accepte de diviser : INCONNU |
| **Reprise d'un château-entreprise** | Château de mariage près de Bordeaux, 6 M€ ; Marols (42), 5,99 M€, 30 chambres ; Fougères/Mayenne | PAGE LUE | Chiffre d'affaires et EBE jamais publiés |
| **Revenus énergie adossés au foncier** | Ain, 80 ha, 3,105 M€ : PV sur 2 100 m² (contrat EDF 35 ans), 3 éoliennes (bail emphytéotique 99 ans) | PAGE LUE | Montants des loyers et revenus : INCONNU |
| **Concession publique / DSP** (contrôler un domaine sans l'acheter) | Haras de Jardy (92, 75 ha) : concession du centre équestre, avis BOAMP 2025, PAGE LUE ; Haras de Rosières-aux-Salines : DSP signée le 10/06/2026, EXTRAIT ; Haras du Pin : appel à projets hôtel 2022, EXTRAIT | Partiel | Calendrier des prochaines consultations : INCONNU. À suivre sur le BOAMP |
| **Vente judiciaire / liquidation** | Aucun château ou domaine équestre en cours trouvé sur Licitor ou Avoventes au 14/10/2026. Seul exemple, ancien : Château de Lévaré (53), liquidation de la SARL Le Château Vert, appel d'offres en 2019 (PAGE LUE sur Licitor) | — | Mettre en place une veille BODACC / Licitor / Avoventes / Actify |
| **Vendeur sous pression** (baisses de prix) | Haras de Hus (44), 128 ha avec château de 1 000 m² : 20 M€ (déc. 2023), puis 12,9 M€ (oct. 2024), sur le marché depuis 2020 | PAGE LUE (presse) | Statut actuel : INCONNU. Hors budget, mais instructif (voir §7) |
| **Crédit-vendeur / location-accession / location** | Aucune annonce lue ne le propose explicitement | — | À négocier au cas par cas. Biens à cibler : propriétaires âgés, successions, biens en vente depuis longtemps |

## 7. Contre-exemples et signaux de prudence

- **Haras de Hus** (PAGE LUE, Xerfi) : chiffre d'affaires de **1 771 k€ en 2024**, pour un **résultat d'exploitation de −3 908 k€** et un résultat net de −2 936 k€. Le cheptel a été entièrement vendu en juin 2024 (EXTRAIT). Un haras de prestige peut donc perdre beaucoup plus qu'il ne gagne. C'est exactement le cas « EBITDA négatif » à éviter.
- **Annonces disparues** (vendues ou retirées, PAGE LUE avec la mention « supprimée ») : Sillans-la-Cascade (83), 160 ha, 13,5 M€ ; Agen (47), 9,93 ha, 2,1 M€ ; Argentan (61), manoir de 12 ha, 2,1 M€ ; Billère (64), 682,5 k€. Les biens équestres de qualité partent. Il faut une veille réactive.
- **Doublons multi-agences avec des écarts de prix** : à Sainte-Foy-la-Grande, deux annonces pour 33 ha et 519 m² affichent 1,95 M€ et 1,85 M€. Cela laisse penser qu'il y a une marge de négociation.
- **Prix bas = travaux lourds** : le château d'Auch (675 k€, DPE G) et le domaine de Carcassonne (86 ha, « coquille vide ») en sont des exemples.

## 8. Points de doute / hypothèses non vérifiées

1. **Accès web** : WebFetch était en échec (DNS). Toutes les lectures sont passées par curl et une conversion texte maison. Des éléments chargés en JavaScript (dates de mise en ligne, photos) n'ont pas été vus.
2. **Pages actives ≠ biens disponibles** : une annonce encore en ligne peut être sous offre. Aucun contact n'a été pris, conformément aux règles.
3. **Données d'agrégateur** : French-Property reprend les données de Green-Acres et des agences. Plusieurs incohérences relevées :
   - Ygrande : 1 760 m² habitables sur French-Property, 1 425 m² sur ma-propriete et environ 1 500 m² pour le château seul dans le texte ;
   - Fougères (35) contre « Mayenne » dans le texte ;
   - « Périgueux » contre « près de Bordeaux » pour le château de mariage ;
   - Penne-d'Agenais : 37 ha en fiche, 40 ha dans le texte ;
   - Saône-et-Loire : « 39 ha » dans le titre, 32 ha en fiche, et « 5,5 ha en propriété + fermages » dans une autre annonce. Ce bien est exclu du CSV.
4. **CAPEX** : toutes les fourchettes sont des **ESTIMATIONS** sans visite ni diagnostic, fondées sur des ratios génériques : rafraîchissement 300-600 €/m², rénovation 1 000-1 500 €/m², restauration lourde 1 200-2 500 €/m², box 5-10 k€, carrière 40-80 k€, manège 150-400 k€. À faire valider par l'agent chargé du benchmark CAPEX ou par un professionnel.
5. **Montages SAFER** : l'exonération des droits d'enregistrement n'est explicitement écrite que sur l'annonce du haras du Pays d'Auge. Pour les autres biens Safer, c'est INCONNU. Les prix des autres annonces Safer sont affichés « HFS » (hors frais Safer, environ 8 à 10 % en sus selon le barème vu sur l'annonce normande).
6. **Sandillon** : le prix de 1,05 M€ « parts de SCI + reprise des emprunts » ne dit rien du montant de la dette reprise. Le coût économique réel est INCONNU et peut être proche de 2,4 M€.
7. **Non couverts** : Belles Demeures (403), Propriétés Le Figaro, Barnes, Sotheby's, Emile Garcin, Mercure Forbes en direct, Equirodi et Cheval Annonce. D'autres biens pertinents existent probablement. Exemple : un château de 59 ha à Nort-sur-Erdre (44) à 4 472 000 €, vu **seulement en EXTRAIT** sur Belles Demeures (page 403). Il pourrait être lié au Haras de Hus voisin : non vérifié.
8. **Marché haut de gamme cité en EXTRAIT seulement** : Haras de Fresnay-le-Buffard (61), 240 à 325 ha selon les sources, 26,8 M€ (2024). Statut actuel INCONNU.
9. **Notes de potentiel /10** : ce sont des jugements (ESTIMATION) qui pondèrent l'adéquation au projet cheval + château + autofinancement. Elles ne constituent pas une évaluation financière.
