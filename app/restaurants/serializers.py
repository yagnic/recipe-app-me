from rest_framework import serializers

from core.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'image', 'mobile')
        read_only_fields = ('id',)
