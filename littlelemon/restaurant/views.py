from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Menu
from .serializers import BookingSerializer, Booking, MenuItemSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]
    
class BookingViewset(ModelViewSet):
    queryset= Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]