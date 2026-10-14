# Règles communes — cellule audiovisuelle (mission 2, v2)

Contexte projet : château français > 50 ha, vie privée sur place, domaine équestre de prestige, apport limité. Cellule indépendante de la recherche financière ; transmet ses découvertes.

## Capacités réelles (vérifiées 2026-10-14)
- Accès web ouvert. WebFetch peut échouer (DNS) : utiliser alors curl via Bash :
  curl -sSL --max-time 30 "URL" | python3 -c "import sys,html,re; t=sys.stdin.read(); t=re.sub(r'(?s)<(script|style).*?</\1>',' ',t); print(html.unescape(re.sub(r'<[^>]+>',' ',t))[:20000])"
- YouTube : la page d'une vidéo donne titre, chaîne, date, durée, DESCRIPTION (souvent avec chapitres horodatés écrits par l'auteur). Pour la durée/date, chercher dans le HTML brut : "lengthSeconds", "publishDate", "uploadDate".
- AUCUN outil de transcription audio (installation refusée par l'utilisateur). Ne PAS télécharger d'audio ni de vidéo. Ne PAS utiliser d'outils tiers de récupération de sous-titres automatiques (contournement interdit par le brief).
- Transcriptions autorisées : uniquement celles publiées en texte par l'auteur ou l'hébergeur (page d'épisode, blog, site de l'émission, transcription publique).
- Budget : 25 WebSearch MAX par agent ; WebFetch/curl sans limite raisonnable.

## Statuts obligatoires (jamais « regardé » ni « écouté »)
- REPÉRÉ : seulement vu dans un résultat de recherche.
- MÉTADONNÉES LUES : page ouverte (titre, date, durée, description).
- DESCRIPTION/CHAPITRES LUS : description détaillée ou notes d'épisode lues.
- TRANSCRIPTION TEXTE LUE (partielle/complète) : transcription publiée en texte réellement lue.
- SOURCE SECONDAIRE : article de presse qui rapporte le contenu de l'interview.

## Honnêteté
- Aucun horodatage inventé : seulement ceux écrits dans une description/chapitres/transcription, avec lien horodaté YouTube (&t=XXs) si dérivé d'un chapitre réel.
- Aucune citation inventée ; paraphrase fidèle signalée comme telle.
- Une affirmation d'un intervenant ≠ fait vérifié : recouper les chiffres importants (presse, comptes Pappers/Companies House).
- Durée/date inconnues → « inconnu ».

## Livrables de chaque agent
- Catalogue : _brut/catalogue_<agent>.csv, séparateur « ; », en-tête exact :
  id;titre;intervenant;chaine_ou_emission;plateforme;type;langue;date;duree;url;sujets;statut_traitement;pertinence_0_100;resume_court
- Fiches : 02_ANALYSES/<agent>_fiches.md — pour chaque contenu pertinent : Identification (titre, intervenant, chaîne, date, durée, URL, niveau d'accès) ; Analyse (résumé, infos entrepreneuriales, modèle économique, financement, difficultés, chiffres cités + statut de vérification, limites, application au projet) ; Passages importants (horodatages réels seulement) ; Note /100.
- Cas réels (si pertinent) : 03_CAS_REELS/<agent>_cas.md
- Idées : 04_IDEES_STRATEGIQUES/<agent>_idees.md — chaque idée : qui, contexte, fonctionnement, intérêt, coût potentiel, difficultés, adaptation au projet, sources.
- Sources : _brut/sources_<agent>.csv (id;titre;url;type;auteur_ou_chaine;date;statut_acces;utilise_dans;fiabilite)
- Réponse finale : résumé ≤ 15 lignes, nombre de contenus par statut, 3 découvertes les plus fortes.

## Fichiers temporaires
Utilise un sous-dossier personnel du scratchpad (ex. scratchpad/<ton_agent>/) : le dossier temporaire est partagé entre agents et des scripts ont déjà été écrasés.
