from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Passwords do not match.')
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password']
        )

        return user

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name','projects', 'created_at', 'updated_at', 'created_by']
        read_only_fields = ['created_at', 'created_by']