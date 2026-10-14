# R2 — Personnel, jardins, terres, équipements, chevaux

Agent : R2. Démarré le 2026-10-14. Fichier écrit au fur et à mesure.
Sources : `01_RECHERCHE/sources/sources_R2.csv` (identifiants [R2-xx]).

Statuts : PAGE LUE (page ouverte, citation exacte) / EXTRAIT (vu dans un résultat de recherche) / ESTIMATION (calcul explicite) / HYPOTHÈSE (choix de modélisation) / INCONNU (non trouvé, méthode de vérification indiquée).

## Résumé

- **Coût du travail 2026.**
  - SMIC : 12,02 €/h au 1er janvier 2026, puis **12,31 €/h (1 867,02 €/mois) depuis le 1er juin 2026**.
  - La nouvelle réduction générale (RGDU) réduit fortement le coût du travail au SMIC : coût employeur de **23 853 €/an**, soit un ratio de 1,065. L'avantage s'efface vers 3 SMIC : 1,5 SMIC coûte 44 118 €/an (ratio 1,31) et 2,5 SMIC, 78 982 €/an (ratio 1,41). Source : simulateur officiel URSSAF.
- **Grilles conventionnelles.** Elles ont été lues pour le paysage, les activités hippiques, la production agricole et les particuliers employeurs. Plusieurs premiers échelons sont désormais sous le SMIC.
- **Salaires de marché** des cadres de domaine : **introuvables**. Les niveaux retenus sont des HYPOTHÈSES.
- **Jardins.** Un seul point sourcé : Villandry, 10 jardiniers pour 7 ha, soit environ 1,4 ETP/ha, à prendre comme plafond.
- **Matériel.** Prix 2026 et durées tirés du guide des CUMA, par exemple un tracteur de 100 à 140 CV à 101 464 € HT, amorti en 10,7 ans. Il y a une forte déséconomie d'échelle sous 100 ha.
- **Terres.** Indice des fermages 2025 : 123,06. Pâtures en Aveyron : 52 à 171 €/ha/an. Foin 2024 départ ferme : environ 100 €/t (extrait).
- **Chevaux.** Les références IFCE datent de 2011-2012. Fumier : 12,8 t par cheval et par an au box, avec des règles du RSD. Installations : prix d'un site commercial (fiabilité faible).
- **Synthèse (§9).**
  - Masse salariale : environ **77 000 €** (S1, 2,7 ETP), **489 000 €** (S2, 13 ETP) et **1,08 M€** (S3, 29 ETP), calculée sur des hypothèses d'effectifs explicites.
  - Coût complet d'un box occupé : environ **5 500 à 8 500 €/an**.

## 1. Coût du travail 2025-2026

### 1.1 SMIC

| Donnée | Valeur | Statut | Source |
|---|---|---|---|
| SMIC brut mensuel au 1er janvier 2026 (35 h) | 1 823,03 €/mois | PAGE LUE | [R2-02] « Au 1er janvier 2026, le Smic brut mensuel (base 35 heures par semaine) est fixé à 1 823,03 € » |
| SMIC brut annuel au 1er janvier 2026 | 21 876,40 €/an | PAGE LUE | [R2-02] « payé au Smic, soit 1 823,03 € par mois et 21 876,40 € sur l'année » |
| SMIC horaire brut au 1er janvier 2026 | 12,02 €/h | PAGE LUE (presse) + ESTIMATION concordante | [R2-04] « 12,02€ brut de l'heure » ; calcul 1 823,03 / 151,67 h = 12,02 €. Valeur horaire non lue sur une page officielle. |
| SMIC horaire brut en vigueur (page vérifiée le 01/06/2026) | 12,31 €/h | PAGE LUE | [R2-01] tableau « Montants du Smic » : horaire « 12,31 € » brut, « 9,74 € » net |
| SMIC mensuel brut en vigueur | 1 867,02 €/mois | PAGE LUE | [R2-01] « 1 867,02 € » brut ; net indicatif « 1 477,93 € » |
| SMIC annuel brut en vigueur | 22 404,20 €/an | PAGE LUE | [R2-01] annuel « 22 404,20 € brut, 17 735,19 € net » |
| Date d'effet du SMIC à 12,31 € | 1er juin 2026 | PAGE LUE (indirecte) | [R2-02] « une mesure de tolérance permet d'appliquer la revalorisation du Smic au 1er juin 2026 dans la formule de calcul » ; [R2-01] référence « Arrêté du 22 mai 2026 relatif au relèvement du salaire minimum de croissance ». Hausse de 12,02 à 12,31 € = +2,4 % (ESTIMATION). |
| Mécanisme de revalorisation | 1er janvier + revalorisation automatique si l'inflation dépasse 2 % | PAGE LUE | [R2-01] « Le Smic est revalorisé chaque année au 1er janvier » ; en cas d'inflation d'au moins 2 %, « il est augmenté automatiquement dans les mêmes proportions ». |

Recoupement presse : [R2-04] (16/01/2026) « Depuis le 1er janvier 2026, le salaire minimum interprofessionnel de croissance s'établit à 12,02€ brut de l'heure, soit 1 823,03€ brut mensuels pour un temps plein de 35 heures » et « Comparé à 2025, le Smic progresse de 14 centimes par heure » (donc 11,88 €/h en 2025, ESTIMATION par soustraction). Le SMIC horaire de 12,02 € au 1er janvier 2026 passe donc du statut ESTIMATION au statut PAGE LUE (source de presse).

Pour le modèle en € constants 2026 : prendre **12,31 €/h brut, soit 1 867,02 €/mois** (valeur en vigueur depuis le 1er juin 2026). Pour une moyenne annuelle 2026 : 5 mois à 1 823,03 € + 7 mois à 1 867,02 € = 22 202,25 € (ESTIMATION).

### 1.2 Cotisations patronales et réforme 2026 de la réduction générale (RGDU)

Source [R2-02], PAGE LUE, citations exactes ou fidèles :
- **Nouveau nom.** Depuis le 1er janvier 2026, l'allègement général s'appelle « réduction générale dégressive unique » (RGDU).
- **Plage.** La réduction est maximale au SMIC, dégressive jusqu'à 3 SMIC (valeur au 1er janvier 2026), et « ne s'applique plus à partir d'une rémunération égale à 3 Smic ». Avec la tolérance du 1er juin 2026, le seuil devient « 2,9293 Smic applicable au 1er juin 2026 ».
- **Formule.** Coefficient = Tmin + Tdelta × [½ × (3 × SMIC annuel / rémunération annuelle brute − 1)]^P. Paramètres :
  - Tmin = 0,0200 ;
  - Tdelta = 0,3781 pour moins de 50 salariés, 0,3821 pour 50 salariés ou plus ;
  - P = 1,75 ;
  - SMIC annuel de référence = 21 876,40 €.
- **Plafond.** « Le coefficient ne peut toutefois pas excéder la somme des valeurs Tmin et Tdelta, soit 0,3981 » pour moins de 50 salariés (0,4021 pour 50 salariés ou plus).
- **Exemple au SMIC.** « La réduction pour l'année sera donc égale à 8 708,99 € (21 876,40 x 0,3981) ». Autre exemple : 3 500 €/mois, coefficient 0,0611, réduction de 2 566,20 €/an.
- **Taux réduits supprimés.** Les taux réduits des cotisations d'assurance maladie et d'allocations familiales « sont supprimés ». Ils restent seulement pour Lodeom, TO-DE (travailleurs occasionnels agricoles), AADPA, ZRD et ZFRR.
- **Cotisations couvertes.** Maladie, vieillesse de base, FNAL, allocations familiales, CSA, retraite complémentaire, chômage, et AT/MP dans la limite de 0,49 %. Chômage : 4 %. FNAL : 0,1 % pour moins de 50 salariés.

**Taux détaillés de cotisations (page URSSAF « taux secteur privé »)** : INCONNU, car la page était inaccessible (urssaf.fr renvoie 503 ou une réponse vide via le proxy, essayé deux fois). Pour vérifier : https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html. À défaut, le taux global avant réduction est déduit du simulateur officiel (§1.3) : environ 43,5 % à 44 % du brut, mutuelle employeur comprise (ESTIMATION).

### 1.3 Coût employeur chargé à 1 ; 1,5 et 2,5 SMIC (régime général, 2026)

Calcul : simulateur officiel URSSAF mon-entreprise, interrogé par son API publique [R2-11]. Le simulateur applique les règles du « 01/07/2026 », donc avec le SMIC à 12,31 €.

Hypothèses par défaut du simulateur :
- CDI à temps plein (35 h), effectif de 10 salariés ;
- taux AT/MP de 2,08 % ;
- mutuelle de 40 €/mois, dont 50 % à la charge de l'employeur ;
- pas de prime, pas d'heures supplémentaires, hors Alsace-Moselle.

Statut : ESTIMATION produite par l'outil officiel. Les chiffres sont des sorties de calcul et non du texte publié.

| Niveau | Brut mensuel | Cotisations patronales nettes (après RGDU) | dont RGDU déduite | **Coût employeur mensuel** | Coût / brut | Coût annuel (× 12) | Net avant impôt mensuel |
|---|---|---|---|---|---|---|---|
| 1 SMIC | 1 867,02 € | 120,74 € | 700,13 € | **1 987,76 €** | 1,065 | **23 853 €** | 1 455,99 € |
| 1,5 SMIC | 2 800,53 € | 876,01 € | 345,31 € | **3 676,54 €** | 1,313 | **44 118 €** | 2 194,95 € |
| 2,5 SMIC | 4 667,55 € | 1 914,24 € | 117,16 € | **6 581,79 €** | 1,410 | **78 982 €** | 3 674,23 € |

**Grille complète** [R2-11], coût employeur annuel = coût mensuel × 12. Mêmes hypothèses par défaut (règles au 01/07/2026, SMIC brut de 1 867,02 €/mois). Statut : ESTIMATION produite par l'outil officiel.

