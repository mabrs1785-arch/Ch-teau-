# Vérification indépendante du topo « Château d'Ygrande » (agent V, 14/10/2026)

> **Suivi des corrections (14/10/2026).** Ce rapport porte sur la première version du topo. Les erreurs E1 à E11, les erreurs d'attribution et les nuances N1 à N31 ont ensuite été reportées dans le topo (doc Claude, révision 106, et `Topo_Ygrande.md`). Les calculs de `Registres_et_comptes.md` ont été corrigés : subventions d'exploitation, dette de 194, 167 et 216 k€, pont d'EBE à −205 k€ de charges et −35 k€ de subventions. La citation de N5 est masquée ici, car elle visait une personne privée. Les citations ci-dessous reprennent donc des phrases qui ne figurent plus dans le topo.

Fichier contrôlé : `PROJET_CHATEAU_24H/02_BENCHMARK/Cas_Ygrande/Topo_Ygrande.md` (non modifié).

**Méthode.** J'ai rouvert moi-même les sources clés avec curl :
- API BODACC (21 avis pour la société hôtelière, avis du haras, des écuries, du GFA et de la SARL de 1998) ;
- API ratios INPI-BCE et ses métadonnées (formules officielles) ;
- API Recherche d'entreprises ;
- France 3, L'Hôtellerie et Mon Bourbonnais ;
- CSV Atout France ;
- API notaires ; annonces SAFER (proprietes-rurales et French-Property), Barnes et Capifrance ;
- Gault&Millau, site du château et site des écuries, ABC Salles, Yonder, localisateur FFE, POP ;
- séries INSEE (BDM, page 2012672), Eurostat, IPC, IPPAP ;
- GHR, communiqué de Bercy du 03/02/2023, Sénat ;
- DVF 2021-2025 (recalcul complet).

J'ai aussi recalculé les natures cadastrales du GFA sur le fichier DGFiP extrait par Y3 et rejoué le script d'estimation de Y2.

**Limites.** 6 WebSearch utilisées sur 15. Légifrance et economie.gouv.fr renvoient 403 : les points de droit sont vérifiés par service-public, BOFiP, le Sénat, et des sources secondaires pour L. 631-8.

Scripts et téléchargements : `ygrande_V/scripts/`, `ygrande_V/dl/` (dossier de travail de la session, non versé au dépôt).

---

## 1. ERREURS (de la plus grave à la moins grave)

