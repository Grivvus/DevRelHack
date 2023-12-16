from rest_framework import serializers

from .models import Competition, Tag


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields=('name', 'time_start', 'time_end',
                'description','level', 'max_num_of_participants',
                'sponsors', 'meaner')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields= ('name',)