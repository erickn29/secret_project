import datetime
from .base_parser import BaseParser
from .analyzer import Analyzer
from requests import request
from bs4 import BeautifulSoup as bs
import re
import time
import random
import json
from tqdm import tqdm
from vacancies_app.models import *


class SuperJobParser(BaseParser):
    @staticmethod
    def _get_num_pages(text: str) -> str:
        """Получаем количество страниц с вакансиями"""
        time.sleep(1)
        page_elements_list = re.findall(r'f-test-link-\d+', text)
        if page_elements_list:
            return str(len(page_elements_list))
        return '0'

    def _get_pages(self, text: str) -> list:
        """Получаем список страниц(URL) с вакансиями"""
        print('Получаем список страниц(URL) с вакансиями')
        time.sleep(1)
        pages = self._get_num_pages(text)
        page_list = []
        if int(pages) > 0:
            for page in tqdm(range(1, int(pages) + 1)):
                url = self.url + f'&page={page}'
                page_list.append(url)
            return page_list
        # page_list.append(self.url + f'&page={pages}')
        return [self.url, ]

    def _get_vacancies_links(self, pages: list) -> list:
        links = []
        for link in pages:
            soup = bs(request(method='GET', url=link, headers=self.headers).text)
            all_links_on_page = soup.find_all('a')
            for link_ in all_links_on_page:
                if 'vakansii' in link_.attrs.get('href') and '.html' in link_.attrs.get('href'):
                    links.append(f"https://russia.superjob.ru{link_.attrs.get('href')}")
        return links

    def _get_vacancy_page(self, link: str):
        """Получаем страницу вакансии"""
        try:
            response = request(method='GET', url=link, headers=self.headers)
            if response.ok:
                time.sleep(1)
                return response.text
        except Exception as e:
            print(e)
            return

    def get_vacancies_links(self):
        html = self._get_vacancies_list_html()
        pages_list = self._get_pages(html)
        links = self._get_vacancies_links(pages_list)
        return links
