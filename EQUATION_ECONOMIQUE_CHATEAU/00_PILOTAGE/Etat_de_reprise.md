# État de reprise — Mission « Équation économique d'un château »

Dernière mise à jour : 2026-10-14 (après la vague 2 et les livrables L1 à L7)

## Où en est-on ?

| Étape | Statut |
|---|---|
| Structure, contexte, règles, plan, cadre analytique | FAIT |
| Vague 1 : 8 agents (R1 à R8) | FAIT |
| Vague 2 : V2A, V2C, V2D, V2V | FAIT, intégrée au modèle et aux livrables |
| Équipe rouge V2R | EN COURS : intégrer ses constats (modèle, L1 à L7), puis rédiger L8 |
| Modèle (`02_MODELE/`) | FAIT : 11 301 formules, 0 erreur, 0 écart Excel/Python, jumeau Monte-Carlo exact |
| Livrables L1 à L7, README, registre des sources (636 sources) | FAIT |
| L8 (conclusion indépendante) | À FAIRE après l'équipe rouge |

## Résultats principaux (cas central, € 2026)

- **Besoin annuel** :
  - S1 : 0,33 M€ (0,20 à 0,56) ;
  - S2 : 1,24 M€ (0,78 à 2,06) ;
  - S3 : 3,64 M€ (2,17 à 6,41).
- **Activités calmes** : environ 4 % du besoin de S2. Le bail d'ancrage atteint 21 %, mais au prix de la partie privée.
- **Fonds d'entretien seul**, 30 ans, avec règles de pilotage :
  - pour une chance sur deux : 9,6 / 36,5 / 108,7 M€ ;
  - pour 95 % : 22,9 / 85,5 / 271,3 M€ ;
  - soit environ 30 et 70 fois le besoin.
- **Solutions** (environ 4 à 6 % d'échec avant 20 ans, 11 à 12 % avant 30 ans) :
  - S1 : 15 M€ + 0,4 M€ par an pendant 10 ans ;
  - S2 : 60 M€ + 1 M€ par an pendant 10 ans ;
  - S3 : 210 M€.
- **Premier risque, l'erreur de budget** : au haut de la fourchette, environ 30 % d'échec avant 20 ans.

## Instruction de reprise

1. Lire `00_PILOTAGE/Contexte_permanent.md`, ce fichier, `Journal.md` et le `README.md` de la mission.
2. Reconstruire le modèle : `cd 02_MODELE && python3 construire_modele.py`. Ensuite, si une hypothèse a changé : `python3 calculer_mc.py`, `python3 sensibilite.py` et `python3 tableaux.py`.
3. Si `01_RECHERCHE/V2R_equipe_rouge.md` existe avec ses sections finales : traiter ses constats, du plus grave au moins grave (correction du modèle ou des livrables, ou réponse argumentée), puis rédiger `03_LIVRABLES/L8_Conclusion_independante.md`.
4. Relancer `04_SOURCES/consolider.py` après tout ajout de sources, puis committer et pousser sur la branche `claude/new-session-4wwka5`.
