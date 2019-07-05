from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    '''creates new user instance'''

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('User should have an Email, or Create One')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    '''Creates A super User'''

    def create_superuser(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('User should have an Email, or Create One')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=254, unique=True, verbose_name='email adress')
    name = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    joined_date = models.DateField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
