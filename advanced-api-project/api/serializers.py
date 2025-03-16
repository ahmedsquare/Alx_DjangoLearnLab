from rest_framework import serializers
from .models import Book,Author
from datetime import datetime
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields in serialization


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'  # Include all fields in serialization

class CustomBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate(self, data):
        if data['publication_year'] > datetime.today().year :
            raise serializers.ValidationError("Publication Year is Invalid!!")
        return data