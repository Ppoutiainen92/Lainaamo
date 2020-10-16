from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from libraries.models import LibraryBook


# class OrderBook(models.Model):
#     library_book = models.OneToOneField(LibraryBook, on_delete=SET_NULL, null=True)
#     ordered = models.BooleanField(default=False)

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     library_book = models.ManyToManyField(
#         LibraryBook, on_delete=models.SET_NULL, null=True)
