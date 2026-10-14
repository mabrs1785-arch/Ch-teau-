"""ESTIMATION du chiffre d'affaires par activité (SAS hôtel-restaurant), 2017-2019.
Toutes les hypothèses sont explicites. Montants en euros hors taxes (HT).
"""

JOURS_OUVERTS = 365 - 59  # fermeture annuelle janvier-février
TVA_HEBERGEMENT = 1.10
TVA_RESTAU_MIXTE = 1.115  # mélange 10 % (nourriture) et 20 % (alcool)
PERS_PAR_CHAMBRE = 1.8

scenarios = {
    "Bas": dict(chambres=19, occ=0.35, adr_ttc=130, pdj_ttc=16, pdj_taux=0.8,
                diner_hotes=0.40, couverts_ext=1500, ticket_ttc=45,
                evenements=30_000, autres=15_000, cheval=0),
    "Médian": dict(chambres=19, occ=0.45, adr_ttc=150, pdj_ttc=18, pdj_taux=0.8,
                   diner_hotes=0.50, couverts_ext=3000, ticket_ttc=55,
                   evenements=70_000, autres=30_000, cheval=15_000),
    "Haut": dict(chambres=19, occ=0.60, adr_ttc=170, pdj_ttc=20, pdj_taux=0.8,
                 diner_hotes=0.60, couverts_ext=4500, ticket_ttc=65,
                 evenements=120_000, autres=45_000, cheval=40_000),
    "Calé sur 1,1 M€": dict(chambres=19, occ=0.55, adr_ttc=160, pdj_ttc=19, pdj_taux=0.8,
                            diner_hotes=0.55, couverts_ext=3800, ticket_ttc=59,
                            evenements=100_000, autres=40_000, cheval=20_000),
}


def calc(p):
    dispo = p["chambres"] * JOURS_OUVERTS
    vendues = dispo * p["occ"]
    adr_ht = p["adr_ttc"] / TVA_HEBERGEMENT
    chambres = vendues * adr_ht
    nb_pdj = vendues * PERS_PAR_CHAMBRE * p["pdj_taux"]
    pdj = nb_pdj * p["pdj_ttc"] / TVA_HEBERGEMENT
    couverts_hotes = vendues * PERS_PAR_CHAMBRE * p["diner_hotes"]
    couverts = couverts_hotes + p["couverts_ext"]
    ticket_ht = p["ticket_ttc"] / TVA_RESTAU_MIXTE
    restaurant = couverts * ticket_ht
    lignes = {
        "Chambres": chambres,
        "Petits-déjeuners": pdj,
        "Restaurant": restaurant,
        "Séminaires, banquets, réceptions": p["evenements"],
        "Bien-être, bar, divers": p["autres"],
        "Cheval (forfaits revendus par l'hôtel)": p["cheval"],
    }
    total = sum(lignes.values())
    return dispo, vendues, adr_ht, couverts_hotes, couverts, ticket_ht, lignes, total


for nom, p in scenarios.items():
    dispo, vendues, adr_ht, ch, couverts, ticket_ht, lignes, total = calc(p)
    print(f"=== Scénario {nom}")
    print(f"  nuitées-chambres disponibles = {p['chambres']} x {JOURS_OUVERTS} = {dispo:,.0f}")
    print(f"  nuitées vendues = {dispo:,.0f} x {p['occ']:.0%} = {vendues:,.0f}")
    print(f"  prix moyen {p['adr_ttc']} € TTC = {adr_ht:,.1f} € HT")
    print(f"  couverts : clients hôtel {ch:,.0f} + extérieurs {p['couverts_ext']:,} = {couverts:,.0f} ; ticket {p['ticket_ttc']} € TTC = {ticket_ht:,.1f} € HT")
    for k, v in lignes.items():
        print(f"  {k:42s} {v/1000:8.1f} k€  {v/total:6.1%}")
    print(f"  {'TOTAL':42s} {total/1000:8.1f} k€")
    print(f"  CA total par nuitée-chambre disponible = {total/dispo:,.0f} € HT")
    print()

# Contrôle inverse : CA 1,1 M€ rapporté aux nuitées-chambres disponibles
for n in (16, 19):
    dispo = n * JOURS_OUVERTS
    print(f"Contrôle : 1 100 000 € / ({n} ch. x {JOURS_OUVERTS} j) = {1_100_000/dispo:,.0f} € HT par nuitée-chambre disponible")
