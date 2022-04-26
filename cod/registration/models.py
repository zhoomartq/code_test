from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models



class MyUserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, email, password):
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, *extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    is_staff = models.BooleanField(default=False)
    username = None
    email = models.EmailField(unique=True, error_messages={'unique': 'Такой пользователь уже зарегистрирован в системе!'}, null=True)
    is_active = models.BooleanField(default=True) # def False


    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email