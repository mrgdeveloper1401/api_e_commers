from django.urls import include
from rest_framework.urls import path
from accounts.views import PublicNotificationViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('public_notification', PublicNotificationViewSet, basename='public_notification')


app_name = 'accounts'
urlpatterns = [
    path('', include(router.urls)),
]
