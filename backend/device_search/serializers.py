from rest_framework import serializers
from .models import EudamedData, FdaData

class EudamedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EudamedData
        fields = '__all__' 

class FdaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FdaData
        fields = '__all__'
