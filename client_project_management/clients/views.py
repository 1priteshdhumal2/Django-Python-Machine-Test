from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer, UserRegistrationSerializer

# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = [TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = [TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated]

class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    authentication_classes = [TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        client = Client.objects.get(pk=self.kwargs['pk'])
        serializer.save(client = client, created_by=self.request.user)



