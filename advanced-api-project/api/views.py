from rest_framework import generics
from .models import Book #replace with your working model
from .serializers import BookSerializer # replace with your project's serializer

class CustomBookCreateView(generics.CreateAPIView):
# can be any name, ensure to align with your project as this is sample exampls 
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CustomBookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer