"""Hypothèses du modèle financier — Opération Château.

Toutes les valeurs sont éditables dans le fichier Excel produit. Statuts :
  SOURCÉ = chiffre issu d'un extrait de source (fiabilité moyenne, page non ouverte),
  ESTIMATION = raisonnement non vérifié, INCONNU = valeur prudente arbitraire, à remplacer.
Références [A3-..], [A4-..], [A2-..] : voir 07_SOURCES/Registre_sources.csv.
"""
import copy

E, S = "ESTIMATION", "SOURCÉ"

LISEZMOI = [
    "Opération Château — Prévisionnels 10 ans (scénarios A, B, C, cas prudent / central / optimiste, stress tests)",
    "Généré le 2026-10-14 par build_model.py à partir de hypotheses.py. Toutes les cellules de calcul sont des formules : modifiez les cellules jaunes (texte bleu) pour recalculer.",
    "AVERTISSEMENT : aucun chiffre de ce fichier n'est une donnée vérifiée sur un bien réel. Les prix de pension, de mariage, de gîte et les taux viennent d'extraits de recherche web (pages non ouvertes : accès bloqué par l'environnement) ; les charges du château, les travaux, les volumes et les loyers sont des ESTIMATIONS. Colonne D / G de chaque feuille = statut de l'hypothèse.",
    "Bien de référence pour A et B : profil type 'château + ~40-60 ha + écuries existantes' à ~2,65 M€ (ordre de grandeur de l'annonce d'Ygrande (03) relevée par l'agent 1, disponibilité NON vérifiée). Ce n'est pas une recommandation d'achat de ce bien.",
    "Scénario A — Château équestre événementiel : le cheval (pension premium, écurie pro, ventes privées, concours, réceptions équestres) est le moteur principal.",
    "Scénario B — Château premium multiactivité : base équestre (pension) + mariages + journées d'étude + gîtes + tournages.",
    "Scénario C — Acquisition progressive : années 1-4 exploitation d'un domaine loué (loyer), acquisition en année 5 financée surtout par les fonds propres d'une holding du fondateur (alimentée par des reprises de PME — NON acquis, à démontrer).",
    "Feuille B_sans_dette : même exploitation que B_central mais acquisition 100 % en fonds propres — sert uniquement à tester si l'EXPLOITATION seule est autofinancée (hors dette).",
    "Cas prudent / optimiste : dérivés du cas central (volumes, prix, charges, travaux, montée en charge) — voir feuille Sources_hypotheses.",
    "Stress tests (feuilles Stress_*) : appliqués au cas central — CA −30 %, travaux +30 %, ouverture retardée de 12 mois, taux +2 points, retrait de 50 % des fonds investisseurs, annulation de 40 % des événements, et un cumul.",
    "Simplifications : IS à 25 % sans taux réduit de 15 % ni plafonnement de l'imputation des déficits ; TVA neutre (montants HT) ; amortissement bâti 30 ans / travaux 15 ans ; pas de dividendes avant la sortie ; valeur de sortie = % du coût historique (hypothèse, les châteaux se revendent souvent sous leur coût de restauration).",
    "Verdict automatique : VIABLE si trésorerie jamais négative, trésorerie an 10 ≥ réserve cible, DSCR ≥ 1,2 sur les années 4-10 et cash-flow libre d'exploitation ≥ 0 sur les années 4-10. Sinon FRAGILE ou NON VIABLE.",
]

