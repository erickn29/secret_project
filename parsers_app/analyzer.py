class Analyzer:

    GRADES = {
        'Trainee': ['trainee', 'стажер'],
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

    SPECIALITIES = {
        'DevOps-инженер': ('devops', 'девопс'),
        'Аналитик': ('аналитик',),
        'Арт-директор': ('арт-директор', 'арт директор'),
        'Бизнес-аналитик': ('бизнес-аналитик', 'бизнес аналитик'),
        'Гейм-дизайнер': ('гейм-дизайнер', 'гейм дизайнер'),
        'Дата-сайентист': ('дата-сайентист', 'дата сайентист'),
        'Директор по информационным технологиям (CIO)': ('директор по информационным технологиям',),
        'Менеджер продукта': ('менеджер продукта',),
        'Методолог': ('методолог',),
        'Программист': ('программист', 'разработчик'),
        'Продуктовый аналитик': ('продуктовый аналитик',),
        'Руководитель группы разработки': ('руководитель группы разработки',),
        'Руководитель отдела аналитики': ('руководитель отдела аналитики',),
        'Руководитель проектов': ('руководитель проектов',),
        'Сетевой инженер': ('сетевой инженер',),
        'Системный администратор': ('системный администратор',),
        'Системный аналитик': ('системный аналитик',),
        'Системный инженер': ('системный инженер',),
        'Специалист по информационной безопасности': ('специалист по информационной безопасности',),
        'Тестировщик': ('тестировщик',),
        'Технический директор(CTO)': ('технический директор',),
        'Технический писатель': ('технический писатель',),
    }

    @staticmethod
    def get_speciality(title: str, text: str):
        for word in title.split(' '):
            for k, v in Analyzer.SPECIALITIES.items():
                if word.lower() in v:
                    return k
        for word in text.split(' '):
            for k, v in Analyzer.SPECIALITIES.items():
                if word.lower() in v:
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

