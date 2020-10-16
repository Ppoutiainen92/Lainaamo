from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Kiitos rekisteröinnistä olet nyt kirjautuneena")
            new_user = authenticate(
                username=form.cleaned_data["username"], password=form.cleaned_data["password1"],)
            login(request, new_user)
            return redirect("profile")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, "Käyttäjä tietosi on päivitetty")
            return redirect("book-list")
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "p_form": p_form
    }
    return render(request, "users/profile.html", context)
