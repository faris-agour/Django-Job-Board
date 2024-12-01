# views in api
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Job
from .serializers import JobSerializer


# i will make this function based view
@api_view(['GET'])
def jobs_api(request):
    alljobs = Job.objects.all()
    data = JobSerializer(alljobs, many=True).data
    return Response({"Jobs": data})


# and this one will be class based view
from rest_framework import generics


class JobDetails(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'