# ---------------------------------------------------------------- Scénario B central
B_INPUTS = {
    "annee_acq": (1, "Achat immédiat"),
    "annee_ouv": (2, "Année 1 = travaux ; ESTIMATION"),
    "prix": (2_650_000, "Ordre de grandeur annonce Ygrande (40 ha, écuries) — agent 1, non vérifié"),
    "frais_acq_pct": (0.075, "Droits ≈6,32 % + notaire/débours ≈1,2 % — agent 6, source secondaire"),
    "part_bati": (0.5, E),
    "capex_restauration": (600_000, "ESTIMATION sans visite ni devis (agent 1 : 0,3-1,2 M€ pour un domaine déjà équipé)"),
    "capex_equestre": (250_000, "ESTIMATION : remise à niveau boxes + carrière + clôtures (agent 3)"),
    "capex_evenementiel": (480_000, "ESTIMATION : salle ERP 300 k€ + 1 gîte 180 k€ (agent 4)"),
    "capex_rep1": (0.6, E), "capex_rep2": (0.3, E), "capex_rep3": (0.1, E),
    "gros_entretien_pct": (0.01, "Règle empirique 1-2 %/an non sourcée (agent 4)"),
    "valo_sortie_pct": (0.8, "ESTIMATION prudente : décote vs coût (Hus −35 % en 1 an, agent 1/7)"),
    "loyer_avant_acq": (0, "Sans objet"),
    "apport_fondateur": (250_000, "Scénario d'apport S2 (hypothèse, apport réel inconnu)"),
    "fp_invest": (1_400_000, "NON ACQUIS — investisseurs à trouver"),
    "fp_fondateur": (0, ""),
    "subventions": (0, "Aucune subvention considérée comme acquise"),
    "dette": (2_100_000, "NON ACQUIS — ≈ 50 % de la valeur, à obtenir"),
    "taux": (0.045, "Moyenne BdF 3,75 % (07/2026) + prime projet atypique — agent 2"),
    "duree": (20, "Agent 2"),
    "differe": (1, E),
    "cv": (400_000, "NON ACQUIS — crédit-vendeur à négocier"),
    "cv_taux": (0.03, E),
    "cv_duree": (5, E),
    "oc": (300_000, "NON ACQUIS — obligations in fine (club deal)"),
    "oc_taux": (0.06, E),
    "oc_ech": (8, E),
    "part_fondateur": (0.35, "ESTIMATION : 250 k€ + apport en industrie / BSPCE ; à négocier"),
    "votes_fondateur": (0.51, "Actions de préférence — acceptation par investisseurs NON acquise"),
    "treso_min": (150_000, E),
    "ramp1": (0.5, E), "ramp2": (0.75, E), "ramp3": (0.9, E),
    "infl_prix": (0.02, E), "infl_ch": (0.025, E),
    "bfr_pct": (-0.03, "Acomptes mariages/pensions payées d'avance — ESTIMATION"),
    "is_taux": (0.25, "Taux normal — agent 6"),
}
# (libellé, volume à maturité, prix unitaire annuel, coût variable %, événement ?, équestre ?, unité / source)
B_REV = [
    ("Pension box premium", 18, 6_600, 0.27, False, True,
     "20 boxes × 90 % ; 550 €/mois [A3, fourchette 430-700 € sourcée] ; coût direct 150 €/mois ESTIMATION"),
    ("Pension au pré / retraite", 27, 3_360, 0.29, False, True,
     "30 places × 90 % ; 280 €/mois (fourchette 120-400 €, source faible) ; coût 80 €/mois ESTIMATION"),
    ("Ventes privées / showcases B2B (location + service)", 4, 5_000, 0.3, True, True,
     "ESTIMATION — aucune preuve de demande pour un lieu privé (agent 3)"),
    ("Mariages (location du lieu, week-end)", 18, 5_500, 0.33, True, False,
     "Médiane ≈5 900 € sur 10 tarifs publiés [A4] ; 18/an = plafond vie privée ESTIMATION"),
    ("Journées d'étude / CODIR (sans nuitée)", 10, 2_500, 0.3, True, False,
     "Mini 2 000 € HT observé [A4-29] ; volume ESTIMATION"),
    ("Gîte de prestige (semaines louées)", 20, 1_000, 0.42, False, False,
     "1 gîte ; 16,9 sem./an observé Gîtes de France [A4-37] ; prix ESTIMATION"),
    ("Tournages / shootings (jours)", 4, 2_000, 0.15, True, False, "≈2 000 €/j [A4-44] ; fréquence INCONNUE"),
    ("Valorisation des terres non pâturées (ha)", 15, 150, 0.1, False, False, "NON VÉRIFIÉ (agent 4)"),
    ("Loyer de la partie privée payé par le fondateur", 1, 24_000, 0.0, False, False,
     "Loyer de marché exigé (risque ABS sinon — agent 6) ; montant ESTIMATION, à payer sur revenus personnels"),
]
# (libellé, montant annuel, dès l'acquisition ?, source)
B_CH = [
    ("Énergie (chauffage partiel, électricité)", 30_000, True, "ESTIMATION 15-40 k€ (agent 4)"),
    ("Assurances bâtiment + RC activités", 15_000, True, "ESTIMATION 5-15 k€ + RC ; devis à obtenir"),
    ("Taxe foncière", 15_000, True, "INCONNU — demander l'avis d'imposition du vendeur"),
    ("Jardinier / agent d'entretien (1 ETP chargé)", 40_000, True, "ESTIMATION 35-45 k€ (agent 4)"),
    ("Parc, haies, clôtures, petit entretien", 15_000, True, E),
    ("Soigneurs (2 ETP chargés)", 50_000, False, "Grille IDCC 7026 1 811 €/mois brut [A3-30] ; 1 ETP/19 équidés [A3-27]"),
    ("Responsable d'écurie (1 ETP chargé)", 35_000, False, E),
    ("Coordinateur événementiel saisonnier", 20_000, False, "ESTIMATION (agent 4)"),
    ("Commercial, marketing, site, salons", 15_000, False, E),
    ("Comptabilité, juridique, banque, logiciels", 15_000, False, E),
    ("Entretien installations équestres, matériel, véhicules", 12_000, False, E),
    ("Rémunération du dirigeant (chargée)", 30_000, False, "Hypothèse minimale ; le dirigeant paie 24 k€ de loyer privé"),
]

