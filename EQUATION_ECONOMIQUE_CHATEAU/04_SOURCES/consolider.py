"""Consolide les registres de sources des agents (01_RECHERCHE/sources/sources_*.csv) en un seul fichier.

Usage : python3 consolider.py  →  écrit Registre_sources.csv et Synthese_sources.md dans ce dossier.
Contrôles : en-tête identique, 8 champs par ligne, identifiants uniques. Les anomalies sont listées.
"""
import csv
import glob
import os
from collections import Counter

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCES = os.path.join(ICI, "..", "01_RECHERCHE", "sources")
ENTETE = ["id", "titre", "url", "type_source", "date_consultation", "statut(page_lue/extrait)", "utilise_dans",
          "fiabilite(haute/moyenne/faible)"]


def main():
    lignes, anomalies, vus = [], [], Counter()
    for chemin in sorted(glob.glob(os.path.join(SOURCES, "sources_*.csv"))):
        lot = os.path.basename(chemin)[len("sources_"):-len(".csv")]
        with open(chemin, encoding="utf-8", newline="") as f:
            lecteur = csv.reader(f, delimiter=";")
            entete = next(lecteur)
            if entete != ENTETE:
                anomalies.append(f"{lot} : en-tête différent ({entete})")
            for n, champs in enumerate(lecteur, start=2):
                if not any(c.strip() for c in champs):
                    continue
                if len(champs) != len(ENTETE):
                    anomalies.append(f"{lot}, ligne {n} : {len(champs)} champs au lieu de {len(ENTETE)} ({champs[0]})")
                    champs = (champs + [""] * len(ENTETE))[:len(ENTETE)] if len(champs) < len(ENTETE) else \
                        champs[:6] + [";".join(champs[6:-1]), champs[-1]]
                vus[champs[0]] += 1
                lignes.append([lot] + champs)
    doublons = [i for i, c in vus.items() if c > 1]
    if doublons:
        anomalies.append(f"identifiants en double : {', '.join(sorted(doublons))}")
    with open(os.path.join(ICI, "Registre_sources.csv"), "w", encoding="utf-8", newline="") as f:
        ecrivain = csv.writer(f, delimiter=";")
        ecrivain.writerow(["lot"] + ENTETE)
        ecrivain.writerows(lignes)
    par_lot = Counter(l[0] for l in lignes)
    par_statut = Counter(l[6].strip().lower() for l in lignes)
    par_fiab = Counter(l[8].strip().lower() for l in lignes)
    out = ["# Synthèse du registre des sources (généré par consolider.py)", "",
           f"**{len(lignes)} sources** dans `Registre_sources.csv`, issues de {len(par_lot)} lots.", "",
           "| Lot | Sources |", "|---|---:|"] + [f"| {k} | {v} |" for k, v in sorted(par_lot.items())] + [
           "", "| Statut | Sources |", "|---|---:|"] + [f"| {k or '(vide)'} | {v} |" for k, v in par_statut.most_common()] + [
           "", "| Fiabilité | Sources |", "|---|---:|"] + [f"| {k or '(vide)'} | {v} |" for k, v in par_fiab.most_common()] + [
           "", "## Anomalies de format", ""] + ([f"- {a}" for a in anomalies] or ["Aucune."])
    with open(os.path.join(ICI, "Synthese_sources.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
