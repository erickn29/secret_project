from django import forms
from .crud import *


class SearchForm(forms.Form):
    cities = forms.ChoiceField(choices=[(item, item) for item in cities_list()])
    specialities = forms.ChoiceField(choices=[(item, item) for item in specialities_list()])
    grades = forms.ChoiceField(choices=[(item, item) for item in grades_list()])
    experiences = forms.ChoiceField(choices=[(item, item) for item in experiences_list()])
    languages = forms.ChoiceField(choices=[(item, item) for item in languages_list()])
    is_remote = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    salary_from = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Зарплата от...'})
    )
