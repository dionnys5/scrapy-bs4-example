# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


def tokenizador(value):
    """

    :param value:
    :return: Uma lista com as palavras com base nas palavras da frase Value, separa com base nos espaços
    """
    return value.split(' ')


class TutorialItem(scrapy.Item):
    quote = scrapy.Field(serializer=tokenizador)
    autor = scrapy.Field()