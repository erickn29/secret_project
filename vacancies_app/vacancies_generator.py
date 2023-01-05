import random

title = ['программист', 'разработчик', 'компьютерщик']
text = 'Тут будет описание вакансии...'
language = ['Python', 'C#', 'JavaScript', 'Java', 'C++', 'Kotlin', 'PHP']
stack = ['git', 'docker', 'drf', 'react', 'fastAPI', '.Net core', 'Postrgesql', 'MySQL']
grade = ['trainee', 'junior', 'middle', 'senior', 'lead']
speciality = ['разработчик', 'дата-сайентист', 'DevOps']
experience = ['нет опыта', 'от 1 года', 'от 3 лет', 'более 5 лет']


def vacancy_generator(count: int) -> list:
    vacancies_list = []
    for i in range(count):
        salary_from = random.choice([None, random.randint(30, 500)])
        salary_to = random.choice([None, random.randint(salary_from if salary_from else 0, 500)])
        buffer = {}
        buffer.update({'title': f'{random.choice(language)} {random.choice(title)}'})
        buffer.update({'text': text})
        buffer.update({'salary_from': salary_from * 1000 if salary_from else salary_from})
        buffer.update({'salary_to': salary_to * 1000 if salary_to else salary_to})
        buffer.update({'stack': ','.join(set(stack[random.randint(0, len(stack) - 1)] for _ in range(random.randint(1, len(stack) - 1))))})
        buffer.update({'grade': f'{random.choice(grade)}'})
        buffer.update({'speciality': random.choice(speciality)})
        buffer.update({'experience': random.choice(experience)})
        vacancies_list.append(buffer)
        buffer = {}
    return vacancies_list


# for item in vacancy_generator(5):
#     print(item)
