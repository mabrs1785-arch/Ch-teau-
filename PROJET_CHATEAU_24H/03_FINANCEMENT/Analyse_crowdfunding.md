# Analyse du financement participatif et du mécénat — Opération Château v2 (Agent 2)

Date : 2026-10-14. Sources : `_brut/sources_agent2.csv`.
Statuts : PAGE LUE / EXTRAIT / ESTIMATION / INCONNU. Les pages sont lues via `curl` (WebFetch en échec DNS).

> Règle du brief : ne jamais confondre **crowdfunding, dons, préventes, mécénat et investissement financier**. Ce sont 7 objets juridiques différents, avec des contributeurs différents et des droits différents. **Aucune campagne n'a été lancée ni testée, et aucun contributeur n'a exprimé d'intérêt.**

---

## 1. Typologie : qui donne quoi, contre quoi ?

| Forme | Nature juridique | Le contributeur reçoit | Rendement financier | Défiscalisation du contributeur | Cadre | Pertinence pour le château |
|---|---|---|---|---|---|---|
| **Don pur** | libéralité | rien (ou un remerciement) | aucun | **non**, sauf si l'organisme est éligible (voir mécénat) | droit civil | faible, sauf récit de sauvetage |
| **Don avec contrepartie** (récompense) | don ou vente de prestations | objet, visite, nom gravé | aucun | non (en principe) | plateformes de dons | communauté, notoriété, petits montants |
| **Prévente** | contrat de vente ou de prestation à exécution différée | prestation future (pension, stage, nuitée, mariage) | aucun, mais réduction de prix possible | non | droit de la consommation | **utile pour la trésorerie de lancement**. C'est une **dette** envers le client si la prestation n'est pas rendue |
| **Mécénat** (particuliers art. 200, entreprises art. 238 bis, via la **Fondation du patrimoine** pour un MH privé) | don à un organisme éligible qui subventionne les travaux | reçu fiscal, contreparties limitées | aucun | **oui** : 66 % (particulier), 75 % (IFI, ≤ 50 000 €), 60 % (entreprise, ≤ 20 000 € ou 0,5 % du CA) (S16, PAGE LUE) | CGI, convention avec la Fondation (S14) | **seulement si recettes commerciales ≤ 60 000 € HT/an** ou entreprise agricole (S14, PAGE LUE) |
| **« Co-châtelain »** (modèle Dartagnans) | **actions d'une SAS** propriétaire du château, souscrites pour 50-100 € | droit de vote, accès, visites, AG | **aucun dividende annoncé** dans les sources lues | non | droit des sociétés. Hors PSFP si la plateforme n'est pas agréée : **régime à vérifier par l'Agent 6** | possible pour l'achat d'une ruine « à sauver ». **Récit faible si le fondateur y habite** |
| **Crowdequity** (actions ou parts avec espérance de gain) | titres financiers | dividendes éventuels, plus-value à la sortie | **espéré, non garanti** | possible (IR-PME / « jusqu'à 50 % » affiché par Lita, S29). **Éligibilité d'une société immobilière ou patrimoniale non vérifiée** | **PSFP**, règlement (UE) 2020/1503 | faible : rendement d'exploitation insuffisant (voir Montages §5) |
| **Crowdlending / obligations / minibons** | titres de créance ou prêts | intérêts + remboursement | **7-12 % affichés** (S27, S30, S36) | non. Intérêts au **PFU de 31,4 % depuis le 01/01/2026** (S25, PAGE LUE) | PSFP | **le plus utilisé pour les châteaux** (Fontenay/Bricks, S36). Coût élevé, remboursement court |
| **Royalties** | contrat de redevance sur le chiffre d'affaires | % du CA pendant N années | variable | non | **INCONNU** (page Tudigo inaccessible ce jour) | intéressant pour l'événementiel, **non vérifié** |

---

## 2. Cadre réglementaire PSFP (prestataires de services de financement participatif)

| Règle | Contenu | Statut |
|---|---|---|
| Texte | règlement (UE) 2020/1503, applicable depuis le 10/11/2021. Agrément PSFP délivré par l'AMF, passeport européen | PAGE LUE (S21, S22). Texte EUR-Lex non ouvrable (challenge anti-robot) |
| Plafond | **5 M€ par porteur de projet sur 12 mois**, sans prospectus (ancien régime français : 8 M€) | PAGE LUE (S21, S22) |
| Investisseur non averti | test de connaissances ; **simulation de la capacité à supporter des pertes** ; au-delà de **1 000 € ou 5 % du patrimoine net** par projet, avertissement spécifique, consentement explicite et preuve de compréhension | PAGE LUE (S21) |
| Délai de réflexion | **4 jours** précontractuels pour les non avertis | PAGE LUE (S21) |
| Fiche d'informations clés | **INCONNU** dans mes sources lues (à vérifier dans le texte officiel) | — |

**Conséquence pour le projet** : une levée unique couvrant **un château à 5 M€ + travaux** dépasse le plafond PSFP. Il faudrait l'étaler sur 2 exercices, ou passer par un prospectus ou un placement privé. Au cas central (≈ 4,4 M€), une levée PSFP **partielle** est la seule réaliste (ESTIMATION).

---

## 3. Plateformes réelles (pages lues le 2026-10-14)

| Plateforme | Ce qu'elle fait | Chiffres affichés | Statut | Pertinence pour le projet |
|---|---|---|---|---|
| **Dartagnans** | achat collectif de châteaux (actions de SAS), dons, événements (Nuit des châteaux) | **6,8 M€ collectés, 7,9 M€ investis, + 50 000 co-châtelains de 183 pays**. Châteaux affichés : Mothe-Chandeniers et Boulogne-la-Grasse | PAGE LUE (S32) | la plus spécialisée, mais elle achète **pour son propre compte**. Ce n'est pas un financeur d'un projet tiers |
| **Bricks** | obligations immobilières **dès 10 €** | taux affichés **10,5-11 % fixes**, montant total affiché 449 134 364 € (libellé exact non vérifié) | PAGE LUE (S30) | **précédent château : Fontenay (S36)** |
| **Anaxago** | immobilier (dette et fonds propres), PME, fonds | **684 M€ dans 280 opérations immobilières, 178 cessions, 5 pertes constatées, TRI net constaté 8,7 %** (auto-déclaré, données au 12/10/2026) | PAGE LUE (S26) | marchands de biens et promoteurs. Un château événementiel est hors cible probable (ESTIMATION) |
| **Homunity** | crowdfunding immobilier, immobilier fractionné | rendements cibles **5 à 12 %**. « les obligations ne sont pas garanties » | PAGE LUE (S27) | idem Anaxago |
| **WiSEED** | actions et obligations (immobilier, transition énergétique, entreprises) | **580 M€ investis, 320 M€ remboursés**, rendement « jusqu'à 12 % » | PAGE LUE (S28) | possible pour une OpCo (obligations) |
| **LITA** | investissement à impact (actions, obligations jusqu'à 11 %) | « +230 m€ » | PAGE LUE (S29) | si l'angle impact (patrimoine, emploi rural) est crédible |
| **MiiMOSA** | **agricole et alimentaire** : dons avec contreparties, prêts rémunérés | « jusqu'à 10 % d'intérêts », **200 M€ dans 8 000 projets**, fonds de dette de 50 M€ | PAGE LUE (S31) | **pertinent pour la partie équestre**, puisque l'équestre est une activité agricole depuis 2005 (S45). Éligibilité à confirmer auprès de MiiMOSA |
| **Fondation du patrimoine** | collecte de dons défiscalisés pour un monument, label, Loto du patrimoine | Mission Patrimoine 2025 : **29,1 M€**, ≤ **300 000 € par site** (S17) | PAGE LUE (S14, S17) | **verrou à 60 k€ de recettes commerciales** |
| **Tudigo** | (royalties et prêts, d'après ma connaissance générale) | — | **INCONNU** : page inaccessible (404 puis échec réseau) | non évaluable |

---

## 4. Campagnes réelles concernant des châteaux

| Château | Année | Plateforme / forme | Montant | Contributeurs | Droits des contributeurs | Issue connue | Statut |
|---|---|---|---|---|---|---|---|
| **La Mothe-Chandeniers** (Vienne), ruine non protégée | 2017 | Dartagnans + association Adopte un château. **Actions de SAS** (≥ 51 € = actionnaire, < 51 € = donateur) | prix **500 000 €**. Collecte finale **> 1,6 M€**. Restauration complète ≥ 3 M€ selon Dartagnans | ≈ 19 000 contributeurs, ≈ **25 000 copropriétaires** de 115 pays | conseil d'administration, **AG annuelle**, comité exécutif, visites réservées, webcams. **Aucun dividende mentionné** | Écolodges et gîtes, étoile au Guide Vert (lien Dartagnans). Fonds de dotation **suspendu en 2023** puis autorisé à reprendre. Le dirigeant déclarait en déc. 2025 : « **On est très légèrement bénéficiaires pour la première fois** » | PAGE LUE (S33, S34, S51, S53) |
| **Boulogne-la-Grasse** (Oise) | 2022 → en cours | Dartagnans, actions (« **co-propriétaire pour 59 €** ») | INCONNU | ≈ 6 000 en 2022, « près de 7 500 » en 2026 | statut de co-châtelain | page 2026 : « **Dernières échéances pour conclure l'achat** », ce qui suggère un **paiement échelonné du prix** (non vérifié) | PAGE LUE (S52, S54, S32) |
| **Vibrac** (Charente), **l'Ebaupinay** (Deux-Sèvres) | avant 2022 | Dartagnans | INCONNU | INCONNU | INCONNU | cités comme « acquis » en 2022 (S52), **absents de la page d'accueil 2026** (S32). Sort **INCONNU**, à vérifier (registre, BODACC) | PAGE LUE (absence constatée) |
| **Château du Theil** (Corrèze), projet d'hôtel 4★ de 14 chambres | ≈ 2020-2023 (date exacte INCONNUE) | Dartagnans, **actions** (mise de base 100 €) | **≈ 1 M€** | ≈ **300 actionnaires** | « accéder librement et gratuitement au domaine, à vie » | ouverture annoncée « dans un an », issue INCONNUE | PAGE LUE (S35) |
| **Château Fontenay** (Sarthe), MH, 11,6 ha, hôtel et réceptions | déc. 2023 | **Bricks, obligations** dès 10 € | **690 000 €**. Titre du communiqué : « ils lèvent 310 000 € en 12 h ». Valeur du bien ≈ 2 M€ | INCONNU | **7 % fixe**, liquidité visée au **31/01/2029**, « objectif … doubler leur investissement » (formule de l'émetteur) | **INCONNUE** : aucun suivi de remboursement trouvé | PAGE LUE (S36) |
| **Chantilly** (Oise), domaine historique avec Grandes Écuries | 2026 | appel à la générosité du public | **68 M€** de besoins sur 10 ans. Financement de l'Aga Khan arrêté fin 2020 | — | dons | en cours | PAGE LUE (S38) |

**Moyennes observées** (ESTIMATION) :
- Mothe : 1,6 M€ / ≈ 19 000 contributeurs ≈ **85 € par contributeur** (masse, ticket minuscule).
- Theil : 1 M€ / 300 ≈ **3 300 € par actionnaire** (petit cercle, ticket moyen).

Il existe donc **deux modèles**, la **foule** et le **cercle**, et le second est le plus compatible avec un projet entrepreneurial.

---

## 5. Taux de défaut publiés (crowdlending immobilier)

| Indicateur | Valeur | Source / statut |
|---|---|---|
| Projets avec retard **> 6 mois** (S1 2025) | **20-25 %** | baromètre Forvis Mazars via ABC Bourse, PAGE LUE (S23) |
| Retard < 6 mois | 8-10 % | idem |
| Procédures collectives | **10-15 %** (S23) / **20-25 %** (S24). **Divergence entre sources secondaires** | PAGE LUE (S23, S24) |
| Pertes définitives | **4-6 %** (S1 2025), contre 2-4 % en 2024 et 0-2 % en 2023 | PAGE LUE (S23) |
| HelloCrowdfunding mi-2024 | **53,06 % en retard, 31,64 % en défaut (> 12 mois)** | PAGE LUE via CPIM (S25), source primaire non lue |
| Collecte immobilière 2024 | **860 M€ (-25,8 %)**. S1 2025 : 388,2 M€ contre 459 M€ (-15 %) | PAGE LUE (S25, S23) |
| Médiation AMF | demandes liées au crowdfunding immobilier **triplées en 2024** | PAGE LUE (S23) |
| Anaxago (auto-déclaré) | 5 pertes constatées sur 178 cessions (280 opérations), TRI net 8,7 % | PAGE LUE (S26) |

**Lecture pour le projet** : les investisseurs du crowdlending ont été échaudés par les **promoteurs**. Un château événementiel, qui est un **actif d'exploitation**, sans prévente de lots et avec un porteur jeune, se placera **au-dessus** du risque moyen. Il faut donc s'attendre à un **coupon de 8-11 %** (ESTIMATION à partir des taux affichés S27, S30), à des **sûretés réelles** exigées par la plateforme et à des **montants plafonnés** autour de 0,5-0,7 M€ (précédent Fontenay).

---

## 6. Ce que chaque forme peut financer dans le projet (ESTIMATION)

| Besoin | Forme adaptée | Montant réaliste | Condition |
|---|---|---|---|
| Achat d'une ruine ou d'un château « à sauver » | co-châtelains (actions sans rendement) | 0,5-1,6 M€ (Mothe, Theil) | récit de sauvetage, pas de résidence privée visible. Partenaire installé (Dartagnans) ou communauté propre |
| Travaux sur parties MH | dons via la Fondation du patrimoine + Mission Patrimoine | ≤ 300 k€ (Mission, S17) + collecte | **≤ 60 k€ de recettes commerciales/an** ou exception agricole. Ouverture 40-50 j/an. Conservation 10 ans, **y compris des titres des associés** (S14) |
| Écuries, carrière, matériel équestre | MiiMOSA (prêt ou don avec contreparties), crédit-bail | 15-500 k€ (fourchette affichée sur la page MiiMOSA, S31, nature exacte non vérifiée) | activité agricole réelle (S45) |
| Aménagements événementiels / hébergement | obligations PSFP (Bricks, WiSEED, LITA) | 0,3-0,7 M€ | coupon 7-11 %, remboursement à 3-5 ans. **Mur de refinancement** |
| Trésorerie de lancement | **préventes** : pensions prépayées, cartes de membre du club, mariages avec acomptes | 50-200 k€ | ce sont des **dettes clients**. Ne pas les consommer pour des travaux |
| Mécénat d'entreprises locales | 238 bis via la Fondation du patrimoine | quelques k€ à 20 k€ par entreprise (plafond 20 000 € ou 0,5 % du CA, S16) | mêmes verrous que les dons ; contreparties ≤ 25 % (règle usuelle, **non vérifiée** ici) |

**Plafond cumulé raisonnable** : **≈ 1-2 M€ hors dette bancaire** (ESTIMATION), si et seulement si le récit, l'ouverture au public et la gouvernance sont acceptés. C'est **insuffisant seul** pour 2-5 M€ d'acquisition et de travaux. Le financement participatif est un **complément**, pas la colonne vertébrale.

---

## 7. Incompatibilités à arbitrer

1. **Résidence privée et argent de la foule.** Les donateurs et co-châtelains financent un **bien commun**. Un fondateur qui y habite crée un **conflit visible**. Il faut un logement séparé, payé au prix du marché, ou un récit clair.
2. **Événementiel et dons défiscalisés.** Au-delà de 60 k€ HT de recettes commerciales sur le site, **tous** les dons via la Fondation tombent, quelle que soit la société exploitante (S14).
3. **Dons défiscalisés et liquidité des associés.** Si une société détient l'immeuble, **tous les porteurs de parts** doivent conserver leurs titres 10 ans (S14). C'est incompatible avec des investisseurs qui veulent sortir.
4. **Crowdequity et régime MH.** Une société à l'IS avec des tiers perd la déduction MH sur le revenu global (156 bis, S13).
5. **Contrôle.** Le modèle Dartagnans montre une gouvernance lourde (AG, conseil, comité) et des « turbulences » (S51). Un fondateur minoritaire face à des milliers d'actionnaires **ne contrôle pas durablement** le château, sauf statuts très protecteurs (actions de préférence), juridiquement possibles mais contestables.

---

## 8. Recommandation (ESTIMATION)

- Ne **pas** fonder l'acquisition sur la foule. Utiliser :
  - les **préventes** pour la trésorerie ;
  - **MiiMOSA ou un équivalent** pour l'équipement équestre agricole ;
  - un **cercle de co-investisseurs** de 50 à 300 personnes, sur le modèle du Theil, avec des **droits d'usage clairs** (pension, accès, événements) plutôt qu'un rendement promis ;
  - les **dons via la Fondation du patrimoine** uniquement sur un **périmètre non commercial** (chapelle, façades, parc), si le seuil de 60 k€ et l'ouverture au public sont tenables.
- Si l'événementiel doit dépasser 60 k€ de recettes : **renoncer aux dons** et financer les travaux par la dette, les subventions publiques directes (DRAC, Région, montants INCONNUS) et la Mission Patrimoine (≤ 300 k€, avec ses propres règles).
- Toute levée de titres passe par un **PSFP agréé** et un **conseil juridique** (Agent 6).

---

## 9. Points de doute / hypothèses non vérifiées

1. Le texte officiel du règlement 2020/1503 n'a pas été ouvert (EUR-Lex bloqué). Les règles sont lues chez 2 cabinets d'avocats (S21, S22). La page AMF consultée n'affichait pas de contenu (rendu JavaScript).
2. **Statut juridique de l'offre « co-châtelain »** au regard du droit des offres au public de titres : non vérifié. Commission Dartagnans « ≈ 8 % » selon Que Choisir 2021 (S37, article partiellement lu).
3. **Sort de Vibrac et de l'Ebaupinay** (Dartagnans) inconnu. Leur absence de la page d'accueil 2026 peut signifier une cession, une sortie de portefeuille ou un simple choix éditorial.
4. **Issue de Fontenay (Bricks)** inconnue. Remboursement 2029 non échu.
5. Taux de défaut : les sources sont **secondaires** (blogs, presse) reprenant Forvis Mazars et HelloCrowdfunding. La divergence sur les procédures collectives (10-15 % contre 20-25 %) n'est pas résolue.
6. Royalties (Tudigo) : non vérifié.
7. Éligibilité MiiMOSA d'une activité équestre de pension, d'enseignement ou d'élevage : non vérifiée.
8. Doctrine Fondation du patrimoine datée de 2012 (S14) : à recouper avec le CGI et la loi en vigueur.
9. Aucune campagne, aucun contributeur et aucun intérêt réel n'ont été testés. Les montants du §6 sont des **ordres de grandeur** tirés de précédents, **pas des prévisions**.
