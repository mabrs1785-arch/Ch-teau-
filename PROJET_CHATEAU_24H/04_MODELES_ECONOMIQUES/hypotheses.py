"""Hypothèses du modèle financier — Opération Château v2 (2026-10-14).

Chaque valeur est éditable dans le fichier Excel produit. Statuts :
  PL = page lue (source ouverte), EX = extrait de recherche, EST = estimation raisonnée, INC = inconnu.
Références : [A1-..] 01_OPPORTUNITES, [A2] 03_FINANCEMENT/Montages_financiers.md,
[A3 Hn] 02_BENCHMARK/Modeles_equestres.md §9, [A4 §n] 02_BENCHMARK/Activites_complementaires.md.
Montants HT (TVA neutre), euros 2026, indexés par le modèle.
"""
import copy

EST = "EST"

LISEZMOI = [
    "Opération Château v2 — Prévisionnels 10 ans",
    "Généré le 2026-10-14 par build_model.py à partir de hypotheses.py. Toutes les cellules de calcul sont des formules : modifiez les cellules jaunes (texte bleu) pour recalculer.",
    "Statuts des hypothèses (colonne D des blocs, colonne G des tableaux) : PL = page lue, EX = extrait de recherche, EST = estimation, INC = inconnu. Aucun financement, investisseur, vendeur ou subvention n'est acquis.",
    "Bien de référence : château + ~40-50 ha + écuries existantes à 2,5 M€ = médiane de 19 annonces de châteaux ≥ 30 ha (agent 1, pages lues). Exemple réel le plus proche : Ygrande (03), 2,65 M€, 40,7 ha, 24 boxes, manège, 16 chambres (vente SAFER, page lue).",
    "Scénario A — Château équestre « sport » : pension travail avec cavalier professionnel, valorisation et vente de jeunes chevaux, concours, pension premium. Financement bancaire classique (apport 1 M€).",
    "Scénario B — Château multiactivité : pension premium + pré + retraite, mariages plafonnés, gîte, séminaires, tournages. Financement bancaire classique (apport 1 M€).",
    "Variantes de financement de B : B_club_deal (apport 250 k€ + investisseurs majoritaires), B_credit_vendeur (apport 250 k€ + crédit-vendeur 1,5 M€), B_sans_dette (diagnostic de l'exploitation seule).",
    "Scénario C — Le capital d'abord : holding de reprise de PME 2026-2030 (hors modèle), achat en année 5 (2031) presque sans dette, exploitation frugale. Les fonds propres viennent de la holding (NON acquis).",
    "Scénario E — Bail emphytéotique : contrôle d'un domaine public pendant 50-99 ans sans propriété ; travaux à la charge du preneur ; redevance INCONNUE ; aucune valeur de sortie (améliorations au bailleur).",
    "Cas prudent / optimiste : dérivés du central (volumes, prix, charges, travaux, montée en charge) — voir Sources_hypotheses. Stress tests (feuilles S_*) : appliqués aux configurations non déficitaires.",
    "Simplifications : IS 25 % sans taux réduit ni plafonnement des déficits ; montants HT ; amortissements bâti 30 ans / travaux 15 ans ; pas de dividendes avant la sortie ; valeur de sortie = % du coût historique moins frais de cession ; loyer privé du fondateur hors CA d'exploitation.",
    "Verdict : VIABLE si trésorerie jamais négative, trésorerie an 10 ≥ réserve, DSCR (après gros entretien) ≥ 1,2 sur les années 4-10, cash-flow libre ≥ 0 sur les années 4-10, TRI des investisseurs extérieurs ≥ 6 % et dirigeant payé. Sinon FRAGILE ou NON VIABLE.",
]

