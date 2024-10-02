from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

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
