from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """User form which contains relevant information for succesfull registeration"""
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    """Form for updating user information(Not used at the moment)"""
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    """Form for profile contact information"""
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "address", "phone"]
