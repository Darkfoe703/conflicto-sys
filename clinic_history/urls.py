from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import (
    OOSSView,
    PatientListView,
    PatientDetailView,
    OOSSCreateView,
    OOSSUpdateView,
)
    

app_name = "clinic_history"

urlpatterns = [
    path('', PatientListView.as_view(), name='home'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('createOOSS/', OOSSCreateView.as_view(), name='createOOSS'),
    path('updateOOSS/', OOSSUpdateView.as_view(), name='updateOOSS')
]