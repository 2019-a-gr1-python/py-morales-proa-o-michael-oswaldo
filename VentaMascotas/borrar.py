import numpy as np
path = './msts.csv'

archivo_escritura_abierto = open(path, mode='w')
    archivo_escritura_abierto.writelines([f'\n{tipo},{nombre},{codigo}'])