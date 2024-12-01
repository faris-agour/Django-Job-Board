from django.urls import include,path
from . import views
from . import api
app_name = 'jobs'
urlpatterns = [
path('', views.jobs,name='job_list'),
path('add',views.add_job,name = 'post_job'),
path('<str:slug>',views.job_details,name = 'job_details'),
    #api fun based view
path('api/jobs',api.jobs_api,name = 'jobs_api'),
    #api generic/class based view
path('api/jobs/<int:id>',api.JobDetails.as_view(),name = 'JobDetails'),

]