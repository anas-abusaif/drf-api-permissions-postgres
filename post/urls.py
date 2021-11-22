from django.urls import path
from post.views import PostListView, PostDetailView

urlpatterns = [
  path('', PostListView.as_view(), name='post_list'),
  path('/<int:pk>', PostDetailView.as_view(), name='post_detail')
]