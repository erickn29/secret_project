from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('vacancies_app.api_urls')),
    path('', include('vacancies_app.urls')),
    path('parsers/', include('parsers_app.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
