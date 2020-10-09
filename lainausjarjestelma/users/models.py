from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile information for user contains basic contact data for it"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username
