import jwt

from datetime import datetime, timedata

from django.conf import settings
from django.contrib.auth.models import {
    AbstractBaseUser, BaseUserManager, PermissionsMixin
}

from django.db import models

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        """Create and return a User with an email, username and password """
        if username is None:
            raise TypeError('User must have a username')

        if email is None:
            raise TypeError('Must have an email address')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """ Create and return a User with admin persimssions """

        if password is None:
            raise TypeError('Admin User must have a password')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
        
