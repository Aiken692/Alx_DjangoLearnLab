# bookshelf/admin.py

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Customize the columns displayed in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Add search functionality by title and author
    search_fields = ('title', 'author')

    # Add filters for publication year
    list_filter = ('publication_year',)

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)
