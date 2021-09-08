from django.db import models
from rest_framework import fields, serializers

from .models import Task

class TaskSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'