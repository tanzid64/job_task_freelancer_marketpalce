from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.constants import USER_ROLE
from accounts.managers import UserManager


class User(AbstractBaseUser):
    username = models.CharField(
        verbose_name="Username",
        max_length=255,
        unique=True,
    )
    email = models.EmailField(
        verbose_name="Email Address",
        max_length=255,
        unique=True,
    )
    name = models.CharField(verbose_name="Full Name", max_length=255)
    is_active = models.BooleanField(verbose_name="Is Active", default=False)
    role = models.CharField(
        verbose_name="Role", max_length=15, choices=USER_ROLE, default="client"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "username"]
    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return self.name

    @property
    def is_staff(self):
        return self.role == "admin"

    @property
    def is_freelancer(self):
        return self.role == "freelancer"

    @property
    def is_client(self):
        return self.role == "client"

    def has_perm(self, perm, obj=None):
        return self.role == "admin"

    def has_module_perms(self, app_label):
        return self.role == "admin"
