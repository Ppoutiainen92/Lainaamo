from django.db import models
import datetime
from django.utils import timezone
from PIL import Image


MAX_HEIGHT = 300
MAX_WIDTH = 300


class Book(models.Model):
    book_title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    publishing_year = models.DateField()
    language = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, blank=True, null=True)
    thumbnail = models.ImageField(
        default="default.jpg", upload_to="book_pics", blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.thumbnail.path)
        if img.height > 300 or img.width > 300:
            output_size = (MAX_HEIGHT, MAX_WIDTH)
            img.thumbnail(output_size)
            img.save(self.thumbnail.path)

    def __str__(self):
        return self.book_title + " " + self.author
