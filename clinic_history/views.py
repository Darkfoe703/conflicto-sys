from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from .models import Patient

# Create your views here.
class PatientPageView(TemplateView):
    template_name = 'clinic_history/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patients'] = Patient.patientobjects.all()
        return context