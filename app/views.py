from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.filters import UserFilters, VacancyFilters
from app.models import Vacancy, User
from app.serializers import VacancyListCreateSerializer, UserListSerializer, VacancyUpdateSerializer


# Create your views here.


class VacancyListAPIView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListCreateSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = VacancyFilters


class VacancyCreateAPIView(CreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListCreateSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = UserFilters
    filter_fields = ('work_time',)


class VacancyUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyUpdateSerializer

    def put(self, request, *args, **kwargs):
        vacancy = Vacancy.objects.get(pk=kwargs['pk'])
        if vacancy.title in self.request.user.related_name('vacancies').title:
            super(VacancyUpdateAPIView, self).put(request, *args, **kwargs)
        else:
            return Response("you can't update vacancy")
