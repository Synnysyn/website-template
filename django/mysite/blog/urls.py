from . import views
from .feeds import LatestPostsFeed
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('upload/', views.image_upload_view, name='upload'),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]