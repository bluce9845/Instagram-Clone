from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from authy.views import UserProfile

urlpatterns = [ 
    # path('profile/edit', EditProfile, name="editprofile"),
]
