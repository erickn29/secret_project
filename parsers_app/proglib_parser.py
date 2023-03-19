import datetime
# from .base_parser import BaseParser
# from .analyzer import Analyzer
# from requests import request
# from bs4 import BeautifulSoup as bs
# import re
# import time
# import random
# import json
# from tqdm import tqdm

month_mapping = {
    'марта': 'March',
    'апреля': 'April',
    'мая': 'May',
    'июня': 'June',
    'июля': 'July',
    'августа': 'August',
    'сентября': 'September',
    'октября': 'October',
    'ноября': 'November',
    'декабря': 'December',
    'января': 'January',
    'февраля': 'February',
}


def get_vacancy_date(date: str) -> datetime:
    date_list = date.split()
    return datetime.datetime.strptime(f'{date_list[0]} {month_mapping.get(date_list[1])} {date_list[2]}',
                                      '%d %B %Y').strftime('%Y-%m-%d')


current_date = datetime.datetime.now().strftime('%Y-%m-%d')
print(get_vacancy_date('19 марта 2023') == current_date)
