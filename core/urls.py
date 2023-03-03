from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('sponsorhub.urls')),
    # path('ideas/', include('ideas.urls')),
    path('sponsors/', include('sponsor_app.urls')),
    # path('accounts/', include('accounts.urls')),

]