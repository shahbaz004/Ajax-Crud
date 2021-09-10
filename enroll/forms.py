from django import forms
from .models import Student


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'mobile', 'program']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'roll': forms.TextInput(attrs={'class': 'form-control', 'id': 'rollid'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'id': 'mobileid'}),
            'program': forms.TextInput(attrs={'class': 'form-control', 'id': 'programid'}),

        }
