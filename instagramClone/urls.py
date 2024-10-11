from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include('authy.urls')),
    path('', include('dashboard.urls')),
    path('', include('post.urls'))
]
