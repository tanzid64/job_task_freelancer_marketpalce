from django_filters import rest_framework as filters
from jobs.models import Job

class JobFilter(filters.FilterSet):
    status = filters.CharFilter(field_name='status', lookup_expr='iexact')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    
    class Meta:
        model = Job
        fields = ('status', 'title')