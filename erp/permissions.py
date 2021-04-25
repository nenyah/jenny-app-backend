from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        """
        自定义权限：只允许对象所有者能够编辑
        :param request:
        :param view:
        :param obj:
        :return:
        """
        # 对象的所有者才有权限
        return bool(request.user and request.user.is_staff) or obj.created_by == request.user
