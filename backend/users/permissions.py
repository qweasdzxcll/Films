from .models import User
from rest_framework.permissions import BasePermission

class IsAuthenticatedUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_status:
            return True



