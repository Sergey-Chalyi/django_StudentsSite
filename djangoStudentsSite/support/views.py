from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def support_main(request: HttpRequest):
    return render(request, 'support/support_main.html')