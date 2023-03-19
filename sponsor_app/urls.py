from django.urls import path
from . import views

urlpatterns = [
    path('', views.for_sponsors, name="sponsor"),
    path('new-post/', views.New_post.as_view(), name='sponsor_page'),
]
