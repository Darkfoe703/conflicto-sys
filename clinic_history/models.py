from django.db import models

from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.utils import timezone
from datetime import date
# Create your models here.


class SocialSecurity(models.Model):
    class OOSSObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().all
        
    practice_codes = (
        ('Nacional', 'nacional'),
        ('Provincial', 'provincial'),
    )
    
    name = models.CharField(max_length=255, editable=True, blank=False, null=False, verbose_name='Obra Social')
    code_type = models.CharField(max_length=100, choices=practice_codes, default='', blank=True, null=True, verbose_name='Tipo de Nomenclador')

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name
    

class Patient(models.Model):
    class PatientObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().all

    ooss_options = (
        ('OSPE', 'OSPE'),
        ('Particular', 'particular'),
    )
    treatment = (
        ('Activo', 'activo'),
        ('Interrumpido', 'interrumpido'),
        ('Abandonado', 'abandonado'),
        ('Alta', 'alta'),
    )
    status = (
        ('Soltero/a', 'Soltero'),
        ('Casado/a', 'Casado'),
        ('Divorciado/a', 'Divorciado'),
        ('Viudo/a', 'Viudo'),
        ('Separado/a', 'Separado'),
        ('En pareja', 'En pareja'),
    )
    formation = (
        ('Incompletos', 'Incompletos'),
        ('Primaria', 'Primaria'),
        ('Secundaria', 'Secundaria'),
        ('Tecnicatura', 'Tecnicatura'),
        ('Universitaria', 'Universitaria'),
        ('Otro', 'Otro'),
    )
    
    id = models.AutoField(primary_key=True, unique=True, editable=False, blank=False, null=False)
    treatment_status = models.CharField(max_length=50, choices=treatment, editable=True, default='activo', blank=False, null=True, verbose_name='Tratamiento')
    register_date = models.DateField(default=date.today, editable=True, verbose_name='Registrado el')
    pac_number = models.IntegerField(primary_key=False, unique=True, editable=True, blank=False, null=False, verbose_name='Nº Hist. Clínica')
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombre')
    surname = models.CharField(max_length=100, blank=False, null=False, verbose_name='Apellido')
    dni = models.IntegerField(unique=True, verbose_name='DNI')
    birthdate = models.DateField(editable=True, verbose_name='Fecha de Nacimiento')
    phone_number = models.IntegerField(blank=True, verbose_name='Telefono')
    address = models.CharField(max_length=100, blank=True, verbose_name='Dirección')
    email = models.EmailField(max_length=100, blank=True, verbose_name='E-mail')
    education = models.CharField(max_length=100, blank=True, verbose_name='Estudios')
    workplace = models.CharField(max_length=100, blank=True, verbose_name='Ocupación')
    other_act = models.CharField(max_length=255, blank=True, verbose_name='Otras actividades')
    times = models.CharField(max_length=255, blank=True, verbose_name='Tiempos')
    civil_status = models.CharField(max_length=100, blank=True, choices=status, default='', verbose_name='Estado Civil')
    #ooss = models.CharField(max_length=32, blank=True, null=True, choices=ooss_options, default='', verbose_name='O.S')
    ooss = models.ForeignKey(SocialSecurity, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='O.S')
    afiliate_number = models.IntegerField(blank=True, null=True, verbose_name='Nº Afiliado')
    cuil = models.IntegerField(unique=True, blank=True, null=True, verbose_name='CUIL')
    reason = models.TextField(max_length=255, blank=False, verbose_name='Motivo de consulta')
    other_treatment = models.CharField(max_length=100, blank=True, verbose_name='Otros tratamientos')
    pharmacology = models.CharField(max_length=255, blank=True, verbose_name='Medicación')
    referal_for = models.CharField(max_length=50, blank=True, verbose_name='Referido por')
    condition_history = models.CharField(max_length=50, blank=True, verbose_name='Historia del padecimiento')
    other_info = models.TextField(max_length=255, blank=True, verbose_name='Otra información')

    objects = models.Manager()
    patientobjects = PatientObjects()

    class Meta:
        ordering = ('pac_number',)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class PatientContact(models.Model):
    class ContactObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().all
        
    relation_types = (
        ('Tutor/a', 'Tutor'),
        ('Progenitor/a', 'Progenitor'),
        ('Abuelo/a', 'Abuelo'),
        ('Amigo/a', 'Amigo'),
        ('Pareja', 'Pareja'),
        ('Hijo/a', 'Hijo'),
        ('Tio/a', 'Tio'),
        ('Conviviente', 'Conviviente'),
        ('Compañero/a', 'Compañero'),
        ('Otro', 'Otro'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='modelo_paciente', blank=False)
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

class PatientLogs(models.Model):
    class LogsObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().all

    date_log = models.DateField(default=date.today, editable=True, blank=False, null=False, verbose_name='Fecha') 
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='paciente', blank=False, verbose_name='Paciente')
    #patient_ooss = models.OneToOneField(Patient, on_delete=models.CASCADE, blank=True, related_name='ooss', verbose_name='Obra Social' )
    id_session = models.AutoField(primary_key=True,editable=False, blank=False, null=False, unique=True, verbose_name='Sesión')
    n_session = models.PositiveIntegerField(editable=True, blank=False, null=False, auto_created=True)
    #ooss_code = 
    session_log = models.TextField(max_length=1024, editable=True, blank=False, null=False, verbose_name='Registro')

    objects = models.Manager()
    patientobjects = LogsObjects()

    """ def __str__(self):
        return (self.session_log) """


        