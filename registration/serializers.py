from rest_framework import serializers
from .models import User, Role, Characteristics


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('name')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields=('role')

class CharacteristicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristics
        fields=('specialization')