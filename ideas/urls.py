from django.urls import path
from . import views


urlpatterns = [
    path("", views.IdeasPage.as_view(), name="ideas"),
    path("new_ideas", views.New_Ideas.as_view(), name="new")
]