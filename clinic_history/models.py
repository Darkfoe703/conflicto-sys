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
        ('particular', 'Particular'),
    )
    treatment = (
        (True, 'Activo'),
        (False, 'Inactivo'),
    )
    status = (
        ('single', 'Soltero/a'),
        ('married', 'Casado/a'),
        ('divorced', 'Divorciado/a'),
        ('widower', 'Viudo/a'),
        ('separated', 'Separado/a'),
        ('in_couple', 'En pareja'),
    )
    
    id = models.AutoField(primary_key=True, unique=True, editable=False, blank=False, null=False)
    treatment_status = models.BooleanField(verbose_name='Estado del tratamiento', choices=treatment, editable=True, default=True, blank=False, null=True)
    register_date = models.DateField(default=date.today, editable=True)
    pac_number = models.IntegerField(primary_key=False, unique=True, editable=True, blank=False, null=False, verbose_name='Historia Clinica Nº')
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombre')
    surname = models.CharField(max_length=100, blank=False, null=False, verbose_name='Apellido')
    dni = models.IntegerField(unique=True, verbose_name='DNI')
    birthdate = models.DateField(editable=True, verbose_name='Fecha de Nacimiento')
    phone_number = models.IntegerField(blank=True)
    address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    education = models.CharField(max_length=100, blank=True)
    workplace = models.CharField(max_length=100, blank=True)
    other_act = models.CharField(max_length=255, blank=True)
    times = models.CharField(max_length=255, blank=True)
    civil_status = models.CharField(max_length=100, blank=True, choices=status, default='')
    ooss = models.CharField(max_length=32, blank=True, null=True, choices=ooss_options, default='')
    cuil = models.IntegerField(unique=True, verbose_name='CUIL', blank=True, null=True)
    reason = models.TextField(max_length=255, blank=False)
    other_treatment = models.CharField(max_length=100, blank=True)
    pharmacology = models.CharField(max_length=255, blank=True)
    referal_for = models.CharField(max_length=50, blank=True)
    condition_history = models.CharField(max_length=50, blank=True)
    other_info = models.TextField(max_length=255, blank=True)

    objects = models.Manager()
    patientobjects = PatientObjects()

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class PatientContact(models.Model):
    class ContactObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().all
        
    relation_types = (
        ('tutor', 'Tutor/a'),
        ('parent', 'Progenitor/a'),
        ('grand', 'Abuelo/a'),
        ('friend', 'Amigo/a'),
        ('couple', 'Pareja'),
        ('children', 'Hijo/a'),
        ('uncle', 'Tio/a'),
        ('cohabitant', 'Conviviente'),
        ('mate', 'Compañero/a'),
        ('other', 'Otro'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='contact', blank=False)
    name = models.CharField(max_length=50, blank=False, verbose_name='Nombre')
    surname = models.CharField(max_length=50, blank=True, verbose_name='Apellido')
    relation = models.CharField(choices=relation_types, default='', blank=False, max_length=20, verbose_name='Relación')
    phone_number = models.IntegerField(blank=False, verbose_name='Contacto')
    address = models.CharField(max_length=20, blank=True, verbose_name='Dirección')
    other_info = models.TextField(max_length=255, blank=True, verbose_name='Info')

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name

