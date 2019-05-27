# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:40:45 2019

@author: MichaelDrake
"""

import pandas as pd
import os #because we'll need to read things from OS

#Archivos de Texto  JSON, CSV, HTML, XML,
#BINARY FILES --->  (ASDASFDASDFSSSSSSSSSSSSSDFSF)
#Relational Databases 

path = 'Documents/GitHub/py-morales-proa-o-michael-oswaldo/04_dataFrames/data/csv/artwork_data.csv'

dir = os.getcwd()#get your directory work
li = os.listdir(os.getcwd())
df = pd.read_csv(
         path,
        nrows = 5,
        usecols = ['id','artist'],
        index_col = 'id'
        )

columnas_a_usar = ['id','artist','title','medium','year','acquisitionYear','height','width','units']


df_completo = pd.read_csv(
         path,
        usecols = columnas_a_usar,
        index_col = 'id'
        )


path_guardado = 'Documents/GitHub/py-morales-proa-o-michael-oswaldo/04_dataFrames/data/csv/artwork_data.pickle'




df_completo.to_pickle(path_guardado)

df_completo_pickle = pd.read_pickle(path_guardado)
