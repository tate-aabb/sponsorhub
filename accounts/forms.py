from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Type



class LoginForms(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "name@example.com"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))

class CustomUserCreationForm1(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))

    class Meta:
        model = User
        fields = ("username","email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            "email": forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        }

class CustomUserCreationForm2(forms.ModelForm):
    user_type = forms.ChoiceField(choices=Type.choices)
    class Meta:
        model = CustomUser
        fields = ["user_type"]
        widgets = {"user_type": forms.RadioSelect(attrs={"class": 'horizontal-radio'}, choices=Type.choices)}