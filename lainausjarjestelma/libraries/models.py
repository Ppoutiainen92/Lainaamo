from django.db import models
from books.models import Book
# Create your models here.


class Library(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    # library_books = models.

    def __str__(self):
        return self.name


class LibraryBook(models.Model):
    """Book associated with assigned library"""
    book = models.ForeignKey(
        Book, default=None, on_delete=models.CASCADE, null=True)
    library = models.ForeignKey(
        Library, default=None, on_delete=models.CASCADE, null=True)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.book.book_title + " - " + self.library.name
