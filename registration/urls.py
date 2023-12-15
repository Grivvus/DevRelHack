from django.urls import path
from registration.views import UserAPIView, RoleAPIView, CharacteristicsAPIView

urlpatterns = [
    path('api/v1/userlist/', UserAPIView.as_view()),
    path('api/v1/rolelist/', RoleAPIView.as_view()),
    path('api/v1/characteristicslist/', CharacteristicsAPIView.as_view())

]