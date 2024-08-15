from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include

from inventory.views import PersonalShopViewSet


router = DefaultRouter()
router.register('personal_shop', PersonalShopViewSet, basename='personal_shop')

app_name = 'inventory'
urlpatterns = [

] + router.urls
