import numpy as np
import matrices_calcu as c
import varios.main as v




print("""
****************************************
****************************************
******  EJERCICIOS CON NUMPY    ********
****************************************
****************************************
""")

accion = -1

while accion!=5:
      print("""
      1. Calculadora de Matrices
      2. Archivos en Numpy
      3. Varios
      4. Imagenes
      5. Salir
      """)
      accion = input('Que desea Hacer')
      if accion == '1':
            c.main()
      elif accion == '2':
            print('a')
      elif accion == '3':
            v.main()

      elif accion == '5':
            print('Hasta Luego')
            accion = 5









