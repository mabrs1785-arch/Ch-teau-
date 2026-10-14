# Cadre juridique, fiscal et réglementaire — Opération Château v2

**Agent 6 — Juridique, fiscalité, réglementation** · rédigé le 2026-10-14 · sources : `_brut/sources_agent6.csv` (identifiants `A6-xx` cités entre crochets).

> **Avertissement.** Ce document est une cartographie des règles, faite à partir des textes. Ce n'est pas une consultation juridique. Chaque point se termine par « À valider par ». Aucun montage ne doit être signé sans revue par un avocat fiscaliste, un notaire et, selon le cas, un avocat en droit rural.

---

## 0. Méthode, accès aux sources et légende

**Accès aux sources le 2026-10-14 (vérifié)**
- **Légifrance** a renvoyé une page anti-robot Cloudflare (HTTP 403) à chaque requête. WebFetch a aussi échoué (DNS) sur legifrance.gouv.fr, impots.gouv.fr et amf-france.org.
- **Textes des codes** : je les ai donc lus dans leur version consolidée, sur le **miroir git « Tricoteuses »** de la base LEGI de Légifrance (`git.tricoteuses.fr/codes/…`) [A6-98]. Chaque citation donne l'identifiant `LEGIARTI` et l'URL Légifrance correspondante. Dernière mise à jour du miroir selon le code : CGI au 01/09/2026, code rural au 14/10/2026, code de commerce au 01/10/2026, CMF au 01/09/2026, code de l'urbanisme au 01/09/2026, code du patrimoine au 05/08/2026, code de la santé publique au 11/10/2026, code de l'environnement au 07/10/2026, CCH au 09/10/2026, code du tourisme au 03/09/2026, code du sport au 08/10/2026, code civil au 29/07/2026, LPF au 01/10/2026. Le projet Tricoteuses précise lui-même que son contenu « peut contenir des erreurs ». Un contrôle sur Légifrance reste donc nécessaire avant tout acte.
- **Pages ouvertes directement** (curl) : BOFiP (bofip.impots.gouv.fr), entreprendre.service-public.fr, collectivites-locales.gouv.fr, culture.gouv.fr et urssaf.fr.
- **Sites inaccessibles** : impots.gouv.fr (« site en maintenance »), amf-france.org (aucun contenu exploitable), ifce.fr (protection anti-robot Incapsula), boss.gouv.fr (échec de connexion) et conseil-constitutionnel.fr (délai dépassé). Pour ces sites, je n'ai que des **EXTRAITS** issus de résultats de recherche.

**Légende des statuts**
- **[PAGE LUE]** : page ou texte ouvert et lu. Pour un article de code, « PAGE LUE (miroir) » signifie que le texte vient du miroir de la base LEGI.
- **[EXTRAIT]** : information vue seulement dans un résultat de recherche.
- **[ESTIMATION]** : calcul ou raisonnement explicite de ma part.
- **[INCONNU]** : je ne sais pas ; la façon de vérifier est indiquée.

---

## 1. Synthèse exécutive

