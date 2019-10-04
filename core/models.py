from django.db import models

# Create your models here.
NONE = 'Not willing to share'
MALE = 'Male'
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
    phone = models.IntegerField(primary_key=True, db_index=True)
    address = models.TextField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)  # auto_now_add adds current time by default while saving.



