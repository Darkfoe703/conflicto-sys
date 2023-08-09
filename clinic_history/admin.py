from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.SocialSecurity)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'code_type')

@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('pac_number', 'name', 'surname', 'dni', 'cuil', 'id', 'treatment_status', 'ooss', 'civil_status')
    
@admin.register(models.PatientContact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('patient', 'name', 'surname', 'relation', 'phone_number')

@admin.register(models.PatientLogs)
class PatientLogAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date_log', 'n_session', 'session_log', 'id_session')