1. **Le piège n° 1 de 2026 est la nouvelle taxe annuelle de 20 % sur les holdings patrimoniales (CGI art. 235 ter C, créé par l'art. 7 de la LF 2026).** Elle frappe les logements qu'une société à l'IS laisse occuper par son associé gratuitement ou sous le prix du marché, ainsi que les chevaux de course ou de concours détenus sans usage professionnel. Elle s'applique si la société détient au moins 5 M€ d'actifs, si une personne physique (famille élargie comprise) en détient au moins 50 % et si ses revenus passifs, loyers compris, dépassent 50 % de ses produits. Premier exercice concerné : celui clos au 31/12/2026. Conséquence directe : un schéma « PropCo à l'IS qui loge le fondateur » devient dangereux dès 5 M€ d'actifs. [A6-01, PAGE LUE (miroir)]
2. **Les sociétés à l'IR, comme une SCI de droit commun, sont hors du champ de cette taxe.** Une SCI à l'IR qui met gratuitement le château à disposition de ses associés ne génère pas non plus de revenu foncier imposable. En revanche, dès que ses recettes commerciales (meublé, événementiel) dépassent 10 % de ses recettes, elle bascule à l'IS. [A6-01, A6-60, A6-61, A6-55]
3. **Le Dutreil a été durci par la LF 2026 (CGI 787 B).** Les « logements et résidences » et les « chevaux de course ou de concours » sont exclus de l'exonération de 75 %, sauf s'ils sont affectés exclusivement à l'activité. L'engagement individuel de conservation passe à 6 ans. [A6-02]
4. **Le statut du fermage est d'ordre public (L.411-1 code rural).** Depuis 2005, les activités équestres sont agricoles (L.311-1). Louer des écuries ou des terres à un exploitant équestre, y compris à sa propre OpCo, peut donc créer un bail rural de 9 ans renouvelable, avec fermage encadré. Le statut couvre aussi certaines conventions de pension. [A6-40, A6-41, A6-90]
5. **La SAFER est renforcée en 2026.** Elle doit être informée de toute cession portant sur des biens de son champ, y compris les cessions de parts de sociétés. Elle peut préempter, au besoin partiellement, et réviser le prix. La loi n° 2026-796 du 18/08/2026 lui a donné un droit d'opposition sur les baux emphytéotiques portant sur des terres agricoles. La loi Sempastous soumet par ailleurs les prises de contrôle de sociétés agricoles au-delà d'un seuil régional à une autorisation préalable. [A6-43 à A6-49]
6. **Monuments historiques.** Le régime fiscal de faveur (156 et 156 bis, 795 A) ne bénéficie qu'aux contribuables à l'IR. Il impose 15 ans de conservation et une ouverture au public pour déduire 100 % des charges (sinon 50 %). Les travaux sont lourdement encadrés (autorisation, ABF, architecte qualifié pour un monument classé). Les subventions indicatives, de 40 % pour un monument classé et 20 % pour un inscrit, ne sont pas un droit. [A6-11, A6-20 à A6-29b]
7. **Lever des fonds** auprès de plus de 149 particuliers non qualifiés, ou par démarchage, sans passer par un prestataire agréé est illicite : les souscriptions sont nulles (L.411-1 CMF). Une SAS ne peut faire que les offres dispensées. Un véhicule de « club deal » qui investit selon une politique définie peut être requalifié en FIA (L.214-24 CMF). Proposer des parts de chevaux en vantant un rendement relève du régime des « biens divers » (L.551-1 CMF). [A6-70 à A6-75]
8. **Coûts fiscaux d'entrée et de structure.** Droits de mutation d'environ 6,32 % du prix dans les 88 départements au taux de 5 %. Droit de 5 % sur une cession de parts de société à prépondérance immobilière. IS à 15 % jusqu'à 42 500 € de bénéfice, puis 25 %. TVA à 5,5 % pour l'enseignement et la pratique de l'équitation, régime en vigueur depuis le 01/01/2024 et maintenu en 2026. [A6-30, A6-31, A6-33, A6-80]

### 1.1 Ce qui a changé en 2025-2026 (point de vigilance demandé)

| Texte | Changement | Entrée en vigueur | Effet sur le projet | Statut |
|---|---|---|---|---|
| LF 2026 (loi n° 2026-103 du 19/02/2026 [A6-03b]), art. 7 → **CGI 235 ter C** (nouveau) | Taxe annuelle de 20 % sur certains actifs non professionnels des holdings à l'IS : logements occupés gratuitement, sous le prix du marché ou loués fictivement, chevaux de course ou de concours, chasse, pêche, véhicules, bijoux, vins | Exercices clos à compter du 31/12/2026 | **Majeur** dès que la structure détenant le château est à l'IS et vaut ≥ 5 M€ | PAGE LUE (miroir) [A6-01] ; recoupé par A6-03 (PAGE LUE) et A6-97 (EXTRAIT) |
| LF 2026 → **CGI 975 VII** | Exonération d'IFI des parts déjà soumises à la taxe 235 ter C | Même calendrier | Neutralisation partielle seulement (20 % de taxe contre 1,5 % au plus d'IFI) | PAGE LUE (miroir) [A6-12] |
| LF 2026 → **CGI 787 B** (Dutreil) | Exclusion des logements et résidences, des chevaux de course ou de concours, etc., sauf affectation exclusive à l'activité pendant 3 ans avant la transmission et jusqu'à la fin de l'engagement ; engagement individuel porté à **6 ans** | Article en vigueur depuis le 21/02/2026. Application aux transmissions faites à compter de cette date selon un commentateur, non confirmée par le BOFiP | Le logement privé du château ne profitera pas du Dutreil | PAGE LUE (miroir) [A6-02] ; date EXTRAIT [A6-90b] |
| LF 2026, art. 11 → **CGI 150-0 B ter** (apport-cession) | Réinvestissement d'au moins 70 % dans les 3 ans, conservation 5 ans. Les activités immobilières et la gestion de son propre patrimoine immobilier sont exclues des réinvestissements éligibles (je n'ai pas comparé avec la version antérieure) | Cessions postérieures au 20/02/2026 | Impossible de financer l'achat du château avec un produit de cession placé en report ; financer une OpCo opérationnelle reste peut-être possible | PAGE LUE (miroir) [A6-17] |
| LF 2026, art. 81 → **CGI 278-0 bis** (réécrit) | Taux de TVA réduits réorganisés ; le **O (équitation à 5,5 %) est maintenu** | 01/03/2026. Transfert des règles de TVA vers le CIBS au 01/01/2027 (ordonnance 2025-1247) | Pas de hausse de TVA équestre en 2026 | PAGE LUE (miroir + BOFiP 25/03/2026) [A6-80, A6-81] |
| LF 2026, art. 96 | TVA à 10 % sur les travaux forestiers limitée aux travaux réalisés jusqu'au 31/12/2028 | — | Marginal (bois du domaine) | PAGE LUE (BOFiP) [A6-81] |
| LF 2026, art. 121 | Sécurisation du calendrier des délibérations départementales de hausse des DMTO (notifiées entre le 01/12/2026 et le 15/04/2027) | — | Les DMTO à 5 % restent possibles jusqu'au 31/03/2028 | PAGE LUE [A6-31] |
| LF 2026, art. 15 → CGI 219 | Article modifié (exercices clos à compter du 31/12/2025) ; **taux de 25 % et 15 % inchangés** | — | Aucun sur les taux | PAGE LUE (miroir) [A6-10] |
| LFSS 2026 (loi n° 2025-1403) | Hausse de 1,4 point de la CSG sur certains revenus du capital (dividendes, plus-values mobilières, LMNP) → prélèvements sociaux 18,6 %, PFU 31,4 % | 2026 | Coût de sortie du cash des sociétés | EXTRAIT [A6-95] |
| Loi n° 2024-1039 (« Le Meur ») | Enregistrement national obligatoire des meublés de tourisme (L.324-1-1 C. tourisme) ; micro-BIC limité à 15 000 € et abattement de 30 % pour les meublés de tourisme non classés (CGI 50-0) | Au plus tard le 20/05/2026 | Gîtes du domaine : classement conseillé | PAGE LUE (miroir) [A6-62, A6-63] |
| **Loi n° 2026-796 du 18/08/2026** « d'urgence pour la protection et la souveraineté agricoles » | Nouveau **droit d'opposition de la SAFER sur les baux emphytéotiques** (L.451-1-1). Le même jour (20/08/2026), L.143-1 et L.141-1-1 (nouveau I bis sur la notification séparée, qui écarte les monuments historiques) ont aussi été modifiés | 20/08/2026 | Le contournement de la SAFER par bail emphytéotique est fermé ; il faut s'attendre à des notifications plus lourdes | Texte PAGE LUE (miroir) [A6-47] ; rattachement de L.143-1 et L.141-1-1 à cette loi = hypothèse, la note de version n'étant pas affichée |
| Décret n° 2026-117 du 20/02/2026 → C. urb. R*421-17 | Article modifié (travaux soumis à déclaration préalable) pour les travaux engagés à partir de mars 2026 | Mars 2026 | Contenu exact du changement non analysé | PAGE LUE (miroir) [A6-37] |
| C. rural L.112-1-1 (CDPENAF) | Article modifié au 26/05/2026 | 26/05/2026 | Contenu du changement non analysé | PAGE LUE (miroir) [A6-38] |
| C. rural L.722-5 (activité minimale d'assujettissement MSA) | Nouvelle version au 01/01/2026 | 01/01/2026 | Affiliation MSA de l'exploitant équestre | PAGE LUE (miroir) [A6-87] |

---

## 2. Structures de détention

### 2.1 Règles
- **SCI de droit commun, à l'IR** (CGI art. 8, 1°). Les associés sont imposés sur leur quote-part. Une société civile qui exerce une activité commerciale (art. 34-35) est soumise à l'IS de plein droit (CGI art. 206-2). Le BOFiP admet qu'une société civile non agricole reste à l'IR tant que ses recettes commerciales hors taxes ne dépassent pas **10 % de ses recettes totales**. Pour les sociétés civiles agricoles, ce sont les seuils de l'art. 75 qui s'appliquent. [A6-55 ; A6-60 BOFiP BOI-BIC-CHAMP-40-20 du 19/08/2026, PAGE LUE]
- **Occupation gratuite par les associés d'une société non soumise à l'IS** : la société est « réputée se réserver la jouissance » du logement, ce qui n'entraîne pas de revenu foncier imposable. [A6-61, BOFiP BOI-RFPI-CHAMP-20-20, PAGE LUE]
- **SCI à l'IS (sur option), SAS ou holding** : IS, régime mère-fille (145/216), intégration fiscale (223 A), Dutreil pour une holding animatrice (787 B). Ces structures sont en revanche exposées à la taxe 235 ter C et à l'acte anormal de gestion (§ 3).
- **OpCo/PropCo** : la PropCo détient les murs, l'OpCo exploite. Le bail est un bail commercial pour l'hôtellerie et l'événementiel, mais peut être requalifié en **bail rural** pour la partie équestre (§ 9). C'est une convention réglementée si un dirigeant ou un actionnaire est commun (§ 4).
- **Démembrement** : en droits d'enregistrement, l'usufruit viager vaut 80 % et la nue-propriété 20 % lorsque l'usufruitier a moins de 31 ans. Un usufruit temporaire vaut 23 % par période de 10 ans (CGI 669). La SAFER peut préempter l'usufruit ou la nue-propriété de biens agricoles (L.143-1). L'administration peut écarter un montage à but exclusivement ou principalement fiscal (LPF L.64 et L.64 A). [A6-15, A6-43, A6-18, A6-19]
- **GFA** (groupement foncier agricole) : ses parts sont exonérées de droits de mutation à titre gratuit à hauteur de 75 % de la fraction correspondant aux biens loués par bail à long terme ou bail cessible (CGI 793 1 4°). Au-delà de 600 000 € par bénéficiaire, l'exonération tombe à 50 %. Le plafond passe à 20 M€ si le bien est conservé 13 ans de plus que les 5 ans de base (CGI 793 bis). En IFI, l'exonération est totale si le bail et le preneur remplissent les conditions du 976 III (bail d'au moins 18 ans, preneur familial exerçant à titre principal). Sinon, elle est de 75 % jusqu'à 101 897 € de parts, puis de 50 % au-delà (CGI 976 IV). Contrepartie : les terres doivent être données à **bail rural à long terme**. [A6-13, A6-14, A6-12b]
- **Groupement forestier** : exonération de 75 % des droits de mutation et de l'IFI sur la fraction boisée, si les bois présentent une garantie de gestion durable appliquée pendant 30 ans (CGI 793 1 3°, 976 II). [A6-13, A6-12b]

### 2.2 Conséquences pratiques
- Pour **la partie privée** (le logement du fondateur), les structures les plus sûres en 2026 sont la détention directe ou une **SCI à l'IR**, hors du champ de la taxe 235 ter C. Cela suppose de cantonner les activités commerciales hors de la SCI, sous la limite des 10 %. **[ESTIMATION]**
- Pour **l'exploitation** (équestre, hébergement, événements) : une ou plusieurs **OpCo à l'IS**, éventuellement sous une holding animatrice. L'activité équestre peut aussi être portée par une société civile agricole (EARL ou SCEA). Ce choix reste à arbitrer avec l'expert-comptable.
- Un **GFA ou groupement forestier familial** porte bien les terres et les bois pour la transmission et l'IFI. Il fige cependant les terres dans un bail rural long. C'est cohérent si le preneur est l'OpCo équestre du fondateur. **[ESTIMATION]**
- Le **démembrement** « nue-propriété au fondateur, usufruit temporaire à une société » se heurte à l'objectif de vivre au château : l'usufruitier contrôle la jouissance. Si cet usufruitier est une société à l'IS qui loge le fondateur, on retombe dans le champ de 235 ter C (7°).

### 2.3 Risques
- Une SCI à l'IR qui bascule à l'IS sans l'avoir anticipé (recettes commerciales au-delà de 10 %).
- Une PropCo à l'IS qui entre dans le champ de 235 ter C.
- La requalification en bail rural de la mise à disposition à l'OpCo équestre.
- Une division du château en lots ou en volumes qui fait perdre le régime monuments historiques (CGI 156 bis V).

**À valider par** : avocat fiscaliste et notaire (choix de la structure, division), expert-comptable (régime d'imposition), avocat en droit rural (bail).

---

## 3. Occupation privée d'un bien détenu par une société

### 3.1 Règles
- **Revenus distribués** : sont réputés distribués « les rémunérations et avantages occultes » (CGI 111 c) et toutes les sommes ou valeurs mises à la disposition des associés et non prélevées sur les bénéfices (CGI 109). [A6-16]
- **Acte anormal de gestion** : le BOFiP range expressément parmi les revenus distribués la « cession ou location aux associés de biens sociaux pour un prix inférieur à leur valeur vénale ». Conséquences : la renonciation à recette est réintégrée au résultat de la société et l'avantage est imposé chez l'associé. [A6-62b, BOFiP BOI-RPPM-RCM-10-20-20-10, PAGE LUE]
- **Avantage en nature logement d'un dirigeant** (président de SAS, assimilé salarié) : en principe évalué à sa valeur réelle. Depuis le 21/06/2024, cette valeur réelle est la **valeur locative cadastrale**, à laquelle s'ajoutent les avantages accessoires (eau, énergie, chauffage, garage) pour leur coût réel. [A6-63b, URSSAF, PAGE LUE]. Selon un extrait URSSAF non confirmé sur la page lue, l'évaluation forfaitaire ne serait ouverte qu'aux dirigeants qui cumulent régulièrement mandat social et contrat de travail [EXTRAIT].
- **Abus de biens sociaux** : 5 ans d'emprisonnement et 375 000 € d'amende pour le dirigeant qui fait de mauvaise foi des biens de la société un usage contraire à son intérêt, à des fins personnelles. La peine monte à 7 ans et 500 000 € en cas de comptes à l'étranger ou d'interposition étrangère. Texte : C. com. L.242-6 3°, rendu applicable à la SAS par L.244-1 ; pour la SARL, L.241-3 4°. [A6-04, A6-05, A6-06]
  - L'ABS ne s'applique pas aux sociétés civiles (SCI). D'autres qualifications restent possibles, comme l'abus de confiance (non vérifié ici).
- **Taxe holdings, CGI 235 ter C** (texte intégral lu) [A6-01] :
  - **Redevables** : sociétés françaises soumises à l'IS de plein droit ou sur option (et certaines sociétés étrangères).
  - **Trois conditions cumulatives, appréciées à la clôture de l'exercice** :
    1. valeur vénale de l'ensemble des actifs ≥ **5 M€** ;
    2. au moins une personne physique détient ≥ **50 %** des droits de vote ou financiers, ou exerce en fait le pouvoir de décision. Le conjoint ou partenaire, le concubin, les ascendants, les descendants et les frères et sœurs sont comptés comme **une seule personne** ;
    3. les **revenus passifs** (dividendes, intérêts, redevances, **loyers**, etc.) dépassent **50 %** des produits d'exploitation et financiers de l'exercice.
  - **Assiette** : valeur vénale à la clôture de la liste fermée de l'article. On y trouve notamment le 5° (« chevaux de course ou de concours ») et le **7° (« logements dont la personne physique se réserve la jouissance »)**, c'est-à-dire les logements occupés gratuitement ou pour un loyer inférieur au prix du marché, à titre de résidence principale ou non, et les logements loués fictivement.
  - **Dettes** : pour les seuls logements, les dettes d'acquisition sont déductibles. Celles contractées auprès de l'associé ou d'une société liée ne le sont pas, sauf preuve d'un objectif non principalement fiscal.
  - **Usage professionnel** : un actif n'est pas pris en compte dans la proportion où il est affecté à une activité industrielle, commerciale, agricole ou libérale de la société, d'une société liée ou de la personne physique.
  - **Taux de 20 %**. La taxe **n'est pas déductible de l'IS** (IX).
  - **Calendrier** : due au titre des exercices clos à compter du 31/12/2026.
  - **Coordination** avec l'IFI par CGI 975 VII.
  - **Commentaire BOFiP** : non trouvé. Un commentateur indiquait qu'il n'était pas publié en 04/2026. [INCONNU au 14/10/2026 ; à vérifier sur bofip.impots.gouv.fr]

### 3.2 Conséquences pratiques
**Exemple illustratif [ESTIMATION, chiffres fictifs].** Une PropCo à l'IS détient un domaine de 6 M€ d'actifs. Elle encaisse surtout le loyer de l'OpCo, ce qui la rend majoritairement passive. Le fondateur y occupe gratuitement un appartement privé valorisé 1,5 M€, et 0,9 M€ de dette d'acquisition se rattache à ce logement. Base taxable : 0,6 M€. Taxe : **120 000 € par an, non déductible**.

**Parades possibles, à valider** :
1. **Loyer de marché réel** pour le logement privé, avec un bail écrit et une expertise. Le logement sort alors du 7°. Le loyer devient en revanche un produit imposable à l'IS.
2. Détenir le **logement privé hors de toute société à l'IS** (en direct ou en SCI à l'IR).
3. **Faire détenir le château par la société opérationnelle elle-même.** Ses revenus d'activité sont actifs, donc la condition n° 3 tombe. Il reste la question de l'acte anormal de gestion et de l'avantage en nature pour le logement.
4. **Ne pas dépasser 5 M€ d'actifs** dans la société concernée.
5. Faire en sorte que des **investisseurs non familiaux détiennent la majorité**, sans contrôle de fait du fondateur.

**Valeur cadastrale et prix du marché ne coïncident pas.** Pour un château, l'avantage en nature calculé sur la valeur locative cadastrale est probablement très inférieur au loyer de marché **[ESTIMATION]**. Déclarer un avantage en nature à la valeur cadastrale ne protège donc pas de la taxe 235 ter C, qui vise tout loyer « inférieur au prix du marché ». Ce point est à confirmer quand le BOFiP sera publié.

**Chevaux du fondateur** : des chevaux de concours logés dans une holding et montés à titre privé sont taxables à 20 % par an. S'ils servent à l'activité équestre (école, commerce, valorisation), ils sont exclus au prorata de cet usage.

### 3.3 Risques
- Redressement d'IS et imposition d'un revenu distribué chez l'associé (au PFU de 31,4 % [EXTRAIT] ou au barème de l'IR).
- Pénal (ABS) si des minoritaires ou des créanciers sont lésés.
- Taxe de 20 % par an.

**À valider par** : avocat fiscaliste (qualification et valeur de marché), expert immobilier agréé (loyer de marché), expert-comptable et commissaire aux comptes s'il y en a un.

---

## 4. Conventions réglementées

### 4.1 Règles
- **SAS, C. com. L.227-10.** Le commissaire aux comptes, ou à défaut le président, présente aux associés un rapport sur les conventions conclues entre la société et son président, un dirigeant, un actionnaire détenant plus de 10 % des droits de vote, ou la société qui contrôle un actionnaire personne morale. Les associés statuent sur ce rapport.
  - Une convention non approuvée produit quand même ses effets, mais la personne intéressée en supporte les conséquences dommageables.
  - Dans une SAS à associé unique, une simple mention au registre des décisions suffit.
  - Ces règles ne s'appliquent pas aux opérations courantes conclues à des conditions normales (L.227-11). [A6-07, A6-08]
- **SARL, L.223-19** : rapport du gérant ou du commissaire aux comptes, et l'associé intéressé ne prend pas part au vote. [A6-09]

### 4.2 Conséquences pratiques
Il faut documenter avec des comparables ou une expertise toutes les conventions intra-groupe :
- bail ou mise à disposition PropCo vers OpCo ;
- logement du fondateur ;
- comptes courants ;
- management fees de la holding ;
- convention de trésorerie ;
- vente ou location des chevaux du fondateur à l'OpCo ;
- prestations croisées entre l'équestre et l'événementiel.

Dès l'arrivée d'investisseurs, il est conseillé de **prévoir dans les statuts de la SAS une autorisation préalable** de ces conventions.

### 4.3 Risque
Responsabilité du dirigeant, conflit avec les minoritaires et, en cas d'abus, ABS. Un loyer intra-groupe sous le marché constitue un acte anormal pour le bailleur ; au-dessus du marché, pour le preneur.

**À valider par** : avocat en droit des sociétés, commissaire aux comptes.

---

## 5. Monuments historiques

### 5.1 Règles
- **Immeuble classé** (C. patrimoine L.621-9) :
  - aucune restauration, réparation ou modification sans autorisation ; les travaux sont exécutés sous contrôle scientifique et technique de l'État ;
  - la maîtrise d'œuvre de restauration revient à un **architecte en chef des monuments historiques** ou à un architecte de l'UE ou de l'EEE remplissant les conditions requises (R.621-28). [A6-20, A6-25]
- **Immeuble inscrit** (L.621-27) :
  - déclaration **4 mois avant** tous travaux ;
  - si les travaux sont soumis à permis ou à déclaration préalable, l'autorisation exige l'accord de l'autorité chargée des monuments historiques ;
  - l'administration ne peut s'opposer aux autres travaux qu'en engageant un classement. [A6-21]
- **Maître d'ouvrage** : c'est le propriétaire. L'État peut l'assister gratuitement s'il manque de ressources (L.621-29-2). [A6-22]
- **Abords** : la protection couvre, en l'absence de périmètre délimité, tout immeuble **visible du monument ou visible en même temps que lui, dans un rayon de 500 m** (L.621-30). Les travaux qui modifient l'aspect extérieur sont soumis à autorisation préalable, avec avis ou accord de l'ABF selon les régimes (L.621-32). Dans les abords, même les petites constructions de 20 m² ou moins sont soumises à déclaration préalable (C. urb. R.421-11). [A6-23, A6-24, A6-36b]
- **Subventions de l'État** (page nationale du ministère de la Culture) :
  - taux indicatifs de **40 % pour un immeuble classé** et **20 % pour un inscrit** ;
  - plafond légal de 40 % de la dépense pour un inscrit (L.621-29, cité par la page du ministère, article non lu) ;
  - les travaux de confort, d'accessibilité et de mise aux normes ne sont pas éligibles ;
  - l'aide dépend des crédits disponibles et n'est pas versée de plein droit. [A6-26, PAGE LUE]
- **Impôt sur le revenu** :
  - **Déficits** : l'imputation exclusive des déficits fonciers sur les revenus fonciers ne s'applique pas aux propriétaires de monuments classés ou inscrits (CGI 156 I 3°). Les charges foncières des monuments sont déductibles du revenu global (156 II 1° ter). [A6-27]
  - **Conditions (156 bis)** : engagement de **conserver 15 ans**. Le régime est fermé aux sociétés civiles non soumises à l'IS, sauf trois cas : affectation de 75 % des surfaces à l'habitation dans les 2 ans, espace culturel non commercial ouvert 15 ans pour un monument classé, ou associés d'une même famille. Il est aussi fermé en cas de division intervenue depuis 2009, sauf affectation de 75 % à l'habitation. [A6-28]
  - **Taux de déduction** (BOFiP) : 100 % des charges si le public est admis à visiter, 50 % si l'immeuble est fermé (immeuble sans recettes). Un château qui n'ouvre au public que ses extérieurs ne déduit que 50 %. [A6-29, BOI-RFPI-SPEC-30-20-20, PAGE LUE]
  - **Définition de l'ouverture** (ann. IV CGI art. 17 ter) : **50 jours par an, dont 25 jours non ouvrables, d'avril à septembre**, ou **40 jours en juillet, août et septembre**, avec un accès effectif d'au moins **6 heures** par jour. Une réduction de 10 jours au plus est possible grâce à des conventions de visites scolaires. [A6-29b, BOI-RFPI-SPEC-30-20-10, PAGE LUE]
- **Transmission, CGI 795 A** : exonération des droits de mutation à titre gratuit pour les immeubles classés ou inscrits et les meubles qui en sont le complément.
  - Contrepartie : une convention à durée indéterminée signée avec l'État, qui fixe les modalités d'accès du public et d'entretien. En cas de non-respect, les droits sont rappelés.
  - Le régime s'étend aux parts de SCI familiales à l'IR, sous conditions : détention de plus de 2 ans, conservation 5 ans, adhésion à la convention. [A6-11]

### 5.2 Conséquences pratiques
- Le régime monuments historiques ne vaut que pour une détention à l'**IR** : en direct, en SCI familiale, ou en SCI non familiale affectée à 75 % à l'habitation. Il ne s'applique pas à une société à l'IS, qui déduit ses charges de droit commun.
- Ce régime entre donc en tension avec les montages en société à l'IS. Il est en revanche cohérent avec une SCI à l'IR qui détient la partie privée.
- L'ouverture au public (50 jours) a un coût d'organisation et de sécurité : le château devient un ERP pendant les visites (§ 7). C'est aussi une source de recettes.

### 5.3 Risques
- Délais d'autorisation et surcoûts liés au maître d'œuvre spécialisé et aux prescriptions de l'ABF.
- Subvention refusée ou différée.
- Rappel d'impôt majoré du tiers des charges déduites en cas de rupture de l'engagement de 15 ans (156 bis III).
- Travaux non autorisés : infraction pénale, non détaillée ici.

**À valider par** : DRAC / CRMH et UDAP (ABF) du département, architecte du patrimoine, notaire et avocat fiscaliste pour la convention 795 A.

---

## 6. Urbanisme

### 6.1 Règles
- **Zones A et N** : le règlement du PLU peut **désigner les bâtiments** qui peuvent changer de destination, si ce changement ne compromet ni l'activité agricole ni la qualité paysagère. Le changement est soumis à l'**avis conforme de la CDPENAF en zone A** et à celui de la **commission départementale de la nature, des paysages et des sites (CDNPS) en zone N** (C. urb. L.151-11 I 2°). [A6-33b]
- **STECAL** (L.151-13) : secteurs « à titre exceptionnel » où des constructions sont permises, délimités après avis de la CDPENAF. [A6-34]
- **Constructions autorisées en zone A** : celles « nécessaires à l'exploitation agricole », ainsi que les changements de destination, extensions et annexes prévus par L.151-11 à L.151-13 (R.151-23). [A6-35]
- **Permis de construire** :
  - obligatoire pour les constructions nouvelles, hors cas de dispense ou de déclaration préalable (R.421-1) ;
  - obligatoire sur l'existant au-delà de 20 m² créés (40 m² en zone U), ou en cas de changement de destination avec modification des structures porteuses ou de la façade (R.421-14) ;
  - le changement de destination sans travaux lourds relève de la déclaration préalable (R.421-17 b). [A6-36, A6-36c, A6-37]
- **Recours à l'architecte** : non obligatoire pour une exploitation agricole qui construit pour elle-même un bâtiment agricole dont la surface de plancher **et** l'emprise au sol ne dépassent pas **800 m²**. Pour un usage non agricole, la limite est de 150 m² (R.431-2). [A6-39]

### 6.2 Conséquences pratiques
- **Manège** : la surface d'un manège dépasse en pratique 800 m², ce qui rend l'**architecte obligatoire** **[ESTIMATION sur les dimensions usuelles ; INCONNU pour le projet]**. En zone A, il faut démontrer que le manège est « nécessaire à l'exploitation agricole » (activité équestre agricole réelle au sens de L.311-1). Sinon, il faut un STECAL ou une modification du PLU.
- **Transformation d'écuries ou de granges en gîtes ou en salle de réception** : le bâtiment doit être désigné au PLU, puis obtenir un avis conforme de la CDPENAF ou de la CDNPS. S'y ajoute l'ABF en abords. **Ces points doivent être vérifiés avant toute offre d'achat** : il faut demander un certificat d'urbanisme et lire le règlement de zone.
- Le changement de destination crée aussi les obligations ERP (§ 7).

### 6.3 Risques
- Refus de la CDPENAF : le business plan événementiel ou d'hébergement devient irréalisable.
- Contentieux de tiers.
- Délais : CDPENAF, ABF et, le cas échéant, modification du PLU.

**À valider par** : service urbanisme de la mairie ou de l'intercommunalité (PLU, certificat d'urbanisme opérationnel), DDT(M) et secrétariat de la CDPENAF, UDAP (ABF), architecte.

