from django.contrib import admin
from .models import Book

# Register the Book model to be managed in the admin interface
admin.site.register(Book)