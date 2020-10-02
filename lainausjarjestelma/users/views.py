from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):
    return render(request, "users/register.html")
