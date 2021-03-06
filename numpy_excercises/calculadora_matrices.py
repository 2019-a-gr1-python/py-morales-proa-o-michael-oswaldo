from validar import OK, OKI
import numpy as np


def val(tipo):
    while tipo != "N" and tipo != "M":
        tipo = input("Introduzca \'N\' para dato numérico y \'M\' para matriz: ")
    return tipo


def dato():

    tipo_dato = val(input("Tipo de dato: "))
    if tipo_dato == "M":
        matr = crea_matriz(fil, col)
    else:
        matr = OK(input("Introduce número: "))
    return matr


def crea_matriz(fil, col):
    f = -1;
    c = -1
    e_fil = []
    for f in range(fil):
        e_col = []
        f += 1
        for c in range(col):
            c += 1
            valor = OK(input(f'Introduzca el valor del campo [{f},{c}]: '))
            e_col.append(valor)
        e_fil.append(e_col)
        matri = np.array(e_fil, float)
    return matri

n = True
while n:
    print("         CALCULADORA DE MATRICES          ")
    print("""
*******************************************
SUMA                            "+"
RESTA                           "-"
MULTIPLICACION                  "*"
VER RESULTADO                   "="
*******************************************
*******************************************""")

    fil = OKI(input("Indique número de filas: "))
    col = OKI(input("Indique número de columnas: "))
    e = fil
    f = -1;
    c = -1
    acum = dato()
    print(acum)
    while True:
        oper = input("Introduzca operador: ")
        while oper != "+" and oper != "-" and oper != "*" and oper != "=":
            oper = input("Introduzca un operador válido: ")
        if oper == "+":
            matr = dato()
            acum = acum + matr
        elif oper == "-":
            matr = dato()
            acum = acum - matr
        elif oper == "*":
            tipo_dato = val(input("Tipo de dato: "))
            if tipo_dato == "M":
                fil = col
                col = OKI(input("Introduce número de columnas: "))
                matr = crea_matriz(fil, col)
                acum = np.dot(acum, matr)
                fil = e
            else:
                matr = OK(input("Introduce número: "))
                acum = acum * matr
        elif oper == "=":
            print("")
            print("MATRIZ RESULTADO")
            print(acum)
            print("")
            break
        print(matr)
    responde = input("""[0]. Salir[Any]. Seguir Calculando""" )
    if responde == "0":
        n = False





