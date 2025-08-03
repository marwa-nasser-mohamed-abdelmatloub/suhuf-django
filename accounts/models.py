from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# [AMS]:- Custom User model extending AbstractUser
class CustomUser(AbstractUser):
    # [AMS]:- Additional fields for user profile
    phone_number = models.CharField(
        _('phone number'),
        max_length=20,
        unique=True
    )
    profile_picture = models.ImageField(
        _('profile picture'),
        upload_to='profile_pictures/',
        blank=True,
        null=True
    )
    full_name = models.CharField(
        _('full name'),
        max_length=255,
        blank=True,
        null=True
    )
    email = models.EmailField(
        _('email address'),
        unique=True
    )
    # [AMS]:- for future if demand to make role-based access control [as a teacher of Quran or student]
    is_quran_teacher = models.BooleanField(
        _('is quran teacher'),
        default=False
    )
    is_student = models.BooleanField(
        _('is student'),
        default=True
    )
    
    # [AMS]:- Required fields for custom user model
    REQUIRED_FIELDS = ['email', 'full_name', 'phone_number']
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    def __str__(self):
        return self.username