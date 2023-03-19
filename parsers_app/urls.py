from django.urls import path
from . import views


urlpatterns = [
    path('get_hh_vacancies/', views.get_hh_vacancies, name='get_hh_vacancies'),
    path('get_habr_vacancies/', views.get_habr_vacancies, name='get_habr_vacancies'),
    path('get_superjob_vacancies/', views.get_superjob_vacancies, name='get_superjob_vacancies'),
    path('get_getmatch_vacancies/', views.get_getmatch_vacancies, name='get_getmatch_vacancies'),
]
