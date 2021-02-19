from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from shortuuidfield import ShortUUIDField


# Customized User Manager
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('Please send a valid email!')
        if not username:
            raise ValueError('Please send a username!')
        if not password:
            raise ValueError('Please send a valid password!')
        user = self.model(email=self.normalize_email(email), username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, username, password, **extra_fields)


# Customized User Model
class ECUser(AbstractBaseUser, PermissionsMixin):
    uid = ShortUUIDField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    telephone = models.CharField(max_length=10, blank=True)
    avatar = models.URLField(max_length=200, default="")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    EMAIL_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username





