from django.shortcuts import render
from rest_framework import viewsets, permissions, filters, generics, status
from .models import Post, Comment, Like
from notifications.models import Notification
from .serializers import PostSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import get_object_or_404


class PostPagination(PageNumberPagination):
    page_size = 10

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PostPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)  # Using generics.get_object_or_404
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked',
                target=post
            )
            return Response({"message": "Post liked successfully!"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Post already liked!"}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)  # Using generics.get_object_or_404
        like = Like.objects.filter(user=request.user, post=post).first()
        if like:
            like.delete()
            return Response({"message": "Post unliked successfully!"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "You haven't liked this post!"}, status=status.HTTP_400_BAD_REQUEST)