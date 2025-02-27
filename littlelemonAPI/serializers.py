from littlelemonAPI.models import MenuItem, ReservationItem
from rest_framework import serializers

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class ReservationItemSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    
    class Meta:
        model = ReservationItem
        fields = '__all__'