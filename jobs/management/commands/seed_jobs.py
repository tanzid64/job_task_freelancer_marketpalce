from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.conf import settings
from faker import Faker
from jobs.models import Job

User = get_user_model()
faker = Faker()

class Command(BaseCommand):
    """
    Command to seed the database with sample Job data.
    Only for users with client role.
    This command will work only in DEBUG mode.
    """
    help = "Seed the database with sample Job data (only for users with client role)"

    def handle(self, *args, **kwargs):
        if not settings.DEBUG:
            self.stdout.write(
                self.style.ERROR("This command can only be used in DEBUG mode.")
            )
            return
        # Get all users with the client role
        clients = User.objects.filter(role="client")
        if not clients.exists():
            self.stdout.write(self.style.ERROR("No clients available to assign jobs."))
            return

        # Create sample job data
        for _ in range(10):  # Create 10 jobs
            client = faker.random_element(clients)  # Randomly pick a client
            title = faker.sentence(nb_words=6)  # Generate a random job title
            job = Job.objects.create(
                created_by=client,
                title=title,
                slug=slugify(title),
                description=faker.paragraph(
                    nb_sentences=5
                ),  # Generate random description
                status=faker.random_element(
                    Job.JobStatus.values
                ),  # Randomly select a status
            )
            job.save()

        self.stdout.write(
            self.style.SUCCESS("Database seeded with Job data successfully!")
        )
