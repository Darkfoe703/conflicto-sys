from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'dni', 'pac_number')