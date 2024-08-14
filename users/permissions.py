from rest_framework import permissions


class IsModer(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moders').exists()


class IsNotModer(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.groups.filter(name='moders').exists()
