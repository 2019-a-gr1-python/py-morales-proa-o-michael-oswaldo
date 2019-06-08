# -*- coding: utf-8 -*-
"""
Created on Wed May 29 07:34:33 2019

@author: MichaelDrake
"""
import pandas as pd

path_guardado = 'C:/Users/MichaelDrake/Documents/GitHub/py-morales-proa-o-michael-oswaldo/04_dataFrames/data/csv/artwork_data.pickle'

df = pd.read_pickle(path_guardado)

primero = df.loc[1035,'Artist']
segundo = df.loc[1036, 'units']
df.loc[0] #erro porque no esta dentro del label


primero_a = df.iloc[0]


primero_b = df.iloc[0,:]

primero_c = df.iloc[0,0:-2]

primero_c2 = df.iloc[0:100,0:-2]


#mayor Ancho Mayor Alto 



tres_primeros = df.head(10)['width'].sort_values(ascending = False).head(3)

tres_ultimos = df.head(10)['width'].sort_values().tail(3)






a = df['year'].sort_values(axis = 0)


serie_validado = pd.to_numeric(df['width'],errors = 'coerce')

df.loc[:,'width'] = serie_validado
df.iloc[:,5] = serie_validado


diez_primeros = df['width'].sort_values(ascending = False).head(10)
diez_ultimos = df['width'].sort_values(ascending = False).tail(10)

serie_validado_height = pd.to_numeric(df['height'],errors = 'coerce')
df.loc[:,'height'] = serie_validado_height


area = df['height']*df['width']

type(area)

df['area'] = area

df = df.assign(areados = area)


df_area = df['area'].sort_values(ascending = False).head(1)

id_max_area = df['area'].idxmax()

id_min_area = df['area'].idxmin()


#registro_mas_area = 






