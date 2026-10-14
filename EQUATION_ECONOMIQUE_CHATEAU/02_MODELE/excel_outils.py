"""Outils d'écriture du classeur : styles, feuille d'hypothèses, tableaux de gabarits."""
from __future__ import annotations

import csv
import glob
import os

from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName

from noyau import CAS, EXTRA, LIBELLES_CAS, REGISTRE, evaluer, vers_excel

POLICE = "Arial"
F_NORMAL = Font(name=POLICE, size=10)
F_GRAS = Font(name=POLICE, size=10, bold=True)
F_TITRE = Font(name=POLICE, size=13, bold=True)
F_ENTREE = Font(name=POLICE, size=10, color="0000FF")          # saisie (bleu)
F_LIEN = Font(name=POLICE, size=10, color="008000")            # lien vers une autre feuille (vert)
F_ENTETE = Font(name=POLICE, size=10, bold=True, color="FFFFFF")
FOND_ENTETE = PatternFill("solid", fgColor="1F3A5F")
FOND_TOTAL = PatternFill("solid", fgColor="E8EEF5")
FOND_CLE = PatternFill("solid", fgColor="FFFF00")               # hypothèse clé
FOND_STATUT = {
    "SOURCÉ": PatternFill("solid", fgColor="E2EFDA"),
    "ESTIMATION": PatternFill("solid", fgColor="FFF2CC"),
    "HYPOTHÈSE": PatternFill("solid", fgColor="FCE4D6"),
    "CALCUL": PatternFill("solid", fgColor="EDEDED"),
}
FIN = Side(style="thin", color="BFBFBF")
BORD = Border(left=FIN, right=FIN, top=FIN, bottom=FIN)
FMT_EUR = '#,##0" €";-#,##0" €";"-"'
FMT_NB = '#,##0.0;-#,##0.0;"-"'
FMT_PCT = '0.0%;-0.0%;"-"'


def entete(ws, ligne, valeurs, largeurs=None):
    for j, v in enumerate(valeurs, start=1):
        c = ws.cell(row=ligne, column=j, value=v)
        c.font = F_ENTETE
        c.fill = FOND_ENTETE
        c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        c.border = BORD
    if largeurs:
        for j, w in enumerate(largeurs, start=1):
            ws.column_dimensions[get_column_letter(j)].width = w


def format_unite(unite: str) -> str:
    u = unite.lower()
    if "%" in u or "taux" in u or "part" in u or "fraction" in u:
        return FMT_PCT
    if "€" in u:
        return '#,##0.00" €";-#,##0.00" €";"-"' if ("/kwh" in u or "kwh" in u) else FMT_EUR
    return '#,##0.###;-#,##0.###;"-"'


def ecrire_hypotheses(wb, ids_cles=()):
    """Feuille « Hypotheses » : une ligne par hypothèse, trois noms définis par hypothèse."""
    ws = wb.create_sheet("Hypotheses")
    ws["A1"] = "HYPOTHÈSES DU MODÈLE — une ligne par paramètre (saisies en bleu)"
    ws["A1"].font = F_TITRE
    ws["A2"] = ("Favorable / Central / Défavorable : valeurs pour l'équilibre du domaine "
                "(favorable = coût plus bas ou recette plus haute). Statut : SOURCÉ (source citée), "
                "ESTIMATION (raisonnement sur sources), HYPOTHÈSE (choix de modélisation). "
                "Identifiants de sources : voir la feuille Sources.")
    ws["A2"].font = F_NORMAL
    ws["A2"].alignment = Alignment(wrap_text=True)
    ws.merge_cells("A2:J2")
    ws.row_dimensions[2].height = 42
    entete(ws, 4, ["Nom (identifiant)", "Libellé", "Favorable", "Central", "Défavorable",
                   "Unité", "Statut", "Sources", "Note / justification", "Groupe"],
           [30, 58, 13, 13, 13, 16, 13, 22, 70, 18])
    groupe_courant = None
    r = 5
    for prm in sorted(REGISTRE.values(), key=lambda x: (x.groupe, x.id)):
        if prm.groupe != groupe_courant:
            groupe_courant = prm.groupe
            c = ws.cell(row=r, column=1, value=f"— {groupe_courant or 'Divers'} —")
            c.font = F_GRAS
            c.fill = FOND_TOTAL
            r += 1
        ws.cell(row=r, column=1, value=prm.id).font = F_NORMAL
        ws.cell(row=r, column=2, value=prm.libelle).font = F_NORMAL
        fmt = format_unite(prm.unite)
        for j, (cas, val) in enumerate((("fav", prm.fav), ("cen", prm.cen), ("def", prm.dfv)), start=3):
            c = ws.cell(row=r, column=j, value=val)
            c.font = F_ENTREE
            c.number_format = fmt
            c.border = BORD
            if prm.id in ids_cles and cas == "cen":
                c.fill = FOND_CLE
            nom = prm.id + CAS[cas]
            wb.defined_names[nom] = DefinedName(nom, attr_text=f"Hypotheses!${get_column_letter(j)}${r}")
        ws.cell(row=r, column=6, value=prm.unite).font = F_NORMAL
        cs = ws.cell(row=r, column=7, value=prm.statut)
        cs.font = F_NORMAL
        cs.fill = FOND_STATUT.get(prm.statut, PatternFill())
        ws.cell(row=r, column=8, value=prm.sources).font = F_NORMAL
        cn = ws.cell(row=r, column=9, value=prm.note)
        cn.font = F_NORMAL
        cn.alignment = Alignment(wrap_text=True, vertical="top")
        ws.cell(row=r, column=10, value=prm.groupe).font = F_NORMAL
        r += 1
    ws.freeze_panes = "C5"
    return ws


