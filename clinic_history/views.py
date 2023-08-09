from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from .models import SocialSecurity, Patient, PatientLogs

# Create your views here.
class OOSSView(TemplateView):
    template_name = 'clinic_history/ooss.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ooss'] = SocialSecurity.objects.all()
        print(context)
        return context

class PatientPageView(TemplateView):
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
        filtro = Patient.objects.filter(id=self.kwargs.get('id'))
        context['sessions'] = PatientLogs.patientobjects.all()
        print(context)
        return context
    