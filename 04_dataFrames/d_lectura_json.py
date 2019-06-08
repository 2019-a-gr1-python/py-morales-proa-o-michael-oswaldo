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
   
   
def leer_en_carpetas(directorio, llaves):
    trabajos_arte = []
    print(type(os.walk(directorio)))
    for path_raiz, lista_directorios, archivos in os.walk(directorio):
        print(path_raiz)
        print(lista_directorios)
        print(archivos)
        print(type(path_raiz))
        print(type(lista_directorios))
        print(type(archivos))
        for nombre_archivo in archivo:
            if nombre_archivo.endswith('json'):
                directorio_archivo = os.path.join(path_raiz,nombre_archivo)
                pieza_arte = leer_json(directorio_archivo,llaves)
                trabajos_arte.append(pieza_arte)
    df = pd.DataFrame.from_records(trabajos_arte,columns = llaves,index = 'id')
    print(trabajos_arte)
    return df

           

df_art = leer_en_carpetas(path,llaves)

           


def leer_json_en_carpetas(directorio, llaves):
    trabajos_arte = []
    print(type(os.walk(directorio)))  # 
    for path_raiz, lista_directorios, archivos in os.walk(directorio):
        print(path_raiz)  
        print(type(path_raiz))  # String -> Path Actual
        print(lista_directorios)
        print(type(lista_directorios))  #  List String directorios 
        print(archivos)
        print(type(archivos))  #  List Strings nombre archivos

        for nombre_archivo in archivos:
            print(nombre_archivo)
            if nombre_archivo.endswith('json'):
                directorio_archivo = os.path.join(
                        path_raiz,
                        nombre_archivo
                        )
                pieza_arte = leer_json(directorio_archivo, llaves)
                trabajos_arte.append(pieza_arte)

    df = pd.DataFrame.from_records(
            trabajos_arte,
            columns = llaves,
            index = 'id'
            )
    return df


df_artworks = leer_json_en_carpetas(path,llaves)
       
       
       
       
       
       
       
       
       
   
   
   
   
    