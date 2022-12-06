from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from applications.account.serializers import UserRegisterSerializer

User = get_user_model()


# Create your views here.

class UserRegisterApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

