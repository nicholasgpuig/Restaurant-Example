from rest_framework import generics
from littlelemonAPI.models import MenuItem, ReservationItem
from littlelemonAPI.serializers import MenuItemSerializer, ReservationItemSerializer

# Create your views here.
class SingleMenuItemViewSet(generics.RetrieveUpdateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemViewSet(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        queryset = MenuItem.objects.all()
        name = self.request.query_params.get('name')
        if name:
            queryset = MenuItem.objects.filter(name=name)
        return queryset

class ReservationItemViewSet(generics.ListCreateAPIView):
    queryset = ReservationItem.objects.all()
    serializer_class = ReservationItemSerializer