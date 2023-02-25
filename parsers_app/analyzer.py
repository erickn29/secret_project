class Analyzer:

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

    SPECIALITIES = {
        'DevOps-инженер': ('devops', 'девопс'),
        'Аналитик': ('аналитик',),
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
    def get_speciality(title: str, text: str):
        for k, v in Analyzer.SPECIALITIES.items():
            for item in v:
                if item in title.lower():
                    return k
        for k, v in Analyzer.SPECIALITIES.items():
            for item in v:
                if item in text.lower():
                    return k
        return None

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
        return None

    @staticmethod
    def get_experience(text: str):
        for k, v in Analyzer.HH_EXPERIENCE.items():
            if text in v:
                return k
        return None