# ------------------------------------------------------------------ bloc commun (B central)
B_INPUTS = {
    "annee_acq": (1, "Achat immédiat (2027)"),
    "annee_ouv": (2, "Année 1 = travaux ; EST"),
    "prix": (2_500_000, "PL : médiane de 19 annonces de châteaux ≥ 30 ha (quartiles 1,29-3,07 M€) [A1]"),
    "frais_acq_pct": (0.075, "EST : DMTO ≈ 5,8-6,3 % + notaire ≈ 1,2 % ; vente SAFER : frais 8,4 % TTC mais exonération de droits possible [A1, PL]"),
    "part_bati": (0.55, EST),
    "capex_restauration": (500_000, "EST sans visite : top 5 des biens équipés 0,1-0,7 M€ [A1]"),
    "capex_equestre": (150_000, "EST : remise à niveau d'écuries existantes (une écurie neuve de 30 box coûterait 0,78-0,83 M€ HT [A3 H20])"),
    "capex_evenementiel": (250_000, "EST : mise aux normes d'une salle existante + aménagement du gîte (neuf : 570 k€-1,24 M€ [A4 §13.2])"),
    "capex_rep1": (0.6, EST), "capex_rep2": (0.3, EST), "capex_rep3": (0.1, EST),
    "gros_entretien_pct": (0.012, "≈ 40 k€/an de provision : Barnes 20-80 k€/an [A4 §11, PL] ; démarre en année d'acquisition + 3"),
    "valo_sortie_pct": (0.8, "EST : Haras de Hus affiché 20 → 12,9 M€ ; les châteaux se revendent sous leur coût [A1, A7]"),
    "loyer_avant_acq": (0, "Sans objet"),
    "frais_cession_pct": (0.05, EST),
    "loyer_prive": (18_000, "EST : loyer de marché de la partie privée, payé par le fondateur sur revenus extérieurs (risque d'abus de biens sociaux sinon)"),
    "apport_fondateur": (1_000_000, "Scénario d'apport S3 (hypothèse ; apport réel inconnu)"),
    "fp_invest": (0, "Aucun investisseur"),
    "fp_fondateur": (0, ""),
    "subventions": (0, "Aucune subvention considérée comme acquise"),
    "dette": (2_400_000, "NON ACQUIS — montage 1 [A2] : prêt hypothécaire 20 ans ; LTV ≈ 70 %, jugée trop élevée par l'agent 2"),
    "taux": (0.04, "PL : nouveaux crédits PME 3,64 % (FBF, 06/2026) ; EX : 3,66 % (BdF, 08/2026) ; retenu 4,0 % [A2]"),
    "duree": (20, "A2 (Bpifrance : 15 ans avec hypothèque, PL)"),
    "differe": (1, EST),
    "cv": (0, ""), "cv_taux": (0.03, EST), "cv_duree": (12, EST),
    "oc": (0, ""), "oc_taux": (0.07, "PL : obligations Château Fontenay 7 % [A2]"), "oc_ech": (6, EST),
    "prime_industrie": (0.0, "Fondateur seul"),
    "votes_fondateur": (1.0, ""),
    "treso_min": (150_000, EST),
    "tri_cible": (0.06, "EST : rendement minimal d'un investisseur en fonds propres illiquide (Anaxago affiche 8,7 % net, PL [A2])"),
    "dirigeant_paye": (1, "Rémunération du dirigeant incluse"),
    "ramp1": (0.5, "A4 : mariages 40/70/100 % ; gîte 50/80/100 %"), "ramp2": (0.8, EST), "ramp3": (1.0, EST),
    "infl_prix": (0.02, EST), "infl_ch": (0.025, EST),
    "bfr_pct": (-0.03, "Acomptes (mariages, pensions payées d'avance) — EST"),
    "is_taux": (0.25, "Taux normal (équestre en BA hors société : non modélisé)"),
}

# (libellé, volume à maturité, prix unitaire annuel HT, coût variable %, événement ?, équestre ?, source)
PENSION_BOX = ("Pension box premium (places occupées)", 22, 5_915, 0.20, False, True,
               "PL : 520 € TTC/mois (premium régional ; IdF 540-650) → 493 € HT à TVA 5,5 % [A3 H1-H2, H8] ; 24 box × 92 % ; coûts directs 1 200 €/an EST (réf. 613-1 729) [A3 §4]")
PENSION_PRE = ("Pension au pré (places occupées)", 23, 2_616, 0.23, False, True,
               "PL : 230 € TTC/mois → 218 € HT [A3 H3] ; 25 places × 92 % ; coûts 613 €/an [A3 §4]")
