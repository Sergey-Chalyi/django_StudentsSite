from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def look_student_main(request: HttpRequest):
    return render(request, 'lookForStudent/lookForStudent_main.html')
