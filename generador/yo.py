"""Plan personal de Guillermo (23 de noviembre de 2026).

Come el 60 % de la comida y la cena que se cocina para los dos (Indi, el 40 %) y solo desayuna los días de gimnasio.
Entrena 3 días de gimnasio, 2–3 de pádel y 1 de carrera a la semana, en días que pueden cambiar, así que su plan va por
tipo de día (gimnasio, pádel, carrera o sin entreno) y no por día de la semana.
"""
from plan import R, NO_PLATO, macros_receta

REPARTO = 0.6                 # su parte de la comida y la cena
FACTOR = REPARTO * 2          # las recetas tienen las kcal por persona (el 50 %)
BATIDO = (120, 24)            # 1 cazo de proteína whey (30 g)
PREPADEL = (173, 11)          # 1 tostada integral (50 g) con 20 g de jamón serrano, antes del pádel


def _m(k):
    kc, p, _, _ = macros_receta(R[k])
    return kc, p


def dia_yo(fila):
    """Kcal y proteína de Guillermo un día del menú, según lo que entrene.
    Sin entreno y con pádel: sin desayuno y 2 cazos de proteína. Con gimnasio: el desayuno del menú y 1 cazo."""
    d, c, me, ce = fila
    k = p = 0.0
    partes = {}
    for slot, key in (("Comida", c), ("Cena", ce)):
        if key not in NO_PLATO:
            kc, pr = _m(key)
            partes[slot] = round(FACTOR * kc)
            k += FACTOR * kc; p += FACTOR * pr
    kc, pr = _m(me); k += kc; p += pr
    dk, dp = _m(d)
    base, base_p = k, p                      # su 60 % de comida y cena + la merienda, sin desayuno ni batidos
    indi = indi_p = 0.0                      # Indi: el 40 %, con su desayuno y su merienda
    for key in (c, ce):
        if key not in NO_PLATO:
            kc2, pr2 = _m(key); indi += (2 - FACTOR) * kc2; indi_p += (2 - FACTOR) * pr2
    kc2, pr2 = _m(me); indi += kc2 + dk; indi_p += pr2 + dp
    sin = (k + 2 * BATIDO[0], p + 2 * BATIDO[1])
    padel = (sin[0] + PREPADEL[0], sin[1] + PREPADEL[1])
    gym = (k + BATIDO[0] + dk, p + BATIDO[1] + dp)
    return dict(sin=round(sin[0]), sin_p=round(sin[1]), padel=round(padel[0]), padel_p=round(padel[1]),
                gym=round(gym[0]), gym_p=round(gym[1]), desayuno=round(dk), partes=partes,
                fuera=ce in NO_PLATO, base=round(base), base_p=round(base_p), des=round(dk), des_p=round(dp),
                indi=round(indi), indi_p=round(indi_p))


def medias(semanas):
    """Media de kcal y proteína por tipo de día (solo días con comida y cena en casa)."""
    filas = [f for s in semanas for f in s["filas"] if f[1] not in NO_PLATO and f[3] not in NO_PLATO]
    ds = [dia_yo(f) for f in filas]
    med = lambda k: round(sum(d[k] for d in ds) / len(ds))
    return {k: med(k) for k in ("sin", "sin_p", "padel", "padel_p", "gym", "gym_p")}


def redondea(v, paso=50):
    return int(round(v / paso) * paso)


def miles(v):
    return f"{v:,}".replace(",", ".")


