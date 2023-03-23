from django.urls import path
from . import views


urlpatterns = [
    path("", views.IdeasBlog.as_view(), name="ideas"),
    path('idea/<int:pk>/', views.IdeasDetail.as_view(), name="ideas_detail"),
    path("new_ideas", views.NewIdeas.as_view(), name="new"),
    path('idea/<int:pk>/update/', views.IdeasUpdate.as_view(), name="update"),
    path('idea/<int:pk>/delete/', views.IdeasDelete.as_view(), name="delete"),
    path('search-idea', views.IdeaSearch.as_view(), name='search_idea'),
]