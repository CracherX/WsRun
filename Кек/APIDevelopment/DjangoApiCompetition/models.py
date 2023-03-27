from django.db import models


class Genre(models.Model):
    genre_name = models.CharField(max_length=70)
    description = models.TextField()
    popularity = models.IntegerField()

    def __str__(self):
        return self.genre_name


class Book(models.Model):
    book_name = models.CharField(max_length=30)
    description = models.TextField()
    genre = models.ForeignKey('Genre', related_name='Book', on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name
