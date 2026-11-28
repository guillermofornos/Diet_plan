from recetas_base import R as R0
from recetas_lentejas import R as R1
from recetas_lara_comidas import R as R2
from recetas_lara_cenas import R as R3
from recetas_pescado import R as R4
from recetas_cecotec import R as R5
from recetas_ciclo import R as R6
from datetime import date, timedelta
from lib import macros_receta
R = {**R0, **R1, **R2, **R3, **R4, **R5, **R6}
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
   filas=[("D1","SOLPIQ","ME_E","FAJ"), ("D4","ALBON","ME_E","SOPA"), ("D2","BBQ","ME_D","ENSHUEVO"), ("D1","POTG","ME_E","KEB"),
          ("D4","ARRPOL","ME_E",FUERA), ("D4S","DORSAL","ME_D",FUERA), ("D2","ARRGAMB","ME_D","CASTA")]),
]
def total_dia(fila):
    k = p = 0
    for clave in fila:
        if clave not in NO_PLATO:
            kc, pr, _, _ = macros_receta(R[clave]); k += kc; p += pr
    return k, p
# ---------------------------------------------------------------------------------------------------------------------
# CICLO DE 5 SEMANAS (28 de noviembre): desde la semana 9 (lunes 7 de diciembre) el menú son estas 5 semanas, que se
# repiten. Las normas de no repetir valen también de la semana 5 a la 1 (comprobar_ciclo). Para generar más semanas,
# sube ULTIMA_SEMANA: la 14 vuelve a ser la 1 del ciclo.
CICLO_SEMANA, CICLO_LUNES = 9, date(2026, 12, 7)
ULTIMA_SEMANA = 13
# 5 semanas de 7 filas (desayuno, comida, merienda, cena), de lunes a domingo
CICLO = [
 [("D4", "LENTJ", "ME_E", "TAC"), ("D1", "BOLO", "ME_E", "FIN"), ("D2", "ESTOF", "ME_D", "CREMCAL"), ("D1", "ARR3D", "ME_E", "ENSHUEVO"),
  ("D4", "CERSAL", "ME_E", FUERA), ("D4S", "SALM2", "ME_D", FUERA), ("D4S", "LUBSAL", "ME_D", "CREMVER")],
 [("D1", "SOLPIQ", "ME_E", "ENSHUEVO"), ("D1", "PULPO", "ME_E", "PZA"), ("D4S", "POTG", "ME_D", "KEB"), ("D1", "ALBON", "ME_E", "TOR"),
  ("D4", "ARRPOL", "ME_E", FUERA), ("D4S", "ARRSEC", "ME_D", FUERA), ("D2", "RAPE", "ME_D", "CREMZAN2")],
 [("D1", "LENTJ", "ME_E", "FAJ"), ("D4", "PASTAF", "ME_E", "FF2"), ("D4S", "TERESC", "ME_D", "SOPA"), ("D1", "ARR3D", "ME_E", "CREMCAL"),
  ("D4", "PASTEL", "ME_E", FUERA), ("D4S", "SALM1", "ME_D", FUERA), ("D2", "SEPIA", "ME_D", "ENSHUEVO")],
 [("D1", "RISOT", "ME_E", "CREMVER"), ("D1", "PULPO", "ME_E", "CRI"), ("D4S", "ESTOF", "ME_D", "ENSHUEVO"), ("D1", "BOLO", "ME_E", "SANDTOR"),
  ("D4", "CERSAL", "ME_E", FUERA), ("D4S", "DORSAL", "ME_D", FUERA), ("D2", "GCAL", "ME_D", "CREMZAN2")],
 [("D1", "PASTAF", "ME_E", "SOPAV"), ("D1", "SOLPIQ", "ME_E", "ENSHUEVO"), ("D2", "MISO", "ME_D", "CENAC"), ("D1", "ALBON", "ME_E", "SANDMIX"),
  ("D4", "POTG", "ME_E", FUERA), ("D4S", "FISHCHIPS", "ME_D", FUERA), ("D2", "ARRGAMB", "ME_D", "CASTA")],
]
# Festivos: comida o cena que quedan libres, aviso para ese día y si cierran las tiendas (las compras pasan a la víspera)
FESTIVOS = {
 date(2026, 12, 24): dict(cena=LIBRE, aviso="Nochebuena: cena libre."),
 date(2026, 12, 25): dict(comida=LIBRE, cena=LIBRE, aviso="Navidad: comida y cena libres.", cerrado=True),
 date(2026, 12, 31): dict(cena=LIBRE, aviso="Nochevieja: cena libre."),
 date(2027, 1, 1): dict(comida=LIBRE, cena=LIBRE, aviso="Año Nuevo: comida y cena libres.", cerrado=True),
}
MES_CORTO = ["", "ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
# Norma del 28 de noviembre: cuando a un día le falta proteína, la merienda por defecto es un batido de proteínas. Cuenta
# como «falta» no llegar a UMBRAL_PROTEINA g por persona (lo que pone cada día del menú, a partes iguales): con eso,
# Guillermo llega a sus ≈170 g con sus cazos de siempre. Los días con la cena fuera o libre no se miran.
UMBRAL_PROTEINA = 120
MERIENDA_BATIDO = {"ME_E": "ME_BE", "ME_D": "ME_BD"}
def con_batido(fila):
    d, c, m, ce = fila
    if c in NO_PLATO or ce in NO_PLATO or m not in MERIENDA_BATIDO: return fila
    return (d, c, MERIENDA_BATIDO[m], ce) if total_dia(fila)[1] < UMBRAL_PROTEINA else fila
# Y cuando falta una receta de cena, la cena por defecto es la avena con leche y cacao (CENAC).
CENA_POR_DEFECTO = "CENAC"
def semana_ciclo(num):
    """La semana `num` del calendario, sacada del ciclo: con sus fechas y con los festivos ya libres."""
    k = (num - CICLO_SEMANA) % len(CICLO); lunes = CICLO_LUNES + timedelta(weeks=num - CICLO_SEMANA); dom = lunes + timedelta(days=6)
    titulo = f"{lunes.day} – {dom.day} {MES_CORTO[dom.month]}" if lunes.month == dom.month else f"{lunes.day} {MES_CORTO[lunes.month]} – {dom.day} {MES_CORTO[dom.month]}"
    filas = []
    for i, (d, c, m, ce) in enumerate(CICLO[k]):
        f = FESTIVOS.get(lunes + timedelta(days=i), {})
        filas.append(con_batido((d, f.get("comida", c), m, f.get("cena", ce))))
    return dict(num=num, ciclo=k + 1, titulo=titulo, fechas=[(lunes + timedelta(days=i)).isoformat() for i in range(7)], filas=filas)
def montar_ciclo():
    """Quita de SEMANAS las semanas del ciclo y las vuelve a generar (se llama al final del módulo, con CICLO ya escrito)."""
    SEMANAS[:] = [s for s in SEMANAS if s["num"] < CICLO_SEMANA] + ([semana_ciclo(n) for n in range(CICLO_SEMANA, ULTIMA_SEMANA + 1)] if CICLO else [])
montar_ciclo()
PESCADOS = {"merluza": "merluza", "bacalao": "bacalao", "gambas": "gambas", "gambas_coc": "gambas", "gambones": "gambas", "calamar": "calamar",
            "sepia": "sepia", "pulpo": "pulpo", "dorada": "dorada", "rape": "rape", "rodaballo": "rodaballo", "salmon": "salmón", "lubina": "lubina", "dorada_sal": "dorada", "atun": "atún", "atun_fresco": "atún"}
PLATOS = ("comida", "cena")
# Cenas fijas, una por semana (la ensalada de huevo y gambas, pedida el 25 de noviembre): no cuentan en la norma
# de no repetir ni en la rotación de pescado
SEMANALES = {"ENSHUEVO"}
def pescados_semana(s, sin=()):
    out = set()
    for fila in s["filas"]:
        for clave in fila:
            if clave not in NO_PLATO and clave not in sin:
                out |= {PESCADOS[c] for _, ings in R[clave]["grupos"] for c, _q, _t in ings if c in PESCADOS}
    return out
def comprobar_pescados():
    """Errores de la norma: merluza y bacalao nunca en la misma semana, y entre una y otra, al menos una semana sin ninguna de las dos; ningún pescado ni marisco dos semanas seguidas."""
    errores, previa = [], None
    for s in SEMANAS:
        p = pescados_semana(s, SEMANALES)
        if {"merluza", "bacalao"} <= p: errores.append(f"Semana {s['num']}: merluza y bacalao en la misma semana")
        if previa is not None and p & previa: errores.append(f"Semanas {s['num'] - 1} y {s['num']}: {', '.join(sorted(p & previa))} dos semanas seguidas")
        mb = {"merluza", "bacalao"}
        if previa is not None and p & mb and previa & mb and not (p & previa & mb):
            errores.append(f"Semanas {s['num'] - 1} y {s['num']}: merluza y bacalao sin una semana de por medio")
        previa = p
    return errores
# Familias: platos distintos que cuentan como el mismo para no repetir (norma del 28 de noviembre, cuando salieron
# lentejas tres semanas seguidas con recetas distintas): entre dos de la misma familia, una semana de por medio, y nunca
# dos en la misma semana. Si te parece que dos platos son el mismo, se añaden aquí.
FAMILIAS = {
 "lentejas": {"LENT1", "LENT2", "LENTJ"},
 "garbanzos": {"POTG", "GARBAC"},
 "guiso de ternera": {"ESTOF", "CARNEG", "JARD"},
 "crema de zanahoria": {"CREMZAN", "CREMZAN2"},
 "sopa de pollo": {"SOPA", "SOPAV"},
 "avena con leche": {"CENAV", "CENAC"},
 "pasta boloñesa": {"TOFU", "TOFU_D", "BOLO"},
 "guisantes con jamón": {"GUIS", "GUIS_D", "GUIS_T"},
 "bacalao a la vizcaína": {"VIZCA", "VIZCA_A"},
}
def familia(c):
    return next((f for f, cs in FAMILIAS.items() if c in cs), c)
def nombre_familia(f):
    return f if f in FAMILIAS else R[f]["nombre"]
def platos_semana(s):
    """Comidas y cenas de una semana (sin desayunos ni meriendas, que se repiten a propósito)."""
    return {c for fila in s["filas"] for c in fila if c not in NO_PLATO and R[c]["tipo"] in PLATOS}
def comprobar_repeticiones(desde=6):
    """Desde la semana `desde`: ninguna comida ni cena se repite de una semana a la siguiente; desde la 7 a la 8, tampoco
       otro plato de la misma familia (FAMILIAS: lentejas, garbanzos, guiso de ternera...), con una semana de por medio.
       El pescado lo vigila comprobar_pescados (nunca el mismo dos semanas seguidas)."""
    errores = []
    for a, b in zip(SEMANAS, SEMANAS[1:]):
        if a["num"] < desde: continue
        clave = familia if a["num"] >= 7 else (lambda c: c)
        rep = {clave(c) for c in platos_semana(a) - SEMANALES} & {clave(c) for c in platos_semana(b) - SEMANALES}
        if rep: errores.append(f"Semanas {a['num']} y {b['num']}: se repite {', '.join(nombre_familia(f) for f in sorted(rep))}"
                               " (entre los dos, una semana de por medio)")
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
    # Desde la semana 7: ningún plato, ni otro de su familia, se repite dentro de la misma semana (las lentejas, un solo
    # día; 22 de noviembre)
    for s in SEMANAS:
        if s["num"] >= 7:
            vistos = [familia(c) for f in s["filas"] for c in (f[1], f[3]) if c not in NO_PLATO]
            rep = sorted({c for c in vistos if vistos.count(c) > 1})
            if rep: errores.append(f"Semana {s['num']}: se repite dentro de la semana: {', '.join(nombre_familia(c) for c in rep)}")
    # Desde la semana 8: cada cena fija semanal, una vez a la semana (si un festivo deja libre esa cena, ninguna)
    for s in SEMANAS:
        if s["num"] >= 8:
            for k in sorted(SEMANALES):
                n = sum(f[3] == k for f in s["filas"])
                festivo = "ciclo" in s and any(f[3] == k for f in CICLO[s["ciclo"] - 1])
                if n != 1 and not (n == 0 and festivo): errores.append(f"Semana {s['num']}: {R[k]['nombre']} va una vez a la semana de cena (va {n})")
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
    # Lo de «una vez al mes» (arroz con secreto, dorada y lubina a la sal, 2 semanas de salmón) va ahora por vuelta del ciclo: comprobar_ciclo
    return errores
MENSUALES = ["ARRSEC", "DORSAL", "LUBSAL"]
CENAS_LIGERAS = {"CREMCAL", "CREMZAN", "CREMZAN2", "CREMVER", "SOPA", "SOPAV", "CASTA", "CENAV", "CENAC", "TOR", "TOM", "SANDTOR", "SANDMIX", "SANDPOL", "ENSHUEVO"}
CENAS_RAPIDAS = {"KEB", "FAJ", "TAC", "CRI", "FIN", "FF2", "BEX", "FPZ", "PZA"}
LEGUMBRES = {"LENT1", "LENT2", "LENTJ", "POTG"}
# Recetas que ha pasado Guillermo (enlaces, fotos del libro, capturas o texto). Norma del 25 de noviembre: tienen prioridad
# sobre las demás; para hacer sitio a un plato o resolver un choque de normas, sale una que no esté aquí. Cada receta
# nueva suya se añade a esta lista.
PROPIAS = {"CRI", "FF2", "TAC", "FAJ", "FIN", "KEB",                        # vídeos, 6 de octubre
           "LENTJ", "ARRPOL", "TERESC", "RISOT", "JARD", "POTG", "ALBON",   # fotos del libro del robot, 25 de octubre
           "CREMCAL", "CREMZAN", "CREMZAN2",                                # enlaces de Cecotec, 26 de octubre
           "SOPA", "CASTA", "ARRSEC", "ESTOF", "ENSHUEVO",                  # 15 a 25 de noviembre
           "SOPAV", "CENAC", "MISO"}                                        # 28 de noviembre: sopa casera, su cena por defecto y la ternera al miso
# Platos con frecuencia fija en cada vuelta del ciclo: el estofado, «cada dos semanas» (22 de noviembre), y la pasta
# boloñesa con carne picada, «al menos cada par de semanas» (28 de noviembre). Con 5 semanas, dos veces: cada 2 o 3 semanas.
FRECUENCIA_CICLO = {"ESTOF": 2, "BOLO": 2}
# Recetas suyas que no entran en el ciclo, con el motivo (comprobar_ciclo avisa si falta alguna que no esté aquí)
PROPIAS_FUERA = {
 "JARD": "es el mismo guiso que su estofado, que es el que pidió como habitual (22 de noviembre)",
 "CREMZAN": "llevaba calamar y el pescado no va de cena: entra como CREMZAN2, con tosta de jamón y mozzarella",
}
POLLO = {"pechuga", "solomillo"}
def lleva_pollo(c):
    return c not in NO_PLATO and any(i in POLLO for _, ings in R[c]["grupos"] for i, _q, _t in ings)
def comprobar_pollo(desde=CICLO_SEMANA):
    """Desde el ciclo (28 de noviembre): como mucho 2 platos con pollo a la semana, contando comidas y cenas y cualquier plato
       que lo lleve (también sopas, cremas y arroces). Y nunca pollo en la comida y en la cena del mismo día."""
    errores = []
    for s in SEMANAS:
        if s["num"] < desde: continue
        con = [R[c]["nombre"] for f in s["filas"] for c in (f[1], f[3]) if lleva_pollo(c)]
        if len(con) > 2: errores.append(f"Semana {s['num']}: {len(con)} platos con pollo (como mucho, 2): {', '.join(con)}")
        for i, f in enumerate(s["filas"]):
            if lleva_pollo(f[1]) and lleva_pollo(f[3]): errores.append(f"Semana {s['num']}, {DIAS[i].lower()}: pollo en la comida y en la cena")
    return errores
def comprobar_ciclo():
    """La vuelta del ciclo: de la semana 5 a la 1 no se repite ningún plato (ni otro de su familia) ni ningún pescado, y
       merluza y bacalao guardan su semana de por medio. En cada vuelta entran el arroz con secreto, la dorada y la lubina a
       la sal y 2 semanas de salmón, la cena fija de cada semana y todas las recetas de Guillermo menos las de PROPIAS_FUERA."""
    errores = []
    if not CICLO: return errores
    sem = [dict(num=i + 1, filas=f) for i, f in enumerate(CICLO)]
    for i, a in enumerate(sem):
        b = sem[(i + 1) % len(sem)]
        rep = {familia(c) for c in platos_semana(a) - SEMANALES} & {familia(c) for c in platos_semana(b) - SEMANALES}
        if rep: errores.append(f"Ciclo, semanas {a['num']} y {b['num']}: se repite {', '.join(nombre_familia(f) for f in sorted(rep))}")
        pa, pb = pescados_semana(a, SEMANALES), pescados_semana(b, SEMANALES)
        if pa & pb: errores.append(f"Ciclo, semanas {a['num']} y {b['num']}: {', '.join(sorted(pa & pb))} dos semanas seguidas")
        mb = {"merluza", "bacalao"}
        if pa & mb and pb & mb and not (pa & pb & mb): errores.append(f"Ciclo, semanas {a['num']} y {b['num']}: merluza y bacalao sin una semana de por medio")
        for k in sorted(SEMANALES):
            n = sum(f[3] == k for f in a["filas"])
            if n != 1: errores.append(f"Ciclo, semana {a['num']}: {R[k]['nombre']} va una vez a la semana de cena (va {n})")
        con = [c for f in a["filas"] for c in (f[1], f[3]) if lleva_pollo(c)]
        if len(con) > 2: errores.append(f"Ciclo, semana {a['num']}: {len(con)} platos con pollo")
    platos = set().union(*(platos_semana(s) for s in sem))
    for k in MENSUALES:
        if k not in platos: errores.append(f"Ciclo: falta {R[k]['nombre']} (una vez en cada vuelta)")
    for k, n in FRECUENCIA_CICLO.items():
        hay = sum(f[1] == k or f[3] == k for s in sem for f in s["filas"])
        if hay != n: errores.append(f"Ciclo: {R[k]['nombre']} va {hay} veces en cada vuelta (tienen que ser {n})")
    for s in sem:
        if {"ESTOF", "MISO"} <= platos_semana(s): errores.append(f"Ciclo, semana {s['num']}: estofado y ternera al miso la misma semana (los dos van en la Le Creuset)")
    ns = sum("salmón" in pescados_semana(s) for s in sem)
    if ns != 2: errores.append(f"Ciclo: salmón en {ns} semana(s); tienen que ser 2")
    for k in sorted(PROPIAS - platos - set(PROPIAS_FUERA)):
        errores.append(f"Ciclo: falta {R[k]['nombre']}, que es receta de Guillermo (o apúntala en PROPIAS_FUERA con el motivo)")
    return errores
def comprobar_todo():
    from batch import comprobar_fuegos
    return comprobar_pescados() + comprobar_repeticiones() + comprobar_pollo() + comprobar_ciclo() + comprobar_fuegos(BATCH)
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
 "CREMZAN2": "Leche normal en vez de evaporada; caldo bajo en sal; tosta de jamón y mozzarella y un yogur +Proteínas para llegar a la proteína (antes llevaba calamar a la plancha, pero el pescado no va de cena). La web no dice raciones: cantidades calculadas para 4 y pasadas a 2.",
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
 "ENSHUEVO": "Apio en vez de pepino (45 en tu test), yogur +Proteínas en vez de griego ligero y 40 g de pan integral tostado para que la cena no se quede corta. Cantidades de la receta, por persona. La receta dice 390 kcal y 46 g de proteína por ración; con el pan, ≈473 kcal y 49 g.",
 "SOPA": "Pasada a vuestra Mambo (la original se hace en una olla); un huevo pochado por persona en vez de uno para los dos; la pechuga, pesada (unos 180 g por persona) y las especias, concretadas.",
 "SOPAV": "La receta es para 4 raciones de primero: como cena única, la receta entera para los dos (150 g de pollo por persona). 1 cucharada de aceite para los dos en vez de 3 y 1 diente de ajo en vez de 2 (ajo 43 en tu test). Pasada a vuestra Mambo (también vale en la olla, como la original); el pan, como dice la receta.",
 "MISO": "En la Le Creuset a fuego mínimo (no tenéis olla lenta), 2 h 30 a 3 horas; medio diente de ajo por persona en vez de uno y pico (ajo 43 en tu test); soja baja en sal; 170 g de carne por persona; con judías verdes para que sea un plato completo de táper. La receta, en inglés, no dice raciones: cantidades calculadas para 2.",
 "BOLO": "Sin vino tinto (alcohol 51 en tu test): caldo de carne; sin panceta y con algo más de ternera magra (150 g por persona); mozzarella en vez del parmesano (queso curado 55); sin apio; 80 g de pasta por persona en vez de 100 y el aceite medido. La receta es para 4: cantidades pasadas a 2.",
 "RISOT": "Con pollo; sin mantequilla (45) ni parmesano (queso curado 55): un poco de mozzarella fresca al final; sin vino; más puerro y setas (no champiñón, 43 en tu test); menos jamón y caldo bajo en sal.",
 "CERSAL": "Magro sin grasa en vez de cabeza de lomo, y 170 g por persona (la receta pone 1 kg para 3 o 4); caldo en vez del vino blanco, como ofrece la propia receta (alcohol 51 en tu test); medio diente de ajo por persona en vez de uno; el aceite, medido; con patata y pan para que sea un plato completo de táper.",
 "ARR3D": "Cantidades pesadas (el vídeo no las da): 60 g de arroz y 150 g de tofu por persona; con zanahoria, como el tres delicias del segundo vídeo; sin gambas.",
 "PASTEL": "Carne picada magra, 150 g por persona; mozzarella light en vez de queso rallado y tomate triturado natural en vez de frito; medio huevo en el puré, como hace Arguiñano en el suyo de patata, para que aguante el táper y el congelador; sin vino.",
 "PASTAF": "Con huevo duro (la original no lleva) y mahonesa proteica de huevo cocido y yogur en vez de la de huevo crudo, que no aguanta 3 días en el táper; 80 g de jamón por persona y algo menos de pasta; carne de choricero de bote en vez de cocer los pimientos.",
}
from batch import BATCH as _BATCH_FIJOS, CICLO_BATCH, NORMAS, instanciar
def _batch_ciclo(s):
    """El batch de una semana del ciclo: la plantilla de su semana, con fechas, sin lo que un festivo deja libre."""
    ant = SEMANAS[SEMANAS.index(s) - 1]; lunes = date.fromisoformat(s["fechas"][0])
    presentes = {c for f in s["filas"] for c in (f[1], f[3])} | {ant["filas"][6][1], ant["filas"][6][3]}
    dias = [lunes + timedelta(days=i) for i in range(-1, 7)]
    avisos = [(d, FESTIVOS[d]["aviso"]) for d in dias if d in FESTIVOS]
    return instanciar(CICLO_BATCH[s["ciclo"]], lunes, presentes, avisos, {d for d in dias if FESTIVOS.get(d, {}).get("cerrado")})
