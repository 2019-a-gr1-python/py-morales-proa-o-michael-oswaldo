import numpy as np





def main():
    accion = -1
    matriz = np.ones((2,2))
    print("Matriz :")
    print(matriz)


    while accion != 8:

        print("""
          1. Matriz Aleatoria
          2. Seno Matriz
          3. Coseno Matriz
          4. Media
          5. Mediana
          6. Varianza
          7. Desviación Estandar
          8. Salir
          """)

        accion = input('Que desea Hacer')
        if accion == '1':
            matriz = np.random.randint(0,100,4)
            matriz.shape = (2,2)
            print(matriz)
        elif accion == '2':
            print(np.sin(matriz))
        elif accion == '8':
            print('Hasta Luego')
            accion = 8




