# Generated by Django 2.1.5 on 2019-11-13 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_financemanagement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financemanagement',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]