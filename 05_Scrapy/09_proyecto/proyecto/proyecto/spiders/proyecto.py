import scrapy
from proyecto.items import Country
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class AraniaProyecto(scrapy.Spider):
    name = 'arania_population'  # Heredado (conservar nombre)
    def start_requests(self):
        urls = ['https://www.worldometers.info/world-population/population-by-country/']
        for url in urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        paises =  response.css('table>tbody>tr')

        for pais in paises:
            datos_pais = pais.css('td')
            i = 0
            campos = ['Ranking','Country','Population','Yearly_Change','Net_Change','Density','Land_Area','Migrants','Fert_Rate','Med_Age','Urban_Population','World_Share']
            pais_loader = ItemLoader(
            item = Country()
            )
            for dato in datos_pais:
                if(i == 1):
                    pais_loader.default_output_processor = TakeFirst()
                    pais_loader.add_value(campos[i],dato.css('td>a::text').extract_first())
                    i = i+1
                else:
                    pais_loader.default_output_processor = TakeFirst()
                    pais_loader.add_value(campos[i],dato.css('::text').extract_first())
                    i = i+1
            yield pais_loader.load_item()
            print('######################################################################3###')

                #print(titulo.extract_first())
                #print(url.extract_first())
