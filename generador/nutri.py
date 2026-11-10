"""Tabla nutricional (por 100 g o 100 ml; en crudo/seco) -> kcal, proteína, grasa, hidratos disponibles.
   Valores medios de etiquetas españolas/BEDCA/USDA. 'ud' = gramos por unidad cuando se compra por piezas."""
T = {
 # Proteínas
 "pechuga":      dict(n=(110, 23.0, 1.5, 0.0)),
 "solomillo":    dict(n=(105, 23.5, 1.2, 0.0)),
 "pavo":         dict(n=(105, 24.0, 1.0, 0.0)),
 "ternera":      dict(n=(125, 21.0, 4.5, 0.0)),
 "merluza":      dict(n=(75, 17.0, 0.8, 0.0)),
 "bacalao":      dict(n=(78, 18.0, 0.6, 0.0)),
 "gambas":       dict(n=(90, 20.0, 1.0, 0.0)),
 "gambones":     dict(n=(45, 10.0, 0.5, 0.0)),   # enteros y crudos, con cabeza y cáscara (≈50 % comestible)
 "calamar":      dict(n=(92, 15.6, 1.4, 3.1)),   # limpio, crudo (USDA)
 "atun":         dict(n=(105, 24.0, 1.0, 0.0)),
 "tofu":         dict(n=(110, 11.1, 6.5, 1.0)),   # tofu firme Hacendado (OFF)
 "huevo":        dict(n=(143, 12.6, 9.5, 0.7), ud=55),
 "clara":        dict(n=(52, 10.9, 0.2, 0.7)),
 "lentejas":     dict(n=(330, 24.0, 1.1, 50.0)),
 "garbanzos":    dict(n=(120, 7.0, 2.2, 15.0)),   # cocidos de bote, escurridos
 # Lácteos
 "yogur":        dict(n=(60, 3.8, 3.0, 4.6), ud=125),
 "yogur_prot":   dict(n=(52, 10.0, 0.2, 3.5), ud=120),   # +Proteínas 0% natural Hacendado (4 x 120 g)
 "mozzarella":   dict(n=(250, 18.0, 19.0, 1.0)),
 "mozza_light":  dict(n=(153, 17.0, 9.0, 1.5), ud=125),  # mozzarella fresca light Hacendado (bola 125 g)
 "leche":        dict(n=(46, 3.2, 1.6, 4.7)),
 "natillas":     dict(n=(81, 8.4, 1.1, 8.7), ud=120),  # +Proteínas Hacendado (OFF: 97 kcal y 10,1 g prot. por 120 g)
 "cottage":      dict(n=(95, 11.0, 4.5, 3.0)),
 # Hidratos
 "arroz_int":    dict(n=(350, 7.5, 2.7, 72.0)),
 "arroz":        dict(n=(350, 7.0, 0.6, 78.0)),
 "pasta_int":    dict(n=(350, 13.0, 2.5, 64.0)),
 "cuscus":       dict(n=(360, 12.0, 1.5, 72.0)),
 "patata":       dict(n=(77, 2.0, 0.1, 15.5)),
 "boniato":      dict(n=(86, 1.6, 0.1, 18.0)),
 "pan_int":      dict(n=(250, 10.0, 3.5, 41.0)),
 "pita":         dict(n=(260, 8.5, 1.2, 52.0), ud=60),
 "wrap_int":     dict(n=(300, 9.0, 7.0, 48.0), ud=60),
 "pan_cristal":  dict(n=(265, 8.5, 4.0, 48.0), ud=70),
 "pan_burger":   dict(n=(267, 10.7, 6.0, 40.0), ud=75),
 "avena":        dict(n=(372, 13.5, 7.0, 59.0)),
 "copos_maiz":   dict(n=(370, 7.5, 1.0, 81.0)),
 "harina":       dict(n=(350, 10.0, 1.0, 72.0)),
 # Verduras
 "tomate":       dict(n=(18, 0.9, 0.2, 3.5)),
 "tomate_trit":  dict(n=(25, 1.2, 0.2, 4.0)),
 "cebolla":      dict(n=(40, 1.1, 0.1, 7.6)),
 "pimiento":     dict(n=(30, 1.0, 0.3, 4.5)),
 "pim_verde":    dict(n=(20, 0.9, 0.2, 2.9)),
 "calabacin":    dict(n=(17, 1.2, 0.3, 2.2)),
 "zanahoria":    dict(n=(41, 0.9, 0.2, 6.8)),
 "berenjena":    dict(n=(25, 1.0, 0.2, 3.0)),
 "calabaza":     dict(n=(26, 1.0, 0.1, 5.5)),
 "puerro":       dict(n=(61, 1.5, 0.3, 12.0)),
 "apio":         dict(n=(16, 0.7, 0.2, 1.4)),
 "guisantes":    dict(n=(81, 5.4, 0.4, 9.5)),
 "acelgas":      dict(n=(19, 1.8, 0.2, 2.0)),
 "hojas":        dict(n=(25, 2.6, 0.7, 2.0)),   # rúcula / canónigos
 "remolacha":    dict(n=(43, 1.6, 0.2, 7.0)),
 "aguacate":     dict(n=(160, 2.0, 14.7, 1.8)),
 "pim_asados":   dict(n=(30, 1.0, 0.3, 5.0)),
 "maiz":         dict(n=(90, 3.0, 1.5, 15.0)),
 # Fruta
 "platano":      dict(n=(89, 1.1, 0.3, 20.0), ud=120),
 "kiwi":         dict(n=(61, 1.1, 0.5, 11.7), ud=100),
 "arandanos":    dict(n=(57, 0.7, 0.3, 12.0)),
 "granada":      dict(n=(83, 1.7, 1.2, 14.0)),
 "limon":        dict(n=(29, 1.1, 0.3, 6.0)),
 # Otros
 "aove":         dict(n=(820, 0.0, 91.0, 0.0)),   # por 100 ml
 "pipas":        dict(n=(560, 30.0, 49.0, 5.0)),
 "cacao":        dict(n=(360, 22.0, 11.0, 15.0)),
 "soja":         dict(n=(60, 6.0, 0.0, 8.0)),
 "mostaza":      dict(n=(66, 4.0, 4.0, 5.0)),
 "ketchup0":     dict(n=(30, 1.0, 0.1, 5.0)),
 "guindilla":    dict(n=(25, 0.8, 0.2, 4.0)),
 "caldo":        dict(n=(5, 0.3, 0.1, 0.5)),
 "especias":     dict(n=(0, 0, 0, 0)),
 # Añadidos para las recetas nuevas
 "tortilla_int": dict(n=(269, 8.5, 5.5, 42.0), ud=36),   # tortillas 100% integrales Hacendado (OFF: 36 g/ud)
 "bbq0":         dict(n=(60, 1.0, 0.2, 10.0)),           # salsa barbacoa sin azúcar Hacendado (aprox.)
 "balsamico":    dict(n=(88, 0.5, 0.0, 17.0)),
 "jamon_serrano":dict(n=(240, 30.0, 13.0, 0.5)),
 "jamon_cocido": dict(n=(105, 19.0, 3.0, 1.0)),
 "pan_pueblo":   dict(n=(260, 9.0, 1.5, 52.0)),
 "aceitunas":    dict(n=(145, 1.0, 15.0, 1.0)),
 "piadina":      dict(n=(320, 8.5, 9.0, 50.0), ud=100),
 "atun_fresco":  dict(n=(110, 24.0, 1.0, 0.0)),   # tacos de atún congelados
 "pavo_fiambre": dict(n=(100, 20.0, 1.5, 1.5)),
 "tortilla_maiz":dict(n=(227, 5.5, 3.0, 43.0), ud=26),   # tortillas de maíz Hacendado (59 kcal/ud)
 "pina":         dict(n=(50, 0.5, 0.1, 11.8)),
 "alcaparras":   dict(n=(23, 2.4, 0.9, 2.0)),
 "choricero":    dict(n=(38, 1.5, 0.5, 6.0)),   # carne de pimiento choricero
 # Recetas del robot Cecotec
 "ternera_pieza":dict(n=(120, 21.5, 3.8, 0.0)),  # redondo, tapa o contra
 "ternera_guiso":dict(n=(135, 20.5, 5.5, 0.0)),  # morcillo, aguja o llana
 "setas":        dict(n=(33, 3.3, 0.4, 4.0)),    # setas de cardo / ostra (USDA)
 "judias_verdes":dict(n=(25, 1.8, 0.2, 3.6)),
 "tomate_conc":  dict(n=(82, 4.3, 0.5, 13.0)),
 "caldo_pollo":  dict(n=(5, 0.3, 0.1, 0.5)),
 "caldo_verd":   dict(n=(5, 0.3, 0.1, 0.5)),
 "picada_mixta": dict(n=(132, 21.0, 5.2, 0.0)),  # mitad ternera magra, mitad lomo de cerdo
}

def macros(items):
    """items: lista de (clave, cantidad en g/ml) -> (kcal, P, G, HC)"""
    k = p = g = h = 0.0
    for clave, q in items:
        a = T[clave]["n"]; f = q / 100
        k += a[0] * f; p += a[1] * f; g += a[2] * f; h += a[3] * f
    return round(k), round(p, 1), round(g, 1), round(h, 1)
