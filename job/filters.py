import django_filters

from .models import Job


class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    # salary = django_filters.NumberFilter()
    salary__lt = django_filters.NumberFilter(field_name='salary', lookup_expr='lt')
    salary__gt = django_filters.NumberFilter(field_name='salary', lookup_expr='gt')

    class Meta:
        model = Job
        fields = ['title', 'description', 'jop_type', 'category', 'salary__lt','salary__gt']
