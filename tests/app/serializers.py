from django.contrib.auth.models import User
from rest_framework import serializers

from tests.app.models import Blog, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
        )


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            "id",
            "name",
        )


class PostInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "publish_date",
            "blog",
            "author",
        )


class PostOutputSerializer(serializers.ModelSerializer):
    blog = BlogSerializer()
    author = UserSerializer()

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "publish_date",
            "blog",
            "author",
        )
