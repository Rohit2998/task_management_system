from rest_framework import generics, permissions
from django.contrib.auth.models import User
from users.seerializers import UserSerializer



class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  