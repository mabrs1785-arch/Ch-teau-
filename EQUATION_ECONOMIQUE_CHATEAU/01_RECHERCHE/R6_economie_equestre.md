# R6 — Économie équestre

Agent : R6. Démarré le 2026-10-14. Statut du fichier : EN COURS DE RÉDACTION (écrit au fur et à mesure).

Conventions : statuts PAGE LUE / EXTRAIT / ESTIMATION / HYPOTHÈSE / INCONNU (voir Contexte_permanent.md §6). Sources citées par identifiant [R6-xx], détaillées dans `sources/sources_R6.csv`. HT/TTC précisé pour chaque prix.

---

## Journal de recherche (compteur web)

| # | Outil | Requête / URL | Résultat utile |
|---|---|---|---|
| WS1 | WebSearch | IFCE OESC chiffres clés filière équine 2025 | lien vers le dépliant 2025 |
| WF1 | WebFetch | dépliant IFCE Chiffres clés 2025 (PDF, texte extrait localement avec pdftotext) | oui → [R6-01] |
| WS2 | WebSearch | réseau REFErences cas type écurie de pension centre équestre EBE | liens vers cas types et synthèses du Réseau Équin |
| WF2 | WebFetch | 2023_Synthese_nationale_Ecuries_de_Pension.pdf (Chambre d'agriculture Pays de la Loire) | non : HTTP 404 |
| WF3 | WebFetch | Cas-type EQCE3 compétition 2025 (PDF) | oui → [R6-02] |
| WF4 | WebFetch | Synthèse nationale Réseau Équin 2023 (données 2021, PDF) | oui → [R6-03] |
| WS3 | WebSearch | écurie pension tarifs 2025 Chantilly Fontainebleau Yvelines | peu utile ; lien délibération Bry-sur-Marne |
| WF5 | WebFetch | délibération Bry-sur-Marne 2025 (PDF) | oui → [R6-04] |
| WF6 | WebFetch | lagosniere.fr tarifs 2025-2026 | non : HTTP 404 |
| WF7 | WebFetch | polo-chantilly.com | non : domaine inexistant (ENOTFOUND) |
| WF8 | WebFetch | Annuaire ECUS 2023 (AQPS) | échec : > 10 Mo ; document téléchargé par curl puis lu → [R6-05] |
| WS4 | WebSearch | France Galop rapport annuel 2024 allocations primes | liens vers comptes sociaux 2025 et programme 2024 |
| WF9 | WebFetch | France Galop comptes sociaux 2025 (PDF) | oui → [R6-06] |
| WF10 | WebFetch | France Galop programme obstacles 2024 (PDF) | échec : > 10 Mo ; téléchargé par curl puis lu → [R6-07] |
| WF11 | WebFetch | letrot.com (accueil) | aucun lien vers rapport annuel ou chiffres clés |
| WF12 | WebFetch | arqana.com (accueil) | liens vers statistiques |
| WF13-14 | WebFetch | arqana.com/statistiques_annuelles.html | oui (2026) ; liens des années |
| WF15 | WebFetch | arqana.com …actions.php?annee=2025 | 302 sans suivi ; pages 2025 et 2024 récupérées par curl avec session → [R6-08] |
| WS5 | WebSearch | haras Normandie tarifs pension poulinière poulinage préparation yearling | peu utile ; extrait d'une fiche des Chambres d'agriculture |
| WF16-18 | WebFetch | fiches « pension reproduction » (Normandie, Hauts-de-France) | non : 503, 301 puis 404 |
| WF19-21 | WebFetch | arqana.com accueil, processus_de_vente.html, processus_d_achat.html | oui → [R6-09], [R6-10] |

---

## 1. Chiffres clés de la filière (IFCE-OESC, FFE)

Source principale : dépliant « Chiffres clés 2025 — Bilan statistique de la filière équine française — données 2024 » [R6-01], PAGE LUE (PDF ouvert via WebFetch, texte extrait localement avec pdftotext ; citations ci-dessous recopiées du texte extrait).

### 1.1 Effectifs, élevage, commerce

| Donnée | Valeur | Année | Citation exacte [R6-01] | Statut |
|---|---|---|---|---|
| Équidés en France | 995 700 | fin 2024 | « 995 700 ÉQUIDÉS EN FRANCE FIN 2024 » | PAGE LUE |
| Part chevaux de selle et poneys | 70 % | 2024 | « 70 % de chevaux de selle et poneys (y compris ONC) » | PAGE LUE |
| Lieux d'élevage | 21 331 (provisoire) | 2024 | « 21 331 LIEUX D'ÉLEVAGE EN 2024 » ; 75 % des élevages ont 1 ou 2 produits déclarés, 9 % plus de 5 | PAGE LUE |
| Lieux d'élevage sport-loisir | 8 297 (+1 %) | 2024 (p) | ligne « Sport-Loisir 6 711 8 297 1% » | PAGE LUE |
| Lieux d'élevage galop / trot | 1 614 (-4 %) / 2 847 (-6 %) | 2024 (p) | lignes « Galop 1 822 1 614 -4 % » et « Trot 3 415 2 847 -6 % » | PAGE LUE |
| Naissances (immatriculations) | 55 692 (-1 %) | 2024 (p) | « 55 692 immatriculations en France, toutes races confondues » ; sport-loisir 17 575 ; galop 6 316 ; trot 8 419 | PAGE LUE |
| Poulinières / étalons | 77 777 / 9 952 | 2024 | « 77 777 POULINIÈRES EN 2024 » ; « 9 952 ÉTALONS EN 2024 » | PAGE LUE |
| Changements de propriété (marché intérieur) | 86 837 (-2 %) | 2024 | « 86 837 ENREGISTREMENTS DE CHANGEMENTS DE PROPRIÉTÉ » ; sport-loisir 22 217 (-1 %) | PAGE LUE |
| Imports / exports d'équidés | 12 736 (+1 %) / 17 744 (-3 %) | 2024 | « 12 736 ÉQUIDÉS IMPORTÉS EN 2024 » ; « 17 744 ÉQUIDÉS EXPORTÉS EN 2024 » | PAGE LUE |
| Surfaces en herbe valorisées | 800 000 ha (+ 350 000 ha de fourrages) | enquête foncier 2023 | « 800 000 HA DE SURFACES EN HERBE VALORISÉES PAR LES ÉQUINS » | PAGE LUE |
| Détenteurs | ≈ 100 000, dont 2/3 particuliers | estimation IFCE | « 100 000 DÉTENTEURS EN FRANCE (ESTIMATION) DONT 2/3 SONT DES PARTICULIERS » | PAGE LUE |

### 1.2 Emplois et entreprises

| Donnée | Valeur | Année | Citation exacte [R6-01] | Statut |
|---|---|---|---|---|
| Emplois liés à la filière | 120 400 personnes | (décompte 2023, IFCE-OMEFFE) | « 120 400 PERSONNES EN EMPLOIS SALARIÉS, NON SALARIÉS » | PAGE LUE |
| dont production et utilisation du cheval | 54 328 | 2023 / 2022 | « DONT 54 328 PERSONNES EN LIEN AVEC LA PRODUCTION ET L'UTILISATION DU CHEVAL » | PAGE LUE |
| Sport/loisir : salariés, ETP salariés, employeurs, non-salariés | 21 212 salariés ; 10 929 ETP ; 5 719 employeurs ; 10 490 non-salariés ; total 31 702 | 2023 (non-salariés : 2022) | ligne « Sport/loisir 21 212 10 929 5 719 10 490 31 702 » | PAGE LUE |
| Élevage | 5 195 salariés ; 2 990 ETP ; 1 392 employeurs ; 9 019 non-salariés | 2023 / 2022 | ligne « Élevage 5 195 2 990 1 392 9 019 14 214 » | PAGE LUE |
| Courses (dont entraînement) | 6 319 salariés ; 3 979 ETP (entraînement : 5 134 salariés, 3 277 ETP, 847 employeurs) | 2023 | lignes « Courses 6 319 3 979 1 185 1 933 8 252 » et « dont entrainement 5 134 3 277 847 1 128 6 262 » | PAGE LUE |
| Offres d'emploi Equi-ressources | 2 493 ; 57 % en CDI ; 25 % palefrenier-soigneur | 2024 | « 2 493 OFFRES D'EMPLOI PUBLIÉES SUR ÉQUI-RESSOURCES EN 2024 » | PAGE LUE |
| Entreprises spécialisées | 31 856 (2022) ; 28 778 (2023 p) ; sport/loisir 13 379 (2022) puis 12 407 (2023 p) | 2022-2023 | « Près de 32 000 entreprises spécialisées en activités équines en 2022 dont 1/3 en élevage » | PAGE LUE |
| Chiffre d'affaires des entreprises équines | 6,2 Md€ (dont 40 % en Île-de-France) | 2023 (provisoire) | « Chiffre d'affaires des entreprises équines : 6,2 Mrds d'€ en 2023 (p) dont 40 % en Île-de-France » | PAGE LUE |

Lecture (ESTIMATION) : ratio sport/loisir ≈ 21 212 salariés pour 10 929 ETP, soit ≈ 0,52 ETP par salarié : beaucoup de temps partiels, d'apprentis et de saisonniers. 5 719 employeurs pour 10 929 ETP ≈ 1,9 ETP salarié par employeur : ce sont de très petites entreprises. Calcul : 10 929 / 21 212 = 0,515 ; 10 929 / 5 719 = 1,91.

### 1.3 Équitation (FFE, reprise par l'IFCE)

| Donnée | Valeur | Année | Citation exacte [R6-01] | Statut |
|---|---|---|---|---|
| Licences FFE totales | 648 254 (-4 % sur 2023/2024) ; 617 524 en 2019 | saison 2024 (01/09/2023-31/08/2024) | ligne « Total 617 524 648 254 -4 % » ; titre « Un nombre de cavaliers licenciés à nouveau en recul en 2024 » | PAGE LUE |
| dont Cheval / Poney / Tourisme | 286 162 (-1 %) / 293 101 (-7 %) / 68 991 (-4 %) | saison 2024 | lignes du tableau FFE | PAGE LUE |
| Établissements équestres adhérents FFE | 9 682 (stable) | 2024 | « Total 9 440 9 682 0% » | PAGE LUE |
| dont clubs dispensant l'équitation | 5 444 structures pour 560 052 licenciés | 2024 | « ils représentent 5 444 structures pour 560 052 licenciés en 2024 » | PAGE LUE |
| Compétition : organisateurs | 2 219 (-6 %) ; 2 507 en 2019 | 2024 | « Nombre d'organisateurs 2 507 2 219 -6 % » | PAGE LUE |
| Compétition : partants | 1 522 479 ; épreuves 125 468 | 2024 | « 1 522 479 partants en compétition en 2024 » | PAGE LUE |
| Gains distribués en compétition (FFE) | 32 581 363 € (-4 %) | 2024 | « Montants des gains distribués 32 390 516 32 581 363 -4 % » | PAGE LUE |
| Cavaliers avec licence compétition | 159 158 ; 78 % club, 20 % amateur, 2 % pro | 2024 | « 159 158 CAVALIERS ONT UNE LICENCE COMPÉTITION » | PAGE LUE |
| Part du CSO dans les partants | 81 % | 2024 | « Le CSO, 1ère discipline en nombre de partants » ; « CSO 81 % » | PAGE LUE |

Lecture (ESTIMATION) : 560 052 licenciés / 5 444 clubs ≈ 103 licenciés par club en moyenne. Gains moyens par partant ≈ 32,6 M€ / 1,52 M ≈ 21 € : la compétition FFE est massivement amateur, ses dotations ne font pas vivre un organisateur.

### 1.4 Courses (enjeux et encouragements) — voir aussi §5

| Donnée | Valeur | Année | Citation exacte [R6-01] | Statut |
|---|---|---|---|---|
| Enjeux paris hippiques (total) | 9 678 M€ (-2 %) | 2024 | « 9,7 Mrds € DE PARIS EN 2024 » ; ligne « Total ... 9 121 ... 9 678 ... -2 % » | PAGE LUE |
| Série des enjeux | 2019 : 9 121 ; 2020 : 7 802 ; 2021 : 8 827 ; 2022 : 9 644 ; 2023 : 9 833 ; 2024 : 9 678 (M€) | 2019-2024 | graphique « Total paris hippiques (en M€) » | PAGE LUE |
| dont internet | 1 566 M€ (16 % des mises) | 2024 | « 16 % DES MISES ENREGISTRÉES SUR INTERNET EN 2024 » | PAGE LUE |
| Encouragements (allocations) | 587 M€ (obstacle 89 ; plat 203 ; trot 294) | 2024 | ligne « Total 17 989 219 214 211 586 2% 513 587 1% » | PAGE LUE |
| Propriétaires de chevaux de course | 10 121 | 2024 | « 10 121 PROPRIÉTAIRES DE CHEVAUX DE COURSE EN FRANCE » | PAGE LUE |
| Chevaux à l'entraînement | 25 482 (galop 9 136 ; trot 16 346) | 2024 | « 25 482 CHEVAUX ENTRAÎNÉS » | PAGE LUE |
| Hippodromes actifs / réunions | 233 / 2 245 | 2024 | « 233 HIPPODROMES EN ACTIVITÉ EN 2024 » | PAGE LUE |

Lecture (ESTIMATION) : 587 M€ d'encouragements / 25 482 chevaux entraînés ≈ 23 000 € par cheval et par an en moyenne, toutes disciplines (moyenne très inégalement répartie). Calcul : 587 000 000 / 25 482 = 23 036 €.

## 2. Références économiques des entreprises équestres (Réseau Équin / Inosys)

### 2.1 Cas-type EQCE3 « Centre équestre tout public — Compétition », campagne 2025 [R6-02] — PAGE LUE

Nature du document : un cas-type n'est pas une moyenne. Citation : « Un cas-type n'est ni la moyenne des résultats observés au sein d'un groupe, ni le résultat de la meilleure exploitation » ; « les performances décrites sont favorables et souvent supérieures à la moyenne ». Méthode d'actualisation 2025 : « baisse de 3,5% sur les heures vendues et une augmentation de 4,5% sur le tarif des cours ».

Structure : « 180 clients • 3 UMO • 26 ha • 57 équidés • 60 clients/UMO » ; 27 boxes ; « un manège de 65*25 m » ; carrière 30 × 70 m éclairée ; 15 chevaux en pension (« 10 pension travail et 5 pension hébergement avec un cours par semaine ») ; 3 poulinières (élevage CSO). L'exploitant est cavalier professionnel, plus 2 salariés BPJEPS.

| Poste (€, campagne 2025) | Montant | Citation exacte |
|---|---|---|
| Produits totaux | 265 238 € | « Produits 265 238 € » |
| dont enseignement | 139 298 € | « Enseignement 139 298 € » |
| dont pensions (15 chevaux) | 85 533 € | « Pensions 85 533 € » |
| dont ventes − achats de chevaux | 23 058 € | « Ventes - achats 23 058 € » (dont « Vente de chevaux valorisés 24 885 € ») |
| dont aides / produits divers | 5 268 € / 9 651 € | « Aides 5 268 € » ; « Produits divers 9 651 € » |
| Charges opérationnelles | 72 755 € | « Charges opérationnelles 72 755 € » (fourrages 19 438 ; litière 9 335 ; maréchalerie 9 019 ; vétérinaire 6 655 ; concentrés 7 647) |
| Charges de structure hors amortissements et frais financiers | 134 548 € | dont « Salaires et chargs sociales 59 258 € », « Assurances 8 907 € », « Carburant 10 271 € », « MSA 5 067 € », « Fermage 3 348 € » |
| EBE | 57 935 € (22 % du produit) | « Excédent Brut d'exploitation (EBE) 57 935 € » ; « EBE/PB 22 % » |
| Annuités | 22 594 € | « Annuités 22 594 € » ; « Annuités/EBE 39 % » |
| Revenu disponible (= EBE − annuités) | 35 340 € pour 1 UMO exploitant | « Revenu disponible 35 340 € » |

Repères par équidé [R6-02] : « Produit total/équidé présent 4 653 € » ; « Charges opérationnelles équines/équidé présent 1 276 € » ; « Charges de structure hors amort. et F.F/équidé présent 2 360 € » ; « Produit total/UMO 88 412 € ».

Tarifs 2025 du référentiel [R6-02] (tous en € HT) :

| Prestation | EQCE1 (rural, jeunes enfants) | EQCE2 (péri-urbain, animation) | EQCE3 (péri-urbain, compétition) |
|---|---|---|---|
| Cours collectif (€ HT/h) | 17,1 | 17,1 | 19,4 |
| Stage (€ HT/h) | 12,5 | 15,9 | 14,8 |
| Pension pré (€ HT/mois) | 126 | — | — |
| Pension box hébergement (€ HT/mois) | — | 334 | 401 |
| Pension box + 1 cours hebdomadaire (€ HT/mois) | — | — | 457 |
| Pension box travail (€ HT/mois) | — | — | 568 |

Comparaison des 3 cas-types « centres équestres » 2025 [R6-02] (tableau 6) :

| Indicateur | EQCE1 | EQCE2 | EQCE3 |
|---|---|---|---|
| Surface | 26 ha | 8 ha | 26 ha |
| UMO | 1,2 | 2,3 | 3 |
| Clients | 100 | 200 | 180 |
| Équidés/UMO | 21 | 17 | 19 |
| Produit/UMO | 68 873 € | 86 737 € | 88 412 € |
| Produit pension/équidé en pension | 1 210 € | 3 347 € | 5 702 € |
| EBE/UMO exploitant | 39 756 € | 61 944 € | 57 935 € |
| EBE/produit | 48 % | 31 % | 22 % |
| Disponible/UMO exploitant | 27 829 € | 40 264 € | 35 340 € |

Référentiel de prix d'investissement [R6-02] (attention : le tableau est titré « Référentiels et produits 2019 utilisés pour la construction du cas-type », donc prix de base 2019 ; HT/TTC non précisé, probablement HT pour une entreprise agricole, HYPOTHÈSE) : « Manège 160 €/m2 » ; « Boxes 300 €/m2 » ; « Carrière extérieure 39 €/ m2 » ; « Marcheur (terrassement compris) 35 000 € » ; « Hangar de stockage 134 €/ m2 » ; « Fumière 100 €/ m2 » ; « Abris de pré 180 €/ m2 » ; « 1 poids lourd 10 places 50 000 € » (occasion implicite) ; « 1 van 2 places 8 300 € ».

Lecture pour le domaine (ESTIMATION) :
- L'EBE du cas-type (57 935 €) rémunère le travail de l'exploitant, qui n'est pas salarié dans les comptes : seules ses cotisations MSA (5 067 €) figurent. Après annuités, il reste 35 340 € pour un temps plein. Une telle structure **fait vivre son exploitant, elle ne dégage pas de surplus pour un tiers** (le château). Si le domaine devait salarier un responsable à la place de l'exploitant, l'essentiel de l'EBE serait absorbé.
- Le produit de pension moyen (85 533 € / 15 chevaux = 5 702 €/cheval/an ≈ 475 € HT/mois) est cohérent avec les tarifs affichés (401 à 568 € HT/mois).
- Manège de 65 × 25 m = 1 625 m² × 160 €/m² ≈ 260 000 € (base 2019, à réactualiser ; ESTIMATION).
- Ces cas-types ne concernent pas le haut de gamme : ce sont des structures péri-urbaines ou rurales ordinaires.

### 2.2 Synthèse nationale du Réseau Équin, données 2021 (88 exploitations suivies) [R6-03] — PAGE LUE

Biais à garder en tête (citation) : « les résultats technico‐économiques recherchés pour les fermes du Réseau Equin sont supérieurs à ce que l'on peut rencontrer habituellement sur le terrain ». Ce sont des exploitations sélectionnées notamment pour leur « viabilité économique ».

#### Centres équestres (21 suivis, 2021)

| Indicateur | Moyenne | Médiane | Citation |
|---|---|---|---|
| Clients | 168 | 182 | tableau « Caractéristiques structurelles des 21 centres équestres » |
| Main-d'œuvre totale (UMO) | 3,04 | 2,80 | idem |
| Équidés (dont pension) | 53 (19) | 53 (20) | idem |
| Produit total | 240 293 € | 183 819 € | « Produit total (€) 240 293 183 819 » |
| EBE | 75 713 € | 62 678 € | « EBE (€) 75 713 62 678 » |
| EBE/UMO exploitant | 56 207 € | 52 341 € | « EBE / UMO exploitant (€) 56 207 52 341 » |
| Revenu disponible/UMO exploitant | 36 985 € | 36 092 € | « Revenu disponible / UMO exploitant (€) 36 985 36 092 » |
| Annuités/EBE | 44 % | 27 % | « Annuités / EBE (%) 44 27 » |

#### Écuries de pension (26 suivies, 2021) : 13 « pensions travail » et 13 « pensions hébergement »

| Indicateur | Pension travail : moyenne / médiane | Pension hébergement : moyenne / médiane |
|---|---|---|
| Main-d'œuvre totale (UMO) | 3,09 / 2,25 | 2,39 / 2,50 |
| Équidés présents (dont en pension) | 46 / 33 (29 / 27) | 46 / 41 (28 / 25) |
| Surface totale | 41 ha / 32 ha | 55 ha / 31 ha |
| Produit brut total | 243 120 € / 200 380 € | 163 262 € / 160 250 € |
| Aides / produit brut | 11 % / 8 % | 12 % / 12 % |
| Produit pension par équidé en pension actif | 4 223 € / 3 504 € | 2 630 € / 2 409 € |
| Charges de structure hors amort. et FF par équidé présent | 2 836 € / 2 972 € | 1 449 € / 1 420 € |
| EBE/UMO exploitant | 42 104 € / 23 011 € | 40 145 € / 31 679 € |
| EBE/produit brut | 22 % / 25 % | 36 % / 36 % |
| Revenu disponible/UMO exploitant | **12 924 € / 9 437 €** | 23 955 € / 18 265 € |
| Annuités/EBE | **103 % / 70 %** | 47 % / 38 % |

Citations exactes [R6-03] :
- « Le niveau de charges est particulièrement élevé chez les pensions travail puisque l'EBE est inférieur à l'annuité. »
- « en pension travail, 1 UMO pour 15 équidés contre 1 UMO pour 19,4 équidés présents en pension hébergement ».
- « 60% des pensions travail ont recours à de la main‐d'œuvre bénévole ainsi que 70% des pensions hébergement ».
- « Une structure pension travail génère en moyenne 5 500 € par équidé et une structure hébergement 3 000 € par équidé. »
- Tarifs observés 2021, en € TTC par jour : « Pensions box sans travail 11 à 17 € » ; « Pension box travail 13 à 24 € » ; « Pension pré 5 à 12 € ».
- Charges de main-d'œuvre : « en moyenne 43 000 € en pension travail contre 15 000 € en pension hébergement ».

Conversion (ESTIMATION, 30,4 jours/mois) : box sans travail 11 à 17 € TTC/j ≈ 334 à 517 € TTC/mois ; box travail 13 à 24 € TTC/j ≈ 395 à 730 € TTC/mois ; pré 5 à 12 € TTC/j ≈ 152 à 365 € TTC/mois (données 2021).

#### Écuries d'entraînement de trotteurs (9 suivies, 2021) — référence « entraîneur »

- Structure : « 3,3 temps pleins dont 2,03 salariées pour 15 à 65 chevaux à l'entraînement » ; 41 équidés dont 33 au travail ; chevaux « en location (45 %) [...] en pension (40 %) et en propriété (15 %) ».
- Tarifs observés (€ HT/jour) : « Tarif Pension repos 8 à 15 € » ; « Tarif Pension pré entrainement 22 à 28 € » ; « Tarif Pension entrainement 25 à 32 € ».
- Résultats : produit total moyen 362 961 € ; « 97 000 € de chiffre d'affaires par unité de main‐d'œuvre » ; EBE/UMO exploitant 64 130 € (moyenne) / 43 941 € (médiane) ; EBE/PB 23 % / 20 % ; revenu disponible/UMO exploitant 22 201 € / 14 622 € ; annuités/EBE 74 % / 68 %.

#### Conclusion du Réseau Équin (citations) [R6-03]
- Centres équestres : « Ils parviennent à dégager un EBE/UMO exploitant médian de 52 341 € ».
- Pensions : « L'EBE/UMO exploitant médian des pensions travail est de 23 011 € et de 31 679 € en pension hébergement en 2021. »
- Trotteurs : « EBE/UMO médian de 43 941 € en 2021 ».

Lecture pour le domaine (ESTIMATION) :
- Les écuries de pension « professionnelles » sélectionnées par le réseau dégagent un revenu disponible médian de 9 437 € (pension travail) à 18 265 € (pension hébergement) par exploitant à temps plein, **avec du bénévolat** dans 60 à 70 % des cas. Pour un château qui salarierait tout le personnel, la pension standard est au mieux à l'équilibre : elle ne finance pas le bâti.
- Le seul levier de marge est le prix : il faut des pensions nettement au-dessus des 11 à 24 € TTC/j observés, donc un positionnement haut de gamme (voir §3) dont la demande reste à prouver localement.

## 3. Pension : prix, niveaux de service, demande

### 3.1 Prix observés (avec HT/TTC)

| Prix | Unité | HT/TTC | Périmètre | Année | Source | Statut |
|---|---|---|---|---|---|---|
| 126 | €/mois, pension pré | HT | cas-type rural EQCE1 | 2025 | [R6-02] | PAGE LUE |
| 334 | €/mois, pension box hébergement | HT | cas-type péri-urbain EQCE2 | 2025 | [R6-02] | PAGE LUE |
| 401 / 457 / 568 | €/mois : box hébergement / box + 1 cours hebdo / box travail | HT | cas-type péri-urbain EQCE3 | 2025 | [R6-02] | PAGE LUE |
| 11 à 17 | €/jour, box sans travail | TTC | 13 pensions hébergement du Réseau Équin | 2021 | [R6-03] | PAGE LUE |
| 13 à 24 | €/jour, box travail | TTC | 13 pensions travail du Réseau Équin | 2021 | [R6-03] | PAGE LUE |
| 5 à 12 | €/jour, pré | TTC | Réseau Équin | 2021 | [R6-03] | PAGE LUE |
| 8 à 15 / 22 à 28 / 25 à 32 | €/jour : repos / pré-entraînement / entraînement (trotteurs) | HT | 9 écuries d'entraînement de trotteurs | 2021 | [R6-03] | PAGE LUE |
| 591 | €/mois, « Hébergement et entretien du box » | non précisé dans la délibération ; tarif public aux particuliers, donc TTC présumé (HYPOTHÈSE) | centre équestre municipal de Bry-sur-Marne (Val-de-Marne, Île-de-France), concession UCPA | saison 2025-2026 | [R6-04] : « Tarif mensuel pension Hébergement et entretien du box 591 € » | PAGE LUE |

Hausse de tarifs votée à Bry-sur-Marne : « augmentation de 1,40% en moyenne » pour 2025-2026 [R6-04].

## 4. Commerce, élevage de chevaux de sport, ventes aux enchères

### 4.1 Prix d'achat des chevaux de selle (enquête IFCE-OESC, ≈ 5 000 questionnaires par semestre) [R6-05] — PAGE LUE

Citation : « Depuis 2012, l'Observatoire Economique et Social du Cheval de l'IFCE lance chaque semestre une enquête [...] Environ 5 000 questionnaires sont collectés lors de chaque enquête. » Prix en euros, HT/TTC non précisé (ventes surtout entre particuliers, donc sans TVA dans la plupart des cas : HYPOTHÈSE).

| Segment (2022) | Prix moyen | Q1 | Médiane | Q3 |
|---|---|---|---|---|
| Sport-loisir, toutes utilisations (n = 5 841) | 5 900 € | 2 000 € | 3 500 € | 6 600 € |
| Uniquement compétition (n = 447) | 14 300 € | 5 000 € | 10 000 € | 18 000 € |
| Polyvalent avec compétition (n = 1 134) | 11 100 € | 4 500 € | 8 500 € | 15 000 € |

| Selle Français achetés pour le CSO (2021-2022) | Prix moyen | Q1 | Médiane | Q3 |
|---|---|---|---|---|
| Tous âges (n = 1 890) | 14 100 € | 7 000 € | 11 000 € | 17 000 € |
| 3 ans (n = 194) | 13 100 € | 8 000 € | 10 400 € | 15 000 € |
| 4 à 6 ans (n = 717) | 15 300 € | 10 000 € | 14 000 € | 20 000 € |
| 7 et 8 ans (n = 284) | 17 600 € | 9 400 € | 13 500 € | 20 000 € |

Citation : « un quart des chevaux sont achetés entre 17 000€ et 150 000€ ».

### 4.2 Ventes aux enchères de chevaux de sport en France, 2022 [R6-05] — PAGE LUE

Périmètre : Fences Élite (Bois-le-Roi), Fences Sélection (Deauville et en ligne), Nash (Saint-Lô) ; les 7 ventes en ligne Fencesweb sont exclues. Prix d'adjudication en euros, HT/TTC non précisé.

| Catégorie | Vendus | Montant total | Prix moyen |
|---|---|---|---|
| Foals | 44 | 870 000 € | 19 773 € |
| 3 ans | 279 | 7 575 000 € | 27 151 € (-2 % sur 2021) |
| 4 ans et plus | 16 | 1 150 500 € | 71 906 € |
| Toutes catégories | 342 | 9 643 000 € | 28 196 € |
| dont Fences Élite | 167 | 5 663 500 € | 33 913 € |

Citation : « 342 chevaux de sport vendus aux enchères en 2022, essentiellement des 3 ans ». Prix maximaux : « Fences élite : prix max 150 000 euros » ; « NASH : prix max 105 000 euros ».

Lecture (ESTIMATION) : les enchères françaises de chevaux de sport représentent environ 9,6 M€ par an (2022), soit un marché étroit. Le prix médian d'un Selle Français de 3 ans acheté pour le CSO (10 400 €) est à comparer au coût de production d'un 3 ans (INCONNU à ce stade, à chercher : coût de saillie, pension de la jument, élevage du poulain sur 3 ans).

### 4.3 Ventes aux enchères de chevaux de course, 2022 [R6-05] — PAGE LUE

- Galop : « 3 279 galopeurs vendus aux enchères en 2022 » ; prix moyen toutes catégories 58 361 € (Arqana 61 242 € ; Osarus 10 981 €) ; « Arqana : Prix maximum = 2 100 000 euros ».
- Trot : « 1 691 trotteurs vendus aux enchères en 2022 à un prix moyen d'environ 14 200 €, stable par rapport à 2021 ».

## 5. Courses : enjeux, encouragements, primes (première partie)

### 5.1 Encouragements 2022 (FNCH, repris par l'IFCE) [R6-05] — PAGE LUE

Citation : « 558 millions d'euros d'encouragements en 2022 : une hausse de 11% ».

| Poste 2022 (€) | Plat | Obstacle | Trot | Total |
|---|---|---|---|---|
| Prix et allocations | 124 160 591 | 63 476 715 | 246 045 369 | 433 682 675 |
| Primes aux éleveurs | 16 737 333 | 10 703 150 | 29 908 290 | 57 348 773 |
| Primes aux propriétaires | 47 850 920 | — | — | 47 850 920 |
| Contributions diverses | 6 128 514 | 2 181 842 | 11 226 942 | 19 537 298 |
| Total | 194 877 358 | 76 361 707 | 287 180 601 | 558 419 666 |

Ratios (ESTIMATION, calcul sur le tableau) : primes aux éleveurs = 57,3 / 433,7 = 13,2 % des prix et allocations (plat 13,5 % ; obstacle 16,9 % ; trot 12,2 %). Primes aux propriétaires (galop) = 47,85 / 187,6 = 25,5 % des allocations de galop (plat + obstacle). Ce sont des ratios globaux, pas les taux réglementaires, qui dépendent du code des courses (voir §5.3).

### 5.2 Flux financiers des paris (2022) [R6-05] — PAGE LUE

- « Montant total des enjeux enregistrés en 2022 : 9 671 millions d'euros ».
- Répartition : « Part reversée aux parieurs gagnants 6 871 » M€ (71,0 %) ; « Net perçu par l'État 819 » M€ (8,5 %) ; « Net perçu par l'institution des courses 1 153 » M€ (11,9 % des enjeux).
- Fonds Éperon 2022 : « Financement des épreuves d'élevage et de sélection - SHF (en €) 3 200 000 ».

### 5.3 France Galop : comptes 2025 [R6-06] — PAGE LUE

Compte de résultat (k€) : « Produits PMU et PMH (note 21) 502 327 521 522 » (2025 / 2024) ; « Charges spécifiques encouragements à l'élevage (note 26) 270 515 283 481 » ; « Résultat net -11 688 -1 510 ».

Détail des encouragements (note 3.26, k€, 2025 / 2024) :
- « Prix et allocations 184 986 193 147 » ;
- « Primes propriétaires attribuées aux chevaux nés et élevés en France 48 958 52 003 » ;
- « Primes aux éleveurs 27 731 29 108 » ;
- « Transports chevaux (transporteurs, VP) 8 112 8 491 » ;
- « Total 270 515 283 481 ».

Série sur cinq ans (note 3.33, k€) : encouragements 2021 : 240 172 ; 2022 : 269 952 ; 2023 : 282 519 ; 2024 : 283 481 ; 2025 : 270 515. Enjeux « Premium » sur courses françaises : 2023 : 4 206 559 ; 2024 : 4 131 030 ; 2025 : 4 003 377. Résultat de l'exercice : 2023 : 7 136 ; 2024 : −1 510 ; 2025 : −11 688. Effectif : 383 salariés fin 2025.

Ratios (ESTIMATION) : en 2025, primes aux éleveurs = 27 731 / 184 986 = 15,0 % des prix et allocations ; primes aux propriétaires = 48 958 / 184 986 = 26,5 %. Les encouragements du galop baissent de 4,6 % en 2025 (283,5 → 270,5 M€) et les enjeux Premium sur courses françaises de 3,1 %. **Le revenu des courses dépend d'un financement par les paris qui se contracte.**

### 5.4 Taux réglementaires de la prime au propriétaire (galop) [R6-07] — PAGE LUE

Citations (programme officiel France Galop, février-mai 2024, p. 3) :
- « Une prime est versée aux propriétaires de chevaux nés et élevés en France ou assimilés » ; « Ce pourcentage sur les allocations hors primes est de : • 80 % pour les 2 et 3 ans • 55 % pour les 4 et 5 ans • 45 % pour les 6 ans et au-dessus ».
- « dans les courses de Groupe 1 & Groupe 1 PA la prime est fixée à 35 % quel que soit l'âge ».
- Obstacle : « Une prime de 15 % est versée aux propriétaires de pouliches de 3 et 4 ans, nées et élevées en France ».
- Plafonnement budgétaire : « chaque performance donnera lieu au versement d'un acompte de 90 % du montant théorique de prime ».

Taux réglementaire des primes aux éleveurs : INCONNU (non trouvé dans ce programme). Ordre de grandeur effectif : 15,0 % des allocations en 2025 [R6-06] (ESTIMATION). Vérification : code des courses au galop, chapitre « primes à l'élevage », sur france-galop.com.

Conséquence pour un domaine (ESTIMATION) : un propriétaire-éleveur de chevaux de galop nés en France cumule allocation, prime au propriétaire et prime à l'éleveur, mais la masse distribuée est fixe et en baisse. Le revenu par cheval est très concentré (voir la moyenne d'environ 23 000 € par cheval entraîné au §1.4, qui inclut les rares grands gagnants).

