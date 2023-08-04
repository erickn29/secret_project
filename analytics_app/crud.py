from vacancies_app.models import Vacancy, Language


langs_mapping = {
    'Python': 'Python',
    'Java': 'Java',
    'JavaScript': 'JavaScript',
    'PHP': 'php',
    'C#': 'Csharp',
    'C++': 'Cplus',
    'Golang': 'Golang',
    'Kotlin': 'Kotlin',
    'Swift': 'Swift',
    'Rust': 'Rust'
}


def get_unique_langs() -> list:
    result = list(Language.objects.values_list('name', flat=True))
    return result
