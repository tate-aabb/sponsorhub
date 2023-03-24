from django import forms
from django.forms import ModelForm, Textarea
from .models import IdeasModel
from django import db

class Add_Ideas(forms.ModelForm):
    class Meta:
        model = IdeasModel
        fields = ("Title", "About_contributor", "Idea_industry", "Idea_text", "Budget", "Contact_email")
        widgets = {
            "Title": forms.TextInput(attrs={"class": "form-control", "style": "width:1255px"}),
            "About_contributor": forms.TextInput(attrs={"class": "form-control", "style": "width:1255px"}),
            "Idea_industry": forms.TextInput(attrs={"class": "form-control", "style": "width:1255px"}),
            "Idea_text": Textarea(attrs={"style": "width: 1255px; height: 300px"}),
            "Budget(USD)": forms.TextInput(attrs={"class": "form-control"}),
            "Contact_email": forms.TextInput(attrs={"class": "form-control"}),
        }
