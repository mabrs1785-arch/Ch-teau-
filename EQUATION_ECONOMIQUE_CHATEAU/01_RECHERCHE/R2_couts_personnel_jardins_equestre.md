# R2 — Personnel, jardins, terres, équipements, chevaux

Agent : R2. Démarré le 2026-10-14. Fichier écrit au fur et à mesure.
Sources : `01_RECHERCHE/sources/sources_R2.csv` (identifiants [R2-xx]).

Statuts : PAGE LUE (page ouverte, citation exacte) / EXTRAIT (vu dans un résultat de recherche) / ESTIMATION (calcul explicite) / HYPOTHÈSE (choix de modélisation) / INCONNU (non trouvé, méthode de vérification indiquée).

---

## 1. Coût du travail 2025-2026

### 1.1 SMIC

| Donnée | Valeur | Statut | Source |
|---|---|---|---|
| SMIC brut mensuel au 1er janvier 2026 (35 h) | 1 823,03 €/mois | PAGE LUE | [R2-02] « Au 1er janvier 2026, le Smic brut mensuel (base 35 heures par semaine) est fixé à 1 823,03 € » |
| SMIC brut annuel au 1er janvier 2026 | 21 876,40 €/an | PAGE LUE | [R2-02] « payé au Smic, soit 1 823,03 € par mois et 21 876,40 € sur l'année » |
| SMIC horaire brut au 1er janvier 2026 | ≈ 12,02 €/h | ESTIMATION | 1 823,03 / 151,67 h = 12,02 €. Valeur horaire non lue sur une page officielle. |
| SMIC horaire brut en vigueur (page vérifiée le 01/06/2026) | 12,31 €/h | PAGE LUE | [R2-01] tableau « Montants du Smic » : horaire « 12,31 € » brut, « 9,74 € » net |
| SMIC mensuel brut en vigueur | 1 867,02 €/mois | PAGE LUE | [R2-01] « 1 867,02 € » brut ; net indicatif « 1 477,93 € » |
| SMIC annuel brut en vigueur | 22 404,20 €/an | PAGE LUE | [R2-01] annuel « 22 404,20 € brut, 17 735,19 € net » |
| Date d'effet du SMIC à 12,31 € | 1er juin 2026 | PAGE LUE (indirecte) | [R2-02] « une mesure de tolérance permet d'appliquer la revalorisation du Smic au 1er juin 2026 dans la formule de calcul » ; [R2-01] référence « Arrêté du 22 mai 2026 relatif au relèvement du salaire minimum de croissance ». Hausse de 12,02 à 12,31 € = +2,4 % (ESTIMATION). |
| Mécanisme de revalorisation | 1er janvier + revalorisation automatique si l'inflation dépasse 2 % | PAGE LUE | [R2-01] « Le Smic est revalorisé chaque année au 1er janvier » ; hausse automatique si l'inflation augmente d'au moins 2 % (reformulation du WebFetch). |

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
| 2,5 SMIC | 4 667,55 € | 1 914,24 € | 117,16 € | **6 581,79 €** | 1,410 | **78 981 €** | 3 674,23 € |

Lectures (ESTIMATION) :
- **Avant réduction**, les cotisations patronales représentent environ 44 % du brut : (120,74 + 700,13) / 1 867,02 = 44,0 % ; (1 914,24 + 117,16) / 4 667,55 = 43,5 %.
- **Effet de la RGDU** : elle ramène le surcoût à environ 6,5 % au SMIC, 31 % à 1,5 SMIC et 41 % à 2,5 SMIC. Une masse salariale proche du SMIC coûte donc beaucoup moins cher que des postes qualifiés.
- **Coût par heure réellement travaillée** : au SMIC, 23 853 € / 1 607 h ≈ **14,8 €/h**. HYPOTHÈSE : 1 607 h travaillées par an, soit la durée annuelle de référence de 35 h. Ce coût sert de base de comparaison avec les tarifs de sous-traitance.
- **Salariés agricoles et équestres (MSA)** : la RGDU s'applique aussi ([R2-02] mentionne TO-DE pour l'agriculture). Les taux AT/MP agricoles diffèrent. Les chiffres ci-dessus sont une approximation : à vérifier avec le simulateur MSA ou un expert-comptable.
- **Particulier employeur (CESU)** : la RGDU ne s'applique pas. Le régime est différent (déduction forfaitaire par heure, crédit d'impôt). Voir §1.5.
- **Non compris** : 13e mois et primes, astreintes de week-end des soigneurs, logement de fonction (avantage en nature), vêtements de travail, médecine du travail, formation au-delà des contributions légales, intérim et remplacements.

### 1.5 Cas du particulier employeur (personnel de maison payé par le propriétaire à titre privé)

- **Déduction forfaitaire** [R2-12, PAGE LUE, vérifiée le 01/06/2026] : « bénéficiez d'une déduction forfaitaire de cotisations patronales de Sécurité sociale de 2 € si vous employez un salarié à votre domicile ». Elle s'applique par heure travaillée, hors heures de congés payés. Elle ne se cumule pas avec les exonérations partielles.
- **Crédit d'impôt** [R2-13, PAGE LUE, vérifiée le 15/04/2026] :
  - 50 % des dépenses, retenues dans la limite de « 12 000 € par an », soit 6 000 € d'avantage au plus ;
  - plafond majoré de 1 500 € dans certains cas, sans dépasser 15 000 € ;
  - petits travaux de jardinage plafonnés à 5 000 € par foyer, à l'intérieur du plafond général.
- **Conséquence (ESTIMATION)** : pour un domaine qui emploie de 2 à 30 personnes, le crédit d'impôt est marginal, au plus 6 000 € à 7 500 € par an. Il ne change pas l'équation. La déduction de 2 €/h représente environ 3 200 €/an pour un temps plein de 1 607 h, contre environ 8 400 €/an de RGDU au SMIC en entreprise (700,13 € × 12). Mais le salarié du particulier employeur relève d'une base conventionnelle de 40 h (§1.4 a). Comparaison fine : INCONNU, à faire avec le simulateur CESU de l'URSSAF ou un expert-comptable.
- **Limite juridique (HYPOTHÈSE à faire valider par R3)** : le statut de particulier employeur suppose un travail au domicile privé du particulier. Le personnel affecté aux activités commerciales (écurie de pension, événements) doit être salarié de la société d'exploitation.

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


## 2. Salaires de marché et tension du recrutement

### 2.1 Équitation : tension du recrutement (pas de salaires publiés)

Source [R2-14], rapport d'activité équi-ressources 2022 de l'IFCE, PAGE LUE (texte extrait du PDF) :
- 3 719 offres d'emploi diffusées en 2022.
- Depuis 2015, « 32 738 offres diffusées », dont « 23 167 offres ont abouties à un recrutement ».
- Secteur sport et loisir : « 2 288 offres d'emploi » ; pourvues via équi-ressources 712, pourvues autrement 779, annulées 757. Environ un tiers des offres sont donc annulées (ESTIMATION : 757 / 2 248).
- « Palefrenier soigneur / Garçon de cour & Enseignant d'équitation représentent 46% des offres d'emploi diffusées en 2022 ».

Le rapport ne donne **aucun salaire proposé**. Les salaires de marché des soigneurs, cavaliers et responsables d'écurie restent INCONNUS par cette voie. Pour vérifier : statistiques d'offres d'équi-ressources (equiressources.fr) ou études de l'Observatoire économique et social du cheval (IFCE).

