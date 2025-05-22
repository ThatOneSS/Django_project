from rest_framework import serializers
from .models import Region, Company, Car

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
class CarSerializer(serializers.ModelSerializer):
    region=serializers.StringRelatedField()
    company=serializers.StringRelatedField()
    class Meta:
        model = Car
        fields = '__all__'