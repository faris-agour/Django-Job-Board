from django.urls import include,path
from . import views
urlpatterns = [
path('', views.jop_details),
path('<int:id>',views.job_details),
]