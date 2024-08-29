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
    
class UserSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='username')
    class Meta:
        model = User
        fields = ['id', 'name']

class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    client = serializers.ReadOnlyField(source='client.client_name')
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Project
        fields = ['id', 'project_name','client', 'users', 'created_at', 'created_by']
        read_only_fields = ['client','created_at', 'created_by']

    def create(self, validated_data):
        users_data = self.initial_data.get('users',[])
        validated_data.pop('users',[])

        project = Project.objects.create(**validated_data)
        for user_data in users_data:
            user = User.objects.get(pk=user_data['id'])
            print(user)
            project.users.add(user)
        return project

class SimpleProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_name']

class SimpleProjectListSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'created_at', 'created_by']

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    projects = SimpleProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name','projects', 'created_at', 'updated_at', 'created_by']
        read_only_fields = ['created_at', 'created_by']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if not representation.get('projects'):
            representation.pop('projects')
        
        return representation