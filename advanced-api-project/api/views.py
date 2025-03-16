from rest_framework import generics,filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated  # ✅ Import added
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Define filterable fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Define searchable fields
    search_fields = ['title', 'author']

    # Define ordering fields
    ordering_fields = ['title', 'publication_year']

    # Default ordering (optional)
    ordering = ['title']

# Create a new book (POST) - Only authenticated users can create
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ Only authenticated users can create

# Retrieve a book by ID (GET) - Publicly accessible
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # ✅ Public read access

# Update a book by ID (PUT/PATCH) - Only authenticated users can update
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ Only authenticated users can update

# Delete a book by ID (DELETE) - Only authenticated users can delete
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ Only authenticated users can delete
