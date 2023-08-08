from django.shortcuts import render, redirect
from .models import User
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from argon2 import PasswordHasher
from .forms import RegisterForm

# Create your views here.


def login(request):
    return render(request, "accounts/login.html", {})


@csrf_exempt
def register(request):
    register_form = RegisterForm()
    context = {"forms": register_form}

    if request.method == "GET":
        return render(request, "accounts/register.html", context)
