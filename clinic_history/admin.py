from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('pac_number', 'name', 'surname', 'dni', 'cuil', 'id', 'treatment_status', 'ooss', 'civil_status')
    
@admin.register(models.PatientContact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('patient', 'name', 'surname', 'relation', 'phone_number')