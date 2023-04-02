from django.urls import path
from . import views


urlpatterns = [
    path('vacancies/', views.VacanciesList.as_view(), name='vacancies_list'),
    # path('vacancies/<int:pk>/', views.VacancyDetail.as_view(), name='vacancies_list')
]
