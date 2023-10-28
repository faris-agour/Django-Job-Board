from django.urls import include,path
from . import views
app_name = 'jobs'
urlpatterns = [
path('', views.jobs),
path('<int:id>',views.job_details,name = 'job_details'),
]