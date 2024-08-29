from django.urls import path
from .views import ClientListCreateView, UserRegistrationView
from rest_framework.authtoken import views

urlpatterns = [
    path('signup/', UserRegistrationView.as_view(), name='signup'),
    path('login/', views.obtain_auth_token, name='login'),
    path('clients/', ClientListCreateView.as_view(), name='clients'),
]