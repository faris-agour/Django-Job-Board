from django.urls import include,path
from . import views
app_name = 'jobs'
urlpatterns = [
path('', views.jobs,name='job_list'),
path('add',views.add_job,name = 'post_job'),
path('<str:slug>',views.job_details,name = 'job_details'),
]