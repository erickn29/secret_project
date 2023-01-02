from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('job/', include('vacancies_app.urls')),
    path('admin/', admin.site.urls),
]
