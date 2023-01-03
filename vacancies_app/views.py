from django.shortcuts import render
from django.http import HttpResponse
from .vacancies_generator import vacancy_generator
from .models import *
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import VacancySerializer


class VacancyViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view vacancies list
    """
    queryset = Vacancy.objects.all().order_by('-date')
    serializer_class = VacancySerializer
    # permission_classes = [permissions.IsAuthenticated]


def fake_db(request, count):
    vacancies = vacancy_generator(count)
    for vacancy in vacancies:
        vacancy_obj = Vacancy.objects.get_or_create(
            title=vacancy.get('title'),
            text=vacancy.get('text'),
            salary_from=vacancy.get('salary_from'),
            salary_to=vacancy.get('salary_to'),
            speciality=vacancy.get('speciality'),
            experience=vacancy.get('experience'),
            grade=vacancy.get('grade'),
        )[0]
        vacancy_obj.save()
        for stack in vacancy['stack'].split(','):
            stack_obj = StackTools.objects.get_or_create(
                name=stack,
                category=StackToolsCategory.objects.get_or_create(name='категория')[0],
            )[0]
            stack_obj.save()
            vacancy_obj.stack.add(stack_obj)
    return HttpResponse('DONE!')
