"""Exporta los datos del plan a JSON y genera la página del mes."""
import json, re
from pathlib import Path
from plan import R, SEMANAS, DIAS, TIPO, FUERA, LIBRE, NO_PLATO, CAMBIOS, PREP, BATCH, NORMAS, NOTA_COMPRA, total_dia
from shop import lista, opcional_bigmac
from lib import macros_receta

MESES = {"10": "oct", "11": "nov", "12": "dic"}
MES_LARGO = {"10": "octubre", "11": "noviembre", "12": "diciembre"}
# La página lleva la semana en curso y el mes nuevo: así el enlace de Indi sirve siempre (se publica en la misma URL).
PAGINA = [7, 8, 9, 10, 11]
SEMANAS = [s for s in SEMANAS if s["num"] in PAGINA]
usadas = set()
for s in SEMANAS:
    for fila in s["filas"]: usadas |= {c for c in fila if c not in NO_PLATO}
usadas.add("FF2")
recetas = {}
for k in sorted(usadas):
    r = R[k]; kc, p, g, h = macros_receta(r)
    recetas[k] = dict(nombre=r["nombre"], tipo=r["tipo"], fuente=r.get("fuente"), url=r.get("url"), url2=r.get("url2"), robot=r.get("robot"), libro=r.get("libro"),
                      kcal=round(kc), prot=round(p), hc=round(h), grasa=round(g), tupper=r.get("tupper"), batch=r.get("batch"), nota=r.get("nota"),
                      cambios=CAMBIOS.get(k), grupos=[[gh, [t for _c, _q, t in ings]] for gh, ings in r["grupos"]], pasos=r["pasos"])
semanas = []
for s in SEMANAS:
    nums = [int(f.split("-")[2]) for f in s["fechas"]]
    prep_dia = {i: [] for i in range(7)}; antes = []
    for etiqueta, txt in PREP[s["num"]]:
        n = int(re.search(r"\d+", etiqueta).group())
        momento = "Por la noche: " if "noche" in etiqueta else "Por la mañana: " if "mañana" in etiqueta else ""
        if n in nums: prep_dia[nums.index(n)].append(momento + (txt[0].lower() + txt[1:] if momento else txt))
        else: antes.append(f"{etiqueta}: {txt}")
    dias = []
    for i, fila in enumerate(s["filas"]):
        kc, p = total_dia(fila); _, m, d = s["fechas"][i].split("-")
        dias.append(dict(nombre=DIAS[i], fecha=s["fechas"][i], n=int(d), mes=MESES[m], tipo=TIPO[i], kcal=round(kc), prot=round(p),
                         fuera=fila[3] == FUERA, libre=("comida y cena libres" if fila[1] == LIBRE else "cena libre") if fila[3] == LIBRE else "", comidas=[["Desayuno", fila[0]], ["Comida", fila[1]], ["Merienda", fila[2]], ["Cena", fila[3]]],
                         prep=prep_dia[i]))
    compra = [dict(h=sec, items=items) for sec, items in lista(s).items()]
    semanas.append(dict(num=s["num"], titulo=s["titulo"], corto=f"{dias[0]['n']} {dias[0]['mes']}", inicio=s["fechas"][0], fin=s["fechas"][-1],
                        antes=antes, dias=dias, compra=compra, opcional=opcional_bigmac(), batch=BATCH[s["num"]], nota_compra=NOTA_COMPRA.get(s["num"])))
data = dict(recetas=recetas, semanas=semanas, normas=NORMAS)
AQUI = Path(__file__).resolve().parent
plantilla = (AQUI / "plantilla.html").read_text()
def largo(f): _, m, d = f.split("-"); return f"{int(d)} de {MES_LARGO[m]}"
ini, fin = SEMANAS[0]["fechas"][0], SEMANAS[-1]["fechas"][-1]
html = (plantilla.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False))
        .replace("__EYEBROW__", f"Semanas {SEMANAS[0]['num']} a {SEMANAS[-1]['num']} · Plan 91 → 81 kg")
        .replace("__TITULO__", f"Del {largo(ini)} al {largo(fin)}")
        .replace("__INICIO__", str(int(ini.split("-")[2]))))
SALIDA = AQUI / "salida"; SALIDA.mkdir(exist_ok=True)
(SALIDA / "menu_mes.html").write_text(html)
print("OK", len(recetas), "recetas,", sum(len(s["dias"]) for s in semanas), "días,", len(html.encode()) // 1024, "KB")