| Multiple du SMIC | Brut mensuel | Coût employeur mensuel (effectif 10) | Ratio coût / brut | **Coût annuel, effectif 10** | **Coût annuel, effectif 25** |
|---|---|---|---|---|---|
| 1,0 | 1 867,02 € | 1 987,76 € | 1,065 | 23 853 € | 23 973 € |
| 1,1 | 2 053,72 € | 2 351,30 € | 1,145 | 28 216 € | 28 346 € |
| 1,2 | 2 240,42 € | 2 699,23 € | 1,205 | 32 391 € | 32 531 € |
| 1,3 | 2 427,13 € | 3 034,64 € | 1,250 | 36 416 € | 36 566 € |
| 1,4 | 2 613,83 € | 3 359,85 € | 1,285 | 40 318 € | 40 479 € |
| 1,5 | 2 800,53 € | 3 676,54 € | 1,313 | 44 118 € | 44 289 € |
| 1,75 | 3 267,28 € | 4 439,52 € | 1,359 | 53 274 € | 53 470 € |
| 2,0 | 3 734,04 € | 5 171,33 € | 1,385 | 62 056 € | 62 277 € |
| 2,5 | 4 667,55 € | 6 581,79 € | 1,410 | 78 982 € | 79 253 € |
| 3,0 | 5 601,06 € | 8 034,02 € | 1,434 | 96 408 € | 96 730 € |

À 3 SMIC (5 601 €), la RGDU est nulle, car le salaire dépasse le seuil de 3 × 1 823,03 € = 5 469 €. L'écart entre un effectif de 10 et de 25 est d'environ 0,5 %.

Lectures (ESTIMATION) :
- **Avant réduction**, les cotisations patronales représentent environ 44 % du brut : (120,74 + 700,13) / 1 867,02 = 44,0 % ; (1 914,24 + 117,16) / 4 667,55 = 43,5 %.
- **Effet de la RGDU** : elle ramène le surcoût à environ 6,5 % au SMIC, 31 % à 1,5 SMIC et 41 % à 2,5 SMIC. Une masse salariale proche du SMIC coûte donc beaucoup moins cher que des postes qualifiés.
- **Coût par heure réellement travaillée** : au SMIC, 23 853 € / 1 607 h ≈ **14,8 €/h**. HYPOTHÈSE : 1 607 h travaillées par an, soit la durée annuelle de référence de 35 h. Ce coût sert de base de comparaison avec les tarifs de sous-traitance.
- **Salariés agricoles et équestres (MSA)** : la RGDU s'applique aussi ([R2-02] mentionne TO-DE pour l'agriculture). Les taux AT/MP agricoles diffèrent. Les chiffres ci-dessus sont une approximation : à vérifier avec le simulateur MSA ou un expert-comptable.
- **Particulier employeur (CESU)** : la RGDU ne s'applique pas. Le régime est différent (déduction forfaitaire par heure, crédit d'impôt). Voir §1.5.
- **Non compris** : 13e mois et primes, astreintes de week-end des soigneurs, logement de fonction (avantage en nature), vêtements de travail, médecine du travail, formation au-delà des contributions légales, intérim et remplacements.

### 1.4 Grilles conventionnelles (minima bruts)

**Quelle convention s'applique ?** Elle dépend de l'employeur, pas du lieu. C'est une HYPOTHÈSE de structuration, à faire valider par R3 ou un expert-comptable.
- Personnel employé par le propriétaire à titre privé (maison, jardin privatif, gardien) : convention des particuliers employeurs (IDCC 3239).
- Personnel d'une société d'exploitation équestre : convention des activités hippiques (IDCC 7026), régime MSA.
- Personnel agricole (foin, prés, bois) : production agricole (IDCC 7024), régime MSA.
- Prestataire de jardins : convention des entreprises du paysage (IDCC 7018), régime MSA.
- Activité hôtellerie ou événementiel : HCR (IDCC 1979), non étudiée ici.

#### a) Particuliers employeurs et emploi à domicile (IDCC 3239)

Source [R2-03] : grille de l'« avenant n°10 du 5 février 2026 ». Salaires bruts ; le mensuel est calculé sur 174 h, soit une base de 40 h par semaine. Le site indique que la certification de branche augmente le salaire de 4 % à 5 %.

| Niveau | €/h brut | €/mois brut (174 h) |
|---|---|---|
| I | 12,61 | 2 194,14 |
| II | 12,74 | 2 216,76 |
| III | 12,89 | 2 242,86 |
| IV | 13,08 | 2 275,92 |
| V | 13,28 | 2 310,72 |
| VI | 13,80 | 2 401,20 |
| VII | 14,11 | 2 455,14 |
| VIII | 14,52 | 2 526,48 |
| IX | 15,29 | 2 660,46 |
| X | 16,12 | 2 804,88 |
| XI | 17,06 | 2 968,44 |
| XII | 18,07 | 3 144,18 |

Statut : PAGE LUE, source secondaire (site de paie), à recouper avec l'avenant au Journal officiel.

- **INCONNU** : correspondance entre ces niveaux et les emplois-repères (jardinier, gardien, gouvernant(e), employé familial, homme ou femme toutes mains). Vérification : texte de la CCN IDCC 3239 (classification), sur Légifrance ou dans la brochure JO 3180.
- **Point d'attention** : la base de 174 h par mois (40 h par semaine) laisse supposer une durée conventionnelle de 40 h. C'est une ESTIMATION déduite du mensuel. À vérifier dans la CCN.
- **Minimum 2026 avec congés payés** ([R2-04], janvier 2026) : « En intégrant 10% de congés payés, le salaire minimum atteint désormais 10,51€ net de l'heure, soit 13,46€ brut. »

#### b) Activités hippiques, dont les centres équestres (IDCC 7026)

La CCN des personnels des activités hippiques du 16 novembre 2023 (IDCC 7026) regroupe désormais les anciennes conventions des trotteurs (7013), du galop (7014) et des centres équestres (7012) [R2-06, EXTRAIT].

Grille de l'avenant n°6 du 20 janvier 2026, applicable au 1er février 2026. Hausse moyenne de 1,28 %. Base : 35 h par semaine, soit 151,67 h par mois [R2-05, PAGE LUE, source secondaire]. Selon la page, l'extension était « en attente de publication au Journal officiel et d'extension ».

| Niveau | Coeff. | Emplois | €/h brut | €/mois brut |
|---|---|---|---|---|
| 1 | 100 | Agent d'entretien | 12,05 | 1 827,62 |
| 1 | 103 | Agent ou hôtesse d'accueil ; soigneur | 12,10 | 1 835,21 |
| 1 | 106 | Cavalier-soigneur | 12,13 | 1 839,76 |
| 1 | 109 | Animateur-soigneur | 12,26 | 1 859,47 |
| 2 | 111 | Secrétaire | 12,38 | 1 877,67 |
| 2 | 118 | Guide équestre | 12,43 | 1 885,26 |
| 2 | 121 | Soigneur responsable d'écurie | 12,73 | 1 930,76 |
| 2 | 130 | Enseignant-animateur ; guide enseignant de tourisme équestre | 13,90 | 2 108,21 |
| 3 | 150 | Secrétaire-comptable ; enseignant | 15,87 | 2 407,00 |
| 4 | 167 | Enseignant | 17,66 | 2 678,49 |
| 4 | forfait 218 j | Responsable pédagogique | n.c. | 2 857,94 |
| 5 | 193 | Directeur | 20,38 | 3 091,03 |
| 5 | forfait 218 j | Directeur | n.c. | 3 501,98 |

**Observation (ESTIMATION)** : depuis le 1er juin 2026, le SMIC est à 12,31 €/h. Les coefficients 100 à 109, de 12,05 € à 12,26 €, sont donc **sous le SMIC**, qui s'applique à leur place. Une écurie paie de fait ses soigneurs et cavaliers-soigneurs débutants au SMIC.

#### c) Entreprises du paysage (IDCC 7018) — prestataires de jardins

Texte lu [R2-07] : « Avenant n° 46 du 17 septembre 2025 », NOR AGRS2597131M. Article 4 : « Les dispositions du présent avenant entreront en vigueur au plus tôt le 1er janvier 2026, sous réserve de la publication au journal officiel de l'arrêté d'extension au plus tard le 26 décembre 2025 ». Selon un EXTRAIT [R2-08], l'avenant a été étendu par arrêté du 11 décembre 2025, publié au JO du 26 décembre 2025, et s'applique donc au 1er janvier 2026 (hausse de 1 %).

Ouvriers et employés (base 151,67 h) [R2-07, PAGE LUE] :

| Position | €/h brut | €/mois brut |
|---|---|---|
| O.1 | 12,12 | 1 838,24 |
| O.2 | 12,18 | 1 847,34 |
| O.3 | 12,30 | 1 865,54 |
| O.4 | 12,59 | 1 909,53 |
| O.5 | 12,95 | 1 964,13 |
| O.6 | 13,56 | 2 056,65 |
| E.1 | 12,12 | 1 838,24 |
| E.2 | 12,30 | 1 865,54 |
| E.3 | 12,67 | 1 921,66 |
| E.4 | 13,56 | 2 056,65 |

Techniciens et agents de maîtrise, mensuel brut sur 151,67 h : TAM.1 2 242 € ; TAM.2 2 352 € ; TAM.3 2 535 € ; TAM.4 2 756 €. En forfait de 218 jours : 2 578 € ; 2 705 € ; 2 916 € ; 3 169 €.

Cadres, annuel brut : C 38 147 € ; C1 42 336 € ; C2 42 336 € ; C3 44 100 € ; C4 45 424 € ; C5 48 510 € ; D « D'un commun accord ».

**Observation (ESTIMATION)** : depuis le 1er juin 2026 (SMIC 12,31 €/h), les positions O.1, O.2, O.3, E.1 et E.2 sont sous le SMIC. Un jardinier débutant d'entreprise du paysage est donc payé au SMIC.

#### d) Production agricole et CUMA (IDCC 7024) — salariés agricoles du domaine (prés, foin, bois)

Source [R2-09], PAGE LUE (FD CUMA 53, 07/04/2026) : « Suite à l'augmentation du SMIC de 1,2 % au 1er janvier, les partenaires sociaux de la branche de la production agricole et des Cuma ont conclu un avenant 10 à la convention collective nationale dont l'arrêté d'extension a été publié au Journal Officiel le 4 avril 2026. Cet avenant fixe la nouvelle grille des salaires minimums tenant compte de l'augmentation moyenne de 1.18% au 1er mai ».

