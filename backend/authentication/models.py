from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .manager import CustomUserManager
from .validators import username_regex, email_regex, phone_regex


USER_TYPE = [('admin', 'Admin'), ('stafe','Stafe'), ('user', 'User')]

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, validators=[username_regex], max_length=35, null=False, blank=False)
    email = models.EmailField(unique=True, validators=[email_regex], max_length=255)
    phone = models.CharField(unique=True, validators=[phone_regex], max_length=20, blank=True, null=True)
    role = models.CharField(choices=USER_TYPE, default='user', max_length=255)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=30)
    
    objects = CustomUserManager()

    class Meta:
        ordering = ['-username']
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        indexes = [
            models.Index(fields=['username'], name='username_idx'),
            models.Index(fields=['email'], name='email_idx'),
        ]
        default_permissions = ['view', 'add', 'change', 'delete']
        
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['role', 'email']


    def __str__(self):
        return self.username