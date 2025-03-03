from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Book(models.Model):
    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date  = models.DateField()


class CustomUserManager(BaseUserManager):
    """Custom manager for handling user creation with additional fields."""

    def create_user(self, username, email, date_of_birth, password=None, **extra_fields):
        """Creates and returns a regular user."""
        if not email:
            raise ValueError("The Email field must be set")  # Ensure email is provided
        email = self.normalize_email(email)  # Normalize email
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)  # Hash password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, password=None, **extra_fields):
        """Creates and returns a superuser."""
        extra_fields.setdefault('is_staff', True)  # Superusers must be staff
        extra_fields.setdefault('is_superuser', True)  # Superusers must have all permissions
        return self.create_user(username, email, date_of_birth, password, **extra_fields)


class CustomUser(AbstractUser):
    """Custom user model extending AbstractUser with additional fields."""
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    objects = CustomUserManager()  # Set the custom manager

    def __str__(self):
        return self.username  # Display username when printed