# ---------------------------------------------------------------- Scénario A central
A_INPUTS = copy.deepcopy(B_INPUTS)
A_INPUTS.update({
    "capex_equestre": (450_000, "ESTIMATION : manège haut de gamme 150 k€ + boxes/carrière/paddocks (agent 3)"),
    "capex_evenementiel": (120_000, "ESTIMATION : aménagement salon de réception (pas de salle ERP > 50 pers.)"),
    "fp_invest": (1_300_000, "NON ACQUIS — investisseurs à trouver"),
    "dette": (2_000_000, "NON ACQUIS"),
})
A_REV = [
    ("Pension box premium / pension travail", 22, 6_600, 0.27, False, True,
     "24 boxes × 90 % ; 550 €/mois ESTIMATION centrale (fourchette sourcée 430-700 €)"),
    ("Écurie louée à un cavalier pro (boxes/an)", 10, 2_400, 0.1, False, True,
     "200 €/box/mois ESTIMATION ; risque de requalification en bail rural (agent 3/6)"),
    ("Pension au pré / retraite", 18, 3_360, 0.29, False, True, "280 €/mois ; source faible"),
    ("Ventes privées / showcases B2B", 8, 5_000, 0.3, True, True,
     "ESTIMATION — aucune preuve de demande pour un lieu privé"),
    ("Concours (CSO amateur, jours) — recettes", 3, 8_000, 0.85, True, True,
     "Budget CSO INCONNU ; marge −5/+10 k€ par événement selon agent 3"),
    ("Réceptions équestres (propriétaires, éleveurs, marques)", 6, 4_000, 0.35, True, True, E),
    ("Séjours / stages équestres haut de gamme", 15, 900, 0.4, False, True, "ESTIMATION, demande non démontrée"),
    ("Gîte de prestige (semaines louées)", 20, 1_000, 0.42, False, False, "Cf. B"),
    ("Tournages / shootings (jours)", 4, 2_000, 0.15, True, False, "Cf. B"),
    ("Valorisation des terres non pâturées (ha)", 10, 150, 0.1, False, False, "NON VÉRIFIÉ"),
    ("Loyer de la partie privée payé par le fondateur", 1, 24_000, 0.0, False, False, "Cf. B"),
]
A_CH = [c for c in B_CH if not c[0].startswith("Coordinateur")]
A_CH = [("Soigneurs (3 ETP chargés)", 75_000, False, "1 ETP/15-19 équidés [A3-27] ; ~50 chevaux") if c[0].startswith("Soigneurs") else c for c in A_CH]
A_CH.append(("Organisation événements équestres (prestataires fixes, sono, secours)", 10_000, False, E))
A_INPUTS["capex_rep1"] = (0.6, E)

