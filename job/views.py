from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm

def jobs(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 2)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj,'j':jobs}
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


    context ={'job': job_details, "form":form}
    return render(request, "job/job_details.html", context)