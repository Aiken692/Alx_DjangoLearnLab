from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class BookList(generics.ListCreateAPIView):
    """List all books or create a new book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users

    def perform_create(self, serializer):
        """Save the post data when creating a new book."""
        serializer.save()

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Requires authentication

    def perform_update(self, serializer):
        """Custom logic before updating."""
        instance = serializer.save()
        print(f"Book '{instance.title}' updated successfully!")

class BookDeleteView(generics.DestroyAPIView):
    """Delete a book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Requires authentication

    def perform_destroy(self, instance):
        """Custom logic before deleting."""
        print(f"Book '{instance.title}' is being deleted.")
        instance.delete()