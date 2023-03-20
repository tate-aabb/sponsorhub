from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm1, CustomUserCreationForm2
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView, CreateView
from .models import CustomUser
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForms
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView




def Login(request):
    if request.method == "POST":
        forms = LoginForms(request.POST)
        if forms.is_valid():
            user = authenticate(request,
                                email=forms.cleaned_data["email"],
                                password=forms.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect("homepage")
            else:
                forms.add_error(None, "Invalid username or password")
    else:
        forms = LoginForms()
    return render(request, "Login.html", {"forms": forms})



def SignUp(request):
    if request.method == "POST":
        forms1 = CustomUserCreationForm1(request.POST)
        forms2 = CustomUserCreationForm2(request.POST)
        if forms1.is_valid() and forms2.is_valid():
            user = forms1.save()
            custom_user = forms2.save(commit=False)
            custom_user.user = user
            custom_user.save()
            messages.success(request, 'Your accounts have been created successfully!')
            return redirect("home")
    else:
        forms1 = CustomUserCreationForm1(request.POST)
        forms2 = CustomUserCreationForm2(request.POST)
    context = {
        "forms1": forms1,
        "forms2": forms2,
    }
    return render(request, "SingUpSponsor.html", context)



