from django.urls import include,path
from . import views
app_name = 'contact'
urlpatterns = [
path('', views.contact,name='contact'),
# path('', views.jobs,name='job_list'),
]