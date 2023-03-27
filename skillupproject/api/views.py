from .models import Sample, Skill
from .serializer import SampleSerializer, SkillSerializer
from rest_framework import generics

class SampleList(generics.ListCreateAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

class SampleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

class SkillList(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class SkillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer