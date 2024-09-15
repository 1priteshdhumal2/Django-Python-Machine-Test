from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from .models import Client
from .serializers import ClientSerializer, ProjectSerializer, UserRegistrationSerializer, SimpleProjectListSerializer

# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
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

class UserProjectsListView(generics.ListAPIView):
    serializer_class = SimpleProjectListSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.projects.all()



