from django.urls import path, include
from .import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from authy.views import UserProfile, OtherUserProfile
from post.views import NewPost

urlpatterns = [
    path("", views.home, name="home"),
    path('sign-up/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html", redirect_authenticated_user=True), name='login'),
    path("logout/", views.logout_user, name="logout"),
    
    # =========== TESTING ============#
    # path('test/', views.test, name="test")
]
