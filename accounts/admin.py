from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from accounts.models import Users, PublicNotifications, MobileVerify


# Register your models here.
@admin.register(Users)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("mobile_phone", "password")}),
        (_("Personal info"), {"fields": ("email", "first_name", "last_name", "bio", "birth_date")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "verify_account",
                    'is_accepted_sheba_number',
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ('mobile_phone', "usable_password", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "mobile_phone", "is_staff", 'is_active', 'is_superuser', 'date_joined',
                    'verify_account')
    list_filter = ("is_staff", "is_superuser", "is_active", "groups", 'date_joined', 'verify_account')
    search_fields = ("mobile_phone", "email")
    ordering = ("date_joined",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    readonly_fields = ['date_joined']
    list_display_links = ['email', 'mobile_phone']


@admin.register(PublicNotifications)
class PublicNotificationsAdmin(admin.ModelAdmin):
    pass


@admin.register(MobileVerify)
class EmailVerifyAdmin(admin.ModelAdmin):
    list_display = ['mobile_phone', 'code', 'expired_code', 'create_at']
