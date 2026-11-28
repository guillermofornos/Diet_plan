"""Batch cooking de cada domingo (comidas de lunes a viernes en táper + preparación de cenas).
   Normas: lunes-miércoles en la nevera; jueves y viernes al congelador (se pasan a la nevera la noche antes);
   el pescado cocinado se hace el mismo día que se come. Programas del robot aproximados: ajústalos a tu modelo."""
NORMAS = [
 "Equipo: olla a presión, olla, la Le Creuset, sartén, horno, airfryer y robot de cocina (vuestra Mambo de Cecotec).",
 "En los fuegos, como mucho 2 ollas y 1 sartén a la vez: en los pasos, los fuegos 1 y 2 son de las ollas y el 3, de la sartén. El horno, la airfryer y el robot van en paralelo.",
 "El estofado de ternera, a fuego suave en la Le Creuset (1 h 30 min a 2 horas), nunca en la olla a presión. La última hora va solo: en ese rato cabe la tanda de cenas.",
 "Táperes de lunes a miércoles, a la nevera; los de jueves y viernes, al congelador, y se pasan a la nevera la noche antes.",
 "El pescado cocinado se hace el mismo día que se come: en el batch se deja la base o la salsa, y el pescado se cuece ese día.",
 "Deja templar la comida antes de guardarla, pero nunca más de 2 horas fuera de la nevera. Etiqueta cada táper con el día.",
 "Al repartir en táperes: 3 de cada 5 cazos para Guillermo (su 60 %) y 2 para Indi.",
 "Cenas ligeras: cremas, sándwiches, tortilla o tomates rellenos. Kebab, fajitas, tacos o pizza, el día que la comida es de legumbre (o una vez suelta a la semana). El pescado, a mediodía.",
 "Como mucho 2 platos con pollo a la semana, entre comidas y cenas. El menú es un ciclo de 5 semanas que se repite.",
 "Robot: los programas son los del libro de la Mambo o parecidos (trocear 4–5 s/vel 5; sofreír a 120 °C, vel 1). Para 4 raciones de legumbre no cabe: va en la olla a presión.",
]
# Pasos que se repiten en varias semanas (desde la 8)
GAMBAS_NOCHE = "Pasa las gambas cocidas del congelador a la nevera (ensalada de la cena de mañana)."
ENSALADA_HOY = ("Cena: ensalada de huevo y gambas, al momento (10 minutos): pela los huevos del batch y machácalos con el yogur y las mostazas; "
                "añade las gambas escurridas, el apio y la cebolla morada. Con el pan tostado.")
ESTOF_PREP = "Corta la carne del estofado (340 g) en dados y salpiméntala, y trocea en el robot su cebolla, su ajo y su zanahoria (4–5 s/vel 5)."
ESTOF_INICIO = ("Estofado (2 raciones): dora la carne 4–5 minutos y sácala; en la misma grasa, pocha la cebolla, el ajo y la zanahoria 10 minutos "
                "y el tomate rallado 5. Vuelve a meter la carne con el balsámico, cubre justo con el caldo (700 ml) y pon las hierbas; "
                "cuando hierva, tapa y a fuego suave 1 h 30 min, moviendo la olla de vez en cuando.")
ESTOF_FINAL = ("Estofado: prueba la carne (si sigue dura, 15 minutos más). Añade la patata chascada (400 g) y cuece 25–30 minutos, "
               "destapado al final si hace falta espesar; los guisantes, los últimos 5. Rectifica de sal.")
ESTOF_TAPER = "Deja templar el estofado y repártelo (3 cazos para Guillermo y 2 para Indi), a la nevera: es la comida del miércoles."
SALSA_PIQUILLOS = ("Salsa de piquillos del solomillo: trocea la cebolla y el ajo 4 s/vel 5 y sofríelos con la mitad del aceite 8 min/120 °C/vel 1; "
                   "añade los piquillos y el caldo, 5 min/100 °C/vel 1, y tritura 30 s, subiendo de vel 5 a 10.")
SOLOMILLO = ("Solomillo en salsa de piquillos (2 raciones): dora los medallones (340 g), salpimentados, 2 minutos por lado con el resto del aceite; "
             "echa la salsa del robot y cuécelos 4–5 minutos a fuego suave.")
TERIYAKI = ("Pollo teriyaki (2 raciones): dora el pollo (340 g) 4–5 minutos y sácalo; saltea las verduras 5–6 minutos; vuelve a meter el pollo "
            "con la salsa (soja, miel, jengibre, ajo, limón, agua y maicena) 1–2 minutos.")
BBQ_ADOBO = "Mezcla el adobo de la barbacoa, unta los solomillos (360 g) y déjalos marinando en la nevera."
BBQ_AIRFRYER = "Solomillos de la barbacoa a 180 °C 5 minutos; dales la vuelta, píntalos con la salsa barbacoa y 4–5 minutos más."
ENSALADA_BBQ = "Comida: la ensalada de los solomillos (canónigos, cherrys, cebolla morada, granada y mozzarella), al momento, y el aliño al servir."
PATATAS_MICRO = ("Patatas de los solomillos de la barbacoa (440 g en rodajas, con spray y sal), 10–12 minutos; luego las del solomillo de cerdo "
                 "(600 g en rodajas, tapadas con un poco de agua y sal), 8–10 minutos.")
POTAJE = ("Potaje de garbanzos (2 raciones): sofríe la cebolla y el ajo con el aceite 5 minutos; añade la patata chascada, el caldo, el tomate "
          "concentrado, el pimentón y el laurel, 20 minutos; luego los garbanzos y las acelgas, 10 minutos más.")
ALBON_MEZCLA = ("Mezcla de las albóndigas en el robot: cebolla, ajo, pan, leche, huevo y perejil 6 s/vel 6, y la carne con la sal 15–20 s/vel 5; "
                "a la nevera. Luego trocea, por tandas (4–5 s/vel 5), la cebolla del potaje, la cebolla, la zanahoria y el pimiento de la salsa de las "
                "albóndigas y los pimientos y el tomate del arroz con pollo, y guarda cada cosa aparte.")
ALBON_SALSA = "Salsa de las albóndigas: sofríe sus verduras con el aceite 8 minutos y añade el tomate y el laurel, 10 minutos; apártala del fuego."
ALBON_AIRFRYER = "Haz las albóndigas (unas 12, del tamaño de una nuez) y ponlas a 190 °C 8–10 minutos, en dos tandas si no caben."
ALBON_COCER = "Quita el laurel de la salsa, mete las albóndigas y cuécelas 10 minutos a fuego suave. Repártelas con el arroz."
ARRPOL_ROBOT = ("Arroz con pollo (2 raciones), con la mariposa: el aceite, el pollo, los pimientos, el tomate, las judías y el caldo, a 120 °C y vel 1 "
                "hasta que hierva (10–15 minutos); luego el arroz redondo (140 g), 15 min/100 °C/vel 0, y 5 minutos de reposo.")
LENTJ_ROBOT = ("Lentejas con jamón (2 raciones): trocea sus verduras 5 s/vel 5; con la mariposa, sofrito 8 min/120 °C/vel 1, y luego las lentejas "
               "escurridas, el jamón, la patata chascada, el caldo, el pimentón y el laurel, 25 min/100 °C/vel 1/giro inverso.")
TOFULONESA = ("Tofuloñesa: pocha la cebolla y los pimientos con el aceite 10 minutos; sube el fuego, añade el tofu y dóralo 6–8 minutos, "
              "removiendo poco, y luego el tomate, 8–10 minutos.")
