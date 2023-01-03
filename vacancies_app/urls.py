from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'vacancies_list', views.VacancyViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('fake_db/<int:count>', views.fake_db, name='fake_db')
]
