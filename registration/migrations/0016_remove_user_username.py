# Generated by Django 5.0 on 2023-12-16 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]