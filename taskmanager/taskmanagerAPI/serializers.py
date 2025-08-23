from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'description', 'completed', 'completion_date', 'user']
        read_only_fields = ['id', 'completed', 'user']
    
    def validate_completion_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Completion date cannot be in the past.")
        return value

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email',]