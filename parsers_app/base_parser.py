from requests import request
from tqdm import tqdm
from vacancies_app.models import *
from .analyzer import Analyzer


class BaseParser:

    # GRADES = {
    #     'trainee': ['trainee', 'стажер'],
    #     'junior': ['junior', 'джуниор'],
    #     'middle': ['middle', 'миддл'],
    #     'senior': ['senior', 'сеньор', 'сениор'],
    #     'lead': ['lead', 'лид']
    # }

    HH_LINK = 'https://arkhangelsk.hh.ru/search/vacancy?area=113&employment=full&excluded_text=%D0%BC%D0%B5%D0%BD%D0%B5%D0%B4%D0%B6%D0%B5%D1%80%2C%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%2C%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%BA%D0%B0%2C%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%BA%D0%B8&search_field=name&search_field=description&only_with_salary=true&text=python+OR+php+OR+c%2B%2B+OR+c%23+OR+javascript+OR+java&no_magic=true&L_save_area=true&search_period=1&items_on_page=20&hhtmFrom=vacancy_search_list'
    HABR_LINK = 'https://career.habr.com/vacancies/rss?currency=RUR&s[]=2&s[]=3&s[]=82&s[]=4&s[]=5&s[]=72&s[]=1&s[]=6&s[]=77&s[]=83&s[]=86&s[]=73&s[]=8&s[]=9&s[]=85&s[]=7&s[]=75&sort=relevance&type=all&with_salary=true'
    SUPERJOBLINK = 'https://russia.superjob.ru/vacancy/search/?keywords=c%23%2Cpython%2Cjavascript%2Cphp%2Cc%2B%2B%2Cjava&payment_value=20000&period=1&payment_defined=1&click_from=facet'
    GETMATCH_LINK = 'https://getmatch.ru/vacancies?sa=150000&l=moscow&l=remote&l=saints_p&pa=1d&s=landing_ca_header'
    PROGLIB_LINK = 'https://proglib.io/vacancies/all?direction=Programming&workType=fulltime&workPlace=all&experience=100&salaryFrom=500&page=1'
    STOP_WORDS = ('машинист', 'водитель', 'таксист', 'курьер', 'охранник', 'поддержки', 'оператор', 'поддержка', 'маркетолог')

    def __init__(self, url: str):
        self.url = url
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'accept-encoding': 'gzip,deflate,br',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }

    def _get_vacancies_list_html(self):
        """Получаем начальную страницу сайта с поиском"""
        try:
            response = request(method='GET', url=self.url, headers=self.headers)
            if response.ok:
                return response.text
        except Exception as e:
            print(e)
            return

    @staticmethod
    def string_cleaner(string: str):
        return string.strip().replace('  ', '').replace('\n', ' ').replace('\t', '').replace('\xa0', ' ')

    @staticmethod
    def text_cleaner(string: str):
        mapping = {
            ord(','): None,
            ord('.'): None,
            ord(':'): None,
            ord(';'): None,
            ord('\''): None,
            ord('\"'): None,
            # ord('<p>'): None,
            # ord('</p>'): None,
            # ord('<br>'): None,
            ord('•'): None,
            ord('('): None,
            ord(')'): None,
        }
        return string.translate(mapping).replace('<p>', '').replace('</p>', '').replace('<br>', '')

    # @staticmethod
    def vacancies_to_db(self, vacancies_dict: dict):
        for vacancy in tqdm(vacancies_dict['vacancies']):
            if not (set(vacancy.get('title').lower().split()) & set(self.STOP_WORDS)):
                try:
                    company_obj = Company.objects.get_or_create(
                        name=vacancy.get('company'),
                        country='Россия',
                        city=vacancy.get('company_address'),
                    )[0]
                    vacancy_obj = Vacancy.objects.get_or_create(
                        title=vacancy.get('title'),
                        text=vacancy.get('text'),
                        company=company_obj,
                        is_remote=vacancy.get('is_remote'),
                        salary_from=vacancy.get('salary_from'),
                        salary_to=vacancy.get('salary_to'),
                        speciality=Analyzer.get_speciality(vacancy.get('title'), vacancy.get('text')),
                        experience=vacancy.get('experience'),
                        grade=vacancy.get('grade'),
                        link=vacancy.get('link'),
                    )[0]
                    if vacancy.get('stack'):
                        for stack in vacancy.get('stack'):
                            stack_obj = StackTools.objects.get_or_create(
                                name=stack,
                            )[0]
                            if stack_obj.count:
                                stack_obj.count += 1
                            else:
                                stack_obj.count = 1
                            stack_obj.save()
                            vacancy_obj.stack.add(stack_obj)
                except Exception as e:
                    print(e)
                    continue
