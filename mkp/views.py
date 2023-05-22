from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

tasks = ["foo", "bar", "baz"]

def index(request):
    return render(request, "mkp/index.html")
