from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError


# Create your models here.

class UserManager(BaseUserManager["User"]):
    def create_user(self, phone_number, email=None, password=None, first_name=None, last_name=None):
        if email:
            email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, email=email, first_name=first_name, last_name=last_name)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_admin_user(self, username, password, email=None, first_name=None, last_name=None):
        if email:
            email = self.normalize_email(email)
        if password:
            password = self.normalize_email(password)
        user = self.model(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()
        return user


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=True, blank=True, null=True)
    short_description = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=11, blank=True, unique=True, null=True)
    email = models.EmailField(max_length=100, unique=True, blank=True)
    twitch = models.URLField(max_length=120)
    twitter = models.URLField(max_length=120)
    youtube = models.URLField(max_length=120)
    instagram = models.URLField(max_length=120)
    facebook = models.URLField(max_length=120)
    tiktok = models.URLField(max_length=120)
    discord = models.URLField(max_length=120)
    website = models.URLField(max_length=120)

    USERNAME_FIELD = "phone_number"

    objects = UserManager()

    def __str__(self):
        return f"{self.phone_number or self.email}"

    def clean(self):
        super.clean()
        if not self.phone_number or not self.email:
            raise ValidationError(message="for creating user should have one phone number or email at least.", )

    def save(self, *args, **kwargs):
        self.clean()
        super.save(self, *args, **kwargs)
