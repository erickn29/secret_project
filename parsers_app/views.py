from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from parsers_app.hh_parser import HhParser
from parsers_app.habr_parser import HabrParser
from parsers_app.superjob_parser import SuperJobParser
from parsers_app.getmatch_parser import GetMatchParser
from parsers_app.base_parser import BaseParser
from dotenv import load_dotenv
import os
from miac_logger.logger import BaseLogger


@api_view(['GET', ])
@login_required
def get_hh_vacancies(request):
    if request.user.is_superuser:
        obj = HhParser(BaseParser.HH_LINK)
        vacancies = obj.get_vacancies()
        obj.vacancies_to_db(vacancies)
        return HttpResponse(str(vacancies))
    return Response({'error': 'access denied'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', ])
@login_required
def get_habr_vacancies(request):
    if request.user.is_superuser:
        obj = HabrParser(BaseParser.HABR_LINK)
        vacancies = obj.get_vacancies()
        obj.vacancies_to_db(vacancies)
        return HttpResponse(str(vacancies))
    return Response({'error': 'access denied'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', ])
@login_required
def get_superjob_vacancies(request):
    if request.user.is_superuser:
        obj = SuperJobParser(BaseParser.SUPERJOBLINK)
        vacancies = obj.get_vacancies()
        obj.vacancies_to_db(vacancies)
        return JsonResponse(vacancies)
    return Response({'error': 'access denied'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', ])
@login_required
def get_getmatch_vacancies(request):
    if request.user.is_superuser:
        obj = GetMatchParser(BaseParser.GETMATCH_LINK)
        vacancies = obj.get_vacancies()
        obj.vacancies_to_db(vacancies)
        return JsonResponse(vacancies)
    return Response({'error': 'access denied'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', ])
@login_required
def get_proglib_vacancies(request):
    if request.user.is_superuser:
        obj = GetMatchParser(BaseParser.GETMATCH_LINK)
        vacancies = obj.get_vacancies()
        obj.vacancies_to_db(vacancies)
        return JsonResponse(vacancies)
    return Response({'error': 'access denied'}, status=status.HTTP_403_FORBIDDEN)
