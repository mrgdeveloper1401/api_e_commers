from rest_framework.permissions import BasePermission, SAFE_METHODS


class ProfilePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.user == request.user
