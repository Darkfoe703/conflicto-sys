from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import (
    OOSSView,
    PatientListView,
    PatientDetailView,
    OOSSCreateView,
    OOSSUpdateView,
    OOSSDeleteView,
    PatientCreateView,
    PatientUpdateView,
    PatientDeleteView,
)
    

app_name = "clinic_history"

urlpatterns = [
    path('', PatientListView.as_view(), name='home'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('listOOSS/', OOSSView.as_view(), name='listOOSS'),
    path('createOOSS/', OOSSCreateView.as_view(), name='createOOSS'),
    path('updateOOSS/<int:pk>', OOSSUpdateView.as_view(), name='updateOOSS'),
    path('delete_ooss/<int:pk>', OOSSDeleteView.as_view(), name='deleteOOSS'),
    path('createPatient/', PatientCreateView.as_view(), name='createPatient'),
    path('updatePatient/<int:pk>', PatientUpdateView.as_view(), name='updatePatient'),
    path('deletePatient/<int:pk>', PatientDeleteView.as_view(), name='deletePatient'),
]