BATCH = {
 3: dict(dia="Domingo 25 de octubre", duracion="1 h 45 min, aproximadamente",
   nevera=["Lentejas con pollo, 4 raciones (lunes y martes)",
           "Pechuga asada y desmenuzada para las fajitas (miércoles)", "Verduras picadas: fajicesta (lunes), pizza (martes) y fajitas (miércoles)"],
   congelador=["Tofuloñesa con los espaguetis, 2 raciones (jueves)", "Guisantes con jamón, 2 raciones (viernes)", "Solomillos del kebab en su marinado (jueves)",
               "Solomillos crudos de la barbacoa (sábado) y de los fingers (domingo), en bolsas"],
   pasos=[
    ("0:00", "Preparación", "Prensa el tofu entre papel de cocina con un peso encima. Lava las lentejas. Precalienta el horno a 200 °C."),
    ("0:05", "Robot y tabla", "Trocea en el robot, por tandas, la cebolla, la zanahoria, los pimientos y el puerro de las lentejas y de la tofuloñesa (4–5 s/vel 5), y guarda cada verdura aparte. A cuchillo: el tomate, la juliana de pimientos y cebolla de las fajitas, la verdura de la fajicesta y el pimiento y la cebolla de la pizza (estas tres, en táperes)."),
    ("0:20", "Horno", "Marina la pechuga de las fajitas con la soja, la mostaza y las especias y hornéala 25–30 minutos."),
    ("0:20", "Fuego 1 · olla a presión", "Dora el pollo de las lentejas 1 minuto por lado y resérvalo en la nevera. En la misma olla, sofrito: cebolla y zanahoria 10 minutos, pimientos y puerro 10 más, y el tomate con las especias."),
    ("0:25", "Fuego 2 · sartén", "Tofuloñesa: mezcla el tofu rallado con las especias; pocha la cebolla y los pimientos 10 minutos, añade el tofu 6–8 minutos y el tomate 8–10."),
    ("0:45", "Fuego 1 · olla a presión", "Añade las lentejas, la patata y el agua, cierra y cuece 12–15 minutos desde que suba la válvula. Deja que baje la presión sola."),
    ("0:50", "Horno", "Saca la pechuga, deja que temple, desmenúzala y guárdala. Apaga el horno."),
    ("0:55", "Fuego 3 · olla", "Agua a hervir y 130 g de espaguetis el tiempo del paquete. Escúrrelos y mézclalos con la tofuloñesa."),
    ("0:55", "Fuego 2 · sartén", "Guisantes del viernes: dora el jamón 1–2 minutos, pocha la cebolleta 4–5 y añade los guisantes congelados 5–7 minutos. Sin patata ni huevo: se ponen el jueves."),
    ("1:15", "Fuego 1", "Abre la olla, mete el pollo de las lentejas 5–6 minutos a fuego suave y rectifica de sal."),
    ("1:20", "Encimera", "Marinado del kebab: solomillos en tiras con las especias y el yogur, en una bolsa de congelación."),
    ("1:25", "Táperes", "Deja templar, reparte, etiqueta con el día y guarda: a la nevera lo de lunes a miércoles y al congelador lo de jueves y viernes."),
   ],
   recordatorios=[
    ("Lunes 26", "Compra 140 g de jamón cocido extra (o pechuga de pavo en lonchas) para la pizza del martes, que ya no lleva atún. El pil pil del miércoles necesita bacalao con piel: los lomos al punto de sal congelados la llevan."),
    ("Martes 27 por la noche", "Pasa el bacalao a la nevera. Asa el pimiento rojo en la airfryer (180 °C, 20 minutos) y cuece la patata en dados (6–7 minutos de microondas) para el pil pil; los dos, a la nevera."),
    ("Miércoles 28 por la mañana", "Bacalao al pil pil (unos 25 minutos: confitado a fuego suave y la salsa ligada con un colador); con la patata y el pimiento, a los táperes. Al recalentarlo, microondas a media potencia."),
    ("Miércoles 28 por la noche", "Pasa del congelador a la nevera la tofuloñesa (jueves) y el marinado del kebab."),
    ("Jueves 29", "Kebab: pon las patatas en remojo al llegar a casa."),
    ("Jueves 29 por la noche", "Pasa a la nevera los guisantes y los solomillos de la barbacoa; cuece 2 huevos 10 minutos y 300 g de patata en dados (5–6 minutos de microondas) y añádelos a los táperes del viernes."),
    ("Viernes 30 por la noche", "Deja los solomillos del sábado en el adobo barbacoa y pasa a la nevera los de los fingers."),
    ("Sábado 31", "Con la compra de la semana siguiente, coge canónigos y hierbabuena frescos para el domingo. No compres garbanzos: te quedan los de esta semana para el potaje del miércoles 4."),
    ("Sábado 31 por la noche", "Pasa la merluza a la nevera, haz la tártara y deja marinando los fingers (para el domingo)."),
   ]),
 4: dict(dia="Domingo 1 de noviembre", duracion="1 h 40 min, aproximadamente. Ese día, además, comes el fish & chips y cenas los fingers",
   nevera=["Lentejas al curry con pavo, 4 raciones con su arroz (lunes y martes)", "Ternera escalfada entera, en su salsa (cena del martes)",
           "Potaje de garbanzos con acelgas, 2 raciones, y 2 huevos duros con cáscara (miércoles)",
           "Pechuga asada y zanahoria rallada para los tacos (lunes)", "Pollo a la plancha para los tomates rellenos (miércoles)"],
   congelador=["Guisantes con jamón, 4 raciones (jueves y viernes)", "Solomillos del crispy en la leche (jueves)", "Pollo crudo de los burritos del domingo 8, en bolsa"],
   pasos=[
    ("0:00", "Preparación", "Lava las lentejas y el arroz. Precalienta el horno a 200 °C. Salpimienta la pieza de ternera."),
    ("0:05", "Robot y tabla", "Ralla en el robot la zanahoria de los tacos del lunes (500 g, por tandas de 5–6 s/vel 5) y guárdala. Trocea la cebolla de las lentejas y la del potaje (4–5 s/vel 5). A cuchillo: la calabaza en dados, las acelgas en tiras y la cebolla y la zanahoria de la ternera en cuartos."),
    ("0:20", "Robot", "Ternera escalfada: la pieza (340 g) con la zanahoria y la cebolla en cuartos, el ajo, el laurel, el caldo y el balsámico: 95 °C, 1 hora, sin movimiento (vel 0). Dale la vuelta a la media hora."),
    ("0:20", "Horno", "Pechuga de los tacos (300 g) untada con aceite y especias, 25 minutos."),
    ("0:20", "Fuego 1 · olla a presión", "Sofrito de cebolla y tomate 6–8 minutos y calabaza 2–3; añade las lentejas, el agua, la sal y el curry, cierra y cuece 12–15 minutos desde que suba la válvula."),
    ("0:25", "Fuego 2 · olla", "Arroz integral: 160 g para las lentejas, el tiempo del paquete."),
    ("0:25", "Fuego 3 · olla", "Potaje de garbanzos (2 raciones): sofríe la cebolla y el ajo con el aceite 5 minutos; añade la patata chascada, el caldo, el tomate concentrado, el pimentón y el laurel, 20 minutos; luego los garbanzos y las acelgas, 10 minutos más."),
    ("0:45", "Horno", "Saca la pechuga y desmenúzala. Apaga el horno."),
    ("0:50", "Fuego 1", "Cuando baje la presión, añade el pavo en dados y cuécelo 5–6 minutos a fuego suave."),
    ("1:00", "Fuego 1 · sartén", "Aparta la olla de las lentejas. Guisantes con jamón para el jueves y el viernes (4 raciones), sin patata ni huevo."),
    ("1:00", "Fuego 3 · cazo", "Aparta el potaje y cuece 2 huevos 10 minutos; guárdalos con cáscara."),
    ("1:05", "Fuego 2 · sartén", "Cuando el arroz esté hecho, escúrrelo y repártelo. En ese fuego, el solomillo de los tomates rellenos (160 g) a la plancha 6–7 minutos; desmenúzalo."),
    ("1:20", "Robot", "Saca la ternera y el laurel y tritura las verduras con el jugo (30 s/vel 5–10): es la salsa. Guarda la carne entera, en su salsa."),
    ("1:20", "Encimera", "Crispy del jueves: solomillos un poco aplastados con la leche, el pimentón y la sal, en una bolsa de congelación. El pollo de los burritos, en otra."),
    ("1:25", "Táperes", "Deja templar, reparte, etiqueta y guarda: nevera de lunes a miércoles; congelador los guisantes, el crispy y el pollo de los burritos. Para comer: el fish & chips, en la airfryer."),
   ],
   recordatorios=[
    ("Miércoles 4 por la noche", "Pasa a la nevera los guisantes del jueves y el crispy; cuece 3 huevos (2 para los táperes y 1 para la mayonesa) y 300 g de patata; haz la mayonesa proteica (robot, 15 s/vel 5)."),
    ("Jueves 5 por la noche", "Pasa a la nevera los guisantes del viernes y prepara sus huevos y su patata."),
    ("Viernes 6 por la noche", "Pasa la merluza a la nevera y deja hechos el pico de gallo y la salsa de yogur (tacos de merluza del sábado)."),
    ("Sábado 7 por la noche", "Pasa a la nevera el pollo de los burritos (comida del domingo)."),
   ]),
 5: dict(dia="Domingo 8 de noviembre", duracion="1 h 30 min, aproximadamente. Ese día, además, comes los burritos y cenas la crema de calabaza (hazla en el robot al terminar el batch)",
   nevera=["Lentejas con jamón, 4 raciones, y 4 huevos duros con cáscara (lunes y martes)", "Gratinado de patata y pollo al curry, 2 raciones (miércoles)",
           "Pimiento y cebolla en tiras para la pizza (lunes)"],
   congelador=["Albóndigas en salsa con su arroz, 2 raciones (jueves)", "Salsa vizcaína con su arroz, 2 raciones (viernes; el bacalao se cuece el viernes)", "Solomillos del crispy en la leche (jueves)",
               "Pechuga cruda del risotto, en dados (martes)", "Solomillos crudos de la barbacoa (sábado) y de los fingers (domingo), en bolsas"],
   pasos=[
    ("0:00", "Preparación", "Lava las lentejas (en la olla a presión no hace falta remojarlas) y el arroz. Si usas choriceros secos, ponlos en remojo. Precalienta el horno a 200 °C."),
    ("0:05", "Robot y tabla", "Trocea en el robot, por tandas, el ajo, el tomate, la zanahoria, el pimiento y la cebolla de las lentejas y la cebolla, la zanahoria y el pimiento de la salsa de las albóndigas (4–5 s/vel 5); guarda cada cosa aparte. Luego, la mezcla de las albóndigas: cebolla, ajo, pan, leche, huevo y perejil 6 s/vel 6, y la carne con la sal 15–20 s/vel 5. A cuchillo, el pimiento y la cebolla de la pizza del lunes."),
    ("0:20", "Robot", "Salsa vizcaína sin el bacalao: cebolla morada, puerro y pimiento verde troceados (5 s/vel 5); con el aceite y el ajo, 30 min/120 °C/vel 1/giro inverso, con el cestillo encima en vez del cubilete. Añade el tomate, el choricero y el pan: 3 min/120 °C. Añade el caldo: 15 min/100 °C/vel 1. Tritura 1 min a vel 5–10 progresivo (no hace falta colarla)."),
    ("0:20", "Airfryer", "Haz las albóndigas (unas 12, del tamaño de una nuez) y ponlas a 190 °C 8–10 minutos, en dos tandas si no caben."),
    ("0:20", "Fuego 1 · olla a presión", "Lentejas con jamón (4 raciones): sofríe sus verduras con el aceite 10 minutos."),
    ("0:25", "Fuego 2 · olla", "Arroz integral: 260 g (140 para la vizcaína y 120 para las albóndigas), el tiempo del paquete."),
    ("0:25", "Horno", "Gratinado al curry en una fuente: patata en rodajas finas con spray y sal 20 minutos; encima el pollo con el huevo, la leche y el curry, 12–15 minutos; la mozzarella y 3–4 minutos más."),
    ("0:30", "Fuego 1 · olla a presión", "Añade las lentejas, el jamón, la patata chascada, el caldo, el pimentón y el laurel: presión 12–15 minutos y que baje sola."),
    ("0:30", "Fuego 3 · sartén", "Salsa de las albóndigas: sofríe sus verduras con el aceite 8 minutos y añade el tomate y el laurel 10 minutos; quita el laurel, mete las albóndigas y cuécelas 10 minutos a fuego suave."),
    ("1:00", "Fuego 2 · cazo", "Cuando el arroz esté hecho, escúrrelo. En ese fuego, cuece 4 huevos 10 minutos para las lentejas; guárdalos con cáscara."),
    ("1:05", "Horno", "Saca el gratinado y deja que temple. Apaga el horno."),
    ("1:10", "Fuego 1", "Abre la olla y rectifica de sal las lentejas."),
    ("1:15", "Encimera", "Crispy del jueves: solomillos con la leche, el pimentón y la sal, en una bolsa de congelación. La pechuga del risotto (280 g), en dados y en otra bolsa."),
    ("1:20", "Táperes", "Deja templar, reparte y etiqueta: nevera de lunes a miércoles; congelador las albóndigas con su arroz, la salsa vizcaína con su arroz, el crispy, la pechuga del risotto y los solomillos de la barbacoa y de los fingers."),
   ],
   recordatorios=[
    ("Lunes 9 por la noche", "Pasa a la nevera la pechuga del risotto (cena del martes)."),
    ("Martes 10", "Risotto: en el robot, unos 30 minutos al llegar a casa."),
    ("Miércoles 11 por la noche", "Pasa a la nevera las albóndigas y el crispy del jueves; cuece 1 huevo y haz la mayonesa proteica."),
    ("Jueves 12 por la noche", "Pasa a la nevera la salsa vizcaína con su arroz, el bacalao y los solomillos de la barbacoa."),
    ("Viernes 13 por la mañana", "Calienta la salsa y cuece dentro el bacalao 10–12 minutos; con el arroz, a los táperes."),
    ("Viernes 13 por la noche", "Deja los solomillos del sábado en el adobo barbacoa y pasa a la nevera los de los fingers."),
    ("Sábado 14 por la noche", "Pasa los gambones del congelador a la nevera (arroz del domingo) y deja marinando los fingers."),
   ]),
 6: dict(dia="Domingo 15 de noviembre", duracion="1 h 45 min, aproximadamente. Ese día, además, comes el arroz meloso con gambones (unos 50 minutos, al terminar) y cenas los fingers",
   nevera=["Lentejas al curry con pavo, 4 raciones con su arroz (lunes y martes)", "Ternera a la jardinera, 2 raciones (miércoles)",
           "Pechuga asada para los tacos (martes) y para las fajitas (miércoles)", "Zanahoria rallada (tacos) y juliana (fajitas)",
           "Pollo del kebab marinado y salsa blanca (lunes)"],
   congelador=["Arroz con pollo y judías verdes, 2 raciones (jueves)", "Tofuloñesa, 2 raciones (viernes)", "Pollo crudo de los burritos del domingo 22, en bolsa"],
   pasos=[
    ("0:00", "Preparación", "Prensa el tofu. Lava las lentejas y el arroz integral. Precalienta el horno a 200 °C."),
    ("0:05", "Robot y tabla", "Ralla en el robot la zanahoria de los tacos (500 g) y trocea la cebolla de las lentejas, la cebolla y los pimientos de la tofuloñesa y los pimientos y el tomate del arroz con pollo (4–5 s/vel 5); guarda cada cosa aparte. A cuchillo: la calabaza, la juliana de las fajitas y el pollo del arroz en dados."),
    ("0:20", "Robot", "Ternera a la jardinera: la cebolla, el ajo, la zanahoria en trozos y el aceite, 5 s/vel 5; el jamón, 8 min/120 °C/vel 1; la carne, el caldo y la sal, 30 min/100 °C/vel 1/giro inverso; la patata, la zanahoria en rodajas y los guisantes, 20–25 min/100 °C/vel 0."),
    ("0:20", "Horno", "Las dos pechugas a la vez, cada una con lo suyo: la de los tacos (300 g, aceite y especias) y la de las fajitas (300 g, soja, mostaza y especias), 25–30 minutos."),
    ("0:20", "Fuego 1 · olla a presión", "Lentejas al curry: sofrito de cebolla y tomate, calabaza, lentejas, agua y curry; presión 12–15 minutos."),
    ("0:25", "Fuego 2 · olla", "Arroz integral: 160 g para las lentejas."),
    ("0:25", "Fuego 3 · sartén", "Tofuloñesa: cebolla y pimientos 10 minutos, tofu 6–8 y tomate 8–10."),
    ("0:50", "Horno", "Saca las pechugas y desmenúzalas por separado. Apaga el horno."),
    ("0:50", "Fuego 1", "Cuando baje la presión, añade el pavo y cuécelo 5–6 minutos."),
    ("0:55", "Fuego 3 · cazuela", "Arroz con pollo (2 raciones), en cazuela porque el robot está con el guiso: dora el pollo 4–5 minutos, añade los pimientos y el tomate 5 minutos y luego las judías y el caldo; cuando hierva, el arroz redondo (140 g) 15–17 minutos, sin remover."),
    ("1:00", "Fuego 1 · olla", "Aparta la olla de las lentejas y pon agua para la pasta: 130 g de espaguetis; mézclalos con la tofuloñesa."),
    ("1:10", "Encimera", "Kebab del lunes: marina los solomillos con las especias y el yogur y haz la salsa blanca (yogur, especias y limón); las dos cosas a la nevera. El pollo de los burritos, en una bolsa al congelador."),
    ("1:25", "Robot", "El guiso ya está: prueba la carne (si sigue dura, 10 minutos más) y rectifica de sal."),
    ("1:30", "Táperes", "Deja templar (el arroz, extendido en una fuente para que se enfríe rápido), reparte y etiqueta: nevera de lunes a miércoles; congelador el arroz con pollo y la tofuloñesa. Para comer: el arroz meloso con gambones."),
   ],
   recordatorios=[
    ("Lunes 16", "Kebab: pon las patatas en remojo al llegar a casa."),
    ("Miércoles 18 por la noche", "Pasa el arroz con pollo del jueves a la nevera."),
    ("Jueves 19 por la noche", "Pasa la tofuloñesa del viernes a la nevera."),
    ("Viernes 20 por la noche", "Pasa la merluza a la nevera y haz la tártara (fish & chips del sábado)."),
    ("Sábado 21 por la noche", "Pasa a la nevera el pollo de los burritos (comida del domingo) y el calamar de la crema (cena)."),
   ]),
 7: dict(dia="Domingo 22 de noviembre", duracion="1 h 45 min, aproximadamente (la carne guisada va casi toda sola, a fuego suave). Ese día, además, comes los burritos y cenas la crema de zanahoria con calamar (la crema, en el robot al terminar)",
   nevera=["Lentejas con pollo, 2 raciones (lunes)", "Crema de verduras, 2 raciones, y 4 huevos cocidos con cáscara (cena del lunes)",
           "Cachelos del pulpo, cocidos y pelados (martes)", "Gratinado de patata y pollo al curry, 2 raciones (miércoles)",
           "Crema de calabaza, 2 raciones (cena del miércoles)"],
   congelador=["Carne guisada con patatas, 2 raciones (jueves)", "Pollo teriyaki con su arroz y verduras, 2 raciones (viernes)",
               "Solomillos del crispy en la leche (jueves)"],
   pasos=[
    ("0:00", "Preparación", "Lava las lentejas (la pardina no necesita remojo) y el arroz basmati. Salpimienta la carne de guisar. Precalienta el horno a 200 °C."),
    ("0:05", "Robot y tabla", "Trocea en el robot, por tandas, la cebolla, la zanahoria y los pimientos de las lentejas y la cebolla, el pimiento verde, el ajo y la zanahoria de la carne guisada (4–5 s/vel 5), y guarda cada cosa aparte. A cuchillo: el puerro y el tomate rallado de las lentejas, el tomate rallado de la carne, el pollo del teriyaki en dados y sus verduras en tiras, y el puerro, la zanahoria y la patata de las dos cremas."),
    ("0:15", "Fuego 3 · cazuela", "Carne guisada (2 raciones): dora la carne (340 g) 4–5 minutos y sácala; pocha el sofrito 10 minutos y el tomate 5; el pimentón, la carne, el caldo (600 ml) y el laurel. Tapa y deja a fuego suave 1 hora."),
    ("0:20", "Fuego 1 · olla a presión", "Lentejas con pollo (2 raciones): dora los dados de pollo (300 g) 1 minuto por lado y resérvalos en la nevera. En la misma olla, sofrito: cebolla y zanahoria 10 minutos, pimientos 5–8 y puerro 5; luego el tomate, el pimentón, el comino y el laurel."),
    ("0:20", "Robot", "Crema de verduras: puerro y cebolla 6 s/vel 6 y sofrito 3 min/120 °C/vel 1; la zanahoria, la patata, las judías y el caldo, 20 min/110 °C/vel 0."),
    ("0:25", "Fuego 2 · olla", "Cachelos del martes: 500 g de patata con piel, en agua con sal, unos 20 minutos, hasta que se pinchen bien."),
    ("0:35", "Fuego 1 · olla a presión", "Añade las lentejas (160 g), la patata chascada y el agua (700 ml), cierra y cuece 12–15 minutos desde que suba la válvula. Deja que baje la presión sola."),
    ("0:45", "Robot", "Tritura la crema de verduras 30 s/vel 10, rectifica de sal y pásala a un táper. Sin lavar el vaso, crema de calabaza: puerro y cebolla 6 s/vel 6, sofrito 4 min/120 °C/vel 1 y la calabaza, la patata y el agua, 20 min/110 °C/vel 0."),
    ("0:45", "Fuego 2", "Escurre los cachelos, pélalos en caliente y córtalos en 4. En ese fuego, cuece 4 huevos 10 minutos (crema del lunes) y guárdalos con cáscara."),
    ("0:50", "Horno", "Gratinado al curry en una fuente: la patata (500 g) en rodajas finas, con spray y sal, 20 minutos."),
    ("1:00", "Fuego 2 · olla", "Arroz basmati del teriyaki: 130 g, el tiempo del paquete (10–12 minutos)."),
    ("1:05", "Fuego 1", "Abre la olla, mete el pollo de las lentejas 5–6 minutos a fuego suave, rectifica de sal y aparta."),
    ("1:05", "Robot", "Tritura la crema de calabaza 1 min/vel 7 y rectifica de sal."),
    ("1:10", "Fuego 1 · sartén grande", "Pollo teriyaki (2 raciones): dora el pollo (340 g) 4–5 minutos y sácalo; saltea las verduras 5–6 minutos; vuelve a meter el pollo con la salsa (soja, miel, jengibre, ajo, limón, agua y maicena) 1–2 minutos, hasta que brille."),
    ("1:10", "Horno", "Echa sobre la patata el pollo del curry mezclado con el huevo, la leche y el curry, 12–15 minutos; luego la mozzarella, 3–4 minutos. Apaga el horno."),
    ("1:15", "Fuego 3 · cazuela", "Añade a la carne las patatas chascadas (500 g), con un poco de agua si hace falta, y cuece 20 minutos más, destapada. Rectifica de sal."),
    ("1:20", "Encimera", "Crispy del jueves: los solomillos, un poco aplastados, con la leche, el pimentón y la sal, en una bolsa de congelación."),
    ("1:40", "Táperes", "Deja templar (el arroz, extendido en una fuente para que se enfríe rápido), reparte y etiqueta: nevera las lentejas, la crema de verduras con los huevos, los cachelos, el gratinado y la crema de calabaza; congelador la carne guisada, el teriyaki con el basmati y el crispy. Para comer: los burritos."),
   ],
   recordatorios=[
    ("Lunes 23", "Cena: calienta la crema de verduras; dora el jamón en taquitos en una sartén sin aceite y pela los huevos cocidos."),
    ("Martes 24", "Comida: abre el pulpo y témplalo con los cachelos (1–2 minutos de microondas, tapado); aceite, pimentón y sal gruesa al servir. Cena: el bol de avena (2 minutos)."),
    ("Miércoles 25 por la noche", "Pasa a la nevera la carne guisada y el crispy del jueves; cuece 1 huevo y haz la mayonesa proteica (robot, 15 s/vel 5)."),
    ("Jueves 26 por la noche", "Pasa el pollo teriyaki del viernes a la nevera."),
    ("Viernes 27", "Compra el rodaballo fresco (o mañana por la mañana): uno de 1–1,2 kg para los dos, limpio. A la nevera, y se hace mañana (unos 50 minutos, casi todo de horno)."),
    ("Domingo 29", "Comida y cena libres. El batch cooking de la semana siguiente, como siempre."),
   ]),
 8: dict(dia="Domingo 29 de noviembre", nota_dia="Ese día coméis y cenáis por libre.",
   tandas=[
    dict(nombre="Mediodía (táperes)", duracion="1 h 25 min, aproximadamente",
     nevera=["Solomillo de cerdo en salsa de piquillos, 2 raciones, y sus patatas (lunes)", "Albóndigas en salsa con su arroz, 2 raciones (martes)",
             "Solomillos al adobo barbacoa con sus patatas, 2 raciones (miércoles; la ensalada, al momento)", "2 huevos duros con cáscara para el potaje (jueves)"],
     congelador=["Potaje de garbanzos con acelgas, 2 raciones (jueves; congelado, la patata queda algo más harinosa)", "Arroz con pollo y judías verdes, 2 raciones (viernes)"],
     pasos=[
      ("0:00", "Preparación", "Lava el arroz integral y el redondo. " + BBQ_ADOBO),
      ("0:05", "Robot y tabla", ALBON_MEZCLA + " A cuchillo: las acelgas en tiras, el pollo del arroz en dados y el solomillo de cerdo en medallones."),
      ("0:15", "Robot", SALSA_PIQUILLOS + " Pásala a un bol y lava el vaso."),
      ("0:20", "Fuego 1 · olla", POTAJE),
      ("0:20", "Fuego 2 · olla", "Arroz integral de las albóndigas: 120 g, el tiempo del paquete; escúrrelo y resérvalo."),
      ("0:20", "Fuego 3 · sartén", ALBON_SALSA),
      ("0:25", "Airfryer", ALBON_AIRFRYER),
      ("0:35", "Robot", ARRPOL_ROBOT),
      ("0:45", "Fuego 3 · sartén", ALBON_COCER),
      ("0:50", "Airfryer", BBQ_AIRFRYER),
      ("0:55", "Fuego 1 · cazo", "Aparta el potaje. Cuece 2 huevos 10 minutos para el potaje y guárdalos con cáscara."),
      ("0:55", "Fuego 3 · sartén", "Pasa las albóndigas a sus táperes. " + SOLOMILLO),
      ("1:00", "Microondas", PATATAS_MICRO),
      ("1:25", "Táperes", "Deja templar (el arroz con pollo, extendido en una fuente para que se enfríe rápido) y reparte: 3 de cada 5 cazos para Guillermo y 2 para Indi. Nevera el solomillo de cerdo y los solomillos de la barbacoa, cada uno con sus patatas, las albóndigas con su arroz y los huevos; congelador el potaje y el arroz con pollo."),
     ]),
    dict(nombre="Cenas", duracion="45 min, aproximadamente (casi todo es la sopa en el robot): empiézala cuando el robot quede libre, hacia la 1 h 10 de la tanda de mediodía. Solo usa un fuego, para los huevos de la ensalada",
     nevera=["Pechuga asada y desmenuzada y juliana para las fajitas (lunes)", "Sopa cremosa de pollo, 2 raciones (martes; el huevo pochado, al momento)",
             "6 huevos cocidos con cáscara para la ensalada (miércoles)"],
     congelador=["Pollo del kebab marinado, en bolsa (jueves; la salsa blanca, el mismo jueves)", "Pechuga cruda de la crema de boniato del domingo 6 (360 g), en bolsa"],
     pasos=[
      ("0:00", "Horno", "Precalienta a 200 °C. Pechuga de las fajitas (300 g) con la soja, la mostaza y las especias, 25–30 minutos."),
      ("0:05", "Tabla", "Pela y trocea la patata, la cebolla y la zanahoria de la sopa, y corta la juliana de pimientos y cebolla de las fajitas (a un táper)."),
      ("0:10", "Robot", "Sopa cremosa de pollo (2 raciones), con la mariposa: las verduras, las pechugas enteras (360 g), el agua (700 ml), la sal, la pimienta, la cúrcuma y el laurel, 30 min/100 °C/vel 1/giro inverso."),
      ("0:15", "Encimera", "Kebab del jueves: marina los solomillos (360 g) con las especias y el yogur en una bolsa de congelación, al congelador. La pechuga de la crema de boniato del domingo 6 (360 g), cruda, en otra bolsa, también al congelador."),
      ("0:15", "Fuego 2 · cazo", "Cuece 6 huevos 10 minutos para la ensalada del miércoles y guárdalos con cáscara."),
      ("0:35", "Horno", "Saca la pechuga, desmenúzala y guárdala con la juliana. Apaga el horno."),
      ("0:40", "Robot", "Sopa: saca las pechugas y el laurel y tritura las verduras con el caldo 1 minuto, subiendo de vel 5 a 10; desmiga la pechuga, vuelve a echarla y calienta 2 min/90 °C/vel 1/giro inverso. Rectifica de sal."),
      ("0:45", "Táperes", "Deja templar y guarda: nevera la sopa, lo de las fajitas y los huevos; congelador el pollo del kebab y la pechuga de la crema."),
     ]),
   ],
   recordatorios=[
    ("Martes 1", "Cena: calienta la sopa y haz los huevos pochados al momento (3 minutos)."),
    ("Martes 1 por la noche", GAMBAS_NOCHE),
    ("Miércoles 2", ENSALADA_BBQ),
    ("Miércoles 2", ENSALADA_HOY),
    ("Miércoles 2 por la noche", "Pasa a la nevera el potaje (comida del jueves) y el pollo del kebab (cena del jueves)."),
    ("Jueves 3", "Kebab: pon las patatas en remojo al llegar a casa y haz la salsa blanca (yogur, especias y limón). Por la noche, pasa el arroz con pollo del viernes a la nevera."),
    ("Viernes 4", "Compra las 2 doradas frescas, enteras y sin escamar, para la comida de mañana (a la sal). Si son congeladas, a la nevera esta noche."),
    ("Sábado 5 por la noche", "Pasa del congelador a la nevera los gambones (arroz del domingo) y la pechuga de la crema de boniato (cena del domingo)."),
   ]),
}

