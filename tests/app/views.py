from rest_framework import generics

from drf_inout.mixins import InOutSerializerMixin, InOutViewSetMixin
from tests.app.models import Post
from tests.app.serializers import PostInputSerializer, PostOutputSerializer


class PostListCreateView(InOutSerializerMixin, generics.ListCreateAPIView):
    input_serializer_class = PostInputSerializer
    output_serializer_class = PostOutputSerializer

    queryset = Post.objects.all()


class SerializerNotSetView(InOutViewSetMixin, generics.ListCreateAPIView):
    queryset = Post.objects.all()
