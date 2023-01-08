from django.urls import path, include
from . import views
# from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


# router = routers.DefaultRouter()
# router.register(r'vacancies_list', views.VacancyListViewSet)
# # router.register(r'vacancy', views.VacancyViewSet)


urlpatterns = [
    path('vacancies/', views.VacancyListViewSet.as_view()),
    path('specialities/', views.SpecialityListViewSet.as_view()),
    path('grades/', views.GradeListViewSet.as_view()),
    path('cities/', views.CityListViewSet.as_view()),
    path('experiences/', views.ExperienceListViewSet.as_view()),
    path('stacktools/', views.StackListViewSet.as_view()),
    path('vacancies/search', views.VacancyListViewSet.as_view()),
    path('vacancies/<int:pk>/', views.VacancyViewSet.as_view()),
    # path('fake_db/<int:count>', views.fake_db, name='fake_db'),
    path('test/', views.test, name='test'),
    path('vacancies/get_hh_vacancies/<parser_token>', views.get_hh_vacancies, name='get_hh_vacancies')
]

urlpatterns = format_suffix_patterns(urlpatterns)
