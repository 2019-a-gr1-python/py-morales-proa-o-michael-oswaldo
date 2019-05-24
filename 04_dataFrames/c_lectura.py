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

path = 'data/csv/artwork_data.csv'
pd.read_csv(
         'data/csv/artwork_data.csv',
        nrows = 5,
        usecols = ['id','artist'],
        
        )