from django.shortcuts import render
from django_filters import rest_framework as filters  # Add this line
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated  # Explicit imports for permissions
from rest_framework.filters import SearchFilter
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookListView(generics.ListAPIView):
    """List all books with filtering, searching, and ordering."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.DjangoFilterBackend, rest_framework_filters.SearchFilter, rest_framework_filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']  # Fields for filtering
    search_fields = ['title', 'author']  # Fields for searching
    ordering_fields = ['title', 'publication_year']  # Fields for ordering
    ordering = ['title']  # Default ordering

class BookDetailView(generics.RetrieveAPIView):
    """Retrieve a single book by ID."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow unauthenticated read-only access

class BookCreateView(generics.CreateAPIView):
    """Create a new book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Requires authentication

    def perform_create(self, serializer):
        """Set the user as the creator of the book."""
        serializer.save(created_by=self.request.user)

class BookUpdateView(generics.UpdateAPIView):
    """Update an existing book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Requires authentication

    def perform_update(self, serializer):
        """Custom validation or actions before saving."""
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
