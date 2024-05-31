import django_filters
from django_filters import FilterSet, CharFilter

from app.models import User, Vacancy


class UserFilters(FilterSet):
    min_seniority = django_filters.NumberFilter(field_name='seniority', lookup_expr='gte')

    class Meta:
        model = User
        fields = ['seniority', ]


class VacancyFilters(FilterSet):
    search_title = CharFilter(method='filter_title')
    search_description = CharFilter(method='filter_description')

    class Meta:
        model = Vacancy
        fields = ['search_title', 'search_description']

    def filter_title(self, queryset, name, value):
        return queryset.filter(Vacancy__name__icontains=value)

    def filter_description(self, queryset, name, value):
        return queryset.filter(Vacancy__name__icontains=value)
