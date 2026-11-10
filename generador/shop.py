"""Lista de la compra semanal (x2) a partir del plan."""
import math
from collections import defaultdict, OrderedDict
from plan import R, SEMANAS, FUERA
from nutri import T

SECS = ["Fruta y verdura", "Carne, huevos y tofu", "Pescado", "Lácteos", "Pan y tortillas", "Despensa", "Congelados", "Especias y condimentos"]
def g(v):
    v = round(v / 10) * 10 if v >= 100 else round(v / 5) * 5
    return f"{str(round(v/1000, 2)).rstrip('0').rstrip('.').replace('.', ',')} kg" if v >= 1000 else f"{int(v)} g"
def ml(v):
    v = round(v / 10) * 10
    return f"{str(round(v/1000, 2)).rstrip('0').rstrip('.').replace('.', ',')} L" if v >= 1000 else f"{int(v)} ml"
def ud(v, n): return math.ceil(v / n - 1e-9)
def docenas(n):   # medias docenas, con al menos 1 huevo de margen
    medias = math.ceil((n + 1) / 6)
    return {2: "1 docena", 3: "docena y media"}.get(medias) or (f"{medias // 2} docenas" + (" y media" if medias % 2 else ""))
# clave -> (sección, nombre, función que formatea el total x2 -> (cantidad, nota))
M = {
 "platano": ("Fruta y verdura", "Plátanos", None), "kiwi": ("Fruta y verdura", "Kiwis", None),
 "granada": ("Fruta y verdura", "Granada", lambda v: (f"{ud(v,150)}", f"se usan {g(v)} de granos")),
 "pina": ("Fruta y verdura", "Piña natural", lambda v: ("1 trozo", f"unos {g(v)}")),
 "aguacate": ("Fruta y verdura", "Aguacates", lambda v: (f"{ud(v,140)}", f"unos {g(v)} de pulpa")),
 "pimiento": ("Fruta y verdura", "Pimientos rojos o de colores", lambda v: (g(v), "")),
 "pim_verde": ("Fruta y verdura", "Pimientos verdes italianos", lambda v: (g(v), "")),
 "cebolla": ("Fruta y verdura", "Cebollas", lambda v: (g(v), "incluye cebolleta y morada")),
 "calabacin": ("Fruta y verdura", "Calabacines", lambda v: (g(v), "")),
 "zanahoria": ("Fruta y verdura", "Zanahorias", lambda v: (g(v), "")),
 "tomate": ("Fruta y verdura", "Tomates", lambda v: (g(v), "incluye cherrys")),
 "patata": ("Fruta y verdura", "Patatas", lambda v: (g(v), "")),
 "calabaza": ("Fruta y verdura", "Calabaza", lambda v: (g(v), "pelada")),
 "puerro": ("Fruta y verdura", "Puerros", lambda v: (g(v), "")),
 "acelgas": ("Fruta y verdura", "Acelgas", lambda v: (g(v), "")),
 "setas": ("Fruta y verdura", "Setas de cardo u ostra", lambda v: (g(v), "no champiñón")),
 "hojas": ("Fruta y verdura", "Rúcula o canónigos", lambda v: (f"{ud(v,125)} bolsa{'s' if ud(v,125) > 1 else ''}", f"unos {g(v)}")),
 "remolacha": ("Fruta y verdura", "Remolacha cocida", lambda v: ("1 paquete", f"se usan {g(v)}")),
 "huevo": ("Carne, huevos y tofu", "Huevos", lambda v: (docenas(ud(v,55)), f"se usan {ud(v,55)}")),
 "clara": ("Carne, huevos y tofu", "Claras de huevo pasteurizadas", lambda v: (ml(v), "")),
 "pechuga": ("Carne, huevos y tofu", "Pechuga de pollo", lambda v: (g(v), "")),
 "solomillo": ("Carne, huevos y tofu", "Solomillos de pollo", lambda v: (g(v), "")),
 "pavo": ("Carne, huevos y tofu", "Pechuga o solomillo de pavo", lambda v: (g(v), "")),
 "pavo_fiambre": ("Carne, huevos y tofu", "Pechuga de pavo en lonchas (92 % carne)", lambda v: (g(v), "")),
 "jamon_serrano": ("Carne, huevos y tofu", "Taquitos de jamón serrano", lambda v: (g(v), "")),
 "jamon_cocido": ("Carne, huevos y tofu", "Jamón cocido extra", lambda v: (g(v), "")),
 "tofu": ("Carne, huevos y tofu", "Tofu firme", lambda v: (g(v), f"{ud(v,400)} bloques de 400 g")),
 "picada_mixta": ("Carne, huevos y tofu", "Carne picada magra, mitad ternera y mitad cerdo", lambda v: (g(v), "pídela en la carnicería y cocínala en 24 horas")),
 "ternera_pieza": ("Carne, huevos y tofu", "Ternera en una pieza para escalfar", lambda v: (g(v), "redondo, tapa o contra")),
 "ternera_guiso": ("Carne, huevos y tofu", "Ternera para guisar en tacos", lambda v: (g(v), "morcillo, aguja o llana, sin grasa visible")),
 "ternera": ("Carne, huevos y tofu", "Carne picada de ternera magra", lambda v: (g(v), "carnicería: tapilla o babilla; cómprala el día que la cocines")),
 "gambas": ("Pescado", "Gambas o langostinos pelados congelados", lambda v: (g(v), "")),
 "merluza": ("Pescado", "Merluza congelada (lomos o filetes)", lambda v: (g(v), "")),
 "gambones": ("Pescado", "Gambones crudos congelados, enteros", lambda v: (g(v), f"unos {round(v / 42)}")),
 "calamar": ("Pescado", "Calamar limpio congelado (tubos o tiras)", lambda v: (g(v), "")),
 "bacalao": ("Pescado", "Lomos de bacalao congelados", lambda v: (g(v), "mira si son desalados")),
 "atun_fresco": ("Pescado", "Tacos de atún congelados", lambda v: (g(v), "")),
 "atun": ("Pescado", "Latas de atún al natural", lambda v: (f"{ud(v,60)}", f"{g(v)} escurrido")),
 "yogur": ("Lácteos", "Yogures naturales sin azúcar", lambda v: (f"{ud(v,125)}", "de 125 g")),
 "yogur_prot": ("Lácteos", "Yogur +Proteínas natural", lambda v: (f"{ud(v,120)}", "vasitos de 120 g, en packs de 4")),
 "natillas": ("Lácteos", "Natillas +Proteínas", lambda v: (f"{ud(v,120)}", f"{ud(ud(v,120),4)} packs de 4")),
 "mozzarella": ("Lácteos", "Mozzarella fresca", lambda v: (f"{ud(v,125)} {'bola' if ud(v,125)==1 else 'bolas'}", f"se usan {g(v)}")),
 "mozza_light": ("Lácteos", "Mozzarella fresca light", lambda v: (f"{ud(v,125)} {'bola' if ud(v,125)==1 else 'bolas'}", f"se usan {g(v)}")),
 "leche": ("Lácteos", "Leche o bebida de soja sin azúcar", lambda v: (ml(v), "")),
 "pan_int": ("Pan y tortillas", "Pan integral", lambda v: (g(v), "100% integral")),
 "pan_pueblo": ("Pan y tortillas", "Pan de pueblo", lambda v: ("1 trozo", g(v)) if v < 60 else (g(v), "")),
 "pan_cristal": ("Pan y tortillas", "Panes de cristal", lambda v: (f"{ud(v,70)}", "o de hamburguesa 100% integrales")),
 "pita": ("Pan y tortillas", "Panes de pita", lambda v: (f"{ud(v,60)}", "mejor integrales")),
 "tortilla_int": ("Pan y tortillas", "Tortillas integrales", lambda v: (f"{ud(v,36)}", "paquete de 10")),
 "tortilla_maiz": ("Pan y tortillas", "Tortillas de maíz", lambda v: (f"{ud(v,26)}", "paquete de 8")),
 "pan_burger": ("Pan y tortillas", "Panes de hamburguesa 100% integrales", lambda v: (f"{ud(v,75)}", "")),
 "ketchup0": ("Despensa", "Ketchup sin azúcar", lambda v: ("1", "si no te queda")),
 "guindilla": ("Despensa", "Guindillas en vinagre", lambda v: ("1 bote", "")),
 "piadina": ("Pan y tortillas", "Piadinas", lambda v: (f"{ud(v,100)}", "")),
 "lentejas": ("Despensa", "Lenteja pardina", lambda v: (g(v), "")),
 "garbanzos": ("Despensa", "Garbanzos cocidos", lambda v: (g(v), f"escurridos, unos {ud(v,250)} botes")),
 "arroz_int": ("Despensa", "Arroz integral", lambda v: (g(v), "")),
 "arroz": ("Despensa", "Arroz redondo", lambda v: (g(v), "")),
 "pasta_int": ("Despensa", "Espaguetis integrales o normales", lambda v: (g(v), "mira si os quedan del paquete")),
 "avena": ("Despensa", "Copos de avena", lambda v: (g(v), "")),
 "copos_maiz": ("Despensa", "Copos de maíz sin azúcar", lambda v: (g(v), "para los rebozados")),
 "pipas": ("Despensa", "Pipas de calabaza sin sal", lambda v: (g(v), "")),
 "tomate_trit": ("Despensa", "Tomate triturado natural", lambda v: (g(v), "")),
 "tomate_conc": ("Despensa", "Tomate concentrado", lambda v: ("1", "tubo o lata pequeña; si no te queda")),
 "choricero": ("Despensa", "Carne de pimiento choricero", lambda v: ("1 bote", f"se usan {g(v)}")),
 "alcaparras": ("Despensa", "Alcaparras", lambda v: ("1 bote", f"se usan {g(v)}")),
 "aceitunas": ("Despensa", "Aceitunas negras", lambda v: ("1 lata", f"se usan {g(v)}")),
 "guisantes": ("Congelados", "Guisantes finos congelados", lambda v: (g(v), "")),
 "judias_verdes": ("Congelados", "Judías verdes troceadas congeladas", lambda v: (g(v), "")),
 "soja": ("Despensa", "Salsa de soja baja en sodio", lambda v: ("1", "si no te queda")),
 "mostaza": ("Despensa", "Mostaza", lambda v: ("1", "si no te queda")),
 "bbq0": ("Despensa", "Salsa barbacoa sin azúcar", lambda v: ("1", "si no te queda")),
 "balsamico": ("Despensa", "Vinagre balsámico", lambda v: ("1", "si no te queda; no crema de balsámico")),
 "caldo_pollo": ("Despensa", "Caldo de pollo bajo en sal", lambda v: (f"{ud(v,1000)} brik{'s' if ud(v,1000) > 1 else ''} de 1 L", f"se usan {ml(v)}")),
 "caldo_verd": ("Despensa", "Caldo de verduras bajo en sal", lambda v: (f"{ud(v,1000)} brik{'s' if ud(v,1000) > 1 else ''} de 1 L", f"se usan {ml(v)}")),
 "caldo": ("Despensa", "Caldo de pescado sin azúcar", lambda v: (ml(v), "o agua")),
 "aove": ("Despensa", "Aceite de oliva virgen extra", lambda v: (ml(v), "se usan esta semana")),
}
FRESCOS = {"Limones": "Limones", "Lima": "Limas", "Perejil": "Perejil", "Cilantro": "Cilantro", "Hierbabuena": "Hierbabuena"}
DESPENSA_X = {"Salsa picante": "Salsa picante (opcional)", "Caldo de pescado": None}
NORMAL = {"Curry": "Curry en polvo", "Sal": None}

