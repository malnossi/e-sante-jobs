from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, email: str, password: str, **kwargs):
        if not email:
            raise ValueError("email not provided")
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email: str, password: str, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)
        if kwargs.get("is_staff") is not True:
            raise ValueError("superuser most have is_staff=True")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("superuser most have is_superuser=True")
        return self.create_user(email=email, password=password, **kwargs)
