from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from accounts.models import PublicNotifications
from accounts.pagination import PublicNotificationPagination
from accounts.serializers import PublicNotificationSerializer, ReadPublicNotificationSerializer


class PublicNotificationViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = PublicNotifications.objects.filter(is_active=True)
    serializer_class = PublicNotificationSerializer
    pagination_class = PublicNotificationPagination
    
    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return ReadPublicNotificationSerializer
        return super().get_serializer_class()
