# Generated by Django 2.1.5 on 2019-11-13 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20191113_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='financemanagement',
            name='month',
            field=models.IntegerField(default=11, editable=False),
        ),
    ]
