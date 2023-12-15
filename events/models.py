import uuid

from django.db import models

class Competition(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200,
                            help_text='Название мероприятия')
    time_start = models.DateTimeField(null=True)
    time_end = models.DateTimeField(null=True)
    description = models.CharField(max_length=1000)
    max_num_of_participants = models.IntegerField()
    level = models.IntegerField()
    sponsors = models.CharField(max_length=200)
    meaner = models.ForeignKey('registration.user', on_delete=models.SET)



class Tag(models.Model):
    name = models.CharField(max_length=50)
