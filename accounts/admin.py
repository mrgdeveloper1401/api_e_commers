from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from accounts.models import Users, PublicNotifications, EmailVerify


# Register your models here.
@admin.register(Users)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("email", "first_name", "last_name", "mobile_phone", "bio", "birth_date")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "verify_email",
                    "verify_phone",
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
                "fields": ('email', "username", "usable_password", "password1", "password2"),
            },
        ),
    )
    list_display = ("username", "email", "mobile_phone", "is_staff", 'is_active', 'is_superuser', 'date_joined')
    list_filter = ("is_staff", "is_superuser", "is_active", "groups", 'date_joined')
    search_fields = ("username", "email")
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    readonly_fields = ['date_joined']


@admin.register(PublicNotifications)
class PublicNotificationsAdmin(admin.ModelAdmin):
    pass


@admin.register(EmailVerify)
class EmailVerifyAdmin(admin.ModelAdmin):
    list_display = ['email', 'code', 'expired_code', 'create_at']
