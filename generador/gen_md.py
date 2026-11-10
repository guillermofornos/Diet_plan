"""Genera los Markdown del repo a partir del plan."""
from pathlib import Path
from plan import R, SEMANAS, DIAS, TIPO, FUERA, CAMBIOS, PREP, BATCH, NORMAS, NOTA_COMPRA, total_dia
from shop import lista, opcional_bigmac
from lib import texto, macros_receta

REPO = Path(__file__).resolve().parent.parent   # el repositorio Diet_plan
MESES = {"10": "oct", "11": "nov"}
COMIDAS = ["LENT1", "LENT2", "PILPIL", "VIZCA_A", "FISHCHIPS", "ARRGAMB", "TOFU", "GUIS_T", "BBQ", "CURRY", "BURR"]
CENAS = ["MERTAC", "TOR", "PZA", "FCE", "TOM", "FPZ", "BEX"]   # sin atún: fuera los tacos de atún y la ensaladilla
ROBOT = ["LENTJ", "POTG", "JARD", "ARRPOL", "ALBON", "TERESC", "RISOT", "CREMCAL", "CREMZAN"]
VARIANTES = {"TOFU": "TOFU_D"}
FICHERO = {**{k: "recetas_videos_internet.md" for k in COMIDAS + CENAS + ["TOFU_D"]},
           **{k: "fast_food_saludable.md" for k in ["TAC", "CRI", "FAJ", "KEB", "FIN", "FF2"]},
           **{k: "recetas_robot_cecotec.md" for k in ROBOT},
           **{k: "desayunos.md" for k in ["D1", "D2", "D3", "D4", "D4L", "D4S"]}, "ME_E": "meriendas.md", "ME_D": "meriendas.md"}

def mac(k):
    kc, p, g, h = macros_receta(R[k]); return f"≈ {kc:.0f} kcal · {p:.0f} g proteína · {h:.0f} g HC · {g:.0f} g grasa"

def enlaces(r):
    """Líneas con el vídeo (y el segundo vídeo o la receta escrita), con la URL a la vista; o la página del libro del robot."""
    if not r.get("url"):
        out = [f"📖 Libro del robot Cecotec, {r['libro']}"] if r.get("libro") else []
        if r.get("url2"): out.append(f"📄 **Receta escrita:** <{r['url2']}>")
        return ["  \n".join(out)] if out else []
    out = [f"▶ **Vídeo:** <{r['url']}>"]
    if r.get("url2"):
        out.append(f"▶ **Otro vídeo:** <{r['url2']}>" if "youtube.com" in r["url2"] else f"📄 **Receta escrita:** <{r['url2']}>")
    return ["  \n".join(out)]

def receta_md(k):
    r = R[k]; out = [f"### {r['nombre']}"]
    out.append(f"*Fuente: {r['fuente']} · {mac(k)} · por persona*\n")
    e = enlaces(r)
    if e: out += e + [""]
    for h, ings in r["grupos"]:
        out.append(f"**Ingredientes ({h}):**" if len(r["grupos"]) > 1 else "**Ingredientes:**")
        out += [f"- {texto(t, 2)}." for _c, _q, t in ings]
        out.append("")
    out.append("**Instrucciones:**")
    out += [f"{i}. {texto(p, 2)}" for i, p in enumerate(r["pasos"], 1)]
    out.append("")
    if k in VARIANTES:
        v = VARIANTES[k]; out.append(f"*Día de descanso:* {texto(R[v]['nota'], 2).split(': ', 1)[1]} ({mac(v)} por persona).")
    if r.get("tupper"): out.append(f"*Tupper:* {r['tupper']}.")
    if r.get("batch"): out.append(f"*Batch cooking:* {r['batch']}")
    if k in CAMBIOS: out.append(f"*Cambios respecto a la fuente:* {CAMBIOS[k]}")
    return "\n".join(out)

