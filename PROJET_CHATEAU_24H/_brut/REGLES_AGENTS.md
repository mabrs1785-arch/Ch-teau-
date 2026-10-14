# Règles communes — Opération Château v2

1. Tout en français. Lire d'abord /home/user/Ch-teau-/PROJET_CHATEAU_24H/CONTEXTE_PERMANENT.md.
2. Budget : 25 WebSearch MAXIMUM par agent. WebFetch fonctionne désormais : OUVRE les pages pour vérifier (annonces, textes officiels, articles). Préfère une page lue à dix extraits.
3. N'invente JAMAIS une source, un chiffre, une annonce, une transaction, un investisseur intéressé. Chaque fait chiffré = URL réellement ouverte ou vue.
4. Statut de chaque donnée : PAGE LUE (WebFetch réussi) / EXTRAIT (résultat de recherche seulement) / ESTIMATION (raisonnement explicite) / INCONNU (« Je ne sais pas » + comment vérifier).
5. Annonces : indiquer « page active le 2026-10-14 » seulement si la page a été ouverte et montre le bien en vente.
6. Sources : _brut/sources_<agent>.csv, séparateur « ; », en-tête exact :
   id;titre;url;type_source;date_consultation;statut(page_lue/extrait);utilise_dans;fiabilite
7. Section finale obligatoire : « Points de doute / hypothèses non vérifiées ». Cherche aussi des contre-exemples.
8. Aucun contact, formulaire, achat. Ne pas toucher aux fichiers des autres agents.
9. Réponse finale : résumé ≤ 15 lignes + les 10 chiffres les plus utiles au modèle financier (avec statut).

## Fichiers temporaires
Utilise un sous-dossier personnel du scratchpad (ex. scratchpad/<ton_agent>/) : le dossier temporaire est partagé entre agents et des scripts ont déjà été écrasés.
