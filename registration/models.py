import uuid, jwt
from datetime import datetime, timedelta

from django.db import models
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
PermissionsMixin)


class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if username is None:
            raise ValueError("Имя пользователя должно быть определено")
        if email is None:
            raise ValueError("Email пользователя должен быть определен")
        if password is None:
            raise ValueError("Пароль пользователя должен быть определен")
        user = self.model(name=username,
                           email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_admin(self, name, email, password):
        if name is None:
            raise ValueError("Имя пользователя должно быть определено")
        if email is None:
            raise ValueError("Email пользователя должен быть определен")
        if password is None:
            raise ValueError("Пароль пользователя должен быть определен")
        user = self.model(name=name,
                           email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    name = models.CharField(max_length=200, help_text='Имя Фамилия', null=True)
    email = models.EmailField(max_length=200, help_text="user's email",
                               unique=True)
    phone = models.CharField(max_length=200, help_text="User's phone")
    password = models.CharField(max_length=255)
    registration_time = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self) -> str:
        return self.email + ' ' + self.name

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': str(self.pk),
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token


class Role(models.Model):
    ROLE = (
        ('DR', 'DevRel'),
        ('U', 'User')
    )
    role = models.CharField(max_length=2, choices=ROLE, default='U')
    userid = models.ForeignKey('User', on_delete=models.SET)


class Characteristics(models.Model):
    specialization = models.CharField(max_length=50, null=True)
    level = models.CharField(max_length=50, null=True)
    competitions = models.CharField(max_length=200, null=True)
    userid = models.ForeignKey('User', on_delete=models.SET)
    is_agree_to_mailing = models.BooleanField(default=False)
