import uuid
from django.db import models

class Competition(models.Model):
    LEVEL_STATUS = (
        ('Университетский', 'Университетский'),
        ('Городской', 'Городской'),
        ('Областной', 'Областной'),
        ('Всероссийский', 'Всероссийский'),
        ('Международный', 'Международный')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200,
                            help_text='Название мероприятия', null=True)
    time_start = models.DateTimeField(null=True)
    time_end = models.DateTimeField(null=True)
    description = models.CharField(max_length=1000)
    tag = models.ManyToManyField('Tag')
    max_num_of_participants = models.IntegerField()
    level = models.CharField(max_length=200, choices=LEVEL_STATUS, blank=True)
    sponsors = models.CharField(max_length=200)
    meaner = models.ForeignKey('registration.user', on_delete=models.SET)

    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name