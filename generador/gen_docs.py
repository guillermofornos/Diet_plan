"""HTML sencillo (sin CSS) para crear Google Docs: lista de la compra y menú+recetas de una semana."""
import html, re, sys
from pathlib import Path
from plan import R, SEMANAS, DIAS, TIPO, FUERA, CAMBIOS, PREP, BATCH, NORMAS, NOTA_COMPRA, total_dia
from shop import lista, opcional_bigmac
from lib import texto, macros_receta
e = html.escape
PAGINA = "https://claude.ai/artifact/6jMeaqcEyCZSnsCG5ZEGRA"
ENLACE = f'<p>📱 <b>Página del mes</b> (menú de cada día, batch paso a paso y lista con casillas): <a href="{PAGINA}">{PAGINA}</a></p>'
MESES = {"10": "oct", "11": "nov"}
def fecha(f): _, m, d = f.split("-"); return f"{int(d)} {MESES[m]}"

def doc_lista(s):
    b = [f"<h1>Lista de la compra · semana del {e(s['titulo'])}</h1>", ENLACE,
         "<p><i>Para los dos. Pescado congelado. Casi todo el pollo se cocina o se marina en el batch del domingo; el del fin de semana va crudo al congelador y se pasa a la nevera la noche antes.</i></p>"]
    if s["num"] in NOTA_COMPRA: b.append(f"<p>⚠️ <b>Ojo:</b> {e(NOTA_COMPRA[s['num']])}</p>")
    for sec, items in lista(s).items():
        b.append(f"<h2>{e(sec)}</h2>")
        b += [f"<p>☐ <b>{e(it['cant'])}</b> {e(it['nombre'])}" + (f" <i>({e(it['nota'])})</i>" if it["nota"] else "") + "</p>"
              if it["cant"] != "—" else f"<p>☐ {e(it['nombre'])}" + (f" <i>({e(it['nota'])})</i>" if it["nota"] else "") + "</p>" for it in items]
    b.append("<h2>Opcional · Big Mac en casa el sábado</h2><p><i>Solo si el sábado cenáis en casa. La carne picada, el mismo día que la cocinéis.</i></p>")
    for it in opcional_bigmac():
        b.append(f"<p>☐ " + (f"<b>{e(it['cant'])}</b> " if it["cant"] != "—" else "") + f"{e(it['nombre'])}" + (f" <i>({e(it['nota'])})</i>" if it["nota"] else "") + "</p>")
    return "<html><body>" + "".join(b) + "</body></html>"

