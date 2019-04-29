import numpy as np

def listar()
    path = '.mascotas.csv'
    arreglo_mascotas = np.genfromtxt(path,delimiter=',',dtype='str')
    print(arreglo_mascotas)
listar()
input('fin???')