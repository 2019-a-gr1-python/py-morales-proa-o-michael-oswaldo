import scrapy
import os
import pandas as pd

def resultados():
    print("\n\nRESULTADOS\n\n")

    path = 'tmp/productos-fybeca.csv'
    df = pd.read_csv(path,usecols=['imagen','precio','titulo'])

    df['precio'] = pd.to_numeric(df['precio'])

    promedio = df['precio'].mean()
    print('EL PROMEDIO DE LOS PRECIOS ES ',promedio)

    print('\nMAYORES AL PROMEDIO\n')
    mayores = df['precio'] > promedio
    print(df[mayores])




    print('\n\nMENORES AL PROMEDIO\n')
    menores = df['precio'] <= promedio
    print(df[menores])



resultados()
