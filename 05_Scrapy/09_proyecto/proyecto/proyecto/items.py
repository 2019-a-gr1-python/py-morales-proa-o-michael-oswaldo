# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose

def transformar_porcentaje(valor_con_porcentaje):
    if (valor_con_porcentaje == 'N.A.'):
        return "0.00%"
    else:
        auxiliar = valor_con_porcentaje[:-2]
        auxiliar = auxiliar + "%"
        return auxiliar
def transformar_valor(valor_entrada):
    if (valor_entrada == 'N.A.'):
        return "0"
    elif(valor_entrada == ' '):
        return "0"
    else:
        return valor_entrada

class Country(scrapy.Item):
    Ranking = scrapy.Field(input_processor = MapCompose(transformar_valor))
    Country = scrapy.Field(input_processor = MapCompose(transformar_valor))
    Population = scrapy.Field(input_processor = MapCompose(transformar_valor))
    Yearly_Change = scrapy.Field(input_processor = MapCompose(transformar_porcentaje))
    Net_Change = scrapy.Field(input_processor = MapCompose(transformar_valor))
    Density = scrapy.Field(input_processor = MapCompose(transformar_valor))
    Land_Area = scrapy.Field(input_processor = MapCompose(transformar_valor))
    Migrants = scrapy.Field(input_processor = MapCompose(transformar_valor))
    Fert_Rate = scrapy.Field(input_processor = MapCompose(transformar_valor))
    Med_Age = scrapy.Field(input_processor = MapCompose(transformar_valor))
    Urban_Population = scrapy.Field(input_processor = MapCompose(transformar_porcentaje))
    World_Share = scrapy.Field(input_processor = MapCompose(transformar_porcentaje))
