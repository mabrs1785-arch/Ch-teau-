# Hypothèses non vérifiées — registre v2

**Niveau de preuve de la v2.** 413 sources, dont **373 pages réellement lues** (90 %). Le reste vient d'extraits de recherche. Les pages ont été lues via curl, car WebFetch échouait. Légifrance a bloqué l'accès : les articles de loi ont été lus sur un miroir non officiel de la base Légifrance (git Tricoteuses) et **doivent être recoupés sur Légifrance** avant tout acte.

Impact sur la conclusion : 🔴 peut renverser la recommandation · 🟠 modifie les montants · 🟢 marginal.

## 1. Le porteur (inconnu — à fournir)
| Hypothèse | Utilisée | Impact | Vérification |
|---|---|---|---|
| Apport disponible | 50 k€ / 250 k€ / 1 M€ | 🔴 | Le porteur |
| Expérience de gestion d'écurie, de reprise d'entreprise | Aucune supposée | 🔴 | Le porteur |
| Revenus extérieurs pour vivre sans salaire du domaine | Nécessaires dans tous les scénarios | 🔴 | Le porteur |

## 2. Immobilier et travaux
| Hypothèse | Utilisée | Impact | Vérification |
|---|---|---|---|
| Prix d'un domaine type | 2,5 M€ (médiane de 19 annonces, PL) | 🟠 | DVF, visites, notaires |
| Disponibilité des 29 biens | Annonces en ligne le 14/10/2026 (PL) ; sous offre possible | 🟠 | Appel des agences (action du porteur) |
| Travaux d'un domaine équipé | 0,9 M€ (EST, sans visite) | 🔴 | Diagnostic d'architecte du patrimoine, devis |
| Gros entretien | 1,8 % de (bâti + travaux), ≈ 41 k€/an | 🟠 | Diagnostic ; Demeure Historique ≥ 40 k€/an (PL) |
| Assurance | 12 k€ (2,5 à 30 k€ selon les sources) | 🟠 | Devis d'un assureur spécialisé |
| Valeur de sortie | 80 % du coût, moins 5 % de frais | 🟠 | Historique DVF ; Hus −35 % (prix affiché), fonds de l'hôtel de Bricquebec −49 % (PL) |

## 3. Revenus
| Hypothèse | Utilisée | Impact | Vérification |
|---|---|---|---|
| Pension box | 450 € TTC (3e quartile hors Île-de-France ; médiane 375 €) | 🔴 | 20 grilles locales autour du bien |
| TVA de la pension | 5,5 % si la pension est liée à l'accès aux installations, 20 % sinon | 🟠 | Rescrit fiscal, expert-comptable équin |
| Occupation | 90-92 % (aucune donnée publiée) | 🟠 | Écuries comparables |
| Mariages | 12/an à 4 197 € HT (prix PL, volume EST) | 🟠 | Comptes de lieux comparables, plateformes |
| Gîte | 92 nuits à 450 € (prix PL, occupation EST) | 🟢 | Gîtes de France du département |
| Showcases, location à un cavalier professionnel | Aucun tarif publié (INC) / une annonce (EX) | 🟢 | Entretiens avec des professionnels (porteur) |

## 4. Charges
| Hypothèse | Utilisée | Impact | Vérification |
|---|---|---|---|
| Salaires | Smic chargé ≈ 30 k€/ETP (PL pour le Smic, EST pour les charges) | 🟠 | Simulateur URSSAF/MSA |
| Productivité | 1 ETP pour 17-20 équidés (PL) | 🟠 | Réseau Équin |
| Foin | Prix INCONNU (pas de cotation officielle) ; pousse de l'herbe −33 % en août 2026 (PL) | 🟠 | FranceAgriMer, Chambres d'agriculture |
| Travail du fondateur | Non payé (variantes frugales et C) | 🔴 | Choix de vie du porteur |

## 5. Financement et holding
| Hypothèse | Utilisée | Impact | Vérification |
|---|---|---|---|
| Taux bancaire | 4,0 % (FBF 3,64 %, PL ; BdF 3,66 %, EX) | 🟢 | Banques |
| LTV et apport pour un château | 50-65 % / 25-35 % (EST ; aucun barème trouvé) | 🟠 | 3 consultations bancaires |
| Multiple de reprise de PME | 4,5 fois l'EBITDA (EST, non sourcé) | 🔴 | Expert en transmission, données de cessions |
| Cash remonté par une reprise | ≈ 50 k€/an pendant 7 ans pour une PME à 1 M€ (agent 2, calcul) | 🔴 | Plan d'affaires réel |
| Investisseurs, vendeur, obligataires, subventions | AUCUN acquis, aucun contacté | 🔴 | — |

## 6. Juridique (à valider par des professionnels)
- Taxe de 20 % de l'art. 235 ter C (loi de finances 2026) : aucun commentaire BOFiP trouvé.
- Loi n° 2026-796 du 18/08/2026 (SAFER, opposition aux baux emphytéotiques) : rattachement des articles L.143-1 et L.141-1-1 à cette loi = hypothèse de l'agent 6.
- Droits de mutation par département : table impots.gouv indisponible ; 6,3185 % retenu (88 départements).
- Requalification en bail rural d'écuries louées : risque élevé selon le Code rural (L.311-1, L.411-1).

## 7. Divergences conservées entre agents
- **Pension premium** : l'agent 3 retenait 520 € TTC ; l'auditeur montre que seules 10 % des offres hors Île-de-France atteignent ce niveau. **450 € retenus.**
- **Loyer privé** : le directeur le comptait en recette ; l'auditeur l'a retiré, car c'est l'argent d'un fondateur non payé. **Retiré.**
- **Fonds propres de C** : le directeur supposait 3,4 M€ venant de la holding ; l'agent 2 et l'auditeur estiment 0,2-0,7 M€ pour une reprise unique. **Les deux sont conservés** (`C_central` et `C_holding_realiste`), et les feuilles H1-H3 chiffrent l'écart.
- **Mariages** : 12/an (agent 4) contre un test haut à 18/an (auditeur, qui rend C robuste). **12 conservés, 18 dans le cas optimiste.**
