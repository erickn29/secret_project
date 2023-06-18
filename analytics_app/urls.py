from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_stat, name='main_stat')
]