---

## 7. ERP, chambres d'hôtes et meublés

### 7.1 Règles
- **Catégories d'ERP** (CCH R.143-19) :

| Catégorie | Effectif |
|---|---|
| 1re | plus de 1 500 personnes |
| 2e | 701 à 1 500 |
| 3e | 301 à 700 |
| 4e | 300 et moins |
| 5e | en dessous du seuil propre à chaque type |

  [A6-50b, PAGE LUE (miroir)]
- **Seuils de la 5e catégorie par type** (règlement de sécurité du 25/06/1980, repris par entreprendre.service-public.fr) [A6-51, PAGE LUE] :

| Type | Seuil 5e catégorie |
|---|---|
| **L** salle polyvalente ou de réunion | 200 personnes au total (100 en sous-sol) |
| L spectacle | 50 personnes |
| N restaurant | 200 personnes |
| **O** hôtel | 100 personnes |
| R avec locaux de sommeil | 30 personnes |
| X établissement sportif couvert (un manège recevant du public en relèverait a priori **[ESTIMATION]**) | 200 personnes |
| Y musée | 200 personnes |
| **PA** plein air | **300 personnes** |
| **CTS** chapiteau ou tente | **50 personnes** |

  - Un **gîte** est un ERP au-delà de **15 couchages** ou s'il accueille plus de 7 mineurs sans leur famille. [A6-51]
