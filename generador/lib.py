"""Utilidades: texto de ingredientes con plantillas {n} / {n|singular|plural}, macros y lista de la compra."""
import re
from collections import defaultdict
from nutri import T

TOKEN = re.compile(r"\{([\d./]+)(?:\|([^|}]+)\|([^}]+))?\}")

def _num(s):
    if "/" in s:
        a, b = s.split("/"); return float(a) / float(b)
    return float(s)

def fmt(v):
    r = round(v)
    if abs(v - r) < 0.02: return str(r)
    whole, frac = int(v), v - int(v)
    for f, s in [(1/4, "1/4"), (1/3, "1/3"), (1/2, "1/2"), (2/3, "2/3"), (3/4, "3/4")]:
        if abs(frac - f) < 0.02: return f"{whole} y {s}" if whole else s
    return f"{round(v, 1)}".replace(".", ",")

def texto(t, k=1):
    """Plantilla -> texto con las cantidades multiplicadas por k."""
    def sub(m):
        v = _num(m.group(1)) * k; s = fmt(v)
        return f"{s} {m.group(3) if v > 1.001 else m.group(2)}" if m.group(2) else s
    return TOKEN.sub(sub, t)

def items_receta(r):
    """[(clave, cantidad)] de una receta (solo los que cuentan para macros/compra)."""
    out = []
    for _, lista in r["grupos"]:
        for clave, q, _t in lista:
            if clave and not clave.startswith("x:"):
                out.append((clave, q))
    return out

def macros_receta(r):
    k = p = g = h = 0.0
    for clave, q in items_receta(r):
        a = T[clave]["n"]; f = q / 100
        k += a[0] * f; p += a[1] * f; g += a[2] * f; h += a[3] * f
    return k, p, g, h

def extras_receta(r):
    """Ingredientes de despensa sin macros ('x:Nombre')."""
    return [c[2:] for _, lista in r["grupos"] for c, _q, _t in lista if c and c.startswith("x:")]
