# Generador de los menús (semanas 3 a 6)

Programa en Python que genera, a partir de las recetas y del plan semanal, todo lo de las semanas 3 a 6:

- los menús (`menus/semana_03..06.md`) y las listas de la compra (`listas_compra/lista_semana_03..06.md`);
- `recetas/recetas_videos_internet.md`, `recetas/recetas_robot_cecotec.md` y `recetas/batch_cooking.md`;
- la página del mes (el artifact que ve Indi en el móvil);
- el HTML de los Google Docs de cada semana (lista de la compra, y menú con las recetas).

No edites a mano esos ficheros del repositorio: cambia el generador y vuelve a generarlos.

## Cómo se usa

Desde esta carpeta:

```bash
python3 plan.py          # kcal y proteína de cada día, y la comprobación de pescados
python3 gen_md.py        # escribe los .md del repositorio
python3 gen_page.py      # página del mes en salida/menu_noviembre.html
python3 gen_docs.py 5    # HTML de los Google Docs de la semana 5 en salida/docs/
```

`salida/` no se sube al repositorio.

## Dónde está cada cosa

- `recetas_*.py`: las recetas, con las cantidades **por persona** (`{n}` y `{n|singular|plural}` se multiplican por 2 al escribirlas).
- `nutri.py`: tabla nutricional (por 100 g). `shop.py`: cómo sale cada ingrediente en la lista de la compra.
- `plan.py`: qué se come cada día (`SEMANAS`), los cambios respecto a cada fuente (`CAMBIOS`) y las notas de la compra (`NOTA_COMPRA`).
- `batch.py`: el batch cooking de cada domingo y los recordatorios de cada noche.
- `plantilla.html`: la página del mes.

## Normas del plan

- Las recetas son para 2 personas: los dos coméis lo mismo.
- Días de entreno, unas 1950 kcal; días de descanso, unas 1600 (±120 kcal).
- Nunca pollo en la comida y en la cena del mismo día.
- Ni atún (tampoco bonito) ni calabacín. Merluza siempre rebozada. Solomillos de pollo en vez de contramuslos.
- El pescado y el marisco se cocinan el día que se comen; en el batch solo se deja la base o la salsa.
- Nunca merluza y bacalao en la misma semana, ni el mismo pescado o marisco dos semanas seguidas (`python3 plan.py` lo comprueba).
- Comidas de lunes a viernes en táper, hechas el domingo, con un solo robot (la Mambo de Cecotec) y 3 fuegos.
