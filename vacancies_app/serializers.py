from .models import *
from rest_framework import serializers


class VacancyListSerializer(serializers.HyperlinkedModelSerializer):
    stack = serializers.StringRelatedField(many=True)
    company = serializers.StringRelatedField(many=False)

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
            'company',
            'date',
        ]


class StackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StackTools
        fields = ['name', ]


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'country', 'city']


class VacancySerializer(serializers.HyperlinkedModelSerializer):
    stack = serializers.StringRelatedField(many=True)
    company = serializers.StringRelatedField(many=False)

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
            'company',
            'date',
        ]

        # extra_kwargs = {
        #     'stack': {'view_name': 'accounts', 'lookup_field': 'account_name'},
        #     # 'users': {'lookup_field': 'username'}
        # }
