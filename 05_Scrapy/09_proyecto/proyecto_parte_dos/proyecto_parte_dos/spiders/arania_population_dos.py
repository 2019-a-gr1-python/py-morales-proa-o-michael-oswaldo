import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from proyecto_parte_dos.items import Country
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst



class AraniaPopulationDos(CrawlSpider):
    name = 'crawl_population_dos'  # Heredado (conservar nombre)

    allowed_domains = [  # Heredado (conservar nombre)
        'worldometers.info'
    ]
    start_urls = [  # Heredado (conservar nombre)
        'https://www.worldometers.info/world-population/population-by-country'
    ]
    # Heredado (conservar nombre)

    regla_uno = (
        Rule(LinkExtractor(), callback='parse_page')
        ,
    )
    url_segmento_permitido = (
    'https://www.worldometers.info/world-population/china-population/',
    'https://www.worldometers.info/world-population/india-population/',
    'https://www.worldometers.info/world-population/us-population/',
    'https://www.worldometers.info/world-population/indonesia-population/',
    'https://www.worldometers.info/world-population/brazil-population/',
    'https://www.worldometers.info/world-population/pakistan-population/',
    'https://www.worldometers.info/world-population/nigeria-population/',
    'https://www.worldometers.info/world-population/bangladesh-population/',
    'https://www.worldometers.info/world-population/russia-population/',
    'https://www.worldometers.info/world-population/mexico-population/'
    )


    regla_tres = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                allow= url_segmento_permitido,
            ), callback='parse_page')
        ,
    )
    rules = regla_tres



    def parse_page(self, response):
        paises =  response.css('table>tbody>tr')

        for pais in paises:
            datos_pais = pais.css('td')
            i = 0
            campos = ['Country','Year','Population','Yearly_Change','Yearly_Net_Change','Migrants','Med_Age','Fert_Rate','Density','Urban_Population','Urban_Net_Population','World_Share','World_population','Ranking']
            pais_loader = ItemLoader(
            item = Country()
            )
            for dato in datos_pais:
                if(i == 0):
                    pais_loader.default_output_processor = TakeFirst()
                
                    pais_loader.add_value(campos[i],response.css('div.content>div[id="maincounter-wrap"]>h1::text').extract_first())
                    i = i+1
                elif(i == 2):
                    pais_loader.default_output_processor = TakeFirst()
                    pais_loader.add_value(campos[i],dato.css('td>strong::text').extract_first())
                    i = i+1
                else:
                    pais_loader.default_output_processor = TakeFirst()
                    pais_loader.add_value(campos[i],dato.css('::text').extract_first())
                    i = i+1
            yield pais_loader.load_item()
            print('######################################################################3###')
