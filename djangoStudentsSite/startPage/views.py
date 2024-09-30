from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def start(request: HttpRequest):
    return render(request, 'startPage/index.html')