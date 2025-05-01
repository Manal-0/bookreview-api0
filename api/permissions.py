from rest_framework import permissions

class IsReviewOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # يسمح فقط لمالك الريفيو بالتعديل أو الحذف
        return obj.user == request.user
