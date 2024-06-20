from rest_framework import serializers
from .models import Nutrition

def build_absolute_uri(path:str):
    return f"http://127.0.0.1:8000{path}"

class NutritionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Nutrition
        fields = ('name','calories')

class IsinutSerializers(serializers.ModelSerializer):   
    class Meta:
        model = Nutrition
        fields = ('name','calories')
class NutritionSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrition
        fields = ['name', 'calories']