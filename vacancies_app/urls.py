from django.urls import path
from . import views

urlpatterns = [
    path('', views.vacancies_list, name='vacancies_list'),
    path('fake_db/<int:count>', views.fake_db, name='fake_db')
]
