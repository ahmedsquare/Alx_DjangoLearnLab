from .views import BookListCreateAPIView
from django.urls import path

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list'),  # Maps to the BookList view
]