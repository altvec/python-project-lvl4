from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Model representing a user account."""
    pass

    def __str__(self):
        return self.username