| Palier | Points (entre / et) | €/h brut au 1er mai 2026 | €/mois brut (151,67 h), ESTIMATION |
|---|---|---|---|
| 1 | 9-11 | 12,02 | 1 823 |
| 2 | 12-16 | 12,11 | 1 837 |
| 3 | 17-24 | 12,28 | 1 863 |
| 4 | 25-35 | 12,55 | 1 903 |
| 5 | 36-51 | 13,08 | 1 984 |
| 6 | 52-73 | 13,70 | 2 078 |
| 7 | 74-104 | 14,50 | 2 199 |
| 8 | 105-143 | 15,50 | 2 351 |
| 9 | 144-196 | 16,78 | 2 545 |
| 10 | 197-270 | 18,58 | 2 818 |
| 11 | 271-399 | 21,15 | 3 208 |
| 12 | 400 et plus | 24,16 | 3 664 |

Selon un EXTRAIT [R2-10], un avenant n°11 du 2 juillet 2026 prévoirait +1,96 % en moyenne. Il n'était pas étendu. Montants INCONNUS ; à vérifier sur Légifrance ou auprès de la FNSEA ou de la FNCUMA. Depuis le 1er juin 2026, les paliers 1 à 3 (12,02 € à 12,28 €) sont sous le SMIC (ESTIMATION).

### 1.5 Cas du particulier employeur (personnel de maison payé par le propriétaire à titre privé)

- **Déduction forfaitaire** [R2-12, PAGE LUE, vérifiée le 01/06/2026] : « bénéficiez d'une déduction forfaitaire de cotisations patronales de Sécurité sociale de 2 € si vous employez un salarié à votre domicile ». Elle s'applique par heure travaillée, hors heures de congés payés. Elle ne se cumule pas avec les exonérations partielles.
- **Crédit d'impôt** [R2-13, PAGE LUE, vérifiée le 15/04/2026] :
  - 50 % des dépenses, retenues dans la limite de « 12 000 € par an », soit 6 000 € d'avantage au plus ;
  - plafond majoré de 1 500 € dans certains cas, sans dépasser 15 000 € ;
  - petits travaux de jardinage plafonnés à 5 000 € par foyer, à l'intérieur du plafond général.
- **Conséquence (ESTIMATION)** : pour un domaine qui emploie de 2 à 30 personnes, le crédit d'impôt est marginal, au plus 6 000 € à 7 500 € par an. Il ne change pas l'équation. La déduction de 2 €/h représente environ 3 200 €/an pour un temps plein de 1 607 h, contre environ 8 400 €/an de RGDU au SMIC en entreprise (700,13 € × 12). Mais le salarié du particulier employeur relève d'une base conventionnelle de 40 h (§1.4 a). Comparaison fine : INCONNU, à faire avec le simulateur CESU de l'URSSAF ou un expert-comptable.
- **Limite juridique (HYPOTHÈSE à faire valider par R3)** : le statut de particulier employeur suppose un travail au domicile privé du particulier. Le personnel affecté aux activités commerciales (écurie de pension, événements) doit être salarié de la société d'exploitation.

## 2. Salaires de marché et tension du recrutement

### 2.1 Équitation : tension du recrutement (pas de salaires publiés)

Source [R2-14], rapport d'activité équi-ressources 2022 de l'IFCE, PAGE LUE (texte extrait du PDF) :
- 3 719 offres d'emploi diffusées en 2022.
- Depuis 2015, « 32 738 offres diffusées », dont « 23 167 offres ont abouties à un recrutement ».
- Secteur sport et loisir : « 2 288 offres d'emploi » ; pourvues via équi-ressources 712, pourvues autrement 779, annulées 757. Environ un tiers des offres sont donc annulées (ESTIMATION : 757 / 2 248).
- « Palefrenier soigneur / Garçon de cour & Enseignant d'équitation représentent 46% des offres d'emploi diffusées en 2022 ».

Le rapport ne donne **aucun salaire proposé**. Les salaires de marché des soigneurs, cavaliers et responsables d'écurie restent INCONNUS par cette voie. Pour vérifier : statistiques d'offres d'équi-ressources (equiressources.fr) ou études de l'Observatoire économique et social du cheval (IFCE).

### 2.2 Domaines : régisseur, chef jardinier, majordome, gouvernante, responsable d'écurie, cavalier

**INCONNU.** Aucune donnée de salaire de marché fiable trouvée.
- La recherche web n'a renvoyé que des métiers voisins, par exemple le directeur de domaine viticole à « environ 4 300 € brut mensuels » sur une fiche métier non ouverte. Ce chiffre n'est pas retenu.
- Indeed renvoie 403.
- Le moteur d'équi-ressources est dynamique et vide en lecture.

Pistes de vérification :
1. Relever 20 à 30 annonces datées sur des sites d'agences de personnel de maison et de propriétés privées, et sur equiressources.fr (filtre « responsable d'écurie », « cavalier ») ;
2. Consulter la fiche ROME de France Travail (Métierscope), rubrique « salaires à l'embauche » ;
3. Interroger un cabinet de recrutement de personnel de maison. Ce contact est réservé au directeur, car les agents n'ont pas le droit de contacter des tiers.

**HYPOTHÈSES de modélisation proposées** (non sourcées, à remplacer dès que des annonces seront relevées). Elles sont construites sur les grilles conventionnelles du §1.4 et sur l'usage selon lequel un poste à responsabilité se paie au-dessus du minimum :

| Poste | Hypothèse brute annuelle | Base de l'hypothèse |
|---|---|---|
| Jardinier qualifié | 1,1 à 1,3 SMIC (24 600 € à 29 100 €) | Paysage O.4 à O.6 = 12,59 € à 13,56 €/h [R2-07] |
| Chef jardinier (équipe de 3 à 10) | 1,5 à 2,0 SMIC (33 600 € à 44 800 €) | Paysage TAM.3 à TAM.4 = 2 535 € à 2 756 €/mois, ou cadre C (38 147 €) [R2-07] |
| Soigneur / palefrenier | 1,0 SMIC (22 404 €) | Coeff. 103 sous le SMIC [R2-05] |
| Responsable d'écurie | 1,2 à 1,6 SMIC (26 900 € à 35 800 €) | Coeff. 121 = 12,73 €/h minimum [R2-05], plus une prime de responsabilité (HYPOTHÈSE) |
| Cavalier (travail et valorisation) | 1,1 à 1,5 SMIC | Coeff. 106 à 130 [R2-05] |
| Employé(e) de maison | 1,0 à 1,2 SMIC | IDCC 3239, niveaux I à VI : 12,61 € à 13,80 €/h [R2-03]. Correspondance entre niveaux et emplois INCONNUE |
| Gouvernante | 1,3 à 1,5 SMIC | IDCC 3239, niveaux supérieurs, jusqu'à 18,07 €/h au niveau XII [R2-03], plus une prime de responsabilité (HYPOTHÈSE) |
| Gardien / homme d'entretien | 1,2 à 1,4 SMIC | HYPOTHÈSE pure. Le gardiennage peut relever d'une autre convention (gardiens, concierges, IDCC 1043, EXTRAIT du premier résultat de recherche) |
| Ouvrier agricole qualifié | 1,1 à 1,3 SMIC | Production agricole, paliers 5 à 7 : 13,08 € à 14,50 €/h [R2-09] |
| Assistant(e) administratif(ve) / comptable | 1,4 à 1,6 SMIC | HYPOTHÈSE ; activités hippiques, coeff. 150 « Secrétaire-comptable » : 15,87 €/h, soit 1,29 SMIC [R2-05] |
| Majordome / house manager | 2,0 à 3,0 SMIC (44 800 € à 67 200 €) | HYPOTHÈSE pure, aucune source |
| Régisseur de domaine | 2,0 à 3,0 SMIC (44 800 € à 67 200 €) | HYPOTHÈSE pure : niveau cadre, au-dessus de paysage C5 = 48 510 € [R2-07] et de production agricole palier 12 = 24,16 €/h, soit environ 44 000 €/an [R2-09] |

Les conversions en € sont des ESTIMATIONS : SMIC annuel de 22 404,20 € × coefficient. Le logement de fonction, fréquent pour les gardiens, palefreniers et régisseurs, est un avantage en nature à chiffrer (INCONNU).

## 3. Jardins et parc

### 3.1 Effectifs de jardiniers : exemples réels

| Site | Surface | Jardiniers | Ratio | Statut / source |
|---|---|---|---|---|
| Villandry (Indre-et-Loire), jardins Renaissance et potager décoratif | « 7 hectares de jardin », dont un potager décoratif d'un hectare ; « 30 km de buis, 10 km de charmille, 1000 tilleuls » | « Ils sont dix à s'en occuper au quotidien, même l'hiver ! » | ≈ 1,4 jardinier/ha, soit 0,7 ha par jardinier (ESTIMATION) | PAGE LUE [R2-15], article du 17/01/2024 |
| Vaux-le-Vicomte | « 33 ha » (EXTRAIT, résultat de recherche, source exacte non identifiée) | INCONNU, moteur interne du site sans résultat chiffré | — | Vérification : dossier de presse du domaine |
| Chantilly | parc de « 115 hectares » (EXTRAIT) | INCONNU | — | Vérification : rapport d'activité de la Fondation pour la sauvegarde et le développement du domaine de Chantilly |
| Versailles, Courances, National Trust | — | INCONNU (pas de recherche dédiée, faute de quota) | — | — |

**Lecture (ESTIMATION)** : Villandry est un extrême, un jardin régulier entièrement planté et potager décoratif. Son ratio d'environ 1,4 jardinier/ha est un **plafond** pour le jardin régulier d'exception, pas un ratio de parc.

### 3.2 Coûts d'entretien des espaces verts (€/m²/an)

**INCONNU** :
- la fiche Plante & Cité ouverte [R2-16] (« La gestion différenciée : méthodologie de mise en place », 2014, mise à jour en 2021) décrit les codes qualité, de 1 « prestige » à 4 « rustique », mais **ne donne aucun chiffre** de coût ni de temps ;
- un second document Plante & Cité (file:1079) dépasse 10 Mo et renvoie 403 en téléchargement ;
- extrait DREAL PACA (non ouvert) : « une prairie nécessite deux à trois fois moins d'entretien qu'une pelouse type gazon ».

Vérification : bibliothèque Plante & Cité (« observatoire des coûts » réservé aux adhérents) ; bordereaux de prix unitaires des marchés d'entretien d'espaces verts des collectivités (BOAMP, profils acheteurs).

## 4. Équipements : prix, durée d'amortissement, coût d'usage

### 4.1 Matériel agricole et d'entretien du domaine (réseau cuma, 2025-2026)

