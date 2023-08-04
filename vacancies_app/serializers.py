from .models import *
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'country', 'city']


class StackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StackTools
        fields = ['name', 'count', ]


class VacancyListSerializer(serializers.HyperlinkedModelSerializer):
    stack = serializers.StringRelatedField(many=True)
    company = CompanySerializer()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['link'] = representation['link'].replace('arkhangelsk.', '').split('?')[0]
        representation['date'] = datetime.strftime(datetime.strptime(representation['date'], '%Y-%m-%d'), '%d.%m.%Y')
        if representation['salary_from']:
            representation['salary_from'] = list(str(representation['salary_from']))
            representation['salary_from'].insert(-3, ' ')
            representation['salary_from'] = ''.join(representation['salary_from'])
        if representation['salary_to']:
            representation['salary_to'] = list(str(representation['salary_to']))
            representation['salary_to'].insert(-3, ' ')
            representation['salary_to'] = ''.join(representation['salary_to'])
        return representation

    class Meta:
        model = Vacancy
        fields = [
            'id',
            'title',
            # 'text',
            'salary_from',
            'salary_to',
            'is_remote',
            'speciality',
            'experience',
            'grade',
            'stack',
            'company',
            'date',
            'link'
        ]


class SpecialitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['speciality', ]


class GradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['grade', ]


class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['experience', ]


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['city', ]


class CityListSerializer(serializers.Serializer):
    cities = serializers.CharField()


class VacancySerializer(serializers.ModelSerializer):
    stack = serializers.StringRelatedField(many=True)
    company = CompanySerializer()

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
