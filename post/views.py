from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from post.serializers import PostSerializer
from post.models import Post
from post.permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class PostListView(ListCreateAPIView):
  permission_classes = (IsAuthenticatedOrReadOnly,)
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class PostDetailView(RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthorOrReadOnly,)
  queryset = Post.objects.all()
  serializer_class = PostSerializer

  