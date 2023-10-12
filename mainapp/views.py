from django.shortcuts import render

from mainapp.serializers import UserSerializer
from mainapp.models import User

from rest_framework.viewsets import ModelViewSet

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
