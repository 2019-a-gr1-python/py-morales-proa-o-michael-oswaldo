import numpy as np
import sys
def listar():
    path = './mascotas.csv'
    arreglo_mascotas = np.genfromtxt(path,delimiter=',',dtype='str')
    print(arreglo_mascotas)
def  crear():
	print('crear')
def borrar():
	print('borrar')
def editar():
	print('editar')
def salir():
	sys.exit()
def crud():
    print('\nBienvenido Administrador!')
    print('1. Listar')
    print('2. Crear')
    print('3. Borrar')
    print('4. Editar')
    print('5. Salir')
    accion = input('Que desea Hacer')
    print(accion)
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
def adoptar():
    print('aqui se adopta')
    
def tienda():    
    print('Bienvenido a  "MyPet Store"')

    usuario = input('ingresa tu Password :');


    if usuario == 'admin':
        crud()
    else:
        print('no admin')	

    input('salir??')