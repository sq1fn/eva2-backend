from django import forms
from Aplicacion.models import Doctor

class FormDoctor(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'