# Generated by Django 5.0 on 2023-12-16 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_competition_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='level',
            field=models.CharField(blank=True, choices=[('Университетский', 'Университетский'), ('Городской', 'Городской'), ('Областной', 'Областной'), ('Всероссийский', 'Всероссийский'), ('Международный', 'Международный')], max_length=200),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
