from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def look_job_main(request: HttpRequest):
    return render(request, 'lookForJob/lookForJob_main.html')
