import numpy as np
#edad = 29
#prinint(edad)
#edad_str = '29'
#suma = int(edad_str)+edad
#print(suma)
parrafo = """chbsacb sdicb asduiasd asdbasjdbkjasdbkjasdbcjasdbkajsdh ckjsadbcbasdvada
sdinte
asdf
as
dfsdv
asd
va
fv
afd
vad
vadfvadfv
dafvadfv
advadfvadfvaf
vafdv
asvafsvadfvadf
"""
#print(type(parrafo))
#print(parrafo)
#nombre = 'Michael Morales'
#nombre.split(' ')
#print(nombre.split(' '))
#print(f'eres lo mef¿jor {nombre}')
#if(not not  False):
#    print('verdad')
#else:
#    print('falso')
#lista = [1,2,3,4,5,6,7,8,9,0]
#print(lista[0:2])


arreglo_frutas = np.array([
    ['Manzana', 'Pera', 'Sandia','Banana'],
    ['Kiwi','Naranja','Tomata','Limon'],
    ['Fritilla','Babaco','Maracuya','Melon'],
    ['Durasno','Papaya','Pitajaya','Uva'],
    ['Cereza','Mora','Lima','Tamarindo'],
    ['Cacao','Aguacate','Zanahoria','Naranjilla']
])



arreglo_filas = np.array([
[0,0,0,0],
    [1,1,1,1],
    [2,2,2,2],
    [3,3,3,3]

])

arreglo_columnas = np.array([
[0,1,2,3],
[0,1,2,3],
[0,1,2,3],
[0,1,2,3],
])





arreglo_frutas_dos = arreglo_frutas.reshape(4,3,2)
print(arreglo_frutas_dos)



arreglo_m1 = np.array([
    [[0,0]],
[[1,1]],
[[2,2]],
[[3,3]]


])
arreglo_m2 = np.array([
    [0,0],
    [1,1],
    [2,2]

])
arreglo_m3 = np.array([
[[0,1]]
])



print(arreglo_frutas_dos[arreglo_m1,arreglo_m2,arreglo_m3])





a = np.array([[1,0,3,4,5,62],[1,2,3,4,55,6]])
print(a)



empieza_letra_lambda = lambda x: x.startswith('P')


array_a = np.array([1,2])
print(array_a[[True, False]])


print(arreglo_frutas.flatten()[(list(map(empieza_letra_lambda,arreglo_frutas.flatten())))])