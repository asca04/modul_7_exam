from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
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
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    ordering_fields = ('id', 'seniority')


class VacancyUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyUpdateSerializer

    def put(self, request, *args, **kwargs):
        vacancy = Vacancy.objects.get(pk=kwargs['pk'])
        if vacancy.user.id == request.user.id:
            super(VacancyUpdateAPIView, self).put(request, *args, **kwargs)
            return Response('Update', status=status.HTTP_200_OK)
        return Response("you can't update vacancy")

    def patch(self, request, *args, **kwargs):
        vacancy = Vacancy.objects.get(pk=kwargs['pk'])
        if vacancy.user.id == request.user.id:
            super(VacancyUpdateAPIView, self).put(request, *args, **kwargs)

        return Response("you can't update vacancy")
