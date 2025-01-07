from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsJobCreatorOrAdminOnly(BasePermission):
    """
    Allows access only to job creator or admin.
    - PUT, PATCH: Allow job creator only
    - DELETE: Allow job creator or admin only
    - GET, POST: Allow all
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'POST':
            return request.user.role == 'client'
        
        if request.method in ['PUT', 'PATCH']:
            return obj.created_by == request.user
        
        if request.method == 'DELETE':
            return obj.created_by == request.user or request.user.is_admin
        
        return False
