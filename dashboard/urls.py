from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", views.home, name="home"),
    path('sign-up/', views.register, name="register"),
    path('', auth_views.LoginView.as_view(template_name="login.html", redirect_authenticated_user=True), name='login'),
    path("logout/", views.logout_user, name="logout"),
]