def ecrire_tableau_gabarits(wb, nom_feuille, titre, lignes, colonnes, note=None, prefixe_noms=None):
    """Écrit un tableau dont chaque cellule est une formule issue d'un gabarit.

    lignes   : liste de tuples (id, libellé, gabarit, catégorie, tva, nature)
    colonnes : liste de (en-tête, scénario ou None, cas)
    Renvoie {(id, en-tête): valeur Python} pour la vérification croisée.
    """
    ws = wb.create_sheet(nom_feuille)
    ws["A1"] = titre
    ws["A1"].font = F_TITRE
    if note:
        ws["A2"] = note
        ws["A2"].font = F_NORMAL
        ws["A2"].alignment = Alignment(wrap_text=True)
        ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=4 + len(colonnes))
        ws.row_dimensions[2].height = 54
    entetes = ["Ligne", "Libellé", "Catégorie", "TVA contenue"] + [c[0] for c in colonnes]
    entete(ws, 4, entetes, [22, 62, 20, 10] + [15] * len(colonnes))
    ligne_de = {lid: 5 + i for i, (lid, *_rest) in enumerate(lignes)}
    controle = {}
    valeurs_par_col = {c[0]: {} for c in colonnes}
    for i, (lid, lib, gab, cat, tva, nature) in enumerate(lignes):
        r = 5 + i
        ws.cell(row=r, column=1, value=lid).font = F_NORMAL
        cl = ws.cell(row=r, column=2, value=lib)
        cl.font = F_GRAS if nature == "S" and lid.startswith(("total", "st_")) else F_NORMAL
        ws.cell(row=r, column=3, value=cat).font = F_NORMAL
        ct = ws.cell(row=r, column=4, value=tva)
        ct.number_format = FMT_PCT
        ct.font = F_NORMAL
        for j, (ent, scen, cas) in enumerate(colonnes, start=5):
            col = get_column_letter(j)

            def adr(ref_id, col=col):
                return f"{col}{ligne_de[ref_id]}"

            c = ws.cell(row=r, column=j, value=vers_excel(gab, scen, cas, adr))
            c.font = F_NORMAL
            c.border = BORD
            est_pct = (lid.startswith(("part_", "taux_", "couv_")) or "pct" in lid or lid.endswith("_rdt"))
            c.number_format = FMT_PCT if est_pct else FMT_EUR
            if lid.startswith(("total", "st_")):
                c.fill = FOND_TOTAL
                c.font = F_GRAS
            v = evaluer(gab, scen, cas, valeurs_par_col[ent])
            valeurs_par_col[ent][lid] = v
            controle[(nom_feuille, f"{col}{r}")] = v
            if prefixe_noms:
                nom = prefixe_noms + lid + (f"_{scen}" if scen else "") + CAS[cas]
                ref = f"'{nom_feuille}'!${col}${r}" if " " in nom_feuille else f"{nom_feuille}!${col}${r}"
                wb.defined_names[nom] = DefinedName(nom, attr_text=ref)
                EXTRA[nom] = v
    ws.freeze_panes = "E5"
    return ws, controle


def ecrire_sources(wb, dossier_sources):
    ws = wb.create_sheet("Sources")
    ws["A1"] = "REGISTRE DES SOURCES (consolidé à partir de 01_RECHERCHE/sources/*.csv)"
    ws["A1"].font = F_TITRE
    entete(ws, 3, ["Identifiant", "Titre / donnée", "URL", "Type", "Consultée le",
                   "Statut", "Utilisée dans", "Fiabilité"], [12, 80, 60, 22, 12, 10, 30, 10])
    r = 4
    for chemin in sorted(glob.glob(os.path.join(dossier_sources, "sources_*.csv"))):
        with open(chemin, encoding="utf-8") as f:
            lecteur = csv.reader(f, delimiter=";")
            next(lecteur, None)
            for row in lecteur:
                if not row or not row[0].strip():
                    continue
                for j, v in enumerate(row[:8], start=1):
                    c = ws.cell(row=r, column=j, value=v)
                    c.font = F_NORMAL
                    c.alignment = Alignment(wrap_text=(j == 2), vertical="top")
                r += 1
    ws.freeze_panes = "B4"
    return ws


