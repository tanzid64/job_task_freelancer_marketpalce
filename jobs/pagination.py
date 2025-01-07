from rest_framework.pagination import CursorPagination
from rest_framework.response import Response


class JobCursorPagination(CursorPagination):
    page_size = 10  # Default number of items per page
    page_size_query_param = "page_size"  # Allow clients to override the page size
    max_page_size = 50  # Maximum number of items per page to prevent abuse
    ordering = "-created_at"  # Default ordering for pagination

    def get_ordering(self, request, queryset, view):
        ordering_param = request.query_params.get("ordering", None)
        if ordering_param == "asc":
            self.ordering = "created_at"  # Ascending order
        elif ordering_param == "desc":
            self.ordering = "-created_at"  # Descending order
        self.count = queryset.count() # save total jobs in the Jobs model
        return super().get_ordering(request, queryset, view)
    
    def get_paginated_response(self, data):
        return Response({
            'total_jobs': self.count,
            'jobs_per_page': self.page_size,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'data': data
        })