def recetas_file():
    cab = ["# Recetas de Vídeos e Internet (Otoño)", "",
           "*Nota: cantidades para **2 personas** (los dos coméis lo mismo). Las kcal y los macros son por persona, aproximados, calculados con valores medios por 100 g y etiquetas de Mercadona.*", "",
           "*Todas vienen de vídeos de YouTube o recetas de internet (enlace en cada una) y están adaptadas a `PERFIL.md` y a tus normas: solomillos en vez de contramuslos, merluza siempre rebozada, nada de lechuga, espinacas, pepinillos ni quesos curados.*", "",
           "*Las 6 cenas de tus vídeos (tacos, crispy, fajitas, kebab, fingers y Big Mac) siguen en `fast_food_saludable.md`. Cada receta dice qué se adelanta en el batch cooking del domingo (paso a paso en `batch_cooking.md`); el pescado se cocina siempre el día que se come.*", "", "---", "", "## Comidas", ""]
    cuerpo = []
    for k in COMIDAS: cuerpo += [receta_md(k), "", "---", ""]
    cuerpo += ["## Cenas", ""]
    for k in CENAS: cuerpo += [receta_md(k), "", "---", ""]
    return "\n".join(cab + cuerpo).rstrip("-\n ") + "\n"

def robot_file():
    cab = ["# Recetas del Robot Cecotec", "",
           "*Nota: cantidades para **2 personas** (los dos coméis lo mismo). Las kcal y los macros son por persona y aproximados.*", "",
           "*Sacadas del libro de recetas del robot Cecotec (fotos del 25 de octubre) y adaptadas a `PERFIL.md`: sin vino (alcohol 51), mantequilla (45), parmesano (queso curado 55) ni espinacas (41); con menos aceite y jamón, caldo bajo en sal y garbanzos de bote. Los programas son los del libro (velocidad, temperatura y tiempo), para vuestra Mambo.*", "",
           "*Cada receta dice qué se adelanta en el batch cooking del domingo (paso a paso en `batch_cooking.md`).*", "", "---", "", "## Comidas", ""]
    cuerpo = []
    for tipo, titulo in [("comida", None), ("cena", "## Cenas")]:
        if titulo: cuerpo += [titulo, ""]
        for k in [k for k in ROBOT if R[k]["tipo"] == tipo]: cuerpo += [receta_md(k), "", "---", ""]
    return "\n".join(cab + cuerpo).rstrip("-\n ") + "\n"

def fecha(f):
    _, m, d = f.split("-"); return f"{int(d)} {MESES[m]}"

def menu_md(s):
    out = [f"# Menú Semana {s['num']} ({s['titulo']})", "",
           "*Nota: las recetas de `recetas/` vienen para 2 personas; las kcal y la proteína de esta tabla son por persona. 🎬 = receta de vídeo o internet, con su enlace en el fichero de recetas; 🤖 = receta del libro del robot Cecotec. E = entreno, D = descanso.*", "",
           "| Día | Desayuno | Comida | Merienda | Cena | Total del día |", "| :--- | :--- | :--- | :--- | :--- | :--- |"]
    for i, fila in enumerate(s["filas"]):
        d, c, m, ce = fila
        kc, p = total_dia(fila)
        nom = lambda k: ("🎬 " if R[k].get("url") else "🤖 " if R[k].get("robot") else "🎬 " if R[k].get("url2") else "") + R[k]["nombre"]
        cena = "**Cena fuera** + *cervezas*" + (" — o en casa: 🎬 Big Mac Fit" if i == 5 else "") if ce == FUERA else nom(ce)
        tot = f"≈{kc:.0f} kcal · {p:.0f} g prot." + (" + cena fuera" if ce == FUERA else "")
        out.append(f"| **{DIAS[i]} {fecha(s['fechas'][i])} ({TIPO[i]})** | {nom(d)} | {nom(c)} | {nom(m)} | {cena} | {tot} |")
    b = BATCH[s["num"]]
    out += ["", f"**Batch cooking del {b['dia'].lower()}:** {b['duracion']}. Paso a paso en `recetas/batch_cooking.md`.",
            "- **A la nevera:** " + "; ".join(b["nevera"]) + ".",
            "- **Al congelador** (pásalo a la nevera la noche antes): " + "; ".join(b["congelador"]) + "."]
    out += ["", "**Recordatorios de la semana:**"] + [f"- **{dia}:** {txt}" for dia, txt in PREP[s["num"]]]
    out += ["", "**Dónde está cada receta:**",
            "- Desayunos: `recetas/desayunos.md` · Meriendas: `recetas/meriendas.md`",
            "- Comidas y cenas nuevas: `recetas/recetas_videos_internet.md` · Cenas de tus vídeos: `recetas/fast_food_saludable.md` · Recetas del robot: `recetas/recetas_robot_cecotec.md`",
            "- Batch cooking del domingo, paso a paso: `recetas/batch_cooking.md`"]
    return "\n".join(out) + "\n"

