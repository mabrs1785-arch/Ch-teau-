# V2V — Vérification indépendante des chiffres les plus influents

Agent : V2V (vérification). Date : 2026-10-14. Statut du fichier : EN COURS (écrit au fur et à mesure).

## Méthode

- Pour chaque chiffre de la liste du directeur (`00_PILOTAGE/Prompts_agents.md`, section V2V), j'ai rouvert l'URL inscrite dans `01_RECHERCHE/sources/sources_*.csv`, sans réutiliser les fichiers téléchargés par les autres agents (dossier de travail propre : `scratchpad/v2v/`).
- PDF : téléchargés avec curl depuis l'URL officielle, texte extrait avec `pdftotext -layout`, puis recherche de la citation. Pages HTML : WebFetch, et curl quand il faut une citation mot pour mot.
- Verdicts :
  - **CONFIRMÉ** : chiffre, unité, année, périmètre et HT/TTC conformes à la source ;
  - **NUANCÉ** : chiffre présent, mais une précision change la lecture (périmètre, unité, année, HT/TTC, statut, arrondi) ;
  - **NON CONFIRMÉ** : chiffre absent de la source ou différent ;
  - **INACCESSIBLE** : source non ouverte ; aucune conclusion n'est tirée à sa place.
- Recommandation pour le modèle : garder / corriger (nouvelle valeur) / retirer.
- Les identifiants V2V-xx renvoient à `sources/sources_V2V.csv` (une ligne par URL rouverte).

## Résultats détaillés

