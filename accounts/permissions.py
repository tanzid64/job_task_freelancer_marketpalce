from rest_framework.permissions import BasePermission


class IsClient(BasePermission):
    """
    Permission class to check if the user is a client
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "client"
        )


class IsFreelancer(BasePermission):
    """
    Permission class to check if the user is a freelancer.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "freelancer"
        )
