from django.db import models
import pandas as pd
from time import timezone
import os

# Create your models here.
NONE = 'NOT WILLING TO SHARE'
MALE = 'MALE'
FEMALE = 'FEMALE'
OTHERS = 'OTHERS'

gender_choices = (
    (NONE, NONE),
    (MALE, MALE),
    (FEMALE, FEMALE),
    (OTHERS, OTHERS)
)


class Patient(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    gender = models.CharField(choices=gender_choices, default=NONE, max_length=20)
    phone = models.CharField(max_length=16, db_index=True, unique=True)
    address = models.TextField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)  # auto_now_add adds current time by default while saving.

    def __str__(self):
        return "{} ({})".format(self.name, self.age)


class CaseSheet(models.Model):
    complaints = models.TextField(blank=True, null=True)
    history = models.TextField(max_length=300, blank=True, null=True)
    # examination
    height = models.CharField(max_length=30, null=True)
    weight = models.CharField(max_length=30, null=True)
    pulse = models.CharField(max_length=30, null=True)
    blood_pressure = models.CharField(max_length=30, null=True)
    heart_rate = models.CharField(max_length=30, null=True)
    other_examination = models.TextField(max_length=300, blank=True, null=True)
    # Ashtashthana Pareeksha
    nadi = models.CharField(max_length=30)
    jihwa = models.CharField(max_length=30)
    mutra = models.CharField(max_length=30)
    drik = models.CharField(max_length=30)
    malam = models.CharField(max_length=30)
    sabdam = models.CharField(max_length=30)
    akriti = models.CharField(max_length=30)
    sparsha = models.CharField(max_length=30)
    # dasavidha pareeksha
    dushyam = models.CharField(max_length=30)
    desha = models.CharField(max_length=30)
    bala = models.CharField(max_length=30)
    kala = models.CharField(max_length=30)
    anala = models.CharField(max_length=30)
    prakriti = models.CharField(max_length=30)
    vaya = models.CharField(max_length=30)
    satwa = models.CharField(max_length=30)
    sathmya = models.CharField(max_length=30)
    ahara = models.CharField(max_length=30)
    # doctor's content
    investigations = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    prescriptions = models.TextField(blank=True, null=True)
    treatments = models.TextField(blank=True, null=True)
    visit_date = models.DateField(auto_now=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="casesheet")

    def __str__(self):
        return self.patient.name


dataframe = pd.read_csv(os.path.join(os.path.abspath(os.curdir), "core/resources/categories.csv"), sep=",")

categories = dataframe["CategoryName"].to_list()

if len(categories) > 0:
    category_values = ((category, category) for category in categories)
else:
    category_values = (("NONE", "NONE"))


class StockManagement(models.Model):
    medicine_name = models.CharField(max_length=150, null=False, db_index=True, unique=True)
    medicine_category = models.CharField(max_length=150, choices=category_values)
    quantity = models.IntegerField(null=False)
    manufacturer = models.CharField(max_length=60, null=True, blank=True)
    date = models.DateTimeField(auto_now=True, editable=False)
    # medicine_category = models.ForeignKey(StockCategory, on_delete=models.CASCADE, related_name="Stock")

    def __str__(self):
        return "Category:{}, Name:{}"




