from django.db import models

# Create your models here.
class Sample(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()