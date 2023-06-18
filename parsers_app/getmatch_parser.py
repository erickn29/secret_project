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


class GetMatchParser(BaseParser):
    @staticmethod
    def _get_num_pages(text: str) -> str:
        """Получаем количество страниц с вакансиями"""
        soup = bs(text, 'html.parser')
        pagination_buttons = soup.find_all('div', {'class': 'b-pagination-page'})
        if pagination_buttons:
            return str(int(len(pagination_buttons) / 2))
        return '1'

    def _get_pages(self, text: str) -> list:
        """Получаем список страниц(URL) с вакансиями"""
        print('Получаем список страниц(URL) с вакансиями')
        time.sleep(1)
        pages = self._get_num_pages(text)
        page_list = []
        if int(pages) > 0:
            for page in tqdm(range(1, int(pages) + 1)):
                url = self.url + f'&p={page}'
                page_list.append(url)
            return page_list
        # page_list.append(self.url + f'&page={pages}')
        return [self.url, ]

    def _get_vacancies_links(self, pages: list) -> list:
        links = []
        for link in pages:
            soup = bs(request(method='GET', url=link, headers=self.headers).text, 'html.parser')
            vacancy_cards = soup.find_all('div', {'class': 'b-vacancy-card'})
            for card in vacancy_cards:
                card_obj = bs(str(card), 'html.parser')
                link = card_obj.find('a')
                links.append(f'https://getmatch.ru{link.get("href")}')
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

    def _get_vacancy_data(self, page: str, link: str):
        """Получаем информацию по вакансии"""
        if page:
            try:
                soup = bs(page, 'html.parser')
                title = soup.find('h1').text
                salary_string = soup.find_all('h3')[0].text
                salary_from = None
                salary_to = None
                if '—' in salary_string:
                    salary_list = salary_string.split('—')
                    salary_from = int(salary_list[0].replace(' ', ''))
                    salary_to = int(salary_list[1].replace('₽/мес на руки', '').replace('$/мес на руки', '').replace('€/мес на руки', ''). replace(' ', '').replace('\u200d', ''))
                    if '$' in salary_string or '€' in salary_string:
                        salary_from = salary_from * 75
                        salary_to = salary_to * 75
                if 'от' in salary_string:
                    salary_string = salary_string.replace(' ', '')
                    number = ''
                    for c in salary_string:
                        if c.isdigit():
                            number += c
                    salary_from = int(number)
                    if '$' in salary_string or '€' in salary_string:
                        salary_from = int(number) * 75

                exp_obj = soup.find('div', text='Уровень').nextSibling.text
                experience = Analyzer.get_getmatch_experience(exp_obj)
                text = soup.find('section', {'class': 'b-vacancy-description'})
                new_text = Analyzer.html_to_text(text)
                stack_obj = bs(str(soup.find('div', {'class': 'b-vacancy-stack-container'})), 'html.parser')
                stack_tags = stack_obj.find_all('span', {'class': 'g-label'})
                stack_list = []
                for obj in stack_tags:
                    stack_list.append(obj.text)
                stack = stack_list
                company = soup.find_all('h2')[0].text.replace('в ', '')
                company_address = None
                if soup.find('span', {'class': 'b-vacancy-locations--first'}):
                    company_address = soup.find('span', {'class': 'b-vacancy-locations--first'}).text.replace('\"', '').replace('📍 ', '')
                is_remote = True if 'Полная удалёнка' in soup.text else False
                grade = None
                if soup.find('div', text='Уровень').nextSibling:
                    grade = soup.find('div', text='Уровень').nextSibling.text
                vacancy = {}
                vacancy.update({
                    'title': title,
                    'salary_from': salary_from,
                    'salary_to': salary_to,
                    'is_remote': is_remote,
                    'experience': experience,
                    'grade': grade,
                    'text': new_text,
                    'stack': stack,
                    'company': company,
                    'company_address': company_address,
                    'date': datetime.datetime.now().strftime('%Y-%m-%d'),
                    'link': link
                })
                time.sleep(1)
                return vacancy
            except Exception as e:
                print(e, link)
        return

    def get_vacancies(self, wright_to_file: bool = True) -> dict:
        # ftc
        vacancy_dict = {'vacancies': []}
        html = self._get_vacancies_list_html()
        pages_list = self._get_pages(html)
        links = self._get_vacancies_links(pages_list)
        for link in tqdm(links):
            vacancy_page = self._get_vacancy_page(link)
            vacancy_data = self._get_vacancy_data(vacancy_page, link)
            vacancy_dict['vacancies'].append(vacancy_data)
            time.sleep(random.randint(1, 3))
        if wright_to_file:
            with open(f'vacancies_hh_{datetime.datetime.now().strftime("%d_%m_%Y")}.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(vacancy_dict))
        return vacancy_dict
