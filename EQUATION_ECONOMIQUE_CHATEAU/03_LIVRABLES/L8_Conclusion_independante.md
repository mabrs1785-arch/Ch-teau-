# L8 — Conclusion indépendante

> **Statut de ce document**
> - Synthèse critique de l'ensemble du dossier (L1 à L7, rapports de recherche, modèle). Elle dit ce que le dossier démontre, ce qu'il ne démontre pas, et ce que j'en conclus.
> - « Indépendante » signifie que cette conclusion ne cherche pas à rendre le projet séduisant. Elle s'appuie sur les chiffres, y compris quand ils déplaisent.

---

## 1. La réponse, sans détour

**1. Un grand château entretenu dans un état d'exception ne se finance pas par son exploitation, si l'on veut qu'il reste calme et privé.**
- Les activités compatibles avec une résidence calme couvrent environ 4 % du besoin d'un domaine S2 dans le cas central (L2, § 3.6).
- Même en cumulant toutes les hypothèses favorables, aucune n'en couvre la moitié.
- Celles qui changent l'ordre de grandeur font venir du monde ou cèdent la maîtrise du lieu :
  - le château-hôtel perd de l'argent dans le cas central, et 54 à 61 % des sociétés de châteaux-hôtels sont en perte ;
  - le bail à un exploitant de séminaires couvre environ 21 %, mais occupe l'essentiel des bâtiments pendant 15 à 30 ans.

**2. La seule solution durable trouvée est un capital affecté au domaine.** Il s'agit d'un fonds d'entretien séparé du patrimoine courant, gouverné par des règles écrites, dont le revenu paie le fonctionnement. Les domaines britanniques qui tiennent sans foule (Burghley, Blenheim, Northumberland) reposent sur un tel patrimoine de rapport [R5-07] [R5-03] [R5-14].

**3. Ce capital est considérable : environ 70 fois le besoin annuel** pour 95 % de chances de tenir 30 ans avec un fonds seul.

| Domaine | Besoin annuel | Fonds seul (95 % sur 30 ans) | Montage hybride (95 % sur 20 ans) |
|---|---:|---:|---|
| S1 | 0,33 M€ | 22,9 M€ | 15 M€ et 0,4 M€ par an pendant 10 ans |
| S2 | 1,24 M€ | 85,5 M€ | 60 M€ et 1 M€ par an pendant 10 ans |
| S3 | 3,64 M€ | 271,3 M€ | 210 M€ (sans dividendes) |

Pour S2, c'est environ **20 fois le prix d'achat retenu**.

**4. La question du brief, « sans dépendre de la fortune personnelle », n'a donc pas de réponse au sens strict.** Le dossier ne trouve aucun moyen de faire vivre un grand domaine calme sans capital. Ce qu'il permet, c'est de **remplacer la dépendance permanente** à la fortune du propriétaire par **un capital affecté une fois pour toutes**. Ce capital doit être séparé, gouverné et dimensionné sur un budget validé. Il peut être constitué par des entreprises dont les revenus sont convertis en capital (L3, modèle 1), ou amorcé par la vente de bâtiments sans usage (modèle 5).

**5. Le principal risque n'est pas une crise, c'est une erreur de budget.**
- Aucun stress test ne crée de déficit sur 20 ans (L6).
- En revanche, si le besoin réel se situe au haut de la fourchette de L1, le risque d'échec passe de 4 % à environ 30 % avant 20 ans.
- Le budget de L1 est un budget nécessaire calculé, qu'aucun budget complet de domaine privé publié ne vient valider [V2C].

**6. La décision la plus importante se prend avant l'achat** : choisir un domaine à la mesure du capital qui peut lui être affecté, et non l'inverse (L3, modèle 3 ; L7, phase 0).

---

## 2. Ce que je tiens pour établi

| Conclusion | Confiance | Pourquoi |
|---|---|---|
| Les activités calmes ne couvrent qu'une faible part du besoin | **Élevée** | Plusieurs sources indépendantes concordent : comptes publiés des châteaux-hôtels [R4-34] et des haras [R4-39] ; note de La Demeure Historique (« pour 99,8 % des propriétaires », l'ouverture à la visite n'est pas rentable [R1-01]) ; comptes de Blenheim [R5-03] ; marges des lieux de réception [R7-63] |
| Un capital dédié est le mécanisme qui fait tenir les domaines privés sans foule | **Élevée** | Comptes publiés de Burghley, Blenheim et Northumberland [R5-07] [R5-03] [R5-14] ; rapport IGF-IGAC de 2020 : le profil « résident » ne finance pas sa part des gros travaux sans revenus extérieurs [V2C-07] |
| Le château-hôtel n'est pas une solution de financement | **Élevée** | Contribution négative dans le cas central ; 54 à 61 % des sociétés en perte selon la période des comptes [R4-34] [V2V] ; liquidations [R7-64] |
| Un domaine en état d'exception coûte de l'ordre de 8 à 10 % de sa valeur de reconstruction par an | **Moyenne** | Cohérent avec la règle du NRC (2 à 4 % pour le seul entretien et la réparation [R1-07] [R1-08]) et avec les dépenses britanniques ; mais aucun budget complet français de cette taille n'a été trouvé |
| Il faut environ 30 fois le besoin pour une chance sur deux de tenir 30 ans, et 70 fois pour 95 % | **Moyenne** | Résultat robuste d'un modèle vérifié (11 301 formules, 0 écart, jumeau Monte-Carlo exact) ; mais il dépend du rendement réel net (§ 3) et du calibrage des crises |
| La discipline de dépense divise le risque par deux | **Moyenne** | Résultat de la simulation, conforme à la pratique des fonds de dotation [R8-34] |

