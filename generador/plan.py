from recetas_base import R as R0
from recetas_lentejas import R as R1
from recetas_lara_comidas import R as R2
from recetas_lara_cenas import R as R3
from recetas_pescado import R as R4
from recetas_cecotec import R as R5
from lib import macros_receta
R = {**R0, **R1, **R2, **R3, **R4, **R5}
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
TIPO = ["E", "E", "D", "E", "E", "D", "D"]
FUERA = "FUERA"
def semana(num, inicio, mes_ini, filas, prep):
    return dict(num=num, inicio=inicio, filas=filas, prep=prep)
SEMANAS = [
 dict(num=3, titulo="26 oct – 1 nov", fechas=["2026-10-26","2026-10-27","2026-10-28","2026-10-29","2026-10-30","2026-10-31","2026-11-01"],
   filas=[("D4L","LENT1","ME_E","FCE"), ("D1","LENT1","ME_E","PZA"), ("D2","PILPIL","ME_D","FAJ"), ("D3","TOFU","ME_E","KEB"),
          ("D4","GUIS_T","ME_E",FUERA), ("D4S","BBQ","ME_D",FUERA), ("D2","FISHCHIPS","ME_D","FIN")]),
 dict(num=4, titulo="2 – 8 nov", fechas=["2026-11-02","2026-11-03","2026-11-04","2026-11-05","2026-11-06","2026-11-07","2026-11-08"],
   filas=[("D3","LENT2","ME_E","TAC"), ("D4L","LENT2","ME_E","TERESC"), ("D2","POTG","ME_D","TOM"), ("D1","GUIS_T","ME_E","CRI"),
          ("D3","GUIS_T","ME_E",FUERA), ("D4S","MERTAC","ME_D",FUERA), ("D4L","BURR","ME_D","CREMCAL")]),
 dict(num=5, titulo="9 – 15 nov", fechas=["2026-11-09","2026-11-10","2026-11-11","2026-11-12","2026-11-13","2026-11-14","2026-11-15"],
   filas=[("D4L","LENTJ","ME_E","PZA"), ("D1","LENTJ","ME_E","RISOT"), ("D2","CURRY","ME_D","TOR"), ("D3","ALBON","ME_E","CRI"),
          ("D4","VIZCA_A","ME_E",FUERA), ("D4S","BBQ","ME_D",FUERA), ("D2","ARRGAMB","ME_D","FIN")]),
 dict(num=6, titulo="16 – 22 nov", fechas=["2026-11-16","2026-11-17","2026-11-18","2026-11-19","2026-11-20","2026-11-21","2026-11-22"],
   filas=[("D3","LENT2","ME_E","KEB"), ("D4L","LENT2","ME_E","TAC"), ("D2","JARD","ME_D","FAJ"), ("D1","ARRPOL","ME_E","PZA"),
          ("D3","TOFU","ME_E",FUERA), ("D4S","FISHCHIPS","ME_D",FUERA), ("D4L","BURR","ME_D","CREMZAN")]),
]
def total_dia(fila):
    k = p = 0
    for clave in fila:
        if clave != FUERA:
            kc, pr, _, _ = macros_receta(R[clave]); k += kc; p += pr
    return k, p
PESCADOS = {"merluza": "merluza", "bacalao": "bacalao", "gambas": "gambas", "gambones": "gambas", "calamar": "calamar",
            "sepia": "sepia", "pulpo": "pulpo", "atun": "atún", "atun_fresco": "atún"}
def pescados_semana(s):
    out = set()
    for fila in s["filas"]:
        for clave in fila:
            if clave != FUERA:
                out |= {PESCADOS[c] for _, ings in R[clave]["grupos"] for c, _q, _t in ings if c in PESCADOS}
    return out
def comprobar_pescados():
    """Errores de la norma: merluza y bacalao nunca en la misma semana; ningún pescado ni marisco dos semanas seguidas."""
    errores, previa = [], None
    for s in SEMANAS:
        p = pescados_semana(s)
        if {"merluza", "bacalao"} <= p: errores.append(f"Semana {s['num']}: merluza y bacalao en la misma semana")
        if previa is not None and p & previa: errores.append(f"Semanas {s['num'] - 1} y {s['num']}: {', '.join(sorted(p & previa))} dos semanas seguidas")
        previa = p
    return errores
