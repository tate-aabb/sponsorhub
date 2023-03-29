from django.urls import path
from . import views

urlpatterns = [
    path('', views.for_sponsors, name="sponsor"),
    path('sponsor/<int:pk>/', views.SponsorDetail.as_view(), name="sponsor_detail"),
    path('new-post/', views.New_post.as_view(), name='sponsor_page'),
    path('my-posts/', views.user_posts, name='user_posts'),
    path('sponsor/<int:pk>/update/', views.SponsorUpdate.as_view(), name="update"),
    path('sponsor/<int:pk>/delete/', views.SponsorDelete.as_view(), name="delete"),
    path('search-sponsor', views.SponsorSearch.as_view(), name='search_sponsor'),
]


