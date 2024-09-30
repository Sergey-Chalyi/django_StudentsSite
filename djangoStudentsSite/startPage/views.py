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
        'pages' : ['Looking for a job', 'Looking for a students']
    }
    return render(request, 'startPage/index.html', data)
