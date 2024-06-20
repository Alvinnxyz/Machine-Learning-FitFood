from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import filters

# Create your views here.

class IsinutView(generics.RetrieveAPIView):
    permission_classes = []
    serializer_class = IsinutSerializers
    queryset = Nutrition.objects.all()
    
class ListnutView(generics.ListAPIView):
    queryset = Nutrition.objects.all()
    serializer_class = NutritionSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class NutritionSearchView(generics.ListAPIView):
    queryset = Nutrition.objects.all()
    serializer_class = NutritionSearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset