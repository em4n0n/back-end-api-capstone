from rest_framework.decorators import api_view
from rest_framework import generics
from .models import MenuItem
from .serializers import UserSerializer

# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = UserSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = UserSerializer