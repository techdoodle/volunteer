# Generated by Django 2.2.1 on 2019-05-03 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngoJourney', '0003_remove_ngo_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='eventName',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
    ]
