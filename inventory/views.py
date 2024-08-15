from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from inventory.models import PersonalShop
from inventory.serialziers import PersonalShopSerializer
# Create your views here.


class PersonalShopViewSet(CreateModelMixin, GenericViewSet):
    queryset = PersonalShop.objects.all()
    serializer_class = PersonalShopSerializer