- **Chambres d'hôtes** : chambres meublées chez l'habitant, avec prestations (C. tourisme L.324-3). L'activité est limitée à **5 chambres et 15 personnes**, couvre la nuitée et le petit-déjeuner, et l'accueil est assuré par l'habitant (D.324-13). Une déclaration préalable en mairie est obligatoire (L.324-4). [A6-52, A6-53, A6-54]
- **Meublés de tourisme** : déclaration soumise à **enregistrement via un téléservice national**. Fausse déclaration : jusqu'à 20 000 € d'amende (L.324-1-1). [A6-62]
- **Micro-BIC** (CGI 50-0) [A6-63] :

| Activité | Plafond de chiffre d'affaires | Abattement |
|---|---|---|
| Fourniture de logement (hors meublés) | 203 100 € | 71 % |
| Meublés de tourisme non classés | 15 000 € | 30 % |
| Autres entreprises | 83 600 € | 50 % |

  - Le rattachement exact des chambres d'hôtes et des meublés classés à l'une de ces catégories est **à valider** (BOI-BIC-DECLA, non lu).

### 7.2 Conséquences pratiques
- Au-delà de 5 chambres ou 15 personnes, on sort du statut de chambres d'hôtes pour entrer dans l'**hôtellerie**, ERP de type O.
- Une grange de réception de type L accueillant 200 à 300 personnes est un ERP de 4e catégorie, et de 3e catégorie au-delà de 300 : passage en commission de sécurité et règles plus lourdes.
- Un concours sous tente de plus de 50 personnes relève du type CTS.
- Chambres d'hôtes de la catégorie « fourniture de logement » au micro : régime simple jusqu'à 203 100 € de chiffre d'affaires. **[ESTIMATION à confirmer]**

