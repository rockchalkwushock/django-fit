from django.contrib.auth.models import User
from rest_framework import generics

from .serializers import UserSerializer


class UserList(generics.ListAPIView):  # new
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):  # new
    queryset = User.objects.all()
    serializer_class = UserSerializer
