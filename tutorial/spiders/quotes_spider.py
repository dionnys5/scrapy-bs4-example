import scrapy
from tutorial.items import TutorialItem
from bs4 import BeautifulSoup


class QuotesSpider(scrapy.Spider):
    """
    A :class QuostesSpider: é composta pelos parâmetros e lógica da seleção e coleta de dados de uma página HTML.
    """
    name = "quotes"

    start_urls = [f'https://repositorio.utfpr.edu.br/jspui/handle/1/{number}' for number in range(2369, 2379)]

    # Lembrar de sempre colocar nomes significativos para os arquivos de saída.
    # Para testes sempre apagar a pasta criada definida em JOBDIR
    custom_settings = {
        'ITEM_PIPELINES': {
            'tutorial.pipelines.TutorialPipeline': 400
        },
        'LOG_FILE': 'tutorial.log',
        'FEED_FORMAT': 'csv',
        'JOBDIR': 'crawls\\tutorial',
        'FEED_URI': 'tutorial_resultados_2.csv'
    }

    def parse(self, response, **kwargs):
        '''
        :param response: Que é o valor do conteúdo da página visitada a partir das start_urls
        :return: Objeto da classe TutorialItem que define a estrutura de dados coletados
        '''
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('td', attrs={'class': 'metadataFieldValue dc_title'})
        authors = soup.find('td', attrs={'class': 'metadataFieldValue dc_creator'})
        advisor = soup.find('td', attrs={'class': 'metadataFieldValue dc_contributor_advisor1'})
        keyWords = soup.find('td', attrs={'class': 'metadataFieldValue dc_subject'})
        date = soup.find('td', attrs={'class': 'metadataFieldValue dc_date_issued'})
        abstrat = soup.find('td', attrs={'class': 'metadataFieldValue dc_description_resumo'})
        print(
            "Título: " + title.text + "\n-" + "Autores: " + authors.text + "\n-" + "Orientadores: " +
            advisor.text + "\n-" + "Palavras-chave: " + keyWords.text + "\n-"  "Data: " + date.text +
            "\n-" + "Resumo: " + abstrat.text
        )
        yield {
            'title': title,
            'authors': authors,
            'advisor': advisor,
            'keyWords': keyWords,
            'date': date,
            'abstrat': abstrat,
        }
