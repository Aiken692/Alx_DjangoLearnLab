from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view

    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),  # Include relationship_app URLs
]
