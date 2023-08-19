from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied, NotAuthenticated


from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #get,head,options이라면 조회가능
        if request.method in permissions.SAFE_METHODS:
            return True

        # 요청자(request.user)가 객체(Blog)의 user와 동일한지 확인
        return obj.user == request.user


class IsAuthorOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        print("호출")
        return False

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            #유저 동일한지 확인
            if obj.user == request.user:
                return True
            else:
                raise PermissionDenied() #유저가 다르다면
        raise NotAuthenticated() # 유저 존재하지않는다면

