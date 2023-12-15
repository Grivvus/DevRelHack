from rest_framework import generics
from .models import Competition, Tag
from .serializers import CompetitionSerializer, TagSerializer
import django_filters

# Create your views here.

class CompetitionAPIView(generics.ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class TagAPIView(generics.ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = TagSerializer