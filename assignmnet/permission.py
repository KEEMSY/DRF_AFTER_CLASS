from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwnerOnlyOrReadOnly(BasePermission):
    '''
    조회는 인증된 유저에게 허용
    수정 및 삭제는 작성자에 한에 허용
    '''
    def has_permission(self, request, view):
        return request.user and request.user_is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
