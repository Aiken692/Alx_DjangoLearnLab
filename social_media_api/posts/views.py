from notifications.models import Notification
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, , views, permissions, filters, generics, status
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

class LikePostView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Use get_object_or_404 to retrieve the post or return 404 if not found
        # generics.get_object_or_404(Post, pk=pk)
        post = get_object_or_404(Post, pk=pk)

        user = request.user

        # Prevent the user from liking a post multiple times
        if Like.objects.filter(user=user, post=post).exists():
            return Response({"detail": "You already liked this post."}, status=400)

        # Create the like
        Like.objects.get_or_create(user=request.user, post=post)

        # Create a notification for the post author
        # Notification.objects.create
        notification = Notification(
            recipient=post.author,
            actor=user,
            verb="liked",
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.id
        )
        notification.save()

        return Response({"detail": "Post liked successfully."})

class UnlikePostView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Use get_object_or_404 to retrieve the post or return 404 if not found
        post = get_object_or_404(Post, pk=pk)

        user = request.user

        # Prevent the user from unliking a post they haven't liked
        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response({"detail": "You haven't liked this post."}, status=400)

        # Remove the like
        like.delete()

        return Response({"detail": "Post unliked successfully."})