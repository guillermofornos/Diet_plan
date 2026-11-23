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
LIBRE = "LIBRE"   # comida o cena sin plan (día libre)
NO_PLATO = (FUERA, LIBRE)
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
 dict(num=7, titulo="23 – 29 nov", fechas=["2026-11-23","2026-11-24","2026-11-25","2026-11-26","2026-11-27","2026-11-28","2026-11-29"],
   filas=[("D4L","LENT1","ME_E","CREMVER"), ("D3","PULPO","ME_E","CENAV"), ("D2","CURRY","ME_D","CREMCAL"), ("D3","CARNEG","ME_E","CRI"),
          ("D4","TERI","ME_E",FUERA), ("D4S","RODA","ME_D",FUERA), ("D2",LIBRE,"ME_D",LIBRE)]),
 dict(num=8, titulo="30 nov – 6 dic", fechas=["2026-11-30","2026-12-01","2026-12-02","2026-12-03","2026-12-04","2026-12-05","2026-12-06"],
   filas=[("D1","LENTJ","ME_E","FAJ"), ("D4","ALBON","ME_E","SOPA"), ("D2","ESTOF","ME_D","SANDTOR"), ("D1","POTG","ME_E","KEB"),
          ("D4","ARRPOL","ME_E",FUERA), ("D4S","DORSAL","ME_D",FUERA), ("D2","ARRGAMB","ME_D","CASTA")]),
 dict(num=9, titulo="7 – 13 dic", fechas=["2026-12-07","2026-12-08","2026-12-09","2026-12-10","2026-12-11","2026-12-12","2026-12-13"],
   filas=[("D4L","LENT2","ME_E","TAC"), ("D1","SOLPIQ","ME_E","CREMCAL"), ("D4S","CURRY","ME_D","SANDMIX"), ("D4","TOFU","ME_E","TOM"),
          ("D4","TERI","ME_E",FUERA), ("D4S","SALM2","ME_D",FUERA), ("D2","LUBSAL","ME_D","CREMVER")]),
 dict(num=10, titulo="14 – 20 dic", fechas=["2026-12-14","2026-12-15","2026-12-16","2026-12-17","2026-12-18","2026-12-19","2026-12-20"],
   filas=[("D4","LENT1","ME_E","PZA"), ("D1","BBQ","ME_E","SANDTOR"), ("D2","ESTOF","ME_D","SANDPOL"), ("D1","ALBON","ME_E","TOR"),
          ("D4","ARRPOL","ME_E",FUERA), ("D4S","ARRSEC","ME_D",FUERA), ("D2","RAPE","ME_D","CASTA")]),
 dict(num=11, titulo="21 – 27 dic", fechas=["2026-12-21","2026-12-22","2026-12-23","2026-12-24","2026-12-25","2026-12-26","2026-12-27"],
   filas=[("D4L","LENT2","ME_E","KEB"), ("D1","SOLPIQ","ME_E","CREMCAL"), ("D2","POTG","ME_D","FAJ"), ("D3","TERI","ME_E",LIBRE),
          ("D4",LIBRE,"ME_E",LIBRE), ("D4S","SALM1","ME_D",FUERA), ("D2","SEPIA","ME_D","CREMVER")]),
]
def total_dia(fila):
    k = p = 0
    for clave in fila:
        if clave not in NO_PLATO:
            kc, pr, _, _ = macros_receta(R[clave]); k += kc; p += pr
    return k, p
PESCADOS = {"merluza": "merluza", "bacalao": "bacalao", "gambas": "gambas", "gambones": "gambas", "calamar": "calamar",
            "sepia": "sepia", "pulpo": "pulpo", "dorada": "dorada", "rape": "rape", "rodaballo": "rodaballo", "salmon": "salmón", "lubina": "lubina", "dorada_sal": "dorada", "atun": "atún", "atun_fresco": "atún"}
