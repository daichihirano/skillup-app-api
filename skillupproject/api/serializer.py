from rest_framework import serializers

from .models import Sample, Skill

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ['id', 'title', 'contents']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['category', 'name', 'level']



class SkillItemSerializer(serializers.Serializer):
    name = serializers.CharField()
    level = serializers.IntegerField()

class SkillCategorySerializer(serializers.Serializer):
    category = serializers.CharField()
    skills = SkillItemSerializer(many=True)


