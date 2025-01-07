from rest_framework import serializers
from django.contrib.auth import get_user_model
from jobs.models import Job

User = get_user_model()


class UserForJobSerializer(serializers.ModelSerializer):
    """ 
    Helper serializer to display only the user's id, email, username, name and role while retriving a job details.
    """
    class Meta:
        model = User
        fields = ("id", "email", "username", "name", "role")


class JobSerializer(serializers.ModelSerializer):
    creator = UserForJobSerializer(read_only=True, source="created_by")

    class Meta:
        model = Job
        fields = (
            "id",
            "created_by",
            "title",
            "slug",
            "description",
            "creator",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at", "slug")
        extra_kwargs = {
            "created_by": {"write_only": True},
        }

