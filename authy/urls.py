from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = "authy"

urlpatterns = [ 
    path("profile/", views.UserProfile, name="profile"),
    path("profile-other/<str:username>/", views.OtherUserProfile, name="profile_other"),
]
