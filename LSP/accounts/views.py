from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import (
    CustomerRegistrationForm,
    ProviderRegistrationForm,
)

# Create your views here.



def register_customer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomerRegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form},
    )


def register_provider(request):
    if request.method == "POST":
        form = ProviderRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = ProviderRegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form},
    )


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(
            request,
            data=request.POST,
        )
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")
    else:
        form = AuthenticationForm(request)

    return render(
        request,
        "accounts/login.html",
        {"form": form},
    )


@login_required
def user_logout(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect("home")
