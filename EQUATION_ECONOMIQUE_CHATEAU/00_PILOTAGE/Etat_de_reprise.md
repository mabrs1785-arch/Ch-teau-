# État de reprise — Mission « Équation économique d'un château »

Dernière mise à jour : 2026-10-14 (après l'intégration de l'équipe rouge et la révision de L1 à L8)

## Où en est-on ?

| Étape | Statut |
|---|---|
| Structure, contexte, règles, plan, cadre analytique | FAIT (ligne 14 du cadre précisée après V2R M3 : échec = réserve négative ; 12 mois de charges = seuil de tension) |
| Vague 1 : 8 agents (R1 à R8) | FAIT |
| Vague 2 : V2A, V2C, V2D, V2V | FAIT, intégrée au modèle et aux livrables |
| Équipe rouge V2R (29 constats) | FAIT : 26 constats corrigés en totalité, 3 en partie (m1, m10, m11) ; traitement détaillé dans L8, § 6 |
| Modèle (`02_MODELE/`) | FAIT : 11 814 formules, 0 erreur, 0 écart Excel/Python, jumeau Monte-Carlo < 10⁻⁶ € (consigné dans `sorties/verification.json`) |
| Livrables L1 à L8 et README | FAIT, révisés après V2R |
| Registre des sources | FAIT : 652 sources (14 lots, dont V2R) ; les 202 identifiants cités dans les livrables existent tous |

## Résultats principaux (cas central, € 2026)

- **Besoin annuel** :
  - S1 : 0,35 M€ (0,21 à 0,60) ;
  - S2 : 1,27 M€ (0,79 à 2,16) ;
  - S3 : 3,77 M€ (2,20 à 6,80).
  - Non chiffrés : chevaux de sport et infrastructures du domaine (INCONNU).
- **Activités calmes** : 1 à 6 % du besoin de S2 (3 % pour le socle retenu). Le bail d'ancrage atteint 18 %, mais au prix de la partie privée.
- **Hypothèses du capital** : rendement réel net de 2 % (1,5 à 2,5 %), retrait plafonné à 1,75 % (règle lissée).
- **Capital seul**, 30 ans, avec règles de pilotage :
  - pour une chance sur deux : 14,1 / 50,1 / 165,9 M€ ;
  - pour 95 % : 37,9 / 132,2 / 491,6 M€ ;
  - soit environ 40 et 100 fois le besoin (jusqu'à 130 fois pour S3).
- **Solutions** (critère n° 6 respecté au plus juste : environ 1,8 à 2,5 % d'échec avant 20 ans, 4,6 à 5,0 % avant 30 ans) :
  - S1 : 34 M€ + 0,4 M€ par an pendant 10 ans ;
  - S2 : 120 M€ + 1 M€ par an pendant 10 ans ;
  - S3 : 480 M€.
- **Constat C1** : le capital affecté reste la fortune du propriétaire ; aucune solution indépendante d'un capital personnel ou familial n'a été trouvée.
- **Risques principaux** (S2, échec à 30 ans) : ne jamais réunir le capital (probabilité INCONNUE) ; besoin au haut de la fourchette (22 %) ; décès en année 15 sans montage successoral (16 %) ; absence de règles de pilotage (16 %) ; capital de 80 M€ (15 %) ; décennie perdue (9 %).

## Instruction de reprise

1. Lire `00_PILOTAGE/Contexte_permanent.md`, ce fichier, `Journal.md` et le `README.md` de la mission.
2. Reconstruire le modèle : `cd 02_MODELE && python3 construire_modele.py`. Ensuite, si une hypothèse a changé : `python3 calculer_mc.py`, `python3 sensibilite.py` et `python3 tableaux.py`.
3. Après tout changement de chiffre, reporter les nouvelles valeurs dans les livrables qui les citent (L1 à L8, README), puis relancer `04_SOURCES/consolider.py` si des sources ont été ajoutées.
4. Committer et pousser sur la branche `claude/new-session-4wwka5`.

## Pistes non traitées

- Holding de PME gérée activement (remplacement des entreprises défaillantes, valeur de revente) : non modélisée (V2R m1).
- IFI calculé séparément pour le château, les terres et les bois : non fait (V2R m11).
- Fiducie, contrat de capitalisation, assurance-vie au décès (article 990 I), interaction de la CDHR avec la déduction MH : à expertiser par un avocat fiscaliste et un notaire.
- Probabilité de décès du propriétaire entre 26 et 56 ans : non recherchée.
