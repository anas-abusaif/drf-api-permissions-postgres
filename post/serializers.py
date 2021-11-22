from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "auther", "body", "created_at", "updated_at")
