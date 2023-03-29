from django.urls import path
from . import views

urlpatterns = [
    path("", views.IdeasBlog.as_view(), name="ideas"),
    path('sponsors/<int:pk>/', views.IdeasDetail.as_view(), name="ideas_detail"),
    path("new_ideas", views.NewIdeas, name="new"),
    path('idea/<int:pk>/update/', views.IdeasUpdate.as_view(), name="update"),
    path('idea/<int:pk>/delete/', views.IdeasDelete.as_view(), name="delete"),
    path('search-idea', views.IdeaSearch.as_view(), name='search_idea'),
    path("<str:username>", views.User_account.as_view(), name="user_account"),
    path("detail/<int:pk>", views.Detail_Sponsors.as_view(), name="derail_sponsor"),
]