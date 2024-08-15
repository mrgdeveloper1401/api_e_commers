from rest_framework.viewsets import ModelViewSet
from address.models import Address
from address.serializers import AddressSerializer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.filter(is_active=True)
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
