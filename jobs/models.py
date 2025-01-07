from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Job(models.Model):
    class JobStatus(models.TextChoices):
        OPEN = "open", "Open"
        CLOSED = "closed", "Closed"
        IN_PROGRESS = "in_progress", "In_Progress"

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs")
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=15, choices=JobStatus.choices, default=JobStatus.OPEN
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)
