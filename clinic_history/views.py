from typing import Any, Dict
from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import (
    SocialSecurity,
    Patient,
    PatientLogs,
    PatientContact
    )
from .forms import OOSS_Form

# Create your views here.
class OOSSView(TemplateView):
    template_name = 'clinic_history/ooss.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ooss'] = SocialSecurity.objects.all()
        print(context)
        return context

class PatientListView(TemplateView):
    template_name = 'clinic_history/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patients'] = Patient.patientobjects.all()

        fields_names_dict = {}
        # Recorremos los campos del modelo y los agregamos al diccionario
        for field in Patient._meta.fields:
            fields_names_dict[field.name] = field.verbose_name
        context['fields'] = fields_names_dict

        return context


class PatientDetailView(DetailView):
    model = Patient
    template_name = 'clinic_history/patient_detail.html'
    context_object_name = 'patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patients'] = Patient.objects.filter(id=self.kwargs.get('id'))
        context['sessions'] = PatientLogs.objects.filter(patient_id=self.kwargs.get('pk'))
        context['contacts'] = PatientContact.objects.filter(patient_id=self.kwargs.get('pk'))
        print(context)
        return context
    

class OOSSCreateView(CreateView):
    form_class = OOSS_Form
    model = SocialSecurity
    success_url = '/clinic_history/listOOSS'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'crear'
        })
        return context


class OOSSUpdateView(UpdateView):
    form_class = OOSS_Form
    model = SocialSecurity
    success_url = '/clinic_history/listOOSS'

    fields = (
        'name',
        'code_type',
    )

"""
TODO:
- Vista de Update OOSS
- Vista de Delete OOSS
- Integrar update y delete en la tabla de OOSS
- Form de Pacientes, Contactos y Registro
"""