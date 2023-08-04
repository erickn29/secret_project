from datetime import datetime, timedelta

from django.db.models import Q
from django.template.defaultfilters import register
from django.views.generic import View, TemplateView, ListView, DetailView, FormView
from django.shortcuts import render, redirect
from .models import Vacancy, Language, Company
from .crud import *
from .forms import SearchForm


class VacanciesList(ListView):
    model = Vacancy
    template_name = 'base.html'
    context_object_name = 'vacancies'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SearchForm()
        # form.fields['cities'].initial = form.fields['cities'].choices[10]
        # form.fields['cities'].initial = ('Москва', 'Москва')
        form.fields['cities'].initial = (self.request.GET.get('location'), self.request.GET.get('location'))
        form.fields['specialities'].initial = (self.request.GET.get('speciality'), self.request.GET.get('speciality'))
        form.fields['grades'].initial = (self.request.GET.get('grade'), self.request.GET.get('grade'))
        form.fields['experiences'].initial = (self.request.GET.get('experience'), self.request.GET.get('experience'))
        form.fields['languages'].initial = (self.request.GET.get('language'), self.request.GET.get('language'))
        form.fields['salary_from'].initial = self.request.GET.get('salary_from')
        form.fields['is_remote'].initial = 'on' if self.request.GET.get('is_remote') else ''
        # for k, v in self.request.GET.items():
        #     initial[k] = v
        context['form'] = form
        context['result'] = len(self.queryset) if self.queryset else len(self.get_queryset())
        return context

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
                is_remote = True if data.get('is_remote') == 'on' else False
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
            self.queryset = queryset
        return queryset.order_by('-date')


@register.filter(name='split_link')
def split_link(value):
    return value.split('?')[0]


@register.filter(name='split_city')
def split_city(value):
    return value.split(',')[0]


@register.filter(name='del_comma')
def del_comma(value):
    if value:
        if value > 999:
            return str(value // 1000) + ' ' + str(value)[len(str(value // 1000)):]
    return value


class VacancyDetail(DetailView):
    model = Vacancy
    template_name = 'vacancy.html'
    context_object_name = 'vacancy'


# class FilterView(FormView):
#     template_name = 'components/search_form.html'
#     form_class = SearchForm
#     success_url = '/vacancies/'
#
#     def get_context_data(self, **kwargs):
#         context = super(FilterView, self).get_context_data(**kwargs)
#         context['test'] = 'self.form_class'
#         return context

    # def get_initial(self):
    #     initial = super().get_initial()
    #     for k, v in self.request.GET.items():
    #         initial[k] = v
    #     return initial
    #
    # def get(self, request, *args, **kwargs):
    #     pass
