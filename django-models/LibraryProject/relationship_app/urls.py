from django.urls import path
from .views import list_books, BookListView, LibraryDetailView
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    
    path('list_books/', list_books, name='list_books'),  # Function-based view
    path('books/', BookListView.as_view(), name='book_list'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view

    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),  # Include relationship_app URLs
]
