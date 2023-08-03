from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import (
    PatientPageView,
)
    

app_name = "clinic_history"

urlpatterns = [
    path('', PatientPageView.as_view(), name='home'),
]