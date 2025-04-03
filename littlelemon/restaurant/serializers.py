from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MenuItem, Booking
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'