PLATOS = ("comida", "cena")
def pescados_semana(s):
    out = set()
    for fila in s["filas"]:
        for clave in fila:
            if clave not in NO_PLATO:
                out |= {PESCADOS[c] for _, ings in R[clave]["grupos"] for c, _q, _t in ings if c in PESCADOS}
    return out
def comprobar_pescados():
    """Errores de la norma: merluza y bacalao nunca en la misma semana, y entre una y otra, al menos una semana sin ninguna de las dos; ningún pescado ni marisco dos semanas seguidas."""
    errores, previa = [], None
    for s in SEMANAS:
        p = pescados_semana(s)
        if {"merluza", "bacalao"} <= p: errores.append(f"Semana {s['num']}: merluza y bacalao en la misma semana")
        if previa is not None and p & previa: errores.append(f"Semanas {s['num'] - 1} y {s['num']}: {', '.join(sorted(p & previa))} dos semanas seguidas")
        mb = {"merluza", "bacalao"}
        if previa is not None and p & mb and previa & mb and not (p & previa & mb):
            errores.append(f"Semanas {s['num'] - 1} y {s['num']}: merluza y bacalao sin una semana de por medio")
        previa = p
    return errores
def platos_semana(s):
    """Comidas y cenas de una semana (sin desayunos ni meriendas, que se repiten a propósito)."""
    return {c for fila in s["filas"] for c in fila if c not in NO_PLATO and R[c]["tipo"] in PLATOS}
def comprobar_repeticiones(desde=6):
    """Desde la semana `desde`: ninguna comida ni cena se repite de una semana a la siguiente, y en el mes nuevo (7 a 10)
       el pescado ya lo vigila comprobar_pescados (nunca el mismo dos semanas seguidas)."""
    errores = []
    for a, b in zip(SEMANAS, SEMANAS[1:]):
        if a["num"] < desde: continue
        rep = platos_semana(a) & platos_semana(b)
        if rep: errores.append(f"Semanas {a['num']} y {b['num']}: se repite {', '.join(R[c]['nombre'] for c in sorted(rep))}")
    # Desde la semana 8: cenas ligeras (cremas, sándwiches, tortilla...). Kebab, fajitas, tacos, pizza o hamburguesa,
    # el día que la comida es de legumbre; si no, como mucho una vez a la semana. Nada de pescado de cena (23 de noviembre)
    for s in SEMANAS:
        if s["num"] < 8: continue
        sueltas = 0
        for i, f in enumerate(s["filas"]):
            comida, cena = f[1], f[3]
            if cena in NO_PLATO: continue
            if cena not in CENAS_LIGERAS | CENAS_RAPIDAS:
                errores.append(f"Semana {s['num']}, {DIAS[i].lower()}: {R[cena]['nombre']} no es una cena ligera")
            elif cena in CENAS_RAPIDAS and comida not in LEGUMBRES:
                sueltas += 1
        if sueltas > 1: errores.append(f"Semana {s['num']}: {sueltas} cenas tipo kebab o hamburguesa sin legumbre a mediodía (como mucho, una)")
    # Desde la semana 7: ningún plato se repite dentro de la misma semana (las lentejas, un solo día; 22 de noviembre)
    for s in SEMANAS:
        if s["num"] >= 7:
            vistos = [c for f in s["filas"] for c in (f[1], f[3]) if c not in NO_PLATO]
            rep = sorted({c for c in vistos if vistos.count(c) > 1})
            if rep: errores.append(f"Semana {s['num']}: se repite dentro de la semana: {', '.join(R[c]['nombre'] for c in rep)}")
    # Desde la semana 7: los guisantes con jamón no son plato principal (fuera del plan, 21 de noviembre)
    for s in SEMANAS:
        if s["num"] >= 7 and {"GUIS", "GUIS_D", "GUIS_T"} & platos_semana(s):
            errores.append(f"Semana {s['num']}: guisantes con jamón (no es plato principal)")
    # Desde la semana 7: nada de pavo, ni en comidas ni en cenas (21 de noviembre)
    for s in SEMANAS:
        if s["num"] >= 7:
            con = [R[c]["nombre"] for f in s["filas"] for c in f if c not in NO_PLATO
                   and any(i in ("pavo", "pavo_fiambre") for _, ings in R[c]["grupos"] for i, _q, _t in ings)]
            if con: errores.append(f"Semana {s['num']}: lleva pavo: {', '.join(sorted(set(con)))}")
    # Cada mes (bloques de 4 semanas desde la 7): arroz con secreto en la Le Creuset, dorada y lubina a la sal y salmón 2 semanas
    for ini in range(8, max(s["num"] for s in SEMANAS) + 1, 4):
        mes = [s for s in SEMANAS if ini <= s["num"] < ini + 4]
        if len(mes) < 4: continue
        platos = set().union(*(platos_semana(s) for s in mes))
        for k in MENSUALES:
            if k not in platos: errores.append(f"Semanas {ini}–{ini + 3}: falta {R[k]['nombre']} (una vez al mes)")
        n_salmon = sum("salmón" in pescados_semana(s) for s in mes)
        if n_salmon < 2: errores.append(f"Semanas {ini}–{ini + 3}: salmón solo {n_salmon} semana(s); tienen que ser 2")
    return errores
