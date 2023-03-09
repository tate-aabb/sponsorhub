from django.urls import path
from .views import BlogListView
from . import views

urlpatterns = [
   # path('posts/', views.post_list, name='post_list'),
    path('', BlogListView.as_view(), name='home'),
    path('form/', views.sponsor_view, name="sponsor")
]