def plan_yo(semanas):
    m = medias(semanas)
    gym, padel, sin = (miles(redondea(m[k])) for k in ("gym", "padel", "sin"))
    return dict(
        titulo="Tu plan, Guillermo",
        intro=[
            "Objetivo: bajar al 15 % de grasa (unos 80–82 kg) ganando algo de músculo. Punto de partida, el 23 de noviembre: 88,7 kg y 23,1 % de grasa.",
            "Con estas cantidades y tus entrenos, el déficit es de unas 400–500 kcal al día: unos 0,4 kg a la semana. Llegarías al 15 % hacia abril. Más deprisa, perderías músculo.",
        ],
        cifras=[("Proteína", "≈170 g al día"), ("Con gimnasio", f"≈{gym} kcal"), ("Con pádel", f"≈{padel} kcal"), ("Sin entreno", f"≈{sin} kcal")],
        secciones=[
            ("Tu parte del menú", [
                "Comida y cena: el 60 % de lo que se cocina para los dos, también el pan y la patata. Indi, el 40 %. De cada 5 cazos, 3 son tuyos.",
                "Desayuno: solo los días de gimnasio.",
                "Merienda: la del menú, todos los días.",
                "En cada día del menú tienes tus kcal y lo que cambian según entrenes.",
            ]),
            ("Días de gimnasio (3 a la semana)", [
                "El desayuno del menú: si entrenas a primera hora, al volver; si entrenas más tarde, 1–2 horas antes.",
                "Al terminar, 1 cazo de proteína (con agua, con leche o dentro del batido del desayuno).",
            ]),
            ("Días de pádel (2–3 a la semana)", [
                "Sin desayuno.",
                "1–2 horas antes de jugar, la merienda del menú con 1 cazo de proteína y 1 tostada integral con 20 g de jamón serrano (o un plátano más).",
                "Al terminar, el segundo cazo, o la cena (tu 60 %) si cenas en menos de una hora.",
                "Agua: medio litro antes y otro medio por cada hora de partido.",
            ]),
            ("Día de carrera (1 a la semana)", [
                "Sin desayuno. Si el rodaje pasa de 45 minutos, un plátano antes.",
                "2 cazos de proteína: en la merienda y al terminar.",
            ]),
            ("Días sin entreno", [
                "Sin desayuno. 2 cazos de proteína: en la merienda y de postre en la cena (o con un vaso de leche).",
            ]),
            ("Fin de semana", [
                "Viernes y sábado, cena fuera: un plato de proteína con verdura, sin pan ni fritos, y las 3 cervezas de la semana, con un vaso de agua entre una y otra.",
                "Domingo, vuelta al plan: pescado a mediodía y cena ligera.",
            ]),
            ("Cómo saber si funciona", [
                "Pésate cada mañana en ayunas y mira la media de la semana, no el dato de un día.",
                "La báscula de composición, una vez por semana, siempre igual (en ayunas y tras ir al baño). Con la creatina marcará algo más de agua y de peso: es normal.",
                "Si la media semanal no baja en 2–3 semanas, quita unas 150 kcal (por ejemplo, el pan de la cena). Si bajas más de 0,8 kg por semana o rindes peor en el pádel, añade la tostada de antes del pádel también los días de gimnasio.",
            ]),
            ("Para ganar músculo", [
                "Fuerza 3 días con cargas progresivas: cuando completes todas las repeticiones, sube el peso o una repetición.",
                "Unas 10–20 series por grupo muscular a la semana, acabando cada serie a 1–3 repeticiones del fallo.",
                "Duerme 7–8 horas: el músculo se construye descansando.",
            ]),
        ],
        suplementos=[
            ("Proteína whey", "1 cazo (30 g: 24 g de proteína y 120 kcal). 2 al día los días sin gimnasio.",
             "Después de entrenar; los días sin gimnasio, en la merienda y al terminar el pádel o de postre en la cena. Un bote de 1 kg te dura unas 3 semanas."),
            ("Creatina monohidrato", "5 g al día, también los días que no entrenas.",
             "Cuando quieras: en el batido o con la comida. Sin fase de carga."),
            ("Omega 3 (MyProtein)", "2 cápsulas al día; 1 las semanas con salmón (7 y 21 de diciembre).",
             "Con la comida, que lleva algo de grasa."),
            ("Vitamina D3", "1.000–2.000 UI al día, de octubre a marzo.",
             "Con la comida. Lo ideal es pedir en la próxima analítica la vitamina D (25-OH) y ajustar."),
            ("Magnesio (bisglicinato), opcional", "200–300 mg.",
             "30 minutos antes de dormir, si duermes mal o te dan calambres después del pádel."),
            ("Nada de", "Cafeína ni pre-entrenos (la cafeína sale 50 en tu test), quemagrasas ni BCAA.",
             "Con 170 g de proteína al día, los BCAA no aportan nada."),
        ],
    )


def reglas():
    """Todo lo acordado para el menú, para la pestaña «Tú» de la página."""
    return [
        ("Comidas", [
            "Lentejas, un solo día por semana. Ningún plato se repite dentro de la semana ni de una semana a la siguiente.",
            "El estofado de ternera (tu receta) es el guiso de carne habitual: cada dos semanas, a fuego suave en la Le Creuset (nunca en la olla a presión).",
            "Una vez al mes, el arroz meloso con secreto ibérico en la Le Creuset.",
            "Nunca pollo en la comida y en la cena del mismo día. Solomillos de pollo, no contramuslos.",
        ]),
        ("Cenas", [
            "Ligeras: cremas de la Mambo, sándwiches, tortilla o tomates rellenos.",
            "Kebab, fajitas, tacos o pizza, el día que a mediodía hay legumbre; hamburguesa, alguna vez.",
            "Viernes y sábado, cena fuera: ahí van las 3 cervezas de la semana.",
        ]),
        ("Pescado", [
            "Siempre a mediodía del fin de semana, porque se cocina el mismo día que se come.",
            "Salmón 2 semanas al mes; dorada a la sal y lubina a la sal, una vez al mes cada una. Los guisos y marmitakos se quedan.",
            "Merluza, siempre rebozada. Entre merluza y bacalao, una semana sin ninguno; y ningún pescado dos semanas seguidas.",
        ]),
        ("Lo que nunca entra", [
            "Pavo (tampoco en fiambre), atún, calabacín, lechuga y espinacas (en su lugar, canónigos o rúcula), champiñón, pepino, escarola, col, espárragos, alcachofa, hinojo y rábano.",
            "Almendras, nueces y avellanas; quesos curados, grasos o de oveja, y mantequilla; alubias (las judías verdes, sí); caballa, sardinas y almejas.",
            "Cafeína y pre-entrenos. Los guisantes con jamón no cuentan como plato principal.",
            "Con moderación: ajo, tomate, patata, berenjena y cacao (este, solo en natillas o porridge).",
        ]),
        ("Batch y compra", [
            "Compra el sábado y batch cooking el domingo, en dos tandas: la de mediodía (táperes) y la de cenas.",
            "En los fuegos, como mucho 2 ollas y 1 sartén a la vez; la Mambo, el horno y la airfryer van en paralelo.",
            "Táperes de lunes a miércoles, a la nevera; los de jueves y viernes, al congelador, y a la nevera la noche antes.",
            "Al repartir: 3 de cada 5 cazos para Guillermo y 2 para Indi.",
            "Navidad: la cena del 24 y el día 25, libres.",
        ]),
    ]
