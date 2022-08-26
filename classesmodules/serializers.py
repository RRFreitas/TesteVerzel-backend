from .models import Class, Module
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class ModuleSerializer(serializers.ModelSerializer):
    classes = serializers.StringRelatedField(many=True)

    class Meta:
        model = Module
        fields = ['id', 'name', 'classes']

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'name', 'date', 'module']