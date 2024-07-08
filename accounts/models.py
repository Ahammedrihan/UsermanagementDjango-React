from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extr_fields):
        if not email:
            raise ValueError("user must contain email")
        if not password:
            raise ValueError("user must contain pasword")

        normalized_email = self.normalize_email(email)
        user = self.model(email=normalized_email, **extr_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self,email,password,**extr_fields):
        user = self.create_user(email,password,**extr_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Accounts(AbstractBaseUser):
    Role = [
        ("admin","Admin"),
        ("user","user")
    ]
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    role = models.CharField(max_length=10,choices=Role, default="user")
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self,*args, **kwargs):
        if self.is_staff:
            self.role ="admin"
        super().save(*args, **kwargs)

    

