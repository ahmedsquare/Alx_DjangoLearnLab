from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),  # List & Create
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve, Update, Delete
]