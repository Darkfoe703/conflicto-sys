from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import (
    OOSSView,
    PatientPageView,
    PatientDetailView
)
    

app_name = "clinic_history"

urlpatterns = [
    path('', PatientPageView.as_view(), name='home'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient-detail')
]