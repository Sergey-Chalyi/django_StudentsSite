from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from lookForStudent.models import Student


def look_student_main(request: HttpRequest):
    data = {
        'students': [
            {
                'name': 'Sergey',
                'age': 20,
                'specialization': 'agronomy'
            },
            {
                'name': 'Anna',
                'age': 22,
                'specialization': 'computer science'
            },
            {
                'name': 'Dmitry',
                'age': 21,
                'specialization': 'mathematics'
            },
            {
                'name': 'Elena',
                'age': 19,
                'specialization': 'biology'
            },
            {
                'name': 'Igor',
                'age': 23,
                'specialization': 'engineering'
            },
        ]
    }

    return render(request, 'lookForStudent/lookForStudent_main.html', data)


def student_blank(request: HttpRequest, student_slug):
    data = {
        'student' : get_object_or_404(Student, slug = student_slug)
    }
    return render(request, 'lookForStudent/student_page.html', data)