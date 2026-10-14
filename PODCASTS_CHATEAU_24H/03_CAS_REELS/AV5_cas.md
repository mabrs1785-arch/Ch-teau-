# AV5 — Cas réels : modèles premium (hospitality, événementiel, domaines, clubs)

Date : 2026-10-14. Les identifiants de sources (S-xx) renvoient à `_brut/sources_AV5.csv`. Les contenus audiovisuels (AV5-xxx) renvoient à `_brut/catalogue_AV5.csv`.

## Méthode et conventions

**Origine des comptes.**
- **France** : jeu de données officiel `ratios_inpi_bce` (comptes déposés à l'INPI), lu via data.economie.gouv.fr. L'identification des sociétés vient de l'API recherche-entreprises.api.gouv.fr.
- **Royaume-Uni** : PDF officiels de Companies House, lus par reconnaissance de caractères (OCR).
- **États-Unis** : rapports déposés à la SEC (10-K, 8-K).

**Abréviations.** CA = chiffre d'affaires. EBE = excédent brut d'exploitation. RN = résultat net. « Conso. » = comptes consolidés du groupe.

**Règles de lecture.**
- « NC » = compte de résultat confidentiel : CA et EBE affichés à 0 dans le jeu INPI, alors que le RN reste visible.
- **[VÉRIFIÉ]** = chiffre lu dans un registre officiel.
- **[REPÉRÉ]** = extrait de résultat de recherche, page non ouverte.
- **[DÉDUCTION]** = raisonnement de l'agent, à confirmer.

---

## Tableau de synthèse : l'EBE n'est pas la rentabilité

| Cas | Type | CA récent | EBE | Résultat net | Statut |
|---|---|---|---|---|---|
| C01 Fontenille (conso.) | 15 hôtels de charme | 33,8 M€ (2024) | +0,7 M€ | **−2,9 M€** | [VÉRIFIÉ] |
| C01 Primard (hôtel) | domaine de plus de 20 ha | 6,7 M€ (2025) | +0,6 M€ | **−1,7 M€** | [VÉRIFIÉ] |
| C04 Le Barn (exploitant et propriétaire des murs) | 73 chambres dans un haras | 6,0 M€ + 1,1 M€ de loyers internes | ≈ 0,9 M€ cumulé | **≈ −0,5 M€** | [VÉRIFIÉ] et [DÉDUCTION] |
| C05 LOV & Ducasse (probablement Le Grand Contrôle) | hôtel de 14 chambres en concession | 16,3 M€ (2024) | −0,6 M€ | **−3,3 M€** | [VÉRIFIÉ], lien avec l'hôtel probable |
| C07 Soho House & Co | 45 clubs | 1 204 M$ (2024) | EBITDA ajusté 131,9 M$ | **−163 M$** | [VÉRIFIÉ] |
| C08 Estelle Manor | 108 chambres et club | 44,4 M£ (2025) | perte d'exploitation de −7,6 M£ | **−23,5 M£** | [VÉRIFIÉ] |
| C09 Domaine des Étangs | château-hôtel et environ 1 000 ha | 3,5 M€ (2025) | −2,8 M€ | **−3,2 M€** | [VÉRIFIÉ] |
| C10 Château La Coste (conso.) | vin, art, hôtel | 36,6 M€ (2024) | **+10,9 M€** | **−8,9 M€** | [VÉRIFIÉ] |
| C11 Domaine Les Crayères | hôtel de 20 chambres et gastronomie | 17,8 M€ (2024) | +2,1 M€ | **+1,3 M€** | [VÉRIFIÉ] |
| C12 Château de la Treyne | hôtel-château familial | 2,7 M€ (2022) | +0,7 M€ | **+0,15 M€** (≈ 0 sur 9 ans) | [VÉRIFIÉ] |
| C13 Château la Beaumetane | lieu de mariage | 0,20 M€ (2019) | +0,05 M€ | **+0,02 M€** | [VÉRIFIÉ] |
| C14 Fermes de Gally (conso.) | agritourisme périurbain | 53,4 M€ (2017) | +1,9 M€ | **+1,2 M€** | [VÉRIFIÉ] |

**Lecture.**
- **Neuf cas sur douze perdent de l'argent au niveau net.** Les pertes ont deux causes : les amortissements des travaux et la dette d'acquisition.
- Les cas positifs ont trois profils : des murs **anciens et amortis** (la Treyne, famille propriétaire depuis les années 1980) ; une **table d'exception** (Les Crayères) ; une **activité de volume sans gros investissement de prestige** (Gally).
- Pour un apport limité, la conséquence est directe : **le modèle doit fonctionner après loyer ou remboursement de la dette, et pas seulement au niveau de l'EBE**.

---

## C01 — Les Domaines de Fontenille (Frédéric Biousse et Guillaume Foucher)

**Parcours**
- Achat du domaine de Lauris en 2014. Les fondateurs cherchaient d'abord une maison pour eux ; l'hôtel devient le moyen de financer la rénovation.
- 16 mois de travaux, ouverture en février 2016 avec 17 chambres (interview du *Journal des Palaces*, S-03).
- Puis Marseille, Minorque, Hossegor, Primard (2021), l'île d'Yeu (2022), Oppède, la Toscane, etc.
- 11 maisons en décembre 2024, 15 ensuite (*Forbes*, S-04).

**Financement**
1. Fondateur actionnaire principal.
2. Entrée de familles investisseuses.
3. Florac participe à une restructuration et à un tour de table en décembre 2017 [REPÉRÉ, S-07].
4. **Caisse des Dépôts au capital** (novembre 2023) et **co-acquisitions immobilières** en France (*Forbes*, TourMaG ; S-04, S-05).
5. **LVMH, participation minoritaire** en décembre 2024, aux côtés d'Anaïs Ventures. LVMH devient l'actionnaire principal (TourMaG, S-05). Environ 20 % selon Bloomberg [REPÉRÉ, S-06].

**Comptes [VÉRIFIÉ INPI]** (S-08 à S-12)

| Entité | Année | CA | EBE | RN |
|---|---|---|---|---|
| Groupe (conso., 798361184) | 2023 | 31,67 M€ | −2,43 M€ | **−6,78 M€** |
| Groupe (conso., 798361184) | 2024 | 33,78 M€ | +0,70 M€ | **−2,89 M€** |
| Hôtel de Fontenille SAS, Lauris (831667092) | 2018 | 3,11 M€ | +0,39 M€ | −0,54 M€ |
| Hôtel de Fontenille SAS, Lauris (831667092) | 2021 | 2,96 M€ | +0,53 M€ | −0,52 M€ |
| Hôtel de Fontenille SAS, Lauris (831667092) | 2023 | 4,03 M€ | +0,67 M€ | −0,45 M€ |
| Hôtel de Fontenille SAS, Lauris (831667092) | 2025 | 4,45 M€ | +0,66 M€ | **−0,30 M€** |
| Primard SAS (842019317) | 2021 | 3,26 M€ | −0,62 M€ | −2,03 M€ |
| Primard SAS (842019317) | 2022 | 6,10 M€ | +0,07 M€ | −2,32 M€ |
| Primard SAS (842019317) | 2023 | 6,79 M€ | +0,14 M€ | −2,51 M€ |
| Primard SAS (842019317) | 2024 | 6,32 M€ | −0,02 M€ | −2,83 M€ |
| Primard SAS (842019317) | 2025 | 6,67 M€ | +0,57 M€ | **−1,69 M€** |
| SAS Fontenille Oppède (905274411) | 2024 | 0,92 M€ | +0,03 M€ | −0,95 M€ |
| SAS Fontenille Oppède (905274411) | 2025 | 1,28 M€ | +0,22 M€ | −0,70 M€ |

- La société de Lauris affiche un **RN négatif chaque année de 2017 à 2025**, alors que l'EBE est positif depuis 2020.
- Primard SAS a été créée en 2018 et réalise son premier CA en 2021. Cela confirme une ouverture en 2021 et non en 2019, comme l'affirment certaines fiches de voyagistes.
- La perte nette cumulée de Primard sur 2021-2025 atteint environ **11,4 M€** (somme des RN ci-dessus, calcul de l'agent).
- **Écart à signaler** : TourMaG annonçait un CA 2024 d'« environ 40 M€ », contre 33,8 M€ dans les comptes consolidés déposés.

**Leçons**
1. L'achat des murs et les travaux pèsent sur le résultat net pendant de nombreuses années, même avec une forte fidélité (55 % du CA réalisé par des clients revenus, affirmation des fondateurs).
2. **La croissance a été rendue possible par des capitaux successifs** : familles, Caisse des Dépôts, LVMH. Les profits n'y ont pas suffi.
3. Le groupe évolue vers les murs loués et les contrats de gestion. **C'est l'angle d'entrée possible pour un entrepreneur sans gros apport** : être exploitant ou apporter un lieu à un exploitant.

---

## C02 — Les Sources de Caudalie et la Collection des Hôtels du Vignoble (Jérôme et Alice Tourbier)

**Parcours**
- Ouverture en 1999, dans les vignes du Château Smith Haut Lafitte, propriété de la famille Cathiard.
- Selon les notes du *Déclic*, les études de marché prédisaient environ 30 % de remplissage et un échec.
- Label Palace ensuite, puis Cheverny (2020), Vougeot et l'Alsace (prévue en 2028).
- **Rachat des Grandes Étapes Françaises en 2023.**

**Registres [VÉRIFIÉ]**
- Les Sources de Caudalie (480358332) et Les Sources de Cheverny (450591573) : aucun ratio publié (comptes non accessibles dans le jeu de données).
- Les deux sociétés sont présidées par La Collection des Hôtels du Vignoble (920548211), elle-même présidée par SOURCEHOTELS.
- Grandes Étapes Françaises (917320319, exercices clos en avril, S-44) :

| Exercice | CA | RN |
|---|---|---|
| 2017 | 16,8 M€ | −1,4 M€ |
| 2018 | 16,3 M€ | +2,1 M€ |
| 2019 | 16,8 M€ | −0,4 M€ |
| 2020 | 15,7 M€ | +0,7 M€ |
| 2021 | 5,8 M€ | −0,7 M€ |
| 2022 | 12,5 M€ | −1,7 M€ |

**Leçon.** La singularité (vin, spa, gastronomie) peut contredire les études de marché. Mais la croissance passe ensuite par des rachats que seule une famille déjà capitalisée peut financer.

---

## C03 — Polo Club du Domaine de Chantilly (Patrick Guerrand-Hermès, Benoit Perrier)

**Montage.** Le Domaine de Chantilly appartient à l'Institut de France, qui l'a reçu en legs du duc d'Aumale. Le club **loue une partie de ces terres** (transcription, S-01, 1:12:58).
- Club fondé en 1995, première saison sur herbe en 1996 (S-01, 0:15:35).
- Bail de 50 ans accordé en 1995 sur la Ferme d'Apremont, d'environ 200 ha [REPÉRÉ, S-29].
- Le club a été fondé par P. Guerrand-Hermès et des amis, dont André Fabre. Ils deviennent membres, et certains actionnaires.

**Économie, selon le directeur (affirmations non vérifiées)**
- **50 % des recettes viennent de la pension des chevaux.**
- **25 % viennent des droits d'engagement aux tournois.**
- **25 % viennent des cotisations, des événements, de la restauration et de l'école de polo.**

Capacités : 400 boxes plus des boxes temporaires, environ 1 400 chevaux en septembre, environ 50 tournois et 500 matchs par an. L'entrée est gratuite pour le public et des formules VIP sont vendues pour les finales. Les sponsors, comme Barnes et Richard Mille [site du partenaire, S-30], sont décrits comme exigeants sur le retour sur investissement.

**Comptes.** Structure exploitante non identifiée au registre (sous « polo club chantilly » et « polo Apremont »). **Pas de chiffres financiers vérifiés.**

**Leçons**
- Le cheval rapporte surtout par **l'occupation des boxes**, pas par le spectacle.
- Le foncier peut être loué à long terme à un grand propriétaire institutionnel.
- Les nouvelles installations, comme l'arena, sont financées en faisant entrer de nouveaux membres et investisseurs.

---

## C04 — Le Barn, hôtel du Haras de la Cense (William Kriegel, Édouard Daehn)

**Lieu.** Hôtel de 73 chambres, ouvert en mai 2018 sur le domaine équestre de La Cense (Bonnelles, forêt de Rambouillet), consacré à l'équitation éthologique. *The Week* parle d'« un domaine de 500 acres » (S-15). Concepteurs : W. Kriegel, industriel propriétaire du haras, et É. Daehn, hôtelier. Exploitation confiée en 2020 à Marugal [REPÉRÉ, S-16]. Financement de développement conseillé par Shift Capital [REPÉRÉ, S-17].

**Structure [VÉRIFIÉ, registre]**
- BARN HOLDING (822248274), présidée par W. Kriegel, préside deux sociétés :
  - **HAMEAU DE LA CENSE** (799342704), qui détient les murs (code d'activité 68.20B, location immobilière) ;
  - **BARN BONNELLES** (915113211), créée en 2022, qui exploite l'hôtel (code 55.10Z).

**Comptes [VÉRIFIÉ INPI, S-13 et S-14]**

| Société | Année | CA | EBE | RN |
|---|---|---|---|---|
| Hameau de la Cense | 2019 | 4,78 M€ | +0,62 M€ | −0,46 M€ |
| Hameau de la Cense | 2021 | 3,79 M€ | +1,42 M€ | +0,36 M€ |
| Hameau de la Cense | 2023 | 1,18 M€ | +1,08 M€ | **−4,06 M€** |
| Hameau de la Cense | 2025 | 1,08 M€ | +0,94 M€ | −0,15 M€ |
| Barn Bonnelles | 2023 | 6,47 M€ | +0,03 M€ | −0,63 M€ |
| Barn Bonnelles | 2024 | 5,88 M€ | ≈ 0 | −0,14 M€ |
| Barn Bonnelles | 2025 | 6,00 M€ | −0,08 M€ | −0,33 M€ |

- [DÉDUCTION] Depuis 2022-2023, la société des murs encaisse environ 1,08 M€ par an avec une marge d'EBE d'environ 90 %. Ce profil correspond à un **loyer versé par l'exploitant**. La perte de 4,06 M€ en 2023 est probablement exceptionnelle (dépréciation ou restructuration, non vérifié).
- Ensemble : environ 6 M€ de CA hôtelier, un EBE cumulé d'environ 0,9 M€ et un RN cumulé d'environ −0,5 M€ en 2025.

**Leçon.** **C'est le cas le plus proche du projet : un domaine équestre qui adosse un hôtel à son haras, près de Paris.** Le montage propriétaire des murs et société d'exploitation permet de faire entrer un exploitant ou de céder une partie séparément. Mais même avec 73 chambres à 45 minutes de Paris, l'ensemble est **à l'équilibre au mieux**. Mission 1 avait déjà relevé les pertes passées du Haras de la Cense lui-même.

---

## C05 — Airelles, Le Grand Contrôle (Château de Versailles)

**Montage [lu, batiweb 17-08-2015, S-18]**
- Appel d'offres de l'établissement public du château de Versailles pour transformer en hôtel trois bâtiments vides depuis 2008, soit **2 800 m²**.
- Investissement estimé à 4 à 7 M€ pour la toiture et les murs, plus 4 M€ d'aménagement intérieur.
- **Concession accordée pour 60 ans.**
- Une première concession de 30 ans, accordée à Ivy International, avait été abandonnée.

**Exploitation**
- Ouverture en 2021, 14 chambres et suites, restaurant d'Alain Ducasse, spa Valmont.
- Chambres Deluxe à partir de 2 885 $ la nuit, suite Necker à environ 16 000 $ (Afar, mise à jour du 2024-04-25, S-19).

**Comptes [VÉRIFIÉ INPI, S-20].** La société **LOV & DUCASSE** (820433456) a été créée le 2016-05-13 et elle est présidée par LOV Hotel Collection. **Son lien avec Le Grand Contrôle est probable mais non vérifié** : date de création juste après l'attribution, et associés Airelles/LOV et Ducasse.

| Année | CA | EBE | RN |
|---|---|---|---|
| 2022 | 13,7 M€ | −0,67 M€ | −2,96 M€ |
| 2023 | 15,1 M€ | −0,83 M€ | −3,39 M€ |
| 2024 | 16,3 M€ | −0,64 M€ | **−3,29 M€** |

**Leçon.** **Un monument public peut être exploité sans être acheté**, par une concession de longue durée. Mais le preneur porte les travaux, et le prestige ne garantit pas le résultat. C'est un modèle d'accès sans achat du foncier à rechercher à l'échelle régionale (communes, départements, fondations ; voir I02).

---

## C06 — Hôtel du Couvent, Nice (Valéry Grégo, groupe Perseus)

- Projet initié en 2013 par le maire de Nice pour transformer un couvent du XVIIe siècle (*Journal des Palaces*, S-21).
- Grégo **vend ses autres hôtels** (Le Pigalle, L'Alpaga) pour le financer (*10 Magazine*, S-22).
- Dix ans de chantier ; ouverture en 2024 dans la *Luxury Collection* de Marriott. L'hôtel compte 88 chambres d'après le *Journal des Palaces*, ou 70 chambres et 18 suites d'après *10 Magazine*.
- Approvisionnement par la ferme de Touët-sur-Var.
- Coût d'environ 93 à 100 M€ [REPÉRÉ, chiffres divergents, S-23].
- Chapitres du podcast : financement d'un hôtel (18:38), vente des autres hôtels (56:50), partenariat Marriott (1:33:22) ; voir la fiche F04.

**Leçon.** Un patrimoine public dormant peut être confié à un entrepreneur, à condition d'une très forte capacité d'investissement. Le partenariat avec un grand groupe (Marriott) apporte la distribution.

---

## C07 — Soho Farmhouse et Soho House & Co

**Soho Farmhouse [VÉRIFIÉ SEC, 10-K 2024, S-24]**
- Lieu loué (et non possédé), ouvert en juin 2015, **114 chambres**.
- Ancien directeur, M. Ward (S-02) : environ 110 à 115 acres (environ 45 ha) ; on est passé de 44 clés à plus de 100 ; « la marge est faible car la masse salariale est énorme ».

**Groupe [VÉRIFIÉ SEC, S-24 à S-26]**

| Indicateur | Exercice 2024 |
|---|---|
| Recettes totales | 1 203,8 M$ |
| dont cotisations | 418,0 M$ (35 %) |
| dont services dans les maisons | 481,6 M$ |
| dont autres | 304,2 M$ |
| Perte nette attribuable | **−163,0 M$** (−130,5 M$ en 2023) |
| EBITDA ajusté | 131,9 M$ |
| Membres | environ 271 500, dont 212 400 membres Soho House |
| Liste d'attente | plus de 112 000 |
| Cotisation « Every House » | environ 5 200 $ par an |
| Cotisation « Friends » | environ 130 $ par an (53 110 membres) |

- Accord de fusion signé le 2025-08-15 avec une filiale de Yucaipa (8-K).
- À la clôture (8-K de janvier 2026) : 220 M$ d'obligations de la holding, à 12,5 % d'intérêts capitalisés les trois premières années.

**Leçon.** Les cotisations apportent du revenu récurrent et payé d'avance. Mais un réseau mondial de clubs, même apprécié, reste déficitaire au niveau net.

---

## C08 — Estelle Manor (Oxfordshire)

**Comptes [VÉRIFIÉ, Companies House 11258257, exercice clos le 2025-03-31, comptes audités, S-27]**
- 108 chambres, 85 acres, ouverture en mai 2023.

| Indicateur | Exercice 2025 | Exercice 2024 |
|---|---|---|
| CA | **44,4 M£** | 15,3 M£ |
| Perte d'exploitation | −7,6 M£ | −22,1 M£ |
| Charges d'intérêts | 14,5 M£ | — |
| **Perte nette** | **−23,5 M£** | −33,7 M£ |

- Immobilisations corporelles de 155 M£ ; dettes à moins d'un an de 230 M£ ; capitaux propres de −65 M£.
- Financement par prêts d'actionnaires. Contrôle déclaré par Norlake Hospitality Ltd ; la direction a mené une « restructuration complète » pour réduire les coûts.

**Leçon.** Le modèle « château et club » au sommet du marché exige plus de 150 M£ et des années de pertes. Pour un apport limité, il faut retenir l'idée du club, pas l'échelle.

---

## C09 — Domaine des Étangs (Massignac, Charente)

**Propriété.** Le domaine est mis en avant par la chaîne YouTube « Collection Garance Primat » et par une vidéo Art Basel consacrée à la collectionneuse Garance Primat [REPÉRÉ, AV5-048 et 049].

**Comptes [VÉRIFIÉ INPI, S-38]**

| Société | Période | CA | EBE | RN |
|---|---|---|---|---|
| Domaine des Étangs, hôtel (814032967) | 2016 | 1,1 M€ | — | −4,8 M€ |
| Domaine des Étangs, hôtel | 2016-2025 | de 1,1 à 3,5 M€ | **de −2,1 à −4,2 M€ chaque année** | de −2,5 à −5,0 M€ chaque année |
| Domaine des Étangs, hôtel | 2025 | 3,5 M€ | — | −3,2 M€ |
| Domaine des Étoiles, société agricole (572046852) | 2016-2024 | environ 1,8 à 2,0 M€ par an | — | **de −4,3 à −8,4 M€ par an** |

**Leçon.** Un domaine d'exception porté par un mécène peut perdre **plus de 7 M€ par an pendant dix ans**, en additionnant l'hôtel et la société agricole. C'est un contre-modèle pour l'autofinancement.

---

## C10 — Château La Coste (Paddy McKillen)

**Comptes consolidés 2024 [VÉRIFIÉ INPI, Château La Coste Participation, 444389183, S-39]**
- CA de **36,6 M€**, EBE de **10,9 M€ (30 %)**, **RN de −8,9 M€**.
- Une nouvelle société, Auberge La Coste (922472998), a été créée en 2022 ; RN de −0,74 M€ en 2025.

**Leçon.** Un excellent EBE (vin, art, hôtel) peut être absorbé par les amortissements et les frais financiers d'un investissement massif.

---

## C11 — Domaine Les Crayères (Reims), copropriété de Laurent Gardinier, président de Relais & Châteaux

**Comptes [VÉRIFIÉ INPI, 908581903, S-42]**

| Année | CA | EBE | RN |
|---|---|---|---|
| 2022 | 16,1 M€ | +3,8 M€ | +2,8 M€ |
| 2023 | 18,0 M€ | +3,2 M€ | +3,6 M€ |
| 2024 | 17,8 M€ | +2,1 M€ | **+1,3 M€** |

20 chambres selon les notes d'*On The Pass*.

**Leçon.** Rentabilité possible si la table et la destination (la Champagne) portent un prix moyen élevé. Les conditions d'acquisition de la société, créée en 2021, n'ont pas été étudiées.

---

## C12 — Château de la Treyne (Lot), famille Gombert

**Comptes [VÉRIFIÉ INPI, S-43]**
- Société d'exploitation 328062724, créée en 1983 ; les murs sont détenus par une société civile immobilière depuis 1981.

| Exercice (clos en octobre) | CA | EBE | RN |
|---|---|---|---|
| 2016 | 2,05 M€ | +0,35 M€ | −0,02 M€ |
| 2017 | 2,31 M€ | +0,45 M€ | +0,05 M€ |
| 2018 | 2,30 M€ | +0,36 M€ | −0,08 M€ |
| 2019 | 2,23 M€ | +0,37 M€ | ≈ 0 |
| 2022 | 2,73 M€ | +0,73 M€ | +0,15 M€ |
| 2023 | NC | NC | −0,07 M€ |
| 2024 | NC | NC | +0,13 M€ |

**Leçon.** Un petit hôtel-château familial, aux murs anciens, **tourne à l'équilibre** : il dégage de quoi vivre et entretenir, sans enrichissement. C'est cohérent avec le cas Mercuès de la mission 1.

---

## C13 — Lieux de mariage

**Château la Beaumetane (Provence) [VÉRIFIÉ INPI, 797507829, S-45]**

| Année | CA | RN |
|---|---|---|
| 2016 | 147 k€ | +16 k€ |
| 2019 | 200 k€ | +22 k€ |
| 2020 | 50 k€ (−75 %, Covid) | −48 k€ |

Une nouvelle société civile immobilière à la même adresse a été créée en 2023 par d'autres personnes. C'est un changement de main probable, non vérifié par un acte.

**Château de Vergières (Saint-Martin-de-Crau).** Après le podcast de 2020 avec la propriétaire D. Rivière, deux sociétés ont été créées en 2024 par A. et L. Caneri, qui présentent désormais le lieu (site officiel lu, S-40). Le lieu a changé de main.

**Domaine de Quincampoix (vallée de Chevreuse).** Selon le site officiel (S-41), c'est un ancien domaine de chasse du XVIIe siècle de 20 ha entouré de douves. Il propose 620 m² de salles, 5 chambres, ainsi que des tournages et shootings. L'éditeur du site est la SCI de Quincampoix (451115277, location immobilière), sans comptes publics.

**Château de Santeny.** Lieu très présent sur YouTube (vidéos de mariages). La société exploitante n'a pas pu être identifiée : le site a renvoyé une erreur TLS et le registre donne des résultats ambigus.

**Leçon.** La location de salle seule plafonne à quelques centaines de milliers d'euros de CA. Les lieux changent souvent de mains.

---

## C14 — Les Fermes de Gally (famille Laureau)

**Comptes consolidés [VÉRIFIÉ INPI, 399506062, S-47]**
- CA de **50,3 M€ (2016) et 53,4 M€ (2017)**, EBE de 1,7 à 1,9 M€, RN d'environ +1,2 M€.
- Filiales : cafés, Fermière de Gally, Jardins de Gally.

**Leçon.** L'agritourisme de volume aux portes d'une grande ville est rentable. Il demande une clientèle de proximité nombreuse, que n'a pas un château isolé.

---

## C15 — Clarkson's Farm, Diddly Squat (Curdle Hill Farm Ltd)

- **[VÉRIFIÉ Companies House, 12478400, S-32]** Au 31 mars 2025 : capitaux propres de 231 452 £, 35 salariés en moyenne. Compte de résultat non publié.
- Bénéfice de 144 £ la première saison ; perte d'environ 86 000 £ d'aides attendue ; refus de permis pour le restaurant ; recours aux droits de construire automatiques des bâtiments agricoles (Irwin Mitchell, S-33 ; *The Grocer* cite 114 £ [REPÉRÉ]).
- La notoriété télévisuelle est la vraie source de valeur. Elle n'est pas reproductible.

---

## C16 — Cairns Farm Estate (Écosse)

Reconversion d'une ferme ovine de colline en lieu de mariages, pour 1,9 M£, lancée en 2017 (notes du podcast du Farm Advisory Service, AV5-065). **Non vérifié** : site hors service.

---

## C17 — Les Bordes Estate (Sologne)

- Domaine d'environ 560 ha [REPÉRÉ, S-36].
- Golf et 52 résidences de marque Six Senses : première tranche de 12 villas, de 2,57 à 8,18 M€ [REPÉRÉ, S-37].
- Adhésion au golf annoncée à « 40 000 €/an » dans un titre YouTube [REPÉRÉ, AV5-050].
- **[VÉRIFIÉ, registre, S-78]** Une société « Les Bordes Hotel Operations » a été créée le 2026-09-30, présidée par Les Bordes Estate. Cela confirme une ouverture hôtelière à venir.

**Leçon.** Sur un très grand domaine, la vente de résidences finance le cœur du projet. C'est transposable en petit (quelques maisons), sous de fortes contraintes d'urbanisme.

---

## C18 — The Newt in Somerset

Économie intégrée : restaurants, club de membres, chambres dans la ferme, cidre, fromagerie de bufflonnes, parc à cerfs (transcriptions, fiche F10). La chasse au faisan a été abandonnée. **Comptes non identifiés.**

---

## C19 — Relais & Châteaux (modèle de réseau)

- Environ 580 maisons dans 65 pays (S-34).
- Entrée de 10 000 à 15 000 € et cotisation de 20 000 à 30 000 € par an selon *Paperjam* (2026, S-35). *Le Temps*, vers 2003, donnait 10 000 € d'entrée et 11 000 à 15 000 € par an (S-50).
- La marque apporte de la distribution internationale et un prix moyen plus élevé (selon l'hôtelier interrogé par *Paperjam*).