### 5.5 Ventes Arqana (pur-sang, Deauville et Saint-Cloud) [R6-08] — PAGE LUE

Montants en euros tels qu'affichés (« Ench. + Am. » = enchères + ventes amiables). HT/TTC et frais acheteur non précisés sur la page : prix d'adjudication présumés hors frais et hors TVA (HYPOTHÈSE à vérifier dans les conditions de vente Arqana).

| Année / vente | Présentés | Vendus (%) | Chiffre d'affaires (ench. + am.) | Prix moyen | Médiane |
|---|---|---|---|---|---|
| **Total 2024** | 3 986 | 3 036 (76,17 %) | 210 814 300 € | 67 761 € | 24 000 € |
| **Total 2025** | 4 064 | 3 168 (77,95 %) | 217 308 500 € | 66 317 € | 23 000 € |
| Total 2026 (au 14/10/2026, ventes d'octobre à décembre non encore tenues) | 1 551 | 1 162 (74,92 %) | 130 442 150 € | 109 636 € | 38 000 € |
| Yearlings d'août 2024 | 292 | 226 (77,4 %) | 50 577 000 € | 216 881 € | 140 000 € |
| La Vente d'Août 2025 (yearlings) | 272 | 216 (79,41 %) | 60 077 000 € | 266 884 € | 165 000 € |
| La Vente d'Août 2026 (yearlings) | 296 | 236 | 67 413 000 € | 277 682 € | 160 000 € |
| Yearlings v.2 2025 | 158 | 135 (85,44 %) | 3 850 500 € | 28 144 € | 25 000 € |
| Yearlings d'octobre 2025 | 764 | 599 (78,4 %) | 26 548 500 € | 42 337 € | 23 000 € |
| Yearlings de novembre 2025 | 119 | 103 (86,55 %) | 807 500 € | 7 752 € | 5 000 € |
| Vente d'Élevage (décembre) 2024 | 782 | 642 (82,1 %) | 55 801 500 € | 84 890 € | 26 000 € |
| Vente d'Élevage (décembre) 2025 | 862 | 667 (77,38 %) | 48 284 800 € | 70 761 € | 28 000 € |
| Vente d'Automne 2025 | 487 | 376 (77,21 %) | 13 391 000 € | 35 314 € | 16 000 € |

Lecture (ESTIMATION) :
- Le marché est très concentré. Un yearling « sélectionné » d'août 2025 vaut en médiane 165 000 €, mais la médiane tombe à 23 000 € en octobre et à 5 000 € en novembre. La moyenne de l'ensemble des ventes (66 317 €) est près de trois fois la médiane (23 000 €).
- Le prix d'un yearling ordinaire (20 000 à 25 000 € en médiane d'octobre) doit couvrir la saillie, la pension de la jument, le poulinage, l'élevage jusqu'à 18 mois, la préparation à la vente et la commission. Le coût de ces postes est à établir (voir §6), mais l'élevage commercial de pur-sang n'est rentable que pour une minorité de produits issus d'étalons chers.
- Les ventes en France sont concentrées à Deauville : un haras proche de Deauville bénéficie d'une logistique (préparation, transport court) que n'a pas un domaine éloigné.