MENSUALES = ["ARRSEC", "DORSAL", "LUBSAL"]
CENAS_LIGERAS = {"CREMCAL", "CREMZAN", "CREMVER", "SOPA", "CASTA", "CENAV", "TOR", "TOM", "SANDTOR", "SANDMIX", "SANDPOL"}
CENAS_RAPIDAS = {"KEB", "FAJ", "TAC", "CRI", "FIN", "FF2", "BEX", "FPZ", "PZA"}
LEGUMBRES = {"LENT1", "LENT2", "LENTJ", "POTG"}
if __name__ == "__main__":
    for s in SEMANAS: print(f"Semana {s['num']}: {', '.join(sorted(pescados_semana(s))) or '—'}")
    from batch import comprobar_fuegos
    for e in comprobar_pescados() + comprobar_repeticiones() + comprobar_fuegos(): print("  NORMA:", e)
    for s in SEMANAS:
        print(f"\nSemana {s['num']} ({s['titulo']})")
        for i, fila in enumerate(s["filas"]):
            k, p = total_dia(fila)
            obj = 1950 if TIPO[i] == "E" else 1600
            nota = "  + cena fuera" if fila[3] == FUERA else ("  + comida y cena libres" if fila[1] == LIBRE else "  + cena libre") if fila[3] == LIBRE else f"  ({k-obj:+.0f} vs {obj})"
            print(f"  {DIAS[i]:10s} {TIPO[i]}  {k:5.0f} kcal  {p:5.0f} g prot  {' / '.join(fila)}{nota}")

