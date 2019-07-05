from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Permission for creator to edit and delte
    '''

    def has_object_permission(self, request, view, obj):
        # return True if request method = get
        if request.method in permissions.SAFE_METHODS:
            return True

        return (obj.creator == request.user)