### 7.3 Risques
- Fermeture administrative et responsabilité pénale en cas d'accident.
- Coûts de mise en conformité incendie et accessibilité, d'autant plus difficile sur un bâtiment monument historique.

**À valider par** : SDIS et commission de sécurité via la préfecture ou la mairie, bureau de contrôle agréé, mairie (déclarations), expert-comptable.

---

## 8. Événementiel : débits de boissons et bruit

### 8.1 Règles
- **Licences** :
  - **licence de 3e catégorie** dite restreinte : boissons des groupes 1 et 3 ; **licence de 4e catégorie** : toutes boissons autorisées (CSP L.3331-1) ;
  - restaurants : « petite licence restaurant » ou « licence restaurant », valables seulement pendant les repas (L.3331-2) ;
  - **permis d'exploitation** obligatoire, obtenu par une formation agréée et valable 10 ans. Une version adaptée existe pour les loueurs de chambres d'hôtes (L.3332-1-1). [A6-64, A6-65, A6-66]
- **Débits temporaires** (fêtes, foires) : autorisation du maire, avec limitation aux groupes 1 et 3. Les associations ont droit à 5 autorisations par an (L.3334-2). [A6-67]
- **Sons amplifiés** (décret n° 2017-1244, CSP R.1336-1) : dans les lieux recevant du public où le niveau dépasse 80 dB(A) équivalents sur 8 h, il faut :
  - ne jamais dépasser **102 dB(A) et 118 dB(C) sur 15 minutes** ;
  - enregistrer et afficher les niveaux lorsque la capacité dépasse 300 personnes ;
  - informer le public, fournir gratuitement des protections et prévoir des zones de repos, en cas de diffusion habituelle. [A6-68]
- **Voisinage** :
  - **émergence globale** maximale de **5 dB(A) le jour (7 h-22 h) et 3 dB(A) la nuit**, plus un terme correctif selon la durée (CSP R.1336-7) ;
  - dans un lieu clos diffusant à titre habituel : émergence de 3 dB(A) au plus et de 3 dB par octave (125-4 000 Hz) dans les logements voisins (C. env. R.571-26) ;
  - **étude de l'impact des nuisances sonores** obligatoire (R.571-27). [A6-69, A6-69b]

### 8.2 Conséquences pratiques
- Pour les mariages et séminaires, le plus simple est de faire servir les boissons par un traiteur titulaire d'une licence restaurant. Ce montage reste **à valider**.
- La vente d'alcool par l'exploitant du lieu exige une licence et un permis d'exploitation. Les licences IV sont rares et leur transfert est encadré : article L.3332-2 non lu, **[INCONNU]**.
- Une orangerie ou une grange utilisée « à titre habituel » pour des soirées amplifiées impose une étude d'impact, voire des limiteurs.

### 8.3 Risques
Plaintes du voisinage, fermeture administrative, amendes, et dégradation de la valeur résidentielle du domaine, ce qui contredit l'objectif d'un cadre de vie privé.

**À valider par** : mairie et préfecture (licences, arrêtés), acousticien (étude d'impact), avocat.

---

## 9. Réglementation équestre et bail rural

### 9.1 Règles
- **Caractère agricole** : sont réputées agricoles « les activités de préparation et d'entraînement des équidés domestiques en vue de leur exploitation, à l'exclusion des activités de spectacle ». Ces activités sont civiles (C. rural L.311-1). Le CGI les rattache aux bénéfices agricoles (art. 63). [A6-40, A6-40b]
- **MSA** : affiliation des « exploitations de dressage, d'entraînement, haras » (L.722-1 1°) dès lors que l'activité minimale d'assujettissement est atteinte (L.722-5, version au 01/01/2026). [A6-86, A6-87]
- **Identification et traçabilité (SIRE)** :
  - tout changement de propriétaire ou de détenteur d'un équidé est déclaré à l'IFCE, et les détenteurs s'enregistrent auprès de lui (L.212-9) ;
  - carte d'immatriculation, mises à jour sous 30 jours (D.212-50) [A6-84, A6-85] ;
  - **lieu de détention** à déclarer, **registre d'élevage**, **vétérinaire sanitaire** obligatoire à partir de 3 équidés, mouvements de plus de 30 jours à déclarer sous 7 jours. [EXTRAIT, IFCE inaccessible, A6-85b]
- **Bien-être animal** : tout détenteur d'équidé atteste de sa connaissance des besoins de l'espèce. Un non-professionnel signe un **certificat d'engagement et de connaissance**. Le propriétaire doit s'en assurer avant tout changement de détenteur (L.211-10-1, loi n° 2021-1539). [A6-88]
- **ICPE** : la nomenclature (annexe de C. env. R.511-9) ne contient **pas de rubrique équidés**. Je n'ai trouvé les équidés que dans une note de la rubrique « chiens » **[PAGE LUE (miroir), recherche textuelle, A6-91]**. Les écuries relèvent alors a priori du **règlement sanitaire départemental** (distances, fumières) **[INCONNU sur le contenu : à vérifier auprès de la DDPP ou de l'ARS du département]**.
- **TVA** (BOFiP BOI-TVA-SECT-80-10-30-50, version du 25/03/2026) [A6-81, PAGE LUE] :
  - **5,5 %**, depuis le 01/01/2024, pour l'enseignement et la pratique de l'équitation, les animations et démonstrations, et l'accès aux installations sportives (manèges, carrières, parcours, écuries) (CGI 278-0 bis O) ;
  - 5,5 % aussi pour la **pension liée à la pratique de l'équitation**, lorsqu'elle n'est pas contractuellement dissociable ;
  - **20 %** pour l'entraînement, le dressage, la pension « de valorisation » commerciale et la **location de boxes sans entretien**, qui n'est pas une activité agricole ;
  - cours donnés par une personne physique rémunérée directement par ses élèves, sans salariés : **exonérés** (CGI 261-4-4° b).
- **Enseignement contre rémunération** : il faut détenir un diplôme, un titre ou un certificat de qualification professionnelle enregistré au RNCP, qui garantit la sécurité (C. sport L.212-1). Sanction : **1 an d'emprisonnement et 15 000 €**, y compris pour l'employeur (L.212-8). [A6-82, A6-83]
- **Contrôle des structures agricoles** : une autorisation préalable d'exploiter est requise au-delà du seuil fixé par le schéma directeur régional (SDREA). Elle est requise **quelle que soit la surface** dans trois cas :
  - l'exploitant n'a pas la capacité ou l'expérience professionnelle exigée ;
  - aucun membre n'a la qualité d'exploitant ;
  - l'exploitant est **pluriactif avec des revenus extra-agricoles supérieurs à 3 120 fois le SMIC horaire** (C. rural L.331-2). [A6-89]
- **Bail rural** :
  - **toute mise à disposition à titre onéreux d'un immeuble à usage agricole pour y exercer une activité de L.311-1 relève du statut, qui est d'ordre public**. Le statut couvre aussi les contrats de prise en pension d'animaux qui transfèrent au propriétaire des animaux les obligations du propriétaire du fonds (L.411-1) [A6-41] ;
  - **exceptions** (L.411-2) : conventions d'occupation précaire en nombre limité, entretien des terrains attenants à une habitation, et biens mis à la disposition d'une société par une personne qui participe effectivement à l'exploitation [A6-42] ;
  - **doctrine** : depuis 2005, l'exploitation d'un centre équestre est agricole, ce qui fait entrer sa mise à disposition dans le statut du fermage (bail de 9 ans renouvelable, éviction très limitée, fermage plafonné par arrêté préfectoral). La **pension « pure »** (litière, nourriture, surveillance) n'est pas agricole. [A6-90, Eurojuris, avocat, PAGE LUE, source secondaire]

### 9.2 Conséquences pratiques
- **Louer les écuries et les herbages à un cavalier professionnel ou à un enseignant, contre un loyer, crée très probablement un bail rural.** Celui-ci prime sur la jouissance du propriétaire pendant 9 ans ou plus.
- Une OpCo équestre détenue par le fondateur limite le risque, mais pas pour toujours : cession de l'OpCo, entrée d'investisseurs, divorce.
- **Alternatives à valider** :
  - exploitation directe par le propriétaire ;
  - convention de mise à disposition SAFER (L.142-6, non lu) ;
  - contrats de **prestation** (pension), sans mise à disposition du foncier ;
  - à l'inverse, recherche volontaire du **bail à long terme** pour bénéficier des exonérations d'IFI et de droits de mutation (CGI 793 2 3°, 976 III).
- Le fondateur est un **entrepreneur pluriactif, probablement à hauts revenus**. Exploiter lui-même 50 ha déclencherait vraisemblablement le **contrôle des structures**, avec une autorisation préfectorale à obtenir. **[ESTIMATION à partir de L.331-2 ; seuils régionaux INCONNUS]**
- **Le modèle financier doit distinguer les taux de TVA** : 5,5 % pour les cours, la pension avec pratique et l'accès aux installations ; 20 % pour la valorisation, le commerce de chevaux et la location de boxes nus.

