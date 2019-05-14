from VALID import OK, OKI, ns
import numpy as np
import subprocess

def crea_matriz(fil,col):
    f=-1;c=-1
    e_fil=[]

    for f in range(0,fil):
        e_col=[]
        f+=1
        for c in range(0,col):
            c+=1
            valor = OK(input(f'introdusca el componente ({f},{c})'))
            e_col.append(valor)
        efil.append(e_col)
    return e_fil

def OKI(n):
    try:
        n= int(n)
    except:
        n = OKI(input("Caracter no valido"))
    return n





