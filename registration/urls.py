from django.urls import path

from . import views

urlpatterns = [
    path('registration/', views.RegistrationAPIView.as_view()),
    path('authorization/', views.LoginAPIView.as_view()),
    path('user/', views.UserRetrieveUpdateAPIView.as_view())
]
