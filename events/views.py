from rest_framework import generics
from .models import Competition, Tag
from .serializers import CompetitionSerializer, TagSerializer


# Create your views here.

class CompetitionAPIView(generics.ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class TagAPIView(generics.ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = TagSerializer