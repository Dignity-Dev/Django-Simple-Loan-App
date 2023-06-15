from django.shortcuts import render

from rest_framework import generics
from .models import Scenario
from .serializers import ScenarioSerializer

class ScenarioListCreateView(generics.ListCreateAPIView):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer

class ScenarioRetrieveView(generics.RetrieveAPIView):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer
