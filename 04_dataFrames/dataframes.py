# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:23:30 2019
@author: MichaelDrake
"""

import pandas as pd
import numpy as np

arr_rand = np.random.randint(0,10,6).reshape(2,3)
df = pd.DataFrame(arr_rand,columns = ['Estatura (cm)','Peso (gr)','Edad (years)'], index = ['Michael','Morales'])

df2 = pd.DataFrame(arr_rand)
df2.columns = ['Estatura (cm)','Peso (gr)','Edad (years)']

#SOBREESCRIBIR LOS INDICES Y COLUMNAS
df2.index = ['Michael','Morales']
df3 = pd.DataFrame(arr_rand)

df3[0]

type(df['Estatura (cm)'])


df_v = pd.DataFrame([[1,2,'Hello'],['Hello',4,5]])
df_v[0]



df['Peso (gr)']['Michael']










