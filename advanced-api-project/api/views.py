from rest_framework import generics
from myapp.models import Book  # Import Book model from myapp
from .serializers import BookSerializer

# ListView: Retrieve all books (GET) & Create a new book (POST)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# DetailView + UpdateView + DeleteView: Retrieve, Update, Delete a book by ID
class BookDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
