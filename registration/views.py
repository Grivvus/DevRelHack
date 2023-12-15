from rest_framework import generics
from .models import User, Role, Characteristics
from .serializers import CharacteristicsSerializer, UserSerializer, RoleSerializer


# Create your views here.

class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoleAPIView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class CharacteristicsAPIView(generics.ListAPIView):
    queryset = Characteristics.objects.all()
    serializer_class = CharacteristicsSerializer
