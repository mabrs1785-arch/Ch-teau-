# CONTEXTE PERMANENT — Opération Château

> Fichier de reprise. À lire en premier par tout agent ou toute session qui reprend la mission.
> Brief complet : `08_JOURNAL/Brief_mission_original.txt`. État d'avancement : `08_JOURNAL/Etat_recherche.md`.

## Mission
Trouver le chemin entrepreneurial et financier le plus crédible pour qu'un entrepreneur français de 26 ans, passionné d'équitation, à apport personnel limité (montant inconnu), devienne propriétaire ou contrôle durablement un château français (> 50 ha si possible), y vive au milieu des chevaux à l'horizon 2030-2031, avec un domaine qui s'autofinance (entretien, dette, investisseurs).

## Contraintes non négociables
- Vivre dans un château entouré de chevaux (seule hypothèse non contestable).
- Le cheval doit être structurant (pas forcément majoritaire dans le CA).
- Honnêteté : aucune source, chiffre, annonce, transaction ou investisseur inventé. « Je ne sais pas » + méthode de vérification si inconnu.
- Ne jamais présenter subvention / financement / intérêt d'investisseur comme acquis.
- EBITDA positif mais cash-flow négatif = non viable.
- Aucun contact de tiers, aucun achat, aucune signature, aucune donnée privée transmise.

## Données manquantes (à fournir par le porteur)
- Apport personnel disponible ; revenus actuels ; capacité d'emprunt personnelle.
- Région(s) préférée(s) ; disponibilité géographique.
- Nature exacte de l'expérience équestre (niveau, discipline, réseau).
- Entreprises détenues aujourd'hui (holding existante ? trésorerie ?).

## Scénarios d'apport utilisés (hypothèses explicites)
- S1 : 50 k€ ; S2 : 250 k€ ; S3 : 1 M€ (via holding après reprises d'entreprises).

## Organisation technique réelle (constatée le 2026-10-14)
- Environnement : session Claude Code cloud, conteneur éphémère. Persistance = commits git sur la branche `ccr-f4e4139a-4lc31x`.
- Internet : WebSearch / WebFetch disponibles (vérifié).
- Sous-agents : outil Agent disponible, exécution parallèle en arrière-plan.
- Excel : Python + openpyxl 3.1.5 (formules conservées). Recalcul vérifié via LibreOffice si présent.
- Pas d'exécution continue garantie de 24 h : les « heures » du brief sont des jalons logiques.
