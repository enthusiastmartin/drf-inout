from django import VERSION as django_version

if django_version[0] >= 2:
    from django.urls import path
else:
    from django.conf.urls import url
from .views import PostListCreateView, SerializerNotSetView

if django_version[0] >= 2:
    urlpatterns = [
        path("blog/posts", PostListCreateView.as_view(), name="post_list_create"),
        path("notset/", SerializerNotSetView.as_view(), name="notset_path"),
    ]
else:
    urlpatterns = [
        url("blog/posts", PostListCreateView.as_view(), name="post_list_create"),
        url("notset/", SerializerNotSetView.as_view(), name="notset_path"),
    ]
