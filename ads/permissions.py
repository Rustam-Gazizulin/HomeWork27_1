from rest_framework import permissions

from users.models import UserRoles


class IsOwnerOrStaff(permissions.BasePermission):
    message = "У вас нет прав на редактирование подборки"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner or request.user.role in [UserRoles.MODERATOR, UserRoles.ADMIN]:
            return True
        return False

