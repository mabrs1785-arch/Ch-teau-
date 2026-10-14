# R6 — Économie équestre

Agent : R6. Démarré le 2026-10-14. Statut du fichier : TERMINÉ (vague 1), 2026-10-14. Rédigé au fur et à mesure ; budget web : 15 WebSearch (quota atteint) et 59 appels WebFetch, plus des téléchargements directs par curl, signalés dans le journal : 4 réussis (2 PDF de plus de 10 Mo, refusés par WebFetch ; 2 pages Arqana derrière une redirection de session) et 2 en échec (erreur 503).

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
| WS6 | WebSearch | prix de saillie 2026 étalons France Etreham Siyouni | liens Aga Khan Studs |
| WF22-25 | WebFetch | agakhanstuds.com (article Bonneval, fiches Siyouni et Zarak, article fees 2026) | oui → [R6-12] à [R6-14] |
| WF26-30 | WebFetch | harasdejardy.com, /les-pensions/, plaquette JPG (×2, fichiers identiques) | oui, image lue visuellement → [R6-15] |
| WF31 | WebFetch | ffe.com (accueil) | aucun chiffre de licences |
| WS7 | WebSearch | pension chevaux taux de remplissage liste d'attente Île-de-France enquête IFCE | un seul résultat utile (rapport IFCE fin de vie) |
| WF32 | WebFetch | IFCE rapport Gestion fin de vie (PDF) | oui → [R6-16] |
| WS8 | WebSearch | budget Mondial du Lion subvention Maine-et-Loire | échec : aucun résultat pertinent |
| WS9 | WebSearch | chambre régionale des comptes Haras du Pin budget Grand Complet | indirect : Lamballe, Haras du Pin (Sénat, Acteurs publics) |
| WF33-34 | WebFetch | Haras de Lamballe point budgétaire 2025 (PDF) ; article Acteurs publics 2012 | oui → [R6-17], [R6-18] |
| WF35-37 | WebFetch | mondialdulion.com, /medias/, dossier de presse 2025 (PDF) | partiel → [R6-20] (pas de budget) |
| WS10 | WebSearch | Polo Club du Domaine de Chantilly cotisation, Deauville | liens poloclubchantilly.com |
| WF38-41 | WebFetch | poloclubchantilly.com /membership, /play (301), Dropbox Tarifs-2026 | partiel → [R6-21] ; fichier Dropbox supprimé |
| WS11 | WebSearch | centre de rééducation équine tarifs €/jour | échec : aucune grille ; fiches Chambres d'agriculture en 503/404 |
| WF42-43 (+ curl) | WebFetch | fiches pension travail chevaux de sport (Normandie, Hauts-de-France) | non : 503, 404 |
| WS12 | WebSearch | rhinopneumonie EHV-1 2021 annulation concours | oui |
| WF44-46 | WebFetch | préfecture Orne (503), préfecture Creuse (503), Around the Rings | partiel → [R6-22] |
| WS13 | WebSearch | coût de production poulain cheval de sport IFCE | oui |
| WF47 | WebFetch | IFCE OESC-4 Coûts de production (PDF 2011) | oui → [R6-24] |
| WS14 | WebSearch | appel à candidatures cavalier résident haras redevance par box | indirect : avis Ville de Paris (Cartoucherie) |
| WF48 | WebFetch | Ville de Paris, avis Cartoucherie 2021 (PDF) | oui → [R6-25] |
| WS15 | WebSearch | centre de reproduction équine tarifs pension jument suivi insémination | oui : monographie Haras du Rond Pré |
| WF49 | WebFetch | Monographie Haras du Rond Pré (PDF ; page 3 rendue en image et lue) | oui → [R6-26] |
| — | — | **Quota WebSearch atteint : 15/15. Suite uniquement en WebFetch.** | — |
| WF50 | WebFetch | chevaux-normandie.com/wp-content/uploads/2026/06/ | non : 403 |
| WF51-52 | WebFetch | equiup.chevaux-normandie.com (accueil) ; étude Covid 2020 (PDF) | oui → [R6-27] |
| WF53-56 | WebFetch | entreprendre.service-public (301 puis page F23567 ×2) ; moteur interne BOFiP | TVA équestre non traitée (aucune occurrence) ; BOFiP 404 |
| WF57 | WebFetch | entreprise.pmu.fr | non : 403 |
| WF58-59 | WebFetch | harasdehus.com ; page tarifs du centre de reproduction | oui → [R6-28] |

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

Haut de gamme proche de Paris — Haras de Jardy (Hauts-de-Seine) [R6-15], PAGE LUE (plaquette image mise en ligne en mars 2026) :
- Ligne « Pension de votre cheval au boxe Accès aux installations » : « Tarifs TTC Hauts-de-Seine 922.50 € » ; « Tarifs TTC Extérieurs 1002.71 € ». L'unité n'est pas écrite sur la plaquette : il s'agit très probablement d'un tarif mensuel (HYPOTHÈSE, cohérente avec les autres grilles).
- Inclus : « Des boxes de 16m² » ; « 6 carrières et 3 manèges » ; « Une piste de galop en sable » ; « Un accès direct à la forêt » ; paddocks drainés ; « 1 séance / semaine de 1 heure réservée aux propriétaires » avec encadrant ; accès mensuel à un parcours ; « - 50% sur le prix TTC » des activités du club.
- Le tarif différencié selon la résidence (Hauts-de-Seine ou extérieur) s'explique par le statut public du site (domaine départemental ; à vérifier, HYPOTHÈSE).
- Conversion HT (ESTIMATION) : 922,50 € TTC = 768,75 € HT si TVA à 20 % ; le taux applicable aux pensions doit être confirmé par R3.

Synthèse des niveaux de prix (ESTIMATION à partir des sources ci-dessus) :

| Niveau de service | Prix mensuel observé | Statut |
|---|---|---|
| Pré, zone rurale | ≈ 126 € HT (cas-type 2025) ; 152 à 365 € TTC (2021) | PAGE LUE / ESTIMATION (conversion) |
| Box « hébergement », zone rurale ou péri-urbaine | 334 à 401 € HT (cas-types 2025) ; 334 à 517 € TTC (2021) | PAGE LUE / ESTIMATION |
| Box, Île-de-France (centre municipal) | 591 € (TTC présumé) | PAGE LUE |
| Box « travail » (cheval monté par un professionnel) | 568 € HT (cas-type 2025) ; 395 à 730 € TTC (2021) | PAGE LUE / ESTIMATION |
| Box haut de gamme à 10 km de Paris, grandes installations | 922,50 à 1 002,71 € TTC | PAGE LUE |
| Pension haut de gamme à Chantilly, Fontainebleau ou Deauville | INCONNU (aucune grille publique trouvée) | INCONNU — vérifier par demande de devis ou annonces |

### 3.2 Pension retraite [R6-16] — PAGE LUE (enquêtes IFCE-OESC de juin 2019, synthèse publiée en 2021)

- Tarifs moyens observés (par mois, HT/TTC non précisé ; clientèle de particuliers, donc TTC probable : HYPOTHÈSE) : « Pré à l'année 160 € » ; « Pré été / rentré Hiver 220 € » ; « Rentré à l'année 320 € ». « Pour les propriétaires de chevaux en pension, les coûts sont plus élevés : principalement entre 200 et 400 € par mois. »
- Travail : « le temps moyen de travail mensuel par équidé est de 4,8 heures ».
- Marché : « Le chiffre d'affaires annuel dégagé par les chevaux à la retraite est estimé à environ 200 millions d'euros dont près de 50 millions issus des équidés en pension. » Projection : « environ 20 000 chevaux sont en pension et cet effectif devrait atteindre près de 40 000 animaux en 2030 ».

### 3.3 Preuves de demande : taux d'occupation et places vacantes

| Indicateur | Valeur | Citation | Statut | Source |
|---|---|---|---|---|
| Places de pension retraite inoccupées en France | ≈ 22 000 | « l'OESC estime que 4 500 établissements proposeraient de la pension retraite et 22 000 places seraient inoccupées » | PAGE LUE (enquête 2019 auprès de 165 dirigeants, taux de réponse 7 %) | [R6-16] |
| Vacance moyenne par structure | 5 places sur 30 à 35 (≈ 14 à 17 %, ESTIMATION) | « Les structures comptent en moyenne 30 à 35 places dont 5 sont vacantes. » | PAGE LUE | [R6-16] |
| Places supplémentaires prévues | + 6 000 | « 6 000 de plus seront disponibles dans des structures qui prévoient de proposer cette prestation » | PAGE LUE | [R6-16] |
| Comportement des propriétaires | proximité et fidélité | « Près de 90% sont à moins » d'une heure de trajet (phrase coupée dans le PDF) ; « 8 équidés sur 10 sont hébergés au domicile de leur propriétaire » (chevaux à la retraite) | PAGE LUE | [R6-16] |
| Listes d'attente de pensions haut de gamme (Île-de-France, Chantilly, Deauville) | INCONNU | — | INCONNU | Vérification : appels mystère auprès de 10 à 15 écuries cibles, annonces (leboncoin, Equirodi), comités régionaux d'équitation |
| Taux de remplissage des écuries de pension sport | INCONNU (le Réseau Équin donne les effectifs, pas la capacité) | — | INCONNU | idem |

Lecture (ESTIMATION) : en 2019, le marché de la pension « standard » n'est pas en pénurie au niveau national : l'offre excède la demande d'environ 15 %. Le client paie à proximité de son domicile (moins d'une heure). Un domaine éloigné d'une grande agglomération ne peut donc compter que sur une clientèle captée par un positionnement distinctif (installations exceptionnelles, encadrement de haut niveau, rééducation), et **aucune preuve publique de demande solvable n'a été trouvée pour ce segment haut de gamme**.

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

Lecture (ESTIMATION) : les enchères françaises de chevaux de sport représentent environ 9,6 M€ par an (2022), soit un marché étroit. Le prix médian d'un Selle Français de 3 ans acheté pour le CSO (10 400 €) est à comparer au coût de production d'un 3 ans (voir §4.2 bis : 9 440 € de coût de production et 7 700 € de prix de revient, référence d'avant 2011).

### 4.2 bis Coût de production d'un cheval de sport (référence ancienne) [R6-24] — PAGE LUE

Source : diaporama IFCE / Réseau Économique de la Filière Équine, journée du 19 janvier 2011 (données antérieures à 2011, **non actualisées**). Le coût de production inclut les charges opérationnelles, les charges de structure (amortissements et frais financiers) et la rémunération des terres, des capitaux propres et du travail de l'exploitant ; le prix de revient déduit les produits associés (gains, primes, saillies).

| « Exemple d'un élevage de chevaux de sport » | Coût de production | Produits annexes | Prix de revient |
|---|---|---|---|
| Poulain sevré | 4 960 € | 1 030 € | 3 930 € |
| Poulain 2 ans | 7 200 € | 1 390 € | 5 810 € |
| Poulain 3 ans | 9 440 € | 1 740 € | 7 700 € |
| Cheval 4 ans | 13 510 € | 2 020 € | 11 490 € |
| Valorisation par an | 4 080 € | 280 € | 3 800 € |

Citation de conclusion : « Les prix de vente sont trop souvent inférieurs au prix de revient, en particulier dans les exploitations spécialisés ».

Comparaison (ESTIMATION) : prix médian d'un Selle Français de 3 ans acheté pour le CSO en 2021-2022 = 10 400 € (moyenne 13 100 €) [R6-05], contre un prix de revient de 7 700 € **en euros d'avant 2011**. Les coûts (aliment, main-d'œuvre, énergie) ont augmenté depuis ; l'actualisation (indice IPAMPA) n'a pas été faite ici. La marge du naisseur médian est donc faible ou nulle ; seuls les produits du quart supérieur (Q3 = 15 000 € à 3 ans ; enchères Fences Élite à 36 058 € en moyenne pour les 3 ans en 2022) dégagent un surplus net.

### 4.3 Ventes aux enchères de chevaux de course, 2022 [R6-05] — PAGE LUE

- Galop : « 3 279 galopeurs vendus aux enchères en 2022 » ; prix moyen toutes catégories 58 361 € (Arqana 61 242 € ; Osarus 10 981 €) ; « Arqana : Prix maximum = 2 100 000 euros ».
- Trot : « 1 691 trotteurs vendus aux enchères en 2022 à un prix moyen d'environ 14 200 €, stable par rapport à 2021 ».

### 4.4 Location d'écuries et d'installations à des professionnels

| Donnée | Valeur | Citation / calcul | Statut | Source |
|---|---|---|---|---|
| Centre équestre de la Cartoucherie (Bois de Vincennes, Paris 12e) : redevance fixe minimale | 80 000 €/an (valeur au 1er janvier 2021), plus une redevance variable sur le chiffre d'affaires HT | « La redevance fixe forfaitaire annuelle perçue par la Ville de Paris ne pourra être inférieure à (quatre-vingt mille euros) 80 000 euros (valeur au 1er janvier 2021). » | PAGE LUE | [R6-25] |
| Installations louées | parcelle d'environ 3 300 m² ; « un manège d'environ 458 m² » ; « 25 boxes » intérieurs ; « 43 boxes extérieurs » ; « une carrière de 45 m x 20 m » ; un logement de 24 m² et un appartement de 55 m² | idem | PAGE LUE | [R6-25] |
| Durée | « une durée maximale de 10 ans » ; travaux d'entretien à la charge de l'occupant ; garantie financière égale à une année de redevance | idem | PAGE LUE | [R6-25] |
| Redevance fixe minimale par box | ≈ 1 176 €/box/an, soit ≈ 98 €/box/mois (80 000 / 68 boxes) | calcul | ESTIMATION (plafond : marché parisien intra-muros, le plus tendu de France) | [R6-25] |
| Loyer d'un box ou d'une écurie loué(e) à un cavalier professionnel dans un domaine rural (€/box/mois) | INCONNU | — | INCONNU | Vérification : annonces de location d'écuries (Equirodi, Cheval Annonce), notaires ruraux, SAFER ; attention au risque de requalification en bail rural (voir R3) |

Lecture (ESTIMATION) : même dans le site le plus attractif de France, un exploitant ne s'engage que sur environ 100 € par box et par mois de loyer fixe minimal, en prenant à sa charge l'entretien courant. Pour un château, la location d'écuries à un professionnel produit un revenu récurrent mais faible, sans commune mesure avec le coût d'entretien des bâtiments historiques qui les abritent. Le cas de Lamballe (§8.2) montre en outre que ces locataires partent facilement.

## 5. Courses : enjeux, encouragements, primes, ventes

### 5.1 Encouragements 2022 (FNCH, repris par l'IFCE) [R6-05] — PAGE LUE

Citation : « 558 millions d'euros d'encouragements en 2022 : une hausse de 11% ».

| Poste 2022 (€) | Plat | Obstacle | Trot | Total |
|---|---|---|---|---|
| Prix et allocations | 124 160 591 | 63 476 715 | 246 045 369 | 433 682 675 |
| Primes aux éleveurs | 16 737 333 | 10 703 150 | 29 908 290 | 57 348 773 |
| Primes aux propriétaires | 47 850 920 | — | — | 47 850 920 |
| Contributions diverses | 6 128 514 | 2 181 842 | 11 226 942 | 19 537 298 |
| Total | 194 877 358 | 76 361 707 | 287 180 601 | 558 419 666 |

Ratios (ESTIMATION, calcul sur le tableau) : primes aux éleveurs = 57,3 / 433,7 = 13,2 % des prix et allocations (plat 13,5 % ; obstacle 16,9 % ; trot 12,2 %). Primes aux propriétaires (galop) = 47,85 / 187,6 = 25,5 % des allocations de galop (plat + obstacle). Ce sont des ratios globaux, pas les taux réglementaires, qui dépendent du code des courses (voir §5.4).

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

Montants en euros tels qu'affichés (« Ench. + Am. » = enchères + ventes amiables). La page de statistiques ne précise pas HT/TTC, mais les conditions d'achat d'Arqana indiquent que « Le prix d'adjudication est hors taxe » [R6-10] : ces montants sont donc **HT**, hors frais acheteur (6 % HT) et hors TVA.

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

### 5.7 Enjeux 2022-2025 et divergences entre sources (conservées, non lissées)

| Indicateur | Source A | Source B | Commentaire |
|---|---|---|---|
| Enjeux hippiques totaux 2022 | 9 644 M€ (graphique du dépliant 2025) [R6-01] | 9 671 M€ (« Montant total des enjeux enregistrés en 2022 ») [R6-05] | Écart de 27 M€ entre deux publications IFCE (révision des données probable). |
| Encouragements du galop 2024 | 292 M€ (obstacle 89 + plat 203, source FNCH) [R6-01] | 283,5 M€ (charges d'encouragements de France Galop) [R6-06] | Périmètres différents : la FNCH inclut des sociétés de province et des contributions diverses ; les comptes de France Galop incluent le transport des chevaux. |
| Enjeux 2025 (total PMU, toutes sociétés) | INCONNU (site institutionnel du PMU bloqué, erreur 403) | Enjeux « Premium » sur courses françaises de France Galop : 4 003 M€ en 2025 contre 4 131 M€ en 2024 [R6-06] | Vérification : rapport annuel du PMU, ANJ, dépliant IFCE « Chiffres clés 2026 » attendu au printemps 2027. |
| Encouragements du trot 2025, primes LeTrot (taux) | INCONNU (aucun rapport trouvé sur letrot.com) | Trot 2024 : 294 M€ d'encouragements [R6-01] ; 2022 : primes aux éleveurs du trot 29,9 M€ pour 246,0 M€ d'allocations, soit 12,2 % [R6-05] | Vérification : comptes annuels de la SECF (LeTrot), code des courses au trot. |

## 6. Haras (pur-sang et sport) : services et étalons

### 6.1 Pension de poulinières

| Donnée | Valeur | Statut | Source |
|---|---|---|---|
| Pension de jument en haras/élevage | « de 9 €/jour pour une jument seule à 15 €/jour pour une jument suitée » (alimentation, litière, surveillance ; transport en sus) | EXTRAIT (document non daté, PDF inaccessible : 404/503) | [R6-11] |
| Pension poulinière dans un haras de pur-sang en Normandie (2025-2026, € HT/jour) | INCONNU | INCONNU | Vérification : grilles tarifaires de haras normands (demande de devis), ou syndicat des éleveurs (SEPEC) / AFAC |
| Forfait poulinage, préparation des yearlings aux ventes | INCONNU | INCONNU | idem ; à demander aux consignors des ventes Arqana |

### 6.1 bis Centre de reproduction (chevaux et poneys de sport) : Haras du Rond Pré, Grand Est, saison 2022 [R6-26] — PAGE LUE

Structure : « Stabulations et boxes pour l'accueil de 70 chevaux » ; « 1 manège (40 x 20 m) » ; « 2 carrières » ; « 96 ha de surface agricole utile » ; « 2,8 temps plein au total dont 1,8 UMO exploitants et 1 UMO salarié ». Activité : « 179 juments ont été inséminées [...] dont 74 % de juments gestantes » ; « 169 juments à la reproduction accueillies sur la saison, confiées par 76 clients » ; « 25 chevaux et poneys en pension à l'année ». Clientèle : « 1/3 d'éleveurs professionnels 2/3 d'éleveurs amateurs ».

« ZOOM : TARIFS DES PRESTATIONS (2022) » — « Tarifs de la pension élevage par jour » :

| Catégorie | Au pré | Au box |
|---|---|---|
| Ponettes non suitées | 5,73 € HT (6,3 € TTC) | 10,91 € HT (12 € TTC) |
| Ponettes suitées | 6,68 € HT (7,35 € TTC) | 12,41 € HT (13,65 € TTC) |
| Juments non suitées | 7,18 € HT (7,9 € TTC) | 11,91 € HT (13,1 € TTC) |
| Juments suitées | 8,09 € HT (8,9 € TTC) | 13,36 € HT (14,7 € TTC) |

« Mise en place et suivi gynécologique (facturé par le vétérinaire) » : « Mise en place en IAF, IART ou IAC 145 € HT (159,90 € TTC) » ; « Forfait gynécologique IAF : 115 € HT (126,50€ TTC) ; ART ou IAC : 145 € HT (159,50 € TTC) ; IAC avec suivi renforcé : 180 € HT (198 € TTC) ». Le rapport TTC/HT ≈ 1,10 indique une **TVA à 10 %** sur ces prestations (ESTIMATION par calcul : 6,3 / 5,73 = 1,099).

Investissement de création (2007) : « Total investissement 35 000 € » (laboratoire et salles 15 000 € ; mannequin 8 000 € ; microscope 3 000 € ; barre d'insémination 2 500 € ; 4 cuves 4 000 €). Consommables ≈ 1 000 €/an ; azote 1 200 €/an.

Résultats (exploitation entière, saison 2022) : « Produit brut total 149 077 € » ; « Produit brut/UMO 53 241 € » ; « Charges Opérationnelles 28 751 € » ; « Charges de structure 45 877 € » ; « EBE 74 449 € » ; « EBE/PB 50 % ».

Contraintes citées : « Astreinte quotidienne sur 6 mois et très intensive sur 3 mois (avril, mai, juin), parfois 48 juments à l'échographie soit 4 heures de travail » ; « Les vétérinaires qui réalisent le suivi gynécologique des juments sont rares ».

Lecture (ESTIMATION) :
- Les juments extérieures restent « en moyenne 25 jours » : 169 juments × 25 jours × 11,91 à 13,36 € HT/jour au box ≈ 50 000 à 56 000 € HT de pension de reproduction par saison (calcul). C'est un complément, pas un moteur, mais avec une bonne marge (EBE/PB de 50 %) et un investissement faible (35 000 €).
- Facteur clé : un vétérinaire disponible et un étalon sur place. Le modèle demande la présence de l'exploitant 6 mois par an ; il ne convient pas à un propriétaire qui veut déléguer.

### 6.1 ter Second point de comparaison : Haras de Hus (Petit-Mars, Loire-Atlantique), grille actuelle [R6-28] — PAGE LUE

Mention : « Tous les tarifs affichés sont hors taxe » ; année non écrite dans le texte (le fichier image des tarifs porte « 2026 »).
- Pension : « Pension pré - paddock collectif : 13,5 €/jour » ; « Pension box - paddock individuel : 18€/jour » ; « Pension box - paddock individuel pour jument suitée : 21 €/jour » ; « Surcoût copeaux : 2 €/jour » (HT).
- Insémination : « lAR : 195 € » ; « lAC ou lARR : 315 € » (HT).
- Embryons : « Récole et transfert d'embryon : 355 € » ; « Location jument porteuse confirmée pleine à 45 jours : 3000 € » ; à 60 jours avec embryon sexé : 3 300 € (HT).
- Divergence avec le Rond Pré (2022, Grand Est) : pension au box de 11,91 à 13,36 € HT/jour contre 18 à 21 € HT/jour ici. L'écart tient à l'année (2022 contre 2026 probable), à la région et au niveau de service (paddock individuel). Les deux valeurs sont conservées.

### 6.2 Prix de saillie des étalons de pur-sang en France (2026)

| Étalon (haras) | Tarif 2026 | Conditions | Citation | Statut | Source |
|---|---|---|---|---|---|
| Siyouni (Haras de Bonneval, Calvados) | 150 000 € | « 1/10 SLF » (paiement au 1er octobre, poulain vivant : HYPOTHÈSE sur le sens de l'abréviation) | « Stallion fee 2026: €150,000 (1/10 SLF) » ; « Standing at Haras de Bonneval » | PAGE LUE | [R6-12] |
| Zarak (Haras de Bonneval) | 80 000 € | « 1/10 SLF » | « Stallion fee 2026: €80,000 (1/10 SLF) » | PAGE LUE | [R6-13] |
| Vadeni | 15 000 € | — | « will stand at a fee of €15,000 next season » | PAGE LUE | [R6-14] |
| Erevann | 8 000 € | — | « will remain at €8,000 » | PAGE LUE | [R6-14] |
| Sea The Stars (Irlande, pour comparaison) | 300 000 € | — | « he will stand for a fee of €300,000 in 2026 » | PAGE LUE | [R6-14] |

HT/TTC : non précisé sur les pages. Les saillies vendues en France par un assujetti sont soumises à la TVA ; la mention « hors TVA » est usuelle mais non vérifiée ici (HYPOTHÈSE).

Lecture (ESTIMATION) : l'économie d'une station d'étalons de pur-sang repose sur la possession (ou la syndication) d'un étalon de premier plan, dont la valeur se chiffre en millions. Ce n'est pas un modèle accessible à un domaine qui démarre : un étalon à 8 000 € la saillie, avec un nombre de juments INCONNU (à vérifier : statistiques de monte IFCE-SIRE par étalon), produit un chiffre d'affaires modeste face au risque (fertilité, mode, mortalité).

### 6.3 Services à forte valeur : rééducation, cliniques, quarantaine et export, transport, « hôtels à chevaux »

| Service | Donnée trouvée | Statut | Vérification proposée |
|---|---|---|---|
| Centre de rééducation (tapis aquatique, balnéothérapie, rééducation post-opératoire) : tarifs €/jour | aucune grille publique trouvée (une recherche dédiée n'a rien donné) | INCONNU | Demande de grille aux centres existants ; vétérinaires équins référents ; cliniques (CIRALE, cliniques privées) |
| Clinique vétérinaire | non étudié faute de source chiffrée ; activité réglementée réservée aux vétérinaires | INCONNU | Ordre des vétérinaires ; modèle de location de locaux à une clinique |
| Centre de reproduction | données réelles : Haras du Rond Pré (EBE 74 449 €, 50 % du produit) [R6-26] ; Haras de Hus (pension 13,5 à 21 € HT/jour) [R6-28] | PAGE LUE | voir §6.1 bis et §6.1 ter |
| Quarantaine et export | flux : « 17 744 ÉQUIDÉS EXPORTÉS EN 2024 » et 12 736 importés [R6-01] ; tarifs de quarantaine : aucun | PAGE LUE (flux) / INCONNU (prix) | Transporteurs agréés, DDPP, centres de collecte agréés pour l'export |
| Transport | France Galop paie 8,1 M€ de transport de chevaux en 2025 (« Transports chevaux (transporteurs, VP) 8 112 ») [R6-06] ; tarifs €/km : aucun | PAGE LUE (masse) / INCONNU (prix) | Grilles de transporteurs ; poids lourd 10 places à 50 000 € (référentiel 2019) [R6-02] |
| « Hôtel à chevaux » (étape, hébergement court lors d'événements) | aucune donnée | INCONNU | Organisateurs d'événements voisins (location de boxes à la nuitée) |

Lecture (ESTIMATION) : ces services ont une valeur unitaire plus élevée que la pension simple, mais ils reposent sur des **compétences rares et réglementées** (vétérinaires, inséminateurs, transporteurs agréés). Le Réseau Équin le dit pour la reproduction : « Les vétérinaires qui réalisent le suivi gynécologique des juments sont rares » [R6-26]. Pour un domaine, la voie réaliste est d'**héberger** un professionnel (bail ou convention), pas d'exploiter soi-même. Aucune preuve de demande solvable n'a été trouvée pour la rééducation ou l'hôtellerie équine.

## 7. Événements équestres

### 7.1 Ordres de grandeur nationaux (FFE, via IFCE) [R6-01]
- 2 219 organisateurs de compétitions en 2024 (2 507 en 2019) ; 125 468 épreuves ; 1 522 479 partants ; 32 581 363 € de gains distribués.
- ESTIMATION : 32,6 M€ / 2 219 organisateurs ≈ 14 700 € de dotations distribuées par organisateur et par an en moyenne ; 1 522 479 / 2 219 ≈ 686 partants par organisateur et par an.
- Réseau Équin 2021 [R6-03] : dans les écuries de « pension travail », le poste « Montant organisation de concours » vaut en moyenne 7 237 € par an (134 € en pension hébergement) : **l'organisation de concours est un produit d'appoint, pas un moteur**.

### 7.2 Cas réel : concours d'élevage au Haras national de Lamballe (Côtes-d'Armor), 2025 [R6-17] — PAGE LUE
- Après le « désengagement de l'association de la sté de concours hippique de Lamballe », le syndicat mixte a organisé lui-même 3 concours d'élevage + 1 CIR, en recrutant un coordinateur équestre en CDD.
- Volumes : « Du 24 au 27 mars -> 118 boxes Haras + 87 boxes parc -> 998 engagés » ; « 3076 engagés - 4 compétitions saison 2025 ».
- Le CDD « concours » n'est pas renouvelé pour 2026, « en raison de la reprise de l'organisation des concours par la société de concours pour 2026 ».
- Montant des recettes d'engagement : INCONNU (non détaillé dans le document).

### 7.3 Grands événements (Mondial du Lion, Pau, Haras du Pin, Chantilly, Saut Hermès, Dinard)

Mondial du Lion (Le Lion-d'Angers, parc départemental de l'Isle-Briand), dossier de presse 2025 [R6-20], PAGE LUE : « Chaque année, 45 000 spectateurs » ; « EN 2025 LE MONDIAL C'EST : 25 NATIONALITÉS 125 CHEVAUX AU DÉPART » ; le Crédit Mutuel « devient partenaire titre de l'événement ». Budget, dotation et subventions : non publiés dans le dossier (INCONNU).

Budgets, recettes, subventions : INCONNU à ce stade (une recherche dédiée au Mondial du Lion n'a rien donné). Vérification : délibérations des conseils départementaux (Maine-et-Loire, Orne, Pyrénées-Atlantiques, Ille-et-Vilaine), rapports d'activité des associations organisatrices, registre des comptes des associations subventionnées (journal-officiel.gouv.fr, comptes annuels des associations recevant plus de 153 000 € de subventions).

### 7.4 Polo : Polo Club du Domaine de Chantilly [R6-21] — PAGE LUE
- « Le Polo Club du Domaine de Chantilly compte en 2023, 155 membres actionnaires » ; la page mentionne aussi 396 joueurs licenciés à la Fédération française de polo (citation complète non relevée).
- Le club fonctionne par actions : les membres détenant plus de 49 actions bénéficient de « 15 % de réduction sur les pensions de chevaux » (chevaux installés en permanence) ou de 5 % (présence partielle).
- « Cotisation stick and ball à l'année: 1200€ » (HT/TTC non précisé ; accès aux terrains en herbe).
- Prix de l'action, cotisation annuelle et pension des poneys de polo : INCONNU (la grille « Tarifs 2026 » liée sur Dropbox a été supprimée). Vérification : secrétariat du club.
- Deauville : INCONNU (aucune donnée trouvée).

Lecture (ESTIMATION) : le polo de Chantilly est un club d'actionnaires adossé au domaine de l'Institut de France. Ce modèle suppose une communauté de joueurs fortunés déjà présente (Chantilly, Deauville, région parisienne) ; il n'est pas transposable à un domaine isolé sans une telle base de clientèle.

## 8. Risques

### 8.1 Épizootie de rhinopneumonie (EHV-1), 2021
- La FEI a annulé les concours internationaux « with immediate effect and until 28 March 2021 » dans « 10 countries on the European mainland » (France, Espagne, Portugal, Belgique, Italie, Autriche, Pologne, Pays-Bas, Allemagne, Slovaquie). Selon la FEI, la souche « has already caused equine fatalities and a very large number of severe clinical cases » [R6-22], PAGE LUE.
- France : un communiqué commun FFE-SHF du 15 mars 2021 aurait prolongé la suspension des compétitions nationales et internationales et des rassemblements jusqu'au 11 avril 2021 inclus, la France étant présentée comme le deuxième pays le plus touché après l'Espagne [R6-23], EXTRAIT (PDF préfectoral inaccessible, erreur 503).
- Pertes économiques chiffrées (organisateurs, cavaliers, pensions) : INCONNU. Vérification : RESPE, IFCE-OESC, rapports d'activité FFE 2021.
- Conséquence pour un domaine (ESTIMATION) : une épizootie supprime d'un coup les recettes d'événements et peut imposer une quarantaine à une écurie de pension (aucun mouvement de chevaux). Ce risque se modélise par une perte de **4 à 8 semaines d'activité événementielle** et un surcoût sanitaire (HYPOTHÈSE fondée sur la durée de la suspension de 2021 : fin février au 11 avril).
- Le cas-type 2025 décrit des pratiques de prévention : vaccination « contre la grippe, le tétanos et la rhinopneumonie » et quarantaine de 15 jours à l'achat [R6-02].

### 8.1 bis Choc de type 2020 : trajectoires des entreprises équines normandes [R6-27] — PAGE LUE

Échantillon : entreprises normandes avec exercices 2018, 2019 et 2020 complets ; comparaison du produit 2020 à la moyenne 2018-2019. Citations :
- Écuries de pension : « Le produit des écuries de pension est similaire en 2020 par rapport à la moyenne 2018/2019. Les pensions subissent même une augmentation de 10% » ; « le confinement aura eu peu d'impacts sur cette activité ; les propriétaires ayant laissé leurs chevaux en pension ».
- Centres équestres : « les centres équestres accusent un déficit de chiffre d'affaires de 15% » ; mais « la rentrée de septembre 2020 a connu une hausse de 17% des licenciés FFE en Normandie ».
- Entraîneurs de trotteurs : « Les gains de courses ont baissé de 25% » ; saillies « avec une tendance à -35% » ; pensions maintenues.
- Éleveurs de trotteurs : « Les gains de courses ont perdu 15%, les produits des saillies chutent de 30% et on observe même une baisse de 10% des pensions ».
- Éleveurs de chevaux de sport : produits en hausse grâce aux ventes de chevaux, interprétées comme « probablement plus d'une stratégie de défense que d'un regain d'activité ».

Lecture (ESTIMATION) : pour le modèle de stress, la pension se comporte comme un **revenu contractuel quasi récurrent** (variation de 0 à +10 % en 2020), l'enseignement comme un revenu semi-récurrent (−15 %), et les courses et saillies comme des revenus cycliques (−25 à −35 %).

### 8.2 Volatilité des cavaliers et écuries résidents (cas du Haras de Lamballe, 2025) [R6-17] — PAGE LUE
- « Départ de plusieurs résidents équestres » en 2025 : « Ecurie d'Armor 5 équidés », « Gwendal Balan 3 équidés », « Ecurie Fournier Laroque 7 Equidés » ; « Au 21/10 : plus qu'une 1 résidente équestre sur le site ».
- Fin de l'activité d'étalons : « Les 3 étalons bretons ont quitté le site en fin d'année 2024, marquant ainsi la fin de l'activité de l'étalonnage au haras ».
- Fréquentation touristique : « La saison touristique de juillet et août s'est traduite par une baisse de 21 % de la fréquentation » ; sur 14 visites thématiques programmées pour le bicentenaire, « seules trois ont pu être maintenues, faute de réservations ».
- Résultat : « Le Résultat prévisionnel de fonctionnement au titre de 2025 est Déficitaire de 130 673 € ».
- Lecture : un haras patrimonial qui loue des écuries à des professionnels, organise des concours et ouvre à la visite reste déficitaire. Les écuries résidentes partent sans préavis long (fin de contrat, situation familiale, transfert d'activité).

### 8.3 Contraction du financement des courses [R6-06]
Encouragements du galop : −4,6 % en 2025 ; résultat net de France Galop : −11,7 M€ en 2025 ; enjeux Premium sur courses françaises en baisse depuis 2022 (4,49 → 4,00 Md€). Un modèle « propriétaire-éleveur de chevaux de course » dépend d'une ressource publique-parapublique en recul.

### 8.4 TVA (à confirmer par R3)
Les taux appliqués aux pensions, à l'enseignement et à la vente de chevaux conditionnent la comparaison HT/TTC des tarifs ci-dessus. L'éditorial de l'Annuaire ECUS 2023 évoque « la bonne nouvelle de la baisse du taux de TVA » [R6-05], sans détail. Les frais Arqana appliquent 10 % (juments saillies, étalons, parts) ou 20 % (autres chevaux) [R6-10]. La grille 2022 du Haras du Rond Pré fait apparaître un rapport TTC/HT de 1,10 sur la pension de reproduction et le suivi vétérinaire, donc une TVA à 10 % sur ces prestations [R6-26] (ESTIMATION par calcul). La fiche officielle des taux de TVA (entreprendre.service-public.gouv.fr, F23567, « Vérifié le 18 juin 2025 ») ne mentionne ni les équidés ni les activités équestres (vérifié par WebFetch). Taux applicable en 2026 aux pensions de chevaux de loisir et à l'enseignement : INCONNU ici, **à confirmer par R3**. Conséquence : les conversions TTC → HT de ce fichier sont données à 20 % (hypothèse prudente) et à 10 % ou 5,5 % en variante.

## 9. Livrable : tableau des modèles équestres

Lecture : « revenu » = chiffre d'affaires par cheval ou par box et par an ; « marge » = indicateur publié (EBE/produit, revenu disponible) ou ESTIMATION ; tous les EBE publiés **excluent la rémunération de l'exploitant**, sauf mention contraire.

| # | Modèle | Revenu par cheval ou box (an) | Marge | Personnel | Investissement | Récurrence | Preuves de demande | Sources |
|---|---|---|---|---|---|---|---|---|
| 1 | Pension « hébergement » standard (rural ou péri-urbain) | 2 630 € (moyenne 2021, produit pension par équidé) ; 4 008 à 4 812 € HT au tarif 2025 (334 à 401 € HT/mois) | EBE/produit 36 % ; revenu disponible médian 18 265 €/UMO exploitant (2021) ; 60 à 70 % des structures ont du bénévolat | 1 UMO pour 19,4 équidés | boxes 300 €/m², carrière 39 €/m², manège 160 €/m² (base 2019) | Haute : produit des pensions stable à +10 % en 2020 | Faible : offre nationale excédentaire (22 000 places de pension retraite vacantes en 2019, 5 sur 30 à 35 par structure) ; clientèle à moins d'une heure | [R6-02] [R6-03] [R6-16] [R6-27] |
| 2 | Pension « travail » (valorisation par un cavalier pro) | 4 223 € (moyenne 2021) ; 6 816 € HT au tarif 2025 (568 € HT/mois) | EBE/produit 22 % ; annuités = 103 % de l'EBE (moyenne) ; revenu disponible médian 9 437 €/UMO exploitant | 1 UMO pour 15 équidés ; cavalier professionnel indispensable | infrastructures plus lourdes que le modèle 1 | Haute (mais dépend du cavalier) | INCONNU | [R6-02] [R6-03] |
| 3 | Pension haut de gamme à proximité d'une grande agglomération | 11 070 € TTC (922,50 € TTC/mois, Jardy 2026), soit 9 225 € HT si TVA à 20 % | INCONNU publié ; ESTIMATION §10 : +1 460 à +3 935 €/box/an à 85 % d'occupation | encadrement et soins (cours hebdomadaire inclus) | très lourd : 3 manèges, 6 carrières, piste à Jardy | Haute | Existence d'un prix public élevé à 10 km de Paris ; aucune liste d'attente publique ; Chantilly, Fontainebleau, Deauville : INCONNU | [R6-15] |
| 4 | Centre équestre (enseignement + pension) | 4 653 € par équidé présent (cas-type 2025) | EBE/produit 22 à 48 % ; EBE/UMO exploitant 39 756 à 61 944 € (cas-types 2025) | 1,2 à 3 UMO pour 100 à 200 clients | manège 65 × 25 m ≈ 260 000 € (base 2019) | Moyenne : −15 % de chiffre d'affaires en 2020 | 648 254 licences FFE (saison 2024, −4 %) ; 560 052 licenciés en club | [R6-01] [R6-02] [R6-03] [R6-27] |
| 5 | Location d'écuries ou d'un pôle équestre à un professionnel | ≈ 1 176 €/box/an de redevance fixe minimale (Paris, 2021 : 80 000 € pour 68 boxes, plus une part variable) | Élevée pour le bailleur (pas de personnel), mais entretien lourd à la charge du propriétaire du bâti | 0 pour le bailleur | installations existantes | Contractuelle mais volatile (à Lamballe en 2025, 3 écuries résidentes sont parties et une seule reste) | Appel d'offres parisien (marché le plus tendu) ; rural : INCONNU | [R6-25] [R6-17] |
| 6 | Pension retraite (prés) | 1 920 à 3 840 €/an (160 à 320 €/mois, 2019, TTC probable) | INCONNU | 4,8 h de travail par équidé et par mois | faible (prés, abris) | Haute | Négative au niveau national (offre excédentaire) mais demande en hausse : 20 000 → 40 000 chevaux en pension retraite d'ici 2030 (projection IFCE) | [R6-16] |
| 7 | Centre de reproduction (sport) | pension 11,91 à 13,36 € HT/jour au box (2022) ou 18 à 21 € HT/jour (Hus, 2026 probable) ; 169 juments × 25 jours | EBE/produit 50 % (exploitation entière, 2022) | 2,8 UTH dont 1,8 exploitants ; vétérinaire disponible indispensable | 35 000 € (laboratoire, 2007) | Saisonnière (mars à mi-août) mais récurrente d'une année à l'autre | Réelle et locale : 169 juments de 76 clients au Rond Pré | [R6-26] [R6-28] |
| 8 | Élevage de chevaux de sport (naisseur, vente à 3 ans) | prix médian d'un Selle Français de 3 ans pour le CSO : 10 400 € (2021-2022) ; enchères : 27 151 € en moyenne (2022) | Faible ou négative : prix de revient d'un 3 ans de 7 700 € (avant 2011, non actualisé) ; « Les prix de vente sont trop souvent inférieurs au prix de revient » | faible par cheval, mais 3 à 4 ans de cycle | juments, prés, abris | Cyclique | 22 217 changements de propriété en sport-loisir (2024) ; 342 chevaux vendus aux enchères (2022, 9,6 M€) | [R6-01] [R6-05] [R6-24] |
| 9 | Élevage de pur-sang (vente de yearlings) | médiane 23 000 € HT (octobre 2025) ; 165 000 € HT (vente d'août 2025) ; 5 000 € HT (novembre 2025) | INCONNU (coûts de pension de poulinière en Normandie non trouvés) ; commission vendeur 6 % HT | haras spécialisé | juments de valeur, saillies de 8 000 à 150 000 € | Cyclique, très concentrée | Arqana 2025 : 3 168 chevaux vendus, 217 M€ | [R6-08] [R6-09] [R6-12] [R6-14] |
| 10 | Propriétaire de chevaux de course | ≈ 23 000 € d'encouragements par cheval entraîné en moyenne (2024, brut, toutes disciplines, avant parts de l'entraîneur, du jockey et de l'éleveur) | INCONNU (médiane non publiée) ; coût d'entraînement au trot 25 à 32 € HT/jour, soit 9 125 à 11 680 €/an (2021) | entraîneur | achat des chevaux | Cyclique (−25 % de gains au trot en 2020) | Financement en baisse : encouragements du galop −4,6 % en 2025 | [R6-01] [R6-03] [R6-06] [R6-27] |
| 11 | Station d'étalons de pur-sang | saillie de 8 000 à 150 000 € (2026) | INCONNU | spécialisé | étalon de plusieurs millions (non sourcé : ESTIMATION qualitative) | Cyclique, effets de mode | réservé aux grands haras | [R6-12] [R6-14] |
| 12 | Concours et événements | ≈ 686 partants par organisateur et par an ; 7 237 €/an de produit « organisation de concours » en pension travail (2021) | INCONNU | bénévoles, CDD (Lamballe) | carrière, parking, boxes démontables | Occasionnelle ; arrêt total possible (EHV-1 en 2021) | 1 522 479 partants FFE (2024) ; grands événements : 45 000 spectateurs au Mondial du Lion | [R6-01] [R6-03] [R6-17] [R6-20] [R6-22] |
| 13 | Club de polo | INCONNU (cotisation « stick and ball » : 1 200 €/an) | INCONNU | — | terrains de polo | Récurrente (cotisations) | 155 membres actionnaires à Chantilly (2023) : demande liée à un bassin existant | [R6-21] |
| 14 | Rééducation, clinique, quarantaine, transport | INCONNU | INCONNU | vétérinaires, transporteurs agréés | INCONNU | — | INCONNU | §6.3 |

## 10. Contribution nette possible au domaine : calcul illustratif (ESTIMATION)

Objectif : vérifier si une pension, seul modèle récurrent et résistant (§8.1 bis), peut dégager un surplus **après rémunération de tout le travail et renouvellement des installations**, comme l'exige un château qui salarie son personnel.

Formule par box et par an :
contribution = prix HT mensuel × 12 × taux d'occupation − charges opérationnelles − charges de structure hors amortissements − travail non rémunéré dans les références − provision de renouvellement.

Paramètres :
- Taux d'occupation : 85 % (HYPOTHÈSE fondée sur la vacance de 5 places sur 30 à 35 [R6-16]).
- Charges opérationnelles par tête (2021) : 770 € (pension hébergement) ou 1 929 € (pension travail) [R6-03].
- Charges de structure hors amortissements et frais financiers par équidé (2021) : 1 449 € ou 2 836 € [R6-03].
- Travail non rémunéré dans les références (exploitants et bénévoles) : (2,39 − 0,60) / 46 = 0,039 UMO par cheval (hébergement) ; (3,09 − 1,41) / 46 = 0,037 UMO (travail) [R6-03]. Valorisé à 29 629 € par UMO, coût salarial moyen du cas-type 2025 (59 258 € pour 2 salariés) [R6-02]. Soit 1 153 € ou 1 082 € par cheval et par an.
- Provision de renouvellement : box de 16 m² × 300 €/m² + 1/40e d'une carrière de 30 × 70 m à 39 €/m² + 1/40e d'un manège de 65 × 25 m à 160 €/m² = 13 348 € par box (base 2019) [R6-02], sur 25 ans (HYPOTHÈSE de durée de vie, à remplacer par les durées de R2) : 534 €/box/an.

Résultats (€ par box et par an ; calcul reproductible) :

| Prix (HT/mois) | Chiffre d'affaires à 85 % | Contribution avec coûts « hébergement » | Contribution avec coûts « travail » |
|---|---|---|---|
| 334 € HT (cas-type EQCE2 2025) | 3 407 € | −499 € | −2 974 € |
| 401 € HT (cas-type EQCE3 2025) | 4 090 € | +184 € | −2 291 € |
| 568 € HT (pension travail 2025) | 5 794 € | +1 888 € | −587 € |
| 768,75 € HT (Jardy 922,50 € TTC, TVA 20 %) | 7 841 € | +3 935 € | +1 460 € |
| 838,64 € HT (Jardy, TVA 10 %) | 8 554 € | +4 648 € | +2 173 € |

Extrapolation aux trois domaines types (ESTIMATION) :

| Domaine | Boxes | Pension standard (334 à 401 € HT) | Pension haut de gamme (prix de Jardy, TVA 20 %) | Location à un professionnel (≈ 1 176 €/box/an, plafond parisien) |
|---|---|---|---|---|
| S1 | 12 | −6 000 à +2 200 €/an | +17 500 à +47 200 €/an | ≈ 14 100 €/an |
| S2 | 40 | −20 000 à +7 400 €/an | +58 400 à +157 400 €/an | ≈ 47 100 €/an |
| S3 | 60 | −29 900 à +11 100 €/an | +87 600 à +236 100 €/an | ≈ 70 600 €/an |

Autres modèles :
- Centre de reproduction (Rond Pré) : EBE 74 449 € − 1,8 UMO d'exploitants valorisées à 29 629 € = **≈ +21 100 €/an** avant amortissement (investissement de 35 000 € seulement) [R6-26].
- Pension retraite : 40 chevaux au pré à 160 à 320 €/mois = 76 800 à 153 600 €/an de chiffre d'affaires (TTC probable) pour 2 304 heures de travail par an [R6-16] ; marge INCONNUE (coûts de foin, abris et clôtures à reprendre de R2).

Biais de ce calcul :
- Les coûts sont de 2021 et ne sont pas actualisés (inflation non appliquée), alors que les prix sont de 2025-2026 : **les contributions sont surestimées**.
- Le coût du travail retenu (≈ 29 600 € par UMO) correspond à des salariés de centre équestre, proches du SMIC. Un responsable d'écurie de domaine coûte plus cher (voir R2) : **contributions encore surestimées**.
- Les charges de structure des références incluent un fermage et des bâtiments agricoles ordinaires, pas l'entretien d'écuries historiques.
- Le prix de Jardy suppose une clientèle à moins d'une heure d'un bassin très aisé (Hauts-de-Seine). Pour un domaine rural, le prix observé tombe à 334-401 € HT et la contribution devient **nulle ou négative**.
- Impôt sur les sociétés, frais de gestion, assurance responsabilité des chevaux de tiers et aléas sanitaires non déduits.

## 11. Conclusion : quel modèle équestre peut dégager une contribution nette au domaine ?

1. **Aucun modèle équestre documenté ne finance un château.** Les meilleures contributions estimées (pension haut de gamme, 40 boxes) atteignent au mieux 0,06 à 0,16 M€ par an avant impôt, dans des conditions de prix proches de Paris, quand l'hypothèse H1 situe le besoin d'un domaine S2 entre 0,5 et 1,5 M€. Hypothèse H4 (« une activité équestre finance au mieux ses propres installations, rarement le château ») : **confirmée** par toutes les références trouvées.
2. **Les modèles « artisanaux » (pension standard, centre équestre, pension travail, élevage de sport) font vivre un exploitant, pas un propriétaire.** Leur EBE rémunère l'exploitant, souvent aidé par des bénévoles (60 à 70 % des pensions). Salariés, ils sont à l'équilibre ou en perte (§10).
3. **Ce qui peut dégager une contribution positive, modeste :**
   - une pension haut de gamme, à condition d'être à moins d'une heure d'une clientèle très solvable (Paris ouest, Chantilly, Deauville ou équivalent) et d'avoir des installations exceptionnelles. Demande non prouvée publiquement : à vérifier par une étude de marché locale avant tout investissement ;
   - la location du pôle équestre à un professionnel réputé (revenu récurrent sans personnel, de l'ordre de 1 200 € par box et par an au mieux, plafond parisien), avec un contrat construit pour éviter la requalification en bail rural (R3) et une clause de durée, car les locataires partent (Lamballe) ;
   - un centre de reproduction, si un vétérinaire et un étalon sont disponibles : investissement faible, marge élevée, contribution de l'ordre de 20 000 € par an, mais astreinte de 6 mois incompatible avec un propriétaire absent ;
   - une pension retraite sur les prés excédentaires des domaines S2 et S3 : peu de travail par cheval, demande nationale en hausse d'ici 2030, mais offre déjà excédentaire et prix bas.
4. **Courses, élevage de pur-sang, station d'étalons, polo, grands événements : des activités de passion ou de prestige, pas des moteurs financiers.** Leurs revenus sont cycliques, très concentrés (yearlings : médiane de 23 000 € HT contre une moyenne de 66 317 € en 2025) et adossés à un financement des courses en recul (France Galop : −11,7 M€ de résultat en 2025). Les événements sont occasionnels, bruyants, et peuvent être arrêtés du jour au lendemain par une épizootie (EHV-1 en 2021).
5. **Recommandation pour le modèle financier :** traiter l'équestre comme un **centre de coût partiellement couvert** (les chevaux du propriétaire relèvent de sa consommation personnelle), avec une contribution récurrente prudente : environ 0 € par box et par an pour une pension standard en zone rurale, environ 1 200 € par box et par an au mieux pour une location à un professionnel (plafond observé à Paris), et de 1 500 à 4 000 € par box et par an seulement si la proximité d'une clientèle haut de gamme est démontrée. Ne pas compter sur l'élevage, les courses ou les événements équestres pour financer le bâti.

## Contre-exemples et cas d'échec trouvés

1. **Haras national de Lamballe (syndicat mixte, Côtes-d'Armor), 2025** [R6-17], PAGE LUE : « Le Résultat prévisionnel de fonctionnement au titre de 2025 est Déficitaire de 130 673 € ». Départ de trois écuries résidentes (15 équidés) ; fin de l'activité d'étalons (« Les 3 étalons bretons ont quitté le site en fin d'année 2024 ») ; fréquentation estivale en baisse de 21 % ; 3 visites thématiques maintenues sur 14 ; rapport de la chambre régionale des comptes médiatisé (« Infraction financière », « carences administratives graves »). Un haras patrimonial qui combine location d'écuries, concours et visites ne s'autofinance pas.
2. **Haras national du Pin (Orne)** : l'activité d'étalonnage est décrite en 2012 comme « non rentable », appelée à être privatisée ou à disparaître [R6-18], PAGE LUE. Une étude d'impact du Sénat (projet de loi pjl20-709) prévoit la dissolution de l'établissement public créé en 2014 et le transfert de ses biens au département de l'Orne et à l'État [R6-19], EXTRAIT (vu en résultat de recherche seulement ; dissolution effective non vérifiée).
3. **Écuries de « pension travail » du Réseau Équin (2021)** : « l'EBE est inférieur à l'annuité » ; annuités = 103 % de l'EBE en moyenne ; revenu disponible médian de 9 437 € par exploitant à temps plein, alors même que ces exploitations sont sélectionnées pour leur viabilité [R6-03], PAGE LUE.
4. **Élevage de chevaux de sport** : « Les prix de vente sont trop souvent inférieurs au prix de revient, en particulier dans les exploitations spécialisés » [R6-24], PAGE LUE (référence de 2011).
5. **Yearlings de pur-sang sans pedigree recherché** : vente de yearlings de novembre 2025 chez Arqana, médiane de 5 000 € HT pour 103 chevaux vendus [R6-08], PAGE LUE ; ce prix ne couvre pas une saillie d'entrée de gamme (8 000 € pour Erevann en 2026 [R6-14]).
6. **France Galop** : résultat net de −11 688 k€ en 2025 et −1 510 k€ en 2024 ; encouragements réduits de 283,5 à 270,5 M€ [R6-06], PAGE LUE.
7. **Pension retraite** : 22 000 places inoccupées en France (2019), 5 places vacantes en moyenne par structure de 30 à 35 places [R6-16], PAGE LUE : multiplier les places de pension ne crée pas la demande.
8. **Épizootie EHV-1 de 2021** : annulation de tous les concours internationaux dans 10 pays jusqu'au 28 mars 2021 [R6-22], PAGE LUE ; suspension française prolongée jusqu'au 11 avril 2021 [R6-23], EXTRAIT.
9. **Club de polo de Chantilly** : la grille « Tarifs 2026 » renvoyait vers un fichier Dropbox supprimé [R6-21] ; ce n'est pas un échec économique, mais une donnée introuvable.

## Points de doute / hypothèses non vérifiées

1. **TVA sur les pensions et l'enseignement en 2026** : non vérifiée ici (la fiche officielle F23567 ne traite pas des équidés). Les conversions TTC → HT utilisent 20 % (prudent), avec des variantes à 10 % et 5,5 %. La grille du Rond Pré suggère 10 % sur la pension de reproduction en 2022 (ESTIMATION). À trancher par R3.
2. **Jardy** : unité mensuelle supposée (non écrite sur la plaquette) ; statut public du domaine supposé (tarif différencié Hauts-de-Seine / extérieurs) ; pas de taux d'occupation ni de liste d'attente connus.
3. **Bry-sur-Marne** : tarif de 591 € présumé TTC (tarif public aux particuliers) ; non écrit dans la délibération.
4. **Références du Réseau Équin** : échantillons sélectionnés, résultats « supérieurs à ce que l'on peut rencontrer habituellement sur le terrain » ; coûts de 2021 non actualisés dans le calcul du §10.
5. **Référentiel d'investissement du cas-type** : prix de base 2019, HT présumé ; durées de vie de 25 ans posées par HYPOTHÈSE (à remplacer par R2).
6. **Coût de production d'un cheval de sport** : référence d'avant 2011, non actualisée (l'indice IPAMPA n'a pas été appliqué).
7. **Taux d'occupation de 85 %** : HYPOTHÈSE tirée de la vacance des pensions retraite en 2019, transposée aux pensions de sport sans preuve.
8. **Coût du travail à 29 629 € par UMO** : coût moyen de deux salariés de centre équestre (cas-type 2025) ; un personnel de domaine haut de gamme coûte davantage (R2).
9. **Pension de poulinière (9 à 15 €/jour)** : EXTRAIT d'une fiche non datée, PDF inaccessible.
10. **Conditions « 1/10 SLF »** des saillies Aga Khan Studs : sens supposé (paiement au 1er octobre, poulain vivant) ; HT non vérifié.
11. **Page Arqana « processus de vente »** partiellement ancienne (mention d'une TVA à 19,6 %) ; droits d'inscription inconnus.
12. **Médiane des gains par cheval de course** : inconnue ; la moyenne de 23 000 € par cheval entraîné est brute, toutes disciplines, avant partage entre propriétaire, entraîneur, jockey et éleveur.
13. **Enjeux PMU 2025, données LeTrot 2025, licences FFE 2025** : INCONNU (site PMU bloqué, aucun rapport LeTrot ou FFE accessible).
14. **Budgets des grands événements** (Mondial du Lion, Pau, Haras du Pin, Chantilly, Saut Hermès, Dinard) : INCONNU.
15. **Tarifs de rééducation, cliniques, quarantaine, transport, « hôtels à chevaux »** : INCONNU.
16. **Pensions haut de gamme à Chantilly, Fontainebleau, Deauville** : aucune grille publique trouvée ; prix et demande INCONNUS.
17. **Loyer d'écuries louées à un professionnel en zone rurale** : INCONNU ; seul le plafond parisien (≈ 98 €/box/mois, 2021) est sourcé.

## Chiffres clés pour le modèle

| # | Donnée | Valeur | Unité | Année | HT/TTC | Statut | Source |
|---|---|---|---|---|---|---|---|
| 1 | Pension box « hébergement » (cas-types péri-urbains) | 334 à 401 | €/mois | 2025 | HT | PAGE LUE | [R6-02] |
| 2 | Pension box « travail » (cas-type) | 568 | €/mois | 2025 | HT | PAGE LUE | [R6-02] |
| 3 | Pension box en Île-de-France, centre municipal (UCPA) | 591 | €/mois | saison 2025-2026 | TTC présumé | PAGE LUE | [R6-04] |
| 4 | Pension box haut de gamme, Haras de Jardy (92), résidents / extérieurs | 922,50 / 1 002,71 | €/mois (unité supposée) | 2026 | TTC | PAGE LUE | [R6-15] |
| 5 | Pensions observées dans le Réseau Équin : box sans travail / box travail / pré | 11-17 / 13-24 / 5-12 | €/jour | 2021 | TTC | PAGE LUE | [R6-03] |
| 6 | Personnel : équidés par UMO, pension hébergement / pension travail | 19,4 / 15 | équidés/UMO | 2021 | — | PAGE LUE | [R6-03] |
| 7 | Charges opérationnelles équines par tête, hébergement / travail | 770 / 1 929 | €/tête/an | 2021 | HT présumé | PAGE LUE | [R6-03] |
| 8 | Charges de structure hors amortissements par équidé, hébergement / travail | 1 449 / 2 836 | €/équidé/an | 2021 | HT présumé | PAGE LUE | [R6-03] |
| 9 | Revenu disponible médian par exploitant, pension travail / hébergement | 9 437 / 18 265 | €/UMO/an | 2021 | — | PAGE LUE | [R6-03] |
| 10 | Cas-type centre équestre « compétition » : produit / EBE / UMO | 265 238 / 57 935 (22 %) / 3 | € et UMO | campagne 2025 | HT | PAGE LUE | [R6-02] |
| 11 | Coûts d'investissement : manège / boxes / carrière | 160 / 300 / 39 | €/m² | base 2019 | HT présumé | PAGE LUE | [R6-02] |
| 12 | Contribution nette d'une pension, par box : standard rurale / haut de gamme (prix de Jardy) | −500 à +184 / +1 460 à +3 935 | €/box/an | 2021-2026 | HT | ESTIMATION (§10) | [R6-02] [R6-03] [R6-15] [R6-16] |
| 13 | Redevance minimale d'un centre équestre à Paris (68 boxes) | 80 000 (≈ 98 €/box/mois) | €/an | 2021 | non précisé dans l'avis | PAGE LUE (calcul par box : ESTIMATION) | [R6-25] |
| 14 | Places de pension retraite vacantes | 22 000 (5 sur 30 à 35 par structure) | places | 2019 | — | PAGE LUE | [R6-16] |
| 15 | Choc 2020 : pensions / centres équestres / gains de courses au trot | 0 à +10 % / −15 % / −25 % | variation du produit | 2020 | — | PAGE LUE | [R6-27] |
| 16 | Centre de reproduction : produit / EBE / investissement | 149 077 / 74 449 (50 %) / 35 000 | € | 2022 (investissement 2007) | HT présumé | PAGE LUE | [R6-26] |
| 17 | Arqana, total des ventes : chevaux vendus / chiffre d'affaires / prix médian | 3 168 / 217,3 M€ / 23 000 € | — | 2025 | HT | PAGE LUE | [R6-08] [R6-10] |
| 18 | Selle Français de 3 ans pour le CSO : prix médian, contre prix de revient d'un 3 ans | 10 400 contre 7 700 | € | 2021-2022 contre avant 2011 | non précisé | PAGE LUE | [R6-05] [R6-24] |
| 19 | France Galop : encouragements 2025 / 2024 ; primes éleveurs en % des allocations | 270,5 / 283,5 M€ ; 15,0 % | M€ ; % | 2025 | — | PAGE LUE (ratio : ESTIMATION) | [R6-06] |
| 20 | Prime au propriétaire au galop (chevaux nés en France), selon l'âge | 80 % (2-3 ans), 55 % (4-5 ans), 45 % (6 ans et plus), 35 % en Groupe 1 | % de l'allocation | 2024 | — | PAGE LUE | [R6-07] |
| 21 | Licences FFE | 648 254 (−4 %) | licences | saison 2024 | — | PAGE LUE | [R6-01] |
| 22 | Enjeux hippiques totaux | 9 678 | M€ | 2024 | — | PAGE LUE | [R6-01] |
