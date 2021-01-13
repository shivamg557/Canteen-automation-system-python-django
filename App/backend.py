from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
#from .models import Student,CanteenEmployee
class LoginBackend(BaseBackend):

    def authenticate(self, username=None, password=None):
        try:
            o = Student.objects.get(username=username, password=password)
        except Student.DoesNotExist:
            try:
                o = Company.objects.get(email=username, password=password)
            except Company.DoesNotExist:
                return None
        return User.objects.get(username=o.username)
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None