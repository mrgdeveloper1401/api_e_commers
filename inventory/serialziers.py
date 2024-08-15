from rest_framework.serializers import ModelSerializer

from inventory.models import PersonalShop


class PersonalShopSerializer(ModelSerializer):
    class Meta:
        model = PersonalShop
        fields = ['first_name', 'last_name', 'nation_code', 'mobile_phone', 'email', 'is_legal']
