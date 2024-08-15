from django.contrib import admin
from address.models import Address
# Register your models here.


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
