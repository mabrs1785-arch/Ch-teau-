# Analyse immobilière — Opération Château (Agent 1, chasse immobilière)

Date de travail : 2026-10-14. Fichier associé : `Domaines_identifies.csv` (20 fiches). Sources : `_brut/sources_agent1.csv` (42 entrées).

> **Avertissement de méthode, à lire en premier.** Pendant cette session, **WebFetch n'a pu ouvrir aucune page** (erreur DNS `ENOTFOUND` sur tous les domaines testés, y compris wikipedia.org). Le proxy de sortie refuse aussi `curl` (403). Toutes les fiches reposent donc sur les **extraits et résumés renvoyés par WebSearch** : aucune page n'a été lue en entier. Le statut de chaque fiche est « vu seulement en résultat de recherche ». Ensuite, le **quota WebSearch partagé (200 appels par tour, tous agents confondus) a été épuisé** pendant la recherche. Des pistes ouvertes n'ont donc pas pu être creusées (liste en fin de document). Chaque chiffre ci-dessous est un **FAIT SOURCÉ (extrait d'annonce)**, une **ESTIMATION** (hypothèse explicite) ou un **INCONNU**.

---

## 1. Méthodologie

1. **Pistes imposées** : 4 pistes ont été vérifiées en premier (Nort-sur-Erdre, Haras de Hus, Sévigny, Fresnay-le-Buffard).
2. **Recherches ciblées** (environ 40 requêtes) :
   - **Portails** : Belles Demeures, French-Property, ma-propriete.fr, Leggett/frenchestateagents, Barnes, Emile Garcin, Mercure Forbes, Patrice Besse, A Place in the Sun, Trovit.
   - **Mots-clés** : château + écuries, haras, domaine équestre, 40/50/60/100 ha.
   - **Régions** : Normandie, Pays de la Loire, Centre-Val de Loire, Bourbonnais, Limousin, Bourgogne, Charente/Vienne, Ain.
   - **Situations particulières** : ventes judiciaires, redressements, cessions de haras nationaux (IFCE), cessions à 1 € symbolique.
3. **Recoupement** : quand plusieurs agences publient le même bien (cas fréquent : mandats multiples), les chiffres ont été comparés. Les divergences sont conservées dans la colonne `contraintes` ou dans `bati_m2`.
4. **Classement** : il suit le **potentiel entrepreneurial** (note sur 10), pas la beauté du bien. Critères :
   - foncier utile au cheval (prairies plutôt que bois) ;
   - installations équestres déjà en place ;
   - capacité d'hébergement ou d'événementiel ;
   - prix compatible avec un levier (1 à 6 M€) ;
   - CAPEX probable ;
   - accessibilité et bassin de clientèle.
5. **CAPEX** : il s'agit d'**ESTIMATIONS non sourcées**, en ordre de grandeur, à valider par devis et diagnostic. Hypothèses utilisées :
   - rénovation légère : 200 à 600 €/m² ;
   - rénovation lourde ou création d'hébergement : 1 000 à 3 000 €/m² ;
   - création ou reprise d'écuries et carrière : 100 à 600 k€ selon l'ampleur.
   
   Les barèmes eux-mêmes n'ont pas été sourcés pendant cette session. Ils sont à confronter avec le travail des agents Benchmark et Financement.
6. **Aucun contact** n'a été pris (aucune agence, aucun vendeur, aucun formulaire).

## 2. État du marché (uniquement à partir des annonces trouvées)

### 2.1 Prix par hectare observés

Le prix par hectare est **calculé par moi** (prix affiché ÷ surface). Il mélange la valeur du bâti et celle du foncier : c'est un indicateur de comparaison, pas un prix de la terre.