---

## 3. Ce qui reste fragile ou inconnu

1. **Le rendement réel net du fonds.**
   - Le modèle retient 3 % par an après impôts. Ce chiffre dépend du véhicule juridique, de la fiscalité française (PFU de 31,4 % sur les revenus nominaux [R8-31]), de l'allocation et des frais.
   - Capital nécessaire pour S2 avec un fonds seul, pour 95 % de chances de tenir 30 ans (`sorties/mc_sensibilite_rendement.json`) :
     - 85,5 M€ à 3 % ;
     - environ 94 à 97 M€ à 2,5 % ;
     - environ 103 à 108 M€ à 2 % ;
     - environ 113 à 124 M€ à 1,5 %.
   - **C'est l'hypothèse à faire valider en premier par un avocat fiscaliste**, avec le choix du véhicule.
2. **Le véhicule du fonds d'entretien.** Le « maintenance fund » britannique n'a pas d'équivalent direct identifié en France. Le fonds de dotation ne convient pas à une résidence privée [R8-45]. Le montage reste à construire.
3. **Le budget du bien réel.** La fourchette de L1 va de 0,78 à 2,06 M€ pour S2. Les deux paramètres qui pèsent le plus, la valeur de reconstruction au m² et le taux de gros entretien, ne peuvent être fixés que par un architecte du patrimoine et un assureur sur un bien précis.
4. **Le loyer d'un locataire d'ancrage et le prix de vente de communs.** Aucun montant réel n'a été trouvé [V2A] [V2D]. Les modèles 4 et 5 restent des pistes à chiffrer.
5. **Le calibrage des chocs.** La fréquence des crises (1 sur 12), leur ampleur, la volatilité et la défaillance des PME sont des hypothèses. Les probabilités servent à comparer des montages, pas à promettre un niveau de sécurité.
6. **La constitution du capital.** Le dossier ne connaît pas la situation du propriétaire. Il ne peut que donner des ordres de grandeur : 10 à 35 ans d'épargne selon le rythme, sauf cession d'entreprise (L4, § 6).

---

## 4. Ce que j'en conclus pour un propriétaire de 26 ans

1. **Ne pas acheter un domaine de type S2 ou S3 avant d'avoir le capital qui le fait vivre**, ou un chemin crédible et daté pour le réunir. Acheter puis entretenir au rabais crée le retard d'entretien que tous les cas réels documentent.
2. **Commencer par le budget, pas par le domaine.** Fixer le niveau d'exigence, puis appliquer la règle des 70 fois pour en déduire la taille compatible. Un S1 bien choisi, avec 15 à 23 M€ de capital, est un projet réaliste. Un S2 en demande environ quatre fois plus.
3. **Si le capital doit être construit, le construire par des entreprises**, puis convertir leurs revenus en fonds diversifié (L3, modèle 1). Une holding de PME seule, sans conversion, échoue dans 67 à 91 % des cas simulés sur 30 ans.
4. **Écrire la charte avant de dépenser** : règle de dépense, réserve, fonds de travaux, règles de tension, avec au moins une personne indépendante pour la faire respecter. À 26 ans, la gouvernance doit aussi prévoir l'incapacité et la transmission.
5. **Garder les activités pour ce qu'elles sont** : un moyen d'occuper et d'entretenir des bâtiments, et de partager les installations équestres. Ce ne sont pas des recettes. Ne jamais répondre à une année difficile en ouvrant le domaine aux réceptions.

---

## 5. Ce qui pourrait changer cette conclusion

| Si l'on découvrait que… | Effet |
|---|---|
| Le budget réel d'un S2 restauré est nettement plus bas (par exemple 0,8 M€) | Le capital nécessaire baisse dans la même proportion. Au bas de la fourchette de L1, la solution S2 n'échoue que dans 0,4 % des cas avant 20 ans (L6, § 4.2) |
| Un véhicule français permet de capitaliser avec une fiscalité plus légère | Le rendement net augmente et le capital nécessaire baisse d'environ 9 à 11 % par demi-point gagné (`sorties/mc_sensibilite_rendement.json`) |
| Le domaine est situé près de Paris ou d'une gare TGV, et le propriétaire accepte de réduire sa partie privée | Le locataire d'ancrage réduit le capital nécessaire d'environ 18 % en S2 (L3, modèle 4) |
| Des communs ou des terres peuvent être vendus à bon prix sans gêner la partie privée | Le fonds est amorcé d'autant (L3, modèle 5) |
| Le propriétaire accepte d'ouvrir le domaine au public 50 jours par an | Déduction fiscale MH à 100 % au lieu de 50 %, pour un propriétaire imposé au barème [R3-02] [R3-04] ; mais moins de tranquillité |

---

## 6. Les critiques de l'équipe rouge et leur traitement

*Section complétée à réception du rapport de l'équipe rouge (`01_RECHERCHE/V2R_equipe_rouge.md`).*

---

## 7. Avertissements

- Ce dossier ne constitue ni un conseil juridique, ni un conseil fiscal, ni un conseil en investissement. Tous les montages cités doivent être validés par des professionnels.
- Aucun chiffre, aucune transaction, aucun client et aucune preuve de rentabilité n'a été inventé. Ce qui n'a pas été trouvé est indiqué comme INCONNU.
- Aucune démarche n'a été engagée : aucun contact avec des tiers, aucune dépense, aucune opération réelle.
