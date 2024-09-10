from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Admin: admin@gamil.com, Password: Satish@123
class CustomerUser(AbstractUser):
    username = None
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