# ---------------------------------------------------------------------------------------------------------------------
# CICLO DE 5 SEMANAS (desde la semana 9, lunes 7 de diciembre). Cada batch se hace el domingo anterior: ese día se
# comen y se cenan los platos del domingo de la semana previa del ciclo (la 5 antes de la 1). En los pasos, cada trozo
# lleva su plato: si un festivo deja libre esa comida o esa cena, el trozo se cae solo (plan.py: FESTIVOS).
def L(antes, lista, despues="."):
    """Frase con una enumeración de cosas por plato: «Nevera: a, b y c.»"""
    return dict(antes=antes, lista=lista, despues=despues)
REPARTO = "Deja templar y reparte: 3 de cada 5 cazos para Guillermo y 2 para Indi."
LENTJ_PRESION = ("Lentejas con jamón (2 raciones): sofríe su verdura troceada con el aceite 8–10 minutos; añade las lentejas, el jamón, la patata chascada, "
                 "el caldo, el pimentón y el laurel, cierra y cuece 12–15 minutos desde que suba la válvula. Apártala y deja que baje la presión sola.")
LENTJ_PREP = "Lava las lentejas (en la olla a presión no hace falta remojarlas) y trocea en el robot su verdura (ajo, tomate, zanahoria, pimiento verde y cebolla; 5 s/vel 5)."
HUEVOS_LENTJ = "Cuece 2 huevos 10 minutos para las lentejas y guárdalos con cáscara."
HUEVOS_PASTAF = "Cuece 4 huevos 10 minutos para la ensaladilla, enfríalos y pélalos."
PASTAF_TABLA = "Ensaladilla: ralla la zanahoria en hilos, corta las aceitunas en cuartos y el jamón cocido (160 g) en dados."
PASTAF_PASTA = "Pasta de la ensaladilla: 140 g con una ramita de romero, 8–10 minutos; refréscala con agua fría y escúrrela bien."
PASTAF_MEZCLA = ("Mahonesa proteica con la batidora: 2 de los huevos duros, el yogur (80 g), el aceite, la carne de choricero, unas gotas de vinagre y sal. "
                 "Mezcla la pasta con la zanahoria, las aceitunas, el jamón, el maíz, los otros 2 huevos en trozos y la mahonesa; perejil por encima.")
