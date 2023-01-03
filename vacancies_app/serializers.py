from .models import Vacancy
from rest_framework import serializers


class VacancyListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacancy
        fields = [
            'id',
            'title',
            # 'text',
            'salary_from',
            'salary_to',
            # 'speciality',
            'experience',
            'grade',
            # 'link',
            'date',
        ]


class VacancySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacancy
        fields = [
            'id',
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