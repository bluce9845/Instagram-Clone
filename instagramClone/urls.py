from django.contrib import admin
from django.urls import path, include
from authy.views import UserProfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include('authy.urls')),
    path('', include('dashboard.urls')),

    # profile
    path("<username>/", UserProfile, name="profile"),
]
