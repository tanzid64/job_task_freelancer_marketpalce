from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom manager for the User model.
    """

    def create_user(
        self, email, username, name, password=None, role="client", **extra_fields
    ):
        """
        Creates and saves a regular user with the specified details.
        """
        if not email:
            raise ValueError("The Email field is required.")
        if not username:
            raise ValueError("The Username field is required.")
        if not name:
            raise ValueError("The Name field is required.")

        email = self.normalize_email(email)
        user = self.model(
            email=email, username=username, name=name, role=role, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, password=None, **extra_fields):
        """
        Creates and saves a superuser with admin privileges.
        """
        # Superuser must always have the role set to 'admin'
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_admin", True)
        return self.create_user(
            email,
            username,
            name,
            password,
            role="admin",
            **extra_fields
        )
