from django import forms
from .models import Patient


# To create editable form for Patient details
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('name', 'age', 'gender', 'phone', 'address')