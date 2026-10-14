# Benchmark — Domaines historiques transformés économiquement (Agent 7)

> Date de recherche : 2026-10-14. Auteur : Agent 7 (Benchmark & intelligence économique).
> Sources : voir `_brut/sources_agent7.csv` (identifiants S01…S60 cités entre crochets).

## 0. Avertissement méthodologique (à lire avant tout chiffre)

- **Accès limité aux registres.** Dans cette session, WebFetch a échoué sur TOUS les domaines testés (erreur DNS `ENOTFOUND` : Charity Commission, Companies House, Pappers, Wikipedia, charitylens, linfodurable) et les connexions directes (curl) vers Pappers / Companies House / Charity Commission sont refusées par le proxy (403). **Aucun compte déposé n'a donc été ouvert directement.** Les chiffres ci-dessous proviennent des résultats WebSearch (extraits/synthèses des pages listées, dont des pages officielles du Charity Commission et de Xerfi). Fiabilité ramenée à « moyenne » tant qu'ils n'ont pas été relus sur la pièce d'origine.
- **Quota de recherche épuisé** en fin de mission (limite partagée de 200 recherches) : Castle Leslie (comptes), Mount Juliet, Coolmore, Euston, Hambleden, Château de Vallery, Château de Mazan, Domaine de la Butte aux Bois (historique de propriété) n'ont pas pu être documentés ou seulement partiellement. Ils ne figurent pas comme cas, ou figurent avec « Je ne sais pas ».
- Légende de statut : **FAIT SOURCÉ** [Sxx] / **ESTIMATION** (hypothèse explicitée) / **INCONNU**.
- Catégorie économique de chaque cas : **A = rentabilité (ou excédent d'exploitation) démontrée par des comptes** / **B = CA ou recettes connus, rentabilité inconnue ou négative** / **C = aucun chiffre public trouvé**.
- Ne pas confondre : *recettes / chiffre d'affaires* ≠ *résultat* ≠ *fortune du propriétaire*. Pour les trusts britanniques, « income − expenditure » est un excédent comptable de l'organisme caritatif, pas la rentabilité du domaine privé ni de la famille.

---

## 1. Tableau de synthèse

| # | Domaine (pays) | Acquéreur / exploitant | Type | Équestre ? | Catégorie | Chiffre clé (sourcé) |
|---|---|---|---|---|---|---|
| 1 | Guédelon (FR) | Société privée du chantier | Création ex nihilo, visites | Non (chevaux de trait sur chantier non vérifié) | **A** | CA 6,0 M€ et RN 879 k€ en 2023 [S07] |
| 2 | Chambord (FR) | EPIC d'État | Public | Oui (spectacles équestres non vérifiés ici) | **B** | Recettes 20,3 M€ 2023 ; ressources propres > 85 % [S10][S11] |
| 3 | Vaux-le-Vicomte (FR) | Famille de Vogüé (5e génération) | Privé familial, visites/événements/tournages | Non | **C** (charges seules) | ~9 M€/an « à trouver » (2016) [S13] ; 320 000 visiteurs 2019 [S14] |
| 4 | Domaine de Chantilly (FR) | Fondation (Institut de France / Aga Khan) | Mécénat + visites, Grandes Écuries | **Oui** | **B (déficitaire)** | 2020 : 7 M€ recettes vs 13 M€ coûts [S16] |
| 5 | Blenheim Palace (UK) | Blenheim Palace Heritage Foundation | Trust + commerce | Oui (horse trials) | **A** | Income £30,96 M / expenditure £27,79 M (exercice clos 03/2025) [S20] |
| 6 | Chatsworth (UK) | Chatsworth House Trust | Trust + commerce | Partiel | **A (fragile)** | Income £19,35 M / exp. £17,39 M (03/2025) ; déficit 2020/21 [S23] |
| 7 | Burghley (UK) | Burghley House Preservation Trust + Burghley Horse Trials Ltd | Trust + événement équestre | **Oui** | **A** | Income £16,04 M / exp. £15,60 M (01/2025) [S26] |
| 8 | Highclere (UK) | Comte et comtesse de Carnarvon | Privé, TV, mariages, marques | Partiel (exports d'aliments chevaux) | **C** | ~£12 M de travaux en 2009 ; « à peu près l'équilibre » en 2023 [S29][S30] |
| 9 | Castle Leslie (IE) | Sammy Leslie (héritière, trustee) | Hôtel + **centre équestre** | **Oui** | **C** | Rénovation ~10 M€ (2006-2007) avec aides publiques irlandaises/UE [S33][S34] |
| 10 | Ballyfin (IE) | Famille Krehbiel (US) | Hôtel ultra-luxe | Non | **B (pertes)** | Perte 2024 ≈ 389 k€ ; CA hébergement ~4 M€ [S37] ; travaux > 50 M€ (estimation presse) [S38] |
| 11 | Château de la Motte Husson (FR) | Dick & Angel Strawbridge (UK) | Privé, TV, mariages, livres | Non | **C** | Prix d'achat « £280 000 » NON CONFIRMÉ [S41] |
| 12 | La Bourdaisière (FR) | Louis-Albert et Philippe-Maurice de Broglie | Hôtel + jardins + produits | Non | **C** | Rachat en 1991, LA de Broglie a 29 ans [S44] |
| 13 | Château de Mercuès (FR) | Georges Vigouroux (vigneron) puis son fils | Hôtel Relais & Châteaux + vignoble | Non | **C** | 30 chambres, 32 ha de vignes [S47] |
| 14 | Domaines de Fontenille / Primard (FR) | F. Biousse & G. Foucher (entrepreneurs mode) | Collection d'hôtels | Non | **C** | Primard acquis 2018, ouvert juin 2021, ~40 chambres [S50][S51] |
| 15 | La Mothe-Chandeniers (FR) | SAS de ~25 000 co-propriétaires (Dartagnans) | Rachat participatif | Non | **C** | Achat 500 000 € (déc. 2017) ; ~1,6 M€ collectés [S01][S02] |
| 16 | Les Bordes (FR) | Consortium RoundShield (2018) | Golf + immobilier + hôtel | Non | **C** | 565 ha ; Six Senses + 120 résidences [S53] |
| 17 | Haras de Hus (FR) — **contre-exemple** | Xavier Marie (fondateur Maisons du Monde) | Haras sport (dressage/CSO) | **Oui** | **B (cessation)** | CA 1,77 M€ 2024 [S56] ; mis en vente 20 M€ (2023) → 12,9 M€ (2024) [S57][S58] |
| 18 | Adare Manor (IE) — **contre-exemple** | JP McManus | Hôtel/golf ultra-luxe | Non | **B (pertes)** | Pertes 2023, 2024, 2025 (comptes détaillés non publics) [S39][S40] |
| 19 | Châteaux-hôtels en procédure (FR) — **contre-exemples** | Sacy (groupe Millésime), Rochegude, Ygrande | Hôtellerie | Non | **B/C** | Sacy : murs vendus 6 M€ (04/2022) puis redressement 2025 [S59] |
| 20 | Haras national du Pin (FR) — **contre-exemple public** | État → département de l'Orne | Public équestre | **Oui** | **C** | Budget prévisionnel 2016 ~1,16 M€ ; État voulait supprimer 21 des 28 postes en 2019 [S61][S62] |

Cas complémentaires plus courts (section 3) : Château de la Ferté-Saint-Aubin, Château des Milandes (dont la vente forcée de 1968), Château de Gudanes, Courances, Brissac, Houghton, Badminton, Haras de Jardy, jeunes couples (Bourneau, Hazeville).

---

## 2. Fiches détaillées

### 2.1 Guédelon (Treigny, Yonne) — catégorie A
- **Situation initiale :** pas une acquisition de château existant : chantier de construction d'un château fort selon les techniques médiévales, projet né en 1994 [S08].
- **Modèle :** billetterie (une grande partie des entrées), boutique, restauration ; chantier autofinancé ; seuil d'autofinancement « dépassé dès 2000 avec 114 000 visiteurs » [S09].
- **Chiffres (FAIT SOURCÉ via fiche Xerfi, non relu sur Infogreffe) :** CA 4,65 M€ (2022), ~6,0 M€ (2023), 6,33 M€ (2024) ; résultat net 2023 : 879 k€ [S07]. CA 2014 : 4,1 M€ [S09]. Fréquentation : 265 000 visiteurs en 2022 dont 1/3 de scolaires [S08] ; « ~300 000/an » selon d'autres sources [S12].
- **ESTIMATION :** recette par visiteur ≈ 4,65 M€ / 265 000 ≈ **17,5 € / visiteur (2022)**, tous postes confondus (hypothèse : CA 2022 et fréquentation 2022 de sources différentes).
- **Leçon :** un récit unique + un public scolaire/familial récurrent peut rendre un site autonome sans fortune préalable, mais il faut **> 100 000 visiteurs/an** pour l'équilibre (seuil 2000) — ordre de grandeur hors d'atteinte d'un domaine privé isolé en zone rurale sans « concept ».
- **Points de doute :** le nom du ou des fondateurs et la structure juridique exacte n'ont pas été vérifiés dans cette session.

### 2.2 Domaine national de Chambord — catégorie B (public)
- EPIC créé en 2005 : recettes = ~67 % d'un budget de fonctionnement d'un peu plus de 5 M€ en 2005 ; ~87 % de ~16,5 M€ en 2014 [S10].
- Rapport d'activité 2016 : frais de fonctionnement 11,713 M€, CA 9,660 M€, taux d'indépendance financière 85,7 % [S11].
- Recettes 2023 : 20,3 M€ (contre 16,8 M€ en 2022) [S10] ; 2025 : recettes liées à la fréquentation 24,34 M€ (+13,3 %) [S10][S12b].
- Subvention de fonctionnement < 10 % du budget + 2,5 M€/an de subvention d'investissement [S10]. Aile François Ier : 37 M€ en 3 phases, dont phase 1 = 12 M€ (6 M€ autofinancés) [S10].
- **Leçon :** même le 2e château le plus visité de France ne finance pas seul ses grosses restaurations : l'investissement reste subventionné / mécéné.

### 2.3 Vaux-le-Vicomte (Maincy, Seine-et-Marne) — catégorie C
- **Acquéreur historique :** Alfred Sommier (1875) ; famille de Vogüé ; ouverture au public en 1968 pour compenser les dépenses de préservation [S15] ; restaurant ouvert en 1985, association des Amis (1983) véhicule de collecte [S15b].
- **Gestion :** Jean-Charles et Alexandre de Vogüé depuis 2012, rejoints par Ascanio en 2015 [S15b].
- **Chiffres :** « près de 9 millions d'euros doivent être trouvés chaque année par 3 frères » (France TV, 2016) [S13] ; ~300 000 visiteurs/an, objectif 400 000 en 2020 [S12c] ; ~320 000 visiteurs en 2019 [S14] ; > 70 salariés [S12d].
- **CA / résultat : INCONNU.** Vérification : rechercher la SIREN de la société d'exploitation sur Pappers/Infogreffe (non accessible dans cette session).
- **ESTIMATION :** 9 M€ / 320 000 visiteurs ≈ **28 € de besoin par visiteur**, ce qui suppose des recettes fortes hors billetterie (événements privés, tournages, chandelles).

### 2.4 Domaine de Chantilly (Oise) — catégorie B, déficitaire, équestre
- Fondation créée en 2005 (État, Institut de France, collectivités, mécènes) ; l'Aga Khan s'en retire en janvier 2020 [S16][S17].
- 2020 : recettes billetterie 6 M€, recettes totales 7 M€, coûts fixes et personnel 13 M€ → **déficit d'exploitation ~6 M€** ; « pas de subvention » selon le directeur [S16]. Déficitaire « depuis des années » avant le Covid selon une autre source [S16].
- Mécénat de l'Aga Khan : 30 M€ sur 2006-2025 (question Sénat) / 40 M€ / 70 M€ selon les sources — **divergence non résolue** [S17][S18].
- **Leçon (contre l'hypothèse de viabilité) :** un site équestre de premier rang mondial (Grandes Écuries, Musée du Cheval) a eu besoin de dizaines de millions de mécénat et reste structurellement déficitaire. Le cheval patrimonial ne finance pas le monument.

### 2.5 Blenheim Palace (Oxfordshire) — catégorie A
- Blenheim Palace Heritage Foundation (charity 1166164) — exercice clos le 31/03/2025 : income ≈ £30,96 M ; expenditure ≈ £27,79 M ; dont trading £16,02 M, activités caritatives £11,07 M, dons £3,06 M, placements £0,81 M [S20].
- Historique income : £17,58 M (2021), £27,21 M (2022), £22,44 M (2023), £28,89 M (2024), £30,96 M (2025) [S20].
- Visites 2025 : 980 678 (1er site Historic Houses) [S21] ; impact économique estimé £175 M (Oxford Brookes, 2022-23) [S22].
- **Équestre :** le domaine accueille des horse trials (non chiffré ici).
- **Leçon :** les recettes « trading » (événements, commerce) dépassent désormais la billetterie/caritatif ; échelle : ~1 M de visites.

### 2.6 Chatsworth (Derbyshire) — catégorie A fragile
- Chatsworth House Trust (511149) — exercice clos 31/03/2025 : income £19 351 531 ; expenditure £17 393 147 ; 170 salariés [S23].
- Historique : 2020/21 £7,44 M de recettes pour £10,08 M de dépenses (déficit Covid) ; £13,94 M / £11,46 M (2021/22) ; £17,41 M / £15,84 M (2022/23) ; £19,40 M / £17,74 M (2023/24) [S23]. **Contradiction relevée :** la synthèse de recherche indique à la fois « expenditure exceeded income in 2024/25 » et des chiffres 2024/25 où l'income dépasse l'expenditure → seul le déficit 2020/21 est retenu comme certain.
- Une dotation (endowment) constituée par la vente d'œuvres d'art et d'autres ressources familiales complète les recettes visiteurs [S24].
- **Leçon :** la rentabilité repose aussi sur une dotation patrimoniale préexistante — non transposable à un primo-accédant.

### 2.7 Burghley (Lincolnshire) — catégorie A, équestre
- Burghley House Preservation Trust (258489) — exercice clos 31/01/2025 : income £16 035 165 ; expenditure £15 601 080 ; dont trading £9,31 M, placements £5,24 M, activités caritatives £1,39 M [S26]. Income ~£7,95 M en 01/2021 [S26].
- Visiteurs +86 % (rapport 2024) après parking et aire de jeux « Hide and Secrets » [S27].
- **Burghley Horse Trials Ltd** (Companies House 07087188), créée le 25/11/2009, organise l'événement pour le domaine depuis janvier 2011 ; derniers comptes au 31/01/2024 [S28]. **CA de l'événement : INCONNU** (les chiffres de ltds.uk sont explicitement « illustratifs » — rejetés).
- Avant la reprise, l'événement générait ~£380 000 de bénéfice pour British Eventing (2009) [S28b].
- **Leçon :** un grand événement équestre internationalement reconnu peut être internalisé par le domaine — mais il s'appuie sur des décennies d'historique et le revenu du trust repose aussi sur £5 M de revenus de placements.

### 2.8 Highclere Castle (Hampshire) — catégorie C
- 2009 : château nécessitant ~£12 M de réparations dont £1,8 M urgents [S29].
- Lady Carnarvon : le tournage de Downton Abbey « n'a pas tant profité financièrement » au château ; c'est la visibilité qui attire les visiteurs ; activités : livres, gin, podcasts, visites [S29].
- Mariages : ~25 grands mariages/saison, jusqu'à 40 % de l'activité au pic ; arrêt annoncé en 2023 (pénurie de personnel post-Brexit) ; 2023 attendu « à peu près à l'équilibre » ; baisse aussi de la boutique et des exportations d'aliments pour chevaux [S30].
- **CA / résultat : INCONNU** (aucun compte trouvé ; les « net worth » en ligne sont non sourcés et écartés).
- **Leçon :** la médiatisation mondiale ne garantit pas la rentabilité ; dépendance à la main-d'œuvre événementielle.

### 2.9 Castle Leslie Estate (Glaslough, Co. Monaghan) — catégorie C, **équestre**
- Sammy Leslie reprend en 1992 un domaine « délabré », toit qui fuit, « pas d'argent en banque » ; premiers revenus via un salon de thé [S33].
- Le Hunting Lodge et le centre équestre avaient été vendus en 1984 ; elle tient une écurie de commerce (achat, vente, débourrage) jusqu'en 1987 ; **rachat du Lodge et des écuries en 2004** [S33].
- Rénovation ~10 M€ démarrée en janvier 2006 (lodge + nouveau centre équestre), **avec aides du gouvernement irlandais et cofinancement UE** ; réouverture mai 2007 [S33][S34].
- Activités : hôtel (château + lodge), spa, centre équestre, école de cuisine, séminaires [S33].
- **CA / résultat : INCONNU** (recherche des comptes non effectuée : quota épuisé). Vérification : CRO irlandais (Companies Registration Office).
- **Leçon :** cas le plus proche de l'objectif du porteur (cheval structurant + hébergement) ; mais 12 ans entre reprise et rachat des écuries, et un financement public significatif.

### 2.10 Ballyfin (Co. Laois) — catégorie B, pertes
- Achat 2001 ou 2002 (divergence) par Fred et Kay Krehbiel ; ~9 ans de restauration ; ouverture en 2011 [S36][S38].
- Coût : non publié ; « > 50 M€ » selon l'Irish Times (non confirmé par la direction) [S38].
- Comptes (presse) : 2020 perte avant impôt 1,86 M€ ; 2021 profit avant impôt 786 923 € aidé par 1,02 M€ d'aides Covid ; revenus 1,12 → 3,73 M€ [S37b]. 2024 : perte après impôt 389 281 € (vs 90 155 € en 2023) ; CA hébergement ~4 M€ [S37].
- **ESTIMATION :** si l'investissement est de 50 M€ et le CA de ~4 M€, le rendement brut est < 8 % du capital en CA (pas en marge) → **le capex n'est pas remboursable par l'exploitation** ; le modèle repose sur la fortune du propriétaire.

### 2.11 Château de la Motte Husson (Mayenne) — « Escape to the Chateau » — catégorie C
- Janvier 2015 : Dick et Angel Strawbridge quittent un appartement de 2 pièces à Londres pour un château délabré : 45 pièces, 7 dépendances, 12 acres (~5 ha), douves [S41][S42].
- **Prix d'achat : INCONNU / non confirmé.** Le chiffre de £280 000 n'apparaît que dans une copie secondaire attribuée à The Sun, sur un domaine douteux [S41]. À ne pas utiliser dans un modèle.
- Modèle : émission TV Channel 4 (vente du programme), mariages, week-ends gastronomiques, livres [S42][S43].
- **CA / résultat : INCONNU.**
- **Leçon :** le levier principal est la notoriété TV préexistante de Dick Strawbridge (présentateur) ; la surface (5 ha) est sans rapport avec un projet équestre > 50 ha.

### 2.12 Château de la Bourdaisière (Montlouis-sur-Loire) — catégorie C
- Remis en vente car « trop coûteux à mettre aux normes » ; acheté en 1991 par Louis-Albert de Broglie (29 ans) et son frère Philippe-Maurice [S44][S45].
- Modèle : hôtel (22 à 25 chambres + 4 appartements selon les sources — divergence), restaurant, parc ouvert, Conservatoire national de la tomate, boutique de produits dérivés [S44][S46].
- **Leçon :** jeune acquéreur (29 ans) → diversification par une **thématique propre** (tomate, biodiversité) qui crée une marque. Fortune familiale initiale : INCONNUE.

### 2.13 Château de Mercuès (Lot) — catégorie C
- Acheté en 1983 (ou 1987, divergence) par Georges Vigouroux, vigneron de Cahors ; transformé en hôtel Relais & Châteaux + domaine viticole ; 30 chambres, 32 ha de Malbec (30 à 36 ha selon les sources), restaurant étoilé ; transmis au fils Bertrand-Gabriel [S47][S48].
- **Leçon :** l'acquéreur apporte un **métier préexistant** (le vin) qui valorise le château et inversement ; c'est l'équivalent possible du métier équestre du porteur.

### 2.14 Les Domaines de Fontenille (Biousse & Foucher) — Domaine de Primard (Eure-et-Loir/Normandie) — catégorie C
- Domaine de Fontenille (Lauris) acquis en 2014, ouvert en février 2016 [S49]. Primard (Guainville), ancienne propriété de Catherine Deneuve, acquis en 2018, ouvert en juin 2021, ~40 chambres [S50][S51]. Vente antérieure à 4 M€ en 2014 citée par un article people — **non vérifiée**.
- Capital : SOFIPACA, BNP Paribas, le chef Éric Frechon associé [S52][S49b].
- **Leçon :** modèle « collection » d'entrepreneurs déjà fortunés et levant des fonds régionaux — mutualisation des fonctions support. **CA : INCONNU.**
- **Point de doute :** le brief évoquait un lien Guerlain/Yvelines — **non confirmé** ; Primard est en Eure-et-Loir/Normandie et appartient à Fontenille.

### 2.15 Château de La Mothe-Chandeniers (Vienne) — catégorie C
- Ruines rachetées 500 000 € le 1er décembre 2017 via Dartagnans et l'association Adopte un château ; SAS ; ticket minimal 51 € pour devenir actionnaire ; ~6 500 contributeurs à l'achat (7 500 selon NPR) ; ensuite ~25 000 copropriétaires de 115 pays et > 1,6 M€ collectés (27 000 selon une source italienne) [S01][S02][S03][S04].
- **Situation 2024-2026 : INCONNUE** (comptes de la SAS au greffe de Poitiers non consultés).
- **Leçon :** le financement participatif peut acheter un bien, pas l'exploiter : 1,6 M€ est très inférieur au coût de restauration d'une ruine de cette taille (ordre de grandeur non sourcé). Gouvernance diluée — incompatible avec l'objectif « vivre dans le château ».

### 2.16 Les Bordes (Loir-et-Cher) — catégorie C
- Créé en 1987 par le baron Bich sur 565 ha de chasse ; à sa mort (1994), M. Sakurai seul propriétaire ; semi-léthargie ; vendu en 2018 à un consortium mené par Driss Benkirane (RoundShield) ; Six Senses + 120 résidences en construction [S53][S54]. Prix : INCONNU. Le lien « Discovery Land » du brief **n'est pas confirmé**.
- **Leçon :** pour les très grands domaines, la promotion immobilière (résidences) finance le patrimoine — modèle à capitaux de private equity.

---

## 3. Contre-exemples et cas d'échec

### 3.1 Haras de Hus (Petit-Mars, Loire-Atlantique) — échec / sortie d'un entrepreneur fortuné, **équestre**
- Propriétaire : Xavier Marie, fondateur de Maisons du Monde ; haras fondé en 2004 ou 2005 (divergence) ; 128 ha [S55][S57].
- Juin 2020 : mise en vente du haras et du cheptel [S55b]. Annonce de « fin d'une ère » : cessation d'activité, vente de tous les chevaux, semence et embryons [S56b]. Décembre 2023 : affiché 20 M€ [S57]. Octobre 2024 : Barnes à 12,9 M€ (–35 %) [S58]. Vente de dispersion le 11 juin 2024 [S57b].
- Chiffres (Xerfi) : CA 2024 : 1 771 k€ ; capital social 8 205 k€ [S56]. **Résultat : INCONNU** (à vérifier sur Pappers/Infogreffe).
- **Ce que ça contredit :** qu'un haras de sport haut de gamme, même porté par un entrepreneur multimillionnaire avec d'excellents étalons, soit rentable ; et que l'immobilier équestre se revende à son prix affiché.

### 3.2 Adare Manor (Co. Limerick) — pertes malgré la Ryder Cup et un propriétaire milliardaire
- Exploitant (Tizzard Holdings UC) déficitaire en 2023, 2024 et 2025 ; statut « unlimited » → comptes détaillés non publiés ; continuité d'exploitation acceptée par l'auditeur (BDO) [S39][S40].
- **Ce que ça contredit :** « luxe = rentabilité ».

### 3.3 Ballyfin — voir 2.10 (pertes 2023 et 2024 malgré un CA en hausse).

### 3.4 Domaine de Chantilly — voir 2.4 (déficit structurel d'un site équestre prestigieux).

### 3.5 Châteaux-hôtels en procédure collective (France)
- **Château de Sacy (Marne)** : groupe Millésime en difficulté depuis 2023 ; murs revendus 6 M€ en avril 2022 à une SCI (cession-bail) ; redressement judiciaire ouvert en 2025 ; repreneur identifié : groupe Reybier [S59].
- **Château de Rochegude (Drôme)** : exploitant Terroir et Gastronomie, conversion en liquidation judiciaire le 19/12/2023 (TC Romans-sur-Isère), vente du fonds [S60].
- **Château d'Ygrande (Allier)** : Groupe Cœur et Détente, liquidation judiciaire le 28/10/2025 (TC Cusset) [S60b].
- **Ce que ça contredit :** l'hôtellerie de château est un métier à forte intensité de main-d'œuvre et de capex ; des opérateurs spécialisés font faillite.

### 3.6 Château des Milandes (Dordogne) — vente forcée historique
- Joséphine Baker : vente aux enchères annoncée en 1964 pour raisons financières, vente effective en 1968 à une fraction de sa valeur (1/5e ou 1/10e selon les sources), expulsion en mars 1969 [S63][S64]. Rachat en 2001 par Claude de Labarre et sa fille Angélique de Saint-Exupéry, qui y créent un musée Joséphine Baker [S65].
- **Ce que ça contredit :** la notoriété personnelle (Baker était une star mondiale) ne protège pas d'une gestion où les charges dépassent les revenus. **Ce que ça confirme :** le second acquéreur a valorisé ce même récit (musée).

### 3.7 Haras national du Pin (Orne) — retrait de l'État
- EPA sous tutelle du ministère de l'Agriculture, dissous ; biens mobiliers transférés au département de l'Orne, immobiliers à l'État ; collectivités incapables d'investir davantage dans des biens qui n'étaient pas les leurs [S61]. Budget prévisionnel 2016 ~1,16 M€ [S61b] ; 2019 : l'État veut supprimer 21 des 28 postes qu'il finance [S62].
- **Ce que ça contredit :** même avec un statut public et un patrimoine équestre majeur, le modèle n'était pas autoporteur.

---

## 4. Cas complémentaires (informations partielles)

- **Château de la Ferté-Saint-Aubin (Loiret)** : acquis en 1987 par Jacques Guyot, ouvert au public et restauré ; deux grandes écuries de 1681 ; activités : escape games, visites à thème ; plein tarif 12,50 € (août 2024, avis visiteur — fiabilité faible) [S66][S67]. Catégorie C.
- **Château de Gudanes (Ariège)** : Karina et Craig Waters (Australie), acheté en 2013 après 2 à 4 ans de négociations, ruine classée, toit effondré ; financement privé + ventes de leur livre ; prix non divulgué [S68][S69]. Catégorie C.
- **Courances (Essonne)** : famille de Ganay, 1 800 ha ; parc de 75 ha ; ouverture le week-end d'avril à novembre ; potager bio relancé par Valentine de Ganay [S70][S71]. Catégorie C.
- **Château de Brissac (Maine-et-Loire)** : famille Cossé-Brissac ; chambres d'hôtes 15 avril–15 octobre ; vignoble de 28 ha ; ouverture au public motivée par fiscalité et coûts de chauffage (1980) [S72][S73]. Catégorie C.
- **Houghton Hall (Norfolk)** : Houghton International Horse Trials, > 700 chevaux/an, statut international dès 2007 ; selon le régisseur, l'événement a « mis Houghton sur la carte » ; en 2020, l'annulation a fait baisser les revenus [S74]. Aucun chiffre. Catégorie C.
- **Badminton (Gloucestershire)** : fondé en 1949 sur le domaine du duc de Beaufort ; > 200 stands commerciaux ; ~£170 000 reversés à British Eventing (vers 2010) ; dotation 2026 de £451 500 [S75][S76]. Revenus du domaine : INCONNUS.
- **Haras / Domaine de Jardy (Hauts-de-Seine)** : ~75 ha (centre équestre, golf, tennis, parc), propriété départementale depuis 2007, avis de concession de service public 2026 de valeur estimée 535 M€ HT (sur toute la durée de la concession — durée INCONNUE) [S77]. Modèle public-délégué, non transposable directement mais **piste de « contrôle durable sans propriété »** (concession).
- **Jeunes couples (presse)** : château de Bourneau (Vendée) — couple d'environ 30-31 ans, 16 ha, chambres d'hôtes et réceptions visées [S78] ; château d'Hazeville — racheté en 2021 par un jeune couple, gîte de 27 personnes ouvert en juin 2024 [S79]. Aucun prix ni CA publiés.
- **Non documentés (quota épuisé ou rien trouvé) :** Castle Leslie (comptes), Mount Juliet, Coolmore, Euston, Hambleden, Château de Vallery, Château de Mazan, historique de propriété de la Butte aux Bois (seuls faits : hôtel de Lanaken, bâtiments depuis 1924, rénovations 2016, restaurant 2 étoiles [S80]).

---

## 5. Synthèse — leçons transposables

### 5.1 Facteurs de succès communs (observés, pas démontrés statistiquement)
1. **Un métier préexistant de l'acquéreur, transféré au domaine** : vin (Mercuès), hôtellerie/mode (Fontenille), TV/ingénierie (Strawbridge), commerce de chevaux (Sammy Leslie). → Pour le porteur : le métier équestre doit être un *métier rentable* (pension, commerce, enseignement, événement), pas un loisir.
2. **Un récit/une marque unique** : Guédelon (construction médiévale), Bourdaisière (tomate), Milandes (Joséphine Baker), Downton (Highclere).
3. **Des revenus non-billetterie dominants** : à Blenheim, le trading (£16 M) dépasse désormais le reste ; à Burghley, trading + placements = 91 % des recettes.
4. **Le temps** : 9 ans de travaux à Ballyfin ; 12 ans à Castle Leslie entre reprise et rachat des écuries ; Vaux ouvert en 1968 et toujours dépendant d'un effort annuel ~9 M€.
5. **Le capital préalable ou externe** : dotations (Chatsworth), mécénat (Chantilly), aides publiques/UE (Castle Leslie), fortunes (Ballyfin, Adare, Hus), private equity (Les Bordes), foule (Mothe-Chandeniers).
6. **Le rôle des médias** : levier de fréquentation (Highclere, Strawbridge, Mothe-Chandeniers), mais **pas une source directe de rentabilité** selon la propriétaire de Highclere elle-même [S29].

### 5.2 Ordres de grandeur (à reprendre dans le modèle, avec prudence)
- Grandes demeures britanniques équilibrées : **£15 à 31 M de recettes annuelles** pour un excédent de £0,4 à 3 M (Burghley, Chatsworth, Blenheim) [S20][S23][S26].
- Seuil d'autofinancement d'un site de visite pur : **~100 000 visiteurs/an** (Guédelon, 2000) [S09].
- Recette moyenne par visiteur, site de visite : **~17-18 €** (ESTIMATION Guédelon 2022).
- Coût annuel d'un grand monument privé : **~9 M€** (Vaux-le-Vicomte, 2016) [S13].
- Hôtel de château ultra-luxe : CA ~4 M€ pour > 50 M€ investis, exploitation déficitaire (Ballyfin) [S37][S38].
- Haras de sport haut de gamme sur 128 ha : CA ~1,8 M€, cessation et décote de 35 % sur le prix demandé en un an (Hus) [S56][S57][S58].

### 5.3 Ce que les contre-exemples contredisent
- « Un beau domaine équestre bien géré s'autofinance » → **contredit** par Haras de Hus, Chantilly, Haras du Pin.
- « Le luxe hôtelier rentabilise le château » → **contredit** par Adare, Ballyfin, Sacy, Rochegude, Ygrande.
- « La médiatisation suffit » → **contredit** par Highclere (équilibre en 2023) et Milandes (vente forcée malgré la célébrité).
- « Le financement participatif permet de devenir châtelain » → La Mothe-Chandeniers montre qu'il permet un rachat collectif, **pas le contrôle individuel** ni la vie sur place.
- **Aucun cas trouvé** d'un entrepreneur de moins de 30 ans, sans fortune familiale identifiée, ayant acquis un domaine > 50 ha à vocation équestre et le rendant **rentable selon des comptes publiés**. Les cas jeunes (Bourneau, Hazeville, Bourdaisière à 29 ans, Strawbridge) sont petits ou sans chiffres.

### 5.4 Implications pour le projet
- Le modèle le plus proche et le plus réaliste à étudier en priorité est **Castle Leslie** (hébergement + centre équestre), mais il a bénéficié d'un héritage et d'aides publiques — à vérifier dans les comptes (CRO irlandais).
- Le scénario « contrôle durable sans propriété » (concession type Jardy, bail emphytéotique, gestion pour un propriétaire) mérite d'être évalué par d'autres agents, vu l'apport limité.
- Toute projection de revenus événementiels équestres doit être confrontée au fait qu'**aucun chiffre public de rentabilité d'un événement équestre de domaine** (Burghley, Badminton, Houghton) n'a été trouvé.

---

## 6. Points de doute / hypothèses non vérifiées
1. **Aucun compte déposé lu directement** (WebFetch en échec DNS, registres bloqués par le proxy). Tous les chiffres financiers proviennent de synthèses WebSearch des pages citées ; à revérifier sur Charity Commission, Companies House, Pappers/Infogreffe, CRO.
2. Chatsworth 2024/25 : contradiction interne de la synthèse (« dépenses > recettes » vs chiffres montrant l'inverse).
3. Chambord : le titre TourMag « dépasse les 12 million de visiteurs en 2025 » est très probablement « 1,2 million » — non vérifié, non utilisé.
4. Prix d'achat de la Motte Husson (£280 000) : non confirmé, source secondaire douteuse.
5. Mécénat de l'Aga Khan à Chantilly : 30 / 40 / 70 M€ selon les sources.
6. Guédelon : CA (Xerfi) et fréquentation proviennent de sources et parfois d'années différentes ; le ratio € / visiteur est une estimation.
7. Ballyfin : coût > 50 M€ = estimation de presse ; chiffres 2024 issus d'un seul article, possiblement au niveau du groupe.
8. Haras de Hus : date de fondation 2004 vs 2005 ; résultat net inconnu ; statut de la vente en 2026 inconnu (disponibilité à vérifier).
9. Domaine de Primard : vente à 4 M€ en 2014 non vérifiée ; lien Guerlain du brief non confirmé.
10. Les Bordes : lien Discovery Land et prix de 2018 non confirmés ; année d'achat 2008 vs 2018 selon les sources.
11. Mercuès : année d'achat 1983 vs 1987.
12. Jardy : la valeur de 535 M€ est la valeur estimée totale de la concession (durée inconnue), pas un CA annuel.
13. Les données du site ltds.uk sur Burghley Horse Trials Ltd sont explicitement illustratives — rejetées.
14. Cas non couverts faute de quota : Mount Juliet, Coolmore, Euston, Hambleden, Vallery, Mazan, comptes de Castle Leslie, historique de la Butte aux Bois.
