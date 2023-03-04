from django import forms
from django.forms import ModelForm, Textarea
from .models import IdeasModel
from django import db

class Add_Ideas(forms.ModelForm):
    class Meta:
        model = IdeasModel
        fields = ("About_contributing", "Idea_industry", "Idea_text", "Budget", "Contact_email")
        widgets = {
            "About_contributing" : forms.TextInput(attrs={"class": "form-control", "style": "width:200px"}),
            "Idea_industry": forms.TextInput(attrs={"class": "form-control", "style": "width:200px"}),
            "Idea_text": Textarea(attrs={"style": "width:1600px; height: 300px"}),
            "Budget": forms.TextInput(attrs={"class": "form-control"}),
            "Contact_email": forms.TextInput(attrs={"class": "form-control"}),

        }
