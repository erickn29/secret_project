from .models import Vacancy
from rest_framework import serializers


class VacancySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacancy
        fields = [
            'title',
            'text',
            'salary_from',
            'salary_to',
            'speciality',
            'experience',
            'grade',
            'link',
            'date',
        ]
