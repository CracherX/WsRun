from rest_framework.generics import ListAPIView
from .serializer import BookSerializer
from .models import Book


class BooksAPI(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()
