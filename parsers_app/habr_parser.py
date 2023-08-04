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
# from vacancies_app.models import *
import xmltodict
import json


# class HabrParser(BaseParser):
#     def _get_all_vacancies_xml(self):
#         response = request(method='GET', url=self.url, headers=self.headers).text
#         print(response)


class HabrParser(BaseParser):
    def get_vacancies(self):
        response = request(method='GET', url=self.url, headers=self.headers)
        if response.ok:
            rss = xmltodict.parse(response.text)
            vacancies_list = rss['rss']['channel']['item']
            vacancies_dict = {'vacancies': []}
            for vacancy in tqdm(vacancies_list):
                date = datetime.datetime.strptime(vacancy['pubDate'], '%a, %d %b %Y %H:%M:%S +0300').strftime('%Y-%m-%d')
                if date == datetime.datetime.now().strftime('%Y-%m-%d'):
                    description = vacancy['description'].split('. ')
                    salary_from = None
                    salary_to = None
                    grade = Analyzer.get_grade(vacancy['title'].lower(), vacancy['description'].replace('#', '').replace(',', '').replace('/', ' ').lower())
                    stack = [i.replace('#', '', 1).replace(',', '').replace('.', '') for i in vacancy['description'].split('Требуемые навыки: ')[-1].split()[1:]]
                    company = re.search(r'«([\s\S]+)»', vacancy['description'].split(' на вакансию ')[0])
                    company_address = [i.split(' ')[0] for i in vacancy['description'].split('. ') if '(Россия)' in i]
                    for item in description:
                        if 'От' in item or 'До' in item:
                            salary = item.lower()
                            if '₽' in salary:
                                if 'от' in salary and 'до' not in salary:
                                    salary_from = int(''.join([i for i in salary if i.isdigit()]))
                                if 'до' in salary and 'от' not in salary:
                                    salary_to = int(''.join([i for i in salary if i.isdigit()]))
                                if 'от' in salary and 'до' in salary:
                                    salary_list = salary.split('до')
                                    salary_from = int(''.join([i for i in salary_list[0] if i.isdigit()]))
                                    salary_to = int(''.join([i for i in salary_list[1] if i.isdigit()]))
                            if '$' in salary or '€' in salary:
                                if 'от' in salary and 'до' not in salary:
                                    salary_from = int(''.join([i for i in salary if i.isdigit()])) * 75
                                if 'до' in salary and 'от' not in salary:
                                    salary_to = int(''.join([i for i in salary if i.isdigit()])) * 75
                                if 'от' in salary and 'до' in salary:
                                    salary_list = salary.split('до')
                                    salary_from = int(''.join([i for i in salary_list[0] if i.isdigit()])) * 75
                                    salary_to = int(''.join([i for i in salary_list[1] if i.isdigit()])) * 75
                    vacancies_dict['vacancies'].append({
                        'title': vacancy['title'].replace('Требуется «', '').split('»')[0],
                        'salary_from': salary_from,
                        'salary_to': salary_to,
                        'is_remote': True if 'Можно удалённо' in vacancy['description'] else False,
                        'experience': Analyzer.HABR_EXPERIENCE.get(grade) if grade else 'нет опыта',
                        'grade': grade,
                        'text': vacancy['description'],
                        'stack': stack,
                        'company': company.group(0)[1: -1],
                        'company_address': company_address[0] if company_address else None,
                        'date': datetime.datetime.now(),
                        'link': vacancy['link']
                    })
            return vacancies_dict
        else:
            raise ConnectionError


# x = HabrParser('https://career.habr.com/vacancies/rss?currency=RUR&s[]=2&s[]=3&s[]=82&s[]=4&s[]=5&s[]=72&s[]=1&s[]=6&s[]=77&s[]=83&s[]=86&s[]=73&s[]=8&s[]=9&s[]=85&s[]=7&s[]=75&sort=relevance&type=all&with_salary=true')

