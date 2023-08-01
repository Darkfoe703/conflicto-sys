from django.db import models

from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.utils import timezone
from datetime import date
# Create your models here.


class Patient(models.Model):
    class PatientObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().all

    ooss_options = (
        ('ospe', 'OSPE'),
        ('published', 'Published'),
    )
    status_treatment = [
        (True, 'Activo'),
        (False, 'Inactivo'),
    ]
    
    id = models.AutoField(primary_key=True, unique=True, editable=False, blank=False, null=False)
    treatment_status = models.BooleanField(verbose_name='Estado del tratamiento', choices=status_treatment, editable=True, default=True, blank=True, null=True)
    register_date = models.DateField(default=date.today, editable=True)
    pac_number = models.IntegerField(primary_key=False, unique=True, editable=True, blank=False, null=False, verbose_name='Historia Clinica Nº')

    name = models.CharField(verbose_name='Nombre', max_length=100, blank=False, null=False)
    surname = models.CharField(max_length=100, blank=False, null=False, verbose_name='Apellido')
    dni = models.IntegerField(unique=True, verbose_name='DNI')
    birthdate = models.DateField(editable=True)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    education = models.CharField(max_length=100)
    workplace = models.CharField(max_length=100)
    other_act = models.CharField(max_length=255)
    times = models.CharField(max_length=255)
    civil_status = models.CharField(max_length=100)
    emotional_bond = models.CharField(max_length=100)
    #pac_ooss = models.CharField(max_length=32, blank=True, null=True, choices='ooss_options', default='')
    reason = models.TextField(max_length=255)
    other_treatment = models.CharField(max_length=100)
    pharmacology = models.CharField(max_length=255)
    referal_for = models.CharField(max_length=50)
    condition_history = models.CharField(max_length=50)
    other_info = models.TextField(max_length=255)

    patients = models.Manager()
    patientobjects = PatientObjects()

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name


