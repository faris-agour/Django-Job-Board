from django.shortcuts import render
from .models import Job


def job_list(request):
    job_list = Job.objects.all()
    context = {'jobs': job_list}
    return render(request, "job/job_list.html", context)


def job_details(request, id):
    job_details = Job.objects.get(id=id)
    context ={'job': job_details}

    return render(request, "job/job_details.html", context)