# ------------------------------------------------------------------------------------------------
# Projection pluriannuelle : une colonne par année, formules identiques d'une année à l'autre
# ------------------------------------------------------------------------------------------------
import re as _re

_REF_PREC = _re.compile(r"\[([A-Za-z0-9_]+)@-1\]")
_REF_COUR = _re.compile(r"\[([A-Za-z0-9_]+)\]")


def ecrire_projection(wb, nom_feuille, titre, lignes, nb_annees, annee_depart, note=None):
    """lignes : liste de (id, libellé, gabarit_initial, gabarit_annuel, format) ; format ∈ {"eur", "pct", "nb", "an"}.

    Syntaxe : [id] = même année ; [id@-1] = année précédente ; {T} = rang de l'année (1..n).
    La colonne D est l'état initial (année 0) ; les colonnes suivantes sont les années 1..n.
    Renvoie {(feuille, cellule): valeur Python} pour la vérification croisée.
    """
    from noyau import espace_noms, vers_python
    ws = wb.create_sheet(nom_feuille)
    ws["A1"] = titre
    ws["A1"].font = F_TITRE
    if note:
        ws["A2"] = note
        ws["A2"].font = F_NORMAL
        ws["A2"].alignment = Alignment(wrap_text=True, vertical="top")
        ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=12)
        ws.row_dimensions[2].height = 66
    ws.cell(row=3, column=3, value="Rang de l'année").font = F_NORMAL
    for k in range(nb_annees + 1):
        c = ws.cell(row=3, column=4 + k, value=k)
        c.font = F_NORMAL
    entete(ws, 4, ["Ligne", "Libellé", "Unité"] + ["Initial"] + [f"An {annee_depart + k - 1}" for k in range(1, nb_annees + 1)],
           [24, 64, 10] + [13] * (nb_annees + 1))
    ligne_de = {lid: 5 + i for i, (lid, *_r) in enumerate(lignes)}
    ns_base = espace_noms()
    controle = {}
    valeurs = [{} for _ in range(nb_annees + 1)]
    for k in range(nb_annees + 1):
        col = get_column_letter(4 + k)
        col_prec = get_column_letter(3 + k)
        for (lid, lib, g_init, g_an, fmt) in lignes:
            r = ligne_de[lid]
            gab = g_init if k == 0 else g_an
            if k == 0 and lid not in [x[0] for x in lignes]:
                continue
            if gab is None:
                continue
            # Excel
            fx = _REF_PREC.sub(lambda m: f"{col_prec}{ligne_de[m.group(1)]}", gab)
            fx = _REF_COUR.sub(lambda m: f"{col}{ligne_de[m.group(1)]}", fx)
            fx = fx.replace("{T}", f"{col}$3")
            c = ws.cell(row=r, column=4 + k, value="=" + fx)
            c.font = F_NORMAL
            c.border = BORD
            c.number_format = {"pct": FMT_PCT, "nb": FMT_NB, "an": '0;-0;"-"'}.get(fmt, FMT_EUR)
            if lid.startswith(("total", "flux", "reserve", "dotation_fin", "kpi")):
                c.fill = FOND_TOTAL
            # Python
            fp = _REF_PREC.sub(lambda m: f"__P_{m.group(1)}", gab)
            fp = _REF_COUR.sub(lambda m: f"__L_{m.group(1)}", fp)
            fp = fp.replace("{T}", str(k))
            ns = dict(ns_base)
            for kk, vv in valeurs[k].items():
                ns[f"__L_{kk}"] = vv
            if k > 0:
                for kk, vv in valeurs[k - 1].items():
                    ns[f"__P_{kk}"] = vv
            v = float(eval(vers_python(fp), {"__builtins__": {}}, ns))  # noqa: S307
            valeurs[k][lid] = v
            controle[(nom_feuille, f"{col}{r}")] = v
        # libellés (une seule fois)
    for (lid, lib, _gi, _ga, fmt) in lignes:
        r = ligne_de[lid]
        ws.cell(row=r, column=1, value=lid).font = F_NORMAL
        cl = ws.cell(row=r, column=2, value=lib)
        cl.font = F_GRAS if lid.startswith(("total", "flux", "reserve", "dotation_fin", "kpi")) else F_NORMAL
        ws.cell(row=r, column=3, value={"pct": "%", "nb": "nombre", "an": "année"}.get(fmt, "€ 2026")).font = F_NORMAL
    ws.freeze_panes = "D5"
    return ws, controle, valeurs
