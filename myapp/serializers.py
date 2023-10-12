from rest_framework import  serializers
from .models import SubmitData

class SubmitDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmitData
        fields = ['id','GENDER','AGE_GRP','INCOME',
                  'TRAVEL_STYL_1','TRAVEL_STYL_2','TRAVEL_STYL_3',
                  'TRAVEL_STYL_4','TRAVEL_STYL_5','TRAVEL_STYL_6',
                  'TRAVEL_STYL_7','TRAVEL_STYL_8','TRAVEL_MOTIVE_1',
                  'TRAVEL_COMPANIONS_NUM','city']
