from django.db import models

# Create your models here.
from django.db import models

class SubmitData(models.Model):
    GENDER = models.CharField(max_length=200)
    AGE_GRP = models.IntegerField(default=20)
    INCOME = models.IntegerField(default=4)
    TRAVEL_STYL_1 = models.IntegerField(default=4)
    TRAVEL_STYL_2 = models.IntegerField(default=4)
    TRAVEL_STYL_3 = models.IntegerField(default=4)
    TRAVEL_STYL_4 = models.IntegerField(default=4)
    TRAVEL_STYL_5 = models.IntegerField(default=4)
    TRAVEL_STYL_6 = models.IntegerField(default=4)
    TRAVEL_STYL_7 = models.IntegerField(default=4)
    TRAVEL_STYL_8 = models.IntegerField(default=4)
    TRAVEL_MOTIVE_1 = models.IntegerField(default=4)
    TRAVEL_COMPANIONS_NUM = models.IntegerField(default=4)
    city = models.CharField(max_length=200)