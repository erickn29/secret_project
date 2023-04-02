from django.urls import path, include
from . import api_views
# from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


# router = routers.DefaultRouter()
# router.register(r'vacancies_list', views.VacancyListViewSet)
# # router.register(r'vacancy', views.VacancyViewSet)


urlpatterns = [
    path('vacancies/', api_views.VacancyListViewSet.as_view()),
    path('specialities/', api_views.SpecialityListViewSet.as_view()),
    path('specialities_by_list/', api_views.specialities_list),
    path('languages_by_list/', api_views.languages_list),
    path('grades/', api_views.GradeListViewSet.as_view()),
    path('grades_by_list/', api_views.grades_list),
    path('cities/', api_views.CityListViewSet.as_view()),
    path('cities_by_list/', api_views.cities_list),
    path('experiences/', api_views.ExperienceListViewSet.as_view()),
    path('experiences_by_list/', api_views.experiences_list),
    path('stacktools/', api_views.StackListViewSet.as_view()),
    path('vacancies/search', api_views.VacancyListViewSet.as_view()),
    path('vacancies/<int:pk>/', api_views.VacancyViewSet.as_view()),
    path('test/', api_views.test, name='test'),
    # path('vacancies/get_hh_vacancies/<parser_token>', views.get_hh_vacancies, name='get_hh_vacancies'),
    # path('vacancies/get_habr_vacancies/<parser_token>', views.get_habr_vacancies, name='get_habr_vacancies'),
    # path('vacancies/get_superjob_vacancies/<parser_token>', views.get_superjob_vacancies, name='get_superjob_vacancies'),
    # path('vacancies/get_getmatch_vacancies/<parser_token>', views.get_getmatch_vacancies, name='get_getmatch_vacancies'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
