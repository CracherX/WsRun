from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['pk', 'book_name', 'description', 'genre']
        depth = 1
