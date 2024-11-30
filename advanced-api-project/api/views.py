from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookListView(generics.ListAPIView):
    """List all books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Read-only access for all
    filter_backends = [SearchFilter]  # filter_backends: Enables filtering functionality.
    search_fields = ['title', 'author'] # search_fields: Specifies which fields to search for the query.

class BookDetailView(generics.RetrieveAPIView):
    """Retrieve a single book by ID."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """Create a new book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the user as the creator of the book
        serializer.save(created_by=self.request.user)

class BookUpdateView(generics.UpdateAPIView):
    """Update an existing book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Perform custom validation or actions before saving
        instance = serializer.save()
        print(f"Book '{instance.title}' updated successfully!")

class BookDeleteView(generics.DestroyAPIView):
    """Delete a book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        # Add custom logic before deleting
        print(f"Book '{instance.title}' is being deleted.")
        instance.delete()