Source [R2-30], PAGE LUE : pages lues en image dans le « Guide des coûts de revient des matériels en cuma, Édition Est 2025-2026 », paru en octobre 2025.

Méthode citée par le guide :
- « les chiffres sont issus des comptabilités des cuma de 2023-2024 » de six régions, dont le Centre-Val de Loire ;
- coûts « hors main-d'œuvre, hors carburant et hors consommables » ;
- la colonne « Simulation 2026 » recalcule les coûts « sur la base des prix récents constatés ».

Les prix sont en **HT** : des comptabilités de cuma, et deux fiches portent la mention « €HT ». Pour les autres fiches, c'est une ESTIMATION.

| Matériel | Prix d'achat moyen (parc 2023-2024) | Prix récent « Simulation 2026 » | Durée d'amortissement | Utilisation annuelle de référence | Coût de revient (sans MO ni carburant) |
|---|---|---|---|---|---|
| Tracteur 100-140 CV | 83 098 € | **101 464 €** | 10,7 ans | 576 h | 25,45 €/h (29,43 €/h en simulation 2026) |
| Tracteur 141-160 CV | 106 942 € | 128 719 € | 10,3 ans | 666 h | 26,64 €/h (30,73 €/h) |
| Tracteur spécialisé viti/arbo (compact) | 57 811 € | 81 013 € | 9,7 ans | 467 h | 21,72 €/h (25,02 €/h) |
| Faucheuse rotative portée | 12 654 € | 14 159 € | 9,0 ans | 206 ha | 15,35 €/ha (16,81 €/ha) |
| Faucheuse conditionneuse | 22 450 € | 25 546 € | 9,1 ans | 227 ha | 22,40 €/ha (24,96 €/ha) |
| Faneuse portée | 11 141 € | 13 028 € | 9,7 ans | 194 ha | 13,94 €/ha (15,86 €/ha) |
| Andaineur double rotor | 20 030 € | 25 204 € | 9,6 ans | 262 ha | 14,46 €/ha (18,10 €/ha) |
| Presse à balles rondes | 41 222 € | 50 577 € | 9,4 ans | 3 160 balles | 3,13 €/balle (3,68 €/balle) |
| Épandeur à fumier 6 à 9 t | 30 968 € | 37 390 € | 8,5 ans | 548 voyages | 12,13 €/voyage (14,18 €/voyage) |
| Broyeur d'accotement 1,5 à 2,2 m | 10 247 € | 11 910 € | 8,2 ans | 104 h | 30,85 €/h (33,65 €/h) |
| Chargeur télescopique (3,6 t) | 84 445 € | 100 956 € | 9,4 ans | 632 h | 25,88 €/h (29,25 €/h) |

**Effet d'échelle, essentiel pour un domaine** (même source, graphiques « coût total en fonction du volume annuel ») :
- faucheuse rotative : 30,2 €/ha sous 100 ha/an, contre 6,6 €/ha au-delà de 250 ha/an ;
- broyeur d'accotement : 56,4 €/h sous 50 h/an, contre 14,3 €/h au-delà de 150 h/an ;
- tracteur 100-140 CV : 34,4 €/h sous 400 h/an, contre 19,1 €/h au-delà de 700 h/an.

Avec 35 à 120 ha de prés, un domaine utilise peu son matériel. Posséder une chaîne de fenaison complète (faucheuse, faneuse, andaineur, presse, environ 100 000 € à prix 2026) coûte cher à l'hectare. Les alternatives sont l'adhésion à une cuma, une entreprise de travaux agricoles ou la vente d'herbe (risque de bail rural : R3). Un résultat de recherche (et non le guide) indique un coût de main-d'œuvre de chauffeur de « 18 à 25 €/h » toutes charges comprises dans le barème d'entraide 2023 (EXTRAIT, non ouvert).

### 4.2 Budget de renouvellement par scénario (ESTIMATION)

Méthode : prix « Simulation 2026 » [R2-30] divisé par la durée d'amortissement, soit une annuité de renouvellement HT hors frais financiers. Les parcs sont des HYPOTHÈSES de modélisation.

| Scénario | Parc type (HYPOTHÈSE) | Valeur à neuf (ESTIMATION) | Renouvellement annuel (ESTIMATION) |
|---|---|---|---|
| S1 (50 ha) | 1 tracteur compact (81 000 €), 1 broyeur d'accotement (11 900 €), 1 épandeur 6-9 t (37 400 €), petit matériel. Fenaison sous-traitée. Tondeuses et utilitaire : INCONNU | ≈ 130 000 € hors tondeuses et utilitaire | ≈ 14 000 €/an (81 013/9,7 + 11 910/8,2 + 37 390/8,5 = 8 352 + 1 452 + 4 399) + tondeuses et véhicules (INCONNU) |
| S2 (120 ha) | 1 tracteur 100-140 CV (101 500 €), 1 tracteur compact (81 000 €), 1 télescopique (101 000 €), 1 épandeur (37 400 €), 1 broyeur (11 900 €), chaîne de fenaison (faucheuse 14 200 €, faneuse 13 000 €, andaineur 25 200 €, presse 50 600 €) | ≈ 436 000 € | ≈ 45 000 €/an (somme des prix divisés par leur durée) |
| S3 (300 ha) | S2 + un second tracteur de 141-160 CV (128 700 €) et du matériel forestier (INCONNU) | ≈ 565 000 € et plus | ≈ 58 000 €/an et plus (45 350 + 128 719/10,3) |

**INCONNU** :
- prix et durée de vie des tondeuses autoportées et des microtracteurs de parc, des véhicules utilitaires, du matériel de carrière (herse, niveleuse) et des voiturettes électriques. Vérification : tarifs publics de constructeurs ou de concessionnaires (Kubota, Iseki, John Deere, Etesia), ou barème des UGAP ou des marchés publics d'espaces verts ;
- camion à chevaux : seule donnée trouvée, datée de 2012 [R2-18] : « env. 35000€ TTC pour un camion d'occasion pour 2 chevaux, et au minimum 50000€ TTC pour un modèle neuf ». Prix 2026 : INCONNU.

## 5. Terres

### 5.1 Fermages

Source [R2-20], PAGE LUE : arrêté préfectoral de l'Aveyron du 29 septembre 2025.
- Indice national : « L'indice national des fermages est constaté pour 2025 à la valeur de 123,06. Sa valeur était de 122,55 en 2024. La variation de cet indice entre 2024 et 2025 est de + 0,42 % ». Il s'applique aux échéances du 1er octobre 2025 au 30 septembre 2026. L'arrêté vise « l'arrêté du ministre de l'agriculture et de l'alimentation en date du 23 juillet 2025 ».
- Minima et maxima pour les nouveaux baux 2025-2026 en Aveyron (valeur du point : 2,01 €) :

| Catégorie | Minimum | Maximum |
|---|---|---|
| Terres labourables | 92,46 €/ha | 261,30 €/ha |
| Pâtures | 52,26 €/ha | 170,85 €/ha |
| Parcours, landes ou pâtures peu productives | 6,03 €/ha | 100,50 €/ha |
| Bâtiment d'élevage | 2,01 €/UGB | 56,28 €/UGB |
| Bâtiment sans équipement | 12,06 € par tranche de 10 m² | 30,15 € par tranche de 10 m² |
| Maison d'habitation (bail rural), loyer mensuel | 1,75 €/m² | 6,66 €/m² |

**Lecture (ESTIMATION)** : louer ses prés en fermage rapporte au plus quelques centaines d'euros par hectare et par an. En Aveyron, une pâture rapporte 52 à 171 €/ha/an. Les 35 ha de prés de S1 donneraient environ 1 800 à 6 000 €/an ; les 80 ha de S2, environ 4 200 à 13 700 €/an. En contrepartie, le bail rural fait perdre la maîtrise du foncier (statut du fermage : voir R3). Les minima et maxima varient fortement d'un département à l'autre. **INCONNU** pour les départements de châteaux typiques (Centre-Val de Loire, Normandie, Île-de-France). Vérification : arrêté préfectoral annuel publié au recueil des actes administratifs, ou DDT/DRAAF du département retenu.

### 5.2 Foin et paille

| Donnée | Valeur | Année / périmètre | Statut / source |
|---|---|---|---|
| Foin de prairie naturelle, départ ferme, grandes bottes | 102 à 107 €/t brute | 2024, Yonne (Bourgogne-Franche-Comté) | EXTRAIT [R2-21], PDF devenu 404 |
| Foin de luzerne ou riche en légumineuses, départ ferme | 117 à 127 €/t brute | 2024, Yonne | EXTRAIT [R2-21] |
| Foin sur pied, 1re coupe, prairie naturelle | 64 à 69 €/t brute | 2024, Nouvelle-Aquitaine | EXTRAIT [R2-22] |
| Foin sur pied, 2e coupe | 91 à 99 €/t brute | 2024, Nouvelle-Aquitaine | EXTRAIT [R2-22] |
| Paille, valeur retenue dans un calcul de chambre | 70 €/t | 2024, Nouvelle-Aquitaine | EXTRAIT [R2-22] |
| Paille en andain, non pressée | 25 à 30 €/t, soit 100 à 120 €/ha pour 4 t/ha | 2025, Hauts-de-France | EXTRAIT [R2-23], source exacte non ouverte |
| Fumier de bovins en tas à la ferme | 18 à 22 €/t | 2025, Hauts-de-France | EXTRAIT [R2-23] |
| Foin dans la fiche IFCE (prix ancien) | 200 €/t, orge 260 €/t | 2011-2012 | PAGE LUE [R2-17] |

