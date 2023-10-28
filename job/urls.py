from django.urls import include,path
from . import views
app_name = 'jobs'
urlpatterns = [
path('', views.jobs),
path('<str:slug>',views.job_details,name = 'job_details'),
]