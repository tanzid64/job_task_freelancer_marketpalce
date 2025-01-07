from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings
from faker import Faker

User = get_user_model()
faker = Faker()

class Command(BaseCommand):
    """
    Seed the database with sample User data.
    All User's password is set to 'example@123'.
    One admin will be created.
    Admin user password is set to 'admin@123'.
    """
    help = "Seed the database with sample User data"

    def handle(self, *args, **kwargs):
        # Check if DEBUG is True
        if not settings.DEBUG:
            self.stdout.write(
                self.style.ERROR("This command can only be used in DEBUG mode.")
            )
            return
        # Create sample users
        sample_data = [
            {
                "username": "freelancer1",
                "email": "freelancer1@example.com",
                "name": "Freelancer One",
                "role": "freelancer",
                "password": "example@123",
            },
            {
                "username": "client1",
                "email": "client1@example.com",
                "name": "Client One",
                "role": "client",
                "password": "example@123",
            },
            {
                "username": "admin1",
                "email": "admin1@example.com",
                "name": "Admin One",
                "role": "admin",
                "is_admin": True,
                "password": "admin@123",
            },
        ]

        # Create specific users
        for data in sample_data:
            user = User.objects.create_user(
                    username=data["username"],
                    email=data["email"],
                    name=data["name"],
                    role=data["role"],
                    is_admin=data.get("is_admin", False),
                    is_active=data.get("is_active", True),
                )
            user.set_password(data["password"])
            user.save()

        # Generate random users
        for _ in range(10):
            password = "example@123"
            user = User.objects.create(
                username=faker.user_name(),
                email=faker.email(),
                name=faker.name(),
                role=faker.random_element(["freelancer", "client"]),
                is_active=True,
            )
            user.set_password(password)
            user.save()

        self.stdout.write(self.style.SUCCESS("Database seeded with User data successfully!"))

