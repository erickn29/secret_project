from datetime import datetime, timedelta

from .models import Vacancy, Language, Company


def cities_list():
    start_date = datetime.now().date() - timedelta(days=30)
    end_date = datetime.now().date()
    vacancy = Vacancy.objects.filter(date__range=[start_date, end_date])
    company_ids = list(vacancy.values_list('company_id', flat=True))
    companies = Company.objects.filter(id__in=company_ids)
    cities_raw: list[str] = list(companies.filter().distinct('city').values_list('city', flat=True))
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
    languages = list(Language.objects.distinct('name').values_list('name', flat=True).exclude(name__isnull=True))
    return languages
