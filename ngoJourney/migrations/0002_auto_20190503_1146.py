# Generated by Django 2.2.1 on 2019-05-03 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngoJourney', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='long',
            new_name='lang',
        ),
    ]