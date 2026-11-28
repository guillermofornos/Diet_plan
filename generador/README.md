# Generador de los menús (semanas 3 a 10)

Programa en Python que genera, a partir de las recetas y del plan semanal, todo lo de las semanas 3 a 10 (26 oct – 20 dic):

- los menús (`menus/semana_03..10.md`) y las listas de la compra (`listas_compra/lista_semana_03..10.md`);
- `recetas/recetas_videos_internet.md`, `recetas/recetas_robot_cecotec.md` y `recetas/batch_cooking.md`;
- la página del mes (el artifact que ve Indi en el móvil);
- el HTML de los Google Docs de cada semana (lista de la compra, y menú con las recetas).

No edites a mano esos ficheros del repositorio: cambia el generador y vuelve a generarlos.

## Cómo se usa

Desde esta carpeta:

```bash
python3 plan.py          # kcal y proteína de cada día, y la comprobación de pescados
python3 gen_md.py        # escribe los .md del repositorio
python3 gen_page.py      # página del mes en salida/menu_mes.html (semanas de PAGINA, en gen_page.py)
python3 gen_docs.py 5    # HTML de los Google Docs de la semana 5 en salida/docs/
```

`salida/` no se sube al repositorio.

## Dónde está cada cosa

- `recetas_*.py`: las recetas, con las cantidades **por persona** (`{n}` y `{n|singular|plural}` se multiplican por 2 al escribirlas).
- `nutri.py`: tabla nutricional (por 100 g). `shop.py`: cómo sale cada ingrediente en la lista de la compra.
- `plan.py`: qué se come cada día (`SEMANAS`: hasta la 8, escritas a mano; desde la 9, sacadas de `CICLO`), los cambios respecto a cada fuente (`CAMBIOS`) y las notas de la compra (`NOTA_COMPRA`).
- `batch.py`: el batch cooking de cada domingo y los recordatorios de cada noche (hasta la semana 8, uno por semana; desde la 9, uno por semana del ciclo, con las fechas puestas al generar).
- `plantilla.html`: la página del mes.

## Normas del plan

- Las recetas son para 2 personas: los dos coméis lo mismo.
- Días de entreno, unas 1950 kcal; días de descanso, unas 1600 (±120 kcal).
- Nunca pollo en la comida y en la cena del mismo día.
- Ni atún (tampoco bonito) ni calabacín. Merluza siempre rebozada. Solomillos de pollo en vez de contramuslos.
- El pescado y el marisco se cocinan el día que se comen; en el batch solo se deja la base o la salsa.
- Nunca merluza y bacalao en la misma semana, y entre una y otra, al menos una semana sin ninguna de las dos.
- Nunca el mismo pescado o marisco dos semanas seguidas, ni la misma comida o cena dos semanas seguidas (desde la semana 6).
- Desde la semana 8 (norma del 28 de noviembre, cuando salieron lentejas tres semanas seguidas con recetas distintas), tampoco otro plato del mismo tipo: entre unas lentejas y las siguientes, sean de la receta que sean, una semana de por medio, y lo mismo con los garbanzos y con los guisos de ternera (estofado, carne guisada o jardinera). Los tipos están en `FAMILIAS` (`plan.py`): si dos platos te parecen el mismo, se añaden ahí.
- **Ciclo de 5 semanas** (28 de noviembre): desde la semana 9 (lunes 7 de diciembre) el menú son 5 semanas que se repiten (`CICLO` en `plan.py`; los batches, en `CICLO_BATCH` de `batch.py`). Las normas de no repetir valen también de la semana 5 a la 1 (`comprobar_ciclo`). Para generar más semanas, se sube `ULTIMA_SEMANA`: la 14 vuelve a ser la 1 del ciclo. Los festivos (`FESTIVOS`) dejan libre una comida o una cena, y lo de ese plato desaparece solo del batch, de los avisos y de la compra.
- Como mucho 2 platos con pollo a la semana, contando comidas y cenas y cualquier plato que lo lleve, también sopas, cremas y arroces (`comprobar_pollo`, desde la semana 9).
- En cada vuelta del ciclo (antes, cada mes): salmón 2 semanas, una dorada a la sal y una lubina a la sal, sin quitar guisos ni marmitakos para meterlos, y el arroz meloso con secreto ibérico en la Le Creuset.
- Ningún plato, ni otro del mismo tipo, se repite dentro de la misma semana: las lentejas, un solo día (desde la semana 7).
- Cenas ligeras (desde la semana 8): cremas, sándwiches, tortilla o tomates rellenos. Kebab, fajitas, tacos, pizza o hamburguesa, el día que la comida es de legumbre (o, como mucho, una vez suelta a la semana). El pescado, nunca de cena: va a las comidas del fin de semana, que es cuando se puede hacer en el momento.
- Las recetas que pasa Guillermo (`PROPIAS` en `plan.py`) se apuntan como suyas y tienen prioridad sobre las demás: todas entran en el ciclo (las que no, en `PROPIAS_FUERA`, con el motivo) y, para hacer sitio a un plato o resolver un choque de normas, sale uno que no sea suyo. Las comidas de `recetas_ciclo.py` las buscó Claude para llegar a 2 platos de pollo por semana: no son suyas.
- Cada semana, una cena es la ensalada cremosa de huevo y gambas (25 de noviembre; `SEMANALES` en `plan.py`): no cuenta en la norma de no repetir ni en la rotación de pescado.
- Los meses se cuentan en bloques de 4 semanas desde la 8 (30 de noviembre).
- Guillermo come el 60 % de la comida y la cena (Indi, el 40 %) y desayuna solo los días de gimnasio. Su plan (kcal por tipo de día, proteína y suplementos) está en `yo.py`, sale en la pestaña «Tú» de la página y en `PLAN_PERSONAL.md`.
- Nada de pavo, ni en comidas ni en cenas, y los guisantes con jamón no cuentan como plato principal.
- El estofado de ternera (tu receta del 22 de noviembre) es el guiso de carne habitual: dos veces en cada vuelta del ciclo (semanas 1 y 4), a fuego suave en la Le Creuset (nunca en la olla a presión).
- `python3 plan.py` comprueba las normas de pescado, de repetición, de pollo y del ciclo, y las de los fuegos del batch (`comprobar_fuegos` en `batch.py`).
- Comidas de lunes a viernes en táper, hechas el domingo, con un solo robot (la Mambo de Cecotec). En los fuegos, como mucho 2 ollas y 1 sartén a la vez (en los pasos, fuegos 1 y 2 para las ollas y 3 para la sartén); el horno y la airfryer, en paralelo.
