#!/usr/bin/env python3
"""Génère interface.html : interface locale (hors ligne, sans dépendance) de la cellule audiovisuelle.

Lit : 01_BASE_DE_DONNEES/catalogue.json, 02_ANALYSES/*.md, 03_CAS_REELS/*.md,
04_IDEES_STRATEGIQUES/*.md, 05_RECOMMANDATIONS/*.md, 06_SOURCES/Registre_sources.csv.
Usage : python3 build_interface.py
"""
import csv
import glob
import html
import io
import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))


# ------------------------------------------------------------------ mini-convertisseur Markdown → HTML
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?!\w)", r"<em>\1</em>", t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    t = re.sub(r'(?<!["=>])(https?://[^\s<|)]+)', r'<a href="\1" target="_blank" rel="noopener">\1</a>', t)
    return t


def md_to_html(md):
    out, lines, i = [], md.split("\n"), 0
    in_list = None
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]):
            if in_list:
                out.append(f"</{in_list}>"); in_list = None
            head = [c.strip() for c in s.strip("|").split("|")]
            rows = []
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            out.append('<div class="tw"><table><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in head) +
                       "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows) +
                       "</tbody></table></div>")
            continue
        m = re.match(r"^(#{1,6})\s+(.*)", s)
        if m:
            if in_list:
                out.append(f"</{in_list}>"); in_list = None
            lvl = min(len(m.group(1)) + 1, 6)
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>")
            i += 1
            continue
        m = re.match(r"^([-*]|\d+[.)])\s+(.*)", s)
        if m:
            tag = "ol" if m.group(1)[0].isdigit() else "ul"
            if in_list != tag:
                if in_list:
                    out.append(f"</{in_list}>")
                out.append(f"<{tag}>"); in_list = tag
            out.append(f"<li>{inline(m.group(2))}</li>")
            i += 1
            continue
        if in_list and s and ln.startswith(("  ", "\t")):
            out[-1] = out[-1][:-5] + " " + inline(s) + "</li>"
            i += 1
            continue
        if in_list:
            out.append(f"</{in_list}>"); in_list = None
        if s.startswith(">"):
            out.append(f"<blockquote>{inline(s.lstrip('> '))}</blockquote>")
        elif s in ("---", "***"):
            out.append("<hr>")
        elif s:
            out.append(f"<p>{inline(s)}</p>")
        i += 1
    if in_list:
        out.append(f"</{in_list}>")
    return "\n".join(out)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def docs(folder):
    res = []
    for f in sorted(glob.glob(os.path.join(BASE, folder, "*.md"))):
        res.append({"nom": os.path.basename(f)[:-3].replace("_", " "), "html": md_to_html(read(f))})
    return res


# ------------------------------------------------------------------ passages horodatés
TS = re.compile(r"\b(\d{1,2}:\d{2}(?::\d{2})?)\b")


def passages():
    res = []
    for f in sorted(glob.glob(os.path.join(BASE, "02_ANALYSES", "AV*_fiches.md"))):
        agent = re.search(r"(AV\d+)", f).group(1)
        titre, actif = None, False
        for ln in read(f).split("\n"):
            s = ln.strip()
            if s.startswith("### ") or s.startswith("## "):
                titre, actif = s.lstrip("# ").strip(), False
                continue
            if "passages importants" in s.lower():
                actif = True
            if s.lower().startswith("**note") or s.startswith("---"):
                actif = False
            if actif and TS.search(s) and titre:
                if s.startswith("|") and set(s.replace("|", "").strip()) <= set("-: "):
                    continue
                txt = re.sub(r"^\s*[-*]\s*", "", s).strip("|").replace("|", " — ")
                res.append({"agent": agent, "contenu": titre, "passage": txt})
    return res


def sources():
    p = os.path.join(BASE, "06_SOURCES", "Registre_sources.csv")
    if not os.path.exists(p):
        return []
    rows = list(csv.reader(io.StringIO(read(p)), delimiter=";"))
    hdr = rows[0]
    return [dict(zip(hdr, r)) for r in rows[1:] if any(x.strip() for x in r)]


def main():
    cat = json.load(open(os.path.join(BASE, "01_BASE_DE_DONNEES", "catalogue.json"), encoding="utf-8"))
    data = {
        "catalogue": cat,
        "passages": passages(),
        "analyses": docs("02_ANALYSES"),
        "cas": docs("03_CAS_REELS"),
        "idees": docs("04_IDEES_STRATEGIQUES"),
        "recos": docs("05_RECOMMANDATIONS"),
        "sources": sources(),
    }
    tpl = read(os.path.join(BASE, "interface_template.html"))
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    out = tpl.replace("/*__DATA__*/null", payload)
    with open(os.path.join(BASE, "interface.html"), "w", encoding="utf-8") as fh:
        fh.write(out)
    print("interface.html écrite :", len(cat), "contenus,", len(data["passages"]), "passages horodatés,",
          len(data["sources"]), "sources,", round(len(out) / 1e6, 2), "Mo")


if __name__ == "__main__":
    main()
