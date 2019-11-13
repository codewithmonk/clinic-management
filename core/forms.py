from django import forms
from .models import Patient, CaseSheet, StockManagement


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
        )


class PatientRecordForm(forms.ModelForm):
    class Meta:
        model = CaseSheet
        fields = (
            'complaints',
            'history',
            # examination
            'height',
            'weight',
            'pulse',
            'blood_pressure',
            'heart_rate',
            'other_examination',
            # Ashtashthana Pareeksha
            'nadi',
            'jihwa',
            'mutra',
            'drik',
            'malam',
            'sabdam',
            'akriti',
            'sparsha',
            # dasavidha pareeksha
            'dushyam',
            'desha',
            'bala',
            'kala',
            'anala',
            'prakriti',
            'vaya',
            'satwa',
            'sathmya',
            'ahara',
            # doctor's content
            'investigations',
            'diagnosis',
            'prescriptions',
            'treatments',
        )


class StockForm(forms.ModelForm):
    class Meta:
        model = StockManagement
        fields = (
            'quantity',
            'medicine_name',
            'medicine_category',
            'manufacturer',
            'unit_price'
        )
