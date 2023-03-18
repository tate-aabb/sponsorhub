from django import forms
from .models import Sponsorpost
from django.contrib.auth import models

class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsorpost
        fields = ('business_name', 'about_sponsor', 'business_industry', 'budget', 'email')