PENSION_RETRAITE = ("Pension retraite / convalescence (places occupées)", 9, 2_100, 0.24, False, True,
                    "PL : 210 € TTC/mois, TVA 20 % → 175 € HT [A3 H4] ; 10 places × 90 %")
MARIAGES = ("Mariages (location du lieu + hébergement 15 couchages)", 12, 4_197, 0.43, True, False,
            "PL : médiane 3 400 € TTC location (17 châteaux) + 1 500 € TTC hébergement → 4 197 € HT [A4 §13.1] ; 12/an EST ; coût variable 1 450 € + 8 %")
GITE = ("Gîte 15 couchages hors mariages (nuits)", 92, 450, 0.45, False, False,
        "PL : fourchettes de prix [A4 §4.2] ; 92 nuits EST (occupation annuelle ≈ 33 % observée en Normandie hors saison) [A4 §4.3]")
SEMINAIRES = ("Séminaires à la journée (jours)", 12, 800, 0.19, True, False, "PL : salle 1 000 €/jour (Feugerets) ; 800 € HT retenu [A4 §3]")
TOURNAGES = ("Tournages / shootings (jours)", 3, 2_000, 0.15, True, False, "PL : 1 500-4 000 €/jour [A4 §5] ; fréquence EST")
HERBE = ("Fermage / vente d'herbe (ha)", 10, 150, 0.0, False, False, "PL : arrêtés Orne/Calvados 2026-27 : 50-268 €/ha [A4 §8.2]")

B_REV = [PENSION_BOX, PENSION_PRE, PENSION_RETRAITE, MARIAGES, GITE, SEMINAIRES, TOURNAGES, HERBE]

# (libellé, montant annuel, dès l'acquisition ?, source)
CH_CHATEAU = [
    ("Taxe foncière", 6_000, True, "EX : 2,6-4,0 k€ sur 3 annonces ; EST 4-8 k€ [A4 §11]"),
    ("Assurance multirisque château", 7_000, True, "PL : « rarement < 2 500 € », hausse 2026 de 7,5-8 % [A4 §11] ; EST 5-10 k€"),
    ("Énergie (chauffage partiel, électricité, eau)", 20_000, True, "PL : Meung, Louvignies ; EX annonce Montluçon 18-25 k€ [A1, A4 §11] ; EST"),
    ("Jardinier / agent d'entretien (1 ETP au Smic chargé)", 27_000, True, "PL : Smic 2026 22 404 € brut/an [A4 §11] ; EST charges"),
    ("Divers (abonnements, petit matériel, véhicule, honoraires)", 8_000, True, EST),
]
CH_EQUESTRE_B = [
    ("Soigneurs (2 ETP au Smic chargés)", 60_000, False, "PL : Smic 1 867 €/mois, grille IDCC 7026 inférieure ; 1 ETP / 17-20 équidés [A3 H13-H14] ; ~54 équidés"),
    ("Autres charges de structure équestres (entretien installations, matériel, assurance RC, énergie écuries)", 30_000, False,
     "Calibré pour un EBE équestre ≈ 37 % (réf. pension hébergement 36-38 %, PL [A3 H10])"),
]
CH_ACTIVITES = [
    ("Coûts fixes mariages (coordination, nettoyage, publicité)", 11_000, False, "EST [A4 §13.1]"),
    ("Coûts fixes du gîte", 4_400, False, "EST [A4 §13.1]"),
    ("Commercial, site, salons", 12_000, False, EST),
    ("Comptabilité, juridique, banque, logiciels", 12_000, False, EST),
]
DIRIGEANT = ("Rémunération du dirigeant (chargée)", 35_000, False, "EST : minimum ; le dirigeant paie en plus 18 k€ de loyer privé")
B_CH = CH_CHATEAU + CH_EQUESTRE_B + CH_ACTIVITES + [DIRIGEANT]

