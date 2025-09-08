from rest_framework import serializers
from agents.models import Tool
class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'