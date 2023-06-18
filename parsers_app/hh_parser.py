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


class HhParser(BaseParser):

    @staticmethod
    def _get_num_pages(text: str) -> str:
        """Получаем количество страниц с вакансиями"""
        time.sleep(1)
        page_elements_list = re.findall(r'pager-page-wrapper-\d+-\d+', text)
        if page_elements_list:
            counter = 0
            for el in tqdm(page_elements_list):
                last_el = int(el.split('-')[-1]) + 1
                if last_el > counter:
                    counter = last_el
            return str(counter)
        return '0'

    def _get_pages(self, text: str) -> list:
        """Получаем список страниц(URL) с вакансиями"""
        print('Получаем список страниц(URL) с вакансиями')
        time.sleep(1)
        pages = self._get_num_pages(text)
        page_list = []
        if int(pages) > 0:
            for page in tqdm(range(int(pages))):
                url = self.url + f'&page={page}'
                page_list.append(url)
            return page_list
        page_list.append(self.url + f'&page={pages}')
        return [self.url, ]

    def _get_vacancies_links(self, pages: list) -> list:
        """Получаем список ссылок на вакансии"""
        links_list = []
        watched = []
        print('\nСобираем ссылки на вакансии со всех страниц')
        time.sleep(1)
        for page in tqdm(pages):
            try:
                response = request(method='GET', url=page, headers=self.headers)
                if response.ok:
                    soup = bs(response.text, 'html.parser')
                    blocks = soup.find_all('div', {'class': 'serp-item'})
                    for block in blocks:
                        block_title = block.find_all_next('a', {'data-qa': 'serp-item__title'})[0].text
                        block_salary = block.find_all_next('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})[0].text
                        block_company = block.find_all_next('a', {'data-qa': 'vacancy-serp__vacancy-employer'})[0].text
                        block_link = block.find_all_next('a', {'data-qa': 'serp-item__title'})[0]['href']
                        watched.append((block_title, block_salary, block_company))
                        if len(watched) > 1:
                            if ((block_title, block_salary, block_company) not in watched[:-1]) and not (set(block_title.lower().split()) & set(self.STOP_WORDS)):
                                links_list.append(block_link)
                    time.sleep(random.randint(1, 3))
            except Exception as e:
                print(e)
        return links_list

    def _get_vacancy_page(self, link: str):
        """Получаем страницу вакансии"""
        try:
            response = request(method='GET', url=link, headers=self.headers)
            if response.ok:
                time.sleep(1)
                return response.text
        except Exception as e:
            print(e, link)
            return

    def _get_vacancy_data(self, page: str, link: str):
        """Получаем информацию по вакансии"""
        if page:
            try:
                soup = bs(page, 'html.parser')
                title = self.string_cleaner(soup.find('h1', {'data-qa': "vacancy-title"}).text)
                salary = self.string_cleaner(soup.find('div', {'data-qa': 'vacancy-salary'}).text).replace('на руки', '').replace('до вычета налогов', '')
                salary_from = None
                salary_to = None
                experience = None
                text = None
                new_text = ''
                stack = None
                company = None
                company_address = None
                is_remote = False
                if 'руб' in salary:
                    if 'от' in salary and 'до' not in salary:
                        salary_from = int(''.join([i for i in salary if i.isdigit()]))
                    if 'до' in salary and 'от' not in salary:
                        salary_to = int(''.join([i for i in salary if i.isdigit()]))
                    if 'от' in salary and 'до' in salary:
                        salary_list = salary.split('до')
                        salary_from = int(''.join([i for i in salary_list[0] if i.isdigit()]))
                        salary_to = int(''.join([i for i in salary_list[1] if i.isdigit()]))
                if 'USD' in salary or 'EUR' in salary:
                    if 'от' in salary and 'до' not in salary:
                        salary_from = int(''.join([i for i in salary if i.isdigit()])) * 75
                    if 'до' in salary and 'от' not in salary:
                        salary_to = int(''.join([i for i in salary if i.isdigit()])) * 75
                    if 'от' in salary and 'до' in salary:
                        salary_list = salary.split('до')
                        salary_from = int(''.join([i for i in salary_list[0] if i.isdigit()])) * 75
                        salary_to = int(''.join([i for i in salary_list[1] if i.isdigit()])) * 75
                if soup.find('span', {'data-qa': "vacancy-experience"}):
                    experience = Analyzer.get_experience(self.string_cleaner(soup.find('span', {'data-qa': "vacancy-experience"}).text))
                if soup.find('div', {'class': "vacancy-section"}):
                    text = soup.find('div', {'class': "vacancy-description"})
                    new_text = Analyzer.html_to_text(text)
                if soup.find('div', {'class': "bloko-tag-list"}):
                    stack_not_clear = soup.find_all('div', {'class': "bloko-tag bloko-tag_inline"})
                    stack = [i.text for i in stack_not_clear]
                if soup.find('div', {'class': "vacancy-company-details"}):
                    company = self.string_cleaner(soup.find('div', {'class': "vacancy-company-details"}).text)
                if soup.find('span', {'data-qa': "vacancy-view-raw-address"}):
                    company_address = self.string_cleaner(soup.find('span', {'data-qa': "vacancy-view-raw-address"}).text)
                if soup.find('p', {'data-qa': "vacancy-view-employment-mode"}):
                    if 'удаленная работа' in self.string_cleaner(soup.find('p', {'data-qa': "vacancy-view-employment-mode"}).text).lower():
                        is_remote = True
                vacancy = {}
                grade = Analyzer.get_grade(title, new_text)
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
        vacancy_dict = {'vacancies': []}
        html = self._get_vacancies_list_html()
        pages_list = self._get_pages(html)
        links = self._get_vacancies_links(pages_list)
        for link in tqdm(links):
            vacancy_page = self._get_vacancy_page(link)
            vacancy_data = self._get_vacancy_data(vacancy_page, link)
            if vacancy_data:
                vacancy_dict['vacancies'].append(vacancy_data)
                time.sleep(random.randint(1, 2))
        if wright_to_file:
            with open(f'vacancies_hh_{datetime.datetime.now().strftime("%d_%m_%Y")}.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(vacancy_dict))
        return vacancy_dict