def lista(semana, claves=None):
    tot = defaultdict(float); cuenta = defaultdict(int); extras = set()
    todas = claves if claves is not None else [c for fila in semana["filas"] for c in fila]
    for fila in [todas]:
        for clave in fila:
            if clave == FUERA: continue
            for _, ings in R[clave]["grupos"]:
                for c, q, _t in ings:
                    if not c: continue
                    if c.startswith("x:"): extras.add(c[2:]); continue
                    tot[c] += q * 2
                    if c in ("platano", "kiwi"): cuenta[c] += 2
    out = OrderedDict((s, []) for s in SECS)
    for c, v in tot.items():
        sec, nombre, f = M[c]
        if f is None: cant, nota = str(cuenta[c]), "desayunos y meriendas"
        else: cant, nota = f(v)
        out[sec].append(dict(id=c, cant=cant, nombre=nombre, nota=nota))
    for x in sorted(extras):
        if x in FRESCOS: out["Fruta y verdura"].append(dict(id="x-" + x, cant="—", nombre=FRESCOS[x], nota=""))
        elif x in DESPENSA_X:
            if DESPENSA_X[x]: out["Despensa"].append(dict(id="x-" + x, cant="—", nombre=DESPENSA_X[x], nota=""))
    if claves is not None:   # lista opcional: sin especias ni básicos
        orden = list(M.keys())
        for s in out: out[s].sort(key=lambda it: orden.index(it["id"]) if it["id"] in orden else 999)
        return OrderedDict((s, v) for s, v in out.items() if v)
    esp = sorted({NORMAL.get(x, x) for x in extras if x not in FRESCOS and x not in DESPENSA_X} - {None})
    out["Especias y condimentos"].append(dict(id="x-especias", cant="—", nombre=", ".join(esp), nota="revisa lo que tienes"))
    out["Especias y condimentos"].append(dict(id="x-basicos", cant="—", nombre="Sal, pimienta, ajo en polvo y cebolla en polvo", nota="básicos"))
    orden = list(M.keys())
    for s in out: out[s].sort(key=lambda it: orden.index(it["id"]) if it["id"] in orden else 999)
    return OrderedDict((s, v) for s, v in out.items() if v)

def opcional_bigmac():
    """Ingredientes x2 de la Big Mac del sábado en casa (sin lo que ya hay en casa)."""
    l = lista(None, claves=["FF2"])
    quitar = {"aove", "cebolla", "hojas", "mostaza", "yogur", "mozzarella"}
    items = [dict(it, id="o-" + it["id"]) for sec in l.values() for it in sec if it["id"] not in quitar]
    items.append(dict(id="o-resto", cant="—", nombre="Yogur, mozzarella, cebolla, canónigos y mostaza", nota="de la lista: añade 1 yogur y 40 g de mozzarella"))
    return items

if __name__ == "__main__":
    for s in SEMANAS:
        print(f"\n===== Semana {s['num']} ({s['titulo']})")
        for sec, items in lista(s).items():
            print(f"-- {sec}")
            for it in items: print(f"   {it['cant']:>14s}  {it['nombre']}" + (f"  ({it['nota']})" if it['nota'] else ""))
