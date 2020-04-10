from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import User
from .serializers import  UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


