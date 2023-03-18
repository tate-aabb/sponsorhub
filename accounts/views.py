from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm1, CustomUserCreationForm2
from django.views.generic import TemplateView, CreateView
from .models import CustomUser
from django.contrib import messages



class Login(TemplateView):
    template_name = "Login.html"

def SignUp(request):
    if request.method == "POST":
        forms1 = CustomUserCreationForm1(request.POST)
        forms2 = CustomUserCreationForm2(request.POST)
        if forms1.is_valid() and forms2.is_valid():
            user1 = forms1.save(commit=False)
            user2 = forms2.save(commit=False)
            user1.save()
            user2.save()
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



