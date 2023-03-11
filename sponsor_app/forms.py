from django import forms
from django.forms import Textarea
from .models import Sponsorpost

class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsorpost
        fields = ('business_name', 'business_industry', 'about_sponsor', 'budget', 'email')
        widgets = {
            "business_name": forms.TextInput(attrs={"class": "form-control", "style": "width:200px"}),
            "business_industry": forms.TextInput(attrs={"class": "form-control", "style": "width:200px"}),
            "about_sponsor": Textarea(attrs={"style": "width:1600px; height: 300px"}),
            "budget": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),

        }
