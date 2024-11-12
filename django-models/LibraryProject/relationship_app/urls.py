from django.urls import path
from .views import list_books, BookListView, LibraryDetailView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('list_books/', list_books, name='list_books'),  # Function-based view
    path('books/', BookListView.as_view(), name='book_list'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view

    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),  # Include relationship_app URLs
]