**Lecture (ESTIMATION)** :
- Les barèmes des chambres sont des prix **départ ferme, sans transport ni livraison**.
- Le foin « cheval », livré, en petites bottes, de qualité contrôlée, coûte nettement plus cher. Le prix IFCE de 2012 (200 €/t) donne un ordre de grandeur. Prix 2025-2026 du foin livré pour chevaux : **INCONNU**. Vérification : relever 10 annonces de fournisseurs ou de négociants de la région retenue, ou les barèmes « paille et fourrages » de la chambre d'agriculture.
- Autoproduction possible : un domaine de 35 à 120 ha de prés peut produire son foin. Rendement et coût de production : **INCONNU** (barème d'entraide ou coût des chantiers de fauche ; voir §4).

### 5.3 Prairies et clôtures

- **Entretien de prairie par un professionnel** (désherbage, travail du sol, semis) : « il faut compter 120€/ha ». Source : IFCE 2012, qui cite la chambre d'agriculture 87 [R2-17], PAGE LUE, prix ancien.
- **Entretien des prairies hors récolte** : environ 185 €/ha/an. Source : chambres d'agriculture des Hauts-de-France, données de 2008 [R2-26], EXTRAIT.
- **Clôture électrique** : « Le coût d'aménagement de la clôture, pour une surface de 0,5 ha, peut varier de 500 à 650€, électrificateur compris » [R2-17], PAGE LUE, 2012. ESTIMATION : un carré de 0,5 ha a un périmètre d'environ 283 m, soit environ 1,8 à 2,3 €/ml pour un simple fil électrique en autopose.
- **Clôtures de prestige** (lices bois, poteaux châtaignier, grillage à chevaux) : **INCONNU** pour le prix au mètre linéaire et la durée de vie. Vérification : devis de clôturistes, ou référentiel prix bâtiment équin de la chambre de Normandie [R2-29] lorsque le site sera rétabli. **HYPOTHÈSE de modèle** : provision de clôtures = linéaire × coût au mètre / durée de vie, avec 20 à 60 €/ml posé et 15 à 25 ans. Ces valeurs ne sont pas sourcées : à remplacer.

### 5.4 Forêt

**INCONNU** dans R2 : faute de quota, aucune recherche n'a porté sur les coûts de gestion forestière (CNPF, Fransylva, ONF). Le revenu net forestier par hectare est dans le périmètre de R8 (« Forêt : revenu net €/ha/an »). À rapprocher de R8. Vérification : indicateur annuel du marché des forêts (Société forestière, Experts forestiers de France, SAFER) ; tarifs des gestionnaires forestiers professionnels ; documents de gestion durable (seuil de surface rendant obligatoire un plan simple de gestion : à vérifier par R3).

## 6. Chevaux

### 6.1 Coût annuel d'un cheval : références de l'IFCE (anciennes, 2011-2012)

**Attention : prix de 2011-2012**, à actualiser. Ce sont des montants payés par un particulier, donc vraisemblablement TTC (ESTIMATION : les fiches ne le précisent que pour le camion).

**Fiche n°1 IFCE, cheval de loisir au pré chez son propriétaire** [R2-17], PAGE LUE :
- total annuel : « 650 à 1310 € » ;
- ration complémentaire de « 4 kg de foin (200€/T) et 1kg d'orge (260€/T) », pour un cheval qui dispose d'un demi-hectare ;
- eau : « Un cheval consomme en moyenne 40L eau/jour soit environ 15m3 par an » ; « en 2012 4€ le m3 en moyenne » ;
- soins : vermifuge « 20€ en moyenne », vaccin tétanos-grippe « 60€ », dentiste « env. 60€ », ostéopathe « env. 80€ » ;
- maréchalerie : « environ 40€ le parage », « environ 75€ la ferrure, à renouveler après 6 à 8 semaines » ;
- prairie : « Pour l'entretien d'une prairie par un professionel (désherbage, travail du sol, semis), il faut compter 120€/ha » (source citée : Chambre d'agriculture 87) ;
- abri : un petit tunnel agricole de 10 m × 8 m × 3,90 m coûte « au minimum 5 000€ ».

**Fiche n°4 IFCE, cheval de compétition amateur en pension box** [R2-18], PAGE LUE :
- total annuel : « 6100 à 14600 € » ;
- hébergement : « de 3000€ (pension box) à 8400€ (pension box/paddock/travail) » ; « pensions box sans sortie du cheval (de 250€ à 400€/mois) », « pensions box avec sortie au paddock et travail du cheval (de 400€ à 700€/mois) » (source citée : IFCE 2011, zone périurbaine) ;
- soins : « de 270€ (vaccins, vermifuges, dentiste, ostéopathe 1 fois) à 500€ » ; vaccin tétanos-grippe-rhinopneumonie « 70€ en moyenne » ; exemple d'une colique « 200€ » ;
- maréchalerie : « de 525€ (7 ferrures complètes) à 1040€ (8 ferrures spéciales) » ; ferrure spéciale « jusqu'à environ 130€ » ;
- assurance : pour un cheval de CSO de 5 000 €, « environ 150€/an pour être assuré contre le vol et la mortalité, et de 300€ à 600€/an pour une assurance frais vétérinaires » ;
- transport : « env. 35000€ TTC pour un camion d'occasion pour 2 chevaux, et au minimum 50000€ TTC pour un modèle neuf » ; van 1,5 place neuf « env. 6000€ ».

Recoupement : la préfecture de Maine-et-Loire indique un coût annuel de 650 € à 1 300 € pour un cheval au pré [R2-19], EXTRAIT. Le chiffre est cohérent avec la fiche n°1.

### 6.2 Ration réelle par cheval : cas d'une écurie de 40 pensions (données 2008-2010)

Source [R2-24], PAGE LUE, témoignage d'exploitants présenté à l'IFCE en 2011. Il s'agit d'une écurie de pension près de Montpellier, avec des chevaux de 450 à 650 kg au travail léger. Quantités par cheval et par an (« enquête éleveur 2008 ») :
- « 900 kg d'orge à 160 €/T » ;
- « 2,7 T de foin à 180 €/T (une augmentation de 172 à 192 €/T de 2007 à 2009) » ;
- « 0,8T de paille à un prix moyen de 100 €/T ».

Résultat : « Coût moyen de la ration par an : 760 € ». Le témoignage ajoute : « Coût moyen de l'alimentation dans les autres exploitations est plus élevé (30 à 35%) et l'écart varie de 760 € à 1 090 €/ cheval ». La litière est surtout de la « sciure, copeaux et très peu de paille ».

**Actualisation (ESTIMATION, à valider)** : 2,7 t de foin × 105 à 200 €/t, soit 280 à 540 €, plus l'orge ou les granulés et la litière. Le budget « alimentation + litière » d'un cheval au box se situe vraisemblablement **entre 1 000 € et 2 000 €/an en 2026**. Cette fourchette est large : les prix 2026 du foin livré, des granulés et des copeaux sont INCONNUS (voir §5.2). HYPOTHÈSE de modèle : 1 500 €/cheval/an TTC.

### 6.3 Ratio de personnel : chevaux par soigneur

| Cas | Chevaux | Personnel | Ratio (ESTIMATION) | Statut / source |
|---|---|---|---|---|
| Écurie de pension, Hérault, 2010 | « 40 pensions » (38 à 40 équidés) | « 2 ETP exploitants + 1 ETP palefrenier + 1 apprenti » | ≈ 10 à 13 chevaux par ETP, enseignement et gestion compris | PAGE LUE [R2-24] |
| Même cas : distribution des repas | 40 chevaux, 5 repas | « Durée de distribution totale 1h 30 par jour » | — | PAGE LUE [R2-24] |
| Centre équestre + pension (monographie, données 2019) | 54 équidés dont 25 en pension | 3 UMO | ≈ 18 équidés par UMO | EXTRAIT [R2-25] |

**HYPOTHÈSE de modèle** : en écurie de propriétaire haut de gamme (box, sorties quotidiennes au paddock, 7 jours sur 7, remplacements pendant les congés), compter **8 à 12 chevaux par ETP de soins**. La valorisation (travail monté) et l'enseignement sont à ajouter. À valider avec les références IFCE et Réseau Équin (synthèse nationale « Écuries de pension » 2023, données 2021 : PDF devenu 404).

## 7. Installations équestres : investissement et durée de vie

**Avertissement sur les sources.**
- La meilleure source repérée, le « référentiel prix bâtiment équin » de la chambre d'agriculture de Normandie [R2-29], n'a pas pu être lue. Le 14/10/2026, le site renvoie : « Le site web du réseau des Chambres d'agriculture auquel vous souhaitez accéder est actuellement en maintenance ». **À relire en priorité** lors de la vague 2.
- Les prix ci-dessous viennent d'un **site commercial** (HelloPro) qui ne précise pas HT ou TTC. Fiabilité faible.

| Élément | Prix relevé | Statut / source |
|---|---|---|
| Manège couvert clé en main 40 × 20 m (800 m²) | « Entre 40 000 € et 100 000 € » ; budget moyen « autour de 85 000 € » | PAGE LUE [R2-27] |
| Manège en kit | « Entre 27 000 € et 65 000 € » ; structure seule d'environ 865 m² : « entre 35 000 € et 37 000 € » | PAGE LUE [R2-27] |
| Terrassement | 5 à 15 €/m² | PAGE LUE [R2-27] |
| Fondations standard / renforcées | 10 à 15 €/m² / 20 à 27 €/m² | PAGE LUE [R2-27] |
| Sol : sable classique / sable fibré | 3 à 8 €/m² / 10 à 15 €/m² | PAGE LUE [R2-27] |
| Éclairage | 15 à 40 €/m² | PAGE LUE [R2-27] |
| Étude de sol G2 | 500 à 5 000 € | PAGE LUE [R2-27] |
| Durée de vie de la structure | acier galvanisé 30 à 40 ans ; bois massif 20 à 30 ans ; lamellé-collé 25 à 30 ans | PAGE LUE [R2-27] |
| Box 3 × 3 m / 3 × 4 m | 1 800 à 7 000 € / 2 200 à 8 500 € | PAGE LUE [R2-28] |
| Box en kit / en bois / maçonné | 1 000 à 6 000 € / 1 500 à 10 000 € / 5 000 à 25 000 € | PAGE LUE [R2-28] |
| Box de poulinière | 3 000 à 12 000 € | PAGE LUE [R2-28] |
| Abreuvoir automatique | 150 à 800 € | PAGE LUE [R2-28] |
| Box aménagé dans un bâtiment existant, en autoconstruction | ≈ 1 000 € par box | EXTRAIT [R2-26], ancien |
| Carrière extérieure | 15 000 à 75 000 € selon le sol et le drainage | EXTRAIT (moteur de recherche, source exacte non identifiée) |

**ESTIMATIONS pour les scénarios.** Elles reposent sur les prix ci-dessus et sont à remplacer par des devis.
- **Manège de 60 × 25 m (1 500 m²)** : 85 000 € / 800 m² ≈ 106 €/m², soit environ 160 000 € pour la structure clé en main. S'y ajoutent le sol fibré (15 000 à 22 500 €), l'éclairage (22 500 à 60 000 €) et le terrassement et les fondations (22 500 à 63 000 €). Total d'environ **220 000 à 305 000 €**, avec une **fiabilité faible**. L'addition est peut-être en partie redondante si le prix clé en main inclut déjà les fondations ou le sol. Un manège de standing pour un domaine classé, avec bardage bois, insertion paysagère et avis de l'architecte des Bâtiments de France, coûtera vraisemblablement plus. Montant INCONNU.
- **Boxes haut de gamme** : 8 000 à 25 000 € par box en écurie neuve maçonnée (HYPOTHÈSE dans la fourchette [R2-28]). 40 boxes coûteraient donc environ 0,3 à 1 M€. La réhabilitation d'écuries historiques relève du bâti (R1).
- **Renouvellement annuel (provision)** :
  - sol de carrière et de manège : remise à niveau, à chiffrer. Durée de vie du sol INCONNUE (vérification : fournisseurs de sols équestres, IFCE) ;
  - structure du manège : 1/30 par an ;
  - boxes : 1/20 à 1/30 par an (HYPOTHÈSE).

## 8. Flux de l'écurie : eau, électricité, fumier

### 8.1 Eau

| Donnée | Valeur | Statut / source |
|---|---|---|
| Consommation d'eau d'un cheval | « Un cheval consomme 15 à 60 L d'eau par jour et produit 9 à 10 L d'urine » | PAGE LUE [R2-32] |
| Consommation moyenne (cheval au pré) | « 40L eau/jour soit environ 15m3 par an » ; « en 2012 4€ le m3 en moyenne » | PAGE LUE [R2-17], 2012 |
| Fourrage consommé | « entre 8 à 12 kg de fourrage par jour » ; « 15 à 17 kg de crottins par jour » | PAGE LUE [R2-32] |

ESTIMATION eau, hors lavage, douches, arrosage des carrières et sanitaires :
- 40 chevaux × 40 L × 365 j ≈ 584 m³/an. À 4 à 5 €/m³, cela représente environ 2 300 à 2 900 €/an. Le prix de l'eau en 2026 est INCONNU ; la valeur de 4 €/m³ date de 2012 [R2-17].
- L'arrosage d'une carrière peut dépasser de loin ce volume : INCONNU.

### 8.2 Électricité

**INCONNU** : aucune source trouvée sur la consommation électrique d'une écurie (kWh par box et par an : éclairage, abreuvoirs chauffants, solarium, marcheur, éclairage du manège). Vérification : références IFCE et Réseau Équin (synthèse écuries de pension), ou factures d'une écurie existante. Les prix de l'électricité sont traités par R1.

### 8.3 Fumier : quantités, réglementation, coût

**Quantités**
- [R2-32] : « la quantité de fumier produite par un cheval au box peut-être de 5 à 14 tonnes par an » ; « 12,8 tonnes/an de fumier pour un cheval hébergé majoritairement en box ».
- Litière utilisée par box et par an, pour 12 cm d'épaisseur [R2-31] : paille 2,6 t ; copeaux 1,8 t ; pellets de bois 1,1 t ; paille en pellets 2,4 t ; tourbe 2 t.
- Fumier produit par box et par an [R2-31] : paille 6 à 7,7 t ; copeaux 6 à 11 t ; pellets de bois 5,6 t ; paille en pellets 6,5 t.
- Exemple IFCE [R2-31] : « 30 chevaux au box 24/24, 365 j/an », « 35 kg/jour/chl », soit « 383,2 tonnes/ an ».

**Réglementation**
- Règles de stockage du Règlement sanitaire départemental (RSD) [R2-32], distances d'implantation des bâtiments d'élevage et du stockage du fumier :
  - « 200 m pisciculture et zones de baignades » ;
  - « 50 m habitations et zones de loisirs » ;
  - « 35 m sources eau, berges puits, forages » ;
  - « 5 m routes ».
- Fumière [R2-32] : sur aire étanche avec point bas ou collecte des lixiviats, sous une surface couverte, ou en benne étanche. « La fumière doit pouvoir contenir une production de fumier équivalente à 2 mois de stockage », soit « 2 m2 /cheval pour 2 mois », « 3,35 m2 /cheval pour 4 mois », « 4,6 m2 /cheval pour 6 mois ». Source citée par l'IFCE : DEXEL, Idele 2018 [R2-31].
- Le RSD varie selon le département. En zone vulnérable nitrates, des règles plus strictes s'appliquent (EXTRAIT, résultat de recherche). **Point à faire vérifier par R3** : statut ICPE éventuel d'une grande écurie (la mission le pose comme question).

**Coût** (exemple réel non daté, d'une entreprise dont l'effectif n'est pas précisé, [R2-32]) :

> « Annuellement, la gestion du fumier coûte à cette entreprise :
> - Paille : 15 500 euros par an
> - Matériel : 7 920 euros de coût d'utilisation du tracteur et du télescopique par an uniquement pour la gestion du fumier
> - Carburant : 1 568 euros […]
> - Main d'œuvre : 4 608 euros par an uniquement pour la gestion du fumier
>
> Soit : 29 596 euros par an. Soit 89 pensions (331 euros de moyenne par pension) »

Autres éléments du même guide [R2-32] :
- « Coût du compostage : 60 à 80 €/ha » et « Diminution de 30 à 50 % de la masse du fumier » ;
- des exploitants peuvent « payer plusieurs milliers d'euros à des prestataires extérieurs pour l'évacuer » ;
- coût moyen d'un trouble musculosquelettique (TMS) en régime agricole en 2015 : « 26 700 € (source observatoire des TMS de la MSA) ».

**Valeur de revente du fumier** : fumier de bovins en tas de 18 à 22 €/t (2025, Hauts-de-France, EXTRAIT [R2-23]). Prix du fumier de cheval et marché local (champignonnières, maraîchers, échange paille contre fumier) : INCONNU.

**ESTIMATION pour le modèle** :
- 40 chevaux au box × 10 à 12,8 t = 400 à 510 t de fumier par an, soit environ 80 m² de fumière pour 2 mois (2 m² par cheval) ou 185 m² pour 6 mois (4,6 m² par cheval).
- Si le fumier est épandu ou composté sur les prés du domaine (50 à 120 ha), le coût se réduit au matériel, au carburant et à la main-d'œuvre. Le coût d'évacuation par un prestataire est INCONNU (« plusieurs milliers d'euros »).

## 9. Synthèse : effectifs et coûts chargés S1, S2, S3

### 9.1 Méthode et statut

- Les **effectifs** sont des HYPOTHÈSES de modélisation, construites à partir de quatre éléments :
  - le ratio de Villandry (≈ 1,4 jardinier/ha de jardin régulier d'exception) [R2-15], utilisé comme plafond ;
  - un ratio de 10 chevaux par ETP de soins, déduit des cas [R2-24] et [R2-25] (≈ 10 à 18 équidés par ETP) ;
  - les ordres de grandeur du Contexte permanent (2 à 3 ; 8 à 12 ; 20 à 30 ETP) ;
  - le jugement de l'agent. **Aucune source ne valide directement ces effectifs.**
- Les **niveaux de salaire** sont des HYPOTHÈSES exprimées en multiples du SMIC (§2.2).
- Le **coût employeur** vient de la grille du simulateur officiel URSSAF [R2-11] (ESTIMATION) : effectif 10 pour S1, effectif 25 pour S2 et S3.
- Le **personnel de maison employé par le propriétaire à titre privé** (particulier employeur) n'a pas droit à la RGDU. Son coût est estimé à **brut × 1,30**. Calcul : environ 44 % de cotisations (taux du régime général avant réduction, ESTIMATION §1.2), moins la déduction de 2 €/h [R2-12] sur environ 13 à 18 €/h, soit un ratio de 1,29 à 1,33. Cette estimation est **fragile** : à vérifier avec le simulateur CESU ou un expert-comptable.
- Le coût est annualisé sur 12 mois. Il **exclut** : 13e mois et primes, logement de fonction (avantage en nature), astreintes et heures supplémentaires de week-end, intérim, saisonniers, formation au-delà des obligations légales, médecine du travail, tenues, véhicules de service.

### 9.2 S1 : domaine relativement économique (50 ha, 12 boxes)

| Poste (HYPOTHÈSE) | ETP | Brut (× SMIC) | Coût employeur / ETP | Coût annuel |
|---|---|---|---|---|
| Jardinier / homme d'entretien (parc de 3 ha, abords) | 1,0 | 1,2 | 32 391 € | 32 391 € |
| Soigneur d'écurie (12 boxes) + remplacements | 1,2 | 1,0 | 23 853 € | 28 624 € |
| Employé(e) de maison (partie privée, particulier employeur) | 0,5 | 1,1 | 32 038 € (× 1,30) | 16 019 € |
| **Total S1** | **2,7** | | | **≈ 77 000 €/an** |

Non compris : fenaison et entretien des prés sous-traités (§4) ; foin acheté ; gardiennage. Le propriétaire assure lui-même une partie du travail. **Leçon de méthode n°3 du contexte** : le temps du fondateur est limité.

### 9.3 S2 : grand domaine équestre haut de gamme (120 ha, 40 boxes)

| Poste (HYPOTHÈSE) | ETP | Brut (× SMIC) | Coût employeur / ETP | Coût annuel |
|---|---|---|---|---|
| Régisseur de domaine | 1,0 | 2,5 | 79 253 € | 79 253 € |
| Chef jardinier | 1,0 | 1,75 | 53 470 € | 53 470 € |
| Jardiniers (2 ha à la française + 8 ha de parc) | 2,0 | 1,2 | 32 531 € | 65 062 € |
| Responsable d'écurie | 1,0 | 1,4 | 40 479 € | 40 479 € |
| Soigneurs (40 boxes, 10 chevaux par ETP) | 3,0 | 1,0 | 23 973 € | 71 919 € |
| Cavalier (valorisation) | 1,0 | 1,3 | 36 566 € | 36 566 € |
| Gardien / homme d'entretien des bâtiments | 1,0 | 1,3 | 36 566 € | 36 566 € |
| Ouvrier agricole (80 ha de prés, clôtures, foin) | 1,0 | 1,2 | 32 531 € | 32 531 € |
| Gouvernante (particulier employeur) | 1,0 | 1,4 | 40 776 € (× 1,30) | 40 776 € |
| Employé(e) de maison (particulier employeur) | 1,0 | 1,1 | 32 038 € (× 1,30) | 32 038 € |
| **Total S2** | **13,0** | | | **≈ 489 000 €/an** |

**Lecture** : avec une écurie pleine de 40 chevaux et des jardins réguliers de 2 ha, on obtient 13 ETP, au-dessus de la fourchette de 8 à 12 ETP du contexte. Pour rester entre 8 et 12, il faut ramener l'écurie à environ 20 chevaux, sous-traiter les jardins ou supprimer le cavalier.

### 9.4 S3 : domaine historique ultra-premium (300 ha, 40 à 60 boxes)

| Poste (HYPOTHÈSE) | ETP | Brut (× SMIC) | Coût employeur / ETP | Coût annuel |
|---|---|---|---|---|
| Régisseur de domaine | 1,0 | 3,0 | 96 730 € | 96 730 € |
| Assistant(e) administratif(ve) / comptable | 1,0 | 1,5 | 44 289 € | 44 289 € |
| Chef jardinier | 1,0 | 2,0 | 62 277 € | 62 277 € |
| Jardiniers des jardins réguliers et du potager (10 ha ; 0,8 ETP/ha, sous le plafond de Villandry de 1,4) | 8,0 | 1,2 | 32 531 € | 260 248 € |
| Jardiniers du parc (50 ha, mécanisé) | 3,0 | 1,1 | 28 346 € | 85 038 € |
| Responsable d'écurie | 1,0 | 1,5 | 44 289 € | 44 289 € |
| Soigneurs (50 boxes, 10 chevaux par ETP) | 4,0 | 1,0 | 23 973 € | 95 892 € |
| Cavaliers (valorisation) | 2,0 | 1,3 | 36 566 € | 73 132 € |
| Gardiens / maintenance des bâtiments | 2,0 | 1,3 | 36 566 € | 73 132 € |
| Ouvriers agricoles et forestiers (120 ha de prés + 120 ha de bois) | 2,0 | 1,2 | 32 531 € | 65 062 € |
| Majordome / house manager (particulier employeur) | 1,0 | 2,5 | 72 814 € (× 1,30) | 72 814 € |
| Gouvernante (particulier employeur) | 1,0 | 1,5 | 43 688 € (× 1,30) | 43 688 € |
| Employé(e)s de maison (particulier employeur) | 2,0 | 1,1 | 32 038 € (× 1,30) | 64 076 € |
| **Total S3** | **29,0** | | | **≈ 1 081 000 €/an** |

**Sensibilité (ESTIMATION)** :
- **Salaires.** Aux bas niveaux, chaque +0,1 SMIC augmente le coût employeur du poste de 12 % à 18 %, car la RGDU fond vite : de 1,0 à 1,1 SMIC, +18,3 % (23 853 € → 28 216 €) ; de 1,1 à 1,2, +14,8 % ; de 1,2 à 1,3, +12,4 % [R2-11]. Une revalorisation salariale coûte donc près de deux fois plus que la hausse du brut.
- **Jardins de S3.** Au ratio de Villandry (1,4 ETP/ha), les jardiniers des 10 ha seraient 14 au lieu de 8, soit environ +195 000 €/an.

### 9.5 Coût annuel par cheval et par box (cheval logé au box sur le domaine, configuration S2)

| Poste | Fourchette (€/an par cheval) | Statut | Source / calcul |
|---|---|---|---|
| Main-d'œuvre de soins (responsable + 3 soigneurs pour 40 chevaux) | 2 810 | ESTIMATION sur HYPOTHÈSES | (40 479 + 3 × 23 973) / 40, d'après [R2-11] |
| Valorisation (cavalier), optionnelle | 914 | ESTIMATION sur HYPOTHÈSES | 36 566 / 40 |
| Alimentation + litière | 1 000 à 2 000 (HYPOTHÈSE centrale 1 500) | HYPOTHÈSE | Part sourcée : foin 2,7 t × 105 à 200 €/t = 284 à 540 € [R2-24, R2-21, R2-17] ; paille 2,6 t × 70 €/t ≈ 182 € [R2-31, R2-22]. Concentrés et copeaux : prix 2026 INCONNUS |
| Maréchalerie (7 ferrures complètes à 8 ferrures spéciales) | 525 à 1 040 | PAGE LUE, **prix 2012** | [R2-18] |
| Soins vétérinaires de base (vaccins, vermifuges, dentiste, ostéopathe) | 270 à 500 | PAGE LUE, **prix 2012** | [R2-18] |
| Provision pour accidents et maladies | 300 à 500 | HYPOTHÈSE | exemples IFCE 2012 : colique 200 €, tendon 130 € [R2-18] |
| Assurance mortalité-vol + frais vétérinaires (cheval de 5 000 €), optionnelle | 450 à 750 | PAGE LUE, **prix 2012** | [R2-18] : 150 € + 300 à 600 € |
| Eau (40 L/jour, 15 m³) | ≈ 60 | PAGE LUE, prix 2012 | [R2-17] |
| Épandage du fumier (12,8 t, épandeur de 8,1 t) | ≈ 22, plus le temps de tracteur | ESTIMATION | 12,8 / 8,1 ≈ 1,6 voyage × 14,18 € [R2-32, R2-30] |
| Électricité | INCONNU | — | — |
| Provision pour les installations (box 8 000 à 25 000 € sur 25 ans ; manège de 220 000 à 305 000 € sur 30 ans ; 2 carrières de 15 000 à 75 000 € sur 15 ans) | 550 à 1 500 | ESTIMATION, fiabilité faible | 320 à 1 000 € + 183 à 254 € + 50 à 250 €, pour 40 boxes [R2-27, R2-28], §7. Durées de 25 ans pour le box et de 15 ans pour la carrière : HYPOTHÈSES |
| **Total par box occupé, hors valorisation et hors assurance** | **≈ 5 500 à 8 500** | ESTIMATION | somme des lignes |
| **Total avec assurance et valorisation** | **≈ 6 900 à 10 100** | ESTIMATION | 5 537 + 450 + 914 ; 8 432 + 750 + 914 |

**Recoupement** : en 2011, l'IFCE observait des pensions de « 250€ à 400€/mois » en box seul et de « 400€ à 700€/mois » avec paddock et travail, soit 3 000 € à 8 400 €/an [R2-18]. Le coût complet estimé pour 2026, de 5 500 € à 8 500 €, est du même ordre que le prix d'une pension haut de gamme. La marge d'une pension dépend donc de son prix 2026, qui relève de R6. **Prix 2026 du box en écurie professionnelle** : non recherché ici, il relève de R6 (« Pension : prix par région et par niveau de service »).

**Box vide** : la provision pour installations (550 à 1 500 €/an) reste due, et la main-d'œuvre ne baisse que par paliers d'un ETP.

## 10. Contre-exemples et cas d'échec trouvés

Le périmètre de R2 porte sur des coûts. Les liquidations et les reventes de domaines relèvent de R4. Les signaux d'échec ou de risque trouvés sont les suivants.

1. **Pénurie de main-d'œuvre équestre.** Dans le secteur sport et loisir, en 2022, 757 offres d'équi-ressources ont été « annulées », contre 1 491 pourvues, soit environ un tiers des offres non abouties (ESTIMATION). « Palefrenier soigneur / Garçon de cour & Enseignant d'équitation représentent 46% des offres » [R2-14]. Risque pour un domaine : postes vacants, recours à l'intérim, surcharge du propriétaire.
2. **Minima conventionnels dépassés par le SMIC.** Après la revalorisation du 1er juin 2026, plusieurs échelons sont passés sous le SMIC : paysage O.1 à O.3, E.1 et E.2 [R2-07] ; activités hippiques, coefficients 100 à 109 [R2-05] ; production agricole, paliers 1 à 3 [R2-09]. Une masse salariale proche du SMIC suit donc mécaniquement l'inflation. Elle dépend aussi des paramètres de la RGDU, réformée en 2026 [R2-02], ce qui crée un **risque politique** sur le coût du travail peu qualifié.
3. **Une écurie de pension a eu besoin d'un revenu extérieur pour démarrer** [R2-24]. Parmi les « clefs de réussite » de l'écurie Artaud (40 pensions en 2010, après 14 ans) figure : « Installation progressive (1 revenu extérieur pendant 4 ans, investissements progressifs) ». C'est un contre-exemple à l'autofinancement immédiat d'une activité équestre.
4. **Le fumier, un coût caché.** Selon le guide MSA [R2-32], les chefs d'entreprise ne chiffrent pas ce coût (« j'ai jamais compté ça »). Certains paient « plusieurs milliers d'euros à des prestataires extérieurs pour l'évacuer ». Dans un exemple réel, la gestion du fumier coûte 29 596 €/an. Le coût moyen d'un TMS en régime agricole était de 26 700 € en 2015.
5. **Pas d'économie d'échelle sur le matériel.** Une faucheuse coûte 30,2 €/ha sous 100 ha/an, contre 6,6 €/ha au-delà de 250 ha [R2-30]. Posséder sa chaîne de fenaison sur 35 à 80 ha de prés est coûteux.
6. **Charge de travail sous-estimée.** Pour un seul cheval à domicile, l'IFCE indique que le temps consacré à l'entretien, notamment l'alimentation, « peut aller jusqu'à 2H par jour » [R2-17], et qu'il faut « prévoir une solution de remplacement en cas d'absence ».

## 11. Points de doute / hypothèses non vérifiées

1. **Date du SMIC à 12,31 €.** Le 1er juin 2026 est déduit de la page RGDU (« revalorisation du Smic au 1er juin 2026 ») et de la référence à l'arrêté du 22 mai 2026, dont le texte n'a pas été lu (Légifrance bloqué).
2. **Coût employeur.** Il est calculé par le simulateur URSSAF avec ses valeurs par défaut (AT/MP 2,08 %, mutuelle de 40 €/mois à 50 %, effectif 10 ou 25). Ce calcul ne couvre pas les spécificités MSA des salariés agricoles et équestres, ni les vrais taux AT/MP du paysage et de l'équitation (INCONNUS). La page URSSAF des taux est restée inaccessible.
3. **Particulier employeur.** Le coefficient de 1,30 appliqué au brut est une ESTIMATION fragile. La correspondance entre niveaux et emplois de l'IDCC 3239 est INCONNUE, tout comme la durée conventionnelle exacte (40 h, déduite des 174 h par mois).
4. **Grilles 3239 et 7026.** Elles viennent de sites secondaires (fiche-paie.net, juristique.org). L'extension de l'avenant 7026 n°6 était « en attente ». L'avenant 7024 n°11 du 2 juillet 2026 (+1,96 %) n'est connu que par un extrait.
5. **Salaires de marché** (régisseur, chef jardinier, majordome, gouvernante, responsable d'écurie, cavalier) : **aucune source**. Tous les niveaux du §2.2 et du §9 sont des HYPOTHÈSES.
6. **Effectifs S1, S2, S3.** Ce sont des HYPOTHÈSES. Il n'y a qu'un seul point de référence pour les jardins (Villandry, 1,4 ETP/ha, un extrême). Le ratio de 10 chevaux par ETP est extrapolé de deux cas, à 10 et 18 équidés par ETP.
7. **Coûts des chevaux.** Les prix IFCE datent de 2011-2012 et n'ont pas été actualisés (maréchal, vétérinaire, assurance). Le budget alimentation et litière de 1 500 € est une HYPOTHÈSE. Le prix 2026 du foin livré, des copeaux et des granulés est INCONNU.
8. **Installations équestres.** Les prix viennent d'un site commercial (HelloPro) sans mention HT ou TTC. Le manège de 60 × 25 m (220 000 à 305 000 €) est extrapolé. Le référentiel de la chambre de Normandie n'a pas été lu (site en maintenance).
9. **Foin, paille et fumier.** Les prix sont des EXTRAITS de moteur de recherche : les PDF des chambres renvoient 404 ou sont en maintenance. Ils sont régionaux et départ ferme.
10. **Fermages.** Seul l'arrêté de l'Aveyron a été lu. Il n'est pas représentatif des régions de châteaux (Val de Loire, Normandie, Île-de-France).
11. **Données INCONNUES**, à rechercher en vague 2 :
    - électricité d'une écurie ;
    - coûts de gestion forestière (à rapprocher de R8) ;
    - clôtures de prestige (€/ml, durée de vie) ;
    - tondeuses autoportées et utilitaires ;
    - tarifs de sous-traitance (tonte, haies, élagage) ;
    - coûts Plante & Cité en €/m² ;
    - nombre de jardiniers à Vaux-le-Vicomte, Chantilly, Versailles, Courances et au National Trust.
12. **Disponibilité des sources.** Le 14/10/2026, plusieurs sites publics étaient indisponibles : urssaf.fr (réponse vide), travail-emploi.gouv.fr (503), agriculture.gouv.fr (503), réseau des chambres d'agriculture (« en maintenance »). Il faudra réessayer en vague 2.

## 12. Chiffres clés pour le modèle

| # | Donnée | Valeur | Unité | Année | Statut | Source |
|---|---|---|---|---|---|---|
| 1 | SMIC horaire brut en vigueur | 12,31 | €/h | depuis le 01/06/2026 | PAGE LUE | [R2-01], [R2-02] |
| 2 | SMIC mensuel brut en vigueur (35 h) | 1 867,02 | €/mois | 2026 | PAGE LUE | [R2-01] |
| 3 | SMIC au 1er janvier 2026 | 12,02 / 1 823,03 | €/h / €/mois | 2026 | PAGE LUE | [R2-02], [R2-04] |
| 4 | RGDU : coefficient maximal (< 50 salariés), sortie | 0,3981 ; nulle à 3 SMIC (2,9293 SMIC depuis juin) | — | 2026 | PAGE LUE | [R2-02] |
| 5 | Coût employeur à 1 SMIC | 23 853 (ratio 1,065) | €/an | 2026 | ESTIMATION (simulateur officiel) | [R2-11] |
| 6 | Coût employeur à 1,5 SMIC | 44 118 (ratio 1,313) | €/an | 2026 | ESTIMATION (simulateur officiel) | [R2-11] |
| 7 | Coût employeur à 2,5 SMIC | 78 982 (ratio 1,410) | €/an | 2026 | ESTIMATION (simulateur officiel) | [R2-11] |
| 8 | Paysage : O.1 / O.6 / TAM.4 / cadre C5 | 12,12 €/h / 13,56 €/h / 2 756 €/mois / 48 510 €/an | brut | 2026 | PAGE LUE | [R2-07] |
| 9 | Activités hippiques : soigneur (coeff. 103) / responsable d'écurie (121) / enseignant (150) | 12,10 / 12,73 / 15,87 | €/h brut | 01/02/2026 | PAGE LUE (secondaire) | [R2-05] |
| 10 | Production agricole : paliers 1 à 12 | 12,02 à 24,16 | €/h brut | 01/05/2026 | PAGE LUE | [R2-09] |
| 11 | Particulier employeur : niveaux I à XII | 12,61 à 18,07 | €/h brut | avenant du 05/02/2026 | PAGE LUE (secondaire) | [R2-03] |
| 12 | Déduction forfaitaire particulier employeur | 2 | €/heure travaillée | 2026 | PAGE LUE | [R2-12] |
| 13 | Crédit d'impôt emploi à domicile | 50 % de 12 000 € max. (jardinage 5 000 €) | €/an | 2026 | PAGE LUE | [R2-13] |
| 14 | Jardins de Villandry : jardiniers / surface | 10 / 7 (≈ 1,4 ETP/ha, plafond) | ETP / ha | 2024 | PAGE LUE | [R2-15] |
| 15 | Indice national des fermages 2025 | 123,06 (+0,42 %) | indice | 2025-2026 | PAGE LUE | [R2-20] |
| 16 | Fermage des pâtures (Aveyron, min. – max.) | 52,26 à 170,85 | €/ha/an | 2025-2026 | PAGE LUE | [R2-20] |
| 17 | Foin de prairie naturelle départ ferme (Yonne) | 102 à 107 | €/t brute | 2024 | EXTRAIT | [R2-21] |
| 18 | Paille (valeur de calcul, Nouvelle-Aquitaine) | 70 | €/t | 2024 | EXTRAIT | [R2-22] |
| 19 | Tracteur 100-140 CV, prix récent | 101 464 (HT) ; 10,7 ans d'amortissement | € | 2026 | PAGE LUE | [R2-30] |
| 20 | Chaîne de fenaison neuve (faucheuse + faneuse + andaineur + presse) | ≈ 103 000 (HT) | € | 2026 | ESTIMATION | [R2-30] |
| 21 | Renouvellement annuel du matériel S1 / S2 / S3 | ≈ 14 000 / 45 000 / 58 000 et plus (HT) | €/an | 2026 | ESTIMATION sur HYPOTHÈSES de parc | §4.2 |
| 22 | Ration réelle d'un cheval (écurie de pension) | 2,7 t de foin + 0,9 t d'orge + 0,8 t de paille ; 760 à 1 090 €/an | par cheval et par an | 2008 | PAGE LUE | [R2-24] |
| 23 | Cheval de compétition amateur en pension box : coût total propriétaire | 6 100 à 14 600 (dont pension 3 000 à 8 400) | €/an (payé par un particulier, vraisemblablement TTC) | 2011-2012 | PAGE LUE | [R2-18] |
| 24 | Maréchalerie / soins de base / assurance mortalité et frais vétérinaires | 525 à 1 040 / 270 à 500 / 450 à 750 | €/an | 2012 | PAGE LUE | [R2-18] |
| 25 | Fumier d'un cheval au box | 12,8 (5 à 14) | t/an | après 2023 | PAGE LUE | [R2-32] |
| 26 | Eau bue par un cheval | 15 à 60 (40 en moyenne au pré) | L/jour | après 2023 / 2012 | PAGE LUE | [R2-32], [R2-17] |
| 27 | Fumière | 2 (2 mois) à 4,6 (6 mois) | m²/cheval | 2018 (DEXEL) | PAGE LUE | [R2-32], [R2-31] |
| 28 | Manège couvert 20 × 40 m clé en main | 40 000 à 100 000 (moyenne ≈ 85 000) | € (HT/TTC non précisé) | 2026 | PAGE LUE (site commercial) | [R2-27] |
| 29 | Box 3 × 4 m | 2 200 à 8 500 | €/box | 2026 | PAGE LUE (site commercial) | [R2-28] |
| 30 | Masse salariale S1 / S2 / S3 | ≈ 77 000 (2,7 ETP) / 489 000 (13 ETP) / 1 081 000 (29 ETP) | €/an | 2026 | ESTIMATION sur HYPOTHÈSES | §9 |
| 31 | Coût complet d'un box occupé (soins, alimentation, maréchal, vétérinaire, installations) | ≈ 5 500 à 8 500 (hors assurance et valorisation) | €/an | 2026 | ESTIMATION | §9.5 |
| 32 | Ratio de soins | 10 (cas observés : 10 à 18) | chevaux par ETP | — | HYPOTHÈSE | [R2-24], [R2-25] |

---

## Journal d'utilisation web (agent R2)

- **WebSearch** : 15 sur 15 autorisées.
- **WebFetch** : 55 appels. 33 ont renvoyé un contenu, dont une dizaine sans donnée utile ; 22 ont échoué (403, 404, 503, redirection, taille, protection anti-robot). 14 PDF enregistrés par WebFetch ont été lus localement avec pdftotext ou en image, dont 2 sans rapport avec le sujet.
- **Autres requêtes réseau (curl)** :
  - 35 requêtes POST à l'API publique de calcul du simulateur URSSAF mon-entreprise.urssaf.fr, sans compte ni donnée personnelle ;
  - 5 requêtes de diagnostic : statut d'urssaf.fr et de mon-entreprise, téléchargement Plante & Cité (403), téléchargement chambre de Normandie (en maintenance), état du proxy.
- Aucun contact, formulaire, achat ni commande git.


## Errata après vérification indépendante (V2V, 2026-10-14)

Ajouté par le directeur de mission. Le texte ci-dessus n'est pas modifié ; ces précisions s'appliquent à sa lecture.

- Allègement général (§ 1.2 et chiffres clés) : 0,3981 est le coefficient **maximal** (moins de 50 salariés, salaire égal au SMIC de janvier 2026). Au SMIC de juin 2026, le coefficient effectif est d'environ 0,375, car la formule garde le SMIC de janvier [V2V-14] [V2V-15]. Les trois coûts employeur du simulateur URSSAF (23 853, 44 118 et 78 982 €/an) sont confirmés au centime [V2V].
- Jardiniers de S3 : V2C a montré, à partir des temps d'entretien de la Ville de Rennes, que 11 jardiniers ne suffisent pas pour 60 ha (au moins 15,7 ETP en gestion différenciée). Le modèle retient désormais 16 jardiniers [V2C-21].
