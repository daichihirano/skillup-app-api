from rest_framework import serializers

from .models import Sample, Skill

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ['id', 'title', 'contents']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'type', 'software', 'level']
