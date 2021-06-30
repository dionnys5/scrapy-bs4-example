# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TutorialPipeline(object):
    """
    Essa classe é responsável por tratar os items coletados pelo spider.
    É obrigatório que o projeto tenha a função process_item, porém outras funções como spider_open, spider_close
    podem ser úteis no gerenciamento das informações.
    """
    def process_item(self, item, spider):
        return item
