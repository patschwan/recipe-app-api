from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class UserManager(BaseUserManager):

    # extra_fields -> take any new fields, we add will programming
    def create_user(self, email, password=None, **extra_fields):
        """creates and saves a new user"""
        if not email:
            raise ValueError('User must have a email address')
        # this is short for get standard user model and add things
        # user = self.model(email=email, **extra_fields)
        # normalize_email is a helper functions for the "UPPERCASE"
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        # is for multiple DBs
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)  # because we change the user

        return user


# we abstract from AbstractBaseUser and PermissionsMixin
class User(AbstractBaseUser, PermissionsMixin):
    """custom user model that supports using email instead username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()  # create new UserManager

    USERNAME_FIELD = 'email'
