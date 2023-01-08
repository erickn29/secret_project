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
from .serializers import *
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
        if len(request.GET) > 0:
            data = request.GET
            queryset = Vacancy.objects.all()
            logger.debug(f'Размер queryset = {len(queryset)}')
            if data.get('language'):
                language = data.get('language')
                queryset = queryset.filter(Q(title__icontains=language) | Q(text__icontains=language))
                logger.debug(f'Размер queryset = {len(queryset)}')
            if data.get('salary_from'):
                salary_from = data.get('salary_from', 0)
                queryset = queryset.filter(Q(salary_from__gte=int(salary_from)) | Q(salary_from=None, salary_to__gte=salary_from))
                logger.debug(f'Размер queryset = {len(queryset)}')
            if data.get('location'):
                location = data.get('location')
                queryset = queryset.filter(company__city__icontains=location)
                logger.debug(f'Размер queryset = {len(queryset)}')
            if data.get('is_remote'):
                is_remote = data.get('is_remote')
                queryset = queryset.filter(is_remote=is_remote)
                logger.debug(f'Размер queryset = {len(queryset)}')
            if data.get('experience'):
                experience = data.get('experience').replace(', ', ',').replace(' , ', ',').replace(' ,', ',').split(',')
                queryset = queryset.filter(experience__in=experience)
                logger.debug(f'Размер queryset = {len(queryset)}')
            if data.get('speciality'):
                speciality = data.get('speciality').replace(', ', ',').replace(' , ', ',').replace(' ,', ',').split(',')
                queryset = queryset.filter(speciality__in=speciality)
                logger.debug(f'Размер queryset = {len(queryset)}')
            if data.get('grade'):
                grade = data.get('grade').replace(', ', ',').replace(' , ', ',').replace(' ,', ',').split(',')
                queryset = queryset.filter(grade__in=grade)
                logger.debug(f'Размер queryset = {len(queryset)}')
            self.queryset = queryset
        return self.list(request, *args, **kwargs)


class VacancyViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class SpecialityListViewSet(generics.ListCreateAPIView):
    queryset = Vacancy.objects.distinct('speciality')
    serializer_class = SpecialitySerializer


class GradeListViewSet(generics.ListCreateAPIView):
    queryset = Vacancy.objects.distinct('grade')
    serializer_class = GradeSerializer


class CityListViewSet(generics.ListCreateAPIView):
    queryset = Company.objects.distinct('city')
    serializer_class = CitySerializer


class ExperienceListViewSet(generics.ListCreateAPIView):
    queryset = Vacancy.objects.distinct('experience')
    serializer_class = ExperienceSerializer


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
