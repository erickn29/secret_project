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
            soup = bs(request(method='GET', url=link, headers=self.headers).text, 'html.parser')
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

    def _get_vacancy_data(self, page: str, link: str):
        """Получаем информацию по вакансии"""
        soup = bs(page, 'html.parser')
        scripts_json = soup.find_all('script', {'type': 'application/ld+json'})
        data = None
        for script in scripts_json:
            if 'title' in script.text:
                data = json.loads(script.text)
        try:
            title = data.get('title')
            salary_from = data.get('baseSalary').get('value').get('minValue')
            salary_to = data.get('baseSalary').get('value').get('maxValue')
            exp_obj = soup.select_one('.f-test-address').nextSibling
            experience = Analyzer.get_superjob_experience(exp_obj.text)
            text = bs(data.get('description'), 'html.parser')
            new_text = Analyzer.html_to_text(text)
            stack = Analyzer.get_stack_raw_text(new_text)
            company = data.get('hiringOrganization').get('name')
            company_address = data.get('jobLocation').get('address').get('addressLocality')
            is_remote = True if data.get('jobLocationType') == 'TELECOMMUTE' else False
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
            print(e)

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
