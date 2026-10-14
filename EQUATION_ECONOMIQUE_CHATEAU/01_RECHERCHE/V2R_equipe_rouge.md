# V2R — Équipe rouge : ce qui est faux, fragile, incohérent ou oublié

Agent : V2R (équipe rouge, vague 2 bis). Date : 2026-10-14.
Sources nouvelles : `sources/sources_V2R.csv` (V2R-01 à V2R-16). Les autres identifiants renvoient aux fichiers des agents R1 à R8 et V2A à V2V.
Versions attaquées : modèle `02_MODELE/` dans son état de 19 h 19 (seules des notes ont changé depuis ma copie de 19 h 12), sorties `mc_*.json` de 19 h 17 à 19 h 26, livrables L1 (19 h 21), L2 (19 h 24), L3 (19 h 29), L4 (19 h 32) et L6 (19 h 24). **Les numéros de ligne renvoient à ces versions.** Le directeur a modifié L1, L2 et L6 pendant mon travail ; les constats déjà corrigés entre-temps ne figurent plus ci-dessous. L5, L7 et L8 sont parus pendant la rédaction ; ils sont examinés rapidement au § 5.

---

## Résumé

1. **Le pilier de la solution n'a pas de véhicule juridique.** Aucun outil français ne réunit affectation au domaine, jouissance privée et revenus défiscalisés. La « dotation affectée » est donc la fortune personnelle du propriétaire, ce que le brief voulait éviter, et les livrables écrivent le contraire (C1).
2. **Le rendement réel net de 3 % n'est cohérent avec aucun véhicule.** La seule donnée (3,5 % réel pour les actions, avant frais et impôts) ne le permet pas. L'impôt atteint 38,6 % pour un haut revenu (PFU + CEHR + CDHR). Estimation : 1,1 à 1,8 %. Avec le Monte-Carlo du modèle relancé, la dotation « 95 % » de S2 passe de 85,5 M€ à environ 110-155 M€, soit 90 à 125 fois le besoin (C2).
3. **Trois mécanismes flattent le Monte-Carlo.** Un sinistre est payé en annulant des travaux et ne coûte rien. Une réserve entamée ne se reconstitue jamais, si bien que l'austérité devient permanente tout en comptant comme un succès. Enfin, l'échec est défini moins sévèrement que dans le Cadre (M1 à M3).
4. **La solution recommandée échoue au critère n° 6 du Cadre** (11 % d'échec à 30 ans pour une cible de 5 %). Les livrables ne le disent pas (M3).
5. **Angles morts.** Les droits de succession (environ 44 % de la dotation par génération), la communauté de biens, le risque de séquence (« décennie perdue » : l'échec double) et le délai de constitution du capital (20 à 40 ans) ne sont pas traités (M5 à M9).
6. **Ce qui résiste.** La calibration des rendements est exacte (moyenne géométrique simulée : 2,99 %), et le jumeau Python reproduit le classeur. La conclusion qualitative en sort renforcée : les activités sur place couvrent moins de 10 % du besoin, et le capital nécessaire est encore plus grand qu'annoncé.

---

## 1. Méthode

- **Lecture.** J'ai lu `Contexte_permanent`, `Regles_agents`, `Cadre_analytique`, `Etat_de_reprise`, L1, L2, L3, L4 et L6, `tableaux.md`, tous les `mc_*.json` et le code du modèle (`parametres*.py`, `budget.py`, `moteurs.py`, `modeles.py`, `projection.py`, `monte_carlo.py`, `calculer_mc.py`, `construire_modele.py`). J'ai aussi lu les passages utiles de R2, R3, R5, R6, R8, V2C, V2D et V2V.
- **Contre-calculs.** J'ai copié le modèle dans le scratchpad (aucun fichier du dépôt modifié) et reconstruit le registre avec `construire()`.
  - J'ai écrit une variante instrumentée de `monte_carlo.simuler()` : `simuler_v`, avec la même graine et le même ordre des tirages. Sans option, elle reproduit exactement le modèle : 1,525 % d'échec à 20 ans et 4,845 % à 30 ans à 85,5 M€, identiques. La dotation « 95 % » publiée de S2 (85,5 M€ après arrondi à 0,1 M€) est retrouvée exactement sur 6 000 trajectoires, avec la même graine.
  - Options ajoutées, une à une :
    - sinistres payés en plus du fonds de travaux ;
    - reconstitution de la réserve ;
    - échec quand la réserve passe sous un an de besoin ;
    - rendement et retrait modifiés ;
    - choc de crise et écart-type modifiés ;
    - rendement moyen abaissé les 10 premières années.
  - Probabilités : 20 000 trajectoires. Dotations nécessaires : dichotomie sur 4 000 trajectoires, précision d'environ ±5 %.
- **Fiscalité et droit.** J'ai lu les textes officiels lisibles : BOFiP, service-public.fr, guide HMRC, guide de la DRAC (PDF via `pdftotext`) et question écrite du Sénat. Légifrance reste inaccessible (403).

---

## 2. Tableau des constats, classés par gravité

Statuts : **VÉRIFIÉ** (texte lu ou calcul refait), **PLAUSIBLE** (raisonnement solide, une pièce manque), **SPÉCULATIF** (piste sans preuve).

| N° | Gravité | Affirmation attaquée (fichier, ligne ou paramètre) | Preuve | Statut | Effet sur les conclusions | Correction proposée |
|---|---|---|---|---|---|---|
| C1 | **CRITIQUE** | L2 l.318 : « Ce n'est pas la fortune personnelle au sens courant : c'est une dotation affectée, sur le modèle des « maintenance funds » britanniques ». L3 l.100 : « distinct du patrimoine personnel ». L4 l.13 : « séparé du patrimoine personnel ». L2 l.335 : « socle de la solution » | Aucun véhicule français ne réunit affectation, jouissance privée et revenus défiscalisés. **Fonds de dotation et fondations** : apport « gratuit et irrévocable » et « mission d'intérêt général » [V2R-02 § 60-110] ; un logement gratuit du fondateur profite à un « cercle restreint » [R3-43]. **Holding à l'IS** : il faut distribuer, sinon c'est un acte anormal de gestion [R3-56]. **Compte-titres, assurance-vie, société civile** : patrimoine personnel, soumis à la communauté [V2R-07] et aux droits de succession [V2R-06]. **Fiducie** : vrai « patrimoine d'affectation » [V2R-13], mais fiscalement transparente et de coût inconnu [V2R-14]. **Maintenance fund britannique** : accès du public obligatoire, aucun contrôle du constituant, logement gratuit interdit, impôts et chauffage de confort exclus, revenus imposés [V2R-01] | VÉRIFIÉ (règles lues). PLAUSIBLE pour l'absence d'équivalent (la fiducie reste à expertiser) | La solution recommandée revient à **détenir personnellement 70 à 125 fois le besoin annuel**. C'est la dépendance à la fortune personnelle que le brief excluait, et les livrables affirment le contraire | Remplacer la phrase de L2 l.318 par le texte du § 3.1, et corriger de même L3 l.100 et L4 l.13. Ajouter le tableau des véhicules (§ 3.1) à L2 § 6.3. Écrire dans L8 : « aucune solution indépendante d'un capital personnel ou familial n'a été trouvée » |
| C2 | **CRITIQUE** | `dot_rendement` = 0,03, « net de frais et d'impôts », statut ESTIMATION (projection.py l.53-56). `dot_taux_net` = 0,0275 (moteurs.py l.204). L2 l.282 ; L3 l.117 ; L4 l.18, l.76 et l.91 | La seule donnée est un rendement d'indice : 3,5 % réel pour les actions mondiales depuis 2000, avant frais et impôts [V2R-08]. R8 § 7.1 qualifie lui-même 2,5-3 % d'« HYPOTHÈSE de travail », sans frais. Impôt d'un haut revenu : PFU 31,4 % + CEHR 3 à 4 % + CDHR (minimum de 20 % hors prélèvements sociaux), soit **38,6 %** [V2R-16][V2R-04][V2R-05]. Assurance-vie : 12,8 % + 17,2 % au rachat [V2R-03]. Holding à l'IS puis distribution : **54 %**. Le modèle associe le risque d'un portefeuille équilibré (σ = 10 %, crise de −25 %) à un rendement net supérieur au rendement brut des actions | VÉRIFIÉ pour les taux. ESTIMATION pour le rendement : 1,1 à 1,8 % réel net en direct, 0 à 0,3 % via une holding (§ 3.2) | Dotation « 95 % » de S2 (Monte-Carlo du modèle relancé) : **85,5 → 109,5 M€** à 2 % et **123,6 M€** à 1,5 %. **143,4 M€** à 3 % avec le risque d'un portefeuille d'actions. **123 à 155 M€** en ajoutant M1 et M2. S1 : 35 à 45 M€ ; S3 : 437 à 599 M€ | `dot_rendement` = 0,02 (favorable 0,025, défavorable 0,015), statut HYPOTHÈSE. `dot_taux_net` = 0,0175 (0,0225 ; 0,0125). L2 l.282 : « rendement réel net de 2 % (HYPOTHÈSE : 3,5 % réel brut pour les actions mondiales depuis 2000 [R8-32], moins 1,2 à 1,8 point de frais et d'impôts en détention directe, et près de 3 points via une holding à l'IS [V2R]) ». Recalculer L2 § 6.1, L3, L4 § 6 et L6 § 4 |
| M1 | **MAJEUR** | Sinistres non assurés prélevés sur le fonds de gros entretien : monte_carlo.py l.117-118 ; projection.py l.219-222. L6 l.25 et l.141-142 (« absorbé »). L4 l.86 (« ne jamais créer de retard d'entretien caché… Oui ») et l.182 | Réplique des formules de projection. Le sinistre de 600 k€ de l'an 6 coûte **0 € de trésorerie** : il ramène la campagne de l'an 8 de 1,31 à 0,71 M€. Le test « travaux » (sinistre + campagnes +30 %) dépasse le fonds de 1,84 M€ sur 20 ans, **moins** que les seules campagnes +30 % (2,02 M€). Dans le Monte-Carlo, 1,28 M€ de sinistres en moyenne sur 30 ans sont payés en supprimant des travaux | VÉRIFIÉ (code et calcul) | Le stress test « travaux » ne teste pas le sinistre, et un retard d'entretien se crée en silence. S2 : dotation « 95 % » **+8 %** (84,9 → 91,6 M€) ; échec à 30 ans de 4,8 à 6,2 % pour 85,5 M€ | projection.py : `depassement_trav` = `MAX(0,[campagne]-[fonds_ge@-1]-[b_ge_prov])+[choc_trav]` et `fonds_ge` = `MAX(0,[fonds_ge@-1]+[b_ge_prov]-[campagne])`. Même correctif dans monte_carlo.py (§ 3.6) |
| M2 | **MAJEUR** | Règles de pilotage et réserve : monte_carlo.py l.97 et l.154-156 ; projection.py l.257-266. L4 l.85 : réserve « reconstituée chaque année… Oui ». L6 l.128 : « la dotation la reconstitue chaque année ». L2 l.289-302 : colonne « 1 chance sur 2 » | Le retrait ne dépasse jamais le besoin net moins les dividendes. Le solde n'est donc jamais positif quand on retire, et tout excédent part dans la dotation : une réserve entamée ne remonte jamais. Une fois déclenchée, la tension dure jusqu'à l'an 30 dans **100 %** des trajectoires concernées. Au seuil « 1 chance sur 2 » (36,5 M€), le domaine est en mode de tension **93 % des années** : coupe de 10 %, travaux −13 %. Preuve que la mesure récompense l'austérité : pour S3, la dotation « 95 % » vaut **242,7 M€** avec une réserve de 3,5 M€ (sous un an de besoin, donc tension dès l'an 1), contre **271,3 M€** avec 4 M€ | VÉRIFIÉ (code et deux calculs) | Le « succès » inclut une austérité permanente. Le seuil de 50 % n'a pas de sens comme objectif. L4 et L6 décrivent un mécanisme que le modèle n'a pas | Ajouter la reconstitution de la réserve (formule au § 3.6). Testée : l'échec ne change pas (4,9 %) et les années de tension sont divisées par deux. Publier la probabilité de tension et la part des années en tension à côté de la probabilité d'échec. Corriger L4 l.85 et L6 l.128 |
| M3 | **MAJEUR** | Cadre l.14 (réserve ≥ 12 mois) et l.131 (échec ≤ 5 % sur 20 **et** 30 ans pour le modèle recommandé). En face : L4 l.32 et L6 l.27-31 (11,1 à 11,2 % à 30 ans) ; note de projection.py l.130-133 | Les trois solutions échouent dans 10,9 à 11,9 % des cas à 30 ans (`mc_distribution_solutions.json`). Avec l'échec défini comme dans le Cadre (réserve sous 12 mois), la dotation « 95 % » de S2 (85,5 M€) échoue dans **17,9 %** des cas à 30 ans. Il faudrait **121 M€** | VÉRIFIÉ | La solution recommandée ne respecte pas les critères de robustesse fixés par le projet, sans que les livrables le signalent | Soit dimensionner à 95 % sur 30 ans (S2 : 85,5 M€ dans le modèle actuel, environ 123 M€ une fois corrigé). Soit écrire en L4 § 1 et L6 § 1 : « la solution S2 ne respecte pas le critère n° 6 du Cadre (11 % > 5 %) ». Aligner la ligne 14 du Cadre sur la définition retenue |
| M4 | **MAJEUR** | Variante « leviers » (MH + besoin −15 %) : projection.py l.63-70 ; monte_carlo.py l.131 ; L2 l.239 et l.289-293 ; `mc_dotation_necessaire.json` | La déduction MH porte sur le revenu global imposé au barème [R3-02]. Or, dans la solution, les revenus du propriétaire sont des revenus de capitaux au PFU. En S2, il faut **279 k€ de déduction par an**, donc environ 0,36 M€ de revenus au barème (ESTIMATION). L'excédent ne se reporte pas [R3-05 § 1], alors que le Monte-Carlo lisse l'avantage sur chaque année. L'effet de la CDHR sur cet avantage est INCONNU | VÉRIFIÉ pour les règles, PLAUSIBLE pour le montant | Le MH explique à lui seul la baisse de 85 à 75,8 M€ (−11 %). Il réintroduit la dépendance aux revenus personnels | Remplacer cette variante par « leviers vérifiés −7,5 %, sans MH », déjà calculée (78,4 M€, `mc_comparaison_modeles.json`), dans `calculer_mc.py` (`dotations()`) et dans L2 § 6.1. Présenter le MH à part, sous condition de revenus au barème |
| M5 | **MAJEUR** | L2 § 6.3, l.316-327 : sept conditions de pérennité, aucune sur la transmission. L4 l.252 ; L6 § 6 | Droits en ligne directe : abattement de 100 000 € par enfant, puis jusqu'à 45 % au-delà de 1 805 677 € [V2R-06]. Sur une dotation de 85,5 M€ partagée entre deux enfants : **37,9 M€, soit 44 %** (ESTIMATION). L'article 795 A n'exonère que le monument et son mobilier, en échange d'une ouverture perpétuelle de 50 jours par an [R3-13][R3-14]. Le maintenance fund britannique, lui, est exonéré [V2R-01] | VÉRIFIÉ (barème), ESTIMATION (montant) | Sans montage, la dotation « perpétuelle » perd environ 44 % à chaque génération. Un décès pendant l'horizon fait échouer le modèle | Ajouter une 8e condition à L2 § 6.3 : « transmission organisée (démembrement des parts d'une société civile [V2D-19], assurance-vie, donation-partage), avec simulation notariale ». Ajouter à `calculer_mc.py` un test « décès en année t : dotation −44 % » |
| M6 | **MAJEUR** | Gouvernance de la dotation : L2 l.322 ; L4 § 2 (comité) ; `part_surplus_dotation` = 1 (projection.py l.57) | En communauté réduite aux acquêts, les « économies faites sur les revenus des biens appartenant à l'un de vous 2 » et les « revenus d'épargne et de placements » sont des biens communs [V2R-07]. Le modèle réinvestit 100 % des excédents : la croissance de la dotation (×1,67 en médiane sur 30 ans à 85,5 M€) deviendrait commune. Aucune charte n'est opposable à son propre auteur | PLAUSIBLE (à faire valider par un notaire) | Un divorce partage la part réinvestie. La discipline de dépense ne repose que sur la volonté du propriétaire | Ajouter aux conditions de pérennité : un contrat de mariage adapté, et un capital logé dans une structure à statuts contraignants (société civile avec un gérant indépendant, ou fiducie), à faire valider |
| M7 | **MAJEUR** | L4 § 6.2, l.204-210 : délais calculés à 3 % pour 60 M€. L3 l.16-17 | Avec la dotation corrigée (environ 123 M€ en S2) et 2 % réel : environ **35 ans** d'épargne à 2,5 M€ par an et 20 ans à 5 M€ par an. Pour 85,5 M€ : 38 ans à 1,5 M€ par an (ESTIMATION). Les dividendes de transition exigent eux-mêmes une entreprise de 2,5 à 2,8 M€ d'EBITDA, soit 12,6 à 22,5 M€ de valeur | ESTIMATION | Le seuil de déclenchement risque d'être atteint vers 50 ou 60 ans, ou jamais. Hors héritage ou cession d'entreprise, seule la voie « S1 d'abord » est accessible | Refaire L4 § 6.2 avec 2 % et la dotation corrigée. Dans L8, placer « ne jamais réunir le capital » au premier rang des risques (probabilité INCONNUE) |
| M8 | **MAJEUR** (S3) / MINEUR (S1, S2) | budget.py l.104 : « hors maîtrise d'œuvre des chantiers ». L1 § 4.1, l.123 | Sur un monument classé : architecte obligatoire pour tous travaux ; architecte en chef des MH ou architecte du patrimoine expérimenté pour une restauration ; diagnostic préalable ; honoraires « évalués sur l'enveloppe prévisionnelle des travaux » ; assurance dommages-ouvrage obligatoire [V2R-09]. Aucune ligne du budget ne porte ces coûts, et la règle du NRC ne dit pas qu'elle les inclut | PLAUSIBLE (taux INCONNU) | S'ils ne sont pas inclus, il faut ajouter 10 à 15 % du gros entretien (HYPOTHÈSE) : **+31 à 47 k€ par an en S2, +118 à 177 k€ en S3** | Créer `taux_moe_do` = 0,12 (favorable 0,08, défavorable 0,18), statut HYPOTHÈSE, et une ligne « maîtrise d'œuvre, diagnostics, SPS, dommages-ouvrage » égale à [bati_ge] × taux. Ou bien écrire noir sur blanc que le taux de 2,25 % les inclut |
| M9 | **MAJEUR** | `ruptures()` de calculer_mc.py ; L6 § 5.3 (la séquence défavorable n'est « pas simulée séparément ») | Monte-Carlo relancé avec un rendement moyen de 0 % réel les 10 premières années, puis 3 % : échec à 30 ans de **4,8 à 12,4 %** à 85,5 M€, et de **11,2 à 23,6 %** pour la solution S2. Avec 1 % au lieu de 0 % : 9,2 % à 85,5 M€ | VÉRIFIÉ (calcul). Le scénario est une HYPOTHÈSE de stress | Le risque de séquence est le premier risque de marché, et les livrables ne le chiffrent pas | Ajouter à `simuler()` un paramètre de rendement moyen des n premières années, et une ligne « décennie perdue » à `ruptures()` et à L6 § 4.2 |
| M10 | **MAJEUR** | L4 l.85-86 : la charte annonce une réserve « reconstituée chaque année » et un fonds de travaux qui ne crée « jamais de retard d'entretien caché », avec « Oui » dans la colonne « Dans le modèle ? ». L6 l.128 | Voir M1 et M2 : le modèle ne reconstitue jamais la réserve, et il crée un retard d'entretien caché (sinistres, report de 30 % des travaux en tension) | VÉRIFIÉ | Le lecteur croit que la simulation applique la charte, alors qu'elle ne l'applique pas | Écrire « Non (à corriger, V2R M1-M2) » tant que les correctifs ne sont pas faits |
| m1 | MINEUR | Holding de PME : monte_carlo.py l.16-17 et l.136 ; L2 l.310 ; L3 l.34 et l.87 | Le taux de défaillance vient de reprises de 1997-2003, souvent endettées [R8-36]. Il est appliqué sans limite de durée à des PME sans dette. Ni réinvestissement, ni remplacement des entreprises disparues, ni valeur de revente | VÉRIFIÉ (code) | Les 67 à 91 % d'échec décrivent une holding passive, pas un groupe géré. La conclusion qualitative tient | Écrire « holding passive, sans réinvestissement ni revente ». Ajouter une variante avec remplacement des PME défaillantes et une valeur terminale |
| m2 | MINEUR | `ent_conversion` = 0,396 (moteurs.py l.208) ; L2 l.309 (0,40) ; L4 l.19 (« environ 2,5 M€ d'EBITDA ») | Pour un actionnaire à haut revenu : 0,77 × 0,75 × (1 − 0,386) = **0,355** [V2R-04][V2R-05] | VÉRIFIÉ pour les taux, ESTIMATION pour le résultat | Rendement des PME de 4,4 à 7,1 % au lieu de 5 à 8 %. EBITDA nécessaire : 2,8 M€ au lieu de 2,5 M€ | `ent_conversion` = 0,355 (favorable 0,40, défavorable 0,33) |
| m3 | MINEUR | `fuite_fiscale` = 0,30 (modeles.py l.64-68) ; L2 l.21 ; L4 l.76 | La chaîne IS + PFU fait 48,6 %, et 54 % avec la CEHR et la CDHR. La valeur centrale suppose, sans calcul, que la moitié des contributions finance des coûts déductibles | VÉRIFIÉ (taux) | Faible : les activités ne pèsent que 47 k€ par an | Valeur centrale 0,40, défavorable 0,54 |
| m4 | MINEUR | `taux_reserve` = 0 (projection.py l.51) | Depuis 2000 : actions à 3,5 % réel et prime de 4,3 % sur les bons du Trésor [V2R-08]. La trésorerie a donc rapporté environ −0,8 % réel par an (ESTIMATION) | ESTIMATION | Faible (réserve de 1,5 M€) | −0,005 (favorable 0, défavorable −0,01) |
| m5 | MINEUR | Seuil de tension fixe : `res < flex_seuil × B0` (monte_carlo.py l.97 ; projection.py l.199-200) | B0 est le besoin de l'année 1. Les charges dérivent de +10 à +18 % en 20 ans : le seuil glisse vers 0,85 à 0,9 an de besoin réel | VÉRIFIÉ (code) | La tension se déclenche trop tard en fin de période | Comparer la réserve à `flex_seuil × total_charges(t)` |
| m6 | MINEUR | Note de la feuille Budget (construire_modele.py l.94-95) : la provision « retient le maximum de deux méthodes indépendantes (composants et ratio) » | budget.py n'applique que le ratio. L1 l.56 indique que la méthode par composants ne sert que de contrôle qualitatif | VÉRIFIÉ | Note fausse dans le classeur | Remplacer par : « La provision applique un taux à la valeur de reconstruction (règle du NRC) ; la méthode par composants n'a pas pu être sourcée » |
| m7 | MINEUR | L2 l.72 : investissement de 35 k€ pour le centre de reproduction. `tableaux.md` affiche « — » pour l'hivernage et le gardiennage | moteurs.py n'a aucun paramètre d'investissement pour la reproduction. `stock_capex` et `auto_capex` existent, mais tableaux.py ne les lit pas | VÉRIFIÉ | Un chiffre non sourcé ; un tableau généré incomplet | Retirer les 35 k€ ou créer un paramètre `repro_capex` sourcé. Faire lire les `*_capex` par tableaux.py |
| m8 | MINEUR | Pension standard dans la solution : projection.py l.77 (`"B": ["eq_std", "eq_ret"]`). Tranquillité jugée « bonne » en L2 l.338 et L6 § 7 | Contribution de −1 k€ dans le cas central et de −40 k€ dans le cas défavorable. Trente boxes en pension, c'est 25 à 30 propriétaires de chevaux présents chaque semaine, week-ends compris (leçon n° 4 du Contexte) | PLAUSIBLE | Du monde en plus et un risque, pour un gain nul | Retirer `eq_std` de la solution, ou le limiter à 10 boxes |
| m9 | MINEUR | L1 l.226 ; `cheval_an` (parametres.py l.251) | Le budget ne compte ni le renouvellement des chevaux, ni un camion de transport, ni les concours, pour un propriétaire « passionné de chevaux » | SPÉCULATIF (aucune source) | De l'ordre de +15 à +40 k€ par an en S2 (HYPOTHÈSE) | Écrire en tête de L1 que les chevaux de sport (achat, renouvellement, transport, concours) sont exclus, ou ajouter une ligne marquée HYPOTHÈSE |
| m10 | MINEUR | Règle du NRC appliquée aux seuls bâtiments (`valeur_reconstruction`, budget.py) | La règle exclut « land and major associated infrastructure » [V2V-02]. Aucun poste ne couvre les murs d'enceinte, les allées, les réseaux, l'assainissement, les étangs ou les ponts | PLAUSIBLE | Sous-estimation non chiffrée (INCONNU) | Ajouter une ligne « voirie et réseaux, murs, allées, ouvrages hydrauliques », à chiffrer sur métré |
| m11 | MINEUR | IFI : abattement de 30 % appliqué à tout le prix d'achat (budget.py l.92-99) | L'abattement ne vise que la résidence principale. Les 80 à 300 ha de terres et de bois ont leurs propres régimes (bois, biens ruraux loués) [R3-01] | PLAUSIBLE | Quelques k€ par an | Calculer séparément château et parc d'un côté, terres et bois de l'autre |
| m12 | MINEUR | L2 l.326 : « enveloppes de capitalisation » | Le HCSF peut limiter les rachats des contrats d'assurance-vie et de capitalisation pour 3 mois, et 6 mois consécutifs au plus [V2R-10, fiabilité faible] | PLAUSIBLE | Liquidités gelées en pleine crise systémique | Garder la réserve (au moins 6 mois de besoin) hors des contrats d'assurance |
| m13 | MINEUR | S1 : 0,6 ETP de soigneur pour 4 chevaux, aucun agent d'entretien (parametres.py l.202) | Un cheval se soigne 365 jours par an : le reste du travail repose sur le propriétaire (leçon n° 3 du Contexte) | PLAUSIBLE | S1 sous-estimé d'environ 10 k€ par an, ou temps du fondateur non compté | `S1_etp_soigneur` = 1,0, ou écrire que le propriétaire assure les week-ends |
| m14 | MINEUR | L1 l.55 : « un « minimum absolu » » | Le NRC écrit « In the absence of specific information […] absolute minimum » et réserve la règle à un parc de bâtiments, en moyenne sur 5 à 10 ans [V2V-02][V2V-03]. parametres.py a été corrigé, pas L1 | VÉRIFIÉ | Formulation trop forte | « … un minimum en l'absence d'information spécifique, pour un parc de bâtiments et sur 5 à 10 ans » |
| m15 | MINEUR | Taxe sur les holdings : L2 l.236 ; L4 l.72 | L'assiette finale se limite aux biens somptuaires ; titres et trésorerie en sont exclus [V2R-11]. Le projet initial visait pourtant les titres et la trésorerie [V2R-12]. Aucun commentaire du BOFiP n'a été trouvé | PLAUSIBLE | Risque législatif pour une dotation logée dans une holding | Ajouter : « assiette susceptible d'être élargie (projet initial) ; texte officiel à lire » |
| m16 | MINEUR | L6 l.6 : contrôle du jumeau « consigné dans `sorties/verification.json` » | Le fichier `verification.json` de 19 h 25 ne contient plus la clé du jumeau : calculer_mc.py relance `recalculer_et_verifier()`, qui réécrit le fichier sans elle | VÉRIFIÉ | Perte de traçabilité | Appeler `verifier_jumeau()` dans calculer_mc.py, ou ne plus y réécrire le fichier |
| m17 | MINEUR | Etat_de_reprise l.21-24 (S1 : 9/20 M€ ; S2 : 36/76 M€ ; S3 : 102/224 M€). Conclusion de L1, l.243 : « 3,5 M€ pour un grand monument classé » | Sorties actuelles : 9,6/22,9 M€, 36,5/85,5 M€ et 108,7/271,3 M€. Besoin de S3 : 3,64 M€ | VÉRIFIÉ | Trois jeux de chiffres circulent | Mettre à jour l'état de reprise et la conclusion de L1 |

---

## 3. Preuves détaillées

### 3.1 C1 — Le véhicule de la « dotation affectée »

| Véhicule | Peut-il financer la partie privée d'un domaine habité ? | Fiscalité des revenus du capital | Affectation réelle au domaine | Sources |
|---|---|---|---|---|
| Fonds de dotation | **Non.** Il reçoit des biens apportés « à titre gratuit et irrévocable » et utilise ses revenus « en vue de la réalisation d'une œuvre ou d'une mission d'intérêt général », avec une gestion désintéressée. Un logement gratuit pour le fondateur sert les intérêts d'une personne « clairement individualisable » | Pas d'IS (1 bis de l'article 206) si la gestion est désintéressée | Totale, mais au profit de la mission d'intérêt général, plus du propriétaire | [V2R-02] § 60, 90, 110 ; [R3-43] ; [R3-58] |
| Fondation reconnue d'utilité publique, fondation abritée | **Non**, pour les mêmes raisons | Pas d'IS (1 bis de l'article 206) | Totale, au profit de l'intérêt général | [V2R-02] § 90 |
| Holding à l'IS (société de portefeuille) | Seulement par distribution. Payer des charges privées sans distribuer = revenu distribué et acte anormal de gestion | IS de 25 %, puis PFU de 31,4 % à la distribution, et 38,6 % avec CEHR et CDHR : **48,6 à 54 %** des revenus nominaux | Faible : l'associé majoritaire peut changer les statuts | [R3-20] [R3-56] [R3-57] [V2R-04] [V2R-05] |
| Même holding, au regard de la taxe de 20 % (LF 2026) | — | Biens somptuaires (logement de l'associé, chevaux de concours) taxés à 20 % de leur valeur. Titres et trésorerie exclus de l'assiette finale, mais visés par le projet initial | — | [R3-18] [V2R-11] [V2R-12] |
| Compte-titres personnel | Oui | 31,4 % + CEHR de 3 à 4 % + CDHR : jusqu'à **38,6 %** | **Aucune** | [V2R-16] [V2R-04] [V2R-05] |
| Société civile de portefeuille à l'IR | Oui | Transparente : comme le compte-titres (régime détaillé non lu, HYPOTHÈSE) | Faible : statuts, gérance, démembrement possible des parts | [V2D-19] |
| Assurance-vie, contrat de capitalisation | Oui | Gains imposés au rachat : 12,8 % (7,5 % après 8 ans dans la limite de 150 000 € de primes) + 17,2 % de prélèvements sociaux, plus CEHR et CDHR. Imposition différée. Rachats gelables jusqu'à 6 mois | **Aucune** | [V2R-03] [V2R-10] |
| Fiducie-gestion (article 2011 du code civil) | Probable (constituant bénéficiaire), régime actuel INCONNU | Transparente : le constituant reste redevable | **Réelle** : « patrimoine d'affectation » confié à un fiduciaire. Coût INCONNU | [V2R-13] [V2R-14] |
| « Maintenance fund » britannique, cité par L2 | N'existe pas en droit français. Au Royaume-Uni, il exige des « undertakings to maintain and allow public access » ; « powers allowing the settlor or owner of the endowed property to exercise control over the Maintenance Fund are not consistent with schedule 4 » ; « powers to make interest-free loans, provide rent-free accommodation […] are not permissible ». Il couvre les « running repairs and maintenance costs, though not rates and taxes », et le chauffage seulement « to the extent […] necessary […] to maintain or preserve the building » | Revenus imposés au nom du constituant ou au « trust rate currently 40% and the dividend trust rate currently 32.5% ». Avantage : exonération de droits de succession | Totale : trustees professionnels, contrôle de l'administration fiscale | [V2R-01] |

**Texte proposé pour L2 l.318 :**

> « Ce capital reste juridiquement le patrimoine du propriétaire, ou d'une société qu'il contrôle. Le droit français n'offre pas d'équivalent privé des maintenance funds britanniques. Ceux-ci exigent d'ailleurs un accès du public, interdisent tout contrôle du constituant et tout logement gratuit, et ne paient ni les impôts ni le confort. L'affectation au domaine ne repose ici que sur une discipline volontaire (charte, comité), éventuellement sur une fiducie dont le coût reste à établir. La solution suppose donc de disposer d'une fortune de 70 à 125 fois le besoin annuel. »

Phrases à corriger de même : L3 l.100 (« distinct du patrimoine personnel au sens courant ») et L4 l.13 (« séparé du patrimoine personnel »).

### 3.2 C2 — Rendement réel net : estimation et effet

**Formule (ESTIMATION).**

```
nominal brut   = (1 + r) × (1 + π) − 1
après frais    = nominal brut − f
impôt annuel   = après frais × s × τ
net réel       = (1 + après frais − impôt annuel) ÷ (1 + π) − 1
```

Paramètres :
- r : rendement réel brut, HYPOTHÈSE de 2,5 à 3,5 %. Ce sont 3,5 % pour des actions seules [V2R-08], moins pour un portefeuille équilibré.
- π : inflation de 2 % [D-01].
- f : frais de 0,4 à 0,6 %, HYPOTHÈSE (mandat, fonds, enveloppe, comité).
- s : part du rendement réalisée et imposée chaque année, de 0,5 à 0,7, HYPOTHÈSE (l'assurance-vie diffère l'impôt).
- τ : taux d'imposition, 30 à 38,6 % [V2R-03][V2R-04][V2R-05][V2R-16].

| Cas | r | f | s | τ | Rendement réel net |
|---|---:|---:|---:|---:|---:|
| Compte-titres, propriétaire à haut revenu, portefeuille équilibré | 3,0 % | 0,6 % | 0,7 | 38,6 % | **1,23 %** |
| Assurance-vie (imposition différée, sans CEHR ni CDHR) | 3,0 % | 0,6 % | 0,5 | 30 % | **1,76 %** |
| Portefeuille d'actions, frais bas, haut revenu | 3,5 % | 0,4 % | 0,7 | 38,6 % | **1,74 %** |
| Hypothèse basse | 2,5 % | 0,6 % | 0,7 | 31,4 % | **1,06 %** |
| Holding à l'IS, tout distribué (τ = 54 %) | 3,0 à 3,5 % | 0,6 % | 1 | 54 % | **0,05 à 0,28 %** |

**Le couple « 3 % net, σ = 10 % » est incohérent.**
- Un portefeuille équilibré, compatible avec σ = 10 %, rapporte moins que les 3,5 % bruts des actions.
- Un portefeuille d'actions, qui peut approcher 3 % net, a un risque proche de σ = 16 % et des crises de −35 % (HYPOTHÈSE). Avec ce risque et 3 % de rendement, la dotation « 95 % » de S2 vaut déjà **143,4 M€**.

**Effet sur la dotation « 95 % » de S2** (Monte-Carlo du modèle, 4 000 trajectoires par dichotomie, précision d'environ ±5 %) :

| Couple rendement net / retrait | Règles du modèle (dotation 95 % / 50 %) | Avec M1 et M2 corrigés (dotation 95 % / 50 %) |
|---|---:|---:|
| 3 % / 2,75 % (modèle) | 84,9 / 36,8 M€ | 91,6 M€ à 95 % (sinistres hors fonds seulement) |
| 2,5 % / 2,25 % | 96,6 / 39,7 M€ | — |
| **2 % / 1,75 % (correction proposée)** | 109,5 / 43,3 M€ | **123,3 / 49,1 M€ (≈ 100 fois / 40 fois le besoin)** |
| 1,5 % / 1,25 % | 123,6 / 47,7 M€ | **154,7 / 55,9 M€ (≈ 125 fois / 45 fois)** |
| 2 % / 2,75 % (retrait inchangé) | 102,7 / 43,9 M€ | — |
| Risque d'actions (σ = 16 %, crise de −35 %), 3 % / 2,75 % | 143,4 M€ à 95 % | — |
| Risque d'actions, 2,5 % / 2,25 % | — | 173,9 M€ à 95 % |

Avec les mêmes corrections, la dotation « 95 % / 50 % » devient :
- **S1** : 35,2 / 13,4 M€ à 2 %, et 44,7 / 15,2 M€ à 1,5 % ;
- **S3** : 436,8 / 162,0 M€ à 2 %, et 598,5 / 189,3 M€ à 1,5 %.

Le sinistre médian du modèle vaut une année de gros entretien, soit 1,18 M€ en S3 : c'est pourquoi S3 réagit le plus.

**La solution S2 publiée (60 M€ + 1 M€ par an pendant 10 ans), avec 2 % et sinistres payés à part :**
- échec de **11,2 % à 20 ans et 23,1 % à 30 ans** ;
- domaine en tension **51 % des années** ;
- avec la définition d'échec du Cadre (réserve sous 12 mois) : 79,6 % et 84,8 %.

### 3.3 M1 — Où passe le sinistre de 600 k€ ?

Les formules de `projection.py` ont été répliquées. Montants en k€ constants.

| Année | Provision | Campagne | Sinistre | Dépassement payé | Fonds en fin d'année |
|---:|---:|---:|---:|---:|---:|
| 4 | 321 | 1 268 | 0 | 0 | 0 |
| 5 | 323 | 0 | 0 | 0 | 323 |
| 6 | 325 | 0 | **600** | **0** | 48 |
| 7 | 328 | 0 | 0 | 0 | 376 |
| 8 | 330 | **707** (au lieu de 1 307) | 0 | 0 | 0 |

- Sur 20 ans, les campagnes réalisées passent de 6,74 à 6,14 M€ (**−600 k€ de travaux**), pour **0 €** de dépense supplémentaire.
- Le test « travaux » (sinistre + campagnes ×1,3) produit 1,84 M€ de dépassements, contre 2,02 M€ pour les seules campagnes ×1,3 : ajouter un choc **réduit** la dépense.
- Dans le Monte-Carlo, à 85,5 M€ : 1,28 M€ de sinistres en moyenne sur 30 ans. Payés à part, ils font passer l'échec à 30 ans de 4,8 à 6,2 %.

### 3.4 M2 — Une austérité permanente comptée comme un succès

Le code le montre directement (monte_carlo.py) :
- l.154 : `retrait = min(max(0, besoin_net − div), plafond_eff)`, donc `solde = div + retrait − besoin_net ≤ 0` dès qu'il y a un retrait ;
- l.156 : tout solde positif part dans la dotation si la réserve est positive.

La réserve ne peut donc que stagner ou baisser. Mesures sur 20 000 trajectoires et 30 ans :

| Configuration (S2) | Échec à 20 / 30 ans | Trajectoires avec au moins une tension | Part des années en tension | Tension encore présente en année 30, si déclenchée | Coupes cumulées (moyenne) |
|---|---:|---:|---:|---:|---:|
| Dotation de 85,5 M€ (seuil « 95 % ») | 1,5 / 4,8 % | 17,5 % | 6,8 % | **100 %** | 0,25 M€ |
| Même dotation, réserve reconstituée | 1,5 / 4,9 % | 17,2 % | 3,1 % | 48 % | 0,11 M€ |
| Dotation de 36,5 M€ (seuil « 1 chance sur 2 ») | 37,9 / 51,1 % | 100 % | **93,5 %** | 100 % | 3,48 M€ (et campagnes −13 %) |
| Solution publiée (60 M€ + dividendes) | 4,5 / 11,2 % | 33,7 % | 14,6 % | 100 % | 0,54 M€ |
| Solution publiée, réserve reconstituée | 4,6 / 11,3 % | 33,0 % | 7,8 % | 54 % | 0,29 M€ |
| 85,5 M€, échec défini comme dans le Cadre (réserve sous 12 mois) | **11,1 / 17,9 %** | — | — | — | — |

**Preuve que la mesure récompense l'austérité.** Même modèle, même graine, 6 000 trajectoires : la dotation « 95 % » de S3 vaut **242,7 M€** avec une réserve initiale de 3,5 M€, et **271,3 M€** avec 4 M€. Avec 3,5 M€, la réserve est sous un an de besoin (3,64 M€) : coupe de 10 % et retrait d'urgence de 4 % s'appliquent dès l'année 1. Ce chiffre de 242,7 M€ figurait dans `mc_dotation_necessaire.json` à 19 h 08. Le garde-fou de calculer_mc.py et la réserve portée à 4 M€ l'ont fait disparaître depuis.

**Autres dotations « 95 % » de S2 :**
- échec défini comme dans le Cadre : 121,9 M€ (121,4 M€ avec reconstitution) ;
- sans règles de pilotage : 101,0 M€.

### 3.5 M4 et M5 — Levier MH et succession

**Levier MH.** Dotation « 95 % » de S2, 4 000 trajectoires :

| Variante | Dotation 95 % |
|---|---:|
| Pure | 84,9 M€ |
| Avantage MH seul | 75,8 M€ |
| Besoin −15 % seul | 70,8 M€ |
| Les deux (publié : 64,0 M€) | 63,2 M€ |

- L'avantage annuel modélisé vaut 114,3 k€. Il suppose 278,9 k€ de charges déduites chaque année du revenu global.
- Il faut donc environ 0,36 M€ de revenus imposés au barème : 0,28 M€ de déduction, plus environ 0,08 M€ de seuil de la tranche à 41 % (barème 2026 non relu). C'est une ESTIMATION.

**Succession.** Barème en ligne directe [V2R-06], abattement de 100 000 € par enfant, calcul ESTIMATION :

| Dotation transmise | Un enfant | Deux enfants | Trois enfants |
|---|---:|---:|---:|
| 36,5 M€ | 16,1 M€ (44,2 %) | 15,9 M€ (43,5 %) | 15,6 M€ (42,7 %) |
| 85,5 M€ | 38,2 M€ (44,7 %) | 37,9 M€ (44,3 %) | 37,6 M€ (44,0 %) |
| 120 M€ | 53,7 M€ (44,8 %) | 53,4 M€ (44,5 %) | 53,2 M€ (44,3 %) |

Parades à étudier avec un notaire :
- démembrement à 26 ans : la nue-propriété vaut 20 % [V2D-19] ;
- assurance-vie (article 990 I, non vérifié) ;
- donation-partage.

### 3.6 Correctifs de code proposés (à reporter par le directeur)

```python
# M1 — monte_carlo.py, lignes 117-118 (et formules équivalentes dans projection.py, lignes 219-222)
depassement = np.maximum(0, campagne - fonds - ge) + sinistre
fonds = np.maximum(0, fonds + ge - campagne)

# M2 — monte_carlo.py, lignes 154-156 : reconstitution de la réserve jusqu'à sa cible res0
manque = np.maximum(0, P["res0"] - res)
retrait = np.minimum(np.maximum(0, besoin_net - div + manque), plafond_eff)
solde = div + retrait - besoin_net
apport = np.where(solde > 0, np.maximum(0, res + solde - P["res0"]), 0.0)
# projection.py, ligne « retrait » : ajouter +MAX(0,{res0}-[reserve@-1]) au besoin ;
# ligne « apport_dot » : IF([flux_solde]>0, MAX(0,[reserve@-1]+[flux_solde]-{res0}), 0)

# m5 — seuil de tension sur le besoin de l'année, et non sur B0 (ligne 97)
tension = (P["pilotage"] * (res < P["flex_seuil"] * total_prec)).astype(float)   # total_prec : charges de t-1

# M9 — simuler(…, rdt_debut=None, n_debut=10) : moyenne = rdt_debut si t <= n_debut, sinon dot_rendement
```

Le comportement de ces correctifs a été testé sur la copie du scratchpad : M1 et M2 donnent les chiffres des § 3.2 à 3.4. Le correctif m5 n'a pas été testé.

---

## 4. Ce qui résiste à l'attaque (contre-vérifications)

| Point vérifié | Résultat |
|---|---|
| Double comptage des crises dans le rendement de la dotation | **Aucun.** Moyenne arithmétique simulée : 3,75 %. Moyenne géométrique : **2,99 %**. Écart-type total, crises comprises : 12,2 % (2 millions de tirages). La correction de moyenne de monte_carlo.py (l.142-148) est exacte. |
| Jumeau Monte-Carlo et projection | Ma variante sans option reproduit `simuler()` à l'identique. La dotation « 95 % » publiée de S2 (85,5 M€) est retrouvée. |
| Formule de l'IFI (budget.py) | Conforme au barème 2026 [R3-15] : 10 550 € pour S2 (base de 2,45 M€). |
| Dividendes de PME | Ils entrent nets dans le Monte-Carlo (`S2_sol_div`, « nets ») : pas de double imposition. |
| Particulier employeur ou entreprise pour le personnel du domaine | Écart d'environ +5 k€ par an pour S2 : sans allègement à bas salaire, mais moins cher à haut salaire selon le coefficient de R2 (× 1,30). Négligeable. |
| Taxe de 20 % sur une dotation de titres | Non applicable dans le texte final : titres et trésorerie exclus [V2R-11]. L4 a raison sur ce point. |
| Fonds de dotation écarté pour la partie privée | L3 l.125 et L4 l.73 le disent correctement. Le défaut est ailleurs : présenter quand même le capital comme « séparé du patrimoine personnel ». |
| Activités sur place inférieures à 10 % du besoin de S2 | Aucune preuve contraire trouvée. Les corrections m3 et m8 réduisent encore leur contribution. |
| Main-d'œuvre de la pension standard | Le travail valorisé (≈ 1,3 ETP pour 25 chevaux) est cohérent avec « 1 UMO pour 19,4 équidés » en pension hébergement [R6]. |

---

## 5. Livrables parus pendant la rédaction (L5, L7, L8, entre 19 h 34 et 19 h 41)

Je les ai lus rapidement, seulement pour situer les constats ci-dessus. Je ne les ai pas attaqués en détail.

- **L8 l.30** reconnaît que la question du brief « n'a donc pas de réponse au sens strict ». C'est juste, et c'est le cœur de C1. Mais L8 l.18 (« fonds d'entretien séparé du patrimoine courant »), L8 l.30 (« capital affecté une fois pour toutes ») et L7 l.31 (« distinct du patrimoine personnel courant ») maintiennent l'idée d'un capital séparé. Le droit français ne le permet pas pour un usage privé (§ 3.1), sauf fiducie, dont le coût est inconnu. Ces phrases appellent la même correction que L2 l.318.
- **L8 l.57-63 et l.87** chiffrent désormais la sensibilité au rendement (`mc_sensibilite_rendement.json`) : 107,7 M€ à 2 % et 124,2 M€ à 1,5 %, avec un retrait adapté. Ces chiffres concordent avec les miens (109,5 et 123,6 M€, à ±5 % près). C2 demande d'aller plus loin : changer la valeur **centrale**, ne pas seulement la signaler, et ajouter M1 et M2 (+12 à +25 %).
- **L8 l.22-25** compare un « fonds seul, 95 % sur 30 ans » à un « montage hybride, 95 % sur 20 ans ». Les horizons diffèrent, et le montage hybride ne respecte pas le critère n° 6 du Cadre sur 30 ans (M3).
- **L5 l.138, L7 l.17 et L7 l.73** gardent 3 % comme valeur de référence (C2).
- **L7 l.98 et l.141** traitent la transmission du château par l'article 795 A, mais pas celle de la dotation : M5 reste entier.
- **L8 l.49** cite le « jumeau Monte-Carlo exact » : c'est exact pour le code, mais `verification.json` ne le consigne plus (m16).

---

## Contre-exemples et cas d'échec trouvés

1. **Même le meilleur régime d'Europe n'empêche pas le retard d'entretien.** Les membres de Historic Houses déclarent 2 Md£ de travaux en retard [R5-15], alors que le Royaume-Uni offre des maintenance funds exonérés de droits de succession. Ces fonds restent soumis à l'impôt sur leurs revenus, à l'accès du public et au contrôle de l'administration [V2R-01].
2. **La fiscalité des revenus du capital change en cours de route.** La CDHR (taux minimal de 20 %) a été créée par la loi de finances pour 2025, puis reconduite en 2026 [V2R-05][V2R-15]. Pour un haut revenu, l'impôt sur les revenus du capital passe de 31,4 % à 38,6 %. C'est exactement le risque d'un plan de 30 ans fondé sur un rendement net.
3. **La taxe sur les holdings a changé d'assiette en quatre mois.** Le projet visait les titres et la trésorerie [V2R-12]. Le texte final ne vise plus que les biens somptuaires, au taux de 20 % [V2R-11]. Une dotation logée dans une holding porte donc un risque législatif.
4. **Une enveloppe d'assurance peut être gelée en crise.** La loi Sapin 2 permet de limiter les rachats jusqu'à 6 mois consécutifs [V2R-10].
5. **Échec méthodologique interne.** Pour S3, la dotation « 95 % » a varié de 11,8 % (242,7 → 271,3 M€) selon que la réserve initiale était juste au-dessous ou au-dessus d'un an de besoin (§ 3.4).
6. **Décennie perdue.** Avec 10 années à 0 % réel, l'échec à 30 ans de la solution S2 passe de 11,2 à 23,6 % (§ 2, M9).

---

## Points de doute / hypothèses non vérifiées

- **Fiducie** (articles 2011 et suivants du code civil). Non vérifié sur Légifrance (403) : ouverture aux personnes physiques, constituant bénéficiaire, régime fiscal actuel, coût, durée, sort au décès. Seuls la question du Sénat de 2008 [V2R-13] et un extrait du rapport de 2006 [V2R-14] ont été vus. **INCONNU.**
- **Contrat de capitalisation.** Fiscalité des rachats supposée alignée sur l'assurance-vie, et inclusion dans la succession : non vérifiées dans une page lue (HYPOTHÈSE).
- **Assurance-vie au décès** (article 990 I) : non vérifié. C'est la principale parade possible au constat M5.
- **CDHR.** Elle est certaine pour les revenus 2025 et 2026 [V2R-05]. Sa prorogation « jusqu'à un déficit public sous 3 % du PIB » repose sur des synthèses d'avocats [R3-18] : à confirmer. Son interaction avec la déduction MH (réintégration éventuelle dans le revenu de référence) est **INCONNUE** : le BOFiP renvoie aux réintégrations « expressément mentionnées dans la loi ».
- **Taux des trusts britanniques.** Le guide HMRC écrit « currently 40% / 32.5% ». La date de la page n'a pas été vérifiée et ces taux ont pu changer, sans effet sur le constat.
- **Honoraires de maîtrise d'œuvre et dommages-ouvrage sur un monument historique** : aucun barème public trouvé. Les 10 à 15 % sont une HYPOTHÈSE. On ignore aussi si l'enveloppe du NRC les inclut.
- **Rendement réel net corrigé.** Les 2 % proposés (1,5 à 2,5 %) sont une ESTIMATION qui repose sur des hypothèses de frais, de part réalisée et d'allocation. Le paramètre est au haut de mon estimation (1,1 à 1,8 %) : je l'ai retenu pour ne pas surcorriger.
- **Variante « actions »** (σ = 16 %, crise de −35 %) : paramètres HYPOTHÈSES, non calibrés sur une série.
- **Application de la communauté de biens** à une dotation de biens propres dont les revenus sont réinvestis : à faire valider par un notaire.
- **Probabilité de décès** du propriétaire entre 26 et 56 ans : non recherchée (tables de l'INSEE). **INCONNU.**
- **Infrastructures** (murs, voirie, réseaux) : aucun ordre de grandeur sourcé. **INCONNU.**
- **Blocage Sapin 2** : source commerciale (fiabilité faible). Le texte de l'article L631-2-1 du code monétaire et financier n'a pas été lu.

---

## Chiffres clés pour le modèle

| # | Donnée | Valeur | Unité | Année | Statut | Source |
|---:|---|---|---|---|---|---|
| 1 | Rendement réel net de la dotation, proposé (favorable / central / défavorable) | 2,5 / **2,0** / 1,5 | % par an | 2026 | ESTIMATION | § 3.2 ; [V2R-03] [V2R-04] [V2R-05] [V2R-08] [V2R-16] |
| 2 | Taux de retrait proposé (favorable / central / défavorable) | 2,25 / **1,75** / 1,25 | % du capital | 2026 | HYPOTHÈSE | § 3.2 |
| 3 | Impôt sur les revenus du capital, revenu de référence > 330 k€ (personne seule) | 38,6 | % | 2026 | ESTIMATION (calcul sur textes lus) | [V2R-04] [V2R-05] [V2R-16] |
| 4 | Contribution exceptionnelle sur les hauts revenus | 3 (250-500 k€) / 4 (> 500 k€) | % du revenu de référence | 2026 | PAGE LUE | [V2R-04] |
| 5 | Contribution différentielle : taux minimal | 20 | % du revenu de référence (hors prélèvements sociaux) | revenus 2025-2026 | PAGE LUE | [V2R-05] |
| 6 | Assurance-vie : impôt au rachat après 8 ans / prélèvements sociaux | 7,5 puis 12,8 au-delà de 150 000 € de primes / 17,2 | % des gains | 2026 | PAGE LUE | [V2R-03] |
| 7 | Holding à l'IS puis distribution : prélèvement total | 48,6 (sans CEHR ni CDHR) / 54 (avec) | % des revenus nominaux | 2026 | ESTIMATION | [R3-20] [R3-57] [V2R-05] |
| 8 | `ent_conversion` corrigé | 0,355 (0,40 / 0,33) | € nets par € d'EBITDA | 2026 | ESTIMATION | m2 |
| 9 | Droits de succession en ligne directe : abattement et taux marginal | 100 000 € par enfant ; 45 % au-delà de 1 805 677 € | € ; % | 2026 | PAGE LUE | [V2R-06] |
| 10 | Part d'une dotation de 85,5 M€ prélevée par les droits (2 enfants) | 44,3 (37,9 M€) | % | 2026 | ESTIMATION | § 3.5 |
| 11 | Dotation « 95 % » de S2 : modèle / rendement corrigé / plus M1 et M2 / rendement de 1,5 % | 85,5 / 109,5 / 123,3 / 154,7 | M€ | 2026 | ESTIMATION (Monte-Carlo du modèle relancé) | § 3.2 |
| 12 | Dotation « 95 % » de S1 et S3, corrigée (2 %) | 35,2 et 436,8 | M€ | 2026 | ESTIMATION | § 3.2 |
| 13 | Dotation « 95 % » de S2 si l'échec est défini comme dans le Cadre (réserve sous 12 mois) | 121,4 | M€ | 2026 | ESTIMATION | § 3.4 |
| 14 | Effet d'une décennie à 0 % réel sur l'échec à 30 ans (85,5 M€ / solution S2) | 4,8 → 12,4 / 11,2 → 23,6 | % | 2026 | ESTIMATION | M9 |
| 15 | Surcoût des sinistres payés à part (S2, dotation 95 %) | +8 (84,9 → 91,6 M€) | % | 2026 | ESTIMATION | § 3.3 |
| 16 | Maîtrise d'œuvre, diagnostics et dommages-ouvrage | 12 (8 à 18) | % du gros entretien | 2026 | HYPOTHÈSE | [V2R-09] (obligations, sans taux) |
| 17 | Rendement réel de la trésorerie depuis 2000 | ≈ −0,8 | % par an | 2000-2024 | ESTIMATION | [V2R-08] |
| 18 | Blocage possible des rachats d'assurance-vie (Sapin 2) | 3 mois, 6 mois consécutifs au plus | mois | 2026 | PAGE LUE (fiabilité faible) | [V2R-10] |

---

## Bilan d'outillage

- **WebSearch : 6 sur 8.**
  - Régime fiscal du fonds de dotation (BOFiP).
  - Contribution différentielle sur les hauts revenus.
  - Blocage Sapin 2.
  - Honoraires de maîtrise d'œuvre sur un monument historique.
  - Taxe sur les holdings patrimoniales.
  - Fiducie.
- **WebFetch : 6 appels, 4 exploitables** :
  - UBS 2025 ;
  - Prosper Conseil ;
  - LégiFiscal ;
  - Deloitte.

  Deux ont échoué : Actu-Juridique (403) et le Sénat (503, page ensuite lue avec curl).
- **curl, avec conversion HTML → texte locale** :
  - guide HMRC (chapitres 3 et 8 lus) ;
  - service-public F22414, F14198, F2613, F31130 et F835, plus des sondages d'identifiants et le moteur de recherche interne du site ;
  - BOFiP BOI-IS-CHAMP-10-50-30-50 (versions 2017 et 2024) et BOI-IR-CDHR-10 ;
  - question écrite du Sénat de 2008.
- **pdftotext** : guide de la DRAC de Normandie (20 pages).
- **Python 3.13** :
  - copie du modèle dans le scratchpad et reconstruction du registre ;
  - variante instrumentée `simuler_v` et huit scripts d'analyse (`a1` à `a8`) ;
  - environ 60 calculs de dotation par dichotomie et une trentaine de simulations à 20 000 trajectoires.

  Fichiers de travail : `scratchpad/v2r/` (hors dépôt).
- **Aucun fichier existant modifié.** Aucune commande git. Aucun contact extérieur.
