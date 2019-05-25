# -*- coding: utf-8 -*-
"""
Created on Fri May 24 18:54:05 2019

@author: MichaelDrake
"""

import pandas as pd
import os
import json


path = 'Documents/GitHub/py-morales-proa-o-michael-oswaldo/04_dataFrames/data/artwork/'
archivo = 'a/000/a00001-1035.json'


path_archivo = path + archivo

with open(path_archivo) as texto_json:
    contenido_json = json.load(texto_json)
    print(type(contenido_json))
    print(contenido_json)
    
    
    
    llaves = ['id','all_artists','title','medium','dateText','acquisitionYear','height','width','units']
    
  
    
    registro_df = []
    
    for llave in llaves:
        valor = contenido_json[llave]
        registro_df.append(valor)
        
    serie = tuple(registro_df)
    
    
    
    print(serie)
    
    
    
    df_chiquito = pd.DataFrame([registro_df],columns = llaves)
    
    
    
    def leer_json(path,llaves):
        with open(path_archivo) as texto_json:
            contenido_json = json.load(texto_json)
            registro_df_lista = []
            for llave in llaves:
                valor = contenido_json[llave]
                registro_df_lista.append(valor)
        return registro_df_lista
        
    
   leer_json(path_archivo,llaves)
    