from django.db import models
from books.models import Book
from PIL import Image

MAX_HEIGHT = 300
MAX_WIDTH = 300


class Library(models.Model):
    """ Basic model for library data """
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    thumbnail = models.ImageField(
        default="default_library.jpg", upload_to="library_pics", blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.thumbnail.path)
        if img.height > MAX_HEIGHT or img.width > MAX_WIDTH:
            output_size = (MAX_HEIGHT, MAX_WIDTH)
            img.thumbnail(output_size)
            img.save(self.thumbnail.path)

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
