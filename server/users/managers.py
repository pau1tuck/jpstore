from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, email, password, is_staff=False, is_active=True, **extra_fields):
        if not email:
            raise ValueError(_('Please enter a valid email address'))
        email = self.normalize_email(email)
        # Google OAuth2 backend sends unnecessary username field:
        extra_fields.pop("username", None)
        user = self.model(
            email=email, is_active=is_active, is_staff=is_staff, **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)