if __name__ == "__main__":
    for s in SEMANAS: print(f"Semana {s['num']}: {', '.join(sorted(pescados_semana(s))) or '—'}")
    for e in comprobar_pescados(): print("  NORMA:", e)
    for s in SEMANAS:
        print(f"\nSemana {s['num']} ({s['titulo']})")
        for i, fila in enumerate(s["filas"]):
            k, p = total_dia(fila)
            obj = 1950 if TIPO[i] == "E" else 1600
            nota = "  + cena fuera" if fila[3] == FUERA else f"  ({k-obj:+.0f} vs {obj})"
            print(f"  {DIAS[i]:10s} {TIPO[i]}  {k:5.0f} kcal  {p:5.0f} g prot  {' / '.join(fila)}{nota}")

CAMBIOS = {
 "LENT1": "Solomillos en vez de contramuslo, mucho menos aceite y sin chorizo; pimiento rojo en vez de calabacín; la patata es el extra para días de entreno.",
 "LENT2": "Pavo añadido (la original es vegana) y 80 g de lentejas en vez de 150; el arroz es el extra para días de entreno.",
 "GARBAC": "Tomate triturado natural en vez de tomate frito; versión sin espinacas.",
 "VIZCA": "Sin vino ni coñac, la mitad de ajo, aceite medido y sofrito tapado para gastar menos aceite.",
 "FISHCHIPS": "Merluza rebozada al horno o airfryer en vez de frita con cerveza; tártara de yogur con alcaparras (sin pepinillos); guisantes con AOVE en vez de mantequilla.",
 "MERTAC": "Rebozado al horno en vez de frito; yogur en vez de queso fresco; canónigos en vez de col.",
 "TOFU": "Tomate triturado natural en vez de frito; mozzarella fresca en vez de rallada.",
 "TOFU_D": "Tomate triturado natural en vez de frito; mozzarella fresca en vez de rallada.",
 "GUIS": "Tosta de atún en vez de salmón ahumado con queso crema; huevo añadido para más proteína.",
 "GUIS_D": "Huevo añadido para más proteína.",
 "BBQ": "Solomillos en vez de alitas; mozzarella en vez de queso de cabra; granada en vez de higos.",
 "CURRY": "Mozzarella fresca en vez de rallada; sin nata ni leche de coco.",
 "BURR": "Canónigos en vez de lechuga, tomate triturado en vez de frito y aguacate en vez de guacamole.",
 "TOR": "Más claras y algo menos de patata para subir la proteína.",
 "PZA": "Yogur +Proteínas y mozzarella light; jamón cocido extra en vez del bonito del vídeo (no queréis atún); masa algo más pequeña.",
 "TAT": "Atún en vez de salmón (el salmón sale alto en tu test).",
 "FCE": "Yogur +Proteínas en vez de cottage, un huevo cambiado por claras y sin calabacín (más pimiento).",
 "TOM": "Mozzarella light en vez de queso rallado; más huevo y pollo para llegar a la proteína.",
 "FPZ": "Mozzarella light en vez de queso rallado y brie; tomate triturado; pollo añadido.",
 "BEX": "Canónigos en vez de lechuga; pollo en vez de carne picada sobrante.",
 "VIZCA_A": "Sin vino ni coñac, la mitad de ajo, aceite medido y sofrito tapado para gastar menos aceite; arroz integral en vez de patata para que el táper aguante y se pueda congelar.",
 "GUIS_T": "Huevo cocido para más proteína y patata en dados para que sea un plato completo de táper.",
 "LENTJ": "Más lenteja y verdura por persona y la mitad de ajo; caldo bajo en sal en vez de la pastilla; huevo duro y patata para que sea un plato completo. El libro es para 6, y en la foto no se ve la temperatura del sofrito: 120 °C.",
 "POTG": "Garbanzos de bote y más cantidad; acelgas en vez de espinacas (41 en tu test); medio diente de ajo por persona; caldo de verduras bajo en sal.",
 "JARD": "Sin vino (alcohol 51 en tu test), con más caldo; la mitad de aceite y de jamón; algo menos de carne y de patata por persona.",
 "ARRPOL": "Solomillos en dados en vez de pollo deshuesado picado; menos arroz y aceite; caldo bajo en sal. El libro lo deja hasta 1 hora: con solomillos basta con que hierva antes de echar el arroz. Judías verdes: no salen en tu test y las has aceptado, aunque son de la misma planta que las alubias (47).",
 "TERESC": "Caldo y un poco de balsámico en vez del vino tinto (alcohol 51 en tu test); la verdura del escalfado, triturada, hace de salsa; patata y canónigos de guarnición.",
 "ALBON": "Al horno o en la airfryer en vez de rebozadas en harina y fritas; pan integral en vez de pan de molde; menos ajo; con salsa de tomate y verduras y arroz integral para que sea un plato completo. La ternera y el cerdo magros salen bien en tu test.",
 "RIOJ": "Sin azúcar; la mitad de ajo y el aceite medido; una sola cebolla, en la salsa (Arguiñano rehoga otra aparte); con patata para que sea un plato completo de táper.",
 "PILPIL": "Menos aceite en la salsa (el que sobra, colado, sirve para cocinar), un diente de ajo por persona que puedes no comerte, y patata cocida y pimiento asado de guarnición, como lo sirve Arguiñano pero sin freír los pimientos.",
 "CREMCAL": "AOVE en vez de mantequilla (45 en tu test); pipas de calabaza por encima y una tortilla de claras con pavo de segundo para llegar a la proteína. La web no dice raciones: cantidades calculadas para 4 y pasadas a 2.",
 "CREMZAN": "Leche normal en vez de evaporada; caldo bajo en sal; calamar a la plancha por encima para llegar a la proteína (en vez de gambas, que ya hay el domingo anterior). La web no dice raciones: cantidades calculadas para 4 y pasadas a 2.",
 "ARRGAMB": "Gambones enteros en vez de colas peladas, para hacer el fumet con sus cabezas (lo que propone la receta si no tienes caldo); 70 g de arroz por persona en vez de 100 y el aceite medido.",
 "RISOT": "Con pollo; sin mantequilla (45) ni parmesano (queso curado 55): un poco de mozzarella fresca al final; sin vino; más puerro y setas (no champiñón, 43 en tu test); menos jamón y caldo bajo en sal.",
}
from batch import BATCH, NORMAS
NOTA_COMPRA = {
 3: "La compra de esta semana ya está hecha (sábado 24). Con los cambios solo falta: 140 g de jamón cocido extra para la pizza del martes, un pimiento rojo para el pil pil y la fajicesta y una guindilla o cayena si no tenéis. Os sobran 2 latas de atún y 400 g de garbanzos (los garbanzos, para el potaje del miércoles 4).",
 4: "No compréis los garbanzos: os sobran de la semana pasada (ya no los lleva el bacalao).",
 5: "La compra de esta semana ya está hecha. El domingo 15 ya no hay tacos de merluza, sino arroz meloso con gambones: el sábado 14, con la compra de la semana 6, añadid 500 g de gambones crudos congelados (unos 12), 140 g de arroz bomba (o redondo, si os queda), 60 g más de pimiento rojo y 30 g de verde, media cebolla, un trozo de puerro (40 g), 120 g de tomate triturado y azafrán si no tenéis. Si ya comprasteis la merluza (340 g), dejadla en el congelador para el fish & chips del sábado 21; las tortillas de maíz, la piña y la lima os sobran.",
 6: "Si comprasteis la merluza de los tacos de la semana pasada (340 g), no compréis más: os vale para el fish & chips del sábado 21.",
}
PREP = {n: b['recordatorios'] for n, b in BATCH.items()}
