from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin

class BookAdmin(admin.ModelAdmin):
    # Display fields in the admin list view
    list_display = ('title', 'author', 'publication_date')

    # Add list filters for easy filtering
    list_filter = ('author', 'publication_date')

    # Enable search capabilities
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)
