from django.urls import path
from . import views

urlpatterns = [
    path('', views.SponsorPost.as_view(), name="sponsor"),
    path("ideas/<int:pk>/", views.SponsorDetail.as_view(), name="sponsor_detail"),
    path('new-post/', views.NewSponsorPost, name='sponsor_page'),
    path("sponsor/<int:pk>/update/", views.SponsorUpdate.as_view(), name="Sponsor_update"),
    path("sponsor/<int:pk>/delete/", views.SponsorDelete.as_view(), name="Sponsor_delete"),
    path("search-sponsor", views.IdeaSearch.as_view(), name="search_sponsor"),
    path("<str:username>", views.Suser_accaunt.as_view(), name="Suser_accaunt"),
    path("detail/<int:pk>", views.Detail_Contributor.as_view(), name="detail_contributor"),
]

