from datetime import datetime, timedelta

from django.db.models import Q
from django.template.defaultfilters import register
from django.views.generic import View, TemplateView, ListView, DetailView, FormView
from django.shortcuts import render, redirect
from .models import Vacancy, Language, Company
from .crud import *


class VacanciesList(ListView):
    model = Vacancy
    template_name = 'base.html'
    context_object_name = 'vacancies'
    extra_context = {
        'cities': cities_list(),
        'specialities': specialities_list(),
        'grades': grades_list(),
        'experiences': experiences_list(),
        'languages': languages_list(),
    }

    def get_queryset(self):
        start_date = datetime.now().date() - timedelta(days=30)
        end_date = datetime.now().date()
        queryset = super().get_queryset()
        queryset = queryset.filter(date__range=[start_date, end_date]).order_by('-date')
        if len(self.request.GET) > 0:
            data = self.request.GET
            if data.get('language'):
                print(data.get('language'))
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
                is_remote = data.get('is_remote')
                queryset = queryset.filter(is_remote=is_remote)
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
        return queryset


@register.filter(name='split_link')
def split_link(value):
    return value.split('?')[0]


@register.filter(name='split_city')
def split_city(value):
    return value.split(',')[0]


class VacancyDetail(DetailView):
    model = Vacancy
    template_name = 'vacancy.html'
    context_object_name = 'vacancy'


class FilterView(TemplateView):
    template_name = 'components/search_form.html'
    extra_context = {
        'cities': cities_list(),
    }

    # def get_context_data(self, **kwargs):