# ---------------------------------------------------------------- Scénario C central
C_INPUTS = copy.deepcopy(B_INPUTS)
C_INPUTS.update({
    "annee_acq": (5, "Option d'achat levée en année 5 — option à NÉGOCIER (non acquise)"),
    "annee_ouv": (1, "Exploitation dès l'an 1 d'un domaine loué, déjà équipé"),
    "prix": (2_650_000, "Même ordre de grandeur ; prix futur INCONNU"),
    "capex_restauration": (500_000, E),
    "capex_equestre": (150_000, E),
    "capex_evenementiel": (300_000, "Salle ERP, après acquisition seulement"),
    "loyer_avant_acq": (100_000, "ESTIMATION ≈ 3,8 % de la valeur ; aucun loyer de domaine sourcé"),
    "apport_fondateur": (250_000, "Fonds de roulement et cautions de la phase locative"),
    "fp_invest": (1_500_000, "Fonds propres de la HOLDING du fondateur — suppose 1-2 reprises de PME réussies : NON acquis"),
    "fp_fondateur": (1, "Fonds propres = holding du fondateur"),
    "dette": (1_900_000, "NON ACQUIS — banque avec 4 ans d'historique d'exploitation"),
    "cv": (0, ""), "oc": (0, ""),
    "part_fondateur": (1.0, "100 % via holding"),
    "votes_fondateur": (1.0, "100 %"),
    "ramp1": (0.6, "Domaine déjà exploité : montée en charge plus rapide (ESTIMATION)"),
    "ramp2": (0.8, E), "ramp3": (0.9, E),
})
C_REV = [r for r in B_REV if not r[0].startswith("Mariages") and not r[0].startswith("Journées")]
C_REV.insert(3, ("Mariages (location du lieu) — limités pendant la location", 10, 5_500, 0.33, True, False,
                 "Volume réduit (salle ERP non construite) — ESTIMATION"))
C_REV.insert(4, ("Journées d'étude / CODIR (sans nuitée)", 6, 2_500, 0.3, True, False, E))
C_CH = []
for lab, amt, acq, src in B_CH:
    if lab.startswith(("Énergie", "Parc", "Jardinier")):
        acq = False  # à la charge de l'exploitant locataire dès l'an 1
    C_CH.append((lab, amt, acq, src))

STRESS0 = {"ca_mult": 1.0, "capex_mult": 1.0, "delai": 0, "taux_add": 0.0, "retrait_inv": 0.0, "annul_evt": 0.0}


def scen(titre, inputs, rev, ch, stress=None):
    st = dict(STRESS0)
    if stress:
        st.update(stress)
    return {"titre": titre, "inputs": copy.deepcopy(inputs), "revenus": copy.deepcopy(rev),
            "charges": copy.deepcopy(ch), "stress": st}


def derive(p, case):
    q = copy.deepcopy(p)
    if case == "prudent":
        fv, fp, fc, fk, ramp = 0.8, 0.92, 1.1, 1.2, (0.4, 0.6, 0.8)
    else:
        fv, fp, fc, fk, ramp = 1.15, 1.08, 0.95, 1.0, (0.6, 0.85, 1.0)
    q["revenus"] = [(l, round(v * fv, 1) if not l.startswith("Loyer de la partie") else v,
                     round(pr * fp) if not l.startswith("Loyer de la partie") else pr, c, e, eq, s)
                    for (l, v, pr, c, e, eq, s) in q["revenus"]]
    q["charges"] = [(l, round(a * fc), acq, s) for (l, a, acq, s) in q["charges"]]
    for k in ("capex_restauration", "capex_equestre", "capex_evenementiel"):
        v, s = q["inputs"][k]
        q["inputs"][k] = (round(v * fk), s)
    for k, v in zip(("ramp1", "ramp2", "ramp3"), ramp):
        q["inputs"][k] = (v, f"Cas {case}")
    q["titre"] = q["titre"].replace("central", case)
    return q


