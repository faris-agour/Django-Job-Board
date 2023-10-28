from django.shortcuts import render
from .models import Job


def jobs(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, "job/jobs.html", context)


def job_details(request, id):
    job_details = Job.objects.get(id=id)
    context ={'job': job_details}

    return render(request, "job/job_details.html", context)