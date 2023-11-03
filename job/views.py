from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse

from .filters import JobFilter
from .forms import ApplyForm, PostJop
from .models import Job


def jobs(request):
    jobs = Job.objects.all()

    jobfilter = JobFilter(request.GET, queryset=jobs)
    jobs = jobfilter.qs

    paginator = Paginator(jobs, 3)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj, 'j': jobs, "filter": jobfilter}
    return render(request, "job/jobs.html", context)


def job_details(request, slug):
    job_details = Job.objects.get(slug=slug)

    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            form1 = form.save(commit=False)
            form1.job = job_details
            form1.save()
    else:
        form = ApplyForm()

    context = {'job': job_details, "form": form}
    return render(request, "job/job_details.html", context)


@login_required
def add_job(request):
    if request.method == "POST":

        form = PostJop(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)  # dont save in db yet
            form.owner = request.user
            form.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = PostJop()
    context = {'form': form}
    return render(request, "job/add_job.html", context)
