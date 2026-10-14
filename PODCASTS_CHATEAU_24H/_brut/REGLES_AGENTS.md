# Règles communes — cellule audiovisuelle (focus : The Family)

Contexte projet : lire /home/user/Ch-teau-/PROJET_CHATEAU_24H/00_SYNTHESE/Rapport_executif.md (conclusion : un château ne finance pas son achat ; stratégie « capital d'abord via reprise de PME, château ensuite »).

Contraintes techniques CONSTATÉES (2026-10-14) :
- YouTube, Spotify, Apple Podcasts, sites de transcription : INACCESSIBLES (proxy). WebFetch bloqué (DNS). Aucun outil de transcription audio.
- Seul WebSearch fonctionne (extraits de résultats). Quota partagé : 45 recherches MAX par agent.

Règles d'honnêteté :
1. Tout en français.
2. Ne jamais prétendre avoir regardé/écouté un contenu. Statut obligatoire pour chaque contenu :
   - « repéré (métadonnées seulement) » : titre/URL/date vus dans un résultat de recherche ;
   - « analysé partiellement via texte de tiers » : un article, un billet ou une transcription publiée en texte résumant le contenu a été lu en extrait ;
   - jamais « analysé intégralement ».
3. Aucun horodatage inventé : n'en indiquer que s'il apparaît textuellement dans une source.
4. Aucune citation inventée. Une affirmation d'un intervenant ≠ un fait vérifié.
5. Durée/date inconnues → « inconnu ».
6. Sources dans _brut/sources_<agent>.csv, séparateur « ; », en-tête : id;titre;url;type(video/podcast/article/officiel/autre);auteur_ou_chaine;date;statut_acces;utilise_dans;fiabilite
7. Fin : résumé de 15 lignes max.
