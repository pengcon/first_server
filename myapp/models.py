from django.db import models

# Create your models here.
from django.db import models

class MyData(models.Model):
    Data1 = models.CharField(max_length=200)
    Data2 = models.CharField(max_length=200)
    Data3 = models.CharField(max_length=200)
    Data4 = models.CharField(max_length=200)