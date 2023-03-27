from rest_framework.urls import path
from .views import BooksAPI

urlpatterns = [
    path('book/', BooksAPI.as_view())
]
