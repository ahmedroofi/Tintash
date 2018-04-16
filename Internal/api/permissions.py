from rest_framework import permissions


class PHOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.employee


class IsAuthenticatedOrCreate(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return super(IsAuthenticatedOrCreate, self).has_permission(request, view)