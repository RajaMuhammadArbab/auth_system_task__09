from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'admin'

class IsEditorOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role in ['admin', 'editor']

class IsViewerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
