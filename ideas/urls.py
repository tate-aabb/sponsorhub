from django.urls import path
from . import views


urlpatterns = [
    path("", views.IdeasBlog, name="ideas"),
    path("new_ideas", views.New_Ideas.as_view(), name="new")
]