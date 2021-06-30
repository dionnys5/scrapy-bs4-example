from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from tutorial.spiders.quotes_spider import QuotesSpider

settings = get_project_settings()
settings.set('FEED_FORMAT', 'csv')
# Aqui os settings do projeto são importados para o processo
process = CrawlerProcess(settings)
# O processo recebe a spider que deve realizar a extração
process.crawl(QuotesSpider)
# O Script vai ficar bloqueado aqui até que o spider tenha finalizado a coleta de dados
process.start()
