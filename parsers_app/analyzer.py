from bs4 import BeautifulSoup

from vacancies_app.models import StackTools, Language


class Analyzer:

    LANGUAGES = ['Python', 'PHP', 'C++', 'C#', 'JavaScript', 'Java', 'Golang', 'Swift', 'Kotlin', 'Rust']

    GRADES = {
        'Trainee': ['trainee', 'стажер', 'стажёр'],
        'Junior': ['junior', 'джуниор'],
        'Middle': ['middle', 'миддл'],
        'Senior': ['senior', 'сеньор', 'сениор'],
        'Lead': ['lead', 'лид', 'тимлид', 'тим лид']
    }

    HH_EXPERIENCE = {
        'нет опыта': 'не требуется',
        'от 1 года': '1–3 года',
        'от 3 лет': '3–6 лет',
        'более 5 лет': 'более 6 лет'
    }

    HABR_EXPERIENCE = {
        'Trainee': 'нет опыта',
        'Junior': 'от 1 года',
        'Middle': 'от 3 лет',
        'Senior': 'более 5 лет',
        'Lead': 'более 5 лет'
    }

    SUPERJOB_EXPERIENCE = {
        'Опыт работы не требуется': 'нет опыта',
        'Опыт работы от 1 года': 'от 1 года',
        'Опыт работы от 3 лет': 'от 3 лет',
        'Опыт работы от 5 лет': 'более 5 лет',
    }

    SPECIALITIES = {
        'DevOps-инженер': ('devops', 'девопс'),
        'Аналитик': ('аналитик', 'analyst'),
        'Арт-директор': ('арт-директор', 'арт директор'),
        'Бизнес-аналитик': ('бизнес-аналитик', 'бизнес аналитик'),
        'Гейм-дизайнер': ('гейм-дизайнер', 'гейм дизайнер'),
        'Дата-сайентист': ('дата-сайентист', 'дата сайентист', 'data engineer', 'analyst', 'базами данных', 'базы данных',
                           'баз данных', 'data'),
        'Директор по информационным технологиям (CIO)': ('директор по информационным технологиям',),
        'Менеджер продукта': ('менеджер продукта',),
        'Методолог': ('методолог',),
        'Программист': ('программист', 'разработчик', 'веб-разработчик', 'developer', 'frontend-разработчик',
                        'инженер-программист', 'backend-разработчик', 'бекенд-программист', 'backend', 'frontend',
                        'web-программист', 'fullstack-разработчик', 'фронтенд-разработчик', 'мидл-разработчик',
                        'backend-developer', 'программист-разработчик', 'инженер-разработчик', 'ml-разработчик'),
        'Продуктовый аналитик': ('продуктовый аналитик',),
        'Руководитель группы разработки': ('руководитель группы разработки', 'lead', 'руководитель группы', 'тимлид', 'teamlead'),
        'Руководитель отдела аналитики': ('руководитель отдела аналитики',),
        'Руководитель проектов': ('руководитель проектов',),
        'Сетевой инженер': ('сетевой инженер',),
        'Системный администратор': ('системный администратор', 'linux-администратор'),
        'Системный аналитик': ('системный аналитик', 'system analyst'),
        'Системный инженер': ('системный инженер',),
        'Специалист по информационной безопасности': ('специалист по информационной безопасности', 'pentest'),
        'Тестировщик': ('тестировщик', 'qa', 'qa-специалист', 'автотестировщик', 'тестированию'),
        'Верстальщик': ('верстальщик', 'html-верстальщик'),
        'Технический директор(CTO)': ('технический директор',),
        'Технический писатель': ('технический писатель',),
    }

    @staticmethod
    def html_to_text(html: BeautifulSoup) -> str:
        new_text = ''
        for e in html.descendants:
            if isinstance(e, str):
                new_text += e
            elif e.name in ['br', 'p', 'h1', 'h2', 'h3', 'h4', 'tr', 'th']:
                new_text += '\n'
            elif e.name == 'li':
                new_text += '\n- '
        return new_text

    @staticmethod
    def get_language(title: str, text: str, stack: list = None):
        for lang in Analyzer.LANGUAGES:
            if lang in title:
                obj = Language.objects.get_or_create(name=lang)[0]
                return obj
        if stack:
            for lang in Analyzer.LANGUAGES:
                if lang in stack:
                    obj = Language.objects.get_or_create(name=lang)[0]
                    return obj
        for lang in Analyzer.LANGUAGES:
            if lang in text:
                obj = Language.objects.get_or_create(name=lang)[0]
                return obj
        return

    @staticmethod
    def get_speciality(title: str, text: str):
        for k, v in Analyzer.SPECIALITIES.items():
            for item in v:
                if item in title.lower():
                    return k
        for k, v in Analyzer.SPECIALITIES.items():
            for item in v:
                if item in text.lower():
                    return k
        return

    @staticmethod
    def get_grade(title: str, text: str):
        for word in title.split(' '):
            for k, v in Analyzer.GRADES.items():
                if word.lower() in v:
                    return k
        for word in text.split(' '):
            for k, v in Analyzer.GRADES.items():
                if word.lower() in v:
                    return k
        return

    @staticmethod
    def get_experience(text: str):
        for k, v in Analyzer.HH_EXPERIENCE.items():
            if text in v:
                return k
        return

    @staticmethod
    def get_superjob_experience(text: str):
        for k, v in Analyzer.SUPERJOB_EXPERIENCE.items():
            if k in text:
                return v
        return

    @staticmethod
    def get_getmatch_experience(text: str):
        for k, v in Analyzer.HABR_EXPERIENCE.items():
            if k in text:
                return v
        return

    @staticmethod
    def get_stack_raw_text(text: str):
        from parsers_app.base_parser import BaseParser
        stack_values = list(StackTools.objects.values_list('name', flat=True))
        stack_list = []
        cleaned_text = BaseParser.text_cleaner(text).lower()
        for stack in stack_values:
            if stack.lower() in cleaned_text and len(stack) > 1 and stack not in stack_list:
                stack_list.append(stack)
        return stack_list

    @staticmethod
    def get_experience_raw_text(text: str):
        from parsers_app.base_parser import BaseParser
        cleaned_text = BaseParser.text_cleaner(text).lower()