BATCH = {**{n: b for n, b in _BATCH_FIJOS.items() if n < CICLO_SEMANA}, **{s["num"]: _batch_ciclo(s) for s in SEMANAS if "ciclo" in s}}
# Notas de la compra: las de cada semana del ciclo y, delante, las de las semanas con festivos
NOTA_CICLO = {
 1: "Las 2 lubinas de la comida del domingo se hacen a la sal: enteras y sin escamar. Mejor frescas: no las compréis hoy, sino el sábado que viene, con la compra de la semana siguiente. El salmón de la comida del sábado, fresco el viernes (o congelado, y a la nevera la noche antes).",
 2: "El secreto ibérico del arroz del sábado va al congelador en el batch de mañana. El pulpo del martes viene cocido y envasado: mirad la fecha.",
 3: "La carne picada de la Big Mac del martes va al congelador en el batch de mañana, y la del pastel se cocina ese día. El salmón de la comida del sábado, fresco el viernes (o congelado, y a la nevera la noche antes). La sepia del domingo, congelada.",
 4: "Las 2 doradas de la comida del sábado se hacen a la sal: enteras y sin escamar. Mejor frescas, compradas el viernes o el mismo sábado; si no, congeladas enteras, y a la nevera la noche antes. El pulpo del martes viene cocido y envasado: mirad la fecha. El calamar del domingo, congelado.",
 5: "La merluza del fish & chips del sábado y los gambones del arroz del domingo, congelados. La pechuga de la crema del domingo va al congelador en el batch de mañana.",
}
NOTA_FESTIVOS = {
 11: "Semana de Navidad: la cena del jueves 24 (Nochebuena) y la comida y la cena del viernes 25 quedan libres y no están en la lista. El salmón de la comida del sábado 26, compradlo el jueves 24 (el 25 cierran las tiendas), o congelado y a la nevera la noche antes.",
 12: "Semana de Año Nuevo: la cena del jueves 31 (Nochevieja) y la comida y la cena del viernes 1 quedan libres y no están en la lista. Las doradas de la comida del sábado 2, compradlas el jueves 31 (el 1 cierran las tiendas), o congeladas y a la nevera la noche antes.",
}
NOTA_COMPRA = {
 3: "La compra de esta semana ya está hecha (sábado 24). Con los cambios solo falta: 140 g de jamón cocido extra para la pizza del martes, un pimiento rojo para el pil pil y la fajicesta y una guindilla o cayena si no tenéis. Os sobran 2 latas de atún y 400 g de garbanzos (los garbanzos, para el potaje del miércoles 4).",
 4: "No compréis los garbanzos: os sobran de la semana pasada (ya no los lleva el bacalao).",
 5: "La compra de esta semana ya está hecha. El domingo 15 ya no hay tacos de merluza, sino arroz meloso con gambones: el sábado 14, con la compra de la semana 6, añadid 500 g de gambones crudos congelados (unos 12), 140 g de arroz bomba (o redondo, si os queda), 60 g más de pimiento rojo y 30 g de verde, media cebolla, un trozo de puerro (40 g), 120 g de tomate triturado y azafrán si no tenéis. Si ya comprasteis la merluza (340 g), dejadla en el congelador para el fish & chips del sábado 21; las tortillas de maíz, la piña y la lima os sobran.",
 6: "Si comprasteis la merluza de los tacos de la semana pasada (340 g), no compréis más: os vale para el fish & chips del sábado 21.",
 7: "Si ya habéis hecho la compra con la lista anterior: os sobran los guisantes, el jamón, el secreto (al congelador, para el arroz del sábado 19 de diciembre), el pavo, el salmón (congelado, para el miércoles 2), la carne picada de las albóndigas y la mitad de las lentejas. Lo nuevo está en la lista: ternera para guisar, judías verdes, arroz basmati, miel, jengibre, copos de maíz y yogures +Proteínas. El pulpo cocido, compradlo ya (es para el martes 24: mirad la fecha). El rodaballo (1 de 1–1,2 kg), mejor fresco: el viernes 27 o el mismo sábado 28.",
 8: "Las 2 doradas de la comida del sábado 5 se hacen a la sal: enteras y sin escamar. Mejor frescas, compradas el viernes 4 o el mismo sábado; si no, congeladas enteras, y a la nevera la noche antes.",
}
for _s in SEMANAS:
    if "ciclo" in _s:
        NOTA_COMPRA[_s["num"]] = " ".join(x for x in (NOTA_FESTIVOS.get(_s["num"]), NOTA_CICLO[_s["ciclo"]]) if x)
PREP = {n: b['recordatorios'] for n, b in BATCH.items()}
if __name__ == "__main__":
    for s in SEMANAS: print(f"Semana {s['num']}: {', '.join(sorted(pescados_semana(s))) or '—'}")
    for e in comprobar_todo(): print("  NORMA:", e)
    for s in SEMANAS:
        print(f"\nSemana {s['num']} ({s['titulo']})")
        for i, fila in enumerate(s["filas"]):
            k, p = total_dia(fila)
            obj = 1950 if TIPO[i] == "E" else 1600
            nota = "  + cena fuera" if fila[3] == FUERA else ("  + comida y cena libres" if fila[1] == LIBRE else "  + cena libre") if fila[3] == LIBRE else f"  ({k-obj:+.0f} vs {obj})"
            print(f"  {DIAS[i]:10s} {TIPO[i]}  {k:5.0f} kcal  {p:5.0f} g prot  {' / '.join(fila)}{nota}")
