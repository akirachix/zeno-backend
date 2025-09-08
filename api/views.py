from django.shortcuts import render
from rest_framework import viewsets
from agents.models import Tool
from .serializers import ToolSerializer
class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all().order_by('tool_name')
    serializer_class = ToolSerializer