from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('samples/', views.SampleList.as_view()),
    path('samples/<int:pk>/', views.SampleDetail.as_view()),

    path('skills/', views.SkillList.as_view()),
    path('skills/<int:pk>/', views.SkillDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)