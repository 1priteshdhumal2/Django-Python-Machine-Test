from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer

# Create your views here.
class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = [TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated]
    
