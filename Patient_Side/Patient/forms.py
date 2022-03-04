from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'number'
        ]


class GetNumber(forms.Form):
    number = forms.NumberInput()
