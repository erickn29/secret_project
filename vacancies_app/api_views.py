from pathlib import Path
from rest_framework.decorators import api_view
# from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics
from dotenv import load_dotenv
from miac_logger.logger import BaseLogger
from . import crud


load_dotenv()
logger = BaseLogger(current_file=Path(__file__).name)


class VacancyListViewSet(generics.ListCreateAPIView):
    queryset = Vacancy.objects.get_actual_vacancies()
    serializer_class = VacancyListSerializer

    def get_queryset(self):
        start_date = datetime.now().date() - timedelta(days=30)
        end_date = datetime.now().date()
        queryset = super().get_queryset()
        queryset = queryset.filter(
            Q(date__range=[start_date, end_date]) &
            (
                Q(salary_from__isnull=False) |
                Q(salary_to__isnull=False)
            )
        ).order_by('-date')
        if len(self.request.GET) > 0:
            data = self.request.GET
            print(data)
            if data.get('language'):
                queryset = queryset.filter(language=Language.objects.get(name=str(data.get('language'))))
                # logger.debug(f'Размер queryset = {len(queryset)}')
            if data.get('salary_from'):
                salary_from = data.get('salary_from', 0)
                queryset = queryset.filter(Q(salary_from__gte=int(salary_from)) | Q(salary_from=None, salary_to__gte=salary_from))
                # logger.debug(f'Размер queryset = {len(queryset)}')
            if data.get('location'):
                location = data.get('location')
                queryset = queryset.filter(company__city__icontains=location)
                # logger.debug(f'Размер queryset = {len(queryset)}')
            if data.get('is_remote'):
                if data.get('is_remote') == 'true':
                    queryset = queryset.filter(is_remote=True)
                # logger.debug(f'Размер queryset = {len(queryset)}')
            if data.get('experience'):
                experience = data.get('experience').replace(', ', ',').replace(' , ', ',').replace(' ,', ',').split(',')
                queryset = queryset.filter(experience__in=experience)
                # logger.debug(f'Размер queryset = {len(queryset)}')
            if data.get('speciality'):
                speciality = data.get('speciality').replace(', ', ',').replace(' , ', ',').replace(' ,', ',').split(',')
                queryset = queryset.filter(speciality__in=speciality)
                # logger.debug(f'Размер queryset = {len(queryset)}')
            if data.get('grade'):
                grade = data.get('grade').replace(', ', ',').replace(' , ', ',').replace(' ,', ',').split(',')
                queryset = queryset.filter(grade__in=grade)
                # logger.debug(f'Размер queryset = {len(queryset)}')
            if data.get('date'):
                queryset = queryset.filter(date=datetime.strptime(data.get('date'), '%Y-%m-%d'))
                # logger.debug(f'Размер queryset = {len(queryset)}')
        return queryset.order_by('-date')


class VacancyViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    # permission_classes = [IsAdminUser, ]


@api_view(['GET'])
def get_cities_list(request):
    if request.method == 'GET':
        cities = crud.cities_list()
        return Response({'result': cities})


@api_view(['GET'])
def get_grades_list(request):
    if request.method == 'GET':
        grades = crud.grades_list()
        return Response({'result': grades})


@api_view(['GET'])
def get_experiences_list(request):
    if request.method == 'GET':
        experiences = crud.experiences_list()
        return Response({'result': experiences})


@api_view(['GET'])
def get_specialities_list(request):
    if request.method == 'GET':
        specialities = crud.specialities_list()
        return Response({'result': specialities})


@api_view(['GET'])
def get_languages_list(request):
    if request.method == 'GET':
        languages = ['Python', 'PHP', 'C', 'C++', 'C#', 'JavaScript', 'Java']
        return Response({'result': languages})
