from rest_framework import generics
from littlelemonAPI.models import MenuItem
from littlelemonAPI.serializers import MenuItemSerializer

# Create your views here.
class SingleMenuItemViewSet(generics.RetrieveUpdateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemViewSet(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer