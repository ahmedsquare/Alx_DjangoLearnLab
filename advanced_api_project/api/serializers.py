from rest_framework import serializers
from .models import Book
from .models import Author
from datetime import datetime
"""Book Serializer"""
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


"""Author Serializer"""
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
"Custom Book Serializer"
class CustomBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    """VaLidation for the Production Year"""
    def validate(self,data):
        if(data['publication_year']  > datetime.today().year):
            raise serializers.ValidationError("The Publication Date is IVALID!!.")
        return data