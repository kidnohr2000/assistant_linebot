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
        dt_string = datetime.now().strftime('%Y%m%d')
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
            if name_href is None:
                return '見つかんないですね'
            name = name_href.string
            url = name_href.get('href')
            _score = part.find('span', class_="list-rst__rating-val")
            _body = part.find('span', class_="list-rst__author-rvw-txt")

            if _score is not None:
                score = D(_score.string)
            else:
                score = None

            if _body is not None:
                body = _body.string
            else:
                body = None

            return ' '.join([name, url, str(score), str(body), self.url])

        else:
            return '見つかんないですね'
