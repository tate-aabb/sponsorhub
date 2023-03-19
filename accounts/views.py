from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm1, CustomUserCreationForm2
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView, CreateView
from .models import CustomUser
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login



# class Login(TemplateView):
#     template_name = "Login.html"
def Login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 0:
                return redirect("sponsor")
            elif user.user_type == 1:
                return redirect("ideas")
    else:
        user = authenticate()
    return render(request, "Login.html", {"form": user})
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



