from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from lookForJob.models import Job


def look_job_main(request: HttpRequest):
    data = {
        'jobs': Job.objects.all()
    }
    return render(request, 'lookForJob/lookForJob_main.html', data)


def job_blank(request: HttpRequest, job_slug):
    data = {
        'job' : get_object_or_404(Job, slug = job_slug)
    }
    return render(request, 'lookForJob/job_page.html', data)