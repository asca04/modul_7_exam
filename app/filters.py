import django_filters
from django_filters import FilterSet, CharFilter

from app.models import User, Vacancy


class UserFilters(FilterSet):
    min_seniority = django_filters.NumberFilter(field_name='seniority', lookup_expr='gte')

    class Meta:
        model = User
        fields = ['seniority', ]


class VacancyFilters(FilterSet):
    search_title = CharFilter(field_name='title', lookup_expr='icontains')
    search_description = CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Vacancy
        fields = ['search_title', 'search_description']



