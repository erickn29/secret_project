import json
from datetime import datetime, timedelta

from django.db.models import Q, Count, Avg

from .crud import *

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from vacancies_app.models import Vacancy, Language
from parsers_app.analyzer import Analyzer


def main_stat(request):
    if request.method == 'GET':
        context = {
            'langs': lang_stats(),
            'profs': json.dumps(profs_stats())
        }
        return render(request, 'statistic.html', context)
    return HttpResponse(status=400)


def lang_stats():
    start_date = datetime.now().date() - timedelta(days=365)
    end_date = datetime.now().date()
    days_count = list(Vacancy.objects.filter(update__gte='2023-05-10').order_by('update').distinct('update').values_list('update', flat=True))
    langs = {}
    langs_unique = get_unique_langs()
    data_frame = {}
    for day in days_count:
        day_string = datetime.strftime(day, '%d.%m.%Y')
        for lang in langs_unique:
            data_frame.update({langs_mapping.get(lang): len(Vacancy.objects.filter(
                Q(salary_from__isnull=False) |
                Q(salary_to__isnull=False)
        ).filter(update=day, language__name=lang))})
        langs.update(
            {
                day_string: data_frame,
            }
        )
        data_frame = {}
    return json.dumps(langs)


def profs_stats():
    days_count = list(Vacancy.objects.filter(update__gte='2023-05-10').order_by('update').distinct('update').values_list('update', flat=True))
    profs_unique = list(Analyzer.SPECIALITIES)
    profs_data = {'profs': [{k: []} for k in profs_unique]}
    # profs_data = {'profs': {k: []} for k in profs_unique}
    # print(profs_data)
    dates = []
    for day in days_count:
        day_string = datetime.strftime(day, '%d.%m.%Y')
        dates.append(day_string)
        for index, prof in enumerate(profs_unique):
            count = Vacancy.objects.filter(update=day, speciality=prof).count()
            profs_data['profs'][index][prof].append(count)
    # print(dates)
    for i in range(-len(profs_data['profs']), 0):
        if sum(*list(profs_data['profs'][i].values())) < len(*list(profs_data['profs'][i].values())) * 1.5:
            del profs_data['profs'][i]
    profs_data.update({'labels': dates})
    return profs_data


def get_experience_by_lang(lang):
    queryset = Vacancy.objects.filter(language__name=lang, update__gte='2023-05-10').values('experience', 'update').annotate(count=Count('experience'))
    # labels = list(queryset.values_list('experience', flat=True))

    print(list(queryset))


def get_salary_by_lang(lang):
    queryset = Vacancy.objects.filter(language__name=lang, update__gte='2023-05-10').values('experience', 'update').annotate(count=Count('id'))
    # Получаем уникальные дни цен
    unique_days_exp = list(queryset.values_list('update', 'experience').distinct())

    filtered_prices = []

    for set_ in unique_days_exp:
        try:
            # Получаем записи только для текущего дня
            day_prices = queryset.filter(update=set_[0], experience=set_[1])
            print(day_prices)

            total_count = list(day_prices)[0]['count']
            print(total_count)
            exclude_count = int(total_count * 0.25)
            print(exclude_count)

            # Получаем 20% самых высоких цен для текущего дня
            highest_prices = list(day_prices.order_by('-salary_from').values_list('salary_from', flat=True))[:exclude_count]
            print(highest_prices)

            # Получаем 20% самых низких цен для текущего дня
            lowest_prices = list(day_prices.order_by('salary_from').values_list('salary_from', flat=True))[:exclude_count]
            print(lowest_prices)
            print('=========')

            # Исключаем записи с самыми высокими и самыми низкими ценами для текущего дня
            filtered_day_prices = day_prices.exclude(salary_from__gte=highest_prices[-1]).exclude(salary_from__lte=lowest_prices[0]).annotate(avg=Avg('salary_from')).order_by('-update')

            filtered_prices.extend(filtered_day_prices)
        except Exception as e:
            print(e)

    for item in filtered_prices:
        print(item)


def get_stack_by_lang(lang):
    pass
