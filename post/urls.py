from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('newpost/', views.NewPost, name="newPost"),
    path("tag/<slug:tag_slug>/", views.tags, name="tags"),
    path("<uuid:post_id>/post-detail", views.postDetails, name="postDetails"),
    path("<uuid:post_id>/like/", views.like, name="postLike"),
    path("<uuid:post_id>/favorite/", views.favorite, name="post-favorite")
]
