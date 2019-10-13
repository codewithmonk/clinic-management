from django import forms
from .models import Patient, CaseSheet


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
            'drik',
            'malam',
            'sabdam',
            'akriti',
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


class PatientRecordForm(forms.ModelForm):
    class Meta:
        model = CaseSheet
        fields = (
            'complaints',
            'diagnosis',
            'prescriptions',
            'treatments',
        )
