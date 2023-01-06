from requests import request


class BaseParser:

    GRADES = {
        'trainee': ['trainee', 'стажер'],
        'junior': ['junior', 'джуниор'],
        'middle': ['middle', 'миддл'],
        'senior': ['senior', 'сеньор', 'сениор'],
        'lead': ['lead', 'лид']
    }

    HH_LINK = 'https://arkhangelsk.hh.ru/search/vacancy?area=113&employment=full&excluded_text=%D0%BC%D0%B5%D0%BD%D0%B5%D0%B4%D0%B6%D0%B5%D1%80%2C%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%2C%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%BA%D0%B0%2C%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%BA%D0%B8&search_field=name&search_field=description&only_with_salary=true&text=python+OR+php+OR+c%2B%2B+OR+c%23+OR+javascript+OR+java&no_magic=true&L_save_area=true&search_period=1&items_on_page=20&hhtmFrom=vacancy_search_list'

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
    def get_grade(title: str, text: str):
        for word in title.split(' '):
            for k, v in BaseParser.GRADES.items():
                if word.lower() in v:
                    return k
        for word in text.split(' '):
            for k, v in BaseParser.GRADES.items():
                if word.lower() in v:
                    return k
        return None
