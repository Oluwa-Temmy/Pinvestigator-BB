from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>This is pinvestigator home page<h1>")

def v1(response):
    return HttpResponse("<h1>view 1 test<h1>")