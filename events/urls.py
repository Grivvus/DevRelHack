from django.urls import path
from events.views import CompetitionAPIView, TagAPIView


urlpatterns = [
    path('api/v1/competitionlist/', CompetitionAPIView.as_view()),
    path('api/v1/taglist/', TagAPIView.as_view())
]