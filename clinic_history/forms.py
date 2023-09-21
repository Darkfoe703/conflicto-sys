from django import forms
from .models import SocialSecurity, Patient


class OOSS_Form(forms.ModelForm):
    class Meta:
        model = SocialSecurity
        fields = (
            'name',
            'code_type',
            'desc',
        )

class Patient_Form(forms.ModelForm):
    class Meta:
        model = Patient
        fields = (
            'treatment_status',
            'register_date',
            'pac_number',
            'name',
            'surname',
            'dni',
            'birthdate',
            'phone_number',
            'address',
            'email',
            'education',
            'workplace',
            'other_act',
            'times',
            'civil_status',
            'ooss',
            'afiliate_number',
            'cuil',
            'reason',
            'other_treatment',
            'pharmacology',
            'referal_for',
            'condition_history',
            'other_info',
        )