def doc_recetas(s):
    nums = [int(f.split("-")[2]) for f in s["fechas"]]
    prep_dia = {i: [] for i in range(7)}; antes = []
    for etiqueta, txt in PREP[s["num"]]:
        n = int(re.search(r"\d+", etiqueta).group())
        momento = "Por la noche: " if "noche" in etiqueta else "Por la mañana: " if "mañana" in etiqueta else ""
        if n in nums: prep_dia[nums.index(n)].append(momento + (txt[0].lower() + txt[1:] if momento else txt))
        else: antes.append(f"{etiqueta}: {txt}")
    bt = BATCH[s["num"]]
    b = [f"<h1>Menú y recetas · semana del {e(s['titulo'])}</h1>", ENLACE,
         "<p><i>Cantidades para los dos (las del batch y las de las recetas). Kcal y proteína por persona. E = entreno, D = descanso. "
         "Las recetas de vídeo llevan el enlace al vídeo debajo del título.</i></p>"]
    for a in antes: b.append(f"<p><b>Antes de empezar.</b> {e(a)}</p>")
    b.append(f"<h2>Batch cooking · {e(bt['dia'].lower())}</h2>")
    b.append(f"<p><i>Las comidas de lunes a viernes, en táper, y lo que se adelanta de las cenas. Duración: {e(bt['duracion'])}.</i></p>")
    b.append("<p><b>Normas</b></p><ul>" + "".join(f"<li>{e(x)}</li>" for x in NORMAS) + "</ul>")
    b.append("<p><b>A la nevera</b></p><ul>" + "".join(f"<li>{e(x)}</li>" for x in bt["nevera"]) + "</ul>")
    b.append("<p><b>Al congelador</b> <i>(pásalo a la nevera la noche antes)</i></p><ul>" + "".join(f"<li>{e(x)}</li>" for x in bt["congelador"]) + "</ul>")
    b.append("<p><b>Paso a paso</b></p><ul>" + "".join(f"<li>☐ <b>{e(h)} · {e(donde)}.</b> {e(x)}</li>" for h, donde, x in bt["pasos"]) + "</ul>")
    b.append("<p><b>Recordatorios de la semana</b></p><ul>" + "".join(f"<li><b>{e(d)}:</b> {e(x)}</li>" for d, x in bt["recordatorios"]) + "</ul>")
    b.append("<h2>Menú de la semana</h2>")
    orden = []
    for i, fila in enumerate(s["filas"]):
        kc, p = total_dia(fila)
        b.append(f"<h3>{DIAS[i]} {fecha(s['fechas'][i])} ({TIPO[i]}) · ≈{kc:.0f} kcal, {p:.0f} g prot.{' + cena fuera' if fila[3] == FUERA else ''}</h3><ul>")
        for slot, k in zip(["Desayuno", "Comida", "Merienda", "Cena"], fila):
            if k == FUERA:
                b.append(f"<li><b>{slot}:</b> cena fuera + cervezas" + (" (o en casa: Big Mac Fit)" if i == 5 else "") + "</li>")
                if i == 5 and "FF2" not in orden: orden.append("FF2")
            else:
                b.append(f"<li><b>{slot}:</b> {e(R[k]['nombre'])}</li>")
                if k not in orden: orden.append(k)
        b.append("</ul>")
        for t in prep_dia[i]: b.append(f"<p><i>Recordatorio: {e(t)}</i></p>")
    tipo_orden = {"comida": 0, "cena": 1, "desayuno": 2, "merienda": 3}
    titulos = {0: "Comidas", 1: "Cenas", 2: "Desayunos", 3: "Meriendas"}
    actual = None
    for k in sorted(orden, key=lambda k: (tipo_orden[R[k]["tipo"]], orden.index(k))):
        r = R[k]; t = tipo_orden[r["tipo"]]
        if t != actual: b.append(f"<h2>{titulos[t]}</h2>"); actual = t
        kc, p, _, _ = macros_receta(r)
        meta = f"≈{kc:.0f} kcal y {p:.0f} g de proteína por persona" + (f" · {e(r['fuente'])}" if r.get("fuente") else "")
        b.append(f"<h3>{e(r['nombre'])}</h3><p><i>{meta}</i></p>")
        if r.get("url"):
            b.append(f'<p>▶ <b>Vídeo:</b> <a href="{e(r["url"])}">{e(r["url"])}</a></p>')
        elif r.get("libro"):
            b.append(f"<p>📖 Libro del robot Cecotec, {e(r['libro'])}</p>")
        if r.get("url2"):
            etiqueta = "▶ <b>Otro vídeo:</b>" if "youtube.com" in r["url2"] else "📄 <b>Receta escrita:</b>"
            b.append(f'<p>{etiqueta} <a href="{e(r["url2"])}">{e(r["url2"])}</a></p>')
        if r.get("nota"): b.append(f"<p><i>{e(texto(r['nota'], 2))}</i></p>")
        for gh, ings in r["grupos"]:
            b.append(f"<p><b>{e(gh)}</b></p><ul>" + "".join(f"<li>{e(texto(x, 2))}</li>" for _c, _q, x in ings) + "</ul>")
        b.append("<p><b>Preparación</b></p><ol>" + "".join(f"<li>{e(texto(x, 2))}</li>" for x in r["pasos"]) + "</ol>")
        if r.get("batch"): b.append(f"<p><b>Batch cooking:</b> {e(r['batch'])}</p>")
    return "<html><body>" + "".join(b) + "</body></html>"

if __name__ == "__main__":
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    s = next(x for x in SEMANAS if x["num"] == num)
    out = Path(__file__).resolve().parent / "salida" / "docs"; out.mkdir(parents=True, exist_ok=True)
    for nombre, txt in [("lista", doc_lista(s)), ("recetas", doc_recetas(s))]:
        (out / f"s{num}_{nombre}.html").write_text(txt)
        print(nombre, len(txt), "caracteres")
