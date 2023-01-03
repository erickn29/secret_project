from django.urls import path, include
from . import views
# from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


# router = routers.DefaultRouter()
# router.register(r'vacancies_list', views.VacancyListViewSet)
# # router.register(r'vacancy', views.VacancyViewSet)


urlpatterns = [
    path('vacancies/', views.VacancyListViewSet.as_view()),
    path('vacancies/<int:pk>/', views.VacancyViewSet.as_view()),
    path('fake_db/<int:count>', views.fake_db, name='fake_db')
]

urlpatterns = format_suffix_patterns(urlpatterns)
