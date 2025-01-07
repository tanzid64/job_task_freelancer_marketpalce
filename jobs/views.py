from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from accounts.permissions import IsClient
from jobs.filters import JobFilter
from jobs.permissions import IsJobCreatorOrAdminOnly
from jobs.serializers import JobSerializer
from jobs.models import Job

User = get_user_model()
# Create your views here.


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
    )
    filterset_class = JobFilter
    search_fields = ("title",)
    lookup_field = "slug"
    http_method_names = ["get", "post", "patch", "delete"]
    def get_queryset(self):
        queryset = super().get_queryset()
        sort_order = self.request.query_params.get("ordering", "desc") # Default to descending order
        if sort_order == "asc":
            queryset = queryset.order_by("created_at")
        elif sort_order == "desc":
            queryset = queryset.order_by("-created_at")
        return queryset


    def get_permissions(self):
        """
        Assign permissions based on action.
        - GET: Allow all users
        - POST: Allow clients only.
        - PUT, PATCH: Allow Job creator only
        - DELETE: Allow Job creator or admin only
        """
        if self.action in ["create"]:
            # Allow clients to create jobs
            permission_classes = [IsClient]
        else:
            permission_classes = [IsJobCreatorOrAdminOnly]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        request.data["created_by"] = request.user.id
        return super().create(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)
