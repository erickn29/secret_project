from .models import Vacancy, StackTools
from rest_framework import serializers


class VacancyListSerializer(serializers.HyperlinkedModelSerializer):
    stack = serializers.StringRelatedField(many=True)

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
            'stack',
            'date',
        ]


class StackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StackTools
        fields = ['name', ]


class VacancySerializer(serializers.HyperlinkedModelSerializer):
    stack = serializers.StringRelatedField(many=True)

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
            'stack',
            'date',
        ]

        # extra_kwargs = {
        #     'stack': {'view_name': 'accounts', 'lookup_field': 'account_name'},
        #     # 'users': {'lookup_field': 'username'}
        # }
