import scrapy
from scrapy_03.items import ProductoFybeca
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
import os
import pandas as pd
class AraniaProductosFybeca(scrapy.Spider):
    name = 'arania_fybeca'

    def start_requests(self):
        urls = []
        for i in range(0, 151, 25):
            urls.append(f'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?s={i}&pp=25&cat=238&ot=0')
        print('URLLLLLLLSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')
        print(urls)
        for url in urls:
            yield scrapy.Request(url=url)
            print('SCRAPEEDD')
            print(url)

    def parse(self, response):

        productos = response.css('div.product-tile-inner')

        for producto in productos:
            existe_producto = len(producto.css('div.detail'))

            if(existe_producto > 0):
                #titulo = producto.css('a.name::text')
                #url = producto.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
                producto_loader = ItemLoader(
                item = ProductoFybeca(),
                selector = producto
                )
                producto_loader.default_output_processor = TakeFirst()
                producto_loader.add_css('titulo',
                'a.name::text')
                producto_loader.add_xpath(
                'imagen',
                'div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src'
                )
                producto_loader.add_css('precio','.price::attr(data-bind)')

                yield producto_loader.load_item()
    




                # print('######################################################################3###')
                #print(producto_loader)

                #print(titulo.extract_first())
                #print(url.extract_first())
