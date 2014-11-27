#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from decimal import Decimal

from lxml import etree
import requests
from redis import Redis

from currency_converter.appconfig import Config

logging.basicConfig(level=logging.DEBUG)

DATA_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

redis = Redis.from_url(Config.REDIS_URL)


def import_currencies():
    logging.info("Fetching data from '%s'" % DATA_URL)

    response = requests.get(DATA_URL, stream=True)

    tree = etree.fromstring(response.content)
    if tree is None:  # using this form to prevent FutureWarning of lxml
        logging.error("Nothing to do. Data is empty")
        exit(1)

    for currency in tree.findall('Valute'):
        code = currency.find('CharCode').text.upper()
        nominal = Decimal(currency.find('Nominal').text.replace(',', '.'))
        value = Decimal(currency.find('Value').text.replace(',', '.'))
        currency_rate = value / nominal
        logging.debug("code %s, nominal %s, value %s, currency_rate %s",
                      code, nominal, value, currency_rate)

        key = code
        redis.hmset(key, {
            'rate': currency_rate,
            'value': value,
            'nominal': nominal,
        })


if __name__ == '__main__':
    import_currencies()
