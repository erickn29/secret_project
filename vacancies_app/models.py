from django.db import models


class StackToolsCategory(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', ], name='unique_stack_item')
        ]


class StackTools(models.Model):
    name = models.CharField(max_length=32)
    category = models.ForeignKey(StackToolsCategory, on_delete=models.CASCADE, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', ], name='unique_stack_item')
        ]

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=128, null=True)
    country = models.CharField(max_length=32, default='Россия')
    city = models.CharField(max_length=32, default='Москва')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'country'], name='unique_company')
        ]

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True)
    is_remote = models.BooleanField(default=False)
    salary_from = models.PositiveIntegerField(null=True)
    salary_to = models.PositiveIntegerField(null=True)
    speciality = models.CharField(max_length=64)
    experience = models.CharField(max_length=32)
    grade = models.CharField(max_length=16)
    stack = models.ManyToManyField(StackTools)
    link = models.URLField(null=True)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'company', 'salary_from', 'salary_to'], name='unique_vacancy')
        ]

    def __str__(self):
        return self.title
