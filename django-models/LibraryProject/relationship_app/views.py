from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import Library

# Create your views here.
def list_books(request):
    books = Book.objects.select_related('author').all()  # Fetch books with authors
    return render(request, 'relationship_app/list_books.html', {'books': books})

    def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

class BookListView(ListView):
    model = Book
    template_name = 'relationship_app/book_list.html'
    context_object_name = 'books'

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'