| Bien | Prix affiché | Surface | Prix/ha (calcul) |
|---|---|---|---|
| Domaine avec manoir, Indre | 1 828 571 € | 176 ha | ≈ 10 k€/ha |
| Manoir et domaine, Vienne (Barnes) | 1 975 000 € | ~150 ha | ≈ 13 k€/ha |
| Château XVe, Aubusson (23) | ~1 360 000 € (converti) | 85 ha | ≈ 16 k€/ha |
| Domaine de chasse, Périgord | 1 840 000 € | ~100 ha | ≈ 18 k€/ha |
| Château XIXe, Gascogne | 795 000 € | 21,9 ha | ≈ 36 k€/ha |
| Propriété équestre, Ain | 3 105 000 € | 80 ha | ≈ 39 k€/ha |
| Haras, Sévigny (61) | 3 000 000 € | 70 ha | ≈ 43 k€/ha |
| Château, Blois-Amboise (41) | 2 120 000 € FAI | 42,42 ha | ≈ 50 k€/ha |
| Château et haras, Ygrande (03) | 2 650 000 € | 40 ha | ≈ 66 k€/ha |
| Château, Nort-sur-Erdre (44) | 4 472 000 € | 59 ha | ≈ 76 k€/ha |
| Château, Chabris (36) | 3 065 000 € | 40 ha | ≈ 77 k€/ha |
| Château, secteur Angoulême (16) | 3 150 000 € | 36,8 ha | ≈ 86 k€/ha |
| Château-hôtel et haras, Poitiers (86) | 10 300 000 € | 112 ha | ≈ 92 k€/ha |
| Haras de Hus (44) | 12 900 000 € | 128 ha | ≈ 101 k€/ha |
| Haras de Fresnay-le-Buffard (61), **vendu** | 26 000 000 € | 240 ha | ≈ 108 k€/ha |
| Manoir et 16 boxes, Argentan (61) | 2 100 000 € | 12,6 ha | ≈ 167 k€/ha |
| Château et 9 boxes, Pont-l'Évêque (14) | 4 950 000 € | ~8 ha | ≈ 620 k€/ha |

### 2.2 Ordres de grandeur

- **Château avec environ 40 à 85 ha** : les annonces trouvées vont de **~1,36 M€** (Aubusson, 85 ha, Creuse) à **4,47 M€** (Nort-sur-Erdre, 59 ha). Le centre de la fourchette se situe vers **2,5 à 3,2 M€** (Ygrande, Chabris, Angoulême, Sévigny pour un haras sans château). Sur les 8 biens « château ou haras ≥ 35 ha et < 13 M€ », la **médiane calculée est d'environ 76 k€/ha**, avec une très forte dispersion (16 à 101 k€/ha).
- **Facteurs de prix observés** :
  - **Localisation** : Normandie et Côte fleurie, périphérie de Nantes, Val de Loire.
  - **État** : un château rénové se vend plus cher.
  - **Notoriété équestre** : Hus, Fresnay.
  - **Part de bois** : un domaine majoritairement boisé se vend moins cher à l'hectare, mais il est moins utile pour les chevaux.
- **Haut de marché** (hors cible, pour mémoire) :
  - Haras de Hus : annoncé 20 M€ en décembre 2023, puis 21,2 M€ (sans les chevaux), puis **12,9 M€ chez Barnes en octobre 2024**.
  - Fresnay-le-Buffard : **vendu 26 M€ le 26/12/2024** à Al Wathba Stud.
  - Château de Cornod (Jura, 130 ha) : 25 M€ affichés.
- **Contre-exemple utile** (règle 8). Un château avec seulement 8 ha et 9 boxes près de Pont-l'Évêque est affiché 4,95 M€. Dans les zones les plus prisées, le prestige se paie sans foncier : un montage autofinancé y est structurellement plus difficile. De même, la baisse de prix de Hus (−35 à −40 % en moins d'un an, calcul sur les montants affichés) montre que **même les domaines équestres prestigieux peinent à trouver preneur** au prix demandé. C'est une opportunité de négociation pour l'acheteur, mais aussi un signal de liquidité faible à la revente.
- **Ventes judiciaires** (repère) : un château du XVIe sur l'Île Barbe (Lyon) a été mis à prix 600 000 € et adjugé 1,35 M€ en 2026, avec un programme de travaux estimé par la presse à 2 à 3,4 M€. La mise à prix basse ne préjuge pas du prix final.

## 3. Top 5 commenté