### 9.3 Risques
- Bail rural non voulu.
- Enseignement sans diplôme.
- Absence de déclaration du lieu de détention (contravention de 5e classe, EXTRAIT).
- TVA appliquée à 5,5 % au lieu de 20 %, ce qui entraîne un rappel.
- Affiliation MSA ou autorisation d'exploiter oubliée.

**À valider par** : avocat en droit rural, chambre d'agriculture et DDT (contrôle des structures), MSA, IFCE / SIRE, expert-comptable agricole (TVA, bénéfices agricoles), DDPP (sanitaire).

---

## 10. SAFER et loi Sempastous

### 10.1 Règles
- **Champ de la préemption** (L.143-1) : aliénations à titre onéreux de biens à usage agricole et de terrains à vocation agricole (zones A et N d'un PLU, zone agricole protégée, etc.). La préemption peut aussi viser :
  - les bâtiments d'habitation faisant partie d'une exploitation ;
  - certains bâtiments ayant servi à une activité agricole dans les 10 dernières années ;
  - l'usufruit ou la nue-propriété ;
  - la **totalité** des parts d'une société agricole, si le but est d'installer un agriculteur.
  - Article dans sa version du 20/08/2026. [A6-43]
- **Préemption partielle** (L.143-1-1). Le vendeur peut alors exiger que la SAFER achète l'ensemble, ou se faire indemniser. [A6-44]
- **Révision du prix** : la SAFER peut faire une offre à ses propres conditions (L.143-10). [A6-45]
- **Exemptions** (L.143-4) : cessions entre parents jusqu'au 4e degré, entre cohéritiers, terrains destinés à la construction, parcelles boisées sous conditions, etc. La SAFER ne peut pas préempter contre un preneur en place depuis plus de 3 ans (L.143-6). [A6-46]
- **Information obligatoire** (L.141-1-1) : la SAFER est informée par le notaire, ou **par le cédant ou le cessionnaire pour une cession de parts**, de toute cession portant sur les biens de son ressort.
  - Le nouveau **I bis** impose une notification séparée pour les biens préemptables et non préemptables non contigus. Il **ne s'applique pas aux monuments historiques** classés ou inscrits et aux terrains qui forment avec eux un ensemble cohérent.
  - Sanctions : annulation demandée en justice, ou amende allant jusqu'à **2 % du montant de la transaction**. [A6-47b]
- **Baux emphytéotiques** (L.451-1-1, créé par la loi n° 2026-796) : information de la SAFER au moins **2 mois avant**, à peine de nullité, et **droit d'opposition** de la SAFER. [A6-47]
- **Loi Sempastous** (L.333-2 et L.333-3) :
  - toute prise de contrôle d'une société qui possède ou exploite des terres agricoles est soumise à l'**autorisation préalable du préfet**, instruite par la SAFER, lorsque l'acquéreur dépasse le **seuil d'agrandissement significatif** ;
  - ce seuil est fixé par le préfet de région entre **1,5 et 3 fois la surface agricole utile régionale moyenne** ; les bois sont exclus ;
  - une opération réalisée sans autorisation est **nulle**, avec une amende allant jusqu'à 2 % ;
  - les cessions familiales sont exemptées sous engagement de 9 ans. [A6-48, A6-49]

### 10.2 Conséquences pratiques
- Lors de l'achat d'un château avec plus de 50 ha, la SAFER peut **préempter les terres** et laisser le château à l'acheteur. Cela met en péril l'objectif de 50 ha pour les chevaux.
- Parades à étudier :
  - se porter **candidat à la rétrocession SAFER** avec un projet agricole équestre crédible ;
  - prévoir une structuration de l'acte permettant au vendeur d'exiger une préemption totale ;
  - dans le cas d'un monument historique, le nouveau I bis évite la notification fractionnée.
- Racheter une société propriétaire n'échappe ni à l'information SAFER ni, au-delà du seuil, à la loi Sempastous.

### 10.3 Risques
Perte des terres, révision du prix, nullité ou amende pour défaut de notification, et délais.

**À valider par** : notaire, SAFER régionale (en tant que candidat, pas de contact à ce stade), avocat en droit rural.

---

## 11. Levée de fonds

### 11.1 Règles
- **Interdiction de principe** : les personnes ou entités non autorisées ne peuvent pas faire d'**offre au public de titres financiers ou de parts sociales**, à peine de **nullité des contrats ou des titres** (CMF L.411-1). [A6-70]
- **Offres autorisées par dérogation** (L.411-2) :
  1. offre réservée à des **investisseurs qualifiés** ou à un **cercle restreint de moins de 150 personnes** agissant pour compte propre (le seuil de 150 est fixé par D.411-4) ;
  2. offre par un **prestataire de services de financement participatif** (PSFP, règlement (UE) 2020/1503) dans la limite du seuil de ce règlement ;
  3. offre réservée aux associés existants. [A6-71, A6-71b]
- **SAS** : interdiction de l'offre au public, sauf ces offres dispensées (C. com. L.227-2). [A6-10b]
- **Seuils (AMF)** :
  - plafond du financement participatif PSFP : **5 M€ sur 12 mois par porteur de projet** ;
  - prospectus exigé à partir de **8 M€** sur 12 mois, en France.
  - Ces deux chiffres sont des **EXTRAITS** : le site de l'AMF était inaccessible. [A6-72, A6-72b]
- **Démarchage** : toute prise de contact non sollicitée, ou toute visite à domicile, en vue de faire souscrire des instruments financiers, des opérations sur biens divers ou un financement participatif est réservée aux personnes habilitées (L.341-1). [A6-73]
- **Biens divers** : sont intermédiaires en biens divers ceux qui proposent d'acquérir des droits sur des biens dont les acquéreurs n'assurent pas la gestion, ou en **mettant en avant un rendement financier**. Ils sont soumis au contrôle de l'AMF (L.551-1, version au 01/07/2026). Cela vise par exemple des parts de chevaux ou des nuitées « investissement ». [A6-74]
- **FIA** : un véhicule qui lève des capitaux auprès de plusieurs investisseurs pour les investir dans leur intérêt, selon une politique d'investissement définie, est un FIA. Il est soumis au régime des sociétés de gestion (L.214-24). [A6-75]
- **Crédit-vendeur** :
  - depuis le 01/01/2022, le « privilège du vendeur » est remplacé par l'**hypothèque légale spéciale** qui garantit le prix de vente d'un immeuble (C. civ. 2402 1°) ;
  - le vendeur impayé peut demander la **résolution de la vente** (C. civ. 1654) ;
  - les formalités de publicité foncière n'ont pas été vérifiées. [A6-76, A6-77]
- **IR-PME**, pour les investisseurs de l'OpCo : réduction d'impôt de **18 %** (CGI 199 terdecies-0 A, version du 21/02/2026). Les activités immobilières et les sociétés dont l'actif est principalement composé de **chevaux de course ou de concours** sont exclues. [A6-78]

### 11.2 Conséquences pratiques
- **Club deal licite** : quelques dizaines d'investisseurs connus, sollicités par le fondateur sans démarchage organisé, qui souscrivent dans une SAS. Pacte d'associés à prévoir :
  - gouvernance ;
  - usage privé du château, avec un loyer de marché pour éviter 235 ter C et l'ABS ;
  - liquidité, préemption, clauses de sortie conjointe (tag) et forcée (drag) ;
  - valorisation.
- **Pas de promesse de rendement chiffrée dans la communication.** Au-delà, il faut passer par un PSFP agréé.
- Le crédit-vendeur est un levier compatible avec un apport limité. Il est garanti par l'hypothèque légale et peut se négocier comme une alternative à la banque.

### 11.3 Risques
Nullité des souscriptions, sanctions de l'AMF, requalification en FIA ou en biens divers, et litiges entre associés.

**À valider par** : avocat en droit financier, PSFP agréé (si financement participatif), notaire (crédit-vendeur), AMF (demande de position, si doute).

---

## 12. Fiscalité

### 12.1 Règles
- **Impôt sur les sociétés** (CGI 219) :
  - taux normal de 25 % ;
  - **15 % jusqu'à 42 500 €** de bénéfice si le chiffre d'affaires ne dépasse pas 10 M€ et si le capital est entièrement libéré et détenu à 75 % au moins par des personnes physiques (ou par une société remplissant les mêmes conditions) ;
  - pour un groupe intégré, le chiffre d'affaires s'apprécie en additionnant celui des membres.
  - Exemple pour 100 000 € de bénéfice : **20 750 € d'IS** **[ESTIMATION, calcul]**. [A6-10]
- **Droits de mutation à titre onéreux** :
  - **Taux départemental** : 3,80 % de droit commun, avec un plafond normal de 4,50 % (CGI 1594 D) [A6-30]. La LF 2025 permet de monter jusqu'à **5 %** pour les actes passés **du 01/04/2025 au 31/03/2028**.
  - **Situation au 01/06/2026** : **88 départements à 5 %**, **seule l'Indre est restée à 3,80 %**, tous les autres appliquent au moins 4,50 %. La majoration ne s'applique pas à la première acquisition de la résidence principale. [A6-31 collectivites-locales.gouv.fr ; A6-32 Weblex citant la liste de la DGFiP, PAGE LUE]
  - **Taxes additionnelles** : taxe communale de 1,20 % (CGI 1584 / 1595 bis), plus **frais d'assiette de 2,37 %** calculés sur la part départementale (1647 V a). [A6-30b, A6-30c]
  - **Total, hors émoluments du notaire [ESTIMATION, calcul]** :

| Taux départemental | Taux total | Pour un prix de 3 M€ |
|---|---|---|
| 5 % | **6,3185 %** | 189 555 € |
| 4,50 % | 5,80665 % | 174 200 € |
| 3,80 % (Indre) | 5,09 % | 152 702 € |

  - **Le taux propre à chaque département est INCONNU dans ce document.** La table officielle est publiée sur impots.gouv.fr/droits-denregistrement, site « en maintenance » le 14/10/2026. Il faut la consulter dès que la région cible est connue.
- **Cession de droits sociaux** (CGI 726) :
  - **0,1 %** pour les actions de sociétés par actions non cotées (SAS) ;
  - **3 %** pour les parts sociales, après un abattement de 23 000 € réparti au prorata des parts ;
  - **5 %** pour les **sociétés à prépondérance immobilière**, assis sur le prix des titres, donc sur la valeur nette de dettes. [A6-33]
- **IFI** :
  - assujettissement au-delà de **1,3 M€** d'actifs immobiliers nets ; barème de 0,50 % à **1,50 %** (CGI 964, 977) ;
  - **abattement de 30 % sur la résidence principale** détenue directement (973) ;
  - exonération des biens professionnels (973, 975) ;
  - exonération de 75 % pour les bois et forêts et les groupements forestiers ; exonération totale ou partielle pour les biens ruraux loués par bail à long terme et les parts de GFA, sous conditions (976). [A6-12, A6-12b, A6-12c]
- **Régime mère-fille** (CGI 145, 216) : détention d'au moins 5 % du capital pendant 2 ans. Quote-part de frais et charges de **5 %**, ramenée à 1 % dans certains cas (groupes intégrés, etc.). [A6-34b]
- **Intégration fiscale** (CGI 223 A) : détention d'au moins **95 %**. Elle devient incompatible avec des investisseurs minoritaires au-delà de 5 % dans la filiale. [A6-35b]
- **Dutreil 2026** (CGI 787 B) : exonération de 75 % avec engagement collectif d'au moins 2 ans, **engagement individuel de 6 ans** et fonction de direction pendant 3 ans. Les **logements et résidences** et les **chevaux de course ou de concours** sont exclus, sauf affectation exclusive à l'activité. Une holding animatrice reste éligible. [A6-02]
- **Apport-cession** (150-0 B ter) : voir § 1.1. [A6-17]
- **Prélèvements sociaux et PFU 2026** : **31,4 %** (12,8 % d'impôt plus 18,6 % de prélèvements) sur les dividendes et les plus-values mobilières. **[EXTRAIT, A6-95]**

### 12.2 Conséquences pratiques
- **Achat des murs ou rachat de la société (share deal)** : racheter une société à prépondérance immobilière coûte 5 % sur la valeur des titres, contre environ 6,3 % sur le prix de l'immeuble. Mais l'acheteur hérite des plus-values latentes et du passif de la société. **[ESTIMATION]**
- **Arrivée d'investisseurs** : des investisseurs personnes morales qui feraient passer la part des personnes physiques sous 75 % font perdre le taux de 15 % à l'OpCo. Au-delà de 5 % de minoritaires, l'intégration fiscale est impossible.
- **Transmission** : plusieurs régimes se combinent (Dutreil pour les OpCo, 795 A pour un monument historique ouvert au public, 793 pour un GFA ou un groupement forestier). Le logement privé ne bénéficie ni du Dutreil ni, hors convention monument historique, d'un autre régime de faveur.

**À valider par** : notaire (DMTO du département, share deal), avocat fiscaliste (IFI, Dutreil, intégration), expert-comptable.

---

## 13. Tableau des 10 risques majeurs

| # | Risque | Mécanisme et source | Probabilité [ESTIMATION] | Impact | Parade principale | À valider par |
|---|---|---|---|---|---|---|
| 1 | **Taxe de 20 % par an sur le logement privé** du fondateur dans une société à l'IS | CGI 235 ter C I et II 7° ; exercices clos à partir du 31/12/2026 [A6-01] | Élevée si PropCo à l'IS ≥ 5 M€ et majoritairement passive | Très élevé (20 % de la valeur nette de dettes, chaque année, non déductible) | Logement privé hors IS (direct ou SCI à l'IR), ou loyer de marché documenté ; société détenant le château majoritairement opérationnelle | Avocat fiscaliste, expert immobilier |
| 2 | **Requalification en bail rural** des écuries ou terres mises à disposition d'un exploitant équestre, OpCo comprise | C. rural L.311-1, L.411-1 (ordre public) [A6-40, A6-41, A6-90] | Moyenne à élevée | Élevé (perte de maîtrise 9 ans et plus, fermage plafonné, droits du preneur) | Exploitation directe, contrats de prestation, convention SAFER, ou bail à long terme assumé (exonérations) | Avocat en droit rural |
| 3 | **Préemption SAFER** des terres (partielle, révision du prix) ou opposition sur un bail emphytéotique ; autorisation Sempastous | L.143-1, L.143-1-1, L.143-10, L.451-1-1 (2026), L.333-2 [A6-43 à A6-49] | Moyenne (selon le territoire) | Élevé (objectif de 50 ha compromis) | Candidature à la rétrocession avec un projet agricole équestre ; structuration de l'acte ; calendrier | Notaire, avocat en droit rural |
| 4 | **Acte anormal de gestion, revenu distribué, ABS** liés à l'usage privé du château ou à des conventions hors marché | CGI 109 et 111 c ; BOFiP RPPM-RCM-10-20-20-10 ; C. com. L.242-6, L.244-1, L.227-10 [A6-16, A6-62b, A6-04 à A6-08] | Moyenne (forte si investisseurs minoritaires) | Élevé (redressements, pénal 5 ans / 375 k€) | Loyers et conventions au prix du marché, rapport L.227-10, pacte d'associés | Avocat fiscaliste et sociétés, commissaire aux comptes |
| 5 | **Levée de fonds irrégulière** : offre au public, démarchage, biens divers, FIA | CMF L.411-1, L.411-2, L.341-1, L.551-1, L.214-24 ; C. com. L.227-2 [A6-70 à A6-75] | Moyenne (tentation du crowdfunding « maison ») | Élevé (nullité des souscriptions, AMF) | Cercle restreint de moins de 150 personnes ou investisseurs qualifiés ; PSFP agréé ; aucune promesse de rendement | Avocat en droit financier |
| 6 | **Blocage d'urbanisme** : changement de destination refusé par la CDPENAF ou la CDNPS, manège non « nécessaire » en zone A, prescriptions ABF | C. urb. L.151-11, L.151-13, R.151-23, R.431-2 ; C. patrimoine L.621-30 et L.621-32 [A6-33b à A6-39, A6-23, A6-24] | Moyenne | Élevé (activités de réception ou d'hébergement impossibles) | Certificat d'urbanisme et lecture du PLU **avant l'offre** ; consultation de l'UDAP | Mairie, DDT(M), UDAP, architecte |
| 7 | **Contraintes monuments historiques** : délais, maîtrise d'œuvre imposée, subventions non garanties, rappel d'impôt en cas de rupture des 15 ans | L.621-9, L.621-27, R.621-28 ; CGI 156 bis ; page Culture [A6-20 à A6-28] | Élevée si le bien est protégé | Moyen à élevé (surcoût de travaux non chiffré **[INCONNU]**) | Budgéter sans subvention ; fixer une stratégie d'ouverture au public dès le départ | DRAC / CRMH, UDAP, architecte du patrimoine |
| 8 | **Sécurité des ERP et bruit** pour l'événementiel et l'hébergement | CCH R.143-19 ; arrêté du 25/06/1980 ; CSP R.1336-1 et R.1336-7 ; C. env. R.571-26 et R.571-27 [A6-50b, A6-51, A6-68, A6-69] | Élevée dès qu'il y a des réceptions | Moyen à élevé (travaux, fermeture, voisinage) | Rester en 5e catégorie si possible ; étude d'impact acoustique ; limiteurs | SDIS / commission de sécurité, acousticien |
| 9 | **Fiscalité de structure mal calibrée** : SCI à l'IR qui bascule à l'IS, perte du taux de 15 % ou de l'intégration, exclusions Dutreil, double imposition à la sortie | CGI 206-2 et BOFiP (10 %), 219 I b, 223 A, 787 B [A6-55, A6-60, A6-10, A6-35b, A6-02] | Moyenne | Moyen à élevé | Modélisation fiscale de chaque scénario d'apport avant création | Expert-comptable, avocat fiscaliste |
| 10 | **Non-conformité équestre** : enseignement sans diplôme, SIRE / lieu de détention, TVA mal appliquée, MSA, autorisation d'exploiter (pluriactif à hauts revenus) | C. sport L.212-1 et L.212-8 ; C. rural L.212-9, L.211-10-1, L.722-1, L.331-2 ; BOFiP TVA équidés [A6-82 à A6-89, A6-81] | Moyenne | Moyen (pénal 1 an / 15 k€, rappels, refus d'exploiter) | Embaucher un enseignant diplômé ; procédure SIRE ; ventilation de la TVA ; demande d'autorisation d'exploiter | MSA, DDT, IFCE, expert-comptable agricole |

---

## 14. Chiffres utiles au modèle financier

| # | Paramètre | Valeur | Statut |
|---|---|---|---|
| 1 | Droits de mutation sur un achat d'immeuble (département à 5 %, cas de 88 départements au 01/06/2026) | **6,3185 % du prix**, hors notaire. 5,81 % à 4,50 %, 5,09 % dans l'Indre | PAGE LUE (CGI, collectivites-locales, Weblex) + ESTIMATION (calcul) |
| 2 | Droit de cession des parts d'une société à prépondérance immobilière | **5 %** de la valeur des titres. 0,1 % pour des actions de SAS non immobilière | PAGE LUE (miroir) |
| 3 | IS | **15 % jusqu'à 42 500 €**, puis 25 % (chiffre d'affaires ≤ 10 M€, capital détenu à 75 % ou plus par des personnes physiques) | PAGE LUE (miroir) |
| 4 | Taxe holdings patrimoniales | **20 % par an** de la valeur des logements occupés gratuitement ou sous le marché (dette d'acquisition déduite) et des chevaux de concours sans usage professionnel, si actifs ≥ 5 M€, contrôle ≥ 50 % et revenus passifs > 50 % | PAGE LUE (miroir) |
| 5 | TVA équestre | **5,5 %** : cours, pratique, accès aux installations, pension liée à la pratique. **20 %** : valorisation, entraînement, location de boxes nus | PAGE LUE (BOFiP 25/03/2026) |
| 6 | Subventions monuments historiques (indicatives, non garanties) | **40 %** classé, **20 %** inscrit (plafond légal de 40 % pour un inscrit) ; confort et mises aux normes exclus | PAGE LUE (culture.gouv) |
| 7 | Déduction des charges d'un monument historique (contribuable à l'IR) | **100 %** si ouvert 50 jours (dont 25 non ouvrables, avril à septembre) ou 40 jours (juillet à septembre), 6 h par jour ; **50 %** si fermé ; engagement de 15 ans | PAGE LUE (BOFiP, CGI) |
| 8 | IFI | Seuil **1,3 M€**, barème de **0,5 % à 1,5 %** ; abattement de 30 % sur la résidence principale détenue directement | PAGE LUE (miroir) |
| 9 | Plafonds d'hébergement | Chambres d'hôtes **5 chambres / 15 personnes** ; gîte ERP au-delà de **15 couchages** ; 5e catégorie : O < 100, L < 200, PA < 300, CTS < 50 personnes | PAGE LUE (miroir + service-public) |
| 10 | Levée de fonds sans prospectus ni PSFP | **Moins de 150** investisseurs non qualifiés (cercle restreint) ; PSFP **5 M€ sur 12 mois** ; prospectus **à partir de 8 M€** | 150 = PAGE LUE ; 5 M€ et 8 M€ = EXTRAIT |

