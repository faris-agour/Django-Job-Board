import django_filters

from .models import Job

from django.db.models import Q
class JobFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search', label='Search')
    # salary = django_filters.NumberFilter()
    salary__lt = django_filters.NumberFilter(field_name='salary', lookup_expr='lt')
    salary__gt = django_filters.NumberFilter(field_name='salary', lookup_expr='gt')

    class Meta:
        model = Job
        fields = ['search', 'jop_type', 'category', 'salary__lt','salary__gt','location']

    def filter_search(self, queryset, name, value):
        """
        Custom filter that searches both 'title' and 'description' fields.
        """
        if value:
            return queryset.filter(Q(title__icontains=value) | Q(description__icontains=value))
        return queryset
