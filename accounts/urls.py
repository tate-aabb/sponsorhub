from django.urls import path
from . import views

urlpatterns = [
    path("", views.Login.as_view(), name="Login"),
    path("SingUpSponsor/", views.SignUp, name="SingUpSponsor"),
]