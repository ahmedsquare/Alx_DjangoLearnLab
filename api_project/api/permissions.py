from rest_framework.permissions import BasePermission

class IsEditor(BasePermission):
    """
    Custom permission to only allow users with the 'editor' role to edit or delete books.
    """

    def has_permission(self, request, view):
        # Allow read-only access to all users
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        # For write access (POST, PUT, PATCH, DELETE), check if the user has the 'editor' role
        return hasattr(request.user, 'role') and request.user.role == 'editor'