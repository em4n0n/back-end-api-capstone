from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MenuItem
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'