from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
from django.utils.translation import gettext_lazy as _

USER_TYPE = (
    ('Salon', 'Salon'),
    ('Customer', 'Customer'),
    ('Admin', 'Admin'),
)
class LowercaseEmailField(models.EmailField):
    # Override EmailField to convert emails to lowercase before saving.
    def to_python(self, value):
        """
        Convert email to lowercase.
        """
        value = super(LowercaseEmailField, self).to_python(value)
        # Value can be None so check that it's a string before lowercasing.
        if isinstance(value, str):
            return value.lower()
        return value
    
class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="profile-pic", blank=True, null=True)
    email = LowercaseEmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE, default='Admin')
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        if self.first_name:
            return  f"{self.first_name}"
        return self.email