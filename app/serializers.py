from rest_framework import serializers

from app.models import User, Vacancy, WorkTime, Category, District


class WorkTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTime
        fields = 'name',


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name',


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = 'name',


class UserListSerializer(serializers.ModelSerializer):
    work_time = WorkTimeSerializer()
    district = DistrictSerializer()

    class Meta:
        model = User
        fields = 'email', 'seniority', 'specialist', 'work_time', 'district', 'additional_info'


class VacancyListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        exclude = 'id',


class VacancyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        exclude = 'id',
