# Vérifications — Vague 2 (chiffres critiques du modèle financier)

> Agent : Vague 2 — vérification. Date : 2026-10-14.
> **Méthode et limite majeure** : WebFetch et curl sont bloqués (vérifié une fois : `getaddrinfo ENOTFOUND` sur chevaux-normandie.com). Seul WebSearch a fonctionné : **45 recherches** effectuées. Tous les chiffres viennent des **extraits de résultats de recherche** et non de la lecture intégrale des documents. Fiabilité plafonnée à « moyenne », même pour les sources officielles (notée « haute » dans le CSV quand le document est officiel et l'extrait sans ambiguïté, mais à relire).
> Sources : `_brut/sources_vague2.csv` (identifiants V2-xx).
> Légende statut : **FAIT SOURCÉ** (extrait de recherche, URL citée) / **ESTIMATION** (raisonnement explicite) / **INCONNU** (« Je ne sais pas »).

---

## 1. Charges annuelles réelles d'un château privé

| Poste | Valeur trouvée | Année | Source (id) | Statut / fiabilité |
|---|---|---|---|---|
| Entretien total (fourchette générale) | 20 000 à 150 000 €/an selon taille | non datée (article SeLoger) | V2-01 | FAIT SOURCÉ, faible (non étayé) |
| Entretien total (agence) | « plus de 20 000 à 100 000 €/an » selon taille | non daté | V2-05 Capifrance | FAIT SOURCÉ, faible |
| Énergie (chauffage+gaz+élec.), château de Meung-sur-Loire | 15 000 à 20 000 €/an « d'habitude » (avant crise 2022) | 2022 | V2-02, V2-03 (AFP) | FAIT SOURCÉ, moyenne |
| Énergie château Cheverny | 30 000 à 40 000 litres de fioul/an | 2022 | V2-03 | FAIT SOURCÉ, moyenne (grand site ouvert au public) |
| Énergie « petit à moyen château » | 15–20 k€ avant 2022 ; 40–50 k€ après | non daté | V2-04 Selectra | FAIT SOURCÉ, faible (acteur commercial) |
| Taxe foncière — château MH Liettres (62), 14 pièces, parc 6,5 ha | 2 652 €/an | annonce (date à vérifier) | V2-06 | FAIT SOURCÉ, moyenne (déclaratif vendeur) |
| Assurance — même château | ~2 200 €/an | idem | V2-06 | FAIT SOURCÉ, moyenne (déclaratif vendeur) |
| Chauffage — même château | 8 000 €/an ; ~1 500 €/an après géothermie (investissement 33 000 €) | idem | V2-06 | FAIT SOURCÉ, moyenne |
| Personnel — même château | ~4 160 €/an | idem | V2-06 | FAIT SOURCÉ, moyenne |
| Taxe foncière — château La Rochebeaucourt (24), annonce 2 750 000 € | 4 038 € TF + 2 343 € TH | annonce | V2-14 | FAIT SOURCÉ, faible (URL exacte de l'extrait incertaine) |
| Assurance château (courtier) | 15 000 à 30 000 €/an pour 600–1 200 m² (≈ 5 ‰ de la valeur assurée) ; ailleurs 10 000 à 50 000 € ; surcoût MH +30 à 50 % | 2025-2026 | V2-07, V2-08 France Epargne | FAIT SOURCÉ, faible (site commercial, chiffres internes contradictoires) |
| Jardinier (salaire) | 13,36 €/h brut, soit 2 025,99 €/mois brut (saisonnier, La Roche-Guyon 2025) ; 2 500–3 500 €/mois (CDI Porto-Vecchio) | 2025 | V2-12, V2-13 | FAIT SOURCÉ, moyenne |
| Ratio jardinier/surface | 1 jardinier pour 4 ha d'espaces verts (offre château de Champchevrier, 37) | 2025 | extrait recherche France Travail (URL exacte non isolée) | FAIT SOURCÉ, faible |
| Règle empirique gros entretien | ~1 % de la valeur/an (bien récent <1 %, ancien non rénové ~2 %) | — | V2-11 UBS | FAIT SOURCÉ (général, pas château), moyenne |
| Seuil de rentabilité visites | Sites patrimoniaux moyens « quasi impossibles à rentabiliser » sous 50 000–100 000 visiteurs/an ; toujours négatif sous 10 000 visiteurs payants | 2019 | V2-10 Demeure Historique | FAIT SOURCÉ, moyenne |
| Hôtels-châteaux | « la majorité des hôtels-châteaux de moins de 15 chambres opèrent sous leur seuil de rentabilité » | 2025 | V2-09 | FAIT SOURCÉ, faible (cabinet non nommé) |

**Ce que je ne sais pas** : aucun témoignage chiffré complet (toutes charges) d'un propriétaire privé français n'a été trouvé ; aucune étude Demeure Historique / VMF donnant une dépense moyenne. Coût d'entretien d'un parc au €/ha : **Je ne sais pas** (vérifier : bordereaux de prix de marchés publics d'espaces verts, devis paysagistes, fiche DREAL PACA « coût global – végétation »).

**ESTIMATION (pour le modèle, à remplacer par des devis)** — château 600–1 000 m², 50 ha, non classé :
- Taxe foncière : 3 000–8 000 €/an (les 2 exemples d'annonces sont à 2,6 k€ et 4 k€ ; hypothèse prudente au-dessus car communes rurales à taux élevés).
- Assurance : 5 000–15 000 €/an (entre l'annonce à 2,2 k€ et le courtier à 15–30 k€ ; hypothèse : valeur assurée 1,5–3 M€ × 3–5 ‰).
- Énergie : 15 000–40 000 €/an (fourchette AFP/Selectra).
- Gros entretien : 1,5–2 % de la valeur bâtie/an (règle UBS « ancien », majorée), soit 15–30 k€ pour un bâti valorisé 1–1,5 M€.
- Parc : 1 ETP jardinier ≈ 35–40 k€ chargé/an (ESTIMATION : 2 025–2 500 € brut × 12 × ~1,45 de charges ; coefficient non sourcé ici).
- **Total charges de propriété (hors dette, hors exploitation) : ~75 000–135 000 €/an**, cohérent avec la fourchette SeLoger 20–150 k€.

## 2. Fermage et prix des terres

| Donnée | Valeur | Année | Source | Statut |
|---|---|---|---|---|
| Indice national des fermages | 123,06 (+0,42 %), échéances 1/10/2025–30/9/2026 | 2025 | V2-21, V2-22 | FAIT SOURCÉ, haute |
| Allier : arrêté | AP 2019/2025 du 26/09/2025 entérine l'indice — **minima/maxima €/ha non trouvés** | 2025 | V2-21 | INCONNU pour les valeurs |
| Orne, Loire-Atlantique, Indre : minima/maxima 2025 | **Je ne sais pas** (arrêtés non remontés par la recherche) | — | — | INCONNU |
| Indre (ancien) | max 156,39 €/ha pour une catégorie | 2014 | V2-23 | FAIT SOURCÉ, moyenne (obsolète) |
| Exemples d'autres départements (ordre de grandeur) | Île-de-France terres sans bâtiment : A 105,29–139,01 ; B 84,24–120,06 ; C 47,70–96,05 €/ha. Creuse : 52,84–202,87 €/ha. Aveyron pâtures max 170,85 €/ha (point 2,01 €). Drôme polyculture-élevage max 174 €/ha | 2025 | V2-22, V2-24, extraits Réussir/Drôme | FAIT SOURCÉ, moyenne |
| Prix terres et prés libres — France | 6 460 €/ha (+0,9 %) ; loués 5 350 €/ha ; zones élevage bovin 4 740 €/ha (-1 %) ; grandes cultures 8 150 €/ha | 2025 | V2-15 (Safer via Terre-net) | FAIT SOURCÉ, moyenne+ |
| Orne | 7 260 €/ha | **2022** | V2-16 | FAIT SOURCÉ, moyenne (ancien) |
| Normandie (libres) | 9 340 €/ha | 2024 | V2-17 | FAIT SOURCÉ, moyenne |
| Allier (moyenne départementale) | 4 050 €/ha (Bocage bourbonnais 3 540 ; Val d'Allier 6 030) | 2024 | V2-18 | FAIT SOURCÉ, faible (libre/loué non précisé) |
| Centre-Val de Loire (libres) | 6 670 €/ha (2024) ; -6,1 % en 2025 | 2024-25 | extrait Safer/Terre-net | FAIT SOURCÉ, moyenne |
| Indre, Loire-Atlantique 2025 | **Je ne sais pas** (tableau Pleinchamp V2-20 / le-prix-des-terres.fr non extrait) | — | — | INCONNU |
| Herbe sur pied | 40–65 €/t MS (prix planchers, Pays de la Loire) ; pour prairie non entretenue par le propriétaire, la vente d'herbe ≈ le prix du fermage | 2017 / 2024 | V2-26, V2-25 | FAIT SOURCÉ, moyenne |
| Risque juridique vente d'herbe | Requalification en bail rural si répétée au profit du même acquéreur | 2025 | V2-27 | FAIT SOURCÉ, moyenne |
| Pension au pré chevaux (Oise) | 130–220 €/mois/cheval, chargement 2 chevaux/ha | 2020 | V2-28 | FAIT SOURCÉ, moyenne |

**ESTIMATION** : loyer de prairies dans les 4 départements visés ≈ 80–180 €/ha/an (fourchette des grilles d'autres départements 2025 ; hypothèse non vérifiée pour 61/03/44/36). 50 ha loués = 4 000–9 000 €/an : recette marginale. À l'inverse, valoriser l'herbe via la pension au pré (2 chevaux/ha × 130–220 €/mois × 6 mois) rapporte 3 100–5 300 €/ha/an de chiffre d'affaires brut, mais avec charges et main-d'œuvre.
Comment vérifier : arrêtés préfectoraux « valeurs locatives des baux ruraux 2025-2026 » sur les sites des préfectures (recueil des actes administratifs) et DDT 61, 03, 44, 36 ; le-prix-des-terres.fr pour les barèmes départementaux.

## 3. Location d'écuries à un cavalier professionnel

| Donnée | Valeur | Année | Source | Statut |
|---|---|---|---|---|
| Location écurie complète (Allemagne, Lüneburger Heide) | 3 600 € HT/mois pour 10 boxes + paddocks + terres + appartement (≈ 360 €/box/mois tout compris) | annonce (date à vérifier) | V2-29 | FAIT SOURCÉ, faible (étranger, traduction auto) |
| Écurie partagée (Normandie, EKIT) | Location de 11 stabulations + accès manège/carrière par planning, **bail agricole** ; loyer non publié | 2024 | V2-30 | FAIT SOURCÉ (modèle), loyer INCONNU |
| Réservation d'un box en absence (contrat de pension type) | 100 €/mois | non daté | V2-33 | FAIT SOURCÉ, faible |
| Pension box sans travail | 250–420 €/mois (IFCE, données anciennes) | 2015 | V2-31 | FAIT SOURCÉ, moyenne (ancien) |
| Pension box-paddock (centre équestre) | 435 €/mois | 2024-25 | V2-34 | FAIT SOURCÉ, moyenne |
| Pension travail chevaux de sport | ~580 €/mois hors déplacement et location de box (850 €/mois total) | non daté | V2-32 | FAIT SOURCÉ, moyenne |
| Cas type « Écurie de pension CSO » 2025 | 37 ha, 2,5 UMO, 43 équidés, ~30 pensions (2/3 avec travail), ~30 concours/an ; **chiffres économiques non lus** | 2025 | V2-35 | partiel |

**Loyer par box/mois en France pour un pro : Je ne sais pas.** ESTIMATION de travail : 100–250 €/box/mois box nu avec accès aux installations (borne basse = « réservation » 100 € ; borne haute ≈ 2/3 de l'exemple allemand tout compris). 20 boxes loués = 24–60 k€/an. À vérifier : annonces Leboncoin « location écurie », Cheval Annonce, Chambres d'agriculture (réseau REFErences équin), PDF du cas type CSO 2025.

## 4. Loyer d'un domaine / château en bail longue durée

| Exemple | Loyer | Rapport loyer/valeur | Source | Statut |
|---|---|---|---|---|
| Maison Fournaise, Chatou (MH, restaurant) — BEA 20 ans (2019) | 80 000 €/an fixe + 7 % du CA | valeur non connue | V2-36 | FAIT SOURCÉ, haute |
| Château de Montfort, Besançon — bail 18 ans (2005) | 22 945,50 €/an indexé ICC | non connue | V2-37 | FAIT SOURCÉ, haute (ancien) |
| Château de la Neuenbourg, Guebwiller — BE à collectivité | 1 €/an symbolique contre projet de travaux ~3 M€ | n/a | V2-38 | FAIT SOURCÉ, haute |
| Château-hôtel Châteauroux (annonce de vente) | > 45 000 €/an de loyers + > 50 000 €/an d'activité hôtelière | prix de vente non extrait | V2-39 | FAIT SOURCÉ, faible |
| Château de Bourgogne, Estaimpuis (BE) — appel à candidatures bail commercial salle 300 places | loyer non extrait | — | V2-40 | partiel |

**Location-gérance d'un château-hôtel : Je ne sais pas** (aucune annonce avec redevance trouvée). **Rapport loyer/valeur pour un château : Je ne sais pas.**
Enseignement utile (FAIT) : les collectivités propriétaires de châteaux pratiquent des baux emphytéotiques où le preneur finance les travaux en échange d'un loyer faible voire symbolique (Neuenbourg). C'est une voie de « contrôle durable » sans achat à étudier (scénario S1).
ESTIMATION : en bail commercial privé, un rendement brut de 3–5 % de la valeur serait l'ordre de grandeur de l'immobilier professionnel, mais non vérifié pour les châteaux, souvent loués bien en dessous car le preneur porte l'entretien.

## 5. Commissions Arqana / Fences / ventes de sport

| Vente | Commission | Source | Statut |
|---|---|---|---|
| Arqana Trot — vendeur | 7,5 % HT du prix (+ TVA 5,5 % ou 20 %) ; rachat par le vendeur : 2,5 % HT de la plus haute enchère ; paiement vendeur à 30 jours ouvrés, garanti à 45 jours | V2-41 | FAIT SOURCÉ, moyenne |
| Arqana (galop) — acheteur | TVA sur prix + commission, taux **non extrait** ; Arqana reverse 5 % à l'agent/entraîneur ayant enchéri pour l'acheteur | V2-42 | partiel / INCONNU pour le taux |
| Arqana (galop) — vendeur yearlings | **Je ne sais pas** (page vendor_information non extraite) | V2-43 | INCONNU |
| Fences (chevaux de sport) | **Je ne sais pas** (conditions de vente sur Calaméo, taux non extraits) | V2-44 | INCONNU |
| Vente aux enchères BWP (Belgique, comparatif) | adjudication majorée de 10 % pour l'acheteur + TVA | V2-45 | FAIT SOURCÉ, moyenne |

Vérifier : conditions générales de vente sur arqana.com et fences.fr (section frais), catalogue de la vente visée.

## 6. Budget d'organisation d'un CSO FFE

| Donnée | Valeur | Source | Statut |
|---|---|---|---|
| Recettes d'engagement par cheval (Club/Amateur/Pro) | **Je ne sais pas** (aucun avant-programme FFE remonté ; résultats tunisiens/golf hors sujet) | — | INCONNU |
| Taille d'un CSO amateur/pro régional | Ouistreham 2017 : 400 cavaliers amateurs et pros, 5 000 spectateurs, Pro 2 ; Porticcio : > 130 cavaliers amateur/pro, Pro 2 à 1,30 m | V2-46, V2-47 | FAIT SOURCÉ, moyenne |
| Coûts (jury, chef de piste, vétérinaire, dotations, redevance FFE) | **Je ne sais pas** | — | INCONNU |

Vérifier : avant-programmes publiés sur FFE Compet (ffecompet.ffe.com), règlement des compétitions FFE (dispositions spécifiques CSO : dotations minimales, plafonds d'engagement), budget d'un comité départemental ou d'un club organisateur.
ESTIMATION non sourcée (ne pas utiliser sans vérification) : un week-end de 300–400 partants à ~25–50 € d'engagement donnerait 7 500–20 000 € de recettes d'engagements, avant dotations et officiels ; marge nette probablement faible, intérêt surtout d'image et de remplissage de boxes.

## 7. Apport exigé et LTV

| Donnée | Valeur | Source | Statut |
|---|---|---|---|
| Apport prêt professionnel (courtier) | 30 % création ; 20 % reprise ; 10 % achat/construction de murs commerciaux | V2-48 Cafpi | FAIT SOURCÉ, moyenne |
| Mode de calcul | apport / besoin global (investissements + BFR) | V2-49 | FAIT SOURCÉ, moyenne |
| Château (achat + restauration) | banques « prudentes », apport de 20 à 40 % du coût total du projet ; les travaux pèsent souvent plus que le prix | V2-05 Capifrance | FAIT SOURCÉ, faible (un seul article d'agence) |
| Taux d'endettement particulier | seuil 35 % examiné | extrait recherche (bourseinside) | FAIT SOURCÉ, moyenne (règle HCSF connue) |
| Prêt hôtellerie Bpifrance | 10 ans, différé jusqu'à 24 mois, sans garantie, hôtels classés 1–4* ; extension annoncée aux chambres d'hôtes « innovantes » | V2-50, V2-51 | FAIT SOURCÉ, haute mais **2016** (actualité à vérifier) |
| LTV usuelle pour un château | **Je ne sais pas** de façon documentée. ESTIMATION : 60–80 % (déduite de l'apport 20–40 %) | — | ESTIMATION |

## 8. Exemples de financement réel par un jeune entrepreneur

| Exemple | Données | Source | Statut |
|---|---|---|---|
| Château de Bourneau (85), couple ~30 ans, 16 ha | Achat pour location réception/mariages + chambres dans les communs ; **montant emprunté et apport non trouvés** | V2-55 (Ouest-France abonnés cité) | partiel |
| Château en Sarthe (G. Durand-Lépine, ex-avocate) | 56 événements en 2012, **90 000 € de CA annuel** | V2-53 | FAIT SOURCÉ, moyenne (2012) |
| La Giraudais (Bretagne) | Investissement 4 M€ pour un lieu de réceptions ; CA visé couvrant des charges annuelles ≥ 100 000 € ; 4–5 salariés à terme | V2-52 | FAIT SOURCÉ, moyenne |
| Château de Chazemais (03) — annonce de cession, 2 090 000 € | CA 139 000 € (2022), 189 000 € (2023) : mariages, séminaires, hébergement 56 lits | V2-54 + extrait jamesedition | FAIT SOURCÉ, faible (chiffres vendeur ; disponibilité à vérifier au 2026-10-14) |
| Château de Matel (Roanne) | Modèle = salle de 250 m² ; chambres 45–95 €/nuit secondaires | V2-56 | FAIT SOURCÉ, moyenne |
| Château du Pont d'Oye (Belgique) | 2 M€ d'achat + > 5 M€ de travaux | V2-57 | FAIT SOURCÉ, moyenne (hors France) |

**Montant emprunté / apport d'un jeune entrepreneur : Je ne sais pas** (aucun article trouvé avec ces deux chiffres). Vérifier : archives Ouest-France / La Nouvelle République / Le Journal des Entreprises (« reprise château » + « prêt »), comptes annuels publiés des SAS exploitantes (Pappers/Infogreffe).

**Exemples qui contredisent la viabilité (règle 8)** : CA de 90 k€ (Sarthe) ou 139–189 k€ (Chazemais) face à des charges de propriété estimées à 75–135 k€/an (§1) et à des charges ≥ 100 k€ (Giraudais) : un château événementiel de taille moyenne couvre difficilement ses charges et ne rembourse pas une dette d'acquisition de plusieurs millions. La Demeure Historique (2019) et France Epargne (2025) vont dans le même sens.

---

## Points de doute / hypothèses non vérifiées

1. Tous les chiffres proviennent d'extraits WebSearch, sans lecture des documents (WebFetch bloqué) : risque d'erreur de lecture d'un tableau ou de citation hors contexte.
2. Les charges de l'annonce de Liettres (TF 2 652 €, assurance 2 200 €) sont très basses par rapport aux sites de courtage (assurance 15–30 k€) : divergence d'un facteur 5 à 10 non résolue. Un château MH peut bénéficier d'avantages fiscaux qui faussent la comparaison.
3. La ligne La Rochebeaucourt (TF 4 038 €) : l'URL exacte qui porte ce chiffre n'est pas certaine.
4. Valeurs de fermage des 4 départements visés : non trouvées ; les fourchettes données viennent d'autres départements.
5. Prix des terres de l'Orne : donnée 2022 seulement.
6. Loyer de box pour un pro et budget CSO : aucune donnée française vérifiée ; les estimations sont à remplacer.
7. Prêt hôtellerie Bpifrance : conditions de 2016, peut-être modifiées ou supprimées.
8. Règle « 1–2 % de la valeur » : issue de l'immobilier résidentiel suisse, non spécifique aux châteaux. Un château dégradé peut demander beaucoup plus.
9. Disponibilité des annonces citées (Chazemais, Châteauroux, Liettres, Allemagne) : à vérifier, constatée via extraits le 2026-10-14 seulement.
