import django_filters
from rest_framework import viewsets, filters

from .models import Sample
from .serializer import SampleSerializer

# Create your views here.
class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer