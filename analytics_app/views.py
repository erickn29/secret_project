import json
from datetime import datetime, timedelta

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from vacancies_app.models import Vacancy


def main_stat(request):
    if request.method == 'GET':
        context = {
            'langs': lang_stats()
        }
        return render(request, 'statistic.html', context)
    return HttpResponse(status=400)


def lang_stats():
    start_date = datetime.now().date() - timedelta(days=365)
    end_date = datetime.now().date()
    # python = Vacancy.objects.filter(date__range=[start_date, end_date], language__name='Python')
    # javascript = Vacancy.objects.filter(date__range=[start_date, end_date], language__name='JavaScript')
    # php = Vacancy.objects.filter(date__range=[start_date, end_date], language__name='PHP')
    days_count = list(Vacancy.objects.filter(date__gte='2023-05-10').order_by('date').distinct('date').values_list('date', flat=True))
    langs = {}
    for day in days_count:
        day_string = datetime.strftime(day, '%d.%m.%Y')
        langs.update(
            {
                day_string: {
                    'Python': len(Vacancy.objects.filter(date=day, language__name='Python')),
                    'JavaScript': len(Vacancy.objects.filter(date=day, language__name='JavaScript')),
                    'Csharp': len(Vacancy.objects.filter(date=day, language__name='C#')),
                    'php': len(Vacancy.objects.filter(date=day, language__name='PHP')),
                },
            }
        )
    return json.dumps(langs)
