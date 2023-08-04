from django.urls import path
from . import api_views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('vacancies/', api_views.VacancyListViewSet.as_view()),
    path('specialities_by_list/', api_views.get_specialities_list),
    path('languages_by_list/', api_views.get_languages_list),
    path('grades_by_list/', api_views.get_grades_list),
    path('cities_by_list/', api_views.get_cities_list),
    path('experiences_by_list/', api_views.get_experiences_list),
    path('vacancies/<int:pk>/', api_views.VacancyViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
