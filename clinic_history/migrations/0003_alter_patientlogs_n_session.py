# Generated by Django 4.2.3 on 2023-08-09 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_history', '0002_patientlogs_n_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientlogs',
            name='n_session',
            field=models.PositiveIntegerField(auto_created=True),
        ),
    ]
