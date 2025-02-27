from rest_framework import generics
from littlelemonAPI.models import MenuItem, ReservationItem
from littlelemonAPI.serializers import MenuItemSerializer, ReservationItemSerializer
from rest_framework.permissions import IsAuthenticated

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
    permission_classes  = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)

    def get_queryset(self):
        queryset = ReservationItem.objects.filter(user=self.request.user)
        return queryset

class SingleReservationItemViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReservationItem.objects.all()
    serializer_class = ReservationItemSerializer