from datetime import timedelta

from django.utils import timezone
from rest_framework.permissions import BasePermission


class CanWriteAfter3Days(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.join_date < (timezone.now() - timedelta(days=3)))


class CanWriteAfter3Min(BasePermission):
    def has_permission(self, request, view):
        bool(request.user and request.user.join_date < (timezone.now() - timedelta(minutes=3)))
