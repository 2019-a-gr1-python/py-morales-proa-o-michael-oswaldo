
def crud():
	print('\nBienvenido Administrador!')
    print('1. Listar')
    print('2. Crear')
    print('3. Borrar')
    print('4. Editar')
    print('5. Salir')
    accion = input('Que desea Hacer')
    def listar():
		print('Esta Listando')
	def crear():
		print('Esta crear')
	def borrar():
		print('Esta borrar')
	def editar():
		print('Esta editar')
    def switch_accion():
        return{
            '1' :listar(),
            '2' :crear(),
            '3' :borrar(),
             '4' :editar() 
            }[accion]
    return switch_accion()



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