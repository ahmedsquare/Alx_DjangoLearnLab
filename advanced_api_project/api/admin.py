from django.contrib import admin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Displays only the name in the admin list

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Shows key details
    list_filter = ('author', 'publication_year')  # Adds filtering options
    search_fields = ('title', 'author__name')  # Enables search by title or author name
