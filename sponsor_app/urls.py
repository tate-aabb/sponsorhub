from django.urls import path
from .views import BlogListView
from . import views

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/', views.sponsor_view, name="sponsor")
]
