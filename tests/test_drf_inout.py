from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from tests.app.models import Blog, Post
from tests.app.serializers import PostOutputSerializer


class TestInOutInputView(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.blog = Blog.objects.create(name="blog1")
        self.user = User.objects.create_user(username="user1", password="password")

    def test_input(self):
        data = {
            "title": "post title",
            "content": "post content",
            "blog": self.blog.id,
            "author": self.user.id,
        }
        response = self.client.post(
            reverse("post_list_create"), data=data, format="json"
        )

        self.assertContains(response, "post title", status_code=201)

    def test_invalid_nested_input(self):
        data = {"title": "post title", "content": "post content", "blog": {"id": 1}}
        response = self.client.post(
            reverse("post_list_create"), data=data, format="json"
        )
        self.assertContains(response, "", status_code=400)


class TestInOutOutputView(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.blog = Blog.objects.create(name="blog1")
        self.user = User.objects.create_user(username="user1", password="password")
        self.post01 = Post.objects.create(
            title="post title",
            content="post content",
            blog_id=self.blog.id,
            author_id=self.user.id,
        )
        self.post02 = Post.objects.create(
            title="post title",
            content="post content",
            blog_id=self.blog.id,
            author_id=self.user.id,
        )

        self.postSer = PostOutputSerializer(self.post01)
        self.postSer02 = PostOutputSerializer(self.post02)

    def test_output(self):
        response = self.client.get(reverse("post_list_create"))
        self.assertContains(response, "post title", status_code=200)

        data = response.data
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["id"], self.post01.id)
        self.assertEqual(data[1]["id"], self.post02.id)
        self.assertDictEqual(data[0], self.postSer.data)
        self.assertDictEqual(data[1], self.postSer02.data)


class TestSerializerNotSet(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_request(self):
        with self.assertRaises(AssertionError):
            self.client.get(reverse("notset_path"))
