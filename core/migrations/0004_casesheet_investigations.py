# Generated by Django 2.1.5 on 2019-10-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_stockmanagement'),
    ]

    operations = [
        migrations.AddField(
            model_name='casesheet',
            name='investigations',
            field=models.TextField(blank=True, null=True),
        ),
    ]
