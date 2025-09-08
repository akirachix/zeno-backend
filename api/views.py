
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from agents.models import Agent
from .serializers import AgentSerializer
from agents.models import Tool
from .serializers import ToolSerializer

class AgentListCreateView(generics.ListCreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class AgentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    lookup_field = 'agent_id'


class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all().order_by('tool_name')
    serializer_class = ToolSerializer

