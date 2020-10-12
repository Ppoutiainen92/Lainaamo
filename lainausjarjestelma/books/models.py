from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Book(models.Model):
    book_title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    publis_year = models.DateTimeField()
    release = models.IntegerField()
    language = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, blank=True, null=True)
    amount = models.IntegerField(default=0, blank=True)
    rental_duration = models.IntegerField(blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True)
    thumbnail = models.ImageField(
        default="default.jpg", upload_to="book_pics", blank=True)

    def __str__(self):
        return self.book_title + " " + self.author
