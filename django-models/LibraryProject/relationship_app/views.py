from django.shortcuts import render

from django.views.generic import DetailView
from .models import Library
from .models import Book

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Use the template for rendering
    context_object_name = 'library'  # This makes "library" available in the template



def list_books(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, 'list_books.html', {'books': books})  # Pass books to the template
