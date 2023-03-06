from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return render(response, "main/base.html", {})

def landing(response):
    return render(response, "main/home.html", {})