from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('scrape-forbes/', views.scrapeandsave),
    path('contact/', views.contact, name='contact'),
]