### E1. « Aucune aide publique visible. » (En bref ; section « Comment ça a été financé »)
- **Ce qui est faux.**
  - Selon les métadonnées officielles du jeu ratios_inpi_bce, plusieurs ratios sont rapportés au chiffre d'affaires augmenté des subventions d'exploitation (FL + FO, ligne FO de la liasse 2052) : `marge_ebe = EBE/(FL+FO)`, `caf_sur_ca` et `resultat_courant_avant_impots_sur_ca`.
  - On en déduit FO = EBE × 100 / marge_ebe − CA. Les subventions d'exploitation valent environ :
    - **38 k€ en 2017** (bornes d'arrondi 38,0 à 38,2) ;
    - **24 k€ en 2018** (23,7 à 25,2) ;
    - **3 k€ en 2019** (calcul).
  - Contrôle de cohérence : avec ces subventions, les produits financiers implicites (RCAI − EBIT + charges financières) valent environ 0 € les trois années (5 €, −12 €, 9 €). Sans elles, ils seraient de −358 € en 2017, ce qui est impossible.
  - Le topo cite lui-même un « prêt de l'État » (PGE probable). Le ministère le range parmi les « dispositifs de soutien public » (réponse au Sénat du 23/02/2023).
- **Version correcte.** « Les ratios publiés révèlent des subventions d'exploitation d'environ 38 k€ en 2017, 24 k€ en 2018 et 3 k€ en 2019 (calcul), de nature non publiée : aides à l'emploi ou à l'apprentissage, voire CICE s'il a été comptabilisé en subvention, ce qui collerait avec sa suppression en 2019 (hypothèse). S'y ajoute le PGE probable de 2020. Aucune subvention d'investissement ni aide d'État de plus de 100 k€ n'a été trouvée. »
- **Sources.** API ratios_inpi_bce (valeurs identiques au fichier du dépôt) ; métadonnées du jeu ; Sénat, question n° SEQ220700510.

### E2. « Entre 2017 et 2019, les ventes progressent de 11 %, mais les charges hors achats bondissent de 31 %, de 0,78 à 1,02 M€. Les ratios publiés ne disent pas lesquelles : salaires, énergie, sous-traitance ou loyers. »
- **Ce qui est faux.**
  - 0,78 et 1,02 M€ correspondent à « marge brute − EBE ». Selon la formule officielle de l'EBE, ce montant vaut charges externes + impôts + salaires + charges sociales, **moins les subventions d'exploitation** (et moins la production stockée ou immobilisée).
  - La baisse des subventions (38 → 3 k€) pèse environ **35 k€** dans les −240 k€ du pont d'EBE.
  - Hors subventions, les charges passent d'environ **0,82 à 1,03 M€, soit +25 %** et non +31 %.
  - L'EBE 2017 de 62 k€ contient environ 38 k€ de subventions : sans elles, il serait d'environ **24 k€ (2,3 % du CA)**.
  - Les ratios « disent » donc au moins une composante : les subventions.
- **Version correcte.** « … les charges hors achats, nettes des subventions d'exploitation, passent de 0,78 à 1,02 M€ (+31 %, calcul). Hors subventions, elles augmentent d'environ 25 % (0,82 → 1,03 M€). La quasi-disparition des subventions d'exploitation (environ 38 k€ en 2017, 3 k€ en 2019) explique environ 35 k€ de la chute de l'EBE. »
- **Graphique.** Corriger aussi la barre « autres charges −240 k€ » : −205 k€ de charges et −35 k€ de subventions.

### E3. « Électricité des professionnels à environ +60 % par rapport à 2019 », sous « **Les hausses de coûts de 2022-2023.** »
- **Ce qui est faux.** +60 % est le niveau de **2025**, pas celui de 2022-2023. Eurostat nrg_pc_205 (France, hors TVA, moyenne des deux semestres comparée à 2019) :

  | Tranche | 2022 | 2023 | 2025 |
  |---|---|---|---|
  | 20-499 MWh | +18 % | **+101 %** | +62 % |
  | < 20 MWh | +21 % | **+75 %** | +59 % |

- **Version correcte.** « Électricité des professionnels : environ +20 % en 2022 et +75 à +100 % en 2023 par rapport à 2019, encore environ +60 % en 2025 (Eurostat, calcul). »

### E4. « **Terres** : 40,7 ha selon l'[annonce SAFER](https://www.french-property.com/sale-property/3772-Av9jehwhfxhhpgne) »
- **Ce qui est faux.**
  - L'annonce SAFER indique **40 ha** : « Domaine d'un seul tenant de 40 ha », « Surface foncier non-bâti 40 ha ».
  - Le relais French-Property/Green-Acres cité en lien indique aussi « Land Size: 40 ha ».
  - 40,7 ha est le chiffre de Capifrance (ma-propriete.fr).
- **Version correcte.** « 40 ha selon l'annonce SAFER (40,7 ha selon Capifrance) ».

### E5. « 30 000 € de capital et des fonds propres sous 11 % du bilan : la première crise a tout emporté. »
- **Ce qui est faux.**
  - Les chiffres du topo lui-même le contredisent : après le Covid, la société fait un bénéfice de 47,5 k€ en 2021, et ses fonds propres restent positifs fin 2021 (4,7 % du bilan).
  - Ils ne deviennent négatifs que fin 2022.
  - La liquidation intervient en 2025, après un second prêt et deux procès.
- **Version correcte.** « … : le Covid a été absorbé par l'emprunt, mais la perte de 2022 a rendu les fonds propres négatifs, et la société n'a plus pu encaisser les chocs suivants. »

### E6. « Chaque activité avait sa propre société. » et « mais chaque activité était facturée par une société différente. »
- **Ce qui est faux.** Le tableau du topo le contredit : hébergement, restaurant et séminaires étaient tous facturés par la société hôtelière. Seules les activités équestres étaient portées par des EARL.
- **Version correcte.** « L'hôtel-restaurant et les activités équestres étaient portés par des sociétés distinctes. »

### E7. « 1,1 M€ de ventes pour 62 k€ d'EBE dans la meilleure année publiée. »
- **Ce qui est faux.** La meilleure année est 2017. Son CA est de **1,02 M€**, et son EBE inclut environ 38 k€ de subventions (E1).
- **Version correcte.** « 1,0 M€ de ventes pour 62 k€ d'EBE en 2017, la meilleure année publiée, dont environ 38 k€ de subventions d'exploitation (calcul). »

### E8. « environ 131 € la nuit en 2025, petit-déjeuner 20 € ([Gault&Millau](…)) ; fermé en janvier et février »
- **Ce qui est faux.** Gault&Millau (avis 2025) donne seulement « Budget (€) Par nuit sans petit déjeuner 131 ». Les autres éléments ne viennent pas de cette page :
  - le petit-déjeuner à 20 € vient de Trip.com et HalalBooking (Y2-28, Y2-31) ;
  - la fermeture en janvier-février vient d'autres fiches (Y2-29 ; LesRestos 2003).
- **Version correcte.** Attribuer chaque élément à sa source.

### E9. « plus de 20 ans dans le marketing de l'industrie médicale avant 1998 » (sourcé « site des écuries »)
- **Ce qui est faux.**
  - La page citée dit : « Après avoir sillonné le monde pour le compte de l'Industrie médicale pendant plus de 20 ans ».
  - « Marketing » ne vient que d'un extrait de recherche d'un article de 2001, non lu (Y1-22).
- **Version correcte.** « plus de 20 ans dans l'industrie médicale avant 1998 ».

### E10. « Le fonds de solidarité Covid n'est publié qu'en totaux nationaux »
- **Ce qui est faux.** Le jeu Etalab publie des agrégats par région et par département, croisés par secteur, forme juridique et effectif (Y3-30). Il ne publie simplement rien par entreprise.
- **Version correcte.** « n'est publié qu'en agrégats (région, département, secteur), jamais par entreprise ».

### E11. « Capital de 7 500 € ; liquidée sans actif » (EARL du haras)
- **Ce qui est faux.** L'avis BODACC A202600675925 parle de « Clôture pour insuffisance d'actif ». Cela signifie un actif insuffisant pour payer les créanciers, pas l'absence d'actif.
- **Version correcte.** « liquidation close pour insuffisance d'actif le 02/04/2026 ».

### Erreurs d'attribution mineures
- « le centre équestre continue ([BODACC]… » : cette information vient de France 3, pas du BODACC.
- « Liste des créances déposée au greffe de Cusset » : le BODACC dit « état des créances ».

---

## 2. FORMULATIONS À NUANCER

### Les plus importantes

**N1. Masse salariale de la cuisine**
- Citations : « Chef ex-étoilé, masse salariale de la cuisine +30 %, menus revus à la baisse » et « La masse salariale de la cuisine monte de 30 % alors que les prix des menus baissent. »
- Problème : L'Hôtellerie (03/12/2018) écrit « Cette orientation **va faire grimper** la masse salariale de la cuisine de 30 % ». C'est une prévision du dirigeant, pas un constat.
- Proposition : « le dirigeant prévoyait +30 % de masse salariale en cuisine ».

**N2. Lien entre prud'hommes et dette**
- Citations :
  - « Le Covid, deux prêts, la hausse des coûts et deux procès perdus aux prud'hommes ont porté sa dette à environ 800 000 €. »
  - « En 2025, deux procès perdus aux prud'hommes ont porté la dette à environ 800 000 €. »
  - « En 2025, deux procès perdus aux prud'hommes en appel portent la dette à environ 800 000 €. »
- Problème : France 3 écrit « la société perd deux procès au prud'hommes en appel. La dette s'élève **alors** à environ 800 000 euros ». L'article ne fait aucun lien de cause à effet et ne parle pas de hausse des coûts.
- Proposition : « En 2025, la société perd deux procès aux prud'hommes en appel ; sa dette atteint alors environ 800 000 € (France 3). » Dans l'En bref, retirer « la hausse des coûts » ou la marquer comme probable.

**N3. Cause de la fermeture**
- Citation : « L'hôtel a fermé parce qu'il ne dégageait presque pas de marge et n'avait aucune réserve. »
- Problème : c'est une interprétation présentée comme une cause établie.
- Proposition : « L'hôtel dégageait très peu de marge et n'avait pas de réserve ; il n'a pas absorbé le Covid, deux prêts et deux condamnations. »

**N4. « Prêt de l'État »**
- Citations : « Viennent ensuite un prêt de l'État en 2020 », « Prêt de l'État en 2020, second prêt » et « Un prêt de l'État en 2020, difficile à rembourser ».
- Problème : France 3 écrit « prêt à l'état », et le topo dit lui-même que c'est très probablement un PGE, c'est-à-dire un prêt bancaire garanti par l'État. « Prêt de l'État » est donc trompeur.
- Proposition : « un prêt garanti par l'État (PGE) probable en 2020 ».

**N5. Personne privée**
- Citation : [masquée : une phrase qui rattachait une personne privée à un litige ; elle a été supprimée du topo].
- Problème : la phrase rattache, sans preuve, une personne privée identifiable (son nom figure sur la fiche du registre que le topo met en lien) à un litige judiciaire.
- Proposition : **supprimer**.
- Dans la même phrase, autre point : « le dirigeant dit avoir récupéré les écuries « suite à une longue et pénible bataille juridique avec son ancienne associée » ». Dans l'article, c'est la narration du journaliste, pas une citation du dirigeant. Écrire plutôt « selon L'Hôtellerie, … ».

**N6. Chronologie et coût du conflit**
- Citations :
  - « | 2016-2017 | Conflit avec l'ancienne associée : le dirigeant crée sa propre EARL des écuries, l'EARL du haras quitte le château » ;
  - « Le conflit sur les écuries a duré des années, puis le dirigeant a dû réinvestir 200 000 € après les avoir récupérées. » ;
  - « a coûté de l'argent et de l'énergie : 200 000 € réinvestis dans les écuries en 2018 ».
- Problèmes :
  - La date du conflit et le lien avec les registres sont déduits : l'article de 2018 ne date pas le conflit, et ne dit pas « des années ».
  - Les 200 000 € sont un investissement de relance, pas un coût du conflit (« a dû » est une causalité ajoutée).
  - On ignore si les écuries avaient été achetées à plusieurs (leçon 5).
- Proposition : « 2016 : création de l'EARL des écuries ; 2017 : l'EARL du haras transfère son siège à la Popinière. Un lien avec la « longue et pénible bataille juridique » évoquée en 2018 est possible, non établi. Après l'avoir récupérée, le dirigeant a investi 200 000 € dans les écuries (L'Hôtellerie). »

**N7. Le cheval face à la restauration**
- Citations : « Ici, le cheval a mieux résisté que la restauration. » et « la restauration est le poste le plus risqué. »
- Problèmes :
  - Le haras a été liquidé le premier.
  - Les comptes des écuries ne sont pas publiés.
  - Rien dans les comptes de l'hôtel ne permet de dire que la restauration perdait de l'argent.
  - La seule source est l'affirmation de France 3 sur une activité « plus importante qu'avant Covid ».
- Proposition : « Ici, le centre équestre a survécu à l'hôtel, alors que le haras a été liquidé le premier. Les comptes publiés ne permettent pas de dire quelle activité perdait de l'argent. »

**N8. Date de cessation des paiements du haras**
- Citations : « | Déc. 2022 | L'EARL du haras cesse ses paiements | » et « **Le haras a sombré en premier**, en pleine flambée du fourrage ».
- Problèmes :
  - Le 06/12/2022 tombe **exactement 18 mois** avant le jugement du 06/06/2024. C'est le report maximal autorisé par l'article L. 631-8 du Code de commerce. Il s'agit donc d'une date juridique fixée à la limite légale, pas d'un événement observé ; la cessation réelle a pu être antérieure.
  - Depuis 2017, le haras était à la Popinière, avec une autre gérante : son lien avec le sort de l'hôtel n'est pas établi.
- Proposition : « Déc. 2022 : date de cessation des paiements retenue par le tribunal (report maximal légal de 18 mois avant le jugement) ».

**N9. Taux d'occupation comparé à l'Allier**
- Citation : « C'est un peu mieux que la moyenne de l'Allier, d'environ 50 % d'occupation. »
- Problèmes :
  - Les 55 % sont une hypothèse, calée pour atteindre 1,1 M€ avec un prix moyen supposé de 160 € TTC.
  - Les 50 % de l'Allier sont une moyenne simple des 12 taux mensuels, janvier et février compris, alors que le château était fermé ces deux mois.
  - Sur mars-décembre 2019, la moyenne de l'Allier est d'environ 54 %.
- Proposition : « Ce niveau, qui reste une hypothèse, est comparable à la moyenne de l'Allier sur les mois d'ouverture (environ 54 % de mars à décembre 2019, INSEE, calcul). »

**N10. Le marché local classé parmi les faits établis**
- Citation : « **Un marché local qui ne revient pas.** », dans « Ce qui est établi ».
- Problème : le chiffre est établi, mais pas son rôle dans la fermeture. En 2024, les hôtels 4-5 étoiles d'Auvergne-Rhône-Alpes progressent de 4,2 % (INSEE).
- Proposition : déplacer ce point dans « probable » ou dans le contexte.

**N11. Effectifs**
- Citation : « 16 à 19 chambres, un restaurant gastronomique et un centre équestre : 20 à 49 salariés déclarés en 2024, pour environ 1,1 M€ de chiffre d'affaires avant le Covid. »
- Problèmes : les 20 à 49 salariés sont ceux de la société hôtelière seule (les écuries en déclarent 6 à 9). La phrase compare aussi un effectif 2024 à un chiffre d'affaires 2017-2019.
- Proposition : « La société hôtelière déclarait 20 à 49 salariés en 2024 ; son CA d'avant Covid était d'environ 1,1 M€ (CA 2024 inconnu). »

**N12. Bouclier tarifaire**
- Citation : « Avec plus de 10 salariés, l'hôtel n'avait pas droit au bouclier tarifaire des TPE ».
- Problèmes :
  - L'effectif de 2023 est inconnu ; seul celui de 2024 est connu.
  - Le bouclier exigeait aussi un CA ou un bilan d'au plus 2 M€ et un compteur de moins de 36 kVA.
  - Les PME avaient droit à l'amortisseur électricité et, sous conditions, au guichet d'aide.
- Proposition : « Avec 20 à 49 salariés en 2024 (effectif 2023 inconnu), l'hôtel n'était vraisemblablement pas éligible au bouclier des TPE, mais relevait de l'amortisseur électricité des PME. »

**N13. Financement par l'emprunt**
- Citation : « L'exploitation reposait sur des sociétés de 30 000 € et 7 500 € de capital, financées par l'emprunt. »
- Problème : seule la dette de la société hôtelière est documentée (environ 0,2 M€). Elle peut inclure des avances d'associés. Le financement des EARL est inconnu.
- Proposition : reformuler en distinguant l'hôtel, dont la dette est documentée, et les EARL, dont le financement est inconnu.

**N14. GFA « familial » et achat de 1998**
- Citations : « **Les murs et les terres sont dans un GFA familial** » et « Acte de vente, au service de la publicité foncière (demande payante) ».
- Problèmes :
  - Le GFA a été créé le 02/09/1981 et a son siège au Mont depuis le 26/01/1982 (SIRENE), 17 ans avant l'arrivée du couple.
  - Ses associés sont inconnus : « familial » n'est pas établi.
  - L'achat de 1998 a pu prendre la forme d'un rachat de parts du GFA. Dans ce cas, il n'y a pas d'acte de vente au service de la publicité foncière, et DVF ne couvre pas ces cessions.
- Proposition : « dans le GFA Domaine du Mont, cogéré par le couple fondateur ». Ajouter dans les inconnues : « achat de 1998 : vente de l'immeuble ou rachat des parts du GFA ? ».

**N15. Ce que peuvent saisir les créanciers**
- Citation : « Les créanciers de l'hôtel n'ont pas de droit direct sur les murs, sauf garanties personnelles des associés, que l'on ne connaît pas. »
- Problème : l'exception est mal identifiée. Les vraies exceptions sont :
  - une hypothèque ou une caution réelle consentie par le GFA lui-même ;
  - une extension de la liquidation au GFA pour confusion des patrimoines (art. L. 621-2 du Code de commerce, non revérifié sur Légifrance).

  Les garanties personnelles des associés visent leurs biens propres, pas les murs.
- Proposition : reformuler en conséquence.

### Les autres, plus courtes

**N16. Exceptionnel 2019**
- Citation : « Il a donc fallu environ 175 k€ de produits exceptionnels (calcul) ».
- Problème : RN − RCAI = résultat exceptionnel − impôt sur les sociétés − participation. Le montant peut inclure un produit d'impôt.
- Proposition : « environ 175 k€ de résultat exceptionnel net ou de produit d'impôt ».

**N17. Charges financières**
- Citation : « pour 6 à 10 k€ d'intérêts par an (calcul) ».
- Problème : la ligne GU couvre le total des charges financières, pas seulement les intérêts.
- Proposition : « 6 à 10 k€ de charges financières ».

**N18. Immobilisations**
- Citation : « **Un outil usé** : les immobilisations de la société sont amorties à environ 80 %. »
- Problème : le ratio porte sur les immobilisations corporelles de la société hôtelière (agencements, matériel), pas sur les murs du GFA. Un amortissement comptable n'est pas un état physique.
- Proposition : « Des équipements très amortis : … ».

**N19. Aides au patrimoine**
- Citation : « Pas d'aides publiques spécifiques au patrimoine, donc. »
- Problème : seules les aides réservées aux monuments historiques sont exclues. D'autres dispositifs existent pour le patrimoine non protégé (non vérifié ici).

**N20. Site du château**
- Citation : « **Depuis la liquidation**, le site du château est édité par l'EARL des écuries ».
- Problème : on ne le sait que par les CGU publiées le 02/10/2026 (refonte du site entre le 22/09 et le 07/10/2026).
- Proposition : « En octobre 2026, … ».

**N21. Comptes 2020-2024**
- Citation : « Confidentiels ou non déposés : seul le liquidateur les détient ».
- Problème : les comptes 2021 et 2022 sont « partiellement confidentiels » : le bilan est public (les ratios de bilan sont publiés) et seul le compte de résultat est confidentiel. Les bilans sont probablement consultables à l'INPI.

**N22. SAFER propriétaire**
- Citation : « **La SAFER n'est pas propriétaire.** »
- Problème : ce n'est établi qu'au 01/01/2025.
- Proposition : « La SAFER n'était pas propriétaire au 01/01/2025 ».

**N23. Date de mise en ligne des annonces**
- Citation : colonne « En ligne depuis » = « 2026 » pour SAFER, Barnes et Capifrance.
- Problème : la date est inconnue. Les annonces ont seulement été vues en ligne le 14/10/2026 ; la référence SAFER contient « 26 ».

**N24. Annonces et cadastre**
- Citation : « **Les annonces enjolivent un peu.** »
- Problème : les natures cadastrales peuvent être anciennes, et Barnes annonce un étang d'environ 1,7 ha.
- Proposition : « Les annonces divergent du cadastre. »

**N25. Prix et bâti**
- Citation : « Le prix porte sur le bâti. »
- Proposition : « L'essentiel du prix porte sur le bâti (estimation). »

**N26. Avis clients**
- Citation : « Le site affiche 4,3/5 sur Google (458 avis) et 4,2/5 sur TripAdvisor (671 avis). »
- Problème : le widget ne nomme pas les plateformes ; Y2 les a déduites des logos.
- Proposition : « vraisemblablement Google et TripAdvisor ».

**N27. Les Collectionneurs**
- Citation : « la chaîne Les Collectionneurs (devenue Teritoria) ».
- Problème : ce n'est pas une chaîne mais une collection d'hôtels indépendants.

**N28. Prix des chambres d'hôtes**
- Citation : « des « chambres d'hôtes de luxe » de 90 à 190 € ».
- Problème : ce sont des prix « à partir de », selon la chambre.

**N29. Étiquetage des calculs**
- Citation : « **Statut des chiffres** : les chiffres sans mention viennent d'une page lue. »
- Problème : plusieurs calculs ne portent pas la mention « (calcul) » : +11 %, +31 %, 0,78 → 1,02 M€, −15 %, environ 50 % d'occupation (moyenne simple des taux mensuels), +60 %, +19 %, +30 % et +51 %, 80 %, « 4 à 15 fois ».

**N30. Prix net et SAFER**
- Citation : « Le domaine est en vente à environ 2,5 M€ net vendeur, notamment par la SAFER. »
- Problème : la SAFER affiche 2,65 M€ hors frais, sans prix net vendeur.

**N31. Autres formulations**
- « **Plus rien à sauver.** » : le critère légal est un redressement « manifestement impossible ». Des actifs peuvent encore être vendus.
- « **Le cheval faisait venir les clients.** » : à attribuer au dirigeant (30 % du CA selon lui en 2018).
- « car la fréquentation était « toujours insuffisante ». » : placé dans « établi », c'est le récit du dirigeant rapporté par France 3.

---

## 3. POINTS DE DROIT

| Point | Verdict | Source |
|---|---|---|
| L. 640-1 C. com. : liquidation si redressement « manifestement impossible » | **Confirmé** : cessation des paiements + redressement manifestement impossible. Texte en vigueur non consulté (Légifrance 403) | Rapport du Sénat n° 335 (2004-2005), commentaire de l'art. L. 640-1 ; jurisprudences de CA citées en recherche (Nîmes, 12/04/2023 ; Aix, 01/02/2024) |
| Chambres d'hôtes : 5 chambres et 15 personnes | **Confirmé, à préciser** : « 5 chambres et 15 clients en même temps » ; au-delà, appellation « chambres chez l'habitant » et règles proches de l'hôtellerie ; accueil assuré par l'habitant | entreprendre.service-public.gouv.fr F17452 (C. tourisme L324-3 à L324-5, D324-13 à R324-16) |
| Préemption du preneur en place prioritaire sur la SAFER | **Confirmé sous conditions** : preneur en place depuis plus de 3 ans, ayant exercé la profession agricole et exploitant personnellement, ne possédant pas plus de 3 fois le seuil du contrôle des structures, engagé à exploiter 9 ans (L. 412-5, L. 143-6, L. 412-12 C. rural). **Non vérifiable** : si une EARL preneuse (personne morale) peut l'exercer. Garder « à vérifier » en ajoutant ces conditions | Réponse ministérielle, JO Sénat du 13/11/2025 (question de Mme Lermytte) |
| Publication des baux de plus de 12 ans | **Confirmé**. Nuance : c'est une obligation, mais un bail non publié existe quand même, et un bail rural standard de 9 ans n'est pas publié. L'absence au SPF ne prouve donc pas l'absence de bail | BOFiP BOI-ENR-JOMI-10-20170802 § 40 (décret 55-22 du 04/01/1955, art. 28, 1°, b) |
| Bouclier tarifaire réservé aux TPE de moins de 10 salariés | **Confirmé**, avec en plus CA ou bilan ≤ 2 M€ et compteur < 36 kVA. **À nuancer** dans le topo : effectif 2023 inconnu ; les PME avaient l'amortisseur et le guichet | Communiqué de Bercy du 03/02/2023 (presse.economie.gouv.fr) |
| Ajout : report de la date de cessation des paiements limité à 18 mois avant le jugement (L. 631-8) | Confirmé par des sources secondaires, Légifrance non consultable. Cela fonde N8 | Actu-Juridique ; Gazette du Palais (Cass. com. 12/01/2022, n° 20-16.394) |
| Ajout : extension de procédure pour confusion des patrimoines (L. 621-2) | Non revérifié (cité en N15) | — |

---

## 4. CALCULS

| Calcul | Verdict | Détail |
|---|---|---|
| Pont d'EBE 2017 → 2019 | **OK arithmétiquement** | +109,9 / −31,8 / −240,5 = −100,6 k€. Marge brute = CA − achats consommés (formule officielle FL − (FS+FT+FU+FV)). Mais les −240 k€ se décomposent en −205 k€ de charges et −35 k€ de subventions (E2) |
| +11 % de ventes | **OK** | 10,7 % |
| +31 % de charges hors achats | **OK sur les charges nettes** (30,8 %), **corrigé à +25 % hors subventions** | 0,82 → 1,03 M€ |
| 175 k€ d'exceptionnel 2019 | **OK** | 174,7 k€ avec le CA seul ; 175,1 k€ avec la formule officielle (CA + subventions). Nature : résultat exceptionnel net d'IS (N16) |
| Dette financière ≈ 0,2 M€ | **OK** | Formule officielle (CAF rapportée au CA + subventions) : 194 / 167 / 216 k€ en 2017 / 2018 / 2019. Registres_et_comptes.md donnait 187 / 164 / 215 k€ en supposant des subventions nulles, à corriger |
| Charges financières 6 à 10 k€ | **OK** | 9,8 / 5,9 / 8,4 k€ |
| Dette 4 à 15 fois les fonds propres | **OK** | 4,4 / 14,8 / 12,2 ; fonds propres implicites 44 / 11 / 18 k€ |
| « Amorties à 80 % » | **OK** | Formule officielle : valeur nette / valeur brute des immobilisations corporelles. Net/brut de 15,5 à 22,1 %, soit 78 à 85 % amortis |
| 734 000 nuitées et −15 % | **OK** | 860 → 734 milliers, −14,7 % (BDM 010607097 ; 734 confirmé sur insee.fr 2012672) |
| « Environ 50 % d'occupation » | **OK, mais c'est un calcul** | Moyenne simple de 12 taux mensuels (49,5 % en 2025, 51,6 % en 2019), pas un taux officiel |
| Saisonnalité « 35 % / 65 % » | **OK** | Janvier 34,7 %, février 42,7 %, novembre 37,0 %, décembre 36,1 %, juillet 64,1 %, août 64,9 % (2025) |
| 3 500 €/ha × 37 ha ≈ 130 k€ | **OK** | DVF recalculé : 18 ventes de 2 ha et plus sans bâti, médiane 3 500 €, Q1 3 391, Q3 3 928 ; 129,5 k€. Sur les seules natures agricoles et forestières du cadastre (33,5 à 34,8 ha) : 117 à 122 k€, même ordre de grandeur |
| Répartition du CA | **OK, reproduite** | Script Y2 rejoué, scénario calé (1 073 k€) : hébergement 50,7 %, restaurant 34,3 %, événements 9,3 % ; 55 %, 3 198 nuitées, 6 966 couverts. Repose sur des hypothèses non sourcées |
| Graphiques : fonds propres/bilan, résultat net | **OK** | Arrondis corrects ; 2018 = 3,6 %, arrondi à 4 |
| Fourrages, alimentation | **OK** | Fourrages +30 % et +51 % (IPPAP 107,6 → 139,8 → 162,4) ; alimentation 1,068 × 1,118 = +19,4 % |
| Grille HCR +16 % | **OK en moyenne simple** des cases de la grille GHR (≈ 16 %) | La page GHR ne donne pas ce chiffre (il vient de Cogep) ; les premiers niveaux, alignés sur le SMIC, n'augmentent que de 4 à 7 % |
| Électricité | **Corrigé** | Voir E3 |

---

## 5. CE QUE J'AI CONFIRMÉ

- **BODACC, société hôtelière.**
  - Liquidation judiciaire directe le 28/10/2025 (TC de Cusset), publiée le 04/11/2025 ; cessation des paiements le 01/09/2025 ; liquidateur SELARL MJ de l'Allier.
  - État des créances déposé le 16/09/2026, publié le 22/09/2026.
  - Transformation en SAS publiée le 13/06/2024 ; capital porté à 30 000 € en 2008.
  - Comptes : 2016 et 2020-2023 confidentiels, comptes 2023 publiés le 10/04/2025, rien pour 2024 ; comptes 2011-2012 et 2013-2014 publiés par paquets.
- **BODACC, haras.** Liquidation judiciaire le 06/06/2024 (TJ de Moulins), cessation des paiements le 06/12/2022, clôture pour insuffisance d'actif le 02/04/2026, radiation ; siège à la Popinière en 2017, avec une gérante distincte depuis 2013.
- **BODACC, écuries.** EARL créée le 01/06/2016, capital 7 500 €, même gérant que l'hôtel, aucune procédure.
- **Registres.**
  - Dates de création : 21/12/1998, 19/03/2003, 01/06/2016, 25/09/1998 (SARL fermée le 21/02/2006).
  - Effectifs 2024 : 20 à 49 (hôtel), 6 à 9 (écuries).
  - GFA Domaine du Mont : créé le 02/09/1981, deux gérants (le couple), actif, aucun avis BODACC.
  - Le haras était au Mont de 2003 au 17/03/2017.
- **Ratios INPI.** Valeurs du fichier du dépôt identiques à l'API ; tous les chiffres publiés repris par le topo sont exacts.
- **Presse.**
  - France 3 du 29/10/2025 : citations exactes.
  - L'Hôtellerie du 03/12/2018 : 30 % du CA, 200 000 €, « longue et pénible bataille juridique », menus revus à la baisse, chef ex-étoilé.
  - Mon Bourbonnais : 1836, comte Eugène de la Roche, 1969, 1983, 1998, environ 200 ha et deux fermes, 40 ha, 16 chambres, ouverture le 24/04/1999, 3 étoiles NN, forêt de Tronçais « à quelques kilomètres ».
- **Classement.** Atout France : 4 étoiles le 27/06/2022, 19 chambres, 43 personnes.
- **Foncier (DGFiP 2025).** GFA propriétaire de 33 parcelles (39,66 ha) et 6 locaux ; 5,45 ha de bois et 1,38 ha d'eau ; aucune parcelle ni local pour les trois sociétés ; parcelles C1246 et C1248 (958 m²) sorties du GFA.
- **Annonces.**
  - Notaire de Souppes-sur-Loing : 2 625 000 € dont 125 000 € d'émoluments à la charge du vendeur (net 2,5 M€), en ligne depuis le 24/03/2026, DPE du 06/01/2026.
  - SAFER : 2 650 000 € hors frais, « accompagne la cession », agriculteur partenaire, 27 ha de pâtures, 10 ha de bois, étang de 3,7 ha.
  - Barnes : 2,65 M€, net 2,5 M€, DPE E, au moins 41 320 €/an d'énergie.
  - Capifrance : 2,65 M€, net 2,525 M€.
- **Offre.**
  - Écuries : tarifs des cours, pensions et séjours ; 25 chevaux et poneys.
  - Site du château en 2026 : EARL, chambres d'hôtes sans restaurant, 126 € par personne, 4,3/5 (458 avis) et 4,2/5 (671 avis).
  - Gault&Millau : 131 € ; ABC Salles : menus, salons, tarifs séminaires ; Yonder (02/07/2024) : 2 toques, Les Collectionneurs.
  - FFE : labels École française d'équitation, Poney Club, Cheval Club, Bien-être animal.
  - Aucune notice POP ; présidence de Nattitude en 2022.
- **Contexte.** INSEE : nuitées et saisonnalité ; IPC alimentation ; IPPAP fourrages ; conditions du bouclier ; Sénat : PGE remboursés à partir de 2022.
- **Étude interne.** Le « domaine type » à environ 2,5 M€ demande environ 3,4 à 3,9 M€ de fonds propres (Recommandation_finale, Feuille_de_route_2031, Scenario_C) : cohérent.
  - Remarque : Activites_complementaires.md définit le domaine type comme environ 50 ha à moins de 2 h 30 de Paris. Ygrande fait 40 ha et se trouve à « 3 h 45 de Paris » selon Capifrance.

## Non revérifié
- Module de transparence des aides d'État (TAM) ; RPG (26,9 ha déclarés à la PAC) ; listes Clef Verte ; erreur 404 sur Teritoria.
- Notes Booking et TripAdvisor (pages bloquées).
- Textes de loi sur Légifrance (403).