def feuilles():
    base = {
        "A": scen("Scénario A — Château équestre événementiel — cas central", A_INPUTS, A_REV, A_CH),
        "B": scen("Scénario B — Château premium multiactivité — cas central", B_INPUTS, B_REV, B_CH),
        "C": scen("Scénario C — Location puis acquisition progressive via holding — cas central", C_INPUTS, C_REV, C_CH),
    }
    out = []
    for k in ("A", "B", "C"):
        out.append((f"{k}_central", base[k]))
        out.append((f"{k}_prudent", derive(base[k], "prudent")))
        out.append((f"{k}_optimiste", derive(base[k], "optimiste")))
    sd = copy.deepcopy(base["B"])
    sd["titre"] = "Test — exploitation B sans aucune dette (acquisition 100 % fonds propres)"
    sd["inputs"]["fp_invest"] = (sd["inputs"]["fp_invest"][0] + sd["inputs"]["dette"][0] + sd["inputs"]["cv"][0]
                                 + sd["inputs"]["oc"][0], "Test : toute la dette remplacée par des fonds propres")
    for k in ("dette", "cv", "oc"):
        sd["inputs"][k] = (0, "Test")
    out.append(("B_sans_dette", sd))
    # Variantes « frugales » : recherche des conditions de viabilité
    def frugal(p, titre):
        q = copy.deepcopy(p)
        q["titre"] = titre
        ch = []
        for lab, amt, acq, src in q["charges"]:
            if lab.startswith(("Responsable d'écurie", "Coordinateur", "Rémunération du dirigeant")):
                continue  # assuré par le fondateur, non rémunéré par le domaine
            if lab.startswith("Jardinier"):
                lab, amt, src = "Jardinier mi-temps / prestataire", 20_000, "Variante frugale — ESTIMATION"
            if lab.startswith("Soigneurs (2"):
                lab, amt, src = "Soigneurs (1,5 ETP chargés)", 37_500, "Variante frugale — fondateur à l'écurie"
            if lab.startswith("Soigneurs (3"):
                lab, amt, src = "Soigneurs (2 ETP chargés)", 50_000, "Variante frugale — fondateur à l'écurie"
            ch.append((lab, amt, acq, src))
        q["charges"] = ch
        return q
    bf = frugal(base["B"], "Variante B frugale — fondateur non rémunéré tenant écurie + événements, même financement que B central")
    out.append(("B_frugal", bf))
    bfs = frugal(sd, "Variante B frugale SANS dette — test de l'autofinancement de l'exploitation")
    out.append(("B_frugal_sans_dette", bfs))
    cf = frugal(base["C"], "Variante C frugale — holding apporte 2,2 M€, dette 1,2 M€")
    cf["inputs"]["fp_invest"] = (2_200_000, "Fonds propres HOLDING — NON acquis ; suppose plusieurs reprises de PME rentables")
    cf["inputs"]["dette"] = (1_200_000, "NON ACQUIS — LTV ≈ 35 %")
    out.append(("C_frugal_holding", cf))
    cc = copy.deepcopy(cf)
    cc["titre"] = "Scénario C CIBLE — holding apporte ~2,9 M€, dette limitée à la capacité (0,9 M€)"
    cc["inputs"]["fp_invest"] = (2_900_000, "Fonds propres HOLDING — NON acquis : objectif à constituer d'ici l'an 5")
    cc["inputs"]["dette"] = (900_000, "≈ dette soutenable calculée (DSCR 1,2) — NON acquise")
    out.append(("C_cible", cc))
    dm = frugal(base["B"], "Variante D — bien modeste et isolé (~1,4 M€, ≥ 80 ha, à restaurer), exploitation frugale")
    dm["inputs"].update({
        "prix": (1_400_000, "Ordre de grandeur annonce Aubusson (23), XVe s., 85 ha ≈ 1,36 M€ — agent 1, non vérifiée"),
        "capex_restauration": (900_000, "ESTIMATION : château ancien à restaurer, sans devis"),
        "capex_equestre": (400_000, "ESTIMATION : écuries à créer (20 boxes + carrière + manège simple)"),
        "fp_invest": (1_000_000, "NON ACQUIS"), "dette": (1_100_000, "NON ACQUIS"), "cv": (0, ""), "oc": (0, ""),
    })
    dm["revenus"] = [(l, (round(v * 0.75, 1) if l.startswith(("Mariages", "Journées", "Gîte", "Pension box")) else v),
                      (round(pr * 0.85) if l.startswith(("Mariages", "Journées", "Gîte", "Pension box")) else pr), c, e, eq, src)
                     for (l, v, pr, c, e, eq, src) in dm["revenus"]]
    out.append(("D_bien_modeste", dm))
    af = frugal(base["A"], "Variante A frugale — fondateur non rémunéré, même financement que A central")
    out.append(("A_frugal", af))
    stresses = [
        ("CA-30", {"ca_mult": 0.7}),
        ("Travaux+30", {"capex_mult": 1.3}),
        ("Retard12m", {"delai": 1}),
        ("Taux+2pts", {"taux_add": 0.02}),
        ("RetraitInv50", {"retrait_inv": 0.5}),
        ("Annul40evt", {"annul_evt": 0.4}),
        ("Cumul", {"ca_mult": 0.85, "capex_mult": 1.15, "delai": 1, "taux_add": 0.01}),
    ]
    for k in ("A", "B", "C"):
        for nm, st in stresses:
            p = copy.deepcopy(base[k])
            p["stress"].update(st)
            p["titre"] = p["titre"].replace("cas central", f"STRESS {nm}")
            out.append((f"S_{k}_{nm}", p))
    return out


SOURCES = [
    ("Prix d'acquisition 2,65 M€", "Ordre de grandeur de l'annonce Ygrande (03), château 1835, 40 ha, 24 boxes — vue en extrait de recherche (french-property / Safer), disponibilité non vérifiée. Voir 01_OPPORTUNITES."),
    ("Frais d'acquisition 7,5 %", "DMTO 6,32 % dans 88 départements (JeChange, décompte 01/06/2026, source secondaire) + émoluments/débours ≈ 1,2 % ESTIMATION."),
    ("Taux bancaire 4,5 % / 20 ans", "Banque de France : coût moyen des nouveaux crédits aux entreprises 3,75 % (07/2026) — extrait ; prime de risque projet atypique ESTIMATION (agent 2)."),
    ("Pension box 550 €/mois", "Fourchette 430-700 €/mois (IFCE OESC, Écuries de Fondurane) ; 395-435 € en rural (La Gosnière 2024-25) — extraits. 550 € = valeur centrale ESTIMÉE."),
    ("Pension pré/retraite 280 €/mois", "Fourchette 120-400 € (INRAE 2012, pétition) — fiabilité faible."),
    ("Soigneur 25 k€ chargé", "Grille IDCC 7026 coefficient 103 : 1 810,94 € brut/mois au 12/2024 (Tripalio) ; charges ESTIMÉES."),
    ("Productivité 1 ETP / 15-19 équidés", "Synthèse nationale des écuries de pension — extrait."),
    ("Mariage 5 500 €/week-end", "10 tarifs publiés de châteaux (Normandie, Centre-Loire) 3 500-12 000 €, médiane ≈ 5 900 € — extraits (agent 4)."),
    ("18 mariages/an", "ESTIMATION : plafond compatible avec une vie privée sur 22 samedis mai-sept. INSEE : 60 % des mariages juin-sept., 82 % le samedi."),
    ("Journée d'étude 2 500 €", "Minimum 2 000 € HT/jour observé (Château du Chesnay-Haguest) ; ESTIMATION."),
    ("Gîte 1 000 €/semaine × 20", "Gîtes de France : 16,9 semaines louées/an pour un gîte rural, 47 % d'occupation 2024 ; prix ESTIMATION."),
    ("Tournage 2 000 €/jour", "SeLoger (extrait) ; fréquence INCONNUE."),
    ("Charges du château (énergie, assurance, taxe foncière, jardinier, parc)", "ESTIMATIONS non sourcées (agent 4 §7) : total 80-175 k€/an. Vague 2 de vérification : voir 05_AUDIT/Verifications_vague2.md."),
    ("Gros entretien 1 %/an", "Règle empirique non sourcée ; à remplacer par un diagnostic d'architecte du patrimoine."),
    ("Travaux 600 k€ + équestre + événementiel", "ESTIMATIONS sans visite ; salle ERP 200-450 k€, gîte 120-250 k€, manège 85-300 k€ (sources commerciales, agents 3-4)."),
    ("Loyer location domaine (C) 100 k€/an", "ESTIMATION ≈ 3,8 % de la valeur ; aucun loyer de domaine sourcé."),
    ("Valeur de sortie 80 %", "ESTIMATION ; contre-exemple Haras de Hus : 20 M€ → 12,9 M€ en un an (prix affichés)."),
    ("Cas prudent", "Volumes × 0,8 ; prix × 0,92 ; charges fixes × 1,1 ; travaux × 1,2 ; montée en charge 40/60/80 %."),
    ("Cas optimiste", "Volumes × 1,15 ; prix × 1,08 ; charges fixes × 0,95 ; travaux inchangés ; montée en charge 60/85/100 %."),
    ("Fonds propres investisseurs / dette / crédit-vendeur / obligations", "AUCUN financement n'est acquis. Aucun investisseur n'a été contacté."),
]
