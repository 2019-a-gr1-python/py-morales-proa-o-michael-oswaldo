import numpy as np
import sys
import csv

def listar():
    path = './mascotas.csv'
    arreglo_mascotas = np.genfromtxt(path, delimiter=',', dtype='str')
    print('**********************************************************\n')
    print('***************      MASCOTAS          *******************\n')
    print('**********************************************************\n')
    print('Código         |     Tipo          |         Nombre         ')
    print('__________________________________________________________')
    for a in arreglo_mascotas:
        print(f'{a[2]}                   {a[0]}                       {a[1]}')


def crear():
    codigo = input('Ingrese el codigo de la nueva mascota:\n')
    tipo = input('Tngrese el tipo de la nueva mascota:\n')
    nombre = input('Ingrese el nombre de la nueva mascota:\n')
    path = './mascotas.csv'

    archivo_escritura_abierto = open(path, mode='a')
    archivo_escritura_abierto.writelines([f'\n{tipo},{nombre},{codigo}'])
    print('Mascota Creada!!!')

def borrar():
    codigo = input('Ingrese el codigo de la mascota a borrar:\n')
    path = './mascotas.csv'
    archivo_escritura_abierto = open(path, mode='r')
    lineas = archivo_escritura_abierto.readlines()
    print(lineas)
    print(type(lineas))
    splited = []
    i = 0
    for a in lineas:
        i=i+1
        splited = a.split(',')
        if splited[2].rstrip('\n')== codigo :
            print(splited)
            print(type(splited))
            lineas.pop(i-1)
    archivo_escritura_abierto.close()
    print(lineas)
    archivo_escritura_abierto2 = open(path,mode='w')
    archivo_escritura_abierto2.writelines(lineas)
       # if lineas[i-1]!='':
        #    if splited[2]==codigo:
         #       lineas[i-1]=''
def editar():
    codigo = input('Ingrese el codigo de la mascota a editar:\n')
    tipo = input('Ingrese el tipo de la mascota a editar:\n')
    nombre = input('Ingrese el nombre de la mascota a editar:\n')
    path = './mascotas.csv'
    archivo_escritura_abierto = open(path, mode='r')
    lineas = archivo_escritura_abierto.readlines()

    splited = []
    i = 0
    for a in lineas:
        i = i + 1
        splited = a.split(',')
        if splited[2].rstrip('\n') == codigo:
            lineas[i-1] =f'{tipo},{nombre},{codigo}\n'
    archivo_escritura_abierto.close()
    print(lineas)
    archivo_escritura_abierto2 = open(path, mode='w')
    archivo_escritura_abierto2.writelines(lineas)


def salir():
    sys.exit()


def adoptar():
    print('se supone codigo adoptar')


def crud():
    volver = 0
    while volver == 0:
        print('\nBienvenido Administrador!')
        print('1. Listar Mascotas')
        print('2. Crear Mascota')
        print('3. Borrar Mascota')
        print('4. Editar Mascota')
        print('5. Salir ')
        accion = input('Que desea Hacer: \n')

        if accion == '1':
            listar()
        if accion == '2':
            crear()
        if accion == '3':
            borrar()
        if accion == '4':
            editar()
        if accion == '5':
            salir()
            volver = 1


def validar(usuario, password):
    path = './usuarios.csv'
    arreglo_usuarios = np.genfromtxt(path, delimiter=',', dtype='str')
    credential_bolean = False;

    for a in arreglo_usuarios:
        if a[0] == usuario and a[1] == password:
            credential_bolean = True
    return credential_bolean


def adoptar_mascota():
    print('Bienvenido!!\n')
    print('1. Ver Mascotas ')
    print('2. Adoptar una Mascota')
    print('3. Salir')
    accion = input('Que desea hacer: \n')
    if accion == '1':
        listar()
    if accion == '2':
        listar()
        adoptar()
    if accion == '3':
        salir()


def main():
    print('\n\n***********************************************')

    print('*********Bienvenido a  "MyPet Store"***********')
    print('***********************************************')
    usuario = input('ingresa tu Nombre de Usuario :\n')
    password = input('Ingresa tu contraseña:\n')
    existe = validar(usuario, password)
    if existe:
        if usuario == 'admin':
            crud()
        else:
            adoptar_mascota()
    else:
        print('Credenciales Incorrectas')
        sys.exit()


main()
