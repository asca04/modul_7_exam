from django.urls import path

from app.views import UserListAPIView, VacancyUpdateAPIView, VacancyListAPIView, VacancyCreateAPIView

urlpatterns = [
    path('user', UserListAPIView.as_view(), name='user-list'),
    path('vacancy', VacancyListAPIView.as_view(), name='vacancy-list'),
    path('vacancy', VacancyCreateAPIView.as_view(), name='vacancy-list'),
    path('vacancy/<int:pk>', VacancyUpdateAPIView.as_view(), name='vacancy-update'),
]