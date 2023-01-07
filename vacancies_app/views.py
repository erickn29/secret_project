import json
import re
from pathlib import Path

from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .vacancies_generator import vacancy_generator
from .models import *
# from rest_framework import viewsets
# from rest_framework import permissions
from .serializers import VacancyListSerializer, VacancySerializer
from rest_framework import generics
from parsers_app.hh_parser import HhParser
from parsers_app.base_parser import BaseParser
from dotenv import load_dotenv
import os
from miac_logger.logger import BaseLogger

load_dotenv()
logger = BaseLogger(current_file=Path(__file__).name)


# class VacancyListViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to view vacancies list
#     """
#     queryset = Vacancy.objects.all().order_by('-date')
#     serializer_class = VacancyListSerializer
#     # permission_classes = [permissions.IsAuthenticated]
#
#
# class VacancyViewSet(viewsets.ModelViewSet):
#     queryset = Vacancy.objects.get(id=6)
#     serializer_class = VacancySerializer


class VacancyListViewSet(generics.ListCreateAPIView):
    # print(Path(__file__).name)
    # logger.error('error')
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer

    def get(self, request, *args, **kwargs):
        exp_list = ['нет опыта', 'от 1 года', 'от 3 лет', 'более 5 лет']
        cities = set(sum(Company.objects.values_list('city'), ()))
        city_list = set()
        for el in cities:
            if isinstance(el, str):
                city_list.add(el.split(',')[0].strip())
            else:
                city_list.add(el)
        if len(request.GET) > 0:
            data = request.GET
            salary_from = data.get('salary_from', 0)
            experience = data.get('experience')
            location = data.get('location', '[а-яА-Я]')
            grade = data.get('grade', '[a-zA-z]')
            self.queryset = Vacancy.objects.filter(
                Q(salary_from__gte=int(salary_from)) | Q(salary_from=None, salary_to__gte=salary_from),
                Q(experience=experience) | Q(experience__isnull=False),
                Q(company__city__regex=rf'{location}') | Q(company__city__isnull=True) & Q(company__country__regex=rf'{location}'),  # Не баг, а фича
                Q(grade__regex=rf'{grade}') | Q(grade__isnull=True) & Q(company__country__regex=rf'{location}'),  # Не баг, а фича №2
            )
        return self.list(request, *args, **kwargs)


class VacancyViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


def fake_db(request, count):
    vacancies = vacancy_generator(count)
    for vacancy in vacancies:
        company_obj = Company.objects.get_or_create(
            name='МИАЦ',
            country='Россия',
            city='Архангельск',
        )[0]
        vacancy_obj = Vacancy.objects.get_or_create(
            title=vacancy.get('title'),
            text=vacancy.get('text'),
            salary_from=vacancy.get('salary_from'),
            salary_to=vacancy.get('salary_to'),
            speciality=vacancy.get('speciality'),
            experience=vacancy.get('experience'),
            grade=vacancy.get('grade'),
            company=company_obj,
        )[0]
        vacancy_obj.save()
        for stack in vacancy['stack'].split(','):
            stack_obj = StackTools.objects.get_or_create(
                name=stack,
            )[0]
            stack_obj.save()
            vacancy_obj.stack.add(stack_obj)
    return HttpResponse('DONE!')


def get_hh_vacancies(request, parser_token):
    if parser_token == os.getenv('PARSER_TOKEN'):
        obj = HhParser(BaseParser.HH_LINK)
        vacancies = obj.get_vacancies()
        obj.vacancies_to_db(vacancies)
        return HttpResponse(str(vacancies))
    else:
        raise Http404
