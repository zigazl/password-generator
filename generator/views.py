from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, "generator/home.html", {"password": "agrdpko2kpo4t"})


def about(request):
    return render(request, "generator/about.html")


def password(request):
    thepassword = ""
    characters = list("abcdefghijklmnopqrstuvwxyz")

    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("special"):
        characters.extend(list("!@#$%^&*()"))
    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))

    length = int(request.GET.get("password_length", 12))

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, "generator/password.html", {"password": thepassword})
