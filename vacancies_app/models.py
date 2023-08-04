from datetime import datetime, timedelta

from django.db import models
from django.db.models import DO_NOTHING, UniqueConstraint, Q


class StackTools(models.Model):
    name = models.CharField(max_length=128)
    count = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=32)

    class META:
        db_table = 'vacancies_app_language'


class Company(models.Model):
    name = models.CharField(max_length=128, default='МИАЦ')
    country = models.CharField(max_length=32, default='Россия', null=True)
    city = models.CharField(max_length=255, default='Москва', null=True)

    def __str__(self):
        return f'{self.name} / Город: {self.city}'


class CustomManager(models.Manager):
    def get_actual_vacancies(self):
        start_date = datetime.now().date() - timedelta(days=30)
        end_date = datetime.now().date()
        return self.filter(
            Q(date__range=[start_date, end_date]) &
            Q(
                Q(salary_from__isnull=False) | Q(salary_to__isnull=False)
            )
        )


class Vacancy(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True)
    is_remote = models.BooleanField(default=False)
    salary_from = models.PositiveIntegerField(null=True)
    salary_to = models.PositiveIntegerField(null=True)
    speciality = models.CharField(max_length=64, null=True)
    experience = models.CharField(max_length=32)
    grade = models.CharField(max_length=16, null=True)
    stack = models.ManyToManyField(StackTools)
    link = models.URLField(null=True)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING, null=True)
    date = models.DateField(auto_now=True)
    update = models.DateField(null=True)

    objects = CustomManager()

    class Meta:
        indexes = [models.Index(fields=['salary_from', 'salary_to', 'speciality', 'date']), ]
        unique_together = ('title', 'salary_from', 'salary_to', 'company')

    def __str__(self):
        return self.title
