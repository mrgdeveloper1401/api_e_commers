from builtins import str

from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView

from accounts.models import PublicNotifications
from accounts.pagination import PublicNotificationPagination
from accounts.serializers import PublicNotificationSerializer, ReadPublicNotificationSerializer, VerifyAccountSerializer


class PublicNotificationViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = PublicNotifications.objects.filter(is_active=True)
    serializer_class = PublicNotificationSerializer
    pagination_class = PublicNotificationPagination
    
    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return ReadPublicNotificationSerializer
        return super().get_serializer_class()


class VerifyAccountView(APIView):
    def post(self, request):
        ser_data = VerifyAccountSerializer(data=request.data)
        print(ser_data)
        ser_data.is_valid(raise_exception=True)
        ser_data.save()
        return Response({'message': 'accepted code'}, status=HTTP_200_OK)
