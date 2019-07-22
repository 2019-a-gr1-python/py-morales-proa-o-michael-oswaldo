# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose

def transformar_url_imagen(texto):
    url = 'https://www.fybeca.com'
    cadena_a_reemplazar = '../..'
    return texto.replace(cadena_a_reemplazar,url)
def transformar_precio(precio_sin_formatear):
    auxiliar = precio_sin_formatear[12:-26]
    return auxiliar
class ProductoFybeca(scrapy.Item):
    imagen = scrapy.Field(input_processor = MapCompose(
            transformar_url_imagen
            )
    )
    precio = scrapy.Field(input_processor = MapCompose(
    transformar_precio
    ))
    titulo = scrapy.Field()
    