1. **Ygrande (Allier) — 2,65 M€, 40 ha, château 1835, 24 boxes, carrière couverte, 16 à 19 chambres** (note 8/10). C'est le seul bien trouvé qui réunit d'emblée **château, écurie, carrière couverte, hébergement et logements annexes** : maison de gardien, club-house, maison des cavaliers. La vente passe par la **Safer Auvergne-Rhône-Alpes**. Cela peut favoriser un projet agricole ou équestre porté par un jeune exploitant (à vérifier : critères d'attribution Safer, statut de jeune agriculteur). Points faibles :
   - 40 ha seulement, mais extensible par location de terres voisines ;
   - surfaces bâties divergentes selon les annonces (1 000 à 1 760 m²) ;
   - bassin de clientèle rural (Montluçon et Moulins, à distance non vérifiée).
2. **Sévigny (Orne) — 3 M€, 70 ha, 70 boxes** (note 7,5/10). C'est un outil d'élevage pur-sang qui revendique plus de 30 gagnants de Groupe, à proximité du Haras du Pin. Il offre le meilleur prix/ha équestre en Normandie dans les résultats (~43 k€/ha). **Il n'y a pas de château** (maison de maître de 346 à 700 m² selon les annonces) : la contrainte « vivre dans un château » n'est donc pas satisfaite. Option : l'intégrer à un montage « haras d'abord, château plus tard », ou le combiner avec une demeure voisine.
3. **Nort-sur-Erdre (Loire-Atlantique) — 4,47 M€, 59 ha, château 760 m² vendu meublé, 6 dépendances (422 m²)** (note 7/10). Le haras attenant (69,67 ha) est proposé séparément à 6,5 M€. **Hypothèse non vérifiée** : château et haras formeraient ensemble le Haras de Hus, vendu en un ou deux lots. Ce découpage rend possible une **acquisition en deux temps** (château et terres d'abord, haras plus tard via promesse ou location). C'est le prix le plus haut du top 5 pour le levier.
4. **Secteur Angoulême (Charente) — 3,15 M€, 36,8 ha + 7 ha loués, 13 chambres** (note 7/10). Un extrait d'annonce de 36,8 ha + 7 ha loués mentionne **16 boxes de 20 m² avec paddock chacun, une carrière de niveau professionnel et un marcheur**. Le rattachement de ces équipements à l'annonce 127-258295 est probable mais non certain. Pension haut de gamme possible dès l'acquisition, et la TGV Angoulême place Paris à environ 2 h (non vérifié dans cette session).
5. **Aubusson (Creuse) — ~1,36 M€, 85 ha, château XVe de 450 m², ferme, granges, boxes, piscine** (note 7/10). C'est le **ticket d'entrée le plus bas pour un château avec plus de 50 ha** (~16 k€/ha). Avec un apport de 250 k€ (scénario S2), c'est le seul bien du top 5 qui paraisse finançable par un montage classique (ESTIMATION). Points faibles : château petit pour l'hébergement, forte isolation, demande touristique et événementielle locale plus faible. Le prix est converti de la livre sterling par le site.

Biens suivants à surveiller : Chabris (château rénové, 40 ha, 3,07 M€), domaine de l'Indre (176 ha, 1,83 M€, manoir à rénover), manoir de la Vienne (~150 ha, 1,98 M€, données très partielles).

## 4. Typologie de domaine à rechercher (recommandation)

- **Foncier** : 40 à 80 ha, dont **au moins 60 % de prairies**. Un domaine très boisé (Blois-Amboise : 37 ha de bois sur 42) ou un domaine de chasse est peu utile aux chevaux, et le défrichement est réglementé.
- **Bâti** :
  - une demeure principale habitable (CAPEX bas sur le logement du porteur) ;
  - **des dépendances transformables en hébergement** : gîtes, chambres, logement de cavaliers ;
  - **au moins 15 à 25 boxes existants et une carrière**, un manège couvert étant un fort plus.
- **Exploitation** : idéalement, une **activité déjà en place** (pension, élevage, gîtes, événements). Elle donne des comptes historiques qui justifient la dette auprès d'une banque. Exemples trouvés : Ygrande (tourisme équestre), Chavanat (cabanes perchées), Tours réf. 4621 (hébergement et événements, mais 4 ha).
- **Prix** : 1,5 à 3,5 M€ affichés. Les trois baisses ou écarts de prix observés (Hus, versions multiples des annonces) suggèrent une marge de négociation, sans qu'elle soit chiffrable.
- **Protection** : préférer un bien **non classé MH**. Un bien inscrit ISMH (cas de Poitiers) peut ouvrir des aides, mais impose des contraintes de travaux et des délais.

## 5. Régions pertinentes pour le cheval (justification)

- **Normandie (Orne, Calvados, Manche)** : c'est le berceau de l'élevage. Haras du Pin, haras privés (Fresnay-le-Buffard, Sévigny), proximité de Deauville. **Revers** : prix par hectare élevé sur la Côte fleurie (Pont-l'Évêque : ~620 k€/ha calculés). L'Orne, autour d'Argentan, et le Sud-Manche sont plus abordables (Sévigny ~43 k€/ha ; château de 14,2 ha au Mont-Saint-Michel à 1,55 M€).
- **Pays de la Loire (Loire-Atlantique, Mayenne, Sarthe)** : présence de grands haras de sport (Hus) et proximité de Nantes, donc d'une clientèle de pension et d'événements. Prix élevés près de Nantes (Nort-sur-Erdre, Hus). La recherche Mayenne/Sarthe n'a remonté **aucun château de 40 ha** pendant cette session.
- **Centre-Val de Loire (Indre, Cher, Loir-et-Cher, Indre-et-Loire)** : grands domaines à prix intermédiaires (Chabris, Blois-Amboise, Chinon, Indre 176 ha), tourisme des châteaux de la Loire et accès depuis Paris. C'est le meilleur compromis apparent entre prix, foncier et attractivité événementielle (ESTIMATION fondée sur les annonces trouvées).
- **Bourbonnais / Allier et Limousin / Creuse** : prix par hectare les plus bas pour un château avec terres (Aubusson ~16 k€/ha, Ygrande ~66 k€/ha avec équipements). Il existe une tradition d'élevage (non sourcée dans cette session). **Revers** : bassin de clientèle faible et isolement, donc un risque commercial plus fort sur l'événementiel.
- **Charente / Vienne** : offre intermédiaire, avec des installations équestres (Angoulême, Poitiers) et de très grands domaines à faible prix par hectare (manoir de la Vienne ~150 ha).

> **Point non sourcé** : les statistiques d'effectifs équins par région (IFCE/SIRE) n'ont pas pu être consultées. Elles sont à vérifier sur ifce.fr, rubrique « chiffres clés de la filière ».

## 6. Biens adaptés à des montages atypiques

| Montage | Biens candidats | Pourquoi | Ce qu'il faut vérifier |
|---|---|---|---|
| **Acquisition en deux temps / découpage** | Nort-sur-Erdre et haras 4133-B (Hus) | Château et haras vendus séparément | Accepter une promesse ou une location du haras ; savoir si les lots sont bien du même domaine |
| **Location-gérance ou bail puis achat** | Haras de Sévigny, Haras de Hus | Vendeurs d'outils d'élevage, baisse de prix (Hus) | Volonté du vendeur (contact interdit dans cette mission) |
| **Crédit-vendeur** | Hus (baisse de prix), biens anciens en ligne (Gascogne MEG3893, Blois-Amboise) | Une longue durée sur le marché suggère un vendeur plus ouvert. C'est une hypothèse, pas un fait | Ancienneté réelle des annonces, historique des prix |
| **Rachat de société d'exploitation (fonds + murs)** | Château-hôtel de Poitiers (hôtel en place, 112 ha, 22 boxes), Tours réf. 4621 | Revenus existants, financement possible en LBO sur l'exploitation | Comptes, détention en SCI ou société, statut ISMH (Poitiers) |
| **Vente Safer / portage foncier** | Ygrande (vente via Safer AURA), Indre 176 ha | La Safer peut rétrocéder à un porteur de projet agricole ou équestre. Le foncier peut être porté par des investisseurs (GFA/GFV), l'exploitant n'achetant que le bâti | Cahier des charges Safer, éligibilité jeune agriculteur ; statut agricole des activités équestres (non vérifié ici) |
| **Vente judiciaire / procédure collective** | Aucun domaine équestre identifié en vente judiciaire ce jour | Mise à prix basse mais enchères concurrentielles (Île Barbe : 600 k€ → 1,35 M€) | Licitor, Avoventes, BODACC, ventes notariales (non consultables : WebFetch indisponible) |
| **Cession d'un site public** | Sites des haras nationaux : l'IFCE a voté en 2016 des cessions à des collectivités (Tarbes, Compiègne, Hennebont, Lamballe) et à la SOVAFIM ; le Haras du Pin a été proposé au département de l'Orne pour 1 € symbolique | Montage possible en **concession ou AOT** avec une collectivité, plutôt qu'en achat | Le rapport IFCE 2019 indiquait des cessions « quasiment à leur terme » : peu ou pas de stock disponible en 2026. À vérifier |

## 7. Points de doute / hypothèses non vérifiées

1. **Aucune page d'annonce n'a été ouverte** (WebFetch en erreur DNS sur tous les domaines). Les données proviennent des extraits WebSearch, que l'outil a pu résumer ou rattacher imparfaitement. **Les 20 fiches sont donc à re-vérifier sur la page source.** La disponibilité n'est confirmée pour aucune au 2026-10-14.
2. **Divergences entre annonces d'un même bien** :
   - Ygrande : 1 000, 1 425, 1 500 ou 1 760 m² ; 16 ou 19 chambres. Capifrance affiche un montant de 407 000 non qualifié.
   - Sévigny : 346, 460 ou 700 m² ; 9 ou 14 chambres ; 70 ou 73 ha.
   - Chabris : 21 ou 22 pièces.
   - Blois-Amboise : 10 ou 13 chambres.
   - Poitiers : 1 600 ou 1 712 m².
3. **Nort-sur-Erdre et Haras de Hus** : l'hypothèse qu'il s'agisse du même domaine vendu en lots (59 + 69,67 ha ≈ 128 ha) est une **déduction**, non confirmée. La FNAIM affiche 12,9 M€ pour l'ensemble, contre 4,472 + 6,5 = 10,97 M€ pour les lots séparés : l'écart reste inexpliqué.
4. **Angoulême** : le rattachement « 16 boxes / carrière pro / marcheur / 7 ha loués » à l'annonce 127-258295 (3,15 M€, 36,8 ha) est probable mais non certain.
5. **Chinon (25 ha, 1,3 M€)** et **Nevers (28 ha, 950 k€)** : ces fiches viennent de résumés agrégés. L'URL exacte de Chinon n'a pas été identifiée.
6. **Annonces probablement retirées ou anciennes** :
   - Blois-Amboise : version française marquée supprimée par l'agence ;
   - Poitiers : une des versions supprimée ;
   - Gascogne MEG3893 : mention de 2022 ;
   - Argentan 110 ha : supprimée par le propriétaire.
7. **Haras de Fresnay-le-Buffard** : il n'est plus à vendre (vendu 26 M€ fin 2024). Il est conservé comme **comparable**, pas comme opportunité.
8. **CAPEX** : toutes les fourchettes sont des **ESTIMATIONS** sans devis, sans visite et sans barème sourcé. Leur incertitude est d'un facteur 2 à 3.
9. **Prix par hectare** : ce sont des calculs personnels sur des prix affichés, pas des prix de transaction. Les prix réels (DVF) n'ont pas été consultés. À vérifier sur app.dvf.etalab.gouv.fr, par commune.
10. **Pistes non explorées faute de quota de recherche** :
    - « Château avec domaine et 74 hectares » (French-Property 3772-A3lk6y8cphxxtcy7) ;
    - chartreuse en Dordogne de 100 ha d'un seul tenant avec installations équestres (ma-propriete) ;
    - domaine équestre de 40 ha en Lot-et-Garonne ;
    - Licitor, Avoventes, enchères notariales, BODACC (procédures collectives de centres équestres et de domaines événementiels) ;
    - Equirodi, Cheval Annonce, Leboncoin, Green-Acres, Sotheby's France ;
    - « château 59 ha bois et zones humides » (lux-residence, prix non affiché).
11. **Contre-hypothèse (règle 8)** :
    - les biens les mieux équipés pour le cheval sont aussi les plus chers (Hus, Fresnay, Poitiers) ;
    - les biens à moins de 2 M€ avec plus de 50 ha sont des manoirs, des domaines de chasse ou des châteaux isolés (Creuse, Indre) ;
    - la baisse de 20 à 12,9 M€ du Haras de Hus montre une liquidité faible du segment.
    
    **Un domaine « château + 50 ha + écuries » à moins de 2 M€ dans une région à forte demande n'a pas été trouvé.**
