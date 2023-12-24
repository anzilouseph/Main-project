# forms.py
from django import forms
from .models import vaccancy

class VacancyForm(forms.ModelForm):
    class Meta:
        model = vaccancy
        fields = ['job', 'Vaccancy', 'qualification', 'exp', 'salary', 'details']
