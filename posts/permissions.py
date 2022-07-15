from math import perm
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #Faqatgina ko'rish uchun ruxsat beriladi
        if request.method in permissions.SAFE_METHODS:
            return True
        #O'zgartirish va yozish uchun ruxsatnoma post mualliflarigagina beriladi
        return obj.author == request.user