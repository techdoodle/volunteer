# Generated by Django 2.2.1 on 2019-05-05 09:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('volunteerJourney', '0005_auto_20190503_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='group',
            field=models.ManyToManyField(blank=True, related_name='groups', to='volunteerJourney.volunteer'),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]