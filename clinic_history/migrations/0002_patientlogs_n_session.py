# Generated by Django 4.2.3 on 2023-08-09 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_history', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientlogs',
            name='n_session',
            field=models.PositiveIntegerField(auto_created=True, default=1, max_length=100),
            preserve_default=False,
        ),
    ]
