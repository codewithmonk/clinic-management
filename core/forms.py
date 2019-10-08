from django import forms
from .models import Patient


# To create editable form for Patient details
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = (
            'name',
            'age',
            'gender',
            'phone',
            'address',
            'nadi',
            'jihwa',
            'mutra',
            'drit',
            'malam',
            'sabdam',
            'atriti',
            'sparsha',
            'dushyam',
            'prakriti',
            'desha',
            'vaya',
            'bala',
            'satwa',
            'kala',
            'sathmaya',
            'anala',
            'ahara',
            'height',
            'weight',
            'pulse',
            'blood_pressure',
            'heart_rate',
            'other_examination'
        )