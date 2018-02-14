# -*- coding: utf-8 -*-
# vim:tabstop=4:shiftwidth=4:expandtab

from urllib.parse import quote, unquote
from datetime import datetime
from decimal import Decimal as D

from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://tabelog.com/rstLst/?vs=1&sa=&sk={search_keyword}&lid=hd_search1&vac_net=&svd={dt_string}&svt=1900&svps=2&hfc=1&Cat=RC&LstCat=RC02&LstCatD=RC0212&sw='


class Talking(object):

    def __init__(self, message):
        self.message = message
        search_keyword = quote(quote(self.message))
        dt_string = datetime.now().strftime('%Y%n%d')
        self.url = BASE_URL.format(
            search_keyword=search_keyword,
            dt_string=dt_string,
        )

    def search(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content, 'html.parser')
        l =soup.find_all('li', class_='list-rst')
        if len(l):
            part = l[0]
            name_href = part.find('a', class_="list-rst__rst-name-target")
            name = name_href.string
            url = name_href.get('href')
            score = D(part.find('span', class_="list-rst__rating-val").string or 0)
            body = part.find('span', class_="list-rst__author-rvw-txt").string
            return ' '.join([name, url])

        else:
            return '見つかんないですね'