def lista_md(s):
    out = [f"# Lista de la Compra - Semana {s['num']} ({s['titulo']})", "",
           "*Nota: cantidades para los dos (x2), calculadas sumando las recetas del menú de esta semana. La merienda también va para los dos: si un día merienda solo uno, sobra la mitad de natillas, plátanos y kiwis.*", "",
           "*Truco: compra el pescado congelado. Casi todo el pollo se cocina o se marina en el batch del domingo; el del fin de semana va crudo al congelador y se pasa a la nevera la noche antes (ver «Recordatorios de la semana» en el menú).*", ""]
    if s["num"] in NOTA_COMPRA: out += [f"> **Ojo:** {NOTA_COMPRA[s['num']]}", ""]
    for sec, items in lista(s).items():
        out.append(f"## {sec}")
        for it in items:
            cant = "" if it["cant"] == "—" else it["cant"] + " "
            nota = f" ({it['nota']})" if it["nota"] else ""
            out.append(f"- {cant}{it['nombre']}{nota}")
        out.append("")
    out += ["## Opcional: Big Mac en casa el sábado (x2)", "*Solo si el sábado cenáis en casa en vez de fuera (receta en `recetas/fast_food_saludable.md`).*"]
    for it in opcional_bigmac():
        cant = "" if it["cant"] == "—" else it["cant"] + " "
        out.append(f"- {cant}{it['nombre']}" + (f" ({it['nota']})" if it["nota"] else ""))
    return "\n".join(out) + "\n"

def batch_md():
    out = ["# Batch Cooking del Domingo", "",
           "*El domingo se cocinan de una vez las comidas de lunes a viernes, que van en táper, y se adelanta lo que se pueda de las cenas. Cantidades para los dos (x2): son las de las recetas multiplicadas por las raciones de cada plato.*", "",
           "**Normas:**"] + [f"- {n}" for n in NORMAS] + [""]
    for s in SEMANAS:
        b = BATCH[s["num"]]
        out += ["---", "", f"## Semana {s['num']} ({s['titulo']}) · {b['dia']}", "", f"*Duración: {b['duracion']}.*", "",
                "**A la nevera:**"] + [f"- {x}" for x in b["nevera"]] + ["", "**Al congelador** (pásalo a la nevera la noche antes):"] + [f"- {x}" for x in b["congelador"]]
        out += ["", "**Paso a paso:**", "", "| Hora | Dónde | Qué hacer |", "| :--- | :--- | :--- |"]
        out += [f"| {h} | {donde} | {txt} |" for h, donde, txt in b["pasos"]]
        out += ["", "**Recordatorios de la semana:**"] + [f"- **{dia}:** {txt}" for dia, txt in b["recordatorios"]] + [""]
    return "\n".join(out)

if __name__ == "__main__":
    (REPO / "recetas" / "batch_cooking.md").write_text(batch_md())
    (REPO / "recetas" / "recetas_videos_internet.md").write_text(recetas_file())
    (REPO / "recetas" / "recetas_robot_cecotec.md").write_text(robot_file())
    for s in SEMANAS:
        (REPO / "menus" / f"semana_{s['num']:02d}.md").write_text(menu_md(s))
        (REPO / "listas_compra" / f"lista_semana_{s['num']:02d}.md").write_text(lista_md(s))
    print("Escritos: batch_cooking.md, recetas_videos_internet.md, recetas_robot_cecotec.md, semana_03..06.md, lista_semana_03..06.md")