CERSAL_PREP = "Salpimienta el magro de cerdo (340 g), en dados de 3 cm."
CERSAL_DORAR = "Magro en salsa: dora la carne con la mitad del aceite, 4–5 minutos, y resérvala."
CERSAL_ROBOT = ("Trocea el ajo, la cebolla, el pimiento rojo y la zanahoria del magro 10 s/vel 6 y sofríelos con el resto del aceite 12 min/100 °C/vel 1. "
                "Pon la mariposa, añade la carne dorada, el laurel, el tomillo y el caldo (300 ml) y programa 45 min/100 °C/vel 1 con giro inverso.")
CERSAL_FIN = "El magro ya está: comprueba que la carne está tierna (si no, 10 minutos más), rectifica de sal y pásalo a un táper."
CERSAL_JUEVES = "Pasa el magro en salsa del viernes a la nevera y haz sus patatas (500 g en dados, tapadas con un poco de agua y sal, 8–10 minutos de microondas)."
ARR3D_PREP = "Lava el basmati; quítale el agua al tofu apretándolo entre papel de cocina con un peso encima."
ARR3D_ARROZ = ("Arroz del tres delicias: 120 g de basmati, 10–12 minutos; los últimos 2, añade la zanahoria en daditos (80 g) y los guisantes (120 g). "
               "Escúrrelo todo y extiéndelo en una fuente para que se enfríe.")
ARR3D_TOFU = "Corta el tofu del tres delicias (300 g) en filetes y úntalos con el aceite, la cebolla en polvo, el pimentón, la pimienta y la sal."
ARR3D_SARTEN = ("Arroz tres delicias: tuesta los filetes de tofu por los dos lados y sácalos; tuesta el jamón 1 minuto, añade el arroz frío con la zanahoria y "
                "los guisantes, 2 minutos; haz un hueco, cuaja los 2 huevos removiendo y mézclalo todo.")
TERESC_OLLA = ("Ternera escalfada: la pieza con la zanahoria y la cebolla en cuartos, el ajo, el laurel, el caldo (300 ml) y el balsámico; cuando rompa a hervir, "
               "tapa y baja al mínimo, 1 hora, dándole la vuelta a la media hora (en el libro va en el robot: 95 °C, 1 hora, sin velocidad).")
TERESC_SALSA = "Saca la ternera y el laurel y tritura las verduras con su jugo (batidora): es la salsa. Corta la carne en filetes finos y cúbrelos con la salsa."
CACHELOS = "Cachelos del pulpo del martes: 500 g de patata con piel, en agua con sal, unos 20 minutos, hasta que se pinchen bien; pélalos en caliente y córtalos en 4."
PULPO_HOY = "Comida: abre el pulpo y témplalo con los cachelos (1–2 minutos de microondas, tapado); aceite, pimentón y sal gruesa al servir."
ARRPOL_CAZUELA = ("Arroz con pollo (2 raciones): dora el pollo 4–5 minutos, añade los pimientos y el tomate 5 minutos y luego las judías y el caldo; "
                  "cuando hierva, el arroz redondo (140 g) 15–17 minutos, sin remover.")
POTAJE_ROBOT = ("Potaje de garbanzos (2 raciones): pica la cebolla y el ajo 10 s/vel 5; añade la patata chascada, el aceite, el caldo, el tomate concentrado, "
                "el pimentón y el laurel, 20 min/100 °C/vel 1/giro inverso, y luego los garbanzos y las acelgas, 10 minutos más.")
CREMCAL_ROBOT = "Crema de calabaza: puerro y cebolla 6 s/vel 6, sofrito 4 min/120 °C/vel 1 y la calabaza, la patata y el agua, 20 min/110 °C/vel 0; tritura 1 min/vel 7, rectifica de sal y pásala a un táper."
CREMZAN_ROBOT = ("Crema de zanahoria (cena de hoy): puerro y cebolla 6 s/vel 6 y sofrito 3 min/120 °C/vel 1; la patata chascada, la zanahoria, el caldo, la sal y la pimienta, "
                 "24 min/110 °C/vel 0, sin cubilete; añade la leche y tritura 1 min/vel 8.")
CREMVER_ROBOT = ("Crema de verduras: puerro y cebolla 6 s/vel 6 y sofrito 3 min/120 °C/vel 1; la zanahoria, la patata, las judías verdes y el caldo, 20 min/110 °C/vel 0; "
                 "tritura 30 s/vel 10, rectifica de sal y pásala a un táper.")
CASTA_ROBOT = ("Crema de boniato con pollo (cena de hoy): cebolla y puerro 5 s/vel 5 y 8 min/120 °C/vel 1; el boniato, 3 min; con la mariposa, las pechugas, la sal, "
               "la pimienta y el agua, 20–25 min/100 °C/vel 1/giro inverso; saca las pechugas y tritura.")
SOPA_ROBOT1 = "Sopa cremosa de pollo (2 raciones), con la mariposa: las verduras, las pechugas enteras (360 g), el agua (700 ml), la sal, la pimienta, la cúrcuma y el laurel, 30 min/100 °C/vel 1/giro inverso."
SOPA_ROBOT2 = ("Sopa: saca las pechugas y el laurel y tritura las verduras con el caldo 1 minuto, subiendo de vel 5 a 10; desmiga la pechuga, vuelve a echarla y calienta "
               "2 min/90 °C/vel 1/giro inverso. Rectifica de sal y pásala a un táper.")
ARRGAMB_FUMET = ("Arroz meloso con gambones para comer hoy (unos 50 minutos): pela las colas y guárdalas; fumet con las cabezas y las cáscaras, el puerro, el tomate y el agua, "
                 "20 minutos; cuélalo y mantenlo caliente.")
ARRGAMB_SOFRITO = "Marca las colas 1 minuto y resérvalas; con el resto del aceite, pocha el ajo y la cebolla 5 minutos, los pimientos y el laurel 10 y el tomate 10 más."
ARRGAMB_ARROZ = "El pimentón, el arroz (140 g) 1 minuto, el fumet caliente y el azafrán: 17–18 minutos a fuego medio, removiendo de vez en cuando, y las colas encima los últimos 2. A comer, meloso."
RAPE_HOY = ("Marmitako de rape para comer hoy (unos 55 minutos): calienta el caldo con el puerro y el perejil (5 minutos de microondas) y cuélalo; en la cazuela, el sofrito de "
            "cebolleta y pimientos 15 minutos, el tomate 5 y el choricero; las patatas chascadas, cubiertas con el caldo, 30–35 minutos, y el rape, un par de minutos al final.")
CREMCAL_HOY = "Cena: calienta la crema de calabaza y haz la tortilla de claras con jamón al momento."
PZA_HOY = "Cena: pizza de avena y yogur, al momento (la masa y 10–12 minutos de horno), con el pimiento y la cebolla del batch."
SALMON_COMPRA = "Compra el salmón para la comida del sábado: fresco, o congelado y a la nevera la noche antes."
ARRPOL_PREP = "Lava el arroz redondo; trocea en el robot los pimientos y el tomate del arroz con pollo (4–5 s/vel 5) y guárdalos; el pollo, en dados."
ALBON_ROBOT = "Mezcla de las albóndigas en el robot: cebolla, ajo, pan, leche, huevo y perejil 6 s/vel 6, y la carne con la sal 15–20 s/vel 5; a la nevera."
ARROZ_ALBON = "Arroz integral de las albóndigas: 120 g, el tiempo del paquete; escúrrelo y resérvalo."
HUEVOS_POTG = "Cuece 2 huevos 10 minutos para el potaje y guárdalos con cáscara."
BOLO_VERDURA = "Trocea en el robot el ajo, la cebolleta y la zanahoria de la boloñesa (5 s/vel 5)."
BOLO_SALSA = ("Salsa boloñesa (2 raciones): rehoga la verdura troceada con el aceite a fuego suave 15 minutos; añade la carne picada (300 g), "
              "salpimentada, y suéltala 5 minutos; luego el orégano, la albahaca, el caldo (100 ml) y el tomate (300 g), 30 minutos a fuego suave.")
BOLO_PASTA = "Macarrones de la boloñesa: 160 g, 1–2 minutos menos de lo que diga el paquete; escúrrelos y mézclalos con la salsa, ya fuera del fuego."
MISO_SALSA = "Mezcla la salsa de la ternera al miso: la soja, el miso, la miel, el ajo picado, el jengibre rallado y la guindilla."
MISO_INICIO = ("Ternera al miso (2 raciones): la pieza (340 g) en la Le Creuset, con la salsa por encima y el caldo (120 ml); cuando hierva, tapa y "
               "a fuego mínimo 2 h 30, dándole la vuelta cada hora.")
MISO_FINAL = ("Ternera al miso: desmenúzala dentro de su salsa con dos tenedores (si sigue dura, 15 minutos más; si está muy líquida, destapa y reduce). "
              "Repártela con el arroz y las judías verdes; la cebolleta y el sésamo, al servir.")
MISO_ARROZ = "Arroz de la ternera al miso: 150 g de basmati, el tiempo del paquete. Las judías verdes (160 g), 6–8 minutos en el microondas con un poco de agua."
SOPAV_ROBOT = ("Sopa casera de pollo y verduras (2 raciones), con la mariposa: las verduras en trozos, las pechugas enteras (300 g), el aceite, el ajo, "
               "las especias y el agua (900 ml), 30 min/100 °C/vel 1/giro inverso. Saca las pechugas, tritura 1 minuto subiendo de vel 5 a 10, "
               "desmiga el pollo y vuelve a echarlo, 2 min/90 °C/vel 1/giro inverso.")
CRI_LECHE = "Crispy del martes: los solomillos (300 g), un poco aplastados, con la leche, el pimentón y la sal, en un táper a la nevera."
CRI_MAYO = "Haz la mayonesa proteica del crispy de mañana: el huevo cocido del batch, el yogur, el aceite, sal y limón (batidora)."
CRI_HOY = "Cena: crispy chicken burger: reboza los solomillos del batch (harina de avena, huevo y copos de maíz) y a la airfryer, 5–6 minutos por lado."
FIN_HOY = "Cena: fingers de pollo: reboza los solomillos en los copos de maíz triturados y a la airfryer (180 °C, 7 minutos por lado); con la ensalada."

CICLO_BATCH = {
 1: dict(nota_dia="Ese día comes el arroz meloso con gambones y cenas la crema de boniato con pollo (en la tanda de cenas).",
   tandas=[
    dict(nombre="Mediodía (táperes)", duracion="2 h 35 min, aproximadamente, por el estofado: a la 1 h 20 están los táperes y hacia las 2 h 10 coméis el arroz meloso con gambones; luego el estofado acaba solo, a fuego suave (en ese rato cabe la tanda de cenas)",
     nevera=[[("LENTJ", "Lentejas con jamón, 2 raciones, y 2 huevos duros con cáscara (lunes)")], [("BOLO", "Macarrones a la boloñesa, 2 raciones (martes)")],
             [("ESTOF", "Estofado de ternera, 2 raciones (miércoles)")]],
     congelador=[[("ARR3D", "Arroz tres delicias con tofu, 2 raciones (jueves)")], [("CERSAL", "Magro de cerdo en salsa, 2 raciones (viernes; las patatas, el jueves por la noche)")]],
     pasos=[
      ("0:00", "Preparación", [("LENTJ", LENTJ_PREP), ("BOLO", BOLO_VERDURA), ("ARR3D", ARR3D_PREP), ("ESTOF", ESTOF_PREP), ("CERSAL", CERSAL_PREP)]),
      ("0:05", "Fuego 1 · Le Creuset", [("ESTOF", ESTOF_INICIO)]),
      ("0:05", "Fuego 2 · olla", [("ARR3D", ARR3D_ARROZ)]),
      ("0:05", "Fuego 3 · sartén", [("CERSAL", CERSAL_DORAR)]),
      ("0:10", "Robot", [("CERSAL", CERSAL_ROBOT)]),
      ("0:12", "Fuego 3 · sartén honda", [("BOLO", BOLO_SALSA)]),
      ("0:20", "Fuego 2 · olla a presión", [("LENTJ", LENTJ_PRESION)]),
      ("0:20", "Tabla", [("ARR3D", ARR3D_TOFU)]),
      ("0:45", "Fuego 2 · cazo", [("LENTJ", HUEVOS_LENTJ)]),
      ("0:55", "Fuego 2 · olla", [("BOLO", BOLO_PASTA)]),
      ("1:00", "Fuego 3 · sartén", [("BOLO", "Aparta la salsa de la boloñesa."), ("ARR3D", ARR3D_SARTEN)]),
      ("1:10", "Robot", [("CERSAL", CERSAL_FIN)]),
      ("1:20", "Táperes", [(None, REPARTO), L("Nevera: ", [("LENTJ", "las lentejas con sus huevos"), ("BOLO", "los macarrones a la boloñesa")]),
                           L("Congelador, en cuanto temple: ", [("ARR3D", "el arroz tres delicias con su tofu"), ("CERSAL", "el magro en salsa")]),
                           ("ESTOF", "El estofado sigue solo, a fuego suave.")]),
      ("1:20", "Fuego 2 · cazo", [("ARRGAMB", ARRGAMB_FUMET)]),
      ("1:20", "Fuego 3 · sartén grande", [("ARRGAMB", ARRGAMB_SOFRITO)]),
      ("1:45", "Fuego 3 · sartén grande", [("ARRGAMB", ARRGAMB_ARROZ)]),
      ("2:00", "Fuego 1 · Le Creuset", [("ESTOF", ESTOF_FINAL)]),
      ("2:35", "Táperes", [("ESTOF", ESTOF_TAPER)]),
     ]),
    dict(nombre="Cenas", duracion="1 h, aproximadamente, con la crema de boniato de la cena de hoy. Empiézala cuando el robot quede libre, hacia la 1 h 10 de la tanda de mediodía",
     nevera=[[("TAC", "Pechuga asada y desmenuzada y zanahoria rallada para los tacos (lunes)")], [("FIN", "Solomillos de los fingers, crudos (martes; se marinan el lunes por la noche)")],
             [("CREMCAL", "Crema de calabaza, 2 raciones (miércoles; la tortilla, al momento)")], [("ENSHUEVO", "6 huevos cocidos con cáscara para la ensalada (jueves)")]],
     congelador=[],
     pasos=[
      ("0:00", "Horno", [("TAC", "Precalienta a 200 °C. Pechuga de los tacos (300 g) untada con aceite y especias, 25 minutos.")]),
      ("0:05", "Robot y tabla", [("TAC", "Ralla en el robot la zanahoria de los tacos (500 g, por tandas de 5–6 s/vel 5) y guárdala."),
                                 L("A cuchillo: ", [("CREMCAL", "la calabaza, el puerro, la cebolla y la patata de la crema de calabaza"), ("CASTA", "la cebolla, el puerro y el boniato de la crema de boniato")])]),
      ("0:10", "Encimera", [("FIN", "Fingers del martes: guarda los solomillos (400 g) en un táper, a la nevera; se marinan el lunes por la noche.")]),
      ("0:15", "Robot", [("CREMCAL", CREMCAL_ROBOT)]),
      ("0:20", "Fuego 2 · cazo", [("ENSHUEVO", "Cuece 6 huevos 10 minutos para la ensalada del jueves y guárdalos con cáscara.")]),
      ("0:25", "Horno", [("TAC", "Saca la pechuga de los tacos y desmenúzala. Apaga el horno.")]),
      ("0:45", "Robot", [("CASTA", CASTA_ROBOT)]),
      ("1:00", "Táperes", [L("Deja templar y guarda en la nevera ", [("CREMCAL", "la crema de calabaza"), ("TAC", "lo de los tacos"), ("FIN", "los solomillos de los fingers"), ("ENSHUEVO", "los huevos")]),
                           ("CASTA", "Para cenar, la crema de boniato con pollo.")]),
     ]),
   ],
   recordatorios=[
    (0, "noche", "FIN", "Marina los solomillos de los fingers de mañana en el huevo batido con el pimentón, la cebolla y el ajo en polvo y la sal; tapados, a la nevera."),
    (1, "", "FIN", FIN_HOY),
    (2, "", "CREMCAL", CREMCAL_HOY),
    (2, "noche", "ARR3D", "Pasa a la nevera el arroz tres delicias (comida del jueves)."),
    (2, "noche", "ENSHUEVO", GAMBAS_NOCHE),
    (3, "", "ENSHUEVO", ENSALADA_HOY),
    (3, "noche", "CERSAL", CERSAL_JUEVES),
    (4, "", "SALM2", SALMON_COMPRA, "compra"),
    (5, "", "LUBSAL", "Con la compra de la semana siguiente, coge las 2 lubinas frescas, enteras y sin escamar, para la comida del domingo.", "compra"),
    (5, "", "CREMVER", "Haz la crema de verduras en el robot (unos 25 minutos) para la cena del domingo y guárdala en la nevera."),
   ]),
 2: dict(nota_dia="Ese día comes la lubina a la sal con pisto (en la tanda de mediodía) y cenas la crema de verduras, hecha el sábado.",
   tandas=[
    dict(nombre="Mediodía (táperes)", duracion="1 h 40 min, aproximadamente: a la 1 h 25 están los táperes y a la 1 h 40 coméis la lubina a la sal",
     nevera=[[("SOLPIQ", "Solomillo de cerdo en salsa de piquillos, 2 raciones, y sus patatas (lunes)")], [("PULPO", "Cachelos del pulpo, cocidos y pelados (martes; el pulpo, en su envase)")],
             [("POTG", "Potaje de garbanzos con acelgas, 2 raciones, y 2 huevos duros con cáscara (miércoles)")]],
     congelador=[[("ALBON", "Albóndigas en salsa con su arroz, 2 raciones (jueves)")], [("ARRPOL", "Arroz con pollo y judías verdes, 2 raciones (viernes)")],
                 [("ARRSEC", "Secreto ibérico crudo del arroz del sábado, en bolsa")]],
     pasos=[
      ("0:00", "Preparación", [L("Lava ", [("ALBON", "el arroz integral"), ("ARRPOL", "el arroz redondo")])]),
      ("0:05", "Robot y tabla", [("ALBON", ALBON_ROBOT),
                                 L("Luego trocea, por tandas (4–5 s/vel 5) y guardando cada cosa aparte, ", [("POTG", "la cebolla del potaje"), ("ALBON", "la cebolla, la zanahoria y el pimiento de la salsa de las albóndigas"), ("ARRPOL", "los pimientos y el tomate del arroz con pollo")]),
                                 L("A cuchillo: ", [("POTG", "las acelgas en tiras"), ("ARRPOL", "el pollo del arroz en dados"), ("SOLPIQ", "el solomillo de cerdo en medallones"), ("LUBSAL", "los pimientos, la cebolla y el tomate del pisto, en dados")])]),
      ("0:15", "Robot", [("SOLPIQ", SALSA_PIQUILLOS + " Pásala a un bol y lava el vaso.")]),
      ("0:15", "Fuego 1 · olla", [("POTG", POTAJE)]),
      ("0:15", "Fuego 2 · olla", [("ALBON", ARROZ_ALBON)]),
      ("0:15", "Fuego 3 · sartén", [("ALBON", ALBON_SALSA)]),
      ("0:20", "Airfryer", [("ALBON", ALBON_AIRFRYER)]),
      ("0:35", "Robot", [("ARRPOL", ARRPOL_ROBOT)]),
      ("0:40", "Fuego 3 · sartén", [("ALBON", ALBON_COCER)]),
      ("0:45", "Fuego 2 · olla", [("PULPO", CACHELOS)]),
      ("0:50", "Fuego 1 · cazo", [("POTG", "Aparta el potaje. " + HUEVOS_POTG)]),
      ("0:50", "Fuego 3 · sartén", [("ALBON", "Pasa las albóndigas a sus táperes."), ("SOLPIQ", SOLOMILLO)]),
      ("1:00", "Microondas", [("SOLPIQ", "Patatas del solomillo: 600 g en rodajas, tapadas con un poco de agua y sal, 8–10 minutos.")]),
      ("1:00", "Fuego 3 · sartén", [("SOLPIQ", "Pasa el solomillo a su táper."), ("LUBSAL", "Pisto: pimiento verde 5 minutos, pimiento rojo y cebolla 10 y tomate 10 más.")]),
      ("1:10", "Horno", [("LUBSAL", "Precalienta a 200 °C para la lubina.")]),
      ("1:20", "Horno", [("LUBSAL", "Lubinas a la sal: mezcla la sal gruesa con las hierbas y las pimientas, humedécela, haz una cama en una bandeja, pon las lubinas sin escamar y cúbrelas bien; 18–20 minutos. La patata de la lubina, en dados, 6–7 minutos de microondas.")]),
      ("1:25", "Táperes", [(None, REPARTO), ("ARRPOL", "El arroz con pollo, antes, extendido en una fuente para que se enfríe rápido."),
                           L("Nevera: ", [("SOLPIQ", "el solomillo de cerdo con sus patatas"), ("PULPO", "los cachelos"), ("POTG", "el potaje con sus huevos")]),
                           L("Congelador: ", [("ALBON", "las albóndigas con su arroz"), ("ARRPOL", "el arroz con pollo"), ("ARRSEC", "el secreto (crudo, en bolsa)")])]),
      ("1:40", "Horno", [("LUBSAL", "Saca las lubinas, rompe la costra de sal y a comer, con el pisto y la patata.")]),
     ]),
    dict(nombre="Cenas", duracion="25 min, aproximadamente. Cabe después de comer",
     nevera=[[("ENSHUEVO", "6 huevos cocidos con cáscara para la ensalada (lunes)")], [("PZA", "Pimiento y cebolla en tiras para la pizza (martes)")]],
     congelador=[[("KEB", "Pollo del kebab marinado, en bolsa (miércoles; la salsa blanca, el mismo miércoles)")]],
     pasos=[
      ("0:00", "Tabla", [("PZA", "Corta en tiras el pimiento y la cebolla de la pizza del martes (a un táper).")]),
      ("0:05", "Encimera", [("KEB", "Kebab del miércoles: marina los solomillos (360 g) con las especias y el yogur en una bolsa de congelación, al congelador.")]),
      ("0:10", "Fuego 2 · olla", [L("Cuece 10 minutos: ", [("CREMVER", "4 huevos para la crema de verduras de esta noche"), ("ENSHUEVO", "6 huevos para la ensalada de mañana, que se guardan con cáscara")])]),
      ("0:25", "Táperes", [L("Guarda en la nevera ", [("PZA", "lo de la pizza"), ("ENSHUEVO", "los 6 huevos")]),
                           ("CREMVER", "Para cenar, la crema de verduras (hecha ayer) con los huevos y el jamón crujiente."),
                           ("ENSHUEVO", "Antes de acostarte, pasa las gambas cocidas del congelador a la nevera: la ensalada es mañana.")]),
     ]),
   ],
   recordatorios=[
    (0, "", "ENSHUEVO", ENSALADA_HOY),
    (1, "", "PULPO", PULPO_HOY),
    (1, "", "PZA", PZA_HOY),
    (1, "noche", "KEB", "Pasa el pollo del kebab del congelador a la nevera (cena de mañana)."),
    (2, "", "KEB", "Kebab: pon las patatas en remojo al llegar a casa y haz la salsa blanca (yogur, especias y limón)."),
    (2, "noche", "ALBON", "Pasa las albóndigas del jueves a la nevera."),
    (3, "", "TOR", "Cena: tortilla de patata con claras, al momento (unos 25 minutos)."),
    (3, "noche", "ARRPOL", "Pasa el arroz con pollo del viernes a la nevera."),
    (4, "noche", "ARRSEC", "Pasa el secreto ibérico a la nevera (arroz meloso del sábado, en la Le Creuset)."),
    (5, "noche", "RAPE", "Pasa el rape del congelador a la nevera (marmitako del domingo)."),
   ]),
 3: dict(nota_dia="Ese día comes el marmitako de rape y cenas la crema de zanahoria con su tosta (en la tanda de cenas).",
   tandas=[
    dict(nombre="Mediodía (táperes)", duracion="1 h 45 min, aproximadamente. Para comer hoy, el marmitako de rape (unos 55 minutos, a partir de la 1 h 25)",
     nevera=[[("LENTJ", "Lentejas con jamón, 2 raciones, y 2 huevos duros con cáscara (lunes)")], [("PASTAF", "Ensaladilla de pasta y jamón, 2 raciones (martes)")],
             [("TERESC", "Ternera escalfada en filetes, con su salsa y sus patatas, 2 raciones (miércoles)")]],
     congelador=[[("ARR3D", "Arroz tres delicias con tofu, 2 raciones (jueves)")], [("PASTEL", "Pastel de carne con puré de boniato, 2 raciones (viernes)")]],
     pasos=[
      ("0:00", "Preparación", [("LENTJ", LENTJ_PREP), ("PASTEL", "Trocea también la cebolla, el ajo y la zanahoria del pastel de carne; pela y trocea el boniato (500 g) y precalienta el horno a 200 °C."),
                               ("ARR3D", ARR3D_PREP),
                               ("TERESC", "Salpimienta la pieza de ternera (340 g).")]),
      ("0:05", "Fuego 1 · olla", [("TERESC", TERESC_OLLA)]),
      ("0:05", "Fuego 2 · olla", [("PASTEL", "Boniato del pastel: cuécelo en agua con sal 10–15 minutos, hasta que esté tierno; escúrrelo y aplástalo con la leche, el huevo batido, sal y pimienta.")]),
      ("0:10", "Fuego 3 · sartén", [("PASTEL", "Carne del pastel: pocha la cebolla, el ajo y la zanahoria con el aceite 10 minutos; añade la carne picada (300 g), salpimienta y suéltala 4–5 minutos; el tomate y el orégano, 5–6 minutos más, hasta que quede seca.")]),
      ("0:20", "Fuego 2 · olla a presión", [("LENTJ", LENTJ_PRESION)]),
      ("0:35", "Horno", [("PASTEL", "Monta el pastel en una fuente (una capa fina de puré, la carne, el resto del puré y la mozzarella) y hornéalo 20 minutos a 200 °C.")]),
      ("0:35", "Tabla", [("ARR3D", ARR3D_TOFU)]),
      ("0:45", "Fuego 2 · cazo", [("LENTJ", HUEVOS_LENTJ), ("PASTAF", HUEVOS_PASTAF)]),
      ("0:45", "Tabla", [("PASTAF", PASTAF_TABLA)]),
      ("0:55", "Fuego 2 · olla", [("PASTAF", PASTAF_PASTA)]),
      ("0:55", "Horno", [("PASTEL", "Saca el pastel y deja que temple antes de cortarlo en 2 raciones.")]),
      ("1:05", "Encimera", [("TERESC", TERESC_SALSA), ("PASTAF", PASTAF_MEZCLA)]),
      ("1:10", "Fuego 2 · olla", [("ARR3D", ARR3D_ARROZ)]),
      ("1:10", "Microondas", [("TERESC", "Patatas de la ternera: 500 g en rodajas, tapadas con un poco de agua y sal, 8–10 minutos.")]),
      ("1:25", "Fuego 1 · cazuela", [("RAPE", RAPE_HOY)]),
      ("1:35", "Fuego 3 · sartén", [("ARR3D", ARR3D_SARTEN)]),
      ("1:45", "Táperes", [(None, REPARTO), L("Nevera: ", [("LENTJ", "las lentejas con sus huevos"), ("PASTAF", "la ensaladilla"), ("TERESC", "la ternera en su salsa con las patatas")]),
                           L("Congelador, en cuanto temple: ", [("ARR3D", "el arroz tres delicias con su tofu"), ("PASTEL", "el pastel de carne, en raciones")])]),
     ]),
    dict(nombre="Cenas", duracion=[L("Hasta 1 h 40 min, casi todo de robot: ", [("SOPA", "la sopa"), ("CREMCAL", "la crema de calabaza"), ("CREMZAN2", "la crema de zanahoria de la cena de hoy")], ". Puede ir a la vez que la tanda de mediodía, que solo usa el robot para trocear")],
     nevera=[[("FAJ", "Pechuga asada y desmenuzada y juliana para las fajitas (lunes)")], [("SOPA", "Sopa cremosa de pollo, 2 raciones (miércoles; el huevo pochado, al momento)")]],
     congelador=[[("FF2", "Carne de la Big Mac, en 4 bolitas de 75 g (martes)")], [("CREMCAL", "Crema de calabaza, 2 raciones (jueves; la tortilla, al momento)")]],
     pasos=[
      ("0:00", "Horno", [("FAJ", "A 200 °C: pechuga de las fajitas (300 g) con la soja, la mostaza y las especias, 25–30 minutos.")]),
      ("0:05", "Tabla", [L("Corta ", [("FAJ", "la juliana de pimientos y cebolla de las fajitas (a un táper)"), ("SOPA", "la patata, la cebolla y la zanahoria de la sopa"),
                                      ("CREMCAL", "la calabaza, el puerro, la cebolla y la patata de la crema de calabaza"), ("CREMZAN2", "la zanahoria, la patata, el puerro y la cebolla de la crema de zanahoria")])]),
      ("0:10", "Robot", [("SOPA", SOPA_ROBOT1)]),
      ("0:15", "Encimera", [("FF2", "Big Mac del martes: forma 4 bolitas de 75 g con la carne picada (300 g), envuélvelas y al congelador.")]),
      ("0:30", "Horno", [("FAJ", "Saca la pechuga, desmenúzala y guárdala con la juliana. Apaga el horno.")]),
      ("0:40", "Robot", [("SOPA", SOPA_ROBOT2)]),
      ("0:45", "Robot", [("CREMCAL", CREMCAL_ROBOT)]),
      ("1:10", "Robot", [("CREMZAN2", CREMZAN_ROBOT)]),
      ("1:40", "Táperes", [L("Deja templar y guarda en la nevera ", [("SOPA", "la sopa"), ("FAJ", "lo de las fajitas")]),
                           L("Al congelador: ", [("FF2", "la carne de la Big Mac"), ("CREMCAL", "la crema de calabaza")]),
                           ("CREMZAN2", "Para cenar, la crema de zanahoria con la tosta de jamón y mozzarella.")]),
     ]),
   ],
   recordatorios=[
    (0, "noche", "FF2", "Pasa la carne de la Big Mac del congelador a la nevera."),
    (1, "", "FF2", "Cena: Big Mac Fit: las patatas al horno (220 °C, 15–25 minutos) y la carne, aplastada en la sartén muy caliente; la salsa, al momento."),
    (2, "", "SOPA", "Cena: calienta la sopa y haz los huevos pochados al momento (3 minutos)."),
    (2, "noche", "ARR3D", "Pasa a la nevera el arroz tres delicias (comida del jueves)."),
    (2, "noche", "CREMCAL", "Pasa a la nevera la crema de calabaza (cena del jueves)."),
    (3, "", "CREMCAL", CREMCAL_HOY),
    (3, "noche", "PASTEL", "Pasa el pastel de carne del viernes a la nevera."),
    (4, "", "SALM1", SALMON_COMPRA, "compra"),
    (5, "noche", "SEPIA", "Pasa la sepia del congelador a la nevera (guiso del domingo)."),
    (5, "noche", "ENSHUEVO", "Pasa las gambas cocidas del congelador a la nevera (ensalada de la cena del domingo)."),
    (6, "", "ENSHUEVO", "Cena: ensalada de huevo y gambas. Los 6 huevos se cuecen en la tanda de cenas del batch de hoy: pélalos y machácalos con el yogur y las mostazas; añade las gambas escurridas, el apio y la cebolla morada. Con el pan tostado."),
   ]),
 4: dict(nota_dia="Ese día comes el guiso de sepia y cenas la ensalada de huevo y gambas (los huevos se cuecen en la tanda de cenas).",
   tandas=[
    dict(nombre="Mediodía (táperes)", duracion="2 h 35 min, aproximadamente, por el estofado: a la 1 h 15 están los táperes, a la 1 h 45 el risotto y hacia las 2 h 05 coméis el guiso de sepia; luego el estofado acaba solo, a fuego suave (en ese rato cabe la tanda de cenas)",
     nevera=[[("RISOT", "Risotto de pollo, puerro y setas, 2 raciones (lunes)")], [("PULPO", "Cachelos del pulpo, cocidos y pelados (martes; el pulpo, en su envase)")],
             [("ESTOF", "Estofado de ternera, 2 raciones (miércoles)")]],
     congelador=[[("BOLO", "Macarrones a la boloñesa, 2 raciones (jueves)")], [("CERSAL", "Magro de cerdo en salsa, 2 raciones (viernes; las patatas, el jueves por la noche)")]],
     pasos=[
      ("0:00", "Preparación", [("ESTOF", ESTOF_PREP), ("CERSAL", CERSAL_PREP), ("BOLO", BOLO_VERDURA),
                               ("RISOT", "Trocea en el robot el puerro y las setas del risotto (10 s/vel 5) y corta la pechuga en dados; a la nevera hasta el final.")]),
      ("0:05", "Fuego 1 · Le Creuset", [("ESTOF", ESTOF_INICIO)]),
      ("0:05", "Fuego 3 · sartén", [("CERSAL", CERSAL_DORAR)]),
      ("0:10", "Robot", [("CERSAL", CERSAL_ROBOT)]),
      ("0:12", "Fuego 3 · sartén honda", [("BOLO", BOLO_SALSA)]),
      ("0:15", "Fuego 2 · olla", [("PULPO", CACHELOS)]),
      ("0:50", "Fuego 2 · olla", [("BOLO", BOLO_PASTA)]),
      ("1:10", "Robot", [("CERSAL", CERSAL_FIN)]),
      ("1:15", "Táperes", [(None, REPARTO), L("Nevera: ", [("PULPO", "los cachelos")]),
                           L("Congelador, en cuanto temple: ", [("BOLO", "los macarrones a la boloñesa"), ("CERSAL", "el magro en salsa")]),
                           ("ESTOF", "El estofado sigue solo, a fuego suave.")]),
      ("1:15", "Robot", [("RISOT", "Risotto del lunes (2 raciones), lo último: con la mariposa, el aceite, el jamón, el pollo, el puerro y las setas, 6 min/120 °C/vel 1/giro inverso; añade el arroz (120 g) y el caldo caliente (600 ml), 15 min/95 °C/vel 1; la mozzarella, los últimos 2 minutos.")]),
      ("1:15", "Fuego 2 · cazuela", [("SEPIA", "Guiso de sepia para comer hoy (unos 50 minutos): rehoga el ajo y la cebolla 6–8 minutos; añade la guindilla, el pimentón y el tomate, las patatas chascadas, agua hasta cubrir y sal.")]),
      ("1:25", "Fuego 3 · sartén", [("SEPIA", "Dora la sepia salpimentada a fuego fuerte 2–3 minutos y pásala a la cazuela; tapa y cuece 30 minutos a fuego medio; añade los guisantes, 10 minutos más. A comer.")]),
      ("1:45", "Táperes", [("RISOT", "Deja templar el risotto y a la nevera: es la comida de mañana.")]),
      ("2:00", "Fuego 1 · Le Creuset", [("ESTOF", ESTOF_FINAL)]),
      ("2:35", "Táperes", [("ESTOF", ESTOF_TAPER)]),
     ]),
    dict(nombre="Cenas", duracion="45 min, aproximadamente. Cabe después de comer, cuando el robot quede libre",
     nevera=[[("CREMVER", "Crema de verduras, 2 raciones, y 4 huevos cocidos con cáscara (lunes)")], [("CRI", "Solomillos del crispy en la leche, y 1 huevo cocido para su mayonesa (martes)")],
             [("ENSHUEVO", "6 huevos cocidos con cáscara para la ensalada (miércoles)")]],
     congelador=[],
     pasos=[
      ("0:00", "Fuego 2 · olla", [L("Cuece 10 minutos (en dos tandas si no caben): ", [("ENSHUEVO", "12 huevos para las dos ensaladas (los 6 de esta noche se enfrían y se pelan; los 6 del miércoles, a la nevera con cáscara)"), ("CREMVER", "4 huevos para la crema de verduras del lunes"), ("CRI", "1 huevo para la mayonesa del crispy")])]),
      ("0:05", "Encimera", [("CRI", CRI_LECHE)]),
      ("0:10", "Tabla", [("CREMVER", "Trocea el puerro, la cebolla, la zanahoria, la patata y las judías verdes de la crema de verduras.")]),
      ("0:15", "Robot", [("CREMVER", CREMVER_ROBOT)]),
      ("0:45", "Táperes", [L("Guarda en la nevera ", [("CREMVER", "la crema de verduras con sus huevos"), ("CRI", "los solomillos del crispy y su huevo"), ("ENSHUEVO", "los 6 huevos del miércoles")]),
                           ("ENSHUEVO", "Para cenar, la ensalada de huevo y gambas: machaca los 6 huevos pelados con el yogur y las mostazas y añade las gambas escurridas, el apio y la cebolla morada. Con el pan tostado.")]),
     ]),
   ],
   recordatorios=[
    (0, "", "CREMVER", "Cena: calienta la crema de verduras; dora el jamón en taquitos en una sartén sin aceite y pela los huevos cocidos."),
    (0, "noche", "CRI", CRI_MAYO),
    (1, "", "PULPO", PULPO_HOY),
    (1, "", "CRI", CRI_HOY),
    (1, "noche", "ENSHUEVO", GAMBAS_NOCHE),
    (2, "", "ENSHUEVO", ENSALADA_HOY),
    (2, "noche", "BOLO", "Pasa los macarrones a la boloñesa del jueves a la nevera."),
    (3, "", "SANDTOR", "Cena: sándwich de tortilla francesa con jamón serrano, al momento (10 minutos)."),
    (3, "noche", "CERSAL", CERSAL_JUEVES),
    (4, "", "DORSAL", "Compra las 2 doradas frescas, enteras y sin escamar, para la comida del sábado (a la sal). Si son congeladas, a la nevera la noche antes.", "compra"),
    (5, "noche", "GCAL", "Pasa el calamar del congelador a la nevera (guiso del domingo)."),
   ]),
 5: dict(nota_dia="Ese día comes el guiso de calamares y cenas la crema de zanahoria con su tosta (en la tanda de cenas).",
   tandas=[
    dict(nombre="Mediodía (táperes)", duracion="2 h 45 min, aproximadamente, por la ternera al miso: a la 1 h 15 están los táperes y hacia las 2 horas coméis el guiso de calamares; luego la ternera acaba sola, a fuego mínimo (en ese rato cabe la tanda de cenas)",
     nevera=[[("PASTAF", "Ensaladilla de pasta y jamón, 2 raciones (lunes)")], [("SOLPIQ", "Solomillo de cerdo en salsa de piquillos, 2 raciones, y sus patatas (martes)")],
             [("MISO", "Ternera al miso con su arroz y sus judías, 2 raciones (miércoles)")], [("POTG", "2 huevos duros con cáscara para el potaje (viernes)")]],
     congelador=[[("ALBON", "Albóndigas en salsa con su arroz, 2 raciones (jueves)")], [("POTG", "Potaje de garbanzos con acelgas, 2 raciones (viernes; congelado, la patata queda algo más harinosa)")]],
     pasos=[
      ("0:00", "Preparación", [("MISO", MISO_SALSA), ("ALBON", "Lava el arroz integral."), ("SOLPIQ", "Corta el solomillo de cerdo en medallones.")]),
      ("0:05", "Fuego 1 · Le Creuset", [("MISO", MISO_INICIO)]),
      ("0:05", "Robot y tabla", [("ALBON", ALBON_ROBOT),
                                 L("Luego trocea, por tandas (4–5 s/vel 5) y guardando cada cosa aparte, ", [("ALBON", "la cebolla, la zanahoria y el pimiento de la salsa de las albóndigas")]),
                                 L("A cuchillo: ", [("POTG", "las acelgas en tiras")])]),
      ("0:15", "Robot", [("SOLPIQ", SALSA_PIQUILLOS + " Pásala a un bol y lava el vaso.")]),
      ("0:15", "Fuego 2 · olla", [("ALBON", ARROZ_ALBON)]),
      ("0:15", "Fuego 3 · sartén", [("ALBON", ALBON_SALSA)]),
      ("0:20", "Airfryer", [("ALBON", ALBON_AIRFRYER)]),
      ("0:35", "Robot", [("POTG", POTAJE_ROBOT)]),
      ("0:40", "Fuego 3 · sartén", [("ALBON", ALBON_COCER)]),
      ("0:45", "Fuego 2 · cazo", [L("Cuece 10 minutos (en dos tandas si no caben): ", [("POTG", "2 huevos para el potaje (con cáscara)"), ("PASTAF", "4 para la ensaladilla (se enfrían y se pelan)"), ("ENSHUEVO", "6 para la ensalada del martes (con cáscara)")])]),
      ("0:50", "Fuego 3 · sartén", [("ALBON", "Pasa las albóndigas a sus táperes."), ("SOLPIQ", SOLOMILLO)]),
      ("0:55", "Fuego 2 · olla", [("PASTAF", PASTAF_PASTA)]),
      ("1:00", "Microondas", [("SOLPIQ", "Patatas del solomillo: 600 g en rodajas, tapadas con un poco de agua y sal, 8–10 minutos.")]),
      ("1:00", "Tabla", [("PASTAF", PASTAF_TABLA)]),
      ("1:05", "Robot", [("POTG", "Pasa el potaje a sus táperes y lava el vaso.")]),
      ("1:10", "Encimera", [("PASTAF", PASTAF_MEZCLA)]),
      ("1:15", "Táperes", [(None, REPARTO), L("Nevera: ", [("PASTAF", "la ensaladilla"), ("SOLPIQ", "el solomillo de cerdo con sus patatas"), ("POTG", "los 2 huevos del potaje"), ("ENSHUEVO", "los 6 huevos de la ensalada")]),
                           L("Congelador: ", [("ALBON", "las albóndigas con su arroz"), ("POTG", "el potaje")]), ("MISO", "La ternera al miso sigue sola, a fuego mínimo.")]),
      ("1:15", "Fuego 2 · olla a presión", [("GCAL", "Guiso de calamares para comer hoy (unos 35 minutos): rehoga el ajo, la cebolleta y el pimiento verde 8–10 minutos; añade el calamar, 2–3 minutos, el choricero y la guindilla; la patata chascada y agua hasta cubrir justo; cierra y cuece 5 minutos desde que suba la válvula. Deja que baje la presión sola.")]),
      ("1:50", "Fuego 3 · sartén", [("GCAL", "Dora los ajos frescos 3–4 minutos y a comer el guiso de calamares, con los ajos por encima.")]),
      ("2:20", "Fuego 2 · olla", [("MISO", MISO_ARROZ)]),
      ("2:35", "Fuego 1 · Le Creuset", [("MISO", MISO_FINAL)]),
      ("2:45", "Táperes", [("MISO", "Deja templar la ternera al miso con su arroz y sus judías y a la nevera: es la comida del miércoles.")]),
     ]),
    dict(nombre="Cenas", duracion="1 h 15 min, aproximadamente, casi todo de robot (la sopa y la crema de zanahoria de la cena de hoy). Empiézala cuando el robot quede libre, hacia la 1 h 10 de la tanda de mediodía",
     nevera=[[("SOPAV", "Sopa casera de pollo y verduras, 2 raciones (lunes)")]],
     congelador=[[("CASTA", "Pechuga cruda de la crema de boniato del domingo (360 g), en bolsa")]],
     pasos=[
      ("0:00", "Tabla", [("SOPAV", "Lava, pela y corta en trozos grandes la zanahoria, la cebolla, el pimiento, el puerro, el tomate y la patata de la sopa."),
                         ("CASTA", "La pechuga de la crema de boniato del domingo (360 g), cruda, en una bolsa al congelador."),
                         ("CREMZAN2", "Trocea la zanahoria, la patata, el puerro y la cebolla de la crema de zanahoria.")]),
      ("0:05", "Robot", [("SOPAV", SOPAV_ROBOT)]),
      ("0:45", "Robot", [("CREMZAN2", CREMZAN_ROBOT)]),
      ("1:15", "Táperes", [L("Guarda en la nevera ", [("SOPAV", "la sopa")]), ("CREMZAN2", "Para cenar, la crema de zanahoria con la tosta de jamón y mozzarella.")]),
     ]),
   ],
   recordatorios=[
    (0, "", "SOPAV", "Cena: calienta la sopa casera de pollo y verduras; con el pan."),
    (0, "noche", "ENSHUEVO", GAMBAS_NOCHE),
    (1, "", "ENSHUEVO", ENSALADA_HOY),
    (2, "", "CENAC", "Cena: avena con leche y cacao, al momento (2–3 minutos)."),
    (2, "noche", "ALBON", "Pasa las albóndigas del jueves a la nevera."),
    (3, "", "SANDMIX", "Cena: sándwich mixto, al momento (5–10 minutos)."),
    (3, "noche", "POTG", "Pasa el potaje del viernes a la nevera."),
    (4, "noche", "FISHCHIPS", "Pasa la merluza a la nevera y haz la tártara (fish & chips del sábado)."),
    (5, "noche", "ARRGAMB", "Pasa los gambones del congelador a la nevera (arroz del domingo)."),
    (5, "noche", "CASTA", "Pasa a la nevera la pechuga de la crema de boniato (cena del domingo)."),
   ]),
}


def tandas(b):
    """Las tandas de un batch: desde la semana 8, comidas (táperes) y cenas por separado; antes, una sola."""
    if "tandas" in b: return b["tandas"]
    return [dict(nombre="Batch cooking", duracion=b["duracion"], nevera=b["nevera"], congelador=b["congelador"], pasos=b["pasos"])]


DIAS_SEM = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
MES_LARGO = ["", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def _enumera(xs):
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " y " + xs[-1]


def _trozos(x, presentes):
    """Texto de un paso o de una línea del ciclo: una cadena, o trozos (plato, texto) de los que solo quedan los de los
       platos que se cocinan esa semana (plato None = siempre). Un trozo L(...) enumera lo que quede: «Nevera: a, b y c.»"""
    if x is None or isinstance(x, str): return x
    out = []
    for t in x:
        if isinstance(t, dict):
            items = [txt for plato, txt in t["lista"] if plato is None or plato in presentes]
            if items: out.append(t["antes"] + _enumera(items) + t["despues"])
        elif t[0] is None or t[0] in presentes:
            out.append(t[1])
    return " ".join(out)


def instanciar(tpl, lunes, presentes, avisos=(), cerrado=()):
    """Batch de una semana del ciclo con sus fechas. `lunes` es el lunes del menú; `presentes`, los platos que se cocinan
       (los de la semana y los del domingo del batch): si un festivo deja libre una comida o una cena, los trozos de ese
       plato se caen solos. `avisos` son recordatorios de festivos [(fecha, texto)] y `cerrado`, los días sin tiendas:
       las compras de ese día pasan a la víspera."""
    from datetime import timedelta
    dom = lunes - timedelta(days=1)
    out = dict(dia=f"Domingo {dom.day} de {MES_LARGO[dom.month]}", nota_dia=_trozos(tpl.get("nota_dia"), presentes), tandas=[])
    for t in tpl["tandas"]:
        pasos = [(h, donde, _trozos(x, presentes)) for h, donde, x in t["pasos"]]
        out["tandas"].append(dict(nombre=t["nombre"], duracion=_trozos(t["duracion"], presentes),
                                  nevera=[x for x in (_trozos(x, presentes) for x in t["nevera"]) if x],
                                  congelador=[x for x in (_trozos(x, presentes) for x in t["congelador"]) if x],
                                  pasos=[x for x in pasos if x[2]]))
    rec = []
    for dia, momento, plato, txt, *tipo in tpl["recordatorios"]:
        if plato is not None and plato not in presentes: continue
        txt = _trozos(txt, presentes)
        if not txt: continue
        f = lunes + timedelta(days=dia)
        if tipo and tipo[0] == "compra" and f in cerrado:
            f -= timedelta(days=1); txt = txt.rstrip(".") + " (mañana cierran las tiendas)."
        rec.append((f, momento, txt))
    rec += [(f, "", txt) for f, txt in avisos]
    orden = {"mañana": 0, "": 1, "noche": 2}
    rec.sort(key=lambda r: (r[0], orden[r[1]]))
    etiqueta = lambda f, m: f"{DIAS_SEM[f.weekday()]} {f.day}" + (" por la noche" if m == "noche" else " por la mañana" if m == "mañana" else "")
    out["recordatorios"] = [(etiqueta(f, m), txt) for f, m, txt in rec]
    return out


def comprobar_fuegos(batches=None, desde=8):
    """Desde la semana 8 (23 de noviembre): en los fuegos, como mucho 2 ollas y 1 sartén a la vez. En los pasos, los fuegos 1 y 2
       son de las ollas (olla, olla a presión, Le Creuset, cazo o cazuela) y el 3, de la sartén, un cacharro detrás de otro en cada fuego.
       El estofado, nunca en la olla a presión. Tampoco puede haber dos pasos a la misma hora en el mismo fuego."""
    import re
    errores = []
    for n, b in (batches or BATCH).items():
        if n < desde: continue
        for t in tandas(b):
            vistos = set()
            for hora, donde, txt in t["pasos"]:
                if "presión" in donde and "estofado" in txt.lower():
                    errores.append(f"Batch {n}, {hora}: el estofado va a fuego suave en la Le Creuset, no en la olla a presión")
                if not donde.startswith("Fuego"): continue
                m = re.fullmatch(r"Fuego ([123])(?: · (.+))?", donde)
                if not m:
                    errores.append(f"Batch {n} ({t['nombre']}), {hora}: «{donde}»: falta el número de fuego (1, 2 o 3)"); continue
                if m.group(2) and (m.group(1) == "3") != m.group(2).startswith("sartén"):
                    errores.append(f"Batch {n} ({t['nombre']}), {hora}: «{donde}»: los fuegos 1 y 2 son de las ollas y el 3, de la sartén")
                if (hora, m.group(1)) in vistos:
                    errores.append(f"Batch {n} ({t['nombre']}), {hora}: dos pasos a la vez en el fuego {m.group(1)}")
                vistos.add((hora, m.group(1)))
    return errores