Autres valeurs :
- **Barème de l'usufruit** (fondateur de moins de 31 ans) : usufruit 80 %, nue-propriété 20 %. Usufruit temporaire : 23 % par tranche de 10 ans. [PAGE LUE]
- **Dutreil** : 75 %, avec engagements de 2 ans puis 6 ans. [PAGE LUE]
- **Taux du PFU** : 31,4 %. [EXTRAIT]
- **Sanction pour enseignement sans diplôme** : 1 an et 15 000 €. [PAGE LUE]
- **Amendes de notification SAFER et Sempastous** : jusqu'à 2 % de la transaction. [PAGE LUE]

---

## 15. Contre-exemples et limites des conclusions

- **« La société est toujours mauvaise » est faux.** La taxe 235 ter C ne vise ni les sociétés à l'IR, ni les sociétés à l'IS majoritairement opérationnelles, ni celles sous 5 M€ d'actifs, ni le logement loué au prix du marché. Une OpCo active qui détient un château et loue au prix du marché l'appartement de son dirigeant reste hors champ, sous réserve de la doctrine à venir.
- **« Toute activité équestre est agricole » est faux.** La pension « pure », l'enseignement sans fourniture de chevaux (selon une décision citée par Eurojuris, non vérifiée) et le spectacle ne sont pas agricoles. Ils ne relèvent donc ni du bail rural ni des bénéfices agricoles, et la TVA est souvent à 20 %.
- **« Monument historique = subventions et défiscalisation » est faux.** La subvention n'est pas un droit. La déduction n'est totale qu'avec une ouverture réelle au public et ne profite qu'aux contribuables à l'IR. Le régime 795 A impose une convention d'ouverture durable.
- **« Un bail emphytéotique permet de contrôler les terres sans la SAFER » n'est plus vrai depuis le 20/08/2026**, du fait du droit d'opposition de L.451-1-1.
- **« Le share deal évite la SAFER » est faux.** Il y a obligation d'information pour les cessions de parts, préemption possible sur la totalité des parts et contrôle Sempastous.

