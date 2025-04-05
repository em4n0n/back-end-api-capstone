from rest_framework.decorators import api_view
from rest_framework import generics
from .models import MenuItem
from .serializers import BookingSerializer, Booking
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = BookingSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = BookingSerializer
    
class BookingViewset(ModelViewSet):
    queryset= Booking.objects.all()
    serializer_class = BookingSerializer