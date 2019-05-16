# Generated by Django 2.2 on 2019-04-30 10:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import volunteerJourney.models


class Migration(migrations.Migration):

    dependencies = [
        ('ngoJourney', '0001_initial'),
        ('volunteerJourney', '0002_auto_20190429_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='journey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ImageField(upload_to=volunteerJourney.models.get_image_path)),
                ('description', models.TextField()),
                ('feedback', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ngoJourney.events')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteerJourney.volunteer')),
            ],
        ),
        migrations.DeleteModel(
            name='ngo',
        ),
    ]