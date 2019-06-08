# -*- coding: utf-8 -*-
"""
Created on Wed May 29 08:23:09 2019

@author: MichaelDrake
"""

import pandas as pd
import numpy as np
import math


path_guardado = 'C:/Users/MichaelDrake/Documents/GitHub/py-morales-proa-o-michael-oswaldo/04_dataFrames/data/csv/artwork_data.pickle'

df = pd.read_pickle(path_guardado)



seccion_df = df.iloc[49980:50019,:].copy()


df_agrupado_ay = seccion_df.groupby('acquisitionYear')
type(df_agrupado_ay)

for acquisitionYear,registros  in df_agrupado_ay:
    print(acquisitionYear)
    #print(registros)
    
    
    df_agrupado_art = seccion_df.groupby('artist')
type(df_agrupado_art)

for artist,registros  in df_agrupado_art:
    print(artist)
    #print(registros)
    
"""   
    # 1) iterar y sumar los valores
    sumatoria = 0
    numero_nans = 0
    for valor in series:
        print(valor)
        print(type(valor))
        if type(valor) == str:
            sumatoria = sumatoria + int(valor)
        if type(valor) == float:
            numero_nans = numero_nans + 1
    print(sumatoria)
    
    # 2) Dividir para el numero de valores
    division = series.size - numero_nans
    valor_mas_utilizado = sumatoria / division
    print(valor_mas_utilizado)
    """

def llenar_valores_vacios(series):
    valores = series.values_counts()
    if(valores.empty):
        return series
    """   
    # 1) iterar y sumar los valores
    sumatoria = 0
    numero_nans = 0
    for valor in series:
        print(valor)
        print(type(valor))
        if type(valor) == str:
            sumatoria = sumatoria + int(valor)
        if type(valor) == float:
            numero_nans = numero_nans + 1
    print(sumatoria)
    
    # 2) Dividir para el numero de valores
    division = series.size - numero_nans
    valor_mas_utilizado = sumatoria / division
    print(valor_mas_utilizado)
    """
    nuevo_valor = series.fillna(valores.index[0])
    return nuevo_valor
    

def transformar_df(df):
    df_artist = df.groupby('artist')
    arreglo_df_grupo = []
    
    for nombre_artista,registros_agrupados in df_artist:
        copia = registros_agrupados.copy()
        serie_medium = registros_agrupados['medium']
        serie_units = registros_agrupados['units']
        copia.loc[:,'medium'] = llenar_valores_vacios(serie_medium)
        copia.loc[:,'inits'] = llenar_valores_vacios(serie_inits)
        arreglo_df_grupo.append(copia)
    nuevo_df_transformado = pd.concat(arreglo_df_grupo)
    return nuevo_transformado


type(seccion_df)
transformar_df_t = transformar_df(seccion_df)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    