from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = "authy"

urlpatterns = [ 
    path("", include('dashboard.urls')),
    path("profile/", views.UserProfile, name="profile"),
    path("profile-other/<str:username>", views.OtherUserProfile, name="profile_other"),
    path("<uuid:post_id>/like/", views.likeProfile, name="likePostProfile"),
    path("<uuid:post_id>/like/", views.likeOtherProfile, name="likePostOtherProfile")
]
