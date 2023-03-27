from django.db import models


# Create your models here.
class Sample(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    contents = models.TextField()

class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    software = models.CharField(max_length=100)
    level = models.IntegerField()