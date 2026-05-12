# Parte 4: Utilizzo del package in es62_reference.py
# Importa il package: from coordinate import punti, linee
# Crea almeno 3 punti
# Crea 2-3 linee dai punti
# Calcola lunghezze e punti medi
# Stampa risultati formattati


from coordinate_student import punti_student, linee_student


def main()->None:
    p1 = punti_student.crea_punto(1.0, 2.0)
    p2 = punti_student.crea_punto(4.0, 6.0)
    p3 = punti_student.crea_punto(5.0, 3.0)

    linea1 = linee_student.crea_linea(p1, p2)
    linea2 = linee_student.crea_linea(p2, p3)

    lunghezza1 = linee_student.lunghezza_linea(linea1)
    lunghezza2 = linee_student.lunghezza_linea(linea2)

    punto_medio1 = linee_student.punto_medio(linea1)
    punto_medio2 = linee_student.punto_medio(linea2)

    print(f"\nLunghezza Linea 1: {lunghezza1:.2f}")
    print(f"\nLunghezza Linea 2: {lunghezza2:.2f}")
    print(f"\nPunto Medio Linea 1: {punto_medio1}")
    print(f"\nPunto Medio Linea 2: {punto_medio2}")
    print(f"\nInfo Linea 1: {linee_student.info_linea(linea1)}")
    print(f"\nInfo Linea 2: {linee_student.info_linea(linea2)}")
    
    

if __name__ == "__main__":
    main()




