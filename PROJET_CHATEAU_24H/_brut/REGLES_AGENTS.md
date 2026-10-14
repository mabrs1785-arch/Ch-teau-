# Règles communes à tous les agents (Opération Château)

Contexte : lire `/home/user/Ch-teau-/PROJET_CHATEAU_24H/CONTEXTE_PERMANENT.md`.

1. Tout en français.
2. N'invente JAMAIS une source, un chiffre, une annonce, une transaction, un investisseur intéressé. Chaque chiffre factuel doit avoir une URL que tu as réellement consultée (WebSearch/WebFetch) ce jour (2026-10-14). Si tu ne trouves pas : écris « Je ne sais pas » + comment le vérifier.
3. Distingue clairement : FAIT SOURCÉ / ESTIMATION (avec hypothèse et raisonnement) / INCONNU.
4. Une annonce immobilière trouvée via un agrégateur ou un article peut être retirée : indique « disponibilité à vérifier » et la date de vérification.
5. Ne contacte personne, ne remplis aucun formulaire, n'achète rien.
6. Ajoute chaque source utilisée dans ton fichier `_brut/sources_<agent>.csv` avec l'en-tête exact :
   `id;titre;url;type_source;date_consultation;utilise_dans;fiabilite`
   (type_source : officiel / presse / annonce / entreprise / etude / autre ; fiabilite : haute / moyenne / faible). Séparateur point-virgule, UTF-8.
7. Conserve les divergences et doutes : une section « Points de doute / hypothèses non vérifiées » est obligatoire à la fin de chaque document.
8. Privilégie une découverte vérifiable à vingt idées spéculatives. Cherche aussi des exemples qui CONTREDISENT l'hypothèse que le projet est viable.
9. Termine ta réponse finale par un résumé de 15 lignes max des conclusions clés + les 10 chiffres les plus utiles pour un modèle financier (avec source ou statut « estimation »).
