from .views import list_books, BookListView, LibraryDetailView, admin_view, librarian_view, member_view, add_book, edit_book, delete_book
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Book CRUD urls
    path('add_book/', add_book, name='add_book'),  # URL for adding a book
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),  # URL for editing a book, identified by primary key (pk)
    path('book/delete/<int:pk>/', delete_book, name='delete_book'),  # URL for deleting a book, identified by primary key (pk)

    # Access control urls
    path('admin/', admin_view, name='admin_view'),  # URL for admin view
    path('librarian/', librarian_view, name='librarian_view'),  # URL for librarian view
    path('member/', member_view, name='member_view'),  # URL for member view

    # Authentication urls
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # URL for login
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # URL for logout
    path('register/', views.register, name='register'),  # URL for user registration

    # Book listing urls
    path('list_books/', list_books, name='list_books'),  # URL for listing books (function-based view)
    path('books/', BookListView.as_view(), name='book_list'),  # URL for listing books (class-based view)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for library detail view, identified by primary key (pk)

    # Admin site urls
    path('admin/', admin.site.urls),  # URL for Django admin site
    path('relationship_app/', include('relationship_app.urls')),  # Include relationship_app URLs
]