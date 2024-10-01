from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def start(request: HttpRequest):
    data = {
        'page_title' : 'Start page',
        'menu' : [
            {
                'name' : 'Home page',
            },
            {
                'name': 'Looking for a job',
            },
            {
                'name': 'Looking for a students',
            },
            {
                'name': 'Support',
            },
        ],
        'pages' : [
            {
                'name' : 'Looking for a job',
                'path' : 'look_job_main'
            },
            # {
            #     'name': 'Looking for a students',
            #     'path': 'look_job_main'
            # },
        ]
    }
    return render(request, 'startPage/startPage_main.html', data)