### 5.6 Frais de vente aux enchères (Arqana) [R6-09] [R6-10] — PAGE LUE

- Vendeur : « Les frais de vente de 6% HT (TVA 20% en sus) » ; rachat (cheval non vendu) : 2 % HT + TVA sur le dernier prix d'adjudication ; droits d'inscription fixes (montant par vente, non affiché sur la page). La page mentionne encore une « TVA 19,6% » sur les droits d'inscription, taux abrogé depuis 2014 : **page partiellement ancienne**, à vérifier dans les conditions générales de la vente concernée.
- Acheteur : « Les frais d'achat sont fixés à 6% HT en sus du prix d'adjudication du lot acheté. » ; « Le prix d'adjudication est hors taxe. » ; TVA de 10 % pour les juments saillies, pouliches destinées à l'élevage, étalons et parts d'étalon ; 20 % pour les autres chevaux (chevaux à l'entraînement, yearlings, foals). « La TVA est appliquée sur le prix d'adjudication augmenté des frais d'achat. »
- Conséquence : les prix du §5.5 sont des prix d'adjudication **HT**. Pour un vendeur, le produit net d'un yearling vendu 23 000 € HT (médiane d'octobre 2025) ≈ 23 000 × (1 − 6 %) − droits d'inscription ≈ 21 600 € HT, avant transport et préparation (ESTIMATION).

## 6. Haras (pur-sang et sport) : services et étalons

### 6.1 Pension de poulinières

| Donnée | Valeur | Statut | Source |
|---|---|---|---|
| Pension de jument en haras/élevage | « de 9 €/jour pour une jument seule à 15 €/jour pour une jument suitée » (alimentation, litière, surveillance ; transport en sus) | EXTRAIT (document non daté, PDF inaccessible : 404/503) | [R6-11] |
| Pension poulinière dans un haras de pur-sang en Normandie (2025-2026, € HT/jour) | INCONNU | INCONNU | Vérification : grilles tarifaires de haras normands (demande de devis), ou syndicat des éleveurs (SEPEC) / AFAC |
| Forfait poulinage, préparation des yearlings aux ventes | INCONNU | INCONNU | idem ; à demander aux consignors des ventes Arqana |

