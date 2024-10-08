from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User


class EmailOrPhoneBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, phone=None):
        try:
            if email:
                user = User.objects.get(email=email)
            elif phone:
                user = User.objects.get(profile__phone=phone)  # Assuming phone is in a profile model
            else:
                return None

            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
