from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

class Staff(AbstractUser):
    position = models.CharField(default='', max_length=200)
    groups = models.ManyToManyField(Group, related_name='users')
    user_permissions = models.ManyToManyField(Permission, related_name='users')

