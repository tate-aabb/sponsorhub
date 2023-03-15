from django.urls import path
from . import views

urlpatterns = [
    path('', views.SponsorPage.as_view(), name="sponsor"),
    path('new-post/', views.New_post.as_view(), name='sponsor_page'),
]

