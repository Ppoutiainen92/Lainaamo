from django.db import models
import datetime
from django.utils import timezone
from PIL import Image
from django_resized import ResizedImageField


MAX_HEIGHT = 250
MAX_WIDTH = 250


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
    thumbnail = ResizedImageField(
        size=[250, 250], default="default.jpg", upload_to="book_pics", blank=True, force_format='JPEG')

    # def save(self):
    #     Image implementation is not finished. Uploading image is going to suffer from artifacting

    #     super(Book, self).save
    #     img = Image.open(self.thumbnail.path)
    #     if img.height > max_height or img.width > max_width:
    #         output_size = (max_height, max_width)
    #         img.thumbnail(output_size)
    #         img.save(self.thumbnail.path)

    def __str__(self):
        return self.book_title + " " + self.author
