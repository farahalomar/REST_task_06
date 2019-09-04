from rest_framework.permissions import BasePermission
from datetime import timedelta, datetime, date

class Is_Staff(BasePermission):
	def has_object_permission(self, request, view, obj):
		if obj.user == request.user or request.user.is_staff:
			return True
		return False 

class IsModified(BasePermission):
	def has_object_permission(self, request, view, obj):
		if obj.date > (date.today()+ timedelta(days=3)):
			return True
		return False 