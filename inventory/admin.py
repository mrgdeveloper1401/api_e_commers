from django.contrib import admin
from inventory.models import CertificateShop, ProfileShop, PersonalShop, RecordProduct
# Register your models here.


@admin.register(RecordProduct)
class IdentityInventoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ProfileShop)
class ProfileInventoryAdmin(admin.ModelAdmin):
    pass


@admin.register(CertificateShop)
class CertificateInventoryAdmin(admin.ModelAdmin):
    pass


@admin.register(PersonalShop)
class RecordProductAdmin(admin.ModelAdmin):
    pass