# ------------------------------------------------------------------ Scénario A
A_INPUTS = copy.deepcopy(B_INPUTS)
A_INPUTS.update({
    "capex_equestre": (350_000, "EST : marcheur 35 k€, carrière 35 €/m², barn 200 €/m² (PL [A3 H19]) + 10 box supplémentaires"),
    "capex_evenementiel": (80_000, "EST : salon de réception pour ventes privées, pas de salle ERP > 50 pers."),
})
A_REV = [
    ("Pension travail (chevaux de sport, places occupées)", 18, 6_560, 0.26, False, True,
     "PL : 656 € TTC/mois (cas-type CSO 2025) → 547 € HT à TVA 20 % (entraînement/valorisation, BOFiP) [A3 H5, H9] ; 20 places × 90 % ; coûts op. 1 729 €/an [A3 §4]"),
    ("Pension box premium (places occupées)", 9, 5_915, 0.20, False, True, "Cf. B ; 10 places × 90 %"),
    ("Pension au pré (places occupées)", 14, 2_616, 0.23, False, True, "Cf. B ; 15 places × 92 %"),
    ("Valorisation et vente de jeunes chevaux (marge nette par cheval vendu)", 3, 9_975, 0.10, False, True,
     "PL : cas-type 2 chevaux/an, 36,75 k€ vendus − 16,8 k€ achetés [A3 §8] ; 3/an EST ; risque élevé"),
    ("Organisation de concours (produit annuel)", 1, 16_076, 0.50, True, True,
     "PL : produit moyen « organisation de concours » d'une pension travail 16 076 €/an [A3 §4] ; marge EST"),
    ("Ventes privées / showcases B2B (soirées)", 3, 3_000, 0.40, True, True,
     "INC : aucun tarif de location publié [A3 §8 n°10] ; EST"),
    ("Gains de compétition", 1, 12_250, 0.0, True, True, "PL : cas-type CSO 2025 12 250 € [A3 §4]"),
    GITE, TOURNAGES, HERBE,
]
A_CH = CH_CHATEAU + [
    ("Cavalier professionnel / responsable d'écurie (chargé)", 45_000, False, "PL : grille 2 108-2 678 € brut (coef. 130-167) [A3 H15] ; EST charges"),
    ("Soigneurs (2 ETP au Smic chargés)", 60_000, False, "PL [A3 H13-H14] ; 10 chevaux au travail / ETP"),
    ("Autres charges de structure équestres", 35_000, False, "EST : réf. structure pension travail 2 471 €/équidé [A3 §4] (salaires inclus) → calibrage"),
    ("Coûts fixes du gîte", 4_400, False, "EST [A4 §13.1]"),
    ("Commercial, site, salons", 12_000, False, EST),
    ("Comptabilité, juridique, banque, logiciels", 12_000, False, EST),
    DIRIGEANT,
]

# ------------------------------------------------------------------ Scénario C (capital d'abord)
C_INPUTS = copy.deepcopy(B_INPUTS)
C_INPUTS.update({
    "annee_acq": (5, "Achat en année 5 (2031) quand la holding a le capital — NON acquis"),
    "annee_ouv": (5, "Domaine déjà équipé : ouverture l'année de l'achat, montée en charge"),
    "apport_fondateur": (0, "Les fonds propres viennent de la holding (ligne suivante)"),
    "fp_invest": (3_400_000, "Fonds propres de la HOLDING (reprises de PME) — NON acquis ; un LBO de ~1 M€ ne libère que ~50 k€/an [A2 montage 6]"),
    "fp_fondateur": (1, "Fonds propres = holding du fondateur"),
    "dette": (400_000, "NON ACQUIS — limitée à la capacité de remboursement"),
    "prime_industrie": (0.0, ""),
})

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
        fv, fp, fc, fk, ramp = 0.8, 0.92, 1.1, 1.25, (0.4, 0.65, 0.85)
    else:
        fv, fp, fc, fk, ramp = 1.15, 1.08, 0.95, 1.0, (0.6, 0.9, 1.0)
    q["revenus"] = [(l, round(v * fv, 1), round(pr * fp), c, e, eq, s) for (l, v, pr, c, e, eq, s) in q["revenus"]]
    q["charges"] = [(l, round(a * fc), acq, s) for (l, a, acq, s) in q["charges"]]
    for k in ("capex_restauration", "capex_equestre", "capex_evenementiel"):
        v, s = q["inputs"][k]
        q["inputs"][k] = (round(v * fk), s)
    for k, v in zip(("ramp1", "ramp2", "ramp3"), ramp):
        q["inputs"][k] = (v, f"Cas {case}")
    q["titre"] = q["titre"].replace("cas central", f"cas {case}")
    return q


