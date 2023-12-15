import uuid

from django.db import models

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, help_text='Имя Фамилия')
    email = models.CharField(max_length=200, help_text="user's email")
    phone = models.CharField(max_length=200, help_text="User's phone")
    password = models.IntegerField()
    registration_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Role(models.Model):
    ROLE = (
        ('DR', 'DevRel'),
        ('U', 'User')
    )
    role = models.CharField(max_length=2, choices=ROLE, default='U')
    userid = models.ForeignKey('User', on_delete=models.SET)

    def __str__(self):
        return self.role


class Characteristics(models.Model):
    specialization = models.CharField(max_length=50, null=True)
    level = models.CharField(max_length=50, null=True)
    competitions = models.CharField(max_length=200, null=True)
    userid = models.ForeignKey('User', on_delete=models.SET)
    is_agree_to_mailing = models.BooleanField(default=False)

    def __str__(self):
        return self.specialization
