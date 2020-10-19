from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from libraries.models import LibraryBook
import datetime
from django.utils import timezone


class OrderBook(models.Model):
    library_book = models.OneToOneField(
        LibraryBook, on_delete=models.SET_NULL, null=True)
    ordered = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True, blank=True)
    expire_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.library_book.book.book_title + " " + self.library_book.library.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    library_book = models.ManyToManyField(
        OrderBook, blank=True)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + " Order" + str(self.id)


class LoanedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    library_book = models.ManyToManyField(
        OrderBook, blank=True)

    def __str__(self):
        return self.user.username + " Order"