---

## 16. Points de doute / hypothèses non vérifiées

1. **Textes lus via un miroir, pas sur Légifrance** (Cloudflare 403). La fidélité au texte officiel est probable mais non garantie : le projet Tricoteuses avertit lui-même des erreurs possibles. Les dates de consolidation varient selon le code (01/09/2026 pour le CGI). Une modification postérieure au 01/09/2026 dans le CGI serait **invisible ici**.
2. **Taxe 235 ter C** :
   - aucun commentaire BOFiP trouvé ;
   - interprétations non tranchées : notion de « loyer inférieur au prix du marché » pour un château, valorisation, prorata d'usage professionnel d'un bâtiment mixte, application à un monument historique ouvert au public, traitement d'un usufruit.
   - L'exemple chiffré du § 3.2 est **fictif**.
   - La validation par le Conseil constitutionnel (décision n° 2026-901 DC) n'est connue que par des sources secondaires [A6-96, EXTRAIT ; A6-90b] : la page du Conseil n'a pas pu être ouverte.
3. **Dutreil** : l'application aux transmissions à compter du 21/02/2026 et l'ancienne durée de l'engagement individuel (4 ans) viennent d'un commentateur (avnear). Il n'y a pas de note de version dans le texte consolidé.
4. **Changements SAFER du 20/08/2026** : la loi n° 2026-796 est citée dans L.451-1-1. Je **suppose** qu'elle est aussi à l'origine des nouvelles versions de L.143-1 et L.141-1-1, ce que la note de version ne montre pas. Je n'ai pas comparé ces articles à leur version antérieure.
5. **Changements non analysés** : R*421-17 (décret n° 2026-117), L.112-1-1 (CDPENAF, 26/05/2026), L.722-5 (MSA, 01/01/2026), L.341-1 et L.551-1 CMF (01/07/2026), CGI 156, 206 et 50-0 (versions au 01/07/2026). J'ai seulement constaté une nouvelle version, sans en analyser le contenu.
6. **DMTO par département** : seulement agrégé (88 à 5 %, Indre à 3,80 %). La table officielle est sur impots.gouv.fr, site « en maintenance » le 14/10/2026. Le nombre exact de départements à 4,50 % est inconnu.
7. **Seuils AMF** (PSFP à 5 M€, prospectus à 8 M€) et **PFU à 31,4 % / prélèvements sociaux à 18,6 %** : EXTRAITS seulement (AMF et service-public non lus sur ces points).
8. **IFCE** (lieu de détention, registre, vétérinaire sanitaire, délais) : EXTRAITS seulement, le site étant protégé contre les robots.
9. **ICPE et équidés** : l'absence de rubrique repose sur une recherche textuelle dans l'annexe de R.511-9. Le contenu du règlement sanitaire départemental du département cible est INCONNU.
10. **Bail rural et activités équestres** : je me suis appuyé sur une source secondaire d'avocat (Eurojuris). Aucun arrêt de la Cour de cassation n'a été lu (« 1er décembre 2007 » et « Cass. 3e civ., 29 avril 2009 » cités, non vérifiés).
11. **Avantage en nature des dirigeants** : la page URSSAF lue ne détaille pas toutes les situations des mandataires sociaux, et le BOSS est inaccessible. À confirmer.
12. **Micro-BIC** : le rattachement des chambres d'hôtes à la catégorie « fourniture de logement » (203 100 € / 71 %) et celui des meublés classés n'ont pas été confirmés par le BOFiP (BOI-BIC-DECLA non lu).
13. **Textes non lus et cités comme pistes** : L.3332-2 CSP (licences IV), L.142-6 C. rural (conventions SAFER), arrêté du 25/06/1980 (lu via service-public seulement), abus de confiance (C. pén. 314-1), formalités de l'hypothèque légale, liste des diplômes équestres (annexe II-1 du code du sport), seuils Sempastous et du SDREA par région.
14. **Données manquantes du projet**, qui conditionnent la plupart des conclusions : région et département (DMTO, PLU, SAFER, seuils régionaux), statut monument historique du bien, présence de terres en zone A ou N, montant de l'apport, revenus du fondateur (contrôle des structures), présence et nature des investisseurs.
