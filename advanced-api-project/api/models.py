from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{Author.name}"
# Create your models here.
class Book(models.Model):
    publication_year = models.IntegerField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{Book.title}"    