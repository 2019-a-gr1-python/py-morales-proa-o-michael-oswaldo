import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_03.items import ProductoFybeca
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst



class AraniaCrawlFybeca(CrawlSpider):
    name = 'crawl_fybeca'  # Heredado (conservar nombre)

    allowed_domains = [  # Heredado (conservar nombre)
        'fybeca.com'
    ]
    start_urls = [  # Heredado (conservar nombre)
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=0&pp=25'
    ]
    # Heredado (conservar nombre)

    regla_uno = (
        Rule(LinkExtractor(), callback='parse_page')
        ,
    )
    url_segmento_permitido = (
    '.+(cat=238)'
    )




    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                #allow=('funds-programmes-specialized-agencies-and-others')
            ), callback='parse_page')
        ,
    )
    regla_tres = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                #allow= url_segmento_permitido,
            ), callback='parse_page')
        ,
    )
    rules = regla_tres



    def parse_page(self, response):

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

                yield producto_loader.load_item()
                print('######################################################################3###')
                print(producto_loader)

                #print(titulo.extract_first())
                #print(url.extract_first())
