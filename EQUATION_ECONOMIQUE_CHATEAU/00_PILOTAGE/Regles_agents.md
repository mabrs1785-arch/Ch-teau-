# Règles communes des agents de recherche — Mission « Équation économique d'un château »

1. **Langue** : tout en français. Commence par lire `/home/user/Ch-teau-/EQUATION_ECONOMIQUE_CHATEAU/00_PILOTAGE/Contexte_permanent.md`.
2. **Budget web** : **15 WebSearch au maximum par agent**, car le quota est partagé. WebFetch n'a pas ce plafond : ouvre les pages pour vérifier (textes officiels, rapports, PDF, articles, sites des domaines). Une page lue vaut mieux que dix extraits. N'utilise **pas** WebFetch sur un moteur de recherche généraliste pour contourner le quota. Les moteurs internes d'un site (par exemple la recherche d'un site officiel) sont autorisés.
3. **Rien d'inventé.** Chaque fait chiffré renvoie à une URL réellement ouverte (PAGE LUE) ou vue dans un résultat de recherche (EXTRAIT), avec la **citation exacte** ou un extrait fidèle. Sinon : ESTIMATION (raisonnement explicite), HYPOTHÈSE (choix assumé) ou INCONNU (« Je ne sais pas » + comment vérifier).
4. **Précision des chiffres** : valeur, unité, année, HT ou TTC, périmètre (région, type de bien, taille), source.
5. Distingue toujours **chiffre d'affaires / EBE / résultat / trésorerie**, **récurrent / occasionnel**, **fortune personnelle / rentabilité d'exploitation**.
6. **Sources** : écris-les dans `01_RECHERCHE/sources/sources_<ID>.csv`, séparateur `;`, avec exactement cet en-tête :
   `id;titre;url;type_source;date_consultation;statut(page_lue/extrait);utilise_dans;fiabilite(haute/moyenne/faible)`
   Identifiants : `<ID>-01`, `<ID>-02`, etc. (par exemple R1-01).
7. **Fichier de résultats** : `01_RECHERCHE/<ID>_<theme>.md`. **Écris-le au fur et à mesure**, pas seulement à la fin, pour ne rien perdre en cas d'interruption. Dans le texte, cite les sources par leur identifiant, par exemple [R1-03].
8. **Sections finales obligatoires** :
   - « Contre-exemples et cas d'échec trouvés » ;
   - « Points de doute / hypothèses non vérifiées » ;
   - « Chiffres clés pour le modèle » : tableau valeur / unité / année / statut / source.
9. **Interdits** : aucun contact de tiers, aucun formulaire, aucun achat, aucune création de compte. Ne modifie pas les fichiers des autres agents. **N'exécute aucune commande git.**
10. **Réponse finale au directeur** (courte, car les détails sont dans tes fichiers) :
    - résumé de 20 lignes au plus ;
    - 10 à 15 chiffres les plus utiles au modèle financier, avec leur statut et leur source ;
    - questions restées ouvertes ;
    - nombre de WebSearch et de WebFetch utilisés.
