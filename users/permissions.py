from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsModer(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moders').exists()


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return request.user == view.get_object().owner