def frugal(p, titre):
    """Fondateur non rémunéré par le domaine, tient l'écurie ; moins de salariés."""
    q = copy.deepcopy(p)
    q["titre"] = titre
    ch = []
    for lab, amt, acq, src in q["charges"]:
        if lab.startswith(("Rémunération du dirigeant", "Cavalier professionnel")):
            continue
        if lab.startswith("Jardinier"):
            lab, amt, src = "Jardinier à mi-temps / prestataire", 14_000, "Variante frugale — EST"
        if lab.startswith("Soigneurs (2"):
            lab, amt, src = "Soigneur (1 ETP + extras week-end)", 36_000, "Variante frugale : le fondateur assure une partie des soins"
        ch.append((lab, amt, acq, src))
    q["charges"] = ch
    q["inputs"]["dirigeant_paye"] = (0, "Variante frugale : fondateur non rémunéré par le domaine")
    return q


def feuilles():
    base = {
        "A": scen("Scénario A — Château équestre « sport » — cas central", A_INPUTS, A_REV, A_CH),
        "B": scen("Scénario B — Château multiactivité — cas central", B_INPUTS, B_REV, B_CH),
    }
    out = []
    for k in ("A", "B"):
        out.append((f"{k}_central", base[k]))
        out.append((f"{k}_prudent", derive(base[k], "prudent")))
        out.append((f"{k}_optimiste", derive(base[k], "optimiste")))

    # Variantes de financement de B
    cd = copy.deepcopy(base["B"])
    cd["titre"] = "B — Club deal : apport 250 k€, investisseurs majoritaires (montage 2) — cas central"
    cd["inputs"].update({
        "apport_fondateur": (250_000, "Scénario d'apport S2"),
        "fp_invest": (1_640_000, "NON ACQUIS — investisseurs à trouver [A2 montage 2]"),
        "dette": (1_800_000, "NON ACQUIS — LTV ≈ 50 % [A2 montage 2]"),
        "prime_industrie": (0.05, "EST : promote négociée"),
        "votes_fondateur": (0.10, "Investisseurs majoritaires [A2]"),
    })
    out.append(("B_club_deal", cd))

    cvd = copy.deepcopy(base["B"])
    cvd["titre"] = "B — Crédit-vendeur : apport 250 k€, crédit-vendeur 1,5 M€ sur 12 ans (montage 3) — cas central"
    cvd["inputs"].update({
        "apport_fondateur": (330_000, "S2 250 k€ + prêts d'honneur 80 k€ [A2 montage 3]"),
        "dette": (1_100_000, "NON ACQUIS — banque 15 ans (750 k€) + prêt OpCo garanti (350 k€) regroupés [A2]"),
        "duree": (15, "A2"),
        "cv": (1_500_000, "NON ACQUIS — vendeur coopératif à trouver ; clause résolutoire [A2 montage 3]"),
        "cv_taux": (0.03, "A2"), "cv_duree": (12, "A2"),
        "oc": (500_000, "NON ACQUIS — obligations PSFP in fine 5 ans [A2]"), "oc_taux": (0.08, "A2 : 7-9 %"), "oc_ech": (6, "Remboursement in fine en année 6"),
    })
    out.append(("B_credit_vendeur", cvd))

    sd = copy.deepcopy(base["B"])
    sd["titre"] = "Diagnostic — exploitation B sans aucune dette (tout en fonds propres)"
    sd["inputs"]["apport_fondateur"] = (3_900_000, "Test : tout financé en fonds propres (emplois + réserve)")
    sd["inputs"]["dette"] = (0, "Test")
    out.append(("B_sans_dette", sd))

    bf = frugal(base["B"], "B frugal — fondateur non rémunéré, même financement bancaire que B central")
    out.append(("B_frugal", bf))
    bfs = frugal(sd, "Diagnostic — B frugal sans dette : l'exploitation s'autofinance-t-elle ?")
    out.append(("B_frugal_sans_dette", bfs))
    af = frugal(base["A"], "A frugal — fondateur cavalier non rémunéré, même financement que A central")
    out.append(("A_frugal", af))

    # Scénario C : capital d'abord
    c = frugal(scen("Scénario C — Le capital d'abord : achat en 2031 avec les fonds propres de la holding — cas central",
                    C_INPUTS, B_REV, B_CH),
               "Scénario C — Le capital d'abord : achat en 2031 avec les fonds propres de la holding — cas central")
    out.append(("C_central", c))
    out.append(("C_prudent", derive(c, "prudent")))
    out.append(("C_optimiste", derive(c, "optimiste")))
    cn = copy.deepcopy(c)
    cn["titre"] = "C négocié — vendeur en difficulté : prix −20 %, travaux −30 % (équipements existants)"
    cn["inputs"]["prix"] = (2_000_000, "Prix −20 % : vendeur en difficulté (Ygrande vendu par la SAFER, Hus −35 %) — NON acquis")
    for k in ("capex_restauration", "capex_equestre", "capex_evenementiel"):
        v, src = cn["inputs"][k]
        cn["inputs"][k] = (round(v * 0.7), "−30 % : équipements existants — EST")
    cn["inputs"]["fp_invest"] = (2_600_000, "Fonds propres HOLDING — NON acquis")
    out.append(("C_negocie", cn))

    # Scénario E : bail emphytéotique
    e = frugal(scen("Scénario E — Bail emphytéotique d'un domaine public (contrôle sans propriété) — cas central",
                    B_INPUTS, B_REV, B_CH + [("Redevance emphytéotique", 20_000, True,
                                              "INC : Montfort 22,9 k€/an, Neuenbourg 1 €/an (exemples, PL v1) ; Maison Fournaise 80 k€ + 7 % du CA")]),
               "Scénario E — Bail emphytéotique d'un domaine public (contrôle sans propriété) — cas central")
    e["inputs"].update({
        "prix": (0, "Pas d'achat : droit réel de 50-99 ans ; droit d'entrée INCONNU"),
        "frais_acq_pct": (0.0, ""),
        "capex_restauration": (1_200_000, "A2 montage 4 : travaux à la charge du preneur 1,5 M€, dont ~0,3 M€ subventionnés côté propriétaire public (non acquis)"),
        "capex_equestre": (150_000, EST), "capex_evenementiel": (150_000, EST),
        "apport_fondateur": (330_000, "S2 250 k€ + prêts d'honneur 80 k€"),
        "dette": (900_000, "NON ACQUIS — prêt hypothéqué sur le droit réel (si le bailleur l'autorise) [A2 montage 4]"),
        "duree": (15, "A2"),
        "oc": (400_000, "NON ACQUIS — obligations PSFP [A2 montage 4]"), "oc_taux": (0.07, EST), "oc_ech": (7, EST),
        "valo_sortie_pct": (0.0, "Améliorations reviennent au bailleur en fin de bail"),
        "gros_entretien_pct": (0.025, "≈ 40 k€/an sur la base des travaux (le preneur entretient)"),
    })
    out.append(("E_bail_emphyteotique", e))
    ea = copy.deepcopy(e)
    ea["titre"] = "Scénario E allégé — bail emphytéotique d'un site en bon état : travaux 0,6 M€, dette 0,3 M€"
    ea["inputs"].update({
        "capex_restauration": (300_000, "EST : site public déjà entretenu — hypothèse favorable"),
        "dette": (300_000, "NON ACQUIS"), "oc": (0, ""),
        "gros_entretien_pct": (0.05, "≈ 30 k€/an sur la base des travaux"),
    })
    out.append(("E_allege", ea))

    stresses = [
        ("CA-30", {"ca_mult": 0.7}),
        ("Travaux+30", {"capex_mult": 1.3}),
        ("Retard12m", {"delai": 1}),
        ("Taux+2pts", {"taux_add": 0.02}),
        ("RetraitFP50", {"retrait_inv": 0.5}),
        ("Annul40evt", {"annul_evt": 0.4}),
        ("Cumul", {"ca_mult": 0.85, "capex_mult": 1.15, "delai": 1, "taux_add": 0.01}),
    ]
    for k, basep in (("Cc", c), ("Cn", cn), ("Bfsd", bfs)):
        for nm, st in stresses:
            p = copy.deepcopy(basep)
            p["stress"].update(st)
            p["titre"] = p["titre"] + f" — STRESS {nm}"
            out.append((f"S_{k}_{nm}", p))
    return out


