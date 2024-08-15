from rest_framework.serializers import ModelSerializer
from address.models import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ['state', 'city', 'state', 'postal_code', 'description_address']

    def create(self, validated_data):
        return Address.objects.create(**validated_data)
