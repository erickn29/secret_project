from .models import Vacancy, Language, Company


def cities_list():
    cities_raw: list[str] = list(Company.objects.distinct('city').values_list('city', flat=True))
    cities = []
    for city in cities_raw:
        if city:
            new_city = city.split(',')[0].strip()
            if new_city not in cities and not city.isdigit():
                cities.append(new_city)
    return cities[1:]


def grades_list():
    grades = list(Vacancy.objects.distinct('grade').values_list('grade', flat=True).exclude(grade__isnull=True))
    return grades


def experiences_list():
    experiences = list(Vacancy.objects.distinct('experience').values_list('experience', flat=True))
    return experiences


def specialities_list():
    specialities = list(Vacancy.objects.distinct('speciality').values_list('speciality', flat=True).exclude(speciality__isnull=True))
    return specialities


def languages_list():
    languages = ['Python', 'PHP', 'C', 'C++', 'C#', 'JavaScript', 'Java']
    return languages
