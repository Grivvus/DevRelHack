# Generated by Django 5.0 on 2023-12-15 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_competition_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='tag',
        ),
        migrations.AddField(
            model_name='competition',
            name='tag',
            field=models.ManyToManyField(null=True, to='events.tag'),
        ),
    ]