CAMBIOS = {
 "LENT1": "Solomillos en vez de contramuslo, mucho menos aceite y sin chorizo; pimiento rojo en vez de calabacín; la patata es el extra para días de entreno.",
 "LENT2": "Huevo cocido añadido para la proteína (la original es vegana) y 80 g de lentejas en vez de 150; el arroz es el extra para días de entreno.",
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
 "FCE": "Jamón cocido en vez de pavo; yogur +Proteínas en vez de cottage, un huevo cambiado por claras y sin calabacín (más pimiento).",
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
 "CREMCAL": "AOVE en vez de mantequilla (45 en tu test); pipas de calabaza por encima y una tortilla de claras con jamón cocido de segundo para llegar a la proteína. La web no dice raciones: cantidades calculadas para 4 y pasadas a 2.",
 "CREMZAN": "Leche normal en vez de evaporada; caldo bajo en sal; calamar a la plancha por encima para llegar a la proteína (en vez de gambas, que ya hay el domingo anterior). La web no dice raciones: cantidades calculadas para 4 y pasadas a 2.",
 "ARRGAMB": "Gambones enteros en vez de colas peladas, para hacer el fumet con sus cabezas (lo que propone la receta si no tienes caldo); 70 g de arroz por persona en vez de 100 y el aceite medido.",
 "GCAL": "Sin vermut (alcohol 51 en tu test): un poco más de agua; carne de choricero de bote en vez de choriceros y ñoras en remojo (valen si los tienes); 2 ajos frescos por persona en vez de 3 (ajo 43) y el aceite medido; algo más de calamar y de patata para que sea un plato completo. La receta es para 4: cantidades pasadas a 2.",
 "PULPO": "Con pulpo ya cocido (envasado) en vez de cocer uno entero: 25 minutos en total; el aceite, medido. La receta es para 4: cantidades pasadas a 2.",
 "SEPIA": "Sin vino; tomate triturado natural en vez de salsa de tomate; la mitad de aceite y de ajo. La receta es para 4: cantidades pasadas a 2.",
 "DORADA": "Agua o caldo de pescado en vez del vino blanco; una dorada de ración por persona y más patata (la receta pone 500 g de dorada para los dos); la mitad de aceite y de ajo.",
 "RAPE": "Rape limpio congelado y caldo de pescado de brik (la receta hace el caldo con la cabeza y la espina); el aceite, medido, y la mitad de ajo. La receta es para 4: cantidades pasadas a 2.",
 "LUBSAL": "Pisto sin calabacín (te sienta mal): con cebolla, pimientos y tomate, y el aceite medido; patata cocida para que sea un plato completo; una lubina de ración por persona. La receta es para 4: cantidades pasadas a 2.",
 "DORSAL": "Doradas de ración (una por persona) en vez de una pieza de 2 kg, a 190 °C como recomienda la receta para piezas pequeñas; sin mayonesa ni alioli: patata cocida con AOVE y una ensalada de tomate para que sea un plato completo.",
 "SALM1": "Medio diente de ajo por persona en vez de uno y medio (ajo 43 en tu test) y el aceite medido. Salmón: 45 en tu test, lo comes con moderación (decisión tuya del 15 de noviembre). La receta es para 4: cantidades pasadas a 2.",
 "SALM2": "Zanahoria en tiras en vez de calabacín y medio diente de ajo; el salmón, pesado (150 g por persona; la receta no lo dice). Salmón: 45 en tu test, con moderación. La receta es para 1: cantidades pasadas a 2.",
 "CASTA": "Boniato en vez de castañas (se encuentra todo el año en Mercadona y da la misma crema dulce y espesa, con menos kcal); menos agua (2 L para dos no caben en el vaso del robot); un huevo pochado por persona en vez de uno para los dos. El boniato no sale en tu test.",
 "TERI": "Sin mirin ni sake (alcohol 51 en tu test): agua y un chorrito de limón; miel medida (una cucharadita por persona) en vez de azúcar; soja baja en sal; solomillos en vez de pechuga o muslo; con judías verdes, zanahoria y pimiento salteados para que sea un plato completo de táper, y el arroz medido.",
 "ESTOF": "Sin vino tinto (alcohol 51 en tu test): una cucharadita de balsámico; 340 g de carne para los dos en vez de 650 y algo menos de patata, para que cuadre con las kcal del día; un diente de ajo en vez de tres (ajo 43); el aceite, medido.",
 "SOLPIQ": "La salsa, solo con cebolla, piquillos y caldo (sin nata ni vino); el aceite, medido; con patata y pan para que sea un plato completo de táper.",
 "CARNEG": "Sin vino (alcohol 51 en tu test): caldo de carne; el aceite, medido; ternera de guisar magra. Cantidades para 2.",
 "CREMVER": "Judías verdes y zanahoria en vez del calabacín (te sienta mal); caldo de verduras; jamón crujiente como en la receta y huevos cocidos de segundo para que sea una cena completa. La receta es para 4: cantidades pasadas a 2.",
 "RODA": "Sin vino blanco (alcohol 51 en tu test): caldo de pescado; el aceite, medido (la receta pone un buen chorro); un solo diente de ajo para los dos (ajo 43). Rodaballo: verde en tu test.",
 "ARRSEC": "Secreto ibérico en vez de carrilleras (en tiras y dorado al principio, así no necesita 1 hora); sin Pedro Ximénez ni vino tinto (alcohol 51 en tu test): caldo y un poco de balsámico; 70 g de arroz por persona en vez de 90 y el aceite medido; la mitad de ajos tiernos (ajo 43).",
 "SOPA": "Pasada a vuestra Mambo (la original se hace en una olla); un huevo pochado por persona en vez de uno para los dos; la pechuga, pesada (unos 180 g por persona) y las especias, concretadas.",
 "RISOT": "Con pollo; sin mantequilla (45) ni parmesano (queso curado 55): un poco de mozzarella fresca al final; sin vino; más puerro y setas (no champiñón, 43 en tu test); menos jamón y caldo bajo en sal.",
}
from batch import BATCH, NORMAS
NOTA_COMPRA = {
 11: "Semana de Navidad: la cena del jueves 24 (Nochebuena) y la comida y la cena del viernes 25 quedan libres, sin compra. El salmón de la comida del sábado 26, compradlo el jueves 24 (el 25 cierran las tiendas), o congelado y a la nevera la noche antes. La sepia del domingo 27, congelada.",
 3: "La compra de esta semana ya está hecha (sábado 24). Con los cambios solo falta: 140 g de jamón cocido extra para la pizza del martes, un pimiento rojo para el pil pil y la fajicesta y una guindilla o cayena si no tenéis. Os sobran 2 latas de atún y 400 g de garbanzos (los garbanzos, para el potaje del miércoles 4).",
 4: "No compréis los garbanzos: os sobran de la semana pasada (ya no los lleva el bacalao).",
 5: "La compra de esta semana ya está hecha. El domingo 15 ya no hay tacos de merluza, sino arroz meloso con gambones: el sábado 14, con la compra de la semana 6, añadid 500 g de gambones crudos congelados (unos 12), 140 g de arroz bomba (o redondo, si os queda), 60 g más de pimiento rojo y 30 g de verde, media cebolla, un trozo de puerro (40 g), 120 g de tomate triturado y azafrán si no tenéis. Si ya comprasteis la merluza (340 g), dejadla en el congelador para el fish & chips del sábado 21; las tortillas de maíz, la piña y la lima os sobran.",
 7: "Si ya habéis hecho la compra con la lista anterior: os sobran los guisantes, el jamón, el secreto (al congelador, para el arroz del sábado 19 de diciembre), el pavo, el salmón (congelado, para el miércoles 2), la carne picada de las albóndigas y la mitad de las lentejas. Lo nuevo está en la lista: ternera para guisar, judías verdes, arroz basmati, miel, jengibre, copos de maíz y yogures +Proteínas. El pulpo cocido, compradlo ya (es para el martes 24: mirad la fecha). El rodaballo (1 de 1–1,2 kg), mejor fresco: el viernes 27 o el mismo sábado 28.",
 8: "Las 2 doradas de la comida del sábado 5 se hacen a la sal: enteras y sin escamar. Mejor frescas, compradas el viernes 4 o el mismo sábado; si no, congeladas enteras, y a la nevera la noche antes.",
 9: "Las 2 lubinas de la comida del domingo 13 se hacen a la sal: enteras y sin escamar. Mejor frescas: no las compréis hoy, sino el sábado 12 con la compra de la semana siguiente. El salmón de la comida del sábado 12, fresco el viernes 11 (o congelado y a la nevera la noche antes).",
 10: "El secreto ibérico del arroz del sábado 19 va al congelador en el batch del domingo 13.",
 6: "Si comprasteis la merluza de los tacos de la semana pasada (340 g), no compréis más: os vale para el fish & chips del sábado 21.",
}
PREP = {n: b['recordatorios'] for n, b in BATCH.items()}
