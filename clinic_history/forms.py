from django import forms
from .models import SocialSecurity


class OOSS_Form(forms.ModelForm):
    class Meta:
        model = SocialSecurity
        fields = (
            'name',
            'code_type',
            'desc',
        )