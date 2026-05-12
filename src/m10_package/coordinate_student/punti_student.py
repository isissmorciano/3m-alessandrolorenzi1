# Parte 2: Implementazione di coordinate/punti.py
# Funzioni per gestire i punti (rappresentati come dizionari):

# crea_punto(x: float, y: float) -> dict:
# Restituisce un dizionario con chiavi: x, y
# distanza_tra_punti(p1: dict, p2: dict) -> float:
# Calcola la distanza euclidea tra due punti
# Formula: √((x2-x1)² + (y2-y1)²)
# info_punto(punto: dict) -> str:
# Restituisce formato: "(x, y)"
# Esempio: "(3.5, 2.0)"

import math

def crea_punto(x: float, y: float) -> dict:
    return {"X": x,
                "Y": y}

def distanza_tra_punti(p1: dict, p2: dict) -> float:
    num = (p2["X"] - p1["X"])**2 + (p2["Y"] - p1["Y"])**2
    return math.sqrt(num)

def info_punto(punto: dict) -> str:
    return (f"({punto['X']}, {punto['Y']})")