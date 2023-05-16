from .models import Sample, Skill
from .serializer import SampleSerializer, SkillSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class SampleList(generics.ListCreateAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

class SampleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


# Skillを配列の形式に変換してレスポンスする
class SkillsAPIView(APIView):
    def get(self, request, format=None):
        # SkillModelから全てを取得
        queryset = Skill.objects.all().order_by('category', 'name')
        # categoryでまとめてレスポンスを返すためcategoryごとに分類した辞書型を作成
        categories = {}
        # 取得したskillに含まれるcategoryを取得
        for skill in queryset:
            if skill.category not in categories:
                categories[skill.category] = []
            # 同じcategoryに所属するskill.nameとskill.levelをまとめる
            categories[skill.category].append({'name': skill.name, 'level': skill.level})
        skills_data = []
        for category, skills in categories.items():
            skills_data.append({'category': category, 'skills': skills})
        return Response(skills_data)
    
    def post(self, request, format=None):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