SOURCES = [
    ("Prix du domaine 2,5 M€", "PL : médiane de 19 annonces French-Property de châteaux ≥ 30 ha (quartiles 1,29-3,07 M€), relevées le 2026-10-14 [01_OPPORTUNITES]. Prix total par ha : médiane ≈ 59 k€/ha."),
    ("Frais d'acquisition 7,5 %", "EST : DMTO + notaire ; vente SAFER : frais 8,4 % TTC, exonération des droits si destination agricole maintenue (une annonce, PL)."),
    ("Taux 4,0 % / 20 ans", "PL : FBF, crédits aux PME 3,64 % (06/2026) ; EX : BdF 3,66 % (08/2026). Bpifrance : 15 ans avec hypothèque (PL). Critères CRA pour une reprise : ≤ 7 ans, ≤ 70 % du prix (PL)."),
    ("Pensions", "PL : annuaire pension-chevaux.com, 402 tarifs de 114 écuries (Normandie, Centre, PdL, IdF) — box 350-450 € TTC (médianes), premium 540-650 €, pré 200-240 €, retraite 170-230 €, travail 535-656 €. TVA 5,5 % (pension liée aux installations) ou 20 % (retraite, valorisation) — BOFiP 2024 (PL), risque de requalification."),
    ("Calibrage équestre", "PL : Réseau Équin (synthèse 2024, données 2022) — EBE/produit brut 36-38 % (pension hébergement), 23-28 % (pension travail, centre équestre) ; échantillon de structures performantes."),
    ("Salaires", "PL : Smic 2026 1 867,02 € brut/mois ; grille IDCC 7026 coef. 100-109 inférieure au Smic ; productivité 1 ETP / 17-20 équidés."),
    ("Mariages", "PL : 1001 Salles, 27 fiches de châteaux — location week-end sans hébergement médiane 3 400 € TTC, avec hébergement 6 800 € TTC. INSEE : 251 000 mariages en 2025, 68 % mai-septembre. Volume 12/an : EST."),
    ("Gîte, séminaires, tournages, fermage", "PL : fourchettes de prix des lieux, arrêtés de fermage Orne/Calvados 2026-27, commission du film des Pays de la Loire. Volumes : EST."),
    ("Charges du château (≈ 68 k€/an + gros entretien ≈ 40 k€)", "Mix PL/EX/EST [A4 §11] : taxe foncière 2,6-4,0 k€ observée, assurance ≥ 2,5 k€, énergie 15-25 k€, Smic, Barnes 20-80 k€/an de charges."),
    ("Travaux", "EST sans visite ni devis : domaine déjà équipé (top 5 de l'agent 1 : 0,1-0,7 M€). Écurie neuve 30 box : 0,78-0,83 M€ HT ; salle ERP + gîte neufs : 0,57-1,24 M€."),
    ("Valeur de sortie 80 %", "EST ; contre-exemple Haras de Hus : CA 1,77 M€, résultat d'exploitation −3,9 M€ (2024, Xerfi, PL), prix affiché 20 → 12,9 M€."),
    ("Cas prudent", "Volumes × 0,8 ; prix × 0,92 ; charges fixes × 1,1 ; travaux × 1,25 ; montée en charge 40/65/85 %."),
    ("Cas optimiste", "Volumes × 1,15 ; prix × 1,08 ; charges fixes × 0,95 ; travaux inchangés ; montée en charge 60/90/100 %."),
    ("Financements", "AUCUN n'est acquis : banques, investisseurs, vendeur, obligataires, holding, subventions. Personne n'a été contacté."),
]
