# Équation économique d'un château — dossier de mission

**Question posée :** comment financer durablement le fonctionnement d'un grand château français (plus de 50 ha) et de son domaine, sans dépendre de la fortune personnelle du propriétaire ? Le propriétaire a 26 ans, aime les chevaux et vit dans une partie entièrement privée. Il veut un patrimoine d'exception, des jardins impeccables, un personnel suffisant et un domaine élégant et calme. Le brief d'origine est dans `00_PILOTAGE/Brief_mission_original.txt`.

---

## La réponse en cinq points

1. **Un grand domaine coûte chaque année environ 8 à 10 % de sa valeur de reconstruction** (L1).
   - S1, relativement économique : environ 0,33 M€ par an.
   - S2, grand domaine équestre haut de gamme : environ 1,24 M€ par an.
   - S3, domaine historique ultra-premium : environ 3,64 M€ par an.
   - Ce sont des budgets **nécessaires** à un entretien d'exception, calculés ligne par ligne. Ils sont plus élevés que ce que dépensent en moyenne les propriétaires réels, qui accumulent du retard d'entretien.
2. **Les activités compatibles avec une résidence calme n'en couvrent que quelques pour cent** : 4 % du besoin de S2 dans le cas central (L2).
   - Le château-hôtel perd de l'argent dans le cas central.
   - Le seul revenu sur place à la bonne échelle, un bail à un exploitant de séminaires (environ 21 %), sacrifie la partie privée.
3. **Le fonctionnement durable repose sur un capital affecté au domaine** (L3, L4) : un fonds d'entretien diversifié, géré avec une règle de dépense, constitué de préférence par des entreprises dont les revenus sont convertis en capital.
   - Pour S2 : 60 M€ de fonds et 1 M€ de dividendes par an pendant 10 ans.
   - Pour S1 : 15 M€ et 0,4 M€ par an.
   - Règle simple : **environ 70 fois le besoin annuel** pour 95 % de chances de tenir 30 ans avec un fonds seul.
4. **Ce montage résiste aux crises testées**, mais il ne résiste pas à une erreur de budget (L5, L6).
   - Aucun déficit sur 20 ans dans 8 stress tests.
   - Environ 4 % d'échec simulé avant 20 ans et 11 % avant 30 ans.
   - Si le besoin réel se situe au haut de la fourchette, le risque passe à 30 % avant 20 ans.
5. **Le premier levier se joue avant l'achat** (L7) : valider le budget sur le bien réel et choisir un domaine à la mesure du capital qu'on peut lui affecter.

La conclusion indépendante (L8) discute ce que ce dossier démontre et ce qu'il ne démontre pas.

---

## Par où commencer

| Pour… | Lire |
|---|---|
| La réponse et ses limites | `03_LIVRABLES/L8_Conclusion_independante.md` |
| Le coût annuel réel | `03_LIVRABLES/L1_Cout_annuel_reel.md` |
| Toutes les manières de financer | `03_LIVRABLES/L2_Analyse_des_financements.md` |
| Les 5 modèles les plus prometteurs | `03_LIVRABLES/L3_Cinq_modeles_prometteurs.md` |
| La solution modélisée sur 20 ans | `03_LIVRABLES/L4_Solution_modelisee_20_ans.md` |
| La démonstration de la couverture | `03_LIVRABLES/L5_Demonstration_couverture.md` |
| La résistance aux crises | `03_LIVRABLES/L6_Resistance_aux_crises.md` |
| Le plan d'action | `03_LIVRABLES/L7_Feuille_de_route.md` |
| Le modèle chiffré | `02_MODELE/sorties/Modele_equation_chateau.xlsx` (feuille « Lisez-moi ») |

---

## Organisation du dossier

| Dossier | Contenu |
|---|---|
| `00_PILOTAGE/` | Brief, contexte permanent, règles des agents, plan de recherche, cadre analytique, consignes des agents, journal, état de reprise |
| `01_RECHERCHE/` | 13 rapports de recherche : vague 1 (R1 à R8) et vague 2 (V2A, V2C, V2D, V2V, V2R), avec leurs registres de sources dans `sources/` |
| `02_MODELE/` | Le modèle en Python et le classeur Excel généré, recalculé et vérifié (`sorties/`) |
| `03_LIVRABLES/` | Les huit livrables L1 à L8 |
| `04_SOURCES/` | Registre consolidé des sources (`Registre_sources.csv`, 636 sources de la vague 1 et de la vague 2 hors équipe rouge) et sa synthèse |

---

## Le modèle (`02_MODELE/`)

**Contenu du classeur** `sorties/Modele_equation_chateau.xlsx` :
- **Hypothèses** : chaque hypothèse en trois cas (favorable, central, défavorable), avec son statut (SOURCÉ, ESTIMATION, HYPOTHÈSE), ses sources et une note.
- **Budget** des trois domaines types.
- **Moteurs** de revenus et **modèles** économiques.
- **Projections** et **stress tests** sur 20 ans.
- **Sources**.

Chaque cellule calculée est une formule. Le classeur compte 11 301 formules, recalculées par LibreOffice et comparées une à une à un calcul Python indépendant : 0 erreur, 0 écart.

**Reconstruire et vérifier :**
```bash
cd 02_MODELE
python3 construire_modele.py   # construit le classeur, le recalcule, vérifie chaque cellule et le jumeau Monte-Carlo
python3 calculer_mc.py         # simulations de Monte-Carlo (dotations, ruptures, distributions, comparaison des modèles)
python3 sensibilite.py         # sensibilité du besoin, hypothèse par hypothèse
python3 tableaux.py            # tableaux Markdown repris dans les livrables (sorties/tableaux.md)
```

**Rôle de chaque fichier :**
- `parametres_scenarios.py`, `parametres.py`, `moteurs.py`, `modeles.py` et `projection.py` contiennent les hypothèses et les formules.
- `monte_carlo.py` est le jumeau stochastique de la projection : sans chocs, il la reproduit exactement.

**Modifier une hypothèse :**
- dans le classeur (cellules bleues de la feuille Hypotheses), les résultats déterministes se recalculent aussitôt ;
- pour mettre à jour les probabilités, modifier la même valeur dans les fichiers Python et relancer les scripts.

---

## Conventions d'honnêteté

- Aucun chiffre, aucune transaction, aucun client et aucune preuve de rentabilité n'a été inventé. Ce qui n'a pas été trouvé est marqué **INCONNU**.
- Chaque hypothèse porte un statut :
  - **SOURCÉ** : page lue, chiffre cité ;
  - **ESTIMATION** : raisonnement sur des sources ;
  - **HYPOTHÈSE** : choix de modélisation à valider.
- Les sources sont identifiées entre crochets (par exemple [R1-05]) et répertoriées dans `04_SOURCES/Registre_sources.csv`, avec leur statut (page lue ou simple extrait) et leur fiabilité.
- Une vérification indépendante de 90 chiffres clés (V2V) n'a trouvé aucun chiffre faux, et a nuancé 9 chiffres. Une équipe rouge (V2R) a attaqué le modèle et les livrables.
- Les montages juridiques et fiscaux sont des pistes **à faire valider** par un avocat fiscaliste, un notaire et un expert-comptable. Ce dossier n'est pas un conseil juridique, fiscal ou financier.
- Aucune démarche n'a été engagée pendant la mission : aucun contact avec des tiers, aucune dépense, aucune opération réelle.
